from ..pages.home_page import ImportantQuestions
import pytest
from ..locators.home_page_locators import HomePageLocators
import allure
from ..data import AnswerText


class TestImportantQuestions:
    
    @allure.title('Тестирование пункта выпадающего списка "Вопросы о важном": {question}')
    @pytest.mark.parametrize('question, answer, text_answer', [
          [HomePageLocators.how_much_how_pay, HomePageLocators.how_much_how_pay_answer, AnswerText.how_much_how_pay_answer_text],
          [HomePageLocators.many_scooters, HomePageLocators.many_scooters_answer, AnswerText.many_scooters_answer_text],
          [HomePageLocators.rent_time, HomePageLocators.rent_time_answer, AnswerText.rent_time_answer_text],
          [HomePageLocators.scooter_today, HomePageLocators.scooter_today_answer, AnswerText.scooter_today_answer_text],
          [HomePageLocators.rent_set, HomePageLocators.rent_set_answer, AnswerText.rent_set_answer_text],
          [HomePageLocators.scooter_charge, HomePageLocators.scooter_charge_answer, AnswerText.scooter_charge_answer_text],
          [HomePageLocators.cancellation, HomePageLocators.cancellation_answer, AnswerText.cancellation_answer_text],
          [HomePageLocators.mordor_habitation, HomePageLocators.mordor_habitation_answer, AnswerText.mordor_habitation_answer_text]])
    def test_description(self, question, answer, text_answer, driver):
        important_questions = ImportantQuestions(driver)
        important_questions.check_important_questions_list(question, answer)
        check_answer = important_questions.get_text_element(answer)

        assert check_answer == text_answer

    
