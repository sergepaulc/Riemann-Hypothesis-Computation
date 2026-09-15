# Project Montecito — Experiment 2 Independent Peer-Review Handoff

Please audit the frozen Experiment 2 primary package together with `Experiment2_Validation_Extension_v1.md`. The requested review should be adversarial and should not assume the reported conclusions are correct.

## Questions for the reviewer

1. Re-derive the finite-window pair-correlation/Frobenius formula, including the factor of 2, finite-density normalization `m(m-1)/L^2`, translation-edge factor `(L-u)`, and piecewise-bin integration.
2. Verify that `C_ij = exp(-(x_i-x_j)^2/(2 sigma^2))` is PSD and that the use of `eta_j(H_lambda)=1-lambda mu_j(C)` correctly determines inertia.
3. Check the sign-specific bound `n_pos >= tr(H)^2/||H||_F^2` under `tr(H)>0`, and assess whether its interpretation in the report is appropriately limited.
4. Audit the block manifest and confirm the 128/256/512 blocks are nested and selected without result-dependent tuning.
5. Check all claimed numerical sign resolutions and the screening/high-precision logic.
6. Assess whether the pair-bridge agreement is characterized correctly as an internal reconstruction/consistency result rather than an independent discovery.
7. Review the sigma=.5 and sigma=2 sensitivity findings and whether the conclusion "quantitative inertia is kernel dependent" is warranted.
8. Review the spectral-tail interpretation: low-height differences in upper-edge/low-tail quantiles versus relatively stable spectral median and later-lambda inertia.
9. Identify any result that should be downgraded, rerun, or rephrased before Experiment 2 is scientifically frozen.

## Freeze rule

Do not start Experiment 3 until this review is complete and any substantive issues are resolved.
