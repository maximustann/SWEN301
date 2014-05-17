'''
Created on 17/05/2014

@author: Nick
'''
import unittest
import login

class TestLogin(unittest.TestCase):

    # Successful login
    def testLogin001(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("Peter", "234567")
        assert(result == 1)
        
    # Invalid username
    def testLogin002(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("ASDFGHJK", "password")
        assert(result == 0 and self.actor_reason == 1)
        
    # Incorrect password
    def testLogin003(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("Peter", "password")
        assert(result == 0 and self.actor_reason == 0)
        
    # Username field empty
    def testLogin004(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("", "password")
        assert(result == 0 and self.actor_reason == 3)
        
    # Password field empty
    def testLogin005(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("username", "")
        assert(result == 0 and self.actor_reason == 4)
        
    # Username and password fields empty
    def testLogin006(self):
        user = login.login()
        user.conn()
        result, self.actor_reason = user.login("", "")
        assert(result == 0 and self.actor_reason == 2)

def suite():
    # combine the tests into a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestLogin))
    return test_suite

# run the test suite
runner=unittest.TextTestRunner()
runner.run(suite())