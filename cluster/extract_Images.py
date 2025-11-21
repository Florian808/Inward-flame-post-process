import argparse
import re
import sys
import os

parser = argparse.ArgumentParser(description="Process sources with destinations")
parser.add_argument("--sources", type=str, required=True, help="Input database paths")
parser.add_argument("--destinations", type=str, required=True, help="Output directories")
parser.add_argument("--toffset", type=float, required=False, help="Correction time offset for cases with wrong internal timestamps", default=0.0)
parser.add_argument("--cinematic", action='store_true', help="Disable all annotations and output a high-res cinematic video")
parser.add_argument("--tfinal", action='store_true', help="Only save image at t_final without any annotation")
parser.add_argument("--local", action='store_true', help="Disable slurm commands to run script locally")
args = parser.parse_args()

t_offset = args.toffset
test_mode = False
# Start parallel compute engine
if not any([test_mode, args.tfinal, args.local]):
    engine_args = ("-l", "srun", "-np", "4", "-hosts", "localhost")
    OpenComputeEngine("localhost", engine_args)
SuppressMessages(3)

# Image Parameters
scalar = "s6"       # OH
res_x = 1920        # Resolution width  
res_y = 1080        # Resolution height
fullscreen = False  # Render image in fullscreen
Tiso = 5            # Isotherm temp for spatial extend 

if args.cinematic:
    res_x = 1920
    res_y = 1080
    fullscreen = True

elif args.tfinal:
    res_x = 1000
    res_y = 1000
    fullscreen = True
# Process the single pair of source and destination
dest = args.destinations
path = args.sources

# Open Database
db_path = path
OpenDatabase(db_path, 0)

if args.tfinal:
    l_plot = 15
    ResizeWindow(1, res_x, res_y)
else:
    # Plot image of final Isotherm to calculate plotting dimensions
    # Add temperature contour (single color as opposed to slicing)
    AddPlot("Contour", "temperature", 0, 0)
    ResizeWindow(1, res_x, res_y)
    SetTimeSliderState(TimeSliderGetNStates() - 1)
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
    l_plot = round((max_coord + 15) / 5) * 5 + 0.001
    print(l_plot)
    DeleteAllPlots()


# Add plot for specified scalar
AddPlot("Pseudocolor", scalar, 0, 0)

# Define the Attributes for plotting
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, ActualData
PseudocolorAtts.minFlag = 1
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.min = 0
PseudocolorAtts.max = 0.007
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
# PseudocolorAtts.colorTableName = "viridis"
# PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.colorTableName = "Spectral"
PseudocolorAtts.invertColorTable = 1
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
SetPlotOptions(PseudocolorAtts)
# Plot pseudocolor
DrawPlots()

if fullscreen:
    layout = "full"
    # Set up layout
    x_lim_cent = 0.5
    View2DAtts = View2DAttributes()
    View2DAtts.windowCoords = (-l_plot, l_plot, -l_plot, l_plot)
    y_lims = [0.0, 1.0]
    x_lims = [0.0, 1.0]
    View2DAtts.viewportCoords = (x_lims[0], x_lims[1], y_lims[0], y_lims[1])
    View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 0
    SetView2D(View2DAtts)
    
     # Set up annotations
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.legendInfoFlag = 0
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
    SetAnnotationAttributes(AnnotationAtts)

    # Define window saving attributes
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = f"{dest}/images"
    SaveWindowAtts.fileName = "placeholder"
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
    SetSaveWindowAttributes(SaveWindowAtts)
