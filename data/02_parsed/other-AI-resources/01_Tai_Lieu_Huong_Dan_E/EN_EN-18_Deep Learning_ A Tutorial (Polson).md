<!-- page: 1 -->

# Deep Learning: A Tutorial

Nick Polson[^*]     Vadim Sokolov[^†]

2023-10-09

arXiv:2310.06251v1 [stat.ML] 10 Oct 2023

## 1 Introduction

Our goal is to provide a review of deep learning methods which provide insight into structured high-dimensional data. Rather than using shallow additive architectures common to most statistical models, deep learning uses layers of semi-affine input transformations to provide a predictive rule. Applying these layers of transformations leads to a set of attributes (or, features) to which probabilistic statistical methods can be applied. Thus, the best of both worlds can be achieved: scalable prediction rules fortified with uncertainty quantification, where sparse regularization finds the features.

Deep learning is one of the widely used machine learning method for analysis of large scale and high-dimensional data sets. Large-scale means that we have many samples (observations) and high dimensional means that each sample is a vector with many entries, usually hundreds and up.

Machine learning is the engineer's version of statistical data analysis. Major difference between ML and statistics is that ML focuses on practical aspects, such as computational efficiency and ease of use of techniques. While statistical analysis is more concerned with rigorousness of the analysis and interpretability of the results.

Deep learning provides a powerful pattern matching tool suitable for many AI applications. Image recognition and text analysis are probably two of the deep learning's most successful. From a computational perspective, you can think of an image or a text as a high dimensional matrices and vectors, respectively. The problem of recognizing objects in images or translating a text requires designing complex decision boundaries in the high dimensional space of inputs.

Although, image analysis and natural language processing are the applications where deep learning is the dominating approach, more traditional engineering and science applications, such as spatio-temporal and financial analysis is where DL also showed superior performance compared to traditional statistical learning techniques (Heaton et al. 2017; Polson and Sokolov 2017, 2023; Sokolov 2017; Dixon et al. 2019; Polson and Sokolov 2020; Behnia et al. 2021; Bhadra et al. 2021; Polson et al. 2021; Nareklishvili et al. 2022a, b; 2023; Wang et al. 2022)

There are several deep learning architectures exist - each has its own uses and purposes. Convolutional Neural Networks (CNN) deal with 2-dimensional input objects, i.e. images and were shown to outperform any other techniques. Recurrent Neural Networks (RNN) were shown the best performance on speech and text analysis tasks.

In general, a neural network can be described as follows. Let \(f_1, \ldots, f_L\) be given *univariate* activation functions for each of the \(L\) layers. Activation functions are nonlinear transformations of weighted data. A semi-affine activation rule is then defined by

$$
f_l^{W,b} = f_l\left(\sum_{j=1}^{N_l} W_{lj} X_j + b_l\right) = f_l\left(W_l X_l + b_l\right),
$$

[^*]: University of Chicago, ngp@chicagobooth.edu

[^†]: George Mason University, vsokolov@gmu.edu

1

<!-- page: 2 -->

which implicitly needs the specification of the number of hidden units \(N_l\). Our deep predictor, given the number of layers \(L\), then becomes the composite map

$$
\hat{Y}(X) = F(X) = \left(f_l^{W_1,b_1} \circ \ldots \circ f_L^{W_L,b_L}\right)(X).
$$

The fact that DL forms a universal 'basis' which we recognise in this formulation dates to Poincare and Hilbert is central. From a practical perspective, given a large enough data set of "test cases", we can empirically learn an optimal predictor.

Similar to a classic basis decomposition, the deep approach uses univariate activation functions to decompose a high dimensional \(X\).

Let \(Z^{(l)}\) denote the \(l\)th layer, and so \(X = Z^{(0)}\). The final output \(Y\) can be numeric or categorical. The explicit structure of a deep prediction rule is then

$$
\begin{aligned}
\hat{Y}(X) &= W^{(L)} Z^{(L)} + b^{(L)} \\
Z^{(1)} &= f^{(1)}\left(W^{(0)} X + b^{(0)}\right) \\
Z^{(2)} &= f^{(2)}\left(W^{(1)} Z^{(1)} + b^{(1)}\right) \\
&\ldots \\
Z^{(L)} &= f^{(L)}\left(W^{(L-1)} Z^{(L-1)} + b^{(L-1)}\right).
\end{aligned}
$$

Here \(W^{(l)}\) is a weight matrix and \(b^{(l)}\) are threshold or activation levels. Designing a good predictor depends crucially on the choice of univariate activation functions \(f^{(l)}\). The \(Z^{(l)}\) are hidden features which the algorithm will extract.

Put differently, the deep approach employs hierarchical predictors comprising of a series of \(L\) nonlinear transformations applied to \(X\). Each of the \(L\) transformations is referred to as a *layer*, where the original input is \(X\), the output of the first transformation is the first layer, and so on, with the output \(\hat{Y}\) as the first layer. The layers 1 to \(L\) are called *hidden layers*. The number of layers \(L\) represents the *depth* of our routine.

