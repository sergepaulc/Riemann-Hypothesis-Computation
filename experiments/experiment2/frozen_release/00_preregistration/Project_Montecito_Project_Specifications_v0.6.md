# Project Montecito — Project Specifications and Paper Outline — Version 0.6

## Computational Exploration of the Riemann Zeta Function, Pair Correlation, Point Processes, and a Toy Indefinite Hermitian Model

**Version:** 0.6  
**Date:** August 31, 2026

---

# Version 0.6 — Main Design Decisions

Version 0.6 is a **pre-Experiment-2 methodological-hardening release**. It preserves the scientific scope and points-in architecture of Version 0.5, keeps Experiment 1 frozen, and incorporates lessons from Akiva Groskin's recent arXiv preprint on a finite Guinand–Weil dictionary and archimedean-tail ordering. Groskin's paper is treated as **adjacent recent work, not as an independently established theorem on which Montecito depends**. No primary Experiment 2 kernel, bandwidth, block size, or \(\lambda\)-grid is changed by this release.

1. **Points-in remains the primary architecture.** Experiment 1 exports both the unfolded zeta-zero positions and the empirical pair-correlation function. Experiment 2 builds the toy Hermitian matrix from the point configuration itself. The full matrix preserves the labeled arrangement of pairwise relationships, whereas \(\widehat R_2(u)\) is an averaged one-dimensional summary. Accordingly, Version 0.6 replaces the loose phrase “structure beyond pair correlation” with the more precise **“structure beyond the averaged empirical two-point summary.”**

2. **The toy form remains explicitly indefinite.** The reference family is
   \[
   H_\lambda(X)=I-\lambda C(X),
   \]
   where \(C(X)\) is a positive-semidefinite Gaussian-kernel Gram matrix. The shift by \(I\) permits nontrivial inertia while keeping the construction transparent and process-agnostic.

3. **The pair-correlation bridge remains independent of the points-in matrix construction.** The empirical function \(\widehat R_\zeta(u)\) predicts the Frobenius/second-moment contribution of \(C(X)\), while the matrix itself is built directly from the labeled point configuration.

4. **The mathematical observable is inertia; the numerical report distinguishes resolved and unresolved signs.** For an exact Hermitian matrix the target is
   \[
   (n_{\mathrm{pos}},n_{\mathrm{neg}},n_{\mathrm{zero}}).
   \]
   In floating-point computation, Version 0.6 does not automatically equate “near zero” with a true zero. It reports **numerically resolved positive**, **numerically resolved negative**, and **numerically unresolved** eigenvalues, with higher-precision escalation for borderline cases.

5. **The previous eigenvalue tolerance becomes a screening threshold, not a certification theorem.** The scale
   \[
   \varepsilon_{\mathrm{screen}}
   =10^{-10}\max(1,\|H_\lambda\|_2)
   \]
   is retained only to flag borderline eigenvalues. A sign inside this band must be recomputed at higher precision or reported unresolved. Project Montecito does not claim a Groskin-style rigorous \(B_T\) error budget for the toy model.

6. **Experiment 2 becomes spectrum-first.** For each block, diagonalize \(C\) once. If \(\mu_j(C)\) are its eigenvalues, then
   \[
   \eta_j(H_\lambda)=1-\lambda\mu_j(C)
   \]
   exactly, and the sign crossings occur at
   \[
   \lambda_j^{\ast}=\frac{1}{\mu_j(C)}
   \]
   for \(\mu_j(C)>0\). The complete inertia profile over the preregistered \(\lambda\)-grid is derived from these thresholds. Direct diagonalization of selected \(H_\lambda\) matrices is retained as an independent implementation check.

7. **Finite-block dependence is separated from numerical sign uncertainty.** Changing block location or block size changes the matrix being studied; a sign change across two different blocks is therefore a finite-window/scaling observation, not automatically a numerical artifact. Experiment 2 will use preregistered common block centers with nested block sizes where possible and will report this sensitivity explicitly.

8. **The primary Gaussian matrix is not kernel-truncated.** For each finite block, every matrix entry \(C_{ij}=k_\sigma(x_i-x_j)\) is computed. The only relevant \(u\)-truncation is in the Experiment-1 pair-correlation artifact used to predict the Frobenius moment. For \(\sigma=1\), \(U_{\max}=30\), and \(m\le512\), the total contribution of omitted ordered pairs to \(\|C\|_F^2\) is bounded by
   \[
   m(m-1)e^{-900}<4\times10^{-386}.
   \]
   Thus the primary pair-correlation/Frobenius tail is explicitly bounded rather than merely assumed negligible.

9. **Groskin clarifies why the toy is useful, but does not replace it.** Recent work gives a much more faithful finite Galerkin realization of the Weil quadratic form. Therefore Montecito should not motivate \(H_\lambda\) by claiming that finite Weil-form matrices are computationally inaccessible. The correct rationale is that the toy provides one unchanged, transparent map
   \[
   X\longmapsto C(X)\longmapsto H_\lambda(X)
   \]
   for zeta, GUE, Poisson, lattice, and other non-arithmetic control processes.

10. **Groskin's archimedean-tail pathology is not assumed to be Montecito's pathology.** Groskin studies a finite-cutoff approximation \(Q_T\) to a distinct cutoff-free target \(Q_\infty\). Our finite-block \(H_\lambda(X)\) is itself the defined object; it has no hidden archimedean tail. The transferable lesson is methodological: distinguish properties of the defined matrix, numerical rounding error, and dependence on finite-window choices.

11. **Experiment 1 remains frozen.** The first \(10{,}000\) zeros remain the primary Experiment 2 input. The near-\(10^{12}\) and near-\(10^{21}\) samples remain secondary zeta controls and may not silently replace the frozen primary input.

12. **Dense \(10{,}000\times10{,}000\) eigendecompositions remain out of scope.** Experiments 2–3 use controlled local blocks of sizes \(128,256,512\).

13. **The scientific scope remains Experiments 1–3.** The removed square-root-cancellation and standalone “67% is not RH” workstreams remain outside the project.

14. **The Alpöge–Furman v2 alignment is unchanged.** Project Montecito remains a computational toy exploration, not a numerical reconstruction of their proof or of Groskin's finite Weil-form construction.

# Alignment with Alpöge–Furman arXiv v2

## Primary reference

Levent Alpöge and Ralph Furman, **“More than two thirds of the zeta zeros are simple and on the critical line,”** arXiv:2608.13637v2 [math.NT], last revised August 19, 2026.

## Precise theorem being used as context

The current paper proves unconditionally, on dyadic height intervals,

