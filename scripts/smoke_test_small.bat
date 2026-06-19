@echo off
cd /d C:\Users\omkarp\Downloads\Opti
call conda activate opti
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
python src\run_optimization.py --dataset small --smoke
pause
