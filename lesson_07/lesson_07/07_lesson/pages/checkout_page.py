from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    def wait_for_load(self):
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_FIELD)
        )
        return self
    
    def fill_personal_info(self, first_name, last_name, postal_code):
        first_name_field = self.driver.find_element(*self.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)
        
        last_name_field = self.driver.find_element(*self.LAST_NAME_FIELD)
        last_name_field.send_keys(last_name)
        
        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_FIELD)
        postal_code_field.send_keys(postal_code)
        
        return self
    
    def click_continue(self):
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()
        return self
    
    def wait_for_summary_load(self):
        self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return self
    
    def get_total_amount(self):
        total_element = self.driver.find_element(*self.TOTAL_LABEL)
        total_text = total_element.text
        # Извлекаем числовое значение из текста "Total: $58.29"
        total_value = total_text.replace("Total: $", "")
        return total_value