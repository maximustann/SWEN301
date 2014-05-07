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
    
    
def insertTransportCost(cUD): # Cost Update Data
    errorMessages = []
    print "inserting"
    errorMessages = errorMessages + cUD.validate()
    if len(errorMessages) > 0:
        return errorMessages
    conn = sqlite3.connect("Business.db")
    c = conn.cursor()
    c.execute('''INSERT INTO BusinessEvents (EventTypeID, Origin, Destination, PricePerGram, PricePerCC, Firm,
    TransportType, DayOfWeek, Frequency, Duration) VALUES (?,?,?,?,?,?,?,?,?,?)''',
              (TRANSPORTCOSTUPDATE,cUD.Origin, cUD.Destination, cUD.PricePerGram, cUD.PricePerCC, cUD.Firm,
              cUD.TransportType, cUD.DayOfWeek, cUD.Frequency, cUD.Duration))
    conn.commit()
    c.execute('select * from BusinessEvents')
    print c.fetchall()
    conn.close()
    return errorMessages
    
def createBusinessEventTable():
    conn = sqlite3.connect("Business.db")
    c = conn.cursor()
    c.execute('DROP TABLE BusinessEvents')
    c.execute('''CREATE TABLE BusinessEvents (
    ID INTEGER PRIMARY KEY NOT NULL,
    EventTypeID INT,
    Origin INT,
    Destination INT,
    Weight REAL,
    Volume REAL,
    TimeOfEntry DATETIME,
    Priority INT,
    PricePerGram REAL,
    PricePerCC REAL,
    Firm TEXT,
    TransportType TEXT,
    DayOfWeek INT,
    Frequency REAL,
    Duration REAL)''')
    
#createBusinessEventTable()    