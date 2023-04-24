from pyfbsdk import *
from pyfbsdk_additions import *
from PySide import QtGui
from PySide import shiboken
import sys
sys.path.append("I:\\MOTIONBUILDER\\FCurve")
import FcurveUIBuild  
class NativeWidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWidgetParent):
        self.mNativeQtWidget = FcurveUIBuild.FCurveDialog()
        return shiboken.getCppPointer(self.mNativeQtWidget)[0]
  
        
class NativeQtWidgetTool(FBTool):
    def BuildLayout(self):
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0,FBAttachType.kFBAttachBottom,"")
        self.AddRegion("main","main", x, y, w, h)
        self.SetControl("main", self.mNativeWidgetHolder)
                
    def __init__(self, name):
        FBTool.__init__(self, name)
        self.mNativeWidgetHolder = NativeWidgetHolder();
        self.BuildLayout()
        self.StartSizeX = 350
        self.StartSizeY = 250   
        self.MaxSizeY = 175     
        self.MaxSizeX = 331    
     
        
gToolName = "FCurve Transfer"
FBDestroyToolByName(gToolName)

if gToolName in FBToolList:
    tool = FBToolList[gToolName]
    ShowTool(tool)
else:
    tool=NativeQtWidgetTool(gToolName)
    FBAddTool(tool)
    ShowTool(tool)

        
