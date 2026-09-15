# Project Montecito — Experiment 2 Peer-Review Response
## Version 1

**Date:** 2 September 2026  
**Closure package:** Part 2 of 6  
**Status:** Complete  
**Scientific baseline:** `Project_Montecito_Project_Specifications_v0.6.md`  
**Corpus index:** `Experiment2_Review_Corpus_Index_v1.md`  
**Direct peer-review sources:** PR-01 and PR-02  
**Interpretive response sources:** AR-01, AR-02, and AR-03  
**Closure recheck support:** `Experiment2_Peer_Review_Response_v1_Support.zip`

---

# 1. Purpose

This document is Project Montecito's formal response to the two scientific peer-review documents that directly audit and extend Experiment 2:

- **PR-01** — `09-experiment2-review`;
- **PR-02** — `12-exploring_further_experiment2`.

The response is informed by the three corresponding ChatGPT analyses:

- **AR-01** — `Your_review_of_Experiment_2_review`;
- **AR-02** — `Your_review_of_exploring_further_experiment2`;
- **AR-03** — `Your_final_analysis_of_experiment2_review`.

The provenance and mapping of these documents are fixed in `Experiment2_Review_Corpus_Index_v1.md`.

This response has four purposes:

1. disposition every material finding in PR-01 and PR-02;
2. distinguish original frozen Experiment 2 results from reviewer-generated follow-up work;
3. record the mathematical and computational rechecks performed for closure;
4. define the corrections that must be incorporated into `Experiment2_Report_v2.md`.

This document does **not** itself:

- rewrite `Experiment2_Report_v1.md`;
- issue the final Experiment 2 closure decision;
- adopt the peer reviewer's later proposed publication/software plan;
- define or begin Experiment 3;
- claim any new theorem or any evidence for or against the Riemann Hypothesis.

The peer reviewer's third document, `Project_Montecito_Added_Project_Specifications_v0.1`, and AR-04 are strategic context only. They are not direct subjects of this reconciliation.

---

# 2. Overall response

The central peer-review judgment is accepted:

> **The frozen Experiment 2 computation is numerically sound and independently reproducible, but several original interpretations overstated what the chosen observables could establish.**

The review did not uncover a numerical failure in the Gaussian Gram matrices, spectra, inertia classifications, trace/Frobenius identities, sign-resolution protocol, or high-height controls. The original computational workmanship remains valid.

The principal scientific correction is instead structural:

> **Experiment 2 was computationally successful but underpowered for its original scientific question.**

Three of the four advertised observable families have limited information content by construction:

- \(\operatorname{tr}H_\lambda\) contains no point-configuration information;
- \(\|H_\lambda\|_F^2\) depends on the configuration only through a two-point scalar;
- the normalized lower bound \(b_{\mathrm{pos}}\) depends on that same scalar;
- only the full spectrum or inertia can, in principle, reflect higher-order organization, and the completed experiment did not isolate such a contribution from ordinary two-point propagation.

The final response is therefore neither “Experiment 2 succeeded exactly as originally interpreted” nor “Experiment 2 failed.” It is:

> **The apparatus and numerical pipeline are valid. The review clarified what information the apparatus actually contains, retired several overinterpretations, and identified the requirements for a better successor experiment.**

---

# 3. Evidence classes used in this response

To prevent reviewer-generated calculations from being silently relabeled as original Experiment 2 results, every disposition below uses one or more of the following evidence classes.

| Code | Evidence class | Meaning |
|---|---|---|
| **FROZEN** | Frozen Experiment 2 artifact | Present in the preregistered primary package or its validation extension |
| **CR-COMP** | Closure-response computational recheck | Recomputed during preparation of this response from checksum-pinned artifacts or under a newly documented fixed protocol |
| **CR-MATH** | Closure-response mathematical recheck | Independently re-derived during preparation of this response |
| **PR-FOLLOWUP** | Peer-review follow-up result | Reported in PR-01 or PR-02 but not supplied with sufficient source artifacts for an exact independent rerun here |
| **INTERP** | Interpretive conclusion | A scientific characterization supported by the evidence, not a new numerical calculation |
| **FUTURE** | Successor-design item | Retained for later work; not an Experiment 2 result |

A PR-FOLLOWUP result may be scientifically valuable, but it must remain explicitly attributed unless its code, data, seeds, and outputs are later incorporated and independently reproduced.

---

# 4. Closure-response verification performed

## 4.1 Frozen package and artifact integrity

The final primary Experiment 2 package was materialized and audited directly.

It contains:

- the v0.6 specification;
- the frozen configuration;
- the exact nested block manifest;
- all six frozen input artifacts;
- `block_matrix_metrics.csv`;
- `C_spectra_and_crossings.csv`;
- all inertia tables;
- the figures;
- the report and execution log;
- the source code;
- the verification suite;
- the artifact manifest and SHA-256 map.

The closure audit found:

| Audit | Result |
|---|---:|
| Primary-package SHA-256 entries checked | 45 |
| Primary-package SHA-256 matches | **45 / 45** |
| Primary-package manifest rows | 45 |
| Manifest size/hash cross-check errors | **0** |
| Validation-package checksum entries checked | 19 |
| Validation-package checksum matches | **19 / 19** |

**Disposition:** the PR-01 objections that the reviewed handoff lacked the machine-readable data artifacts and v0.6 specification are **resolved in the final archived package**. The historical objection remains valid for the package the reviewer originally received; it is no longer an open closure defect.

## 4.2 Primary verification suite rerun

The frozen `src/verify_experiment2.py` suite was rerun in the following environment:

- Python 3.13.5;
- Linux 6.18.35 x86_64;
- NumPy 2.3.5;
- pandas 2.2.3;
- SciPy 1.17.0.

Result:

```text
all_passed = true
n_checks   = 19
n_passed   = 19
n_failed   = 0
```

Selected rerun values were:

| Check | Closure rerun value |
|---|---:|
| Exactly nested common locations | 16 |
| Block-matrix rows | 144 |
| Block/\(\lambda\) inertia rows | 2,592 |
| Minimum eigenvalue over all \(C\) blocks | \(9.4208996031\times10^{-5}\) |
| Unresolved frozen-grid signs | 0 |
| Maximum trace-identity error | \(1.1369\times10^{-13}\) |
| Maximum \(H\)-Frobenius identity error | \(3.4106\times10^{-13}\) |
| Maximum \(C\)-Frobenius spectral identity error | \(5.6843\times10^{-13}\) |
| Maximum direct-\(H\) spectrum difference | \(2.4869\times10^{-14}\) |
| Independent GUE weighted-benchmark difference | \(2.2204\times10^{-16}\) |

