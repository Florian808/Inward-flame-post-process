import argparse
import pandas as pd
import os
import shutil
import re
import glob
import subprocess

# Some General Parameters
test_mode = False
dt = 5.0e-04
l_time_lim = 72


def get_restart_params(start, u_in, case, df):
    # Getting restart parameters
    print(f"[INFO] Looking for restart files")
    res_u_in, res_run_num = start.split("_")
    res_case_dir = f"/cluster/scratch/fkaufmann/{case}/Uin_{res_u_in}/RUN{res_run_num}"
    out_files = glob.glob(f"{res_case_dir}/slurm-*.out")
    if not out_files:
        print("[INFO] Restart case has not run yet, looking in this Joblist...")
        for j in range(len(df)):
            if df.iloc[j,0] == case and df.iloc[j,1] == res_u_in and df.iloc[j,2] == res_run_num:
                print("[INFO] Found restart in Joblist, job needs to be appended")
                res_time = df.iloc[j, 4]
                res_dir = f"{res_case_dir}/{final_checkpoints[j]}"
                if u_in != res_u_in:
                    res_time = "0.0"
                return res_dir, res_time
    # Parsing start time from output file
    else:
        # Searching for .out file
        if len(out_files) > 1:
            print("[WARNING] multiple slurm output files detected, choosing most recent file")
            latest_file = max(out_files, key=os.path.getmtime)
        else:
            latest_file = out_files[0]
        # Searching for time and filenames of checkpoints in the last byte_off bytes
        with open(latest_file, 'rb') as f:
            byte_off = -10000000
            f.seek(byte_off, os.SEEK_END)
            f_tail = str(f.readlines())
            time_matches = re.findall(r"([\d.Ee+-]+)\s+Write checkpoint", f_tail)
            file_matches = re.findall(r"FILE:(\S+)", f_tail)

        if time_matches and file_matches:
            if glob.glob(f"{res_case_dir}/{file_matches[-1]}"):
                res_time = time_matches[-1]
                if u_in != res_u_in:
                    res_time = "0.0"
                print(f"[INFO] Using restart file : {file_matches[-1]} at time:{res_time}")
                return f"{res_case_dir}/{file_matches[-1]}", res_time
            else:
                raise Exception("Restart file not found")
        else: 
            raise Exception("No restart parameter found in .out file. seek() offset may need to be increase")

parser = argparse.ArgumentParser(description="Process a list of velocity/run cases.")
parser.add_argument("--path", type=str, required=True,
                    help="path to csv of jobs to submit")
parser.add_argument("--override", type=bool, required=False,
                    help="should already existing folders be overriden", default=False)

args = parser.parse_args()
csv_path = args.path
dst_override = args.override

df = pd.read_csv(csv_path, dtype=str, skipinitialspace=True)
final_checkpoints = [None] * len(df)

for i in range(len(df)):
    # Read case params from csv
    case = df.iloc[i,0]
    u_in = df.iloc[i,1]
    run_num = df.iloc[i,2]
    if df.iloc[i,3]== "None" or df.iloc[i,3] == "":
        IC = "None"
        re_start = "None"
    elif "circ" in df.iloc[i,3]:
        IC, start_r = df.iloc[i,3].split("_")
        re_start = "None"
    else:
        IC = "None"
        re_start = df.iloc[i,3]
    t_end = df.iloc[i,4]
    t_write = df.iloc[i,5]
    n_cores = df.iloc[i,6]
    args = df.iloc[i,7]

    # create directories
    case_dir = f"/cluster/scratch/fkaufmann/{case}/Uin_{u_in}"
    print("[INFO] Creating directories...")
    os.makedirs(case_dir, exist_ok=True)
    
    # copy casefiles to scratch
    src_dir = f"/cluster/home/fkaufmann/inward_prop/casefiles/{case}"
    dst_dir = f"{case_dir}/RUN{run_num}"
    if os.path.exists(dst_dir):
        if dst_override:
            shutil.rmtree(dst_dir)  # Remove the existing folder and its contents
            shutil.copytree(src_dir, dst_dir)
            print(f"[INFO] Destination '{dst_dir}' overwritten.")
        else:
            print(f"[WARNING] Destination '{dst_dir}' already contains files. Skipping case.")
            continue
    else:
        shutil.copytree(src_dir, dst_dir)
        print("[INFO] Copying casefiles...") 

    # Edit .par file
    print(f"[INFO] Writing .par file:")
    with open(f"{dst_dir}/inward.par", "r") as file:
        lines = file.readlines()
    
    new_lines = []
    for line in lines:
        stripped = line.strip()

        # Replace the startFrom line (commented or not)
        if stripped.startswith("#startFrom") or stripped.startswith("startFrom"):
            if re_start == "None":
                print("[INFO] Not using restart files")
                line = "#startFrom = <path>/inward0.f00200 time=0.0\n"
                start_time = 0.0
            else:
                start_path, start_time = get_restart_params(re_start, u_in, case, df)
                line = f"startFrom = {start_path} time={float(start_time):.4f}\n"
         
        # Update number of steps
        if "numSteps" in line:
            match = re.match(r"(numSteps\s*=\s*)(\d+)", line)
            if match:
                t_sim = float(t_end) - float(start_time)
                if t_sim < 0.0:
                    print("[ERROR] Final time is smaller than restart time. Skipping case")
                    continue
                n_steps = int(t_sim / dt)
                line = f"numSteps = {n_steps}\n"
                n_fin_check = int(n_steps * dt / float(t_write))
                final_checkpoints[i] = f"inward0.f{n_fin_check:05d}"
        # Sanity check: dt is same as defined in this file
        if "dt" in line:
            match = re.match(r"dt\s*=\s*([\d.+-eE]+)?", line)
            if match:
                dt_file = match.group(1)
                if float(dt_file) != dt:
                    print("[WARNING] dt in .par does not match defined dt")

        # Update write interval
        if "writeInterval" in line:
            line = f"writeInterval = {t_write}\n"

        # Update initia radius 
        if "userParam01" in line and IC == "circ":
            match = re.match(r"(userParam01\s*=\s*)(\d+\.\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                new_val = start_r  
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
                print(f"[INFO] IC is circle with r={start_r}")

        # Update userParam02 value but keep the inline comment
        if "userParam02" in line:
            match = re.match(r"(userParam02\s*=\s*)(\d+\.\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                new_val = u_in  
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
        
        new_lines.append(line)
    with open(f"{dst_dir}/inward.par", "w") as file:
        file.writelines(new_lines)
    
    print("[INFO] Writing .par file done")
    if int(n_cores) != 256:
        # TODO rewrite SIZE and recompilation
        # May not be necessary as case maybe already compiled with higher core count
        # If implemented add check to prevent unnecessary recompiles
        print("[INFO] Using more than 256 cores")
    if "l" in args:
        with open(f"{dst_dir}/launch.sh", "r") as g:
            new_lines = []
            for lines in g.readlines():
                if "time" in lines:
                    lines = f"#SBATCH --time={l_time_lim}:00:00\n"
                new_lines.append(lines)
        with open(f"{dst_dir}/launch.sh", "w") as g:
            g.writelines(new_lines)

    cmd = ["sbatch", "-J", f"Uin{u_in.replace(".","")}{int(run_num)}", "launch.sh"]
    work_dir = dst_dir
    
    if not test_mode:
        print(f"[INFO] Submitting SLURM job" )
        subprocess.Popen(cmd, cwd=work_dir)
    else:
        print(f"TESTMODE; Command is {cmd}")
    



    