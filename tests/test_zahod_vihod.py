from pages.registration_page import Registration
from pages.smart_food import Smart_food
from config import EMAIL, PASSWORD
import allure
import time


@allure.description('Проверка авторизации и выход в десктоп версии')
@allure.severity(allure.severity_level.CRITICAL)
def test_authorization(browser_headless):
    smart_food = Smart_food(browser_headless)
    smart_food.visit()

    with allure.step('Авторизация'):
        smart_food.register_button.wait_and_click_force()
        smart_food.login_email_modal_autorization.wait_and_click_force()
        smart_food.user_login_input.send_keys(EMAIL)
        smart_food.user_password_input.send_keys(PASSWORD)
        smart_food.user_label_zapomnit_menya.wait_and_click_force()
        smart_food.user_login_button.wait_and_click_force()

    with allure.step('Выход'):
        smart_food.cabinet_menu_button.wait_and_hover()
        cabinet_menu_button_title = smart_food.cabinet_menu_button.get_dom_attribute("Title")
        assert cabinet_menu_button_title == "autotest testing"
        smart_food.cabinet_menu_button_quit.wait_and_click_force()


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
    time.sleep(1)
