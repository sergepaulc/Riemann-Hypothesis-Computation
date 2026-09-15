
from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = Path(__file__).resolve().parents[1] / "code" / "reproduce_experiment1.py"
spec = importlib.util.spec_from_file_location("exp1_public", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


def test_headline_d05_values():
    expected = {
        "first_10000": 0.22400972450456524,
        "near_1e12": 0.016228671241873993,
        "near_1e21": -0.036660946330020705,
    }
    for name, (path, column) in module.DATASETS.items():
        points = pd.read_csv(path)[column].to_numpy(float)
        summary, _ = module.analyze(points)
        assert abs(summary["D0_5"] - expected[name]) < 1e-6
