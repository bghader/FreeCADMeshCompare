# FreeCADMeshCompare
This is an Add-On for the popular open-source tool FreeCAD adding a functionality of version control for Mesh Files
Project of EECE 437 Spring 2018 - AUB 
Author: Bilal M. Ghader
 ###########INTRODUCTION################
This repositroy is a class project aiming to add a version control tool for FreeCAD. 
The current Files present in the repository are as follows: 

-->	Init.py : Used to load dependencies files from the FreeCAD libraries and setup some required settings.

-->	InitGui.py :Configure the GUI of the Benchmark MeshCompare. 
--> ImportOriginal.py : Includes the functions Original and ToCompare used to import the STL files. 
	
--> Diff.py : Includes the main analysis functions functions that takes 2 STL files and compare them.  Init.py
--> Export.py:  overloads the export function of FreeCAD in order to get only stl and obj file format 
--> Visualization.py: include one function smooth for better Mesh Visualization


To be able to use this tool, the FreeCAD software is needed. After downloading
FreeCAD, kindly perform the following steps:
1. download this repository 
2. copy the MeshCompare folder
3. Paste the MeshCompare folder in FreeCAD Mod directory usually found under C:/Program Files/FreeCAD 0.16/Modn
4. Relaunch FreeCAD, you should find MeshCompare in FreeCAD Workbench List.
