# Project Montecito — Project Specifications and Paper Outline — Version 0.7

## A Computational Walk Toward Higher-Order Structure in the Zeta Zeros

**Version:** 0.7  
**Draft date:** September 3, 2026  
**Approval and freeze date:** September 4, 2026  
**Release status:** **APPROVED AND FROZEN**  
**Release class:** Post–Experiment 2 scientific consolidation and pre–Experiment 3 design release  
**Approval record:** `Project_Montecito_v0.7_Approval_and_Freeze_Record_v1.md`  
**Experiment 1 status:** **SCIENTIFICALLY CLOSED AND FROZEN**  
**Experiment 2 status:** **SCIENTIFICALLY CLOSED AFTER INDEPENDENT REVIEW**  
**Experiment 3 status:** **DETAILED SPECIFICATION DRAFTING AUTHORIZED; EXECUTION NOT AUTHORIZED**  
**Public reproducibility repository gate:** **REQUIRED BEFORE EXPERIMENT 3 EXECUTION**

---

# Version 0.7 — Release Purpose and Authority

Version 0.7 is **formally approved and frozen** and supersedes Version 0.6 as the current project-level specification for Project Montecito.

It does **not** rewrite the historical design of Experiments 1 or 2, replace their frozen data, or alter their completed numerical results. Instead, Version 0.7:

1. records the completed scientific state of Experiments 1 and 2;
2. incorporates the formal Experiment 2 closure decision;
3. incorporates the approved Experiment 2-to-Experiment 3 migration rules;
4. replaces the original Version 0.6 Experiment 3 plan with a higher-order, gated successor direction;
5. updates the paper outline to match the current manuscript and working title;
6. adopts a stricter source-reliability policy for external mathematical claims;
7. removes the dedicated adjacent-preprint discussion introduced in Version 0.6 from the active scientific specification.

Version 0.6 remains an immutable historical record of the pre–Experiment 2 design. Where Version 0.7 and Version 0.6 differ about current project status, Experiment 2 interpretation, or future Experiment 3 direction, **Version 0.7 controls**. The exact approved Version 0.7 bytes are identified by the SHA-256 fingerprint recorded in the separate approval-and-freeze record and checksum sidecar.

## Controlling upstream artifacts

| Artifact | Role | SHA-256 |
|---|---|---|
| `Project_Montecito_Project_Specifications_v0.6.md` | Frozen pre–Experiment 2 design baseline | `70ade4842e9eabbdaf352876266247b14cb7569fa7c57216905969a08ed15a2a` |
| `Experiment2_Report_v2.md` | Controlling revised Experiment 2 scientific report | `38782299c171f0e2b7abe3dfc2c7455ff62cbaaa95bf39b4693a014b0cfd2c94` |
| `Experiment2_Closure_Report_v1.md` | Formal Experiment 2 closure certificate | `5258b559d585f5121d8867edfec61e83a879fd26fa77b5de78687c280ab0db2e` |
| `Experiment2_to_Experiment3_Migration_Manifest_v1.md` | Controlling migration and successor-design rules | `bbc9fd437dd81b9c37c11e9d7589fd6ee74425bce488374f845e23593a6f66c8` |
| `Project_Montecito_Paper_Working_Draft_Sections_1_4_v0.2.1.md` | Current working manuscript through Experiment 2 | `d393ae3cc397b91a5840cf88e16375696aa0b329119d0bff0d00116df5664106` |

## Current status block

```text
PROJECT_MONTECITO_VERSION                  = 0.7
PROJECT_MONTECITO_SPECIFICATION_STATUS     = APPROVED_AND_FROZEN
PROJECT_MONTECITO_APPROVAL_DATE            = 2026-09-04
EXPERIMENT1_SCIENTIFIC_STATUS              = CLOSED_AND_FROZEN
EXPERIMENT1_RERUN                          = NOT_REQUIRED
EXPERIMENT2_SCIENTIFIC_STATUS              = CLOSED_AFTER_INDEPENDENT_REVIEW
EXPERIMENT2_COMPUTATION                    = COMPLETE_AND_REPRODUCED
EXPERIMENT2_INTERPRETATION                 = REVISED_AND_FROZEN
EXPERIMENT2_REPLACEMENT                    = NOT_PERMITTED
EXPERIMENT2_FORMAL_NAME                    = FIRST_HERMITIAN_INSTRUMENT
EXPERIMENT3_DIRECTION                      = HIGHER_ORDER_SPECTRAL_DIAGNOSTICS
EXPERIMENT3_DIRECTION_APPROVAL             = ACCEPTED
EXPERIMENT3_CONTROL_DIRECTION              = CONTROLLED_COMPARATORS_AND_FALSIFICATION
EXPERIMENT3_SPECIFICATION_DRAFTING         = AUTHORIZED
EXPERIMENT3_DETAILED_SPECIFICATION         = NOT_YET_FROZEN
EXPERIMENT3_EXECUTION                      = NOT_AUTHORIZED
SOURCE_RELIABILITY_POLICY                  = APPROVED_AND_FROZEN
PUBLIC_REPRODUCIBILITY_REPOSITORY_GATE     = REQUIRED_BEFORE_EXPERIMENT3_EXECUTION
PROJECT_MONTECITO_VERSION_2                = NOT_STARTED
CURRENT_PAPER_DRAFT                        = SECTIONS_1_TO_4_VERSION_0_2_1
```

---

# Version 0.7 — Main Design Decisions

1. **Experiment 1 remains frozen.**  
   Its low-height and high-height zero data, pair-correlation measurements, finite-height conclusions, provenance, and checksums remain valid. No Experiment 1 rerun is required.

2. **Experiment 2 is closed, not overwritten.**  
   The Gaussian Hermitian instrument is retained as the validated First Hermitian Instrument and historical baseline. A new kernel, statistic, or research question belongs to successor work and does not reopen Experiment 2.

3. **Experiment 2 is characterized as a meaningful diagnostic limitation.**  
   Its computation is correct and reproducible, but most advertised summary observables were structurally unable to isolate higher-order information beyond the measured two-point level.

4. **The Experiment 1-to-Experiment 2 pair bridge is reconstruction, not independent evidence.**  
   The direct Gaussian pair energy and the histogram reconstruction use the same pair differences. The bridge remains useful for normalization, quadrature, smoothness, and code-path validation.

5. **The information level of the observable must match the scientific question.**  
   This becomes the governing principle for Experiment 3.

6. **The original Version 0.6 Experiment 3 will not be executed unchanged.**  
   Experiment 3 will not merely rerun the Gaussian Hermitian instrument on GUE, Poisson, and lattice inputs. Those processes remain valuable controls, but the primary successor measurement must be explicitly capable of carrying higher-order information.

7. **The leading Experiment 3 candidate is a boundary-controlled sinc-kernel fourth spectral moment.**  
   The candidate is
   \[
   \mu_4=\frac{1}{n}\operatorname{tr}(K^4),
   \qquad
   K_{ij}=\operatorname{sinc}(x_i-x_j).
   \]
   This is a design candidate, not yet a frozen primary result.

8. **Raw \(\mu_4\) is higher-order-capable, not automatically a pure higher-order signal.**  
   Repeated-index terms can carry one- and two-point contributions. The Experiment 3 design must separate, match, or account for those lower-order components before using the phrase “higher-order structure.”

9. **Core-plus-halo validation is mandatory before zeta interpretation.**  
   A fourth-moment estimator must stabilize as the halo grows around a fixed central core. Matched-bias cancellation alone is not sufficient for a primary claim.

10. **Synthetic and arithmetic controls have distinct roles.**  
    Lattice, Poisson, and a repeated random-matrix/sine-process ensemble validate the instrument and measure dynamic range. RH-false functions, if used, are separate stress tests and must state exactly what zero information is supplied to the instrument.

11. **Existing zeta samples are development and replication data, not fully unseen confirmation data.**  
    The first \(10{,}000\), near-\(10^{12}\), and near-\(10^{21}\) samples have already influenced the design. A fresh preregistered high-height holdout is strongly preferred for a confirmatory positive claim.

12. **Experiment 3 must be adequately powered before a null result is called informative.**  
    Between-realization noise, window dependence, halo dependence, numerical error, and minimum detectable effect must be quantified before the primary zeta comparison.

13. **Experiment 3 has three legitimate outcomes.**  
    The result may be a positive candidate signal, an informative negative result, or an inconclusive result. The outcome rules must be fixed before computation.

14. **Experiment 3 is not an RH detector.**  
    It studies higher-order organization in known zero ordinates. It does not prove or disprove RH, estimate the fraction of zeros satisfying RH, or directly observe critical-line membership from data that omit the zeros’ real parts.

15. **A separate detailed Experiment 3 specification remains mandatory.**  
    Version 0.7 authorizes the scientific direction. It does not freeze core size, halo sequence, random-matrix generator, realization count, test statistic, power threshold, holdout block, or computational budget. Those belong in `Project_Montecito_Experiment3_Specification_v1.md`.

16. **The project adopts a stricter external-source policy.**  
    Load-bearing mathematical claims must come from published primary literature, authoritative datasets, or clearly identified recent preprints whose status and independent support are stated explicitly. Author-controlled code or an arXiv posting alone is not sufficient to make an unreviewed claim controlling background.

17. **The active analytic context is Alpöge–Furman plus Lamzouri.**  
    Their 2026 preprints give complementary unconditional proofs of the same proportion results through different representations of a quadratic/second-moment mechanism. Both are clearly labeled as recent preprints rather than silently treated as settled journal literature.

18. **The current working paper title is updated.**

   > **A Computational Walk Toward Higher-Order Structure in the Zeta Zeros**  
   > *Pair Correlation, Hermitian Instruments, and Higher Spectral Moments*

19. **No open-ended numerical fishing is permitted.**  
    Kernels, moments, core/halo rules, comparator ensembles, thresholds, and stopping rules must be preregistered before the result they are intended to test is examined.

20. **The active formal name of the Experiment 2 construction is the First Hermitian Instrument.**  
    New Project Montecito specifications, manuscript versions, repository documentation, and Experiment 3 materials will use **First Hermitian Instrument**, **Gaussian Hermitian instrument**, or **finite Hermitian instrument** as appropriate. The deprecated informal label may remain only inside immutable historical source documents or direct quotations whose original wording must be preserved.

21. **A public-reproducibility-repository gate is required before Experiment 3 execution.**  
    Experiments 1 and 2 must be transformed from internal freeze archives into a public-repository-ready package containing source provenance, acquisition or download instructions where redistribution rights are unclear, frozen configurations, runnable code, tests, machine-readable outputs, figure-generation paths, reports, paper-to-code traceability, and SHA-256 manifests. A clean-clone reproduction must pass before Experiment 3 Gate 1 begins. The repository may remain private until the project is ready for public release.

---

# Source Reliability and Citation Policy

## 1. Purpose

Project Montecito separates the existence of a public document from the reliability required for a load-bearing scientific source.

The project does not reject work merely because an author is unfamiliar. Mathematical correctness is determined by argument and verification, not reputation. However, an official project specification must also make source provenance, review status, and evidentiary role explicit.

## 2. Source classes

### Class A — Established published primary literature

Examples include peer-reviewed journal articles and classical monographs. These may be used as mathematical background, subject to ordinary scholarly checking.

### Class B — Authoritative data sources

Examples include Andrew Odlyzko’s published zeta-zero tables and other official data repositories with stated precision and provenance.

### Class C — Recent identifiable preprints with explicit status

A recent arXiv preprint may be cited when:

- the primary manuscript is available;
- authorship and scholarly provenance are traceable;
- its status as a preprint is stated;
- its role is contextual rather than silently treated as settled background;
- load-bearing claims receive independent checking or corroboration where feasible.

### Class D — Unverified or provenance-uncertain adjacent work

Such work may be retained in private research notes, but it does not enter the active project specification as an authoritative source until independently verified to the project’s standard.

## 3. Version 0.7 source decision

The dedicated adjacent-preprint section introduced in Version 0.6 is removed from the active Version 0.7 specification.

This removal is **not** a claim that the preprint is false. It reflects three narrower judgments:

1. the preprint is not required for any Experiment 1, Experiment 2, or Experiment 3 design decision;
2. its main claims are not needed as load-bearing background;
3. the project can state the relevant numerical principles directly—distinguishing floating-point uncertainty, model error, finite-window dependence, and truncation—without relying on that source.

Version 0.6 remains unchanged as the historical record of why the source was once considered adjacent.

## 4. Controlling mathematical sources for Version 0.7

The principal sources are:

- H. L. Montgomery, pair correlation of zeta zeros;
- A. M. Odlyzko, numerical zeta-zero tables and spacing studies;
- Z. Rudnick and P. Sarnak, higher-level correlations and random-matrix theory for principal \(L\)-functions;
- L. Alpöge and R. Furman, 2026 preprint on simple critical-line and distinct zeros;
- Y. Lamzouri, 2026 complementary proof of the same proportion bounds;
- the published and independently documented literature cited for any additional higher-correlation or numerical-control claim.

## 5. Citation language

Every external result must be labeled as one of:

- established published theorem;
- recent preprint result;
- numerical dataset;
- numerical reproduction;
- computational observation;
- conjecture;
- project hypothesis.

No preprint may be upgraded silently into settled theorem-level background.

---

# Analytic Context — Alpöge–Furman and Lamzouri

## 1. The 2026 proportion results

Alpöge and Furman prove unconditionally that at least two thirds of the nontrivial zeros, counted with multiplicity, are simple and lie on the critical line, and that at least five sixths are distinct. With the Montgomery–Taylor window, the constants improve to approximately

\[
0.67250
\qquad\text{and}\qquad
0.83625.
\]

Lamzouri subsequently gives a shorter, conceptually different unconditional proof of the same bounds.

Both works are recent arXiv preprints in Version 0.7 and must be cited with that status.

## 2. Alpöge–Furman proof architecture

Alpöge and Furman compress Weil’s Hermitian form to a finite real symmetric matrix \(\widetilde G\). Schematically,

\[
\widetilde G=P+Q,
\]

where critical-line zeros contribute positive rank-one pieces and symmetric off-line pairs contribute blocks with controlled signature. A prime-side calculation supplies a Hilbert–Schmidt second moment,

\[
\|\widetilde G\|_{\mathrm{HS}}^2
=
(R(\psi)+o(1))N,
\]

