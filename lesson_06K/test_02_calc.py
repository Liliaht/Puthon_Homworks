from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    # Инициализация драйвера Google Chrome
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    try:
        # Вводим значение 45 в поле задержки
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        # Нажимаем кнопки: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        # Ждем появления результата 15 в течение 46 секунд (с запасом)
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        
        # Используем ожидание с таймаутом 46 секунд
        WebDriverWait(driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        
        # Проверяем, что результат равен 15
        result_text = result_element.text
        assert result_text == "15", f"Ожидался результат '15', но получено '{result_text}'"
        
    finally:
        # Закрываем браузер
        driver.quit()