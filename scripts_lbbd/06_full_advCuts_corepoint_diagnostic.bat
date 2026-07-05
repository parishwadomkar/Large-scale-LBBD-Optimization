@echo off
cd /d %~dp0\..
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --threads 12 --master-gap 0.002 --subproblem-gap 0.001 --lbbd-gap 0.001 --max-iterations 25 --time-limit 64800 --cut-strategy corepoint --core-weight 0.35 --pareto-tolerance 1e-7
