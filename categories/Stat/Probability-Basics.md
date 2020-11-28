# Relative Frequency

The relative frequency of an event, $A$, is given by $Q_{n}(A)$

$$Q_{n}(A) = \frac{N_{n}(A)}{n}$$

where $N_{n}(A)$ is the number of times the event $A$ is observed in $n$ trials.

## Mutually Exclusive

It can be derived simply that

$$Q_{n}(A + B) = Q_{n}(A) + Q_{n}(B)$$

Consider it logically.  Flip a coin ten times.  The relative frequency of both events should equal ten, and this formula proves it.

<span class="keyword1">Mutually exclusive events</span> are <span class="keyword1">disjoint sets</span>

# Countable

Continuous events are inherently *uncountable* while discrete events are *countable*.  This is where **discretization** comes into play in `Sci-Kit Learn`. 

## Discretization

Often times, we need to discretize the sample space, $\Omega$'s, subsets.  For example, the Pharoah's land shouldn't be continuous; rather, we would ask "how many acres?"

# Combinatorics

## Permutations

Order matters.  Think sequences.

![Permutations](https://miro.medium.com/max/1000/1*JNK-n0Pt0Vbxk0lxVpgT5A.png)

## Combinations

Order does not matter.  Think sets.

![Combinations](https://miro.medium.com/max/1000/1*7cFRn8jW4g_91YgDAbmxRQ.png)
