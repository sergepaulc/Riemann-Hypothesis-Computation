# Project Montecito — Experiment 2 Report — Version 2

## Indefinite Gaussian Hermitian Apparatus on Frozen Zeta Point Configurations

**Date:** 2 September 2026  
**Closure package:** Part 3 of 6  
**Status:** Complete  
**Specification:** `Project_Montecito_Project_Specifications_v0.6.md`  
**Revision basis:** frozen Experiment 2 run, Validation Extension, adversarial peer review, and `Experiment2_Peer_Review_Response_v1.md`  
**Experiment 2 computational status:** **complete and independently reproduced**  
**Experiment 2 interpretation:** **revised after adversarial peer review**  
**Formal scientific closure:** **pending `Experiment2_Closure_Report_v1.md`**  
**Primary input:** frozen unfolded first 10,000 zeta zeros from Experiment 1  
**Secondary zeta controls:** samples near zero numbers $10^{12}$ and $10^{21}$  
**Primary kernel:** Gaussian, $\sigma=1$  
**Block sizes:** $m\in\{128,256,512\}$  
**Locations:** 16 preregistered common nested locations  
**$\lambda$ grid:** $0.10,0.15,\ldots,0.95$

> **Figure-path note.** Figure links in this report refer to files in the archived primary Experiment 2 package. Validation figures remain in the separate Validation Extension package.

---

# Version 2 revision note

Version 2 does **not** alter the frozen Experiment 2 input data, block manifest, kernel, $\lambda$ grid, spectra, inertia classifications, or primary numerical tables. The original computation survived independent reconstruction and the closure reruns.

The principal changes are interpretive and documentary:

1. the pair-correlation-to-Frobenius calculation is reframed as a **histogram reconstruction and quadrature check** over the same pair differences, not an independent zeta finding;
2. the height dependence of $D_C$ is described as a **Gaussian smoothing of the already measured two-point evolution**, not a second independent confirmation;
3. the positive-inertia lower bound is written in closed form and retained as an **algebraic lower bound and implementation check**, not a process discriminator;
4. the information content of the advertised observables is analyzed explicitly;
5. finite-window and kernel dependence are reported beside the inertia results rather than treated as secondary details;
6. the Experiment 2 outcome is characterized as **computationally valid but structurally underpowered for its original higher-order question**;
7. reviewer-generated Davenport–Heilbronn, Epstein, $\mu_4$, CUE-power, and matched-thinning calculations are clearly attributed and are not silently relabeled as frozen or independently reproduced Experiment 2 results;
8. the broad interpretations involving a rigidity ladder, RH-failure detection, and arithmetic number variance are withdrawn or narrowed.

The complete finding-by-finding disposition is recorded in `Experiment2_Peer_Review_Response_v1.md`.

---

# Executive summary

Experiment 2 constructed and tested the preregistered Hermitian toy family

$$
C_{ij}=\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right],
\qquad
H_\lambda=I-\lambda C,
$$

on the frozen zeta point configurations.

The numerical experiment is sound. The primary and validation packages were independently rechecked after peer review: all 19 frozen verification checks passed; all 2,592 block/$\lambda$ inertia classifications were reproduced exactly by the separate validation implementation; all primary and validation package checksums matched; and no numerically unresolved sign remained on the frozen grid.

The revised scientific findings are:

1. **The frozen toy has a reproducible, nontrivial inertia profile.** For primary $m=512$ blocks, all directions are positive through $\lambda=0.30$; negative directions first appear on the frozen grid at $\lambda=0.35$; and the mean positive fraction falls to approximately $0.777$ at $\lambda=0.50$, $0.670$ at $\lambda=0.70$, and $0.597$ at $\lambda=0.95$. These are descriptive properties of the defined finite Gaussian toy.

2. **Most advertised observables were structurally limited before any data were examined.** The trace $\operatorname{tr}H_\lambda=m(1-\lambda)$ contains no point-set information. The Frobenius second moment depends on the configuration through one two-point scalar, $D_C$. The normalized positive-inertia lower bound depends on that same scalar. Only the full spectrum or inertia can, in principle, reflect higher-order organization, and the completed experiment did not isolate such a contribution from ordinary two-point propagation.

3. **The pair-correlation bridge is a reconstruction, not independent evidence.** The direct Gaussian pair sum and the histogram calculation use the same multiset of pair differences. Their discrepancy is principally binning and quadrature error. The closure rechecks reproduced the zeta bin-width sequence, the large lattice failure, and a 200-realization Poisson ensemble whose discrepancies were centered essentially at zero. The bridge remains valuable as a normalization, smoothness, and code-path check.

4. **The height sequence in $D_C$ is valid but not independent of Experiment 1.** For the full 10,000-point samples, direct $D_C$ rises from $0.920167$ at low height to $0.945814$ near $10^{12}$ and $0.951435$ near $10^{21}$, close to the asymptotic Gaussian-weighted GUE benchmark $0.952040560$. Because $D_C$ is a linear functional of the two-point statistic, this is a smoothed expression of the finite-height pair-correlation evolution already measured in Experiment 1.

5. **Finite-window and kernel choices materially affect quantitative inertia.** The largest mean absolute $m=128$ versus $m=512$ positive-fraction difference is $0.007202$ at $\lambda=0.40$, and the largest single-location difference is $0.023438$. Changing the Gaussian bandwidth from $\sigma=1$ to $0.5$ or $2$ changes the inertia curve substantially. Numerical fractions must therefore be interpreted as properties of the frozen apparatus, not universal invariants of zeta zeros.

6. **The principal outcome is a limitation, not a numerical failure.** The apparatus and computation worked as specified, but the selected summary observables did not provide a clean test of structure beyond pair correlation. Experiment 2 is therefore **computationally valid but underpowered for its original higher-order question**.

Nothing in this report validates the Alpöge–Furman theorem, identifies $H_\lambda$ with a finite compression of Weil's Hermitian form, or constitutes evidence for or against the Riemann Hypothesis. Experiment 3 status is not decided in this report.

---

# 1. Purpose, scope, and evidence boundary

## 1.1 Original purpose

Experiment 2 is the apparatus stage of Project Montecito. It was designed to construct one mathematically transparent, process-agnostic finite Hermitian family whose input is an unfolded point configuration and whose second moment has an explicit two-point interpretation.

