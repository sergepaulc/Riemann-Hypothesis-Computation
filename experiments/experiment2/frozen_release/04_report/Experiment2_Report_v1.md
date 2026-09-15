# Project Montecito - Experiment 2 Report - Version 1

## Indefinite Hermitian Apparatus on Frozen Zeta Point Configurations

**Specification:** Project Montecito v0.6  
**Experiment status:** **COMPLETED - Stages A, B, and C**  
**Primary input:** frozen unfolded first 10,000 zeta zeros from Experiment 1  
**Secondary controls:** zeta samples near zero numbers $10^{12}$ and $10^{21}$  
**Primary kernel:** Gaussian, $\sigma=1$  
**Block sizes:** $m\in\{128,256,512\}$  
**Locations:** 16 preregistered common nested locations  
**$\lambda$ grid:** $0.10,0.15,\ldots,0.95$

---

# Executive summary

Experiment 2 successfully built and tested the preregistered toy Hermitian apparatus

$$
C_{ij}=\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right],
\qquad
H_\lambda=I-\lambda C,
$$

on the frozen zeta point configurations.

The main findings are:

1. **The Experiment 1 -> Experiment 2 pair-correlation bridge works quantitatively.** For the primary first-10,000 dataset, the frozen empirical pair-correlation curve predicts the Gaussian Gram second moment to better than $0.05\%$ on the full dataset and to well below $1\%$ at the individual-block level. At $m=512$, the mean normalized off-diagonal energy is $D_C=0.918209$ from the points and $D_C=0.919679$ from the pair-correlation prediction.

2. **The known finite-height effect from Experiment 1 propagates into the Gaussian-weighted second moment.** For the complete 10,000-point samples,

$$
D_C:=\frac{\|C\|_F^2}{N}-1
$$

moves from 0.920167 for the first 10,000 zeros to 0.945814 near $10^{12}$ and 0.951435 near $10^{21}$. The asymptotic GUE weighted benchmark for this Gaussian kernel is

$$
D_C^{\mathrm{GUE}}
=2\int_0^\infty e^{-u^2}
\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]du
=0.952040560.
$$

The $10^{21}$ sample lies within about 0.064% of that benchmark. No convergence rate is inferred from three height regimes.

3. **The toy matrix has a stable nontrivial inertia profile.** For primary $m=512$ blocks, all eigenvalues of $H_\lambda$ are positive through $\lambda=0.30$; negative directions appear on the frozen grid at $\lambda=0.35$. The mean positive fraction then decreases smoothly, reaching approximately $0.777$ at $\lambda=0.50$, $0.670$ at $\lambda=0.70$, $0.653$ at $\lambda=0.75$, and $0.597$ at $\lambda=0.95$

4. **The generic trace/Frobenius positive-inertia bound is valid but becomes very loose.** At $m=512$, the mean bound is about $0.521$ at $\lambda=0.50$, $0.167$ at $\lambda=0.70$, $0.108$ at $\lambda=0.75$, and only $0.003$ at $\lambda=0.95$, while the observed positive fraction remains near $0.60$. Thus the first two matrix moments are sufficient to generate a rigorous lower bound but do not closely determine the full inertia of this toy family over much of the grid.

5. **Numerical and finite-window audits passed.** Across 144 matrices and 2,592 block/$\lambda$ evaluations, there were no numerically unresolved signs. The closest grid eigenvalue to zero was 2.516e-06, more than four orders of magnitude outside its screening scale. Direct eigendecomposition checks agreed with the spectrum-first construction to at most 2.487e-14.

These results complete Experiment 2 under specification v0.6 and make the fixed apparatus ready for Experiment 3. They do **not** validate the Alpöge-Furman Weil-form argument and do not constitute evidence for RH.

---

# 1. Purpose and frozen design

Experiment 2 is the apparatus stage of Project Montecito. Its purpose is not to approximate the true finite compression of Weil's Hermitian form. It is to construct one mathematically transparent, process-agnostic finite Hermitian family whose input is an unfolded point configuration and whose second moment has a direct two-point interpretation.

The design was frozen before spectra were examined. Sixteen $512$-point blocks were placed at evenly spaced index locations from 1-512 through 9489-10000. The $256$- and $128$-point blocks were then nested concentrically inside each $512$-point block, preserving the same midpoint. This gives 48 blocks per dataset and 144 block matrices across the primary sample and two secondary controls.

