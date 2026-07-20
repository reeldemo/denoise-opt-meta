# Nomenclature — baselines and controls

| Manuscript name | Meaning | Legacy JSON / code key |
|-----------------|---------|------------------------|
| **Ideal sibling** $r^{\star}$ | Same generator draw with open-wrap cliff **withheld**. Scoring target only — not a method. | `ideal` |
| **No-bake (passthrough)** | Unrepaired cracked engine $x$; then score $R(x,r^{\star})$. $f(x)=x$; no seam op. | `identity` |
| DualCosine | Raised-cosine end fades on the cracked engine (classical bake + search reward ref.) | `dual_cosine` |
| `seam_fir3` / poly / VA | Other classical (non-AI) repairs on the same $x\to R(\cdot,r^{\star})$ protocol | various |
| Favorite / meta favorite | DenoiseOpt hybrid-search champion bake graph | `favorite` |

## What is scored against what

```
cracked engine x  --Θ-->  baked y  --ResidualScore-->  R vs ideal sibling r*
                      (no-bake: Θ = identity)
```

- **Ideal sibling** = target (cliff off).
- **No-bake** = do nothing to $x$, still score vs $r^{\star}$.
- Beating no-bake = closer to $r^{\star}$ than the unrepaired engine.

## Comparison policy

Always rank learned methods on **absolute $R$** vs the full classical non-AI board (no-bake, DualCosine, FIR, poly, fades, VA).
$\Delta R$ vs DualCosine alone is a search-reward convenience column, not the only classical comparison.

## Why rename `identity` → no-bake

Reviewers read “identity” as (i) residual-net identity skips, (ii) “what is this method’s identity,” or (iii) a learned identity map.
In this paper it only ever meant **leave the cracked engine unchanged**.
Use **no-bake** / **No-bake (passthrough)** in prose and tables; keep reading `identity` from frozen artifacts.
