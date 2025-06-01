import pytest
import requests

BASE_URL = "https://www.kinopoisk.ru"

def test_api_homepage_status_code():
    """Проверка статус-кода главной страницы."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_api_search_movie():
    """Проверка API поиска фильма."""
    search_url = f"{BASE_URL}/s/type/film/find/interstellar/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    assert response.status_code == 200
    assert "Интерстеллар" in response.text

def test_api_film_page_load():
    """Проверка загрузки страницы фильма."""
    film_url = f"{BASE_URL}/film/258687/"
    response = requests.get(film_url)
    assert response.status_code == 200
    assert "Побег из Шоушенка" in response.text

def test_api_top_movies_list():
    """Проверка API топ-фильмов."""
    top_url = f"{BASE_URL}/api/v1/top-films/"
    response = requests.get(top_url)
    assert response.status_code == 200
    assert "items" in response.json()

def test_api_suggestions_endpoint():
    """Проверка API подсказок при поиске."""
    suggest_url = f"{BASE_URL}/api/v1/suggestions"
    params = {"query": "матрица"}
    response = requests.get(suggest_url, params=params)
    assert response.status_code == 200
    assert len(response.json()["suggestions"]) > 0