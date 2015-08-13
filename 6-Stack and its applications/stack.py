""" Stack

    thomas moll 2015
"""

class Stack(object):
    def __init__(self):
        self.size = 0
        self.top  = None

    def __len__(self):
        return self.size

    def __str__(self):
        stack_str = ''
        cursor = self.top
        while cursor.next is not None:
            stack_str+="|"+str(cursor.data)+"|\n"
        stack_str+="----"
        return stack_str

    def push(self, item):
        if self.top is None:
            print 'No head'
            self.top = StackNode(item)
        else:
            #self.top->[item1]->None
            old_top = self.top
            self.top = StackNode(item)
            self.top.next = old_top

            #self.top->[item2]->[item1]->None
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

print s
