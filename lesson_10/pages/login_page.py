from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from typing import Tuple

class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации SauceDemo.
    
    Attributes:
        USERNAME_INPUT (Tuple[str, str]): Локатор поля ввода имени пользователя
        PASSWORD_INPUT (Tuple[str, str]): Локатор поля ввода пароля
        LOGIN_BUTTON (Tuple[str, str]): Локатор кнопки входа
        ERROR_MESSAGE (Tuple[str, str]): Локатор сообщения об ошибке
    """
    
    USERNAME_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT: Tuple[str, str] = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE: Tuple[str, str] = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
    
    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get(self.url)
        self.take_screenshot("login_page_loaded")
    
    @allure.step("Авторизоваться пользователем: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию.
        
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.fill_field(self.USERNAME_INPUT, username)
        self.fill_field(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        self.take_screenshot("after_login_attempt")
    
    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self) -> str:
        """
        Получить текст сообщения об ошибке.
        
        Returns:
            str: Текст ошибки
        """
        return self.get_element_text(self.ERROR_MESSAGE)