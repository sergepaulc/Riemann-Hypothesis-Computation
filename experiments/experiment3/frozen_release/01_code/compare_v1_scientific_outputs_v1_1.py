#!/usr/bin/env python3
"""Verify that the corrected v1.1 release preserves all v1 scientific outputs."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REFERENCE = BASE / '08_reference_v1'

SCIENCE_COLUMNS = [
    'point_count', 'span', 'mean_spacing', 'mu1', 'mu2', 'mu3', 'mu4_raw',
    'mu4_gt2', 'q4_per_core', 'pair_part_per_core', 'three_index_part_per_core',
    'window_start',
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


def max_csv_difference() -> tuple[float, int]:
    old = read_csv(REFERENCE / 'all_window_endpoints_v1.csv')
    new = read_csv(BASE / '02_results' / 'all_window_endpoints.csv')
    if len(old) != len(new):
        raise RuntimeError(f'row count changed: {len(old)} vs {len(new)}')
    maximum = 0.0
    comparisons = 0
    for old_row, new_row in zip(old, new):
        if (old_row['source'], old_row['index']) != (new_row['source'], new_row['index']):
            raise RuntimeError('row identity/order changed')
        for column in SCIENCE_COLUMNS:
            maximum = max(maximum, abs(float(old_row[column]) - float(new_row[column])))
            comparisons += 1
    return maximum, comparisons


def compare_json_science() -> dict[str, Any]:
    old = json.loads((REFERENCE / 'bounded_cloud_results_v1.json').read_text())
    new = json.loads((BASE / '02_results' / 'bounded_cloud_results.json').read_text())
    errors: dict[str, float] = {}
    for group, metrics in old['summaries'].items():
        for metric, stats in metrics.items():
            if metric == 'max_reconstruction_relative_error':
                continue
            if not isinstance(stats, dict):
                continue
            for stat, value in stats.items():
                if isinstance(value, (int, float)) and stat in new['summaries'][group][metric]:
                    key = f'summaries.{group}.{metric}.{stat}'
                    errors[key] = abs(float(value) - float(new['summaries'][group][metric][stat]))
    for dataset, metrics in old['zeta_vs_cue_descriptive_comparisons'].items():
        for metric, values in metrics.items():
            for key, value in values.items():
                if isinstance(value, (int, float)) and key in new['zeta_vs_cue_descriptive_comparisons'][dataset][metric]:
                    path = f'comparisons.{dataset}.{metric}.{key}'
                    errors[path] = abs(float(value) - float(new['zeta_vs_cue_descriptive_comparisons'][dataset][metric][key]))
    return {
        'numeric_fields_compared': len(errors),
        'maximum_absolute_difference': max(errors.values(), default=0.0),
        'nonzero_differences': {k: v for k, v in errors.items() if v != 0.0},
    }


def main() -> int:
    csv_max, csv_count = max_csv_difference()
    json_comparison = compare_json_science()
    tolerance = 1e-12
    maximum = max(csv_max, json_comparison['maximum_absolute_difference'])
    result = {
        'document_id': 'Experiment3BS_v1_to_v1_1_Scientific_Equivalence_Check',
        'reference_release': 'Project_Montecito_Experiment3_Bounded_Cloud_Closure_v1',
        'corrected_release': 'Project_Montecito_Experiment3BS_v1.1',
        'endpoint_numeric_values_compared': csv_count,
        'endpoint_maximum_absolute_difference': csv_max,
        'json_scientific_comparison': json_comparison,
        'excluded_as_non_scientific_or_superseded': [
            'runtime and peak-memory fields',
            'document identifiers and release labels',
            'legacy reconstruction_relative_error field, retired as evidentiary check',
            'new uncertainty-scale and independent-validation fields',
        ],
        'tolerance': tolerance,
        'status': 'PASS' if maximum <= tolerance else 'FAIL',
    }
    out = BASE / '04_report' / 'Experiment3BS_v1_to_v1_1_Scientific_Equivalence_Check.json'
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
