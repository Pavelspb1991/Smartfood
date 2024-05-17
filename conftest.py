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


@pytest.fixture(scope="session")
def browser_mobile():
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 9; Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def browser_mobile_headless():
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 740, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 9; Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(
        "--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(360, 740)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def delay_between_tests():
    yield
    time.sleep(4)
