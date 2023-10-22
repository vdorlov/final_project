from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import urlparse

class SeleniumBase:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 15)
        self.driver = driver

    @staticmethod
    def __get_selenium_by(find_by: str):
        find_by = find_by.lower()
        locators = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH
        }
        return locators[find_by]

    def is_present(self, find_by: str, locator: str, locator_name: str):
        return self.wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str):
        return self.wait.until(EC.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_visible(self, find_by: str, locator: str, locator_name: str):
        return self.wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                               locator_name)

    def get_relative_page(self):
        self.driver.implicitly_wait(20)
        url = urlparse(self.driver.current_url)
        return url.path

