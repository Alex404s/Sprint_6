from ..pages.home_page import ImportantQuestions
from selenium import webdriver
import pytest
from ..locators.home_page_locators import HomePageLocators
import allure


class TestImportantQuestions:

    driver = None

    
    @classmethod
    def setup_class(cls):        
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")   



    
    @pytest.mark.parametrize('question, answer, text_answer', [
          [HomePageLocators.how_much_how_pay, HomePageLocators.how_much_how_pay_answer, ImportantQuestions.how_much_how_pay_answer_text],
          [HomePageLocators.many_scooters, HomePageLocators.many_scooters_answer, ImportantQuestions.many_scooters_answer_text],
          [HomePageLocators.rent_time, HomePageLocators.rent_time_answer, ImportantQuestions.rent_time_answer_text],
          [HomePageLocators.scooter_today, HomePageLocators.scooter_today_answer, ImportantQuestions.scooter_today_answer_text],
          [HomePageLocators.rent_set, HomePageLocators.rent_set_answer, ImportantQuestions.rent_set_answer_text],
          [HomePageLocators.scooter_charge, HomePageLocators.scooter_charge_answer, ImportantQuestions.scooter_charge_answer_text],
          [HomePageLocators.cancellation, HomePageLocators.cancellation_answer, ImportantQuestions.cancellation_answer_text],
          [HomePageLocators.mordor_habitation, HomePageLocators.mordor_habitation_answer, ImportantQuestions.mordor_habitation_answer_text]])
    def test_description(self, question, answer, text_answer):
        important_questions = ImportantQuestions(self.driver)
        important_questions.check_important_questions_list(question, answer)
        check_answer = important_questions.text_question_answer(answer)

        assert check_answer == text_answer

    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 