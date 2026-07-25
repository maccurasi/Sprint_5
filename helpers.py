from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_email, generate_password
from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators
from urls import REGISTER_URL, LOGIN_URL

def wait_and_click(driver, locator):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    ).click()

def wait_and_send_keys(driver, locator, text):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator)
    ).send_keys(text)

def register_user(driver):
    email = generate_email()
    password = generate_password()
    driver.get(REGISTER_URL)
    wait_and_send_keys(driver, RegisterPageLocators.NAME_INPUT, "Bekbolat")
    wait_and_send_keys(driver, RegisterPageLocators.EMAIL_INPUT, email)
    wait_and_send_keys(driver, RegisterPageLocators.PASSWORD_INPUT, password)
    wait_and_click(driver, RegisterPageLocators.REGISTER_BUTTON)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    return email, password

def login_user(driver, email, password):
    wait_and_send_keys(driver, LoginPageLocators.EMAIL_INPUT, email)
    wait_and_send_keys(driver, LoginPageLocators.PASSWORD_INPUT, password)
    wait_and_click(driver, LoginPageLocators.LOGIN_BUTTON)

def register_and_login_user(driver):
    email, password = register_user(driver)
    driver.get(LOGIN_URL)
    login_user(driver, email, password)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    )
    return email, password
