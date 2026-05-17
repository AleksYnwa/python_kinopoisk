import pytest
import allure

from config.test_data import TestData
from pages.kinopoisk_page import KinopoiskPage


@pytest.mark.ui
class TestKinopoiskUI:
    @allure.title("Главная: логотип и форма входа")
    def test_auth_form_consistency(self, browser):
        with allure.step("Открыть kinopoisk.ru и форму входа"):
            page = KinopoiskPage(browser).open_login_form()

        with allure.step("Проверить поле логина"):
            placeholder = page.get_login_placeholder().lower()
            assert any(word in placeholder for word in ("логин", "email", "почт", "телефон"))
            assert page.get_login_value() == ""
            assert not page.is_password_field_visible()

    @allure.title("Кнопка входа активна после ввода логина")
    def test_login_button_state(self, browser):
        page = KinopoiskPage(browser).open_login_form()

        with allure.step("Пустое поле логина"):
            assert page.get_login_value() == ""

        with allure.step("Ввод email"):
            page.enter_login(TestData.VALID_EMAIL)
            assert TestData.VALID_EMAIL in page.get_login_value()
            assert page.is_login_submit_enabled()

    @allure.title("Ошибка при неверном логине")
    def test_validation_errors(self, browser):
        page = KinopoiskPage(browser).open_login_form()

        with allure.step("Отправить неверный логин"):
            page.enter_login(TestData.INVALID_EMAIL).submit_login()

        with allure.step("Проверить сообщение об ошибке"):
            error = (page.get_error_message() or "").lower()
            assert error
            assert any(word in error for word in ("логин", "email", "существ", "неверн", "укажите"))

    @allure.title("Поле поиска на главной")
    def test_search_visibility(self, browser):
        page = KinopoiskPage(browser).open_main()
        assert page.is_search_visible()
        placeholder = page.get_search_placeholder().lower()
        assert any(word in placeholder for word in ("фильм", "сериал", "персон", "поиск"))
