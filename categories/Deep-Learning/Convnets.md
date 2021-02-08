---
export_on_save:
    html: true
title: Convolutional Neural Networks
image: https://miro.medium.com/max/1000/1*vkQ0hXDaQv57sALXAJquxA.jpeg
description: An introduction to convolutional neural networks and their implications
topics: Convolutional neural networks, 
sources: <i>Deep Learning with Python</i>and <a href="https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53">this Medium article</a>
publish: True
---

# CNN 

[CNN's](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53) are stacks of `Conv2D` and `MaxPooling2D` layers. 

![CNN](https://cezannec.github.io/assets/cnn_intro/CNN_ex.png)

## Purpose 

The idea behind CNN's is that we **extract the useful features** from things like images.  Edges, perhaps. 

## Convolution 

While `Dense` layers learn **global** patterns, `Conv2D` layers learn **local** patterns.  

We had 28 x 28 pixel images in this exmample.  Convolutional operations broke this into 3 x 3 sections. 

## Properties 

* **Translation Invariance** - A pattern learned in one window propagates to the others.  Consider I learned a pattern in the bottom left of an image - it would be usable in the upper right. 
* **Hierarchial Learning** - Consider an image of a dog.  It might break down it's nose, ears, and legs to make the whole dog easier to recognize. 
* `Conv2D` operate on **3D tensors**
    * The `2D` represents the **two spatial axes** they take - e.g. (height, width)
    * The last axis is the *depth* axis.  In RGB, it would be three dimensional (for R, B or G)
    * The final output's depth axis is no longer representing the same thing as the input.  It represents a **filter**, which may represent something, like the presence of a tail. 
        * This is a *parameter of the layer*.  We could configure a length 32 output from an RGB image on the depth axis. 

## Filters 

The <span class="red">filter, feature detector or kernel</span> is the iterative, moving piece over the feature map (our input image). 

![](https://miro.medium.com/max/500/1*GcI7G-JLAQiEoCON7xFbhg.gif)

It has the same depth as the input as well. If we have very high resolution images, we may increase the **stride value**, or the filter's movement on each iteration. 

## Padding/Strides 

Modifying our strides and padding is crucial to adjusting on how our model either reduces or increases dimensionality.  See the animations on [this GitHub repo.](https://github.com/vdumoulin/conv_arithmetic)

Padding also counteracts **border effects**.  

Here's a border effect.  It's what makes one output of a 28 x 28 x 1 turn into 26 x 26 x 1. 

![Border Effect](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQR2FNdV5MbP6YRhpcd_p_yBUlEA-WAmQF3A&usqp=CAU)

Types of `padding` in Keras: 

* `same` - pad in a way to have same as initial dimensions 
* `valid` - don't pad, reduce dimensions for me.

## Pooling 

Dimensionality reduction of the convolved feature.  Two types: 

* **Max** - Greatest value in the matrix
* Average - Average of matrix

We *almost always* use max, because it performs **noise suppression**. 

![Pooling](https://miro.medium.com/max/396/1*uoWYsCV5vBU8SHFPAPao-w.gif)

### Max Pooling 

Rather than using strides to reduce dimensionality, it's more common and effective to use max pooling.  

* Usually done in 2 x 2 windows 
* 

## Parameters 

* **Patch Size** - Typically 3 x 3 or 5 x 5
* **Depth Output** 

# Architecture 

One feeds `Conv2D` layers into `MaxPooling2D` Layers.  Here's an example: 

```python 
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
```

## Final Flattening

At the end of this *convoluted* (I had to take that opportunity) process, we connect it to a normal neural network.  

![](https://miro.medium.com/max/700/1*kToStLowjokojIQ7pY2ynQ.jpeg)

We want to connect the CNN to a stack of `Dense` layers.  This is where the `Flatten()` constructor of `layers` comes in.  

```python 
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
```

Additionally, notice that last line.  `softmax` is for multi-class, and because we have multiple types of digits we're identifying here, we use that. 

## Data Size

The size of a convnet network, like most networks, is proportional to the data size and problem complexity.  

Additionally, **small datasets call for data augmentation** 

### Data Augmentation 

Increase the amount of 'data' you have by changing orientation or scale.  For instance, maybe change the orientation of one image of a dog 9 times, and turn that one image into ten. 

# Pretrained Models 

In general, you want to just use the *convolutional base* of other models.  These are more generic, and thus more reusable.  

## Options 

Two options: 

1. Run the conv base on your dataset **once**, and save that.  Then, run a `Dense` network on that.  Less accurate, but **much** cheaper and more efficient. 
2. Run the conv base over each iteration - **only use this if you have access to a GPU** 

## Freezing 

Freeze pretrained models that are too expensive by setting the `trainable` attribute to false.  Do this **before compiling**. 

Here's what that looked like in this example: 

```python 
conv_base.trainable = False
```

![Frozen ConvNet](https://camo.githubusercontent.com/28a6cb7048317aba34f39cb02f15520708189008/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f626f6f6b2e6b657261732e696f2f696d672f6368352f76676731365f66696e655f74756e696e672e706e67)

And, here's how we froze just a few of the upper layers when we unfroze the base: 

```python 
conv_base.trainable = True

set_trainable = False
for layer in conv_base.layers:
    if layer.name == 'block5_conv1':
        set_trainable = True
    if set_trainable:
        layer.trainable = True
    else:
        layer.trainable = False
```

## Fine-Tuning 

Once we've trained our model with the `.fit()` method, we can *now fine-tune* it.  This is when we unfreeze the top layers now that the error signal won't destroy our CPUs.  

# Takeaways 

* Convnets work great for computer vision 
* On small datasets, use data augmentation to fight overfitting 
* Reuse existing convnets, especially with small datasets 


# Examples 

1. [Intro](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.1-introduction-to-convnets.ipynb)
2. [On a small dataset](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.2-using-convnets-with-small-datasets.ipynb)
3. [Pre-Trained Convnet](https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.3-using-a-pretrained-convnet.ipynb)
4. [Full Kaggle Tutorial](https://www.kaggle.com/kanncaa1/convolutional-neural-network-cnn-tutorial)