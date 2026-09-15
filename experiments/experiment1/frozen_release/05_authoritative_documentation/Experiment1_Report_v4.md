# Project Montecito — Experiment 1 Report — Version 4

## Experiment

**Pair correlation from the first 10,000 nontrivial zeta-zero ordinates**

**Project specification:** v0.4  
**Report version:** 4  
**Revision basis:** independent peer review and re-analysis of frozen Experiment 1 artifacts

---

## Version 3 documentation update

Version 3 does not change frozen Experiment 1 source data. It supersedes the preliminary dimension-256 GUE control with the matched dimension-1200 ensemble, adopts the second peer review's statistical framing, and records the subsequent High-Height Replication result.

# Executive Summary

Experiment 1 remains **sound, reproducible, and successful under all four Project Montecito v0.4 success criteria**, with one substantive correction to the original interpretation.

The first 10,000 unfolded zeta zeros clearly reproduce the **qualitative GUE/Montgomery pair-correlation structure**: they are strongly non-Poisson, exhibit a deep correlation hole at short distance, and satisfy the sine-kernel correlation-hole sum rule to good finite-window accuracy.

However, the original Version 1 report overstated the quantitative short-range agreement when it said the empirical curve "closely tracks the predicted GUE shape at short range."

Version 2 corrects that statement:

> **At these relatively low heights, the empirical zeta process shows a robust wider correlation hole and stronger short-range exclusion than the asymptotic GUE curve, followed by a compensating excess at larger sub-unit separations.**

For \(0<u<0.5\), the data contain **878** pairs compared with **1131.46** expected from the bin-integrated, edge-weighted asymptotic GUE curve: a **22.4% deficit**.

The overall mass of the correlation hole remains essentially correct. The empirical sum-rule integral through \(u=30\) is

\[
-0.507157,
\]

compared with the sine-kernel infinite-window value

\[
-\frac12
\]

and the GUE finite-window value

\[
-0.498311.
\]

The Experiment 1 artifacts required by Experiment 2 remain valid and unchanged.

---

# 1. Scientific Objective

Experiment 1 produces:

1. the unfolded zeta-zero point configuration
   \[
   X_\zeta=\{x_1,\ldots,x_{10000}\},
   \]
2. the empirical pair-correlation estimate
   \[
   \widehat R_\zeta(u).
   \]

The asymptotic comparison curve is

\[
R_{\rm GUE}(u)
=
1-
\left(
\frac{\sin(\pi u)}{\pi u}
\right)^2.
\]

This is a finite-height point-process experiment. It does **not** test RH and does not reproduce the Alpöge–Furman prime-side second-moment calculation.

---

# 2. Reproducibility Audit

Independent peer review regenerated every originally reported quantity from the exported CSV artifacts.

The peer review found exact or machine-precision agreement for:

- 294,472 pairs in the \(u\le30\) window;
- all 300 histogram-bin counts;
- all empirical pair-correlation values;
- the GUE theory column;
- RMSE, MAE, Pearson correlation;
- long-range mean correlation;
- unfolding statistics.

This confirms that the computational outputs are reproducible from the frozen artifacts.

---

# 3. Data Provenance, Validation, and Completeness

The Version 1 execution environment could view but not directly ingest Odlyzko's raw table, so the first 10,000 ordinates were regenerated numerically and the substitution was explicitly documented.

Independent peer review strengthened validation:

- 10 indexed ordinates spanning 1 through 10,000 were checked against high-precision `mpmath.zetazero`;
- maximum discrepancy was approximately \(1.8\times10^{-12}\);
- sampled Hardy \(Z(\gamma)\) values were near zero;
- indices are contiguous 1 through 10,000;
- \(\gamma_n\) and \(x_n\) are strictly increasing;
- no NaNs occur.

Version 2 adds the completeness/indexing diagnostic

\[
\widetilde S(n)
=
n-\frac12-x_n.
\]

For the exported sequence,

\[
-0.853239
\le
\widetilde S(n)
\le
0.948472,
\]

with

\[
\operatorname{mean}\widetilde S
=
0.0000004,
\qquad
\operatorname{sd}\widetilde S
=
0.288777.
\]

