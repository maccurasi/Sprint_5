import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from locators import *
from conftest import URL

class TestConstructor:

    def test_go_to_buns_section(self, driver):
        driver.get(URL)
        element = driver.find_element(By.XPATH, TAB_BUNS)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, SECTION_BUNS))
        )
        assert driver.find_element(By.XPATH, SECTION_BUNS).is_displayed()

    def test_go_to_sauces_section(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, TAB_SAUCES).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, SECTION_SAUCES))
        )
        assert driver.find_element(By.XPATH, SECTION_SAUCES).is_displayed()

    def test_go_to_fillings_section(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, TAB_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, SECTION_FILLINGS))
        )
        assert driver.find_element(By.XPATH, SECTION_FILLINGS).is_displayed()
