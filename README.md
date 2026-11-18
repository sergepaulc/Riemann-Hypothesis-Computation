# Riemann Hypothesis Computation

**Version 1.0 — Code, data, and research paper**

A computational investigation of pair correlations and spectral statistics of Riemann-zeta zeros. The repository contains three finite experiments, their numerical inputs and reference outputs, and checks of the calculations. It does not prove or disprove the Riemann Hypothesis.

## Read the paper
## Abstract

We study, through three reproducible experiments, how finite kernel-based spectral observables encode structure in unfolded Riemann-zeta zero configurations. Motivated by the 2026 quadratic and second-moment results of Alpöge--Furman and Lamzouri, we investigate a complementary finite question: which features of a zero configuration are retained by a chosen observable?

Experiment 1 measures pair correlation in three samples of $`10,000`$ zeros. The first sample contains $`22.4\%`$ fewer pairs below half a mean spacing than the sine-kernel prediction, while the same statistic lies within the matched finite-GUE resolution near zero numbers $`10^{12}`$ and $`10^{21}`$. Experiment 2 applies a Gaussian Hermitian family and proves that its trace is data-independent, whereas its Frobenius moment and elementary inertia bound depend only on one weighted pair statistic; the full inertia calculation did not isolate an additional residual. Experiment 3 studies core-anchored moments of a sinc-kernel matrix. An exact homometric example proves that the fourth moment distinguishes configurations with the same pair-distance multiset, and an exact collision decomposition shows that $`72\%`$--$`80\%`$ of the observed raw fourth-moment displacement in two regimes is pair-driven. The study thus separates exact higher-order capacity from the lower-order content of the observed zeta comparisons.

**[PDF](paper/Zeta_Zeros_Spectral_Statistics_v1.0.pdf) · [Markdown](paper/Zeta_Zeros_Spectral_Statistics_v1.0.md) · [Word](paper/Zeta_Zeros_Spectral_Statistics_v1.0.docx)**

Serge-Paul Carrasco, *A Computational Walk from Pair Correlation to Higher-Order Spectral Statistics of Zeta Zeros*, Version 1.0.

Canonical repository: https://github.com/sergepaulc/Riemann-Hypothesis-Computation

## Run the computations

Use Python 3.13 on macOS, Linux, or Windows with WSL. This package was tested on Linux with Python 3.13.5; see [validation results](docs/VALIDATION.md).

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_repository.py
python scripts/smoke_test.py
```

Reproduce the three main calculations into a separate `build/` directory:

```bash
python scripts/reproduce.py --experiment 1
python scripts/reproduce.py --experiment 2
python scripts/reproduce.py --experiment 3
```

Or use `--experiment all`. A repeat run requires `--overwrite`, which replaces only marked workspaces created by this runner, never the committed reference files.

## What each experiment does

| Experiment | Computation | Reproduction coverage |
|---|---|---|
| 1 | Pair correlation for three samples of 10,000 unfolded zeros | Recomputes three full-sample histograms, pair counts, short-range deficits, and integrated correlation statistics. Original finite-GUE and Poisson calibration outputs are supplied, but this runner does not resimulate those ensembles. |
| 2 | Gaussian kernel matrices and a shifted Hermitian family | Recomputes 144 spectra and 2,592 inertia classifications; runs 19 numerical checks and regenerates the main diagnostic plots. |
| 3 | Sinc-kernel moments and their collision decomposition | Recomputes 48 zeta windows, 64 CUE controls, and 64 Poisson controls; runs exact-control and separate numerical checks. |

The [reproduction guide](docs/REPRODUCING.md) gives the commands and their limits. The [results map](docs/RESULTS_MAP.md) links paper sections to the relevant code and data.

## Repository contents

```text
paper/                       Final paper in three formats and its eight figures
experiments/experiment1/      Pair-correlation code, inputs, reference outputs, tests
experiments/experiment2/      Gaussian code, inputs, reference outputs, numerical checks
experiments/experiment3/      Sinc code, inputs, reference outputs, numerical checks
scripts/                     Reproduction and package checks
data/                        Original-source catalogue and optional downloader
docs/                        Reproduction, result mapping, and validation information
manifests/input_data.json     Automated checks of scientific inputs only
```

There are no governance specifications, internal review conversations, earlier paper drafts, or Git history in this upload package. Some computational filenames retain their original implementation identifiers to avoid unnecessary changes; the public package and paper version are **1.0**.

## Data and figure availability

The derived unfolded coordinates needed for the main reruns are included. Original third-party Odlyzko tables are not bundled. To obtain them separately:

```bash
python data/download_odlyzko_tables.py zeros1 zeros3 zeros4
```

The downloader checks the recorded input fingerprints. Documentation is not checksum-locked.

The eight publication figures are supplied with the paper. The numerical runners also regenerate experiment diagnostic plots. Rebuilding every publication panel pixel-for-pixel and every historical calibration is not claimed; see the reproduction guide.

## Release and citation

- [Release notes](RELEASE_NOTES.md)
- [How to publish Version 1.0](docs/PUBLISHING.md)
- [Citation metadata](CITATION.cff)
- [License](LICENSE) and [third-party notices](NOTICE.md)

The existing MIT license for original code and documentation is retained. The notices explain the separate status of third-party data.
