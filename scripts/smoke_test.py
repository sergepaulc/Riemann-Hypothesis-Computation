
#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="rhc-smoke-") as tmp:
        run([
            sys.executable,
            str(ROOT / "experiments/experiment1/code/reproduce_experiment1.py"),
            "--output-dir",
            tmp,
        ], ROOT)
    with tempfile.TemporaryDirectory(prefix="rhc-exp2-smoke-") as tmp:
        target = Path(tmp) / "frozen_release"
        shutil.copytree(ROOT / "experiments/experiment2/frozen_release", target)
        run([sys.executable, "src/verify_experiment2.py"], target)
    run([
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "01_code/tests/test_experiment3bs_v1_1.py",
    ], ROOT / "experiments/experiment3/frozen_release")
    print(json.dumps({"status": "PASS", "checks": ["experiment1", "experiment2", "experiment3"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
