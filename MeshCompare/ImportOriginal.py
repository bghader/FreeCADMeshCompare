## Version 0.2 this file contains the first step of the project, the import procedure for the 2 STL files

#################################ChangeLog########################################################
## Version 0.1 		The function were created statically, not being able to take argument using the open window mechanism 
## Version 0.2		These function were modified to be part of the Benchmark GUI
## Version 0.3 		TODO  Finishe, added 2 variables pathOfOriginalOriginal and pathOfToCompare
## Version 0.4		solved the static path problem
## Version 0.5		Added icons support
## Version 0.6 		Added Filter for STL and OBJ files


## the Icons Added in Version 0.5 are not mine 
## you may find the credits below
## Addition icon : https://www.flaticon.com/authors/icomoon
import sys
import Mesh
import FreeCAD 
import FreeCADGui
import PySide
from PySide import QtCore, QtGui



class Original: ## Importing the Original File 
 "this class will be used to import the original file of the comparaison"
 def Activated(self):
  if not (FreeCAD.activeDocument()):
   FreeCAD.newDocument("MeshCompare")
  pathOfOriginal = PySide.QtGui.QFileDialog.getOpenFileName(caption = "Please select the original file name" , filter = ('*.stl *.obj')) 
  pathOfOriginalascii = pathOfOriginal[0].encode("ascii")
  OriginalMesh = Mesh.Mesh(pathOfOriginalascii)
  OriginalObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "OriginalMesh")
  OriginalObject.Mesh = OriginalMesh
 def GetResources(self):
	directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\interface.png'
	return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'Import The Original File'} 
FreeCADGui.addCommand('Original', Original()) 


class ToCompare:	
 "this class will be used to import the comparaison file of the comparaison"
 def Activated(self):
  if not (FreeCAD.activeDocument()):
   FreeCAD.newDocument("MeshCompare")
  pathToCompare = PySide.QtGui.QFileDialog.getOpenFileName(caption = "Please select the Modified file name", filter = ('*.stl *.obj')) 
  pathToCompareascii = pathToCompare[0].encode("ascii")
  ToCompareMesh = Mesh.Mesh(pathToCompareascii)
  ToCompareObject = FreeCAD.ActiveDocument.addObject ("Mesh::Feature", "ToCompareMesh")
  ToCompareObject.Mesh = ToCompareMesh
 def GetResources(self):
	directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\File.png'
	return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'Import The comparaison File'} 
FreeCADGui.addCommand('ToCompare', ToCompare()) 