Traditional statistical models are estimated by maximizing likelihood and using the least squares algorithm for linear regression and weighted least squares or Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm for generalized linear models.

## 2 Deep Learning and Least Squares

The deep learning model approximates the relation between inputs \(x\) and outputs \(y\) using a non-linear function \(f(x,\theta)\), where \(\theta\) is a vector of parameters. The goal is to find the optimal value of \(\theta\) that minimizes the expected loss function, given a training data set \(D = \{x_i, y_i\}_{i=1}^{n}\). The loss function is a measure of discrepancy between the true value of \(y\) and the predicted value \(f(x,\theta)\). The loss function is usually defined as the negative log-likelihood function of the model.

$$
l(\theta) = -\sum_{i=1}^{n} \log p(y_i|x_i,\theta),
$$

where \(p(y_i|x_i,\theta)\) is the conditional distribution of \(y_i\) given \(x_i\) and \(\theta\). Thus, in the case of regression, we have

$$
y_i = f(x_i,\theta) + \epsilon,\ \epsilon \sim N(0,\sigma^2),
$$

Thus, the loss function is

$$
l(\theta) = -\sum_{i=1}^{n} \log p(y_i|x_i,\theta) = \sum_{i=1}^{n} (y_i - f(x_i,\theta))^2,
$$

2

<!-- page: 3 -->

### 2.1 Regresson

Regression is simply a neural network which is wide and shallow. The insight of DL is that you use a deep and shallow neural network. Let's look at a simple example and fit a linear regression model to `iris` dataset.

```r
data(iris)
y = iris$Petal.Length
# initialize theta
theta <- matrix(c(0, 0), nrow = 2, ncol = 1)
# learning rate
alpha <- 0.0001
# number of iterations
n_iter <- 1000
# gradient descent
for (i in 1:n_iter) {
    # compute gradient
    grad <- -2 * t(x) %*% (y - x %*% theta)
    # update theta
    theta <- theta - alpha * grad
}
```

Our gradient descent finds the following coefficients

| Intercept (\(\theta_1\)) | Petal.Width (\(\theta_2\)) |
|---:|---:|
| 1.1 | 2.2 |

Let's plot the data and model estimated using gradient descent

```r
plot(x[,2],y,pch=16, xlab="Petal.Width")
abline(theta[2],theta[1], lwd=3,col="red")
```

[FIGURE: Scatter plot of the iris data with the regression line estimated by gradient descent]

Text in figure:
- y (vertical axis label)
- 1, 2, 3, 4, 5, 6, 7 (vertical axis ticks)
- 0.5, 1.0, 1.5, 2.0, 2.5 (horizontal axis ticks)
- Petal.Width (horizontal axis label)

Let's compare it to the standard estimation algorithm

```r
m = lm(Petal.Length~Petal.Width, data=iris)
```

3

<!-- page: 4 -->

| (Intercept) | Petal.Width |
|---:|---:|
| 1.1 | 2.2 |

The values found by gradient descent are very close to the ones found by the standard OLS algorithm.

### 2.2 Logistic Regression

Logistic regression is a generalized linear model (GLM) with a logit link function, defined as:

$$
\log\left(\frac{p}{1-p}\right) = \theta_0 + \theta_1 x_1 + \ldots + \theta_p x_p,
$$

where \(p\) is the probability of the positive class. The negative log-likelihood function for logistic regression is a cross-entropy loss

$$
l(\theta) = -\sum_{i=1}^{n} \left[y_i \log p_i + (1-y_i)\log(1-p_i)\right],
$$

where \(p_i = 1/\left(1 + \exp(-\theta_0 - \theta_1 x_{i1} - \ldots - \theta_p x_{ip})\right)\). The derivative of the negative log-likelihood function is

$$
\nabla l(\theta) = -\sum_{i=1}^{n} \left[y_i - p_i\right] \begin{pmatrix} 1 \\ x_{i1} \\ \vdots \\ x_{ip} \end{pmatrix}.
$$

In matrix notations, we have

$$
\nabla l(\theta) = -X^T(y - p).
$$

Let's implement gradient descent algorithm now.

```r
y = ifelse(iris$Species=="setosa",1,0)
x = cbind(rep(1,150),iris$Sepal.Length)
lrgd  = function(x,y, alpha, n_iter) {
  theta <- matrix(c(0, 0), nrow = 2, ncol = 1)
  for (i in 1:n_iter) {
    # compute gradient
    p = 1/(1+exp(-x %*% theta))
    grad <- -t(x) %*% (y - p)
    # update theta
    theta <- theta - alpha * grad
  }
  return(theta)
}
theta = lrgd(x,y,0.005,20000)
```

The gradient descent parameters are

| Intercept (\(\theta_1\)) | Sepal.Length (\(\theta_2\)) |
|---:|---:|
| 28 | -5.2 |

