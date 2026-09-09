========== MONOLITHIC TERMINAL LOG ==========
Run transcript : C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
=============================================

Project root  : C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization
Dataset       : small
Run profile   : monolithic.small
Scenario      : with_redirection
Disable PV    : False
Disable BESS  : False
Hard no-slack : False
Sensitivity overrides: none
Run directory : C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty
Loading inputs...
Preprocessing inputs...
Hex cells: 57
Active redirection arc-slots: 57,600
Building type-aware Pyomo model...
Solving with Gurobi...
Read LP format model from file C:\Users\omkarp\AppData\Local\Temp\tmpinac14rd.pyomo.lp
Reading time = 3.20 seconds
x1: 1189599 rows, 1340745 columns, 7590291 nonzeros
Set parameter Threads to value 16
Set parameter Presolve to value 2
Set parameter NumericFocus to value 2
Set parameter Heuristics to value 0.1
Set parameter MIPGap to value 1e-05
Set parameter NodefileStart to value 0.5
Set parameter Cuts to value 3
Set parameter TimeLimit to value 21600
Set parameter MIPFocus to value 1
Set parameter LogFile to value "C:/Users/omkarp/IdeaProjects/VSCode/Large-scale-LBBD-Optimization/runs/2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty/logs/gurobi_run.log"
Set parameter NodefileDir to value "C:/Users/omkarp/IdeaProjects/VSCode/Large-scale-LBBD-Optimization/runs/gurobi_nodefiles"
Gurobi Optimizer version 13.0.1 build v13.0.1rc0 (win64 - Windows 11+.0 (26200.2))

CPU model: 12th Gen Intel(R) Core(TM) i7-12700, instruction set [SSE2|AVX|AVX2]
Thread count: 12 physical cores, 20 logical processors, using up to 16 threads

Non-default parameters:
TimeLimit  21600
MIPGap  1e-05
Heuristics  0.1
MIPFocus  1
NodefileStart  0.5
Cuts  3
NumericFocus  2
Presolve  2
Threads  16

Optimize a model with 1189599 rows, 1340745 columns and 7590291 nonzeros (Max)
Model fingerprint: 0xe12e50c2
Model has 616605 linear objective coefficients
Variable types: 1192428 continuous, 148317 integer (90432 binary)
Coefficient statistics:
  Matrix range     [4e-05, 2e+03]
  Objective range  [1e+01, 6e+05]
  Bounds range     [1e+00, 7e+02]
  RHS range        [9e-02, 7e+02]

Found heuristic solution: objective -5.39435e+11
Presolve removed 130482 rows and 146246 columns (presolve time = 5s)...
Presolve removed 155121 rows and 167079 columns (presolve time = 10s)...
Presolve removed 266862 rows and 271905 columns (presolve time = 16s)...
Presolve removed 318501 rows and 325295 columns (presolve time = 20s)...
Presolve removed 420027 rows and 427444 columns (presolve time = 32s)...
Presolve removed 569507 rows and 589566 columns (presolve time = 121s)...
Presolve removed 569507 rows and 589566 columns
Presolve time: 121.60s
Presolved: 620092 rows, 751179 columns, 4258963 nonzeros
Found heuristic solution: objective -3.97883e+11
Variable types: 659256 continuous, 91923 integer (54438 binary)
Root relaxation presolve removed 135511 rows and 207373 columns
Root relaxation presolved: 484581 rows, 543806 columns, 3049852 nonzeros

Deterministic concurrent LP optimizer: primal simplex, dual simplex, and barrier
Showing barrier log only...

Root barrier log...

Ordering time: 2.14s

Barrier statistics:
 Dense cols : 135
 AA' NZ     : 3.455e+06
 Factor NZ  : 1.597e+07 (roughly 500 MB of memory)
 Factor Ops : 1.942e+09 (less than 1 second per iteration)
 Threads    : 14

                  Objective                Residual
