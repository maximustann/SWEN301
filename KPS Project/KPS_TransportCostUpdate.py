#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *;
from PyQt4.QtCore import *;
from ui import Ui_KPS_TransportCostUpdate;
import RouteCommandHandler as RH;
import BusinessEventHandler as EH;


class TransportCostUpdate_Dialog(QtGui.QDialog):

    def __init__(self):
        super(TransportCostUpdate_Dialog, self).__init__()
        self.ui = Ui_KPS_TransportCostUpdate.Ui_TransportCostUpdate()
        self.ui.setupUi(self)
        self.ui.bt_AddEvent.clicked.connect(self.clicked_bt_Add_Event)    
       
        self.ui.cb_Origin.addItems(RH.getLocations())
        self.ui.cb_Destination.addItems(RH.getLocations())
        self.ui.cb_TransportType.addItems(RH.getTransportTypes())
        self.ui.cb_DayOfWeek.addItems(RH.getDaysOfWeek())
        
        self.ui.cb_Origin.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_Destination.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_TransportType.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_DayOfWeek.currentIndexChanged.connect(self.updateDisplayedRoutes)
        

    def clicked_bt_Add_Event(self):
        costUpdate = dict(
        Origin = int(self.ui.cb_Origin.currentIndex() + 1),
        Destination = int(self.ui.cb_Destination.currentIndex() + 1),
        Company = str(self.ui.tb_Company.text()),
        TransportType = str(self.ui.cb_TransportType.currentText()),
        PricePerGram = self.ui.tb_PriceG.text(),
        PricePerCC = self.ui.tb_PriceCC.text(),
        DayOfWeek = int(self.ui.cb_DayOfWeek.currentIndex() + 1),
        Frequency = self.ui.tb_Frequency.text(),
        Duration = self.ui.tb_Duration.text())
        messages =EH.insertTransportCost(costUpdate)
        if len(messages)==0:
            self.ui.errorLabel.setStyleSheet("color: green")
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
                    Destination = "'"+str(self.ui.cb_Destination.currentText())+"'")
        fields = ['Company','Frequency','Duration']
        routes = RH.getFilteredRoutes(RH.TransportDisplayRoutes,fields,params)
        for route in routes:
            item = QStandardItem('%s : Freq= %s , Duration= %s'%route )
            model.appendRow(item)
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Ui_KPS_TransportCostUpdate()
    Dialog.show()
    sys.exit(app.exec_())