**Disposition:** PR-01's reproduction, PSD, inertia-map, sign-resolution, and numerical-cleanliness conclusions are accepted.

## 4.3 Independent validation implementation rerun

The separate validation implementation was also rerun against the frozen primary package. It reconstructed the Gaussian matrices and spectra independently.

At \(\sigma=1\), the largest independent-versus-primary differences included:

| Quantity | Maximum absolute difference |
|---|---:|
| \(\mu_{\min}(C)\) | \(1.6393\times10^{-15}\) |
| \(\mu_{\max}(C)\) | \(2.2204\times10^{-14}\) |
| Direct \(\lVert C\rVert_F^2\) | \(1.1369\times10^{-13}\) |
| Direct \(D_C\) | \(1.1102\times10^{-16}\) |
| Pair-predicted \(\lVert C\rVert_F^2\) | \(2.2737\times10^{-13}\) |
| Pair-predicted \(D_C\) | \(5.5511\times10^{-16}\) |
| Positive, negative, and unresolved inertia counts | **exactly identical** |
| Normalized \(b_{\mathrm{pos}}\) | \(1.1102\times10^{-16}\) |

All 2,592 primary block/\(\lambda\) sign classifications were reproduced exactly.

**Disposition:** the numerical core of Experiment 2 is independently validated.

## 4.4 Closed-form positive-inertia bound recheck

Starting from

\[
\operatorname{tr}H_\lambda=m(1-\lambda)
\]

and

\[
\|H_\lambda\|_F^2
=m(1-2\lambda)+\lambda^2\|C\|_F^2,
\]

write

\[
c:=\frac{\|C\|_F^2}{m}=1+D_C.
\]

Then

\[
\boxed{
 b_{\mathrm{pos}}(\lambda)
 =
 \frac{(1-\lambda)^2}
 {(1-2\lambda)+\lambda^2c}
 =
 \frac{(1-\lambda)^2}
 {(1-2\lambda)+\lambda^2(1+D_C)}
 }.
\]

This formula was evaluated against all 2,592 frozen rows. The maximum absolute difference from the stored values was

\[
3.33\times10^{-16}.
\]

Consequences:

1. there is no separate explicit dependence on \(m\) after \(c\) is specified;
2. the point configuration enters this bound only through the scalar \(c\);
3. the bound cannot distinguish configurations sharing the same \(c\);
4. its decay as \(\lambda\to1\) is algebraic, not an empirical discovery.

**Disposition:** the reviewer’s derivation is accepted. `b_pos` remains a valid lower-bound and implementation check, but it is retired as a discriminating scientific observable.

## 4.5 Pair-bridge interpretation recheck

Let bin \(B_k=[a_k,b_k]\) contain \(n_k\) positive pair differences. Under the finite-window estimator,

\[
\widehat R_{2,k}
=
\frac{n_k}
{\widehat\rho^2\int_{a_k}^{b_k}(L-u)\,du}.
\]

Substitution into the bridge gives

\[
2\widehat\rho^2
\sum_k \widehat R_{2,k}
\int_{a_k}^{b_k}(L-u)e^{-u^2}\,du
=
2\sum_k n_k
\frac{\int_{a_k}^{b_k}(L-u)e^{-u^2}\,du}
{\int_{a_k}^{b_k}(L-u)\,du}.
\]

The direct off-diagonal quantity is

\[
2\sum_{i<j}e^{-(x_j-x_i)^2}.
\]

Thus the bridge replaces each individual kernel weight inside a bin by an edge-weighted bin average. Both calculations use the same multiset of pair differences. Their discrepancy is principally deterministic histogram/quadrature error, not independent evidence about zeta.

For the numerical controls below, the signed relative Frobenius discrepancy is

\[
100\,\frac{\widehat F-F}{F},
\qquad
F=\lVert C\rVert_F^2,
\]

where \(F\) is the direct finite-matrix value and \(\widehat F\) is the histogram reconstruction. The table reports the magnitude for the positive zeta discrepancies.

The closure rerun reproduced the PR-01/PR-02 zeta bin-width sequence:

| Bin width \(\Delta u\) | Relative Frobenius discrepancy |
|---:|---:|
| 0.40 | 1.001829% |
| 0.20 | 0.254882% |
| 0.10 | 0.042085% |
| 0.05 | 0.014347% |

The same estimator applied to the exact unit lattice reproduced:

\[
D_C^{\mathrm{direct}}=0.77255623,
\qquad
D_C^{\mathrm{bridge}}=0.69495983,
\]

with relative Frobenius discrepancy

\[
-4.377655\%.
\]

This exactly confirms the reviewer’s substantive lattice control: a singular two-point measure concentrated at discrete spacings is poorly represented by a piecewise-constant density histogram.

A separate closure control generated 200 unit-density Poisson realizations of 10,000 points each using NumPy `default_rng` seed `20260902`. Each realization used independent exponential gaps and was rescaled to exact finite-sample mean nearest-neighbor spacing 1 before applying the same \(U_{\max}=30\), \(\Delta u=0.1\) estimator. Their bridge discrepancies were centered essentially at zero:

| Statistic | Value |
|---|---:|
| Mean signed discrepancy | \(-0.000025\%\) |
| Standard deviation | 0.015492% |
| Minimum | \(-0.035917\%\) |
| Maximum | 0.040089% |
| 1st–99th percentile range | \([-0.033215\%,\ 0.035726\%]\) |

This independently confirms the interpretive point: very small bridge discrepancies occur for an ordinary smooth process and are not special evidence about the zeta zeros.

The exact single Poisson and CUE realizations quoted by PR-01 were not reproducible from the review documents alone because their generator settings, seeds, and point arrays were not supplied. Their exact numbers therefore remain PR-FOLLOWUP results. The conclusion they support is nevertheless independently confirmed by the zeta rebinning, lattice, and new Poisson-ensemble checks.

**Disposition:** the bridge survives as a code-path, normalization, smoothness, and quadrature check. It is not a headline zeta finding or independent validation of the underlying mathematical theory.

## 4.6 Block-size sensitivity recheck

