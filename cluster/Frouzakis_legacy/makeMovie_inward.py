RestoreSession("YOH_T5.0.session", 0)

DefineScalarExpression("Vmag_dim", "velocity_magnitude*3.75223")
DefineScalarExpression("Temp_dim", "temperature*333.15")

# Set SaveWindow attributes:
#dirname="movie" 
#os.mkdir(dirname)
#dirname="movie/3D"
#os.mkdir(dirname)
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "."
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG #TIFF  
#SaveWindowAtts.width = 1024 #4096
SaveWindowAtts.stereo = 0
SetSaveWindowAttributes(SaveWindowAtts)

for i in range (TimeSliderGetNStates()):
    SetTimeSliderState(i)
    # Save window
    SaveWindowAtts.stereo = 0
    SaveWindowAtts.fileName = "mov%04d" %j
    SetSaveWindowAttributes(SaveWindowAtts)
    SaveWindow()

