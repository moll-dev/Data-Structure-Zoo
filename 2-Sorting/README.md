# 3: Sorting

[ Draw picture of some dude trying to sort blocks idk]

Now let's get to something a bit more fun than Big-O and algorithm analysis
from now on we'll be mentioning the amortized time next to any crucial algorithms
or methods. Sorting is used for all sorts of things! As you may well know, computers
can collect way more information than we can process in our life times, so if we
can programmatically sort out what we want, we'll be able to find what we really want.
Google's PageRank is essentially a huge sorting algorithm that helps us find cat
pictures, among other things.

### Simple sorts
Starting out with the most basic types of sorting methods, we have Selection and Insertion
sorts. Two algorithms which I most often confuse because they're so similar!
Selection sort essentially starts at the beginning and searches the rest of the
list for the smallest number then "selects" it. After it finds what it's looking for
it moves to the next number, essentially making a bubble of sorted numbers, cool right?

Insertion sort works in a similar way, in that it saves its place in the array.
However, insertion sort swaps the current item down the list until it the current
item is bigger than the item to its left.

### Recursive sorts using Divide and Conquer

Unfortunately these simple sorts, while being easy to conceptualize, have a generally
terrible average O() time of O(n^2). Let's try tackling a more complex method, such
as Mergesort! It takes advantage of a helper function called Merge which, given two
already sorted lists of items, sorts them into a larger list of sorted items. Using
recursion with this Merge function creates Mergesort. It's running time complexity is
O(n log(n)), which isn't the best but it is a guaranteed running time!

If you're familiar with a Binary search, which uses a divide and conquer algorithm. Quicksort
will be a breeze! With an average run time of O(n log(n)) it's a pretty good one.
Essentially, Quicksort picks a central value (determined various ways) to pivot values around.
This pivot function is similar to Merge, except it separates all values less than the pivot
into the "left" list and all greater than into a "right" list. Done recursively, Quicksort
pivots the entire list then pivots sublists by halving the original list.

That's pretty much it for sorting. We'll cover heapsort after trees have been covered! Protip: sorting
is a traditionally difficult thing for students to wrap their head around (I know it was for me). In order
to become proficient, don't just write out the algorithms, work them out on a white board and see how they
move data around.
