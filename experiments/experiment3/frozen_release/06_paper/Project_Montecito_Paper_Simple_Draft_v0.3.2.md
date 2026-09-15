# A Computational Walk Toward Higher-Order Structure in the Zeta Zeros

## Pair correlation, a first Hermitian instrument, and a bounded sinc-kernel study

### Project Montecito — Simple Paper Draft v0.3.2

**Date:** September 11, 2026  
**Status:** Corrected working draft after independent peer review of the bounded Experiment 3 study  

## Abstract

Project Montecito is a three-stage computational exploration of structure in the ordinates of Riemann-zeta zeros. Experiment 1 measures pair correlation and identifies a pronounced finite-height deformation in the first zeros that is no longer resolved in two much higher samples. Experiment 2 passes the ordinates through a Gaussian Hermitian instrument; the computation is valid, but analysis shows that most of its principal observables contain no more than two-point information. This limitation motivates Experiment 3, a bounded study of sinc-kernel spectral moments. An exact homometric control demonstrates that the fourth moment can distinguish configurations sharing the same unordered pair-distance multiset. In the zeta comparison, the first zeros remain displaced from finite CUE, the sample near zero number \(10^{12}\) lies marginally above the identically windowed CUE ensemble, and the sample near \(10^{21}\) is consistent with it at the resolution of this study. A collision decomposition also shows that much of the raw fourth-moment displacement remains pair-driven. We claim neither a new higher-order law nor evidence for the Riemann Hypothesis. The contribution is the computational journey itself: measuring pair structure, identifying the information ceiling of a first instrument, and testing a more appropriate higher-order-capable observable.

---

# 1. Introduction

The nontrivial zeros of the Riemann zeta function are written

\[
\rho=\beta+i\gamma,
\qquad 0<\beta<1.
\]

The Riemann Hypothesis asserts that every nontrivial zero lies on the critical line

\[
\beta=\frac12.
\]

Project Montecito does not attempt to prove or disprove this statement. Its purpose is computational and exploratory: to examine the local point-process structure of known zero ordinates and to ask what levels of that structure are visible to simple, reproducible spectral instruments.

The project was motivated in part by the 2026 work of Alpöge and Furman, who obtain new unconditional lower bounds for simple critical-line zeros and distinct zeros using a finite compression of Weil's Hermitian form, and by Lamzouri's complementary Hilbert-space proof. Those arguments are arithmetic and theorem-level. Montecito reconstructs neither proof. The point of contact is more modest: both the analytic work and the experiments emphasize the relation among zero geometry, quadratic forms, spectral moments, and the distinction between information available at the two-point level and information requiring higher correlations.

The project proceeds as a computational walk rather than a single numerical claim:

\[
\text{pair correlation}
\longrightarrow
\text{first Hermitian instrument}
\longrightarrow
\text{explicit fourth-moment diagnostic}.
\]

Each stage changes the next one. Experiment 1 establishes the measured two-point baseline. Experiment 2 shows why a mathematically clean apparatus can nevertheless be structurally underpowered. Experiment 3 asks a narrower question with an observable chosen specifically because it can carry higher-order information.

The final paper deliberately reports the corrections as well as the successful computations. Several tempting interpretations disappeared under algebraic analysis or cheap controls. We regard that as part of the result: computational exploration is useful not only when it reveals a new pattern, but also when it identifies which apparently promising patterns contain no new information.

---

# 2. Experiment 1: the pairwise baseline

## 2.1 Data and unfolding

Experiment 1 uses three authoritative numerical samples of zeta zeros:

1. the first 10,000 nontrivial zeros;
2. 10,000 zeros near zero number \(10^{12}\);
3. 10,000 zeros near zero number \(10^{21}\).

The ordinates are unfolded to approximately unit mean density using the smooth zero-counting function. Checksums and process-specific mean-spacing assertions are preserved with the data.

For unfolded positions \(x_i\), the asymptotic GUE pair-correlation density is

\[
R_{\mathrm{GUE}}(u)
=
1-
\left(
\frac{\sin\pi u}{\pi u}
\right)^2.
\]

The principal short-range statistic is the relative deficit of forward pairs below one half of a mean spacing,

\[
D_{0.5}
=
1-
\frac{\text{observed pairs with }0<u<0.5}
{\text{finite-window GUE expectation}}.
\]

## 2.2 Results

For the first 10,000 zeros,

\[
D_{0.5}\approx 0.2240.
\]

