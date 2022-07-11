import random
import string
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from helpers.functional_helpers import user_logout, user_login
from helpers.operational_helpers import visibility_of_element_wait, wait_for_elements


class UserAccountSanityTests(unittest.TestCase):
    """A class containing sample smoke tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'
        cls.login_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        cls.email_address = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15)) + '@o2.pl'
        cls.first_name = 'Jan'
        cls.last_name = 'Kowalski'
        cls.passwd = 'jkow20'
        cls.address_city = 'Krakow'
        cls.address_street = 'Woronicza'
        cls.state = 'Colorado'
        cls.zip_code = '30644'
        cls.country = 'United States'
        cls.mobile_phone = '344566788'
        cls.address_alias = 'Nothing Hill'

    def setUp(self) -> None:
        user_logout(self.driver)

    def test_user_can_create_new_account_with_required_data(self):
        email_create_input_field_xpath = '//input[@id="email_create"]'
        email_create_button_xpath = '//button[@id="SubmitCreate"]'
        # registration form elements
        form_gender_male_xpath = '//label[@for="id_gender1"]'
        input_firstname_xpath = '//input[@id="customer_firstname"]'
        input_lastname_xpath = '//input[@id="customer_lastname"]'
        input_email_xpath = '//input[@id="email"]'
        input_password_xpath = '//input[@id="passwd"]'
        input_address_firstname_xpath = '//input[@id="firstname"]'
        input_address_lastname_xpath = '//input[@id="lastname"]'
        input_address_address_xpath = '//input[@id="address1"]'
        input_address_city_xpath = '//input[@id="city"]'
        selector_address_state_xpath = '//select[@id="id_state"]'
        selector_address_state_options_xpath = '//select[@id="id_state"]/option' # should contains 54 options
        input_address_zip_xpath = '//input[@id="postcode"]'
        selector_address_country_xpath = '//select[@id="id_country"]'
        selector_address_country_options_xpath = '//select[@id="id_country"]/option'  # should contains 2 options
        input_address_mobile_phone_xpath = '//input[@id="phone_mobile"]'
        input_address_alias_xpath = '//input[@id="alias"]'
        button_submit_xpath = '//button[@id="submitAccount"]'
        # registration form elements end
        button_view_account_xpath = '//a[@title="View my customer account"]'

        driver = self.driver
        driver.get(self.login_url)
        email_create_input_field = visibility_of_element_wait(driver, email_create_input_field_xpath)
        email_create_input_field.send_keys(self.email_address)
        email_create_button = visibility_of_element_wait(driver, email_create_button_xpath)
        email_create_button.click()
        form_gender_male = visibility_of_element_wait(driver, form_gender_male_xpath, 10)
        form_gender_male.click()
        visibility_of_element_wait(driver, input_firstname_xpath).send_keys(self.first_name)
        visibility_of_element_wait(driver, input_lastname_xpath).send_keys(self.last_name)
        input_email = visibility_of_element_wait(driver, input_email_xpath)
        visibility_of_element_wait(driver, input_password_xpath).send_keys(self.passwd)
        input_address_firstname = visibility_of_element_wait(driver, input_address_firstname_xpath)
        input_address_lastname = visibility_of_element_wait(driver, input_address_lastname_xpath)
        visibility_of_element_wait(driver, input_address_address_xpath).send_keys(self.address_street)
        visibility_of_element_wait(driver, input_address_city_xpath).send_keys(self.address_city)
        form_state_selector = driver.find_element(By.XPATH, selector_address_state_xpath)
        form_state_selector_select = Select(form_state_selector)
        wait_for_elements(driver, selector_address_state_options_xpath, 5, 54)
        form_state_selector_select.select_by_visible_text(self.state)
        visibility_of_element_wait(driver, input_address_zip_xpath).send_keys(self.zip_code)
        form_country_selector = driver.find_element(By.XPATH, selector_address_country_xpath)
        form_country_selector_select = Select(form_country_selector)
        wait_for_elements(driver, selector_address_country_options_xpath, 5, 2)
        form_country_selector_select.select_by_visible_text(self.country)
        visibility_of_element_wait(driver, input_address_mobile_phone_xpath).send_keys(self.mobile_phone)
        input_address_alias = visibility_of_element_wait(driver, input_address_alias_xpath)
        input_address_alias.clear()
        input_address_alias.send_keys(self.address_alias)

        self.assertTrue(input_email.get_attribute('value') == self.email_address,
                        f'Wrong email address in registration form for page {driver.current_url}')
        self.assertTrue(input_address_firstname.get_attribute('value') == self.first_name,
                        f'Wrong firstname in registration form (address) for page {driver.current_url}')
        self.assertTrue(input_address_lastname.get_attribute('value') == self.last_name,
                        f'Wrong lastname in registration form (address) for page {driver.current_url}')

        visibility_of_element_wait(driver, button_submit_xpath).click()
        button_view_account = visibility_of_element_wait(driver, button_view_account_xpath)

        self.assertTrue(self.first_name in button_view_account.text and self.last_name in button_view_account.text,
                        f'Wrong user personal data after registration for page {driver.current_url}')

    def test_user_can_change_current_address_in_user_panel(self):
        user_email = 'po_test@xxx.pl'
        user_password = 'testtest'

        button_my_address_xpath = '//a[@title="Addresses"]'
        form_name_fields_xpath = '//ul[@class="last_item item box"]/li[2]'
        button_update_xpath = '//a[@title="Update"]'
        input_address_firstname_xpath = '//input[@id="firstname"]'
        input_address_lastname_xpath = '//input[@id="lastname"]'
        button_submit_xpath = '//button[@id="submitAddress"]'

        driver = self.driver
        user_login(driver, user_email, user_password)
        visibility_of_element_wait(driver, button_my_address_xpath).click()
        visibility_of_element_wait(driver, button_update_xpath).click()
        input_address_firstname = visibility_of_element_wait(driver, input_address_firstname_xpath)
        old_firstname = input_address_firstname.get_attribute('value')
        input_address_firstname.clear()
        input_address_firstname.send_keys(f'{old_firstname} Test')
        input_address_lastname = visibility_of_element_wait(driver, input_address_lastname_xpath)
        old_lastname = input_address_lastname.get_attribute('value')
        input_address_lastname.clear()
        input_address_lastname.send_keys(f'{old_lastname} Test')
        visibility_of_element_wait(driver, button_submit_xpath).click()
        names = visibility_of_element_wait(driver, form_name_fields_xpath)

        self.assertTrue(f'{old_firstname} Test' in names.text and f'{old_lastname} Test' in names.text)

        # restore previous data
        visibility_of_element_wait(driver, button_update_xpath).click()
        input_address_firstname = visibility_of_element_wait(driver, input_address_firstname_xpath)
        input_address_firstname.clear()
        input_address_firstname.send_keys(f'{old_firstname}')

        input_address_lastname = visibility_of_element_wait(driver, input_address_lastname_xpath)
        input_address_lastname.clear()
        input_address_lastname.send_keys(f'{old_lastname}')
        visibility_of_element_wait(driver, button_submit_xpath).click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
