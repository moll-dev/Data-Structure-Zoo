# 6: Stack and its applications

![Imgur](http://i.imgur.com/tS3dd5i.png)

WHEW that last section took a lot of work, didn't it? Well you've made it halfway
through the Zoo! Now that you've conquered linked-lists let's move on to a
data structure called the Stack. It's a LIFO (Last in, First out) structure because
the first object gets to leave the structure first. Also, Stacks are called access-limited
because there's no ability to get an item at a certain index, all you have access to
is the top of the stack!

Before we jump in with some nice ASCII diagrams, let's talk functions. A Stack has
a few simple methods that we must implement. ``push()``, ``peek()``, ``pop()``,
``is_empty()``, and ``__len__()``. We've seen ``__len__()`` before, and ``is_empty()``
goes along nicely with the aformentioned. However, what's all this pushing and popping
and peeking about? Let's first take a look at ``push()``. Imagine the stack like a
PEZ dispenser.

```
    |    |
    |    |  <- Stack
    |    |
    ------
```

Let's ``push()`` the number 42 and the number 21 and see what happens!
```
      42                    21
      \/                    \/
    |    |     |    |     |    |     |    |
    |    |  >  |    |  >  |    |  >  | 21 |
    |    |  >  | 42 |  >  | 42 |  >  | 42 |
    ------     ------     ------     ------
```

The 42 "falls" to the bottom of the stack, then the 21 sits on top. Can you guess
what will happen when we call ``pop()``?
```
                 21                    42
                 /\                    /\
    |    |     |    |     |    |     |    |
    | 21 |  >  |    |  >  |    |  >  |    |
    | 42 |  >  | 42 |  >  | 42 |  >  |    |
    ------     ------     ------     ------
```

The order that we pushed the numbers into the stack was the opposite of the order
we popped them. (p.s. We can use ``peek()`` to see what's on top) Before we get
into the applications that a Stack object, we'll talk about the implementation of
one. There are two ways to implement a stack; one being with a list, the other with
a linked-list. We'll use a linked-list because Python's built in list operations make
it too easy. Typically we'd just follow DRY principles and just use List, but you're
supposed to be learning, not writing enterprise code (just yet!).

Let's start by making a top node, a tail node, and a size. Did you forget linked-lists
already? Let's pull up that diagram again. I'll show you what the sequence of events
looks like for the example that we did earlier.

```
    # push(42)
    self.top->[42]->None

    # push(21)
    self.top->[21]->[42]->None

```
