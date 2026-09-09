========== MONOLITHIC TERMINAL LOG ==========
Run transcript : C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
=============================================

Project root  : C:\Users\omkarp\Downloads\Opti
Dataset       : full
Scenario      : with_redirection
Disable PV    : False
Disable BESS  : False
Hard no-slack : False
Sensitivity overrides: none
Run directory : C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty
Loading inputs...
Preprocessing inputs...
Hex cells: 638
Active redirection arc-slots: 472,800
Building type-aware Pyomo model...
Solving with Gurobi...
Read LP format model from file C:\Users\omkarp\AppData\Local\Temp\tmporednf4p.pyomo.lp
Reading time = 41.02 seconds
x1: 11483106 rows, 12772030 columns, 67905490 nonzeros
Set parameter Threads to value 6
Set parameter Presolve to value 2
Set parameter NumericFocus to value 2
Set parameter Heuristics to value 0.1
Set parameter MIPGap to value 0.0001
Set parameter NodefileStart to value 2
Set parameter Cuts to value 3
Set parameter TimeLimit to value 99999
Set parameter MIPFocus to value 1
Set parameter LogFile to value "C:/Users/omkarp/Downloads/Opti/runs/2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty/logs/gurobi_run.log"
Set parameter NodefileDir to value "C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty\nodefiles"
Gurobi Optimizer version 13.0.1 build v13.0.1rc0 (win64 - Windows 11+.0 (26200.2))

CPU model: Intel(R) Xeon(R) w5-2465X, instruction set [SSE2|AVX|AVX2|AVX512]
Thread count: 16 physical cores, 32 logical processors, using up to 6 threads

