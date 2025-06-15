# Visit 3.4.2 log file
ScriptVersion = "3.4.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
ShowAllWindows()
launchArguments = ("-l", "srun", "-la", "--mem-per-cpu=4096", "-np", "1", "-t", "300", "-hosts", "localhost")
OpenComputeEngine("localhost", launchArguments)
ResizeWindow(1, 1000, 1000)
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.25/RUN01/inward.nek5000", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
AddPlot("Pseudocolor", "velocity_mag", 1, 1)
AddOperator("Isosurface", 1)
SetActivePlots(0)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 10
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 0, 1)
SetActivePlots(0)
DrawPlots()
SetTimeSliderState(0)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(1)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(2)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(3)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(4)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(5)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(6)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(7)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(8)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(9)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(10)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(11)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(12)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(13)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(14)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(15)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(16)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(17)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(18)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(19)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(20)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(21)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(22)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(23)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(24)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(25)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(26)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(27)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(28)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(29)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(30)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(31)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(32)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(33)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(34)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(35)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(36)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(37)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(38)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(39)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(40)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(41)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(42)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(43)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(44)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(45)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(46)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(47)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(48)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(49)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(50)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(51)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(52)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(53)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(54)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(55)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(56)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(57)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(58)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(59)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(60)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(61)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(62)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(63)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(64)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(65)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(66)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(67)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(68)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(69)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(70)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(71)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(72)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(73)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(74)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(75)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(76)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(77)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(78)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(79)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(80)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(81)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(82)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(83)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(84)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(85)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(86)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(87)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(88)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(89)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(90)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(91)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(92)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(93)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(94)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(95)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(96)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(97)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(98)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(99)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetActivePlots(0)
DeleteActivePlots()
AddPlot("Contour", "temperature", 1, 1)
ResizeWindow(1, 1000, 1000)
ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.SetNumControlPoints(30)
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.NONE  # NONE, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.tagNames = ("Default", "Discrete")
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (3)
ContourAtts.contourPercent = ()
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()
Query("SpatialExtents", use_actual_data=1)
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-11, 11, -11, 11)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
# End spontaneous state

