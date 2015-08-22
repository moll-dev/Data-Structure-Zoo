""" Collections - TESTS 
    Testing Collections programming examples from collections.py 

    Gabby Ortman 
"""
import unittest 
import collections 

class TestObjectMethods(unittest.TestCase): 
    def setUp(self): 
        print collections.__dict__()
        self.singleLinkList = collections.SinglyLinkedList()

    #test that a newly initialized singly linked list has size 0, null head and null cursor
    def test_empty_list(self): 
        self.assertEqual(0, self.singleLinkList.size)




if __name__ == '__main__':
    unittest.main(verbosity=2)
