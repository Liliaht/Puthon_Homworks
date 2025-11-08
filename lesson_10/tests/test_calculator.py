import pytest
import allure

@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для калькулятора."""
    
    @allure.title("Тест медленного калькулятора с задержкой 45 секунд")
    @allure.description("""
    Тест проверяет работу медленного калькулятора:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Выполнить вычисление 7 + 8
    4. Проверить что результат равен 15 через 45 секунд
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_slow_calculator(self, calculator_page):
        """
        Тест медленного калькулятора.
        """
        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()
        
        with allure.step("Выполнить вычисление 7 + 8 с задержкой 45 секунд"):
            result = calculator_page.calculate_expression("7+8", delay=45)
        
        with allure.step("Проверить результат вычисления"):
            assert result == "15", f"Ожидался результат 15, но получен {result}"
            allure.attach(f"Результат вычисления: {result}", name="calculation_result", attachment_type=allure.attachment_type.TEXT)

    @allure.title("Тест сложения с минимальной задержкой")
    @allure.description("Тест проверяет базовое сложение с минимальной задержкой для быстрого выполнения")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculator_addition(self, calculator_page):
        """
        Тест сложения с минимальной задержкой.
        """
        calculator_page.open()
        
        result = calculator_page.calculate_expression("5+3", delay=1)
        
        with allure.step("Проверить результат сложения 5 + 3"):
            assert result == "8", f"Ожидался результат 8, но получен {result}"