class MyWorkbench (Workbench): 
   MenuText = "MeshComapre"
   def Initialize(self):
       import ImportOriginal
       import Mesh
       import MeshGui
       import Diff
       commandslist = ["Original", "ToCompare" , "Addition" , "Deletion"]
       self.appendToolbar("MeshComapre",commandslist)
Gui.addWorkbench(MyWorkbench()) 