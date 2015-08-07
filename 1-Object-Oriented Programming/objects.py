""" 1: Object-Oriented Programming

    Some examples of Object-Oriented programming with
    Python

    thomas moll 2015
"""
class Vehicle(object):
    number_of_wheels = None
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Type: '+str(self.__class__)+' Name: '+self.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if len(new_value) > 3:
            self._name = new_value
        else:
            raise ValueError("Name length must be greater than 5 characters")

    def vroom(self):
        raise NotImplementedError("A generic vehicle doesn't make a sound!")


class Car(Vehicle):
    def __init__(self, name):
        super(Car, self).__init__(name)
        self.number_of_wheels = 4

    def vroom(self):
        return 'Put Put Put'


class Truck(Vehicle):
    def __init__(self,name):
        super(Truck, self).__init__(name)
        self.number_of_wheels = 18

    def vroom(self):
        return 'Vroooooom'


# c = Car('Ford')
# print c