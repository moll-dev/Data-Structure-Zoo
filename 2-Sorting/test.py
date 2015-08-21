""" 3: Sorting test file

    thomas moll 2015
"""

import unittest
import sorting

class TestSortingMethods(unittest.TestCase):
    def setUp(self):
        self.unordered = [4,14,6,21,11,9,7,5]
        self.ordered =   [4,5,6,7,9,11,14,21]
        self.unordered_with_dupes = [4,5,6,7,6,5,4,5]
        self.ordered_with_dupes =   [4,4,5,5,5,6,6,7]

    def test_static_sorts(self):
        # Note: None of these methods should affect the original lists!
        original = self.unordered

        sorting.selection_sort(self.unordered)
        self.assertEqual(original, self.unordered)

        sorting.insertion_sort(self.unordered)
        self.assertEqual(original, self.unordered)

        sorting.merge_sort(self.unordered)
        self.assertEqual(original, self.unordered)

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
        orig1, orig2 = num1, num2
        ans =  [1,2,4,5,6,7,9,20,23]

        test = sorting.merge(num1, num2)
        self.assertEqual(test, ans)

        self.assertEqual(orig1, num1)
        self.assertEqual(orig2, num2)

    def test_quick_sort(self):
        test = self.unordered
        test_with_dupes = self.unordered_with_dupes

        sorting.quick_sort(test, 0, len(test)-1)
        sorting.quick_sort(test_with_dupes, 0, len(test_with_dupes)-1)

        self.assertEqual(test, self.ordered)
        self.assertEqual(test_with_dupes, self.ordered_with_dupes)

    def test_partition(self):
        test = self.unordered
        ans = [4, 5, 6, 21, 11, 9, 7, 14]
        pivot_ans = 1

        pivot = sorting.partition(test, 0, len(test)-1)

        self.assertEqual(ans, test)
        self.assertEqual(pivot, pivot_ans)

if __name__ == '__main__':
    unittest.main(verbosity=2)
