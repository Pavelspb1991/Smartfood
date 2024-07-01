from pages.base_page import BasePage
from pages.protein_page import Protein_page
from pages.registration_page import Registration
from pages.smart_food import Smart_food
from components.components import WebElement


class Order(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://smart-food.shop/')
        self.card_compare = WebElement(driver,
                                       'div.catalog_block.items.row.margin0.has-bottom-nav.js_append.ajax_load.block.flexbox > div:nth-child(1)')
        self.compare_button = WebElement(driver, '(//div/div[2]/div[1]/div[2]/span)[7]', 'xpath')
        self.compare_modal_message = WebElement(driver, '#main > div.notice-surface.notice-surface--right')
        self.compare_menu_count = WebElement(driver,
                                             '#header > div > div.logo_and_menu-row.with-search.header__top-part > div > div > div.right-icons.wb.header__top-item > div > div:nth-child(2) > a > span > span.count')
        self.card_compare_2 = WebElement(driver,
                                         'div.catalog_block.items.row.margin0.has-bottom-nav.js_append.ajax_load.block.flexbox > div:nth-child(2)')
        self.compare_button_2 = WebElement(driver, '(//div/div[2]/div[1]/div[2]/span)[11]', 'xpath')
        self.compare_menu = WebElement(driver, 'div.right-icons.wb.header__top-item > div > div:nth-child(2) > a')
        self.delete_all_compare_batton = WebElement(driver,
                                                    ' div.catalog-compare__top.flexbox.flexbox--row.justify-content-between.align-items-normal > span')
        self.delete_one_card_button = WebElement(driver, '(//div/span)[32]', 'xpath')
        self.text_compare_menu_empty = WebElement(driver, 'p > font')
        self.checkbox_difference = WebElement(driver, '#compare_diff')
        self.checkbox_difference_div = WebElement(driver, 'div > div.owl-item.active.current > div > div')
        self.add_card_in_menu_compare_button = WebElement(driver,
                                                          '(//div/div[1]/div[1]/div/div[2]/div/div/div/a)[3]', 'xpath')
        self.input_name = WebElement(driver, '#input_NAME')
        self.input_email = WebElement(driver, "#input_EMAIL")
        self.input_phone = WebElement(driver, "#input_PERSONAL_PHONE")
        self.input_password = WebElement(driver, '#input_PASSWORD')
        self.confirm_password = WebElement(driver, '#input_CONFIRM_PASSWORD')
        self.capcha = WebElement(driver, ' div.captcha_input > input')
        self.capcha_refresh = WebElement(driver,
                                         "#registraion-page-form > div.form_body > div.form-control.captcha-row.clearfix > div.captcha_image > div")
        self.register_button = WebElement(driver, ".person > div:nth-child(1) > a:nth-child(1)")
        self.login_email_modal_autorization = WebElement(driver, ".nav > li:nth-child(2) > a:nth-child(1)")
        self.user_login_input = WebElement(driver, "#USER_LOGIN_POPUP")
        self.user_password_input = WebElement(driver, "#auth_by_login > div:nth-child(2) > input:nth-child(2)")
        self.user_label_zapomnit_menya = WebElement(driver, ".prompt > label:nth-child(2)")
        self.user_login_button = WebElement(driver, "button.btn:nth-child(2)")
        self.cabinet_menu_button = WebElement(driver,
                                              "div.right-icons.wb.header__top-item > div > div:nth-child(1) > div > div > a")
        self.cabinet_menu_button_quit = WebElement(driver,
                                                   " .person > div:nth-child(1) > ul:nth-child(3) > li:nth-child(11) > a:nth-child(1)")
        self.catalog_button = WebElement(driver, 'td.menu-item.dropdown.catalog.wide_menu > div > a')
        self.sales_button = WebElement(driver, 'tr > td:nth-child(2) > div > a')
        self.goals_button = WebElement(driver, 'tr > td:nth-of-type(3) > div > a')
        self.articles_button = WebElement(driver, ' td:nth-child(4) > div > a')
        self.brands_button = WebElement(driver, 'td:nth-child(5) > div > a')
        self.payments_shipping_button = WebElement(driver, "td:nth-child(6) > div > a")
        self.contacts_button = WebElement(driver, 'td:nth-child(7) > div > a')
        self.registration_button = WebElement(driver, 'div.line-block__item.width100 > a')
        # Блок слайдер
        self.slider_1 = WebElement(driver, '#bx_2875157043_9621 > a')
        self.slider_1_img = WebElement(driver, '#bx_2875157043_9621 > div > table > tbody > tr > td > a > img')
        self.slider_right_button = WebElement(driver, ' div > div.swiper-button-next')
        self.slider_2 = WebElement(driver, '#bx_2875157043_9622 > a')
        self.slider_3 = WebElement(driver, '#bx_2875157043_9574 > a')
        self.slider_2_img = WebElement(driver, '#bx_2875157043_9622 > div > table > tbody > tr > td > a > img')
        self.slider_3_img = WebElement(driver, '#bx_2875157043_9574 > div > table > tbody > tr > td > a > img')
        self.slider_left_button = WebElement(driver, 'div > div.swiper-button-prev')
        # Блок для заказа и класса order
        self.add_to_basket_button = WebElement(driver, '//div/div[3]/div[2]/div/div[3]/div/span[1]', 'xpath')
        self.go_to_order_button = WebElement(driver, 'div.basket-checkout-section-right > div > button')
        self.order_from_store_evrika_button = WebElement(driver,
                                                         '//*[@id="bx-soa-delivery"]/div[3]/div[2]/div[1]/div[2]/div/div[1]/label/span',
                                                         'xpath')
        self.select_store_evrika = WebElement(driver, '#store-8 > div.bx-soa-pickup-item-info')
        self.payment_method = WebElement(driver, '#bx-soa-paysystem > div.bx-soa-section-title-container.bx-soa-section-title-container--flex > div')
        self.payment_method_cash_button = WebElement(driver, '//*[@id="bx-soa-paysystem"]/div[2]/div[2]/div/div[2]/div/div[1]/label/span',  'xpath')
        self.place_an_order_button = WebElement(driver, '.bx-soa-total-wrapper > div:nth-child(1) > div:nth-child(9) > a:nth-child(1)')
        self.order_discription_input = WebElement(driver, '#orderDescription')
        self.check_order_success = WebElement(driver, ' tr > td > b:nth-child(1)')
        self.cancel_order_button = WebElement(driver, 'div.col-md-2.col-sm-12.sale-order-list-cancel-container > a')
        self.cancel_order_area_input = WebElement(driver, 'form > textarea')
        self.cancel_order_final_button = WebElement(driver, ' input[type=submit]:nth-child(12)')
        self.orders_not_found_text = WebElement(driver, 'div > h3')
        # Блок для добавления товаров в избранное
        self.favorite_button = WebElement(driver, 'div.right-icons.wb.header__top-item > div > div:nth-child(3) > a > span')
        self.add_to_favorite_button = WebElement(driver, '(//div/div[2]/div[1]/div[1]/span)[9]', 'xpath')
        self.add_to_favorite_2_button = WebElement(driver, '(//div/div[2]/div[1]/div[1]/span)[10]', 'xpath')
        self.favorite_menu_count = WebElement(driver, ' div > div:nth-child(3) > a > span > span.count.js-count')
        self.delete_all_favorite_button = WebElement(driver, ' div.topic > div > div > div')
        # селекторы моблиьной версии
        self.register_button_mobile = WebElement(driver,
                                                 'div.right-icons.pull-right > div:nth-child(2) > div > div > a')
        self.login_email_modal_aut_mobile = WebElement(driver, '//*[@id="auth-page-form"]/div[1]/div/div[1]/ul/li[2]/a',
                                                       'xpath')

        self.search_input_mobile_button = WebElement(driver, 'div:nth-child(3) > div > button')
        self.search_input_mobile_input = WebElement(driver, '#title-search-input')
        self.text_catalog = WebElement(driver, '#pagetitle')








