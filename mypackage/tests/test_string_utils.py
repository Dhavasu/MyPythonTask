import unittest
from package.string_utils import to_uppercase, to_lowercase, reverse_string, is_palindrome, count_vowels

class TestStringUtils(unittest.TestCase):

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Hello World"), "HELLO WORLD")
        self.assertEqual(to_uppercase("123"), "123")  # Test with numbers

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Hello World"), "hello world")
        self.assertEqual(to_lowercase("123"), "123")  # Test with numbers

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string(""), "")  # Test with empty string

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()))  # Ignore case and spaces

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(count_vowels("123456"), 0)  # Test with numbers

if __name__ == '__main__':
    unittest.main()
