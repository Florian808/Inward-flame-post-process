"""
Script to automatically create working directories, copy relevant casefiles and modify the .par file, using a .csv list of jobs
Finally it will submit a batch job to the Euler cluster.

ATTENTION: This script assumes that NO JOBS ARE RUNNING on the cluster. Problems occur if jobs require checkpoints from currently running jobs.

Inputs:
    -- path: mandatory path to the .csv file specifying jobs
    -- override: boolean, if set to True will override working directory if it already exists, USE WITH CARE as it can override existing simulation files
For example .csv file look at "Job_list_for_sub.csv"

Parameters:
    - test_mode     boolean, specifies if script should actually submit batch Job to cluster
    - dt            float, default timestep, script issues warning if value different from this is used
    - l_time_lim    int, specifies the number of hours allocated to batch job if l flag is set in "extra_args"
"""


import argparse
import pandas as pd
import os
import shutil
import re
import glob
import subprocess

# Some General Parameters
test_mode = False
dt = 2.0e-04
l_time_lim = 72

# Files source and destination settings
euler_usrname = 'fkaufmann'
dst_top_dir = f"/cluster/scratch/{euler_usrname}"                       # Destination where case and subsequent folders containing runs and checkpoints should be saved; usually on scratch
src_top_dir = f"/cluster/home/{euler_usrname}/inward_prop/casefiles"     # Source directory where compiled folders for different cases are located

# Function to find the necessary parameters to restart a job from another checkpoint
# Assumes that no Jobs are currently running
# Returns checkpoint location, restart time and if job needs to be chained (-1 = no)
def get_restart_params(start, u_in, case, df):
    # Getting restart parameters
    print(f"[INFO] Looking for restart files")
    res_u_in, res_run_num = start.split("_")
    res_case_dir = f"{dst_top_dir}/{case}/Uin_{res_u_in}/RUN{res_run_num}"
    # Look for slurm output files
    out_files = glob.glob(f"{res_case_dir}/slurm-*.out")
    # Case 1: the job required for this simulation has not run yet, so 
    if not out_files:
        print("[INFO] No output file found, looking in this Joblist...")
        for j in range(len(df)):
            if df['case'].iloc[j] == case and df['velocity'].iloc[j] == res_u_in and df['run_number'].iloc[j] == res_run_num:
                print("[INFO] Found restart in Joblist, job needs to be appended")
                res_time = df.iloc[j, 4]
                res_dir = f"{res_case_dir}/{final_checkpoints[j]}"
                if u_in != res_u_in:
                    res_time = "0.0"
                return res_dir, res_time, j
        raise Exception("No matching slurm output file or entry in this joblist found. Job restart checkpoint cannot be defined")
    # Case 2: output file has been found. Parse restart time and checkpoint location from .out file
    else:
        # Check if .out file is unique
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
                return f"{res_case_dir}/{file_matches[-1]}", res_time, -1
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
job_ids = [None] * len(df)

