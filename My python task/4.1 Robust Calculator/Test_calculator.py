import unittest
import math
from basic_calculator import Calculator  # Corrected module name and import

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.Add(10, 5), 15)
        self.assertIsNone(self.calc.Add("x", 5))  # Adjusted to handle error case without exception

    def test_subtract(self):
        self.assertEqual(self.calc.Subtract(24, 7), 17)
        self.assertIsNone(self.calc.Subtract(24, "y"))  # Adjusted to handle error case without exception

    def test_multiply(self):
        self.assertEqual(self.calc.Multiply(10, 5), 50)
        self.assertIsNone(self.calc.Multiply("x", None))  # Adjusted to handle error case without exception

    def test_divide(self):
        self.assertEqual(self.calc.Divide(10, 5), 2.0)
        self.assertIsNone(self.calc.Divide("x", 5))  # Adjusted to handle error case without exception
        self.assertIsNone(self.calc.Divide(10, 0))   # Adjusted to handle division by zero without exception

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4.0)
        self.assertIsNone(self.calc.square_root("16"))  # Adjusted to handle error case without exception

    def test_exponentiate(self):
        self.assertEqual(self.calc.exponentiate(2, 3), 8)
        self.assertIsNone(self.calc.exponentiate("2", 3))  # Adjusted to handle error case without exception

    def test_logarithm(self):
        self.assertAlmostEqual(self.calc.logarithm(100), 4.605170185988092)
        self.assertIsNone(self.calc.logarithm(-100))  # Adjusted to handle error case without exception
        self.assertIsNone(self.calc.logarithm(0))  # Adjusted to handle error case without exception


if __name__ == '__main__':
    unittest.main()
