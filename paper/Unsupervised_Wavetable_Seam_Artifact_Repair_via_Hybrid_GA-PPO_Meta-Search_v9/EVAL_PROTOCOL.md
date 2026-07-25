# Evaluation protocol v10 (frozen metric lock)

**Date:** 25 July 2026 (paper v10 protocol)  
**Venue template:** arXiv twocolumn (`article` + `arxiv-twocolumn.sty`)  
**Claim scope:** cycle-local wavetable / wrap-seam artifact repair (not general speech enhancement)  
**Venue class:** DAFx / AES / arXiv cs.SD (not NeurIPS speech SOTA)

Supersedes v9 whole-curve prolonged \(R\) as the **search/champ primary**. Whole-curve \(R\) remains an optional debug JSON key.

## Metrics

| Role | Metric | Notes |
|------|--------|-------|
| **Primary (search / champ)** | Discontinuity-local \(R_{\mathrm{seam}}\in[0,1]\) | After prolong-tile (\(N{=}16\)), RMS only on wrap neighborhoods `SEAM_W=8` at each period head/tail. Same unit form as whole-curve \(R\): \(\mathrm{clamp}(1 - \mathrm{rms}_{\mathrm{seam}}/\mathrm{rms}_{\mathrm{ideal,seam}},0,1)\). Promotes prior edge-RMSE geometry. |
| **Search objective** | \(J = R_{\mathrm{seam}} - \lambda\cdot\mathrm{latency\_norm}\) | \(\lambda{=}0.02\), \(\mathrm{latency\_norm}=\log(1{+}t_{\mathrm{ms}})/\log(1{+}50)\). Timing folded into candidate eval (forward + \(R_{\mathrm{seam}}\)). |
| Champ gate (Phase 2) | Strictly beat frozen N2N holdout \(R_{\mathrm{seam}}\) | Corrupt→corrupt SeamN2N baseline. |
| Debug / optional | Whole-curve prolonged \(R\) | Legacy tiled RMS over all samples; not used for selection. |
| Secondary | SNR, SDR on tiled audio vs ideal | Required for strata matrices. |
| Seam diagnostic | \(\|x_0-x_{L-1}\|\) / wrap-jump | Report on engine and baked cycles. |
| Seam-local secondary | edge RMSE | RMS of `(out - ideal)` on `[0:W] ∪ [L-W:L]` (single-cycle). |
| Optional | click energy | Mean square first-diff across tiled wrap boundaries. |
| Out of scope (default) | PESQ, STOI, MUSHRA | Domain mismatch on non-speech cycles. |

## Baseline names

| Manuscript | Meaning | Legacy JSON key |
|------------|---------|-----------------|
| **Ideal sibling** \(r^{\star}\) | Cliff withheld; scoring target only | `ideal` |
| **No-bake (passthrough)** | Unrepaired cracked engine; score vs \(r^{\star}\) | `identity` |
| **Noise2Noise (primary)** | `SeamN2N` (~53.5k); corrupt→corrupt | `n2n` / `n2n_seam` |
| DualCosine | Raised-cosine end fades; classical appendix row | `dual_cosine` |
| Classical board | no-bake, DualCosine, FIR, poly, fades, VA residuals | various |

Searchable arch vocab includes `n2n_unet` (SeamN2N-parity scale/topology). Existing TinyUNet1D `"unet"` is **not** equivalent.

See also `NOMENCLATURE.md`.

## Comparison policy

- **Objective / reward:** maximize \(J\) (equivalently high \(R_{\mathrm{seam}}\) at modest latency). Closer to \(r^{\star}\) on wrap neighborhoods \(\Rightarrow\) larger \(R_{\mathrm{seam}}\) \(\Rightarrow\) better.
- **Near-ceiling regime:** no-bake often \(\approx 0.97\) on whole-curve \(R\); report \(R_{\mathrm{seam}}\) / \(J\) honestly under v10.
- **Primary reporting:** absolute \(R_{\mathrm{seam}}\) (and \(t_{\mathrm{ms}}\), \(J\)) of every method vs the same \(r^{\star}\).
- **Classical board (required):** always report learned/searched methods against non-AI rows (no-bake, DualCosine, `seam_fir3`, poly, fades, VA). DualCosine demoted from primary narrative comparator to classical appendix.
- **\(\Delta R_{\mathrm{seam}}\) vs DualCosine:** optional reporting gap; PPO may center advantages vs DualCosine \(R_{\mathrm{seam}}\), but DualCosine is not the reward target.

## Seeds and geometry

| Item | Value |
|------|-------|
| Holdout seed | `20260719` |
| Overnight search seed | `1902771841` |
| N2N train seed | `424242` (disjoint) |
| Seq train seed | `424243` (disjoint) |
| Cycle length \(L\) | 256 |
| Prolong tiles \(N\) | 16 |
| Seam width `SEAM_W` | 8 |
| Latency \(\lambda\) | 0.02 |
| Latency ref | 50 ms (norm denominator) |
| Score batch (tables) | 64 |
| Multi-seed spread | Five consecutive seeds starting at holdout |
| Cliff strata draw | 4096 tiles, seed `20260719` |
| Cliff cutoffs | wrap-jump p75 ≈ 1.387, p90 ≈ 1.832 (frozen in `cliff_strata.json`) |

## What we report (honesty)

- Frozen **canonical sine+cliff holdout** method scores under \(R_{\mathrm{seam}}\) / \(J\).
- Live overnight / meta campaign under v10 objective (`r_seam`, `t_ms`, `j` in checkpoints).
- **Hard-cliff strata** (top 25% / top 10% wrap-jump): no-bake / DualCosine / favorite / N2N / seq.
- **N2N baselines:** primary corrupt→corrupt under \(R_{\mathrm{seam}}\); secondary sibling-supervised; no holdout leakage.
- **Seq baselines:** LSTM + 1D CNN.
- **Wavetable-native realism:** ReelSynth factory (+ FX) + AKWF under wrap protocol.
- **Transfer domains:** CWRU, MFPT, MIT-BIH, PTB-XL 500 Hz subset, synth CNC, synth PMU — scored with \(R_{\mathrm{seam}}\) / \(J\) (re-run under v10; DualCosine-era whole-curve transfer searches cancelled).
- Do **not** claim unfinished larger budgets as complete mean-\(R\).
- Do **not** treat TinyUNet1D `"unet"` as SeamN2N.

## Waveform diversity target (Phase 3a)

\(\ge 20\) scored items spanning Rust `sound_bench` families and/or multi-seed `make_batch` variants.

**Landed:** (i) 20 Python generative family draws; (ii) 20 Rust `sound_bench` tiles; (iii) factory + OA wrap-protocol matrices. Residual gap: Python generative families are not byte-identical to Rust.

## Claim freeze

Adopt **narrow claims + deep extension**: title/abstract say seam / wrap discontinuity repair. Keep DenoiseOpt as method name. Demote “general audio denoising” to the periodic seam artifact class. Primary baseline narrative is Noise2Noise; DualCosine is classical appendix only.
