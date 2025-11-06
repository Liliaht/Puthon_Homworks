import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from typing import Generator

@pytest.fixture(scope="function")
def driver() -> Generator:
    """
    Фикстура для инициализации и закрытия веб-драйвера.
    
    Yields:
        WebDriver: Экземпляр веб-драйвера Chrome
    """
    with allure.step("Инициализация веб-драйвера Chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Для CI/CD
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
    yield driver
    
    with allure.step("Закрытие веб-драйвера"):
        driver.quit()

@pytest.fixture
def login_page(driver):
    """Фикстура для страницы авторизации."""
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def products_page(driver):
    """Фикстура для страницы товаров."""
    from pages.products_page import ProductsPage
    return ProductsPage(driver)

@pytest.fixture
def cart_page(driver):
    """Фикстура для страницы корзины."""
    from pages.cart_page import CartPage
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver):
    """Фикстура для страницы оформления заказа."""
    from pages.checkout_page import CheckoutPage
    return CheckoutPage(driver)

@pytest.fixture
def calculator_page(driver):
    """Фикстура для страницы калькулятора."""
    from pages.calculator_page import CalculatorPage
    return CalculatorPage(driver)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    """
    Хук для получения результата выполнения теста и прикрепления скриншотов при падении.
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )