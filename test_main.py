import unittest
from unittest import TestCase
from main import add

class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__=="__main__":
    unittest.main()