from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.XPATH, "//*[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//*[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//*[@placeholder='* Станция метро']")
    TEL_NUM_FIELD = (By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUT = (By.XPATH, "//*[text()='Далее']")
