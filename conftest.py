import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import generate_email, generate_password

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
