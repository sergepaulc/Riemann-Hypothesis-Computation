# Project Montecito — Project Specifications and Paper Outline — Version 0.4

## Computational Exploration of the Riemann Zeta Function, Pair Correlation, Point Processes, and a Toy Indefinite Hermitian Model

**Version:** 0.4  
**Date:** August 26, 2026

---

# Version 0.4 — Main Design Decisions

Version 0.4 is a **paper-alignment release**. It keeps the experimental architecture of Version 0.3 unchanged and updates the specification to match the current Alpöge–Furman arXiv paper, arXiv:2608.13637v2 (last revised August 19, 2026).

1. **Points-in is now the primary architecture.** Experiment 1 exports both the unfolded zeta-zero positions and the empirical pair-correlation function. Experiment 2 builds the toy Hermitian matrix from the point configuration itself. This allows the apparatus to remain sensitive to structure beyond pair correlation.

2. **The toy form is explicitly indefinite.** The reference model is no longer an unspecified Hermitian matrix derived directly from a correlation function. It is a one-parameter family
   \[
   H_\lambda(X)=I-\lambda C(X),
   \]
   where \(C(X)\) is a positive-semidefinite kernel Gram matrix built from the unfolded point configuration \(X\). The shift by \(I\) makes nontrivial inertia possible.

3. **Pair correlation is not discarded.** The empirical pair-correlation function \(\widehat R_\zeta(u)\) is used independently to predict the second-moment/Frobenius contribution of the toy matrix. This gives a direct bridge from Experiment 1 to Experiment 2 while avoiding a correlation-only architecture.

4. **The primary observable is inertia, not rank.** We distinguish
   \[
   n_{\mathrm{pos}}(H),\quad n_{\mathrm{neg}}(H),\quad n_{\mathrm{zero}}(H)
   \]
   from ordinary rank. The trace/Frobenius inequality used for positive directions is stated only under the required sign condition.

5. **Experiment 1 uses precomputed zeros as the primary data source.** The default source is Andrew Odlyzko's published zero tables, with spot validation against an independent source or high-precision computation.

6. **Dense \(10{,}000\times10{,}000\) eigendecompositions are explicitly avoided.** Experiments 2–3 use controlled local blocks of the unfolded point process.

7. **The toy-model mathematics is decided before implementation is time-boxed.** Coding is time-boxed; the model-selection decision is not rushed.

8. **Square-root cancellation uses the Mertens function as the primary arithmetic illustration.**

9. **All LaTeX in this specification uses standard Markdown/LaTeX syntax.** WordPress conversion, if needed, is a publication step rather than part of the internal specification.

10. **The project is aligned to Alpöge–Furman arXiv v2 without changing the toy architecture.** Version 0.4 incorporates the paper's precise theorem statement, the actual finite-compression/inertia skeleton, and the stated limits of the method. Project Montecito remains a computational toy exploration rather than a numerical reconstruction of that proof.

---

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

# Project Goal

The goal of this project is **not to prove the Riemann Hypothesis and not to validate the recent Alpöge–Furman theorem that approximately 67.25% of the zeros are simple and on the critical line**.

The goal is to build a reproducible computational framework that helps us explore four questions:

1. What does the pair-correlation structure of actual zeta zeros look like numerically?
2. Can that same zero configuration drive a simple indefinite Hermitian model whose inertia and spectral moments are mathematically interpretable?
3. What changes when the zeta point configuration is replaced by synthetic GUE, Poisson, lattice, and intermediate point processes while the apparatus remains fixed?
4. How much of the toy model's second-moment behavior is explained by pair correlation alone, and how much of its full inertia profile may reflect structure beyond pair correlation?

Supporting sections will also illustrate square-root cancellation and explain why a positive proportion of critical-line zeros does not make RH-dependent results "partly true."

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

Agreement at level 1 but disagreement at level 2 would be especially interesting because the points-in architecture can, in principle, respond to structure beyond pair correlation.

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

It is not a model of the finite compression of Weil's Hermitian form used by Alpöge–Furman and does not attempt to reproduce their proof of the two-thirds / 0.67250 simple-critical-line result.

Its purpose is narrower:

> Build a simple finite Hermitian family whose inertia responds to the geometry of a point configuration, while its Frobenius second moment can be connected directly to pair correlation.

## Architecture Decision: Points-In

The primary input to Experiment 2 is the unfolded point configuration

\[
X=\{x_1,\ldots,x_m\}.
\]

The empirical pair-correlation function is **not** the sole input to the matrix.

This is deliberate. A correlation-only apparatus would, by construction, be blind to all information beyond the two-point function and would make the zeta-versus-GUE consistency test largely a calibration exercise.

The measured pair correlation remains important as an **independent predictor of the matrix's second moment**.

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

For a block \(X=\{x_1,\ldots,x_m\}\), define the Gram matrix

\[
C_{ij}=k_\sigma(x_i-x_j).
\]

The Gaussian kernel is positive definite, so \(C\) is positive semidefinite.

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

For each eigenvalue \(\mu_j(C)\) of \(C\),

\[
\lambda_j(H_\lambda)=1-\lambda\mu_j(C).
\]

Therefore the inertia of \(H_\lambda\) changes when eigenvalues of \(C\) cross

\[
\frac{1}{\lambda}.
\]

The reference design does **not** select a single value of \(\lambda\) after seeing the data.

Instead, use a preregistered grid

\[
\Lambda=\{0.10,0.15,0.20,\ldots,0.95\}.
\]

The main observable is therefore an **inertia profile as a function of \(\lambda\)** rather than one cherry-picked number.

This construction is one transparent toy choice, not the "true" Hermitian model behind the zeta theorem.

### Why this design is useful

The shift by \(I\) avoids the trivial all-positive behavior that would occur if we studied only a positive-semidefinite Gram matrix.

At the same time, the construction remains simple enough to analyze exactly.

---

# Experiment 2 Observables

For each \(H_\lambda\), compute the inertia

\[
\operatorname{Inertia}(H_\lambda)
=
(n_{\mathrm{pos}},n_{\mathrm{neg}},n_{\mathrm{zero}}),
\]

where:

- \(n_{\mathrm{pos}}\) = number of positive eigenvalues;
- \(n_{\mathrm{neg}}\) = number of negative eigenvalues;
- \(n_{\mathrm{zero}}\) = number of numerically zero eigenvalues.

Define normalized inertia fractions

\[
p_{\mathrm{pos}}(\lambda)=\frac{n_{\mathrm{pos}}}{m},
\qquad
p_{\mathrm{neg}}(\lambda)=\frac{n_{\mathrm{neg}}}{m},
\qquad
p_{\mathrm{zero}}(\lambda)=\frac{n_{\mathrm{zero}}}{m}.
\]

Ordinary rank is

\[
\operatorname{rank}(H_\lambda)=n_{\mathrm{pos}}+n_{\mathrm{neg}}.
\]

**Do not use "rank" and "positive inertia" interchangeably.**

Use a numerical zero tolerance of the form

\[
\varepsilon_{\mathrm{eig}}
=
10^{-10}\max(1,\|H_\lambda\|_2),
\]

with a sensitivity check at neighboring tolerances.

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
\sum_{i,j}
k_\sigma(x_i-x_j)^2.
\]

This is the key bridge to pair correlation: the matrix second moment is explicitly a sum over **pairs of points**.

---

# A Valid Positive-Inertia Bound

Let the positive eigenvalues of \(H\) be \(\alpha_1,\ldots,\alpha_{n_{\mathrm{pos}}}\).

If

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
\frac{\operatorname{tr}(H)^2}
{\|H\|_F^2}.
\]

This is the sign-specific inequality used in the toy experiment.

