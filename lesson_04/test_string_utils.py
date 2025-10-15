import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def test_capitalize_first_letter(self):
        """
        Тестирование метода capitalize_first_letter.
        Примеры использования:
        StringUtils.capitalize_first_letter("hello") -> "Hello"
        StringUtils.capitalize_first_letter("") -> ""
        StringUtils.capitalize_first_letter("a") -> "A"
        """
       
        self.assertEqual(StringUtils.capitalize_first_letter("hello"), "Hello")
        self.assertEqual(StringUtils.capitalize_first_letter("world"), "World")
        self.assertEqual(StringUtils.capitalize_first_letter("a"), "A")
       
        self.assertEqual(StringUtils.capitalize_first_letter("Hello"), "Hello")
        
        self.assertEqual(StringUtils.capitalize_first_letter(""), "")

    def test_reverse_string(self):
        """
        Тестирование метода reverse_string.
        Примеры использования:
        StringUtils.reverse_string("hello") -> "olleh"
        StringUtils.reverse_string("") -> ""
        StringUtils.reverse_string("a") -> "a"
        """
        
        self.assertEqual(StringUtils.reverse_string("hello"), "olleh")
        self.assertEqual(StringUtils.reverse_string("abc"), "cba")
        self.assertEqual(StringUtils.reverse_string("a"), "a")
        
        self.assertEqual(StringUtils.reverse_string(""), "")

    def test_is_palindrome(self):
        """
        Тестирование метода is_palindrome.
        Примеры использования:
        StringUtils.is_palindrome("madam") -> True
        StringUtils.is_palindrome("A man a plan a canal Panama") -> True
        StringUtils.is_palindrome("hello") -> False
        StringUtils.is_palindrome("") -> True
        """
       
        self.assertTrue(StringUtils.is_palindrome("madam"))
        self.assertTrue(StringUtils.is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(StringUtils.is_palindrome("racecar"))
        self.assertTrue(StringUtils.is_palindrome(""))
        
        self.assertFalse(StringUtils.is_palindrome("hello"))
        self.assertFalse(StringUtils.is_palindrome("Python"))
        self.assertFalse(StringUtils.is_palindrome("OpenAI"))

if __name__ == '__main__':
    unittest.main()