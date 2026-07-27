# Klaut v12 review merge — DenoiseOpt

**Paper id:** `unsupervised-wrap-discontinuity-repair-in-waveta-a2139527`  
**Klaut artifact root:** `li-lang/klaut_artifacts/.../v01/`  
**Science pass:** `reviews/pass_20260727T045538Z` (aggregate: **revise**; mean prior_work 1.33, validity 2.0)  
**English polish:** subsections rewritten in Klaut `v01/` (score 1.0 → **3.2**)  
**Post-polish audit:** `english_audit/pass_20260727T045828Z` (score **3.2**; critical=0, major=3 rhythm, minor=2)

## English merge policy

Klaut polish often collapsed short sentences into semicolon / em-dash walls and rewrote figure hrefs back to the **v11** folder slug.  
Canonical v12 keeps:

- short-sentence prose (no semicolon/em-dash slop),
- **v12** GitHub figure / EVAL_PROTOCOL paths,
- repair-operator nomenclature and Ours < N2N honesty on holdout $R_{\mathrm{blend}}$.

Accepted English: terminology wording, mild rhythm splits (methods / results learning-curve note), algorithm indent, grammar (`listening remains`), abstract unsupervised clarification merged into `main.tex` abstract environment (not a separate `\input`).

Rejected English: paragraph-wall merges in conclusion / ethics / experiments / limitations; v11 path rewrites.

## Science must-fix (from peer review)

| Ask | Decision | Where |
|-----|----------|--------|
| Clarify **unsupervised** (no studio-clean pairs; ideal sibling = procedural cliff-withheld twin for scoring) | **Accepted** | Abstract; Intro ¶Unsupervised; Methods ideal-sibling |
| Transfer = **stress test**, not domain diagnosis | **Accepted** (strengthened) | Intro Transfer; Experiments `sec:transfer-protocol` already stated; one more explicit sentence |
| Abstract holdout numbers (Ours≈0.9697, N2N≈0.9750, DualCosine≈0.541) | **Already present** / kept | `main.tex` abstract |
| Foundational wavetable / VA cites (stilson / nam / esqueda only — OA in bib) | **Accepted** | Related Work paragraph retitled + one foundation sentence |
| No formal verification claims | **Accepted** | Tooling: “checked … not formal verification”; Scope already denies wrap-closure / convergence theorems |
| THD+N / dB / MOS tables | **Rejected inventing** | Limitations: no THD+N; PESQ/MOS out; note existing SNR/SDR on strata boards |
| Undefined external resources (“Klaut Research Gateway”) | **Accepted** | Acknowledgments → OpenAlex/Crossref/arXiv + Tooling cross-ref |
| Broken `PENDING_RBLEND.md` pointer | **Accepted** | Limitations → `METRIC_REGEN.md` only |

## Deferred (honest)

- Full matched-$5$k outer-loop **re-search** under $R_{\mathrm{blend}}$ (Deferred D1).
- Invented THD+N / MOS / perceptual dB-click tables.
- Extra OA wavetable textbooks beyond stilson/nam/esqueda (constitution: OA-only bib).
- Second English audit via MCP (score already ≥3; optional).

## Build

`.\build.ps1` → `Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v12.pdf`
