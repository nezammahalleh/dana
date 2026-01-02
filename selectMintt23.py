import arcpy
from arcpy import *

wk = arcpy.env.workspace = r"D:\Nezammahalleh\project_Nezammahalleh\MyProject3\MyProject3.gdb"
arcpy.env.overwriteOutput = True

#helped by James Crandall

tbb = "srt"
fdd= "dist"
selt = "dist"
minfdd = arcpy.SearchCursor(tbb,"","","",fdd+ " A").next().getValue(selt)
print (minfdd)

arcpy.analysis.Select("srt", r"D:\Nezammahalleh\project_Nezammahalleh\MyProject3\MyProject3.gdb\srt_Select4", "dist" + '='+str(minfdd))
