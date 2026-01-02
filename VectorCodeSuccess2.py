

import arcpy

from arcpy import *

wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\str10.gdb"

masahat = 500


fp = arcpy.ListFeatureClasses("","POINT")
fl = arcpy.ListFeatureClasses("","POYLINE")

if masahat > 200:
    for ll in fl:
        arcpy.Buffer_analysis(ll,'xl_{}'.format(ll),"20 Meter")
else:
    for p in fp:
        arcpy.Buffer_analysis(p,'yp_{}'.format(p),"35 Meter")




#n
#python format 

sn="Happy"

for i in ["iran","egypt","turkey","russia"]:
    ct = i
    dx2 = "Here is {} and we are {}. :)".format(ct,sn)
    print(dx2)

#n


import arcpy
wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\st10.gdb"
fc = "points"
sotun = "type"

cursornz = arcpy.SearchCursor(fc)

for rdf in cursornz:
    db = rdf.getValue(sotun)
    print(db)


#n
# if greater than 500 , do buffer all polylines if not do buffer points layers in all gdb. 
import arcpy

from arcpy import *

wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\str10.gdb"

masahat = 500


fp = arcpy.ListFeatureClasses("","POINT")
fl = arcpy.ListFeatureClasses("","POYLINE")

if masahat > 200:
    for ll in fl:
        arcpy.Buffer_analysis(ll,'xl_{}'.format(ll),"20 Meter")
else:
    for p in fp:
        arcpy.Buffer_analysis(p,'yp_{}'.format(p),"masahat Meter")

#n


import arcpy
from arcpy import *
wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\str10.gdb"
laye = "places"
sotun = "r_n"
arzesh = 24

cursornz = arcpy.UpdateCursor(laye)

for radif in cursornz:
    radif.setValue(sotun,arzesh)
    cursornz.updateRow(radif)

del radif
del cursornz

#n

import arcpy

fc = r"E:\TEST\ASHPs\test6\mkyy.gdb\awadi"

arcpy.management.AddField(fc, "sot", "LONG", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')


cursornz= arcpy.UpdateCursor(fc)

for radif in cursornz:
    if radif.getValue("kk") > 5:
        radif.setValue("sot", 25)
    else:
        radif.setValue("sot",33)
    cursornz.updateRow(radif)
    
del cursornz
del radif


#n


import arcpy
wq = arcpy.env.workspace = r"E:\TEST\ASHPs\test6\str10.gdb"
marz = "bordr"
fields = ['Shape_Area', 'taj', 'SHAPE@XY']
# For each row, print the WELL_ID and WELL_TYPE fields, and
# the feature's x,y coordinates
with arcpy.da.SearchCursor(marz, fields) as cursornz:
    for radf in cursornz:
        print(f'{radf[0]}, {radf[1]}, {radf[2]}')


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