Thus the sample contains approximately 22.4% fewer very close pairs than predicted by the asymptotic GUE curve. The qualitative correlation hole is present, but it is wider at low height.

At much greater height, the same statistic becomes

\[
D_{0.5}\approx 0.0162
\qquad\text{near }10^{12},
\]

and

\[
D_{0.5}\approx -0.0367
\qquad\text{near }10^{21}.
\]

The matched finite-GUE calibration has a standard deviation of approximately 0.0248, corresponding to a rough two-standard-deviation scale of 0.05. Both high-height values lie inside that scale. The supported statement is therefore not that the finite-height correction becomes mathematically zero, but that the large low-height deformation is suppressed below the resolution of the experiment at both high heights.

Experiment 1 establishes the first piece of the Montecito hierarchy:

> The measured zeta point process is already strongly repulsive and qualitatively GUE-like, but the first zeros are not interchangeable with an asymptotic sine-process sample. At high height, the measured pair structure becomes much closer to the finite random-matrix benchmark.

---

# 3. Experiment 2: the information ceiling of a first Hermitian instrument

## 3.1 Construction

Experiment 2 uses the Gaussian Gram matrix

\[
C_{ij}
=
\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right]
\]

and the shifted Hermitian family

\[
H_\lambda=I-\lambda C.
\]

The eigenvalues of \(H_\lambda\) are

\[
1-\lambda\mu_j(C),
\]

so a single eigendecomposition of \(C\) determines the full inertia profile across \(\lambda\).

This apparatus was inspired by the broad architecture of a Hermitian-form argument, but it is not a finite Weil-form compression. It receives unfolded ordinates only; it contains no real parts \(\beta\), no prime-side explicit formula, and no arithmetic interpretation of its positive or negative directions.

## 3.2 Numerical validity

The frozen experiment evaluates 2,592 block/parameter cases. All signs are resolved on the frozen grid, direct and spectrum-first calculations agree, and independent reconstruction reproduces the results. The experiment therefore did not fail numerically.

## 3.3 Structural diagnosis

The decisive result came from examining what each observable can contain.

First,

\[
\operatorname{tr}H_\lambda=m(1-\lambda),
\]

which is independent of the point configuration.

Second,

\[
\|H_\lambda\|_F^2
=
m(1-2\lambda)+\lambda^2\|C\|_F^2,
\]

and

\[
\frac{\|C\|_F^2}{m}-1
\]

is a Gaussian-weighted two-point statistic.

Third, the generic positive-inertia bound becomes

\[
b_{\mathrm{pos}}(\lambda)
=
\frac{(1-\lambda)^2}
{(1-2\lambda)+\lambda^2(1+D_C)},
\]

so it depends on the point process only through the same scalar \(D_C\).

The full spectrum can in principle contain higher-order information through terms such as

\[
\operatorname{tr}(C^3),
\qquad
\operatorname{tr}(C^4),
\ldots,
\]

but the completed experiment does not isolate that information from the measured pair-level evolution.

The correct conclusion is therefore:

> Experiment 2 was computationally valid but structurally underpowered for its most ambitious question. Most of its advertised gauges were data-free or two-point-limited by construction.

This diagnosis motivates the next step. The answer is not to make the matrix complicated for its own sake. It is to choose an observable whose information level matches the question.

---

# 4. Experiment 3: a bounded sinc-kernel study

## 4.1 Scope decision

A more extensive version of Experiment 3 was designed and archived for possible future work. The present paper does not depend on that larger program.

For Project Montecito Version 1, we adopt a bounded study that can be run once in a small cloud environment and reported with correspondingly limited claims. No parameter is changed after seeing the output, and no unattractive result triggers a redesigned experiment.

## 4.2 Fixed design

For each of the three 10,000-zero datasets, we use 16 deterministic 512-point windows. In every window, the central 128 points form the measured core and the remaining 192 points on each side form the halo.

The same geometry is applied to:

- 64 independent finite CUE realizations generated by the Killip--Nenciu CMV construction;
- 64 independent fixed-count circular Poisson realizations;
- an integer lattice;
- a six-point homometric pair.

D3 is not accessed.

## 4.3 Sinc-kernel moments

We define

\[
K_{ij}
=
\operatorname{sinc}_\pi(x_i-x_j)
=
\frac{\sin\pi(x_i-x_j)}{\pi(x_i-x_j)},
\qquad K_{ii}=1.
\]

The core-anchored moments are