else:
    layout = "std"
    # Set up layout
    x_lim_cent = 0.5
    View2DAtts = View2DAttributes()
    View2DAtts.windowCoords = (-l_plot, l_plot, -l_plot, l_plot)
    y_lims = [0.07, 0.97]
    #x_lims = [0.5 - (0.5 - y_lim) * res_y / res_x for y_lim in y_lims]
    x_lims = [x_lim_cent - (y_lims[1] - y_lims[0]) * res_y / res_x / 2,1]
              #x_lim_cent + (y_lims[1] - y_lims[0]) * res_y / res_x / 2]
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
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 1
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
    x_off_l = 0.02
    # phi = ...
    phi_match = re.search(r'phi_(\d+\.\d+)', path).group(1)
    Plot_title1 = CreateAnnotationObject("Text2D")
    Plot_title1.position = (x_off_l, 0.93)
    Plot_title1.height = 0.02
    Plot_title1.useForegroundForTextColor = 1
    Plot_title1.text = f"phi = {phi_match}"
    Plot_title1.fontFamily = Plot_title1.Courier  # Arial, Courier, Times
    Plot_title1.fontBold = 0
    Plot_title1.fontItalic = 0
    Plot_title1.fontShadow = 0
    # U = ... S
    uin_match = re.search(r'Uin_(\d+\.\d+)', path).group(1)
    Plot_title2 = CreateAnnotationObject("Text2D")
    Plot_title2.position = (x_off_l, 0.88)
    Plot_title2.height = 0.02
    Plot_title2.useForegroundForTextColor = 1
    Plot_title2.text = f"U   = {float(uin_match):.4f} S"
    Plot_title2.fontFamily = Plot_title2.Courier  # Arial, Courier, Times
    Plot_title2.fontBold = 0
    Plot_title2.fontItalic = 0
    Plot_title2.fontShadow = 0
    # in and L subscript
    Plot_title3 = CreateAnnotationObject("Text2D")
    Plot_title3.position = (x_off_l + 0.0075, 0.88)
    Plot_title3.height = 0.01
    Plot_title3.useForegroundForTextColor = 1
    Plot_title3.text = f"in                          L"
    Plot_title3.fontFamily = Plot_title3.Courier  # Arial, Courier, Times
    Plot_title3.fontBold = 1
    Plot_title3.fontItalic = 0
    Plot_title3.fontShadow = 0
    # time
    time = 0.0
    Plot_time = CreateAnnotationObject("Text2D")
    Plot_time.position = (x_off_l, 0.07)
    Plot_time.height = 0.03
    Plot_time.useForegroundForTextColor = 1
    Plot_time.text = f"time = {time}" # Placeholder; is later changed in loop
    Plot_time.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_time.fontBold = 0
    Plot_time.fontItalic = 0
    Plot_time.fontShadow = 0
    # legend
    plotname =  GetPlotList().GetPlots(0).plotName
    Plot_legend = GetAnnotationObject(plotname)
    Plot_legend.active = 0
    Plot_legend.managePosition = 0
    Plot_legend.position = (x_off_l, 0.69)
    Plot_legend.xScale = 0.6
    Plot_legend.yScale = 1.2
    Plot_legend.useForegroundForTextColor = 1
    Plot_legend.numberFormat = "%# -9.2e"
    Plot_legend.fontFamily = Plot_legend.Courier  # Arial, Courier, Times
    Plot_legend.fontBold = 0
    Plot_legend.fontItalic = 0
    Plot_legend.fontShadow = 0
    Plot_legend.fontHeight = 0.04
    Plot_legend.drawLabels = Plot_legend.Values # None, Values, Labels, Both
    Plot_legend.drawTitle = 1
    Plot_legend.useCustomTitle = 1
    Plot_legend.customTitle = " "
    Plot_legend.drawMinMax = 0
    Plot_legend.orientation = Plot_legend.VerticalRight  # VerticalRight, VerticalLeft, HorizontalTop, HorizontalBottom
    Plot_legend.controlTicks = 1
    Plot_legend.drawLabels = Plot_legend.Values # None Values Labels Both
    Plot_legend.numTicks = 5
    Plot_legend.suppliedValues = ()
    # Y 
    Plot_legend2 = CreateAnnotationObject("Text2D")
    Plot_legend2.position = (x_off_l + 0.000, 0.669)
    Plot_legend2.height = 0.03
    Plot_legend2.useForegroundForTextColor = 1
    Plot_legend2.text = f"Y"
    Plot_legend2.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_legend2.fontBold = 0
    Plot_legend2.fontItalic = 0
    Plot_legend2.fontShadow = 0
    # OH subscript
    Plot_legend3 = CreateAnnotationObject("Text2D")
    Plot_legend3.position = (x_off_l + 0.012, 0.670)
    Plot_legend3.height = 0.015
    Plot_legend3.useForegroundForTextColor = 1
    Plot_legend3.text = f"OH"
    Plot_legend3.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_legend3.fontBold = 1
    Plot_legend3.fontItalic = 0
    Plot_legend3.fontShadow = 0
    # f subscript
    Plot_xaxis1 = CreateAnnotationObject("Text2D")
    Plot_xaxis1.position = (x_lim_cent + 0.014, 0.008)
    Plot_xaxis1.height = 0.01
    Plot_xaxis1.useForegroundForTextColor = 1
    Plot_xaxis1.text = f"f"
    Plot_xaxis1.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_xaxis1.fontBold = 1
    Plot_xaxis1.fontItalic = 0
    Plot_xaxis1.fontShadow = 0
    # y/d
    Plot_yaxis1 = CreateAnnotationObject("Text2D")
    y_pos_yax = y_lims[0] + 0.5 * (y_lims[1]-y_lims[0]) - 0.01
    Plot_yaxis1.position = (x_lims[0] - 0.06, y_pos_yax)
    Plot_yaxis1.height = 0.02
    Plot_yaxis1.useForegroundForTextColor = 1
    Plot_yaxis1.text = f"y/d"
    Plot_yaxis1.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_yaxis1.fontBold = 0
    Plot_yaxis1.fontItalic = 1
    Plot_yaxis1.fontShadow = 0

    # f subscript
    Plot_yaxis2 = CreateAnnotationObject("Text2D")
    Plot_yaxis2.position = (x_lims[0] - 0.034, y_pos_yax - 0.001)
    Plot_yaxis2.height = 0.01
    Plot_yaxis2.useForegroundForTextColor = 1
    Plot_yaxis2.text = f"f"
    Plot_yaxis2.fontFamily = Plot_time.Courier  # Arial, Courier, Times
    Plot_yaxis2.fontBold = 1
    Plot_yaxis2.fontItalic = 0
    Plot_yaxis2.fontShadow = 0

    # Define window saving attributes
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 0
    SaveWindowAtts.outputDirectory = f"{dest}/images"
    SaveWindowAtts.fileName = "placeholder"
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
    SetSaveWindowAttributes(SaveWindowAtts)

if test_mode:
    SaveWindowAtts.outputDirectory = f"."
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()
else:   
    # Prepare time CSV output file
    f = open(f'{dest}/images_{layout}.csv', 'w', encoding='utf-8')
    f.write('time, image_name\n')

    # Set time for first frame and define time steps
    if args.tfinal:
        startSlide = TimeSliderGetNStates() - 1
    else:
        startSlide = 0
    tstep = 1

    # Iterate through the times and save the corresponding image
    for i in range(startSlide, TimeSliderGetNStates(), tstep):
        SetTimeSliderState(i)

        # Set time specific parameters
        Query("Time")
        time = GetQueryOutputValue() + t_offset
        if not fullscreen: Plot_time.text = f"time = {time:.2f}"

        # Writing image and tracking file entry
        filename = f"OH_Pcol_{layout}_{i:04d}"
        SaveWindowAtts.fileName = filename
        SetSaveWindowAttributes(SaveWindowAtts)
        SaveWindow()

        print('Exporting ', filename, '.png')
        f.write(f'{time:.2f}, {filename}\n')

    f.close()
DeleteAllPlots()
CloseDatabase(db_path)
CloseComputeEngine("localhost")
Close()
"""
GetAnnotationObjectNames()
GetAnnotationObject()
"""