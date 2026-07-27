# DenoiseOpt v6 Weakness Elimination Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.  
> **Plan only.** Do not implement until the user explicitly starts execution.  
> **Canonical path:** `denoise-opt-meta/paper/v7/WEAKNESS_ELIMINATION_PLAN.md`  
> **Prior loop:** Phases A–E in `PEER_REVIEW_IMPROVEMENT_PLAN.md` are **done** (`PEER_REVIEW_COMPLETE.flag`, 19 Jul 2026).  
> **This plan:** eliminate **residual** critique pressure still visible after A–E.

**Goal:** Close remaining peer-review weaknesses and suggestions that are still PARTIAL or OPEN after paper v6 Phases A–E, without reopening REJECT items (LibriSpeech/MUSDB SOTA, fake theory, MUSHRA).

**Architecture:** Keep DenoiseOpt hybrid + prolonged $R$ as the story. Deepen honesty where v6 still has soft spots: (1) realism corpora that are procedural stand-ins rather than true exports/OA files, (2) wrap-jump / seam-local metric lock, (3) missing cheap classical poly (+ optional SSM), (4) transfer-gap narrative when favorite trails identity on factory/Rust. Do not pivot to speech enhancement.

**Tech Stack:** Same as prior plan — `reelsynth/scripts/` benches (local, uncommitted by default), TeX + JSON under `denoise-opt-meta/paper/v7/` (commit/push **only** here).

## Global Constraints

- **Commit/push only** `denoise-opt-meta`. Never commit/push `reelsynth` unless the user explicitly asks.
- **Locked grill decisions still apply** (19 Jul 2026): Lemma/Props DELETE; N2N full stress; realism BOTH tracks; venue DAFx/AES/arXiv DSP; no LibriSpeech/MUSDB.
- **Narrow claims only:** cycle-local wavetable / wrap-seam repair.
- **OA-only cites.** No invented PESQ/STOI on non-speech tiles. No MUSHRA unless user asks.
- **No fake theory** (no resurrected Lemma 1 / Props theater; no convergence guarantees).
- Holdout seed `20260719`; overnight search seed `1902771841`; N2N train `424242`; seq train `424243`.

---

## Executive summary

**Already fixed in v6 (Phases A–E):** hard-cliff strata + identity-$R$ prose; true corrupt→corrupt N2N + sibling ceiling + LSTM/1D-CNN; theory theater deleted; venue/writing repositioned; wrap protocol + factory/OA matrices exist; Demucs/DiffWave screening documented.

**What remains scientifically soft:**

1. **Realism is still mostly synthetic.** `SAMPLE_LICENSES.md` and `real_wt_wrap_protocol.py` generate ReelSynth-style / OA-instrument **procedural stand-ins**, not byte-true ReelSynth factory exports or third-party OA WT files. Reviewers who asked for “real WT / instrument eval” can still call this partial.
2. **Wrap-jump stays flat** on the favorite; edge RMSE helps but is still framed as optional; grill never locked seam-local primary secondary.
3. **S7 incomplete:** LSTM/CNN landed; **polynomial fitter** and **SSM** never added.
4. **Transfer gaps** (factory favorite trails identity/FIR; Rust favorite trails identity; N2N ≈ favorite on sine cliffs) are reported honestly but not yet turned into a crisp “what fails / when search still wins” story with actionable follow-up benches.
5. **Main SOTA table** (`tab:sota-main`) still omits N2N/seq rows (they live in cliff/N2N subsections only).

**Counts (critique IDs below):** **CLOSED 9+7 residual** · **PARTIAL 0** · **STILL OPEN 0** · **REJECT 3** (plus REJECT splits noted in table).

**Status:** Residual phases **F1–F5 DONE** (`WEAKNESS_ELIMINATION_COMPLETE.flag`, 19 Jul 2026).

---

## Master triage table

Statuses: **CLOSED in v6** | **PARTIAL (residual)** | **STILL OPEN** | **REJECT (venue/claim)**.

### Weaknesses

