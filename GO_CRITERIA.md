# Go / no-go for public release

## Gate (your criteria)

We ship when **all** of the following hold:

1. **Clean overnight segment ≥ 5 000 iterations** on the hybrid GPU search (`PPO+GA+PBT+NAS+depth+MoE`) with no process crash (NaN hardened; plateau adapt may fire).
2. **Documented repro commands** below complete without interruption on a fresh shell.
3. **Paper v5 PDF** rebuilds from sources and matches the title / ORCID / clickable links.

Until then: keep the detached GPU job running; do not claim final overnight mean-$R$ as finished science.

## Current snapshot

Check live progress:

```powershell
Get-Content brand\artifacts\overnight_gpu_rl_arch_latest.json | ConvertFrom-Json |
  Select-Object iter, champion_residual, baseline_dual_cosine, iters_since_improve
```

(Run from the **reelsynth** checkout.)

## Repro checklist (paper + plots)

### A. Paper PDF (denoise-opt-meta)

```powershell
cd path\to\denoise-opt-meta\paper\v5
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
# → main.pdf
```

Requires MiKTeX/TeX Live with `orcidlink`, `hyperref`, `cite`, `balance`, `times`/`mathptmx`.

### B. Benchmark matrix figures (from committed JSON)

```powershell
cd path\to\denoise-opt-meta
python scripts\render_benchmark_matrix.py
# → artifacts/fig_benchmark_matrix.png, fig_pareto_1500.png, fig_prior_families.png
```

### C. Lit-combo / residual meta (optional, reelsynth)

```powershell
cd path\to\reelsynth
cargo test -p reelsynth residual_score -- --nocapture
cargo run -p reelsynth --release --bin bench_denoise_meta -- 40
```

Use a small `N` for smoke; full 1500/500 is slow.

### D. Overnight GPU (optional; needs CUDA + `.venv_gpu`)

```powershell
cd path\to\reelsynth
.\scripts\start_overnight_gpu_detached.ps1
# or: .\.venv_gpu\Scripts\python.exe scripts\overnight_gpu_rl_arch.py --iters 5000 --device cuda --history-every 1 --max-hours 24
```

Do **not** start a second GPU job if one is already writing `overnight_gpu_rl_arch_latest.json`.

## What is already publication-ready (independent of 5k)

- Family-conditional hardness (100k + lit-combo stress): nonlinear/combo/overlay hard; Outlook for follow-up pub.
- Residual formula, DualCosine baseline protocol, lit used vs screened.
- arXiv twocolumn template + ORCID icon + clickable links.

## After 5k

1. Snapshot `history.jsonl` + `overnight_gpu_rl_arch_latest.json` into `denoise-opt-meta/artifacts/`.
2. Regenerate overnight figures into `paper/v5/figures/`.
3. Fill Results tables with frozen numbers; recompile PDF.
4. Tag repos / open PRs as needed.
