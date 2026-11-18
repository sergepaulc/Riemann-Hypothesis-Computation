from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'02_results'; FIG=ROOT/'03_figures'; FIG.mkdir(exist_ok=True)
agg=pd.read_csv(RES/'inertia_profile_summary_by_location.csv')
bagg=pd.read_csv(RES/'block_metric_summary.csv')

# 1 Primary m=512: inertia and lower bound
x=agg[(agg.dataset=='low_height_first_10000')&(agg.m==512)]
plt.figure(figsize=(8,5.2))
plt.errorbar(x['lambda'],x.p_pos_mean,yerr=x.p_pos_sd_location,marker='o',capsize=2,label='positive inertia fraction (mean ± location SD)')
plt.plot(x['lambda'],x.p_neg_mean,marker='s',label='negative inertia fraction')
plt.plot(x['lambda'],x.b_pos_mean,marker='^',label='trace/Frobenius lower bound')
plt.xlabel(r'$\lambda$'); plt.ylabel('fraction'); plt.ylim(-0.03,1.05)
plt.title('Experiment 2: primary zeta inertia profile (m=512)')
plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'01_primary_inertia_and_bound_m512.png',dpi=180); plt.close()

# 2 ppos by block size
plt.figure(figsize=(8,5.2))
for m in [128,256,512]:
 g=agg[(agg.dataset=='low_height_first_10000')&(agg.m==m)]
 plt.plot(g['lambda'],g.p_pos_mean,marker='o',label=f'm={m}')
plt.xlabel(r'$\lambda$'); plt.ylabel('mean resolved positive fraction')
plt.title('Primary zeta positive inertia across nested block sizes')
plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'02_primary_positive_inertia_by_block_size.png',dpi=180); plt.close()

# 3 pair bridge primary D_C
p=bagg[bagg.dataset=='low_height_first_10000'].sort_values('m')
plt.figure(figsize=(7.5,5.2))
plt.errorbar(p.m-4,p.D_C_points_mean,yerr=p.D_C_points_sd_location,fmt='o',capsize=4,label=r'points-in $D_C$ (mean ± location SD)')
plt.plot(p.m+4,p.D_C_prediction_mean,'s',label=r'pair-correlation prediction')
plt.xlabel('block size m'); plt.ylabel(r'$D_C=\|C\|_F^2/m-1$')
plt.title('Experiment 1 → 2 bridge: Gaussian Gram off-diagonal energy')
plt.xticks([128,256,512]); plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'03_primary_pair_correlation_frobenius_bridge.png',dpi=180); plt.close()

# 4 height control D_C m512
q=bagg[bagg.m==512].copy()
order=['low_height_first_10000','near_1e12','near_1e21']
q['ord']=q.dataset.map({v:i for i,v in enumerate(order)}); q=q.sort_values('ord')
xx=np.arange(len(q))
plt.figure(figsize=(7.5,5.2))
plt.errorbar(xx-.06,q.D_C_points_mean,yerr=q.D_C_points_sd_location,fmt='o',capsize=4,label='points-in mean ± location SD')
plt.plot(xx+.06,q.D_C_prediction_mean,'s',label='pair-correlation prediction')
plt.xticks(xx,['first 10k','near 10^12','near 10^21']); plt.ylabel(r'$D_C$')
plt.title('Secondary zeta controls: Gaussian Gram energy (m=512)')
plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'04_zeta_height_controls_Dc_m512.png',dpi=180); plt.close()

# 5 height control inertia m512
plt.figure(figsize=(8,5.2))
for ds,label in [('low_height_first_10000','first 10k'),('near_1e12','near 10^12'),('near_1e21','near 10^21')]:
 g=agg[(agg.dataset==ds)&(agg.m==512)]
 plt.plot(g['lambda'],g.p_pos_mean,marker='o',label=label)
plt.xlabel(r'$\lambda$'); plt.ylabel('mean resolved positive fraction')
plt.title('Zeta-height control comparison: positive inertia (m=512)')
plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'05_zeta_height_controls_positive_inertia_m512.png',dpi=180); plt.close()

# 6 bound slack primary
plt.figure(figsize=(8,5.2))
plt.plot(x['lambda'],x.bound_slack_mean,marker='o')
plt.xlabel(r'$\lambda$'); plt.ylabel(r'mean $p_{pos}-b_{pos}$')
plt.title('Slack in the generic positive-inertia lower bound (primary, m=512)')
plt.grid(alpha=.25); plt.tight_layout()
plt.savefig(FIG/'06_primary_positive_bound_slack_m512.png',dpi=180); plt.close()

# 7 location SD primary by block size
plt.figure(figsize=(8,5.2))
for m in [128,256,512]:
 g=agg[(agg.dataset=='low_height_first_10000')&(agg.m==m)]
 plt.plot(g['lambda'],g.p_pos_sd_location,marker='o',label=f'm={m}')
plt.xlabel(r'$\lambda$'); plt.ylabel('descriptive SD across 16 locations')
plt.title('Finite-window location variability of positive inertia')
plt.grid(alpha=.25); plt.legend(); plt.tight_layout()
plt.savefig(FIG/'07_primary_location_variability.png',dpi=180); plt.close()

print('created',len(list(FIG.glob('*.png'))),'figures')