The apparatus is deliberately a toy. It is **not** the finite compression of Weil's Hermitian form used by Alpöge–Furman, and its positive-inertia inequality is not their specialized rank–trace/inertia result.

The original questions were:

1. What inertia profile does the frozen zeta point configuration produce in this fixed Gaussian apparatus?
2. How much of the apparatus's second-moment behavior can be reconstructed from the empirical pair correlation?
3. Does the full inertia reveal anything that can be separated from the measured two-point structure?

Version 2 preserves the first two calculations but revises how their scientific content is described. The third question remains unresolved by this apparatus.

## 1.2 Evidence classes

This report separates four evidence classes.

| Evidence class | Meaning in this report |
|---|---|
| **Frozen Experiment 2** | Preregistered inputs, code, outputs, and figures in the primary package |
| **Validation Extension** | Separate implementation and preregistered $\sigma$-sensitivity/spectral diagnostics |
| **Closure recheck** | Targeted package, algebra, quadrature, Poisson, lattice, and reproducibility checks archived with the peer-review response |
| **Peer-review follow-up** | Calculations reported by the peer reviewer but not supplied with sufficient code, seeds, arrays, and outputs for exact independent closure reproduction |

Peer-review follow-up evidence may be scientifically useful, but it is explicitly attributed when discussed. It does not become a frozen Experiment 2 result merely by appearing in this revised report.

## 1.3 Report boundary

This report:

- revises `Experiment2_Report_v1.md`;
- incorporates the approved dispositions in `Experiment2_Peer_Review_Response_v1.md`;
- preserves the frozen numerical experiment;
- records later corrections and limitations.

It does **not**:

- issue the formal Experiment 2 scientific-freeze decision;
- define or start Experiment 3;
- independently reproduce the unsupplied Davenport–Heilbronn, Epstein, CUE-power, exploratory $\mu_4$, or matched-thinning control packages;
- adopt the peer reviewer's proposed software or publication plan;
- claim a new theorem or a new zero-density bound.

---

# 2. Frozen design and preregistration

The design was frozen before spectra were examined.

Sixteen $512$-point blocks were placed at evenly spaced index locations from 1–512 through 9489–10000. The $256$- and $128$-point blocks were then nested concentrically inside each $512$-point block, preserving the same midpoint. This gives 48 blocks per dataset and 144 block matrices across the primary sample and two secondary zeta controls.

The frozen primary choices were:

- Gaussian kernel width $\sigma=1$;
- block sizes $m\in\{128,256,512\}$;
- 16 common nested locations;
- $\lambda=0.10,0.15,\ldots,0.95$;
- spectrum-first inertia computation;
- numerical sign-screening scale
  $$
  \varepsilon_{\mathrm{screen}}
  =10^{-10}\max(1,\|H_\lambda\|_2);
  $$
- direct $H_\lambda$ eigendecomposition checks at selected blocks and $\lambda$ values;
- the finite-window translation-edge pair-correlation convention inherited from Experiment 1;
- the first 10,000 zeros as the primary point set, with near-$10^{12}$ and near-$10^{21}$ samples as controls only.

The exact block indices, input SHA-256 hashes, kernel, $\lambda$ grid, screening rule, and direct-check locations are stored in:

- `00_preregistration/experiment2_config_v1_frozen.json`;
- `00_preregistration/block_manifest_v1.csv`.

The review did not identify result-dependent tuning of the block design.

---

# 3. Mathematical construction

For a block

$$
X=\{x_1,\ldots,x_m\},
$$

the primary kernel is

$$
k(u)=e^{-u^2/2},
$$

and the full Gram matrix is

$$
C_{ij}=k(x_i-x_j)=e^{-(x_i-x_j)^2/2}.
$$

The Gaussian kernel is positive definite. For distinct points, $C$ is mathematically positive definite. Also,

$$
C_{ii}=1,
\qquad
\operatorname{tr}C=m.
$$

The toy indefinite family is

$$
H_\lambda=I-\lambda C,
\qquad
\lambda\in\{0.10,0.15,\ldots,0.95\}.
$$

If

$$
0<\mu_1\le\cdots\le\mu_m
$$

are the eigenvalues of $C$, then the eigenvalues of $H_\lambda$ are exactly

$$
\eta_j(H_\lambda)=1-\lambda\mu_j.
$$

The crossings occur at

$$
\lambda_j^*=\frac1{\mu_j}.
$$

Thus one eigendecomposition of $C$ determines the complete frozen $H_\lambda$ inertia profile.

The trace and Frobenius identities are

$$
\operatorname{tr}H_\lambda=m(1-\lambda),
$$

and

$$
\|H_\lambda\|_F^2
=m(1-2\lambda)+\lambda^2\|C\|_F^2.
$$

Because the preregistered grid has $\lambda<1$, the trace is positive throughout the experiment.

---

# 4. Information content of the observables

The peer review exposed the central structural limitation of the original design. The relevant identities can be analyzed before looking at the data.

Define

$$
D_C:=\frac{\|C\|_F^2}{m}-1
=\frac{\operatorname{tr}(C^2)}{m}-1.
$$

Then

$$
\|H_\lambda\|_F^2
=m\left[(1-2\lambda)+\lambda^2(1+D_C)\right].
$$

The information hierarchy is therefore:

| Observable | Information available from the point set |
|---|---|
| $\operatorname{tr}H_\lambda=m(1-\lambda)$ | None |
| $\|H_\lambda\|_F^2$ | One normalized two-point scalar, $D_C$ |
| $b_{\mathrm{pos}}(\lambda)$ | The same scalar $D_C$ only |
| Full spectrum of $C$ / $p_{\mathrm{pos}}(\lambda)$ | Potentially higher-order information through the full spectral distribution |

The positive fraction can be written as the empirical spectral cumulative distribution of $C$ at the threshold $1/\lambda$:

$$
p_{\mathrm{pos}}(\lambda)
=\frac1m\#\left\{j:\mu_j(C)<\frac1\lambda\right\}.
$$

Unlike the trace and Frobenius quantities, the full spectral distribution is not fixed by one second moment. In principle it can reflect higher traces such as

$$
\operatorname{tr}(C^3),
\qquad
\operatorname{tr}(C^4),
\qquad\ldots
$$

and therefore higher-order products among points.

However, the completed Experiment 2 comparisons did not isolate such a contribution from the known two-point changes. This yields the central revised interpretation:

> **The matrix construction is not itself correlation-only, but three of the four advertised observable families are fixed by no point-set information or by one two-point scalar. The completed inertia analysis did not cleanly separate higher-order structure from two-point propagation.**

Experiment 2 was therefore underpowered for its original beyond-two-point question.

---

# 5. Positive-inertia lower bound and its exact role

For a Hermitian matrix $H$ with $\operatorname{tr}H>0$, let

$$
r=n_{\mathrm{pos}}(H)
$$

and let its positive eigenvalues be $\alpha_1,\ldots,\alpha_r$. Negative eigenvalues can only lower the total trace, so

$$
\operatorname{tr}H
\le
\sum_{j=1}^{r}\alpha_j.
$$

Cauchy–Schwarz gives

$$
\left(\sum_{j=1}^{r}\alpha_j\right)^2
\le
r\sum_{j=1}^{r}\alpha_j^2
\le
r\|H\|_F^2.
$$

Hence

$$
\boxed{
n_{\mathrm{pos}}(H)
\ge
\frac{\operatorname{tr}(H)^2}{\|H\|_F^2}
}.
$$

The normalized lower bound is

$$
b_{\mathrm{pos}}(\lambda)
=
\frac1m
\frac{\operatorname{tr}(H_\lambda)^2}
{\|H_\lambda\|_F^2}.
$$

Substituting the exact identities and writing $1+D_C=\|C\|_F^2/m$ gives

$$
\boxed{
b_{\mathrm{pos}}(\lambda)
=
\frac{(1-\lambda)^2}
{(1-2\lambda)+\lambda^2(1+D_C)}
}.
$$

The closure recheck evaluated this expression against all 2,592 frozen block/$\lambda$ rows. The maximum absolute difference from the stored values was

$$
3.33\times10^{-16}.
$$

The closed form has three immediate consequences:

1. once $D_C$ is specified, there is no additional explicit dependence on block size $m$;
2. the point configuration enters the bound only through $D_C$;
3. as $\lambda\to1$, the numerator vanishes as $(1-\lambda)^2$ while the denominator tends to $D_C>0$.

The collapse of the bound near $\lambda=1$ is therefore algebraic and predictable before any data are examined. It is not an empirical discovery. The bound remains mathematically valid and useful as an implementation check, but it is not a process discriminator or a close predictor of the measured inertia.

---

# 6. Histogram reconstruction of the Gaussian pair functional

## 6.1 Direct finite-matrix quantity

The Gram second moment is

$$
\|C\|_F^2
=m+\sum_{i\ne j}e^{-(x_i-x_j)^2}.
$$

Thus

$$
D_C=\frac{\|C\|_F^2}{m}-1
$$

is exactly the normalized off-diagonal Gaussian pair energy.

## 6.2 Frozen histogram reconstruction

For a block of span $L=x_m-x_1$, Experiment 2 uses the same finite-window translation-edge convention as Experiment 1. With

$$
\widehat{\rho^2}
=\frac{m(m-1)}{L^2},
$$

and the positive-separation empirical pair-correlation histogram $\widehat R_2$, the reconstructed Gram second moment is

$$
\widehat{\|C\|_F^2}
=
m+2\widehat{\rho^2}
\sum_k
\widehat R_{2,k}
\int_{a_k}^{b_k}(L-u)e^{-u^2}\,du,
$$

where $[a_k,b_k]$ is the $k$th bin, truncated only at $U_{\max}=30$ and at the block span.

For $\sigma=1$,

$$
\int_a^b(L-u)e^{-u^2}\,du
=
\frac{L\sqrt\pi}{2}
\left(\operatorname{erf}b-\operatorname{erf}a\right)
+
\frac12\left(e^{-b^2}-e^{-a^2}\right).
$$

No Gaussian matrix entry is truncated. Only the stored pair-correlation histogram ends at $u=30$. For $m=512$, the omitted ordered-pair contribution is bounded by

$$
m(m-1)e^{-900}
\approx3.57\times10^{-386},
$$

which is negligible relative to double precision.

## 6.3 Why this is a reconstruction

Let $n_k$ be the number of positive pair differences in bin $B_k=[a_k,b_k]$. The finite-window estimator is

$$
\widehat R_{2,k}
=
\frac{n_k}
{\widehat\rho^2\int_{a_k}^{b_k}(L-u)\,du}.
$$

Substituting it into the reconstruction gives

$$
2\sum_k n_k
\frac{
\int_{a_k}^{b_k}(L-u)e^{-u^2}\,du
}{
\int_{a_k}^{b_k}(L-u)\,du
}.
$$

The direct off-diagonal quantity is

$$
2\sum_{i<j}e^{-(x_j-x_i)^2}.
$$

Both sides therefore use the same multiset of pair differences. The histogram route replaces each individual Gaussian weight by an edge-weighted average over its bin. The discrepancy principally measures histogram resolution and quadrature, not statistically independent information about zeta.

## 6.4 Frozen primary block results

For the first-10,000 primary sample, the 16-location block averages are:

| $m$ | Direct $D_C$ mean | Location SD | Histogram reconstruction mean | Direct minus reconstruction | Mean relative Frobenius error |
|---:|---:|---:|---:|---:|---:|
| 128 | 0.911447 | 0.005052 | 0.914656 | -0.003209 | -0.1683% |
| 256 | 0.917196 | 0.004797 | 0.918541 | -0.001345 | -0.0706% |
| 512 | 0.918209 | 0.004610 | 0.919679 | -0.001470 | -0.0771% |

For the complete primary 10,000-point sample,

$$
D_C^{\mathrm{direct}}=0.920166507,
\qquad
D_C^{\mathrm{hist}}=0.920974609.
$$

Using the direct Frobenius value in the denominator, the relative Frobenius discrepancy is

$$
0.042085\%.
$$

![Frozen primary pair-functional reconstruction](03_figures/03_primary_pair_correlation_frobenius_bridge.png)

## 6.5 Closure quadrature controls

The closure recheck rebinned the same primary pair differences at four resolutions:

| Bin width $\Delta u$ | Reconstructed $D_C$ | Relative Frobenius discrepancy |
|---:|---:|---:|
| 0.40 | 0.939403297 | 1.001829% |
| 0.20 | 0.925060669 | 0.254882% |
| 0.10 | 0.920974609 | 0.042085% |
| 0.05 | 0.920441988 | 0.014347% |

