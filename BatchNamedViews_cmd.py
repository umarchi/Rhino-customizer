import System
import Rhino as rh
import scriptcontext as sc
import rhinoscriptsyntax as rs

__commandname__ = "BatchNamedView"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    print __commandname__ 
    fileLocation = rh.RhinoDoc.ActiveDoc.Path
    fileName = fileLocation.replace(".3dm","")

    allNamedViews = rs.NamedViews()
    allDisplayModes = rs.ViewDisplayModes()

    selectedViews = rs.MultiListBox(allNamedViews, "Select views to export.")
    selectedDisplayMode = rs.MultiListBox(allDisplayModes, "Select views to export.")

    resolutionList = ["1,920*1,080", "2,560*1,440", "3,820*2,160", "5,120*2,880"]
    resolution = rs.ListBox(resolutionList, "Select views to export.")


    if(resolution == "1,920*1,080"):
        for view in selectedViews:
            rs.RestoreNamedView(view)
            rs.Command("-SetDisplayMode" + str(selectedDisplayMode))
            saveName = chr(34) + fileName + "_" + view + ".png" +chr(34)
            rs.Command("-ViewCaptureToFile "+ " _Width 1980 _Height 1080 " + saveName)
        
    elif(resolution == "2,560*1,440"):
        for view in selectedViews:
            rs.RestoreNamedView(view)
            rs.Command("-SetDisplayMode" + str(selectedDisplayMode))
            saveName = chr(34) + fileName + "_" + view + ".png" +chr(34)
            rs.Command("-ViewCaptureToFile "+ " _Width 2560 _Height 1440 " + saveName)
        
    elif(resolution == "3,820*2,160"):
        for view in selectedViews:
            rs.RestoreNamedView(view)
            rs.Command("-SetDisplayMode" + str(selectedDisplayMode))
            saveName = chr(34) + fileName + "_" + view + ".png" +chr(34)
            rs.Command("-ViewCaptureToFile "+ " _Width 3820 _Height 2160 " + saveName)
        
    elif(resolution == "5,120*2,880"):
        for view in selectedViews:
            rs.RestoreNamedView(view)
            rs.Command("-SetDisplayMode" + str(selectedDisplayMode))
            saveName = chr(34) + fileName + "_" + view + ".png" +chr(34)
            rs.Command("-ViewCaptureToFile "+ " _Width 5120 _Height 2880 " + saveName)

    return 0
