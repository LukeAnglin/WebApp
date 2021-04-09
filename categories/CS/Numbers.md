---
export_on_save:
  html: True
title: Numbers
image: https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Positional_notation_glossary-en.svg/1200px-Positional_notation_glossary-en.svg.png
description: Radix
topics: Radix, numbers, Y2K
sources:
publish: True
---

# Conversion

## Integers - Radix to Decimal

$$
\sum_{i=0}^{n} d_i\ \times R^i
$$

## Decimal to Radix Example

Use the **remainder** method specified [here](https://www.youtube.com/watch?v=gvJYNAiwOhc)

# In C++

- Any number that **begins with 0** is octal
- Any that **begins with 0x** is hex

# Conversion

## Binary to Hex

1. Split the binary number into 4 bit nibbles
2. Convert each to a **single** hex digit

1000 1101 is equivalent to 8d

# Endian

Byte reversal or lack thereof

- Big-endian - most significant **first**, **lowest** address
  - $1000 = 2^4$
  - 0xdeadbeef
- Little-endian - most significant **last**, **highest** address
  - $1000 = 2^0$
  - 0xefbeadde

# Integers

Commonly encoded by the **two's complement**, which flips the bits of negative numbers and then adds one.

## Two's Complement

- Zero is $n$ zeroes
- Encode positives in $n-1$ bits
  - Max val is $2^{n-1}-1$
  - Sign bit is zero
  - This zero is **positive** (all zeroes)
- Negatives, encode abs val
  - Subtract that from $2^n$
  - Max value is $-2^{n-1}$
  - **OR** encode abs val, flip bits, and add 1. The <span class="red">Luke method</span>

# Floating Point

## Four Parts

- Sign bit
- Mantissa - the value, in range $1.0 \leq m < 10.0$ for sci notation, or $1.0 \leq m < 2.0$
  - Example - $106$ is the same as $1.06 * 10^2$
- Base
- Exponent - $2^(n exp -1)-1$

## Conversion

Once you follow these steps, it's viable to convert to binary.

- Get the mantissa between 1 and 2
- Make the base 2

## IEEE Bit Splitting (Floats)

32 bits split into

- Bit 1 - Sign bit
- Bits 2-9 - Exponent (8 bits) - Powers of $\frac{1}{2}$
- Bits 10-32 - Mantissa (23 bits)

### Exponent Values

Exponents are **not** in two's complement!

- 0 is for zeros - **Reserved!**
- 1-254 - exponent-127
  - The exponent offset or bias is 127 for binary, also known as $2^\text{num exponent digits - 1} -1$
- 255 is for NaN and overflow. **Reserved!**

### Mantissa

Each bit set represents a power of $\frac{1}{2}$

Mantissa $= 1+ \sum_{i=1}^{23} \frac{b_i}{2^i}$

For floating point, must be between 1 and 2. See the paper for examples worked out from past exams.

## Conversion Examples

### Binary to Decimal

For a text overview with an <span class="red">awesome formula</span> on binary to decimal floating point, see [this](https://www.educative.io/edpresso/how-to-convert-a-single-precision-binary-float-to-decimal).

The formula is

$$
(-1)^{ \text{sign} } \times (1 + \text{mantissa}) \times 2^{\text{exponent} - \text{exponent offset}}
$$

### Decimal to Binary

For a video on decimal to binary, use this [numbers goddess](https://www.youtube.com/watch?v=8afbTaA-gOQ&t=425s)

**Steps**:

**Step one** - Convert the left and right to powers of two, positive and negative respectively.

**Example: 29.5**

16 + 8 + 4 + 1 and $\frac{1}{2}$

Which is also known as

$$
1*2^4+1*2^3+1*2^2+0*2^1+1*2^0+1*2^{-1}
$$

**Or, in binary**

11101.1

**Step two** - Move the decimal so the mantissa is between one and two, with the respective exponent

1.11011 \* $2^4$

**Step three** - Take that exponent, and add the exponent offset, which is $2^{\text{exp bits} - 1} - 1$. Also, encode it in binary.

$e = 4 + \text{offset} = 131$

That's

1000 0011

in binary.

**Step four** - Finalize!

**Sign** **exponent** **mantissa**

1 1000001 11011------ a whole bunch of zeroes til u finish off the number

## Maxs and Mins

255 and 0 for exponent bits are reserved, so

- **Max positive number** - Ones except for a zero in the final exponent bit position and a zero in the sign bit.
- **Min positive number** - All zeroes except a one in the last exponent bit position. Basically `xor` the max, except for the sign bit

# Doubles

## Bit Splitting

- Bit 1 is for sign
- Bits 2-12 are for exponent (11)
- Bits 13-64 are for mantissa (52)
- Exponent offset works out to 1023 ($2^{11-1}-1$)
