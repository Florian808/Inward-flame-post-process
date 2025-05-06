import os
import sys
import math
import numpy as np

# Compute Engine Launcher:
def LaunchComputeEngine():
    #OpenComputeEngine("127.0.0.1", ("-l", "sbatch/srun", "-t", "10", "-np", "4", "-nn", "1", "-b", "dems", "-p", "batch"))
    OpenComputeEngine("127.0.0.1", ('-noloopback', '-forcestatic', '-l', 'sbatch/srun', '-t', '120', '-p', 'batch', '-b', 'dems', '-np', '10', '-nn', '1', '-host', 'jwvis00.juwels'))

# Launch engine and load the Database:
#LaunchComputeEngine()

# Specify and open timeslider:
#db1="po_post.nek5000"
#OpenDatabase(db1, 0)

# instead of launching engine and opening database:
RestoreSession("T5.0.session", 0)

# Engine data
rpm   = 800          # engine speed 
CAD0  = 590.0        # starting CAD 
bore  = 86.0         # bore [mm]
stroke=bore          # stroke [mm]
Lrod  = 148.0        # connecting rod length [mm]
crvh  = 74.4         # crevice height [mm]
Hcl   = 2.6          # clearance height [mm]
cr    = 0.5*stroke   # crank radius

Lref = bore       # mm
#Uref = 3.75223e3  # max piston vel. at 800rpm [mm/s]   --> from .par file
Uref = 3.75222913483e3    # max piston vel. at 800rpm [mm/s] 
dtOut= 9.0897044574E-03   # Uref/(6*rpm*Lref) dumping inteval for 1 CAD
                          # Uref = Up,max, Lref= bore 
fac=0.65          # mesh resolution factor
bdryL=0.012       # height of first elm layer at piston [mm]
nbdL=6            # number of elm layers within the piston BL
growth=1.8        # geometric growth factor of elm layers close to piston

pi = np.pi

# Compute piston position
# -----------------------
#  cubit: 
# {Zpiston = cr*cos(d2r(CAD)) + sqrt( rodlen^2 - cr^2*sin(d2r(CAD))^2 ) - ( rodlen+cr+Hcl) }
#
def Zpiston(CAD): 
   deg2rad = CAD*pi/180.0
   Zp      = cr*np.cos(deg2rad) + np.sqrt(Lrod**2-cr**2*np.sin(deg2rad)**2) - (Lrod+cr+Hcl) 
   return Zp/Lref

def Vpiston(CAD):
   deg2rad = CAD*pi/180.0
   omega   = pi*rpm/30         # rad/s
   v1 = -cr*np.sin(deg2rad) - cr**2*np.sin(deg2rad)*np.cos(deg2rad)/(np.sqrt(Lrod**2 - cr**2*np.sin(deg2rad)**2))  # cm/rad
   vp = omega*v1
   return vp

# find Vp,max  : scipy unavailable with visit on juwelsvis
#import scipy
#x_max = -scipy.optimize.fmin(lambda x: -Vpiston(x), 0)
#Vpmax = Vpiston(x_max)

# Dimensional variables
#Tref=333.15
#value='"temperature*'+str(Tref)+'"'
DefineScalarExpression("Temp_dim", "temperature*333.15")

#AddPlot("Pseudocolor", "temperature", 1, 0)
AddPlot("Pseudocolor", "Temp_dim", 1, 0)
AddOperator("Slice",0)

DrawPlots()


#    Define slice at a distance from the piston
dz   = 0.05    # distance from piston, mm
dznd = dz/Lref  

# Piston position from mesh
zp_mesh = []
for i in range(0, TimeSliderGetNStates()):
#for i in range(0, 5):
    SetTimeSliderState(i)
    Query("SpatialExtents", use_actual_data=1)
    q=GetQueryOutputValue()
    Query('Time')
    t = GetQueryOutputValue()
    cc = CAD0 + t/dtOut
    Zpp = Zpiston(cc)
    print('t= %.8e   CAD= %.8e   Zmin= %.8e  Zp= %.8e  Zp-Zmin= %.8e ' % (t, CAD0+t/dtOut, q[2], Zpp, (Zpp-q[2]), ) )
    zp_mesh.append(q[2])

print('\nzp_mesh:')
print(zp_mesh)

SetActivePlots(0)
DeleteActivePlots()

# Get min/max of x, z to find piston location
Query("SpatialExtents", use_actual_data=1)
q=GetQueryOutputValue()
Zp = q[2]
# 
zz1 = Zp +     dznd
zz2 = Zp + 2.0*dznd
zz3 = Zp + 3.0*dznd
print('Zp = %.5f, zz1= %.5f ' % (Zp, zz1))

SliceAtts = SliceAttributes()
SliceAtts.originType = SliceAtts.Point  # Point, Intercept, Percent, Zone, Node
SliceAtts.originPoint = (0, 0, zz1)
SliceAtts.project2d = 1
SliceAtts.axisType = SliceAtts.ZAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
SliceAtts.interactive = 0
SetOperatorOptions(SliceAtts, 0)

