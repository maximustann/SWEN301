from PyQt4 import QtCore,QtGui;
from PyQt4.QtSql import *;

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Database:
    def __init__(self, parent = None):
        self.data = QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("test.db")
        self.data.open()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(364, 215)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tbx_Record1 = QtGui.QLineEdit(Dialog)
        self.tbx_Record1.setGeometry(QtCore.QRect(150, 30, 171, 20))
        self.tbx_Record1.setObjectName(_fromUtf8("tbx_Record1"))
        self.tbx_Record2 = QtGui.QLineEdit(Dialog)
        self.tbx_Record2.setGeometry(QtCore.QRect(150, 70, 171, 20))
        self.tbx_Record2.setObjectName(_fromUtf8("tbx_Record2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Test Window", None))
        self.label.setText(_translate("Dialog", "Record 1", None))
        self.label_2.setText(_translate("Dialog", "Record 2", None))
        
class Ui_MainWindow(object):      
    
    def setupUi(self, MainWindow):
    
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 465)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(110, 130, 661, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.db = Database()
        self.model = QSqlTableModel()
        self.model.setTable("Table1")
        self.model.select()
        self.tableView.setModel(self.model)
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kelburn Postal Service", None))
        self.pushButton.setText(_translate("MainWindow", "Add Item", None))
        
    def buttonClicked(self):
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        result = Dialog.exec_()
        if result == 1:
                Record1 = ui.tbx_Record1.text()
                Record2 = ui.tbx_Record2.text()
                self.insertData(Record1, Record2)
                self.model.select()
                self.tableView.setModel(self.model)
        
    def insertData(self,R1,R2):
        import sqlite3
        conn = sqlite3.connect('test.db')
        conn.execute("INSERT INTO Table1 (Record1,Record2) values ('" + R1 + "','" + R2 + "')")
        conn.commit()
        conn.close()

if __name__ == '__main__':
    import sys
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
