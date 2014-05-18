#!/usr/bin/env python

from PyQt4 import QtCore, QtGui;
from ui import Ui_KPS_RevisitBusinessEvents as ui_BusinessEvents;

class RevistBusinessEvents_Dialog(QtGui.QDialog):
    def __init__(self):
        super(RevistBusinessEvents_Dialog, self).__init__()
        self.ui = ui_BusinessEvents.Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = RevistBusinessEvents_Dialog()
    Dialog.show()
    sys.exit(app.exec_())