for i in range(len(df)):
    print(f"[INFO] Working on entry {i}")
    # Read case params from csv
    case = df['case'].iloc[i]
    u_in = df['velocity'].iloc[i]
    run_num = df['run_number'].iloc[i]
    start_from = df['startfrom'].iloc[i]
    if start_from == "None" or start_from == "":
        IC = "None"
        re_start = "None"
    elif "circ" in start_from:
        IC, start_r = start_from.split("_")
        re_start = "None"
    elif "PC" in start_from:
        IC, start_r, amp_pert, m_start_pert, m_end_pert = start_from.split("_")
        re_start = "None"
    else:
        IC = "None"
        re_start = start_from
    t_end = df['t_end'].iloc[i]
    t_write = df['write_interval'].iloc[i]
    n_cores = df['no_cores'].iloc[i]
    args = df['extra_args'].iloc[i]

    # create directories
    case_dir = f"{dst_top_dir}/{case}/Uin_{u_in}"
    print("[INFO] Creating directories...")
    os.makedirs(case_dir, exist_ok=True)
    
    # copy casefiles to scratch
    src_dir = f"{src_top_dir}/{case}"
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
    job_dep_idx = -1

    for line in lines:
        stripped = line.strip()

        # Replace the startFrom line
        if stripped.startswith("#startFrom") or stripped.startswith("startFrom"):
            if re_start == "None":
                print("[INFO] Not using restart files")
                line = "#startFrom = <path>/inward0.f00200 time=0.0\n"
                start_time = 0.0
            else:
                start_path, start_time, job_dep_idx = get_restart_params(re_start, u_in, case, df)
                line = f"startFrom = {start_path} time={float(start_time):.4f}\n"
         
        # Update number of simulation steps
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

        # Update initial radius (userParam01) value but keep the inline comment
        if "userParam01" in line and (IC == "circ" or IC =="PC"):
            match = re.match(r"(userParam01\s*=\s*)(\d+\.\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                new_val = start_r  
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
                print(f"[INFO] IC is circle with r = {start_r}")

        # Update inlet velocity (userParam02) value but keep the inline comment
        if "userParam02" in line:
            match = re.match(r"(userParam02\s*=\s*)(\d+\.\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                new_val = u_in  
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"

        # Update perturbation amplitude (userParam04) value but keep the inline comment
        if "userParam04" in line:
            match = re.match(r"(userParam04\s*=\s*)([\d.+-eE]+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                if IC == "PC":
                    new_val = amp_pert
                else:
                    new_val = 0.0
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
        
        # Update starting mode for polychromatic perturbation (userParam05) but keep the inline comment
        if "userParam05" in line:
            match = re.match(r"(userParam05\s*=\s*)(\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                if IC == "PC":
                    new_val = int(m_start_pert)
                else:
                    new_val = 1
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
        
        # Update final mode for polychromatic perturbation (userParam06) but keep the inline comment
        if "userParam06" in line:
            match = re.match(r"(userParam06\s*=\s*)(\d+)(\s*!.*)?", line)
            if match:
                prefix, old_val, comment = match.groups()
                if IC == "PC":
                    new_val = int(m_end_pert)
                    print(f"[INFO] IC is perturbed: A = {amp_pert}; ns = {int(m_start_pert)}; ne = {int(m_end_pert)}")
                else:
                    new_val = 1
                comment = comment or ""
                line = f"{prefix}{new_val}{comment}\n"
                
        
        new_lines.append(line)
    # Write new .par file with updated parameters
    with open(f"{dst_dir}/inward.par", "w") as file:
        file.writelines(new_lines)
    print("[INFO] Writing .par file done")

    # Check if default no. of compute cores are used
    if int(n_cores) != 256:
        # TODO rewrite SIZE and recompilation
        # May not be necessary as case maybe already compiled with higher core count
        # If implemented add check to prevent unnecessary recompiles
        print(f"[INFO] Using more than 256 cores (n = {n_cores})")

    # Change launch.sh file if Job should run for an extended time (>24h) defined at beginning of this script
    if "l" in args:
        with open(f"{dst_dir}/launch.sh", "r") as g:
            new_lines = []
            for lines in g.readlines():
                if "time" in lines:
                    lines = f"#SBATCH --time={l_time_lim}:00:00\n"
                new_lines.append(lines)
        with open(f"{dst_dir}/launch.sh", "w") as g:
            g.writelines(new_lines)

    # Prepare command for batch job submission on the cluster
    if job_dep_idx < 0:
        cmd = ["sbatch", "-J", f"Uin{u_in.replace('.','')}{int(run_num)}", "launch.sh"]
    else:
        job_dep_id = job_ids[job_dep_idx]
        cmd = ["sbatch", "-J", f"Uin{u_in.replace('.','')}{int(run_num)}", "--dependency", f"afterok:{job_dep_id}", "launch.sh"]
        print(f"[INFO] Job will be chained to job {job_dep_id}")
    work_dir = dst_dir

    # Submit Job to queueing system
    if not test_mode:
        print(f"[INFO] Submitting SLURM job" )
        result = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True)
        match = re.search(r"Submitted batch job (\d+)", result.stdout)
        if match:
            job_id = match.group(1)
            job_ids[i] = job_id
            print(f"[INFO] Job {i} submitted with JobID {job_id}")
            print("----------------------------------------------------------")
        else:
            print(f"[WARNING] Could not parse JobID from sbatch output:\n{result.stdout}")
    else:
        print(f"TESTMODE; Command is {cmd}")
        job_ids[i] = '00000'
    



    