import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators
from conftest import driver


class MainPage(BasePage):

    @allure.step('Открываем браузер Chrome')
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Переходим на страницу ЯндексСамокат')
    def open_main_page(self):
        self.navigation(MainPageLocators.MAIN_PAGE_URL)

    @allure.step('Кликаем кнопку "Заказать" на хедере страницы')
    def click_header_order_but(self):
        self.click_element(MainPageLocators.ORDER_BUT_HEADER)

    @allure.step('Кликаем кнопку "Заказать" в центре страницы страницы')
    def click_home_order_but(self):
        self.click_element(MainPageLocators.ORDER_BUT_HOME)

    @allure.step('Скроллим страницу до кнопки заказать')
    def scroll_to_home_order_but(self):
        self.execute_script(MainPageLocators.ORDER_BUT_HOME)

    @allure.step('Принимаем cookie сообщение')
    def submit_cookie(self):
        self.click_element(MainPageLocators.COOKIE_BUT)

    @allure.step('Скроллим страницу до локатора вопроса')
    def scroll_to_question(self, locator_question):
        self.execute_script(locator_question)

    @allure.step('Кликаем вопрос')
    def click_question(self, locator_question):
        self.click_element(locator_question)

    @allure.step('Проверяем отображение ответа на соответствующий локатор вопроса')
    def check_open_right_response_displayed(self, locator_response):
        return self.visibility_of_element_located(locator_response).is_displayed()

    @allure.step('Кликаем гиперссылку "Самокат" в хедере')
    def click_scooter_logo(self):
        return self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Проверяем текущий url страницы')
    def check_yandex_scooter_url(self):
        return self.driver.current_url

    @allure.step('Кликаем гиперссылку "Яндекс" в хедере')
    def click_yandex_logo(self):
        return self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверяем открытие страницы Дзен')
    def check_open_dzen_url(self):
        return self.driver.current_url

    @allure.step('Переходим на открытую страницу Дзен')
    def switch_to_dzen_tab(self):
        return self.switch_to_the_new_tab()

    def wait_until_DZEN_link_ready(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(MainPageLocators.DZEN_URL))





