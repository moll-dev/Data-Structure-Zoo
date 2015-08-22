# 4: Generics

![Imgur](http://i.imgur.com/Va8UF2l.png?1)

If you've ever used other languages you'll probably notice that Python doesn't
have strict typing (not strong typing). For example, in Java if you had a sorting
method that worked on an array of Integer objects, you couldn't use it on an array
of strings. However, in Python you can! Consider the following:

```python
    a = 'hello'
    b = 'thomas'

    if a == b:
        print 'They're equal'
    if a < b:
        print 'foo!'
    if a > b:
        print 'bar!'
```

What do you think will be printed to the console? Obviously 'They're equal' won't
be printed. But what about the next two? It's uncertain, maybe they're compared
by length or lexicographically. If you tried it yourself you'll see that it would
print 'foo!' because the Natural Ordering of those strings puts the string 'hello'
before 'thomas'. Natural Ordering is very important in sorting and other algorithms,
integers are simple enough but what about comparing complex objects?

Enter the magic method. You've seen them before; ``__init__`` and ``__str__`` are
two popular ones. They are methods that can be used to define a certain language
operation such as calling str() or in our case any of the comparison operators
(>, >= , <=, !=, ==). In general, you should stick to the ``__cmp__`` method for
establishing a natural order. It takes two arguments ``self`` and ``other``, your
job is to write a method to compare the two and return a value accordingly that
other methods can use.

Now let's compare apples and oranges. Take a look at the generics.py file and
follow along. So first off we have an object, simple enough. It has a string method
and encapsulates a name, radius, and number of seeds. Let's say the Natural Ordering
of our fruit objects was by the number of seeds. The more seeds the better. Now
look and see that I've gone ahead and implemented that logic into the ``__cmp__``
function!

The only rule for ``__cmp__`` is that it returns negative when self < other, zero
when self == other, and positive when self > other. You can see that it does just
that. Let's try it out with some code from a previous section!

```python
    #See also generics.py
    fruit_basket = [ Fruit(random.randint(0,30), 4) for x in xrange(30)]

    quick_sort(fruit_basket, 0, len(fruit_basket)-1)
```

If you run the generics.py, it'll sort our fruit by number of seeds. Without having
to modify our original sorting function! If you're looking for a challenge, try
modifying the Fruit class to sort by radius instead of seeds. That's all for
this section!
