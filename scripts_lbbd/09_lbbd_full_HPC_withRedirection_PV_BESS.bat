@echo off
setlocal
cd /d "%~dp0\.."

REM Production cold-start full-data LBBD run.
REM No previous run, bootstrap checkpoint, monolithic seed, or external investment is read.
REM Internal LP/bootstrap candidates and MIP starts are generated only from this run's data/config.
REM The 20-day wall-clock allowance is a safety ceiling; convergence may occur much earlier.
python src_lbbd\run_lbbd.py ^
  --dataset full ^
  --scenario with_redirection ^
  --threads 10 ^
  --subproblem-threads 2 ^
  --first-master-lp-bootstrap ^
  --bootstrap-hall-repair-passes 3 ^
  --exact-slack-repair-passes 2 ^
  --integer-only-master-start ^
  --bootstrap-hall-refinement-rounds 0 ^
  --lp-fallback-on-master-no-incumbent ^
  --bound-polish ^
  --bound-polish-trigger-gap 0.001 ^
  --master-gap 0.0001 ^
  --master-gap-tight 0.00002 ^
  --lbbd-gap 0.00025 ^
  --subproblem-gap 0.00001 ^
  --annual-lp-frequency 1 ^
  --annual-core-cut-frequency 1 ^
  --max-iterations 12 ^
  --time-limit 1728000 ^
  --master-time-limit 172800 ^
  --master-late-time-limit 172800 ^
  --subproblem-time-limit 172800 ^
  --annual-lp-time-limit 86400 ^
  --soft-mem-limit-gb 180 ^
  --nodefile-start 0.5 ^
  --nodefile-dir "runs\gurobi_nodefiles"

endlocal
