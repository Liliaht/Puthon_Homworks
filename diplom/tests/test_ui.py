"""
UI тесты для Labirint.ru - дипломный проект
"""
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import config


class TestLabirintUI:
    """Класс UI тестов для сайта Labirint.ru"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, config.TIMEOUT)
    
    def teardown_method(self):
        """Очистка после каждого теста"""
        self.driver.quit()
    
    @allure.title("Поиск книги на латинице")
    @allure.description("Тестирование поиска с использованием латинских символов")
    @pytest.mark.ui
    def test_search_latin(self):
        """Тест поиска с текстом на латинице"""
        with allure.step("Открыть главную страницу"):
            self.driver.get(config.BASE_URL)
        
        with allure.step("Ввести поисковый запрос на латинице"):
            search_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "search-field"))
            )
            search_input.clear()
            search_input.send_keys("python programming")
        
        with allure.step("Нажать кнопку поиска"):
            search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            search_button.click()
        
        with allure.step("Проверить результаты поиска"):
            # Ждем загрузки результатов
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-row"))
            )
            
            # Проверяем что URL содержит поисковый запрос
            assert "python" in self.driver.current_url.lower()
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="search_latin_results",
                attachment_type=allure.attachment_type.PNG
            )
    
    @allure.title("Поиск книги на кириллице")
    @allure.description("Тестирование поиска с использованием кириллических символов")
    @pytest.mark.ui
    def test_search_cyrillic(self):
        """Тест поиска с текстом на кириллице"""
        self.driver.get(config.BASE_URL)
        
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "search-field"))
        )
        search_input.clear()
        search_input.send_keys("программирование")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-row"))
        )
        
        assert "search" in self.driver.current_url
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="search_cyrillic_results",
            attachment_type=allure.attachment_type.PNG
        )
    
    @allure.title("Поиск книги в верхнем регистре")
    @allure.description("Тестирование поиска с текстом в верхнем регистре")
    @pytest.mark.ui
    def test_search_uppercase(self):
        """Тест поиска с текстом в верхнем регистре"""
        self.driver.get(config.BASE_URL)
        
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "search-field"))
        )
        search_input.clear()
        search_input.send_keys("JAVA")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-row"))
        )
        
        assert "java" in self.driver.current_url.lower()
    
    @allure.title("Поиск книги в нижнем регистре")
    @allure.description("Тестирование поиска с текстом в нижнем регистре")
    @pytest.mark.ui
    def test_search_lowercase(self):
        """Тест поиска с текстом в нижнем регистре"""
        self.driver.get(config.BASE_URL)
        
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "search-field"))
        )
        search_input.clear()
        search_input.send_keys("javascript")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-row"))
        )
        
        assert "javascript" in self.driver.current_url.lower()
    
    @allure.title("Поиск книги в смешанном регистре")
    @allure.description("Тестирование поиска с текстом в верхнем и нижнем регистре")
    @pytest.mark.ui
    def test_search_mixed_case(self):
        """Тест поиска с текстом в смешанном регистре"""
        self.driver.get(config.BASE_URL)
        
        search_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "search-field"))
        )
        search_input.clear()
        search_input.send_keys("Data Science")
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        search_button.click()
        
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.products-row"))
        )
        
        assert "data" in self.driver.current_url.lower()
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="search_mixed_case_results",
            attachment_type=allure.attachment_type.PNG
        )


if __name__ == "__main__":
    # Запуск тестов напрямую для отладки
    pytest.main([__file__, "-v"])