and a specialized rank–trace/inertia inequality converts this information into lower bounds for simple critical-line zeros and distinct zeros.

## 3. Lamzouri proof architecture

Lamzouri replaces the finite-dimensional matrix framework with a Hilbert-space inequality and applies an unconditional form of Montgomery’s pair-correlation theorem directly.

The two proofs use different representations, but both reduce the decisive information to a quadratic-form or second-moment estimate and lead to the same Montgomery–Taylor extremal problem.

## 4. Relevance to Montecito

Project Montecito does not numerically reproduce either proof.

- Experiment 1 measures an empirical finite-sample two-point statistic from known zero ordinates.
- Experiment 2 studies a process-agnostic Gaussian Hermitian instrument.
- Experiment 3 will study an explicitly higher-order finite statistic on zero-ordinate point sets and controls.

The theorem-level mechanisms contain arithmetic and analytic information absent from Montecito’s finite Hermitian instruments.

## 5. Scope of the approximately \(0.682\) ceiling

The approximately \(0.682\) ceiling discussed in the Alpöge–Furman framework concerns a particular bandwidth-one certificate based on first-two-moment information and the relevant on-line/off-line decomposition.

Experiment 3 does not test or attempt to break that ceiling. A finite \(\mu_4\) computation is not a numerical path around an analytic obstruction. It is a much narrower computational study of the correlation hierarchy in observed point sets.

---

# Project Goal

Project Montecito is a reproducible computational investigation of how progressively richer statistics describe the local organization of Riemann-zeta zero ordinates.

It asks three linked questions:

1. **Pairwise level:** What finite-height pair-correlation structure is visible in actual zeta-zero samples?
2. **First spectral-instrument level:** What can a transparent finite Hermitian instrument extract from those point configurations, and what are the information limits of its observables?
3. **Higher-order level:** Can a validated higher-order spectral statistic detect reproducible organization in zero ordinates that is not accounted for by the measured two-point structure?

The project is **not** designed to:

- prove or disprove the Riemann Hypothesis;
- estimate a percentage of RH that is “true”;
- improve a simple-zero or critical-line proportion;
- validate the Alpöge–Furman or Lamzouri proofs numerically;
- identify a Hilbert–Pólya operator;
- construct a faithful adèlic or Weil-form spectral realization;
- claim that a finite numerical pattern generalizes without replication and theoretical analysis.

The project should remain mathematically modest, experimentally ambitious, reproducible, and explicit about the difference between observation and theorem.

---

# Architecture at a Glance

## Experiment 1 — Pairwise baseline

\[
\text{actual zeta zeros}
\longrightarrow
\begin{cases}
\text{unfolded positions }X_\zeta,\\
\text{empirical pair correlation }\widehat R_\zeta(u)
\end{cases}
\]

**Status:** closed and frozen.

## Experiment 2 — First Hermitian instrument

\[
X_\zeta
\longrightarrow
C_{ij}=e^{-(x_i-x_j)^2/2}
\longrightarrow
H_\lambda=I-\lambda C
\longrightarrow
\text{spectrum and inertia}
\]

**Status:** closed after independent review.

**Controlling conclusion:** computationally valid and scientifically informative, but structurally underpowered for its original higher-order question.

## Experiment 3 — Higher-order spectral diagnostics

Leading candidate:

\[
X
\longrightarrow
K_{ij}=\operatorname{sinc}(x_i-x_j)
\longrightarrow
\mu_k=\frac1n\operatorname{tr}(K^k)
\longrightarrow
\text{two-point and higher-order comparison}
\]

Primary design hierarchy:

\[
\mu_2
\quad\text{as the two-point validation level},
\]

\[
\mu_4
\quad\text{as the leading higher-order-capable candidate}.
\]

**Status:** project-level direction approved; detailed specification and execution not yet authorized.

---

# Part I — Scientific Project Specifications

# Experiment 1 — Pair Correlation from Actual Zeta Zeros

## 1. Status

**SCIENTIFICALLY CLOSED AND FROZEN.**

Experiment 1 is not reopened by Version 0.7.

## 2. Objective

Produce two reproducible point-process artifacts:

\[
X_\zeta=\{x_1,\ldots,x_N\},
\]

and

\[
\widehat R_\zeta(u),
\]

from actual zeta-zero ordinates.

## 3. Data

The frozen primary sample is the first \(10{,}000\) nontrivial zeros.

The frozen high-height controls are:

- zeros numbered \(10^{12}+1\) through \(10^{12}+10^4\);
- zeros numbered \(10^{21}+1\) through \(10^{21}+10^4\).

The authoritative source is Andrew Odlyzko’s published zero tables, with recorded precision and checksums.

## 4. Unfolding

At low height,

\[
x_n=\overline N(\gamma_n),
\]

using the smooth Riemann–von Mangoldt term.

At very high height, relative arbitrary-precision theta unfolding is used before conversion to ordinary floating-point coordinates:

\[
x_n-x_1
=
\frac{\theta(\gamma_n)-\theta(\gamma_1)}{\pi}.
\]

Every future use of a newly unfolded process must assert that the mean unfolded spacing is approximately one.

## 5. Pair-correlation estimator

Experiment 1 uses:

- positive separations;
- \(U_{\max}=30\);
- bin width \(\Delta u=0.1\);
- translation-edge correction;
- bin-averaged GUE comparison near the origin;
- Poisson normalization checks;
- matched random-matrix finite-sample calibration.

The GUE/sine-kernel benchmark is

\[
R_{\mathrm{GUE}}(u)
=
1-
\left(\frac{\sin \pi u}{\pi u}\right)^2.
\]

## 6. Frozen results

For the first \(10{,}000\) zeros,

\[
N_{\mathrm{obs}}(0<u<0.5)=878,
\]

against the finite-window GUE expectation

\[
N_{\mathrm{GUE}}(0<u<0.5)=1131.46,
\]

so

\[
D_{0.5}\approx0.224.
\]

At higher height,

\[
D_{0.5}
\approx
0.016
\quad\text{near }10^{12},
\]

and

\[
D_{0.5}
\approx
-0.037
\quad\text{near }10^{21}.
\]

The supported conclusion is not that the effect vanishes, but that the large low-height distortion is suppressed below the experiment’s approximately \(5\%\) \(D_{0.5}\) detection scale at both high heights.

The integrated correlation-hole statistics remain close to the sine-kernel value \(-1/2\):

\[
S_{30}
\approx
-0.507158,
\quad
-0.494109,
\quad
-0.507531.
\]

## 7. Scientific interpretation

Experiment 1 establishes:

- strong non-Poisson short-range repulsion;
- qualitative GUE/sine-kernel pair structure;
- a substantial low-height redistribution of the correlation hole;
- approximate conservation of its integrated mass;
- strong suppression of the low-height shape distortion at much greater height.

It does not establish:

- RH;
- a convergence rate in height;
- exact equality with GUE at high height;
- higher-order correlation structure;
- validation of any 2026 simple-zero theorem.

## 8. Migration status

All Experiment 1 data and conclusions migrate unchanged into Experiment 3 as:

- development data;
- finite-height stress tests;
- high-height replication data;
- Level-1 two-point baselines;
- inputs to a new higher-order instrument.

The existing samples are not fully unseen confirmation data because they have already influenced the design.

---

