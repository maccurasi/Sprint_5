from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_email
from locators import RegisterPageLocators
from urls import REGISTER_URL

def test_successful_registration(driver):
    driver.get(REGISTER_URL)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Bekbolat")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    assert "/login" in driver.current_url

def test_registration_with_invalid_password(driver):
    driver.get(REGISTER_URL)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("Bekbolat")
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.INCORRECT_PASSWORD)
    )
    assert error.text == "Некорректный пароль"
