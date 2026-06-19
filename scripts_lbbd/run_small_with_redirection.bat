@echo off
cd /d "%~dp0.."
call conda activate opti
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
python src_lbbd\run_lbbd.py --dataset small --scenario with_redirection --preset small_validation --threads 10 --cut-strategy corepoint --mip-reconstruction-frequency 2
pause
