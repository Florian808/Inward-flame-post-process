"""
Script to export some properties of the Temperature Isocontour at Tiso over time:
        - Mean Temperature over Contour
        - Total Contour Length
        - Database of Location, Velocity, Temperature and Scalars at points on Countour
        - Image of the Isocontour at the end time

Input:  - List of directories of databases 
          e.g. /cluster/scratch/fkaufmann/base_18.4k_phi_0.6/Uin_02.00/RUN05/inward.nek5000
        - List of directories of corresponding output file destinations
          e.g. /cluster/home/fkaufmann/inward_prop/post_processed_data/base_18.4k_phi_0.6/Uin_02.00_RUN05/database/
        These two lists must have the same length

Usage:  visit [-cli -nowin] -s extract_Iso avgs --sources >list of sources> --destinations <list of destinations> 
        There are some additional mode/plotting parameters that are set directly in the script (Tiso, test_mode, only_final)
"""

import argparse
import re

# Parse source and destination directories
parser = argparse.ArgumentParser(description="Process sources with destinations")
parser.add_argument("--sources", nargs="+", required=True, help="Input database paths")
parser.add_argument("--destinations", nargs="+", required=True, help="Output directories")
parser.add_argument("--fields", nargs="+", required=True, help="Fields to extract")

args = parser.parse_args()

if len(args.sources) != len(args.destinations):
    raise ValueError("Number of paths and destinations must match")

# Internal plotting params
test_mode = False       # Enable testing mode for the script
only_final = True       # Only export the isocontour at the final time
field = args.fields[0]
r_crop = 20
#iso = 3              # Temperature used for isocountour

# Start parallel compute engine
if not test_mode:
    n_proc = 8
    t_lim = 300 #int(len(args.sources) * 10) + 30
    engine_args = ("-l", "srun", "-la", "--mem-per-cpu=4096", "-np", str(n_proc), "-t", str(t_lim),"-hosts", "localhost")
    OpenComputeEngine("localhost", engine_args)
SuppressMessages(3)

# # Image Parameters
# res_x = 1000        # Resolution width  
# res_y = 1000        # Resolution height

# ResizeWindow(1, res_x, res_y)

# Process each pair of source and destination
is_first_db = True
for path, dest in zip(args.sources, args.destinations):
    print(f"[PROCESSING] {path} --> {dest}")

    # Open database
    db_path = path
    OpenDatabase(db_path, 0)

    # Define the expressions needed for further processing
    # DefineScalarExpression("radius", "polar_radius(mesh)")
    # DefineScalarExpression("x-coord", "coord(mesh)[0]")
    # DefineScalarExpression("y-coord", "coord(mesh)[1]")

    # Add Pseudocolor plot for selected field and crop it to set radius
    AddPlot("Pseudocolor", field, 0, 0)
    AddOperator("Cylinder", 1)
    CylinderAtts = CylinderAttributes()
    CylinderAtts.point1 = (0, 0, -1)
    CylinderAtts.point2 = (0, 0, 1)
    CylinderAtts.radius = r_crop
    CylinderAtts.inverse = 0
    SetOperatorOptions(CylinderAtts, 0, 1)
    DrawPlots()

    # Define the Database export Attributes to export the Isotherm
    dB = ExportDBAttributes()
    dB.db_type = "Xmdv"
    dB.variables = ("temperature") # "x-coord","y-coord",
    dB.allTimes= 0
    #dB.timeStateFormat= "_%04d"
    dB.dirname = f"{dest}/database"

    # # Prepare time series CSV output file
    # f = open(f'{dest}/timeseries_T_{Tiso}_meanvel_len.csv', 'w', encoding='utf-8')
    # f.write('time, v_mag_mean, total_length\n')

    # Do time query
    if only_final:
        startSlide = TimeSliderGetNStates() - 1
    else:
        startSlide = 0

    tstep = 1
    for i in range(startSlide, TimeSliderGetNStates(), tstep):
        SetTimeSliderState(i)

        Query("Time")
        t = GetQueryOutputValue()

        # Export database at that timestep
        dB.filename = f'field_{field}_t_{t:.2f}'
        print('[VISIT] Exporting ', dB.filename)
        ExportDatabase(dB)
    
    #f.close()
    DeleteAllPlots()
    CloseDatabase(db_path)

Close()
