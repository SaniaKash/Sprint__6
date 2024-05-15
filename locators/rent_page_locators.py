
from selenium.webdriver.common.by import By


class RentPageLocators:
    DATE_FIELD = (By.XPATH, "//*[@placeholder='* Когда привезти самокат']")
    RENT_TIME_FIELD = (By.XPATH, "//*[text()='* Срок аренды']")
    RENT_TIME_FIELD_2_DAYS = (By.XPATH, "//*[@class='Dropdown-menu']/*[text()='двое суток']")
    RENT_TIME_FIELD_3_DAYS = (By.XPATH, "//*[@class='Dropdown-menu']/*[text()='трое суток']")
    COLOR_FIELD_BLACK = (By.ID, 'black')
    COLOR_FIELD_GREY = (By.ID, 'grey')
    ORDER_BUT_MIDDLE = (By.XPATH, "//*[contains(@class,'Order_Buttons')]/*[text()='Заказать']")
    YES_BUT = (By.XPATH, "//*[text()='Да']")
    COMPLETE_ORDER_WINDOW = (By.XPATH, "//*[contains(@class,'Order_ModalHeader')]")
    STATUS_BUT = (By.XPATH, "//button[text()='Посмотреть статус']")
