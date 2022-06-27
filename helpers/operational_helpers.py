import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_elements(driver: WebDriver, xpath: str, max_seconds_to_wait=5, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath is grater then 0
    :param driver: WebDriver instance
    :param xpath: xpath of web element
    :param max_seconds_to_wait: Maximum number of seconds function will wait (default: 5)
    :param number_of_expected_elements: Minimum number of elements function will waiting for (default: 1)
    :return list of found elements
    """
    for i in range(max_seconds_to_wait):
        elements = driver.find_elements(by=By.XPATH, value=xpath)
        print(f'Total waiting: {i} sec.')
        if len(elements) >= number_of_expected_elements:
            return elements
        if i == max_seconds_to_wait - 1:
            print(f'End of time...')
            assert len(elements) >= number_of_expected_elements, f'Expected {number_of_expected_elements}, but found ' \
                                                                 f'{len(elements)} for XPATH: {xpath} in time of ' \
                                                                 f'{max_seconds_to_wait} '
        time.sleep(1)


def visibility_of_element_wait(driver, xpath: str, timeout=1) -> WebElement:
    """Checking every 0.5 second if element specified by xpath is visible on page

    :param driver: WebDriver instance
    :param xpath: xpath of expected element
    :param timeout: max time to wait for element appear (default: 10
    :return: first element in list of found elements
    """
    timeout_message = f'Cant find element {xpath} for url {driver.current_url} with waiting time {timeout} '
    locator = (By.XPATH, xpath)
    element_located = expected_conditions.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout)
    return wait.until(element_located, timeout_message)


def visibility_of_all_elements_wait(driver: WebDriver, xpath: str, timeout=10) -> WebElement:
    """Checking every 0.5 second if elements specified by xpath is visible on page

       :param driver: WebDriver instance
       :param xpath: xpath of expected elements
       :param timeout: max time to wait for element appear (default: 10
       :return: list of found elements
       """

    timeout_message = f'Cant find element {xpath} for url {driver.current_url} with waiting time {timeout} '
    locator = (By.XPATH, xpath)
    elements_located = expected_conditions.visibility_of_all_elements_located(locator)
    wait = WebDriverWait(driver, timeout)
    return wait.until(elements_located, timeout_message)