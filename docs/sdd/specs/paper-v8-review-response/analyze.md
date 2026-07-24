# Analyze: paper-v8-review-response

Drift check of implementation vs [`requirements.md`](requirements.md), [`design.md`](design.md), and [`CONSTITUTION.md`](../../CONSTITUTION.md).  
Date: 2026-07-24. Task: T7 after T6 ship.

## Constitution compliance

| § | Principle | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Honesty over hype | OK | Abstract/Intro/Discussion/Limitations: no speech enhancement / no deep-SOTA CWRU/ECG |
| 2 | OA-only bibliography | OK | Unchanged OA `\bibitem` set in `paper/v8/main.tex` |
| 3 | Canonical metric truth | OK | Methods: ideal sibling $G$, no-bake ≠ ideal, $\max R$, DualCosine = PPO centering only |
| 4 | Primary claim = cycle-local WT seam | OK | Abstract + App.~\ref{app:transfer-pilot} classical-board disclaimer |
| 5 | Reproducibility; never wipe compare | OK | `meta_hp_sensitivity/` + `vibrato_spectrogram/` sibling dirs; `meta_approach_compare/` intact |
| 6 | Review completeness | OK | `paper/v8/REVIEW_RESPONSE.md` — every W/Q/S row filled (no TBD) |
| 7 | Cross-repo hygiene | OK | CHANGELOG v8; pointer `paper/main.tex`; reelsynth mirror README → v8 |

## Requirements AC drift

| AC | Expected | Observed | Drift? |
|----|----------|----------|--------|
| AC-1.1 | Algs 1–9 appendix; slim Methods + overview | `appendix_algorithms.tex` + `methods.tex` + `arch_diagram.tex` | None |
| AC-1.2 | Display names; objective vs DualCosine separate | Methods Rem. DualCosine centering; display names in meta table | None |
| AC-1.3 | Abstract/Intro match constitution scope | Explicit no speech / no deep SOTA | None |
| AC-2.1 | Formal $\Theta$, $G$ cliff on/off | Methods Notation / Ideal sibling | None |
| AC-2.2 | $\max R$; Q1–Q2 in Methods + REVIEW_RESPONSE | eqs + REVIEW_RESPONSE Q1–Q2 rows | None |
| AC-2.3 | Fig.1 / no-bake captions | Captions distinguish no-bake / DualCosine / ideal / Ours | None |
| AC-3.1 | Vibrato script + figure in `paper/v8/figures/` | `bench_vibrato_spectrogram.py`; `fig_vibrato_spectrogram.{png,pdf}` | None |
| AC-3.2 | Hear panel + WAV path | `results_eval_listening.tex`; WAVs under `hear_samples/` | None |
| AC-3.3 | Transfer appendix + classical disclaimer | `appendix_transfer_pilot.tex` | None |
| AC-3.4 | Fold 5k meta; no re-run | v7 JSON/figures retained; compare tree not wiped | None |
| AC-4.1 | `meta_hp_sensitivity/` seed `1902771841` | STATUS `all_complete` 11/11; REPRO_MANIFEST | None |
| AC-4.2 | Table/figure; Q3 answered | `tab_meta_hp_sensitivity.tex`, `fig_meta_hp_sensitivity.png`, Results para | None |
| AC-4.3 | Do not modify compare tree | Sensitivity writes only under `meta_hp_sensitivity/` | None |
| AC-5.1 | `main.pdf` + CHANGELOG + pointer + TITLES | 23 pp PDF; CHANGELOG/TITLES/main.tex pointer | None |
| AC-5.2 | REVIEW_RESPONSE every review item | All W/Q/S rows have v8 locations | None |
| AC-5.3 | Mirror README v8; both repos pushed | README updated; commits/pushes in T6/T7 ship | None (verify remotes after push) |

## Design / grill locks

| Lock | Honored? |
|------|----------|
| HP: 500 iters, OAT ±50%, seed `1902771841`, sensitivity label | Yes |
| Listening: spectrogram + WAVs + panel; no formal A/B claim | Yes |
| WT diversity: existing exports only; no new NAS | Yes |
| No wipe `meta_approach_compare/` | Yes |

## Critical drift

**None.** Implementation matches locked design and ACs.

## Minor notes (non-blocking)

- PDF grew to 23 pages after W2/W4 figure inserts (expected).
- HP table footnote for incomplete runs removed after 11/11 completion.
- Dual-repo push status is part of AC-5.3 verification at commit time.
