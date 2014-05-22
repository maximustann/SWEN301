
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
        self.treeView.setGeometry(QtCore.QRect(20, 200, 661, 341))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(25, 190, 221, 21))
        self.label_2.setStyleSheet("Color: white;")
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        self.label_2.setFont(font)
      
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setText(_translate("MainWindow", "Customer Routes", None))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 321, 81))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Images/logo_small.png")))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdd_Item = QtGui.QMenu(self.menubar)
        self.menuAdd_Item.setObjectName(_fromUtf8("menuAdd_Item"))
        self.menuAdd_Hub = QtGui.QMenu(self.menubar)
        self.menuAdd_Hub.setObjectName(_fromUtf8("menuAdd_Hub"))
        
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Hub = QtGui.QAction(MainWindow)
        self.actionAdd_Hub.setObjectName(_fromUtf8("actionAdd_Hub"))
        self.actionAdd_TransportRoute = QtGui.QAction(MainWindow)
        self.actionAdd_TransportRoute.setObjectName(_fromUtf8("actionAdd_TransportRoute"))
        self.actionAdd_CustomerRoute = QtGui.QAction(MainWindow)
        self.actionAdd_CustomerRoute.setObjectName(_fromUtf8("actionAdd_CustomerRoute"))
        self.actionAdd_Mail_Item = QtGui.QAction(MainWindow)
        self.actionAdd_Mail_Item.setObjectName(_fromUtf8("actionAdd_Mail_Item"))
        self.actionAdd_Company = QtGui.QAction(MainWindow)
        self.actionAdd_Company.setObjectName(_fromUtf8("actionAdd_Company"))
        self.actionAdd_History = QtGui.QAction(MainWindow)
        self.actionAdd_History.setObjectName(_fromUtf8("actionAdd_History"))
        self.actionAdd_KeyFigures = QtGui.QAction(MainWindow)
        self.actionAdd_KeyFigures.setObjectName(_fromUtf8("actionAdd_KeyFigures"))
        
        self.actionAdd_ViewRoutes = QtGui.QAction(MainWindow)
        self.actionAdd_ViewRoutes.setObjectName(_fromUtf8("actionAdd_ViewRoutes"))
        
        self.actionAdd_DiscontinueRoutes = QtGui.QAction(MainWindow)
        self.actionAdd_DiscontinueRoutes.setObjectName(_fromUtf8("actionAdd_DiscontinueRoutes"))
        
        self.menuAdd_Hub.addAction(self.actionAdd_Mail_Item)
        self.menuAdd_Hub.addAction(self.actionAdd_Hub)
        self.menuAdd_Hub.addAction(self.actionAdd_TransportRoute)
        self.menuAdd_Hub.addAction(self.actionAdd_CustomerRoute)
        self.menuAdd_Hub.addAction(self.actionAdd_History)
        self.menuAdd_Hub.addAction(self.actionAdd_KeyFigures)
        
        self.menuAdd_Hub.addAction(self.actionAdd_ViewRoutes)
        self.menuAdd_Hub.addAction(self.actionAdd_DiscontinueRoutes)
              
        self.menubar.addAction(self.menuAdd_Hub.menuAction())
        
        self.routeAction = QtGui.QAction(QtGui.QIcon('Images/route.png'), 'Update Customer Price', MainWindow)
        
        self.routeAction.setShortcut('Ctrl+R')
        self.routeAction.setIconText('Update Customer Price')
        
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
        self.addHubAction.setIconText('Add City')
        
        self.addMailAction = QtGui.QAction(QtGui.QIcon('Images/mailitem.png'), 'Mail Item', MainWindow)
        self.addMailAction.setShortcut('Ctrl+M')
        self.addMailAction.setIconText('Add Mail')
        
        self.routesAction = QtGui.QAction(QtGui.QIcon('Images/routes.png'), 'Routes', MainWindow)
        self.routesAction.setShortcut('Ctrl+R')
        self.routesAction.setIconText('Transport Routes')
        
        self.transportAction = QtGui.QAction(QtGui.QIcon('Images/transport.png'), 'Update Transport Cost', MainWindow)
        self.transportAction.setShortcut('Ctrl+R')
        self.transportAction.setIconText('Update Transport Cost')
        
        self.discontinueAction = QtGui.QAction(QtGui.QIcon('Images/discontinue.png'), 'Discontinue Transport Route', MainWindow)
        self.discontinueAction.setShortcut('Ctrl+R')
        self.discontinueAction.setIconText('Discontinue Route')
   
        self.exitAction.triggered.connect(self.parent.close)
        
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
        self.menuAdd_Hub.setTitle(_translate("MainWindow", "Menu", None))
        self.actionAdd_Hub.setText(_translate("MainWindow", "Add City", None))
        self.actionAdd_TransportRoute.setText(_translate("MainWindow", "Update Transport Cost", None))
        self.actionAdd_CustomerRoute.setText(_translate("MainWindow", "Update Customer Price", None))
        self.actionAdd_Mail_Item.setText(_translate("MainWindow", "Add Mail", None))
        self.actionAdd_Company.setText(_translate("MainWindow", "MCompanys", None))
        self.actionAdd_History.setText(_translate("MainWindow", "History", None))
        self.actionAdd_KeyFigures.setText(_translate("MainWindow", "Key Figures", None))
        
        self.actionAdd_ViewRoutes.setText(_translate("MainWindow", "Transport Routes", None))
        self.actionAdd_DiscontinueRoutes.setText(_translate("MainWindow", "Discontinue Route", None))
