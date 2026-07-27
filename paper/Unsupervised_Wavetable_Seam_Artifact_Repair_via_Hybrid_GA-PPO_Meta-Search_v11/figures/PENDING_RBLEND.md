# Pending R_blend regenerations (v11)

Do **not** retag prolonged-$R$ numbers as $R_{\mathrm{blend}}$.

## Done (this pass)

| Board | Artifact | Script |
|-------|----------|--------|
| Four-board N2N vs Ours | `n2n_vs_ours.json` | already locked |
| Canonical holdout | `method_scores.json` | `bench_canonical_eval_dataset.py` |
| Cliff strata | `cliff_strata.json` | `bench_cliff_strata.py` |
| Multi-family SOTA | `sota_matrix.json` + figs | `bench_sota_matrix.py`, `plot_sota_matrix.py` |
| VA seam | `va_seam_blep.json` + `fig_va_seam_techniques.*` | `bench_va_seam_blep.py`, `plot_va_seam_techniques.py` |
| Poly / jump | `poly_baseline.json`, `jump_control.json` | `bench_poly_seam_baseline.py`, `bench_jump_control.py` |
| Real WT | `real_wt_matrix.json` | `real_wt_wrap_protocol.py` |
| Transfer Table | `signal_heal_transfer_results_table.json` | `bench_signal_heal_transfer.py --skip-search --merge-existing` (domain champs already v10.1) |
| Intro tile JSON | `fig_intro_sine_problem.json` | rescore under blend |

## Still pending

### Matched multi-approach 5k outer loops

```powershell
cd C:\Users\Julian\Documents\Programming\github\reeldemo\reelsynth
.\.venv_gpu\Scripts\python.exe scripts\bench_meta_approaches_5k.py --iters 5000 --device cuda
```

Copy resulting `meta_approach_compare.json` (+ bars/compare figs) into v11 `figures/`.

### Top-5 inference-bench ranking (`tab:top5`)

```powershell
.\.venv_gpu\Scripts\python.exe scripts\bench_inference_same_score.py --device cuda
```

Requires scoring fitted overnight champs under `residual_score_blend` (script still has prolonged-$R$ timing path in places — extend before claiming).

### Rust sound_bench table (`tab:rust-bench`)

```powershell
.\.venv_gpu\Scripts\python.exe scripts\bench_rust_sound_bench_tiles.py --device cuda
```

### Ablation / compute appendix tables

Isolated 150-it re-runs and branch freezes under $R_{\mathrm{blend}}$ (not overnight 5k, but still a search budget).

### Intro PNG panel annotations

JSON scores updated; if `fig_intro_sine_problem.png` burns in prolonged-$R$ labels, re-render the figure script under blend.
