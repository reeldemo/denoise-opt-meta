# DenoiseOpt paper v14 — FitCell-to-convergence follow-up

**Parent:** v13 (Deferred D1 matched-$5$k complete).  
**New:** hybrid-only FitCell-to-plateau campaign after D1 ranked hybrid best.

## Headline numbers (honest)

| Item | Value |
|------|------:|
| D1 hybrid (3-seed short FitCell) | $0.9748{\pm}0.0018$ |
| Converge seed `1902771841` (750/750) | $R_{\mathrm{blend}}{=}0.9912$ (clears N2N gate $0.9750$) |
| Converge seed `2026072701` | paused at $170/750$, live $R{=}0.9895$ |
| Converge seed `2026072702` | pending |

Artifacts: `reelsynth/brand/artifacts/meta_approach_compare_v14_converge/`  
JSON: `figures/v14_hybrid_converge_results.json`

## Why hybrid-only

D1 six-way bake-off under locked $R_{\mathrm{blend}}+J$ put hybrid ahead of Random/CMA/TPE/Aging/REINFORCE. Further GPU goes to deeper FitCell on that winner, not re-running losers.

## Build

```powershell
.\build.ps1
```

## Klaut

Reuse / re-register paper id from v13 when auditing; see `KLAUT_PAPER_ID.txt`.
