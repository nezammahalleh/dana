import arcpy
from arcpy.sa import *
arcpy.env.workspace = r'E:\Test\qq'
arcpy.env.overwriteOutput = True

q=1
while q<5:
    ot= 'Norr_{}'.format(q)    #produce name 
    tr= arcpy.sa.CreateNormalRaster()   #create raster 
    tr.save(ot)   #save created raster with the produced name 
    q=q+1   #go to the next name 
del tr
print "complete"