\[
\widehat\mu_k
=
\frac1{|C|}
\sum_{i\in C}(K^k)_{ii},
\qquad k=2,3,4.
\]

The fourth moment admits the exact anchored collision decomposition

\[
\sum_{i\in C}(K^4)_{ii}
=
|C|
+6S_{2,C}+S_{4,C}
+4T_{3,C}+W_{3,C}^{(0)}+W_{3,C}^{(1)}+Q_{4,C}.
\]

We report both the raw fourth moment and

\[
\widehat\mu_4^{(>2)}
=
\frac{4T_{3,C}+W_{3,C}^{(0)}+W_{3,C}^{(1)}+Q_{4,C}}{|C|},
\]

which removes all one-point and two-distinct-point collision terms. This is a higher-order-capable finite functional, not a connected four-point cumulant.

## 4.4 Exact demonstration that the fourth moment adds information

Before comparing zeta with random-matrix controls, we test whether the chosen fourth moment can in fact see arrangement information absent from an unordered pair-distance multiset. Consider

\[
A=\tfrac12\{0,1,2,6,8,11\},
\qquad
B=\tfrac12\{0,1,6,7,9,11\}.
\]

These two homometric configurations have the same unordered pair-distance multiset. Their normalized sinc moments are

| moment | \(A\) | \(B\) |
|---|---:|---:|
| \(\mu_1\) | 1.0000000000 | 1.0000000000 |
| \(\mu_2\) | 1.3015493260 | 1.3015493260 |
| \(\mu_3\) | 1.9046479780 | 1.9046479780 |
| \(\mu_4\) | 3.0446207814 | 2.9463110767 |

Thus

\[
\mu_4(A)-\mu_4(B)
=
0.0983097048.
\]

This exact finite example is the conceptual control on which Experiment 3 rests: the fourth sinc-kernel moment can distinguish two configurations that every additive functional of their unordered pair-distance multiset treats identically, even though their first three spectral moments agree.

---

# 5. Controls

## 5.1 Lattice normalization

For the integer lattice, every nonzero integer difference is a zero of the normalized sinc function. Hence

\[
K=I
\]

and the computation gives exactly

\[
\mu_2=\mu_3=\mu_4=1,
\qquad
\mu_4^{(>2)}=0.
\]

## 5.2 CUE and Poisson dynamic range

The identically windowed controls give

| process | \(\mu_2\) | \(\mu_3\) | raw \(\mu_4\) | \(\mu_4^{(>2)}\) |
|---|---:|---:|---:|---:|
| CUE mean | 1.32631 | 1.97725 | 3.19307 | 0.12261 |
| Poisson mean | 2.00081 | 5.00389 | 14.67303 | 6.99848 |

The finite CUE values lie slightly below the infinite sine-process targets because the core and halo are finite. Poisson lies far away. The instrument therefore has ample finite-sample dynamic range.

---

# 6. Zeta results

## 6.1 Moment hierarchy across height

| dataset | \(\mu_2\) mean ± SD | \(\mu_3\) mean ± SD | raw \(\mu_4\) mean ± SD | \(\mu_4^{(>2)}\) mean ± SD |
|---|---:|---:|---:|---:|
| first 10,000 | 1.29647 ± 0.01275 | 1.87369 ± 0.04318 | 2.90815 ± 0.11224 | 0.04284 ± 0.03658 |
| near \(10^{12}\) | 1.33700 ± 0.01803 | 2.01188 ± 0.06115 | 3.28254 ± 0.17549 | 0.14073 ± 0.08554 |
| near \(10^{21}\) | 1.33136 ± 0.02919 | 1.99089 ± 0.10169 | 3.21907 ± 0.27180 | 0.11634 ± 0.07782 |
| finite CUE | 1.32631 ± 0.02220 | 1.97725 ± 0.07615 | 3.19307 ± 0.20339 | 0.12261 ± 0.06832 |

The \(\pm\) SD entries in the table describe variation across individual windows. They are not the uncertainty scale of a 16-window dataset mean. We therefore report two descriptive scales below:

1. **individual-window scale:** the zeta--CUE mean difference divided by the standard deviation across individual CUE windows;
2. **16-window-mean scale:** the same difference divided by the standard deviation of 20,000 bootstrap means, each formed from 16 CUE windows.

The second scale is the more relevant calibration for comparing dataset means, but it remains exploratory: the 16 deterministic zeta windows are not asserted to be fully independent, and the bootstrap values are not confirmatory \(p\)-values.

