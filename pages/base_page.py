from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Переход по ссылке
    def navigation(self, url):
        return self.driver.get(url)

    # Ожидание отображения элемента
    def visibility_of_element_located(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    # Ожидание кликабельности элемента
    def check_clickable_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    # Клик элемента
    def click_element(self, locator):  # Клик на элемент
        element = self.check_clickable_of_element_located(locator)
        return element.click()

    # Проверка отображения элемента
    def check_element_displayed(self, locator):
        return self.visibility_of_element_located(locator).is_displayed()

    # Отправить значение в поля
    def input_text(self, locator, text):
        element = self.visibility_of_element_located(locator)
        element.clear()
        return element.send_keys(text)

    # Скролл страницы до элемента
    def execute_script(self, locator):
        element = self.visibility_of_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Переключить на новую вкладку
    def switch_to_the_new_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