plotName = GetPlotList().GetPlots(0).plotName
legend = GetAnnotationObject(plotName)
legend.numTicks=3
legend.numberFormat = "%# -9.2f"
legend.controlTicks=1
legend.fontHeight=0.02
legend.drawTitle=0
legend.fontHeight=0.02
legend.drawTitle=0
legend.managePosition=0
legend.position=(0.01, 0.90)
legend.drawMinMax = 0

# Set annotation attributes: turn off database, user, axes, bbox
AnnotationAtts = AnnotationAttributes()
AnnotationAtts.axes2D.visible = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.legendInfoFlag = 1
SetAnnotationAttributes(AnnotationAtts)

SetActivePlots(0)
PseudocolorAtts = PseudocolorAttributes()
PseudocolorAtts.colorTableName = "hot_desaturated"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.legendFlag = 1
SetPlotOptions(PseudocolorAtts)

# legend:
l1 = CreateAnnotationObject("Text2D")
l1.position = (0.01, 0.92)
l1.fontBold = 0
l1.textColor = (0, 0, 0, 232)
l1.height=0.02 
l1.text = "T [K]"
l1.fontFamily = 2

View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-0.513752, 0.506957, -0.507662, 0.506276)
View2DAtts.viewportCoords = (0.15, 0.94, 0.05, 0.94)
View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 1
SetView2D(View2DAtts)

DrawPlots()


#
# Create CAD and legend text:
#
cad = CreateAnnotationObject("Text2D")
cad.position = (0.70, 0.92)
cad.fontBold = 1
cad.textColor = (0, 0, 0, 232)
cad.height=0.030
Query('Time')
t = GetQueryOutputValue()
t = t / dtOut
tstext = '%03.2f CAD' % (t+CAD0)
cad.text = tstext

#
# Set SaveWindow attributes:
#
#dirname="movie" 
#os.mkdir(dirname)
#dirname="movie/3D"
#os.mkdir(dirname)
#
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "."
#SaveWindowAtts.outputDirectory = "/home/ggiannak/movie"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG #TIFF  
SaveWindowAtts.width = 1024 #4096
SaveWindowAtts.stereo = 0
SetSaveWindowAttributes(SaveWindowAtts)
#
SaveWindowAtts.fileName = "T_dz"+str(dz)+"_"+str(t+CAD0)
SetSaveWindowAttributes(SaveWindowAtts)

#SaveWindow()

#
# Animate 
#
#
for i in range(0, TimeSliderGetNStates()):
#for i in range(0, 5):
    SetTimeSliderState(i)
    #
    # Set time and CAD: 
    Query("Time")
    t = GetQueryOutputValue()
    t = t / dtOut
    CAD = t+CAD0
    tstext = '%03.2f CAD' % CAD
    cad.text = tstext
    #
    # Get min/max of x, z to find piston location
    #   WRONG SLICE: we're plotting on a z plane
    #Query("SpatialExtents", use_actual_data=1)
    #q=GetQueryOutputValue()
    #print(q)
    #Zpiston = q[5]
    #Zp = Zpiston(CAD)
    #print('At %03d CAD, Zp = %.5f' %(CAD, Zp) )
    # 
    Zp = zp_mesh[i]
    zz1 = Zp +     dznd
    zz2 = Zp + 2.0*dznd
    zz3 = Zp + 3.0*dznd
    print('\n CAD: %3.2f  Data from z= %.6f' % (CAD, zz1) )
    #  Get slice at specified distance from piston 
    SliceAtts = SliceAttributes()
    SliceAtts.originType = SliceAtts.Point  
    SliceAtts.originPoint = (0, 0, zz1)
    SliceAtts.project2d = 1
    SliceAtts.axisType = SliceAtts.ZAxis  
    SliceAtts.interactive = 0
    SetOperatorOptions(SliceAtts, 0)
    # 
    #
    # Determine min/max values and set colormap and legend:
    Query("Population Statistics")
    q=GetQueryOutputValue()
    tmean=q[0]
    tstd=q[1]
    tmin=tmean-tstd
    tmax=tmean+tstd
    PseudocolorAtts=GetPlotOptions()
    PseudocolorAtts.min = tmin
    PseudocolorAtts.max = tmax
    SetPlotOptions(PseudocolorAtts)
    plotName = GetPlotList().GetPlots(0).plotName
    legend = GetAnnotationObject(plotName)
    legend.suppliedValues=(tmin, tmin+0.5*(tmax-tmin), tmax)
    RemoveOperator(1, 0) 
    #
    DrawPlots()
    # Set save options
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 1
    SaveWindowAtts.family = 0
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.fileName = "T_dz"+str(dz)+"_"+str(t+CAD0)
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

