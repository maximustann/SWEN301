'''
@author: Nick
'''
import unittest
import Validation

class TestDiscontinueTransportRoute(unittest.TestCase):

    # Successfully delete route
    def testDiscontinueTRoute001(self):
        event = {"Origin": 10,"Destination": 5, "Priority": 2, "Company": "Patrick Mumford Railways", "TransportType": "Air"}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 0),errorMessages     
        
    # Invalid format
    def testDiscontinueTRoute002a(self):
        event = {"Origin": 9,"Destination": 9, "Priority": "Team A", "Company": 7, "TransportType": 'z'}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 4),errorMessages    
        
    # Values out of range 
    def testDiscontinueTRoute002b(self):
        event = {"Origin": 5,"Destination": 6, "Priority": 3, "Company": "Air Balloon Rides", "TransportType": "Sea"}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1),errorMessages
        
    # Origin cannot equal destination
    def testUpdateCustomerPrice002c(self):
        event = {"Origin": 45,"Destination": 45, "Priority": 1, "Company": "Submarine Services", "TransportType": "Land"}
        errorMessages = Validation.validate(event)
        assert(len(errorMessages) == 1), errorMessages

    # Cannot access route database
    def testDiscontinueTRoute003(self):
        print("")
        
        

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestDiscontinueTransportRoute))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())