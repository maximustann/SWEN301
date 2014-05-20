#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, QtSql;
from ui import Ui_KPS_TransportRoutes as ui_TransportRoutes;
from PyQt4.QtCore import *;
from PyQt4.QtGui import *;
import locale

class Database:
    def __init__(self, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Database/Business.db")
        self.data.open()


class TransportRoutes_Dialog(QtGui.QDialog):
    def __init__(self):
        super(TransportRoutes_Dialog, self).__init__()
        self.ui = ui_TransportRoutes.Ui_Form()
        self.ui.setupUi(self)
        self.db = Database()
        locale.setlocale( locale.LC_ALL, '' )
        self.loadTree()
   
    def loadTree(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Destination', 'Company','TransportType','DeliverDay','PricePerGram','PricePerCC','Frequency','Duration'])
        self.ui.treeView.setModel(model)
        self.ui.treeView.setUniformRowHeights(True)
        self.ui.treeView.setColumnWidth(0,200)
        query = QtSql.QSqlQuery()
        query.exec_("select * from Cities")
        while query.next():
            parent = QStandardItem(query.value(1).toString())
            innerQuery = QtSql.QSqlQuery()
            innerQuery.exec_("select Name,Company,TransportType,DeliverDay,PricePerGram,PricePerCC,Frequency,Duration from TransportRoutes a, Cities b where a.Origin = '" + query.value(0).toString() + "' and a.Destination = b.ID")
            while innerQuery.next():
                if str(innerQuery.value(0))  != '':
                    childDestination = QStandardItem(innerQuery.value(0).toString())
                    childTransportType = QStandardItem(innerQuery.value(1).toString())
                    childDD = QStandardItem(innerQuery.value(2).toString())
                    childPPG = QStandardItem(innerQuery.value(3).toString())
                    childPPCC = QStandardItem(innerQuery.value(4).toString())
                    childFrequency = QStandardItem(innerQuery.value(5).toString())
                    childDuration = QStandardItem(innerQuery.value(6).toString())
                    #childPPG = QStandardItem(locale.currency(float(innerQuery.value(2).toString())))
                   # childPCC = QStandardItem(locale.currency(float(innerQuery.value(3).toString())))
                    parent.appendRow([childDestination,childTransportType,childDD,childPPG,childPPCC,childFrequency,childDuration])
            model.appendRow(parent) 
        self.ui.treeView.setFirstColumnSpanned(3, self.ui.treeView.rootIndex(), True)  

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = TransportRoutes_Dialog()
    Dialog.show()
    sys.exit(app.exec_())