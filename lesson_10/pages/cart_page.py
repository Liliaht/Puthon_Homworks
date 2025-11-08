from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from typing import Tuple, List

class CartPage(BasePage):
    """
    Класс для работы со страницей корзины SauceDemo.
    
    Attributes:
        CART_TITLE (Tuple[str, str]): Локатор заголовка страницы корзины
        CHECKOUT_BUTTON (Tuple[str, str]): Локатор кнопки оформления заказа
        CART_ITEMS (Tuple[str, str]): Локатор элементов корзины
    """
    
    CART_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BUTTON: Tuple[str, str] = (By.CSS_SELECTOR, "#checkout")
    CART_ITEMS: Tuple[str, str] = (By.CSS_SELECTOR, ".cart_item")
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Проверить загрузку страницы корзины")
    def is_cart_page_loaded(self) -> bool:
        """
        Проверить, что страница корзины загружена.
        
        Returns:
            bool: True если страница загружена, иначе False
        """
        try:
            return "Your Cart" in self.get_element_text(self.CART_TITLE)
        except:
            return False
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.
        
        Returns:
            int: Количество товаров
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))
    
    @allure.step("Получить названия товаров в корзине")
    def get_cart_item_names(self) -> List[str]:
        """
        Получить названия товаров в корзине.
        
        Returns:
            List[str]: Список названий товаров
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        item_names = []
        for item in items:
            name_element = item.find_element(By.CSS_SELECTOR, ".inventory_item_name")
            item_names.append(name_element.text)
        return item_names
    
    @allure.step("Начать оформление заказа")
    def proceed_to_checkout(self) -> None:
        """Начать оформление заказа."""
        self.click_element(self.CHECKOUT_BUTTON)
        self.take_screenshot("proceeded_to_checkout")