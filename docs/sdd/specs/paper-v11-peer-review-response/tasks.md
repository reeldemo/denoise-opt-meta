# Tasks: paper-v11-peer-review-response

| ID | Task | Depends | DoD |
|----|------|---------|-----|
| T0 | **Human gate:** accept `requirements.md` + answer open Q1–Q3 (transfer policy, regen budget, venue rigor) | — | Answers recorded at top of this file or in `OPEN_DECISIONS.md` |
| T1 | Create `paper/..._v11/REVIEW_RESPONSE.md` skeleton; map every Strength / Weakness / Suggestion + synopsis fact-check | T0 | Every pasted review bullet has a row (AC-8.2) |
| T2 | Synopsis correction pass: kill any reader-facing \(R_{\mathrm{blend}}{\approx}0.99093\) as current; point to `tab:n2n-vs-ours` | T1 | AC-3.2; grep clean for misleading blend claims |
| T3 | Clarity pass: acronyms on first use; DualCosine centering vs objective; Related Work motivation | T1 | AC-1.1–1.3 |
| T4 | Modest contribution rewrite (abstract / contributions / conclusion) | T1 | AC-2.1–2.2 |
| T5 | Transfer reframing paragraphs (or appendix move / delete per T0) | T0 | AC-4.1–4.3 |
| T6 | Inventory prolonged-\(R\)-only boards; write regen list with exact scripts | T2 | Markdown inventory in REVIEW_RESPONSE or `METRIC_REGEN.md` (AC-3.3) |
| T7 | Regen cheap \(R_{\mathrm{blend}}\) boards per T0 budget; update tex/figures | T6 | Real JSON + tex; no invented scores (AC-3.4) |
| T8 | Param-count fairness: favorite Θ vs SeamN2N in Results | T2 | AC-5.2 |
| T9 | Error bars / CI on primary \(R_{\mathrm{blend}}\) tables where multi-seed exists; document gaps | T7 | AC-5.1 |
| T10 | Search learning-curve figure (hybrid + Random); caption metric honesty | T2 | AC-6.1–6.3; figure in `figures/` |
| T11 | Branch ablation table/figure from ablate-* or bounded re-run | T2 | AC-7.1 |
| T12 | Limitations + Discussion aligned with metric lock + transfer policy | T5, T7 | AC-3.1 |
| T13 | Rebuild slug PDF; CHANGELOG; fill remaining REVIEW_RESPONSE locations | T3–T12 | AC-8.1–8.2 |
| T14 | Commit + push denoise-opt-meta + reelsynth (scripts/artifacts only as needed) | T13 | AC-8.3; clean status on touched paths |

## Deferred

| ID | Item | Why |
|----|------|-----|
| D1 | Full matched-5k outer-loop re-search under \(R_{\mathrm{blend}}\) | Needs explicit GPU budget (open Q2) |
| D2 | MOS/MUSHRA | Out of scope |
| D3 | Deep domain SOTA | Constitution |

## Suggested implement order

`T0 → T1 → T2 → T3∥T4 → T5 → T6 → T7 → T8∥T9 → T10∥T11 → T12 → T13 → T14`
