from selenium import webdriver
import pytest
from ..pages.scooter_order_page import ScooterOrderPage
from ..pages.rent_list_page import RentListPage
from ..pages.base_page import BasePage
from ..locators.scooter_order_page_locators import ScooterOrderPageLocators
from ..locators.rent_list_page_locators import RentListPageLocators
from ..locators.base_page_locators import BasePageLocators
from ..data import UserData
import time

class TestMakingOrder2:

    driver = None
      
    @classmethod
    def setup_class(cls):        
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    def test_making_order_success_scenario_2(self):
        order_page_2 = ScooterOrderPage(self.driver)
        order_page_2.set_order_page_scenario_2(
                                  UserData.user_2_info['name'] , 
                                  UserData.user_2_info['surname'],
                                  UserData.user_2_info['adress'],
                                  UserData.user_2_info['metro_station'],
                                  UserData.user_2_info['phone'])
        
        rent_page_2 = RentListPage(self.driver)
        rent_page_2.making_an_order_scenario_2(
                                  UserData.user_2_info['rent_date'],
                                  UserData.user_2_info['rent_comment'])
        
        check_success_order = rent_page_2.get_text_success_field()        

        assert check_success_order == 'Номер заказа: .  Запишите его:\nпригодится, чтобы отслеживать статус'

        rent_page_2.wait_for_load_success_field()
        rent_page_2.click_look_status()        

        home_page = BasePage(self.driver)        
        home_page.click_scooter_button()
        home_page.wait_for_load_home_page()
        current_url = self.driver.current_url      
        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 