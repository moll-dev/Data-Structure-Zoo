""" testing for generics

    thomas moll 2015
"""

import unittest
import generics

class TestGenericsMethods(unittest.TestCase):
    def setUp(self):
        self.apple = generics.Fruit(4, 5, 'Apple')
        self.orange = generics.Fruit(6, 4, 'Orange')
        self.banana = generics.Fruit(4, 3, 'Banana')

    def test_simple_comparisons(self):
        self.assertLess(self.apple, self.orange)
        self.assertEqual(self.apple, self.banana)
        self.assertGreater(self.orange, self.apple)

if __name__ == '__main__':
    unittest.main(verbosity=2)
