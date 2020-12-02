---
export_on_save: 
    html: true 
title: Python Tips
author: Luke Anglin
image: https://files.realpython.com/media/Real-Python-Tips-and-Tricks_Watermarked.ee4e4265c99b.jpg
description: Notes from RealPython's "Python Tricks" book.  Lots of time-savers here! 
topics: Clean code, 
---


# Clean Code 

## Assertions to cover your Ass

Consider a bank account.  The withdrawal should *never* be higher than the balance.  Assertions can prevent someone from 'gaming' your code.  

```python 
def withdraw(amount, balance):
    # Do stuff 

    # Make an assertion
    assert 0 <= amount <= balance 

    # Return something
    return "Withdrawed " + str(amount)
```

Now, this statement will generate an `AssertionError`. 

```python 
withdraw(100, 50)
>> AssertionError
```

Keep in mind: 

* **Not** an exception handling mechanism
* Meant to handle *impossible* conditions.

### Security 

The first caveat to assertions is security.  The `-o` or `-OO` flag being passed to the command line will **disable assertions**.  So, if you're using them for validation schemes . . . good luck.  

As a general rule, your code should *work just fine* if we *remove all assertions*. 

Here's what you <span class="text-danger">shouldn't EVER do</span>

```python 
def withdraw(amount, balance):
    # If this get's disabled, we have problems.  
    assert amount < balance
    balance - amount 
    return True 
```

### raise

What's the solution to that caveat?  `raise` your own exception! 

Have the custom Exception inherit from exception, and use `super().__init__`, passing in any necessary parameters.

```python 
class ScrewYouException(Exception)
"""
Exception raised by losers who disable my assertion flag 
"""

def __init__(self, message = "Re-enable my assertion flag."):
    self.message = message 
    super().__init__(message)
```

```python 
def withdraw(amount, balance):
    # If this get's disabled, we have problems.  
    if (amount < balance)
        raise ScrewYouException
    return True 
```

### Lying Assertions

Tuple truthfulness with non-empty values leads this assertion to never fail! 

```python 
assert(4==5, 'This fails, right?')
```

Countermeasures
* Smoke tests - make sure the assertions *can* fail 
* Code linters 

## Multi-Line Iterables

Because of Git's syntax highlighting, rather than typing: 

```python 
amounts = [1, 2, 3]
```

Type

```python 
amounts = [
    1,
    2,
    3,
]
```

Oh, and did you see that extra comma?  Yeah.  Makes it easier to add/remove items later.  

## Context Managers

The `with` statement is a perfect example.  To make a statement compatabile with the easily readabl `with` syntax, just use an `__enter__(self)` and `__exit__(self)` in the class definition. 

```python 
class Indenter:
    def __init__(self):
        self.level = 0
    def __enter__(self):
        self.level += 1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    def print(self, text):
        print(' ' * self.level + text)
```

If you really want to level up your game, look into the [`contextlib` module](https://docs.python.org/3/library/contextlib.html)

# Generators 

Return **lazy iterators**, which are storage efficient `Iterables`.  

