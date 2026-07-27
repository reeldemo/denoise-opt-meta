# Review response map — v13

Extends v11/v12 responses. Canonical PDF: this folder via `build.ps1`.

## Multi-seed statistics (new in v13)

| Request | Status | Location |
|---------|--------|----------|
| Multi-run holdout mean±std | **Done** (5 seeds) | Table `tab:n2n-vs-ours`; `figures/multiseed_summary.json` |
| Multi-family win-rate / sign test | **Done** | Results §n2n-vs-ours; mean win frac 0.47, sign $p{=}1.0$ |
| Matched-5k re-search under $R_{\mathrm{blend}}$ (D1) | **Running** | `reelsynth/brand/artifacts/meta_approach_compare_v13_rblend/` (3 seeds) |

## Narrative / clarity

| Request | Status |
|---------|--------|
| Assertive abstract/intro; fewer "not X" | Done |
| Explicit $R_{\mathrm{seam}}$/$R_{\mathrm{body}}$ RMS | Done (`eq:R-component`) |
| Role summary ($R_{\mathrm{blend}}$, $J$, N2N gate) | Done |
| Disclaimers → Limitations | Done |
| Transfer keep reframed | Done (unchanged policy) |

## Locked honesty

- Holdout: Ours $0.971{\pm}0.001$ < N2N $0.977{\pm}0.001$ on all 5 seeds.
- Dual Cosine $0.542{\pm}0.038$.
- Multi-family Ours edges on mean-of-means only; do not claim majority wins across seeds.
