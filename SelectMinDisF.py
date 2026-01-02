import os
import arcpy
from arcpy import *
from arcpy import env

arcpy.env.workspace = r"D:\Nezammahalleh\project_Nezammahalleh\MyProject3\vol2.gdb"
arcpy.env.overwriteOutput = True

qqf = arcpy.ListFeatureClasses("F*","")

qqd =arcpy.ListFeatureClasses("D*","")

for idx_d in qqd:
    number = idx_d[1:]
    idx_f = qqf[qqf.index('F'+number)]
    arcpy.analysis.Near(idx_d, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
    minfdd = arcpy.SearchCursor(idx_d,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
    print (minfdd)
    arcpy.analysis.Select(idx_d, f'n2_{idx_f}', "OBJECTID" + '='+str(minfdd))
    

    