| ID | Critique | Status | Evidence in v6 | Residual action |
|----|----------|--------|----------------|-----------------|
| W1 | Synthetic-only / limited generalizability | **PARTIAL** | §Wavetable-native transfer + `real_wt_matrix.json`; still procedural stand-ins | **Phase F1** |
| W2 | No real instrument / speech / polyphonic eval | **PARTIAL** / **REJECT** split | Instruments: procedural OA track. Speech/poly: explicitly OFF | F1 (true OA WT); **REJECT** speech/poly primary |
| W3 | Honest “no speech/music SOTA” limits contribution | **REJECT** (as defect) / **CLOSED** via E | Discussion venue sentence; Limitations | None (keep honesty) |
| W4 | Props 1–2 trivial | **CLOSED** | Deleted in Methods | None |
| W5 | Prop 3 self-evident | **CLOSED** | Folded into $R$ prose / deleted theater | None |
| W6 | Lemma 1 sketch / not real | **CLOSED** | Deleted; no-guarantee sentence present | None |
| W7 | Identity $R$ deceptively high | **CLOSED** | Hard-cliff table + Discussion identity-$R$ paragraph | Optional F3 prose refresh only |
| W8 | Wrap-jump flat while $R$ jumps | **PARTIAL** | Honest “tiled residual not endpoint-zeroing”; edge RMSE in JSON/prose; jump still ≈flat | **Phase F3** |
| W9 | Cite N2N but no true baseline | **CLOSED** | Primary corrupt→corrupt + sibling; Related Work updated | Optional F5: promote rows into `tab:sota-main` |

### Suggestions

| ID | Suggestion | Status | Evidence in v6 | Residual action |
|----|------------|--------|----------------|-----------------|
| S1 | Real-world WT / instrument eval | **PARTIAL** | Protocol + matrices; stand-ins not true exports/OA files | **Phase F1** |
| S2 | LibriSpeech / MUSDB for relevance | **REJECT** | Locked; Limitations + SAMPLE_LICENSES | None (optional OOD label-only probe stays OFF) |
| S3 | Modern self-supervised DL baseline | **CLOSED** | N2N corrupt→corrupt | None required |
| S4 | Replace props with convergence / landscape | **CLOSED** / **REJECT** invent | Theory deleted; budget accounting remark only | No fake guarantees |
| S5 | Prove Lemma 1 or remove | **CLOSED** | Removed | None |
| S6 | Top 10% hard-cliff strata | **CLOSED** | `tab:cliff-strata`, `cliff_strata.json` | None |
| S7 | Polynomial / LSTM / SSM baselines | **PARTIAL** | LSTM + 1D CNN done; **no poly, no SSM** | **Phase F2** (poly required; SSM optional timebox) |

### Extra residuals surfaced by v6 numbers (not in original paste, but block “weaknesses eliminated”)

| ID | Issue | Status | Residual action |
|----|-------|--------|-----------------|
| X1 | Factory transfer: favorite $R$ trails identity / `seam_fir3` | **STILL OPEN** | **Phase F4** |
| X2 | Seam-local metric grill still unlocked (edge RMSE vs click) | **STILL OPEN** | **Phase F3** Task F3.0 lock |
| X3 | N2N/seq absent from main multifamily SOTA table | **PARTIAL** | **Phase F5** |
| X4 | Search vs supervised ceiling story (N2N ≈ favorite on sine) | **PARTIAL** | F4 narrative + factory win case |

---

## What we still will NOT do

- Full **LibriSpeech / MUSDB / speech-music enhancement SOTA** chase (REJECT unless later reframed as optional non-claim OOD probe, default OFF).
- Invented **PESQ/STOI** on sine or non-speech tiles.
- **MUSHRA** / listening panels unless the user explicitly requests.
- Fake **Lemma / Props / convergence theorems**.
- Training **full Demucs / DiffWave** as primary baselines (screened; keep screening text).
- Pivoting abstract to general audio denoising or NeurIPS-impact cosplay.
- Committing/pushing **reelsynth** for this workstream.

---

## Priority order (residual only)

1. **Phase F1** — True wavetable-native corpus (W1, S1, W2-instrument)  
2. **Phase F3** — Seam-metric lock + wrap-jump honesty (W8, X2)  
3. **Phase F2** — Polynomial (+ optional SSM) baselines (S7 residual)  
4. **Phase F4** — Transfer-failure analysis + search-value narrative (X1, X4)  
5. **Phase F5** — Manuscript table unify + abstract refresh (X3, polish)

Parallelization: F3.0 (metric lock, TeX-only) can run with F1. F2 poly is independent of F1 once scoring helpers exist.

---

# Phase F1 — True wavetable-native corpus

