---
export_on_save:
    html: true
title: Choosing Models
author: Luke Anglin
image: https://scikit-learn.org/stable/_static/ml_map.png
description: How to choose the right model for machine learning
topics: Model choice, linear models, Bayes Theorem
sources: https://towardsdatascience.com/probability-learning-ii-how-bayes-theorem-is-applied-in-machine-learning-bd747a960962
publish: true
---

# Bayes Theorem 

The foundation behind model **learning**.  This is how we update our beliefs.  

Consider a linear regression.  Rather than the slopes (the ) being constant, we turn them into **distributions** 

## Regressive 

We iteratively tweak thetas based on prior probabilities, and then use the posterior probabilities as the prior.  Then repeat.  

![Applied formula](https://miro.medium.com/max/480/1*gdgddVSaJQ_BXWJJNYtZ9g.png)

![Posterior thetas](https://miro.medium.com/max/486/1*KmnRZ_zc_cD7CIWylEyrFg.png)

## Classifiers 

Fairly similar approach, only difference is that we use a density function $P(X)$ and define a class rather than a model in the equation.  

![Bayes-Classification](https://miro.medium.com/max/502/1*c63H7VlsTrcntMc5P2v7aw.png)

## Maximum Likelihood

Fit a distribution to the data to make it easier to work with.  Think Poisson, Gaussian, Exponential . . . 

![](https://miro.medium.com/max/700/1*twrMncyWo2RV21D_9QVZgA.png)

# Linear

## Linear Regression

* $O(n^3)$ complexity
* Least Squares
* **Overfitting** problems

## SGD

Stochastic Gradient Descent iteratively minimizes the error by taking small steps.  

## Ridge, Lasso, Elastic-Net

These regressions minimize the overfitting problems of least squares.  They are **regularizing** estimators.  

When should I use each?



Estimator | Many Variables | Most Variables Useful
---------|----------|---------
Ridge | No | Yes
Lasso | Yes | No
 Elastic-Net | Yes | Yes

## Keep in mind 

* Data should **not be noisy**
* Many variables generally hurts linear regressions 
    * Removing collinearity is beneficial with many variables.  This may involve calculating *pairwise* correlations

# Probablistic

## Odds and Log(Odds)

First, let's understand odds and log(odds). 

$$
\text{odds} = \frac{success}{failure}
$$

Or, we can use *probabilities* to calculate odds. 

$$
\text{odds} = \frac{P(success)}{1-P(success)}
$$

or, even more simply 
$$
\text{odds} = \frac{p}{1-p}
$$

### Odds Properties

**Favorable** odds - $(1, \infin)$
**Unfavorable**  odds- $(0, 1)$

Those don't seem very symmetric, because they aren't.  And that's not good for ML.  Let's fix that with *log odds.*

### Log Odds

Log odds make our odds better suited for classification, because it often makes the distribution *more normal*. 

$$
\log(\text{odds}) = \log(\frac{p}{1-p})
$$

This is also known as the *logit* function.

![Log Odds Histogram](https://miro.medium.com/max/1200/1*zMJ7QJ5E1iJKmPr1PvfMCw.png)

## Logistic Regression 

The name is incredibly ridiculous considering we use this as a classifier.  But I digress.  

Oh, one more thing.  It's a linear model - a **generalized linear model**, to be exact.  Okay, now we're ready. 

### 

We calculate probabilities of class membership using a sigmoid function. 

![](https://miro.medium.com/max/287/0*59BSXTBcxZcZGtVT)

Step 1:  Calculate our $\theta$s, using, say, Maximum Likelihood 

![](https://miro.medium.com/max/246/0*vq7V-FuK9EirWDeN)

Step 2: Calculate the probability of being whatever class 

![](https://miro.medium.com/max/449/0*p5Yczl6itusXkxN8)

We need to recognize that logistic regression creates that squiggly line on the graph where the y axis is probabilities, from 0 to 1.  

**But** when we take the $\log(odds)$ of that graph, it transforms into a line, with coefficients we can use. 

![Linear Logistic Reg Depiction](https://miro.medium.com/max/435/1*TRW0vVdhjOmRfp0UZDTDeA.png)

Here's a helpful logistic regression video (and some useful info on t-tests) from [StatQuest](https://www.youtube.com/watch?v=vN5cNN2-HWE&feature=emb_rel_pause)!

# Kernel Methods 

Attempt to classify with **decision boundaries**

## SVMs

![SVM](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/SVM_margin.png/300px-SVM_margin.png)

Orders: 

1. Based on the number of features, create a boundary in a higher-dimensional system.  
2. Maximize the difference betweeen the hyperplane and the closest data points.  

![Kernel Visualized](https://miro.medium.com/max/1676/1*mCwnu5kXot6buL7jeIafqQ.png)

How it's done: 

A kernel function is utilized to map two points to the distance btween them.  When we've gotten the greatest distances, we're done. 

![Kernel Function Examples](https://www.researchgate.net/profile/Jui-Sheng_Chou/publication/239386696/figure/tbl2/AS:667912230674445@1536254093339/SVM-Kernel-Function-Types.png)

### The Downfall

Requires most features to be useful.  Therefore, if you have some which might not be, you have to **feature engineer** to remove them.

# Forests and Gradient Boost

## Random Forests 

Random forests are easy to understand and visualize.  Just take a look at the below decision tree. Then, imagine a bunch of these *ensembled* to make a final decision.  

![](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/05/rfc_vs_dt11.png)

## Gradient Boosts 

I group gradient boosts with Random Forest because gradient boost tends to be an ensemble of random forests and, maybe, some other ML algorithms.  To date, gradient boosts provide **the best** algorithm for classifications.  

What makes these really special is the <span class="keyword1">iterative tweaking</span> that they perform.  Imagine your random forest is on a domain of [0, 1], and it performs great everywhere except in the (0.4, 0.6) range.  

Gradient boost says:  "Hey, let's train a *new* algorithm in that range.  Then, we're good everywhere"

One last thing to note.  Gradient boost uses *lots* of *weak* classifiers.  

![](https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-3-030-34482-5_25/MediaObjects/482246_1_En_25_Fig2_HTML.png)