# Experiment 2 — The First Hermitian Instrument

## 1. Status

**SCIENTIFICALLY CLOSED AFTER INDEPENDENT REVIEW.**

Permanent classification:

> **CLOSED — VALIDATED COMPUTATION, REVISED INTERPRETATION, INFORMATIVE LIMITATION.**

## 2. Original objective

Construct one transparent finite Hermitian family from an unfolded point configuration and ask:

1. what inertia profile the zeta configuration produces;
2. how much of the second moment can be reconstructed from pair differences;
3. whether the full inertia isolates information beyond the measured two-point structure.

## 3. Frozen design

For a block \(X=\{x_1,\ldots,x_m\}\),

\[
C_{ij}
=
\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right],
\]

and

\[
H_\lambda=I-\lambda C.
\]

Frozen parameters:

- Gaussian width \(\sigma=1\);
- \(m\in\{128,256,512\}\);
- 16 preregistered common nested locations;
- \(\lambda=0.10,0.15,\ldots,0.95\);
- spectrum-first inertia calculation;
- explicit sign-screening and higher-precision escalation rule;
- low-height primary sample and two high-height controls.

## 4. Spectrum-first identity

If \(\mu_j(C)\) are the eigenvalues of \(C\), then

\[
\eta_j(H_\lambda)=1-\lambda\mu_j(C),
\]

and crossings occur at

\[
\lambda_j^*=\frac1{\mu_j(C)}.
\]

One diagonalization of \(C\) determines the full frozen \(H_\lambda\) inertia flow.

## 5. Numerical validity

The closure record established:

- 144 block matrices analyzed;
- 2,592 block/\(\lambda\) inertia evaluations;
- 2,592 of 2,592 independent inertia classifications reproduced exactly;
- 19 of 19 frozen verification checks passed;
- zero unresolved sign assignments;
- 45 of 45 primary-package checksum entries matched;
- 19 of 19 validation-package checksum entries matched.

No frozen numerical result requires retraction or regeneration.

## 6. Primary descriptive results

For the primary \(m=512\) blocks:

- all directions remain positive through \(\lambda=0.30\);
- negative directions first appear on the frozen grid at \(\lambda=0.35\);
- mean \(p_{\mathrm{pos}}\approx0.777\) at \(\lambda=0.50\);
- mean \(p_{\mathrm{pos}}\approx0.670\) at \(\lambda=0.70\);
- mean \(p_{\mathrm{pos}}\approx0.597\) at \(\lambda=0.95\).

These are reproducible properties of the defined finite instrument, not universal invariants of zeta zeros.

## 7. Information hierarchy

Define

\[
D_C
=
\frac{\|C\|_F^2}{m}-1
=
\frac{\operatorname{tr}(C^2)}{m}-1.
\]

Then:

| Observable | Information level |
|---|---|
| \(\operatorname{tr}H_\lambda=m(1-\lambda)\) | no point-set information |
| \(\|H_\lambda\|_F^2\) | one Gaussian-weighted two-point scalar through \(D_C\) |
| \(b_{\mathrm{pos}}(\lambda)\) | the same scalar \(D_C\) |
| full spectrum / inertia | potentially higher-order, but no separable contribution was isolated |

The normalized lower bound is

\[
b_{\mathrm{pos}}(\lambda)
=
\frac{(1-\lambda)^2}
{(1-2\lambda)+\lambda^2(1+D_C)}.
\]

Its collapse near \(\lambda=1\) is algebraic, not an experimental discovery.

## 8. Pair-functional reconstruction

The direct Gaussian pair energy and its histogram reconstruction use the same multiset of pair differences.

The small \(0.0421\%\) discrepancy at \(\Delta u=0.1\) is principally a binning and quadrature effect. Poisson controls produce similarly small discrepancies, while the lattice exposes the expected failure of a smooth-density histogram representation for a discrete pair measure.

The bridge is retained as:

- a normalization check;
- a quadrature check;
- a smoothness check;
- an agreement check between two implementation paths.

It is not an independent zeta finding.

## 9. Height and instrument dependence

For the complete samples,

\[
D_C
\approx
0.920167,
\quad
0.945814,
\quad
0.951435
\]

from low height to the \(10^{12}\) and \(10^{21}\) regions.

This is a Gaussian smoothing of the two-point evolution already measured in Experiment 1.

The quantitative inertia curve also depends materially on:

- block size and location;
- the first-crossing region;
- Gaussian bandwidth.

The largest mean \(m=128\) versus \(m=512\) positive-fraction difference was approximately \(0.007202\), and the largest single-location difference was approximately \(0.023438\). Changing \(\sigma\) from \(1\) to \(0.5\) or \(2\) changes the inertia curve materially.

## 10. Permanent interpretation

Experiment 2 succeeded as:

- a validated computational experiment;
- a descriptive finite-matrix study;
- an information-content diagnosis;
- a methodological and falsification milestone.

It did not succeed as a clean detector of higher-order zeta structure.

The controlling conclusion is:

> **Experiment 2 is a computationally valid and scientifically informative diagnostic experiment, but its chosen summary observables were structurally insufficient to isolate the higher-order effect under investigation.**

## 11. Permanent dispositions

### Retained

- frozen spectra and inertia profiles;
- sign-resolution and reproducibility record;
- finite-window and kernel dependence;
- information hierarchy;
- pair-functional reconstruction as a code and quadrature check.

### Reframed

- pair bridge: reconstruction, not independent validation;
- \(D_C\) height sequence: smoothing of Level-1 evolution;
- \(b_{\mathrm{pos}}\): algebraic sanity check, not discriminator.

### Withdrawn or retracted

- \(\mu_{\max}\) as a general rigidity proxy;
- a universal claim that the First Hermitian Instrument cannot detect RH failure;
- an arithmetic interpretation of the raw number-variance ladder;
- any claim that the \(0.0421\%\) bridge discrepancy is special to zeta.

### Closed branch

The direct Christoffel-function-to-simple-zero-proportion conversion is closed unless new analytic on-line/off-line block accounting is developed.

## 12. Freeze rule

Experiment 2 may be reopened only for:

- a reproducible numerical error;
- an input-provenance failure;
- an unsupported closure claim demonstrated by independent audit;
- a formally authorized erratum.

A new model, kernel, statistic, or control is successor research and does not reopen Experiment 2.

---

# Experiment 3 — Higher-Order Spectral Diagnostics and Controlled Falsification

## 1. Status

**APPROVED FOR DETAILED SPECIFICATION DRAFTING, WITH MANDATORY GATES.**

**Execution is not authorized by Version 0.7.**

## 2. Primary scientific question

> **Can a numerically validated, explicitly higher-order spectral statistic reveal a reproducible feature of zeta-zero configurations that is not accounted for by the two-point structure already measured in Experiment 1?**

This is an ordinate-statistics question, not an RH-detection question.

## 3. Secondary questions

Experiment 3 may ask:

1. Does the candidate statistic recover known or simulated behavior on lattice, Poisson, and random-matrix controls?
2. Does it stabilize under increasing halo, core size, precision, and independent implementation?
3. How does the low-height Experiment 1 distortion appear at the higher-order level?
4. Do high-height zeta samples agree with matched random-matrix ensembles at both two-point and higher-order levels?
5. Is any apparent difference larger than realization noise, finite-window variation, and estimator bias?
6. Can omission effects be separated from arithmetic effects through matched thinning?
7. What information remains visible when an RH-false function is represented only by surviving on-line ordinates?

