import arcpy
from arcpy import*
from sys import argv



arcpy.env.overwriteOutput = True

ss = "sourcep" #arcpy.GetParameterAsText(0) #"sourcep"
sf = "safety" #arcpy.GetParameterAsText(1) #"safety"
bnd = "SwathBoundary" #arcpy.GetParameterAsText(2) #"SwathBoundary"
nawp = "noalw" #arcpy.GetParameterAsText(3) #"w1"
finalaw = "finalw" #arcpy.GetParameterAsText(4) #"w2"
wks =  r"D:\Nezammahalleh\project_Nezammahalleh\MyProject6\vol3.gdb" #arcpy.GetParameterAsText(5) #r"D:\Nezammahalleh\project_Nezammahalleh\MyProject3\vol7.gdb"
finalmg = "mergbjoin" #arcpy.GetParameterAsText(6) #final "merg12"

arcpy.env.workspace = wks 

arcpy.env.overwriteOutput = True


sel1 = arcpy.MakeFeatureLayer_management(ss, "sel2")
nawf = arcpy.Select_analysis(arcpy.SelectLayerByLocation_management(sel1, "INTERSECT", sf), nawp, "")

qaxy = arcpy.AddXY_management(nawf)
aaf1 = arcpy.AddField_management(qaxy, "mjr", "LONG", 9,"")
aaf2 = arcpy.AddField_management(qaxy, "mnr", "LONG", 9,"")
aaf3 = arcpy.AddField_management(qaxy, "azm", "DOUBLE", 9,"")
acf1 = arcpy.CalculateField_management(aaf3, "mjr",'350',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "mnr",'1',"PYTHON_9.3")
acf2 = arcpy.CalculateField_management(aaf3, "azm",'42',"PYTHON_9.3")
qbb2 = arcpy.Buffer_analysis(arcpy.Buffer_analysis(arcpy.TableToEllipse_management(acf2, "xecpp", "POINT_X", "POINT_Y", "mjr", "mnr","METERS","azm", "DEGREES", ""), "xbuf1", "12.01 Meters", "FULL", "FLAT", ""), "xbuf2", "-12.0 Meters", "FULL", "ROUND","")
qsp = arcpy.SpatialJoin_analysis(qbb2, nawf, "xoutsp","","","","INTERSECT")
qring = arcpy.MultipleRingBuffer_analysis(nawf, "xmrng", [1,50,100,150],"meters", "", "ALL")
qbb3 = arcpy.Buffer_analysis(arcpy.Intersect_analysis ([qring, qsp], "xqinsc", "ALL", "", "POINT"), "xwbb", "12.49 Meters", "FULL", "ROUND", "LIST", "Stationtext")
qerz = arcpy.Erase_analysis(bnd, sf, "xeraseOut")
qfaw = arcpy.Intersect_analysis ([qbb3, qerz], finalaw, "ALL", "", "")
qras2 = arcpy.RasterToPoint_conversion(arcpy.FeatureToRaster_conversion(qfaw, "FID_xwbb", "xoutras1", 2), "xpalw", "VALUE")

qaltv = arcpy.SpatialJoin_analysis(qras2, qfaw, "xoutsp2","","","","INTERSECT")

#for 1m center  points 

qbb5 = arcpy.Buffer_analysis(arcpy.Intersect_analysis ([qring, qsp], "xqinsc5", "ALL", "", "POINT"), "xwbb5", "1 Meters", "FULL", "ROUND", "LIST", "Stationtext")
qerz5 = arcpy.Erase_analysis(bnd, sf, "xeraseOut5")
xcntr5=arcpy.Intersect_analysis ([qbb5, qerz5], "xfourcentr5", "ALL", "", "")
qras5 = arcpy.RasterToPoint_conversion(arcpy.FeatureToRaster_conversion(xcntr5, "FID_xwbb5", "xoutras15", 1), "xcenter5", "VALUE")

qaltv5 = arcpy.SpatialJoin_analysis(qras5, xcntr5, "xoutsp5","","","","INTERSECT")



