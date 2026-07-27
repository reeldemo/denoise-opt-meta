# Pending R_blend regenerations (v11)

Do **not** retag prolonged-$R$ numbers as $R_{\mathrm{blend}}$.

## Done (this pass + follow-up)

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
| Intro tile JSON + PNG | `fig_intro_sine_problem.json` / `.png` | `plot_intro_sine_problem.py` (burned-in labels now $R_{\mathrm{blend}}$) |
| Top-5 inference (`tab:top5`) | `inference_bench.json` | `bench_inference_same_score.py --from-json …` (live $R_{\mathrm{blend}}$) |
| Rust sound_bench (`tab:rust-bench`) | `rust_sound_bench_matrix.json` | `bench_rust_sound_bench_tiles.py` |
| Matched 5k appendix (cheap) | `meta_approach_compare_rblend_rescore.json` + `meta_approaches_table.tex` | `rescore_meta_champs_rblend.py` (one-shot re-fit of frozen champs; **not** full D1 re-search) |
| Ablation isolated 150-it | `ablate_rblend_rescore.json` | `rescore_ablate_rblend.py` |
| Compute caption | `tab:compute` | labeled historical prolonged-$R$ overnight |

## Still deferred

### D1 — Full matched multi-approach 5k outer loops under $R_{\mathrm{blend}}{+}J$

Multi-hour GPU overnight. Do **not** wipe `meta_approach_compare/`; write a new tree:

```powershell
cd C:\Users\Julian\Documents\Programming\github\reeldemo\reelsynth
.\.venv_gpu\Scripts\python.exe scripts\bench_meta_approaches_5k.py --iters 5000 --device cuda
# then publish into meta_approach_compare_v11_rblend/ (or equivalent) + refresh bars/compare figs
```

Until D1 completes, Table `tab:meta-approaches` uses the cheap frozen-champ re-fit; learning-curve bars/plots remain historical prolonged-$R$ trajectories.

### Branch-best freezes under $R_{\mathrm{blend}}$

Left column of `tab:ablation` (PBT / Combined / NAS search freezes) has no separate fitted weights — prolonged-$R$ only unless a new hybrid history is recorded under $R_{\mathrm{blend}}$.

### HP ±50% probe under $R_{\mathrm{blend}}$

Optional: `python scripts/bench_meta_hp_sensitivity.py` under blend (still prolonged in appendix).
