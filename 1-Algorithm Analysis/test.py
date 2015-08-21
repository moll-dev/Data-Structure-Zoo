""" algorithms tests
    thomas moll 2015

"""
import unittest
import algorithms

class TestAlgorithms(unittest.TestCase):
    def setUp(self):
        self.list_a = [12,43,60,32,10]
        self.list_b = [43,60,32,10,12]
        self.list_c = [10,12,9,7,40,6]
        self.big_sorted = list(xrange(1000))

    def test_array_equals(self):
        test = algorithms.array_equals(self.list_a, self.list_b)
        self.assertTrue(test)

        test = algorithms.array_equals(self.list_a, self.list_c)
        self.assertFalse(test)

    def test_sequential_search(self):
        item_in_list = 738
        item_not_in_list = -30

        test = algorithms.find_sequentially(self.big_sorted, item_in_list)
        self.assertTrue(test)

        test = algorithms.find_sequentially(self.big_sorted, item_not_in_list)
        self.assertFalse(test)

    def test_binary_search(self):
        item_in_list = 738
        item_not_in_list = -30

        test = algorithms.binary_search(self.big_sorted, item_in_list)
        self.assertTrue(test)

        test = algorithms.binary_search(self.big_sorted, item_not_in_list)
        self.assertFalse(test)

if __name__ == '__main__':
    unittest.main(verbosity=2)
