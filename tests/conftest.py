import sys
from pathlib import Path

import pytest

root_path = Path(__file__).parent.parent
sys.path.append(str(root_path))

from config.settings import Settings
from utilities.browser_factory import create_driver
from utilities.kinopoisk_session import prepare_kinopoisk_session


@pytest.fixture(scope="function", params=Settings.BROWSERS)
def browser(request):
    driver = create_driver(request.param)
    driver.implicitly_wait(Settings.UI_TIMEOUT)
    try:
        prepare_kinopoisk_session(driver)
        yield driver
    finally:
        driver.quit()
