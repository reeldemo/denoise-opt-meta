# Tasks: paper-v8-review-response

Ordered implement checklist from [`design.md`](design.md) / [`requirements.md`](requirements.md).  
**Do not start T1+ until T0 DoD is satisfied.** Gates A–D accepted via user Build (2026-07-24).

| ID | Task | Depends | DoD |
|----|------|---------|-----|
| T0 | Write SDD artifacts: `docs/sdd/CONSTITUTION.md` + `specs/paper-v8-review-response/{requirements,design,tasks}.md` | — | Files exist; Gate A–D accepted (user Build 2026-07-24). **T0 DoD satisfied** once these four paths are present (this file completes the set). |
| T1 | **W0** Scaffold `paper/v8/` from v7; CHANGELOG / `paper/main.tex` pointer / TITLES; `REVIEW_RESPONSE.md` skeleton | T0 | `denoise-opt-meta/paper/v8/` exists with copied manuscript; pointer + CHANGELOG updated; REVIEW_RESPONSE skeleton present. Supports AC-5.1 (scaffold), AC-5.2 (skeleton). |
| T2 | **W3** Math + captions: formal $\Theta$, ideal sibling $G$, $\max R$; Fig.1/no-bake captions; Q1–Q2 rows | T1 | AC-2.1, AC-2.2, AC-2.3 checkable in `paper/v8/` + REVIEW_RESPONSE. |
| T3 | **W1** IMRaD Methods slim + overview TikZ + `appendix_algorithms.tex` (algs 1–9); display names; Abstract/Intro scope | T1 | AC-1.1, AC-1.2, AC-1.3. |
| T4 | **W2** Vibrato spectrogram script+figure; hear panel + WAV citation; compact WT gallery from existing exports; transfer appendix | T1 | AC-3.1, AC-3.2, AC-3.3, AC-3.4. Artifacts under `reelsynth/brand/artifacts/vibrato_spectrogram/` + figures in `paper/v8/figures/`; no new NAS; no wipe of `meta_approach_compare/`. |
| T5 | **W4** HP ±50% OAT sensitivity (500 iters, seed `1902771841`) → `meta_hp_sensitivity/`; table/figure; Q3 | T1 | AC-4.1, AC-4.2, AC-4.3. Script `reelsynth/scripts/bench_meta_hp_sensitivity.py`; honest sensitivity label (not full 5k re-search). |
| T6 | **W5** Results/Discussion/Limitations; rebuild `paper/v8/main.pdf`; complete REVIEW_RESPONSE; mirror README → v8; commit+push both repos | T2, T3, T4, T5 | AC-5.1, AC-5.2, AC-5.3. No formal A/B listening claim; no deep-SOTA transfer claim. |
| T7 | **sdd-analyze** + **checklist** vs constitution/requirements/design | T6 | `analyze.md` + `checklist.md` under this spec dir; no critical drift; all AC checked pass/fail. |

## Human gates

| Gate | Status |
|------|--------|
| A Constitution | Accepted (user Build, 2026-07-24) |
| B Requirements | Accepted (user Build, 2026-07-24) |
| C Design (+ grill locks) | Accepted (user Build, 2026-07-24) |
| D Tasks | Accepted (user Build, 2026-07-24) |

**Unlock:** Implement **T1–T7** (W0–W5 + analyze/checklist) may start immediately. Do **not** implement until the agent session assigned to implement begins; this Phase-1 session stops at T0.

## Deferred / out of scope (do not schedule)

- Formal human listening study / formal A/B scores
- Deep SOTA CWRU/ECG baselines
- Wiping or re-running publishable 5k `meta_approach_compare/`
- Full 5k re-search per HP perturbation
- DAW plugin / S7 host I/O
- New NAS runs for WT diversity gallery

## Grill locks (must honor in T4–T5)

1. **HP:** 500 iters × one-at-a-time ±50% on key Table-2 HPs; seed `1902771841`; out → `reelsynth/brand/artifacts/meta_hp_sensitivity/`; label as sensitivity not full re-search.
2. **Listening:** spectrogram + hear WAVs + paper panel; formal study OUT OF SCOPE; no formal A/B claim.
3. **WT diversity:** compact gallery from existing ReelSynth/AKWF exports / `real_wt_matrix.json`; no new NAS.
