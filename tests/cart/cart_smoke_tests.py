import unittest

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from helpers.operational_helpers import visibility_of_element_wait
from helpers.assertion_helpers import assert_page_title


class CartSmokeTests(unittest.TestCase):
    """A class containing sample smoke tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'
        cls.cart_url = 'http://automationpractice.com/index.php?controller=order'

    def test_if_cart_page_has_correct_name(self):
        expected_title = 'Order - My Store'
        assert_page_title(self, self.cart_url, expected_title)

    def test_cart_is_empty_after_entering_website(self):
        cart_button_xpath = '//div[@class="shopping_cart"]/a'
        empty_cart_alert_xpath = '//div[@id="center_column"]/p[contains(@class, "alert")]'
        product_table_xpath = '//table[@id="cart_summary"]'
        driver = self.driver
        driver.get(self.base_url)
        cart_button = driver.find_element(By.XPATH, cart_button_xpath)
        cart_button.click()
        empty_cart_alert = driver.find_element(By.XPATH, empty_cart_alert_xpath)
        try:
            driver.find_element(By.XPATH, product_table_xpath)
            raise Exception(f'Product table visible in empty cart for page {driver.current_url}')
        except NoSuchElementException:
            pass

        self.assertTrue(empty_cart_alert.text == 'Your shopping cart is empty.', f'Shoping cart isnt empty for page {driver.current_url} ')

    def test_product_is_visible_in_cart_after_being_added(self):
        product_name = 'Faded Short Sleeve T-shirts'
        t_shirts_button_xpath = '//div[@id="block_top_menu"]/ul/li/a[text()="T-shirts"]'
        product_exac_xpath = f'//ul[contains(@class, "product_list")]//a[@title="{product_name}" and @class="product-name"]'
        add_to_cart_button_xpath = '//ul[contains(@class, "product_list")]/li[1]//a[contains(@title, "Add to cart")]'
        proceed_button_xpath = '//div[@id="layer_cart"]//a[@title="Proceed to checkout"]'
        product_in_cart_xpath = f'//tr//a[text()="{product_name}"]'
        driver = self.driver
        driver.get(self.base_url)
        t_shirts_button = driver.find_element(By.XPATH, t_shirts_button_xpath)
        t_shirts_button.click()
        product = driver.find_element(By.XPATH, product_exac_xpath)
        action = ActionChains(driver)
        action.move_to_element(product).perform()
        add_to_cart_button = driver.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()
        proceed_button = visibility_of_element_wait(driver, proceed_button_xpath, 10)
        proceed_button.click()
        product_in_cart = driver.find_element(By.XPATH, product_in_cart_xpath)
        self.assertTrue(product_in_cart.is_displayed(), f'Product arent visible in cart for page {driver.current_url}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
