import os
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_KINOPOISK_DATA_DIR = _PROJECT_ROOT / ".kinopoisk"


def _env_bool(name: str, default: str) -> bool:
    return os.getenv(name, default).lower() in ("1", "true", "yes")


class Settings:
    # UI — https://www.kinopoisk.ru/
    KINOPOISK_URL = "https://www.kinopoisk.ru/"
    PASSPORT_LOGIN_URL = (
        "https://passport.yandex.ru/auth/add/login"
        "?origin=kinopoisk&retpath=https%3A%2F%2Fwww.kinopoisk.ru%2F"
    )
    BASE_URL = KINOPOISK_URL
    BROWSERS = ["chrome"]

    CHROME_PROFILE_DIR = _KINOPOISK_DATA_DIR / "chrome-profile"
    COOKIES_FILE = _KINOPOISK_DATA_DIR / "cookies.json"
    HEADLESS = _env_bool("KINOPOISK_HEADLESS", "0")

    # API
    API_URL = "https://api.kinopoisk.dev/"
    API_KEY = os.getenv(
        "KINOPOISK_API_KEY",
        "5MHJKGM-MQ7MNRM-JCTY8A5-BXKXJ2P",
    )
    API_VERSION = "v1.4"

    UI_TIMEOUT = 15
    API_TIMEOUT = 5
