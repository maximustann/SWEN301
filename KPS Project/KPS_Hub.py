#!/usr/bin/env python

from PyQt4 import QtGui, QtCore, QtSql
from ui import Ui_KPS_Hub as ui_hub;

class Database:
    def __init__(self, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Database/Business.db")
        self.data.open()

class Hub_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Hub_Dialog, self).__init__()
        self.ui = ui_hub.Ui_wn_Hubs()
        self.ui.setupUi(self)
        self.db = Database()
        self.setHubs()
        self.ui.bt_Add_Hub.clicked.connect(self.AddHub)
        
    def setHubs(self):
        modelView = QtGui.QStandardItemModel()
        query = QtSql.QSqlQuery()
        query.exec_("Select * from Cities order by Name")
        while query.next():
                modelValue = QtGui.QStandardItem(query.value(1).toString())
                modelView.appendRow(modelValue)
        self.ui.listView.setModel(modelView)   
        
    def AddHub(self):
            if self.ui.lineEdit.text() != "":
                query = QtSql.QSqlQuery()
                query.exec_("insert into Cities (Name) values ('" + self.ui.lineEdit.text() + "')")
                self.ui.lineEdit.setText("")
                self.setHubs()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Hub_Dialog()
    Dialog.show()
    sys.exit(app.exec_())


