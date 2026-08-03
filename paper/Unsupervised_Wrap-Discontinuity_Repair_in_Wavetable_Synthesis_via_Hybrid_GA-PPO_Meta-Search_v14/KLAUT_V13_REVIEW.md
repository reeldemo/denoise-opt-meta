# Klaut v13 peer review — DenoiseOpt

**Paper id:** `unsupervised-wrap-discontinuity-repair-in-waveta-a2139527`  
**Pass:** `reviews/pass_20260731T170418Z`  
**Model:** `qwen2.5:14b` (local Ollama; MCP default `qwen3.5:9b` returned empty JSON)  
**Pipeline:** Stage A sections (22) → Stage B 3 personas → Stage C meta

## Scores

| | Value |
|--|------:|
| Overall (editor) | **5 / 10** |
| Mean persona overall | 5.33 |
| Systems PC | 5 |
| Formal methods | 6 |
| Empirical eval | 6 |
| Aggregate recommendation | **revise** |
| Convergence | `needs_another_pass` → English polish handoff |

### Axis means (1–5)

| Axis | Mean |
|------|-----:|
| Significance | 3.33 |
| Originality | 3.67 |
| Validity | 3.0 |
| Clarity | 2.67 |
| Prior work | 3.33 |

## Consensus must-fixes (and our response)

| Ask | Decision |
|-----|----------|
| Abstract lacks concrete numbers | **Accepted** — abstract now reports 5-seed holdout mean±std, multi-family edge, and 3-seed D1 hybrid $0.9748{\pm}0.0018$ |
| Eval protocol needs more statistical detail | **Partial** — already have 5-seed ±std, win frac, sign test; D1 3-seed ±std in Table `tab:meta-approaches`. Not inventing MOS/THD |
| Discussion clarity / stale D1 prose | **Accepted** — discussion updated to multi-seed numbers; “until D1” removed |
| Ethics / data-availability regenerate figures | **Accepted** — seeds + D1 paths + regen scripts named |
| Transfer “real-world” overclaim | **Keep** — already framed as stress test; no domain diagnosis |

## Honesty locks (unchanged)

- Holdout: Ours $0.9708{\pm}0.0014$ < N2N $0.9767{\pm}0.0015$ on **0/5** seeds.
- Multi-family mean-of-means edges N2N; win frac $0.47$; sign $p{=}1.0$.
- D1: hybrid leads $0.9748{\pm}0.0018$; only 1/3 seeds beats N2N gate.
- No invented THD+N / MOS.

## Artifacts

- Klaut pass dir: `…/klaut_artifacts/…/v01/reviews/pass_20260731T170418Z/`
- PDF: `Unsupervised_Wrap-Discontinuity_Repair_in_Wavetable_Synthesis_via_Hybrid_GA-PPO_Meta-Search_v13.pdf`

## Harness note

Final `ReviewNote` append crashed when an LLM put a finding-dict inside `must_fix` (expected `list[str]`). Pass artifacts (`summary.json`, persona reviews, meta) were already written. Gateway `review.py` now coerces dict items to summary strings.
