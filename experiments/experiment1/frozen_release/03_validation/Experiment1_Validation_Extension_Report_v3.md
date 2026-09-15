# Project Montecito — Experiment 1 Validation Extension Report — Version 2

**Parent:** Project Montecito Experiment 1  
**Revision basis:** second independent peer review plus subsequent High-Height Replication  
**Experiment 2:** not started

## Version 2 change log

Version 2 does **not** change the frozen Experiment 1 source data or any core numerical result. It changes interpretation, statistical framing, and artifact delivery.

The principal revisions are:

1. promote **mass approximately conserved / short-range shape shifted** to the headline scientific finding;
2. reframe the theta-unfolding check as an expected O(1/T) confirmation rather than independent evidence;
3. treat the 8.97-ensemble-SD distance as a descriptive effect size, while direct Monte Carlo enumeration is the inferential result;
4. explain the two correct D0.5 values: single-window geometry versus matched 10-block geometry;
5. retire the preliminary dimension-256 GUE control in favor of the matched dimension-1200 ensemble;
6. correct the incomplete artifact handoff;
7. record that the later High-Height Replication has now resolved the finite-height question.

---

# 1. Headline finding: mass approximately conserved, shape anomalous

Define the finite-height pair-correlation correction conceptually as:

`delta R2(u) = R2_zeta(u; T) - R2_GUE(u)`.

The first 10,000 zeros show a large redistribution inside the first mean spacing:

- substantial deficit for roughly 0.1 < u < 0.5;
- compensating excess at somewhat larger sub-unit separation.

At the same time, the finite-window correlation-hole integral is close to the matched GUE value.

Project Montecito's 200-replicate ensemble gives:

- zeta S30 = **-0.511017**
- GUE mean S30 = **-0.499315**
- GUE SD = **0.006857**
- difference = **-0.011702**

The independent reviewer generated 400 additional GUE replicates with a separate implementation and reports:

- GUE mean S30 = **-0.498186**
- GUE SD = **0.006913**
- corresponding difference from the same zeta S30 = **-0.012831**

These independent calibrations support the same conclusion:

> **The low-height effect is dominated by redistribution of short-range pair-correlation mass rather than a large change in the total correlation-hole mass.**

This is now the primary scientific finding of the Validation Extension.

A candidate finite-height correction formula should therefore reproduce both the local D0.5 distortion and the near-cancellation of the integrated correction over the measured window.

---

# 2. Odlyzko provenance

The numerical provenance conclusion is unchanged.

Eleven official-table anchors differed from the Experiment 1 sequence by at most **1.499e-9**, consistent with the stated table precision. Independent indexed high-precision checks, Hardy-Z checks, monotonicity, and the completeness diagnostic all support the same sequence.

The only remaining `zeros1` item is a **byte-level source lock**: direct machine ingestion of the complete official file and a checksum.

This is a procedural provenance task, not an identified numerical defect. The reviewer correctly notes that it is easy to close in an unrestricted local environment and should not be described in a manuscript as a hard scientific obstacle.

---

# 3. Theta-unfolding sensitivity: analytically expected, numerically confirmed

The two smooth unfoldings are:

- asymptotic Riemann–von Mangoldt smooth count;
- `1 + theta(T)/pi`, where `theta` is the Riemann–Siegel theta function.

Their difference has the standard asymptotic expansion:

`Nbar_theta(T) - Nbar_asym(T) = 1/(48*pi*T) + 7/(5760*pi*T^3) + O(T^-5)`.

Therefore the two smooth unfoldings were expected to be extremely close before the numerical check was run.

The numerical check confirms that expectation:

- maximum position shift: **0.000469298**
- mean position shift: **2.84741e-06**
- maximum nearest-neighbor-spacing change: **0.000153804**
- only **6 of 300** pair-correlation bins changed count
- no bin changed by more than one pair
- the u<0.5 pair count did not change

The correct interpretation is:

> **The theta check closes an implementation/referee question and confirms the expected O(1/T) equivalence of the two smooth unfoldings; it is not independent evidence that the short-range anomaly is physically real.**

Both are global smooth counting functions. Unfolding by the exact staircase N(T) would be inappropriate because mapping each zero to its exact counting index would manufacture a lattice by construction and erase the local-spacing phenomenon being measured.

The previously misleading overlay figure has been retired and replaced by a direct difference plot.

---

# 4. Matched GUE calibration

## Authoritative construction

The authoritative Experiment 1 synthetic control is now the Validation Extension ensemble:

- 200 Monte Carlo replicates;
- 10 independent beta=2 Hermite tridiagonal matrices per replicate;
- matrix dimension 1200;
- semicircle unfolding;
- central 1000 unfolded points retained from each matrix;
- the same 10-block geometry used for the zeta calibration statistic.

The earlier dimension-256 control is historical preliminary work and is no longer used for inference.

## Why two D0.5 values appear

Two D0.5 values are correct because they use different edge geometries.

### Single-window value

