import sys
sys.path.append(r"C:\Users\flori\LLNL\VisIt3.4.2\lib\site-packages")
import visit as vi
vi.Launch() # loads rest of visit functions
print("launched visit \n")
import visit as vi # loads rest of visit functions
print("imported visit \n")

import argparse
import os
import subprocess

def parse_case(case_str):
    try:
        velocity, run = case_str.split(",")
        return velocity.strip(), run.strip()
    except ValueError:
        raise argparse.ArgumentTypeError("Cases must be in the format velocity,run")

parser = argparse.ArgumentParser(description="Process a list of velocity/run cases.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--cases", nargs="+", type=parse_case, required=False,
                    help="List of cases as velocity_in,run_number pairs (e.g. 02.00,01 02.75,07)")
group.add_argument("--path", type=str,
                   help="Direct path to a single database (e.g. /scratch/fkaufmanann/<path to all.visit>)")
parser.add_argument("--phi", type=float, required=False,
                    help="phi value to use for all cases (0.6 or 0.75)")

args = parser.parse_args()

phi = args.phi
print(f"Using phi = {phi}")
sources = []
destinations = []
case_params = []

if args.path:
    sources.append(f"/cluster/scratch/fkaufmann/{args.path}")
    case_params.append([0, 0, 0])
    dest = args.path + "_results"
    destinations.append(dest)
    os.makedirs(dest, exist_ok=True)
else:
    for velocity, run_number in args.cases:
        db_path = f"/cluster/scratch/fkaufmann/base_18.4k_phi_{phi}/Uin_{velocity}/RUN{run_number}/inward.nek5000"
        sources.append(db_path)
        case_params.append([phi, velocity, run_number])
        dest = f"base_18.4k_phi_{phi}/Uin_{velocity}/RUN{run_number}/"
        destinations.append(f"/cluster/scratch/fkaufmann/{dest}")

 
# Build and run the command

cmd = ["visit", "-cli", "-s extract_Iso_avgs.py", "--destinations"] + destinations + ["--paths"] + sources
#print(f"[INFO] Created {len(destinations)} destination folders")
print(f"[INFO] Launching extract_Iso_averages...")

try:
   subprocess.run(cmd, check=True, capture_output=False, text=True)
   #print(f"[SUCCESS] Command completed:\n{result.stdout.strip()}")
except subprocess.CalledProcessError as e:
   print(f"[ERROR] Command failed with exit code {e.returncode}:\n{e.stderr}")





