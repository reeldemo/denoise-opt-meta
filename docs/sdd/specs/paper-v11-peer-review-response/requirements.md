# Requirements: paper-v11-peer-review-response

## Problem

An external peer-style review of the v11 DenoiseOpt manuscript praises the seam-restoration framing and hybrid search, but rejects clarity, oversold novelty, weak non-audio transfer justification, missing statistical rigor / learning curves, and confuses **superseded whole-curve prolonged \(R{\approx}0.99093\)** with locked **\(R_{\mathrm{blend}}\)** (holdout Ours \({\approx}0.9697\) vs N2N \({\approx}0.9750\) vs Dual Cosine \({\approx}0.541\)).

v11 must answer every Strength / Weakness / Suggestion with manuscript + experiment changes under the constitution, without inventing scores or claiming deep domain SOTA.

**Canonical paper:** `paper/Unsupervised_Wavetable_Seam_Artifact_Repair_via_Hybrid_GA-PPO_Meta-Search_v11/`  
**Companion code:** `reelsynth` benches/scripts.

## Review fact-check (locked)

| Review claim | Truth |
|--------------|--------|
| Champion \(R_{\mathrm{blend}}{\approx}0.99093\) vs DualCosine \(0.81658\) | **Wrong metric.** Those numbers are historical **whole-curve prolonged \(R\)**. Locked holdout uses \(R_{\mathrm{blend}}\): Ours \({\approx}0.9697\), N2N \({\approx}0.9750\), Dual Cosine \({\approx}0.541\). |
| “bake-cell” | Manuscript term is **repair operator** \(\Theta\) (legacy code: bake cell). |
| Hybrid “surpasses” DualCosine on primary holdout under \(R_{\mathrm{blend}}\) | True directionally, but **N2N still gates / beats Ours** on holdout \(R_{\mathrm{blend}}\). Do not erase that honesty. |

## User stories

### US-1 — Clarity and organization

As a reviewer, I want a readable IMRaD narrative with defined jargon so I can follow Problem → Protocol → Search space → Algorithm → Experiments → Results.

**Acceptance criteria**

- AC-1.1: Every acronym (MoE, PBT, FitCell, \(J\), \(R_{\mathrm{blend}}\), etc.) defined on first use; Terminology primer stays early in Introduction.
- AC-1.2: Methods body stays slim; Algorithms 1–9 remain appendix; DualCosine centering is a labeled remark separate from the outer objective.
- AC-1.3: Related Work motivates used vs screened citations in plain English (no “dependencies” jargon).
- AC-1.4: `REVIEW_RESPONSE.md` row maps this review’s “Severe Clarity…” weakness to concrete tex locations.

### US-2 — Modest contribution framing

As an author, I want contribution claims that match integrative novelty (hybrid search on a crisp DSP problem), not foundational ML theater.

**Acceptance criteria**

- AC-2.1: Abstract / Contributions / Conclusion say **hybrid GA–PPO(+PBT) applied to cycle-local seam repair**, not “a new learning algorithm.”
- AC-2.2: Explicit non-claims: no wrap-closure proof, no search-convergence theorem, no speech/music SOTA.
- AC-2.3: Review “Overselling…” weakness closed in `REVIEW_RESPONSE.md`.

### US-3 — Metric lock and correct primary numbers

As a reader, I want every main-text table/figure to report locked \(R_{\mathrm{blend}}\) (or be clearly pending regeneration), never historical \(R{\approx}0.991\) sold as current.

**Acceptance criteria**

- AC-3.1: Intro / Results / Limitations forbid “historical context only” as an excuse for wrong-metric boards.
- AC-3.2: Primary holdout story is Table `tab:n2n-vs-ours` (\(R_{\mathrm{blend}}\)); synopsis-style \(0.99093\) appears only as **superseded** freeze if at all.
- AC-3.3: Boards still on prolonged \(R\) only are listed with regen commands or moved to appendix labeled incomplete.
- AC-3.4: No invented \(R_{\mathrm{blend}}\) retags of prolonged-\(R\) JSON.

