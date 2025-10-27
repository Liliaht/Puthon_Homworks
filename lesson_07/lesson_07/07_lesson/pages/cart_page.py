from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .checkout_page import CheckoutPage

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    
    def wait_for_load(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        return self
    
    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def click_checkout(self):
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        checkout_button.click()
        return CheckoutPage(self.driver)