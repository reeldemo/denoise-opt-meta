# Signal healing / wrap-discontinuity applications — lit map

**Full brief (canonical in reelsynth):**  
[`reelsynth/docs/papers/denoise_opt/SIGNAL_HEALING_APPLICATIONS_LIT.md`](https://github.com/reeldemo/reelsynth/blob/main/docs/papers/denoise_opt/SIGNAL_HEALING_APPLICATIONS_LIT.md)

Survey date: 2026-07-23.

## Executive takeaway

DenoiseOpt-style **cycle-local wrap repair** (bake Θ, prolonged residual \(R\)) transfers best to:

1. Wavetable / sample looping (home)  
2. Granular / concatenative grain seams  
3. PSOLA period splices  
4. Graphics seam optimization analogues (quilting / graphcut / video textures)  
5. ECG beat restoration (medium — different metrics)

**Closest published neighbors:** LoopGen (arXiv:2504.04466), DWTS (arXiv:2111.10003), Creative US6084170 optimal looping, Efros quilting / Kwatra graphcut / Schödl video textures.

**Open niche:** NAS / meta-search over repair-operator graphs scored by prolonged tiled residual — still largely unoccupied outside DenoiseOpt.
