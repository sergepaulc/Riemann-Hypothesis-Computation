#!/usr/bin/env python3
"""Reproduce the supplied experiments in isolated build directories.
Committed reference files are never overwritten. --overwrite replaces only a
workspace created by this runner. The main reruns require no network access.
"""
from __future__ import annotations
import argparse, json, os, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MARKER='.rhc-workspace'
def run(args, cwd):
    env=os.environ.copy()
    for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):env[k]='2'
    env['MPLBACKEND']='Agg'
    print('+',' '.join(map(str,args)),flush=True)
    subprocess.run(list(map(str,args)),cwd=cwd,env=env,check=True)
def workspace(source,target,overwrite):
    if target.exists():
        if not overwrite or not (target/MARKER).is_file():
            raise RuntimeError(f'{target} already exists; --overwrite is allowed only for a marked reproduction workspace.')
        shutil.rmtree(target)
    if source:shutil.copytree(source,target,ignore=shutil.ignore_patterns('__pycache__','.pytest_cache'))
    else:target.mkdir(parents=True)
    (target/MARKER).write_text('Generated reproduction workspace.\n')
def compare_tables(reference,generated,names):
    import numpy as np
    import pandas as pd
    records=[]
    for name in names:
        a,b=pd.read_csv(reference/name),pd.read_csv(generated/name)
        if a.shape!=b.shape or list(a.columns)!=list(b.columns):raise AssertionError(f'Table layout differs: {name}')
        max_abs=0.0
        for col in a:
            if pd.api.types.is_numeric_dtype(a[col]) and pd.api.types.is_numeric_dtype(b[col]):
                av,bv=a[col].to_numpy(float),b[col].to_numpy(float)
                if not np.allclose(av,bv,atol=2e-10,rtol=2e-10,equal_nan=True):raise AssertionError(f'Numerical mismatch: {name}, {col}')
                finite=np.isfinite(av)&np.isfinite(bv)
                if finite.any():max_abs=max(max_abs,float(np.max(np.abs(av[finite]-bv[finite]))))
            elif not a[col].fillna('').equals(b[col].fillna('')):raise AssertionError(f'Non-numerical mismatch: {name}, {col}')
        records.append({'table':name,'rows':len(a),'status':'PASS','max_absolute_difference':max_abs})
    return records
def reproduce(exp,build,overwrite):
    target=build/f'experiment{exp}'
    if exp=='1':
        workspace(None,target,overwrite)
        run([sys.executable,ROOT/'experiments/experiment1/code/reproduce_experiment1.py','--output-dir',target],ROOT)
        r=json.loads((target/'experiment1_reproduction_summary.json').read_text())
        return {'experiment':exp,'status':r['status'],'scope':'Three full-sample pair histograms, counts, D0.5 and S30. Stored GUE/Poisson calibration ensembles are not resimulated by this runner.','validation_checks':r['validation_checks']}
    if exp=='2':
        source=ROOT/'experiments/experiment2/frozen_release';workspace(source,target,overwrite)
        for name in ['02_results','03_figures','05_reproducibility']:
            shutil.rmtree(target/name,ignore_errors=True);(target/name).mkdir()
        for script in ['experiment2_run.py','verify_experiment2.py','make_figures.py']:run([sys.executable,'src/'+script],target)
        comparisons=compare_tables(source/'02_results',target/'02_results',['inertia_profiles_all_blocks.csv','full_dataset_pair_bridge_checks.csv'])
        checks=json.loads((target/'05_reproducibility/verification_summary.json').read_text())
        return {'experiment':exp,'status':'PASS','checks':checks,'comparisons':comparisons}
    if exp=='3':
        source=ROOT/'experiments/experiment3/frozen_release';workspace(source,target,overwrite)
        for name in ['02_results','03_figures','04_report','05_integrity']:
            shutil.rmtree(target/name,ignore_errors=True);(target/name).mkdir()
        for script in ['run_experiment3bs_v1_1.py','make_paper_figures_v1.py','validate_collision_decomposition_v1_1.py','validate_moments_v1_1.py']:run([sys.executable,'01_code/'+script],target)
        run([sys.executable,'-m','pytest','-q','01_code/tests'],target)
        comparisons=compare_tables(source/'02_results',target/'02_results',['all_window_endpoints.csv','group_summary.csv','mu4_difference_decomposition_vs_cue.csv','uncertainty_scale_comparison.csv'])
        return {'experiment':exp,'status':'PASS','comparisons':comparisons,
                'collision_validation':json.loads((target/'04_report/independent_collision_validation_v1_1.json').read_text())['status'],
                'moment_validation':json.loads((target/'04_report/independent_moment_validation_v1_1.json').read_text())['status']}
    if exp=='2-validation':
        workspace(None,target,overwrite)
        run([sys.executable,ROOT/'experiments/experiment2/validation_release/src/independent_validate.py','--output-dir',target],ROOT)
        reference=ROOT/'experiments/experiment2/validation_release/01_results'
        names=sorted(p.name for p in (target/'01_results').glob('*.csv') if (reference/p.name).is_file())
        comparisons=compare_tables(reference,target/'01_results',names)
        return {'experiment':exp,'status':'PASS','scope':'Supplementary Gaussian-width tables compared with their archived outputs.', 'comparisons':comparisons}
    raise ValueError(exp)
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--experiment',choices=['1','2','3','2-validation','all'],required=True)
    p.add_argument('--output-dir',type=Path,default=ROOT/'build');p.add_argument('--overwrite',action='store_true')
    args=p.parse_args();build=args.output_dir.resolve();build.mkdir(parents=True,exist_ok=True)
    selected=['1','2','3'] if args.experiment=='all' else [args.experiment];results=[]
    for exp in selected:
        result=reproduce(exp,build,args.overwrite);results.append(result)
        (build/f'experiment{exp}_validation.json').write_text(json.dumps(result,indent=2)+'\n')
    summary={'status':'PASS','checks_run':selected,'results':results}
    (build/'reproduction_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
