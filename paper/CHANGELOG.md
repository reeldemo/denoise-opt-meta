# Paper versions

| Version | Date | Headline |
|---------|------|----------|
| **v4** | 2026-07-18 | Generic RL+GA meta-learning title; full Introduction + Literature landscape (used vs screened); Results deferred while overnight GPU run continues |
| **v3** | 2026-07-18 | Regenerated via Klaut scientific writing workflow (plan→write→revise→export); same residual science as v2, fuller IMRaD prose + workflow audit trail |
| **v2** | 2026-07-18 | Residual score ∈ [0,1] as outer objective; nested unsupervised loss opt; Meta Top 1 `evo_explore_515` residual ≈0.824 vs DualCosine ≈0.698 |
| **v1** | 2026-07-18 | D/S quality $Q$ objective; champion `racing_mid_1043` Q≈0.790 vs DualCosine ≈0.789 |

## v4 notes

- Primary title: *Unsupervised Audio Denoising via Hybrid Reinforcement Learning and Genetic Algorithm Meta-Learning* (see `v4/TITLES.md`).
- Klaut: attach curated harvest → fetch/analyze OA PDFs → plan/write with Ollama `qwen3.5:9b` → author revision for claim hygiene (no invented final overnight numbers).
- Results/Discussion: family-conditional hardness (nonlinear/combo/overlay hard; harmonic/am_fm easier) from 100k + lit-combo stress; Outlook sketches a follow-up paper on family-/cliff-conditional meta-learning toward $R>0.999$.
- Overnight GPU job continues (`PPO+GA+PBT+NAS+depth+MoE` + plateau deepen-adapt).

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