View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-11, 11, -11, 11)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
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
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 0
AnnotationAtts.axes2D.yAxis.label.font.italic = 0
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
DrawPlots()
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/cluster/home/fkaufmann/inward_prop/post_processed_data/shapeIC_18.4k_phi_0.6/Uin_02.25_RUN01/images_CON"
SaveWindowAtts.fileName = "T3_Isocon_t_final"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.width = 1000
SaveWindowAtts.height = 1000
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.pixelData = 1
SaveWindowAtts.advancedMultiWindowSave = 0
SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
SaveWindowAtts.subWindowAtts.win1.layer = 0
SaveWindowAtts.subWindowAtts.win1.transparency = 0
SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
SaveWindowAtts.subWindowAtts.win2.position = (0, 0)
SaveWindowAtts.subWindowAtts.win2.size = (128, 128)
SaveWindowAtts.subWindowAtts.win2.layer = 0
SaveWindowAtts.subWindowAtts.win2.transparency = 0
SaveWindowAtts.subWindowAtts.win2.omitWindow = 0
SaveWindowAtts.subWindowAtts.win3.position = (0, 0)
SaveWindowAtts.subWindowAtts.win3.size = (128, 128)
SaveWindowAtts.subWindowAtts.win3.layer = 0
SaveWindowAtts.subWindowAtts.win3.transparency = 0
SaveWindowAtts.subWindowAtts.win3.omitWindow = 0
SaveWindowAtts.subWindowAtts.win4.position = (0, 0)
SaveWindowAtts.subWindowAtts.win4.size = (128, 128)
SaveWindowAtts.subWindowAtts.win4.layer = 0
SaveWindowAtts.subWindowAtts.win4.transparency = 0
SaveWindowAtts.subWindowAtts.win4.omitWindow = 0
SaveWindowAtts.subWindowAtts.win5.position = (0, 0)
SaveWindowAtts.subWindowAtts.win5.size = (128, 128)
SaveWindowAtts.subWindowAtts.win5.layer = 0
SaveWindowAtts.subWindowAtts.win5.transparency = 0
SaveWindowAtts.subWindowAtts.win5.omitWindow = 0
SaveWindowAtts.subWindowAtts.win6.position = (0, 0)
SaveWindowAtts.subWindowAtts.win6.size = (128, 128)
SaveWindowAtts.subWindowAtts.win6.layer = 0
SaveWindowAtts.subWindowAtts.win6.transparency = 0
SaveWindowAtts.subWindowAtts.win6.omitWindow = 0
SaveWindowAtts.subWindowAtts.win7.position = (0, 0)
SaveWindowAtts.subWindowAtts.win7.size = (128, 128)
SaveWindowAtts.subWindowAtts.win7.layer = 0
SaveWindowAtts.subWindowAtts.win7.transparency = 0
SaveWindowAtts.subWindowAtts.win7.omitWindow = 0
SaveWindowAtts.subWindowAtts.win8.position = (0, 0)
SaveWindowAtts.subWindowAtts.win8.size = (128, 128)
SaveWindowAtts.subWindowAtts.win8.layer = 0
SaveWindowAtts.subWindowAtts.win8.transparency = 0
SaveWindowAtts.subWindowAtts.win8.omitWindow = 0
SaveWindowAtts.subWindowAtts.win9.position = (0, 0)
SaveWindowAtts.subWindowAtts.win9.size = (128, 128)
SaveWindowAtts.subWindowAtts.win9.layer = 0
SaveWindowAtts.subWindowAtts.win9.transparency = 0
SaveWindowAtts.subWindowAtts.win9.omitWindow = 0
SaveWindowAtts.subWindowAtts.win10.position = (0, 0)
SaveWindowAtts.subWindowAtts.win10.size = (128, 128)
SaveWindowAtts.subWindowAtts.win10.layer = 0
SaveWindowAtts.subWindowAtts.win10.transparency = 0
SaveWindowAtts.subWindowAtts.win10.omitWindow = 0
SaveWindowAtts.subWindowAtts.win11.position = (0, 0)
SaveWindowAtts.subWindowAtts.win11.size = (128, 128)
SaveWindowAtts.subWindowAtts.win11.layer = 0
SaveWindowAtts.subWindowAtts.win11.transparency = 0
SaveWindowAtts.subWindowAtts.win11.omitWindow = 0
SaveWindowAtts.subWindowAtts.win12.position = (0, 0)
SaveWindowAtts.subWindowAtts.win12.size = (128, 128)
SaveWindowAtts.subWindowAtts.win12.layer = 0
SaveWindowAtts.subWindowAtts.win12.transparency = 0
SaveWindowAtts.subWindowAtts.win12.omitWindow = 0
SaveWindowAtts.subWindowAtts.win13.position = (0, 0)
SaveWindowAtts.subWindowAtts.win13.size = (128, 128)
SaveWindowAtts.subWindowAtts.win13.layer = 0
SaveWindowAtts.subWindowAtts.win13.transparency = 0
SaveWindowAtts.subWindowAtts.win13.omitWindow = 0
SaveWindowAtts.subWindowAtts.win14.position = (0, 0)
SaveWindowAtts.subWindowAtts.win14.size = (128, 128)
SaveWindowAtts.subWindowAtts.win14.layer = 0
SaveWindowAtts.subWindowAtts.win14.transparency = 0
SaveWindowAtts.subWindowAtts.win14.omitWindow = 0
SaveWindowAtts.subWindowAtts.win15.position = (0, 0)
SaveWindowAtts.subWindowAtts.win15.size = (128, 128)
SaveWindowAtts.subWindowAtts.win15.layer = 0
SaveWindowAtts.subWindowAtts.win15.transparency = 0
SaveWindowAtts.subWindowAtts.win15.omitWindow = 0
SaveWindowAtts.subWindowAtts.win16.position = (0, 0)
SaveWindowAtts.subWindowAtts.win16.size = (128, 128)
SaveWindowAtts.subWindowAtts.win16.layer = 0
SaveWindowAtts.subWindowAtts.win16.transparency = 0
SaveWindowAtts.subWindowAtts.win16.omitWindow = 0
SaveWindowAtts.opts.types = ()
SaveWindowAtts.opts.help = ""
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetActivePlots(0)
DeleteActivePlots()
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.25/RUN01/inward.nek5000")
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.50/RUN01/inward.nek5000", 0)
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
AddPlot("Pseudocolor", "velocity_mag", 1, 1)
AddOperator("Isosurface", 1)
SetActivePlots(0)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 10
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 0, 1)
SetActivePlots(0)
DrawPlots()
SetTimeSliderState(0)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(1)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(2)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(3)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(4)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(5)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(6)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(7)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(8)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(9)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(10)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(11)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(12)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(13)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(14)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(15)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(16)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(17)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(18)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(19)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(20)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(21)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(22)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(23)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(24)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(25)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(26)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(27)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(28)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(29)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(30)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(31)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(32)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(33)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(34)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(35)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(36)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(37)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(38)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(39)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(40)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(41)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(42)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(43)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(44)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(45)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(46)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(47)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(48)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(49)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(50)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(51)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(52)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(53)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(54)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(55)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(56)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(57)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(58)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(59)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(60)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(61)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(62)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(63)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(64)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(65)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(66)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(67)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(68)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(69)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(70)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(71)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(72)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(73)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(74)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(75)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(76)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(77)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(78)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(79)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(80)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(81)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(82)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(83)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(84)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(85)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(86)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(87)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(88)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(89)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(90)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(91)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(92)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(93)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(94)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(95)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(96)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(97)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(98)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(99)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetActivePlots(0)
DeleteActivePlots()
AddPlot("Contour", "temperature", 1, 1)
ResizeWindow(1, 1000, 1000)
ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.SetNumControlPoints(30)
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.NONE  # NONE, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.tagNames = ("Default", "Discrete")
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (3)
ContourAtts.contourPercent = ()
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()
Query("SpatialExtents", use_actual_data=1)
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-12, 12, -12, 12)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
# End spontaneous state

