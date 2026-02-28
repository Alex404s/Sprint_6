from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    @allure.step('Инициализация переменной')
    def __init__(self, driver):
        self.driver = driver 

    @allure.step('Ожидание отображения элемента')
    def wait_for_load_element(self, element_locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(element_locator))

    @allure.step('Клик по элементу')
    def click_button(self, button_locator):
        self.driver.find_element(*button_locator).click()

    @allure.step('Получение текста элемента')
    def get_text_element(self, element_locator):
        element_text = self.driver.find_element(*element_locator).text
        return element_text
    
    @allure.step('Прокрутка страницы до элемента')
    def scroll_to_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввод значения')
    def send_keys_to_element(self, element_locator, data):
        self.driver.find_element(*element_locator).send_keys(data)

    @allure.step('Получение URL текущей страницы')
    def get_url(self):
        current_url = self.driver.current_url
        return current_url
    
    @allure.step('Переключение на последнюю открытую страницу в браузере')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, element_locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(element_locator))



