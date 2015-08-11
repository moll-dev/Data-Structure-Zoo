""" Collections

    thomas moll 2015
"""

class SinglyLinkedList(object):
    __next__ = next # For Python 3.X compatability

    def __init__(self):
        self.head = None
        self.size = 0
        self.cursor = None

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    """ Both getitem and setitem represent the magic methods
        for the object[index] and object[index] = other operations
        for linked lists they run in O(n) time making them less
        efficient than a list() for lookups
    """
    def __getitem__(self, index):
        if index > self.size:
            return IndexError()
        else:
            cur = self.head
            for x in xrange(index):
                cur = cur.next
            return cur.data

    def __setitem__(self, index, value):
        if index > self.size:
            return IndexError()
        else:
            cur = self.head
            for x in xrange(index):
                cur = cur.next
            cur.data = value

    def next(self):
        if self.cursor is None:
            raise StopIteration()
        else:
            node = self.cursor.data
            self.cursor = self.cursor.next
            return node

    def append(self, data):
        """ Note: The average time for append is O(n)
            however, insertion is O(1), giving it an
            advantage over arrays.
        """
        if self.head is None:
            self.head = SinglyLinkedNode(data)
            self.cursor = self.head
        else:
            node = self.head
            # This is a common pattern with linked lists
            while node.next is not None:
                node = node.next
            new_node = SinglyLinkedNode(data)
            node.next = new_node
        self.size += 1


class SinglyLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    test = SinglyLinkedList()
    test.append(2)
    test.append(3)
    test.append(4)
