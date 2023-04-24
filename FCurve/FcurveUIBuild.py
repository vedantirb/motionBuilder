from PySide import QtCore, QtGui
import sys
import logging
sys.path.append("I:\\MOTIONBUILDER\\FCurve")
import utilFCurve
import FCurveUI

class FCurveDialog(QtGui.QDialog, FCurveUI.Ui_animTransfer):
    def __init__(self, parent=None):
        super(FCurveDialog, self).__init__()
        self.setupUi(self)
        self.connection()
        self.sourceObject = None
        self.destObject = []
        self.operationObject = []
        self.opObjectInvertScale =  []
        self.sourceController = None
        self.sourceAxies = None
        self.destiController = None
        self.destiDataAxies = None
        
    def connection(self):
        self.btnFCurveTransfer.clicked.connect(self.fcurveOpration)    
        self.offsetDown.clicked.connect(lambda:self.transferOperation("offsetDown"))
        self.offsetUp.clicked.connect(lambda:self.transferOperation("offsetUp"))
        self.scaleDown.clicked.connect(lambda:self.transferOperation("scaleDown"))
        self.scaleUp.clicked.connect(lambda:self.transferOperation("scaleUp"))
        self.Invertbtn.clicked.connect(lambda:self.transferOperation("Invert"))
        self.Invertbtn.setToolTip("Invert")

    def transferOperation(self, operation):
        utilFCurve.transferActivity(
            self.sourceObject, self.destObject, self.sourceController,
            self.sourceAxies, self.destiController, self.destiDataAxies, operation, self.operationObject, self.opObjectInvertScale
            )

    def fcurveOpration(self):
        msg = ""
        sourceData = self.srcTxGroup.checkedButton().text()
        destData = self.destTxGroup.checkedButton().text() 
        data = sourceData + "," + destData
        self.sourceController = sourceData[0]
        self.sourceAxies = sourceData[-1]
        self.destiController = destData[0]
        self.destiDataAxies = destData[-1]
        selections = utilFCurve.selectedElements()
        if len(selections)>=2:
            self.sourceObject = selections[0]
            self.destObject = selections[1:]
            if len(selections) == 2:
                self.operationObject = selections[1:]   
            else:
                self.operationObject = selections[2:]
            self.opObjectInvertScale =  selections[1:]  
            self.transferOperation("TransferCurve")
        else:
            msg = "Please select at least two object"
            QtGui.QMessageBox.information(self, "Information", msg)                          
