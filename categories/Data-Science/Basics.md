---
export_on_save: 
    html: true
title: Stat Basics 
author: Luke Anglin
image: https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Comparison_of_three_stock_indices_after_1975.svg/1200px-Comparison_of_three_stock_indices_after_1975.svg.png
description: Here lies the basics behind all stat.
topics: Hypotheses, p-values, indices, measures of location, sensitivity, robust measurements
---

# Indices 

Indices **summarize and rank** observations.  

![Indices](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Comparison_of_three_stock_indices_after_1975.svg/1200px-Comparison_of_three_stock_indices_after_1975.svg.png)

# Hypotheses 

* Null - nothing special. 
    * If we were trying to see if creatine made a difference, defining values as the *increase in muscle growth*, we would say $H_0 = 0$
* Alternative - special things going on here. 
    * Creatine *does* make a difference.  $H_A = 5 g$

# P-Values 

The p-value is the probability of the **observed outcome plus all "more extreme" outcomes** 

Consider flipping a coin.  Then, the p-value would be the sum of getting 19 heads and one tail or 20 heads and one tail (one-sided). 

![P-Values](https://www.simplypsychology.org/p-value.png)

# Variability

## Standard Error 

Standard error is similar to standard deviation, but is used for **confidence intervals**.  

![SE](https://www.wallstreetmojo.com/wp-content/uploads/2019/12/Standard-Error.jpg)

# Measures of Location 

## Weighted Means 

You have a sensor giving bad data a small portion of the time.  You can lower the weight of that sensor while still using it's *generally* decent data. 

<!-- Weighted Mean Images  -->
<div class="row">
    <div class="col-6 thumb">
        <a class="thumbnail" href="#">
            <img class="img-responsive" src="https://www.mathsisfun.com/data/images/weighted-average-seesaw.svg" alt="">
        </a>
    </div>
    <div class="col-6 thumb">
        <a class="thumbnail" href="#">
            <img class="img-responsive" src="https://www.wikihow.com/images/thumb/5/56/Calculate-Weighted-Average-Step-3-Version-7.jpg/v4-460px-Calculate-Weighted-Average-Step-3-Version-7.jpg" alt="">
        </a>
    </div>
</div>

## Trimmed Means 

![Trimmed Means](https://images.slideplayer.com/27/9207184/slides/slide_6.jpg)

The Great Depression was full of inflation spikes.  To get rid of these outliers, a trimmed mean would be useful.  

## Sensitivity 

Variance and standard deviation are sensitive to outliers, despite their commonality.  

### Example in R 

```r
sd(data[["population"]])
iqr(data[["population"]])
                            
# May have drastically different outputs.  A better choice might be:
                            
mad(data[["population"]]) 

# Or perhaps

quantile(state[["Murder.Rate"]],p=c(.05,.25,.5,.75,.95))
```

## Robust Measures 

* Median 
* MAD - Mean Absolute Difference 
* Robust ANOVA 
* Robust Regression 
* Percentiles 