The frozen nested-scale table was recomputed and inspected.

For the primary low-height sample:

- largest **mean absolute** \(m=128\) versus \(m=512\) positive-fraction difference:
  \[
  0.0072021484
  \]
  at \(\lambda=0.40\);
- largest **single-location absolute** difference:
  \[
  0.0234375
  \]
  also at \(\lambda=0.40\).

PR-01 compared the first quantity with its reviewer-generated zeta-versus-CUE signal of approximately 0.0064. The 0.007202 block-size result is independently confirmed; the 0.0064 comparison value remains tied to the reviewer’s unsupplied CUE realization.

**Disposition:** the warning is accepted. Future process comparisons must fix \(m\) exactly and report finite-window sensitivity beside any effect size, especially near the first-crossing region.

## 4.7 Kernel sensitivity recheck

The independent validation extension confirms that quantitative inertia depends materially on the Gaussian bandwidth. For primary \(m=512\) blocks:

| \(\lambda\) | \(p_{\mathrm{pos}}\), \(\sigma=0.5\) | \(p_{\mathrm{pos}}\), \(\sigma=1\) | \(p_{\mathrm{pos}}\), \(\sigma=2\) |
|---:|---:|---:|---:|
| 0.35 | 1.000000 | 0.998657 | 0.834961 |
| 0.50 | 0.997559 | 0.776978 | 0.784546 |
| 0.70 | 0.788818 | 0.669678 | 0.750977 |
| 0.95 | 0.596436 | 0.596558 | 0.722290 |

**Disposition:** the statement “quantitative inertia is kernel dependent” is accepted. The primary \(\sigma=1\) analysis remains frozen; robustness kernels may not replace it post hoc.

## 4.8 Fourth-moment arithmetic recheck

For the first-two-moment extremal spectral distribution

\[
0\text{ with weight }\frac16,
\qquad
1\text{ with weight }\frac23,
\qquad
2\text{ with weight }\frac16,
\]

the exact moments are

\[
m_1=1,
\qquad
m_2=\frac43,
\qquad
m_3=2,
\qquad
m_4=\frac{10}{3}.
\]

Against the sine-process target sequence stated in the review corpus,

\[
1,\quad\frac43,\quad2,\quad\frac{13}{4},
\]

the first separation is therefore

\[
\boxed{
 m_4^{\mathrm{extremal}}-m_4^{\mathrm{sine}}
 =
 \frac{10}{3}-\frac{13}{4}
 =
 \frac1{12}
 }.
\]

**Disposition:** the arithmetic is accepted. For this specific extremal-versus-sine comparison, \(\mu_4\), not \(\mu_3\), is the first separating moment. This is a future-design observation, not a completed Experiment 2 result, and no novelty claim is made here.

## 4.9 Thinning identity recheck

Let \(N_A\) be the original count in a window of length \(A\), and retain each point independently with probability \(p\). Conditional on \(N_A\),

\[
M_A\mid N_A\sim\operatorname{Binomial}(N_A,p).
\]

Therefore

\[
\operatorname{Var}(M_A)
=p^2\operatorname{Var}(N_A)
+p(1-p)\operatorname{E}(N_A).
\]

After rescaling the thinned process to unit density, a window of length \(L\) corresponds to \(A=L/p\) in the original coordinates. Hence

\[
\boxed{
\Sigma_{\mathrm{thin}}^2(L)
=
 p^2\Sigma_{\mathrm{orig}}^2(L/p)
 +(1-p)L
}.
\]

The linear term \((1-p)L\) is unavoidable under independent thinning and can dominate the slowly growing number variance of a rigid process.

**Disposition:** the mathematical confound is established. The proposed arithmetic interpretation of the DH/Epstein number-variance ladder is retracted. The reviewer’s exact matched-thinned-CUE simulation remains PR-FOLLOWUP because its seeds and outputs were not supplied, but that simulation is not needed to establish that thinning is a decisive confound.

## 4.10 Reviewer-generated follow-up calculations not exactly rerun here

The following calculations were not supplied with sufficient machine-readable artifacts for exact closure reproduction:

- the exact CUE bridge realization and eight-realization CUE power table;
- the Davenport–Heilbronn zero search, finite-window counting, unfolding, spectra, and inertia profiles;
- the Epstein zeta zero search, finite-window counting, unfolding, spectra, and inertia profiles;
- the exploratory \(\mu_4=3.2601\pm0.0198\) estimate and the reported \(-0.018\) versus \(-0.0007\) boundary-bias comparison;
- the exact matched-thinned-CUE simulation said to reproduce the number-variance values within approximately two standard deviations.

These are not rejected. They are retained as **PR-FOLLOWUP** findings and interpreted cautiously. They may be promoted to independently reproduced project artifacts later only if their code, inputs, seeds, and outputs are added and audited.

## 4.11 Closure recheck support record

The scripts, machine-readable outputs, and captured verification logs generated specifically for this reconciliation are archived in:

`Experiment2_Peer_Review_Response_v1_Support.zip`

SHA-256:

`8d304597e3ba4845e2c4efb516c6d34f67956124ac5617b92c8955d98d7a7c37`

The support archive records the exact Poisson protocol and all 200 realization-level outputs, the zeta bin-width sequence, the lattice control, representative kernel-sensitivity values, package-integrity results, the original verification-suite output, and the independent-validation output. Its internal `SHA256SUMS.txt` fingerprints every support file.

The upstream archives used by the closure reruns were:

| Archive | SHA-256 |
|---|---|
| `Project_Montecito_Experiment2_v1_FINAL.zip` | `c5df778e606ad94d55c84c5e14d741f7a4549a89964e922e07a08612c812175e` |
| `Project_Montecito_Experiment2_Validation_v1.zip` | `7496200c5de6a3ea82e4f9ce1ec300ea7736d16f09142843466e9843464c1512` |

This support record concerns only the closure-response rechecks. It does not convert the unsupplied CUE, DH, Epstein, exploratory \(\mu_4\), or matched-thinning calculations into independently reproduced project artifacts.

---

# 5. Disposition vocabulary

