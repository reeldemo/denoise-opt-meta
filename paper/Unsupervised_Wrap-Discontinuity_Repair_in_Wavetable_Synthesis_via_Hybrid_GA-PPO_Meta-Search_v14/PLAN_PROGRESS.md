# Peer-review + weakness-elimination progress

**Plans:** `PEER_REVIEW_IMPROVEMENT_PLAN.md` (A–E) · `WEAKNESS_ELIMINATION_PLAN.md` (F1–F5)  
**Updated:** 19 July 2026  
**Flags:** `PEER_REVIEW_COMPLETE.flag` · `WEAKNESS_ELIMINATION_COMPLETE.flag`

## Phases A–E (peer review) — DONE

| Phase | Status | Notes |
|-------|--------|-------|
| **A Metric honesty** | **DONE** | Hard-cliff strata + identity-$R$ prose |
| **D Theory cleanup** | **DONE** | Lemma/Props deleted |
| **B N2N + seq** | **DONE** | Corrupt→corrupt + sibling + LSTM/CNN |
| **C Realism (interim)** | **DONE** | Procedural stand-ins (superseded by F1) |
| **E Writing** | **DONE** | Venue DAFx/AES/arXiv |

## Residual phases F1–F5 — DONE

| Phase | Status | Notes |
|-------|--------|-------|
| **F1 True corpus** | **DONE** | ReelSynth export $n{=}25$ primary; AKWF CC0 $n{=}24$ secondary; procedural demoted |
| **F3 Seam metrics** | **DONE** | Edge RMSE locked; `tab:cliff-edge-rmse`; endpoint-pin jump control |
| **F2 Poly (+SSM)** | **DONE** | `poly_baseline.json` $R\approx0.972$; SSM explicitly deferred |
| **F4 Transfer** | **DONE** | `transfer_failures.json` + Discussion win conditions |
| **F5 Unify** | **DONE** | N2N/seq/poly in `tab:sota-main`; abstract/limitations sync; PDF |

## Headline residual numbers (F1–F5)

| Item | Value |
|------|-------|
| Export favorite / identity / DualCosine $R$ | 0.911 / 0.967 / 0.883 |
| AKWF favorite / identity / DualCosine $R$ | 0.970 / 0.969 / 0.937 |
| Poly seam $d{=}3$ canonical $R$ | 0.972 |
| Endpoint-pin hard jump / $R$ | 0.0 / 0.822 |
| Export win-rate fav vs id / vs DC | 0.24 / 0.64 |
| Sine-cliff win-rate fav vs id / vs DC | 0.92 / 1.00 |
| SSM | deferred (LSTM ceiling) |

## Gates G1–G7

- [x] G1 CLOSED IDs remain closed
- [x] G2 W1/S1: true export + OA files
- [x] G3 W8/X2: edge RMSE locked + jump control
- [x] G4 S7: poly published; SSM deferred
- [x] G5 X1/X4: transfer JSON + narrative
- [x] G6 REJECT items stay rejected
- [x] G7 artifacts + flag + denoise-opt-meta commit/push
