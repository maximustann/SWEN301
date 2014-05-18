# -*- coding: utf-8 -*-
"""
Created on Wed May 07 20:20:51 2014

@author: Patrick
"""

import sqlite3
import RouteCommandHandler as RH;

TRANSPORTCOSTUPDATE = 1
CUSTOMERPRICEUPDATE = 2
TRANSPORTDISCONTINUED = 3
MAILDELIVERY = 4

def insertTransportCost(cUD): # Cost Update Data
    errorMessages = []
  #  errorMessages = errorMessages + cUD.validate()
    if len(errorMessages) > 0:
        return errorMessages
    RH.updateTransportRoute(cUD)
    return errorMessages  

def updateCustomerPrice(pUD):
    errorMessages = []
  #  errorMessages = errorMessages + pUD.validate()
    if len(errorMessages) > 0:
        return errorMessages
    RH.updateCustomerRoute(pUD)
    return errorMessages  