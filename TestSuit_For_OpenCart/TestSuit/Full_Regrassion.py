import unittest

from TestSuit_For_OpenCart.Login.test_login import login
from TestSuit_For_OpenCart.Registration.test_Registration import Registration
from TestSuit_For_OpenCart.AddToCart.test_AddToCart import Addtocart

login_test = unittest.TestLoader().loadTestsFromTestCase(login)
registration_test  =unittest.TestLoader().loadTestsFromTestCase(Registration)
AddToCart_test = unittest.TestLoader().loadTestsFromTestCase(Addtocart)

regression = unittest.TestSuite([login_test,registration_test,AddToCart_test])
unittest.TextTestRunner(verbosity=2).run(regression)