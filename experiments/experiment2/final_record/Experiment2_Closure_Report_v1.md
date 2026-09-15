# Project Montecito — Experiment 2 Closure Report
## Version 1

**Date:** 2 September 2026  
**Closure package:** Part 4 of 6  
**Status:** Complete  
**Formal decision:** **EXPERIMENT 2 SCIENTIFICALLY CLOSED AFTER INDEPENDENT REVIEW**  
**Scientific baseline:** `Project_Montecito_Project_Specifications_v0.6.md`  
**Final scientific report:** `Experiment2_Report_v2.md`  
**Peer-review disposition:** `Experiment2_Peer_Review_Response_v1.md`  
**Review provenance:** `Experiment2_Review_Corpus_Index_v1.md`

---

# 1. Purpose

This document issues the formal scientific-closure decision for **Project Montecito Experiment 2**.

Experiment 2 constructed and tested the preregistered Gaussian Hermitian toy family

$$
C_{ij}=\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right],
\qquad
H_\lambda=I-\lambda C,
$$

on the frozen low-height and high-height zeta-zero point configurations inherited from Experiment 1.

The closure decision is based on:

1. the frozen Version 0.6 scientific specification;
2. the original Experiment 2 primary package;
3. the Experiment 2 Validation Extension;
4. the seven-document review corpus indexed in Part 1;
5. the formal response to the two scientific peer-review documents in Part 2;
6. the revised scientific report in Part 3;
7. the targeted mathematical, computational, artifact, and checksum rechecks performed during reconciliation.

This document does not repeat the full numerical report or the finding-by-finding peer-review response. Its role is narrower and more consequential:

> **to decide whether Experiment 2 is sufficiently complete, reproducible, correctly interpreted, and scientifically bounded to be frozen and closed.**

The answer is **yes**.

---

# 2. Formal closure decision

## 2.1 Decision

Project Montecito Experiment 2 is hereby classified as:

> **CLOSED — VALIDATED COMPUTATION, REVISED INTERPRETATION, INFORMATIVE LIMITATION.**

The experiment is closed because:

- its preregistered computation is complete;
- its primary numerical outputs survived independent reconstruction;
- its numerical sign classifications are resolved on the frozen grid;
- its artifacts and checksums have been audited;
- the independent peer review is complete;
- every material peer-review finding has been formally dispositioned;
- the original report has been revised to remove or narrow interpretations that did not survive review;
- the remaining open questions would require a new apparatus, a new observable, a new control representation, or a new experimental design.

Those remaining questions are therefore **successor research**, not unfinished Experiment 2 work.

## 2.2 Closure status block

```text
EXPERIMENT2_DESIGN                    = FROZEN_UNDER_SPECIFICATION_V0_6
EXPERIMENT2_PRIMARY_COMPUTATION       = COMPLETE
EXPERIMENT2_NUMERICAL_REPRODUCTION    = PASSED
EXPERIMENT2_PEER_REVIEW               = COMPLETE_AND_DISPOSITIONED
EXPERIMENT2_INTERPRETATION            = REVISED_AFTER_ADVERSARIAL_REVIEW
EXPERIMENT2_PRIMARY_ARTIFACTS         = CHECKSUM_VERIFIED
EXPERIMENT2_SCIENTIFIC_RESULT_CLASS   = INFORMATIVE_LIMITATION_AND_DIAGNOSTIC
EXPERIMENT2_HIGHER_ORDER_DETECTION    = NOT_ACHIEVED_BY_THIS_APPARATUS
EXPERIMENT2_SCIENTIFIC_STATUS         = CLOSED
EXPERIMENT3_EXECUTION                 = NOT_STARTED
```

## 2.3 Meaning of “closed”

“Closed” means that no additional computation is required to determine the scientific meaning of the **frozen Experiment 2 apparatus**.

It does not mean:

- that every question raised during peer review has been solved;
- that zeta zeros contain no higher-order structure;
- that no better Hermitian or spectral apparatus can be designed;
- that Project Montecito is ending;
- that the future paper is complete;
- that Experiment 3 has been specified or begun.

It means that the first apparatus has been run, audited, understood, and placed in its correct scientific scope.

---

# 3. Closure criteria and evidence

The following gates were required for scientific closure.

