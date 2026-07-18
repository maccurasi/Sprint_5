import pytest
import random
import string
from selenium import webdriver

URL = "https://stellarburgers.education-services.ru"

def generate_email():
    random_digits = str(random.randint(10000, 99999))
    return f"bekbolat_test_{random_digits}@yandex.ru"

def generate_password():
    return "Test" + "".join(random.choices(string.digits, k=6))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    return {
        "name": "Bekbolat",
        "email": generate_email(),
        "password": generate_password()
    }
