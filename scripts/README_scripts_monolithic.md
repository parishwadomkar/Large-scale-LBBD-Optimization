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
python src\run_optimization.py --dataset small --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-pv --disable-bess
```

```bat
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-pv --disable-bess
```

```bat
python src\run_optimization.py --dataset small --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-bess
```

```bat
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-bess
```

```bat
python src\run_optimization.py --dataset small --scenario no_redirection --threads 10 --mip-gap 0.0001
```

```bat
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.001
```

```bat
python src\run_optimization.py --dataset small --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-pv
```

```bat
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-pv
```


-------------------------------------------------------------------------------
```bat
python src\run_optimization.py --dataset full --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-pv --disable-bess
```

```bat
python src\run_optimization.py --dataset full --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-pv --disable-bess
```

```bat
python src\run_optimization.py --dataset full --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-bess
```

```bat
python src\run_optimization.py --dataset full --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-bess
```

```bat
python src\run_optimization.py --dataset full --scenario no_redirection --threads 10 --mip-gap 0.0001 --disable-pv
```

```bat
python src\run_optimization.py --dataset full --scenario with_redirection --threads 10 --mip-gap 0.0001 --disable-pv
```

```bat
python src\run_optimization.py --dataset full --scenario no_redirection --threads 10 --mip-gap 0.0001
```

```bat
python src\run_optimization.py --dataset full --scenario with_redirection --threads 10 --mip-gap 0.0001

```

For long full-data runs, running one script at a time is safer than launching all eight at once.

