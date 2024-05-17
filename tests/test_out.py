import pytest
from pages.registration_page import Registration
from pages.smart_food import Smart_food
import time
from config import EMAIL
from config import PASSWORD
import allure


@allure.description('Проверка регистрации')
@allure.severity(allure.severity_level.CRITICAL)
def test_register(browser_headless):
    smart_food = Smart_food(browser_headless)
    register = Registration(browser_headless)

    smart_food.visit()
    time.sleep(2)
    with allure.step('Нажать на кнопку регистрации'):
        smart_food.register_button.wait_and_click_force()
        time.sleep(1)
        smart_food.registration_button.wait_and_click_force()
    assert smart_food.get_url() == 'https://smart-food.shop/auth/registration/?register=yes&backurl=/'
    with allure.step('Заполнить форму регистрации'):
        register.input_name.send_keys('Тест')
        register.input_email.send_keys('xx@xx.xx')
        register.input_phone.send_keys('1111111111')
        register.input_password.send_keys('123456')
        register.confirm_password.send_keys('123456')
        register.capcha.send_keys('123456')
        time.sleep(2)
    register.capcha_refresh.wait_and_click_force()
    time.sleep(1)
    assert register.capcha.get_text() == ""


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
