from selenium.webdriver.common.by import By


class ScooterOrderPageLocators:
    order_button_bottom_field = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]']   
    order_field = [By.CLASS_NAME, "Order_Header__BZXOb"]
    order_name = [By.XPATH, '//input[@placeholder= "* Имя"]']
    order_surname = [By.XPATH, '//input[@placeholder= "* Фамилия"]']
    order_adress = [By.XPATH, '//input[@placeholder= "* Адрес: куда привезти заказ"]']
    order_metro_station = [By.XPATH, '//input[@placeholder= "* Станция метро"]']
    order_metro_station_choice = [By.CLASS_NAME, "select-search__select"]
    order_phone = [By.XPATH, '//input[@placeholder= "* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[text()= "Далее"]']
