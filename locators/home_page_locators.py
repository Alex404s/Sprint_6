from selenium.webdriver.common.by import By

class HomePageLocators:
    important_questions_list = [By.CLASS_NAME, "Home_FourPart__1uthg"]
    how_much_how_pay = [By.XPATH, '//div[text()= "Сколько это стоит? И как оплатить?"]']
    how_much_how_pay_answer = [By.ID, "accordion__panel-0"]
    many_scooters = [By.XPATH, '//div[text()= "Хочу сразу несколько самокатов! Так можно?"]']
    many_scooters_answer = [By.ID, "accordion__panel-1"]
    rent_time = [By.XPATH, '//div[text()= "Как рассчитывается время аренды?"]']
    rent_time_answer = [By.ID, "accordion__panel-2"]
    scooter_today = [By.XPATH, '//div[text()= "Можно ли заказать самокат прямо на сегодня?"]']
    scooter_today_answer = [By.ID, "accordion__panel-3"]
    rent_set = [By.XPATH, '//div[text()= "Можно ли продлить заказ или вернуть самокат раньше?"]']
    rent_set_answer = [By.ID, "accordion__panel-4"]
    scooter_charge = [By.XPATH, '//div[text()= "Вы привозите зарядку вместе с самокатом?"]']
    scooter_charge_answer = [By.ID, "accordion__panel-5"]
    cancellation = [By.XPATH, '//div[text()= "Можно ли отменить заказ?"]']
    cancellation_answer = [By.ID, "accordion__panel-6"]
    mordor_habitation = [By.XPATH, '//div[text()= "Я жизу за МКАДом, привезёте?"]']
    mordor_habitation_answer = [By.ID, "accordion__panel-7"]
    