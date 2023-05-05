import pytest
from selene.support.shared import config
from selene.support.shared import browser


@pytest.fixture()
def mobile_config():
    config.window_width = 390
    config.window_height = 844
    yield
    browser.quit()


@pytest.fixture()
def desktop_config():
    config.window_width = 1920
    config.window_height = 1080
    yield
    browser.quit()
