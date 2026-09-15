"""
Project Montecito — Experiment 1 High-Height Replication
Core reproducibility notes.

Raw data:
  data/raw/zeros3.txt
  data/raw/zeros4.txt

The raw files store offsets from large base ordinates. Do not convert the full
10^21-scale ordinates to float64 before differencing.

Unfolding:
  x_n = (siegeltheta(gamma_n) - siegeltheta(gamma_1)) / pi

Primary statistic:
  D0.5 = 1 - observed_pairs(0<u<0.5) / GUE_expected_pairs(0<u<0.5)

GUE expected pairs use:
  rho_hat^2 * integral_0^0.5 R_GUE(u) * (L-u) du
where rho_hat^2 = N(N-1)/L^2 and
  R_GUE(u)=1-(sin(pi*u)/(pi*u))^2.

Primary histogram:
  Umax=30, bin_width=0.1, translation edge correction (L-u).
"""
