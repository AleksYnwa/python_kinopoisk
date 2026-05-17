from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.settings import Settings


def create_driver(browser_name: str) -> webdriver.Remote:
    if browser_name == "chrome":
        return _create_chrome()
    if browser_name == "firefox":
        return _create_firefox()
    raise ValueError(f"Unsupported browser: {browser_name}")


def _create_chrome() -> webdriver.Chrome:
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=ru-RU")
    options.add_argument("--window-size=1400,900")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    profile_dir = Path(Settings.CHROME_PROFILE_DIR)
    profile_dir.mkdir(parents=True, exist_ok=True)
    options.add_argument(f"--user-data-dir={profile_dir}")

    if Settings.HEADLESS:
        options.add_argument("--headless=new")

    return webdriver.Chrome(options=options)


def _create_firefox() -> webdriver.Firefox:
    options = FirefoxOptions()
    options.set_preference("intl.accept_languages", "ru-RU, ru")
    if Settings.HEADLESS:
        options.add_argument("--headless")
    return webdriver.Firefox(options=options)
