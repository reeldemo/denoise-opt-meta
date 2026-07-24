# DenoiseOpt paper: LaTeX layout

arXiv-style double-column preprint for the DenoiseOpt residual-scored hybrid RL+GA meta-search on wavetable seam restoration.

**Baseline naming:** the unrepaired-engine control is **No-bake (passthrough)** ($x\mapsto x$). Legacy JSON key `identity` still appears in frozen artifacts — see [`NOMENCLATURE.md`](NOMENCLATURE.md).

## Revision plan (checklist)

See [`MANUSCRIPT_CHECKLIST_IMPLEMENTATION_PLAN.md`](MANUSCRIPT_CHECKLIST_IMPLEMENTATION_PLAN.md) for the Phase 0–6 plan against the Manuscript Checklist Review (triage of REAL vs FALSE FAIL, ambitious SOTA/Methods extension, narrow claims).

## Build

```bash
pdflatex main.tex
pdflatex main.tex
```

## Bibliography policy (OA-only)

Every `\bibitem` must have a downloadable open-access PDF.
Catalog + fetcher:

```bash
python scripts/fetch_oa_pdfs.py
```

PDFs land in `artifacts/literature_oa/pdfs/`. Inventory: `artifacts/literature_oa/REFERENCES_OA.md`.

## Figures

Regenerate search learning curves and dataset distribution plots (one command):

```powershell
powershell -File paper/v8/regen_search_figures.ps1
```

## Style

`article` + `twocolumn` + lean local `arxiv-twocolumn.sty`.
Title/abstract span both columns via `\twocolumn[{...}]`.
Single-column figures use `width=\columnwidth`. Wide panels use `figure*` + `width=\textwidth`.
