@echo off
cd /d %~dp0\..
if exist src_lbbd_arcwitness rmdir /s /q src_lbbd_arcwitness
if exist src_lbbd_exact rmdir /s /q src_lbbd_exact
if exist scripts_lbbd_arcwitness rmdir /s /q scripts_lbbd_arcwitness
if exist scripts_lbbd_exact rmdir /s /q scripts_lbbd_exact
echo Old experimental LBBD folders removed. The maintained LBBD folders are src_lbbd and scripts_lbbd.
