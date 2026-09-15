# Project Montecito — Experiment 1 to Experiment 2 Migration Manifest — Version 4

## Migration status

**APPROVED WITH RECORDED LEVEL-1 QUALIFICATION**

The two required source artifacts remain unchanged and are fit for Experiment 2:

- `data/zeta_unfolded_points.csv`
- `data/zeta_pair_correlation.csv`

They were independently reproduced from the exported data in peer review and remain the authoritative Experiment 1 outputs.

## Frozen source artifacts

### 1. Unfolded point configuration

\[
X_\zeta=\{x_1,\ldots,x_{10000}\}.
\]

The point configuration is strictly increasing, approximately unit density, and has no missing/NaN entries.

Normalization diagnostics:

\[
\frac{L}{N-1}=1.000023001
\]

(mean nearest-neighbor spacing across the full span), and

\[
\frac{N}{L}=1.000077007
\]

(point density).

These are different but mutually consistent statistics.

### 2. Empirical pair correlation

The raw empirical estimator output remains frozen in

`data/zeta_pair_correlation.csv`.

Version 2 adds, but does not overwrite it:

`data/zeta_pair_correlation_diagnostics_v2.csv`

with bin-averaged GUE expectations, expected counts, ratios, and descriptive residual diagnostics.

## Completeness diagnostic

Version 2 adds

\[
\widetilde S(n)=n-\frac12-x_n.
\]

Observed range:

\[
-0.853239
\le
\widetilde S(n)
\le
0.948472,
\]

with standard deviation **0.288777** and no persistent unit shift.

Combined with indexed spot validation, this provides strong evidence that the exported sequence is contiguous and suitable for migration.

## Known Level-1 discrepancy

The first 10,000 zeros are **not quantitatively identical to the asymptotic GUE two-point function at very short range**.

For \(u<0.5\):

\[
N_{\rm observed}=878,
\qquad
N_{\rm GUE,expected}=1131.46.
\]

This is a **22.4% deficit** relative to the asymptotic GUE expectation.

The empirical correlation hole is wider, with compensating excess at larger sub-unit separations.

At the same time, the correlation-hole sum rule over \(0<u<30\) is

\[
-0.507157,
\]

close to the sine-kernel value \(-1/2\).

## Mandatory interpretation rule for Experiments 2–3

When comparing zeta and synthetic GUE inertia profiles:

1. report the measured Level-1 pair-correlation difference first;
2. propagate the Level-1 difference through the fixed toy apparatus;
3. only then ask whether any remaining Level-2 inertia discrepancy may reflect information beyond pair correlation.

**Do not attribute a raw zeta/GUE inertia difference to higher-order structure merely because the two processes are asymptotically expected to share GUE local statistics.**

## Optional Experiment 1B before final Experiment 3 interpretation

A high-height extension is recommended using Odlyzko blocks near approximately the \(10^{12}\)-th and \(10^{21}\)-st zeros.

Purpose:

- test whether the short-range excess exclusion shrinks with height;
- improve the finite-height interpretation;
- provide a zeta/GUE baseline closer to the asymptotic regime.

This extension is **not required to begin Experiment 2**, but is strongly recommended before final claims about Experiment 3.

## Publication provenance gate

The current numerical zero sequence has independent spot-check agreement at approximately floating-point precision and passes the completeness diagnostics.

A direct machine-ingested rerun using Odlyzko's raw zero table remains required before manuscript submission if the paper states that Odlyzko's file was the actual computational source.

This is a documentation/provenance gate, not an identified numerical defect.


## Version 3 quantitative anchors

When the **first-10,000** zeta configuration is used, carry forward:

- D0.5(single-window) = **0.224010**
- D0.5(matched 10-block) = **0.223872**
- matched-GUE D0.5 SD = **0.024797**
- zeta S30 = **-0.511017**
- matched-GUE mean S30 = **-0.499315**
- matched-GUE S30 SD = **0.006857**

The low-height Level-1 discrepancy is therefore primarily a **shape redistribution with near-conserved integrated correlation-hole mass**.

The High-Height Replication shows that the large low-height D0.5 distortion disappears near zero numbers 10^12 and 10^21.

### Interpretation rule

A Level-2 inertia difference from the first-10,000 configuration must first be compared against propagation of this measured finite-height Level-1 shape distortion. Only residual behavior not explained by the Level-1 difference may be discussed as possible sensitivity beyond pair correlation.


## Version 4: resolved origin and dual-reference policy

The first-10,000 Level-1 distortion is now:

- quantified;
- reproduced independently;
- shown not to be an estimator artifact;
- shown not to be a smooth-unfolding-formula artifact;
- shown not to be an artifact of nonlinear unfolding across a nonstationary window;
- strongly suppressed below an approximately 5.0% D0.5 detection scale at high height.

### Input roles for future experiments

**Primary frozen Experiment 2 input:** keep the first-10,000 `X_zeta` point set when the goal is to study the exact artifact specified by Experiment 1.

**Secondary high-height zeta controls:** retain the near-10^12 and near-10^21 point sets as controls for what zeta looks like when its D0.5 statistic is already inside the matched-GUE range.

Do not silently replace the first-10,000 primary input with high-height data. Any high-height use should be labeled as a control or separately specified extension.

This dual-reference policy prevents two opposite mistakes:
1. mistaking the first-10,000 finite-height distortion for a universal zeta property;
2. erasing the known distortion by swapping in a more asymptotic point set after the fact.