| Disposition | Meaning |
|---|---|
| **ACCEPT** | The finding is supported and carried forward |
| **ACCEPT WITH QUALIFICATION** | The core result is retained with narrower scope or wording |
| **REFRAME** | The computation remains valid but its scientific meaning changes |
| **WITHDRAW INTERPRETATION** | A previously suggested interpretation is no longer supported |
| **CLOSE BRANCH** | A specific proposed research route is stopped |
| **RESOLVED** | A package or documentation defect has been corrected |
| **DEFER** | The issue belongs to Report v2, the closure report, migration manifest, or successor design |
| **ATTRIBUTE** | Retain as a reviewer-generated follow-up result, not an independently reproduced original result |

---

# 6. Detailed response to PR-01 — `09-experiment2-review`

## PR-01.1 — Exact numerical reproduction

**Reviewer finding.** Every checkable primary quantity reproduced to all printed digits.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-COMP.

The closure rerun confirms 19/19 primary checks, 45/45 primary artifact hashes, 19/19 validation hashes, and exact agreement of all 2,592 inertia classifications in the independent validation implementation.

**Report v2 action:** retain the numerical results and strengthen the reproducibility statement with the post-review rerun record.

---

## PR-01.2 — Finite-window bridge derivation

**Reviewer finding.** The factor of two, factorial-density normalization, translation-edge factor, analytic bin integral, and \(u>30\) tail bound are correct.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-MATH, CR-COMP.

The bridge formula itself is mathematically and computationally correct. The correction concerns its interpretation, not its derivation.

**Report v2 action:** keep the derivation and tail budget.

---

## PR-01.3 — Gaussian PSD and spectrum-first inertia map

**Reviewer finding.** The Gaussian kernel is positive definite, and

\[
\eta_j(H_\lambda)=1-\lambda\mu_j(C)
\]

exactly determines inertia.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-MATH, CR-COMP.

**Report v2 action:** retain without substantive change.

---

## PR-01.4 — Sign-specific positive-inertia inequality

**Reviewer finding.** The inequality

\[
n_{\mathrm{pos}}(H)
\ge
\frac{\operatorname{tr}(H)^2}{\|H\|_F^2}
\]

under \(\operatorname{tr}H>0\) is correct.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-MATH, CR-COMP.

The inequality remains valid and was never violated by the frozen data.

**Report v2 action:** retain the proof but immediately add the closed form and information-content limitation.

---

## PR-01.5 — Closed form and role of `b_pos`

**Reviewer finding.** `b_pos` depends on the configuration only through \(c=1+D_C\), has no separate explicit block-size dependence once \(c\) is fixed, and cannot discriminate configurations with the same second moment.

**Disposition:** **ACCEPT AND REFRAME.**  
**Evidence:** CR-MATH, CR-COMP.

The closure response reproduced all stored values from the closed form to a maximum error of \(3.33\times10^{-16}\).

**Report v2 action:**

- add the closed form;
- remove `b_pos` from the list of discriminating observables;
- retain it only as a valid algebraic lower bound and implementation sanity check;
- state that its collapse near \(\lambda=1\) is an algebraic consequence.

---

## PR-01.6 — Numerical sign resolution

**Reviewer finding.** No hidden zero assignment exists on the frozen grid; the closest sign margin is safely outside the screening threshold.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-COMP.

**Report v2 action:** retain the sign-resolution result and continue to use “resolved/unresolved,” not “certified/uncertified.”

---

## PR-01.7 — The pair bridge is a reconstruction, not independent evidence

**Reviewer finding.** Direct \(D_C\) and histogram-predicted \(D_C\) summarize the same pair differences; the small discrepancy is principally binning/quadrature error.

**Disposition:** **ACCEPT AND REFRAME.**  
**Evidence:** CR-MATH, CR-COMP.

The exact zeta bin-width sequence, lattice failure, and Poisson ensemble independently confirm this conclusion.

**Report v2 action:** replace “strongest direct validation” and similar wording with:

> **The frozen empirical pair-correlation histogram reconstructs the corresponding smooth Gaussian pair functional with the expected discretization accuracy. This validates normalization and two code paths; it is not an independent zeta-zero finding.**

---

## PR-01.8 — The finite-height `D_C` shift is not a second independent confirmation

**Reviewer finding.** Since \(D_C\) is a linear smoothing of \(R_2\), the height dependence of \(D_C\) follows from Experiment 1’s measured two-point change.

**Disposition:** **ACCEPT AND REFRAME.**  
**Evidence:** CR-MATH, FROZEN.

The values

\[
0.920167\to0.945814\to0.951435
\]

remain valid. Their meaning is that the known finite-height two-point distortion propagates through the Gaussian weight—not that an independent observable separately confirms the phenomenon.

**Report v2 action:** merge original findings 1 and 2 conceptually and remove claims of independent confirmation.

---

## PR-01.9 — Kernel dependence

**Reviewer finding.** Quantitative inertia is kernel dependent; \(\sigma\) must remain frozen in cross-process comparisons.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN validation extension, CR-COMP.

**Report v2 action:** retain the \(\sigma=0.5,1,2\) sensitivity results and state that they demonstrate model dependence rather than robustness of a universal numerical profile.

---

## PR-01.10 — Spectral-tail interpretation

**Reviewer finding.** Height differences are concentrated near the upper edge and lower tail of the \(C\) spectrum, while the median and later-\(\lambda\) inertia are comparatively stable.

**Disposition:** **ACCEPT WITH QUALIFICATION.**  
**Evidence:** FROZEN validation extension, CR-COMP, INTERP.

The spectral diagnostics are descriptive and valid. They do not, by themselves, establish a rigidity ordering or isolate higher-order structure.

**Report v2 action:** preserve the spectral-tail description but avoid using a single spectral scalar as a general rigidity measure.

---

## PR-01.11 — Initial proposal to promote `mu_max`

**Reviewer finding.** The initial review proposed \(\mu_{\max}\) as a “rigidity ladder.” The v2 addendum withdrew that recommendation after the Davenport–Heilbronn control broke the proposed ordering.

**Disposition:** **ACCEPT THE WITHDRAWAL.**  
**Evidence:** PR-FOLLOWUP, INTERP.

`mu_max` remains a descriptive short-range spectral statistic. It must not be presented as a general rigidity proxy.

**Report v2 action:** report it only where needed to explain first crossing thresholds; remove any rigidity-ladder interpretation.

---

## PR-01.12 — CUE power calculation and Experiment 3 readiness

**Reviewer finding.** Eight independent CUE realizations gave effect/noise approximately 5.2, supporting the apparatus’s ability to resolve the low-height zeta-versus-CUE difference.

