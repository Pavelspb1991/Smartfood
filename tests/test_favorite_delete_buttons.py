from config import EMAIL, PASSWORD
from pages.order_page import Order
import time
import allure
import pytest
import os

email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')

@pytest.mark.functional
@allure.description('Добавление товара в избранное и его удаление')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_favorite_and_delete(browser_headless):
    order = Order(browser_headless)
    browser_headless.get('https://smart-food.shop/catalog/dobavki-dlya-sportsmenov/proteiny/syvorotochnyy-protein/')
    with allure.step('Проверка добавления товара в избранное'):
        order.card_compare.wait_and_hover()
        order.add_to_favorite_button.click_force()
        order.card_compare_2.wait_and_hover()
        order.add_to_favorite_2_button.click_force()
        time.sleep(1)
    order.refresh()
    with allure.step('Проверка того,что добавлено 2 товара в избранное'):
        order.favorite_button.wait_and_click_force()
        time.sleep(1)
        assert order.favorite_menu_count.get_text() == '2'
    with allure.step('Удаление из избранного'):
        order.delete_all_favorite_button.click_force()
        time.sleep(1)
        assert order.favorite_menu_count.get_text() != '2'


@pytest.mark.functional
@allure.description('Добавление товара в избранное и его удаление в мобильной версии')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_favorite_and_delete_mobile(browser_mobile_headless):
    order = Order(browser_mobile_headless)
    browser_mobile_headless.get(
        'https://smart-food.shop/catalog/dobavki-dlya-sportsmenov/proteiny/syvorotochnyy-protein/')
    with allure.step('Проверка добавления товара в избранное'):
        order.card_compare.wait_and_hover()
        order.add_to_favorite_button.click_force()
        order.card_compare_2.wait_and_hover()
        order.add_to_favorite_2_button.click_force()
    time.sleep(1)
    with allure.step('Удаление из избрарного'):
        browser_mobile_headless.get('https://smart-food.shop/personal/favorite/')
        order.delete_all_favorite_button.click_force()
        time.sleep(1)
