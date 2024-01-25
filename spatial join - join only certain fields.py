## GOAL: Spatial join, but only join certain fields, using field mapping.

# Note: I think this has recently been introduced in ArcGIS Pro. 
#  But I wrote this tool before it was available.

################################################################################

import arcpy as a
from arcpy import env

a.mapping.MapDocument('CURRENT')   # use if running within ArcMap
mxd = a.mapping.MapDocument('CURRENT')   # use if running within ArcMap

#######################

# OR: TO USE AS A FUNCTION:

def SpatialJoinField(targetfc,joinfc,outfc,joinop,jointype,joinfields,matchoption,searchradius):
	# use field mappings to join only selected field(s)
	fieldmappings =	a.FieldMappings()
	fieldmappings.addTable(targetfc)  				# keep all fields from targetfc
	for f in a.ListFields(joinfc):
		if f.name in joinfields:
			fm = a.FieldMap() # create empty field map object for one field
			fm.addInputField(joinfc,f.name) # populate field map with input field
			fieldmappings.addFieldMap(fm) # add field map to field mappings object
		else:
			pass
	a.SpatialJoin_analysis(targetfc,joinfc,outfc,joinop,jointype,fieldmappings,matchoption,searchradius)

# to run above function:
targetfc = 		""
joinfc = 		""
outfc = 		""  # output fc 
joinop = 		""	# "JOIN_ONE_TO_ONE" - DEFAULT (OR "JOIN_ONE_TO_MANY")
jointype = 		""	# "KEEP_ALL" - DEFAULT (OR "KEEP_COMMON")
joinfields = 	["[field name]","[field name]"]  	# list of field(s) to join
matchoption = 	"INTERSECT"	# "INTERSECT", etc.
searchradius = 	"1 Feet"	# "1 Feet", etc. (optional)
SpatialJoinField(targetfc,joinfc,outfc,joinop,jointype,joinfields,matchoption,searchradius)