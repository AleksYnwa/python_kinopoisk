import json
import time
from pathlib import Path
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import Settings


def is_captcha_page(driver: WebDriver) -> bool:
    return "showcaptcha" in driver.current_url.lower()


def is_kinopoisk_home(driver: WebDriver) -> bool:
    url = driver.current_url.lower()
    return "kinopoisk.ru" in url and "showcaptcha" not in url and "passport.yandex" not in url


def load_cookies(driver: WebDriver, path: Path) -> bool:
    if not path.is_file():
        return False

    raw: list[dict[str, Any]] = json.loads(path.read_text(encoding="utf-8"))
    driver.get(Settings.KINOPOISK_URL)
    for cookie in raw:
        item = dict(cookie)
        item.pop("sameSite", None)
        try:
            driver.add_cookie(item)
        except Exception:
            pass
    driver.refresh()
    time.sleep(2)
    return True


def save_cookies(driver: WebDriver, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(driver.get_cookies(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def prepare_kinopoisk_session(driver: WebDriver) -> None:
    """Открывает kinopoisk.ru с сохранённой сессией (профиль + cookies)."""
    load_cookies(driver, Settings.COOKIES_FILE)
    driver.get(Settings.KINOPOISK_URL)
    time.sleep(2)

    if is_captcha_page(driver):
        raise RuntimeError(
            "Кинопоиск показал капчу. Один раз выполните:\n"
            "  python scripts/init_kinopoisk_session.py\n"
            "Пройдите капчу в открывшемся Chrome — cookies сохранятся для тестов."
        )

    if not is_kinopoisk_home(driver):
        raise RuntimeError(
            f"Не удалось открыть главную Кинопоиска. Текущий URL: {driver.current_url}"
        )

    save_cookies(driver, Settings.COOKIES_FILE)
