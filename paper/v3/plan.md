# Paper plan: DenoiseOpt: Residual Scoring and Bi-Level Meta-Learning for Wavetable Wrap Crackle

_Source: **template** · created 2026-07-18T08:41:43.827735+00:00_

## User needs
Short technical paper. Honest about evo_explore winning over nested loss opt under residual. Cite used vs screened literature. Include equation for residual. Primary numbers: 0.824 vs 0.698 (delta +0.126). Paper version v3 via scientific workflow.

## Abstract sketch
Open wrap seams in periodic wavetable cycles inject audible crackle under cyclic playback. DenoiseOpt is a seam-local bake stack $f_\theta$, $\theta\in[0,1]^{12}$, scored without paired clean labels. We replace wrap-energy quality $Q$ as the outer meta objective with a prolonged residual score $R\in[0,1]$ (1~=~best): the engine's tiled DenoiseOpt cycle is compared to an ideal multi-period reference from the same seed with open-wrap cliffs withheld ($N{=}16$). The outer loop also nests an inner unsupervised loss fit $L=(1-\mathcal{D})+\lambda(1-\mathcal{S})$. Across 1500 literature-informed trials, Meta Top~1 \texttt{evo\_explore\_515} reaches residual $\approx 0.824$ vs naive DualCosine $\approx 0.698$ on held-out validation ($N{=}2000$)---a clear $+0.126$ margin---while keeping $\mathcal{S}\approx 1.0$. Nested loss-opt priors were searched but did not dominate the residual elite set; wide evolutionary mutation did.

## Writing mode hint
Write full academic paragraphs (IMRaD). Prefer precise claims tied to ingested metrics. Do not invent numbers. Mark template-mode output if no LLM is used.

## Literature count: 10

## Open data gaps
- `baseline_comparison`
- `baselines`
- `hyperparameters`
- `method_definition`
- `protocol`

## Sections

### `abstract` — Abstract
- **IMRaD role:** abstract
- **Target words:** ~180
- **Goal:** Concise problem–method–result–limitation summary with the key numeric headline (primary metric and baseline comparison).
- **Claims:**
  - State the scientific problem in one sentence.
  - Name the method and evaluation protocol.
  - Report the primary quantitative finding vs baseline.
- **Citation slots:** optional domain anchors
- **Data still needed:** `baseline_comparison`

### `introduction` — Introduction
- **IMRaD role:** introduction
- **Target words:** ~450
- **Goal:** Motivate the problem, situate it in prior practice, state contributions as falsifiable claims, and preview the paper.
- **Claims:**
  - Why the phenomenon matters scientifically or practically.
  - Gap in existing proxies / methods.
  - Explicit numbered contributions.
- **Citation slots:** foundational domain refs

### `related_work` — Related Work
- **IMRaD role:** related_work
- **Target words:** ~500
- **Goal:** Organize prior art by theme; distinguish used vs screened literature; end with how this work differs.
- **Claims:**
  - Group citations thematically (not as a dump).
  - State what was screened out and why.
- **Citation slots:** used_refs, screened_refs

### `methods` — Methods
- **IMRaD role:** methods
- **Target words:** ~650
- **Goal:** Define notation, model/operator, objective(s), and search procedure so a reader could reimplement the essentials.
- **Claims:**
  - Formal definition of the primary score / loss.
  - Algorithmic procedure (outer/inner loops if any).
  - Implementation constraints that affect validity.
- **Citation slots:** methodological priors
- **Data still needed:** `method_definition`, `hyperparameters`

### `experiments` — Experiments
- **IMRaD role:** experiments
- **Target words:** ~350
- **Goal:** Describe protocol: datasets/seeds, trial budget, validation sizes, baselines, and selection rules before revealing outcomes.
- **Claims:**
  - Protocol is fixed before reporting winners.
  - Baselines and ablations are named.
- **Data still needed:** `protocol`, `baselines`

### `results` — Results
- **IMRaD role:** results
- **Target words:** ~450
- **Goal:** Present primary metrics with table(s) and figure(s); report effect sizes vs baselines; avoid overclaiming.
- **Claims:**
  - Primary metric ranking with uncertainty or held-out N.
  - Secondary metrics that check for failure modes.
- **Figures:** primary_comparison
- **Tables:** benchmark_matrix

### `discussion` — Discussion
- **IMRaD role:** discussion
- **Target words:** ~400
- **Goal:** Interpret results relative to hypotheses; reconcile surprising outcomes (e.g. which prior won); connect to related work.
- **Claims:**
  - What the evidence supports.
  - What it does not support.
- **Citation slots:** interpretive anchors

### `limitations` — Limitations
- **IMRaD role:** limitations
- **Target words:** ~220
- **Goal:** State validity threats, metric proxies, and compute budgets honestly.
- **Claims:**
  - At least three concrete limitations.

### `conclusion` — Conclusion
- **IMRaD role:** conclusion
- **Target words:** ~180
- **Goal:** Restate contributions and headline numbers; point to artifacts.
- **Claims:**
  - One-paragraph takeaway with primary metric.
