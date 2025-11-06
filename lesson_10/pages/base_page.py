from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
from typing import Tuple, Optional, Union

class BasePage:
    """
    Базовый класс для всех страниц приложения.
    
    Attributes:
        driver (WebDriver): Экземпляр веб-драйвера
        timeout (int): Время ожидания по умолчанию в секундах
    """
    
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: Экземпляр веб-драйвера
            timeout: Время ожидания по умолчанию в секундах
        """
        self.driver = driver
        self.timeout = timeout
    
    @allure.step("Найти элемент: {locator[1]}")
    def find_element(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebDriver:
        """
        Найти элемент на странице с ожиданием.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Время ожидания в секундах
            
        Returns:
            WebDriver: Найденный элемент
        """
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    @allure.step("Кликнуть на элемент: {locator[1]}")
    def click_element(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> None:
        """
        Кликнуть на элемент после ожидания его кликабельности.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Время ожидания в секундах
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    @allure.step("Заполнить поле {locator[1]} значением: {text}")
    def fill_field(self, locator: Tuple[str, str], text: str, timeout: Optional[int] = None) -> None:
        """
        Заполнить поле ввода текстом.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            text: Текст для ввода
            timeout: Время ожидания в секундах
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента: {locator[1]}")
    def get_element_text(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> str:
        """
        Получить текст элемента.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            timeout: Время ожидания в секундах
            
        Returns:
            str: Текст элемента
        """
        element = self.find_element(locator, timeout)
        return element.text
    
    @allure.step("Ожидать текст '{text}' в элементе: {locator[1]}")
    def wait_for_text_in_element(self, locator: Tuple[str, str], text: str, timeout: Optional[int] = None) -> bool:
        """
        Ожидать появления определенного текста в элементе.
        
        Args:
            locator: Кортеж (By, selector) для поиска элемента
            text: Ожидаемый текст
            timeout: Время ожидания в секундах
            
        Returns:
            bool: True если текст появился, иначе False
        """
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Сделать скриншот: {name}")
    def take_screenshot(self, name: str) -> None:
        """
        Сделать скриншот и прикрепить к Allure отчету.
        
        Args:
            name: Название скриншота
        """
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )