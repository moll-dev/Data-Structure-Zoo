# 5: Collections and Iterators

[ put list or something idk ]

Collections, or Data Structures are simply a way to store elements of the same type.
We can establish rules as to what and how items are stored in our collection.
Should the list have a size limit? Should it allow None objects? Are the elements ordered?
Can elements have multiple sucessors? Should access be limited? These will all be answered in the next couple of sections.
We've already used a collection in Python called ``list()``.

As we've seen with ``list()``, there are a few methods that we need when creating our own
collection: ``append()``, ``__len__``, ``__contains__``, and ``__iter__``. These methods
allow us add items to, size up, and search the collection. Let's jump into the different
types! Note: We are going to skill Array-based collections because well List already does
this for you.


### Singly-Linked Lists
Hopping right into the slightly more difficult stuff, Singly-linked lists (not to be confused with ``list()``)are a different
way to thing about organizing data. Think about a simple toy train with wheeled boxes
and string tying them together. Each box can hold something different and the string gives
a distinct Natural Order to the train. Below is a more diagram like way of describing it.

```
    self.head->[item1]->[item2]->[item3]->None
```

To make something like this in Python we'll need two things: a container, and a node.
The container will keep track of the head of the list, it's size, and it's iterator. The
node will hold the data and a reference to the next node in the list. Now on to the methods
the ``__iter__`` method is easy enough, just ``return self`` should do. For append, use a
``while`` loop to iterate to the end of the list (that is until you find a None). Then
make a new object and tell the last object to point to it.

### Iterators for Singly-Linked Lists
How do we then use the ``for item in list:`` piece of syntactic sugar on our new list?
We use an interator! Now currently there are 4 ways to add iterative capabilities to
a collection in Python. I'll go over one of the easier for Singly-Linked lists and
leave the more complicated one for the Doubly-Linked list. For our basic iterator method
``__iter__`` we simply write ``return self``. Now we can implement the ``next()`` method,
it involves holding our place via a cursor variable, then returning it's data when ``next()`` is
called and jumping to the next element using the next variable. Like below:

```
            self.cursor
                 \/
    self.head->[item1]->[item2]->[item3]->None

    [ object.next()  is called ]

                      self.cursor
                          \/
    self.head->[item1]->[item2]->[item3]->None
```

Now before we move on to Doubly-linked lists, I hope you haven't forgotten your Big-O notation!
The reason we would use a linked-list over a normal list comes down to average running time.
While ``list()`` takes O(1) time for an access operation, it takes O(n) time for Insertion,
and Deletion. Link-lists on the other hand take O(n) for access and O(1) time for Insertion,
and Deletion, making them better candidates if your data structure was constantly expanding or
shrinking!

### Doubly-linked lists
Alright, let's move on to Doubly-linked lists. Since you get the gist of Singly-linked lists,
Doubly-linked ones are easy. You just add an attribute to your node that points backwards
to the item before it. Pretty simple right? This allows us to delete objects more easily, and
to iterate backwards as well.

```
                 _____    _____    _____
    self.head|->|item1|->|item2|->|item3|->None
             |<-|_____|<-|_____|<-|_____|
```

We'll write a new method called insert (which was purposefully left out of the Singly-Linked list). 
This one will insert a new node at the given index and move the references of other nodes to fit.

