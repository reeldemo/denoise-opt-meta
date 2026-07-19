# DenoiseOpt meta-learning

Public artifacts and versioned papers for **DenoiseOpt** — unsupervised audio / wavetable wrap denoising with hybrid RL + genetic-algorithm meta-learning.

Companion to the synth implementation: [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth).

**Release gate:** see [GO_CRITERIA.md](GO_CRITERIA.md) (≥5k clean GPU iterations + documented repro).

---

## Author

**Julian M. Kleber** · [ORCID 0000-0001-5518-0932](https://orcid.org/0000-0001-5518-0932) · [julian.m.kleber@gmail.com](mailto:julian.m.kleber@gmail.com)

## Current paper (v7)

**Title:** *Unsupervised Wavetable Seam Artifact Repair via Hybrid GA–PPO Meta-Search*

| | |
|--|--|
| PDF | [`paper/v7/main.pdf`](paper/v7/main.pdf) |
| Sources | [`paper/v7/`](paper/v7/) |
| Changelog | [`paper/CHANGELOG.md`](paper/CHANGELOG.md) |

Build:

```powershell
cd paper\v7
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### Headline empirical claims (ready now)

- Prolonged residual $R\in[0,1]$ (1 = best) vs DualCosine baseline.
- Peer-review strata: hard-cliff top10%/25%, N2N + sequential baselines, factory/OA wavetable realism.
- Weakness elimination: true ReelSynth export + AKWF realism, edge RMSE lock, poly baseline, transfer honesty, unified SOTA table.
- Lit-combo / residual meta: e.g. `pbt_exploit+residual_primary` **R≈0.903** vs DualCosine **≈0.705** (500-iter timing run).
- **Family hardness:** `nonlinear` / `combo` / `extreme_overlay` / `triple_mix` repeatedly worst; follow-up paper sketched in Outlook (family-/cliff-conditional meta-learning).
- Overnight GPU hybrid (PPO+GA+PBT+NAS+depth+MoE) interim champ **R≈0.991** — final overnight tables after the 5k+ clean gate.

Older versions: [`paper/v6/`](paper/v6/) (peer-review A–E / pre–weakness-elim archive), [`paper/v5/`](paper/v5/) (pre–peer-review-revision archive), [`paper/v4/`](paper/v4/), [`paper/v3/`](paper/v3/), [`paper/v2/`](paper/v2/), [`paper/v1/`](paper/v1/).

---

## Reproduce plots

```powershell
cd path\to\denoise-opt-meta
python scripts\render_benchmark_matrix.py
```

Needs committed JSON under `artifacts/`. Optional reelsynth re-search:

```powershell
cd path\to\reelsynth
cargo run -p reelsynth --release --bin bench_denoise_meta -- 1500
```

---

## Layout

```
GO_CRITERIA.md        # release gate
paper/v7/             # current arXiv twocolumn paper
paper/v6/             # peer-review A–E / pre–weakness-elim archive
paper/v5/             # pre–peer-review-revision archive
paper/v1..v4/         # older versions
artifacts/              # JSON + figure PNGs
scripts/              # render / harvest / regen
```

## Related

| Repo | Role |
|------|------|
| [reeldemo/reelsynth](https://github.com/reeldemo/reelsynth) | DSP, overnight GPU search, `bench_denoise_meta` |
| [reeldemo/denoise-opt-meta](https://github.com/reeldemo/denoise-opt-meta) | This repo |
| Klaut research gateway | `research_paper_*` + `arxiv-twocolumn` template |

MIT — see [LICENSE](LICENSE). Pseudocode: [docs/PSEUDOCODE.md](docs/PSEUDOCODE.md). OA reference flags: [artifacts/literature_oa/REFERENCES_OA.md](artifacts/literature_oa/REFERENCES_OA.md).
