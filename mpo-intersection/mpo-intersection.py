import arcpy

mpo = 'C:/Users/jjiang/AppData/Roaming/ESRI/Desktop10.3/ArcCatalog/Connection to DOTICSQLP31.dot.state.oh.us.sde/TIMS.TIMS.REFER_MPO'
lrs = r'W:\GIS projects\KPI Report V3 - Andrew Willims\PRD31.GIS.TSRV.sde\GIS.TSRV.ODOT_LRS_Routes_Hist'
outDir = r'W:\GIS projects\KPI Report V3 - Andrew Willims\KPI Report V3.gdb'

for year in range (2009,2016):

	where_clause = "Perp" + "=" + str(year)
	try:
		arcpy.env.workspace = outDir
		# create lrs layer	
		arcpy.MakeFeatureLayer_management(lrs, "lrs_lyr", where_clause)
		print str(year)+' lrs layer is created'
		
		# select the lrs intersect mpo and create a layer
		arcpy.SelectLayerByLocation_management('lrs_lyr',"INTERSECT",mpo)
		print str(year)+' lrs layer is selected'
		
		# create lrs subset layer	
		arcpy.MakeFeatureLayer_management('lrs_lyr','lrs_subset')
		print str(year)+' lrs subset layer created'
		
		# locate mpo along lrs subset
		arcpy.LocateFeaturesAlongRoutes_lr(mpo,'lrs_subset',"NLF_ID",'','lrs_mpo_' + str(year),"NLF_ID LINE CTL_BEGIN_NBR CTL_END_NBR")
		print str(year)+' lrs_mpo table created'
		
		arcpy.Delete_management('lrs_subset')
		arcpy.Delete_management('lrs_lyr')
		print 'lrs and subset layer deleted'
		
	except:
		print(arcpy.GetMessages()) 

raw_input()



