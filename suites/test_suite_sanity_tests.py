import unittest
from tests.cart.cart_sanity_tests import CartSanityTests
from tests.home_page.home_page_sanity_tests import HomePageSanityTests
from tests.user_account.user_account_sanity_tests import UserAccountSanityTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(CartSanityTests))
    test_suite.addTest(unittest.makeSuite(HomePageSanityTests))
    test_suite.addTest(unittest.makeSuite(UserAccountSanityTests))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())
