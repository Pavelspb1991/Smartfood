import pytest
from pages.order_page import Order
from pages.smart_food import Smart_food
import time
from config import EMAIL
from config import PASSWORD
import allure
import os

email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')


@allure.description('Проверка cлайдера,кнопки лево право,картинки и ссылки')
@allure.severity(allure.severity_level.CRITICAL)
def test_slider(browser_headless):
    smart_food = Smart_food(browser_headless)
    smart_food.visit()
    smart_food.slider_1.wait_for_element_visible()
    assert smart_food.slider_1.exist()
    assert smart_food.slider_1_img.visible()
    smart_food.slider_1.wait_and_hover()
    smart_food.slider_right_button.click_force()
    time.sleep(1)
    assert smart_food.slider_2.exist()
    assert smart_food.slider_2_img.visible()
    smart_food.slider_right_button.click_force()
    time.sleep(1)
    assert smart_food.slider_3_img.visible()
    smart_food.slider_left_button.click_force()
    time.sleep(1)
    assert smart_food.slider_2_img.visible()