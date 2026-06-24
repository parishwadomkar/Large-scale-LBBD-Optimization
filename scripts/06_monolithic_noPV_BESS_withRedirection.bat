@echo off
cd /d "%~dp0.."
call conda activate omkarp
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
set DATASET=full
set THREADS=10
set MIPGAP=0.0001
python src\run_optimization.py --dataset %DATASET% --scenario with_redirection --threads %THREADS% --mip-gap %MIPGAP% --disable-pv
pause
