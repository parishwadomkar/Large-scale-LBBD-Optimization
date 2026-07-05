@echo off
cd /d %~dp0\..
REM Replace RUN_FOLDER names before executing.
python src_lbbd\compare_runs.py --lbbd-run "runs\<LBBD_RUN_FOLDER>" --monolithic-run "runs\<MONOLITHIC_RUN_FOLDER>"
