# -*- coding: utf-8 -*-
"""
Created on Wed May 07 16:15:46 2014

@author: Patrick
"""
import sqlite3

def getLocations():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT name FROM cities')
    locs = [r[0] for r in c.fetchall()]
    conn.close()
    return locs
    
def insertLocations():
    # Only do this once. This method should otherwise never be used
    f = open('locations.txt','r')
    locations = []
    for line in f:
        locations.append((None,line.strip('\n')))
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()
    c.executemany('INSERT INTO Cities VALUES (?,?)',locations)
    conn.commit()
    conn.close()
    
def getPriorities():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT name FROM cities')
    locs = [r[0] for r in c.fetchall()]
    conn.close()
    return locs
    
def getTransportTypes():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT type FROM TransportTypes')
    locs = [r[0] for r in c.fetchall()]
    conn.close()
    return locs

def getDaysOfWeek():
    conn = sqlite3.connect("../Database/Business.db")
    conn.text_factory = str
    c = conn.cursor()
    c.execute('SELECT day FROM DaysOfWeek')
    locs = [r[0] for r in c.fetchall()]
    conn.close()
    return locs

def updateTransportRoute(cUD):
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()
    c.execute('''INSERT INTO BusinessEvents (EventTypeID, Origin, Destination, PricePerGram, PricePerCC, Company,
    TransportType, DayOfWeek, Frequency, Duration) VALUES (?,?,?,?,?,?,?,?,?,?)''',
              (TRANSPORTCOSTUPDATE,cUD.Origin, cUD.Destination, cUD.PricePerGram, cUD.PricePerCC, cUD.Firm,
              cUD.TransportType, cUD.DayOfWeek, cUD.Frequency, cUD.Duration))
    c.execute('''SELECT * FROM TransportRoutes 
        WHERE Origin = ? 
        AND Destination = ? 
        AND Company = ? 
        AND TransportType = ?
        AND DeliverDay = ?
        AND Frequency = ?
        AND Duration = ?''',(cUD.Origin, cUD.Destination, cUD.Firm, cUD.TransportType,cUD.DayOfWeek,cUD.Frequency,cUD.Duration))
    if c.fetchone() != None:
         print 'Holla'
         c.execute('''UPDATE TransportRoutes
            SET 
            PricePerGram = ? 
            AND PricePerCC = ?
            WHERE Origin=? 
            AND Destination=? 
            AND Company=? 
            AND TransportType=?
            AND DeliverDay=?
            AND Frequency=?
            AND Duration=?''',
            (cUD.PricePerGram, cUD.PricePerCC,
             cUD.Origin, cUD.Destination, cUD.Firm, cUD.TransportType,cUD.DayOfWeek,cUD.Frequency,cUD.Duration))
    else:
        print c.fetchone()
        c.execute('''INSERT INTO TransportRoutes (Origin, Destination, PricePerGram, PricePerCC, Company, DeliverDay, TransportType, Duration, Frequency)
            VALUES (?,?,?,?,?,?,?,?,?)
            ''',
            (cUD.Origin, cUD.Destination, cUD.PricePerGram, cUD.PricePerCC, cUD.Firm, cUD.DayOfWeek, cUD.TransportType, cUD.Duration, cUD.Frequency))
    conn.commit()
    #c.execute('select * from BusinessEvents')
    #print c.fetchall()
    c.execute('select * from TransportRoutes')
    #print c.fetchall()
    conn.close()
    
def updateCustomerRoute(pUD):
     conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()  

    conn.close()