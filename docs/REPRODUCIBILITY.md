
# Reproducibility guide

## Environment

The frozen computations used Python 3.13.5 with the versions pinned in
`requirements.txt`. Equivalent recent Python 3.11+ environments should work,
but the versioned release records the exact original package versions.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verify the delivered repository

```bash
python scripts/verify_repository.py
python scripts/smoke_test.py
```

## Reproduce

```bash
python scripts/reproduce.py --experiment 1
python scripts/reproduce.py --experiment 2
python scripts/reproduce.py --experiment 3
```

or:

```bash
make reproduce-all
```

Each run is copied to `build/` before execution. The committed frozen evidence
is never used as a writable output directory.

## Expected scale

- Experiment 1 public reproduction: seconds.
- Experiment 2 primary rerun and verification: typically minutes or less on a modern machine.
- Experiment 3 bounded study: approximately one minute in the recorded cloud environment, but hardware-dependent.

## Claim boundary

Successful reproduction validates the finite computations and their packaging.
It does not prove RH, validate the theorem-level Alpöge–Furman or Lamzouri
arguments, or establish a new higher-order law for zeta zeros.
