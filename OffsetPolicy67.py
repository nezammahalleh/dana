import arcpy
from arcpy import*



arcpy.env.overwriteOutput = True

ss = arcpy.GetParameterAsText(0)
sf = arcpy.GetParameterAsText(1)
bnd = arcpy.GetParameterAsText(2)
nawp =arcpy.GetParameterAsText(3)
finalaw =arcpy.GetParameterAsText(4)
palw = arcpy.GetParameterAsText(5)


sel1 = arcpy.MakeFeatureLayer_management(ss, "sel2")
nawf = arcpy.Select_analysis(arcpy.SelectLayerByLocation_management(sel1, "INTERSECT", sf), nawp, "")

qaxy = arcpy.AddXY_management(nawf)
aaf1 = arcpy.AddField_management(qaxy, "mjr", "LONG", 9,"")
aaf2 = arcpy.AddField_management(qaxy, "mnr", "LONG", 9,"")
aaf3 = arcpy.AddField_management(qaxy, "azm", "DOUBLE", 9,"")
acf1 = arcpy.CalculateField_management(aaf3, "mjr",'350',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "mnr",'1',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "azm",'53.4997',"PYTHON_9.3")
qbb2 = arcpy.Buffer_analysis(arcpy.Buffer_analysis(arcpy.TableToEllipse_management(acf2, "xecpp", "POINT_X", "POINT_Y", "mjr", "mnr","METERS","azm", "DEGREES", ""), "xbuf1", "12.01 Meters", "FULL", "FLAT", ""), "xbuf2", "-12.0 Meters", "FULL", "ROUND","")
qsp = arcpy.SpatialJoin_analysis(qbb2, nawf, "xoutsp","","","","INTERSECT")
qring = arcpy.MultipleRingBuffer_analysis(nawf, "xmrng", [1,50,100,150],"meters", "", "ALL")
qbb3 = arcpy.Buffer_analysis(arcpy.Intersect_analysis ([qring, qsp], "xqinsc", "ALL", "", "POINT"), "xwbb", "12.49 Meters", "FULL", "ROUND", "LIST", "Stationtext")
qerz = arcpy.Erase_analysis(bnd, sf, "xeraseOut")
qfaw = arcpy.Intersect_analysis ([qbb3, qerz], finalaw, "ALL", "", "")
qras2 = arcpy.RasterToPoint_conversion(arcpy.FeatureToRaster_conversion(qfaw, "FID_xwbb", "xoutras1", 1), palw, "VALUE")