Iter       Primal          Dual         Primal    Dual     Compl     Time
   0  -5.41363247e+12  5.07514625e+13  5.50e+04 2.31e+06  3.85e+09   128s
   1   7.98853574e+11  5.64405797e+13  4.48e+04 1.72e+06  2.97e+09   128s
   2   2.16654786e+12  5.85772058e+13  3.27e+04 6.74e+05  2.11e+09   129s
   3   2.10394374e+12  5.74014081e+13  2.90e+04 3.09e+05  1.82e+09   130s
   4   1.95683423e+12  5.36891633e+13  2.12e+04 3.61e+04  1.33e+09   131s
   5   1.36669776e+12  4.77564971e+13  1.26e+04 4.27e-05  7.91e+08   131s
   6   8.43176925e+11  3.55265974e+13  6.19e+03 2.59e-05  3.80e+08   132s
   7   5.76218507e+11  2.54956264e+13  3.69e+03 3.34e-05  2.19e+08   132s
   8   2.83105147e+11  1.63691927e+13  1.54e+03 4.30e-05  8.96e+07   133s
   9   1.01879316e+11  9.44275534e+12  5.29e+02 1.52e-05  3.14e+07   133s
  10   2.32418988e+10  6.47113601e+12  1.71e+02 8.42e-06  1.19e+07   134s
  11  -2.90834795e+09  3.56625896e+12  4.85e+01 3.38e-06  4.22e+06   135s
  12  -6.02832946e+09  9.31839643e+11  1.21e+01 3.07e-06  9.15e+05   136s
  13  -2.38193427e+09  2.10444598e+11  1.29e+00 1.24e-06  1.59e+05   136s
  14  -4.36141796e+08  3.51819056e+10  1.30e-01 3.27e-07  2.48e+04   137s
  15  -1.08081983e+07  1.09921158e+10  1.31e-02 1.14e-07  7.59e+03   137s
  16   4.94558916e+07  4.87227334e+09  2.45e-03 5.62e-08  3.32e+03   138s
  17   6.25934528e+07  2.61335646e+09  7.90e-04 2.95e-08  1.76e+03   139s
  18   6.92185528e+07  9.93157871e+08  3.26e-04 9.97e-09  6.36e+02   139s
  19   7.48260216e+07  7.32537678e+08  2.16e-04 7.22e-09  4.53e+02   141s
  20   8.10319917e+07  4.93693201e+08  1.45e-04 5.59e-09  2.84e+02   142s
  21   8.50171497e+07  4.15165229e+08  1.11e-04 5.59e-09  2.27e+02   143s
  22   8.88505269e+07  3.15150304e+08  8.53e-05 5.59e-09  1.56e+02   144s
  23   9.31879105e+07  2.66611655e+08  6.35e-05 5.59e-09  1.19e+02   146s
  24   9.64158655e+07  2.18393241e+08  5.19e-05 5.59e-09  8.40e+01   147s
  25   1.00580899e+08  1.98348700e+08  3.95e-05 5.59e-09  6.73e+01   148s
  26   1.04999324e+08  1.75842903e+08  2.94e-05 5.59e-09  4.88e+01   150s
  27   1.09001420e+08  1.64571962e+08  2.17e-05 5.59e-09  3.83e+01   151s
  28   1.12881239e+08  1.54069467e+08  1.51e-05 5.59e-09  2.84e+01   153s
  29   1.15892219e+08  1.47788547e+08  1.08e-05 5.59e-09  2.20e+01   154s
  30   1.17989963e+08  1.42067824e+08  8.18e-06 7.45e-09  1.66e+01   155s
  31   1.20018035e+08  1.37886301e+08  5.99e-06 7.45e-09  1.23e+01   157s
  32   1.21838628e+08  1.34790232e+08  4.30e-06 7.45e-09  8.92e+00   158s
  33   1.22862951e+08  1.32356476e+08  3.41e-06 7.45e-09  6.54e+00   160s
  34   1.23887393e+08  1.31424651e+08  2.58e-06 7.45e-09  5.19e+00   161s
  35   1.24753147e+08  1.30317538e+08  1.91e-06 1.12e-08  3.83e+00   163s
  36   1.25395000e+08  1.29731647e+08  1.44e-06 7.45e-09  2.99e+00   164s
  37   1.25854708e+08  1.29304487e+08  1.11e-06 7.45e-09  2.38e+00   166s
  38   1.26245385e+08  1.28758145e+08  8.32e-07 7.45e-09  1.73e+00   169s
  39   1.26534465e+08  1.28531009e+08  6.34e-07 1.12e-08  1.37e+00   173s
  40   1.26723673e+08  1.28336760e+08  5.04e-07 7.45e-09  1.11e+00   176s
  41   1.26828585e+08  1.28124465e+08  4.34e-07 7.45e-09  8.92e-01   179s
  42   1.26976221e+08  1.28012582e+08  3.37e-07 1.12e-08  7.14e-01   184s
  43   1.27108802e+08  1.27905119e+08  2.50e-07 7.45e-09  5.48e-01   188s
  44   1.27209210e+08  1.27794097e+08  1.85e-07 7.45e-09  4.03e-01   191s
  45   1.27237503e+08  1.27760595e+08  1.68e-07 7.45e-09  3.60e-01   194s
  46   1.27279378e+08  1.27708774e+08  1.41e-07 1.12e-08  2.96e-01   198s
  47   1.27328378e+08  1.27677844e+08  1.11e-07 7.45e-09  2.41e-01   201s
  48   1.27358340e+08  1.27645033e+08  9.29e-08 7.45e-09  1.97e-01   204s
  49   1.27385123e+08  1.27617004e+08  7.73e-08 7.45e-09  1.60e-01   207s
  50   1.27417401e+08  1.27604426e+08  5.84e-08 7.45e-09  1.29e-01   210s
  51   1.27430610e+08  1.27580974e+08  5.09e-08 7.45e-09  1.04e-01   213s
  52   1.27446516e+08  1.27567756e+08  4.20e-08 7.45e-09  8.35e-02   215s
  53   1.27453594e+08  1.27561203e+08  3.81e-08 7.45e-09  7.41e-02   217s
  54   1.27467688e+08  1.27553771e+08  3.01e-08 5.59e-09  5.93e-02   219s
  55   1.27475835e+08  1.27547623e+08  2.55e-08 5.59e-09  4.94e-02   222s
  56   1.27488100e+08  1.27541734e+08  1.85e-08 5.59e-09  3.69e-02   224s
  57   1.27495823e+08  1.27536956e+08  1.42e-08 5.59e-09  2.83e-02   226s
  58   1.27499393e+08  1.27534440e+08  1.23e-08 5.59e-09  2.41e-02   229s
  59   1.27505309e+08  1.27528563e+08  9.29e-09 3.73e-09  1.60e-02   232s
  60   1.27509188e+08  1.27526796e+08  7.21e-09 2.79e-09  1.21e-02   234s
  61   1.27512936e+08  1.27526109e+08  5.90e-09 2.33e-09  9.07e-03   237s
  62   1.27516154e+08  1.27525055e+08  5.12e-09 1.86e-09  6.13e-03   241s
  63   1.27517800e+08  1.27524649e+08  4.70e-09 1.53e-09  4.72e-03   244s
  64   1.27518363e+08  1.27524068e+08  4.57e-09 1.62e-09  3.93e-03   246s
  65   1.27519447e+08  1.27523732e+08  4.27e-09 1.82e-09  2.95e-03   249s
  66   1.27519995e+08  1.27523631e+08  4.13e-09 1.54e-09  2.50e-03   252s
  67   1.27520789e+08  1.27523507e+08  2.77e-08 1.87e-09  1.87e-03   256s
  68   1.27521249e+08  1.27523352e+08  5.72e-08 1.80e-09  1.45e-03   260s
  69   1.27521576e+08  1.27523247e+08  1.08e-07 1.86e-09  1.15e-03   266s
  70   1.27521822e+08  1.27523192e+08  1.27e-07 1.86e-09  9.43e-04   272s
  71   1.27522057e+08  1.27523162e+08  2.55e-07 1.90e-09  7.61e-04   277s
  72   1.27522125e+08  1.27523103e+08  2.37e-07 2.00e-09  6.74e-04   283s
  73   1.27522258e+08  1.27523079e+08  2.71e-07 2.04e-09  5.65e-04   289s
  74   1.27522363e+08  1.27523069e+08  1.53e-07 1.95e-09  4.86e-04   296s
  75   1.27522431e+08  1.27523022e+08  9.77e-08 1.86e-09  4.07e-04   303s
  76   1.27522528e+08  1.27523010e+08  3.04e-07 3.53e-09  3.32e-04   310s

