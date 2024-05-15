from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait


class Protein_page(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 'https://smart-food.shop/catalog/dobavki-dlya-sportsmenov/proteiny/syvorotochnyy-protein/')
        # Блок с кнопкапи сравнить, отложить и корзина
        self.card_compare = WebElement(driver,
                                       'div.catalog_block.items.row.margin0.has-bottom-nav.js_append.ajax_load.block.flexbox > div:nth-child(1)')
        self.compare_button = WebElement(driver, '(//div/div[2]/div[1]/div[2]/span)[7]', 'xpath')
        self.compare_modal_message = WebElement(driver, '#main > div.notice-surface.notice-surface--right')
        self.compare_menu_count = WebElement(driver, '#header > div > div.logo_and_menu-row.with-search.header__top-part > div > div > div.right-icons.wb.header__top-item > div > div:nth-child(2) > a > span > span.count')
        self.card_compare_2 = WebElement(driver, 'div.catalog_block.items.row.margin0.has-bottom-nav.js_append.ajax_load.block.flexbox > div:nth-child(2)')
        self.compare_button_2 = WebElement(driver, '(//div/div[2]/div[1]/div[2]/span)[11]', 'xpath')
        self.compare_menu = WebElement(driver, 'div.right-icons.wb.header__top-item > div > div:nth-child(2) > a')
        self.delete_all_compare_batton = WebElement(driver, ' div.catalog-compare__top.flexbox.flexbox--row.justify-content-between.align-items-normal > span')
        self.delete_one_card_button = WebElement(driver, '(//div/span)[32]', 'xpath')
        self.text_compare_menu_empty = WebElement(driver, 'p > font')
        self.checkbox_difference = WebElement(driver, '#compare_diff')
        self.checkbox_difference_div = WebElement(driver, 'div > div.owl-item.active.current > div > div')
        self.add_card_in_menu_compare_button = WebElement(driver,
                                                          '(//div/div[1]/div[1]/div/div[2]/div/div/div/a)[3]', 'xpath')