\[
N_0^s(T,2T)
\ge
\left(\frac23-o(1)\right)N(T,2T),
\]

where \(N_0^s\) counts **simple zeros on the critical line**. It also proves

\[
N_d(T,2T)
\ge
\left(\frac56-o(1)\right)N(T,2T),
\]

where \(N_d\) counts distinct zeros. With the Montgomery–Taylor window, the constants improve to approximately

\[
0.67250
\qquad\text{and}\qquad
0.83625,
\]

respectively.

Therefore, when this specification informally refers to the “67.25% result,” it means the stronger statement that approximately **67.25% of the zeros are proved simple and on the critical line**, not merely that 67.25% lie on the line.

## Actual proof skeleton

The paper compresses Weil's Hermitian form to a finite-dimensional real symmetric matrix \(\widetilde G\). Up to a negligible tail, the zero-side structure is organized schematically as

\[
\widetilde G=P+Q.
\]

The roles of the two pieces are qualitatively different:

- each distinct zero on the critical line contributes a positive rank-one form to \(P\);
- each symmetric off-line pair contributes to \(Q\) with signature \((1,1)\), handled through Sylvester's law of inertia.

The prime-side calculation gives a second-moment identity of the form

\[
\|\widetilde G\|_{\mathrm{HS}}^2
=
(R(\psi)+o(1))N,
\]

with \(R(\psi_0)=4/3\) for the indicator window and the Montgomery–Taylor window giving the optimized constant. A specialized rank–trace/inertia inequality then converts the trace, Hilbert–Schmidt second moment, and off-line positive index into lower bounds for simple critical-line zeros and distinct zeros.

This is the real mathematical architecture to which Project Montecito is only **conceptually analogous**.

## Important distinction from Experiment 1

Experiment 1 measures the empirical local pair-correlation curve of a finite set of actual zeta zeros. That is **not** the same object as numerically evaluating the paper's analytic prime-side second moment. In Alpöge–Furman, the relevant Hilbert–Schmidt second moment is obtained unconditionally through the explicit formula and prime-side analysis; its zero-side reading is related to a smoothed Fejér-kernel sum over zero differences.

Accordingly, Experiment 1 is a computational study of established zeta/GUE statistics and a source of point-process data for our toy apparatus. It does **not** numerically verify the analytic input to the Alpöge–Furman theorem.

## Limits of the paper's method and limits of our experiment

Alpöge–Furman show that the optimized \(0.67250\ldots\) result is already close to the ceiling of the bandwidth-one, first-two-moment certificate framework; the broader bandwidth-one ceiling is approximately \(0.682\). The paper explains that moving substantially beyond this regime would require new information, such as pair-correlation input beyond Fourier support \([-1,1]\), prime-pair information, or usable higher moments.

**Experiment 3 does not attempt to reproduce, test, or break that \(0.682\) ceiling.** It asks a different and simpler computational question: how does a fixed toy Hermitian inertia profile respond when its input point process is changed from zeta to synthetic GUE, Poisson, lattice, or intermediate models?

---

# Adjacent Finite Weil-Form Work — Groskin arXiv:2607.02828v3

## Reference and status

Akiva Groskin, **“A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3 [math.NT], revised August 14, 2026.

This is a recent arXiv preprint. Version 0.6 treats its main theorems as **important adjacent claims that appear mathematically serious but are not yet independently established background for Project Montecito**. Experiment 2 must remain valid even if later review modifies one of Groskin's claims.

## Relevance to Montecito

Groskin studies a Connes–van Suijlekom / Connes–Consani–Moscovici finite Galerkin truncation of the Weil quadratic form, not Alpöge–Furman's finite compression and not Montecito's Gaussian toy.

The preprint claims two results of particular methodological interest:

1. a finite dictionary sending Galerkin coefficient vectors to admissible band-limited Guinand–Weil test functions, giving an exact zero-sum representation of finite quadratic values;
2. a positive archimedean tail order, together with a cutoff error budget that distinguishes finite-cutoff positivity, certified negativity beyond the budget, and an inconclusive band.

The second result was motivated by a correction to earlier finite-cutoff computations in which apparent negative eigenvalues did not persist for the cutoff-free form. Project Montecito does **not** inherit that exact truncation problem: our finite-block matrix is the object we define, rather than an approximation to a hidden cutoff-free Gaussian matrix. We nevertheless adopt the broader numerical lesson that a floating-point sign threshold is not by itself a model-error or truncation-error bound.

## Why Montecito deliberately keeps the simpler apparatus

A more faithful finite Weil-form matrix would be preferable if the objective were to approximate Weil's form as closely as possible. That is not the primary Montecito question. Experiments 2–3 require a common apparatus that accepts arbitrary point processes without introducing zeta-specific prime, pole, or archimedean terms. Therefore the Gaussian points-in family remains the primary design.

The paper should state this positively: **the toy is chosen for controlled cross-process comparability, not because finite Weil-form matrices are inaccessible.**

If a separate faithful Weil-form implementation is developed later, Groskin's shipped formulas, code, and finite-dictionary checks may provide a useful external validation target. Such a comparison would be a secondary faithful-vs-toy study and is **not** part of the primary Experiment 2 deliverable in Version 0.6.

---

# Project Goal

The goal of this project is **not to prove the Riemann Hypothesis and not to validate the recent Alpöge–Furman theorem that approximately 67.25% of the zeros are simple and on the critical line**.

The goal is to build a reproducible computational framework that helps us explore four questions:

1. What does the pair-correlation structure of actual zeta zeros look like numerically?
2. Can that same zero configuration drive a simple indefinite Hermitian model whose inertia and spectral moments are mathematically interpretable?
3. What changes when the zeta point configuration is replaced by synthetic GUE, Poisson, lattice, and intermediate point processes while the apparatus remains fixed?
4. How much of the toy model's second-moment behavior is explained by pair correlation alone, and how much of its full inertia profile may reflect structure beyond the averaged empirical two-point summary?

The distinction between positive-density critical-line results and the full Riemann Hypothesis remains part of the paper's introductory and mathematical framing, but it is not a separate project section or experiment.

The project should remain mathematically modest, experimentally rigorous, reproducible, and explicit about the distinction between established mathematics and toy modeling.

---

# Architecture at a Glance

## Experiment 1

\[
\text{actual zeta zeros}
\longrightarrow
\begin{cases}
\text{unfolded positions }X_\zeta=\{x_i\}\\
\text{empirical pair correlation }\widehat R_\zeta(u)
\end{cases}
\]

## Experiment 2

Primary path:

\[
X_\zeta
\longrightarrow
C(X_\zeta)
\longrightarrow
H_\lambda(X_\zeta)
\longrightarrow
\text{inertia + trace + Frobenius + bounds}
\]

Independent pair-correlation bridge:

\[
\widehat R_\zeta(u)
\longrightarrow
\text{predicted second moment}
\longleftrightarrow
\text{measured }\|C(X_\zeta)\|_F^2
\]

## Experiment 3

Keep the construction fixed and replace only the point process:

\[
X_\zeta,\quad X_{\mathrm{GUE}},\quad X_{\mathrm{Poisson}},\quad X_{\mathrm{lattice}}
\]

For each process, compute both its pair correlation and its toy-model inertia profile.

The most important consistency check becomes:

\[
\text{actual zeta}
\quad\text{vs}\quad
\text{synthetic GUE}
\]

at **two levels**:

1. pair-correlation agreement;
2. Hermitian-inertia-profile agreement.

Agreement at level 1 but disagreement at level 2 would be especially interesting because the points-in architecture can, in principle, respond to structure beyond the averaged empirical two-point summary.

---

# Part I — Experimental Project Specifications

# Experiment 1 — Measure Pair Correlation from Actual Zeta Zeros

## Objective

Use approximately **10,000 actual nontrivial zeros of the Riemann zeta function** to construct:

1. a trusted unfolded point configuration
   \[
   X_\zeta=\{x_1,\ldots,x_N\},
   \]
2. an empirical normalized pair-correlation function
   \[
   \widehat R_\zeta(u).
   \]

The measured pair correlation should be compared with the Montgomery/GUE prediction

\[
R_{\mathrm{GUE}}(u)
=
1-\left(\frac{\sin(\pi u)}{\pi u}\right)^2.
\]

## Data Source

### Primary source

Use a **precomputed authoritative zero table** rather than computing 10,000 zeros individually.

Preferred primary source:

- Andrew Odlyzko's table of the first 100,000 zeta zeros.

Use the first 10,000 entries for the baseline experiment.

### Validation

Spot-check a small preregistered subset of zeros against:

- LMFDB values; and/or
- high-precision `mpmath.zetazero` evaluations.

The spot check validates ingestion and indexing. It is not used to regenerate the complete dataset.

## Unfolding

Write the zeros as

\[
\rho_n=\frac12+i\gamma_n.
\]

Use the smooth Riemann–von Mangoldt counting approximation

\[
\overline N(T)
=
\frac{T}{2\pi}\log\left(\frac{T}{2\pi}\right)
-
\frac{T}{2\pi}
+
\frac78
\]

and define the unfolded positions

\[
x_n=\overline N(\gamma_n).
\]

After unfolding, the local mean spacing is approximately 1.

The exact unfolding convention must be frozen before the final run and documented in the paper.

## Pair-Correlation Estimator

Estimate pair correlation using only pair differences within a finite window

\[
0<|x_i-x_j|\le U_{\max}.
\]

Primary window:

\[
U_{\max}=30.
\]

Use a standard edge-corrected estimator normalized so that a unit-rate Poisson point process gives a flat baseline near

\[
R_2(u)=1.
\]

The estimator must pass this Poisson unit test before being applied to zeta zeros.

Primary implementation should use sorted points plus a moving-window/two-pointer or binary-search strategy. The effective cost is approximately proportional to the number of points times the number of neighbors inside the window, not all \(N^2\) pairs.

## Outputs

- raw zero table used;
- validation report;
- unfolded positions \(X_\zeta\);
- empirical pair-correlation estimate \(\widehat R_\zeta(u)\);
- fixed numerical grid for \(u\);
- finite-sample uncertainty estimate;
- GUE comparison plot;
- Poisson-estimator unit test;
- machine-readable artifacts:
  - `zeta_unfolded_points.csv`
  - `zeta_pair_correlation.csv`
  - metadata/configuration file.

## Success Criterion

Experiment 1 succeeds if:

1. the estimator reproduces the Poisson baseline on synthetic Poisson data;
2. the zeta data show the expected short-range suppression/level repulsion and qualitative agreement with the Montgomery/GUE curve;
3. the result is stable under reasonable changes in binning/smoothing and sample subwindows;
4. the unfolded points and pair-correlation artifact are reproducible and ready for Experiment 2.

## Risks

Primary risks are:

- unfolding mistakes;
- edge-correction mistakes;
- finite-sample noise;
- estimator sensitivity to bin width or smoothing;
- indexing or parsing errors in the zero table.

The computational cost of pair differences is **not** considered a major risk once the finite pair window is used.

---

# Experiment 2 — Build and Calibrate an Indefinite Hermitian Apparatus

## Purpose

Experiment 2 is the **apparatus** required for Experiment 3.

It is not the finite compression of Weil's Hermitian form used by Alpöge–Furman, and it is not the finite Galerkin Weil-form construction analyzed in Groskin's recent preprint. It does not attempt to reproduce either proof architecture.

Its purpose is narrower:

> Build a simple finite Hermitian family whose inertia responds to the geometry of a point configuration, while its Frobenius second moment can be connected directly to an averaged empirical two-point statistic.

The apparatus is deliberately process-agnostic. The same construction must accept actual zeta points, synthetic GUE points, Poisson points, and lattice points without adding zeta-specific arithmetic terms.

## Architecture Decision: Points-In

The primary input to Experiment 2 is the unfolded point configuration

\[
X=\{x_1,\ldots,x_m\}.
\]

The empirical pair-correlation function is **not** the sole input to the matrix.

This is deliberate. The matrix retains the labeled collection of all pairwise kernel relationships, while \(\widehat R_2(u)\) averages pair separations into a one-dimensional summary. The later zeta-versus-GUE comparison therefore asks whether the fixed matrix apparatus distinguishes configurations whose **averaged empirical two-point summaries** are already similar at the measured scale.

The measured pair correlation remains important as an **independent predictor of the matrix's second moment**.

---

## Frozen Primary and Secondary Zeta Inputs

The primary Experiment 2 zeta input is the frozen unfolded first-\(10{,}000\) point configuration from Experiment 1.

The high-height samples near zero numbers \(10^{12}\) and \(10^{21}\) are secondary controls. They may be used to distinguish properties of the particular low-height frozen point set from properties observed in zeta samples that are already within the matched-GUE range at Experiment 1's resolution.

The primary input may not be replaced post hoc because a secondary sample produces a more interesting matrix profile.

---

## Reference Design

### Step 1 — Fixed positive-definite kernel

Use the Gaussian kernel

\[
k_\sigma(u)
=
\exp\left(-\frac{u^2}{2\sigma^2}\right).
\]

Primary bandwidth:

\[
\sigma=1,
\]

because the points have already been unfolded to mean spacing 1.

