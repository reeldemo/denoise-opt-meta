# DenoiseOpt paper v12: LaTeX layout

arXiv-style double-column preprint for the DenoiseOpt residual-scored hybrid RL+GA meta-search on wavetable **wrap-discontinuity** repair.

**Klaut paper id:** [`KLAUT_PAPER_ID.txt`](KLAUT_PAPER_ID.txt) (`unsupervised-wrap-discontinuity-repair-in-waveta-a2139527`).  
**Review merge log:** [`KLAUT_V12_REVIEW.md`](KLAUT_V12_REVIEW.md).

**Protocol (locked v10.1, carried into v12):** primary $R_{\mathrm{blend}}$ ($\alpha{=}0.7$) + latency objective $J$; Noise2Noise (`SeamN2N`) is the primary neural baseline/gate; DualCosine is classical appendix only. See [`EVAL_PROTOCOL.md`](EVAL_PROTOCOL.md).

**Baseline naming:** the unrepaired-engine control is **No-bake (passthrough)** ($x\mapsto x$). Legacy JSON key `identity` still appears in frozen artifacts (see [`NOMENCLATURE.md`](NOMENCLATURE.md)).

**Honesty:** holdout Ours $R_{\mathrm{blend}}{\approx}0.9697$ < Noise2Noise ${\approx}0.9750$; Dual Cosine ${\approx}0.541$. Transfer boards are wrap-protocol stress tests, not domain diagnosis SOTA.

## Build

Source file stays `main.tex`. The PDF basename is set by the compiler `-jobname` (not by `\title`).

```powershell
.\build.ps1
```

or:

```bash
JOB=Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v12
pdflatex -jobname=$JOB main.tex
pdflatex -jobname=$JOB main.tex
```

or `latexmk` (see `.latexmkrc`). Output:
`Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v12.pdf`.

## Figures

Sync from reelsynth `brand/artifacts/` after benches (dataset inventory, N2N vs Ours, transfer tables/plots), then rebuild PDF. Single-column figures use `width=\columnwidth`. Wide panels use `figure*` + `width=\textwidth`.
