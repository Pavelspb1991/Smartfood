from selenium.webdriver import Keys

from pages.order_page import Order
from pages.smart_food import Smart_food
from config import EMAIL, PASSWORD
import allure
import time

import os

email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')


@allure.description('Проверка поиска при пустов поле поиска и нажатие enter')
@allure.severity(allure.severity_level.CRITICAL)
def test_order_mobile(browser_mobile_headless):
    search = Order(browser_mobile_headless)
    search.visit()
    search.search_input_mobile_button.click()
    search.search_input_mobile_input.send_keys('')
    search.search_input_mobile_input.send_keys(Keys.ENTER)
    time.sleep(1)
    assert search.text_catalog.get_text() == 'Каталог'


@allure.description('Проверка поиска при вводе слова протеин и нажатие enter')
@allure.severity(allure.severity_level.CRITICAL)
def test_order_mobile(browser_mobile_headless):
    search = Order(browser_mobile_headless)
    search.visit()
    search.search_input_mobile_button.click()
    search.search_input_mobile_input.send_keys('Протеин')
    search.search_input_mobile_input.send_keys(Keys.ENTER)
    time.sleep(1)
