# Paper versions

| Version | Date | Headline |
|---------|------|----------|
| **v7** | 2026-07-19 | Current: weakness elimination F1–F5 (true export+AKWF, edge RMSE lock, poly, transfer honesty, SOTA unify) |
| v6 | 2026-07-19 | Archived peer-review A–E complete snapshot (restored from `83f4b48`, pre–weakness-elim) |
| v5 | 2026-07-19 | Archived pre–peer-review-revision snapshot (restored from `3f409b2`) |
| v4 | 2026-07-18 | Superseded archive |
| v3 | 2026-07-18 | Regenerated via Klaut scientific writing workflow (plan→write→revise→export); same residual science as v2, fuller IMRaD prose + workflow audit trail |
| v2 | 2026-07-18 | Residual score ∈ [0,1] as outer objective; nested unsupervised loss opt; Meta Top 1 `evo_explore_515` residual ≈0.824 vs DualCosine ≈0.698 |
| v1 | 2026-07-18 | D/S quality $Q$ objective; champion `racing_mid_1043` Q≈0.790 vs DualCosine ≈0.789 |

## v7 notes (current)

### Near-ceiling R and reward/HP tuning (20 July 2026)
- Methods/Discussion: no-bake $\approx 0.97$ compresses absolute $\Delta R$; reward shaping and search hyperparameters are first-class tunables with architecture (sec:reward-shaping).
- DualCosine centering framed as one shaping choice under that regime, not the objective.

### Objective vs DualCosine centering (20 July 2026)
- Clarified: reward/objective is maximize prolonged $R$ toward the ideal sibling (best $R{=}1$); DualCosine is not the reward.
- PPO uses $\rho{=}R-R_{\mathrm{DualCosine}}$ only as constant advantage centering; selection/FitCell use absolute $R$.
- Scrubbed “search-reward reference” wording in abstract/Methods/Experiments/Results/EVAL/NOMENCLATURE.

### Ideal sibling vs no-bake + classical board (20 July 2026)
- Clarified: ideal sibling $r^{\star}$ is the scoring target (cliff withheld); no-bake is unrepaired engine scored against $r^{\star}$.
- Reporting policy: always rank AI/favorite on absolute $R$ vs the full classical non-AI board (no-bake, FIR, DualCosine, poly, fades, VA); DualCosine $\Delta R$ is search-reward only.
- Abstract / Methods / Experiments / Results / Discussion / EVAL\_PROTOCOL / NOMENCLATURE updated; PDF rebuilt.

### Nomenclature: identity → no-bake (20 July 2026)
- Renamed the unrepaired-engine control from **identity** to **No-bake (passthrough)** in manuscript prose/tables.
- Defined in Methods (`sec:no-bake`): $f(x)=x$; not a residual skip; legacy JSON key remains `identity`.
- See `paper/v7/NOMENCLATURE.md`.

### Classical VA seam techniques figure (20 July 2026)
- Added `fig_va_seam_techniques.png` (ideal / cracked / BLIT/BLEP / PolyBLEP / BLAMP / DualCosine on tile 46, seed `20260719`).
- Expanded Section `sec:va-seam-baselines` with plain-language operator roles + tile $R$ caption.
- Meta: `figures/fig_va_seam_techniques.json`. Plot script lives in reelsynth (`scripts/plot_va_seam_techniques.py`).

### Weakness elimination F1–F5 (19 July 2026)
- F1: primary realism = true ReelSynth-exported factory periods ($n{=}25$); secondary = AKWF CC0 WAVs ($n{=}24$); procedural demoted.
- F3: edge RMSE locked as required seam-local secondary; endpoint-pin jump control; `tab:cliff-edge-rmse`.
- F2: polynomial seam fitter published (`poly_baseline.json`); SSM deferred (LSTM ceiling).
- F4: `transfer_failures.json` + Discussion win-condition narrative (export/Rust identity lead admitted).
- F5: N2N/seq/poly promoted into `tab:sota-main`; abstract/limitations sync; PDF rebuild (15 pp).
- Artifacts: `real_wt_matrix.json`, `poly_baseline.json`, `jump_control.json`, `transfer_failures.json`, updated `sota_matrix.json`.
- Flag: `paper/v7/WEAKNESS_ELIMINATION_COMPLETE.flag`.
- Sources: `paper/v7/`.

