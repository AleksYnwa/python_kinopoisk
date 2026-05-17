"""
Сохранить cookies для UI-тестов на kinopoisk.ru.

Запуск:
    python scripts/init_kinopoisk_session.py

Если появится капча — пройдите её в открывшемся окне Chrome.
"""
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from config.settings import Settings
from utilities.browser_factory import create_driver
from utilities.kinopoisk_session import is_captcha_page, is_kinopoisk_home, save_cookies


def main() -> None:
    print("Открываю https://www.kinopoisk.ru/ ...")
    print(f"Профиль Chrome: {Settings.CHROME_PROFILE_DIR}")
    driver = create_driver("chrome")
    driver.set_window_size(1400, 900)
    try:
        driver.get(Settings.KINOPOISK_URL)
        if is_captcha_page(driver):
            print("Пройдите капчу в браузере. Ожидание до 3 минут...")
            for _ in range(180):
                time.sleep(1)
                if is_kinopoisk_home(driver):
                    break
        if not is_kinopoisk_home(driver):
            print("Не удалось открыть Кинопоиск:", driver.current_url)
            sys.exit(1)
        save_cookies(driver, Settings.COOKIES_FILE)
        print(f"Cookies сохранены: {Settings.COOKIES_FILE}")
        print("Запуск тестов: pytest -m ui")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
