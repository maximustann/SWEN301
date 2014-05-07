# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_TransportCostUpdate.ui'
#
# Created: Wed May  7 21:25:52 2014
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

class Ui_TransportCostUpdate(object):
    def setupUi(self, TransportCostUpdate):
        TransportCostUpdate.setObjectName(_fromUtf8("TransportCostUpdate"))
        TransportCostUpdate.resize(773, 343)
        self.lv_availableRoutes = QtGui.QListView(TransportCostUpdate)
        self.lv_availableRoutes.setGeometry(QtCore.QRect(20, 30, 256, 271))
        self.lv_availableRoutes.setObjectName(_fromUtf8("lv_availableRoutes"))
        self.label = QtGui.QLabel(TransportCostUpdate)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.bt_Select_Route = QtGui.QPushButton(TransportCostUpdate)
        self.bt_Select_Route.setGeometry(QtCore.QRect(20, 310, 91, 23))
        self.bt_Select_Route.setObjectName(_fromUtf8("bt_Select_Route"))
        self.groupBox = QtGui.QGroupBox(TransportCostUpdate)
        self.groupBox.setGeometry(QtCore.QRect(310, 10, 321, 321))
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
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(31, 80, 45, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(31, 110, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cb_TransportType = QtGui.QComboBox(self.groupBox)
        self.cb_TransportType.setGeometry(QtCore.QRect(180, 110, 131, 20))
        self.cb_TransportType.setObjectName(_fromUtf8("cb_TransportType"))
        self.tb_PriceCC = QtGui.QLineEdit(self.groupBox)
        self.tb_PriceCC.setGeometry(QtCore.QRect(180, 170, 133, 20))
        self.tb_PriceCC.setObjectName(_fromUtf8("tb_PriceCC"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 170, 58, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 260, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(30, 230, 111, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.bt_AddEvent = QtGui.QPushButton(self.groupBox)
        self.bt_AddEvent.setGeometry(QtCore.QRect(180, 290, 75, 23))
        self.bt_AddEvent.setObjectName(_fromUtf8("bt_AddEvent"))
        self.tb_PriceG = QtGui.QLineEdit(self.groupBox)
        self.tb_PriceG.setGeometry(QtCore.QRect(180, 140, 133, 20))
        self.tb_PriceG.setObjectName(_fromUtf8("tb_PriceG"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(30, 140, 58, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.cb_DayOfWeek = QtGui.QComboBox(self.groupBox)
        self.cb_DayOfWeek.setGeometry(QtCore.QRect(180, 200, 131, 20))
        self.cb_DayOfWeek.setObjectName(_fromUtf8("cb_DayOfWeek"))
        self.tb_Frequency = QtGui.QLineEdit(self.groupBox)
        self.tb_Frequency.setGeometry(QtCore.QRect(180, 230, 133, 20))
        self.tb_Frequency.setObjectName(_fromUtf8("tb_Frequency"))
        self.tb_Duration = QtGui.QLineEdit(self.groupBox)
        self.tb_Duration.setGeometry(QtCore.QRect(180, 260, 133, 20))
        self.tb_Duration.setObjectName(_fromUtf8("tb_Duration"))
        self.tb_Firm = QtGui.QLineEdit(self.groupBox)
        self.tb_Firm.setGeometry(QtCore.QRect(180, 80, 133, 20))
        self.tb_Firm.setObjectName(_fromUtf8("tb_Firm"))

        self.retranslateUi(TransportCostUpdate)
        QtCore.QObject.connect(self.bt_Select_Route, QtCore.SIGNAL(_fromUtf8("clicked()")), self.bt_Select_Route.click)
        QtCore.QObject.connect(self.bt_AddEvent, QtCore.SIGNAL(_fromUtf8("clicked()")), self.bt_AddEvent.click)
        QtCore.QMetaObject.connectSlotsByName(TransportCostUpdate)

    def retranslateUi(self, TransportCostUpdate):
        TransportCostUpdate.setWindowTitle(_translate("TransportCostUpdate", "Routes", None))
        self.label.setText(_translate("TransportCostUpdate", "Current Routes", None))
        self.bt_Select_Route.setText(_translate("TransportCostUpdate", "Select Route", None))
        self.groupBox.setTitle(_translate("TransportCostUpdate", "Route Details", None))
        self.label_2.setText(_translate("TransportCostUpdate", "Select Origin Hub", None))
        self.label_3.setText(_translate("TransportCostUpdate", "Select Destination Hub", None))
        self.label_4.setText(_translate("TransportCostUpdate", "Firm", None))
        self.label_5.setText(_translate("TransportCostUpdate", "Transport Type", None))
        self.label_6.setText(_translate("TransportCostUpdate", "Price (g)", None))
        self.label_7.setText(_translate("TransportCostUpdate", "Duration (hours)", None))
        self.label_8.setText(_translate("TransportCostUpdate", "Frequency (hours)", None))
        self.bt_AddEvent.setText(_translate("TransportCostUpdate", "Add Event", None))
        self.label_9.setText(_translate("TransportCostUpdate", "Price (cc)", None))
        self.label_10.setText(_translate("TransportCostUpdate", "Day of Week", None))

