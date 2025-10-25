from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CLASS_NAME, "screen")
        self.buttons = {
            "0": (By.XPATH, "//span[text()='0']"),
            "1": (By.XPATH, "//span[text()='1']"),
            "2": (By.XPATH, "//span[text()='2']"),
            "3": (By.XPATH, "//span[text()='3']"),
            "4": (By.XPATH, "//span[text()='4']"),
            "5": (By.XPATH, "//span[text()='5']"),
            "6": (By.XPATH, "//span[text()='6']"),
            "7": (By.XPATH, "//span[text()='7']"),
            "8": (By.XPATH, "//span[text()='8']"),
            "9": (By.XPATH, "//span[text()='9']"),
            "+": (By.XPATH, "//span[text()='+']"),
            "-": (By.XPATH, "//span[text()='-']"),
            "*": (By.XPATH, "//span[text()='×']"),
            "/": (By.XPATH, "//span[text()='÷']"),
            "=": (By.XPATH, "//span[text()='=']"),
            "C": (By.XPATH, "//span[text()='C']")
        }
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(delay))
    
    def click_button(self, button):
        button_element = self.driver.find_element(*self.buttons[button])
        button_element.click()
    
    def get_result(self, timeout=46):
        result_element = WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "")
        )
        return self.driver.find_element(*self.screen).text
    
    def calculate(self, expression, delay):
        self.set_delay(delay)
        for char in expression:
            self.click_button(char)
        return self.get_result()