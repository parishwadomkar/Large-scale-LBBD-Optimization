# Clean LBBD scenario scripts
Scenarios:
1. noPV + noBESS + no redirection
2. noPV + noBESS + with redirection
3. PV + noBESS + no redirection
4. PV + noBESS + with redirection
5. noPV + BESS + no redirection
6. noPV + BESS + with redirection
7. PV + BESS + no redirection
8. PV + BESS + with redirection

```bat
python src_lbbd\run_lbbd_final.py
```

The with-redirection scripts use the validated acceleration settings:

```bat
--cut-strategy corepoint --mip-reconstruction-frequency 2
```

The no-redirection scripts use `--max-iterations 1` because no redirection subproblem/cuts are active.

Before running these scripts, ensure that the LBBD technology-switch hotfix is installed so that `--disable-pv` and `--disable-bess` are enforced correctly.

Recommended usage from the project root:

```bat
scripts_lbbd\01_lbbd_noPV_noBESS_noRedirection.bat
```

or run all eight sequentially:

```bat
scripts_lbbd\run_all_lbbd_01_to_08.bat
```

For long full-data runs, running one script at a time is safer than launching all eight at once.

