import pytest
from ..pages.scooter_order_page import ScooterOrderPage
from ..pages.rent_list_page import RentListPage
from ..data import UserData
from ..pages.home_page import ImportantQuestions
import allure

class TestMakingOrder1:
    @allure.title('Проверка первого сценария успешного оформления заказа и перехода на главную страницу через кнопку "Самокат"')
    def test_making_order_success_scenario_1(self, driver):
        order_page = ScooterOrderPage(driver)
        order_page.set_order_page_scenario_1(
                                  UserData.user_1_info['name'] , 
                                  UserData.user_1_info['surname'],
                                  UserData.user_1_info['adress'],
                                  UserData.user_1_info['metro_station'],
                                  UserData.user_1_info['phone'])
        
        rent_page = RentListPage(driver)
        rent_page.making_an_order_scenario_1(
                                  UserData.user_1_info['rent_date'],
                                  UserData.user_1_info['rent_comment'])        
    
        check_success_order = rent_page.get_text_success_order()

        assert 'Заказ оформлен' in check_success_order     
           
        rent_page.click_status_button()               
        rent_page.click_scooter_button()
        rent_page.wait_for_load_home_page()
        current_url = rent_page.get_url()     

        assert current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка перехода на "https://dzen.ru/?yredirect=true"')
    def test_yandex_button_dzen_url(self,driver):
        yandex_button = ImportantQuestions(driver)
        yandex_button.click_yandex_button()       
        yandex_button.switch_window()
        yandex_button.wait_for_load_dzen()
        current_url = yandex_button.get_url()   

        assert current_url == 'https://dzen.ru/?yredirect=true'




      


   

   
    