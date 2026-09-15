# Riemann Hypothesis Computation

**Reproducibility code and data for _A Computational Walk from Pair Correlation to Higher-Order Spectral Statistics of Zeta Zeros_.**

This repository contains three reproducible computational experiments:

1. **Experiment 1 — pair-correlation baseline.** Measures the finite-height evolution of local two-point statistics in three samples of Riemann-zeta zeros.
2. **Experiment 2 — first Hermitian instrument.** Applies a Gaussian Gram matrix and shifted Hermitian family, then identifies the information ceiling of its principal observables.
3. **Experiment 3 — bounded sinc-kernel study.** Computes second through fourth spectral moments, an exact collision decomposition, and lattice/CUE/Poisson/homometric controls. The historical research archive labels this bounded release Experiment 3BS.

The repository accompanies a finite computational study. It does not prove or disprove the Riemann Hypothesis, verify the theorem-level arguments of Alpöge--Furman or Lamzouri, or establish a new higher-order law for zeta zeros.

## Repository URL

Canonical repository: `https://github.com/sergepaulc/Riemann-Hypothesis-Computation`

Release: **v1.0.1**

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/verify_repository.py
python scripts/smoke_test.py
```

Reproduce one experiment in an isolated `build/` directory:

```bash
python scripts/reproduce.py --experiment 1
python scripts/reproduce.py --experiment 2
python scripts/reproduce.py --experiment 3
```

## Structure

```text
paper/                       repository-linked manuscript and figure sources
experiments/experiment1/     pair-correlation computation and frozen artifacts
experiments/experiment2/     Gaussian Hermitian computation, validation, closure
experiments/experiment3/     corrected bounded Experiment 3 release and tests
data/                        raw-source downloader and checksum catalogue
docs/                        paper-to-code map, reproducibility, status, governance
scripts/                     verification, isolated reproduction, finalization
manifests/                   release-level SHA-256 records
```

## Code and data availability

All code, derived inputs, frozen configurations, machine-readable results, figures, scientific reports, tests, and checksum manifests required for the paper's computations are included. Raw third-party Odlyzko tables are not redistributed; use:

```bash
python data/download_odlyzko_tables.py zeros1 zeros3 zeros4
```

The downloader fetches from the authoritative source and fails if a SHA-256 fingerprint differs from the exact source file used for provenance.

## Documentation

- [Paper-to-code map](docs/PAPER_TO_CODE.md)
- [Reproducibility guide](docs/REPRODUCIBILITY.md)
- [Project status](docs/PROJECT_STATUS.md)
- [GitHub publishing instructions](docs/GITHUB_PUBLISHING.md)
- [Current manuscript draft](paper/Project_Montecito_Paper_v1_9.md)

## License and citation

Original code and documentation are released under the MIT License. Third-party data are excluded from that grant; see [NOTICE.md](NOTICE.md). Citation metadata are in [CITATION.cff](CITATION.cff).

## Historical naming

The internal research project and many frozen artifacts were historically named **Project Montecito**. Those immutable filenames and records are preserved for provenance. The public GitHub repository is named **Riemann-Hypothesis-Computation**.