And the plot is

```r
par(mar=c(4,4,0,0), bty='n')
plot(x[,2],y,pch=16, xlab="Sepal.Length")
lines(x[,2],p,type='p', pch=16,col="red")
```

4

<!-- page: 5 -->

[FIGURE: Scatter plot of the binary response against Sepal.Length with the fitted logistic probabilities]

Text in figure:
- y (vertical axis label)
- 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 (vertical axis ticks)
- 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0 (horizontal axis ticks)
- Sepal.Length (horizontal axis label)

Let's compare it to the standard estimation algorithm

```r
glm(y~x-1, family=binomial(link="logit"))
#>
#> Call:  glm(formula = y ~ x - 1, family = binomial(link = "logit"))
#>
#> Coefficients:
#>    x1     x2
#> 27.83  -5.18
#>
#> Degrees of Freedom: 150 Total (i.e. Null);  148 Residual
#> Null Deviance:       208
#> Residual Deviance: 72    AIC: 76
```

### 2.3 Model Estimation

Deep learning as well as a large number of statistical problems, can be expressed in the form

$$
\min l(x) + \phi(x).
$$

In learning \(l(x)\) is the negative log-likelihood and \(\phi(x)\) is a penalty function that regularizes the estimate. From the Bayesian perspective, the solution to this problem may be interpreted as a maximum a posteriori

$$
p(y \mid x) \propto \exp\{-l(x)\},\ p(x) \propto \exp\{-\phi(x)\}.
$$

Second order optimisation algorithms, such as BFGS used for traditional statistical models do not work well for deep learning models. The reason is that the number of parameters a DL model has is large and estimating second order derivatives (Hessian or Fisher information matrix) becomes prohibitive from both computational and memory use standpoints. Instead, first order gradient descent methods are used for estimating parameters of a deep learning models.

The problem of parameter estimation (when likelihood belongs to the exponential family) is an optimisation problem

$$
\min_{\theta} l(\theta) := \frac{1}{n}\sum_{i=1}^{n} \log p(y_i, f(x_i,\theta))
$$

5

<!-- page: 6 -->

where \(l\) is the negative log-likelihood of a sample, and \(\theta\) is the vector of parameters. The gradient descent method is an iterative algorithm that starts with an initial guess \(\theta^0\) and then updates the parameter vector \(\theta\) at each iteration \(t\) as follows:

$$
\theta^{t+1} = \theta^{t} - \alpha_t \nabla l(\theta^t).
$$

Let's demonstrate these algorithms on a simple example of linear regression. We will use the `mtcars` data set and try to predict the fuel consumption (mpg) \(y\) using the number of cylinders (cyl) as a predictor \(x\). We will use the following model:

$$
y_i = \theta_0 + \theta_1 x_i + \epsilon_i,
$$

or in matrix form

$$
y = X\theta + \epsilon,
$$

where \(\epsilon_i \sim N(0,\sigma^2)\), \(X = [1\ x]\) is the design matrix with first column beign all ones.

The negative log-likelihood function for the linear regression model is

$$
l(\theta) = \sum_{i=1}^{n} (y_i - \theta_0 - \theta_1 x_i)^2.
$$

The gradient then is

$$
\nabla l(\theta) = -2\sum_{i=1}^{n} (y_i - \theta_0 - \theta_1 x_i) \begin{pmatrix} 1 \\ x_i \end{pmatrix}.
$$

In matrix form, we have

$$
\nabla l(\theta) = -2X^T(y - X\theta).
$$

Now, we demonstrate the gradient descent for estimating a generalized linear model (GLM), namely logistic regression. We will use the `iris` data set again and try to predict the species of the flower using the petal width as a predictor. We will use the following model

$$
\log\left(\frac{p_i}{1-p_i}\right) = \theta_0 + \theta_1 x_i,
$$

where \(p_i = P(y_i = 1)\) is the probability of the flower being of the species \(y_i = 1\) (setosa).

The negative log-likelihood function for logistic regression model is

$$
l(\theta) = -\sum_{i=1}^{n} \left[y_i \log p_i + (1-y_i)\log(1-p_i)\right],
$$

where \(p_i = 1/\left(1 + \exp(-\theta_0 - \theta_1 x_i)\right)\). The derivative of the negative log-likelihood function is

$$
\nabla l(\theta) = -\sum_{i=1}^{n} \left[y_i - p_i\right] \begin{pmatrix} 1 \\ x_i \end{pmatrix}.
$$

In matrix notations, we have

$$
\nabla l(\theta) = -X^T(y - p).
$$

### 2.4 Stochastic Gradient Descent

Stochastic gradient descent (SGD) is a variant of the gradient descent algorithm. The main difference is that instead of computing the gradient over the whole data set, SGD computes the gradient over a randomly selected subset of the data. This allows SGD to be applied to estimate models when data set is too large to fit into memory, which is often the case with the deep learning models. The SGD algorithm replaces

