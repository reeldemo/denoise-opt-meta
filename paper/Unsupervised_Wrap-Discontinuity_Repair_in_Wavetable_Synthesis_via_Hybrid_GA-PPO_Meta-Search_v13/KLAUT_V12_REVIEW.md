# Klaut v12 review merge — DenoiseOpt

**Paper id:** `unsupervised-wrap-discontinuity-repair-in-waveta-a2139527`  
**Klaut artifact root:** `li-lang/klaut_artifacts/.../v01/`  
**Science pass:** `reviews/pass_20260727T045538Z` (aggregate: **revise**; mean prior_work 1.33, validity 2.0)  
**English (final):** heuristics score **5.0 / 5** (maps to **10 / 10** on a doubled scale; Klaut max is 5)  
**Final audit pass:** written under `english_audit/` after rhythm + abstract pass (0 critical / 0 major / 0 minor)

## Score scale note

Klaut English audit is **0–5**, not 0–10. Target “8–10” ≈ **≥4.0** (`good_enough`) to **5.0**. This cycle lands at **5.0**.

## English work this cycle

- Varied sentence length in abstract, conclusion, ethics, experiments, transfer recipe, learning-curve, VA scores.
- Kept science locks: Ours holdout $R_{\mathrm{blend}}{\approx}0.9697$ < N2N ${\approx}0.9750$; Dual Cosine ${\approx}0.541$; no invented THD+N/MOS.
- Klaut heuristic update (gateway): strip `itemize` / `enumerate` / `algorithm` bodies before rhythm checks (definition lists and pseudocode were false metronome positives).

## English merge policy

Klaut LLM polish often collapsed short sentences into semicolon / em-dash walls and rewrote figure hrefs back to the **v11** folder slug.  
Canonical v12 keeps:

- short-sentence prose (no semicolon/em-dash slop),
- **v12** GitHub figure / EVAL_PROTOCOL paths,
- repair-operator nomenclature and Ours < N2N honesty on holdout $R_{\mathrm{blend}}$.

## Science must-fix (from peer review)

| Ask | Decision | Where |
|-----|----------|--------|
| Clarify **unsupervised** (no studio-clean pairs; ideal sibling = procedural cliff-withheld twin for scoring) | **Accepted** | Abstract; Intro ¶Unsupervised; Methods ideal-sibling |
| Transfer = **stress test**, not domain diagnosis | **Accepted** (strengthened) | Intro Transfer; Experiments `sec:transfer-protocol` |
| Abstract holdout numbers (Ours≈0.9697, N2N≈0.9750, DualCosine≈0.541) | **Kept** | `main.tex` abstract |
| Foundational wavetable / VA cites (stilson / nam / esqueda) | **Accepted** | Related Work |
| No formal verification claims | **Accepted** | Tooling / Scope |
| THD+N / dB / MOS tables | **Rejected inventing** | Limitations |
| Broken `PENDING_RBLEND.md` pointer | **Accepted** | → `METRIC_REGEN.md` |

## Deferred (honest)

- Full matched-$5$k outer-loop **re-search** under $R_{\mathrm{blend}}$ (Deferred D1).
- Invented THD+N / MOS / perceptual dB-click tables.
- Extra OA wavetable textbooks beyond stilson/nam/esqueda (constitution: OA-only bib).

## PDF

`Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v12.pdf`
