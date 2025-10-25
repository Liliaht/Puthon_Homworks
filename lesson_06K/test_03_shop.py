from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_cart_total():
    # Инициализация драйвера Firefox
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    
    try:
        # Авторизация как standard_user
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Ждем загрузки страницы с товарами
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
        # Добавляем товары в корзину
        # Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()
        
        # Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()
        
        # Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()
        
        # Переходим в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        # Ждем загрузки корзины
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        
        # Нажимаем Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        # Ждем загрузки формы checkout
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        
        # Заполняем форму данными
        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")
        
        first_name_field.send_keys("Иван")
        last_name_field.send_keys("Петров")
        postal_code_field.send_keys("123456")
        
        # Нажимаем Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        # Ждем загрузки страницы с итоговой стоимостью
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        
        # Читаем итоговую стоимость
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        
        # Извлекаем числовое значение из текста
        total_value = total_text.replace("Total: $", "")
        
        # Проверяем, что итоговая сумма равна $58.29
        assert total_value == "58.29", f"Ожидалась сумма $58.29, но получено ${total_value}"
        
    finally:
        # Закрываем браузер
        driver.quit()