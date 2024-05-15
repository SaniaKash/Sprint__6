import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions




@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