View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-12, 12, -12, 12)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
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
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 0
AnnotationAtts.axes2D.yAxis.label.font.italic = 0
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
DrawPlots()
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/cluster/home/fkaufmann/inward_prop/post_processed_data/shapeIC_18.4k_phi_0.6/Uin_02.50_RUN01/images_CON"
SaveWindowAtts.fileName = "T3_Isocon_t_final"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.width = 1000
SaveWindowAtts.height = 1000
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.pixelData = 1
SaveWindowAtts.advancedMultiWindowSave = 0
SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
SaveWindowAtts.subWindowAtts.win1.layer = 0
SaveWindowAtts.subWindowAtts.win1.transparency = 0
SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
SaveWindowAtts.subWindowAtts.win2.position = (0, 0)
SaveWindowAtts.subWindowAtts.win2.size = (128, 128)
SaveWindowAtts.subWindowAtts.win2.layer = 0
SaveWindowAtts.subWindowAtts.win2.transparency = 0
SaveWindowAtts.subWindowAtts.win2.omitWindow = 0
SaveWindowAtts.subWindowAtts.win3.position = (0, 0)
SaveWindowAtts.subWindowAtts.win3.size = (128, 128)
SaveWindowAtts.subWindowAtts.win3.layer = 0
SaveWindowAtts.subWindowAtts.win3.transparency = 0
SaveWindowAtts.subWindowAtts.win3.omitWindow = 0
SaveWindowAtts.subWindowAtts.win4.position = (0, 0)
SaveWindowAtts.subWindowAtts.win4.size = (128, 128)
SaveWindowAtts.subWindowAtts.win4.layer = 0
SaveWindowAtts.subWindowAtts.win4.transparency = 0
SaveWindowAtts.subWindowAtts.win4.omitWindow = 0
SaveWindowAtts.subWindowAtts.win5.position = (0, 0)
SaveWindowAtts.subWindowAtts.win5.size = (128, 128)
SaveWindowAtts.subWindowAtts.win5.layer = 0
SaveWindowAtts.subWindowAtts.win5.transparency = 0
SaveWindowAtts.subWindowAtts.win5.omitWindow = 0
SaveWindowAtts.subWindowAtts.win6.position = (0, 0)
SaveWindowAtts.subWindowAtts.win6.size = (128, 128)
SaveWindowAtts.subWindowAtts.win6.layer = 0
SaveWindowAtts.subWindowAtts.win6.transparency = 0
SaveWindowAtts.subWindowAtts.win6.omitWindow = 0
SaveWindowAtts.subWindowAtts.win7.position = (0, 0)
SaveWindowAtts.subWindowAtts.win7.size = (128, 128)
SaveWindowAtts.subWindowAtts.win7.layer = 0
SaveWindowAtts.subWindowAtts.win7.transparency = 0
SaveWindowAtts.subWindowAtts.win7.omitWindow = 0
SaveWindowAtts.subWindowAtts.win8.position = (0, 0)
SaveWindowAtts.subWindowAtts.win8.size = (128, 128)
SaveWindowAtts.subWindowAtts.win8.layer = 0
SaveWindowAtts.subWindowAtts.win8.transparency = 0
SaveWindowAtts.subWindowAtts.win8.omitWindow = 0
SaveWindowAtts.subWindowAtts.win9.position = (0, 0)
SaveWindowAtts.subWindowAtts.win9.size = (128, 128)
SaveWindowAtts.subWindowAtts.win9.layer = 0
SaveWindowAtts.subWindowAtts.win9.transparency = 0
SaveWindowAtts.subWindowAtts.win9.omitWindow = 0
SaveWindowAtts.subWindowAtts.win10.position = (0, 0)
SaveWindowAtts.subWindowAtts.win10.size = (128, 128)
SaveWindowAtts.subWindowAtts.win10.layer = 0
SaveWindowAtts.subWindowAtts.win10.transparency = 0
SaveWindowAtts.subWindowAtts.win10.omitWindow = 0
SaveWindowAtts.subWindowAtts.win11.position = (0, 0)
SaveWindowAtts.subWindowAtts.win11.size = (128, 128)
SaveWindowAtts.subWindowAtts.win11.layer = 0
SaveWindowAtts.subWindowAtts.win11.transparency = 0
SaveWindowAtts.subWindowAtts.win11.omitWindow = 0
SaveWindowAtts.subWindowAtts.win12.position = (0, 0)
SaveWindowAtts.subWindowAtts.win12.size = (128, 128)
SaveWindowAtts.subWindowAtts.win12.layer = 0
SaveWindowAtts.subWindowAtts.win12.transparency = 0
SaveWindowAtts.subWindowAtts.win12.omitWindow = 0
SaveWindowAtts.subWindowAtts.win13.position = (0, 0)
SaveWindowAtts.subWindowAtts.win13.size = (128, 128)
SaveWindowAtts.subWindowAtts.win13.layer = 0
SaveWindowAtts.subWindowAtts.win13.transparency = 0
SaveWindowAtts.subWindowAtts.win13.omitWindow = 0
SaveWindowAtts.subWindowAtts.win14.position = (0, 0)
SaveWindowAtts.subWindowAtts.win14.size = (128, 128)
SaveWindowAtts.subWindowAtts.win14.layer = 0
SaveWindowAtts.subWindowAtts.win14.transparency = 0
SaveWindowAtts.subWindowAtts.win14.omitWindow = 0
SaveWindowAtts.subWindowAtts.win15.position = (0, 0)
SaveWindowAtts.subWindowAtts.win15.size = (128, 128)
SaveWindowAtts.subWindowAtts.win15.layer = 0
SaveWindowAtts.subWindowAtts.win15.transparency = 0
SaveWindowAtts.subWindowAtts.win15.omitWindow = 0
SaveWindowAtts.subWindowAtts.win16.position = (0, 0)
SaveWindowAtts.subWindowAtts.win16.size = (128, 128)
SaveWindowAtts.subWindowAtts.win16.layer = 0
SaveWindowAtts.subWindowAtts.win16.transparency = 0
SaveWindowAtts.subWindowAtts.win16.omitWindow = 0
SaveWindowAtts.opts.types = ()
SaveWindowAtts.opts.help = ""
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetActivePlots(0)
DeleteActivePlots()
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.50/RUN01/inward.nek5000")
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.75/RUN02/inward.nek5000", 0)
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
AddPlot("Pseudocolor", "velocity_mag", 1, 1)
AddOperator("Isosurface", 1)
SetActivePlots(0)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 10
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 0, 1)
SetActivePlots(0)
DrawPlots()
SetTimeSliderState(0)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(1)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(2)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(3)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(4)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(5)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(6)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(7)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(8)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(9)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(10)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(11)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(12)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(13)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(14)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(15)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(16)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(17)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(18)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(19)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(20)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(21)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(22)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(23)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(24)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(25)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(26)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(27)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(28)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(29)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(30)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(31)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(32)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(33)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(34)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(35)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(36)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(37)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(38)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(39)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(40)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(41)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(42)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(43)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(44)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(45)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(46)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(47)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(48)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(49)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(50)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(51)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(52)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(53)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(54)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(55)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(56)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(57)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(58)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(59)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(60)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(61)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(62)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(63)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(64)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(65)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(66)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(67)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(68)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(69)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(70)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(71)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(72)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(73)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(74)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(75)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(76)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(77)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(78)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(79)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(80)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(81)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(82)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(83)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(84)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(85)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(86)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(87)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(88)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(89)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(90)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(91)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(92)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(93)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(94)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(95)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(96)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(97)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(98)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(99)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetActivePlots(0)
DeleteActivePlots()
AddPlot("Contour", "temperature", 1, 1)
ResizeWindow(1, 1000, 1000)
ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.SetNumControlPoints(30)
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.NONE  # NONE, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.tagNames = ("Default", "Discrete")
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (3)
ContourAtts.contourPercent = ()
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()
Query("SpatialExtents", use_actual_data=1)
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-13, 13, -13, 13)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
# End spontaneous state

