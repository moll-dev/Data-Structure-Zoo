""" 2: Algorithms

    thomas moll 2015
"""
import time, random

def find_sequentially(arr, item):
    """ Sequential Search
        Complexity: O(n)
    """
    for value, i in enumerate(arr):
        # Check each item in the list
        if item == value:               #Runs N number of times
            return True
    return False

def binary_search(arr, item):
    """ Binary Search
        Complexity: O(log(n))
        Only works on sorted arrays
    """
    first = 0
    last = len(arr)-1
    found = False

    # Note that first and last will get closer!
    while first <= last and not found:
        # Divide problem set
        mid = (first+last)//2
        if arr[mid] == item:
            found = True
        else:
            # Decide which half to search next
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

def array_equals(a, b):
    """ Checks to see that two arrays
        are completely equal, regardless of order
        Complexity: O(n^2)
    """
    i = 0
    # Check all values in A
    while i < len(a):                # This loop runs N times
        flag = False
        j = 0
        # Search for that value in B
        while j < len(b):            # This loop runs N times
            if a[i] == b[j]:
                flag = True
                break
            j+=1
        if not flag:
            return False
        i+=1
    return True

# Below are some speed tests comparing sequential to binary search
if __name__ == '__main__':

    print 'Given an array of a million ordered ints...'
    big_o_list = list(xrange(1000000))

    item = random.randint(0, 1000000)
    print 'Finding',item,'using sequential search'

    t0 = time.time()
    find_sequentially(big_o_list, item)
    t1 = time.time()
    total = t1-t0

    print 'Found',item,'in',total,'MS'

    item = random.randint(0, 1000000)
    print 'Finding',item,'using binary search'

    t2 = time.time()
    binary_search(big_o_list, item)
    t3 = time.time()
    total = t2-t3

    print 'Found',item,'in',total,'MS'
