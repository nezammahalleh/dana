#code using while loop: 

import arcpy

try:

    worknz = raw_input("E:/Test/aq")
    arcpy.env.workspace = worknz

    fcs = "wq.shp"
    field = "fac" 

    shart = "\"fac\" = 'WA'"
    searchCursornz = arcpy.SearchCursor(fcs, shart, "", "", "")
    row = searchCursnz.next()

    while row:
        print(row.getValue(field)) 
        row = searchCursnz.next


except Exception as e:
        print "Error: " + str(e)
        print arcpy.GetMessages()
        arcpy.AddError(e)
