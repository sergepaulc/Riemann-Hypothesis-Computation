# Project Montecito — Experiment 2 to Experiment 3 Migration Manifest
## Version 1

**Date:** 2 September 2026  
**Closure package:** Part 5 of 6  
**Migration status:** **APPROVED FOR EXPERIMENT 3 SPECIFICATION DRAFTING, WITH MANDATORY GATES**  
**Experiment 2 status:** **SCIENTIFICALLY CLOSED**  
**Experiment 3 execution status:** **NOT AUTHORIZED**  
**Working successor title:** **Experiment 3 — Higher-Order Spectral Diagnostics and Controlled Falsification**

---

# 1. Purpose

This manifest is the formal bridge between the closed Experiment 2 phase and the design of Experiment 3.

Its purpose is to decide, before a new experiment is specified or run:

- which Experiment 1 data and conclusions remain valid and may be reused;
- which Experiment 2 artifacts remain frozen historical results;
- which Experiment 2 lessons and safeguards must become Experiment 3 design requirements;
- which observables and interpretations are retired;
- which higher-order ideas may migrate only as unvalidated candidates;
- which controls are mandatory, conditional, or out of scope;
- what scientific question Experiment 3 is authorized to pursue;
- what must be demonstrated before any positive or negative result is interpretable;
- what outcomes will count as positive, informative negative, or inconclusive.

This document is a **migration and change-control artifact**. It is not the full Experiment 3 scientific specification, does not freeze detailed Experiment 3 parameters, and does not authorize computation.

---

# 2. Authority and controlling record

This manifest follows the completed Experiment 2 closure record.

The controlling upstream documents are:

1. `Project_Montecito_Project_Specifications_v0.6.md` — frozen design baseline for Experiments 1 and 2;
2. `Experiment2_Review_Corpus_Index_v1.md` — authoritative provenance map for the seven-document review corpus;
3. `Experiment2_Peer_Review_Response_v1.md` — controlling finding-by-finding disposition of the two scientific peer-review documents;
4. `Experiment2_Report_v2.md` — controlling revised scientific interpretation of Experiment 2;
5. `Experiment2_Closure_Report_v1.md` — formal closure certificate and boundary between Experiment 2 and successor work.

The Experiment 2 closure decision is not reopened by this manifest.

The original Experiment 3 section of Project Montecito v0.6 remains part of the historical specification, but it is **not authorized for execution unchanged**. A separately versioned Experiment 3 specification must supersede it for future execution.

---

# 3. Formal migration decision

Project Montecito makes the following decision:

> **Experiment 1 remains frozen and reusable. Experiment 2 remains closed and is preserved as the validated first apparatus and diagnostic baseline. Experiment 3 will not simply repeat the original Gaussian-inertia comparison. It will be redesigned around a demonstrably higher-order spectral measurement, with controlled point-process comparators, boundary-bias validation, power calibration, and falsification gates.**

The decision can be summarized as:

```text
EXPERIMENT1_STATUS                     = FROZEN_AND_REUSED
EXPERIMENT1_RERUN                      = NOT_REQUIRED
EXPERIMENT2_STATUS                     = CLOSED_AND_PRESERVED
EXPERIMENT2_REPLACEMENT                = NOT_PERMITTED
EXPERIMENT2_GAUSSIAN_TOY_ROLE          = HISTORICAL_BASELINE_AND_CONTROL
EXPERIMENT3_SCIENTIFIC_DIRECTION       = HIGHER_ORDER_SPECTRAL_DIAGNOSTICS
EXPERIMENT3_CONTROL_DIRECTION          = CONTROLLED_COMPARATORS_AND_FALSIFICATION
EXPERIMENT3_SPECIFICATION              = NOT_YET_WRITTEN
EXPERIMENT3_PREREGISTRATION            = NOT_YET_FROZEN
EXPERIMENT3_EXECUTION                  = NOT_AUTHORIZED
PROJECT_MONTECITO_VERSION_2            = NOT_STARTED
```

This is a migration approval, not a result forecast.

---

# 4. Scientific rationale for the migration

Experiment 2 established an information hierarchy that now controls successor design:

| Experiment 2 observable | Information level |
|---|---|
| \(\operatorname{tr}H_\lambda=m(1-\lambda)\) | no point-set information |
| \(\lVert H_\lambda\rVert_F^2\) | one Gaussian-weighted two-point scalar through \(D_C\) |
| \(b_{\mathrm{pos}}(\lambda)\) | the same scalar \(D_C\), through an algebraic formula |
| full spectrum / inertia | potentially higher-order, but no separable higher-order contribution was isolated |

Experiment 2 therefore succeeded as a computation and as a diagnosis of the first apparatus, but not as a clean detector of structure beyond pair correlation.

The migration is based on one central rule:

\[
\boxed{
\text{Choose an observable whose information level matches the scientific question.}
}
\]

Experiment 3 is authorized to pursue the higher-order question only through an observable whose dependence on configurations beyond averaged two-point information is stated and tested explicitly.

---

# 5. Experiment 1 assets approved for migration

## 5.1 Frozen data and results

The following Experiment 1 assets migrate unchanged:

1. the first 10,000 unfolded zeta-zero point set;
2. the low-height empirical pair-correlation artifacts;
3. the matched-GUE calibration and its fixed methodology;
4. the low-height short-range \(D_{0.5}\) distortion;
5. the high-height point sets near zero numbers \(10^{12}\) and \(10^{21}\);
6. the corresponding high-height pair-correlation measurements;
7. the conclusion that the large low-height \(D_{0.5}\) distortion is suppressed below the experiment's approximately \(5\%\) detection scale at the two high heights;
8. the raw-data provenance, official-file checksums, processed-data checksums, and unfolding records.

These assets remain valid because the limitations discovered in Experiment 2 concern the downstream apparatus and observables, not the upstream zero data or pair-correlation measurements.

## 5.2 No Experiment 1 repetition

Experiment 3 does **not** require Experiment 1 to be redone.

The existing point sets and pair-correlation results may be reused as:

- development data;
- two-point baselines;
- finite-height controls;
- high-height random-matrix comparisons;
- inputs to a new higher-order apparatus.

## 5.3 New data are an Experiment 3 extension, not an Experiment 1 reopening

A core-plus-halo estimator or confirmatory holdout may require more points around a measurement window than are presently contained in a selected Experiment 1 block.

If additional zeros are needed, they must be acquired and validated as **new Experiment 3 inputs**. This does not reopen or replace Experiment 1.

The new specification must state:

- the authoritative source;
- exact index and height range;
- precision;
- checksum;
- unfolding convention;
- whether the data are development, calibration, replication, or confirmatory holdout data.

## 5.4 Existing zeta samples have been observed during design

The low-height, near-\(10^{12}\), and near-\(10^{21}\) samples have already influenced the project, and an exploratory fourth-moment value has already been reported for a high-height sample.

They may therefore be used honestly for:

- estimator development;
- debugging;
- halo selection studies;
- qualitative replication;
- comparison with prior exploratory values.

They must not be presented as fully unseen confirmatory data.

A strong confirmatory claim about a newly designed higher-order statistic should, where feasible, use a **fresh preregistered high-height holdout block** not used to select the estimator or its parameters.

---

# 6. Experiment 2 assets approved for migration

## 6.1 Frozen apparatus and artifacts

The following migrate as immutable historical baselines:

- the Gaussian kernel definition;
- the frozen \(\sigma=1\) reference apparatus;
- the \(\lambda\)-grid;
- the block manifest and nested locations;
- the spectra and crossing thresholds;
- the inertia tables;
- the finite-window and kernel-sensitivity outputs;
- the verification suite and validation implementation;
- `Experiment2_Report_v2.md`;
- `Experiment2_Closure_Report_v1.md`;
- the complete review and reconciliation record.

They may be cited, compared, or reused as controls. They may not be silently edited, regenerated as replacements, or reinterpreted under the superseded Report v1 framing.

## 6.2 Role of the Gaussian toy in Experiment 3

The Gaussian family

\[
H_\lambda=I-\lambda C
\]

may migrate only as:

1. a historical first instrument;
2. a two-point-dominated baseline;
3. an implementation and process-sensitivity control;
4. a contrast with the new explicitly higher-order measurement.

It is not the primary higher-order detector for Experiment 3.

Where an Experiment 2 result already exists, the archived output should be reused rather than recomputed merely to create a new-looking result.