| Closure gate | Required condition | Evidence | Decision |
|---|---|---|---|
| **Design integrity** | Frozen parameters and block geometry existed before result inspection | Version 0.6 specification, frozen JSON configuration, exact block manifest | **PASS** |
| **Primary computation** | Gaussian matrices, spectra, inertia, identities, and bridge outputs completed | Primary Experiment 2 package and execution log | **PASS** |
| **Independent reproduction** | Separate implementation reproduces the principal outputs | Validation Extension and closure reruns | **PASS** |
| **Numerical sign resolution** | No frozen-grid eigenvalue sign remains unresolved | All 2,592 block/\(\lambda\) classifications reproduced; zero unresolved signs | **PASS** |
| **Verification suite** | Frozen automated checks pass | 19 of 19 checks passed in the closure rerun | **PASS** |
| **Artifact integrity** | Required packages and manifests are present and checksum-consistent | 45 of 45 primary-package entries and 19 of 19 validation-package entries matched | **PASS** |
| **Independent peer review** | Adversarial review completed | PR-01 and PR-02, with subsequent analytical responses | **PASS** |
| **Finding disposition** | Every material criticism is accepted, narrowed, rejected, withdrawn, closed, or deferred explicitly | `Experiment2_Peer_Review_Response_v1.md` | **PASS** |
| **Report correction** | Final report reflects the approved interpretations | `Experiment2_Report_v2.md` | **PASS** |
| **Scope integrity** | No unsupported claim about RH, Alpöge–Furman, or universal apparatus behavior remains | Report v2 limitations and nonclaims | **PASS** |
| **Successor boundary** | Open research questions are separated from the frozen experiment | This closure report; migration work deferred to Part 5 | **PASS** |

No closure gate remains open.

---

# 4. Final scientific characterization

## 4.1 The controlling conclusion

The final characterization of Experiment 2 is:

> **Experiment 2 is a computationally valid and scientifically informative diagnostic experiment, but its chosen summary observables were structurally insufficient to isolate the higher-order effect under investigation.**

A slightly fuller formulation is:

> **Experiment 2 succeeded as a computation and as a diagnosis of the first apparatus. It did not succeed as a clean detector of structure beyond pair correlation.**

This distinction is the central scientific judgment of the closure process.

## 4.2 What “underpowered” means

In this context, **underpowered** does not primarily mean:

- too few zeros;
- too few blocks;
- inadequate hardware;
- insufficient floating-point precision;
- an insufficiently dense \(\lambda\)-grid.

It means **structurally and informationally underpowered**.

The principal summary observables did not all contain the information level required by the original higher-order question:

| Observable | Information supplied by the point configuration |
|---|---|
| \(\operatorname{tr}H_\lambda=m(1-\lambda)\) | none |
| \(\lVert H_\lambda\rVert_F^2\) | one smoothed two-point scalar through \(D_C\) |
| \(b_{\mathrm{pos}}(\lambda)\) | the same scalar \(D_C\) |
| full spectrum / inertia | potentially higher-order, but no separable higher-order contribution was isolated |

Consequently, merely enlarging the existing calculation would not turn the first three quantities into higher-order observables. The limitation is mathematical before it is computational.

## 4.3 Plain-language interpretation

In nontechnical terms:

> **We built a first mathematical instrument. It worked correctly, but most of its gauges were designed in a way that could mainly see pairwise relationships. They could not cleanly reveal the deeper collective pattern we hoped to isolate. By testing the instrument rigorously, we learned exactly why it was limited, prevented several misleading interpretations, and obtained a much better basis for designing the next experiment.**

This is not a failed journey. It is the point at which the project learned how to ask the next question more precisely.

---

# 5. What Experiment 2 established

## 5.1 A reproducible finite Hermitian apparatus

The frozen Gaussian construction is mathematically transparent and computationally reproducible.

The experiment established that:

- the Gaussian Gram matrices were constructed correctly;
- the matrices were positive definite to the reported numerical resolution;
- the spectrum-first identity
  $$
  \eta_j(H_\lambda)=1-\lambda\mu_j(C)
  $$
  determines the complete frozen inertia flow;
- direct selected diagonalizations of \(H_\lambda\) agree with the spectrum-first route;
- trace and Frobenius identities agree to floating-point precision;
- no numerical sign ambiguity survives on the frozen grid.

These are not claims about RH. They are verified properties of the defined finite matrices.

## 5.2 A nontrivial but apparatus-specific inertia profile

