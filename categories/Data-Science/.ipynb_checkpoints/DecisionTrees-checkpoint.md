---
export_on_save:
    html: true
title: Decision Trees with Sci-Kit Learn
image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJKVDHDE50DVQVlgNWSuq1FA6Ucii3MtL6Zw&usqp=CAU
description: Looking at Decision Trees in Sci-Kit Learn 
topics: Decision Trees
sources: <i>Hands on Machine Learning with Sci-Kit Learn</i>
publish: True
---

The relevant notebook can be found [here](https://nbviewer.jupyter.org/github/LukeAnglin/WebApp/blob/master/categories/MLProjects/Notes/Decision-Trees.ipynb)

# Decision Trees 

We construct decision trees just like other classifiers in Sci-Kit.  Construct it, and fit it.  Predict when ready, and fine-tune.  

## Visualizing 

Use `export_graphviz` and use dot conversion to get a nice png of what your AI is doing.  

## Tree Properties

* Extremely little data cleaning.  
* Easy to understand
* Can predict *probabilities* (with `predict_proba`)
* Makes **few assumptions** about training data 

## Node Properties

* **samples** - how many samples on the node
* **value** - how many of each class on the node 
* **gini** - the nodes impurity.  

All of these are mirrored in Sci-Kit with the appropriate code naming convention (i.e., samples is `samples`)

## Regularization 

There are a few hyperparameters we can use to regularize.  If we don't do this, decision trees will grow large enough to perfectly fit (i.e. an infinite overfit)

* `min_samples_split` - The minimum number of samples a node must have for it to split.
* `min_samples_leaf` - The minimum number of samples a leaf must have.
* `min_weight_fraction_leaf` - `mean_samples_leaf` as a fraction.
* `max_leaf_nodes` - The maximum number of leaf nodes.
*  `max_features` - The maximum number of features that are evaluated for any split.

## Regression

Decision Trees can even be used for regression!
