@echo off
setlocal
cd /d "%~dp0.."
set "DATASET=%~1"
if "%DATASET%"=="" set "DATASET=full"

echo Running Benders: %DATASET% / PV_BESS_noRedirection
python src_benders\run_benders.py --dataset %DATASET% --scenario no_redirection
if errorlevel 1 exit /b %errorlevel%
endlocal
