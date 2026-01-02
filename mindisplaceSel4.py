import os
import arcpy
from arcpy import *
from arcpy import env

arcpy.env.workspace = r'E:\Test\New Folder\New Personal Geodatabase (2).mdb'
arcpy.env.overwriteOutput = True

tbb = "nnr"
fdd = "NEAR_DIST"
selt = "NEAR_DIST"
outsp = "outpza1"

#helped by James Crandall

#tbb = "raster points"
#fdd= "NEAR_DIST"
#selt = "stationText"

minfdd = arcpy.SearchCursor(tbb,"","","",fdd+ " A").next().getValue(selt)

#minfdd is nearest and its id is output value

arcpy.Select_analysis(tbb, outsp, "NEAR_DIST" + '=' + str(minfdd))


