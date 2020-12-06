---
export_on_save:
    html: true
title: Fundamentals of Machine Learning
author: Luke Anglin
image: https://miro.medium.com/max/2628/1*8wU0hfUY3UK_D8Y7tbIyFQ.png
description: The basics of machine learning
topics: Machine learning principles and essentials
sources: <i>Deep Learning with Python</i>
publish: False
---

# Types of Learning

## Supervised Learnings 

Some lesser known variants include: 

* Sequence generation - Here's a picture, tell me the caption. 
* Syntax tree prediction - NLP, give me the parts of speech decomposition. 
* Object deletion - Draw a bounding-box around the lymph nodes in this image 
* Image segmentation - Similar to object deletion, but pixel-level 

## Unsupervised

* Dimensionality reduction 
* Clustering 

## Self-supervised 

We make labels ourselves.  Autoencoders generate their own inputs to train themselves. 

## Reinforcement

An *agent* receives information about its environment and learns to choose actions to maximize a reward. 

Give a robot a game with a score.  Once he maximizes his score, he'll be trained the best to do his task. 

Currently, this field has less practical successes, but this gamification idea is going to be huge in education, resource management, and more.  Eventually, it will extend more into ML.  

# Terminology 

* **Target** - The truth - this is in contrast to *predictions*, or *output*
* **Ground Truth** - The set of targets
* **Loss** - Distance between predictions and targets 
* **Multilabel Classification** - Each input can map to multiple labels 
    * An image with a human and an elephant should be classified with *both labels* 
* **Multiclass Classification** - Non-binary, more than two classes 
* **Hyperparameter** - a parameter that influences other parameters 
    * The number of layers is a hyperparameter, because it influences the weights, which are parameters 
    * These are the reason we need **validation sets**
* **Data Representativeness** - If you're classifying something, don't train on classes 0-7 and test on 8-9! 
* **Arrow of Time** - When we are using time data, we have to train on the most recent data and test on the older.  Otherwise, we might end up with *temporal leaks*, where we are predicting on data from the future that we can't evaluate properly. 
* **Train-Test Redundancy** - If you have redundant samples in your train and test set, you're effectively *testing on your training data*. Ensure that your <span class="keyword1">validation and train sets are disjoint</span>!

# Validation Techniques

## Simple Hold-Out 

Cut out some data from the training set and validate on it.  Take say 20%.  What could go wrong?

![Simple Hold Out Validation](https://www.kdnuggets.com/wp-content/uploads/dataiku-holdout-strategy.jpg)

## K-Fold Shuffled 

K-Fold, but we iteratively shuffle our deck.  This means we end up with $P \times K$ total evaluations, where $P$ is the number of iterations, so this is taxing.  However, if we have **very little data**, it's worth it. 

# Over/Underfitting 

The optimization-generalization, bias-variance tradeoff.  What can we do?

## Solutions 

* Get more training data 
* **Regularization** helps with overfitting (e.g. Ridge and Lasso)

