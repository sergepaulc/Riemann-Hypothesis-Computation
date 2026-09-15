# Project Montecito — Experiment 3 Bounded Cloud Closure Protocol v1

**Date:** September 11, 2026  
**Status at issue:** Fixed before numerical execution  
**Classification:** Exploratory finite-sample closure study; not the full confirmatory Experiment 3 preregistration  

## 1. Governance decision

The approved full Experiment 3 specification, preregistration, Mac handoff, and feasibility work are preserved unchanged as a deferred research program. They are not invalidated or silently edited.

For Project Montecito Version 1, the experiment is narrowed to a bounded cloud study that can be completed in one execution cycle. The purpose is to obtain an honest, interpretable finite-sample result and close the active project. The full pair-matched, power-gated, D3-confirmed design is moved to a future-work appendix.

## 2. Scientific question

> On fixed finite windows, how do the normalized sinc-kernel second and fourth spectral moments of zeta-zero ordinates compare across height and against CUE, Poisson, lattice, and an exact homometric positive control?

The study asks whether the fourth-moment instrument behaves meaningfully on controlled examples and whether the three zeta height regimes are descriptively CUE-like or non-CUE-like under the same geometry.

It does **not** establish that a detected difference is independent of the complete two-point function, because the full pair-matched surrogate arm is deferred.

## 3. Frozen inputs

- `D0_zeta_first_10000_unfolded.csv`: first 10,000 unfolded zeta zeros.
- `D1_zeta_near_1e12_unfolded.csv`: 10,000 unfolded zeros near zero number 10^12.
- `D2_zeta_near_1e21_unfolded.csv`: 10,000 unfolded zeros near zero number 10^21.

D3 is excluded and must not be accessed.

## 4. Fixed zeta windows

For each 10,000-point dataset, use 16 deterministic contiguous windows of 512 points. Window starts are

```text
round(linspace(0, 9488, 16))
```

Within each 512-point outer window, use the centered 128-point core with local indices 192 through 319 inclusive. Thus the halo is 192 points per side. No window is selected or removed after endpoint inspection.

## 5. Synthetic controls

- CUE: 64 independent 512-point realizations from the Killip–Nenciu CMV beta=2 generator.
- Poisson: 64 independent fixed-count circular 512-point realizations.
- Lattice: one 512-point integer lattice with the same 128-point core.
- Homometric positive control: the two six-point sets

\[
A=\tfrac12\{0,1,2,6,8,11\},\qquad
B=\tfrac12\{0,1,6,7,9,11\}.
\]

The CUE and Poisson realization seeds are derived deterministically from the SHA-256 of this protocol and the realization index.

## 6. Kernel and endpoints

Use

\[
K_{ij}=\frac{\sin \pi(x_i-x_j)}{\pi(x_i-x_j)},\qquad K_{ii}=1.
\]

For every core/outer configuration report:

\[
\mu_2=\frac1{|C|}\sum_{i\in C}(K^2)_{ii},
\qquad
\mu_3=\frac1{|C|}\sum_{i\in C}(K^3)_{ii},
\qquad
\mu_4=\frac1{|C|}\sum_{i\in C}(K^4)_{ii}.
\]

Also report the exact anchored collision decomposition and

\[
\mu_4^{(>2)}
=
\frac{4T_{3,c}+W_{3,c}^{(0)}+W_{3,c}^{(1)}+Q_{4,c}}{|C|},
\]

which removes the one-point and two-distinct-point collision terms from the finite fourth moment.

## 7. Analysis rules

- Report all 16 zeta windows and all synthetic realizations.
- Summarize means, standard deviations, medians, and 2.5%/97.5% empirical quantiles.
- Compare each zeta dataset mean with the CUE distribution using a descriptive standardized difference and a bootstrap distribution of 16-window CUE means.
- These are exploratory finite-sample comparisons, not theorem-level or preregistered confirmatory p-values.
- Report lower-order `mu2` beside `mu4` and `mu4_gt2` before interpreting any fourth-moment difference.
- No parameter, dataset, window, or endpoint may be changed after results are viewed.

## 8. Terminal outcomes

Whichever of the following occurs closes the bounded study:

1. high-height zeta is descriptively consistent with CUE while low-height zeta differs;
2. one or more high-height zeta samples show a reproducible finite-sample difference from CUE;
3. no stable difference is observed;
4. a numerical or implementation defect prevents interpretation.

No outcome triggers an Experiment 3.1 in Project Montecito Version 1.

## 9. Claim boundary

This bounded study may support statements about the measured finite sinc-kernel moments and their behavior across the tested point configurations. It cannot prove a new fact about RH, certify higher-order correlation beyond the complete two-point law, or validate the Alpöge–Furman/Lamzouri theorems.
