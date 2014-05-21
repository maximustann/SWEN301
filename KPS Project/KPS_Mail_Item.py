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
        self.ui.comboBox_3.currentIndexChanged.connect(self.change_destination)
        self.conn = None
        self.cur = None
        self.history_city = None
        self.connect()
        self.cur = self.conn.cursor()
        self.setOrigin()
        self.setPriority()
        self.setDestination()
        self.init_destination()

    def accept(self):
        self.ui.label_6.setStyleSheet("color: red")
        self.ui.label_7.setStyleSheet("color: red")
        if self.ui.lineEdit_3.text() == "":
            self.ui.label_6.setText("input weight")
            if self.ui.lineEdit_4.text() == "":
                self.ui.label_7.setText("input volume")
            else:
                self.ui.label_7.setText("")

        if self.ui.lineEdit_4.text() == "":
            self.ui.label_7.setText("input volume")
            if self.ui.lineEdit_3.text() == "":
                self.ui.label_6.setText("input weight")
            else:
                self.ui.label_6.setText("")

        if self.ui.lineEdit_3.text() != "" and self.ui.lineEdit_4.text() != "":
            self.ui.label_6.setText("")
            self.ui.label_7.setText("")
            super(Mail_Item_Dialog, self).accept()
    def connect(self):
        try:
            self.conn = lite.connect("../Database/Business.db")
        except lite.Error, e:
            print("Error %s:" % e.args[0])
            sys.exit(1)

    def init_destination(self):
        origin_city = self.ui.comboBox_3.currentText()
        dest_city = self.ui.comboBox_2.findText(origin_city)
        if dest_city != -1:
            self.ui.comboBox_2.removeItem(dest_city)
            self.history_city = origin_city

    def change_destination(self):
        origin_city = self.ui.comboBox_3.currentText()
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
            self.ui.comboBox.addItem(row[0])
    def setOrigin(self):
        self.cur.execute("SELECT name from Cities")
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            self.ui.comboBox_3.addItem(row[0])
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
        origin = self.ui.comboBox_3.currentText()
        destination = self.ui.comboBox_2.currentText()
        priority = self.ui.comboBox.currentText()
        weight = self.ui.lineEdit_3.text()
        volume = self.ui.lineEdit_4.text()
        entrytime = time.time()
        sql = str("SELECT ID from Priorities where priority=\"" + priority + "\"")
        self.cur.execute(sql)
        row = self.cur.fetchone()
        self.mail = mail_item.Mail_Item(
                    origin,
                    row[0], #priority
                    destination,
                    weight,
                    volume,
                    entrytime
               )
        self.trans()
        if self.transport_cost() == -1:
            return -1
        self.construct_graph()
        self.mail.delivertime = self.cal_duration()
        if self.costclient() == -1:
            return -1
        return self.mail

    def handle_mail(self):
        if self.getValue() != -1:
            self.add_to_db_mail()
        else:
            print("customer route does not exist")
            return -1
    def add_to_db_mail(self):
        sql = str("INSERT INTO Mail(Origin, Destination, costKPS, costClient, Priority, Volume, Weight, TimeOfEntry, DeliverTime) VALUES(" + str(self.mail.origin) + "," +
                                                    str(self.mail.destination) + "," +
                                                    str(self.mail.costkps) + "," +
                                                    str(self.mail.costclient) + "," +
                                                    str(self.mail.priority) + "," +
                                                    str(self.mail.volume) + "," +
                                                    str(self.mail.weight) + "," +
                                                    str(self.mail.entrytime) + "," +
                                                    str(self.mail.delivertime) + ")")
        self.cur.execute(sql)
        row = self.cur.fetchone()
        self.conn.commit()        
       
    def transport_cost(self):
        if self.mail.priority == 1:
            sql = str("SELECT * from TransportRoutes")
        else:
            sql = str("SELECT * from TransportRoutes WHERE TransportType='Air'")
        route = []
        self.transport = []
        self.cur.execute(sql)
        while True:
            row = self.cur.fetchone()
            if row == None:
                break
            route.append(row[1]) #origin new_transport[0]
            route.append(row[2]) #destination  new_transport[1]
            route.append(row[3]) #company new_transport[2]
            route.append(row[4]) #transportType new_transport[3]
            route.append(row[5]) #deliverDay new_transport[4]
            cost = row[6] * float(self.mail.weight)
            cost += row[7] * float(self.mail.volume)
            route.append(cost)  #Pricegram * weight + PriceCC * volume new_transport[5]
            route.append(row[8]) #frequency new_transport[6]
            route.append(row[9]) #duration new_transport[7]
            self.transport.append(route)
            route = []
        if self.trans_filter() == -1:
            return -1
        print self.transport
        #print self.new_transport

    def costclient(self):
        #print str(self.mail.origin), str(self.mail.destination), str(row[0])
        sql = str("SELECT * FROM  CustomerRoutes WHERE Origin=\"" + str(self.mail.origin) +
                    "\" AND Destination=\"" + str(self.mail.destination) + "\" AND Priority=\"" +
                    str(self.mail.priority) + "\"")
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if(row == None):
            print("No Customer Route!!")
            return -1
        cost = row[4] * float(self.mail.weight) + row[5] * float(self.mail.volume)
        self.mail.costclient = cost

    #also count costKPS
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
        #print "charge us=", charge
        self.mail.costkps = charge

    def cal_duration(self):
        duration = 0
        for i in range(len(self.path) - 1):
            #looking for the route in new_tranport
            for j in range(len(self.new_transport)):
                if self.new_transport[j][0] == self.path[i] and self.new_transport[j][1] == self.path[i + 1]:
                    
                    weekday = self._analyse_week(self.mail.entrytime + duration * 3600)
                    deliverday = self.new_transport[j][4]
                    trans_duration = self.new_transport[j][7]
                    frequency = self.new_transport[j][6]

                    hours = self._analyse_hour(self.mail.entrytime + duration * 3600)
                    waiting_time = self._calculate_waiting_time(hours, weekday, deliverday, frequency)
                    if waiting_time != None:
                        duration += waiting_time + trans_duration
        return duration

    def _calculate_waiting_time(self, hours, weekday, deliverday, frequency):
        if weekday == deliverday:
            if hours < 7:
                #print 7 - hours
                return (7 - hours) 
            else:
                for i in range(int((24 - 7) / frequency)):
                    if 7 + frequency * i - hours > 0:
                       # print 7 + frequency * i - hours
                        return 7 + frequency * i - hours
                
        elif weekday > deliverday:
           # print (24 - hours) + (7 - (weekday - deliverday) - 2) * 24 + 7
            return (24 - hours) + (7 - (weekday - deliverday) - 2) * 24 + 7
        else:
           # print (24 - hours) + (deliverday - weekday - 1) * 24 + 7
            return (24 - hours) + (deliverday - weekday - 1) * 24 + 7

    def _analyse_week(self, entrytime):
        return int(time.strftime("%w", time.localtime(entrytime))) + 1

    def _analyse_hour(self, entrytime):
        return int(time.strftime("%H", time.localtime(entrytime)))

    def trans_filter(self):
        if(len(self.transport) == 0):
            print("no transport route")
            return -1
        self.new_transport = []
        temp = None
        i = 0
        #print "size of transport", len(self.transport)
        while True:
            if i >= len(self.transport) - 1:
                if temp != None:
                    self.new_transport.append(temp)
                    try:
                        if self.transport[i] != None:
                            self.new_transport.append(self.transport[i])
                    except IndexError:
                        pass
                break
            if temp == None:
                if (self.transport[i][0] == self.transport[i + 1][0]) and (self.transport[i][1] == self.transport[i + 1][1]):
                    if self.transport[i][5] >= self.transport[i + 1][5]:
                        temp = self.transport[i + 1]
                        i += 2
                    else:
                        temp = self.transport[i]
                        i += 1
                else:
                    self.new_transport.append(self.transport[i])
                    i += 1
            else:
                if (self.transport[i][0] == temp[0]) and (self.transport[i][1] == temp[1]):
                    if self.transport[i][5] < temp[5]:
                        temp = self.transport[i]
                        i += 1
                    else:
                        i += 1
                else:
                    self.new_transport.append(temp)
                    temp = self.transport[i]
                    i += 1
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Mail_Item_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
    Dialog.getValue()
    Dialog.trans()
