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

## Applications:

- Undo
- Symbol Balancing
- Postfix calculator

## Linked List Implementation

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

## Array Implementation

### Pros

Most operations **fast, constant time**
Consists of

- `theArray` - the stack itself
- `topOfStack`

### Cons

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

## Summary

Attributes only include the **top of the stack**, and they can be implemented as `LinkedList`, arrays, or `vector`.

The fundamental operations, `push_back`, `pop` and `top` are **constant time**.

# [Queues](https://uva-cs.github.io/pdr/slides/02-lists.html#/queues)

Also can be implemented as `LinkedList`, arrays, or `vector`, also which are **constant time** with a slight exception for `vector`.

## Arrays

Again issues with the array being full.

## Enqueue

- Increment size
- Increment back
- set `theArray[back] = element`

## Dequeue

- set return value to `theArray[front]`
- decrement current size
- increment front

## Linked List

![](https://uva-cs.github.io/pdr/slides/images/02-lists/queue-diagram.svg)

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

- Size $N$
- $A_0$ is first element, then $A_1, A_2 . . . A_i$ where $i$ is the position

### Arrays

- Fixed capacity, operations constant or linear

### Linked List

Operations constant or linear

# Pointer Reroutes

[Awesome pointer illustrations](https://www.softwaretestinghelp.com/doubly-linked-list-2/#Insertion)