## 4. Questions outside the primary scope

Experiment 3 is not designed to:

- prove or disprove RH;
- estimate the fraction of zeros satisfying RH;
- improve a simple-zero proportion;
- test the approximately \(0.682\) bandwidth-one ceiling;
- reconstruct prime-side higher moments;
- certify a universal property of Hermitian approaches;
- infer \(\beta\)-coordinates from ordinate-only data;
- identify a self-adjoint Hilbert–Pólya operator;
- build a faithful adèlic or Weil-form spectral space.

## 5. Candidate sinc-kernel architecture

For a unit-density point configuration \(X=\{x_1,\ldots,x_n\}\), define

\[
K_{ij}
=
\operatorname{sinc}(x_i-x_j)
=
\begin{cases}
\dfrac{\sin\pi(x_i-x_j)}{\pi(x_i-x_j)}, & i\ne j,\\[2mm]
1, & i=j.
\end{cases}
\]

Define normalized spectral moments

\[
\mu_k
=
\frac1n\operatorname{tr}(K^k).
\]

Candidate roles:

| Moment | Planned role |
|---|---|
| \(\mu_1\) | normalization and implementation check |
| \(\mu_2\) | two-point validation level linked to Experiment 1 |
| \(\mu_3\) | secondary higher-order-capable diagnostic |
| \(\mu_4\) | leading primary candidate after numerical validation |

## 6. Why \(\mu_4\) is the leading candidate

For the first-two-moment extremal distribution with atoms \(0,1,2\) and weights \(1/6,2/3,1/6\), the first four moments are

\[
1,
\qquad
\frac43,
\qquad
2,
\qquad
\frac{10}{3}.
\]

The quoted sine-process targets are

\[
1,
\qquad
\frac43,
\qquad
2,
\qquad
\frac{13}{4}.
\]

The first three agree, while the fourth differs by

\[
\frac{10}{3}-\frac{13}{4}
=
\frac1{12}.
\]

Thus \(\mu_4\), not \(\mu_3\), is the first moment separating these two specific spectral models.

This is a design motivation only. It is not yet a novelty claim and does not imply that a finite zeta computation will distinguish the models reliably.

## 7. Raw \(\mu_4\) and lower-order contamination

The expansion

\[
\operatorname{tr}(K^4)
=
\sum_{i,j,k,\ell}
K_{ij}K_{jk}K_{k\ell}K_{\ell i}
\]

contains:

- all-distinct-index terms;
- three-index terms;
- pair-collision terms;
- diagonal terms.

Therefore raw \(\mu_4\):

- can contain genuine three- and four-point information;
- also contains lower-order contributions;
- may respond to a pair-correlation change already visible in Experiment 1.

Before attributing a contrast to higher-order structure, the detailed specification must adopt at least one of these safeguards:

1. establish pair-correlation and \(\mu_2\) agreement before interpreting \(\mu_4\);
2. decompose \(\mu_4\) by index-collision class;
3. use a preregistered surrogate ensemble matched at the measured two-point level;
4. provide another explicit mathematical subtraction or attribution argument.

## 8. Core-plus-halo estimator

Let \(I_c\) be a central core and \(I_h\supset I_c\) a halo-augmented index set. Construct \(K^{(h)}\) on all points in \(I_h\), but measure only contributions based in the core:

\[
\widehat\mu_{k,c|h}
=
\frac1{|I_c|}
\sum_{i\in I_c}
\left[(K^{(h)})^k\right]_{ii},
\qquad
k\in\{2,4\}.
\]

The halo must be increased according to a preregistered sequence while the core remains fixed.

Required diagnostics:

- core definition;
- halo definition in point count and unfolded distance;
- \(\widehat\mu_{2,c|h}\) and \(\widehat\mu_{4,c|h}\) at every halo size;
- successive-halo changes;
- precision and algorithmic error;
- time and memory use;
- agreement between two implementations or algorithms;
- the same halo study on exact or simulated controls.

The detailed specification must define a stabilization rule relative to:

- the target gap \(1/12\);
- realization noise;
- the desired minimum detectable effect.

If halo stability fails, the experiment stops before a zeta claim is made.

## 9. Zeta-data roles

### A. First \(10{,}000\) zeros

Role:

- estimator development;
- low-height stress test;
- study of how known Level-1 distortion propagates into higher moments.

Not an unseen confirmatory sample.

### B. Near \(10^{12}\)

Role:

- high-height replication and control;
- comparison in a regime where the Experiment 1 short-range discrepancy is below the current detection scale.

### C. Near \(10^{21}\)

Role:

- high-height development and control;
- closest frozen input to the asymptotic random-matrix regime;
- not unseen, because exploratory higher-moment information has already influenced the design.

### D. Fresh high-height holdout

Strongly preferred for a confirmatory positive claim.

Any new block must record:

- authoritative source;
- exact zero indices and height range;
- precision;
- checksum;
- unfolding convention;
- role as calibration, development, replication, or confirmation data.

## 10. Mandatory control architecture

### A. Lattice

The integer lattice is an exact sinc-kernel anchor because nonzero integer differences give zero sinc entries. It validates normalization, indexing, and matrix-power implementation.

### B. Poisson

A unit-rate Poisson process supplies a non-rigid, non-repulsive comparator and tests dynamic range.

### C. Random-matrix / sine-process comparator

One primary repeated generator must be frozen in advance.

The detailed specification must fix:

- CUE, GUE, or another explicit sine-process approximation;
- matrix size or point-count regime;
- bulk extraction or circular construction;
- unfolding convention;
- number of independent realizations;
- random seeds or seed-generation rule.

CUE and GUE may both be used only if their roles are distinct and preregistered.

### D. Matched thinning

Whenever a subset is created by omission or selection, a matched non-arithmetic thinning control is mandatory.

For independent retention probability \(p\),

\[
\Sigma_{\mathrm{thin}}^2(L)
=
p^2\Sigma_{\mathrm{orig}}^2(L/p)
+(1-p)L
\]

is a baseline confound, not an arithmetic signal.

### E. RH-false stress tests

Davenport–Heilbronn and the selected Epstein zeta may be used only as secondary stress-test classes after their calculations are independently packaged.

Any such use must state whether the instrument receives:

1. only the surviving on-line ordinates;
2. an all-zero ordinate multiset preserving repeated ordinates;
3. the full complex zeros \(\beta+i\gamma\).

The first representation tests the geometry of a surviving on-line subset. It does not directly test sensitivity to the real parts of off-line zeros.

All-zero and full-complex representations are deferred unless the detailed specification explicitly introduces a new mathematical object.

## 11. Level-1-before-higher-order interpretation rule

For every zeta-versus-random-matrix comparison, report in this order:

1. pair correlation under the relevant window and unfolding;
2. \(\mu_2\) or another explicit two-point validation statistic;
3. halo, window, precision, and realization-noise diagnostics;
4. \(\mu_4\) or the selected higher-order statistic;
5. lower-order decomposition or matched-two-point control;
6. only then, a possible higher-order interpretation.

A low-height \(\mu_4\) difference is not automatically a higher-order result because the low-height sample already has a known pair-correlation distortion.

