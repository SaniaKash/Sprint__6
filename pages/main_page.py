


from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators



class MainPage(BasePage):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def scooter_main_page(self):
    #    return driver.current_url

    def open_main_page(self):
        self.navigation(MainPageLocators.MAIN_PAGE_URL)

    def click_header_order_but(self):
        self.click_element(MainPageLocators.ORDER_BUT_HEADER)

    def scroll_to_question(self, locator_question):
        self.execute_script(locator_question)

    def click_question(self, locator_question):
        self.click_element(locator_question)

    def check_open_right_response(self, locator_response):
        response = self.driver.find_element(locator_response).text
        assert response

    def click_scooter_logo(self):
        element = self.driver.find_element(*MainPageLocators.SCOOTER_LOGO)
        return element.click()


