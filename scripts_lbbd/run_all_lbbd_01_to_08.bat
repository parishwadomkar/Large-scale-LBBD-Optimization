@echo off
cd /d "%~dp0.."

echo ======================================================
echo Running all eight full-data LBBD scenarios in sequence
echo ======================================================

echo.
echo [01/08] noPV noBESS no redirection
call scripts_lbbd\01_lbbd_noPV_noBESS_noRedirection.bat

echo.
echo [02/08] noPV noBESS with redirection
call scripts_lbbd\02_lbbd_noPV_noBESS_withRedirection.bat

echo.
echo [03/08] PV noBESS no redirection
call scripts_lbbd\03_lbbd_PV_noBESS_noRedirection.bat

echo.
echo [04/08] PV noBESS with redirection
call scripts_lbbd\04_lbbd_PV_noBESS_withRedirection.bat

echo.
echo [05/08] noPV BESS no redirection
call scripts_lbbd\05_lbbd_noPV_BESS_noRedirection.bat

echo.
echo [06/08] noPV BESS with redirection
call scripts_lbbd\06_lbbd_noPV_BESS_withRedirection.bat

echo.
echo [07/08] PV BESS no redirection
call scripts_lbbd\07_lbbd_PV_BESS_noRedirection.bat

echo.
echo [08/08] PV BESS with redirection
call scripts_lbbd\08_lbbd_PV_BESS_withRedirection.bat

echo.
echo All requested LBBD scripts finished.
pause
