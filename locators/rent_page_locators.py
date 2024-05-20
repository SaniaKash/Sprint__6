
from selenium.webdriver.common.by import By


class RentPageLocators:
    # Локатор даты доставки
    DATE_FIELD = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    # Локатор стрелочки выпадающего списка "Срока аренды"
    RENT_TIME_FIELD = By.CLASS_NAME, 'Dropdown-arrow'
    # Локатор времени: 2 суток выпадающего списка "Срока аренды"
    RENT_TIME_FIELD_2_DAYS = By.XPATH, "//*[@class='Dropdown-menu']/*[text()='двое суток']"
    # Локатор времени: 3 суток выпадающего списка "Срока аренды"
    RENT_TIME_FIELD_3_DAYS = By.XPATH, "//*[@class='Dropdown-menu']/*[text()='трое суток']"
    # Локатор цвета самоката "черный"
    COLOR_FIELD_BLACK = By.ID, 'black'
    # Локатор цвета самоката "серый"
    COLOR_FIELD_GREY = By.ID, 'grey'
    # Локатор кнопки заказать в поле аренды
    ORDER_BUT_MIDDLE = By.XPATH, "//*[contains(@class,'Order_Buttons')]/*[text()='Заказать']"
    # Локатор кнопки "да" при подтверждении заказа
    YES_BUT = By.XPATH, "//*[text()='Да']"
    # Локатор сообщения "Заказ оформлен"
    COMPLETE_ORDER_MESSAGE = By.XPATH, "//*[text()='Заказ оформлен']"
    # Локатор кнопки "Посмотреть статус"
    STATUS_BUT = By.XPATH, "//button[text()='Посмотреть статус']"
