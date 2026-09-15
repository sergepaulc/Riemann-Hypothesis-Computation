from pathlib import Path
import hashlib, json, math
import numpy as np, pandas as pd
from scipy.linalg import eigh
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'00_preregistration/experiment2_config_v1_frozen.json').read_text())
RES=ROOT/'02_results'

def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()

checks=[]
def add(name,passed,value,criterion): checks.append({'check':name,'passed':bool(passed),'value':str(value),'criterion':criterion})

# Input checksum mapping to copied names.
mapfiles={
 'low_height_points':ROOT/'01_inputs/low_height_zeta_unfolded_points.csv',
 'low_height_pair_correlation':ROOT/'01_inputs/low_height_zeta_pair_correlation.csv',
 'near_1e12_points':ROOT/'01_inputs/near_1e12_unfolded_points.csv',
 'near_1e12_pair_correlation':ROOT/'01_inputs/near_1e12_pair_correlation.csv',
 'near_1e21_points':ROOT/'01_inputs/near_1e21_unfolded_points.csv',
 'near_1e21_pair_correlation':ROOT/'01_inputs/near_1e21_pair_correlation.csv',
}
for k,p in mapfiles.items():
 got=sha(p); exp=CFG['input_sha256'][k]
 add(f'input_sha256::{k}',got==exp,got,'must equal preregistered SHA-256')

# Block nesting.
bm=pd.read_csv(ROOT/'00_preregistration/block_manifest_v1.csv')
nesting=True
for r in bm.itertuples():
 nesting &= (r.m512_start_1based+128==r.m256_start_1based and r.m256_start_1based+64==r.m128_start_1based)
 nesting &= (r.m128_end_1based+64==r.m256_end_1based and r.m256_end_1based+128==r.m512_end_1based)
add('nested_block_geometry',nesting,len(bm),'16 exactly nested common locations')

blocks=pd.read_csv(RES/'block_matrix_metrics.csv')
inertia=pd.read_csv(RES/'inertia_profiles_all_blocks.csv')
direct=pd.read_csv(RES/'direct_H_eigendecomposition_checks.csv')
add('row_count_blocks',len(blocks)==144,len(blocks),'3 datasets * 16 locations * 3 sizes = 144')
add('row_count_inertia',len(inertia)==2592,len(inertia),'144 blocks * 18 lambdas = 2592')
add('C_PSD',blocks.n_mu_below_negative_psd_tolerance.sum()==0,blocks.mu_min.min(),'no eigenvalue below negative PSD tolerance')
add('no_unresolved_grid_signs',inertia.n_unres.sum()==0,inertia.n_unres.sum(),'zero unresolved signs on frozen grid')
add('trace_identity',inertia.trace_abs_error.max()<1e-10,inertia.trace_abs_error.max(),'< 1e-10')
add('H_frobenius_identity',inertia.frobH2_abs_error.max()<1e-9,inertia.frobH2_abs_error.max(),'< 1e-9')
add('C_frobenius_spectral_identity',blocks.frobC2_spectral_abs_error.max()<1e-9,blocks.frobC2_spectral_abs_error.max(),'< 1e-9')
add('direct_H_spectrum_identity',direct.max_abs_eigenvalue_difference.max()<1e-12,direct.max_abs_eigenvalue_difference.max(),'< 1e-12')
add('positive_inertia_bound',np.all(inertia.npos_lower_bound_raw<=inertia.n_pos_res+1e-10),(inertia.npos_lower_bound_raw-inertia.n_pos_res).max(),'bound never exceeds resolved positive count')

# Independent recomputation of one primary m=512 location 8 using scipy.linalg.eigh.
pts=pd.read_csv(ROOT/'01_inputs/low_height_zeta_unfolded_points.csv')
xall=pts.x_unfolded.to_numpy(float)
r=bm[bm.location_id==8].iloc[0]; s=int(r.m512_start_1based)-1; e=int(r.m512_end_1based)
x=xall[s:e]; x=x-x[0]
d=x[:,None]-x[None,:]; C=np.exp(-0.5*d*d)
mu=eigh(C,eigvals_only=True,driver='evd')
out=blocks[(blocks.dataset=='low_height_first_10000')&(blocks.location_id==8)&(blocks.m==512)].iloc[0]
add('independent_scipy_mu_min',abs(mu.min()-out.mu_min)<1e-11,abs(mu.min()-out.mu_min),'< 1e-11')
add('independent_scipy_mu_max',abs(mu.max()-out.mu_max)<1e-11,abs(mu.max()-out.mu_max),'< 1e-11')

# Independent GUE weighted benchmark.
def sincpi(u): return 1.0 if u==0 else math.sin(math.pi*u)/(math.pi*u)
val=2*quad(lambda u:math.exp(-u*u)*(1-sincpi(u)**2),0,np.inf,epsabs=1e-12,epsrel=1e-12,limit=300)[0]
bench=json.loads((RES/'theoretical_GUE_gaussian_benchmark.json').read_text())['GUE_D_C_asymptotic']
add('GUE_weighted_benchmark_recompute',abs(val-bench)<1e-11,abs(val-bench),'< 1e-11')

outdf=pd.DataFrame(checks)
outdf.to_csv(ROOT/'05_reproducibility/verification_checks.csv',index=False)
summary={'all_passed':bool(outdf.passed.all()),'n_checks':len(outdf),'n_passed':int(outdf.passed.sum()),'n_failed':int((~outdf.passed).sum())}
(ROOT/'05_reproducibility/verification_summary.json').write_text(json.dumps(summary,indent=2))
print(outdf.to_string(index=False))
print(summary)
if not summary['all_passed']: raise SystemExit(1)
