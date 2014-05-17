# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_KeyFigures.ui'
#
# Created: Sat May 17 18:42:48 2014
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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(631, 377)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 231, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(160, 30, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(160, 60, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(160, 90, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(270, 40, 341, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 109))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tableView = QtGui.QTableView(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 341, 111))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(280, 20, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.scrollArea_2 = QtGui.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 180, 281, 141))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 279, 139))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.tableView_2 = QtGui.QTableView(self.scrollAreaWidgetContents_2)
        self.tableView_2.setGeometry(QtCore.QRect(0, 0, 281, 141))
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 160, 91, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.scrollArea_3 = QtGui.QScrollArea(Dialog)
        self.scrollArea_3.setGeometry(QtCore.QRect(320, 180, 291, 141))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 289, 139))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.tableView_3 = QtGui.QTableView(self.scrollAreaWidgetContents_3)
        self.tableView_3.setGeometry(QtCore.QRect(0, 0, 291, 141))
        self.tableView_3.setObjectName(_fromUtf8("tableView_3"))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(330, 160, 121, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Totals", None))
        self.label.setText(_translate("Dialog", "Total Revenue:", None))
        self.label_2.setText(_translate("Dialog", "Total Expenditure:", None))
        self.label_3.setText(_translate("Dialog", "Total No. of Events:", None))
        self.label_4.setText(_translate("Dialog", "TextLabel", None))
        self.label_5.setText(_translate("Dialog", "TextLabel", None))
        self.label_6.setText(_translate("Dialog", "TextLabel", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.label_7.setText(_translate("Dialog", "Amount of Mail", None))
        self.label_8.setText(_translate("Dialog", "Critical Routes", None))
        self.label_9.setText(_translate("Dialog", "Average Delivery Time", None))

