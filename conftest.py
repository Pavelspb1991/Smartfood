import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1500, 1100)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser_headless():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1500, 1100)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def delay_between_tests():
    yield
    time.sleep(2)
