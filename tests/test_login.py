import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from locators import *
from data import EMAIL, PASSWORD, URL

class TestLogin:

    def test_login_via_main_button(self, driver):
        driver.get(URL)
        driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_MAIN).click()
        driver.find_element(By.XPATH, LOGIN_EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(By.XPATH, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"

    def test_login_via_personal_account(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        driver.find_element(By.XPATH, LOGIN_EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(By.XPATH, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"

    def test_login_via_register_link(self, driver):
        driver.get(f"{URL}/register")
        driver.find_element(By.XPATH, REGISTER_LOGIN_LINK).click()
        driver.find_element(By.XPATH, LOGIN_EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(By.XPATH, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"

    def test_login_via_forgot_password_link(self, driver):
        driver.get(f"{URL}/forgot-password")
        driver.find_element(By.XPATH, FORGOT_PASSWORD_LOGIN_LINK).click()
        driver.find_element(By.XPATH, LOGIN_EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(By.XPATH, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"
