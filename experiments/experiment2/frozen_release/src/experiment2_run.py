from __future__ import annotations

import json, math, hashlib, platform, sys
from pathlib import Path
import numpy as np
import pandas as pd
import scipy
from scipy.special import erf

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT/'00_preregistration/experiment2_config_v1_frozen.json').read_text())
RES = ROOT/'02_results'
FIG = ROOT/'03_figures'
REPRO = ROOT/'05_reproducibility'
RES.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True); REPRO.mkdir(exist_ok=True)

DATASETS = {
    'low_height_first_10000': {
        'points': ROOT/'01_inputs/low_height_zeta_unfolded_points.csv',
        'pair': ROOT/'01_inputs/low_height_zeta_pair_correlation.csv',
        'xcol': 'x_unfolded',
        'rcol': 'empirical_full',
        'role': 'primary',
    },
    'near_1e12': {
        'points': ROOT/'01_inputs/near_1e12_unfolded_points.csv',
        'pair': ROOT/'01_inputs/near_1e12_pair_correlation.csv',
        'xcol': 'theta_unfolded_relative_x',
        'rcol': 'empirical_pair_correlation',
        'role': 'secondary_control',
    },
    'near_1e21': {
        'points': ROOT/'01_inputs/near_1e21_unfolded_points.csv',
        'pair': ROOT/'01_inputs/near_1e21_pair_correlation.csv',
        'xcol': 'theta_unfolded_relative_x',
        'rcol': 'empirical_pair_correlation',
        'role': 'secondary_control',
    },
}

LAMBDAS = np.array(CFG['lambda_grid'], float)
SIGMA = float(CFG['kernel']['sigma_primary'])
U_MAX = float(CFG['pair_correlation_u_max'])
DU = float(CFG['pair_correlation_bin_width'])


def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20), b''):
            h.update(b)
    return h.hexdigest()


def load_x(ds):
    d = DATASETS[ds]
    df = pd.read_csv(d['points'])
    x = df[d['xcol']].to_numpy(float)
    assert len(x)==10000 and np.all(np.isfinite(x)) and np.all(np.diff(x)>0)
    return x


def load_r2(ds):
    d=DATASETS[ds]
    df=pd.read_csv(d['pair'])
    u=df['u_center'].to_numpy(float)
    r=df[d['rcol']].to_numpy(float)
    assert len(u)==300 and np.allclose(np.diff(u),DU,rtol=0,atol=1e-12)
    return u,r,df


def block_bounds(location_row, m):
    s=int(location_row[f'm{m}_start_1based'])-1
    e=int(location_row[f'm{m}_end_1based'])
    assert e-s==m
    return s,e


def gram_matrix(x):
    # Full, untruncated Gaussian matrix per v0.6.
    d=x[:,None]-x[None,:]
    return np.exp(-(d*d)/(2*SIGMA*SIGMA))


def weighted_edge_integral(L, a, b):
    # Integral_a^b (L-u) exp(-u^2/sigma^2) du; primary sigma=1.
    # General sigma formula retained for auditability.
    s=SIGMA
    return (L*s*math.sqrt(math.pi)/2.0)*(erf(b/s)-erf(a/s)) + (s*s/2.0)*(math.exp(-(b/s)**2)-math.exp(-(a/s)**2))


def predict_frob_from_r2(m, L, u_centers, r2):
    rho2=m*(m-1)/(L*L)
    positive_weighted=0.0
    for uc,R in zip(u_centers,r2):
        a=max(0.0, uc-DU/2)
        b=min(U_MAX, L, uc+DU/2)
        if b<=a: continue
        positive_weighted += R*weighted_edge_integral(L,a,b)
    positive_weighted *= rho2
    frob=m+2.0*positive_weighted
    return frob, frob/m-1.0, rho2


def direct_weighted_full(x, umax=30.0):
    # Exact pair-distance weighted sum inside Umax, no dense 10000x10000 matrix.
    pos=0.0; n_pairs=0
    n=len(x)
    for i in range(n-1):
        j=np.searchsorted(x, x[i]+umax, side='right')
        if j>i+1:
            d=x[i+1:j]-x[i]
            pos += np.exp(-(d*d)/(SIGMA*SIGMA)).sum()
            n_pairs += len(d)
    return n + 2*pos, n_pairs


