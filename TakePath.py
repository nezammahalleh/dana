import arcpy
from arcpy import*
from sys import argv

arcpy.env.workspace = r'C:\Project_Nezammahalleh\MyProject7\vol2.gdb' 

arcpy.env.overwriteOutput = True

idx_d = r'C:\Project_Nezammahalleh\MyProject7\vol2.gdb\kd51272540'
idx_f = r'C:\Project_Nezammahalleh\MyProject7\vol2.gdb\kf51272540'


 
dec = arcpy.Describe (idx_f)
pathy = dec.path

print(pathy)

#nr = arcpy.analysis.Select(idx_d, f'jc_{idx_f}', "OBJECTID" + '='+str(minfdd))



##
## 
##
##qqf =  (arcpy.ListFeatureClasses("F*",""))
##qqd =  (arcpy.ListFeatureClasses("D*",""))
##qqpc =  (arcpy.ListFeatureClasses("pc*",""))
##
##for idx_f in qqf:
##    number = idx_f[1:]
##
##    try:
##        idx_d = qqd[qqd.index('D'+number)]
##    except:
##        print(number)
##    
##        
