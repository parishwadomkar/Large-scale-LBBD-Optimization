@echo off
cd /d "%~dp0.."
call conda activate omkarp
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8:replace

set DATASET=full
set THREADS=16
set MASTER_GAP=0.002
set SUBPROBLEM_GAP=0.002
set LBBD_GAP=0.00025
set MAX_ITER=1
set TIME_LIMIT=64800

python src_lbbd\run_lbbd_final.py ^
  --dataset %DATASET% ^
  --scenario no_redirection ^
  --preset full_trial ^
  --threads %THREADS% ^
  --master-gap %MASTER_GAP% ^
  --subproblem-gap %SUBPROBLEM_GAP% ^
  --lbbd-gap %LBBD_GAP% ^
  --max-iterations %MAX_ITER% ^
  --time-limit %TIME_LIMIT% ^
  --disable-pv ^
  --disable-bess

pause
