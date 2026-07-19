# Paper versions

| Version | Date | Headline |
|---------|------|----------|
| **v6** | 2026-07-19 | Current: peer-review response (hard-cliff strata, N2N/seq baselines, wavetable-native realism, theory honesty) |
| v5 | 2026-07-19 | Archived pre–peer-review-revision snapshot (restored from `3f409b2`) |
| v4 | 2026-07-18 | Superseded archive |
| v3 | 2026-07-18 | Regenerated via Klaut scientific writing workflow (plan→write→revise→export); same residual science as v2, fuller IMRaD prose + workflow audit trail |
| v2 | 2026-07-18 | Residual score ∈ [0,1] as outer objective; nested unsupervised loss opt; Meta Top 1 `evo_explore_515` residual ≈0.824 vs DualCosine ≈0.698 |
| v1 | 2026-07-18 | D/S quality $Q$ objective; champion `racing_mid_1043` Q≈0.790 vs DualCosine ≈0.789 |

## v6 notes (current)

### Peer-review response (19 July 2026)
- Phase A: cliff strata (top 10%/25% wrap-jump); identity-$R$ honesty; edge RMSE / click energy; `tab:cliff-strata`.
- Phase B: primary corrupt→corrupt N2N + sibling-supervised ceiling + LSTM/1D-CNN (no holdout leakage).
- Phase C: ReelSynth-style factory + OA instrument wrap protocol; `SAMPLE_LICENSES.md`; no LibriSpeech/MUSDB.
- Phase D: deleted Lemma 1 and trivial Props; kept formal $R$; explicit no wrap-closure / no search-convergence guarantees.
- Phase E: abstract/discussion/related work/venue positioning (DAFx/AES/arXiv DSP); PDF rebuild.
- Artifacts: `figures/cliff_strata.json`, `n2n_baseline.json`, `seq_baseline.json`, `real_wt_matrix.json`.
- Flag: `paper/v6/PEER_REVIEW_COMPLETE.flag`.
- Sources: `paper/v6/`.

### Baseline manuscript notes (carried into v6)
- Primary title: *Unsupervised Wavetable Seam Artifact Repair via Hybrid GA–PPO Meta-Search* (see `v6/TITLES.md`).
- Results: top-5 distinct bake architectures from the CUDA inference-bench leaderboard snapshot (§Top-5 architectures).
- Tooling/AI disclosure section; OA PDF harvest + non-OA flags (`artifacts/literature_oa/`).
- Method pseudocode: `docs/PSEUDOCODE.md`.
- Inference bench: favorite = fastest in near-max-$R$ band ($R\approx0.991$, $\approx3.15$\,ms/batch).
- Classical vs AI bench (same $R$ protocol): DualCosine $R\approx0.820$; best active classical `seam_fir3` $R\approx0.963$; neural favorite $R\approx0.991$ at $\approx2.47$\,ms/batch ($\Delta R{+}0.028$ / $\approx4.1\times$ latency vs `seam_fir3`). Artifacts: `artifacts/classical_vs_ai_bench/`, figures `fig_classical_vs_ai_*.png`.
- Family-conditional hardness + Outlook for follow-up pub.
- Overnight GPU hybrid continues; final overnight tables after 5k+ clean gate.

## v5 notes (archived pre–peer-review revision)

- Restored from commit `3f409b2` (parent of `f6dfbdf`, immediately before Phases A–E landed).
- Snapshot includes checklist/manuscript-review work and the peer-review *plan* docs, but **not** the A–E manuscript/artifact changes (no `cliff_strata` / N2N tables / Lemma deletion in tex).
- Sources: `paper/v5/`. Current canonical paper is `paper/v6/`.

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
