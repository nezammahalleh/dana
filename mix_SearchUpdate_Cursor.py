


#n1

import arcpy

wq = arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\Intop.gdb"

jv =  "Mahshr"
sv = "c103"


for radif in arcpy.SearchCursor(jv):
    hr = radif.getValue(sv)
    print(hr+10)



#n
import arcpy

arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\Intop.gdb"

fk = "Mahshr"

cursorz = arcpy.UpdateCursor(fk)

for radif in cursorz:
    radif.setValue("nesbtmz", radif.getValue("jamyat")+radif.getValue("c103"))
    cursorz.updateRow(radif)
    
del radif
del cursorz






#n2

import arcpy

arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\Intop.gdb"

fk = "Mahshr"

cursorz = arcpy.UpdateCursor(fk)

for radif in cursorz:
    try:
        radif.setValue("nesbtmz", radif.getValue("jamyat")/radif.getValue("c103"))
        cursorz.updateRow(radif)
    except:
        radif.setValue("nesbtmz",1)
        cursorz.updateRow(radif)

del radif
del cursorz


#n

import arcpy

arcpy.env.workspace = "E:\\Rasht_Shahrdari\\Projects\\Sessions\\Jalase11\\New File Geodatabase.gdb"
esmlaye = "E:\\Rasht_Shahrdari\\Projects\\Sessions\\Jalase11\\New File Geodatabase.gdb\\village2"

flk = arcpy.management.MakeFeatureLayer('village2',"kaw")
esm2 = arcpy.management.SelectLayerByAttribute('el_lyr2',"",'"JAMEYAT">1000',"")

cursorh = arcpy.UpdateCursor(esm2)
for radif in cursorh:
    radif.setValue("MARD", radif.getValue("KHANEVAR")+radif.getValue("JAMEYAT")+10000)
    radif.setValue("ZAN", radif.getValue("KHANEVAR")+radif.getValue("JAMEYAT")*0.5)
    cursorh.updateRow(radif)

del radif
del cursorh


#n



#start 12

import arcpy

wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\str10.gdb"
marz = "bordr"
sotun_masahat = 'Shape_Area'

with arcpy.da.SearchCursor(marz, sotun_masahat) as cursornz:
    for radf in cursornz:
        masr = (f'{radf[0]}')


#now we make conditional area for layers. 
masri = int(float(masr))

fp = arcpy.ListFeatureClasses("","POINT")
fl = arcpy.ListFeatureClasses("","POYLINE")

harimk = masri/1000000
harimb = str(harimk) + ' '+ 'Meter'

if masri > 2000000:
    for ll in fl:
        arcpy.Buffer_analysis(ll,'xl_{}'.format(ll),"20 Meter")
else:
    for p in fp:
        arcpy.Buffer_analysis(p,'yp_{}'.format(p),harimb) 


#end 12

