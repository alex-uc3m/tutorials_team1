import unittest
from unittest import TestCase
from main import add, subtract, multiply, divide

class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_subtract(self):
        self.assertEqual(subtract(4, 1), 3)
        
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)

if __name__=="__main__":
    unittest.main()