The discrepancy decreases strongly as the bin width is reduced, consistent with the interpretation as piecewise-constant quadrature error.

The same estimator was applied to the exact unit lattice:

$$
D_C^{\mathrm{direct}}=0.77255623,
\qquad
D_C^{\mathrm{hist}}=0.69495983,
$$

with signed relative Frobenius discrepancy

$$
-4.377655\%.
$$

The lattice's two-point measure is concentrated at discrete spacings rather than represented by a smooth density. The piecewise-constant density histogram therefore performs poorly, which is a genuine and useful failure mode of the reconstruction.

A separate closure control used 200 unit-density Poisson realizations of 10,000 points, with independent exponential gaps, NumPy `default_rng` seed `20260902`, and exact finite-sample rescaling to mean nearest-neighbor spacing 1. At $\Delta u=0.1$:

| Poisson ensemble statistic | Relative Frobenius discrepancy |
|---|---:|
| Mean signed | -0.000025% |
| Standard deviation | 0.015492% |
| Minimum | -0.035917% |
| Maximum | 0.040089% |
| 1st percentile | -0.033215% |
| 99th percentile | 0.035726% |

Very small reconstruction discrepancies therefore occur for an ordinary smooth process and are not peculiar evidence about zeta.

## 6.6 Revised interpretation

The retained result is:

> **A width-0.1 empirical pair-correlation histogram reconstructs the associated smooth Gaussian pair functional with small quadrature error for the zeta data and for smooth control processes.**

This validates the estimator normalization, bin integration, smoothness assumption at the chosen resolution, and agreement of two implementation routes. It is not an independent confirmation of Experiment 1, the Alpöge–Furman theorem, or RH.

---

# 7. Numerical methodology, integrity, and independent reproduction

## 7.1 Frozen computation

For every block, the primary pipeline:

1. constructed the full Gaussian matrix $C$;
2. verified symmetry and unit diagonal;
3. diagonalized $C$ once with a symmetric eigensolver;
4. recorded every $\mu_j(C)$ and crossing threshold $1/\mu_j$;
5. derived all 18 $H_\lambda$ spectra from $1-\lambda\mu_j$;
6. applied the screening scale
   $$
   \varepsilon_{\mathrm{screen}}
   =10^{-10}\max(1,\|H_\lambda\|_2);
   $$
7. designated any value inside the screening band for higher-precision escalation;
8. independently diagonalized selected $H_\lambda$ matrices at locations 1, 8, and 16 for all three block sizes and $\lambda\in\{0.10,0.50,0.95\}$;
9. verified the trace and Frobenius identities;
10. compared the direct pair functional with its histogram reconstruction.

No case entered the high-precision escalation path. Location and block-size variation are descriptive finite-window quantities, not standard errors from exchangeable samples.

## 7.2 Frozen numerical integrity

| Check | Result |
|---|---:|
| Block matrices analyzed | 144 |
| Block/$\lambda$ evaluations | 2,592 |
| Numerically unresolved sign assignments | 0 |
| Maximum symmetry error in $C$ | 0 |
| Maximum diagonal error in $C$ | 0 |
| Minimum eigenvalue of any $C$ block | $9.421\times10^{-5}$ |
| Blocks failing PSD tolerance | 0 |
| Maximum $\|C\|_F^2$ spectral-identity error | $5.684\times10^{-13}$ |
| Maximum trace-identity error | $1.137\times10^{-13}$ |
| Maximum $\|H\|_F^2$ identity error | $3.411\times10^{-13}$ |
| Maximum selected direct-$H$ spectrum error | $2.487\times10^{-14}$ |
| Closest frozen-grid $H$ eigenvalue to zero | $2.516\times10^{-6}$ |
| $m=512$ Gaussian tail bound | $3.57\times10^{-386}$ |

The smallest sign margin was approximately $1.4944\times10^4$ screening thresholds. The absence of unresolved signs is not marginal.

## 7.3 Post-review package and verification audit

The closure audit confirmed:

| Audit | Result |
|---|---:|
| Primary package SHA-256 matches | **45 / 45** |
| Primary artifact-manifest size/hash errors | **0** |
| Validation package SHA-256 matches | **19 / 19** |
| Frozen verification checks rerun | **19 / 19 PASS** |
| Independent validation inertia classifications | **2,592 / 2,592 exact** |
| Maximum closed-form $b_{\mathrm{pos}}$ difference | $3.33\times10^{-16}$ |

The closure rerun environment was:

- Python 3.13.5;
- NumPy 2.3.5;
- pandas 2.2.3;
- SciPy 1.17.0;
- Linux 6.18.35 x86_64.

The separate validation implementation reconstructed the $\sigma=1$ matrices and spectra from the frozen inputs and block manifest. Its largest primary-versus-independent differences were approximately $2.22\times10^{-14}$ for $\mu_{\max}$, $1.14\times10^{-13}$ for direct $\|C\|_F^2$, and machine precision for the normalized summary values. All inertia counts were exactly identical.

**Conclusion:** no frozen numerical result in Experiment 2 requires retraction or regeneration.

---

# 8. Primary inertia results

For primary $m=512$ blocks:

| $\lambda$ | Mean $p_{\mathrm{pos}}$ | Location SD | Mean $p_{\mathrm{neg}}$ | Mean $b_{\mathrm{pos}}$ | Mean bound slack |
|---:|---:|---:|---:|---:|---:|
| 0.10 | 1.000000 | 0.000000 | 0.000000 | 0.988791 | 0.011209 |
| 0.25 | 1.000000 | 0.000000 | 0.000000 | 0.907422 | 0.092578 |
| 0.35 | 0.998657 | 0.001549 | 0.001343 | 0.789749 | 0.208908 |
| 0.40 | 0.882202 | 0.007436 | 0.117798 | 0.710182 | 0.172020 |
| 0.50 | 0.776978 | 0.005154 | 0.223022 | 0.521322 | 0.255655 |
| 0.60 | 0.717041 | 0.004026 | 0.282959 | 0.326164 | 0.390877 |
| 0.70 | 0.669678 | 0.002842 | 0.330322 | 0.166693 | 0.502984 |
| 0.75 | 0.652954 | 0.002642 | 0.347046 | 0.107948 | 0.545006 |
| 0.85 | 0.623169 | 0.003227 | 0.376831 | 0.032804 | 0.590365 |
| 0.95 | 0.596558 | 0.003634 | 0.403442 | 0.003008 | 0.593550 |

