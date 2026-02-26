from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.scooter_order_page_locators import ScooterOrderPageLocators
from .base_page import BasePage
import time




class ScooterOrderPage:
    def __init__(self, driver):
        self.driver = driver  

    def scroll_to_bottom_button(self):
        button_bottom = self.driver.find_element(*ScooterOrderPageLocators.order_button_bottom_field)
        self.driver.execute_script("arguments[0].scrollIntoView();", button_bottom)  

    def click_order_bottom_button(self):
        self.driver.find_element(*ScooterOrderPageLocators.order_button_bottom_field).click()

    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(ScooterOrderPageLocators.order_field))
    
    def send_name(self, name):
        self.driver.find_element(*ScooterOrderPageLocators.order_name).send_keys(name)

    def send_surname(self, surname):
        self.driver.find_element(*ScooterOrderPageLocators.order_surname).send_keys(surname)

    def send_adress(self, adress):
        self.driver.find_element(*ScooterOrderPageLocators.order_adress).send_keys(adress)

    def send_metro_station(self, metro_station):
        self.driver.find_element(*ScooterOrderPageLocators.order_metro_station).send_keys(metro_station)
        self.driver.find_element(*ScooterOrderPageLocators.order_metro_station_choice).click()

    def send_phone(self, phone):
        self.driver.find_element(*ScooterOrderPageLocators.order_phone).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*ScooterOrderPageLocators.next_button).click()

    def set_order_page_scenario_1(self, name, surname, adress, metro_station, phone):
        BasePage.wait_for_load_home_page(self)  
        BasePage.click_order_button_top(self)
        self.wait_for_load_order_page()
        self.send_name(name)
        self.send_surname(surname)
        self.send_adress(adress)
        self.send_metro_station(metro_station)
        self.send_phone(phone)
        self.click_next_button()

    def set_order_page_scenario_2(self, name, surname, adress, metro_station, phone):
        BasePage.wait_for_load_home_page(self)        
        self.scroll_to_bottom_button()        
        self.click_order_bottom_button()        
        self.wait_for_load_order_page()        
        self.send_name(name)
        self.send_surname(surname)
        self.send_adress(adress)
        self.send_metro_station(metro_station)
        self.send_phone(phone)
        self.click_next_button()    