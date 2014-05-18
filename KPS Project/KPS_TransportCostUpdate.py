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
        self.ui.bt_Select_Route.clicked.connect(self.selectRoute)
       
        self.ui.cb_Origin.addItems(RH.getLocations())
        self.ui.cb_Destination.addItems(RH.getLocations())
        self.ui.cb_TransportType.addItems(RH.getTransportTypes())
        self.ui.cb_DayOfWeek.addItems(RH.getDaysOfWeek())
        
        self.ui.cb_Origin.currentIndexChanged.connect(self.updateDisplayedRoutes)
        

    def clicked_bt_Add_Event(self):
        costUpdate = dict(
        Origin = int(self.ui.cb_Origin.currentIndex() + 1),
        Destination = int(self.ui.cb_Destination.currentIndex() + 1),
        Firm = str(self.ui.tb_Firm.text()),
        TransportType = str(self.ui.cb_TransportType.currentText()),
        PricePerGram = self.ui.tb_PriceG.text(),
        PricePerCC = self.ui.tb_PriceCC.text(),
        DayOfWeek = int(self.ui.cb_DayOfWeek.currentIndex() + 1),
        Frequency = self.ui.tb_Frequency.text(),
        Duration = self.ui.tb_Duration.text())
        if len(EH.insertTransportCost(costUpdate))==0:
            return
    
    def selectRoute(self):
        print "Select Route"
        
    def updateDisplayedRoutes(self):
        model = QStandardItemModel()
        self.ui.lv_availableRoutes.setModel(model)
        item = QStandardItem('Dog')
        model.appendRow(item)
        item2 = QStandardItem('Cat')
        model.appendRow(item2)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Ui_KPS_TransportCostUpdate()
    Dialog.show()
    sys.exit(app.exec_())