from ..locators.scooter_order_page_locators import ScooterOrderPageLocators
from ..locators.base_page_locators import BasePageLocators
from .base_page import BasePage
import allure


class ScooterOrderPage(BasePage): 

    @allure.step('Прокрутка до нижней кнопки "Заказать"')
    def scroll_to_bottom_button(self):
        super().scroll_to_element(ScooterOrderPageLocators.order_button_bottom_field)

    @allure.step('Нажатие по нижней кнопке "Заказать"')
    def click_order_bottom_button(self):
        super().click_button(ScooterOrderPageLocators.order_button_bottom_field)

    @allure.step("Ожидание прогрузки страницы оформления заказа")
    def wait_for_load_order_page(self):
        super().wait_for_load_element(ScooterOrderPageLocators.order_field)
    
    @allure.step("Ввод имени")
    def send_name(self, name):
        super().send_keys_to_element(ScooterOrderPageLocators.order_name, name)

    @allure.step("Ввод фамилии")
    def send_surname(self, surname):
        super().send_keys_to_element(ScooterOrderPageLocators.order_surname, surname)

    @allure.step("Ввод адреса")
    def send_adress(self, adress):
        super().send_keys_to_element(ScooterOrderPageLocators.order_adress, adress)

    @allure.step("Выбор станции метро")
    def send_metro_station(self, metro_station):
        super().send_keys_to_element(ScooterOrderPageLocators.order_metro_station, metro_station)
        super().click_button(ScooterOrderPageLocators.order_metro_station_choice)

    @allure.step("Ввод номера телефона")
    def send_phone(self, phone):
        super().send_keys_to_element(ScooterOrderPageLocators.order_phone, phone)

    @allure.step("Нажатие кнопки Далее")
    def click_next_button(self):
        super().click_button(ScooterOrderPageLocators.next_button)

    @allure.step("Первый сценарий перехода и заполения формы заказа")
    def set_order_page_scenario_1(self, name, surname, adress, metro_station, phone):        
        super().wait_for_load_element(BasePageLocators.order_button_top)  
        super().click_button(BasePageLocators.order_button_top)
        self.wait_for_load_order_page()
        self.send_name(name)
        self.send_surname(surname)
        self.send_adress(adress)
        self.send_metro_station(metro_station)
        self.send_phone(phone)
        self.click_next_button()

    @allure.step("Второй сценарий перехода и заполения формы заказа")
    def set_order_page_scenario_2(self, name, surname, adress, metro_station, phone):
        super().wait_for_load_element(BasePageLocators.home_title_img)        
        self.scroll_to_bottom_button()        
        self.click_order_bottom_button()        
        self.wait_for_load_order_page()        
        self.send_name(name)
        self.send_surname(surname)
        self.send_adress(adress)
        self.send_metro_station(metro_station)
        self.send_phone(phone)
        self.click_next_button()    