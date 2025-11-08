import pytest
import allure

@allure.feature("SauceDemo E-commerce")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemo:
    """Тесты для интернет-магазина SauceDemo."""
    
    @allure.title("Полный цикл покупки в интернет-магазине")
    @allure.description("""
    Тест полного цикла покупки в интернет-магазине SauceDemo:
    1. Авторизоваться как standard_user
    2. Добавить в корзину три товара
    3. Перейти в корзину
    4. Начать оформление заказа
    5. Заполнить информацию
    6. Проверить итоговую сумму
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_complete_purchase_flow(self, login_page, products_page, cart_page, checkout_page):
        """
        Тест полного цикла покупки в интернет-магазине.
        """
        # Данные для теста
        username = "standard_user"
        password = "secret_sauce"
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt", 
            "Sauce Labs Onesie"
        ]
        customer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "postal_code": "12345"
        }
        expected_total = "$58.29"
        
        with allure.step("Авторизоваться пользователем standard_user"):
            login_page.open()
            login_page.login(username, password)
            
            with allure.step("Проверить успешную авторизацию"):
                assert products_page.is_products_page_loaded(), "Страница товаров не загрузилась после авторизации"
                allure.attach("Авторизация прошла успешно", name="auth_status", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step(f"Добавить товары в корзину: {', '.join(products_to_add)}"):
            products_page.add_products_to_cart(products_to_add)
            
            with allure.step("Проверить что товары добавлены в корзину"):
                cart_count = products_page.get_element_text((By.CSS_SELECTOR, ".shopping_cart_badge"))
                assert cart_count == "3", f"Ожидалось 3 товара в корзине, но найдено {cart_count}"
        
        with allure.step("Перейти в корзину"):
            products_page.go_to_cart()
            
            with allure.step("Проверить загрузку страницы корзины"):
                assert cart_page.is_cart_page_loaded(), "Страница корзины не загрузилась"
            
            with allure.step("Проверить содержимое корзины"):
                cart_items = cart_page.get_cart_item_names()
                assert len(cart_items) == 3, f"Ожидалось 3 товара в корзине, но найдено {len(cart_items)}"
                allure.attach(f"Товары в корзине: {', '.join(cart_items)}", name="cart_contents", attachment_type=allure.attachment_type.TEXT)
        
        with allure.step("Начать оформление заказа"):
            cart_page.proceed_to_checkout()
        
        with allure.step("Заполнить информацию для оформления заказа"):
            checkout_page.fill_checkout_info(
                customer_data["first_name"],
                customer_data["last_name"], 
                customer_data["postal_code"]
            )
            checkout_page.continue_to_overview()
        
        with allure.step("Проверить итоговую сумму заказа"):
            total_amount = checkout_page.get_total_amount()
            allure.attach(f"Итоговая сумма: {total_amount}", name="total_amount", attachment_type=allure.attachment_type.TEXT)
            
            assert expected_total in total_amount, f"Ожидалась сумма {expected_total}, но получена {total_amount}"

    @allure.title("Тест авторизации с валидными данными")
    @allure.description("Тест проверяет успешную авторизацию с корректными учетными данными")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_valid_credentials(self, login_page, products_page):
        """
        Тест авторизации с валидными данными.
        """
        with allure.step("Авторизоваться с валидными данными"):
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
        
        with allure.step("Проверить успешную авторизацию"):
            assert products_page.is_products_page_loaded(), "Авторизация не удалась"
            allure.attach("Авторизация прошла успешно", name="login_success", attachment_type=allure.attachment_type.TEXT)