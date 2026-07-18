# DenoiseOpt meta-learning

Public artifacts and versioned papers for **DenoiseOpt** — literature-informed meta-learning for label-free wavetable wrap crackle reduction.

This repo is the companion to the synth implementation in [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth). Code that *runs* the search lives there; the JSON, figures, and PDFs that *document* the search live here.

---

## Author

**Julian M. Kleber** · [ORCID 0000-0001-5518-0932](https://orcid.org/0000-0001-5518-0932) · [julian.m.kleber@gmail.com](mailto:julian.m.kleber@gmail.com)

## What changed in v3

v3 regenerates the residual-objective paper through the Klaut Research Gateway **scientific writing workflow** (plan → write section-by-section → revise → figures → export), rather than hand-gluing a README into LaTeX.

Scientific content is unchanged in substance from v2:

- Prolonged residual $R\in[0,1]$ (1 = best), tiled $N{=}16$ ideal vs engine
- Nested unsupervised loss $L=(1-\mathcal{D})+\lambda(1-\mathcal{S})$ searched inside priors
- Killer: `evo_explore_515` residual **≈0.824** vs DualCosine **≈0.698** ($\Delta{+}0.126$)
- Honest: top residual elites were mutate-only `evo_explore` (inner sweeps = 0)

### Killer result (1500 trials, val $N{=}2000$)

| Algorithm | Residual | Notes |
|-----------|----------|-------|
| Naive DualCosine | **0.698** | hand baseline |
| Meta Top 1 — `evo_explore_515` | **0.824** | +0.126 over naive |
| Meta Top 2–4 | ≈0.821–0.823 | all `evo_explore` |

---

## Lit-combo 500 timing footnote

Combinatorial hybrids of lit families (bayes / PBT / irace / MOEA·D / evo / N2N / bilevel / residual-primary + bake DualCosine/Classic/Soft/Ensemble*/Crossfade). Each outer trial **fits until convergence**: relative $|J_{\mathrm{prev}}-J_{\mathrm{cur}}|/\max(|J_{\mathrm{prev}}|,10^{-6}) < 10^{-4}$ for **3** consecutive coordinate sweeps (else max **16**).

| Algorithm | Residual | Notes |
|-----------|----------|-------|
| Naive DualCosine | **0.705** | bake baseline (val 400) |
| Lit-combo Top 1 — `pbt_exploit+residual_primary` | **0.903** | +0.198 over naive |

**Measured wall clock (release, 500 outer iterations):** `500_ITER_WALL_TIME_SEC=157.990` (157989 ms). Host: AMD Ryzen 9 7950X3D / Windows / `BENCH_N=256` / prolong=16 / `val_fast=80`. Mean conv steps ≈10.5; 87.8% converged before max. Artifact: [`artifacts/denoise_opt_meta_lit_combo_500.json`](artifacts/denoise_opt_meta_lit_combo_500.json).

```bash
cargo run -p reelsynth --release --bin bench_denoise_meta -- 500
```

(Does not rewrite `paper/v3`; numbers for timing / hybrid search only.)

---

## Paper versions

| Version | Path | PDF |
|---------|------|-----|
| **v3** (current) | [`paper/v3/`](paper/v3/) | [`paper/v3/main.pdf`](paper/v3/main.pdf) |
| v2 | [`paper/v2/`](paper/v2/) | [`paper/v2/main.pdf`](paper/v2/main.pdf) |
| v1 (D/S quality) | [`paper/v1/`](paper/v1/) | [`paper/v1/main.pdf`](paper/v1/main.pdf) |

Changelog: [`paper/CHANGELOG.md`](paper/CHANGELOG.md)

Workflow audit trail in `paper/v3/`: `plan.md`, `revision_notes.md`, `subsections/`, `drafts/`.

```bash
cd paper/v3
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Regenerate via gateway workflow (optional):

```bash
# Requires klaut-research-gateway on PYTHONPATH
python scripts/regen_paper_v3.py
```

---

## Reproduce the plots in the paper

You need a checkout of **reelsynth** (Rust toolchain) and Python 3 with `matplotlib` + `numpy`.

### 1. Run the meta search (writes the JSON the plots read)

```bash
cd /path/to/reelsynth
cargo run -p reelsynth --release --bin bench_denoise_meta
# → brand/artifacts/denoise_opt_meta_1500.json
```

### 2. Render figures

```bash
cd /path/to/denoise-opt-meta
python scripts/render_benchmark_matrix.py
# → artifacts/fig_benchmark_matrix.png, fig_pareto_1500.png, fig_prior_families.png
```

Copy PNGs into `paper/v3/figures/` before compiling if you regenerate them.

### 3. Compile the PDF

```bash
cd paper/v3
pdflatex -interaction=nonstopmode main.tex
```

---

## Layout

```
paper/
  CHANGELOG.md
  v1/                 # D/S quality paper
  v2/                 # residual + loss-opt (manual draft)
  v3/                 # residual paper via scientific writing workflow (current)
artifacts/            # JSON + figure PNGs
scripts/              # harvest / render / regen helpers
```

## Related

| Repo | Role |
|------|------|
| [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth) | DSP, `FROZEN_THETA`, `bench_denoise_meta` |
| [reeldemo/denoise-opt-meta](https://github.com/reeldemo/denoise-opt-meta) | This repo |
| [klaut-pro/klaut-research-gateway](https://github.com/klaut-pro/klaut-research-gateway) | `research_paper_*` scientific writing tools |

## License

MIT — see [LICENSE](LICENSE).
