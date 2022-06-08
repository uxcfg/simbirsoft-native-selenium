from pages import BasePage
from pages.google_calculator_page import Elements as CaclElements


class Elements:
    search_input = "//input[@aria-label='Найти']"
    submit_btn = "//div[@jsname]//input[@name='btnK']"


class GoogleHomePage(BasePage):
    url = "https://google.com"

    def fill_search_input(self, value):
        self.fill(Elements.search_input, value)

    def click_on_search_btn(self):
        self.click(Elements.submit_btn)
        self.wait_visible(CaclElements.number1)