For a block \(X=\{x_1,\ldots,x_m\}\), define the full dense Gram matrix

\[
C_{ij}=k_\sigma(x_i-x_j).
\]

No kernel-support cutoff is used in the primary matrix construction.

The Gaussian kernel is positive definite, so

\[
C\succeq0.
\]

Also,

\[
C_{ii}=1,
\qquad
\operatorname{tr}(C)=m.
\]

### Step 2 — Make the form explicitly indefinite

Define the one-parameter Hermitian family

\[
H_\lambda(X)=I-\lambda C(X).
\]

The preregistered grid remains

\[
\Lambda=\{0.10,0.15,0.20,\ldots,0.95\}.
\]

The main observable is the **inertia profile as a function of \(\lambda\)** rather than one selected value.

This is one transparent toy choice, not the “true” Hermitian model behind the zeta theorem.

### Step 3 — Spectrum-first inertia map

Let

\[
\mu_1(C),\ldots,\mu_m(C)\ge0
\]

be the eigenvalues of \(C\). Then

\[
\eta_j(H_\lambda)=1-\lambda\mu_j(C).
\]

Therefore one eigendecomposition of \(C\) determines the complete \(H_\lambda\) spectrum over the entire \(\lambda\)-grid. For every \(\mu_j(C)>0\), the exact crossing threshold is

\[
\lambda_j^{\ast}=\frac{1}{\mu_j(C)}.
\]

Primary implementation rule:

1. diagonalize \(C\) once per block;
2. store the ordered \(\mu_j(C)\) and all crossing thresholds in the experiment artifact;
3. derive the inertia profile from \(1-\lambda\mu_j(C)\);
4. directly diagonalize selected \(H_\lambda\) matrices as an independent verification route.

This makes the inertia flow auditable rather than treating each \(\lambda\) as an unrelated numerical eigendecomposition.

---

# Experiment 2 Observables and Numerical Sign Resolution

For an exact Hermitian matrix, define the mathematical inertia

\[
\operatorname{Inertia}(H_\lambda)
=
(n_{\mathrm{pos}},n_{\mathrm{neg}},n_{\mathrm{zero}}).
\]

In floating-point computation, however, Version 0.6 reports three numerical categories:

- \(n_{\mathrm{pos}}^{\mathrm{res}}\): numerically resolved positive eigenvalues;
- \(n_{\mathrm{neg}}^{\mathrm{res}}\): numerically resolved negative eigenvalues;
- \(n_{\mathrm{unres}}\): eigenvalues whose sign is not numerically resolved at the current precision.

Use the screening scale

\[
\varepsilon_{\mathrm{screen}}
=
10^{-10}\max(1,\|H_\lambda\|_2).
\]

This is **not** called a rigorous certification bound. It is only a trigger for additional computation.

For the spectrum-first route define

\[
r_j(\lambda)=1-\lambda\mu_j(C).
\]

Classification procedure:

1. if \(|r_j(\lambda)|>\varepsilon_{\mathrm{screen}}\), assign the floating-point sign provisionally;
2. if \(|r_j(\lambda)|\le\varepsilon_{\mathrm{screen}}\), recompute the relevant eigenvalue/crossing at substantially higher precision;
3. increase precision until the sign is stable with a documented margin or until the case is declared numerically unresolved;
4. do not convert an unresolved value into a numerical zero merely to complete the inertia count.

When \(n_{\mathrm{unres}}>0\), report interval-valued sign counts:

\[
n_{\mathrm{pos}}\in
[n_{\mathrm{pos}}^{\mathrm{res}},
 n_{\mathrm{pos}}^{\mathrm{res}}+n_{\mathrm{unres}}],
\]

\[
n_{\mathrm{neg}}\in
[n_{\mathrm{neg}}^{\mathrm{res}},
 n_{\mathrm{neg}}^{\mathrm{res}}+n_{\mathrm{unres}}].
\]

If interval arithmetic is later introduced, the terminology may be upgraded to mathematically certified signs. Without it, use **resolved/unresolved**, not **certified/uncertified**.

Normalized reporting quantities are

\[
p_{\mathrm{pos}}^{\mathrm{res}}(\lambda)
=
\frac{n_{\mathrm{pos}}^{\mathrm{res}}}{m},
\qquad
p_{\mathrm{neg}}^{\mathrm{res}}(\lambda)
=
\frac{n_{\mathrm{neg}}^{\mathrm{res}}}{m},
\qquad
p_{\mathrm{unres}}(\lambda)
=
\frac{n_{\mathrm{unres}}}{m}.
\]

Ordinary rank remains conceptually distinct from positive inertia.

---

# Trace and Frobenius Structure

Because \(\operatorname{tr}(C)=m\),

\[
\operatorname{tr}(H_\lambda)
=
m(1-\lambda).
\]

For the preregistered range \(\lambda<1\), the trace is positive.

Also,

\[
\|H_\lambda\|_F^2
=
\|I-\lambda C\|_F^2
=
m(1-2\lambda)
+
\lambda^2\|C\|_F^2.
\]

And

\[
\|C\|_F^2
=
\sum_{i,j}k_\sigma(x_i-x_j)^2.
\]

These identities are exact for the defined finite matrix and serve as implementation checks.

---

# A Valid Positive-Inertia Bound

Let the positive eigenvalues of an exact Hermitian matrix \(H\) be \(\alpha_1,\ldots,\alpha_{n_{\mathrm{pos}}}\). If

\[
\operatorname{tr}(H)>0,
\]

then

\[
\sum_{j=1}^{n_{\mathrm{pos}}}\alpha_j
\ge
\operatorname{tr}(H).
\]

By Cauchy–Schwarz,

\[
\left(
\sum_{j=1}^{n_{\mathrm{pos}}}\alpha_j
\right)^2
\le
n_{\mathrm{pos}}
\sum_{j=1}^{n_{\mathrm{pos}}}\alpha_j^2
\le
n_{\mathrm{pos}}\|H\|_F^2.
\]

Therefore

\[
n_{\mathrm{pos}}(H)
\ge
\frac{\operatorname{tr}(H)^2}{\|H\|_F^2}.
\]

This is the sign-specific inequality used in the toy experiment. It is not Alpöge–Furman's Lemma 3.2 and is not derived from Groskin's tail-order theorem.

Define

\[
b_{\mathrm{pos}}(\lambda)
=
\frac{1}{m}
\frac{\operatorname{tr}(H_\lambda)^2}{\|H_\lambda\|_F^2}.
\]

When all signs are numerically resolved, compare \(b_{\mathrm{pos}}\) with the observed positive fraction. When unresolved signs remain, compare the bound with the reported interval for the positive fraction rather than forcing a single count.

