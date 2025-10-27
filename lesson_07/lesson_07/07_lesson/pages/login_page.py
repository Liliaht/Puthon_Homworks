from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Локаторы
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self
    
    def enter_username(self, username):
        username_field = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME_FIELD)
        )
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        return MainPage(self.driver)