from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Smart_food(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://smart-food.shop/'
        super().__init__(driver, self.base_url)
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
        self.registration_button = WebElement(driver,'div.line-block__item.width100 > a')

    def test_button_link(self, button, url):
        button.open_new_tab()
        # Ожидание
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == url)
        assert self.driver.current_url == url, f"Expected URL {url}, but got {self.driver.current_url}"
        button.close_new_tab()
