# -*- coding: utf-8 -*-
"""
Created on Wed May 07 20:20:51 2014

@author: Patrick
"""

import RouteCommandHandler as RH;
import Validation

TRANSPORTCOSTUPDATE = 1
CUSTOMERPRICEUPDATE = 2
TRANSPORTDISCONTINUED = 3
MAILDELIVERY = 4

def insertTransportCost(cUD): # Cost Update Data
    errorMessages = Validation.validate(cUD)
    if len(errorMessages) > 0:
        return errorMessages
    RH.updateTransportRoute(cUD)
    return errorMessages  

def updateCustomerPrice(pUD):
    errorMessages = Validation.validate(pUD)
    if len(errorMessages) > 0:
        return errorMessages
    RH.updateCustomerRoute(pUD)
    return errorMessages  

def discontinueTransport(dtT):
    errorMessages = Validation.validate(dtT)   
    if len(errorMessages) > 0:
        return errorMessages
    RH.discontinueRoute(dtT)
    return errorMessages    