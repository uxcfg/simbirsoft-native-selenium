import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def browser(request):
    chromedriver_binary.add_chromedriver_to_path()
    browser_name = request.config.getoption("--browser").lower()
    headless_mode = request.config.getoption("--headless")
    options_chrome = ChromeOptions()
    options_firefox = FirefoxOptions()

    if browser_name == "chrome":
        if headless_mode:
            options_chrome.add_argument("--headless")

        br = webdriver.Chrome(options=options_chrome)

    elif browser_name == "firefox":
        if headless_mode:
            options_firefox.add_argument("--headless")

        br = webdriver.Firefox(options=options_firefox)
    else:
        raise Exception(f"Такого значения значения параметра для browser {browser_name} не найдено")

    request.addfinalizer(br.quit)
    br.maximize_window()
    return br
