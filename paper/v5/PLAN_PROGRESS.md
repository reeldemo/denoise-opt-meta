# Peer-review improvement plan progress

**Plan:** `PEER_REVIEW_IMPROVEMENT_PLAN.md`  
**Updated:** 19 July 2026  
**Flag:** `PEER_REVIEW_COMPLETE.flag` set when phases A–E done.

| Phase | Status | Notes |
|-------|--------|-------|
| **A Metric honesty** | **DONE** | `cliff_strata.json` (4096 tiles, seed 20260719). Top10%: id $R$ 0.9667, DualCosine 0.6574, favorite 0.9915. Edge RMSE + click energy defined. Table `tab:cliff-strata`. |
| **D Theory cleanup** | **DONE** | Lemma 1 + Props 1–3 deleted. Formal $R$ kept. Explicit no wrap-closure / no search-convergence sentence. |
| **B N2N + seq** | **DONE** | Primary corrupt→corrupt $R\approx0.9917$; sibling-sup $R\approx0.9933$; LSTM $R\approx0.9952$; CNN1D $R\approx0.9864`. Train seeds disjoint from holdout. |
| **C Realism** | **DONE** | ReelSynth factory $n{=}24$ + OA instrument $n{=}20$ under wrap protocol. `SAMPLE_LICENSES.md`. No LibriSpeech/MUSDB. |
| **E Writing** | **DONE** | Abstract/discussion/related work/venue (DAFx/AES/arXiv). PDF rebuilt (14 pp). |

## Headline peer-review numbers

| Item | Value |
|------|-------|
| Hard-cliff top10% favorite $R$ | 0.9915 |
| Hard-cliff top10% DualCosine $R$ | 0.6574 |
| Hard-cliff top10% identity $R$ | 0.9667 |
| N2N corrupt→corrupt (primary) | $R\approx0.9917$ |
| N2N sibling-supervised | $R\approx0.9933$ |
| Seq LSTM ceiling | $R\approx0.9952$ |
| Factory favorite / DualCosine | 0.954 / 0.943 |
| OA instrument favorite / DualCosine | 0.988 / 0.944 |

## Cross-phase checklist

- [x] Narrow claim freeze intact
- [x] Cliff strata 10%/25% published
- [x] Identity-$R$ explained; hard-cliff operative
- [x] Primary corrupt→corrupt N2N + sibling + seq
- [x] ReelSynth + OA realism; no LibriSpeech/MUSDB
- [x] Theory cleaned (props/lemma deleted; $R$ kept)
- [x] OA cites; no PESQ-on-sine; no MUSHRA; no em-dash slop
- [x] Canonical artifacts under `denoise-opt-meta/paper/v5/`
