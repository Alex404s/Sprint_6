import pytest
from ..pages.scooter_order_page import ScooterOrderPage
from ..pages.rent_list_page import RentListPage
from ..locators.rent_list_page_locators import RentListPageLocators
from ..locators.base_page_locators import BasePageLocators
from ..data import UserData
from ..pages.home_page import ImportantQuestions
import allure

class TestMakingOrder2:

    @allure.title('Проверка второго сценария успешного оформления заказа и перехода на главную страницу через кнопку "Самокат"')
    def test_making_order_success_scenario_2(self, driver):
        order_page = ScooterOrderPage(driver)
        order_page.set_order_page_scenario_2(
                                  UserData.user_2_info['name'] , 
                                  UserData.user_2_info['surname'],
                                  UserData.user_2_info['adress'],
                                  UserData.user_2_info['metro_station'],
                                  UserData.user_2_info['phone'])
        
        rent_page = RentListPage(driver)
        rent_page.making_an_order_scenario_2(
                                  UserData.user_2_info['rent_date'],
                                  UserData.user_2_info['rent_comment'])
        
        rent_page.wait_for_load_element(RentListPageLocators.order_success_field)
        check_success_order = rent_page.get_text_element(RentListPageLocators.order_success_field)

        assert 'Заказ оформлен' in check_success_order    
          
        rent_page.click_button(RentListPageLocators.look_status_button)               
        rent_page.click_button(BasePageLocators.scooter_button)
        rent_page.wait_for_load_element(BasePageLocators.home_title_img)
        current_url = rent_page.get_url()     

        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка перехода на "https://dzen.ru/?yredirect=true"')
    def test_yandex_button_dzen_url(self,driver):
        yandex_button = ImportantQuestions(driver)
        yandex_button.click_button(BasePageLocators.yandex_button)       
        driver.switch_to.window(driver.window_handles[-1])
        yandex_button.wait_for_load_element(BasePageLocators.yandex_dzen)
        current_url = yandex_button.get_url()   

        assert current_url == 'https://dzen.ru/?yredirect=true'