---

# Pair-Correlation Bridge and Explicit Tail Budget

For the kernel matrix,

\[
\|C\|_F^2
=
m
+
\sum_{i\ne j}k_\sigma(x_i-x_j)^2.
\]

For a long, approximately stationary, unfolded unit-density process with signed two-point density \(R_2(u)\),

\[
\frac{1}{m}\|C\|_F^2
\approx
1+
\int_{\mathbb R}k_\sigma(u)^2R_2(u)\,du.
\]

Because Experiment 1 stores the positive-separation version of the empirical pair correlation and the Gaussian kernel is even, the equivalent positive-side convention is

\[
\frac{1}{m}\|C\|_F^2
\approx
1+
2\int_0^\infty k_\sigma(u)^2R_2(u)\,du.
\]

The primary finite-sample prediction must use the same translation-edge convention as Experiment 1 rather than relying only on this asymptotic display.

Experiment 1 stores \(\widehat R_2(u)\) to

\[
U_{\max}=30.
\]

For the primary kernel \(\sigma=1\),

\[
k_1(u)^2=e^{-u^2}.
\]

For every omitted ordered pair with \(|u|>30\),

\[
k_1(u)^2\le e^{-900}.
\]

Hence for \(m\le512\),

\[
\sum_{\substack{i\ne j\\|x_i-x_j|>30}}
k_1(x_i-x_j)^2
\le
m(m-1)e^{-900}
<4\times10^{-386}.
\]

Thus the primary \(U_{\max}=30\) tail is rigorously negligible relative to double precision. Robustness kernels \(\sigma=0.5\) and \(\sigma=2\), if used later, must record their own corresponding tail budgets.

Experiment 2 therefore makes two distinct measurements:

1. **points-in measurement**
   \[
   \|C(X)\|_F^2;
   \]

2. **pair-correlation prediction**
   \[
   \widehat R_2(u)
   \longrightarrow
   \widehat{\|C\|_F^2}.
   \]

Agreement between them is an internal consistency check and a direct Experiment 1 \(\rightarrow\) Experiment 2 bridge.

---

# Matrix Size, Block Design, and Finite-Window Stability

Do **not** construct or diagonalize a dense \(10{,}000\times10{,}000\) matrix.

Use local contiguous blocks of the unfolded point process.

Primary block sizes remain

\[
m\in\{128,256,512\}.
\]

Use multiple preregistered common locations across the frozen \(10{,}000\)-point sequence. The baseline remains approximately 16 locations where possible.

Version 0.6 adds a **nested-location preference**: block sizes \(128,256,512\) should be centered on the same preregistered locations whenever boundaries permit. The exact indices must be written to a configuration file before the Experiment 2 spectra are examined.

This enables two different sensitivity questions to be kept separate:

- **location sensitivity:** same block size at different positions in the point process;
- **scale sensitivity:** nested block sizes around the same location.

A change in inertia across these different matrices is a finite-window/scaling observation, not automatically a floating-point failure. Numerical sign uncertainty is handled separately by the resolved/unresolved protocol above.

---

# Experiment 2 Development Stages

## Stage A — Mathematical and numerical pre-registration

No coding time box.

Before implementation, freeze:

- points-in architecture;
- Gaussian kernel and primary \(\sigma=1\);
- \(\lambda\)-grid;
- block sizes and common block-center rule;
- spectrum-first computation from \(C\);
- screening threshold and high-precision escalation rule;
- resolved/unresolved reporting convention;
- sign-specific positive-inertia bound;
- finite-window pair-correlation/Frobenius prediction;
- explicit Gaussian tail budget;
- primary first-\(10{,}000\) zeta input and secondary high-height-control status.

## Stage B — Baseline implementation

Time-box the initial implementation to approximately **2–4 hours**.

The baseline implementation succeeds if:

- unit tests pass;
- \(C\) and \(H_\lambda\) are Hermitian to numerical precision;
- \(C\) is PSD to the numerical resolution expected from the eigensolver;
- the spectrum-first identity \(\eta_j(H_\lambda)=1-\lambda\mu_j(C)\) agrees with direct selected \(H_\lambda\) eigendecompositions;
- trace and Frobenius identities agree with direct calculations;
- the pair-correlation-predicted and points-measured Frobenius terms agree within the finite-sample uncertainty budget;
- the code emits crossing thresholds and flags borderline signs rather than hiding them.

If these fail, stop and diagnose rather than tuning the model to obtain a desired result.

## Stage C — Numerical-resolution and finite-window audit

Before interpreting the inertia profile:

- rerun every borderline crossing at higher precision;
- record all remaining unresolved signs explicitly;
- compare nested block sizes at common locations;
- compare common block sizes across preregistered locations;
- verify that changing numerical precision does not alter resolved signs away from crossing neighborhoods;
- verify and archive the analytic Gaussian-tail bound;
- distinguish any block-size/location effect from numerical sign uncertainty in the report.

Experiment 2 is considered scientifically ready for Experiment 3 only after Stage C is complete.

# Experiment 3 — Controlled Point-Process Replacement

## Objective

Keep every Experiment 2 choice fixed and replace only the point process.

Compare:

1. actual unfolded zeta zeros;
2. synthetic GUE point configurations;
3. Poisson point configurations;
4. lattice point configurations.

Optional later extensions:

- perturbed lattice;
- intermediate repulsion models;
- tunable \(\beta\)-ensembles.

---

# Synthetic Inputs

## A. Synthetic GUE

Generate eigenvalues from complex Hermitian Gaussian random matrices.

Use bulk eigenvalues only and unfold them to unit mean spacing before entering the Experiment 2 apparatus.

Synthetic matrix sizes and extraction windows should be chosen to provide point blocks comparable to

\[
m\in\{128,256,512\}.
\]

The synthetic generator is validated by reproducing the expected GUE pair-correlation behavior.

## B. Poisson

Generate a unit-rate Poisson process, equivalently exponential nearest-neighbor spacings with mean 1.

## C. Lattice

Use

\[
x_j=j+\phi,
\]

where a fixed or randomly seeded phase \(\phi\) may be used without affecting spacings.

The lattice represents maximal regularity rather than randomness.

---

# Experiment 3 Consistency Checks

## Level 1 — Pair Correlation

Compare

\[
\widehat R_\zeta(u)
\quad\text{and}\quad
\widehat R_{\mathrm{GUE}}(u).
\]

They should show similar local two-point behavior within finite-sample uncertainty.

## Level 2 — Inertia Profile

Compare

