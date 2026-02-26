from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.rent_list_page_locators import RentListPageLocators
from .base_page import BasePage
import time
from ..data import UserData

class RentListPage:
    def __init__(self, driver):
        self.driver = driver   

    def wait_for_load_rent_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(RentListPageLocators.rent_field))

    def choose_rent_date(self, date):
        self.driver.find_element(*RentListPageLocators.rent_date).send_keys(date)

    def choose_period_day(self):
        self.driver.find_element(*RentListPageLocators.rent_period).click()
        self.driver.find_element(*RentListPageLocators.rent_period_day).click()

    def choose_period_two_days(self):
        self.driver.find_element(*RentListPageLocators.rent_period).click()
        self.driver.find_element(*RentListPageLocators.rent_period_two_days).click()

    def choose_grey_scooter(self):
        self.driver.find_element(*RentListPageLocators.rent_scooter_grey).click()
    
    def choose_black_scooter(self):
        self.driver.find_element(*RentListPageLocators.rent_scooter_black).click()
    
    def send_comment(self, comment):
        self.driver.find_element(*RentListPageLocators.rent_comment).send_keys(comment)

    def click_rent_order_button(self):
        self.driver.find_element(*RentListPageLocators.rent_order_button).click()

    def wait_for_load_accept_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(RentListPageLocators.order_accept_field))

    def accept_order(self):
        self.driver.find_element(*RentListPageLocators.order_accept_button).click()

    def wait_for_load_success_field(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(RentListPageLocators.order_success_field))

    def get_text_success_field(self):
        text_success_field = self.driver.find_element(*RentListPageLocators.order_success_field).text
        return text_success_field    
    
    def click_look_status(self):
        self.driver.find_element(*RentListPageLocators.look_status_button).click()
    
    def wait_for_load_order_status(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(RentListPageLocators.cancel_order))

    def making_an_order_scenario_1(self, date, comment):        
        self.wait_for_load_rent_page()        
        self.choose_rent_date(date)        
        self.choose_period_day()        
        self.choose_grey_scooter()        
        self.send_comment(comment)        
        self.click_rent_order_button()        
        self.wait_for_load_accept_page()        
        self.accept_order()        
        self.wait_for_load_success_field()              

    def making_an_order_scenario_2(self, date, comment):
        self.wait_for_load_rent_page()
        self.choose_rent_date(date)
        self.choose_period_two_days()
        self.choose_black_scooter()
        self.send_comment(comment)
        self.click_rent_order_button()
        self.wait_for_load_accept_page()
        self.accept_order()
        self.wait_for_load_success_field()
        self.get_text_success_field()
        print 