If the Gaussian apparatus is applied to a genuinely new Experiment 3 input, that run belongs to the Experiment 3 package and must use either:

- the exact frozen Experiment 2 configuration; or
- a separately preregistered configuration clearly labeled as new and not comparable without qualification.

No result-dependent tuning of \(m\), \(\sigma\), or \(\lambda\) is permitted.

## 6.3 Methodological assets that migrate as mandatory rules

The following Experiment 2 lessons become Experiment 3 requirements:

- preregistration before zeta output is examined;
- exact distinction between mathematical identity, numerical approximation, and empirical observation;
- independent implementation of central quantities;
- checksum-locked inputs and machine-readable outputs;
- process-specific unfolding;
- an automatic mean-spacing-near-one assertion;
- explicit numerical sign or precision-resolution logic where eigenvalues are used;
- fixed window and scale rules across compared processes;
- realization noise measured separately from within-sample block variation;
- negative controls treated as gates rather than optional decorations;
- matched thinning whenever omission creates a subset process;
- no universal conclusion from two stress-test examples;
- no novelty claim before a targeted literature review.

---

# 7. Items that do not migrate as scientific claims

The following are retired and may not appear as positive Experiment 3 premises:

1. the claim that the Gaussian pair-correlation bridge is independent evidence about zeta zeros;
2. the claim that the \(D_C\) height sequence is independent of Experiment 1's two-point evolution;
3. the use of \(b_{\mathrm{pos}}\) as a process discriminator;
4. the use of \(\mu_{\max}\) as a general rigidity proxy;
5. the arithmetic or RH interpretation of the raw number-variance ladder for on-line subsets;
6. a direct Christoffel-function-to-simple-zero-proportion conversion;
7. a universal statement that the Gaussian toy contains only pair-correlation information;
8. a universal statement that an ordinate-only Hermitian apparatus cannot detect RH failure;
9. the claim that the original Experiment 3 is already complete or unnecessary;
10. the claim that Experiment 3 is computationally ready merely because Experiment 2 was internally stable;
11. the claim that high-height residuals vanish exactly;
12. any convergence-rate claim from the three existing height regimes;
13. any assertion that a new higher-order signal would validate, improve, or numerically reproduce the Alpöge–Furman theorem.

These items remain in the historical record with their proper labels: reframed, withdrawn, retracted, closed, or not established.

---

# 8. Experiment 3 scientific question

## 8.1 Primary question

Experiment 3 is authorized to ask:

> **Can a numerically validated, explicitly higher-order spectral statistic reveal a reproducible feature of zeta-zero configurations that is not accounted for by the two-point structure already measured in Experiment 1?**

This is narrower and more defensible than asking whether a toy matrix can detect RH or discover a new theorem.

## 8.2 Secondary questions

Experiment 3 may also ask:

1. Does the candidate higher-order statistic recover its known or simulated behavior on lattice, Poisson, and random-matrix controls?
2. Does the statistic stabilize under increasing halo, core size, precision, and independent implementation?
3. How does the low-height finite-height distortion appear at the higher-order level?
4. Do high-height zeta samples agree with matched random-matrix ensembles at both the two-point and higher-order levels?
5. If a difference appears, is it larger than realization noise, finite-window variation, and estimator bias?
6. Can missing-point effects be separated from arithmetic effects by matched thinning?
7. What information is—and is not—visible when RH-false functions are represented only by surviving on-line ordinates?

## 8.3 Questions not authorized as primary Experiment 3 claims

Experiment 3 is not designed to:

- prove or disprove RH;
- estimate the percentage of zeros satisfying RH;
- improve a simple-zero or critical-line proportion;
- test the Alpöge–Furman approximately \(0.682\) bandwidth-one ceiling;
- reconstruct the analytic prime-side higher moments required by that theorem;
- certify a universal property of all Hermitian approaches;
- infer critical-line membership from data that do not contain the real parts of zeros.

---

# 9. Candidate higher-order architecture

## 9.1 Sinc-kernel spectral moments

The leading candidate transferred from the Experiment 2 review cycle is the sinc-kernel Gram matrix

\[
K_{ij}
=
\operatorname{sinc}(x_i-x_j)
=
\begin{cases}
\dfrac{\sin \pi(x_i-x_j)}{\pi(x_i-x_j)}, & i\ne j,\\[2mm]
1, & i=j.
\end{cases}
\]

