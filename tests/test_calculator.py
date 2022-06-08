from pages import GoogleHomePage
from pages import GoogleCalculatorPage
from allure import step


def test_calculator(browser):
    """
    Открыть страницу http://google.com
    В поисковую строку ввести слово “Калькулятор”
    Нажать на кнопку поиска
    В открывшемся калькуляторе посчитать результат выражения: «1 * 2 - 3 + 1»

    OP:
    в строке памяти (строка над результатом) отображается ранее введенная формула «1 * 2 - 3 + 1 =»
    в строке результата отображается «0»
    """
    home = GoogleHomePage(browser)
    calc = GoogleCalculatorPage(browser)

    with step("Открыть страницу http://google.com"):
        home.open("https://google.com")

    with step("В поисковую строку ввести слово “Калькулятор”"):
        home.fill_search_input("Калькулятор")

    with step("Нажать на кнопку поиска"):
        home.click_on_search_btn()

    with step("В открывшемся калькуляторе посчитать результат выражения: «1 * 2 - 3 + 1»"):
        calc.calculate_expression()
