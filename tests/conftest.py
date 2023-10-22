import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions




@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')  # Use 'headless' if you don't need browser UI or 'chrome' if you need UI
    options.add_argument('--start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # for cleaning console out of DevTools warns
    options.add_argument('--window-size=1920,1080')
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()