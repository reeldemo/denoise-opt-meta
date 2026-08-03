# Prose audit log — v11 manuscript

**Date:** 27 July 2026  
**Scope:** Main body (`main.tex`, `subsections/*.tex` except appendix)  
**Rules:** No em dashes, no semicolon stacks in prose, no “y, not x” contrast slop, narrow claims, repair-operator / no-bake nomenclature preserved.

---

## Abstract (`main.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Opening problem + method | **FAIL → fixed** | Removed bloggy “heal the signal” / “click noise artifact” stack. Tightened to seam-local repair without paired clean recordings. |
| Baselines + transfer | **FAIL → fixed** | Split semicolon stack (“Noise2Noise; transfer boards further probe cross-domain travel”) into two sentences. |
| Results + contribution | **FAIL → fixed** | Replaced semicolon between N2N miss and Dual Cosine score. Dropped “stay robust”. Stated holdout gap honestly. |

---

## Introduction (`introduction.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Opening (L4–7) | **PASS** | Clear seam definition and cyclic click geometry. |
| Terminology list | **FAIL → fixed** | Split “seam is local; signal is whole waveform” semicolon. Clarified outer-loop item (avoid “giant net” slop). |
| Problem framing (L19–20) | **PASS** | $R_{\mathrm{blend}}$ and $J$ scoped correctly. |
| Four roles | **PASS** | Nomenclature aligned with NOMENCLATURE.md. |
| Prior work paragraph (L46–50) | **PASS** | Calm citations, no hype. |
| Key findings | **FAIL → fixed** | Replaced “Contribution in one line:” with “In summary,”. Split historical-score semicolon into two sentences. |
| Transfer datasets | **PASS** | Scoped as stress test; diagnosis SOTA excluded. |
| Contributions enum | **PASS** | Numbered, concrete. |

---

## Related Work (`related_work.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Discontinuity / DDSP | **FAIL → fixed** | Removed “operators, not end-to-end vocoders” semicolon slop. Two sentences. |
| Label-free restoration | **PASS** | N2N and screened Demucs/DiffWave stated plainly. |
| Compact waveform operators | **FAIL → fixed** | “design priors, not frozen…” → positive framing. |
| Search / hybrids | **PASS** | Dense but accurate. |
| Used vs screened | **PASS** | Bullet-style summary OK. |

---

## Methods (`methods.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Notation + symbols table | **PASS** | Repair operator $\Theta$ defined; table clear. |
| Ideal sibling | **PASS** | Sibling relationship explicit; not a method output. |
| $R_{\mathrm{blend}}$ + objective | **PASS** | No convergence theater; N2N gate stated. |
| Four roles (no-bake) | **FAIL → fixed** | Removed triple “Not $r^{\star}$, not …” stack. Clarified passthrough vs perceptual score. |
| Classical board / DualCosine remark | **PASS** | Advantage centering scoped to PPO only. |
| Search pipeline / hyperparams | **PASS** | Near-ceiling shaping explained without hype. |
| Meta-compare | **PASS** | NOMENCLATURE display names used. |

---

## Experiments (`experiments.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Locked protocol | **PASS** | Seeds, metrics, venue stated. |
| Dataset creation | **PASS** | Generator geometry and no-bake gloss present. |
| Multi-family / stats | **PASS** | Board sizes and disjoint seeds clear. |
| Search campaign / baselines | **PASS** | Historical vs v10.1 lock distinguished. |

---

## Results (`results.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Reading guide | **PASS** | Points to $R_{\mathrm{blend}}$ primary tables. |
| v10 freeze / N2N vs Ours | **PASS** | Holdout gate failure stated upfront. |
| Family hardness | **PASS** | “Hard sounds recur.” telegraphic but acceptable. |
| Classical vs favorite | **FAIL → fixed** | “do-nothing reference, not the ideal” → clearer passthrough wording. |
| Cliff strata | **PASS** | Identity-$R$ explanation and edge RMSE present. |
| VA seam baselines | **FAIL → fixed** | Dropped informal “Honest reading:” lead-in. |
| Transfer / Rust | **PASS** | Win-rates and gaps honest. |

---

## Results transfer (`results_transfer.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Setup reminder | **PASS** | Historical $R$ vs $R_{\mathrm{blend}}$ flagged. |
| Takeaways | **FAIL → fixed** | Replaced `---` em-dash slop (lines 99, 102) with periods. Split semicolon stack on BeatDiff. |

---

## Discussion (`discussion.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Main story | **FAIL → fixed** | Removed “useful reading is not X. It is: Y” contrast stack. Replaced with “operative claim is narrower.” |
| Hard families | **FAIL → fixed** | Split semicolon between hard/easy family lists. |
| Search near ceiling | **PASS** | Plateau adaptation without SOTA claims. |
| Evidence beyond tiles | **PASS** | Listening informal; transfer scoped. |

---

## Limitations (`limitations.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Bullet list | **PASS** | Honesty notes collected; negations are scope boundaries (acceptable). |
| Future work | **PASS** | Family-stratified follow-up framed narrowly. |

---

## Conclusion (`conclusion.tex`)

| Paragraph | Verdict | Notes |
|-----------|---------|-------|
| Full section | **FAIL → fixed** | Split holdout/N2N semicolon. Removed “not speech-enhancement SOTA” slop ending. Positive narrow claim instead. |

---

## Appendix

| Section | Verdict | Notes |
|---------|---------|-------|
| Algorithms / supplement | **SKIP** | Pseudocode and auto-generated tables; no main-body prose changes. |

---

## Top fixes (severity order)

1. Abstract: removed hype/opening slop and semicolon stack on baselines/transfer.
2. Discussion: removed “not X / It is Y” contrast stack on the main claim.
3. Methods no-bake: removed triple-negative identity clarification.
4. `results_transfer.tex`: replaced em-dash (`---`) prose joins.
5. Conclusion: removed “not speech SOTA” ending; split semicolon.
6. Related work: split DDSP semicolon; reframed waveform-operator negation.
7. Introduction: terminology semicolon + informal “Contribution in one line”.
8. Results canonical table: clearer no-bake vs ideal sibling wording.
9. Results VA section: dropped “Honest reading:” throat-clearing.
10. Abstract: “stay robust” → “remain competitive”; explicit holdout ordering.

---

## Build

Rebuild with `build.ps1` after edits.

---

## Semicolon pass (27 July 2026)

Full grill of prose `;` stacks: see [`PROSE_SEMICOLON_AUDIT_v11.md`](PROSE_SEMICOLON_AUDIT_v11.md).

- **62** prose semicolon sites rewritten (periods / commas / two sentences).
- Keywords, math `\Theta(x;h)`, algorithm `\State`, TikZ, and table `---` missing cells kept.
- Priority body + experiments + transfer/listening captions cleaned. Science and nomenclature unchanged.
