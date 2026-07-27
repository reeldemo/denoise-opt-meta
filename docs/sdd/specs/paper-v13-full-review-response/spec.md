# Spec: paper-v13-full-review-response

Technical plan for v13. Obeys `docs/sdd/CONSTITUTION.md`.

## Architecture

v13 is a paper-folder + artifacts revision. No new scripts needed beyond a small stats aggregator; existing bench scripts gain `--eval-seed` support where missing.

### Folder structure

```
paper/Unsupervised_..._v13/       # copied from v12, all tex files edited
brand/artifacts/
  meta_approach_compare_v13_rblend/
    1902771841/                    # per-seed search results
    2026072701/
    2026072702/
  holdout_multiseed_v13/           # per-holdout-seed eval results
    20260719/ ... 20260723/
```

### Script changes (reelsynth)

1. **`bench_meta_approaches_5k.py`** — already accepts `--seed` and `--out-dir`. Verify it scores under R_blend (not prolonged R). If `make_batch` or `FitCell` still maximizes prolonged R, patch the scoring path.

2. **`bench_sota_matrix.py`** / **`bench_canonical_eval_dataset.py`** / **`bench_cliff_strata.py`** / **`bench_v10_n2n_vs_ours.py`** — add `--eval-seed` argument if not present; run 5x with different seeds; output per-seed JSON.

3. **New: `scripts/aggregate_multiseed_stats.py`** — reads per-seed JSONs, computes mean/std/win-rate/sign-test, emits `paper/...v13/figures/multiseed_summary.json`.

### Paper tex changes (denoise-opt-meta)

Key files and what changes:

- **`main.tex`**: version bump, abstract rewrite (AC-3.1)
- **`subsections/introduction.tex`**: contributions rewrite (AC-3.2), one scope statement
- **`subsections/methods.tex`**: expand R_blend definition (AC-4.1, AC-4.2)
- **`subsections/results.tex`**: restructure around multi-seed (AC-3.3), add stats (AC-2.2, AC-2.3)
- **`subsections/limitations.tex`**: consolidate disclaimers (AC-3.4), replace "variance honesty" with "multi-seed protocol"
- **`subsections/experiments.tex`**: document multi-seed protocol, list seeds
- **`subsections/experiments_transfer.tex`**: reframe paragraph (AC-5.1, AC-5.2)
- **`figures/meta_approaches_table.tex`**: multi-seed mean +/- std
- **`figures/n2n_vs_ours_table.tex`**: multi-seed mean +/- std

### Statistical methods

- **Per-board mean +/- std**: arithmetic mean and sample std over holdout seeds
- **Win-rate**: fraction of (family x seed) pairs where Ours > N2N
- **Sign test**: on 20 multi-family boards (paired Ours vs N2N per family, aggregated across seeds). Report two-sided p-value.
- **No fabricated CIs** for quantities with <3 samples

### Build and verify

1. `build.ps1` compiles PDF
2. Klaut `audit_english` >= 4.5
3. Manual check: no text implies Ours beats N2N on holdout
4. Prolonged R labeled superseded everywhere

## Risks

- GPU wall time (~24h for 3-seed search) may delay; narrative work proceeds in parallel
- Multi-seed results may change the holdout story (Ours could beat N2N on average); report honestly either way
- Script `--eval-seed` plumbing may need non-trivial changes if seed is hardcoded

## Dependencies

- RTX 3090 or equivalent CUDA GPU
- Python 3.12, PyTorch 2.6+CUDA 12.4
- LaTeX toolchain for PDF build
