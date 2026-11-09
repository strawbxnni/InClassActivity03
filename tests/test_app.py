import unittest
from mult_numbers import mult_numbers

class TestMultNumbers(unittest.TestCase):
    def test_multiply_positive(self):
        self.assertEqual(mult_numbers(2, 3), 6)

    def test_multiply_zero(self):
        self.assertEqual(mult_numbers(5, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(mult_numbers(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
