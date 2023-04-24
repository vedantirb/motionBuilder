# selected model
from pyfbsdk import *
import pyfbsdk

def selectedElements():
    allObject = [] 
    selectedModels = FBModelList()
    FBGetSelectedModels(selectedModels,None, True, True) 
    if selectedModels:
        for model in selectedModels:
            allObject.append(model) 
    return allObject


def transferActivity(sourceObject, destTransferObject, sourceController, sourceAxies, destiController, destiDataAxies, activity, activityObject, opObjectInvertScale):

    if sourceController == "T":
        sourceAnim = sourceObject.Translation.GetAnimationNode()
    elif sourceController == "R":
        sourceAnim = sourceObject.Rotation.GetAnimationNode()
    sourceAnimNodes = sourceAnim.Nodes
    i = 0
    if activity == 'TransferCurve':
        destObject = destTransferObject
    elif activity in ('offsetUp', 'offsetDown'):
        destObject =  activityObject
    else:
        destObject =  opObjectInvertScale
    
    lFilter = FBFilterManager().CreateFilter( 'Key Reducing' )
        
    for each in destObject:
        each.Translation.SetAnimated(True)
        each.Rotation.SetAnimated(True)
        each.Scaling.SetAnimated(True)
        if destiController == "T":
            destiAnim = each.Translation.GetAnimationNode()
        elif destiController == "R":
            destiAnim = each.Rotation.GetAnimationNode()

        destiAnimNodes = destiAnim.Nodes
        for eachNode in sourceAnimNodes:
            axies = eachNode.Name
            if axies == sourceAxies:
                for distNode in destiAnimNodes:
                    if destiDataAxies == distNode.Name:
                        if activity == 'TransferCurve':
                            distNode.FCurve.KeyReplaceBy(eachNode.FCurve)
                            lFilter.PropertyList.Find( 'Precision' ).Data = 1.0
                            lFilter.Apply( destiAnim, True )
                        elif activity == 'offsetUp':
                            i = i+1
                            offsetUp(distNode, i)

                        elif activity == 'offsetDown':
                            i = i-1
                            offsetDown(distNode, i)

                        elif activity == 'Invert':
                            invert(distNode)

                        elif activity == 'scaleUp':
                            i = 1.1
                            print "Scale Up"
                            scale(distNode, i)
                        elif activity == 'scaleDown':
                            i = 0.9
                            print "Scale Down"
                            scale(distNode, i)

def invert(distNode):
    for key in distNode.FCurve.Keys:
        key.Value = (key.Value * -1)  
          
def offsetDown(distNode, offset):
    for key in distNode.FCurve.Keys:
        valueTime = (key.Time.GetFrame() + offset)
        timeDef = FBTime(0, 0, 0, valueTime, 0)
        key.Time = timeDef


def offsetUp(distNode, offset):
    for key in reversed(sorted(distNode.FCurve.Keys)):
        valueTime = (key.Time.GetFrame() + offset)
        timeDef = FBTime(0, 0, 0, valueTime, 0)
        key.Time = timeDef
        
def scale(distNode, scale):
    print "Scale "
    for key in distNode.FCurve.Keys:
        key.Value = (key.Value * scale)  
