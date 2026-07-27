# Metric regeneration inventory — v11 peer-review response

Locked primary protocol: **\(R_{\mathrm{blend}}\)** (\(\alpha{=}0.7\)) + latency-aware \(J\) (EVAL_PROTOCOL v10.1).
Whole-curve prolonged \(R{\approx}0.991\) is **superseded** and must not be sold as current.

T0 budget: cheap re-scores only. Full matched-\(5\)k outer-loop re-search under \(R_{\mathrm{blend}}\) = **Deferred D1**.

## Primary (locked, do not overwrite with prolonged \(R\))

| Board | Status | Artifact |
|-------|--------|----------|
| Holdout / four-board N2N vs Ours | **Done** \(R_{\mathrm{blend}}\) | Table `tab:n2n-vs-ours`; `figures/` N2N boards |
| v10.1 hybrid \(1{,}200\)-iter freeze | **Done** \(R_{\mathrm{blend}}{+}J\) | `reelsynth/brand/artifacts/meta_approach_compare_v10/hybrid_lstm/` |

## Cheap regen completed this cycle (JSON already \(R_{\mathrm{blend}}\); TeX updated)

| Board | Script | Notes |
|-------|--------|-------|
| Cliff strata (\(4{,}096\) tiles) | `reelsynth/scripts/bench_cliff_strata.py` | `brand/artifacts/cliff_strata.json` + paper `figures/cliff_strata.json` (`primary_metric=r_blend`) |
| Transfer seven boards | `reelsynth/scripts/bench_signal_heal_transfer.py` | `brand/artifacts/signal_heal_transfer/results_table.json` (`skip_search` rescoring existing hybrid ckpts under \(R_{\mathrm{blend}}\)) |
| Jump control / poly / VA | `bench_jump_control.py`, `bench_poly_seam_baseline.py`, `bench_va_seam_blep.py` / `plot_va_seam_techniques.py` | Scripts emit `primary_metric=r_blend`; paper TeX may still quote older prolonged snapshots — see pending |

## Still prolonged-\(R\)-only or incomplete (label in Limitations / appendix)

| Board | Why incomplete | Exact regen command (when budgeted) |
|-------|----------------|-------------------------------------|
| Matched \(5\)k outer-loop bake-off (Random, CMA-ES, REINFORCE, aging, TPE, hybrid) | Historical FitCell maximized prolonged \(R\); histories in `meta_approach_compare/` | **Cheap done:** `rescore_meta_champs_rblend.py` → `meta_approach_compare_rblend_rescore.json` (one-shot re-fit). **D1 full re-search still deferred:** `bench_meta_approaches_5k.py --iters 5000` into a new `meta_approach_compare_v11_rblend/` tree (multi-hour). |
| Canonical classical holdout Table `tab:canonical-methods` | Snapshot under prolonged \(R\) | `python scripts/bench_canonical_eval_dataset.py` (confirm emits \(R_{\mathrm{blend}}\); refresh paper JSON) |
| Multi-family SOTA matrix Table `tab:sota-main` | Historical prolonged \(R\) means | `python scripts/bench_sota_matrix.py` then copy JSON → paper `figures/sota_matrix.json` |
| Real WT / export / AKWF Table `tab:real-wt` | Prolonged \(R\) means in TeX | Re-score with locked metric script used for Factory+FX / AKWF \(R_{\mathrm{blend}}\) four-board (already in `tab:n2n-vs-ours` for balanced corpora) |
| Branch ablations `ablate-*` (\(150\)-it) | Champions store prolonged `residual` only | **Isolated done:** `rescore_ablate_rblend.py`. Branch-best freezes (no weights) remain prolonged-labeled. |
| HP ±50% probe | Prolonged \(R\) | Optional: `python scripts/bench_meta_hp_sensitivity.py` under \(R_{\mathrm{blend}}\) |
| Random NAS learning curve under \(R_{\mathrm{blend}}\) | Only hybrid v10 history has `r_blend` keys | Part of D1 or a short Random-only \(1{,}200\)-iter run mirroring v10 |

## Learning-curve honesty

| Curve | Metric | Source |
|-------|--------|--------|
| Hybrid vs Random champion vs evaluations (Fig. search-learning-curve, prolonged panel) | **Superseded** whole-curve prolonged \(R\) | `brand/artifacts/meta_approach_compare/{hybrid_lstm,random}/history.jsonl` |
| Hybrid champion vs evaluations (v10.1 panel) | Locked \(R_{\mathrm{blend}}\) / \(J\) | `brand/artifacts/meta_approach_compare_v10/hybrid_lstm/history.jsonl` |

## Forbidden

- Renaming prolonged-\(R\) JSON fields to \(R_{\mathrm{blend}}\) without re-scoring.
- Wiping `meta_approach_compare/`.
- Inventing error bars or transfer SOTA scores.
