#!/usr/bin/env python

from PyQt4 import QtGui, QtCore;
from ui import Ui_KPS_Routes as ui_routes;
import KPS_Routes_Add as routes_add;

class Routes_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Routes_Dialog, self).__init__()
        self.ui = ui_routes.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.bt_Add_Route.clicked.connect(self.clicked_bt_Add_Routes)

    def clicked_bt_Add_Routes(self):
        Dialog = routes_add.Routes_add_Dialog()
	Dialog.show()
        result = Dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Routes_Dialog()
    Dialog.show()
    sys.exit(app.exec_())

