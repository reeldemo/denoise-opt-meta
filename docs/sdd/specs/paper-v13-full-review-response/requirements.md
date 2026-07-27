# Requirements: paper-v13-full-review-response

## Problem

v12 answers the peer review's clarity and metric-lock concerns but still runs single-seed experiments and uses defensive framing. v13 closes Deferred D1 (matched-5k outer-loop re-search under R_blend with multiple seeds), adds multi-run statistics (mean/std, win-rate, sign test), rewrites the narrative to be assertive, and cleans up appendix/math definitions.

**Canonical paper:** `paper/Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v13/`
**Companion code:** `reelsynth` benches/scripts.
**Constitution:** `docs/sdd/CONSTITUTION.md` (unchanged).

## User stories

### US-1 — Multi-seed outer-loop re-search (Deferred D1)

As an author, I want the matched-5k meta-approach bake-off re-run under locked R_blend with multiple search seeds so the paper reports reproducible search statistics, not a single lucky freeze.

**Acceptance criteria**

- AC-1.1: `bench_meta_approaches_5k.py` runs under R_blend (not prolonged R) for 5,000 iterations with at least 3 distinct search seeds.
- AC-1.2: All 6 approaches (random, cmaes, reinforce, aging_evo, tpe, hybrid_lstm) complete per seed.
- AC-1.3: Artifacts land in `brand/artifacts/meta_approach_compare_v13_rblend/<seed>/` with `history.jsonl` and `checkpoint.json` per approach.
- AC-1.4: Champion R_blend per approach reported as mean +/- std across seeds.

### US-2 — Multi-seed holdout evaluation

As a reviewer, I want primary tables to report mean +/- std over multiple holdout seeds, not a single frozen draw.

**Acceptance criteria**

- AC-2.1: Frozen champions + N2N + classical baselines evaluated on at least 5 holdout seeds under R_blend.
- AC-2.2: Tables `tab:n2n-vs-ours`, `tab:canonical-methods`, `tab:sota-main` show mean +/- std.
- AC-2.3: Multi-family board reports win-rate (Ours vs N2N) and a nonparametric test (sign test or Wilcoxon signed-rank) with p-value.
- AC-2.4: Cliff strata table includes multi-seed error bars.

### US-3 — Assertive narrative rewrite

As an author, I want the paper to read as confident and honest, centering the ideal-sibling protocol and hard-cliff robustness, without repeated self-negation.

**Acceptance criteria**

- AC-3.1: Abstract leads with DSP problem, ideal-sibling protocol, hybrid search, multi-seed results. Contains one scope statement; no other "not X" disclaimers.
- AC-3.2: Contributions list is positive: (1) cycle-local seam restoration, (2) unsupervised ideal-sibling protocol, (3) applied hybrid search, (4) open multi-seed evaluation.
- AC-3.3: Results section leads with multi-seed holdout, then multi-family edge, then hard-cliff advantage.
- AC-3.4: All repeated novelty-deflation caveats consolidated into Limitations.

### US-4 — Math and metric clarity

As a reader, I want R_blend, J, and the N2N gate fully defined with explicit RMS formulas, not shorthand.

**Acceptance criteria**

- AC-4.1: `sec:residual-score` spells out R_seam and R_body with explicit numerator/denominator and mask.
- AC-4.2: One compact role-summary (table or list): R_blend = reporting, J = search selection, N2N gate = holdout pass/fail.
- AC-4.3: Prolonged R labeled superseded/debug everywhere it appears.

### US-5 — Transfer sections reframed

As a reviewer, I want transfer boards justified as wrap-protocol stress tests with per-domain seam analogies.

**Acceptance criteria**

- AC-5.1: One clear paragraph: transfer = same wrap discontinuity protocol on other periodic signals, not domain diagnosis SOTA.
- AC-5.2: Per-domain seam analogy in <=1 sentence each.
- AC-5.3: Table honest about OOD footnotes and blocked rows.

### US-6 — Ship v13

As a maintainer, I want a buildable v13 PDF, Klaut English audit pass, and complete review response.

**Acceptance criteria**

- AC-6.1: PDF builds via `build.ps1`.
- AC-6.2: Klaut English audit score >= 4.5/5.
- AC-6.3: CHANGELOG entry; both repos committed and pushed.
- AC-6.4: `REVIEW_RESPONSE.md` updated for v13.

## Out of scope

- Formal MOS/MUSHRA / human listening panel.
- Deep domain SOTA on CWRU/ECG/Paderborn under clinical metrics.
- New foundational RL/NAS algorithm proofs.
- Wiping `meta_approach_compare/` or inventing R_blend by renaming prolonged R.

## Open questions

None — all decisions resolved (multi-seed = 3 search seeds + 5 holdout seeds; transfer = keep reframed; full SDD).
