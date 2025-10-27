import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Используем Firefox как указано в задании
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()