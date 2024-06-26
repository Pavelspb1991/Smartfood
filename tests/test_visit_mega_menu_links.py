import pytest
from pages.smart_food import Smart_food
import time
import allure
import os

email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')

# Проверка кликабельности кнопок мега-меню
@pytest.mark.smoke
@allure.description('Проверка кликабельности кнопок мега-меню (зеленые) и переход по ним')
@allure.severity(allure.severity_level.NORMAL)
def test_mega_menu_buttons(browser_headless):
    smart_food = Smart_food(browser_headless)
    smart_food.visit()

    links = [
        ('catalog_button', 'https://smart-food.shop/catalog/'),
        ('sales_button', 'https://smart-food.shop/sale/'),
        ('goals_button', 'https://smart-food.shop/goals/'),
        ('articles_button', 'https://smart-food.shop/articles/'),
        ('brands_button', 'https://smart-food.shop/brands/'),
        ('payments_shipping_button', 'https://smart-food.shop/payment-shipping/'),
        ('contacts_button', 'https://smart-food.shop/contacts/')

    ]

    for button_name, url in links:
        button = getattr(smart_food, button_name)
        assert button.visible()
        smart_food.test_button_link(button, url)
