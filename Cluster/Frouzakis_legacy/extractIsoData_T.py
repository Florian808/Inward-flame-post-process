# Specify and open timeslider:
db1="po_post.nek5000"
OpenDatabase(db1, 0)

#  hrr,       s10 Heat release rate
#  curvature, s11 Curvature 
#  stretch,   s12 flame stretch rate 
#  sd,        s13 density weighted disp. speed
#  sa,        s14 normal comp. of abs flame prop speed
#  strain,    s15 strain rate 
#  vort,      s16 vorticity
#  l2,        s17 lambda2
#  hFlux,     s18 heat flux

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



AddPlot("Pseudocolor", "temperature", 1, 0)

AddOperator("Isosurface", 1)
Tiso = 5.0
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourValue = (Tiso)
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Value  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "temperature"
SetOperatorOptions(IsosurfaceAtts, 0, 1)

DrawPlots()

dB = ExportDBAttributes()
dB.db_type = "Xmdv"
dB.variables = ("x_velocity","y_velocity","z_velocity","temperature","s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11","s12","s13","s14","s15", "s16") 
dB.dirname= "."
dB.allTimes= 0
dB.timeStateFormat= "_%04d"

startSlide = 0
for i in range(startSlide, TimeSliderGetNStates(), 5):
#   TimeSliderNextState()
    #print("Step number:", i)
    SetTimeSliderState(i)
    Query('Time')
    time = GetQueryOutputValue()
    #
    SetQueryFloatFormat("%g")
    Query("3D surface area")
    area = GetQueryOutputValue()
    #
    #Query("Volume")
    #volume = GetQueryOutputValue()
    #
    print("%.5e %.5e " % (time, area))
    #print("%.5e %.5e %.5e" % (time, area, volume))
    #
    tt=time/dtOut
    nEnd = "{:.4f}".format(tt+CAD0)
    dB.filename= "T5.0_"+nEnd+"CAD.dat"
    print('Exporting ', dB.filename)
    ExportDatabase(dB)
    #
    #DrawPlots()

