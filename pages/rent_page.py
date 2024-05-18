import allure
from locators.rent_page_locators import RentPageLocators
from conftest import driver
from pages.base_page import BasePage


class RentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим дату доставки')
    def input_date(self, text_date):
        self.input_text(RentPageLocators.DATE_FIELD, text_date)

    @allure.step('Кликакем на поле "Срок аренды"')
    def click_rent_date_field(self):
        self.click_element(RentPageLocators.RENT_TIME_FIELD)

    @allure.step('Кликакем на количество суток выпадающего списка "Срок аренды"')
    def click_rent_date(self, locator_rent_date):
        self.click_element(locator_rent_date)

    @allure.step('Кликакем на чекбокс поля "Цвет самоката" ')
    def select_color(self, locator_color):
        self.click_element(locator_color)

    @allure.step('Заполняем поля формы "Про аренду"')
    def rent_page_fields_input(self, text_date, locator_rent_date, locator_color):
        self.input_date(text_date)
        self.click_rent_date_field()
        self.click_rent_date(locator_rent_date)
        self.select_color(locator_color)

    @allure.step('Кликакем на кнопку заказать в форме "Про аренду"')
    def click_order_but_rent_page(self):
        self.click_element(RentPageLocators.ORDER_BUT_MIDDLE)

    @allure.step('Кликакем на кнопку "Да" сообщения о подтверждения')
    def click_yes_but_order_rent_page(self):
        self.click_element(RentPageLocators.YES_BUT)

    @allure.step('проверяем отображение сообщения "Заказ оформлен"')
    def check_success_message_displayed(self):
        return self.visibility_of_element_located(RentPageLocators.COMPLETE_ORDER_MESSAGE).is_displayed()

    @allure.step('Кликаем на кнопку "Проверить статус заказа"')
    def click_status_but(self):
        self.click_element(RentPageLocators.STATUS_BUT)



