---
export_on_save:
    html: true
title: Lists 
image: https://miro.medium.com/max/970/1*f2oDQ0cdY54olxCFOIMIdQ.png
description: Lists in C++ in depth 
topics: Linked lists, list structures
sources: 
publish: True 
---

# Std Lib 

Implements 

* `vector`- solve capacity, index validity checking and copying issues of arrays 
* `string` - solve comparison issues with `char` arrays 

## [Vectors](https://www.cplusplus.com/reference/vector/vector/)

```cpp
// Create Vertex object 
std::vector<Vertex> vertices; 

// Add elements 

vertices.push_back({ 1, 2, 3 })

// Remove that element 

vertices.erase(vertices.begin())

// Insert an element at a position 
it = vertices.begin()
vertices.insert(it, {1, 4, 5})

// You could also remove everything 
vertices.clear()
```

### Iterators 

Represents **position**

* `.begin()` and `.end()`
* Increment with `itr++` or `++itr`
* `==` and `!=` function properly 

Looping through: 

```cpp 
for ( vector<int>::iterator it = v.begin(); 
    it != v.end(); it++ )
    // Print the value at the iterator 
    cout << *it << endl;
```

 # Templates 

Basically **generics** for functions and/or classes 

Used for function/class that **might take different types**. 

## Functions 

```cpp 
template <typename Comparable> 
const Comparable & findMax (const vector<Comparable> & a) {
  int maxIndex = 0; 
  for( int i = 1; i < a.size(); i++ ) 
      if( a[ maxIndex ] < a[ i ] ) // note the use of '<'
          maxIndex = i; 
  return a[ maxIndex ]; 
}
```

## Classes 

```cpp 
template <typename Object>
class ObjectCell {
  public:
  // Initializes a holder for whatever the default constructor of the passed in Object parameter is 
    ObjectCell(const Object & initValue = Object()) 
                : storedValue(initValue) {}
    const Object & getValue() const {
               return storedValue;
    }
```

# [Stacks](https://uva-cs.github.io/pdr/slides/02-lists.html#/5/1)

Applications: 

* Undo 
* Symbol Balancing 
* Postfix calculator 

## Linked List 

![Linked List Stack Implementation](https://uva-cs.github.io/pdr/slides/images/02-lists/stack-diagram.svg)
```cpp 
#include "StackNode.h"

// assumes a stack of ints stored in StackNodes
class Stack {
  public:
    Stack();                // constructor    
    ~Stack();               // destructor
    bool isEmpty() const;   // checks for empty
    void push(int value);   // push value onto stack
    void pop();             // pop top of stack
    int top() const;        // returns topOfStack

  private:
    StackNode *head;        // like a ListNode...
};
```

## Array

Most operations **fast, constant time**
Consists of 
* `theArray` - the stack itself 
* `topOfStack`

Fails when array is full, so we need `vector`

## Vector 

```CPP
#include <vector>
using namespace std;

class Stack {
  public:
    Stack();                // constructor    
    ~Stack();               // destructor
    bool isEmpty() const;   // checks for empty
    void push(int value);   // push value onto stack
    void pop();             // pop top of stack
    int top() const;        // returns topOfStack

  private:
    vector<int> theStack;    
};
```

### Pushing 

```CPP
void Stack::push(int value){
  theStack.push_back(value);
}
```

## Summary 

Attributes only include the **top of the stack**, and they can be implemented as `LinkedList`, arrays, or `vector`. 

The fundamental operations, `push_back`, `pop` and `top` are **constant time**. 

# [Queues](https://uva-cs.github.io/pdr/slides/02-lists.html#/queues)

Also can be implemented as `LinkedList`, arrays, or `vector`, also which are **constant time** with a slight exception for `vector`. 

## Arrays 

Again issues with the array being full. 

## Enqueue 

* increment size 
* increment back 
* set `theArray[back] = element`

## Dequeue 

* set return value to `theArray[front]`
* decrement current size 
* increment front 

## Linked List 
  
![  Linked List Queue Implementation](https://uva-cs.github.io/pdr/slides/images/02-lists/queue-diagram.svg)
```cpp 
#include "QueueNode.h"

// assumes a queue of ints stored in QueueNodes
class Queue{
  public:
    Queue();     // constructor
    ~Queue();    // destructor

    // enqueue item to back of list
    void enqueue(int value);

    // remove item from front of list
    int dequeue();    
```

# [ADTs](https://uva-cs.github.io/pdr/slides/02-lists.html#/adts)

Things with sets of operations - **definition of a type** - generally classes. 

## Lists 

* Size $N$ 
* $A_0$ is first element, then $A_1, A_2 . . . A_i$ where $i$ is the position

### Arrays 

* Fixed capacity, operations constant or linear

### Linked List 

Opertaions constant or linear 