The exact block indices, input SHA-256 hashes, $\lambda$ grid, kernel, screening rule, and direct-check locations are stored in `00_preregistration/experiment2_config_v1_frozen.json` and `00_preregistration/block_manifest_v1.csv`.

---

# 2. Mathematical construction

For a block

$$
X=\{x_1,\ldots,x_m\},
$$

the primary kernel is

$$
k(u)=e^{-u^2/2},
$$

and the full dense Gram matrix is

$$
C_{ij}=k(x_i-x_j)=e^{-(x_i-x_j)^2/2}.
$$

The Gaussian kernel is positive definite, so for distinct points $C$ is mathematically positive definite. Also

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

are the eigenvalues of $C$, then exactly

$$
\eta_j(H_\lambda)=1-\lambda\mu_j.
$$

Therefore the sign crossings occur when

$$
\lambda=\frac1{\mu_j},
$$

and a single eigendecomposition of $C$ determines the complete $H_\lambda$ inertia profile.

The trace and Frobenius identities used as independent checks are

$$
\operatorname{tr}H_\lambda=m(1-\lambda),
$$

and

$$
\|H_\lambda\|_F^2
=m(1-2\lambda)+\lambda^2\|C\|_F^2.
$$

Because $\lambda<1$, the trace is positive on the complete preregistered grid.

---

# 3. Positive-inertia bound

For a Hermitian matrix $H$ with $\operatorname{tr}H>0$, write

$$
r=n_{\mathrm{pos}}(H)
$$

and let its positive eigenvalues be $\alpha_1,\ldots,\alpha_r$. Negative eigenvalues can only lower the total trace, so

$$
\operatorname{tr}H
\le
\sum_{j=1}^{r}\alpha_j.
$$

Cauchy-Schwarz gives

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
n_{\mathrm{pos}}(H)\ge
\frac{\operatorname{tr}(H)^2}{\|H\|_F^2}
}
$$

and the normalized bound used here is

$$
b_{\mathrm{pos}}(\lambda)
=
\frac1m\frac{\operatorname{tr}(H_\lambda)^2}{\|H_\lambda\|_F^2}.
$$

The bound was checked against every computed resolved positive count; there were no violations.

---

# 4. Pair-correlation -> Frobenius bridge

The Gram second moment is

$$
\|C\|_F^2
=m+\sum_{i\ne j} e^{-(x_i-x_j)^2}.
$$

Thus

$$
D_C:=\frac{\|C\|_F^2}m-1
$$

is exactly the normalized off-diagonal Gaussian Gram energy.

For a block of span $L=x_m-x_1$, Experiment 2 uses the same finite-window translation-edge convention as Experiment 1. With

$$
\widehat{\rho^2}
=
\frac{m(m-1)}{L^2},
$$

and the frozen positive-separation empirical pair correlation $\widehat R_2(u)$, the predicted Gram second moment is

$$
\widehat{\|C\|_F^2}
=
m
+2\widehat{\rho^2}
\sum_k
\widehat R_2(u_k)
\int_{a_k}^{b_k}
(L-u)e^{-u^2}du,
$$

where $[a_k,b_k]$ is the $k$th $0.1$-wide Experiment-1 bin, truncated only at $U_{\max}=30$ and the block span.

For $\sigma=1$ the bin integral is evaluated analytically:

$$
\int_a^b(L-u)e^{-u^2}du
=
\frac{L\sqrt\pi}2\bigl(\operatorname{erf}b-\operatorname{erf}a\bigr)
+
\frac12\bigl(e^{-b^2}-e^{-a^2}\bigr).
$$

No Gaussian matrix entries are truncated. Only the frozen pair-correlation artifact stops at $u=30$. The omitted ordered-pair contribution is bounded by

$$
m(m-1)e^{-900},
$$

which for $m=512$ equals approximately

$$
3.57\times10^{-386}.
$$

It is therefore irrelevant even relative to double precision.

---

# 5. Numerical methodology and sign resolution

For every block:

1. construct the full Gaussian matrix $C$;
2. verify symmetry and unit diagonal;
3. diagonalize $C$ once with a symmetric eigensolver;
4. record all $\mu_j(C)$ and crossing thresholds $1/\mu_j$;
5. derive all 18 $H_\lambda$ spectra from $1-\lambda\mu_j$;
6. apply the screening scale
   $$
   \varepsilon_{\mathrm{screen}}
   =10^{-10}\max(1,\|H_\lambda\|_2);
   $$
