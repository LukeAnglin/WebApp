---
export_on_save:
    html: true
title: Markov Chains
image: https://cdn-images-1.medium.com/max/800/1*jcbUF7dAhAIRS8nfUlNtow.gif
description: Learning about Markov Chains in the context of linear algebra
topics: Markov Chains
sources: 
publish: True
---

# What are Markov Chains?

![Markov Gif](https://miro.medium.com/max/516/1*jcbUF7dAhAIRS8nfUlNtow.gif)

Markov chains describe the **transition** from one state to another. 

Let's look at an example to better understand **what Markov chains are**. 

## Stock Market

Luke has taken up stock trading on Robinhood. He wants to trade based on the probability of whether the market is stagnant, bull or bear.

A depiction of the **transitions** in the stock market can be modeled by the following image: 

![Stocks](https://miro.medium.com/max/400/1*oqBd8eLkXyU-h0AhV-m73w.png)

Perhaps Luke starts off his new trading sequence in the Bull Market. Then, each day for the following month, he *chains* the correct description of the market on that day. 

His records are as follows: 

**January 1** - Bull Market 
**January 2** - Bull Market

*Continue, continue* . . . 

**January 30** - Stagnant
**January 31** - Stagnant

Where does the Markov chain come in? This transition of states could be modeled by a **transition matrix**, which in this case, is a <span class="red">stochastic matrix</span>, or one where **all the rows add up to one**. 

The number of rows, $n$, is equal to the number of states, and the number of columns, $m$ the probabilities of transitioning from one state to another.

# Markov Example 

Let's look at something we might model with a **transition matrix** and an <span class="red">initial state vector</span>, both of which we will understand as we work through this. 

On January 22, Luke decided to give up trying to model the entire market, and wanted to model whether the GameStop stock is growing or shrinking. He described the **growing** state as whether or not the GameStop stock had a **daily gain**, and the **shrinking** state will hold if the GameStop stock had a **daily loss**. 

![GameStop](https://images.mktw.net/im-290050?width=1260&size=1.7728531855955678)

Using his supreme wisdom, he decides that the GameStop stock has a probability of **0.1** of transitioning from the growth state to the shrinking state, and a probability of **0.01** of going from shrinking to growing. 

Let's see what the transition matrix looks like. Each entry in the matrix $(x, y)$ is the probability of going from state $x$ to $y$.

We let column 1 represent the **growing** state and column 2 represent the **shrinking** state. Then, we let row 1 represent being in the growing state and row 2 as being in the shrinking state. 

$$
A = 
\begin{bmatrix} 
0.9 & 0.1\\
0.05 & 0.95
\end{bmatrix}
$$

Okay. Now we need to put this in **matrix times vector** form. But what is our vector?

We start with the <span class="red">initial state vector</span> which describes which state we started in. Since Luke began on January 22, when the stock was growing, and row 1 represents the growing state, we let the first row of the vector be a 1, and the other component be a zero. 

$$
\vec{x} = \begin{bmatrix} 
1\\
0
\end{bmatrix}
$$

Note that **in this case** we only have ones and zeroes, because the states are <span class="red">mutually exclusive</span>. However, some Markov chains will not have mutually exclusive states, and therefore the initial state vector may have non-binary values. 

We can represent this as matrix vector multiplication now, where the product, $\vec{b}$ is equivalent to the probability distribution of being in a growing state or a shrinking state the next day. 

$$
A\vec{x} = \vec{b}\newline
A\vec{x} =  \begin{bmatrix} 
0.9 & 0.1\\
0.05 & 0.95
\end{bmatrix} * \begin{bmatrix} 
1\\
0
\end{bmatrix} = \vec{b} = \begin{bmatrix} 
0.9\\
0.1
\end{bmatrix} 
$$

This is fairly obvious. But, it's as we continue that this becomes powerful. What about the day after that? 

$$
A\vec{x} = \vec{b}\newline
A\vec{x} =  \begin{bmatrix} 
0.9 & 0.1\\
0.05 & 0.95
\end{bmatrix} * \begin{bmatrix} 
0.9\\
0.1
\end{bmatrix} = \vec{b} = \begin{bmatrix} 
0.815\\
0.185
\end{bmatrix} 
$$

By continuing this process, Luke will be able to get a better understanding of how GameStop will trend over the long run! 

# Steady State Vectors 

As we can imagine, that vector $\vec{b}$ that we kept changing little by little **eventually converges**, and that gives us the <span class="red">steady state vector</span>.  This is the vector that when multiplied by the stochastic matrix always results in the *same* vector. 

## Finding steady state vectors 

To find all steady state vectors for a stochastic matrix $A$, we take $A_{n \times m}$ and then multiply by a vector with $m$ components, and set that to that same vector. 

Let's see what that looks like. 

Let's go back to the GameStop transition matrix. We multiply that by a vector of $m$ components, $\vec{x}$, our **steady state vector**, and set that to zero. 

$$
\begin{bmatrix} 
0.1 & 0.9\\
0.05 & 0.95
\end{bmatrix} * 
\begin{bmatrix} x\\
y
\end{bmatrix} = \begin{bmatrix} x\\
y
\end{bmatrix} 
$$

We'll also use the fact that $x + y = 1$, because this is a **stochastic matrix**. Setting up the augmented matrix would give us
$$
\begin{bmatrix} 
0.1 & 0.9 & x\\
0.05 & 0.95 & y\\
1 & 1 & 1
\end{bmatrix}
$$

where the <span class="red">last column</span> are the constants, and columns 1 and 2 represent the coefficients of the variables. Obviously, we can't leave the variables like that! We subtract them over and leave ourselves with zeroes in those spots, giving us: 
$$
\begin{bmatrix} 
-0.1 & 0.9 & 0\\
0.05 & -0.95 & 0\\
1 & 1 & 1
\end{bmatrix}
$$

Solving the corresponding system through RREF row operations, we find that $x = \frac{1}{2}$ and $y = \frac{1}{2}$.

# More Real Life Examples 

We've already seen two real life examples of Markov chains. One with respect to the entire indexing of the stock market in terms of bear, bull, and stagnancy, and another with the GameStop phenomenon. 

However, the Markov chain is even more expansive. Some other applications include modeling weather patterns, consumer and sales data, and more! I recommend reading up more on them if you would like to learn about them in more depth than I cover in this summary. 


