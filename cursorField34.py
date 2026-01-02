#Summary

#The UpdateCursor function creates a cursor that allows you to update or delete rows
#on the specified feature class, shapefile, or table. The cursor places a lock on the data that
#will remain until either the script completes or the update cursor object is deleted.
#The arcpy.da cursors (arcpy.da.SearchCursor, arcpy.da.UpdateCursor, and arcpy.da.InsertCursor)
#were introduced with ArcGIS 10.1 to provide significantly faster performance over the previously
#existing set of cursor functions (arcpy.SearchCursor, arcpy.UpdateCursor, and arcpy.InsertCursor).
#The original cursors are provided only for continuing backward compatibility.

#Update cursors can be iterated with a for loop or in a while loop using the cursor's next
#method to return the next row. When using the next method on a cursor to retrieve all rows in a
#table containing N rows, the script must make N calls to next. A call to next after the last row
#in the result set has been retrieved returns None, which is a Python data type that acts here
#as a placeholder.

#Using UpdateCursor with a for loop.


import arcpy

wq = "e:/test/aq/wq.shp"
field1 = "val"
field2 = "val2"

cursor = arcpy.UpdateCursor(wq)
for fz in cursor:
    if field1 > 5:
        print fz.setValue(field2, fz.getValue(field1) * 100.0)
    else:
        print fz.setValue(field2, fz.getValue(field1) * 3.0)
    # field2 will be equal to field1 multiplied by 3.0
    cursor.updateRow(fz)