Treat all 10,000 zeta points as one observation window:

- D0.5(single) = **0.224010**
- percentage = **22.4010%**

This is the natural descriptive statistic for the complete Experiment 1 sample.

### Matched 10-block value

For comparison to the GUE ensemble, split the zeta sample into ten contiguous 1000-point blocks and apply edge correction within each block:

- D0.5(matched) = **0.223872**

The difference between the two values is entirely due to observation-window geometry. It is not a computational inconsistency.

## Statistical framing

Project Montecito's 200-replicate ensemble has:

- GUE D0.5 mean = **0.001558**
- GUE D0.5 SD = **0.024797**
- GUE replicates at or above zeta = **0/200**

The independent reviewer generated 400 further replicates with a separate sampler and different seed and also reports **0/400** exceedances.

Combining the reported direct enumeration gives **0/600** exceedances, with Monte Carlo resolution:

`1/601 = 0.00166`.

That is the defensible simulation-tail statement.

The zeta statistic is 8.97 Project-Monte-Carlo standard deviations above our ensemble mean, and the independent reviewer reports about 8.75 SD. These are useful **descriptive effect sizes**, not verified Gaussian 9-sigma tail probabilities.

The purpose of the calibration is quantitative: measure the magnitude of the low-height shape distortion. It is not surprising in principle that a finite-height zeta sample differs from the T -> infinity sine-kernel process.

---

# 5. Zeta calibration blocks are not exchangeable

The ten zeta blocks occupy different heights and therefore are not exchangeable samples from a single stationary finite-T distribution.

The pooled matched-block statistic is valid for the intended observation geometry, but **no zeta-side block bootstrap or block-permutation significance test should be used**.

Matched GUE Monte Carlo remains the appropriate calibration mechanism.

---

# 6. Subsequent resolution: High-Height Replication

The Validation Extension originally stopped at the correct statement that finite height was plausible but not yet demonstrated by Project Montecito's own same-statistic rerun.

That open question has since been resolved by the separately documented **Experiment 1 High-Height Replication**.

The same primary statistic gives:

| zeta sample | full-window D0.5 | matched-GUE distance |
|---|---:|---:|
| first 10,000 | 0.2240 | 8.97 SD |
| near zero 10^12 | 0.0162 | 0.65 SD |
| near zero 10^21 | -0.0367 | -1.56 SD |

The large low-height short-range exclusion is suppressed below the approximately 5% D0.5 detection scale in both high-height samples.

The current Project Montecito conclusion is therefore:

> **The 22.4% low-height close-pair deficit is strongly supported as a finite-height phenomenon; at both high heights its magnitude is suppressed below the experiment's approximately 5% D0.5 detection scale and the samples fall within the matched-GUE range.**

No functional convergence law in height is claimed from only three height regimes.

---

# 7. Artifact-delivery correction

The second peer review reported that the delivered folder exposed no CSV artifacts and only two figures.

Inspection after the review found that the original ZIP archive **did contain** the six CSV outputs and four figures, but the separately surfaced handoff directory was incomplete.

Therefore this was a **distribution/handoff defect**, not a missing-computation defect.

Version 2 corrects it by shipping a self-contained package containing:

- all original CSV artifacts;
- the complete 200-replicate Monte Carlo CSV;
- all original figures;
- the corrected unfolding-difference figure;
- the mass-vs-shape diagnostic figure;
- configuration and metrics;
- the peer review;
- an artifact manifest;
- checksums.

---

# 8. Authoritative conclusions after the second review

1. **No frozen Experiment 1 numerical source artifact needs regeneration.**
2. The first-10,000 pair-correlation curve has a real short-range shape distortion.
3. The total correlation-hole mass is approximately conserved; this is the most informative low-height finding.
4. The theta-unfolding check is an expected O(1/T) confirmation, not independent evidence.
5. The matched dimension-1200 GUE ensemble supersedes the preliminary dimension-256 control.
6. The High-Height Replication now directly supports the finite-height interpretation.
7. The Experiment 1 -> Experiment 2 migration rule remains valid and should carry both:
   - the low-height D0.5 distortion;
   - the near-conservation of integrated correlation-hole mass.

**No Experiment 2 work is performed in this report.**


# Version 3 note from High-Height Replication peer review

A third independent review raised a possible confound not addressed by the theta-versus-asymptotic unfolding check: the first-10,000 sample spans a strongly varying local density, whereas the high-height windows are almost affine under unfolding.

That confound has now been tested directly. Restricting the low-height sample to its nearly affine tails gives:

- last 5,000: density ratio 1.088, D0.5 = 0.206
- last 2,500: density ratio 1.035, D0.5 = 0.173
- last 1,000: density ratio 1.012, D0.5 = 0.258

Thus the low-height shape distortion is not an artifact of strongly nonlinear unfolding across the full sample.

The High-Height Replication wording is also sharpened: the anomaly is **suppressed below an approximately 5% detection floor**, not proven to equal zero exactly.
