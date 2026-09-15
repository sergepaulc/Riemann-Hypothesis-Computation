
#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests/repository_manifest.json"
SUMS = ROOT / "manifests/SHA256SUMS.txt"
EXCLUDED = {MANIFEST.resolve(), SUMS.resolve()}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


IGNORED_PARTS = {".git", "build", ".venv", "__pycache__", ".pytest_cache"}


def ignored(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return (
        any(part in IGNORED_PARTS for part in rel.parts)
        or path.name == ".DS_Store"
        or path.suffix == ".pyc"
    )


def files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file()
        and not ignored(p)
        and p.resolve() not in EXCLUDED
    )


def main() -> int:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    for p in files():
        entries.append({"path": p.relative_to(ROOT).as_posix(), "size_bytes": p.stat().st_size, "sha256": digest(p)})
    MANIFEST.write_text(json.dumps({"release": "v1.0.1", "files": entries}, indent=2) + "\n", encoding="utf-8")
    sum_paths = files() + [MANIFEST]
    SUMS.write_text("".join(f"{digest(p)}  {p.relative_to(ROOT).as_posix()}\n" for p in sorted(sum_paths)), encoding="utf-8")
    print(f"Wrote manifest for {len(entries)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
