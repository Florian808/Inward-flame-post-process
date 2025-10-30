import argparse
import os
import subprocess
import pandas as pd
import shutil
import re
import glob
import time

# Runtime params
delete_vid_img = True
db_temp = "/cluster/scratch/fkaufmann/other/temp"

def parse_case(case_str):
    try:
        velocity, run = case_str.split("_")
        return velocity.strip(), run.strip()
    except ValueError:
        raise argparse.ArgumentTypeError("Cases must be in the format velocity_run")

parser = argparse.ArgumentParser(description="Process a list of velocity/run cases.")
#group = parser.add_mutually_exclusive_group(required=True)
parser.add_argument("--runs", nargs="+", type=parse_case, required=False,
                    help="List of runs as velocity_in,run_number pairs (e.g. 02.00_01 02.75_07)")
parser.add_argument("--path", type=str, required=False,
                   help="Direct path to a single database (e.g. /scratch/fkaufmanann/<path to all.visit>)")
parser.add_argument("--case", type=str, required=False,
                    help="case name value to use for all cases (e.g. base_18.4k_phi_0.6)")
parser.add_argument("--mode", type=str, required=False,
                    help="Mode to run postprocessing (d dryrun; c contour; i images; h heat release; p post-processing)")
parser.add_argument('--all', action='store_true', help='Go through all casefiles on the scratch folder')
parser.add_argument('--new', action='store_true', help='Go through new casefiles on the scratch folder')
args = parser.parse_args()

case_name = args.case
enabled_modes = set(args.mode) if args.mode else set('d')
if args.all:
    proc_all_files = True
else:
    proc_all_files = False
if not any([args.runs, args.case, args.all, args.new]):
    raise ValueError("No folders given to process")
sources = []
destinations = []
#case_params = []
time_offsets = []


# Parse case sources and destinations from arguments 
# Create necessary folder structer in the destiniation for the results
if args.path:
    sources.append(f"/cluster/scratch/fkaufmann/{args.path}")
    #case_params.append([0, 0, 0])
    dest = f"/cluster/home/fkaufmann/inward_prop/post_processed_data/{args.path}"
    destinations.append(dest)
    os.makedirs(dest, exist_ok=True)
    os.makedirs(f"{dest}/database", exist_ok=True)
    os.makedirs(f"{dest}/images", exist_ok=True)

elif args.all or args.new:
    case_pattern = re.compile(r'^[^_]+_[^_]+_[^_]+_[^_]+$')
    vel_pattern  = re.compile(r'^Uin_[0-9]+.[0-9]+$')
    run_pattern  = re.compile(r'^RUN[0-9]+$')
    
    # Go through all case directories, then velocity directories, then runs directories
    for case_dir in os.listdir("/cluster/scratch/fkaufmann/"):
        case_full_dir = f"/cluster/scratch/fkaufmann/{case_dir}"
        if os.path.isdir(case_full_dir) and case_pattern.match(case_dir):
            for vel_dir in os.listdir(case_full_dir):
                vel_full_dir = f"{case_full_dir}/{vel_dir}"
                if os.path.isdir(vel_full_dir) and vel_pattern.match(vel_dir):
                    for run_dir in os.listdir(vel_full_dir):
                        run_full_dir = f"{vel_full_dir}/{run_dir}"
                        if os.path.isdir(run_full_dir) and run_pattern.match(run_dir):
                            if not args.new:
                                db_path = f"{run_full_dir}/inward.nek5000"
                                sources.append(db_path)
                                dest =  f"/cluster/home/fkaufmann/inward_prop/post_processed_data/{case_dir}/{vel_dir}_{run_dir}"
                                destinations.append(dest)
                                os.makedirs(dest, exist_ok=True)
                                os.makedirs(f"{dest}/database", exist_ok=True)
                                os.makedirs(f"{dest}/images", exist_ok=True)
                                os.makedirs(f"{dest}/images_CON", exist_ok=True)
                                #print(run_full_dir)
                                if vel_dir == "Uin_02.75" and run_dir == "RUN04":
                                    time_offsets.append(50.0)
                                else:
                                    time_offsets.append(0.0)
    