Define normalized spectral moments

\[
\mu_k
=
\frac{1}{n}\operatorname{tr}(K^k).
\]

The migration roles are:

| Moment | Migration role |
|---|---|
| \(\mu_1\) | normalization and implementation check |
| \(\mu_2\) | two-point validation level, linked to Experiment 1 |
| \(\mu_3\) | potentially higher-order diagnostic, but not the primary separator for the stated extremal comparison |
| \(\mu_4\) | leading candidate higher-order statistic |

## 9.2 Why the fourth moment is the leading candidate

For the stated first-two-moment extremal spectral distribution, with atoms \(0,1,2\) and weights \(1/6,2/3,1/6\), the first four moments are

\[
1,
\qquad
\frac{4}{3},
\qquad
2,
\qquad
\frac{10}{3}.
\]

The quoted sine-process targets are

\[
1,
\qquad
\frac{4}{3},
\qquad
2,
\qquad
\frac{13}{4}.
\]

The first three moments agree, while the fourth differs:

\[
\frac{10}{3}-\frac{13}{4}
=
\frac{1}{12}.
\]

Thus \(\mu_4\), not \(\mu_3\), is the first moment separating those two specific spectral models.

This arithmetic is accepted as a design motivation. It is not yet a novelty claim and does not itself establish that a finite zeta computation will discriminate the models reliably.

## 9.3 Raw \(\mu_4\) is higher-order-capable, not purely higher-order

The expansion

\[
\operatorname{tr}(K^4)
=
\sum_{i,j,k,\ell}
K_{ij}K_{jk}K_{k\ell}K_{\ell i}
\]

contains terms with four distinct indices as well as terms in which indices coincide.

Therefore raw \(\mu_4\):

- can contain genuine three- and four-point information;
- also contains lower-order contributions from repeated-index patterns;
- may correlate with changes already visible in \(R_2\) or \(\mu_2\).

The Experiment 3 specification must prevent the phrase “higher-order statistic” from being silently upgraded to “pure higher-order signal.”

Before attributing a zeta difference to structure beyond pair correlation, the design must do at least one of the following:

1. demonstrate Level-1 agreement in pair correlation and \(\mu_2\) before interpreting a \(\mu_4\) difference;
2. decompose \(\mu_4\) by index-collision class and report the all-distinct or otherwise genuinely higher-order contribution;
3. compare against a preregistered surrogate or ensemble matched at the measured two-point level;
4. provide another explicit mathematical argument showing why the observed contrast cannot be explained by the lower-order terms.

The exact choice belongs in the Experiment 3 specification.

---

# 10. Core-plus-halo numerical gate

## 10.1 Reason for the gate

The exploratory fourth-moment calculation found material block-edge bias. A statistic that depends on closed products

\[
K_{ij}K_{jk}K_{k\ell}K_{\ell i}
\]

can be biased when intermediate indices outside a chopped block are omitted.

Matched-bias cancellation alone is not sufficient for a primary claim.

## 10.2 Required estimator form

The leading validation design is a core-plus-halo estimator.

Let \(I_c\) be a central core index set and \(I_h\supset I_c\) a larger halo-augmented index set. Construct the sinc matrix \(K^{(h)}\) on all points in \(I_h\), but measure only diagonal contributions originating in the core:

\[
\widehat\mu_{k,\,c|h}
=
\frac{1}{|I_c|}
\sum_{i\in I_c}
\left[(K^{(h)})^k\right]_{ii},
\qquad k\in\{2,4\}.
\]

Increase the halo according to a preregistered sequence while holding the core fixed.

## 10.3 Required halo diagnostics

Before zeta interpretation, the experiment must report:

- the halo sequence in unfolded distance and/or point count;
- \(\widehat\mu_{2,c|h}\) and \(\widehat\mu_{4,c|h}\) at every halo size;
- changes between successive halo sizes;
- numerical precision and algorithmic error;
- computation time and memory use;
- agreement between two independent implementations or algorithms;
- the same halo-stability study on at least one exact or simulated control.

## 10.4 Gate decision

The Experiment 3 specification must preregister a quantitative stabilization rule relative to:

- the target fourth-moment gap \(1/12\);
- the estimated realization noise;
- the desired effect-detection threshold.