It should not be confused with the standard rank inequality

\[
\operatorname{rank}(H)
\ge
\frac{\operatorname{tr}(H)^2}
{\|H\|_F^2},
\]

which by itself does not distinguish positive from negative eigenvalues.

Define the normalized lower bound

\[
b_{\mathrm{pos}}(\lambda)
=
\frac{1}{m}
\frac{\operatorname{tr}(H_\lambda)^2}
{\|H_\lambda\|_F^2}.
\]

The experiment compares

\[
b_{\mathrm{pos}}(\lambda)
\quad\text{with}\quad
p_{\mathrm{pos}}(\lambda).
\]

---

# Pair-Correlation Bridge

For the kernel matrix,

\[
\|C\|_F^2
=
m
+
\sum_{i\ne j}
k_\sigma(x_i-x_j)^2.
\]

For a long, approximately stationary, unfolded unit-density point process, pair correlation predicts the off-diagonal contribution schematically through

\[
\frac{1}{m}\|C\|_F^2
\approx
1+
\int_{\mathbb R}
k_\sigma(u)^2 R_2(u)\,du,
\]

up to finite-window and edge corrections.

Therefore Experiment 2 makes two measurements:

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

Agreement between them is an internal consistency check.

This preserves a direct Experiment 1 \(\rightarrow\) Experiment 2 dataflow without reducing the entire apparatus to pair correlation alone.

---

# Matrix Size and Feasibility

Do **not** construct or diagonalize a dense \(10{,}000\times10{,}000\) matrix.

Use local contiguous blocks of the unfolded point process.

Primary block sizes:

\[
m\in\{128,256,512\}.
\]

For each size, sample multiple preregistered blocks across the 10,000-zero sequence.

Suggested baseline:

- 16 blocks per size where possible;
- fixed selection rule recorded before comparing synthetic processes.

For each block, compute the full inertia profile over \(\Lambda\).

This keeps memory and eigendecomposition costs modest on a modern laptop.

---

# Experiment 2 Development Stages

## Stage A — Mathematical design

No coding time box.

Before implementation, freeze:

- points-in architecture;
- kernel \(k_\sigma\);
- primary bandwidth \(\sigma=1\);
- \(\lambda\)-grid;
- block sizes;
- inertia convention;
- eigenvalue tolerance;
- sign-specific bound;
- pair-correlation/Frobenius bridge.

## Stage B — Implementation

Time-box initial implementation to approximately **2–4 hours**.

The implementation succeeds if:

- unit tests pass;
- matrix is Hermitian to numerical precision;
- \(C\) is PSD to tolerance;
- \(H_\lambda\) shows nontrivial inertia for at least part of the preregistered grid on at least some baseline blocks;
- trace and Frobenius identities agree with direct calculations;
- pair-correlation-predicted and points-measured Frobenius terms are consistent within finite-sample error.

If these fail, stop and diagnose rather than tuning the model to obtain a desired result.

---

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

and similarly \(p_{\mathrm{neg}}\), \(p_{\mathrm{zero}}\), and \(b_{\mathrm{pos}}\).

This check is genuinely nontrivial because the apparatus ingests point configurations, not only their pair-correlation functions.

Possible outcomes:

- **Pair correlation and inertia both agree:** the toy apparatus sees zeta and GUE similarly at the measured scales.
- **Pair correlation agrees but inertia differs:** the apparatus may be responding to finite-sample effects or structure beyond pair correlation.
- **Pair correlation already differs materially:** first diagnose unfolding, estimator, or finite-size GUE generation before interpreting inertia.
- **All processes produce similar inertia:** the toy apparatus may be too insensitive.
- **Poisson or lattice produces stronger apparent positivity:** the toy observable measures something different from the initial intuition; this is a valid negative/redirecting result.

---

# Experiment 3 Metrics

For every process and block size report:

