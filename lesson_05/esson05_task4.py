from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

def login_test():
    """Тест авторизации на сайте"""
    
    driver = None
    try:
        # Открыть браузер Firefox
        print("🦊 Запускаем Firefox...")
        driver = webdriver.Firefox()
        driver.set_window_size(1200, 800)
        
        # Перейти на страницу логина
        print("🌐 Переходим на страницу логина...")
        driver.get("http://the-internet.herokuapp.com/login")
        time.sleep(2)
        
        # Проверить заголовок страницы
        print(f"📄 Заголовок страницы: '{driver.title}'")
        
        # Найти поле username и ввести значение
        print("👤 Вводим username...")
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("tomsmith")
        print("✅ Username 'tomsmith' введен")
        
        # Найти поле password и ввести значение
        print("🔒 Вводим password...")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("SuperSecretPassword!")
        print("✅ Password введен")
        
        # Нажать кнопку Login
        print("🚀 Нажимаем кнопку Login...")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("✅ Кнопка Login нажата")
        
        # Ждем загрузки следующей страницы
        time.sleep(2)
        
        # Найти зеленую плашку с сообщением об успехе
        print("🔍 Ищем сообщение об успешной авторизации...")
        success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        message_text = success_message.text.strip()
        
        # Вывести текст плашки в консоль
        print("\n" + "="*50)
        print("💚 ТЕКСТ ЗЕЛЕНОЙ ПЛАШКИ:")
        print(message_text)
        print("="*50 + "\n")
        
        # Проверим URL после логина
        print(f"🔗 Текущий URL: {driver.current_url}")
        
        print("🎉 Авторизация прошла успешно!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        
    finally:
        # Закрыть браузер методом quit()
        if driver:
            print("🔒 Закрываем браузер...")
            driver.quit()
            print("🔒 Браузер закрыт (метод quit())")

if __name__ == "__main__":
    login_test()