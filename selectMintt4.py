import arcpy
from arcpy import *

wk = arcpy.env.workspace = r"D:\Nezammahalleh\project_Nezammahalleh\MyProject3\vol2.gdb"
arcpy.env.overwriteOutput = True


tbb = "D51272540"
fdd= "NEAR_DIST"
selt = "OBJECTID"
minfdd = arcpy.SearchCursor(tbb,"","","",fdd+ " A").next().getValue(selt)
print (str(minfdd))

arcpy.analysis.Select(tbb, "nnx", "OBJECTID" + '='+str(minfdd))


