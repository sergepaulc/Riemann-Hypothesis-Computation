# Project Montecito — Experiment 1 Peer-Review Response — Version 4

## Scope

This document records the disposition of the independent peer review of Project Montecito Experiment 1.

The peer review independently recomputed the experiment from the exported CSV artifacts and concluded that the experiment is sound and reproducible, while identifying one substantive interpretation error in the original report: the phrase **"closely tracks the predicted GUE shape at short range"** understated a systematic short-range deviation.

## Disposition

| Peer-review recommendation | Decision | Version 2 action |
|---|---|---|
| Correct the short-range GUE interpretation | Accepted | Main finding rewritten as qualitative GUE structure plus systematic stronger short-range exclusion |
| Distinguish mean spacing and density | Accepted | Definitions stated explicitly |
| Add completeness diagnostic | Accepted with cautious wording | Added \(\widetilde S(n)=n-1/2-x_n\) diagnostic as strong evidence of indexing/completeness |
| Use bin-averaged GUE expectation | Accepted | Added exact bin-integrated, edge-weighted GUE expected counts |
| Add sine-kernel sum rule | Accepted | Added finite-window sum-rule diagnostic |
| Add synthetic GUE control | Accepted | Added independent fixed-seed GUE pipeline control |
| Treat block bands as descriptive | Accepted | Report no longer uses them for formal per-bin inference |
| Multiply all standard errors by 1.48 | Not adopted as a formal calibration | The 1.49 factor is reported diagnostically; formal inference is deferred to matched Monte Carlo ensembles |
| Attribute deviation to finite height | Accepted only as a hypothesis | Report states finite height is plausible and directionally supported, not demonstrated |
| Direct Odlyzko-file rerun | Retained as publication provenance gate | Classified as low numerical risk because independent checks already agree |
| Carry Level-1 discrepancy into Experiment 2/3 | Strongly accepted | Added a formal migration rule and migration manifest |

## Independent rechecks added in Version 2

### Correlation-hole sum rule

For the sine-kernel process,

\[
\int_0^\infty (R_2(u)-1)\,du=-\frac12.
\]

Using the Experiment 1 empirical histogram through \(U=30\),

\[
\int_0^{30}(\widehat R_\zeta(u)-1)\,du
=
-0.507157.
\]

The bin-averaged GUE curve over the same finite interval gives

\[
-0.498311.
\]

### Short-range pair deficit

For \(0<u<0.5\):

- observed zeta pairs: **878**
- bin-integrated/edge-weighted GUE expectation: **1131.46**
- relative deficit: **22.4%**

For \(0<u<1\), the integrated mass deficit is only **1.59%**, confirming that the main discrepancy is a redistribution of short-range shape rather than a comparable loss of total mass.

### Authoritative matched GUE pipeline control

The earlier dimension-256 control is retained only as historical preliminary work and is no longer used for inference.

The authoritative control is the Validation Extension's 200-replicate dimension-1200 matched GUE ensemble:

- zeta matched D0.5 = **0.223872**
- GUE mean = **0.001558**
- GUE SD = **0.024797**
- exceedances = **0/200**

The second independent reviewer generated 400 additional replicates and also reported zero exceedances.

The ensemble-SD distance is descriptive only. Direct Monte Carlo enumeration is the inferential statement.

The mass-vs-shape result is now the more informative scientific summary: strong local redistribution occurs while the S30 correlation-hole integral remains close to the GUE value.

## Scientific correction

The Experiment 1 Version 2 conclusion is:

> **The first 10,000 unfolded zeta zeros reproduce the qualitative sine-kernel/GUE pair-correlation structure but exhibit a robust wider correlation hole and stronger short-range exclusion than the asymptotic GUE curve. The missing short-range mass is largely redistributed rather than absent, as shown by the near-satisfaction of the sine-kernel sum rule. A finite-height explanation is plausible but is not established by this dataset.**

## Migration consequence

The frozen Experiment 1 point configuration and empirical pair-correlation artifacts remain valid.

However, the known Level-1 zeta/GUE discrepancy must be carried into later interpretation:

> **A Level-2 inertia difference between zeta and synthetic GUE cannot be interpreted as sensitivity to higher-order structure until the measured Level-1 pair-correlation difference has first been quantified and propagated through the toy apparatus.**


## Subsequent high-height resolution

The later Experiment 1 High-Height Replication directly measured the same statistic:

- first 10,000 D0.5 = **0.2240**
- near 10^12 D0.5 = **0.0162**
- near 10^21 D0.5 = **-0.0367**

This now strongly supports the finite-height interpretation.


## High-Height Replication peer-review refinement

A third end-to-end review reproduced every High-Height Replication number. It identified a nonlinear-unfolding confound, which was then closed by testing nearly affine tails of the low-height sample.

The high-height wording is now calibrated to the experiment's resolution: the 22.4% low-height anomaly is suppressed below an approximately 5% D0.5 detection scale at high height, rather than proven to equal zero exactly.
