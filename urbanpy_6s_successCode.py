

#n

import os
import arcpy

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = r"E:\UrbanPython\data\bbbikeex\planet_51.39187,35.7981_51.42382,35.81487-shp\shape"

# Use the ListFeatureClasses function to return a list of
#  shapefiles.
featureclasses = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.CopyFeatures_management(
        fc, os.path.join("E:/UrbanPython/data/lu/landuse.gdb",
                         os.path.splitext(fc)[0]))

#n
# how 'x_{}'.format() works for layers. 

#  ''.format()

ff = ["Tehran","Behshahr"]
nb = 24


mt = 'There are 24 shopping center in {}'.format(ff[1])
print(mt)

#n
#how use 'd_[]'.format() for many layers 
#  ''.format()

ff = ["Tehran","Behshahr"]
nb = ["shopping center","drug store","tower"]


for i in  ff:
    for n in nb:
        mt = 'There is {} in {}'.format(n,i)
        print(mt)

#n




ct = ["Tehran","Behshahr","Ahvaz"]
nb = [24000,35000,18000]
#nbt = str(nb)

for i in ct:
    mtn = 'We have {} buildings in {}'.format(str(nb[2]),i)
    print(mtn)


#n


import arcpy

arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\landuse.gdb"


mk = arcpy.ListFeatureClasses("p*")

for i in mk:
    tk = arcpy.analysis.Buffer(i,'bf4_{}'.format(i),"25 Meter")
    arcpy.management.AddField(tk,"pawiii","LONG")
    
#n
#intersect many layers one by one , 

import arcpy

knn = arcpy.ListFeatureClasses('',"POLYGON")
kjj = arcpy.ListFeatureClasses('',"POLYLINE")

for n in knn:
    for j in kjj:
        arcpy.analysis.Intersect([n,j], 'nj2_{}_{}'.format(n,j), "ALL", None, "INPUT")
        
#n

#doing different processes by layer-type of point and polyline based on Shape_Area variable. 


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
#how we can edit border layer and make code to do different processes. 

import arcpy
import math

ss = 15000

we = math.log10(ss) * math.sqrt(ss+1000)


print(we)

#n

import arcpy
import math

ss = 15000
shahr = "Tehran"

we = math.log10(ss) * math.sqrt(ss+1000)


mt = 'There is {} bridge in {} City.'.format(ss,shahr)

si = "We have " + str(ss) + " bridges in Tehran."

print(mt)
print(si)

#n


import arcpy
from arcpy import* 

wq4 = arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\landuse.gdb"

kp = arcpy.ListFeatureClasses('',"POLYLINE")
kt = arcpy.ListFeatureClasses('',"POINT")

marz = "bordr"
sotun = "Shape_Area"

with arcpy.da.SearchCursor(marz,sotun) as cursornz:
    for radif in cursornz:
        mas = radif[0]

#masahat = 120
mash = float(mas)




if mash > 5000000:
    for p in kp:
        arcpy.Buffer_analysis(p,'bfpol3_{}'.format(p),"20 Meter")
else:
    for t in kt:
        arcpy.Buffer_analysis(t,'bfpoint3_{}'.format(t),"33 Meter")

#n
#why we use radif[] instead of just radif
import arcpy
from arcpy import* 
wq4 = arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\landuse.gdb"

marz = "bordr"
sotun = "Shape_Area"

with arcpy.da.SearchCursor(marz,sotun) as cursornz:
    for radif in cursornz:
        mas = radif[0]
print(mas)

#n

import arcpy
from arcpy import* 
import math

wq4 = arcpy.env.workspace = r"E:\TEST\ASHPs\tst7\landuse.gdb"

kp = arcpy.ListFeatureClasses('',"POLYLINE")
kt = arcpy.ListFeatureClasses('',"POINT")

marz = "bordr"
sotun = "Shape_Area"

with arcpy.da.SearchCursor(marz,sotun) as cursornz:
    for radif in cursornz:
        mas = radif[0]

#masahat = 120
mash = float(mas)

wsg = math.log10(mash)

bufx = (str(wsg) + ' '+ "Meter")

if mash > 5000000:
    for p in kp:
        arcpy.Buffer_analysis(p,'bfpol4_{}'.format(p),"20 Meter")
else:
    for t in kt:
        arcpy.Buffer_analysis(t,'bfpoint4_{}'.format(t),bufx)

#n


