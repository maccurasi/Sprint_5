from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import register_and_login_user
from locators import MainPageLocators, ProfilePageLocators
from urls import BASE_URL

def test_go_to_personal_account(driver):
    register_and_login_user(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )
    assert "/account/profile" in driver.current_url

def test_go_from_account_to_constructor_by_constructor_button(driver):
    register_and_login_user(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"

def test_go_from_account_to_constructor_by_logo(driver):
    register_and_login_user(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )
    driver.find_element(*MainPageLocators.LOGO).click()
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL + "/")
    )
    assert driver.current_url == BASE_URL + "/"

def test_logout_from_personal_account(driver):
    register_and_login_user(driver)
    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account/profile")
    )
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url
