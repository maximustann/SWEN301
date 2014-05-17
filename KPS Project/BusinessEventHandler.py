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
        errorMessages = []
        
        if not (isinstance(self.Origin, str)):
            errorMessages.append("Origin not in string format");
            
        if not (isinstance(self.Destination, str)):
            errorMessages.append("Destination not in string format");
            
        if not (isinstance(self.PricePerGram, float)):
            errorMessages.append("PricePerGram not in float format");
            
        if not (isinstance(self.PricePerCC, float)):
            errorMessages.append("PricePerCC not in float format");
            
        if not (isinstance(self.Firm, str)):
            errorMessages.append("Firm not in string format");
            
        if not (isinstance(self.TransportType, str)):
            errorMessages.append("TransportType not in string format");
            
        if not (isinstance(self.DayOfWeek, str)):
            errorMessages.append("DayOfWeek not in string format");
            
        if not (isinstance(self.Frequency, int)):
            errorMessages.append("Frequency not in integer format");
            
        if not (isinstance(self.Duration, float)):
            errorMessages.append("Duration not in float format");    
            
        if (isinstance(self.Frequency, int) and self.Frequency < 0):
            errorMessages.append("Frequency cannot be less than zero");    
            
        if (isinstance(self.Duration, float) and self.Duration <= 0):
            errorMessages.append("Duration cannot be less than or equal to zero");  
            
        if (isinstance(self.PricePerGram, float) and self.PricePerGram < 0):
            errorMessages.append("PricePerGram cannot be less than zero");  
            
        if (isinstance(self.PricePerCC, float) and self.PricePerCC < 0):
            errorMessages.append("PricePerCC cannot be less than zero"); 
            
        if (self.Origin == self.Destination):
            errorMessages.append("The Origin and Destination cannot be the same"); 
                
        return errorMessages
        
class PriceUpdateData(object):
    """ A class that just holds the customer price data"""
    
    def __init__(self,Origin,Destination,PricePerGram,PricePerCC,Priority):
        self.Origin = Origin
        self.Destination = Destination
        self.PricePerGram = PricePerGram
        self.PricePerCC = PricePerCC
        self.Priority = Priority
                 
    def validate(self):
        errorMessages = []
        
        if not (isinstance(self.Origin, str)):
            errorMessages.append("Origin not in string format");
            
        if not (isinstance(self.Destination, str)):
            errorMessages.append("Destination not in string format");
            
        if not (isinstance(self.PricePerGram, float)):
            errorMessages.append("PricePerGram not in float format");
            
        if not (isinstance(self.PricePerCC, float)):
            errorMessages.append("PricePerCC not in float format");

        if(self.Priority != 1 and self.Priority != 2):
            errorMessages.append("Priority must be either 1 or 2");
            
        if (isinstance(self.PricePerGram, float) and self.PricePerGram < 0):
            errorMessages.append("PricePerGram cannot be less than zero");  
            
        if (isinstance(self.PricePerCC, float) and self.PricePerCC < 0):
            errorMessages.append("PricePerCC cannot be less than zero"); 
            
        if (self.Origin == self.Destination):
            errorMessages.append("The Origin and Destination cannot be the same"); 
                
        return errorMessages
        
    
def insertTransportCost(cUD): # Cost Update Data
    errorMessages = []
    print ("inserting")
    errorMessages = errorMessages + cUD.validate()
    if len(errorMessages) > 0:
        return errorMessages
    conn = sqlite3.connect("../Database/Business.db")
    c = conn.cursor()
    print (cUD.DayOfWeek)
    print
    print
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
         print ('Holla')
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
        print (c.fetchone())
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
    return errorMessages  