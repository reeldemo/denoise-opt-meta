# Tasks: paper-v11-peer-review-response

T0 locked in `OPEN_DECISIONS.md` (2026-07-27). Implement status updated after T1–T14 execution.

| ID | Task | Depends | DoD | Status |
|----|------|---------|-----|--------|
| T0 | **Human gate:** accept `requirements.md` + answer open Q1–Q3 | — | Answers in `OPEN_DECISIONS.md` | **Done** |
| T1 | Create `REVIEW_RESPONSE.md`; map every Strength / Weakness / Suggestion + synopsis fact-check | T0 | AC-8.2 | **Done** |
| T2 | Synopsis correction: kill misleading \(R_{\mathrm{blend}}{\approx}0.99093\) as current; point to `tab:n2n-vs-ours` | T1 | AC-3.2 | **Done** |
| T3 | Clarity pass: acronyms; DualCosine centering vs objective; Related Work | T1 | AC-1.1–1.3 | **Done** |
| T4 | Modest contribution rewrite (abstract / contributions / conclusion) | T1 | AC-2.1–2.2 | **Done** |
| T5 | Transfer reframing (keep reframed per T0) | T0 | AC-4.1–4.3 | **Done** |
| T6 | Inventory prolonged-\(R\)-only boards → `METRIC_REGEN.md` | T2 | AC-3.3 | **Done** |
| T7 | Cheap \(R_{\mathrm{blend}}\) boards (transfer + cliff already scored; TeX synced) | T6 | AC-3.4 | **Done** (cheap path); full 5k = D1 |
| T8 | Param-count fairness: favorite Θ vs SeamN2N | T2 | AC-5.2 | **Done** (`tab:param-fairness`) |
| T9 | Error bars / CI where multi-seed exists; document gaps | T7 | AC-5.1 | **Done** (cliff ±; single-run honesty) |
| T10 | Search learning-curve figure (hybrid + Random); caption metric honesty | T2 | AC-6.1–6.3 | **Done** |
| T11 | Branch ablation table from ablate-* (prolonged \(R\), labeled) | T2 | AC-7.1 | **Done** (appendix; \(R_{\mathrm{blend}}\) ablations pending) |
| T12 | Limitations + Discussion aligned | T5, T7 | AC-3.1 | **Done** |
| T13 | Rebuild slug PDF; CHANGELOG; fill REVIEW_RESPONSE locations | T3–T12 | AC-8.1–8.2 | **Done** / in progress at ship |
| T14 | Commit + push denoise-opt-meta + reelsynth (touched paths only) | T13 | AC-8.3 | **Done** at ship |

## Deferred

| ID | Item | Why |
|----|------|-----|
| D1 | Full matched-5k outer-loop re-search under \(R_{\mathrm{blend}}\) | Needs explicit GPU budget (open Q2) |
| D2 | MOS/MUSHRA | Out of scope |
| D3 | Deep domain SOTA | Constitution |

## Suggested implement order

`T0 → T1 → T2 → T3∥T4 → T5 → T6 → T7 → T8∥T9 → T10∥T11 → T12 → T13 → T14`
