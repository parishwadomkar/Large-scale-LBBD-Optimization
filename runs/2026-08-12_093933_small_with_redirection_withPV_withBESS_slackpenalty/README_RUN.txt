========== MONOLITHIC TERMINAL LOG ==========
Run transcript : C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
=============================================

Project root  : C:\Users\omkarp\Downloads\Opti
Dataset       : small
Run profile   : monolithic.small
Scenario      : with_redirection
Disable PV    : False
Disable BESS  : False
Hard no-slack : False
Sensitivity overrides: none
Run directory : C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty
Loading inputs...
Preprocessing inputs...
Hex cells: 57
Active redirection arc-slots: 57,600
Building type-aware Pyomo model...
Solving with Gurobi...
Read LP format model from file C:\Users\omkarp\AppData\Local\Temp\tmpbmk48k1h.pyomo.lp
Reading time = 4.06 seconds
x1: 1189599 rows, 1340745 columns, 7590291 nonzeros
Set parameter Threads to value 32
Set parameter Presolve to value 2
Set parameter NumericFocus to value 2
Set parameter Heuristics to value 0.1
Set parameter MIPGap to value 0.0001
Set parameter NodefileStart to value 0.5
Set parameter Cuts to value 3
Set parameter TimeLimit to value 21600
Set parameter MIPFocus to value 1
Set parameter LogFile to value "C:/Users/omkarp/Downloads/Opti/runs/2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty/logs/gurobi_run.log"
Set parameter NodefileDir to value "C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\nodefiles"
Gurobi Optimizer version 13.0.1 build v13.0.1rc0 (win64 - Windows 11+.0 (26200.2))

CPU model: Intel(R) Xeon(R) w5-2465X, instruction set [SSE2|AVX|AVX2|AVX512]
Thread count: 16 physical cores, 32 logical processors, using up to 32 threads

Non-default parameters:
TimeLimit  21600
Heuristics  0.1
MIPFocus  1
NodefileStart  0.5
Cuts  3
NumericFocus  2
Presolve  2
Threads  32

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
Presolve removed 117978 rows and 138398 columns (presolve time = 5s)...
Presolve removed 130926 rows and 146330 columns (presolve time = 10s)...
Presolve removed 138991 rows and 153246 columns (presolve time = 15s)...
Presolve removed 210542 rows and 216447 columns (presolve time = 22s)...
Presolve removed 266862 rows and 271905 columns (presolve time = 25s)...
Presolve removed 318501 rows and 325295 columns (presolve time = 31s)...
Presolve removed 420027 rows and 427444 columns (presolve time = 50s)...
Presolve removed 569507 rows and 589566 columns (presolve time = 283s)...
Presolve removed 569507 rows and 589566 columns
Presolve time: 283.01s
Presolved: 620092 rows, 751179 columns, 4258963 nonzeros
Found heuristic solution: objective -3.97883e+11
Variable types: 659256 continuous, 91923 integer (54438 binary)
Root relaxation presolve removed 135511 rows and 207373 columns
Root relaxation presolved: 484581 rows, 543806 columns, 3049852 nonzeros

Deterministic concurrent LP optimizer: primal simplex, dual simplex, and barrier
Showing barrier log only...

Root barrier log...

Ordering time: 3.72s

Barrier statistics:
 Dense cols : 135
 AA' NZ     : 3.455e+06
 Factor NZ  : 1.597e+07 (roughly 500 MB of memory)
 Factor Ops : 1.942e+09 (less than 1 second per iteration)
 Threads    : 30

                  Objective                Residual
Iter       Primal          Dual         Primal    Dual     Compl     Time
   0  -5.41363247e+12  5.07514625e+13  5.50e+04 2.31e+06  3.85e+09   293s
   1   7.98853574e+11  5.64405797e+13  4.48e+04 1.72e+06  2.97e+09   294s
   2   2.16654786e+12  5.85772058e+13  3.27e+04 6.74e+05  2.11e+09   295s
   3   2.10394374e+12  5.74014081e+13  2.90e+04 3.09e+05  1.82e+09   296s
   4   1.95683423e+12  5.36891633e+13  2.12e+04 3.61e+04  1.33e+09   297s
   5   1.36669776e+12  4.77564971e+13  1.26e+04 4.01e-05  7.91e+08   298s
   6   8.43176925e+11  3.55265974e+13  6.19e+03 2.52e-05  3.80e+08   298s
   7   5.76218507e+11  2.54956264e+13  3.69e+03 3.29e-05  2.19e+08   299s
   8   2.83105147e+11  1.63691927e+13  1.54e+03 4.57e-05  8.96e+07   299s
   9   1.01879316e+11  9.44275534e+12  5.29e+02 1.35e-05  3.14e+07   300s
  10   2.32418988e+10  6.47113601e+12  1.71e+02 7.84e-06  1.19e+07   301s
  11  -2.90834795e+09  3.56625896e+12  4.85e+01 2.94e-06  4.22e+06   302s
  12  -6.38364330e+09  1.15595338e+12  1.44e+01 1.93e-06  1.13e+06   302s
  13  -2.62918753e+09  2.60515327e+11  1.68e+00 1.34e-06  1.99e+05   303s
  14  -5.11275528e+08  4.33220736e+10  1.70e-01 4.92e-07  3.07e+04   304s
  15  -7.17123016e+06  8.76663783e+09  1.70e-02 1.13e-07  6.06e+03   304s
  16   5.77126825e+07  2.52351593e+09  1.70e-03 1.44e-08  1.70e+03   306s
  17   6.81692415e+07  1.18043459e+09  4.55e-04 8.21e-09  7.66e+02   307s
  18   7.29276177e+07  6.31280596e+08  2.79e-04 3.74e-09  3.85e+02   308s
  19   8.03196006e+07  4.56837306e+08  1.88e-04 5.59e-09  2.59e+02   309s
  20   8.51575800e+07  3.50958986e+08  1.32e-04 5.59e-09  1.83e+02   311s
  21   8.92124840e+07  3.15613804e+08  1.04e-04 5.59e-09  1.56e+02   312s
  22   9.24685391e+07  2.76011433e+08  8.53e-05 5.59e-09  1.26e+02   313s
  23   9.57514333e+07  2.19488589e+08  7.03e-05 5.59e-09  8.52e+01   314s
  24   1.00363913e+08  1.98947875e+08  5.26e-05 5.59e-09  6.79e+01   316s
  25   1.04731754e+08  1.81680416e+08  3.87e-05 5.59e-09  5.30e+01   318s
  26   1.08491944e+08  1.67341822e+08  2.79e-05 5.59e-09  4.05e+01   320s
  27   1.12016983e+08  1.58925331e+08  2.03e-05 5.59e-09  3.23e+01   321s
  28   1.14833184e+08  1.46872969e+08  1.54e-05 5.59e-09  2.21e+01   323s
  29   1.17856908e+08  1.41956905e+08  1.07e-05 5.59e-09  1.66e+01   325s
  30   1.19580577e+08  1.36244477e+08  8.33e-06 7.45e-09  1.15e+01   326s
  31   1.21068514e+08  1.33411123e+08  6.58e-06 5.59e-09  8.50e+00   328s
  32   1.22673389e+08  1.32127562e+08  4.78e-06 5.59e-09  6.51e+00   330s
  33   1.23852508e+08  1.31162844e+08  3.51e-06 5.59e-09  5.03e+00   331s
  34   1.24627878e+08  1.30010971e+08  2.72e-06 5.59e-09  3.71e+00   333s
  35   1.25447019e+08  1.29458671e+08  1.91e-06 5.59e-09  2.76e+00   334s
  36   1.25946941e+08  1.29141297e+08  1.42e-06 7.45e-09  2.20e+00   336s
  37   1.26311356e+08  1.28724796e+08  1.07e-06 7.45e-09  1.66e+00   338s
  38   1.26577139e+08  1.28543893e+08  8.24e-07 7.45e-09  1.35e+00   340s
  39   1.26744252e+08  1.28287840e+08  6.71e-07 7.45e-09  1.06e+00   343s
  40   1.26881965e+08  1.28083627e+08  5.47e-07 7.45e-09  8.28e-01   345s
  41   1.26991341e+08  1.27927906e+08  4.49e-07 5.59e-09  6.45e-01   347s
  42   1.27056176e+08  1.27869061e+08  3.92e-07 7.45e-09  5.60e-01   349s
  43   1.27155735e+08  1.27824709e+08  3.05e-07 7.45e-09  4.61e-01   352s
  44   1.27234797e+08  1.27775338e+08  2.36e-07 7.45e-09  3.72e-01   354s
  45   1.27246774e+08  1.27740850e+08  2.25e-07 7.45e-09  3.40e-01   355s
  46   1.27268586e+08  1.27732996e+08  2.06e-07 7.45e-09  3.20e-01   357s
  47   1.27304341e+08  1.27689387e+08  1.75e-07 7.45e-09  2.65e-01   359s
  48   1.27346054e+08  1.27659073e+08  1.40e-07 7.45e-09  2.16e-01   361s
  49   1.27376997e+08  1.27626945e+08  1.14e-07 7.45e-09  1.72e-01   364s
  50   1.27400651e+08  1.27612479e+08  9.47e-08 5.59e-09  1.46e-01   365s
  51   1.27420011e+08  1.27593507e+08  7.94e-08 5.59e-09  1.19e-01   367s
  52   1.27436741e+08  1.27580867e+08  6.60e-08 5.59e-09  9.93e-02   368s
  53   1.27447746e+08  1.27574792e+08  5.75e-08 5.59e-09  8.75e-02   369s
  54   1.27458586e+08  1.27566811e+08  4.89e-08 5.59e-09  7.45e-02   371s
  55   1.27469183e+08  1.27557204e+08  4.08e-08 5.59e-09  6.06e-02   372s
  56   1.27476451e+08  1.27552523e+08  3.51e-08 5.59e-09  5.24e-02   373s
  57   1.27488929e+08  1.27546369e+08  2.54e-08 3.73e-09  3.96e-02   375s
  58   1.27500190e+08  1.27538912e+08  1.72e-08 3.73e-09  2.67e-02   376s
  59   1.27502803e+08  1.27536962e+08  1.51e-08 3.73e-09  2.35e-02   377s
  60   1.27504762e+08  1.27535271e+08  1.36e-08 4.66e-09  2.10e-02   379s
  61   1.27507635e+08  1.27532421e+08  1.14e-08 3.73e-09  1.71e-02   380s
  62   1.27510961e+08  1.27529493e+08  8.95e-09 2.79e-09  1.28e-02   382s
  63   1.27513850e+08  1.27528558e+08  6.71e-09 2.79e-09  1.01e-02   383s
  64   1.27515089e+08  1.27526671e+08  6.10e-09 1.86e-09  7.98e-03   385s
  65   1.27517880e+08  1.27526256e+08  5.13e-09 1.92e-09  5.77e-03   386s
  66   1.27518510e+08  1.27524712e+08  4.91e-09 1.76e-09  4.27e-03   388s
  67   1.27519289e+08  1.27524157e+08  4.63e-09 1.87e-09  3.35e-03   390s
  68   1.27520394e+08  1.27523875e+08  4.24e-09 1.81e-09  2.40e-03   392s
  69   1.27521018e+08  1.27523712e+08  4.28e-08 2.10e-09  1.86e-03   395s
  70   1.27521429e+08  1.27523429e+08  7.12e-08 1.63e-09  1.38e-03   399s
  71   1.27521828e+08  1.27523327e+08  5.79e-08 1.79e-09  1.03e-03   402s
  72   1.27522001e+08  1.27523241e+08  1.12e-07 1.91e-09  8.54e-04   408s
  73   1.27522292e+08  1.27523191e+08  4.72e-07 2.21e-09  6.19e-04   413s
  74   1.27522466e+08  1.27523123e+08  3.00e-07 1.83e-09  4.52e-04   417s
  75   1.27522676e+08  1.27523096e+08  9.63e-07 1.71e-09  2.89e-04   422s

