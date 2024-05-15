
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigation(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        element = self.driver.find_element(locator)
        return element

    def click_element(self, locator):
        self.wait_for_element_visible(locator)
        return self.find_element(locator).click()

    def execute_script(self, locator):  # Скролл страницы до элемента
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_visible(self, locator):  # Ожидание отображения элемента
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        return element.send_keys(text)



