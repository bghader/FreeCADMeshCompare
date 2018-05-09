## Export Function 

## Version 0.1  no filter for saving type, saving directory static
## Version 0.2	added icon support
## Version 0.3  added dynamic saving location using PySide
## Version 0.4  added filter control on file export type
## Version 0.5 	added a warning message in case no mesh was selected
## Version 0.6	Added Warnings
import Mesh
import FreeCAD 
import FreeCADGui 
import PySide
from PySide import QtCore, QtGui

class Export: 
 def Activated(self): 
	if not (FreeCAD.ActiveDocument.ActiveObject):
		Widget  = PySide.QtGui.QWidget()
		DialogueBox = PySide.QtGui.QMessageBox() 
		DialogueBox.warning(Widget,'incorrect selection', 'Kindly select a Mesh to export')
		
		
	else : 
		directory = PySide.QtGui.QFileDialog.getSaveFileName(caption = "Select location of export", filter = ('*.stl *.obj'))
		exportVector = []
		exportVector.append(FreeCAD.ActiveDocument.ActiveObject)
		Mesh.export(exportVector,directory[0])
	
 def GetResources(self):
	directory = str(FreeCAD.getHomePath()) + 'Mod\MeshCompare\icons\export.png'
	return {'Pixmap' : directory, 'MenuText': 'Line', 'ToolTip': 'Export File'}

	
FreeCADGui.addCommand('Export', Export()) 

### Modif TOol
#import Mesh
#mesh=App.ActiveDocument.Owl.Mesh.copy()
#mat = App.Matrix()
#factor = 75 / 7.347
#mat.scale(factor,factor,factor)
#mesh.transform(mat)
#Mesh.show(mesh)