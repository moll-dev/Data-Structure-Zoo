import unittest
import collections_and_iterators

""" Collections - TESTS 
    Testing Collections programming examples from collections.py 

    Gabby Ortman 
"""

class TestObjectMethods(unittest.TestCase): 
    def setUp(self): 
        self.singleLinkList = collections_and_iterators.SinglyLinkedList()
        self.doubleLinkList = collections_and_iterators.DoublyLinkedList()

    #test that a newly initialized singly linked list has size 0, null head and null cursor
    def test_empty_single_list(self): 
        self.assertEqual(0, self.singleLinkList.size)
        self.assertIsNone(self.singleLinkList.head)
        self.assertIsNone(self.singleLinkList.cursor)

    def test_contains(self): 
        pass

    def test_append(self): 
        self.singleLinkList.append("Cosmo") 
        self.singleLinkList.append("Allie")
        self.singleLinkList.append("Watson the Award-Winning Betta Fish")
        with self.assertRaises(IndexError):
            self.singleLinkList.__getitem__(3)
        self.singleLinkList.append("Foley")
        self.assertEqual("Foley", self.singleLinkList.__getitem__(3))

    def test_getitem(self): 
        pass 

    def test_setitem(self): 
        pass 

    #test that a newly initated doubly linked list has size 0, null head and null cursor 
    #this shouldn't be any different from the previous test, BUT, what if inheritance was done incorectly? 
    def test_empty_double_list(self): 
        self.assertEqual(0, self.doubleLinkList.size)
        self.assertIsNone(self.doubleLinkList.head)
        self.assertIsNone(self.doubleLinkList.cursor)



if __name__ == '__main__':
    unittest.main(verbosity=2)
