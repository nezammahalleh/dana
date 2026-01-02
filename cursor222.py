



#List field contents for Counties.shp. Cursor is sorted by state name and population.


import arcpy

# Open a searchcursor
#  Input: C:/Data/Counties.shp
#  Fields: NAME; STATE_NAME; POP2000
#  Sort fields: STATE_NAME A; POP2000 D
rows = arcpy.SearchCursor("e:/Test/aq/wq.shp",
                          fields="Name; fac; nazdik",
                          sort_fields="fac; nazdik")

# Iterate through the rows in the cursor and print out the
# state name, county and population of each.
for row in rows:
    print("Name: {0}, fac: {1}, nazdik: {2}".format(
        row.getValue("Name"),
        row.getValue("fac"),
        row.getValue("nazdik")))

