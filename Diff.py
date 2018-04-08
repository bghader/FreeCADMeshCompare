## Modify file 
## Version 0.1 		compare 2 meshes to give back them giving back the Added Part
## Version 0.2		Gives back the deleted part also 
## TODO 			--> Select Meshes Dynamically

import Mesh
import FreeCAD 
import FreeCADGui

class Addition: ## Tracking the additions to the original file

 "this class will return the additions to the original file when compared to the to Compare file"
 def __init__(self):
  Diff = FreeCAD.ActiveDocument.OriginalMesh.Mesh.difference(FreeCAD.ActiveDocument.ToCompareMesh.Mesh)
  Doc  =  FreeCAD.newDocument("Additions")
  newObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Diff")
  newObject.Mesh = Diff


class Deletion: ## Tracking the Deletions to the original file

 "this class will return the Deletions to the original file when compared to the to Compare file"
 def __init__(self, OriginalMesh, ToCompareMesh):
  Diff = ToCompareMesh.Mesh.difference(OriginalMesh.Mesh)
  Doc  =  FreeCAD.newDocument("Deletion")
  newObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Diff")
  newObject.Mesh = Diff
 