\[
p_{\mathrm{pos}}^{\zeta}(\lambda)
\quad\text{and}\quad
p_{\mathrm{pos}}^{\mathrm{GUE}}(\lambda)
\]

and similarly the resolved/interval-aware negative and unresolved fractions, together with \(b_{\mathrm{pos}}\).

This check is genuinely nontrivial because the apparatus ingests point configurations, not only their pair-correlation functions.

Possible outcomes:

- **Pair correlation and inertia both agree:** the toy apparatus sees zeta and GUE similarly at the measured scales.
- **Pair correlation agrees but inertia differs:** the apparatus may be responding to finite-sample effects or to the labeled arrangement of pairwise relationships that is not retained by the averaged empirical two-point summary.
- **Pair correlation already differs materially:** first diagnose unfolding, estimator, or finite-size GUE generation before interpreting inertia.
- **All processes produce similar inertia:** the toy apparatus may be too insensitive.
- **Poisson or lattice produces stronger apparent positivity:** the toy observable measures something different from the initial intuition; this is a valid negative/redirecting result.

---

# Experiment 3 Metrics

For every process and block size report:

- empirical pair-correlation curve;
- \(p_{\mathrm{pos}}(\lambda)\);
- \(p_{\mathrm{neg}}(\lambda)\);
- \(p_{\mathrm{unres}}(\lambda)\), with mathematical zeros reported separately if genuinely identified;
- \(b_{\mathrm{pos}}(\lambda)\);
- \(\|C\|_F^2/m\);
- pair-correlation-predicted \(\|C\|_F^2/m\);
- eigenvalue distribution of \(C\) and crossing thresholds \(1/\mu_j(C)\);
- eigenvalue distribution of \(H_\lambda\).

Across repeated blocks/replicates report uncertainty intervals.

Possible scalar curve-comparison summaries may include preregistered integrated distances, but plots and full profiles remain primary.

No numerical ordering among GUE, Poisson, lattice, and zeta is assumed in advance.

---

# Reference-Design Sensitivity

The primary apparatus uses the Gaussian kernel with \(\sigma=1\).

After the main analysis is frozen and completed, optional robustness checks may use:

\[
\sigma\in\{0.5,2\}.
\]

A sinc kernel

\[
k(u)=\frac{\sin(\pi u)}{\pi u}
\]

may be studied as a **secondary sensitivity experiment**, not as the primary design, because it is especially tied to GUE/sine-kernel mathematics and could bias interpretation toward that structure.

No robustness result may replace the preregistered primary analysis merely because it looks more interesting.

---

# Computational and Resource Constraints

## Core execution model

Experiments 1–3 use a **single controlled Python codebase**.

No multi-agent architecture is required.

LLMs may assist with:

- code generation;
- code review;
- mathematical explanation;
- test design;
- interpretation checks;
- literature review.

Numerical experiments themselves run in ordinary Python/NumPy/SciPy code.

## No open-ended autonomous loops

The project must not depend on an LLM autonomously searching indefinitely.

Each computational run has:

- a predefined input;
- a defined output;
- a fixed parameter set;
- a bounded numerical workload.

## Subscription and vendor limits

Do not hard-code a vendor-specific subscription limit into the scientific specification.

If ChatGPT, Claude Code, Codex, or another coding assistant is used during implementation, record the actual usage constraints in the execution log at that time.

The scientific design must remain executable without requiring long-running multi-agent inference.

## Hardware discipline

Target a modern laptop-class machine.

Avoid:

- dense 10,000-dimensional eigendecompositions;
- unnecessary recomputation of zeta zeros;
- brute-force all-pairs calculations without windows;
- synthetic 10,000-dimensional GUE matrices.

Use blocks, vectorized numerical code, and fixed seeds.

---

# Reproducibility Requirements

All experiments must record:

- Python version;
- package versions;
- zero-table source and checksum;
- raw-data preservation;
- unfolding convention;
- pair-correlation estimator;
- window and smoothing parameters;
- kernel and bandwidth;
- \(\lambda\)-grid;
- block-selection rule;
- eigenvalue screening threshold;
- high-precision escalation settings and unresolved-sign log;
- stored eigenvalues of \(C\) and crossing thresholds \(1/\mu_j(C)\);
- common block-center/nesting rule;
- analytic kernel-tail budget for the pair-correlation/Frobenius bridge;
- random seeds;
- synthetic-process generator settings;
- all figures generated from source data;
- no manually edited numerical results.

Suggested structure:

```text
riemann-experiments/
│
├── README.md
├── pyproject.toml
├── environment/
│   └── lockfile-or-requirements.txt
│
├── data/
│   ├── raw/
│   │   └── odlyzko/
│   ├── processed/
│   │   ├── zeta_unfolded_points.csv
│   │   └── zeta_pair_correlation.csv
│   └── checksums/
│
├── src/
│   ├── zeros.py
│   ├── unfold.py
│   ├── pair_correlation.py
│   ├── point_processes.py
│   ├── hermitian_toy.py
│   ├── inertia.py
│   ├── spectrum_audit.py
│   └── metrics.py
│
├── experiments/
│   ├── exp1_pair_correlation/
│   ├── exp2_hermitian_apparatus/
│   └── exp3_point_processes/
│
├── tests/
│
├── figures/
│
└── paper/
    ├── manuscript.tex
    └── references.bib
```

---

# Research Integrity Rules

Throughout the project distinguish explicitly between:

**Established theorem**  
A result already proved in the mathematical literature.

**Numerical reproduction**  
A computational reproduction of an established phenomenon.

**Toy model**  
A deliberately simplified construction used to isolate one mechanism.

**Computational observation**  
A pattern observed experimentally but not proved.

**Conjecture or hypothesis**  
A proposed explanation requiring further mathematical work.

The following statements must remain explicit:

- Experiment 1 does not verify RH; it numerically illustrates known zero statistics.
- Experiments 2–3 do not reproduce the Weil/Bombieri form.
- The family \(H_\lambda=I-\lambda C\) is a reference toy construction, not the finite compression of Weil's Hermitian form used by Alpöge–Furman.
- A similarity between zeta and synthetic GUE in the toy apparatus is not evidence that RH is true.
- No observation from Experiments 2–3 is evidence for a proof of RH or validation of the Alpöge–Furman two-thirds / 0.67250 theorem.
- A null or negative result is an acceptable scientific outcome.
- A sign change across different finite blocks is not automatically called a truncation artifact; it may reflect finite-window dependence of the defined toy matrix.
- A numerically unresolved eigenvalue is not forced into the zero category.
- Project Montecito claims no Groskin-style rigorous \(B_T\) certification bound for \(H_\lambda\).
- Groskin arXiv:2607.02828v3 is cited as recent adjacent preprint work, not as independently established theorem-level background.
- The toy apparatus is chosen for process-agnostic cross-comparison, not because finite Weil-form matrices are assumed computationally inaccessible.

