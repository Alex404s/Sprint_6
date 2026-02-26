from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(BasePageLocators.home_title_img))

    def click_order_button_top(self):
        self.driver.find_element(*BasePageLocators.order_button_top).click()

    def click_scooter_button(self):
        self.driver.find_element(*BasePageLocators.scooter_button).click()

    def click_yandex_button(self):
        self.driver.find_element(*BasePageLocators.yandex_button).click()

