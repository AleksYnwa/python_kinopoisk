📌 UI и API тесты для Кинопоиска (Kinopoisk.ru)
Этот проект содержит автоматизированные тесты для сайта Кинопоиск с использованием:

Selenium (UI-тесты)

Requests (API-тесты)

Pytest (фреймворк для тестирования)

📋 Содержание
Установка и настройка

Запуск тестов

Структура проекта

Описание тестов

Генерация отчета

⚙️ Установка и настройка
1. Установите зависимости
bash
pip install selenium pytest requests pytest-html webdriver-manager
2. Убедитесь, что у вас установлен Chrome
Selenium использует ChromeDriver для запуска браузера.

3. Клонируйте репозиторий
bash
git clone <ваш-репозиторий>
cd kinopoisk_tests
🚀 Запуск тестов
Запуск всех тестов
bash
pytest -v
Запуск только UI-тестов
bash
pytest test_ui.py -v
Запуск только API-тестов
bash
pytest test_api.py -v
Запуск с генерацией HTML-отчета
Отчет сохранится в файле report.html.

bash
pytest -v --html=report.html --self-contained-html
📂 Структура проекта
kinopoisk_tests/
├── conftest.py          # Фикстуры и настройки Pytest
├── test_ui.py           # UI-тесты (Selenium)
├── test_api.py          # API-тесты (Requests)
├── pytest.ini           # Конфигурация Pytest
└── README.md            # Документация
🧪 Описание тестов
🔸 UI-тесты (test_ui.py)
test_open_kinopoisk_homepage – Проверка загрузки главной страницы.

test_search_movie – Проверка поиска фильма ("Интерстеллар").

test_navigate_to_films_section – Проверка перехода в раздел "Фильмы".

test_login_button_clickable – Проверка открытия модального окна авторизации.

test_check_popular_movies_list – Проверка отображения списка популярных фильмов.

🔸 API-тесты (test_api.py)
test_api_homepage_status_code – Проверка статус-кода главной страницы.

test_api_search_movie – Проверка поиска фильма через API.

test_api_film_page_load – Проверка загрузки страницы фильма ("Побег из Шоушенка").

test_api_top_movies_list – Проверка API топ-фильмов.

test_api_suggestions_endpoint – Проверка API подсказок при поиске.

📊 Генерация отчета
После запуска тестов с ключом --html=report.html будет создан отчет в формате HTML:

bash
pytest -v --html=report.html --self-contained-html
Отчет включает:
✅ Статус прохождения тестов
✅ Время выполнения
✅ Скриншоты при падении UI-тестов (благодаря conftest.py)