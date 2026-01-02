import os
import arcpy
from arcpy import *

wk = arcpy.env.workspace = "D:\Nezammahalleh\project_Nezammahalleh\MyProject2"
arcpy.env.overwriteOutput = True

tbb = arcpy.GetParameterAsText(0)
fdd = arcpy.GetParameterAsText(1)
selt = arcpy.GetParameterAsText(2)
minfdd = arcpy.GetParameterAsText(3)

#helped by James Crandall

#tbb = "raster points"
#fdd= "NEAR_DIST"
#selt = "stationText"

minfdd = arcpy.SearchCursor(tbb,"","","",fdd+ " A").next().getValue(selt)

#minfdd is nearest and its id is output value
