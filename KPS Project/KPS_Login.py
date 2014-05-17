#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_KPS_Login as ui_login;
import login;

class Login_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Login_Dialog, self).__init__()
        self.ui = ui_login.Ui_Dialog()
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
            self.ui.label_4.setText("")
            super(Login_Dialog, self).accept()
        elif result == 0 and self.actor_reason == 0:
            self.ui.label_4.setText("Incorrect password")
        elif result == 0 and self.actor_reason == 1:
            self.ui.label_4.setText("Invalid username")
        elif result == 0 and self.actor_reason == 2:
            self.ui.label_4.setText("Username and password fields are empty")
        elif result == 0 and self.actor_reason == 3:
            self.ui.label_4.setText("Username field empty")
        elif result == 0 and self.actor_reason == 4:
            self.ui.label_4.setText("Password field empty")

        self.ui.label_4.setStyleSheet("color: red")
	
    def get_value(self):
        return self.actor_reason
    def get_value(self):
        return self.actor_reason

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Login_Dialog()
    Dialog.show()
    sys.exit(app.exec_())