**Effort:** M  
**Answers:** W1 (residual), S1 (residual), W2 instrument half  
**Depends on:** Existing `scripts/real_wt_wrap_protocol.py`, `EVAL_PROTOCOL.md`, `SAMPLE_LICENSES.md`  
**Why first:** v6 “realism” is still generator-shaped audio. Closing synthetic-only pressure requires **true** exports and/or license-clean third-party cycles.

### Intent

Replace or supplement procedural stand-ins with:

1. **Primary:** byte-true ReelSynth-exported periods (factory banks / patches via Rust or app export path).  
2. **Secondary:** at least one **external** OA instrument/WT one-shot pack with URL + license in `SAMPLE_LICENSES.md` (not only in-script additive harmonics).

Keep LibriSpeech/MUSDB OFF.

### Tasks

#### Task F1.1: ReelSynth export corpus (PRIMARY)

**Files:**
- Create or extend: `reelsynth/src/bin/export_reelsynth_wt_cycles.rs` (or documented Python export from existing `.reelwt` / factory assets)
- Create: `reelsynth/artifacts/real_wt_cycles/` (local) with `README` listing patch names + hashes
- Modify: `reelsynth/scripts/real_wt_wrap_protocol.py` — add `--source reelsynth_export` loader
- Update: `denoise-opt-meta/paper/v7/figures/real_wt_matrix.json`
- Update: `denoise-opt-meta/paper/v7/SAMPLE_LICENSES.md`

**Interfaces:**
- Consumes: exported mono cycles length ≥ $L$ or already $L{=}256$
- Produces: JSON methods matrix identical schema to current `real_wt_matrix.json` under key `reelsynth_export_primary`

- [ ] **Step 1:** Export ≥20 distinct factory/patch periods; record SHA256 in SAMPLE_LICENSES.  
- [ ] **Step 2:** Run wrap protocol (close-seam ideal → open-wrap cliff, seed `20260719`) for identity / DualCosine / seam_fir3 / favorite / N2N modes / seq.  
- [ ] **Step 3:** Write `real_wt_matrix.json` with explicit `meta.primary = "reelsynth_export"` (demote procedural factory to `procedural_standin` or remove from claim tables).  
- [ ] **Step 4:** Unit check: $n\ge20$; no LibriSpeech paths; licenses present.

**Done-when:** Paper primary realism table cites **exported** cycles, not `real_wt_wrap_protocol` procedural factory shapes.

**Risks:** Period extraction from multi-frame `.reelwt` ambiguous — document frame index / morph position in protocol.

#### Task F1.2: External OA WT / instrument pack (SECONDARY)

**Files:**
- Modify: `SAMPLE_LICENSES.md` (URL, license SPDX, retrieval date, file list)
- Modify: `real_wt_wrap_protocol.py` — `--source oa_files --glob ...`
- Update: `real_wt_matrix.json` secondary block

- [ ] **Step 1:** Select license-clean OA pack (CC0 / CC-BY / similar). Prefer single-cycle WT or easily periodized one-shots.  
- [ ] **Step 2:** Document crop/resample rule in EVAL_PROTOCOL (zero-crossing or fixed window).  
- [ ] **Step 3:** Score ≥20 cycles under same wrap protocol; refresh secondary table.  
- [ ] **Step 4:** Keep procedural additive harmonics only as **tertiary smoke** (optional appendix), not as “OA instrument” claim.

**Done-when:** Secondary realism is third-party OA files with auditable licenses; Limitations text updated to match.

#### Task F1.3: Manuscript honesty update

**Files:**
- Modify: `subsections/results.tex` (§Wavetable-native), `experiments.tex`, `limitations.tex`, `discussion.tex`
- Modify: `CHANGELOG.md` (under denoise-opt-meta paper)

- [ ] **Step 1:** Replace “ReelSynth-style factory” wording with “ReelSynth-exported periods” once F1.1 lands.  
- [ ] **Step 2:** State that v6 procedural stand-ins were interim; current numbers supersede.  
- [ ] **Step 3:** Rebuild PDF; commit **only** denoise-opt-meta artifacts (JSON + TeX + SAMPLE_LICENSES).

**Acceptance criteria (Phase F1):**
- [ ] ≥20 true ReelSynth-exported periods in primary matrix.  
- [ ] ≥20 external OA cycles in secondary matrix with SPDX + URL.  
- [ ] Procedural stand-ins no longer carry the primary realism claim.  
- [ ] No LibriSpeech/MUSDB.

