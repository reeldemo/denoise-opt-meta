# Review response map — paper v11 (peer-review paste 2026-07-27)

Point-by-point map from the external peer-style review → DenoiseOpt v11 manuscript.
Locked T0: transfer **keep reframed**; cheap \(R_{\mathrm{blend}}\) only (full 5k = D1); DAFx/AES bar.
Source SDD: `docs/sdd/specs/paper-v11-peer-review-response/`.

Columns: **Verdict** = agree / partial / disagree+why. **Action** = what we changed. **Location** = TeX / artifact path.

## Synopsis fact-check (reviewer numbers)

| Review claim | Verdict | Action | Location |
|--------------|---------|--------|----------|
| Champion \(R_{\mathrm{blend}}{\approx}0.99093\) vs DualCosine \(0.81658\) on primary holdout | **Disagree (wrong metric).** Those are historical **whole-curve prolonged \(R\)** from the superseded \(5\)k-gate freeze, not locked \(R_{\mathrm{blend}}\). | Primary story is Table~\ref{tab:n2n-vs-ours}: holdout Ours \({\approx}0.9697\), N2N \({\approx}0.9750\), Dual Cosine \({\approx}0.5409\). Prolonged \(0.99093\) appears only as superseded freeze / appendix. | `REVIEW_RESPONSE.md` (this row); Intro Key findings; Results §\ref{sec:n2n-vs-ours-boards}; Limitations Metric lock; `METRIC_REGEN.md` |
| “bake-cell” operators \(\Theta\) | **Partial.** Legacy code name. Manuscript term is **repair operator** \(\Theta\) (bake operator). | Terminology primer + Methods Notation already use repair operator. Sweep remaining bake-cell reader-facing prose. | Intro Terminology; Methods §\ref{sec:notation}; NOMENCLATURE.md |
| Hybrid “surpasses” DualCosine on primary holdout under \(R_{\mathrm{blend}}\) | **Agree directionally** on Dual Cosine. **Must not erase:** N2N still beats / gates Ours on holdout \(R_{\mathrm{blend}}\). | Keep honesty in Abstract / Key findings / Discussion. | `main.tex` abstract; Intro; Results; Discussion |

## Strengths (preserve)

| ID | Review item | Verdict | Action | Location |
|----|-------------|---------|--------|----------|
| S1 | Novel problem framing + unsupervised \(R_{\mathrm{blend}}\) / ideal sibling protocol | Agree | Keep framing as primary novelty. | Intro; Methods §\ref{sec:ideal-tile}–\ref{sec:residual-score} |
| S2 | Comprehensive hybrid GA+PPO+PBT meta-search + Algorithms 1–9 | Agree (engineering integration) | Keep; modestly frame as application of hybrid search, not a new learning algorithm. | Methods §\ref{sec:hybrid}; Appendix~\ref{app:algorithms} |
| S3 | Strong empirical results on primary task (reviewer’s \(0.99093\)) | **Partial** — numbers wrong metric; qualitative “hybrid clears Dual Cosine; competitive with N2N” stands under \(R_{\mathrm{blend}}\) | Point readers to `tab:n2n-vs-ours`; keep Dual Cosine gap honesty. | Results §\ref{sec:n2n-vs-ours-boards} |
| S4 | Clear scope / DAFx–AES venue / classical VA baselines | Agree | Preserve Limitations + VA section. | Intro Scope; §\ref{sec:va-seam-baselines}; Limitations |

## Weaknesses

| ID | Review item | Verdict | Action | Location |
|----|-------------|---------|--------|----------|
| W1 | Severe clarity / undefined acronyms (MoE, PBT, FitCell, \(J\), …); DualCosine centering obfuscated | Agree | Acronym pass on first use; DualCosine centering stays Remark~\ref{rem:dualcosine-centering} separate from outer \(J\). | Intro Terminology + first-use expansions; Methods Rem.~\ref{rem:dualcosine-centering}; Related Work polish |
| W2 | Weak justification for non-audio transfer | Agree | **Keep reframed** (T0): one wrap-protocol stress-test paragraph + short seam analogy per domain family. Not diagnosis SOTA. | §\ref{sec:transfer-protocol}; §\ref{sec:transfer-main}; Intro Transfer datasets |
| W3 | Insufficient statistical rigor (param fairness, variance, \(\Delta R{=}{+}0.174\) significance) | Partial | Param counts: favorite \(\Theta\) vs SeamN2N \(\sim 53\)k side-by-side. Error bars where multi-seed exists. \(\Delta R{+}0.174\) labeled superseded prolonged \(R\). Single-run boards stated honestly. | Results param table; `tab:canonical-methods` / `tab:sota-main` ±; Limitations |
| W4 | Overselling integrative novelty as foundational ML | Agree | Soften Abstract / Contributions / Conclusion: hybrid GA–PPO(+PBT) **applied to** cycle-local seam repair. Explicit non-claims. | `main.tex` abstract; §\ref{sec:contributions}; Conclusion |
| W5 | No learning-curve / search-efficiency analysis | Agree | Add champion score vs evaluations (hybrid + Random). Caption states metric honesty (\(R_{\mathrm{blend}}\) vs superseded prolonged \(R\)). | Fig.~\ref{fig:search-learning-curve}; Results paragraph; `scripts/plot_search_learning_curve.py` |

## Suggestions

| ID | Suggestion | Verdict | Action | Location |
|----|------------|---------|--------|----------|
| Sug1 | Major restructuring / acronyms / IMRaD flow; Related Work as motivation not laundry list | Partial (full rewrite out of scope for this cycle) | Clarity pass + acronyms; Related Work already Used vs Screened — polish. Algorithms stay appendix. | Methods; Related Work; Intro |
| Sug2 | Collapse or remove non-audio transfer **or** reframe with per-domain analogy | Agree → **reframe** (T0) | Mechanistic wrap paragraphs; honesty footnotes unchanged. | §\ref{sec:transfer-protocol} |
| Sug3 | Strengthen experimental validation: error bars, branch ablations, learning curves, define \(\Theta\) | Agree within artifact budget | Learning curve fig; branch ablation table from `ablate-*` (prolonged \(R\), labeled); param fairness; \(\Theta\) already formalized. | Fig.~\ref{fig:search-learning-curve}; Table~\ref{tab:ablation}; Results |
| Sug4 | Reframe contributions with modesty | Agree | Same as W4. | Contributions; Abstract; Conclusion |
| Sug5 | Search convergence figure: champion vs outer-loop evals for hybrid + Random | Agree | Same as W5 / Sug3. Random under locked \(R_{\mathrm{blend}}\) not in logs → prolonged-\(R\) matched \(5\)k curve labeled superseded; v10 hybrid \(R_{\mathrm{blend}}\) curve included. | Fig.~\ref{fig:search-learning-curve}; `METRIC_REGEN.md` |

## Deferred (explicit)

| ID | Item | Why |
|----|------|-----|
| D1 | Full matched-\(5\)k outer-loop re-search under \(R_{\mathrm{blend}}\) | T0 / open Q2 |
| D2 | MOS / MUSHRA | Constitution / out of scope |
| D3 | Deep CWRU / ECG diagnosis SOTA | Constitution |

## Regen inventory

See `METRIC_REGEN.md` in this paper folder for boards still prolonged-\(R\)-only and exact commands.
