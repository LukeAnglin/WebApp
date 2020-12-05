With a multiclass problem like the Reuters dataset, we need to change some of our approaches.  

# Multiclass layering 

If you're trying to classify $N$ classes, you're output `Dense` layer should be of the same size $N$

# Encoding 

Generally, we'll be using one-hot-encoding with the `keras.utils.np_utils` module's `to_categorical()` function. 

# Activation 

For a multiclass problem, we want to use `softmax` activation, so it will output a probability distribution over the $N$ classes. 

# Loss 

Multiclass demands the `categorical_crossentropy` loss function, which minimizes the distance between our prediction probability distribution and the true distribution. 

# Advice

* Don't use too many layers, especially if they're small.  This leads to **information bottlenecks**. 
* One way to remedy overfitting and improve model accuracy is playing with the number of layers and hidden units you are using

