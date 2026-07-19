# Method pseudocode

Algorithms used in DenoiseOpt hybrid meta-learning. Notation matches paper v7 /
`reelsynth` overnight GPU search. LaTeX Algorithms in `paper/v7/subsections/methods.tex`
mirror this file.

## Prolonged residual score

```
function ResidualScore(ideal_cycle, engine_cycle, periods=16):
    I ← Tile(ideal_cycle, periods)
    Y ← Tile(engine_cycle, periods)
    r_rms ← RMS(Y − I)
    i_rms ← max(RMS(I), ε)
    return clamp(1 − r_rms / i_rms, 0, 1)
```

## DualCosine baseline

```
function DualCosine(engine_cycle):
    fade ends of the cycle with raised-cosine windows of width SEAM_W
    return ResidualScore(ideal_sibling, faded_cycle)
```

## MoE soft gating

```
function MoEMix(cycle, experts, gate_logits):
    w ← softmax(gate_logits)
    y ← Σ_k w[k] · experts[k](cycle)
    return y
```

## Seam-cell forward (bake denoise)

```
function ApplyOps(cycle, cell, ops):
    x ← cycle
    for op in ops:
        if op is FIR:      x ← Conv1D(x, fir_taps)
        if op is fade/pull/polish/pin: x ← SeamLocalEdit(x, op)
        if op is cycle_net / mlp_seam: x ← WriteSeam(x, cell(PackSeam(x)))
        if op uses composed blocks: x ← cell.forward_cycle(x)  # U-Net/attn/…
        if op is moe_mix: x ← MoEMix(x, cell.experts, cell.gate_logits)
    return x
```

## Fit one architecture until convergence

```
function FitCell(cfg, steps, batch):
    cell ← SeamCell(cfg)
    opt ← Adam(cell.params)
    prev ← null
    patience ← 0
    for t = 1..steps:
        ideal, eng ← MakeBatch(batch)          # or procedural family batch
        out ← ApplyOps(eng, cell, cfg.ops)
        R ← mean ResidualScore(ideal, out)
        loss ← 1 − R  (+ optional tiny adv aux)
        if finite(loss): AdamStep(opt, loss)
        if prev ≠ null and |prev−R|/max(|prev|,ε) < 1e−4:
            patience ← patience + 1
            if patience ≥ 3: break
        else: patience ← 0
        prev ← R
    return cell, R
```

## GA tournament step

```
function GATournamentStep(pop, k=3, p_c=0.7, p_m=0.3):
    sample k genomes; parents ← top-2 by R
    child ← Crossover(parents) with prob p_c else clone elite
    Mutate(child) with rate p_m   # ops, depth, cell type, θ box
    FitCell(child); insert into pop (replace worst if full)
    return pop
```

## PPO architecture update

```
function PPOArchUpdate(policy, clip_ε=0.2):
    a ← sample mutate action from actor (edit ops / hparams)
    FitCell(proposed cfg); ρ ← R − DualCosineBaseline
    Â ← advantage from critic
    r ← π(a)/π_old(a)
    update actor with clipped surrogate min(rÂ, clip(r,1−ε,1+ε)Â)
    return policy
```

## PBT exploit–mutate

```
function PBTExploitMutate(pop, quantile=1/3, σ=0.2):
    rank pop by R
    for each bottom member:
        copy hparams from a top-quantile elite
        multiply hparams by (1 + σ·noise)
        brief refit; write back
    return pop
```

## Outer hybrid loop (PPO + GA + PBT + NAS)

```
function HybridMetaSearch(iters, pop_size):
    pop ← InitPopulation(pop_size)             # random deep-biased arch genomes
    policy ← ActorCritic()                     # PPO over mutate actions
    champ ← WarmStartBestFitted() or null
    boredom ← 0
    for it = 1..iters:
        branch ← Rotate(ppo, ga, pbt, nas, combo)
        cfg, hp ← Propose(branch, pop, policy, plateau_state)
        cell, R_fit ← FitCell(cfg, hp.fit_steps)
        R_eval ← EvalCell(cell)
        R ← 0.5·R_fit + 0.5·R_eval + DepthMixtureBonus(cfg)
        UpdatePopulation(pop, cfg, R)
        PPOUpdate(policy, reward = R − DualCosineBaseline)
        if R > champ.R:
            champ ← (cfg, cell, R); boredom ← 0
        else:
            boredom ← boredom + 1
        if boredom ≥ 1000:
            PlateauAdapt(deeper=true, crazier_mix=true, more_GA_PBT=true)
            boredom ← 0
        LogHistory(it, R, champ.R, branch)
    return champ
```

## Plateau adapt (deeper first)

```
function PlateauAdapt(level):
    MAX_SEARCH_DEPTH ← MAX_SEARCH_DEPTH + 2·level
    bump population genome depths upward
    raise P(moe_mix), P(unet+attn+dilated+…)
    raise GA/PBT/NAS proposal weight; lower HOLD
    log PLATEAU_ADAPT deeper=true depth=…
```

## Inference-time selection (same score band)

```
function PickFavorite(fitted_models, tol):
    champ_R ← max residual among models
    band ← { m : |m.R − champ_R| ≤ tol }
    for m in band:
        m.latency ← MedianTime(Forward(m, fixed_batch))
    return argmin_latency( argmax_R(band) )
```
