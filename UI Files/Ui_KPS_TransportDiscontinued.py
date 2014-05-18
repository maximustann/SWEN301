# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_TransportDiscontinued.ui'
#
# Created: Sun May 18 22:25:15 2014
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

class Ui_TransportDiscontinued(object):
    def setupUi(self, TransportDiscontinued):
        TransportDiscontinued.setObjectName(_fromUtf8("TransportDiscontinued"))
        TransportDiscontinued.resize(773, 371)
        self.lv_availableRoutes = QtGui.QListView(TransportDiscontinued)
        self.lv_availableRoutes.setGeometry(QtCore.QRect(20, 30, 391, 321))
        self.lv_availableRoutes.setObjectName(_fromUtf8("lv_availableRoutes"))
        self.label = QtGui.QLabel(TransportDiscontinued)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(TransportDiscontinued)
        self.groupBox.setGeometry(QtCore.QRect(420, 10, 321, 351))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cb_Origin = QtGui.QComboBox(self.groupBox)
        self.cb_Origin.setGeometry(QtCore.QRect(180, 20, 131, 20))
        self.cb_Origin.setObjectName(_fromUtf8("cb_Origin"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(31, 21, 82, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cb_Destination = QtGui.QComboBox(self.groupBox)
        self.cb_Destination.setGeometry(QtCore.QRect(180, 50, 131, 20))
        self.cb_Destination.setObjectName(_fromUtf8("cb_Destination"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(31, 53, 108, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(31, 80, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cb_TransportType = QtGui.QComboBox(self.groupBox)
        self.cb_TransportType.setGeometry(QtCore.QRect(180, 80, 131, 20))
        self.cb_TransportType.setObjectName(_fromUtf8("cb_TransportType"))
        self.bt_AddEvent = QtGui.QPushButton(self.groupBox)
        self.bt_AddEvent.setGeometry(QtCore.QRect(180, 320, 75, 23))
        self.bt_AddEvent.setObjectName(_fromUtf8("bt_AddEvent"))
        self.errorLabel = QtGui.QLabel(self.groupBox)
        self.errorLabel.setGeometry(QtCore.QRect(30, 290, 281, 20))
        self.errorLabel.setText(_fromUtf8(""))
        self.errorLabel.setObjectName(_fromUtf8("errorLabel"))

        self.retranslateUi(TransportDiscontinued)
        QtCore.QMetaObject.connectSlotsByName(TransportDiscontinued)

    def retranslateUi(self, TransportDiscontinued):
        TransportDiscontinued.setWindowTitle(_translate("TransportDiscontinued", "Routes", None))
        self.label.setText(_translate("TransportDiscontinued", "Available Routes", None))
        self.groupBox.setTitle(_translate("TransportDiscontinued", "Route Details", None))
        self.label_2.setText(_translate("TransportDiscontinued", "Select Origin Hub", None))
        self.label_3.setText(_translate("TransportDiscontinued", "Select Destination Hub", None))
        self.label_5.setText(_translate("TransportDiscontinued", "Transport Type", None))
        self.bt_AddEvent.setText(_translate("TransportDiscontinued", "Add Event", None))