def analyze_block(ds, xall, r2_u, r2, loc, m):
    s,e=block_bounds(loc,m)
    x=xall[s:e].copy()
    x-=x[0]
    L=float(x[-1]-x[0])
    C=gram_matrix(x)
    sym_err=float(np.max(np.abs(C-C.T)))
    diag_err=float(np.max(np.abs(np.diag(C)-1.0)))
    mu=np.linalg.eigvalsh(C)
    mu.sort()
    min_mu=float(mu[0]); max_mu=float(mu[-1])
    psd_tol=100*np.finfo(float).eps*max(1.0,max_mu)*m
    n_mu_below_psd_tol=int(np.sum(mu < -psd_tol))
    frobC=float(np.sum(C*C))
    frobC_spec=float(np.sum(mu*mu))
    predF,predD,rho2=predict_frob_from_r2(m,L,r2_u,r2)
    D=frobC/m-1.0
    crossings=np.where(mu>0,1.0/mu,np.inf)

    blockrow={
      'dataset':ds,'role':DATASETS[ds]['role'],'location_id':int(loc['location_id']),'m':m,
      'start_index_1based':s+1,'end_index_1based':e,'midpoint_index_1based':float(loc['midpoint_index_1based']),
      'L':L,'mean_spacing':L/(m-1),'rho2_finite':rho2,
      'symmetry_max_abs_error':sym_err,'diagonal_max_abs_error':diag_err,
      'mu_min':min_mu,'mu_max':max_mu,'psd_tolerance':psd_tol,'n_mu_below_negative_psd_tolerance':n_mu_below_psd_tol,
      'frobC2_points':frobC,'frobC2_from_spectrum':frobC_spec,'frobC2_spectral_abs_error':abs(frobC-frobC_spec),
      'D_C_points':D,'frobC2_pair_prediction':predF,'D_C_pair_prediction':predD,
      'pair_prediction_abs_error_D':D-predD,'pair_prediction_rel_error_frob':(frobC-predF)/frobC,
      'n_crossings_lambda_0p10_0p95':int(np.sum((crossings>=0.10)&(crossings<=0.95))),
      'crossing_min':float(np.min(crossings)),'crossing_max_finite':float(np.max(crossings[np.isfinite(crossings)])),
    }

    inertia=[]
    for lam in LAMBDAS:
        r=1.0-lam*mu
        hnorm=float(np.max(np.abs(r)))
        eps=1e-10*max(1.0,hnorm)
        pos=int(np.sum(r>eps)); neg=int(np.sum(r<-eps)); unres=m-pos-neg
        trace_spec=float(r.sum())
        trace_formula=m*(1.0-lam)
        frobH_spec=float(np.sum(r*r))
        frobH_formula=m*(1.0-2.0*lam)+lam*lam*frobC
        braw=trace_formula*trace_formula/frobH_formula if trace_formula>0 else np.nan
        inertia.append({
          'dataset':ds,'role':DATASETS[ds]['role'],'location_id':int(loc['location_id']),'m':m,'lambda':lam,
          'n_pos_res':pos,'n_neg_res':neg,'n_unres':unres,
          'p_pos_res':pos/m,'p_neg_res':neg/m,'p_unres':unres/m,
          'H_norm2_from_spectrum':hnorm,'epsilon_screen':eps,
          'min_abs_H_eigenvalue':float(np.min(np.abs(r))),
          'trace_formula':trace_formula,'trace_spectrum':trace_spec,'trace_abs_error':abs(trace_formula-trace_spec),
          'frobH2_formula':frobH_formula,'frobH2_spectrum':frobH_spec,'frobH2_abs_error':abs(frobH_formula-frobH_spec),
          'npos_lower_bound_raw':braw,'b_pos_normalized':braw/m,
          'bound_slack_fraction':pos/m-braw/m,
        })

    spectrum=pd.DataFrame({
      'dataset':ds,'location_id':int(loc['location_id']),'m':m,
      'eigen_index_ascending':np.arange(1,m+1),'mu_C':mu,
      'lambda_crossing':crossings,
    })
    return blockrow,inertia,spectrum,C,mu


