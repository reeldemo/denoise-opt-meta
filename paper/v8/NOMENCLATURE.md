# Nomenclature — baselines and controls

| Manuscript name | Meaning | Legacy JSON / code key |
|-----------------|---------|------------------------|
| **Ideal sibling** $r^{\star}$ | Same generator draw with open-wrap cliff **withheld**. Scoring target only — not a method. | `ideal` |
| **No-bake (passthrough)** | Unrepaired cracked engine $x$; then score $R(x,r^{\star})$. $f(x)=x$; no seam op. | `identity` |
| DualCosine | Raised-cosine end fades on the cracked engine (classical bake + search reward ref.) | `dual_cosine` |
| `seam_fir3` / poly / VA | Other classical (non-AI) repairs on the same $x\to R(\cdot,r^{\star})$ protocol | various |
| Favorite / meta favorite | DenoiseOpt hybrid-search champion bake graph | `favorite` |

## Meta-approach comparison labels

Code keys in `meta_approach_compare/` stay stable; **manuscript / table / plot legends** use the short display names below.

| Code key | Manuscript name | What the reader should understand |
|----------|-----------------|-----------------------------------|
| `random` | **Random NAS** | Uniform iid draws over bake graphs + fit HPs (control). |
| `cmaes` | **Cont. CMA-ES** | Diagonal CMA-ES on a continuous encoding of depth/width/blocks/fit HPs. |
| `reinforce` | **Arch REINFORCE** | Vanilla policy gradient on discrete architecture-edit actions (no PPO clip). |
| `aging_evo` | **Aging evolution** | Regularized evolution with oldest-member replacement (Real et al.). |
| `tpe` | **TPE Bayes NAS** | Tree-structured Parzen estimator over discrete bake categoricals. |
| `hybrid_lstm` | **Ours (hybrid GA–PPO)** | Multi-branch GA+PPO+PBT+NAS+combo; LSTM/xLSTM in vocab; co-tunes reward mode + fit/PPO HPs. |

Avoid bare `hybrid_lstm` / “(+LSTM)” in prose — readers cannot tell it is the proposed method.
Keep artifact folder names and JSON `approach` fields as the code keys.

## What is scored against what

```
cracked engine x  --Θ-->  baked y  --ResidualScore-->  R vs ideal sibling r*
                      (no-bake: Θ = identity)
```

- **Ideal sibling** = target (cliff off).
- **No-bake** = do nothing to $x$, still score vs $r^{\star}$.
- Beating no-bake = closer to $r^{\star}$ than the unrepaired engine.

## Comparison policy

Always rank learned methods on **absolute $R$** vs the full classical non-AI board (no-bake, DualCosine, FIR, poly, fades, VA).
**Reward / objective** = maximize $R$ toward the ideal sibling (best $R{=}1$).
$\Delta R$ vs DualCosine is one classical reporting gap; PPO may center $\rho{=}R-R_{\mathrm{DualCosine}}$, but DualCosine is not the reward.

## Why rename `identity` → no-bake

Reviewers read “identity” as (i) residual-net identity skips, (ii) “what is this method’s identity,” or (iii) a learned identity map.
In this paper it only ever meant **leave the cracked engine unchanged**.
Use **no-bake** / **No-bake (passthrough)** in prose and tables; keep reading `identity` from frozen artifacts.
