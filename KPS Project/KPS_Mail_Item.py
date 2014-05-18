#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
from ui import Ui_KPS_Mail_Item as ui_mail_item
import sqlite3 as lite
import time
import mail_item
import graph
import dij


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
        self.cur.execute("SELECT Priority from Priorities")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_3.addItem(row[0])
    def setOrigin(self):
        self.cur.execute("SELECT name from Cities")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_4.addItem(row[0])
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
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_2.addItem(row[0])
    def trans(self):
        sql = str("SELECT ID FROM Cities WHERE Name=\"" + self.mail.origin + "\"")
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == None:
            print("Database Error!")
        else:
            self.mail.origin = row[0]

        sql = str("SELECT ID FROM Cities WHERE Name=\"" + self.mail.destination+ "\"")
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row == None:
            print("Database Error!")
        else:
            self.mail.destination = row[0]
    def getValue(self):
        origin = self.ui.comboBox_4.currentText()
        destination = self.ui.comboBox_2.currentText()
        print destination
        priority = self.ui.comboBox_3.currentText()
        weight = self.ui.lineEdit_3.text()
        volume = self.ui.lineEdit_4.text()
        entrytime = time.time()
        self.mail = mail_item.Mail_Item(
                    origin,
                    priority,
                    destination,
                    weight,
                    volume,
                    entrytime
               )
        self.trans()
        self.transport_cost()
        self.construct_graph()
        return self.mail

    def transport_cost(self):
        route = []
        self.transport = []
        sql = str("SELECT * from TransportRoutes")
        self.cur.execute(sql)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            route.append(row[1]) #origin
            route.append(row[2]) #destination
            route.append(row[3]) #company
            route.append(row[4]) #transportType
            route.append(row[5]) #deliverDay
            cost = row[6] * float(self.mail.weight)
            cost += row[7] * float(self.mail.volume)
            route.append(cost)  #Pricegram * weight + PriceCC * volume
            route.append(row[9]) #duration
            self.transport.append(route)
            route = []
        self.trans_filter()

    def construct_graph(self):
        self.G = {}
        raw_data = []
        charge = 0
        for i in range(len(self.new_transport)):
            data = {}
            dest = {}
            origin_city = self.new_transport[i][0]
            dest_city = self.new_transport[i][1]
            dest[dest_city] = self.new_transport[i][5]
            data[origin_city] = dest
            raw_data.append(data)
        for meta in raw_data:
            graph.make_link(self.G, meta.keys()[0], meta.values()[0].keys()[0], meta.values()[0].values()[0])

        self.path = dij.shortestPath(self.G, self.mail.origin, self.mail.destination)
        for i in range(len(self.path) - 1):
            charge += self.G[self.path[i]][self.path[i + 1]]

        self.mail.costKPS = charge
        print self.cal_duration()

    def cal_duration(self):
        duration = 0
        for i in range(len(self.path) - 1):
            for j in range(len(self.new_transport)):
                if (self.new_transport[j][0] == self.path[i]) and (self.new_transport[j][1] == self.path[i + 1]):
                    print self.new_transport[j][7]
                    duration += self.new_transport[j][7]
        return duration

    def trans_filter(self):
        self.new_transport = []
        temp = None
        i = 0
        while True:
            if i > len(self.transport) - 2:
                break
            if temp == None:
                if (self.transport[i][0] == self.transport[i + 1][0]) and (self.transport[i][1] == self.transport[i + 1][1]):
                    if self.transport[i][5] >= self.transport[i + 1][5]:
                        temp = self.transport[i]
                        i += 1
                    else:
                        temp = self.transport[i + 1]
                        i += 1
                else:
                    self.new_transport.append(self.transport[i])
                    i += 1
            else:
                if (self.transport[i][0] == temp[0]) and (self.transport[i][1] == temp[1]):
                    if self.transport[i][5] >= temp[5]:
                        temp = self.transport[i]
                        i += 1
                    else:
                        i += 1
                else:
                    self.new_transport.append(temp)
                    temp = None
                    i += 1
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
    Dialog.getValue()
    Dialog.trans()
