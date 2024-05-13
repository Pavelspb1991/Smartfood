from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class Mass_page(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://smart-food.shop/goals/nabor-myshechnoy-massy/'
        super().__init__(driver, self.base_url)
        # Блок с кнопкапи сравнить, отложить и корзина
        self.card_compare = WebElement(driver,
                                       'div.catalog_block.items.row.margin0.has-bottom-nav.js_append.ajax_load.block.flexbox > div:nth-child(1)')
        self.compare_button = WebElement(driver, '(//div/div[2]/div[1]/div[2]/span)[4]', 'xpath')
        self.compare_modal_message = WebElement(driver, '#main > div.notice-surface.notice-surface--right')
        self.compare_menu_count = WebElement(driver, 'a.basket-link.compare.inner-table-block.big.basket-count > span > span.count')
