from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

def test_class_attr():
    """Тестирование клика по синей кнопке на странице Class Attribute"""
    
    try:
        # Настройка ChromeDriver (автоматический поиск в PATH)
        driver = webdriver.Chrome()
        
        # Установить размер окна для стабильности
        driver.set_window_size(1200, 800)
        
        # Перейти на страницу
        print("🌐 Переходим на страницу...")
        driver.get("http://uitestingplayground.com/classattr")
        
        # Небольшая пауза для загрузки страницы
        time.sleep(2)
        
        # Найти синюю кнопку по XPath (более надежный способ)
        blue_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]")
        
        print("🔵 Найдена синяя кнопка")
        
        # Кликнуть на синюю кнопку
        blue_button.click()
        print("✅ Клик выполнен")
        
        # Обработать всплывающее окно (alert)
        time.sleep(1)  # Небольшая пауза для появления alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"📢 Текст всплывающего окна: {alert_text}")
        alert.accept()  # Закрыть окно
        print("✅ Всплывающее окно закрыто")
        
        # Небольшая пауза для визуального наблюдения
        time.sleep(2)
        
        print("🎉 Скрипт успешно выполнен!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        print("💡 Убедитесь, что:")
        print("   - Установлен Chrome браузер")
        print("   - Установлен ChromeDriver и он доступен в PATH")
        print("   - Есть подключение к интернету")
        
    finally:
        # Закрыть браузер
        if 'driver' in locals():
            driver.quit()
            print("🔒 Браузер закрыт")

if __name__ == "__main__":
    test_class_attr()