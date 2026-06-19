@echo off
cd /d "%~dp0.."
call conda activate opti
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace
python src\run_optimization.py --smoke
pause
