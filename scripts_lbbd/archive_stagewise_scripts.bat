@echo off
cd /d C:\Users\omkarp\Downloads\Opti
if not exist scripts_lbbd\_archive_stage_development mkdir scripts_lbbd\_archive_stage_development
for %%F in (scripts_lbbd\stage0*.bat scripts_lbbd\stage1*.bat scripts_lbbd\stage2*.bat scripts_lbbd\stage3*.bat scripts_lbbd\stage4*.bat scripts_lbbd\stage5*.bat scripts_lbbd\stage6*.bat) do (
  if exist "%%F" move /Y "%%F" scripts_lbbd\_archive_stage_development\ >nul
)
echo Stagewise development scripts moved to scripts_lbbd\_archive_stage_development.
echo Core src_lbbd modules were not deleted because the final runner imports the validated implementation.