---

# Part II — Proposed Paper Outline

# Working Title

Primary working title:

**Point Processes, Pair Correlation, and Hermitian Inertia: Computational Experiments with Riemann Zeta Zeros**

Alternative:

**From Zeta-Zero Pair Correlation to Hermitian Inertia: A Reproducible Computational Exploration**

Do not use a title implying new progress on RH unless the results genuinely justify such language.

---

# Abstract

The abstract should state:

- motivation from RH and the Alpöge–Furman result proving at least two thirds of the zeros simple and on the critical line (optimized to approximately 0.67250), together with at least five sixths distinct (optimized to approximately 0.83625);
- that the work is computational/expository rather than a proof attempt;
- use of actual unfolded zeta zeros and their pair correlation;
- construction of an explicitly indefinite toy Hermitian family;
- comparison with synthetic GUE, Poisson, and lattice point processes;
- the two-level zeta/GUE comparison:
  - pair correlation;
  - inertia profile;
- reproducibility and limitations;
- principal observations only after experiments are complete.

---

# 1. Introduction

## 1.1 The Riemann Hypothesis

Introduce the zeta function, critical strip, critical line, and

\[
\rho=\beta+i\gamma.
\]

## 1.2 Historical progress on critical-line zeros

Briefly summarize Hardy, Selberg, Levinson, Conrey, Bui–Conrey–Young, Pratt–Robles–Zaharescu–Zeindler, and the Alpöge–Furman result: at least two thirds simple and on the critical line, at least five sixths distinct, with Montgomery–Taylor optimization to approximately 0.67250 and 0.83625.

## 1.3 Motivation

Main computational question:

> How do the local statistics of zero-like point configurations manifest themselves in a fixed indefinite Hermitian toy model?

Secondary question:

> How much of the toy matrix's second-moment behavior can be predicted from pair correlation alone?

## 1.4 Contributions

State only what the completed experiments actually establish.

Expected categories:

1. reproducible measurement of zeta pair correlation;
2. a transparent indefinite Hermitian toy apparatus;
3. a pair-correlation prediction of the apparatus's second moment;
4. a points-in comparison of zeta, GUE, Poisson, and lattice;
5. a two-level zeta/GUE consistency check.

---

# 2. Mathematical Background

## 2.1 Zeta zeros and unfolding

Define \(N(T)\), the smooth zero-counting approximation, and unfolded positions.

## 2.2 Montgomery pair correlation

Explain

\[
R_{\mathrm{GUE}}(u)
=
1-\left(\frac{\sin(\pi u)}{\pi u}\right)^2
\]

and level repulsion.

## 2.3 Positive-definite kernels and Gram matrices

Explain why a fixed positive-definite kernel produces a PSD matrix

\[
C_{ij}=k(x_i-x_j).
\]

## 2.4 Why the toy must be indefinite

Introduce

\[
H_\lambda=I-\lambda C
\]

as the reference toy construction and explicitly distinguish it from both Alpöge–Furman's finite Weil compression and Groskin's recent finite Galerkin Weil-form preprint. State that the toy is chosen for process-agnostic cross-process comparison, not because finite Weil-form matrices are computationally inaccessible.

## 2.5 Inertia, rank, trace, and Frobenius norm

Define:

\[
(n_{\mathrm{pos}},n_{\mathrm{neg}},n_{\mathrm{zero}}),
\qquad
\operatorname{rank},
\qquad
\operatorname{tr},
\qquad
\|\cdot\|_F.
\]

## 2.6 Positive-inertia lower bound

Derive

\[
n_{\mathrm{pos}}(H)
\ge
\frac{\operatorname{tr}(H)^2}
{\|H\|_F^2}
\]

under the condition \(\operatorname{tr}(H)>0\).

## 2.7 Pair correlation and the Frobenius second moment

Explain why

\[
\|C\|_F^2
=
\sum_{i,j}k(x_i-x_j)^2
\]

is naturally controlled, at the averaged level, by two-point statistics.

## 2.8 Relation to Alpöge–Furman v2

Present the actual proof skeleton before introducing the toy analogy:

\[
\widetilde G=P+Q,
\]

where on-line zeros contribute positive rank-one pieces to \(P\), while symmetric off-line pairs contribute blocks of signature \((1,1)\) to \(Q\). The prime-side calculation supplies

\[
\|\widetilde G\|_{\mathrm{HS}}^2
=
(R(\psi)+o(1))N,
\]

and the paper's specialized rank–trace/inertia inequality converts this structure into lower bounds for simple critical-line zeros and distinct zeros.

Then explain Project Montecito's deliberately looser analogy:

\[
\text{point-process geometry}
\rightarrow
\text{toy Hermitian inertia}
\rightarrow
\text{trace/second moment}
\rightarrow
\text{computational comparison}.
\]

State prominently that the toy family \(H_\lambda=I-\lambda C\) is **not** \(\widetilde G\) and that the toy positive-inertia bound is **not** Alpöge–Furman's Lemma 3.2.

## 2.9 Analytic second moment versus empirical pair correlation

Explain that Experiment 1's empirical GUE-style pair-correlation curve is related in spirit to the zero-difference statistics appearing in the paper, but it is not a numerical reproduction of the paper's unconditional prime-side second-moment evaluation.

## 2.10 Scope of the 0.682 ceiling

Explain that Alpöge–Furman's approximately \(0.682\) ceiling applies to a bandwidth-one certificate framework based on first two moments and the on-line/off-line block structure. Project Montecito Experiment 3 does not test this ceiling and should not be interpreted as a numerical route beyond it.

---

# 3. Experiment 1 — Actual Zeta Zeros

## 3.1 Data provenance

Odlyzko source, precision, checksum, validation.

## 3.2 Unfolding

Definition and diagnostics.

## 3.3 Pair-correlation estimator

Poisson unit test, edge correction, windowing.

## 3.4 Zeta results

Measured \(\widehat R_\zeta(u)\), GUE overlay, uncertainty.

## 3.5 Exported point-process artifacts

Unfolded points plus empirical pair correlation.

## 3.6 Relationship to the Alpöge–Furman analytic input

State explicitly that the measured empirical pair-correlation curve is not a numerical verification of the paper's prime-side Hilbert–Schmidt second moment; it is a computational characterization of the point process used by our toy experiments.

---

# 4. Experiment 2 — Indefinite Hermitian Apparatus

## 4.1 Reference design

Gaussian kernel and

