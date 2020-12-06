---
export_on_save:
    html: True
title: Boston Housing Dataset Regression with Keras
author: Luke Anglin
image: https://joshuagoings.com/assets/linear.png
description: Looking at how one goes about creating a regression algorithm with a neural network
topics: Keras regression
sources: Francois Chollet's <i>Deep Learning with Python</i>
publish: True
link: https://nbviewer.jupyter.org/github/LukeAnglin/WebApp/blob/master/categories/MLProjects/Notes/Keras-Boston-Regression.ipynb
---

# Regression

Regression is yet another type of problem that we must change our methods 

* Use a `Dense` final layer with only **one** hidden unit and **no** activation function. 
* Monitor during training with the `mae` metric, and use `mse` as your loss function

# Model Functions

One best practice takeaway from this experiment is that you should always use a function to define models.  This allows you to easily play with parameters and reach the desired accuracy/loss quicker. 

# Few Samples

## K Folds 

* K Fold validation is often a good idea, but it is **especially crucial when you have few samples** 

![K Folds](https://upload.wikimedia.org/wikipedia/commons/b/b5/K-fold_cross_validation_EN.svg)

## Small Network 

With little data, use small networks with few hidden layers (one or two) in order to *avoid overfitting*. 

# Normalization 

Another takeaway from this experiment was how key normalization is.  Use Sklearn's `normalize()` function from the `preprocessing` module in order to accelerate this process. 








