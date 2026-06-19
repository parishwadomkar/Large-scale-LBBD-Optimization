@echo off
cd /d C:\Users\omkarp\Downloads\Opti
call conda activate opti
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
set DATASET=full
set THREADS=10
set MIPGAP=0.0001
python src\run_optimization.py --dataset %DATASET% --scenario no_redirection --threads %THREADS% --mip-gap %MIPGAP%
pause
