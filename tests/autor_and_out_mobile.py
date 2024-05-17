from pages.registration_page import Registration
from pages.smart_food import Smart_food
from config import EMAIL, PASSWORD
import allure
import time


@allure.description('Проверка авторизации и выход в десктоп версии')
@allure.severity(allure.severity_level.CRITICAL)
def test_authorization(browser_mobile_headless):
    smart_food = Smart_food(browser_mobile_headless)
    smart_food.visit()
    smart_food.register_button_mobile.wait_and_click_force()
    smart_food.login_email_modal_aut_mobile.wait_and_click_force()
    smart_food.user_login_input.send_keys(EMAIL)
    smart_food.user_password_input.send_keys(PASSWORD)
    smart_food.user_label_zapomnit_menya.wait_and_click()
    smart_food.user_login_button.wait_and_click()
    time.sleep(1)
