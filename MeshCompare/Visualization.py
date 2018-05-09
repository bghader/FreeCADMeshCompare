## Visualization Tool 

# first Function to be implemented is a function to smooth the surface of our shapes, because the Mesh can be corrupted
import Mesh
import FreeCAD 
import FreeCADGui
import PySide
from PySide import QtCore, QtGui

class Smooth: 
 "needed to correct the Mesh After comparaison"
 def Activated (self):
 	if not (FreeCAD.ActiveDocument.ActiveObject):
		Widget  = PySide.QtGui.QWidget()
		DialogueBox = PySide.QtGui.QMessageBox() 
		DialogueBox.warning(Widget,'incorrect selection', 'Kindly select a Mesh to export')

	else : 
		FreeCAD.ActiveDocument.ActiveObject.smooth() ;
		
 def GetResources(self):
  directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\arrows.png'
  return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'Smooth Mesh'}
FreeCADGui.addCommand('Smooth', Smooth())

