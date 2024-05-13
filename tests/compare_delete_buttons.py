from pages.massa_page import Mass_page
import time
import allure
import pytest


@allure.description('Проверка  добавления и удаления товаров из сравнения')
@allure.severity(allure.severity_level.NORMAL)
def test_compare_button(browser):
    mass_page = Mass_page(browser)
    mass_page.visit()
    mass_page.card_compare.exist()
    mass_page.card_compare.wait_and_hover()
    with allure.step('Нажать на кнопку сравнения'):
        mass_page.compare_button.click_force()
    mass_page.compare_modal_message.wait_for_element_visible()
    with allure.step('Проверить модальное окно'):
        assert mass_page.compare_modal_message.visible()
    mass_page.compare_modal_message.click()
    time.sleep(2)
    mass_page.back()