All primary blocks are positive definite through $\lambda=0.30$. The first negative directions on the frozen grid appear at $\lambda=0.35$. The positive fraction then decreases smoothly rather than collapsing and remains approximately $0.60$ at $\lambda=0.95$.

This behavior is exactly auditable from the fixed spectrum of $C$: increasing $\lambda$ lowers the threshold $1/\lambda$ through that spectrum.

![Primary inertia and algebraic lower bound](03_figures/01_primary_inertia_and_bound_m512.png)

The measured positive fraction and the lower bound separate substantially at later $\lambda$. For example:

- at $\lambda=0.50$, $p_{\mathrm{pos}}\approx0.777$ while $b_{\mathrm{pos}}\approx0.521$;
- at $\lambda=0.70$, $p_{\mathrm{pos}}\approx0.670$ while $b_{\mathrm{pos}}\approx0.167$;
- at $\lambda=0.95$, $p_{\mathrm{pos}}\approx0.597$ while $b_{\mathrm{pos}}\approx0.003$.

This is not a surprising empirical collapse of an otherwise discriminating statistic. The lower bound is algebraically constrained to vanish near $\lambda=1$. Its large slack demonstrates that one trace and one Frobenius moment do not closely specify the full inertia, but the bound itself cannot identify where the additional spectral information comes from.

![Slack between measured positive fraction and lower bound](03_figures/06_primary_positive_bound_slack_m512.png)

---

# 9. Finite-window and kernel sensitivity

## 9.1 Nested block-size and location dependence

For the primary sample, the largest mean absolute difference between nested $m=128$ and $m=512$ positive fractions is

$$
0.0072021484
$$

at $\lambda=0.40$. The largest single-location nested difference is

$$
0.0234375,
$$

also at $\lambda=0.40$.

For $m=512$, the largest descriptive standard deviation across the 16 locations is $0.007436$, again at $\lambda=0.40$. Away from the first-crossing region, location variation is generally smaller.

These values show that the finite matrices are reproducible across the preregistered windows, but they also set a practical scale for process comparisons. The $0.007202$ mean block-size effect is comparable with some small zeta-versus-control differences discussed during review. Internal stability alone therefore does not demonstrate power for every future comparison. Any such comparison must fix $m$ and report finite-window sensitivity beside the effect size.

The block audit does not establish an infinite-size limit.

![Positive inertia by block size](03_figures/02_primary_positive_inertia_by_block_size.png)

![Location variability](03_figures/07_primary_location_variability.png)

## 9.2 Gaussian-width sensitivity

The Validation Extension kept the point sets and block locations fixed while changing only the Gaussian width.

For the complete 10,000-point samples, direct $D_C$ is:

| Sample | $\sigma=0.5$ | $\sigma=1$ | $\sigma=2$ |
|---|---:|---:|---:|
| First 10,000 | 0.209146 | 0.920167 | 2.606175 |
| Near $10^{12}$ | 0.238238 | 0.945814 | 2.625158 |
| Near $10^{21}$ | 0.242363 | 0.951435 | 2.630736 |
| GUE weighted benchmark | 0.241262 | 0.952041 | 2.634701 |

For the primary first-10,000 sample at $m=512$:

| $\lambda$ | $p_{\mathrm{pos}}$, $\sigma=0.5$ | $p_{\mathrm{pos}}$, $\sigma=1$ | $p_{\mathrm{pos}}$, $\sigma=2$ |
|---:|---:|---:|---:|
| 0.35 | 1.000000 | 0.998657 | 0.834961 |
| 0.50 | 0.997559 | 0.776978 | 0.784546 |
| 0.70 | 0.788818 | 0.669678 | 0.750977 |
| 0.95 | 0.596436 | 0.596558 | 0.722290 |

The exact numerical inertia profile is therefore kernel dependent. This does not invalidate the preregistered $\sigma=1$ result. It means that the fractions are properties of a specified toy apparatus, not universal statistics of the zeta process.

The primary $\sigma=1$ result remains controlling. Sensitivity widths may not replace it post hoc because they appear more interesting.

---

# 10. Secondary high-height zeta controls

The high-height samples were processed with the same frozen block indices and Gaussian apparatus. They remain secondary controls and were not substituted for the primary first-10,000 point set.

## 10.1 Gaussian-weighted two-point scalar

For $\sigma=1$:

| Zeta sample | Direct $D_C$ | Histogram $D_C$ | Relative Frobenius discrepancy | Direct minus GUE benchmark | Relative deviation from GUE benchmark |
|---|---:|---:|---:|---:|---:|
| First 10,000 | 0.920167 | 0.920975 | 0.0421% | -0.031874 | -3.348% |
| Near $10^{12}$ | 0.945814 | 0.946631 | 0.0420% | -0.006227 | -0.654% |
| Near $10^{21}$ | 0.951435 | 0.953012 | 0.0808% | -0.000605 | -0.064% |

The asymptotic Gaussian-weighted GUE benchmark is

$$
D_C^{\mathrm{GUE}}
=2\int_0^\infty e^{-u^2}
\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]du
=0.952040560.
$$

The height sequence is real and reproducible. Its revised interpretation is narrower than in Report v1:

> **$D_C$ is a linear Gaussian smoothing of the two-point statistic. Its movement toward the GUE benchmark is therefore a weighted expression of the pair-correlation evolution already documented in Experiment 1, not a second independent confirmation.**

No monotone convergence law or convergence rate is inferred from three height regimes.

![Full-data $D_C$ across height](03_figures/08_full_dataset_Dc_vs_GUE_benchmark.png)

## 10.2 Inertia across height

For $m=512$, the mean positive fractions are:

| $\lambda$ | First 10,000 | Near $10^{12}$ | Near $10^{21}$ |
|---:|---:|---:|---:|
| 0.35 | 0.998657 | 0.973267 | 0.970093 |
| 0.50 | 0.776978 | 0.781006 | 0.781250 |
| 0.70 | 0.669678 | 0.672729 | 0.673950 |
| 0.90 | 0.607178 | 0.613525 | 0.613403 |
| 0.95 | 0.596558 | 0.600586 | 0.600952 |