The cleanest initial higher-order test is a comparison in which zeta and the random-matrix ensemble agree at the preregistered Level-1 resolution.

## 12. Power and sensitivity

Before the primary zeta comparison, quantify:

- between-realization random-matrix variation;
- within-sample location variation;
- core-size variation;
- halo-size variation;
- numerical and algorithmic variation;
- false-positive behavior under matched null comparisons;
- minimum detectable effect;
- sensitivity relative to \(1/12\) or another preregistered target.

The detailed specification must define:

- primary statistic;
- null ensemble;
- effect-size metric;
- uncertainty interval;
- multiplicity policy for secondary observables;
- stopping rule;
- power criterion.

A null result is informative only if the design could have detected a scientifically meaningful contrast.

## 13. Staged authorization

### Gate 0 — Detailed scientific specification

Produce and approve `Project_Montecito_Experiment3_Specification_v1.md`.

### Gate 1 — Implementation and exact-control validation

Demonstrate identities, lattice behavior, process-specific unfolding, unit-spacing assertions, and agreement between independent implementations.

### Gate 2 — Core-plus-halo validation

Demonstrate stable \(\mu_2\) and \(\mu_4\) under the preregistered halo rule on non-zeta controls.

### Gate 3 — Power calibration

Use repeated random-matrix and Poisson realizations to establish noise, dynamic range, and minimum detectable effect.

### Gate 4 — Development zeta analysis

Apply the frozen estimator to the existing Experiment 1 samples, labeling them as previously observed development or replication data.

### Gate 5 — Falsification and confound controls

Run matched thinning where applicable and separate Level-1 propagation from higher-order changes.

### Gate 6 — Confirmatory holdout or qualified replication

Where feasible, run the frozen design on a fresh high-height holdout. Otherwise classify the result as exploratory or internally replicated.

### Gate 7 — Independent review and freeze

An independent reviewer must audit the mathematics, implementation, provenance, boundary control, power analysis, and interpretation.

No gate may be passed by tuning the statistic after viewing the result it is meant to test.

## 14. Predeclared outcome classes

### Outcome A — Positive candidate signal

Required conditions:

- implementation and halo gates pass;
- power is adequate;
- effect exceeds realization noise and finite-window variation;
- effect survives independent implementation;
- Level-1 behavior is matched or explicitly accounted for;
- falsification and thinning controls pass;
- replication or holdout succeeds where feasible.

Permitted language:

> **A candidate higher-order zeta-zero signal was detected by the preregistered finite statistic under the tested conditions.**

This would trigger replication, literature review, theoretical interpretation, and possible Project Montecito Version 2 work.

### Outcome B — Informative negative result

Required conditions:

- stable validated estimator;
- demonstrated power;
- functioning controls;
- no reproducible departure beyond the uncertainty threshold.

Permitted language:

> **At the tested heights, scales, and sensitivity, the validated higher-order statistic found no detectable departure from the matched comparator beyond the measured two-point structure.**

This remains a scientifically useful result and may complete a coherent three-experiment paper.

### Outcome C — Inconclusive result

Examples:

- halo nonconvergence;
- uncontrolled block bias;
- inadequate power;
- control failure;
- disagreement between implementations;
- missing provenance;
- effect below uncertainty;
- inability to separate Level-1 propagation from higher-order contribution.

An inconclusive result may motivate redesign but may not be presented as a positive or informative negative result.

## 15. No-fishing and change-control rules

Before examining the primary zeta output, freeze:

- kernel and normalization;
- moment order;
- core geometry;
- halo sequence;
- comparator generator;
- realization count;
- seeds or seed-generation rule;
- effect-size metric;
- uncertainty method;
- power threshold;
- stopping rule;
- outcome language.

After preregistration:

- material changes require a dated amendment;
- development and confirmatory roles may not be reassigned;
- unsuccessful configurations remain in the execution log;
- no robustness result replaces the primary result because it is more favorable;
- all tested primary and secondary configurations must be reported.

## 16. Experiment 3 deliverables

The planned package should contain:

- detailed specification and preregistration;
- source and data manifest;
- code and environment lock;
- exact-control tests;
- core-plus-halo validation report;
- power-calibration report;
- primary and control outputs in machine-readable form;
- execution log;
- figures generated from source data;
- independent validation implementation;
- peer-review handoff;
- final report, closure decision, and migration decision if warranted.

---

# Part II — Common Computational, Reproducibility, and Governance Rules

# 1. Core execution model

Experiments use one controlled Python codebase.

LLMs may assist with:

- code generation;
- code review;
- mathematical exposition;
- test design;
- literature discovery;
- interpretation checks.

Numerical claims must be produced by ordinary deterministic or explicitly seeded numerical code, archived outputs, and reviewable formulas.

No scientific result may depend on an unrecoverable conversational computation.

# 2. Resource discipline

The project should remain executable on a modern workstation or laptop-class machine unless a later specification justifies additional resources.

Avoid:

- unnecessary recomputation of established zero tables;
- open-ended autonomous search loops;
- brute-force parameter sweeps without preregistered purpose;
- dense calculations whose memory cost is not justified by the estimator;
- unlogged manual editing of numerical outputs.

# 3. Reproducibility record

Every experiment must record:

- Python version;
- package versions and lock file;
- operating system and hardware summary;
- source URLs and access dates;
- raw-data hashes;
- processed-data hashes;
- unfolding convention;
- unit-spacing diagnostics;
- estimator formulas;
- window, core, and halo definitions;
- kernel and normalization;
- random seeds;
- realization counts;
- stopping and power rules;
- numerical precision;
- algorithmic tolerances;
- all primary and secondary outputs;
- all figure-generation scripts;
- unsuccessful or superseded runs;
- independent-validation results.

# 4. Suggested repository structure

```text
project-montecito/
│
├── README.md
├── pyproject.toml
├── environment/
│   └── lockfile-or-requirements.txt
│
├── specifications/
│   ├── Project_Montecito_Project_Specifications_v0.7.md
│   └── Project_Montecito_Experiment3_Specification_v1.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── manifests/
│   └── checksums/
│
├── src/
│   ├── zeros.py
│   ├── unfold.py
│   ├── pair_correlation.py
│   ├── point_processes.py
│   ├── gaussian_instrument.py
│   ├── sinc_moments.py
│   ├── halo_estimators.py
│   ├── thinning_controls.py
│   ├── power.py
│   └── metrics.py
│
├── experiments/
│   ├── exp1_pair_correlation/
│   ├── exp2_gaussian_hermitian/
│   └── exp3_higher_order/
│
├── validation/
├── tests/
├── figures/
├── review/
└── paper/
    ├── manuscript.md
    ├── manuscript.tex
    └── references.bib
```

# 5. Public Reproducibility Repository Gate

Before Experiment 3 execution, Project Montecito must prepare and validate a public-repository-ready release for the completed Experiments 1 and 2.

The gate requires:

