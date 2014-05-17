# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_Mail_Item.ui'
#
# Created: Wed May 14 23:18:07 2014
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
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 320, 341, 32))
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 240, 81, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 290, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(240, 290, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 160, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 200, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 230, 113, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 120, 91, 27))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(220, 50, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 80, 71, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 92, 28))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), self.label_7.setText)
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("editTextChanged(QString)")), self.label_7.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Mail Item", None))
        self.label.setText(_translate("Dialog", "Origin:", None))
        self.label_2.setText(_translate("Dialog", "Destination:", None))
        self.label_3.setText(_translate("Dialog", "Weight:", None))
        self.label_4.setText(_translate("Dialog", "Volume:", None))
        self.label_5.setText(_translate("Dialog", "EntryTime:", None))
        self.label_6.setText(_translate("Dialog", "Price:", None))
        self.label_7.setText(_translate("Dialog", "TextLabel", None))
        self.label_8.setText(_translate("Dialog", "Wellington", None))
        self.label_9.setText(_translate("Dialog", "Priority", None))
        self.comboBox.setItemText(0, _translate("Dialog", "Regular", None))
        self.comboBox.setItemText(1, _translate("Dialog", "Air", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

