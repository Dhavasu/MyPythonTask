import unittest
from unittest.mock import mock_open, patch
from package.file_utils import read_file, write_file, append_to_file, count_lines

class TestFileUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="line1\nline2\nline3\n")
    def test_read_file(self, mock_file):
        result = read_file("test.txt")
        self.assertEqual(result, "line1\nline2\nline3\n")
        mock_file.assert_called_once_with("test.txt", "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_file(self, mock_file):
        write_file("test.txt", "Hello, World!")
        mock_file.assert_called_once_with("test.txt", "w")
        mock_file().write.assert_called_once_with("Hello, World!")

    @patch("builtins.open", new_callable=mock_open)
    def test_append_to_file(self, mock_file):
        append_to_file("test.txt", "Hello again!")
        mock_file.assert_called_once_with("test.txt", "a")
        mock_file().write.assert_called_once_with("Hello again!")

    @patch("builtins.open", new_callable=mock_open, read_data="line1\nline2\nline3\n")
    def test_count_lines(self, mock_file):
        result = count_lines("test.txt")
        self.assertEqual(result, 3)
        mock_file.assert_called_once_with("test.txt", "r")

if __name__ == '__main__':
    unittest.main()