1. a human-readable repository entry point explaining the three-experiment architecture and the evidence status of each result;
2. authoritative source acquisition instructions and expected SHA-256 values for external data that should not be redistributed without clear permission;
3. frozen Experiment 1 and Experiment 2 configurations, manifests, code, tests, machine-readable outputs, and figure-generation procedures;
4. a paper-to-code map connecting every quantitative manuscript claim to its input, configuration, computation, output, and figure or table;
5. a clean-clone or clean-environment reproduction of the central Experiment 1 and Experiment 2 results;
6. a versioned repository release or internal release candidate with a Git commit or tag identifier and a public-package SHA-256 manifest;
7. clear separation between controlling reports and superseded historical drafts;
8. retention of the Experiment 2 corrections, reframed findings, withdrawn interpretations, and closed research branches in the public record.

This gate prepares the scientific record for publication and provides the reproducibility template for Experiment 3. It does not require the GitHub repository to be publicly visible before Experiment 3 begins, but the package must already be organized and validated as though an outside researcher were cloning it.

# 6. Research integrity language

Throughout the project distinguish:

**Established theorem**  
A result proved in published mathematical literature.

**Recent preprint result**  
A result currently available as a preprint and labeled accordingly.

**Numerical reproduction**  
A computational reproduction of an established or previously reported phenomenon.

**Finite research instrument**  
A deliberately simplified and mathematically explicit construction used to isolate or test one mechanism.

**Computational observation**  
A finite pattern observed experimentally but not proved.

**Candidate signal**  
A preregistered computational effect that has passed internal controls but still requires independent confirmation and literature review.

**Informative negative result**  
A null result from a validated, adequately powered, and properly controlled experiment.

**Inconclusive result**  
A result whose estimator, power, controls, provenance, or interpretation is insufficient.

**Conjecture or hypothesis**  
A proposed generalization or explanation requiring mathematical proof.

# 7. Mandatory nonclaims

The following must remain explicit:

- Experiment 1 does not verify RH.
- Experiment 2 is not a finite Weil compression.
- Experiment 3 is not a direct test of critical-line membership.
- No Montecito statistic validates the Alpöge–Furman or Lamzouri proofs.
- Agreement with GUE does not imply RH.
- A positive finite-sample signal does not imply a theorem.
- A null result does not prove that higher-order structure does not exist.
- Existing development samples are not unseen confirmation data.
- A preprint is not silently treated as peer-reviewed literature.
- An unfamiliar or unaffiliated author is not automatically unreliable, but provenance-uncertain work is not used as controlling background without independent verification.

---

# Part III — Updated Paper Outline

# Working title

## Primary working title

**A Computational Walk Toward Higher-Order Structure in the Zeta Zeros**

## Technical subtitle

**Pair Correlation, Hermitian Instruments, and Higher Spectral Moments**

The title is provisional until Experiment 3 is complete. “Toward” must remain unless the final evidence justifies stronger language.

# Provisional abstract requirements

The abstract should state:

- motivation from RH and recent 2026 proportion results;
- complementary Alpöge–Furman and Lamzouri proof architectures;
- that Montecito is computational and not a proof attempt;
- use of actual unfolded zero ordinates;
- Experiment 1’s low-height pair-correlation distortion and high-height suppression;
- Experiment 2’s validated First Hermitian Instrument;
- Experiment 2’s information-content limitation;
- the corrected reconstruction interpretation of the pair bridge;
- the prospective higher-order Experiment 3 question;
- the exact outcome class after Experiment 3 is complete;
- reproducibility, negative controls, and limitations.

Until Experiment 3 is completed, the abstract must not state that a higher-order signal has been found.

# 1. Introduction

## 1.1 The Riemann Hypothesis

Define \(\zeta(s)\), the critical strip, the critical line, and \(\rho=\beta+i\gamma\).

## 1.2 Historical progress on critical-line and simple zeros

Include:

- Hardy;
- Selberg;
- Levinson;
- Conrey;
- Bui–Conrey–Young;
- Pratt–Robles–Zaharescu–Zeindler;
- Alpöge–Furman;
- Lamzouri.

Clearly distinguish published classical results from 2026 preprints.

## 1.3 From Montgomery to random matrices and higher correlations

Explain:

- pair correlation;
- Dyson’s GUE recognition;
- the distinction between a statistical spectral analogy and a Hilbert–Pólya operator;
- higher-level correlations as the natural hierarchy beyond pairs.

## 1.4 Project motivation

Present the three-experiment progression:

\[
\text{pairwise baseline}
\longrightarrow
\text{first Hermitian instrument}
\longrightarrow
\text{explicitly higher-order diagnostic}.
\]

## 1.5 Contributions

Separate:

- completed Experiment 1 contributions;
- completed Experiment 2 contributions and limitations;
- prospective Experiment 3 contribution until frozen.

# 2. Mathematical Background

## 2.1 Zeta zeros and unfolding

## 2.2 Montgomery pair correlation

## 2.3 Higher-level correlation hierarchy

Explain why pair correlation need not determine three- and four-point organization.

## 2.4 Positive-definite kernels and Gram matrices

## 2.5 The Gaussian Hermitian Instrument

## 2.6 Inertia, trace, Frobenius norm, and spectral moments

## 2.7 Information content of matrix observables

Include the Experiment 2 hierarchy.

## 2.8 Alpöge–Furman and Lamzouri

Compare the finite-matrix/inertia and Hilbert-space approaches.

## 2.9 Analytic second moments versus empirical pair statistics

## 2.10 Why a fourth spectral moment is a natural candidate

Present the \(10/3\) versus \(13/4\) distinction with appropriate qualification.

# 3. Experiment 1 — Pair Correlation from Actual Zeta Zeros

## 3.1 Data provenance

## 3.2 Unfolding

## 3.3 Estimator and controls

## 3.4 Low-height result

## 3.5 Matched-GUE calibration

## 3.6 High-height replication

## 3.7 Frozen artifacts and interpretation

# 4. Experiment 2 — The First Hermitian Instrument

## 4.1 Frozen Gaussian design

## 4.2 Preregistration and spectrum-first computation

## 4.3 Numerical integrity and independent reproduction

## 4.4 Information hierarchy

## 4.5 Pair-functional reconstruction

## 4.6 Inertia results

## 4.7 Window and kernel dependence

## 4.8 Peer-review corrections

## 4.9 Informative limitation and closure

# 5. Experiment 3 — Higher-Order Spectral Diagnostics

This section remains prospective until Experiment 3 is frozen.

Planned subsections:

## 5.1 Scientific question and preregistration

## 5.2 Sinc-kernel moments

## 5.3 Core-plus-halo estimator

## 5.4 Lattice and Poisson validation

## 5.5 Random-matrix comparator and power

## 5.6 Development zeta samples

## 5.7 Matched-two-point and thinning controls

## 5.8 Confirmatory holdout or qualified replication

## 5.9 Positive, informative negative, or inconclusive result

# 6. Results and Discussion

## 6.1 What pair correlation reveals

## 6.2 What the First Hermitian Instrument reveals

## 6.3 What Experiment 2 could not reveal

## 6.4 What the higher-order statistic adds—or fails to add

## 6.5 Finite-height versus high-height behavior

## 6.6 Random-matrix consistency and possible residuals

## 6.7 Negative controls and interpretations that did not survive

## 6.8 The three-experiment scientific arc

# 7. Limitations

Discuss explicitly:

