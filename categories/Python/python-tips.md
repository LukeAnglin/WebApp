---
export_on_save: 
    html: true 
title: Python Tips
author: Luke Anglin
image: https://files.realpython.com/media/Real-Python-Tips-and-Tricks_Watermarked.ee4e4265c99b.jpg
description: Notes from RealPython's "Python Tricks" book.  Lots of time-savers here! 
topics: Clean code, 
sources: Python Tricks, by Dan Bader
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

## Underscores 

| Variety                        | Meaning                                                                                        | Convention? | Usage                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------|-------------|--------------------------------------------------------------------------------|
| Single Leading (```_Luke```)         | Mind your own business, I'm private.                                                           | True        | Bans usage only on wildcart imports, which **shouldn't be used anyways**       |
| Single Trailing (```class_```)       | I'm escaping a keyword                                                                         | True        | Used when you have a keyword that you want to use a variable name for          |
| Single Leading dunder (```__Luke```) | I can't be overridden                                                                          | False       | A class where you want the method or attribute to not be changed in subclasses |
| Double Dunder (```__Luke__```)       | I'm magic.  Avoid naming your own variables/methods with a double dunder.  That's Python's job | True        | Use magics **provided by Python**, don't make your own double dunders.         |
| Lonely (```for _ in range(10)```)    | I'm useless in scripts, not so much in iPython shells.                                                                                   | True        | When you're looping.  Use like $\text{ans}$ in iPython shells                                                           |

## Format Strings

The `f"{my_string}"` format string can also do the `.format()` notation with **colon hashtag** syntax:  

```python 
errno = 50159747054
print(f"See the {errno:#x} error on aisle 5")

>> Output: 
See the 0xbadc0ffee error on aisle 5
```

## Template Strings 

These are used for security purposes.  Let's see why.  

```python 
secret_key = 'password'
class Error: 
    def __init__(self):
        pass 
err = Error()
user_input = '{error.__init__.__globals__[secret_key]}'
user_input.format(error=err)

>> Output: 
password 

user_input = '${error.__init__.__globals__[secret_key]}'
Template(user_input).substitute(error=err)

>> Output: 
Error
```

## Format String Summary 

![Format String Summary](https://files.realpython.com/media/python-string-formatting-flowchart.4ecf0148fd87.png)

# Function Frenzy

## Objects <-> Functions

We all know by now functions are first class objects.  But, what about the reverse?

The `__call__` dunder in python allows us some object -> function directionality. 

```python 
class Adder: 
    def __init__(self, n):
        self.n = n 
    def __call__(self, x)
        return self.n + x

plus_8 = Adder(8)
plus_8(2)

>> Output: 10
```

## Lambdas

When should we *use* lambda expressions?  They can be somewhat less readable at times.  

### Sorting 

When we are sorting by a different key, commonly with tuples, lambda functions come in handy.  

```python 
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])

>> Output: 
[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
```

Sorting is **just about the only time** lambda expressions should be used (in my incredibly humble and unbiased opinion).

# Decorators 

First, let's look at what a decorator *really is* 

Here's a wrapper function.  

```python 
def decorator(func):
    return func 

def hello():
    return 'Hello'

hello = decorator(hello)
hello()

>> Output: 'Hello'
```

And, the *exact same thing* with a decorator. 

```python 
@decorator 
def hello(): 
    return 'Hello'

hello()
```

## Wrappers

Generally, you want to actually modify the function, unlike the example above.  Let's try writing a function the just changes whatever the return value is to "Yoda loves Python". 

Oh, and make sure the arguments of the decorated function and the wrapper function match.  If you don't care about arguments, use `*args` and `**kwargs` accordingly. 

```python 
# Wrappers/Decorators
def yoda(func):
    def wrapper(*args, **kwargs):
        return "Yoda loves Python"
    return wrapper 

@yoda
def add(x, y):
    return x+y 

print(add(5, 2))

>> Output: 
Yoda loves Python
```

## Multi-Decoration

You aren't limited to *one* decorator.  Go crazy. 

Keep in mind that decorators **wrap** like it sounds.  Here's Dan's example: 

```python 
@strong
@emphasis 
def greet():
    return 'Hello!'

>> Output: 
<strong><em>Hello!</em></strong>
```
## Uses 

* Logging 
* Access control and Auth Ops 
* Timing and Instrumentation 
* Rate-limiting 
* Caching 

## Metadata

One severely unfortunate aspect of decorators is that they destroy metadata, like docstrings.  To fix this, I recommend *always* using the `@functools.wraps(func)` decorator before defining the wrapper.  

```python 
def decorator(func):
    @functools.wrap(func)
    def wrapper():
        return something 
    return wrapper
```

If you do that, your docstring will be preserved in `__doc__`, like it should! 

# *args and **kwargs 



# Generators 

Return **lazy iterators**, which are storage efficient `Iterables`.  

