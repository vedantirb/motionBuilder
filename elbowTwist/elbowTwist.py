
from pyfbsdk import *
from pyfbsdk_additions import *
import sys


class TwistedLegs(object):
    def selectedElements(self):
        allObject = [] 
        selectedModels = FBModelList()
        FBGetSelectedModels(selectedModels,None, True, True) 
        for model in selectedModels:
            print  model.Name
            if model.Name.find("Elbow_Controller")>=0 and model.Type.name == "kFBMarkerTypeStandard":
                allObject.append(model) 
        return allObject

    def apply_leg_twist(self):     
        selected = self.selectedElements()
        marker=selected[0] if selected else None
        if not marker:
            FBMessageBox("Warning", "Selection of elbow is required !!","OK") 
            return
        GetRefTwistProperty = None  
        if marker.PropertyList.Find("ctrl1.Twist"):
            GetRefTwistProperty =  marker.PropertyList.Find("ctrl1.Twist").GetReferencedProperty()
        elif marker.PropertyList.Find("Left_Low_ChainIk