#spliting 3set
##
qafj1 = arcpy.AddField_management(nawf, "stationf", "STRING", 9,"")
qcfj1 = arcpy.CalculateField_management(qafj1, "stationf",'"kf" + !Stationtext! ',"PYTHON_9.3")
qadj2 = arcpy.AddField_management(qaltv, "stationd", "STRING", 9,"")
qcdj2 = arcpy.CalculateField_management(qadj2, "stationd",'"kd" + !Stationtext! ',"PYTHON_9.3")
qacj3 = arcpy.AddField_management(qaltv5, "stationc", "STRING", 9,"")
qccj3 = arcpy.CalculateField_management(qacj3, "stationc",'"kc" + !Stationtext! ',"PYTHON_9.3")

qqf = arcpy.SplitByAttributes_analysis(qcfj1, wks, ['STATIONF'])
qqd = arcpy.SplitByAttributes_analysis(qcdj2, wks, ['STATIOND'])
qqd = arcpy.SplitByAttributes_analysis(qccj3, wks, ['STATIONC'])


#list 3sets 
qqf = arcpy.ListFeatureClasses("kf*","")
qqd =arcpy.ListFeatureClasses("kd*","")
qqc =arcpy.ListFeatureClasses("kc*","")

#selecting





##
for idx_f in qqf:
    number = idx_f[2:]
    try:
        idx_d = qqd[qqd.index('kd'+number)]
        try:
            idx_c = qqc[qqc.index('kc'+number)]
            arcpy.analysis.Near(idx_d, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
            arcpy.analysis.Near(idx_c, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
            minfdd = arcpy.SearchCursor(idx_d,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
            minfdc = arcpy.SearchCursor(idx_c,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
            if (minfdd - minfdc) < 5:
                arcpy.analysis.Select(idx_c, f'jc_{idx_f}', "OBJECTID" + '='+str(minfdc))
            else:
                arcpy.analysis.Select(idx_d, f'jd_{idx_f}', "OBJECTID" + '='+str(minfdd))
        except:
                arcpy.analysis.Select(idx_d, f'jd_{idx_f}', "OBJECTID" + '='+str(minfdd))


    except:
        print(number)

    
##for idx_f in qqf:
##    number = idx_f[2:]
##    idx_d = qqd[qqd.index('kd'+number)]
##    arcpy.analysis.Near(idx_d, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
##    minfdd = arcpy.SearchCursor(idx_d,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
##    arcpy.analysis.Select(idx_d, f'jd_{idx_f}', "OBJECTID" + '='+str(minfdd))
##    idx_c = qqc[qqc.index('kc'+number)]
##    arcpy.analysis.Near(idx_c, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
##    minfdc = arcpy.SearchCursor(idx_c,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
##    arcpy.analysis.Select(idx_c, f'jc_{idx_f}', "OBJECTID" + '='+str(minfdc))
##
##    
    
qmrg = arcpy.ListFeatureClasses("j*","")

arcpy.management.Merge(qmrg, finalmg, field_mappings="", add_source="NO_SOURCE_INFO")

arcpy.management.Delete(arcpy.ListFeatureClasses("x*",""), '')
arcpy.management.Delete(arcpy.ListRasters("x*",""), '')


#previous bellow

##
##for idx_d in qqd:
##    number = idx_d[1:]
##    idx_f = qqf[qqf.index('F'+number)]
##    arcpy.analysis.Near(idx_d, idx_f, None, "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST")
##    minfdd = arcpy.SearchCursor(idx_d,"","","","NEAR_DIST"+ " A").next().getValue("OBJECTID")
##    arcpy.analysis.Select(idx_d, f'n2_{idx_f}', "OBJECTID" + '='+str(minfdd))
##    
##qmrg = arcpy.ListFeatureClasses("n2*","")
##
##arcpy.management.Merge(qmrg, finalmg, field_mappings="", add_source="NO_SOURCE_INFO")
##
##listx = arcpy.ListFeatureClasses("x*","")
##
##arcpy.management.Delete(listx, '')
