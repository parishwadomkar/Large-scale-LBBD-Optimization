@echo off
cd /d %~dp0\..
python src_lbbd\run_lbbd.py --dataset small --scenario with_redirection --threads 8 --master-gap 0.0002 --subproblem-gap 0.0001 --lbbd-gap 0.0002 --max-iterations 40 --cut-strategy standard
