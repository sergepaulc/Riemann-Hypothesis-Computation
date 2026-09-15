# Review — Experiment 1 High-Height Replication (v1)

Third reviewer pass. This package shipped the **raw Odlyzko files**, so unlike the
previous round I was able to replicate the entire chain end to end: raw text →
arbitrary-precision ordinate reconstruction → independent θ-unfolding →
pair-correlation pipeline → every reported statistic.

**Verdict: the experiment is correct, the replication is exact, and the
conclusion is sound. This is the decisive result for Experiment 1. I found one
confound the report does not address — which I tested, and which does not
overturn anything — plus three points where the claims can be stated more
precisely.**

---

## 1. Full independent replication

SHA-256 of both raw files matches the report exactly:

```
75a1f1a9…64807  zeros3.txt
10d9f7da…2da8f  zeros4.txt
```

Parsing: 10,009 lines each = 9 header + **10,000** data. Offsets strictly
increasing; 10 decimals in `zeros3`, 8 in `zeros4`. Reconstructed first
ordinates match the file headers exactly:
`267653395648.8475231278` and `144176897509546973538.4981`.

I re-unfolded from scratch using `x_n = (θ(γ_n) − θ(γ₁))/π` at 40–50 decimal
digits, having first confirmed that the asymptotic θ-series agrees with
`mpmath.siegeltheta` to **0.0** at both heights (dps 50).

| statistic | report | my value | status |
|---|---:|---:|---|
| mean spacing, 10¹² | 1.000108698 | 1.000108698 | exact |
| mean spacing, 10²¹ | 0.999969908 | 0.999969908 | exact |
| `D₀.₅` first 10⁴ | 22.40% | 22.40% (878 / 1131.46) | exact |
| `D₀.₅` near 10¹² | 1.62% | 1.62% (1113 / 1131.36) | exact |
| `D₀.₅` near 10²¹ | −3.67% | −3.67% (1173 / 1131.52) | exact |
| matched 10-block `D` | 0.22387 / 0.01764 / −0.03713 | 0.22388 / 0.01764 / −0.03712 | exact |
| RMSE `0<u<1` | 0.05951 / 0.01715 / 0.02149 | identical | exact |
| RMSE `0<u<5` | 0.03711 / 0.02275 / 0.02996 | identical | exact |
| `S₃₀` | −0.507158 / −0.494109 / −0.507531 | −0.507157 / −0.494109 / −0.507531 | exact |
| block mean/sd/#pos/min/max | all three rows | identical | exact |

**Every published number reproduces.** Shipping the raw inputs is what made this
possible, and it is a marked improvement over the previous package (which shipped
none of its six claimed CSVs). Please keep doing this.

## 2. Precision handling — correct

The report's precision analysis checks out. Source accuracy propagates to
unfolded units through the local density `ρ = (1/2π)log(γ/2π)`:

- `10¹²`: `1e-8 × 3.8953 = 3.90e-8`
- `10²¹`: `1e-6 × 7.0951 = 7.10e-6`

Both are 4–6 orders below the `Δu = 0.1` bin width, so neither can affect
`D₀.₅`. (The quoted densities are the *theoretical* `ρ`; my empirical mean-gap
densities are 3.8949 and 7.0953. Consistent — worth labelling which is which.)

The decision to keep the offsets as text and reconstruct in arbitrary precision
was necessary, not fastidious: at `γ ≈ 1.44e20`, `θ(γ) ≈ 3.1e21`, so recovering
`x`-differences of order 1 to six decimals needs ~28 significant digits. Plain
`float64` would have destroyed the sample. The report is right to flag this and
right about the remedy.

## 3. The confound the report does not address — and its resolution

**At high height the unfolding is effectively affine; at low height it is
strongly nonlinear.** Across `zeros3` the density varies by ~1 part in 10⁸, and
across `zeros4` similarly; across the first 10,000 zeros it varies by a factor of
**3.6** (`L` runs 0.81 → 7.36). So the three-sample comparison changes *two*
things at once: the height, and how much work the unfolding map is doing.

A referee will raise this: is the 22.4% a finite-height effect, or an artifact of
unfolding a strongly non-stationary stretch by a global smooth function? The
Validation Extension's θ-vs-RvM test does **not** answer it, because both maps are
the same nonlinear map to within `1/(48πT)`.

I tested it directly, by restricting the low-height sample to tails where the
density is nearly constant:

| subsample | γ range | density ratio | `D₀.₅` | z |
|---|---|---:|---:|---:|
| last 5000 | 5,449–9,878 | 1.088 | +0.206 ± 0.037 | +5.5 |
| last 2500 | 7,709–9,878 | 1.035 | +0.173 ± 0.054 | +3.2 |
| last 1000 | 9,020–9,878 | 1.012 | +0.258 ± 0.081 | +3.2 |

