---
export_on_save:
    html: true
title: Python's Forgotten Beauties
author: Luke Anglin 
image: https://data-flair.training/blogs/wp-content/uploads/sites/2/2018/03/Python-itertools-01-1-1-1200x720.jpg
description: Here lies some of hidden gems of the Python, as well as some things I (and others) tend to forget.  
topics: Itertools, debugging, pprint, testing, functions for each datatype, file extraction, os module, and so, much, MORE!
sources: Python Basics, A Practical Introduction to Python 3
publish: True
---

# Help/Docs 

The `help(function)` returns a function's docstring.  

The `dir(module)` gives a list of the functions and variables in a module. 

# Debugging 

## pprint 

The `pprint` module has helpful data structure printing functions.  

```python
import pprint as pp 

pp.pprint(my_dictionary)
```

# Testing 

## unittest 

Steps: 
1. `import unittest`
2. Create a class called `Test<myTest>` that is descriptively describing what you are testing. 
3. Have it inherit from the `TestCase` class 
4. Create test methods, making sure to add `self` as the first argument. 
5. `self.<some-assertion>`
6. End with: 
```python 
if __name__ == 'main':
    unittest.main()
```

Example from the [unittest docs](https://docs.python.org/3/library/unittest.html#basic-example)

```python 
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

## doctest 


Super cool if you're building something where you really want to make some clear examples.  Parses docstring for example code resembling an iPython session and conducts the tests. Best shown by example from [the docs](https://docs.python.org/3/library/doctest.html)

```python
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## pytest 

# Strings

## f-Strings 

[f-Strings](https://realpython.com/python-f-strings/) have a whole host of uses.  A couple common ones are inline bracket notation with evaluated expressions, and also aligning printed content.  

## In 

The `in` operator can be used to see if a character, or sequence of characters, exists in a string.  

```python
if '.html' not in string 
    continue
```

## Split and partition

Essentially the same.  Note that `partition()` requires a delimiter while `split()` does not, and `partition()` returns the delimiter in the output. 

```python
name = 'Luke Anglin' 
split_name = name.split(' ')
partitioned_name = name.partition(' ')
print(f"With split: {split_name}")
print(f"With partition: {partitioned_name}")

>> Output: 
>> With split: ['Luke', 'Anglin']
>> With partition: ('Luke', ' ', 'Anglin')
```

## Slicing

### Iteration by a $c$

One can iterate by a certain amount.  Say we want to iterate every two letters.  

```python 
hello = 'hello'
print(hello[1:len(hello):2])

>> Output: el
```

### Char Change 

Strings are immutable.  Slicing allows us to change a single character. 

The syntax takes the first slice up to the index we want to change.  Then, concatenate the new char, and add the remaining characters.

```python
name = 'Lake'
name_fixed = name[:1] + 'u' + name[2:]
print(name_fixed)
>> Output: Luke
```

# Lists

## Copying 

### Shallow 

A shallow copy is what is generally used.  It copies the references of all sublists.  This is similar to the `copy()` method for other objects. 

```python 
new_list = list_1[:]
```

### Deep 

`deepcopy()` is used when lists are multi-dimensional.  Values are copied, not references.  

## Random 

![](/static/assets/media/Lists-Random.png)

# Tuples 

Immutable lists.  When is this useful?  Consider a dictionary.  Tuples might be used as the keys.  

```python
grades = { ('Luke', 'five'): 95, . . .}
```

# Sets 

Enclosed in curly braces.  Convert lists to sets with the `set` function. 

```python 
my_set = {1, 2, 3}
a_list = [1, 2, 3, 3, 2, 1]

my_same_set = set(a_list)

```

Note that converting a <span class="keyword1">list to a set</span> will <span class="keyword1">remove all repeats</span>

## Operations 

![SetOps](/assets/SetOps.png)

# Enumerate and Zip

`enumerate` takes some list and returns each value with an indices, in pairs.  `zip` is essentially the opposite.  

Note that **neither produce lists** with tuples.  In order to get a list, you have to use the `list` function.  

One use of `zip` is to create dictionaries from two lists.  

```python
names = ['Luke', 'Casey']
grades = [95, 50]
gradebook = dict(zip(names, grades))
print(gradebook)

>> Output: {'Luke': 95, 'Casey': 50}
```

# OS  

## Split 

To retrieve a tuple of the directory and filename, use `split()`

```python
import os

filepath = 'C:/users/lib/run.exe'
os.path.split(filepath)
>> Output: ('C:/users/lib', 'run.exe')
```

## Basename and Dirname

Retrieves *just* the file name (the first index of the `split` function).

```python
import os

filepath = 'C:/users/lib/run.exe'
os.path.basename(filepath)
>> Output: run.exe
```

In contrast, `dirname` returns just the directory (the zero index of the `split` function)

## Walk 

``walk`` is recursive.  It returns a tuple of the `(path, subdirectories, files)` and takes a filepath parameter.  

```python 
for path, dirs, files in os.walk('MLProjects'):
    # Do things
```

## Running

The `.system` function is used to run a program.  
```python 
import os 

# Change directory to where the .exe is located 
os.chdir('usr/evilpath')

# Run it 
os.system('evil.exe')
```

## Quitting 

Maybe I screwed up my recursive fibonnacci sequence.  To quit it, I have to import `sys` and use the `.exit()` function.  

```python
import sys 
fibonnaci()

# uh oh, infinite recursion happening, what do I do?

sys.exit()
```

## File Extraction 

One example is the `zipfile` module and it's `extractall` method.  Probably best that you use some other [resources](http://piorkowski.ca/rev/2016/01/python-zipfile-and-tarfile/) on this, as it can get complicated.  

# RegEx

You know RegEx.  But do you know Python RegEx?  Here's an intro. 

Use the letter `r` to prefix the string like you do `f` for format strings

I have it bookmarked, but here's my favorite [RegEx tester](https://regexr.com/)

To transition it to Python more seamlessly, [this site](https://regex101.com/quiz) has a dedicated Python section of RegEx. 

## Sub 

Use the `sub(pattern, replacement, string)` function to replace strings based on regex patterns. 

```python 
import re
re.sub(r'uke', 'ame', 'Luke')
>> Output: 'Lame'
```

## Cheatsheet

No reason to go through RegEx again.  Here's a [cheatsheet](https://www.debuggex.com/cheatsheet/regex/python) for Python-flavored RegEx, but it seems like it's the same as what I've already learned.

Additionally, here's a handy chart. 

![RegEx Chart](../../static/assets/media/Python-RegEx.png)

![RegEx Example Chart](../../static/assets/media/Python-RegEx-2.png)

## Groups 

The normal grouping with parentheses from regular RegEx applies, but Python allows us some other cool features.  

I'm stealing the example from the book on this one, credit to Dan Bader.  

```python 
def modify(match):
    letter = match.group()
    return letter.lower()
re.sub(r'([A-Z])[a-z]', modify,'PEACH Apple ApriCot')
>> Output: 'PEACH apple apricot'
```

## Other Functions 

* `findall` - return all matches 
* `split` - analagous to string splitting
* `search` - returns a `Match` object if the match is found in the string 
    * To use the groups: 
    ```python 
    match = re.search(r'([ABC])(\d)', '= A3+B2+C8')
    match.group()
    match.group(1)
    >> Output: 'A3'
               'A'
    ```

## finditer 

Gives us a list to loop through our matches.  

```python 
for s in re.finditer(r'([AB])(\d)', 'A3+B4'):
    print(s.group(1))

>> Output: A 
           B
```

## compile 

An efficiency function when reusing the same pattern often, which is a common case.  

```python 
pattern = re.compile(r'[AB]\d')
pattern.sub('*', 'A3+B4')

>> Output: '*+*'
```

# Storage/Efficiency 

## Sparse Matrices 

Use dictionaries to store non-zero locations. 

## array 

The `array` module of Python allows you to only store a certain datatype, making it more efficient.  

As we know, `numpy` and `scipy` have similar applications. 

## Numpy vs scipy

Scipy is a numpy extension.  It is numpy and more; think of MATLAB housed in a Python module - that's Scipy. 

# Base Conversion 

Maybe it will come in handy.  

* `hex(int)`
* `oct(int)`
* `bin(int)`
* `int(any base)`

When using int: 

* Hex values take the $0x$ prefix 
* Oct values take the $0o$ prefix 
* Binary values take the $0b$ prefix

Or, even easier, specify the number and then the base number as the second arg. 

```python 
int('1011101101', 2) # Converts from binary

>> Output: 749
```

# iPython 

## _

The underscore holds *ans* 

## Logs 

In Python, $ln$ is $log$.  Strange, yes, but if you want to change this, just do `ln = log` 

## Summations 

Just some advanced syntax with the `sum` function.  

Say we want to sum $\sum_{n=1}^{\infty} \frac{1}{n^2-1}$

```python 
sum([1/(n**2-1) for n in range(2,1000)])

>> Output: 0.7489
```

And that's $\approx \frac{3}{4}$.  

# Functions 

## First class 

Functions can be assigned to variables, copied, used as args, etc.  We know this, but what are the implications? 

### List Chaining 

We can put functions in a list and iterate through the list on an argument, effectively applying multiple functions at a time. 

```python
def f(x): 
    return x+2 

def g(x): 
    return x+3

function_chain = [f, g]
x=0
for function in function_chain:
    x = function(x)

print(x)

>> Output: 5
```

## Lambda Functions 

For the sake of completeness, I include these, but I find them less readable and generally just a way to show off.  You could generally just include another argument.  Sometimes they do come in handy though.  

```python 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

>> Output: 22
```

Essentially, the purpose of lambda functions is to create a new function based on some input. 

## List Comprehension

A couple functions have been replaced by List Comprehension, but are still worth knowing 

### map 

Equivalent of Panda's `apply` function.  

```python 
# With map 
L =list(map(len, ['this','is','a','test']))

# With List Comprehension 
L = [len(word) for word in ['this','is','a','test']]
```

### filter 

Returns the Iterable where the function evaluates to `True` 

```python 
# With filter 
L =list(filter(lambda x: len(x)>2, ['this','is','a','test']))

# With List Comprehension
L = [word for word in['this','is','a','test']if len(word)>2]
```

## reduce 

This one **can't** be easily replaced by List Comprehension (yet . . .)

Applies a function cumulatively to an Iterable. 

```python 
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
```

Note that the final part of the Iterable is generally going to be **one plus whatever is natural**. 

## operator Module 

Faster than regular anonymous/lambda functions.  Everything from addition to slicing.  

Rather than using 

```python 
total = reduce(lambda x, y: x+y, range(1,101))
```

we can use 

```python 
from operator import add 
total = reduce(add, range(1, 101))
```

## Optional args 

### No keywords

Use an asterisk * to collect multiple non-keyword, optional arguments into a tuple. 

```python 
def sum(*nums): 
    sum = 0; 
    for num in nums: 
        sum+=num 
    return sum 
print(sum(3,4), sum(8,9,3), sep='\n')

>> Output: 7
           20
```

On the other

## kwargs 

Often, you want to use the `.items()` function on the `kwargs` in order to iterate through it like a `dict`. 

What is stored in `**kwargs` is a dictionary mapping keys to values.  

```python 
def upper(**kwargs): 
    for keyword, value in kwargs.items(): 
        print(f"{keyword}: {value.upper()}")

upper(name = 'Luke')

>> Output: name: Luke
```

## ** and * 

Commonly, you see this sort of notation for `*args` and `**kwargs` in a function, like this: 

```python 
# Positional args, *args and/or default args, *kwargs
def f(a, b, *c, d=5, **e)
```

But, you can also use them for unpacking tuples to be **used as arguments**.  

```python 
def f(a,b):
    print(a+b)
args = [(1,2), (3,4), (5,6), (7,8), (9,10)]
i = eval(input('Enter a number from 0 to 4:'))

f(*args[i])
```

```python 
Enter a number from 0 to 4: 
3

>> Output: 15
```


## Ordering

`*args` before `**kwargs`.  Simple as that.

## Variable retention

You can give a function sort of static attributes.  

```python 
def add_members():
    add_members.members += 1
    print(add_members.members)
# Initialize that var 
add_members.members = 0

add_members()
add_members()

>> Output: 1
           2
```

# Itertools and collections

Note that many of the features of these return `iterator` objects rather than lists.  Permutations are one example that we'll see right here. 

## Permutations

One cool thing is rather than just passing a list to permutations and getting the rearrangements, you can pass an int as an optional second argument and get all of the permutations of that subset.  

Make sure to convert with `list`, because an `iterator` is returned. 

```python 
from itertools import permutations

# No second argument
list(permutations([1,2,3]))

>> Output:  
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# With second integer arg 
list(permutations([1,2,3], 2))

>> Output: 
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

```

## Combinations

Same syntax for combinations where you **can't repeat**.  If you want to repeat, just change it to `combinations_with_replacement()`

## Cartesian Product 

Wonderfully simple.  Just use `product()`

```python
from itertools import product 
[''.join(seq) for seq in product('abc', '123')]

>> Output: 
['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
```

# Sorting

There are two big functions in this category.  `sort()` and `sorted()`

## sort()

`sort()` takes three optional `kwargs`.  

```python
L.sort(cmp = None, key = None, reverse = False)
```

Realistically, only `key` matters.  It allows you to sort by applying some function.  For example, you could pass `len` (**no parentheses**), the function object, to that parameter and it would sort by the length of the values in the list.  

```python 
L = ['hello', 'supercalifragilisticexpialadocious']
L.sort(key = len, reverse = True)

>> Output: 
['supercalifragilisticexpialadocious', 'hello']
```

Note that the `Iterable` is sorted *in place* 

## sorted()

`sorted()` is similar, but you pass an `Iterable` as the first argument, and the `Iterable` is not sorted in place. 

## Groupby 

Useful for seeing how many of similar things occur in an `Iterable`.  Generates a `groupby` `iterator` object, so you must convert with a `list()`. 

Generally, you want to `sort()` the collection first.  Let's see why.  

Here's a **non-sorted** example. 

```python 
L = [0, 0, 1, 1, 1, 0, 0, 4, 4, 4]
for key, group in groupby(L): 
    print(key, ':', list(group))

>> Output: 
0 : [0, 0]
1 : [1, 1, 1]
0 : [0, 0]
4 : [4, 4, 4]
```

As we can see, the zeroes get repeated.  

If we sort, though . . . 

```python 
L.sort()
for key, group in groupby(L): 
    print(key, ':', list(group))

>> Output: 
0 : [0, 0, 0, 0]
1 : [1, 1, 1]
4 : [4, 4, 4]
```

Generally, you'd probably take the `len()` of those lists and see how many unique values there are.  

### Optional key param

Additionally, you can specify a `key` parameter to tell groupby how to map the dict more effectively.  This is best explained by a visual.  

```python 
L = ['this','is','a','test','of','groupby']
L.sort(key =len) 
for key, group in groupby(L, len):
    print(key,':',list(group))

>> Output: 
1 : ['a']
2 : ['is', 'of']
4 : ['this', 'test']
7 : ['groupby']
```

## Chain 

This one is **extremely useful**.  If you have a list of lists, or an `Iterable` of other `Iterables`, which is very common, you can flatten it.  

Note that the inner parts of the `Iterable` should be of the same dimension $n$ and you often will need to unpack the `Iterable` by calling something like `*tuple(<Iterable>)`

```python 
import itertools
L = [[1], [2], [1, 2, 3]]
all_nums = list(itertools.chain(*tuple(L)))
print(all_nums)

>> Output: 
[1, 2, 1, 2, 3]
```

## Counter 

The `Counter` class has useful methods for, well, *counting*.  Revolutionary, right? 

```python 
import re 
from collections import Counter 
names = ('LukeLukeLuke')
repetitions = re.findall('Luke', names)
my_counter = Counter(repetitions)
list(zip(my_counter.keys(), my_counter.values()))

>> Output: 
[('Luke', 3)]
```

As you can see, it returns a `dict`.  A couple other cool things about `Counter` include: 

* `most_common(*index/slice)` 
    * Tip:  Use negative slicing to get least common elements
* You can do math on `Counter` objects

## defaultdict 

Allows one to store a default value in the dictionary.  Very useful. 

```python 
from collections import defaultdict
description_dict = defaultdict(lambda: 'Description: ')

descriptions = ['Cool!', 'Boring', '']
count = 0
for description in descriptions: 
    count += 1
    description_dict[count] += description 
print(dict(description_dict))

>> Output: 
{1: 'Description: Cool!', 2: 'Description: Boring', 3: 'Description: '}
```

Okay, not saying that's it's best use.  May have to come up with a better one.  I'm confident it's handy though.  

Don't forget to convert to a `dict` if you want that type of output.  Otherwise, you get some weird Python gibberish before the `dict`. 

# Generators 

Any function containing the keyword `yield` is a generator. These functions don't lose their variables when iterating, and are generally **recursive** functions. 

Generators are often <span class="keyword1">more efficient</span> than regular `Iterables` because they do **not store all values in memory**.  

This comes with one drawback though.  You can only iterate over a generator *once*, because they generate values *on the fly*. 

```python 
generator = (x*x for x in range(3)) 
for value in generator:
    print(value)

>> Output: 
0
1
4
```

## yield 

Similar to return, but for creating generators from functions.  

```python 
def createGenerator():
       mylist = range(3)
       for i in mylist:
       yield i*i

mygenerator = createGenerator()
print(mygenerator) # generators are objects

>> Output: <generator object createGenerator at 0xb8324c38>

for i in mygenerator:
    print(i)

>> Output: 
0
1
4
```

This section and the above section on generators as a whole was inspired by this [Stack Overflow post](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)

# Exceptions 

# try except 

Similar to `try catch` blocks in Java.  Quick example: 

```python 
a = 3 
b = 0 
try: 
    c = a/b 
except ZeroDivisionError: 
    print('Unable to do so.')
except NameError: 
    print('Just showing we can have multiple except blocks')
except: 
    print('We don\'t even need an extension')

print('We\'re all good')

>> Output: 
Unable to do so.
We're all good
```

## else 

You can also use `else` blocks with try.  Maybe you open a file in the `try` block, and read it in the `else` if you don't get an error due to the file not being located. 

Generally, you can just do everything in the `try` though. If you *know* it's not going to fail, put it in an `else`. 

Summary:  If it's not the part raising the exception, put it in the `else` block as convention and good practice. 

![else description](https://static.javatpoint.com/python/images/python-exception-handling2.png)

## finally 

Same as `finally` in all code. 

## with as 

As we've seen from IO ops, `with as` is great for opening files.  

```python 
with open('cool-file.txt') as f: 
    # Do things and don't break my program doing them. 
```

## raise 

Use `raise` when you want to signal <span class="keyword1">your own exceptions</span>! 

```python 
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
```

## Exception Diagram 

See the [docs](https://docs.python.org/3/library/exceptions.html) for descriptions of the `Exception`s 

![Exception Diagram](https://www.programcreek.com/wp-content/uploads/2009/02/Exception-Hierarchy-Diagram.jpeg)



## Exception class 

Exceptions are stored in an `Exception` object.  Access them, and generally store them with an `as`. 

```python 
try: 
    c = 5/0
except Exception as e: 
    print(e)

>> Output: 
division by zero  
```

# Decorators 

Decorators *wrap* functions, modifying their behavior.  They are **syntactic sugar** for inner functions and function objects. 

**decorators.py** 
```python 
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice
```

**real_file.py** 
```python 
from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")

say_whee()

>> Output: 
Whee!
Whee!
```

## *args and **kwargs 

You can't pass arguments to decorators unless you take advantage of these two (assuming the wrapper function, the one you are decorating with, doesn't take any arguments).  

```python 
from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Luke")

>> Output: ERROR MADNESS 
```

But, if we modify the `do_twice` decorator/wrapper function, we'd be fine. 

```python 
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice
```

## Return values 

If you want your decorator to allow return values, make sure you account for this in your wrapper/decorator function.  

```python {highlight=4}
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs) 
    return wrapper_do_twice
```

