========== MONOLITHIC TERMINAL LOG ==========
Run transcript : C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
=============================================

Project root  : C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization
Dataset       : full
Run profile   : monolithic.full
Scenario      : with_redirection
Disable PV    : False
Disable BESS  : False
Hard no-slack : False
Sensitivity overrides: none
Run directory : C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty
Loading inputs...
Preprocessing inputs...
Hex cells: 638
Active redirection arc-slots: 472,800
Building type-aware Pyomo model...
Solving with Gurobi...
Read LP format model from file C:\Users\omkarp\AppData\Local\Temp\tmpxd8e5d3a.pyomo.lp
Reading time = 43.09 seconds
x1: 11483106 rows, 12772030 columns, 67905490 nonzeros
Set parameter Threads to value 10
Set parameter Presolve to value 2
Set parameter NumericFocus to value 2
Set parameter Heuristics to value 0.1
Set parameter MIPGap to value 0.0002
Set parameter NodefileStart to value 0.5
Set parameter Cuts to value 1
Set parameter TimeLimit to value 1728000
Set parameter MIPFocus to value 1
Set parameter Method to value 1
Set parameter NodeMethod to value 1
Set parameter PreSparsify to value 1
Set parameter SoftMemLimit to value 180
Set parameter LogFile to value "C:/Users/omkarp/Downloads/Large-scale-LBBD-Optimization/runs/2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty/logs/gurobi_run.log"
Set parameter NodefileDir to value "C:/Users/omkarp/Downloads/Large-scale-LBBD-Optimization/runs/gurobi_nodefiles"
Gurobi Optimizer version 13.0.1 build v13.0.1rc0 (win64 - Windows 11+.0 (26200.2))

CPU model: Intel(R) Xeon(R) w5-2465X, instruction set [SSE2|AVX|AVX2|AVX512]
Thread count: 16 physical cores, 32 logical processors, using up to 10 threads

Non-default parameters:
TimeLimit  1728000
SoftMemLimit  180
MIPGap  0.0002
Method  1
Heuristics  0.1
MIPFocus  1
NodefileStart  0.5
NodeMethod  1
Cuts  1
NumericFocus  2
Presolve  2
PreSparsify  1
Threads  10

Optimize a model with 11483106 rows, 12772030 columns and 67905490 nonzeros (Max)
Model fingerprint: 0x6f88ea49
Model has 6038902 linear objective coefficients
Variable types: 11455752 continuous, 1316278 integer (840288 binary)
Coefficient statistics:
  Matrix range     [4e-05, 2e+03]
  Objective range  [6e-01, 6e+05]
  Bounds range     [1e+00, 1e+03]
  RHS range        [2e-02, 1e+03]

Found heuristic solution: objective -2.13255e+12
Presolve removed 509404 rows and 1243570 columns (presolve time = 5s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 10s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 15s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 21s)...
Presolve removed 691540 rows and 1243570 columns (presolve time = 25s)...
Presolve removed 691540 rows and 1243570 columns (presolve time = 30s)...
Presolve removed 909988 rows and 1462018 columns (presolve time = 35s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 40s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 45s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 50s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 55s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 60s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 65s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 70s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 76s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 81s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 86s)...
Presolve removed 1642384 rows and 1825618 columns (presolve time = 92s)...
Presolve removed 1642384 rows and 1825618 columns (presolve time = 95s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 100s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 105s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 110s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 115s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 120s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 125s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 130s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 135s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 142s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 145s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 150s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 155s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 160s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 165s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 170s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 175s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 180s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 185s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 191s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 196s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 201s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 207s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 210s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 215s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 223s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 229s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 231s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 235s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 240s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 245s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 250s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 255s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 260s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 265s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 270s)...
Presolve removed 1981111 rows and 2723372 columns (presolve time = 275s)...
Presolve removed 2265883 rows and 3114404 columns (presolve time = 280s)...
Presolve removed 2327431 rows and 3175664 columns (presolve time = 285s)...
Presolve removed 2465851 rows and 3175664 columns (presolve time = 290s)...
Presolve removed 2475883 rows and 3185696 columns (presolve time = 295s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 300s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 305s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 310s)...
Presolve removed 2476483 rows and 3191744 columns (presolve time = 315s)...
Presolve removed 2476483 rows and 3191744 columns (presolve time = 320s)...
Presolve removed 2476483 rows and 3225488 columns (presolve time = 325s)...
Presolve removed 2629675 rows and 3291896 columns (presolve time = 330s)...
Presolve removed 2629675 rows and 3334796 columns (presolve time = 335s)...
Presolve removed 2665651 rows and 3336128 columns (presolve time = 340s)...
Presolve removed 2665651 rows and 3336128 columns (presolve time = 345s)...
Presolve removed 2690611 rows and 3361088 columns (presolve time = 350s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 355s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 360s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 365s)...
Presolve removed 2690827 rows and 3361196 columns (presolve time = 370s)...
Presolve removed 2690827 rows and 3361196 columns (presolve time = 375s)...
Presolve removed 2734144 rows and 3413249 columns (presolve time = 381s)...
Presolve removed 2734144 rows and 3417017 columns (presolve time = 385s)...
Presolve removed 2740732 rows and 3417197 columns (presolve time = 391s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 395s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 400s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 405s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 410s)...
Presolve removed 2742388 rows and 3419033 columns (presolve time = 415s)...
Presolve removed 2742388 rows and 3419033 columns (presolve time = 420s)...
Presolve removed 2756948 rows and 3440957 columns (presolve time = 425s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 431s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 435s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 440s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 445s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 450s)...
Presolve removed 2758712 rows and 3445769 columns (presolve time = 455s)...
Presolve removed 2762614 rows and 3447461 columns (presolve time = 460s)...
Presolve removed 2762614 rows and 3448097 columns (presolve time = 465s)...
Presolve removed 2762614 rows and 3448097 columns (presolve time = 470s)...
Presolve removed 3081668 rows and 3662358 columns (presolve time = 475s)...
Presolve removed 3289777 rows and 3811369 columns (presolve time = 480s)...
Presolve removed 3404080 rows and 3898462 columns (presolve time = 485s)...
Presolve removed 3583141 rows and 4045948 columns (presolve time = 491s)...
Presolve removed 3712178 rows and 4152374 columns (presolve time = 496s)...
Presolve removed 3800362 rows and 4234285 columns (presolve time = 501s)...
Presolve removed 3873534 rows and 4295674 columns (presolve time = 506s)...
Presolve removed 3904124 rows and 4323116 columns (presolve time = 510s)...
Presolve removed 3982911 rows and 4395348 columns (presolve time = 515s)...
Presolve removed 4110636 rows and 4514685 columns (presolve time = 525s)...
Presolve removed 4166166 rows and 4560514 columns (presolve time = 530s)...
Presolve removed 4227733 rows and 4610426 columns (presolve time = 532s)...
Presolve removed 4293704 rows and 4667466 columns (presolve time = 539s)...
Presolve removed 4351021 rows and 4723190 columns (presolve time = 542s)...
Presolve removed 4407461 rows and 4781058 columns (presolve time = 546s)...
Presolve removed 4478063 rows and 4850142 columns (presolve time = 551s)...
Presolve removed 4558145 rows and 4930568 columns (presolve time = 570s)...
Presolve removed 4650084 rows and 5020152 columns (presolve time = 591s)...
Presolve removed 4818448 rows and 5177287 columns (presolve time = 613s)...
Presolve removed 5089501 rows and 5458139 columns (presolve time = 697s)...
Presolve removed 5533049 rows and 5914648 columns (presolve time = 871s)...
Presolve removed 5533049 rows and 5914648 columns (presolve time = 2184s)...
Presolve removed 5533049 rows and 5914648 columns (presolve time = 2186s)...
Sparsify removed 6885216 nonzeros (19%)
Presolve removed 5533049 rows and 6236152 columns (presolve time = 2190s)...
Presolve removed 5578445 rows and 5675440 columns
Presolve time: 2192.69s
Presolved: 5904661 rows, 7096590 columns, 29765033 nonzeros
Found heuristic solution: objective -1.56736e+12
Variable types: 6345732 continuous, 750858 integer (558328 binary)
Root relaxation presolve removed 1692072 rows and 2760000 columns (presolve time = 5s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 10s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 15s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 20s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 25s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 30s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 35s)...
Root relaxation presolve removed 1759504 rows and 2809072 columns (presolve time = 40s)...
Root relaxation presolve removed 1966288 rows and 2809072 columns (presolve time = 45s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 50s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 55s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 60s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 65s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 70s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 75s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 80s)...
Root relaxation presolve removed 2094616 rows and 3327775 columns (presolve time = 85s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 90s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 95s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 100s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 105s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 110s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 115s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 120s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 125s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns (presolve time = 130s)...
Root relaxation presolve removed 2099467 rows and 3338572 columns
Root relaxation presolved: 3805194 rows, 3758018 columns, 15740672 nonzeros


Root simplex log...

Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    8.8787877e+09   3.282367e+07   0.000000e+00   2353s
     303    8.8434174e+09   3.228789e+07   0.000000e+00   2355s
    1010    8.7745903e+09   3.212254e+07   0.000000e+00   2361s
    1616    8.7080947e+09   3.207028e+07   0.000000e+00   2365s
    2323    8.6552591e+09   3.206662e+07   0.000000e+00   2371s
    2929    8.6073688e+09   3.203199e+07   0.000000e+00   2375s
    3535    8.5543576e+09   3.204631e+07   0.000000e+00   2380s
    4242    8.4796110e+09   3.200742e+07   0.000000e+00   2386s
    4747    8.4172377e+09   3.191986e+07   0.000000e+00   2390s
    5454    8.3751465e+09   3.191426e+07   0.000000e+00   2395s
    6161    8.3446176e+09   3.196005e+07   0.000000e+00   2401s
    6767    8.2780863e+09   3.186997e+07   0.000000e+00   2405s
    7373    8.1949760e+09   3.180059e+07   0.000000e+00   2410s
    7979    8.1478998e+09   3.180622e+07   0.000000e+00   2415s
    8585    8.0748135e+09   3.168315e+07   0.000000e+00   2420s
    9191    8.0137311e+09   3.163735e+07   0.000000e+00   2425s
    9797    7.9691246e+09   3.167618e+07   0.000000e+00   2430s
   10403    7.9350282e+09   3.165760e+07   0.000000e+00   2435s
   11110    7.8924031e+09   3.160107e+07   0.000000e+00   2440s
   11615    7.8567279e+09   3.158188e+07   0.000000e+00   2445s
   12120    7.8209216e+09   3.148159e+07   0.000000e+00   2450s
   12625    7.7645713e+09   3.135154e+07   0.000000e+00   2455s
   13130    7.7176255e+09   3.133397e+07   0.000000e+00   2460s
   13635    7.6713605e+09   3.121397e+07   0.000000e+00   2466s
   14140    7.6256922e+09   3.109488e+07   0.000000e+00   2470s
   14645    7.5867106e+09   3.103875e+07   0.000000e+00   2476s
   15049    7.5477903e+09   3.097694e+07   0.000000e+00   2480s
   15554    7.5112815e+09   3.094422e+07   0.000000e+00   2486s
   16059    7.4668869e+09   3.084751e+07   0.000000e+00   2491s
   16463    7.4378352e+09   3.081506e+07   0.000000e+00   2495s
   16968    7.4125339e+09   3.089532e+07   0.000000e+00   2500s
   17473    7.3976398e+09   3.089103e+07   0.000000e+00   2505s
   17978    7.3835877e+09   3.087826e+07   0.000000e+00   2510s
   18483    7.3679835e+09   3.094076e+07   0.000000e+00   2515s
   18988    7.3541517e+09   3.089770e+07   0.000000e+00   2520s
   19594    7.3326637e+09   3.094231e+07   0.000000e+00   2526s
   20099    7.3182967e+09   3.096930e+07   0.000000e+00   2531s
   20604    7.3013430e+09   3.097898e+07   0.000000e+00   2536s
   21109    7.2844898e+09   3.103115e+07   0.000000e+00   2540s
   21715    7.2657131e+09   3.102086e+07   0.000000e+00   2546s
   22220    7.2506715e+09   3.098565e+07   0.000000e+00   2551s
   22725    7.2338494e+09   3.099118e+07   0.000000e+00   2555s
   23331    7.2155208e+09   3.101256e+07   0.000000e+00   2561s
   23836    7.2000989e+09   3.104676e+07   0.000000e+00   2566s
   24341    7.1861023e+09   3.101738e+07   0.000000e+00   2570s
   24846    7.1715315e+09   3.104926e+07   0.000000e+00   2575s
   25452    7.1463556e+09   3.103526e+07   0.000000e+00   2581s
   25957    7.1234188e+09   3.105738e+07   0.000000e+00   2586s
   26361    7.1085395e+09   3.104151e+07   0.000000e+00   2591s
   26866    7.0769927e+09   3.105384e+07   0.000000e+00   2596s
   27371    7.0502241e+09   3.098424e+07   0.000000e+00   2601s
   27775    7.0338893e+09   3.099598e+07   0.000000e+00   2605s
   28280    7.0087836e+09   3.093660e+07   0.000000e+00   2610s
   28785    6.9874567e+09   3.092546e+07   0.000000e+00   2615s
   29290    6.9681164e+09   3.082565e+07   0.000000e+00   2620s
   29795    6.9478085e+09   3.080107e+07   0.000000e+00   2625s
   30300    6.9141140e+09   3.074950e+07   0.000000e+00   2631s
   30805    6.8930842e+09   3.076990e+07   0.000000e+00   2636s
   31310    6.8733875e+09   3.069560e+07   0.000000e+00   2641s
   31815    6.8423856e+09   3.070782e+07   0.000000e+00   2646s
   32320    6.8190672e+09   3.072249e+07   0.000000e+00   2651s
   32825    6.7954605e+09   3.069272e+07   0.000000e+00   2656s
   33330    6.7778738e+09   3.069513e+07   0.000000e+00   2661s
   33835    6.7571309e+09   3.071624e+07   0.000000e+00   2666s
   34239    6.7433074e+09   3.069431e+07   0.000000e+00   2670s
   34744    6.7159321e+09   3.063422e+07   0.000000e+00   2676s
   35249    6.6942909e+09   3.058343e+07   0.000000e+00   2681s
   35653    6.6717204e+09   3.050207e+07   0.000000e+00   2685s
   36158    6.6461566e+09   3.043469e+07   0.000000e+00   2690s
   36663    6.6225052e+09   3.043238e+07   0.000000e+00   2696s
   37067    6.6012889e+09   3.036399e+07   0.000000e+00   2700s
   37673    6.5806302e+09   3.034737e+07   0.000000e+00   2706s
   38178    6.5682829e+09   3.043666e+07   0.000000e+00   2710s
   38784    6.5535534e+09   3.043444e+07   0.000000e+00   2715s
   39390    6.5384348e+09   3.048090e+07   0.000000e+00   2721s
   39895    6.5275090e+09   3.049720e+07   0.000000e+00   2726s
   40299    6.5159911e+09   3.054540e+07   0.000000e+00   2730s
   40905    6.5012282e+09   3.054356e+07   0.000000e+00   2736s
   41410    6.4885460e+09   3.058057e+07   0.000000e+00   2740s
   42016    6.4718316e+09   3.057805e+07   0.000000e+00   2746s
   42521    6.4581608e+09   3.059457e+07   0.000000e+00   2750s
   43127    6.4439451e+09   3.066458e+07   0.000000e+00   2755s
   43733    6.4294958e+09   3.067415e+07   0.000000e+00   2761s
   44238    6.4167700e+09   3.073828e+07   0.000000e+00   2765s
   44844    6.4041716e+09   3.076604e+07   0.000000e+00   2770s
   45450    6.3896465e+09   3.080245e+07   0.000000e+00   2775s
   46056    6.3752477e+09   3.081196e+07   0.000000e+00   2781s
   46662    6.3616100e+09   3.084782e+07   0.000000e+00   2785s
   47268    6.3480265e+09   3.087728e+07   0.000000e+00   2790s
   47874    6.3334695e+09   3.084172e+07   0.000000e+00   2796s
   48379    6.3212969e+09   3.086901e+07   0.000000e+00   2800s
   49086    6.3060474e+09   3.092757e+07   0.000000e+00   2806s
   49692    6.2901637e+09   3.095272e+07   0.000000e+00   2811s
   50298    6.2776013e+09   3.101758e+07   0.000000e+00   2816s
   50904    6.2652105e+09   3.099940e+07   0.000000e+00   2821s
   51510    6.2541047e+09   3.103763e+07   0.000000e+00   2826s
   52116    6.2408511e+09   3.106591e+07   0.000000e+00   2830s
   52722    6.2254725e+09   3.107077e+07   0.000000e+00   2835s
   53227    6.1996962e+09   3.101498e+07   0.000000e+00   2840s
   53732    6.1721076e+09   3.095736e+07   0.000000e+00   2845s
   54237    6.1495925e+09   3.087116e+07   0.000000e+00   2850s
   54742    6.1286110e+09   3.084658e+07   0.000000e+00   2855s
   55247    6.1098580e+09   3.082205e+07   0.000000e+00   2860s
   55752    6.0876710e+09   3.073956e+07   0.000000e+00   2865s
   56358    6.0709180e+09   3.069837e+07   0.000000e+00   2871s
   56863    6.0536182e+09   3.065471e+07   0.000000e+00   2875s
   57368    6.0272521e+09   3.057316e+07   0.000000e+00   2880s
   57974    6.0010591e+09   3.048057e+07   0.000000e+00   2886s
   58479    5.9825214e+09   3.039956e+07   0.000000e+00   2891s
   58984    5.9632678e+09   3.036629e+07   0.000000e+00   2895s
   59489    5.9420874e+09   3.027962e+07   0.000000e+00   2900s
   59994    5.9212677e+09   3.017646e+07   0.000000e+00   2905s
   60499    5.9012761e+09   3.010211e+07   0.000000e+00   2910s
   61105    5.8778366e+09   3.002940e+07   0.000000e+00   2916s
   61509    5.8570673e+09   2.995980e+07   0.000000e+00   2920s
   62014    5.8316928e+09   2.988349e+07   0.000000e+00   2926s
   62519    5.8073542e+09   2.981043e+07   0.000000e+00   2931s
   62923    5.7804488e+09   2.973793e+07   0.000000e+00   2935s
   63428    5.7621843e+09   2.969790e+07   0.000000e+00   2940s
   63933    5.7415519e+09   2.966866e+07   0.000000e+00   2945s
   64539    5.7202649e+09   2.959892e+07   0.000000e+00   2951s
   65044    5.7037491e+09   2.953547e+07   0.000000e+00   2956s
   65448    5.6854984e+09   2.949620e+07   0.000000e+00   2960s
   65953    5.6687387e+09   2.949325e+07   0.000000e+00   2965s
   66458    5.6445677e+09   2.943157e+07   0.000000e+00   2971s
   66862    5.6267183e+09   2.938685e+07   0.000000e+00   2975s
   67468    5.6054452e+09   2.932197e+07   0.000000e+00   2981s
   67872    5.5863793e+09   2.930770e+07   0.000000e+00   2985s
   68478    5.5738550e+09   2.922852e+07   0.000000e+00   2990s
   69084    5.5496851e+09   2.913370e+07   0.000000e+00   2996s
   69589    5.5323794e+09   2.906510e+07   0.000000e+00   3000s
   70195    5.5048322e+09   2.899863e+07   0.000000e+00   3006s
   70700    5.4903491e+09   2.896006e+07   0.000000e+00   3011s
   71205    5.4770102e+09   2.893398e+07   0.000000e+00   3016s
   71609    5.4575139e+09   2.888070e+07   0.000000e+00   3020s
   72114    5.4371953e+09   2.884387e+07   0.000000e+00   3025s
   72619    5.4144654e+09   2.876666e+07   0.000000e+00   3030s
   73124    5.3937781e+09   2.871627e+07   0.000000e+00   3035s
   73629    5.3654107e+09   2.864054e+07   0.000000e+00   3041s
   74134    5.3446987e+09   2.859718e+07   0.000000e+00   3045s
   74639    5.3226791e+09   2.853163e+07   0.000000e+00   3051s
   75144    5.3102127e+09   2.852821e+07   0.000000e+00   3055s
   75649    5.2950660e+09   2.848884e+07   0.000000e+00   3060s
   76154    5.2775462e+09   2.845713e+07   0.000000e+00   3065s
   76760    5.2579748e+09   2.838123e+07   0.000000e+00   3071s
   77265    5.2462312e+09   2.835835e+07   0.000000e+00   3075s
   77770    5.2314025e+09   2.830945e+07   0.000000e+00   3080s
   78376    5.2179118e+09   2.830840e+07   0.000000e+00   3086s
   78780    5.2104056e+09   2.830390e+07   0.000000e+00   3090s
   79285    5.1924006e+09   2.827380e+07   0.000000e+00   3095s
   79790    5.1781156e+09   2.821426e+07   0.000000e+00   3101s
   80295    5.1592815e+09   2.814221e+07   0.000000e+00   3106s
   80800    5.1434306e+09   2.809864e+07   0.000000e+00   3111s
   81305    5.1312385e+09   2.807081e+07   0.000000e+00   3115s
   81810    5.1188295e+09   2.803415e+07   0.000000e+00   3120s
   82315    5.1094877e+09   2.800358e+07   0.000000e+00   3125s
   82820    5.0959232e+09   2.796107e+07   0.000000e+00   3130s
   83325    5.0826126e+09   2.786739e+07   0.000000e+00   3135s
   83830    5.0691697e+09   2.783786e+07   0.000000e+00   3140s
   84335    5.0557551e+09   2.778296e+07   0.000000e+00   3145s
   84840    5.0407186e+09   2.774460e+07   0.000000e+00   3151s
   85345    5.0214512e+09   2.768125e+07   0.000000e+00   3156s
   85749    5.0093621e+09   2.768361e+07   0.000000e+00   3160s
   86254    4.9974350e+09   2.762817e+07   0.000000e+00   3165s
   86860    4.9828848e+09   2.760418e+07   0.000000e+00   3171s
   87264    4.9719190e+09   2.759137e+07   0.000000e+00   3175s
   87769    4.9567207e+09   2.750292e+07   0.000000e+00   3181s
   88274    4.9383723e+09   2.744141e+07   0.000000e+00   3186s
   88779    4.9224449e+09   2.736007e+07   0.000000e+00   3190s
   89284    4.9092124e+09   2.731432e+07   0.000000e+00   3196s
   89789    4.8961325e+09   2.727935e+07   0.000000e+00   3200s
   90294    4.8820368e+09   2.716175e+07   0.000000e+00   3206s
   90799    4.8670727e+09   2.713500e+07   0.000000e+00   3211s
   91203    4.8591974e+09   2.709489e+07   0.000000e+00   3215s
   91708    4.8478947e+09   2.707289e+07   0.000000e+00   3221s
   92213    4.8358301e+09   2.701301e+07   0.000000e+00   3225s
   92718    4.8222642e+09   2.696926e+07   0.000000e+00   3231s
   93223    4.8084922e+09   2.692891e+07   0.000000e+00   3235s
   93728    4.7975179e+09   2.692401e+07   0.000000e+00   3240s
   94233    4.7765946e+09   2.688620e+07   0.000000e+00   3245s
   94839    4.7465918e+09   2.681351e+07   0.000000e+00   3251s
   95243    4.7319281e+09   2.674564e+07   0.000000e+00   3255s
   95748    4.7199782e+09   2.668436e+07   0.000000e+00   3261s
   96253    4.7123887e+09   2.658663e+07   0.000000e+00   3266s
   96657    4.7020256e+09   2.667668e+07   0.000000e+00   3271s
   97162    4.6917678e+09   2.646925e+07   0.000000e+00   3275s
   97667    4.6736993e+09   2.641942e+07   0.000000e+00   3280s
   98172    4.6582698e+09   2.636609e+07   0.000000e+00   3286s
   98576    4.6469494e+09   2.632351e+07   0.000000e+00   3290s
   99081    4.6260929e+09   2.630224e+07   0.000000e+00   3295s
   99586    4.6156638e+09   2.626098e+07   0.000000e+00   3300s
  100091    4.6042983e+09   2.613852e+07   0.000000e+00   3306s
  100596    4.5937249e+09   2.609639e+07   0.000000e+00   3310s
  101101    4.5849371e+09   2.601611e+07   0.000000e+00   3316s
  101606    4.5719467e+09   2.598402e+07   0.000000e+00   3321s
  102010    4.5606129e+09   2.593249e+07   0.000000e+00   3326s
  102515    4.5542186e+09   2.597140e+07   0.000000e+00   3331s
  103020    4.5376059e+09   2.590638e+07   0.000000e+00   3336s
  103525    4.5270957e+09   2.590181e+07   0.000000e+00   3341s
  103929    4.5166145e+09   2.585932e+07   0.000000e+00   3345s
  104434    4.5028036e+09   2.584392e+07   0.000000e+00   3350s
  104939    4.4901139e+09   2.579462e+07   0.000000e+00   3356s
  105444    4.4789506e+09   2.578507e+07   0.000000e+00   3360s
  105949    4.4664276e+09   2.573776e+07   0.000000e+00   3366s
  106454    4.4515170e+09   2.568988e+07   0.000000e+00   3371s
  106858    4.4373079e+09   2.563029e+07   0.000000e+00   3376s
  107262    4.4241772e+09   2.559588e+07   0.000000e+00   3380s
  107767    4.4060899e+09   2.555448e+07   0.000000e+00   3386s
  108171    4.4027202e+09   2.557176e+07   0.000000e+00   3390s
  108676    4.3849134e+09   2.553467e+07   0.000000e+00   3396s
  109181    4.3724745e+09   2.547520e+07   0.000000e+00   3401s
  109585    4.3590006e+09   2.543514e+07   0.000000e+00   3405s
  110090    4.3514942e+09   2.542689e+07   0.000000e+00   3410s
  110494    4.3428767e+09   2.537301e+07   0.000000e+00   3415s
  110898    4.3359376e+09   2.533417e+07   0.000000e+00   3420s
  111403    4.3244344e+09   2.528498e+07   0.000000e+00   3426s
  111908    4.3154672e+09   2.527587e+07   0.000000e+00   3430s
  112514    4.3032019e+09   2.521122e+07   0.000000e+00   3436s
  112918    4.2941013e+09   2.522982e+07   0.000000e+00   3441s
  113423    4.2797209e+09   2.517479e+07   0.000000e+00   3446s
  113827    4.2663533e+09   2.510983e+07   0.000000e+00   3451s
  114231    4.2537590e+09   2.503156e+07   0.000000e+00   3456s
  114635    4.2387904e+09   2.497919e+07   0.000000e+00   3460s
  115140    4.2240299e+09   2.495713e+07   0.000000e+00   3466s
  115544    4.2172194e+09   2.502282e+07   0.000000e+00   3470s
  116049    4.2012380e+09   2.498242e+07   0.000000e+00   3476s
  116554    4.1868810e+09   2.491216e+07   0.000000e+00   3481s
  116958    4.1780578e+09   2.496682e+07   0.000000e+00   3485s
  117463    4.1691205e+09   2.492918e+07   0.000000e+00   3490s
  117968    4.1573700e+09   2.490120e+07   0.000000e+00   3495s
  118473    4.1494358e+09   2.487857e+07   0.000000e+00   3501s
  118877    4.1426499e+09   2.488072e+07   0.000000e+00   3505s
  119382    4.1347494e+09   2.487489e+07   0.000000e+00   3511s
  119887    4.1211294e+09   2.475735e+07   0.000000e+00   3516s
  120392    4.1003971e+09   2.469605e+07   0.000000e+00   3521s
  120796    4.0899363e+09   2.465853e+07   0.000000e+00   3525s
  121301    4.0815969e+09   2.456618e+07   0.000000e+00   3531s
  121705    4.0687320e+09   2.450535e+07   0.000000e+00   3536s
  122109    4.0598841e+09   2.446171e+07   0.000000e+00   3540s
  122614    4.0541362e+09   2.441810e+07   0.000000e+00   3545s
  123119    4.0409866e+09   2.440905e+07   0.000000e+00   3551s
  123624    4.0237223e+09   2.435718e+07   0.000000e+00   3556s
  124028    4.0151644e+09   2.422079e+07   0.000000e+00   3560s
  124533    4.0067838e+09   2.418195e+07   0.000000e+00   3566s
  124937    4.0002116e+09   2.421104e+07   0.000000e+00   3571s
  125341    3.9880002e+09   2.414447e+07   0.000000e+00   3576s
  125745    3.9808134e+09   2.412222e+07   0.000000e+00   3580s
  126250    3.9677238e+09   2.406160e+07   0.000000e+00   3585s
  126755    3.9553116e+09   2.399578e+07   0.000000e+00   3591s
  127159    3.9480647e+09   2.394388e+07   0.000000e+00   3595s
  127664    3.9423795e+09   2.393716e+07   0.000000e+00   3601s
  128068    3.9353629e+09   2.391345e+07   0.000000e+00   3605s
  128573    3.9283829e+09   2.383974e+07   0.000000e+00   3611s
  128977    3.9195798e+09   2.378768e+07   0.000000e+00   3616s
  129381    3.9098033e+09   2.378781e+07   0.000000e+00   3620s
  129886    3.8938912e+09   2.369326e+07   0.000000e+00   3626s
  130391    3.8856401e+09   2.365254e+07   0.000000e+00   3631s
  130694    3.8781587e+09   2.365978e+07   0.000000e+00   3636s
  131098    3.8695392e+09   2.364808e+07   0.000000e+00   3641s
  131502    3.8632957e+09   2.369942e+07   0.000000e+00   3646s
  131906    3.8537605e+09   2.365995e+07   0.000000e+00   3651s
  132310    3.8472233e+09   2.362334e+07   0.000000e+00   3656s
  132714    3.8393473e+09   2.357665e+07   0.000000e+00   3661s
  133217    3.8328594e+09   2.353952e+07   0.000000e+00   3665s
  134025    3.8181783e+09   2.338049e+07   0.000000e+00   3670s
  134833    3.8049254e+09   2.327993e+07   0.000000e+00   3675s
  135439    3.7935522e+09   2.324527e+07   0.000000e+00   3680s
  136146    3.7855323e+09   2.321196e+07   0.000000e+00   3685s
  136853    3.7725770e+09   2.318689e+07   0.000000e+00   3690s
  137560    3.7647661e+09   2.313515e+07   0.000000e+00   3696s
  138166    3.7542069e+09   2.310374e+07   0.000000e+00   3701s
  138772    3.7432551e+09   2.305565e+07   0.000000e+00   3705s
  139580    3.7267988e+09   2.297172e+07   0.000000e+00   3710s
  140287    3.7173747e+09   2.295841e+07   0.000000e+00   3715s
  141196    3.7080856e+09   2.287023e+07   0.000000e+00   3720s
  142004    3.6908568e+09   2.281125e+07   0.000000e+00   3725s
  142812    3.6810190e+09   2.277817e+07   0.000000e+00   3730s
  143721    3.6707448e+09   2.275639e+07   0.000000e+00   3735s
  144630    3.6540233e+09   2.270890e+07   0.000000e+00   3740s
  145539    3.6405401e+09   2.264321e+07   0.000000e+00   3745s
  146347    3.6313813e+09   2.257700e+07   0.000000e+00   3750s
  147256    3.6218454e+09   2.269327e+07   0.000000e+00   3756s
  148064    3.6102245e+09   2.257336e+07   0.000000e+00   3760s
  148973    3.5986720e+09   2.250073e+07   0.000000e+00   3765s
  149781    3.5845972e+09   2.236410e+07   0.000000e+00   3770s
  150690    3.5683523e+09   2.229856e+07   0.000000e+00   3776s
  151498    3.5606123e+09   2.230598e+07   0.000000e+00   3780s
  152407    3.5493157e+09   2.234091e+07   0.000000e+00   3785s
  153215    3.5352552e+09   2.227423e+07   0.000000e+00   3790s
  154124    3.5199400e+09   2.220021e+07   0.000000e+00   3795s
  155033    3.5101235e+09   2.202996e+07   0.000000e+00   3800s
  155841    3.5025122e+09   2.189649e+07   0.000000e+00   3805s
  156750    3.4844874e+09   2.179462e+07   0.000000e+00   3810s
  157659    3.4686575e+09   2.180664e+07   0.000000e+00   3815s
  158568    3.4578097e+09   2.167863e+07   0.000000e+00   3820s
  159477    3.4466084e+09   2.165178e+07   0.000000e+00   3825s
  160386    3.4326880e+09   2.144226e+07   0.000000e+00   3831s
  161295    3.4218443e+09   2.135018e+07   0.000000e+00   3835s
  162103    3.4120045e+09   2.127094e+07   0.000000e+00   3840s
  163012    3.3959487e+09   2.113000e+07   0.000000e+00   3845s
  163921    3.3825155e+09   2.107475e+07   0.000000e+00   3851s
  164729    3.3738155e+09   2.105811e+07   0.000000e+00   3855s
  165537    3.3595124e+09   2.093120e+07   0.000000e+00   3860s
  166446    3.3442420e+09   2.084741e+07   0.000000e+00   3865s
  167355    3.3255023e+09   2.081295e+07   0.000000e+00   3870s
  168264    3.3109710e+09   2.077464e+07   0.000000e+00   3875s
  169173    3.2976441e+09   2.071939e+07   0.000000e+00   3881s
  169981    3.2898270e+09   2.059758e+07   0.000000e+00   3885s
  170890    3.2700672e+09   2.050620e+07   0.000000e+00   3890s
  171698    3.2507023e+09   2.041045e+07   0.000000e+00   3895s
  172607    3.2390917e+09   2.027149e+07   0.000000e+00   3900s
  173516    3.2197122e+09   2.018901e+07   0.000000e+00   3905s
  174526    3.2006790e+09   2.016513e+07   0.000000e+00   3911s
  175334    3.1893326e+09   2.038799e+07   0.000000e+00   3915s
  176243    3.1727144e+09   2.036178e+07   0.000000e+00   3920s
  177152    3.1664227e+09   2.049492e+07   0.000000e+00   3926s
  177960    3.1477221e+09   2.039927e+07   0.000000e+00   3930s
  178869    3.1278117e+09   2.016587e+07   0.000000e+00   3935s
  179778    3.1161860e+09   2.011408e+07   0.000000e+00   3940s
  180687    3.0979715e+09   2.000745e+07   0.000000e+00   3945s
  181596    3.0777616e+09   1.986106e+07   0.000000e+00   3951s
  182404    3.0632082e+09   1.980572e+07   0.000000e+00   3955s
  183313    3.0446806e+09   1.970141e+07   0.000000e+00   3960s
  184222    3.0278454e+09   1.965915e+07   0.000000e+00   3965s
  185131    3.0078494e+09   1.954158e+07   0.000000e+00   3971s
  186040    2.9881223e+09   1.947324e+07   0.000000e+00   3976s
  186848    2.9749328e+09   1.935374e+07   0.000000e+00   3980s
  187656    2.9609634e+09   1.926267e+07   0.000000e+00   3985s
  188565    2.9404748e+09   1.918585e+07   0.000000e+00   3990s
  189373    2.9273254e+09   1.913488e+07   0.000000e+00   3995s
  190181    2.9105552e+09   1.905855e+07   0.000000e+00   4000s
  191090    2.8885843e+09   1.896317e+07   0.000000e+00   4005s
  191999    2.8731442e+09   1.889873e+07   0.000000e+00   4010s
  192807    2.8594995e+09   1.868330e+07   0.000000e+00   4015s
  193716    2.8453449e+09   1.901022e+07   0.000000e+00   4021s
  194625    2.8320971e+09   1.871398e+07   0.000000e+00   4026s
  195433    2.8160104e+09   1.865862e+07   0.000000e+00   4030s
  196241    2.8023695e+09   1.859008e+07   0.000000e+00   4035s
  197150    2.7835005e+09   1.841210e+07   0.000000e+00   4040s
  197958    2.7669716e+09   1.829887e+07   0.000000e+00   4045s
  198867    2.7532936e+09   1.812212e+07   0.000000e+00   4050s
  199675    2.7436262e+09   1.799107e+07   0.000000e+00   4055s
  200584    2.7278118e+09   1.780898e+07   0.000000e+00   4060s
  201392    2.7169517e+09   1.772847e+07   0.000000e+00   4065s
  202200    2.7039626e+09   1.765084e+07   0.000000e+00   4070s
  203109    2.6868005e+09   1.754068e+07   0.000000e+00   4075s
  203917    2.6806507e+09   1.735153e+07   0.000000e+00   4080s
  204826    2.6769126e+09   1.655489e+07   0.000000e+00   4085s
  205735    2.6713280e+09   1.622769e+07   0.000000e+00   4090s
  206644    2.6662572e+09   1.601909e+07   0.000000e+00   4095s
  207654    2.6614588e+09   1.579255e+07   0.000000e+00   4100s
  208563    2.6586476e+09   1.554359e+07   0.000000e+00   4105s
  209472    2.6537112e+09   1.533024e+07   0.000000e+00   4110s
  210482    2.6498410e+09   1.512024e+07   0.000000e+00   4116s
  211391    2.6461585e+09   1.495264e+07   0.000000e+00   4120s
  212300    2.6432309e+09   1.473693e+07   0.000000e+00   4125s
  213209    2.6383724e+09   1.449179e+07   0.000000e+00   4130s
  214118    2.6311658e+09   1.438360e+07   0.000000e+00   4135s
  215027    2.6247248e+09   1.424850e+07   0.000000e+00   4140s
  216037    2.6203308e+09   1.390095e+07   0.000000e+00   4146s
  216946    2.6189844e+09   1.384019e+07   0.000000e+00   4150s
  217754    2.6160453e+09   1.365996e+07   0.000000e+00   4155s
  218764    2.6076049e+09   1.354751e+07   0.000000e+00   4160s
  219572    2.5965460e+09   1.339748e+07   0.000000e+00   4165s
  220481    2.5845120e+09   1.329852e+07   0.000000e+00   4170s
  221390    2.5714874e+09   1.322901e+07   0.000000e+00   4176s
  222198    2.5619867e+09   1.315798e+07   0.000000e+00   4180s
  223107    2.5518514e+09   1.305452e+07   0.000000e+00   4185s
  224016    2.5368107e+09   1.296418e+07   0.000000e+00   4191s
  224925    2.5253379e+09   1.295439e+07   0.000000e+00   4196s
  225733    2.5121432e+09   1.290837e+07   0.000000e+00   4200s
  226642    2.4966873e+09   1.287850e+07   0.000000e+00   4205s
  227551    2.4897154e+09   1.271217e+07   0.000000e+00   4211s
  228359    2.4886583e+09   1.263293e+07   0.000000e+00   4215s
  229268    2.4852274e+09   1.256959e+07   0.000000e+00   4220s
  230076    2.4729713e+09   1.247865e+07   0.000000e+00   4225s
  231086    2.4571635e+09   1.237714e+07   0.000000e+00   4231s
  231995    2.4419516e+09   1.232646e+07   0.000000e+00   4236s
  232803    2.4309916e+09   1.225199e+07   0.000000e+00   4240s
  233712    2.4185547e+09   1.221140e+07   0.000000e+00   4246s
  234520    2.4101942e+09   1.220023e+07   0.000000e+00   4250s
  235429    2.3980755e+09   1.220758e+07   0.000000e+00   4255s
  236338    2.3825733e+09   1.214761e+07   0.000000e+00   4260s
  237247    2.3694331e+09   1.211046e+07   0.000000e+00   4265s
  238055    2.3593802e+09   1.212883e+07   0.000000e+00   4270s
  238964    2.3499296e+09   1.201972e+07   0.000000e+00   4275s
  239772    2.3488540e+09   1.194429e+07   0.000000e+00   4280s
  240681    2.3475985e+09   1.184081e+07   0.000000e+00   4285s
  241489    2.3422016e+09   1.182011e+07   0.000000e+00   4290s
  242398    2.3362669e+09   1.179923e+07   0.000000e+00   4295s
  243307    2.3358397e+09   1.178630e+07   0.000000e+00   4300s
  244216    2.3278990e+09   1.179589e+07   0.000000e+00   4305s
  245125    2.3169276e+09   1.181853e+07   0.000000e+00   4310s
  245933    2.3035305e+09   1.175652e+07   0.000000e+00   4316s
  246842    2.2912392e+09   1.170766e+07   0.000000e+00   4321s
  247751    2.2788355e+09   1.169582e+07   0.000000e+00   4326s
  248559    2.2668435e+09   1.170697e+07   0.000000e+00   4330s
  249367    2.2529220e+09   1.170513e+07   0.000000e+00   4335s
  250276    2.2394350e+09   1.160888e+07   0.000000e+00   4340s
  251084    2.2381328e+09   1.143369e+07   0.000000e+00   4345s
  251892    2.2370461e+09   1.135249e+07   0.000000e+00   4350s
  252700    2.2360519e+09   1.133453e+07   0.000000e+00   4355s
  253508    2.2354336e+09   1.131404e+07   0.000000e+00   4360s
  254417    2.2347801e+09   1.144857e+07   0.000000e+00   4365s
  255225    2.2229463e+09   1.143636e+07   0.000000e+00   4370s
  256033    2.2067228e+09   1.143979e+07   0.000000e+00   4375s
  256841    2.1966237e+09   1.144136e+07   0.000000e+00   4380s
  257750    2.1812429e+09   1.153603e+07   0.000000e+00   4385s
  258659    2.1670837e+09   1.154591e+07   0.000000e+00   4390s
  259568    2.1532318e+09   1.154711e+07   0.000000e+00   4395s
  260477    2.1403581e+09   1.149365e+07   0.000000e+00   4401s
  261386    2.1258742e+09   1.141439e+07   0.000000e+00   4406s
  262295    2.1181536e+09   1.094759e+07   0.000000e+00   4410s
  263204    2.1171826e+09   1.068393e+07   0.000000e+00   4416s
  264012    2.1164973e+09   1.061189e+07   0.000000e+00   4420s
  264921    2.1156526e+09   1.066832e+07   0.000000e+00   4425s
  265830    2.1136418e+09   1.084599e+07   0.000000e+00   4430s
  266739    2.1022859e+09   1.100454e+07   0.000000e+00   4435s
  267648    2.0868847e+09   1.078049e+07   0.000000e+00   4441s
  268456    2.0752829e+09   1.069545e+07   0.000000e+00   4445s
  269365    2.0640097e+09   1.066993e+07   0.000000e+00   4450s
  270274    2.0504371e+09   1.064955e+07   0.000000e+00   4455s
  271183    2.0354747e+09   1.059828e+07   0.000000e+00   4460s
  272092    2.0204359e+09   1.057034e+07   0.000000e+00   4465s
  273001    2.0073907e+09   1.055638e+07   0.000000e+00   4471s
  273809    2.0006086e+09   1.012455e+07   0.000000e+00   4475s
  274718    1.9997437e+09   1.000870e+07   0.000000e+00   4480s
  275627    1.9988784e+09   9.991541e+06   0.000000e+00   4485s
  276536    1.9979516e+09   1.033242e+07   0.000000e+00   4490s
  277445    1.9968374e+09   1.029287e+07   0.000000e+00   4495s
  278253    1.9872549e+09   1.025242e+07   0.000000e+00   4501s
  279061    1.9809210e+09   1.021821e+07   0.000000e+00   4505s
  279869    1.9699321e+09   1.021532e+07   0.000000e+00   4510s
  280677    1.9607702e+09   1.022979e+07   0.000000e+00   4515s
  281485    1.9512072e+09   1.023832e+07   0.000000e+00   4520s
  282293    1.9422777e+09   1.013964e+07   0.000000e+00   4525s
  283101    1.9322788e+09   1.010002e+07   0.000000e+00   4530s
  283909    1.9194745e+09   1.012263e+07   0.000000e+00   4535s
  284717    1.9085799e+09   1.009960e+07   0.000000e+00   4540s
  285525    1.9016255e+09   9.640826e+06   0.000000e+00   4545s
  286434    1.9008922e+09   9.395147e+06   0.000000e+00   4550s
  287242    1.9003507e+09   9.387144e+06   0.000000e+00   4555s
  288050    1.8994879e+09   9.549516e+06   0.000000e+00   4560s
  288858    1.8984177e+09   9.411768e+06   0.000000e+00   4565s
  289666    1.8890005e+09   9.351627e+06   0.000000e+00   4570s
  290474    1.8775326e+09   9.383114e+06   0.000000e+00   4575s
  291282    1.8656358e+09   9.356668e+06   0.000000e+00   4580s
  292191    1.8571414e+09   9.358912e+06   0.000000e+00   4585s
  292999    1.8458114e+09   9.331402e+06   0.000000e+00   4590s
  293807    1.8379767e+09   9.323589e+06   0.000000e+00   4596s
  294615    1.8315380e+09   9.550859e+06   0.000000e+00   4600s
  295423    1.8212022e+09   9.597938e+06   0.000000e+00   4605s
  296231    1.8123028e+09   9.571908e+06   0.000000e+00   4611s
  297039    1.8050387e+09   9.138766e+06   0.000000e+00   4615s
  297847    1.8041485e+09   8.925263e+06   0.000000e+00   4620s
  298655    1.8035465e+09   8.964673e+06   0.000000e+00   4625s
  299564    1.8020990e+09   8.943635e+06   0.000000e+00   4630s
  300372    1.8010235e+09   9.052174e+06   0.000000e+00   4635s
  301281    1.7992570e+09   9.048992e+06   0.000000e+00   4641s
  302089    1.7896899e+09   9.066060e+06   0.000000e+00   4645s
  302897    1.7787061e+09   9.024636e+06   0.000000e+00   4650s
  303806    1.7674866e+09   9.026441e+06   0.000000e+00   4655s
  304715    1.7571754e+09   9.032094e+06   0.000000e+00   4660s
  305523    1.7453083e+09   9.005688e+06   0.000000e+00   4665s
  306432    1.7387418e+09   9.128677e+06   0.000000e+00   4671s
  307341    1.7268740e+09   9.031093e+06   0.000000e+00   4676s
  308149    1.7174638e+09   9.012493e+06   0.000000e+00   4680s
  308957    1.7149856e+09   8.708552e+06   0.000000e+00   4686s
  309765    1.7142471e+09   8.717254e+06   0.000000e+00   4690s
  310573    1.7135235e+09   8.705920e+06   0.000000e+00   4695s
  311381    1.7126739e+09   8.722833e+06   0.000000e+00   4700s
  312189    1.7107880e+09   8.697670e+06   0.000000e+00   4705s
  313098    1.7002363e+09   8.680956e+06   0.000000e+00   4710s
  313906    1.6924228e+09   8.682081e+06   0.000000e+00   4716s
  314613    1.6811299e+09   8.709272e+06   0.000000e+00   4720s
  315320    1.6736979e+09   8.720815e+06   0.000000e+00   4725s
  316128    1.6604284e+09   8.718391e+06   0.000000e+00   4731s
  316936    1.6502346e+09   8.684096e+06   0.000000e+00   4735s
  317744    1.6412524e+09   8.674987e+06   0.000000e+00   4740s
  318552    1.6316868e+09   8.684741e+06   0.000000e+00   4745s
  319360    1.6217512e+09   8.680677e+06   0.000000e+00   4750s
  320168    1.6146665e+09   8.145460e+06   0.000000e+00   4755s
  321077    1.6139820e+09   8.113300e+06   0.000000e+00   4760s
  321885    1.6135691e+09   7.936377e+06   0.000000e+00   4765s
  322794    1.6128708e+09   8.075377e+06   0.000000e+00   4770s
  323703    1.6090376e+09   8.152786e+06   0.000000e+00   4776s
  324511    1.6017645e+09   8.163862e+06   0.000000e+00   4780s
  325319    1.5933256e+09   8.133480e+06   0.000000e+00   4785s
  326228    1.5842785e+09   8.077714e+06   0.000000e+00   4790s
  327137    1.5751943e+09   8.049303e+06   0.000000e+00   4796s
  327945    1.5657713e+09   7.953746e+06   0.000000e+00   4800s
  328652    1.5611652e+09   7.999415e+06   0.000000e+00   4805s
  329460    1.5538858e+09   7.970158e+06   0.000000e+00   4810s
  330268    1.5438834e+09   7.921867e+06   0.000000e+00   4815s
  331076    1.5335276e+09   7.915719e+06   0.000000e+00   4820s
  331783    1.5298775e+09   7.632904e+06   0.000000e+00   4825s
  332692    1.5292682e+09   7.532602e+06   0.000000e+00   4830s
  333500    1.5288301e+09   7.576641e+06   0.000000e+00   4835s
  334207    1.5284509e+09   7.578697e+06   0.000000e+00   4840s
  335015    1.5275948e+09   7.550387e+06   0.000000e+00   4845s
  335823    1.5210046e+09   7.530089e+06   0.000000e+00   4851s
  336631    1.5123572e+09   7.533367e+06   0.000000e+00   4855s
  337439    1.5059527e+09   7.519143e+06   0.000000e+00   4860s
  338348    1.4994230e+09   7.497540e+06   0.000000e+00   4865s
  339156    1.4923605e+09   7.491991e+06   0.000000e+00   4870s
  340065    1.4839352e+09   7.491527e+06   0.000000e+00   4876s
  340873    1.4777536e+09   7.523145e+06   0.000000e+00   4880s
  341681    1.4698745e+09   7.525030e+06   0.000000e+00   4885s
  342489    1.4624548e+09   7.508717e+06   0.000000e+00   4890s
  343297    1.4571293e+09   7.276091e+06   0.000000e+00   4895s
  344206    1.4565595e+09   7.021080e+06   0.000000e+00   4901s
  345014    1.4559801e+09   7.037119e+06   0.000000e+00   4905s
  345822    1.4553848e+09   7.078252e+06   0.000000e+00   4910s
  346630    1.4547061e+09   7.129648e+06   0.000000e+00   4915s
  347438    1.4493762e+09   7.198110e+06   0.000000e+00   4920s
  348347    1.4416989e+09   7.172049e+06   0.000000e+00   4926s
  349155    1.4299145e+09   7.096135e+06   0.000000e+00   4930s
  349963    1.4197848e+09   7.072101e+06   0.000000e+00   4935s
  350771    1.4126626e+09   7.021310e+06   0.000000e+00   4940s
  351579    1.4064435e+09   7.027510e+06   0.000000e+00   4945s
  352387    1.4008551e+09   7.013335e+06   0.000000e+00   4950s
  353195    1.3961644e+09   7.045672e+06   0.000000e+00   4955s
  354003    1.3871347e+09   7.010590e+06   0.000000e+00   4960s
  354811    1.3801080e+09   6.959601e+06   0.000000e+00   4965s
  355720    1.3795734e+09   6.724774e+06   0.000000e+00   4970s
  356528    1.3792770e+09   6.740607e+06   0.000000e+00   4975s
  357336    1.3788408e+09   6.705949e+06   0.000000e+00   4980s
  358144    1.3779986e+09   6.740632e+06   0.000000e+00   4985s
  358952    1.3684740e+09   6.725017e+06   0.000000e+00   4990s
  359760    1.3620513e+09   6.833888e+06   0.000000e+00   4995s
  360568    1.3561761e+09   6.728431e+06   0.000000e+00   5000s
  361376    1.3487421e+09   6.719561e+06   0.000000e+00   5005s
  362184    1.3434023e+09   6.717215e+06   0.000000e+00   5010s
  362992    1.3365491e+09   6.698982e+06   0.000000e+00   5015s
  363800    1.3301028e+09   6.663505e+06   0.000000e+00   5020s
  364608    1.3157629e+09   6.649063e+06   0.000000e+00   5025s
  365517    1.3075327e+09   6.661744e+06   0.000000e+00   5030s
  366325    1.3016869e+09   6.669307e+06   0.000000e+00   5035s
  367133    1.3011824e+09   6.347427e+06   0.000000e+00   5040s
  367941    1.3009090e+09   6.404501e+06   0.000000e+00   5045s
  368850    1.3005003e+09   6.305358e+06   0.000000e+00   5051s
  369658    1.3000045e+09   6.377732e+06   0.000000e+00   5055s
  370466    1.2963390e+09   6.322446e+06   0.000000e+00   5061s
  371274    1.2901885e+09   6.294005e+06   0.000000e+00   5065s
  371981    1.2857939e+09   6.293660e+06   0.000000e+00   5070s
  372789    1.2800826e+09   6.285416e+06   0.000000e+00   5076s
  373597    1.2742338e+09   6.260664e+06   0.000000e+00   5080s
  374405    1.2687518e+09   6.261658e+06   0.000000e+00   5086s
  375112    1.2555989e+09   6.241395e+06   0.000000e+00   5090s
  375920    1.2449440e+09   6.220705e+06   0.000000e+00   5095s
  376728    1.2394619e+09   6.200016e+06   0.000000e+00   5100s
  377536    1.2343095e+09   6.188196e+06   0.000000e+00   5105s
  378344    1.2317252e+09   6.025285e+06   0.000000e+00   5110s
  379152    1.2314601e+09   5.912326e+06   0.000000e+00   5115s
  379960    1.2310516e+09   6.009534e+06   0.000000e+00   5121s
  380667    1.2304886e+09   5.991216e+06   0.000000e+00   5125s
  381475    1.2296327e+09   5.976359e+06   0.000000e+00   5130s
  382283    1.2257976e+09   5.980008e+06   0.000000e+00   5135s
  383091    1.2206525e+09   5.935632e+06   0.000000e+00   5140s
  383899    1.2147102e+09   5.925728e+06   0.000000e+00   5145s
  384808    1.2091810e+09   5.967623e+06   0.000000e+00   5151s
  385616    1.2056170e+09   6.014993e+06   0.000000e+00   5155s
  386323    1.2010950e+09   5.939134e+06   0.000000e+00   5160s
  387232    1.1958521e+09   5.943715e+06   0.000000e+00   5166s
  388040    1.1882697e+09   5.922129e+06   0.000000e+00   5171s
  388848    1.1842635e+09   5.890776e+06   0.000000e+00   5175s
  389555    1.1806723e+09   5.892082e+06   0.000000e+00   5180s
  390363    1.1802545e+09   5.606775e+06   0.000000e+00   5185s
  391171    1.1799683e+09   5.564431e+06   0.000000e+00   5190s
  391878    1.1796108e+09   5.604397e+06   0.000000e+00   5195s
  392686    1.1790058e+09   5.674566e+06   0.000000e+00   5200s
  393494    1.1782149e+09   5.741035e+06   0.000000e+00   5205s
  394302    1.1741829e+09   5.767728e+06   0.000000e+00   5211s
  395009    1.1715321e+09   5.687235e+06   0.000000e+00   5215s
  395716    1.1674175e+09   5.667222e+06   0.000000e+00   5220s
  396524    1.1623308e+09   5.640304e+06   0.000000e+00   5225s
  397332    1.1581369e+09   5.648698e+06   0.000000e+00   5230s
  398140    1.1528646e+09   5.650081e+06   0.000000e+00   5236s
  398847    1.1484143e+09   5.606922e+06   0.000000e+00   5240s
  399655    1.1431524e+09   5.625869e+06   0.000000e+00   5245s
  400362    1.1393664e+09   5.627437e+06   0.000000e+00   5250s
  401170    1.1354933e+09   5.616051e+06   0.000000e+00   5255s
  401978    1.1351218e+09   5.346371e+06   0.000000e+00   5260s
  402786    1.1347809e+09   5.365061e+06   0.000000e+00   5265s
  403594    1.1344069e+09   5.429926e+06   0.000000e+00   5271s
  404402    1.1340210e+09   5.436614e+06   0.000000e+00   5276s
  405210    1.1334916e+09   5.494411e+06   0.000000e+00   5281s
  405917    1.1306088e+09   5.518870e+06   0.000000e+00   5285s
  406725    1.1220791e+09   5.508262e+06   0.000000e+00   5290s
  407432    1.1177286e+09   5.485263e+06   0.000000e+00   5295s
  408240    1.1132210e+09   5.489730e+06   0.000000e+00   5300s
  409048    1.1080273e+09   5.470505e+06   0.000000e+00   5306s
  409755    1.1043176e+09   5.461720e+06   0.000000e+00   5311s
  410361    1.1012859e+09   5.411011e+06   0.000000e+00   5315s
  411169    1.0972503e+09   5.404017e+06   0.000000e+00   5321s
  411876    1.0941533e+09   5.421305e+06   0.000000e+00   5326s
  412583    1.0898607e+09   5.396458e+06   0.000000e+00   5330s
  413391    1.0892248e+09   5.015842e+06   0.000000e+00   5335s
  414199    1.0889698e+09   4.956775e+06   0.000000e+00   5340s
  415007    1.0886591e+09   4.995345e+06   0.000000e+00   5345s
  415815    1.0883318e+09   5.160371e+06   0.000000e+00   5350s
  416623    1.0873103e+09   5.167186e+06   0.000000e+00   5355s
  417431    1.0794691e+09   5.150179e+06   0.000000e+00   5360s
  418340    1.0697152e+09   5.159936e+06   0.000000e+00   5366s
  419148    1.0639512e+09   5.116847e+06   0.000000e+00   5370s
  419956    1.0575700e+09   5.111310e+06   0.000000e+00   5376s
  420764    1.0527197e+09   5.090447e+06   0.000000e+00   5381s
  421471    1.0492835e+09   5.072783e+06   0.000000e+00   5385s
  422279    1.0455613e+09   5.054103e+06   0.000000e+00   5390s
  422986    1.0415272e+09   5.061500e+06   0.000000e+00   5395s
  423794    1.0374870e+09   5.036690e+06   0.000000e+00   5400s
  424602    1.0349457e+09   4.740295e+06   0.000000e+00   5405s
  425410    1.0347054e+09   4.706759e+06   0.000000e+00   5410s
  426218    1.0344467e+09   4.757303e+06   0.000000e+00   5415s
  427026    1.0340468e+09   4.783412e+06   0.000000e+00   5421s
  427834    1.0330987e+09   4.757483e+06   0.000000e+00   5426s
  428541    1.0294388e+09   4.753246e+06   0.000000e+00   5430s
  429349    1.0241070e+09   4.866131e+06   0.000000e+00   5435s
  430056    1.0200091e+09   4.853957e+06   0.000000e+00   5440s
  430864    1.0162640e+09   4.836311e+06   0.000000e+00   5446s
  431571    1.0123348e+09   4.833474e+06   0.000000e+00   5450s
  432379    1.0083110e+09   4.829872e+06   0.000000e+00   5455s
  433187    1.0038989e+09   4.758927e+06   0.000000e+00   5460s
  433894    1.0007928e+09   4.732912e+06   0.000000e+00   5465s
  434702    9.9691941e+08   4.727569e+06   0.000000e+00   5470s
  435510    9.9332188e+08   4.739535e+06   0.000000e+00   5475s
  436318    9.9167579e+08   4.552083e+06   0.000000e+00   5480s
  437025    9.9148471e+08   4.377608e+06   0.000000e+00   5485s
  437833    9.9122321e+08   4.446742e+06   0.000000e+00   5490s
  438641    9.9089465e+08   4.507369e+06   0.000000e+00   5496s
  439348    9.9056856e+08   4.450250e+06   0.000000e+00   5500s
  440156    9.8961017e+08   4.475935e+06   0.000000e+00   5506s
  440863    9.8740928e+08   4.486040e+06   0.000000e+00   5510s
  441671    9.8379489e+08   4.472656e+06   0.000000e+00   5516s
  442378    9.7917576e+08   4.472171e+06   0.000000e+00   5521s
  443186    9.7323745e+08   4.453479e+06   0.000000e+00   5526s
  443994    9.6854099e+08   4.442544e+06   0.000000e+00   5531s
  444701    9.6433842e+08   4.422898e+06   0.000000e+00   5535s
  445509    9.6180832e+08   4.424438e+06   0.000000e+00   5540s
  446317    9.5883577e+08   4.413074e+06   0.000000e+00   5546s
  447024    9.5625289e+08   4.465495e+06   0.000000e+00   5550s
  447832    9.5399106e+08   4.296460e+06   0.000000e+00   5555s
  448640    9.5373320e+08   4.306040e+06   0.000000e+00   5560s
  449347    9.5353983e+08   4.280294e+06   0.000000e+00   5565s
  450155    9.5330185e+08   4.283795e+06   0.000000e+00   5570s
  450862    9.5303707e+08   4.340009e+06   0.000000e+00   5575s
  451569    9.5264956e+08   4.360710e+06   0.000000e+00   5580s
  452377    9.5043654e+08   4.361395e+06   0.000000e+00   5586s
  453084    9.4736022e+08   4.426031e+06   0.000000e+00   5590s
  453892    9.4366583e+08   4.403040e+06   0.000000e+00   5595s
  454700    9.4076560e+08   4.408026e+06   0.000000e+00   5601s
  455407    9.3810420e+08   4.446537e+06   0.000000e+00   5605s
  456114    9.3213835e+08   4.475053e+06   0.000000e+00   5610s
  456922    9.2743268e+08   4.513052e+06   0.000000e+00   5615s
  457730    9.2394204e+08   4.460627e+06   0.000000e+00   5620s
  458538    9.2084905e+08   4.422249e+06   0.000000e+00   5625s
  459346    9.1908074e+08   4.101795e+06   0.000000e+00   5631s
  460053    9.1890505e+08   4.024762e+06   0.000000e+00   5635s
  460861    9.1870111e+08   4.083037e+06   0.000000e+00   5641s
  461568    9.1843309e+08   4.122846e+06   0.000000e+00   5645s
  462376    9.1819561e+08   4.158042e+06   0.000000e+00   5651s
  463083    9.1719331e+08   4.176498e+06   0.000000e+00   5655s
  463790    9.1486845e+08   4.173171e+06   0.000000e+00   5660s
  464497    9.1221321e+08   4.204949e+06   0.000000e+00   5666s
  465204    9.0960140e+08   4.308180e+06   0.000000e+00   5670s
  465911    9.0684109e+08   4.180047e+06   0.000000e+00   5676s
  466618    9.0391449e+08   4.176304e+06   0.000000e+00   5680s
  467325    9.0186929e+08   4.198802e+06   0.000000e+00   5685s
  468032    8.9903310e+08   4.124796e+06   0.000000e+00   5690s
  468840    8.9610839e+08   4.120823e+06   0.000000e+00   5695s
  469648    8.9227344e+08   4.079773e+06   0.000000e+00   5701s
  470355    8.8714170e+08   4.070799e+06   0.000000e+00   5705s
  471062    8.8640398e+08   3.861831e+06   0.000000e+00   5710s
  471769    8.8625120e+08   3.804905e+06   0.000000e+00   5715s
  472476    8.8604270e+08   3.845885e+06   0.000000e+00   5720s
  473284    8.8578117e+08   3.846075e+06   0.000000e+00   5726s
  473991    8.8555283e+08   3.864754e+06   0.000000e+00   5731s
  474597    8.8526991e+08   3.845778e+06   0.000000e+00   5735s
  475405    8.7696921e+08   3.859912e+06   0.000000e+00   5741s
  476112    8.7009590e+08   3.885157e+06   0.000000e+00   5745s
  476920    8.6777314e+08   3.912707e+06   0.000000e+00   5750s
  477627    8.6574495e+08   3.920785e+06   0.000000e+00   5755s
  478435    8.6372026e+08   3.919599e+06   0.000000e+00   5760s
  479243    8.6175129e+08   3.903577e+06   0.000000e+00   5766s
  479950    8.5955025e+08   3.880328e+06   0.000000e+00   5770s
  480758    8.5714270e+08   3.987576e+06   0.000000e+00   5775s
  481566    8.5370555e+08   3.973136e+06   0.000000e+00   5781s
  482172    8.5075996e+08   3.957795e+06   0.000000e+00   5785s
  482879    8.5058310e+08   3.935465e+06   0.000000e+00   5790s
  483586    8.5044259e+08   3.821174e+06   0.000000e+00   5795s
  484293    8.5024455e+08   3.814645e+06   0.000000e+00   5800s
  485000    8.4997494e+08   3.857173e+06   0.000000e+00   5805s
  485808    8.4976352e+08   3.878076e+06   0.000000e+00   5810s
  486616    8.4933890e+08   3.882863e+06   0.000000e+00   5816s
  487323    8.4761141e+08   3.924425e+06   0.000000e+00   5821s
  488030    8.4487845e+08   3.906164e+06   0.000000e+00   5825s
  488838    8.4156721e+08   3.954910e+06   0.000000e+00   5831s
  489545    8.3917634e+08   3.950134e+06   0.000000e+00   5835s
  490252    8.3738721e+08   4.036449e+06   0.000000e+00   5840s
  490959    8.3553904e+08   3.955337e+06   0.000000e+00   5846s
  491666    8.3334772e+08   3.919557e+06   0.000000e+00   5850s
  492474    8.3046648e+08   3.910162e+06   0.000000e+00   5856s
  493282    8.2748901e+08   3.915390e+06   0.000000e+00   5861s
  494090    8.2581347e+08   3.595012e+06   0.000000e+00   5866s
  494797    8.2559440e+08   3.613441e+06   0.000000e+00   5870s
  495605    8.2539400e+08   3.628603e+06   0.000000e+00   5876s
  496312    8.2518676e+08   3.596812e+06   0.000000e+00   5881s
  497019    8.2496430e+08   3.608968e+06   0.000000e+00   5886s
  497625    8.2476469e+08   3.602971e+06   0.000000e+00   5890s
  498332    8.2451254e+08   3.588412e+06   0.000000e+00   5895s
  499039    8.2273536e+08   3.623484e+06   0.000000e+00   5901s
  499746    8.1963415e+08   3.600674e+06   0.000000e+00   5905s
  500554    8.1704006e+08   3.589231e+06   0.000000e+00   5910s
  501261    8.1481239e+08   3.585015e+06   0.000000e+00   5915s
  502069    8.1194955e+08   3.638119e+06   0.000000e+00   5920s
  502877    8.1017362e+08   3.630976e+06   0.000000e+00   5926s
  503584    8.0840752e+08   3.627937e+06   0.000000e+00   5931s
  504291    8.0638469e+08   3.645056e+06   0.000000e+00   5936s
  504897    8.0396185e+08   3.634990e+06   0.000000e+00   5940s
  505705    8.0270528e+08   3.377712e+06   0.000000e+00   5946s
  506311    8.0258550e+08   3.328043e+06   0.000000e+00   5950s
  507119    8.0235902e+08   3.334632e+06   0.000000e+00   5956s
  507725    8.0216864e+08   3.333062e+06   0.000000e+00   5960s
  508432    8.0195521e+08   3.466015e+06   0.000000e+00   5965s
  509139    8.0168634e+08   3.463965e+06   0.000000e+00   5970s
  509846    8.0135601e+08   3.496722e+06   0.000000e+00   5976s
  510452    7.9861361e+08   3.495032e+06   0.000000e+00   5980s
  511159    7.9659947e+08   3.499395e+06   0.000000e+00   5985s
  511866    7.9448347e+08   3.501847e+06   0.000000e+00   5990s
  512674    7.9142448e+08   3.509878e+06   0.000000e+00   5995s
  513381    7.8980191e+08   3.489650e+06   0.000000e+00   6000s
  514088    7.8794237e+08   3.485633e+06   0.000000e+00   6005s
  514896    7.8302566e+08   3.476879e+06   0.000000e+00   6010s
  515603    7.8088736e+08   3.487247e+06   0.000000e+00   6015s
  516411    7.7886558e+08   3.468331e+06   0.000000e+00   6021s
  517118    7.7770955e+08   3.268651e+06   0.000000e+00   6026s
  517825    7.7757633e+08   3.171821e+06   0.000000e+00   6030s
  518532    7.7739664e+08   3.201456e+06   0.000000e+00   6035s
  519340    7.7720352e+08   3.214879e+06   0.000000e+00   6041s
  519946    7.7706343e+08   3.209274e+06   0.000000e+00   6045s
  520653    7.7684417e+08   3.219033e+06   0.000000e+00   6051s
  521360    7.7569725e+08   3.262231e+06   0.000000e+00   6055s
  522168    7.7411074e+08   3.250509e+06   0.000000e+00   6060s
  522875    7.7166604e+08   3.265022e+06   0.000000e+00   6065s
  523582    7.6998848e+08   3.260693e+06   0.000000e+00   6070s
  524390    7.6804279e+08   3.270375e+06   0.000000e+00   6075s
  525097    7.6569072e+08   3.296662e+06   0.000000e+00   6080s
  525905    7.6402865e+08   3.309393e+06   0.000000e+00   6085s
  526612    7.6268353e+08   3.342633e+06   0.000000e+00   6090s
  527319    7.6009086e+08   3.344963e+06   0.000000e+00   6096s
  528026    7.5799909e+08   3.351516e+06   0.000000e+00   6101s
  528733    7.5725322e+08   3.173204e+06   0.000000e+00   6105s
  529440    7.5707998e+08   3.257642e+06   0.000000e+00   6110s
  530147    7.5693186e+08   3.239102e+06   0.000000e+00   6115s
  530854    7.5673024e+08   3.276248e+06   0.000000e+00   6120s
  531561    7.5656505e+08   3.237344e+06   0.000000e+00   6126s
  532268    7.5636646e+08   3.257710e+06   0.000000e+00   6130s
  532975    7.5592744e+08   3.312933e+06   0.000000e+00   6136s
  533581    7.5410887e+08   3.316066e+06   0.000000e+00   6140s
  534288    7.5270346e+08   3.361073e+06   0.000000e+00   6145s
  534995    7.5119055e+08   3.358193e+06   0.000000e+00   6151s
  535601    7.5018782e+08   3.377113e+06   0.000000e+00   6155s
  536207    7.4933368e+08   3.374417e+06   0.000000e+00   6160s
  536914    7.4818206e+08   3.403660e+06   0.000000e+00   6165s
  537621    7.4671478e+08   3.413623e+06   0.000000e+00   6171s
  538227    7.4404709e+08   3.445287e+06   0.000000e+00   6176s
  538631    7.4240350e+08   3.453300e+06   0.000000e+00   6180s
  539237    7.4137085e+08   3.464290e+06   0.000000e+00   6186s
  539742    7.4053097e+08   3.510568e+06   0.000000e+00   6190s
  540348    7.4020664e+08   3.080131e+06   0.000000e+00   6195s
  541055    7.4010483e+08   3.077700e+06   0.000000e+00   6201s
  541661    7.3999664e+08   3.008879e+06   0.000000e+00   6206s
  542065    7.3992876e+08   3.073055e+06   0.000000e+00   6210s
  542570    7.3980326e+08   3.139243e+06   0.000000e+00   6215s
  543176    7.3962826e+08   3.166607e+06   0.000000e+00   6221s
  543681    7.3951238e+08   3.112912e+06   0.000000e+00   6225s
  544287    7.3941089e+08   3.178154e+06   0.000000e+00   6230s
  544893    7.3917359e+08   3.198555e+06   0.000000e+00   6235s
  545499    7.3792046e+08   3.215856e+06   0.000000e+00   6240s
  546105    7.3653867e+08   3.218165e+06   0.000000e+00   6245s
  546711    7.3532714e+08   3.205327e+06   0.000000e+00   6251s
  547317    7.3420534e+08   3.273367e+06   0.000000e+00   6256s
  547923    7.3350323e+08   3.315976e+06   0.000000e+00   6261s
  548529    7.3248159e+08   3.329475e+06   0.000000e+00   6266s
  549135    7.3133406e+08   3.322289e+06   0.000000e+00   6271s
  549640    7.3025241e+08   3.335783e+06   0.000000e+00   6275s
  550246    7.2928306e+08   3.378576e+06   0.000000e+00   6281s
  550852    7.2829455e+08   3.379926e+06   0.000000e+00   6286s
  551458    7.2704960e+08   3.340696e+06   0.000000e+00   6291s
  552064    7.2697940e+08   2.984972e+06   0.000000e+00   6296s
  552670    7.2689673e+08   2.941928e+06   0.000000e+00   6301s
  553276    7.2671522e+08   2.965462e+06   0.000000e+00   6305s
  553882    7.2658127e+08   3.014430e+06   0.000000e+00   6310s
  554488    7.2646503e+08   2.967755e+06   0.000000e+00   6316s
  554993    7.2632049e+08   2.987629e+06   0.000000e+00   6320s
  555599    7.2611585e+08   3.080296e+06   0.000000e+00   6325s
  556205    7.2586507e+08   3.164640e+06   0.000000e+00   6331s
  556710    7.2516753e+08   3.260264e+06   0.000000e+00   6335s
  557316    7.2414726e+08   3.209014e+06   0.000000e+00   6341s
  557821    7.2289056e+08   3.186549e+06   0.000000e+00   6345s
  558427    7.2214429e+08   3.212326e+06   0.000000e+00   6350s
  559033    7.2044430e+08   3.201075e+06   0.000000e+00   6356s
  559538    7.1933084e+08   3.184395e+06   0.000000e+00   6360s
  560144    7.1812992e+08   3.180555e+06   0.000000e+00   6365s
  560750    7.1721880e+08   3.179597e+06   0.000000e+00   6371s
  561255    7.1631320e+08   3.181169e+06   0.000000e+00   6375s
  561861    7.1531743e+08   3.176054e+06   0.000000e+00   6381s
  562366    7.1451201e+08   3.173058e+06   0.000000e+00   6385s
  562972    7.1333607e+08   3.013999e+06   0.000000e+00   6391s
  563477    7.1325313e+08   2.771349e+06   0.000000e+00   6395s
  564083    7.1316928e+08   2.715000e+06   0.000000e+00   6401s
  564689    7.1307276e+08   2.752908e+06   0.000000e+00   6406s
  565194    7.1298323e+08   2.774157e+06   0.000000e+00   6410s
  565800    7.1289241e+08   2.824740e+06   0.000000e+00   6415s
  566406    7.1278475e+08   2.863748e+06   0.000000e+00   6421s
  566911    7.1266109e+08   2.840297e+06   0.000000e+00   6425s
  567517    7.1243447e+08   2.914132e+06   0.000000e+00   6430s
  568123    7.1204231e+08   3.022263e+06   0.000000e+00   6435s
  568729    7.1114962e+08   3.038528e+06   0.000000e+00   6440s
  569335    7.1022973e+08   3.064285e+06   0.000000e+00   6446s
  569840    7.0958289e+08   3.080955e+06   0.000000e+00   6450s
  570446    7.0850145e+08   3.085482e+06   0.000000e+00   6456s
  571052    7.0756912e+08   3.073655e+06   0.000000e+00   6461s
  571658    7.0676858e+08   3.076992e+06   0.000000e+00   6465s
  572264    7.0552542e+08   3.069210e+06   0.000000e+00   6471s
  572870    7.0464061e+08   3.104519e+06   0.000000e+00   6476s
  573476    7.0373169e+08   3.035980e+06   0.000000e+00   6481s
  573981    7.0223111e+08   3.039632e+06   0.000000e+00   6485s
  574587    7.0161959e+08   2.748026e+06   0.000000e+00   6490s
  575193    7.0154503e+08   2.710761e+06   0.000000e+00   6495s
  575799    7.0145338e+08   2.647612e+06   0.000000e+00   6501s
  576405    7.0134869e+08   2.620210e+06   0.000000e+00   6506s
  576910    7.0124989e+08   2.669040e+06   0.000000e+00   6510s
  577516    7.0112246e+08   2.691322e+06   0.000000e+00   6515s
  578122    7.0102196e+08   2.795141e+06   0.000000e+00   6520s
  578728    7.0084451e+08   2.945958e+06   0.000000e+00   6526s
  579334    7.0068961e+08   2.985071e+06   0.000000e+00   6530s
  579940    7.0052597e+08   2.967819e+06   0.000000e+00   6536s
  580546    6.9985673e+08   2.938619e+06   0.000000e+00   6541s
  581152    6.9872965e+08   2.943424e+06   0.000000e+00   6546s
  581657    6.9785998e+08   2.940537e+06   0.000000e+00   6550s
  582263    6.9690973e+08   2.970125e+06   0.000000e+00   6555s
  582970    6.9616714e+08   2.946313e+06   0.000000e+00   6561s
  583576    6.9530231e+08   2.948234e+06   0.000000e+00   6566s
  584182    6.9452419e+08   2.956909e+06   0.000000e+00   6571s
  584788    6.9390301e+08   2.968526e+06   0.000000e+00   6576s
  585394    6.9337412e+08   3.014981e+06   0.000000e+00   6581s
  586000    6.9293908e+08   2.756914e+06   0.000000e+00   6586s
  586606    6.9286467e+08   2.598908e+06   0.000000e+00   6591s
  587111    6.9280414e+08   2.577274e+06   0.000000e+00   6595s
  587717    6.9271048e+08   2.591234e+06   0.000000e+00   6601s
  588323    6.9259793e+08   2.649358e+06   0.000000e+00   6606s
  588828    6.9253872e+08   2.575924e+06   0.000000e+00   6610s
  589434    6.9241023e+08   2.548677e+06   0.000000e+00   6615s
  590040    6.9228052e+08   2.668998e+06   0.000000e+00   6620s
  590646    6.9216091e+08   2.704643e+06   0.000000e+00   6626s
  591151    6.9195484e+08   2.695452e+06   0.000000e+00   6630s
  591757    6.9120850e+08   2.597615e+06   0.000000e+00   6635s
  592363    6.9021981e+08   2.580888e+06   0.000000e+00   6641s
  592969    6.8840562e+08   2.624823e+06   0.000000e+00   6646s
  593575    6.8681557e+08   2.825216e+06   0.000000e+00   6651s
  594080    6.8619471e+08   2.837744e+06   0.000000e+00   6655s
  594686    6.8506938e+08   2.930932e+06   0.000000e+00   6660s
  595292    6.8418442e+08   3.004242e+06   0.000000e+00   6666s
  595797    6.8356615e+08   3.008708e+06   0.000000e+00   6670s
  596504    6.8307181e+08   3.042143e+06   0.000000e+00   6676s
  597009    6.8224390e+08   3.038167e+06   0.000000e+00   6680s
  597615    6.8188638e+08   2.451206e+06   0.000000e+00   6685s
  598221    6.8178806e+08   2.442982e+06   0.000000e+00   6691s
  598827    6.8170386e+08   2.445543e+06   0.000000e+00   6696s
  599433    6.8160027e+08   2.643734e+06   0.000000e+00   6701s
  599938    6.8149927e+08   2.440951e+06   0.000000e+00   6705s
  600544    6.8135965e+08   2.472032e+06   0.000000e+00   6710s
  601150    6.8122753e+08   2.649553e+06   0.000000e+00   6716s
  601655    6.8110519e+08   2.660554e+06   0.000000e+00   6720s
  602261    6.8093501e+08   2.694725e+06   0.000000e+00   6725s
  602867    6.8070322e+08   2.719222e+06   0.000000e+00   6731s
  603473    6.8017934e+08   2.679940e+06   0.000000e+00   6736s
  603978    6.7953076e+08   2.689695e+06   0.000000e+00   6740s
  604584    6.7870102e+08   2.717962e+06   0.000000e+00   6745s
  605190    6.7730527e+08   2.726396e+06   0.000000e+00   6750s
  605796    6.7648784e+08   2.762785e+06   0.000000e+00   6756s
  606402    6.7586605e+08   2.738038e+06   0.000000e+00   6761s
  607008    6.7482962e+08   2.767819e+06   0.000000e+00   6766s
  607513    6.7423943e+08   2.793923e+06   0.000000e+00   6770s
  608119    6.7338793e+08   2.778473e+06   0.000000e+00   6776s
  608725    6.7256859e+08   2.771142e+06   0.000000e+00   6781s
  609230    6.7251088e+08   2.370525e+06   0.000000e+00   6785s
  609836    6.7241349e+08   2.316855e+06   0.000000e+00   6790s
  610442    6.7232804e+08   2.351939e+06   0.000000e+00   6795s
  611048    6.7222809e+08   2.417379e+06   0.000000e+00   6800s
  611553    6.7216329e+08   2.425744e+06   0.000000e+00   6805s
  612159    6.7205977e+08   2.492185e+06   0.000000e+00   6811s
  612664    6.7194763e+08   2.541819e+06   0.000000e+00   6815s
  613270    6.7180551e+08   2.539360e+06   0.000000e+00   6821s
  613775    6.7171342e+08   2.546512e+06   0.000000e+00   6825s
  614381    6.7098363e+08   2.559204e+06   0.000000e+00   6831s
  614987    6.7037197e+08   2.620753e+06   0.000000e+00   6836s
  615492    6.6945984e+08   2.613439e+06   0.000000e+00   6840s
  616098    6.6886851e+08   2.620834e+06   0.000000e+00   6845s
  616704    6.6828850e+08   2.603208e+06   0.000000e+00   6850s
  617310    6.6720393e+08   2.609061e+06   0.000000e+00   6856s
  617815    6.6665308e+08   2.608612e+06   0.000000e+00   6860s
  618421    6.6567725e+08   2.608264e+06   0.000000e+00   6865s
  619027    6.6508791e+08   2.605681e+06   0.000000e+00   6870s
  619633    6.6444877e+08   2.605397e+06   0.000000e+00   6876s
  620138    6.6401746e+08   2.617443e+06   0.000000e+00   6880s
  620744    6.6389658e+08   2.262882e+06   0.000000e+00   6885s
  621350    6.6381577e+08   2.211207e+06   0.000000e+00   6891s
  621855    6.6374554e+08   2.283184e+06   0.000000e+00   6895s
  622461    6.6366746e+08   2.242002e+06   0.000000e+00   6901s
  622966    6.6359560e+08   2.275919e+06   0.000000e+00   6905s
  623572    6.6348914e+08   2.312689e+06   0.000000e+00   6910s
  624178    6.6336909e+08   2.395380e+06   0.000000e+00   6916s
  624784    6.6326337e+08   2.390417e+06   0.000000e+00   6921s
  625289    6.6314532e+08   2.456186e+06   0.000000e+00   6925s
  625895    6.6297347e+08   2.543672e+06   0.000000e+00   6930s
  626501    6.6228960e+08   2.569435e+06   0.000000e+00   6935s
  627006    6.6109144e+08   2.585683e+06   0.000000e+00   6940s
  627612    6.6057216e+08   2.573821e+06   0.000000e+00   6945s
  628218    6.6000214e+08   2.549728e+06   0.000000e+00   6950s
  628824    6.5936374e+08   2.608018e+06   0.000000e+00   6956s
  629329    6.5903537e+08   2.594334e+06   0.000000e+00   6960s
  629935    6.5838210e+08   2.603398e+06   0.000000e+00   6965s
  630541    6.5800004e+08   2.587479e+06   0.000000e+00   6971s
  631147    6.5782958e+08   2.581152e+06   0.000000e+00   6975s
  631753    6.5736580e+08   2.304381e+06   0.000000e+00   6980s
  632359    6.5730303e+08   2.126507e+06   0.000000e+00   6986s
  632864    6.5722480e+08   2.158079e+06   0.000000e+00   6990s
  633470    6.5714145e+08   2.154003e+06   0.000000e+00   6995s
  634076    6.5704167e+08   2.174322e+06   0.000000e+00   7001s
  634581    6.5695184e+08   2.170088e+06   0.000000e+00   7005s
  635187    6.5684512e+08   2.181578e+06   0.000000e+00   7010s
  635793    6.5673515e+08   2.232172e+06   0.000000e+00   7016s
  636399    6.5660531e+08   2.311494e+06   0.000000e+00   7021s
  636904    6.5641375e+08   2.300335e+06   0.000000e+00   7025s
  637510    6.5585797e+08   2.300926e+06   0.000000e+00   7031s
  638015    6.5530752e+08   2.304913e+06   0.000000e+00   7035s
  638621    6.5414728e+08   2.345135e+06   0.000000e+00   7040s
  639227    6.5328826e+08   2.359238e+06   0.000000e+00   7046s
  639732    6.5239600e+08   2.371669e+06   0.000000e+00   7050s
  640338    6.5140452e+08   2.348538e+06   0.000000e+00   7055s
  641045    6.5040216e+08   2.346066e+06   0.000000e+00   7061s
  641651    6.4958496e+08   2.350846e+06   0.000000e+00   7065s
  642257    6.4878843e+08   2.351596e+06   0.000000e+00   7070s
  642964    6.4811984e+08   2.373809e+06   0.000000e+00   7076s
  643570    6.4802779e+08   2.079179e+06   0.000000e+00   7081s
  644176    6.4795282e+08   2.043755e+06   0.000000e+00   7085s
  644883    6.4786952e+08   2.069338e+06   0.000000e+00   7091s
  645489    6.4774506e+08   2.153072e+06   0.000000e+00   7095s
  646095    6.4762739e+08   2.290388e+06   0.000000e+00   7100s
  646802    6.4747518e+08   2.850530e+06   0.000000e+00   7106s
  647509    6.4732483e+08   2.925294e+06   0.000000e+00   7111s
  648115    6.4719966e+08   3.034147e+06   0.000000e+00   7115s
  648721    6.4698168e+08   3.031284e+06   0.000000e+00   7120s
  649327    6.4546170e+08   3.072194e+06   0.000000e+00   7125s
  649933    6.4484509e+08   3.074965e+06   0.000000e+00   7130s
  650539    6.4427076e+08   3.081962e+06   0.000000e+00   7135s
  651246    6.4195478e+08   3.078669e+06   0.000000e+00   7141s
  651852    6.4110952e+08   3.094837e+06   0.000000e+00   7145s
  652559    6.4053326e+08   3.028812e+06   0.000000e+00   7151s
  653266    6.4002215e+08   3.113511e+06   0.000000e+00   7156s
  653872    6.3939164e+08   3.031827e+06   0.000000e+00   7160s
  654579    6.3853177e+08   2.168035e+06   0.000000e+00   7165s
  655286    6.3847529e+08   2.043353e+06   0.000000e+00   7171s
  655993    6.3838501e+08   2.116555e+06   0.000000e+00   7176s
  656599    6.3830100e+08   2.111134e+06   0.000000e+00   7180s
  657205    6.3821695e+08   2.125328e+06   0.000000e+00   7185s
  657811    6.3811735e+08   2.226054e+06   0.000000e+00   7191s
  658417    6.3800135e+08   2.266551e+06   0.000000e+00   7195s
  659124    6.3782723e+08   2.282066e+06   0.000000e+00   7200s
  659831    6.3770051e+08   2.427740e+06   0.000000e+00   7205s
  660538    6.3717981e+08   2.362946e+06   0.000000e+00   7211s
  661144    6.3657310e+08   2.406350e+06   0.000000e+00   7215s
  661851    6.3538561e+08   2.376892e+06   0.000000e+00   7221s
  662457    6.3449492e+08   2.367234e+06   0.000000e+00   7225s
  663164    6.3403789e+08   2.310807e+06   0.000000e+00   7230s
  663871    6.3330296e+08   2.306501e+06   0.000000e+00   7236s
  664477    6.3266372e+08   2.338816e+06   0.000000e+00   7240s
  665184    6.3186271e+08   2.347345e+06   0.000000e+00   7245s
  665891    6.3101910e+08   2.359116e+06   0.000000e+00   7250s
  666598    6.3095127e+08   1.950181e+06   0.000000e+00   7256s
  667204    6.3085896e+08   1.992974e+06   0.000000e+00   7260s
  667911    6.3077733e+08   1.996593e+06   0.000000e+00   7266s
  668517    6.3071151e+08   2.000451e+06   0.000000e+00   7271s
  669123    6.3061553e+08   2.026830e+06   0.000000e+00   7275s
  669830    6.3048687e+08   2.100138e+06   0.000000e+00   7281s
  670436    6.3036039e+08   2.156341e+06   0.000000e+00   7285s
  671042    6.3023605e+08   2.191916e+06   0.000000e+00   7290s
  671749    6.3003042e+08   2.320337e+06   0.000000e+00   7296s
  672254    6.2982636e+08   2.265440e+06   0.000000e+00   7300s
  672860    6.2910768e+08   2.268890e+06   0.000000e+00   7305s
  673567    6.2780354e+08   2.272434e+06   0.000000e+00   7311s
  674173    6.2714894e+08   2.274624e+06   0.000000e+00   7315s
  674880    6.2617323e+08   2.263869e+06   0.000000e+00   7320s
  675486    6.2509061e+08   2.276164e+06   0.000000e+00   7325s
  676193    6.2473456e+08   2.305507e+06   0.000000e+00   7330s
  676900    6.2453889e+08   2.293521e+06   0.000000e+00   7336s
  677506    6.2437091e+08   2.056861e+06   0.000000e+00   7340s
  678213    6.2429475e+08   1.893170e+06   0.000000e+00   7346s
  678819    6.2423118e+08   1.897111e+06   0.000000e+00   7350s
  679526    6.2411614e+08   1.861662e+06   0.000000e+00   7356s
  680132    6.2403737e+08   1.924028e+06   0.000000e+00   7360s
  680839    6.2394986e+08   1.905425e+06   0.000000e+00   7366s
  681546    6.2383128e+08   1.951184e+06   0.000000e+00   7371s
  682152    6.2370130e+08   1.969483e+06   0.000000e+00   7375s
  682859    6.2354316e+08   1.994555e+06   0.000000e+00   7380s
  683566    6.2326778e+08   2.012991e+06   0.000000e+00   7385s
  684273    6.2291613e+08   2.016527e+06   0.000000e+00   7391s
  684879    6.2245065e+08   2.038338e+06   0.000000e+00   7395s
  685586    6.2218975e+08   2.005919e+06   0.000000e+00   7400s
  686293    6.2176065e+08   2.008284e+06   0.000000e+00   7405s
  687000    6.2114245e+08   2.015456e+06   0.000000e+00   7410s
  687707    6.2054963e+08   2.008457e+06   0.000000e+00   7415s
  688414    6.1949222e+08   2.009706e+06   0.000000e+00   7420s
  689020    6.1914898e+08   1.780503e+06   0.000000e+00   7425s
  689626    6.1908162e+08   1.757574e+06   0.000000e+00   7430s
  690333    6.1900415e+08   1.753002e+06   0.000000e+00   7436s
  690939    6.1894348e+08   1.798168e+06   0.000000e+00   7440s
  691646    6.1885044e+08   1.780501e+06   0.000000e+00   7445s
  692353    6.1875297e+08   1.828540e+06   0.000000e+00   7451s
  692959    6.1864544e+08   1.843101e+06   0.000000e+00   7455s
  693666    6.1852443e+08   1.826023e+06   0.000000e+00   7460s
  694373    6.1826345e+08   1.847265e+06   0.000000e+00   7466s
  694979    6.1748960e+08   1.843065e+06   0.000000e+00   7470s
  695686    6.1632262e+08   1.833947e+06   0.000000e+00   7475s
  696393    6.1572755e+08   1.850326e+06   0.000000e+00   7480s
  697100    6.1525012e+08   1.897427e+06   0.000000e+00   7486s
  697706    6.1463311e+08   1.945357e+06   0.000000e+00   7490s
  698413    6.1399602e+08   1.951508e+06   0.000000e+00   7495s
  699120    6.1308392e+08   1.952328e+06   0.000000e+00   7500s
  699726    6.1222508e+08   1.956304e+06   0.000000e+00   7505s
  700433    6.1185034e+08   1.742859e+06   0.000000e+00   7510s
  701140    6.1179030e+08   1.721131e+06   0.000000e+00   7515s
  701847    6.1171888e+08   1.708176e+06   0.000000e+00   7521s
  702453    6.1165694e+08   1.724417e+06   0.000000e+00   7525s
  703160    6.1158080e+08   1.706656e+06   0.000000e+00   7530s
  703766    6.1149026e+08   1.728775e+06   0.000000e+00   7535s
  704473    6.1138406e+08   1.761502e+06   0.000000e+00   7541s
  705079    6.1125993e+08   1.816733e+06   0.000000e+00   7545s
  705786    6.1059656e+08   1.874969e+06   0.000000e+00   7550s
  706493    6.0997720e+08   1.871296e+06   0.000000e+00   7556s
  707200    6.0940703e+08   1.917385e+06   0.000000e+00   7561s
  707806    6.0904308e+08   1.895676e+06   0.000000e+00   7565s
  708513    6.0849332e+08   1.851251e+06   0.000000e+00   7570s
  709220    6.0777614e+08   1.854723e+06   0.000000e+00   7576s
  709826    6.0706579e+08   1.928285e+06   0.000000e+00   7580s
  710533    6.0682743e+08   1.946091e+06   0.000000e+00   7586s
  711038    6.0651187e+08   1.951429e+06   0.000000e+00   7590s
  711745    6.0600453e+08   1.951266e+06   0.000000e+00   7596s
  712351    6.0594480e+08   1.644359e+06   0.000000e+00   7600s
  713058    6.0586874e+08   1.613580e+06   0.000000e+00   7605s
  713765    6.0577996e+08   1.640357e+06   0.000000e+00   7611s
  714371    6.0569697e+08   1.686721e+06   0.000000e+00   7615s
  715078    6.0559252e+08   1.758501e+06   0.000000e+00   7620s
  715785    6.0550226e+08   1.828221e+06   0.000000e+00   7626s
  716391    6.0539100e+08   1.921187e+06   0.000000e+00   7630s
  716997    6.0529408e+08   1.926633e+06   0.000000e+00   7635s
  717704    6.0490984e+08   1.955152e+06   0.000000e+00   7641s
  718310    6.0321247e+08   1.970084e+06   0.000000e+00   7645s
  719017    6.0212429e+08   2.126047e+06   0.000000e+00   7651s
  719522    6.0161615e+08   2.020668e+06   0.000000e+00   7655s
  720229    6.0135361e+08   2.027785e+06   0.000000e+00   7660s
  720936    6.0003087e+08   2.073518e+06   0.000000e+00   7666s
  721643    5.9973899e+08   2.076696e+06   0.000000e+00   7671s
  722249    5.9899762e+08   2.097596e+06   0.000000e+00   7675s
  722956    5.9811094e+08   2.099922e+06   0.000000e+00   7680s
  723663    5.9782293e+08   1.642365e+06   0.000000e+00   7685s
  724269    5.9777228e+08   1.643516e+06   0.000000e+00   7690s
  724976    5.9769165e+08   1.659657e+06   0.000000e+00   7696s
  725582    5.9760170e+08   1.746156e+06   0.000000e+00   7701s
  726188    5.9751071e+08   1.735030e+06   0.000000e+00   7705s
  726895    5.9741832e+08   1.799834e+06   0.000000e+00   7710s
  727602    5.9732923e+08   1.821996e+06   0.000000e+00   7716s
  728208    5.9725091e+08   1.815193e+06   0.000000e+00   7720s
  728814    5.9690241e+08   1.822380e+06   0.000000e+00   7725s
  729420    5.9657153e+08   1.827756e+06   0.000000e+00   7730s
  730026    5.9610619e+08   1.823168e+06   0.000000e+00   7735s
  730733    5.9540074e+08   1.838566e+06   0.000000e+00   7740s
  731440    5.9490829e+08   1.821237e+06   0.000000e+00   7745s
  732046    5.9455082e+08   1.835601e+06   0.000000e+00   7750s
  732753    5.9374205e+08   1.853628e+06   0.000000e+00   7756s
  733258    5.9321800e+08   1.839893e+06   0.000000e+00   7760s
  733864    5.9298891e+08   1.901124e+06   0.000000e+00   7765s
  734470    5.9276755e+08   1.923985e+06   0.000000e+00   7770s
  735076    5.9272941e+08   1.534305e+06   0.000000e+00   7776s
  735682    5.9263615e+08   1.569772e+06   0.000000e+00   7781s
  736288    5.9256744e+08   1.574056e+06   0.000000e+00   7786s
  736894    5.9250103e+08   1.715343e+06   0.000000e+00   7791s
  737399    5.9243783e+08   1.651083e+06   0.000000e+00   7795s
  738106    5.9234642e+08   1.707737e+06   0.000000e+00   7801s
  738712    5.9224002e+08   1.748205e+06   0.000000e+00   7806s
  739318    5.9210259e+08   1.879787e+06   0.000000e+00   7811s
  739924    5.9196672e+08   1.935613e+06   0.000000e+00   7815s
  740530    5.9133425e+08   1.847018e+06   0.000000e+00   7820s
  741237    5.9064731e+08   1.877175e+06   0.000000e+00   7826s
  741843    5.9029870e+08   1.867075e+06   0.000000e+00   7830s
  742449    5.8995680e+08   1.878642e+06   0.000000e+00   7835s
  743055    5.8954808e+08   1.855993e+06   0.000000e+00   7840s
  743762    5.8874713e+08   1.863666e+06   0.000000e+00   7846s
  744368    5.8826780e+08   1.853730e+06   0.000000e+00   7851s
  744974    5.8794664e+08   1.879161e+06   0.000000e+00   7855s
  745681    5.8715346e+08   1.870465e+06   0.000000e+00   7860s
  746287    5.8679347e+08   1.546467e+06   0.000000e+00   7865s
  746994    5.8670764e+08   1.481145e+06   0.000000e+00   7870s
  747701    5.8662343e+08   1.512663e+06   0.000000e+00   7876s
  748307    5.8655049e+08   1.558155e+06   0.000000e+00   7880s
  749014    5.8646605e+08   1.589265e+06   0.000000e+00   7886s
  749620    5.8635884e+08   1.624773e+06   0.000000e+00   7890s
  750327    5.8625648e+08   1.705657e+06   0.000000e+00   7896s
  750933    5.8618664e+08   1.781124e+06   0.000000e+00   7900s
  751539    5.8605677e+08   1.815923e+06   0.000000e+00   7905s
  752145    5.8563365e+08   1.842829e+06   0.000000e+00   7911s
  752751    5.8497281e+08   1.839555e+06   0.000000e+00   7915s
  753357    5.8478923e+08   1.847546e+06   0.000000e+00   7920s
  753963    5.8449425e+08   1.886308e+06   0.000000e+00   7925s
  754670    5.8426059e+08   1.895252e+06   0.000000e+00   7931s
  755276    5.8394600e+08   1.895584e+06   0.000000e+00   7935s
  755983    5.8344585e+08   1.886790e+06   0.000000e+00   7941s
  756488    5.8299440e+08   1.915722e+06   0.000000e+00   7945s
  757094    5.8256722e+08   1.896344e+06   0.000000e+00   7950s
  757700    5.8248939e+08   1.521254e+06   0.000000e+00   7955s
  758407    5.8244168e+08   1.451088e+06   0.000000e+00   7961s
  759013    5.8237622e+08   1.441767e+06   0.000000e+00   7965s
  759720    5.8230519e+08   1.611765e+06   0.000000e+00   7970s
  760326    5.8223971e+08   1.641612e+06   0.000000e+00   7975s
  760932    5.8216452e+08   1.630982e+06   0.000000e+00   7980s
  761639    5.8207485e+08   1.717903e+06   0.000000e+00   7986s
  762245    5.8198338e+08   1.681905e+06   0.000000e+00   7991s
  762851    5.8188138e+08   1.767758e+06   0.000000e+00   7996s
  763457    5.8174923e+08   1.799227e+06   0.000000e+00   8000s
  764164    5.8127787e+08   1.859182e+06   0.000000e+00   8006s
  764770    5.8105479e+08   1.864714e+06   0.000000e+00   8010s
  765376    5.8090131e+08   1.910829e+06   0.000000e+00   8015s
  766083    5.8040658e+08   1.920625e+06   0.000000e+00   8020s
  766790    5.7997630e+08   1.950204e+06   0.000000e+00   8026s
  767396    5.7954593e+08   1.956856e+06   0.000000e+00   8031s
  768002    5.7937334e+08   1.973166e+06   0.000000e+00   8035s
  768709    5.7893182e+08   1.520272e+06   0.000000e+00   8041s
  769315    5.7888156e+08   1.478549e+06   0.000000e+00   8045s
  769921    5.7883231e+08   1.500183e+06   0.000000e+00   8051s
  770527    5.7875417e+08   1.525185e+06   0.000000e+00   8056s
  771133    5.7869370e+08   1.564003e+06   0.000000e+00   8061s
  771840    5.7862281e+08   1.569291e+06   0.000000e+00   8066s
  772446    5.7855193e+08   1.555810e+06   0.000000e+00   8070s
  773052    5.7849001e+08   1.567137e+06   0.000000e+00   8075s
  773658    5.7839552e+08   1.581998e+06   0.000000e+00   8080s
  774264    5.7830262e+08   1.709184e+06   0.000000e+00   8086s
  774870    5.7803311e+08   1.749464e+06   0.000000e+00   8091s
  775476    5.7783200e+08   1.782534e+06   0.000000e+00   8096s
  775981    5.7763175e+08   1.791405e+06   0.000000e+00   8100s
  776587    5.7718124e+08   1.801042e+06   0.000000e+00   8105s
  777294    5.7653977e+08   1.788363e+06   0.000000e+00   8111s
  777900    5.7621432e+08   1.869851e+06   0.000000e+00   8115s
  778607    5.7598473e+08   1.871974e+06   0.000000e+00   8120s
  779314    5.7570358e+08   1.968778e+06   0.000000e+00   8126s
  779920    5.7544158e+08   1.964794e+06   0.000000e+00   8131s
  780425    5.7539839e+08   1.462782e+06   0.000000e+00   8135s
  781031    5.7535225e+08   1.416211e+06   0.000000e+00   8140s
  781738    5.7530034e+08   1.434939e+06   0.000000e+00   8145s
  782344    5.7522398e+08   1.480338e+06   0.000000e+00   8150s
  782950    5.7516646e+08   1.466254e+06   0.000000e+00   8155s
  783556    5.7510256e+08   1.490083e+06   0.000000e+00   8160s
  784263    5.7504539e+08   1.556063e+06   0.000000e+00   8166s
  784869    5.7497381e+08   1.605944e+06   0.000000e+00   8170s
  785475    5.7485689e+08   1.837856e+06   0.000000e+00   8175s
  786081    5.7429019e+08   1.761554e+06   0.000000e+00   8180s
  786788    5.7399217e+08   1.755021e+06   0.000000e+00   8186s
  787394    5.7358572e+08   1.784758e+06   0.000000e+00   8191s
  787899    5.7339105e+08   1.805464e+06   0.000000e+00   8195s
  788505    5.7297901e+08   1.882286e+06   0.000000e+00   8201s
  789111    5.7279603e+08   1.920943e+06   0.000000e+00   8206s
  789616    5.7241966e+08   1.920613e+06   0.000000e+00   8210s
  790222    5.7214351e+08   1.957902e+06   0.000000e+00   8215s
  790929    5.7186537e+08   1.964209e+06   0.000000e+00   8220s
  791636    5.7157965e+08   1.392848e+06   0.000000e+00   8226s
  792242    5.7152951e+08   1.378580e+06   0.000000e+00   8231s
  792747    5.7148039e+08   1.337198e+06   0.000000e+00   8235s
  793454    5.7139753e+08   1.431052e+06   0.000000e+00   8241s
  794060    5.7133835e+08   1.431435e+06   0.000000e+00   8246s
  794666    5.7127004e+08   1.403079e+06   0.000000e+00   8251s
  795171    5.7120669e+08   1.441084e+06   0.000000e+00   8255s
  795777    5.7110538e+08   1.495906e+06   0.000000e+00   8260s
  796383    5.7101979e+08   1.499916e+06   0.000000e+00   8265s
  797090    5.7091606e+08   1.500008e+06   0.000000e+00   8270s
  797696    5.7078671e+08   1.500605e+06   0.000000e+00   8275s
  798302    5.7041386e+08   1.506793e+06   0.000000e+00   8280s
  798908    5.7030130e+08   1.577313e+06   0.000000e+00   8285s
  799615    5.6994650e+08   1.600233e+06   0.000000e+00   8290s
  800221    5.6963328e+08   1.640713e+06   0.000000e+00   8295s
  800928    5.6936657e+08   1.641097e+06   0.000000e+00   8301s
  801534    5.6902005e+08   1.648128e+06   0.000000e+00   8305s
  802241    5.6879021e+08   2.147390e+06   0.000000e+00   8311s
  802847    5.6858583e+08   1.387029e+06   0.000000e+00   8315s
  803554    5.6851978e+08   1.346811e+06   0.000000e+00   8321s
  804059    5.6848512e+08   1.363535e+06   0.000000e+00   8325s
  804766    5.6840649e+08   1.525946e+06   0.000000e+00   8331s
  805372    5.6829989e+08   1.599393e+06   0.000000e+00   8335s
  806079    5.6820979e+08   1.576632e+06   0.000000e+00   8341s
  806685    5.6812990e+08   1.613139e+06   0.000000e+00   8346s
  807291    5.6804311e+08   1.634827e+06   0.000000e+00   8350s
  807998    5.6795088e+08   1.623275e+06   0.000000e+00   8356s
  808604    5.6786125e+08   1.628667e+06   0.000000e+00   8360s
  809210    5.6775940e+08   1.627140e+06   0.000000e+00   8365s
  809917    5.6755454e+08   1.691108e+06   0.000000e+00   8371s
  810523    5.6724631e+08   1.688193e+06   0.000000e+00   8375s
  811129    5.6711955e+08   1.716634e+06   0.000000e+00   8380s
  811836    5.6684332e+08   1.719193e+06   0.000000e+00   8386s
  812442    5.6668977e+08   1.717253e+06   0.000000e+00   8390s
  813149    5.6642076e+08   1.696717e+06   0.000000e+00   8395s
  813856    5.6618844e+08   1.760407e+06   0.000000e+00   8401s
  814462    5.6614135e+08   1.319328e+06   0.000000e+00   8406s
  815068    5.6610501e+08   1.291332e+06   0.000000e+00   8410s
  815775    5.6604281e+08   1.286157e+06   0.000000e+00   8416s
  816381    5.6597098e+08   1.321035e+06   0.000000e+00   8420s
  817088    5.6589700e+08   1.328452e+06   0.000000e+00   8426s
  817694    5.6584032e+08   1.374164e+06   0.000000e+00   8430s
  818401    5.6574988e+08   1.458313e+06   0.000000e+00   8435s
  819108    5.6566881e+08   1.509068e+06   0.000000e+00   8441s
  819815    5.6555200e+08   1.494620e+06   0.000000e+00   8446s
  820421    5.6543040e+08   1.615056e+06   0.000000e+00   8450s
  821128    5.6511538e+08   1.532932e+06   0.000000e+00   8456s
  821734    5.6497835e+08   1.533137e+06   0.000000e+00   8460s
  822441    5.6449305e+08   1.592274e+06   0.000000e+00   8465s
  823148    5.6427893e+08   1.580434e+06   0.000000e+00   8471s
  823754    5.6393044e+08   1.580832e+06   0.000000e+00   8475s
  824461    5.6375464e+08   1.568970e+06   0.000000e+00   8481s
  825067    5.6343894e+08   1.572833e+06   0.000000e+00   8485s
  825774    5.6334557e+08   1.324069e+06   0.000000e+00   8490s
  826380    5.6330424e+08   1.417444e+06   0.000000e+00   8495s
  827087    5.6324396e+08   1.349333e+06   0.000000e+00   8501s
  827693    5.6319423e+08   1.319581e+06   0.000000e+00   8505s
  828400    5.6312798e+08   1.353542e+06   0.000000e+00   8510s
  829006    5.6303898e+08   1.417307e+06   0.000000e+00   8515s
  829713    5.6294038e+08   1.476003e+06   0.000000e+00   8520s
  830420    5.6280578e+08   1.552921e+06   0.000000e+00   8526s
  831026    5.6272195e+08   1.560351e+06   0.000000e+00   8530s
  831733    5.6261153e+08   1.606352e+06   0.000000e+00   8536s
  832440    5.6235128e+08   1.608695e+06   0.000000e+00   8541s
  833046    5.6216485e+08   1.661351e+06   0.000000e+00   8545s
  833753    5.6174970e+08   1.713126e+06   0.000000e+00   8550s
  834460    5.6139710e+08   1.737499e+06   0.000000e+00   8555s
  835167    5.6105676e+08   1.756192e+06   0.000000e+00   8561s
  835874    5.6081229e+08   1.763573e+06   0.000000e+00   8566s
  836480    5.6048742e+08   1.764032e+06   0.000000e+00   8570s
  837187    5.6037396e+08   1.283948e+06   0.000000e+00   8575s
  837793    5.6032070e+08   1.320283e+06   0.000000e+00   8580s
  838500    5.6025164e+08   1.266611e+06   0.000000e+00   8585s
  839106    5.6018822e+08   1.249420e+06   0.000000e+00   8590s
  839813    5.6011214e+08   1.318513e+06   0.000000e+00   8595s
  840520    5.6004923e+08   1.365698e+06   0.000000e+00   8601s
  841126    5.5997842e+08   1.350703e+06   0.000000e+00   8605s
  841833    5.5987349e+08   1.522271e+06   0.000000e+00   8611s
  842338    5.5980582e+08   1.526140e+06   0.000000e+00   8615s
  842944    5.5965137e+08   1.513711e+06   0.000000e+00   8620s
  843449    5.5957317e+08   1.519315e+06   0.000000e+00   8625s
  844055    5.5957081e+08   1.520299e+06   0.000000e+00   8630s
  844560    5.5949289e+08   1.524864e+06   0.000000e+00   8635s
  845166    5.5929533e+08   1.522175e+06   0.000000e+00   8641s
  845671    5.5926369e+08   1.521296e+06   0.000000e+00   8645s
  846378    5.5902087e+08   1.586579e+06   0.000000e+00   8651s
  846984    5.5895515e+08   1.597646e+06   0.000000e+00   8655s
  847691    5.5872129e+08   1.600139e+06   0.000000e+00   8661s
  848297    5.5865006e+08   1.198314e+06   0.000000e+00   8666s
  848903    5.5860950e+08   1.182380e+06   0.000000e+00   8671s
  849509    5.5856546e+08   1.154024e+06   0.000000e+00   8675s
  850115    5.5851175e+08   1.236813e+06   0.000000e+00   8680s
  850822    5.5842957e+08   1.404190e+06   0.000000e+00   8686s
  851428    5.5834589e+08   1.374367e+06   0.000000e+00   8690s
  852034    5.5829242e+08   1.546863e+06   0.000000e+00   8695s
  852640    5.5820125e+08   1.395580e+06   0.000000e+00   8700s
  853347    5.5811700e+08   1.336497e+06   0.000000e+00   8706s
  853953    5.5785384e+08   1.358288e+06   0.000000e+00   8711s
  854559    5.5773586e+08   1.361818e+06   0.000000e+00   8715s
  855165    5.5736525e+08   1.385172e+06   0.000000e+00   8720s
  855771    5.5706831e+08   1.451121e+06   0.000000e+00   8725s
  856478    5.5677991e+08   1.498787e+06   0.000000e+00   8731s
  857084    5.5667536e+08   1.492396e+06   0.000000e+00   8735s
  857690    5.5652699e+08   1.486525e+06   0.000000e+00   8740s
  858397    5.5636695e+08   1.522039e+06   0.000000e+00   8746s
  859003    5.5612199e+08   1.478699e+06   0.000000e+00   8750s
  859609    5.5605278e+08   1.230996e+06   0.000000e+00   8755s
  860316    5.5599958e+08   1.103992e+06   0.000000e+00   8761s
  860922    5.5595279e+08   1.137224e+06   0.000000e+00   8765s
  861528    5.5589761e+08   1.146630e+06   0.000000e+00   8770s
  862235    5.5582916e+08   1.152271e+06   0.000000e+00   8776s
  862841    5.5575159e+08   1.206297e+06   0.000000e+00   8781s
  863447    5.5567565e+08   1.241291e+06   0.000000e+00   8786s
  864053    5.5563392e+08   1.236390e+06   0.000000e+00   8790s
  864659    5.5557524e+08   1.284004e+06   0.000000e+00   8795s
  865265    5.5550732e+08   1.279489e+06   0.000000e+00   8800s
  865871    5.5543007e+08   1.317209e+06   0.000000e+00   8805s
  866477    5.5513216e+08   1.349955e+06   0.000000e+00   8810s
  867083    5.5493109e+08   1.332386e+06   0.000000e+00   8815s
  867790    5.5475922e+08   1.375665e+06   0.000000e+00   8821s
  868396    5.5447503e+08   1.358317e+06   0.000000e+00   8826s
  869002    5.5418390e+08   1.338572e+06   0.000000e+00   8831s
  869608    5.5406968e+08   1.352199e+06   0.000000e+00   8835s
  870214    5.5381469e+08   1.403734e+06   0.000000e+00   8840s
  870820    5.5362695e+08   1.128084e+06   0.000000e+00   8845s
  871527    5.5358441e+08   1.085027e+06   0.000000e+00   8851s
  872133    5.5353555e+08   1.138397e+06   0.000000e+00   8856s
  872739    5.5348956e+08   1.209925e+06   0.000000e+00   8861s
  873345    5.5344011e+08   1.219861e+06   0.000000e+00   8866s
  873951    5.5339739e+08   1.240899e+06   0.000000e+00   8871s
  874557    5.5334578e+08   1.308055e+06   0.000000e+00   8875s
  875264    5.5326642e+08   1.320688e+06   0.000000e+00   8881s
  875870    5.5319491e+08   1.353975e+06   0.000000e+00   8886s
  876476    5.5312638e+08   1.378047e+06   0.000000e+00   8890s
  877082    5.5295767e+08   1.407714e+06   0.000000e+00   8895s
  877688    5.5266396e+08   1.385565e+06   0.000000e+00   8901s
  878294    5.5249254e+08   1.390963e+06   0.000000e+00   8905s
  878900    5.5221221e+08   1.409435e+06   0.000000e+00   8910s
  879506    5.5200843e+08   1.400387e+06   0.000000e+00   8915s
  880112    5.5174780e+08   1.444380e+06   0.000000e+00   8920s
  880718    5.5161489e+08   1.466203e+06   0.000000e+00   8925s
  881425    5.5141914e+08   1.485635e+06   0.000000e+00   8930s
  882031    5.5132098e+08   1.985501e+06   0.000000e+00   8935s
  882637    5.5128566e+08   1.089003e+06   0.000000e+00   8940s
  883344    5.5123473e+08   1.045322e+06   0.000000e+00   8946s
  883950    5.5117704e+08   1.080744e+06   0.000000e+00   8950s
  884556    5.5112648e+08   1.114897e+06   0.000000e+00   8955s
  885162    5.5108151e+08   1.119975e+06   0.000000e+00   8960s
  885869    5.5101534e+08   1.315698e+06   0.000000e+00   8966s
  886475    5.5094792e+08   1.412455e+06   0.000000e+00   8971s
  887081    5.5089815e+08   1.412544e+06   0.000000e+00   8976s
  887687    5.5081488e+08   1.424887e+06   0.000000e+00   8980s
  888293    5.5073208e+08   1.376613e+06   0.000000e+00   8985s
  888899    5.5045194e+08   1.373478e+06   0.000000e+00   8990s
  889606    5.5018211e+08   1.397468e+06   0.000000e+00   8996s
  890212    5.4992373e+08   1.403735e+06   0.000000e+00   9001s
  890818    5.4973893e+08   1.408206e+06   0.000000e+00   9006s
  891424    5.4957177e+08   1.413526e+06   0.000000e+00   9011s
  892030    5.4939708e+08   1.469744e+06   0.000000e+00   9015s
  892636    5.4921517e+08   1.517247e+06   0.000000e+00   9020s
  893242    5.4895033e+08   1.520039e+06   0.000000e+00   9025s
  893848    5.4889899e+08   1.266874e+06   0.000000e+00   9030s
  894454    5.4885404e+08   1.420656e+06   0.000000e+00   9035s
  895161    5.4879475e+08   1.473681e+06   0.000000e+00   9041s
  895767    5.4874054e+08   1.516061e+06   0.000000e+00   9046s
  896373    5.4868589e+08   1.502787e+06   0.000000e+00   9051s
  896979    5.4864649e+08   1.546781e+06   0.000000e+00   9056s
  897585    5.4859644e+08   1.610267e+06   0.000000e+00   9061s
  898191    5.4854838e+08   1.246261e+06   0.000000e+00   9066s
  898696    5.4849129e+08   1.278111e+06   0.000000e+00   9070s
  899302    5.4841245e+08   1.363459e+06   0.000000e+00   9075s
  899908    5.4833018e+08   1.404557e+06   0.000000e+00   9081s
  900514    5.4816180e+08   1.465851e+06   0.000000e+00   9086s
  901120    5.4791622e+08   1.473325e+06   0.000000e+00   9090s
  901726    5.4743323e+08   1.464864e+06   0.000000e+00   9095s
  902332    5.4730553e+08   1.461129e+06   0.000000e+00   9100s
  902938    5.4717410e+08   1.457612e+06   0.000000e+00   9106s
  903544    5.4701625e+08   1.456856e+06   0.000000e+00   9111s
  904049    5.4688720e+08   1.455989e+06   0.000000e+00   9115s
  904655    5.4675733e+08   1.459790e+06   0.000000e+00   9120s
  905261    5.4670039e+08   1.018152e+06   0.000000e+00   9125s
  905867    5.4664778e+08   1.003044e+06   0.000000e+00   9131s
  906473    5.4657599e+08   9.644531e+05   0.000000e+00   9135s
  907079    5.4653953e+08   9.621643e+05   0.000000e+00   9140s
  907786    5.4647830e+08   1.006599e+06   0.000000e+00   9146s
  908291    5.4642282e+08   1.060146e+06   0.000000e+00   9150s
  908897    5.4633955e+08   1.163105e+06   0.000000e+00   9155s
  909503    5.4626822e+08   1.204945e+06   0.000000e+00   9160s
  910109    5.4620522e+08   1.197633e+06   0.000000e+00   9165s
  910715    5.4609350e+08   1.233591e+06   0.000000e+00   9170s
  911321    5.4601083e+08   1.240976e+06   0.000000e+00   9175s
  911927    5.4593085e+08   1.251498e+06   0.000000e+00   9180s
  912533    5.4591501e+08   1.251347e+06   0.000000e+00   9186s
  912937    5.4590142e+08   1.248376e+06   0.000000e+00   9190s
  913543    5.4578095e+08   1.280539e+06   0.000000e+00   9195s
  914250    5.4564696e+08   1.267457e+06   0.000000e+00   9201s
  914755    5.4552888e+08   1.262867e+06   0.000000e+00   9205s
  915361    5.4543595e+08   1.264980e+06   0.000000e+00   9210s
  916068    5.4529358e+08   1.263862e+06   0.000000e+00   9216s
  916674    5.4526127e+08   1.010452e+06   0.000000e+00   9220s
  917381    5.4520367e+08   9.712393e+05   0.000000e+00   9226s
  917987    5.4515775e+08   9.911313e+05   0.000000e+00   9230s
  918593    5.4510688e+08   1.034674e+06   0.000000e+00   9235s
  919300    5.4504256e+08   1.041153e+06   0.000000e+00   9240s
  919906    5.4495572e+08   1.267078e+06   0.000000e+00   9245s
  920512    5.4488842e+08   1.245012e+06   0.000000e+00   9250s
  921219    5.4482325e+08   1.145732e+06   0.000000e+00   9255s
  921825    5.4475339e+08   1.162267e+06   0.000000e+00   9261s
  922330    5.4470156e+08   1.167049e+06   0.000000e+00   9266s
  922936    5.4460455e+08   1.183301e+06   0.000000e+00   9270s
  923542    5.4448740e+08   1.200392e+06   0.000000e+00   9275s
  924249    5.4437485e+08   1.200122e+06   0.000000e+00   9280s
  924956    5.4428232e+08   1.243203e+06   0.000000e+00   9286s
  925562    5.4413161e+08   1.241488e+06   0.000000e+00   9291s
  926168    5.4407631e+08   1.221894e+06   0.000000e+00   9295s
  926875    5.4382733e+08   1.242406e+06   0.000000e+00   9301s
  927380    5.4375302e+08   1.245990e+06   0.000000e+00   9305s
  927986    5.4371717e+08   9.632464e+05   0.000000e+00   9310s
  928592    5.4367663e+08   9.754969e+05   0.000000e+00   9315s
  929299    5.4363559e+08   9.659346e+05   0.000000e+00   9321s
  929905    5.4357777e+08   9.469680e+05   0.000000e+00   9325s
  930511    5.4352112e+08   9.535029e+05   0.000000e+00   9331s
  931117    5.4347982e+08   9.779648e+05   0.000000e+00   9336s
  931723    5.4343242e+08   1.031684e+06   0.000000e+00   9340s
  932329    5.4336288e+08   1.068813e+06   0.000000e+00   9345s
  932935    5.4329882e+08   1.131160e+06   0.000000e+00   9350s
  933541    5.4320599e+08   1.147996e+06   0.000000e+00   9356s
  934147    5.4309512e+08   1.158161e+06   0.000000e+00   9361s
  934652    5.4298644e+08   1.194218e+06   0.000000e+00   9366s
  935157    5.4290585e+08   1.195803e+06   0.000000e+00   9370s
  935763    5.4263626e+08   1.208576e+06   0.000000e+00   9376s
  936268    5.4246689e+08   1.186844e+06   0.000000e+00   9380s
  936874    5.4222737e+08   1.199180e+06   0.000000e+00   9385s
  937581    5.4198512e+08   1.199631e+06   0.000000e+00   9391s
  938086    5.4183422e+08   1.211401e+06   0.000000e+00   9395s
  938692    5.4170591e+08   1.205500e+06   0.000000e+00   9400s
  939399    5.4165529e+08   8.983959e+05   0.000000e+00   9406s
  940005    5.4160036e+08   8.659714e+05   0.000000e+00   9410s
  940611    5.4156736e+08   9.007068e+05   0.000000e+00   9415s
  941217    5.4152421e+08   9.026460e+05   0.000000e+00   9421s
  941823    5.4148280e+08   9.045692e+05   0.000000e+00   9425s
  942429    5.4144289e+08   1.017985e+06   0.000000e+00   9431s
  943035    5.4140432e+08   1.018395e+06   0.000000e+00   9436s
  943540    5.4134552e+08   1.098322e+06   0.000000e+00   9440s
  944146    5.4128721e+08   1.127981e+06   0.000000e+00   9445s
  944752    5.4120691e+08   1.162351e+06   0.000000e+00   9450s
  945257    5.4115468e+08   1.162676e+06   0.000000e+00   9455s
  945863    5.4105806e+08   1.160240e+06   0.000000e+00   9460s
  946469    5.4083682e+08   1.167629e+06   0.000000e+00   9465s
  947075    5.4065136e+08   1.107299e+06   0.000000e+00   9470s
  947782    5.4039072e+08   1.098528e+06   0.000000e+00   9476s
  948388    5.4021073e+08   1.121840e+06   0.000000e+00   9480s
  949095    5.4006543e+08   1.123070e+06   0.000000e+00   9486s
  949701    5.3997059e+08   1.123984e+06   0.000000e+00   9491s
  950206    5.3987294e+08   9.461479e+05   0.000000e+00   9495s
  950812    5.3982920e+08   9.247997e+05   0.000000e+00   9501s
  951317    5.3979181e+08   9.298319e+05   0.000000e+00   9505s
  951822    5.3975948e+08   9.426245e+05   0.000000e+00   9510s
  952428    5.3971746e+08   9.700036e+05   0.000000e+00   9515s
  953034    5.3968139e+08   9.561302e+05   0.000000e+00   9520s
  953640    5.3963670e+08   9.522576e+05   0.000000e+00   9525s
  954246    5.3957501e+08   9.757235e+05   0.000000e+00   9531s
  954852    5.3950929e+08   1.011233e+06   0.000000e+00   9535s
  955458    5.3943562e+08   1.046787e+06   0.000000e+00   9540s
  956064    5.3933204e+08   1.052601e+06   0.000000e+00   9545s
  956670    5.3914903e+08   1.059519e+06   0.000000e+00   9550s
  957276    5.3890567e+08   1.062597e+06   0.000000e+00   9555s
  957882    5.3880730e+08   1.101260e+06   0.000000e+00   9560s
  958488    5.3872923e+08   1.128642e+06   0.000000e+00   9565s
  959094    5.3846212e+08   1.119184e+06   0.000000e+00   9570s
  959801    5.3829619e+08   1.136157e+06   0.000000e+00   9576s
  960306    5.3816024e+08   1.135428e+06   0.000000e+00   9580s
  960912    5.3806132e+08   1.160847e+06   0.000000e+00   9585s
  961518    5.3789565e+08   1.169675e+06   0.000000e+00   9591s
  962023    5.3785420e+08   8.907919e+05   0.000000e+00   9595s
  962629    5.3781722e+08   8.469369e+05   0.000000e+00   9600s
  963235    5.3777773e+08   8.591350e+05   0.000000e+00   9605s
  963841    5.3773994e+08   8.796489e+05   0.000000e+00   9611s
  964447    5.3770419e+08   9.024027e+05   0.000000e+00   9615s
  965053    5.3766547e+08   9.328434e+05   0.000000e+00   9620s
  965659    5.3759892e+08   9.883698e+05   0.000000e+00   9625s
  966366    5.3751491e+08   1.008454e+06   0.000000e+00   9631s
  966972    5.3744024e+08   9.505091e+05   0.000000e+00   9635s
  967679    5.3737047e+08   9.920370e+05   0.000000e+00   9641s
  968285    5.3729855e+08   1.004958e+06   0.000000e+00   9646s
  968891    5.3722157e+08   1.063363e+06   0.000000e+00   9650s
  969598    5.3700008e+08   1.080588e+06   0.000000e+00   9656s
  970204    5.3683561e+08   1.100096e+06   0.000000e+00   9660s
  970810    5.3671395e+08   1.101101e+06   0.000000e+00   9665s
  971517    5.3658995e+08   1.115073e+06   0.000000e+00   9671s
  972123    5.3643813e+08   1.129185e+06   0.000000e+00   9675s
  972729    5.3632103e+08   1.143708e+06   0.000000e+00   9680s
  973436    5.3626941e+08   8.444439e+05   0.000000e+00   9686s
  974042    5.3624125e+08   8.981407e+05   0.000000e+00   9690s
  974648    5.3620721e+08   9.150732e+05   0.000000e+00   9695s
  975254    5.3617107e+08   9.072159e+05   0.000000e+00   9700s
  975860    5.3612711e+08   9.239278e+05   0.000000e+00   9705s
  976466    5.3609317e+08   9.199823e+05   0.000000e+00   9710s
  977173    5.3603653e+08   9.439224e+05   0.000000e+00   9716s
  977779    5.3599453e+08   9.280468e+05   0.000000e+00   9720s
  978486    5.3589370e+08   9.700791e+05   0.000000e+00   9726s
  978991    5.3583696e+08   9.198404e+05   0.000000e+00   9730s
  979698    5.3577470e+08   9.743696e+05   0.000000e+00   9736s
  980304    5.3571110e+08   1.015511e+06   0.000000e+00   9741s
  980910    5.3551259e+08   1.017051e+06   0.000000e+00   9746s
  981516    5.3534144e+08   1.023385e+06   0.000000e+00   9750s
  982122    5.3518623e+08   1.040261e+06   0.000000e+00   9755s
  982728    5.3508070e+08   1.051105e+06   0.000000e+00   9760s
  983334    5.3496424e+08   1.057043e+06   0.000000e+00   9765s
  983940    5.3462713e+08   1.044478e+06   0.000000e+00   9770s
  984546    5.3455458e+08   8.785718e+05   0.000000e+00   9776s
  985152    5.3450969e+08   8.335046e+05   0.000000e+00   9781s
  985758    5.3445682e+08   8.405675e+05   0.000000e+00   9786s
  986364    5.3440827e+08   8.194961e+05   0.000000e+00   9790s
  986970    5.3435904e+08   8.297360e+05   0.000000e+00   9795s
  987576    5.3432671e+08   9.057632e+05   0.000000e+00   9800s
  988182    5.3426597e+08   9.372606e+05   0.000000e+00   9805s
  988788    5.3422205e+08   9.131931e+05   0.000000e+00   9810s
  989394    5.3416324e+08   9.471300e+05   0.000000e+00   9815s
  990101    5.3407017e+08   9.625749e+05   0.000000e+00   9821s
  990707    5.3400755e+08   9.395962e+05   0.000000e+00   9826s
  991313    5.3392387e+08   9.921908e+05   0.000000e+00   9830s
  992020    5.3379251e+08   1.001682e+06   0.000000e+00   9836s
  992626    5.3364785e+08   9.996661e+05   0.000000e+00   9840s
  993333    5.3347055e+08   1.021321e+06   0.000000e+00   9846s
  993939    5.3331801e+08   1.025303e+06   0.000000e+00   9850s
  994545    5.3317181e+08   1.015429e+06   0.000000e+00   9855s
  995252    5.3303055e+08   1.051938e+06   0.000000e+00   9861s
  995858    5.3297480e+08   8.078553e+05   0.000000e+00   9865s
  996464    5.3294332e+08   7.889251e+05   0.000000e+00   9870s
  997171    5.3288731e+08   7.914757e+05   0.000000e+00   9876s
  997777    5.3284746e+08   8.345627e+05   0.000000e+00   9881s
  998383    5.3280101e+08   8.642195e+05   0.000000e+00   9886s
  998888    5.3277238e+08   8.930342e+05   0.000000e+00   9891s
  999393    5.3270796e+08   8.929167e+05   0.000000e+00   9895s
  999999    5.3265084e+08   8.994399e+05   0.000000e+00   9900s
 1000605    5.3260195e+08   9.378470e+05   0.000000e+00   9906s
 1001211    5.3255654e+08   9.943366e+05   0.000000e+00   9911s
 1001817    5.3249345e+08   9.968564e+05   0.000000e+00   9916s
 1002423    5.3242972e+08   1.014536e+06   0.000000e+00   9920s
 1003029    5.3227890e+08   1.049405e+06   0.000000e+00   9926s
 1003635    5.3163422e+08   1.059753e+06   0.000000e+00   9931s
 1004241    5.3152460e+08   1.067487e+06   0.000000e+00   9935s
 1004847    5.3139760e+08   1.086137e+06   0.000000e+00   9940s
 1005453    5.3129054e+08   1.060555e+06   0.000000e+00   9945s
 1006059    5.3119436e+08   1.054918e+06   0.000000e+00   9951s
 1006665    5.3106643e+08   1.067215e+06   0.000000e+00   9956s
 1007170    5.3103188e+08   8.365366e+05   0.000000e+00   9960s
 1007776    5.3100487e+08   7.690049e+05   0.000000e+00   9965s
 1008483    5.3095618e+08   7.653146e+05   0.000000e+00   9971s
 1009089    5.3090256e+08   7.902573e+05   0.000000e+00   9975s
 1009796    5.3084462e+08   7.906985e+05   0.000000e+00   9981s
 1010402    5.3079815e+08   8.266571e+05   0.000000e+00   9985s
 1011008    5.3074710e+08   8.424299e+05   0.000000e+00   9990s
 1011715    5.3067816e+08   8.385103e+05   0.000000e+00   9996s
 1012321    5.3061434e+08   8.662992e+05   0.000000e+00  10001s
 1012927    5.3057032e+08   8.858836e+05   0.000000e+00  10005s
 1013533    5.3046117e+08   9.768008e+05   0.000000e+00  10010s
 1014240    5.3038785e+08   1.008913e+06   0.000000e+00  10016s
 1014745    5.3032280e+08   9.954953e+05   0.000000e+00  10020s
 1015351    5.2964677e+08   9.969502e+05   0.000000e+00  10025s
 1015957    5.2948387e+08   1.028903e+06   0.000000e+00  10030s
 1016664    5.2936390e+08   1.022771e+06   0.000000e+00  10036s
 1017270    5.2926457e+08   1.026450e+06   0.000000e+00  10041s
 1017876    5.2877816e+08   1.034207e+06   0.000000e+00  10045s
 1018482    5.2870671e+08   7.548260e+05   0.000000e+00  10050s
 1019189    5.2867643e+08   7.670330e+05   0.000000e+00  10056s
 1019795    5.2864485e+08   7.531176e+05   0.000000e+00  10061s
 1020300    5.2861959e+08   7.866426e+05   0.000000e+00  10066s
 1020906    5.2858540e+08   8.315071e+05   0.000000e+00  10071s
 1021512    5.2855300e+08   7.957064e+05   0.000000e+00  10076s
 1022017    5.2849009e+08   8.506668e+05   0.000000e+00  10080s
 1022522    5.2844796e+08   8.804407e+05   0.000000e+00  10085s
 1023229    5.2839116e+08   8.682831e+05   0.000000e+00  10091s
 1023835    5.2833672e+08   9.005041e+05   0.000000e+00  10096s
 1024441    5.2828846e+08   9.477383e+05   0.000000e+00  10101s
 1025047    5.2822421e+08   9.520935e+05   0.000000e+00  10106s
 1025552    5.2810201e+08   9.795226e+05   0.000000e+00  10110s
 1026158    5.2794276e+08   9.959885e+05   0.000000e+00  10115s
 1026764    5.2783526e+08   1.002905e+06   0.000000e+00  10121s
 1027370    5.2768823e+08   1.014028e+06   0.000000e+00  10126s
 1027976    5.2751658e+08   1.017024e+06   0.000000e+00  10130s
 1028582    5.2741842e+08   1.030256e+06   0.000000e+00  10135s
 1029188    5.2729767e+08   1.026074e+06   0.000000e+00  10140s
 1029895    5.2722413e+08   7.302639e+05   0.000000e+00  10146s
 1030501    5.2719052e+08   7.318831e+05   0.000000e+00  10151s
 1031107    5.2715095e+08   7.661478e+05   0.000000e+00  10155s
 1031713    5.2711553e+08   7.541717e+05   0.000000e+00  10160s
 1032319    5.2707058e+08   8.431972e+05   0.000000e+00  10166s
 1032824    5.2703580e+08   8.885336e+05   0.000000e+00  10170s
 1033531    5.2697651e+08   9.385657e+05   0.000000e+00  10176s
 1034036    5.2693252e+08   9.089518e+05   0.000000e+00  10180s
 1034642    5.2688480e+08   1.054934e+06   0.000000e+00  10185s
 1035248    5.2682857e+08   1.076327e+06   0.000000e+00  10190s
 1035955    5.2675255e+08   1.161452e+06   0.000000e+00  10196s
 1036561    5.2663008e+08   1.143922e+06   0.000000e+00  10200s
 1037167    5.2642932e+08   1.126738e+06   0.000000e+00  10205s
 1037874    5.2625806e+08   1.164283e+06   0.000000e+00  10210s
 1038480    5.2611151e+08   1.146312e+06   0.000000e+00  10215s
 1039187    5.2595118e+08   1.149775e+06   0.000000e+00  10221s
 1039692    5.2586375e+08   1.153662e+06   0.000000e+00  10225s
 1040298    5.2554299e+08   1.128198e+06   0.000000e+00  10230s
 1040904    5.2543253e+08   7.141780e+05   0.000000e+00  10235s
 1041409    5.2540930e+08   7.348674e+05   0.000000e+00  10240s
 1042015    5.2537657e+08   7.311004e+05   0.000000e+00  10245s
 1042621    5.2533796e+08   7.760114e+05   0.000000e+00  10250s
 1043227    5.2529966e+08   8.044206e+05   0.000000e+00  10255s
 1043833    5.2526321e+08   9.118861e+05   0.000000e+00  10261s
 1044338    5.2523239e+08   9.327684e+05   0.000000e+00  10265s
 1044944    5.2518104e+08   9.447858e+05   0.000000e+00  10270s
 1045651    5.2510670e+08   9.206072e+05   0.000000e+00  10276s
 1046257    5.2502642e+08   9.531794e+05   0.000000e+00  10281s
 1046863    5.2496984e+08   9.654813e+05   0.000000e+00  10285s
 1047469    5.2489669e+08   1.012297e+06   0.000000e+00  10290s
 1048176    5.2480886e+08   1.075779e+06   0.000000e+00  10296s
 1048782    5.2468557e+08   1.087955e+06   0.000000e+00  10301s
 1049287    5.2456288e+08   1.068271e+06   0.000000e+00  10305s
 1049893    5.2446410e+08   1.099579e+06   0.000000e+00  10311s
 1050499    5.2430657e+08   1.132858e+06   0.000000e+00  10315s
 1051105    5.2419385e+08   1.130986e+06   0.000000e+00  10320s
 1051812    5.2399734e+08   1.145673e+06   0.000000e+00  10326s
 1052418    5.2391197e+08   8.100081e+05   0.000000e+00  10331s
 1052923    5.2386347e+08   8.227489e+05   0.000000e+00  10335s
 1053630    5.2381876e+08   7.288351e+05   0.000000e+00  10340s
 1054236    5.2378322e+08   7.618297e+05   0.000000e+00  10345s
 1054842    5.2373907e+08   8.883072e+05   0.000000e+00  10350s
 1055448    5.2369680e+08   8.689135e+05   0.000000e+00  10355s
 1056155    5.2365030e+08   8.484766e+05   0.000000e+00  10361s
 1056660    5.2361236e+08   8.447310e+05   0.000000e+00  10365s
 1057266    5.2356410e+08   8.242260e+05   0.000000e+00  10370s
 1057872    5.2350805e+08   8.253318e+05   0.000000e+00  10375s
 1058579    5.2344238e+08   8.825044e+05   0.000000e+00  10380s
 1059185    5.2337156e+08   9.330496e+05   0.000000e+00  10385s
 1059791    5.2328502e+08   9.071681e+05   0.000000e+00  10391s
 1060397    5.2320340e+08   9.309407e+05   0.000000e+00  10396s
 1061003    5.2312891e+08   9.432175e+05   0.000000e+00  10400s
 1061609    5.2296876e+08   9.534182e+05   0.000000e+00  10405s
 1062215    5.2280992e+08   9.443953e+05   0.000000e+00  10410s
 1062821    5.2266878e+08   9.956337e+05   0.000000e+00  10416s
 1063326    5.2239351e+08   1.012302e+06   0.000000e+00  10421s
 1063831    5.2235681e+08   7.678549e+05   0.000000e+00  10425s
 1064437    5.2232653e+08   6.465603e+05   0.000000e+00  10430s
 1064942    5.2230497e+08   6.808698e+05   0.000000e+00  10436s
 1065548    5.2226397e+08   7.212038e+05   0.000000e+00  10440s
 1066154    5.2223129e+08   6.236934e+05   0.000000e+00  10445s
 1066861    5.2220634e+08   6.235121e+05   0.000000e+00  10451s
 1067366    5.2218425e+08   6.251076e+05   0.000000e+00  10455s
 1068073    5.2214383e+08   6.401503e+05   0.000000e+00  10461s
 1068679    5.2211236e+08   6.477102e+05   0.000000e+00  10465s
 1069285    5.2208336e+08   6.634618e+05   0.000000e+00  10470s
 1069891    5.2203749e+08   6.719407e+05   0.000000e+00  10475s
 1070497    5.2200280e+08   7.093471e+05   0.000000e+00  10480s
 1071103    5.2194510e+08   7.912167e+05   0.000000e+00  10485s
 1071810    5.2190441e+08   7.758538e+05   0.000000e+00  10491s
 1072416    5.2185334e+08   8.114339e+05   0.000000e+00  10496s
 1073022    5.2175732e+08   8.259318e+05   0.000000e+00  10500s
 1073729    5.2147279e+08   8.341097e+05   0.000000e+00  10506s
 1074335    5.2137058e+08   8.465681e+05   0.000000e+00  10511s
 1074941    5.2124630e+08   8.508146e+05   0.000000e+00  10515s
 1075648    5.2114094e+08   8.572750e+05   0.000000e+00  10521s
 1076254    5.2101666e+08   8.660310e+05   0.000000e+00  10526s
 1076759    5.2093809e+08   8.807649e+05   0.000000e+00  10530s
 1077365    5.2086752e+08   6.572496e+05   0.000000e+00  10535s
 1077971    5.2084242e+08   6.240644e+05   0.000000e+00  10540s
 1078577    5.2081976e+08   6.176806e+05   0.000000e+00  10545s
 1079284    5.2078627e+08   6.108377e+05   0.000000e+00  10551s
 1079890    5.2075435e+08   6.269408e+05   0.000000e+00  10556s
 1080496    5.2072280e+08   6.584775e+05   0.000000e+00  10561s
 1081102    5.2068149e+08   7.103947e+05   0.000000e+00  10565s
 1081708    5.2064277e+08   7.182653e+05   0.000000e+00  10570s
 1082415    5.2057035e+08   7.515597e+05   0.000000e+00  10576s
 1083021    5.2052683e+08   7.709614e+05   0.000000e+00  10581s
 1083627    5.2048469e+08   8.720108e+05   0.000000e+00  10586s
 1084233    5.2036931e+08   8.375163e+05   0.000000e+00  10590s
 1084839    5.2027668e+08   8.423277e+05   0.000000e+00  10595s
 1085445    5.2021555e+08   7.837333e+05   0.000000e+00  10601s
 1086051    5.2015766e+08   7.892082e+05   0.000000e+00  10606s
 1086657    5.2010758e+08   8.378071e+05   0.000000e+00  10611s
 1087162    5.2002473e+08   8.353096e+05   0.000000e+00  10615s
 1087768    5.1998477e+08   8.890565e+05   0.000000e+00  10620s
 1088273    5.1992273e+08   8.959074e+05   0.000000e+00  10625s
 1088879    5.1987940e+08   6.205384e+05   0.000000e+00  10630s
 1089586    5.1984901e+08   6.594329e+05   0.000000e+00  10636s
 1090192    5.1982059e+08   6.118396e+05   0.000000e+00  10641s
 1090697    5.1980092e+08   6.053476e+05   0.000000e+00  10645s
 1091303    5.1976615e+08   6.367683e+05   0.000000e+00  10650s
 1091909    5.1971700e+08   6.613291e+05   0.000000e+00  10655s
 1092414    5.1966777e+08   6.747880e+05   0.000000e+00  10660s
 1093020    5.1963637e+08   6.676032e+05   0.000000e+00  10665s
 1093626    5.1959509e+08   6.793996e+05   0.000000e+00  10670s
 1094232    5.1954880e+08   7.079449e+05   0.000000e+00  10676s
 1094838    5.1950224e+08   7.143872e+05   0.000000e+00  10680s
 1095444    5.1946513e+08   7.370569e+05   0.000000e+00  10685s
 1096151    5.1939818e+08   7.253481e+05   0.000000e+00  10691s
 1096656    5.1936535e+08   7.104745e+05   0.000000e+00  10695s
 1097363    5.1924909e+08   7.113697e+05   0.000000e+00  10701s
 1097868    5.1919838e+08   7.150588e+05   0.000000e+00  10705s
 1098575    5.1912284e+08   7.559086e+05   0.000000e+00  10711s
 1099181    5.1905539e+08   7.531296e+05   0.000000e+00  10715s
 1099787    5.1895931e+08   7.174810e+05   0.000000e+00  10720s
 1100393    5.1893330e+08   5.877629e+05   0.000000e+00  10726s
 1100999    5.1890586e+08   6.011098e+05   0.000000e+00  10731s
 1101605    5.1887320e+08   5.699020e+05   0.000000e+00  10736s
 1102211    5.1884275e+08   6.336492e+05   0.000000e+00  10741s
 1102716    5.1881070e+08   6.331622e+05   0.000000e+00  10745s
 1103322    5.1877643e+08   7.408320e+05   0.000000e+00  10750s
 1103928    5.1874767e+08   7.365926e+05   0.000000e+00  10755s
 1104534    5.1868296e+08   7.311570e+05   0.000000e+00  10760s
 1105140    5.1859759e+08   7.499980e+05   0.000000e+00  10765s
 1105746    5.1854780e+08   7.671388e+05   0.000000e+00  10770s
 1106352    5.1850620e+08   7.706754e+05   0.000000e+00  10775s
 1107059    5.1844606e+08   7.748487e+05   0.000000e+00  10781s
 1107665    5.1840406e+08   7.711128e+05   0.000000e+00  10785s
 1108271    5.1835501e+08   7.739782e+05   0.000000e+00  10790s
 1108978    5.1827196e+08   7.831575e+05   0.000000e+00  10796s
 1109584    5.1815146e+08   7.890296e+05   0.000000e+00  10801s
 1110190    5.1808501e+08   7.862198e+05   0.000000e+00  10806s
 1110695    5.1804290e+08   7.909908e+05   0.000000e+00  10810s
 1111301    5.1801266e+08   6.320187e+05   0.000000e+00  10815s
 1111907    5.1798885e+08   5.630939e+05   0.000000e+00  10821s
 1112412    5.1796750e+08   5.724044e+05   0.000000e+00  10825s
 1113119    5.1792648e+08   6.740327e+05   0.000000e+00  10831s
 1113624    5.1789717e+08   6.591100e+05   0.000000e+00  10835s
 1114230    5.1786469e+08   6.450943e+05   0.000000e+00  10841s
 1114735    5.1784027e+08   6.183964e+05   0.000000e+00  10846s
 1115240    5.1780531e+08   6.291530e+05   0.000000e+00  10850s
 1115846    5.1776782e+08   6.414291e+05   0.000000e+00  10856s
 1116452    5.1773330e+08   6.512726e+05   0.000000e+00  10861s
 1116957    5.1770652e+08   6.304523e+05   0.000000e+00  10865s
 1117462    5.1767584e+08   6.163837e+05   0.000000e+00  10870s
 1118068    5.1763185e+08   6.357177e+05   0.000000e+00  10875s
 1118674    5.1757017e+08   6.838262e+05   0.000000e+00  10880s
 1119381    5.1753228e+08   6.399322e+05   0.000000e+00  10886s
 1119987    5.1748459e+08   6.515068e+05   0.000000e+00  10890s
 1120694    5.1743599e+08   6.458070e+05   0.000000e+00  10896s
 1121300    5.1740183e+08   6.535180e+05   0.000000e+00  10900s
 1121906    5.1730888e+08   6.543935e+05   0.000000e+00  10905s
 1122613    5.1726765e+08   5.368230e+05   0.000000e+00  10911s
 1123219    5.1724297e+08   5.360534e+05   0.000000e+00  10916s
 1123825    5.1720964e+08   5.961801e+05   0.000000e+00  10920s
 1124431    5.1718361e+08   5.940479e+05   0.000000e+00  10925s
 1125138    5.1715539e+08   6.122878e+05   0.000000e+00  10931s
 1125744    5.1709530e+08   6.041357e+05   0.000000e+00  10936s
 1126350    5.1705063e+08   6.212548e+05   0.000000e+00  10940s
 1126956    5.1702312e+08   6.114361e+05   0.000000e+00  10945s
 1127562    5.1698206e+08   6.151780e+05   0.000000e+00  10950s
 1128269    5.1694583e+08   6.259843e+05   0.000000e+00  10956s
 1128875    5.1691045e+08   6.342876e+05   0.000000e+00  10961s
 1129380    5.1685929e+08   6.523681e+05   0.000000e+00  10965s
 1129986    5.1680834e+08   6.448297e+05   0.000000e+00  10970s
 1130592    5.1675925e+08   6.582913e+05   0.000000e+00  10975s
 1131299    5.1670226e+08   6.453306e+05   0.000000e+00  10981s
 1131905    5.1662053e+08   6.441962e+05   0.000000e+00  10985s
 1132511    5.1657419e+08   6.513969e+05   0.000000e+00  10990s
 1133117    5.1651902e+08   6.562223e+05   0.000000e+00  10995s
 1133622    5.1649474e+08   6.346207e+05   0.000000e+00  11000s
 1134228    5.1647037e+08   4.935149e+05   0.000000e+00  11005s
 1134834    5.1645212e+08   4.887580e+05   0.000000e+00  11010s
 1135339    5.1642605e+08   4.957730e+05   0.000000e+00  11015s
 1135945    5.1638309e+08   5.081321e+05   0.000000e+00  11020s
 1136551    5.1635781e+08   5.094405e+05   0.000000e+00  11025s
 1137157    5.1632724e+08   5.223141e+05   0.000000e+00  11030s
 1137763    5.1629237e+08   5.340458e+05   0.000000e+00  11036s
 1138369    5.1624381e+08   5.344965e+05   0.000000e+00  11041s
 1138975    5.1620506e+08   5.291955e+05   0.000000e+00  11045s
 1139581    5.1614886e+08   5.226289e+05   0.000000e+00  11050s
 1140187    5.1611384e+08   5.282016e+05   0.000000e+00  11055s
 1140894    5.1606012e+08   5.343746e+05   0.000000e+00  11061s
 1141500    5.1601398e+08   5.523392e+05   0.000000e+00  11066s
 1142106    5.1596156e+08   6.336714e+05   0.000000e+00  11071s
 1142712    5.1592682e+08   6.401887e+05   0.000000e+00  11075s
 1143318    5.1588288e+08   6.629796e+05   0.000000e+00  11080s
 1143924    5.1584599e+08   6.816720e+05   0.000000e+00  11085s
 1144530    5.1581101e+08   6.966688e+05   0.000000e+00  11091s
 1145136    5.1578598e+08   5.336275e+05   0.000000e+00  11096s
 1145742    5.1576822e+08   5.024050e+05   0.000000e+00  11100s
 1146348    5.1575200e+08   5.061470e+05   0.000000e+00  11105s
 1147055    5.1572347e+08   5.219139e+05   0.000000e+00  11111s
 1147661    5.1569384e+08   5.364186e+05   0.000000e+00  11116s
 1148166    5.1566125e+08   5.241132e+05   0.000000e+00  11120s
 1148772    5.1562428e+08   5.731543e+05   0.000000e+00  11126s
 1149277    5.1560131e+08   5.380772e+05   0.000000e+00  11130s
 1149883    5.1556472e+08   5.549151e+05   0.000000e+00  11136s
 1150388    5.1553245e+08   5.756746e+05   0.000000e+00  11140s
 1150994    5.1549493e+08   5.782214e+05   0.000000e+00  11145s
 1151701    5.1545829e+08   5.606448e+05   0.000000e+00  11151s
 1152307    5.1542731e+08   5.699142e+05   0.000000e+00  11155s
 1152913    5.1539504e+08   5.853864e+05   0.000000e+00  11160s
 1153620    5.1534679e+08   5.832849e+05   0.000000e+00  11166s
 1154125    5.1530141e+08   5.557870e+05   0.000000e+00  11170s
 1154731    5.1520375e+08   5.666246e+05   0.000000e+00  11176s
 1155337    5.1517320e+08   5.467273e+05   0.000000e+00  11181s
 1155943    5.1510073e+08   5.504365e+05   0.000000e+00  11185s
 1156549    5.1504743e+08   4.649396e+05   0.000000e+00  11190s
 1157256    5.1502488e+08   4.689806e+05   0.000000e+00  11196s
 1157862    5.1500280e+08   5.070416e+05   0.000000e+00  11201s
 1158468    5.1498187e+08   4.882876e+05   0.000000e+00  11206s
 1159074    5.1496004e+08   5.105118e+05   0.000000e+00  11210s
 1159781    5.1493837e+08   4.301299e+05   0.000000e+00  11216s
 1160286    5.1492234e+08   4.448545e+05   0.000000e+00  11220s
 1160993    5.1488521e+08   4.652435e+05   0.000000e+00  11226s
 1161599    5.1485968e+08   4.558498e+05   0.000000e+00  11231s
 1162104    5.1483676e+08   4.534923e+05   0.000000e+00  11235s
 1162710    5.1479522e+08   4.682089e+05   0.000000e+00  11240s
 1163316    5.1476513e+08   4.621063e+05   0.000000e+00  11245s
 1163922    5.1473940e+08   4.672744e+05   0.000000e+00  11250s
 1164528    5.1470758e+08   4.781772e+05   0.000000e+00  11255s
 1165235    5.1466448e+08   4.840429e+05   0.000000e+00  11261s
 1165841    5.1455381e+08   5.570234e+05   0.000000e+00  11266s
 1166346    5.1447352e+08   5.241453e+05   0.000000e+00  11270s
 1166952    5.1444121e+08   5.284483e+05   0.000000e+00  11275s
 1167659    5.1439236e+08   5.276713e+05   0.000000e+00  11281s
 1168265    5.1435016e+08   5.311576e+05   0.000000e+00  11285s
 1168871    5.1431096e+08   5.331299e+05   0.000000e+00  11291s
 1169376    5.1427601e+08   5.406012e+05   0.000000e+00  11295s
 1169982    5.1423890e+08   5.350063e+05   0.000000e+00  11300s
 1170487    5.1420447e+08   4.766123e+05   0.000000e+00  11305s
 1171093    5.1416989e+08   4.511799e+05   0.000000e+00  11310s
 1171800    5.1414248e+08   4.357369e+05   0.000000e+00  11316s
 1172406    5.1411672e+08   4.232595e+05   0.000000e+00  11321s
 1173012    5.1409234e+08   4.454768e+05   0.000000e+00  11325s
 1173618    5.1406509e+08   4.364225e+05   0.000000e+00  11331s
 1174123    5.1404123e+08   4.364179e+05   0.000000e+00  11335s
 1174830    5.1400634e+08   4.513179e+05   0.000000e+00  11341s
 1175436    5.1397503e+08   4.711579e+05   0.000000e+00  11346s
 1176042    5.1391159e+08   4.824737e+05   0.000000e+00  11350s
 1176648    5.1387764e+08   5.345352e+05   0.000000e+00  11355s
 1177254    5.1385158e+08   4.869650e+05   0.000000e+00  11360s
 1177860    5.1382335e+08   4.003659e+05   0.000000e+00  11365s
 1178466    5.1380038e+08   3.995568e+05   0.000000e+00  11370s
 1179072    5.1377638e+08   4.550259e+05   0.000000e+00  11375s
 1179678    5.1373813e+08   4.817538e+05   0.000000e+00  11380s
 1180284    5.1369288e+08   4.733900e+05   0.000000e+00  11385s
 1180991    5.1358725e+08   4.586098e+05   0.000000e+00  11391s
 1181496    5.1353485e+08   4.871510e+05   0.000000e+00  11395s
 1182102    5.1349419e+08   5.056545e+05   0.000000e+00  11400s
 1182708    5.1344227e+08   5.525215e+05   0.000000e+00  11405s
 1183314    5.1339987e+08   5.628001e+05   0.000000e+00  11411s
 1183819    5.1336602e+08   6.026932e+05   0.000000e+00  11415s
 1184425    5.1333541e+08   5.950270e+05   0.000000e+00  11421s
 1184930    5.1331037e+08   6.063266e+05   0.000000e+00  11426s
 1185536    5.1328255e+08   6.002805e+05   0.000000e+00  11431s
 1186041    5.1325752e+08   6.011123e+05   0.000000e+00  11435s
 1186647    5.1323002e+08   5.969599e+05   0.000000e+00  11440s
 1187253    5.1317071e+08   5.948844e+05   0.000000e+00  11446s
 1187859    5.1312822e+08   5.816906e+05   0.000000e+00  11451s
 1188465    5.1310292e+08   5.757503e+05   0.000000e+00  11455s
 1189071    5.1308638e+08   4.025772e+05   0.000000e+00  11460s
 1189677    5.1307231e+08   4.029842e+05   0.000000e+00  11466s
 1190283    5.1304643e+08   4.035944e+05   0.000000e+00  11471s
 1190889    5.1302150e+08   4.281020e+05   0.000000e+00  11476s
 1191495    5.1299587e+08   4.283585e+05   0.000000e+00  11481s
 1192000    5.1297545e+08   4.206032e+05   0.000000e+00  11485s
 1192606    5.1293738e+08   4.201908e+05   0.000000e+00  11491s
 1193212    5.1291169e+08   4.310361e+05   0.000000e+00  11496s
 1193818    5.1288369e+08   4.164594e+05   0.000000e+00  11501s
 1194323    5.1285071e+08   4.508958e+05   0.000000e+00  11505s
 1194929    5.1281289e+08   4.712631e+05   0.000000e+00  11511s
 1195535    5.1278888e+08   4.636629e+05   0.000000e+00  11516s
 1196141    5.1275385e+08   5.827499e+05   0.000000e+00  11520s
 1196747    5.1272815e+08   6.131442e+05   0.000000e+00  11525s
 1197454    5.1268459e+08   6.324401e+05   0.000000e+00  11531s
 1198060    5.1265048e+08   6.505792e+05   0.000000e+00  11535s
 1198666    5.1262557e+08   5.135301e+05   0.000000e+00  11540s
 1199373    5.1257663e+08   5.064443e+05   0.000000e+00  11546s
 1199979    5.1255394e+08   4.145730e+05   0.000000e+00  11550s
 1200686    5.1252990e+08   4.354216e+05   0.000000e+00  11556s
 1201292    5.1250834e+08   3.993308e+05   0.000000e+00  11560s
 1201898    5.1249104e+08   4.114297e+05   0.000000e+00  11565s
 1202605    5.1241641e+08   4.157461e+05   0.000000e+00  11570s
 1203211    5.1238008e+08   4.219815e+05   0.000000e+00  11575s
 1203817    5.1234028e+08   4.262130e+05   0.000000e+00  11581s
 1204423    5.1232018e+08   4.122702e+05   0.000000e+00  11585s
 1205029    5.1229561e+08   4.170872e+05   0.000000e+00  11590s
 1205736    5.1226254e+08   4.381961e+05   0.000000e+00  11596s
 1206342    5.1222416e+08   4.685437e+05   0.000000e+00  11601s
 1206847    5.1220720e+08   4.354327e+05   0.000000e+00  11605s
 1207453    5.1217093e+08   4.707248e+05   0.000000e+00  11611s
 1207958    5.1213296e+08   4.745241e+05   0.000000e+00  11615s
 1208564    5.1210214e+08   4.942310e+05   0.000000e+00  11621s
 1209170    5.1207622e+08   5.169818e+05   0.000000e+00  11626s
 1209776    5.1205523e+08   5.326246e+05   0.000000e+00  11631s
 1210382    5.1202173e+08   5.325557e+05   0.000000e+00  11635s
 1211089    5.1198914e+08   5.301859e+05   0.000000e+00  11641s
 1211695    5.1197205e+08   4.272448e+05   0.000000e+00  11645s
 1212301    5.1195467e+08   4.206674e+05   0.000000e+00  11650s
 1212907    5.1193793e+08   4.014128e+05   0.000000e+00  11656s
 1213513    5.1191577e+08   3.976932e+05   0.000000e+00  11661s
 1214119    5.1189450e+08   4.196322e+05   0.000000e+00  11666s
 1214725    5.1187820e+08   4.182274e+05   0.000000e+00  11670s
 1215331    5.1185597e+08   4.215813e+05   0.000000e+00  11675s
 1215937    5.1182845e+08   4.193201e+05   0.000000e+00  11680s
 1216644    5.1178213e+08   4.410434e+05   0.000000e+00  11686s
 1217250    5.1174612e+08   4.576387e+05   0.000000e+00  11690s
 1217957    5.1172425e+08   4.435786e+05   0.000000e+00  11696s
 1218563    5.1170091e+08   4.681053e+05   0.000000e+00  11700s
 1219270    5.1164866e+08   4.772323e+05   0.000000e+00  11706s
 1219876    5.1158323e+08   4.778359e+05   0.000000e+00  11710s
 1220583    5.1152591e+08   4.658014e+05   0.000000e+00  11716s
 1221189    5.1149542e+08   4.878036e+05   0.000000e+00  11720s
 1221795    5.1147373e+08   4.996920e+05   0.000000e+00  11726s
 1222300    5.1145629e+08   5.000232e+05   0.000000e+00  11730s
 1222906    5.1144179e+08   3.311064e+05   0.000000e+00  11735s
 1223512    5.1142739e+08   3.343251e+05   0.000000e+00  11741s
 1224017    5.1141090e+08   3.374926e+05   0.000000e+00  11745s
 1224724    5.1139107e+08   3.563426e+05   0.000000e+00  11751s
 1225229    5.1137256e+08   3.453798e+05   0.000000e+00  11755s
 1225835    5.1135085e+08   3.536881e+05   0.000000e+00  11761s
 1226441    5.1132436e+08   3.743047e+05   0.000000e+00  11766s
 1226946    5.1130928e+08   3.688511e+05   0.000000e+00  11770s
 1227552    5.1128167e+08   4.004359e+05   0.000000e+00  11775s
 1228259    5.1124355e+08   3.967991e+05   0.000000e+00  11781s
 1228865    5.1122082e+08   3.822562e+05   0.000000e+00  11785s
 1229471    5.1119741e+08   3.893401e+05   0.000000e+00  11791s
 1230077    5.1117575e+08   3.973024e+05   0.000000e+00  11796s
 1230582    5.1115104e+08   4.650415e+05   0.000000e+00  11800s
 1231289    5.1106538e+08   4.665318e+05   0.000000e+00  11805s
 1231895    5.1100647e+08   4.751347e+05   0.000000e+00  11810s
 1232602    5.1098459e+08   4.794622e+05   0.000000e+00  11816s
 1233208    5.1096350e+08   4.704426e+05   0.000000e+00  11820s
 1233713    5.1093495e+08   4.561363e+05   0.000000e+00  11825s
 1234319    5.1091742e+08   3.164800e+05   0.000000e+00  11830s
 1234925    5.1090205e+08   3.063586e+05   0.000000e+00  11836s
 1235430    5.1088687e+08   3.087137e+05   0.000000e+00  11840s
 1236036    5.1086895e+08   3.133034e+05   0.000000e+00  11845s
 1236743    5.1084665e+08   3.367938e+05   0.000000e+00  11851s
 1237349    5.1082868e+08   3.437745e+05   0.000000e+00  11856s
 1237955    5.1080755e+08   3.582492e+05   0.000000e+00  11860s
 1238561    5.1077956e+08   3.556751e+05   0.000000e+00  11866s
 1239167    5.1075469e+08   3.536436e+05   0.000000e+00  11870s
 1239773    5.1073515e+08   3.978300e+05   0.000000e+00  11875s
 1240379    5.1071358e+08   3.915419e+05   0.000000e+00  11880s
 1240985    5.1067833e+08   3.913174e+05   0.000000e+00  11885s
 1241692    5.1065199e+08   3.890935e+05   0.000000e+00  11891s
 1242298    5.1062717e+08   3.941923e+05   0.000000e+00  11896s
 1242904    5.1060481e+08   4.079685e+05   0.000000e+00  11900s
 1243510    5.1057210e+08   4.134081e+05   0.000000e+00  11905s
 1244116    5.1054964e+08   4.229712e+05   0.000000e+00  11910s
 1244722    5.1048872e+08   4.263054e+05   0.000000e+00  11915s
 1245328    5.1047310e+08   2.986980e+05   0.000000e+00  11920s
 1246035    5.1045046e+08   3.147839e+05   0.000000e+00  11926s
 1246641    5.1043190e+08   3.093225e+05   0.000000e+00  11931s
 1247247    5.1041335e+08   3.184689e+05   0.000000e+00  11936s
 1247853    5.1039637e+08   3.237267e+05   0.000000e+00  11940s
 1248560    5.1036496e+08   3.195113e+05   0.000000e+00  11946s
 1249166    5.1034773e+08   3.342845e+05   0.000000e+00  11950s
 1249873    5.1032471e+08   3.331282e+05   0.000000e+00  11956s
 1250479    5.1030465e+08   3.422620e+05   0.000000e+00  11960s
 1251085    5.1028460e+08   3.385731e+05   0.000000e+00  11965s
 1251691    5.1024922e+08   3.521260e+05   0.000000e+00  11970s
 1252196    5.1023459e+08   2.917802e+05   0.000000e+00  11975s
 1252802    5.1021815e+08   3.022511e+05   0.000000e+00  11980s
 1253408    5.1019827e+08   2.974411e+05   0.000000e+00  11985s
 1254014    5.1018529e+08   2.678877e+05   0.000000e+00  11990s
 1254620    5.1017057e+08   2.620066e+05   0.000000e+00  11996s
 1255125    5.1015685e+08   2.660289e+05   0.000000e+00  12000s
 1255731    5.1013674e+08   2.784087e+05   0.000000e+00  12005s
 1256438    5.1011417e+08   2.758661e+05   0.000000e+00  12011s
 1257044    5.1009855e+08   2.772405e+05   0.000000e+00  12016s
 1257650    5.1007416e+08   3.265850e+05   0.000000e+00  12020s
 1258256    5.1005510e+08   3.073958e+05   0.000000e+00  12025s
 1258862    5.1003691e+08   3.411388e+05   0.000000e+00  12030s
 1259569    5.1000082e+08   3.402550e+05   0.000000e+00  12036s
 1260175    5.0998293e+08   3.202913e+05   0.000000e+00  12040s
 1260781    5.0996367e+08   3.231250e+05   0.000000e+00  12046s
 1261286    5.0994213e+08   3.312584e+05   0.000000e+00  12050s
 1261892    5.0991656e+08   3.290476e+05   0.000000e+00  12055s
 1262498    5.0989192e+08   3.488064e+05   0.000000e+00  12060s
 1263104    5.0987272e+08   3.430843e+05   0.000000e+00  12066s
 1263609    5.0985641e+08   3.377486e+05   0.000000e+00  12071s
 1264215    5.0983031e+08   3.727130e+05   0.000000e+00  12076s
 1264720    5.0981192e+08   3.767903e+05   0.000000e+00  12080s
 1265326    5.0978482e+08   3.790764e+05   0.000000e+00  12086s
 1265932    5.0976016e+08   4.029649e+05   0.000000e+00  12091s
 1266437    5.0974708e+08   2.846010e+05   0.000000e+00  12096s
 1266942    5.0973264e+08   2.793630e+05   0.000000e+00  12100s
 1267548    5.0971570e+08   2.764826e+05   0.000000e+00  12105s
 1268154    5.0970134e+08   2.744037e+05   0.000000e+00  12111s
 1268760    5.0967187e+08   2.667700e+05   0.000000e+00  12115s
 1269366    5.0965341e+08   2.551901e+05   0.000000e+00  12120s
 1269972    5.0963584e+08   2.669900e+05   0.000000e+00  12126s
 1270477    5.0962269e+08   2.601921e+05   0.000000e+00  12130s
 1270982    5.0960838e+08   2.780149e+05   0.000000e+00  12135s
 1271689    5.0957735e+08   2.823615e+05   0.000000e+00  12141s
 1272295    5.0955671e+08   2.928382e+05   0.000000e+00  12146s
 1272901    5.0953040e+08   2.957420e+05   0.000000e+00  12151s
 1273406    5.0948879e+08   3.109376e+05   0.000000e+00  12155s
 1274012    5.0946058e+08   3.042562e+05   0.000000e+00  12160s
 1274618    5.0943211e+08   3.157740e+05   0.000000e+00  12165s
 1275224    5.0940276e+08   3.076839e+05   0.000000e+00  12170s
 1275830    5.0937315e+08   3.075997e+05   0.000000e+00  12175s
 1276436    5.0935064e+08   3.104709e+05   0.000000e+00  12181s
 1277042    5.0931658e+08   3.356177e+05   0.000000e+00  12186s
 1277648    5.0927858e+08   2.528085e+05   0.000000e+00  12190s
 1278254    5.0926417e+08   2.355296e+05   0.000000e+00  12195s
 1278860    5.0924530e+08   2.378389e+05   0.000000e+00  12200s
 1279466    5.0921949e+08   2.506783e+05   0.000000e+00  12205s
 1280072    5.0920565e+08   2.506953e+05   0.000000e+00  12210s
 1280779    5.0918038e+08   2.735570e+05   0.000000e+00  12216s
 1281385    5.0915385e+08   2.510962e+05   0.000000e+00  12220s
 1281991    5.0911950e+08   2.941587e+05   0.000000e+00  12225s
 1282597    5.0906193e+08   2.997482e+05   0.000000e+00  12231s
 1283203    5.0901918e+08   3.112626e+05   0.000000e+00  12236s
 1283809    5.0899722e+08   3.392175e+05   0.000000e+00  12241s
 1284314    5.0898159e+08   3.440901e+05   0.000000e+00  12245s
 1284920    5.0896779e+08   3.504007e+05   0.000000e+00  12251s
 1285425    5.0895644e+08   2.163823e+05   0.000000e+00  12255s
 1286031    5.0893686e+08   2.147652e+05   0.000000e+00  12260s
 1286738    5.0890971e+08   2.335583e+05   0.000000e+00  12266s
 1287344    5.0887234e+08   2.419838e+05   0.000000e+00  12270s
 1288051    5.0885237e+08   2.507547e+05   0.000000e+00  12276s
 1288657    5.0883332e+08   2.615977e+05   0.000000e+00  12281s
 1289162    5.0881714e+08   2.536221e+05   0.000000e+00  12285s
 1289768    5.0879920e+08   2.612729e+05   0.000000e+00  12290s
 1290374    5.0877974e+08   2.753676e+05   0.000000e+00  12295s
 1291081    5.0875540e+08   2.744665e+05   0.000000e+00  12301s
 1291687    5.0873381e+08   2.732005e+05   0.000000e+00  12306s
 1292192    5.0871881e+08   2.750085e+05   0.000000e+00  12310s
 1292798    5.0870255e+08   2.781189e+05   0.000000e+00  12315s
 1293505    5.0867925e+08   2.953000e+05   0.000000e+00  12321s
 1294111    5.0866182e+08   2.942438e+05   0.000000e+00  12326s
 1294717    5.0864567e+08   2.823699e+05   0.000000e+00  12330s
 1295323    5.0862998e+08   2.745775e+05   0.000000e+00  12335s
 1296030    5.0861078e+08   2.804530e+05   0.000000e+00  12341s
 1296636    5.0859971e+08   2.238368e+05   0.000000e+00  12346s
 1297242    5.0858603e+08   2.242539e+05   0.000000e+00  12350s
 1297949    5.0856685e+08   2.193766e+05   0.000000e+00  12356s
 1298555    5.0855161e+08   2.256471e+05   0.000000e+00  12360s
 1299161    5.0853099e+08   2.307239e+05   0.000000e+00  12365s
 1299868    5.0851273e+08   2.333327e+05   0.000000e+00  12371s
 1300474    5.0849412e+08   2.416103e+05   0.000000e+00  12375s
 1301080    5.0847921e+08   2.342737e+05   0.000000e+00  12380s
 1301787    5.0845561e+08   2.291451e+05   0.000000e+00  12386s
 1302393    5.0843767e+08   2.496514e+05   0.000000e+00  12390s
 1303100    5.0842031e+08   2.765266e+05   0.000000e+00  12396s
 1303706    5.0840297e+08   2.773384e+05   0.000000e+00  12400s
 1304312    5.0838073e+08   2.896102e+05   0.000000e+00  12405s
 1304918    5.0836275e+08   2.845285e+05   0.000000e+00  12410s
 1305625    5.0834414e+08   3.004671e+05   0.000000e+00  12416s
 1306231    5.0832250e+08   2.937592e+05   0.000000e+00  12421s
 1306837    5.0830751e+08   3.011643e+05   0.000000e+00  12426s
 1307342    5.0829184e+08   3.044192e+05   0.000000e+00  12430s
 1307948    5.0828127e+08   2.118060e+05   0.000000e+00  12435s
 1308655    5.0826560e+08   2.125697e+05   0.000000e+00  12441s
 1309261    5.0825414e+08   1.926976e+05   0.000000e+00  12445s
 1309867    5.0823597e+08   2.036590e+05   0.000000e+00  12450s
 1310574    5.0822306e+08   2.225693e+05   0.000000e+00  12456s
 1311180    5.0820975e+08   2.119209e+05   0.000000e+00  12460s
 1311786    5.0819193e+08   2.219409e+05   0.000000e+00  12465s
 1312392    5.0817748e+08   2.226263e+05   0.000000e+00  12470s
 1313099    5.0815258e+08   2.280991e+05   0.000000e+00  12476s
 1313705    5.0813176e+08   2.357647e+05   0.000000e+00  12480s
 1314311    5.0811610e+08   2.344663e+05   0.000000e+00  12486s
 1314917    5.0810129e+08   2.334016e+05   0.000000e+00  12491s
 1315422    5.0808820e+08   2.632868e+05   0.000000e+00  12495s
 1316028    5.0806724e+08   2.644440e+05   0.000000e+00  12500s
 1316735    5.0804287e+08   2.715257e+05   0.000000e+00  12505s
 1317341    5.0802687e+08   2.942464e+05   0.000000e+00  12511s
 1317947    5.0801064e+08   2.840323e+05   0.000000e+00  12516s
 1318553    5.0799147e+08   3.141689e+05   0.000000e+00  12520s
 1319260    5.0797466e+08   2.190150e+05   0.000000e+00  12526s
 1319866    5.0796331e+08   1.939496e+05   0.000000e+00  12530s
 1320472    5.0795111e+08   2.127851e+05   0.000000e+00  12536s
 1320977    5.0793932e+08   2.145571e+05   0.000000e+00  12540s
 1321684    5.0792297e+08   2.292000e+05   0.000000e+00  12546s
 1322290    5.0791045e+08   1.989418e+05   0.000000e+00  12550s
 1322997    5.0789757e+08   2.265962e+05   0.000000e+00  12556s
 1323603    5.0788404e+08   2.347327e+05   0.000000e+00  12561s
 1324209    5.0787235e+08   2.045024e+05   0.000000e+00  12565s
 1324916    5.0785542e+08   2.068289e+05   0.000000e+00  12571s
 1325421    5.0784342e+08   2.145172e+05   0.000000e+00  12575s
 1326027    5.0782636e+08   2.655521e+05   0.000000e+00  12581s
 1326532    5.0781092e+08   2.771563e+05   0.000000e+00  12585s
 1327239    5.0779295e+08   3.119470e+05   0.000000e+00  12591s
 1327744    5.0777836e+08   2.423158e+05   0.000000e+00  12595s
 1328451    5.0776412e+08   2.468940e+05   0.000000e+00  12601s
 1329057    5.0775033e+08   2.793228e+05   0.000000e+00  12606s
 1329663    5.0773138e+08   2.798941e+05   0.000000e+00  12610s
 1330269    5.0771747e+08   1.916596e+05   0.000000e+00  12616s
 1330774    5.0770792e+08   1.706327e+05   0.000000e+00  12620s
 1331380    5.0769747e+08   1.837513e+05   0.000000e+00  12625s
 1331986    5.0768759e+08   1.763250e+05   0.000000e+00  12631s
 1332592    5.0767714e+08   1.923648e+05   0.000000e+00  12636s
 1333097    5.0766776e+08   1.858890e+05   0.000000e+00  12640s
 1333703    5.0765449e+08   1.952468e+05   0.000000e+00  12645s
 1334410    5.0763033e+08   1.998994e+05   0.000000e+00  12651s
 1335016    5.0761817e+08   2.089059e+05   0.000000e+00  12655s
 1335622    5.0760230e+08   2.270324e+05   0.000000e+00  12660s
 1336228    5.0758983e+08   2.274321e+05   0.000000e+00  12666s
 1336834    5.0757627e+08   2.289451e+05   0.000000e+00  12671s
 1337339    5.0756402e+08   2.187672e+05   0.000000e+00  12675s
 1338046    5.0755064e+08   2.311485e+05   0.000000e+00  12681s
 1338652    5.0753613e+08   2.345619e+05   0.000000e+00  12685s
 1339258    5.0751453e+08   2.377753e+05   0.000000e+00  12690s
 1339965    5.0748923e+08   2.774868e+05   0.000000e+00  12696s
 1340470    5.0745273e+08   2.496577e+05   0.000000e+00  12700s
 1341076    5.0743458e+08   2.484151e+05   0.000000e+00  12705s
 1341783    5.0741882e+08   1.806427e+05   0.000000e+00  12711s
 1342389    5.0740386e+08   1.672375e+05   0.000000e+00  12715s
 1342995    5.0739198e+08   1.599918e+05   0.000000e+00  12720s
 1343601    5.0737759e+08   1.646362e+05   0.000000e+00  12725s
 1344308    5.0736641e+08   1.641098e+05   0.000000e+00  12731s
 1344914    5.0735225e+08   1.657269e+05   0.000000e+00  12736s
 1345419    5.0734276e+08   1.706528e+05   0.000000e+00  12741s
 1345924    5.0732755e+08   1.656757e+05   0.000000e+00  12745s
 1346530    5.0731603e+08   1.728094e+05   0.000000e+00  12750s
 1347136    5.0729999e+08   1.774378e+05   0.000000e+00  12756s
 1347641    5.0729125e+08   1.731487e+05   0.000000e+00  12761s
 1348146    5.0728258e+08   1.844714e+05   0.000000e+00  12765s
 1348752    5.0726971e+08   1.873915e+05   0.000000e+00  12770s
 1349358    5.0725459e+08   1.861150e+05   0.000000e+00  12775s
 1350065    5.0724068e+08   1.866025e+05   0.000000e+00  12781s
 1350671    5.0722709e+08   1.867265e+05   0.000000e+00  12786s
 1351277    5.0720837e+08   1.967535e+05   0.000000e+00  12791s
 1351782    5.0719560e+08   1.928747e+05   0.000000e+00  12795s
 1352287    5.0718632e+08   1.933449e+05   0.000000e+00  12800s
 1352893    5.0717412e+08   1.619721e+05   0.000000e+00  12806s
 1353398    5.0716785e+08   1.345082e+05   0.000000e+00  12810s
 1354004    5.0716103e+08   1.423225e+05   0.000000e+00  12815s
 1354610    5.0714875e+08   1.553638e+05   0.000000e+00  12821s
 1355115    5.0714060e+08   1.480700e+05   0.000000e+00  12825s
 1355721    5.0712902e+08   1.514637e+05   0.000000e+00  12831s
 1356327    5.0711945e+08   1.621379e+05   0.000000e+00  12835s
 1356933    5.0710795e+08   1.609546e+05   0.000000e+00  12840s
 1357640    5.0708975e+08   1.592611e+05   0.000000e+00  12845s
 1358246    5.0707217e+08   1.620937e+05   0.000000e+00  12850s
 1358852    5.0705577e+08   1.682637e+05   0.000000e+00  12855s
 1359458    5.0704331e+08   1.768967e+05   0.000000e+00  12860s
 1360064    5.0702889e+08   1.840262e+05   0.000000e+00  12866s
 1360569    5.0701725e+08   1.790420e+05   0.000000e+00  12870s
 1361175    5.0700462e+08   1.843217e+05   0.000000e+00  12875s
 1361781    5.0699244e+08   1.929347e+05   0.000000e+00  12880s
 1362488    5.0698032e+08   2.090265e+05   0.000000e+00  12886s
 1363094    5.0696704e+08   2.081990e+05   0.000000e+00  12891s
 1363700    5.0695474e+08   2.114933e+05   0.000000e+00  12895s
 1364306    5.0694282e+08   1.504088e+05   0.000000e+00  12900s
 1364912    5.0693239e+08   1.286431e+05   0.000000e+00  12905s
 1365518    5.0692440e+08   1.222726e+05   0.000000e+00  12910s
 1366124    5.0691584e+08   1.205407e+05   0.000000e+00  12915s
 1366831    5.0690295e+08   1.274922e+05   0.000000e+00  12921s
 1367437    5.0688971e+08   1.277856e+05   0.000000e+00  12926s
 1368043    5.0688116e+08   1.379931e+05   0.000000e+00  12931s
 1368548    5.0686622e+08   1.310288e+05   0.000000e+00  12935s
 1369053    5.0685471e+08   1.385924e+05   0.000000e+00  12940s
 1369659    5.0684713e+08   1.450555e+05   0.000000e+00  12945s
 1370265    5.0683445e+08   1.583450e+05   0.000000e+00  12950s
 1370871    5.0682205e+08   1.617636e+05   0.000000e+00  12956s
 1371477    5.0680885e+08   1.608696e+05   0.000000e+00  12961s
 1372083    5.0679457e+08   1.398073e+05   0.000000e+00  12965s
 1372689    5.0678012e+08   1.508608e+05   0.000000e+00  12970s
 1373396    5.0676774e+08   1.729700e+05   0.000000e+00  12976s
 1374002    5.0675666e+08   1.689172e+05   0.000000e+00  12980s
 1374608    5.0674588e+08   1.702702e+05   0.000000e+00  12985s
 1375214    5.0673591e+08   1.723687e+05   0.000000e+00  12990s
 1375820    5.0672858e+08   1.353370e+05   0.000000e+00  12995s
 1376527    5.0671611e+08   1.206864e+05   0.000000e+00  13001s
 1377133    5.0670663e+08   1.178438e+05   0.000000e+00  13006s
 1377739    5.0669480e+08   1.169630e+05   0.000000e+00  13011s
 1378345    5.0668398e+08   1.195328e+05   0.000000e+00  13015s
 1378951    5.0667429e+08   1.718628e+05   0.000000e+00  13020s
 1379658    5.0666081e+08   2.017184e+05   0.000000e+00  13026s
 1380163    5.0665432e+08   1.419155e+05   0.000000e+00  13030s
 1380769    5.0663990e+08   1.191943e+05   0.000000e+00  13035s
 1381375    5.0663189e+08   1.311418e+05   0.000000e+00  13041s
 1381981    5.0662229e+08   1.163163e+05   0.000000e+00  13046s
 1382587    5.0661282e+08   1.053063e+05   0.000000e+00  13050s
 1383193    5.0660561e+08   9.559186e+04   0.000000e+00  13055s
 1383799    5.0659456e+08   1.186382e+05   0.000000e+00  13060s
 1384506    5.0658327e+08   1.139298e+05   0.000000e+00  13066s
 1385112    5.0657339e+08   1.082058e+05   0.000000e+00  13071s
 1385617    5.0656443e+08   1.284749e+05   0.000000e+00  13075s
 1386223    5.0655541e+08   1.462757e+05   0.000000e+00  13080s
 1386930    5.0653961e+08   1.535717e+05   0.000000e+00  13085s
 1387536    5.0652806e+08   1.507871e+05   0.000000e+00  13090s
 1388243    5.0651343e+08   1.553003e+05   0.000000e+00  13095s
 1388849    5.0650041e+08   1.659550e+05   0.000000e+00  13100s
 1389556    5.0649153e+08   1.732285e+05   0.000000e+00  13106s
 1390162    5.0648273e+08   1.838776e+05   0.000000e+00  13110s
 1390768    5.0647166e+08   1.877142e+05   0.000000e+00  13116s
 1391374    5.0645588e+08   1.773850e+05   0.000000e+00  13121s
 1391980    5.0644402e+08   1.745533e+05   0.000000e+00  13126s
 1392485    5.0643394e+08   1.790978e+05   0.000000e+00  13130s
 1393091    5.0642148e+08   1.742710e+05   0.000000e+00  13136s
 1393596    5.0641328e+08   1.598515e+05   0.000000e+00  13141s
 1394202    5.0640711e+08   1.196340e+05   0.000000e+00  13145s
 1394808    5.0640110e+08   1.083449e+05   0.000000e+00  13150s
 1395515    5.0639093e+08   1.361557e+05   0.000000e+00  13156s
 1396121    5.0638386e+08   1.486674e+05   0.000000e+00  13161s
 1396626    5.0637497e+08   1.384574e+05   0.000000e+00  13165s
 1397232    5.0636696e+08   1.509600e+05   0.000000e+00  13171s
 1397737    5.0635894e+08   1.501858e+05   0.000000e+00  13175s
 1398343    5.0634906e+08   1.084660e+05   0.000000e+00  13181s
 1398848    5.0634239e+08   1.165204e+05   0.000000e+00  13186s
 1399454    5.0633492e+08   1.253997e+05   0.000000e+00  13191s
 1399959    5.0632870e+08   1.234242e+05   0.000000e+00  13195s
 1400565    5.0632119e+08   1.222263e+05   0.000000e+00  13200s
 1401070    5.0631433e+08   1.238022e+05   0.000000e+00  13205s
 1401676    5.0630285e+08   1.298093e+05   0.000000e+00  13210s
 1402383    5.0629125e+08   1.296138e+05   0.000000e+00  13215s
 1403090    5.0627883e+08   1.379686e+05   0.000000e+00  13221s
 1403696    5.0627091e+08   1.433650e+05   0.000000e+00  13225s
 1404302    5.0626390e+08   1.440007e+05   0.000000e+00  13230s
 1405009    5.0625416e+08   9.521899e+04   0.000000e+00  13236s
 1405615    5.0624769e+08   8.673610e+04   0.000000e+00  13240s
 1406221    5.0623727e+08   9.070994e+04   0.000000e+00  13245s
 1406827    5.0622965e+08   8.422334e+04   0.000000e+00  13250s
 1407433    5.0622215e+08   8.905037e+04   0.000000e+00  13256s
 1408039    5.0621012e+08   9.217571e+04   0.000000e+00  13261s
 1408645    5.0619967e+08   9.655341e+04   0.000000e+00  13266s
 1409251    5.0618762e+08   9.758706e+04   0.000000e+00  13271s
 1409857    5.0617918e+08   9.454738e+04   0.000000e+00  13276s
 1410463    5.0617093e+08   1.128129e+05   0.000000e+00  13281s
 1411069    5.0616272e+08   1.040806e+05   0.000000e+00  13285s
 1411776    5.0615333e+08   1.264493e+05   0.000000e+00  13291s
 1412281    5.0614401e+08   1.196425e+05   0.000000e+00  13295s
 1412887    5.0613450e+08   1.045419e+05   0.000000e+00  13300s
 1413493    5.0612731e+08   1.098574e+05   0.000000e+00  13305s
 1414099    5.0611966e+08   1.044985e+05   0.000000e+00  13310s
 1414806    5.0610960e+08   1.088287e+05   0.000000e+00  13316s
 1415412    5.0610233e+08   1.122726e+05   0.000000e+00  13321s
 1416018    5.0609678e+08   1.221131e+05   0.000000e+00  13325s
 1416725    5.0609104e+08   8.160448e+04   0.000000e+00  13331s
 1417331    5.0608594e+08   7.948741e+04   0.000000e+00  13336s
 1417937    5.0607904e+08   7.880539e+04   0.000000e+00  13340s
 1418543    5.0607286e+08   9.299607e+04   0.000000e+00  13345s
 1419250    5.0606626e+08   1.068860e+05   0.000000e+00  13350s
 1419856    5.0606146e+08   6.932412e+04   0.000000e+00  13355s
 1420462    5.0605634e+08   8.610054e+04   0.000000e+00  13360s
 1421169    5.0604771e+08   7.820598e+04   0.000000e+00  13365s
 1421775    5.0603882e+08   7.660204e+04   0.000000e+00  13370s
 1422482    5.0602784e+08   7.094912e+04   0.000000e+00  13375s
 1423189    5.0601876e+08   7.609836e+04   0.000000e+00  13381s
 1423795    5.0600961e+08   8.035113e+04   0.000000e+00  13386s
 1424401    5.0600197e+08   8.955795e+04   0.000000e+00  13391s
 1425007    5.0599505e+08   9.200089e+04   0.000000e+00  13395s
 1425613    5.0598746e+08   9.534584e+04   0.000000e+00  13400s
 1426219    5.0598074e+08   7.253925e+04   0.000000e+00  13405s
 1426825    5.0597411e+08   6.474131e+04   0.000000e+00  13411s
 1427330    5.0596871e+08   7.241633e+04   0.000000e+00  13415s
 1427936    5.0596053e+08   6.006555e+04   0.000000e+00  13421s
 1428441    5.0595429e+08   6.945487e+04   0.000000e+00  13425s
 1429047    5.0594426e+08   6.316653e+04   0.000000e+00  13430s
 1429653    5.0593781e+08   6.255109e+04   0.000000e+00  13435s
 1430259    5.0593172e+08   4.889898e+04   0.000000e+00  13441s
 1430865    5.0592718e+08   5.273735e+04   0.000000e+00  13446s
 1431471    5.0592032e+08   5.518612e+04   0.000000e+00  13451s
 1431976    5.0591418e+08   5.690984e+04   0.000000e+00  13456s
 1432582    5.0590736e+08   5.635789e+04   0.000000e+00  13460s
 1433188    5.0590007e+08   6.477710e+04   0.000000e+00  13465s
 1433895    5.0589179e+08   6.631998e+04   0.000000e+00  13471s
 1434501    5.0588517e+08   6.815786e+04   0.000000e+00  13475s
 1435107    5.0587780e+08   7.550841e+04   0.000000e+00  13481s
 1435713    5.0586213e+08   7.320379e+04   0.000000e+00  13485s
 1436218    5.0585570e+08   5.298341e+04   0.000000e+00  13490s
 1436824    5.0584896e+08   4.634968e+04   0.000000e+00  13496s
 1437430    5.0584239e+08   4.960698e+04   0.000000e+00  13501s
 1438036    5.0583593e+08   5.780522e+04   0.000000e+00  13505s
 1438642    5.0582996e+08   5.741382e+04   0.000000e+00  13510s
 1439248    5.0582393e+08   5.542011e+04   0.000000e+00  13515s
 1439955    5.0581507e+08   7.222604e+04   0.000000e+00  13521s
 1440561    5.0580873e+08   6.403978e+04   0.000000e+00  13525s
 1441167    5.0580277e+08   6.282414e+04   0.000000e+00  13530s
 1441874    5.0579643e+08   6.647780e+04   0.000000e+00  13536s
 1442480    5.0579046e+08   6.921845e+04   0.000000e+00  13541s
 1443086    5.0578183e+08   7.679941e+04   0.000000e+00  13545s
 1443793    5.0577435e+08   8.141520e+04   0.000000e+00  13551s
 1444399    5.0576809e+08   8.314240e+04   0.000000e+00  13556s
 1445005    5.0576269e+08   8.067709e+04   0.000000e+00  13560s
 1445611    5.0575726e+08   7.773342e+04   0.000000e+00  13565s
 1446318    5.0574865e+08   8.607933e+04   0.000000e+00  13571s
 1446924    5.0574387e+08   5.926447e+04   0.000000e+00  13575s
 1447530    5.0574112e+08   5.063812e+04   0.000000e+00  13580s
 1448136    5.0573637e+08   5.260517e+04   0.000000e+00  13585s
 1448843    5.0572977e+08   5.162458e+04   0.000000e+00  13591s
 1449449    5.0572342e+08   5.963513e+04   0.000000e+00  13595s
 1450156    5.0571662e+08   6.075783e+04   0.000000e+00  13601s
 1450762    5.0570832e+08   6.362851e+04   0.000000e+00  13605s
 1451469    5.0570176e+08   6.734949e+04   0.000000e+00  13611s
 1452075    5.0569579e+08   6.419922e+04   0.000000e+00  13616s
 1452681    5.0569047e+08   6.794006e+04   0.000000e+00  13620s
 1453287    5.0568399e+08   7.210106e+04   0.000000e+00  13625s
 1453994    5.0567842e+08   7.411840e+04   0.000000e+00  13630s
 1454600    5.0567112e+08   7.112230e+04   0.000000e+00  13635s
 1455307    5.0566407e+08   6.455932e+04   0.000000e+00  13641s
 1455913    5.0565843e+08   7.471298e+04   0.000000e+00  13645s
 1456620    5.0565490e+08   3.922201e+04   0.000000e+00  13651s
 1457125    5.0565160e+08   4.245336e+04   0.000000e+00  13656s
 1457630    5.0564813e+08   4.162990e+04   0.000000e+00  13661s
 1458135    5.0564389e+08   4.172238e+04   0.000000e+00  13665s
 1458741    5.0563786e+08   4.997554e+04   0.000000e+00  13671s
 1459246    5.0563424e+08   3.958967e+04   0.000000e+00  13675s
 1459852    5.0562897e+08   4.040065e+04   0.000000e+00  13680s
 1460458    5.0562306e+08   3.920432e+04   0.000000e+00  13686s
 1460963    5.0561953e+08   3.503188e+04   0.000000e+00  13690s
 1461569    5.0561417e+08   3.969438e+04   0.000000e+00  13696s
 1462074    5.0561160e+08   4.272602e+04   0.000000e+00  13700s
 1462680    5.0560673e+08   3.594437e+04   0.000000e+00  13705s
 1463286    5.0560335e+08   4.304075e+04   0.000000e+00  13711s
 1463791    5.0559955e+08   3.882648e+04   0.000000e+00  13715s
 1464397    5.0559539e+08   4.148464e+04   0.000000e+00  13720s
 1465003    5.0558909e+08   4.006043e+04   0.000000e+00  13725s
 1465609    5.0558506e+08   4.855334e+04   0.000000e+00  13730s
 1466114    5.0558261e+08   3.894255e+04   0.000000e+00  13735s
 1466720    5.0557758e+08   6.750346e+04   0.000000e+00  13740s
 1467326    5.0557205e+08   4.725536e+04   0.000000e+00  13745s
 1468033    5.0556519e+08   4.345364e+04   0.000000e+00  13751s
 1468639    5.0556107e+08   5.423904e+04   0.000000e+00  13755s
 1469245    5.0555633e+08   6.776086e+04   0.000000e+00  13760s
 1469952    5.0555139e+08   4.640824e+04   0.000000e+00  13766s
 1470558    5.0554768e+08   4.695287e+04   0.000000e+00  13770s
 1471265    5.0554458e+08   3.808002e+04   0.000000e+00  13776s
 1471871    5.0553991e+08   5.744035e+04   0.000000e+00  13781s
 1472275    5.0553766e+08   5.556354e+04   0.000000e+00  13785s
 1472881    5.0553458e+08   3.331927e+04   0.000000e+00  13791s
 1473386    5.0553128e+08   4.079616e+04   0.000000e+00  13795s
 1473992    5.0552476e+08   3.232443e+04   0.000000e+00  13801s
 1474497    5.0552151e+08   3.390361e+04   0.000000e+00  13805s
 1475002    5.0551787e+08   3.657911e+04   0.000000e+00  13810s
 1475709    5.0551404e+08   1.024794e+05   0.000000e+00  13816s
 1476214    5.0551108e+08   3.008428e+04   0.000000e+00  13820s
 1476820    5.0550777e+08   2.884862e+04   0.000000e+00  13825s
 1477426    5.0550366e+08   2.962599e+04   0.000000e+00  13831s
 1478032    5.0549705e+08   2.802197e+04   0.000000e+00  13836s
 1478537    5.0549360e+08   2.772650e+04   0.000000e+00  13840s
 1479143    5.0548708e+08   3.045306e+04   0.000000e+00  13845s
 1479749    5.0548362e+08   4.270660e+04   0.000000e+00  13850s
 1480355    5.0547668e+08   3.002294e+04   0.000000e+00  13856s
 1480961    5.0547273e+08   3.247194e+04   0.000000e+00  13860s
 1481567    5.0546935e+08   3.202910e+04   0.000000e+00  13865s
 1482173    5.0546413e+08   3.229756e+04   0.000000e+00  13870s
 1482779    5.0546078e+08   3.386855e+04   0.000000e+00  13875s
 1483486    5.0545593e+08   3.692211e+04   0.000000e+00  13881s
 1484092    5.0545187e+08   3.990968e+04   0.000000e+00  13885s
 1484799    5.0544729e+08   3.961549e+04   0.000000e+00  13891s
 1485405    5.0544505e+08   3.618602e+04   0.000000e+00  13895s
 1486112    5.0544223e+08   3.138811e+04   0.000000e+00  13901s
 1486718    5.0543889e+08   3.141779e+04   0.000000e+00  13906s
 1487324    5.0543379e+08   2.818228e+04   0.000000e+00  13910s
 1488031    5.0542998e+08   2.815389e+04   0.000000e+00  13916s
 1488637    5.0542664e+08   2.913808e+04   0.000000e+00  13920s
 1489344    5.0542199e+08   4.830899e+04   0.000000e+00  13926s
 1489950    5.0541916e+08   4.730974e+04   0.000000e+00  13930s
 1490657    5.0541612e+08   3.084698e+04   0.000000e+00  13936s
 1491263    5.0541452e+08   2.061019e+04   0.000000e+00  13940s
 1491869    5.0541231e+08   2.390561e+04   0.000000e+00  13945s
 1492576    5.0540970e+08   2.319046e+04   0.000000e+00  13951s
 1493182    5.0540707e+08   2.653054e+04   0.000000e+00  13956s
 1493788    5.0540450e+08   2.547457e+04   0.000000e+00  13960s
 1494394    5.0540174e+08   2.596121e+04   0.000000e+00  13965s
 1495101    5.0539919e+08   1.961409e+04   0.000000e+00  13971s
 1495707    5.0539716e+08   2.052997e+04   0.000000e+00  13976s
 1496313    5.0539487e+08   2.150914e+04   0.000000e+00  13980s
 1497020    5.0539137e+08   2.053149e+04   0.000000e+00  13986s
 1497626    5.0538755e+08   2.440233e+04   0.000000e+00  13990s
 1498333    5.0538435e+08   2.292392e+04   0.000000e+00  13996s
 1498939    5.0538178e+08   2.202703e+04   0.000000e+00  14000s
 1499545    5.0537887e+08   2.335653e+04   0.000000e+00  14005s
 1500151    5.0537674e+08   4.747158e+04   0.000000e+00  14010s
 1500757    5.0537394e+08   2.316254e+04   0.000000e+00  14015s
 1501363    5.0537208e+08   2.356496e+04   0.000000e+00  14020s
 1502070    5.0537015e+08   2.727947e+04   0.000000e+00  14026s
 1502676    5.0536831e+08   1.642528e+04   0.000000e+00  14030s
 1503282    5.0536697e+08   1.467226e+04   0.000000e+00  14035s
 1503989    5.0536432e+08   1.308929e+04   0.000000e+00  14041s
 1504595    5.0536269e+08   1.349101e+04   0.000000e+00  14045s
 1505302    5.0535970e+08   1.624434e+04   0.000000e+00  14051s
 1505908    5.0535728e+08   1.639441e+04   0.000000e+00  14055s
 1506615    5.0535462e+08   1.572712e+04   0.000000e+00  14061s
 1507221    5.0535155e+08   3.417489e+04   0.000000e+00  14065s
 1507928    5.0534788e+08   2.196866e+04   0.000000e+00  14071s
 1508534    5.0534578e+08   2.519353e+04   0.000000e+00  14075s
 1509140    5.0534392e+08   2.305256e+04   0.000000e+00  14080s
 1509847    5.0534157e+08   2.153676e+04   0.000000e+00  14086s
 1510453    5.0533982e+08   1.497270e+04   0.000000e+00  14090s
 1511160    5.0533734e+08   1.151656e+04   0.000000e+00  14096s
 1511766    5.0533530e+08   2.881799e+04   0.000000e+00  14100s
 1512473    5.0533318e+08   3.093160e+04   0.000000e+00  14106s
 1513079    5.0533152e+08   3.227758e+04   0.000000e+00  14110s
 1513786    5.0532965e+08   3.195381e+04   0.000000e+00  14116s
 1514392    5.0532786e+08   2.963655e+04   0.000000e+00  14121s
 1514998    5.0532606e+08   1.061327e+04   0.000000e+00  14125s
 1515705    5.0532441e+08   1.089135e+04   0.000000e+00  14131s
 1516311    5.0532279e+08   1.243237e+04   0.000000e+00  14136s
 1516917    5.0532122e+08   2.630062e+04   0.000000e+00  14140s
 1517624    5.0531834e+08   7.784897e+03   0.000000e+00  14146s
 1518230    5.0531592e+08   6.813816e+03   0.000000e+00  14150s
 1518937    5.0531410e+08   6.865690e+03   0.000000e+00  14156s
 1519543    5.0531303e+08   7.281377e+03   0.000000e+00  14160s
 1520149    5.0531158e+08   2.541087e+04   0.000000e+00  14165s
 1520856    5.0530981e+08   1.150259e+04   0.000000e+00  14171s
 1521462    5.0530865e+08   8.985024e+03   0.000000e+00  14176s
 1522068    5.0530722e+08   8.867152e+03   0.000000e+00  14180s
 1522775    5.0530605e+08   9.282994e+03   0.000000e+00  14186s
 1523381    5.0530421e+08   9.626238e+03   0.000000e+00  14190s
 1524088    5.0530276e+08   9.372584e+03   0.000000e+00  14196s
 1524694    5.0530162e+08   1.244543e+04   0.000000e+00  14200s
 1525300    5.0530039e+08   1.158946e+04   0.000000e+00  14205s
 1526007    5.0529924e+08   1.088076e+04   0.000000e+00  14211s
 1526613    5.0529804e+08   2.351530e+04   0.000000e+00  14215s
 1527219    5.0529624e+08   9.178713e+03   0.000000e+00  14220s
 1527926    5.0529465e+08   1.336232e+04   0.000000e+00  14226s
 1528532    5.0529268e+08   1.152122e+04   0.000000e+00  14230s
 1529138    5.0529132e+08   1.199225e+04   0.000000e+00  14235s
 1529845    5.0529025e+08   8.122007e+03   0.000000e+00  14241s
 1530451    5.0528946e+08   8.739511e+03   0.000000e+00  14245s
 1531158    5.0528819e+08   9.637275e+03   0.000000e+00  14251s
 1531764    5.0528696e+08   7.092533e+03   0.000000e+00  14256s
 1532370    5.0528546e+08   9.774609e+03   0.000000e+00  14260s
 1532976    5.0528412e+08   1.054799e+04   0.000000e+00  14265s
 1533582    5.0528305e+08   7.176245e+03   0.000000e+00  14270s
 1534188    5.0528219e+08   8.498570e+03   0.000000e+00  14275s
 1534895    5.0528013e+08   1.524805e+04   0.000000e+00  14281s
 1535501    5.0527896e+08   6.471917e+03   0.000000e+00  14286s
 1536107    5.0527798e+08   1.674336e+04   0.000000e+00  14291s
 1536713    5.0527705e+08   5.271418e+03   0.000000e+00  14295s
 1537319    5.0527591e+08   9.820024e+03   0.000000e+00  14300s
 1538026    5.0527451e+08   5.446550e+03   0.000000e+00  14306s
 1538632    5.0527365e+08   6.423596e+03   0.000000e+00  14310s
 1539339    5.0527257e+08   7.297243e+03   0.000000e+00  14316s
 1539844    5.0527203e+08   4.421594e+03   0.000000e+00  14320s
 1540551    5.0527121e+08   4.186890e+03   0.000000e+00  14326s
 1541157    5.0527018e+08   3.805819e+03   0.000000e+00  14330s
 1541864    5.0526923e+08   4.776339e+03   0.000000e+00  14336s
 1542470    5.0526837e+08   4.593707e+03   0.000000e+00  14340s
 1543076    5.0526782e+08   3.754144e+03   0.000000e+00  14345s
 1543783    5.0526699e+08   7.262896e+03   0.000000e+00  14350s
 1544389    5.0526632e+08   9.120928e+03   0.000000e+00  14355s
 1545096    5.0526556e+08   5.249143e+03   0.000000e+00  14361s
 1545702    5.0526507e+08   6.836182e+03   0.000000e+00  14365s
 1546308    5.0526401e+08   5.843126e+03   0.000000e+00  14370s
 1547015    5.0526300e+08   4.801195e+03   0.000000e+00  14376s
 1547621    5.0526198e+08   2.756228e+03   0.000000e+00  14381s
 1548126    5.0526147e+08   3.627065e+03   0.000000e+00  14385s
 1548833    5.0526093e+08   4.912452e+03   0.000000e+00  14391s
 1549439    5.0526040e+08   8.023089e+03   0.000000e+00  14395s
 1550045    5.0526013e+08   2.528546e+03   0.000000e+00  14400s
 1550752    5.0525939e+08   2.736274e+03   0.000000e+00  14406s
 1551358    5.0525883e+08   1.276298e+03   0.000000e+00  14410s
 1551964    5.0525831e+08   3.610057e+03   0.000000e+00  14415s
 1552671    5.0525781e+08   1.819750e+03   0.000000e+00  14421s
 1553277    5.0525746e+08   3.511888e+03   0.000000e+00  14425s
 1553883    5.0525651e+08   3.840520e+03   0.000000e+00  14430s
 1554590    5.0525591e+08   5.916239e+03   0.000000e+00  14436s
 1555196    5.0525515e+08   2.303890e+03   0.000000e+00  14441s
 1555802    5.0525449e+08   1.014818e+04   0.000000e+00  14445s
 1556408    5.0525397e+08   2.176604e+03   0.000000e+00  14450s
 1557115    5.0525359e+08   1.531451e+03   0.000000e+00  14456s
 1557721    5.0525328e+08   1.669848e+03   0.000000e+00  14461s
 1558327    5.0525276e+08   1.947456e+03   0.000000e+00  14465s
 1558933    5.0525197e+08   2.229449e+03   0.000000e+00  14470s
 1559640    5.0525140e+08   6.146236e+03   0.000000e+00  14476s
 1560246    5.0525077e+08   1.772091e+03   0.000000e+00  14480s
 1560852    5.0525041e+08   6.395569e+02   0.000000e+00  14485s
 1561559    5.0525023e+08   8.583163e+02   0.000000e+00  14491s
 1562165    5.0524998e+08   7.302979e+02   0.000000e+00  14495s
 1562771    5.0524972e+08   1.872492e+03   0.000000e+00  14500s
 1563478    5.0524934e+08   3.779005e+02   0.000000e+00  14506s
 1564084    5.0524912e+08   4.177036e+02   0.000000e+00  14511s
 1564690    5.0524895e+08   3.916681e+02   0.000000e+00  14515s
 1565296    5.0524882e+08   6.634017e+02   0.000000e+00  14521s
 1565902    5.0524867e+08   7.477442e+02   0.000000e+00  14525s
 1566609    5.0524847e+08   2.450320e+02   0.000000e+00  14531s
 1567215    5.0524837e+08   2.567343e+02   0.000000e+00  14535s
 1567922    5.0524817e+08   3.325900e+02   0.000000e+00  14541s
 1568528    5.0524801e+08   3.319438e+02   0.000000e+00  14545s
 1569134    5.0524790e+08   2.443591e+03   0.000000e+00  14550s
 1569841    5.0524782e+08   3.516997e+02   0.000000e+00  14556s
 1570447    5.0524777e+08   2.208307e+02   0.000000e+00  14560s
 1571053    5.0524774e+08   1.322615e+02   0.000000e+00  14565s
 1571760    5.0524770e+08   2.923179e+02   0.000000e+00  14570s
 1572366    5.0524769e+08   3.653279e+03   0.000000e+00  14576s
 1572972    5.0524768e+08   6.829881e+02   0.000000e+00  14581s
 1573578    5.0524765e+08   1.037921e+01   0.000000e+00  14586s
 1574184    5.0524762e+08   7.538551e+01   0.000000e+00  14590s
 1574790    5.0524759e+08   2.495452e+02   0.000000e+00  14595s
 1575497    5.0524758e+08   6.426726e+02   0.000000e+00  14601s
 1575834    5.0524759e+08   0.000000e+00   0.000000e+00  14605s
 1575904    5.0524759e+08   0.000000e+00   0.000000e+00  14610s

Extra simplex iterations after uncrush: 70

Root relaxation: objective 5.052476e+08, 1575904 iterations, 12397.72 seconds (12531.98 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 5.0525e+08    0 3126 -1.567e+12 5.0525e+08   100%     - 15120s
H    0     0                    -6.36507e+11 5.0525e+08   100%     - 15167s
H    0     0                    -6.34243e+11 5.0525e+08   100%     - 15168s
H    0     0                    -6.34060e+11 5.0525e+08   100%     - 15168s
     0     0 5.0505e+08    0 4296 -6.341e+11 5.0505e+08   100%     - 15627s
     0     0 5.0502e+08    0 4293 -6.341e+11 5.0502e+08   100%     - 15742s
     0     0 5.0500e+08    0 4450 -6.341e+11 5.0500e+08   100%     - 15812s
     0     0 5.0497e+08    0 4549 -6.341e+11 5.0497e+08   100%     - 15869s
     0     0 5.0495e+08    0 4631 -6.341e+11 5.0495e+08   100%     - 15929s
     0     0 5.0493e+08    0 4667 -6.341e+11 5.0493e+08   100%     - 15980s
     0     0 5.0491e+08    0 4695 -6.341e+11 5.0491e+08   100%     - 16031s
     0     0 5.0489e+08    0 4760 -6.341e+11 5.0489e+08   100%     - 16088s
     0     0 5.0487e+08    0 4859 -6.341e+11 5.0487e+08   100%     - 16146s
     0     0 5.0486e+08    0 4797 -6.341e+11 5.0486e+08   100%     - 16192s
     0     0 5.0484e+08    0 4792 -6.341e+11 5.0484e+08   100%     - 16231s
     0     0 5.0483e+08    0 4825 -6.341e+11 5.0483e+08   100%     - 16282s
     0     0 5.0480e+08    0 4823 -6.341e+11 5.0480e+08   100%     - 16368s
     0     0 5.0479e+08    0 4951 -6.341e+11 5.0479e+08   100%     - 16409s
     0     0 5.0478e+08    0 4981 -6.341e+11 5.0478e+08   100%     - 16459s
     0     0 5.0476e+08    0 4978 -6.341e+11 5.0476e+08   100%     - 16520s
     0     0 5.0475e+08    0 5037 -6.341e+11 5.0475e+08   100%     - 16560s
     0     0 5.0474e+08    0 4995 -6.341e+11 5.0474e+08   100%     - 16602s
     0     0 5.0474e+08    0 5051 -6.341e+11 5.0474e+08   100%     - 16644s
     0     0 5.0473e+08    0 5046 -6.341e+11 5.0473e+08   100%     - 16673s
     0     0 5.0472e+08    0 4951 -6.341e+11 5.0472e+08   100%     - 16721s
     0     0 5.0471e+08    0 4971 -6.341e+11 5.0471e+08   100%     - 16750s
     0     0 5.0471e+08    0 4910 -6.341e+11 5.0471e+08   100%     - 16774s
     0     0 5.0470e+08    0 4887 -6.341e+11 5.0470e+08   100%     - 16804s
     0     0 5.0469e+08    0 4844 -6.341e+11 5.0469e+08   100%     - 16848s
     0     0 5.0469e+08    0 4822 -6.341e+11 5.0469e+08   100%     - 16886s
     0     0 5.0468e+08    0 4834 -6.341e+11 5.0468e+08   100%     - 16923s
     0     0 5.0467e+08    0 4871 -6.341e+11 5.0467e+08   100%     - 16954s
     0     0 5.0467e+08    0 4878 -6.341e+11 5.0467e+08   100%     - 16975s
     0     0 5.0466e+08    0 4848 -6.341e+11 5.0466e+08   100%     - 17003s
     0     0 5.0466e+08    0 4863 -6.341e+11 5.0466e+08   100%     - 17059s
     0     0 5.0465e+08    0 4886 -6.341e+11 5.0465e+08   100%     - 17107s
     0     0 5.0465e+08    0 4886 -6.341e+11 5.0465e+08   100%     - 17131s
     0     0 5.0464e+08    0 4889 -6.341e+11 5.0464e+08   100%     - 17151s
     0     0 5.0464e+08    0 4940 -6.341e+11 5.0464e+08   100%     - 17182s
     0     0 5.0463e+08    0 4913 -6.341e+11 5.0463e+08   100%     - 17221s
     0     0 5.0463e+08    0 4903 -6.341e+11 5.0463e+08   100%     - 17241s
     0     0 5.0462e+08    0 4872 -6.341e+11 5.0462e+08   100%     - 17264s
     0     0 5.0462e+08    0 4878 -6.341e+11 5.0462e+08   100%     - 17287s
     0     0 5.0462e+08    0 4895 -6.341e+11 5.0462e+08   100%     - 17306s
     0     0 5.0461e+08    0 4893 -6.341e+11 5.0461e+08   100%     - 17339s
     0     0 5.0461e+08    0 4911 -6.341e+11 5.0461e+08   100%     - 17365s
     0     0 5.0460e+08    0 4898 -6.341e+11 5.0460e+08   100%     - 17390s
     0     0 5.0460e+08    0 4893 -6.341e+11 5.0460e+08   100%     - 17415s
     0     0 5.0460e+08    0 4937 -6.341e+11 5.0460e+08   100%     - 17439s
     0     0 5.0459e+08    0 4914 -6.341e+11 5.0459e+08   100%     - 17462s
     0     0 5.0459e+08    0 4945 -6.341e+11 5.0459e+08   100%     - 17505s
     0     0 5.0459e+08    0 4953 -6.341e+11 5.0459e+08   100%     - 17535s
     0     0 5.0458e+08    0 4954 -6.341e+11 5.0458e+08   100%     - 17553s
     0     0 5.0458e+08    0 4968 -6.341e+11 5.0458e+08   100%     - 17576s
     0     0 5.0458e+08    0 4970 -6.341e+11 5.0458e+08   100%     - 17619s
     0     0 5.0457e+08    0 4961 -6.341e+11 5.0457e+08   100%     - 17654s
     0     0 5.0457e+08    0 4962 -6.341e+11 5.0457e+08   100%     - 17685s
     0     0 5.0457e+08    0 4963 -6.341e+11 5.0457e+08   100%     - 17726s
     0     0 5.0457e+08    0 4958 -6.341e+11 5.0457e+08   100%     - 17747s
     0     0 5.0456e+08    0 4957 -6.341e+11 5.0456e+08   100%     - 17776s
     0     0 5.0456e+08    0 4998 -6.341e+11 5.0456e+08   100%     - 17806s
     0     0 5.0456e+08    0 4984 -6.341e+11 5.0456e+08   100%     - 17825s
     0     0 5.0456e+08    0 4959 -6.341e+11 5.0456e+08   100%     - 17859s
     0     0 5.0455e+08    0 4956 -6.341e+11 5.0455e+08   100%     - 17882s
     0     0 5.0455e+08    0 4929 -6.341e+11 5.0455e+08   100%     - 17912s
     0     0 5.0455e+08    0 4941 -6.341e+11 5.0455e+08   100%     - 17928s
     0     0 5.0455e+08    0 5011 -6.341e+11 5.0455e+08   100%     - 17966s
     0     0 5.0454e+08    0 4980 -6.341e+11 5.0454e+08   100%     - 17995s
     0     0 5.0454e+08    0 4979 -6.341e+11 5.0454e+08   100%     - 18026s
     0     0 5.0454e+08    0 4961 -6.341e+11 5.0454e+08   100%     - 18042s
     0     0 5.0454e+08    0 4948 -6.341e+11 5.0454e+08   100%     - 18064s
     0     0 5.0454e+08    0 4963 -6.341e+11 5.0454e+08   100%     - 18083s
     0     0 5.0453e+08    0 4854 -6.341e+11 5.0453e+08   100%     - 18101s
     0     0 5.0453e+08    0 4951 -6.341e+11 5.0453e+08   100%     - 18117s
     0     0 5.0453e+08    0 4967 -6.341e+11 5.0453e+08   100%     - 18131s
     0     0 5.0453e+08    0 4865 -6.341e+11 5.0453e+08   100%     - 18154s
     0     0 5.0453e+08    0 4873 -6.341e+11 5.0453e+08   100%     - 18175s
     0     0 5.0453e+08    0 4874 -6.341e+11 5.0453e+08   100%     - 18193s
     0     0 5.0452e+08    0 4875 -6.341e+11 5.0452e+08   100%     - 18209s
     0     0 5.0452e+08    0 4877 -6.341e+11 5.0452e+08   100%     - 18231s
     0     0 5.0452e+08    0 4876 -6.341e+11 5.0452e+08   100%     - 18255s
     0     0 5.0452e+08    0 4894 -6.341e+11 5.0452e+08   100%     - 18281s
     0     0 5.0452e+08    0 4894 -6.341e+11 5.0452e+08   100%     - 18306s
     0     0 5.0452e+08    0 4910 -6.341e+11 5.0452e+08   100%     - 18333s
     0     0 5.0452e+08    0 4949 -6.341e+11 5.0452e+08   100%     - 18368s
     0     0 5.0451e+08    0 4914 -6.341e+11 5.0451e+08   100%     - 18398s
     0     0 5.0451e+08    0 4938 -6.341e+11 5.0451e+08   100%     - 18435s
     0     0 5.0451e+08    0 4940 -6.341e+11 5.0451e+08   100%     - 18461s
     0     0 5.0450e+08    0 4920 -6.341e+11 5.0450e+08   100%     - 18486s
     0     0 5.0450e+08    0 4908 -6.341e+11 5.0450e+08   100%     - 18513s
     0     0 5.0450e+08    0 4907 -6.341e+11 5.0450e+08   100%     - 18528s
     0     0 5.0450e+08    0 4906 -6.341e+11 5.0450e+08   100%     - 18546s
     0     0 5.0449e+08    0 4944 -6.341e+11 5.0449e+08   100%     - 18581s
     0     0 5.0449e+08    0 4935 -6.341e+11 5.0449e+08   100%     - 18608s
     0     0 5.0449e+08    0 4921 -6.341e+11 5.0449e+08   100%     - 18639s
     0     0 5.0449e+08    0 4957 -6.341e+11 5.0449e+08   100%     - 18661s
     0     0 5.0448e+08    0 4955 -6.341e+11 5.0448e+08   100%     - 18681s
     0     0 5.0448e+08    0 4958 -6.341e+11 5.0448e+08   100%     - 18706s
     0     0 5.0448e+08    0 4949 -6.341e+11 5.0448e+08   100%     - 18731s
     0     0 5.0448e+08    0 4919 -6.341e+11 5.0448e+08   100%     - 18755s
     0     0 5.0448e+08    0 4923 -6.341e+11 5.0448e+08   100%     - 18772s
     0     0 5.0448e+08    0 5086 -6.341e+11 5.0448e+08   100%     - 18806s
     0     0 5.0447e+08    0 4947 -6.341e+11 5.0447e+08   100%     - 18825s
     0     0 5.0447e+08    0 4938 -6.341e+11 5.0447e+08   100%     - 18845s
     0     0 5.0447e+08    0 4967 -6.341e+11 5.0447e+08   100%     - 18871s
     0     0 5.0447e+08    0 4950 -6.341e+11 5.0447e+08   100%     - 18888s
     0     0 5.0447e+08    0 4917 -6.341e+11 5.0447e+08   100%     - 18909s
     0     0 5.0447e+08    0 4909 -6.341e+11 5.0447e+08   100%     - 18933s
     0     0 5.0447e+08    0 5076 -6.341e+11 5.0447e+08   100%     - 18961s
     0     0 5.0447e+08    0 4937 -6.341e+11 5.0447e+08   100%     - 18992s
     0     0 5.0447e+08    0 4931 -6.341e+11 5.0447e+08   100%     - 19011s
     0     0 5.0447e+08    0 4926 -6.341e+11 5.0447e+08   100%     - 19031s
     0     0 5.0446e+08    0 4929 -6.341e+11 5.0446e+08   100%     - 19049s
     0     0 5.0446e+08    0 4947 -6.341e+11 5.0446e+08   100%     - 19072s
     0     0 5.0446e+08    0 4921 -6.341e+11 5.0446e+08   100%     - 19106s
     0     0 5.0446e+08    0 4915 -6.341e+11 5.0446e+08   100%     - 19133s
     0     0 5.0446e+08    0 4912 -6.341e+11 5.0446e+08   100%     - 19168s
     0     0 5.0446e+08    0 4931 -6.341e+11 5.0446e+08   100%     - 19191s
     0     0 5.0446e+08    0 4902 -6.341e+11 5.0446e+08   100%     - 19226s
     0     0 5.0446e+08    0 4916 -6.341e+11 5.0446e+08   100%     - 19251s
     0     0 5.0446e+08    0 4913 -6.341e+11 5.0446e+08   100%     - 19275s
     0     0 5.0446e+08    0 4919 -6.341e+11 5.0446e+08   100%     - 19292s
     0     0 5.0445e+08    0 4931 -6.341e+11 5.0445e+08   100%     - 19320s
     0     0 5.0445e+08    0 4933 -6.341e+11 5.0445e+08   100%     - 19350s
     0     0 5.0445e+08    0 4936 -6.341e+11 5.0445e+08   100%     - 19368s
     0     0 5.0445e+08    0 4933 -6.341e+11 5.0445e+08   100%     - 19386s
     0     0 5.0445e+08    0 4932 -6.341e+11 5.0445e+08   100%     - 19397s
     0     0 5.0445e+08    0 4933 -6.341e+11 5.0445e+08   100%     - 19411s
     0     0 5.0445e+08    0 4935 -6.341e+11 5.0445e+08   100%     - 19424s
     0     0 5.0445e+08    0 4935 -6.341e+11 5.0445e+08   100%     - 19441s
     0     0 5.0445e+08    0 4943 -6.341e+11 5.0445e+08   100%     - 19454s
     0     0 5.0445e+08    0 4944 -6.341e+11 5.0445e+08   100%     - 19465s
     0     0 5.0445e+08    0 4963 -6.341e+11 5.0445e+08   100%     - 19487s
     0     0 5.0444e+08    0 4929 -6.341e+11 5.0444e+08   100%     - 19511s
     0     0 5.0444e+08    0 4965 -6.341e+11 5.0444e+08   100%     - 19529s
     0     0 5.0444e+08    0 4966 -6.341e+11 5.0444e+08   100%     - 19550s
     0     0 5.0444e+08    0 4973 -6.341e+11 5.0444e+08   100%     - 19569s
     0     0 5.0444e+08    0 4958 -6.341e+11 5.0444e+08   100%     - 19591s
     0     0 5.0444e+08    0 4971 -6.341e+11 5.0444e+08   100%     - 19617s
     0     0 5.0444e+08    0 4972 -6.341e+11 5.0444e+08   100%     - 19631s
     0     0 5.0444e+08    0 4971 -6.341e+11 5.0444e+08   100%     - 19647s
     0     0 5.0444e+08    0 4941 -6.341e+11 5.0444e+08   100%     - 19662s
     0     0 5.0444e+08    0 4961 -6.341e+11 5.0444e+08   100%     - 19680s
     0     0 5.0444e+08    0 4976 -6.341e+11 5.0444e+08   100%     - 19699s
     0     0 5.0444e+08    0 4963 -6.341e+11 5.0444e+08   100%     - 19717s
     0     0 5.0444e+08    0 4965 -6.341e+11 5.0444e+08   100%     - 19728s
     0     0 5.0444e+08    0 4965 -6.341e+11 5.0444e+08   100%     - 19746s
     0     0 5.0444e+08    0 4972 -6.341e+11 5.0444e+08   100%     - 19761s
     0     0 5.0444e+08    0 4979 -6.341e+11 5.0444e+08   100%     - 19775s
     0     0 5.0444e+08    0 4984 -6.341e+11 5.0444e+08   100%     - 19794s
     0     0 5.0444e+08    0 4987 -6.341e+11 5.0444e+08   100%     - 19814s
     0     0 5.0444e+08    0 4979 -6.341e+11 5.0444e+08   100%     - 19828s
     0     0 5.0444e+08    0 4966 -6.341e+11 5.0444e+08   100%     - 19842s
     0     0 5.0444e+08    0 4969 -6.341e+11 5.0444e+08   100%     - 19854s
     0     0 5.0444e+08    0 4971 -6.341e+11 5.0444e+08   100%     - 19870s
     0     0 5.0444e+08    0 4963 -6.341e+11 5.0444e+08   100%     - 19885s
     0     0 5.0444e+08    0 4966 -6.341e+11 5.0444e+08   100%     - 19902s
     0     0 5.0444e+08    0 4963 -6.341e+11 5.0444e+08   100%     - 19917s
     0     0 5.0444e+08    0 4969 -6.341e+11 5.0444e+08   100%     - 19929s
     0     0 5.0443e+08    0 4967 -6.341e+11 5.0443e+08   100%     - 19947s
     0     0 5.0443e+08    0 4983 -6.341e+11 5.0443e+08   100%     - 19968s
     0     0 5.0443e+08    0 4973 -6.341e+11 5.0443e+08   100%     - 19978s
     0     0 5.0443e+08    0 4988 -6.341e+11 5.0443e+08   100%     - 19995s
     0     0 5.0443e+08    0 4989 -6.341e+11 5.0443e+08   100%     - 20006s
     0     0 5.0443e+08    0 4988 -6.341e+11 5.0443e+08   100%     - 20023s
     0     0 5.0442e+08    0 4998 -6.341e+11 5.0442e+08   100%     - 20040s
     0     0 5.0442e+08    0 4993 -6.341e+11 5.0442e+08   100%     - 20052s
     0     0 5.0442e+08    0 4993 -6.341e+11 5.0442e+08   100%     - 20061s
     0     0 5.0442e+08    0 4989 -6.341e+11 5.0442e+08   100%     - 20071s
     0     0 5.0442e+08    0 4991 -6.341e+11 5.0442e+08   100%     - 20076s
     0     0 5.0442e+08    0 4991 -6.341e+11 5.0442e+08   100%     - 20082s
     0     0 5.0441e+08    0 4991 -6.341e+11 5.0441e+08   100%     - 20087s
     0     0 5.0441e+08    0 4995 -6.341e+11 5.0441e+08   100%     - 20096s
     0     0 5.0441e+08    0 5000 -6.341e+11 5.0441e+08   100%     - 20108s
     0     0 5.0441e+08    0 5006 -6.341e+11 5.0441e+08   100%     - 20114s
     0     0 5.0441e+08    0 5004 -6.341e+11 5.0441e+08   100%     - 20121s
     0     0 5.0441e+08    0 5007 -6.341e+11 5.0441e+08   100%     - 20128s
     0     0 5.0441e+08    0 5003 -6.341e+11 5.0441e+08   100%     - 20138s
     0     0 5.0441e+08    0 5005 -6.341e+11 5.0441e+08   100%     - 20154s
     0     0 5.0441e+08    0 5005 -6.341e+11 5.0441e+08   100%     - 20159s
     0     0 5.0441e+08    0 5004 -6.341e+11 5.0441e+08   100%     - 20165s
     0     0 5.0441e+08    0 5003 -6.341e+11 5.0441e+08   100%     - 20179s
     0     0 5.0441e+08    0 5006 -6.341e+11 5.0441e+08   100%     - 20194s
     0     0 5.0441e+08    0 5013 -6.341e+11 5.0441e+08   100%     - 20208s
     0     0 5.0441e+08    0 5013 -6.341e+11 5.0441e+08   100%     - 20213s
     0     0 5.0441e+08    0 5009 -6.341e+11 5.0441e+08   100%     - 20224s
     0     0 5.0440e+08    0 5011 -6.341e+11 5.0440e+08   100%     - 20240s
     0     0 5.0440e+08    0 5012 -6.341e+11 5.0440e+08   100%     - 20254s
     0     0 5.0440e+08    0 5020 -6.341e+11 5.0440e+08   100%     - 20268s
     0     0 5.0440e+08    0 5020 -6.341e+11 5.0440e+08   100%     - 20273s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20287s
     0     0 5.0440e+08    0 5019 -6.341e+11 5.0440e+08   100%     - 20300s
     0     0 5.0440e+08    0 5015 -6.341e+11 5.0440e+08   100%     - 20311s
     0     0 5.0440e+08    0 5018 -6.341e+11 5.0440e+08   100%     - 20327s
     0     0 5.0440e+08    0 5016 -6.341e+11 5.0440e+08   100%     - 20337s
     0     0 5.0440e+08    0 5013 -6.341e+11 5.0440e+08   100%     - 20351s
     0     0 5.0440e+08    0 5013 -6.341e+11 5.0440e+08   100%     - 20360s
     0     0 5.0440e+08    0 5013 -6.341e+11 5.0440e+08   100%     - 20366s
     0     0 5.0440e+08    0 5013 -6.341e+11 5.0440e+08   100%     - 20373s
     0     0 5.0440e+08    0 5013 -6.341e+11 5.0440e+08   100%     - 20379s
     0     0 5.0440e+08    0 5015 -6.341e+11 5.0440e+08   100%     - 20385s
     0     0 5.0440e+08    0 5017 -6.341e+11 5.0440e+08   100%     - 20395s
     0     0 5.0440e+08    0 5018 -6.341e+11 5.0440e+08   100%     - 20404s
     0     0 5.0440e+08    0 5021 -6.341e+11 5.0440e+08   100%     - 20415s
     0     0 5.0440e+08    0 5018 -6.341e+11 5.0440e+08   100%     - 20426s
     0     0 5.0440e+08    0 5018 -6.341e+11 5.0440e+08   100%     - 20435s
     0     0 5.0440e+08    0 5017 -6.341e+11 5.0440e+08   100%     - 20451s
     0     0 5.0440e+08    0 5022 -6.341e+11 5.0440e+08   100%     - 20464s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20473s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20481s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20489s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20498s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20504s
     0     0 5.0440e+08    0 5023 -6.341e+11 5.0440e+08   100%     - 20509s
     0     0 5.0439e+08    0 5023 -6.341e+11 5.0439e+08   100%     - 20514s
     0     0 5.0439e+08    0 5023 -6.341e+11 5.0439e+08   100%     - 20519s
     0     0 5.0439e+08    0 5023 -6.341e+11 5.0439e+08   100%     - 20525s
     0     0 5.0439e+08    0 5025 -6.341e+11 5.0439e+08   100%     - 20532s
     0     0 5.0439e+08    0 5025 -6.341e+11 5.0439e+08   100%     - 20538s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20546s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20551s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20557s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20563s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20568s
     0     0 5.0439e+08    0 5028 -6.341e+11 5.0439e+08   100%     - 20573s
     0     0 5.0439e+08    0 5029 -6.341e+11 5.0439e+08   100%     - 20580s
     0     0 5.0439e+08    0 5029 -6.341e+11 5.0439e+08   100%     - 20589s
     0     0 5.0439e+08    0 5029 -6.341e+11 5.0439e+08   100%     - 20594s
     0     0 5.0439e+08    0 5029 -6.341e+11 5.0439e+08   100%     - 20599s
     0     0 5.0439e+08    0 5029 -6.341e+11 5.0439e+08   100%     - 20608s
     0     0 5.0439e+08    0 5032 -6.341e+11 5.0439e+08   100%     - 20614s
     0     0 5.0439e+08    0 5032 -6.341e+11 5.0439e+08   100%     - 20622s
     0     0 5.0439e+08    0 5032 -6.341e+11 5.0439e+08   100%     - 20629s
     0     0 5.0439e+08    0 4990 -6.341e+11 5.0439e+08   100%     - 20638s
     0     0 5.0439e+08    0 4990 -6.341e+11 5.0439e+08   100%     - 20646s
     0     0 5.0437e+08    0 4920 -6.341e+11 5.0437e+08   100%     - 20845s
H    0     0                    -4.48510e+11 5.0437e+08   100%     - 20889s
H    0     0                    -4.48510e+11 5.0437e+08   100%     - 20890s
H    0     0                    -4.48397e+11 5.0437e+08   100%     - 20892s
H    0     0                    -4.48366e+11 5.0437e+08   100%     - 20898s
H    0     0                    -4.48318e+11 5.0437e+08   100%     - 20907s
H    0     0                    -4.48316e+11 5.0437e+08   100%     - 20907s
H    0     0                    -4.48277e+11 5.0437e+08   100%     - 20914s
     0     0 5.0437e+08    0 4958 -4.483e+11 5.0437e+08   100%     - 20965s
     0     0 5.0436e+08    0 4998 -4.483e+11 5.0436e+08   100%     - 21003s
     0     0 5.0436e+08    0 4986 -4.483e+11 5.0436e+08   100%     - 21048s
     0     0 5.0436e+08    0 5028 -4.483e+11 5.0436e+08   100%     - 21083s
     0     0 5.0436e+08    0 5082 -4.483e+11 5.0436e+08   100%     - 21117s
     0     0 5.0436e+08    0 5074 -4.483e+11 5.0436e+08   100%     - 21143s
     0     0 5.0436e+08    0 5063 -4.483e+11 5.0436e+08   100%     - 21183s
     0     0 5.0436e+08    0 5064 -4.483e+11 5.0436e+08   100%     - 21203s
     0     0 5.0436e+08    0 4944 -4.483e+11 5.0436e+08   100%     - 21229s
     0     0 5.0435e+08    0 4911 -4.483e+11 5.0435e+08   100%     - 21259s
     0     0 5.0435e+08    0 4920 -4.483e+11 5.0435e+08   100%     - 21278s
     0     0 5.0435e+08    0 4971 -4.483e+11 5.0435e+08   100%     - 21301s
     0     0 5.0435e+08    0 4947 -4.483e+11 5.0435e+08   100%     - 21318s
     0     0 5.0435e+08    0 4912 -4.483e+11 5.0435e+08   100%     - 21339s
     0     0 5.0435e+08    0 4911 -4.483e+11 5.0435e+08   100%     - 21354s
     0     0 5.0435e+08    0 4912 -4.483e+11 5.0435e+08   100%     - 21371s
     0     0 5.0435e+08    0 4912 -4.483e+11 5.0435e+08   100%     - 21387s
     0     0 5.0435e+08    0 4919 -4.483e+11 5.0435e+08   100%     - 21405s
     0     0 5.0435e+08    0 4861 -4.483e+11 5.0435e+08   100%     - 21418s
     0     0 5.0435e+08    0 4880 -4.483e+11 5.0435e+08   100%     - 21440s
     0     0 5.0435e+08    0 4890 -4.483e+11 5.0435e+08   100%     - 21461s
     0     0 5.0435e+08    0 4883 -4.483e+11 5.0435e+08   100%     - 21480s
     0     0 5.0435e+08    0 4891 -4.483e+11 5.0435e+08   100%     - 21501s
     0     0 5.0435e+08    0 4849 -4.483e+11 5.0435e+08   100%     - 21516s
     0     0 5.0435e+08    0 4869 -4.483e+11 5.0435e+08   100%     - 21532s
     0     0 5.0435e+08    0 4871 -4.483e+11 5.0435e+08   100%     - 21552s
     0     0 5.0434e+08    0 4672 -4.483e+11 5.0434e+08   100%     - 21713s
     0     0 5.0434e+08    0 2972 -4.483e+11 5.0434e+08   100%     - 22290s
H    0     0                    -1.34243e+10 5.0434e+08   104%     - 22909s
H    0     0                    -4.67117e+09 5.0434e+08   111%     - 24451s
H    0     0                    -4.67116e+09 5.0434e+08   111%     - 24515s
H    0     0                    -4.56634e+09 5.0434e+08   111%     - 25232s
H    0     0                    -4.56612e+09 5.0434e+08   111%     - 25238s
H    0     0                    -4.56612e+09 5.0434e+08   111%     - 25307s
H    0     0                    -4.56612e+09 5.0434e+08   111%     - 25308s
H    0     0                    -2.90000e+09 5.0434e+08   117%     - 25464s
H    0     0                    -2.89999e+09 5.0434e+08   117%     - 25465s
H    0     0                    -2.89999e+09 5.0434e+08   117%     - 25557s
H    0     0                    -2.89999e+09 5.0434e+08   117%     - 25558s
H    0     0                    -1.57346e+09 5.0434e+08   132%     - 25642s
H    0     0                    -1.57346e+09 5.0434e+08   132%     - 25643s
H    0     0                    -1.12293e+09 5.0434e+08   145%     - 25755s
H    0     0                    -1.12293e+09 5.0434e+08   145%     - 25927s
H    0     0                    -1.08769e+09 5.0434e+08   146%     - 25983s
H    0     0                    -1.08765e+09 5.0434e+08   146%     - 26054s
H    0     0                    -1.13525e+08 5.0434e+08   544%     - 26102s
H    0     0                    -1.13525e+08 5.0434e+08   544%     - 26102s
H    0     0                    8866397.4973 5.0434e+08  5588%     - 26187s
H    0     0                    8866676.3205 5.0434e+08  5588%     - 26187s
H    0     0                    4.592016e+08 5.0434e+08  9.83%     - 26319s
H    0     0                    4.592022e+08 5.0434e+08  9.83%     - 26322s
H    0     0                    4.802556e+08 5.0434e+08  5.02%     - 26371s
H    0     0                    4.802561e+08 5.0434e+08  5.02%     - 26373s
H    0     0                    4.802618e+08 5.0434e+08  5.01%     - 26389s
H    0     0                    4.803588e+08 5.0434e+08  4.99%     - 26390s
H    0     0                    4.803591e+08 5.0434e+08  4.99%     - 26392s
H    0     0                    4.958032e+08 5.0434e+08  1.72%     - 26540s
H    0     0                    4.958037e+08 5.0434e+08  1.72%     - 26542s
H    0     0                    4.958039e+08 5.0434e+08  1.72%     - 26898s
H    0     0                    4.958077e+08 5.0434e+08  1.72%     - 27416s
H    0     0                    5.000783e+08 5.0434e+08  0.85%     - 28070s
     4     2 5.0434e+08    1 2190 5.0008e+08 5.0434e+08  0.85% 263825 32819s
     4     2 5.0434e+08    1 3557 5.0008e+08 5.0434e+08  0.85% 270273 33008s
     4     2 5.0434e+08    1 3629 5.0008e+08 5.0434e+08  0.85% 271051 33067s
     4     2 5.0434e+08    1 3685 5.0008e+08 5.0434e+08  0.85% 272000 33107s
     4     2 5.0434e+08    1 3683 5.0008e+08 5.0434e+08  0.85% 272716 33127s
     4     2 5.0434e+08    1 3675 5.0008e+08 5.0434e+08  0.85% 273314 33146s
     4     2 5.0434e+08    1 3691 5.0008e+08 5.0434e+08  0.85% 273771 33163s
     4     2 5.0434e+08    1 3722 5.0008e+08 5.0434e+08  0.85% 274175 33178s
     4     2 5.0434e+08    1 3735 5.0008e+08 5.0434e+08  0.85% 274873 33201s
     4     2 5.0434e+08    1 3745 5.0008e+08 5.0434e+08  0.85% 275453 33219s
     4     2 5.0434e+08    1 3768 5.0008e+08 5.0434e+08  0.85% 276087 33239s
     4     2 5.0434e+08    1 3783 5.0008e+08 5.0434e+08  0.85% 276661 33257s
     4     2 5.0434e+08    1 3734 5.0008e+08 5.0434e+08  0.85% 277181 33276s
     4     2 5.0434e+08    1 3666 5.0008e+08 5.0434e+08  0.85% 277848 33296s
     4     2 5.0434e+08    1 3659 5.0008e+08 5.0434e+08  0.85% 278236 33320s
     4     2 5.0434e+08    1 3769 5.0008e+08 5.0434e+08  0.85% 280365 33421s
     4     2 5.0434e+08    1 3777 5.0008e+08 5.0434e+08  0.85% 281150 33474s
     4     2 5.0434e+08    1 3866 5.0008e+08 5.0434e+08  0.85% 286091 33592s
     4     4 5.0434e+08    1 3866 5.0008e+08 5.0434e+08  0.85% 286091 36431s
H    4     4                    5.024073e+08 5.0434e+08  0.39% 286091 36455s
     5     4 5.0263e+08    1  499 5.0241e+08 5.0434e+08  0.39% 277210 36705s
     5     4 5.0259e+08    1 1136 5.0241e+08 5.0434e+08  0.39% 279043 36725s
     5     4 5.0258e+08    1 1081 5.0241e+08 5.0434e+08  0.39% 279310 36733s
     5     4 5.0258e+08    1 1083 5.0241e+08 5.0434e+08  0.39% 279472 36737s
     5     4 5.0258e+08    1 1087 5.0241e+08 5.0434e+08  0.39% 280145 36750s
     5     4 5.0257e+08    1 1099 5.0241e+08 5.0434e+08  0.39% 280301 36759s
     5     4 5.0257e+08    1 1175 5.0241e+08 5.0434e+08  0.39% 281486 36772s
     5     6 5.0257e+08    1 1175 5.0241e+08 5.0434e+08  0.39% 281486 36903s
H    5     6                    5.024075e+08 5.0434e+08  0.39% 281486 36906s
     6     6 5.0252e+08    1  256 5.0241e+08 5.0434e+08  0.39% 256744 36989s
     6     6 5.0250e+08    1  568 5.0241e+08 5.0434e+08  0.39% 257449 36997s
     6     6 5.0249e+08    1  516 5.0241e+08 5.0434e+08  0.39% 257607 37001s
     6     6 5.0248e+08    1  581 5.0241e+08 5.0434e+08  0.39% 258055 37007s
     6     6 5.0248e+08    1  583 5.0241e+08 5.0434e+08  0.39% 258111 37011s
     6     6 5.0248e+08    1  569 5.0241e+08 5.0434e+08  0.39% 258491 37016s
     6     8 5.0248e+08    1  569 5.0241e+08 5.0434e+08  0.39% 258491 37062s
H    6     8                    5.024075e+08 5.0434e+08  0.39% 258491 37064s
     6    10 5.0434e+08    2 3793 5.0241e+08 5.0434e+08  0.39% 258491 37079s
     8    14 5.0434e+08    3 3777 5.0241e+08 5.0434e+08  0.39% 194116 37103s
    12    15 5.0434e+08    4 3560 5.0241e+08 5.0434e+08  0.39% 130137 37144s
    13    22 5.0434e+08    5 3529 5.0241e+08 5.0434e+08  0.39% 120417 37216s
    20    24 5.0429e+08    6 3325 5.0241e+08 5.0434e+08  0.39% 78808 37280s
    22    32 5.0428e+08    7 3244 5.0241e+08 5.0434e+08  0.39% 72183 37373s
    30    42 5.0425e+08    8 3172 5.0241e+08 5.0434e+08  0.39% 53544 37623s
    40    52 5.0381e+08    9 3312 5.0241e+08 5.0434e+08  0.39% 42019 37867s
    50    62 5.0419e+08    9 3137 5.0241e+08 5.0434e+08  0.39% 34445 38274s
    60   122 5.0380e+08   10 3304 5.0241e+08 5.0434e+08  0.39% 29069 38882s
   120   182 5.0405e+08   15 2939 5.0241e+08 5.0434e+08  0.39% 14884 38966s
   180   242 5.0393e+08   20 2798 5.0241e+08 5.0434e+08  0.39% 10135 39068s
   240   293 5.0372e+08   24 2861 5.0241e+08 5.0434e+08  0.39%  7710 39275s
   291   327 5.0382e+08   27 2561 5.0241e+08 5.0434e+08  0.39%  6507 39425s
   339   383 5.0375e+08   30 2614 5.0241e+08 5.0434e+08  0.39%  5869 39528s
   399   439 5.0375e+08   36 2585 5.0241e+08 5.0434e+08  0.39%  5086 39595s
   459   487 5.0374e+08   42 2617 5.0241e+08 5.0434e+08  0.39%  4456 39668s
H  519   452                    5.035718e+08 5.0434e+08  0.15%  3976 39693s
   519   454 5.0370e+08    2 1099 5.0357e+08 5.0434e+08  0.15%  3976 39700s
   521   458 5.0367e+08    3  879 5.0357e+08 5.0434e+08  0.15%  3970 39709s
   525   466 5.0363e+08    4  787 5.0357e+08 5.0434e+08  0.15%  3947 39720s
   533   474 5.0358e+08    5  815 5.0357e+08 5.0434e+08  0.15%  3905 39736s
   543   480 5.0358e+08    6  648 5.0357e+08 5.0434e+08  0.15%  3865 39765s
   557   496     cutoff    7      5.0357e+08 5.0434e+08  0.15%  3831 39792s
   636   524     cutoff    7      5.0357e+08 5.0432e+08  0.15%  3435 39817s
   676   593 5.0364e+08    6  550 5.0357e+08 5.0431e+08  0.15%  3254 39862s
   794   772 5.0358e+08   11  523 5.0357e+08 5.0431e+08  0.15%  2807 39901s
  1011   962 5.0359e+08   24  473 5.0357e+08 5.0431e+08  0.15%  2232 39941s
H 1251   908                    5.035773e+08 5.0430e+08  0.14%  1822 39945s
  1253   914 5.0360e+08    3  284 5.0358e+08 5.0426e+08  0.14%  1822 39958s
  1257   914 5.0359e+08    4  283 5.0358e+08 5.0426e+08  0.14%  1818 39960s
  1273   926 5.0359e+08    6  247 5.0358e+08 5.0425e+08  0.13%  1803 39973s
  1283   929 5.0359e+08    7  242 5.0358e+08 5.0425e+08  0.13%  1790 39993s
  1296   967 5.0359e+08    8  242 5.0358e+08 5.0425e+08  0.13%  1774 40007s
  1350   989 5.0358e+08   15  224 5.0358e+08 5.0425e+08  0.13%  1707 40028s
  1380  1013 5.0358e+08   16  240 5.0358e+08 5.0425e+08  0.13%  1671 40047s
  1436  1140 5.0358e+08   17  239 5.0358e+08 5.0425e+08  0.13%  1613 40071s
  1599  1302 5.0358e+08   30  217 5.0358e+08 5.0425e+08  0.13%  1455 40106s
H 1941  1302                    5.035774e+08 5.0424e+08  0.13%  1217 40108s
  1941  1351 5.0375e+08   48 2634 5.0358e+08 5.0424e+08  0.13%  1217 40192s
  2001  1390 5.0374e+08   52 2629 5.0358e+08 5.0424e+08  0.13%  1191 40242s
  2046  1416     cutoff   20      5.0358e+08 5.0424e+08  0.13%  1170 40296s
  2075  1434 5.0358e+08   22 3276 5.0358e+08 5.0424e+08  0.13%  1156 40352s
  2106  1454     cutoff   21      5.0358e+08 5.0424e+08  0.13%  1146 40414s
  2132  1480 5.0365e+08   41 2330 5.0358e+08 5.0424e+08  0.13%  1136 40481s
  2162  1523 5.0365e+08   47 2387 5.0358e+08 5.0424e+08  0.13%  1125 40568s
  2205  1565 5.0364e+08   53 2360 5.0358e+08 5.0424e+08  0.13%  1116 40663s
  2247  1604 5.0363e+08   56 2318 5.0358e+08 5.0424e+08  0.13%  1106 40728s
  2286  1655 5.0363e+08   57 2314 5.0358e+08 5.0424e+08  0.13%  1094 40801s
  2341  1708 5.0363e+08   63 2341 5.0358e+08 5.0424e+08  0.13%  1073 40870s
  2394  1768 5.0363e+08   69 2362 5.0358e+08 5.0424e+08  0.13%  1055 40919s
  2454  1821 5.0362e+08   75 2384 5.0358e+08 5.0424e+08  0.13%  1032 40960s
  2511  1877 5.0362e+08   81 2441 5.0358e+08 5.0424e+08  0.13%  1012 40998s
  2571  1927 5.0362e+08   87 2451 5.0358e+08 5.0424e+08  0.13%   991 41042s
  2629  2094     cutoff   34      5.0358e+08 5.0424e+08  0.13%   971 41105s
  2869  2307 5.0359e+08   39  543 5.0358e+08 5.0422e+08  0.13%   904 41132s
  3099  2489 5.0358e+08   63  499 5.0358e+08 5.0422e+08  0.13%   841 41159s
  3327  2682 5.0358e+08   34  220 5.0358e+08 5.0422e+08  0.13%   787 41210s
  3737  2906 5.0358e+08   27  247 5.0358e+08 5.0422e+08  0.13%   711 41251s
H 4144  2906                    5.035775e+08 5.0422e+08  0.13%   648 41254s
  4144  2957 5.0362e+08   93 2513 5.0358e+08 5.0422e+08  0.13%   648 41353s
  4201  3004 5.0361e+08   99 2504 5.0358e+08 5.0422e+08  0.13%   645 41462s
  4248  3055 5.0361e+08  105 2465 5.0358e+08 5.0422e+08  0.13%   639 41499s
  4302  3109 5.0361e+08  111 2458 5.0358e+08 5.0422e+08  0.13%   633 41532s
  4356  3158 5.0361e+08  117 2453 5.0358e+08 5.0422e+08  0.13%   627 41565s
  4405  3214 5.0361e+08  123 2363 5.0358e+08 5.0422e+08  0.13%   621 41595s
  4461  3271 5.0361e+08  129 2370 5.0358e+08 5.0422e+08  0.13%   615 41625s
  4518  3321 5.0361e+08  135 2340 5.0358e+08 5.0422e+08  0.13%   608 41674s
  4570  3371 5.0361e+08  141 2334 5.0358e+08 5.0422e+08  0.13%   602 41723s
  4625  3296 5.0376e+08   15 2172 5.0358e+08 5.0422e+08  0.13%   597 50755s
  4626  3297 5.0415e+08   15 5364 5.0358e+08 5.0422e+08  0.13%   597 51058s
  4627  3298 5.0405e+08   15 5465 5.0358e+08 5.0422e+08  0.13%   596 51152s
  4628  3298 5.0376e+08   15 5484 5.0358e+08 5.0422e+08  0.13%   596 51239s
  4629  3299 5.0385e+08   15 5506 5.0358e+08 5.0422e+08  0.13%   596 51321s
  4630  3300 5.0379e+08   15 5512 5.0358e+08 5.0422e+08  0.13%   596 51383s
  4631  3300 5.0374e+08   15 5635 5.0358e+08 5.0422e+08  0.13%   596 51417s
  4632  3301 5.0376e+08   15 5632 5.0358e+08 5.0422e+08  0.13%   596 51445s
  4633  3302 5.0378e+08   15 5609 5.0358e+08 5.0422e+08  0.13%   596 51477s
  4634  3302 5.0359e+08   15 5560 5.0358e+08 5.0422e+08  0.13%   596 51516s
  4635  3303 5.0359e+08   15 5627 5.0358e+08 5.0422e+08  0.13%   595 51546s
  4636  3304 5.0376e+08   15 5599 5.0358e+08 5.0422e+08  0.13%   595 51573s
  4637  3304 5.0402e+08   15 5455 5.0358e+08 5.0422e+08  0.13%   595 51631s
  4638  3305 5.0389e+08   15 6054 5.0358e+08 5.0422e+08  0.13%   595 51780s
  4639  3306 5.0377e+08   15 6012 5.0358e+08 5.0422e+08  0.13%   595 51873s
  4640  3306 5.0406e+08   15 6130 5.0358e+08 5.0422e+08  0.13%   595 51944s
  4641  3307 5.0377e+08   15 5921 5.0358e+08 5.0422e+08  0.13%   595 55357s
  4642  3165 5.0422e+08    1 5921 5.0358e+08 5.0422e+08  0.13%   882 57699s
  4643  3100 5.0422e+08    2 5769 5.0358e+08 5.0422e+08  0.13%   882 57715s
  4645  3104 5.0422e+08    3 5767 5.0358e+08 5.0422e+08  0.13%   882 57802s
  4649  3042 5.0422e+08    4 5295 5.0358e+08 5.0422e+08  0.13%   882 57889s
  4653  3051 5.0422e+08    5 5214 5.0358e+08 5.0422e+08  0.13%   888 57924s
  4663  3066 5.0422e+08    6 5041 5.0358e+08 5.0422e+08  0.13%   888 58034s
  4681  2964 5.0422e+08    7 4917 5.0358e+08 5.0422e+08  0.13%   898 58178s
  4702  2975 5.0382e+08    9 5069 5.0358e+08 5.0422e+08  0.13%   896 58394s
  4720  3035 5.0413e+08   12 3665 5.0358e+08 5.0422e+08  0.13%   898 58534s
  4790  3065 5.0399e+08   16 3381 5.0358e+08 5.0422e+08  0.13%   899 58662s
  4860  3103 5.0400e+08   19 3023 5.0358e+08 5.0422e+08  0.13%   897 58787s
  4929  3124 5.0383e+08   23 3030 5.0358e+08 5.0422e+08  0.13%   897 58944s
  4975  3101 5.0383e+08   26 2816 5.0358e+08 5.0422e+08  0.13%   904 59061s
H 5022  3085                    5.035972e+08 5.0422e+08  0.12%   903 59087s
  5022  3232 5.0360e+08   87  524 5.0360e+08 5.0422e+08  0.12%   903 59125s
  5262  3106     cutoff  111      5.0360e+08 5.0422e+08  0.12%   864 59153s
  5488  3234 5.0361e+08   42  520 5.0360e+08 5.0422e+08  0.12%   832 59191s
  5632  3236 5.0361e+08   15  453 5.0360e+08 5.0422e+08  0.12%   812 59677s
  5633  3237 5.0362e+08   15 2390 5.0360e+08 5.0422e+08  0.12%   811 59715s
  5634  3238 5.0362e+08   15 2292 5.0360e+08 5.0422e+08  0.12%   811 59729s
  5635  3238 5.0361e+08   15 2339 5.0360e+08 5.0422e+08  0.12%   811 59738s
  5636  3239 5.0361e+08   15 2313 5.0360e+08 5.0422e+08  0.12%   811 59751s
  5637  3240 5.0361e+08   15 2520 5.0360e+08 5.0422e+08  0.12%   811 59772s
  5638  3240 5.0361e+08   15 2520 5.0360e+08 5.0422e+08  0.12%   811 59782s
  5639  3241 5.0362e+08   15 2343 5.0360e+08 5.0422e+08  0.12%   811 59792s
  5640  3242 5.0362e+08   15 2307 5.0360e+08 5.0422e+08  0.12%   810 59800s
  5641  3242 5.0361e+08   15 2810 5.0360e+08 5.0422e+08  0.12%   810 60014s
  5642  3076 5.0362e+08    1 2593 5.0360e+08 5.0422e+08  0.12%   861 60156s
  5643  3078 5.0362e+08    2 2257 5.0360e+08 5.0422e+08  0.12%   861 60163s
  5645  3077 5.0362e+08    3 2007 5.0360e+08 5.0422e+08  0.12%   862 60170s
  5649  3078 5.0362e+08    4 1346 5.0360e+08 5.0422e+08  0.12%   862 60176s
  5653  3078 infeasible    5      5.0360e+08 5.0422e+08  0.12%   862 60186s
  5659  3080 5.0362e+08    6 1166 5.0360e+08 5.0422e+08  0.12%   863 60192s
  5667  3082 5.0362e+08    7 1085 5.0360e+08 5.0422e+08  0.12%   863 60200s
  5677  3092 5.0361e+08    8  933 5.0360e+08 5.0422e+08  0.12%   865 60212s
  5703  3079 5.0361e+08    9  647 5.0360e+08 5.0422e+08  0.12%   862 60223s
  5718  3074 5.0360e+08   10  645 5.0360e+08 5.0422e+08  0.12%   864 60231s
  5731  3064 5.0360e+08   11  601 5.0360e+08 5.0422e+08  0.12%   864 60244s
  5754  3061 5.0361e+08   13  569 5.0360e+08 5.0422e+08  0.12%   863 60258s
  5779  3077 5.0361e+08   17  588 5.0360e+08 5.0422e+08  0.12%   862 60284s
  5808  3091 5.0361e+08   21  576 5.0360e+08 5.0422e+08  0.12%   860 60298s
H 5892  3063                    5.035993e+08 5.0422e+08  0.12%   851 60302s
  5892  3116 5.0382e+08   28 2497 5.0360e+08 5.0422e+08  0.12%   851 60482s
  5951  3155 5.0379e+08   32 2334 5.0360e+08 5.0422e+08  0.12%   859 60581s
  6014  3197 5.0377e+08   35 2373 5.0360e+08 5.0422e+08  0.12%   858 60934s
  6077  3144 5.0379e+08   39 2309 5.0360e+08 5.0422e+08  0.12%   852 61000s
  6145  3185 5.0375e+08   42 2180 5.0360e+08 5.0422e+08  0.12%   845 61055s
  6208  3203 5.0378e+08   46 2173 5.0360e+08 5.0422e+08  0.12%   838 61188s
  6247  3199 5.0378e+08   48 2178 5.0360e+08 5.0422e+08  0.12%   835 61281s
  6256  3237 5.0378e+08   49 2160 5.0360e+08 5.0422e+08  0.12%   836 61354s
  6297  3287 5.0378e+08   52 2211 5.0360e+08 5.0422e+08  0.12%   832 61420s
  6361  3328 5.0378e+08   55 2207 5.0360e+08 5.0422e+08  0.12%   826 61488s
  6427  3324 5.0377e+08   59 2186 5.0360e+08 5.0422e+08  0.12%   819 61685s
  6445  3281 5.0377e+08   59 2182 5.0360e+08 5.0422e+08  0.12%   818 61751s
  6501  3318 5.0377e+08   63 2213 5.0360e+08 5.0422e+08  0.12%   814 61810s
  6557  3360 5.0376e+08   66 2193 5.0360e+08 5.0422e+08  0.12%   808 61868s
  6618  3400 5.0376e+08   70 2202 5.0360e+08 5.0422e+08  0.12%   803 61924s
  6678  3442 5.0376e+08   73 2200 5.0360e+08 5.0422e+08  0.12%   797 61977s
  6740  3478 5.0376e+08   77 2255 5.0360e+08 5.0422e+08  0.12%   790 62031s
  6797  3521 5.0376e+08   80 2130 5.0360e+08 5.0422e+08  0.12%   787 62083s
  6859  3567 5.0375e+08   84 2119 5.0360e+08 5.0422e+08  0.12%   782 62130s
  6925  3612 5.0375e+08   87 2136 5.0360e+08 5.0422e+08  0.12%   775 62183s
H 6992  3589                    5.036171e+08 5.0422e+08  0.12%   769 62210s
  6992  3722 5.0362e+08   28  517 5.0362e+08 5.0422e+08  0.12%   769 62262s
  7165  3818 5.0362e+08   36  479 5.0362e+08 5.0422e+08  0.12%   753 62340s
  7361  3783 5.0363e+08   20  547 5.0362e+08 5.0422e+08  0.12%   735 62390s
  7631  3884 5.0362e+08   47  468 5.0362e+08 5.0422e+08  0.12%   713 62422s
  7901  3886 5.0362e+08   39  508 5.0362e+08 5.0422e+08  0.12%   692 62458s
H 8171  3796                    5.036203e+08 5.0421e+08  0.12%   671 62465s
  8171  3862 5.0375e+08   91 2128 5.0362e+08 5.0421e+08  0.12%   671 62543s
  8239  3906 5.0375e+08   94 2131 5.0362e+08 5.0421e+08  0.12%   668 62587s
  8305  3947 5.0375e+08   98 2096 5.0362e+08 5.0421e+08  0.12%   663 62621s
  8368  3993 5.0375e+08  101 2088 5.0362e+08 5.0421e+08  0.12%   659 62653s
  8435  4029 5.0375e+08  105 2086 5.0362e+08 5.0421e+08  0.12%   654 62688s
  8494  4066 5.0375e+08  108 2081 5.0362e+08 5.0421e+08  0.12%   651 62736s
  8550  4107 5.0375e+08  109 2091 5.0362e+08 5.0421e+08  0.12%   647 62767s
  8610  4146 5.0375e+08  111 2080 5.0362e+08 5.0421e+08  0.12%   643 62801s
  8669  4164 5.0375e+08  112 2070 5.0362e+08 5.0421e+08  0.12%   640 62848s
  8707  4219 5.0375e+08  115 2071 5.0362e+08 5.0421e+08  0.12%   637 62879s
  8774  4263 5.0375e+08  118 2070 5.0362e+08 5.0421e+08  0.12%   633 62911s
  8841  4309 5.0375e+08  122 2058 5.0362e+08 5.0421e+08  0.12%   628 62944s
  8909  4352 5.0375e+08  125 2055 5.0362e+08 5.0421e+08  0.12%   624 62976s
  8975  4397 5.0375e+08  128 2048 5.0362e+08 5.0421e+08  0.12%   620 63009s
  9042  4443 5.0375e+08  132 2045 5.0362e+08 5.0421e+08  0.12%   615 63039s
  9110  4485 5.0375e+08  135 2038 5.0362e+08 5.0421e+08  0.12%   611 63071s
  9175  4522 5.0375e+08  138 2036 5.0362e+08 5.0421e+08  0.12%   607 63103s
  9233  4580 5.0375e+08  141 2034 5.0362e+08 5.0421e+08  0.12%   604 63133s
  9298  4645 5.0375e+08  144 2015 5.0362e+08 5.0421e+08  0.12%   600 63160s
  9363  4706 5.0375e+08  147 2016 5.0362e+08 5.0421e+08  0.12%   596 63191s
  9424  4772 5.0375e+08  150 2012 5.0362e+08 5.0421e+08  0.12%   592 63222s
  9490  4790 5.0375e+08  154 2040 5.0362e+08 5.0421e+08  0.12%   589 63316s
  9510  4800 5.0375e+08  155 2038 5.0362e+08 5.0421e+08  0.12%   588 63401s
  9520  4810 5.0375e+08  155 2039 5.0362e+08 5.0421e+08  0.12%   587 63429s
  9530  4820 5.0375e+08  156 2044 5.0362e+08 5.0421e+08  0.12%   587 63460s
  9540  4842 5.0375e+08  156 2030 5.0362e+08 5.0421e+08  0.12%   586 63498s
  9562  4883 5.0375e+08  157 2051 5.0362e+08 5.0421e+08  0.12%   585 63531s
  9603  5107 5.0363e+08   23  588 5.0362e+08 5.0421e+08  0.12%   583 63593s
  9873  5133     cutoff   44      5.0362e+08 5.0421e+08  0.12%   569 63640s
 10015  5209 5.0363e+08   32  538 5.0362e+08 5.0421e+08  0.12%   562 63679s
 10274  5318 5.0362e+08   54  511 5.0362e+08 5.0421e+08  0.12%   550 63713s
 10542  5410 5.0363e+08   31  559 5.0362e+08 5.0421e+08  0.12%   538 63747s
 10808  5592 5.0362e+08   58  541 5.0362e+08 5.0421e+08  0.12%   527 63784s
 11065  5662 5.0375e+08  159 2045 5.0362e+08 5.0421e+08  0.12%   516 63835s
 11135  5725 5.0375e+08  162 2027 5.0362e+08 5.0421e+08  0.12%   513 63868s
 11198  5791 5.0375e+08  164 2009 5.0362e+08 5.0421e+08  0.12%   511 63898s
 11264  5849 5.0375e+08  167 1999 5.0362e+08 5.0421e+08  0.12%   508 63927s
 11322  5904 5.0375e+08  169 2008 5.0362e+08 5.0421e+08  0.12%   506 63963s
 11377  5963 5.0375e+08  172 2011 5.0362e+08 5.0421e+08  0.12%   504 63994s
 11436  6023 5.0374e+08  175 2067 5.0362e+08 5.0421e+08  0.12%   501 64022s
 11496  6090 5.0375e+08  179 2063 5.0362e+08 5.0421e+08  0.12%   499 64052s
 11563  6157 5.0375e+08  182 2040 5.0362e+08 5.0421e+08  0.12%   496 64082s
 11630  6219 5.0375e+08  186 2036 5.0362e+08 5.0421e+08  0.12%   494 64109s
 11692  6285 5.0375e+08  189 2034 5.0362e+08 5.0421e+08  0.12%   491 64138s
 11758  6351 5.0375e+08  192 2037 5.0362e+08 5.0421e+08  0.12%   489 64170s
 11824  6409 5.0374e+08  194 2058 5.0362e+08 5.0421e+08  0.12%   486 64200s
 11882  6469 5.0374e+08  196 2037 5.0362e+08 5.0421e+08  0.12%   484 64235s
 11942  6532 5.0374e+08  198 2030 5.0362e+08 5.0421e+08  0.12%   482 64262s
 12005  6588 5.0374e+08  201 2055 5.0362e+08 5.0421e+08  0.12%   479 64290s
 12061  6652 5.0374e+08  203 2030 5.0362e+08 5.0421e+08  0.12%   478 64317s
 12125  6715 5.0374e+08  207 2026 5.0362e+08 5.0421e+08  0.12%   475 64346s
 12188  6774 5.0374e+08  210 2023 5.0362e+08 5.0421e+08  0.12%   473 64377s
 12247  6836 5.0374e+08  214 2019 5.0362e+08 5.0421e+08  0.12%   471 64417s
 12309  6882 5.0374e+08  216 2027 5.0362e+08 5.0421e+08  0.12%   469 64462s
 12355  6933 5.0374e+08  220 2010 5.0362e+08 5.0421e+08  0.12%   467 64491s
 12406  6976 5.0374e+08  223 2006 5.0362e+08 5.0421e+08  0.12%   466 64523s
 12449  7014 5.0374e+08  226 2023 5.0362e+08 5.0421e+08  0.12%   464 64561s
 12489  7060 5.0374e+08  229 2018 5.0362e+08 5.0421e+08  0.12%   463 64616s
 12535  7105 5.0374e+08  232 2016 5.0362e+08 5.0421e+08  0.12%   461 64650s
 12580  7156 5.0374e+08  235 2005 5.0362e+08 5.0421e+08  0.12%   460 64682s
 12631  7166 5.0374e+08  238 2003 5.0362e+08 5.0421e+08  0.12%   458 64746s
 12641  7183 5.0374e+08  239 2003 5.0362e+08 5.0421e+08  0.12%   458 64794s
 12658  7222 5.0374e+08  239 2037 5.0362e+08 5.0421e+08  0.12%   458 64835s
 12697  7288 5.0374e+08  241 2021 5.0362e+08 5.0421e+08  0.12%   456 64861s
 12763  7357 5.0374e+08  244 2001 5.0362e+08 5.0421e+08  0.12%   454 64888s
 12832  7415 5.0374e+08  247 1998 5.0362e+08 5.0421e+08  0.12%   452 64924s
 12890  7483 5.0374e+08  250 1988 5.0362e+08 5.0421e+08  0.12%   450 64953s
H12958  7483                    5.036207e+08 5.0421e+08  0.12%   448 64981s
 12958  7696 5.0363e+08   22  580 5.0362e+08 5.0421e+08  0.12%   448 65013s
 13228  7849 5.0362e+08   47  497 5.0362e+08 5.0421e+08  0.12%   440 65044s
 13486  8014 5.0362e+08   48  470 5.0362e+08 5.0421e+08  0.12%   433 65074s
 13736  8159 infeasible   48      5.0362e+08 5.0421e+08  0.12%   426 65117s
 13951  8403 5.0363e+08   48  520 5.0362e+08 5.0421e+08  0.12%   421 65148s
 14217  8517 5.0362e+08   75  438 5.0362e+08 5.0421e+08  0.12%   414 65178s
 14455  8748 5.0363e+08   43  547 5.0362e+08 5.0421e+08  0.12%   409 65209s
 14711  8885 5.0362e+08   70  462 5.0362e+08 5.0421e+08  0.12%   403 65242s
 14926  8955 5.0374e+08  253 2000 5.0362e+08 5.0421e+08  0.12%   398 65284s
 14996  9018 5.0374e+08  257 1963 5.0362e+08 5.0421e+08  0.12%   396 65312s
 15059  9079 5.0374e+08  260 1956 5.0362e+08 5.0421e+08  0.12%   394 65339s
 15120  9099 5.0374e+08  262 1954 5.0362e+08 5.0421e+08  0.12%   393 65415s
 15140  9117 5.0374e+08  263 1954 5.0362e+08 5.0421e+08  0.12%   392 65468s
 15158  9139 5.0374e+08  264 1956 5.0362e+08 5.0421e+08  0.12%   392 65503s
 15180  9174 5.0374e+08  264 1952 5.0362e+08 5.0421e+08  0.12%   391 65542s
 15215  9235 5.0374e+08  265 1955 5.0362e+08 5.0421e+08  0.12%   391 65587s
 15276  9269 5.0374e+08  267 1950 5.0362e+08 5.0421e+08  0.12%   389 65637s
 15310  9303 5.0371e+08  270 1958 5.0362e+08 5.0421e+08  0.12%   388 65676s
 15344  9347 5.0374e+08  274 1941 5.0362e+08 5.0421e+08  0.12%   388 65723s
 15388  9411 5.0374e+08  277 1928 5.0362e+08 5.0421e+08  0.12%   387 65757s
 15452  9481 5.0374e+08  281 1940 5.0362e+08 5.0421e+08  0.12%   385 65789s
 15522  9494 5.0374e+08  284 1937 5.0362e+08 5.0421e+08  0.12%   384 65876s
 15535  9516 5.0374e+08  285 1936 5.0362e+08 5.0421e+08  0.12%   383 65917s
 15557  9536 5.0374e+08  285 1943 5.0362e+08 5.0421e+08  0.12%   383 65956s
 15577  9588 5.0374e+08  286 1935 5.0362e+08 5.0421e+08  0.12%   383 66000s
 15629  9658 5.0373e+08  287 1949 5.0362e+08 5.0421e+08  0.12%   381 66034s
 15699  9726 5.0373e+08  290 1904 5.0362e+08 5.0421e+08  0.12%   380 66115s
 15767  9796 5.0373e+08  294 1901 5.0362e+08 5.0421e+08  0.12%   378 66149s
 15837  9866 5.0373e+08  297 1888 5.0362e+08 5.0421e+08  0.12%   377 66184s
 15907  9936 5.0373e+08  301 1906 5.0362e+08 5.0421e+08  0.12%   375 66219s
 15977 10005 5.0373e+08  304 1902 5.0362e+08 5.0421e+08  0.12%   374 66254s
 16046 10075 5.0373e+08  308 1899 5.0362e+08 5.0421e+08  0.12%   372 66284s
 16116 10135 5.0373e+08  311 1896 5.0362e+08 5.0421e+08  0.12%   371 66357s
 16176 10162 5.0373e+08  314 1911 5.0362e+08 5.0421e+08  0.12%   370 66408s
 16203 10193 5.0373e+08  317 1888 5.0362e+08 5.0421e+08  0.12%   369 66445s
 16234 10254 5.0373e+08  321 1884 5.0362e+08 5.0421e+08  0.12%   368 66476s
 16301 10321 5.0373e+08  324 1880 5.0362e+08 5.0421e+08  0.12%   367 66513s
 16371 10383 5.0373e+08  328 1876 5.0362e+08 5.0421e+08  0.12%   366 66545s
 16441 10450 5.0373e+08  331 1866 5.0362e+08 5.0421e+08  0.12%   364 66577s
 16510 10518 5.0373e+08  335 1864 5.0362e+08 5.0421e+08  0.12%   363 66611s
 16578 10587 5.0373e+08  338 1861 5.0362e+08 5.0421e+08  0.12%   361 66646s
 16647 10654 5.0373e+08  342 1857 5.0362e+08 5.0421e+08  0.12%   360 66687s
 16715 10718 5.0373e+08  345 1854 5.0362e+08 5.0421e+08  0.12%   358 66737s
 16783 10734 5.0373e+08  349 1848 5.0362e+08 5.0421e+08  0.12%   357 66780s
 16805 10753 5.0373e+08  349 1849 5.0362e+08 5.0421e+08  0.12%   357 66819s
 16832 10801 5.0373e+08  350 1848 5.0362e+08 5.0421e+08  0.12%   356 66856s
 16888 10867 5.0372e+08  352 1869 5.0362e+08 5.0421e+08  0.12%   355 66886s
 16956 10930 5.0373e+08  356 1838 5.0362e+08 5.0421e+08  0.12%   354 66918s
 17025 10992 5.0373e+08  359 1833 5.0362e+08 5.0421e+08  0.12%   352 66953s
 17094 11052 5.0373e+08  363 1831 5.0362e+08 5.0421e+08  0.12%   351 66985s
 17162 11067 5.0373e+08  366 1827 5.0362e+08 5.0421e+08  0.12%   350 67145s
 17177 11098 5.0373e+08  367 1825 5.0362e+08 5.0421e+08  0.12%   350 67192s
 17210 10777 5.0373e+08  367 1825 5.0362e+08 5.0421e+08  0.12%   349 67224s
 17275 10840 5.0373e+08  371 1819 5.0362e+08 5.0421e+08  0.12%   348 67254s
 17338 10903 5.0373e+08  374 1815 5.0362e+08 5.0421e+08  0.12%   347 67287s
H17401 10903                    5.036902e+08 5.0421e+08  0.10%   345 67312s
 17401 11098 5.0369e+08   37  563 5.0369e+08 5.0421e+08  0.10%   345 67352s
 17669 11284 5.0369e+08   64  522 5.0369e+08 5.0421e+08  0.10%   341 67388s
 17907 11473 5.0369e+08   44  551 5.0369e+08 5.0421e+08  0.10%   337 67423s
 18174 11612     cutoff   69      5.0369e+08 5.0421e+08  0.10%   333 67458s
 18400 11770 5.0370e+08   29  518 5.0369e+08 5.0421e+08  0.10%   330 67490s
 18634 11934 5.0369e+08   53  514 5.0369e+08 5.0421e+08  0.10%   327 67533s
 18859 12152 5.0370e+08   29  553 5.0369e+08 5.0421e+08  0.10%   323 67566s
 19117 12294 5.0369e+08   56  519 5.0369e+08 5.0421e+08  0.10%   319 67600s
 19365 12495 5.0369e+08   27  517 5.0369e+08 5.0421e+08  0.10%   316 67638s
 19629 12694 5.0369e+08   32  520 5.0369e+08 5.0421e+08  0.10%   313 67671s
 19888 12354 5.0373e+08  378 1811 5.0369e+08 5.0421e+08  0.10%   309 67725s
 19953 12400 5.0373e+08  381 1808 5.0369e+08 5.0421e+08  0.10%   309 67764s
 20011 12452 5.0373e+08  385 1801 5.0369e+08 5.0421e+08  0.10%   308 67794s
 20063 12509 5.0373e+08  388 1798 5.0369e+08 5.0421e+08  0.10%   307 67828s
 20120 12571 5.0373e+08  391 1795 5.0369e+08 5.0421e+08  0.10%   307 67856s
 20182 12630 5.0373e+08  395 1790 5.0369e+08 5.0421e+08  0.10%   306 67885s
 20241 12689 5.0373e+08  398 1786 5.0369e+08 5.0421e+08  0.10%   305 67920s
 20300 12745 5.0373e+08  402 1781 5.0369e+08 5.0421e+08  0.10%   304 67948s
 20356 12804 5.0373e+08  405 1752 5.0369e+08 5.0421e+08  0.10%   303 67977s
 20415 12862 5.0373e+08  408 1747 5.0369e+08 5.0421e+08  0.10%   303 68012s
 20473 12920 5.0373e+08  411 1743 5.0369e+08 5.0421e+08  0.10%   302 68042s
 20531 12979 5.0373e+08  415 1739 5.0369e+08 5.0421e+08  0.10%   301 68073s
 20590 13039 5.0373e+08  418 1737 5.0369e+08 5.0421e+08  0.10%   300 68103s
 20650 13096 5.0373e+08  422 1732 5.0369e+08 5.0421e+08  0.10%   299 68133s
 20707 13109 5.0373e+08  425 1730 5.0369e+08 5.0421e+08  0.10%   299 68207s
 20720 12936 5.0373e+08  426 1729 5.0369e+08 5.0421e+08  0.10%   299 68239s
 20776 12998 5.0373e+08  430 1724 5.0369e+08 5.0421e+08  0.10%   298 68270s
 20838 13060 5.0373e+08  433 1721 5.0369e+08 5.0421e+08  0.10%   297 68297s
 20900 13120 5.0373e+08  437 1718 5.0369e+08 5.0421e+08  0.10%   296 68332s
 20960 13185 5.0373e+08  440 1715 5.0369e+08 5.0421e+08  0.10%   296 68364s
 21025 13248 5.0373e+08  444 1712 5.0369e+08 5.0421e+08  0.10%   295 68393s
 21090 13305 5.0373e+08  447 1704 5.0369e+08 5.0421e+08  0.10%   294 68424s
 21151 13370 5.0373e+08  451 1700 5.0369e+08 5.0421e+08  0.10%   294 68457s
 21216 13432 5.0373e+08  454 1697 5.0369e+08 5.0421e+08  0.10%   293 68486s
 21280 13491 5.0373e+08  458 1692 5.0369e+08 5.0421e+08  0.10%   292 68519s
 21345 13551 5.0373e+08  461 1687 5.0369e+08 5.0421e+08  0.10%   291 68563s
 21407 13571 5.0373e+08  465 1677 5.0369e+08 5.0421e+08  0.10%   291 68638s
 21427 13581 5.0373e+08  466 1663 5.0369e+08 5.0421e+08  0.10%   290 68716s
 21437 13592 5.0373e+08  466 1663 5.0369e+08 5.0421e+08  0.10%   290 68754s
 21448 13645 5.0373e+08  467 1662 5.0369e+08 5.0421e+08  0.10%   290 68787s
 21501 13702 5.0373e+08  470 1659 5.0369e+08 5.0421e+08  0.10%   289 68817s
 21558 13759 5.0373e+08  473 1655 5.0369e+08 5.0421e+08  0.10%   289 68865s
 21615 13820 5.0373e+08  477 1650 5.0369e+08 5.0421e+08  0.10%   288 68900s
 21676 13884 5.0373e+08  480 1647 5.0369e+08 5.0421e+08  0.10%   287 68938s
 21741 13950 5.0373e+08  484 1642 5.0369e+08 5.0421e+08  0.10%   286 68979s
 21808 13912 5.0373e+08  487 1639 5.0369e+08 5.0421e+08  0.10%   286 69085s
 21826 13930 5.0373e+08  488 1638 5.0369e+08 5.0421e+08  0.10%   285 69121s
 21845 13950 5.0373e+08  488 1639 5.0369e+08 5.0421e+08  0.10%   285 69157s
 21865 13996 5.0373e+08  489 1636 5.0369e+08 5.0421e+08  0.10%   285 69191s
 21911 14052 5.0373e+08  491 1634 5.0369e+08 5.0421e+08  0.10%   285 69221s
 21967 14115 5.0373e+08  495 1617 5.0369e+08 5.0421e+08  0.10%   284 69259s
 22030 14183 5.0373e+08  498 1614 5.0369e+08 5.0421e+08  0.10%   283 69290s
 22098 14251 5.0373e+08  502 1610 5.0369e+08 5.0421e+08  0.10%   282 69323s
 22166 14318 5.0373e+08  505 1592 5.0369e+08 5.0421e+08  0.10%   282 69359s
 22233 14388 5.0373e+08  509 1588 5.0369e+08 5.0421e+08  0.10%   281 69393s
 22303 14448 5.0373e+08  512 1585 5.0369e+08 5.0421e+08  0.10%   280 69458s
 22363 14464 5.0373e+08  515 1581 5.0369e+08 5.0421e+08  0.10%   279 69535s
 22379 14480 5.0373e+08  516 1580 5.0369e+08 5.0421e+08  0.10%   279 69568s
 22395 14500 5.0373e+08  516 1580 5.0369e+08 5.0421e+08  0.10%   279 69602s
 22415 14549 5.0373e+08  517 1579 5.0369e+08 5.0421e+08  0.10%   279 69634s
 22464 14605 5.0373e+08  519 1577 5.0369e+08 5.0421e+08  0.10%   278 69664s
 22520 14675 5.0373e+08  523 1577 5.0369e+08 5.0421e+08  0.10%   277 69694s
 22590 14745 5.0373e+08  526 1576 5.0369e+08 5.0421e+08  0.10%   277 69727s
 22660 14813 5.0373e+08  530 1569 5.0369e+08 5.0421e+08  0.10%   276 69761s
 22728 14879 5.0373e+08  533 1565 5.0369e+08 5.0421e+08  0.10%   275 69794s
 22794 14949 5.0373e+08  537 1560 5.0369e+08 5.0421e+08  0.10%   275 69827s
 22864 15018 5.0373e+08  540 1556 5.0369e+08 5.0421e+08  0.10%   274 69858s
 22933 15085 5.0373e+08  544 1550 5.0369e+08 5.0421e+08  0.10%   273 69890s
 23000 15155 5.0373e+08  547 1543 5.0369e+08 5.0421e+08  0.10%   272 69921s
H23070 15155                    5.037047e+08 5.0421e+08  0.10%   271 69951s
 23070 15271 5.0371e+08   59  496 5.0370e+08 5.0421e+08  0.10%   271 69988s
 23213 15475 5.0370e+08   70  462 5.0370e+08 5.0421e+08  0.10%   270 70022s
 23483 15721 5.0371e+08   44  510 5.0370e+08 5.0421e+08  0.10%   268 70052s
 23753 15828 5.0371e+08   37  501 5.0370e+08 5.0421e+08  0.10%   265 70086s
 23981 15234 5.0371e+08   60  453 5.0370e+08 5.0421e+08  0.10%   263 70118s
 24221 15419 5.0371e+08   34  513 5.0370e+08 5.0421e+08  0.10%   262 70147s
 24470 15492 5.0371e+08   53  493 5.0370e+08 5.0421e+08  0.10%   260 70197s
 24592 15022 5.0371e+08   65  447 5.0370e+08 5.0421e+08  0.10%   259 70229s
 24861 15094 5.0371e+08   81  393 5.0370e+08 5.0421e+08  0.10%   257 70259s
 25063 15154 5.0371e+08   28  528 5.0370e+08 5.0421e+08  0.10%   256 70293s
 25261 15282     cutoff   34      5.0370e+08 5.0421e+08  0.10%   255 70326s
 25481 15369     cutoff   31      5.0370e+08 5.0421e+08  0.10%   253 70359s
 25596 15440 5.0371e+08   32  531 5.0370e+08 5.0421e+08  0.10%   253 70395s
 25721 15634 5.0371e+08   35  534 5.0370e+08 5.0421e+08  0.10%   252 70427s
 25966 15758 5.0371e+08   38  524 5.0370e+08 5.0421e+08  0.10%   251 70464s
H26223 15758                    5.037060e+08 5.0421e+08  0.10%   249 70472s
 26223 15593 5.0373e+08  551 1537 5.0371e+08 5.0421e+08  0.10%   249 70501s
 26293 15646 5.0373e+08  554 1531 5.0371e+08 5.0421e+08  0.10%   248 70539s
 26349 15701 5.0373e+08  558 1526 5.0371e+08 5.0421e+08  0.10%   248 70568s
 26404 15758 5.0373e+08  561 1523 5.0371e+08 5.0421e+08  0.10%   248 70595s
 26461 15768 5.0373e+08  565 1519 5.0371e+08 5.0421e+08  0.10%   247 70683s
 26471 15778 5.0373e+08  565 1519 5.0371e+08 5.0421e+08  0.10%   247 70752s
 26481 15788 5.0373e+08  566 1518 5.0371e+08 5.0421e+08  0.10%   247 70782s
 26491 15798 5.0373e+08  566 1518 5.0371e+08 5.0421e+08  0.10%   247 70866s
 26501 15818 5.0373e+08  567 1517 5.0371e+08 5.0421e+08  0.10%   247 70955s
 26521 15846 5.0373e+08  567 1517 5.0371e+08 5.0421e+08  0.10%   247 70991s
 26549 15874 5.0373e+08  568 1516 5.0371e+08 5.0421e+08  0.10%   246 71027s
 26577 15902 5.0373e+08  568 1516 5.0371e+08 5.0421e+08  0.10%   246 71065s
 26605 15934 5.0373e+08  569 1515 5.0371e+08 5.0421e+08  0.10%   246 71108s
 26637 15973 5.0373e+08  569 1515 5.0371e+08 5.0421e+08  0.10%   246 71151s
 26676 16034 5.0373e+08  570 1514 5.0371e+08 5.0421e+08  0.10%   245 71197s
 26738 16091 5.0373e+08  573 1511 5.0371e+08 5.0421e+08  0.10%   245 71233s
 26801 16153 5.0373e+08  577 1507 5.0371e+08 5.0421e+08  0.10%   244 71272s
 26865 16211 5.0373e+08  580 1503 5.0371e+08 5.0421e+08  0.10%   244 71308s
 26928 16263 5.0373e+08  584 1499 5.0371e+08 5.0421e+08  0.10%   243 71351s
 26990 16324 5.0373e+08  587 1497 5.0371e+08 5.0421e+08  0.10%   243 71393s
 27051 16392 5.0373e+08  591 1491 5.0371e+08 5.0421e+08  0.10%   243 71427s
 27119 16457 5.0373e+08  594 1488 5.0371e+08 5.0421e+08  0.10%   242 71464s
 27184 16523 5.0373e+08  598 1482 5.0371e+08 5.0421e+08  0.10%   242 71495s
 27250 16588 5.0373e+08  601 1478 5.0371e+08 5.0421e+08  0.10%   241 71531s
 27315 16652 5.0373e+08  605 1472 5.0371e+08 5.0421e+08  0.10%   241 71566s
 27381 16715 5.0373e+08  608 1469 5.0371e+08 5.0421e+08  0.10%   240 71602s
 27444 16777 5.0373e+08  612 1465 5.0371e+08 5.0421e+08  0.10%   240 71638s
 27508 16841 5.0373e+08  615 1462 5.0371e+08 5.0421e+08  0.10%   239 71672s
 27574 16905 5.0373e+08  619 1457 5.0371e+08 5.0421e+08  0.10%   239 71705s
 27640 16964 5.0373e+08  622 1454 5.0371e+08 5.0421e+08  0.10%   238 71739s
 27701 17018 5.0373e+08  626 1449 5.0371e+08 5.0421e+08  0.10%   238 71781s
 27761 17027 5.0373e+08  629 1447 5.0371e+08 5.0421e+08  0.10%   237 71851s
 27776 17042 5.0373e+08  630 1445 5.0371e+08 5.0421e+08  0.10%   237 71891s
 27795 17058 5.0373e+08  630 1446 5.0371e+08 5.0421e+08  0.10%   237 71929s
 27819 17121 5.0373e+08  631 1445 5.0371e+08 5.0421e+08  0.10%   237 71963s
 27886 17179 5.0373e+08  634 1442 5.0371e+08 5.0421e+08  0.10%   237 71996s
 27950 17237 5.0373e+08  638 1436 5.0371e+08 5.0421e+08  0.10%   236 72035s
 28015 17284 5.0373e+08  641 1433 5.0371e+08 5.0421e+08  0.10%   236 72095s
 28068 17346 5.0373e+08  644 1428 5.0371e+08 5.0421e+08  0.10%   235 72131s
 28137 17407 5.0373e+08  647 1426 5.0371e+08 5.0421e+08  0.10%   235 72162s
 28203 17468 5.0373e+08  651 1421 5.0371e+08 5.0421e+08  0.10%   234 72192s
 28270 17527 5.0373e+08  654 1417 5.0371e+08 5.0421e+08  0.10%   234 72229s
 28335 17591 5.0373e+08  658 1414 5.0371e+08 5.0421e+08  0.10%   234 72264s
 28401 17657 5.0373e+08  661 1409 5.0371e+08 5.0421e+08  0.10%   233 72303s
 28467 17719 5.0373e+08  665 1403 5.0371e+08 5.0421e+08  0.10%   233 72337s
 28531 17784 5.0373e+08  668 1399 5.0371e+08 5.0421e+08  0.10%   232 72369s
 28596 17851 5.0373e+08  672 1392 5.0371e+08 5.0421e+08  0.10%   232 72404s
 28663 17913 5.0373e+08  675 1389 5.0371e+08 5.0421e+08  0.10%   231 72440s
 28727 17973 5.0373e+08  679 1385 5.0371e+08 5.0421e+08  0.10%   231 72470s
 28787 18030 5.0373e+08  682 1386 5.0371e+08 5.0421e+08  0.10%   231 72502s
 28850 18084 5.0373e+08  686 1375 5.0371e+08 5.0421e+08  0.10%   230 72533s
 28908 18140 5.0373e+08  689 1372 5.0371e+08 5.0421e+08  0.10%   230 72577s
 28968 18195 5.0373e+08  693 1369 5.0371e+08 5.0421e+08  0.10%   229 72604s
 29031 18254 5.0373e+08  696 1365 5.0371e+08 5.0421e+08  0.10%   229 72648s
 29092 18318 5.0373e+08  700 1361 5.0371e+08 5.0421e+08  0.10%   229 72686s
 29156 18375 5.0373e+08  703 1357 5.0371e+08 5.0421e+08  0.10%   228 72751s
 29213 18386 5.0373e+08  706 1353 5.0371e+08 5.0421e+08  0.10%   228 72827s
 29224 18399 5.0373e+08  707 1351 5.0371e+08 5.0421e+08  0.10%   228 72867s
 29237 18414 5.0373e+08  707 1351 5.0371e+08 5.0421e+08  0.10%   228 72901s
 29254 18459 5.0373e+08  708 1352 5.0371e+08 5.0421e+08  0.10%   228 72940s
 29303 18512 5.0373e+08  710 1348 5.0371e+08 5.0421e+08  0.10%   227 72970s
 29356 18571 5.0373e+08  714 1343 5.0371e+08 5.0421e+08  0.10%   227 73014s
 29415 18592 5.0373e+08  717 1339 5.0371e+08 5.0421e+08  0.10%   227 73083s
 29436 18613 5.0373e+08  717 1338 5.0371e+08 5.0421e+08  0.10%   227 73120s
 29457 18637 5.0373e+08  718 1336 5.0371e+08 5.0421e+08  0.10%   226 73186s
 29481 18684 5.0373e+08  718 1338 5.0371e+08 5.0421e+08  0.10%   226 73256s
 29528 18740 5.0373e+08  720 1335 5.0371e+08 5.0421e+08  0.10%   226 73286s
 29584 18793 5.0373e+08  724 1330 5.0371e+08 5.0421e+08  0.10%   226 73325s
 29639 18851 5.0373e+08  727 1328 5.0371e+08 5.0421e+08  0.10%   225 73358s
 29697 18910 5.0373e+08  731 1321 5.0371e+08 5.0421e+08  0.10%   225 73390s
 29756 18969 5.0373e+08  734 1317 5.0371e+08 5.0421e+08  0.10%   224 73452s
 29815 18982 5.0373e+08  737 1314 5.0371e+08 5.0421e+08  0.10%   224 73533s
 29830 18734 5.0373e+08  738 1314 5.0371e+08 5.0421e+08  0.10%   224 73582s
 29897 18790 5.0373e+08  741 1309 5.0371e+08 5.0421e+08  0.10%   223 73613s
 29959 18820 5.0373e+08  745 1305 5.0371e+08 5.0421e+08  0.10%   223 73688s
 29989 18564 5.0373e+08  746 1320 5.0371e+08 5.0421e+08  0.10%   223 73725s
 30052 18619 5.0373e+08  750 1299 5.0371e+08 5.0421e+08  0.10%   223 73757s
 30114 18679 5.0373e+08  753 1296 5.0371e+08 5.0421e+08  0.10%   222 73789s
 30178 18735 5.0373e+08  757 1294 5.0371e+08 5.0421e+08  0.10%   222 73821s
 30240 18799 5.0373e+08  760 1288 5.0371e+08 5.0421e+08  0.10%   221 73900s
H30309 18799                    5.037094e+08 5.0421e+08  0.10%   221 73930s
 30309 18993     cutoff   45      5.0371e+08 5.0421e+08  0.10%   221 73960s
 30573 19150     cutoff   34      5.0371e+08 5.0421e+08  0.10%   220 73989s
 30808 19296     cutoff   36      5.0371e+08 5.0421e+08  0.10%   219 74019s
 31039 19420     cutoff   38      5.0371e+08 5.0421e+08  0.10%   218 74053s
 31256 19602     cutoff   40      5.0371e+08 5.0421e+08  0.10%   217 74090s
 31500 19733 5.0371e+08   49  498 5.0371e+08 5.0421e+08  0.10%   215 74122s
 31738 19911 5.0371e+08   36  522 5.0371e+08 5.0421e+08  0.10%   215 74156s
 31971 20046 5.0371e+08   63  480 5.0371e+08 5.0421e+08  0.10%   214 74189s
 32217 20232 5.0372e+08   33  540 5.0371e+08 5.0421e+08  0.10%   213 74222s
 32475 20353 5.0371e+08   60  519 5.0371e+08 5.0421e+08  0.10%   211 74254s
 32703 20463 5.0372e+08   23  515 5.0371e+08 5.0421e+08  0.10%   210 74289s
 32868 20643 5.0371e+08   31  552 5.0371e+08 5.0421e+08  0.10%   210 74321s
 33121 20753     cutoff   42      5.0371e+08 5.0421e+08  0.10%   209 74351s
 33338 20864 5.0371e+08   49  537 5.0371e+08 5.0421e+08  0.10%   208 74389s
 33527 21040     cutoff   55      5.0371e+08 5.0421e+08  0.10%   207 74421s
 33770 21184 5.0371e+08   34  518 5.0371e+08 5.0421e+08  0.10%   206 74454s
 34007 21282 5.0371e+08   31  510 5.0371e+08 5.0421e+08  0.10%   205 74496s
 34218 21466 5.0371e+08   41  496 5.0371e+08 5.0421e+08  0.10%   205 74534s
 34485 21667 5.0371e+08   27  255 5.0371e+08 5.0421e+08  0.10%   204 74617s
 34895 21881 5.0371e+08   28  230 5.0371e+08 5.0421e+08  0.10%   203 74697s
 35257 21912     cutoff   32      5.0371e+08 5.0421e+08  0.10%   201 74789s
 35316 22111     cutoff   32      5.0371e+08 5.0421e+08  0.10%   201 74822s
 35726 22365 5.0371e+08   33  220 5.0371e+08 5.0421e+08  0.10%   200 74849s
 36128 22600 5.0371e+08   43  201 5.0371e+08 5.0420e+08  0.10%   198 74879s
 36538 22829 5.0371e+08   18  247 5.0371e+08 5.0420e+08  0.10%   197 74915s
 36914 23038 5.0371e+08   43  189 5.0371e+08 5.0420e+08  0.10%   195 74964s
 37283 23019     cutoff   20      5.0371e+08 5.0420e+08  0.10%   194 74995s
 37673 23020 5.0371e+08   15  217 5.0371e+08 5.0420e+08  0.10%   193 75178s
 37674 23021 5.0371e+08   15  640 5.0371e+08 5.0420e+08  0.10%   193 75191s
 37675 23022 5.0371e+08   15  647 5.0371e+08 5.0420e+08  0.10%   193 75198s
 37676 23022 5.0371e+08   15  634 5.0371e+08 5.0420e+08  0.10%   193 75201s
 37677 23023 5.0371e+08   15  673 5.0371e+08 5.0420e+08  0.10%   193 75209s
 37678 23024 5.0371e+08   15  675 5.0371e+08 5.0420e+08  0.10%   193 75212s
 37679 23024 5.0371e+08   15  910 5.0371e+08 5.0420e+08  0.10%   193 75295s
 37680 23027 5.0371e+08    1  910 5.0371e+08 5.0420e+08  0.10%   196 75366s
 37683 23030 5.0371e+08    3  351 5.0371e+08 5.0420e+08  0.10%   197 75373s
 37693 23031     cutoff    5      5.0371e+08 5.0420e+08  0.10%   197 75377s
 37701 23041 5.0371e+08    6  331 5.0371e+08 5.0420e+08  0.10%   197 75380s
 37724 23041 5.0371e+08    7  305 5.0371e+08 5.0420e+08  0.10%   197 75391s
 37734 23042 5.0371e+08    9  296 5.0371e+08 5.0420e+08  0.10%   197 75398s
 37748 23046 5.0371e+08   10  295 5.0371e+08 5.0420e+08  0.10%   197 75431s
 37771 22831 5.0371e+08   13  268 5.0371e+08 5.0420e+08  0.10%   197 75441s
 37817 22823 5.0371e+08   18  252 5.0371e+08 5.0420e+08  0.10%   197 75460s
 37829 22826 5.0371e+08   19  251 5.0371e+08 5.0420e+08  0.10%   197 75501s
 37842 22864 5.0371e+08   20  230 5.0371e+08 5.0420e+08  0.10%   197 75532s
 37887 22841 5.0371e+08   21  230 5.0371e+08 5.0420e+08  0.10%   197 75551s
 38167 22823 5.0371e+08   18  264 5.0371e+08 5.0420e+08  0.10%   196 75618s
 38358 22681     cutoff   17      5.0371e+08 5.0420e+08  0.10%   195 75699s
H38619 22376                    5.037101e+08 5.0420e+08  0.10%   195 75701s
 38619 22421 5.0373e+08  764 1283 5.0371e+08 5.0420e+08  0.10%   195 75745s
 38683 22486 5.0373e+08  767 1283 5.0371e+08 5.0420e+08  0.10%   194 75775s
 38752 22546 5.0373e+08  771 1275 5.0371e+08 5.0420e+08  0.10%   194 75805s
 38814 22601 5.0373e+08  774 1276 5.0371e+08 5.0420e+08  0.10%   194 75836s
 38876 22663 5.0373e+08  778 1268 5.0371e+08 5.0420e+08  0.10%   194 75867s
 38944 22723 5.0373e+08  781 1264 5.0371e+08 5.0420e+08  0.10%   193 75897s
 39011 22778 5.0373e+08  785 1260 5.0371e+08 5.0420e+08  0.10%   193 75931s
 39070 22797 5.0373e+08  788 1256 5.0371e+08 5.0420e+08  0.10%   193 76019s
 39089 22807 5.0373e+08  789 1254 5.0371e+08 5.0420e+08  0.10%   193 76085s
 39099 22826 5.0373e+08  789 1254 5.0371e+08 5.0420e+08  0.10%   193 76121s
 39118 22863 5.0373e+08  790 1252 5.0371e+08 5.0420e+08  0.10%   193 76153s
 39157 22731 5.0373e+08  794 1250 5.0371e+08 5.0420e+08  0.10%   193 76187s
 39222 22779 5.0373e+08  797 1246 5.0371e+08 5.0420e+08  0.10%   192 76222s
 39272 22840 5.0373e+08  801 1240 5.0371e+08 5.0420e+08  0.10%   192 76255s
 39333 22905 5.0373e+08  804 1235 5.0371e+08 5.0420e+08  0.10%   192 76286s
 39398 22970 5.0373e+08  808 1230 5.0371e+08 5.0420e+08  0.10%   192 76322s
 39463 23031 5.0373e+08  811 1227 5.0371e+08 5.0420e+08  0.10%   192 76353s
 39526 23086 5.0373e+08  814 1224 5.0371e+08 5.0420e+08  0.10%   191 76386s
 39585 23140 5.0373e+08  818 1220 5.0371e+08 5.0420e+08  0.10%   191 76420s
 39642 23194 5.0373e+08  821 1221 5.0371e+08 5.0420e+08  0.10%   191 76455s
 39700 23248 5.0373e+08  824 1215 5.0371e+08 5.0420e+08  0.10%   191 76486s
 39757 23299 5.0373e+08  827 1212 5.0371e+08 5.0420e+08  0.10%   191 76516s
 39816 23352 5.0373e+08  830 1209 5.0371e+08 5.0420e+08  0.10%   190 76546s
 39880 23408 5.0373e+08  834 1205 5.0371e+08 5.0420e+08  0.10%   190 76578s
 39938 23461 5.0373e+08  837 1199 5.0371e+08 5.0420e+08  0.10%   190 76614s
 40000 23519 5.0373e+08  840 1194 5.0371e+08 5.0420e+08  0.10%   190 76644s
 40060 23581 5.0373e+08  844 1189 5.0371e+08 5.0420e+08  0.10%   190 76675s
 40122 23635 5.0373e+08  847 1188 5.0371e+08 5.0420e+08  0.10%   189 76721s
 40178 23696 5.0373e+08  851 1181 5.0371e+08 5.0420e+08  0.10%   189 76756s
 40241 23754 5.0373e+08  854 1176 5.0371e+08 5.0420e+08  0.10%   189 76790s
 40303 23810 5.0373e+08  858 1170 5.0371e+08 5.0420e+08  0.10%   189 76830s
 40361 23866 5.0373e+08  861 1164 5.0371e+08 5.0420e+08  0.10%   189 76877s
 40417 23912 5.0373e+08  865 1160 5.0371e+08 5.0420e+08  0.10%   188 76912s
 40463 23975 5.0373e+08  867 1156 5.0371e+08 5.0420e+08  0.10%   188 76942s
 40526 24035 5.0373e+08  871 1150 5.0371e+08 5.0420e+08  0.10%   188 76972s
 40586 24094 5.0373e+08  874 1146 5.0371e+08 5.0420e+08  0.10%   188 77004s
 40645 24155 5.0373e+08  878 1141 5.0371e+08 5.0420e+08  0.10%   188 77035s
 40706 24204 5.0373e+08  881 1137 5.0371e+08 5.0420e+08  0.10%   187 77074s
 40755 24262 5.0373e+08  885 1131 5.0371e+08 5.0420e+08  0.10%   187 77106s
 40813 24319 5.0373e+08  888 1127 5.0371e+08 5.0420e+08  0.10%   187 77136s
 40870 24339 5.0373e+08  892 1120 5.0371e+08 5.0420e+08  0.10%   187 77208s
 40890 24354 5.0373e+08  893 1118 5.0371e+08 5.0420e+08  0.10%   187 77264s
 40905 24395 5.0373e+08  893 1118 5.0371e+08 5.0420e+08  0.10%   187 77303s
 40906 15256 5.0373e+08  894 1118 5.0371e+08 5.0420e+08  0.10%   187 77308s
 40946 13992     cutoff  896      5.0371e+08 5.0420e+08  0.10%   187 77329s
 41009 13978     cutoff  894      5.0371e+08 5.0420e+08  0.10%   186 77360s
 41049 14014 5.0378e+08   31 2077 5.0371e+08 5.0420e+08  0.10%   186 77405s
 41086 14053 5.0378e+08   33 2095 5.0371e+08 5.0420e+08  0.10%   186 77451s
 41127 14097 5.0378e+08   38 2043 5.0371e+08 5.0420e+08  0.10%   187 77484s
 41171 14105 5.0377e+08   45 2049 5.0371e+08 5.0420e+08  0.10%   187 77583s
 41179 14123 5.0377e+08   46 2059 5.0371e+08 5.0420e+08  0.10%   187 77637s
 41198 14148 5.0377e+08   47 2046 5.0371e+08 5.0420e+08  0.10%   187 77674s
 41223 14166 5.0377e+08   48 2059 5.0371e+08 5.0420e+08  0.10%   187 77705s
 41245 14183 5.0377e+08   49 2084 5.0371e+08 5.0420e+08  0.10%   186 77745s
 41277 14216 5.0377e+08   50 2093 5.0371e+08 5.0420e+08  0.10%   186 77782s
 41313 14228 5.0376e+08   53 2091 5.0371e+08 5.0420e+08  0.10%   186 77850s
 41330 14258 5.0376e+08   55 2075 5.0371e+08 5.0420e+08  0.10%   186 77886s
 41369 14271     cutoff  348      5.0371e+08 5.0420e+08  0.10%   186 77945s
 41387 14283 5.0376e+08   59 2052 5.0371e+08 5.0420e+08  0.10%   186 77997s
 41403 14297 infeasible  356      5.0371e+08 5.0420e+08  0.10%   186 78036s
 41423 14323 5.0376e+08   58 2078 5.0371e+08 5.0420e+08  0.10%   186 78075s
 41453 14333     cutoff   16      5.0371e+08 5.0420e+08  0.10%   186 78108s
 41474 14355 5.0376e+08   59 2061 5.0371e+08 5.0420e+08  0.10%   186 78148s
 41509 14380 5.0379e+08   31 2110 5.0371e+08 5.0420e+08  0.10%   186 78190s
 41549 14402 infeasible   30      5.0371e+08 5.0420e+08  0.10%   186 78235s
 41591 14421 5.0378e+08   38 2092 5.0371e+08 5.0420e+08  0.10%   186 78279s
 41626 14449 5.0377e+08    9 4318 5.0371e+08 5.0420e+08  0.10%   186 78313s
 41665 14484 5.0374e+08   12 3509 5.0371e+08 5.0420e+08  0.10%   186 78370s
 41720 14509     cutoff   13      5.0371e+08 5.0420e+08  0.10%   186 78423s
 41753 14541 5.0411e+08    6 4852 5.0371e+08 5.0420e+08  0.10%   186 78455s
 41794 14573 5.0410e+08   10 3773 5.0371e+08 5.0420e+08  0.10%   186 78488s
 41839 14601 5.0405e+08   13 3503 5.0371e+08 5.0420e+08  0.10%   186 78522s
 41878 14650 5.0403e+08   16 3235 5.0371e+08 5.0420e+08  0.10%   186 78558s
 41943 14692 5.0386e+08   22 2895 5.0371e+08 5.0420e+08  0.10%   186 78598s
 42006 14727 5.0376e+08   26 2838 5.0371e+08 5.0420e+08  0.10%   186 78647s
 42055 14758 5.0379e+08   25 2844 5.0371e+08 5.0420e+08  0.10%   186 78686s
 42108 14776     cutoff   27      5.0371e+08 5.0420e+08  0.10%   186 78735s
 42148 14803 5.0377e+08   27 2669 5.0371e+08 5.0420e+08  0.10%   186 78776s
 42185 14828 5.0374e+08   82 2195 5.0371e+08 5.0420e+08  0.10%   186 78815s
 42224 14835 5.0374e+08   89 2245 5.0371e+08 5.0420e+08  0.10%   186 78858s
 42266 14843 5.0376e+08   29 2496 5.0371e+08 5.0420e+08  0.10%   186 78904s
 42295 14847 5.0374e+08   95 2109 5.0371e+08 5.0420e+08  0.10%   186 78953s
 42313 14855 5.0375e+08   30 2503 5.0371e+08 5.0420e+08  0.10%   186 79025s
 42325 14857     cutoff   97      5.0371e+08 5.0420e+08  0.10%   186 79076s
 42346 14872 5.0376e+08   27 2635 5.0371e+08 5.0420e+08  0.10%   186 79133s
 42363 14884 5.0377e+08   27 2852 5.0371e+08 5.0420e+08  0.10%   186 79172s
 42381 14911 infeasible   30      5.0371e+08 5.0420e+08  0.10%   187 79224s
 42412 14935 5.0377e+08   27 2688 5.0371e+08 5.0420e+08  0.10%   187 79269s
 42442 14954 5.0377e+08   29 2514 5.0371e+08 5.0420e+08  0.10%   187 79313s
 42475 14970 infeasible   21      5.0371e+08 5.0420e+08  0.10%   187 79360s
 42507 14970     cutoff   30      5.0371e+08 5.0420e+08  0.10%   187 79414s
 42533 14967 5.0378e+08   29 2202 5.0371e+08 5.0420e+08  0.10%   187 79476s
 42545 14972 5.0378e+08   31 1988 5.0371e+08 5.0420e+08  0.10%   187 79530s
 42562 14979 5.0378e+08   37 1946 5.0371e+08 5.0420e+08  0.10%   187 79571s
 42577 15004 5.0377e+08   44 1984 5.0371e+08 5.0420e+08  0.10%   188 79614s
 42608 15022 5.0377e+08   48 2012 5.0371e+08 5.0420e+08  0.10%   188 79657s
 42632 15032 5.0376e+08   54 1968 5.0371e+08 5.0420e+08  0.10%   188 79706s
 42656 15048 5.0376e+08   61 1924 5.0371e+08 5.0420e+08  0.10%   188 79762s
 42684 15067 5.0375e+08   63 2004 5.0371e+08 5.0420e+08  0.10%   188 79825s
 42713 15082 5.0375e+08   70 1951 5.0371e+08 5.0420e+08  0.10%   189 79888s
 42738 15098 5.0375e+08   77 1965 5.0371e+08 5.0420e+08  0.10%   189 79949s
 42758 15112 5.0375e+08   84 2010 5.0371e+08 5.0420e+08  0.10%   189 79990s
 42779 15128 5.0375e+08   91 2059 5.0371e+08 5.0420e+08  0.10%   190 80056s
 42803 15161 5.0374e+08   98 1997 5.0371e+08 5.0420e+08  0.10%   190 80100s
 42836 15200 5.0374e+08  105 1991 5.0371e+08 5.0420e+08  0.10%   190 80147s
 42877 15232 5.0374e+08  112 1982 5.0371e+08 5.0420e+08  0.10%   190 80192s
 42913 15254 5.0374e+08  117 1870 5.0371e+08 5.0420e+08  0.10%   191 80235s
 42950 15276 5.0374e+08  119 1839 5.0371e+08 5.0420e+08  0.10%   191 80279s
 42983 15282 5.0374e+08  120 1792 5.0371e+08 5.0420e+08  0.10%   191 80329s
 43013 15298 5.0384e+08   25 2579 5.0371e+08 5.0420e+08  0.10%   191 80394s
 43033 15322 5.0378e+08   26 2699 5.0371e+08 5.0420e+08  0.10%   192 80455s
 43063 15329 5.0377e+08   29 2500 5.0371e+08 5.0420e+08  0.10%   192 80500s
 43086 15334 5.0375e+08   32 2484 5.0371e+08 5.0420e+08  0.10%   192 80565s
 43107 15344 5.0375e+08   32 2482 5.0371e+08 5.0420e+08  0.10%   192 80621s
 43129 15347 5.0375e+08   31 2505 5.0371e+08 5.0420e+08  0.10%   192 80686s
 43162 15353 5.0376e+08   31 2491 5.0371e+08 5.0420e+08  0.10%   193 80757s
 43182 15358 infeasible   32      5.0371e+08 5.0420e+08  0.10%   193 80823s
 43201 15368     cutoff   32      5.0371e+08 5.0420e+08  0.10%   193 80892s
 43235 15374 5.0380e+08   21 2779 5.0371e+08 5.0420e+08  0.10%   194 80939s
 43264 15375 5.0377e+08   22 2775 5.0371e+08 5.0420e+08  0.10%   194 81006s
 43299 15381 5.0378e+08    9 4244 5.0371e+08 5.0420e+08  0.10%   194 81059s
 43315 15397 5.0378e+08   10 3643 5.0371e+08 5.0420e+08  0.10%   195 81106s
 43339 15408     cutoff   12      5.0371e+08 5.0420e+08  0.10%   195 81166s
 43366 15419 5.0386e+08   18 2809 5.0371e+08 5.0420e+08  0.10%   195 81214s
 43385 15422 5.0376e+08   24 2678 5.0371e+08 5.0420e+08  0.10%   195 81262s
 43404 15433     cutoff   25      5.0371e+08 5.0420e+08  0.10%   196 81325s
 43431 15442 5.0413e+08   10 3310 5.0371e+08 5.0420e+08  0.10%   196 81393s
 43446 15447 5.0408e+08   15 3069 5.0371e+08 5.0420e+08  0.10%   196 81457s
 43469 15451 5.0391e+08   21 2730 5.0371e+08 5.0420e+08  0.10%   196 81540s
 43489 15453 5.0385e+08   24 2654 5.0371e+08 5.0420e+08  0.10%   196 81604s
 43503 15464 5.0382e+08   25 2718 5.0371e+08 5.0420e+08  0.10%   197 81657s
 43522 15473 5.0379e+08   26 2721 5.0371e+08 5.0420e+08  0.10%   197 81720s
 43541 15489 5.0379e+08   27 2542 5.0371e+08 5.0420e+08  0.10%   197 81780s
 43561 15510 5.0378e+08   32 2549 5.0371e+08 5.0420e+08  0.10%   197 81829s
 43588 15519 5.0383e+08   20 2828 5.0371e+08 5.0420e+08  0.10%   198 81881s
 43618 15523 5.0377e+08   32 2571 5.0371e+08 5.0420e+08  0.10%   198 81938s
 43635 15537 5.0377e+08   25 2681 5.0371e+08 5.0420e+08  0.10%   198 82008s
 43659 15544 5.0377e+08   31 2535 5.0371e+08 5.0420e+08  0.10%   198 82067s
 43684 15558 5.0376e+08   33 2140 5.0371e+08 5.0420e+08  0.10%   198 82136s
 43716 15565 5.0376e+08   34 2126 5.0371e+08 5.0420e+08  0.10%   199 82209s
 43749 15581 5.0376e+08   41 2115 5.0371e+08 5.0420e+08  0.10%   200 82276s
 43781 15583 5.0375e+08   48 2122 5.0371e+08 5.0420e+08  0.10%   200 82326s
 43815 15591 5.0375e+08   55 1947 5.0371e+08 5.0420e+08  0.10%   200 82399s
 43845 15596 5.0375e+08   62 1930 5.0371e+08 5.0420e+08  0.10%   201 82530s
 43854 15611 5.0375e+08   63 1911 5.0371e+08 5.0420e+08  0.10%   201 82605s
 43871 15617 5.0375e+08   64 1908 5.0371e+08 5.0420e+08  0.10%   201 82704s
 43897 15508 5.0375e+08   65 1912 5.0371e+08 5.0420e+08  0.10%   202 82757s
H43943 15508                    5.037429e+08 5.0420e+08  0.09%   202 82783s
 43943 15673 5.0375e+08   34  507 5.0374e+08 5.0420e+08  0.09%   202 82813s
 44199 15785 5.0374e+08   57  477 5.0374e+08 5.0420e+08  0.09%   201 82848s
 44413 15904     cutoff   47      5.0374e+08 5.0420e+08  0.09%   201 82889s
 44652 15995 5.0374e+08   50  421 5.0374e+08 5.0420e+08  0.09%   200 82920s
 44892 16121 5.0374e+08   45  513 5.0374e+08 5.0420e+08  0.09%   199 82955s
 45135 16257 5.0374e+08   45  563 5.0374e+08 5.0420e+08  0.09%   199 82998s
 45357 16441 5.0375e+08   29  519 5.0374e+08 5.0420e+08  0.09%   198 83031s
 45615 16658 5.0374e+08   56  485 5.0374e+08 5.0420e+08  0.09%   197 83074s
 45885 16771 5.0375e+08   40  521 5.0374e+08 5.0420e+08  0.09%   197 83176s
 46080 16881     cutoff   59      5.0374e+08 5.0420e+08  0.09%   196 83234s
 46309 16987 5.0375e+08   37  532 5.0374e+08 5.0420e+08  0.09%   196 83271s
 46525 17175 5.0375e+08   64  479 5.0374e+08 5.0420e+08  0.09%   195 83305s
 46787 17289 5.0374e+08   78  448 5.0374e+08 5.0420e+08  0.09%   194 83338s
 47031 17461 5.0375e+08   57  511 5.0374e+08 5.0420e+08  0.09%   194 83373s
 47284 17633 5.0374e+08   31  513 5.0374e+08 5.0420e+08  0.09%   193 83409s
 47553 17780     cutoff   49      5.0374e+08 5.0420e+08  0.09%   193 83442s
 47799 17916 5.0375e+08   58  510 5.0374e+08 5.0420e+08  0.09%   192 83479s
 48031 17979 5.0374e+08   74  389 5.0374e+08 5.0420e+08  0.09%   192 83517s
 48154 18088     cutoff   41      5.0374e+08 5.0420e+08  0.09%   191 83552s
 48339 18265 5.0374e+08   51  485 5.0374e+08 5.0420e+08  0.09%   191 83583s
 48599 18371 5.0375e+08   47  517 5.0374e+08 5.0420e+08  0.09%   190 83618s
 48844 18515 5.0374e+08   68  463 5.0374e+08 5.0420e+08  0.09%   190 83708s
 49071 18719 5.0374e+08   52  491 5.0374e+08 5.0420e+08  0.09%   189 83741s
 49339 18516 5.0374e+08   72 1880 5.0374e+08 5.0420e+08  0.09%   188 83821s
 49362 18540 5.0374e+08   73 1881 5.0374e+08 5.0420e+08  0.09%   189 83981s
 49410 18559     cutoff   73      5.0374e+08 5.0420e+08  0.09%   189 84123s
 49459 18584 5.0407e+08   15 2962 5.0374e+08 5.0420e+08  0.09%   190 84277s
 49520 18604 5.0380e+08   21 2859 5.0374e+08 5.0420e+08  0.09%   191 84416s
 49575 18608 infeasible   23      5.0374e+08 5.0420e+08  0.09%   193 84569s
 49631 18636 5.0411e+08   11 3207 5.0374e+08 5.0420e+08  0.09%   194 84713s
 49694 18647 5.0407e+08   15 2906 5.0374e+08 5.0420e+08  0.09%   195 84854s
 49751 18666     cutoff   18      5.0374e+08 5.0420e+08  0.09%   196 85000s
 49800 18704 5.0380e+08   22 2662 5.0374e+08 5.0420e+08  0.09%   197 85123s
 49864 18703 5.0378e+08   25 2464 5.0374e+08 5.0420e+08  0.09%   198 85334s
 49885 18720 5.0377e+08   26 2420 5.0374e+08 5.0420e+08  0.09%   199 85529s
 49914 18746 5.0377e+08   29 2216 5.0374e+08 5.0420e+08  0.09%   199 85674s
 49966 18761 5.0376e+08   31 1940 5.0374e+08 5.0420e+08  0.09%   200 85861s
 49995 18802 5.0375e+08   32 1940 5.0374e+08 5.0420e+08  0.09%   201 85997s
 50050 18839     cutoff   35      5.0374e+08 5.0420e+08  0.09%   201 86100s
 50118 18882 5.0376e+08   39 1951 5.0374e+08 5.0420e+08  0.09%   202 86200s
 50187 18882 5.0376e+08   42 1954 5.0374e+08 5.0420e+08  0.09%   202 86441s
 50205 18883 5.0375e+08   43 1979 5.0374e+08 5.0420e+08  0.09%   203 86596s
 50232 18891 5.0375e+08   43 1946 5.0374e+08 5.0420e+08  0.09%   203 86748s
 50254 18910 5.0375e+08   44 1968 5.0374e+08 5.0420e+08  0.09%   204 86886s
 50297 18916 5.0375e+08   47 1958 5.0374e+08 5.0420e+08  0.09%   204 87032s
 50339 18943 5.0375e+08   51 1903 5.0374e+08 5.0420e+08  0.09%   205 87190s
 50382 18981 5.0375e+08   54 1896 5.0374e+08 5.0420e+08  0.09%   206 87412s
 50426 18989 5.0375e+08   58 1770 5.0374e+08 5.0420e+08  0.09%   208 87553s
 50495 19000     cutoff   61      5.0374e+08 5.0420e+08  0.09%   209 87714s
 50553 19027 infeasible   63      5.0374e+08 5.0420e+08  0.09%   210 87886s
 50614 19041     cutoff    8      5.0374e+08 5.0420e+08  0.09%   212 88046s
 50674 19068 5.0404e+08   10 4372 5.0374e+08 5.0420e+08  0.09%   213 88188s
 50735 19097 5.0389e+08   17 3243 5.0374e+08 5.0420e+08  0.09%   214 88351s
 50792 19132 5.0380e+08   20 3218 5.0374e+08 5.0420e+08  0.09%   215 88494s
 50853 19158 5.0375e+08   23 3137 5.0374e+08 5.0420e+08  0.09%   216 88641s
 50909 19186 5.0408e+08    9 4281 5.0374e+08 5.0420e+08  0.09%   217 88746s
 50973 19195 5.0401e+08   15 3281 5.0374e+08 5.0420e+08  0.09%   218 88895s
 51034 19219 5.0378e+08   19 3204 5.0374e+08 5.0420e+08  0.09%   219 89038s
 51097 19251 5.0378e+08   20 3119 5.0374e+08 5.0420e+08  0.09%   219 89160s
 51155 19275     cutoff   22      5.0374e+08 5.0420e+08  0.09%   220 89288s
 51217 19297 5.0407e+08   12 3193 5.0374e+08 5.0420e+08  0.09%   221 89429s
 51279 19301 infeasible   19      5.0374e+08 5.0420e+08  0.09%   222 89558s
 51339 19307 5.0387e+08   17 2711 5.0374e+08 5.0420e+08  0.09%   223 89705s
 51391 19327 5.0376e+08   20 2710 5.0374e+08 5.0420e+08  0.09%   224 89826s
 51445 19352 infeasible   18      5.0374e+08 5.0420e+08  0.09%   225 89987s
 51498 19380 5.0400e+08   16 2774 5.0374e+08 5.0420e+08  0.09%   226 90131s
 51560 19401 5.0380e+08   23 2726 5.0374e+08 5.0420e+08  0.09%   227 90278s
 51609 19425 5.0376e+08   29 2317 5.0374e+08 5.0420e+08  0.09%   228 90425s
 51661 19449 5.0376e+08   36 2140 5.0374e+08 5.0420e+08  0.09%   229 90570s
 51715 19482 5.0375e+08   43 2127 5.0374e+08 5.0419e+08  0.09%   230 90718s
 51768 19495 5.0375e+08   50 2076 5.0374e+08 5.0419e+08  0.09%   230 90846s
 51827 19512 5.0375e+08   57 2011 5.0374e+08 5.0419e+08  0.09%   231 90983s
 51880 19553 5.0375e+08   64 2017 5.0374e+08 5.0419e+08  0.09%   232 91110s
 51943 19580 5.0374e+08   71 2006 5.0374e+08 5.0419e+08  0.09%   233 91214s
 52009 19579 5.0374e+08   78 1973 5.0374e+08 5.0419e+08  0.09%   233 91361s
 52066 19588 5.0374e+08   78 1971 5.0374e+08 5.0418e+08  0.09%   233 91518s
 52091 19606     cutoff   80      5.0374e+08 5.0418e+08  0.09%   234 91668s
 52125 19621 5.0374e+08   80 1958 5.0374e+08 5.0418e+08  0.09%   235 91778s
 52187 19627 5.0374e+08   80 2021 5.0374e+08 5.0418e+08  0.09%   236 91909s
 52246 19644 5.0403e+08   11 3464 5.0374e+08 5.0418e+08  0.09%   236 92034s
 52297 19665 5.0384e+08   18 3097 5.0374e+08 5.0418e+08  0.09%   237 92190s
 52346 19665 5.0377e+08   21 3066 5.0374e+08 5.0418e+08  0.09%   238 92336s
 52392 19679     cutoff   22      5.0374e+08 5.0417e+08  0.08%   238 92483s
 52436 19702 5.0389e+08   17 3314 5.0374e+08 5.0417e+08  0.08%   240 92638s
 52491 19733     cutoff   21      5.0374e+08 5.0417e+08  0.08%   241 92771s
 52543 19752 infeasible   12      5.0374e+08 5.0417e+08  0.08%   241 92898s
 52589 19774 5.0398e+08   15 3154 5.0374e+08 5.0417e+08  0.08%   242 93015s
 52647 19800 5.0387e+08   16 3201 5.0374e+08 5.0417e+08  0.08%   243 93145s
 52709 19824     cutoff   20      5.0374e+08 5.0417e+08  0.08%   244 93285s
 52766 19832 infeasible   22      5.0374e+08 5.0417e+08  0.08%   244 93449s
 52790 19848 5.0377e+08   43 2191 5.0374e+08 5.0417e+08  0.08%   245 93574s
 52816 19866 5.0396e+08   16 2718 5.0374e+08 5.0417e+08  0.08%   245 93711s
 52850 19897 5.0393e+08   18 2573 5.0374e+08 5.0417e+08  0.08%   246 93847s
 52915 19908     cutoff   24      5.0374e+08 5.0417e+08  0.08%   246 93968s
 52976 19933 5.0400e+08   18 2622 5.0374e+08 5.0417e+08  0.08%   247 94111s
 53029 19965 5.0396e+08   19 2610 5.0374e+08 5.0417e+08  0.08%   248 94225s
 53097 20012 5.0382e+08   23 2672 5.0374e+08 5.0417e+08  0.08%   249 94328s
 53166 20028 5.0389e+08   22 2600 5.0374e+08 5.0416e+08  0.08%   249 94481s
 53196 20042     cutoff   24      5.0374e+08 5.0416e+08  0.08%   249 94608s
 53238 20070     cutoff   26      5.0374e+08 5.0416e+08  0.08%   249 94720s
 53304 20105 5.0383e+08   25 2552 5.0374e+08 5.0416e+08  0.08%   250 94832s
 53372 20128 5.0377e+08   27 2582 5.0374e+08 5.0416e+08  0.08%   250 94964s
 53421 20164 5.0376e+08   31 2220 5.0374e+08 5.0416e+08  0.08%   251 95097s
 53471 20187 5.0375e+08   38 2221 5.0374e+08 5.0416e+08  0.08%   252 95213s
 53524 20213 5.0374e+08   44 2257 5.0374e+08 5.0416e+08  0.08%   252 95324s
 53573 20251 infeasible   45      5.0374e+08 5.0416e+08  0.08%   253 95420s
 53637 20286 5.0375e+08   43 2226 5.0374e+08 5.0416e+08  0.08%   253 95522s
 53702 20309 5.0375e+08   43 2253 5.0374e+08 5.0416e+08  0.08%   253 95610s
 53769 20331 5.0375e+08   41 2291 5.0374e+08 5.0416e+08  0.08%   254 95712s
 53831 20353     cutoff   45      5.0374e+08 5.0416e+08  0.08%   254 95817s
 53900 20401 5.0375e+08   42 2295 5.0374e+08 5.0416e+08  0.08%   254 95906s
 53964 20411 infeasible   48      5.0374e+08 5.0416e+08  0.08%   255 96024s
 54008 20434 5.0374e+08   45 2267 5.0374e+08 5.0416e+08  0.08%   255 96163s
 54043 20462 5.0374e+08   46 2265 5.0374e+08 5.0416e+08  0.08%   256 96264s
 54089 20224 5.0374e+08   46 2271 5.0374e+08 5.0416e+08  0.08%   256 96404s
 54141 20253 5.0376e+08   39 2283 5.0374e+08 5.0416e+08  0.08%   257 96510s
 54178 20302 5.0376e+08   44 2238 5.0374e+08 5.0416e+08  0.08%   257 96601s
 54237 20338 5.0399e+08   15 2778 5.0374e+08 5.0416e+08  0.08%   257 96711s
 54301 20368 5.0382e+08   18 2707 5.0374e+08 5.0416e+08  0.08%   257 96849s
 54363 20403 5.0398e+08   15 2771 5.0374e+08 5.0416e+08  0.08%   258 97010s
 54412 20441 5.0383e+08   18 2668 5.0374e+08 5.0416e+08  0.08%   258 97111s
 54466 20450 5.0376e+08   21 2644 5.0374e+08 5.0416e+08  0.08%   258 97244s
 54507 20484 5.0400e+08   14 2842 5.0374e+08 5.0415e+08  0.08%   259 97351s
 54559 20507 5.0375e+08   20 2824 5.0374e+08 5.0415e+08  0.08%   259 97477s
 54618 20531 5.0401e+08   13 2838 5.0374e+08 5.0415e+08  0.08%   259 97618s
 54674 20573 5.0386e+08   17 2717 5.0374e+08 5.0415e+08  0.08%   260 97713s
 54738 20585 5.0375e+08   20 2843 5.0374e+08 5.0415e+08  0.08%   261 97820s
 54802 20599 5.0395e+08   16 2814 5.0374e+08 5.0415e+08  0.08%   261 97947s
 54860 20626 5.0380e+08   20 2870 5.0374e+08 5.0415e+08  0.08%   262 98056s
 54913 20654 5.0375e+08   22 2836 5.0374e+08 5.0415e+08  0.08%   262 98191s
 54967 20645 5.0390e+08   18 2607 5.0374e+08 5.0415e+08  0.08%   263 98323s
 54990 20686 5.0401e+08   13 2848 5.0374e+08 5.0415e+08  0.08%   264 98420s
 55041 20715 infeasible   19      5.0374e+08 5.0415e+08  0.08%   264 98546s
 55102 20727     cutoff   21      5.0374e+08 5.0414e+08  0.08%   265 98678s
 55160 20759     cutoff   18      5.0374e+08 5.0414e+08  0.08%   265 98793s
 55218 20784     cutoff   20      5.0374e+08 5.0414e+08  0.08%   266 98905s
 55280 20798     cutoff   22      5.0374e+08 5.0414e+08  0.08%   266 99031s
 55340 20829 5.0395e+08   15 2674 5.0374e+08 5.0414e+08  0.08%   267 99166s
 55391 20850 5.0377e+08   20 2755 5.0374e+08 5.0414e+08  0.08%   268 99259s
 55451 20871 5.0401e+08   14 2798 5.0374e+08 5.0414e+08  0.08%   268 99390s
 55498 20901 5.0387e+08   18 2682 5.0374e+08 5.0414e+08  0.08%   269 99522s
 55562 20927 5.0375e+08   21 2820 5.0374e+08 5.0414e+08  0.08%   269 99705s
 55617 20953 infeasible   18      5.0374e+08 5.0414e+08  0.08%   270 99826s
 55666 20953 5.0385e+08   19 2837 5.0374e+08 5.0414e+08  0.08%   270 99959s
 55708 20972 5.0374e+08   21 2969 5.0374e+08 5.0414e+08  0.08%   271 100080s
 55769 20985 5.0379e+08   23 2773 5.0374e+08 5.0414e+08  0.08%   271 100195s
 55829 20994 infeasible   12      5.0374e+08 5.0414e+08  0.08%   272 100326s
 55882 21006 5.0396e+08   15 3022 5.0374e+08 5.0414e+08  0.08%   272 100454s
 55927 21034 infeasible   18      5.0374e+08 5.0414e+08  0.08%   273 100577s
 55981 21055     cutoff   21      5.0374e+08 5.0414e+08  0.08%   274 100692s
 56044 21076 5.0400e+08   17 2502 5.0374e+08 5.0414e+08  0.08%   275 100822s
 56099 21122 5.0390e+08   20 2504 5.0374e+08 5.0414e+08  0.08%   276 100916s
 56151 21144     cutoff   25      5.0374e+08 5.0414e+08  0.08%   276 101016s
 56208 21167     cutoff   28      5.0374e+08 5.0414e+08  0.08%   277 101135s
H56267 21167                    5.037436e+08 5.0413e+08  0.08%   277 101158s
 56267 21320     cutoff   75      5.0374e+08 5.0413e+08  0.08%   277 101188s
 56526 21493 5.0375e+08   37  516 5.0374e+08 5.0413e+08  0.08%   276 101224s
 56758 21622 5.0374e+08   61  479 5.0374e+08 5.0413e+08  0.08%   275 101458s
 56934 21699     cutoff   70      5.0374e+08 5.0413e+08  0.08%   275 101501s
 57156 21869     cutoff   37      5.0374e+08 5.0413e+08  0.08%   274 101533s
 57416 22032 5.0375e+08   42  490 5.0374e+08 5.0413e+08  0.08%   273 101566s
 57645 22083 5.0374e+08   52  450 5.0374e+08 5.0413e+08  0.08%   273 101610s
 57719 22254 5.0375e+08   37  538 5.0374e+08 5.0413e+08  0.08%   272 101651s
 57977 22375 5.0375e+08   64  467 5.0374e+08 5.0413e+08  0.08%   271 101684s
 58234 22509 5.0375e+08   35  505 5.0374e+08 5.0413e+08  0.08%   271 101723s
 58457 22700 5.0374e+08   45  500 5.0374e+08 5.0413e+08  0.08%   270 101757s
 58725 22826 5.0375e+08   45  478 5.0374e+08 5.0413e+08  0.08%   269 101911s
 58931 23004 5.0374e+08   60  422 5.0374e+08 5.0413e+08  0.08%   269 101954s
 59179 23142 5.0375e+08   50  482 5.0374e+08 5.0413e+08  0.08%   268 101989s
 59375 23283 5.0375e+08   67  469 5.0374e+08 5.0413e+08  0.08%   267 102024s
 59635 23442 5.0375e+08   48  523 5.0374e+08 5.0413e+08  0.08%   266 102069s
 59893 23582     cutoff   67      5.0374e+08 5.0413e+08  0.08%   265 102103s
 60132 23748 5.0374e+08   48  513 5.0374e+08 5.0413e+08  0.08%   265 102147s
 60372 23918 5.0374e+08   43  524 5.0374e+08 5.0413e+08  0.08%   264 102180s
 60642 24044 5.0374e+08   44  502 5.0374e+08 5.0413e+08  0.08%   263 102220s
 60892 24202 5.0374e+08   42  555 5.0374e+08 5.0413e+08  0.08%   262 102255s
 61153 24326 5.0374e+08   49  510 5.0374e+08 5.0413e+08  0.08%   262 102288s
 61422 24419 5.0374e+08   57  492 5.0374e+08 5.0413e+08  0.08%   261 102326s
 61673 24526 5.0375e+08   46  507 5.0374e+08 5.0413e+08  0.08%   260 102554s
 61870 24743 5.0374e+08   68  478 5.0374e+08 5.0413e+08  0.08%   260 102587s
 62139 24859 5.0375e+08   50  483 5.0374e+08 5.0413e+08  0.08%   259 102632s
 62371 24976     cutoff   69      5.0374e+08 5.0413e+08  0.08%   258 102666s
 62615 25168 5.0374e+08   59  458 5.0374e+08 5.0413e+08  0.08%   257 102699s
 62878 25280 5.0375e+08   45  487 5.0374e+08 5.0413e+08  0.08%   257 102730s
 63112 25455 5.0374e+08   69  398 5.0374e+08 5.0413e+08  0.08%   256 102763s
 63367 25464 5.0392e+08   18 2653 5.0374e+08 5.0413e+08  0.08%   255 102984s
 63376 25496 5.0384e+08   19 2741 5.0374e+08 5.0413e+08  0.08%   255 103278s
 63442 25518 5.0376e+08   24 2652 5.0374e+08 5.0413e+08  0.08%   256 103440s
 63511 25532 5.0395e+08   16 2755 5.0374e+08 5.0413e+08  0.08%   257 103609s
 63575 25558 5.0379e+08   22 2790 5.0374e+08 5.0413e+08  0.08%   258 103763s
 63635 25575 5.0398e+08   14 2686 5.0374e+08 5.0413e+08  0.08%   259 103924s
 63696 25605 5.0383e+08   20 2560 5.0374e+08 5.0413e+08  0.08%   259 104071s
 63756 25637 5.0396e+08   14 2856 5.0374e+08 5.0413e+08  0.08%   260 104223s
 63816 25669 5.0382e+08   21 2632 5.0374e+08 5.0413e+08  0.08%   261 104322s
 63870 25695 infeasible   25      5.0374e+08 5.0413e+08  0.08%   261 104460s
 63926 25734 5.0398e+08   16 2521 5.0374e+08 5.0413e+08  0.08%   263 104541s
 63991 25757 5.0394e+08   17 2502 5.0374e+08 5.0413e+08  0.08%   263 104655s
 64054 25787 5.0378e+08   22 2544 5.0374e+08 5.0413e+08  0.08%   263 104779s
 64112 25820 5.0397e+08   14 2671 5.0374e+08 5.0413e+08  0.08%   264 104875s
 64173 25852 infeasible   21      5.0374e+08 5.0413e+08  0.08%   264 104983s
 64238 25875 5.0397e+08   14 2634 5.0374e+08 5.0413e+08  0.08%   264 105098s
 64293 25906 5.0387e+08   16 2536 5.0374e+08 5.0413e+08  0.08%   265 105211s
 64348 25923     cutoff   20      5.0374e+08 5.0413e+08  0.08%   265 105323s
 64407 25948     cutoff   22      5.0374e+08 5.0413e+08  0.08%   265 105426s
 64458 25980 5.0401e+08   15 2767 5.0374e+08 5.0412e+08  0.08%   266 105522s
 64514 26014 5.0388e+08   22 2565 5.0374e+08 5.0412e+08  0.08%   266 105599s
 64572 26052 5.0379e+08   29 2533 5.0374e+08 5.0412e+08  0.08%   266 105691s
 64622 26075 5.0378e+08   31 2083 5.0374e+08 5.0412e+08  0.08%   266 105795s
 64681 26109 5.0378e+08   38 2044 5.0374e+08 5.0412e+08  0.08%   267 105908s
 64731 26145 5.0377e+08   45 2046 5.0374e+08 5.0412e+08  0.08%   267 106014s
 64785 26186 5.0377e+08   52 2052 5.0374e+08 5.0412e+08  0.08%   268 106103s
 64840 26227 5.0377e+08   59 2071 5.0374e+08 5.0412e+08  0.08%   268 106205s
 64905 26259 5.0376e+08   66 1995 5.0374e+08 5.0412e+08  0.08%   268 106303s
 64969 26305 5.0376e+08   73 1970 5.0374e+08 5.0412e+08  0.08%   268 106390s
 65021 26349 5.0376e+08   80 1983 5.0374e+08 5.0412e+08  0.08%   269 106482s
 65083 26392 5.0376e+08   87 2030 5.0374e+08 5.0412e+08  0.07%   269 106571s
 65150 26430 5.0376e+08   94 2019 5.0374e+08 5.0412e+08  0.07%   269 106659s
 65204 26483 5.0376e+08  101 2002 5.0374e+08 5.0412e+08  0.07%   269 106731s
 65263 26509 5.0375e+08  108 2011 5.0374e+08 5.0412e+08  0.07%   269 106856s
 65307 26535 5.0375e+08  113 2007 5.0374e+08 5.0412e+08  0.07%   269 106935s
 65342 26592 5.0375e+08  116 2007 5.0374e+08 5.0412e+08  0.07%   269 106999s
 65405 26647 5.0375e+08  123 1969 5.0374e+08 5.0412e+08  0.07%   269 107093s
 65469 26698 5.0375e+08  130 1965 5.0374e+08 5.0412e+08  0.07%   269 107164s
 65520 26740 5.0375e+08  137 1962 5.0374e+08 5.0412e+08  0.07%   269 107252s
 65572 26786 5.0375e+08  144 1956 5.0374e+08 5.0412e+08  0.07%   269 107336s
 65624 26834 5.0375e+08  151 1939 5.0374e+08 5.0412e+08  0.07%   269 107403s
 65680 26875 5.0375e+08  158 1931 5.0374e+08 5.0412e+08  0.07%   269 107494s
 65733 26934 5.0375e+08  165 1931 5.0374e+08 5.0412e+08  0.07%   269 107555s
 65796 26982 5.0375e+08  172 1980 5.0374e+08 5.0412e+08  0.07%   269 107634s
 65859 27031 5.0375e+08  179 1976 5.0374e+08 5.0412e+08  0.07%   269 107703s
 65915 27063 5.0375e+08  186 2101 5.0374e+08 5.0412e+08  0.07%   269 107795s
 65962 27084 5.0375e+08  193 1972 5.0374e+08 5.0412e+08  0.07%   269 107898s
 66004 26817 5.0375e+08  200 1966 5.0374e+08 5.0412e+08  0.07%   269 107989s
 66060 26853 5.0375e+08  207 1995 5.0374e+08 5.0412e+08  0.07%   269 108067s
 66126 26881 5.0375e+08  214 1998 5.0374e+08 5.0412e+08  0.07%   269 108162s
 66179 26907 5.0375e+08  221 1990 5.0374e+08 5.0412e+08  0.07%   270 108253s
 66229 26931 5.0375e+08  228 1991 5.0374e+08 5.0412e+08  0.07%   270 108336s
 66271 26967 5.0374e+08  234 2013 5.0374e+08 5.0412e+08  0.07%   270 108422s
 66315 27012 5.0374e+08  241 2000 5.0374e+08 5.0412e+08  0.07%   270 108504s
 66372 27037 5.0374e+08  248 1991 5.0374e+08 5.0412e+08  0.07%   271 108580s
 66431 27056 5.0374e+08  250 1834 5.0374e+08 5.0412e+08  0.07%   271 108674s
 66486 27085     cutoff  250      5.0374e+08 5.0412e+08  0.07%   271 108753s
 66538 27110     cutoff  251      5.0374e+08 5.0411e+08  0.07%   271 108823s
 66595 27122     cutoff  248      5.0374e+08 5.0411e+08  0.07%   272 108925s
 66633 27143 5.0398e+08   18 2577 5.0374e+08 5.0411e+08  0.07%   272 109020s
 66675 27146     cutoff   24      5.0374e+08 5.0411e+08  0.07%   272 109090s
 66710 27165 5.0379e+08   24 2607 5.0374e+08 5.0411e+08  0.07%   273 109200s
 66745 27198 5.0376e+08   30 2194 5.0374e+08 5.0411e+08  0.07%   273 109303s
 66800 27220 5.0375e+08   32 2153 5.0374e+08 5.0411e+08  0.07%   273 109392s
 66858 27255 5.0375e+08   39 2209 5.0374e+08 5.0411e+08  0.07%   273 109466s
 66911 27278 5.0374e+08   45 2170 5.0374e+08 5.0411e+08  0.07%   273 109544s
 66960 27305 infeasible   50      5.0374e+08 5.0411e+08  0.07%   274 109650s
 67007 27334 5.0392e+08   18 2791 5.0374e+08 5.0411e+08  0.07%   274 109742s
 67052 27335 5.0375e+08   25 2778 5.0374e+08 5.0411e+08  0.07%   274 109847s
 67094 27361 5.0397e+08   17 2608 5.0374e+08 5.0411e+08  0.07%   275 109952s
 67134 27395 5.0392e+08   18 2587 5.0374e+08 5.0411e+08  0.07%   276 110027s
 67196 27402 5.0376e+08   23 2618 5.0374e+08 5.0411e+08  0.07%   276 110152s
 67239 27424 5.0391e+08   19 2513 5.0374e+08 5.0411e+08  0.07%   276 110267s
 67279 27451 5.0393e+08   19 2584 5.0374e+08 5.0411e+08  0.07%   276 110399s
 67334 27472 5.0382e+08   22 2685 5.0374e+08 5.0411e+08  0.07%   277 110527s
 67391 27500 5.0397e+08   10 3463 5.0374e+08 5.0411e+08  0.07%   278 110629s
 67453 27526 5.0388e+08   17 2718 5.0374e+08 5.0411e+08  0.07%   278 110738s
 67511 27547 infeasible   21      5.0374e+08 5.0411e+08  0.07%   278 110841s
 67564 27564 5.0393e+08   13 3246 5.0374e+08 5.0411e+08  0.07%   279 111036s
 67605 27577 5.0388e+08   16 2712 5.0374e+08 5.0411e+08  0.07%   279 111173s
 67640 27592 5.0388e+08   17 2693 5.0374e+08 5.0411e+08  0.07%   280 111313s
 67683 27611 5.0382e+08   20 2653 5.0374e+08 5.0411e+08  0.07%   280 111424s
 67732 27656 5.0375e+08   22 2650 5.0374e+08 5.0411e+08  0.07%   280 111556s
 67788 27688 5.0398e+08   14 2995 5.0374e+08 5.0411e+08  0.07%   280 111660s
 67840 27730 5.0388e+08   16 2883 5.0374e+08 5.0411e+08  0.07%   281 111787s
 67901 27764     cutoff   20      5.0374e+08 5.0411e+08  0.07%   281 111873s
 67953 27798 5.0376e+08   21 2890 5.0374e+08 5.0411e+08  0.07%   281 111960s
 68007 27849     cutoff   10      5.0374e+08 5.0411e+08  0.07%   281 112068s
 68066 27862 5.0398e+08   13 3340 5.0374e+08 5.0411e+08  0.07%   282 112244s
 68094 27879 5.0398e+08   14 3066 5.0374e+08 5.0411e+08  0.07%   282 112374s
 68123 25723 5.0398e+08   14 3077 5.0374e+08 5.0411e+08  0.07%   282 112499s
 68189 25745     cutoff   18      5.0374e+08 5.0411e+08  0.07%   282 112622s
 68240 25775 5.0383e+08   21 2737 5.0374e+08 5.0411e+08  0.07%   282 112724s
 68286 25799 5.0395e+08   16 2934 5.0374e+08 5.0411e+08  0.07%   282 112835s
 68337 25813 5.0390e+08   18 2768 5.0374e+08 5.0411e+08  0.07%   283 112934s
 68398 25825 infeasible   23      5.0374e+08 5.0411e+08  0.07%   283 113040s
 68466 25829     cutoff   24      5.0374e+08 5.0411e+08  0.07%   284 113270s
 68488 25843 5.0404e+08    9 3619 5.0374e+08 5.0411e+08  0.07%   284 113366s
 68512 25859 5.0404e+08   10 3511 5.0374e+08 5.0411e+08  0.07%   284 113456s
 68560 25890 5.0398e+08   14 2996 5.0374e+08 5.0411e+08  0.07%   284 113562s
 68615 25916     cutoff   20      5.0374e+08 5.0411e+08  0.07%   285 113677s
 68675 25934     cutoff   23      5.0374e+08 5.0411e+08  0.07%   285 113791s
 68736 25951 5.0393e+08   13 3267 5.0374e+08 5.0411e+08  0.07%   285 113906s
 68789 25979 5.0378e+08   18 2851 5.0374e+08 5.0411e+08  0.07%   286 114014s
 68853 25983 5.0393e+08   13 3271 5.0374e+08 5.0411e+08  0.07%   286 114128s
 68911 25988     cutoff   19      5.0374e+08 5.0411e+08  0.07%   287 114273s
 68934 25998 infeasible   18      5.0374e+08 5.0411e+08  0.07%   287 114397s
 68962 26027 5.0401e+08   14 2682 5.0374e+08 5.0411e+08  0.07%   288 114546s
 69015 26029 5.0401e+08   15 2538 5.0374e+08 5.0411e+08  0.07%   288 114665s
 69067 26035 5.0384e+08   22 2442 5.0374e+08 5.0411e+08  0.07%   288 114914s
 69079 26052 5.0380e+08   23 2430 5.0374e+08 5.0411e+08  0.07%   289 115035s
 69114 26090 5.0378e+08   25 2495 5.0374e+08 5.0410e+08  0.07%   289 115152s
 69168 26113 5.0377e+08   30 2029 5.0374e+08 5.0410e+08  0.07%   289 115280s
 69225 26140 5.0377e+08   37 2041 5.0374e+08 5.0410e+08  0.07%   290 115374s
 69276 26165 5.0376e+08   44 1998 5.0374e+08 5.0410e+08  0.07%   290 115464s
 69329 26188 5.0376e+08   51 1901 5.0374e+08 5.0410e+08  0.07%   291 115540s
 69392 26204 5.0376e+08   58 1887 5.0374e+08 5.0410e+08  0.07%   291 115648s
 69454 26215 5.0376e+08   65 1910 5.0374e+08 5.0410e+08  0.07%   291 115776s
 69503 26259 5.0376e+08   72 1914 5.0374e+08 5.0410e+08  0.07%   292 115894s
 69561 26284     cutoff   79      5.0374e+08 5.0410e+08  0.07%   292 116100s
 69624 26303 5.0375e+08   81 1963 5.0374e+08 5.0410e+08  0.07%   292 116210s
 69671 26320     cutoff   86      5.0374e+08 5.0410e+08  0.07%   292 116318s
 69724 26330 5.0375e+08   84 1885 5.0374e+08 5.0410e+08  0.07%   293 116441s
 69784 26351 5.0391e+08   14 2814 5.0374e+08 5.0410e+08  0.07%   293 116563s
 69837 26391 5.0393e+08   17 2515 5.0374e+08 5.0410e+08  0.07%   293 116692s
 69891 26422 5.0386e+08   20 2474 5.0374e+08 5.0410e+08  0.07%   294 116811s
 69954 26443 infeasible   24      5.0374e+08 5.0410e+08  0.07%   294 116924s
 70005 26469 5.0397e+08   15 2694 5.0374e+08 5.0410e+08  0.07%   295 117038s
 70049 26511 5.0390e+08   19 2505 5.0374e+08 5.0410e+08  0.07%   295 117137s
 70109 26534 5.0383e+08   21 2504 5.0374e+08 5.0410e+08  0.07%   296 117241s
 70164 26531 5.0375e+08   31 2269 5.0374e+08 5.0410e+08  0.07%   296 117378s
 70191 26547 5.0395e+08   15 2574 5.0374e+08 5.0410e+08  0.07%   296 117537s
 70215 26588 5.0391e+08   18 2406 5.0374e+08 5.0410e+08  0.07%   297 117637s
 70274 26598 5.0375e+08   23 2455 5.0374e+08 5.0410e+08  0.07%   297 117756s
 70328 26640 5.0388e+08   18 2615 5.0374e+08 5.0410e+08  0.07%   297 117842s
 70386 26654     cutoff   23      5.0374e+08 5.0410e+08  0.07%   298 117954s
 70446 26682 5.0403e+08    9 4032 5.0374e+08 5.0410e+08  0.07%   298 118072s
 70498 26701 5.0394e+08   16 2772 5.0374e+08 5.0410e+08  0.07%   298 118160s
 70554 26715 5.0377e+08   22 2829 5.0374e+08 5.0410e+08  0.07%   298 118279s
 70610 26735     cutoff   24      5.0374e+08 5.0410e+08  0.07%   298 118402s
 70668 26755 5.0403e+08   12 3036 5.0374e+08 5.0410e+08  0.07%   299 118532s
 70716 26771 5.0377e+08   19 2820 5.0374e+08 5.0410e+08  0.07%   299 118641s
 70766 26771 5.0376e+08   22 2674 5.0374e+08 5.0410e+08  0.07%   299 118805s
 70794 26782 5.0396e+08   17 2766 5.0374e+08 5.0410e+08  0.07%   300 118903s
 70827 26811 5.0392e+08   18 2746 5.0374e+08 5.0410e+08  0.07%   300 119012s
 70890 26828     cutoff   24      5.0374e+08 5.0410e+08  0.07%   301 119133s
 70941 26849 5.0383e+08   20 2624 5.0374e+08 5.0410e+08  0.07%   301 119255s
 70988 26869 5.0396e+08   14 2653 5.0374e+08 5.0410e+08  0.07%   301 119369s
 71044 26884 5.0386e+08   18 2459 5.0374e+08 5.0410e+08  0.07%   302 119498s
 71096 26887 5.0379e+08   21 2448 5.0374e+08 5.0410e+08  0.07%   302 119610s
 71147 26915 5.0396e+08   16 2531 5.0374e+08 5.0410e+08  0.07%   303 119733s
 71202 26932 5.0387e+08   18 2556 5.0374e+08 5.0410e+08  0.07%   303 119861s
 71262 26946 5.0380e+08   22 2465 5.0374e+08 5.0410e+08  0.07%   303 120011s
 71318 26960 5.0379e+08   21 2591 5.0374e+08 5.0409e+08  0.07%   304 120127s
 71360 26953     cutoff   21      5.0374e+08 5.0409e+08  0.07%   304 120239s
 71418 26967 5.0398e+08   18 2626 5.0374e+08 5.0409e+08  0.07%   304 120371s
 71471 26981 infeasible   24      5.0374e+08 5.0409e+08  0.07%   305 120495s
 71525 26988 5.0392e+08   14 2989 5.0374e+08 5.0409e+08  0.07%   305 120624s
 71586 26997     cutoff   18      5.0374e+08 5.0409e+08  0.07%   306 120750s
 71637 27017 5.0394e+08   15 3033 5.0374e+08 5.0409e+08  0.07%   306 120878s
 71687 27053 5.0390e+08   16 2924 5.0374e+08 5.0409e+08  0.07%   307 120994s
 71749 27058 5.0383e+08   20 2726 5.0374e+08 5.0409e+08  0.07%   307 121119s
 71800 27091     cutoff   23      5.0374e+08 5.0409e+08  0.07%   308 121243s
 71853 27107 5.0395e+08   14 2783 5.0374e+08 5.0409e+08  0.07%   308 121383s
 71891 27112 5.0380e+08   19 2725 5.0374e+08 5.0409e+08  0.07%   308 121508s
 71940 27121 5.0375e+08   21 2724 5.0374e+08 5.0409e+08  0.07%   309 121652s
 71975 27167 5.0395e+08   15 2624 5.0374e+08 5.0409e+08  0.07%   309 121759s
 72033 27174 5.0380e+08   21 2487 5.0374e+08 5.0409e+08  0.07%   309 121954s
 72046 27178     cutoff   22      5.0374e+08 5.0409e+08  0.07%   309 122070s
 72062 27180     cutoff   23      5.0374e+08 5.0409e+08  0.07%   309 122208s
 72098 27190     cutoff   22      5.0374e+08 5.0409e+08  0.07%   310 122338s
 72145 27213     cutoff   21      5.0374e+08 5.0409e+08  0.07%   310 122429s
 72200 27233     cutoff   22      5.0374e+08 5.0409e+08  0.07%   310 122530s
 72262 27240     cutoff   24      5.0374e+08 5.0409e+08  0.07%   310 122730s
 72319 27262 5.0396e+08   11 3242 5.0374e+08 5.0409e+08  0.07%   311 122863s
H72363 27262                    5.037502e+08 5.0409e+08  0.07%   311 122886s
 72363 27446 5.0375e+08   44  521 5.0375e+08 5.0409e+08  0.07%   311 122917s
 72627 27539     cutoff   69      5.0375e+08 5.0409e+08  0.07%   310 122958s
 72820 27659 5.0375e+08   42  500 5.0375e+08 5.0409e+08  0.07%   310 122997s
 73048 27826     cutoff   68      5.0375e+08 5.0409e+08  0.07%   309 123034s
 73267 27908     cutoff   50      5.0375e+08 5.0409e+08  0.07%   308 123067s
 73519 28056 5.0375e+08   34  510 5.0375e+08 5.0409e+08  0.07%   308 123105s
 73771 28240     cutoff   54      5.0375e+08 5.0409e+08  0.07%   307 123140s
 74039 28339 5.0375e+08   52  479 5.0375e+08 5.0409e+08  0.07%   306 123184s
 74215 28456 5.0375e+08   36  536 5.0375e+08 5.0409e+08  0.07%   306 123221s
 74463 28634     cutoff   44      5.0375e+08 5.0409e+08  0.07%   305 123255s
 74723 28736 5.0375e+08   37  511 5.0375e+08 5.0409e+08  0.07%   304 123292s
 74951 28916 5.0376e+08   36  538 5.0375e+08 5.0409e+08  0.07%   303 123326s
 75205 29018 5.0375e+08   63  482 5.0375e+08 5.0409e+08  0.07%   303 123361s
 75346 29173 5.0375e+08   40  529 5.0375e+08 5.0409e+08  0.07%   302 123397s
 75601 29361 5.0375e+08   62  506 5.0375e+08 5.0409e+08  0.07%   302 123436s
 75871 29510 5.0375e+08   59  496 5.0375e+08 5.0409e+08  0.07%   301 123466s
 76104 29612 5.0376e+08   23  535 5.0375e+08 5.0409e+08  0.07%   300 123499s
 76313 29769     cutoff   36      5.0375e+08 5.0409e+08  0.07%   299 123531s
 76556 29893 5.0375e+08   60  477 5.0375e+08 5.0409e+08  0.07%   299 123641s
 76758 30037     cutoff   71      5.0375e+08 5.0409e+08  0.07%   298 123675s
 76998 30225 5.0375e+08   55  500 5.0375e+08 5.0409e+08  0.07%   297 123709s
 77262 30388 5.0376e+08   31  503 5.0375e+08 5.0409e+08  0.07%   297 123741s
 77523 30536 5.0375e+08   58  501 5.0375e+08 5.0409e+08  0.07%   296 123780s
 77766 30665     cutoff   38      5.0375e+08 5.0409e+08  0.07%   295 123814s
 78015 30775 5.0375e+08   45  501 5.0375e+08 5.0409e+08  0.07%   294 123847s
 78232 30851     cutoff   56      5.0375e+08 5.0409e+08  0.07%   294 123882s
 78440 30964     cutoff   54      5.0375e+08 5.0409e+08  0.07%   293 123924s
 78666 31132 5.0376e+08   52  465 5.0375e+08 5.0409e+08  0.07%   293 123955s
 78918 31281     cutoff   71      5.0375e+08 5.0409e+08  0.07%   292 123992s
 79150 31487 5.0375e+08   55  501 5.0375e+08 5.0409e+08  0.07%   291 124024s
 79413 31613 5.0375e+08   79  429 5.0375e+08 5.0409e+08  0.07%   291 124057s
 79657 31720 5.0375e+08   52  481 5.0375e+08 5.0409e+08  0.07%   290 124089s
 79919 31785 5.0375e+08   58  467 5.0375e+08 5.0409e+08  0.07%   289 124125s
 80162 31914     cutoff   42      5.0375e+08 5.0409e+08  0.07%   289 124155s
 80399 32056 5.0376e+08   38  526 5.0375e+08 5.0409e+08  0.07%   288 124186s
 80643 32222 5.0375e+08   65  472 5.0375e+08 5.0409e+08  0.07%   287 124218s
 80911 32355 5.0375e+08   36  526 5.0375e+08 5.0409e+08  0.07%   287 124250s
 81154 32458 5.0375e+08   61  422 5.0375e+08 5.0409e+08  0.07%   286 124283s
 81368 32454 5.0380e+08   17 2915 5.0375e+08 5.0409e+08  0.07%   286 124396s
 81410 32455 5.0376e+08   17 2909 5.0375e+08 5.0409e+08  0.07%   286 124554s
 81425 32472     cutoff   18      5.0375e+08 5.0409e+08  0.07%   286 124762s
 81478 32492 5.0401e+08   16 2559 5.0375e+08 5.0409e+08  0.07%   287 124925s
 81536 32519 5.0381e+08   23 2487 5.0375e+08 5.0409e+08  0.07%   287 125090s
 81591 32571 5.0378e+08   29 2032 5.0375e+08 5.0409e+08  0.07%   288 125200s
 81659 32585 5.0377e+08   36 1997 5.0375e+08 5.0409e+08  0.07%   288 125339s
 81725 32608 5.0377e+08   43 1980 5.0375e+08 5.0409e+08  0.07%   288 125464s
 81772 32612 5.0377e+08   50 1995 5.0375e+08 5.0409e+08  0.07%   289 125777s
 81792 32640 5.0377e+08   51 1998 5.0375e+08 5.0409e+08  0.07%   289 125911s
 81846 32672 5.0376e+08   58 1927 5.0375e+08 5.0409e+08  0.07%   290 126016s
 81916 32689 5.0376e+08   65 1943 5.0375e+08 5.0409e+08  0.07%   290 126149s
 81975 32724 5.0375e+08   72 1997 5.0375e+08 5.0408e+08  0.07%   291 126287s
 82032 32737 5.0375e+08   79 1987 5.0375e+08 5.0408e+08  0.07%   291 126419s
 82089 32761 5.0375e+08   86 1988 5.0375e+08 5.0408e+08  0.07%   292 126546s
 82143 32769 5.0375e+08   93 1982 5.0375e+08 5.0408e+08  0.07%   292 126699s
 82191 32798 5.0375e+08   95 1961 5.0375e+08 5.0408e+08  0.07%   293 126816s
 82256 32793 5.0375e+08   98 1756 5.0375e+08 5.0408e+08  0.07%   293 126957s
 82305 32826 5.0390e+08   15 2750 5.0375e+08 5.0408e+08  0.07%   293 127069s
 82366 32851 5.0379e+08   19 2643 5.0375e+08 5.0408e+08  0.07%   294 127275s
 82429 32868 infeasible   19      5.0375e+08 5.0408e+08  0.07%   294 127411s
 82472 32878 5.0390e+08   16 2589 5.0375e+08 5.0408e+08  0.07%   295 127697s
 82488 32890 5.0390e+08   17 2571 5.0375e+08 5.0408e+08  0.07%   295 127838s
 82522 32906 5.0386e+08   18 2550 5.0375e+08 5.0408e+08  0.07%   295 127964s
 82578 32930     cutoff   21      5.0375e+08 5.0408e+08  0.07%   295 128089s
 82633 32948     cutoff   24      5.0375e+08 5.0408e+08  0.07%   296 128220s
 82697 32979     cutoff   22      5.0375e+08 5.0408e+08  0.07%   296 128326s
 82762 32993     cutoff   24      5.0375e+08 5.0408e+08  0.07%   296 128437s
 82820 33021 5.0398e+08   16 2657 5.0375e+08 5.0408e+08  0.07%   297 128569s
 82876 33031 infeasible   22      5.0375e+08 5.0408e+08  0.07%   297 128706s
 82936 33049     cutoff   24      5.0375e+08 5.0408e+08  0.07%   297 128830s
 82988 33062 5.0385e+08   16 2531 5.0375e+08 5.0408e+08  0.07%   298 128964s
 83051 33073 infeasible   18      5.0375e+08 5.0408e+08  0.07%   298 129091s
 83105 33097     cutoff   20      5.0375e+08 5.0408e+08  0.07%   298 129212s
 83159 33122 infeasible   23      5.0375e+08 5.0408e+08  0.07%   299 129337s
 83220 33124 5.0395e+08   14 2655 5.0375e+08 5.0408e+08  0.07%   299 129465s
 83266 33137 5.0389e+08   17 2528 5.0375e+08 5.0408e+08  0.07%   300 129615s
 83305 33154     cutoff   21      5.0375e+08 5.0408e+08  0.07%   300 129733s
 83344 33161     cutoff   22      5.0375e+08 5.0408e+08  0.07%   300 129842s
 83393 33183 5.0400e+08   13 2789 5.0375e+08 5.0408e+08  0.07%   301 129961s
 83449 33192 5.0396e+08   15 2534 5.0375e+08 5.0408e+08  0.07%   301 130090s
 83502 33213 5.0387e+08   19 2532 5.0375e+08 5.0408e+08  0.07%   301 130204s
 83557 33225     cutoff   23      5.0375e+08 5.0408e+08  0.07%   302 130630s
 83597 33232     cutoff   24      5.0375e+08 5.0408e+08  0.07%   302 130985s
 83620 33242 infeasible   22      5.0375e+08 5.0408e+08  0.07%   302 131122s
 83646 33257 infeasible   23      5.0375e+08 5.0408e+08  0.07%   302 131240s
 83677 33256     cutoff   20      5.0375e+08 5.0408e+08  0.07%   303 131387s
 83708 33267 infeasible   21      5.0375e+08 5.0408e+08  0.07%   303 131530s
 83735 33274 infeasible   17      5.0375e+08 5.0408e+08  0.07%   303 131666s
 83768 33279 5.0390e+08   16 2802 5.0375e+08 5.0408e+08  0.07%   303 131793s
 83799 33284 5.0390e+08   17 2658 5.0375e+08 5.0408e+08  0.07%   303 131937s
 83820 33304 5.0386e+08   18 2656 5.0375e+08 5.0408e+08  0.07%   304 132124s
 83848 33323 5.0378e+08   19 2751 5.0375e+08 5.0408e+08  0.07%   304 132238s
 83892 33332 infeasible   20      5.0375e+08 5.0408e+08  0.07%   304 132363s
 83948 33340 5.0376e+08   23 2595 5.0375e+08 5.0408e+08  0.07%   304 132503s
 84003 33373 5.0393e+08   15 2607 5.0375e+08 5.0408e+08  0.07%   304 132600s
 84066 33385 5.0379e+08   22 2380 5.0375e+08 5.0408e+08  0.07%   304 132801s
 84121 33391     cutoff   23      5.0375e+08 5.0408e+08  0.07%   305 132918s
 84153 33411 5.0399e+08   14 2675 5.0375e+08 5.0408e+08  0.07%   305 133048s
 84197 33419 5.0377e+08   19 2622 5.0375e+08 5.0408e+08  0.07%   306 133181s
 84263 33426 5.0375e+08   22 2461 5.0375e+08 5.0408e+08  0.07%   306 133331s
 84310 33455 5.0396e+08   17 2794 5.0375e+08 5.0408e+08  0.06%   306 133453s
 84370 33465 5.0381e+08   20 2905 5.0375e+08 5.0408e+08  0.06%   307 133600s
 84420 33479 5.0378e+08   23 2816 5.0375e+08 5.0408e+08  0.06%   307 133749s
 84472 33486     cutoff   25      5.0375e+08 5.0408e+08  0.06%   307 133927s
 84489 33511 5.0388e+08   18 2611 5.0375e+08 5.0408e+08  0.06%   307 134068s
 84546 33521     cutoff   23      5.0375e+08 5.0408e+08  0.06%   308 134183s
 84602 33541 5.0384e+08   14 2664 5.0375e+08 5.0408e+08  0.06%   308 134325s
 84660 33563     cutoff   19      5.0375e+08 5.0408e+08  0.06%   309 134458s
 84714 33570     cutoff   25      5.0375e+08 5.0408e+08  0.06%   309 134599s
 84767 33601 5.0397e+08   17 2606 5.0375e+08 5.0408e+08  0.06%   309 134789s
 84818 33617 infeasible   22      5.0375e+08 5.0408e+08  0.06%   310 134924s
 84864 33626     cutoff   17      5.0375e+08 5.0408e+08  0.06%   310 135045s
 84923 33644 5.0388e+08   18 2593 5.0375e+08 5.0408e+08  0.06%   310 135176s
 84977 33674 5.0377e+08   21 2729 5.0375e+08 5.0407e+08  0.06%   311 135313s
 85041 33678 infeasible   12      5.0375e+08 5.0407e+08  0.06%   311 135453s
 85097 33700 5.0388e+08   17 2595 5.0375e+08 5.0407e+08  0.06%   312 135559s
 85161 33715 5.0377e+08   20 2677 5.0375e+08 5.0407e+08  0.06%   312 135699s
 85220 33739 5.0392e+08   17 2683 5.0375e+08 5.0407e+08  0.06%   312 135820s
 85280 33757 infeasible   23      5.0375e+08 5.0407e+08  0.06%   313 135973s
 85330 33771     cutoff   22      5.0375e+08 5.0407e+08  0.06%   313 136095s
 85389 33790 5.0385e+08   18 2561 5.0375e+08 5.0407e+08  0.06%   314 136246s
 85438 33811     cutoff   23      5.0375e+08 5.0407e+08  0.06%   314 136385s
 85493 33837 5.0398e+08   14 2782 5.0375e+08 5.0407e+08  0.06%   314 136512s
 85557 33843 5.0380e+08   18 2601 5.0375e+08 5.0407e+08  0.06%   315 136638s
 85619 33862 5.0389e+08   15 2861 5.0375e+08 5.0407e+08  0.06%   315 136764s
 85678 33885     cutoff   20      5.0375e+08 5.0407e+08  0.06%   315 136873s
 85739 33900     cutoff   22      5.0375e+08 5.0407e+08  0.06%   316 136989s
 85806 33916 5.0399e+08   16 2549 5.0375e+08 5.0407e+08  0.06%   316 137135s
 85858 33958 5.0391e+08   19 2556 5.0375e+08 5.0407e+08  0.06%   316 137228s
 85922 33981     cutoff   23      5.0375e+08 5.0407e+08  0.06%   316 137342s
 85983 33990     cutoff   26      5.0375e+08 5.0407e+08  0.06%   317 137465s
 86048 34008 5.0388e+08   21 2703 5.0375e+08 5.0407e+08  0.06%   317 137574s
 86100 34012 5.0376e+08   29 2075 5.0375e+08 5.0407e+08  0.06%   317 137701s
 86146 34028 5.0375e+08   30 2073 5.0375e+08 5.0407e+08  0.06%   318 137862s
 86184 34038 5.0375e+08   32 2094 5.0375e+08 5.0407e+08  0.06%   318 138002s
 86233 34051     cutoff   36      5.0375e+08 5.0407e+08  0.06%   318 138124s
 86290 34070 5.0388e+08   16 3006 5.0375e+08 5.0407e+08  0.06%   319 138272s
 86341 34077     cutoff   20      5.0375e+08 5.0407e+08  0.06%   319 138394s
 86400 34094     cutoff   22      5.0375e+08 5.0407e+08  0.06%   320 138524s
 86457 34114 5.0394e+08   14 2608 5.0375e+08 5.0407e+08  0.06%   320 138658s
 86515 34124     cutoff   21      5.0375e+08 5.0407e+08  0.06%   320 138788s
 86570 34135 infeasible   22      5.0375e+08 5.0407e+08  0.06%   321 138991s
 86607 34145 5.0394e+08   18 2554 5.0375e+08 5.0407e+08  0.06%   321 139130s
 86657 34156 5.0384e+08   22 2524 5.0375e+08 5.0407e+08  0.06%   321 139257s
 86710 34183 5.0377e+08   25 2482 5.0375e+08 5.0407e+08  0.06%   321 139396s
 86769 34187 5.0397e+08   16 2671 5.0375e+08 5.0407e+08  0.06%   322 139578s
 86807 34201 5.0390e+08   19 2618 5.0375e+08 5.0407e+08  0.06%   322 139759s
 86845 34219 5.0382e+08   20 2696 5.0375e+08 5.0407e+08  0.06%   323 139897s
 86885 34212     cutoff   22      5.0375e+08 5.0407e+08  0.06%   323 140036s
 86934 34248 5.0397e+08   13 2695 5.0375e+08 5.0407e+08  0.06%   323 140183s
 86984 34254 5.0376e+08   19 2538 5.0375e+08 5.0407e+08  0.06%   324 140328s
 87042 34289 5.0395e+08   16 2472 5.0375e+08 5.0407e+08  0.06%   324 140461s
 87101 34300     cutoff   23      5.0375e+08 5.0407e+08  0.06%   324 140581s
 87160 34323 5.0398e+08   17 2581 5.0375e+08 5.0407e+08  0.06%   325 140725s
 87205 34357     cutoff   18      5.0375e+08 5.0407e+08  0.06%   325 140847s
 87266 34363 infeasible   23      5.0375e+08 5.0407e+08  0.06%   325 141019s
 87316 34389 5.0394e+08   14 2685 5.0375e+08 5.0407e+08  0.06%   326 141131s
 87362 34409     cutoff   21      5.0375e+08 5.0407e+08  0.06%   326 141248s
 87420 34421 5.0398e+08   14 2698 5.0375e+08 5.0407e+08  0.06%   326 141379s
 87478 34448 5.0388e+08   17 2542 5.0375e+08 5.0407e+08  0.06%   327 141491s
 87535 34464 5.0376e+08   20 2519 5.0375e+08 5.0407e+08  0.06%   327 141605s
 87603 34482 5.0395e+08   17 2692 5.0375e+08 5.0407e+08  0.06%   327 141739s
 87658 34499 5.0378e+08   23 2665 5.0375e+08 5.0407e+08  0.06%   328 141878s
 87711 34515 5.0375e+08   23 2704 5.0375e+08 5.0407e+08  0.06%   328 141995s
 87767 34545     cutoff   24      5.0375e+08 5.0407e+08  0.06%   328 142209s
 87827 34548 5.0400e+08   13 2739 5.0375e+08 5.0407e+08  0.06%   329 142321s
 87874 34553 5.0390e+08   14 2759 5.0375e+08 5.0407e+08  0.06%   329 142419s
 87933 34558 5.0376e+08   19 2693 5.0375e+08 5.0407e+08  0.06%   329 142515s
 88000 34575 5.0379e+08   19 2590 5.0375e+08 5.0407e+08  0.06%   329 142621s
 88066 34594     cutoff   21      5.0375e+08 5.0407e+08  0.06%   330 142828s
 88129 34624     cutoff   21      5.0375e+08 5.0406e+08  0.06%   330 142951s
 88186 34632 5.0376e+08   19 2585 5.0375e+08 5.0406e+08  0.06%   330 143040s
 88252 34642 5.0377e+08   18 2728 5.0375e+08 5.0406e+08  0.06%   330 143106s
 88322 34644     cutoff   21      5.0375e+08 5.0406e+08  0.06%   330 143196s
 88388 34647 5.0381e+08   17 2628 5.0375e+08 5.0406e+08  0.06%   330 143275s
 88455 34658 5.0396e+08   14 2630 5.0375e+08 5.0406e+08  0.06%   330 143359s
 88518 34648     cutoff   21      5.0375e+08 5.0406e+08  0.06%   330 143440s
 88582 34660 5.0375e+08   21 2584 5.0375e+08 5.0406e+08  0.06%   331 143530s
 88648 34661 5.0376e+08   23 2392 5.0375e+08 5.0406e+08  0.06%   331 143605s
 88718 34671     cutoff   21      5.0375e+08 5.0406e+08  0.06%   331 143687s
 88788 34671     cutoff   22      5.0375e+08 5.0406e+08  0.06%   331 143776s
 88854 34691     cutoff   23      5.0375e+08 5.0406e+08  0.06%   331 143865s
 88916 34699 5.0392e+08   16 2457 5.0375e+08 5.0406e+08  0.06%   331 143947s
 88980 34706 5.0382e+08   20 2412 5.0375e+08 5.0406e+08  0.06%   331 144045s
 89038 34709 5.0378e+08   20 2515 5.0375e+08 5.0406e+08  0.06%   331 144130s
 89100 34712     cutoff   21      5.0375e+08 5.0406e+08  0.06%   332 144241s
 89167 34721     cutoff   20      5.0375e+08 5.0406e+08  0.06%   332 144379s
 89228 34732 5.0385e+08   18 2534 5.0375e+08 5.0406e+08  0.06%   332 144492s
 89283 34736 5.0378e+08   21 2524 5.0375e+08 5.0406e+08  0.06%   332 144583s
 89343 34749 5.0380e+08   19 2605 5.0375e+08 5.0406e+08  0.06%   332 144685s
 89406 34751     cutoff   21      5.0375e+08 5.0406e+08  0.06%   333 144763s
 89472 34749     cutoff   21      5.0375e+08 5.0406e+08  0.06%   333 144943s
 89510 34760 5.0386e+08   17 2491 5.0375e+08 5.0406e+08  0.06%   333 145059s
 89559 34760     cutoff   21      5.0375e+08 5.0406e+08  0.06%   333 145145s
 89623 34766 5.0382e+08   18 2522 5.0375e+08 5.0406e+08  0.06%   334 145246s
 89685 34766     cutoff   17      5.0375e+08 5.0406e+08  0.06%   334 145344s
 89746 34775 5.0392e+08   14 2845 5.0375e+08 5.0406e+08  0.06%   334 145431s
 89807 34771 5.0387e+08   17 2659 5.0375e+08 5.0406e+08  0.06%   334 145513s
 89871 34774 5.0376e+08   20 2786 5.0375e+08 5.0406e+08  0.06%   334 145791s
 89916 34773 5.0378e+08   21 2593 5.0375e+08 5.0406e+08  0.06%   335 145899s
 89962 34766     cutoff   22      5.0375e+08 5.0406e+08  0.06%   335 145989s
 90024 34773     cutoff   21      5.0375e+08 5.0406e+08  0.06%   335 146077s
 90086 34769 5.0384e+08   17 2654 5.0375e+08 5.0406e+08  0.06%   335 146158s
 90150 34761 5.0376e+08   20 2610 5.0375e+08 5.0406e+08  0.06%   335 146272s
 90213 34758 5.0390e+08   16 2713 5.0375e+08 5.0406e+08  0.06%   335 146400s
 90260 34781     cutoff   19      5.0375e+08 5.0406e+08  0.06%   336 146511s
 90321 34786 5.0375e+08   22 2625 5.0375e+08 5.0406e+08  0.06%   336 146599s
 90382 34774     cutoff   22      5.0375e+08 5.0406e+08  0.06%   336 146692s
 90438 34789 5.0382e+08   17 2684 5.0375e+08 5.0406e+08  0.06%   336 146786s
 90499 34796 5.0398e+08   16 2548 5.0375e+08 5.0406e+08  0.06%   337 146871s
 90558 34801 5.0383e+08   20 2588 5.0375e+08 5.0406e+08  0.06%   337 146964s
 90615 34796     cutoff   23      5.0375e+08 5.0406e+08  0.06%   337 147052s
 90670 34808 5.0381e+08   22 2455 5.0375e+08 5.0406e+08  0.06%   338 147450s
 90708 34806 5.0375e+08   24 2522 5.0375e+08 5.0406e+08  0.06%   338 147552s
 90745 34809 5.0384e+08   19 2637 5.0375e+08 5.0406e+08  0.06%   338 147650s
 90798 34802     cutoff   21      5.0375e+08 5.0406e+08  0.06%   338 147768s
 90857 34803     cutoff   21      5.0375e+08 5.0406e+08  0.06%   338 147860s
 90912 34804 5.0381e+08   21 2524 5.0375e+08 5.0406e+08  0.06%   338 147938s
 90977 34806 5.0377e+08   20 2658 5.0375e+08 5.0406e+08  0.06%   338 148034s
 91035 34809 5.0390e+08   17 2524 5.0375e+08 5.0406e+08  0.06%   339 148121s
 91098 34814 5.0377e+08   21 2590 5.0375e+08 5.0406e+08  0.06%   339 148246s
 91159 34823 5.0377e+08   22 2466 5.0375e+08 5.0406e+08  0.06%   339 148333s
 91225 34832     cutoff   21      5.0375e+08 5.0406e+08  0.06%   340 148411s
 91292 34825     cutoff   21      5.0375e+08 5.0406e+08  0.06%   340 148514s
 91351 34830     cutoff   20      5.0375e+08 5.0406e+08  0.06%   340 148617s
 91406 34843 5.0385e+08   15 2579 5.0375e+08 5.0406e+08  0.06%   340 148705s
 91467 34857 5.0377e+08   18 2532 5.0375e+08 5.0406e+08  0.06%   340 148990s
 91527 34859 5.0377e+08   17 2524 5.0375e+08 5.0406e+08  0.06%   341 149107s
 91559 34856 5.0379e+08   17 2564 5.0375e+08 5.0406e+08  0.06%   341 149200s
 91608 34859     cutoff   17      5.0375e+08 5.0406e+08  0.06%   341 149286s
 91659 34871 5.0385e+08   18 2376 5.0375e+08 5.0406e+08  0.06%   341 149370s
 91725 34869 5.0377e+08   21 2365 5.0375e+08 5.0406e+08  0.06%   341 149492s
 91784 34862     cutoff   20      5.0375e+08 5.0406e+08  0.06%   341 149574s
 91845 34869     cutoff   19      5.0375e+08 5.0406e+08  0.06%   341 149662s
 91902 34871     cutoff   20      5.0375e+08 5.0406e+08  0.06%   342 149779s
 91954 34875     cutoff   20      5.0375e+08 5.0406e+08  0.06%   342 149862s
 92008 34895 5.0385e+08   17 2433 5.0375e+08 5.0406e+08  0.06%   342 149971s
 92070 34898     cutoff   19      5.0375e+08 5.0406e+08  0.06%   342 150182s
 92113 34897     cutoff   20      5.0375e+08 5.0406e+08  0.06%   342 150274s
 92154 34899     cutoff   21      5.0375e+08 5.0406e+08  0.06%   342 150385s
 92212 34902 5.0381e+08   17 2416 5.0375e+08 5.0406e+08  0.06%   343 150472s
 92275 34916 5.0376e+08   19 2434 5.0375e+08 5.0406e+08  0.06%   343 150562s
 92335 34929 5.0383e+08   16 2593 5.0375e+08 5.0406e+08  0.06%   343 150694s
 92388 34943     cutoff   18      5.0375e+08 5.0406e+08  0.06%   343 150782s
 92430 34961     cutoff   17      5.0375e+08 5.0406e+08  0.06%   343 150865s
 92484 34963     cutoff   18      5.0375e+08 5.0406e+08  0.06%   344 150947s
 92550 34980 5.0377e+08   17 2518 5.0375e+08 5.0406e+08  0.06%   344 151027s
 92615 34991 5.0385e+08   17 2441 5.0375e+08 5.0406e+08  0.06%   344 151102s
 92668 34994     cutoff   19      5.0375e+08 5.0406e+08  0.06%   344 151262s
 92719 35002 infeasible   21      5.0375e+08 5.0406e+08  0.06%   344 151356s
 92765 35005 5.0381e+08   17 2428 5.0375e+08 5.0406e+08  0.06%   344 151432s
 92818 35004     cutoff   20      5.0375e+08 5.0406e+08  0.06%   344 151522s
 92875 35020 5.0391e+08   15 2448 5.0375e+08 5.0406e+08  0.06%   344 151597s
 92929 35025 5.0385e+08   18 2381 5.0375e+08 5.0406e+08  0.06%   344 151689s
 92990 35036 5.0377e+08   21 2371 5.0375e+08 5.0406e+08  0.06%   345 151783s
 93052 35214     cutoff   24      5.0375e+08 5.0406e+08  0.06%   345 151837s
 93298 35359 5.0375e+08   58  499 5.0375e+08 5.0406e+08  0.06%   344 151869s
 93539 35477 5.0375e+08   37  533 5.0375e+08 5.0406e+08  0.06%   343 151913s
 93738 35653     cutoff   41      5.0375e+08 5.0406e+08  0.06%   343 151947s
 93998 35818     cutoff   50      5.0375e+08 5.0406e+08  0.06%   342 151980s
 94254 35982     cutoff   39      5.0375e+08 5.0406e+08  0.06%   341 152014s
 94517 36128 5.0375e+08   66  475 5.0375e+08 5.0406e+08  0.06%   341 152061s
 94763 36310 5.0375e+08   51  520 5.0375e+08 5.0406e+08  0.06%   340 152095s
 95023 36318 5.0375e+08   78  444 5.0375e+08 5.0406e+08  0.06%   339 152150s
 95038 36460 5.0375e+08   79  432 5.0375e+08 5.0406e+08  0.06%   339 152183s
 95293 36663 5.0375e+08   43  534 5.0375e+08 5.0406e+08  0.06%   338 152212s
 95563 36793 5.0375e+08   61  440 5.0375e+08 5.0406e+08  0.06%   338 152246s
 95809 36917 5.0375e+08   35  543 5.0375e+08 5.0406e+08  0.06%   337 152287s
 96051 36953     cutoff   36      5.0375e+08 5.0406e+08  0.06%   336 152320s
 96282 37116     cutoff   36      5.0375e+08 5.0406e+08  0.06%   336 152351s
 96546 37242 5.0375e+08   45  466 5.0375e+08 5.0406e+08  0.06%   335 152382s
 96785 37335 5.0375e+08   40  553 5.0375e+08 5.0406e+08  0.06%   334 152420s
 96990 37446 5.0375e+08   48  549 5.0375e+08 5.0406e+08  0.06%   334 152452s
 97241 37567 5.0375e+08   56  503 5.0375e+08 5.0406e+08  0.06%   333 152482s
 97474 37733 5.0375e+08   45  536 5.0375e+08 5.0406e+08  0.06%   332 152514s
 97716 37810 5.0375e+08   55  463 5.0375e+08 5.0406e+08  0.06%   332 152556s
 97934 37990 5.0375e+08   41  510 5.0375e+08 5.0406e+08  0.06%   331 152588s
 98196 38166 5.0375e+08   65  478 5.0375e+08 5.0406e+08  0.06%   331 152620s
 98450 38280 5.0376e+08   46  529 5.0375e+08 5.0406e+08  0.06%   330 152652s
 98669 38426 5.0375e+08   50  515 5.0375e+08 5.0406e+08  0.06%   329 152690s
 98904 38535 5.0375e+08   63  493 5.0375e+08 5.0406e+08  0.06%   329 152724s
 99056 38632 5.0375e+08   66  486 5.0375e+08 5.0406e+08  0.06%   328 152857s
 99258 38824 5.0375e+08   40  503 5.0375e+08 5.0406e+08  0.06%   328 152890s
 99527 38976 5.0375e+08   43  575 5.0375e+08 5.0406e+08  0.06%   327 152922s
 99770 39081 5.0375e+08   58  522 5.0375e+08 5.0406e+08  0.06%   327 152965s
 99984 39264 5.0375e+08   36  540 5.0375e+08 5.0406e+08  0.06%   326 152997s
 100242 39416 5.0375e+08   41  504 5.0375e+08 5.0406e+08  0.06%   325 153030s
 100501 39546 5.0375e+08   68  456 5.0375e+08 5.0406e+08  0.06%   325 153073s
 100758 39717 5.0376e+08   46  478 5.0375e+08 5.0406e+08  0.06%   324 153106s
 101014 39844 5.0375e+08   73  409 5.0375e+08 5.0406e+08  0.06%   323 153185s
 101237 40047 5.0375e+08   52  494 5.0375e+08 5.0406e+08  0.06%   323 153283s
 101484 40165     cutoff   79      5.0375e+08 5.0406e+08  0.06%   322 153315s
 101736 40309 5.0375e+08   44  509 5.0375e+08 5.0406e+08  0.06%   322 153349s
 101993 40457 5.0376e+08   38  538 5.0375e+08 5.0406e+08  0.06%   321 153401s
 102247 40579 5.0375e+08   64  494 5.0375e+08 5.0406e+08  0.06%   320 153475s
 102447 40584 5.0375e+08   69  484 5.0375e+08 5.0406e+08  0.06%   320 153527s
 102493 40712 5.0375e+08   42  500 5.0375e+08 5.0406e+08  0.06%   320 153562s
 102688 40816 5.0375e+08   69  447 5.0375e+08 5.0406e+08  0.06%   319 153593s
 102873 40903 5.0375e+08   37  499 5.0375e+08 5.0406e+08  0.06%   319 153626s
 103055 41012     cutoff   46      5.0375e+08 5.0406e+08  0.06%   318 153703s
 103219 41050     cutoff   39      5.0375e+08 5.0406e+08  0.06%   318 153753s
 103298 41088 5.0375e+08   41  526 5.0375e+08 5.0406e+08  0.06%   318 153810s
 103350 41154 5.0375e+08   40  518 5.0375e+08 5.0406e+08  0.06%   318 153841s
 103510 41261 5.0375e+08   42  528 5.0375e+08 5.0406e+08  0.06%   317 153888s
 103651 41373 5.0375e+08   43  518 5.0375e+08 5.0406e+08  0.06%   317 153935s
 103819 41483     cutoff   44      5.0375e+08 5.0406e+08  0.06%   317 153989s
 104033 41642 5.0375e+08   48  493 5.0375e+08 5.0406e+08  0.06%   316 154031s
 104303 41759     cutoff   50      5.0375e+08 5.0406e+08  0.06%   315 154079s
 104573 41945 5.0375e+08   62  486 5.0375e+08 5.0406e+08  0.06%   315 154119s
H104843 41945                    5.037502e+08 5.0406e+08  0.06%   314 154127s
 104843 41942 5.0381e+08   19 2467 5.0375e+08 5.0406e+08  0.06%   314 154229s
 104896 41957     cutoff   17      5.0375e+08 5.0406e+08  0.06%   314 154308s
 104957 41960 infeasible   21      5.0375e+08 5.0406e+08  0.06%   315 154466s
 105022 41963     cutoff   20      5.0375e+08 5.0406e+08  0.06%   315 154556s
 105067 41968     cutoff   19      5.0375e+08 5.0406e+08  0.06%   315 154640s
 105124 41973 infeasible   21      5.0375e+08 5.0406e+08  0.06%   315 154730s
 105175 41977 5.0382e+08   17 2610 5.0375e+08 5.0406e+08  0.06%   315 154807s
 105241 41969 5.0394e+08   15 2587 5.0375e+08 5.0406e+08  0.06%   316 154882s
 105302 41972 5.0377e+08   21 2519 5.0375e+08 5.0406e+08  0.06%   316 154969s
 105357 41980 5.0378e+08   22 2379 5.0375e+08 5.0406e+08  0.06%   316 155092s
 105405 41989     cutoff   21      5.0375e+08 5.0406e+08  0.06%   316 155183s
 105458 41978     cutoff   21      5.0375e+08 5.0406e+08  0.06%   316 155272s
 105513 41974     cutoff   17      5.0375e+08 5.0406e+08  0.06%   316 155396s
 105549 41977 5.0385e+08   19 2448 5.0375e+08 5.0406e+08  0.06%   316 155484s
 105608 41977     cutoff   22      5.0375e+08 5.0406e+08  0.06%   317 155566s
 105658 41979     cutoff   20      5.0375e+08 5.0406e+08  0.06%   317 155688s
 105720 41976 5.0376e+08   21 2491 5.0375e+08 5.0406e+08  0.06%   317 155772s
 105773 41981 5.0383e+08   20 2630 5.0375e+08 5.0406e+08  0.06%   317 155886s
 105820 41996 infeasible   17      5.0375e+08 5.0406e+08  0.06%   317 155967s
 105879 42007 5.0398e+08   14 3058 5.0375e+08 5.0406e+08  0.06%   318 156052s
 105938 42012 5.0384e+08   21 2744 5.0375e+08 5.0406e+08  0.06%   318 156135s
 105995 42019 5.0380e+08   21 2848 5.0375e+08 5.0406e+08  0.06%   318 156221s
 106060 42021     cutoff   22      5.0375e+08 5.0406e+08  0.06%   318 156368s
 106111 42020 5.0385e+08   20 2808 5.0375e+08 5.0406e+08  0.06%   318 156512s
 106156 42017 5.0381e+08   21 2800 5.0375e+08 5.0406e+08  0.06%   318 156651s
 106203 42036 5.0378e+08   22 2804 5.0375e+08 5.0406e+08  0.06%   318 156746s
 106254 42024     cutoff   22      5.0375e+08 5.0406e+08  0.06%   319 156822s
 106307 42028     cutoff   18      5.0375e+08 5.0406e+08  0.06%   319 156906s
 106367 42033 5.0380e+08   21 2731 5.0375e+08 5.0406e+08  0.06%   319 157093s
 106382 42034 5.0377e+08   22 2736 5.0375e+08 5.0406e+08  0.06%   319 157196s
 106410 42045     cutoff   23      5.0375e+08 5.0406e+08  0.06%   319 157291s
 106457 42044     cutoff   21      5.0375e+08 5.0406e+08  0.06%   319 157464s
 106522 42050     cutoff   21      5.0375e+08 5.0406e+08  0.06%   319 157568s
 106574 42058 5.0389e+08   18 2820 5.0375e+08 5.0406e+08  0.06%   319 157652s
 106637 42065     cutoff   24      5.0375e+08 5.0406e+08  0.06%   320 157757s
 106694 42082     cutoff   22      5.0375e+08 5.0406e+08  0.06%   320 157834s
 106753 42087 5.0376e+08   22 2840 5.0375e+08 5.0406e+08  0.06%   320 157914s
 106816 42097 5.0376e+08   20 2986 5.0375e+08 5.0406e+08  0.06%   320 157994s
 106882 42114 5.0385e+08   18 2808 5.0375e+08 5.0406e+08  0.06%   320 158062s
 106951 42122     cutoff   20      5.0375e+08 5.0406e+08  0.06%   320 158136s
 107011 42142     cutoff   20      5.0375e+08 5.0406e+08  0.06%   321 158222s
 107065 42147 5.0388e+08   16 2917 5.0375e+08 5.0406e+08  0.06%   321 158296s
 107134 42148     cutoff   22      5.0375e+08 5.0406e+08  0.06%   321 158364s
 107199 42144     cutoff   20      5.0375e+08 5.0406e+08  0.06%   321 158438s
 107253 42144 5.0381e+08   18 2879 5.0375e+08 5.0406e+08  0.06%   321 158518s
 107311 42145 5.0386e+08   16 2957 5.0375e+08 5.0406e+08  0.06%   321 158591s
 107374 42138     cutoff   20      5.0375e+08 5.0406e+08  0.06%   321 158675s
 107421 42142 5.0383e+08   17 2920 5.0375e+08 5.0406e+08  0.06%   322 158776s
 107482 42161 infeasible   18      5.0375e+08 5.0406e+08  0.06%   322 158859s
 107541 42169 5.0394e+08   16 2522 5.0375e+08 5.0406e+08  0.06%   322 158948s
 107597 42172     cutoff   17      5.0375e+08 5.0406e+08  0.06%   322 159030s
 107632 42186 5.0385e+08   19 2521 5.0375e+08 5.0406e+08  0.06%   322 159123s
 107686 42199     cutoff   20      5.0375e+08 5.0406e+08  0.06%   323 159199s
 107747 42198     cutoff   20      5.0375e+08 5.0406e+08  0.06%   323 159278s
 107808 42209     cutoff   22      5.0375e+08 5.0406e+08  0.06%   323 159353s
 107871 42195 5.0377e+08   21 2567 5.0375e+08 5.0406e+08  0.06%   323 159454s
 107930 42198     cutoff   17      5.0375e+08 5.0406e+08  0.06%   323 159525s
 107975 42196 5.0396e+08   15 2617 5.0375e+08 5.0406e+08  0.06%   323 159601s
 108033 42194 5.0379e+08   21 2654 5.0375e+08 5.0406e+08  0.06%   323 159708s
 108085 42191 5.0382e+08   21 2561 5.0375e+08 5.0406e+08  0.06%   323 159787s
 108138 42192 5.0382e+08   19 2704 5.0375e+08 5.0406e+08  0.06%   324 159862s
 108201 42193 5.0387e+08   18 2606 5.0375e+08 5.0406e+08  0.06%   324 159941s
 108258 42188 5.0376e+08   21 2678 5.0375e+08 5.0406e+08  0.06%   324 160053s
 108311 42202 5.0380e+08   21 2597 5.0375e+08 5.0406e+08  0.06%   324 160151s
 108361 42203 5.0376e+08   20 2734 5.0375e+08 5.0406e+08  0.06%   324 160276s
 108410 42204 5.0392e+08   16 2594 5.0375e+08 5.0406e+08  0.06%   325 160367s
 108455 42211     cutoff   21      5.0375e+08 5.0406e+08  0.06%   325 160461s
 108507 42215     cutoff   23      5.0375e+08 5.0406e+08  0.06%   325 160561s
 108547 42226 5.0375e+08   20 2682 5.0375e+08 5.0406e+08  0.06%   325 160642s
 108608 42226 5.0376e+08   21 2592 5.0375e+08 5.0406e+08  0.06%   325 160720s
 108672 42232 5.0394e+08   15 2595 5.0375e+08 5.0406e+08  0.06%   325 160833s
 108724 42249     cutoff   22      5.0375e+08 5.0406e+08  0.06%   326 160915s
 108777 42258     cutoff   23      5.0375e+08 5.0406e+08  0.06%   326 160994s
 108838 42261     cutoff   22      5.0375e+08 5.0406e+08  0.06%   326 161073s
 108897 42265     cutoff   22      5.0375e+08 5.0406e+08  0.06%   326 161153s
 108955 42280     cutoff   24      5.0375e+08 5.0406e+08  0.06%   326 161223s
 109014 42283 5.0390e+08   17 2420 5.0375e+08 5.0406e+08  0.06%   326 161312s
 109077 42298 5.0380e+08   21 2374 5.0375e+08 5.0406e+08  0.06%   326 161394s
 109140 42318     cutoff   21      5.0375e+08 5.0406e+08  0.06%   326 161489s
 109202 42334 infeasible   20      5.0375e+08 5.0406e+08  0.06%   327 161568s
 109264 42351 5.0388e+08   18 2457 5.0375e+08 5.0406e+08  0.06%   327 161651s
 109327 42353 5.0382e+08   21 2414 5.0375e+08 5.0406e+08  0.06%   327 161724s
 109393 42373 5.0378e+08   20 2561 5.0375e+08 5.0406e+08  0.06%   327 161814s
 109451 42391     cutoff   22      5.0375e+08 5.0406e+08  0.06%   327 161879s
 109515 42394 5.0376e+08   22 2462 5.0375e+08 5.0406e+08  0.06%   327 161971s
 109576 42408 5.0388e+08   17 2455 5.0375e+08 5.0406e+08  0.06%   328 162054s
 109630 42429     cutoff   21      5.0375e+08 5.0406e+08  0.06%   328 162134s
 109689 42454 5.0379e+08   20 2456 5.0375e+08 5.0406e+08  0.06%   328 162210s
 109748 42474     cutoff   20      5.0375e+08 5.0406e+08  0.06%   328 162303s
 109808 42488 5.0389e+08   15 3063 5.0375e+08 5.0406e+08  0.06%   328 162373s
 109866 42500 5.0381e+08   19 2890 5.0375e+08 5.0406e+08  0.06%   328 162459s
 109914 42520     cutoff   22      5.0375e+08 5.0406e+08  0.06%   329 162535s
 109972 42529 5.0385e+08   17 2888 5.0375e+08 5.0406e+08  0.06%   329 162626s
 110031 42528 5.0387e+08   16 2960 5.0375e+08 5.0406e+08  0.06%   329 162705s
 110092 42539 5.0387e+08   17 2940 5.0375e+08 5.0406e+08  0.06%   329 162778s
 110155 42534 5.0376e+08   20 2936 5.0375e+08 5.0406e+08  0.06%   329 162848s
 110212 42548 5.0395e+08   15 2943 5.0375e+08 5.0406e+08  0.06%   329 162928s
 110268 42559     cutoff   22      5.0375e+08 5.0406e+08  0.06%   329 162996s
 110323 42579 5.0377e+08   20 2880 5.0375e+08 5.0406e+08  0.06%   329 163087s
 110383 42579 5.0378e+08   21 2785 5.0375e+08 5.0406e+08  0.06%   329 163161s
 110437 42587 5.0395e+08   17 2779 5.0375e+08 5.0406e+08  0.06%   330 163263s
 110491 42593     cutoff   23      5.0375e+08 5.0406e+08  0.06%   330 163334s
 110551 42597     cutoff   24      5.0375e+08 5.0406e+08  0.06%   330 163412s
 110603 42620 5.0386e+08   19 2793 5.0375e+08 5.0406e+08  0.06%   330 163513s
 110656 42638     cutoff   22      5.0375e+08 5.0406e+08  0.06%   330 163614s
 110718 42632     cutoff   24      5.0375e+08 5.0406e+08  0.06%   330 163734s
 110772 42631 5.0393e+08   16 2840 5.0375e+08 5.0406e+08  0.06%   330 163855s
 110818 42649 5.0389e+08   18 2818 5.0375e+08 5.0406e+08  0.06%   330 163961s
 110880 42651     cutoff   22      5.0375e+08 5.0406e+08  0.06%   330 164035s
 110941 42665 5.0387e+08   19 2801 5.0375e+08 5.0406e+08  0.06%   330 164128s
 110995 42677 5.0382e+08   21 2785 5.0375e+08 5.0406e+08  0.06%   331 164200s
 111043 42696     cutoff   23      5.0375e+08 5.0406e+08  0.06%   331 164271s
 111102 42729 5.0389e+08   17 2811 5.0375e+08 5.0406e+08  0.06%   331 164351s
 111159 42732 5.0376e+08   22 2786 5.0375e+08 5.0406e+08  0.06%   331 164473s
 111208 42735 5.0380e+08   20 2819 5.0375e+08 5.0406e+08  0.06%   331 164558s
 111251 42725     cutoff   20      5.0375e+08 5.0406e+08  0.06%   331 164648s
 111297 42722 5.0391e+08   14 2969 5.0375e+08 5.0406e+08  0.06%   331 164728s
 111355 42729 5.0376e+08   18 2804 5.0375e+08 5.0406e+08  0.06%   332 164817s
 111408 42757     cutoff   18      5.0375e+08 5.0406e+08  0.06%   332 164889s
 111466 42778     cutoff   18      5.0375e+08 5.0406e+08  0.06%   332 164967s
 111531 42781 5.0382e+08   18 2673 5.0375e+08 5.0406e+08  0.06%   332 165033s
 111590 42797     cutoff   20      5.0375e+08 5.0406e+08  0.06%   332 165108s
 111646 42799     cutoff   18      5.0375e+08 5.0406e+08  0.06%   332 165178s
 111698 42811     cutoff   21      5.0375e+08 5.0406e+08  0.06%   332 165271s
 111750 42823     cutoff   18      5.0375e+08 5.0406e+08  0.06%   332 165364s
 111800 42841 5.0378e+08   19 2679 5.0375e+08 5.0406e+08  0.06%   332 165450s
 111860 42846     cutoff   20      5.0375e+08 5.0406e+08  0.06%   332 165651s
 111905 42854 5.0377e+08   18 2697 5.0375e+08 5.0406e+08  0.06%   332 165788s
 111941 42863 5.0389e+08   17 2696 5.0375e+08 5.0406e+08  0.06%   332 165893s
 111986 42869     cutoff   23      5.0375e+08 5.0406e+08  0.06%   333 166021s
 112044 42872 5.0380e+08   20 2702 5.0375e+08 5.0406e+08  0.06%   333 166101s
 112105 42867 5.0386e+08   17 2691 5.0375e+08 5.0406e+08  0.06%   333 166169s
 112168 42859 5.0377e+08   19 2705 5.0375e+08 5.0406e+08  0.06%   333 166256s
 112220 42871 5.0387e+08   16 2760 5.0375e+08 5.0406e+08  0.06%   333 166336s
 112284 42870 infeasible   22      5.0375e+08 5.0406e+08  0.06%   333 166409s
 112351 42878     cutoff   20      5.0375e+08 5.0406e+08  0.06%   333 166490s
 112398 42888 5.0380e+08   18 2710 5.0375e+08 5.0406e+08  0.06%   333 166585s
 112456 42876     cutoff   18      5.0375e+08 5.0406e+08  0.06%   333 166662s
 112506 42870 5.0384e+08   16 2858 5.0375e+08 5.0406e+08  0.06%   333 166739s
 112562 42879 5.0380e+08   17 2828 5.0375e+08 5.0406e+08  0.06%   333 166941s
 112595 42875     cutoff   19      5.0375e+08 5.0406e+08  0.06%   333 167019s
 112634 42881 5.0382e+08   17 2860 5.0375e+08 5.0406e+08  0.06%   334 167103s
 112676 42885 5.0377e+08   18 2839 5.0375e+08 5.0406e+08  0.06%   334 167207s
 112722 42881 5.0378e+08   17 2858 5.0375e+08 5.0406e+08  0.06%   334 167281s
 112781 42898 5.0393e+08   14 2983 5.0375e+08 5.0406e+08  0.06%   334 167356s
 112832 42911 5.0378e+08   21 2652 5.0375e+08 5.0406e+08  0.06%   334 167435s
 112889 42898     cutoff   21      5.0375e+08 5.0406e+08  0.06%   334 167511s
 112950 42897     cutoff   21      5.0375e+08 5.0406e+08  0.06%   334 167588s
 113007 42903 5.0381e+08   18 2677 5.0375e+08 5.0406e+08  0.06%   334 167666s
 113066 42897 5.0376e+08   20 2709 5.0375e+08 5.0406e+08  0.06%   335 167740s
 113122 42907 5.0387e+08   16 2755 5.0375e+08 5.0406e+08  0.06%   335 167827s
 113184 42903     cutoff   22      5.0375e+08 5.0406e+08  0.06%   335 167916s
 113244 42904     cutoff   20      5.0375e+08 5.0406e+08  0.06%   335 167994s
 113304 42896 5.0377e+08   20 2680 5.0375e+08 5.0406e+08  0.06%   335 168100s
 113353 42911 5.0383e+08   15 2993 5.0375e+08 5.0406e+08  0.06%   335 168179s
 113412 42908 5.0380e+08   17 2819 5.0375e+08 5.0406e+08  0.06%   336 168255s
 113472 42912 5.0382e+08   16 2874 5.0375e+08 5.0406e+08  0.06%   336 168333s
 113536 42904 5.0378e+08   17 2843 5.0375e+08 5.0406e+08  0.06%   336 168417s
 113594 42907 5.0396e+08   13 2779 5.0375e+08 5.0406e+08  0.06%   336 168495s
 113650 42904 5.0382e+08   17 2613 5.0375e+08 5.0406e+08  0.06%   336 168570s
 113712 42902     cutoff   22      5.0375e+08 5.0406e+08  0.06%   336 168662s
 113766 42916     cutoff   20      5.0375e+08 5.0406e+08  0.06%   337 168751s
 113822 42920 5.0378e+08   17 2604 5.0375e+08 5.0406e+08  0.06%   337 168835s
 113881 42915 5.0380e+08   17 2640 5.0375e+08 5.0406e+08  0.06%   337 168912s
 113942 42909     cutoff   20      5.0375e+08 5.0406e+08  0.06%   337 168986s
 114002 42931 5.0376e+08   17 2632 5.0375e+08 5.0406e+08  0.06%   337 169065s
 114067 42938 5.0388e+08   17 2487 5.0375e+08 5.0406e+08  0.06%   337 169145s
 114118 42946     cutoff   21      5.0375e+08 5.0406e+08  0.06%   337 169227s
 114168 42950     cutoff   23      5.0375e+08 5.0406e+08  0.06%   338 169302s
 114220 42942     cutoff   21      5.0375e+08 5.0406e+08  0.06%   338 169378s
 114270 42948 5.0384e+08   17 2484 5.0375e+08 5.0406e+08  0.06%   338 169456s
 114326 42935     cutoff   21      5.0375e+08 5.0406e+08  0.06%   338 169546s
 114384 42959 5.0390e+08   15 2575 5.0375e+08 5.0406e+08  0.06%   338 169628s
 114441 42967     cutoff   21      5.0375e+08 5.0406e+08  0.06%   338 169732s
 114489 42962 infeasible   20      5.0375e+08 5.0406e+08  0.06%   339 169824s
 114520 42982     cutoff   21      5.0375e+08 5.0406e+08  0.06%   339 169917s
 114578 42988     cutoff   17      5.0375e+08 5.0406e+08  0.06%   339 169995s
 114632 42986     cutoff   20      5.0375e+08 5.0406e+08  0.06%   339 170071s
 114694 42980     cutoff   20      5.0375e+08 5.0406e+08  0.06%   339 170155s
 114751 43001 5.0398e+08   15 2729 5.0375e+08 5.0406e+08  0.06%   339 170232s
 114812 43003 5.0392e+08   19 2544 5.0375e+08 5.0406e+08  0.06%   339 170300s
 114872 43004 5.0384e+08   22 2532 5.0375e+08 5.0406e+08  0.06%   339 170398s
 114921 43015 5.0375e+08   25 2500 5.0375e+08 5.0406e+08  0.06%   340 170472s
 114975 43013     cutoff   28      5.0375e+08 5.0406e+08  0.06%   340 170543s
 115029 43023     cutoff   30      5.0375e+08 5.0406e+08  0.06%   340 170618s
 115085 43009     cutoff   25      5.0375e+08 5.0406e+08  0.06%   340 170690s
 115145 43013 5.0378e+08   23 2609 5.0375e+08 5.0406e+08  0.06%   340 170772s
 115203 43020 5.0392e+08   14 2804 5.0375e+08 5.0406e+08  0.06%   340 170871s
 115250 43019 5.0388e+08   17 2620 5.0375e+08 5.0406e+08  0.06%   340 170949s
 115298 43038 5.0376e+08   20 2743 5.0375e+08 5.0406e+08  0.06%   341 171030s
 115355 43038 5.0378e+08   21 2559 5.0375e+08 5.0406e+08  0.06%   341 171104s
 115405 43044     cutoff   22      5.0375e+08 5.0406e+08  0.06%   341 171181s
 115457 43037     cutoff   21      5.0375e+08 5.0406e+08  0.06%   341 171455s
 115512 43037 5.0384e+08   17 2600 5.0375e+08 5.0406e+08  0.06%   341 171544s
 115550 43032 5.0377e+08   19 2598 5.0375e+08 5.0406e+08  0.06%   341 171634s
 115600 43038 5.0390e+08   15 2686 5.0375e+08 5.0406e+08  0.06%   341 171724s
 115652 43035 5.0386e+08   17 2647 5.0375e+08 5.0406e+08  0.06%   341 171822s
 115697 43044 5.0378e+08   20 2611 5.0375e+08 5.0406e+08  0.06%   342 171897s
 115749 43047 5.0378e+08   20 2686 5.0375e+08 5.0406e+08  0.06%   342 171980s
 115806 43041 5.0382e+08   17 2626 5.0375e+08 5.0406e+08  0.06%   342 172071s
 115860 43044 5.0398e+08   16 2507 5.0375e+08 5.0406e+08  0.06%   342 172226s
 115903 43053 5.0391e+08   18 2460 5.0375e+08 5.0406e+08  0.06%   342 172363s
 115938 43059     cutoff   23      5.0375e+08 5.0406e+08  0.06%   342 172488s
 115986 43052     cutoff   22      5.0375e+08 5.0406e+08  0.06%   342 172569s
 116038 43047     cutoff   25      5.0375e+08 5.0406e+08  0.06%   342 172651s
 116092 43055     cutoff   21      5.0375e+08 5.0406e+08  0.06%   343 172734s
 116151 43060 5.0388e+08   19 2494 5.0375e+08 5.0406e+08  0.06%   343 172803s
 116212 43059 5.0378e+08   21 2580 5.0375e+08 5.0406e+08  0.06%   343 172884s
 116269 43061     cutoff   22      5.0375e+08 5.0406e+08  0.06%   343 172951s
 116331 43061 5.0377e+08   20 2627 5.0375e+08 5.0406e+08  0.06%   343 173037s
 116385 43063 5.0390e+08   17 2470 5.0375e+08 5.0406e+08  0.06%   343 173116s
 116445 43065 5.0377e+08   21 2527 5.0375e+08 5.0406e+08  0.06%   343 173187s
 116507 43064 5.0377e+08   22 2418 5.0375e+08 5.0406e+08  0.06%   343 173264s
 116561 43069     cutoff   21      5.0375e+08 5.0406e+08  0.06%   344 173479s
 116598 43069 5.0377e+08   20 2553 5.0375e+08 5.0406e+08  0.06%   344 173559s
 116628 43059     cutoff   21      5.0375e+08 5.0406e+08  0.06%   344 173649s
 116670 43056 5.0378e+08   21 2475 5.0375e+08 5.0406e+08  0.06%   344 173744s
 116725 43077 5.0394e+08   15 2879 5.0375e+08 5.0406e+08  0.06%   344 173822s
 116788 43073     cutoff   18      5.0375e+08 5.0406e+08  0.06%   344 173903s
 116842 43077 5.0390e+08   18 2711 5.0375e+08 5.0406e+08  0.06%   344 173979s
 116898 43081 5.0385e+08   20 2732 5.0375e+08 5.0406e+08  0.06%   344 174056s
 116960 43083     cutoff   18      5.0375e+08 5.0406e+08  0.06%   345 174302s
 117006 43095 5.0383e+08   19 2776 5.0375e+08 5.0406e+08  0.06%   345 174448s
 117032 43098 5.0387e+08   20 2680 5.0375e+08 5.0406e+08  0.06%   345 174586s
 117065 43097 5.0378e+08   22 2731 5.0375e+08 5.0406e+08  0.06%   345 174712s
 117108 43109     cutoff   22      5.0375e+08 5.0406e+08  0.06%   345 174801s
 117168 43123     cutoff   23      5.0375e+08 5.0406e+08  0.06%   345 174884s
 117216 43123 5.0376e+08   22 2765 5.0375e+08 5.0406e+08  0.06%   345 175068s
 117234 43118     cutoff   23      5.0375e+08 5.0406e+08  0.06%   345 175150s
 117257 43116     cutoff   22      5.0375e+08 5.0406e+08  0.06%   345 175233s
 117281 43120 5.0376e+08   21 2817 5.0375e+08 5.0406e+08  0.06%   345 175317s
 117327 43125     cutoff   20      5.0375e+08 5.0406e+08  0.06%   345 175399s
 117382 43135     cutoff   21      5.0375e+08 5.0406e+08  0.06%   345 175495s
 117436 43137     cutoff   23      5.0375e+08 5.0406e+08  0.06%   346 175583s
 117498 43159 5.0380e+08   22 2679 5.0375e+08 5.0406e+08  0.06%   346 175674s
 117554 43183 5.0377e+08   22 2667 5.0375e+08 5.0406e+08  0.06%   346 175759s
 117617 43192 5.0381e+08   20 2717 5.0375e+08 5.0406e+08  0.06%   346 175854s
 117682 43193 5.0378e+08   23 2652 5.0375e+08 5.0406e+08  0.06%   346 175937s
 117739 43206 infeasible   17      5.0375e+08 5.0406e+08  0.06%   346 176016s
 117796 43196 5.0383e+08   15 2658 5.0375e+08 5.0406e+08  0.06%   346 176095s
 117848 43211 5.0378e+08   17 2617 5.0375e+08 5.0406e+08  0.06%   346 176186s
 117901 43222     cutoff   17      5.0375e+08 5.0406e+08  0.06%   347 176259s
 117965 43242     cutoff   18      5.0375e+08 5.0406e+08  0.06%   347 176332s
 118028 43242 5.0377e+08   17 2577 5.0375e+08 5.0406e+08  0.06%   347 176409s
 118084 43251 5.0386e+08   17 2469 5.0375e+08 5.0406e+08  0.06%   347 176478s
 118138 43261     cutoff   21      5.0375e+08 5.0406e+08  0.06%   347 176549s
 118204 43281 5.0381e+08   18 2497 5.0375e+08 5.0406e+08  0.06%   347 176620s
 118264 43289 5.0387e+08   16 2478 5.0375e+08 5.0406e+08  0.06%   347 176692s
 118318 43287 5.0381e+08   18 2429 5.0375e+08 5.0406e+08  0.06%   347 176789s
 118386 43297 5.0378e+08   18 2487 5.0375e+08 5.0406e+08  0.06%   347 176878s
 118445 43311     cutoff   17      5.0375e+08 5.0406e+08  0.06%   347 176953s
 118495 43314     cutoff   20      5.0375e+08 5.0406e+08  0.06%   347 177029s
 118559 43313     cutoff   20      5.0375e+08 5.0406e+08  0.06%   347 177226s
 118616 43326 5.0379e+08   18 2458 5.0375e+08 5.0406e+08  0.06%   347 177308s
 118661 43329 5.0378e+08   19 2451 5.0375e+08 5.0406e+08  0.06%   347 177459s
 118703 43325     cutoff   20      5.0375e+08 5.0406e+08  0.06%   347 177546s
 118749 43330 5.0385e+08   15 2635 5.0375e+08 5.0406e+08  0.06%   347 177645s
 118786 43335     cutoff   18      5.0375e+08 5.0406e+08  0.06%   348 177730s
 118825 43358     cutoff   18      5.0375e+08 5.0406e+08  0.06%   348 177805s
 118887 43359 5.0378e+08   17 2607 5.0375e+08 5.0406e+08  0.06%   348 177881s
 118946 43358     cutoff   17      5.0375e+08 5.0406e+08  0.06%   348 177967s
 119005 43369 5.0386e+08   17 2464 5.0375e+08 5.0406e+08  0.06%   348 178040s
 119070 43360     cutoff   21      5.0375e+08 5.0406e+08  0.06%   348 178125s
 119134 43363 5.0381e+08   18 2491 5.0375e+08 5.0406e+08  0.06%   348 178195s
 119199 43375 5.0387e+08   16 2477 5.0375e+08 5.0406e+08  0.06%   348 178275s
 119249 43374 5.0383e+08   17 2456 5.0375e+08 5.0406e+08  0.06%   348 178373s
 119306 43378     cutoff   19      5.0375e+08 5.0406e+08  0.06%   348 178450s
 119362 43383 5.0389e+08   16 2504 5.0375e+08 5.0406e+08  0.06%   349 178708s
 119387 43396 5.0382e+08   19 2450 5.0375e+08 5.0406e+08  0.06%   349 178796s
 119428 43413 5.0379e+08   19 2504 5.0375e+08 5.0406e+08  0.06%   349 178879s
 119481 43424 5.0381e+08   17 2470 5.0375e+08 5.0406e+08  0.06%   349 178956s
 119530 43442 5.0375e+08   19 2490 5.0375e+08 5.0406e+08  0.06%   349 179037s
 119586 43453 5.0392e+08   15 2839 5.0375e+08 5.0406e+08  0.06%   349 179117s
 119639 43464 5.0377e+08   20 2785 5.0375e+08 5.0406e+08  0.06%   349 179221s
 119692 43477 5.0384e+08   19 2666 5.0375e+08 5.0406e+08  0.06%   349 179294s
 119742 43485 5.0375e+08   24 2583 5.0375e+08 5.0406e+08  0.06%   349 179366s
 119798 43501     cutoff   24      5.0375e+08 5.0406e+08  0.06%   349 179439s
 119860 43503     cutoff   23      5.0375e+08 5.0406e+08  0.06%   349 179655s
 119904 43504 5.0388e+08   17 2667 5.0375e+08 5.0406e+08  0.06%   349 179813s
 119937 43511 5.0377e+08   20 2664 5.0375e+08 5.0406e+08  0.06%   349 179915s
 119978 43526     cutoff   18      5.0375e+08 5.0406e+08  0.06%   349 180032s
 120027 43694 5.0375e+08   48  480 5.0375e+08 5.0406e+08  0.06%   349 180089s
 120282 43823     cutoff   60      5.0375e+08 5.0406e+08  0.06%   349 180121s
 120534 43981 5.0375e+08   53  555 5.0375e+08 5.0406e+08  0.06%   348 180157s
 120797 44082 5.0375e+08   50  514 5.0375e+08 5.0406e+08  0.06%   348 180277s
 120938 44197 5.0375e+08   63  447 5.0375e+08 5.0406e+08  0.06%   347 180314s
 121201 44342 5.0376e+08   50  485 5.0375e+08 5.0406e+08  0.06%   347 180357s
 121431 44487 5.0375e+08   75  427 5.0375e+08 5.0406e+08  0.06%   346 180390s
 121668 44569 5.0375e+08   67  488 5.0375e+08 5.0406e+08  0.06%   346 180423s
 121917 44596     cutoff   69      5.0375e+08 5.0406e+08  0.06%   345 180492s
 121950 44664 5.0375e+08   65  517 5.0375e+08 5.0406e+08  0.06%   345 180564s
 122090 44739 5.0375e+08   66  516 5.0375e+08 5.0406e+08  0.06%   345 180629s
 122222 44838 5.0375e+08   67  515 5.0375e+08 5.0406e+08  0.06%   345 180689s
 122362 44931 5.0375e+08   68  467 5.0375e+08 5.0406e+08  0.06%   344 180748s
 122502 44998 5.0375e+08   69  467 5.0375e+08 5.0406e+08  0.06%   344 180805s
 122640 45069 5.0375e+08   70  464 5.0375e+08 5.0406e+08  0.06%   344 180862s
 122779 45168 5.0375e+08   70  459 5.0375e+08 5.0406e+08  0.06%   343 180918s
 122920 45248 5.0375e+08   71  461 5.0375e+08 5.0406e+08  0.06%   343 180973s
 123060 45329 5.0375e+08   72  454 5.0375e+08 5.0406e+08  0.06%   343 181046s
 123203 45404 5.0375e+08   73  438 5.0375e+08 5.0406e+08  0.06%   342 181119s
 123343 45494 5.0375e+08   74  437 5.0375e+08 5.0406e+08  0.06%   342 181181s
 123484 45551 5.0375e+08   75  449 5.0375e+08 5.0406e+08  0.06%   342 181244s
 123624 45653 5.0375e+08   76  448 5.0375e+08 5.0406e+08  0.06%   341 181329s
 123790 45749 5.0375e+08   77  444 5.0375e+08 5.0406e+08  0.06%   341 181388s
 123977 45834 5.0375e+08   79  447 5.0375e+08 5.0406e+08  0.06%   341 181450s
 124171 45940     cutoff   44      5.0375e+08 5.0406e+08  0.06%   340 181510s
 124367 46042     cutoff   50      5.0375e+08 5.0406e+08  0.06%   340 181609s
 124571 46191 5.0375e+08   64  451 5.0375e+08 5.0406e+08  0.06%   339 181661s
 124801 46341     cutoff   51      5.0375e+08 5.0406e+08  0.06%   339 181726s
 125046 46488 5.0375e+08   52  507 5.0375e+08 5.0406e+08  0.06%   338 181855s
 125316 46685 5.0375e+08   79  412 5.0375e+08 5.0406e+08  0.06%   338 181892s
 125586 46831 5.0375e+08   51  501 5.0375e+08 5.0406e+08  0.06%   337 181943s
 125856 46991 5.0375e+08   48  508 5.0375e+08 5.0406e+08  0.06%   337 181981s
 126126 47146 5.0375e+08   73  398 5.0375e+08 5.0406e+08  0.06%   336 182016s
 126396 47331 5.0375e+08   59  473 5.0375e+08 5.0406e+08  0.06%   336 182069s
 126666 47495 5.0375e+08   57  515 5.0375e+08 5.0406e+08  0.06%   335 182104s
 126936 47634     cutoff   75      5.0375e+08 5.0406e+08  0.06%   334 182142s
 127206 47822 5.0375e+08   65  473 5.0375e+08 5.0406e+08  0.06%   334 182200s
 127476 47970 5.0375e+08   55  488 5.0375e+08 5.0406e+08  0.06%   333 182235s
 127746 48098 5.0375e+08   72  445 5.0375e+08 5.0406e+08  0.06%   333 182271s
 128016 48262 5.0375e+08   70  449 5.0375e+08 5.0406e+08  0.06%   332 182307s
 128286 48404 5.0375e+08   74  452 5.0375e+08 5.0406e+08  0.06%   332 182360s
 128554 48560 5.0375e+08   67  456 5.0375e+08 5.0406e+08  0.06%   331 182398s
 128822 48700 5.0375e+08   59  519 5.0375e+08 5.0406e+08  0.06%   331 182438s
 129054 48892 5.0376e+08   51  491 5.0375e+08 5.0406e+08  0.06%   330 182471s
 129324 49069     cutoff   74      5.0375e+08 5.0406e+08  0.06%   330 182504s
 129594 49234 5.0375e+08   69  412 5.0375e+08 5.0406e+08  0.06%   329 182554s
 129859 49379 5.0375e+08   64  475 5.0375e+08 5.0406e+08  0.06%   328 182591s
 130127 49485 5.0375e+08   55  491 5.0375e+08 5.0406e+08  0.06%   328 182629s
 130289 49656 5.0375e+08   58  490 5.0375e+08 5.0406e+08  0.06%   328 182678s
 130557 49837 5.0375e+08   43  528 5.0375e+08 5.0406e+08  0.06%   327 182711s
 130825 49935 5.0375e+08   69  458 5.0375e+08 5.0406e+08  0.06%   327 182753s
 131018 50104 5.0375e+08   52  478 5.0375e+08 5.0406e+08  0.06%   326 182790s
 131285 50303 5.0375e+08   55  484 5.0375e+08 5.0406e+08  0.06%   326 182838s
 131555 50486     cutoff   78      5.0375e+08 5.0406e+08  0.06%   325 182873s
 131825 50631 5.0375e+08   54  477 5.0375e+08 5.0406e+08  0.06%   325 182912s
 132081 50841 5.0375e+08   47  534 5.0375e+08 5.0406e+08  0.06%   324 182949s
 132350 50949 5.0375e+08   73  487 5.0375e+08 5.0406e+08  0.06%   324 182985s
 132616 51128 5.0375e+08   52  476 5.0375e+08 5.0406e+08  0.06%   323 183021s
 132884 51314     cutoff   78      5.0375e+08 5.0406e+08  0.06%   323 183071s
 133153 51422 5.0375e+08   63  499 5.0375e+08 5.0406e+08  0.06%   322 183108s
 133412 51587 5.0376e+08   39  520 5.0375e+08 5.0406e+08  0.06%   322 183143s
 133646 51614 5.0375e+08   49  489 5.0375e+08 5.0406e+08  0.06%   321 183209s
 133677 51667 5.0375e+08   48  486 5.0375e+08 5.0406e+08  0.06%   321 183250s
 133766 51738 5.0375e+08   48  492 5.0375e+08 5.0406e+08  0.06%   321 183304s
 133855 51788 5.0375e+08   49  491 5.0375e+08 5.0406e+08  0.06%   321 183344s
 133941 51827 5.0375e+08   49  491 5.0375e+08 5.0406e+08  0.06%   321 183379s
 134048 51882 5.0375e+08   50  490 5.0375e+08 5.0406e+08  0.06%   320 183411s
 134163 51929 5.0375e+08   50  488 5.0375e+08 5.0406e+08  0.06%   320 183444s
 134290 52068 5.0375e+08   50  483 5.0375e+08 5.0406e+08  0.06%   320 183492s
 134544 52211     cutoff   59      5.0375e+08 5.0406e+08  0.06%   319 183525s
 134810 52339 5.0375e+08   49  488 5.0375e+08 5.0406e+08  0.06%   319 183565s
 135049 52516 5.0375e+08   46  531 5.0375e+08 5.0406e+08  0.06%   319 183606s
H135319 52516                    5.037502e+08 5.0406e+08  0.06%   318 183614s
 135319 52692     cutoff   30      5.0375e+08 5.0406e+08  0.06%   318 183645s
 135749 52777 5.0375e+08   34  195 5.0375e+08 5.0406e+08  0.06%   317 183750s
 136095 52705 5.0375e+08   37  155 5.0375e+08 5.0406e+08  0.06%   317 183780s
 136519 52687 5.0375e+08   24  227 5.0375e+08 5.0406e+08  0.06%   316 183813s
 136917 52704     cutoff   37      5.0375e+08 5.0406e+08  0.06%   315 183845s
 137306 52765     cutoff   34      5.0375e+08 5.0406e+08  0.06%   314 183928s
 137684 52650     cutoff   35      5.0375e+08 5.0406e+08  0.06%   314 183958s
 137911 52762     cutoff   36      5.0375e+08 5.0406e+08  0.06%   313 183991s
 138322 52684     cutoff   38      5.0375e+08 5.0405e+08  0.06%   313 184325s
 138489 52796 5.0375e+08   32  166 5.0375e+08 5.0405e+08  0.06%   312 184358s
 138907 52998 5.0375e+08   33  200 5.0375e+08 5.0405e+08  0.06%   312 184423s
 139336 53200 5.0375e+08   44  161 5.0375e+08 5.0405e+08  0.06%   311 184498s
 139759 53294     cutoff   27      5.0375e+08 5.0405e+08  0.06%   310 184757s
 139981 53441 5.0375e+08   32  181 5.0375e+08 5.0405e+08  0.06%   310 184904s
 140323 53640     cutoff   30      5.0375e+08 5.0405e+08  0.06%   309 184936s
 140733 53751     cutoff   44      5.0375e+08 5.0405e+08  0.06%   309 185045s
 141113 53925     cutoff   30      5.0375e+08 5.0405e+08  0.06%   308 185079s
 141528 53945 5.0375e+08   38  193 5.0375e+08 5.0405e+08  0.06%   307 185271s
 141572 54068     cutoff   43      5.0375e+08 5.0405e+08  0.06%   307 185374s
 141902 54216     cutoff   33      5.0375e+08 5.0405e+08  0.06%   307 185406s
 142329 54391 5.0375e+08   42  174 5.0375e+08 5.0405e+08  0.06%   306 185438s
 142758 54551 5.0375e+08   36  168 5.0375e+08 5.0405e+08  0.06%   305 185633s
 143049 54752 5.0375e+08   33  210 5.0375e+08 5.0405e+08  0.06%   305 185759s
 143393 54893 5.0375e+08   34  208 5.0375e+08 5.0405e+08  0.06%   304 185804s
 143813 55153     cutoff   34      5.0375e+08 5.0405e+08  0.06%   304 185837s
 144242 55308     cutoff   48      5.0375e+08 5.0405e+08  0.06%   303 185934s
 144609 55473 5.0375e+08   26  211 5.0375e+08 5.0405e+08  0.06%   302 186087s
 144909 55695 5.0375e+08   33  185 5.0375e+08 5.0405e+08  0.06%   302 186121s
 145336 55859     cutoff   36      5.0375e+08 5.0405e+08  0.06%   301 186186s
 145758 56014 5.0375e+08   32  207 5.0375e+08 5.0405e+08  0.06%   301 186338s
 146045 56175 5.0375e+08   28  224 5.0375e+08 5.0405e+08  0.06%   300 186451s
 146416 56295 5.0375e+08   27  199 5.0375e+08 5.0405e+08  0.06%   300 186522s
 146836 56495 5.0375e+08   29  183 5.0375e+08 5.0405e+08  0.06%   299 186588s
 147257 56608 5.0375e+08   43  155 5.0375e+08 5.0405e+08  0.06%   298 186742s
 147579 56819 5.0375e+08   28  208 5.0375e+08 5.0405e+08  0.06%   298 186797s
 147989 56999 5.0375e+08   29  174 5.0375e+08 5.0405e+08  0.06%   297 186834s
 148417 57226 5.0375e+08   35  223 5.0375e+08 5.0405e+08  0.06%   296 186866s
 148847 57433 5.0375e+08   33  189 5.0375e+08 5.0405e+08  0.06%   296 187035s
 149190 57566     cutoff   41      5.0375e+08 5.0405e+08  0.06%   295 187111s
 149568 57756 5.0375e+08   27  231 5.0375e+08 5.0405e+08  0.06%   295 187280s
 149891 57907 5.0375e+08   38  187 5.0375e+08 5.0405e+08  0.06%   294 187314s
 150318 58071 5.0375e+08   33  158 5.0375e+08 5.0405e+08  0.06%   294 187427s
H150700 58071                    5.037503e+08 5.0405e+08  0.06%   293 187432s
 150700 58076 5.0386e+08   18 2686 5.0375e+08 5.0405e+08  0.06%   293 187568s
 150749 58088     cutoff   20      5.0375e+08 5.0405e+08  0.06%   293 187671s
 150799 58088     cutoff   23      5.0375e+08 5.0405e+08  0.06%   294 187761s
 150862 58085     cutoff   23      5.0375e+08 5.0405e+08  0.06%   294 187833s
 150923 58088 5.0382e+08   18 2666 5.0375e+08 5.0405e+08  0.06%   294 187907s
 150985 58082     cutoff   18      5.0375e+08 5.0405e+08  0.06%   294 188014s
 151043 58090 5.0390e+08   14 2977 5.0375e+08 5.0405e+08  0.06%   294 188090s
 151101 58100 5.0382e+08   18 2680 5.0375e+08 5.0405e+08  0.06%   294 188164s
 151160 58087     cutoff   21      5.0375e+08 5.0405e+08  0.06%   294 188233s
 151213 58094     cutoff   20      5.0375e+08 5.0405e+08  0.06%   294 188303s
 151271 58099 5.0378e+08   18 2666 5.0375e+08 5.0405e+08  0.06%   294 188371s
 151334 58094 5.0377e+08   17 2822 5.0375e+08 5.0405e+08  0.06%   294 188505s
 151375 58107     cutoff   18      5.0375e+08 5.0405e+08  0.06%   294 188576s
 151422 58112 5.0380e+08   18 2719 5.0375e+08 5.0405e+08  0.06%   295 188654s
 151483 58106 5.0381e+08   17 2729 5.0375e+08 5.0405e+08  0.06%   295 188718s
 151542 58113     cutoff   19      5.0375e+08 5.0405e+08  0.06%   295 188787s
 151599 58107     cutoff   18      5.0375e+08 5.0405e+08  0.06%   295 188863s
 151661 58103 5.0385e+08   15 2684 5.0375e+08 5.0405e+08  0.06%   295 188933s
 151713 58112     cutoff   18      5.0375e+08 5.0405e+08  0.06%   295 189003s
 151776 58106 5.0377e+08   17 2629 5.0375e+08 5.0405e+08  0.06%   295 189072s
 151831 58101 5.0378e+08   17 2673 5.0375e+08 5.0405e+08  0.06%   295 189190s
 151888 58113     cutoff   17      5.0375e+08 5.0405e+08  0.06%   295 189272s
 151928 58117 5.0386e+08   17 2513 5.0375e+08 5.0405e+08  0.06%   295 189347s
 151980 58121 infeasible   21      5.0375e+08 5.0405e+08  0.06%   295 189419s
 152042 58124 5.0382e+08   18 2544 5.0375e+08 5.0405e+08  0.06%   296 189490s
 152099 58122     cutoff   19      5.0375e+08 5.0405e+08  0.06%   296 189586s
 152145 58116     cutoff   21      5.0375e+08 5.0405e+08  0.06%   296 189663s
 152205 58123     cutoff   19      5.0375e+08 5.0405e+08  0.06%   296 189801s
 152252 58132 5.0384e+08   17 2538 5.0375e+08 5.0405e+08  0.06%   296 189874s
 152311 58127     cutoff   19      5.0375e+08 5.0405e+08  0.06%   296 189947s
 152370 58127     cutoff   21      5.0375e+08 5.0405e+08  0.06%   296 190023s
 152426 58126     cutoff   19      5.0375e+08 5.0405e+08  0.06%   296 190094s
 152489 58128 5.0395e+08   13 2801 5.0375e+08 5.0405e+08  0.06%   296 190172s
 152545 58132 5.0386e+08   17 2503 5.0375e+08 5.0405e+08  0.06%   297 190243s
 152599 58123     cutoff   21      5.0375e+08 5.0405e+08  0.06%   297 190327s
 152658 58126     cutoff   20      5.0375e+08 5.0405e+08  0.06%   297 190402s
 152715 58137     cutoff   21      5.0375e+08 5.0405e+08  0.06%   297 190474s
 152772 58140 5.0383e+08   17 2491 5.0375e+08 5.0405e+08  0.06%   297 190547s
 152831 58128     cutoff   19      5.0375e+08 5.0405e+08  0.06%   297 190633s
 152885 58147 5.0389e+08   16 2548 5.0375e+08 5.0405e+08  0.06%   297 190710s
 152932 58137 5.0382e+08   18 2502 5.0375e+08 5.0405e+08  0.06%   297 190838s
 152983 58141 5.0380e+08   18 2556 5.0375e+08 5.0405e+08  0.06%   297 190918s
 153033 58144     cutoff   17      5.0375e+08 5.0405e+08  0.06%   298 191066s
 153076 58157 5.0378e+08   19 2481 5.0375e+08 5.0405e+08  0.06%   298 191198s
 153115 58163     cutoff   20      5.0375e+08 5.0405e+08  0.06%   298 191324s
 153157 58165 5.0380e+08   17 2623 5.0375e+08 5.0405e+08  0.06%   298 191405s
 153211 58168 5.0377e+08   17 2611 5.0375e+08 5.0405e+08  0.06%   298 191507s
 153260 58172 5.0378e+08   17 2649 5.0375e+08 5.0405e+08  0.06%   298 191582s
 153312 58186     cutoff   17      5.0375e+08 5.0405e+08  0.06%   298 191689s
 153360 58201 5.0397e+08   14 2780 5.0375e+08 5.0405e+08  0.06%   298 191764s
 153421 58196     cutoff   20      5.0375e+08 5.0405e+08  0.06%   298 191847s
 153482 58201     cutoff   22      5.0375e+08 5.0405e+08  0.06%   298 191920s
 153535 58199 5.0384e+08   17 2628 5.0375e+08 5.0405e+08  0.06%   299 192105s
 153579 58195     cutoff   19      5.0375e+08 5.0405e+08  0.06%   299 192179s
 153623 58194     cutoff   20      5.0375e+08 5.0405e+08  0.06%   299 192278s
 153672 58185 5.0386e+08   17 2670 5.0375e+08 5.0405e+08  0.06%   299 192359s
 153719 58185     cutoff   20      5.0375e+08 5.0405e+08  0.06%   299 192444s
 153761 58191     cutoff   19      5.0375e+08 5.0405e+08  0.06%   299 192529s
 153817 58204 5.0387e+08   20 2471 5.0375e+08 5.0405e+08  0.06%   299 192605s
 153878 58196     cutoff   22      5.0375e+08 5.0405e+08  0.06%   299 192682s
 153936 58198     cutoff   21      5.0375e+08 5.0405e+08  0.06%   300 192917s
 153972 58199     cutoff   22      5.0375e+08 5.0405e+08  0.06%   300 192999s
 154013 58200 5.0377e+08   20 2662 5.0375e+08 5.0405e+08  0.06%   300 193083s
 154066 58207 5.0386e+08   18 2491 5.0375e+08 5.0405e+08  0.06%   300 193163s
 154123 58197     cutoff   22      5.0375e+08 5.0405e+08  0.06%   300 193238s
 154183 58206 5.0381e+08   19 2517 5.0375e+08 5.0405e+08  0.06%   300 193325s
 154248 58215     cutoff   18      5.0375e+08 5.0405e+08  0.06%   300 193400s
 154309 58219 5.0377e+08   21 2597 5.0375e+08 5.0405e+08  0.06%   300 193478s
 154363 58223 5.0375e+08   23 2471 5.0375e+08 5.0405e+08  0.06%   301 193553s
 154419 58229 5.0382e+08   20 2539 5.0375e+08 5.0405e+08  0.06%   301 193637s
 154477 58238 5.0375e+08   22 2538 5.0375e+08 5.0405e+08  0.06%   301 193715s
 154528 58237 5.0388e+08   17 2527 5.0375e+08 5.0405e+08  0.06%   301 193793s
 154581 58241     cutoff   22      5.0375e+08 5.0405e+08  0.06%   301 193868s
 154632 58238     cutoff   18      5.0375e+08 5.0405e+08  0.06%   301 194037s
 154679 58238     cutoff   20      5.0375e+08 5.0405e+08  0.06%   301 194123s
 154719 58243 5.0395e+08   16 2560 5.0375e+08 5.0405e+08  0.06%   301 194204s
 154764 58244 5.0378e+08   22 2593 5.0375e+08 5.0405e+08  0.06%   302 194318s
 154815 58243 5.0382e+08   22 2507 5.0375e+08 5.0405e+08  0.06%   302 194396s
 154868 58243     cutoff   26      5.0375e+08 5.0405e+08  0.06%   302 194493s
 154926 58243     cutoff   22      5.0375e+08 5.0405e+08  0.06%   302 194608s
 154978 58261 5.0376e+08   22 2622 5.0375e+08 5.0405e+08  0.06%   302 194687s
 155035 58260 5.0377e+08   23 2517 5.0375e+08 5.0405e+08  0.06%   302 194835s
 155080 58264     cutoff   21      5.0375e+08 5.0405e+08  0.06%   302 194912s
 155126 58263 5.0385e+08   20 2498 5.0375e+08 5.0405e+08  0.06%   302 195036s
 155175 58268     cutoff   22      5.0375e+08 5.0405e+08  0.06%   302 195115s
 155230 58274     cutoff   24      5.0375e+08 5.0405e+08  0.06%   303 195234s
 155286 58277 5.0379e+08   21 2531 5.0375e+08 5.0405e+08  0.06%   303 195335s
 155345 58283     cutoff   21      5.0375e+08 5.0405e+08  0.06%   303 195430s
 155395 58301 5.0388e+08   13 3121 5.0375e+08 5.0405e+08  0.06%   303 195531s
 155459 58302 5.0378e+08   20 2521 5.0375e+08 5.0405e+08  0.06%   303 195604s
 155512 58309     cutoff   21      5.0375e+08 5.0405e+08  0.06%   303 195686s
 155564 58314     cutoff   19      5.0375e+08 5.0405e+08  0.06%   303 195765s
 155621 58326 5.0376e+08   19 2552 5.0375e+08 5.0405e+08  0.06%   303 195847s
 155683 58334 5.0379e+08   17 2572 5.0375e+08 5.0405e+08  0.06%   303 195931s
 155737 58347 5.0378e+08   16 2707 5.0375e+08 5.0405e+08  0.06%   304 196009s
 155801 58348 5.0376e+08   17 2714 5.0375e+08 5.0405e+08  0.06%   304 196080s
 155858 58359 5.0384e+08   15 2732 5.0375e+08 5.0405e+08  0.06%   304 196180s
 155919 58367     cutoff   21      5.0375e+08 5.0405e+08  0.06%   304 196260s
 155977 58364 5.0381e+08   17 2551 5.0375e+08 5.0405e+08  0.06%   304 196333s
 156032 58382 5.0382e+08   16 2617 5.0375e+08 5.0405e+08  0.06%   304 196661s
 156082 58388     cutoff   21      5.0375e+08 5.0405e+08  0.06%   304 196751s
 156128 58397     cutoff   18      5.0375e+08 5.0405e+08  0.06%   304 196881s
 156167 58404 5.0378e+08   16 2722 5.0375e+08 5.0405e+08  0.06%   304 196953s
 156230 58414     cutoff   18      5.0375e+08 5.0405e+08  0.06%   304 197079s
 156294 58415     cutoff   18      5.0375e+08 5.0405e+08  0.06%   304 197177s
 156341 58431 5.0397e+08   14 2737 5.0375e+08 5.0405e+08  0.06%   305 197257s
 156397 58435 5.0382e+08   21 2400 5.0375e+08 5.0405e+08  0.06%   305 197337s
 156458 58440 5.0379e+08   21 2491 5.0375e+08 5.0405e+08  0.06%   305 197427s
 156511 58448     cutoff   21      5.0375e+08 5.0405e+08  0.06%   305 197503s
 156567 58459     cutoff   22      5.0375e+08 5.0405e+08  0.06%   305 197579s
 156630 58483     cutoff   18      5.0375e+08 5.0405e+08  0.06%   305 197730s
 156688 58491 5.0379e+08   21 2381 5.0375e+08 5.0405e+08  0.06%   305 197812s
 156746 58506     cutoff   22      5.0375e+08 5.0405e+08  0.06%   305 197885s
 156801 58506     cutoff   22      5.0375e+08 5.0405e+08  0.06%   305 197964s
 156855 58523 5.0391e+08   16 2526 5.0375e+08 5.0405e+08  0.06%   306 198059s
 156904 58532     cutoff   23      5.0375e+08 5.0405e+08  0.06%   306 198127s
 156969 58539     cutoff   21      5.0375e+08 5.0405e+08  0.06%   306 198195s
 157034 58547     cutoff   21      5.0375e+08 5.0405e+08  0.06%   306 198545s
 157076 58552 5.0384e+08   18 2469 5.0375e+08 5.0405e+08  0.06%   306 198633s
 157117 58557     cutoff   20      5.0375e+08 5.0405e+08  0.06%   306 198787s
 157176 58557 5.0387e+08   15 2745 5.0375e+08 5.0405e+08  0.06%   306 198871s
 157230 58559 5.0376e+08   21 2538 5.0375e+08 5.0405e+08  0.06%   306 199026s
 157294 58551     cutoff   18      5.0375e+08 5.0405e+08  0.06%   306 199116s
 157337 58535     cutoff   19      5.0375e+08 5.0405e+08  0.06%   306 199203s
 157379 58522 5.0381e+08   18 2588 5.0375e+08 5.0405e+08  0.06%   306 199280s
 157437 58528 5.0382e+08   17 2599 5.0375e+08 5.0405e+08  0.06%   307 199348s
 157502 58528 5.0390e+08   14 2989 5.0375e+08 5.0405e+08  0.06%   307 199412s
 157570 58514     cutoff   18      5.0375e+08 5.0405e+08  0.06%   307 199483s
 157629 58515 5.0378e+08   16 2898 5.0375e+08 5.0405e+08  0.06%   307 199564s
 157693 58512 5.0386e+08   16 2736 5.0375e+08 5.0405e+08  0.06%   307 199643s
 157752 58519     cutoff   20      5.0375e+08 5.0405e+08  0.06%   307 199719s
 157812 58507     cutoff   21      5.0375e+08 5.0405e+08  0.06%   307 199802s
 157870 58512     cutoff   21      5.0375e+08 5.0405e+08  0.06%   307 199873s
 157927 58517 5.0384e+08   17 2761 5.0375e+08 5.0405e+08  0.06%   307 199952s
 157976 58513     cutoff   21      5.0375e+08 5.0405e+08  0.06%   307 200029s
 158025 58518 5.0377e+08   18 2746 5.0375e+08 5.0405e+08  0.06%   308 200120s
 158074 58524 5.0393e+08   19 2617 5.0375e+08 5.0405e+08  0.06%   308 200211s
 158122 58530 5.0392e+08   20 2607 5.0375e+08 5.0405e+08  0.06%   308 200309s
 158164 58552 5.0385e+08   21 2695 5.0375e+08 5.0405e+08  0.06%   308 200388s
 158230 58558 5.0376e+08   24 2674 5.0375e+08 5.0405e+08  0.06%   308 200741s
 158294 58551 5.0381e+08   21 2744 5.0375e+08 5.0405e+08  0.06%   308 200833s
 158339 58543 5.0375e+08   23 2720 5.0375e+08 5.0405e+08  0.06%   308 200917s
 158386 58545     cutoff   24      5.0375e+08 5.0405e+08  0.06%   308 200996s
 158446 58547 5.0377e+08   25 2656 5.0375e+08 5.0405e+08  0.06%   308 201067s
 158507 58539 5.0376e+08   27 2620 5.0375e+08 5.0405e+08  0.06%   308 201159s
 158568 58566 5.0375e+08   29 2617 5.0375e+08 5.0405e+08  0.06%   308 201242s
 158627 58586 5.0383e+08   20 2760 5.0375e+08 5.0405e+08  0.06%   309 201322s
 158685 58608 5.0375e+08   29 2620 5.0375e+08 5.0405e+08  0.06%   309 201403s
 158737 58612 5.0376e+08   29 2578 5.0375e+08 5.0405e+08  0.06%   309 201479s
 158786 58614 5.0386e+08   17 2778 5.0375e+08 5.0405e+08  0.06%   309 201557s
 158826 58613 5.0375e+08   30 2296 5.0375e+08 5.0405e+08  0.06%   309 201634s
 158869 58623     cutoff   30      5.0375e+08 5.0405e+08  0.06%   309 201708s
 158917 58633     cutoff   33      5.0375e+08 5.0405e+08  0.06%   309 201783s
 158965 58635     cutoff   18      5.0375e+08 5.0405e+08  0.06%   309 201859s
 159007 58647 5.0375e+08   34 2265 5.0375e+08 5.0405e+08  0.06%   309 201928s
 159065 58665     cutoff   36      5.0375e+08 5.0405e+08  0.06%   309 202028s
 159119 58678 5.0401e+08   14 2863 5.0375e+08 5.0405e+08  0.06%   310 202054s

Cutting planes:
  Learned: 8
  Implied bound: 4646
  MIR: 11844
  Flow cover: 4044
  Flow path: 1097
  Network: 1
  RLT: 11
  Relax-and-lift: 368

Explored 159137 nodes (51196961 simplex iterations) in 202084.59 seconds (256315.83 work units)
Thread count was 10 (of 32 available processors)

Solution count 10: 5.0375e+08 5.0375e+08 5.0375e+08 ... 5.03706e+08

Memory limit reached
Best objective 5.037502636963e+08, best bound 5.040511760283e+08, gap 0.0597%
Gurobi reached SoftMemLimit but returned a feasible incumbent; loading and exporting the incumbent/bound as a partial solve.

- Status: aborted
  Return code: 0
  Message: Unhandled Gurobi solve status (17)
  Termination condition: resourceInterrupt
  Termination message: Unhandled Gurobi solve status (17)
  Wall time: 202084.88400006294
  Error rc: 0

Solver certificate: {'termination_reason': 'memory_limit', 'pyomo_termination': 'resourceInterrupt', 'pyomo_status': 'aborted', 'has_loaded_incumbent': True, 'objective_SEK': 503750263.69632816, 'valid_bound_SEK': 504051176.0283356, 'gurobi_mip_gap': 0.0005973442669775053, 'requested_mip_gap': 0.0002}
Solver stopped at a configured/resource limit with a feasible incumbent. The incumbent will be exported, but the requested MIP gap may not have been reached.

===============  BEST FEASIBLE ANNUAL PROFIT  ===============
Total profit : 503,750,264 SEK / yr

==================  BREAKDOWN  =================
Revenue (all chargers)             :   708,737,416
Opex - grid purchases              :   141,136,180
Opex - redirection distance        :     3,152,047
Opex - redirection price comp.     :             0
Opex - unmet-demand penalty        :             0
Capex - chargers                   :    20,911,402
Capex - PV & batteries             :    39,787,524
----------------------------------------------------------
Slow   chargers:        206 | energy:   1,224,909.7 | cap ratio: 0.062
Medium chargers:      2,179 | energy:  78,627,093.3 | cap ratio: 0.187
Fast   chargers:        176 | energy:  35,421,208.2 | cap ratio: 0.459
==========================================================

Writing CSV/XLSX outputs...
Combined XLSX written; oversized tables kept as CSV only: origin_type_q
Combined XLSX written to: C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty\results
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
Figures written to: C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty\figures
Run finished with a feasible incumbent after a solver/resource limit; results were exported, but this is not a requested-gap convergence claim. Run directory: C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty

Terminal transcript written to: C:\Users\omkarp\Downloads\Large-scale-LBBD-Optimization\runs\2026-10-01_073813_full_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