def direct_H_checks(ds,xall,block_rows, spectra_cache):
    checks=[]
    locmap={int(r['location_id']):r for r in CFG['blocks']}
    for locid in CFG['direct_H_verification']['location_ids']:
      loc=locmap[locid]
      for m in CFG['direct_H_verification']['block_sizes']:
        s,e=block_bounds(loc,m)
        x=xall[s:e].copy(); x-=x[0]
        C=gram_matrix(x)
        mu=np.linalg.eigvalsh(C); mu.sort()
        for lam in CFG['direct_H_verification']['lambdas']:
          H=np.eye(m)-lam*C
          eta=np.linalg.eigvalsh(H); eta.sort()
          derived=np.sort(1.0-lam*mu)
          checks.append({'dataset':ds,'location_id':locid,'m':m,'lambda':lam,
                         'max_abs_eigenvalue_difference':float(np.max(np.abs(eta-derived))),
                         'trace_direct':float(np.trace(H)),'trace_formula':m*(1-lam),
                         'frobH2_direct':float(np.sum(H*H)),
                         'frobH2_from_eigs':float(np.sum(derived*derived))})
    return checks


def aggregate(inertia_df, blocks_df):
    # Descriptive location variability only; not exchangeability-based inference.
    agg=inertia_df.groupby(['dataset','role','m','lambda']).agg(
      p_pos_mean=('p_pos_res','mean'),p_pos_sd_location=('p_pos_res','std'),
      p_neg_mean=('p_neg_res','mean'),p_neg_sd_location=('p_neg_res','std'),
      p_unres_mean=('p_unres','mean'),
      b_pos_mean=('b_pos_normalized','mean'),b_pos_sd_location=('b_pos_normalized','std'),
      min_abs_H_eig_min=('min_abs_H_eigenvalue','min'),
      n_unres_total=('n_unres','sum'),
      bound_slack_mean=('bound_slack_fraction','mean'),
    ).reset_index()
    bagg=blocks_df.groupby(['dataset','role','m']).agg(
      n_locations=('location_id','count'),
      D_C_points_mean=('D_C_points','mean'),D_C_points_sd_location=('D_C_points','std'),
      D_C_prediction_mean=('D_C_pair_prediction','mean'),D_C_prediction_sd_location=('D_C_pair_prediction','std'),
      D_C_bridge_bias_mean=('pair_prediction_abs_error_D','mean'),
      D_C_bridge_rmse=('pair_prediction_abs_error_D',lambda s:float(np.sqrt(np.mean(np.asarray(s)**2)))),
      frob_rel_error_mean=('pair_prediction_rel_error_frob','mean'),
      frob_rel_error_maxabs=('pair_prediction_rel_error_frob',lambda s:float(np.max(np.abs(s)))),
      mu_min_min=('mu_min','min'),mu_max_max=('mu_max','max'),
      mean_spacing_mean=('mean_spacing','mean'),mean_spacing_sd=('mean_spacing','std'),
    ).reset_index()
    return agg,bagg


def scale_sensitivity(inertia_df):
    rows=[]
    for (ds,lam,locid),g in inertia_df.groupby(['dataset','lambda','location_id']):
      d={int(r.m):r.p_pos_res for r in g.itertuples()}
      if set(d)=={128,256,512}:
        rows.append({'dataset':ds,'lambda':lam,'location_id':locid,
                     'abs_p_pos_128_256':abs(d[128]-d[256]),
                     'abs_p_pos_256_512':abs(d[256]-d[512]),
                     'abs_p_pos_128_512':abs(d[128]-d[512])})
    df=pd.DataFrame(rows)
    summary=df.groupby(['dataset','lambda']).agg(
      mean_abs_128_256=('abs_p_pos_128_256','mean'),max_abs_128_256=('abs_p_pos_128_256','max'),
      mean_abs_256_512=('abs_p_pos_256_512','mean'),max_abs_256_512=('abs_p_pos_256_512','max'),
      mean_abs_128_512=('abs_p_pos_128_512','mean'),max_abs_128_512=('abs_p_pos_128_512','max'),
    ).reset_index()
    return df,summary


def full_bridge(ds,x,r2u,r2):
    measured,n_pairs=direct_weighted_full(x,U_MAX)
    L=float(x[-1]-x[0]); pred,predD,rho2=predict_frob_from_r2(len(x),L,r2u,r2)
    tail=len(x)*(len(x)-1)*math.exp(-900)
    return {'dataset':ds,'N':len(x),'L':L,'rho2_finite':rho2,'pairs_within_30':n_pairs,
            'frobC2_direct_window30_plus_diag':measured,'D_C_direct':measured/len(x)-1,
            'frobC2_pair_prediction':pred,'D_C_pair_prediction':predD,
            'D_C_abs_difference':measured/len(x)-1-predD,
            'frob_relative_difference':(measured-pred)/measured,
            'tail_bound_ordered_pairs':tail}


