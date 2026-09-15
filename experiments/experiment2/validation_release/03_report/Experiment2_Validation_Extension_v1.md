# Project Montecito — Experiment 2 Validation Extension v1

**Scope:** validation steps 1–3 requested after the Experiment 2 primary run.  
**Specification:** Project Montecito v0.6.  
**Status:** primary Experiment 2 results validated; scientific freeze still awaits the user's independent peer-review audit (Step 4).

## Executive conclusion

The validation extension found **no error that requires re-evaluating or retracting the primary Experiment 2 results**.

Three independent checks were completed:

1. an independent reimplementation of the Gaussian Gram matrix, spectrum, inertia, trace/Frobenius identities, and pair-correlation bridge;
2. the preregistered kernel-width sensitivity checks at `sigma = 0.5` and `sigma = 2`, with `sigma = 1` retained as the frozen primary analysis;
3. deeper spectral diagnostics identifying where the low-height versus high-height differences occur in the spectrum of `C`.

The strongest validation result is that the independently rebuilt `sigma=1` matrices reproduce the published matrix and inertia quantities essentially to floating-point precision. The pair-correlation/Frobenius bridge is also reproduced when the frozen histogram is treated as piecewise constant and the Gaussian/edge weight is integrated exactly over each bin.

## 1. Independent computational reproduction

The validation implementation is separate from the primary Experiment 2 analysis code. It reads only the frozen input CSV files, block manifest, and parameter configuration, then independently constructs

`C_ij = exp(-(x_i-x_j)^2/(2 sigma^2))`

and diagonalizes `C` directly.

At `sigma=1`, the largest absolute independent-vs-primary differences were:

- `mu_min`: 1.639e-15
- `mu_max`: 2.220e-14
- direct `||C||_F^2`: 1.137e-13
- `D_C`: 1.110e-16
- pair-predicted `||C||_F^2`: 2.274e-13
- pair-predicted `D_C`: 5.551e-16
- positive/negative/unresolved inertia counts: **exactly identical for all 2,592 primary block/lambda evaluations**
- normalized positive-inertia bound: 1.110e-16

The full-dataset `D_C` values reproduce to approximately machine precision:

| zeta sample | direct `D_C` | pair-predicted `D_C` | direct minus predicted |
|---|---:|---:|---:|
| first 10,000 | 0.920166507 | 0.920974609 | -0.000808103 |
| near 10^12 | 0.945813929 | 0.946630759 | -0.000816829 |
| near 10^21 | 0.951435314 | 0.953011858 | -0.001576544 |

### Diagnostic encountered during validation

The first independent bridge implementation used the kernel value at each histogram-bin center (a midpoint quadrature). That produced a small but visible mismatch with the frozen result (maximum block `D_C` prediction difference about `5.7e-4`). This was traced to the quadrature convention, not to the matrix data: the frozen analysis treats the empirical `R_2` value as constant across each width-0.1 bin and **integrates `(L-u) exp(-u^2/sigma^2)` analytically over the whole bin**. Implementing that independently reproduces the frozen pair prediction to floating-point precision.

This is a useful validation finding because it confirms that the reported ~0.04% full-data bridge discrepancy is not an artifact of using bin centers.

## 2. Kernel-width sensitivity (`sigma=0.5` and `sigma=2`)

The sensitivity experiment keeps every block and every point fixed and changes only the Gaussian width. The primary analysis remains `sigma=1`.

For the full 10,000-point datasets, direct `D_C` is:

| sample | `sigma=.5` | `sigma=1` | `sigma=2` |
|---|---:|---:|---:|
| first 10,000 | 0.209146 | 0.920167 | 2.606175 |
| near 10^12 | 0.238238 | 0.945814 | 2.625158 |
| near 10^21 | 0.242363 | 0.951435 | 2.630736 |

The asymptotic GUE benchmarks for the same Gaussian weighting are:

- `sigma=.5`: 0.241262
- `sigma=1`: 0.952041
- `sigma=2`: 2.634701

Thus the finite-height ordering seen in the primary analysis is robust: the first-10,000 sample lies below the high-height samples at every tested Gaussian width, and the high-height samples are much closer to the corresponding GUE benchmark.

The pair-correlation/Frobenius bridge also remains quantitatively accurate at all three widths. For `m=512`, the mean absolute relative block discrepancy remains below 1% in every dataset/width combination; the largest single-block value is about 2.63%.

### Important sensitivity result: the inertia curve is kernel dependent

Changing `sigma` changes the spectrum scale of `C`, so the positive-inertia curve as a function of the same fixed `lambda` grid changes quantitatively. For the primary first-10,000 sample (`m=512`):

