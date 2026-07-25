from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from urls import BASE_URL

def test_go_to_sauces_section(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.SAUCES_TAB).click()
    active_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
    )
    assert active_tab.text == "Соусы"

def test_go_to_fillings_section(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
    active_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
    )
    assert active_tab.text == "Начинки"

def test_go_to_buns_section(driver):
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.SAUCES_TAB).click()
    driver.find_element(*MainPageLocators.BUNS_TAB).click()
    active_tab = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ACTIVE_TAB)
    )
    assert active_tab.text == "Булки"