7. escalate any value inside the screening band to higher precision, otherwise retain its resolved sign;
8. independently diagonalize selected $H_\lambda$ matrices at locations 1, 8, and 16 for all three block sizes and $\lambda\in\{0.10,0.50,0.95\}$;
9. verify the trace and Frobenius identities;
10. compare the points-in Gram second moment with the pair-correlation prediction.

No case entered the high-precision escalation path: all signs were comfortably resolved on the frozen grid.

Location variability and block-size variability are reported descriptively. They are **not** treated as exchangeable-sample inferential standard errors.

---

# 6. Numerical integrity results

The implementation passed all preregistered checks.

| Check | Result |
|---|---:|
| Block matrices analyzed | 144 |
| Block/$\lambda$ evaluations | 2592 |
| Numerically unresolved sign assignments | 0 |
| Maximum symmetry error in $C$ | 0.0e+00 |
| Maximum diagonal error in $C$ | 0.0e+00 |
| Minimum eigenvalue of any $C$ block | 9.421e-05 |
| Blocks failing PSD tolerance | 0 |
| Maximum $\|C\|_F^2$ spectral identity error | 5.684e-13 |
| Maximum trace identity error | 1.137e-13 |
| Maximum $\|H\|_F^2$ identity error | 3.411e-13 |
| Maximum selected direct-$H$ spectrum error | 2.487e-14 |
| Closest frozen-grid $H$ eigenvalue to zero | 2.516e-06 |
| $m=512$ Gaussian tail bound | $3.57\times10^{-386}$ |

The smallest sign margin on the grid was about $1.49\times10^4$ times its screening threshold, so the absence of unresolved signs is not marginal.

---

# 7. Primary result A - pair correlation predicts the Gram second moment

For the first-10,000 primary sample, the 16-location block averages are:

| $m$ | points-in $D_C$ mean | location SD | predicted $D_C$ mean | points - prediction | mean relative Frobenius error |
|---:|---:|---:|---:|---:|---:|
| 128 | 0.911447 | 0.005052 | 0.914656 | -0.003209 | -0.1683% |
| 256 | 0.917196 | 0.004797 | 0.918541 | -0.001345 | -0.0706% |
| 512 | 0.918209 | 0.004610 | 0.919679 | -0.001470 | -0.0771% |

At $m=512$, the mean pair-correlation prediction differs from the direct points-in value by only 0.001470 in $D_C$. The individual-block maximum relative Frobenius discrepancy is 0.807%, while the mean signed relative discrepancy is -0.077%.

The full 10,000-point calculation provides an additional bridge check without constructing a dense $10,000\times10,000$ matrix. Pair distances up to $u=30$ are accumulated directly using the Gaussian weight; the omitted tail is negligible. For the primary sample,

$$
D_C^{\mathrm{direct}}=0.920166507,
\qquad
D_C^{R_2}=0.920974609,
$$

with a relative Frobenius discrepancy of only 0.0421%.

**Interpretation.** For this toy matrix and kernel, the second moment is almost completely recovered from the frozen averaged two-point statistic at the measured resolution. This is the strongest direct validation of the intended Experiment 1 -> Experiment 2 bridge.

![Primary pair-correlation/Frobenius bridge](03_figures/03_primary_pair_correlation_frobenius_bridge.png)

---

# 8. Primary result B - nontrivial and stable inertia

For the primary $m=512$ blocks:

| $\lambda$ | mean $p_{\mathrm{pos}}$ | location SD | mean $p_{\mathrm{neg}}$ | mean $b_{\mathrm{pos}}$ | mean bound slack |
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

All primary blocks are positive definite through $\lambda=0.30$. The first negative directions on the preregistered grid appear at $\lambda=0.35$. From there the positive fraction decreases smoothly rather than collapsing: it is still about $0.60$ at $\lambda=0.95$.

This behavior is exactly auditable from the spectrum of $C$: increasing $\lambda$ moves the threshold $1/\lambda$ downward through the fixed $C$ spectrum.

![Primary inertia and lower bound](03_figures/01_primary_inertia_and_bound_m512.png)

---