There is no persistent unit shift. Combined with independent indexed checks, this is strong evidence that the 1–10,000 sequence is complete and correctly indexed.

The direct Odlyzko raw-file rerun remains a manuscript-level provenance requirement, but the current evidence makes it a **low numerical-risk documentation gate**, not an identified data-quality defect.

---

# 4. Unfolding

Use

\[
\overline N(T)
=
\frac{T}{2\pi}
\log\left(\frac{T}{2\pi}\right)
-
\frac{T}{2\pi}
+
\frac78
\]

and

\[
x_n=\overline N(\gamma_n).
\]

With

\[
L=x_N-x_1,
\]

the two normalization diagnostics are explicitly distinguished.

Mean spacing across the full span:

\[
\frac{L}{N-1}
=
1.000023001.
\]

Point density:

\[
\frac{N}{L}
=
1.000077007.
\]

They are different statistics but mutually consistent with unit-density unfolding.

---

# 5. Pair-Correlation Estimator

For positive separations

\[
d_{ij}=x_j-x_i,\qquad j>i,
\]

retain

\[
0<d_{ij}\le30.
\]

For bin \(B_k=[a_k,b_k]\), the stationary-process expectation is

\[
\mathbb E[C_k]
=
\rho^2
\int_{B_k}
R_2(v)(L-v)\,dv.
\]

The implemented translation-edge-corrected histogram estimator is

\[
\widehat R_2(u_k)
=
\frac{C_k}
{\widehat{\rho^2}(L-u_k)\Delta u},
\qquad
\widehat{\rho^2}
=
\frac{N(N-1)}{L^2}.
\]

The factor \(L-u\) is the interval translation edge correction.

### Version 2 theoretical comparison

The original report plotted the theoretical GUE value at the bin center.

Version 2 uses the **bin-averaged GUE curve** for density comparisons and the exact edge-weighted bin integral for expected counts:

\[
E_k^{\rm GUE}
=
\widehat{\rho^2}
\int_{a_k}^{b_k}
R_{\rm GUE}(v)(L-v)\,dv.
\]

This matters mainly in the first bin and removes a small avoidable comparison bias.

The endpoint-conditioned density estimate introduces only an \(O(1/N)\) effect here.

---

# 6. Estimator Controls

## 6.1 Poisson unit test

The original 100-replicate Poisson test remains a strong PASS.

The estimated mean curve is essentially flat at the expected Poisson value

\[
R_2(u)=1.
\]

## 6.2 Authoritative matched GUE control

The preliminary Version 2 dimension-256 synthetic-GUE check is **retired as a preliminary control**.

The authoritative Experiment 1 calibration is the Validation Extension's matched ensemble:

- 200 independent Monte Carlo replicates;
- 10 beta=2 Hermite tridiagonal matrices per replicate;
- matrix dimension 1200;
- central 1000 unfolded bulk points retained from each matrix;
- the same 10-block geometry used for the zeta calibration statistic.

For the matched statistic:

- zeta D0.5 = **0.223872**
- GUE mean D0.5 = **0.001558**
- GUE SD = **0.024797**
- Project Montecito exceedances = **0/200**

A second independent peer review generated 400 additional replicates with a separate implementation and also reported zero exceedances.

The standardized distance (8.97 SD in our ensemble) is retained only as a **descriptive effect size**. The simulation-supported inferential statement is the direct enumeration result, not a Gaussian 9-sigma tail extrapolation.

The same calibration shows that the integrated correlation-hole mass is much less anomalous than the local u<0.5 shape.


---

# 7. Main Zeta Pair-Correlation Finding

The experiment reproduces the qualitative GUE structure but shows a systematic short-range displacement relative to the asymptotic GUE curve.

Selected bins:

| u | observed count | GUE expected count | observed/expected | naive count diagnostic |
|---:|---:|---:|---:|---:|
| 0.05 | 5 | 10.9 | 0.46 | -1.78 |
| 0.15 | 37 | 74.1 | 0.50 | -4.31 |
| 0.25 | 121 | 190.9 | 0.63 | -5.06 |
| 0.35 | 282 | 344.0 | 0.82 | -3.34 |
| 0.45 | 433 | 511.5 | 0.85 | -3.47 |
| 0.55 | 642 | 672.1 | 0.96 | -1.16 |
| 0.65 | 805 | 808.0 | 1.00 | -0.11 |
| 0.75 | 1032 | 908.2 | 1.14 | +4.11 |