6

<!-- page: 7 -->

the gradient of the negative log-likelihood function with the gradient of the negative log-likelihood function computed over a randomly selected subset of the data

$$
\nabla l(\theta) \approx \frac{1}{|B|}\sum_{i \in B} \nabla l(y_i, f(x_i,\theta)),
$$

where \(B \in \{1, 2, \ldots, n\}\) is the batch samples from the data set. This method can be interpreted as gradient descent using noisy gradients, which are typically called mini-batch gradients with batch size \(|B|\).

The SGD is based on the idea of stochastic approximation introduced by Robbins and Monro (1951). Stochastic simply replaces \(F(l)\) with its Monte Carlo approximation.

In a small mini-batch regime, when \(|B| \ll n\) and typically \(|B| \in \{32, 64, \ldots, 1024\}\) it was shown that SGD converges faster than the standard gradient descent algorithm, it does converge to minimizers of strongly convex functions (negative log-likelihood function from exponential family is strongly convex) (Bottou et al. 2018) and it is more robust to noise in the data (Hardt et al. 2016). Further, it was shown that it can avoid saddle-points, which is often an issue with deep learning log-likelihood functions. In the case of multiple-minima, SGD can find a good solution LeCun et al. (2002), meaning that the out-of-sample performance is often worse when trained with large- batch methods as compared to small-batch methods.

Now, we implement SGD for logistic regression and compare performance for different batch sizes

```r
lrgd_minibatch  = function(x,y, alpha, n_iter, bs) {
  theta <- matrix(c(0, 0), nrow = 2, ncol = n_iter+1)
  n = length(y)
  for (i in 1:n_iter) {
    s = ((i-1)*bs+1)%%n
    e = min(s+bs-1,n)
    xl = x[s:e,]; yl = y[s:e]
    p = 1/(1+exp(-xl %*% theta[,i]))
    grad <- -t(xl) %*% (yl - p)
    # update theta
    theta[,i+1] <- theta[,i] - alpha * grad
  }
  return(theta)
}
```

Now run our SGD algorithm with different batch sizes.

```r
set.seed(92) # kuzy
ind = sample(150)
y = ifelse(iris$Species=="setosa",1,0)[ind] # shuffle data
x = cbind(rep(1,150),iris$Sepal.Length)[ind,] # shuffle data
nit=200000
lr = 0.01
th1 = lrgd_minibatch(x,y,lr,nit,5)
th2 = lrgd_minibatch(x,y,lr,nit,15)
th3 = lrgd_minibatch(x,y,lr,nit,30)
```

7

<!-- page: 8 -->

[FIGURE: Plot of \(\theta_1\) against iteration for three batch sizes]

Text in figure:
- \(\theta_1\) (vertical axis label)
- 0, 5, 10, 15, 20, 25, 30 (vertical axis ticks)
- Batch Size (legend title)
- 5, 15, 30 (legend entries)
- 0, 50, 100, 150, 200 (horizontal axis ticks)
- Iteration (horizontal axis label)

We run it with \(2 \times 10^5\) iterations and the learning rate of 0.01 and plot the values of \(\theta_1\) every 1000 iteration. There are a couple of important points we need to highlight when using SGD. First, we shuffle the data before using it. The reason is that if the data is sorted in any way (e.g. by date or by value of one of the inputs), then data within batches can be highly correlated, which reduces the convergence speed. Shuffling helps avoiding this issue. Second, the larger the batch size, the smaller number of iterations are required for convergence, which is something we would expect. However, in this specific example, from the number of computation point of view, the batch size does not change the number calculations required overall. Let's look at the same plot, but scale the x-axis according to the amount of computations

```r
plot(ind/1000,th1[1,ind], type='l', ylim=c(0,33), col=1, ylab=expression(theta[1]), xlab="Iteration")
abline(h=27.83, lty=2)
lines(ind/1000*3,th2[1,ind], type='l', col=2)
lines(ind/1000*6,th3[1,ind], type='l', col=3)
legend("bottomright", legend=c(5,15,30),col=1:3, lty=1, bty='n',title = "Batch Size")
```

[FIGURE: Plot of \(\theta_1\) against iteration for three batch sizes, with the x-axis scaled by the amount of computations]

Text in figure:
- \(\theta_1\) (vertical axis label)
- 0, 5, 10, 15, 20, 25, 30 (vertical axis ticks)
- Batch Size (legend title)
- 5, 15, 30 (legend entries)
- 0, 50, 100, 150, 200 (horizontal axis ticks)
- Iteration (horizontal axis label)

There are several important considerations about choosing the batch size for SGD.

- The larger the batch size, the more memory is required to store the data.
- Parallelization is more efficient with larger batch sizes. Modern harware supports parallelization of

8

<!-- page: 9 -->

  matrix operations, which is the main operation in SGD. The larger the batch size, the more efficient the parallelization is. Usually there is a sweet spot \(|B|\) for the batch size, which is the largest batch size that can fit into the memory or parallelized. Meaning it takes the same amount of time to compute SGD step for batch size 1 and B.

- Third, the larger the batch size, the less noise in the gradient. This means that the larger the batch size, the more accurate the gradient is. However, it was empirically shown that in many applications we should prefer noisier gradients (small batches) to obtain high quality solutions when the objective function (negative log-likelihood) is non-convex (Keskar et al. 2016).

## 3 Feed-Forward ReLu Neural Networks

Now we will turn out attention to the second and the more important, the model itself. We will start with a simple neural network with one hidden layer and will motivate it using a problem of binary classification on a simulated data set. We start by generating a simple dataset shown in Figure below. The data is generated from a mixture of two distributions (Gaussian and truncated Gaussian). The red points are the positive class and the green points are the negative class. The goal is to find a model boundary that discriminates the two classes.

[FIGURE: Scatter plot of the simulated two-class data set]

Text in figure:
- x2 (vertical axis label)
- −10, −5, 0, 5, 10 (vertical axis ticks)
- −10, −5, 0, 5, 10 (horizontal axis ticks)
- x1 (horizontal axis label)

We can see that a logistic regression could not do it. It uses a single line to separate observations of two classes.

```r
# Fit a logistic regression model
fit = glm(label~x1+x2, data=as.data.frame(d), family=binomial(link='logit'))
# Plot the training dataset
plot(d[,2],d[,3], col=d[,1]+2, pch=16, xlab="x1", ylab="x2")
th = fit$coefficients
# Plot the decision boundary
abline(-th[1]/th[3], -th[2]/th[3], col=2)
```

9

<!-- page: 10 -->

[FIGURE: Scatter plot of the simulated data with the logistic regression decision boundary]

Text in figure:
- x2 (vertical axis label)
- −10, −5, 0, 5, 10 (vertical axis ticks)
- −10, −5, 0, 5, 10 (horizontal axis ticks)
- x1 (horizontal axis label)

Indeed, the line found by the logistic regression is not able to separate the two classes. We can see that the data is not linearly separable. However, we can use multiple lines to separate the data.

```r
plot(x1~x2, data=d,col=d[,1]+2, pch=16)
# Plot lines that separate once class (red) from another (green)
lines(x1, -x1 - 6); text(-4,-3,1)
lines(x1, -x1 + 6); text(4,3,2)
lines(x1, x1 - 6); text(4,-3,3)
lines(x1, x1 + 6); text(-3,4,4)
```

[FIGURE: Scatter plot of the simulated data with four separating lines labelled 1, 2, 3 and 4]

Text in figure:
- x1 (vertical axis label)
- −10, −5, 0, 5, 10 (vertical axis ticks)
- 1, 2, 3, 4 (line labels)
- −10, −5, 0, 5, 10 (horizontal axis ticks)
- x2 (horizontal axis label)

Now, we do the same thing as in simple logistic regression and apply logistic function to each of those lines

```r
# Define sigmoid function
sigmoid = function(z)
  return(exp(z)/(1+exp(z)))

# Define hidden layer of our neural network
features = function(x1,x2) {
  z1 = 6 + x1 + x2; a1 = sigmoid(z1)
```

10

<!-- page: 11 -->

```r
  z2 =  6 - x1 - x2; a2 = sigmoid(z2)
  z3 =  6 - x1 + x2; a3 = sigmoid(z3)
  z4 =  6 + x1 - x2; a4 = sigmoid(z4)
  return(c(a1,a2,a3,a4))
}
```

Using the matrix notaitons, we have

$$
z = \sigma(Wx + b),\ W = \begin{bmatrix} 1 & 1 \\ -1 & -1 \\ -1 & 1 \\ 1 & -1 \end{bmatrix},\ b = \begin{bmatrix} 6 \\ 6 \\ 6 \\ 6 \end{bmatrix},\ \sigma(z) = \frac{1}{1 + e^{-z}}
$$

The model shown above is the first layer of our neural network. It takes a two-dimensional input \(x\) and produces a four-dimensional output \(z\) which is a called a feature vector. The feature vector is then passed to the output layer, which applies simple logistic regression to the feature vector.

$$
\hat{y} = \sigma(w^T z + b),\ w = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix},\ b = -3.1,\ \sigma(z) = \frac{1}{1 + e^{-z}}
$$

The output of the output layer is the probability of the positive class.

```r
# Calculate prediction (classification) using our neural network
predict_prob = function(x){
  x1 = x[1]; x2 = x[2]
  z = features(x1,x2)
  # print(z)
  mu = sum(z) - 3.1
  # print(mu)
  sigmoid(mu)
}
```

We can use our model to do the predictions now

```r
# Predict the probability of the positive class for a given point
predict_prob(c(0,0))
#> [1] 0.71
predict_prob(c(0,10))
#> [1] 0.26
```

The model generates sensible predictions, let's plot the decision boundary to see how well it separates the data.

```r
x1 = seq(-11,11,length.out = 100)
x2 = seq(-11,11,length.out = 100)
gr = as.matrix(expand.grid(x1,x2));
#> [1] 10000     2
yhat = apply(gr,1,predict_prob)
#> [1] 10000
image(x1,x2,matrix(yhat,ncol = 100), col = heat.colors(20,0.7))
```

11

<!-- page: 12 -->

[FIGURE: Decision surface of the neural network with the four separating lines labelled 1, 2, 3 and 4]

Text in figure:
- x2 (vertical axis label)
- −10, −5, 0, 5, 10 (vertical axis ticks)
- 1, 2, 3, 4 (line labels)
- −10, −5, 0, 5, 10 (horizontal axis ticks)
- x1 (horizontal axis label)

## 4 Automatic Differentiation (Backpropagation)

To calculate the value of the gradient vector, at each step of the optimization process, deep learning libraries require calculations of derivatives. In general, there are three different ways to calculate those derivatives. First, is numerical differentiation, when a gradient is approximated by a finite difference \(f'(x) = (f(x+h) - f(x))/h\) and requires two function evaluations. However, the numerical differentiation is not backward stable (Griewank et al. 2012), meaning that for a small perturbation in input value \(x\), the calculated derivative is not the correct one. Second, is a symbolic differentiation which has been used in symbolic computational frameworks such as `Mathematica` or `Maple` for decades. Symbolic differentiation uses a tree form representation of a function and applies chain rule to the tree to calculate the symbolic derivative of a given function. Figure @ref(fig:comp-graph) shows a tree representation of of composition of affine and sigmoid functions (the first layer of our neural network).

[FIGURE: Figure 1. Computational graph of the first layer of our neural network]

Text in figure:
- layer1
- w [2,4]
- x [200,2]
- b [4]
- dot [200,4]
- add [200,4]
- neg [200,4]
- exp [200,4]
- 1
- add [200,4]
- output div [200,4]

Figure 1: Computational graph of the first layer of our neural network

The advantage of symbolic calculations is that the analytical representation of derivative is available for further analysis. For example, when derivative calculation is in an intermediate step of the analysis. Third way to calculate a derivative is to use automatic differentiation (AD). Similar to symbolic differentiation, AD recursively applies the chain rule and calculates the exact value of derivative and thus avoids the problem of

12

<!-- page: 13 -->

numerical instability. The difference between AD and symbolic differentiation is that AD provides the value of derivative evaluated at a specific point, rather than an analytical representation of the derivative.

AD does not require analytical specification and can be applied to a function defined by a sequence of algebraic manipulations, logical and transient functions applied to input variables and specified in a computer code. AD can differentiate complex functions which involve IF statements and loops, and AD can be implemented using either forward or backward mode. Consider an example of calculating a derivative of the following function with respect to `x`.

```r
sigmoid = function(x,b,w){
  v1 = w*x;
  v2 = v1 + b
  v3 = 1/(1+exp(-v2))
}
```

In the forward mode an auxiliary variable, called a dual number, will be added to each line of the code to track the value of the derivative associated with this line. In our example, if we set `x=2`, `w=3`, `b=52`, we get the calculations given in Table below.

| Function calculations | Derivative calculations |
|---|---|
| 1. `v1 = w*x = 6` | 1. `dv1 = w = 3` (derivative of `v1` with respect to `x`) |
| 2. `v2 = v1 + b = 11` | 2. `dv2 = dv1 = 3` (derivative of `v2` with respect to `x`) |
| 3. `v3 = 1/(1+exp(-v2)) = 0.99` | 3. `dv3 = eps2*exp(-v2)/(1+exp(-v2))**2   = 5e-05` |

Variables `dv1,dv2,dv3` correspond to partial (local) derivatives of each intermediate variables `v1,v2,v3` with respect to \(x\), and are called dual variables. Tracking for dual variables can either be implemented using source code modification tools that add new code for calculating the dual numbers or via operator overloading.

The reverse AD also applies chain rule recursively but starts from the outer function, as shown in Table below.

| Function calculations | Derivative calculations |
|---|---|
| 1. `v1 = w*x = 6` | 4. `dv1dx =w; dv1 = dv2*dv1dx = 3*1.3e-05=5e-05` |
| 2. `v2 = v1 + b = 11` | 3. `dv2dv1 =1; dv2 = dv3*dv2dv1 = 1.3e-05` |
| 3. `v3 = 1/(1+exp(-v2)) = 0.99` | 2. `dv3dv2 = exp(-v2)/(1+exp(-v2))**2;` |
| 4. `v4 = v3` | 1. `dv4=1` |

For DL, derivatives are calculated by applying reverse AD algorithm to a model which is defined as a superposition of functions. A model is defined either using a general purpose language as it is done in `PyTorch` or through a sequence of function calls defined by framework libraries (e.g. in `TensorFlow`). Forward AD algorithms calculate the derivative with respect to a single input variable, but reverse AD produces derivatives with respect to all intermediate variables. For models with many parameters, it is much more computationally feasible to perform the reverse AD.

In the context of neural networks, the reverse AD algorithms is called back-propagation and was popularized in AI by Rumelhart et al. (1986). According to Schmidhuber (2015) the first version of what we call today back-propagation was published in 1970 in a master's thesis Linnainmaa (1970) and was closely related to the work of Ostrovskii et al. (1971). However, similar techniques rooted in Pontryagin's maximization principle Boltyanskii et al. (1960) were discussed in the context of multi-stage control problems Bryson (1961),bryson1969applied}. Dreyfus (1962) applies back-propagation to calculate the first order derivative of a return function to numerically solve a variational problem. Later Dreyfus (1973) used back-propagation to derive an efficient algorithm to solve a minimization problem. The first neural network specific version of back-propagation was proposed in Werbos (1974) and an efficient back-propagation algorithm was discussed in Werbos (1982).

