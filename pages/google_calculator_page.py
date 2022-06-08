from pages import BasePage

class Elements:
    number1 = "//div[text()='1']"
    number2 = "//div[text()='2']"
    number3 = "//div[text()='3']"

    multi = "//div[@aria-label='умножение']"
    subtraction = "//div[@aria-label='вычитание']"
    addition = "//div[@aria-label='сложение']"
    equal = "//div[@aria-label='равно']"

    value_memory = "//span[text()='1 × 2 - 3 + 1 =']"
    calc_result = "//div[@role='presentation']//span[text()='0']"


class GoogleCalculatorPage(BasePage):
    def is_load(self):
        pass

    def calculate_expression(self):
        self.click(Elements.number1)
        self.click(Elements.multi)
        self.click(Elements.number2)
        self.click(Elements.subtraction)
        self.click(Elements.number3)
        self.click(Elements.addition)
        self.click(Elements.number1)
        self.click(Elements.equal)

        assert self.get_text(Elements.value_memory) == "1 × 2 - 3 + 1 ="
        assert self.get_text(Elements.calc_result) == "0"
