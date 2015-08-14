
""" Generics

    thomas moll 2015
"""

import random

""" Here i've stolen our quick_sort implementation
notice that I haven't modified anything to make it
work with our fruit object. Pay close attention to
the places in which the '<' is used.
"""
def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: O(n log(n))
    """
    if first < last:
        pos = partition(arr, first, last)
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    pivot = first
    for pos in xrange(first, last):
        # This check happens naturally now that we've defined __cmp__
        if arr[pos] < arr[last]:
            arr[pos], arr[pivot] = arr[pivot], arr[pos]
            pivot += 1
    arr[pivot], arr[last] = arr[last], arr[pivot]
    return pivot


class Fruit(object):
    def __init__(self, seeds, radius, name='fruit',):
        self.name = name
        self.number_of_seeds = seeds
        self.radius = radius

    def __str__(self):
        return 'Fruit:'+str(self.number_of_seeds)

    def __cmp__(self, other):
        # If the object I'm comparing myself to has more seeds
        # then it is considered higher in a list.
        self_value = self.number_of_seeds
        other_value = other.number_of_seeds
        return self_value - other_value


if __name__ == '__main__':

    # Let's make some fruit
    apple = Fruit(3, 4, 'Apple')
    orange = Fruit(7, 3, 'Orange')

    # If an apple has less seeds...
    if apple < orange:
        print 'An apple has less seeds!'
    if apple > orange:
        print 'An orange has less seeds!'

    # Now let's see that sorting is unchanged
    fruit_basket = [ Fruit(random.randint(0,30), 4) for x in xrange(30)]

    print 'Before:'
    for fruit in fruit_basket:
        print str(fruit),',',

    print 'Sorting...'
    # Note: This method works because we're modifiying fruit_basket
    # directly and not returning our sorted array.
    quick_sort(fruit_basket, 0, len(fruit_basket)-1)

    print 'After:'
    for fruit in fruit_basket:
        print str(fruit),',',
