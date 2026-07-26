# DenoiseOpt paper v11: LaTeX layout

arXiv-style double-column preprint for the DenoiseOpt residual-scored hybrid RL+GA meta-search on wavetable seam restoration.

**Protocol (locked v10.1, carried into v11):** primary $R_{\mathrm{blend}}$ ($\alpha{=}0.7$) + latency objective $J$; Noise2Noise (`SeamN2N`) is the primary neural baseline/gate; DualCosine is classical appendix only. See [`EVAL_PROTOCOL.md`](EVAL_PROTOCOL.md).

**Baseline naming:** the unrepaired-engine control is **No-bake (passthrough)** ($x\mapsto x$). Legacy JSON key `identity` still appears in frozen artifacts (see [`NOMENCLATURE.md`](NOMENCLATURE.md)).

## Build

Source file stays `main.tex`. The PDF basename is set by the compiler `-jobname` (not by `\title`).

```powershell
.\build.ps1
```

or:

```bash
JOB=Unsupervised_Wavetable_Seam_Artifact_Repair_via_Hybrid_GA-PPO_Meta-Search_v11
pdflatex -jobname=$JOB main.tex
pdflatex -jobname=$JOB main.tex
```

or `latexmk` (see `.latexmkrc`). Output:
`Unsupervised_Wavetable_Seam_Artifact_Repair_via_Hybrid_GA-PPO_Meta-Search_v11.pdf`.

## Figures

Sync from reelsynth `brand/artifacts/` after benches (dataset inventory, N2N vs Ours, transfer tables/plots), then rebuild PDF.Single-column figures use `width=\columnwidth`. Wide panels use `figure*` + `width=\textwidth`.