The count diagnostics are **descriptive, not formal independent-bin hypothesis tests**, because pair counts and neighboring bins are dependent.

The coherent pattern is nevertheless clear:

- deficit across approximately \(0.1\lesssim u\lesssim0.5\);
- return toward the GUE level near \(u\approx0.6\);
- compensating excess around \(u\approx0.75\).

Integrated through \(u=0.5\):

\[
N_{\rm observed}=878,
\qquad
N_{\rm GUE,expected}=1131.46,
\]

a relative deficit of

\[
22.4\%.
\]

Integrated through \(u=1\), the total mass deficit is only

\[
1.59\%.
\]

Thus the strongest result is a **shape redistribution**: the correlation hole is wider than the asymptotic GUE hole, while much of the mass reappears at somewhat larger sub-unit separations.

---

# 8. Correlation-Hole Sum Rule

For the sine-kernel determinantal process,

\[
\int_0^\infty
(R_2(u)-1)\,du
=
-\frac12.
\]

Experiment 1 gives, over the finite interval \(0<u<30\),

\[
\int_0^{30}
(\widehat R_\zeta(u)-1)\,du
=
-0.507157.
\]

The GUE curve integrated over the identical finite interval gives

\[
-0.498311.
\]

This is an important parameter-free check: the **total missing correlation mass is very close to the sine-kernel value**, even though its short-range distribution is measurably shifted.

---

# 9. Uncertainty and Inference

The original 20-block standard errors remain useful **descriptive variability measures**.

They should not be interpreted as calibrated per-bin inferential standard errors.

In the nominally flat region \(u>5\):

- residual scatter versus the GUE curve: **0.04899**
- mean exported block SE: **0.03296**
- ratio: **1.49**
- fraction of bins exceeding nominal \(\pm1.96\) block-SE: **21.2%**

This demonstrates that the block bands are too narrow for formal binwise inference.

Version 2 therefore does **not** multiply all standard errors by a universal correction factor. Formal significance calibration, if required for the paper, should use matched synthetic GUE/CUE Monte Carlo ensembles and statistics defined before inspecting the result.

---

# 10. Finite-Height Interpretation

The asymptotic GUE curve is a \(T\to\infty\) prediction.

The observed low-height deviation is plausibly a finite-height arithmetic correction, but Experiment 1 alone does not demonstrate that attribution.

Height quartiles show the directionally expected but statistically unresolved pattern:

| quartile   |   gamma_min |   gamma_max |   median_log_gamma_over_2pi |   observed_pairs_u_lt_0_5 |   gue_expected_pairs_u_lt_0_5 |   deficit_fraction |
|:-----------|------------:|------------:|----------------------------:|--------------------------:|------------------------------:|-------------------:|
| Q1         |     14.1347 |     3031.29 |                     5.6036  |                       205 |                       282.846 |           0.275225 |
| Q2         |   3032.76   |     5447.86 |                     6.52074 |                       224 |                       282.874 |           0.208128 |
| Q3         |   5448.91   |     7708.22 |                     6.95581 |                       215 |                       282.881 |           0.239964 |
| Q4         |   7709.24   |     9877.78 |                     7.24497 |                       234 |                       282.813 |           0.172599 |

The first quartile has a larger \(u<0.5\) deficit than the fourth, but the present height lever arm is too short for a strong extrapolation.

The correct statement is:

> **The short-range deviation is real and robust in the first 10,000 zeros. The subsequent High-Height Replication shows that the large deficit disappears near zero numbers 10^12 and 10^21, strongly supporting the finite-height interpretation.**

A future Experiment 1B using Odlyzko high-height blocks would provide a much stronger test.

---

# 11. Outcome Assessment Against v0.4

## Criterion 1 — Poisson baseline

**PASS.**

## Criterion 2 — expected short-range suppression and qualitative GUE agreement

**PASS WITH MATERIAL QUALIFICATION.**

The qualitative GUE/Montgomery structure is reproduced, but quantitative agreement with the asymptotic GUE curve is not close at very short range. Instead, the first 10,000 zeros show stronger exclusion and a wider correlation hole.

