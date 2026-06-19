#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from src_lbbd.lbbd_final_production import run_final_lbbd
else:
    from .lbbd_final_production import run_final_lbbd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the final clean LBBD production formulation for the EV CPO model. "
            "This is the thesis-facing wrapper around the validated PV+BESS LBBD implementation."
        )
    )
    parser.add_argument("--dataset", choices=["small", "full"], default="small")
    parser.add_argument("--scenario", choices=["no_redirection", "with_redirection"], default="with_redirection")
    parser.add_argument("--project-root", default=str(PROJECT_ROOT))
    parser.add_argument("--threads", type=int, default=None)
    parser.add_argument("--time-limit", type=int, default=None)
    parser.add_argument("--preset", choices=["small_validation", "full_trial", "full_production"], default=None)
    parser.add_argument("--master-gap", type=float, default=None)
    parser.add_argument("--subproblem-gap", type=float, default=None)
    parser.add_argument("--lbbd-gap", type=float, default=None)
    parser.add_argument("--max-iterations", type=int, default=None)
    parser.add_argument("--cut-tolerance", type=float, default=1e-5)
    parser.add_argument("--disable-pv", action="store_true", help="Diagnostic only; final thesis workflow normally keeps PV enabled.")
    parser.add_argument("--disable-bess", action="store_true", help="Diagnostic only; final thesis workflow normally keeps BESS enabled.")
    parser.add_argument("--show-master-log", action="store_true", help="Print full Gurobi master logs to console. By default only LBBD iteration summaries are printed live.")
    return parser.parse_args()


def main() -> int:
    return run_final_lbbd(parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
