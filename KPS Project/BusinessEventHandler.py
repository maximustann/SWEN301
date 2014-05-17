# -*- coding: utf-8 -*-
"""
Created on Wed May 07 20:20:51 2014

@author: Patrick
"""

import sqlite3

TRANSPORTCOSTUPDATE = 1
CUSTOMERPRICEUPDATE = 2
TRANSPORTDISCONTINUED = 3
MAILDELIVERY = 4

class TransportCostData(object):
    """ A class that just holds the transport cost data"""
    
    def __init__(self,Origin,Destination,PricePerGram,PricePerCC,Firm,TransportType,DayOfWeek,Frequency,Duration):
        self.Origin = Origin
        self.Destination = Destination
        self.PricePerGram = PricePerGram
        self.PricePerCC = PricePerCC
        self.Firm = Firm
        self.TransportType = TransportType
        self.DayOfWeek = DayOfWeek
        self.Frequency = Frequency
        self.Duration = Duration
                 
    def validate(self):
        return []
        
class PriceUpdateData(object):
    """ A class that just holds the customer price data"""
    
    def __init__(self,Origin,Destination,PricePerGram,PricePerCC,Priority):
        self.Origin = Origin
        self.Destination = Destination
        self.PricePerGram = PricePerGram
        self.PricePerCC = PricePerCC
        self.Priority = Priority
                 
    def validate(self):
        return []
    
def insertTransportCost(cUD): # Cost Update Data
    errorMessages = []
    print "inserting"
    errorMessages = errorMessages + cUD.validate()
    if len(errorMessages) > 0:
        return errorMessages
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()
    c.execute('''INSERT INTO BusinessEvents (EventTypeID, Origin, Destination, PricePerGram, PricePerCC, Company,
    TransportType, DayOfWeek, Frequency, Duration) VALUES (?,?,?,?,?,?,?,?,?,?)''',
              (TRANSPORTCOSTUPDATE,cUD.Origin, cUD.Destination, cUD.PricePerGram, cUD.PricePerCC, cUD.Firm,
              cUD.TransportType, cUD.DayOfWeek, cUD.Frequency, cUD.Duration))
    c.execute('''SELECT * FROM TransportRoutes''')    
    print c.fetchall()
    c.execute('''SELECT * FROM TransportRoutes 
        WHERE Origin = ? 
        AND Destination = ? 
        AND Company = ? 
        AND TransportType = ?
        AND DeliverDay = ?
        AND Frequency = ?
        AND Duration = ?''',(cUD.Origin, cUD.Destination, cUD.Firm, cUD.TransportType,cUD.DayOfWeek,cUD.Frequency,cUD.Duration))
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
                        AND Duration=?''',
                        (cUD.PricePerGram, cUD.PricePerCC,
                         cUD.Origin, cUD.Destination, cUD.Firm, cUD.TransportType,cUD.DayOfWeek,cUD.Frequency,cUD.Duration))
    else:
        c.execute('''INSERT INTO TransportRoutes (Origin, Destination, PricePerGram, PricePerCC, Company, TransportType, Duration, Frequency)
            VALUES (?,?,?,?,?,?,?,?)
            ''',
            (cUD.Origin, cUD.Destination, cUD.PricePerGram, cUD.PricePerCC, cUD.Firm, cUD.TransportType, cUD.Duration, cUD.Frequency))
    conn.commit()
    c.execute('select * from BusinessEvents')
    print c.fetchall()
    c.execute('select * from TransportRoutes')
    print c.fetchall()
    conn.close()
    return errorMessages  