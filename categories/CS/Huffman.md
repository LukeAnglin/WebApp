---
export_on_save:
    html: true
title: Huffman and Heaps
image: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Max-Heap-new.svg/1200px-Max-Heap-new.svg.png
description: Huffman Encoding and binary heaps
topics: Heaps and stuff
sources: 
publish: true
---

# Binary Heaps 

## Priority Queues 

Anything that **IMPLEMENTS FORCEFUL DISCIPLINE** can be considered a priority queue. 

* **I** - insert with priority 
* **F** - Find the minimum (the root)
* **D** - Delete the min, remove root, re-percolate

## Data Structure Running Times 

![](/static/assets/media/pq.png)

A heap gives us: 

* `findMin()` - $\Theta(1)$ 
* `deleteMin()` - $\Theta(log(n))$ worst and average
* `insert` - $\Theta(log(n))$ worst, typically $\Theta(1)$

## Properties 

* Structure - **almost complete** binary tree with bottom exception, levels filled left to right 
* Order - Every parent is smaller than it's child (in a minheap)
* $2^{h+1}-1$ nodes 
* $2^h-1$ non-leaves 
* $2^h$ leaves 

## Benefits of Arrays 

* Saves space 
* Saves time 
* Easy to find stuff 

### Array Representation 

* Note that **the zero index has NOTHING**
* Level by level, left to right
* **Left Child** - $2i$
* **Right Child** - $2i+1$
* **Parent** - $\text{floor}(\frac{i}{2})$

## Operations + Animation

See [this](https://www.cs.usfca.edu/~galles/JavascriptVisual/Heap.html)

* Insertion - put it in, `percolateUp` - Is my parent greater? Let's swap then. 
* Deletion - put it in, `percolateDown` - Move farthest down farthest right node to root, and percolate it down. 

# Huffman Encoding

Repeatedly take the two highest priority (smallest) node and create a joining node with the sum of them as its priority. 