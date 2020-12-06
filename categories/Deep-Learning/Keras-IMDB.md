---
title: First Neural Network with Keras
author: Luke Anglin
image: https://miro.medium.com/max/874/1*eJ36Jpf-DE9q5nKk67xT0Q.jpeg
description: Here, we work through the IMDB dataset, classifying reviews, by training a neural network with Keras.  This follows along with Francois Chollet's <i>Deep Learning with Python</i> book
topics: Neural networks, activation functions, loss functions, basic deep learning
sources: Deep Learning with Python by Francois Chollet 
publish: True
link: https://nbviewer.jupyter.org/github/LukeAnglin/WebApp/blob/master/categories/MLProjects/Notes/Keras-IMDB.ipynb
---

The first project on our Deep Learning journey is evaluating the IMDB dataset.

The link to this notebook can be found [here](https://hub.gke2.mybinder.org/user/lukeanglin-webapp-2vh99wk0/notebooks/categories/MLProjects/Notes/Keras-IMDB.ipynb)

The main takeaways: 

# Encoding 

Sometimes, we have categorical descriptions/sequences, like the reviews.  Here, we first encode them as sequences of integers mapping to words in a dictionary.  Then, we one-hot encode them into large binary sequences.  

This process **simplifies** our process, as binary classifaction is much more feasible 

# Validation Sets

A test set isn't enough.  We need a validation set too, to ensure that our model isn't overfitting *during training*.  

# Problem-Specific DL

Each problem in machine and deep learning is unique, and we must treat it as such.  Here, we learned about **binary classifation**. 

# Binary Classifaction

* Use `sigmoid` activation
    * Output should be a *probability* 
* `binary_crossentropy` is the proper loss function (crossentropy entails probability)