View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-13, 13, -13, 13)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
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
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 0
AnnotationAtts.axes2D.yAxis.label.font.italic = 0
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
DrawPlots()
SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/cluster/home/fkaufmann/inward_prop/post_processed_data/shapeIC_18.4k_phi_0.6/Uin_02.75_RUN02/images_CON"
SaveWindowAtts.fileName = "T3_Isocon_t_final"
SaveWindowAtts.family = 0
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY, EXR
SaveWindowAtts.width = 1000
SaveWindowAtts.height = 1000
SaveWindowAtts.screenCapture = 0
SaveWindowAtts.saveTiled = 0
SaveWindowAtts.quality = 80
SaveWindowAtts.progressive = 0
SaveWindowAtts.binary = 0
SaveWindowAtts.stereo = 0
SaveWindowAtts.compression = SaveWindowAtts.NONE  # NONE, PackBits, Jpeg, Deflate, LZW
SaveWindowAtts.forceMerge = 0
SaveWindowAtts.resConstraint = SaveWindowAtts.ScreenProportions  # NoConstraint, EqualWidthHeight, ScreenProportions
SaveWindowAtts.pixelData = 1
SaveWindowAtts.advancedMultiWindowSave = 0
SaveWindowAtts.subWindowAtts.win1.position = (0, 0)
SaveWindowAtts.subWindowAtts.win1.size = (128, 128)
SaveWindowAtts.subWindowAtts.win1.layer = 0
SaveWindowAtts.subWindowAtts.win1.transparency = 0
SaveWindowAtts.subWindowAtts.win1.omitWindow = 0
SaveWindowAtts.subWindowAtts.win2.position = (0, 0)
SaveWindowAtts.subWindowAtts.win2.size = (128, 128)
SaveWindowAtts.subWindowAtts.win2.layer = 0
SaveWindowAtts.subWindowAtts.win2.transparency = 0
SaveWindowAtts.subWindowAtts.win2.omitWindow = 0
SaveWindowAtts.subWindowAtts.win3.position = (0, 0)
SaveWindowAtts.subWindowAtts.win3.size = (128, 128)
SaveWindowAtts.subWindowAtts.win3.layer = 0
SaveWindowAtts.subWindowAtts.win3.transparency = 0
SaveWindowAtts.subWindowAtts.win3.omitWindow = 0
SaveWindowAtts.subWindowAtts.win4.position = (0, 0)
SaveWindowAtts.subWindowAtts.win4.size = (128, 128)
SaveWindowAtts.subWindowAtts.win4.layer = 0
SaveWindowAtts.subWindowAtts.win4.transparency = 0
SaveWindowAtts.subWindowAtts.win4.omitWindow = 0
SaveWindowAtts.subWindowAtts.win5.position = (0, 0)
SaveWindowAtts.subWindowAtts.win5.size = (128, 128)
SaveWindowAtts.subWindowAtts.win5.layer = 0
SaveWindowAtts.subWindowAtts.win5.transparency = 0
SaveWindowAtts.subWindowAtts.win5.omitWindow = 0
SaveWindowAtts.subWindowAtts.win6.position = (0, 0)
SaveWindowAtts.subWindowAtts.win6.size = (128, 128)
SaveWindowAtts.subWindowAtts.win6.layer = 0
SaveWindowAtts.subWindowAtts.win6.transparency = 0
SaveWindowAtts.subWindowAtts.win6.omitWindow = 0
SaveWindowAtts.subWindowAtts.win7.position = (0, 0)
SaveWindowAtts.subWindowAtts.win7.size = (128, 128)
SaveWindowAtts.subWindowAtts.win7.layer = 0
SaveWindowAtts.subWindowAtts.win7.transparency = 0
SaveWindowAtts.subWindowAtts.win7.omitWindow = 0
SaveWindowAtts.subWindowAtts.win8.position = (0, 0)
SaveWindowAtts.subWindowAtts.win8.size = (128, 128)
SaveWindowAtts.subWindowAtts.win8.layer = 0
SaveWindowAtts.subWindowAtts.win8.transparency = 0
SaveWindowAtts.subWindowAtts.win8.omitWindow = 0
SaveWindowAtts.subWindowAtts.win9.position = (0, 0)
SaveWindowAtts.subWindowAtts.win9.size = (128, 128)
SaveWindowAtts.subWindowAtts.win9.layer = 0
SaveWindowAtts.subWindowAtts.win9.transparency = 0
SaveWindowAtts.subWindowAtts.win9.omitWindow = 0
SaveWindowAtts.subWindowAtts.win10.position = (0, 0)
SaveWindowAtts.subWindowAtts.win10.size = (128, 128)
SaveWindowAtts.subWindowAtts.win10.layer = 0
SaveWindowAtts.subWindowAtts.win10.transparency = 0
SaveWindowAtts.subWindowAtts.win10.omitWindow = 0
SaveWindowAtts.subWindowAtts.win11.position = (0, 0)
SaveWindowAtts.subWindowAtts.win11.size = (128, 128)
SaveWindowAtts.subWindowAtts.win11.layer = 0
SaveWindowAtts.subWindowAtts.win11.transparency = 0
SaveWindowAtts.subWindowAtts.win11.omitWindow = 0
SaveWindowAtts.subWindowAtts.win12.position = (0, 0)
SaveWindowAtts.subWindowAtts.win12.size = (128, 128)
SaveWindowAtts.subWindowAtts.win12.layer = 0
SaveWindowAtts.subWindowAtts.win12.transparency = 0
SaveWindowAtts.subWindowAtts.win12.omitWindow = 0
SaveWindowAtts.subWindowAtts.win13.position = (0, 0)
SaveWindowAtts.subWindowAtts.win13.size = (128, 128)
SaveWindowAtts.subWindowAtts.win13.layer = 0
SaveWindowAtts.subWindowAtts.win13.transparency = 0
SaveWindowAtts.subWindowAtts.win13.omitWindow = 0
SaveWindowAtts.subWindowAtts.win14.position = (0, 0)
SaveWindowAtts.subWindowAtts.win14.size = (128, 128)
SaveWindowAtts.subWindowAtts.win14.layer = 0
SaveWindowAtts.subWindowAtts.win14.transparency = 0
SaveWindowAtts.subWindowAtts.win14.omitWindow = 0
SaveWindowAtts.subWindowAtts.win15.position = (0, 0)
SaveWindowAtts.subWindowAtts.win15.size = (128, 128)
SaveWindowAtts.subWindowAtts.win15.layer = 0
SaveWindowAtts.subWindowAtts.win15.transparency = 0
SaveWindowAtts.subWindowAtts.win15.omitWindow = 0
SaveWindowAtts.subWindowAtts.win16.position = (0, 0)
SaveWindowAtts.subWindowAtts.win16.size = (128, 128)
SaveWindowAtts.subWindowAtts.win16.layer = 0
SaveWindowAtts.subWindowAtts.win16.transparency = 0
SaveWindowAtts.subWindowAtts.win16.omitWindow = 0
SaveWindowAtts.opts.types = ()
SaveWindowAtts.opts.help = ""
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
SetActivePlots(0)
DeleteActivePlots()
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_02.75/RUN02/inward.nek5000")
OpenDatabase("/cluster/scratch/fkaufmann/shapeIC_18.4k_phi_0.6/Uin_03.00/RUN01/inward.nek5000", 0)
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("radius", "polar_radius(mesh)")
DefineScalarExpression("x-coord", "coord(mesh)[0]")
DefineScalarExpression("y-coord", "coord(mesh)[1]")
DefineScalarExpression("operators/ConnectedComponents/mesh", "cell_constant(<mesh>, 0.)")
DefineCurveExpression("operators/DataBinning/1D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/2D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/DataBinning/3D/mesh", "cell_constant(<mesh>, 0)")
DefineScalarExpression("operators/Flux/mesh", "cell_constant(<mesh>, 0.)")
DefineScalarExpression("operators/IntegralCurve/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineVectorExpression("operators/LCS/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lagrangian/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/LimitCycle/velocity", "cell_constant(<velocity>, 0.)")
DefineCurveExpression("operators/Lineout/pressure", "cell_constant(<pressure>, 0.)")
DefineCurveExpression("operators/Lineout/temperature", "cell_constant(<temperature>, 0.)")
DefineCurveExpression("operators/Lineout/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineCurveExpression("operators/Lineout/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineCurveExpression("operators/Lineout/s1", "cell_constant(<s1>, 0.)")
DefineCurveExpression("operators/Lineout/s2", "cell_constant(<s2>, 0.)")
DefineCurveExpression("operators/Lineout/s3", "cell_constant(<s3>, 0.)")
DefineCurveExpression("operators/Lineout/s4", "cell_constant(<s4>, 0.)")
DefineCurveExpression("operators/Lineout/s5", "cell_constant(<s5>, 0.)")
DefineCurveExpression("operators/Lineout/s6", "cell_constant(<s6>, 0.)")
DefineCurveExpression("operators/Lineout/s7", "cell_constant(<s7>, 0.)")
DefineCurveExpression("operators/Lineout/s8", "cell_constant(<s8>, 0.)")
DefineCurveExpression("operators/Lineout/s9", "cell_constant(<s9>, 0.)")
DefineCurveExpression("operators/Lineout/radius", "cell_constant(radius, 0.)")
DefineCurveExpression("operators/Lineout/x-coord", "cell_constant(x-coord, 0.)")
DefineCurveExpression("operators/Lineout/y-coord", "cell_constant(y-coord, 0.)")
DefineScalarExpression("operators/ModelFit/model", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/ModelFit/distance", "point_constant(<mesh>, 0)")
DefineScalarExpression("operators/Poincare/velocity", "cell_constant(<velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/pressure", "cell_constant(<pressure>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/temperature", "cell_constant(<temperature>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x_velocity", "cell_constant(<x_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y_velocity", "cell_constant(<y_velocity>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/velocity_mag", "cell_constant(<velocity_mag>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s1", "cell_constant(<s1>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s2", "cell_constant(<s2>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s3", "cell_constant(<s3>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s4", "cell_constant(<s4>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s5", "cell_constant(<s5>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s6", "cell_constant(<s6>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s7", "cell_constant(<s7>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s8", "cell_constant(<s8>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/s9", "cell_constant(<s9>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Sum/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Mean/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Variance/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Std. Dev./y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Slope/y-coord", "cell_constant(<y-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/radius", "cell_constant(<radius>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/x-coord", "cell_constant(<x-coord>, 0.)")
DefineScalarExpression("operators/StatisticalTrends/Residuals/y-coord", "cell_constant(<y-coord>, 0.)")
DefineVectorExpression("operators/SurfaceNormal/mesh", "cell_constant(<mesh>, 0.)")
AddPlot("Pseudocolor", "velocity_mag", 1, 1)
AddOperator("Isosurface", 1)
SetActivePlots(0)
IsosurfaceAtts = IsosurfaceAttributes()
IsosurfaceAtts.contourNLevels = 10
IsosurfaceAtts.contourValue = ()
IsosurfaceAtts.contourPercent = ()
IsosurfaceAtts.contourMethod = IsosurfaceAtts.Level  # Level, Value, Percent
IsosurfaceAtts.minFlag = 0
IsosurfaceAtts.min = 0
IsosurfaceAtts.maxFlag = 0
IsosurfaceAtts.max = 1
IsosurfaceAtts.scaling = IsosurfaceAtts.Linear  # Linear, Log
IsosurfaceAtts.variable = "default"
SetOperatorOptions(IsosurfaceAtts, 0, 1)
SetActivePlots(0)
DrawPlots()
SetTimeSliderState(0)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(1)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(2)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(3)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(4)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(5)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(6)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(7)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(8)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(9)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(10)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(11)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(12)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(13)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(14)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(15)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(16)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(17)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(18)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(19)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(20)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(21)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(22)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(23)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(24)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(25)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(26)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(27)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(28)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(29)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(30)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(31)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(32)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(33)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(34)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(35)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(36)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(37)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(38)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(39)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(40)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(41)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(42)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(43)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(44)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(45)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(46)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(47)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(48)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(49)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(50)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(51)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(52)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(53)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(54)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(55)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(56)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(57)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(58)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(59)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(60)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(61)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(62)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(63)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(64)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(65)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(66)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(67)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(68)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(69)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(70)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(71)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(72)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(73)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(74)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(75)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(76)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(77)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(78)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(79)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(80)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(81)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(82)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(83)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(84)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(85)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(86)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(87)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(88)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(89)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(90)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(91)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(92)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(93)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(94)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(95)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(96)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(97)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(98)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetTimeSliderState(99)
Query("Time")
Query("Average Value")
Query("Total Length")
Logging of ExportDatabase currently disabled.
SetActivePlots(0)
DeleteActivePlots()
AddPlot("Contour", "temperature", 1, 1)
ResizeWindow(1, 1000, 1000)
ContourAtts = ContourAttributes()
ContourAtts.defaultPalette.SetNumControlPoints(30)
ContourAtts.defaultPalette.GetControlPoints(0).colors = (255, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(0).position = 0
ContourAtts.defaultPalette.GetControlPoints(1).colors = (0, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(1).position = 0.034
ContourAtts.defaultPalette.GetControlPoints(2).colors = (0, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(2).position = 0.069
ContourAtts.defaultPalette.GetControlPoints(3).colors = (0, 255, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(3).position = 0.103
ContourAtts.defaultPalette.GetControlPoints(4).colors = (255, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(4).position = 0.138
ContourAtts.defaultPalette.GetControlPoints(5).colors = (255, 255, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(5).position = 0.172
ContourAtts.defaultPalette.GetControlPoints(6).colors = (255, 135, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(6).position = 0.207
ContourAtts.defaultPalette.GetControlPoints(7).colors = (255, 0, 135, 255)
ContourAtts.defaultPalette.GetControlPoints(7).position = 0.241
ContourAtts.defaultPalette.GetControlPoints(8).colors = (168, 168, 168, 255)
ContourAtts.defaultPalette.GetControlPoints(8).position = 0.276
ContourAtts.defaultPalette.GetControlPoints(9).colors = (255, 68, 68, 255)
ContourAtts.defaultPalette.GetControlPoints(9).position = 0.31
ContourAtts.defaultPalette.GetControlPoints(10).colors = (99, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(10).position = 0.345
ContourAtts.defaultPalette.GetControlPoints(11).colors = (99, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(11).position = 0.379
ContourAtts.defaultPalette.GetControlPoints(12).colors = (40, 165, 165, 255)
ContourAtts.defaultPalette.GetControlPoints(12).position = 0.414
ContourAtts.defaultPalette.GetControlPoints(13).colors = (255, 99, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(13).position = 0.448
ContourAtts.defaultPalette.GetControlPoints(14).colors = (255, 255, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(14).position = 0.483
ContourAtts.defaultPalette.GetControlPoints(15).colors = (255, 170, 99, 255)
ContourAtts.defaultPalette.GetControlPoints(15).position = 0.517
ContourAtts.defaultPalette.GetControlPoints(16).colors = (170, 79, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(16).position = 0.552
ContourAtts.defaultPalette.GetControlPoints(17).colors = (150, 0, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(17).position = 0.586
ContourAtts.defaultPalette.GetControlPoints(18).colors = (0, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(18).position = 0.621
ContourAtts.defaultPalette.GetControlPoints(19).colors = (0, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(19).position = 0.655
ContourAtts.defaultPalette.GetControlPoints(20).colors = (0, 109, 109, 255)
ContourAtts.defaultPalette.GetControlPoints(20).position = 0.69
ContourAtts.defaultPalette.GetControlPoints(21).colors = (150, 0, 150, 255)
ContourAtts.defaultPalette.GetControlPoints(21).position = 0.724
ContourAtts.defaultPalette.GetControlPoints(22).colors = (150, 150, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(22).position = 0.759
ContourAtts.defaultPalette.GetControlPoints(23).colors = (150, 84, 0, 255)
ContourAtts.defaultPalette.GetControlPoints(23).position = 0.793
ContourAtts.defaultPalette.GetControlPoints(24).colors = (160, 0, 79, 255)
ContourAtts.defaultPalette.GetControlPoints(24).position = 0.828
ContourAtts.defaultPalette.GetControlPoints(25).colors = (255, 104, 28, 255)
ContourAtts.defaultPalette.GetControlPoints(25).position = 0.862
ContourAtts.defaultPalette.GetControlPoints(26).colors = (0, 170, 81, 255)
ContourAtts.defaultPalette.GetControlPoints(26).position = 0.897
ContourAtts.defaultPalette.GetControlPoints(27).colors = (68, 255, 124, 255)
ContourAtts.defaultPalette.GetControlPoints(27).position = 0.931
ContourAtts.defaultPalette.GetControlPoints(28).colors = (0, 130, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(28).position = 0.966
ContourAtts.defaultPalette.GetControlPoints(29).colors = (130, 0, 255, 255)
ContourAtts.defaultPalette.GetControlPoints(29).position = 1
ContourAtts.defaultPalette.smoothing = ContourAtts.defaultPalette.NONE  # NONE, Linear, CubicSpline
ContourAtts.defaultPalette.equalSpacingFlag = 1
ContourAtts.defaultPalette.discreteFlag = 1
ContourAtts.defaultPalette.tagNames = ("Default", "Discrete")
ContourAtts.changedColors = ()
ContourAtts.colorType = ContourAtts.ColorBySingleColor  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
ContourAtts.colorTableName = "Default"
ContourAtts.invertColorTable = 0
ContourAtts.legendFlag = 0
ContourAtts.lineWidth = 3
ContourAtts.singleColor = (255, 0, 0, 255)
ContourAtts.contourMethod = ContourAtts.Value  # Level, Value, Percent
ContourAtts.contourNLevels = 10
ContourAtts.contourValue = (3)
ContourAtts.contourPercent = ()
ContourAtts.SetMultiColor(0, (255, 0, 0, 255))
ContourAtts.SetMultiColor(1, (0, 255, 0, 255))
ContourAtts.SetMultiColor(2, (0, 0, 255, 255))
ContourAtts.SetMultiColor(3, (0, 255, 255, 255))
ContourAtts.SetMultiColor(4, (255, 0, 255, 255))
ContourAtts.SetMultiColor(5, (255, 255, 0, 255))
ContourAtts.SetMultiColor(6, (255, 135, 0, 255))
ContourAtts.SetMultiColor(7, (255, 0, 135, 255))
ContourAtts.SetMultiColor(8, (168, 168, 168, 255))
ContourAtts.SetMultiColor(9, (255, 68, 68, 255))
ContourAtts.minFlag = 0
ContourAtts.maxFlag = 0
ContourAtts.min = 0
ContourAtts.max = 1
ContourAtts.scaling = ContourAtts.Linear  # Linear, Log
ContourAtts.wireframe = 0
SetPlotOptions(ContourAtts)
DrawPlots()
Query("SpatialExtents", use_actual_data=1)
# Begin spontaneous state
View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-13, 13, -13, 13)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
# End spontaneous state

View2DAtts = View2DAttributes()
View2DAtts.windowCoords = (-13, 13, -13, 13)
View2DAtts.viewportCoords = (0.1, 1, 0.1, 1)
View2DAtts.fullFrameActivationMode = View2DAtts.Off  # On, Off, Auto
View2DAtts.fullFrameAutoThreshold = 100
View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
View2DAtts.windowValid = 0
SetView2D(View2DAtts)
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
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
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
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 0
AnnotationAtts.axes2D.yAxis.label.font.italic = 0
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 1
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 1
AnnotationAtts.axes3D.bboxFlag = 1
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 1
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = ""
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented 