# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_Mail_Item.ui'
#
# Created: Tue May 20 16:11:03 2014
#      by: PyQt4 UI code generator 4.10.2
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
        Dialog.resize(458, 408)
        Dialog.setStyleSheet("background-color:rgb(8,129,2);Color: white;font-size:16px;")
        self.label_Head = QtGui.QLabel(Dialog)
        self.label_Head.setGeometry(QtCore.QRect(70, 0, 511, 41))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 350, 341, 32))
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttonBox.setStyleSheet("background-color:#dddddd;Color: black; font-size:12px;")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(230, 190, 141, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(230, 270, 141, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(100, 50, 271, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_3 = QtGui.QComboBox(self.widget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(100, 100, 271, 31))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtGui.QComboBox(self.widget1)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.widget2 = QtGui.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(100, 220, 271, 30))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.widget3 = QtGui.QWidget(Dialog)
        self.widget3.setGeometry(QtCore.QRect(100, 300, 271, 30))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.widget3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget3)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_3.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.lineEdit_4.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.widget4 = QtGui.QWidget(Dialog)
        self.widget4.setGeometry(QtCore.QRect(100, 140, 271, 31))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.widget4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox = QtGui.QComboBox(self.widget4)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.comboBox.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.comboBox_2.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        self.comboBox_3.setStyleSheet("background-color:white;Color: black; font-size:12px;")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_Head.setFont(font)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Mail Item", None))
        self.label_6.setText(_translate("Dialog", "", None))
        self.label_7.setText(_translate("Dialog", "", None))
        self.label.setText(_translate("Dialog", "Origin:", None))
        self.label_2.setText(_translate("Dialog", "Destination:", None))
        self.label_3.setText(_translate("Dialog", "Weight:", None))
        self.label_4.setText(_translate("Dialog", "Volume:", None))
        self.label_5.setText(_translate("Dialog", "Priority", None))
        self.label_Head.setText(_translate("Dialog", "Add Mail Item", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

