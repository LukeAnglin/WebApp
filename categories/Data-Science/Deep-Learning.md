---
export_on_save:
    html: true
title: Deep Learning
author: 
image: 
description: 
topics: 
sources: 
publish: 
---

# AI vs. ML vs. DL

![AI vs ML vs DL](https://www.kdnuggets.com/wp-content/uploads/ai-machine-learning-deep-learning-1.jpg)

<dl>
    <dt>AI</dt>
    <dd>Classical Programming - The human inputs code which let's computers do tasks for us</dd>
    <dt>Machine Learning</dt>
    <dd>Humans clean up some data, feed it to the model, and the model creates it's own rules.  Trained, not explicitly programmed.</dd>
    <dt>Deep Learning</dt>
    <dd></dd>
</dl>

## ML Requirements

* Inputs - sound files 
* Labels - transcripts 
* Scoring metrics - used to adjust the model as it learns 

## Deep Learning 

Here, we define *our own representations* of data in multiple layers.  Layers are assigned weights, which are constantly optimized based on the **loss function**

![Deep-Learning-Diagram](../../static/assets/media/Deep-Learning-Diagram.png)

## ML or DL? 

Don't start using deep learning for every problem.  That's using a jackhammer to floss rabbit teeth. 

For complex problems, here are the advantage of DL: 

* Removes feature engineering 
* **Adjusts everything** at once rather than one weak model at a time, as high-performing ML algorithms like XGBoost do. 

## Practical ML/DL 

Learn XGBoost and Keras.  Watch the Kaggle competitions to stay up-to-date.  Win. 

# Keras Neural Network

What steps should we take to build a neural network with Keras? 

## Split

First, we have to decide our data into features and labels.  A dimension check never hurts anyone, using the `.shape` attribute. 

Don't forget to use a `reshape(-1, 1)` to get the proper **column vector** for the labels.  For example, if we have a table of 4 features and 10 samples (10, 4), then the shape of our labels should be (10, 1). 

## Sculpt

This step involves: 

* Instantiate the model - for example, run `models.Sequential()`, and put that in a `network` variable. 
* Add layers with `.add(layers)`

## Compile

To make our network ready for training, we need three things: 

* Loss function 
* Optimizer 
* Scoring metrics 

Pass these to `network.compile()` as `**kwargs`, and we're on our way!

## Preprocess 

### Reshaping 

The training images from the MNIST dataset are of shape (60000, 28, 28).  How do we make this *usable* for Keras? 

```python 
train_images = train_imags.reshape((60000, 28*28))
```

With multi-dimensional shapes, the `reshape` must have the same **product** as the original shape. 

### DataType Check 

Just like with machine learning, we need *numbers*.  A quick `.astype('float32')` can do wonders.  

### Standardization

If our interval is [0, 255], we just divide the data by 255 so it's in the range [0, 1].  

If necessary, you can always use Sci-Kit's toolbox.  

### Categorical Types 

Keras makes this easier for us than other libraries.  Rather than one hot encoding, just use the `to_categorical(data)` function from the `keras.utils` module. 

## Train! 

Use the `.fit(training_data, training_labels)` function on the network, and be exposed to the wonders of Deep Learning! 

# Tensor Manipulation 

Ahh, tensors, arrays of matrices (or tensors . . .).  How do we work with them?

## Slicing 

Slicing tensors is just like slicing numpy matrices.  You can even use shorthand.  

```python 
# This 
train_images[10:100]

# Is equivalent to this 
train_images[10:100, :, :]
```

## Batches 

We know the samples axis and axis = 0 are equivalent.  But, with neural networks, we're constantly subdividing data into simpler parts. 

In batches, axis 0 is the **batch axis**. 

## Common dimensions

* 2D - Vectors
    * Tables - Bank represents everyone as a name, income, and zip code.  If we have 100,000 people, our shape would be (100000, 3)
* 3D - Timeseries or Sequences 
    * Stock data has samples, features, and time attributes 
* 4D - Image Data 
    * Samples, height, width, color-depth 
* 5D - Video 
    * Image data with the extra frames dimension 

## Operations 

### Elementwise 

Let's look at the sculpting process to understand elementwise operations.

```python 
keras.layers.Dense(512, activation = 'relu')
```

Here, 512 represents the *neuron units* in our network.  `activation` is the function which takes an input 2D tensor and outputs another 2D tensor.  

```python 
output = relu(dot(W, input) + b)
```

There are a few things going on here. 

* `dot` - dot product 
* $W$ - a slope like parameter for our tensor 
* $b$ - An intercept 

### Broadcasting 

Here's a [helpful video](https://deeplizard.com/learn/video/6_33ulFDuCg), and my summary.

First, we ask:  Are the dimensions compatabile?

Conditions: 

* Dimensions are equal - (1, 3) and (1, 3)
* One of the dimensions is 1 - (1, 5, 3) and (5, 5, 3)

The **resultant shape** of a broadcasting operation takes the *maximum* of the compared dimensions.  

Consider (1, 3) and (3, 1).  The resultant shape would be (3, 3)

#### Mental Model 

The easiest way to picture broadcasting ops is imagining the smaller rank tensor being *copied out*.  Then, the operation is performed. 

### Dot Product 

The `dot` operation differs from `*`. 

![Dot Product](https://www.mathsisfun.com/algebra/images/matrix-multiply-a.svg)

My steps: 

* Transpose the first matrix
* Multiply column by column 
* Add up that sum

That's worded a bit different than other explanations, but I like the transposition idea.  

Here's a [simple explanation](https://www.mathsisfun.com/algebra/matrix-multiplying.html).  If you think about matrix multiplication (the dot product) in terms of economics, costs and demand, it's facile to grasp the logic.  

#### Requirements

Columns of the first matrix must equal the rows of th second.  

$$ c_x = r_y $$

The final output is flipped, so to speak.  The matrix will have the same amount of rows as the first matrix, and the same amount of columns as the second 

$$ x * y = \text{A matrix of dimensions }r_x \text{and }c_y$$

![Dot Product Requirements Mapping Image](../../static/assets/media/DotMap.png)

# Gradient Optimization 




