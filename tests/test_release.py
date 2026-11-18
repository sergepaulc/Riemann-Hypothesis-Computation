"""Packaging tests that do not lock documentation or change numerical results."""
import hashlib,importlib.util,json,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def test_input_fingerprints():
    manifest=json.loads((ROOT/'manifests/input_data.json').read_text())
    for item in manifest['files']:
        assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256']

def test_experiment3_recorded_seed_and_geometry():
    code=ROOT/'experiments/experiment3/frozen_release/01_code'
    sys.path.insert(0,str(code))
    spec=importlib.util.spec_from_file_location('exp3_release_runner',code/'run_experiment3bs_v1_1.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    config=json.loads((code.parent/'00_protocol/experiment3_config.json').read_text())
    assert mod.OUTER_SIZE==config['outer_size']
    assert mod.N_CONTROLS==config['cue_realizations']==config['poisson_realizations']
    assert mod.CORE.tolist()==config['core_indices_zero_based']
    assert mod.WINDOW_STARTS.tolist()==config['window_starts_zero_based']
    assert config['seed_namespace']=='815e08aec7f55ddb5ba00655a24df77be94bad9b05384027c39a0c316a16251e'
    for label in ['CUE','Poisson','bootstrap_D0_first_10000_mu2']:
        for index in [0,1,63]:
            raw=f"{config['seed_namespace']}|{label}|{index:08d}".encode()
            assert mod.seed_for(label,index)==int.from_bytes(hashlib.sha256(raw).digest()[:8],'big')