def main():
    block_manifest=pd.read_csv(ROOT/'00_preregistration/block_manifest_v1.csv')
    all_blocks=[]; all_inertia=[]; all_spec=[]; all_checks=[]; full=[]
    unresolved=[]
    for ds in DATASETS:
      x=load_x(ds); u,r2,pairdf=load_r2(ds)
      full.append(full_bridge(ds,x,u,r2))
      for loc in block_manifest.to_dict('records'):
        for m in CFG['block_sizes']:
          brow,irs,sp,C,mu=analyze_block(ds,x,u,r2,loc,m)
          all_blocks.append(brow); all_inertia.extend(irs); all_spec.append(sp)
      all_checks.extend(direct_H_checks(ds,x,all_blocks,None))
    bdf=pd.DataFrame(all_blocks); idf=pd.DataFrame(all_inertia); sdf=pd.concat(all_spec,ignore_index=True)
    cdf=pd.DataFrame(all_checks); fdf=pd.DataFrame(full)
    agg,bagg=aggregate(idf,bdf)
    scale,scaleagg=scale_sensitivity(idf)

    bdf.to_csv(RES/'block_matrix_metrics.csv',index=False)
    idf.to_csv(RES/'inertia_profiles_all_blocks.csv',index=False)
    sdf.to_csv(RES/'C_spectra_and_crossings.csv',index=False)
    cdf.to_csv(RES/'direct_H_eigendecomposition_checks.csv',index=False)
    fdf.to_csv(RES/'full_dataset_pair_bridge_checks.csv',index=False)
    agg.to_csv(RES/'inertia_profile_summary_by_location.csv',index=False)
    bagg.to_csv(RES/'block_metric_summary.csv',index=False)
    scale.to_csv(RES/'nested_scale_sensitivity_by_location.csv',index=False)
    scaleagg.to_csv(RES/'nested_scale_sensitivity_summary.csv',index=False)

    # unresolved audit
    udf=idf[idf.n_unres>0].copy()
    udf.to_csv(RES/'numerically_unresolved_cases.csv',index=False)

    # global numerical integrity summary
    integrity={
      'datasets':list(DATASETS),
      'blocks_analyzed':int(len(bdf)),
      'inertia_rows':int(len(idf)),
      'unresolved_eigenvalue_assignments_total':int(idf.n_unres.sum()),
      'max_C_symmetry_error':float(bdf.symmetry_max_abs_error.max()),
      'max_C_diagonal_error':float(bdf.diagonal_max_abs_error.max()),
      'minimum_C_eigenvalue_all_blocks':float(bdf.mu_min.min()),
      'blocks_with_C_eigenvalue_below_negative_psd_tolerance':int((bdf.n_mu_below_negative_psd_tolerance>0).sum()),
      'max_C_frobenius_spectral_identity_error':float(bdf.frobC2_spectral_abs_error.max()),
      'max_H_trace_identity_error':float(idf.trace_abs_error.max()),
      'max_H_frobenius_identity_error':float(idf.frobH2_abs_error.max()),
      'max_direct_H_eigenvalue_check_error':float(cdf.max_abs_eigenvalue_difference.max()),
      'min_abs_H_eigenvalue_over_grid':float(idf.min_abs_H_eigenvalue.min()),
      'primary_tail_bound_m512':float(512*511*math.exp(-900)),
    }
    (RES/'numerical_integrity_summary.json').write_text(json.dumps(integrity,indent=2))

    env={
      'python':sys.version,'platform':platform.platform(),'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,
    }
    (REPRO/'environment.json').write_text(json.dumps(env,indent=2))

    # concise scalar summary for report automation
    primary_b=bagg[bagg.dataset=='low_height_first_10000']
    primary_a=agg[agg.dataset=='low_height_first_10000']
    summary={'integrity':integrity,
             'primary_block_metrics':primary_b.to_dict('records'),
             'full_bridge':fdf.to_dict('records')}
    (RES/'experiment2_summary.json').write_text(json.dumps(summary,indent=2))
    print(json.dumps(integrity,indent=2))
    print('\nPRIMARY BLOCK SUMMARY')
    print(primary_b.to_string(index=False))
    print('\nFULL BRIDGE')
    print(fdf.to_string(index=False))
    print('\nPRIMARY INERTIA SUMMARY selected lambda')
    print(primary_a[primary_a['lambda'].isin([.1,.25,.5,.75,.95])][['m','lambda','p_pos_mean','p_pos_sd_location','p_neg_mean','b_pos_mean','bound_slack_mean','min_abs_H_eig_min']].to_string(index=False))

if __name__=='__main__': main()