# 9. Primary result C - the trace/Frobenius bound is not an inertia predictor

The generic lower bound behaves very differently from the actual positive fraction. It is fairly informative at small $\lambda$, when the trace is large and nearly all directions are positive. But because

$$
\operatorname{tr}H_\lambda=m(1-\lambda),
$$

the numerator of the bound shrinks quadratically as $\lambda\to1$, while the observed positive fraction remains substantial.

For $m=512$:

- at $\lambda=0.50$: $p_{\mathrm{pos}}\approx0.777$ versus $b_{\mathrm{pos}}\approx0.521$;
- at $\lambda=0.70$: $p_{\mathrm{pos}}\approx0.670$ versus $b_{\mathrm{pos}}\approx0.167$;
- at $\lambda=0.75$: $p_{\mathrm{pos}}\approx0.653$ versus $b_{\mathrm{pos}}\approx0.108$;
- at $\lambda=0.95$: $p_{\mathrm{pos}}\approx0.597$ versus $b_{\mathrm{pos}}\approx0.003$.

Thus, in this toy apparatus, **knowing trace and Frobenius second moment well is not enough to closely determine inertia**. The bound remains mathematically correct; it simply carries much less information than the full spectrum over much of the parameter range.

This is an important limiting result rather than a failure of the experiment.

![Bound slack](03_figures/06_primary_positive_bound_slack_m512.png)

---

# 10. Finite-window and scaling stability

The positive-inertia profile is stable across the preregistered block sizes.

For the primary sample, the largest mean absolute difference between nested $m=128$ and $m=512$ positive fractions is 0.007202, occurring at $\lambda=0.40$. The largest single-location nested difference is 0.023438, also near the onset region ($\lambda=0.40$).

For $m=512$, the largest descriptive standard deviation across the 16 locations is 0.007436, occurring at $\lambda=0.40$. Away from the first crossing region, location variation is generally smaller.

These numbers support the use of local blocks as a stable finite-window toy observable. They do not imply an infinite-size limit.

![Block-size stability](03_figures/02_primary_positive_inertia_by_block_size.png)

![Location variability](03_figures/07_primary_location_variability.png)

---

# 11. Secondary high-height zeta controls

The high-height controls were run using the same frozen block indices and the same apparatus. They were not substituted for the primary sample.

## 11.1 Gaussian-weighted second moment

| zeta sample | direct $D_C$ | $R_2$ prediction | relative bridge error | direct minus GUE benchmark | relative deviation from GUE benchmark |
|---|---:|---:|---:|---:|---:|
| first 10,000 | 0.920167 | 0.920975 | 0.0421% | -0.031874 | -3.348% |
| near $10^{12}$ | 0.945814 | 0.946631 | 0.0420% | -0.006227 | -0.654% |
| near $10^{21}$ | 0.951435 | 0.953012 | 0.0808% | -0.000605 | -0.064% |

The Experiment-1 finite-height phenomenon therefore appears in a second, independently weighted two-point observable: the low-height sample has a Gaussian Gram energy about $3.35\%$ below the asymptotic GUE weighted benchmark, while the $10^{21}$ sample is within about $0.064\%$.

This is consistent with Experiment 1's conclusion that the large low-height short-range distortion is a finite-height effect. No monotone convergence law or rate is inferred.

![Full-data weighted second moment across height](03_figures/08_full_dataset_Dc_vs_GUE_benchmark.png)

## 11.2 Inertia across height

For $m=512$ the mean positive fractions are:

| $\lambda$ | first 10,000 | near $10^{12}$ | near $10^{21}$ |
|---:|---:|---:|---:|
| 0.35 | 0.998657 | 0.973267 | 0.970093 |
| 0.50 | 0.776978 | 0.781006 | 0.781250 |
| 0.70 | 0.669678 | 0.672729 | 0.673950 |
| 0.90 | 0.607178 | 0.613525 | 0.613403 |
| 0.95 | 0.596558 | 0.600586 | 0.600952 |

The largest height-dependent difference occurs near the **first spectral crossing** at $\lambda=0.35$: the low-height configuration remains almost entirely positive, whereas the high-height controls have already acquired about $2.7$-$3.0\%$ negative directions. This is explained by the upper edge of the $C$ spectrum: the low-height blocks have a smaller maximum kernel eigenvalue, hence a later first crossing.

