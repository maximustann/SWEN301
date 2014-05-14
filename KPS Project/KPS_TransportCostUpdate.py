#!/usr/bin/env python

from PyQt4 import QtGui, QtCore;
from ui import Ui_KPS_TransportCostUpdate as ui_transportCostUpdate;

class TransportCostUpdate_Dialog(QtGui.QDialog):
    def __init__(self):
        super(TransportCostUpdate_Dialog, self).__init__()
        self.ui = ui_transportCostUpdate.Ui_TransportCostUpdate()
        self.ui.setupUi(self)

       # self.ui.bt_Add_Route.clicked.connect(self.clicked_bt_Add_Routes)

    def clicked_bt_Add_Routes(self):
        Dialog = routes_add.Routes_add_Dialog()
	Dialog.show()
        result = Dialog.exec_()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Ui_TransportCostUpdate()
    Dialog.show()
    sys.exit(app.exec_())

      #  QtCore.QObject.connect(self.bt_Select_Route, QtCore.SIGNAL(_fromUtf8("clicked()")), self.selectRoute)
      #  QtCore.QObject.connect(self.bt_AddEvent, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addEvent)