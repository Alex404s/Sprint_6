from ..locators.home_page_locators import HomePageLocators
from ..locators.base_page_locators import BasePageLocators
from .base_page import BasePage
import allure


class ImportantQuestions(BasePage):

    @allure.step('Нажатие кнопки "Яндекс"')
    def click_yandex_button(self):
        super().click_button(BasePageLocators.yandex_button)

    @allure.step('Ожидание прогрузки страницы Дзен')
    def wait_for_load_dzen(self):
        super().wait_for_load_element(BasePageLocators.yandex_dzen)

    @allure.step('Переход и нажатие по пункту выпадающего списка в разделе «Вопросы о важном»')
    def check_important_questions_list(self, question, question_answer):    
        super().wait_for_load_element(BasePageLocators.home_title_img)        
        super().scroll_to_element(HomePageLocators.important_questions_list)
        super().wait_for_clickable_element(question)
        super().click_button(question)        
        super().wait_for_load_element(question_answer)

