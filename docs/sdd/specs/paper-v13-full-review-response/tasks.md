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

## T4 — Run multi-seed outer-loop search (D1) [IN PROGRESS]

Execute `bench_meta_approaches_5k.py` with seeds 1902771841, 2026072701, 2026072702 (5k iters each, all 6 approaches).
Launcher: `reelsynth/scripts/launch_v13_multiseed_search.ps1` → `brand/artifacts/meta_approach_compare_v13_rblend/`.

**ACs:** AC-1.1–AC-1.4 (partial until all seeds finish).
**Gate:** GPU compute (~days wall for full 3×6×5k).

## T5 — Run multi-seed holdout evaluation [DONE]

Five holdout seeds evaluated. Summary in `holdout_multiseed_v13/multiseed_summary.json`.

**ACs:** AC-2.1, AC-2.4.

## T6 — Aggregate statistics [DONE]

`scripts/aggregate_multiseed_stats.py` wrote mean/std, win-rate, sign test.

**ACs:** AC-2.3.

## T7 — Update tables and results narrative [DONE pending D1 curves]

Multi-seed holdout numbers in Results / Intro / Conclusion. Learning-curve figure refresh waits on D1 seed completion.

**ACs:** AC-2.2, AC-2.3, AC-3.3 (holdout side).

## T8 — Build, audit, push [IN PROGRESS]

PDF built via `build.ps1`. Commit/push both repos. Klaut English audit optional follow-up.

## Parallel plan

```
T1 ──> T2 ──> T4 ──> T5 ──> T6 ──> T7 ──> T8
  └──> T3 (parallel with T2–T4) ──────────┘
```
