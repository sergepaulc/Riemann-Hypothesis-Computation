# Experiment 1 — zeros1 Raw-Byte Provenance Closure — Version 2

## Status

**CLOSED. No remaining Experiment 1 raw-data provenance item is pending.**

The user downloaded the official Odlyzko `zeros1` plaintext table and attached the raw file unchanged for byte-level validation.

## Exact raw-file fingerprint

File: `zeros1.txt`

- SHA-256: `3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632`
- size: `1,800,000` bytes
- parsed data rows: `100,000`
- first value: `14.134725142`
- row 10,000: `9877.782654004`
- row 100,000: `74920.827498994`
- strictly increasing: `TRUE`
- every row has 9 decimal places: `TRUE`

## Full first-10,000 comparison against the frozen Experiment 1 sequence

All 10,000 official values were compared against the frozen `zeta_zeros_10000_validated.csv` sequence.

- maximum absolute ordinate difference: `2.912202035077e-09`
- mean absolute ordinate difference: `4.322567210835e-10`
- rows outside the Odlyzko approximately 3e-9 source-precision envelope: `0`
- location of maximum difference: zero index `5343`

The frozen sequence was originally regenerated numerically rather than copied from `zeros1`, so exact decimal-string identity is not expected. The correct provenance test is numerical agreement inside the official table's stated precision. All 10,000 rows pass that test.

## Downstream Experiment 1 invariance check

The official raw first-10,000 values were passed through the original Riemann–von Mangoldt smooth unfolding used by Experiment 1.

Relative to the frozen Experiment 1 unfolded coordinates:

- maximum absolute unfolded-coordinate difference: `3.292370820418e-09`
- mean absolute unfolded-coordinate difference: `4.574522789680e-10`

The complete pair-correlation histogram was then recomputed with the frozen `Umax=30`, `du=0.1` geometry.

- total pair count through u=30: `294,472` official vs `294,472` frozen
- bins whose count changed: `0 / 300`
- maximum absolute bin-count change: `0`
- pairs with u<0.5: `878` official vs `878` frozen

Therefore the official raw file produces **exactly the same 300-bin pair-count histogram** as the frozen Experiment 1 artifact.

## Decision

The raw-byte provenance gap is closed.

The original frozen Experiment 1 point set remains unchanged for historical and preregistration integrity. The official raw `zeros1.txt` is now stored alongside it as the source-provenance record.

No Experiment 1 scientific result requires revision.
