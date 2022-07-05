from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def user_login(driver, user_login: str, user_password: str) -> None:
    """Login user to website using given company, login and password

    :param driver: webdriver instance
    :param user_login, user_password
    :return None
    """
    login_page_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
    signin_page_button_xpath = '//a[@class="login"]'
    input_email_xpath = '//input[@id="email"]'
    input_password_xpath = '//input[@id="passwd"]'
    input_signin_xpath = '//button[@id="SubmitLogin"]'
    driver.get(login_page_url)
    signin_button = driver.find_element(By.XPATH, signin_page_button_xpath)
    signin_button.click()
    input_email = driver.find_element(By.XPATH, input_email_xpath)
    input_email.send_keys(user_login)
    input_password = driver.find_element(By.XPATH, input_password_xpath)
    input_password.send_keys(user_password)
    input_signin = driver.find_element(By.XPATH, input_signin_xpath)
    input_signin.click()


def user_logout(driver: WebDriver) -> None:
    """Logs out the user when logged in

       :param driver: webdriver instance
       :return None
       """
    logout_button_xpath = '//a[@title="Log me out"]'
    try:
        driver.find_element(By.XPATH, logout_button_xpath).click()
    except NoSuchElementException:
        pass