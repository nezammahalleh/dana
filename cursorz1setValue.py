import arcpy

# Set the workspace
arcpy.env.workspace =  "E:\Test\New Folder"

# Use row object to get and set field values
cursorz = arcpy.UpdateCursor("Export_Output_4.dbf", '"NPP" = \'gg\'' )

# Iterate through rows and update values
for kok in cursorz:
    kok.setValue("NPP", "Great gate")
    cursorz.updateRow(kok)

del cursorz, kok