else:
    for u_in, run_num in args.runs:
        if 'e' in enabled_modes:
            db_path = f"/cluster/scratch/fkaufmann/{case_name}/Uin_{u_in}/RUN{run_num}/po_inward.nek5000"
        else:
            db_path = f"/cluster/scratch/fkaufmann/{case_name}/Uin_{u_in}/RUN{run_num}/inward.nek5000"
        sources.append(db_path)
        #case_params.append([phi, velocity, run_number])
        dest = f"/cluster/home/fkaufmann/inward_prop/post_processed_data/{case_name}/Uin_{u_in}_RUN{run_num}"
        destinations.append(dest)
        os.makedirs(dest, exist_ok=True)
        os.makedirs(f"{dest}/database", exist_ok=True)
        os.makedirs(f"{dest}/images", exist_ok=True)
        os.makedirs(f"{dest}/images_CON", exist_ok=True)
        vid_path = f"/cluster/home/fkaufmann/inward_prop/post_processed_data/{case_name}/videos"
        if os.path.exists(f"{vid_path}/temp"):
            shutil.rmtree(f"{vid_path}/temp")
        os.makedirs(f"{vid_path}/temp", exist_ok=True)
        if u_in == "02.75" and run_num == "04":
            time_offsets.append(50.0)
        else:
            time_offsets.append(0.0)

        # Add time correction factor for cases that were run with the wrong initial time


 
# Run in dry mode
if 'd' in enabled_modes:
    print(f'[INFO] Testing mode, running the following command:')
    cmd = ["visit", "-cli", "-nowin", "-s", "extract_Iso_avgs.py", "--destinations"] + destinations + ["--sources"] + sources
    print(cmd)
    #exit()

# Output temperature contour properties
if 'c' in enabled_modes:
    print(f"[INFO] Launching extract_Iso_averages...")
    try:
        cmd = ["visit", "-cli", "-nowin", "-s", "extract_Iso_avgs.py", "--destinations"] + destinations + ["--sources"] + sources 
        subprocess.run(cmd, check=True)
        print(f"[INFO] extract_Iso_averages has finished")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}:\n{e.stderr}")

# Output pseudocolor images of Y_OH (can be specified in extract_Images.py)
if 'i' in enabled_modes:
    print(f"[INFO] Extracting Images")
    processes = []
    for source, destination, t_offset in zip(sources, destinations, time_offsets):
        print(f"[INFO] Launching extract_Images process...")
        cmd = ["visit", "-cli", "-nowin", "-s", "extract_Images.py", "--na", "--tfinal", "--destinations"] + [destination] + ["--sources"] + [source] + ["--toffset"] + [str(t_offset)]
        #cmd = ["visit", "-cli", "-nowin", "-s", "extract_Images.py", "--destinations"] + [destination] + ["--sources"] + [source] + ["--toffset"] + [str(t_offset)]
        try:
            processes.append(subprocess.Popen(cmd))
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Command failed with exit code {e.returncode}:\n{e.stderr}")

    for p in processes:
        p.wait()
    print("[INFO] All extract_Images processes finished")

# Create consecutive video of cases
if 'v' in enabled_modes:
    # Go through cases and compare timesteps (they can vary by an integer factor)
    dt_list = []
    dt_max = 0
    mode = "std"
    for destination in destinations:
        df = pd.read_csv(f"{destination}/images_{mode}.csv")
        dt = df.iloc[1, 0] - df.iloc[0, 0]
        dt_list.append(dt)
        if dt > dt_max:
            dt_max = dt
    dt_fac = [int(dt_max / dt_list[i]) for i in range(len(destinations))]
    # Create symbolic links for images in temp folder
    print("[INFO] creating temporary symbolic links")
    k = 0
    for i, destination in enumerate(destinations):
        # Read csv containing the image names
        df = pd.read_csv(f"{destination}/images_{mode}.csv", skipinitialspace=True)
        for j in range(dt_fac[i]-1, len(df), dt_fac[i]):
            dst = f"{vid_path}/temp/frame{k:05d}.png"
            image = f"{df.iloc[j, 1]}.png"
            #print(image)

            os.symlink(f"{destination}/images/{image}", dst)
            k += 1

    # Prepare ffmpeg command
    frame_rate = int(15 / float(dt_max)) / 2 
    # Create Video name and path
    output_video = f"Vid_Uin_{args.runs[0][0].replace('.', '')}_RUN"
    for run in args.runs:
        output_video += "_" + run[1]
    output_video += ".mp4"
    video_path = f"{vid_path}/{output_video}"
    ffmpeg_cmd = [
    "ffmpeg",
    "-y",
    "-framerate", str(frame_rate),
    "-i", str(vid_path) + "/temp/frame%05d.png", 
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    video_path
    ]
    # print(ffmpeg_cmd)
    print("[INFO] Running FFmpeg...")
    subprocess.run(ffmpeg_cmd)
    print(f"[INFO] Video saved to {video_path}")
    # delete images to save space
    if delete_vid_img:
        print("[INFO] Deleting images used for video")
        for destination in destinations:
            shutil.rmtree(f"{destination}/images/")

# Write csv with iHRR
if 'h' in enabled_modes:
    for source, destination, t_offset in zip(sources, destinations, time_offsets):
        source_parent = os.path.dirname(source)
        print(f"[INFO] Extracting iHRR for {source_parent}")
        hrr_sources  = glob.glob(f"{source_parent}/slurm*")
        if len(hrr_sources) > 1:
            print(f"[WARNING] several slurm.out files found in {source_parent}, picking first one")
        if hrr_sources == []:
            print(f"[WARNING] No .out file found, skipping case")
            continue
        hrr_source = hrr_sources[0]
        hrr_destination = f"{destination}/iHRR.csv"
        data = []
        try:
            with open(hrr_source, 'r') as f:
                for line in f:
                    if 'hrr' in line:
                        data.append(line)
        except Exception as e:
            print(f"Error reading {hrr_source}: {e}")
        
        timeseries = []
        # Write to CSV (skip the first match)
        for line in data[1:]:  # Skip first matching line
            fields = line.strip().split()
            if len(fields) >= 6:
                timeseries.append([float(fields[5]) + t_offset, fields[4]])  # 6th and 5th fields (reversed)

        # Convert to DataFrame and write to CSV
        print("[INFO] Saving .csv")
        df = pd.DataFrame(timeseries, columns=["time", "ihrr"])  
        df.to_csv(hrr_destination, index=False)
            
if 'f' in enabled_modes:
    print(f"[INFO] Launching extract_fields...")
    temp_destinations = []
    for u_in, run_num in args.runs:
        temp_dest = f"{db_temp}/{u_in}_{run_num}"
        os.makedirs(f"{temp_dest}", exist_ok=True)
        os.makedirs(f"{temp_dest}/database", exist_ok=True)
        temp_destinations.append(temp_dest)
    
    try:
        cmd = ["visit", "-cli", "-nowin", "-s", "extract_fields.py", "--destinations"] + temp_destinations + ["--sources"] + sources + ["--fields", "temperature"] 
        subprocess.run(cmd, check=True)
        print(f"[INFO] extract_Iso_averages has finished")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}:\n{e.stderr}")

    #for temp_dest in temp_destinations:
        
if 'p' in enabled_modes:
    for u_in, run_num in args.runs:
        run_filepath = f"/cluster/scratch/fkaufmann/{case_name}/Uin_{u_in}/RUN{run_num}"
        ckp_file_list =  glob.glob(f"{run_filepath}/inward0.f*")
        ckp_file_list.sort()
        work_dir = f"/cluster/home/fkaufmann/inward_prop/casefiles/{case_name}_po"
        file_list_path = f"{work_dir}/file.list"
        if not ckp_file_list:
            print(f"[ERROR] no files found to post-process for {u_in}_{run_num}")
            continue
        else:
            with open(file_list_path, 'w') as file:
                file.write(f"{len(ckp_file_list)}\n")
                file.writelines(f"{fname}\n" for fname in ckp_file_list)
        cmd = ["sbatch", "-J", f"PP{u_in.replace('.','')}{int(run_num)}", "launch.sh"]
        
    
        if 'd' in enabled_modes:
            print(f'[INFO] Testing mode, running the following command:')
            print(cmd)
        else:
            print(f"[INFO] Submitting SLURM job" )
            subprocess.Popen(cmd, cwd=work_dir)
        while(True):
            po_file_list = glob.glob(f"{work_dir}/po_inward0.f[0-9][0-9][0-9][0-9][0-9]")
            print(f"[INFO] {len(po_file_list)} out of {len(ckp_file_list)} files processed")
            if len(po_file_list) == len(ckp_file_list):
                print(f"[INFO] processing finished, moving files...")
                cmd = ['mv', *po_file_list, f"{run_filepath}/"]
                subprocess.run(cmd, cwd=work_dir)
                cmd = ['mv', 'po_inward.nek5000', f"{run_filepath}/"]
                subprocess.run(cmd, cwd=work_dir)
                break
            time.sleep(5)

if 'e' in enabled_modes:
    print(f"[INFO] Launching extract_Iso_averages...")
    try:
        cmd = ["visit", "-cli", "-nowin", "-s", "extract_Iso_avgs.py", "--destinations"] + destinations + ["--sources"] + sources + ["--po"]
        subprocess.run(cmd, check=True)
        print(f"[INFO] extract_Iso_averages has finished")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with exit code {e.returncode}:\n{e.stderr}")

