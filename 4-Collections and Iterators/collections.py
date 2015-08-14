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

            # [node] [new_node]->None
            new_node = SinglyLinkedNode(data)

            # [node]->[new_node]->None
            node.next = new_node

        self.size += 1


class SinglyLinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        # DRY: We're just going to inherit this for convinence
        super(DoublyLinkedList, self).__init__()

    def previous(self):
        if self.cursor.prev is None:
            raise StopIteration()
        else:
            self.cursor.prev
            self.cursor = self.cursor.prev
            return self.cursor.data

    def append(self, data):
        """ Note: The average time for append is O(n)
            however, insertion is O(1), giving it an
            advantage over arrays.
        """
        if self.head is None:
            self.head = DoublyLinkedNode(data)
            self.cursor = self.head
        else:
            node = self.head
            # This is a common pattern with linked lists
            while node.next is not None:
                node = node.next
            # A simple change to use the double node
            # and link the previous
            new_node = DoublyLinkedNode(data)
            node.next = new_node
            new_node.prev = node
        self.size += 1

    def insert(self, data, index):
        if index >= self.size:
            raise IndexError()
        if self.head is None:
            self.head = DoublyLinkedNode(data)
            self.cursor = self.head
        else:
            # If this insertion should be an append
            if index == self.size - 1:
                # We've got a method for that!
                self.append(data)
            # If a new head needs to be added
            elif index == 0:
                print 'head'
                #              _____   _____
                # self.head|->|  A  | |  C  |
                #           <-|_____| |_____|
                a = self.head ; print 'a',a.data
                c = DoublyLinkedNode(data)

                #              _____    ______
                # self.head|->|  C  |->|  A  |
                #           <-|_____|<-|_____|
                self.head = c
                c.next = a
                a.prev = c
                self.cursor = self.head
            # It's between two nodes
            else:
                a = self.head
                for x in xrange(index):
                    a = a.next
                #  _____    _____
                # |  A  |->|  B  |
                # |_____|<-|_____|
                b = a.next
                c = DoublyLinkedNode(data)

                #  _____    _____    _____
                # |  A  |  |  C  |->|  B |
                # |_____|  |_____|<-|____|
                b.prev = c
                c.next = b

                #  _____    _____    _____
                # |  A  |->|  C  |->|  B |
                # |_____|<-|_____|<-|____|
                a.next = c
                c.prev = a

        self.size += 1


class DoublyLinkedNode(SinglyLinkedNode):
    def __init__(self, data):
        # Staying DRY!
        super(DoublyLinkedNode, self).__init__(data)
        self.prev = None

if __name__ == '__main__':
    test = DoublyLinkedList()
    test.append(2)
    test.append(3)
    test.append(4)

    test.insert(50, 1)

    for node in test:
        print node,',',
