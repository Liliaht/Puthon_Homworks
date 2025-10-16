import pytest
from string_utils import StringUtils

# Создадим экземпляр для тестирования
utils = StringUtils()

def test_capitalize():
    # Позитивные тесты
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("Skypro") == "Skypro"
    assert utils.capitalize("a") == "A"
    assert utils.capitalize("") == ""  # пустая строка
    assert utils.capitalize("123abc") == "123abc"  # первая буква не обязательно буква

def test_trim():
    # Строки с пробелами
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro   ") == "skypro"  # пробелов в конце не трогает
    assert utils.trim("   skypro   ") == "skypro   "  # только в начале
    # Строки без пробелов
    assert utils.trim("skypro") == "skypro"
    # Пустая строка
    assert utils.trim("") == ""
    # Строка только из пробелов
    assert utils.trim("     ") == ""

def test_contains():
    # В строке есть искомый символ
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "o") is True
    # В строке нет искомого символа
    assert utils.contains("SkyPro", "u") is False
    assert utils.contains("hello", "z") is False
    # Пустая строка
    assert utils.contains("", "a") is False
    # Проверка на пустой символ
    assert utils.contains("abc", "") is True  # пустая строка содержится в любой строке

def test_delete_symbol():
    # Удаление существующего символа
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("hello world", "l") == "heo word"
    # Удаление символа, которого нет
    assert utils.delete_symbol("abc", "z") == "abc"
    # Удаление пустого символа
    assert utils.delete_symbol("test", "") == "test"
    # Пустая строка
    assert utils.delete_symbol("", "a") == ""