- empirical pair-correlation curve;
- \(p_{\mathrm{pos}}(\lambda)\);
- \(p_{\mathrm{neg}}(\lambda)\);
- \(p_{\mathrm{zero}}(\lambda)\);
- \(b_{\mathrm{pos}}(\lambda)\);
- \(\|C\|_F^2/m\);
- pair-correlation-predicted \(\|C\|_F^2/m\);
- eigenvalue distribution of \(C\);
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

# Experiment 4 — Numerical Illustration of Square-Root Cancellation

## Objective

Illustrate square-root cancellation with one probabilistic baseline and one arithmetic example.

This experiment is explanatory and is not quantitatively connected to the Alpöge–Furman 0.67250 simple-critical-line theorem.

## Random-Walk Baseline

Let

\[
S_N=\sum_{n=1}^N \varepsilon_n,
\qquad
\varepsilon_n\in\{-1,+1\}
\]

with independent equal probabilities.

Then

\[
\operatorname{Var}(S_N)=N,
\]

so the natural fluctuation scale is

\[
\sqrt N.
\]

## Arithmetic Example — Mertens Function

Define

\[
M(x)=\sum_{n\le x}\mu(n),
\]

where \(\mu\) is the Möbius function.

A standard equivalent formulation of RH is that, for every \(\varepsilon>0\),

\[
M(x)=O\left(x^{1/2+\varepsilon}\right).
\]

Numerically compare \(M(x)\) with square-root-scale reference curves while stating explicitly:

- the historical Mertens conjecture \(|M(x)|<\sqrt{x}\) is false;
- finite numerical behavior does not test RH;
- the experiment illustrates cancellation only.

## Outputs

- random-walk ensemble;
- \(M(x)\) computation over a feasible range;
- normalized plots such as \(M(x)/\sqrt{x}\);
- optional \(x^{1/2+\varepsilon}\) envelopes;
- explanation of what the plots do and do not imply.

---

# Section Study — Why 67% Is Not 67% of RH

Let \(N(T)\) count nontrivial zeros and \(N_0(T)\) those on the critical line.

A result such as

\[
\liminf_{T\to\infty}\frac{N_0(T)}{N(T)}
\ge 0.67
\]

does not imply that RH-dependent conclusions are "67% true."

RH requires every nontrivial zero to satisfy

\[
\beta=\frac12.
\]

Even a density-one result

\[
\frac{N_0(T)}{N(T)}\to1
\]

could leave infinitely many exceptional zeros off the line.

This section should survey several conditional consequences of RH and explain why exceptional zeros can still matter.

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
- eigenvalue tolerance;
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
│   └── metrics.py
│
├── experiments/
│   ├── exp1_pair_correlation/
│   ├── exp2_hermitian_apparatus/
│   ├── exp3_point_processes/
│   └── exp4_square_root/
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
- No observation from Experiments 2–4 is evidence for a proof of RH or validation of the Alpöge–Furman two-thirds / 0.67250 theorem.
- A null or negative result is an acceptable scientific outcome.

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
5. a two-level zeta/GUE consistency check;
6. explanatory square-root-cancellation numerics;
7. clarification of the gap between positive-density critical-line results and RH.

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

as the reference toy construction and explicitly distinguish it from the Weil form.

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

Kernel width, \(\lambda\)-grid, block sizes, tolerance, block-selection rule.

## 4.3 Trace/Frobenius identities

Analytic checks against implementation.

## 4.4 Pair-correlation second-moment prediction

Compare predicted and directly measured \(\|C\|_F^2\).

## 4.5 Actual inertia

Measure \(p_{\mathrm{pos}}\), \(p_{\mathrm{neg}}\), \(p_{\mathrm{zero}}\).

## 4.6 Positive-inertia bound

Compare \(b_{\mathrm{pos}}\) with observed \(p_{\mathrm{pos}}\).

## 4.7 Scaling and stability

Block-size and tolerance sensitivity.

