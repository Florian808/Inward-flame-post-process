# import sys
# sys.path.append("/cluster/home/fkaufmann/visit_3.4.2/3.4.2/linux-x86_64/lib/site-packages")
# from visit import *
# Launch()

#  GetEngineList()
# args = ("-l", "mpiexec", "-np", "4", "-hosts", "localhost")

# # Create a launch profile that uses srun
# lp = LaunchProfile()
# lp.profileName = "slurm_srun"
# #lp.host = "localhost"
# lp.parallel = 1
# lp.launchMethod = "srun"
# lp.numProcessors = 4  # or however many you want
# lp.arguments = ["--ntasks=4"]
# lp.timeout = 60

# hplist = GetLaunchProfiles()
# hplist.AddLaunchProfile(lp)
# SetLaunchProfiles(hplist)

# Now open the engine using this profile
args = ("-l", "srun", "-np", "4", "-hosts", "localhost")
OpenComputeEngine("localhost", args)


# Specify and open timeslider:
#args = ()
#print(GetMachineProfileNames())
#GetMachineProfile('euler.ethz.ch')
#args = ("-np", "4", "-hosts", "localhost")
#OpenComputeEngine("localhost", args)
db1="/cluster/scratch/fkaufmann/base_18.4k_phi_0.6/Uin_01.50/RUN02/inward.nek5000"
OpenDatabase(db1, 0)

#  hrr,       s10 Heat release rate
#  curvature, s11 Curvature 
#  stretch,   s12 flame stretch rate 
#  sd,        s13 density weighted disp. speed
#  strain,    s15 strain rate 
#  vort,      s16 vorticity
#  l2,        s17 lambda2
#  hFlux,     s18 heat flux



#Lref = bore       # mm
#Uref = 3.75223e3  # max piston vel. at 800rpm [mm/s]   --> from .par file
#Uref = 3.75222913483e3    # max piston vel. at 800rpm [mm/s] 
#dtOut= 9.0897044574E-03   # Uref/(6*rpm*Lref) dumping inteval for 1 CAD
                          # Uref = Up,max, Lref= bore 
#fac=0.65          # mesh resolution factor
#bdryL=0.012       # height of first elm layer at piston [mm]
#nbdL=6            # number of elm layers within the piston BL
#growth=1.8        # geometric growth factor of elm layers close to piston
GetEngineProperties("localhost")
AddPlot("Contour", "temperature", 0, 0)

# Set up the Contour Attributes
ContourAtts = ContourAttributes()
ContourAtts.legendFlag = 1
ContourAtts.lineWidth = 0
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourValue = (3)
SetPlotOptions(ContourAtts)
#Set up the Annotations
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.databaseInfoFlag = 1
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.Full  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.axes2D.xAxis.title.userTitle = 1
AnnotationAtts.axes2D.xAxis.title.title = "x-Coordinate"
AnnotationAtts.axes2D.xAxis.title.userUnits = 1
AnnotationAtts.axes2D.xAxis.title.units = "m/s"
AnnotationAtts.axes2D.yAxis.title.userTitle = 1
AnnotationAtts.axes2D.yAxis.title.title = "y-Coordinate"
AnnotationAtts.axes2D.yAxis.title.userUnits = 1
AnnotationAtts.axes2D.yAxis.title.units = "kg"

SetAnnotationAttributes(AnnotationAtts)


DrawPlots()



# AddPlot("Pseudocolor", "temperature", 1, 0)

# AddOperator("Isosurface", 1)
# Tiso = 5.0
# IsosurfaceAtts = IsosurfaceAttributes()
# IsosurfaceAtts.contourValue = (Tiso)
# IsosurfaceAtts.contourPercent = ()
# IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
# IsosurfaceAtts.minFlag = 0
# IsosurfaceAtts.min = 0
# IsosurfaceAtts.maxFlag = 0
# IsosurfaceAtts.max = 1
# IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
# IsosurfaceAtts.variable = "temperature"
# SetOperatorOptions(IsosurfaceAtts, 0, 1)

# DrawPlots()

# dB = ExportDBAttributes()
# dB.db_type = "Xmdv"
# dB.variables = ("x_velocity","y_velocity","z_velocity","temperature","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15", "s16") 
# dB.dirname= "."
# dB.allTimes= 0
# dB.timeStateFormat= "_%04d"

# startSlide = 0
# for i in range(startSlide, TimeSliderGetNStates(), 5):
# #   TimeSliderNextState()
#     #print("Step number:", i)
#     SetTimeSliderState(i)
#     Query('Time')
#     time = GetQueryOutputValue()
#     #
#     SetQueryFloatFormat("%g")
#     Query("3D surface area")
#     area = GetQueryOutputValue()
#     #
#     #Query("Volume")
#     #volume = GetQueryOutputValue()
#     #
#     print("%.5e %.5e " % (time, area))
#     #print("%.5e %.5e %.5e" % (time, area, volume))
#     #
#     tt=time/dtOut
#     nEnd = "{:.4f}".format(tt+CAD0)
#     dB.filename= "T5.0_"+nEnd+"CAD.dat"
#     print('Exporting ', dB.filename)
#     ExportDatabase(dB)
#     #
#     #DrawPlots()

