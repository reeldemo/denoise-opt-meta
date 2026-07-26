# Appendix stub — sci/eng wrap-heal transfer pilot

**Date:** 20260725T123816Z

Pilot transfer of DenoiseOpt’s winning outer loop (**hybrid GA–PPO / `hybrid_lstm`**) to public cycle-local wrap tasks (CWRU, MIT-BIH, PTB-XL; MFPT if available; synthetic CNC/PMU proxies when OA downloads are blocked). Period length $L=256$; score = prolonged residual $R$ vs ideal sibling.

## Results (prolonged $R$, higher better)

### cwru_bearings

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9623 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `cot_linear_periodize` | 0.8451 | bearings classical bad-COT control (passthrough of linear resample) |
| `no_bake` | 0.8451 | classical / passthrough |
| `endpoint_pin_mean` | 0.5054 | classical endpoint pin |
| `linear_fade` | 0.4814 | classical linear fade |
| `cot_cubic_then_dualcosine` | 0.4608 | bearings classical: DualCosine on cracked (not published deep COT) |
| `dual_cosine` | 0.4608 | classical DualCosine fade |
| `seam_fir3` | 0.4483 | classical seam FIR3 |
| `soft_periodize_hann` | 0.4233 | classical Hann soft-periodize |

### mitbih_ecg

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9565 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `endpoint_pin_mean` | 0.8650 | classical endpoint pin |
| `spline_join` | 0.8082 | domain classical spline/FIR join (not Cycle-GAN / deep SOTA) |
| `seam_fir3` | 0.7662 | classical seam FIR3 |
| `no_bake` | 0.7495 | classical / passthrough |
| `linear_fade` | 0.4671 | classical linear fade |
| `dual_cosine` | 0.4137 | classical DualCosine fade |
| `soft_periodize_hann` | 0.3743 | classical Hann soft-periodize |
| `beat_average_sbmm_lite` | 0.3541 | ECG classical SBMM-lite beat average (not BeatDiff/Cycle-GAN) |

### ptbxl_ecg

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9336 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `endpoint_pin_mean` | 0.8569 | classical endpoint pin |
| `no_bake` | 0.7503 | classical / passthrough |
| `seam_fir3` | 0.7462 | classical seam FIR3 |
| `spline_join` | 0.7442 | domain classical spline/FIR join (not Cycle-GAN / deep SOTA) |
| `linear_fade` | 0.5108 | classical linear fade |
| `dual_cosine` | 0.4769 | classical DualCosine fade |
| `soft_periodize_hann` | 0.4530 | classical Hann soft-periodize |
| `beat_average_sbmm_lite` | 0.3260 | ECG classical SBMM-lite beat average (not BeatDiff/Cycle-GAN) |

### synth_cnc_g01

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9918 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `spline_join` | 0.7006 | domain classical spline/FIR join (not Cycle-GAN / deep SOTA) |
| `linear_fade` | 0.5691 | classical linear fade |
| `seam_fir3` | 0.5344 | classical seam FIR3 |
| `dual_cosine` | 0.4943 | classical DualCosine fade |
| `soft_periodize_hann` | 0.4734 | classical Hann soft-periodize |
| `no_bake` | 0.4499 | classical / passthrough |
| `endpoint_pin_mean` | 0.4096 | classical endpoint pin |

### synth_pmu_cycle

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9915 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `endpoint_pin_mean` | 0.9442 | classical endpoint pin |
| `no_bake` | 0.9356 | classical / passthrough |
| `seam_fir3` | 0.9119 | classical seam FIR3 |
| `linear_fade` | 0.8374 | classical linear fade |
| `spline_join` | 0.8315 | domain classical spline/FIR join (not Cycle-GAN / deep SOTA) |
| `dual_cosine` | 0.8272 | classical DualCosine fade |
| `soft_periodize_hann` | 0.8106 | classical Hann soft-periodize |

### mfpt_bearings

| Method | $R$ | Label |
|--------|-----|-------|
| `ours_hybrid_lstm` | 0.9411 | Ours (hybrid GA–PPO / hybrid_lstm outer loop) |
| `cot_linear_periodize` | 0.8657 | bearings classical bad-COT control (passthrough of linear resample) |
| `no_bake` | 0.8657 | classical / passthrough |
| `seam_fir3` | 0.5726 | classical seam FIR3 |
| `endpoint_pin_mean` | 0.5446 | classical endpoint pin |
| `linear_fade` | 0.4990 | classical linear fade |
| `cot_cubic_then_dualcosine` | 0.4830 | bearings classical: DualCosine on cracked (not published deep COT) |
| `dual_cosine` | 0.4830 | classical DualCosine fade |
| `soft_periodize_hann` | 0.4405 | classical Hann soft-periodize |

## Caveats

- Classical board + domain classical proxies; not a claim of beating published deep SOTA unless those models were executed.
- Modest outer-loop budget (pilot hours, not multi-day).
- Real content is z-scored per period; musical/clinical absolute scale not preserved.

Artifacts live in reelsynth `brand/artifacts/signal_heal_transfer/`.

