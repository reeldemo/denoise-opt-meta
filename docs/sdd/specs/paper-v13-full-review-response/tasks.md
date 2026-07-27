# Tasks: paper-v13-full-review-response

Ordered implementation tasks. Each must pass its ACs before the next starts, unless marked parallel.

## T1 — Scaffold v13 folder [DONE]

Copy v12 to v13 slug. Update `build.ps1` jobname, `main.tex` header, CHANGELOG.

**ACs:** v13 folder exists; `build.ps1` jobname updated.

## T2 — Verify/patch bench scripts for R_blend scoring [PARALLEL with T3]

Audit `bench_meta_approaches_5k.py` scoring path. Confirm FitCell and champion selection use R_blend, not prolonged R. Add `--eval-seed` to holdout bench scripts where missing.

**ACs:** AC-1.1 (R_blend scoring confirmed); holdout scripts accept `--eval-seed`.

## T3 — Narrative rewrite (abstract, intro, methods) [PARALLEL with T2]

Rewrite abstract (AC-3.1), contributions list (AC-3.2), and expand R_blend/J definitions in methods (AC-4.1, AC-4.2). Consolidate disclaimers (AC-3.4). Reframe transfer (AC-5.1, AC-5.2).

**ACs:** AC-3.1, AC-3.2, AC-3.4, AC-4.1, AC-4.2, AC-5.1, AC-5.2.

## T4 — Run multi-seed outer-loop search (D1)

Execute `bench_meta_approaches_5k.py` with seeds 1902771841, 2026072701, 2026072702 (5k iters each, all 6 approaches).

**ACs:** AC-1.1–AC-1.4.

**Gate:** GPU compute (~8h/seed).

## T5 — Run multi-seed holdout evaluation

Evaluate frozen champions on 5 holdout seeds. Run `bench_sota_matrix.py`, `bench_canonical_eval_dataset.py`, `bench_cliff_strata.py`, `bench_v10_n2n_vs_ours.py` per seed.

**ACs:** AC-2.1, AC-2.4.

## T6 — Aggregate statistics

Write `scripts/aggregate_multiseed_stats.py`. Compute mean/std, win-rate, sign test. Emit `multiseed_summary.json`.

**ACs:** AC-2.3 (sign test p-value computed).

## T7 — Update tables and results narrative

Replace single-freeze tables with multi-seed mean +/- std. Restructure results section (AC-3.3). Insert win-rate and sign-test results.

**ACs:** AC-2.2, AC-2.3, AC-3.3.

## T8 — Build, audit, push

Build PDF (AC-6.1). Klaut English audit (AC-6.2). Update REVIEW_RESPONSE.md (AC-6.4). Commit and push both repos (AC-6.3).

**ACs:** AC-6.1–AC-6.4.

## Parallel plan

```
T1 ──> T2 ──> T4 ──> T5 ──> T6 ──> T7 ──> T8
  └──> T3 (parallel with T2–T4) ──────────┘
```
