'''
Created on 17/05/2014

@author: Nick
'''
import unittest
import BusinessEventHandler

class TestCustomerPriceUpdate(unittest.TestCase):

    # Successful transport cost update
    def testUpdateCustomerPrice001(self):
        cUD = BusinessEventHandler.PriceUpdateData("Japan","France", 1.20, 2.50,2)
        errorMessages = cUD.validate()
        assert(len(errorMessages) == 0),errorMessages       
        
    # Invalid data format
    def testUpdateCustomerPrice002(self):
        invalidData = [BusinessEventHandler.PriceUpdateData("Japan","Japan", 1.20, 2.50,2),
                       BusinessEventHandler.PriceUpdateData(1.95,"France", 1.20, 2.50,2),
                       BusinessEventHandler.PriceUpdateData("Japan", 6, 1.20, 2.50,2),
                       BusinessEventHandler.PriceUpdateData("Italy","France", 'a', 2.50,2),
                       BusinessEventHandler.PriceUpdateData("Japan","USA", 1.20, "abc",2),
                       BusinessEventHandler.PriceUpdateData("Canada","France", 1.20, 2.50,'a'),
                       BusinessEventHandler.PriceUpdateData("Canada","France", 1.20, 2.50, 0)]

        for data in invalidData:
            errorMessages = data.validate()
            assert(len(errorMessages) != 0), errorMessages   

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestCustomerPriceUpdate))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())