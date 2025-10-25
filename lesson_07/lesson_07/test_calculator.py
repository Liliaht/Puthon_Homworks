from pages.calculator_page import CalculatorPage

def test_calculator_with_delay(driver):
    # Создаем объект страницы калькулятора
    calculator_page = CalculatorPage(driver)
    
    # Открываем страницу калькулятора
    calculator_page.open()
    
    # Выполняем вычисление: 7 + 8 с задержкой 45 секунд
    result = calculator_page.calculate("7+8=", 45)
    
    # Проверяем результат
    assert result == "15", f"Ожидался результат '15', но получено '{result}'"