| lambda | `p_pos`, sigma=.5 | `p_pos`, sigma=1 | `p_pos`, sigma=2 |
|---:|---:|---:|---:|
| 0.35 | 1.000000 | 0.998657 | 0.834961 |
| 0.50 | 0.997559 | 0.776978 | 0.784546 |
| 0.75 | 0.740479 | 0.652954 | 0.743042 |
| 0.95 | 0.596436 | 0.596558 | 0.722290 |


This **does not invalidate** the primary `sigma=1` result: `sigma=1` was preregistered because the points have unit mean spacing, and the sensitivity widths were secondary robustness checks. It does mean that the numerical inertia fractions should not be interpreted as universal properties of the zeta point process independent of the toy kernel. The scientific comparison in Experiment 3 must therefore keep the same frozen kernel and `sigma` across all point processes.

## 3. Deeper spectral diagnostics

The validation confirms that the low-height/high-height difference is concentrated disproportionately in the **spectral tails**, especially the upper edge where the first negative directions appear.

For `m=512`, `sigma=1`, the mean largest eigenvalue and implied first crossing are:

| sample | mean `mu_max(C)` | mean first crossing `1/mu_max` |
|---|---:|---:|
| first 10,000 | 2.857267 | 0.350134 |
| near 10^12 | 3.174937 | 0.315128 |
| near 10^21 | 3.225853 | 0.310351 |

Pooling the 16 `m=512` block spectra gives the following representative quantiles:

| quantile | first 10,000 | near 10^12 | near 10^21 |
|---:|---:|---:|---:|
| 0.010 | 0.006247 | 0.002540 | 0.002128 |
| 0.050 | 0.012730 | 0.008619 | 0.008072 |
| 0.250 | 0.107397 | 0.100653 | 0.099947 |
| 0.500 | 0.658056 | 0.651962 | 0.651426 |
| 0.750 | 1.852215 | 1.840396 | 1.844431 |
| 0.950 | 2.701841 | 2.757917 | 2.758784 |
| 0.990 | 2.794286 | 2.979380 | 3.014965 |
| 0.999 | 2.862505 | 3.177541 | 3.267953 |


The median is nearly unchanged (`~0.65–0.66`), while the top 1% and extreme upper edge differ substantially. This explains why the primary low-height sample can show a pronounced shift in the **first crossing** near `lambda≈0.35` even though the inertia curves become very close over most of the later `lambda` range.

For `m=512`, `sigma=1`, the maximum absolute difference in mean positive fraction between the low-height and `10^21` samples over `lambda >= 0.40` is only **0.00623**, while at `lambda=0.35` the difference is about **0.0286**.

Descriptive pooled-spectrum distances also show that the two high-height controls are much closer to each other than either is to the low-height sample (Wasserstein distances: low vs `10^12` = 0.01560, low vs `10^21` = 0.01770, `10^12` vs `10^21` = 0.00453). These are descriptive finite-sample distances, not independence-based significance tests because the block spectra are structured and overlapping only through their sampling design.

## What has and has not been validated

**Validated:**

- direct construction of the Gaussian Gram matrices;
- PSD behavior of `C` for the primary width;
- direct Frobenius values and their spectral identities;
- the full `sigma=1` inertia counts and crossing behavior;
- the pair-correlation/Frobenius bridge and its bin-integration normalization;
- the finite-height ordering of `D_C` across all three tested kernel widths;
- the qualitative finding that the first-crossing difference is primarily an upper-spectral-tail phenomenon;
- the earlier conclusion that the generic trace/Frobenius positive-inertia bound becomes very loose near `lambda=1`.

**Qualified by validation:**

- exact inertia fractions are **kernel dependent**. They are properties of the frozen toy apparatus, not universal statistics of zeta zeros;
- the impressive pair-bridge agreement is an internal consistency/reconstruction result because both sides summarize the same underlying pair differences through different computational routes; it is not evidence for RH or for the Alpöge–Furman theorem;
- pooled/block spectral comparisons are descriptive; no independence-based p-values are attached to them.

## Validation verdict

**No re-evaluation of the primary Experiment 2 numerical results is required.** The primary `sigma=1` results are independently reproduced. The sensitivity analysis strengthens rather than overturns the finite-height conclusion, while adding an important limitation: inertia depends materially on the chosen kernel bandwidth.

The recommended project state is therefore:

`EXPERIMENT2_PRIMARY_RUN = VALIDATED`

`EXPERIMENT2_STEPS_1_TO_3_VALIDATION = COMPLETE`

`EXPERIMENT2_SCIENTIFIC_FREEZE = PENDING_INDEPENDENT_PEER_REVIEW`

Experiment 3 should **not** be started until the planned peer-review audit is complete and any audit findings are resolved.
