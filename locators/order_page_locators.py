from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Локатор поля "Имя"
    NAME_FIELD = By.XPATH, "//*[@placeholder='* Имя']"
    # Локатор поля "Фамилия"
    SURNAME_FIELD = By.XPATH, "//*[@placeholder='* Фамилия']"
    # Локатор поля "Адрес"
    ADDRESS_FIELD = By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"
    # Локатор поля станции метро"
    METRO_STATION_FIELD = By.XPATH, "//*[@placeholder='* Станция метро']"
    # Локатор значения "Черкизовская" поля метро
    METRO_STATION_1 = By.XPATH, "//*[contains(@class,'Order_SelectOption')]/*[text()='Черкизовская']"
    # Локатор значения "Сокольники" поля метро
    METRO_STATION_2 = By.XPATH, "//*[contains(@class,'Order_SelectOption')]/*[text()='Сокольники']"
    # Локатор поля "Номер телефона"
    TEL_NUM_FIELD = By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"
    # Локатор кнопки "Далее"
    NEXT_BUT = By.XPATH, "//*[text()='Далее']"