13

<!-- page: 14 -->

Modern deep learning frameworks fully automate the process of finding derivatives using AD algorithms. For example, PyTorch relies on autograd library which automatically finds gradient using back-propagation algorithm. Here is a small code example using autograd library in jax.

```python
import jax.numpy as jnp
from jax import grad,jit
import pandas as pd
from jax import random
import matplotlib.pyplot as plt

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = jnp.array(axes.get_xlim())
    ylim = axes.get_xlim()
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-'); plt.ylim(ylim)

d = pd.read_csv('circle.csv').values
x = d[:, 1:3]; y = d[:, 0]
def sigmoid(x):
    return 1 / (1 + jnp.exp(-x))
def predict(x, w1,b1,w2,b2):
    z = sigmoid(jnp.dot(x, w1)+b1)
    return sigmoid(jnp.dot(z, w2)+b2)[:,0]
def nll(x, y, w1,b1,w2,b2):
    yhat = predict(x, w1,b1,w2,b2)
    return -jnp.sum(y * jnp.log(yhat) + (1 - y) * jnp.log(1 - yhat))
@jit
def sgd_step(x, y, w1,b1,w2,b2, lr):
    grads = grad(nll,argnums=[2,3,4,5])(x, y, w1,b1,w2,b2)
    return w1 - lr * grads[0],b1 - lr * grads[1],w2 - lr * grads[2],b2 - lr * grads[3]
def accuracy(x, y, w1,b1,w2,b2):
    y_pred = predict(x, w1,b1,w2,b2)
    return jnp.mean((y_pred > 0.5) == y)
k = random.PRNGKey(0)
w1 = 0.1*random.normal(k,(2,4))
b1 = 0.01*random.normal(k,(4,))
w2 = 0.1*random.normal(k,(4,1))
b2 = 0.01*random.normal(k,(1,))

for i in range(1000):
    w1,b1,w2,b2 = sgd_step(x,y,w1,b1,w2,b2,0.003)
print(accuracy(x,y,w1,b1,w2,b2))
#> 1.0

fig, ax = plt.subplots()
ax.scatter(x[:,0], x[:,1], c=['r' if x==1 else 'g' for x in y],s=7); plt.xlabel("x1"); plt.ylabel("x2");
#> <matplotlib.collections.PathCollection object at 0x1654b2f10>
#> Text(0.5, 0, 'x1')
#> Text(0, 0.5, 'x2')
#> (-10.0, 10.0)
ax.spines['top'].set_visible(False)
# plt.scatter((x[:,1]*w1[1,0] - b1[0])/w1[0,0], x[:,1])
```

14

<!-- page: 15 -->

```python
abline(w1[1,0]/w1[0,0],b1[0]/w1[0,0])
abline(w1[1,1]/w1[0,1],b1[1]/w1[0,1])
abline(w1[1,2]/w1[0,2],b1[2]/w1[0,2])
abline(w1[1,3]/w1[0,3],b1[3]/w1[0,3])
plt.show()
```

[FIGURE: Scatter plot of the simulated data with the four lines given by the first layer weights]

Text in figure:
- x2 (vertical axis label)
- 10.0, 7.5, 5.0, 2.5, 0.0, 2.5, 5.0, 7.5, 10.0 (vertical axis ticks)
- 10.0, 7.5, 5.0, 2.5, 0.0, 2.5, 5.0, 7.5, 10.0 (horizontal axis ticks)
- x1 (horizontal axis label)

## 5 Discussion

The goal of our paper is to provide an overview of of DL for statisticians. To do this, we have discussed the model estimation procedure and demonstrated that DL is an extension of a generalized linear model. One goal of statistics is to build predictive models along with uncertainty and to develop an understanding of the data generating mechanism. Data models are well studied in statistical literature, but often do not provide enough flexibility to learn the input-output relations. Closed box predictive rules, such as trees and neural networks, are more flexible learners. However, in high-dimensional problems, finding good models is challenging, and this is where deep learning methods shine. We can think of deterministic DL model as a transformation of high dimensional input and outputs. Hidden features lie on the transformed space, and are empirically learned as opposed to theoretically specified.

