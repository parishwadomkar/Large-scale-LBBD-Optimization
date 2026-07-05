# Final LBBD module

This patch keeps the validated monolithic-comparable LBBD implementation in:

- `src_lbbd/`
- `scripts_lbbd/`

The run folders are named as `LBBD_Standard` for standard dual cuts and `LBBD_advCuts_<strategy>` for diagnostic advanced cuts.

Recommended final small feasibility run:

```bat
python src_lbbd\run_lbbd.py --dataset small --scenario with_redirection --threads 8 --master-gap 0.0005 --subproblem-gap 0.0001 --lbbd-gap 0.0005 --max-iterations 30 --cut-strategy standard
```

Recommended full-data run on the workstation/HPC:

```bat
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --threads 16 --master-gap 0.002 --subproblem-gap 0.001 --lbbd-gap 0.001 --max-iterations 25 --time-limit 64800 --cut-strategy standard
```

Use corepoint only as a diagnostic. It may produce stronger cuts but was slower on the validated small instance.
