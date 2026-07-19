# Evaluation protocol v1 (frozen)

**Date:** 19 July 2026 (peer-review strata extension)  
**Venue template:** arXiv twocolumn (`article` + `arxiv-twocolumn.sty`)  
**Claim scope:** cycle-local wavetable / wrap-seam artifact repair (not general speech enhancement)  
**Venue class:** DAFx / AES / arXiv cs.SD (not NeurIPS speech SOTA)

## Metrics

| Role | Metric | Notes |
|------|--------|-------|
| Primary | Prolonged residual $R\in[0,1]$ | $1$ = best. Tiled RMS ratio vs ideal sibling. |
| Secondary | SNR, SDR on tiled audio vs ideal | Required for Phase 3a matrices. |
| Seam-specific | $\|x_0-x_{L-1}\|$ / wrap-jump | Report on engine and baked cycles. |
| Optional seam-local | edge RMSE | RMS of `(out - ideal)` on indices `[0:W] ∪ [L-W:L]`. |
| Optional seam-local | click energy | Mean square first-diff across tiled wrap boundaries. |
| Out of scope (default) | PESQ, STOI, MUSHRA | Domain mismatch on non-speech cycles. Explicitly deferred in Limitations: no invented PESQ on sine tiles; MUSHRA not run (needs humans). Speech-proxy secondary only if OA speech snippets are imported and labeled. |

## Seeds and geometry

| Item | Value |
|------|-------|
| Holdout seed | `20260719` |
| Overnight search seed | `1902771841` |
| N2N train seed | `424242` (disjoint) |
| Seq train seed | `424243` (disjoint) |
| Cycle length $L$ | 256 |
| Prolong tiles $N$ | 16 |
| Seam width `SEAM_W` | 8 |
| Score batch (tables) | 64 |
| Multi-seed spread | Five consecutive seeds starting at holdout |
| Cliff strata draw | 4096 tiles, seed `20260719` |
| Cliff cutoffs | wrap-jump p75 ≈ 1.387, p90 ≈ 1.832 (frozen in `cliff_strata.json`) |

## What we report (honesty)

- Frozen **canonical sine+cliff holdout** method scores (`method_scores.json`).
- Live overnight campaign at the **5k clean-iteration gate** (`results_blob_5k.json`): champion $R$ vs DualCosine on the runner geometry.
- **Hard-cliff strata** (top 25% / top 10% wrap-jump): identity / DualCosine / favorite / N2N / seq (`cliff_strata.json`).
- **N2N baselines:** primary corrupt→corrupt; secondary sibling-supervised; no holdout leakage (`n2n_baseline.json`).
- **Seq baselines:** LSTM + 1D CNN (`seq_baseline.json`).
- **Wavetable-native realism:** ReelSynth-style factory (primary) + OA instrument-like (secondary) under wrap protocol (`real_wt_matrix.json`). No LibriSpeech/MUSDB.
- Do **not** claim unfinished larger budgets as complete mean-$R$.
- Do **not** resurrect long-horizon “tables remain open” narrative.
- Do **not** claim wrap-closure or hybrid-search convergence theorems.

## Waveform diversity target (Phase 3a)

$\ge 20$ scored items spanning Rust `sound_bench` families and/or multi-seed `make_batch` variants.

**Landed:** (i) 20 Python generative family draws (primary SOTA matrix); (ii) 20 Rust `sound_bench` tiles via `export_sound_bench_tiles` (secondary transfer table); (iii) factory + OA wrap-protocol matrices. Residual gap: Python generative families are not byte-identical to Rust. Rust export closes the “no Rust tiles in the matrix” gap for $\ge 20$ waveforms.

## Claim freeze

Adopt **narrow claims + deep extension**: title/abstract say seam / wrap discontinuity repair. Keep DenoiseOpt as method name. Demote “general audio denoising” to the periodic seam artifact class.
