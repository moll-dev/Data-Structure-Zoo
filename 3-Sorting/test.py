""" 3: Sorting test file

    thomas moll 2015
"""

import unittest
import sorting

class TestSortingMethods(unittest.TestCase):
    """ Note: None of these methods should affect the original lists! """
    def setUp(self):
        self.unordered = [4,14,6,21,11,9,7,5]
        self.ordered =   [4,5,6,7,9,11,14,21]
        self.unordered_with_dupes = [4,5,6,7,6,5,4,5]
        self.ordered_with_dupes =   [4,4,5,5,5,6,6,7]

    def test_selection_sort(self):
        test = sorting.selection_sort(self.unordered)
        self.assertEqual(test, self.ordered)

        test = sorting.selection_sort(self.unordered_with_dupes)
        self.assertEqual(test, self.ordered_with_dupes)

    def test_insertion_sort(self):
        test = sorting.insertion_sort(self.unordered)
        self.assertEqual(test, self.ordered)

        test = sorting.insertion_sort(self.unordered_with_dupes)
        self.assertEqual(test, self.ordered_with_dupes)

    def test_merge_sort(self):
        test = sorting.merge_sort(self.unordered)
        self.assertEqual(test, self.ordered)

        test = sorting.merge_sort(self.unordered_with_dupes)
        self.assertEqual(test, self.ordered_with_dupes)

    def test_merge(self):
        # Note: merge works in O(n) time assuming that the two lists are SORTED
        num1 = [1,4,6,7,20]
        num2 = [2,5,9,23]
        ans =  [1,2,4,5,6,7,9,20,23]

        test = sorting.merge(num1, num2)
        self.assertEqual(test, ans)

if __name__ == '__main__':
    unittest.main()