**Disposition:** **ATTRIBUTE AND DEFER.**  
**Evidence:** PR-FOLLOWUP.

The exact calculation was not independently rerun because its generator settings, seeds, and arrays were not supplied. It is not required to establish Experiment 2’s numerical validity.

**Report v2 action:** do not use this reviewer-generated power table as an unqualified Experiment 2 result. A future controlled-comparator design should preregister and ship between-realization ensembles.

---

## PR-01.13 — Height controls as a natural experiment

**Reviewer finding.** Low-height pair-correlation and inertia differences appear together, while high-height pair correlation and inertia both approach the GUE/CUE controls.

**Disposition:** **ACCEPT WITH QUALIFICATION.**  
**Evidence:** FROZEN for zeta height controls; PR-FOLLOWUP for exact CUE comparison; INTERP.

The pattern is consistent with the observed Level-2 effect being ordinary propagation of Level-1 structure. It is useful negative evidence. It does **not** prove that the full inertia contains only pair-correlation information in every process or parameter regime.

**Report v2 action:** describe the pattern as a consistency result and limitation, not a universal theorem about the apparatus.

---

## PR-01.14 — Missing machine-readable artifacts

**Reviewer finding.** The package presented to the reviewer listed essential files but did not ship them.

**Disposition:** **RESOLVED.**  
**Evidence:** CR-COMP package audit.

The final primary archive contains all named artifacts, and every manifest/hash entry passes.

**Report v2 action:** update the reproducibility map and final package manifest; preserve the historical review finding in this response.

---

## PR-01.15 — Missing v0.6 specification in the reviewed repository

**Reviewer finding.** The reviewer could not audit preregistration compliance against the claimed v0.6 document.

**Disposition:** **RESOLVED.**  
**Evidence:** CR-COMP package audit.

The final primary archive contains the exact v0.6 specification in `00_preregistration/` and the configuration explicitly records `specification_version = 0.6`.

**Report v2 action:** cite the archived v0.6 path and checksum.

---

## PR-01.16 — Block-size sensitivity comparable with the reported process signal

**Reviewer finding.** The largest mean absolute \(m=128\) versus \(m=512\) difference is 0.007202 at \(\lambda=0.40\), comparable with the reviewer’s approximately 0.0064 zeta-versus-CUE effect.

**Disposition:** **ACCEPT THE BLOCK-SENSITIVITY FINDING; ATTRIBUTE THE CUE EFFECT.**  
**Evidence:** CR-COMP for 0.007202; PR-FOLLOWUP for 0.0064.

**Report v2 action:** state explicitly that block/window sensitivity is of the same order as small cross-process effects near the crossing region. Future comparisons must fix block size and display scale sensitivity beside effect size.

---

## PR-01.17 — Groskin-style truncation pathology

**Reviewer finding.** The Gaussian toy has no hidden archimedean cutoff tail analogous to the adjacent finite Weil-form problem; its matrix is the defined finite object, and the Gaussian pair tail is negligible.

**Disposition:** **ACCEPT.**  
**Evidence:** FROZEN, CR-MATH, CR-COMP.

The relevant residual sensitivity is finite block/window choice, not a missing Gaussian-kernel tail.

**Report v2 action:** retain this distinction.

---

## PR-01.18 — Freeze recommendation

**Reviewer finding.** Freeze Experiment 2 after correcting the framing, observable role, package completeness, and scale comparison.

**Disposition:** **ACCEPT WITH PROCESS QUALIFICATION.**

This peer-review response resolves or dispositions those issues. Formal scientific closure still requires:

1. `Experiment2_Report_v2.md`;
2. `Experiment2_Closure_Report_v1.md`;
3. the final migration manifest and updated reproducibility status.

**Report v2 action:** implement every accepted change in Section 9 below.

---

## PR-01.19 — v2 claim that Experiment 3 is superseded

**Reviewer finding.** The DH/Epstein controls are said to make the original synthetic-process Experiment 3 unnecessary.

**Disposition:** **DO NOT ADOPT IN THIS RESPONSE; DEFER TO MIGRATION DESIGN.**  
**Evidence:** INTERP.

Synthetic GUE/CUE, Poisson, and lattice controls vary point-process geometry in a controlled and interpretable way. DH/Epstein on-line subsets ask a different question and do not directly expose \(\beta\)-coordinates. The two control classes are complementary.

**Report v2 action:** remove any definitive declaration that Experiment 3 is ready, superseded, or closed. Its status belongs to the later migration manifest.

---

## PR-01.20 — v2 claim that the apparatus cannot detect RH failure

**Reviewer finding.** The addendum states universally that “the apparatus cannot detect RH-failure.”

**Disposition:** **REFRAME AND NARROW.**  
**Evidence:** PR-FOLLOWUP, CR-MATH, INTERP.

The frozen toy takes unfolded ordinates

\[
X=\{x(\gamma_i)\}
\]

and does not receive the real parts \(\beta_i\) of zeros \(\rho_i=\beta_i+i\gamma_i\). In the reported DH/Epstein controls, the on-line subset was selected and then renormalized, so direct off-line information was removed before the matrix was constructed.

The supportable statement is:

> **In the finite windows and parameter regime reported by the peer reviewer, the frozen ordinate-only Gaussian apparatus showed no reliable sensitivity to RH failure in the on-line zero subsets of the two tested functions. This is consistent with the apparatus receiving ordinates but not real-part information.**

The statements “the toy sees only pair correlation” and “the apparatus can never detect RH failure” are not established.

**Report v2 action:** use only the narrow wording above, with explicit PR-FOLLOWUP attribution unless the control artifacts are later supplied and reproduced.

---

# 7. Detailed response to PR-02 — `12-exploring_further_experiment2`

## PR-02.A — Structural analysis of the observables

**Reviewer finding.** Three of the four advertised observables are structurally incapable of answering the intended beyond-two-point question.

**Disposition:** **STRONGLY ACCEPT.**  
**Evidence:** CR-MATH, CR-COMP, INTERP.

The exact hierarchy is:

\[
\operatorname{tr}H_\lambda=m(1-\lambda)
\quad\text{contains no point-set data};
\]

\[
\|H_\lambda\|_F^2
\quad\text{depends only on }\operatorname{tr}(C^2);
\]

\[
b_{\mathrm{pos}}(\lambda)
\quad\text{depends only on the same normalized second moment};
\]

