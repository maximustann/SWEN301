#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from ui import Ui_KPS_Hub as ui_hub;

class Hub_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Hub_Dialog, self).__init__()
        self.ui = ui_hub.Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Hub_Dialog()
    Dialog.show()
    sys.exit(app.exec_())

