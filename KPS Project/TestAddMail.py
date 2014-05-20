'''
@author: Nick
'''
import unittest
import Validation

class TestAddMail(unittest.TestCase):

    # Successfully added mail request
    def testAddMail001(self):
        event = {"Origin": 3,"Destination": 2, "Weight": 1.00,"Volume": 2.00,"Priority": 2}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages          

    # Invalid format
    def testAddMail002a(self):
        event = {"Origin": 'za',"Destination": 'az', "Weight": "_ab_","Volume": "1a2b3c","Priority": 'x'}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 5), errorMessages   
    
    # Values out of range
    def testAddMail002b(self):
        event = {"Origin": 3,"Destination": 2, "Weight": 0,"Volume": 0,"Priority": 0}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 3), errorMessages 
        
    # Origin cannot equal destination
    def testAddMail002c(self):
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