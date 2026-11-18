# Publishing Version 1.0 with the same repository name

The display name is **Riemann Hypothesis Computation**. The GitHub repository name is **Riemann-Hypothesis-Computation**, under **sergepaulc**. Keeping this exact owner and name preserves the repository address used in the paper:

https://github.com/sergepaulc/Riemann-Hypothesis-Computation

## Before replacing the existing repository

Keep a private local backup of the old repository and check the validation results for this clean package. Read the documented reproduction limits before deciding that the package is ready to publish. The package was assembled from the saved complete computational archive and the corrected paper; it is not a verified snapshot of any later live GitHub edits.

Nothing in this package deletes or updates GitHub automatically. Delete the old repository only after you have confirmed that your backup and replacement are usable. Deleting a public repository does not remove other users' public forks or downloaded copies.

## Create the replacement

1. After removing the old repository, create a public repository under `sergepaulc` named exactly `Riemann-Hypothesis-Computation`.
2. Do not initialize it with an extra README, license, or Git history. These files are already in this package.
3. Extract this package and publish the contents of its `Riemann-Hypothesis-Computation/` folder, not the ZIP file itself. The root README must be at the repository root, not inside another nested folder.
4. Use a fresh local Git repository rather than pushing the old repository's history.

GitHub Desktop is suitable for publishing the extracted folder to the empty repository. A command-line equivalent, run inside the extracted folder, is:

```bash
git init -b main
git config --local user.name "Serge-Paul Carrasco"
# Set user.email to the exact personal or noreply email shown in
# Settings > Emails for the sergepaulc account before making the commit.
git add .
git commit -m "Publish clean Version 1.0 research package"
git remote add origin https://github.com/sergepaulc/Riemann-Hypothesis-Computation.git
git push -u origin main
```

Do not copy a `.git/` directory from the old repository. Check `git config user.email` before committing so the old `Serge-Paul` account is not inadvertently credited again.

## Publish the release

In GitHub, open **Releases → Draft a new release**. Create tag `v1.0` from the validated `main` commit. Use the title **Riemann Hypothesis Computation — Version 1.0**, and paste `RELEASE_NOTES.md` into the release description. Attach the final paper PDF, Word, and Markdown; an additional ZIP of the clean package is optional. Save as a draft until the checks below pass, then publish.

The paper and code remain Version 1.0. `cff-version: 1.2.0` is the citation-file format, not the project version. The citation file intentionally omits a release date until the actual publication date is known.

## Final browser check

Open the README links, the complete PDF, and the Word download. Check the Markdown's critical strip, piecewise equation in Section 2.7, norm expressions, tables, and all eight figures. Local MathJax checks are included, but GitHub's live renderer cannot be guaranteed without this final preview. Confirm that no governance or internal-review folders were uploaded.

Useful official instructions:

- https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
- https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository
