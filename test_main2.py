import unittest
from unittest import TestCase
from main import add, subtract, multiply, divide


class Test(TestCase):
    def test_add(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)

    def test_subtract(self):
        self.assertAlmostEqual(subtract(3.5, 2.5), 1.0)

    def test_multiply(self):
        self.assertAlmostEqual(multiply(2.5, 4.0), 10.0)

    def test_divide(self):
        self.assertAlmostEqual(divide(5.0, 2.0), 2.5)


if __name__ == "__main__":
    unittest.main()
