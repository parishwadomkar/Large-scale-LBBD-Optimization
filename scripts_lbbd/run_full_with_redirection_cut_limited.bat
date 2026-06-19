@echo off
cd /d "%~dp0.."
call conda activate opti
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --preset full_default --threads 16 --cut-strategy corepoint --mip-reconstruction-frequency 2 --max-cuts-per-iteration 300
pause
