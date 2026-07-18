# Literature grounding notes (PDF-backed)

Generated from OA arXiv PDFs under `paper/v4/pdfs/` with text extraction.
Use only for claims supported by these snippets; do not invent citations.

## Used (method / design anchors)

### lehtinen2018n2n — Noise2Noise
- **PDF:** `pdfs/lehtinen2018n2n.pdf`
- **Grounding:** Label-free restoration: train from corrupted pairs without clean targets.
- **Relevance:** Motivates unsupervised residual scoring without paired “clean” wavetable cycles.

### engel2020ddsp — DDSP
- **PDF:** `pdfs/engel2020ddsp.pdf`
- **Grounding:** Differentiable DSP modules as interpretable audio synthesizer components.
- **Relevance:** Places seam-local bake operators in the broader differentiable / modular audio DSP landscape (not end-to-end waveform nets).

### jaderberg2017pbt — Population Based Training
- **PDF:** `pdfs/jaderberg2017pbt.pdf`
- **Grounding:** Asynchronous population that jointly optimizes models and hyperparameters; discovers schedules rather than a single fixed hyperparameter set.
- **Relevance:** Informs lit-combo / exploit–mutate overnight branch design.

### snoek2012bo — Practical Bayesian Optimization
- **PDF:** `pdfs/snoek2012bo.pdf`
- **Grounding:** Bayesian optimization for expensive ML hyperparameters.
- **Relevance:** Literature prior family for local Bayesian search (not claimed as the overnight winner).

### elsken2019nas — Neural Architecture Search survey
- **PDF:** `pdfs/elsken2019nas.pdf`
- **Grounding:** Taxonomy of NAS methods; search space / strategy / evaluation trade-offs.
- **Relevance:** Frames discrete seam-op DAG + cell search as application-specific NAS.

### pham2018enas — ENAS
- **PDF:** `pdfs/pham2018enas.pdf`
- **Grounding:** RL controller with parameter sharing for efficient NAS.
- **Relevance:** Conceptual ancestor of RL proposing architecture edits (our overnight RL branch uses residual reward, not ImageNet controllers).

### liu2019darts — DARTS
- **PDF:** `pdfs/liu2019darts.pdf`
- **Grounding:** Continuous relaxation of architecture search.
- **Relevance:** Contrasted approach — we keep discrete ops + small MLP/FIR cells, scored by prolonged residual R.

### zhang2007moead — MOEA/D
- **PDF:** `pdfs/zhang2007moead.pdf`
- **Grounding:** Decomposition-based multi-objective evolutionary algorithm.
- **Relevance:** Informs multi-objective cues in lit-combo priors (shape vs residual).

## Screened (on-topic but not methodological dependencies)

### finn2017maml — MAML
- **PDF:** `pdfs/finn2017maml.pdf`
- **Why screened:** Inspirational bi-level / fast-adaptation framing; we do **not** backprop through a deep task network. Nested loss fit is coordinate descent on θ, outer rank by R.

### shan2021diffwave — DiffWave (Kong et al.; filename legacy)
- **PDF:** `pdfs/shan2021diffwave.pdf` (arXiv 2009.00713)
- **Note:** This PDF is DiffWave diffusion vocoder, not Shan differentiable wavetable. Kept as audio generative context; **not** a DenoiseOpt operator dependency.
- Cite carefully as Kong et al. DiffWave if used at all; prefer Engel DDSP for DSP lineage.

## Classical audio (cited from prior paper versions; not all OA PDFs here)
- Välimäki VA / Esqueda aliasing & BLAMP — discontinuity control lineage for wrap seams.
- These remain domain anchors from v3; OA PDF harvest prioritized ML/NAS/meta sources for RL overnight.
