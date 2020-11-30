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


