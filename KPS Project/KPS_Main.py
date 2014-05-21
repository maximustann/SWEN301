#!/usr/bin/env python

from PyQt4 import QtGui, QtCore,QtSql
from PyQt4.QtCore import *;
from PyQt4.QtGui import *;
import KPS_Hub as hub;
import KPS_TransportCostUpdate as transportCostUpdate;
import KPS_Login as login;
import KPS_TransportRoutes as TransportRoutes;
import KPS_Key_Figures as KeyFigures;
import KPS_TransportDiscontinued as TransportDiscontinued
import KPS_Mail_Item as MailItem;
import KPS_CustomerPriceUpdate as Routes;
import KPS_RevisitBusinessEvents as RevisitBusinessEvents;
import locale

from ui import Ui_KPS_Main as ui_main;

class Database:
    def __init__(self, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Database/Business.db")
        self.data.open()

class KPS_MainWindow(QtGui.QMainWindow):
    def __init__(self):

        user = self.login()
        if user == None:
            sys.exit(-1)
        
        self.db = Database()
        super(KPS_MainWindow, self).__init__()
        
        self.ui = ui_main.Ui_MainWindow(self)
        self.ui.setupUi(self)
        locale.setlocale( locale.LC_ALL, '' )
        if user==0:
            self.ui.keyBusinessAction.setEnabled(0)
            self.ui.revisitAction.setEnabled(0)
            self.ui.actionAdd_History.setEnabled(0)
            self.ui.actionAdd_KeyFigures.setEnabled(0)

  
        #self.ui.bt_hubs.clicked.connect(self.clicked_bt_Hubs)
       # self.ui.bt_Routes.clicked.connect(self.clicked_bt_Routes)

        self.ui.routeAction.triggered.connect(self.clicked_bt_Routes)
        self.ui.keyBusinessAction.triggered.connect(self.clicked_bt_keyBusiness)
        self.ui.addHubAction.triggered.connect(self.clicked_bt_Hubs)
        self.ui.addMailAction.triggered.connect(self.clicked_bt_MailItem)
        self.ui.revisitAction.triggered.connect(self.clicked_bt_Revisit)      
        self.ui.transportAction.triggered.connect(self.clicked_bt_Transportcost)
        self.ui.discontinueAction.triggered.connect(self.clicked_bt_Discontinue)
        self.ui.routesAction.triggered.connect(self.clicked_bt_TransportRoutes)
        
        self.ui.actionAdd_Mail_Item.triggered.connect(self.clicked_bt_MailItem)
        self.ui.actionAdd_Hub.triggered.connect(self.clicked_bt_Hubs)
        self.ui.actionAdd_TransportRoute.triggered.connect(self.clicked_bt_Transportcost)
        self.ui.actionAdd_CustomerRoute.triggered.connect(self.clicked_bt_Routes)
        self.ui.actionAdd_History.triggered.connect(self.clicked_bt_Revisit)
        self.ui.actionAdd_KeyFigures.triggered.connect(self.clicked_bt_keyBusiness)
        self.ui.actionAdd_ViewRoutes.triggered.connect(self.clicked_bt_TransportRoutes)
        self.ui.actionAdd_DiscontinueRoutes.triggered.connect(self.clicked_bt_Discontinue)
        self.loadTree()
        
       # parent1 = QStandardItem('Auckland')
       # child1 = QStandardItem('Sydney')
       # child2 = QStandardItem('Wellington')
       # parent1.appendRow([child1, child2])
        
     #   model.appendRow(parent1)
     #   for i in range(3):
     #       parent1 = QStandardItem('Family {}. Some long estatus text for sp'.format(i))
    #        for j in range(3):
     #           child1 = QStandardItem('Child {}'.format(i*3+j))
     #           child2 = QStandardItem('row: {}, col: {}'.format(i, j+1))
     #           child3 = QStandardItem('row: {}, col: {}'.format(i, j+2))
       #         parent1.appendRow([child1, child2, child3])
      #      model.appendRow(parent1)
    #    self.ui.treeView.setFirstColumnSpanned(i, self.ui.treeView.rootIndex(), True)

    def loadTree(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Destination', 'Priority','Price Per Gram','Price Per Volume'])
        self.ui.treeView.setModel(model)
        self.ui.treeView.setUniformRowHeights(True)
        self.ui.treeView.setColumnWidth(0,200)
        query = QtSql.QSqlQuery()
        query.exec_("select * from Cities")
        while query.next():
            parent = QStandardItem(query.value(1).toString())
            innerQuery = QtSql.QSqlQuery()
            innerQuery.exec_("select Name,Priority,PricePerGram,PricePerCC from CustomerRoutes a, Cities b where a.Origin = '" + query.value(0).toString() + "' and a.Destination = b.ID")
            while innerQuery.next():
                if str(innerQuery.value(0))  != '':
                    childDestination = QStandardItem(innerQuery.value(0).toString())
                    childPriority = QStandardItem(innerQuery.value(1).toString())
                    childPPG = QStandardItem(locale.currency(float(innerQuery.value(2).toString())))
                    childPCC = QStandardItem(locale.currency(float(innerQuery.value(3).toString())))
                    parent.appendRow([childDestination,childPriority,childPPG,childPCC])
            model.appendRow(parent) 
        self.ui.treeView.setFirstColumnSpanned(3, self.ui.treeView.rootIndex(), True)   
        
    def login(self):
        Dialog = login.Login_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            return Dialog.get_value()
        
   
    def clicked_bt_Hubs(self):
        Dialog = hub.Hub_Dialog()     
        Dialog.show()
        result = Dialog.exec_()
        self.loadTree();
        
    def clicked_bt_keyBusiness(self):
        Dialog = KeyFigures.Key_Figures_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        self.loadTree();
    
    def clicked_bt_TransportRoutes(self):
        Dialog = TransportRoutes.TransportRoutes_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        self.loadTree();


    def clicked_bt_Revisit(self):
        Dialog = RevisitBusinessEvents.RevistBusinessEvents_Dialog()
        Dialog.show()
        result = Dialog.exec_()

    def clicked_bt_Transportcost(self):
        Dialog = transportCostUpdate.TransportCostUpdate_Dialog()
        Dialog.show()
        result = Dialog.exec_()
             
    def clicked_bt_MailItem(self):
        Dialog = MailItem.Mail_Item_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            return Dialog.handle_mail()
    def clicked_bt_Routes(self):
        Dialog = Routes.CustomerPriceUpdate_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        self.loadTree()
        
    def clicked_bt_Discontinue(self):
        Dialog = TransportDiscontinued.TransportDiscontinued_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        self.loadTree()

if __name__ == '__main__':
         import sys        
         app = QtGui.QApplication(sys.argv)
         MainWindow = KPS_MainWindow()
         MainWindow.show()
         sys.exit(app.exec_())

