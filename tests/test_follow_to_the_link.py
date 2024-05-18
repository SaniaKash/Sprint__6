import allure
from locators.main_page_locator import MainPageLocators
from conftest import driver
from pages.main_page import MainPage



class TestFollowToTheLink:

    @allure.title('Проверка перехода по гиперссылке "Самокат" с формы "Для кого самокат"')
    @allure.description("Открываем страницу 'ЯндексСамокат' и нажимаем кнопку 'Заказать'. Затем нажимаем на "
                        "гиперссылку 'Самокат' в хедере и"
                        "делаем проверку url адреса 'Яндекс Самокат'.")
    def test_click_scooter_link_open_main_page_success(self, driver):
        user = MainPage(driver)
        user.open_main_page()
        user.click_header_order_but()
        user.click_scooter_logo()
        assert user.check_yandex_scooter_url() == MainPageLocators.MAIN_PAGE_URL

    @allure.title('Проверка перехода по гиперссылке "Яндекс"')
    @allure.description("Открываем страницу 'ЯндексСамокат' , нажимаем на гиперссылку 'Яндекс' и делаем "
                        "проверку перехода на url Дзен")
    def test_click_yandex_link_open_dzen_page_success(self, driver):
        user = MainPage(driver)
        user.open_main_page()
        user.click_yandex_logo()
        user.switch_to_dzen_tab()
        user.wait_until_DZEN_link_ready()
        assert user.check_open_dzen_url() == MainPageLocators.DZEN_URL
