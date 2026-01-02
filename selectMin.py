import arcpy
from arcpy import *

wk = arcpy.env.workspace = "E:\Test\New Folder"
arcpy.env.overwriteOutput = True

#helped by James Crandall

tbb = "nnr.shp"
fdd= "NEAR_DIST"
selt = "idp"
minfdd = arcpy.SearchCursor(tbb,"","","",fdd+ " A").next().getValue(selt)
print minfdd
