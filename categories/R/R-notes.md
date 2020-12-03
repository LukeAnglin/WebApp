---
export_on_save:
    html: true
title: R for Stat
author: Luke Anglin
image: https://miro.medium.com/max/2404/1*WSZpEbx1J71GL7KZ4BOONQ.jpeg
description: R is a phenomenal, simply-syntaxed language for Statistics.  Similar to MATLAB in some respects, it may be the best choice for certain projects.  Note, however, that Python scripts may be better as things scale.
topics: R syntax, RStudio, Visualization in R, and statistical programming
---

# R

## RStudio

### Keybinds

| Run selection in terminal | <kbd> ⌘ Enter</kbd> |
| --- | --- |
| 

## Packages

<!-- Description of loading vs installing -->
<dl>
    <dt>Installing</dt>
    <dd>Putting it on your hard drive</dd>
    <dt>Loading</dt>
    <dd>Makes it <i>accessible</i></dd>
</dl>

### Getting Packages

```r
# No confirmation message
library("pacman")

# Confirmation message
require("pacman")
```
You can also simply check the box in the *packages* section of RStudio.


#### Sources

* GitHub
* [CRAN](https://cran.r-project.org/)

#### Common

* ggplot2
* rmarkdown
* shiny
* stringr
* pacman

### Clearing Packages

```r
detach("package: <package>", unload = TRUE)
```

To unload package(s)

```r
# Notice the lack of quotation marks.  This clears a specific package
p_unload(pacman)

# To clear all packages . . . 
p_unload(all)
```

### Visualization

#### Basic syntax

Easily plot bar charts of categorical variables with `<dataset>$<var>`{.r}
```r
plot(iris$Species)
```

To plot other pairs, use x as first parameter and y as second.

```r
plot(iris$Species, iris$Petal.Length)
```

You could also plot the **entire dataset** 

```r
plot(iris)
```

#### Specific Charts

##### Bar Plots

**Categorical variables!**

You cannot simply do `barplot(dataset$variable)`

Instead, convert to a table and *then* do that. 

```r
# Convert to table
cylinders <- table (mtcars$cyl)

# Plot the table
barplot(cylinders)
```

##### Histograms

**Quantitative Variables**

What are you looking for?

* Shape
* Gaps
* Outliers
* Symmetry

#### Plotting Functions

Pass the function, the xmin, and the xmax

```r
plot(dnorm, -3, 3)
```

#### Additional Parameters

Specify keyword arguments after the x and y

```r
plot(iris$Petal.Length, iris$Petal.width
col = "#cc0000",
pch = 19, # Solid circles
main = "Iris: Petal Length vs. Petal Width", #Title
xlab = "Petal Length",
ylab = "Petal Width")
)
```
### Help/Docs

```r
# Use question mark plus command to get help
?plot
```


<!-- END -->