
from PyQt4 import QtCore, QtGui;
from KPS_Hub import *;
from KPS_Routes import *;

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(725, 511)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 100, 661, 341))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.bt_hubs = QtGui.QPushButton(self.centralwidget)
        self.bt_hubs.setGeometry(QtCore.QRect(380, 10, 75, 23))
        self.bt_hubs.setObjectName(_fromUtf8("bt_hubs"))
        self.bt_Routes = QtGui.QPushButton(self.centralwidget)
        self.bt_Routes.setGeometry(QtCore.QRect(380, 40, 75, 23))
        self.bt_Routes.setObjectName(_fromUtf8("bt_Routes"))
        self.bt_MailItems = QtGui.QPushButton(self.centralwidget)
        self.bt_MailItems.setGeometry(QtCore.QRect(470, 10, 75, 23))
        self.bt_MailItems.setObjectName(_fromUtf8("bt_MailItems"))
        self.bt_Companys = QtGui.QPushButton(self.centralwidget)
        self.bt_Companys.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.bt_Companys.setObjectName(_fromUtf8("bt_Companys"))
        self.bt_Reports = QtGui.QPushButton(self.centralwidget)
        self.bt_Reports.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.bt_Reports.setObjectName(_fromUtf8("bt_Reports"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 321, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/logo_small.png")))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHome = QtGui.QMenu(self.menubar)
        self.menuHome.setObjectName(_fromUtf8("menuHome"))
        self.menuAdd_Hub = QtGui.QMenu(self.menubar)
        self.menuAdd_Hub.setObjectName(_fromUtf8("menuAdd_Hub"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Hub = QtGui.QAction(MainWindow)
        self.actionAdd_Hub.setObjectName(_fromUtf8("actionAdd_Hub"))
        self.actionAdd_Route = QtGui.QAction(MainWindow)
        self.actionAdd_Route.setObjectName(_fromUtf8("actionAdd_Route"))
        self.actionAdd_Mail_Item = QtGui.QAction(MainWindow)
        self.actionAdd_Mail_Item.setObjectName(_fromUtf8("actionAdd_Mail_Item"))
        self.actionAdd_Company = QtGui.QAction(MainWindow)
        self.actionAdd_Company.setObjectName(_fromUtf8("actionAdd_Company"))
        self.menuAdd_Hub.addAction(self.actionAdd_Hub)
        self.menuAdd_Hub.addAction(self.actionAdd_Route)
        self.menuAdd_Hub.addAction(self.actionAdd_Mail_Item)
        self.menuAdd_Hub.addAction(self.actionAdd_Company)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuAdd_Hub.menuAction())
        self.bt_hubs.clicked.connect(self.clicked_bt_Hubs)
        self.bt_Routes.clicked.connect(self.clicked_bt_Routes)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bt_hubs.setText(_translate("MainWindow", "Hubs", None))
        self.bt_Routes.setText(_translate("MainWindow", "Routes", None))
        self.bt_MailItems.setText(_translate("MainWindow", "Mail Items", None))
        self.bt_Companys.setText(_translate("MainWindow", "Companies", None))
        self.bt_Reports.setText(_translate("MainWindow", "Reports", None))
        self.menuHome.setTitle(_translate("MainWindow", "Home", None))
        self.menuAdd_Hub.setTitle(_translate("MainWindow", "Actions", None))
        self.actionAdd_Hub.setText(_translate("MainWindow", "Hubs", None))
        self.actionAdd_Route.setText(_translate("MainWindow", "Routes", None))
        self.actionAdd_Mail_Item.setText(_translate("MainWindow", "Mail Items", None))
        self.actionAdd_Company.setText(_translate("MainWindow", "Companys", None))

    def clicked_bt_Hubs(self):
        Dialog = QtGui.QDialog()
        ui = Ui_wn_Hubs()
        ui.setupUi(Dialog)
        Dialog.exec_()
        
    def clicked_bt_Routes(self):
        Dialog = QtGui.QDialog()
        ui = Ui_KPS_Routes()
        ui.setupUi(Dialog)
        result = Dialog.exec_()

if __name__ == '__main__':
         import sys
         
         app = QtGui.QApplication(sys.argv)
         MainWindow = QtGui.QMainWindow()
         ui = Ui_MainWindow()
         ui.setupUi(MainWindow)
         MainWindow.show()
         sys.exit(app.exec_())
