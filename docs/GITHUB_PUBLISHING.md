# Publish Riemann-Hypothesis-Computation to GitHub

1. Create an empty public GitHub repository with the exact name:

```text
Riemann-Hypothesis-Computation
```

2. Expand the delivered repository ZIP. Its root folder is already named `Riemann-Hypothesis-Computation`.

3. From the repository root, replace the URL placeholder and regenerate the checksum manifest:

```bash
python scripts/finalize_repository.py \
  --github-url https://github.com/OWNER/Riemann-Hypothesis-Computation
```

Replace `OWNER` with your GitHub account or organization name.

4. Verify the finalized tree and run the smoke tests:

```bash
python scripts/verify_repository.py
python scripts/smoke_test.py
```

5. Initialize Git and push:

```bash
git init -b main
git add .
git commit -m "Initial public release of Riemann-Hypothesis-Computation"
git remote add origin https://github.com/OWNER/Riemann-Hypothesis-Computation.git
git push -u origin main
```

6. Create GitHub release `v1.0.1`. Attach:

```text
Riemann-Hypothesis-Computation_GitHub_Repository_v1.0.1.zip
SHA256_Riemann-Hypothesis-Computation_GitHub_Repository_v1.0.1.txt
```

7. Optionally archive the GitHub release with a DOI service and add the DOI to the paper and `CITATION.cff`.

## Final checks before paper submission

Do not submit the manuscript while the literal token

```text
https://github.com/sergepaulc/Riemann-Hypothesis-Computation
```

remains anywhere in the repository or paper. Check with:

```bash
grep -RIn 'https://github.com/sergepaulc/Riemann-Hypothesis-Computation' .
```

The command should return no matches after `finalize_repository.py` has run.
