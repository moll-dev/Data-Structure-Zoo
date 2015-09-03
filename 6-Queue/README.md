# 6: Queue

[ Picture of British people waiting in line ]

This next section is about as fun as waiting in line at the grocery mart. A Queue is just as it sounds, it's 
a restricted access list, like Stack but it's a FIFO (First in First Out) structure. This means that Queue
operates just like a line in real life. The method ``enqueue()`` will add an object to the "back" of the structure, and
``dequeue()`` will pop the first object from the "front" of the structure. We also have a ``peek()`` method that allows
us to see who's at the front of the Queue.

Let's talk internals, there are a couple of different ways that we can implement our Queue, including using a normal
list (but that's too easy in Python), using a circular array, and using a linked list. We're going to use a linked list
but feel free to make your own using the other methods and see if it passes the tests in ``test.py``. Like any good linked
list we're going to need a Node, simple enough, we can use the pattern we used with Stacks. We also require a ``head`` which
we'll call the ``front``, a ``tail`` or ``back`` variable to keep track of the end. We'll also have a ``size()``, ``__str__()``,
and ``clear()`` method to help us test.

First, what about ``enqueue()``. When someone first enters a line they're considered the front of the line. However, before
the ``front`` of the line is undefined or ``none``. This becomes our first case for ``enqueue()``, if there is no ``front`` 
we should make the first node or person who enters it both the ``front`` and the ``back``. Check out the diagram below:

Initially we have no ``front`` or ``back``
```
	self.front -> None <- self.back
```

We then add a person named 'Keith' to the ``Queue``
```
				 _______
	self.front-> 'Keith' <- self.back  	
				 -------
```

If you've followed along so far, the other case is quite simple. We have a back node and we simply update
the old back nodes ``next`` variable to point to our new back node. So let's go ahead and add our friend
'Jacob' to the list.

``` 
   				 ____________________
	self.front-> 'Keith'     'Jacob'  <- self.back  	
				 --------------------
```

Notice how we have both the ``front`` and ``back`` nodes connected up now? Let's finish up by setting
Keith's next variable to 'Jacob'. 
``` 
   				 ________________
	self.front-> 'Keith'->'Jacob'<- self.back  	
				 ----------------
```

Now that looks more like a line! Unfortunately this is all for the Queue section, Stack tends to be more useful in Computer Science, however Queue can be used for, well, queuing items to be processed, or sorted. Now on to some more complicated 
data structures!