Non-default parameters:
TimeLimit  99999
Heuristics  0.1
MIPFocus  1
NodefileStart  2
Cuts  3
NumericFocus  2
Presolve  2
Threads  6

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
Presolve removed 509404 rows and 1243570 columns (presolve time = 6s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 10s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 16s)...
Presolve removed 510680 rows and 1243570 columns (presolve time = 20s)...
Presolve removed 691540 rows and 1243570 columns (presolve time = 27s)...
Presolve removed 691540 rows and 1243570 columns (presolve time = 30s)...
Presolve removed 757970 rows and 1310000 columns (presolve time = 37s)...
Presolve removed 909988 rows and 1462018 columns (presolve time = 40s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 45s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 50s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 55s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 60s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 65s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 70s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 75s)...
Presolve removed 917548 rows and 1462018 columns (presolve time = 80s)...
Presolve removed 1581868 rows and 1806682 columns (presolve time = 85s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 90s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 96s)...
Presolve removed 1591588 rows and 1825618 columns (presolve time = 101s)...
Presolve removed 1642384 rows and 1825618 columns (presolve time = 106s)...
Presolve removed 1642384 rows and 1825618 columns (presolve time = 111s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 115s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 120s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 125s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 130s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 135s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 140s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 145s)...
Presolve removed 1680244 rows and 1863478 columns (presolve time = 150s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 159s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 161s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 166s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 172s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 175s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 180s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 185s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 190s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 195s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 200s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 205s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 210s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 215s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 220s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 226s)...
Presolve removed 1684744 rows and 1867114 columns (presolve time = 231s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 236s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 240s)...
Presolve removed 1858003 rows and 2335052 columns (presolve time = 245s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 250s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 255s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 262s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 267s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 270s)...
Presolve removed 1981111 rows and 2458160 columns (presolve time = 275s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 280s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 285s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 290s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 295s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 300s)...
Presolve removed 1981111 rows and 2538152 columns (presolve time = 305s)...
Presolve removed 1981111 rows and 2911712 columns (presolve time = 310s)...
Presolve removed 2327431 rows and 3175664 columns (presolve time = 315s)...
Presolve removed 2327431 rows and 3175664 columns (presolve time = 321s)...
Presolve removed 2465851 rows and 3175664 columns (presolve time = 325s)...
Presolve removed 2470187 rows and 3180000 columns (presolve time = 331s)...
Presolve removed 2475883 rows and 3185696 columns (presolve time = 335s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 340s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 345s)...
Presolve removed 2476483 rows and 3186416 columns (presolve time = 350s)...
Presolve removed 2476483 rows and 3191744 columns (presolve time = 355s)...
Presolve removed 2476483 rows and 3191744 columns (presolve time = 360s)...
Presolve removed 2476483 rows and 3229628 columns (presolve time = 365s)...
Presolve removed 2629675 rows and 3334796 columns (presolve time = 372s)...
Presolve removed 2665651 rows and 3336128 columns (presolve time = 375s)...
Presolve removed 2665651 rows and 3336128 columns (presolve time = 380s)...
Presolve removed 2690611 rows and 3361088 columns (presolve time = 385s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 390s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 395s)...
Presolve removed 2690827 rows and 3361088 columns (presolve time = 400s)...
Presolve removed 2690827 rows and 3361196 columns (presolve time = 405s)...
Presolve removed 2690827 rows and 3361196 columns (presolve time = 410s)...
Presolve removed 2690827 rows and 3389107 columns (presolve time = 415s)...
Presolve removed 2734144 rows and 3417017 columns (presolve time = 421s)...
Presolve removed 2740732 rows and 3417197 columns (presolve time = 425s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 430s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 435s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 440s)...
Presolve removed 2742388 rows and 3418853 columns (presolve time = 445s)...
Presolve removed 2742388 rows and 3419033 columns (presolve time = 450s)...
Presolve removed 2742388 rows and 3419033 columns (presolve time = 455s)...
Presolve removed 2742388 rows and 3430217 columns (presolve time = 460s)...
Presolve removed 2756948 rows and 3440957 columns (presolve time = 465s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 470s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 475s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 480s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 485s)...
Presolve removed 2758712 rows and 3442769 columns (presolve time = 490s)...
Presolve removed 2758712 rows and 3445253 columns (presolve time = 495s)...
Presolve removed 2762614 rows and 3447461 columns (presolve time = 500s)...
Presolve removed 2762614 rows and 3448097 columns (presolve time = 505s)...
Presolve removed 2762614 rows and 3448097 columns (presolve time = 510s)...
Presolve removed 2976989 rows and 3591211 columns (presolve time = 515s)...
Presolve removed 3260229 rows and 3789129 columns (presolve time = 520s)...
Presolve removed 3380905 rows and 3880388 columns (presolve time = 525s)...
Presolve removed 3543621 rows and 4011179 columns (presolve time = 530s)...
Presolve removed 3660477 rows and 4107317 columns (presolve time = 535s)...
Presolve removed 3769183 rows and 4206371 columns (presolve time = 540s)...
Presolve removed 3873534 rows and 4295674 columns (presolve time = 547s)...
Presolve removed 3904124 rows and 4323116 columns (presolve time = 552s)...
Presolve removed 3982911 rows and 4395348 columns (presolve time = 556s)...
Presolve removed 4066402 rows and 4474480 columns (presolve time = 561s)...
Presolve removed 4110636 rows and 4514685 columns (presolve time = 567s)...
Presolve removed 4166166 rows and 4560514 columns (presolve time = 572s)...
Presolve removed 4293704 rows and 4667466 columns (presolve time = 583s)...
Presolve removed 4351021 rows and 4723190 columns (presolve time = 585s)...
Presolve removed 4407461 rows and 4781058 columns (presolve time = 590s)...
Presolve removed 4478063 rows and 4850142 columns (presolve time = 596s)...
Presolve removed 4558145 rows and 4930568 columns (presolve time = 614s)...
Presolve removed 4650084 rows and 5020152 columns (presolve time = 634s)...
Presolve removed 4818448 rows and 5177287 columns (presolve time = 655s)...
Presolve removed 5089501 rows and 5458139 columns (presolve time = 745s)...
Presolve removed 5533049 rows and 5914648 columns (presolve time = 954s)...
Presolve removed 5533049 rows and 5914648 columns (presolve time = 2146s)...
Presolve removed 5533049 rows and 5914840 columns (presolve time = 2151s)...
Presolve removed 5532473 rows and 5914840 columns
Presolve time: 2150.54s
Presolved: 5950633 rows, 6857190 columns, 36713717 nonzeros
Found heuristic solution: objective -1.56736e+12
Variable types: 6106332 continuous, 750858 integer (558328 binary)
Root relaxation presolve removed 1285096 rows and 2320000 columns (presolve time = 5s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 10s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 15s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 20s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 25s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 30s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 35s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 40s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 45s)...
Root relaxation presolve removed 1582372 rows and 2596396 columns (presolve time = 50s)...
Root relaxation presolve removed 1691644 rows and 2596396 columns (presolve time = 55s)...
Root relaxation presolve removed 1854294 rows and 2604621 columns (presolve time = 60s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 65s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 70s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 75s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 80s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 85s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 90s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 95s)...
Root relaxation presolve removed 1854294 rows and 2610021 columns (presolve time = 100s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 105s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 110s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 115s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 120s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 125s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns (presolve time = 130s)...
Root relaxation presolve removed 1860929 rows and 2625837 columns
Root relaxation presolved: 4089704 rows, 4231353 columns, 22696880 nonzeros

Deterministic concurrent LP optimizer: primal simplex, dual simplex, and barrier
Showing barrier log only...

Root barrier log...

Elapsed ordering time = 5s
Elapsed ordering time = 13s
Elapsed ordering time = 15s
Elapsed ordering time = 20s
Ordering time: 34.11s
Elapsed ordering time = 54s
Elapsed ordering time = 56s
Elapsed ordering time = 64s
Elapsed ordering time = 65s
Elapsed ordering time = 70s
Elapsed ordering time = 75s
Elapsed ordering time = 80s
Elapsed ordering time = 85s
Elapsed ordering time = 90s
Elapsed ordering time = 140s
Elapsed ordering time = 142s
Elapsed ordering time = 147s
Elapsed ordering time = 164s
Elapsed ordering time = 166s
Elapsed ordering time = 175s
Elapsed ordering time = 176s
Elapsed ordering time = 188s
Elapsed ordering time = 193s
Elapsed ordering time = 196s
Elapsed ordering time = 200s
Elapsed ordering time = 205s
Elapsed ordering time = 210s
Elapsed ordering time = 215s
Elapsed ordering time = 221s
Elapsed ordering time = 226s
Elapsed ordering time = 230s
Elapsed ordering time = 235s
Elapsed ordering time = 243s
Elapsed ordering time = 245s
Elapsed ordering time = 250s
Elapsed ordering time = 255s
Elapsed ordering time = 260s
Elapsed ordering time = 265s
Elapsed ordering time = 270s
Elapsed ordering time = 275s
Elapsed ordering time = 282s
Elapsed ordering time = 285s
Elapsed ordering time = 290s
Elapsed ordering time = 295s
Elapsed ordering time = 300s
Elapsed ordering time = 305s
Elapsed ordering time = 312s
Elapsed ordering time = 315s
Elapsed ordering time = 320s
Elapsed ordering time = 329s
Elapsed ordering time = 330s
Elapsed ordering time = 335s
Elapsed ordering time = 340s
Elapsed ordering time = 345s
Elapsed ordering time = 350s
Elapsed ordering time = 356s
Elapsed ordering time = 360s
Elapsed ordering time = 365s
Elapsed ordering time = 427s
Elapsed ordering time = 434s
Elapsed ordering time = 449s
Elapsed ordering time = 451s
Elapsed ordering time = 460s
Elapsed ordering time = 461s
Elapsed ordering time = 470s
Elapsed ordering time = 476s
Elapsed ordering time = 480s
Elapsed ordering time = 485s
Elapsed ordering time = 493s
Elapsed ordering time = 497s
Elapsed ordering time = 503s
Elapsed ordering time = 505s
Elapsed ordering time = 511s
Elapsed ordering time = 519s
Elapsed ordering time = 522s
Elapsed ordering time = 526s
Elapsed ordering time = 530s
Elapsed ordering time = 536s
Elapsed ordering time = 543s
Elapsed ordering time = 546s
Elapsed ordering time = 551s
Elapsed ordering time = 555s
Elapsed ordering time = 560s
Elapsed ordering time = 566s
Elapsed ordering time = 570s
Elapsed ordering time = 576s
Elapsed ordering time = 584s
Elapsed ordering time = 585s
Elapsed ordering time = 590s
Elapsed ordering time = 597s
Elapsed ordering time = 600s
Elapsed ordering time = 607s
Elapsed ordering time = 613s
Elapsed ordering time = 617s
Elapsed ordering time = 625s
Elapsed ordering time = 625s
Elapsed ordering time = 630s
Elapsed ordering time = 635s
Elapsed ordering time = 640s
Elapsed ordering time = 645s
Elapsed ordering time = 652s
Elapsed ordering time = 655s
Elapsed ordering time = 660s
Elapsed ordering time = 709s
Elapsed ordering time = 712s
Elapsed ordering time = 716s
Elapsed ordering time = 732s
Elapsed ordering time = 736s
Elapsed ordering time = 742s
Elapsed ordering time = 753s
Elapsed ordering time = 759s
Elapsed ordering time = 761s
Elapsed ordering time = 766s
Elapsed ordering time = 770s
Elapsed ordering time = 776s
Elapsed ordering time = 782s
Elapsed ordering time = 786s
Elapsed ordering time = 792s
Elapsed ordering time = 795s
Elapsed ordering time = 802s
Elapsed ordering time = 805s
Elapsed ordering time = 812s
Elapsed ordering time = 816s
Elapsed ordering time = 821s
Elapsed ordering time = 825s
Elapsed ordering time = 830s
Elapsed ordering time = 835s
Elapsed ordering time = 841s
Elapsed ordering time = 846s
Elapsed ordering time = 851s
Elapsed ordering time = 855s
Elapsed ordering time = 860s
Elapsed ordering time = 865s
Elapsed ordering time = 870s
Elapsed ordering time = 878s
Elapsed ordering time = 880s
Elapsed ordering time = 887s
Elapsed ordering time = 893s
Elapsed ordering time = 900s
Elapsed ordering time = 900s
Elapsed ordering time = 905s
Elapsed ordering time = 910s
Elapsed ordering time = 915s
Elapsed ordering time = 920s
Elapsed ordering time = 926s
Elapsed ordering time = 930s
Elapsed ordering time = 935s
Elapsed ordering time = 1003s
Elapsed ordering time = 1007s
Elapsed ordering time = 1015s
Elapsed ordering time = 1046s
Elapsed ordering time = 1055s
Elapsed ordering time = 1060s
Elapsed ordering time = 1077s
Elapsed ordering time = 1092s
Elapsed ordering time = 1098s
Elapsed ordering time = 1101s
Elapsed ordering time = 1106s
Elapsed ordering time = 1110s
Elapsed ordering time = 1116s
Elapsed ordering time = 1132s
Elapsed ordering time = 1140s
Elapsed ordering time = 1142s
Elapsed ordering time = 1147s
Elapsed ordering time = 1151s
Elapsed ordering time = 1155s
Elapsed ordering time = 1162s
Elapsed ordering time = 1175s
Elapsed ordering time = 1175s
Elapsed ordering time = 1183s
Elapsed ordering time = 1186s
Elapsed ordering time = 1191s
Elapsed ordering time = 1196s
Elapsed ordering time = 1201s
Elapsed ordering time = 1205s
Elapsed ordering time = 1210s
Elapsed ordering time = 1217s
Elapsed ordering time = 1226s
Elapsed ordering time = 1230s
Elapsed ordering time = 1236s
Elapsed ordering time = 1240s
Elapsed ordering time = 1245s
Elapsed ordering time = 1250s
Elapsed ordering time = 1256s
Elapsed ordering time = 1261s
Elapsed ordering time = 1265s
Elapsed ordering time = 1270s
Elapsed ordering time = 1277s
Elapsed ordering time = 1280s
Elapsed ordering time = 1285s
Elapsed ordering time = 1290s
Elapsed ordering time = 1295s
Elapsed ordering time = 1301s
Elapsed ordering time = 1305s
Elapsed ordering time = 1311s
Elapsed ordering time = 1315s
Elapsed ordering time = 1322s
Elapsed ordering time = 1327s
Elapsed ordering time = 1330s
Elapsed ordering time = 1335s
Elapsed ordering time = 1345s
Elapsed ordering time = 1349s
Elapsed ordering time = 1357s
Elapsed ordering time = 1360s
Elapsed ordering time = 1365s
Elapsed ordering time = 1370s
Elapsed ordering time = 1375s
Elapsed ordering time = 1380s
Elapsed ordering time = 1385s
Elapsed ordering time = 1449s
Elapsed ordering time = 1452s
Elapsed ordering time = 1456s
Elapsed ordering time = 1471s
Elapsed ordering time = 1476s
Elapsed ordering time = 1481s
Elapsed ordering time = 1492s
Elapsed ordering time = 1498s
Elapsed ordering time = 1501s
Elapsed ordering time = 1507s
Elapsed ordering time = 1514s
Elapsed ordering time = 1518s
Elapsed ordering time = 1524s
Elapsed ordering time = 1525s
Elapsed ordering time = 1530s
Elapsed ordering time = 1535s
Elapsed ordering time = 1540s
Elapsed ordering time = 1547s
Elapsed ordering time = 1550s
Elapsed ordering time = 1555s
Elapsed ordering time = 1560s
Elapsed ordering time = 1565s
Elapsed ordering time = 1571s
Elapsed ordering time = 1575s
Elapsed ordering time = 1581s
Elapsed ordering time = 1585s
Elapsed ordering time = 1590s
Elapsed ordering time = 1595s
Elapsed ordering time = 1603s
Elapsed ordering time = 1606s
Elapsed ordering time = 1610s
Elapsed ordering time = 1615s
Elapsed ordering time = 1622s
Elapsed ordering time = 1628s
Elapsed ordering time = 1632s
Elapsed ordering time = 1639s
Elapsed ordering time = 1640s
Elapsed ordering time = 1645s
Elapsed ordering time = 1650s
Elapsed ordering time = 1655s
Elapsed ordering time = 1660s
Elapsed ordering time = 1666s
Elapsed ordering time = 1670s
Ordering time: 1704.57s
Elapsed ordering time = 1707s
Elapsed ordering time = 1710s
Elapsed ordering time = 1715s
Elapsed ordering time = 1720s
Elapsed ordering time = 1725s
Elapsed ordering time = 1730s
Elapsed ordering time = 1735s
Elapsed ordering time = 1743s
Elapsed ordering time = 1746s
Elapsed ordering time = 1750s
Elapsed ordering time = 1755s
Elapsed ordering time = 1760s
Elapsed ordering time = 1765s
Elapsed ordering time = 1772s
Elapsed ordering time = 1775s
Elapsed ordering time = 1780s
Elapsed ordering time = 1785s
Elapsed ordering time = 1790s
Elapsed ordering time = 1795s
Elapsed ordering time = 1800s
Elapsed ordering time = 1805s
Elapsed ordering time = 1811s
Elapsed ordering time = 1815s
Elapsed ordering time = 1820s
Elapsed ordering time = 1825s
Elapsed ordering time = 1830s
Elapsed ordering time = 1838s
Elapsed ordering time = 1841s
Elapsed ordering time = 1845s
Elapsed ordering time = 1850s
Elapsed ordering time = 1855s
Elapsed ordering time = 1860s
Ordering time: 1862.75s

Barrier statistics:
 Dense cols : 1173
 AA' NZ     : 4.172e+07
 Factor NZ  : 1.182e+09 (roughly 13.0 GB of memory)
 Factor Ops : 9.632e+12 (roughly 70 seconds per iteration)
 Threads    : 4

                  Objective                Residual
Iter       Primal          Dual         Primal    Dual     Compl     Time
   0  -1.54307273e+14  3.50191318e+14  7.30e+04 2.37e+06  3.86e+09  4406s
   1  -1.07224069e+14  4.08330556e+14  6.01e+04 1.28e+06  2.93e+09  4679s
   2  -7.21874376e+13  4.28493080e+14  4.18e+04 3.97e+05  1.98e+09  4986s
   3  -4.79404614e+13  4.11641487e+14  2.84e+04 1.58e+05  1.35e+09  5305s
   4  -3.39772151e+13  3.64457484e+14  2.07e+04 5.26e+04  9.81e+08  5622s
   5  -2.55884229e+13  3.27292899e+14  1.63e+04 2.39e+04  7.66e+08  5948s
   6  -1.16617709e+13  2.35545612e+14  7.78e+03 3.81e-06  3.64e+08  6288s
   7  -2.03833573e+12  1.36654857e+14  1.66e+03 2.74e-06  8.17e+07  6616s
   8  -3.69790240e+11  6.38108982e+13  3.96e+02 4.71e-06  2.05e+07  6886s
   9  -1.35819023e+11  4.00757075e+13  1.14e+02 2.55e-06  7.36e+06  7110s
  10  -8.33251518e+10  1.63694372e+13  4.04e+01 1.46e-06  2.44e+06  7328s
  11  -5.61996682e+10  5.85501270e+12  1.77e+01 1.06e-06  8.09e+05  7570s
  12  -3.30939896e+10  1.92906307e+12  6.43e+00 3.43e-07  2.32e+05  7860s
  13  -8.88697381e+09  5.44016197e+11  8.94e-01 9.80e-08  5.14e+04  8206s
  14  -1.73293574e+09  1.18772892e+11  1.20e-01 5.55e-08  1.06e+04  8282s
  15  -2.16047925e+08  2.75238146e+10  1.20e-02 2.98e-08  2.41e+03  8364s
  16  -1.30291324e+07  8.48360872e+09  1.98e-03 1.19e-08  7.38e+02  8453s
  17   1.11485687e+08  3.46476942e+09  9.47e-04 5.59e-09  2.91e+02  8609s
  18   1.69830940e+08  2.03749981e+09  7.05e-04 5.59e-09  1.62e+02  8759s
  19   2.27667248e+08  1.63250839e+09  5.08e-04 5.59e-09  1.22e+02  8898s
  20   2.70519889e+08  1.42260798e+09  3.72e-04 5.59e-09  1.00e+02  9006s
  21   2.93106056e+08  1.29532032e+09  3.11e-04 5.59e-09  8.70e+01  9104s
  22   3.19013378e+08  1.15865116e+09  2.46e-04 5.59e-09  7.29e+01  9206s
  23   3.44320002e+08  1.02425236e+09  1.88e-04 5.59e-09  5.90e+01  9314s
  24   3.66387331e+08  8.64904095e+08  1.45e-04 5.59e-09  4.33e+01  9439s
  25   3.85064980e+08  7.79249609e+08  1.12e-04 5.59e-09  3.42e+01  9551s
  26   4.01067707e+08  7.04595286e+08  8.74e-05 5.59e-09  2.64e+01  9668s
  27   4.20481677e+08  6.55461019e+08  6.27e-05 5.59e-09  2.04e+01  9774s
  28   4.33263753e+08  6.16953119e+08  4.92e-05 5.59e-09  1.59e+01  9880s
  29   4.43137649e+08  5.80843235e+08  4.05e-05 5.59e-09  1.20e+01  9986s
  30   4.51085660e+08  5.66286029e+08  3.41e-05 5.59e-09  1.00e+01  10096s
  31   4.62191696e+08  5.53176121e+08  2.59e-05 5.59e-09  7.90e+00  10202s
  32   4.69994651e+08  5.41010243e+08  2.06e-05 5.59e-09  6.17e+00  10313s
  33   4.76882529e+08  5.33809717e+08  1.61e-05 5.59e-09  4.94e+00  10420s
  34   4.81593411e+08  5.26527281e+08  1.32e-05 5.59e-09  3.90e+00  10524s
  35   4.85433968e+08  5.23618026e+08  1.09e-05 5.59e-09  3.32e+00  10628s
  36   4.88911681e+08  5.19151903e+08  8.85e-06 8.52e-09  2.63e+00  10731s
  37   4.92044966e+08  5.16118892e+08  7.05e-06 8.63e-09  2.09e+00  10835s
  38   4.94131092e+08  5.13623568e+08  5.90e-06 8.26e-09  1.69e+00  10939s
  39   4.95967548e+08  5.12439844e+08  4.88e-06 6.92e-09  1.43e+00  11043s
  40   4.97905264e+08  5.10901335e+08  3.81e-06 5.59e-09  1.13e+00  11147s
  41   4.99053016e+08  5.09770266e+08  3.19e-06 2.63e-08  9.31e-01  11252s
  42   5.00053874e+08  5.08785567e+08  2.66e-06 4.35e-08  7.58e-01  11356s
  43   5.00916771e+08  5.08294583e+08  2.20e-06 3.86e-08  6.41e-01  11460s
  44   5.01652355e+08  5.07681503e+08  1.81e-06 3.89e-08  5.24e-01  11569s
  45   5.02243291e+08  5.07333815e+08  1.50e-06 4.39e-08  4.42e-01  11674s
  46   5.02704815e+08  5.06894244e+08  1.27e-06 3.29e-08  3.64e-01  11796s
  47   5.03184827e+08  5.06659878e+08  1.02e-06 3.01e-08  3.02e-01  11916s
  48   5.03501121e+08  5.06428324e+08  8.61e-07 5.46e-08  2.54e-01  12038s
  49   5.03834796e+08  5.06202374e+08  6.90e-07 3.74e-08  2.06e-01  12155s
  50   5.03990314e+08  5.05990919e+08  6.13e-07 5.59e-09  1.74e-01  12276s
  51   5.04172765e+08  5.05869073e+08  5.23e-07 8.07e-09  1.47e-01  12390s
  52   5.04344860e+08  5.05741317e+08  4.37e-07 5.59e-09  1.21e-01  12512s
  53   5.04482199e+08  5.05676229e+08  3.72e-07 5.59e-09  1.04e-01  12630s
  54   5.04580904e+08  5.05584488e+08  3.22e-07 5.59e-09  8.72e-02  12743s
  55   5.04693558e+08  5.05531144e+08  2.70e-07 5.59e-09  7.27e-02  12867s
  56   5.04769538e+08  5.05496437e+08  2.32e-07 5.59e-09  6.31e-02  12969s
  57   5.04851387e+08  5.05457154e+08  1.92e-07 1.17e-08  5.26e-02  13095s
  58   5.04923431e+08  5.05412733e+08  1.57e-07 5.59e-09  4.25e-02  13220s
  59   5.04957207e+08  5.05390326e+08  1.40e-07 5.59e-09  3.76e-02  13325s
  60   5.04997742e+08  5.05363262e+08  1.21e-07 1.18e-08  3.17e-02  13456s
  61   5.05034207e+08  5.05339165e+08  1.04e-07 1.24e-07  2.65e-02  13576s
  62   5.05073089e+08  5.05328052e+08  8.58e-08 1.20e-07  2.21e-02  13693s
  63   5.05096492e+08  5.05310605e+08  7.42e-08 2.66e-08  1.86e-02  13807s
  64   5.05109138e+08  5.05305893e+08  6.79e-08 1.26e-08  1.71e-02  13930s
  65   5.05132763e+08  5.05297092e+08  5.66e-08 1.16e-08  1.43e-02  14041s
  66   5.05156059e+08  5.05287787e+08  4.49e-08 5.59e-09  1.14e-02  14140s
  67   5.05178003e+08  5.05279682e+08  3.43e-08 1.34e-08  8.83e-03  14261s
  68   5.05188596e+08  5.05274800e+08  2.91e-08 2.53e-08  7.49e-03  14377s
  69   5.05197318e+08  5.05270188e+08  2.48e-08 1.65e-08  6.33e-03  14499s
  70   5.05209812e+08  5.05264617e+08  1.86e-08 5.59e-09  4.76e-03  14651s
  71   5.05218065e+08  5.05261719e+08  1.47e-08 6.80e-09  3.79e-03  14809s
  72   5.05223070e+08  5.05259650e+08  3.25e-08 3.42e-08  3.18e-03  14970s
  73   5.05226181e+08  5.05256673e+08  9.10e-08 9.67e-08  2.65e-03  15150s
  74   5.05231837e+08  5.05255077e+08  9.92e-08 6.42e-08  2.02e-03  15325s
  75   5.05234261e+08  5.05253038e+08  1.77e-07 4.47e-08  1.63e-03  15526s
  76   5.05237532e+08  5.05251910e+08  2.46e-07 3.01e-08  1.25e-03  15750s
  77   5.05239570e+08  5.05251291e+08  2.09e-07 3.24e-08  1.02e-03  15990s
  78   5.05240568e+08  5.05250721e+08  1.99e-07 3.61e-08  8.82e-04  16269s
  79   5.05240831e+08  5.05250154e+08  1.93e-07 2.49e-08  8.09e-04  16420s
  80   5.05242575e+08  5.05249661e+08  1.66e-07 2.01e-08  6.15e-04  16678s
  81   5.05243952e+08  5.05249315e+08  1.79e-07 1.66e-08  4.66e-04  16964s
  82   5.05245391e+08  5.05248645e+08  1.69e-07 1.06e-08  2.82e-04  17253s
  83   5.05245803e+08  5.05248122e+08  1.66e-07 4.47e-09  2.01e-04  17679s
  84   5.05246360e+08  5.05248031e+08  1.03e-07 3.73e-09  1.45e-04  17934s

Barrier solved model in 84 iterations and 17934.42 seconds (16421.87 work units)
Optimal objective 5.05246360e+08


Root crossover log...

 1059413 DPushes remaining with DInf 0.0000000e+00             17938s
  511922 DPushes remaining with DInf 0.0000000e+00             17941s
  283993 DPushes remaining with DInf 0.0000000e+00             17946s
  274334 DPushes remaining with DInf 0.0000000e+00             17951s
  273643 DPushes remaining with DInf 0.0000000e+00             17955s
  272739 DPushes remaining with DInf 0.0000000e+00             17961s
  272148 DPushes remaining with DInf 0.0000000e+00             17965s
  271302 DPushes remaining with DInf 0.0000000e+00             17970s
  270542 DPushes remaining with DInf 0.0000000e+00             17975s
  269346 DPushes remaining with DInf 0.0000000e+00             17980s
  268312 DPushes remaining with DInf 0.0000000e+00             17985s
  267288 DPushes remaining with DInf 0.0000000e+00             17990s
  266041 DPushes remaining with DInf 0.0000000e+00             17996s
  264108 DPushes remaining with DInf 0.0000000e+00             18001s
  263561 DPushes remaining with DInf 0.0000000e+00             18005s
  262921 DPushes remaining with DInf 0.0000000e+00             18010s
  262296 DPushes remaining with DInf 0.0000000e+00             18015s
  261537 DPushes remaining with DInf 0.0000000e+00             18021s
  260072 DPushes remaining with DInf 0.0000000e+00             18026s
  259307 DPushes remaining with DInf 0.0000000e+00             18030s
  258474 DPushes remaining with DInf 0.0000000e+00             18035s
  257612 DPushes remaining with DInf 0.0000000e+00             18040s
  256489 DPushes remaining with DInf 0.0000000e+00             18045s
  255064 DPushes remaining with DInf 0.0000000e+00             18050s
  254023 DPushes remaining with DInf 0.0000000e+00             18055s
  252689 DPushes remaining with DInf 0.0000000e+00             18061s
  251494 DPushes remaining with DInf 0.0000000e+00             18065s
  249771 DPushes remaining with DInf 0.0000000e+00             18070s
  247946 DPushes remaining with DInf 0.0000000e+00             18075s
  246485 DPushes remaining with DInf 0.0000000e+00             18081s
  245123 DPushes remaining with DInf 0.0000000e+00             18086s
  244412 DPushes remaining with DInf 0.0000000e+00             18091s
  243605 DPushes remaining with DInf 0.0000000e+00             18096s
  242447 DPushes remaining with DInf 0.0000000e+00             18101s
  241384 DPushes remaining with DInf 0.0000000e+00             18106s
  240706 DPushes remaining with DInf 0.0000000e+00             18111s
  239994 DPushes remaining with DInf 0.0000000e+00             18115s
  238552 DPushes remaining with DInf 0.0000000e+00             18120s
  236524 DPushes remaining with DInf 0.0000000e+00             18125s
  235793 DPushes remaining with DInf 0.0000000e+00             18130s
  234673 DPushes remaining with DInf 0.0000000e+00             18135s
  233797 DPushes remaining with DInf 0.0000000e+00             18141s
  232877 DPushes remaining with DInf 0.0000000e+00             18146s
  232272 DPushes remaining with DInf 0.0000000e+00             18150s
  231528 DPushes remaining with DInf 0.0000000e+00             18156s
  230695 DPushes remaining with DInf 0.0000000e+00             18161s
  229711 DPushes remaining with DInf 0.0000000e+00             18166s
  228037 DPushes remaining with DInf 0.0000000e+00             18170s
  225718 DPushes remaining with DInf 0.0000000e+00             18175s
  224698 DPushes remaining with DInf 0.0000000e+00             18180s
  223565 DPushes remaining with DInf 0.0000000e+00             18186s
  222919 DPushes remaining with DInf 0.0000000e+00             18190s
  221696 DPushes remaining with DInf 0.0000000e+00             18195s
  220395 DPushes remaining with DInf 0.0000000e+00             18200s
  219358 DPushes remaining with DInf 0.0000000e+00             18205s
  218455 DPushes remaining with DInf 0.0000000e+00             18210s
  217460 DPushes remaining with DInf 0.0000000e+00             18216s
  216575 DPushes remaining with DInf 0.0000000e+00             18221s
  215257 DPushes remaining with DInf 0.0000000e+00             18226s
  214358 DPushes remaining with DInf 0.0000000e+00             18230s
  213465 DPushes remaining with DInf 0.0000000e+00             18235s
  212397 DPushes remaining with DInf 0.0000000e+00             18240s
  211447 DPushes remaining with DInf 0.0000000e+00             18246s
  210550 DPushes remaining with DInf 0.0000000e+00             18251s
  209742 DPushes remaining with DInf 0.0000000e+00             18256s
  209067 DPushes remaining with DInf 0.0000000e+00             18260s
  208175 DPushes remaining with DInf 0.0000000e+00             18265s
  207208 DPushes remaining with DInf 0.0000000e+00             18270s
  206202 DPushes remaining with DInf 0.0000000e+00             18275s
  205157 DPushes remaining with DInf 0.0000000e+00             18280s
  204080 DPushes remaining with DInf 0.0000000e+00             18285s
  203037 DPushes remaining with DInf 0.0000000e+00             18291s
  201861 DPushes remaining with DInf 0.0000000e+00             18296s
  200931 DPushes remaining with DInf 0.0000000e+00             18300s
  199867 DPushes remaining with DInf 0.0000000e+00             18305s
  198933 DPushes remaining with DInf 0.0000000e+00             18310s
  197696 DPushes remaining with DInf 0.0000000e+00             18315s
  196255 DPushes remaining with DInf 0.0000000e+00             18321s
  194335 DPushes remaining with DInf 0.0000000e+00             18326s
  192654 DPushes remaining with DInf 0.0000000e+00             18331s
  191408 DPushes remaining with DInf 0.0000000e+00             18335s
  190421 DPushes remaining with DInf 0.0000000e+00             18340s
  189639 DPushes remaining with DInf 0.0000000e+00             18346s
  188842 DPushes remaining with DInf 0.0000000e+00             18351s
  188031 DPushes remaining with DInf 0.0000000e+00             18355s
  186777 DPushes remaining with DInf 0.0000000e+00             18361s
  185669 DPushes remaining with DInf 0.0000000e+00             18365s
  184368 DPushes remaining with DInf 0.0000000e+00             18371s
  183415 DPushes remaining with DInf 0.0000000e+00             18376s
  182552 DPushes remaining with DInf 0.0000000e+00             18380s
  181280 DPushes remaining with DInf 0.0000000e+00             18386s
  179885 DPushes remaining with DInf 0.0000000e+00             18391s
  178975 DPushes remaining with DInf 0.0000000e+00             18395s
  177944 DPushes remaining with DInf 0.0000000e+00             18400s
  176842 DPushes remaining with DInf 0.0000000e+00             18405s
  175897 DPushes remaining with DInf 0.0000000e+00             18411s
  175024 DPushes remaining with DInf 0.0000000e+00             18416s
  174296 DPushes remaining with DInf 0.0000000e+00             18420s
  173371 DPushes remaining with DInf 0.0000000e+00             18425s
  172392 DPushes remaining with DInf 0.0000000e+00             18430s
  171471 DPushes remaining with DInf 0.0000000e+00             18435s
  170546 DPushes remaining with DInf 0.0000000e+00             18440s
  169458 DPushes remaining with DInf 0.0000000e+00             18446s
  168331 DPushes remaining with DInf 0.0000000e+00             18450s
  166890 DPushes remaining with DInf 0.0000000e+00             18455s
  165613 DPushes remaining with DInf 0.0000000e+00             18460s
  164510 DPushes remaining with DInf 0.0000000e+00             18466s
  163440 DPushes remaining with DInf 0.0000000e+00             18471s
  162657 DPushes remaining with DInf 0.0000000e+00             18475s
  161752 DPushes remaining with DInf 0.0000000e+00             18480s
  160748 DPushes remaining with DInf 0.0000000e+00             18485s
  159693 DPushes remaining with DInf 0.0000000e+00             18491s
  158756 DPushes remaining with DInf 0.0000000e+00             18495s
  157638 DPushes remaining with DInf 0.0000000e+00             18500s
  156326 DPushes remaining with DInf 0.0000000e+00             18505s
  154755 DPushes remaining with DInf 0.0000000e+00             18511s
  153494 DPushes remaining with DInf 0.0000000e+00             18515s
  151963 DPushes remaining with DInf 0.0000000e+00             18520s
  150588 DPushes remaining with DInf 0.0000000e+00             18526s
  149636 DPushes remaining with DInf 0.0000000e+00             18530s
  148333 DPushes remaining with DInf 0.0000000e+00             18536s
  147191 DPushes remaining with DInf 0.0000000e+00             18540s
  146174 DPushes remaining with DInf 0.0000000e+00             18545s
  145282 DPushes remaining with DInf 0.0000000e+00             18551s
  144204 DPushes remaining with DInf 0.0000000e+00             18556s
  143020 DPushes remaining with DInf 0.0000000e+00             18561s
  141793 DPushes remaining with DInf 0.0000000e+00             18566s
  140490 DPushes remaining with DInf 0.0000000e+00             18571s
  139212 DPushes remaining with DInf 0.0000000e+00             18576s
  138029 DPushes remaining with DInf 0.0000000e+00             18581s
  136892 DPushes remaining with DInf 0.0000000e+00             18585s
  135538 DPushes remaining with DInf 0.0000000e+00             18590s
  134191 DPushes remaining with DInf 0.0000000e+00             18596s
  132958 DPushes remaining with DInf 0.0000000e+00             18601s
  131906 DPushes remaining with DInf 0.0000000e+00             18605s
  130412 DPushes remaining with DInf 0.0000000e+00             18611s
  128890 DPushes remaining with DInf 0.0000000e+00             18616s
  127712 DPushes remaining with DInf 0.0000000e+00             18620s
  126357 DPushes remaining with DInf 0.0000000e+00             18626s
  125367 DPushes remaining with DInf 0.0000000e+00             18630s
  124219 DPushes remaining with DInf 0.0000000e+00             18636s
  123470 DPushes remaining with DInf 0.0000000e+00             18640s
  122359 DPushes remaining with DInf 0.0000000e+00             18646s
  121501 DPushes remaining with DInf 0.0000000e+00             18650s
  120303 DPushes remaining with DInf 0.0000000e+00             18655s
  118945 DPushes remaining with DInf 0.0000000e+00             18660s
  117667 DPushes remaining with DInf 0.0000000e+00             18665s
  116456 DPushes remaining with DInf 0.0000000e+00             18670s
  115343 DPushes remaining with DInf 0.0000000e+00             18676s
  114249 DPushes remaining with DInf 0.0000000e+00             18681s
  113168 DPushes remaining with DInf 0.0000000e+00             18686s
  112057 DPushes remaining with DInf 0.0000000e+00             18691s
  111057 DPushes remaining with DInf 0.0000000e+00             18695s
  109922 DPushes remaining with DInf 0.0000000e+00             18701s
  108881 DPushes remaining with DInf 0.0000000e+00             18705s
  107715 DPushes remaining with DInf 0.0000000e+00             18710s
  106567 DPushes remaining with DInf 0.0000000e+00             18715s
  105350 DPushes remaining with DInf 0.0000000e+00             18720s
  104220 DPushes remaining with DInf 0.0000000e+00             18725s
  103220 DPushes remaining with DInf 0.0000000e+00             18731s
  102358 DPushes remaining with DInf 0.0000000e+00             18735s
  101221 DPushes remaining with DInf 0.0000000e+00             18740s
  100144 DPushes remaining with DInf 0.0000000e+00             18745s
   98924 DPushes remaining with DInf 0.0000000e+00             18751s
   97826 DPushes remaining with DInf 0.0000000e+00             18755s
   96565 DPushes remaining with DInf 0.0000000e+00             18760s
   95515 DPushes remaining with DInf 0.0000000e+00             18765s
   94662 DPushes remaining with DInf 0.0000000e+00             18771s
   93683 DPushes remaining with DInf 0.0000000e+00             18776s
   92744 DPushes remaining with DInf 0.0000000e+00             18780s
   91678 DPushes remaining with DInf 0.0000000e+00             18785s
   90546 DPushes remaining with DInf 0.0000000e+00             18790s
   89596 DPushes remaining with DInf 0.0000000e+00             18796s
   88717 DPushes remaining with DInf 0.0000000e+00             18800s
   87633 DPushes remaining with DInf 0.0000000e+00             18805s
   86542 DPushes remaining with DInf 0.0000000e+00             18810s
   85432 DPushes remaining with DInf 0.0000000e+00             18815s
   84316 DPushes remaining with DInf 0.0000000e+00             18821s
   83300 DPushes remaining with DInf 0.0000000e+00             18826s
   82298 DPushes remaining with DInf 0.0000000e+00             18831s
   81457 DPushes remaining with DInf 0.0000000e+00             18835s
   80446 DPushes remaining with DInf 0.0000000e+00             18841s
   79459 DPushes remaining with DInf 0.0000000e+00             18845s
   78470 DPushes remaining with DInf 0.0000000e+00             18851s
   77700 DPushes remaining with DInf 0.0000000e+00             18855s
   76716 DPushes remaining with DInf 0.0000000e+00             18860s
   75765 DPushes remaining with DInf 0.0000000e+00             18865s
   74840 DPushes remaining with DInf 0.0000000e+00             18871s
   74085 DPushes remaining with DInf 0.0000000e+00             18875s
   73156 DPushes remaining with DInf 0.0000000e+00             18880s
   72286 DPushes remaining with DInf 0.0000000e+00             18885s
   71399 DPushes remaining with DInf 0.0000000e+00             18890s
   70546 DPushes remaining with DInf 0.0000000e+00             18896s
   69882 DPushes remaining with DInf 0.0000000e+00             18900s
   69072 DPushes remaining with DInf 0.0000000e+00             18905s
   68286 DPushes remaining with DInf 0.0000000e+00             18910s
   67521 DPushes remaining with DInf 0.0000000e+00             18915s
   66755 DPushes remaining with DInf 0.0000000e+00             18921s
   66030 DPushes remaining with DInf 0.0000000e+00             18926s
   65292 DPushes remaining with DInf 0.0000000e+00             18931s
   64710 DPushes remaining with DInf 0.0000000e+00             18935s
   64006 DPushes remaining with DInf 0.0000000e+00             18940s
   63345 DPushes remaining with DInf 0.0000000e+00             18945s
   62673 DPushes remaining with DInf 0.0000000e+00             18951s
   62020 DPushes remaining with DInf 0.0000000e+00             18955s
   61357 DPushes remaining with DInf 0.0000000e+00             18960s
   60672 DPushes remaining with DInf 0.0000000e+00             18965s
   60013 DPushes remaining with DInf 0.0000000e+00             18970s
   59319 DPushes remaining with DInf 0.0000000e+00             18975s
   58646 DPushes remaining with DInf 0.0000000e+00             18981s
   58079 DPushes remaining with DInf 0.0000000e+00             18985s
   57326 DPushes remaining with DInf 0.0000000e+00             18991s
   56770 DPushes remaining with DInf 0.0000000e+00             18995s
   56120 DPushes remaining with DInf 0.0000000e+00             19000s
   55490 DPushes remaining with DInf 0.0000000e+00             19005s
   54862 DPushes remaining with DInf 0.0000000e+00             19011s
   54328 DPushes remaining with DInf 0.0000000e+00             19015s
   53704 DPushes remaining with DInf 0.0000000e+00             19020s
   52979 DPushes remaining with DInf 0.0000000e+00             19026s
   52464 DPushes remaining with DInf 0.0000000e+00             19030s
   51846 DPushes remaining with DInf 0.0000000e+00             19035s
   51215 DPushes remaining with DInf 0.0000000e+00             19040s
   50568 DPushes remaining with DInf 0.0000000e+00             19046s
   50048 DPushes remaining with DInf 0.0000000e+00             19050s
   49421 DPushes remaining with DInf 0.0000000e+00             19056s
   48898 DPushes remaining with DInf 0.0000000e+00             19060s
   48272 DPushes remaining with DInf 0.0000000e+00             19065s
   47651 DPushes remaining with DInf 0.0000000e+00             19071s
   47130 DPushes remaining with DInf 0.0000000e+00             19075s
   46485 DPushes remaining with DInf 0.0000000e+00             19081s
   45955 DPushes remaining with DInf 0.0000000e+00             19085s
   45317 DPushes remaining with DInf 0.0000000e+00             19090s
   44678 DPushes remaining with DInf 0.0000000e+00             19096s
   44152 DPushes remaining with DInf 0.0000000e+00             19100s
   43525 DPushes remaining with DInf 0.0000000e+00             19105s
   42866 DPushes remaining with DInf 0.0000000e+00             19111s
   42236 DPushes remaining with DInf 0.0000000e+00             19116s
   41675 DPushes remaining with DInf 0.0000000e+00             19120s
   41046 DPushes remaining with DInf 0.0000000e+00             19125s
   40240 DPushes remaining with DInf 0.0000000e+00             19131s
   39626 DPushes remaining with DInf 0.0000000e+00             19135s
   38925 DPushes remaining with DInf 0.0000000e+00             19141s
   38399 DPushes remaining with DInf 0.0000000e+00             19145s
   37776 DPushes remaining with DInf 0.0000000e+00             19150s
   37155 DPushes remaining with DInf 0.0000000e+00             19155s
   36538 DPushes remaining with DInf 0.0000000e+00             19161s
   36013 DPushes remaining with DInf 0.0000000e+00             19166s
   35496 DPushes remaining with DInf 0.0000000e+00             19170s
   34869 DPushes remaining with DInf 0.0000000e+00             19175s
   34251 DPushes remaining with DInf 0.0000000e+00             19180s
   33629 DPushes remaining with DInf 0.0000000e+00             19185s
   33007 DPushes remaining with DInf 0.0000000e+00             19190s
   32391 DPushes remaining with DInf 0.0000000e+00             19195s
   31771 DPushes remaining with DInf 0.0000000e+00             19201s
   31264 DPushes remaining with DInf 0.0000000e+00             19205s
   30655 DPushes remaining with DInf 0.0000000e+00             19210s
   30142 DPushes remaining with DInf 0.0000000e+00             19215s
   29527 DPushes remaining with DInf 0.0000000e+00             19220s
   28917 DPushes remaining with DInf 0.0000000e+00             19226s
   28405 DPushes remaining with DInf 0.0000000e+00             19230s
   27799 DPushes remaining with DInf 0.0000000e+00             19235s
   27192 DPushes remaining with DInf 0.0000000e+00             19241s
   26685 DPushes remaining with DInf 0.0000000e+00             19245s
   26076 DPushes remaining with DInf 0.0000000e+00             19251s
   25571 DPushes remaining with DInf 0.0000000e+00             19255s
   24963 DPushes remaining with DInf 0.0000000e+00             19261s
   24456 DPushes remaining with DInf 0.0000000e+00             19265s
   23846 DPushes remaining with DInf 0.0000000e+00             19271s
   23338 DPushes remaining with DInf 0.0000000e+00             19275s
   22732 DPushes remaining with DInf 0.0000000e+00             19280s
   22126 DPushes remaining with DInf 0.0000000e+00             19286s
   21620 DPushes remaining with DInf 0.0000000e+00             19290s
   21013 DPushes remaining with DInf 0.0000000e+00             19295s
   20405 DPushes remaining with DInf 0.0000000e+00             19301s
   19899 DPushes remaining with DInf 0.0000000e+00             19305s
   19293 DPushes remaining with DInf 0.0000000e+00             19310s
   18687 DPushes remaining with DInf 0.0000000e+00             19316s
   18181 DPushes remaining with DInf 0.0000000e+00             19320s
   17575 DPushes remaining with DInf 0.0000000e+00             19326s
   17068 DPushes remaining with DInf 0.0000000e+00             19330s
   16462 DPushes remaining with DInf 0.0000000e+00             19336s
   15957 DPushes remaining with DInf 0.0000000e+00             19340s
   15351 DPushes remaining with DInf 0.0000000e+00             19346s
   14846 DPushes remaining with DInf 0.0000000e+00             19350s
   14240 DPushes remaining with DInf 0.0000000e+00             19355s
   13735 DPushes remaining with DInf 0.0000000e+00             19360s
   13129 DPushes remaining with DInf 0.0000000e+00             19366s
   12624 DPushes remaining with DInf 0.0000000e+00             19370s
   12017 DPushes remaining with DInf 0.0000000e+00             19376s
   11512 DPushes remaining with DInf 0.0000000e+00             19380s
   10906 DPushes remaining with DInf 0.0000000e+00             19385s
   10300 DPushes remaining with DInf 0.0000000e+00             19391s
    9694 DPushes remaining with DInf 0.0000000e+00             19396s
    9189 DPushes remaining with DInf 0.0000000e+00             19400s
    8583 DPushes remaining with DInf 0.0000000e+00             19406s
    8078 DPushes remaining with DInf 0.0000000e+00             19410s
    7471 DPushes remaining with DInf 0.0000000e+00             19416s
    6966 DPushes remaining with DInf 0.0000000e+00             19420s
    6360 DPushes remaining with DInf 0.0000000e+00             19426s
    5854 DPushes remaining with DInf 0.0000000e+00             19430s
    5248 DPushes remaining with DInf 0.0000000e+00             19436s
    4743 DPushes remaining with DInf 0.0000000e+00             19440s
    4136 DPushes remaining with DInf 0.0000000e+00             19446s
    3631 DPushes remaining with DInf 0.0000000e+00             19451s
    3025 DPushes remaining with DInf 0.0000000e+00             19456s
    2520 DPushes remaining with DInf 0.0000000e+00             19461s
    2015 DPushes remaining with DInf 0.0000000e+00             19465s
    1409 DPushes remaining with DInf 0.0000000e+00             19471s
     904 DPushes remaining with DInf 0.0000000e+00             19475s
     297 DPushes remaining with DInf 0.0000000e+00             19481s
       0 DPushes remaining with DInf 0.0000000e+00             19483s

 3108700 PPushes remaining with PInf 0.0000000e+00             19485s
 1913212 PPushes remaining with PInf 2.8038811e+00             19492s
  973125 PPushes remaining with PInf 1.2010754e+01             19499s
  403443 PPushes remaining with PInf 1.1281598e+01             19504s
  221422 PPushes remaining with PInf 1.0123593e+01             19507s
   92930 PPushes remaining with PInf 9.3103474e+00             19511s
   35207 PPushes remaining with PInf 9.6247397e+00             19516s
   12387 PPushes remaining with PInf 2.8786066e+00             19521s
    2080 PPushes remaining with PInf 1.5363141e-01             19525s
       0 PPushes remaining with PInf 2.9508948e-02             19527s

  Push phase complete: Pinf 2.9508948e-02, Dinf 2.8613241e+07  19527s


Root simplex log...

Iteration    Objective       Primal Inf.    Dual Inf.      Time
 3860245    5.0524758e+08   0.000000e+00   2.861324e+07  19528s
 3860447    5.0524759e+08   0.000000e+00   3.479392e+06  19531s
 3860851    5.0524759e+08   0.000000e+00   2.586606e+06  19535s
 3861356    5.0524759e+08   0.000000e+00   2.316957e+06  19541s
 3861862    5.0524759e+08   0.000000e+00   1.937160e+06  19546s
 3862266    5.0524759e+08   0.000000e+00   1.676391e+06  19550s
 3862774    5.0524759e+08   0.000000e+00   1.409302e+06  19556s
 3863178    5.0524759e+08   0.000000e+00   1.583164e+06  19560s
 3863686    5.0524759e+08   0.000000e+00   1.310920e+06  19565s
 3864191    5.0524759e+08   0.000000e+00   8.655278e+05  19571s
 3864595    5.0524759e+08   0.000000e+00   7.247184e+05  19575s
 3865103    5.0524759e+08   0.000000e+00   6.105987e+05  19581s
 3865509    5.0524759e+08   0.000000e+00   9.139909e+05  19585s
 3866015    5.0524759e+08   0.000000e+00   4.834233e+05  19591s
 3866423    5.0524759e+08   0.000000e+00   3.849456e+05  19596s
 3866829    5.0524759e+08   0.000000e+00   3.438277e+05  19600s
 3867334    5.0524759e+08   0.000000e+00   2.658868e+05  19606s
 3867738    5.0524759e+08   0.000000e+00   2.466672e+05  19610s
 3868243    5.0524759e+08   0.000000e+00   2.100464e+05  19616s
 3868648    5.0524759e+08   0.000000e+00   1.920585e+05  19620s
 3869153    5.0524759e+08   0.000000e+00   1.757264e+05  19626s
 3869658    5.0524759e+08   0.000000e+00   1.429071e+05  19631s
 3870062    5.0524759e+08   0.000000e+00   1.183920e+05  19635s
 3870468    5.0524759e+08   0.000000e+00   1.313438e+05  19640s
 3870975    5.0524759e+08   0.000000e+00   7.839426e+04  19646s
 3871480    5.0524759e+08   0.000000e+00   5.782641e+04  19651s
 3871885    5.0524759e+08   0.000000e+00   7.110627e+04  19655s
 3872390    5.0524759e+08   0.000000e+00   4.775204e+04  19661s
 3872795    5.0524759e+08   0.000000e+00   4.395589e+04  19666s
 3873199    5.0524759e+08   0.000000e+00   2.469755e+04  19670s
 3873704    5.0524759e+08   0.000000e+00   2.523979e+04  19676s
 3874108    5.0524759e+08   0.000000e+00   1.464760e+04  19680s
 3874513    5.0524759e+08   0.000000e+00   9.763730e+03  19685s
 3875018    5.0524759e+08   0.000000e+00   3.772875e+03  19691s
 3875422    5.0524759e+08   0.000000e+00   9.613720e+01  19696s
 3875827    5.0524759e+08   0.000000e+00   1.378269e+00  19700s
 3875945    5.0524759e+08   0.000000e+00   0.000000e+00  19707s
Crossover time: 1771.52 seconds (1354.96 work units)
Concurrent spin time: 6286.43s (can be avoided by choosing Method=3)

Solved with barrier
 3875945    5.0524759e+08   0.000000e+00   8.024318e+05  19894s
 3876347    5.0524759e+08   0.000000e+00   7.299172e+05  19896s
 3877352    5.0524759e+08   0.000000e+00   5.647678e+05  19901s
 3878156    5.0524759e+08   0.000000e+00   4.588297e+05  19905s
 3879161    5.0524759e+08   0.000000e+00   3.312417e+05  19910s
 3880166    5.0524759e+08   0.000000e+00   1.989207e+05  19916s
 3881171    5.0524759e+08   0.000000e+00   6.868064e+04  19921s
 3882034    5.0524759e+08   0.000000e+00   0.000000e+00  19927s

Extra simplex iterations after uncrush: 6089

Root relaxation: objective 5.052476e+08, 3882034 iterations, 17759.21 seconds (13497.96 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

     0     0 5.0525e+08    0 2508 -1.567e+12 5.0525e+08   100%     - 21704s
H    0     0                    -6.52475e+11 5.0525e+08   100%     - 21755s
H    0     0                    -6.51943e+11 5.0525e+08   100%     - 21755s
H    0     0                    -6.51738e+11 5.0525e+08   100%     - 21756s
     0     0 5.0500e+08    0 3765 -6.517e+11 5.0500e+08   100%     - 22258s
H    0     0                    -2.01663e+10 5.0500e+08   103%     - 22358s
H    0     0                    -2.00507e+10 5.0500e+08   103%     - 22442s
H    0     0                    -2.00507e+10 5.0500e+08   103%     - 22443s
     0     0 5.0498e+08    0 3727 -2.005e+10 5.0498e+08   103%     - 22523s
     0     0 5.0496e+08    0 3837 -2.005e+10 5.0496e+08   103%     - 22570s
     0     0 5.0495e+08    0 3849 -2.005e+10 5.0495e+08   103%     - 22606s
     0     0 5.0494e+08    0 3891 -2.005e+10 5.0494e+08   103%     - 22641s
     0     0 5.0493e+08    0 3886 -2.005e+10 5.0493e+08   103%     - 22676s
     0     0 5.0492e+08    0 3940 -2.005e+10 5.0492e+08   103%     - 22713s
     0     0 5.0491e+08    0 3976 -2.005e+10 5.0491e+08   103%     - 22747s
     0     0 5.0490e+08    0 4047 -2.005e+10 5.0490e+08   103%     - 22818s
     0     0 5.0489e+08    0 4073 -2.005e+10 5.0489e+08   103%     - 22856s
     0     0 5.0488e+08    0 4069 -2.005e+10 5.0488e+08   103%     - 22894s
     0     0 5.0487e+08    0 4087 -2.005e+10 5.0487e+08   103%     - 22953s
     0     0 5.0484e+08    0 4096 -2.005e+10 5.0484e+08   103%     - 23025s
     0     0 5.0484e+08    0 4164 -2.005e+10 5.0484e+08   103%     - 23064s
     0     0 5.0483e+08    0 4087 -2.005e+10 5.0483e+08   103%     - 23089s
     0     0 5.0483e+08    0 4138 -2.005e+10 5.0483e+08   103%     - 23119s
     0     0 5.0482e+08    0 4137 -2.005e+10 5.0482e+08   103%     - 23147s
     0     0 5.0482e+08    0 4119 -2.005e+10 5.0482e+08   103%     - 23175s
     0     0 5.0482e+08    0 4085 -2.005e+10 5.0482e+08   103%     - 23200s
     0     0 5.0481e+08    0 4168 -2.005e+10 5.0481e+08   103%     - 23279s
     0     0 5.0481e+08    0 4111 -2.005e+10 5.0481e+08   103%     - 23320s
     0     0 5.0480e+08    0 4126 -2.005e+10 5.0480e+08   103%     - 23357s
     0     0 5.0480e+08    0 4097 -2.005e+10 5.0480e+08   103%     - 23405s
     0     0 5.0480e+08    0 4091 -2.005e+10 5.0480e+08   103%     - 23429s
     0     0 5.0478e+08    0 4110 -2.005e+10 5.0478e+08   103%     - 23468s
     0     0 5.0478e+08    0 4014 -2.005e+10 5.0478e+08   103%     - 23504s
     0     0 5.0478e+08    0 4119 -2.005e+10 5.0478e+08   103%     - 23527s
     0     0 5.0477e+08    0 4128 -2.005e+10 5.0477e+08   103%     - 23560s
     0     0 5.0477e+08    0 4126 -2.005e+10 5.0477e+08   103%     - 23587s
     0     0 5.0477e+08    0 4015 -2.005e+10 5.0477e+08   103%     - 23615s
     0     0 5.0476e+08    0 4126 -2.005e+10 5.0476e+08   103%     - 23664s
     0     0 5.0476e+08    0 4022 -2.005e+10 5.0476e+08   103%     - 23687s
     0     0 5.0476e+08    0 4056 -2.005e+10 5.0476e+08   103%     - 23772s
     0     0 5.0476e+08    0 4038 -2.005e+10 5.0476e+08   103%     - 23825s
     0     0 5.0475e+08    0 4033 -2.005e+10 5.0475e+08   103%     - 23849s
     0     0 5.0475e+08    0 4029 -2.005e+10 5.0475e+08   103%     - 23874s
     0     0 5.0475e+08    0 4034 -2.005e+10 5.0475e+08   103%     - 23915s
     0     0 5.0474e+08    0 4012 -2.005e+10 5.0474e+08   103%     - 23957s
     0     0 5.0474e+08    0 4057 -2.005e+10 5.0474e+08   103%     - 24001s
     0     0 5.0474e+08    0 4064 -2.005e+10 5.0474e+08   103%     - 24022s
     0     0 5.0474e+08    0 4042 -2.005e+10 5.0474e+08   103%     - 24043s
     0     0 5.0474e+08    0 4064 -2.005e+10 5.0474e+08   103%     - 24069s
     0     0 5.0474e+08    0 4092 -2.005e+10 5.0474e+08   103%     - 24118s
     0     0 5.0474e+08    0 4094 -2.005e+10 5.0474e+08   103%     - 24136s
     0     0 5.0473e+08    0 4094 -2.005e+10 5.0473e+08   103%     - 24150s
     0     0 5.0473e+08    0 4088 -2.005e+10 5.0473e+08   103%     - 24164s
     0     0 5.0473e+08    0 4093 -2.005e+10 5.0473e+08   103%     - 24177s
     0     0 5.0473e+08    0 4109 -2.005e+10 5.0473e+08   103%     - 24193s
     0     0 5.0472e+08    0 4169 -2.005e+10 5.0472e+08   103%     - 24215s
     0     0 5.0472e+08    0 4117 -2.005e+10 5.0472e+08   103%     - 24241s
     0     0 5.0472e+08    0 4113 -2.005e+10 5.0472e+08   103%     - 24259s
     0     0 5.0472e+08    0 4136 -2.005e+10 5.0472e+08   103%     - 24276s
     0     0 5.0472e+08    0 4131 -2.005e+10 5.0472e+08   103%     - 24295s
     0     0 5.0472e+08    0 4122 -2.005e+10 5.0472e+08   103%     - 24312s
     0     0 5.0471e+08    0 4120 -2.005e+10 5.0471e+08   103%     - 24326s
     0     0 5.0471e+08    0 4130 -2.005e+10 5.0471e+08   103%     - 24343s
     0     0 5.0471e+08    0 4110 -2.005e+10 5.0471e+08   103%     - 24360s
     0     0 5.0471e+08    0 4118 -2.005e+10 5.0471e+08   103%     - 24375s
     0     0 5.0471e+08    0 4076 -2.005e+10 5.0471e+08   103%     - 24387s
     0     0 5.0471e+08    0 4066 -2.005e+10 5.0471e+08   103%     - 24405s
     0     0 5.0471e+08    0 4068 -2.005e+10 5.0471e+08   103%     - 24423s
     0     0 5.0471e+08    0 4071 -2.005e+10 5.0471e+08   103%     - 24438s
     0     0 5.0471e+08    0 4070 -2.005e+10 5.0471e+08   103%     - 24452s
     0     0 5.0471e+08    0 4079 -2.005e+10 5.0471e+08   103%     - 24466s
     0     0 5.0470e+08    0 4075 -2.005e+10 5.0470e+08   103%     - 24480s
     0     0 5.0470e+08    0 4075 -2.005e+10 5.0470e+08   103%     - 24495s
     0     0 5.0470e+08    0 4081 -2.005e+10 5.0470e+08   103%     - 24509s
     0     0 5.0470e+08    0 4064 -2.005e+10 5.0470e+08   103%     - 24523s
     0     0 5.0470e+08    0 4074 -2.005e+10 5.0470e+08   103%     - 24538s
     0     0 5.0470e+08    0 4102 -2.005e+10 5.0470e+08   103%     - 24552s
     0     0 5.0470e+08    0 4079 -2.005e+10 5.0470e+08   103%     - 24567s
     0     0 5.0470e+08    0 4102 -2.005e+10 5.0470e+08   103%     - 24581s
     0     0 5.0470e+08    0 4076 -2.005e+10 5.0470e+08   103%     - 24592s
     0     0 5.0470e+08    0 4076 -2.005e+10 5.0470e+08   103%     - 24602s
     0     0 5.0470e+08    0 4122 -2.005e+10 5.0470e+08   103%     - 24618s
     0     0 5.0470e+08    0 4088 -2.005e+10 5.0470e+08   103%     - 24629s
     0     0 5.0470e+08    0 4121 -2.005e+10 5.0470e+08   103%     - 24638s
     0     0 5.0470e+08    0 4091 -2.005e+10 5.0470e+08   103%     - 24646s
     0     0 5.0470e+08    0 4091 -2.005e+10 5.0470e+08   103%     - 24658s
     0     0 5.0470e+08    0 4124 -2.005e+10 5.0470e+08   103%     - 24667s
     0     0 5.0470e+08    0 4098 -2.005e+10 5.0470e+08   103%     - 24678s
     0     0 5.0470e+08    0 4129 -2.005e+10 5.0470e+08   103%     - 24690s
     0     0 5.0470e+08    0 4097 -2.005e+10 5.0470e+08   103%     - 24702s
     0     0 5.0470e+08    0 4097 -2.005e+10 5.0470e+08   103%     - 24711s
     0     0 5.0470e+08    0 4126 -2.005e+10 5.0470e+08   103%     - 24720s
     0     0 5.0470e+08    0 4095 -2.005e+10 5.0470e+08   103%     - 24732s
     0     0 5.0470e+08    0 4127 -2.005e+10 5.0470e+08   103%     - 24743s
     0     0 5.0470e+08    0 4096 -2.005e+10 5.0470e+08   103%     - 24752s
     0     0 5.0470e+08    0 4148 -2.005e+10 5.0470e+08   103%     - 24764s
     0     0 5.0469e+08    0 4117 -2.005e+10 5.0469e+08   103%     - 24776s
     0     0 5.0469e+08    0 4120 -2.005e+10 5.0469e+08   103%     - 24790s
     0     0 5.0469e+08    0 4150 -2.005e+10 5.0469e+08   103%     - 24804s
     0     0 5.0469e+08    0 4121 -2.005e+10 5.0469e+08   103%     - 24816s
     0     0 5.0469e+08    0 4130 -2.005e+10 5.0469e+08   103%     - 24828s
     0     0 5.0469e+08    0 4132 -2.005e+10 5.0469e+08   103%     - 24840s
     0     0 5.0469e+08    0 4131 -2.005e+10 5.0469e+08   103%     - 24851s
     0     0 5.0469e+08    0 4133 -2.005e+10 5.0469e+08   103%     - 24865s
     0     0 5.0469e+08    0 4124 -2.005e+10 5.0469e+08   103%     - 24881s
     0     0 5.0469e+08    0 4126 -2.005e+10 5.0469e+08   103%     - 24896s
     0     0 5.0469e+08    0 4121 -2.005e+10 5.0469e+08   103%     - 24905s
     0     0 5.0469e+08    0 4123 -2.005e+10 5.0469e+08   103%     - 24915s
     0     0 5.0469e+08    0 4123 -2.005e+10 5.0469e+08   103%     - 24926s
     0     0 5.0469e+08    0 4122 -2.005e+10 5.0469e+08   103%     - 24937s
     0     0 5.0469e+08    0 4120 -2.005e+10 5.0469e+08   103%     - 24946s
     0     0 5.0469e+08    0 4119 -2.005e+10 5.0469e+08   103%     - 24958s
     0     0 5.0469e+08    0 4112 -2.005e+10 5.0469e+08   103%     - 24973s
     0     0 5.0469e+08    0 4112 -2.005e+10 5.0469e+08   103%     - 24982s
     0     0 5.0469e+08    0 4112 -2.005e+10 5.0469e+08   103%     - 24991s
     0     0 5.0469e+08    0 4112 -2.005e+10 5.0469e+08   103%     - 24997s
     0     0 5.0469e+08    0 4112 -2.005e+10 5.0469e+08   103%     - 25006s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25015s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25024s
     0     0 5.0469e+08    0 4109 -2.005e+10 5.0469e+08   103%     - 25033s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25043s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25052s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25061s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25070s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25077s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25083s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25094s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25100s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25107s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25117s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25126s
     0     0 5.0469e+08    0 4111 -2.005e+10 5.0469e+08   103%     - 25132s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25140s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25149s
     0     0 5.0469e+08    0 4110 -2.005e+10 5.0469e+08   103%     - 25156s
     0     0 5.0469e+08    0 4105 -2.005e+10 5.0469e+08   103%     - 25166s
     0     0 5.0469e+08    0 4104 -2.005e+10 5.0469e+08   103%     - 25177s
     0     0 5.0468e+08    0 4104 -2.005e+10 5.0468e+08   103%     - 25183s
     0     0 5.0468e+08    0 4104 -2.005e+10 5.0468e+08   103%     - 25190s
     0     0 5.0468e+08    0 4104 -2.005e+10 5.0468e+08   103%     - 25196s
     0     0 5.0468e+08    0 4105 -2.005e+10 5.0468e+08   103%     - 25202s
     0     0 5.0468e+08    0 4108 -2.005e+10 5.0468e+08   103%     - 25212s
     0     0 5.0468e+08    0 4105 -2.005e+10 5.0468e+08   103%     - 25218s
     0     0 5.0468e+08    0 4105 -2.005e+10 5.0468e+08   103%     - 25227s
     0     0 5.0468e+08    0 4103 -2.005e+10 5.0468e+08   103%     - 25233s
     0     0 5.0468e+08    0 4104 -2.005e+10 5.0468e+08   103%     - 25243s
     0     0 5.0468e+08    0 4105 -2.005e+10 5.0468e+08   103%     - 25250s
     0     0 5.0468e+08    0 4106 -2.005e+10 5.0468e+08   103%     - 25256s
     0     0 5.0468e+08    0 4106 -2.005e+10 5.0468e+08   103%     - 25265s
     0     0 5.0468e+08    0 4107 -2.005e+10 5.0468e+08   103%     - 25274s
     0     0 5.0468e+08    0 4108 -2.005e+10 5.0468e+08   103%     - 25284s
     0     0 5.0468e+08    0 4109 -2.005e+10 5.0468e+08   103%     - 25294s
     0     0 5.0468e+08    0 4110 -2.005e+10 5.0468e+08   103%     - 25304s
     0     0 5.0468e+08    0 4099 -2.005e+10 5.0468e+08   103%     - 25313s
     0     0 5.0468e+08    0 4099 -2.005e+10 5.0468e+08   103%     - 25322s
     0     0 5.0468e+08    0 4099 -2.005e+10 5.0468e+08   103%     - 25333s
     0     0 5.0468e+08    0 4101 -2.005e+10 5.0468e+08   103%     - 25345s
     0     0 5.0468e+08    0 4104 -2.005e+10 5.0468e+08   103%     - 25357s
     0     0 5.0461e+08    0 3563 -2.005e+10 5.0461e+08   103%     - 25565s
H    0     0                    -1.61412e+10 5.0461e+08   103%     - 25657s
H    0     0                    -1.61170e+10 5.0461e+08   103%     - 25741s
H    0     0                    -1.61170e+10 5.0461e+08   103%     - 25742s
     0     0 5.0461e+08    0 3681 -1.612e+10 5.0461e+08   103%     - 25793s
     0     0 5.0461e+08    0 3701 -1.612e+10 5.0461e+08   103%     - 25835s
     0     0 5.0461e+08    0 3687 -1.612e+10 5.0461e+08   103%     - 25860s
     0     0 5.0461e+08    0 3682 -1.612e+10 5.0461e+08   103%     - 25893s
     0     0 5.0461e+08    0 3707 -1.612e+10 5.0461e+08   103%     - 25927s
     0     0 5.0461e+08    0 3749 -1.612e+10 5.0461e+08   103%     - 25959s
     0     0 5.0460e+08    0 3732 -1.612e+10 5.0460e+08   103%     - 25997s
     0     0 5.0460e+08    0 3669 -1.612e+10 5.0460e+08   103%     - 26030s
     0     0 5.0460e+08    0 3665 -1.612e+10 5.0460e+08   103%     - 26046s
     0     0 5.0460e+08    0 3688 -1.612e+10 5.0460e+08   103%     - 26065s
     0     0 5.0460e+08    0 3685 -1.612e+10 5.0460e+08   103%     - 26086s
     0     0 5.0460e+08    0 3695 -1.612e+10 5.0460e+08   103%     - 26120s
     0     0 5.0460e+08    0 3675 -1.612e+10 5.0460e+08   103%     - 26142s
     0     0 5.0460e+08    0 3683 -1.612e+10 5.0460e+08   103%     - 26162s
     0     0 5.0460e+08    0 3558 -1.612e+10 5.0460e+08   103%     - 26193s
     0     0 5.0460e+08    0 3687 -1.612e+10 5.0460e+08   103%     - 26215s
     0     0 5.0460e+08    0 3680 -1.612e+10 5.0460e+08   103%     - 26233s
     0     0 5.0460e+08    0 3549 -1.612e+10 5.0460e+08   103%     - 26275s
     0     0 5.0460e+08    0 3702 -1.612e+10 5.0460e+08   103%     - 26301s
     0     0 5.0451e+08    0 3463 -1.612e+10 5.0451e+08   103%     - 26711s
     0     0 5.0451e+08    0 3461 -1.612e+10 5.0451e+08   103%     - 28608s
H    0     0                    -5.23273e+09 5.0451e+08   110%     - 36058s
H    0     0                    -5.23269e+09 5.0451e+08   110%     - 36059s
H    0     0                    -4.14786e+09 5.0451e+08   112%     - 36139s
H    0     0                    -3.26605e+09 5.0451e+08   115%     - 36196s
H    0     0                    -3.26605e+09 5.0451e+08   115%     - 36227s
H    0     0                    -1.44671e+09 5.0451e+08   135%     - 37530s
H    0     0                    -1.44671e+09 5.0451e+08   135%     - 39761s
H    0     0                    -1.15431e+09 5.0451e+08   144%     - 40454s
     4     2 5.0451e+08    1 1621 -1.154e+09 5.0451e+08   144% 638925 43270s
     4     2 5.0451e+08    1 2522 -1.154e+09 5.0451e+08   144% 644285 43451s
     4     2 5.0451e+08    1 2432 -1.154e+09 5.0451e+08   144% 645324 43510s
     4     2 5.0451e+08    1 2473 -1.154e+09 5.0451e+08   144% 645805 43647s
     4     2 5.0450e+08    1 2594 -1.154e+09 5.0451e+08   144% 648070 43803s
     4     2 5.0448e+08    1 2402 -1.154e+09 5.0451e+08   144% 648778 43831s
     4     2 5.0447e+08    1 2523 -1.154e+09 5.0451e+08   144% 649229 43854s
     4     2 5.0446e+08    1 2496 -1.154e+09 5.0451e+08   144% 652526 43936s
     4     2 5.0445e+08    1 2472 -1.154e+09 5.0451e+08   144% 653452 44099s
     4     2 5.0442e+08    1 2520 -1.154e+09 5.0451e+08   144% 669907 44459s
     4     4 5.0442e+08    1 2520 -1.154e+09 5.0451e+08   144% 669907 46977s
H    4     4                    4.965512e+08 5.0451e+08  1.60% 669907 47018s
     4     6 5.0442e+08    2 2443 4.9655e+08 5.0451e+08  1.60% 669907 47059s
     6     8 5.0439e+08    3 2431 4.9655e+08 5.0451e+08  1.60% 446851 47134s
     8    11 5.0436e+08    4 2384 4.9655e+08 5.0451e+08  1.60% 336824 47219s
    11    17 5.0435e+08    4 2417 4.9655e+08 5.0451e+08  1.60% 246906 47327s
    17    37 5.0433e+08    5 2342 4.9655e+08 5.0451e+08  1.60% 161218 47504s
    37    45 5.0424e+08    8 2327 4.9655e+08 5.0451e+08  1.60% 75502 47840s
    45    59 5.0417e+08    9 2316 4.9655e+08 5.0451e+08  1.60% 62159 48264s
    59    80 5.0417e+08   10 2315 4.9655e+08 5.0451e+08  1.60% 47758 48791s
    80    95 5.0401e+08   14 2233 4.9655e+08 5.0451e+08  1.60% 35511 49280s
    95   121 5.0390e+08   19 2282 4.9655e+08 5.0451e+08  1.60% 30045 49776s
   121   157 5.0379e+08   23 2335 4.9655e+08 5.0451e+08  1.60% 23715 49876s
   157   193 5.0378e+08   28 2026 4.9655e+08 5.0451e+08  1.60% 18451 49992s
   193   229 5.0378e+08   33 1905 4.9655e+08 5.0451e+08  1.60% 15176 50092s
   229   265 5.0378e+08   39 1789 4.9655e+08 5.0451e+08  1.60% 12881 50188s
   265   301 5.0377e+08   45 1788 4.9655e+08 5.0451e+08  1.60% 11217 50215s
   301   337 5.0377e+08   51 1796 4.9655e+08 5.0451e+08  1.60%  9887 50276s
   337   373 5.0376e+08   57 1792 4.9655e+08 5.0451e+08  1.60%  8840 50301s
   373   409 5.0376e+08   62 1742 4.9655e+08 5.0451e+08  1.60%  7994 50347s
   409   442 5.0376e+08   68 1748 4.9655e+08 5.0451e+08  1.60%  7305 50405s
   442   478 5.0376e+08   74 1764 4.9655e+08 5.0451e+08  1.60%  6784 50432s
   478   514 5.0376e+08   80 1765 4.9655e+08 5.0451e+08  1.60%  6277 50458s
H  514   514                    5.020598e+08 5.0451e+08  0.49%  5842 50485s
   515   514 5.0217e+08    1  232 5.0206e+08 5.0451e+08  0.49%  6643 50622s
   515   514 5.0215e+08    1  347 5.0206e+08 5.0451e+08  0.49%  6650 50628s
   515   514 5.0215e+08    1  313 5.0206e+08 5.0451e+08  0.49%  6652 50630s
   515   514 5.0214e+08    1  448 5.0206e+08 5.0451e+08  0.49%  6656 50638s
   515   514 5.0214e+08    1  449 5.0206e+08 5.0451e+08  0.49%  6657 50643s
   515   514 5.0213e+08    1  435 5.0206e+08 5.0450e+08  0.49%  6662 50648s
   515   516 5.0213e+08    1  435 5.0206e+08 5.0450e+08  0.49%  6662 50704s
   515   518 5.0208e+08    2  425 5.0206e+08 5.0450e+08  0.49%  6662 50707s
   517   520 5.0208e+08    3  324 5.0206e+08 5.0445e+08  0.48%  6644 50713s
   521   526 5.0208e+08    4  323 5.0206e+08 5.0445e+08  0.48%  6599 50724s
   527   532 5.0208e+08    5  308 5.0206e+08 5.0445e+08  0.48%  6525 50739s
   533   536 5.0208e+08    6  306 5.0206e+08 5.0445e+08  0.48%  6454 50765s
   541   576 5.0208e+08    7  305 5.0206e+08 5.0445e+08  0.48%  6360 50781s
   601   601 5.0207e+08   17  281 5.0206e+08 5.0445e+08  0.48%  5732 50811s
   636   717 5.0207e+08   21  254 5.0206e+08 5.0445e+08  0.48%  5421 50835s
   852   879 5.0207e+08   17  278 5.0206e+08 5.0445e+08  0.48%  4073 50860s
H 1068   879                    5.020612e+08 5.0445e+08  0.47%  3266 50863s
  1068   915 5.0376e+08   85 1751 5.0206e+08 5.0445e+08  0.47%  3266 50931s
  1104   951 5.0376e+08   90 1730 5.0206e+08 5.0445e+08  0.47%  3175 50960s
  1140   987 5.0376e+08   96 1722 5.0206e+08 5.0445e+08  0.47%  3077 50988s
  1176  1021 5.0375e+08  102 1716 5.0206e+08 5.0445e+08  0.47%  2986 51017s
  1210  1057 5.0375e+08  107 1712 5.0206e+08 5.0445e+08  0.47%  2905 51041s
  1246  1093 5.0375e+08  113 1709 5.0206e+08 5.0445e+08  0.47%  2822 51064s
  1282  1129 5.0375e+08  119 1700 5.0206e+08 5.0445e+08  0.47%  2744 51088s
  1318  1165 5.0375e+08  125 1675 5.0206e+08 5.0445e+08  0.47%  2670 51111s
  1354  1189 5.0375e+08  131 1684 5.0206e+08 5.0445e+08  0.47%  2600 51151s
  1378  1204 5.0375e+08  135 1676 5.0206e+08 5.0445e+08  0.47%  2555 51183s
  1393  1225 5.0375e+08  136 1682 5.0206e+08 5.0445e+08  0.47%  2529 51219s
  1414  1246 5.0375e+08  137 1679 5.0206e+08 5.0445e+08  0.47%  2492 51251s
  1435  1267 5.0375e+08  138 1678 5.0206e+08 5.0445e+08  0.47%  2456 51285s
  1456  1279 5.0375e+08  139 1678 5.0206e+08 5.0445e+08  0.47%  2422 51349s
  1468  1310 5.0375e+08  141 1674 5.0206e+08 5.0445e+08  0.47%  2402 51375s
  1499  1346 5.0375e+08  147 1650 5.0206e+08 5.0445e+08  0.47%  2355 51402s
  1535  1380 5.0375e+08  153 1648 5.0206e+08 5.0445e+08  0.47%  2301 51427s
  1569  1416 5.0375e+08  159 1639 5.0206e+08 5.0445e+08  0.47%  2252 51447s
  1605  1445 5.0375e+08  165 1666 5.0206e+08 5.0445e+08  0.47%  2203 51476s
  1634  1473 5.0375e+08  167 1630 5.0206e+08 5.0445e+08  0.47%  2166 51506s
  1662  1503 5.0375e+08  168 1629 5.0206e+08 5.0445e+08  0.47%  2133 51536s
  1692  1534 5.0375e+08  173 1697 5.0206e+08 5.0445e+08  0.47%  2098 51560s
H 1723  1534                    5.023721e+08 5.0445e+08  0.41%  2062 51594s
  1724  1534 5.0258e+08    1  405 5.0237e+08 5.0445e+08  0.41%  2206 51884s
  1724  1534 5.0254e+08    1  563 5.0237e+08 5.0445e+08  0.41%  2209 51898s
  1724  1534 5.0253e+08    1  516 5.0237e+08 5.0445e+08  0.41%  2209 51902s
  1724  1534 5.0253e+08    1  497 5.0237e+08 5.0445e+08  0.41%  2210 51912s
  1724  1534 5.0252e+08    1  495 5.0237e+08 5.0445e+08  0.41%  2211 51920s
  1724  1534 5.0252e+08    1  506 5.0237e+08 5.0445e+08  0.41%  2211 51930s
  1724  1534 5.0251e+08    1  504 5.0237e+08 5.0445e+08  0.41%  2215 51943s
  1724  1536 5.0251e+08    1  504 5.0237e+08 5.0445e+08  0.41%  2215 52001s
  1724  1538 5.0247e+08    2  509 5.0237e+08 5.0445e+08  0.41%  2215 52010s
  1726  1542 5.0242e+08    3  508 5.0237e+08 5.0445e+08  0.41%  2215 52025s
  1736  1546 5.0240e+08    5  374 5.0237e+08 5.0443e+08  0.41%  2207 52037s
  1746  1545 5.0239e+08    7  340 5.0237e+08 5.0443e+08  0.41%  2198 52043s
  1754  1547 5.0239e+08    8  359 5.0237e+08 5.0443e+08  0.41%  2190 52049s
  1760  1545 5.0239e+08    9  364 5.0237e+08 5.0443e+08  0.41%  2184 52062s
  1769  1548     cutoff    9      5.0237e+08 5.0443e+08  0.41%  2175 52072s
  1776  1561 5.0240e+08    7  341 5.0237e+08 5.0442e+08  0.41%  2167 52084s
  1802  1569 infeasible    8      5.0237e+08 5.0442e+08  0.41%  2137 52101s
  1838  1604 5.0239e+08    9  364 5.0237e+08 5.0442e+08  0.41%  2104 52124s
  1889  1690 5.0238e+08   10  369 5.0237e+08 5.0442e+08  0.41%  2053 52154s
  2011  1719 5.0238e+08    9  369 5.0237e+08 5.0441e+08  0.41%  1936 52199s
  2094  1780 5.0238e+08   29  352 5.0237e+08 5.0441e+08  0.40%  1867 52244s
  2209  1868     cutoff   39      5.0237e+08 5.0441e+08  0.40%  1780 52311s
  2299  1962 5.0238e+08   29  332 5.0237e+08 5.0440e+08  0.40%  1715 52337s
H 2425  1925                    5.023743e+08 5.0440e+08  0.40%  1628 52341s
  2425  1961 5.0375e+08  179 1651 5.0237e+08 5.0440e+08  0.40%  1628 52365s
  2461  1991 5.0375e+08  185 1661 5.0237e+08 5.0440e+08  0.40%  1605 52385s
  2491  2022 5.0375e+08  189 1649 5.0237e+08 5.0440e+08  0.40%  1586 52406s
  2522  2056 5.0375e+08  195 1647 5.0237e+08 5.0440e+08  0.40%  1567 52427s
  2556  2080 5.0375e+08  201 1641 5.0237e+08 5.0440e+08  0.40%  1547 52459s
  2580  2089 5.0375e+08  205 1635 5.0237e+08 5.0440e+08  0.40%  1533 52489s
  2589  2122 5.0375e+08  206 1634 5.0237e+08 5.0440e+08  0.40%  1528 52511s
  2622  2158 5.0375e+08  210 1570 5.0237e+08 5.0440e+08  0.40%  1509 52531s
  2658  2170 5.0375e+08  216 1568 5.0237e+08 5.0440e+08  0.40%  1489 52578s
  2670  2199 5.0375e+08  218 1569 5.0237e+08 5.0440e+08  0.40%  1483 52601s
  2699  2228 5.0375e+08  224 1555 5.0237e+08 5.0440e+08  0.40%  1467 52620s
  2728  2260 5.0375e+08  230 1559 5.0237e+08 5.0440e+08  0.40%  1452 52645s
  2760  2295 5.0375e+08  236 1553 5.0237e+08 5.0440e+08  0.40%  1435 52666s
  2795  2331 5.0375e+08  242 1539 5.0237e+08 5.0440e+08  0.40%  1418 52688s
  2831  2365 5.0375e+08  248 1523 5.0237e+08 5.0440e+08  0.40%  1400 52707s
  2865  2401 5.0375e+08  252 1520 5.0237e+08 5.0440e+08  0.40%  1384 52724s
  2901  2435 5.0375e+08  258 1520 5.0237e+08 5.0440e+08  0.40%  1367 52743s
  2935  2470 5.0375e+08  264 1515 5.0237e+08 5.0440e+08  0.40%  1351 52763s
  2970  2505 5.0375e+08  269 1510 5.0237e+08 5.0440e+08  0.40%  1336 52781s
  3005  2538 5.0375e+08  275 1504 5.0237e+08 5.0440e+08  0.40%  1320 52799s
  3038  2569 5.0375e+08  281 1500 5.0237e+08 5.0440e+08  0.40%  1306 52818s
  3069  2599 5.0375e+08  285 1494 5.0237e+08 5.0440e+08  0.40%  1293 52837s
  3099  2632 5.0375e+08  290 1492 5.0237e+08 5.0440e+08  0.40%  1281 52855s
  3132  2664 5.0374e+08  293 1480 5.0237e+08 5.0440e+08  0.40%  1267 52872s
  3164  2696 5.0374e+08  298 1471 5.0237e+08 5.0440e+08  0.40%  1254 52890s
  3196  2727 5.0374e+08  303 1465 5.0237e+08 5.0440e+08  0.40%  1242 52908s
  3227  2759 5.0374e+08  308 1458 5.0237e+08 5.0440e+08  0.40%  1230 52925s
  3259  2765 5.0374e+08  313 1449 5.0237e+08 5.0440e+08  0.40%  1218 52952s
  3265  2797 5.0374e+08  314 1448 5.0237e+08 5.0440e+08  0.40%  1216 52972s
H 3297  2797                    5.035156e+08 5.0440e+08  0.18%  1204 53003s
  3297  2871     cutoff   46      5.0352e+08 5.0440e+08  0.18%  1204 53031s
  3513  2992 5.0352e+08   23  229 5.0352e+08 5.0440e+08  0.18%  1138 53059s
  3706  3101 5.0352e+08   16  253 5.0352e+08 5.0440e+08  0.18%  1083 53089s
  3881  3220 5.0352e+08   40  176 5.0352e+08 5.0440e+08  0.18%  1038 53114s
  4095  3356 5.0352e+08   36  183 5.0352e+08 5.0440e+08  0.18%   990 53137s
H 4310  3356                    5.035156e+08 5.0440e+08  0.18%   945 53140s
  4310  3392 5.0374e+08  319 1440 5.0352e+08 5.0440e+08  0.18%   945 53160s
  4346  3422 5.0374e+08  325 1429 5.0352e+08 5.0440e+08  0.18%   937 53177s
  4376  3452 5.0374e+08  330 1423 5.0352e+08 5.0440e+08  0.18%   930 53194s
  4406  3484 5.0374e+08  334 1416 5.0352e+08 5.0440e+08  0.18%   924 53212s
  4438  3516 5.0374e+08  340 1411 5.0352e+08 5.0440e+08  0.18%   917 53230s
  4470  3534 5.0374e+08  344 1405 5.0352e+08 5.0440e+08  0.18%   911 53259s
  4488  3540 5.0374e+08  347 1401 5.0352e+08 5.0440e+08  0.18%   907 53287s
  4494  3546 5.0374e+08  348 1400 5.0352e+08 5.0440e+08  0.18%   906 53312s
  4500  3562 5.0374e+08  349 1399 5.0352e+08 5.0440e+08  0.18%   905 53341s
  4516  3597 5.0374e+08  353 1395 5.0352e+08 5.0440e+08  0.18%   902 53360s
  4551  3632 5.0374e+08  359 1387 5.0352e+08 5.0440e+08  0.18%   895 53378s
  4586  3666 5.0374e+08  365 1380 5.0352e+08 5.0440e+08  0.18%   888 53398s
  4620  3701 5.0374e+08  371 1373 5.0352e+08 5.0440e+08  0.18%   882 53417s
  4655  3736 5.0374e+08  377 1370 5.0352e+08 5.0440e+08  0.18%   875 53436s
  4690  3769 5.0374e+08  382 1368 5.0352e+08 5.0440e+08  0.18%   869 53455s
  4723  3805 5.0374e+08  387 1364 5.0352e+08 5.0440e+08  0.18%   863 53472s
  4759  3840 5.0374e+08  393 1357 5.0352e+08 5.0440e+08  0.18%   856 53490s
  4794  3869 5.0374e+08  399 1330 5.0352e+08 5.0440e+08  0.18%   850 53511s
  4823  3903 5.0374e+08  404 1325 5.0352e+08 5.0440e+08  0.18%   845 53530s
  4857  3937 5.0374e+08  410 1317 5.0352e+08 5.0440e+08  0.18%   839 53547s
  4891  3966 5.0374e+08  416 1313 5.0352e+08 5.0440e+08  0.18%   833 53568s
  4920  3996 5.0374e+08  420 1309 5.0352e+08 5.0440e+08  0.18%   829 53587s
  4950  4026 5.0374e+08  425 1301 5.0352e+08 5.0440e+08  0.18%   824 53605s
  4980  4057 5.0374e+08  431 1300 5.0352e+08 5.0440e+08  0.18%   819 53623s
  5011  4089 5.0374e+08  436 1296 5.0352e+08 5.0440e+08  0.18%   814 53640s
  5043  4123 5.0374e+08  439 1290 5.0352e+08 5.0440e+08  0.18%   809 53658s
  5077  4159 5.0374e+08  443 1284 5.0352e+08 5.0440e+08  0.18%   803 53675s
  5113  4193 5.0374e+08  449 1277 5.0352e+08 5.0440e+08  0.18%   798 53693s
  5147  4223 5.0374e+08  453 1273 5.0352e+08 5.0440e+08  0.18%   792 53711s
  5177  4254 5.0374e+08  457 1275 5.0352e+08 5.0440e+08  0.18%   788 53730s
  5208  4285 5.0374e+08  462 1267 5.0352e+08 5.0440e+08  0.18%   783 53749s
  5239  4320 5.0374e+08  467 1262 5.0352e+08 5.0440e+08  0.18%   779 53767s
  5274  4354 5.0374e+08  472 1257 5.0352e+08 5.0440e+08  0.18%   773 53786s
  5308  4388 5.0374e+08  477 1249 5.0352e+08 5.0440e+08  0.18%   768 53804s
  5342  4419 5.0374e+08  483 1240 5.0352e+08 5.0440e+08  0.18%   764 53822s
  5373  4448 5.0374e+08  487 1235 5.0352e+08 5.0440e+08  0.18%   759 53841s
  5402  4474 5.0374e+08  492 1231 5.0352e+08 5.0440e+08  0.18%   755 53858s
H 5428  4474                    5.035161e+08 5.0440e+08  0.18%   752 53891s
  5428  4614 5.0352e+08   22  200 5.0352e+08 5.0440e+08  0.18%   752 53927s
  5639  4616 5.0352e+08   15  199 5.0352e+08 5.0440e+08  0.18%   727 54153s
  5640  4617 5.0352e+08   15  406 5.0352e+08 5.0440e+08  0.18%   727 54164s
  5641  4618 5.0352e+08   15  423 5.0352e+08 5.0440e+08  0.18%   727 54168s
  5642  4618 5.0352e+08   15  415 5.0352e+08 5.0440e+08  0.18%   727 54186s
  5643  4619 5.0352e+08   15  496 5.0352e+08 5.0440e+08  0.18%   727 54191s
  5644  4620 5.0352e+08   15  495 5.0352e+08 5.0440e+08  0.18%   726 54239s
  5645  4620 5.0352e+08   15  415 5.0352e+08 5.0440e+08  0.18%   726 54286s
  5646  4623 5.0353e+08    1  415 5.0352e+08 5.0440e+08  0.18%   787 54331s
  5649  4626 5.0353e+08    3  285 5.0352e+08 5.0440e+08  0.18%   787 54338s
  5653  4627 5.0353e+08    4  282 5.0352e+08 5.0440e+08  0.18%   788 54340s
  5666  4637 5.0353e+08    6  259 5.0352e+08 5.0440e+08  0.18%   787 54346s
  5684  4639 5.0352e+08    9  205 5.0352e+08 5.0440e+08  0.18%   785 54350s
  5704  4640 5.0352e+08   13  205 5.0352e+08 5.0440e+08  0.18%   783 54367s
  5724  4654 5.0352e+08   18  187 5.0352e+08 5.0440e+08  0.18%   781 54374s
  5759  4660 5.0352e+08   25  175 5.0352e+08 5.0440e+08  0.18%   777 54388s
  5781  4691 5.0352e+08   31  221 5.0352e+08 5.0440e+08  0.18%   774 54408s
  5829  4795     cutoff   39      5.0352e+08 5.0440e+08  0.18%   769 54436s
  6017  4833 5.0352e+08   21  190 5.0352e+08 5.0440e+08  0.18%   748 54474s
  6257  4829 5.0352e+08   20  170 5.0352e+08 5.0440e+08  0.18%   726 54525s
  6459  4828     cutoff   40      5.0352e+08 5.0440e+08  0.17%   708 54582s
H 6662  4760                    5.035161e+08 5.0440e+08  0.17%   690 54584s
  6662  4827 5.0352e+08   50  328 5.0352e+08 5.0440e+08  0.17%   690 54625s
  6784  4841 5.0352e+08   71  309 5.0352e+08 5.0439e+08  0.17%   680 54649s
  6909  4887 5.0352e+08   92  262 5.0352e+08 5.0439e+08  0.17%   669 54675s
  7022  4960 5.0352e+08  113  234 5.0352e+08 5.0439e+08  0.17%   661 54700s
  7135  5046 5.0352e+08  134  210 5.0352e+08 5.0439e+08  0.17%   653 54723s
  7260  5116 5.0352e+08  155  180 5.0352e+08 5.0439e+08  0.17%   643 54752s
  7373  5020     cutoff  176      5.0352e+08 5.0439e+08  0.17%   634 54777s
  7489  5068 5.0352e+08   37  318 5.0352e+08 5.0439e+08  0.17%   627 54801s
  7609  5122 5.0352e+08   20  354 5.0352e+08 5.0439e+08  0.17%   619 54839s
  7704  5181 5.0352e+08   25  351 5.0352e+08 5.0439e+08  0.17%   612 54863s
H 7816  5180                    5.035167e+08 5.0439e+08  0.17%   605 54867s
  7816  5216 5.0374e+08  497 1225 5.0352e+08 5.0439e+08  0.17%   605 54890s
  7852  5248 5.0374e+08  503 1220 5.0352e+08 5.0439e+08  0.17%   602 54908s
  7884  5280 5.0374e+08  508 1212 5.0352e+08 5.0439e+08  0.17%   599 54927s
  7916  5286 5.0374e+08  512 1204 5.0352e+08 5.0439e+08  0.17%   597 54964s
  7922  5297 5.0374e+08  513 1207 5.0352e+08 5.0439e+08  0.17%   597 55022s
  7933  5313 5.0374e+08  514 1205 5.0352e+08 5.0439e+08  0.17%   596 55048s
  7949  5329 5.0374e+08  515 1204 5.0352e+08 5.0439e+08  0.17%   595 55075s
  7965  5346 5.0374e+08  516 1203 5.0352e+08 5.0439e+08  0.17%   593 55112s
  7982  5382 5.0374e+08  519 1199 5.0352e+08 5.0439e+08  0.17%   592 55135s
  8018  5418 5.0374e+08  525 1190 5.0352e+08 5.0439e+08  0.17%   590 55154s
  8054  5452 5.0374e+08  530 1184 5.0352e+08 5.0439e+08  0.17%   587 55178s
  8088  5458 5.0374e+08  536 1178 5.0352e+08 5.0439e+08  0.17%   584 55220s
  8094  5485 5.0374e+08  537 1177 5.0352e+08 5.0439e+08  0.17%   584 55248s
  8121  5521 5.0374e+08  541 1173 5.0352e+08 5.0439e+08  0.17%   582 55267s
  8157  5545 5.0374e+08  545 1169 5.0352e+08 5.0439e+08  0.17%   580 55306s
  8181  5580 5.0374e+08  549 1165 5.0352e+08 5.0439e+08  0.17%   578 55329s
  8216  5615 5.0374e+08  555 1154 5.0352e+08 5.0439e+08  0.17%   575 55352s
  8251  5650 5.0374e+08  561 1144 5.0352e+08 5.0439e+08  0.17%   573 55378s
  8286  5685 5.0374e+08  567 1137 5.0352e+08 5.0439e+08  0.17%   571 55400s
  8321  5721 5.0374e+08  573 1131 5.0352e+08 5.0439e+08  0.17%   568 55420s
  8357  5745 5.0374e+08  579 1124 5.0352e+08 5.0439e+08  0.17%   566 55452s
  8381  5775 5.0373e+08  583 1120 5.0352e+08 5.0439e+08  0.17%   564 55477s
  8411  5450 5.0373e+08  587 1113 5.0352e+08 5.0439e+08  0.17%   562 55499s
  8442  5471 5.0373e+08  593 1108 5.0352e+08 5.0439e+08  0.17%   560 55525s
  8470  5300 5.0377e+08   12 1863 5.0352e+08 5.0439e+08  0.17%   558 61141s
  8471  5301 5.0373e+08   12 4540 5.0352e+08 5.0439e+08  0.17%   558 61395s
  8472  5302 5.0393e+08   12 4489 5.0352e+08 5.0439e+08  0.17%   558 61504s
  8473  5302 5.0376e+08   12 4501 5.0352e+08 5.0439e+08  0.17%   558 61599s
  8474  5303 5.0417e+08   12 4563 5.0352e+08 5.0439e+08  0.17%   558 61664s
  8475  5304 5.0376e+08   12 4524 5.0352e+08 5.0439e+08  0.17%   558 61730s
  8476  5304 5.0373e+08   12 4454 5.0352e+08 5.0439e+08  0.17%   558 61796s
  8477  5305 5.0417e+08   12 4568 5.0352e+08 5.0439e+08  0.17%   558 61854s
  8478  5306 5.0378e+08   12 4495 5.0352e+08 5.0439e+08  0.17%   558 61885s
  8479  5306 5.0396e+08   12 4579 5.0352e+08 5.0439e+08  0.17%   558 61934s
  8480  5307 5.0429e+08   12 4611 5.0352e+08 5.0439e+08  0.17%   558 61966s
  8481  5308 5.0395e+08   12 4574 5.0352e+08 5.0439e+08  0.17%   558 62014s
  8482  5308 5.0376e+08   12 4519 5.0352e+08 5.0439e+08  0.17%   558 62192s
  8483  5309 5.0379e+08   12 3621 5.0352e+08 5.0433e+08  0.16%   558 62338s
  8484  5310 5.0378e+08   12 3514 5.0352e+08 5.0432e+08  0.16%   558 62746s
  8485  5310 5.0374e+08   12 3900 5.0352e+08 5.0429e+08  0.15%   557 64293s
  8486  5148 5.0428e+08    1 3900 5.0352e+08 5.0429e+08  0.15%   849 64960s
  8487  5150 5.0426e+08    2 3866 5.0352e+08 5.0429e+08  0.15%   849 64980s
  8489  5152 5.0425e+08    3 3619 5.0352e+08 5.0428e+08  0.15%   849 65028s
  8492  5157 5.0424e+08    4 3427 5.0352e+08 5.0428e+08  0.15%   850 65098s
  8498  5161 5.0422e+08    5 3138 5.0352e+08 5.0428e+08  0.15%   854 65179s
  8504  5031 5.0418e+08    6 3126 5.0352e+08 5.0428e+08  0.15%   856 65438s
  8532  4904 5.0376e+08    9 3288 5.0352e+08 5.0428e+08  0.15%   859 65607s
  8563  4906 5.0414e+08    9 3093 5.0352e+08 5.0428e+08  0.15%   859 65798s
  8586  4918     cutoff   12      5.0352e+08 5.0428e+08  0.15%   859 66008s
  8615  4930 5.0399e+08   14 2707 5.0352e+08 5.0428e+08  0.15%   861 66221s
  8637  4939 5.0399e+08   15 2684 5.0352e+08 5.0428e+08  0.15%   860 66483s
  8655  4947 5.0395e+08   15 2638 5.0352e+08 5.0428e+08  0.15%   860 66730s
  8673  4830     cutoff   16      5.0352e+08 5.0428e+08  0.15%   859 66815s
  8709  4838 5.0391e+08   19 2758 5.0352e+08 5.0428e+08  0.15%   859 66933s
  8743  4848 5.0386e+08   22 2705 5.0352e+08 5.0428e+08  0.15%   859 67016s
  8779  4854 5.0380e+08   25 2681 5.0352e+08 5.0428e+08  0.15%   859 67124s
  8799  4864 5.0377e+08   28 2507 5.0352e+08 5.0428e+08  0.15%   860 67237s
  8821  4875 5.0375e+08   30 2385 5.0352e+08 5.0428e+08  0.15%   860 67353s
  8852  4870     cutoff   30      5.0352e+08 5.0428e+08  0.15%   861 67559s
  8859  4871     cutoff   31      5.0352e+08 5.0428e+08  0.15%   861 67701s
  8868  4882     cutoff   32      5.0352e+08 5.0428e+08  0.15%   860 67955s
  8902  4879 5.0375e+08   35 2295 5.0352e+08 5.0428e+08  0.15%   857 68163s
  8923  4885 infeasible   36      5.0352e+08 5.0426e+08  0.15%   857 68483s
  8948  4889 5.0414e+08    9 3024 5.0352e+08 5.0425e+08  0.15%   857 68794s
  8972  4895 5.0396e+08   13 3110 5.0352e+08 5.0425e+08  0.15%   858 69101s
  8996  4915 5.0391e+08   19 2713 5.0352e+08 5.0425e+08  0.15%   859 69294s
  9024  4797 5.0392e+08   21 2731 5.0352e+08 5.0425e+08  0.15%   860 69396s
  9060  4816     cutoff   24      5.0352e+08 5.0425e+08  0.15%   859 69509s
  9095  4820 5.0379e+08   28 2483 5.0352e+08 5.0425e+08  0.15%   859 69623s
  9125  4837 5.0378e+08   29 2203 5.0352e+08 5.0425e+08  0.15%   859 69740s
  9158  4845 5.0378e+08   34 2078 5.0352e+08 5.0425e+08  0.15%   859 69847s
  9187  4863 5.0377e+08   40 2107 5.0352e+08 5.0425e+08  0.15%   860 69959s
  9215  4888 5.0377e+08   45 2120 5.0352e+08 5.0425e+08  0.15%   860 70041s
H 9251  4876                    5.037494e+08 5.0425e+08  0.10%   859 70073s
  9251  4974 5.0375e+08   39  155 5.0375e+08 5.0425e+08  0.10%   859 70107s
  9491  4999     cutoff   35      5.0375e+08 5.0425e+08  0.10%   840 70133s
  9716  5042 5.0375e+08   25  167 5.0375e+08 5.0425e+08  0.10%   824 70163s
  9925  5060     cutoff   29      5.0375e+08 5.0425e+08  0.10%   809 70200s
 10093  5139 5.0375e+08   28  191 5.0375e+08 5.0425e+08  0.10%   798 70233s
 10330  5131 5.0375e+08   26  168 5.0375e+08 5.0425e+08  0.10%   783 70287s
 10483  5187     cutoff   35      5.0375e+08 5.0425e+08  0.10%   773 70314s
 10723  5143 5.0377e+08   51 2082 5.0375e+08 5.0425e+08  0.10%   758 70381s
 10759  5161 5.0376e+08   56 2082 5.0375e+08 5.0425e+08  0.10%   757 70417s
 10791  5185 5.0376e+08   62 2107 5.0375e+08 5.0425e+08  0.10%   755 70457s
 10826  5204 5.0376e+08   68 2055 5.0375e+08 5.0425e+08  0.10%   753 70493s
 10856  5221 5.0376e+08   74 2083 5.0375e+08 5.0425e+08  0.10%   751 70526s
 10885  5233 5.0376e+08   80 2082 5.0375e+08 5.0425e+08  0.10%   750 70560s
 10915  5246 5.0376e+08   86 2087 5.0375e+08 5.0425e+08  0.10%   748 70595s
 10940  5261 5.0375e+08   92 2031 5.0375e+08 5.0425e+08  0.10%   746 70631s
 10969  5277 5.0375e+08   98 2037 5.0375e+08 5.0424e+08  0.10%   745 70667s
 10999  5290 5.0375e+08  104 2036 5.0375e+08 5.0424e+08  0.10%   744 70721s
 11028  5301 5.0375e+08  110 2021 5.0375e+08 5.0424e+08  0.10%   743 70764s
 11051  5313 5.0375e+08  115 2019 5.0375e+08 5.0424e+08  0.10%   742 70811s
 11080  5329 5.0375e+08  121 2017 5.0375e+08 5.0424e+08  0.10%   740 70854s
 11106  5335 5.0375e+08  127 1999 5.0375e+08 5.0424e+08  0.10%   739 70900s
 11129  5343 5.0375e+08  133 1993 5.0375e+08 5.0424e+08  0.10%   738 70945s
 11148  5344 5.0375e+08  137 2022 5.0375e+08 5.0424e+08  0.10%   738 70985s
 11166  5346 5.0375e+08  143 2015 5.0375e+08 5.0424e+08  0.10%   737 71028s
 11184  5351 5.0375e+08  149 2010 5.0375e+08 5.0424e+08  0.10%   737 71071s
 11203  5349 5.0375e+08  155 1979 5.0375e+08 5.0424e+08  0.10%   736 71113s
 11225  5355 5.0375e+08  159 1985 5.0375e+08 5.0424e+08  0.10%   735 71168s
 11244  5351 infeasible  162      5.0375e+08 5.0424e+08  0.10%   734 71241s
 11253  5353 5.0375e+08  161 1941 5.0375e+08 5.0424e+08  0.10%   735 71286s
 11264  5356 5.0375e+08  164 1975 5.0375e+08 5.0424e+08  0.10%   735 71338s
 11276  5360 5.0375e+08  168 1934 5.0375e+08 5.0424e+08  0.10%   735 71403s
 11290  5360 5.0375e+08  170 1799 5.0375e+08 5.0424e+08  0.10%   735 71451s
 11299  5361     cutoff  175      5.0375e+08 5.0424e+08  0.10%   735 71524s
 11319  5362     cutoff  172      5.0375e+08 5.0424e+08  0.10%   735 71578s
 11337  5372 5.0417e+08    7 3169 5.0375e+08 5.0423e+08  0.09%   735 71630s
 11355  5384 5.0410e+08   10 3116 5.0375e+08 5.0423e+08  0.09%   735 71693s
 11375  5386 5.0392e+08   15 3073 5.0375e+08 5.0423e+08  0.09%   735 71774s
 11397  5384 5.0389e+08   17 3081 5.0375e+08 5.0423e+08  0.09%   736 71849s
 11415  5385 5.0377e+08   21 3022 5.0375e+08 5.0423e+08  0.09%   737 71901s
 11434  5389     cutoff   24      5.0375e+08 5.0423e+08  0.09%   737 71986s
 11456  5396 5.0375e+08   23 3049 5.0375e+08 5.0421e+08  0.09%   738 72056s
 11478  5399 5.0400e+08   14 2695 5.0375e+08 5.0421e+08  0.09%   738 72112s
 11493  5396 5.0379e+08   18 2967 5.0375e+08 5.0421e+08  0.09%   738 72184s
 11505  5399     cutoff   19      5.0375e+08 5.0421e+08  0.09%   739 72260s
 11526  5407 5.0415e+08    8 2938 5.0375e+08 5.0421e+08  0.09%   739 72329s
 11549  5417 5.0399e+08   14 2639 5.0375e+08 5.0421e+08  0.09%   739 72403s
 11570  5421 5.0391e+08   19 2684 5.0375e+08 5.0421e+08  0.09%   740 72471s
 11595  5423 5.0380e+08   25 2577 5.0375e+08 5.0420e+08  0.09%   740 72531s
 11616  5428 5.0377e+08   22 2646 5.0375e+08 5.0420e+08  0.09%   740 72602s
 11634  5436     cutoff   28      5.0375e+08 5.0420e+08  0.09%   741 72664s
 11660  5439 5.0377e+08   25 2601 5.0375e+08 5.0420e+08  0.09%   740 72726s
 11681  5443     cutoff   28      5.0375e+08 5.0420e+08  0.09%   740 72808s
 11706  5458 5.0406e+08   11 2875 5.0375e+08 5.0420e+08  0.09%   741 72873s
 11734  5467 5.0393e+08   17 2782 5.0375e+08 5.0420e+08  0.09%   740 72932s
 11762  5467 5.0382e+08   23 2688 5.0375e+08 5.0420e+08  0.09%   740 73021s
 11787  5473 5.0376e+08   29 2117 5.0375e+08 5.0420e+08  0.09%   740 73116s
 11808  5476 5.0376e+08   30 2068 5.0375e+08 5.0420e+08  0.09%   741 73175s
 11832  5470 5.0375e+08   36 1989 5.0375e+08 5.0420e+08  0.09%   740 73256s
 11854  5466     cutoff   41      5.0375e+08 5.0419e+08  0.09%   740 73333s
 11869  5476 5.0410e+08    7 3021 5.0375e+08 5.0419e+08  0.09%   740 73396s
 11896  5485 5.0400e+08   12 2849 5.0375e+08 5.0419e+08  0.09%   740 73463s
 11922  5483     cutoff   17      5.0375e+08 5.0419e+08  0.09%   740 73545s
 11951  5479     cutoff   21      5.0375e+08 5.0419e+08  0.09%   740 73612s
 11978  5473 5.0377e+08   21 2860 5.0375e+08 5.0419e+08  0.09%   740 73710s
 11991  5476 5.0375e+08   23 2769 5.0375e+08 5.0419e+08  0.09%   740 73804s
 12019  5483 5.0385e+08   18 2781 5.0375e+08 5.0419e+08  0.09%   741 73879s
 12049  5481 5.0375e+08   20 2740 5.0375e+08 5.0419e+08  0.09%   742 73957s
 12078  5478     cutoff   23      5.0375e+08 5.0419e+08  0.09%   742 74021s
 12109  5467     cutoff   21      5.0375e+08 5.0419e+08  0.09%   742 74106s
 12138  5473 5.0392e+08   16 2696 5.0375e+08 5.0419e+08  0.09%   742 74194s
 12164  5488 5.0379e+08   18 2736 5.0375e+08 5.0419e+08  0.09%   743 74267s
 12195  5488 5.0382e+08   19 2798 5.0375e+08 5.0419e+08  0.09%   743 74335s
 12224  5488 5.0375e+08   23 2706 5.0375e+08 5.0419e+08  0.09%   743 74421s
 12248  5482 5.0387e+08   14 3177 5.0375e+08 5.0419e+08  0.09%   743 74575s
 12258  5489 5.0384e+08   15 3223 5.0375e+08 5.0419e+08  0.09%   743 74648s
 12289  5478     cutoff   21      5.0375e+08 5.0419e+08  0.09%   743 74733s
 12306  5487 infeasible   21      5.0375e+08 5.0419e+08  0.09%   743 74827s
 12325  5484 5.0405e+08   12 2824 5.0375e+08 5.0419e+08  0.09%   745 74930s
 12340  5486 5.0397e+08   15 2761 5.0375e+08 5.0419e+08  0.09%   746 75016s
 12355  5499 5.0389e+08   21 2693 5.0375e+08 5.0419e+08  0.09%   746 75082s
 12375  5511 5.0379e+08   27 2500 5.0375e+08 5.0419e+08  0.09%   746 75151s
 12396  5521 5.0390e+08   17 2776 5.0375e+08 5.0419e+08  0.09%   746 75218s
 12421  5523     cutoff   28      5.0375e+08 5.0419e+08  0.09%   746 75309s
 12449  5534 5.0387e+08   14 3114 5.0375e+08 5.0419e+08  0.09%   746 75373s
 12479  5533     cutoff   28      5.0375e+08 5.0419e+08  0.09%   745 75469s
 12502  5541     cutoff   22      5.0375e+08 5.0418e+08  0.09%   746 75552s
 12524  5548 5.0405e+08   11 2887 5.0375e+08 5.0418e+08  0.09%   746 75630s
 12550  5557 5.0392e+08   17 2765 5.0375e+08 5.0418e+08  0.09%   745 75697s
 12574  5564 5.0381e+08   23 2685 5.0375e+08 5.0418e+08  0.09%   744 75780s
 12595  5620 5.0375e+08   42  314 5.0375e+08 5.0418e+08  0.09%   745 75844s
 12721  5634 5.0375e+08   23  339 5.0375e+08 5.0418e+08  0.09%   739 75870s
 12823  5647     cutoff   23      5.0375e+08 5.0418e+08  0.09%   734 75899s
 12939  5695 5.0375e+08   22  323 5.0375e+08 5.0418e+08  0.09%   728 75927s
 13043  5744 5.0375e+08   26  430 5.0375e+08 5.0418e+08  0.09%   724 75963s
 13158  5802 5.0375e+08   30  363 5.0375e+08 5.0418e+08  0.09%   718 75990s
 13277  5865     cutoff   29      5.0375e+08 5.0418e+08  0.09%   713 76018s
 13396  5927 5.0375e+08   32  315 5.0375e+08 5.0418e+08  0.09%   708 76044s
 13519  5973 5.0375e+08   36  328 5.0375e+08 5.0418e+08  0.09%   702 76073s
 13642  6010     cutoff   24      5.0375e+08 5.0418e+08  0.09%   697 76111s
 13726  6038     cutoff   31      5.0375e+08 5.0418e+08  0.09%   694 76141s
 13826  6045 5.0375e+08   25  398 5.0375e+08 5.0418e+08  0.09%   690 76177s
 13909  6063 5.0375e+08   24  341 5.0375e+08 5.0418e+08  0.09%   686 76208s
 13987  6105     cutoff   25      5.0375e+08 5.0418e+08  0.09%   683 76236s
 14107  6126 5.0375e+08   38  354 5.0375e+08 5.0418e+08  0.09%   678 76263s
 14232  6171 5.0375e+08   26  339 5.0375e+08 5.0418e+08  0.09%   674 76295s
 14348  6214 5.0375e+08   29  354 5.0375e+08 5.0418e+08  0.09%   670 76321s
H14474  6214                    5.037495e+08 5.0418e+08  0.09%   664 76333s
 14474  6232 5.0412e+08    7 2985 5.0375e+08 5.0418e+08  0.09%   664 76458s
 14502  6238 5.0402e+08   12 2825 5.0375e+08 5.0418e+08  0.09%   666 76548s
 14534  6250 5.0385e+08   17 2898 5.0375e+08 5.0418e+08  0.09%   666 76663s
 14561  6250     cutoff   23      5.0375e+08 5.0418e+08  0.09%   667 76766s
 14592  6246 5.0388e+08   15 2773 5.0375e+08 5.0418e+08  0.09%   667 76898s
 14604  6254 5.0388e+08   16 2780 5.0375e+08 5.0418e+08  0.09%   667 77042s
 14624  6265     cutoff   17      5.0375e+08 5.0418e+08  0.09%   667 77143s
 14646  6273 5.0386e+08   18 2680 5.0375e+08 5.0418e+08  0.09%   668 77249s
 14675  6276 5.0379e+08   19 2737 5.0375e+08 5.0418e+08  0.09%   667 77353s
 14698  6293 5.0377e+08   20 2687 5.0375e+08 5.0418e+08  0.09%   667 77454s
 14729  6300 5.0376e+08   21 2632 5.0375e+08 5.0418e+08  0.09%   667 77560s
 14760  6314 5.0375e+08   22 2624 5.0375e+08 5.0418e+08  0.09%   666 77649s
 14794  6322 5.0411e+08    9 2890 5.0375e+08 5.0418e+08  0.09%   666 77741s
 14824  6329 5.0391e+08   15 2907 5.0375e+08 5.0418e+08  0.09%   666 77837s
 14851  6322 infeasible   21      5.0375e+08 5.0418e+08  0.09%   666 77919s
 14881  6314     cutoff   24      5.0375e+08 5.0418e+08  0.09%   667 78009s
 14905  6327 5.0389e+08   14 2840 5.0375e+08 5.0418e+08  0.08%   668 78107s
 14938  6337 5.0380e+08   17 2893 5.0375e+08 5.0418e+08  0.08%   668 78188s
 14971  6334 infeasible   21      5.0375e+08 5.0418e+08  0.08%   668 78281s
 15003  6340 5.0395e+08   13 2785 5.0375e+08 5.0418e+08  0.08%   669 78373s
 15027  6347 5.0388e+08   14 2812 5.0375e+08 5.0418e+08  0.08%   670 78480s
 15058  6355 5.0381e+08   18 2695 5.0375e+08 5.0418e+08  0.08%   670 78589s
 15085  6362     cutoff   23      5.0375e+08 5.0418e+08  0.08%   671 78684s
 15111  6369 5.0397e+08   14 2684 5.0375e+08 5.0418e+08  0.08%   671 78784s
 15138  6369 5.0395e+08   15 2743 5.0375e+08 5.0418e+08  0.08%   671 78868s
 15173  6369 5.0383e+08   21 2740 5.0375e+08 5.0418e+08  0.08%   671 78977s
 15201  6377 5.0378e+08   23 2736 5.0375e+08 5.0418e+08  0.08%   672 79042s
 15232  6372 5.0375e+08   25 2703 5.0375e+08 5.0418e+08  0.08%   671 79132s
 15266  6375 5.0407e+08    9 2917 5.0375e+08 5.0417e+08  0.08%   671 79235s
 15290  6390 5.0400e+08   12 2787 5.0375e+08 5.0417e+08  0.08%   672 79309s
 15319  6396 5.0389e+08   14 2787 5.0375e+08 5.0417e+08  0.08%   672 79386s
 15355  6385 5.0390e+08   17 2694 5.0375e+08 5.0417e+08  0.08%   672 79514s
 15366  6398 infeasible   17      5.0375e+08 5.0417e+08  0.08%   673 79621s
 15398  6408 5.0382e+08   20 2627 5.0375e+08 5.0417e+08  0.08%   672 79698s
 15431  6398 5.0380e+08   23 2620 5.0375e+08 5.0417e+08  0.08%   672 79785s
 15458  6395 infeasible   25      5.0375e+08 5.0417e+08  0.08%   672 79893s
 15482  6403 5.0405e+08    8 2907 5.0375e+08 5.0417e+08  0.08%   674 79962s
 15506  6396 5.0393e+08   14 2666 5.0375e+08 5.0417e+08  0.08%   674 80039s
 15529  6394 5.0383e+08   20 2697 5.0375e+08 5.0417e+08  0.08%   674 80133s
 15547  6398 infeasible   25      5.0375e+08 5.0417e+08  0.08%   675 80248s
 15567  6403 5.0392e+08   14 2764 5.0375e+08 5.0417e+08  0.08%   677 80328s
 15596  6406 5.0391e+08   15 2686 5.0375e+08 5.0417e+08  0.08%   678 80421s
 15623  6405 5.0382e+08   20 2671 5.0375e+08 5.0417e+08  0.08%   678 80503s
 15649  6408 5.0378e+08   23 2614 5.0375e+08 5.0416e+08  0.08%   678 80580s
 15677  6407 5.0390e+08   13 3118 5.0375e+08 5.0416e+08  0.08%   679 80743s
 15695  6399 5.0383e+08   14 3207 5.0375e+08 5.0416e+08  0.08%   678 80854s
 15719  6396     cutoff   19      5.0375e+08 5.0416e+08  0.08%   679 80953s
 15740  6400     cutoff    9      5.0375e+08 5.0416e+08  0.08%   681 81036s
 15769  6404 5.0403e+08   11 2692 5.0375e+08 5.0416e+08  0.08%   681 81128s
 15803  6408 5.0390e+08   14 2591 5.0375e+08 5.0416e+08  0.08%   682 81230s
 15834  6408 5.0384e+08   16 2758 5.0375e+08 5.0416e+08  0.08%   683 81297s
 15870  6403     cutoff   16      5.0375e+08 5.0416e+08  0.08%   683 81404s
 15899  6397 5.0383e+08   19 2728 5.0375e+08 5.0416e+08  0.08%   683 81482s
 15925  6402 5.0381e+08   21 2652 5.0375e+08 5.0416e+08  0.08%   684 81576s
 15951  6402 5.0390e+08   13 3004 5.0375e+08 5.0416e+08  0.08%   685 81687s
 15979  6397 5.0380e+08   15 3160 5.0375e+08 5.0416e+08  0.08%   686 81935s
 15986  6278 5.0380e+08   16 3159 5.0375e+08 5.0416e+08  0.08%   686 82055s
 16006  6274     cutoff   19      5.0375e+08 5.0416e+08  0.08%   686 82154s
 16039  6273     cutoff   15      5.0375e+08 5.0416e+08  0.08%   686 82231s
 16065  6272 5.0383e+08   18 2985 5.0375e+08 5.0416e+08  0.08%   686 82334s
 16088  6266 5.0378e+08   21 2910 5.0375e+08 5.0416e+08  0.08%   687 82447s
 16108  6265 5.0375e+08   20 2903 5.0375e+08 5.0416e+08  0.08%   687 82557s
 16134  6276 5.0405e+08    9 2843 5.0375e+08 5.0416e+08  0.08%   687 82635s
 16165  6270 5.0385e+08   15 2937 5.0375e+08 5.0416e+08  0.08%   687 82726s
 16192  6276     cutoff   20      5.0375e+08 5.0415e+08  0.08%   687 82801s
 16219  6277     cutoff   22      5.0375e+08 5.0415e+08  0.08%   687 82908s
 16249  6276     cutoff    8      5.0375e+08 5.0415e+08  0.08%   687 83011s
 16270  6277 5.0387e+08   13 2779 5.0375e+08 5.0415e+08  0.08%   687 83093s
 16290  6282 5.0378e+08   18 2831 5.0375e+08 5.0415e+08  0.08%   688 83190s
 16321  6281     cutoff   21      5.0375e+08 5.0415e+08  0.08%   689 83296s
 16353  6280     cutoff    9      5.0375e+08 5.0415e+08  0.08%   689 83399s
 16382  6274 5.0391e+08   13 2899 5.0375e+08 5.0415e+08  0.08%   690 83504s
 16408  6276 5.0386e+08   17 2977 5.0375e+08 5.0415e+08  0.08%   691 83627s
 16431  6288 infeasible   22      5.0375e+08 5.0415e+08  0.08%   692 83745s
 16464  6289 5.0388e+08   14 2880 5.0375e+08 5.0415e+08  0.08%   693 83822s
 16494  6286 5.0392e+08   12 2972 5.0375e+08 5.0415e+08  0.08%   692 83925s
 16517  6298 5.0388e+08   14 2952 5.0375e+08 5.0415e+08  0.08%   694 83998s
 16550  6294 5.0376e+08   19 2942 5.0375e+08 5.0415e+08  0.08%   694 84109s
 16579  6288     cutoff   20      5.0375e+08 5.0415e+08  0.08%   694 84229s
 16597  6295 5.0392e+08   12 3063 5.0375e+08 5.0415e+08  0.08%   695 84343s
 16624  6292 5.0389e+08   14 3061 5.0375e+08 5.0415e+08  0.08%   696 84673s
 16630  6307 5.0388e+08   15 3068 5.0375e+08 5.0415e+08  0.08%   696 84874s
 16661  6309 5.0380e+08   20 2962 5.0375e+08 5.0415e+08  0.08%   696 84972s
 16695  6300     cutoff   23      5.0375e+08 5.0415e+08  0.08%   696 85078s
 16721  6307 5.0394e+08   12 2706 5.0375e+08 5.0415e+08  0.08%   696 85164s
 16741  6318     cutoff   18      5.0375e+08 5.0415e+08  0.08%   697 85259s
 16773  6312     cutoff   22      5.0375e+08 5.0415e+08  0.08%   697 85376s
 16797  6309 infeasible   11      5.0375e+08 5.0415e+08  0.08%   698 85474s
 16822  6306 5.0389e+08   14 2872 5.0375e+08 5.0415e+08  0.08%   698 85590s
 16844  6305 5.0376e+08   20 2970 5.0375e+08 5.0414e+08  0.08%   698 85671s
 16872  6307 5.0392e+08   13 2791 5.0375e+08 5.0414e+08  0.08%   698 85791s
H16895  6299                    5.037495e+08 5.0414e+08  0.08%   700 85823s
 16895  6441 5.0375e+08   23  185 5.0375e+08 5.0414e+08  0.08%   700 85882s
 17116  6484 5.0375e+08   37  155 5.0375e+08 5.0414e+08  0.08%   692 85926s
 17325  6472 5.0375e+08   41  196 5.0375e+08 5.0414e+08  0.08%   685 85981s
 17527  6574     cutoff   46      5.0375e+08 5.0414e+08  0.08%   678 86038s
 17732  6715 5.0375e+08   25  173 5.0375e+08 5.0414e+08  0.08%   672 86065s
 17972  6837 5.0375e+08   48  141 5.0375e+08 5.0414e+08  0.08%   664 86091s
 18205  6960 5.0375e+08   29  210 5.0375e+08 5.0414e+08  0.08%   657 86134s
 18441  6968 5.0375e+08   40  160 5.0375e+08 5.0414e+08  0.08%   650 86190s
 18461  7085     cutoff   41      5.0375e+08 5.0414e+08  0.08%   650 86218s
 18691  7216 5.0375e+08   59  111 5.0375e+08 5.0414e+08  0.08%   643 86277s
 18902  7315     cutoff   93      5.0375e+08 5.0414e+08  0.08%   637 86333s
 19093  7418     cutoff   32      5.0375e+08 5.0414e+08  0.08%   632 86373s
H19311  7418                    5.037497e+08 5.0414e+08  0.08%   626 86375s
 19311  7433 5.0383e+08   16 2856 5.0375e+08 5.0414e+08  0.08%   626 86498s
 19342  7438 5.0378e+08   19 2787 5.0375e+08 5.0414e+08  0.08%   627 86580s
 19375  7422     cutoff   23      5.0375e+08 5.0414e+08  0.08%   627 86653s
 19396  7419     cutoff   11      5.0375e+08 5.0414e+08  0.08%   627 86733s
 19410  7424 5.0404e+08   11 2811 5.0375e+08 5.0414e+08  0.08%   628 86906s
 19422  7434 5.0401e+08   12 2803 5.0375e+08 5.0414e+08  0.08%   628 87082s
 19438  7449     cutoff   16      5.0375e+08 5.0414e+08  0.08%   629 87172s
 19474  7437     cutoff   21      5.0375e+08 5.0414e+08  0.08%   629 87247s
 19510  7435     cutoff   24      5.0375e+08 5.0414e+08  0.08%   629 87350s
 19544  7442 5.0398e+08   13 2778 5.0375e+08 5.0414e+08  0.08%   629 87467s
 19571  7453     cutoff   26      5.0375e+08 5.0414e+08  0.08%   630 87554s
 19601  7458 infeasible   25      5.0375e+08 5.0414e+08  0.08%   630 87677s
 19630  7467 5.0397e+08   14 2746 5.0375e+08 5.0414e+08  0.08%   630 87755s
 19656  7479 5.0385e+08   19 2744 5.0375e+08 5.0414e+08  0.08%   631 87860s
 19691  7479     cutoff   23      5.0375e+08 5.0413e+08  0.08%   631 87938s
 19721  7488 5.0399e+08   14 2731 5.0375e+08 5.0413e+08  0.08%   631 88041s
 19749  7508 5.0394e+08   17 2780 5.0375e+08 5.0413e+08  0.08%   631 88111s
 19784  7515 5.0381e+08   22 2705 5.0375e+08 5.0413e+08  0.08%   631 88191s
 19815  7520 5.0375e+08   24 2692 5.0375e+08 5.0413e+08  0.08%   630 88282s
 19842  7532 infeasible   11      5.0375e+08 5.0413e+08  0.08%   631 88353s
 19865  7529 5.0389e+08   12 3023 5.0375e+08 5.0413e+08  0.08%   631 88738s
 19872  7547 5.0387e+08   13 3082 5.0375e+08 5.0413e+08  0.08%   631 88983s
 19900  7557 5.0381e+08   13 3014 5.0375e+08 5.0413e+08  0.08%   630 89044s
 19933  7564     cutoff   16      5.0375e+08 5.0413e+08  0.08%   630 89132s
 19969  7574 5.0375e+08   19 2911 5.0375e+08 5.0413e+08  0.08%   630 89205s
 20005  7576     cutoff   22      5.0375e+08 5.0413e+08  0.08%   630 89313s
 20035  7588 5.0403e+08   11 2769 5.0375e+08 5.0413e+08  0.08%   630 89401s
 20069  7601 5.0393e+08   16 2742 5.0375e+08 5.0413e+08  0.08%   630 89511s
 20100  7609 5.0383e+08   21 2698 5.0375e+08 5.0413e+08  0.08%   630 89578s
 20132  7620     cutoff   23      5.0375e+08 5.0413e+08  0.08%   630 89666s
 20166  7632 5.0399e+08   12 2714 5.0375e+08 5.0413e+08  0.08%   629 89729s
 20197  7637 5.0386e+08   18 2770 5.0375e+08 5.0413e+08  0.08%   629 89805s
 20230  7645     cutoff   23      5.0375e+08 5.0413e+08  0.08%   629 89883s
 20259  7652 5.0377e+08   23 2665 5.0375e+08 5.0413e+08  0.08%   629 89973s
 20288  7656 5.0388e+08   13 2935 5.0375e+08 5.0413e+08  0.08%   629 90037s
 20318  7652 5.0385e+08   15 2932 5.0375e+08 5.0413e+08  0.08%   628 90142s
 20346  7647     cutoff   20      5.0375e+08 5.0413e+08  0.08%   628 90198s
 20376  7635 5.0376e+08   22 2823 5.0375e+08 5.0413e+08  0.08%   628 90291s
 20402  7631     cutoff    9      5.0375e+08 5.0413e+08  0.08%   628 90369s
 20420  7642 5.0401e+08   10 2786 5.0375e+08 5.0413e+08  0.08%   628 90439s
 20456  7635 5.0389e+08   16 2743 5.0375e+08 5.0413e+08  0.08%   628 90628s
 20463  7632 5.0389e+08   17 2618 5.0375e+08 5.0413e+08  0.08%   628 90752s
 20482  7641 5.0385e+08   18 2606 5.0375e+08 5.0413e+08  0.08%   629 90850s
 20503  7647 5.0379e+08   22 2536 5.0375e+08 5.0413e+08  0.08%   630 90924s
 20534  7641     cutoff   24      5.0375e+08 5.0413e+08  0.08%   630 91014s
 20568  7641 5.0396e+08   14 2683 5.0375e+08 5.0413e+08  0.07%   630 91127s
 20591  7648 5.0386e+08   18 2725 5.0375e+08 5.0413e+08  0.07%   631 91211s
 20620  7647 infeasible   23      5.0375e+08 5.0413e+08  0.07%   631 91316s
 20646  7650     cutoff   23      5.0375e+08 5.0413e+08  0.07%   632 91387s
 20680  7640     cutoff   22      5.0375e+08 5.0413e+08  0.07%   632 91442s
 20715  7627 5.0377e+08   22 2369 5.0375e+08 5.0413e+08  0.07%   633 91534s
 20736  7636 infeasible   12      5.0375e+08 5.0413e+08  0.07%   633 91601s
 20760  7636 infeasible   11      5.0375e+08 5.0413e+08  0.07%   634 91681s
 20792  7632 5.0401e+08   10 2602 5.0375e+08 5.0413e+08  0.07%   634 91755s
 20823  7633 5.0389e+08   16 2538 5.0375e+08 5.0412e+08  0.07%   634 91867s
 20846  7639 5.0385e+08   18 2542 5.0375e+08 5.0412e+08  0.07%   635 91936s
 20872  7637 5.0379e+08   22 2478 5.0375e+08 5.0412e+08  0.07%   635 92037s
 20900  7638     cutoff   24      5.0375e+08 5.0412e+08  0.07%   635 92138s
 20927  7641 5.0392e+08   12 2914 5.0375e+08 5.0412e+08  0.07%   636 92223s
 20953  7630 5.0390e+08   13 2972 5.0375e+08 5.0412e+08  0.07%   636 92317s
 20986  7626     cutoff   16      5.0375e+08 5.0412e+08  0.07%   636 92426s
 21001  7639 5.0381e+08   19 2859 5.0375e+08 5.0412e+08  0.07%   637 92506s
 21027  7636     cutoff   22      5.0375e+08 5.0412e+08  0.07%   637 92602s
 21059  7642 5.0399e+08   12 2559 5.0375e+08 5.0412e+08  0.07%   637 92699s
 21090  7644 5.0393e+08   16 2535 5.0375e+08 5.0412e+08  0.07%   638 92788s
 21124  7636 5.0383e+08   21 2530 5.0375e+08 5.0412e+08  0.07%   638 92890s
 21155  7629     cutoff   23      5.0375e+08 5.0412e+08  0.07%   638 93006s
 21175  7633 5.0403e+08   11 2595 5.0375e+08 5.0412e+08  0.07%   639 93089s
 21199  7636 5.0394e+08   16 2558 5.0375e+08 5.0412e+08  0.07%   639 93203s
 21226  7636 5.0384e+08   21 2565 5.0375e+08 5.0412e+08  0.07%   640 93302s
 21253  7635     cutoff   23      5.0375e+08 5.0412e+08  0.07%   640 93418s
 21281  7637 5.0396e+08   14 2518 5.0375e+08 5.0412e+08  0.07%   640 93526s
 21305  7647 5.0394e+08   16 2580 5.0375e+08 5.0412e+08  0.07%   640 93604s
 21337  7654 5.0385e+08   22 2493 5.0375e+08 5.0412e+08  0.07%   641 93716s
 21363  7659 5.0375e+08   27 2053 5.0375e+08 5.0412e+08  0.07%   641 93829s
 21389  7671 5.0375e+08   30 1929 5.0375e+08 5.0412e+08  0.07%   642 93927s
 21420  7676     cutoff   31      5.0375e+08 5.0412e+08  0.07%   642 94004s
 21453  7663     cutoff   33      5.0375e+08 5.0412e+08  0.07%   642 94108s
 21478  7670 5.0393e+08   12 2870 5.0375e+08 5.0412e+08  0.07%   642 94216s
 21507  7675 5.0381e+08   16 2790 5.0375e+08 5.0412e+08  0.07%   642 94307s
 21541  7685     cutoff   20      5.0375e+08 5.0412e+08  0.07%   642 94423s
 21567  7706 5.0401e+08   12 2590 5.0375e+08 5.0412e+08  0.07%   643 94503s
 21602  7721 5.0392e+08   17 2539 5.0375e+08 5.0412e+08  0.07%   643 94598s
 21633  7727 5.0382e+08   22 2531 5.0375e+08 5.0412e+08  0.07%   643 94676s
 21659  7735 5.0375e+08   24 2518 5.0375e+08 5.0412e+08  0.07%   643 94776s
 21687  7742 5.0402e+08   12 2572 5.0375e+08 5.0412e+08  0.07%   643 94877s
 21712  7759 5.0392e+08   17 2536 5.0375e+08 5.0412e+08  0.07%   643 94977s
 21743  7773 5.0382e+08   22 2531 5.0375e+08 5.0411e+08  0.07%   644 95066s
 21777  7779 5.0376e+08   24 2522 5.0375e+08 5.0411e+08  0.07%   644 95164s
 21803  7786 5.0391e+08   12 2844 5.0375e+08 5.0411e+08  0.07%   644 95275s
 21824  7810 5.0388e+08   14 2843 5.0375e+08 5.0411e+08  0.07%   645 95360s
 21858  7817 5.0379e+08   20 2787 5.0375e+08 5.0411e+08  0.07%   645 95459s
 21887  7834 infeasible   11      5.0375e+08 5.0411e+08  0.07%   645 95532s
 21916  7839 5.0395e+08   15 2565 5.0375e+08 5.0411e+08  0.07%   645 95645s
 21937  7846 5.0383e+08   20 2534 5.0375e+08 5.0411e+08  0.07%   645 95721s
 21958  7859     cutoff   23      5.0375e+08 5.0411e+08  0.07%   645 95794s
 21989  7861 5.0376e+08   20 2542 5.0375e+08 5.0411e+08  0.07%   645 95891s
 22021  7873 5.0380e+08   21 2498 5.0375e+08 5.0411e+08  0.07%   645 95993s
 22050  7885 5.0398e+08   14 2500 5.0375e+08 5.0411e+08  0.07%   645 96110s
 22076  7902 infeasible   17      5.0375e+08 5.0411e+08  0.07%   646 96190s
 22109  7922 5.0385e+08   20 2480 5.0375e+08 5.0411e+08  0.07%   647 96268s
 22145  7939 5.0383e+08   23 2496 5.0375e+08 5.0411e+08  0.07%   647 96338s
 22178  7946 5.0378e+08   25 2554 5.0375e+08 5.0411e+08  0.07%   647 96429s
 22207  7949 5.0376e+08   27 2151 5.0375e+08 5.0411e+08  0.07%   647 96516s
 22234  7959 5.0376e+08   28 2093 5.0375e+08 5.0411e+08  0.07%   647 96618s
 22252  7979 5.0376e+08   31 2018 5.0375e+08 5.0411e+08  0.07%   648 96698s
 22284  7981 5.0376e+08   34 2026 5.0375e+08 5.0411e+08  0.07%   648 97229s
 22294  7992 5.0376e+08   34 2019 5.0375e+08 5.0411e+08  0.07%   648 97510s
 22325  7998 5.0375e+08   37 2045 5.0375e+08 5.0411e+08  0.07%   648 97613s
 22353  8002 5.0376e+08   40 2046 5.0375e+08 5.0411e+08  0.07%   648 97724s
 22379  8016 5.0376e+08   43 2006 5.0375e+08 5.0411e+08  0.07%   648 97807s
 22405  8033     cutoff   46      5.0375e+08 5.0411e+08  0.07%   648 97879s
 22438  8044 5.0375e+08   49 2019 5.0375e+08 5.0411e+08  0.07%   648 97950s
 22473  8051 5.0375e+08   27  337 5.0375e+08 5.0411e+08  0.07%   648 98017s
 22531  8103 5.0375e+08   28  335 5.0375e+08 5.0411e+08  0.07%   647 98064s
 22645  8118 5.0375e+08   49  330 5.0375e+08 5.0411e+08  0.07%   644 98092s
 22771  8148 5.0375e+08   31  358 5.0375e+08 5.0411e+08  0.07%   641 98132s
 22871  8143 5.0375e+08   22  316 5.0375e+08 5.0411e+08  0.07%   640 98161s
 22995  8152     cutoff   29      5.0375e+08 5.0411e+08  0.07%   637 98189s
 23112  8145     cutoff   32      5.0375e+08 5.0411e+08  0.07%   635 98220s
 23236  8158 5.0375e+08   24  380 5.0375e+08 5.0411e+08  0.07%   633 98267s
 23286  8165 5.0375e+08   27  393 5.0375e+08 5.0411e+08  0.07%   632 98309s
 23367  8192 5.0375e+08   33  353 5.0375e+08 5.0411e+08  0.07%   630 98337s
 23490  8241 infeasible   28      5.0375e+08 5.0411e+08  0.07%   628 98368s
 23615  8248     cutoff   25      5.0375e+08 5.0411e+08  0.07%   625 98403s
 23741  8252     cutoff   29      5.0375e+08 5.0411e+08  0.07%   623 98431s
 23841  8283 5.0375e+08   40  355 5.0375e+08 5.0411e+08  0.07%   621 98459s
 23966  8288 5.0375e+08   49  299 5.0375e+08 5.0411e+08  0.07%   619 98492s
 24088  8289 5.0375e+08   25  353 5.0375e+08 5.0411e+08  0.07%   616 98519s
 24209  8271     cutoff   22      5.0375e+08 5.0411e+08  0.07%   614 98546s
 24325  8272 5.0375e+08   24  344 5.0375e+08 5.0411e+08  0.07%   612 98577s
 24431  8283     cutoff   30      5.0375e+08 5.0411e+08  0.07%   610 98613s
 24520  8314     cutoff   33      5.0375e+08 5.0411e+08  0.07%   609 98643s
 24643  8300 5.0375e+08   21  377 5.0375e+08 5.0411e+08  0.07%   607 98697s
 24739  8267 5.0375e+08   22  370 5.0375e+08 5.0411e+08  0.07%   605 98725s
 24837  8257     cutoff   23      5.0375e+08 5.0411e+08  0.07%   604 98757s
 24933  8256 5.0375e+08   22  394 5.0375e+08 5.0411e+08  0.07%   603 98785s
 25032  8282     cutoff   22      5.0375e+08 5.0411e+08  0.07%   602 98816s
 25130  8279     cutoff   27      5.0375e+08 5.0411e+08  0.07%   600 98846s
 25239  8320 5.0375e+08   37  322 5.0375e+08 5.0411e+08  0.07%   598 98881s
 25338  8318 5.0375e+08   55  327 5.0375e+08 5.0411e+08  0.07%   596 98919s
 25441  8352 5.0375e+08   23  370 5.0375e+08 5.0411e+08  0.07%   595 98957s
 25559  8379 5.0375e+08   43  312 5.0375e+08 5.0411e+08  0.07%   592 98995s
H25679  8379                    5.037497e+08 5.0411e+08  0.07%   590 99003s
 25679  8437 5.0375e+08   28  165 5.0375e+08 5.0411e+08  0.07%   590 99036s
 25911  8555 5.0375e+08   29  159 5.0375e+08 5.0411e+08  0.07%   586 99060s
 26151  8630 5.0375e+08   32  131 5.0375e+08 5.0411e+08  0.07%   582 99087s
 26358  8749 5.0375e+08   22  211 5.0375e+08 5.0411e+08  0.07%   578 99129s
 26563  8823 5.0375e+08   18  215 5.0375e+08 5.0411e+08  0.07%   574 99179s
 26739  8943 5.0375e+08   24  179 5.0375e+08 5.0411e+08  0.07%   571 99215s
 26960  9013 5.0375e+08   23  197 5.0375e+08 5.0411e+08  0.07%   568 99246s
 27132  9142 5.0375e+08   35  156 5.0375e+08 5.0411e+08  0.07%   565 99282s
 27356  9229 5.0375e+08   35  161 5.0375e+08 5.0411e+08  0.07%   561 99311s
 27579  9322 5.0375e+08   39  142 5.0375e+08 5.0411e+08  0.07%   558 99391s
 27743  9429 5.0375e+08   24  197 5.0375e+08 5.0411e+08  0.07%   555 99419s
 27976  9532     cutoff   38      5.0375e+08 5.0411e+08  0.07%   551 99466s
 28166  9646 5.0375e+08   23  203 5.0375e+08 5.0411e+08  0.07%   548 99533s
 28365  9711 5.0375e+08   43  187 5.0375e+08 5.0411e+08  0.07%   545 99603s
 28547  9825     cutoff   38      5.0375e+08 5.0411e+08  0.07%   542 99629s
 28787  9876 5.0375e+08   31  192 5.0375e+08 5.0411e+08  0.07%   539 99674s
H28978  9876                    5.037497e+08 5.0411e+08  0.07%   536 99676s
 28978  9872 infeasible   52      5.0375e+08 5.0411e+08  0.07%   536 99793s
 29008  9876     cutoff   55      5.0375e+08 5.0411e+08  0.07%   537 99873s
 29022  9881     cutoff   24      5.0375e+08 5.0411e+08  0.07%   537 99987s
 29039  9884 5.0390e+08   14 2741 5.0375e+08 5.0411e+08  0.07%   537 99999s

Cutting planes:
  Learned: 9
  Implied bound: 1874
  Projected implied bound: 539
  MIR: 15985
  Flow cover: 6945
  Flow path: 2841
  RLT: 13
  Relax-and-lift: 408

Explored 29042 nodes (19980102 simplex iterations) in 100008.90 seconds (129873.67 work units)
Thread count was 6 (of 32 available processors)

Solution count 10: 5.0375e+08 5.0375e+08 5.0375e+08 ... 5.03516e+08

Time limit reached
Best objective 5.037497393071e+08, best bound 5.041067473329e+08, gap 0.0709%

- Status: aborted
  Return code: 0
  Message: Optimization terminated because the time expended exceeded the value specified in the TimeLimit parameter.
  Termination condition: maxTimeLimit
  Termination message: Optimization terminated because the time expended exceeded the value specified in the TimeLimit parameter.
  Wall time: 100009.15799999237
  Error rc: 0


================  OPTIMAL ANNUAL PROFIT  ================
Total profit : 503,749,739 SEK / yr

==================  BREAKDOWN  =================
Revenue (all chargers)             :   708,788,599
Opex - grid purchases              :   141,186,439
Opex - redirection distance        :     3,186,458
Opex - redirection price comp.     :             0
Opex - unmet-demand penalty        :             0
Capex - chargers                   :    20,925,668
Capex - PV & batteries             :    39,740,294
----------------------------------------------------------
Slow   chargers:        233 | energy:   1,420,330.3 | cap ratio: 0.063
Medium chargers:      2,156 | energy:  78,133,887.1 | cap ratio: 0.188
Fast   chargers:        177 | energy:  35,718,993.7 | cap ratio: 0.461
==========================================================

Writing CSV/XLSX outputs...
WARNING: Could not write combined XLSX (This sheet is too large! Your sheet size is: 1102464, 6 Max sheet size is: 1048576, 16384). CSV files were still written.
Output files written to: C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty\results
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
Figure skipped: lbbd_convergence (No LBBD iteration history)
Figure skipped: lbbd_cut_generation (No LBBD iteration history)
Figure skipped: slack (No positive slack)
Figure generated: spatial_maps
Figures written to: C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty\figures
Run finished successfully. Run directory: C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty

Terminal transcript written to: C:\Users\omkarp\Downloads\Opti\runs\2026-07-21_134817_full_with_redirection_withPV_withBESS_slackpenalty\README_RUN.txt