Barrier solved model in 75 iterations and 421.55 seconds (214.88 work units)
Optimal objective 1.27522676e+08


Root crossover log...

  304492 DPushes remaining with DInf 0.0000000e+00               422s
   17058 DPushes remaining with DInf 0.0000000e+00               425s
    6182 DPushes remaining with DInf 0.0000000e+00               430s
       0 DPushes remaining with DInf 0.0000000e+00               435s

  387157 PPushes remaining with PInf 1.4985645e+00               435s
  163919 PPushes remaining with PInf 1.6056174e+00               435s
       0 PPushes remaining with PInf 5.8562182e-05               437s

  Push phase complete: Pinf 5.8562182e-05, Dinf 3.6813558e+06    437s


Root simplex log...

Iteration    Objective       Primal Inf.    Dual Inf.      Time
  522227    1.2752293e+08   0.000000e+00   3.681356e+06    437s
  524541    1.2752294e+08   0.000000e+00   0.000000e+00    439s
Crossover time: 17.86 seconds (20.07 work units)
Concurrent spin time: 0.05s

Solved with barrier
  524541    1.2752294e+08   0.000000e+00   1.500000e+01    440s
  524542    1.2752294e+08   0.000000e+00   0.000000e+00    440s

Extra simplex iterations after uncrush: 1

