import os,json,hashlib,math
import numpy as np, pandas as pd
from scipy.linalg import eigvalsh
from scipy.integrate import quad
from math import erf

root='/mnt/data/exp2_validation_work/Project_Montecito_Experiment2_v1'
out='/mnt/data/Project_Montecito_Experiment2_Validation_v1'
os.makedirs(out,exist_ok=True)
os.makedirs(os.path.join(out,'01_results'),exist_ok=True)
os.makedirs(os.path.join(out,'02_figures'),exist_ok=True)
os.makedirs(os.path.join(out,'03_report'),exist_ok=True)
os.makedirs(os.path.join(out,'src'),exist_ok=True)

cfg=json.load(open(os.path.join(root,'00_preregistration/experiment2_config_v1_frozen.json')))
manifest=pd.read_csv(os.path.join(root,'00_preregistration/block_manifest_v1.csv'))
pub_metrics=pd.read_csv(os.path.join(root,'02_results/block_matrix_metrics.csv'))
pub_inertia=pd.read_csv(os.path.join(root,'02_results/inertia_profiles_all_blocks.csv'))
pub_full=pd.read_csv(os.path.join(root,'02_results/full_dataset_pair_bridge_checks.csv'))

DS={
 'low_height_first_10000':('01_inputs/low_height_zeta_unfolded_points.csv','01_inputs/low_height_zeta_pair_correlation.csv','primary'),
 'near_1e12':('01_inputs/near_1e12_unfolded_points.csv','01_inputs/near_1e12_pair_correlation.csv','secondary_control'),
 'near_1e21':('01_inputs/near_1e21_unfolded_points.csv','01_inputs/near_1e21_pair_correlation.csv','secondary_control')}

# Independent kernel and finite-window pair bridge implementation.
def kernel_matrix(x,sigma):
    d=x[:,None]-x[None,:]
    return np.exp(-(d*d)/(2*sigma*sigma))

def pair_predict(pc, m, L, sigma):
    # Independent finite-window translation-edge prediction. Treat R2 as piecewise
    # constant on each histogram bin and integrate the Gaussian weight exactly.
    u=pc['u_center'].to_numpy(float)
    rcol='empirical_full' if 'empirical_full' in pc.columns else 'empirical_pair_correlation'
    R=pc[rcol].to_numpy(float)
    du=float(np.median(np.diff(u)))
    rho2=m*(m-1)/(L*L)
    def edge_int(a,b):
        # integral (L-t) exp(-t^2/sigma^2) dt
        return (L*sigma*math.sqrt(math.pi)/2)*(erf(b/sigma)-erf(a/sigma)) + (sigma*sigma/2)*(math.exp(-(b/sigma)**2)-math.exp(-(a/sigma)**2))
    pos=0.0
    for uc,rv in zip(u,R):
        a=max(0.0,uc-du/2); b=min(30.0,L,uc+du/2)
        if b>a: pos += rv*edge_int(a,b)
    return m+2*rho2*pos

def full_direct_window(x,sigma,umax=30):
    # independent moving window, unordered pairs then double
    n=len(x); s=0.0; pairs=0
    for i in range(n):
        j=i+1
        while j<n and x[j]-x[i] <= umax:
            d=x[j]-x[i]
            s += math.exp(-(d*d)/(sigma*sigma))
            pairs += 1
            j += 1
    return n+2*s,pairs

rows=[]; inert=[]; fullrows=[]
for ds,(pf,cf,role) in DS.items():
    pts=pd.read_csv(os.path.join(root,pf)); xcol='x_unfolded' if 'x_unfolded' in pts.columns else 'theta_unfolded_relative_x'; xall=pts[xcol].to_numpy(float)
    pc=pd.read_csv(os.path.join(root,cf))
    for sigma in [0.5,1.0,2.0]:
        fdir,pairs=full_direct_window(xall,sigma)
        L=xall[-1]-xall[0]
        fp=pair_predict(pc,len(xall),L,sigma)
        fullrows.append(dict(dataset=ds,sigma=sigma,N=len(xall),L=L,pairs_within_30=pairs,
                             frobC2_direct_window30_plus_diag=fdir,D_C_direct=fdir/len(xall)-1,
                             frobC2_pair_prediction=fp,D_C_pair_prediction=fp/len(xall)-1,
                             abs_D=(fdir-fp)/len(xall),rel_frob=(fdir-fp)/fp))
        for _,b in manifest.iterrows():
            loc=int(b.location_id)
            for m in [128,256,512]:
                st=int(b[f'm{m}_start_1based'])-1; en=int(b[f'm{m}_end_1based'])
                x=xall[st:en]
                C=kernel_matrix(x,sigma)
                mu=eigvalsh(C,check_finite=True,driver='evr')
                frob=float(np.sum(C*C)); frobspec=float(np.dot(mu,mu)); Lb=float(x[-1]-x[0])
                pred=pair_predict(pc,m,Lb,sigma)
                rows.append(dict(dataset=ds,role=role,sigma=sigma,location_id=loc,m=m,
                                 start_index_1based=st+1,end_index_1based=en,L=Lb,
                                 mean_spacing=Lb/(m-1),mu_min=float(mu[0]),mu_max=float(mu[-1]),
                                 frobC2_points=frob,frobC2_spectrum=frobspec,
                                 D_C_points=frob/m-1,frobC2_pair_prediction=pred,
                                 D_C_pair_prediction=pred/m-1,
                                 pair_prediction_abs_error_D=(frob-pred)/m,
                                 pair_prediction_rel_error_frob=(frob-pred)/pred,
                                 q01=float(np.quantile(mu,.01)),q05=float(np.quantile(mu,.05)),q25=float(np.quantile(mu,.25)),
                                 q50=float(np.quantile(mu,.5)),q75=float(np.quantile(mu,.75)),q95=float(np.quantile(mu,.95)),q99=float(np.quantile(mu,.99))))
                if True:
                    for lam in cfg['lambda_grid']:
                        r=1-lam*mu
                        # independent exact-ish classification; no values close to screening expected.
                        norm2=float(np.max(np.abs(r))); eps=1e-10*max(1,norm2)
                        npos=int(np.sum(r>eps)); nneg=int(np.sum(r<-eps)); nun=int(m-npos-nneg)
                        tr=m*(1-lam); fh=m*(1-2*lam)+lam*lam*frob
                        braw=tr*tr/fh if tr>0 else float('nan')
                        inert.append(dict(dataset=ds,sigma=sigma,location_id=loc,m=m,lambda_=lam,n_pos_res=npos,n_neg_res=nneg,n_unres=nun,
                                          p_pos_res=npos/m,p_neg_res=nneg/m,p_unres=nun/m,
                                          min_abs_H_eigenvalue=float(np.min(np.abs(r))),epsilon_screen=eps,
                                          trace_formula=tr,frobH2_formula=fh,b_pos_normalized=braw/m))

rdf=pd.DataFrame(rows); idf=pd.DataFrame(inert); fdf=pd.DataFrame(fullrows)
rdf.to_csv(os.path.join(out,'01_results/independent_block_metrics_all_sigma.csv'),index=False)
idf.to_csv(os.path.join(out,'01_results/independent_inertia_all_sigma.csv'),index=False)
fdf.to_csv(os.path.join(out,'01_results/independent_full_dataset_pair_bridge_all_sigma.csv'),index=False)

# exact comparison with published sigma=1 metrics
r1=rdf[rdf.sigma==1].copy()
keys=['dataset','location_id','m']
mm=r1.merge(pub_metrics,on=keys,suffixes=('_ind','_pub'))
comparisons={}
for col in ['mu_min','mu_max','frobC2_points','D_C_points','frobC2_pair_prediction','D_C_pair_prediction','pair_prediction_abs_error_D','pair_prediction_rel_error_frob']:
    comparisons[col]=float(np.max(np.abs(mm[col+'_ind']-mm[col+'_pub'])))
# inertia compare
ip=idf[idf.sigma==1].rename(columns={'lambda_':'lambda'}).merge(pub_inertia,on=['dataset','location_id','m','lambda'],suffixes=('_ind','_pub'))
for col in ['n_pos_res','n_neg_res','n_unres','p_pos_res','p_neg_res','min_abs_H_eigenvalue','b_pos_normalized']:
    comparisons['inertia_'+col]=float(np.max(np.abs(ip[col+'_ind']-ip[col+'_pub'])))
# full bridge compare
ff=fdf[fdf.sigma==1].merge(pub_full,on=['dataset'],suffixes=('_ind','_pub'))
for col in ['D_C_direct','D_C_pair_prediction']:
    comparisons['full_'+col]=float(np.max(np.abs(ff[col+'_ind']-ff[col+'_pub'])))
comparisons['full_frob_relative_difference']=float(np.max(np.abs(ff['rel_frob']-ff['frob_relative_difference'])))
json.dump(comparisons,open(os.path.join(out,'01_results/independent_reproduction_differences.json'),'w'),indent=2)

# summaries sensitivity and spectral diagnostics
sumdf=(rdf.groupby(['dataset','sigma','m']).agg(D_mean=('D_C_points','mean'),D_sd=('D_C_points','std'),
       mu_max_mean=('mu_max','mean'),mu_max_sd=('mu_max','std'),mu_min_mean=('mu_min','mean'),
       q05_mean=('q05','mean'),q50_mean=('q50','mean'),q95_mean=('q95','mean'),pair_rel_abs_mean=('pair_prediction_rel_error_frob',lambda s: np.mean(np.abs(s))),pair_rel_abs_max=('pair_prediction_rel_error_frob',lambda s: np.max(np.abs(s)))).reset_index())
sumdf.to_csv(os.path.join(out,'01_results/sigma_sensitivity_summary.csv'),index=False)

# crossing onset: 1/mu_max; distribution thresholds quantiles for sigma1
spec=rdf[rdf.sigma==1].copy(); spec['first_crossing_lambda']=1/spec['mu_max']; spec['last_crossing_lambda']=1/spec['mu_min']
spec.to_csv(os.path.join(out,'01_results/spectral_diagnostics_sigma1.csv'),index=False)
specsum=(spec.groupby(['dataset','m']).agg(first_cross_mean=('first_crossing_lambda','mean'),first_cross_sd=('first_crossing_lambda','std'),
    mu_max_mean=('mu_max','mean'),mu_max_sd=('mu_max','std'),q95_mean=('q95','mean'),q50_mean=('q50','mean'),q05_mean=('q05','mean'),mu_min_mean=('mu_min','mean')).reset_index())
specsum.to_csv(os.path.join(out,'01_results/spectral_summary_sigma1.csv'),index=False)

# Direct full N=10000 Dc sigma sensitivities versus analytic benchmarks computed quadrature for Poisson and GUE.
def sincpi(u): return 1.0 if u==0 else math.sin(math.pi*u)/(math.pi*u)
def gue_D(sig):
    fun=lambda u: 2*math.exp(-(u*u)/(sig*sig))*(1-sincpi(u)**2)
    return quad(fun,0,np.inf,epsabs=1e-13,epsrel=1e-13,limit=300)[0]
def pois_D(sig): return math.sqrt(math.pi)*sig
bench=[]
for s in [.5,1,2]: bench.append({'sigma':s,'GUE_D':gue_D(s),'Poisson_D':pois_D(s)})
pd.DataFrame(bench).to_csv(os.path.join(out,'01_results/analytic_kernel_benchmarks.csv'),index=False)

# bootstrap-ish descriptive block SE (not iid claim) for primary sensitivity
# create simple figures
import matplotlib.pyplot as plt
for s in [.5,1,2]:
    sub=rdf[(rdf.dataset=='low_height_first_10000')&(rdf.sigma==s)&(rdf.m==512)]
    plt.figure(figsize=(7,4)); plt.plot(sub.location_id,sub.D_C_points,marker='o'); plt.xlabel('Block location'); plt.ylabel('D_C'); plt.title(f'Primary zeta D_C across m=512 blocks, sigma={s}'); plt.tight_layout(); plt.savefig(os.path.join(out,'02_figures',f'primary_Dc_locations_sigma_{str(s).replace(".","p")}.png'),dpi=160); plt.close()

# spectra summary quantiles versus height for m512 sigma1
sub=spec[spec.m==512]
plt.figure(figsize=(7,4))
for ds,g in sub.groupby('dataset'):
    plt.plot(g.location_id,g.mu_max,marker='o',label=ds)
plt.xlabel('Block location'); plt.ylabel('largest eigenvalue of C'); plt.title('Upper spectral edge by zeta height (m=512, sigma=1)'); plt.legend(fontsize=8); plt.tight_layout(); plt.savefig(os.path.join(out,'02_figures','spectral_upper_edge_by_height.png'),dpi=160); plt.close()

# inertia means validation
isum=idf.groupby(['dataset','sigma','m','lambda_']).agg(p_pos_mean=('p_pos_res','mean'),p_pos_sd=('p_pos_res','std')).reset_index()
isum.to_csv(os.path.join(out,'01_results/independent_inertia_summary_all_sigma.csv'),index=False)

# copy script itself
import shutil
shutil.copy(__file__,os.path.join(out,'src','independent_validate.py'))

print('comparisons',json.dumps(comparisons,indent=2))
print('\nfull',fdf.to_string(index=False))
print('\nsensitivity m512')
print(sumdf[sumdf.m==512].to_string(index=False))
print('\nspectral m512')
print(specsum[specsum.m==512].to_string(index=False))
