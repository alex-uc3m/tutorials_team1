import unittest
from unittest import TestCase
from main import add, subtract

class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_subtract(self):
        self.assertEqual(subtract(4, 1), 3)

if __name__=="__main__":
    unittest.main()
