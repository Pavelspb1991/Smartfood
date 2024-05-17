from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import logging


class WebElement:

    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def click(self):
        self.find_element().click()

    def click_x(self, x):
        for i in range(x):
            self.find_element().click()

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.DELETE)

    def enter(self):
        self.find_element().send_keys(Keys.ENTER)

    def arrow_right(self):
        self.find_element().send_keys(Keys.ARROW_RIGHT)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + "not correct")
        return False

    def scroll_to_element(self):
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value

    def find_element_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def find_elements_by_tag_name(self, tag_name):
        return self.driver.find_elements_by_tag_name(tag_name)

    def wait_and_click(self):
        element = self.wait.until(EC.element_to_be_clickable((self.get_by_type(), self.locator)))
        element.click()

    def wait_and_hover(self):
        element = self.wait.until(EC.visibility_of_element_located((self.get_by_type(), self.locator)))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_clickable_and_hover(self):
        element = self.wait.until(EC.element_to_be_clickable((self.get_by_type(), self.locator)))
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_for_element_visible(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((self.get_by_type(), self.locator)))

    def wait_for_element_clickable(self, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((self.get_by_type(), self.locator)))
        return element  # Возвращаем базовый WebElement от Selenium

    def press_and_hold_ctrl(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.LEFT_CONTROL).click(self.find_element()).perform()

    def open_new_tab(self):
        button = self.get_selenium_webelement()
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).click(button).key_up(Keys.CONTROL).perform()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def close_new_tab(self):
        self.driver.close()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])

    def get_selenium_webelement(self):
        return self.wait_for_element_clickable()

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

    def wait_and_click_force(self):
        self.wait.until(EC.element_to_be_clickable((self.get_by_type(), self.locator)))
        self.click_force()