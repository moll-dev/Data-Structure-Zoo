""" stack.py tester

    thomas moll 2015
"""

import unittest
import stack

class TestStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_push(self):
        test_stack = stack.Stack()
        with self.assertRaises(ValueError):
            test_stack.peek()

        test_value = 22
        test_stack.push(test_value)
        self.assertEquals(test_value, test_stack.peek())

    def test_pop(self):
        test_stack = stack.Stack()
        test_value = 42
        test_stack.push(test_value)

        self.assertEquals(test_value, test_stack.pop())

    def test_peek(self):
        test_stack = stack.Stack()

        test_value = 22
        test_stack.push(test_value)
        self.assertEquals(test_value, test_stack.peek())

    def test_size(self):
        test_stack = stack.Stack()

        test_stack.push('Woo!')
        test_stack.push('This is fun!')
        test_stack.push('Wow! I love reading UnitTests!')

        self.assertEquals(3, test_stack.size)


if __name__ == '__main__':
    unittest.main(verbosity=2)
