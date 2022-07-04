import string
import time
import unittest
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from helpers.operational_helpers import visibility_of_element_wait


class HomePageSanityTests(unittest.TestCase):
    """A class containing sample sanity tests for the site http://automationpractice.com/ """

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        service = Service(r'C:\TestFiles\chromedriver_101.exe')
        cls.driver = WebDriver(service=service)
        cls.base_url = 'http://automationpractice.com/'

    def test_home_page_slider_images_have_correct_size_on_half_hd_screen(self):
        img_expected_width_half_screen = 480
        img_expected_height_half_screen = 276
        slider_images_xpath = '//ul[@id="homeslider"]/li/a/img'
        driver = self.driver
        driver.set_window_size(950, 1000)
        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slider_images_xpath)
        for element in slider_elements:
            self.assertTrue(int(element.get_attribute('width')) == img_expected_width_half_screen,
                            f'Img size differ that expected for page {driver.current_url}')
            self.assertTrue(int(element.get_attribute('height')) == img_expected_height_half_screen,
                            f'Img size differ that expected for page {driver.current_url}')

    def test_home_page_slider_images_have_correct_size_on_full_hd_screen(self):
        img_expected_width_full_screen = 779
        img_expected_height_full_screen = 448
        slider_images_xpath = '//ul[@id="homeslider"]/li/a/img'
        driver = self.driver
        driver.set_window_size(1900, 1000)
        driver.get(self.base_url)
        slider_elements = driver.find_elements(By.XPATH, slider_images_xpath)
        for element in slider_elements:
            self.assertTrue(int(element.get_attribute('width')) == img_expected_width_full_screen,
                            f'Img size differ that expected for page {driver.current_url}')
            self.assertTrue(int(element.get_attribute('height')) == img_expected_height_full_screen,
                            f'Img size differ that expected for page {driver.current_url}')

    def test_home_page_slider_have_correct_size_on_half_hd_screen(self):
        expected_width_half_screen = 480
        expected_height_half_screen = 276
        slider_xpath = '//div[@id="homepage-slider"]/div[@class="bx-wrapper"]'
        driver = self.driver
        driver.set_window_size(950, 1000)
        driver.get(self.base_url)
        slider = driver.find_element(By.XPATH, slider_xpath)
        self.assertTrue(int(slider.get_attribute('clientWidth')) == expected_width_half_screen,
                        f'Slider size differ that expected for page {driver.current_url}')
        self.assertTrue(int(slider.get_attribute('clientHeight')) == expected_height_half_screen,
                        f'Slider size differ that expected for page {driver.current_url}')

    def test_home_page_slider_have_correct_size_on_full_hd_screen(self):
        expected_width_full_screen = 779
        expected_height_full_screen = 448
        slider_xpath = '//ul[@id="homeslider"]/li/a/img'
        driver = self.driver
        driver.set_window_size(1900, 1000)
        driver.get(self.base_url)
        slider = driver.find_element(By.XPATH, slider_xpath)
        self.assertTrue(int(slider.get_attribute('clientWidth')) == expected_width_full_screen,
                        f'Slider size differ that expected for page {driver.current_url}')
        self.assertTrue(int(slider.get_attribute('clientHeight')) == expected_height_full_screen,
                        f'Slider size differ that expected for page {driver.current_url}')

    def test_home_page_slider_change_elements_after_page_open(self):
        slider_xpath = '//ul[@id="homeslider"]'
        driver = self.driver
        driver.get(self.base_url)
        slider = driver.find_element(By.XPATH, slider_xpath)
        start_pos = slider.get_attribute('offsetLeft')
        time.sleep(4)
        end_pos = slider.get_attribute('offsetLeft')
        self.assertFalse(start_pos == end_pos, f'Slider elements do not change for page {driver.current_url}')

    def test_home_page_slider_stop_change_elements_when_next_button_clicked(self):
        slider_xpath = '//ul[@id="homeslider"]'
        slider_next_button_xpath = '//div[@id="homepage-slider"]//a[@class="bx-next"]'
        driver = self.driver
        driver.get(self.base_url)
        slider = driver.find_element(By.XPATH, slider_xpath)
        slider_next_button = driver.find_element(By.XPATH, slider_next_button_xpath)
        slider_next_button.click()
        time.sleep(1)
        start_pos = slider.get_attribute('offsetLeft')
        time.sleep(4)
        end_pos = slider.get_attribute('offsetLeft')
        self.assertTrue(start_pos == end_pos, f'Next button does not stop elements change for page '
                                              f'{driver.current_url}')

    def test_home_page_slider_stop_change_elements_when_cursor_over_slider(self):
        mouseover_slider_xpath = '//div[@id="homepage-slider"]'
        slider_xpath = '//ul[@id="homeslider"]'
        driver = self.driver
        driver.get(self.base_url)
        mouseover_slider = driver.find_element(By.XPATH, mouseover_slider_xpath)
        slider = driver.find_element(By.XPATH, slider_xpath)
        action = ActionChains(driver)
        action.move_to_element(mouseover_slider).perform()
        time.sleep(1)
        start_pos = slider.get_attribute('offsetLeft')
        time.sleep(4)
        end_pos = slider.get_attribute('offsetLeft')
        self.assertTrue(start_pos == end_pos, f'Mouseover does not stop elements change for page {driver.current_url}')

    def test_top_trends_tile_redirects_to_prestashop_url(self):
        redirect_link = 'http://www.prestashop.com/'
        redirect_url = 'https://www.prestashop.com/pl'
        tile_xpath = '//div[@id="htmlcontent_home"]/ul/li[1]'
        driver = self.driver
        driver.get(self.base_url)
        tile = driver.find_element(By.XPATH, tile_xpath)
        tile_url = tile.find_element(By.XPATH, 'a')
        self.assertTrue(tile_url.get_attribute('href') == redirect_link, f'Wrong tile url for page '
                                                                         f'{driver.current_url}')
        tile.click()
        self.assertTrue(driver.current_url == redirect_url, f'Wrong tile url for page {driver.current_url}')

    def test_user_can_subscribe_newsletter(self):
        success_alert_text = 'Newsletter : You have successfully subscribed to this newsletter.'
        newsletter_mail_input_xpath = '//input[@id="newsletter-input"]'
        newsletter_input_button_xpath = '//button[@name="submitNewsletter"]'
        success_alert_xpath = '//p[@class="alert alert-success"]'
        email_address = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15)) + '@o2.pl'
        driver = self.driver
        driver.get(self.base_url)
        newsletter_mail_input = driver.find_element(By.XPATH, newsletter_mail_input_xpath)
        newsletter_mail_input.send_keys(email_address)
        newsletter_input_button = driver.find_element(By.XPATH, newsletter_input_button_xpath)
        newsletter_input_button.click()
        success_alert = visibility_of_element_wait(driver, success_alert_xpath, 4)
        self.assertTrue(success_alert.text == success_alert_text, f'Cant subscribe newsletter for page '
                                                                  f'{driver.current_url}')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
