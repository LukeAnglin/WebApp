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

## Simple Hello World 

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
    * `#efine <identifier (generally file name)>`
    * And at the bottom, `#endif`
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
* If you're **not modifying fields**, for example with <span class="keyword1">getters</span>, you need to use `const`

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

Class definition 

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





