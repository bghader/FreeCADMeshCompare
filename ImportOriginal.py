## Version 0.2 this file contains the first step of the project, the import procedure for the 2 STL files

#################################ChangeLog########################################################
## Version 0.1 		The function were created statically, not being able to take argument using the open window mechanism 
## Version 0.2		These function were modified to be part of the Benchmark GUI
## TODO				--> Select file using open file function

import Mesh
import FreeCAD 
import FreeCADGui


class Original: ## Importing the Original File 
 "this class will be used to import the original file of the comparaison"
 def Activated(self):
  FreeCAD.newDocument("Compare")
  OriginalMesh = Mesh.Mesh("C:/Users/Bilal/Documents/AUB/EECE 437/10mm_test_cube/10mm_test_cube/Cube2.stl")
  OriginalObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "OriginalMesh")
  OriginalObject.Mesh = OriginalMesh
 def GetResources(self): 
     return {'Pixmap' : 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Import The Original File'} 
FreeCADGui.addCommand('Original', Original()) 


class ToCompare:	
 "this class will be used to import the comparaison file of the comparaison"
 def Activated(self):
  ToCompareMesh = Mesh.Mesh("C:/Users/Bilal/Documents/AUB/EECE 437/10mm_test_cube/10mm_test_cube/10mm_test_cube.stl")
  ToCompareObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "ToCompareMesh")
  ToCompareObject.Mesh = ToCompareMesh
 def GetResources(self): 
     return {'Pixmap' : 'path_to_an_icon/line_icon.png', 'MenuText': 'Line', 'ToolTip': 'Import The comparaison File'} 
FreeCADGui.addCommand('ToCompare', ToCompare()) 
