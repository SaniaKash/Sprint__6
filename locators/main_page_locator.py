from selenium.webdriver.common.by import By


class MainPageLocators:
    # URL страницы Яндекс Самокат
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    # URL страницы Дзен
    DZEN_URL = 'https://dzen.ru/?yredirect=true'

    # Локатор кнопки "Заказать" в хедере
    ORDER_BUT_HEADER = By.XPATH, '//*[contains(@class,"Header")]/*[text()="Заказать"]'
    # Локатор кнопки "Заказать" в середине страницы
    ORDER_BUT_HOME = By.XPATH, '//*[contains(@class,"Home")]/*[text()="Заказать"]'
    # Локатор гипперссылки "Самокат"
    SCOOTER_LOGO = By.XPATH, "//*[@alt='Scooter']"
    # Локатор гипперссылки "Яндекс"
    YANDEX_LOGO = By.XPATH, "//*[@alt='Yandex']"
    # Локатор кнопки куки "Да все к этому привыкли"
    COOKIE_BUT = By.ID, 'rcc-confirm-button'


class QuestionResponse:
    # Локаторы "Вопросы о важном"
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    # Локаторы ответов на вопросы
    RESPONSE_LOCATORS = [
        (By.XPATH, '//*[@id="accordion__panel-0"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-1"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-2"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-3"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-4"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-5"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-6"]/p'),
        (By.XPATH, '//*[@id="accordion__panel-7"]/p')
    ]

