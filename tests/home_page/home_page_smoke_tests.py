import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from helpers.assertion_helpers import assert_page_title


class SmokeTests(unittest.TestCase):
    """A class containing sample smoke tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'

    def test_if_main_page_title_is_correct(self):
        expected_title = 'My Store'
        assert_page_title(self, self.base_url, expected_title)

    def test_headers_banner_is_visible(self):
        baner_xpath = '//header[@id="header"]//img[@class="img-responsive"]'
        driver = self.driver
        driver.get(self.base_url)
        banner = driver.find_element(By.XPATH, baner_xpath)
        self.assertTrue(banner.is_displayed(), f'Header banner not visible for url {driver.current_url}')

    def test_shop_logo_is_visible(self):
        logo_xpath = '//div[@id="header_logo"]//img[contains(@class, "logo")]'
        driver = self.driver
        driver.get(self.base_url)
        logo = driver.find_element(By.XPATH, logo_xpath)
        self.assertTrue(logo.is_displayed(), f'Logo not visible for url {driver.current_url}')

    def test_home_page_slider_contains_exact_elements_number(self):
        slider_elements_xpath = '//ul[@id="homeslider"]/li'
        elements_number = 5
        driver = self.driver
        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slider_elements_xpath)
        self.assertTrue(len(slider_elements) == elements_number, f'Page slider contains different number of elements '
                                                                 f'that expected for url {driver.current_url}')

    def test_home_page_contains_recommended_product_list_with_exact_elements_number(self):
        product_list_xpath = '//ul[@id="homefeatured"]/li'
        products_number = 7
        driver = self.driver
        driver.get(self.base_url)
        product_list = driver.find_elements(By.XPATH, product_list_xpath)
        counter = 0
        for product in product_list:
            if product.is_displayed():
                counter += 1
        self.assertTrue(counter == products_number, f'Page contains different number of recommended products that '
                                                    f'expected for url {driver.current_url}')

    def test_bottom_content_list_is_visible_and_contains_exact_product_number(self):
        list_xpath = '//div[@id="htmlcontent_home"]//li'
        elements_number = 5
        driver = self.driver
        driver.get(self.base_url)
        list = driver.find_elements(By.XPATH, list_xpath)
        counter = 0
        for element in list:
            if element.is_displayed():
                counter += 1
        self.assertTrue(counter == elements_number, f'Page contains different number of bottom elements that expected '
                                                    f'for url {driver.current_url}')

    def test_searching_engine_return_results(self):
        searchbar_xpath = '//input[@id="search_query_top"]'
        search_result_list_xpath = '//div[@id="center_column"]/ul/li'
        driver = self.driver
        driver.get(self.base_url)
        searchbar = driver.find_element(By.XPATH, searchbar_xpath)
        searchbar.send_keys('dress')
        searchbar.send_keys(Keys.RETURN)
        search_result_list = driver.find_elements(By.XPATH, search_result_list_xpath)
        self.assertTrue(len(search_result_list) > 0, f'Search engine did not return any results for page '
                                                     f'{driver.current_url}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
