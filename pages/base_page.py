from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import Settings


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.UI_TIMEOUT)

    def open(self):
        """Открывает базовый URL"""
        self.driver.get(Settings.BASE_URL)
        return self

    def wait_for_visibility(self, locator, timeout=Settings.UI_TIMEOUT):
        """Ожидает видимости элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=Settings.UI_TIMEOUT):
        """Ожидает, когда элемент станет кликабельным"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
