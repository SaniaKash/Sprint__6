import pytest
from conftest import driver
from pages.main_page import MainPage
from locators.main_page_locator import QuestionResponse


class TestQuestionResponse:

    @pytest.mark.parametrize('locator_question , locator_response',
                             zip(QuestionResponse.QUESTION_LOCATORS, QuestionResponse.RESPONSE_LOCATORS))
    def test_click_question_check_response(self, driver, locator_question, locator_response):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.submit_cookie()
        main_page.scroll_to_question(locator_question)
        main_page.click_question(locator_question)
        assert main_page.check_open_right_response_displayed(locator_response)
