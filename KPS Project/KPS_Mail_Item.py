#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_KPS_Mail_Item as ui_mail_item

class Mail_Item_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Mail_Item_Dialog, self).__init__()
        self.ui = ui_mail_item.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Mail_Item_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