---

# Phase F2 — Polynomial (+ optional SSM) baselines

**Effort:** S (poly) / M (SSM optional)  
**Answers:** S7 residual  
**Depends on:** Shared score helpers in `metrics_snr_sdr.py`, `bench_cliff_strata.py`, `bench_sota_matrix.py`

### Intent

Add the cheap classical baseline the critique asked for. LSTM/CNN already exist. Full SSM only if timeboxed (≤1–2 days); otherwise document “screened / deferred” with reason.

### Tasks

#### Task F2.1: Polynomial / endpoint fitter (REQUIRED)

**Files:**
- Create: `reelsynth/scripts/baselines/poly_seam_fitter.py`
- Create: `reelsynth/scripts/bench_poly_seam_baseline.py`
- Modify: `bench_cliff_strata.py`, `bench_sota_matrix.py`, `real_wt_wrap_protocol.py` (register method)
- Create: `denoise-opt-meta/paper/v7/figures/poly_baseline.json`

**Interfaces:**
- `fit_poly_seam(eng: Tensor[B,L], degree: int = 3, seam_w: int = 8) -> Tensor[B,L]`
- Fit low-degree polynomial (or linear endpoint ramp) on seam neighborhoods only; leave mid-cycle untouched; optional global DC match.

- [ ] **Step 1:** Implement seam-local poly / endpoint fitter (no learning).  
- [ ] **Step 2:** Score on canonical holdout + cliff strata + real-wt matrices.  
- [ ] **Step 3:** Export `poly_baseline.json` with $R$, SNR/SDR, wrap-jump, edge RMSE, ms/batch.  
- [ ] **Step 4:** Add row to Results (cliff table and/or baselines subsection).

**Done-when:** Polynomial baseline appears beside DualCosine/FIR with frozen JSON.

#### Task F2.2: Optional lightweight SSM (TIMEBOXED)

**Files:**
- Optional create: `reelsynth/scripts/baselines/ssm_seam.py`, `train_ssm_seam_baseline.py`
- Optional: `figures/ssm_baseline.json`

- [ ] **Step 1:** If ≤2 days available: tiny S4/S5-style or linear SSM ≤100k params, engine→ideal, train seed `424244` (disjoint).  
- [ ] **Step 2:** If over budget: add one Limitations/Related Work sentence: SSM deferred; LSTM is the seq ceiling.  
- [ ] **Step 3:** Never claim SSM SOTA without a completed JSON freeze.

**Acceptance criteria (Phase F2):**
- [ ] Polynomial baseline in paper + JSON.  
- [ ] SSM either reported with JSON **or** explicitly deferred (not silent).  
- [ ] LSTM/CNN/N2N remain.

---

# Phase F3 — Seam-metric lock + wrap-jump honesty

**Effort:** S–M  
**Answers:** W8 residual, X2  
**Depends on:** Existing edge RMSE / click energy in `cliff_strata.json`

### Intent

Lock the open grill item. Make wrap-jump flatness impossible to misread as a hidden win. Optionally add a **jump-aware** classical control (not a new overnight search) so readers see what endpoint-targeting looks like vs $R$-maximizing favorite.

### Tasks

#### Task F3.0: Lock seam-local metric (grill close)

**Default recommendation (carry forward):** **edge RMSE** as required secondary seam metric; click energy remains optional diagnostic.

**Files:**
- Modify: `PEER_REVIEW_IMPROVEMENT_PLAN.md` open decisions → mark edge RMSE locked (or note lock here only)
- Modify: `EVAL_PROTOCOL.md` — promote edge RMSE from optional → required secondary
- Modify: `experiments.tex`, `results.tex` tables that omit edge RMSE

- [ ] **Step 1:** Record lock in this plan + EVAL_PROTOCOL.  
- [ ] **Step 2:** Ensure `tab:cliff-strata` or a companion column/footnote reports edge RMSE for identity / DualCosine / favorite on top-10%.  
- [ ] **Step 3:** One Discussion sentence: primary claim remains $R$; wrap-jump is diagnostic; edge RMSE is the seam-local secondary.

#### Task F3.1: Jump-aware classical control (no new meta-search)

