#!/usr/bin/env python
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *;
from PyQt4.QtCore import *;
from ui import Ui_KPS_TransportDiscontinued;
import RouteCommandHandler as RH;
import BusinessEventHandler as EH;


class TransportDiscontinued_Dialog(QtGui.QDialog):

    def __init__(self):
        super(TransportDiscontinued_Dialog, self).__init__()
        self.ui = Ui_KPS_TransportDiscontinued.Ui_TransportDiscontinued()
        self.ui.setupUi(self)
        self.ui.bt_AddEvent.clicked.connect(self.clicked_bt_Add_Event)    
       
        self.ui.cb_Origin.addItems(RH.getLocations())
        self.ui.cb_Destination.addItems(RH.getLocations())
        self.ui.cb_TransportType.addItems(RH.getTransportTypes())
        
        self.ui.cb_Origin.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_Destination.currentIndexChanged.connect(self.updateDisplayedRoutes)
        self.ui.cb_TransportType.currentIndexChanged.connect(self.updateDisplayedRoutes)

    def clicked_bt_Add_Event(self):
        #if self.ui.lv_availableRoutes.curr
        item = self.ui.lv_availableRoutes.currentIndex()
        if int(item.row()) < 0:
            self.ui.errorLabel.setStyleSheet("color: red")
            self.ui.errorLabel.setText('Select a route')
        else:
            strin = str(item.data().toString())
            values = strin.split(':')
            tdD = dict(Company=values[0],
                        Frequency=values[1],
                        Duration=values[2],
                        DeliverDay=values[3],
                        Origin = int(self.ui.cb_Origin.currentIndex() + 1),
                        Destination = int(self.ui.cb_Destination.currentIndex() + 1),
                        TransportType = str(self.ui.cb_TransportType.currentText())
            )
            messages = EH.discontinueTransport(tdD)
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
                    TransportType = "'"+str(self.ui.cb_TransportType.currentText()+"'"))
        fields = ['Company','Frequency','Duration','DeliverDay']
        routes = RH.getFilteredRoutes(RH.TransportDisplayRoutes,fields,params)
        for route in routes:
            item = QStandardItem('%s:%s:%s:%s'%route )
            model.appendRow(item)
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Ui_KPS_TransportDiscontinued()
    Dialog.show()
    sys.exit(app.exec_())