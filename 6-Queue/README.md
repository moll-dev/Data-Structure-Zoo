# 6: Queue

[ Picture of British people waiting in line ]

This next section is about as fun as waiting in line at the grocery mart. A Queue is just as it sounds, it's 
a restricted access list, like Stack but it's a FIFO (First in First Out) structure. This means that Queue
operates just like a line in real life. The method ``queue()`` will add an object to the "back" of the structure, and
``dequeue()`` will pop the first object from the "front" of the structure. We also have a ``peek()`` method that allows
us to see who's at the front of the Queue.

Let's talk internals, there are a couple of different ways that we can implement our Queue, including using a normal
list (but that's too easy in Python), using a circular array, and using a linked list. We're going to use a linked list
but feel free to make your own using the other methods and see if it passes the tests in ``test.py``. Like any good linked
list we're going to need a Node, simple enough, we can use the pattern we used with Stacks. We also require a ``head`` which
we'll call the ``front``, a ``tail`` or ``back`` variable to keep track of the end. We'll also have a ``size()``, ``__str__()``,
and ``clear()`` method to help us test.