The largest height-dependent difference occurs near the first spectral crossing at $\lambda=0.35$. The low-height configuration remains almost entirely positive while the high-height controls have already acquired approximately $2.7$–$3.0\%$ negative directions.

For $\lambda\ge0.40$, the maximum absolute difference in mean positive fraction between the low-height and near-$10^{21}$ samples is $0.00623$. The later inertia curves are therefore close at the measured scale.

This pattern is consistent with the known Level-1 pair-correlation distortion propagating into the Gaussian spectrum and then becoming small at high height. It is not a proof that the full inertia is universally determined by pair correlation.

![Positive inertia across zeta height controls](03_figures/05_zeta_height_controls_positive_inertia_m512.png)

## 10.3 Spectral-tail localization

For $m=512$, $\sigma=1$:

| Sample | Mean $\mu_{\max}(C)$ | Mean first crossing $1/\mu_{\max}$ |
|---|---:|---:|
| First 10,000 | 2.857267 | 0.350134 |
| Near $10^{12}$ | 3.174937 | 0.315128 |
| Near $10^{21}$ | 3.225853 | 0.310351 |

Representative pooled-spectrum quantiles are:

| Quantile | First 10,000 | Near $10^{12}$ | Near $10^{21}$ |
|---:|---:|---:|---:|
| 0.010 | 0.006247 | 0.002540 | 0.002128 |
| 0.050 | 0.012730 | 0.008619 | 0.008072 |
| 0.250 | 0.107397 | 0.100653 | 0.099947 |
| 0.500 | 0.658056 | 0.651962 | 0.651426 |
| 0.750 | 1.852215 | 1.840396 | 1.844431 |
| 0.950 | 2.701841 | 2.757917 | 2.758784 |
| 0.990 | 2.794286 | 2.979380 | 3.014965 |
| 0.999 | 2.862505 | 3.177541 | 3.267953 |

The median is nearly unchanged, whereas the upper one percent and the extreme upper edge differ substantially. This explains the pronounced first-crossing shift even though most of the later inertia curve is close.

$\mu_{\max}$ is retained only as a descriptive upper-edge statistic and as the determinant of the first crossing. The earlier suggestion that it forms a general rigidity ladder is withdrawn.

---

# 11. Scientific interpretation after peer review

## 11.1 What the apparatus measured successfully

The experiment successfully measured:

- the complete spectra of 144 frozen Gaussian Gram matrices;
- exact spectrum-first inertia profiles across 2,592 block/$\lambda$ evaluations;
- finite-window variation across common nested blocks;
- sensitivity to Gaussian bandwidth;
- the Gaussian pair functional $D_C$ at low and high zeta heights;
- the upper-spectral-tail origin of the first-crossing shift.

These are reproducible computational facts about the defined toy.

## 11.2 What the original framing overstated

The original framing assigned too much independent scientific content to three quantities:

1. **Histogram bridge agreement.** It is a reconstruction from the same pair differences, not a statistically independent validation.
2. **Height evolution of $D_C$.** It is a linear smoothing of the two-point evolution, not a second independent observable in the evidential sense.
3. **Positive-inertia lower-bound collapse.** It follows algebraically from the closed form, not from an unexpected numerical phenomenon.

## 11.3 Why “underpowered” is the correct conclusion

The experiment did not fail computationally. It did exactly what was preregistered, and its outputs survived review.

The limitation is the mismatch between the information level of the question and that of the chosen summaries:

$$
\operatorname{tr}H_\lambda
\quad\text{contains no point-set data},
$$

$$
\|H_\lambda\|_F^2
\quad\text{contains a two-point scalar},
$$

$$
b_{\mathrm{pos}}
\quad\text{contains that same scalar},
$$

while only the full spectrum had a route to higher-order information. The completed height comparison did not isolate a higher-order residual after accounting for the known Level-1 changes.

The principal scientific outcome is therefore a limitation:

> **The frozen Gaussian apparatus is a valid instrument for visualizing how a point configuration generates an indefinite inertia profile, but the advertised summary observables were underpowered for separating higher-order structure from pair-correlation propagation.**

---

# 12. Peer-review follow-up controls, corrections, and successor clues

This section records later work prompted by the peer review. It is not retroactively part of the preregistered Gaussian experiment.

## 12.1 Evidence boundary for follow-up work

The following were independently rechecked during closure:

- the closed form and numerical reproduction of $b_{\mathrm{pos}}$;
- the algebra showing that the bridge is an edge-weighted bin approximation to the direct pair sum;
- the zeta bin-width sequence;
- the lattice reconstruction failure;
- the 200-realization Poisson reconstruction control;
- the fourth-moment arithmetic described below;
- the thinning identity described below.

The following were reported by the peer reviewer but were not supplied with sufficient source artifacts for exact closure reproduction:

- the exact CUE bridge realization and eight-realization power calculation;
- Davenport–Heilbronn zero searches, unfolding, spectra, and inertia profiles;
- Epstein-zeta zero searches, unfolding, spectra, and inertia profiles;
- the exploratory $\mu_4=3.2601\pm0.0198$ estimate and its block-bias study;
- the matched-thinned-CUE simulation.

They remain attributed peer-review follow-up findings.

## 12.2 Davenport–Heilbronn and Epstein stress tests

The peer reviewer reported two controls based on functions with finite-window evidence of zeros away from the critical line.

In the finite windows reported by the reviewer:

- approximately $8.3\%$ of the expected Davenport–Heilbronn zeros were not represented on the critical line;
- approximately $32.3\%$ of the expected zeros for the selected class-number-two Epstein example were not represented on the critical line.

These are finite-window counting deficits, not universal asymptotic percentages.

The reported frozen Gaussian inertia profiles for the surviving on-line subsets remained close to those of zeta and CUE: differences were reported as at most approximately $0.005$ for Davenport–Heilbronn at $\lambda\ge0.5$ and approximately $0.02$ for Epstein at later $\lambda$.

The appropriate conclusion is narrow:

> **In the two finite on-line-subset, ordinate-only controls reported by the peer reviewer, the frozen Gaussian apparatus showed no reliable sensitivity to the underlying RH failure.**

The apparatus receives unfolded ordinates $x(\gamma_i)$ but not the real parts $\beta_i$ of zeros $\rho_i=\beta_i+i\gamma_i$. It cannot directly encode critical-line membership. It can respond only indirectly if off-line zeros alter the selected ordinate process.

