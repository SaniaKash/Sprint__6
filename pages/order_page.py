from selenium import webdriver
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from conftest import driver
from selenium.webdriver.chrome.webdriver import WebDriver


class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_name_field_to_load(self):
        self.wait_for_element_visible(*OrderPageLocators.NAME_FIELD)

    def input_name(self, text_name):
        self.input_text(*OrderPageLocators.NAME_FIELD, text_name)

    def input_surname(self, text_surname):
        self.input_text(*OrderPageLocators.SURNAME_FIELD, text_surname)

    def input_address(self, text_address):
        self.input_text(*OrderPageLocators.ADDRESS_FIELD, text_address)

    def input_metro_station(self, text_metro):
        self.input_text(*OrderPageLocators.METRO_STATION, text_metro)

    def input_tel_num(self, text_tel):
        self.input_text(*OrderPageLocators.TEL_NUM_FIELD, text_tel)

    def input_order_page_fields(self, text_name, text_surname, text_address, text_metro, text_tel):
        self.input_name(text_name)
        self.input_surname(text_surname)
        self.input_address(text_address)
        self.input_metro_station(text_metro)
        self.input_tel_num(text_tel)

    def click_but_next(self):
        self.click_element(*OrderPageLocators.NEXT_BUT)