### US-4 — Non-audio transfer reframed or cut

As a reviewer, I want transfer boards either mechanistically justified as wrap-protocol stress tests or removed from the main narrative.

**Acceptance criteria**

- AC-4.1: One clear paragraph: transfer = **same wrap discontinuity protocol on other periodic signals**, not diagnosis SOTA / not “audio bake transfers to bearings.”
- AC-4.2: Per-domain seam analogy (bearing revolution, ECG beat, CNC/PMU) in ≤1 short paragraph each, or transfer section demoted to appendix.
- AC-4.3: Table 14 / transfer status stays honest (OOD footnotes, blocked rows).
- AC-4.4: User gate: **keep reframed** (default) vs **appendix-only** vs **delete** — resolve before heavy rewrite.

### US-5 — Statistical rigor

As a reviewer, I want variance, fair N2N size comparison, and significance where claimed.

**Acceptance criteria**

- AC-5.1: Primary \(R_{\mathrm{blend}}\) tables report mean±std or CI over declared seeds/runs where multi-seed already exists; add missing error bars for new primary claims.
- AC-5.2: Explicit param counts: favorite Θ vs SeamN2N (~53k) side-by-side.
- AC-5.3: Wilcoxon / CI already on multi-family prolonged board stay labeled by metric; add analogous stats on \(R_{\mathrm{blend}}\) multi-family if regenerating.
- AC-5.4: Train/holdout seed separation restated (holdout `20260719`, search `1902771841`, N2N train `424242`).

### US-6 — Search efficiency / learning curves

As a reader, I want champion score vs outer-loop evaluations for hybrid vs at least Random NAS.

**Acceptance criteria**

- AC-6.1: Figure: champion \(R_{\mathrm{blend}}\) (or locked search objective \(J\)) vs evaluation index for hybrid + Random (reuse `meta_approach_compare` / v10 search logs if present).
- AC-6.2: Caption states budget, seed, and whether curve is \(R_{\mathrm{blend}}\) or superseded prolonged \(R\).
- AC-6.3: Short Results paragraph: when Dual Cosine is surpassed; plateau/boredom mentioned with one factual sentence.

### US-7 — Branch ablations

As a reviewer, I want GA / PPO / PBT contribution evidence, not only final hybrid score.

**Acceptance criteria**

- AC-7.1: Table or figure from existing ablate-* artifacts or a bounded re-run (document budget); no wipe of publishable 5k compare.
- AC-7.2: Mapped in `REVIEW_RESPONSE.md` to “Strengthen Experimental Validation.”

### US-8 — Ship response package

As a maintainer, I want a buildable v11 PDF and a complete review map.

**Acceptance criteria**

- AC-8.1: Slug PDF builds via `build.ps1`.
- AC-8.2: `REVIEW_RESPONSE.md` has a row for every Strength, Weakness, and Suggestion in the pasted review (including synopsis fact-check).
- AC-8.3: CHANGELOG entry; constitution obeyed; both repos pushed when implement finishes.

## Out of scope

- Formal MOS/MUSHRA / human listening panel.
- Deep CWRU / ECG / Paderborn diagnosis SOTA bake-off under clinical metrics.
- New foundational RL/NAS algorithm (proofs, convergence).
- Wiping `meta_approach_compare/` or inventing \(R_{\mathrm{blend}}\) by renaming prolonged \(R\).
- Full overnight re-search of every historical board unless tasked and budgeted.

## Open questions

1. **Transfer keep policy (US-4.4):** keep in main text with mechanistic reframing (recommended), move to appendix, or delete?
2. **Regen budget:** which prolonged-\(R\) boards must get \(R_{\mathrm{blend}}\) this cycle (canonical / cliff / VA / transfer / matched 5k curves)?
3. **Venue bar:** DAFx/AES preprint bar vs “top-tier ML venue” rigor — how hard to push error bars / multi-seed?

**Gate:** accept `requirements.md` (and answer open questions) before locking `spec.md` / implement.
