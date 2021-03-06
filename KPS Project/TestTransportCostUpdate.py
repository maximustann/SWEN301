'''
Created on 17/05/2014

@author: Nick
'''
import unittest
import Validation

class TestTransportCostUpdate(unittest.TestCase):

    # Successfully updated transport cost
    def testTransportCostUpdate001(self):
        event = {"Origin": 1,"Destination": 2, "Priority": 2,"PricePerGram": 5,"PricePerCC": 4, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 6, "Frequency": 54,"Duration": 3}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages            
        
    # Invalid format
    def testTransportCostUpdate002a(self):
        event = {"Origin":"abc","Destination": "def", "Priority": "ghi","PricePerGram": "jkl","PricePerCC": "mno", "Company": 7,
                 "TransportType": 1,"DayOfWeek": "pqr", "Frequency": "stu","Duration": "vwx"}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 10), errorMessages   
    
    # Values out of range
    def testTransportCostUpdate002b(self):
        event = {"Origin": 3,"Destination": 4, "Priority": 8,"PricePerGram": 0,"PricePerCC": -4.60, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 8, "Frequency": 0,"Duration": -10}
        
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 6), errorMessages 
        
    # Origin cannot equal destination
    def testTransportCostUpdate002c(self):
        event = {"Origin": 5,"Destination": 5, "Priority": 2,"PricePerGram": 5,"PricePerCC": 4, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 6, "Frequency": 54,"Duration": 3}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1), errorMessages  
        
    # Cannot access route database
    def testTransportCostUpdate003(self):
        print("")


def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTransportCostUpdate))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())