For the first 10,000 zeros, the differences in \(\mu_2\), raw \(\mu_4\), and \(\mu_4^{(>2)}\) are

\[
-0.02984,\qquad -0.28492,\qquad -0.07977.
\]

They correspond to \(-1.34\), \(-1.40\), and \(-1.17\) individual-window standard deviations, but to \(-5.39\), \(-5.62\), and \(-4.72\) bootstrap standard deviations of a 16-window CUE mean. In all three cases the two-sided descriptive tail reached the finite resolution \(1/(20{,}000+1)\). The low-height displacement is therefore clear under the bounded study's descriptive mean calibration.

The sample near zero number \(10^{12}\) lies above the CUE mean for all four displayed moments. For \(\mu_2\), \(\mu_3\), raw \(\mu_4\), and \(\mu_4^{(>2)}\), the differences are \(1.94\), \(1.82\), \(1.77\), and \(1.07\) bootstrap standard deviations of a 16-window CUE mean; the corresponding descriptive tails are approximately \(0.053\), \(0.067\), \(0.079\), and \(0.286\). This is a consistently signed, marginal intermediate-height displacement, not a resolved discovery. The bounded design is not powered to determine whether it persists.

For the sample near zero number \(10^{21}\), the differences from CUE are

\[
\Delta\mu_2=+0.00506,
\qquad
\Delta\mu_4=+0.02601,
\qquad
\Delta\mu_4^{(>2)}=-0.00627.
\]

These are \(0.23\), \(0.13\), and \(-0.09\) individual-window standard deviations and \(0.92\), \(0.51\), and \(-0.37\) bootstrap standard deviations of a 16-window mean. The corresponding descriptive tails are approximately \(0.36\), \(0.61\), and \(0.71\). Within the resolution of this study, the \(10^{21}\) sample is fully consistent with the identically windowed finite CUE ensemble.

The bounded result therefore refines, rather than merely repeats, the finite-height narrative of Experiment 1:

> The first zeros remain distinctly displaced from finite CUE; the \(10^{12}\) sample is marginally high across the moment hierarchy; and the \(10^{21}\) sample is CUE-consistent under the same finite geometry.

## 6.2 How much of the fourth-moment difference is lower-order?

The decomposition

\[
\mu_4
=
1
+
\frac{6S_2+S_4}{|C|}
+
\mu_4^{(>2)}
\]

allows the raw difference from CUE to be separated.

| dataset | raw \(\mu_4\) difference | pair-part difference | \(>2\)-distinct difference |
|---|---:|---:|---:|
| first 10,000 | -0.28492 | -0.20514 | -0.07977 |
| near \(10^{12}\) | +0.08947 | +0.07135 | +0.01812 |
| near \(10^{21}\) | +0.02601 | +0.03227 | -0.00627 |

For the first two rows, 72--80% of the raw displacement is carried by the pair component. Near \(10^{21}\), the pair and collision-reduced differences have opposite signs and mostly cancel.

This is an important restraint on interpretation. The raw fourth moment is higher-order-capable, but most of its observed finite displacement need not be higher-order. The collision decomposition makes that visible.

The all-distinct four-cycle contribution \(Q_4/|C|\) is close to zero for CUE and all three zeta datasets. Most of the reported \(\mu_4^{(>2)}\) therefore comes from three-distinct-index configurations in this finite geometry.

---

# 7. Discussion

## 7.1 What Experiment 3 adds

Experiment 3 does not produce a theorem or a spectacular new numerical constant. Its value is more precise.

First, the homometric control establishes that the chosen fourth moment genuinely has access to arrangement information not fixed by an unordered pair-distance multiset.

Second, the control hierarchy shows that the statistic behaves coherently across maximal regularity, random-matrix repulsion, and independence.

Third, the zeta calculation shows that the finite-height evolution is visible not only in the pair-correlation statistic of Experiment 1, but also in the raw and collision-reduced sinc moments: the first zeros are displaced, the \(10^{12}\) sample is marginally high, and the \(10^{21}\) sample is CUE-consistent.

Fourth, the decomposition shows why a raw fourth moment must not be overinterpreted: lower-order terms still account for most of the finite difference in two of the three zeta regimes.

## 7.2 What Experiment 3 does not add

The bounded design does not include a control process matched to the complete measured pair features of each target. Therefore it cannot establish that the residual \(\mu_4^{(>2)}\) behavior is unexplained by the full two-point law.