### Peer-review response (carried into v7 from A–E)
- Phase A: cliff strata (top 10%/25% wrap-jump); identity-$R$ honesty; edge RMSE / click energy; `tab:cliff-strata`.
- Phase B: primary corrupt→corrupt N2N + sibling-supervised ceiling + LSTM/1D-CNN (no holdout leakage).
- Phase C: ReelSynth-style factory + OA instrument wrap protocol; `SAMPLE_LICENSES.md`; no LibriSpeech/MUSDB.
- Phase D: deleted Lemma 1 and trivial Props; kept formal $R$; explicit no wrap-closure / no search-convergence guarantees.
- Phase E: abstract/discussion/related work/venue positioning (DAFx/AES/arXiv DSP); PDF rebuild.
- Artifacts: `figures/cliff_strata.json`, `n2n_baseline.json`, `seq_baseline.json`, `real_wt_matrix.json`.
- Flag: `paper/v7/PEER_REVIEW_COMPLETE.flag`.

### Baseline manuscript notes (carried into v7)
- Primary title: *Unsupervised Wavetable Seam Artifact Repair via Hybrid GA–PPO Meta-Search* (see `v7/TITLES.md`).
- Results: top-5 distinct bake architectures from the CUDA inference-bench leaderboard snapshot (§Top-5 architectures).
- Tooling/AI disclosure section; OA PDF harvest + non-OA flags (`artifacts/literature_oa/`).
- Method pseudocode: `docs/PSEUDOCODE.md`.
- Inference bench: favorite = fastest in near-max-$R$ band ($R\approx0.991$, $\approx3.15$\,ms/batch).
- Classical vs AI bench (same $R$ protocol): DualCosine $R\approx0.820$; best active classical `seam_fir3` $R\approx0.963$; neural favorite $R\approx0.991$ at $\approx2.47$\,ms/batch ($\Delta R{+}0.028$ / $\approx4.1\times$ latency vs `seam_fir3`). Artifacts: `artifacts/classical_vs_ai_bench/`, figures `fig_classical_vs_ai_*.png`.
- Family-conditional hardness + Outlook for follow-up pub.
- Overnight GPU hybrid continues; final overnight tables after 5k+ clean gate.

## v6 notes (archived peer-review A–E / pre–weakness-elim)

- Restored from commit `83f4b48` (parent of `b4cef83`, immediately before F1–F5 weakness-elimination landed).
- Snapshot includes peer-review Phases A–E complete manuscript/artifacts and the weakness-elimination *plan*, but **not** the F1–F5 manuscript/artifact changes (no `poly_baseline` / `jump_control` / `transfer_failures` / `tab:cliff-edge-rmse` / unified SOTA promotion in tex).
- Sources: `paper/v6/`. Current canonical paper is `paper/v7/`.

## v5 notes (archived pre–peer-review revision)

- Restored from commit `3f409b2` (parent of `f6dfbdf`, immediately before Phases A–E landed).
- Snapshot includes checklist/manuscript-review work and the peer-review *plan* docs, but **not** the A–E manuscript/artifact changes (no `cliff_strata` / N2N tables / Lemma deletion in tex).
- Sources: `paper/v5/`.

## v4 notes (superseded)

- Archived snapshot under `paper/v4/`.

## v3 notes

- Produced with gateway tools: `research_paper_plan` → `research_paper_write_subsection` × IMRaD → `research_paper_revise` → figures → export.
- Artifacts: `plan.md`, `revision_notes.md`, `subsections/`, `drafts/` under `paper/v3/`.
- Primary numbers unchanged: residual ≈0.824 vs DualCosine ≈0.698 ($\Delta{+}0.126$); elites all `evo_explore`.

## v2 notes

- Primary metric: prolonged residual vs `generate_sound_ideal` (tiled $N{=}16$).
- Bi-level search includes `bilevel_loss`, PBT, Bayes, etc.; elites under residual were all `evo_explore` (mutate-only).
- Frozen θ in ReelSynth re-locked to champion.

## v1 notes

- Outer objective was wrap-energy $Q=\tfrac12(\mathcal{D}+\mathcal{S})$.
- Small Q margin over DualCosine; still useful as historical baseline.
