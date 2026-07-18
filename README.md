# DenoiseOpt meta-learning

Public artifacts, paper, and reproduction scripts for **DenoiseOpt**: literature-informed meta-learning for label-free wavetable wrap crackle reduction.

## Author

- **Julian M. Kleber**
- ORCID: [0000-0001-5518-0932](https://orcid.org/0000-0001-5518-0932)
- Email: [julian.m.kleber@gmail.com](mailto:julian.m.kleber@gmail.com)

## Related repositories

| Repo | Role |
|------|------|
| [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth) | Synth DSP, frozen `FROZEN_THETA`, `bench_denoise_meta` |
| [reeldemo/denoise-opt-meta](https://github.com/reeldemo/denoise-opt-meta) | This repo — paper PDF, 1500-trial JSON, figures, harvest/render scripts |

## Abstract

Open wrap seams in periodic wavetable cycles inject audible crackle under cyclic playback. We cast bake-time periodization as an unsupervised optimization problem: a seam-local stack \(f_\theta\) with \(\theta\in[0,1]^{12}\) is scored by a joint denoise/shape loss without paired clean labels. After a procedural 100 000-cycle bench, a **1500-trial** literature-informed meta-learning / HPO search compares a naive DualCosine baseline against the top-4 meta champions. On held-out validation (\(N{=}2000\)), **Meta Top 1** reaches \(Q\approx 0.790\) vs naive \(Q\approx 0.789\) while keeping \(\mathcal{S}\approx 0.997\).

Champion trial: `racing_mid_1043` (prior family `racing_mid`).

## Paper

- Source: [`paper/main.tex`](paper/main.tex)
- Compiled PDF: [`paper/main.pdf`](paper/main.pdf)
- Figures: [`paper/figures/`](paper/figures/)

```bash
cd paper
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

## Key results (1500 trials)

From [`artifacts/denoise_opt_meta_1500.json`](artifacts/denoise_opt_meta_1500.json):

| Algorithm | Prior / kind | \(Q\) (matrix, \(N{=}2000\)) |
|-----------|--------------|------------------------------|
| Naive DualCosine | hand baseline | ≈ 0.789 |
| Meta Top 1 | racing_mid | ≈ 0.790 |
| Meta Top 2–4 | racing_mid / pbt_exploit | ≈ 0.790 |

Frozen θ ships in ReelSynth as `FROZEN_THETA` in `src/denoise_opt.rs` (matches champion `theta`).

## Layout

```
paper/           # main.tex, main.pdf, figures/
artifacts/       # denoise_opt_meta_1500.json, 100k fit, literature_*.json, fig_*.png
scripts/         # harvest_*.py, render_*.py
```

## Reproduce (from reelsynth)

Clone the synth, then:

```bash
cargo run -p reelsynth --release --bin bench_denoise_meta
python brand/artifacts/render_benchmark_matrix.py
python brand/artifacts/render_paper_figures.py
pdflatex docs/papers/denoise_opt/main.tex
```

Scripts in this repo mirror `brand/artifacts/` in reelsynth.

## License

MIT — see [LICENSE](LICENSE).
