---
title: Preprocessing Data 
author: Luke Anglin 
image: https://miro.medium.com/max/2144/1*yjgyRtY3sPpjpmp6t2U9Xg.png
description: Preprocessing data for maximal efficiency, storage, speed, and F1 scores. 
topics: standardization, feature adherence, sparse data, distributional mappings, categorical encoding, normalization, discretization
---

# Standardization  

Estimators do not perform well when features are not close to normal distributions.  Considering the <span class="red">Central Limit Theorem</span>, we want at least $n > 30$ samples.  

## Feature Adherence

SKLearn estimators assume a **zero mean and unit variance** for **all features**.  Use `StandardScalar` to ensure adherence, or the `scale()` function

## Ranges

If you have many **zeroes** or **very small** standard deviations, the `MinMaxScaler` or `MaxAbsScaler` will be preferable.

## Sparse Data 

`MaxAbsScaler` and `maxabs_scale` are used for this, which improve performance since the data includes so many zero rows.

## Robust 

Some data is riddled with outliers, and because `StandardScaler` relies on mean and variance, one should opt for the `robust_scale()` or `RobustScaler` instead.

## Kernel Data 

For Kernel matrices, use `KernelCenterer` 

# Distributional Mappings

## Gaussian

Many ML algorithms do best with Gaussians.  To map to one, use a **power transform**, using the `PowerTransformer`

To imagine what this means, picture a histogram strongly skewed in one direction.  Now, picture it normalized.  That's what your `PowerTransformer` is doing.  

![](https://miro.medium.com/max/2144/1*yjgyRtY3sPpjpmp6t2U9Xg.png)

Even the notoriously skewed Boston Housing Dataset becomes fairly normal after a power transform. 

The `QuantileTransformer` is similar if the `output_distribution='normal'` parameter is passed.  Use both and visualize afterwards to decide which is best. 

## Uniform

`QuantileTransformer` is used for this.

# Normalization

Very simple.  Just use the `normalize()` function, or the stateless `Normalizer` class for `Pipeline` transformations.

# Categorical Encoding

For ordered features, use `OrdinalEncoder`.  Otherwise, `OneHotEncoder`.  

To see what the numbers correspond to, use the `.categories_` attribute.

# Discretization

Transforming continuous data to discrete data is known as **discretization**.  This article by [Rohan Gupta](https://towardsdatascience.com/an-introduction-to-discretization-in-data-science-55ef8c9775a2) goes into detail about it's usefulness.

## Usefulness

* Limits DoF 
* Feature Interpretation
    * Consider dividing bench presses into categories.  Below 100 lbs is weak, between 100 - 135 is average, and anything above is fit. 
* Model Compatability
* Smoothing (reducing noise)

# Vectorization 

This is essentially the same as **changing your datatypes**.  Give me tensors of floats, or give me death. 

# Missing Values

## Neural Networks

*Generally*, you can get away with changing NaN's to zeroes.  However, *if* the data has *meaningful* zeroes, DO NOT do this.  

Why can we get away with zeroes?  Because the neural network will eventually say "zeroes mean nothing to me."  

# Feature Engineering

Hard code to make the model's life easier.  

Consider an ML algorithm trying to tell time based on a clock.  If you hard code it to pass in the polar coordinates rather than the entire pixel grid, you've just saved a ton of computation and improved the accuracy massively.  



