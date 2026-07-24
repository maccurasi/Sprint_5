import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from locators import *
from data import URL

TAB_ACTIVE_CLASS = 'tab_tab_type_current__2BEPc'
TAB_BUNS_ACTIVE = "//div[contains(@class,'tab_tab_type_current__2BEPc') and .//span[text()='Булки']]"
TAB_SAUCES_ACTIVE = "//div[contains(@class,'tab_tab_type_current__2BEPc') and .//span[text()='Соусы']]"
TAB_FILLINGS_ACTIVE = "//div[contains(@class,'tab_tab_type_current__2BEPc') and .//span[text()='Начинки']]"

class TestConstructor:

    def test_go_to_buns_section(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, TAB_SAUCES).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, TAB_SAUCES_ACTIVE))
        )
        element = driver.find_element(By.XPATH, TAB_BUNS)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, TAB_BUNS_ACTIVE))
        )
        assert driver.find_element(By.XPATH, TAB_BUNS_ACTIVE).is_displayed()

    def test_go_to_sauces_section(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, TAB_SAUCES).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, TAB_SAUCES_ACTIVE))
        )
        assert driver.find_element(By.XPATH, TAB_SAUCES_ACTIVE).is_displayed()

    def test_go_to_fillings_section(self, driver):
        driver.get(URL)
        driver.find_element(By.XPATH, TAB_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, TAB_FILLINGS_ACTIVE))
        )
        assert driver.find_element(By.XPATH, TAB_FILLINGS_ACTIVE).is_displayed()
