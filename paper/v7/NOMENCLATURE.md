# Nomenclature — baselines and controls

| Manuscript name | Meaning | Legacy JSON / code key |
|-----------------|---------|------------------------|
| **No-bake (passthrough)** | Unrepaired cracked engine scored vs ideal sibling; $f(x)=x$; no seam op | `identity` |
| DualCosine | Raised-cosine end fades on the cracked engine | `dual_cosine` |
| Favorite / meta favorite | DenoiseOpt hybrid-search champion bake graph | `favorite` |
| Ideal sibling | Same generator draw with open-wrap cliff withheld | `ideal` |

## Why rename `identity` → no-bake

Reviewers read “identity” as (i) residual-net identity skips, (ii) “what is this method’s identity,” or (iii) a learned identity map.
In this paper it only ever meant **leave the cracked engine unchanged**.
Use **no-bake** / **No-bake (passthrough)** in prose and tables; keep reading `identity` from frozen artifacts.