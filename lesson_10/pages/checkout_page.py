from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from typing import Tuple

class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа SauceDemo.
    
    Attributes:
        FIRST_NAME_INPUT (Tuple[str, str]): Локатор поля ввода имени
        LAST_NAME_INPUT (Tuple[str, str]): Локатор поля ввода фамилии
        POSTAL_CODE_INPUT (Tuple[str, str]): Локатор поля ввода почтового индекса
        CONTINUE_BUTTON (Tuple[str, str]): Локатор кнопки продолжения
        TOTAL_LABEL (Tuple[str, str]): Локатор итоговой суммы
    """
    
    FIRST_NAME_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "#continue")
    TOTAL_LABEL: Tuple[str, str] = (By.CSS_SELECTOR, ".summary_total_label")
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Заполнить информацию для оформления заказа")
    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнить информацию для оформления заказа.
        
        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс
        """
        self.fill_field(self.FIRST_NAME_INPUT, first_name)
        self.fill_field(self.LAST_NAME_INPUT, last_name)
        self.fill_field(self.POSTAL_CODE_INPUT, postal_code)
        self.take_screenshot("filled_checkout_info")
    
    @allure.step("Перейти к обзору заказа")
    def continue_to_overview(self) -> None:
        """Перейти к обзору заказа."""
        self.click_element(self.CONTINUE_BUTTON)
        self.take_screenshot("checkout_overview")
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму заказа.
        
        Returns:
            str: Текст итоговой суммы
        """
        return self.get_element_text(self.TOTAL_LABEL)