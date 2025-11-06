from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure
from typing import Tuple, List

class ProductsPage(BasePage):
    """
    Класс для работы со страницей товаров SauceDemo.
    
    Attributes:
        PRODUCTS_TITLE (Tuple[str, str]): Локатор заголовка страницы товаров
        SHOPPING_CART (Tuple[str, str]): Локатор иконки корзины
        PRODUCT_ITEMS (Tuple[str, str]): Локатор карточек товаров
    """
    
    PRODUCTS_TITLE: Tuple[str, str] = (By.CSS_SELECTOR, ".title")
    SHOPPING_CART: Tuple[str, str] = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_ITEMS: Tuple[str, str] = (By.CSS_SELECTOR, ".inventory_item")
    
    def __init__(self, driver):
        """
        Инициализация страницы товаров.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Проверить загрузку страницы товаров")
    def is_products_page_loaded(self) -> bool:
        """
        Проверить, что страница товаров загружена.
        
        Returns:
            bool: True если страница загружена, иначе False
        """
        try:
            return "Products" in self.get_element_text(self.PRODUCTS_TITLE)
        except:
            return False
    
    @allure.step("Добавить товар в корзину: {product_name}")
    def add_product_to_cart_by_name(self, product_name: str) -> None:
        """
        Добавить товар в корзину по названию.
        
        Args:
            product_name: Название товара
        """
        # Локатор кнопки добавления в корзину для конкретного товара
        add_to_cart_button = (
            By.XPATH, 
            f"//div[contains(@class, 'inventory_item_name') and text()='{product_name}']/ancestor::div[@class='inventory_item_description']//button"
        )
        self.click_element(add_to_cart_button)
        self.take_screenshot(f"added_{product_name.replace(' ', '_')}_to_cart")
    
    @allure.step("Добавить товары в корзину: {product_names}")
    def add_products_to_cart(self, product_names: List[str]) -> None:
        """
        Добавить несколько товаров в корзину.
        
        Args:
            product_names: Список названий товаров
        """
        for product_name in product_names:
            self.add_product_to_cart_by_name(product_name)
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Перейти в корзину."""
        self.click_element(self.SHOPPING_CART)
        self.take_screenshot("navigated_to_cart")