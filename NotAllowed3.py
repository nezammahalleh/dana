import arcpy
from arcpy import*


arcpy.env.workspace = r'E:\Test\dana\New Personal Geodatabase (6).mdb'
arcpy.env.overwriteOutput = True

ss = "Soursepp"
sf = "safetyd"

sel1 = arcpy.MakeFeatureLayer_management(ss, "sel2")
nawf = arcpy.Select_analysis(arcpy.SelectLayerByLocation_management(sel1, "INTERSECT", sf), "naw1", "")

qaxy = arcpy.AddXY_management(nawf)
aaf1 = arcpy.AddField_management(qaxy, "mjr", "LONG", 9,"")
aaf2 = arcpy.AddField_management(qaxy, "mnr", "LONG", 9,"")
aaf3 = arcpy.AddField_management(qaxy, "azm", "DOUBLE", 9,"")
acf1 = arcpy.CalculateField_management(aaf3, "mjr",'350',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "mnr",'1',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "azm",'46.5',"PYTHON_9.3")
qazm = arcpy.TableToEllipse_management(acf2, "ecpp", "POINT_X", "POINT_Y", "mjr", "mnr","METERS","azm", "DEGREES", "")
qbb = arcpy.Buffer_analysis(qazm, "buf1", "12.01 Meters", "FULL", "FLAT", "")
qbb2 = arcpy.Buffer_analysis(qbb, "buf2", "-12.0 Meters", "FULL", "ROUND","")
qsp = arcpy.SpatialJoin_analysis(qbb2, nawf, "outsp","","","","INTERSECT")
qring = arcpy.MultipleRingBuffer_analysis(nawf, "mrng", [1,50,100,150],"meters", "", "ALL")
qins = arcpy.Intersect_analysis ([qring, qsp], "qinsc", "ALL", "", "POINT")



