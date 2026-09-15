# Project Montecito — Experiment 1 High-Height Replication — Version 2

**Project:** Project Montecito  
**Parent experiment:** Experiment 1 — zeta-zero pair correlation  
**Revision basis:** third independent peer review  
**Experiment 2:** not started

## Executive revision summary

The third independent review reproduced the complete chain from raw Odlyzko text through arbitrary-precision reconstruction, theta unfolding, pair correlation, and every reported statistic. The reviewer found the experiment correct and the conclusion sound.

Version 2 makes one substantive methodological addition and three precision-of-language improvements:

1. closes a possible **nonlinear-unfolding confound** using nearly affine low-height tail subsamples;
2. replaces "the anomaly disappears" with the more defensible statement that it is **suppressed below an approximately 5% detection floor** at high height;
3. adds a descriptive block-sign consistency calculation while explicitly stating its assumptions;
4. warns against over-interpreting block-standard-deviation differences estimated from only ten blocks.

No raw input, unfolded point set, pair-correlation curve, or previously reported numerical statistic is changed.

---

# 1. What the third review independently verified

The reviewer reproduced the package end to end and confirmed:

- raw-file SHA-256 values;
- exactly 10,000 strictly increasing offsets in each Odlyzko file;
- arbitrary-precision ordinate reconstruction;
- theta unfolding;
- mean spacings;
- D0.5 at all three heights;
- matched-block D0.5 values;
- RMSE values;
- S30 values;
- block summary statistics.

This closes the reproducibility audit of the High-Height Replication.

---

# 2. Precision handling remains correct

The source-header precision maps to unfolded-coordinate uncertainty through the theoretical local smooth density

`rho(T) = log(T / (2*pi)) / (2*pi)`.

Theoretical densities used in the original report were approximately:

- 3.8953 zeros per gamma unit near 10^12;
- 7.0951 zeros per gamma unit near 10^21.

The reviewer's empirical mean-gap densities, 3.8949 and 7.0953, are consistent. Version 2 labels the former explicitly as **theoretical smooth densities**.

The decision to preserve large offsets as decimal text and reconstruct them with arbitrary precision remains essential.

---

# 3. New confound check: does nonlinear low-height unfolding create D0.5?

The reviewer raised the strongest remaining methodological objection:

> The high-height samples are almost stationary over their 10,000-zero windows, whereas the first-10,000 sample spans a strongly varying local density. Could the 22.4% deficit be created by applying a global smooth unfolding to a highly nonstationary low-height stretch?

This concern is distinct from the earlier theta-versus-Riemann-von-Mangoldt check. Both of those smooth maps are nearly identical, so that comparison does not test whether the **amount of nonlinearity across the low-height sample** is itself responsible.

We independently reproduced the reviewer's proposed tail test using theta-unfolded points.

| low-height subsample | gamma range | endpoint density ratio | D0.5 |
|---|---:|---:|---:|
| full first 10,000 | 14.1–9877.8 | 9.078 | 0.224 |
| last 5,000 | 5449–9878 | 1.088 | 0.206 |
| last 2,500 | 7709–9878 | 1.035 | 0.173 |
| last 1,000 | 9020–9878 | 1.012 | 0.258 |

The final 1,000-zero tail changes its theoretical local density by only about **1.25%**, yet its D0.5 point estimate is still **25.8%**.

Therefore:

> **The low-height close-pair deficit survives when the unfolding is nearly affine. It is not produced by the strong nonlinearity of unfolding the complete first-10,000 stretch.**

This closes the principal confound identified by the third review.

### Minor correction to the review itself

The review states that local density varies by a factor of 3.6 across the complete first-10,000 sample while also quoting `log(gamma/2pi)` from 0.81 to 7.36. Using its own density definition, the endpoint ratio is approximately **9.08**, not 3.6.

This arithmetic slip does not affect the reviewer's confound argument; it makes the full-window nonstationarity larger, while the nearly affine tail result still closes the concern.

---

# 4. Primary height result, stated at the experiment's resolution

The full-window point estimates remain:

| sample | D0.5 |
|---|---:|
| first 10,000 | 22.40% |
| near 10^12 | 1.62% |
| near 10^21 | -3.67% |

The frozen matched GUE ensemble has D0.5 SD approximately **0.0248**. A convenient two-SD detection scale is therefore about

`2 * SD = 0.0496`,

or roughly **5%**.

The matched high-height values are:

- near 10^12: **0.0176**
- near 10^21: **-0.0371**

