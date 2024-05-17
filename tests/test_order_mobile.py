from pages.order_page import Order
from pages.smart_food import Smart_food
from config import EMAIL, PASSWORD
import allure
import time


@allure.description('Проверка авторизации и выход в десктоп версии')
@allure.severity(allure.severity_level.CRITICAL)
def test_order_mobile(browser_mobile_headless):
    order = Order(browser_mobile_headless)
    order.visit()
    order.register_button_mobile.wait_and_click_force()
    order.login_email_modal_aut_mobile.wait_and_click_force()
    order.user_login_input.send_keys(EMAIL)
    order.user_password_input.send_keys(PASSWORD)
    order.user_label_zapomnit_menya.wait_and_click()
    order.user_login_button.wait_and_click()
    time.sleep(1)
    with allure.step('Переход на страницу с товаром и добавления в корзину'):
        browser_mobile_headless.get('https://smart-food.shop/catalog/dobavki-dlya-sportsmenov/proteiny/syvorotochnyy-protein/')
        order.add_to_basket_button.scroll_to_element()
        order.add_to_basket_button.click_force()
    with allure.step('Оформление заказа из корзины'):
        browser_mobile_headless.get('https://smart-food.shop/basket/')
        order.go_to_order_button.wait_and_click_force()
    with allure.step('Меню оформления заказа'):
        order.order_from_store_evrika_button.wait_and_click_force()
        order.select_store_evrika.wait_and_hover()
        order.select_store_evrika.click_force()
        assert order.payment_method.exist()
    with allure.step('Выбор метода оплаты'):
        order.payment_method.scroll_to_element()
        order.payment_method.wait_and_click_force()
        order.payment_method_cash_button.wait_and_click_force()
    order.order_discription_input.send_keys('Тестирование сайта! Отмените заказ!')
    time.sleep(1)
    with allure.step('Подтверждение заказа и проверка успешности заказа'):
        order.place_an_order_button.click_force()
        order.check_order_success.wait_for_element_visible()
        assert order.check_order_success.exist()
    with allure.step('Отмена заказа из личного кабинета'):
        browser_mobile_headless.get('https://smart-food.shop/personal/orders/')
        order.cancel_order_button.wait_and_hover()
        order.cancel_order_button.click_force()
        order.cancel_order_area_input.wait_and_hover()
        order.cancel_order_area_input.send_keys('Тестирование сайта! Отмените заказ!')
        order.cancel_order_final_button.click_force()
    time.sleep(2)
    with allure.step('Проверка того,что заказы отменены'):
        order.orders_not_found_text.wait_for_element_visible()
        assert order.orders_not_found_text.get_text() == 'Текущие заказы не найдены'
