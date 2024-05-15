from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'
    ORDER_BUT_HEADER = By.XPATH, '//*[contains(@class,"Header")]/*[text()="Заказать"]'
    ORDER_BUT_HOME = By.XPATH, '//*[contains(@class,"Home")]/*[text()="Заказать"]'
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"
    DZEN_LOGO = By.XPATH, "//*[@alt='Yandex']"


class QuestionResponse:

    questions_locators = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    response_locators = [
        (By.XPATH, '//*[@id="accordion__panel-0"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-1"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-2"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-3"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-4"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-5"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-8"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-7"]/p')
    ]