**The deficit survives where the unfolding is essentially affine.** So it is a
property of the zeros at low height, not of the unfolding geometry. This closes
the confound and should be added to the report — it costs three lines and removes
the strongest available objection.

## 4. Where the claims can be sharpened

**(a) State the detection threshold, not just "compatible with GUE".** The frozen
ensemble has `sd = 0.0248`, and each high-height sample is a single draw. So the
experiment establishes

    |D₀.₅| ≲ 0.05  (2σ)  at both 10¹² and 10²¹,

**not** `D₀.₅ = 0`. The honest headline is that the anomaly fell from 22.4% to
below a ~5% detection floor — a factor of ≥4.5 suppression — rather than that it
vanished. That is still decisive, and it is more defensible.

**(b) Quantify the sign test.** The report notes 10/10 low-height blocks are
positive but gives no p-value. It is worth having, because it is assumption-free
and does not depend on the GUE ensemble at all:

| sample | positive blocks | two-sided sign test |
|---|---:|---:|
| first 10⁴ | 10/10 | **p = 0.0020** |
| near 10¹² | 7/10 | p = 0.34 |
| near 10²¹ | 3/10 | p = 0.34 |

**(c) Block SDs are estimated from ten values.** The `10²¹` block sd (0.106) is
nearly double the other two (0.057 each). With n = 10 the relative SE of an sd is
≈ 24%, so 0.106 vs 0.057 is only ≈1.7σ — not a finding. Worth a footnote so it is
not over-read. Note also that 0.057 sits *below* the naive Poisson block scale
(`√113/113 ≈ 0.094`), consistent with a rigid process, while 0.106 sits above it;
both are within noise of the same underlying value.

## 5. On declining to fit a rate — right call, with one observation worth recording

The report explicitly refuses to fit `1/log T` from three points. That is correct
and I would not change it. But one arithmetic observation is worth recording as a
*prediction for future work*, clearly labelled as not a fit:

| law calibrated on the low-height point | predicts at 10¹² | predicts at 10²¹ |
|---|---:|---:|
| `c/L` | +0.062 | +0.034 |
| `c/L²` | **+0.0171** | +0.0052 |
| **observed** | **+0.0176** | −0.0371 |

A pure `1/L` law calibrated on the low-height sample over-predicts the `10¹²`
value by ≈1.8σ of the ensemble; `1/L²` lands on it almost exactly. I would **not**
claim this: the low-height sample has no well-defined single `L` (it spans
0.81–7.36, and I used the median 6.77), there are three points, and the `10²¹`
point carries ±2.5%. But it is a cheap, falsifiable statement to have on record,
and it points at the right next measurement — an *intermediate* height, where
`1/L` and `1/L²` differ by a factor of ~2.

## 6. Methodology points that are simply right

- **Reusing the frozen 200-replicate ensemble** rather than regenerating it is
  good practice: it was pre-registered before the high-height files arrived, so
  there is no forking-paths exposure. (I independently confirmed that ensemble
  last round with 400 replicates of my own: mean −0.00097, sd 0.02571 against
  their 0.00156 / 0.02480.)
- **Freezing the analysis plan before the files were supplied**, and saying so.
- **Treating `zeros4` as a secondary replication** because of Odlyzko's explicit
  "not guaranteed" caveat, rather than averaging it in with equal weight.
- **Using θ-unfolding uniformly across all three samples.** Note for the record
  that this makes the first-10⁴ row directly comparable to the original artifact:
  I get 22.40% from the RvM-unfolded CSV and the report gets 22.40% from θ, which
  is exactly what the Validation Extension predicted.
- **Not starting Experiment 2**, and saying so.

## 7. Bottom line

The finite-height explanation is now established as far as this data can
establish it. The chain is complete and each link is verified:

1. the low-height deficit is real (z ≈ 9 against a matched ensemble, p < 1/601 by
   enumeration, and p = 0.002 by an assumption-free sign test);
2. it is not an estimator artifact (GUE and CUE controls, both rounds);
3. it is not an unfolding artifact — neither of the smooth-counting-function
   choice (Validation Extension) nor of unfolding nonlinearity (§3 above);
4. it drops below a ~5% detection floor at 10¹² and stays there at 10²¹.

The one substantive change I would make to the report is to add §3, since it is
the objection a referee is most likely to raise and the answer is already in the
data. Everything else is refinement of wording.

For Experiment 2 the migration rule is unchanged but now has a cleaner
justification: the first-10⁴ artifact carries a *known, quantified, and
explained* Level-1 distortion of `D₀.₅ = 0.224`, which is a finite-height
property of that particular sample rather than a property of zeta zeros. When the
Level-2 inertia comparison is run, the high-height samples are the better zeta
reference for "what GUE-like zeta looks like", and the first 10⁴ is the better
reference for "what this specific frozen point set does".
