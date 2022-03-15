import unittest
from unittest import TestCase
from Party import Party

class TestParty(TestCase):
    def test_validate(self):
        guest = Party(19, False, True)
        self.assertEqual(guest.validate(), False)

if __name__=="__main__":
    unittest.main()