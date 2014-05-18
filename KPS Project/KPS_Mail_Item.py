#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_KPS_Mail_Item as ui_mail_item
import sqlite3 as lite
import time
import mail_item


class Mail_Item_Dialog(QtGui.QDialog):
    def __init__(self):
        super(Mail_Item_Dialog, self).__init__()
        self.ui = ui_mail_item.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.comboBox_4.currentIndexChanged.connect(self.change_destination)
        self.conn = None
        self.cur = None
        self.history_city = None
        self.connect()
        self.cur = self.conn.cursor()
        self.setOrigin()
        self.setPriority()
        self.setDestination()
        self.init_destination()



    def connect(self):
        try:
            self.conn = lite.connect("../Database/Business.db")
        except lite.Error, e:
            print("Error %s:" % e.args[0])
            sys.exit(1)

    def init_destination(self):
        origin_city = self.ui.comboBox_4.currentText()
        dest_city = self.ui.comboBox_2.findText(origin_city)
        if dest_city != -1:
            self.ui.comboBox_2.removeItem(dest_city)
            self.history_city = origin_city

    def change_destination(self):
        origin_city = self.ui.comboBox_4.currentText()
        if self.history_city == None:
            print origin_city
            dest_city = self.ui.comboBox_2.findText(origin_city)
            if dest_city != -1:
                self.ui.comboBox_2.removeItem(dest_city)
                self.history_city = origin_city
        else:
            self.ui.comboBox_2.addItem(self.history_city)
            dest_city = self.ui.comboBox_2.findText(origin_city)
            if dest_city != -1:
                self.ui.comboBox_2.removeItem(dest_city)
                self.history_city = origin_city
    def setPriority(self):
        self.ui.comboBox_3.addItem("")
        self.ui.comboBox_3.addItem("")
        self.ui.comboBox_3.setItemText(0, "1")
        self.ui.comboBox_3.setItemText(1, "2")
    def setOrigin(self):
        self.cur.execute("SELECT name from Cities")
        i = 0
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_4.addItem("")
            self.ui.comboBox_4.setItemText(i, row[0])
            i += 1
    '''        
    def setTransportType(self):
        self.cur.execute("SELECT Type from TransportTypes")
        i = 0
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox.addItem("")
            self.ui.comboBox.setItemText(i, row[0])
            i += 1
'''
    def setDestination(self):
        self.cur.execute("SELECT name from Cities")
        i = 0
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.setItemText(i, row[0])
            i += 1
    def getValue(self):
        origin = self.ui.comboBox_4.currentText()
        destination = self.ui.comboBox_2.currentText()
        priority = self.ui.comboBox_3.currentText()
        types = self.ui.comboBox.currentText()
        weight = self.ui.lineEdit_3.text()
        volume = self.ui.lineEdit_4.text()
        entrytime = time.time()
        mail = mail_item.Mail_Item(
                    origin,
                    priority,
                    types,
                    destination,
                    weight,
                    volume,
                    entrytime
               )
        return mail
'''
    def change_types(self):
        if(self.ui.comboBox_3.currentText() == '2'):
            air = self.ui.comboBox.findText("Air")
            if air != -1:
                self.ui.comboBox.removeItem(air)
            land = self.ui.comboBox.findText("Land")
            if land == -1:
                self.ui.comboBox.addItem("Land")
            sea = self.ui.comboBox.findText("Sea")
            if sea == -1:
                self.ui.comboBox.addItem("Sea")
        if(self.ui.comboBox_3.currentText() == '1'):
            land = self.ui.comboBox.findText("Land")
            if land != -1:
                self.ui.comboBox.removeItem(land)
            sea = self.ui.comboBox.findText("Sea")
            if sea != -1:
                self.ui.comboBox.removeItem(sea)
            air = self.ui.comboBox.findText("Air")
            if air == -1:
                self.ui.comboBox.addItem("Air")
'''
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Mail_Item_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
