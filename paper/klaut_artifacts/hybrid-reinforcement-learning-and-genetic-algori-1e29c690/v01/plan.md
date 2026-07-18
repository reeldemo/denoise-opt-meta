# Paper plan: Hybrid Reinforcement Learning and Genetic Algorithms for Meta-Learning Audio Denoising

_Source: **template** · created 2026-07-18T17:34:42.498245+00:00_

## User needs
Write excellent CS/DSP Introduction and Literature Landscape.
Frame as generic audio signal denoising; wavetable/periodic wrap crackle is motivating instance.
Hybrid RL+GA meta-learning outer loop. Numbered falsifiable contributions.
Literature thematic with Used vs Screened. Cite with \cite{key} only from attached keys.
No invented final overnight results — note experiments ongoing.
Do not dump JSON. Full academic paragraphs.

## Abstract sketch
Periodic discontinuities in cyclic audio frames inject broadband crackle under wrap-around playback. We treat cycle-local seam restoration as an instance of audio signal denoising and search denoising operators with a hybrid meta-learning outer loop that interleaves genetic-algorithm population updates with reinforcement-learning architecture proposals, scored by a prolonged residual objective without paired clean waveforms. Large-scale GPU experiments are ongoing; this draft establishes the problem framing and literature landscape.

## Writing mode hint
Write full academic paragraphs (IMRaD / CS–DSP). Prefer precise claims tied to ingested metrics and PDF analyses. Cite with \cite{cite_key} only for attached refs. Distinguish used vs screened literature. Do not invent numbers or references. Mark template-mode output if no LLM is used. Screened-relevant count: 11.

## Literature count: 36

## Open data gaps
- `baseline_comparison`
- `baselines`
- `hyperparameters`
- `method_definition`
- `metrics`
- `protocol`
- `table_rows`
- `trial_budget`

## Sections

### `abstract` — Abstract
- **IMRaD role:** abstract
- **Target words:** ~180
- **Goal:** Concise problem–method–result–limitation summary with the key numeric headline (primary metric and baseline comparison).
- **Claims:**
  - State the scientific problem in one sentence.
  - Name the method and evaluation protocol.
  - Report the primary quantitative finding vs baseline.
- **Citation slots:** lehtinen2018 [method]: Noise2Noise: Learning Image Restoration without Clean Data, jaderberg2017 [method]: Population Based Training of Neural Networks, khadka2018 [method]: Evolution-Guided Policy Gradient in Reinforcement Learning
- **Data still needed:** `baseline_comparison`

### `introduction` — Introduction
- **IMRaD role:** introduction
- **Target words:** ~450
- **Goal:** Motivate the problem, situate it in prior practice, state contributions as falsifiable claims, and preview the paper.
- **Claims:**
  - Why the phenomenon matters scientifically or practically.
  - Gap in existing proxies / methods.
  - Explicit numbered contributions.
- **Citation slots:** lehtinen2018 [used]: Noise2Noise: Learning Image Restoration without Clean Data, jaderberg2017 [used]: Population Based Training of Neural Networks, khadka2018 [used]: Evolution-Guided Policy Gradient in Reinforcement Learning, real2019 [used]: Regularized Evolution for Image Classifier Architecture Sear, pdf_analyses (36 grounded)

### `related_work` — Related Work
- **IMRaD role:** related_work
- **Target words:** ~500
- **Goal:** Organize prior art by theme; distinguish used vs screened literature; end with how this work differs.
- **Claims:**
  - Group citations thematically (not as a dump).
  - State what was screened out and why.
- **Citation slots:** lehtinen2018 [used]: Noise2Noise: Learning Image Restoration without Clean Data, jaderberg2017 [used]: Population Based Training of Neural Networks, khadka2018 [used]: Evolution-Guided Policy Gradient in Reinforcement Learning, real2019 [used]: Regularized Evolution for Image Classifier Architecture Sear, engel2020 [used]: DDSP: Differentiable Digital Signal Processing, elsken2019 [used]: Neural Architecture Search: A Survey, pham2018 [used]: Efficient Neural Architecture Search via Parameter Sharing, schulman2017 [used]: Proximal Policy Optimization Algorithms, finn2017 [screened]: Model-Agnostic Meta-Learning for Fast Adaptation of Deep Net, liu2019 [screened]: DARTS: Differentiable Architecture Search, dfossez2021 [screened]: Hybrid Spectrogram and Waveform Source Separation, kong2021 [screened]: DiffWave: A Versatile Diffusion Model for Audio Synthesis, dfossez2019 [screened]: Demucs: Deep Extractor for Music Sources with extra unlabele, pascual2017 [screened]: SEGAN: Speech Enhancement Generative Adversarial Network, theme:general → lehtinen2018, jaderberg2017, khadka2018, real2019, theme:MAML model-agnostic meta-learning → behl2019, alsaleh2024, nguyen2021, chen2025, theme:Wave-U-Net audio source separation → luo2019, jansson2017, macartney2018, nakamura2020, theme:Noise2Noise unsupervised denoising → mansour2023, qiu2021, pdf_analyses (36 grounded)

### `methods` — Methods
- **IMRaD role:** methods
- **Target words:** ~650
- **Goal:** Define notation, model/operator, objective(s), and search procedure so a reader could reimplement the essentials.
- **Claims:**
  - Formal definition of the primary score / loss.
  - Algorithmic procedure (outer/inner loops if any).
  - Implementation constraints that affect validity.
- **Citation slots:** lehtinen2018 [method]: Noise2Noise: Learning Image Restoration without Clean Data, jaderberg2017 [method]: Population Based Training of Neural Networks, khadka2018 [method]: Evolution-Guided Policy Gradient in Reinforcement Learning
- **Data still needed:** `method_definition`, `hyperparameters`

### `experiments` — Experiments
- **IMRaD role:** experiments
- **Target words:** ~350
- **Goal:** Describe protocol: datasets/seeds, trial budget, validation sizes, baselines, and selection rules before revealing outcomes.
- **Claims:**
  - Protocol is fixed before reporting winners.
  - Baselines and ablations are named.
- **Data still needed:** `protocol`, `trial_budget`, `baselines`

### `results` — Results
- **IMRaD role:** results
- **Target words:** ~450
- **Goal:** Present primary metrics with table(s) and figure(s); report effect sizes vs baselines; avoid overclaiming.
- **Claims:**
  - Primary metric ranking with uncertainty or held-out N.
  - Secondary metrics that check for failure modes.
- **Figures:** primary_comparison
- **Tables:** benchmark_matrix
- **Data still needed:** `metrics`, `table_rows`

### `discussion` — Discussion
- **IMRaD role:** discussion
- **Target words:** ~400
- **Goal:** Interpret results relative to hypotheses; reconcile surprising outcomes (e.g. which prior won); connect to related work.
- **Claims:**
  - What the evidence supports.
  - What it does not support.
- **Citation slots:** lehtinen2018 [compare]: Noise2Noise: Learning Image Restoration without Clean Data, jaderberg2017 [compare]: Population Based Training of Neural Networks, khadka2018 [compare]: Evolution-Guided Policy Gradient in Reinforcement Learning, real2019 [compare]: Regularized Evolution for Image Classifier Architecture Sear, engel2020 [compare]: DDSP: Differentiable Digital Signal Processing, pdf_analyses (36 grounded)

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
