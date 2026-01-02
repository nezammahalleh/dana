
import arcpy

wq = "E:/TEST/ASHPs/test6/mkyy.gdb/villg"



fields = [f.name for f in arcpy.ListFields(wq)]
print(fields)

fields.remove('Shape')
fields.remove('ObjectID')

arcpy.DeleteField_management(wq, fields)

#new

import arcpy
from arcpy import *

qw = "E:/TEST/ASHPs/test6/mkyy.gdb/villg"

arcpy.management.AddField(wq,"karx","LONG")


#new

#fill field "karx" with value 25 in all rows

import arcpy
from arcpy import *

qw = "E:/TEST/ASHPs/test6/mkyy.gdb/villg"

arcpy.management.CalculateField(wq,"karx","25","PYTHON_9.3")



#copy bb field values into sss field 
arcpy.CalculateField_management("t_bb","sss",'!BB!',"PYTHON_9.3")

#plus "OBJECTID_1" + 3 and write the values in field Parx. 
#fill all rows of field "Parx" with formul of "!OBJECTID_1! + 3"

import arcpy
from arcpy import *

qw = "E:/TEST/ASHPs/test6/mkyy.gdb/villg"

arcpy.management.CalculateField(wq,"Parx",'!OBJECTID_1! + 3',"PYTHON_9.3")


#new 
# feature to point 

import arcpy
from arcpy import *

qwt = arcpy.env.workspace = "E:/TEST/ASHPs/test6/mkyy.gdb"


for i in arcpy.ListFeatureClasses("teh22*"):
    arcpy.management.FeatureToPoint(i,'Tp_{}'.format(i))


#new
#fishnet 

outputf = r"E:\TEST\ASHPs\test6\test6.gdb\k2"
qox = 51.3632051
qoy = 35.6888829
qdx = 51.3635725
qdy = 35.701082
qh = 1250
qw = 1400
qr = 1
qc = 1

qoxy = (str(qox) + ' ' + str(qoy))
qdxy = (str(qdx )+ ' ' + str(qdy))




arcpy.management.CreateFishnet(outputf, qoxy, qdxy, 10, 10, 1, 1, None, "LABELS", "DEFAULT", "POLYGON")


#fishnet by UTM


outputf = r"E:\TEST\ASHPs\test6\test6.gdb\k7"
qox = 532891
qoy = 3949492
qdx = 532847
qdy = 3950839
qh = 1250
qw = 1400
qr = 1
qc = 1

qoxy = (str(qox) + ' ' + str(qoy))
qdxy = (str(qdx )+ ' ' + str(qdy))

#arcpy.management.CreateFishnet(outputf, qoxy, qdxy, 10, 10, 1, 1, None, "LABELS", "DEFAULT", "POLYGON") 

with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_UTM_Zone_39N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",51.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'):
    arcpy.management.CreateFishnet(outputf, qoxy, qdxy, qw, qh, qr, qc, None, "LABELS", "DEFAULT", "POLYGON")


    
#new
#not complete yet 

import arcpy
from arcpy import *

qwt = arcpy.env.workspace = "E:/TEST/ASHPs/test6/test6.gdb"

landusef = "lu_r10p"

urd = arcpy.analysis.Select(landusef, r"E:\TEST\ASHPs\test6\test6.gdb\lu_r10p_Select", "LANDUSEID = 1")
unrd = arcpy.analysis.Select(landusef, r"E:\TEST\ASHPs\test6\test6.gdb\lu_r10p_Select", "LANDUSEID > 1")

userv = arcpy.ListFeatureClasses("E:/TEST/ASHPs/test6/pot.gdb")

for s in users:
    arcpy.analysis.Near(urd, s, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")



#arcpy.analysis.Near("k7", "k8_label", None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")


#arcpy.analysis.SplitByAttributes("r10t_points", r"E:\TEST\ASHPs\test6\fdr", "type")




