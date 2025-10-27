from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .cart_page import CartPage

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    
    def wait_for_load(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        return self
    
    def add_backpack_to_cart(self):
        backpack_button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        backpack_button.click()
        return self
    
    def add_bolt_tshirt_to_cart(self):
        tshirt_button = self.driver.find_element(*self.BOLT_TSHIRT_ADD_BUTTON)
        tshirt_button.click()
        return self
    
    def add_onesie_to_cart(self):
        onesie_button = self.driver.find_element(*self.ONESIE_ADD_BUTTON)
        onesie_button.click()
        return self
    
    def add_all_required_products(self):
        self.add_backpack_to_cart()
        self.add_bolt_tshirt_to_cart()
        self.add_onesie_to_cart()
        return self
    
    def go_to_cart(self):
        cart_icon = self.driver.find_element(*self.CART_ICON)
        cart_icon.click()
        return CartPage(self.driver)