while

\[
p_{\mathrm{pos}}(\lambda)=F_C(1/\lambda)
\]

depends on the full spectral distribution of \(C\) and can, in principle, reflect traces \(\operatorname{tr}(C^k)\) for \(k\ge3\).

The completed Experiment 2 did not isolate such higher-order sensitivity from two-point propagation.

**Report v2 action:** add a dedicated “information content of the observables” section and characterize Experiment 2 as underpowered for its original higher-order question.

---

## PR-02.B — Bridge circularity and quadrature controls

**Reviewer finding.** The 0.04% agreement is quadrature/code-path consistency, not a zeta discovery.

**Disposition:** **ACCEPT AND REFRAME.**  
**Evidence:** CR-MATH, CR-COMP.

The closure response independently reproduced the full zeta bin-width sequence and exact lattice values, and added a 200-realization Poisson control.

**Report v2 action:** demote the bridge from headline scientific result to validation result.

---

## PR-02.C — Power calculation

**Reviewer finding.** The instrument can resolve the low-height zeta-versus-CUE effect under the reviewer’s eight-realization ensemble.

**Disposition:** **ATTRIBUTE AND DEFER.**  
**Evidence:** PR-FOLLOWUP.

The result is relevant to successor design, not needed for Experiment 2 closure, and not independently reproducible from the supplied review documents.

**Report v2 action:** either omit the numerical table or identify it explicitly as a peer-review follow-up. Do not use it as the basis for a formal Experiment 3 decision in Report v2.

---

## PR-02.D — Height controls as a natural experiment

**Reviewer finding.** Level-1 and Level-2 discrepancies appear and disappear together.

**Disposition:** **ACCEPT WITH QUALIFICATION.**  
**Evidence:** FROZEN, PR-FOLLOWUP, INTERP.

This is useful evidence that the observed inertia differences need no explanation beyond the known two-point changes. It is not proof that no higher-order sensitivity exists.

**Report v2 action:** present as a negative/limiting consistency observation.

---

## PR-02.E — Sinc-kernel moment ladder

**Reviewer finding.** Spectral moments of a sinc-kernel matrix provide an explicit route beyond \(\operatorname{tr}(C^2)\).

**Disposition:** **RETAIN AS FUTURE EXPLORATORY DIRECTION.**  
**Evidence:** CR-MATH for the information hierarchy; PR-FOLLOWUP for scouting numerics.

The moment ladder is not part of the frozen Gaussian Experiment 2 and must not be inserted retroactively as though preregistered.

**Report v2 action:** mention only in future work or a clearly labeled post-review exploration section.

---

## PR-02.F — Correction from `mu_3` to `mu_4`

**Reviewer finding.** The specific first-two-moment extremal and sine-process target agree through the third moment and first separate at the fourth.

**Disposition:** **ACCEPT.**  
**Evidence:** CR-MATH.

The exact difference is \(1/12\).

**Qualifications:**

- this is specific to the stated extremal-versus-sine comparison;
- it does not mean \(\mu_3\) contains no higher-order information in general;
- no novelty claim is made without a targeted literature review.

**Report v2 action:** retain as a secondary successor-design insight, not as an Experiment 2 result.

---

## PR-02.G — Exploratory `mu_4` measurement and boundary bias

**Reviewer finding.** High-height zeta gave \(\mu_4=3.2601\pm0.0198\), but chopped blocks showed approximately \(-0.018\) bias versus about \(-0.0007\) for complete runs.

**Disposition:** **ATTRIBUTE; RETAIN AS PROMISING BUT UNRESOLVED.**  
**Evidence:** PR-FOLLOWUP, INTERP.

The underlying arrays and code were not supplied for independent reproduction. The reported bias is material relative to the target separation \(1/12\).

AR-03's stronger requirement is adopted:

> Before \(\mu_4\) becomes a primary successor observable, validate a core-plus-halo estimator and increase the halo until the core \(\mu_4\) stabilizes.

Matched-bias cancellation alone is not yet sufficient.

**Report v2 action:** no headline \(\mu_4\) numerical claim. Place the idea in future work with the boundary-bias gate.

---

## PR-02.H — Christoffel ladder

**Reviewer finding.** The direct conversion from \(1-\Lambda_m(0)\) to a certified simple-critical-line proportion fails against known cases and would require new analytic block accounting.

**Disposition:** **CLOSE THE DIRECT CHRISTOFFEL-TO-PROPORTION BRANCH.**  
**Evidence:** CR-MATH, INTERP.

This closure applies to the proposed direct conversion. It does not invalidate spectral-moment exploration generally.

**Report v2 action:** record the branch as closed and do not imply a route to an improved zero-proportion bound.

---

## PR-02.I — Davenport–Heilbronn control

**Reviewer finding.** The reviewer located off-line zeros, identified scan-resolution and unfolding traps, and found the frozen ordinate-only Gaussian inertia close to zeta.

**Disposition:** **ACCEPT AS A VALUABLE PR-FOLLOWUP CONTROL WITH NARROW WORDING.**  
**Evidence:** PR-FOLLOWUP, CR-MATH, INTERP.

Durable methodological lessons accepted:

1. zero-search resolution can miss close pairs in a hypothesis-favorable direction;
2. unfolding must match the actual point process being analyzed;
3. mean unfolded spacing near one must become a code-level assertion;
4. an ordinate-only apparatus has no direct access to \(\beta\).

The reported 8.3% is a finite-window counting deficit, not a universal proportion for the function.

**Report v2 action:** if included, label the numerical values as reviewer-generated follow-up and use the finite-window/on-line-subset wording.

---

## PR-02.J — Epstein zeta control

**Reviewer finding.** A class-number-two Epstein example gave a larger finite-window deficit while the ordinate-only Gaussian inertia remained comparatively close.

**Disposition:** **ACCEPT AS A SECOND PR-FOLLOWUP STRESS TEST WITH NARROW WORDING.**  
**Evidence:** PR-FOLLOWUP, CR-MATH, INTERP.

The reported 32.3% is a finite-window counting deficit, not a universal asymptotic percentage. The second example materially strengthens the empirical stress test but does not establish a universal impossibility theorem.

**Report v2 action:** use the same provenance and scope qualifications as for DH.

---

## PR-02.K — Number variance and thinning