Root relaxation: objective 1.275229e+08, 524542 iterations, 155.47 seconds (123.31 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 1.2752e+08    0  399 -3.979e+11 1.2752e+08   100%     -  452s
H    0     0                    -2.77316e+09 1.2752e+08   105%     -  455s
H    0     0                    -2.49253e+09 1.2752e+08   105%     -  458s
     0     0 1.2748e+08    0  466 -2.493e+09 1.2748e+08   105%     -  481s
     0     0 1.2747e+08    0  476 -2.493e+09 1.2747e+08   105%     -  489s
     0     0 1.2747e+08    0  478 -2.493e+09 1.2747e+08   105%     -  490s
     0     0 1.2747e+08    0  483 -2.493e+09 1.2747e+08   105%     -  491s
     0     0 1.2747e+08    0  482 -2.493e+09 1.2747e+08   105%     -  493s
     0     0 1.2747e+08    0  517 -2.493e+09 1.2747e+08   105%     -  494s
     0     0 1.2746e+08    0  521 -2.493e+09 1.2746e+08   105%     -  496s
     0     0 1.2746e+08    0  519 -2.493e+09 1.2746e+08   105%     -  497s
     0     0 1.2746e+08    0  515 -2.493e+09 1.2746e+08   105%     -  498s
     0     0 1.2746e+08    0  514 -2.493e+09 1.2746e+08   105%     -  499s
     0     0 1.2746e+08    0  511 -2.493e+09 1.2746e+08   105%     -  500s
     0     0 1.2746e+08    0  493 -2.493e+09 1.2746e+08   105%     -  502s
     0     0 1.2746e+08    0  478 -2.493e+09 1.2746e+08   105%     -  503s
     0     0 1.2746e+08    0  483 -2.493e+09 1.2746e+08   105%     -  504s
     0     0 1.2746e+08    0  484 -2.493e+09 1.2746e+08   105%     -  505s
     0     0 1.2746e+08    0  484 -2.493e+09 1.2746e+08   105%     -  506s
     0     0 1.2746e+08    0  485 -2.493e+09 1.2746e+08   105%     -  507s
     0     0 1.2746e+08    0  478 -2.493e+09 1.2746e+08   105%     -  508s
     0     0 1.2746e+08    0  469 -2.493e+09 1.2746e+08   105%     -  509s
     0     0 1.2746e+08    0  475 -2.493e+09 1.2746e+08   105%     -  510s
     0     0 1.2746e+08    0  464 -2.493e+09 1.2746e+08   105%     -  511s
     0     0 1.2745e+08    0  467 -2.493e+09 1.2745e+08   105%     -  512s
     0     0 1.2745e+08    0  467 -2.493e+09 1.2745e+08   105%     -  513s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  514s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  514s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  515s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  516s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  517s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  518s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  519s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  520s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  521s
     0     0 1.2745e+08    0  466 -2.493e+09 1.2745e+08   105%     -  521s
     0     0 1.2745e+08    0  468 -2.493e+09 1.2745e+08   105%     -  522s
     0     0 1.2745e+08    0  468 -2.493e+09 1.2745e+08   105%     -  523s
     0     0 1.2745e+08    0  471 -2.493e+09 1.2745e+08   105%     -  524s
     0     0 1.2745e+08    0  474 -2.493e+09 1.2745e+08   105%     -  525s
     0     0 1.2745e+08    0  474 -2.493e+09 1.2745e+08   105%     -  526s
     0     0 1.2745e+08    0  476 -2.493e+09 1.2745e+08   105%     -  527s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  528s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  529s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  530s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  531s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  532s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  533s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  534s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  535s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  536s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  537s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  538s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  539s
     0     0 1.2745e+08    0  472 -2.493e+09 1.2745e+08   105%     -  540s
     0     0 1.2745e+08    0  473 -2.493e+09 1.2745e+08   105%     -  541s
     0     0 1.2745e+08    0  473 -2.493e+09 1.2745e+08   105%     -  542s
     0     0 1.2745e+08    0  476 -2.493e+09 1.2745e+08   105%     -  543s
     0     0 1.2745e+08    0  477 -2.493e+09 1.2745e+08   105%     -  544s
     0     0 1.2745e+08    0  478 -2.493e+09 1.2745e+08   105%     -  545s
     0     0 1.2745e+08    0  478 -2.493e+09 1.2745e+08   105%     -  546s
     0     0 1.2745e+08    0  478 -2.493e+09 1.2745e+08   105%     -  547s
     0     0 1.2744e+08    0  477 -2.493e+09 1.2744e+08   105%     -  549s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  550s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  551s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  552s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  553s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  554s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  555s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  556s
     0     0 1.2744e+08    0  484 -2.493e+09 1.2744e+08   105%     -  557s
     0     0 1.2744e+08    0  491 -2.493e+09 1.2744e+08   105%     -  557s
     0     0 1.2744e+08    0  491 -2.493e+09 1.2744e+08   105%     -  558s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  560s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  561s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  562s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  563s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  564s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  565s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  565s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  566s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  566s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  567s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  568s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  568s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  569s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  569s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  570s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  571s
     0     0 1.2744e+08    0  492 -2.493e+09 1.2744e+08   105%     -  571s
     0     0 1.2744e+08    0  485 -2.493e+09 1.2744e+08   105%     -  572s
     0     0 1.2744e+08    0  485 -2.493e+09 1.2744e+08   105%     -  573s
     0     0 1.2744e+08    0  484 -2.493e+09 1.2744e+08   105%     -  573s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  574s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  575s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  576s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  577s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  578s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  579s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  580s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  580s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  581s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  581s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  582s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  583s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  583s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  584s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  584s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  585s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  586s
     0     0 1.2743e+08    0  484 -2.493e+09 1.2743e+08   105%     -  586s
     0     0 1.2743e+08    0  483 -2.493e+09 1.2743e+08   105%     -  587s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  587s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  588s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  589s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  590s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  590s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  591s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  591s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  592s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  592s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  593s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  593s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  594s
     0     0 1.2743e+08    0  482 -2.493e+09 1.2743e+08   105%     -  594s
     0     0 1.2741e+08    0  458 -2.493e+09 1.2741e+08   105%     -  595s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  597s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  598s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  598s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  599s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  600s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  600s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  601s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  602s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  602s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  603s
     0     0 1.2741e+08    0  469 -2.493e+09 1.2741e+08   105%     -  603s
     0     0 1.2741e+08    0  471 -2.493e+09 1.2741e+08   105%     -  604s
     0     0 1.2741e+08    0  471 -2.493e+09 1.2741e+08   105%     -  605s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  605s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  606s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  607s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  607s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  608s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  608s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  609s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  610s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  611s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  611s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  613s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  613s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  614s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  614s
     0     0 1.2741e+08    0  472 -2.493e+09 1.2741e+08   105%     -  615s
     0     0 1.2734e+08    0  414 -2.493e+09 1.2734e+08   105%     -  619s
H    0     0                    -2.46053e+09 1.2734e+08   105%     -  622s
H    0     0                    -2.45341e+09 1.2734e+08   105%     -  625s
     0     0 1.2734e+08    0  418 -2.453e+09 1.2734e+08   105%     -  626s
     0     0 1.2734e+08    0  420 -2.453e+09 1.2734e+08   105%     -  627s
     0     0 1.2734e+08    0  422 -2.453e+09 1.2734e+08   105%     -  628s
     0     0 1.2734e+08    0  433 -2.453e+09 1.2734e+08   105%     -  630s
     0     0 1.2734e+08    0  433 -2.453e+09 1.2734e+08   105%     -  631s
     0     0 1.2734e+08    0  433 -2.453e+09 1.2734e+08   105%     -  632s
     0     0 1.2734e+08    0  435 -2.453e+09 1.2734e+08   105%     -  633s
     0     0 1.2734e+08    0  440 -2.453e+09 1.2734e+08   105%     -  634s
     0     0 1.2734e+08    0  440 -2.453e+09 1.2734e+08   105%     -  635s
     0     0 1.2734e+08    0  442 -2.453e+09 1.2734e+08   105%     -  635s
     0     0 1.2734e+08    0  426 -2.453e+09 1.2734e+08   105%     -  636s
     0     0 1.2732e+08    0  456 -2.453e+09 1.2732e+08   105%     -  656s
     0     0 1.2732e+08    0  310 -2.453e+09 1.2732e+08   105%     -  673s
H    0     0                    -1.06811e+09 1.2732e+08   112%     -  695s
H    0     0                    -1.06811e+09 1.2732e+08   112%     -  695s
H    0     0                    -1.06194e+09 1.2732e+08   112%     -  696s
H    0     0                    -5.88208e+08 1.2732e+08   122%     -  697s
H    0     0                    -5.88208e+08 1.2732e+08   122%     -  698s
H    0     0                    -5.88189e+08 1.2732e+08   122%     -  698s
H    0     0                    -5.88189e+08 1.2732e+08   122%     -  698s
H    0     0                    -5.75366e+08 1.2732e+08   122%     -  698s
H    0     0                    -5.75262e+08 1.2732e+08   122%     -  698s
H    0     0                    -5.57450e+08 1.2732e+08   123%     -  778s
H    0     0                    -4.89567e+08 1.2732e+08   126%     -  781s
H    0     0                    -4.89561e+08 1.2732e+08   126%     -  781s
H    0     0                    -4.88085e+08 1.2732e+08   126%     -  782s
H    0     0                    -4.88080e+08 1.2732e+08   126%     -  783s
H    0     0                    9.864930e+07 1.2732e+08  29.1%     -  785s
H    0     0                    9.865473e+07 1.2732e+08  29.1%     -  785s
H    0     0                    1.036924e+08 1.2732e+08  22.8%     -  790s
H    0     0                    1.051737e+08 1.2732e+08  21.1%     -  797s
H    0     0                    1.057928e+08 1.2732e+08  20.3%     -  797s
H    0     0                    1.057929e+08 1.2732e+08  20.3%     -  797s
H    0     0                    1.086226e+08 1.2732e+08  17.2%     -  810s
H    0     0                    1.087280e+08 1.2732e+08  17.1%     -  810s
H    0     0                    1.120582e+08 1.2732e+08  13.6%     -  836s
H    0     0                    1.202834e+08 1.2732e+08  5.85%     -  836s
H    0     0                    1.238941e+08 1.2732e+08  2.77%     -  852s
H    0     0                    1.238952e+08 1.2732e+08  2.77%     -  864s
H    0     2                    1.269721e+08 1.2732e+08  0.28%     -  903s
     0     2 1.2732e+08    0  296 1.2697e+08 1.2732e+08  0.28%     -  903s
H    1     4                    1.269721e+08 1.2732e+08  0.27%   0.0  924s
     3     8 1.2715e+08    2  284 1.2697e+08 1.2723e+08  0.20%   850  927s
     7    14 1.2705e+08    3  314 1.2697e+08 1.2718e+08  0.16%   563  932s
    15    16 1.2702e+08    4  333 1.2697e+08 1.2711e+08  0.11%   607  942s
    29    10 1.2699e+08    5  328 1.2697e+08 1.2708e+08  0.08%   433  949s
    45     6     cutoff    6      1.2697e+08 1.2705e+08  0.06%   384  956s
    55    11 1.2701e+08    7  390 1.2697e+08 1.2702e+08  0.04%   363  963s
    61    14     cutoff    8      1.2697e+08 1.2702e+08  0.04%   397  971s
    72    16 1.2700e+08    9  357 1.2697e+08 1.2702e+08  0.04%   410  980s
H   79    16                    1.269842e+08 1.2700e+08  0.01%   432  980s
    86     8 1.2700e+08   10  357 1.2698e+08 1.2700e+08  0.01%   460  986s
    98    12     cutoff   11      1.2698e+08 1.2700e+08  0.01%   425  997s
H  104    12                    1.269855e+08 1.2700e+08  0.01%   407  997s

Cutting planes:
  Lift-and-project: 120
  Implied bound: 980
  Projected implied bound: 180
  MIR: 1475
  Flow cover: 1345
  Flow path: 505
  RLT: 12
  Relax-and-lift: 27

Explored 106 nodes (602954 simplex iterations) in 998.77 seconds (774.43 work units)
Thread count was 32 (of 32 available processors)

Solution count 10: 1.26986e+08 1.26986e+08 1.26984e+08 ... 1.08623e+08

Optimal solution found (tolerance 1.00e-04)
Best objective 1.269855410695e+08, best bound 1.269967004672e+08, gap 0.0088%

- Status: ok
  Return code: 0
  Message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Termination condition: optimal
  Termination message: Model was solved to optimality (subject to tolerances), and an optimal solution is available.
  Wall time: 999.0710000991821
  Error rc: 0


================  OPTIMAL ANNUAL PROFIT  ================
Total profit : 126,985,541 SEK / yr

==================  BREAKDOWN  =================
Revenue (all chargers)             :   178,857,773
Opex - grid purchases              :    39,795,923
Opex - redirection distance        :       721,241
Opex - redirection price comp.     :             0
Opex - unmet-demand penalty        :             0
Capex - chargers                   :     4,349,806
Capex - PV & batteries             :     7,005,262
----------------------------------------------------------
Slow   chargers:         55 | energy:     931,450.8 | cap ratio: 0.176
Medium chargers:        416 | energy:  19,484,180.0 | cap ratio: 0.243
Fast   chargers:         40 | energy:   8,743,032.9 | cap ratio: 0.499
==========================================================

Writing CSV/XLSX outputs...
Combined XLSX written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\results
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
Figures written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\figures
Run finished successfully. Run directory: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty

Terminal transcript written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_093933_small_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
