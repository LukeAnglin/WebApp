---
export_on_save:
    html: true
title: Graphs
image: https://www.geeksforgeeks.org/wp-content/uploads/undirectedgraph.png
description: Graphs
topics: Graphs
sources: https://www.youtube.com/watch?v=88fsIA53sWE
publish: True
---

# Graphs 

![Graph](https://www.geeksforgeeks.org/wp-content/uploads/undirectedgraph.png)

[This](https://medium.com/brandons-computer-science-notes/graph-theory-3bd99b24fa2a) and [this](http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/Graphs.html) from Medium and UC are both great.

## DAGs 

* No cycles 
* Either **strongly** or **weakly** connected. 
    * Strong - path from every vertex to every other vertex (connected)
    * Weakly - not totally connected

## Terminlogy 

For a graph $G = (V, E)$

* **Weights** - a weight $w$ associated with each edge, and they are **adjacent** to $v$ IFF $(v, w) \in E$
* **Paths** are sequences of vertices of edges 
* **Connected** - path from every vertex to another vertex
* **Loop** - $(v, v) \in E$
* **Complete** - edge between every pair of vertices 

## Adjacency Matrix 

 Is there an edge? Make that a 1. 

 ![Adj Mat](https://static.javatpoint.com/ds/images/sequential-representation.png)

Adjacency lists are similar 

![Adj list](https://notes.shichao.io/clrs/figure_22.2.png)

## Topological Sorting 

Given a path from $v_1$ to $v_n$, make sure $v_n$ comes after $v_1$ in the ordering 

* Can be multiple 
* First vertex always has in-degree 0
* Must be a DAG 

# Shortest Path 

## Single Source 

The **weighted path length** of $v_1 . . . v_n$ is 

$$\sum_{i=1}^{n-1}c_{i,i+1}$$ where $c_{i,i+1}$ is the cost of edge $(v_i,v_{i+1})$

### Unweighted 

For unweighted, just do **breadth-first** search 

### Weighted 
 
* [Daik-struh](https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/) - $\Theta(n^2)$
* 