---

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

# 6. Square-Root Cancellation

## 6.1 Random-walk intuition

Variance and \(\sqrt N\) scale.

## 6.2 Mertens function

Define \(M(x)\) and explain its RH connection.

## 6.3 Numerical illustration

Plots and limitations.

---

# 7. Why 67% Is Not 67% of RH

Explain why even density-one critical-line results can leave infinitely many exceptional zeros and why many RH-dependent consequences require control of every zero.

---

# 8. Results and Discussion

## 8.1 What pair correlation reproduces

## 8.2 How accurately pair correlation predicts the toy second moment

## 8.3 What the full point configuration adds

## 8.4 Zeta versus GUE

## 8.5 GUE versus Poisson versus lattice

## 8.6 Negative/null results

## 8.7 What the toy model does not imply

---

# 9. Limitations

Explicitly discuss:

- only 10,000 baseline zeta zeros;
- finite-height effects;
- finite GUE matrix effects;
- toy-kernel arbitrariness;
- dependence on bandwidth and \(\lambda\);
- local block sampling;
- no identification with the actual finite compression of Weil's form;
- no numerical test of the Alpöge–Furman bandwidth-one ceiling near \(0.682\);
- no theorem inferred from numerical similarity.

---

# 10. Conclusion

Return to the paper's intended contribution:

> Computational experiments can make the relationship among point-process statistics, matrix second moments, and Hermitian inertia visible without pretending to replace analytic proof.

---

# Appendices

## Appendix A — Zero Data and Checksums

## Appendix B — Unfolding

## Appendix C — Pair-Correlation Estimator

## Appendix D — Toy Kernel and Indefinite Family

## Appendix E — Inertia and Trace/Frobenius Identities

## Appendix F — Synthetic Point-Process Generators

## Appendix G — Reproducibility Instructions

## Appendix H — Additional Sensitivity Analyses

## Appendix I — Alignment Notes for Alpöge–Furman arXiv:2608.13637v2

---

# Proposed Execution Order

## Phase 0 — Freeze the Mathematics

Before coding Experiment 2:

- freeze arXiv:2608.13637v2 as the external theorem reference for Version 0.4;
- confirm the distinction between the paper's finite Weil compression \(\widetilde G\) and our toy family \(H_\lambda\);
- confirm the points-in architecture;
- confirm Gaussian kernel as the primary reference design;
- confirm \(H_\lambda=I-\lambda C\);
- confirm \(\lambda\)-grid;
- confirm inertia definitions and sign-specific inequality;
- confirm block sizes and tolerances.

## Phase 1 — Experiment 1

- download authoritative zero table;
- validate selected entries;
- unfold first 10,000 zeros;
- validate pair-correlation estimator on Poisson;
- measure \(\widehat R_\zeta(u)\);
- export unfolded points and pair-correlation artifact.

## Phase 2 — Experiment 2

- implement frozen toy apparatus;
- verify algebraic identities;
- run zeta blocks;
- compare pair-correlation-predicted and measured Frobenius terms;
- measure inertia profiles.

## Phase 3 — Experiment 3

- generate and validate synthetic GUE, Poisson, and lattice point sets;
- use the unchanged apparatus;
- run the two-level zeta/GUE comparison;
- compare all inertia profiles.

## Phase 4 — Supporting Material

- Mertens/square-root-cancellation illustration;
- "67% is not RH" study.

## Phase 5 — Literature and External Review

Before any novelty claim:

- search for prior computational studies of comparable kernel-inertia models;
- have a mathematically knowledgeable reader inspect the toy-model section if possible;
- classify every claimed contribution as reproduction, toy-model observation, or new computational observation.

## Phase 6 — Paper Decision

Only after seeing the results decide whether the project supports:

- a computational notebook/blog project;
- an expository computational paper;
- an arXiv preprint.

**arXiv follows the results; it is not a project success criterion.**
