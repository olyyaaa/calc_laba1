import unittest
from functions import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, '+', 1), 3)

    def test_subtraction(self):
        self.assertEqual(calculate(14, '-', 3), 11)

    def test_multiplication(self):
        self.assertEqual(calculate(5, '*', 5), 25)

    def test_division(self):
        self.assertEqual(calculate(10, '/', 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, '/', 0)

    def test_sqrt(self):
        self.assertEqual(calculate(25, '√'), 5)

    def test_power(self):
        self.assertEqual(calculate(2, '^', 4), 16)

if __name__ == "__main__":
    unittest.main()