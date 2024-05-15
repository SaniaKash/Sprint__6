import pytest
from conftest import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from locators.main_page_locator import QuestionResponse
from locators.main_page_locator import MainPageLocators



class TestQuestionResponse:

    @pytest.mark.parametrize('locator_question , locator_response',
                             zip(QuestionResponse.questions_locators, QuestionResponse.response_locators))
    def test_click_question_check_response(self, driver, locator_question, locator_response):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_question(locator_question)
        main_page.click_question(locator_question)
        main_page.check_open_right_response(locator_response)