If the estimator fails the halo-stability rule, the experiment stops before a zeta claim is made.

---

# 11. Control architecture

Controls have distinct roles and may not be treated as interchangeable.

## 11.1 Mandatory instrument-validation controls

### A. Lattice

The integer lattice is an exact structural anchor for the sinc kernel because nonzero integer differences give vanishing sinc entries. It tests normalization, indexing, and matrix-power implementation.

### B. Poisson

A unit-rate Poisson process supplies a non-rigid, non-repulsive comparator and tests whether the statistic has meaningful dynamic range.

### C. Random-matrix / sine-process comparator

A repeated CUE, GUE, or other clearly specified sine-process approximation supplies the primary asymptotic comparator.

The future specification must select and freeze:

- one primary generator;
- matrix size or point-count regime;
- bulk extraction or circular construction;
- unfolding convention;
- number of independent realizations;
- random seeds or seed-generation rule.

CUE and GUE may both appear, but they may not be mixed without explicitly different roles.

## 11.2 Mandatory zeta comparisons

The existing zeta samples have different roles:

- **first 10,000 zeros:** finite-height development and stress-test sample;
- **near \(10^{12}\):** high-height replication/control sample;
- **near \(10^{21}\):** high-height development/control sample closest to the asymptotic regime among the frozen inputs.

Because exploratory higher-moment information has already been observed, a fresh high-height holdout is strongly preferred for a confirmatory positive claim.

## 11.3 Mandatory matched-thinning control when subsets are used

Whenever an analysis selects only a subset of zeros or deletes points, it must include a matched-thinning control.

For independent retention probability \(p\), the exact number-variance identity

\[
\Sigma^2_{\mathrm{thin}}(L)
=
p^2\Sigma^2_{\mathrm{orig}}(L/p)
+(1-p)L
\]

must be treated as a baseline confound, not as an arithmetic signal.

The same principle applies more broadly: omission-induced changes must be compared with non-arithmetic deletion under the same retention and unfolding rules.

## 11.4 RH-false stress tests

Davenport–Heilbronn and the selected Epstein zeta may migrate as **secondary stress-test classes**, subject to all of the following:

- their computations must be independently packaged and reproducible before promotion to primary evidence;
- finite-window counting deficits must not be stated as universal proportions;
- the exact point representation supplied to the apparatus must be declared;
- on-line-only controls test the geometry of surviving on-line ordinates, not direct sensitivity to the zeros' real parts;
- matched thinning is required for any missing-point interpretation.

## 11.5 Control representations that are deferred

The following are not automatically included in the first Experiment 3 implementation:

1. all-zero ordinate multisets preserving repeated ordinates from symmetric off-line pairs;
2. full complex-zero inputs retaining \(\beta\) as well as \(\gamma\);
3. a faithful finite Weil-type construction.

They require distinct mathematical objects and may become later Experiment 3 extensions or Project Montecito Version 2 work.

---

# 12. Level-1 versus higher-order interpretation rule

Experiment 1 remains the Level-1 baseline.

For every zeta-versus-random-matrix comparison, Experiment 3 must report in this order:

1. pair correlation under the relevant window and unfolding;
2. \(\mu_2\) or another explicit two-point validation statistic;
3. halo, window, and realization-noise diagnostics;
4. \(\mu_4\) or the selected higher-order observable;
5. any lower-order contribution decomposition or matched-two-point control;
6. only then, a possible higher-order interpretation.

A low-height \(\mu_4\) difference is not automatically higher-order because the low-height sample already has a known Level-1 distortion.

The cleanest initial higher-order test is a comparison in which the zeta and random-matrix samples already agree at the preregistered Level-1 resolution.

If Level 1 differs materially, the higher-order result may still be reported descriptively, but it cannot be presented as a residual beyond pair correlation without further analysis.

---

# 13. Power, noise, and sensitivity requirements

Internal stability is not sufficient to establish scientific power.

Before the primary zeta comparison, Experiment 3 must quantify:

- between-realization variation of the random-matrix control;
- within-sample location variation;
- core-size and halo-size variation;
- numerical/algorithmic variation;
- sensitivity to the target gap \(1/12\) or another preregistered effect size;
- false-positive behavior under matched null comparisons;
- the minimum detectable effect under the final design.

