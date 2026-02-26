from selenium.webdriver.common.by import By

class BasePageLocators:
    home_title_img = [By.XPATH, '//img[@src="/assets/scooter.png"]'] 
    order_button_top = [By.CLASS_NAME, "Button_Button__ra12g"] 
    scooter_button = [By.XPATH, '//img[@src="/assets/scooter.svg"]']
    yandex_button = [By.XPATH, '//img[@src="/assets/ya.svg"]']

    