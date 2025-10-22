from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def click_dynamic_button():
    """Клик по синей кнопке с динамическим ID"""
    
    try:
        # Открыть браузер Google Chrome
        driver = webdriver.Chrome()
        driver.set_window_size(1200, 800)
        
        # Перейти на страницу
        print("🌐 Переходим на страницу Dynamic ID...")
        driver.get("http://uitestingplayground.com/dynamicid")
        time.sleep(2)
        
        # Найти синюю кнопку по классу (класс остается постоянным, в отличие от ID)
        blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        
        print(f"🔵 Найдена синяя кнопка:")
        print(f"   - Текст: '{blue_button.text}'")
        print(f"   - Класс: '{blue_button.get_attribute('class')}'")
        print(f"   - ID: '{blue_button.get_attribute('id')}' (динамическое)")
        
        # Кликнуть на синюю кнопку
        blue_button.click()
        print("✅ Клик по синей кнопке выполнен")
        
        # Проверим, что клик прошел успешно (кнопка становится активной)
        print("🎯 Кнопка успешно нажата!")
        
        # Небольшая пауза для визуального наблюдения
        time.sleep(2)
        
        print("🎉 Скрипт успешно выполнен!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрыть браузер
        if 'driver' in locals():
            driver.quit()
            print("🔒 Браузер закрыт")

if __name__ == "__main__":
    click_dynamic_button()