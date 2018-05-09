## Modify file 
## Version 0.1 		compare 2 meshes to give back them giving back the Added Part
## Version 0.2		Gives back the deleted part also 
## Version 0.3		Added the Similarities function 
## Version 0.4		Added icons



## the Icons Added in Version 0.4 are not mine 
## you may find the credits below
## Addition icon : https://www.flaticon.com/authors/icomoon
import Mesh
import FreeCAD 
import FreeCADGui

class Addition: ## Tracking the additions to the original file

 "this class will return the additions to the original file when compared to the to Compare file"
 def Activated (self):
    Diff = FreeCAD.ActiveDocument.OriginalMesh.Mesh.difference(FreeCAD.ActiveDocument.ToCompareMesh.Mesh)
    Doc  =  FreeCAD.newDocument("Additions")
    newObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Diff")
    newObject.Mesh = Diff
  
 def GetResources(self):
     directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\plus.png'
     return {'Pixmap' :directory, 'MenuText': 'Line', 'ToolTip': 'return the additions '} 
FreeCADGui.addCommand('Addition', Addition()) 


class Deletion: ## Tracking the Deletions to the original file

 "this class will return the Deletions to the original file when compared to the to Compare file"
 def Activated(self):
 
    Diff = FreeCAD.ActiveDocument.ToCompareMesh.Mesh.difference(FreeCAD.ActiveDocument.OriginalMesh.Mesh)
    Doc  =  FreeCAD.newDocument("Deletion")
    newObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Diff")
    newObject.Mesh = Diff
	
 def GetResources(self):
  directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\minus.png'
  return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'return Deletions'} 
FreeCADGui.addCommand('Deletion', Deletion()) 

class Similarities: 
 "this class will return the Similarities between the original file and the compare file"
 def Activated(self): 
  
	Deletion = FreeCAD.ActiveDocument.ToCompareMesh.Mesh.difference(FreeCAD.ActiveDocument.OriginalMesh.Mesh)
	Diff     = FreeCAD.ActiveDocument.OriginalMesh.Mesh.difference(Deletion)
	Doc  =  FreeCAD.newDocument("Similarities")
	newObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Diff")
	newObject.Mesh = Diff
	
 def GetResources(self):
  directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\Button.png' 
  return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'return Similarities'} 
FreeCADGui.addCommand('Similarities', Similarities()) 



class Analyze: ## Tracking the Deletions to the original file

 "this class will return the complete Analysis"
 def Activated(self):

    Del = FreeCAD.ActiveDocument.ToCompareMesh.Mesh.difference(FreeCAD.ActiveDocument.OriginalMesh.Mesh)
    Add = FreeCAD.ActiveDocument.OriginalMesh.Mesh.difference(FreeCAD.ActiveDocument.ToCompareMesh.Mesh)
    Sim = FreeCAD.ActiveDocument.OriginalMesh.Mesh.difference(Del)
    Doc  =  FreeCAD.newDocument("Analysis")
    newObjectSim = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Sim")
    newObjectSim.Mesh = Sim
    newObjectAdd = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Add")
    newObjectAdd.Mesh = Add
    newObjectDel = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "Del")
    newObjectDel.Mesh = Del
    FreeCAD.ActiveDocument.Add.ViewObject.ShapeColor = (1.00 , 0.00 , 0.00)
    FreeCAD.ActiveDocument.Sim.ViewObject.ShapeColor = (0.00 , 1.00 , 0.00)
    FreeCAD.ActiveDocument.Del.ViewObject.ShapeColor = (0.00 , 0.00 , 1.00)
  
  
 def GetResources(self):
  directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\layer.png' 
  return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'Perform full analysis'} 
FreeCADGui.addCommand('Analyze', Analyze()) 
  
  
  