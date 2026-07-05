@echo off
cd /d %~dp0\..
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --threads 6 --master-gap 0.005 --subproblem-gap 0.001 --lbbd-gap 0.003 --max-iterations 20 --time-limit 64800 --cut-strategy standard