**Files:**
- Create: `reelsynth/scripts/baselines/endpoint_pin.py` (pin/crossfade endpoints to minimize $|y_0-y_{L-1}|$ or match ideal endpoints)
- Modify: cliff + real-wt benches
- Update: `cliff_strata.json` / small `jump_control.json`

- [ ] **Step 1:** Implement endpoint-pin / hard wrap-closure classical op.  
- [ ] **Step 2:** Show it can lower wrap-jump while often hurting $R$ (expected tradeoff).  
- [ ] **Step 3:** TeX: “methods that zero wrap-jump are not the same objective as prolonged $R$.”

**Acceptance criteria (Phase F3):**
- [ ] Edge RMSE locked as required secondary in EVAL_PROTOCOL.  
- [ ] Hard-cliff reporting includes edge RMSE for key methods.  
- [ ] Explicit jump-aware control demonstrates objective tradeoff (or document if it fails).  
- [ ] No claim of wrap-jump SOTA for the favorite if numbers stay flat.

---

# Phase F4 — Transfer-failure analysis + search-value narrative

**Effort:** M  
**Answers:** X1, X4; softens residual W1 after F1  
**Depends on:** F1 matrices preferred (can start on current JSON)

### Intent

v6 already admits factory/Rust gaps and N2N≈favorite on sine cliffs. Turn that into a reviewer-proof story: **when** hybrid search wins (hard cliffs, OA instrument track, compact bake without oracle labels) vs **when** identity/FIR/supervised nets win (mild seams, OOD factory geometry).

### Tasks

#### Task F4.1: Failure stratification script

**Files:**
- Create: `reelsynth/scripts/bench_transfer_failures.py`
- Create: `denoise-opt-meta/paper/v7/figures/transfer_failures.json`

- [ ] **Step 1:** Per-cycle $\Delta R$ (favorite − identity) and (favorite − DualCosine) on export + OA + Rust tiles.  
- [ ] **Step 2:** Report win-rate, mean $\Delta R$, worst-10% cycles, correlate with wrap-jump / edge RMSE.  
- [ ] **Step 3:** JSON + short Results paragraph or Discussion subsection “Transfer conditions.”

#### Task F4.2: Search-value narrative (no claim inflation)

**Files:**
- Modify: `discussion.tex`, `introduction.tex` / abstract only if numbers support

Locked talking points:
- On sine+cliff holdout, corrupt→corrupt N2N matches favorite ≈ within $10^{-3}$ — expected for same generator.  
- DenoiseOpt contribution = **discover compact bake graphs without engine→ideal labels at search time** + hard-cliff DualCosine collapse contrast.  
- On true exported WT (after F1), report honestly whether favorite still beats DualCosine / N2N.

- [ ] **Step 1:** Rewrite Discussion N2N paragraph to lead with conditions-of-win.  
- [ ] **Step 2:** Do not claim meta-search superiority on factory if identity leads; call it domain shift.

**Acceptance criteria (Phase F4):**
- [ ] `transfer_failures.json` frozen.  
- [ ] Discussion states win conditions without burying factory/Rust losses.  
- [ ] Abstract still narrow; no speech SOTA pivot.

---

# Phase F5 — Manuscript table unify + polish

**Effort:** S  
**Answers:** X3; polish W9 visibility  
**Depends on:** F2 poly row if available; F1 numbers if ready

### Tasks

#### Task F5.1: Promote modern baselines into main SOTA table

**Files:**
- Modify: `subsections/results.tex` (`tab:sota-main` or new full-width baselines table)
- Regenerate: `figures/sota_matrix.json` if script supports N2N/seq/poly registration

- [ ] **Step 1:** Add rows: N2N corrupt→corrupt, N2N sibling-sup, seq LSTM, seq CNN1D, poly fitter (if F2 done).  
- [ ] **Step 2:** Keep DualCosine / FIR / identity / favorite.  
- [ ] **Step 3:** Caption notes train seeds disjoint from holdout.

#### Task F5.2: Abstract / Limitations sync

**Files:**
- Modify: `main.tex` abstract, `limitations.tex`, `PLAN_PROGRESS.md`
- Create: `WEAKNESS_ELIMINATION_COMPLETE.flag` only when Done-when below is met

- [ ] **Step 1:** Abstract mentions true export realism only after F1 freeze.  
- [ ] **Step 2:** Limitations list poly/SSM status accurately.  
- [ ] **Step 3:** Prose pass: no em dashes; no PESQ; OA cites intact; rebuild PDF.

