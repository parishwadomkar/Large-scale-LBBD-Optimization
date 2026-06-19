@echo off
cd /d C:\Users\omkarp\Downloads\Opti
call conda activate opti
python src_lbbd\run_lbbd_final.py --dataset full --scenario with_redirection --preset full_trial --threads 16