Both lie within approximately two ensemble SD of the GUE mean.

The correct headline is therefore:

> **The 22.4% low-height anomaly is suppressed below the experiment's approximately 5% detection floor at both high heights.**

Relative to the low-height matched value, this establishes at least approximately a **4.5-fold suppression** at the resolution of this experiment.

It does **not** establish D0.5 = 0 exactly.

---

# 5. Block-sign consistency

The ten contiguous 1,000-zero blocks give:

| sample | positive D0.5 blocks / 10 | two-sided binomial sign value |
|---|---:|---:|
| first 10,000 | 10/10 | 0.0020 |
| near 10^12 | 7/10 | 0.3438 |
| near 10^21 | 3/10 | 0.3438 |

The 10/10 low-height sign consistency is a useful robustness diagnostic.

However, Version 2 does **not** call this test "assumption-free." A literal binomial sign-test interpretation assumes independent, equiprobable signs under the null. Contiguous zeta blocks are not proven independent or exchangeable.

Accordingly, the p-values above are reported as **descriptive conditional sign-consistency values**, not as the primary inference. The frozen matched-GUE ensemble remains the main calibration.

---

# 6. Block-SD caution

The block D0.5 standard deviations are approximately:

- first 10,000: 0.057;
- near 10^12: 0.057;
- near 10^21: 0.106.

Each SD is estimated from only ten blocks. The relative sampling uncertainty of an SD at n=10 is large, so the larger 10^21 value is **not treated as a finding**.

No conclusion is drawn from differences among these three block-SD estimates.

---

# 7. Sum-rule result is unchanged

The S30 values remain:

- first 10,000: **-0.507158**
- near 10^12: **-0.494109**
- near 10^21: **-0.507531**

They remain close to the sine-kernel value -1/2.

Thus the mass-versus-shape interpretation remains intact:

> **The low-height effect is primarily a redistribution of short-range pair-correlation mass, not a large change in total correlation-hole mass.**

---

# 8. Scientific conclusion after the third review

The evidence chain is now:

1. the low-height D0.5 distortion is reproducible;
2. matched GUE controls show that its magnitude is large relative to finite-sample GUE variation;
3. it is not created by the estimator;
4. it is not created by choosing one of two nearly identical smooth unfolding formulas;
5. **it is not created by the strong nonlinearity of unfolding the full low-height stretch**, because the deficit survives in nearly affine low-height tails;
6. at zero numbers near 10^12 and 10^21, the same statistic is suppressed below the experiment's approximately 5% detection scale.

The strongest defensible conclusion is:

> **Project Montecito finds a large, sample-specific low-height Level-1 distortion in the first 10,000 zeros. That distortion is strongly suppressed at vastly greater height and is no longer detectable above an approximately 5% D0.5 scale. The data therefore strongly support a finite-height origin, without claiming that the asymptotic correction is exactly zero or that its convergence rate has been measured.**

---

# 9. Prospective rate question — explicitly not a result

The third review notes that different simple decay laws can make different predictions at an intermediate height.

We agree that an intermediate-height sample could eventually distinguish candidate convergence behaviors. We **do not fit or select a decay law from the current three height regimes**.

This is recorded only as a prospective question for future work, not as evidence for a 1/log(T), 1/log(T)^2, or any other specific law.

---

# 10. Consequence for future Project Montecito work

The migration logic is clarified, not changed.

- The **first 10,000 zeros remain the frozen primary Experiment 1 point set** and should remain the primary input when Experiment 2 is explicitly studying that artifact.
- The high-height zeta samples are better controls for the question: **"What does GUE-like zeta look like at our current resolution?"**
- The first-10,000 sample is better for the question: **"What does this specific frozen finite-height point set do in the toy Hermitian apparatus?"**

A future Level-2 inertia difference obtained from the first-10,000 points must first be interpreted through their known Level-1 finite-height distortion.

No Experiment 2 computation is performed here.

---

# 11. Reproducibility additions in Version 2

Version 2 adds:

- `data/processed/low_height_affine_tail_check_v2.csv`
- `data/processed/D05_detection_floor_v2.csv`
- `data/processed/block_sign_consistency_v2.csv`
- `figures/low_height_affine_tail_check_v2.png`
- `figures/D05_detection_floor_v2.png`
- `report/Experiment1_High_Height_Replication_Peer_Review_Response_v2.md`
- the third peer review itself.

All Version 1 raw and processed numerical artifacts are preserved.