The frozen toy produced a stable, nontrivial inertia profile.

For the primary \(m=512\) blocks:

- all directions remain positive through \(\lambda=0.30\);
- negative directions first appear on the frozen grid at \(\lambda=0.35\);
- the mean positive fraction is approximately \(0.777\) at \(\lambda=0.50\);
- approximately \(0.670\) at \(\lambda=0.70\);
- approximately \(0.597\) at \(\lambda=0.95\).

These values are meaningful as a characterization of the **frozen finite apparatus**. They are not universal invariants of zeta zeros.

## 5.3 The information hierarchy of the observables

The strongest conceptual result of the review cycle is the explicit information hierarchy.

The trace is data-free. The Frobenius second moment is a weighted two-point statistic. The positive-inertia lower bound is algebraically determined by that same two-point statistic:

$$
b_{\mathrm{pos}}(\lambda)
=
\frac{(1-\lambda)^2}
{(1-2\lambda)+\lambda^2(1+D_C)}.
$$

Only the complete spectrum or quantities involving higher matrix powers can, in principle, access higher-order point relationships.

This diagnosis explains why the original experiment did not cleanly answer its most ambitious question. It is more informative than simply observing that the numerical curves were not surprising.

## 5.4 The pair-correlation bridge as a reconstruction result

The direct Gaussian Gram energy and the histogram-based calculation are built from the same multiset of point differences.

The small discrepancy between them is principally controlled by:

- bin width;
- piecewise-constant quadrature;
- smoothness of the two-point function at the bin scale;
- agreement between two implementation paths.

The bridge remains useful as a normalization, quadrature, smoothness, and code-consistency check.

It is not an independent zeta discovery.

## 5.5 Finite-window and kernel dependence

The experiment established that quantitative inertia depends materially on the apparatus choices.

In particular:

- nested block-size effects are comparable to some of the process-comparison signals considered during review;
- changing \(\sigma\) from the frozen value \(1\) to \(0.5\) or \(2\) materially changes the inertia profile;
- the finite matrix is the object being studied, so block dependence is a property of the experimental definition rather than automatically a numerical error.

This produces a durable rule for future work:

> **A process comparison is interpretable only when matrix size, kernel, window geometry, and parameter range are fixed or explicitly controlled.**

## 5.6 A successful diagnostic and falsification role

Experiment 2 did not falsify the existence of higher-order zeta structure.

It did falsify or retire several interpretations of the first apparatus:

- that the bridge agreement was independent scientific evidence;
- that the positive-inertia bound was a meaningful process discriminator;
- that \(\mu_{\max}\) could be treated as a general rigidity proxy;
- that the observed number-variance ladder had an arithmetic interpretation without a thinning control.

Preventing these interpretations from entering a paper as findings is a substantive scientific outcome.

---

# 6. What Experiment 2 did not establish

Experiment 2 does **not** establish:

1. that the Riemann Hypothesis is true or false;
2. that the zeta zeros possess no higher-order structure;
3. that the complete Gaussian spectrum contains no higher-order information whatsoever;
4. that every ordinate-only Hermitian construction is insensitive to off-critical-line zeros;
5. that the frozen apparatus universally cannot detect RH failure;
6. that Davenport–Heilbronn or Epstein finite-window measurements define universal off-line-zero percentages;
7. that zeta and GUE/CUE are identical at finite height;
8. that the high-height residuals are mathematically zero;
9. that a convergence rate in height has been measured;
10. that \(H_\lambda\) is the finite compression of Weil's Hermitian form;
11. that the toy positive-inertia inequality is Alpöge–Furman's specialized inequality;
12. that the pair-correlation experiment numerically validates the Alpöge–Furman prime-side second moment;
13. that the Christoffel function directly yields an improved proportion of simple critical-line zeros;
14. that the exploratory fourth-moment value is a validated primary result;
15. that Experiment 3 is ready, unnecessary, closed, or already executed.

The absence of a clean higher-order detection in Experiment 2 is **not evidence of the absence of higher-order structure**. It is evidence that this apparatus and these summaries did not isolate it.

---

# 7. Permanent disposition of the review findings

## 7.1 Results retained

The permanent Experiment 2 record retains:

