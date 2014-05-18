'''
Created on 10/05/2014

@author: Alix
'''
from PyQt4.QtSql import *;
from PyQt4 import QtGui, Qt
import KeyEventsCommandHandler as events_handler
from ui import Ui_KPS_KeyFigures as ui_key_figures;

class Database:
    def __init__(self, parent = None):
        self.data = QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Database/Business.db")
        self.data.open()

class Key_Figures_Dialog(QtGui.QDialog):
    def __init__(self, parent = Qt.QObject):
        super(Key_Figures_Dialog, self).__init__()
        self.ui = ui_key_figures.Ui_Dialog()
        self.ui.setupUi(self)
        
        self.db = Database()

        self.ui.label_4.setText(self.totalRevenue())
        self.ui.label_5.setText(self.totalExpenditure())
        self.ui.label_6.setText(self.totalNoEvents())
        
        self.ui.tableView.setModel(self.amountOfMail())
        self.ui.tableView_2.setModel(self.criticalRoutes())
        self.ui.tableView_3.setModel(self.averageDelTime())
        
        #self.ui.tableView.show()
        
    def totalRevenue(self):
        tup = events_handler.getTotalRevenue()
        return tup[0]
    
    def totalExpenditure(self):
        tup = events_handler.getTotalExpenditure()
        return tup[0]
    
    def totalNoEvents(self):
        tup = events_handler.getTotalNumberOfEvents()
        return str(tup[0])
    
    def amountOfMail(self):
        model = QSqlQueryModel()
        model.setQuery('''SELECT origin, destination, sum(volume), sum(weight), count(*)
                    FROM mail
                    group by origin''')
        model.setHeaderData(2, Qt.Qt.Horizontal, "Total Volume")
        model.setHeaderData(3, Qt.Qt.Horizontal, "Total Weight")
        model.setHeaderData(4, Qt.Qt.Horizontal, "Total Count")
        return model
    
    def criticalRoutes(self):
        model = QSqlQueryModel()
        model.setQuery('''SELECT C.Name, R.Name, R.Priority, R.Loss
                FROM(SELECT Q.Origin, C.Name, P.Priority, Q.Loss
                    FROM(SELECT Origin, Destination, Priority, avg(costKPS-costClient) as Loss
                        FROM Mail
                        WHERE costKPS > costClient
                        GROUP BY Origin, Destination, Priority) as Q, Priorities as P, Cities as C
                    WHERE P.ID = Q.Priority AND C.ID = Q.Destination) as R, Cities as C
                WHERE C.ID = R.Origin;''')
        model.setHeaderData(0, Qt.Qt.Horizontal, "Origin")
        model.setHeaderData(1, Qt.Qt.Horizontal, "Destination")
        model.setHeaderData(2, Qt.Qt.Horizontal, "Priority")
        model.setHeaderData(3, Qt.Qt.Horizontal, "Average Loss")
        return model
    
    def averageDelTime(self): # this doesn't work if the DeliverTime column doesn't exist...
        model = QSqlQueryModel()
        model.setQuery('''SELECT origin, destination, priority, avg(DeliverTime)
                FROM mail
                group by origin, destination, priority;''')
        model.setHeaderData(3, Qt.Qt.Horizontal, "Time")
        return model

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Key_Figures_Dialog()
    Dialog.show()
    sys.exit(app.exec_())