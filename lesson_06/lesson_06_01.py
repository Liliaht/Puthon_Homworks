from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # Нажимаем на синюю кнопку
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()
    
    # Ждем появления зеленой плашки и получаем текст
    green_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    
    # Получаем текст из зеленой плашки
    text = green_badge.text
    print(text)
    
finally:
    # Закрываем браузер
    driver.quit()