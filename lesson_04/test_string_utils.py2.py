import pytest
from string_utils import StringUtils

utils = StringUtils()

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),   # Позитивные
    ("Skypro", "Skypro"),   # Позитивные
    ("a", "A"),             # Позитивные
    ("", ""),               # Позитивные (пустая строка)
    ("123abc", "123abc")    # Позитивные (первая буква не обязательно буква)
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),      # Позитивные
    ("skypro   ", "skypro"),      # Позитивные
    ("   skypro   ", "skypro   "), # Позитивные
    ("skypro", "skypro"),         # Позитивные
    ("", ""),                     # Позитивные (пустая строка)
    ("     ", "")                 # Позитивные (только пробелы, возвращается пустая)
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected

@pytest.mark.parametrize("string, char, expected", [
    ("SkyPro", "S", True),             # Позитивные
    ("SkyPro", "o", True),             # Позитивные
    ("SkyPro", "u", False),            # Негативные
    ("hello", "z", False),             # Негативные
    ("", "a", False),                  # Негативные
    ("abc", "", True)                  # Позитивные (пустая строка содержится в любой)
])
def test_contains(string, char, expected):
    assert utils.contains(string, char) is expected

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),           # Позитивные
    ("SkyPro", "Pro", "Sky"),           # Позитивные
    ("hello world", "l", "heo word"),   # Позитивные
    ("abc", "z", "abc"),                # Позитивные (символа нет, возвращается исходная)
    ("test", "", "test"),               # Позитивные (пустой символ, строка без изменений)
    ("", "a", "")                       # Позитивные (пустая строка)
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
