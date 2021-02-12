---
export_on_save:
    html: true
title: Numbers
image: https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Positional_notation_glossary-en.svg/1200px-Positional_notation_glossary-en.svg.png
description: Radix 
topics: Radix, numbers, Y2K
sources: 
publish: True 
--- 

# Positional Systems 

## Integers

$\sum_{i=0}^{n} d_i\ \times R^i$

## Reals 

$\sum_{i=-m}^{n} d_i\ \times R^i$

# In C++ 

* Any number that **begins with 0** is octal 
* Any that **begins with 0x** is hex 

# Conversion 

## Binary to Hex 

1. Split the binary number into 4 bit nibbles 
2. Convert each to a **single** hex digit 
3. Example: 1000 1101 is equivalent to 8d

# Endian 

Byte reversal or lack thereof

* Big-endian - most significant **first**, **lowest** address 
    * $1000 = 2^4$
    * 0xdeadbeef
* Little-endian - most significant **last**, **highest** address 
    * $1000 = 2^0$ 
    * 0xefbeadde

# Integers 

## Sign 

The **sign bit** is the first bit, and it is **one** if the number is **negative**.  

Could also be represented by the **sign complement**, flipping the bits if negative, but has the same issue with zero representation.