The future specification must define:

- the primary test statistic;
- null ensemble;
- effect-size metric;
- uncertainty interval;
- multiplicity policy for secondary observables;
- stopping rule;
- power criterion.

The design must demonstrate that it could detect a scientifically meaningful contrast before interpreting a null result as informative.

---

# 14. Experiment 3 staged authorization

Experiment 3 must proceed through gates. Passing one gate does not authorize skipping the next.

## Gate 0 — Scientific specification

Produce and approve a versioned Experiment 3 specification containing the exact mathematical object, data roles, parameters, estimators, controls, success criteria, and resource budget.

## Gate 1 — Implementation and exact-control validation

Demonstrate basic identities, lattice behavior, process-specific unfolding, unit-spacing assertions, and agreement between independent implementations.

## Gate 2 — Core-plus-halo validation

Demonstrate stable \(\mu_2\) and \(\mu_4\) estimates under the preregistered halo rule on non-zeta controls.

## Gate 3 — Power calibration

Use repeated independent random-matrix and Poisson realizations to establish dynamic range, noise, and minimum detectable effect.

## Gate 4 — Development zeta analysis

Apply the frozen estimator to the existing Experiment 1 zeta samples, explicitly labeling them as previously observed development/control data.

## Gate 5 — Falsification and confound controls

Run matched thinning where applicable, separate Level-1 from higher-order changes, and test any arithmetic stress controls under their declared representation.

## Gate 6 — Confirmatory holdout or qualified replication

Where feasible, run the frozen design on a fresh high-height zeta holdout. If no holdout is available, classify the result as exploratory or internally replicated rather than fully confirmatory.

## Gate 7 — Independent review and freeze

An independent reviewer must audit the mathematics, implementation, data provenance, boundary control, power analysis, and interpretation before Experiment 3 is frozen.

No gate may be passed by tuning the statistic after viewing the result it is meant to test.

---

# 15. Predeclared Experiment 3 outcome classes

Experiment 3 has three legitimate outcome classes.

## 15.1 Positive candidate result

A positive candidate result requires all of the following:

- the estimator passes implementation and halo-stability gates;
- the design has demonstrated adequate power;
- the effect exceeds realization noise and finite-window variation under the preregistered rule;
- the effect survives independent implementation;
- the relevant Level-1 behavior is matched or explicitly accounted for;
- the effect survives falsification and thinning controls;
- the result replicates on a holdout or clearly separated dataset where feasible.

The permitted conclusion is:

> **A candidate higher-order zeta-zero signal was detected by the preregistered finite statistic under the tested conditions.**

It is not immediately a discovery about RH. It triggers independent replication, literature review, theoretical interpretation, and a possible **Project Montecito Version 2**.

## 15.2 Informative negative result

An informative negative result requires:

- a validated and stable estimator;
- demonstrated power to detect the preregistered meaningful contrast;
- properly functioning controls;
- no reproducible zeta departure beyond the uncertainty and sensitivity threshold.

The permitted conclusion is:

> **At the tested heights, scales, and sensitivity, the validated higher-order statistic found no detectable departure from the matched comparator beyond the measured two-point structure.**

This is a scientifically valuable result and can complete a coherent three-experiment Project Montecito paper.

## 15.3 Inconclusive result

The result is inconclusive if any central condition fails, including:

- halo nonconvergence;
- uncontrolled block bias;
- inadequate power;
- control failure;
- dependence on result-selected parameters;
- disagreement between implementations;
- missing provenance;
- a measured effect smaller than the design uncertainty;
- inability to separate Level-1 propagation from a higher-order contribution.

An inconclusive result may motivate redesign, but it may not be promoted to a positive or informative negative finding.

---

# 16. Claim and language rules

Experiment 3 must distinguish:

- **exact identity**;
- **numerical reproduction**;
- **finite-sample observation**;
- **control result**;
- **candidate higher-order signal**;
- **informative null result**;
- **inconclusive result**;
- **conjectural interpretation**.

The following language rules apply:

