import System
import Rhino as rh
import scriptcontext as sc
import rhinoscriptsyntax as rs

fileLocation = rh.RhinoDoc.ActiveDoc.Path
fileName = fileLocation.replace(".3dm","")

allNamedViews = rs.NamedViews()
allDisplayModes = rs.ViewDisplayModes()

selectedViews = rs.MultiListBox(allNamedViews, "Select views to export.")
selectedDisplayMode = rs.MultiListBox(allDisplayModes, "Select views to export.")

for view in selectedViews:
    rs.RestoreNamedView(view)
    rs.Command("-SetDisplayMode" + str(selectedDisplayMode))
    saveName = chr(34) + fileName + "_" + view + ".png" +chr(34)
    rs.Command("-ViewCaptureToFile "+ " _Width 1980 _Height 1080 _Scale 1 " + saveName)
