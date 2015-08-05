""" 1: Object-Oriented Programming

    Some examples of Object-Oriented programming with
    Python

    thomas moll 2015
"""

class MyObject(object):
    def __init__(self):
        self.my_member_variable = 'buh'
        self._fancy_variable = 0

    def say_hello(self):
        print 'hello',self.my_member_variable,'!'

    @property
    def fancy_variable(self):
        return self._fancy_variable

    @fancy_variable.setter
    def fancy_variable(self, new_value):
        if new_value >= 0:
            print new_value
            self._fancy_variable = new_value
        else:
            raise ValueError("Value needs to be greater than 0")


class Vehicle(object):
    def __init__(self, name):
        self.name = name


obj = MyObject()
print obj.my_member_variable
obj.fancy_variable = 5
obj.fancy_variable = -3
obj.say_hello()