**Acceptance criteria (Phase F5):**
- [ ] Modern baselines visible in primary comparison surface.  
- [ ] PDF rebuild clean.  
- [ ] denoise-opt-meta-only commit of TeX/JSON/flags.

---

## Done-when: “weaknesses eliminated”

Treat critique weaknesses as **eliminated for DAFx/AES/arXiv DSP venue** when all of the following hold:

| Gate | Criterion |
|------|-----------|
| G1 | Every **CLOSED** ID above remains closed (no theory resurrection; N2N retained; strata retained). |
| G2 | **W1/S1 residual closed:** primary realism = true ReelSynth exports; secondary = external OA files with licenses (F1). |
| G3 | **W8 residual closed:** edge RMSE locked; jump-aware control or explicit tradeoff text; no wrap-jump SOTA overclaim (F3). |
| G4 | **S7 residual closed:** polynomial baseline published; SSM reported or explicitly deferred (F2). |
| G5 | **X1/X4 residual closed:** transfer failure JSON + win-condition narrative (F4). |
| G6 | **REJECT items stay rejected:** no LibriSpeech/MUSDB SOTA, no MUSHRA, no fake theory, no PESQ-on-sine. |
| G7 | Artifacts under `paper/v7/` updated; `WEAKNESS_ELIMINATION_COMPLETE.flag` written; commit+push **denoise-opt-meta only**. |

**Not required for “eliminated”:** beating identity on every factory tile; speech SOTA; perceptual listening study; proving search convergence.

---

## File map (residual phases)

| Path | Role |
|------|------|
| `reelsynth/scripts/real_wt_wrap_protocol.py` | Extend loaders for true exports + OA files |
| `reelsynth/scripts/bench_cliff_strata.py` | Strata + edge RMSE / new baselines |
| `reelsynth/scripts/bench_sota_matrix.py` | Register poly / N2N / seq in main matrix |
| `reelsynth/scripts/baselines/poly_seam_fitter.py` | New classical baseline |
| `reelsynth/scripts/baselines/endpoint_pin.py` | Jump-aware control |
| `reelsynth/scripts/bench_transfer_failures.py` | Win-rate / failure strata |
| `denoise-opt-meta/paper/v7/figures/real_wt_matrix.json` | Realism freeze |
| `denoise-opt-meta/paper/v7/figures/poly_baseline.json` | Poly freeze |
| `denoise-opt-meta/paper/v7/figures/transfer_failures.json` | Transfer freeze |
| `denoise-opt-meta/paper/v7/SAMPLE_LICENSES.md` | True licenses + URLs |
| `denoise-opt-meta/paper/v7/EVAL_PROTOCOL.md` | Edge RMSE lock |
| `denoise-opt-meta/paper/v7/subsections/{results,discussion,limitations,experiments}.tex` | Manuscript |
| `denoise-opt-meta/paper/v7/WEAKNESS_ELIMINATION_COMPLETE.flag` | Completion marker |

---

## Suggested commit sequence (when executing)

1. `docs(paper): weakness elimination plan (post A–E residuals)` — **this file** (plan-only)  
2. `feat(eval): true ReelSynth export + OA file realism matrices` (F1) — meta JSON/TeX in denoise-opt-meta  
3. `docs(paper): lock edge RMSE; jump-aware control table` (F3)  
4. `feat(baselines): polynomial seam fitter JSON + TeX` (F2)  
5. `docs(paper): transfer failure narrative + SOTA table unify` (F4–F5)  
6. `chore(paper): WEAKNESS_ELIMINATION_COMPLETE.flag`

---

## Execution handoff

Plan complete and saved to:

`denoise-opt-meta/paper/v7/WEAKNESS_ELIMINATION_PLAN.md`

**Triage counts:** CLOSED **9** · PARTIAL **5** · STILL OPEN **2** · REJECT **3** (plus W2/S4 REJECT splits).

**Recommended first residual phase:** **Phase F1 (True wavetable-native corpus).**

**Two execution options when ready:**

1. **Subagent-Driven (recommended)** — fresh subagent per task, review between tasks  
2. **Inline Execution** — execute with `superpowers:executing-plans`, batch with checkpoints

Do not start F1–F5 until the user confirms phase start.
