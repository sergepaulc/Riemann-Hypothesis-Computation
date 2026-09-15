#!/usr/bin/env python3
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE=Path(__file__).resolve().parents[1]
DF=pd.read_csv(BASE/'02_results/all_window_endpoints.csv')
DEC=pd.read_csv(BASE/'02_results/mu4_difference_decomposition_vs_cue.csv')
H=json.loads((BASE/'02_results/homometric_control.json').read_text())
OUT=BASE/'03_figures'
OUT.mkdir(exist_ok=True)
order=['D0_first_10000','D1_near_1e12','D2_near_1e21','CUE']
labels=['zeta first 10k','zeta near $10^{12}$','zeta near $10^{21}$','CUE']
for metric,title,ylabel in [
    ('mu2','Second sinc-kernel moment: zeta and CUE',r'$\mu_2$'),
    ('mu4_raw','Raw fourth sinc-kernel moment: zeta and CUE',r'$\mu_4$'),
    ('mu4_gt2','Collision-reduced fourth-moment component: zeta and CUE',r'$\mu_4^{(>2)}$')]:
    data=[DF.loc[DF.source==g,metric].to_numpy() for g in order]
    fig,ax=plt.subplots(figsize=(9,5.5))
    ax.boxplot(data,tick_labels=labels,showmeans=True)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x',rotation=15)
    ax.grid(axis='y',alpha=.25)
    fig.tight_layout()
    fig.savefig(OUT/f'{metric}_zeta_cue_zoom.png',dpi=180)
    plt.close(fig)

# Fourth-moment difference decomposition.
fig,ax=plt.subplots(figsize=(9,5.5))
x=np.arange(len(DEC))
width=.25
ax.bar(x-width,DEC['raw_mu4_difference_vs_CUE'],width,label=r'raw $\mu_4$ difference')
ax.bar(x,DEC['pair_part_difference'],width,label='pair-part difference')
ax.bar(x+width,DEC['gt2_difference'],width,label=r'$\mu_4^{(>2)}$ difference')
ax.axhline(0,linewidth=1)
ax.set_xticks(x,['first 10k','near $10^{12}$','near $10^{21}$'])
ax.set_ylabel('zeta mean minus CUE mean')
ax.set_title('Decomposition of the fourth-moment displacement from CUE')
ax.legend()
ax.grid(axis='y',alpha=.25)
fig.tight_layout()
fig.savefig(OUT/'mu4_difference_decomposition_vs_cue.png',dpi=180)
plt.close(fig)

# Homometric moment comparison.
orders=np.array([1,2,3,4])
A=np.array([H['moments_A'][str(k)] for k in orders])
B=np.array([H['moments_B'][str(k)] for k in orders])
fig,ax=plt.subplots(figsize=(8,5))
ax.plot(orders,A,marker='o',label='homometric set A')
ax.plot(orders,B,marker='s',label='homometric set B')
ax.set_xticks(orders)
ax.set_xlabel('moment order $k$')
ax.set_ylabel(r'$\mu_k$')
ax.set_title('Same pair-distance multiset; first separation at the fourth moment')
ax.legend()
ax.grid(alpha=.25)
fig.tight_layout()
fig.savefig(OUT/'homometric_moment_comparison.png',dpi=180)
plt.close(fig)
print('Experiment 3BS v1.1 paper figures generated')
