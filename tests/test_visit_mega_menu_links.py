import pytest
from pages.smart_food import Smart_food
import time
import allure


# Проверка кликабельности кнопок мега-меню
@pytest.mark.smoke
@allure.description('Проверка авторизации и выход')
@allure.severity(allure.severity_level.NORMAL)
def test_mega_menu_buttons(browser):
    smart_food = Smart_food(browser)
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