The controls also exposed two important methodological traps:

1. a coarse zero scan can miss close pairs and bias the result toward excessive apparent repulsion;
2. unfolding an on-line subset with a smooth count for all zeros can produce a plausible but invalid non-unit mean spacing.

Future process-specific unfolding should therefore include an automatic assertion that the resulting mean spacing is approximately one.

Three possible representations of an RH-false control must not be conflated:

1. the surviving on-line ordinate subset;
2. the all-zero ordinate multiset, preserving coincident ordinates and multiplicity;
3. the full complex-zero configuration, retaining both $\beta$ and $\gamma$.

Only the first was represented in the reported Gaussian controls.

## 12.3 Number variance and the thinning retraction

The peer-review exploration initially reported a striking number-variance sequence for zeta, Davenport–Heilbronn, and Epstein on-line subsets. That arithmetic interpretation is withdrawn.

If an original unit-density process is independently retained with probability $p$, then conditional binomial variance and rescaling give the exact identity

$$
\boxed{
\Sigma_{\mathrm{thin}}^2(L)
=
p^2\Sigma_{\mathrm{orig}}^2(L/p)
+(1-p)L
}.
$$

The linear term $(1-p)L$ is unavoidable and can dominate the slowly growing number variance of a rigid process. Number variance of a surviving on-line subset is therefore strongly confounded by the missing-point/thinning mechanism and cannot, by itself, distinguish arithmetic loss of critical-line zeros from ordinary deletion.

The peer reviewer's matched-thinned-CUE simulation was not independently reproduced in the closure package, but the exact identity is sufficient to establish thinning as a decisive confound. No residual number-variance claim is carried forward.

## 12.4 Fourth-moment clue and numerical gate

A sinc-kernel moment exploration was proposed after the limitations of the Gaussian summaries were understood. For the first-two-moment extremal spectral distribution

$$
0\text{ with weight }\frac16,
\qquad
1\text{ with weight }\frac23,
\qquad
2\text{ with weight }\frac16,
$$

the exact moments are

$$
m_1=1,
\qquad
m_2=\frac43,
\qquad
m_3=2,
\qquad
m_4=\frac{10}{3}.
$$

Against the sine-process target sequence stated in the review corpus,

$$
1,
\qquad
\frac43,
\qquad
2,
\qquad
\frac{13}{4},
$$

the first separation is

$$
\frac{10}{3}-\frac{13}{4}
=\frac1{12}.
$$

Thus $\mu_4$, not $\mu_3$, is the first separating moment for this specific extremal-versus-sine comparison. This does not imply that $\mu_3$ lacks higher-order information in general, and no novelty claim is made here.

The peer reviewer reported an exploratory high-height estimate

$$
\mu_4=3.2601\pm0.0198,
$$

but also reported a chopped-block bias of approximately $-0.018$, compared with approximately $-0.0007$ for complete runs. Those numerical values were not independently reproduced for closure. The reported bias is material relative to the target separation $1/12$.

Before $\mu_4$ can become a primary successor observable, a core-plus-halo estimator should construct the kernel on a larger surrounding window, measure the fourth-moment contribution only on a central core, and increase the halo until the core estimate stabilizes. Matched-bias cancellation alone is not yet an adequate validation.

## 12.5 Closed Christoffel-to-proportion branch

The follow-up reproduced the finite identity

$$
\Lambda_m(0)=\frac1{(H^{-1})_{00}}
$$

for a Hankel moment matrix and recovered $\Lambda_2=5/36$. But the proposed direct conversion

$$
1-\Lambda_m(0)
\longrightarrow
\text{simple-critical-line proportion}
$$

does not match the known cases:

| $m$ | $1-\Lambda_m(0)$ | Relevant quoted constant |
|---:|---:|---:|
| 1 | 0.7500 | $2/3\approx0.6667$ |
| 2 | 0.8611 | $13/18\approx0.7222$ |

The missing on-line/off-line block accounting is analytic mathematics, not a numerical detail. The direct Christoffel-to-proportion route is therefore closed unless that mathematics is developed. This does not close higher-moment exploration generally.

## 12.6 Formal status of corrected interpretations

| Item | Final status |
|---|---|
| Pair-correlation bridge as independent validation | **Reframed** as reconstruction/quadrature |
| Height-dependent $D_C$ as independent confirmation | **Reframed** as smoothed two-point evolution |
| $b_{\mathrm{pos}}$ as a discriminator | **Retired**; algebraic sanity check only |
| $\mu_{\max}$ as a rigidity proxy | **Withdrawn interpretation** |
| Arithmetic number-variance ladder | **Retracted** |
| Universal claim that the toy cannot detect RH failure | **Not accepted** |
| Direct Christoffel-to-proportion route | **Closed branch** |
| $\mu_4$ | **Retained secondary idea with a boundary-bias gate** |
| Experiment 3 readiness or closure | **Not decided in this report** |

---

# 13. What Experiment 2 establishes

For the frozen v0.6 Gaussian apparatus, Experiment 2 establishes that:

1. the preregistered Gaussian Gram matrices were constructed correctly and are positive definite at the reported numerical resolution;
2. the spectrum-first identity exactly determines the frozen $H_\lambda$ inertia profiles;
3. the complete frozen grid has no unresolved sign assignments;
4. the apparatus produces a reproducible nontrivial inertia profile on the primary zeta point set;
5. a finite pair-correlation histogram accurately reconstructs the smooth Gaussian pair functional at the chosen resolution, with a quantifiable quadrature error;
6. the low-height-to-high-height $D_C$ sequence is a reproducible Gaussian smoothing of the corresponding two-point evolution;
7. the quantitative inertia profile depends on block/window choices and materially on the Gaussian bandwidth;
8. the positive-inertia lower bound is valid but depends on the point process only through the scalar $D_C$ and becomes algebraically vacuous near $\lambda=1$;
9. the completed apparatus did not isolate a higher-order inertia contribution after the known two-point changes were taken into account;
10. the original Experiment 2 design was computationally clean but structurally underpowered for its intended beyond-two-point question.

---

# 14. What Experiment 2 does not establish

Experiment 2 does **not** establish:

