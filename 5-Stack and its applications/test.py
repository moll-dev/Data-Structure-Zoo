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

class TestApplications(unittest.TestCase):
    def setUp(self):
        pass

    def test_parenthesis(self):
        well_formed = "[{}[]]((({}[])))"
        not_well_formed = "[[[]]())"

        # WHAT IS C DOING IN THIS REPO????
        well_formed_with_text = ''' while (!feof(autoexec))
                                    {
                                        if (fgets(rline, 256, autoexec))
                                        {
                                            if ((SUCCESS == strnicmp(tline, TAG_1, strlen(TAG_1))) ||
                                                (SUCCESS == strnicmp(tline, TAG_2, strlen(TAG_2))))
                                            {
                                                if ('\n' == LAST_CHAR(rline))
                                                      LAST_CHAR(rline) = NUL;
                                                strcat(rline, (';' == LAST_CHAR(rline) ? "" : ";"));
                                                strcat(strcat(rline, newdir), "\n");
                                            }
                                            fputs(rline, tmp);
                                        }
                                    }
                                '''

        not_well_formed_with_text = "if(something == foo()"

        self.assertTrue(stack.check_parenthesis(well_formed))
        self.assertFalse(stack.check_parenthesis(not_well_formed))
        self.assertTrue(stack.check_parenthesis(well_formed_with_text))
        self.assertFalse(stack.check_parenthesis(not_well_formed_with_text))

    def test_postfix_eval(self):
        eighty_eight = "5 6 + 7 4 3 - + *"
        too_many_operands = "2 3 + 4 6 -"
        too_many_operators = "2 3 + -"

        self.assertEquals(88, stack.postfix_eval(eighty_eight))
        with self.assertRaises(ValueError): 
            stack.postfix_eval(too_many_operands)

        with self.assertRaises(ValueError):
            stack.postfix_eval(too_many_operators)



if __name__ == '__main__':
    unittest.main(verbosity=2)
