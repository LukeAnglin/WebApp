---
title: Combinatorics Introduction
author: Luke Anglin
image: https://www.birmingham.ac.uk/Images/Research-and-teaching/Engineering-and-Physical-Sciences/Mathematics/pictures/ham-900px300x300.png
description: Some background knowledge on combinatorics; useful for statistics, probability, and data science in general. 
topics: Binomials, Bernoulli's Theorem . . . 
---

# Binomials

We have 
$$
(x+y)^3
$$

Ask yourself the following questions.  

* Choose no $y$'s.  

$$
{3 \choose 0}\times x^3y^0 
$$

* Choose <span class="red">one</span> y 

$$
{3 \choose 1}\times x^2y^1
$$

Keep going.  What do you end up with?  **Bernoulli's theorem**

$$
 P(A) = \sum P(\{ (e_1,\dotsc,e_N) \})  =  \binom{N}{k} \cdot p^kq^{N-k}
$$

This is used for <span class="red">binary trials</span>.  Think about tossing a coin.  Then, $k$ is how many times, say heads, is achieved, and $N$ is the number of trials


# Multinomials

