from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ..locators.home_page_locators import HomePageLocators
from .base_page import BasePage


class ImportantQuestions:
    how_much_how_pay_answer_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    many_scooters_answer_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    rent_time_answer_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    scooter_today_answer_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    rent_set_answer_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    scooter_charge_answer_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    cancellation_answer_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    mordor_habitation_answer_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_important_questions_list(self):
        questions_list = self.driver.find_element(*HomePageLocators.important_questions_list)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_list)

    def click_to_question_button(self, question):
        self.driver.find_element(*question).click()

    def wait_for_load_answer_text(self, question_answer):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(question_answer))

    def text_question_answer(self, question_answer):
        text_question_answer = self.driver.find_element(*question_answer).text
        return text_question_answer
    
    def check_important_questions_list(self, question, question_answer):    
        BasePage.wait_for_load_home_page(self)        
        self.scroll_to_important_questions_list()
        self.click_to_question_button(question)
        self.wait_for_load_answer_text(question_answer)
        self.text_question_answer(question_answer)
        return self.text_question_answer













