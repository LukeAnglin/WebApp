---
title: Multiclass Classification on the Reuters Dataset with Keras 
author: Luke Anglin
image: https://miro.medium.com/max/972/1*SwXHlCzh-d9UqHOglp3vcA.png
description: A follow-along to the Deep Learning with Python book, with a few edits and experiments of my own.  Here, I look into some other libraries on my own time which help with visualizing and evaluating the accuracy and loss of a neural network.  Moreover, we look at the appropriate loss function and optimizers for multiclass situations
topics: Multiclass classification, categorical crossentropy, and the plot-keras-history library
sources: Francois Chollet's <i>Deep Learning with Python</i> book
publish: True
category:  Deep Learning 
link: https://nbviewer.jupyter.org/github/LukeAnglin/WebApp/blob/master/categories/MLProjects/Notes/Keras-Reuters-Multiclass.ipynb
---

With a multiclass problem like the Reuters dataset, we need to change some of our approaches.  

# Multiclass layering 

If you're trying to classify $N$ classes, you're output `Dense` layer should be of the same size $N$

# Encoding 

Generally, we'll be using one-hot-encoding with the `keras.utils.np_utils` module's `to_categorical()` function. 

# Activation 

For a multiclass problem, we want to use `softmax` activation, so it will output a probability distribution over the $N$ classes. 

# Loss 

Multiclass demands the `categorical_crossentropy` loss function, which minimizes the distance between our prediction probability distribution and the true distribution. 

# Advice

* Don't use too many layers, especially if they're small.  This leads to **information bottlenecks**. 
* One way to remedy overfitting and improve model accuracy is playing with the number of layers and hidden units you are using