Barrier solved model in 76 iterations and 309.91 seconds (229.65 work units)
Optimal objective 1.27522528e+08


Root crossover log...

  284181 DPushes remaining with DInf 0.0000000e+00               310s
    7140 DPushes remaining with DInf 0.0000000e+00               315s
       0 DPushes remaining with DInf 0.0000000e+00               320s

  409783 PPushes remaining with PInf 9.6500728e-01               320s
  163173 PPushes remaining with PInf 1.1924928e+00               321s
       0 PPushes remaining with PInf 7.6922738e-06               322s

  Push phase complete: Pinf 7.6922738e-06, Dinf 5.2787142e+06    322s


Root simplex log...

Iteration    Objective       Primal Inf.    Dual Inf.      Time
  534093    1.2752294e+08   0.000000e+00   5.278714e+06    322s
  536159    1.2752294e+08   0.000000e+00   0.000000e+00    325s
Crossover time: 14.75 seconds (16.00 work units)
Concurrent spin time: 11.27s

Solved with barrier
  536159    1.2752294e+08   0.000000e+00   5.120566e+00    325s
  536160    1.2752294e+08   0.000000e+00   0.000000e+00    325s

Extra simplex iterations after uncrush: 1

Root relaxation: objective 1.275229e+08, 536160 iterations, 202.78 seconds (121.49 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 1.2752e+08    0  350 -3.979e+11 1.2752e+08   100%     -  337s
H    0     0                    -2.69616e+09 1.2752e+08   105%     -  340s
H    0     0                    -2.38903e+09 1.2752e+08   105%     -  344s
     0     0 1.2748e+08    0  442 -2.389e+09 1.2748e+08   105%     -  371s
     0     0 1.2747e+08    0  449 -2.389e+09 1.2747e+08   105%     -  381s
     0     0 1.2747e+08    0  452 -2.389e+09 1.2747e+08   105%     -  382s
     0     0 1.2747e+08    0  462 -2.389e+09 1.2747e+08   105%     -  384s
     0     0 1.2747e+08    0  458 -2.389e+09 1.2747e+08   105%     -  385s
     0     0 1.2747e+08    0  492 -2.389e+09 1.2747e+08   105%     -  387s
     0     0 1.2746e+08    0  494 -2.389e+09 1.2746e+08   105%     -  388s
     0     0 1.2746e+08    0  496 -2.389e+09 1.2746e+08   105%     -  390s
     0     0 1.2746e+08    0  497 -2.389e+09 1.2746e+08   105%     -  391s
     0     0 1.2746e+08    0  487 -2.389e+09 1.2746e+08   105%     -  393s
     0     0 1.2746e+08    0  460 -2.389e+09 1.2746e+08   105%     -  394s
     0     0 1.2746e+08    0  446 -2.389e+09 1.2746e+08   105%     -  396s
     0     0 1.2746e+08    0  449 -2.389e+09 1.2746e+08   105%     -  397s
     0     0 1.2746e+08    0  442 -2.389e+09 1.2746e+08   105%     -  398s
     0     0 1.2746e+08    0  442 -2.389e+09 1.2746e+08   105%     -  399s
     0     0 1.2746e+08    0  442 -2.389e+09 1.2746e+08   105%     -  400s
     0     0 1.2746e+08    0  442 -2.389e+09 1.2746e+08   105%     -  401s
     0     0 1.2746e+08    0  443 -2.389e+09 1.2746e+08   105%     -  402s
     0     0 1.2746e+08    0  441 -2.389e+09 1.2746e+08   105%     -  403s
     0     0 1.2746e+08    0  427 -2.389e+09 1.2746e+08   105%     -  404s
     0     0 1.2746e+08    0  425 -2.389e+09 1.2746e+08   105%     -  406s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  407s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  408s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  409s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  410s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  411s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  412s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  413s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  414s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  415s
     0     0 1.2745e+08    0  428 -2.389e+09 1.2745e+08   105%     -  416s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  417s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  418s
     0     0 1.2745e+08    0  427 -2.389e+09 1.2745e+08   105%     -  419s
     0     0 1.2745e+08    0  427 -2.389e+09 1.2745e+08   105%     -  419s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  421s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  422s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  423s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  424s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  425s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  426s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  427s
     0     0 1.2745e+08    0  425 -2.389e+09 1.2745e+08   105%     -  428s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  429s
     0     0 1.2745e+08    0  426 -2.389e+09 1.2745e+08   105%     -  431s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  432s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  433s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  434s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  435s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  436s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  437s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  438s
     0     0 1.2745e+08    0  434 -2.389e+09 1.2745e+08   105%     -  439s
     0     0 1.2745e+08    0  435 -2.389e+09 1.2745e+08   105%     -  440s
     0     0 1.2745e+08    0  436 -2.389e+09 1.2745e+08   105%     -  440s
     0     0 1.2745e+08    0  436 -2.389e+09 1.2745e+08   105%     -  441s
     0     0 1.2745e+08    0  449 -2.389e+09 1.2745e+08   105%     -  442s
     0     0 1.2745e+08    0  443 -2.389e+09 1.2745e+08   105%     -  442s
     0     0 1.2745e+08    0  443 -2.389e+09 1.2745e+08   105%     -  443s
     0     0 1.2745e+08    0  443 -2.389e+09 1.2745e+08   105%     -  444s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  445s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  445s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  446s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  447s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  447s
     0     0 1.2744e+08    0  444 -2.389e+09 1.2744e+08   105%     -  448s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  449s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  450s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  451s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  451s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  452s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  452s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  453s
     0     0 1.2744e+08    0  451 -2.389e+09 1.2744e+08   105%     -  453s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  453s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  454s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  454s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  455s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  455s
     0     0 1.2744e+08    0  440 -2.389e+09 1.2744e+08   105%     -  456s
     0     0 1.2743e+08    0  440 -2.389e+09 1.2743e+08   105%     -  456s
     0     0 1.2743e+08    0  440 -2.389e+09 1.2743e+08   105%     -  457s
     0     0 1.2743e+08    0  440 -2.389e+09 1.2743e+08   105%     -  457s
     0     0 1.2743e+08    0  440 -2.389e+09 1.2743e+08   105%     -  458s
     0     0 1.2743e+08    0  439 -2.389e+09 1.2743e+08   105%     -  458s
     0     0 1.2743e+08    0  439 -2.389e+09 1.2743e+08   105%     -  459s
     0     0 1.2743e+08    0  439 -2.389e+09 1.2743e+08   105%     -  459s
     0     0 1.2743e+08    0  439 -2.389e+09 1.2743e+08   105%     -  460s
     0     0 1.2743e+08    0  438 -2.389e+09 1.2743e+08   105%     -  460s
     0     0 1.2743e+08    0  438 -2.389e+09 1.2743e+08   105%     -  461s
     0     0 1.2743e+08    0  438 -2.389e+09 1.2743e+08   105%     -  461s
     0     0 1.2743e+08    0  438 -2.389e+09 1.2743e+08   105%     -  462s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  462s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  463s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  464s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  464s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  465s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  465s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  466s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  466s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  467s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  467s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  467s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  468s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  468s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  469s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  469s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  470s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  470s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  470s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  471s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  471s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  472s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  472s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  472s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  473s
     0     0 1.2743e+08    0  437 -2.389e+09 1.2743e+08   105%     -  473s
     0     0 1.2743e+08    0  441 -2.389e+09 1.2743e+08   105%     -  474s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  474s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  475s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  475s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  475s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  476s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  476s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  477s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  477s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  477s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  478s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  478s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  478s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  479s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  479s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  480s
     0     0 1.2743e+08    0  442 -2.389e+09 1.2743e+08   105%     -  480s
     0     0 1.2736e+08    0  396 -2.389e+09 1.2736e+08   105%     -  483s
H    0     0                    -2.33332e+09 1.2736e+08   105%     -  487s
     0     0 1.2736e+08    0  398 -2.333e+09 1.2736e+08   105%     -  488s
     0     0 1.2736e+08    0  409 -2.333e+09 1.2736e+08   105%     -  489s
     0     0 1.2734e+08    0  398 -2.333e+09 1.2734e+08   105%     -  490s
     0     0 1.2734e+08    0  412 -2.333e+09 1.2734e+08   105%     -  490s
     0     0 1.2734e+08    0  415 -2.333e+09 1.2734e+08   105%     -  491s
     0     0 1.2734e+08    0  416 -2.333e+09 1.2734e+08   105%     -  492s
     0     0 1.2734e+08    0  417 -2.333e+09 1.2734e+08   105%     -  493s
     0     0 1.2734e+08    0  414 -2.333e+09 1.2734e+08   105%     -  493s
     0     0 1.2734e+08    0  415 -2.333e+09 1.2734e+08   105%     -  494s
     0     0 1.2734e+08    0  416 -2.333e+09 1.2734e+08   105%     -  495s
     0     0 1.2734e+08    0  404 -2.333e+09 1.2734e+08   105%     -  495s
     0     0 1.2730e+08    0  446 -2.333e+09 1.2730e+08   105%     -  509s
     0     0 1.2730e+08    0  302 -2.333e+09 1.2730e+08   105%     -  520s
H    0     0                    -1.60616e+09 1.2730e+08   108%     -  534s
H    0     0                    -1.56000e+09 1.2730e+08   108%     -  534s
H    0     0                    -1.55475e+09 1.2730e+08   108%     -  535s
H    0     0                    -1.55475e+09 1.2730e+08   108%     -  535s
H    0     0                    -1.55039e+09 1.2730e+08   108%     -  536s
H    0     0                    -1.55039e+09 1.2730e+08   108%     -  536s
H    0     0                    -1.55028e+09 1.2730e+08   108%     -  536s
H    0     0                    -1.55028e+09 1.2730e+08   108%     -  536s
H    0     0                    -1.54595e+09 1.2730e+08   108%     -  536s
H    0     0                    -1.53713e+09 1.2730e+08   108%     -  536s
H    0     0                    -8.48823e+08 1.2730e+08   115%     -  537s
H    0     0                    -8.48807e+08 1.2730e+08   115%     -  537s
H    0     0                    -8.43763e+08 1.2730e+08   115%     -  537s
H    0     0                    -8.29764e+08 1.2730e+08   115%     -  538s
H    0     0                    -8.29764e+08 1.2730e+08   115%     -  538s
H    0     0                    -8.16957e+08 1.2730e+08   116%     -  538s
H    0     0                    -8.16948e+08 1.2730e+08   116%     -  587s
H    0     0                    -6.68896e+08 1.2730e+08   119%     -  591s
H    0     0                    -6.68627e+08 1.2730e+08   119%     -  592s
H    0     0                    -6.65759e+08 1.2730e+08   119%     -  592s
H    0     0                    -6.62605e+08 1.2730e+08   119%     -  594s
H    0     0                    -6.38660e+08 1.2730e+08   120%     -  594s
H    0     0                    -5.05906e+07 1.2730e+08   352%     -  595s
H    0     0                    7.672342e+07 1.2730e+08  65.9%     -  596s
H    0     0                    9.071716e+07 1.2730e+08  40.3%     -  597s
H    0     0                    9.280691e+07 1.2730e+08  37.2%     -  597s
H    0     0                    1.062821e+08 1.2730e+08  19.8%     -  597s
H    0     0                    1.223602e+08 1.2730e+08  4.04%     -  597s
H    0     0                    1.238469e+08 1.2730e+08  2.79%     -  598s
H    0     0                    1.266820e+08 1.2730e+08  0.49%     -  602s
H    0     0                    1.267296e+08 1.2730e+08  0.45%     -  602s
H    0     0                    1.268113e+08 1.2730e+08  0.39%     -  603s
H    0     0                    1.269118e+08 1.2730e+08  0.31%     -  604s
H    0     0                    1.269118e+08 1.2730e+08  0.31%     -  606s
H    0     2                    1.269756e+08 1.2730e+08  0.26%     -  626s
     0     2 1.2730e+08    0  302 1.2698e+08 1.2730e+08  0.26%     -  626s
H    1     4                    1.269756e+08 1.2730e+08  0.26%   0.0  633s
H    2     4                    1.269765e+08 1.2730e+08  0.26%  86.5  633s
     3     8 1.2711e+08    2  293 1.2698e+08 1.2721e+08  0.19%   947  636s
    15    15 1.2702e+08    4  318 1.2698e+08 1.2711e+08  0.11%   522  644s
    29     8 1.2699e+08    5  311 1.2698e+08 1.2708e+08  0.08%   387  649s
    44     6 1.2699e+08    6  300 1.2698e+08 1.2705e+08  0.06%   351  653s
    52    12 1.2699e+08    7  309 1.2698e+08 1.2702e+08  0.04%   341  658s
    58    13     cutoff    8      1.2698e+08 1.2702e+08  0.04%   367  665s
    70    11 1.2700e+08    9  366 1.2698e+08 1.2702e+08  0.03%   390  672s
    83    10 1.2700e+08   10  364 1.2698e+08 1.2700e+08  0.02%   421  676s
    94    16 1.2698e+08   11  353 1.2698e+08 1.2700e+08  0.02%   392  681s
   104    16 1.2698e+08   12  347 1.2698e+08 1.2700e+08  0.02%   367  689s
   120    27 1.2698e+08   13  347 1.2698e+08 1.2700e+08  0.02%   397  700s
   136    48     cutoff   14      1.2698e+08 1.2699e+08  0.01%   395  707s
H  139    48                    1.269877e+08 1.2699e+08  0.01%   390  707s
   165    23 1.2699e+08   15  316 1.2699e+08 1.2699e+08  0.01%   336  712s
   211    44 1.2699e+08   16  329 1.2699e+08 1.2699e+08  0.01%   278  719s
   240    59 1.2699e+08   18  285 1.2699e+08 1.2699e+08  0.00%   255  731s
H  256    82                    1.269890e+08 1.2699e+08  0.00%   243  750s
H  260    82                    1.269903e+08 1.2699e+08  0.00%   240  750s
   288    91     cutoff   21      1.2699e+08 1.2699e+08  0.00%   220  759s
   391   160 1.2699e+08   25  326 1.2699e+08 1.2699e+08  0.00%   169  778s
   520   343 1.2699e+08   20  297 1.2699e+08 1.2699e+08  0.00%   133  813s
   740   583 1.2699e+08   33  296 1.2699e+08 1.2699e+08  0.00%  96.2  894s
  1108   788 1.2699e+08   56  273 1.2699e+08 1.2699e+08  0.00%  65.8  980s
H 1476   928                    1.269919e+08 1.2699e+08  0.00%  50.9 1097s
H 1497   928                    1.269919e+08 1.2699e+08  0.00%  50.2 1097s
H 1537   928                    1.269919e+08 1.2699e+08  0.00%  49.0 1097s
H 1728   928                    1.269919e+08 1.2699e+08  0.00%  44.0 1098s

Cutting planes:
  Lift-and-project: 139
  Implied bound: 957
  Projected implied bound: 225
  MIR: 2022
  Flow cover: 1354
  Flow path: 461
  RLT: 13
  Relax-and-lift: 28

Explored 1811 nodes (642255 simplex iterations) in 1099.62 seconds (907.90 work units)
Thread count was 16 (of 20 available processors)

Solution count 10: 1.26992e+08 1.26992e+08 1.26992e+08 ... 1.26976e+08

Optimal solution found (tolerance 1.00e-05)
Best objective 1.269919459744e+08, best bound 1.269932139162e+08, gap 0.0010%

- Status: ok
  Return code: 0
  Message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Termination condition: optimal
  Termination message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Wall time: 1099.641000032425
  Error rc: 0


================  OPTIMAL ANNUAL PROFIT  ================
Total profit : 126,991,946 SEK / yr

==================  BREAKDOWN  =================
Revenue (all chargers)             :   178,925,070
Opex - grid purchases              :    39,770,307
Opex - redirection distance        :       759,802
Opex - redirection price comp.     :             0
Opex - unmet-demand penalty        :             0
Capex - chargers                   :     4,379,017
Capex - PV & batteries             :     7,023,998
----------------------------------------------------------
Slow   chargers:         72 | energy:   1,194,426.0 | cap ratio: 0.172
Medium chargers:        402 | energy:  18,823,635.6 | cap ratio: 0.243
Fast   chargers:         41 | energy:   9,140,602.0 | cap ratio: 0.509
==========================================================

Writing CSV/XLSX outputs...
Combined XLSX written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty\results
Generating result figures...
Figure generated: economic_breakdown
Figure generated: charger_deployment
Figure generated: monthly_energy
Figure generated: dispatch_January
Figure generated: dispatch_April
Figure generated: dispatch_July
Figure generated: dispatch_October
Figure generated: bess_soc
Figure generated: bess_operation_January
Figure generated: bess_operation_July
Figure generated: demand_supply_balance
Figure generated: redirection_heatmap
Figure generated: redirection_type_matrix
Figure skipped: decomposition_convergence (No decomposition iteration history)
Figure skipped: decomposition_cut_generation (No decomposition iteration history)
Figure skipped: lbbd_cut_families (No LBBD iteration history)
Figure skipped: lbbd_candidate_bounds (No LBBD iteration history)
Figure skipped: lbbd_infrastructure_evolution (No LBBD iteration history)
Figure skipped: lbbd_iteration_timing (No LBBD iteration history)
Figure skipped: lbbd_gap_diagnostics (No LBBD iteration history)
Figure skipped: lbbd_adaptive_master_control (No LBBD iteration history)
Figure skipped: lbbd_candidate_reuse (No LBBD iteration history)
Figure skipped: slack (No positive slack)
Figure generated: spatial_maps
Figures written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty\figures
Run finished successfully. Run directory: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty

Terminal transcript written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_190033_small_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
