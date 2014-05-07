
from PyQt4 import QtCore, QtGui
from ui import Ui_KPS_Routes_Add as ui_routes_add;

class Routes_add_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Routes_add_Dialog, self).__init__()
        self.ui = ui_routes_add.Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Routes_add_Dialog()
    Dialog.show()
    sys.exit(app.exec_())

