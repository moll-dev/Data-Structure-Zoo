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
    # Make one last check that we don't have any extras
    if stack.size != 0:
        return False
    else:
        # If we've made it all the way through without incident
        return True

def postfix_eval(string):
    ''' Here we setup a dictionary relating the characters of 
        operations to lambda functions. It's similar to saying:
        
        def add(a,b):
            return a + b

        and then doing:

        print add(4,5)
        >>> 9

        The add function can also be accessed via the ``operator``
        module.
    '''

    stack = Stack()
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b, 
           '/': lambda a, b: a / b,
           '%': lambda a, b: a % b,
           '^': lambda a, b: a ** b,}

    # Split the string into a list using spaces
    tokens = string.split(' ') 

    for character in tokens:
        # Check if it's an operator
        if character in ops.keys():
            try:
                # Get our last two values
                right = stack.pop()
                left = stack.pop()

                # Calculate and accumulate it
                result = ops[character](left, right)
                stack.push(result)

            # If there aren't enough operands, raise it.
            except ValueError, e:
                raise e
        else:
            # Else it's either a number or garbage
            try:
                # It'll raise an exception if it can't parse it.
                value = int(character)
                stack.push(value)

            except ValueError, e:
                raise e

    # If we have too many operands or operators
    if stack.size > 1:
        raise ValueError()

    return stack.pop()



