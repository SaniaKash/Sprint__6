import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.chrome.webdriver import WebDriver


class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Вводим имя')
    def input_name(self, text_name):
        self.input_text(OrderPageLocators.NAME_FIELD, text_name)

    @allure.step('Вводим фамилию')
    def input_surname(self, text_surname):
        self.input_text(OrderPageLocators.SURNAME_FIELD, text_surname)

    @allure.step('Вводим адрес')
    def input_address(self, text_address):
        self.input_text(OrderPageLocators.ADDRESS_FIELD, text_address)

    @allure.step('Кликаем на поле ввода станции метро')
    def click_metro_field(self):
        self.click_element(OrderPageLocators.METRO_STATION_FIELD)

    @allure.step('Кликаем станцию метро из выпадающего списка')
    def click_metro_station(self, locator):
        self.click_element(locator)

    @allure.step('Вводим номер телефона')
    def input_tel_num(self, text_tel):
        self.input_text(OrderPageLocators.TEL_NUM_FIELD, text_tel)

    @allure.step('Вводим данные в форму аренды самоката')
    def input_order_page_fields(self, text_name, text_surname, text_address, locator, text_tel):
        self.input_name(text_name)
        self.input_surname(text_surname)
        self.input_address(text_address)
        self.click_metro_field()
        self.click_metro_station(locator)
        self.input_tel_num(text_tel)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_but_next(self):
        self.click_element(OrderPageLocators.NEXT_BUT)
