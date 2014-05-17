'''
Created on 17/05/2014

@author: Nick
'''
import unittest
import BusinessEventHandler

class TestTransportCostUpdate(unittest.TestCase):

    # Successful transport cost update
    def testUpdateTransportCost001(self):
        cUD = BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, "Nick McNeil Airways", "Air", "Sunday", 3, 2.0)
        errorMessages = cUD.validate()
        assert(len(errorMessages) == 0),errorMessages       
        
    # Invalid data format
    def testUpdateTransportCost002(self):
        invalidData = [BusinessEventHandler.TransportCostData("Auckland","Auckland", 1.20, 2.50, "Nick McNeil Airways", "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData(1,"Croatia", 1.20, 2.50, "Nick McNeil Airways", "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland", 5.0, 1.20, 2.50, "Nick McNeil Airways", "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", "abc", 2.50, "Nick McNeil Airways", "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 'd', "Nick McNeil Airways", "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, 123, "Air", "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, "Nick McNeil Airways", 4, "Sunday", 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, "Nick McNeil Airways", "Air", 123, 3, 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, "Nick McNeil Airways", "Air", 123, "def", 2.0),
                       BusinessEventHandler.TransportCostData("Auckland","Croatia", 1.20, 2.50, "Nick McNeil Airways", "Air", 123, 3, "ghi"),]

        for data in invalidData:
            errorMessages = data.validate()
            assert(len(errorMessages) != 0), errorMessages   


def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestTransportCostUpdate))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())