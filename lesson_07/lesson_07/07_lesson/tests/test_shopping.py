import pytest
from pages.login_page import LoginPage

class TestShopping:
    def test_total_amount_after_checkout(self, driver):
        # Открываем сайт и авторизуемся
        main_page = (LoginPage(driver)
                    .open()
                    .enter_username("standard_user")
                    .enter_password("secret_sauce")
                    .click_login())
        
        # Добавляем товары в корзину и переходим в корзину
        cart_page = (main_page
                    .wait_for_load()
                    .add_all_required_products()
                    .go_to_cart())
        
        # Переходим к оформлению заказа
        checkout_page = (cart_page
                        .wait_for_load()
                        .click_checkout())
        
        # Заполняем форму и получаем итоговую стоимость
        total_amount = (checkout_page
                       .wait_for_load()
                       .fill_personal_info("Иван", "Петров", "123456")
                       .click_continue()
                       .wait_for_summary_load()
                       .get_total_amount())
        
        # Проверяем итоговую сумму
        assert total_amount == "58.29", f"Ожидалась сумма 58.29, но получено {total_amount}"