#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *;
from PyQt4.QtCore import *;
from ui import Ui_KPS_CustomerPriceUpdate;
import RouteCommandHandler as RH;
import BusinessEventHandler as EH;

class CustomerPriceUpdate_Dialog(QtGui.QDialog):
    def __init__(self):
        super(CustomerPriceUpdate_Dialog, self).__init__()
        self.ui = Ui_KPS_CustomerPriceUpdate.Ui_CustomerPriceUpdate()
        self.ui.setupUi(self)
        self.ui.bt_AddEvent.clicked.connect(self.clicked_bt_Add_Event)    
        #self.ui.bt_Select_Route.clicked.connect(self.clicked_bt_Add_Event)
        self.ui.cb_Origin.addItems(RH.getLocations())
        self.ui.cb_Destination.addItems(RH.getLocations())
        self.ui.cb_Priority.addItems(RH.getPriorities())
        self.updateDisplayedRoutes()
        self.ui.cb_Origin.currentIndexChanged.connect(self.updateDisplayedRoutes)  
        self.ui.cb_Destination.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_Priority.currentIndexChanged.connect(self.updateDisplayedRoutes)  

    def clicked_bt_Add_Event(self):
        pUD = dict(
            Origin = int(self.ui.cb_Origin.currentIndex() + 1),
            Destination = int(self.ui.cb_Destination.currentIndex() + 1),
            Priority = int(self.ui.cb_Priority.currentIndex()+1),
            PricePerGram = self.ui.tb_PriceG.text(),
            PricePerCC = self.ui.tb_PriceCC.text()
            )
        messages =EH.updateCustomerPrice(pUD)
        if len(messages)==0:
            self.ui.errorLabel.setStyleSheet("color: white")
            self.ui.errorLabel.setText('Update Complete')
            self.updateDisplayedRoutes()
        else:
            self.ui.errorLabel.setStyleSheet("color: red")
            self.ui.errorLabel.setText(messages[0])
            self.updateDisplayedRoutes()   
            
    def updateDisplayedRoutes(self):
        model = QStandardItemModel()
        self.ui.lv_availableRoutes.setModel(model)
        params = dict(
                    Origin="'"+str(self.ui.cb_Origin.currentText())+"'",
                    Destination = "'"+str(self.ui.cb_Destination.currentText())+"'",
                    Priority = "'"+str(self.ui.cb_Priority.currentText())+"'")
        fields = ['Origin','Destination','Priority']
        routes = RH.getFilteredRoutes(RH.CustomerDisplayRoutes,fields,params)
        for route in routes:
            item = QStandardItem('%s to %s , %s'%route )
            model.appendRow(item)