- the frozen Gaussian matrices and all numerical outputs;
- the complete inertia profiles;
- the numerical sign-resolution result;
- the trace and Frobenius identities;
- the finite-window and kernel-sensitivity measurements;
- the negligible Gaussian tail budget beyond \(u=30\);
- the exact information-content analysis of the principal observables;
- the bridge as an implementation and quadrature reconstruction check.

## 7.2 Interpretations reframed

The permanent record reframes:

- the pair bridge from “independent validation” to **reconstruction and quadrature consistency**;
- the height sequence in \(D_C\) from a second independent finding to a **Gaussian smoothing of the two-point evolution already measured in Experiment 1**;
- the positive-inertia lower bound from a process-sensitive measurement to an **algebraic lower bound and sanity check**;
- the overall outcome from “failure” to **computationally valid, scientifically informative, and structurally underpowered**.

## 7.3 Interpretations withdrawn or retracted

The permanent record withdraws:

- \(\mu_{\max}\) as a general rigidity proxy;
- any universal claim that the frozen toy cannot detect RH failure;
- any implication that the \(0.0421\%\) bridge discrepancy is special to zeta.

It retracts:

- the arithmetic/RH interpretation of the number-variance ladder.

## 7.4 Research branch closed

The direct route

$$
1-\Lambda_m(0)
\quad\longrightarrow\quad
\text{simple critical-line zero proportion}
$$

is closed under the current computational program.

The known values do not support that conversion. Reopening it would require new analytic on-line/off-line block accounting, not merely more numerical data.

## 7.5 Ideas retained but not promoted to Experiment 2 results

The following remain legitimate successor ideas, not frozen Experiment 2 findings:

- the fourth spectral moment \(\mu_4\) as the first separator of the stated Alpöge–Furman extremal and sine-process moment sequences;
- a core-plus-halo estimator to control fourth-moment boundary bias;
- controlled synthetic comparators;
- RH-false stress tests with precisely specified input representations;
- matched thinning controls;
- process-specific unfolding with an automatic mean-spacing assertion.

Their presence in the review record does not make them completed Experiment 2 results.

---

# 8. Why the closure result is scientifically meaningful

## 8.1 Not an empty experiment

Experiment 2 is not classified as scientifically empty.

It produced tangible knowledge at three levels.

### Mathematical knowledge about the instrument

The review identified exactly which observables are data-free, two-point-limited, or potentially higher-order.

### Computational knowledge about the implementation

The full numerical pipeline was independently reproduced, its signs were resolved, and its artifact integrity was verified.

### Methodological knowledge about future experiments

The review demonstrated that:

- apparently impressive agreement may be circular reconstruction;
- boundary and block effects must be compared with effect size;
- kernel dependence must be treated as part of the result;
- negative controls must be gates rather than decorations;
- unfolding must be appropriate to the actual point process;
- missing-point effects require thinning controls;
- an observable must contain the level of information required by the question.

These are concrete and transferable findings.

## 8.2 A milestone rather than a dead end

Experiment 2 marks a transition in Project Montecito.

Before Experiment 2, the project had a plausible intuition: a transparent indefinite Hermitian toy might convert point-process differences into informative inertia differences.

After Experiment 2, the project has a sharper conclusion:

> **A simple matrix is not useful merely because its spectrum is nontrivial. Its observables must be shown to contain information beyond the statistical level already measured.**

That conclusion narrows the search space and improves the next experimental design.

## 8.3 The optimistic but accurate interpretation

A fair summary is:

> **The first toy matrix did not reveal the deeper phenomenon we hoped to isolate. In the process, however, Project Montecito learned what the matrix could and could not measure, identified several misleading routes before publication, preserved a set of useful negative and methodological results, and developed better ideas for an explicitly higher-order successor experiment.**

This is an important scientific milestone because the project is moving forward with more information, not merely with more computation.

---

# 9. Relationship to Experiment 1

Experiment 2 closure does not alter, reopen, or weaken Experiment 1.

The following Experiment 1 assets remain frozen and valid:

- the first 10,000 unfolded zeta-zero point set;
- the empirical pair-correlation data;
- the low-height short-range distortion;
- the matched-GUE calibration;
- the high-height controls near zero numbers \(10^{12}\) and \(10^{21}\);
- the conclusion that the large low-height \(D_{0.5}\) distortion is suppressed below the experiment's approximately \(5\%\) detection scale at the two high heights;
- the raw-data provenance and checksums.

