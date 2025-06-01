import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


def test_open_kinopoisk_homepage(driver):
    """Проверка загрузки главной страницы."""
    driver.get("https://www.kinopoisk.ru/")
    assert "КиноПоиск" in driver.title


def test_search_movie(driver):
    """Проверка поиска фильма."""
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "kp_query"))
    )
    search_input.send_keys("Интерстеллар")
    search_input.submit()

    results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".search_results"))
    )
    assert "Интерстеллар" in results.text


def test_navigate_to_films_section(driver):
    """Проверка перехода в раздел 'Фильмы'."""
    films_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Фильмы"))
    films_link.click()

    assert "/film/" in driver.current_url


def test_login_button_clickable(driver):
    """Проверка кликабельности кнопки входа."""
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "styles_loginButton__"))
    )
    login_button.click()

    auth_modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".auth-modal"))
    )
    assert auth_modal.is_displayed()


def test_check_popular_movies_list(driver):
    """Проверка наличия списка популярных фильмов."""
    driver.get("https://www.kinopoisk.ru/lists/movies/popular/")
    movies_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_root__"))
    assert len(movies_list.find_elements(By.CSS_SELECTOR, ".styles_row__")) > 0