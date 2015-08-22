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
            self.top = StackNode(item)
        else:
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
        if self.top is None:
            raise ValueError()
        else:
            return self.top.data

class StackNode(object):
    """ Look familiar? """
    def __init__(self, item):
        self.data = item
        self.next = None


def check_parenthesis(string):
    stack = Stack()
    # We're using a dict which allows us to do some fun things!
    brackets = {'{':'}', '[':']', '(':')'}

    for character in string:
        # Keys being the left-side brackets
        if character in brackets.keys():
            stack.push(character)

        # Values being the right-side brackets
        if character in brackets.values():
            try:
                other = stack.pop()

                # Check for it's pair using the dict earlier
                if brackets[other] != character:
                    return False

            except ValueError:
                return False

    # If we've made it all the way through without incident
    return True


print check_parenthesis('{[2333][]}')


