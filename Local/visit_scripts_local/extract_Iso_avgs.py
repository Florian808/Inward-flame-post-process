import os
username = os.getenv("USERNAME")
import sys
if username == "Florian":
    sys.path.append(r"C:\Program Files\LLNL\VisIt3.4.2\lib\site-packages")
else:
    sys.path.append(r"C:\Users\flori\LLNL\VisIt3.4.2\lib\site-packages")
import visit as vi
#vi.AddArgument("-gui")
vi.Launch() # loads rest of visit functions
print("launched visit \n")
import visit as vi # loads rest of visit functions
print("imported visit \n")

import argparse

parser = argparse.ArgumentParser(description="Process sources with destinations")
parser.add_argument("--sources", nargs="+", required=True, help="Input database paths")
parser.add_argument("--destinations", nargs="+", required=True, help="Output directories")

args = parser.parse_args()

if len(args.sources) != len(args.destinations):
    raise ValueError("Number of paths and destinations must match")

# Process each pair
for path, dest in zip(args.sources, args.destinations):
    print(f"[PROCESSING] {path} --> {dest}")
    db_path = path
    #args = ("-dir", "/cluster/home/fkaufmann/visit_3.4.2", "-assume_format", "PDB", "-debug", "4")
# Open a metadata server before the call to OpenDatabase so we
# can launch it how we want.
    #vi.OpenMDServer("fkaufmann@euler.ethz.ch", args)
    print("test")
    profile = vi.GetMachineProfile("euler.ethz.ch")
    #print(profile)
    vi.OpenComputeEngine(profile)
    vi.OpenDatabase(db_path, 0)
    print("test2")
    
    #engine.open(nprocs = 4, rtime = 60, method = "srun")

    # Define the expressions needed for further processing
    vi.DefineScalarExpression("radius", "polar_radius(mesh)")
    # DefineScalarExpression("x-coord", "coord(mesh)[0]")
    # DefineScalarExpression("y-coord", "coord(mesh)[1]")

    # Add Temperature Iso contour of velocity magnitude
    vi.AddPlot("Pseudocolor", "velocity_mag", 0, 0)
    vi.AddOperator("Isosurface", 0)

    # Define the Attributes for plotting
    Tiso = 3.0
    IsosurfaceAtts = vi.IsosurfaceAttributes()
    IsosurfaceAtts.variable = "temperature"
    IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
    IsosurfaceAtts.contourValue = (Tiso)
    vi.SetOperatorOptions(IsosurfaceAtts, 0, 0)

    vi.DrawPlots()

    # Define the Database export Attributes to export the Isotherm
    dB = vi.ExportDBAttributes()
    dB.db_type = "Xmdv"
    dB.variables = ("x-coord","y-coord","x_velocity","y_velocity","temperature","s1","s2","s3","s4","s5","s6","s7","s8","s9") 
    dB.allTimes= 0
    dB.timeStateFormat= "_%04d"

    # Prepare time series CSV output file
    f = open('timeseries_test.txt', 'w', encoding='utf-8')
    f.write('time, v_mag_mean, total_length\n')

    # Do time query
    startSlide = 0
    tstep = 10
    for i in range(startSlide, vi.TimeSliderGetNStates(), tstep):
        vi.SetTimeSliderState(i)

        vi.Query("Time")
        t = vi.GetQueryOutputValue()

        vi.Query("Average Value")
        vel_mag_avg = vi.GetQueryOutputValue()
        vi.Query("Total Length")
        length = vi.GetQueryOutputValue()

        print(f'{t:.2f}, {vel_mag_avg}, {length}')
        f.write(f'{t:.2f}, {vel_mag_avg}, {length}\n')
    #print("%.5e %.5e %.5e" % (time, area, volume))
    #
    # tt=time/dtOut
    # nEnd = "{:.4f}".format(tt+CAD0)

    f.close()
    # Write the database data
    dB.filename = "Test"
    dB.dirname = f"{dest}/database"
    print('Exporting ', dB.filename)
    vi.ExportDatabase(dB)




