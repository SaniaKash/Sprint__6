from pages.base_page import BasePage
from locators.rent_page_locators import RentPageLocators
from conftest import driver



class RentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_date_field_to_load(self):
        self.wait_for_element_visible(*RentPageLocators.DATE_FIELD)

    def input_date(self, text_date):
        self.input_text(*RentPageLocators.DATE_FIELD, text_date)

    def click_rent_date_field(self):
        self.click_element(*RentPageLocators.DATE_FIELD)

    def submit_rent_date(self, locator_rent_date):
        self.click_element(locator_rent_date)

    def select_color(self, locator_color):
        self.click_element(locator_color)

    def rent_page_fields_input(self, text_date, locator_rent_date, locator_color):
        self.input_date(text_date)
        self.click_rent_date_field()
        self.submit_rent_date(*locator_rent_date)
        self.select_color(*locator_color)

    def click_order_but_rent_page(self):
        self.click_element(*RentPageLocators.ORDER_BUT_MIDDLE)

    def click_yes_but_order_rent_page(self):
        self.click_element(*RentPageLocators.YES_BUT)

    def success_order_message_displayed(self):
        element = self.find_element(*RentPageLocators.COMPLETE_ORDER_WINDOW)
        return element.is_displayed()

    def click_status_but(self):
        self.click_element(*RentPageLocators.STATUS_BUT)
