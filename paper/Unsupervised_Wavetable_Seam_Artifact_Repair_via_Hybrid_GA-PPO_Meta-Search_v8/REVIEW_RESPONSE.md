# Review response map — paper v8

Point-by-point map from peer review (24 Jul 2026) → DenoiseOpt paper v8.
Fill **v8 location** as W1–W5 land (section / figure / table / appendix).

Source plans: SDD `docs/sdd/specs/paper-v8-review-response/`; locked paper plan W0–W5 (1A + 2B).

## Weaknesses

| ID | Review item | Planned workstream | v8 location |
|----|-------------|--------------------|-------------|
| W-clarity | Poor Methods clarity / organization (algorithms drowning the pipeline) | W1 | §Methods slim body (`subsections/methods.tex`); overview Fig.~\ref{fig:denoiseopt-arch}; Algorithms 1–9 → Appendix~\ref{app:algorithms} (`appendix_algorithms.tex`) |
| W-eval | Narrow synthetic eval (static sine+cliff tiles) | W2 | §\ref{sec:vibrato-eval} Fig.~\ref{fig:vibrato-spectrogram}; §\ref{sec:hear-samples} Fig.~\ref{fig:hear-samples-panel}; §\ref{sec:wt-gallery} Fig.~\ref{fig:wt-diversity-gallery}; App.~\ref{app:transfer-pilot}; existing 5k/bars/heals folded (no re-run) |
| W-math | Sloppy math / ideal-sibling definition | W3 | §Methods Notation + Ideal sibling: $\Theta$, $r^{\star}=G(\mathrm{seed},\mathrm{cliff=off})$, $x=G(\mathrm{seed},\mathrm{cliff=on})$, outer $\max R$; Rem.~\ref{rem:dualcosine-centering} |
| W-hp | Unjustified HP meta-search claims | W4 | §Results para.~\ref{para:hp-sensitivity}; Table~\ref{tab:hp-sensitivity}; Fig.~\ref{fig:hp-sensitivity}; artifacts `reelsynth/brand/artifacts/meta_hp_sensitivity/` (500-iter OAT ±50% probe, seed `1902771841`; **not** full 5k re-search) |

## Author questions

| ID | Question | Planned workstream | v8 location |
|----|----------|--------------------|-------------|
| Q1 | Ideal sibling — how generated for arbitrary cracked period? | W3 (+ appendix alg) | §Methods Ideal sibling (eq.~\ref{eq:G-siblings}); cite `make_batch` in `overnight_gpu_rl_arch.py`; same seed, cliff withheld |
| Q2 | DualCosine centering — objective vs advantage baseline? | W3 | §Methods Rem.~\ref{rem:dualcosine-centering} + eq.~\ref{eq:dualcosine-centering}; outer obj eq.~\ref{eq:outer-obj}; DualCosine centering = PPO advantage only |
| Q3 | Hyperparameter sensitivity of meta-search? | W4 | §Results para.~\ref{para:hp-sensitivity} + Table~\ref{tab:hp-sensitivity} / Fig.~\ref{fig:hp-sensitivity}; `subsections/results_hp_sensitivity.tex`; script `reelsynth/scripts/bench_meta_hp_sensitivity.py`. **Answer:** 11/11 OAT ±50% arms @500 iters (seed `1902771841`) complete; default champ $R\approx 0.9888$; largest $|\Delta R|\approx 0.012$ (`lr_m50`). Local robustness vs DualCosine gap $\approx 0.17$ — sensitivity evidence, **not** a second 5k ranking. |

## Suggestions

| ID | Suggestion | Planned workstream | v8 location |
|----|------------|--------------------|-------------|
| S-imrad | IMRaD-style Methods restructure | W1 | §Methods: problem → ideal sibling → $R$ → $\Theta$ → overview TikZ → search/FitCell → hybrid → meta → HPs |
| S-appendix | Move Algorithms 1–9 to appendix | W1 | Appendix~\ref{app:algorithms} (`subsections/appendix_algorithms.tex`); `\appendix` in `main.tex` |
| S-overview | Overview figure before component deep-dives | W1 | Fig.~\ref{fig:denoiseopt-arch} (`arch_diagram.tex`) before search-space deep-dives |
| S-real-wt | Real wavetable diversity beyond sine+cliff | W2 | §\ref{sec:wt-gallery} Fig.~\ref{fig:wt-diversity-gallery}; Table~\ref{tab:real-wt} / `real_wt_matrix.json` (existing exports only; no new NAS) |
| S-vibrato | Vibrato / dynamic-pitch playback + spectrogram | W2 | §\ref{sec:vibrato-eval} Fig.~\ref{fig:vibrato-spectrogram}; script `reelsynth/scripts/bench_vibrato_spectrogram.py`; artifacts `brand/artifacts/vibrato_spectrogram/` |
| S-ab | Listening / A/B perceptual evidence | W2 | §\ref{sec:hear-samples} Fig.~\ref{fig:hear-samples-panel}; WAVs `brand/artifacts/meta_approach_compare/hear_samples/` — **no formal A/B / MOS** (constitution) |
| S-theta | Formal bake operator $\Theta$ | W3 | eq.~\ref{eq:Theta}; Notation table; bake § |
| S-hp50 | HP ±50% sensitivity study | W4 | Same as Q3 / W-hp: OAT ±50% on $n$, $\epsilon$, fit lr, GA mut2, entropy; out `meta_hp_sensitivity/`; paper figures + `results_hp_sensitivity.tex` |

## Notes (scope honesty)

- **Formal human listening study / formal A/B scores:** out of scope for v8 (constitution / requirements). S-ab is answered with spectrogram + hear WAVs + paper panel, not claimed formal A/B scores.
- **Deep SOTA CWRU/ECG:** out of scope; transfer pilot stays classical-board appendix (`appendix_transfer_pilot.tex`).
- **Do not wipe** publishable `meta_approach_compare/` (fold existing 5k / bars / heals).
- **Q1–Q2 answered in Methods (W3/T2).** **Q3 / W4 (T5):** HP ±50% OAT sensitivity probe landed (script + artifacts + Results snippet); honesty label = sensitivity not full 5k re-search; never touches `meta_approach_compare/`.
- **AC-1 / W1 (T3):** slim Methods + appendix algs + overview TikZ + display names + constitution-scoped Abstract/Intro.
- **AC-3 / W2 (T4):** vibrato spectrogram + hear panel + WT gallery + transfer appendix landed; no new NAS; no formal A/B.
- **AC-5 / W5 (T6):** `main.tex` inputs listening + HP Results; Discussion/Limitations review narrative; CHANGELOG/pointer/TITLES/reelsynth README → v8; `main.pdf` rebuilt; dual-repo commit+push.