- finite zero samples;
- previously observed development data;
- finite-height effects;
- unfolding dependence;
- boundary and halo effects;
- random-matrix finite-size effects;
- realization noise;
- lower-order contributions inside raw \(\mu_4\);
- kernel choice;
- holdout availability;
- ordinate-only representation;
- no direct access to \(\beta\);
- no faithful Weil/adèlic construction;
- no theorem inferred from numerical similarity;
- preprint status of the 2026 analytic context.

# 8. Conclusion

The paper should conclude according to the final Experiment 3 outcome.

A suitable invariant framing is:

> **Project Montecito follows a reproducible progression from pairwise statistics, through a first finite Hermitian instrument, to a deliberately higher-order test. Its contribution is to show what each level can measure, what it cannot measure, and which interpretations survive adversarial controls.**

# Appendices

## Appendix A — Zero data, provenance, and checksums

## Appendix B — Unfolding and unit-spacing tests

## Appendix C — Pair-correlation estimator

## Appendix D — First Hermitian Instrument

## Appendix E — Experiment 2 spectra, inertia, and verification

## Appendix F — Sinc-kernel moments and collision decomposition

## Appendix G — Core-plus-halo estimator

## Appendix H — Synthetic-process generators

## Appendix I — Power and outcome rules

## Appendix J — Reproducibility instructions

## Appendix K — Peer-review corrections and withdrawn interpretations

## Appendix L — Source-status and bibliography notes

---

# Execution Order After Version 0.7

## Phase 0 — Version 0.7 release

**Complete by this approval and freeze record.**

- approve and freeze this project-level specification;
- preserve Version 0.6 as historical;
- approve the external-source policy;
- accept the higher-order Experiment 3 direction;
- authorize detailed Experiment 3 specification drafting;
- record that no Experiment 3 computation is authorized.

## Phase 1 — Experiment 1

**Complete and frozen.**

## Phase 2 — Experiment 2

**Complete, independently reproduced, reviewed, and scientifically closed.**

## Phase 3 — Complete remaining Experiment 2 closure administration

- update the final closure README/status record;
- produce the final closure archive index or reproducibility manifest.

This administrative step does not reopen Experiment 2 and does not authorize Experiment 3.

## Phase 4 — Public reproducibility repository for Experiments 1 and 2

- produce `Project_Montecito_Public_Repository_Manifest_v1.md`;
- organize the public-repository-ready Experiment 1 and Experiment 2 packages;
- add authoritative source acquisition and SHA-256 verification;
- complete the paper-to-code map;
- pass a clean-clone reproduction;
- freeze the first pre–Experiment 3 repository release candidate.

The repository may remain private until public release, but this gate must pass before Experiment 3 Gate 1 begins.

## Phase 5 — Focused Experiment 3 literature and source audit

Review reliable primary sources for higher-level zeta correlations, sinc-kernel spectral moments, fourth-moment targets, finite-section and boundary effects, collision decompositions, and matched-two-point controls. No novelty claim or final observable selection may be made before this audit.

## Phase 6 — Detailed Experiment 3 specification

Produce:

`Project_Montecito_Experiment3_Specification_v1.md`

Freeze:

- exact statistic;
- lower-order separation method;
- core and halo geometry;
- data roles;
- random-matrix generator;
- controls;
- realization count;
- seeds;
- power threshold;
- outcome rules;
- resource budget.

## Phase 7 — Machine-readable Experiment 3 preregistration

Create the checksum-locked configuration, data manifest, seed policy, output schemas, environment record, and change-control log corresponding exactly to the approved specification.

## Phase 8 — Instrument validation

Run Gates 1–3 only on exact and synthetic controls.

## Phase 9 — Development zeta analysis

Apply the frozen estimator to existing zeta samples only after the instrument passes its validation, halo-stability, and power gates.

## Phase 10 — Falsification and confirmation

Run matched controls and, where feasible, a fresh high-height holdout.

## Phase 11 — Independent review and Experiment 3 freeze

Do not update the manuscript with a claimed Experiment 3 result before review.

## Phase 12 — Paper update and publication decision

Update the manuscript after the final Experiment 3 interpretation is frozen.

The arXiv decision follows the scientific result. It is not a success criterion imposed in advance.

---

# Version History

| Version | Date | Purpose |
|---|---|---|
| 0.3 | August 2026 | Established the points-in architecture and first indefinite Hermitian-instrument family |
| 0.4 | August 26, 2026 | Aligned the project with Alpöge–Furman Version 2 |
| 0.5 | August 31, 2026 | Consolidated scope to Experiments 1–3 |
| 0.6 | August 31, 2026 | Hardened Experiment 2 numerical methodology before execution |
| **0.7** | **September 4, 2026** | **Approved and froze the post–Experiment 2 project state; accepted the higher-order direction and source policy; adopted First Hermitian Instrument terminology; added the public-reproducibility gate; authorized detailed Experiment 3 specification drafting without authorizing computation** |

---

# Version 0.7 Formal Approval and Freeze Decision

Project Montecito Version 0.7 is **approved and frozen as of September 4, 2026**.

The following five project-level decisions are closed:

| Decision item | Final disposition |
|---|---|
| Experiment 1 remains frozen | **APPROVED AND CLOSED** |
| Experiment 2 remains closed | **APPROVED AND CLOSED** |
| Higher-order Experiment 3 direction | **ACCEPTED** |
| Source Reliability and Citation Policy | **ACCEPTED AND FROZEN** |
| Detailed Experiment 3 specification drafting | **AUTHORIZED** |

Approval also adopts the active terminology **First Hermitian Instrument** and the public-reproducibility-repository gate for Experiments 1 and 2.

## What this approval authorizes

- use Version 0.7 as the controlling project-level specification;
- preserve Experiment 1 without rerun;
- preserve Experiment 2 without reopening or retrospective replacement;
- draft `Project_Montecito_Experiment3_Specification_v1.md`;
- perform the focused literature and source audit needed to select and justify the final Experiment 3 observable;
- prepare and validate the public-repository-ready packages for Experiments 1 and 2;
- complete the remaining Experiment 2 closure administration.

## What this approval does not authorize

- treating \(\mu_4\) as the already frozen primary statistic;
- selecting a core or halo size outside the detailed specification process;
- selecting a random-matrix generator or realization count outside the detailed specification process;
- exposing any zeta dataset to an unfrozen Experiment 3 estimator;
- beginning Experiment 3 Gate 1 or any later computational gate;
- claiming that a higher-order signal has been detected;
- beginning Project Montecito Version 2.

## Freeze and change-control rule

The canonical Version 0.7 Markdown file is immutable once its SHA-256 fingerprint is recorded in `Project_Montecito_v0.7_Approval_and_Freeze_Record_v1.md` and `SHA256SUMS_Project_Montecito_v0.7.txt`.

Any later change must be issued transparently as:

- Version 0.7.1 for a non-scientific editorial correction that does not alter the approved design or status decisions;
- Version 0.8 for a material scientific, governance, scope, or execution-order change;
- or a dated erratum or amendment that explicitly identifies the affected text.

No silent modification of the frozen Version 0.7 file is permitted.

## Next authorized scientific artifact

After the remaining closure administration, public-repository gate, and focused literature audit, the next authorized scientific-design artifact is:

`Project_Montecito_Experiment3_Specification_v1.md`.

Experiment 3 computation remains **NOT AUTHORIZED** until that separate specification and its machine-readable preregistration are approved and frozen.

