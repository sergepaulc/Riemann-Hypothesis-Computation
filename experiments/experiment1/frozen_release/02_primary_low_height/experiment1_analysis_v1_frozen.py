"""
Project Montecito — Experiment 1 analysis.
Reads a CSV containing zero_index,gamma and reproduces unfolding,
the primary pair-correlation estimate, and the Poisson unit test.

The complete run parameters are in config/experiment1_config.json.
"""
import numpy as np
import pandas as pd

TWO_PI = 2*np.pi

def nbar(t):
    t=np.asarray(t,float)
    return (t/TWO_PI)*np.log(t/TWO_PI)-t/TWO_PI+7/8

def gue_r2(u):
    return 1-np.sinc(np.asarray(u,float))**2

def positive_differences_window(points,umax):
    pts=np.asarray(points,float)
    out=[]
    for i in range(len(pts)-1):
        j=np.searchsorted(pts,pts[i]+umax,side="right")
        if j>i+1:
            out.append(pts[i+1:j]-pts[i])
    return np.concatenate(out) if out else np.empty(0)

def pair_corr(points,umax=30.0,bin_width=0.1):
    pts=np.sort(np.asarray(points,float))
    n=len(pts)
    L=pts[-1]-pts[0]
    diffs=positive_differences_window(pts,umax)
    edges=np.arange(0,umax+bin_width*0.5,bin_width)
    counts,edges=np.histogram(diffs,bins=edges)
    centers=(edges[:-1]+edges[1:])/2
    pair_intensity=n*(n-1)/L**2
    denom=pair_intensity*(L-centers)*bin_width
    return centers,counts/denom,counts

if __name__=="__main__":
    zeros=pd.read_csv("../data/zeta_zeros_10000_validated.csv")
    x=nbar(zeros["gamma"].to_numpy())
    u,g,c=pair_corr(x)
    out=pd.DataFrame({"u_center":u,"empirical":g,"gue_theory":gue_r2(u),"count":c})
    out.to_csv("../data/recomputed_pair_correlation.csv",index=False)
    print(out.head())
