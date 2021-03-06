'''
@author: Nick
'''
import unittest
import Validation

class TestCustomerPriceUpdate(unittest.TestCase):

    # Successful updated customer price
    def testUpdateCustomerPrice001(self):
        event = {"Origin": 4,"Destination": 9, "Priority": 1,"PricePerGram": 10.50,"PricePerCC": 12.60}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages          

    # Invalid format
    def testUpdateCustomerPrice002a(self):
        event = {"Origin": 'z',"Destination": 'a', "Priority": "a","PricePerGram": "abc","PricePerCC": "def"}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 5), errorMessages   
    
    # Values out of range
    def testUpdateCustomerPrice002b(self):
        event = {"Origin": 12,"Destination": 56, "Priority": 0,"PricePerGram": -2.50,"PricePerCC": -1.00}
        
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 3), errorMessages 
        
    # Origin cannot equal destination
    def testUpdateCustomerPrice002c(self):
        event = {"Origin": 10,"Destination": 10, "Priority": 1,"PricePerGram": 6.25,"PricePerCC": 4.23}

        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1), errorMessages  
        
    # Cannot access route database
    def testUpdateCustomerPrice003(self):
        print("")

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCustomerPriceUpdate))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())