Although DL models have been almost exclusively used for problems of image analysis and natural language processing, more traditional data sets, which arise in finance, science and engineering, such as spatial and temporal data can be efficiently analyzed using deep learning. Thus, DL provides an alternative for applications where traditional statistical techniques apply. There are a number of areas of future research for Statisticians. In particular, uncertainty quantification and model selection, such as architecture design, as well as algorithmic improvements and Bayesian deep learning. We hope this review will make DL models accessible for statisticians.

## References

Behnia F, Karbowski D, Sokolov V (2021) Deep generative models for vehicle speed trajectories. arXiv preprint arXiv:211208361

Bhadra A, Datta J, Polson N, et al (2021) Merging two cultures: Deep and statistical learning. arXiv preprint arXiv:211011561

Boltyanskii VG, Gamkrelidze RV, Pontryagin (1960) Theory of optimal processes i: Maximum principle. News of Akad Nauk SSSR Mathematics Series 24:3–42

15

<!-- page: 16 -->

Bottou L, Curtis FE, Nocedal J (2018) Optimization methods for large-scale machine learning. SIAM review 60:223–311

Bryson AE (1961) A gradient method for optimizing multi-stage allocation processes. In: Proc. Harvard univ. Symposium on digital computers and their applications

Dixon MF, Polson NG, Sokolov VO (2019) Deep learning for spatio-temporal modeling: Dynamic traffic flows and high frequency trading. Applied Stochastic Models in Business and Industry 35:788–807

Dreyfus S (1973) The computational solution of optimal control problems with time lag. IEEE Transactions on Automatic Control 18:383–385

Dreyfus S (1962) The numerical solution of variational problems. Journal of Mathematical Analysis and Applications 5:30–45

Griewank A, Kulshreshtha K, Walther A (2012) On the numerical stability of algorithmic differentiation. Computing 94:125–149

Hardt M, Recht B, Singer Y (2016) Train faster, generalize better: Stability of stochastic gradient descent. In: International conference on machine learning. PMLR, pp 1225–1234

Heaton J, Polson N, Witte JH (2017) Deep learning for finance: Deep portfolios. Applied Stochastic Models in Business and Industry 33:3–12

Keskar NS, Mudigere D, Nocedal J, et al (2016) On large-batch training for deep learning: Generalization gap and sharp minima. arXiv preprint arXiv:160904836

LeCun Y, Bottou L, Orr GB, Müller K-R (2002) Efficient backprop. In: Neural networks: Tricks of the trade. Springer, pp 9–50

Linnainmaa S (1970) The representation of the cumulative rounding error of an algorithm as a taylor expansion of the local rounding errors. Master's Thesis (in Finnish), Univ Helsinki 6–7

Nareklishvili M, Polson N, Sokolov V (2022a) Deep partial least squares for iv regression. arXiv preprint arXiv:220702612

Nareklishvili M, Polson N, Sokolov V (2022b) Feature selection for personalized policy analysis. arXiv preprint arXiv:230100251

Nareklishvili M, Polson N, Sokolov V (2023) Generative causal inference. arXiv preprint arXiv:230616096

Ostrovskii G, Volin YM, Borisov W (1971) Uber die berechnung von ableitungen. Wissenschaftliche Zeitschrift der Technischen Hochschule f ur Chemie, Leuna-Merseburg 13:382–384

Polson NG, Sokolov V (2017) Deep learning: A bayesian perspective

Polson NG, Sokolov V (2023) Generative AI for bayesian computation. arXiv preprint arXiv:230514972

Polson N, Sokolov V (2020) Deep learning: Computational aspects. Wiley Interdisciplinary Reviews: Computational Statistics 12:e1500

Polson N, Sokolov V, Xu J (2021) Deep learning partial least squares. arXiv preprint arXiv:210614085

Robbins H, Monro S (1951) A Stochastic Approximation Method. The Annals of Mathematical Statistics 22:400–407. https://doi.org/10.1214/aoms/1177729586

Rumelhart DE, Hinton GE, Williams RJ (1986) Learning representations by back-propagating errors. nature 323:533

Schmidhuber J (2015) Deep learning in neural networks: An overview. Neural networks 61:85–117

Sokolov V (2017) Discussion of 'deep learning for finance: Deep portfolios'. Applied Stochastic Models in Business and Industry 33:16–18

Wang Y, Polson N, Sokolov VO (2022) Data augmentation for bayesian deep learning. Bayesian Analysis 1:1–29

Werbos P (1974) Beyond regression:" new tools for prediction and analysis in the behavioral sciences. Ph D dissertation, Harvard University

Werbos PJ (1982) Applications of advances in nonlinear sensitivity analysis. In: System modeling and optimization. Springer, pp 762–770

16
