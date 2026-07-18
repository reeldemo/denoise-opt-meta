# DenoiseOpt meta-learning

Public artifacts and versioned papers for **DenoiseOpt** — literature-informed meta-learning for label-free wavetable wrap crackle reduction.

This repo is the companion to the synth implementation in [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth). Code that *runs* the search lives there; the JSON, figures, and PDFs that *document* the search live here.

---

## Author

**Julian M. Kleber** · [ORCID 0000-0001-5518-0932](https://orcid.org/0000-0001-5518-0932) · [julian.m.kleber@gmail.com](mailto:julian.m.kleber@gmail.com)

## What changed in v2

v1 ranked trials by wrap-energy quality $Q$. That closed seams but did not ask whether prolonged cyclic playback matched the intended continuous wave.

**v2** ranks by a prolonged **residual score** $\in[0,1]$ (1 = best):

\[
R = \mathrm{clamp}\!\left(1 - \frac{\mathrm{rms}(y_{\mathrm{engine}}-y_{\mathrm{ideal}})}{\max(\mathrm{rms}(y_{\mathrm{ideal}}),\varepsilon)},\,0,\,1\right)
\]

- Ideal: same seed, no open-wrap cliffs (`generate_sound_ideal`), tiled 16×  
- Engine: DenoiseOpt on the (possibly cliffed) cycle, tiled 16×  
- Soft shape gate: $\mathcal{S}<0.97$ → rank $\times 0.45$

The outer loop also nests an **inner unsupervised loss** fit $L=(1-\mathcal{D})+\lambda(1-\mathcal{S})$ on $\theta$ (and optionally $\lambda$). Seven prior families, including explicit `bilevel_loss`.

### Killer result (1500 trials, val $N{=}2000$)

| Algorithm | Residual | Notes |
|-----------|----------|-------|
| Naive DualCosine | **0.698** | hand baseline |
| Meta Top 1 — `evo_explore_515` | **0.824** | +0.126 over naive |
| Meta Top 2–4 | ≈0.821–0.823 | all `evo_explore` |

Shape stays $\mathcal{S}\approx 1.0$ on the matrix. Nested loss-opt priors were searched; under residual they did not beat wide evolutionary mutation. That is reported honestly in the paper.

Frozen $\theta^\star$ in ReelSynth matches the champion.

---

## Paper versions

| Version | Path | PDF |
|---------|------|-----|
| **v2** (current) | [`paper/v2/`](paper/v2/) | [`paper/v2/main.pdf`](paper/v2/main.pdf) |
| v1 (D/S quality) | [`paper/v1/`](paper/v1/) | [`paper/v1/main.pdf`](paper/v1/main.pdf) |

Changelog: [`paper/CHANGELOG.md`](paper/CHANGELOG.md)

```bash
cd paper/v2
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## Reproduce the plots in the paper

You need a checkout of **reelsynth** (Rust toolchain) and Python 3 with `matplotlib` + `numpy`.

### 1. Run the meta search (writes the JSON the plots read)

```bash
cd /path/to/reelsynth
cargo run -p reelsynth --release --bin bench_denoise_meta
# → brand/artifacts/denoise_opt_meta_1500.json
# (~2–3 min on a typical laptop; sanity: append `-- 40`)
```

### 2. Render figures

From reelsynth:

```bash
python brand/artifacts/render_benchmark_matrix.py
# → brand/artifacts/fig_benchmark_matrix.png
# → brand/artifacts/fig_pareto_1500.png
# → brand/artifacts/fig_prior_families.png
```

Or from this repo (same script, expects JSON next to `../artifacts` or edit `ART`):

```bash
cd /path/to/denoise-opt-meta
python scripts/render_benchmark_matrix.py   # if ART points at artifacts/
```

Expected artifacts after a full run:

| File | Role |
|------|------|
| `artifacts/denoise_opt_meta_1500.json` | Full trial report + matrix |
| `artifacts/fig_benchmark_matrix.png` | Paper Fig. matrix |
| `artifacts/fig_pareto_1500.png` | Residual vs loss elite scatter |
| `artifacts/fig_prior_families.png` | Prior-family histogram |

Copy PNGs into `paper/v2/figures/` before compiling if you regenerate them.

### 3. Compile the PDF

```bash
cd paper/v2
pdflatex -interaction=nonstopmode main.tex
```

---

## Layout

```
paper/
  CHANGELOG.md
  v1/                 # D/S quality paper
  v2/                 # residual + loss-opt paper (current)
artifacts/            # JSON + figure PNGs
scripts/              # harvest / render helpers
```

## Related

| Repo | Role |
|------|------|
| [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth) | DSP, `FROZEN_THETA`, `bench_denoise_meta` |
| [reeldemo/denoise-opt-meta](https://github.com/reeldemo/denoise-opt-meta) | This repo |

## License

MIT — see [LICENSE](LICENSE).
