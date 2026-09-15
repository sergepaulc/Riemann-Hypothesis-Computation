
#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests/repository_manifest.json"
IGNORED_PARTS = {".git", "build", ".venv", "__pycache__", ".pytest_cache"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def ignored(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return any(part in IGNORED_PARTS for part in rel.parts) or path.name == ".DS_Store" or path.suffix == ".pyc"


def main() -> int:
    record = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    expected = {entry["path"] for entry in record["files"]}
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file()
        and not ignored(p)
        and p != MANIFEST
        and p != ROOT / "manifests/SHA256SUMS.txt"
    }
    for extra in sorted(actual - expected):
        failures.append({"path": extra, "error": "unexpected file not covered by manifest"})
    for missing in sorted(expected - actual):
        failures.append({"path": missing, "error": "missing from working tree"})
    for entry in record["files"]:
        path = ROOT / entry["path"]
        if not path.is_file():
            failures.append({"path": entry["path"], "error": "missing"})
            continue
        if path.stat().st_size != entry["size_bytes"]:
            failures.append({"path": entry["path"], "error": "size mismatch"})
            continue
        actual = digest(path)
        if actual != entry["sha256"]:
            failures.append({"path": entry["path"], "error": "sha256 mismatch", "actual": actual})
    status = {"status": "PASS" if not failures else "FAIL", "files_checked": len(record["files"]), "failures": failures}
    print(json.dumps(status, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
