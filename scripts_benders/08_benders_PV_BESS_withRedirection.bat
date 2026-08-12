@echo off
setlocal
cd /d "%~dp0.."
set "DATASET=%~1"
if "%DATASET%"=="" set "DATASET=full"

echo Running Benders: %DATASET% / PV_BESS_withRedirection
python src_benders\run_benders.py --dataset %DATASET% --scenario with_redirection
if errorlevel 1 exit /b %errorlevel%
endlocal
