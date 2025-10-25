from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

def test_input_field():
    """Тестирование поля ввода в Firefox"""
    
    try:
        # Открыть браузер Firefox
        driver = webdriver.Firefox()
        driver.set_window_size(1200, 800)
        
        # Перейти на страницу
        print("🌐 Переходим на страницу Inputs...")
        driver.get("http://the-internet.herokuapp.com/inputs")
        time.sleep(2)
        
        # Найти поле ввода
        input_field = driver.find_element(By.TAG_NAME, "input")
        print("✅ Поле ввода найдено")
        
        # Ввести текст "Sky"
        input_field.send_keys("Sky")
        print("📝 Введен текст: 'Sky'")
        time.sleep(1)
        
        # Очистить поле
        input_field.clear()
        print("🧹 Поле очищено")
        time.sleep(1)
        
        # Ввести текст "Pro"
        input_field.send_keys("Pro")
        print("📝 Введен текст: 'Pro'")
        time.sleep(1)
        
        # Проверить введенное значение
        current_value = input_field.get_attribute("value")
        print(f"🔍 Текущее значение поля: '{current_value}'")
        
        print("🎉 Операции с полем ввода успешно выполнены!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрыть браузер методом quit()
        if 'driver' in locals():
            driver.quit()
            print("🔒 Браузер закрыт (метод quit())")

if __name__ == "__main__":
    test_input_field()