1. Use “higher-order statistic” when describing \(\mu_4\) before attribution.
2. Use “higher-order structure” only after lower-order explanations have been controlled under the preregistered design.
3. Use “candidate signal” rather than “discovery” before independent confirmation and literature review.
4. Use “no detectable departure at the tested sensitivity” rather than “no higher-order structure exists.”
5. Do not use a positive or null result as evidence for or against RH.
6. Do not describe a finite computation as validating the Alpöge–Furman theorem.
7. Do not claim novelty for the fourth-moment observation without a targeted literature search.
8. Report all negative controls and failed interpretations, not only favorable results.

---

# 17. Project chronology and publication role

The scientific chronology is preserved:

1. **Experiment 1:** established the pairwise and finite-height baseline.
2. **Experiment 2:** tested the first Hermitian apparatus and diagnosed its information limits.
3. **Experiment 3:** will test a deliberately higher-order observable under stronger controls.

This produces a coherent research arc whether Experiment 3 yields a positive candidate result or an informative negative result.

The current working paper title may remain:

> **A Computational Walk Toward Higher-Order Structure in the Zeta Zeros**

with a possible technical subtitle:

> *Pair Correlation, Hermitian Toy Models, and Higher Spectral Moments*

This title is a nonbinding publication concept. The publication decision and final title remain outside this migration manifest.

---

# 18. Change-control rules

## 18.1 Experiment 2 remains closed

A new kernel, statistic, halo, control, data block, or scientific question does not reopen Experiment 2.

## 18.2 New Experiment 3 specification required

Before computation begins, the project must produce a separately versioned document, provisionally:

`Project_Montecito_Experiment3_Specification_v1.md`.

It must state which portions of the original v0.6 Experiment 3 plan are retained, revised, or superseded.

## 18.3 No silent parameter changes

After preregistration:

- any material change requires a dated amendment;
- development and confirmatory data roles may not be changed after results are viewed;
- unsuccessful configurations remain in the execution log;
- no robustness result may replace the primary result merely because it is more favorable.

## 18.4 Independent review before freeze

Experiment 3 may not be declared complete or paper-ready until its primary computation, validation package, negative controls, and interpretation receive independent review.

---

# 19. Migration register

| Item | Migration disposition | Experiment 3 role |
|---|---|---|
| First 10,000 unfolded zeta zeros | **MIGRATE UNCHANGED** | low-height development and finite-height stress test |
| Near-\(10^{12}\) zeta points | **MIGRATE UNCHANGED** | high-height replication/control |
| Near-\(10^{21}\) zeta points | **MIGRATE UNCHANGED** | high-height development/control |
| Experiment 1 pair correlation | **MIGRATE UNCHANGED** | Level-1 baseline |
| Experiment 1 finite-height conclusion | **MIGRATE WITH EXISTING QUALIFICATION** | interpretation of low/high comparisons |
| Experiment 2 Gaussian apparatus | **MIGRATE AS FROZEN BASELINE** | historical and two-point-dominated control |
| Experiment 2 inertia outputs | **MIGRATE AS DESCRIPTIVE BASELINE** | comparison only |
| Spectrum-first and validation methods | **MIGRATE** | reproducibility template |
| Pair bridge | **MIGRATE AS QUADRATURE/CODE CHECK ONLY** | implementation validation |
| \(D_C\) | **MIGRATE AS TWO-POINT SCALAR** | Level-1 smoothing diagnostic |
| \(b_{\mathrm{pos}}\) | **RETIRE AS DISCRIMINATOR** | optional algebraic sanity check only |
| \(\mu_{\max}\) rigidity interpretation | **WITHDRAWN** | descriptive only if reported |
| Raw number variance as RH-sensitive result | **RETRACTED** | not a primary observable |
| Matched thinning | **MIGRATE AS MANDATORY CONFOUND CONTROL** | subset/deletion analyses |
| Christoffel-to-proportion route | **CLOSED** | no migration without new analytic theory |
| Sinc-kernel \(\mu_2\) | **MIGRATE AS CANDIDATE VALIDATION LEVEL** | two-point check |
| Sinc-kernel \(\mu_3\) | **MIGRATE AS SECONDARY DIAGNOSTIC** | not primary separator |
| Sinc-kernel \(\mu_4\) | **MIGRATE AS LEADING CANDIDATE** | higher-order primary candidate after validation |
| Core-plus-halo method | **MIGRATE AS MANDATORY NUMERICAL GATE** | boundary-bias control |
| Lattice, Poisson, CUE/GUE | **MIGRATE AS DISTINCT CONTROL CLASSES** | exact anchor, dynamic range, asymptotic comparator |
| DH/Epstein on-line subsets | **MIGRATE WITH NARROW QUALIFICATION** | secondary RH-false stress tests |
| All-zero ordinate multiset | **DEFER** | possible later extension |
| Full complex-zero / Weil-type apparatus | **DEFER** | possible Montecito Version 2 or separate project |
| Universal apparatus-blindness claim | **NOT MIGRATED** | unsupported |
| Original v0.6 Experiment 3 readiness claim | **NOT MIGRATED** | replaced by gated specification process |

