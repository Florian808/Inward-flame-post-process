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

args = parser.parse_args()

if len(args.sources) != len(args.destinations):
    raise ValueError("Number of paths and destinations must match")

# Internal plotting params
test_mode = False       # Enable testing mode for the script
only_final = False       # Only export the isocontour at the final time
Tiso = 5              # Temperature used for isocountour

# Start parallel compute engine
if not test_mode:
    n_proc = 1
    t_lim = 300 #int(len(args.sources) * 10) + 30
    engine_args = ("-l", "srun", "-la", "--mem-per-cpu=4096", "-np", str(n_proc), "-t", str(t_lim),"-hosts", "localhost")
    OpenComputeEngine("localhost", engine_args)
SuppressMessages(3)

# Image Parameters
res_x = 1000        # Resolution width  
res_y = 1000        # Resolution height

ResizeWindow(1, res_x, res_y)

# Process each pair of source and destination
is_first_db = True
for path, dest in zip(args.sources, args.destinations):
    print(f"[PROCESSING] {path} --> {dest}")

    # Open database
    db_path = path
    OpenDatabase(db_path, 0)

    # Define the expressions needed for further processing
    DefineScalarExpression("radius", "polar_radius(mesh)")
    DefineScalarExpression("x-coord", "coord(mesh)[0]")
    DefineScalarExpression("y-coord", "coord(mesh)[1]")

    # Add Temperature Iso contour of velocity magnitude
    AddPlot("Pseudocolor", "velocity_mag", 0, 0)
    AddOperator("Isosurface", 0)

    # Define the Attributes for plotting
    IsosurfaceAtts = IsosurfaceAttributes()
    IsosurfaceAtts.variable = "temperature"
    IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
    IsosurfaceAtts.contourValue = (Tiso)
    SetOperatorOptions(IsosurfaceAtts, 0, 0)

    DrawPlots()

    # Define the Database export Attributes to export the Isotherm
    dB = ExportDBAttributes()
    dB.db_type = "Xmdv"
    dB.variables = ("x_velocity","y_velocity","temperature", "s1", "s2", "s3", "s4", "s5", "s6", "7", "s8", "s9") # "x-coord","y-coord",
    dB.allTimes= 0
    dB.timeStateFormat= "_%04d"
    dB.dirname = f"{dest}/database"

    # Prepare time series CSV output file
    f = open(f'{dest}/timeseries_meanvel_len.csv', 'w', encoding='utf-8')
    f.write('time, v_mag_mean, total_length\n')

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
        Query("Average Value")
        vel_mag_avg = GetQueryOutputValue()
        Query("Total Length")
        length = GetQueryOutputValue()

        #print(f'{t:.2f}, {vel_mag_avg}, {length}')
        f.write(f'{t:.2f}, {vel_mag_avg}, {length}\n')

        # Export database at that timestep
        dB.filename = f'Isotherm_t_{t:.2f}'
        print('[VISIT] Exporting ', dB.filename)
        ExportDatabase(dB)
    
    f.close()
    DeleteAllPlots()

    # Plot image of final Isotherm
    # Add temperature contour (single color as opposed to slicing)
    AddPlot("Contour", "temperature", 0, 0)
    ResizeWindow(1, res_x, res_y)

    # Set up contour attributes
    ContourAtts = ContourAttributes()
    ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    ContourAtts.legendFlag = 0
    ContourAtts.wireframe = 0
    ContourAtts.lineWidth = 3
    ContourAtts.singleColor = (255, 0, 0, 255)
    ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
    ContourAtts.contourValue = (Tiso)
    ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
    SetPlotOptions(ContourAtts)
    DrawPlots()

    # Set up layout
    Query("SpatialExtents", use_actual_data=1)
    max_coord = max([abs(GetQueryOutputValue()[i]) for i in range(4)])
    l_plot = round(max_coord) + 5
    View2DAtts = View2DAttributes()
    View2DAtts.windowCoords = (-l_plot, l_plot, -l_plot, l_plot)
    y_lims = [0.10, 1.0]
    x_lims = [0.10, 1.0]
    View2DAtts.viewportCoords = (x_lims[0], x_lims[1], y_lims[0], y_lims[1])
    View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 0
    SetView2D(View2DAtts)

    # Set up annotations
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 1
    AnnotationAtts.axes2D.lineWidth = 0
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Inside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.All  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 0
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1.4
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.bold = 0
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 1
    AnnotationAtts.axes2D.xAxis.title.userUnits = 0
    AnnotationAtts.axes2D.xAxis.title.title = "x/d"
    AnnotationAtts.axes2D.xAxis.title.units = "d_L"
    AnnotationAtts.axes2D.xAxis.label.visible = 1
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1.2
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.bold = 0
    AnnotationAtts.axes2D.xAxis.label.font.italic = 0
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.xAxis.grid = 0
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.bold = 1
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 1
    AnnotationAtts.axes2D.yAxis.title.userUnits = 1
    AnnotationAtts.axes2D.yAxis.title.title = "y"
    AnnotationAtts.axes2D.yAxis.title.units = "d_L"
    AnnotationAtts.axes2D.yAxis.label.visible = 1
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1.2
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.bold = 0
    AnnotationAtts.axes2D.yAxis.label.font.italic = 0
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.yAxis.grid = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.legendInfoFlag = 1
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
    SetAnnotationAttributes(AnnotationAtts)

    # Annotation params
    x_off_l = 0.15
    # phi = ...
    phi_match = re.search(r'phi_(\d+\.\d+)', path).group(1)
    if is_first_db: Plot_title1 = CreateAnnotationObject("Text2D")
    Plot_title1.position = (x_off_l, 0.94)
    Plot_title1.height = 0.02
    Plot_title1.useForegroundForTextColor = 1
    Plot_title1.text = f"phi = {phi_match}"
    Plot_title1.fontFamily = Plot_title1.Courier  # Arial, Courier, Times
    Plot_title1.fontBold = 0
    Plot_title1.fontItalic = 0
    Plot_title1.fontShadow = 0

    # U = ... S
    uin_match = re.search(r'Uin_(\d+\.\d+)', path).group(1)
    if is_first_db: Plot_title2 = CreateAnnotationObject("Text2D")
    Plot_title2.position = (x_off_l, 0.89)
    Plot_title2.height = 0.02
    Plot_title2.useForegroundForTextColor = 1
    Plot_title2.text = f"U   = {float(uin_match):.4f} S"
    Plot_title2.fontFamily = Plot_title2.Courier  # Arial, Courier, Times
    Plot_title2.fontBold = 0
    Plot_title2.fontItalic = 0
    Plot_title2.fontShadow = 0

    # in and L subscript
    if is_first_db: Plot_title3 = CreateAnnotationObject("Text2D")
    Plot_title3.position = (x_off_l + 0.0145, 0.89)
    Plot_title3.height = 0.01
    Plot_title3.useForegroundForTextColor = 1
    Plot_title3.text = f"in                        L"
    Plot_title3.fontFamily = Plot_title3.Courier  # Arial, Courier, Times
    Plot_title3.fontBold = 1
    Plot_title3.fontItalic = 0
    Plot_title3.fontShadow = 0

    # y/d
    if is_first_db: Plot_yaxis1 = CreateAnnotationObject("Text2D")
    y_pos_yax = y_lims[0] + 0.5 * (y_lims[1]-y_lims[0]) - 0.015
    Plot_yaxis1.position = (0.01, y_pos_yax)
    Plot_yaxis1.height = 0.02
    Plot_yaxis1.useForegroundForTextColor = 1
    Plot_yaxis1.text = f"y/d"
    Plot_yaxis1.fontFamily = Plot_yaxis1.Courier  # Arial, Courier, Times
    Plot_yaxis1.fontBold = 0
    Plot_yaxis1.fontItalic = 1
    Plot_yaxis1.fontShadow = 0

    # f subscript
    if is_first_db: Plot_yaxis2 = CreateAnnotationObject("Text2D")
    Plot_yaxis2.position = (0.057, y_pos_yax)
    Plot_yaxis2.height = 0.01
    Plot_yaxis2.useForegroundForTextColor = 1
    Plot_yaxis2.text = f"f"
    Plot_yaxis2.fontFamily = Plot_yaxis2.Courier  # Arial, Courier, Times
    Plot_yaxis2.fontBold = 1
    Plot_yaxis2.fontItalic = 0
    Plot_yaxis2.fontShadow = 0

    # x/d
    if is_first_db: Plot_xaxis1 = CreateAnnotationObject("Text2D")
    x_pos_xax = x_lims[0] + 0.5 * (x_lims[1]-x_lims[0]) - 0.025
    Plot_xaxis1.position = (x_pos_xax, 0.03)
    Plot_xaxis1.height = 0.02
    Plot_xaxis1.useForegroundForTextColor = 1
    Plot_xaxis1.text = f"x/d"
    Plot_xaxis1.fontFamily = Plot_xaxis1.Courier  # Arial, Courier, Times
    Plot_xaxis1.fontBold = 0
    Plot_xaxis1.fontItalic = 1
    Plot_xaxis1.fontShadow = 0

    # f subscript
    if is_first_db: Plot_xaxis2 = CreateAnnotationObject("Text2D")
    Plot_xaxis2.position = (x_pos_xax + 0.047, 0.03)
    Plot_xaxis2.height = 0.01
    Plot_xaxis2.useForegroundForTextColor = 1
    Plot_xaxis2.text = f"f"
    Plot_xaxis2.fontFamily = Plot_xaxis2.Courier  # Arial, Courier, Times
    Plot_xaxis2.fontBold = 1
    Plot_xaxis2.fontItalic = 0
    Plot_xaxis2.fontShadow = 0

    DrawPlots()

    # Writing image and tracking file entry
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.family = 0
    SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
    SaveWindowAtts.width = res_x
    SaveWindowAtts.height = res_y
    SaveWindowAtts.screenCapture = 0
    SaveWindowAtts.saveTiled = 0
    #SaveWindowAtts.quality = 80
    #SaveWindowAtts.progressive = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
    SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
    SaveWindowAtts.pixelData = 1 # RGB
    SaveWindowAtts.opts.types = ()
    SaveWindowAtts.opts.help = ""
    if test_mode:
        SaveWindowAtts.outputDirectory ="."
        SaveWindowAtts.fileName = "placeholder"
    else:
        SaveWindowAtts.outputDirectory = f"{dest}/images_CON"
        filename = f"T{Tiso}_Isocon_t_final"
        SaveWindowAtts.fileName = filename
        print(f"[VISIT] Saving {filename}.png")        
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

    DeleteAllPlots()
    CloseDatabase(db_path)
    is_first_db = False

Close()



