
from PyQt4 import QtCore, QtGui;
from PyQt4.QtCore import *;
from PyQt4.QtGui import *;
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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__( self, parent ):
        self.parent = parent

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1024, 600)
        palette = QtGui.QPalette()
        toolBarPalette = QtGui.QPalette()
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
        self.treeView.setGeometry(QtCore.QRect(20, 150, 661, 341))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        '''
        self.bt_hubs = QtGui.QPushButton(self.centralwidget)
        self.bt_hubs.setGeometry(QtCore.QRect(380, 60, 75, 23))
        self.bt_hubs.setObjectName(_fromUtf8("bt_hubs"))
        self.bt_Routes = QtGui.QPushButton(self.centralwidget)
        self.bt_Routes.setGeometry(QtCore.QRect(380, 90, 75, 23))
        self.bt_Routes.setObjectName(_fromUtf8("bt_Routes"))
        self.bt_MailItems = QtGui.QPushButton(self.centralwidget)
        self.bt_MailItems.setGeometry(QtCore.QRect(470, 60, 75, 23))
        self.bt_MailItems.setObjectName(_fromUtf8("bt_MailItems"))
        self.bt_Companys = QtGui.QPushButton(self.centralwidget)
        self.bt_Companys.setGeometry(QtCore.QRect(470, 90, 75, 23))
        self.bt_Companys.setObjectName(_fromUtf8("bt_Companys"))
        self.bt_Reports = QtGui.QPushButton(self.centralwidget)
        self.bt_Reports.setGeometry(QtCore.QRect(560, 60, 75, 23))
        self.bt_Reports.setObjectName(_fromUtf8("bt_Reports"))
        '''
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 321, 81))
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
        
        self.routeAction = QtGui.QAction(QtGui.QIcon('Images/route.png'), 'Add Customer Route', MainWindow)
        
        self.routeAction.setShortcut('Ctrl+R')
        self.routeAction.setIconText('Add Customer Route')
        
        self.revisitAction = QtGui.QAction(QtGui.QIcon('Images/revisit.png'), 'History', MainWindow)
        self.revisitAction.setShortcut('Ctrl+E')
        self.revisitAction.setIconText('History')
       
        self.exitAction = QtGui.QAction(QtGui.QIcon('Images/exit.png'), 'Exit', MainWindow)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setIconText('Exit')
        
        self.keyBusinessAction = QtGui.QAction(QtGui.QIcon('Images/key_business.png'), 'Key Figures', MainWindow)
        self.keyBusinessAction.setShortcut('Ctrl+B')
        self.keyBusinessAction.setIconText('Key Figures')
        
        self.addHubAction = QtGui.QAction(QtGui.QIcon('Images/addhub.png'), 'Add Hub', MainWindow)
        self.addHubAction.setShortcut('Ctrl+H')
        self.addHubAction.setIconText('Add Hub')
        
        self.addMailAction = QtGui.QAction(QtGui.QIcon('Images/mailitem.png'), 'Mail Item', MainWindow)
        self.addMailAction.setShortcut('Ctrl+M')
        self.addMailAction.setIconText('Add Mail')
        
        self.routesAction = QtGui.QAction(QtGui.QIcon('Images/routes.png'), 'Routes', MainWindow)
        self.routesAction.setShortcut('Ctrl+R')
        self.routesAction.setIconText('View Routes')
        
        self.transportAction = QtGui.QAction(QtGui.QIcon('Images/transport.png'), 'Add Transport Route', MainWindow)
        self.transportAction.setShortcut('Ctrl+R')
        self.transportAction.setIconText('Add Transport Route')
        
        self.discontinueAction = QtGui.QAction(QtGui.QIcon('Images/discontinue.png'), 'Discontinue Transport Route', MainWindow)
        self.discontinueAction.setShortcut('Ctrl+R')
        self.discontinueAction.setIconText('Discontinue Route')
   
        #self.exitAction.triggered.connect(self.parent.close)
        
        self.toolbar = QtGui.QToolBar(self.centralwidget)
        self.toolbar.addAction(self.exitAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.addMailAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.addHubAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.transportAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.routeAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.revisitAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.keyBusinessAction)      
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.routesAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.discontinueAction)
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        
        toolBarPalette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
       
        self.toolbar.setAutoFillBackground(1)
        self.toolbar.setPalette(toolBarPalette)
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        
        self.toolbar.setGeometry(0,0,2000,50)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
       # fileMenu = self.menubar.addMenu('Exit1')
       # fileMenu.addAction(exitAction)     

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "KP Smart - SWEN301 (A Team)", None))
        #self.bt_hubs.setText(_translate("MainWindow", "Hubs", None))
        #self.bt_Routes.setText(_translate("MainWindow", "Routes", None))
       # self.bt_MailItems.setText(_translate("MainWindow", "Mail Items", None))
        #self.bt_Companys.setText(_translate("MainWindow", "Companies", None))
       # self.bt_Reports.setText(_translate("MainWindow", "Reports", None))
        self.menuHome.setTitle(_translate("MainWindow", "Home", None))
        self.menuAdd_Hub.setTitle(_translate("MainWindow", "Actions", None))
        self.actionAdd_Hub.setText(_translate("MainWindow", "Hubs", None))
        self.actionAdd_Route.setText(_translate("MainWindow", "Routes", None))
        self.actionAdd_Mail_Item.setText(_translate("MainWindow", "Mail Items", None))
        self.actionAdd_Company.setText(_translate("MainWindow", "Companys", None))
        

