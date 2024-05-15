import pytest
from pages.registration_page import Registration
from pages.smart_food import Smart_food
import time
from config import EMAIL
from config import PASSWORD
import allure


@pytest.mark.functional
@allure.description('Проверка авторизации и выход')
@allure.severity(allure.severity_level.CRITICAL)
def test_authorization_and_out(browser_headless):  # Тест проверяет авторизацию на сайте по email и выходит из аккаунта
    smart_food = Smart_food(browser_headless)
    smart_food.visit()
    smart_food.register_button.click()
    smart_food.login_email_modal_autorization.wait_and_click()
    smart_food.user_login_input.send_keys(EMAIL)
    smart_food.user_password_input.send_keys(PASSWORD)
    smart_food.user_label_zapomnit_menya.wait_and_click()
    smart_food.user_login_button.wait_and_click()
    time.sleep(1)
    smart_food.cabinet_menu_button.wait_and_hover()
    cabinet_menu_button_title = smart_food.cabinet_menu_button.get_dom_attribute("Title")
    assert cabinet_menu_button_title == "autotest testing"
    smart_food.cabinet_menu_button_quit.click()
    browser_headless.refresh()
    cabinet_menu_button_title = smart_food.cabinet_menu_button.get_dom_attribute("Title")
    assert cabinet_menu_button_title != "autotest testing"


@pytest.mark.functional
@allure.description('Проверка регистрации')
@allure.severity(allure.severity_level.CRITICAL)
def test_registration(browser_headless):
    smart_food = Smart_food(browser_headless)
    register = Registration(browser_headless)

    smart_food.visit()
    smart_food.register_button.click()
    smart_food.registration_button.wait_and_click()
    assert smart_food.get_url() == 'https://smart-food.shop/auth/registration/?register=yes&backurl=/'
    register.input_name.send_keys('Тест')
    register.input_email.send_keys('xx@xx.xx')
    register.input_phone.send_keys('1111111111')
    register.input_password.send_keys('123456')
    register.confirm_password.send_keys('123456')
    register.capcha.send_keys('123456')
    time.sleep(1)
    register.capcha_refresh.click()
    time.sleep(1)
    assert register.capcha.get_text() == ""

    time.sleep(1)


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