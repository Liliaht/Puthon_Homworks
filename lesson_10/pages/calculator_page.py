from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from typing import Tuple, Dict

class CalculatorPage(BasePage):
    """
    Класс для работы со страницей калькулятора.
    
    Attributes:
        DELAY_INPUT (Tuple[str, str]): Локатор поля ввода задержки
        RESULT_DISPLAY (Tuple[str, str]): Локатор поля вывода результата
        BUTTONS (Dict[str, Tuple[str, str]]): Словарь с локаторами кнопок калькулятора
    """
    
    DELAY_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY: Tuple[str, str] = (By.CSS_SELECTOR, ".screen")
    
    # Словарь с локаторами кнопок калькулятора
    BUTTONS: Dict[str, Tuple[str, str]] = {
        '0': (By.XPATH, "//span[text()='0']"),
        '1': (By.XPATH, "//span[text()='1']"),
        '2': (By.XPATH, "//span[text()='2']"),
        '3': (By.XPATH, "//span[text()='3']"),
        '4': (By.XPATH, "//span[text()='4']"),
        '5': (By.XPATH, "//span[text()='5']"),
        '6': (By.XPATH, "//span[text()='6']"),
        '7': (By.XPATH, "//span[text()='7']"),
        '8': (By.XPATH, "//span[text()='8']"),
        '9': (By.XPATH, "//span[text()='9']"),
        '+': (By.XPATH, "//span[text()='+']"),
        '-': (By.XPATH, "//span[text()='-']"),
        '*': (By.XPATH, "//span[text()='×']"),
        '/': (By.XPATH, "//span[text()='÷']"),
        '=': (By.XPATH, "//span[text()='=']"),
        'C': (By.XPATH, "//span[text()='C']")
    }
    
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    
    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора."""
        self.driver.get(self.url)
        self.take_screenshot("calculator_page_loaded")
    
    @allure.step("Установить задержку: {delay_seconds} секунд")
    def set_delay(self, delay_seconds: int) -> None:
        """
        Установить значение задержки вычислений.
        
        Args:
            delay_seconds: Задержка в секундах
        """
        self.fill_field(self.DELAY_INPUT, str(delay_seconds))
    
    @allure.step("Нажать кнопку: {button}")
    def click_button(self, button: str) -> None:
        """
        Нажать на кнопку калькулятора.
        
        Args:
            button: Символ кнопки ('0'-'9', '+', '-', '*', '/', '=', 'C')
        """
        if button in self.BUTTONS:
            self.click_element(self.BUTTONS[button])
        else:
            raise ValueError(f"Кнопка '{button}' не найдена в калькуляторе")
    
    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 50) -> str:
        """
        Получить результат вычислений.
        
        Args:
            timeout: Время ожидания результата в секундах
            
        Returns:
            str: Текст результата
        """
        return self.get_element_text(self.RESULT_DISPLAY, timeout)
    
    @allure.step("Выполнить вычисление: {expression} с задержкой {delay} секунд")
    def calculate_expression(self, expression: str, delay: int = 45) -> str:
        """
        Выполнить вычисление выражения.
        
        Args:
            expression: Выражение для вычисления (например, "7+8")
            delay: Задержка вычислений в секундах
            
        Returns:
            str: Результат вычислений
        """
        self.set_delay(delay)
        
        # Нажимаем кнопки посимвольно
        for char in expression:
            self.click_button(char)
        
        # Нажимаем кнопку '='
        self.click_button('=')
        
        # Ждем результат
        result = self.get_result(delay + 5)
        self.take_screenshot("calculation_result")
        
        return result