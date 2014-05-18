'''
@author: Nick
'''
import unittest

def validate(eventDict):
    errorMessages = []
        
    if(eventDict.get("Origin") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Origin"))):
            errorMessages.append("Origin not in int format");
            
        # origin cannot be equal to destination   
        if(eventDict.get("Destination")==eventDict.get("Origin")):
            errorMessages.append("Origin cannot be equal to destination");
           
    if(eventDict.get("Destination") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Destination"))):
            errorMessages.append("Destination not in int format");
           
    if(eventDict.get("Weight") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Weight"))):
            errorMessages.append("Weight not in real format");
            
        # check greater than zero
        if not(eventDict.get("Weight") > 0):
            errorMessages.append("Weight must be greater than zero");

    if(eventDict.get("Volume") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Volume"))):
            errorMessages.append("Volume not in real format");
            
        # check greater than zero
        if not(eventDict.get("Volume") > 0):
            errorMessages.append("Volume must be greater than zero");
           
    if(eventDict.get("TimeOfEntry") != None):
        # check correct format
        if not (isinstance(eventDict.get("TimeOfEntry"), int)):
            errorMessages.append("TimeOfEntry not in int format");
           
    if(eventDict.get("Priority") != None):
        # check correct format
        if not (isinstance(eventDict.get("Priority"), int)):
            errorMessages.append("Priority not in int format");   
        # check priority either 1 or 2
        elif(eventDict.get("Priority") != 1 and eventDict.get("Priority") != 2):
            errorMessages.append("Priority must be either 1 or 2");
           
    if(eventDict.get("PricePerGram") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("PricePerGram"))):
            errorMessages.append("PricePerGram not in real format");
        # check greater than zero
        elif not(eventDict.get("PricePerGram") > 0):
            errorMessages.append("PricePerGram must be greater than zero");
           
    if(eventDict.get("PricePerCC") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("PricePerCC"))):
            errorMessages.append("PricePerCC not in real format");
        # check greater than zero
        elif not(eventDict.get("PricePerCC") > 0):
            errorMessages.append("PricePerCC must be greater than zero");
           
    if(eventDict.get("Firm") != None):
        # check correct format
        if not (isinstance(eventDict.get("Firm"), str)):
            errorMessages.append("Firm not in string format");
           
    if(eventDict.get("TransportType") != None):
        # check correct format
        if not (isinstance(eventDict.get("TransportType"), str)):
            errorMessages.append("TransportType not in string format");
        
        elif not(eventDict.get("TransportType") != "Air" or eventDict.get("TransportType") != "Land" or eventDict.get("TransportType") != "Sea"):
            errorMessages.append("TransportType must be either Air, Land, or Sea")
           
    if(eventDict.get("DayOfWeek") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("DayOfWeek"))):
            errorMessages.append("DayOfWeek not in int format");
        # day of the week must be between 1 and 7
        elif (eventDict.get("DayOfWeek")>7 or eventDict.get("DayOfWeek")<1):
            errorMessages.append("DayOfWeek must be between 1 and 7. Actual output: " + str(eventDict.get("DayOfWeek")))
             
    if(eventDict.get("Frequency") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Frequency"))):
            errorMessages.append("Frequency not in real format");
        elif not (eventDict.get("Frequency")>0):
            errorMessages.append("Frequency must be greater than 0");
           
    if(eventDict.get("Duration") != None):
        # check correct format
        if not (Validation.valueToFloat(eventDict.get("Duration"))):
            errorMessages.append("Duration not in real format");    
        # check greater than zero
        elif not(eventDict.get("Duration") > 0):
            errorMessages.append("Duration must be greater than zero");
           
    return errorMessages

def valueToFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False