It also lacks a complete boundary-convergence study, larger control ensembles, formal power and false-positive calibration, and an independent holdout confirmation.

Accordingly, we do not write:

> Project Montecito discovered new higher-order structure in the zeta zeros.

We write instead:

> Project Montecito constructed and validated a higher-order-capable sinc-kernel statistic, observed a finite-height transition consistent with the random-matrix picture, and identified exactly which stronger attribution question remains open.

## 7.3 Relationship among the three experiments

The experiments are most useful when read as one chain.

Experiment 1 asks:

> What is visible at the pairwise level?

Experiment 2 asks:

> What does a simple Hermitian apparatus retain from that information?

Its answer is that most principal summaries retain only pairwise information.

Experiment 3 asks:

> Can an explicitly higher-order-capable statistic be made numerically meaningful?

Its answer is yes at the level of exact controls and finite descriptive comparison, but the stronger pair-matched attribution question is deferred.

This is a modest conclusion, but it is a coherent one. The project begins with an empirical pair correlation, learns why a first instrument is underpowered, and ends with a statistic whose additional information content is demonstrated exactly on a controlled finite example.

---

# 8. Conclusion

Project Montecito does not advance the proof of the Riemann Hypothesis. It does, however, provide a reproducible computational account of three related questions.

The first 10,000 zeta zeros display a substantial finite-height deformation of the asymptotic GUE pair-correlation curve. In the spectral-moment study, the \(10^{12}\) sample remains marginally above finite CUE, while the \(10^{21}\) sample is fully consistent with the finite random-matrix calibration at the present resolution.

A first Gaussian Hermitian instrument is numerically sound but scientifically limited: its trace is data-free, its Frobenius moment and generic positive-inertia bound are two-point-determined, and its full inertia profile does not isolate a higher-order residual.

A normalized sinc-kernel fourth moment is demonstrably capable of seeing more than an unordered pair-distance multiset. Applied in a bounded finite geometry, it distinguishes lattice, CUE, and Poisson controls and traces the zeta samples from a clear low-height displacement, through a marginal intermediate-height offset, to CUE consistency near zero number \(10^{21}\). Yet the collision decomposition also shows that much of the raw fourth-moment displacement remains lower-order.

The final lesson is methodological:

\[
\boxed{
\text{The information content of an observable must be established before its numerical pattern is interpreted.}
}
\]

That lesson, rather than a claim about RH, is the central contribution of this first paper.

---

# Appendix A. Roadmap for future work

The present paper closes the first computational cycle of Project Montecito. Several natural extensions remain.

**Experiment 1** could be extended to additional heights, larger zero samples, and more detailed models of finite-height convergence.

**Experiment 2** could be revisited using instruments that retain richer arithmetic or complex-zero information, or through comparisons among alternative kernel constructions.

**Experiment 3** could be strengthened through larger control ensembles, additional boundary validation, more stringent lower-order matching, and independent replication.

These directions are not required for the conclusions of the present paper. More detailed designs have been preserved in the Project Montecito research archive and may be reconsidered as separate future work. In particular, a more extensive study of higher-order spectral attribution could form the subject of a separate future paper.

---

# Appendix B. Reproducibility record

The corrected bounded Experiment 3 package contains:

- the pre-result protocol and its SHA-256;
- the three frozen zeta input files and checksums;
- the self-contained execution and aggregation scripts;
- copied sinc-kernel, moment, collision, CUE, Poisson, and input-loading modules;
- all 176 zeta/control endpoint rows and regenerable derived tables;
- both uncertainty-scale records;
- lattice and homometric control records;
- the shipped unit tests and independent brute-force collision validator;
- figures, execution logs, manifest, and checksum file.

The corrected deterministic cloud rerun completed in approximately 37 seconds with a peak resident memory of approximately 0.164 GiB. Its common scientific outputs matched the original release exactly. No D3 data were accessed.

---

# References

- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, 1973.
- A. M. Odlyzko, numerical tables and studies of the zeros of the Riemann zeta function.
- Z. Rudnick and P. Sarnak, work on \(n\)-level correlations of zeros and eigenvalues.
- L. Alpöge and R. Furman, *More than two thirds of the zeta zeros are simple and on the critical line*, arXiv:2608.13637, 2026.
- Y. Lamzouri, *A new proof that more than \(2/3\) of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882, 2026.
- R. Killip and I. Nenciu, matrix models for circular ensembles, 2004.
- F. Mezzadri, methods for generating random matrices from classical compact groups, 2007.
