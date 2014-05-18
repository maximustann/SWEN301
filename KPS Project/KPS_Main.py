#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *;
from PyQt4.QtGui import *;
import KPS_Hub as hub;
import KPS_TransportCostUpdate as transportCostUpdate;
import KPS_Login as login;
import KPS_Key_Figures as KeyFigures;
import KPS_Mail_Item as MailItem;
import KPS_CustomerPriceUpdate as Routes;
import KPS_RevisitBusinessEvents as RevisitBusinessEvents;
from ui import Ui_KPS_Main as ui_main;


class KPS_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        '''
        user = self.login()
        if user == None:
            sys.exit(-1)
        '''
        super(KPS_MainWindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow(self)
        self.ui.setupUi(self)

  
        #self.ui.bt_hubs.clicked.connect(self.clicked_bt_Hubs)
       # self.ui.bt_Routes.clicked.connect(self.clicked_bt_Routes)

        self.ui.routeAction.triggered.connect(self.clicked_bt_Routes)
        self.ui.keyBusinessAction.triggered.connect(self.clicked_bt_keyBusiness)
        self.ui.addHubAction.triggered.connect(self.clicked_bt_Hubs)
        self.ui.addMailAction.triggered.connect(self.clicked_bt_MailItem)
        self.ui.revisitAction.triggered.connect(self.clicked_bt_Revisit)      
        self.ui.transportAction.triggered.connect(self.clicked_bt_Transportcost)
        
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Hub', 'Destination','Void'])
        self.ui.treeView.setModel(model)
        self.ui.treeView.setUniformRowHeights(True)
        
        parent1 = QStandardItem('Auckland')
        child1 = QStandardItem('Sydney')
        child2 = QStandardItem('Wellington')
        parent1.appendRow([child1, child2])
        
        model.appendRow(parent1)
        for i in range(3):
            parent1 = QStandardItem('Family {}. Some long estatus text for sp'.format(i))
            for j in range(3):
                child1 = QStandardItem('Child {}'.format(i*3+j))
                child2 = QStandardItem('row: {}, col: {}'.format(i, j+1))
                child3 = QStandardItem('row: {}, col: {}'.format(i, j+2))
                parent1.appendRow([child1, child2, child3])
            model.appendRow(parent1)
        self.ui.treeView.setFirstColumnSpanned(i, self.ui.treeView.rootIndex(), True)

    def login(self):
        Dialog = login.My_Dialog()
        Dialog.show()
        result = Dialog.exec_()
        if result == 1:
            return Dialog.get_value()
   
    def clicked_bt_Hubs(self):
        Dialog = hub.Hub_Dialog()     
        Dialog.show()
        result = Dialog.exec_()
        
    def clicked_bt_keyBusiness(self):
        Dialog = KeyFigures.Key_Figures_Dialog()
        Dialog.show()
        result = Dialog.exec_()

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
        
    def clicked_bt_Routes(self):
        Dialog = Routes.CustomerPriceUpdate_Dialog()
        Dialog.show()
        result = Dialog.exec_()

if __name__ == '__main__':
         import sys        
         app = QtGui.QApplication(sys.argv)
         MainWindow = KPS_MainWindow()
         MainWindow.show()
         sys.exit(app.exec_())