## Criterion 3 — robustness

**PASS.**

The qualitative effect survives sample-subwindow and bin-width changes.

## Criterion 4 — Experiment 2 artifacts

**PASS.**

The frozen source artifacts remain:

- `data/zeta_unfolded_points.csv`
- `data/zeta_pair_correlation.csv`

---

# 12. Experiment 1 to Experiment 2 Migration

The two frozen artifacts are valid and should **not** be overwritten.

Version 2 adds diagnostics and a migration manifest.

The key interpretation rule is:

> **A future zeta-versus-synthetic-GUE inertia difference cannot be interpreted as evidence of sensitivity beyond pair correlation until the already-measured Level-1 pair-correlation difference has first been quantified and propagated through the toy apparatus.**

This prevents an Experiment 3 Level-1 discrepancy from being mislabeled as a Level-2 effect.

---

# 13. Final Experiment 1 Version 2 Conclusion

> **The first 10,000 unfolded zeta zeros are strongly non-Poisson and reproduce the qualitative sine-kernel/GUE pair-correlation structure. At the same time, they exhibit a robust, systematically wider short-range correlation hole than the asymptotic GUE curve: approximately 22.4% fewer pairs than the asymptotic GUE expectation occur below half a mean spacing. The missing mass is largely redistributed, and the finite-window correlation-hole sum rule is close to the sine-kernel value \(-1/2\). The later High-Height Replication shows that this large short-range deficit disappears near zero numbers 10^12 and 10^21, strongly supporting a finite-height origin.**

Experiment 1 remains successful and fit for migration to Experiment 2.

---

# 14. Version 2 Files

## Frozen source artifacts

- `data/zeta_unfolded_points.csv`
- `data/zeta_pair_correlation.csv`
- `data/zeta_zeros_10000_validated.csv`

## Added Version 2 diagnostics

- `data/zeta_pair_correlation_diagnostics_v2.csv`
- `data/short_range_diagnostics_v2.csv`
- `data/completeness_diagnostic_v2.csv`
- `data/sum_rule_v2.csv`
- `data/height_quartile_diagnostics_v2.csv`
- `data/synthetic_gue_control_v2.csv`
- `report/metrics_v2.json`

## Added Version 2 documentation

- `report/Experiment1_Report_v2.md`
- `report/Experiment1_Peer_Review_Response_v2.md`
- `report/Experiment1_to_Experiment2_Migration_Manifest_v2.md`
- `README_v2.md`

## Added Version 2 figures

- `figures/pair_correlation_short_range_v2.png`
- `figures/synthetic_gue_control_v2.png`
- `figures/sum_rule_v2.png`


# Subsequent high-height resolution

After this report's original low-height analysis, Project Montecito completed a High-Height Replication using 10,000 zeros near zero numbers 10^12 and 10^21.

The same full-window D0.5 statistic changed from:

- first 10,000: **0.2240**
- near 10^12: **0.0162**
- near 10^21: **-0.0367**

Both high-height samples fall within the frozen matched-GUE calibration. More precisely, the low-height anomaly is suppressed below an approximately 5% D0.5 detection scale at high height; the experiment does not establish an exactly zero correction.


# Version 4 closure of the nonlinear-unfolding confound

The third High-Height Replication peer review raised a legitimate concern: the first-10,000 sample is much less stationary in its raw ordinate scale than the high-height windows.

We tested nearly affine low-height tails directly:

| subsample | endpoint density ratio | D0.5 |
|---|---:|---:|
| last 5,000 | 1.088 | 0.206 |
| last 2,500 | 1.035 | 0.173 |
| last 1,000 | 1.012 | 0.258 |

The last 1,000 zeros change theoretical local density by only about 1.25% across the window, yet retain a large positive D0.5.

Therefore the first-10,000 short-range distortion is not produced by the nonlinear unfolding geometry.

# Version 4 high-height resolution language

The strongest current statement is:

> **The low-height D0.5 distortion is strongly suppressed at much greater height and is no longer detectable above the present experiment's approximately 5% D0.5 scale.**

This is stronger and more precise than saying the effect "vanishes." It leaves open smaller finite-height corrections below current resolution.
