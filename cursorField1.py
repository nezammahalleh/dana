#Search cursors can be iterated with a for loop or in a while loop using the cursor's next method to return the next row. When using the next method on a cursor to retrieve all rows in a table containing N rows, the script must make N calls to next. A call to next after the last row in the result set has been retrieved returns None, which is a Python data type that acts here as a placeholder.

#Using SearchCursor with a for loop.



import arcpy

layer = "E:/Test/aq/wq.shp"
field = "Name"
mycursor = arcpy.SearchCursor(layer)
for mm in mycursor:
    print(mm.getValue(field))