For $\lambda\ge0.40$, however, the three mean inertia curves are strikingly close. For $m=512$ the low-height versus high-height differences are generally only a few tenths of a percentage point, with the largest later-grid difference about $0.6\%$ near $\lambda=0.90$.

**Interpretation.** The known Level-1 finite-height distortion has a clear effect on the Gaussian second moment and on the onset of negative directions, but it does **not** produce a large persistent separation of the full inertia profiles under this primary toy apparatus.

![High-height inertia controls](03_figures/05_zeta_height_controls_positive_inertia_m512.png)

---

# 12. What Experiment 2 establishes

Experiment 2 establishes the following computational facts for the frozen v0.6 apparatus:

1. The Gaussian points-in construction produces positive-definite Gram matrices and a nontrivial indefinite $H_\lambda$ regime with stable inertia profiles.
2. The spectrum-first identity provides an exact and numerically well-resolved map from the Gram spectrum to the complete preregistered inertia profile.
3. The Experiment-1 empirical pair-correlation artifact predicts the Gaussian Gram Frobenius second moment with very high accuracy.
4. The low-height zeta finite-height effect propagates to this Gaussian-weighted second moment and becomes much smaller in the high-height controls.
5. The generic trace/Frobenius positive-inertia bound is valid but increasingly loose; second-moment information alone does not closely specify the toy inertia.
6. Local-block and nested-scale dependence is small enough that the primary apparatus is suitable for controlled process replacement in Experiment 3.

---

# 13. What Experiment 2 does not establish

Experiment 2 does **not** establish:

- any new statement about the location, simplicity, or multiplicity of zeta zeros;
- any numerical validation of the Alpöge-Furman theorem;
- any identification of $H_\lambda$ with the finite Weil/Bombieri Hermitian form;
- any evidence for the Riemann Hypothesis;
- that pair correlation uniquely determines inertia;
- that the observed block-size stability proves an infinite-size limit;
- that the small high-height differences are higher-order effects.

The last point is especially important: Experiment 3 must compare point processes under the same frozen apparatus and must report Level-1 differences before interpreting Level-2 inertia differences.

---

# 14. Experiment 2 closure decision

All Stage A-C criteria in specification v0.6 have been satisfied:

- pre-registration was written before spectra were examined;
- the frozen first-10,000 point set remained primary;
- $C$ was PSD on every block to numerical resolution;
- the spectrum-first and direct-$H$ routes agreed;
- trace and Frobenius identities agreed;
- the pair-correlation/Frobenius bridge agreed quantitatively;
- all signs were resolved without hidden zero assignments;
- block location and nested block-size sensitivity were audited;
- the Gaussian $u>30$ tail was bounded explicitly.

Therefore:

`SCIENTIFIC_EXPERIMENT2_COMPLETE = TRUE`

`COMPUTATIONAL_EXPERIMENT3_READY = TRUE`

The apparatus should now be frozen before synthetic GUE, Poisson, or lattice configurations are passed through it.

---

# Reproducibility map

- `00_preregistration/experiment2_config_v1_frozen.json` - frozen design and hashes.
- `00_preregistration/block_manifest_v1.csv` - exact nested block indices.
- `01_inputs/` - frozen Experiment-1 inputs used by this run.
- `02_results/block_matrix_metrics.csv` - one row per dataset/location/block size.
- `02_results/inertia_profiles_all_blocks.csv` - all block/$\lambda$ inertia and bound results.
- `02_results/C_spectra_and_crossings.csv` - every Gram eigenvalue and crossing threshold.
- `02_results/inertia_profile_summary_by_location.csv` - descriptive location summaries.
- `02_results/block_metric_summary.csv` - second-moment bridge summaries.
- `02_results/full_dataset_pair_bridge_checks.csv` - full-10,000 weighted bridge calculation.
- `02_results/nested_scale_sensitivity_summary.csv` - nested block-size audit.
- `02_results/direct_H_eigendecomposition_checks.csv` - independent direct-$H$ checks.
- `02_results/numerical_integrity_summary.json` - numerical QA summary.
- `02_results/analytic_gaussian_tail_budget.csv` - explicit tail bounds.
- `src/experiment2_run.py` - complete computational pipeline.
- `src/make_figures.py` - figure-generation pipeline.
- `05_reproducibility/environment.json` - Python/package versions.
