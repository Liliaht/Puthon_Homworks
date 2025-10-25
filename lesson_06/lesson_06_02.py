from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    # Находим поле ввода и вводим текст SkyPro
    text_input = driver.find_element(By.ID, "newButtonName")
    text_input.clear()
    text_input.send_keys("SkyPro")
    
    # Нажимаем на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    
    # Ждем, пока текст кнопки изменится на SkyPro и получаем его
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    # Получаем окончательный текст кнопки
    button_text = blue_button.text
    print(button_text)
    
finally:
    # Закрываем браузер
    driver.quit()