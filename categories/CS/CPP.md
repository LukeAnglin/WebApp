---
export_on_save:
    html: true
title: C++
image: https://pluralsight.imgix.net/paths/path-icons/c-plus-plus-93c7ddd5cc.png
description: Introduction to C++
topics: C++
sources: <a href="https://uva-cs.github.io/pdr/slides/01-cpp.html#/3/3">C++ Intro Slides</a> 
publish: True
---

# Basics

```cpp
// C++
#include <iostream>
using namespace std;
int main() {
    cout << "Hello World" << endl;
    return 0;
}
```

* `include` statements are like `import`, this is the **preprocessor**
* `using namespace std` needs to be at the top of **every single C++ program you write**

# Compilation

**Pretty Cool Loading**

* Preprocess 
    * `include` and `#` statements
* Compile resulting file 
* Link resulting files from compilation 

## Preprocessor 

**Pre-pounding** - All the `#include`, `#ifndef`, `#endif` and `#define` 

* `include` is for direct file copies. Only use `.h` files. 
* `define` is for **macros** - constants, text replacement

### In practice 

Every `.h` file should have: 

```cpp 
// Check if it's define, and then define
#ifndef HEADER_H 
#define HEADER_H 

// Includes 
#include "other_header.h"

// Code goes here

#endif
```

## `using`

* Uses a **namespace**
* Then you don't have to type the full namespace name each time.

## Int Truth Values 

```cpp
// Valid!
if (x)

// Technically valid, TERRIBLE idea without the double ==
if (x = 0)
```

* 0 is false, 0 is true

## Function Prototype 

* C++ is **single pass** compilation, **top to bottom**
* We need function prototypes for things like **mutually recursive functions** 

```cpp
// Prototype
// ret_type func_name (param_list);
bool even (int x);

bool even (int x) {
    // Do stuff here
}
```

# [Classes](https://uva-cs.github.io/pdr/slides/01-cpp.html#/classes)

## Structure 

* `public:` and `private:` sections 
* Double colon syntax 
* Semi colon *after* class declaration bracket
 
## File Splitting 

* **Header file** - contains the class definition, `.h` file 
* **Class implementation** - `cpp` file 
* **Main** - A `cpp` file for `main()`

### Parenthese Confusion 

When you call the **default constructor**, do not use parentheses. 
```cpp 
// Calling default constructor, NO PARENTHESES!
IntCell m1;

// Calling specific constructor, PARENTHESES!
IntCell m2 ( 37 );
```

### Header File 

* Need all the preprocessor lines in the code below. 
    * `#ifndef <identifier (generally file name)>`
    * `#define <identifier (generally file name)>`
    * And at the bottom, `#endif`
* Class Definition
```cpp
#ifndef INTCELL_H
#define INTCELL_H

class IntCell {
  public:
    IntCell( int initialValue = 0 );

    // const used like this means "I won't modify this object"
    int getValue( ) const;
    void setValue( int val );

  private:
    int storedValue;
    int max(int m) const;
};

#endif
```

### Class Implementation 

Actually *write* your methods at some point!

* Define the methods with form `return_type Class::method_name() maybe_const`
* If you're **not modifying fields**, for example with <span class="red">getters</span>, you need to use `const`

```cpp 
// Include your header 
#include "IntCell.h" 
using namespace std; // (not really necessary, but...)

// Constructor
IntCell::IntCell( int initialValue ) : 
        // This is equivalent to storedValue = initialValue 
          storedValue( initialValue ) { 
}

int IntCell::getValue( ) const { 
    return storedValue; 
}

void IntCell::setValue( int val ) { 
    storedValue = val; 
} 

int IntCell::max(int m) const {
    return (m>storedValue) ? m : storedValue;
}
```
### Main File

* Include your headers 
* Non-member function prototypes above `main` and static variables
* Below main, non-member method definitions

```cpp 
#include <iostream>
using namespace std; 

// Don't forget to include your header file
#include "MyHeaderFile.h"

int main () {

    // Do things 

    return 0
}
```

## Headers vs CPP 

Headers: 
* Prototypes 
* Class definitions 
* Macro definitions 

CPP: 
* Implementation 





## Friends 

The `friend` keyword (ex. `friend class List`) in the fields of a class allow one class to access another's **private** members. 

# Pointers 

![Pointer vs References](/static/assets/media/pointers_vs_references.png)

Can be for **primitive or object** types 

* `int * x;` - A pointer to an int. The address where that integer lives. 


## Dereferences 

The non-spaced, non-declaring asterisk can also be used to <span class="red">evaluate</span> the object to which the pointer points 
    * `*x = 2;`

The star **follows a pointer** to the pointee, and deal with its **target/value.**

It really means **whatever is at that address** . . . 

## & 

Means **address of** 

```cpp 
// Sir! Fetch the address of John, and put it in folder.
folder = &John;
```

## Initialization

Initialize your pointers to `NULL`! Otherwise, <span class="red">RUNTIME ERRORS</span> will occur. 

Then, you just **check** for a `NULL` value before proceeding.

## References 

Differences between references and pointers, remember icky (**ICI**): 

* **I**mplicit dereferencing 
* **C**onstant - address doesn't change 
* **I**nitialized - has to be initialized
```cpp
List sampleList
// Holds an address
List & theList = sampleList;
```

 # Memory Allocation 

 ## Types 

 * **Static** - you know how much. `float myArray[5]` 
    * Compiler also **deallocates** it after the subroutine
 * **Dynamic** - need on the fly
    * Create with `type * somePointer = new type` 
    * You need to **clean up** 
    * **Outlives** the usual scope
    * On the heap 
 
Stack addressed memory would be something like `Entity e()` using the default constructor. 

```cpp 
// Creation 
int * myIntPointer = new int
int * myArrayPointer = new int [5]

// Deletion 
delete myIntPointer
delete [] myArrayPointer
```

## Object Field Access 

* Use `.` for non-pointers and references 
* Use `->` for pointers, equivalent to `(*object).field`

# Parameter Passing 

Call by value, reference, or const? 

## Value 

* Actual param **copied** into formal 
* You **don't change** the arguments 

## Reference 

* Passes in the **address**
* Use when you **want to change** the arguments 

```cpp
void swap (int &x, int &y);
```

## Const Reference 

* Use when you want to access a non-copy **class reference**, but **don't** want to modify it. 
* Speed and security! 

```CPP 
bool compare(const Rational & left, 
             const Rational & right);
```

# Constructors 

C++ automatically provides us with: 

* <span class="red">D</span>efault constructor 
* <span class="red">O</span>perator = ()
* <span class="red">C</span>opy constructor
* <span class="red">D</span>estructor 

Just remember **DOCD**, like docked, because boats are constructed and have to then be docked. 

## Default 

No params, just for compilation 

## Destructors 

Called when 
* Object leaves scope 
* `delete` 



Uses the `~`, like `~ObjectName();`

## Copy Constructor 

```cpp 
IntCell original;
IntCell copy = original; // or IntCell copy(original);
```

Called in the following situations: 
* Declaration with initialization 
* Objects passed by value 
* Object returned by value 

# Operators

## Overload 

```cpp 
class Box {
    public: 
        // Overload + operator to add two Box objects.
        Box operator+(const Box& b) {
            Box box;
            box.length = this->length + b.length;
            box.breadth = this->breadth + b.breadth;
            box.height = this->height + b.height;
            return box;
}
```


