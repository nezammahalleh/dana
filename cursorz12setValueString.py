import arcpy

# Set the workspace
arcpy.env.workspace = "E:\Test\New Folder"

# Use row object to get and set field values
cursor = arcpy.UpdateCursor("Export_Output_4.dbf", '"NPP" = \'wq\'' )

# Iterate through rows and update values
for row in cursor:
    row.setValue("NPP", "world questions")
    cursor.updateRow(row)

del cursor, row
