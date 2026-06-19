@echo off
cd /d C:\Users\omkarp\Downloads\Opti
call conda activate opti
python src_lbbd\run_lbbd_final.py --dataset small --scenario no_redirection --preset small_validation --threads 10 --master-gap 0.001 --subproblem-gap 0.001 --lbbd-gap 0.0001 --max-iterations 1
