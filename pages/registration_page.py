from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Registration(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://smart-food.shop/'
        super().__init__(driver, self.base_url)
        self.input_name = WebElement(driver, '#input_NAME')
        self.input_email = WebElement(driver, "#input_EMAIL")
        self.input_phone = WebElement(driver, "#input_PERSONAL_PHONE")
        self.input_password = WebElement(driver, '#input_PASSWORD')
        self.confirm_password = WebElement(driver, '#input_CONFIRM_PASSWORD')
        self.capcha = WebElement(driver,' div.captcha_input > input')
        self.capcha_refresh = WebElement(driver, "#registraion-page-form > div.form_body > div.form-control.captcha-row.clearfix > div.captcha_image > div")






#input_NAME