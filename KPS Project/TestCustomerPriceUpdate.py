'''
@author: Nick
'''
import unittest
import Validation

class TestCustomerPriceUpdate(unittest.TestCase):

    # Successful transport cost update
    def testUpdateCustomerPrice001(self):
        event = {"Origin": 1,"Destination": 2, "Priority": 2,"PricePerGram": 5,"PricePerCC": 4, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 6, "Frequency": 54,"Duration": 3}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages          

    # Invalid format
    def testUpdateCustomerPrice002a(self):
        event = {"Origin":"abc","Destination": "def", "Priority": "ghi","PricePerGram": "jkl","PricePerCC": "mno", "Company": 7,
                 "TransportType": 1,"DayOfWeek": "pqr", "Frequency": "stu","Duration": "vwx"}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 10), errorMessages   
    
    # Values out of range
    def testUpdateCustomerPrice002b(self):
        event = {"Origin": 3,"Destination": 4, "Priority": 8,"PricePerGram": 0,"PricePerCC": -4.60, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 8, "Frequency": 0,"Duration": -10}
        
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 6), errorMessages 
        
    # Origin cannot equal destination
    def testUpdateCustomerPrice002c(self):
        event = {"Origin": 5,"Destination": 5, "Priority": 2,"PricePerGram": 5,"PricePerCC": 4, "Company": "Nick McNeil Airways",
                 "TransportType": "Air","DayOfWeek": 6, "Frequency": 54,"Duration": 3}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1), errorMessages  

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCustomerPriceUpdate))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())