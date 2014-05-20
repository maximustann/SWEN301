# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KPS_RevisitBusinessEvents.ui'
#
# Created: Sun May 18 14:50:49 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtSql
import sqlite3


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

class Ui_Form(object):
   
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(666, 538)
        palette = QtGui.QPalette()
        self.eventSkip = 0;
        self.db = Database()
      
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)  
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        
        self.inWork = True
        
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)  
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 129, 2))
        brush.setStyle(QtCore.Qt.SolidPattern)
        
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        self.tb_EventViewer = QtGui.QTableView(Form)
        self.tb_EventViewer.setGeometry(QtCore.QRect(60, 120, 531, 351))
        self.tb_EventViewer.setObjectName(_fromUtf8("tb_EventViewer"))
        self.tb_EventViewer.horizontalHeader().setVisible(False)
        self.tb_EventViewer.verticalHeader().setVisible(False)
       # self.tb_EventViewer.setColumnCount(0)
       # self.tb_EventViewer.setRowCount(0)
        self.bt_Earlier = QtGui.QPushButton(Form)
        self.bt_Earlier.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.bt_Earlier.setObjectName(_fromUtf8("bt_Earlier"))
        self.bt_Earlier.clicked.connect(self.clicked_bt_Earlier)
        
        
        self.bt_Later = QtGui.QPushButton(Form)
        self.bt_Later.setGeometry(QtCore.QRect(510, 90, 75, 23))
        self.bt_Later.setObjectName(_fromUtf8("bt_Later"))
        self.bt_Later.clicked.connect(self.clicked_bt_Later)
        
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 0, 511, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Light"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cb_EventType = QtGui.QComboBox(Form)
        self.cb_EventType.setGeometry(QtCore.QRect(230, 50, 221, 22))
        self.cb_EventType.setObjectName(_fromUtf8("cb_EventType"))  
        self.cb_EventType.currentIndexChanged['QString'].connect(self.handleChanged)       
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 50, 121, 21))
        
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(190, 90, 221, 21))
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.initialize()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Revisit business events", None))
        self.bt_Earlier.setText(_translate("Form", "<<", None))
        self.bt_Later.setText(_translate("Form", ">>", None))
        self.label.setText(_translate("Form", "Revisit business events", None))
        self.label_2.setText(_translate("Form", "Select Event Type", None))
       
    
    def initialize(self):
       self.cb_EventType.addItems(self.getBusinessEventsType())
      #  self.cb_Destination.addItems(RH.getLocations())
      
    def getBusinessEventsType(self):
        conn = sqlite3.connect("../Database/Business.db")
        conn.text_factory = str
        c = conn.cursor()
        c.execute('SELECT Event FROM EventTypes')
        locs = [r[0] for r in c.fetchall()]
        conn.close()
        return locs
    
    def handleChanged(self, text):
        modelView = QtGui.QStandardItemModel()
        query = QtSql.QSqlQuery()

        query.exec_("Select * from BusinessEvents a, EventTypes b where b.Event = '" + text + "' and b.EventTypeID = a.EventTypeID order by ID DESC LIMIT " + str(self.eventSkip) + ",1")
        recCount = 0;
  
        while query.next():
            recCount = recCount + 1
            if  query.value(2).toString() != '':
                query_Origin = QtSql.QSqlQuery()
                query_Origin.exec_("Select Name from Cities where ID = '" + query.value(2).toString() + "' LIMIT 1")
                query_Origin.next()
                modelInputItem = QtGui.QStandardItem("Origin")
                modelInputValue = QtGui.QStandardItem(query_Origin.value(0).toString())
                modelView.appendRow([modelInputItem,modelInputValue])
            if  query.value(3).toString() != '':
                query_Destination = QtSql.QSqlQuery()
                query_Destination.exec_("Select Name from Cities where ID = '" + query.value(3).toString() + "' LIMIT 1")
                query_Destination.next()
                modelInputItem = QtGui.QStandardItem("Destination")
                modelInputValue = QtGui.QStandardItem(query_Destination.value(0).toString())
                modelView.appendRow([modelInputItem,modelInputValue])    
            if  query.value(4).toString() != '':
                modelInputItem = QtGui.QStandardItem("Weight")
                modelInputValue = QtGui.QStandardItem(query.value(4).toString())
                modelView.appendRow([modelInputItem,modelInputValue])    
            if  query.value(5).toString() != '':
                modelInputItem = QtGui.QStandardItem("Volume")
                modelInputValue = QtGui.QStandardItem(query.value(5).toString())
                modelView.appendRow([modelInputItem,modelInputValue])     
            if  query.value(6).toString() != '':
                modelInputItem = QtGui.QStandardItem("Time of Entry")
                modelInputValue = QtGui.QStandardItem(query.value(6).toString())
                modelView.appendRow([modelInputItem,modelInputValue])
            if  query.value(7).toString() != '':
                modelInputItem = QtGui.QStandardItem("Priority")
                modelInputValue = QtGui.QStandardItem(query.value(7).toString())
                modelView.appendRow([modelInputItem,modelInputValue])
            if query.value(8).toString() != '':
                modelInputItem = QtGui.QStandardItem("Price Per Gram")
                modelInputValue = QtGui.QStandardItem(query.value(8).toString())
                modelView.appendRow([modelInputItem,modelInputValue])
            if query.value(9).toString() != '':
                modelInputItem = QtGui.QStandardItem("Price Per CC")
                modelInputValue = QtGui.QStandardItem(query.value(9).toString())
                modelView.appendRow([modelInputItem,modelInputValue]) 
            if query.value(10).toString() != '':
                modelInputItem = QtGui.QStandardItem("Company")
                modelInputValue = QtGui.QStandardItem(query.value(10).toString())
                modelView.appendRow([modelInputItem,modelInputValue])   
            if query.value(11).toString() != '':
                modelInputItem = QtGui.QStandardItem("Transport Type")
                modelInputValue = QtGui.QStandardItem(query.value(11).toString())
                modelView.appendRow([modelInputItem,modelInputValue]) 
            if query.value(12).toString() != '':
                modelInputItem = QtGui.QStandardItem("Day of the Week")
                modelInputValue = QtGui.QStandardItem(query.value(12).toString())
                modelView.appendRow([modelInputItem,modelInputValue]) 
            if query.value(13).toString() != '':
                modelInputItem = QtGui.QStandardItem("Frequency")
                modelInputValue = QtGui.QStandardItem(query.value(13).toString())
                modelView.appendRow([modelInputItem,modelInputValue]) 
            if query.value(14).toString() != '':
                modelInputItem = QtGui.QStandardItem("Duration")
                modelInputValue = QtGui.QStandardItem(query.value(14).toString())
                modelView.appendRow([modelInputItem,modelInputValue]) 
        #modelInputValue = QtGui.QStandardItem('Value')
        # modelView.appendRow([modelInputItem,modelInputValue])
        if recCount == 0:
            self.label_3.setText(_translate("Form", "No Records found", None))
            self.inWork = False
        else:
            self.label_3.setText(_translate("Form", "", None))
            self.inWork = True
               
        self.tb_EventViewer.setModel(modelView)
 
    def clicked_bt_Earlier(self):
        self.eventSkip = self.eventSkip + 1
        self.handleChanged(self.cb_EventType.currentText())
        
    def clicked_bt_Later(self):
        if self.eventSkip > 0:
            self.eventSkip = self.eventSkip - 1    
            self.handleChanged(self.cb_EventType.currentText())
        
class Database:
    def __init__(self, parent = None):
        self.data = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.data.setDatabaseName("../Database/Business.db")
        self.data.open()
