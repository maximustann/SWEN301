# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_Hub.ui'
#
# Created: Mon Apr 21 15:25:45 2014
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

class Ui_Dialog(object):
    def setupUi(self, wn_Hubs):
        wn_Hubs.setObjectName(_fromUtf8("wn_Hubs"))
        wn_Hubs.resize(494, 232)
        self.listView = QtGui.QListView(wn_Hubs)
        self.listView.setGeometry(QtCore.QRect(20, 30, 256, 151))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(wn_Hubs)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pb_Remove_Hub = QtGui.QPushButton(wn_Hubs)
        self.pb_Remove_Hub.setGeometry(QtCore.QRect(20, 190, 75, 23))
        self.pb_Remove_Hub.setObjectName(_fromUtf8("pb_Remove_Hub"))
        self.groupBox = QtGui.QGroupBox(wn_Hubs)
        self.groupBox.setGeometry(QtCore.QRect(290, 30, 181, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.bt_Add_Hub = QtGui.QPushButton(self.groupBox)
        self.bt_Add_Hub.setGeometry(QtCore.QRect(20, 120, 75, 23))
        self.bt_Add_Hub.setObjectName(_fromUtf8("bt_Add_Hub"))

        self.retranslateUi(wn_Hubs)
        QtCore.QMetaObject.connectSlotsByName(wn_Hubs)

    def retranslateUi(self, wn_Hubs):
        wn_Hubs.setWindowTitle(_translate("wn_Hubs", "Hubs", None))
        self.label.setText(_translate("wn_Hubs", "Current Hubs", None))
        self.pb_Remove_Hub.setText(_translate("wn_Hubs", "Remove Hub", None))
        self.groupBox.setTitle(_translate("wn_Hubs", "Add New Hub", None))
        self.label_2.setText(_translate("wn_Hubs", "Hub name", None))
        self.bt_Add_Hub.setText(_translate("wn_Hubs", "Add Hub", None))

