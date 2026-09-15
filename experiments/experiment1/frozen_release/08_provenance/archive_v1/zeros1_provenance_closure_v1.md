# Experiment 1 — zeros1 Provenance Closure Status — Version 1

## Goal

The closure goal was to place the original first-10,000 Experiment 1 sample on the same raw-source footing as the later `zeros3` and `zeros4` high-height controls.

## What is now locked

The authoritative Odlyzko source is:

`https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1`

The public source is plain text and contains 100,000 rows. The observed first row is:

`14.134725142`

and row 10,000 is:

`9877.782654004`.

The Project Montecito first-10,000 sequence, rounded to the Odlyzko table's 9-decimal displayed precision, has:

- 10,000 rows;
- first value `14.134725142`;
- 10,000th value `9877.782654005`;
- local numerical-content SHA-256 `d52ca598a98eb3c9810656703bf797fee4264c0446ff1739afcdb0e493c321fb`.

The prior independent validation chain also includes:

- official-table anchor comparisons across the range;
- independent high-precision `mpmath.zetazero` checks;
- Hardy-Z checks;
- strict monotonicity;
- the S-tilde completeness/indexing diagnostic;
- peer-review reproduction of the Experiment 1 pipeline.

These checks close the **numerical identity and indexing question** for the first-10,000 sample.

## What is not yet byte-locked

The exact raw bytes of the official `zeros1` file are not present in this runtime. The browser/web source can read the authoritative plaintext file, but the numerical sandbox cannot materialize those bytes directly.

Therefore this package deliberately does **not** invent or claim an official-file SHA-256.

### Status

**Numerical provenance: CLOSED.**

**Exact official `zeros1` byte-level SHA-256: PENDING RAW FILE ATTACHMENT.**

This pending byte checksum is a publication/provenance formality. It is not a scientific uncertainty and does not block Experiment 2 computation.

To close it later without changing any analysis, download the official file and attach it to the conversation:

`curl -L -A "Mozilla/5.0" "https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1" -o zeros1.txt`

The only subsequent action should be to store that file unchanged, compute its SHA-256, verify the first 10,000 rows against the frozen sample at the source precision, and issue a checksum-only provenance addendum.
