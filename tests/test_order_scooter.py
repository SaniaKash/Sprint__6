import pytest
from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_locator import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from input_data import User1, User2

class TestOrderScooter:


    def test_user_scooter_order_success(self, driver):
        user = MainPage(driver)
        user.open_main_page()
        user.click_header_order_but()
        user = OrderPage(driver)
        user.wait_for_name_field_to_load()
        user.input_order_page_fields(User1.text_name, User1.text_surname, User1.text_address, User1.text_metro, User1.text_metro)
        user.click_but_next()
        user = RentPage(driver)
        user.wait_for_date_field_to_load()
        user.rent_page_fields_input(User1.text_date, User1.locator_rent_date_2_days, User1.locator_color_black)
        user.click_order_but_rent_page()
        user.click_yes_but_order_rent_page()
        assert user.success_order_message_displayed()

        user.click_status_but()
        user = MainPage(driver)
        user.click_scooter_logo()
