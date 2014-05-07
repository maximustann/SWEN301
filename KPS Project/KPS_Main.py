#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import KPS_Hub as hub;
import KPS_Routes as routes;
import KPS_Login as login;
from ui import Ui_KPS_Main as ui_main;



class KPS_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        user = self.login()
        if user == None:
            sys.exit(-1)

        super(KPS_MainWindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.bt_hubs.clicked.connect(self.clicked_bt_Hubs)
        self.ui.bt_Routes.clicked.connect(self.clicked_bt_Routes)



    def login(self):
        Dialog = login.Login_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            return Dialog.get_value()
    def clicked_bt_Hubs(self):
        Dialog = hub.Hub_Dialog()
        Dialog.show()
        result = Dialog.exec_()

    def clicked_bt_Routes(self):
        Dialog = routes.Routes_Dialog()
        Dialog.show()
        result = Dialog.exec_()


if __name__ == '__main__':
         import sys
         
         app = QtGui.QApplication(sys.argv)
         MainWindow = KPS_MainWindow()
         MainWindow.show()
         sys.exit(app.exec_())
