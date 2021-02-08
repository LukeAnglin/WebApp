---
export_on_save:
    html: true
title: Decision Trees with Sci-Kit Learn
image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJKVDHDE50DVQVlgNWSuq1FA6Ucii3MtL6Zw&usqp=CAU
description: Looking at Decision Trees in Sci-Kit Learn 
topics: Decision Trees
sources: <i>Hands on Machine Learning with Sci-Kit Learn</i>, and <a href="https://towardsdatascience.com/understanding-decision-tree-classification-with-scikit-learn-2ddf272731bd">this Medium article.</a>
publish: True
---

The relevant notebook can be found [here](https://nbviewer.jupyter.org/github/LukeAnglin/WebApp/blob/master/categories/MLProjects/Notes/Decision-Trees.ipynb)

A helpful article from Towards Data Science can be found [here](https://towardsdatascience.com/understanding-decision-tree-classification-with-scikit-learn-2ddf272731bd).
# Decision Trees 

We construct decision trees just like other classifiers in Sci-Kit.  Construct it, and fit it.  Predict when ready, and fine-tune.  

## Visualizing 

Use `export_graphviz` and use dot conversion to get a nice png of what your AI is doing.  

## Tree Properties

* Extremely little data cleaning.  
* Easy to understand
* Can predict *probabilities* (with `predict_proba`)
* Makes **few assumptions** about training data 

## Impurity 

The general measure of impurity is the **gini impurity**, which is a criterion to minimize the probability of misclassification. 

0 is pure-fect, 1 is impure.  

![Gini Impurity](https://miro.medium.com/max/500/1*sURE2Znb8ai1bzt9z7Kv5w.png)

## Node Properties

* **samples** - how many samples on the node
* **value** - how many of each class on the node 
* **gini** - the node's impurity.  

All of these are mirrored in Sci-Kit with the appropriate code naming convention (i.e., samples is `samples`)

### Root 

The **root node** should be the one with the <span class="red">least impurity</span>

## Regularization 

There are a few hyperparameters we can use to regularize.  If we don't do this, decision trees will grow large enough to perfectly fit (i.e. an infinite overfit)

The **best parameter** to lower to avoid overfitting is `max_depth`. 

* `min_samples_split` - The minimum number of samples a node must have for it to split.
* `min_samples_leaf` - The minimum number of samples a leaf must have.
* `min_weight_fraction_leaf` - `mean_samples_leaf` as a fraction.
* `max_leaf_nodes` - The maximum number of leaf nodes.
*  `max_features` - The maximum number of features that are evaluated for any split.

## Regression

Decision Trees can even be used for regression!  Simply use the `DecisionTreeRegressor` rather than the `DecisionTreeClassifier`.  

Note that this ends up predicting **discrete** values rather than continuous ones.  To clarify, here are some example predictions: 

![DTR](https://scikit-learn.org/stable/_images/sphx_glr_plot_tree_regression_001.png)

## CART

Decision Trees in Sci-Kit are constructed using the **CART** algorithm.  This seeks to minimize the impurity of both splits, and does so recursively.  

## Drawbacks 

* Orthogonal decision boundaries makes them sensitive to training rotation 
    * Use PCA to limit this effect 
* Sensitive to small changes in training data 

## Efficiency 

$O(log_2(m))$, so it's **very fast**.  

## Takeaways 

* Use `GridSearchCV` or `RandomSearchCV` to decide the `max_depth` and `max_leaf_nodes` in order to prevent overfitting
* Generally, hold off on Decision Tree Regression unless you're predicting **discrete** values 
* A fantastic **white box** model choice for classification 

# Ensemble 

Let's graduate from trees to forests.  We can improve accuracy by choosing the <span class="red">most frequent</span> prediction of a group of weak classifiers.  

Let's take Sci-Kit's `VotingClassifier` as an example

## VotingClassifier

This is a useful way to create ensembles.  It is based on the *wisdom of the crowd*, meaning the most frequent prediction wins. 

### Construction 

Pass tuples of string keys and model pairs.  Example: 

```
voting_clf = VotingClassifier(estimators = [('lr', log_clf), ('rf', random_forest_clf)])
```

## Bagging/Pasting 