**Reviewer finding.** The apparent arithmetic number-variance ladder was reproduced by thinning a rigid process and was retracted.

**Disposition:** **ACCEPT THE RETRACTION.**  
**Evidence:** CR-MATH for the exact thinning identity; PR-FOLLOWUP for the exact matched-CUE simulation.

The durable conclusion is:

> **Number variance of a surviving on-line subset is strongly confounded by missing-point/thinning effects and cannot, by itself, distinguish arithmetic loss of critical-line zeros from ordinary point deletion.**

Number variance is not declared universally useless; no residual claim is supported by the current data.

**Report v2 action:** record the withdrawn arithmetic interpretation in a post-review corrections subsection or appendix. Do not present the ladder as a project result.

---

## PR-02.L — “Experiment 2 failed”

**Reviewer framing.** The document repeatedly describes Experiment 2 as having failed.

**Disposition:** **REFRAME.**  
**Evidence:** INTERP.

Preferred wording:

> **Experiment 2 was computationally valid but underpowered for the scientific question it was intended to answer.**

This wording preserves both facts:

- the numerical experiment worked as specified;
- most selected observables could not isolate the information level sought.

**Report v2 action:** use “underpowered” or “structurally limited,” not an unqualified “failed.”

---

## PR-02.M — “Every apparent discovery died”

**Reviewer framing.** The lessons section says every apparent discovery that was tested died.

**Disposition:** **REVISE THE RHETORIC.**  
**Evidence:** INTERP.

Several interpretations were correctly withdrawn, but durable results remain:

- numerical validity of Experiment 2;
- exact information-content diagnosis;
- bridge reconstruction result;
- fourth-moment separation for the stated spectral models;
- ordinate-only limitation of the tested controls;
- thinning confound;
- process-specific unfolding requirement;
- the value of mandatory negative controls.

**Report v2 action:** distinguish “retraction,” “withdrawn interpretation,” “reframing,” “closed branch,” and “retained secondary idea.”

---

## PR-02.N — Negative controls and unfolding as gates

**Reviewer lesson.** RH-false controls should be gates rather than optional extensions, and mean-spacing validation should be asserted in code.

**Disposition:** **ACCEPT FOR RELEVANT FUTURE OBSERVABLES.**  
**Evidence:** PR-FOLLOWUP, CR-MATH, INTERP.

The exact form of a negative control must be specified:

1. on-line-only ordinate subset;
2. all-zero ordinate multiset preserving multiplicity;
3. full complex-zero representation retaining \(\beta\) and \(\gamma\).

These are not interchangeable.

**Report v2 action:** record the methodological lesson; defer actual successor-control design to the migration manifest.

---

# 8. Consolidated scientific state after reconciliation

## 8.1 What survives unchanged

The following Experiment 2 results remain valid:

1. The preregistered Gaussian Gram matrices were constructed correctly.
2. Every \(C\) block was positive definite to the reported numerical resolution.
3. The spectrum-first map exactly determines the frozen \(H_\lambda\) inertia profiles.
4. All frozen-grid signs were comfortably resolved.
5. Trace, Frobenius, spectral, and direct-eigendecomposition identities pass.
6. The primary inertia curves and their finite-window variation are reproducible descriptive properties of the defined toy matrices.
7. Quantitative inertia depends materially on kernel bandwidth.
8. The Gaussian tail beyond \(u=30\) is negligible for the bridge calculation.

## 8.2 What is reframed

1. **Pair bridge:** reconstruction/quadrature validation, not independent zeta evidence.
2. **Height dependence of \(D_C\):** Gaussian smoothing of the already measured two-point change, not a second independent confirmation.
3. **Trace/Frobenius bound:** correct lower bound and algebraic sanity check, not an inertia predictor or process discriminator.
4. **Experiment 2 outcome:** computationally valid but structurally underpowered for its higher-order question.
5. **Height-control pattern:** consistency with Level-1 propagation, not proof that the apparatus contains no higher-order information.

## 8.3 What is withdrawn

1. `mu_max` as a general rigidity proxy.
2. The number-variance ladder as an arithmetic/RH-sensitive result.
3. Any universal statement that the frozen toy “cannot detect RH failure.”
4. Any implication that the 0.0421% bridge discrepancy is a special zeta phenomenon.

## 8.4 What is closed

The direct Christoffel-function-to-simple-zero-proportion route is closed unless new analytic block accounting is developed.

## 8.5 What is retained for future work

1. \(\mu_4\) as a secondary higher-order diagnostic for the specific extremal-versus-sine comparison;
2. a core-plus-halo boundary-bias validation before any primary \(\mu_4\) claim;
3. controlled synthetic comparators and RH-false stress tests as distinct control classes;
4. matched thinning where a point subset is created by omission;
5. process-specific unfolding with an automatic mean-spacing assertion;
6. explicit control over what RH-failure information is supplied to an apparatus.

---

# 9. Mandatory changes for `Experiment2_Report_v2.md`

The following changes are approved and required.

## 9.1 Front matter and status

Replace any pre-review readiness language with:

> **Experiment 2 computational status: complete and independently reproduced.**  
> **Experiment 2 interpretation: revised after adversarial peer review.**  
> **Formal scientific closure: pending the closure report.**

Remove `COMPUTATIONAL_EXPERIMENT3_READY = TRUE` from the scientific conclusion. Experiment 3 status belongs to the later migration manifest.

## 9.2 Executive summary

The revised executive summary should lead with:

1. numerical validity and reproducibility of the apparatus;
2. the nontrivial but descriptive inertia profile;
3. the structural information-content diagnosis;
4. the bridge as histogram reconstruction;
5. kernel and finite-window dependence;
6. the resulting limitation: the experiment did not isolate beyond-two-point information.

The original bridge and \(D_C\)-height findings must not appear as two independent headline discoveries.

## 9.3 Positive-inertia section

Add

\[
b_{\mathrm{pos}}(\lambda)
=
\frac{(1-\lambda)^2}
{(1-2\lambda)+\lambda^2(1+D_C)}.
\]

State explicitly that:

- the formula depends on the point configuration only through \(D_C\);
- the disappearance of the lower bound near \(\lambda=1\) is algebraic;
- `b_pos` is not a discriminating observable.

Remove “important limiting result” if it implies an empirical discovery.

## 9.4 Bridge section

Retain the correct finite-window formula and tail bound, but add the substitution showing that the histogram calculation is an edge-weighted bin approximation to the direct sum over the same pair differences.

