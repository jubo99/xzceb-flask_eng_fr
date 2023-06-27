import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Good Day'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye') 

if __name__ == '__main__':
    unittest.main()