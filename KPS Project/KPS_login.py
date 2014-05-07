# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_login.ui'
#
# Created: Wed May  7 06:42:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import login

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
        self.actor_reason = None
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 299)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 250, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(9, 9, 382, 121))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../Images/logo1.png")))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 160, 281, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 130, 251, 21))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Username:", None))
        self.label_2.setText(_translate("Dialog", "Password:", None))


class My_Dialog(QtGui.QDialog):
    def __init__(self):
        super(My_Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    def accept(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login(username, password)
        if result == 1:
            self.ui.label_4.setText(_fromUtf8(""))
            super(My_Dialog, self).accept()
        elif result == 0 and self.actor_reason == 0:
            self.ui.label_4.setText(_fromUtf8("wrong password"))
        else:
            self.ui.label_4.setText(_fromUtf8("No user information"))
        self.ui.label_4.setStyleSheet("color: red")
	def get_value(self):
		return self.actor_reason
    def get_value(self):
        return self.actor_reason

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = My_Dialog()
    Dialog.show()
    sys.exit(app.exec_())