Experiment 1 need not be redone because the limitations found in Experiment 2 concern the **downstream apparatus and observables**, not the validity of the upstream zero data or pair-correlation measurements.

Any successor apparatus may reuse the frozen Experiment 1 point configurations and pair-correlation artifacts, subject to its own preregistered window, halo, or control requirements.

---

# 10. Boundary between Experiment 2 and successor work

## 10.1 Experiment 2 will not be overwritten

A future, better-targeted apparatus should not replace Experiment 2 retrospectively.

The scientific progression is itself valuable:

1. Experiment 1 established the point-process baseline.
2. Experiment 2 tested the first Hermitian apparatus.
3. Peer review established the apparatus's information limits.
4. A successor experiment can now be designed from those lessons.

Preserving that chronology is more honest and more informative than rewriting Experiment 2 as though the first design had never been attempted.

## 10.2 What constitutes a new experiment

The following would constitute successor research rather than an Experiment 2 correction:

- replacing the Gaussian kernel with a sinc-kernel higher-moment program;
- making \(\mu_4\) a primary observable;
- adding a core-plus-halo estimator;
- introducing repeated synthetic-process ensembles as a principal design;
- adding all-zero ordinate multisets;
- incorporating the real parts \(\beta\) of complex zeros;
- building a more faithful Weil-type construction;
- changing the primary scientific question from inertia characterization to explicit higher-order detection.

Such work must receive its own specification, preregistration, validation plan, controls, execution log, and review.

## 10.3 High-level successor requirements preserved by closure

Without deciding the detailed design, Experiment 2 establishes the following requirements for any successor that seeks higher-order structure:

1. the primary observable must be demonstrably higher-order;
2. numerical boundary bias must be measured and controlled before interpretation;
3. synthetic comparators and arithmetic stress tests must have distinct stated roles;
4. omission or thinning must be matched by explicit controls;
5. unfolding must be process-specific and validated by an automatic unit-spacing gate;
6. the information supplied to an RH-false control must be stated explicitly;
7. effect size must be compared against realization noise and window dependence;
8. positive and negative outcomes must both be interpretable before the run begins.

The detailed migration decision belongs to Part 5, not to this closure report.

---

# 11. Freeze and change-control rules

The following rules apply after this closure decision.

## 11.1 Frozen numerical artifacts

The original Experiment 2 inputs, frozen configuration, block manifest, code, machine-readable results, spectra, figures, and validation outputs are immutable historical artifacts.

They may not be silently regenerated, replaced, or edited.

## 11.2 Controlling interpretation

`Experiment2_Report_v2.md` is the controlling Experiment 2 scientific report.

`Experiment2_Report_v1.md` remains part of the historical record but is superseded for interpretation by Version 2.

## 11.3 Controlling peer-review disposition

`Experiment2_Peer_Review_Response_v1.md` is the controlling finding-by-finding disposition of PR-01 and PR-02.

The seven review-corpus source documents remain unchanged and retain their original authorship and sequence.

## 11.4 Reopening rule

Experiment 2 may be reopened only if one of the following occurs:

- a reproducible numerical error is discovered in a frozen artifact;
- an input-provenance failure is established;
- an independent audit demonstrates that a closure claim is unsupported by the archived evidence;
- the project owner explicitly authorizes a formal erratum or new report version.

A new model, kernel, statistic, control class, or research question is **not** a reason to reopen Experiment 2. It belongs to successor work.

## 11.5 Versioning rule

Any correction after closure must be issued as one of:

- an erratum;
- `Experiment2_Report_v3`;
- `Experiment2_Closure_Report_v2`;
- a separately versioned successor specification.

No silent correction is permitted.

---

# 12. Open items that do not block closure

The following remain open but are explicitly nonblocking:

1. independent packaging and reproduction of the peer reviewer's exact CUE power ensemble;
2. independent packaging and reproduction of the Davenport–Heilbronn control;
3. independent packaging and reproduction of the Epstein control;
4. a matched-thinned-CUE control package;
5. core-plus-halo validation of \(\mu_4\);
6. a targeted literature search before any novelty claim about the fourth-moment observation;
7. a decision among on-line-only, all-ordinate, and full-complex-zero stress tests;
8. a new Experiment 3 scientific specification;
9. a numerical companion software specification and audit;
10. the publication plan and manuscript update.

These items may materially shape future Project Montecito work. None changes the closure conclusion for the frozen Gaussian Experiment 2.

