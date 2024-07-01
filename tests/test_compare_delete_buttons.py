from pages.protein_page import Protein_page
import time
import allure
import pytest

import os

email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')
@allure.description('Проверка  добавления и удаления товаров 2 товаров из сравнения')
@allure.severity(allure.severity_level.NORMAL)
def test_compare_button(browser_headless):
    protein_page = Protein_page(browser_headless)
    protein_page.visit()
    protein_page.card_compare.exist()
    protein_page.card_compare.wait_and_hover()
    with allure.step('Нажать на кнопку сравнения 1 товар'):
        protein_page.compare_button.click_force()
    protein_page.compare_modal_message.wait_for_element_visible()
    with allure.step('Проверить кликабельность модальное окно'):
        assert protein_page.compare_modal_message.visible()
    protein_page.compare_modal_message.click()
    time.sleep(2)
    protein_page.back()
    time.sleep(2)
    with allure.step('Проверить, что счетчик +1'):
        assert protein_page.compare_menu_count.get_text() == '1'
    with allure.step('Нажать на кнопку сравнения 2  карточки товара'):
        protein_page.card_compare_2.wait_and_hover()
        protein_page.compare_button_2.click()
    time.sleep(2)
    with allure.step('Проверить счетчик после 2 товара'):
        assert protein_page.compare_menu_count.get_text() == '2'
    protein_page.refresh()
    protein_page.compare_menu.click()
    with allure.step('Нажать на кнопку удалить все и проверить,что счетчик 0'):
        protein_page.delete_all_compare_batton.click()
        protein_page.refresh()
        assert protein_page.compare_menu_count.get_text() == '0'


@allure.description('Проверка  добавления и удаления товаров 2 товаров из сравнения,по одному')
@allure.severity(allure.severity_level.NORMAL)
def test_compare_button_2(browser_headless):
    protein_page = Protein_page(browser_headless)
    protein_page.visit()
    protein_page.card_compare.exist()
    protein_page.card_compare.wait_and_hover()
    with allure.step('Нажать на кнопку сравнения 2 товаров'):
        protein_page.compare_button.click()
        protein_page.card_compare_2.wait_and_hover()
        protein_page.compare_button_2.click()
        protein_page.refresh()
        protein_page.compare_menu.click()
        protein_page.delete_one_card_button.wait_and_click()
        time.sleep(2)
        protein_page.delete_one_card_button.wait_and_click()
    with allure.step('Обновляем страницу'):
        protein_page.refresh()
    with allure.step('Проверить, что cписок сравниваемых элементов пуст'):
        assert protein_page.text_compare_menu_empty.get_text() == 'Список сравниваемых элементов пуст.'


@allure.description('Проверка  чекбокса  Только отличия в меню сравнения')
@allure.severity(allure.severity_level.NORMAL)
def test_checkbox_compare(browser_headless):
    protein_page = Protein_page(browser_headless)
    protein_page.visit()
    protein_page.card_compare.exist()
    protein_page.card_compare.wait_and_hover()
    with allure.step('Нажать на кнопку сравнения 2 товаров'):
        protein_page.compare_button.click()
        protein_page.card_compare_2.wait_and_hover()
        protein_page.compare_button_2.click()
        protein_page.refresh()
        protein_page.compare_menu.click()
        time.sleep(2)
    with allure.step('Считаем количество div с опциями сравнения'):
        div_before_click = protein_page.checkbox_difference_div.find_elements()
    with allure.step('Клик на чебокс с разницей'):
        protein_page.checkbox_difference.click_force()
    time.sleep(2)
    with allure.step('Считаем количество div с опциями после клика на чекбокс,должнно быть разное количество'):
        assert div_before_click != protein_page.checkbox_difference_div.find_elements()


@allure.description('Проверка  добавления товаров сравнения из меню сравнения')
@allure.severity(allure.severity_level.NORMAL)
def test_add_card_to_compare(browser_headless):
    protein_page = Protein_page(browser_headless)
    protein_page.visit()
    protein_page.card_compare.wait_for_element_clickable()
    with allure.step('Нажать на кнопку добавления товаров в сравнение'):
        protein_page.card_compare.wait_and_hover()
        protein_page.compare_button.click_force()
    protein_page.refresh()
    time.sleep(1)
    protein_page.compare_menu.click_force()
    with allure.step('Нажать на кнопку добавления карточки в сравнение из меню сравнения'):
        protein_page.add_card_in_menu_compare_button.click_force()
    time.sleep(1)