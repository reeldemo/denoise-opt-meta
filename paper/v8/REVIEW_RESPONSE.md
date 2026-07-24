# Review response map — paper v8

Point-by-point map from peer review (24 Jul 2026) → DenoiseOpt paper v8.
Fill **v8 location** as W1–W5 land (section / figure / table / appendix). Until then: `v8 location TBD`.

Source plans: SDD `docs/sdd/specs/paper-v8-review-response/`; locked paper plan W0–W5 (1A + 2B).

## Weaknesses

| ID | Review item | Planned workstream | v8 location |
|----|-------------|--------------------|-------------|
| W-clarity | Poor Methods clarity / organization (algorithms drowning the pipeline) | W1 | v8 location TBD |
| W-eval | Narrow synthetic eval (static sine+cliff tiles) | W2 | v8 location TBD |
| W-math | Sloppy math / ideal-sibling definition | W3 | v8 location TBD |
| W-hp | Unjustified HP meta-search claims | W4 | v8 location TBD |

## Author questions

| ID | Question | Planned workstream | v8 location |
|----|----------|--------------------|-------------|
| Q1 | Ideal sibling — how generated for arbitrary cracked period? | W3 (+ appendix alg) | v8 location TBD |
| Q2 | DualCosine centering — objective vs advantage baseline? | W3 | v8 location TBD |
| Q3 | Hyperparameter sensitivity of meta-search? | W4 | v8 location TBD |

## Suggestions

| ID | Suggestion | Planned workstream | v8 location |
|----|------------|--------------------|-------------|
| S-imrad | IMRaD-style Methods restructure | W1 | v8 location TBD |
| S-appendix | Move Algorithms 1–9 to appendix | W1 | v8 location TBD |
| S-overview | Overview figure before component deep-dives | W1 | v8 location TBD |
| S-real-wt | Real wavetable diversity beyond sine+cliff | W2 | v8 location TBD |
| S-vibrato | Vibrato / dynamic-pitch playback + spectrogram | W2 | v8 location TBD |
| S-ab | Listening / A/B perceptual evidence | W2 | v8 location TBD |
| S-theta | Formal bake operator $\Theta$ | W3 | v8 location TBD |
| S-hp50 | HP ±50% sensitivity study | W4 | v8 location TBD |

## Notes (scope honesty)

- **Formal human listening study / formal A/B scores:** out of scope for v8 (constitution / requirements). S-ab is answered with spectrogram + hear WAVs + paper panel, not claimed formal A/B scores.
- **Deep SOTA CWRU/ECG:** out of scope; transfer pilot stays classical-board appendix.
- **Do not wipe** publishable `meta_approach_compare/` (fold existing 5k / bars / heals).
