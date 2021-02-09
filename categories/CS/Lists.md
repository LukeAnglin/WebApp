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