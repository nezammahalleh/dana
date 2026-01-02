import arcpy

fc = "e:/Test/aq/wq.shp"
ff1="val"
ff2="val2"

nzcursor = arcpy.UpdateCursor(fc)
for mm in nzcursor:
    mm.setValue(ff2, mm.getValue(ff1)*10)
    nzcursor.updateRow(mm)
    
