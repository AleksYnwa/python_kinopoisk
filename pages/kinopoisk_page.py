import time
from typing import Optional

from selenium.webdriver.common.by import By

from config.settings import Settings

from .base_page import BasePage


class KinopoiskPage(BasePage):
    """Главная kinopoisk.ru и форма входа (Яндекс ID)."""

    LOGO = (By.CSS_SELECTOR, "a[class*='styles_logo']")
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input.kinopoisk-header-search-form-input__input, header input[type='text']",
    )
    HEADER_LOGIN_BUTTON = (By.XPATH, "//button[contains(normalize-space(), 'Войти')]")

    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']:not([name='hidden-password'])")
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(), 'Войти') and not(contains(normalize-space(), 'другим'))]",
    )
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[class*='error'], [role='alert'], .passp-form-field__error",
    )

    def open_main(self) -> "KinopoiskPage":
        self.driver.get(Settings.KINOPOISK_URL)
        self.wait_for_visibility(self.LOGO)
        return self

    def open_login_form(self) -> "KinopoiskPage":
        """Главная → страница входа по email (Яндекс ID)."""
        self.open_main()
        self.driver.get(Settings.PASSPORT_LOGIN_URL)
        self.wait_for_visibility(self.LOGIN_FIELD)
        return self

    def enter_login(self, value: str) -> "KinopoiskPage":
        field = self.wait_for_visibility(self.LOGIN_FIELD)
        field.clear()
        field.send_keys(value)
        return self

    def enter_password(self, password: str) -> "KinopoiskPage":
        field = self.wait_for_visibility(self.PASSWORD_FIELD)
        field.clear()
        field.send_keys(password)
        return self

    def submit_login(self) -> "KinopoiskPage":
        self.wait_for_clickable(self.LOGIN_SUBMIT_BUTTON).click()
        return self

    def get_login_value(self) -> str:
        return self.wait_for_visibility(self.LOGIN_FIELD).get_attribute("value") or ""

    def get_login_placeholder(self) -> str:
        field = self.wait_for_visibility(self.LOGIN_FIELD)
        return (field.get_attribute("placeholder") or field.get_attribute("aria-label") or "").strip()

    def get_password_placeholder(self) -> str:
        if not self.is_password_field_visible():
            return ""
        field = self.wait_for_visibility(self.PASSWORD_FIELD)
        return (field.get_attribute("placeholder") or field.get_attribute("aria-label") or "Пароль").strip()

    def is_password_field_visible(self) -> bool:
        try:
            elements = self.driver.find_elements(*self.PASSWORD_FIELD)
            return any(el.is_displayed() for el in elements)
        except Exception:
            return False

    def is_login_submit_enabled(self) -> bool:
        return self.wait_for_visibility(self.LOGIN_SUBMIT_BUTTON).is_enabled()

    def get_error_message(self) -> Optional[str]:
        time.sleep(1)
        for element in self.driver.find_elements(*self.ERROR_MESSAGE):
            text = (element.text or "").strip()
            if len(text) > 3:
                return text
        body = self.driver.find_element(By.TAG_NAME, "body").text
        for line in body.split("\n"):
            line = line.strip()
            if any(word in line.lower() for word in ("логин", "существ", "неверн", "укажите")):
                return line
        return None

    def is_search_visible(self) -> bool:
        try:
            return self.wait_for_visibility(self.SEARCH_INPUT, timeout=5).is_displayed()
        except Exception:
            return False

    def get_search_placeholder(self) -> str:
        field = self.wait_for_visibility(self.SEARCH_INPUT)
        return (field.get_attribute("placeholder") or "").strip()
