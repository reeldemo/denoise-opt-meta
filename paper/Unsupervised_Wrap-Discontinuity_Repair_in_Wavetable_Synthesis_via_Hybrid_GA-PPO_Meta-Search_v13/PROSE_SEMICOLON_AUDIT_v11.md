# Prose semicolon audit — v11

**Date:** 27 July 2026  
**Rules:** `MANUSCRIPT_REVIEW_FIX_PLAN.md` / `PEER_REVIEW_IMPROVEMENT_PLAN.md` Global Constraints — no em-dash slop, no semicolon stacks in prose, no “y, not x” contrast slop. Grill each `;` for readability.  
**Nomenclature preserved:** repair operator, seam = wrap join, no-bake, beat/outperform (not crush).

---

## Count

| Category | Count |
|----------|------:|
| **Prose `;` fixed** (rewritten to periods, commas, or two sentences) | **62** |
| **Kept** (keywords, math `\Theta(x;h)`, algorithm `\State`/`\If`, TikZ `;`, table `---` missing cells, comments) | remaining inventory clean |

Post-pass `rg ';'` on v11 `*.tex` shows only keep-list hits.

---

## KEEP (intentional)

- `\keywords{...; ...}` in `main.tex`
- Math: `y=\Theta(x;h)`, `\Theta(\cdot;h)`, `\Theta(x;\theta)`
- Algorithmic `\State` / `\If` pseudocode separators in `appendix_algorithms.tex`
- TikZ statement terminators in `arch_diagram.tex`
- Table missing-score marker `---` (not prose em dash)
- Comment-only lines

---

## Top before → after (grill examples)

1. **Intro pitch/timbre stack**  
   - Before: `Pitch is set by how fast the pointer advances; timbre comes from the stored shape…`  
   - After: two sentences.

2. **Transfer diagnosis scope**  
   - Before: `…(Table~\ref{tab:transfer-main}); deep diagnosis baselines remain out of scope.`  
   - After: two sentences.

3. **Related-work “Used: A; B; C; D.”**  
   - Before: semicolon-separated citation dump.  
   - After: prose list with commas and “and”.

4. **Wilcoxon vs no-bake**  
   - Before: long sentence ending `…[0.155,0.170]$); vs no-bake the multifamily mean gap…`  
   - After: DualCosine Wilcoxon sentence, then separate vs-no-bake sentence.

5. **No-bake gloss**  
   - Before: `(passthrough; unrepaired engine vs $r^{\star}$)`  
   - After: `(passthrough, unrepaired engine vs $r^{\star}$)`.

6. **Methods FitCell / selection**  
   - Before: `FitCell minimizes $1-R_{\mathrm{blend}}$; selection and champion updates use $J$.`  
   - After: two sentences.

7. **VA roles stack**  
   - Before: `…value step at wrap; BLAMP corrects…; DualCosine fades…`  
   - After: three short sentences.

8. **Tooling verification**  
   - Before: `…assisted preparation; the authors verified…`  
   - After: two sentences.

9. **Limitations primary/secondary**  
   - Before: `The Python multi-family matrix is primary; Rust export is secondary.`  
   - After: two sentences.

10. **Transfer takeaways CNC / Paderborn**  
    - Before: `Ours near $0.992$; SeamN2N only recovers…` / `…$0.4710$; an architecture-reuse…`  
    - After: split into separate sentences.

---

## Files touched

`introduction.tex`, `related_work.tex` (prior + this pass), `methods.tex`, `experiments.tex`, `experiments_transfer.tex`, `experiments_eval_listening.tex`, `results.tex`, `results_transfer.tex`, `results_eval_listening.tex`, `results_hp_sensitivity.tex`, `results_transfer_latency.tex`, `limitations.tex`, `tooling.tex`, `ethics.tex`, `appendix_algorithms.tex` (narrative only), `appendix_supplement.tex`, `figures/meta_approaches_table.tex`.

Em-dash prose: none remaining outside table missing-cell `---`.

---

## Rebuild

`.\build.ps1` → slug PDF.
