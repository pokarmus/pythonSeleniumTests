import unittest
from tests.cart.cart_smoke_tests import CartSmokeTests
from tests.home_page.home_page_smoke_tests import HomePageSmokeTests
from tests.user_account.user_account_smoke_tests import UserAccountSmokeTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(CartSmokeTests))
    test_suite.addTest(unittest.makeSuite(HomePageSmokeTests))
    test_suite.addTest(unittest.makeSuite(UserAccountSmokeTests))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())
