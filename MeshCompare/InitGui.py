class MyWorkbench (Workbench): 
   def __init__(self):
	self.__class__.MenuText = "MeshCompare"
   def Initialize(self):
	import ImportOriginal
	import Mesh
	import MeshGui
	import Diff
	import Export
	import Visualization
	VisualizationCommand = ["Smooth", "Scale"]
	ExportCommand= ["Export"]
	CompareList =[ "Addition" , "Deletion", "Similarities", "Analyze"]
	ImportList =["Original", "ToCompare" ] 
	self.appendToolbar("Import",ImportList)
	self.appendToolbar("Mesh Compare",CompareList)
	self.appendToolbar("Export",ExportCommand)
	self.appendToolbar("VIsualization",VisualizationCommand)
	
		
Gui.addWorkbench(MyWorkbench())  