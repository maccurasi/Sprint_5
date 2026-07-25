from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_user, login_user
from locators import MainPageLocators, RegisterPageLocators
from urls import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL

def test_login_from_main_page(driver):
    email, password = register_user(driver)
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"

def test_login_from_personal_account(driver):
    email, password = register_user(driver)
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"

def test_login_from_registration_form(driver):
    email, password = register_user(driver)
    driver.get(REGISTER_URL)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"

def test_login_from_forgot_password_form(driver):
    email, password = register_user(driver)
    driver.get(FORGOT_PASSWORD_URL)
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    login_user(driver, email, password)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"
