# Reproducing the experiments

## Environment

The release retains the source package's dependency pins in `requirements.txt`: NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0, Matplotlib 3.10.8, mpmath 1.3.0, and pytest 9.0.2. Python 3.13.5 on Linux is the tested environment. Use macOS, Linux, or WSL; native Windows is not claimed because the Experiment 3 implementation uses the Unix `resource` module.

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_repository.py
python scripts/smoke_test.py
python -m pytest -q
```

`verify_repository.py` checks required files, public version labels, relative Markdown links, input fingerprints, and known Markdown-math hazards. It does not impose fingerprints on prose or ordinary code edits.

## Main reruns

```bash
python scripts/reproduce.py --experiment 1
python scripts/reproduce.py --experiment 2
python scripts/reproduce.py --experiment 3
```

Outputs are written below `build/experiment1`, `build/experiment2`, and `build/experiment3`. Each run creates a machine-readable validation summary. Existing workspaces are not replaced unless `--overwrite` is supplied. `--output-dir PATH` selects a different parent directory. Source files and committed reference tables remain unchanged.

The runner sets numerical-library threads to two to avoid oversubscription. It uses the supplied unfolded coordinates, so the main reruns do not require downloading the original zero tables.

### Experiment 1

Recomputes the edge-corrected pair histograms and the D0.5 and S30 statistics for all three 10,000-point samples. It verifies counts and summary values against the supplied tables using the original tolerances.

Coverage limitation: the original 200-realization finite-GUE calibration, Poisson normalization, and some supplementary robustness results are present as reference outputs and configuration, but the archived source package does not contain a complete executable reconstruction of all of them. The main command does not claim to regenerate these ensembles. No replacement calibration has been invented for this release.

### Experiment 2

Recomputes the spectra, inertia curves, pair-statistic bridge, and nested-block comparisons, then runs the original 19 numerical checks. Its regenerated inertia and pair-bridge tables are compared with the committed reference tables. The analytic GUE benchmark is retained as a recorded reference input and independently recomputed by the verifier.

Run the supplementary kernel-width checks separately:

```bash
python scripts/reproduce.py --experiment 2-validation
```

That command writes the width-sensitivity and separate-recomputation tables below `build/experiment2-validation`.

### Experiment 3

Recomputes all 176 sampled-window endpoints and derived tables. It regenerates diagnostic figures, checks the collision decomposition by explicit small-matrix enumeration, compares separate moment calculations, and runs the eight existing unit tests.

The 64-character seed namespace in `experiments/experiment3/frozen_release/00_protocol/experiment3_config.json` preserves the exact original random streams. It must not be changed to a new document checksum. The same scientific settings remain defined in the original computational implementation and are checked against the recorded configuration.

## Publication figures

All eight figures displayed in the paper are supplied in `paper/figures/`. Experiment 2 and Experiment 3 also ship runnable diagnostic-figure scripts. These are not a promise to recreate every final publication layout pixel-for-pixel. The [results map](RESULTS_MAP.md) identifies their underlying data.

## Data sources

Original-source URLs and expected fingerprints are in `data/odlyzko_tables.json`. The optional downloader writes under `data/raw/` and refuses a source file with a different fingerprint:

```bash
python data/download_odlyzko_tables.py zeros1 zeros3 zeros4
```

Raw-source downloading requires network access and was not retested during this offline packaging run. The provided derived coordinates are the inputs for the tested main reruns.

## Numerical differences

Floating-point results can vary slightly between linear-algebra implementations. The runner uses explicit tolerances for numerical table comparisons; it does not infer mathematical truth from byte-identical image or CSV files. The collision checks and independent moment checks have their own tolerances in the source.

A passing smoke test checks selected identities and saved results. It is not equivalent to running all three main experiments.
