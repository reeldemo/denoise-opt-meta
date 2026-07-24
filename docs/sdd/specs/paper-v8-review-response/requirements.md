# Requirements: paper-v8-review-response

## Problem

Peer review (24 Jul 2026) found poor Methods clarity, sloppy ideal-sibling math, narrow eval, and unjustified HP meta-search. v8 must answer the review with a full IMRaD rewrite and new experiments before claiming readiness.

Locked paper workstreams: **1A + 2B** (full IMRaD restructure; experiments blocked until HP ±50%, vibrato/spectrogram, and hear-panel evidence land). See companion plan `denoiseopt_paper_v8` (W0–W5).

## User stories

### US-1 — Clarity rewrite

As an author, I want Methods reorganized for IMRaD readability so reviewers can follow the pipeline without drowning in algorithms.

**Acceptance criteria**

- AC-1.1: Algorithms 1–9 live in appendix; body has overview figure + slim Methods.
- AC-1.2: Display names consistent; objective vs DualCosine centering are separate paragraphs/equations.
- AC-1.3: Abstract/Intro claims match constitution scope.

### US-2 — Math formalization

As a reviewer, I want $\Theta$, ideal sibling, and the outer objective defined unambiguously.

**Acceptance criteria**

- AC-2.1: Formal $\Theta$ and $r^{\star} = G(\mathrm{seed},\mathrm{cliff=off})$ vs cracked $\mathrm{cliff=on}$ in Notation/Methods.
- AC-2.2: Single outer objective $\max R(y, r^{\star})$; Q1–Q2 answered in Methods + `REVIEW_RESPONSE.md`.
- AC-2.3: Fig.1 / no-bake captions distinguish no-bake, DualCosine, ideal, Ours.

### US-3 — Eval + listening

As a reader, I want evidence beyond static sine+cliff tiles.

**Acceptance criteria**

- AC-3.1: Vibrato/spectrogram eval script + figure in `paper/v8/figures/`.
- AC-3.2: Hear-sample pack cited with paper panel; WAVs path documented.
- AC-3.3: Transfer pilot appendix with classical-board disclaimer.
- AC-3.4: Existing 5k meta/bars/heals folded (not re-run).

### US-4 — HP sensitivity

As a reviewer, I want ±50% HP sensitivity evidence for meta-search claims.

**Acceptance criteria**

- AC-4.1: Bench under `reelsynth/.../meta_hp_sensitivity/` with seed `1902771841`.
- AC-4.2: Table/figure of champion $R$ vs default; Q3 answered in Results + `REVIEW_RESPONSE.md`.
- AC-4.3: Does not modify/wipe `meta_approach_compare/`.

### US-5 — Ship

As a maintainer, I want a buildable v8 PDF and synced pointers.

**Acceptance criteria**

- AC-5.1: `paper/v8/main.pdf` builds; CHANGELOG + pointer + TITLES updated.
- AC-5.2: `REVIEW_RESPONSE.md` has a row for every review item.
- AC-5.3: reelsynth mirror README points at v8; both repos committed/pushed when implement finishes.

## Out of scope

- Formal human listening study (no IRB / no claimed formal A/B listening scores).
- Deep SOTA CWRU/ECG baselines.
- Wiping or re-running the publishable 5k `meta_approach_compare/` campaign.
- DAW plugin / S7 host audio-MIDI work.
- Full 5k re-search for every HP perturbation (sensitivity budget only; see design.md).

## Open questions

None blocking implement. Grill-locked decisions live in `design.md` (HP budget, listening claims, WT diversity).

Accepted: Gate B (user Build), 2026-07-24.
