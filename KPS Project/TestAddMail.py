'''
@author: Nick
'''
import unittest
import Validation

class TestMail(unittest.TestCase):

    # Successfully added mail request
    def testUpdateCustomerPrice001(self):
        event = {"Origin": 3,"Destination": 2, "Weight": 1.00,"Volume": 2.00,"Priority": 2}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages          

    # Invalid format
    def testUpdateCustomerPrice002a(self):
        event = {"Origin": 'za',"Destination": 'az', "Weight": "2.0","Volume": "123","Priority": 'x'}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 5), errorMessages   
    
    # Values out of range
    def testUpdateCustomerPrice002b(self):
        event = {"Origin": 3,"Destination": 2, "Weight": 0,"Volume": 0,"Priority": 0}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 3), errorMessages 
        
    # Origin cannot equal destination
    def testUpdateCustomerPrice002c(self):
        event = {"Origin": 3,"Destination": 3, "Weight": 5.00,"Volume": 5.00,"Priority": 1}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1), errorMessages  

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAddMail))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())