Add the closure controls:

- zeta bin-width sequence;
- exact lattice failure;
- fixed-seed Poisson ensemble summary.

Retitle the result along the lines of:

> **Histogram reconstruction of the Gaussian pair functional.**

## 9.5 Structural information-content section

Add a new section explaining:

| Observable | Information content |
|---|---|
| \(\operatorname{tr}H_\lambda\) | none from the point set |
| \(\lVert H_\lambda\rVert_F^2\) | normalized two-point scalar |
| \(b_{\mathrm{pos}}\) | the same scalar only |
| full spectrum / \(p_{\mathrm{pos}}\) | potentially higher-order, but not isolated here |

This section should contain the central conclusion that the original apparatus was underpowered for the intended higher-order question.

## 9.6 Finite-window section

Keep the frozen scale results and add the explicit comparison:

- mean absolute \(m=128\) versus \(m=512\) difference 0.007202 at \(\lambda=0.40\);
- maximum single-location difference 0.023438 at \(\lambda=0.40\).

Do not imply that internal block stability alone demonstrates adequate power for every future process comparison.

## 9.7 High-height controls

Keep the numerical values, but state:

- the \(D_C\) sequence is a smoothed consequence of the measured two-point evolution;
- the low/high inertia pattern is consistent with Level-1 propagation;
- it does not prove that inertia is universally determined by pair correlation.

## 9.8 Spectral statistics

Retain `mu_max` only to describe the upper spectral edge and first crossing. Remove any rigidity-proxy interpretation.

## 9.9 Post-review follow-up section

Add a clearly labeled section or appendix titled, for example:

> **Peer-review follow-up controls and withdrawn interpretations**

It should distinguish:

- **independently rechecked mathematics:** `b_pos`, bridge quadrature structure, \(\mu_4\) arithmetic, thinning identity;
- **reviewer-generated calculations not independently rerun here:** exact CUE ensemble, DH/Epstein numerics, exploratory \(\mu_4\), matched-thinned-CUE simulation;
- **withdrawn interpretations:** rigidity ladder and arithmetic number-variance claim;
- **closed branch:** direct Christoffel-to-proportion conversion;
- **future direction:** boundary-controlled \(\mu_4\).

## 9.10 DH/Epstein wording, if included

Use only finite-window, on-line-subset, ordinate-only wording. Do not write that DH “has 8.3% of its zeros off line” or Epstein “has 32.3% off line” without qualification.

Preferred wording:

> **In the finite windows reported by the peer reviewer, approximately 8.3% and 32.3% of the expected zeros, respectively, were not represented on the critical line. The frozen ordinate-only Gaussian apparatus showed no reliable sensitivity to RH failure in these two on-line-subset controls.**

Because the underlying control artifacts were not included in PR-01/PR-02, these values must remain attributed unless later reproduced.

## 9.11 Experiment 2 conclusion

The final Report v2 conclusion should state:

> **Experiment 2 is a numerically clean and reproducible study of a defined Gaussian Hermitian toy. Its principal scientific outcome is a limitation: most of its advertised observables are fixed by no data or by two-point information, and the completed inertia analysis did not isolate an additional higher-order signal. The experiment is therefore computationally valid but underpowered for its original higher-order question.**

It must continue to state that none of the work validates the Alpöge–Furman theorem, identifies the toy with Weil’s Hermitian form, or constitutes evidence for or against RH.

---

# 10. Items explicitly deferred beyond this response

The following do not block drafting Report v2 but are not decided or executed here:

1. core-plus-halo validation of \(\mu_4\);
2. exact reproduction of the reviewer’s CUE power calculation;
3. exact reproduction and packaging of DH/Epstein controls;
4. all-zero ordinate-multiset controls;
5. a full complex-zero or Weil-type control;
6. a new Experiment 3 specification;
7. a numerical companion software specification;
8. a publication plan;
9. any novelty search for the fourth-moment observation.

These belong to later closure-package parts or successor work.

---

# 11. Formal disposition summary

| Category | Outcome |
|---|---|
| Original Experiment 2 numerics | **Accepted; independently reproduced** |
| Primary package completeness | **Resolved and checksum-verified** |
| Gaussian bridge derivation | **Accepted** |
| Gaussian bridge interpretation | **Reframed as reconstruction/quadrature** |
| \(D_C\) height sequence | **Accepted; not independent of Level-1 two-point change** |
| Inertia profiles | **Accepted as descriptive properties of the frozen toy** |
| Numerical sign resolution | **Accepted** |
| Kernel dependence | **Accepted** |
| `b_pos` inequality | **Accepted** |
| `b_pos` as discriminator | **Retired** |
| `mu_max` as rigidity proxy | **Withdrawn** |
| Height-control Level-1/Level-2 pattern | **Accepted as suggestive consistency, not universal proof** |
| CUE power table | **Reviewer-generated; deferred/attributed** |
| DH/Epstein controls | **Reviewer-generated; retained with narrow finite-window ordinate-only interpretation** |
| Universal apparatus-blindness claim | **Not accepted** |
| Number-variance arithmetic claim | **Retracted** |
| Thinning confound | **Mathematically confirmed** |
| \(\mu_3\to\mu_4\) correction | **Accepted for the specific spectral-model comparison** |
| Exploratory \(\mu_4\) numerical claim | **Promising but unverified here; future only** |
| Direct Christoffel-to-proportion route | **Closed** |
| Characterization of Experiment 2 | **Computationally valid, structurally underpowered** |
| Experiment 3 status | **Not decided in this response** |

---

# 12. Part 2 completion statement

This document completes **Part 2 — Experiment 2 Peer-Review Response** of the Project Montecito Experiment 2 closure package.

The direct PR-01/PR-02 reconciliation is complete. Every material finding has been:

- accepted;
- accepted with qualification;
- reframed;
- withdrawn;
- closed;
- resolved;
- attributed;
- or deferred.

Targeted closure verification has been performed. The original computation remains valid, while the required interpretive corrections are now fixed for the next document.

The next planned artifact is:

`Experiment2_Report_v2.md`.

No Report v2 rewrite, formal Experiment 2 closure, migration decision, or Experiment 3 execution is performed in this document.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1 | 2 September 2026 | Initial formal reconciliation of PR-01 and PR-02, including targeted mathematical and computational closure rechecks |
