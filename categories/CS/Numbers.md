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

# Conversion 

## Integers

$\sum_{i=0}^{n} d_i\ \times R^i$

## Reals 

$\sum_{i=-m}^{n} d_i\ \times R^i$

These are for **decimal to radix**. To go the other way, use: 

$$
\frac{n}{R} = d_nR^{n-1}
$$

**Note**: This will have a **remainder** of $d_0$

## Decimal to Radix Example 

Use the **remainder** method specified [here](https://www.youtube.com/watch?v=R5v3FmG5qus)

## Radix to Decimal Example 

$$ 
356.3_8 = 3*8^2 + 5*8^1 + 6*8^0 + 3*8^{-1}
$$
#

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

Commonly encoded by the **two's complement**, which flips the bits of negative numbers and then adds one. 

## Sign 

The **sign bit** is the first bit, and it is **one** if the number is **negative**.  

Could also be represented by the **sign complement**, flipping the bits if negative, but has the same issue with zero representation.

## Two's Complement 

* Zero is $n$ zeroes 
* Encode positives in $n-1$ bits 
    * Max val is $2^{n-1}-1$
    * Sign bit is zero 
    * This zero is **positive** (all zeroes)
* Negatives, encode abs val
    * Subtract that from $2^n$
    * Max value is $-2^{n-1}$
    * **OR** encode abs val, flip bits, and add 1. The <span class="red">Luke method</span>

# Floating Point 

## Four Parts 

* Sign bit 
* Mantissa - the value, in range $1.0 \leq m < 10.0$ for sci notation, or $1.0 \leq m < 2.0$
* Base 
* Exponent 

## Conversion

Once you follow these steps, it's viable to convert to binary. 

* Get the mantissa between 1 and 2
* Make the base 2

## IEEE Bit Splitting 

32 bits split into 

* Bit 1 - Sign bit 
* Bits 2-9 - Exponent (8 bits)
* Bits 10-32 - Mantissa (23 bits)