---

# 13. Closure artifact register

The formal closure decision relies on the following principal artifacts.

| Artifact | Role | SHA-256 |
|---|---|---|
| `Project_Montecito_Project_Specifications_v0.6.md` | Controlling scientific design baseline | `70ade4842e9eabbdaf352876266247b14cb7569fa7c57216905969a08ed15a2a` |
| `Project_Montecito_Experiment2_v1_FINAL.zip` | Frozen primary Experiment 2 package | `c5df778e606ad94d55c84c5e14d741f7a4549a89964e922e07a08612c812175e` |
| `Project_Montecito_Experiment2_Validation_v1.zip` | Separate validation package | `7496200c5de6a3ea82e4f9ce1ec300ea7736d16f09142843466e9843464c1512` |
| `Experiment2_Review_Corpus_Index_v1.md` | Seven-document provenance and response map | `007015954e626245347f805d74f58d05e372269a882a6d3f8dc2f9d4f75c5ff2` |
| `Experiment2_Peer_Review_Response_v1.md` | Formal reconciliation of PR-01 and PR-02 | `34d5e0ce436d607cfb4464f86986d0c4d6e8e89400d400aa2e6df2f58839bd4b` |
| `Experiment2_Peer_Review_Response_v1_Support.zip` | Closure recheck scripts, outputs, and logs | `8d304597e3ba4845e2c4efb516c6d34f67956124ac5617b92c8955d98d7a7c37` |
| `Experiment2_Report_v2.md` | Controlling revised scientific report | `38782299c171f0e2b7abe3dfc2c7455ff62cbaaa95bf39b4693a014b0cfd2c94` |

The exact seven-document review-corpus fingerprints are preserved in `Experiment2_Review_Corpus_Index_v1.md`.

The primary and validation internal artifact checksums were verified during Part 2. This closure report relies on those verification results rather than duplicating their full manifests.

---

# 14. Final closure certificate

## 14.1 Scientific decision

After review of the specification, primary computation, validation extension, adversarial peer-review corpus, formal finding disposition, closure reruns, revised report, and artifact integrity record, Project Montecito concludes:

> **The frozen Experiment 2 computation is correct and reproducible. Its original higher-order ambition was not achieved by the selected summary observables, but the resulting limitation is scientifically informative and sufficiently well understood to close the experiment.**

## 14.2 Result classification

The result is best classified as:

- a **validated computational experiment**;
- a **descriptive finite-matrix result**;
- an **information-content diagnosis**;
- an **informative limitation**;
- a **methodological and falsification milestone**;
- a **foundation for better-targeted successor work**.

It is not classified as:

- a proof or disproof;
- evidence for or against RH;
- a new zero-density theorem;
- a numerical validation of Alpöge–Furman;
- a universal impossibility result for Hermitian approaches;
- a validated detection of higher-order zeta structure.

## 14.3 Closure statement

```text
PROJECT_MONTECITO_EXPERIMENT_2

Scientific status: CLOSED
Closure date: 2 September 2026
Computation: complete and independently reproduced
Interpretation: corrected and frozen in Experiment2_Report_v2.md
Primary outcome: meaningful diagnostic limitation
Unresolved higher-order question: transferred to successor-design work
Experiment 1: remains frozen and unchanged
Experiment 3: not started; status and design deferred to Part 5
```

---

# 15. Part 4 completion and next-step boundary

This document completes:

> **Part 4 — `Experiment2_Closure_Report_v1.md`**

of the six-part Experiment 2 closure package.

With this decision, Experiment 2 is formally and scientifically closed.

This document does not:

- modify the frozen Experiment 2 computation;
- begin a new higher-order calculation;
- decide the detailed Experiment 3 design;
- adopt the peer reviewer's proposed Added Project Specifications;
- write the future publication plan;
- build or validate the proposed numerical companion.

The next planned closure artifact is:

`Experiment2_to_Experiment3_Migration_Manifest_v1.md`.

Its task will be to decide what data, lessons, controls, observables, exclusions, and research questions may migrate from the closed Experiment 2 phase into the next Project Montecito experiment.

No Part 5 work is performed in this document.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1 | 2 September 2026 | Formal scientific closure of Experiment 2 after independent reproduction, adversarial review, finding reconciliation, Report v2 revision, and artifact-integrity verification |
