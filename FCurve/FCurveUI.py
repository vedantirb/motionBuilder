# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\MOTIONBUILDER\FCurve\resources\FCurve.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_animTransfer(object):
    def setupUi(self, animTransfer):
        animTransfer.setObjectName(_fromUtf8("animTransfer"))
        animTransfer.setWindowModality(QtCore.Qt.NonModal)
        animTransfer.resize(330, 168)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(animTransfer.sizePolicy().hasHeightForWidth())
        animTransfer.setSizePolicy(sizePolicy)
        animTransfer.setMinimumSize(QtCore.QSize(330, 100))
        animTransfer.setMaximumSize(QtCore.QSize(350, 300))
        self.btnFCurveTransfer = QtGui.QPushButton(animTransfer)
        self.btnFCurveTransfer.setGeometry(QtCore.QRect(80, 110, 181, 23))
        self.btnFCurveTransfer.setObjectName(_fromUtf8("btnFCurveTransfer"))
        self.offsetDown = QtGui.QPushButton(animTransfer)
        self.offsetDown.setGeometry(QtCore.QRect(10, 140, 31, 23))
        self.offsetDown.setToolTip(_fromUtf8(""))
        self.offsetDown.setObjectName(_fromUtf8("offsetDown"))
        self.offsetUp = QtGui.QPushButton(animTransfer)
        self.offsetUp.setGeometry(QtCore.QRect(90, 140, 31, 23))
        self.offsetUp.setObjectName(_fromUtf8("offsetUp"))
        self.Invertbtn = QtGui.QPushButton(animTransfer)
        self.Invertbtn.setGeometry(QtCore.QRect(130, 140, 81, 23))
        self.Invertbtn.setToolTip(_fromUtf8(""))
        self.Invertbtn.setStatusTip(_fromUtf8(""))
        self.Invertbtn.setWhatsThis(_fromUtf8(""))
        self.Invertbtn.setAccessibleName(_fromUtf8(""))
        self.Invertbtn.setAccessibleDescription(_fromUtf8(""))
        self.Invertbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Invertbtn.setAutoFillBackground(False)
        self.Invertbtn.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Invertbtn.setShortcut(_fromUtf8(""))
        self.Invertbtn.setFlat(False)
        self.Invertbtn.setObjectName(_fromUtf8("Invertbtn"))
        self.scaleDown = QtGui.QPushButton(animTransfer)
        self.scaleDown.setGeometry(QtCore.QRect(220, 140, 31, 23))
        self.scaleDown.setObjectName(_fromUtf8("scaleDown"))
        self.scaleUp = QtGui.QPushButton(animTransfer)
        self.scaleUp.setGeometry(QtCore.QRect(290, 140, 31, 23))
        self.scaleUp.setObjectName(_fromUtf8("scaleUp"))
        self.label = QtGui.QLabel(animTransfer)
        self.label.setGeometry(QtCore.QRect(50, 140, 46, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(animTransfer)
        self.label_2.setGeometry(QtCore.QRect(260, 140, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.DestiBox = QtGui.QGroupBox(animTransfer)
        self.DestiBox.setGeometry(QtCore.QRect(170, 11, 151, 96))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DestiBox.sizePolicy().hasHeightForWidth())
        self.DestiBox.setSizePolicy(sizePolicy)
        self.DestiBox.setMinimumSize(QtCore.QSize(0, 50))
        self.DestiBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.DestiBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DestiBox.setObjectName(_fromUtf8("DestiBox"))
        self.Dest_TZ = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TZ.setGeometry(QtCore.QRect(30, 60, 61, 17))
        self.Dest_TZ.setObjectName(_fromUtf8("Dest_TZ"))
        self.destTxGroup = QtGui.QButtonGroup(animTransfer)
        self.destTxGroup.setObjectName(_fromUtf8("destTxGroup"))
        self.destTxGroup.addButton(self.Dest_TZ)
        self.Dest_TY = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TY.setGeometry(QtCore.QRect(30, 40, 51, 17))
        self.Dest_TY.setObjectName(_fromUtf8("Dest_TY"))
        self.destTxGroup.addButton(self.Dest_TY)
        self.Dest_TX = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TX.setGeometry(QtCore.QRect(30, 20, 51, 17))
        self.Dest_TX.setChecked(True)
        self.Dest_TX.setObjectName(_fromUtf8("Dest_TX"))
        self.destTxGroup.addButton(self.Dest_TX)
        self.Dest_TZ_3 = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TZ_3.setGeometry(QtCore.QRect(90, 60, 130, 17))
        self.Dest_TZ_3.setObjectName(_fromUtf8("Dest_TZ_3"))
        self.destTxGroup.addButton(self.Dest_TZ_3)
        self.Dest_TX_3 = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TX_3.setGeometry(QtCore.QRect(90, 20, 130, 17))
        self.Dest_TX_3.setChecked(False)
        self.Dest_TX_3.setObjectName(_fromUtf8("Dest_TX_3"))
        self.destTxGroup.addButton(self.Dest_TX_3)
        self.Dest_TY_3 = QtGui.QRadioButton(self.DestiBox)
        self.Dest_TY_3.setGeometry(QtCore.QRect(90, 40, 130, 17))
        self.Dest_TY_3.setObjectName(_fromUtf8("Dest_TY_3"))
        self.destTxGroup.addButton(self.Dest_TY_3)
        self.sourceBox = QtGui.QGroupBox(animTransfer)
        self.sourceBox.setGeometry(QtCore.QRect(10, 11, 161, 96))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceBox.sizePolicy().hasHeightForWidth())
        self.sourceBox.setSizePolicy(sizePolicy)
        self.sourceBox.setMinimumSize(QtCore.QSize(0, 50))
        self.sourceBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.sourceBox.setAlignment(QtCore.Qt.AlignCenter)
        self.sourceBox.setObjectName(_fromUtf8("sourceBox"))
        self.Src_TZ = QtGui.QRadioButton(self.sourceBox)
        self.Src_TZ.setGeometry(QtCore.QRect(20, 60, 117, 17))
        self.Src_TZ.setObjectName(_fromUtf8("Src_TZ"))
        self.srcTxGroup = QtGui.QButtonGroup(animTransfer)
        self.srcTxGroup.setObjectName(_fromUtf8("srcTxGroup"))
        self.srcTxGroup.addButton(self.Src_TZ)
        self.Src_Tx = QtGui.QRadioButton(self.sourceBox)
        self.Src_Tx.setGeometry(QtCore.QRect(20, 18, 51, 16))
        self.Src_Tx.setChecked(True)
        self.Src_Tx.setObjectName(_fromUtf8("Src_Tx"))
        self.srcTxGroup.addButton(self.Src_Tx)
        self.Src_TY = QtGui.QRadioButton(self.sourceBox)
        self.Src_TY.setGeometry(QtCore.QRect(20, 40, 117, 17))
        self.Src_TY.setObjectName(_fromUtf8("Src_TY"))
        self.srcTxGroup.addButton(self.Src_TY)
        self.Src_TZ_3 = QtGui.QRadioButton(self.sourceBox)
        self.Src_TZ_3.setGeometry(QtCore.QRect(80, 60, 51, 17))
        self.Src_TZ_3.setObjectName(_fromUtf8("Src_TZ_3"))
        self.srcTxGroup.addButton(self.Src_TZ_3)
        self.Src_Tx_3 = QtGui.QRadioButton(self.sourceBox)
        self.Src_Tx_3.setGeometry(QtCore.QRect(80, 20, 51, 16))
        self.Src_Tx_3.setChecked(False)
        self.Src_Tx_3.setObjectName(_fromUtf8("Src_Tx_3"))
        self.srcTxGroup.addButton(self.Src_Tx_3)
        self.Src_TY_3 = QtGui.QRadioButton(self.sourceBox)
        self.Src_TY_3.setGeometry(QtCore.QRect(80, 40, 61, 17))
        self.Src_TY_3.setObjectName(_fromUtf8("Src_TY_3"))
        self.srcTxGroup.addButton(self.Src_TY_3)

        self.retranslateUi(animTransfer)
        QtCore.QMetaObject.connectSlotsByName(animTransfer)

    def retranslateUi(self, animTransfer):
        animTransfer.setWindowTitle(_translate("animTransfer", "FCurve Transfers ", None))
        self.btnFCurveTransfer.setText(_translate("animTransfer", "FCurve Transfer", None))
        self.offsetDown.setText(_translate("animTransfer", "<-", None))
        self.offsetUp.setText(_translate("animTransfer", "->", None))
        self.Invertbtn.setText(_translate("animTransfer", "Invert", None))
        self.scaleDown.setText(_translate("animTransfer", "-", None))
        self.scaleUp.setText(_translate("animTransfer", "+", None))
        self.label.setText(_translate("animTransfer", "Offset", None))
        self.label_2.setText(_translate("animTransfer", "Scale", None))
        self.DestiBox.setTitle(_translate("animTransfer", "Destination Object(s)", None))
        self.Dest_TZ.setText(_translate("animTransfer", "TZ", None))
        self.Dest_TY.setText(_translate("animTransfer", "TY", None))
        self.Dest_TX.setText(_translate("animTransfer", "TX", None))
        self.Dest_TZ_3.setText(_translate("animTransfer", "RZ", None))
        self.Dest_TX_3.setText(_translate("animTransfer", "RX", None))
        self.Dest_TY_3.setText(_translate("animTransfer", "RY", None))
        self.sourceBox.setTitle(_translate("animTransfer", "Source Object", None))
        self.Src_TZ.setText(_translate("animTransfer", "TZ", None))
        self.Src_TZ.setProperty("value", _translate("animTransfer", "Z", None))
        self.Src_Tx.setText(_translate("animTransfer", "TX", None))
        self.Src_Tx.setProperty("value", _translate("animTransfer", "X", None))
        self.Src_TY.setText(_translate("animTransfer", "TY", None))
        self.Src_TY.setProperty("value", _translate("animTransfer", "Y", None))
        self.Src_TZ_3.setText(_translate("animTransfer", "RZ", None))
        self.Src_TZ_3.setProperty("value", _translate("animTransfer", "Z", None))
        self.Src_Tx_3.setText(_translate("animTransfer", "RX", None))
        self.Src_Tx_3.setProperty("value", _translate("animTransfer", "X", None))
        self.Src_TY_3.setText(_translate("animTransfer", "RY", None))
        self.Src_TY_3.setProperty("value", _translate("animTransfer", "Y", None))

