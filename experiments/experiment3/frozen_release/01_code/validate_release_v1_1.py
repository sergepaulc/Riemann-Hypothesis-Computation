#!/usr/bin/env python3
"""Validate the internal consistency of the Experiment 3BS v1.1 release."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import py_compile
from typing import Any

BASE = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def check(name: str, condition: bool, detail: Any = None) -> dict[str, Any]:
    return {'name': name, 'status': 'PASS' if condition else 'FAIL', 'detail': detail}


def main() -> int:
    checks: list[dict[str, Any]] = []
    protocol = BASE / '00_protocol' / 'Experiment3_Bounded_Cloud_Closure_Protocol_v1.md'
    expected_protocol_sha = '815e08aec7f55ddb5ba00655a24df77be94bad9b05384027c39a0c316a16251e'
    checks.append(check('protocol_sha256', sha256(protocol) == expected_protocol_sha, sha256(protocol)))

    result_path = BASE / '02_results' / 'bounded_cloud_results.json'
    result = json.loads(result_path.read_text())
    checks.append(check('result_protocol_binding', result['protocol_sha256'] == expected_protocol_sha))
    checks.append(check('D3_not_accessed', result['scientific_parameters']['D3_accessed'] is False))

    for filename, expected in result['input_sha256'].items():
        actual = sha256(BASE / '00_protocol' / filename)
        checks.append(check(f'input_sha256:{filename}', actual == expected, actual))

    endpoint_path = BASE / '02_results' / 'all_window_endpoints.csv'
    with endpoint_path.open(newline='', encoding='utf-8') as handle:
        endpoints = list(csv.DictReader(handle))
    checks.append(check('endpoint_row_count', len(endpoints) == 176, len(endpoints)))
    counts = {}
    for row in endpoints:
        counts[row['source']] = counts.get(row['source'], 0) + 1
    checks.append(check('endpoint_group_counts', counts == {
        'D0_first_10000': 16, 'D1_near_1e12': 16, 'D2_near_1e21': 16,
        'CUE': 64, 'Poisson': 64,
    }, counts))
    fields = set(endpoints[0])
    checks.append(check('legacy_circular_field_retired', 'reconstruction_relative_error' not in fields))
    checks.append(check('algebraic_residual_labeled', 'algebraic_closure_residual_by_construction' in fields))

    derived = json.loads((BASE / '02_results' / 'derived_table_validation.json').read_text())
    checks.append(check('derived_tables_regenerable', derived['status'] == 'PASS', derived))

    collision = json.loads((BASE / '04_report' / 'independent_collision_validation_v1_1.json').read_text())
    checks.append(check('independent_collision_validation', collision['status'] == 'PASS', {
        'cases': collision['cases_tested'],
        'max_term_error': collision['maximum_term_absolute_error'],
    }))
    moments = json.loads((BASE / '04_report' / 'independent_moment_validation_v1_1.json').read_text())
    checks.append(check('independent_moment_validation', moments['status'] == 'PASS', moments['maximum_dense_crosscheck_absolute_error']))
    equivalence = json.loads((BASE / '04_report' / 'Experiment3BS_v1_to_v1_1_Scientific_Equivalence_Check.json').read_text())
    checks.append(check('scientific_equivalence_to_v1', equivalence['status'] == 'PASS', {
        'endpoint_max': equivalence['endpoint_maximum_absolute_difference'],
        'json_max': equivalence['json_scientific_comparison']['maximum_absolute_difference'],
    }))

    uncertainty_path = BASE / '02_results' / 'uncertainty_scale_comparison.csv'
    with uncertainty_path.open(newline='', encoding='utf-8') as handle:
        uncertainty = list(csv.DictReader(handle))
    checks.append(check('uncertainty_scale_rows', len(uncertainty) == 12, len(uncertainty)))
    checks.append(check('both_uncertainty_scales_present', all(
        row.get('effect_in_cue_individual_window_sd') not in (None, '') and
        row.get('effect_in_cue_16_window_mean_bootstrap_sd') not in (None, '')
        for row in uncertainty
    )))

    test_log = (BASE / '04_report' / 'unit_test_log_v1_1.txt').read_text()
    checks.append(check('unit_test_source_shipped', (BASE / '01_code' / 'tests' / 'test_experiment3bs_v1_1.py').exists()))
    checks.append(check('unit_tests_pass', '8 passed' in test_log, test_log.strip()))

    py_files = sorted((BASE / '01_code').rglob('*.py'))
    compile_errors = []
    for path in py_files:
        try:
            py_compile.compile(str(path), doraise=True)
        except Exception as exc:  # pragma: no cover
            compile_errors.append(f'{path.relative_to(BASE)}: {exc}')
    checks.append(check('python_compilation', not compile_errors, compile_errors))

    expected_figures = {
        'homometric_moment_comparison.png', 'mu2_boxplot.png', 'mu2_height_trajectory.png',
        'mu2_zeta_cue_zoom.png', 'mu4_difference_decomposition_vs_cue.png',
        'mu4_gt2_boxplot.png', 'mu4_gt2_height_trajectory.png', 'mu4_gt2_zeta_cue_zoom.png',
        'mu4_raw_boxplot.png', 'mu4_raw_height_trajectory.png', 'mu4_raw_zeta_cue_zoom.png',
    }
    actual_figures = {p.name for p in (BASE / '03_figures').glob('*.png') if p.stat().st_size > 0}
    checks.append(check('figure_set_complete', expected_figures == actual_figures, sorted(actual_figures)))

    paper = (BASE / '06_paper' / 'Project_Montecito_Paper_Simple_Draft_v0.3.2.md').read_text()
    checks.append(check('paper_uses_public_experiment3_name', 'Experiment 3BS' not in paper and '# 4. Experiment 3:' in paper))
    checks.append(check('paper_uncertainty_scales_explained', 'individual-window scale' in paper and '16-window-mean scale' in paper))
    checks.append(check('paper_D1_D2_distinction', 'marginal intermediate-height displacement' in paper and 'fully consistent' in paper))
    checks.append(check('paper_homometric_promoted', paper.index('## 4.4 Exact demonstration') < paper.index('# 5. Controls')))

    forbidden_names = [p.name for p in BASE.rglob('*') if p.is_file() and ('D3_zeta' in p.name or 'zeros5' in p.name)]
    checks.append(check('no_D3_source', not forbidden_names, forbidden_names))

    failed = [item for item in checks if item['status'] != 'PASS']
    report = {
        'document_id': 'Project_Montecito_Experiment3BS_Release_Validation_v1_1',
        'checks_total': len(checks),
        'checks_passed': len(checks) - len(failed),
        'checks_failed': len(failed),
        'status': 'PASS' if not failed else 'FAIL',
        'checks': checks,
    }
    out = BASE / '05_integrity' / 'Project_Montecito_Experiment3BS_Release_Validation_v1_1.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('document_id','checks_total','checks_passed','checks_failed','status')}, indent=2))
    return 0 if not failed else 1


if __name__ == '__main__':
    raise SystemExit(main())
