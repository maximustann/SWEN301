# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_Routes.ui'
#
# Created: Mon Apr 21 15:26:07 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui;

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

class Ui_Dialog(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(787, 304)
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.bt_Remove_Route = QtGui.QPushButton(Form)
        self.bt_Remove_Route.setGeometry(QtCore.QRect(20, 230, 91, 23))
        self.bt_Remove_Route.setObjectName(_fromUtf8("bt_Remove_Route"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(310, 10, 321, 291))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cb_Origin = QtGui.QComboBox(self.groupBox)
        self.cb_Origin.setGeometry(QtCore.QRect(180, 20, 69, 20))
        self.cb_Origin.setObjectName(_fromUtf8("cb_Origin"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(31, 21, 82, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cb_Destination = QtGui.QComboBox(self.groupBox)
        self.cb_Destination.setGeometry(QtCore.QRect(180, 50, 69, 20))
        self.cb_Destination.setObjectName(_fromUtf8("cb_Destination"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(31, 53, 108, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(31, 85, 45, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cb_Company = QtGui.QComboBox(self.groupBox)
        self.cb_Company.setGeometry(QtCore.QRect(180, 80, 71, 20))
        self.cb_Company.setObjectName(_fromUtf8("cb_Company"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(31, 110, 34, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cb_Priority = QtGui.QComboBox(self.groupBox)
        self.cb_Priority.setGeometry(QtCore.QRect(180, 110, 69, 20))
        self.cb_Priority.setObjectName(_fromUtf8("cb_Priority"))
        self.tb_Volume = QtGui.QLineEdit(self.groupBox)
        self.tb_Volume.setGeometry(QtCore.QRect(180, 140, 133, 20))
        self.tb_Volume.setObjectName(_fromUtf8("tb_Volume"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 58, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 170, 41, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.cb_Duration = QtGui.QComboBox(self.groupBox)
        self.cb_Duration.setGeometry(QtCore.QRect(180, 170, 69, 20))
        self.cb_Duration.setObjectName(_fromUtf8("cb_Duration"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 51, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cb_Frequency = QtGui.QComboBox(self.groupBox)
        self.cb_Frequency.setGeometry(QtCore.QRect(180, 200, 69, 20))
        self.cb_Frequency.setObjectName(_fromUtf8("cb_Frequency"))
        self.bt_Update_Route = QtGui.QPushButton(self.groupBox)
        self.bt_Update_Route.setGeometry(QtCore.QRect(180, 230, 75, 23))
        self.bt_Update_Route.setObjectName(_fromUtf8("bt_Update_Route"))
        self.bt_Add_Route = QtGui.QPushButton(Form)
        self.bt_Add_Route.setGeometry(QtCore.QRect(200, 230, 75, 23))
        self.bt_Add_Route.setObjectName(_fromUtf8("bt_Add_Route"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Routes", None))
        self.label.setText(_translate("Form", "Current Routes", None))
        self.bt_Remove_Route.setText(_translate("Form", "Remove Route", None))
        self.groupBox.setTitle(_translate("Form", "Route Details", None))
        self.label_2.setText(_translate("Form", "Select Origin Hub", None))
        self.label_3.setText(_translate("Form", "Select Destination Hub", None))
        self.label_4.setText(_translate("Form", "Company", None))
        self.label_5.setText(_translate("Form", "Priority", None))
        self.label_6.setText(_translate("Form", "Volume Cost", None))
        self.label_7.setText(_translate("Form", "Duration", None))
        self.label_8.setText(_translate("Form", "Frequency", None))
        self.bt_Update_Route.setText(_translate("Form", "Update Route", None))
        self.bt_Add_Route.setText(_translate("Form", "Add Route", None))
 
