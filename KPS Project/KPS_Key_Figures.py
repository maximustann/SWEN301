'''
Created on 10/05/2014

@author: Lesley
'''

from PyQt4 import QtGui, QtCore
from ui import Ui_KPS_KeyFigures as ui_key_figures;

class Key_Figures_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Key_Figures_Dialog, self).__init__()
        self.ui = ui_key_figures.Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Key_Figures_Dialog()
    Dialog.show()
    sys.exit(app.exec_())