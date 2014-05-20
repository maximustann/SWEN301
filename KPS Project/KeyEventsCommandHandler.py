# -*- coding: utf-8 -*-
"""
Created on Sat May 17 15:08:42 2014

@author: Patrick
"""
import sqlite3

def getTotalRevenue():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT sum(costClient) FROM mail')
    total = c.fetchone()
    conn.close()
    return total
    
def getTotalExpenditure():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT sum(costKPS) FROM mail')
    total = c.fetchone()
    conn.close()
    return total
    
def getTotalNumberOfEvents():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT count(*) FROM BusinessEvents')
    total = c.fetchone()
    conn.close()
    return total
    
def getTotalMail():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('''SELECT origin, destination, sum(volume), sum(weight), count(*)
                    FROM mail
                    group by origin''')
    mails = c.fetchall()
    conn.close()
    return mails
    
def getAverageDeliveryTimes():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('''select origin, destination, priority, avg(DeliveryTime)
                from mail
                group by origin, destination, priority;''')
    times = c.fetchall()
    conn.close()
    return times



    
    