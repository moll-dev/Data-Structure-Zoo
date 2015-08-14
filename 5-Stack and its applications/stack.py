""" Stack

    thomas moll 2015
"""

class Stack(object):
    def __init__(self):
        self.size = 0
        self.top  = None

    def __len__(self):
        return self.size

    def push(self, item):
        if self.top is None:
            print 'Added new',item
            self.top = StackNode(item)
        else:
            print 'Added',item
            #self.top->[item1]->None
            item1 = self.top
            item2 = StackNode(item)

            #self.top->[item2]->[item1]->None
            self.top = item2
            item2.next = item1

        self.size += 1

    def pop(self):
        if self.top is None:
            raise ValueError()
        else:
            top_data = self.top.data
            # Skip over the top and set the next to the top
            self.top = self.top.next
            self.size -= 1
            return top_data

    def peek(self):
        return self.top.data


class StackNode(object):
    """ Look familiar? """
    def __init__(self, item):
        self.data = item
        self.next = None


s = Stack()
s.push(42)
s.push(21)

print s.pop()
print s.pop()
