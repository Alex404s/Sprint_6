from ..locators.rent_list_page_locators import RentListPageLocators
from ..locators.base_page_locators import BasePageLocators
from .base_page import BasePage
import allure


class RentListPage(BasePage):    

    @allure.step('Выбор срока аренды: один день')
    def choose_period_day(self):
        super().click_button(RentListPageLocators.rent_period)
        super().click_button(RentListPageLocators.rent_period_day)

    @allure.step('Выбор срока аренды: два дня')
    def choose_period_two_days(self):
        super().click_button(RentListPageLocators.rent_period)
        super().click_button(RentListPageLocators.rent_period_two_days)

    @allure.step('Выбор серого самоката')
    def choose_grey_scooter(self):
        super().click_button(RentListPageLocators.rent_scooter_grey)
    
    @allure.step('Выбор черного самоката')
    def choose_black_scooter(self):
        super().click_button(RentListPageLocators.rent_scooter_black)
    
    @allure.step('Комментарий')
    def send_comment(self, comment):
        super().send_keys_to_element(RentListPageLocators.rent_comment, comment)

    @allure.step('Нажать "Заказать"')
    def click_rent_order_button(self):
        super().click_button(RentListPageLocators.rent_order_button)   

    @allure.step('Подтверждение заказа')
    def accept_order(self):
        super().click_button(RentListPageLocators.order_accept_button)

    @allure.step('Получение текста успешного заказа')
    def get_text_success_order(self):
        text = super().get_text_element(RentListPageLocators.order_success_field)
        return text 
    
    @allure.step('Нажатие кнопки "Посмотреть статус"')
    def click_status_button(self):
        super().click_button(RentListPageLocators.look_status_button)               
    
    @allure.step('Нажатие кнопки "Самокат"')
    def click_scooter_button(self):
        super().click_button(BasePageLocators.scooter_button)
    
    @allure.step('Ожидание прогрузки домашней страницы')
    def wait_for_load_home_page(self):
        super().wait_for_load_element(BasePageLocators.home_title_img)


    @allure.step('Первый сценарий оформления аренды и дальнейшего заказа')
    def making_an_order_scenario_1(self, date, comment):        
        super().wait_for_load_element(RentListPageLocators.rent_field)      
        super().send_keys_to_element(RentListPageLocators.rent_date, date)        
        self.choose_period_day()        
        self.choose_grey_scooter()        
        self.send_comment(comment)        
        self.click_rent_order_button()        
        super().wait_for_load_element(RentListPageLocators.order_accept_field)       
        self.accept_order()        
        super().wait_for_load_element(RentListPageLocators.order_success_field)              

    @allure.step('Второй сценарий оформления аренды и дальнейшего заказа')
    def making_an_order_scenario_2(self, date, comment):
        super().wait_for_load_element(RentListPageLocators.rent_field)
        super().send_keys_to_element(RentListPageLocators.rent_date, date)
        self.choose_period_two_days()
        self.choose_black_scooter()
        self.send_comment(comment)
        self.click_rent_order_button()
        super().wait_for_load_element(RentListPageLocators.order_accept_field)
        self.accept_order()
        super().wait_for_load_element(RentListPageLocators.order_success_field)
        
         