import time
import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from helpers.operational_helpers import visibility_of_element_wait, wait_for_expected_element_value
from helpers.functional_helpers import user_login, remove_all_products_from_cart


class CartSanityTests(unittest.TestCase):
    """A class containing sample sanity tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'
        cls.cart_url = 'http://automationpractice.com/index.php?controller=order'

    def setUp(self) -> None:
        remove_all_products_from_cart(self.driver)

    def test_product_added_before_user_signin_is_visible_in_cart_view_after_user_signin(self):
        user_email = 'po_test@xxx.pl'
        user_password = 'testtest'
        product_name = 'Printed Chiffon Dress'
        cart_button_xpath = '//div[@class="shopping_cart"]/a'
        product_image_xpath = f'//div[@class="cart_block_list"]//img[@alt="{product_name}"]'
        dresses_button_xpath = '//div[@id="block_top_menu"]/ul/li/a[text()="Dresses"]'
        product_exac_xpath = f'//ul[contains(@class, "product_list")]//a[@title="{product_name}" and @class="product-name"]'
        add_to_cart_button_xpath = '//ul[contains(@class, "product_list")]/li[5]//a[contains(@title, "Add to cart")]'
        proceed_button_xpath = '//div[@id="layer_cart"]//a[@title="Proceed to checkout"]'
        product_in_cart_xpath = f'//tr//a[text()="{product_name}"]'

        driver = self.driver
        driver.get(self.base_url)
        t_shirts_button = visibility_of_element_wait(driver, dresses_button_xpath)
        t_shirts_button.click()
        product = visibility_of_element_wait(driver, product_exac_xpath)
        action = ActionChains(driver)
        action.move_to_element(product).perform()
        add_to_cart_button = visibility_of_element_wait(driver, add_to_cart_button_xpath)
        add_to_cart_button.click()
        proceed_button = visibility_of_element_wait(driver, proceed_button_xpath, 10)
        proceed_button.click()
        product_in_cart = visibility_of_element_wait(driver, product_in_cart_xpath)

        self.assertTrue(product_in_cart.is_displayed(), f'Product arent visible in cart for page {driver.current_url}')
        user_login(driver, user_email, user_password)

        action = ActionChains(driver)
        cart_button = visibility_of_element_wait(driver, cart_button_xpath)
        action.move_to_element(cart_button).perform()
        product_image = visibility_of_element_wait(driver, product_image_xpath)
        self.assertTrue(product_image.get_attribute('alt') == product_name)

    def test_user_can_rise_product_number_in_cart_from_1_to_2(self):
        product_name = 'Printed Chiffon Dress'
        quantity_field_xpath = '//td[contains(@class,"cart_quantity")]/input[@type="text"]'
        quantity_rise_xpath = '//a[contains(@id,"cart_quantity_up")]'
        dresses_button_xpath = '//div[@id="block_top_menu"]/ul/li/a[text()="Dresses"]'
        product_exac_xpath = f'//ul[contains(@class, "product_list")]//a[@title="{product_name}" and @class="product-name"]'
        add_to_cart_button_xpath = '//ul[contains(@class, "product_list")]/li[5]//a[contains(@title, "Add to cart")]'
        proceed_button_xpath = '//div[@id="layer_cart"]//a[@title="Proceed to checkout"]'

        driver = self.driver
        driver.get(self.base_url)
        t_shirts_button = visibility_of_element_wait(driver, dresses_button_xpath)
        t_shirts_button.click()
        product = visibility_of_element_wait(driver, product_exac_xpath)
        action = ActionChains(driver)
        action.move_to_element(product).perform()
        add_to_cart_button = visibility_of_element_wait(driver, add_to_cart_button_xpath)
        add_to_cart_button.click()
        proceed_button = visibility_of_element_wait(driver, proceed_button_xpath, 10)
        proceed_button.click()
        product_quantity = visibility_of_element_wait(driver, quantity_field_xpath).get_attribute('value')
        self.assertTrue(int(product_quantity) == 1)
        visibility_of_element_wait(driver, quantity_rise_xpath).click()

        product_quantity = wait_for_expected_element_value(driver, quantity_field_xpath, '2')
        self.assertTrue(int(product_quantity) == 2)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
