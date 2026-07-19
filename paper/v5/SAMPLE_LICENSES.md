# Sample licenses (Phase C wavetable-native realism)

**Date:** 19 July 2026  
**Policy:** license-clean only. No scraped commercial wavetable banks. No LibriSpeech. No MUSDB.

## Primary realism: ReelSynth-style factory periods

| Item | Detail |
|------|--------|
| Source | Procedural factory shapes (saw, square, triangle, pulse, morph) generated in `scripts/real_wt_wrap_protocol.py` |
| License | MIT (ReelSynth / denoise-opt-meta companion code) |
| Count | ≥24 periods, $L{=}256$ |
| Notes | Same engine geometry as DenoiseOpt eval. Not third-party audio files. |

## Secondary realism: OA instrument / WT one-shots

| Item | Detail |
|------|--------|
| Source | Additive-harmonic instrument-like one-shots (string / flute / reed / clarinet / brass stacks) generated in `scripts/real_wt_wrap_protocol.py` |
| License | MIT procedural stand-ins (no third-party sample download required for reproducibility) |
| Count | ≥20 periods, $L{=}256$ |
| Notes | Documented as OA-clean procedural instrument slices under the wrap protocol. Not commercial library rips. |

## Explicitly excluded

- LibriSpeech
- MUSDB / MUSDB18
- Scraped commercial wavetable packs
- Any sample without a recorded OA-compatible license

## Wrap protocol (shared)

1. Close-seam ideal (linear endpoint match).
2. Open-wrap cliff amplitude $\pm\mathcal{U}(0.08,0.43)$ over `SEAM_W=8`.
3. Seam-boosted noise matching `make_batch`.
4. Score prolonged $R$, SNR/SDR, wrap-jump, edge RMSE.
