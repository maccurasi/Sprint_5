import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from locators import *
from data import URL

class TestRegistration:

    def test_register_success(self, driver, user_data):
        driver.get(f"{URL}/register")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, REGISTER_NAME_FIELD))
        )
        driver.find_element(By.XPATH, REGISTER_NAME_FIELD).send_keys(user_data["name"])
        driver.find_element(By.XPATH, REGISTER_EMAIL_FIELD).send_keys(user_data["email"])
        driver.find_element(By.XPATH, REGISTER_PASSWORD_FIELD).send_keys(user_data["password"])
        driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_register_invalid_password(self, driver, user_data):
        driver.get(f"{URL}/register")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, REGISTER_NAME_FIELD))
        )
        driver.find_element(By.XPATH, REGISTER_NAME_FIELD).send_keys(user_data["name"])
        driver.find_element(By.XPATH, REGISTER_EMAIL_FIELD).send_keys(user_data["email"])
        driver.find_element(By.XPATH, REGISTER_PASSWORD_FIELD).send_keys("123")
        driver.find_element(By.CSS_SELECTOR, REGISTER_SUBMIT_BUTTON).click()
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_ERROR))
        )
        assert error.is_displayed()
