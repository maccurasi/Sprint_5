import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from locators import *
from conftest import URL

EMAIL = "amanbek_bekbolat_49_33@yandex.ru"
PASSWORD = "513937иуЛфв"

class TestProfile:

    def login(self, driver):
        driver.get(f"{URL}/login")
        driver.find_element(By.XPATH, LOGIN_EMAIL_FIELD).send_keys(EMAIL)
        driver.find_element(By.XPATH, LOGIN_PASSWORD_FIELD).send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))

    def test_go_to_personal_account(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_go_to_constructor_from_profile(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"

    def test_go_to_constructor_via_logo(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        driver.find_element(By.CSS_SELECTOR, LOGO).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{URL}/"))
        assert driver.current_url == f"{URL}/"

    def test_logout(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON))
        )
        driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
