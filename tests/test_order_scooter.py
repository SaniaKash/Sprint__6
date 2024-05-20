import allure
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from input_data import User1, User2


class TestOrderScooter:

    @allure.title('Проверка позитивного сценария заказа самоката User2')
    @allure.description("Открываем страницу 'ЯндексСамокат'.Нажимаем кнопку заказать в хедере страницы 'Яндекс "
                        "Самокат'. Заполняем все поля в формах"
                        "'Для кого самокат' , 'Про аренду' и подтверждаем заказ. Делаем проверку появления "
                        "сообщения об успешном оформлении заказа.")
    def test_user_1_header_order_but_scooter_order_success(self, driver):
        user = MainPage(driver)
        user.open_main_page()
        user.click_header_order_but()
        user = OrderPage(driver)
        user.input_order_page_fields(User1.text_name, User1.text_surname, User1.text_address, User1.text_metro,
                                     User1.text_tel)
        user.click_but_next()
        user = RentPage(driver)
        user.rent_page_fields_input(User1.text_date, User1.locator_rent_date_2_days, User1.locator_color_black)
        user.click_order_but_rent_page()
        user.click_yes_but_order_rent_page()
        assert user.check_success_message_displayed()

    @allure.title('Проверка позитивного сценария заказа самоката с данными User2')
    @allure.description("Открываем страницу 'ЯндексСамокат'.Нажимаем кнопку заказать в середине страницы 'Яндекс "
                        "Самокат'. Заполняем все поля в формах"
                        "'Для кого самокат' , 'Про аренду' и подтверждаем заказ. Делаем проверку появления "
                        "сообщения об успешном оформлении заказа.")
    def test_user_2_home_order_but_scooter_order_success(self, driver):
        user = MainPage(driver)
        user.open_main_page()
        user.scroll_to_home_order_but()
        user.click_home_order_but()
        user = OrderPage(driver)
        user.input_order_page_fields(User2.text_name, User2.text_surname, User2.text_address, User2.text_metro,
                                     User2.text_tel)
        user.click_but_next()
        user = RentPage(driver)
        user.rent_page_fields_input(User2.text_date, User2.locator_rent_date_3_days, User2.locator_color_grey)
        user.click_order_but_rent_page()
        user.click_yes_but_order_rent_page()
        assert user.check_success_message_displayed()
