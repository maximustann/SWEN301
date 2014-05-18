# -*- coding: utf-8 -*-
"""
Created on Wed May 07 16:15:46 2014

@author: Patrick
"""
import sqlite3

TRANSPORTCOSTUPDATE = 1
CUSTOMERPRICEUPDATE = 2
TRANSPORTDISCONTINUED = 3
MAILDELIVERY = 4

CustomerDisplayRoutes = 'CustomerDisplayRoutes'
CustomerRoutes = 'CustomerRoutes'
TransportRoutes = 'TransportRoutes'
TransportDisplayRoutes = 'TransportDisplayRoutes'

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
    c.execute('SELECT priority FROM Priorities')
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
              (TRANSPORTCOSTUPDATE,cUD['Origin'], cUD['Destination'], float(cUD['PricePerGram']), float(cUD['PricePerCC']), cUD['Company'],
              cUD['TransportType'], cUD['DayOfWeek'], int(cUD['Frequency']), int(cUD['Duration'])))
    c.execute('''SELECT * FROM TransportRoutes 
        WHERE Origin = ? 
        AND Destination = ? 
        AND Company = ? 
        AND TransportType = ?
        AND DeliverDay = ?
        AND Frequency = ?
        AND Duration = ?  LIMIT 1''',(cUD['Origin'], cUD['Destination'], cUD['Company'], cUD['TransportType'],cUD['DayOfWeek'],int(cUD['Frequency']),int(cUD['Duration'])))
    if c.fetchone() != None:
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
            AND Duration=? ''',
            (float(cUD['PricePerGram']), float(cUD['PricePerCC']),
             cUD['Origin'], cUD['Destination'], cUD['Company'], cUD['TransportType'],cUD['DayOfWeek'],int(cUD['Frequency']),int(cUD['Duration'])))
    else:
         c.execute('''INSERT INTO TransportRoutes (Origin, Destination, PricePerGram, PricePerCC, Company, DeliverDay, TransportType, Duration, Frequency)
            VALUES (?,?,?,?,?,?,?,?,?)
            ''',
            (cUD['Origin'], cUD['Destination'], float(cUD['PricePerGram']), float(cUD['PricePerCC']), cUD['Company'], cUD['DayOfWeek'], cUD['TransportType'], int(cUD['Duration']), int(cUD['Frequency'])))
    conn.commit()
    conn.close()
    
def updateCustomerRoute(pUD):
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()  
    c.execute('''INSERT INTO BusinessEvents (EventTypeID, Origin, Destination, Priority, PricePerGram, PricePerCC) 
              VALUES (?,?,?,?,?,?)''',
              (CUSTOMERPRICEUPDATE,pUD['Origin'], pUD['Destination'], pUD['Priority'], float(pUD['PricePerGram']), float(pUD['PricePerCC'])))
    c.execute('''SELECT * FROM CustomerRoutes 
        WHERE Origin = ? 
        AND Destination = ? 
        AND Priority = ? LIMIT 1''',(pUD['Origin'], pUD['Destination'], pUD['Priority']))
    if c.fetchone() != None:
         c.execute('''UPDATE CustomerRoutes
            SET 
            PricePerGram = ?, 
            PricePerCC = ?
            WHERE Origin=? 
            AND Destination=? 
            AND Priority=?''',
            (float(pUD['PricePerGram']), float(pUD['PricePerCC']),pUD['Origin'], pUD['Destination'], pUD['Priority']))
    else:
        c.execute('''INSERT INTO CustomerRoutes (Origin, Destination, PricePerGram, PricePerCC, Priority)
            VALUES (?,?,?,?,?)
            ''',
            (pUD['Origin'], pUD['Destination'], float(pUD['PricePerGram']), float(pUD['PricePerCC']), pUD['Priority'])) 
    conn.commit()
    conn.close()
    
def getFilteredRoutes(table,fields,params):
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()  
    conn.text_factory = str
    queryString = '''SELECT '''
    if fields == None:
        queryString += '*'
    else:
        queryString += ",".join(fields)
    queryString+=' FROM %s '%table
    if params != None:
        queryString+='WHERE '
        stringFields = []
        for key in params: 
            stringFields.append(key + "=" + params[key])
        queryString += " AND ".join(stringFields)
    c.execute(queryString)
    routes = c.fetchall()
    conn.close()
    return routes


#getCustomerRoutes(dict(Origin=1))    