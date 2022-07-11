import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from helpers.operational_helpers import visibility_of_element_wait
from helpers.assertion_helpers import assert_page_title


class CartSanityTests(unittest.TestCase):
    """A class containing sample smoke tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'
        cls.cart_url = 'http://automationpractice.com/index.php?controller=order'




    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
