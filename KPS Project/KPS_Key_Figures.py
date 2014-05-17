'''
Created on 10/05/2014

@author: Alix
'''
from PyQt4.QtSql import *;
from PyQt4 import QtGui, QtCore
import KeyEventsCommandHandler as events_handler
from ui import Ui_KPS_KeyFigures as ui_key_figures;

class Database: # temporary
    def __init__(self, parent = None):
        self.data = QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("test.db")
        self.data.open()

class Key_Figures_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Key_Figures_Dialog, self).__init__()
        self.ui = ui_key_figures.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.db = Database()
        
        self.ui.label_4.setText(self.totalRevenue()) # label 4 shows total revenue
        self.ui.label_5.setText(self.totalExpenditure()) # 5 is total expenditure
        self.ui.label_6.setText(self.totalNoEvents()) # 6 is total no. of events
        
        self.ui.tableView.setModel(self.amountOfMail()) # this table shows amount of mail
        self.ui.tableView_2.setModel(self.criticalRoutes()) # critical routes
        self.ui.tableView_3.setModel(self.averageTime()) # average delivery time
        
    def totalRevenue(self):
        return events_handler.getTotalRevenue()
    
    def totalExpenditure(self):
        return events_handler.getTotalExpenditure()
    
    def totalNoEvents(self):
        return events_handler.getTotalNumberOfEvents()
    
    def amountOfMail(self): # experimental
        self.model = QSqlTableModel()
        self.model.setTable('Table1')
        # you can add things to model to be displayed in the amountOfMail table   
        self.model.select()
        return self.model
    
    def criticalRoutes(self): # incomplete
        return
    
    def averageTime(self): # incomplete
        return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Key_Figures_Dialog()
    Dialog.show()
    sys.exit(app.exec_())