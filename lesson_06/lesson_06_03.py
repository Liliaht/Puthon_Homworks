from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

try:
    # Ждем, когда все 4 картинки станут видимыми
    images = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
    )
    
    # Проверяем, что загрузилось достаточно картинок
    assert len(images) >= 3, "Не загрузилось достаточно картинок"
    
    # Получаем src третьей картинки
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)
    
finally:
    driver.quit()