- any new statement about the location, simplicity, or multiplicity of Riemann-zeta zeros;
- any numerical validation of the Alpöge–Furman theorem;
- any identification of $H_\lambda$ with the finite Weil/Bombieri Hermitian form;
- any evidence for or against the Riemann Hypothesis;
- that pair correlation uniquely determines the full inertia of every point-process kernel matrix;
- that the frozen Gaussian apparatus contains no higher-order information whatsoever;
- that the apparatus universally cannot detect RH failure;
- that the finite-window Davenport–Heilbronn or Epstein percentages are asymptotic proportions;
- that $\mu_{\max}$ is a general rigidity measure;
- that number variance of an on-line subset is an RH-sensitive statistic;
- that the observed block stability implies an infinite-size limit;
- that the high-height residuals are exactly zero;
- a convergence rate in height;
- a justified direct route from Christoffel functions to an improved simple-zero proportion;
- a validated primary $\mu_4$ result;
- that Experiment 3 is ready, unnecessary, or closed; any revised design is outside this report.

---

# 15. Conclusion and report-status decision

Experiment 2 is a numerically clean and reproducible study of a defined Gaussian Hermitian toy. Its frozen computation survived independent validation and post-review closure checks.

Its principal scientific outcome is a limitation:

> **Most of the advertised observables are fixed by no point-set data or by two-point information, and the completed inertia analysis did not isolate an additional higher-order signal. Experiment 2 is therefore computationally valid but underpowered for its original higher-order question.**

That limitation is informative. It clarifies what the apparatus contains, prevents a paper from being built around a circular bridge interpretation, and establishes a design rule for successor work:

$$
\boxed{
\text{Choose an observable whose information level matches the scientific question.}
}
$$

The status after Report v2 is:

```text
EXPERIMENT2_COMPUTATION = COMPLETE_AND_INDEPENDENTLY_REPRODUCED
EXPERIMENT2_INTERPRETATION = REVISED_AFTER_ADVERSARIAL_REVIEW
EXPERIMENT2_FORMAL_SCIENTIFIC_CLOSURE = PENDING_CLOSURE_REPORT
EXPERIMENT3_STATUS = NOT_DECIDED_IN_THIS_REPORT
```

Nothing in this report validates the Alpöge–Furman theorem, replaces analytic proof, identifies the Gaussian toy with Weil's Hermitian form, or constitutes evidence for or against RH.

---

# 16. Reproducibility map

## 16.1 Frozen primary package

- `00_preregistration/Project_Montecito_Project_Specifications_v0.6.md` — scientific baseline.
- `00_preregistration/experiment2_config_v1_frozen.json` — frozen design and input hashes.
- `00_preregistration/block_manifest_v1.csv` — exact nested block indices.
- `01_inputs/` — six frozen Experiment 1 input artifacts.
- `02_results/block_matrix_metrics.csv` — one row per dataset/location/block size.
- `02_results/inertia_profiles_all_blocks.csv` — every block/$\lambda$ inertia and bound result.
- `02_results/C_spectra_and_crossings.csv` — every Gram eigenvalue and crossing threshold.
- `02_results/inertia_profile_summary_by_location.csv` — descriptive location summaries.
- `02_results/block_metric_summary.csv` — pair-functional reconstruction summaries.
- `02_results/full_dataset_pair_bridge_checks.csv` — full-sample Gaussian pair-functional calculations.
- `02_results/nested_scale_sensitivity_summary.csv` — nested block-size audit.
- `02_results/direct_H_eigendecomposition_checks.csv` — selected direct-$H$ checks.
- `02_results/numerical_integrity_summary.json` — numerical QA summary.
- `02_results/analytic_gaussian_tail_budget.csv` — explicit tail bounds.
- `src/experiment2_run.py` — primary computational pipeline.
- `src/verify_experiment2.py` — frozen verification suite.
- `src/make_figures.py` — figure-generation pipeline.
- `05_reproducibility/environment.json` — original Python/package versions.
- `05_reproducibility/verification_summary.json` — original 19-check result.
- `05_reproducibility/Experiment2_Artifact_Manifest_v1.csv` — artifact sizes and hashes.
- `05_reproducibility/SHA256SUMS_Experiment2_v1.json` — primary package SHA-256 map.

Primary archive used for closure:

```text
Project_Montecito_Experiment2_v1_FINAL.zip
SHA-256 c5df778e606ad94d55c84c5e14d741f7a4549a89964e922e07a08612c812175e
```

## 16.2 Validation Extension

- `01_results/independent_block_metrics_all_sigma.csv`;
- `01_results/independent_inertia_all_sigma.csv`;
- `01_results/independent_reproduction_differences.json`;
- `01_results/sigma_sensitivity_summary.csv`;
- `01_results/spectral_diagnostics_sigma1.csv`;
- `01_results/spectral_summary_sigma1.csv`;
- `03_report/Experiment2_Validation_Extension_v1.md`;
- `src/independent_validate.py`;
- `SHA256SUMS.json`.

Validation archive used for closure:

```text
Project_Montecito_Experiment2_Validation_v1.zip
SHA-256 7496200c5de6a3ea82e4f9ce1ec300ea7736d16f09142843466e9843464c1512
```

## 16.3 Review and closure-recheck record

- `Experiment2_Review_Corpus_Index_v1.md` — seven-document provenance index.
- `Experiment2_Peer_Review_Response_v1.md` — formal PR-01/PR-02 disposition.
- `Experiment2_Peer_Review_Response_v1_Support.zip` — closure scripts, outputs, and logs.

Closure support archive:

```text
SHA-256 8d304597e3ba4845e2c4efb516c6d34f67956124ac5617b92c8955d98d7a7c37
```

The support archive includes:

- `closure_recheck_summary.json`;
- `zeta_bridge_bin_width_scaling.csv`;
- `lattice_bridge_control.json`;
- `poisson_bridge_ensemble_200.csv`;
- `kernel_sensitivity_representative.csv`;
- captured primary and validation rerun logs;
- the closure-recheck script;
- internal checksums.

---

# 17. Next-step boundary

This document completes **Part 3 — `Experiment2_Report_v2.md`** of the Experiment 2 closure package.

It does not issue the formal closure certificate. The next planned artifact is:

`Experiment2_Closure_Report_v1.md`.

No Experiment 3 migration decision or successor computation is made here.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1 | 31 August 2026 | Original frozen Experiment 2 report |
| 2 | 2 September 2026 | Revised after independent validation, adversarial peer review, formal reconciliation, and targeted closure rechecks; frozen numerical results preserved, interpretations corrected |
