from config import EMAIL, PASSWORD
from pages.order_page import Order
import time
import allure
import pytest


@pytest.mark.functional
@allure.description('Добавление товара в избранное и его удаление')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_favorite_and_delete(browser_headless):
    order = Order(browser_headless)
    order.visit()

