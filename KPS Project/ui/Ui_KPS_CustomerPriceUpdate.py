# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_CustomerPriceUpdate.ui'
#
# Created: Sun May 18 21:04:25 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_CustomerPriceUpdate(object):
    def setupUi(self, CustomerPriceUpdate):
        CustomerPriceUpdate.setObjectName(_fromUtf8("CustomerPriceUpdate"))
        CustomerPriceUpdate.resize(773, 260)
        CustomerPriceUpdate.setStyleSheet("background-color:rgb(8,129,2);Color: white;font-size:12px;")
        self.lv_availableRoutes = QtGui.QListView(CustomerPriceUpdate)
        self.lv_availableRoutes.setGeometry(QtCore.QRect(20, 30, 256, 191))
        self.lv_availableRoutes.setObjectName(_fromUtf8("lv_availableRoutes"))
        self.label = QtGui.QLabel(CustomerPriceUpdate)
        self.label.setGeometry(QtCore.QRect(20, 10, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(CustomerPriceUpdate)
        self.groupBox.setGeometry(QtCore.QRect(310, 10, 321, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cb_Origin = QtGui.QComboBox(self.groupBox)
        self.cb_Origin.setGeometry(QtCore.QRect(180, 20, 131, 20))
        self.cb_Origin.setObjectName(_fromUtf8("cb_Origin"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(31, 21, 150, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cb_Destination = QtGui.QComboBox(self.groupBox)
        self.cb_Destination.setGeometry(QtCore.QRect(180, 50, 131, 20))
        self.cb_Destination.setObjectName(_fromUtf8("cb_Destination"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(31, 53, 150, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(31, 80, 150, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cb_Priority = QtGui.QComboBox(self.groupBox)
        self.cb_Priority.setGeometry(QtCore.QRect(180, 80, 131, 20))
        self.cb_Priority.setObjectName(_fromUtf8("cb_Priority"))
        self.tb_PriceCC = QtGui.QLineEdit(self.groupBox)
        self.tb_PriceCC.setGeometry(QtCore.QRect(180, 110, 133, 20))
        self.tb_PriceCC.setObjectName(_fromUtf8("tb_PriceCC"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 150, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.bt_AddEvent = QtGui.QPushButton(self.groupBox)
        self.bt_AddEvent.setGeometry(QtCore.QRect(180, 210, 75, 23))
        self.bt_AddEvent.setObjectName(_fromUtf8("bt_AddEvent"))
        self.tb_PriceG = QtGui.QLineEdit(self.groupBox)
        self.tb_PriceG.setGeometry(QtCore.QRect(180, 140, 133, 20))
        self.tb_PriceG.setObjectName(_fromUtf8("tb_PriceG"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 110, 58, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.errorLabel = QtGui.QLabel(self.groupBox)
        self.errorLabel.setGeometry(QtCore.QRect(30, 170, 271, 20))
        self.errorLabel.setText(_fromUtf8(""))
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))
        self.cb_Destination.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.cb_Origin.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.cb_Priority.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.tb_PriceCC.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.tb_PriceG.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.lv_availableRoutes.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.bt_AddEvent.setStyleSheet("background-color:#dddddd;Color: black; font-size:12px;")
        self.retranslateUi(CustomerPriceUpdate)
        QtCore.QMetaObject.connectSlotsByName(CustomerPriceUpdate)

    def retranslateUi(self, CustomerPriceUpdate):
        CustomerPriceUpdate.setWindowTitle(_translate("CustomerPriceUpdate", "Routes", None))
        self.label.setText(_translate("CustomerPriceUpdate", "Current Route Available", None))
        self.groupBox.setTitle(_translate("CustomerPriceUpdate", "Route Details", None))
        self.label_2.setText(_translate("CustomerPriceUpdate", "Select Origin Hub", None))
        self.label_3.setText(_translate("CustomerPriceUpdate", "Select Destination Hub", None))
        self.label_5.setText(_translate("CustomerPriceUpdate", "Priority", None))
        self.label_6.setText(_translate("CustomerPriceUpdate", "Price (g)", None))
        self.bt_AddEvent.setText(_translate("CustomerPriceUpdate", "Add Event", None))
        self.label_9.setText(_translate("CustomerPriceUpdate", "Price (cc)", None))

