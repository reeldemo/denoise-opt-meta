# Review response map — paper v8

Point-by-point map from peer review (24 Jul 2026) → DenoiseOpt paper v8.
Fill **v8 location** as W1–W5 land (section / figure / table / appendix).

Source plans: SDD `docs/sdd/specs/paper-v8-review-response/`; locked paper plan W0–W5 (1A + 2B).

## Weaknesses

| ID | Review item | Planned workstream | v8 location |
|----|-------------|--------------------|-------------|
| W-clarity | Poor Methods clarity / organization (algorithms drowning the pipeline) | W1 | §Methods slim body (`subsections/methods.tex`); overview Fig.~\ref{fig:denoiseopt-arch}; Algorithms 1–9 → Appendix~\ref{app:algorithms} (`appendix_algorithms.tex`) |
| W-eval | Narrow synthetic eval (static sine+cliff tiles) | W2 | v8 location TBD |
| W-math | Sloppy math / ideal-sibling definition | W3 | §Methods Notation + Ideal sibling: $\Theta$, $r^{\star}=G(\mathrm{seed},\mathrm{cliff=off})$, $x=G(\mathrm{seed},\mathrm{cliff=on})$, outer $\max R$; Rem.~\ref{rem:dualcosine-centering} |
| W-hp | Unjustified HP meta-search claims | W4 | v8 location TBD |

## Author questions

| ID | Question | Planned workstream | v8 location |
|----|----------|--------------------|-------------|
| Q1 | Ideal sibling — how generated for arbitrary cracked period? | W3 (+ appendix alg) | §Methods Ideal sibling (eq.~\ref{eq:G-siblings}); cite `make_batch` in `overnight_gpu_rl_arch.py`; same seed, cliff withheld |
| Q2 | DualCosine centering — objective vs advantage baseline? | W3 | §Methods Rem.~\ref{rem:dualcosine-centering} + eq.~\ref{eq:dualcosine-centering}; outer obj eq.~\ref{eq:outer-obj}; DualCosine centering = PPO advantage only |
| Q3 | Hyperparameter sensitivity of meta-search? | W4 | v8 location TBD |

## Suggestions

| ID | Suggestion | Planned workstream | v8 location |
|----|------------|--------------------|-------------|
| S-imrad | IMRaD-style Methods restructure | W1 | §Methods: problem → ideal sibling → $R$ → $\Theta$ → overview TikZ → search/FitCell → hybrid → meta → HPs |
| S-appendix | Move Algorithms 1–9 to appendix | W1 | Appendix~\ref{app:algorithms} (`subsections/appendix_algorithms.tex`); `\appendix` in `main.tex` |
| S-overview | Overview figure before component deep-dives | W1 | Fig.~\ref{fig:denoiseopt-arch} (`arch_diagram.tex`) before search-space deep-dives |
| S-real-wt | Real wavetable diversity beyond sine+cliff | W2 | v8 location TBD |
| S-vibrato | Vibrato / dynamic-pitch playback + spectrogram | W2 | v8 location TBD |
| S-ab | Listening / A/B perceptual evidence | W2 | v8 location TBD |
| S-theta | Formal bake operator $\Theta$ | W3 | eq.~\ref{eq:Theta}; Notation table; bake § |
| S-hp50 | HP ±50% sensitivity study | W4 | v8 location TBD |

## Notes (scope honesty)

- **Formal human listening study / formal A/B scores:** out of scope for v8 (constitution / requirements). S-ab is answered with spectrogram + hear WAVs + paper panel, not claimed formal A/B scores.
- **Deep SOTA CWRU/ECG:** out of scope; transfer pilot stays classical-board appendix.
- **Do not wipe** publishable `meta_approach_compare/` (fold existing 5k / bars / heals).
- **Q1–Q2 answered in Methods (W3/T2).** Q3 deferred to W4.
- **AC-1 / W1 (T3):** slim Methods + appendix algs + overview TikZ + display names + constitution-scoped Abstract/Intro.
