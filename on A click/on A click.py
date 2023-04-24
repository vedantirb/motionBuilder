from pyfbsdk import *
from pyfbsdk_additions import *
import sys
class DataSlection(object):
    def __init__(self):
        self.selection = []
        self.speedIndex = 0
        self.speedToggle = [1, 0.5, 0.33]
        self.currentTakeIndex = self.setCurrentTakeIndex()
        self.toggleFKIK_pt = "IK"
        self.app = FBApplication()

        
    def PopulateLayout(self, mainLyt):
        x = FBAddRegionParam(0,FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0,FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0,FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(25,FBAttachType.kFBAttachNone,"")
        mainLyt.AddRegion("main","main", x, y, w, h)
        lyt = FBHBoxLayout()
        mainLyt.SetControl("main",lyt)      
        
        addSelect = FBButton()
        addSelect.Caption = "Add Sel"
        lyt.Add(addSelect,60)    
        addSelect.OnClick.Add(self.addSelection)    
        
        applySel = FBButton()
        applySel.Caption = "Select"
        lyt.Add(applySel,60)
        applySel.OnClick.Add(self.applySelction)
        
        ###############
        playerSpeed = FBButton()
        playerSpeed.Caption = "PBSpeed"        
        lyt.Add(playerSpeed,60)    
        playerSpeed.OnClick.Add(self.playerSpeedControl)    
        
        ###################
        snapMode = FBButton()
        snapMode.Caption = "F Snap"
        lyt.Add(snapMode,60)   
        snapMode.OnClick.Add(self.snapModeControl)
        
        #####################
        preTrans = FBButton()
        preTrans.Caption = "| - T"
        preTrans.Hint = "copy previous Translations key"        
        lyt.Add(preTrans, 60)
        preTrans.OnClick.Add(self.copyPreFrameTran)
 
        #####################
        preRot = FBButton()
        preRot.Caption = "| - R"
        preRot.Hint = "copy previous Rotations key"             
        lyt.Add(preRot, 60)
        preRot.OnClick.Add(self.copyPreFrameRot)

        #####################
        delKey = FBButton()
        delKey.Caption = "Del key"
        lyt.Add(delKey, 60)
        delKey.OnClick.Add(self.defaultButton)
                       
        #########################
        nextTrans = FBButton()
        nextTrans.Caption = "T - |"
        nextTrans.Hint = "copy next Translations key"        
        lyt.Add(nextTrans, 60)
        nextTrans.OnClick.Add(self.copyNextFrameTR)
 
        #####################
        nextRot = FBButton()
        nextRot.Caption = "R - |"
        nextRot.Hint = "copy next Rotations key"         
        lyt.Add(nextRot, 60)
        nextRot.OnClick.Add(self.copyNextFrameRot)

        #####################
        flatCurve = FBButton()
        flatCurve.Caption = "Flat"
        lyt.Add(flatCurve, 60)
        flatCurve.OnClick.Add(self.makeCurveFlat)                
              
        #####################
        preTake = FBButton()
        preTake.Caption = "<-- Take"
        preTake.Hint = "Jump to previous take"            
        lyt.Add(preTake, 60)
        preTake.OnClick.Add(self.navigateNegativeTakes)             

        #####################
        nextTake = FBButton()
        nextTake.Caption = "Take -->"
        nextTake.Hint = "Jump to next take"         
        lyt.Add(nextTake, 60)
        nextTake.OnClick.Add(self.navigateTakes)                  
                                                 
        #####################
        selIkFk = FBButton()
        selIkFk.Caption = "IKs / FKs"
        selIkFk.Hint = "iks / fks selection"              
        lyt.Add(selIkFk, 60)
        selIkFk.OnClick.Add(self.toggleIK_FK)        
        
        #####################
        pcConstraints = FBButton()
        pcConstraints.Caption = "p/c Const"
        pcConstraints.Hint = "Parent/Child constraint"       
        lyt.Add(pcConstraints, 60)
        pcConstraints.OnClick.Add(self.addConstraints)                          

        #####################
        halfBodyKey = FBButton()
        halfBodyKey.Caption = "HB Key"
        halfBodyKey.Hint = "Putting key on bodypart"           
        lyt.Add(halfBodyKey, 60)                  
        halfBodyKey.OnClick.Add(self.bodyPartKey)

        #####################
        ChMarker = FBButton()
        ChMarker.Caption = "Marker"
        lyt.Add(ChMarker, 60)                                  
        ChMarker.OnClick.Add(self.markerModelPointer)
        
        #####################
        DelSelKey = FBButton()
        DelSelKey.Caption = "DelSelKey"
        DelSelKey.Hint = "Deleting keys from selected object or rig control"                   
        lyt.Add(DelSelKey, 60)                                  
        DelSelKey.OnClick.Add(self.delKeySelected)
        
        #####################
        if self.isApp2016()==False:
            fCycles = FBButton()
            fCycles.Caption = "~ Cycles ~"
            fCycles.Hint = "pre/post cycles on selected control/s"             
            lyt.Add(fCycles, 60)
            fCycles.OnClick.Add(self.cycleOperation)     
    
       
    def cycleOperation(self, control, event):
        selections = self.selectedElements()
        if not selections:
            FBMessageBox("Warning", "Selection is required !!","OK")
        for node in selections:
            node.Translation.SetAnimated =True
            node.Rotation.SetAnimated =True
            for animNode in node.Translation.GetAnimationNode().Nodes:  
                animNode.FCurve.SetPreExtrapolationMode(pyfbsdk.FBExtrapolationMode.kFCurveExtrapolationRepetition)
                animNode.FCurve.SetPreExtrapolationCount(4)
                animNode.FCurve.SetPostExtrapolationMode(pyfbsdk.FBExtrapolationMode.kFCurveExtrapolationRepetition)
                animNode.FCurve.SetPostExtrapolationCount(4)
        
            for animNode in node.Rotation.GetAnimationNode().Nodes:      
                animNode.FCurve.SetPreExtrapolationMode(pyfbsdk.FBExtrapolationMode.kFCurveExtrapolationRepetition)
                animNode.FCurve.SetPreExtrapolationCount(4)
        
                animNode.FCurve.SetPostExtrapolationMode(pyfbsdk.FBExtrapolationMode.kFCurveExtrapolationRepetition)
                animNode.FCurve.SetPostExtrapolationCount(4)


    def isApp2016(self):
        version = False 
        for path in  sys.path:
            if path.find("2016")>0 :   
                version = True        
                return version
        return  version 

    def addConstraints(self, control, event):
        #added selection
        self.constraints_selection = []
        aimConstObjects = self.selectedElements()
        if len(aimConstObjects)<2:
            FBMessageBox("Error", "Please Select at least two objects!!","OK")
            return
        aimTarget = aimConstObjects[0]
        aimChild = aimConstObjects[-1]
        msg = "Parent constraint driver set to  (%s)" % (aimTarget.Name)
        res = FBMessageBox("Warning", msg,"OK", "Cancel")
        if res==2:
            return
        lCnst = FBCreateObject("Browsing/Templates/Constraints", "Parent/Child", aimChild.Name)
        FBSystem().Scene.Constraints.append(lCnst)
        lCnst.Name = "ByOnAClick_Script"   
        self.setConstraintsByName(lCnst, aimChild, "Constrained object (Child)")
        self.setConstraintsByName(lCnst, aimTarget, "Source (Parent)")
        lCnst.Snap()
        
    def setConstraintsByName(self, constraint, model, referenceGroupName):
        for ref in range(constraint.ReferenceGroupGetCount()):
            if constraint.ReferenceGroupGetName(ref) == referenceGroupName: 
                constraint.ReferenceAdd(ref ,model)
                       
    def bodyPartKey(self, control, event):
        app = FBApplication()
        obj=self.selectedElements()
        if not obj:
            FBMessageBox("Info", "Please select object!!", "OK")
            return
        playCtrl = FBPlayerControl()
        oldMode = self.app.CurrentCharacter.KeyingMode
        app.CurrentCharacter.KeyingMode = FBCharacterKeyingMode.kFBCharacterKeyingBodyPart
        playCtrl.Key()
        app.CurrentCharacter.KeyingMode = oldMode

    def markerModelPointer(self, control, event):
        obj=self.selectedElements()
        if not obj:
            FBMessageBox("Info", "Nothing is selected to snap!!!", "OK")
            return 
        lModel = FBModelMarker('MarkserByScript')
        lModel.Translation.SetAnimated(True)
        lModel.Visible = True
        lModel.Show = True
        lModel.Look=pyfbsdk.FBMarkerLook.kFBMarkerLookHardCross  
        aimObj = obj[0]   
        lModel.Translation = FBVector3d(aimObj.Translation)
        aimObj.Selected = False
        lModel.Selected = True


    def RemoveKeyAtCurrent(self, pAnimationNode):
        if len(pAnimationNode.Nodes)==0:
            pAnimationNode.KeyRemove()
        else:
            for lNode in pAnimationNode.Nodes:
                self.RemoveKeyAtCurrent(lNode)
                del(lNode)

    def delKeySelected(self, control, event):
        lModelList = FBModelList()
        FBGetSelectedModels(lModelList)
        for lModel in lModelList:
            self.RemoveKeyAtCurrent(lModel.AnimationNode)
            del(lModel)  
          
    def setCurrentTakeIndex(self):  
        lSystem = FBSystem()
        allTakes = lSystem.Scene.Takes
        lCurrentTakeName = lSystem.CurrentTake.Name
        for index in range(len(allTakes)):
            if lCurrentTakeName == lSystem.Scene.Takes[index].Name:
                return index
                
    def toggleIK_FK(self, control, event):
        if self.toggleFKIK_pt == "IK":
            self.toggleFKIK_pt = "FK"
            self.selectIK()
        else:
            self.toggleFKIK_pt = "IK"
            self.selectFK()        

    def Select(self, modelproviders):
        """
        Gather all models obtained from modelproviders list and select them.
        """
        if not self.app.CurrentCharacter:
            return
        self.DeselectAll()
        models = []
        for provider in modelproviders:
            models.extend(provider())

        for model in models:
            model.Selected = True

    def DeselectAll(self):

        models = FBModelList()
        FBGetSelectedModels(models)
        for model in models:        
            model.Selected = False

    def GetFK(self):
        """
        Find all FK node and return them as a list.
        """
        fk_list = []
        for id in FBBodyNodeId.values.itervalues():
            if id == FBBodyNodeId.kFBReferenceNodeId:
                continue
            m = self.app.CurrentCharacter.GetCtrlRigModel(id)
            if m:
                fk_list.append(m)
        return fk_list
                
    def GetIK(self):
        """
        Find all IK node and return them as a list.
        """
        ik_list = []
        for id in FBEffectorId.values.itervalues():
            m = self.app.CurrentCharacter.GetEffectorModel(id)
            if m:
                ik_list.append(m)
        return ik_list

    def selectIK(self):
        self.Select([self.GetIK])


    def selectFK(self):
        self.Select([self.GetFK])

                                                                                                               
    def navigateTakes(self, control, event):

        lSystem = FBSystem()
        allTakes = lSystem.Scene.Takes

        lCurrentTakeName = lSystem.CurrentTake.Name
        for lTakeIdx in range( len(lSystem.Scene.Takes)):
            if lSystem.Scene.Takes[lTakeIdx].Name == lCurrentTakeName:
                indexMatch = lTakeIdx
        if indexMatch != self.currentTakeIndex:
            self.currentTakeIndex = indexMatch
        if self.currentTakeIndex < len(allTakes)-1:
            self.currentTakeIndex = self.currentTakeIndex + 1
        else:
            self.currentTakeIndex = 0
        lSystem.CurrentTake = lSystem.Scene.Takes[self.currentTakeIndex]
        lPlayer = FBPlayerControl()
        lPlayer.GotoStart()
        
    def navigateNegativeTakes(self, control, event):
        lSystem = FBSystem()
        allTakes = lSystem.Scene.Takes
        lCurrentTakeName = lSystem.CurrentTake.Name
        for lTakeIdx in range( len(lSystem.Scene.Takes)):
            if lSystem.Scene.Takes[lTakeIdx].Name == lCurrentTakeName:
                indexMatch = lTakeIdx
        if indexMatch != self.currentTakeIndex:
            self.currentTakeIndex = indexMatch
        if self.currentTakeIndex < len(allTakes)-1:
            self.currentTakeIndex = self.currentTakeIndex - 1 
        else:
            currentTake = self.setCurrentTakeIndex()
            self.currentTakeIndex = currentTake -1
        lSystem.CurrentTake = lSystem.Scene.Takes[self.currentTakeIndex]
        lPlayer = FBPlayerControl()
        lPlayer.GotoStart()
        
        
    def makeCurveFlat(self, control, event):
        lTime = FBSystem().LocalTime
        currentFrame = lTime.GetFrame()
        selected = self.selectedElements()
        if not selected:
            FBMessageBox("Info", "Please select control", "OK")
            return 
        node = selected[0]
        self.makeCurveFlatOp(node)

    def makeCurveFlatOp(self, node):
        currentFrame = FBSystem().LocalTime.GetFrame()
        animNode = node.Translation.GetAnimationNode()
        frame, index = self.currentFrame(animNode, currentFrame)

        animNode = node.Rotation.GetAnimationNode()
        frame, index = self.currentFrame(animNode, currentFrame)       
                                                         
    def defaultButton(self, control, event):
        FBMessageBox("Info", "Progressing","OK")
            
    def snapModeControl(self, control, event):
        player = FBPlayerControl()
        if player.SnapMode == FBTransportSnapMode.kFBTransportSnapModeSnapOnFrames:
            player.SnapMode = FBTransportSnapMode.kFBTransportSnapModeNoSnap
        else:
            player.SnapMode = FBTransportSnapMode.kFBTransportSnapModeSnapOnFrames            
         
        
    def playerSpeedControl(self, control, event):
        player = FBPlayerControl()
        speed = player.GetPlaySpeed()
        player.SetPlaySpeed(self.speedToggle[self.speedIndex])
        if self.speedIndex==2:
            self.speedIndex=0
        else:     
            self.speedIndex=self.speedIndex+1

    def addSelection(self,control, event):
        self.selection = self.selectedElements()
        
    def applySelction(self,control, event):
        for eachObj in self.selection:
            eachObj.Selected  = True
            
    def CreateTool(self):
        # Tool creation will serve as the hub for all other controls
        t = FBCreateUniqueTool("[ on  A  click ]")
        t.StartSizeX = 1200
        t.StartSizeY = 75
        self.PopulateLayout(t)
        ShowTool(t)

    def selectedElements(self):
        allObject = [] 
        selectedModels = FBModelList()
        FBGetSelectedModels(selectedModels,None, True, True) 
        if selectedModels:
            for model in selectedModels:
                allObject.append(model) 
        return allObject
        
    def copyNextFrameTR(self, control, event):
        selected = self.selectedElements()
        if not selected:
            FBMessageBox("Info", "Please select control", "OK")
            return 
        node = selected[0]
        animNode = node.Translation.GetAnimationNode()  
        self.copyAnimFromNextPreFrame(animNode)
        self.makeCurveFlatOp(node)

    def copyNextFrameRot(self, control, event):
        selected = self.selectedElements()
        if not selected:
            FBMessageBox("Info", "Please select control", "OK")
            return 
        node = selected[0]
        animNode = node.Rotation.GetAnimationNode()  
        self.copyAnimFromNextPreFrame(animNode)
        self.makeCurveFlatOp(node)

    def copyPreFrameTran(self, control, event):
        selected = self.selectedElements()
        if not selected:
            FBMessageBox("Info", "Please select control", "OK")
            return 
        node = selected[0]
        animNode = node.Translation.GetAnimationNode()  
        self.copyAnimFromNextPreFrame(animNode, nextKey=False)
        self.makeCurveFlatOp(node)

    def copyPreFrameRot(self, control, event):
        selected = self.selectedElements()
        if not selected:
            FBMessageBox("Info", "Please select control", "OK")
            return 
        node = selected[0]
        animNode = node.Rotation.GetAnimationNode()  
        self.copyAnimFromNextPreFrame(animNode, nextKey=False)
        self.makeCurveFlatOp(node)
                        
    def copyAnimFromNextPreFrame(self, animNode, nextKey=True):

        lTime = FBSystem().LocalTime
        currentFrame = lTime.GetFrame()
        if nextKey:
            res = self.nextPreKey(animNode, currentFrame)
        else:
            res = self.nextPreKey(animNode, currentFrame, nextKey=False)
            
        if not res:
            FBMessageBox("Info", "Next Key not found","OK")
            return 
        
        nextKey, index = res[0], res[1]
        
        for eachT in animNode.Nodes:
            keyObj = eachT.FCurve.Keys[index]
            eachT.KeyAdd(FBTime(0,0,0,currentFrame), keyObj.Value)
            
    def nextAnimFrame(self, animNode, currentFrame):
        keysAnim =[] 
        index = 0
        for eachKey in animNode.Nodes[0].FCurve.Keys:
            if currentFrame < eachKey.Time.GetFrame():
                return eachKey.Time.GetFrame(), index
            else:
                index +=1

    def currentFrame(self, animNode, currentFrame):
        keysAnim =[]
        index = 0    
        for eachKey in animNode.Nodes[0].FCurve.Keys:
            keysAnim.append(eachKey.Time.GetFrame())
        for eachKey in keysAnim:
            if eachKey == currentFrame:
                for eachCurve in animNode.Nodes:
                    keyData = eachCurve.FCurve.Keys[index]
                    keyData.TangentMode = FBTangentMode.kFBTangentModeUser

                return keysAnim[index], index      
            index += 1  
            
    def nextPreKey(self, animNode, currentFrame, nextKey=True):
        keysAnim =[]
        index = 0    
        for eachKey in animNode.Nodes[0].FCurve.Keys:
            keysAnim.append(eachKey.Time.GetFrame())
        for eachKey in keysAnim:
            if nextKey:
                if eachKey > currentFrame:
                    return keysAnim[index], index       
            else:
                if eachKey > currentFrame or eachKey == currentFrame:
                    index -= 1
                    return keysAnim[index], index           
            index += 1  
        
obj =  DataSlection()
obj.CreateTool()


