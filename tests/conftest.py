import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = (
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    )

    yield
    browser.quit()
