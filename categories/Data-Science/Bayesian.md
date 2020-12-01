---
author: Luke
title: Bayesian Statistics
---
The relevant notebook can be found [here](../../MLProjects/Notes/Bayesian/Chapter1_Introduction/Ch1_Introduction_PyMC3.ipynb)

A wonderful [Kaggle notebook](https://www.kaggle.com/mrisdal/the-philosophy-of-bayesian-inference) summarizes it nicely. 
# Framework

The Bayesian framework is based on **conditional probabilities**. 


$$P(A|X) = \frac{P(X|A)\times P(A)}{P(X)}$$

Posterior probabilities lead us to update our theory.  

![BayesianPosterior](assets/BayesianPosterior.png)

The <span class="keyword1">wider</span> the curve, the greater the <span class="keyword1">uncertainty</span>. 

Often, we plot the <span class="keyword2">prior probability</span> vs the <span class="keyword2">posterior probability</span>.  The x value is the **initial probability**, and the y value is our **updated probability**. 

![](/assets/BayesianPosteriorBugGraph.png)

# Probability Distributions

## Discrete

For some discrete random variable $Z$, there is a pprobaility *mass* function $P(Z=k)$ which maps $k$ to a probability.  $k \in \N $ because it is discrete.  

**Discrete** variables follow the **Poisson** distribution.

$$
P(Z = k) =\frac{ \lambda^k e^{-\lambda} }{k!}, \; \; k=0,1,2, \dots
$$

### Poisson 

Denoted $Z \sim \text{Poi}(\lambda)$

Properties: 

* $\lambda$ is the *intensity* of the distribution.  **Patterns** of lambda include: 
    * **Increasing** means bigger values will give **bigger probabilities**
    * * **Decreasing** means smaller values will give **bigger probabilities**
* The <span class="keyword2">expected value </span>is equal to the parameter.

$$
E\large[ \;Z\; | \; \lambda \;\large] = \lambda
$$

Here's a depiction of the intensity factor, $\lambda$

![lambda-property](/assets/lambda-property.png)

## Continuous

Follows a probability *density* function. 

$$f_Z(z | \lambda) = \lambda e^{-\lambda z }, \;\; z\ge 0$$

A common case is the *exponential distribution* 

$$
Z \sim \text{Exp}(\lambda)
$$

### Properties

We have the **expected value identity** 

$$
E[\; Z \;|\; \lambda \;] = \frac{1}{\lambda}
$$

What does this mean in English?  For some random variable given some coefficient, the expected value of that random variable is equal to the inverse of the coefficient.

![lambda-for-continuous](https://i.imgur.com/HmgXEwF.png)

# Solving for Lambda

## Switchpoints

Consider graphing rain in Seattle.  Some spans of days are dry, and then all the sudden, it spikes.  One might model $\lambda$ with a piecewise function based on a **switchpoint**. 

$$
\lambda = 
\begin{cases}
\lambda_1  & \text{if } t \lt \tau \cr
\lambda_2 & \text{if } t \ge \tau
\end{cases}
$$

Here, $\tau$ is the switchpoint.  We can assign a uniform density function to it, that is, it could be on any one of the 70 days. 

## Lambda's Continuity

Lambda can be *any positive number*. Therefore, we need to model it with a PDF.  

The exponential density function takes a $\lambda$ of it's own.  Thus, we need to sub in another variable for that because we're trying to solve for $\lambda$

$$
\lambda_{1} \sim \text{Exp}(\alpha) \\
\lambda_{2} \sim \text{Exp}(\alpha)
$$

## Hyperparameters

Here, $\alpha$ is the **hyperparameter**, a parameter defining another variable.  Generally, these have *little effect* on the outcome as a whole.

Good practice is to set $\alpha$ to the inverse of the data's mean.  

Using our expected value identity . . . 

$$
\frac{1}{N}\sum_{i=0}^N \;C_i \approx E[\; \lambda \; |\; \alpha ] = \frac{1}{\alpha}
$$


