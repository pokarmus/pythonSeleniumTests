import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from helpers.assertion_helpers import assert_page_title
from helpers.functional_helpers import user_login


class UserAccountSmokeTests(unittest.TestCase):
    """A class containing sample smoke tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'
        cls.login_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

    def test_if_user_page_has_correct_name(self):
        expected_title = 'Login - My Store'
        assert_page_title(self, self.login_url, expected_title)

    def test_registration_and_login_form_are_displayed_when_user_is_not_logged_in(self):
        create_account_form_xpath = '//form[@id="create-account_form"]'
        login_form_xpath = '//form[@id="login_form"]'
        driver = self.driver
        driver.get(self.login_url)
        create_account_form = driver.find_element(By.XPATH, create_account_form_xpath)
        login_form = driver.find_element(By.XPATH, login_form_xpath)
        self.assertTrue(create_account_form.is_displayed(), f'No registration form displayed for page {driver.current_url}')
        self.assertTrue(login_form.is_displayed(), f'No login form displayed for page {driver.current_url}')

    def test_no_user_is_logged_in_after_entering_website(self):
        sign_in_button_xpath = '//a[@class="login"]'
        driver = self.driver
        driver.get(self.base_url)
        sign_in_button = driver.find_element(By.XPATH, sign_in_button_xpath)
        self.assertTrue(sign_in_button.text == 'Sign in')

    def test_user_can_log_in_with_correct_user_and_password(self):
        user_email = 'po_test@xxx.pl'
        user_password = 'testtest'
        user_name = 'Test Test'
        user_name_field_xpath = '//a[@title="View my customer account"]'
        user_personal_information_button_xpath = '//i[@class="icon-user"]/../span'
        driver = self.driver
        user_login(driver, user_email, user_password)
        user_name_field = driver.find_element(By.XPATH, user_name_field_xpath)
        user_personal_information_button = driver.find_element(By.XPATH, user_personal_information_button_xpath)
        self.assertTrue(user_name_field.text == user_name
                        and str.upper(user_personal_information_button.text) == str.upper('My personal information'),
                        f'Cant login with correct user/password for page {driver.current_url}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