---

# 20. Artifact and provenance continuity

The migration decision relies on the following closure artifacts:

| Artifact | Role | SHA-256 |
|---|---|---|
| `Experiment2_Review_Corpus_Index_v1.md` | review provenance map | `007015954e626245347f805d74f58d05e372269a882a6d3f8dc2f9d4f75c5ff2` |
| `Experiment2_Peer_Review_Response_v1.md` | formal peer-review reconciliation | `34d5e0ce436d607cfb4464f86986d0c4d6e8e89400d400aa2e6df2f58839bd4b` |
| `Experiment2_Peer_Review_Response_v1_Support.zip` | targeted closure verification | `8d304597e3ba4845e2c4efb516c6d34f67956124ac5617b92c8955d98d7a7c37` |
| `Experiment2_Report_v2.md` | controlling Experiment 2 scientific report | `38782299c171f0e2b7abe3dfc2c7455ff62cbaaa95bf39b4693a014b0cfd2c94` |
| `Experiment2_Closure_Report_v1.md` | formal Experiment 2 closure certificate | `5258b559d585f5121d8867edfec61e83a879fd26fa77b5de78687c280ab0db2e` |

The frozen primary and validation archive hashes remain as recorded in the closure report.

The future Experiment 3 package must include its own configuration, input hashes, execution log, machine-readable outputs, code, environment lock, validation package, and independent review record.

---

# 21. Migration certificate

Project Montecito certifies:

> **Experiment 2 is closed and will not be rewritten. Its validated computation, information-content diagnosis, failed interpretations, and methodological safeguards migrate into successor design. Experiment 1 remains frozen and reusable. Experiment 3 is approved for specification drafting as a higher-order spectral and controlled-falsification experiment, but no computation is authorized until the new estimator, data roles, core-plus-halo gate, control architecture, power criterion, and outcome rules are preregistered.**

Formal status:

```text
PROJECT_MONTECITO_MIGRATION_2_TO_3

Migration decision: APPROVED_WITH_MANDATORY_GATES
Experiment 1: frozen, unchanged, reusable
Experiment 2: scientifically closed, preserved as baseline
Primary successor question: higher-order structure beyond measured pair correlation
Leading candidate: boundary-controlled sinc-kernel fourth spectral moment
Mandatory numerical gate: core-plus-halo stability
Mandatory controls: lattice, Poisson, repeated random-matrix ensemble
Conditional controls: matched thinning and independently packaged RH-false stress tests
Confirmatory preference: fresh preregistered high-height holdout
Experiment 3 specification: required
Experiment 3 computation: not authorized
Project Montecito Version 2: not started
```

---

# 22. Part 5 completion and next-step boundary

This document completes:

> **Part 5 — `Experiment2_to_Experiment3_Migration_Manifest_v1.md`**

of the six-part Experiment 2 closure package.

It decides the scientific inheritance and successor-design constraints. It does not:

- run a sinc-kernel calculation;
- select final core and halo sizes;
- freeze the primary random-matrix generator;
- acquire a new holdout zero block;
- reproduce the peer reviewer's DH/Epstein packages;
- write the full Experiment 3 specification;
- begin Project Montecito Version 2;
- finalize the paper or software-companion plan.

The remaining closure-package work is Part 6: update the Experiment 2 closure README/status record and produce the final closure reproducibility manifest or archive index.

After Part 6, the first successor-research artifact should be:

`Project_Montecito_Experiment3_Specification_v1.md`.

No Part 6 work and no Experiment 3 computation are performed in this document.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1 | 2 September 2026 | Initial formal migration decision from the closed Experiment 2 Gaussian apparatus to a gated higher-order Experiment 3 design |
