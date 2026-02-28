from selenium.webdriver.common.by import By

class RentListPageLocators:
    rent_field = [By.CLASS_NAME, "Order_Content__bmtHS"]
    rent_date = [By.XPATH, '//input[@placeholder= "* Когда привезти самокат"]']
    rent_period = [By.XPATH, '//span[@class= "Dropdown-arrow"]']
    rent_period_day = [By.XPATH, '//div[text()= "сутки"]']
    rent_period_two_days = [By.XPATH, '//div[text()= "двое суток"]']
    rent_scooter_grey = [By.ID, "grey"]
    rent_scooter_black = [By.ID, "black"]
    rent_comment = [By.XPATH, '//input[@placeholder= "Комментарий для курьера"]']
    rent_order_button = [By.XPATH, '//div[@class= "Order_Buttons__1xGrp"]/button[text()= "Заказать"]']
    order_accept_field = [By.CLASS_NAME, "Order_Modal__YZ-d3"]
    order_accept_button = [By.XPATH, '//button[text()= "Да"]']
    order_success_field = [By.XPATH, '//div[text()= "Заказ оформлен"]']
    look_status_button = [By.XPATH, '//button[text()= "Посмотреть статус"]']
    
    
