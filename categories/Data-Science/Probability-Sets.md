---
title: Sets
author: Luke Anglin
image: https://media.nagwa.com/723124583276/en/thumbnail_l.jpeg
description: A look at set theory; at least, that which I deem relevant to probability and statistics. 
topics: sample space, set operations, set laws, indicators, symbols
---

# Sets

**Meaning**: No duplicates. 

The <span class="keyword1">sample space</span> is denoted by $\Omega$

## Sample Space 

The set of possible outcomes.  Consider a roll of dice.
$$\Omega = \{1, 2, 3, 4, 5, 6\} $$

## Set Operations

* Union $\cup$
* Intersection $\cap$
* Complement $A^c$ - the set of points that does **not belong to A** within the sample space, $\Omega$

## Set Laws

Sets are <span class="keyword1">commutative</span> and <span class="keyword1">associative</span>.  

<!-- Associativity Warning -->
<div class="alert alert-danger" role="alert">
<b>Warning: </b>Associativity is <b>only true</b> when the operators are the same between the sets.
</div>

<div class="bs-example" data-example-id="simple-panel">
<div class="panel panel-default">
   <div class="panel-heading">
      <h5 class="panel-title">Set Associativity . . . or lack thereof</h5>
   </div>
   <div class="panel-body">$$(A\cup B) \cap C \neq A\cup (B\cap C)$$
   <img src="../../../assets/media/Stat/Associativity.png" alt="">
   </div>
</div>

## Indicators

A <span class="keyword1">function</span> that maps a sample point to a member of a binary value is known as an <span class="keyword1">indicator</span>. 

![Indicator Function](https://wikimedia.org/api/rest_v1/media/math/render/svg/e14a338f7566bf9113eaffc7cc2a51e5db37261d)

The subscript represents the **set** the indicator maps to the one or zero.

### Symbols

$\wedge$ represents the maximum

$\vee$ represents the minimum


