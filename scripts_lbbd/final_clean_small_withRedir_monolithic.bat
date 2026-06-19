@echo off
cd /d C:\Users\omkarp\Downloads\Opti
call conda activate opti
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.001
