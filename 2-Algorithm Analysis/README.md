# 2: Algorithm Analysis

![Imgur](http://i.imgur.com/pL6nSPE.png)

Before we get started with the fun stuff, we need to tackle some math. I'll try
to make it as painless as possible. Let's say we've got a huge list of sorted numbers.
Maybe a million or so. How should we find a number in that list? Well, why don't
we just iterate through and check each value.

```python
# See also in algorithms.py
def find_sequentially(arr, item):
    for value, i in enumerate(arr):
        # Check each item in the list
        if item == value:               #Runs N number of times
            return True
    return False
```

Let's give the number of items in the list an official name called "n". Now we'll
take a look at the function and see home many times various operations are called.
This one is pretty simple because it uses a single ``for`` loop, thus this function
takes N number of times to complete.

The general rule of thumb is that a loop over a list will take O(n) time. The notation callled Big O that I
just used represents the average time that a function will take to complete. It's less
of an exact measurement and more of a good approximation to see if the algorithm you
wrote will scale well with tons and tons of data. Now let's try adding another loop!

```python
# Also in algorithms.py
def array_equals(a, b):
    i = 0
    while i < len(a):                # This loop runs N times
        flag = False
        j = 0
        while j < len(b):            # This loop runs N times
            if a[i] == b[j]:
                flag = True
                continue
            j+=1
        if not flag:
            return False
        i+=1
    return True
```

You'll see that we have nested loops meaning that since the outside loop
runs like normal, that the inside loop makes the entire function run in O(n^2)
time. Which is much slower than linear, given two lists of a million items or so.
Essentially the power of N increases whenever loops are nested. However, what do
you think the running time of two loops running one after another would be? Not
N^2! It would be 2N because each loop is running once.

Back to our item finding problem. Now that we know a bit about how this whole
Big O thing works, let's talk about a better way to search and its running time.
Enter, Binary Search, a method that uses the fact that the array is sorted to
significantly speed up its seach process.

```python
# See more comments in algorithms.py
def binary_search(arr, item):
    front = 0
    back = len(arr)-1
    found = False

    while first <= last and not found:
        mid = (front+back)//2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                back = mid - 1
            else:
                fist = mid + 1
    return found
```

Can you guess what this function's running time is? Let's take a crack at it.
There's a loop, so we can put an n down. However, if you take a look at the condition,
it won't always be iterating through the entire list. In fact everytime an interation
happens the problem set is cut in half. Take the limit as n goes to infinity given ``n/(2^i)``
and you get log(n). Making our function run in O(log(n)) time, and if you graph these
two functions with reasonably large sets of numbers you'll se that n^2 goes to infinity
much quicker than log(n), making this search more efficient.