\[
H_\lambda=I-\lambda C.
\]

## 4.2 Pre-registration

Kernel width, \(\lambda\)-grid, common block centers, nested block sizes, screening threshold, high-precision escalation rule, and frozen primary/secondary zeta inputs.

## 4.3 Spectrum-first inertia map and numerical sign resolution

Diagonalize \(C\) once, record \(\mu_j(C)\), derive crossing thresholds \(1/\mu_j(C)\), and classify signs as resolved positive, resolved negative, or numerically unresolved. Use selected direct \(H_\lambda\) diagonalizations as an independent check.

## 4.4 Trace/Frobenius identities

Analytic checks against implementation.

## 4.5 Pair-correlation second-moment prediction

Compare predicted and directly measured \(\|C\|_F^2\), including the explicit \(U_{\max}=30\) Gaussian tail budget.

## 4.6 Actual inertia

Report resolved positive/negative fractions and any unresolved-sign intervals. Do not silently map unresolved values to zero.

## 4.7 Positive-inertia bound

Compare \(b_{\mathrm{pos}}\) with observed or interval-valued positive fractions.

## 4.8 Scaling and finite-window stability

Compare common locations, nested block sizes, and numerical precision separately. Distinguish properties of the defined finite matrix from numerical uncertainty.

# 5. Experiment 3 — Synthetic Point Processes

## 5.1 Synthetic GUE

Generation, bulk extraction, unfolding, pair-correlation validation.

## 5.2 Poisson

Generation and validation.

## 5.3 Lattice

Construction and validation.

## 5.4 Pair-correlation comparison

Actual zeta versus synthetic processes.

## 5.5 Inertia-profile comparison

All processes under the same frozen apparatus.

## 5.6 Zeta versus GUE consistency check

Separate conclusions at the pair-correlation and inertia levels.

## 5.7 Optional intermediate models

Only if primary comparisons justify them.

## 5.8 What Experiment 3 does not test

State explicitly that the synthetic point-process comparison does not reproduce or probe the Alpöge–Furman bandwidth-one ceiling near \(0.682\), nor the paper's conditional higher-moment/support-beyond-one routes.

---

# 6. Results and Discussion

## 6.1 What pair correlation reproduces

## 6.2 How accurately pair correlation predicts the toy second moment

## 6.3 What the labeled pairwise arrangement adds beyond the averaged two-point summary

## 6.4 Zeta versus GUE

## 6.5 GUE versus Poisson versus lattice

## 6.6 Negative/null results

## 6.7 What the toy model does not imply

---

# 7. Limitations

Explicitly discuss:

- only 10,000 baseline zeta zeros;
- finite-height effects;
- finite GUE matrix effects;
- toy-kernel arbitrariness;
- dependence on bandwidth and \(\lambda\);
- local block sampling and finite-window dependence;
- numerically unresolved eigenvalue signs near crossing thresholds;
- no Groskin-style rigorous model-truncation budget for the Gaussian toy because there is no corresponding hidden cutoff-free target;
- no identification with the actual finite compression of Weil's form;
- no numerical test of the Alpöge–Furman bandwidth-one ceiling near \(0.682\);
- no theorem inferred from numerical similarity.

---

# 8. Conclusion

Return to the paper's intended contribution:

> Computational experiments can make the relationship among point-process statistics, matrix second moments, and Hermitian inertia visible without pretending to replace analytic proof.

---

# Appendices

## Appendix A — Zero Data and Checksums

## Appendix B — Unfolding

## Appendix C — Pair-Correlation Estimator

## Appendix D — Toy Kernel and Indefinite Family

## Appendix E — Spectrum-First Inertia, Sign Resolution, and Trace/Frobenius Identities

## Appendix F — Synthetic Point-Process Generators

## Appendix G — Reproducibility Instructions

## Appendix H — Additional Sensitivity Analyses

## Appendix I — Alignment Notes for Alpöge–Furman arXiv:2608.13637v2 and Groskin arXiv:2607.02828v3

---

# Proposed Execution Order

## Phase 0 — Freeze the Mathematics and Numerical Interpretation

Before coding Experiment 2:

- freeze arXiv:2608.13637v2 as the theorem reference;
- record Groskin arXiv:2607.02828v3 as recent adjacent preprint work, not a theorem on which Montecito depends;
- confirm the distinction among Alpöge–Furman's \(\widetilde G\), Groskin's finite Galerkin Weil-form matrix, and Montecito's \(H_\lambda\);
- confirm the points-in architecture and process-agnostic rationale;
- confirm the Gaussian kernel, primary \(\sigma=1\), and \(H_\lambda=I-\lambda C\);
- confirm the \(\lambda\)-grid;
- freeze the spectrum-first crossing computation;
- freeze resolved-positive / resolved-negative / unresolved numerical sign reporting;
- freeze common block centers and nested block-size rule;
- freeze the explicit Gaussian-tail budget for the pair-correlation/Frobenius bridge;
- preserve the first-\(10{,}000\) zeta points as primary and the high-height samples as secondary controls.

## Phase 1 — Experiment 1

- download authoritative zero table;
- validate selected entries;
- unfold first 10,000 zeros;
- validate pair-correlation estimator on Poisson;
- measure \(\widehat R_\zeta(u)\);
- export unfolded points and pair-correlation artifact.

## Phase 2 — Experiment 2

- implement the frozen Gaussian points-in apparatus;
- diagonalize \(C\) once per block and archive its spectrum/crossing thresholds;
- verify selected \(H_\lambda\) eigendecompositions against the spectrum-first identity;
- verify trace and Frobenius identities;
- compare pair-correlation-predicted and measured Frobenius terms with the explicit tail budget;
- run the preregistered zeta blocks;
- escalate borderline signs to higher precision and report unresolved cases;
- run nested block-size and block-location stability checks;
- only then freeze the Experiment 2 inertia profiles for use in Experiment 3.

## Phase 3 — Experiment 3

- generate and validate synthetic GUE, Poisson, and lattice point sets;
- use the unchanged apparatus;
- run the two-level zeta/GUE comparison;
- compare all inertia profiles.

## Phase 4 — Literature and External Review

Before any novelty claim:

- search for prior computational studies of comparable kernel-inertia models and monitor independent mathematical review of Groskin's preprint;
- have a mathematically knowledgeable reader inspect the toy-model section if possible;
- classify every claimed contribution as reproduction, toy-model observation, or new computational observation.

## Phase 5 — Paper Decision

Only after seeing the results decide whether the project supports:

- a computational notebook/blog project;
- an expository computational paper;
- an arXiv preprint.

**arXiv follows the results; it is not a project success criterion.**
