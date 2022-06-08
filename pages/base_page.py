from typing import Union
from selenium import webdriver
from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

WebDriver = Union[webdriver.Firefox, webdriver.Chrome]


def _by(path: str):
    try:
        if "/" in path:
            return By.XPATH
        else:
            return By.CSS_SELECTOR
    except Exception:
        raise Exception(f"Локатор должен быть либо xpath, либо css_selector. Сейчас {path}")


class BasePage(ABC):
    def __init__(self, browser):
        self.br: WebDriver = browser
        self.wait = 20

    def _element(self, selector: str, wait=None):
        _wait = wait if wait else self.wait
        try:
            WebDriverWait(self.br, timeout=_wait).until(EC.presence_of_element_located((_by(selector), selector)))
            return self.br.find_element(_by(selector), selector)
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором {selector} не найден в течение {_wait} сек")

    def open(self, url: str = ""):
        self.br.get(url)

    def click(self, selector: str):
        self._element(selector).click()

    def get_text(self, selector: str):
        return self._element(selector).text

    def fill(self, selector: str, text: str):
        self._element(selector).clear()
        self._element(selector).send_keys(text)

    def wait_visible(self, selector: str, wait=None):
        _wait = wait if wait else self.wait
        WebDriverWait(self.br, timeout=_wait).until(
            EC.visibility_of_element_located((_by(selector), selector)))
