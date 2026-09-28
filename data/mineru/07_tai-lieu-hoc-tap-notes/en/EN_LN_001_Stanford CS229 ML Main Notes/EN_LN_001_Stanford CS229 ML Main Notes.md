<!-- page: 1 -->

CS229 Lecture Notes

Tengyu Ma and Andrew Ng

August 23, 2026

<!-- page: 2 -->

## Contents

- I Supervised learning 6
- 1 Linear regression 9
- 1.1 LMS algorithm 10
- 1.2 The normal equations 14
- 1.2.1 Matrix derivatives 14
- 1.2.2 Least squares revisited 15
- 1.3 Probabilistic interpretation 16
- 1.4 Locally weighted linear regression 18
- 2 Classification and logistic regression 21
- 2.1 Logistic regression 21
- 2.2 Digression: the perceptron learning algorithm 24
- 2.3 Multi-class classification 25
- 2.4 Another algorithm for maximizing $\ell(\theta)$ 28
- 3 Generalized linear models 30
- 3.1 The exponential family 30
- 3.2 Constructing GLMs 32
- 3.2.1 Ordinary least squares 33
- 3.2.2 Logistic regression 34
- 4 Generative learning algorithms 35
- 4.1 Gaussian discriminant analysis 36
- 4.1.1 The multivariate normal distribution 36
- 4.1.2 The Gaussian discriminant analysis model 39
- 4.1.3 Discussion: GDA and logistic regression 41
- 4.2 Naive bayes (Optional Reading) 42
- 4.2.1 Laplace smoothing 45
- 4.2.2 Event models for text classification 47

<!-- page: 3 -->

- 5 Kernel methods 49
- 5.1 Feature maps 49
- 5.2 LMS (least mean squares) with features 50
- 5.3 LMS with the kernel trick 50
- 5.4 Properties of kernels 54
- 6 Support vector machines 60
- 6.1 Margins: intuition 60
- 6.2 Notation 62
- 6.3 Functional and geometric margins 62
- 6.4 The optimal margin classifier 64
- 6.5 Lagrange duality 66
- 6.6 Optimal margin classifiers: the dual form 69
- 6.7 Regularization and the non-separable case 73
- 6.8 The SMO algorithm 74
- 6.8.1 Coordinate ascent 75
- 6.8.2 SMO 76
- II Deep learning 79
- 7 Deep learning 80
- 7.1 Supervised learning with non-linear models 80
- 7.2 Neural networks 84
- 7.3 Modules in Modern Neural Networks 93
- 7.4 Backpropagation 99
- 7.4.1 Preliminaries on partial derivatives 101
- 7.4.2 General strategy of backpropagation 103
- 7.4.3 Backward functions for basic modules 106
- 7.4.4 Back-propagation for MLPs 109
- 7.5 Vectorization over training examples 111
- III Generalization and regularization 114
- 8 Generalization 115
- 8.1 Bias-variance tradeoff 117
- 8.1.1 A mathematical decomposition (for regression) 122
- 8.2 The double descent phenomenon 123
- 8.3 Sample complexity bounds 128

<!-- page: 4 -->

- 8.3.1 Preliminaries 128
- 8.3.2 The case of finite $\mathcal{H}$ 130
- 8.3.3 The case of infinite $\mathcal{H}$ 133
- 9 Regularization and model selection 137
- 9.1 Regularization 137
- 9.2 Implicit regularization effect 139
- 9.3 Model selection via cross validation 141
- 9.4 Bayesian statistics and regularization 144
- IV Unsupervised learning 146
- 10 Clustering and the $k$-means algorithm 147
- 11 EM algorithms 150
- 11.1 EM for mixture of Gaussians 150
- 11.2 Jensen's inequality 153
- 11.3 General EM algorithms 154
- 11.3.1 Other interpretation of ELBO 160
- 11.4 Mixture of Gaussians revisited 160
- 11.5 Variational inference and variational auto-encoder 162
- 12 Principal components analysis 167
- 13 Independent components analysis 173
- 13.1 ICA ambiguities 174
- 13.2 Densities and linear transformations 175
- 13.3 ICA algorithm 176
- V Generative models and Foundation Models 179
- 14 Diffusion models 180
- 14.1 The diffusion process 180
- 14.2 Parameterizing the reverse process 183
- 14.3 Training diffusion models by maximizing the ELBO 184
- 14.4 Continuous-time view of reverse diffusion 188

<!-- page: 5 -->

- 15 Foundation models overview 191
- 15.1 Linear Probe and Finetuning with Representation Learning . 192
- 15.2 Low-rank adaptation (LoRA). 194
- 16 Representation Learning 196
- 16.1 Supervised pretraining . 196
- 16.2 Contrastive learning . 196
- 16.3 Semantic retrieval . 198
- 16.4 Retrieval-augmented generation . 201
- 17 Large language models 202
- 17.1 Tokenization . 202
- 17.2 Autoregressive models and next-token prediction loss . 203
- 17.3 Transformer architecture . 207
- 17.4 Variants of Attention . 214
- 17.5 Mixture-of-Experts Layers . 215
- 17.6 In-context learning . 216
- 17.7 Zero-shot learning / prompting . 217
- 17.8 Supervised Finetuning (SFT) . 218
- 18 Reasoning in LLMs 220
- 18.1 Chain of thoughts . 220
- 18.2 RLVR with long chain-of-thought reasoning . 221
- VI Reinforcement Learning and Control 226
- 19 Reinforcement learning 227
- 19.1 Markov decision processes . 228
- 19.2 Value iteration and policy iteration . 230
- 19.3 Learning a model for an MDP . 232
- 19.4 Continuous state MDPs . 234
- 19.4.1 Discretization . 234
- 19.4.2 Value function approximation . 237
- 19.5 Connections between Policy and Value Iteration (Optional) . 241
- 20 LQR, DDP and LQG 244
- 20.1 Finite-horizon MDPs . 244
- 20.2 Linear Quadratic Regulation (LQR) . 248
- 20.3 From non-linear dynamics to LQR . 251
- 20.3.1 Linearization of dynamics . 252

<!-- page: 6 -->

- 20.3.2 Differential Dynamic Programming (DDP) ..... 252
- 20.4 Linear Quadratic Gaussian (LQG) ..... 254
- 21 Policy Gradient and its Variants ..... 258
- 21.1 REINFORCE ..... 258
- 21.2 PPO ..... 263
- A Gaussian and KL facts ..... 266
- A.1 Basic Gaussian and KL identities ..... 266

<!-- page: 7 -->

Part I

Supervised learning

<!-- page: 8 -->

Let’s start by talking about a few examples of supervised learning problems. Suppose we have a dataset giving the living areas and prices of 47 houses from Portland, Oregon:

| Living area (feet<sup>2</sup>) | Price (1000$s) |
| --- | --- |
| 2104 | 400 |
| 1600 | 330 |
| 2400 | 369 |
| 1416 | 232 |
| 3000 | 540 |
| ... | ... |

We can plot this data:

![](images/page_7_chart_4.jpg)

Given data like this, how can we learn to predict the prices of other houses in Portland, as a function of the size of their living areas?

To establish notation for future use, we’ll use $x ^ { ( i ) }$ to denote the “input” variables (living area in this example), also called input features, and $y ^ { ( i ) }$ to denote the “output” or target variable that we are trying to predict (price). A pair $( x ^ { ( i ) } , y ^ { ( i ) } )$ is called a training example, and the dataset that we’ll be using to learn—a list of n training examples $\{ ( x ^ { ( i ) } , y ^ { ( i ) } ) ; i   =$ $1 , \ldots , n \}$ —is called a training set. Note that the superscript ${ \bf \Phi } ^ { \mathfrak { c } } ( i ) ^ { \mathfrak { p } }$ in the notation is simply an index into the training set, and has nothing to do with exponentiation. We will also use X denote the space of input values, and Y the space of output values. In this example, $\mathcal { X } = \mathcal { Y } = \mathbb { R }$

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function $h : { \mathcal { X } } \mapsto { \mathcal { Y } }$ so that $h ( x )$ is a “good” predictor for the corresponding value of y. For historical reasons, this

<!-- page: 9 -->

function h is called a hypothesis. Seen pictorially, the process is therefore like this:

![](images/page_8_image_2.jpg)

When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression prob lem. When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.

<!-- page: 10 -->

## Chapter 1

## Linear regression

To make our housing example more interesting, let’s consider a slightly richer dataset in which we also know the number of bedrooms in each house:

| Living area (feet<sup>2</sup>) | #bedrooms | Price (1000$s) |
| --- | --- | --- |
| 2104 | 3 | 400 |
| 1600 | 3 | 330 |
| 2400 | 3 | 369 |
| 1416 | 2 | 232 |
| 3000 | 4 | 540 |
| ... | ... | ... |

Here, the x’s are two-dimensional vectors in $\mathbb { R } ^ { 2 }$ . For instance, $x _ { 1 } ^ { ( i ) }$ is the living area of the i-th house in the training set, and $x _ { 2 } ^ { ( i ) }$ is its number of bedrooms. (In general, when designing a learning problem, it will be up to you to decide what features to choose, so if you are out in Portland gathering housing data, you might also decide to include other features such as whether each house has a fireplace, the number of bathrooms, and so on. We’ll say more about feature selection later, but for now let’s take the features as given.)

To perform supervised learning, we must decide how we’re going to represent functions/hypotheses h in a computer. As an initial choice, let’s say we decide to approximate y as a linear function of x:

$$
h _ {\theta} (x) = \theta_ {0} + \theta_ {1} x _ {1} + \theta_ {2} x _ {2}
$$

Here, the $\theta _ { i } { } ^ { \prime } \mathrm { s }$ are the parameters (also called weights) parameterizing the space of linear functions mapping from X to Y. When there is no risk of

<!-- page: 11 -->

confusion, we will drop the $\theta$ subscript in $h _ { \theta } ( x )$ , and write it more simply as $h ( x )$ To simplify our notation, we also introduce the convention of letting $x _ { 0 } = 1$ (this is the intercept term), so that

$$
h (x) = \sum_ {i = 0} ^ {d} \theta_ {i} x _ {i} = \theta^ {T} x,
$$

where on the right-hand side above we are viewing $\theta$ and $x$ both as vectors, and here d is the number of input variables (not counting $x _ { 0 } )$

Now, given a training set, how do we pick, or learn, the parameters $\theta ?$ One reasonable method seems to be to make h(x) $h ( x )$ close to $y ,$ at least for the training examples we have. To formalize this, we will define a function that measures, for each value of the $\theta ^ { \prime } \mathrm { s } ,$ how close the $h ( x ^ { ( i ) } ) \mathrm { { ' s } }$ are to the corresponding $y ^ { ( i ) } \mathrm { ^ { \prime } s }$ . We define the cost function:

$$
J (\theta) = \frac {1}{2} \sum_ {i = 1} ^ {n} (h _ {\theta} (x ^ {(i)}) - y ^ {(i)}) ^ {2}.
$$

If you’ve seen linear regression before, you may recognize this as the familiar least-squares cost function that gives rise to the ordinary least squares regression model. Whether or not you have seen it previously, let’s keep going, and we’ll eventually show this to be a special case of a much broader family of algorithms.

## 1.1 LMS algorithm

We want to choose $\theta$ so as to minimize $J ( \theta )$ . To do $\mathrm { s o } ,$ let’s use a search algorithm that starts with some “initial guess” for $\theta ,$ and that repeatedly changes $\theta$ to make $J ( \theta )$ smaller, until hopefully we converge to a value of $\theta$ that minimizes $J ( \theta )$ . Specifically, let’s consider the gradient descent algorithm, which starts with some initial $\theta ,$ and repeatedly performs the update:

$$
\theta_ {j} := \theta_ {j} - \alpha \frac {\partial}{\partial \theta_ {j}} J (\theta).
$$

(This update is simultaneously performed for all values of $j \; = \; 0 , \ldots , d . )$ Here, α is called the learning rate. This is a very natural algorithm that repeatedly takes a step in the direction of steepest decrease of $J .$

In order to implement this algorithm, we have to work out what is the partial derivative term on the right hand side. Let’s first work it out for the

<!-- page: 12 -->

case of if we have only one training example $( x , y )$ , so that we can neglect the sum in the definition of J. We have:

$$
\begin{array}{r c l} \frac {\partial}{\partial \theta_ {j}} J (\theta) & = & \frac {\partial}{\partial \theta_ {j}} \frac {1}{2} (h _ {\theta} (x) - y) ^ {2} \\ & = & 2 \cdot \frac {1}{2} (h _ {\theta} (x) - y) \cdot \frac {\partial}{\partial \theta_ {j}} (h _ {\theta} (x) - y) \\ & = & (h _ {\theta} (x) - y) \cdot \frac {\partial}{\partial \theta_ {j}} \left(\sum_ {i = 0} ^ {d} \theta_ {i} x _ {i} - y\right) \\ & = & (h _ {\theta} (x) - y) x _ {j} \end{array}
$$

For a single training example, this gives the update rule:<sup>1</sup>

$$
\theta_ {j} := \theta_ {j} + \alpha \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x _ {j} ^ {(i)}.
$$

The rule is called the LMS update rule (LMS stands for “least mean squares”), and is also known as the Widrow-Hoff learning rule. This rule has several properties that seem natural and intuitive. For instance, the magnitude of the update is proportional to the error term $( y ^ { ( i ) } - h _ { \theta } ( x ^ { ( i ) } ) )$ ; thus, for instance, if we are encountering a training example on which our prediction nearly matches the actual value of $y ^ { ( i ) }$ , then we find that there is little need to change the parameters; in contrast, a larger change to the parameters will be made if our prediction $h _ { \theta } ( x ^ { ( i ) } )$ has a large error (i.e., if it is very far from $y ^ { ( i ) } )$

We’d derived the LMS rule for when there was only a single training example. There are two ways to modify this method for a training set of more than one example. The first is replace it with the following algorithm:

Repeat until convergence {

$$
\theta_ {j} := \theta_ {j} + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x _ {j} ^ {(i)}, (\text {for every} j)\tag{1.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“ ”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“ b”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>We use the notation a := b to denote an operation (in a computer program) in which we set the value of a variable a to be equal to the value of b. In other words, this operation overwrites a with the value of b. In contrast, we will write a = when we are asserting a statement of fact, that the value of a is equal to the value of b.</span></small>

<!-- page: 13 -->

By grouping the updates of the coordinates into an update of the vector $\theta ,$ we can rewrite update (1.1) in a slightly more succinct way:

$$
\theta := \theta + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x ^ {(i)}
$$

The reader can easily verify that the quantity in the summation in the update rule above is just $\partial J ( \theta ) / \partial \theta _ { j }$ (for the original definition of J). So, this is simply gradient descent on the original cost function J. This method looks at every example in the entire training set on every step, and is called batch gradient descent. Note that, while gradient descent can be susceptible to local minima in general, the optimization problem we have posed here for linear regression has only one global, and no other local, optima; thus gradient descent always converges (assuming the learning rate α is not too large) to the global minimum. Indeed, J is a convex quadratic function. Here is an example of gradient descent as it is run to minimize a quadratic function.

![](images/page_12_chart_4.jpg)

The ellipses shown above are the contours of a quadratic function. Also shown is the trajectory taken by gradient descent, which was initialized at (48,30). The $x   ^ { \prime } \mathrm { s }$ in the figure (joined by straight lines) mark the successive values of θ that gradient descent went through.

When we run batch gradient descent to fit θ on our previous dataset, to learn to predict housing price as a function of living area, we obtain $\theta _ { 0 }   =   7 1 . 2 7 , \; \theta _ { 1 }   =   0 . 1 3 4 5$ . If we plot $h _ { \theta } ( x )$ as a function of x (area), along with the training data, we obtain the following figure:

<!-- page: 14 -->

![](images/page_13_chart_1.jpg)

If the number of bedrooms were included as one of the input features as well, we get $\theta _ { 0 } = 8 9 . 6 0 , \theta _ { 1 } = 0 . 1 3 9 2 ,   \theta _ { 2 } = - 8 . 7 3 8$

The above results were obtained with batch gradient descent. There is an alternative to batch gradient descent that also works very well. Consider the following algorithm:

$$
\begin{array}{c} \text {Loop} \{\quad \\ \text {for i = 1 to n,} \{\quad \\ \theta_ {j} := \theta_ {j} + \alpha \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x _ {j} ^ {(i)}, \quad (\text {for every j}) \\ \} \\ \} \end{array}\tag{1.2}
$$

By grouping the updates of the coordinates into an update of the vector θ, we can rewrite update (1.2) in a slightly more succinct way:

$$
\theta := \theta + \alpha \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x ^ {(i)}
$$

In this algorithm, we repeatedly run through the training set, and each time we encounter a training example, we update the parameters according to the gradient of the error with respect to that single training example only. This algorithm is called stochastic gradient descent (also incremental gradient descent). Whereas batch gradient descent has to scan through the entire training set before taking a single step—a costly operation if n is large—stochastic gradient descent can start making progress right away, and

<!-- page: 15 -->

continues to make progress with each example it looks at. Often, stochastic gradient descent gets $\theta$ “close” to the minimum much faster than batch gradient descent. (Note however that it may never “converge” to the minimum, and the parameters θ will keep oscillating around the minimum of $J ( \theta )$ ; but in practice most of the values near the minimum will be reasonably good approximations to the true minimum.<sup>2</sup>) For these reasons, particularly when the training set is large, stochastic gradient descent is often preferred over batch gradient descent.

## 1.2 The normal equations

Gradient descent gives one way of minimizing J. Let’s discuss a second way of doing so, this time performing the minimization explicitly and without resorting to an iterative algorithm. In this method, we will minimize J by explicitly taking its derivatives with respect to the $\theta _ { j } { \mathrm { ` s } } ,$ and setting them to zero. To enable us to do this without having to write reams of algebra and pages full of matrices of derivatives, let’s introduce some notation for doing calculus with matrices.

## 1.2.1 Matrix derivatives

For a function $f \; : \; \mathbb { R } ^ { n \times d } \; \mapsto$ R mapping from n-by-d matrices to the real numbers, we define the derivative of f with respect to A to be:

$$
\nabla_ {A} f (A) = \left[ \begin{array}{c c c} \frac {\partial f}{\partial A _ {1 1}} & \dots & \frac {\partial f}{\partial A _ {1 d}} \\ \vdots & \ddots & \vdots \\ \frac {\partial f}{\partial A _ {n 1}} & \dots & \frac {\partial f}{\partial A _ {n d}} \end{array} \right]
$$

Thus, the gradient $\nabla _ { A } f ( A )$ is itself an n-by-d matrix, whose $( i , j )$ -element is $\partial f / \partial A _ { i j }$ . For example, suppose $\mathbf { \mathit { A } } = \left[ \begin{array} { l l } { \mathbf { \mathit { A } } _ { 1 1 } } & { \mathbf { \mathit { A } } _ { 1 2 } } \\ { \mathbf { \mathit { A } } _ { 2 1 } } & { \mathbf { \mathit { A } } _ { 2 2 } } \end{array} \right]$ is a 2-by-2 matrix, and the function $f : \mathbb { R } ^ { 2 \times 2 } \mapsto \mathbb { R }$ is given by

$$
f (A) = \frac {3}{2} A _ {1 1} + 5 A _ {1 2} ^ {2} + A _ {2 1} A _ {2 2}.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>By slowly letting the learning rate α decrease to zero as the algorithm runs, it is also possible to ensure that the parameters will converge to the global minimum rather than merely oscillate around the minimum.</span></small>

<!-- page: 16 -->

Here, $A _ { i j }$ denotes the $( i , j )$ entry of the matrix A. We then have

$$
\nabla_ {A} f (A) = \left[ \begin{array}{c c} \frac {3}{2} & 1 0 A _ {1 2} \\ A _ {2 2} & A _ {2 1} \end{array} \right].
$$

## 1.2.2 Least squares revisited

Armed with the tools of matrix derivatives, let us now proceed to find in closed-form the value of $\theta$ that minimizes $J ( \theta )$ . We begin by re-writing J in matrix-vectorial notation.

Given a training set, define the design matrix X to be the n-by-d matrix (actually $n \text {-by-} d+1$ , if we include the intercept term) that contains the training examples’ input values in its rows:

$$
X = \left[ \begin{array}{c} - (x ^ {(1)}) ^ {T} - \\ - (x ^ {(2)}) ^ {T} - \\ \vdots \\ - (x ^ {(n)}) ^ {T} - \end{array} \right].
$$

Also, let $\vec { y }$ be the n-dimensional vector containing all the target values from the training set:

$$
\vec {y} = \left[ \begin{array}{c} y ^ {(1)} \\ y ^ {(2)} \\ \vdots \\ y ^ {(n)} \end{array} \right].
$$

Now, since $h _ { \theta } ( x ^ { ( i ) } ) = ( x ^ { ( i ) } ) ^ { T } \theta$ , we can easily verify that

$$
\begin{array}{r c l} X \theta - \vec {y} & = & \left[ \begin{array}{c} (x ^ {(1)}) ^ {T} \theta \\ \vdots \\ (x ^ {(n)}) ^ {T} \theta \end{array} \right] - \left[ \begin{array}{c} y ^ {(1)} \\ \vdots \\ y ^ {(n)} \end{array} \right] \\ & = & \left[ \begin{array}{c} h _ {\theta} (x ^ {(1)}) - y ^ {(1)} \\ \vdots \\ h _ {\theta} (x ^ {(n)}) - y ^ {(n)} \end{array} \right]. \end{array}
$$

Thus, using the fact that for a vector z, we have that $\begin{array} { r } { z ^ { T } z = \sum _ { i } z _ { i } ^ { 2 } } \end{array}$

$$
\begin{array}{r c l} \frac {1}{2} (X \theta - \vec {y}) ^ {T} (X \theta - \vec {y}) & = & \frac {1}{2} \sum_ {i = 1} ^ {n} (h _ {\theta} (x ^ {(i)}) - y ^ {(i)}) ^ {2} \\ & = & J (\theta) \end{array}
$$

<!-- page: 17 -->

Finally, to minimize J, let’s find its derivatives with respect to θ. Hence,

$$
\begin{array}{r c l} \nabla_ {\theta} J (\theta) & = & \nabla_ {\theta} \frac {1}{2} (X \theta - \vec {y}) ^ {T} (X \theta - \vec {y}) \\ & = & \frac {1}{2} \nabla_ {\theta} \left((X \theta) ^ {T} X \theta - (X \theta) ^ {T} \vec {y} - \vec {y} ^ {T} (X \theta) + \vec {y} ^ {T} \vec {y}\right) \\ & = & \frac {1}{2} \nabla_ {\theta} \left(\theta^ {T} (X ^ {T} X) \theta - \vec {y} ^ {T} (X \theta) - \vec {y} ^ {T} (X \theta)\right) \\ & = & \frac {1}{2} \nabla_ {\theta} \left(\theta^ {T} (X ^ {T} X) \theta - 2 (X ^ {T} \vec {y}) ^ {T} \theta\right) \\ & = & \frac {1}{2} \left(2 X ^ {T} X \theta - 2 X ^ {T} \vec {y}\right) \\ & = & X ^ {T} X \theta - X ^ {T} \vec {y} \end{array}
$$

In the third step, we used the fact that $a ^ { T } b   =   b ^ { T } a$ , and in the fifth step used the facts $\nabla _ { x } b ^ { T } x = b$ and $\nabla _ { x } x ^ { T } A x = 2 A x$ for symmetric matrix A (for more details, see Section 4.3 of “Linear Algebra Review and Reference”). To minimize J, we set its derivatives to zero, and obtain the normal equations:

$$
X ^ {T} X \theta = X ^ {T} \vec {y}
$$

Thus, the value of $\theta$ that minimizes $J ( \theta )$ is given in closed form by the equation

$$
\theta = (X ^ {T} X) ^ {- 1} X ^ {T} \vec {y}. ^ {3}
$$

## 1.3 Probabilistic interpretation

When faced with a regression problem, why might linear regression, and specifically why might the least-squares cost function $J ,$ be a reasonable choice? In this section, we will give a set of probabilistic assumptions, under which least-squares regression is derived as a very natural algorithm.

Let us assume that the target variables and the inputs are related via the equation

$$
y ^ {(i)} = \theta^ {T} x ^ {(i)} + \epsilon^ {(i)},
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">XT X</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Note that in the above step, we are implicitly assuming that X X is an invertible matrix. This can be checked before calculating the inverse. If either the number of linearly independent examples is fewer than the number of features, or if the features are not linearly independent, then will not be invertible. Even in such cases, it is possible to “fix” the situation with additional techniques, which we skip here for the sake of simplicty.</span></small>

<!-- page: 18 -->

where $\epsilon ^ { ( i ) }$ is an error term that captures either unmodeled effects (such as if there are some features very pertinent to predicting housing price, but that we’d left out of the regression), or random noise. Let us further assume that the $\epsilon ^ { ( i ) }$ are distributed IID (independently and identically distributed) according to a Gaussian distribution (also called a Normal distribution) with mean zero and some variance $\sigma ^ { 2 }$ . We can write this assumption as $`` \epsilon^{(i)}\sim$ $\mathcal { N } ( 0 , \sigma ^ { 2 } ) .$ I.e., the density of $\epsilon ^ { ( i ) }$ is given by

$$
p (\epsilon^ {(i)}) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(\epsilon^ {(i)}) ^ {2}}{2 \sigma^ {2}}\right).
$$

This implies that

$$
p (y ^ {(i)} | x ^ {(i)}; \theta) = \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2}}{2 \sigma^ {2}}\right).
$$

The notation $`` p(y^{(i)}|x^{(i)};\theta)$ indicates that this is the distribution of $y ^ { ( i ) }$ given $x ^ { ( i ) }$ and parameterized by θ. Note that we should not condition on θ $( `` p(y^{(i)}|x^{(i)},\theta) '' )$ , since $\theta$ is not a random variable. We can also write the distribution of $y ^ { ( i ) }$ as $y ^ { ( i ) } \mid x ^ { ( i ) } ; \theta \sim \mathcal { N } ( \theta ^ { T } x ^ { ( i ) } , \sigma ^ { 2 } )$

Given X (the design matrix, which contains all the $x ^ { ( i ) } { } ^ { \mathrm { { , } } } \mathrm { { S ) } }$ and $\theta ,$ what is the distribution of the $y ^ { ( i ) } \mathrm { ^ { \prime } S ^ { \prime } }$ The probability of the data is given by $p ( { \vec { y } } | X ; \theta )$ . This quantity is typically viewed a function of $\vec { y }$ (and perhaps $X )$ for a fixed value of $\theta .$ When we wish to explicitly view this as a function of $\theta ,$ we will instead call it the likelihood function:

$$
L (\theta) = L (\theta ; X, \vec {y}) = p (\vec {y} | X; \theta).
$$

Note that by the independence assumption on the $\epsilon ^ { ( i ) } \mathrm { ^ { \mathrm { { \scriptsize ~ \mathrm { ~ \scriptsize ~ } } } } S }$ (and hence also the $y ^ { ( i ) } \mathrm { ^ { \prime } s }$ given the $x ^ { ( i ) } { } ^ { \mathrm { { \textquotedblright } } } \mathrm { { S ) } }$ , this can also be written

$$
\begin{array}{l l} L (\theta) & = \prod_ {i = 1} ^ {n} p (y ^ {(i)} \mid x ^ {(i)}; \theta) \\ & = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2}}{2 \sigma^ {2}}\right). \end{array}
$$

Now, given this probabilistic model relating the $y ^ { ( i ) } !$ ’s and the $x ^ { ( i ) } { } ^ { \flat } \mathrm { s } .$ what is a reasonable way of choosing our best guess of the parameters $\theta ?$ The principal of maximum likelihood says that we should choose $\theta$ so as to make the data as high probability as possible. I.e., we should choose $\theta$ to maximize $L ( \theta )$

<!-- page: 19 -->

Instead of maximizing $L ( \theta )$ , we can also maximize any strictly increasing function of $L ( \theta )$ . In particular, the derivations will be a bit simpler if we instead maximize the log likelihood $\ell ( \theta )$

$$
\begin{array}{r c l} \ell (\theta) & = & \log L (\theta) \\ & = & \log \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2}}{2 \sigma^ {2}}\right) \\ & = & \sum_ {i = 1} ^ {n} \log \frac {1}{\sqrt {2 \pi} \sigma} \exp \left(- \frac {(y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2}}{2 \sigma^ {2}}\right) \\ & = & n \log \frac {1}{\sqrt {2 \pi} \sigma} - \frac {1}{\sigma^ {2}} \cdot \frac {1}{2} \sum_ {i = 1} ^ {n} (y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2}. \end{array}
$$

Hence, maximizing $\ell ( \theta )$ gives the same answer as minimizing

$$
\frac {1}{2} \sum_ {i = 1} ^ {n} (y ^ {(i)} - \theta^ {T} x ^ {(i)}) ^ {2},
$$

which we recognize to be $J ( \theta )$ , our original least-squares cost function.

To summarize: Under the previous probabilistic assumptions on the data, least-squares regression corresponds to finding the maximum likelihood estimate of $\theta .$ This is thus one set of assumptions under which least-squares regression can be justified as a very natural method that’s just doing maximum likelihood estimation. (Note however that the probabilistic assumptions are by no means necessary for least-squares to be a perfectly good and rational procedure, and there may—and indeed there are—other natural assumptions that can also be used to justify it.)

Note also that, in our previous discussion, our final choice of $\theta$ did not depend on what was $\sigma ^ { 2 }$ , and indeed we’d have arrived at the same result even if $\sigma ^ { 2 }$ were unknown. We will use this fact again later, when we talk about the exponential family and generalized linear models.

## 1.4 Locally weighted linear regression

Consider the problem of predicting $y$ from $x \in \mathbb { R }$ . The leftmost figure below shows the result of fitting a $y = \theta _ { 0 } + \theta _ { 1 } x$ to a dataset. We see that the data doesn’t really lie on straight line, and so the fit is not very good.

Instead, if we had added an extra feature $x ^ { 2 }$ , and fit $y = \theta _ { 0 } + \theta _ { 1 } x + \theta _ { 2 } x ^ { 2 }$ then we obtain a slightly better fit to the data. (See middle figure) Naively, it

<!-- page: 20 -->

![](images/page_19_chart_1.jpg)

![](images/page_19_chart_2.jpg)

![](images/page_19_chart_3.jpg)

might seem that the more features we add, the better. However, there is also a danger in adding too many features: The rightmost figure is the result of fitting a 5-th order polynomial $\begin{array} { r } { y = \sum _ { j = 0 } ^ { 5 } \theta _ { j } x ^ { j } } \end{array}$ . We see that even though the fitted curve passes through the data perfectly, we would not expect this to be a very good predictor of, say, housing prices $( y )$ for different living areas (x). Without formally defining what these terms mean, we’ll say the figure on the left shows an instance of underfitting—in which the data clearly shows structure not captured by the model—and the figure on the right is an example of overfitting. (Later in this class, when we talk about learning theory we’ll formalize some of these notions, and also define more carefully just what it means for a hypothesis to be good or bad.)

As discussed previously, and as shown in the example above, the choice of features is important to ensuring good performance of a learning algorithm. (When we talk about model selection, we’ll also see algorithms for automatically choosing a good set of features.) In this section, let us briefly talk about the locally weighted linear regression (LWR) algorithm which, assuming there is sufficient training data, makes the choice of features less critical. This treatment will be brief, since you’ll get a chance to explore some of the properties of the LWR algorithm yourself in the homework.

In the original linear regression algorithm, to make a prediction at a query point x (i.e., to evaluate $h ( x ) )$ , we would:

1. Fit θ to minimize $\textstyle \sum _ { i } ( y ^ { ( i ) } - \theta ^ { T } x ^ { ( i ) } ) ^ { 2 }$

2. Output $\theta ^ { T } x$

In contrast, the locally weighted linear regression algorithm does the following:

1. Fit θ to minimize $\textstyle \sum _ { i } w ^ { ( i ) } ( y ^ { ( i ) } - \theta ^ { T } x ^ { ( i ) } ) ^ { 2 }$

2. Output $\theta ^ { T } x$

<!-- page: 21 -->

Here, the $w ^ { ( i ) } \mathrm { ^ { \circ } s }$ are non-negative valued weights. Intuitively, if $w ^ { ( i ) }$ is large for a particular value of $i ,$ then in picking $\theta ,$ we’ll try hard to make $( y ^ { ( i ) } -$ $\theta ^ { T } x ^ { ( i ) \bar { ) } 2 }$ small. If $w ^ { ( i ) }$ is small, then the $\tilde { ( y ^ { ( i ) } - \theta ^ { T } x ^ { ( i ) } ) ^ { 2 } }$ error term will be pretty much ignored in the fit.

A fairly standard choice for the weights $\mathrm { i s } ^ { 4 }$

$$
w ^ {(i)} = \exp \left(- \frac {(x ^ {(i)} - x) ^ {2}}{2 \tau^ {2}}\right)
$$

Note that the weights depend on the particular point x at which we’re trying to evaluate x. Moreover, if $| x ^ { ( i ) } - x |$ is small, then $w ^ { ( i ) }$ is close to 1; and if $| x ^ { ( i ) } - x |$ is large, then $w ^ { ( i ) }$ is small. Hence, $\theta$ is chosen giving a much higher “weight” to the (errors on) training examples close to the query point x. (Note also that while the formula for the weights takes a form that is cosmetically similar to the density of a Gaussian distribution, the $w ^ { ( i ) } \mathrm { ^ { \prime } s }$ do not directly have anything to do with Gaussians, and in particular the $w ^ { ( i ) }$ are not random variables, normally distributed or otherwise.) The parameter $\tau$ controls how quickly the weight of a training example falls off with distance of its $x ^ { ( i ) }$ from the query point $x ; \; \tau$ is called the bandwidth parameter, and is also something that you’ll get to experiment with in your homework.

Locally weighted linear regression is the first example we’re seeing of a non-parametric algorithm. The (unweighted) linear regression algorithm that we saw earlier is known as a parametric learning algorithm, because it has a fixed, finite number of parameters (the $\theta _ { i } \mathrm { { } ^ { \prime } s ) }$ , which are fit to the data. Once we’ve fit the $\theta _ { i } \mathrm { ~ ' s ~ }$ and stored them away, we no longer need to keep the training data around to make future predictions. In contrast, to make predictions using locally weighted linear regression, we need to keep the entire training set around. The term “non-parametric” (roughly) refers to the fact that the amount of stuff we need to keep in order to represent the hypothesis h grows linearly with the size of the training set.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">or w = exp(−(x − x) Σ (x − x)/(2τ )), for an appropriate choice of τ or Σ. ( i ) ( i ) T − 1( i ) 2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">w = exp(−(x −x) (x −x)/(2τ ))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>If x is vector-valued, this is generalized to be (i) (i) T(i) 2,</span></small>

<!-- page: 22 -->

## Chapter 2

## Classification and logistic regression

Let’s now talk about the classification problem. This is just like the regression problem, except that the values y we now want to predict take on only a small number of discrete values. For now, we will focus on the binary classification problem in which y can take on only two values, 0 and 1. (Most of what we say here will also generalize to the multiple-class case.) For instance, if we are trying to build a spam classifier for email, then $x ^ { ( i ) }$ may be some features of a piece of email, and y may be 1 if it is a piece of spam mail, and 0 otherwise. 0 is also called the negative class, and 1 the positive class, and they are sometimes also denoted by the symbols $6 \underline { { \hphantom { 6 } } } 9 9$ and $^ { 2 , }$ Given $x ^ { ( i ) }$ , the corresponding $y ^ { ( i ) }$ is also called the label for the training example.

## 2.1 Logistic regression

We could approach the classification problem ignoring the fact that y is discrete-valued, and use our old linear regression algorithm to try to predict y given x. However, it is easy to construct examples where this method performs very poorly. Intuitively, it also doesn’t make sense for $h _ { \theta } ( x )$ to take values larger than 1 or smaller than 0 when we know that $y \in \{ 0 , 1 \}$

To fix this, let’s change the form for our hypotheses $h _ { \theta } ( x )$ . We will choose

$$
h _ {\theta} (x) = g (\theta^ {T} x) = \frac {1}{1 + e ^ {- \theta^ {T} x}},
$$

where

$$
g (z) = \frac {1}{1 + e ^ {- z}}
$$

<!-- page: 23 -->

is called the logistic function or the sigmoid function. Here is a plot showing $g ( z )$

![](images/page_22_chart_2.jpg)

Notice that $g ( z )$ tends towards 1 as $z \rightarrow \infty$ , and $g ( z )$ tends towards 0 as $z \to - \infty$ . Moreover, $\mathrm { g } ( \mathrm { z } )$ , and hence also $h ( x )$ , is always bounded between 0 and 1. As before, we are keeping the convention of letting $x _ { 0 } = 1$ , so that $\begin{array} { r } { \theta ^ { T } x = \theta _ { 0 } + \sum _ { j = 1 } ^ { d } \theta _ { j } x _ { j } } \end{array}$

For now, let’s take the choice of g as given. Other functions that smoothly increase from 0 to 1 can also be used, but for a couple of reasons that we’ll see later (when we talk about GLMs, and when we talk about generative learning algorithms), the choice of the logistic function is a fairly natural one. Before moving on, here’s a useful property of the derivative of the sigmoid function, which we write as $g ^ { \prime } ;$

$$
\begin{array}{r c l} g ^ {\prime} (z) & = & \frac {d}{d z} \frac {1}{1 + e ^ {- z}} \\ & = & \frac {1}{(1 + e ^ {- z}) ^ {2}} \left(e ^ {- z}\right) \\ & = & \frac {1}{(1 + e ^ {- z})} \cdot \left(1 - \frac {1}{(1 + e ^ {- z})}\right) \\ & = & g (z) (1 - g (z)). \end{array}
$$

So, given the logistic regression model, how do we fit θ for it? Following how we saw least squares regression could be derived as the maximum likelihood estimator under a set of assumptions, let’s endow our classification model with a set of probabilistic assumptions, and then fit the parameters via maximum likelihood.

<!-- page: 24 -->

Let us assume that

$$
\begin{array}{r c l} P (y = 1 \mid x; \theta) & = & h _ {\theta} (x) \\ P (y = 0 \mid x; \theta) & = & 1 - h _ {\theta} (x) \end{array}
$$

Note that this can be written more compactly as

$$
p (y \mid x; \theta) = (h _ {\theta} (x)) ^ {y} \left(1 - h _ {\theta} (x)\right) ^ {1 - y}
$$

Assuming that the n training examples were generated independently, we can then write down the likelihood of the parameters as

$$
\begin{array}{r c l} L (\theta) & = & p (\vec {y} \mid X; \theta) \\ & = & \prod_ {i = 1} ^ {n} p (y ^ {(i)} \mid x ^ {(i)}; \theta) \\ & = & \prod_ {i = 1} ^ {n} \left(h _ {\theta} (x ^ {(i)})\right) ^ {y ^ {(i)}} \left(1 - h _ {\theta} (x ^ {(i)})\right) ^ {1 - y ^ {(i)}} \end{array}
$$

As before, it will be easier to maximize the log likelihood:

$$
\ell (\theta) = \log L (\theta) = \sum_ {i = 1} ^ {n} y ^ {(i)} \log h (x ^ {(i)}) + (1 - y ^ {(i)}) \log (1 - h (x ^ {(i)}))\tag{2.1}
$$

How do we maximize the likelihood? Similar to our derivation in the case of linear regression, we can use gradient ascent. Written in vectorial notation, our updates will therefore be given by $\theta : = \theta + \alpha \nabla _ { \theta } \ell ( \theta )$ . (Note the positive rather than negative sign in the update formula, since we’re maximizing, rather than minimizing, a function now.) Let’s start by working with just one training example $( x , y )$ , and take derivatives to derive the stochastic gradient ascent rule:

$$
\begin{array}{l} \frac {\partial}{\partial \theta_ {j}} \ell (\theta) = \left(y \frac {1}{g (\theta^ {T} x)} - (1 - y) \frac {1}{1 - g (\theta^ {T} x)}\right) \frac {\partial}{\partial \theta_ {j}} g (\theta^ {T} x) \\ \quad = \left(y \frac {1}{g (\theta^ {T} x)} - (1 - y) \frac {1}{1 - g (\theta^ {T} x)}\right) g (\theta^ {T} x) (1 - g (\theta^ {T} x)) \frac {\partial}{\partial \theta_ {j}} \theta^ {T} x \\ \quad = \left(y (1 - g (\theta^ {T} x)) - (1 - y) g (\theta^ {T} x)\right) x _ {j} \\ \quad = (y - h _ {\theta} (x)) x _ {j} \end{array} \tag {2}\tag{2.2}
$$

<!-- page: 25 -->

Above, we used the fact that $g ^ { \prime } ( z ) = g ( z ) ( 1 - g ( z ) )$ . This therefore gives us the stochastic gradient ascent rule

$$
\theta_ {j} := \theta_ {j} + \alpha \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x _ {j} ^ {(i)}
$$

If we compare this to the LMS update rule, we see that it looks identical; but this is not the same algorithm, because $h _ { \theta } ( x ^ { ( i ) } )$ is now defined as a non-linear function of $\theta ^ { T } x ^ { ( i ) }$ . Nonetheless, it’s a little surprising that we end up with the same update rule for a rather different algorithm and learning problem. Is this coincidence, or is there a deeper reason behind this? We’ll answer this when we get to GLM models.

Remark 2.1.1. : An alternative notational viewpoint of the same loss function is also useful, especially for Section 7.1 where we study nonlinear models. Let $\ell _ { \mathrm { l o g i s t i c } } : \mathbb { R } \times \{ 0 , 1 \} \to \mathbb { R } _ { \geq 0 }$ be the logistic loss defined as

$$
\ell_ {\text {logistic}} (t, y) \triangleq y \log (1 + \exp (- t)) + (1 - y) \log (1 + \exp (t)).\tag{2.3}
$$

One can verify by plugging in $h _ { \theta } ( x ) = 1 / ( 1 + e ^ { - \theta ^ { \top } x } )$ that the negative loglikelihood (the negation of \`(θ) in equation (2.1)) can be re-written as

$$
- \ell (\theta) = \ell_ {\mathrm{logistic}} (\theta^ {\top} x, y).\tag{2.4}
$$

Oftentimes $\theta ^ { \top } x$ or t is called the logit. Basic calculus gives us that

$$
\frac {\partial \ell_ {\text {logistic}} (t , y)}{\partial t} = y \frac {- \exp (- t)}{1 + \exp (- t)} + (1 - y) \frac {1}{1 + \exp (- t)}\tag{2.5}
$$

$$
= 1 / (1 + \exp (- t)) - y.\tag{2.6}
$$

Then, using the chain rule, we have that

$$
\frac {\partial}{\partial \theta_ {j}} \ell (\theta) = - \frac {\partial \ell_ {\text {logistic}} (t , y)}{\partial t} \cdot \frac {\partial t}{\partial \theta_ {j}}\tag{2.7}
$$

$$
= (y - 1 / (1 + \exp (- t))) \cdot x _ {j} = (y - h _ {\theta} (x)) x _ {j},\tag{2.8}
$$

which is consistent with the derivation in equation (2.2). We will see this viewpoint can be extended nonlinear models in Section 7.1.

## 2.2 Digression: the perceptron learning algorithm

We now digress to talk briefly about an algorithm that’s of some historical interest, and that we will also return to later when we talk about learning

<!-- page: 26 -->

theory. Consider modifying the logistic regression method to “force” it to output values that are either 0 or 1 or exactly. To do $\mathrm { S O } _ { 2 }$ it seems natural to change the definition of $g$ to be the threshold function:

$$
g (z) = \left\{ \begin{array}{l l} 1 & \text {if} z \geq 0 \\ 0 & \text {if} z <   0 \end{array} \right.
$$

If we then let $h _ { \theta } ( x ) = g ( \theta ^ { T } x )$ as before but using this modified definition of $g ,$ and if we use the update rule

$$
\theta_ {j} := \theta_ {j} + \alpha \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x _ {j} ^ {(i)}.
$$

then we have the perceptron learning algorithn.

In the 1960s, this “perceptron” was argued to be a rough model for how individual neurons in the brain work. Given how simple the algorithm is, it will also provide a starting point for our analysis when we talk about learning theory later in this class. Note however that even though the perceptron may be cosmetically similar to the other algorithms we talked about, it is actually a very different type of algorithm than logistic regression and least squares linear regression; in particular, it is difficult to endow the perceptron’s predictions with meaningful probabilistic interpretations, or derive the perceptron as a maximum likelihood estimation algorithm.

## 2.3 Multi-class classification

Consider a classification problem in which the response variable y can take on any one of k values, so $y \in \{ 1 , 2 , \ldots , k \}$ . For example, rather than classifying emails into the two classes spam or not-spam—which would have been a binary classification problem—we might want to classify them into three classes, such as spam, personal mails, and work-related mails. The label / response variable is still discrete, but can now take on more than two values. We will thus model it as distributed according to a multinomial distribution.

In this case, $p ( y \mid x ; \theta )$ is a distribution over k possible discrete outcomes and is thus a multinomial distribution. Recall that a multinomial distribution involves k numbers $\phi _ { 1 } , \ldots , \phi _ { k }$ specifying the probability of each of the outcomes. Note that these numbers must satisfy $\textstyle \sum _ { i = 1 } ^ { k } \phi _ { i } = 1$ . We will de sign a parameterized model that outputs $\phi _ { 1 } , \ldots , \phi _ { k }$ satisfying this constraint given the input x.

We introduce k groups of parameters $\theta _ { 1 } , \ldots , \theta _ { k } ,$ each of them being a vector in $\mathbb { R } ^ { d }$ . Intuitively, we would like to use $\theta _ { 1 } ^ { \top } x , \ldots , \theta _ { k } ^ { \top } x$ to represent

<!-- page: 27 -->

$\phi _ { 1 } , \ldots , \phi _ { k }$ , the probabilities $P ( y   =   1 | x ; \theta ) , \ldots , P ( y   =   k | x ; \theta )$ . However, there are two issues with such a direct approach. First, $\theta _ { j } ^ { \top }$ x is not necessarily within [0, 1]. Second, the summation of $\theta _ { j } ^ { \top } x ^ { \dagger } \mathrm { s }$ is not necessarily 1. Thus, instead, we will use the softmax function to turn $( \theta _ { 1 } ^ { \top } x , \cdots , \theta _ { k } ^ { \top } x )$ into a probability vector with nonnegative entries that sum up to 1.

Define the softmax function softmax : $\mathbb { R } ^ { k } \to \mathbb { R } ^ { k }$ as

$$
\text {softmax} (t _ {1}, \ldots , t _ {k}) = \left[ \begin{array}{c} \frac {\exp (t _ {1})}{\sum_ {j = 1} ^ {k} \exp (t _ {j})} \\ \vdots \\ \frac {\exp (t _ {k})}{\sum_ {j = 1} ^ {k} \exp (t _ {j})} \end{array} \right].\tag{2.9}
$$

The inputs to the softmax function, the vector t here, are often called logits. Note that by definition, the output of the softmax function is always a probability vector whose entries are nonnegative and sum up to 1.

Let $( t _ { 1 } , \ldots , t _ { k } ) \; = \; ( \theta _ { 1 } ^ { \top } x , \cdots , \theta _ { k } ^ { \top } x )$ . We apply the softmax function to $( t _ { 1 } , \ldots , t _ { k } )$ , and use the output as the probabilities $P ( y = 1 \mid x ; \theta ) , \ldots , P ( y =$ $k \mid x ; \theta )$ . We obtain the following probabilistic model:

$$
\left[ \begin{array}{c} P (y = 1 \mid x; \theta) \\ \vdots \\ P (y = k \mid x; \theta) \end{array} \right] = \text {softmax} (t _ {1}, \dots , t _ {k}) = \left[ \begin{array}{c} \frac {\exp (\theta_ {1} ^ {\top} x)}{\sum_ {j = 1} ^ {k} \exp (\theta_ {j} ^ {\top} x)} \\ \vdots \\ \frac {\exp (\theta_ {k} ^ {\top} x)}{\sum_ {j = 1} ^ {k} \exp (\theta_ {j} ^ {\top} x)} \end{array} \right].\tag{2.10}
$$

For notational convenience, we will let $\begin{array} { r } { \phi _ { i } = \frac { \exp ( t _ { i } ) } { \sum _ { j = 1 } ^ { k } \exp ( t _ { j } ) } } \end{array}$ . More succinctly, the equation above can be written as:

$$
P (y = i \mid x; \theta) = \phi_ {i} = \frac {\exp (t _ {i})}{\sum_ {j = 1} ^ {k} \exp (t _ {j})} = \frac {\exp (\theta_ {i} ^ {\top} x)}{\sum_ {j = 1} ^ {k} \exp (\theta_ {j} ^ {\top} x)}.\tag{2.11}
$$

Next, we compute the negative log-likelihood of a single example $( x , y )$

$$
- \log p (y \mid x, \theta) = - \log \left(\frac {\exp (t _ {y})}{\sum_ {j = 1} ^ {k} \exp (t _ {j})}\right) = - \log \left(\frac {\exp (\theta_ {y} ^ {\top} x)}{\sum_ {j = 1} ^ {k} \exp (\theta_ {j} ^ {\top} x)}\right)\tag{2.12}
$$

Thus, the loss function, the negative log-likelihood of the training data, is given as

$$
\ell (\theta) = \sum_ {i = 1} ^ {n} - \log \left(\frac {\exp (\theta_ {y ^ {(i)}} ^ {\top} x ^ {(i)})}{\sum_ {j = 1} ^ {k} \exp (\theta_ {j} ^ {\top} x ^ {(i)})}\right).\tag{2.13}
$$

<!-- page: 28 -->

It’s convenient to define the cross-entropy loss $\ell _ { \mathrm { c e } } : \mathbb { R } ^ { k } \times \{ 1 , \ldots , k \} \to \mathbb { R } _ { \geq 0 }$ which modularizes in the complex equation above:<sup>1</sup>

$$
\ell_ {\mathrm{ce}} ((t _ {1}, \dots , t _ {k}), y) = - \log \left(\frac {\exp (t _ {y})}{\sum_ {j = 1} ^ {k} \exp (t _ {j})}\right).\tag{2.14}
$$

With this notation, we can simply rewrite equation (2.13) as

$$
\ell (\theta) = \sum_ {i = 1} ^ {n} \ell_ {\mathrm{ce}} ((\theta_ {1} ^ {\top} x ^ {(i)}, \dots , \theta_ {k} ^ {\top} x ^ {(i)}), y ^ {(i)}).\tag{2.15}
$$

Moreover, conveniently, the cross-entropy loss also has a simple gradient. Let $t = ( t _ { 1 } , \ldots , t _ { k } )$ , and recall $\begin{array} { r } { \phi _ { i } = \frac { \exp ( t _ { i } ) ^ { \sigma } } { \sum _ { j = 1 } ^ { k } \exp ( t _ { j } ) } } \end{array}$ . By basic calculus, we can derive

$$
\frac {\partial \ell_ {\mathrm{ce}} (t , y)}{\partial t _ {i}} = \phi_ {i} - 1 \{y = i \},\tag{2.16}
$$

where $1 \{ \cdot \}$ is the indicator function, that is, $1 \{ y   =   i \}   =   1$ if $y   =   i ,$ , and $1 \{ y   =   i \}   =   0 \mathrm { ~ i f ~ } y   \neq   i$ . Alternatively, in vectorized notations, we have the following form which will be useful for Chapter 7:

$$
\frac {\partial \ell_ {\mathrm{ce}} (t , y)}{\partial t} = \phi - e _ {y},\tag{2.17}
$$

where $e _ { s } \in \mathbb { R } ^ { k }$ is the s-th natural basis vector (where the s-th entry is 1 and all other entries are zeros.) Using Chain rule, we have that

$$
\frac {\partial \ell_ {\mathrm{ce}} ((\theta_ {1} ^ {\top} x , \dots , \theta_ {k} ^ {\top} x) , y)}{\partial \theta_ {i}} = \frac {\partial \ell (t , y)}{\partial t _ {i}} \cdot \frac {\partial t _ {i}}{\partial \theta_ {i}} = (\phi_ {i} - 1 \{y = i \}) \cdot x.\tag{2.18}
$$

Therefore, the gradient of the loss with respect to the part of parameter $\theta _ { i }$

$$
\frac {\partial \ell (\theta)}{\partial \theta_ {i}} = \sum_ {j = 1} ^ {n} (\phi_ {i} ^ {(j)} - 1 \{y ^ {(j)} = i \}) \cdot x ^ {(j)},\tag{2.19}
$$

where $\begin{array} { r } { \phi _ { i } ^ { ( j ) } = \frac { \exp ( \theta _ { i } ^ { \top } x ^ { ( j ) } ) } { \sum _ { s = 1 } ^ { k } \exp ( \theta _ { s } ^ { \top } x ^ { ( j ) } ) } } \end{array}$ is the probability that the model predicts item i for example $x ^ { ( j ) }$ . With the gradients above, one can implement (stochastic) gradient descent to minimize the loss function $\ell ( \theta )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>There are some ambiguity in the naming here. Some people call the cross-entropy loss the function that maps the probability vector (the φ in our language) and label y to the final real number, and call our version of cross-entropy loss softmax-cross-entropy loss. We choose our current naming convention because it’s consistent with the naming of most modern deep learning library such as PyTorch and Jax.</span></small>

<!-- page: 29 -->

![](images/page_28_chart_1.jpg)

![](images/page_28_chart_2.jpg)

![](images/page_28_chart_3.jpg)

## 2.4 Another algorithm for maximizing $\ell ( \theta )$

Returning to logistic regression with $g ( z )$ being the sigmoid function, let’s now talk about a different algorithm for maximizing $\ell ( \theta )$

To get us started, let’s consider Newton’s method for finding a zero of a function. Specifically, suppose we have some function $f : \mathbb { R } \mapsto$ R, and we wish to find a value of $\theta$ so that $f ( \theta )   =   0$ . Here, $\theta \in \mathbb { R }$ is a real number. Newton’s method performs the following update:

$$
\theta := \theta - \frac {f (\theta)}{f ^ {\prime} (\theta)}.
$$

This method has a natural interpretation in which we can think of it as approximating the function $f$ via a linear function that is tangent to $f$ at the current guess $\theta ,$ solving for where that linear function equals to zero, and letting the next guess for $\theta$ be where that linear function is zero.

Here’s a picture of the Newton’s method in action:

In the leftmost figure, we see the function f plotted along with the line $y = 0$ . We’re trying to find $\theta \; \mathrm { s o }$ that $f(\theta) = 0;$ the value of θ that achieves this is about 1.3. Suppose we initialized the algorithm with $\theta = 4 . 5$ . Newton’s method then fits a straight line tangent to $f$ at $\theta = 4 . 5$ , and solves for the where that line evaluates to 0. (Middle figure.) This give us the next guess for $\theta ,$ which is about 2.8. The rightmost figure shows the result of running one more iteration, which the updates $\theta$ to about 1.8. After a few more iterations, we rapidly approach $\theta = 1 . 3$

Newton’s method gives a way of getting to $f ( \theta ) = 0$ . What if we want to use it to maximize some function $\ell ?$ The maxima of \` correspond to points where its first derivative $\ell ^ { \prime } ( \theta )$ is zero. $\mathrm { S o } ,$ by letting $f ( \theta ) = \ell ^ { \prime } ( \theta )$ , we can use the same algorithm to maximize $\ell ,$ and we obtain update rule:

$$
\theta := \theta - \frac {\ell^ {\prime} (\theta)}{\ell^ {\prime \prime} (\theta)}.
$$

(Something to think about: How would this change if we wanted to use Newton’s method to minimize rather than maximize a function?)

<!-- page: 30 -->

Lastly, in our logistic regression setting, θ is vector-valued, so we need to generalize Newton’s method to this setting. The generalization of Newton’s method to this multidimensional setting (also called the Newton-Raphson method) is given by

$$
\theta := \theta - H ^ {- 1} \nabla_ {\theta} \ell (\theta).
$$

Here, $\nabla _ { \theta } \ell ( \theta )$ is, as usual, the vector of partial derivatives of $\ell ( \theta )$ with respect to the $\theta _ { i } { } ^ { \prime } \mathrm { s } _ { \mathrm { i } } ^ { \prime }$ and H is an d-by-d matrix (actually, $d{+}1{-}by{-}d{+}1$ , assuming that we include the intercept term) called the Hessian, whose entries are given by

$$
H _ {i j} = \frac {\partial^ {2} \ell (\theta)}{\partial \theta_ {i} \partial \theta_ {j}}.
$$

Newton’s method typically enjoys faster convergence than (batch) gradient descent, and requires many fewer iterations to get very close to the minimum. One iteration of Newton’s can, however, be more expensive than one iteration of gradient descent, since it requires finding and inverting an d-by-d Hessian; but so long as d is not too large, it is usually much faster overall. When Newton’s method is applied to maximize the logistic regression log likelihood function $\ell ( \theta )$ , the resulting method is also called Fisher scoring.

<!-- page: 31 -->

## Chapter 3

## Generalized linear models

So far, we’ve seen a regression example, and a classification example. In the regression example, we had $y | x ; \theta \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ , and in the classification one, $y | x ; \theta \sim$ Bernoulli(φ), for some appropriate definitions of $\mu$ and $\phi$ as functions of $x$ and $\theta .$ In this section, we will show that both of these methods are special cases of a broader family of models, called Generalized Linear Models (GLMs).<sup>1</sup> We will also show how other models in the GLM family can be derived and applied to other classification and regression problems.

## 3.1 The exponential family

To work our way up to GLMs, we will begin by defining exponential family distributions. We say that a class of distributions is in the exponential family if it can be written in the form

$$
p (y; \eta) = b (y) \exp (\eta^ {T} T (y) - a (\eta))\tag{3.1}
$$

Here, η is called the natural parameter (also called the canonical parameter) of the distribution; $T ( y )$ is the sufficient statistic (for the distributions we consider, it will often be the case that $T ( y ) = y )$ ; and $a ( \eta )$ is the log partition function. The quantity $e ^ { - a ( \eta ) }$ essentially plays the role of a normalization constant, that makes sure the distribution $p ( y ; \eta )$ sums/integrates over y to 1.

A fixed choice of $T ,   a$ and b defines a family (or set) of distributions that is parameterized by $\eta ;$ as we vary $\eta ,$ we then get different distributions within this family.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>The presentation of the material in this section takes inspiration from Michael I. Jordan, Learning in graphical models (unpublished book draft), and also McCullagh and Nelder, Generalized Linear Models (2nd ed.).</span></small>

<!-- page: 32 -->

We now show that the Bernoulli and the Gaussian distributions are examples of exponential family distributions. The Bernoulli distribution with mean $\phi ,$ written Bernoulli $( \phi )$ , specifies a distribution over $y \in \{ 0 , 1 \}$ , so that $p ( y   =   1 ; \phi )   =   \phi ; \; p ( y   =   0 ; \phi )   =   1 - \phi$ . As we vary $\phi ,$ we obtain Bernoulli distributions with different means. We now show that this class of Bernoulli distributions, ones obtained by varying $\phi ,$ is in the exponential family; $\mathbf { i . e . }$ that there is a choice of $T ,$ a and $b$ so that Equation (3.1) becomes exactly the class of Bernoulli distributions.

We write the Bernoulli distribution as:

$$
\begin{array}{r c l} p (y; \phi) & = & \phi^ {y} (1 - \phi) ^ {1 - y} \\ & = & \exp (y \log \phi + (1 - y) \log (1 - \phi)) \\ & = & \exp \left(\left(\log \left(\frac {\phi}{1 - \phi}\right)\right) y + \log (1 - \phi)\right). \end{array}
$$

Thus, the natural parameter is given by $\eta = \log ( \phi / ( 1 - \phi ) )$ . Interestingly, if we invert this definition for $\eta$ by solving for $\phi$ in terms of $\eta ,$ we obtain $\phi =$ $1 / ( 1 + e ^ { - \eta } )$ . This is the familiar sigmoid function! This will come up again when we derive logistic regression as a GLM. To complete the formulation of the Bernoulli distribution as an exponential family distribution, we also have

$$
\begin{array}{r c l} T (y) & = & y \\ a (\eta) & = & - \log (1 - \phi) \\ & = & \log (1 + e ^ {\eta}) \\ b (y) & = & 1 \end{array}
$$

This shows that the Bernoulli distribution can be written in the form of Equation (3.1), using an appropriate choice of $T$ , a and $b .$

Let’s now move on to consider the Gaussian distribution. Recall that, when deriving linear regression, the value of $\sigma ^ { 2 }$ had no effect on our final choice of $\theta$ and $h _ { \theta } ( x )$ . Thus, we can choose an arbitrary value for $\sigma ^ { 2 }$ without changing anything. To simplify the derivation below, let’s set $\sigma ^ { 2 } = 1 . ^ { 2 }$ We

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">σ.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">η∈R2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">a(η))/c(τ ))</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2If we leave σ as a variable, the Gaussian distribution can also be shown to be in the exponential family, where η ∈ R is now a dimension vector that depends on both  and µ For the purposes of GLMs, however, the σparameter can also be treated by considering 2 a more general definition of the exponential family: p(y; η, τ ) = b(a, τ ) exp((η<sup>T</sup> T(y) −. Here, τ is called the dispersion parameter, and for the Gaussian, c(τ ) = σ <sup>2</sup>; but given our simplification above, we won’t need the more general definition for the examples we will consider here.</span></small>

<!-- page: 33 -->

then have:

$$
\begin{array}{r c l} {p (y; \mu)} & = & {\frac {1}{\sqrt {2 \pi}} \exp \left(- \frac {1}{2} (y - \mu) ^ {2}\right)} \\ & = & {\frac {1}{\sqrt {2 \pi}} \exp \left(- \frac {1}{2} y ^ {2}\right) \cdot \exp \left(\mu y - \frac {1}{2} \mu^ {2}\right)} \end{array}
$$

Thus, we see that the Gaussian is in the exponential family, with

$$
\begin{array}{r c l} \eta & = & \mu \\ T (y) & = & y \\ a (\eta) & = & \mu^ {2} / 2 \\ & = & \eta^ {2} / 2 \\ b (y) & = & (1 / \sqrt {2 \pi}) \exp (- y ^ {2} / 2). \end{array}
$$

There’re many other distributions that are members of the exponential family: The multinomial (which we’ll see later), the Poisson (for modelling count-data; also see the problem set); the gamma and the exponential (for modelling continuous, non-negative random variables, such as timeintervals); the beta and the Dirichlet (for distributions over probabilities); and many more. In the next section, we will describe a general “recipe” for constructing models in which y (given x and θ) comes from any of these distributions.

## 3.2 Constructing GLMs

Suppose you would like to build a model to estimate the number y of customers arriving in your store (or number of page-views on your website) in any given hour, based on certain features x such as store promotions, recent advertising, weather, day-of-week, etc. We know that the Poisson distribution usually gives a good model for numbers of visitors. Knowing this, how can we come up with a model for our problem? Fortunately, the Poisson is an exponential family distribution, so we can apply a Generalized Linear Model (GLM). In this section, we will we will describe a method for constructing GLM models for problems such as these.

More generally, consider a classification or regression problem where we would like to predict the value of some random variable y as a function of x. To derive a GLM for this problem, we will make the following three assumptions about the conditional distribution of y given x and about our model:

<!-- page: 34 -->

1. $y \mid x ; \theta \sim$ ExponentialFamily(η). I.e., given x and $\theta ,$ the distribution of y follows some exponential family distribution, with parameter η.

2. Given $x ,$ our goal is to predict the expected value of $T ( y )$ given x. In most of our examples, we will have $T ( y ) \; = \; y$ , so this means we would like the prediction $h ( x )$ output by our learned hypothesis h to satisfy $h ( x ) \: = \: \operatorname { E } [ y | x ]$ (Note that this assumption is satisfied in the choices for $h _ { \theta } ( x )$ for both logistic regression and linear regression. For instance, in logistic regression, we had $h _ { \theta } ( x ) = p ( y = 1 | x ; \theta ) = 0 \cdot p ( y =$ $0 | x ; \theta ) + 1 \cdot p ( y = 1 | x ; \theta ) = \operatorname { E } [ y | x ; \theta ] . )$

3. The natural parameter η and the inputs x are related linearly: $\eta = \theta ^ { T } x$ (Or, if η is vector-valued, then $\eta _ { i } = \theta _ { i } ^ { T } x . )$

The third of these assumptions might seem the least well justified of the above, and it might be better thought of as a “design choice” in our recipe for designing GLMs, rather than as an assumption per se. These three assumptions/design choices will allow us to derive a very elegant class of learning algorithms, namely GLMs, that have many desirable properties such as ease of learning. Furthermore, the resulting models are often very effective for modelling different types of distributions over $y ;$ for example, we will shortly show that both logistic regression and ordinary least squares can both be derived as GLMs.

## 3.2.1 Ordinary least squares

To show that ordinary least squares is a special case of the GLM family of models, consider the setting where the target variable y (also called the response variable in GLM terminology) is continuous, and we model the conditional distribution of $y$ given x as a Gaussian $\mathcal { N } ( \mu , \sigma ^ { 2 } )$ . (Here, $\mu$ may depend $x . ) \mathrm { ~  ~ { ~ S o ~ } ~ }$ , we let the ExponentialF amily(η) distribution above be the Gaussian distribution. As we saw previously, in the formulation of the Gaussian as an exponential family distribution, we had $\mu = \eta$ . So, we have

$$
\begin{array}{r c l} h _ {\theta} (x) & = & E [ y | x; \theta ] \\ & = & \mu \\ & = & \eta \\ & = & \theta^ {T} x. \end{array}
$$

The first equality follows from Assumption 2, above; the second equality follows from the fact that $y | x ; \theta \sim \mathcal { N } ( \mu , \sigma ^ { 2 } )$ , and so its expected value is given

<!-- page: 35 -->

by $\mu ;$ the third equality follows from Assumption 1 (and our earlier derivation showing that $\mu   =   \eta$ in the formulation of the Gaussian as an exponential family distribution); and the last equality follows from Assumption 3.

## 3.2.2 Logistic regression

We now consider logistic regression. Here we are interested in binary classification, so $y \in \{ 0 , 1 \}$ . Given that y is binary-valued, it therefore seems natural to choose the Bernoulli family of distributions to model the conditional distribution of y given x. In our formulation of the Bernoulli distribution as an exponential family distribution, we had $\phi   =   1 / ( 1 + e ^ { - \eta } )$ . Furthermore, note that if $y | x ; \theta \sim \operatorname { B e r n o u l l i } ( \phi )$ , then $\operatorname { E } [ y | x ; \theta ] = \phi$ . So, following a similar derivation as the one for ordinary least squares, we get:

$$
\begin{array}{r c l} h _ {\theta} (x) & = & E [ y | x; \theta ] \\ & = & \phi \\ & = & 1 / (1 + e ^ {- \eta}) \\ & = & 1 / (1 + e ^ {- \theta^ {T} x}) \end{array}
$$

So, this gives us hypothesis functions of the form $h _ { \theta } ( x ) = 1 / ( 1 + e ^ { - \theta ^ { T } x } )$ . If you are previously wondering how we came up with the form of the logistic function $1 / ( 1 + e ^ { - z } )$ , this gives one answer: Once we assume that y conditioned on x is Bernoulli, it arises as a consequence of the definition of GLMs and exponential family distributions.

To introduce a little more terminology, the function g giving the distribution’s mean as a function of the natural parameter $( g ( \eta )   =   \operatorname { E } [ T ( y ) ; \eta ] )$ is called the canonical response function. Its inverse, $g ^ { - 1 }$ , is called the canonical link function. Thus, the canonical response function for the Gaussian family is just the identify function; and the canonical response function for the Bernoulli is the logistic function.<sup>3</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">g</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">−1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3Many texts use  to denote the link function, and gto denote the response function; but the notation we’re using here, inherited from the early machine learning literature, will be more consistent with the notation used in the rest of the class.</span></small>

<!-- page: 36 -->

## Chapter 4

# Generative learning algorithms

So far, we’ve mainly been talking about learning algorithms that model $p ( y | x ; \theta )$ , the conditional distribution of y given x. For instance, logistic regression modeled $p ( y | x ; \theta )$ as $h _ { \theta } ( x ) = g ( \theta ^ { T } x )$ where g is the sigmoid function. In these notes, we’ll talk about a different type of learning algorithm.

Consider a classification problem in which we want to learn to distinguish between elephants $( y   =   1 )$ and dogs $( y   =   0 )$ , based on some features of an animal. Given a training set, an algorithm like logistic regression or the perceptron algorithm (basically) tries to find a straight line—that is, a decision boundary—that separates the elephants and dogs. Then, to classify a new animal as either an elephant or a dog, it checks on which side of the decision boundary it falls, and makes its prediction accordingly.

Here’s a different approach. First, looking at elephants, we can build a model of what elephants look like. Then, looking at dogs, we can build a separate model of what dogs look like. Finally, to classify a new animal, we can match the new animal against the elephant model, and match it against the dog model, to see whether the new animal looks more like the elephants or more like the dogs we had seen in the training set.

Algorithms that try to learn $p ( y | x )$ directly (such as logistic regression), or algorithms that try to learn mappings directly from the space of inputs X to the labels {0, 1}, (such as the perceptron algorithm) are called discriminative learning algorithms. Here, we’ll talk about algorithms that instead try to model $p ( x | y )$ (and $p ( y ) )$ . These algorithms are called generative learning algorithms. For instance, if y indicates whether an example is a dog (0) or an elephant (1), then $p ( x | y = 0 )$ models the distribution of dogs features, and $p ( x | y = 1 )$ models the distribution of elephants’ features.

After modeling $p ( y )$ (called the class priors) and $p ( x | y )$ , our algorithm

<!-- page: 37 -->

can then use Bayes rule to derive the posterior distribution on y given x:

$$
p (y | x) = \frac {p (x | y) p (y)}{p (x)}.
$$

Here, the denominator is given by $p ( x )   =   p ( x | y   =   1 ) p ( y   =   1 )   +   p ( x | y   =$ $0 ) p ( y = 0 )$ (you should be able to verify that this is true from the standard properties of probabilities), and thus can also be expressed in terms of the quantities $p ( x | y )$ and $p ( y )$ that we’ve learned. Actually, if were calculating $p ( y | x )$ in order to make a prediction, then we don’t actually need to calculate the denominator, since

$$
\begin{array}{r c l} \arg \max _ {y} p (y | x) & = & \arg \max _ {y} \frac {p (x | y) p (y)}{p (x)} \\ & = & \arg \max _ {y} p (x | y) p (y). \end{array}
$$

## 4.1 Gaussian discriminant analysis

The first generative learning algorithm that we’ll look at is Gaussian discriminant analysis (GDA). In this model, we’ll assume that $p ( x | y )$ is distributed according to a multivariate normal distribution. Let’s talk briefly about the properties of multivariate normal distributions before moving on to the GDA model itself.

## 4.1.1 The multivariate normal distribution

The multivariate normal distribution in d-dimensions, also called the multi-variate Gaussian distribution, is parameterized by a mean vector $\mu \in \mathbb { R } ^ { d }$ and a covariance matrix $\Sigma \in \mathbb { R } ^ { d \times d }$ , where $\Sigma \geq 0$ is symmetric and positive semi-definite. Also written ${ \mathcal { N } } ( \mu , \Sigma )$ , its density is given by:

$$
p (x; \mu , \Sigma) = \frac {1}{(2 \pi) ^ {d / 2} | \Sigma | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x - \mu) ^ {T} \Sigma^ {- 1} (x - \mu)\right).
$$

In the equation above, $`` \left| \sum \right|  ''$ denotes the determinant of the matrix $\Sigma$ .

For a random variable X distributed $\mathcal { N } ( \mu , \Sigma )$ , the mean is (unsurprisingly) given by $\mu ;$

$$
\mathrm{E} [ X ] = \int_ {x} x p (x; \mu , \Sigma) d x = \mu
$$

The covariance of a vector-valued random variable Z is defined as $\mathrm{Cov}(Z) =$ $\mathrm{E}[(Z - \mathrm{E}[Z])(Z - \mathrm{E}[Z])^T]$ This generalizes the notion of the variance of a

<!-- page: 38 -->

real-valued random variable. The covariance can also be defined as $\mathrm{Cov}(Z) =$ $\operatorname { E } [ Z Z ^ { T } ] - ( \operatorname { E } [ Z ] ) ( \operatorname { E } [ Z ] ) ^ { T }$ . (You should be able to prove to yourself that these two definitions are equivalent.) If $X \sim \mathcal { N } ( \mu , \Sigma )$ , then

$$
\mathrm{Cov} (X) = \Sigma .
$$

Here are some examples of what the density of a Gaussian distribution looks like:

![](images/page_37_image_4.jpg)

The left-most figure shows a Gaussian with mean zero (that is, the 2x1 zero-vector) and covariance matrix $\Sigma = I$ (the 2x2 identity matrix). A Gaussian with zero mean and identity covariance is also called the standard normal distribution. The middle figure shows the density of a Gaussian with zero mean and $\Sigma = 0.6I;$ and in the rightmost figure shows one with , $\Sigma = 2 I$ We see that as Σ becomes larger, the Gaussian becomes more “spread-out,” and as it becomes smaller, the distribution becomes more “compressed.” Let’s look at some more examples.

![](images/page_37_image_6.jpg)

![](images/page_37_image_7.jpg)

![](images/page_37_image_8.jpg)

The figures above show Gaussians with mean 0, and with covariance matrices respectively

$$
\Sigma = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right]; \Sigma = \left[ \begin{array}{c c} 1 & 0. 5 \\ 0. 5 & 1 \end{array} \right]; \Sigma = \left[ \begin{array}{c c} 1 & 0. 8 \\ 0. 8 & 1 \end{array} \right].
$$

The leftmost figure shows the familiar standard normal distribution, and we see that as we increase the off-diagonal entry in $\Sigma ,$ the density becomes more

<!-- page: 39 -->

“compressed” towards the $4 5 ^ { \circ }$ line (given by $x _ { 1 } = x _ { 2 } )$ . We can see this more clearly when we look at the contours of the same three densities:

![](images/page_38_image_2.jpg)

Here’s one last set of examples generated by varying Σ:

![](images/page_38_image_4.jpg)

The plots above used, respectively,

$$
\Sigma = \left[ \begin{array}{c c} 1 & - 0. 5 \\ - 0. 5 & 1 \end{array} \right]; \Sigma = \left[ \begin{array}{c c} 1 & - 0. 8 \\ - 0. 8 & 1 \end{array} \right]; \Sigma = \left[ \begin{array}{c c} 3 & 0. 8 \\ 0. 8 & 1 \end{array} \right].
$$

From the leftmost and middle figures, we see that by decreasing the offdiagonal elements of the covariance matrix, the density now becomes “compressed” again, but in the opposite direction. Lastly, as we vary the parameters, more generally the contours will form ellipses (the rightmost figure showing an example).

As our last set of examples, fixing $\Sigma = I$ , by varying µ, we can also move the mean of the density around.

![](images/page_38_image_9.jpg)

<!-- page: 40 -->

The figures above were generated using $\Sigma = I$ , and respectively

$$
\mu = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right]; \mu = \left[ \begin{array}{c} - 0. 5 \\ 0 \end{array} \right]; \mu = \left[ \begin{array}{c} - 1 \\ - 1. 5 \end{array} \right].
$$

## 4.1.2 The Gaussian discriminant analysis model

When we have a classification problem in which the input features x are continuous-valued random variables, we can then use the Gaussian Discriminant Analysis (GDA) model, which models $p ( x | y )$ using a multivariate normal distribution. The model is:

$$
\begin{array}{r c l} y & \sim & \mathrm{Bernoulli} (\phi) \\ x | y = 0 & \sim & \mathcal {N} (\mu_ {0}, \Sigma) \\ x | y = 1 & \sim & \mathcal {N} (\mu_ {1}, \Sigma) \end{array}
$$

Writing out the distributions, this is:

$$
\begin{array}{r c l} p (y) & = & \phi^ {y} (1 - \phi) ^ {1 - y} \\ p (x | y = 0) & = & \frac {1}{(2 \pi) ^ {d / 2} | \Sigma | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x - \mu_ {0}) ^ {T} \Sigma^ {- 1} (x - \mu_ {0})\right) \\ p (x | y = 1) & = & \frac {1}{(2 \pi) ^ {d / 2} | \Sigma | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x - \mu_ {1}) ^ {T} \Sigma^ {- 1} (x - \mu_ {1})\right) \end{array}
$$

Here, the parameters of our model are $\phi , \; \Sigma , \; \mu _ { 0 }$ and $\mu _ { 1 }$ . (Note that while there’re two different mean vectors $\mu _ { 0 }$ and $\mu _ { 1 }$ , this model is usually applied using only one covariance matrix $\Sigma . )$ The log-likelihood of the data is given by

$$
\begin{array}{r c l} \ell (\phi , \mu_ {0}, \mu_ {1}, \Sigma) & = & \log \prod_ {i = 1} ^ {n} p (x ^ {(i)}, y ^ {(i)}; \phi , \mu_ {0}, \mu_ {1}, \Sigma) \\ & = & \log \prod_ {i = 1} ^ {n} p (x ^ {(i)} | y ^ {(i)}; \mu_ {0}, \mu_ {1}, \Sigma) p (y ^ {(i)}; \phi). \end{array}
$$

<!-- page: 41 -->

By maximizing \` with respect to the parameters, we find the maximum likelihood estimate of the parameters (see problem set 1) to be:

$$
\phi = \frac {1}{n} \sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}
$$

$$
\mu_ {0} = \frac {\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \} x ^ {(i)}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \}}
$$

$$
\mu_ {1} = \frac {\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \} x ^ {(i)}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}}
$$

$$
\Sigma = \frac {1}{n} \sum_ {i = 1} ^ {n} (x ^ {(i)} - \mu_ {y ^ {(i)}}) (x ^ {(i)} - \mu_ {y ^ {(i)}}) ^ {T}.
$$

Pictorially, what the algorithm is doing can be seen in as follows:

![](images/page_40_image_7.jpg)

Shown in the figure are the training set, as well as the contours of the two Gaussian distributions that have been fit to the data in each of the two classes. Note that the two Gaussians have contours that are the same shape and orientation, since they share a covariance matrix $\Sigma ,$ but they have different means $\mu _ { 0 }$ and $\mu _ { 1 }$ . Also shown in the figure is the straight line giving the decision boundary at which $p ( y   =   1 | x )   =   0 . 5$ . On one side of the boundary, we’ll predict $y = 1$ to be the most likely outcome, and on the other side, we’ll predict $y = 0$

<!-- page: 42 -->

## 4.1.3 Discussion: GDA and logistic regression

The GDA model has an interesting relationship to logistic regression. If we view the quantity $p ( y = 1 | x ; \phi , \mu _ { 0 } , \mu _ { 1 } , \Sigma )$ as a function of $x ,$ we’ll find that it can be expressed in the form

$$
p (y = 1 | x; \phi , \Sigma , \mu_ {0}, \mu_ {1}) = \frac {1}{1 + \exp (- \theta^ {T} x)},
$$

where $\theta$ is some appropriate function of $\phi , \Sigma , \mu _ { 0 } , \mu _ { 1 } . ^ { 1 }$ This is exactly the form that logistic regression—a discriminative algorithm—used to model $p ( y =$ $1 | x )$

When would we prefer one model over another? GDA and logistic regression will, in general, give different decision boundaries when trained on the same dataset. Which is better?

We just argued that if $p ( x | y )$ is multivariate gaussian (with shared Σ), then $p ( y | x )$ necessarily follows a logistic function. The converse, however, is not true; i.e., $p ( y | x )$ being a logistic function does not imply $p ( x | y )$ is multivariate gaussian. This shows that GDA makes stronger modeling assumptions about the data than does logistic regression. It turns out that when these modeling assumptions are correct, then GDA will find better fits to the data, and is a better model. Specifically, when $p ( x | y )$ is indeed gaussian (with shared Σ), then GDA is asymptotically efficient. Informally, this means that in the limit of very large training sets (large n), there is no algorithm that is strictly better than GDA (in terms of, say, how accurately they estimate $p ( y | x ) )$ In particular, it can be shown that in this setting, GDA will be a better algorithm than logistic regression; and more generally, even for small training set sizes, we would generally expect GDA to better.

In contrast, by making significantly weaker assumptions, logistic regression is also more robust and less sensitive to incorrect modeling assumptions. There are many different sets of assumptions that would lead to $p ( y | x )$ taking the form of a logistic function. For example, if $x | y = 0 \sim \mathrm { P o i s s o n } ( \lambda _ { 0 } )$ , and $x | y = 1 \sim \mathrm { P o i s s o n } ( \lambda _ { 1 } )$ , then $p ( y | x )$ will be logistic. Logistic regression will also work well on Poisson data like this. But if we were to use GDA on such data—and fit Gaussian distributions to such non-Gaussian data—then the results will be less predictable, and GDA may (or may not) do well.

To summarize: GDA makes stronger modeling assumptions, and is more data efficient (i.e., requires less training data to learn “well”) when the modeling assumptions are correct or at least approximately correct. Logistic

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i)’</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x0 (i) = 1;</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">( + )-</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>This uses the convention of redefining the x s on the right-hand-side to be d 1 dimensional vectors by adding the extra coordinate = 1; see problem set 1.</span></small>

<!-- page: 43 -->

regression makes weaker assumptions, and is significantly more robust to deviations from modeling assumptions. Specifically, when the data is indeed non-Gaussian, then in the limit of large datasets, logistic regression will almost always do better than GDA. For this reason, in practice logistic regression is used more often than GDA. (Some related considerations about discriminative vs. generative models also apply for the Naive Bayes algorithm that we discuss next, but the Naive Bayes algorithm is still considered a very good, and is certainly also a very popular, classification algorithm.)

## 4.2 Naive bayes (Optional Reading)

In GDA, the feature vectors x were continuous, real-valued vectors. Let’s now talk about a different learning algorithm in which the $x _ { j }$ ’s are discretevalued.

For our motivating example, consider building an email spam filter using machine learning. Here, we wish to classify messages according to whether they are unsolicited commercial (spam) email, or non-spam email. After learning to do this, we can then have our mail reader automatically filter out the spam messages and perhaps place them in a separate mail folder. Classifying emails is one example of a broader set of problems called text classification.

Let’s say we have a training set (a set of emails labeled as spam or non-spam). We’ll begin our construction of our spam filter by specifying the features $x _ { j }$ used to represent an email.

We will represent an email via a feature vector whose length is equal to the number of words in the dictionary. Specifically, if an email contains the j-th word of the dictionary, then we will set $x _ { j } = 1$ ; otherwise, we let $x _ { j } = 0$ For instance, the vector

$$
x = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{array} \right] \quad \begin{array}{l} \text {a} \\ \text {aardvark} \\ \text {aardwolf} \\ \vdots \\ \text {buy} \\ \vdots \\ \text {zygmurgy} \end{array}
$$

is used to represent an email that contains the words $a ^ { 2 }$ and “buy,” but not

<!-- page: 44 -->

“aardvark,” “aardwolf” or “zygmurgy.”<sup>2</sup> The set of words encoded into the feature vector is called the vocabulary, so the dimension of x is equal to the size of the vocabulary.

Having chosen our feature vector, we now want to build a generative model. So, we have to model $p ( x | y )$ . But if we have, say, a vocabulary of 50000 words, then $x \in \{ 0 , 1 \} ^ { 5 0 0 0 0 }$ (x is a 50000-dimensional vector of $0 ^ { \prime } \mathrm { s }$ and $\mathrm { 1 ^ { \prime } s ) }$ , and if we were to model x explicitly with a multinomial distribution over the $2 ^ { 5 0 0 0 0 }$ possible outcomes, then we’d end up with a $( 2 ^ { 5 0 0 0 0 }   -   1 )$ -dimensional parameter vector. This is clearly too many parameters.

To model $p ( x | y )$ , we will therefore make a very strong assumption. We will assume that the $x _ { i } ^ { \mathrm { ~ ' ~ } }$ s are conditionally independent given y. This assumption is called the Naive Bayes (NB) assumption, and the resulting algorithm is called the Naive Bayes classifier. For instance, if $y = 1$ means spam email; $`` \mathrm{buy}  ''$ is word 2087 and “price” is word 39831; then we are assuming that if I tell you $y = 1$ (that a particular piece of email is spam), then knowledge of $x _ { 2 0 8 7 }$ (knowledge of whether “buy” appears in the message) will have no effect on your beliefs about the value of $x _ { 3 9 8 3 1 }$ (whether “price” appears). More formally, this can be written $p ( x _ { 2 0 8 7 } | y ) = p ( x _ { 2 0 8 7 } | y , x _ { 3 9 8 3 1 } )$ . (Note that this is not the same as saying that x<sub>2087</sub> and x<sub>39831</sub> are independent, which would have been written $\text{" } p(x_{2087}) \; = \; p(x_{2087} | x_{39831})  \text{" }$ ; rather, we are only assuming that $x _ { 2 0 8 7 }$ and $x _ { 3 9 8 3 1 }$ are conditionally independent given $y . )$

We now have:

$$
\begin{array}{r l} & p (x _ {1}, \dots , x _ {5 0 0 0 0} | y) \\ & = p (x _ {1} | y) p (x _ {2} | y, x _ {1}) p (x _ {3} | y, x _ {1}, x _ {2}) \dots p (x _ {5 0 0 0 0} | y, x _ {1}, \dots , x _ {4 9 9 9 9}) \\ & = p (x _ {1} | y) p (x _ {2} | y) p (x _ {3} | y) \dots p (x _ {5 0 0 0 0} | y) \\ & = \prod_ {j = 1} ^ {d} p (x _ {j} | y) \end{array}
$$

The first equality simply follows from the usual properties of probabilities, and the second equality used the NB assumption. We note that even though

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Actually, rather than looking through an English dictionary for the list of all English words, in practice it is more common to look through our training set and encode in our feature vector only the words that occur at least once there. Apart from reducing the number of words modeled and hence reducing our computational and space requirements, this also has the advantage of allowing us to model/include as a feature many words that may appear in your email (such as “cs229”) but that you won’t find in a dictionary. Sometimes (as in the homework), we also exclude the very high frequency words (which will be words like “the,” “of,” “and”; these high frequency, “content free” words are called stop words) since they occur in so many documents and do little to indicate whether an email is spam or non-spam.</span></small>

<!-- page: 45 -->

the Naive Bayes assumption is an extremely strong assumptions, the resulting algorithm works well on many problems.

Our model is parameterized by $\phi _ { j | y = 1 } = p ( x _ { j } = 1 | y = 1 ) ,   \phi _ { j | y = 0 } = \underline { { p } } ( x _ { j } =$ $1 | y = 0 )$ , and $\phi _ { y } = p ( y = 1 )$ . As usual, given a training set $\{ (x^{(i)},y^{(i)}); \dot{i} =$ $\{ 1 , \ldots , n \}$ , we can write down the joint likelihood of the data:

$$
\mathcal {L} (\phi_ {y}, \phi_ {j | y = 0}, \phi_ {j | y = 1}) = \prod_ {i = 1} ^ {n} p (x ^ {(i)}, y ^ {(i)}).
$$

Maximizing this with respect to $\phi _ { y } , \phi _ { j | y = 0 }$ and $\phi _ { j | y = 1 }$ gives the maximum likelihood estimates:

$$
\begin{array}{r c l} \phi_ {j | y = 1} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{x _ {j} ^ {(i)} = 1 \land y ^ {(i)} = 1 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}} \\ \phi_ {j | y = 0} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{x _ {j} ^ {(i)} = 1 \land y ^ {(i)} = 0 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \}} \\ \phi_ {y} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}}{n} \end{array}
$$

In the equations above, the $`` \bigwedge ''$ symbol means “and.” The parameters have a very natural interpretation. For instance, $\phi _ { j | y = 1 }$ is just the fraction of the spam $( y = 1 )$ emails in which word $j$ does appear.

Having fit all these parameters, to make a prediction on a new example with features x, we then simply calculate

$$
\begin{array}{r c l} p (y = 1 | x) & = & \frac {p (x | y = 1) p (y = 1)}{p (x)} \\ & = & \frac {\left(\prod_ {j = 1} ^ {d} p (x _ {j} | y = 1)\right) p (y = 1)}{\left(\prod_ {j = 1} ^ {d} p (x _ {j} | y = 1)\right) p (y = 1) + \left(\prod_ {j = 1} ^ {d} p (x _ {j} | y = 0)\right) p (y = 0)}, \end{array}
$$

and pick whichever class has the higher posterior probability.

Lastly, we note that while we have developed the Naive Bayes algorithm mainly for the case of problems where the features $x _ { j }$ are binary-valued, the generalization to where $x _ { j }$ can take values in $\{ 1 , 2 , \ldots , k _ { j } \}$ is straightforward. Here, we would simply model $p ( x _ { j } | y )$ as multinomial rather than as Bernoulli. Indeed, even if some original input attribute (say, the living area of a house, as in our earlier example) were continuous valued, it is quite common to discretize it—that is, turn it into a small set of discrete values—and apply Naive Bayes. For instance, if we use some feature $x _ { j }$ to represent living area, we might discretize the continuous values as follows:

<!-- page: 46 -->

| Living area (sq. feet) | &lt; 400 | 400-800 | 800-1200 | 1200-1600 | >1600 |
| --- | --- | --- | --- | --- | --- |
| x<sub>i</sub> | 1 | 2 | 3 | 4 | 5 |

Thus, for a house with living area 890 square feet, we would set the value of the corresponding feature $x _ { j }$ to 3. We can then apply the Naive Bayes algorithm, and model $p ( x _ { j } | y )$ with a multinomial distribution, as described previously. When the original, continuous-valued attributes are not wellmodeled by a multivariate normal distribution, discretizing the features and using Naive Bayes (instead of GDA) will often result in a better classifier.

## 4.2.1 Laplace smoothing

The Naive Bayes algorithm as we have described it will work fairly well for many problems, but there is a simple change that makes it work much better, especially for text classification. Let’s briefly discuss a problem with the algorithm in its current form, and then talk about how we can fix it.

Consider spam/email classification, and let’s suppose that, we are in the year of 20xx, after completing CS229 and having done excellent work on the project, you decide around May 20xx to submit work you did to the NeurIPS conference for publication.<sup>3</sup> Because you end up discussing the conference in your emails, you also start getting messages with the word “neurips” in it. But this is your first NeurIPS paper, and until this time, you had not previously seen any emails containing the word “neurips”; in particular “neurips” did not ever appear in your training set of spam/non-spam emails. Assuming that “neurips” was the 35000th word in the dictionary, your Naive Bayes spam filter therefore had picked its maximum likelihood estimates of the parameters φ<sub>35000</sub>|y to be

$$
\begin{array}{r c l} \phi_ {3 5 0 0 0 | y = 1} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{x _ {3 5 0 0 0} ^ {(i)} = 1 \land y ^ {(i)} = 1 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}} = 0 \\ \phi_ {3 5 0 0 0 | y = 0} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{x _ {3 5 0 0 0} ^ {(i)} = 1 \land y ^ {(i)} = 0 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \}} = 0 \end{array}
$$

I.e., because it has never seen “neurips” before in either spam or non-spam training examples, it thinks the probability of seeing it in either type of email is zero. Hence, when trying to decide if one of these messages containing

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>NeurIPS is one of the top machine learning conferences. The deadline for submitting a paper is typically in May-June.</span></small>

<!-- page: 47 -->

“neurips” is spam, it calculates the class posterior probabilities, and obtains

$$
\begin{array}{r c l} p (y = 1 | x) & = & \frac {\prod_ {j = 1} ^ {d} p (x _ {j} | y = 1) p (y = 1)}{\prod_ {j = 1} ^ {d} p (x _ {j} | y = 1) p (y = 1) + \prod_ {j = 1} ^ {d} p (x _ {j} | y = 0) p (y = 0)} \\ & = & \frac {0}{0}. \end{array}
$$

This is because each of the terms $`` \textstyle \prod _ { j = 1 } ^ { d } p ( x _ { j } | y )  ''$ includes a term $p ( x _ { 3 5 0 0 0 } | y ) =$ 0 that is multiplied into it. Hence, our algorithm obtains $0 / 0$ , and doesn’t know how to make a prediction.

Stating the problem more broadly, it is statistically a bad idea to estimate the probability of some event to be zero just because you haven’t seen it before in your finite training set. Take the problem of estimating the mean of a multinomial random variable z taking values in $\{ 1 , \ldots , k \}$ . We can parameterize our multinomial with $\phi _ { j } = p ( z = j )$ . Given a set of n independent observations $\{ z ^ { ( 1 ) } , \ldots , z ^ { ( n ) } \}$ , the maximum likelihood estimates are given by

$$
\phi_ {j} = \frac {\sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \}}{n}.
$$

As we saw previously, if we were to use these maximum likelihood estimates, then some of the $\phi _ { j } { } ^ { \prime } \mathrm { s }$ might end up as zero, which was a problem. To avoid this, we can use Laplace smoothing, which replaces the above estimate with

$$
\phi_ {j} = \frac {1 + \sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \}}{k + n}.
$$

Here, we’ve added 1 to the numerator, and k to the denominator. Note that $\textstyle \sum _ { j = 1 } ^ { k } \phi _ { j } = 1$ still holds (check this yourself!), which is a desirable property since the $\phi _ { j } ^ { \mathrm { ~ l ~ } }$ ’s are estimates for probabilities that we know must sum to 1. $Also, $\phi _ { j } \neq 0$$ for all values of $j ,$ solving our problem of probabilities being estimated as zero. Under certain (arguably quite strong) conditions, it can be shown that the Laplace smoothing actually gives the optimal estimator of the $\phi _ { j } { } ^ { \prime } \mathrm { s }$

Returning to our Naive Bayes classifier, with Laplace smoothing, we therefore obtain the following estimates of the parameters:

$$
\phi_ {j | y = 1} = \frac {1 + \sum_ {i = 1} ^ {n} 1 \{x _ {j} ^ {(i)} = 1 \land y ^ {(i)} = 1 \}}{2 + \sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}}
$$

$$
\phi_ {j | y = 0} = \frac {1 + \sum_ {i = 1} ^ {n} 1 \{x _ {j} ^ {(i)} = 1 \land y ^ {(i)} = 0 \}}{2 + \sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \}}
$$

<!-- page: 48 -->

(In practice, it usually doesn’t matter much whether we apply Laplace smoothing to $\phi _ { y }$ or not, since we will typically have a fair fraction each of spam and non-spam messages, so $\phi _ { y }$ will be a reasonable estimate of $p ( y = 1 )$ and will be quite far from 0 anyway.)

## 4.2.2 Event models for text classification

To close off our discussion of generative learning algorithms, let’s talk about one more model that is specifically for text classification. While Naive Bayes as we’ve presented it will work well for many classification problems, for text classification, there is a related model that does even better.

In the specific context of text classification, Naive Bayes as presented uses the what’s called the Bernoulli event model (or sometimes multi-variate Bernoulli event model). In this model, we assumed that the way an email is generated is that first it is randomly determined (according to the class priors $p ( y ) )$ whether a spammer or non-spammer will send you your next message. Then, the person sending the email runs through the dictionary, deciding whether to include each word $j$ in that email independently and according to the probabilities $p ( x _ { j } = 1 | y ) = \phi _ { j | y }$ . Thus, the probability of a message was given by $\textstyle p ( y ) \prod _ { j = 1 } ^ { d } p ( x _ { j } | y )$

Here’s a different model, called the Multinomial event model. To describe this model, we will use a different notation and set of features for representing emails. We let $x _ { j }$ denote the identity of the j-th word in the email. Thus, $x _ { j }$ is now an integer taking values in $\{ 1 , \ldots , | V | \}$ , where $| V |$ is the size of our vocabulary (dictionary). An email of d words is now represented by a vector $( x _ { 1 } , x _ { 2 } , \ldots , x _ { d } )$ of length $d ;$ note that $d$ can vary for different documents. For instance, if an email starts with “A NeurIPS ” then $x_{1}   =   1   ( ``a$ is the first word in the dictionary), and $x _ { 2 }   =   3 5 0 0 0$ (if “neurips” is the 35000th word in the dictionary).

In the multinomial event model, we assume that the way an email is generated is via a random process in which spam/non-spam is first determined (according to $p ( y ) )$ as before. Then, the sender of the email writes the email by first generating $x _ { 1 }$ from some multinomial distribution over words $( p ( x _ { 1 } | y ) )$ . Next, the second word $x _ { 2 }$ is chosen independently of $x _ { 1 }$ but from the same multinomial distribution, and similarly for $x _ { 3 } ,   x _ { 4 }$ , and so on, until all d words of the email have been generated. Thus, the overall probability of a message is given by $\textstyle p ( y ) \prod _ { j = 1 } ^ { d } p ( x _ { j } | y )$ . Note that this formula looks like the one we had earlier for the probability of a message under the Bernoulli event model, but that the terms in the formula now mean very different things. In particular $x _ { j } | y$ is now a multinomial, rather than a Bernoulli distribution.

<!-- page: 49 -->

The parameters for our new model are $\phi _ { y }   =   p ( y )$ as before, $\phi _ { k | y = 1 }   =$ $p ( x _ { j } = k | y = 1 )$ (for any j) and $\phi _ { k | y = 0 } = p ( x _ { j } = k | y = 0 )$ . Note that we have assumed that $p ( x _ { j } | y )$ is the same for all values of $j \; ( \mathrm { i . e . }$ , that the distribution according to which a word is generated does not depend on its position $j$ within the email).

If we are given a training set $\{ ( x ^ { ( i ) } , y ^ { ( i ) } ) ; i \; = \; 1 , \ldots , n \}$ where $x ^ { ( i ) } =$ $( x _ { 1 } ^ { ( i ) } , x _ { 2 } ^ { ( i ) } , \ldots , \tilde { x _ { d _ { i } } ^ { ( i ) } } )$ (here, $d _ { i }$ is the number of words in the i-training example), the likelihood of the data is given by

$$
\begin{array}{l l l} \mathcal {L} (\phi_ {y}, \phi_ {k | y = 0}, \phi_ {k | y = 1}) & = & \prod_ {i = 1} ^ {n} p (x ^ {(i)}, y ^ {(i)}) \\ & = & \prod_ {i = 1} ^ {n} \left(\prod_ {j = 1} ^ {d _ {i}} p (x _ {j} ^ {(i)} | y; \phi_ {k | y = 0}, \phi_ {k | y = 1})\right) p (y ^ {(i)}; \phi_ {y}). \end{array}
$$

Maximizing this yields the maximum likelihood estimates of the parameters:

$$
\begin{array}{r c l} \phi_ {k | y = 1} & = & \frac {\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {d _ {i}} 1 \{x _ {j} ^ {(i)} = k \wedge y ^ {(i)} = 1 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \} d _ {i}} \\ \phi_ {k | y = 0} & = & \frac {\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {d _ {i}} 1 \{x _ {j} ^ {(i)} = k \wedge y ^ {(i)} = 0 \}}{\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \} d _ {i}} \\ \phi_ {y} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \}}{n}. \end{array}
$$

If we were to apply Laplace smoothing (which is needed in practice for good performance) when estimating $\phi _ { k | y = 0 }$ and $\phi _ { k | y = 1 }$ , we add 1 to the numerators and $| V |$ to the denominators, and obtain:

$$
\begin{array}{r c l} \phi_ {k | y = 1} & = & \frac {1 + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {d _ {i}} 1 \{x _ {j} ^ {(i)} = k \wedge y ^ {(i)} = 1 \}}{| V | + \sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 1 \} d _ {i}} \\ \phi_ {k | y = 0} & = & \frac {1 + \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {d _ {i}} 1 \{x _ {j} ^ {(i)} = k \wedge y ^ {(i)} = 0 \}}{| V | + \sum_ {i = 1} ^ {n} 1 \{y ^ {(i)} = 0 \} d _ {i}}. \end{array}
$$

While not necessarily the very best classification algorithm, the Naive Bayes classifier often works surprisingly well. It is often also a very good “first thing to $\mathrm { t r y } , ^ { \prime \prime }$ given its simplicity and ease of implementation.

<!-- page: 50 -->

## Chapter 5

## Kernel methods

## 5.1 Feature maps

Recall that in our discussion about linear regression, we considered the problem of predicting the price of a house (denoted by $( y )$ from the living area of the house (denoted by $x )$ , and we fit a linear function of x to the training data. What if the price y can be more accurately represented as a non-linear function of $x ?$ In this case, we need a more expressive family of models than linear models.

We start by considering fitting cubic functions $y = \theta _ { 3 } x ^ { 3 } + \theta _ { 2 } x ^ { 2 } + \theta _ { 1 } x + \theta _ { 0 }$ It turns out that we can view the cubic function as a linear function over the a different set of feature variables (defined below). Concretely, let the function $\phi : \mathbb { R } \rightarrow \mathbb { R } ^ { 4 }$ be defined as

$$
\phi (x) = \left[ \begin{array}{c} 1 \\ x \\ x ^ {2} \\ x ^ {3} \end{array} \right] \in \mathbb {R} ^ {4}.\tag{5.1}
$$

Let $\theta \in \mathbb { R } ^ { 4 }$ be the vector containing $\theta _ { 0 } , \theta _ { 1 } , \theta _ { 2 } , \theta _ { 3 }$ as entries. Then we can rewrite the cubic function in x as:

$$
\theta_ {3} x ^ {3} + \theta_ {2} x ^ {2} + \theta_ {1} x + \theta_ {0} = \theta^ {T} \phi (x)
$$

Thus, a cubic function of the variable x can be viewed as a linear function over the variables $\phi ( x )$ . To distinguish between these two sets of variables, in the context of kernel methods, we will call the “original” input value the input attributes of a problem (in this case, x, the living area). When the

<!-- page: 51 -->

original input is mapped to some new set of quantities $\phi ( x )$ , we will call those new quantities the features variables. (Unfortunately, different authors use different terms to describe these two things in different contexts.) We will call $\phi$ a feature map, which maps the attributes to the features.

## 5.2 LMS (least mean squares) with features

We will derive the gradient descent algorithm for fitting the model $\theta ^ { T } \phi ( x )$ First recall that for ordinary least square problem where we were to fit $\theta ^ { T } x ,$ the batch gradient descent update is (see the first lecture note for its derivation):

$$
\begin{array}{c} \theta := \theta + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - h _ {\theta} (x ^ {(i)})\right) x ^ {(i)} \\ := \theta + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - \theta^ {T} x ^ {(i)}\right) x ^ {(i)}. \end{array}\tag{5.2}
$$

Let $\phi : \mathbb { R } ^ { d } \rightarrow \mathbb { R } ^ { p }$ be a feature map that maps attribute $x ( \mathrm { i n } \mathbb { R } ^ { d } )$ to the features $\phi ( x )$ in $\mathbb { R } ^ { p }$ . (In the motivating example in the previous subsection, we have $d = 1$ and $p = 4 . )$ Now our goal is to fit the function $\theta ^ { T } \phi ( x )$ , with $\theta$ being a vector in $\mathbb { R } ^ { p }$ instead of $\mathbb { R } ^ { d }$ . We can replace all the occurrences of $x ^ { ( i ) }$ in the algorithm above by $\phi ( x ^ { ( i ) } )$ to obtain the new update:

$$
\theta := \theta + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right) \phi (x ^ {(i)})\tag{5.3}
$$

Similarly, the corresponding stochastic gradient descent update rule is

$$
\theta := \theta + \alpha \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right) \phi (x ^ {(i)})\tag{5.4}
$$

## 5.3 LMS with the kernel trick

The gradient descent update, or stochastic gradient update above becomes computationally expensive when the features $\phi ( x )$ is high-dimensional. For example, consider the direct extension of the feature map in equation (5.1) to high-dimensional input x: suppose $x \in \mathbb { R } ^ { d }$ , and let $\phi ( x )$ be the vector that

<!-- page: 52 -->

contains all the monomials of x with degree $\leq 3$

$$
\phi (x) = \left[ \begin{array}{c} 1 \\ x _ {1} \\ x _ {2} \\ \vdots \\ x _ {1} ^ {2} \\ x _ {1} x _ {2} \\ x _ {1} x _ {3} \\ \vdots \\ x _ {2} x _ {1} \\ \vdots \\ x _ {1} ^ {3} \\ x _ {1} ^ {2} x _ {2} \\ \vdots \end{array} \right].\tag{5.5}
$$

The dimension of the features $\phi ( x )$ is on the order of $d ^ { 3 } . ^ { 1 }$ This is a prohibitively long vector for computational purposes — when $d   =   1 0 0 0$ , each update requires at least computing and storing a $1 0 0 0 ^ { 3 }   =   1 0 ^ { 9 }$ dimensional vector, which is $1 0 ^ { 6 }$ times slower than the update rule for ordinary least squares updates (5.2).

It may appear at first that such $d ^ { 3 }$ runtime per update and memory usage are inevitable, because the vector $\theta$ itself is of dimension $p \approx d ^ { 3 }$ , and we may need to update every entry of $\theta$ and store it. However, we will introduce the kernel trick with which we will not need to store $\theta$ explicitly, and the runtime can be significantly improved.

For simplicity, we initialize $\theta \; = \; 0$ , and we focus on the iterative update (5.3). The main observation is that at any time, $\theta$ can be represented as a linear combination of the vectors $\phi ( x ^ { ( 1 ) } ) , \ldots , \phi ( x ^ { ( n ) } )$ . Indeed, we can show this inductively as follows. At initialization, $\begin{array} { r } { \theta = 0 = \sum _ { i = 1 } ^ { n } 0 \cdot \phi ( x ^ { ( i ) } ) } \end{array}$ Assume at some point, $\theta$ can be represented as

$$
\theta = \sum_ {i = 1} ^ {n} \beta_ {i} \phi (x ^ {(i)})\tag{5.6}
$$

for some $\beta _ { 1 } , \ldots , \beta _ { n } \in \mathbb { R }$ . Then we claim that in the next round, $\theta$ is still a

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x2x3x1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">. φ(x)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 + d + d2 + d3</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Here, for simplicity, we include all the monomials with repetitions (so that, e.g., x<sub>1</sub><sup>x</sup><sub>2</sub><sup>x</sup><sub>3</sub> and both appear in φ( )) Therefore, there are totally 1 + d + d+ dentries in</span></small>

<!-- page: 53 -->

linear combination of $\phi ( x ^ { ( 1 ) } ) , \ldots , \phi ( x ^ { ( n ) } )$ because

$$
\begin{array}{l} \theta := \theta + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right) \phi (x ^ {(i)}) \\ \quad = \sum_ {i = 1} ^ {n} \beta_ {i} \phi (x ^ {(i)}) + \alpha \sum_ {i = 1} ^ {n} \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right) \phi (x ^ {(i)}) \\ \quad = \sum_ {i = 1} ^ {n} \underbrace {\left(\beta_ {i} + \alpha \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right)\right)} _ {\text {new} \beta_ {i}} \phi (x ^ {(i)}) \end{array}\tag{5.7}
$$

You may realize that our general strategy is to implicitly represent the $p -$ dimensional vector $\theta$ by a set of coefficients $\beta _ { 1 } , \ldots , \beta _ { n }$ . Towards doing this, we derive the update rule of the coefficients $\beta _ { 1 } , \ldots , \beta _ { n }$ . Using the equation above, we see that the new $\beta _ { i }$ depends on the old one via

$$
\beta_ {i} := \beta_ {i} + \alpha \left(y ^ {(i)} - \theta^ {T} \phi (x ^ {(i)})\right)\tag{5.8}
$$

Here we still have the old $\theta$ on the RHS of the equation. Replacing $\theta$ by $\begin{array} { r } { \theta = \sum _ { j = 1 } ^ { n } \beta _ { j } \phi ( x ^ { ( j ) } ) } \end{array}$ gives

$$
\forall i \in \{1, \dots , n \}, \beta_ {i} := \beta_ {i} + \alpha \left(y ^ {(i)} - \sum_ {j = 1} ^ {n} \beta_ {j} \phi (x ^ {(j)}) ^ {T} \phi (x ^ {(i)})\right)
$$

We often rewrite $\phi { ( { x ^ { ( j ) } } ) } ^ { T } \phi ( { x ^ { ( i ) } } )$ as $\langle \phi ( x ^ { ( j ) } ) , \phi ( x ^ { ( i ) } ) \rangle$ to emphasize that it’s the inner product of the two feature vectors. Viewing $\beta _ { i } \mathrm { { ^ \prime } s }$ as the new representation of $\theta ,$ we have successfully translated the batch gradient descent algorithm into an algorithm that updates the value of $\beta$ iteratively. It may appear that at every iteration, we still need to compute the values of $\langle \phi ( x ^ { ( j ) } ) , \widetilde { \phi ( x ^ { ( i ) } ) } \rangle$ for all pairs of $i , j$ , each of which may take roughly $O ( p )$ operation. However, two important properties come to rescue:

1. We can pre-compute the pairwise inner products $\langle \phi ( x ^ { ( j ) } ) , \phi ( x ^ { ( i ) } ) \rangle$ for all pairs of $i , j$ before the loop starts.

2. For the feature map $\phi$ defined in (5.5) (or many other interesting feature maps), computing $\langle \phi ( x ^ { ( j ) } ) , \phi \dot { ( } x ^ { ( i ) } ) \rangle$ can be efficient and does not

<!-- page: 54 -->

necessarily require computing $\phi ( x ^ { ( i ) } )$ explicitly. This is because:

$$
\begin{array}{l} \langle \phi (x), \phi (z) \rangle = 1 + \sum_ {i = 1} ^ {d} x _ {i} z _ {i} + \sum_ {i, j \in \{1, \dots , d \}} x _ {i} x _ {j} z _ {i} z _ {j} + \sum_ {i, j, k \in \{1, \dots , d \}} x _ {i} x _ {j} x _ {k} z _ {i} z _ {j} z _ {k} \\ = 1 + \sum_ {i = 1} ^ {d} x _ {i} z _ {i} + \left(\sum_ {i = 1} ^ {d} x _ {i} z _ {i}\right) ^ {2} + \left(\sum_ {i = 1} ^ {d} x _ {i} z _ {i}\right) ^ {3} \\ = 1 + \langle x, z \rangle + \langle x, z \rangle^ {2} + \langle x, z \rangle^ {3} \end{array} \tag {5.9}
$$

Therefore, to compute $\langle \phi ( x ) , \phi ( z ) \rangle$ , we can first compute $\langle x , z \rangle$ with $O ( d )$ time and then take another constant number of operations to compute $1 + \langle x , z \rangle + \langle x , z \rangle ^ { 2 } + \langle x , z \rangle ^ { 3 }$

As you will see, the inner products between the features $\langle \phi ( x ) , \phi ( z ) \rangle$ are essential here. We define the Kernel corresponding to the feature map $\phi$ as a function that maps $\mathcal { X } \times \mathcal { X } \rightarrow \mathbb { R }$ satisfying: <sup>2</sup>

$$
K (x, z) \triangleq \langle \phi (x), \phi (z) \rangle\tag{5.10}
$$

To wrap up the discussion, we write the down the final algorithm as follows:

1. Compute all the values $K ( x ^ { ( i ) } , x ^ { ( j ) } ) ~ \triangleq ~ \langle \phi ( x ^ { ( i ) } ) , \phi ( x ^ { ( j ) } ) \rangle$ using equation (5.9) for all $i , j \in \{ 1 , \ldots , n \}$ . Set $\beta : = 0$

2. Loop:

$$
\forall i \in \{1, \dots , n \}, \beta_ {i} := \beta_ {i} + \alpha \left(y ^ {(i)} - \sum_ {j = 1} ^ {n} \beta_ {j} K (x ^ {(i)}, x ^ {(j)})\right)\tag{5.11}
$$

Or in vector notation, letting K be the $n \times n$ matrix with $K _ { i j } =$ $K ( x ^ { ( i ) } , x ^ { ( j ) } )$ , we have

$$
\beta := \beta + \alpha (\vec {y} - K \beta)
$$

With the algorithm above, we can update the representation $\beta$ of the vector $\theta$ efficiently with $O ( n )$ time per update. Finally, we need to show that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">X = Rd</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Recall that X is the space of the input x. In our running example, X = R<sup>d</sup></span></small>

<!-- page: 55 -->

the knowledge of the representation $\beta$ suffices to compute the prediction $\theta ^ { T } \phi ( x )$ . Indeed, we have

$$
\theta^ {T} \phi (x) = \sum_ {i = 1} ^ {n} \beta_ {i} \phi (x ^ {(i)}) ^ {T} \phi (x) = \sum_ {i = 1} ^ {n} \beta_ {i} K (x ^ {(i)}, x)\tag{5.12}
$$

You may realize that fundamentally all we need to know about the feature map $\phi ( \cdot )$ is encapsulated in the corresponding kernel function $K ( \cdot , \cdot )$ . We will expand on this in the next section.

## 5.4 Properties of kernels

In the last subsection, we started with an explicitly defined feature map $\phi ,$ which induces the kernel function $K ( x , z ) \triangleq \langle \phi ( x ) , \phi ( z ) \rangle$ . Then we saw that the kernel function is so intrinsic so that as long as the kernel function is defined, the whole training algorithm can be written entirely in the language of the kernel without referring to the feature map $\phi ,$ so can the prediction of a test example x (equation (5.12).)

Therefore, it would be tempted to define other kernel function $K ( \cdot , \cdot )$ and run the algorithm (5.11). Note that the algorithm (5.11) does not need to explicitly access the feature map $\phi ,$ and therefore we only need to ensure the existence of the feature map $\phi .$ , but do not necessarily need to be able to explicitly write $\phi$ down.

What kinds of functions $K ( \cdot , \cdot )$ can correspond to some feature map $\phi ?$ In other words, can we tell if there is some feature mapping $\phi$ so that $K(x,z)=$ $\phi ( x ) ^ { T } \phi ( z )$ for all $x , \; z ?$

If we can answer this question by giving a precise characterization of valid kernel functions, then we can completely change the interface of selecting feature maps $\phi$ to the interface of selecting kernel function $K$ . Concretely, we can pick a function $K$ , verify that it satisfies the characterization (so that there exists $\mathbf { a }$ feature map $\phi$ that $K$ corresponds to), and then we can run update rule (5.11). The benefit here is that we don’t have to be able to compute $\phi$ or write it down analytically, and we only need to know its existence. We will answer this question at the end of this subsection after we go through several concrete examples of kernels.

Suppose $x , z \in \mathbb { R } ^ { d }$ , and let’s first consider the function $K ( \cdot , \cdot )$ defined as:

$$
K (x, z) = (x ^ {T} z) ^ {2}.
$$

<!-- page: 56 -->

We can also write this as

$$
\begin{array}{r c l} K (x, z) & = & \left(\sum_ {i = 1} ^ {d} x _ {i} z _ {i}\right) \left(\sum_ {j = 1} ^ {d} x _ {j} z _ {j}\right) \\ & = & \sum_ {i = 1} ^ {d} \sum_ {j = 1} ^ {d} x _ {i} x _ {j} z _ {i} z _ {j} \\ & = & \sum_ {i, j = 1} ^ {d} (x _ {i} x _ {j}) (z _ {i} z _ {j}) \end{array}
$$

Thus, we see that $K ( x , z )   =   \langle \phi ( x ) , \phi ( z ) \rangle$ is the kernel function that corresponds to the feature mapping φ given (shown here for the case of $d = 3 )$ by

$$
\phi (x) = \left[ \begin{array}{l} x _ {1} x _ {1} \\ x _ {1} x _ {2} \\ x _ {1} x _ {3} \\ x _ {2} x _ {1} \\ x _ {2} x _ {2} \\ x _ {2} x _ {3} \\ x _ {3} x _ {1} \\ x _ {3} x _ {2} \\ x _ {3} x _ {3} \end{array} \right].
$$

Revisiting the computational efficiency perspective of kernel, note that whereas calculating the high-dimensional $\phi ( x )$ requires $O ( d ^ { 2 } )$ time, finding $K ( x , z )$ takes only $O ( d )$ time—linear in the dimension of the input attributes.

For another related example, also consider $K ( \cdot , \cdot )$ defined by

$$
\begin{array}{r c l} K (x, z) & = & (x ^ {T} z + c) ^ {2} \\ & = & \sum_ {i, j = 1} ^ {d} (x _ {i} x _ {j}) (z _ {i} z _ {j}) + \sum_ {i = 1} ^ {d} (\sqrt {2 c} x _ {i}) (\sqrt {2 c} z _ {i}) + c ^ {2}. \end{array}
$$

(Check this yourself.) This function K is a kernel function that corresponds

<!-- page: 57 -->

to the feature mapping (again shown for $d = 3 )$

$$
\phi (x) = \left[ \begin{array}{c} x _ {1} x _ {1} \\ x _ {1} x _ {2} \\ x _ {1} x _ {3} \\ x _ {2} x _ {1} \\ x _ {2} x _ {2} \\ x _ {2} x _ {3} \\ x _ {3} x _ {1} \\ x _ {3} x _ {2} \\ x _ {3} x _ {3} \\ \sqrt {2 c} x _ {1} \\ \sqrt {2 c} x _ {2} \\ \sqrt {2 c} x _ {3} \\ c \end{array} \right],
$$

and the parameter c controls the relative weighting between the $x _ { i }$ (first order) and the $x _ { i } x _ { j }$ (second order) terms.

More broadly, the kernel $K ( x , z )   =   ( x ^ { T } z + c ) ^ { k }$ corresponds to a feature mapping to an ${ \binom { d + k } { k } }$ feature space, corresponding of all monomials of the form $x _ { i _ { 1 } } x _ { i _ { 2 } } \ldots x _ { i _ { k } }$ that are up to order $k .$ However, despite working in this $O ( d ^ { k } )$ -dimensional space, computing $K ( x , z )$ still takes only $O ( d )$ time, and hence we never need to explicitly represent feature vectors in this very high dimensional feature space.

Kernels as similarity metrics. Now, let’s talk about a slightly different view of kernels. Intuitively, (and there are things wrong with this intuition, but nevermind), if $\phi ( x )$ and $\phi ( z )$ are close together, then we might expect $K ( x , z ) = \phi ( x ) ^ { T } \phi ( z )$ to be large. Conversely, if $\phi ( x )$ and $\phi ( z )$ are far apart— say nearly orthogonal to each other—then $K ( x , z ) = \phi ( x ) ^ { T } \phi ( z )$ will be small. So, we can think of $K ( x , z )$ as some measurement of how similar are $\phi ( x )$ and $\phi ( z )$ , or of how similar are x and z.

Given this intuition, suppose that for some learning problem that you’re working on, you’ve come up with some function $K ( x , z )$ that you think might be a reasonable measure of how similar x and $z   \mathrm { a r e }$ . For instance, perhaps you chose

$$
K (x, z) = \exp \left(- \frac {| | x - z | | ^ {2}}{2 \sigma^ {2}}\right).
$$

This is a reasonable measure of x and $z   ^ { \prime } \mathrm { s }$ similarity, and is close to 1 when x and z are close, and near 0 when x and z are far apart. Does there exist

<!-- page: 58 -->

a feature map $\phi$ such that the kernel K defined above satisfies $K ( x , z )   =$ $\phi ( x ) ^ { T } \phi ( z ) ?$ In this particular example, the answer is yes. This kernel is called the Gaussian kernel, and corresponds to an infinite dimensional feature mapping $\phi .$ We will give a precise characterization about what properties a function K needs to satisfy so that it can be a valid kernel function that corresponds to some feature map $\phi .$

Necessary conditions for valid kernels. Suppose for now that $K$ is indeed a valid kernel corresponding to some feature mapping $\phi ,$ and we will first see what properties it satisfies. Now, consider some finite set of $n$ points (not necessarily the training set) $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \}$ , and let a square, n-by-n matrix K be defined so that its $( i , j )$ -entry is given by $K _ { i j }   =   K ( x ^ { ( i ) } , x ^ { ( j ) } )$ This matrix is called the kernel matrix. Note that we’ve overloaded the notation and used K to denote both the kernel function $K ( x , z )$ and the kernel matrix K, due to their obvious close relationship.

Now, if K is a valid kernel, then $K _ { i j }   =   K ( x ^ { ( i ) } , x ^ { ( j ) } )   =   \phi ( x ^ { ( i ) } ) ^ { T } \phi ( x ^ { ( j ) } )   =$ $\phi ( x ^ { ( j ) } ) ^ { T } \phi ( x ^ { ( i ) } ) = K ( x ^ { ( j ) } , x ^ { ( i ) } ) = K _ { j i }$ , and hence K must be symmetric. Moreover, letting $\phi _ { k } ( x )$ denote the k-th coordinate of the vector $\phi ( x )$ , we find that for any vector z, we have

$$
\begin{array}{l l} z ^ {T} K z & = \sum_ {i} \sum_ {j} z _ {i} K _ {i j} z _ {j} \\ & = \sum_ {i} \sum_ {j} z _ {i} \phi (x ^ {(i)}) ^ {T} \phi (x ^ {(j)}) z _ {j} \\ & = \sum_ {i} \sum_ {j} z _ {i} \sum_ {k} \phi_ {k} (x ^ {(i)}) \phi_ {k} (x ^ {(j)}) z _ {j} \\ & = \sum_ {k} \sum_ {i} \sum_ {j} z _ {i} \phi_ {k} (x ^ {(i)}) \phi_ {k} (x ^ {(j)}) z _ {j} \\ & = \sum_ {k} \left(\sum_ {i} z _ {i} \phi_ {k} (x ^ {(i)})\right) ^ {2} \\ & \geq 0. \end{array}
$$

The second-to-last step uses the fact that $\textstyle \sum _ { i , j } a _ { i } a _ { j } \; = \; ( \sum _ { i } a _ { i } ) ^ { 2 }$ for $a _ { i } =$ $z _ { i } \phi _ { k } ( x ^ { ( i ) } )$ . Since z was arbitrary, this shows that K is positive semi-definite $( K \geq 0 )$

Hence, we’ve shown that if K is a valid kernel (i.e., if it corresponds to some feature mapping $\phi )$ , then the corresponding kernel matrix $K \in \mathbb { R } ^ { n \times n }$ is symmetric positive semidefinite.

<!-- page: 59 -->

Sufficient conditions for valid kernels. More generally, the condition above turns out to be not only a necessary, but also a sufficient, condition for K to be a valid kernel (also called a Mercer kernel). The following result is due to Mercer.<sup>3</sup>

Theorem (Mercer). Let $K : \mathbb { R } ^ { d }   \times   \mathbb { R } ^ { d } \mapsto \mathbb { R }$ be given. Then for K to be a valid (Mercer) kernel, it is necessary and sufficient that for any $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \} ,   ( n < \infty )$ , the corresponding kernel matrix is symmetric positive semi-definite.

Given a function K, apart from trying to find a feature mapping $\phi$ that corresponds to it, this theorem therefore gives another way of testing if it is a valid kernel. You’ll also have a chance to play with these ideas more in problem set 2.

In class, we also briefly talked about a couple of other examples of ker nels. For instance, consider the digit recognition problem, in which given an image (16x16 pixels) of a handwritten digit (0-9), we have to figure out which digit it was. Using either a simple polynomial kernel $K ( x , z ) = ( x ^ { T } z ) ^ { k }$ or the Gaussian kernel, SVMs were able to obtain extremely good perfor mance on this problem. This was particularly surprising since the input attributes x were just 256-dimensional vectors of the image pixel intensity values, and the system had no prior knowledge about vision, or even about which pixels are adjacent to which other ones. Another example that we briefly talked about in lecture was that if the objects x that we are trying to classify are strings (say, x is a list of amino acids, which strung together form a protein), then it seems hard to construct a reasonable, “small” set of features for most learning algorithms, especially if different strings have different lengths. However, consider letting $\phi ( x )$ be a feature vector that counts the number of occurrences of each length-k substring in x. If we’re considering strings of English letters, then there are $2 6 ^ { k }$ such strings. Hence, $\phi ( x )$ is a $2 6 ^ { k }$ dimensional vector; even for moderate values of $k ,$ this is probably too big for us to efficiently work with. $( \mathrm { e . g . , } ~ 2 6 ^ { 4 } \approx 4 6 0 0 0 0 . )$ However, using (dynamic programming-ish) string matching algorithms, it is possible to efficiently compute $K ( x , z ) = \phi ( x ) ^ { T } \phi ( z )$ , so that we can now implicitly work in this 26<sup>k</sup>-dimensional feature space, but without ever explicitly computing feature vectors in this space.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">d</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Many texts present Mercer’s theorem in a slightly more complicated form involving Lfunctions, but when the input attributes take values in R, the version given here is equivalent.</span></small>

<!-- page: 60 -->

Application of kernel methods: We’ve seen the application of kernels to linear regression. In the next part, we will introduce the support vector machines to which kernels can be directly applied. dwell too much longer on it here. In fact, the idea of kernels has significantly broader applicability than linear regression and SVMs. Specifically, if you have any learning algorithm that you can write in terms of only inner products $\langle x , z \rangle$ between input attribute vectors, then by replacing this with $K ( x , z )$ where K is a kernel, you can “magically” allow your algorithm to work efficiently in the high dimensional feature space corresponding to K. For instance, this kernel trick can be applied with the perceptron to derive a kernel perceptron algorithm. Many of the algorithms that we’ll see later in this class will also be amenable to this method, which has come to be known as the “kernel trick.”

<!-- page: 61 -->

## Chapter 6

## Support vector machines

This set of notes presents the Support Vector Machine (SVM) learning algorithm. SVMs are among the best (and many believe are indeed the best) “off-the-shelf” supervised learning algorithms. To tell the SVM story, we’ll need to first talk about margins and the idea of separating data with a large “gap.” Next, we’ll talk about the optimal margin classifier, which will lead us into a digression on Lagrange duality. We’ll also see kernels, which give a way to apply SVMs efficiently in very high dimensional (such as infinitedimensional) feature spaces, and finally, we’ll close off the story with the SMO algorithm, which gives an efficient implementation of SVMs.

## 6.1 Margins: intuition

We’ll start our story on SVMs by talking about margins. This section will give the intuitions about margins and about the “confidence” of our predictions; these ideas will be made formal in Section 6.3.

Consider logistic regression, where the probability $p ( y = 1 | x ; \theta )$ is modeled by $h _ { \theta } ( x )   =   g ( \theta ^ { T } x )$ We then predict $^ { \circ } 1 ^ { \prime }$ on an input x if and only if $h _ { \theta } ( x )   \geq   0 . 5$ , or equivalently, if and only if $\theta ^ { T } x   \geq   0$ . Consider a positive training example $( y = 1 )$ . The larger $\theta ^ { T }$ x is, the larger also is $h _ { \theta } ( x ) = p ( y =$ $1 | x ; \theta )$ , and thus also the higher our degree of “confidence” that the label is 1. Thus, informally we can think of our prediction as being very confident that $y = 1$ if $\theta ^ { T } x \gg 0$ . Similarly, we think of logistic regression as confidently predicting $y = 0$ , if $\theta ^ { T } x \ll 0$ . Given a training set, again informally it seems that we’d have found a good fit to the training data if we can find θ so that $\theta ^ { T } x ^ { ( i ) } \gg 0$ whenever $y ^ { ( i ) } = 1$ , and $\theta ^ { T } x ^ { ( i ) } \ll 0$ whenever $y ^ { ( i ) } = 0$ , since this would reflect a very confident (and correct) set of classifications for all the

<!-- page: 62 -->

training examples. This seems to be a nice goal to aim for, and we’ll soon formalize this idea using the notion of functional margins.

For a different type of intuition, consider the following figure, in which x’s represent positive training examples, o’s denote negative training examples, a decision boundary (this is the line given by the equation $\theta ^ { T } x   =   0 ,$ and is also called the separating hyperplane) is also shown, and three points have also been labeled A, B and C.

![](images/page_61_image_3.jpg)

Notice that the point A is very far from the decision boundary. If we are asked to make a prediction for the value of $y$ at A, it seems we should be quite confident that $y   =   1$ there. Conversely, the point C is very close to the decision boundary, and while it’s on the side of the decision boundary on which we would predict $y = 1$ , it seems likely that just a small change to the decision boundary could easily have caused out prediction to be $y = 0$ Hence, we’re much more confident about our prediction at A than at C. The point B lies in-between these two cases, and more broadly, we see that if a point is far from the separating hyperplane, then we may be significantly more confident in our predictions. Again, informally we think it would be nice if, given a training set, we manage to find a decision boundary that allows us to make all correct and confident (meaning far from the decision boundary) predictions on the training examples. We’ll formalize this later using the notion of geometric margins.

<!-- page: 63 -->

## 6.2 Notation

To make our discussion of SVMs easier, we’ll first need to introduce a new notation for talking about classification. We will be considering a linear classifier for a binary classification problem with labels $y$ and features x. From now, we’ll use $y \in \{ - 1 , 1 \}$ (instead of $\{ 0 , 1 \} )$ to denote the class labels. Also, rather than parameterizing our linear classifier with the vector $\theta ,$ we will use parameters $w , b ,$ and write our classifier as

$$
h _ {w, b} (x) = g (w ^ {T} x + b).
$$

Here, $g ( z )   =   1 \mathrm { ~ i f ~ } z   \geq   0$ , and $g ( z )   =   - 1$ otherwise. This ${ } ^ { \omega } w , b { } ^ { \prime \prime }$ notation allows us to explicitly treat the intercept term b separately from the other parameters. (We also drop the convention we had previously of letting $x _ { 0 } = 1$ be an extra coordinate in the input feature vector.) Thus, b takes the role of what was previously $\theta _ { 0 }$ , and $w$ takes the role of $[ \theta _ { 1 } \dots \theta _ { d } ] ^ { T }$

Note also that, from our definition of $g$ above, our classifier will directly predict either 1 or −1 (cf. the perceptron algorithm), without first going through the intermediate step of estimating $p ( y = 1 )$ (which is what logistic regression does).

## 6.3 Functional and geometric margins

Let’s formalize the notions of the functional and geometric margins. Given a training example $( x ^ { ( i ) } , y ^ { ( i ) } )$ , we define the functional margin of $( w , b )$ with respect to the training example as

$$
\hat {\gamma} ^ {(i)} = y ^ {(i)} (w ^ {T} x ^ {(i)} + b).
$$

Note that if $y ^ { ( i ) }   =   1$ , then for the functional margin to be large $\mathrm { ( i . e . , }$ for our prediction to be confident and correct), we need $w ^ { T } x ^ { ( i ) } + b$ to be a large positive number. Conversely, if $y ^ { ( i ) }   =   - \dot { 1 }$ , then for the functional margin to be large, we need $w ^ { T } x ^ { ( i ) } + b$ to be a large negative number. Moreover, if $y ^ { ( i ) } ( w ^ { T } x ^ { ( i ) } + b ) > 0$ , then our prediction on this example is correct. (Check this yourself.) Hence, a large functional margin represents a confident and a correct prediction.

For a linear classifier with the choice of $g$ given above (taking values in $\{ - 1 , 1 \} )$ , there’s one property of the functional margin that makes it not a very good measure of confidence, however. Given our choice of g, we note that if we replace w with 2w and b with 2b, then since $g ( w ^ { T } x   +   b ) = g ( 2 w ^ { T } x   +   2 b )$

<!-- page: 64 -->

this would not change $h _ { w , b } ( x )$ at all. I.e., g, and hence also $h _ { w , b } ( x )$ , depends only on the sign, but not on the magnitude, of $w ^ { T } x + b$ . However, replacing $( w , b )$ with (2w, 2b) also results in multiplying our functional margin by a factor of 2. Thus, it seems that by exploiting our freedom to scale w and b, we can make the functional margin arbitrarily large without really changing anything meaningful. Intuitively, it might therefore make sense to impose some sort of normalization condition such as that $| | w | | _ { 2 } = 1 ; \mathrm { i . e . }$ , we might replace $( w , b )$ with $( w / | | w | | _ { 2 } , b / | | w | | _ { 2 } )$ , and instead consider the functional margin of $( w / | | w | | _ { 2 } , b / | | w | | _ { 2 } )$ . We’ll come back to this later.

Given a training set $S   =   \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) ; i   =   1 , \ldots , n \}$ , we also define the function margin of $( w , b )$ with respect to S as the smallest of the functional margins of the individual training examples. Denoted by $\hat { \gamma }$ , this can therefore be written:

$$
\hat {\gamma} = \min _ {i = 1, \dots , n} \hat {\gamma} ^ {(i)}.
$$

Next, let’s talk about geometric margins. Consider the picture below:

![](images/page_63_image_5.jpg)

The decision boundary corresponding to $( w , b )$ is shown, along with the vector w. Note that w is orthogonal (at 90◦) to the separating hyperplane. (You should convince yourself that this must be the case.) Consider the point at A, which represents the input $x ^ { ( i ) }$ of some training example with label $y ^ { ( i ) } = 1$ . Its distance to the decision boundary, $\gamma ^ { ( i ) }$ , is given by the line segment AB.

How can we find the value of $\gamma ^ { ( i ) } { } _ { \bullet } ^ { ? }$ Well, $w / | | w | |$ is a unit-length vector pointing in the same direction as w. Since A represents $x ^ { ( i ) }$ , we therefore

<!-- page: 65 -->

find that the point B is given by $x ^ { ( i ) } - \gamma ^ { ( i ) } \cdot w / | | w | |$ . But this point lies on the decision boundary, and all points x on the decision boundary satisfy the equation $w ^ { T } x + b = 0$ . Hence,

$$
w ^ {T} \left(x ^ {(i)} - \gamma^ {(i)} \frac {w}{| | w | |}\right) + b = 0.
$$

Solving for $\gamma ^ { ( i ) }$ yields

$$
\gamma^ {(i)} = \frac {w ^ {T} x ^ {(i)} + b}{| | w | |} = \left(\frac {w}{| | w | |}\right) ^ {T} x ^ {(i)} + \frac {b}{| | w | |}.
$$

This was worked out for the case of a positive training example at A in the figure, where being on the “positive” side of the decision boundary is good. More generally, we define the geometric margin of $( w , b )$ with respect to a training example $( x ^ { ( i ) } , y ^ { ( i ) } )$ to be

$$
\gamma^ {(i)} = y ^ {(i)} \left(\left(\frac {w}{| | w | |}\right) ^ {T} x ^ {(i)} + \frac {b}{| | w | |}\right).
$$

Note that if $| | w | | = 1$ , then the functional margin equals the geometric margin—this thus gives us a way of relating these two different notions of margin. Also, the geometric margin is invariant to rescaling of the parameters; i.e., if we replace w with 2w and b with 2b, then the geometric margin does not change. This will in fact come in handy later. Specifically, because of this invariance to the scaling of the parameters, when trying to fit w and b to training data, we can impose an arbitrary scaling constraint on w without changing anything important; for instance, we can demand that $| | w | | = 1$ , or $| w _ { 1 } | = 5 , \mathrm { o r } | w _ { 1 } + b | + | w _ { 2 } | = 2$ , and any of these can be satisfied simply by rescaling w and b.

Finally, given a training set $S = \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) ; i = 1 , \ldots , n \}$ , we also define the geometric margin of $( w , b )$ with respect to S to be the smallest of the geometric margins on the individual training examples:

$$
\gamma = \min _ {i = 1, \dots , n} \gamma^ {(i)}.
$$

## 6.4 The optimal margin classifier

Given a training set, it seems from our previous discussion that a natural desideratum is to try to find a decision boundary that maximizes the (geometric) margin, since this would reflect a very confident set of predictions

<!-- page: 66 -->

on the training set and a good $`` \mathrm{fit} ''$ to the training data. Specifically, this will result in a classifier that separates the positive and the negative training examples with a “gap” (geometric margin).

For now, we will assume that we are given a training set that is linearly separable; i.e., that it is possible to separate the positive and negative examples using some separating hyperplane. How will we find the one that achieves the maximum geometric margin? We can pose the following optimization problem:

$$
\begin{array}{l l} \max _ {\gamma , w, b} & \gamma \\ \text {s.t.} & y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq \gamma , i = 1, \ldots , n \\ & | | w | | = 1. \end{array}
$$

$\operatorname { I . e . }$ , we want to maximize $\gamma ,$ subject to each training example having functional margin at least $\gamma .$ . The $| | w | | = 1$ constraint moreover ensures that the functional margin equals to the geometric margin, so we are also guaranteed that all the geometric margins are at least γ. Thus, solving this problem will result in $( w , b )$ with the largest possible geometric margin with respect to the training set.

If we could solve the optimization problem above, we’d be done. But the $`` || w || = 1  ''$ constraint is a nasty (non-convex) one, and this problem certainly isn’t in any format that we can plug into standard optimization software to solve. $\mathrm { S o }$ , let’s try transforming the problem into a nicer one. Consider:

$$
\begin{array}{r l} \max _ {\hat {\gamma}, w, b} & \frac {\hat {\gamma}}{| | w | |} \\ \mathrm{s.t.} & y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq \hat {\gamma}, i = 1, \dots , n \end{array}
$$

Here, we’re going to maximize $\hat { \gamma } / | | w | |$ , subject to the functional margins all being at least $\hat { \gamma } .$ Since the geometric and functional margins are related by $\gamma = \hat { \gamma } / | | w | |$ , this will give us the answer we want. Moreover, we’ve gotten rid of the constraint $| | w | | = 1$ that we didn’t like. The downside is that we now have a nasty (again, non-convex) objective $\big | \frac { \hat { \gamma } } { | | w | | }$ function; and, we still don’t have any off-the-shelf software that can solve this form of an optimization problem.

Let’s keep going. Recall our earlier discussion that we can add an arbitrary scaling constraint on w and b without changing anything. This is the key idea we’ll use now. We will introduce the scaling constraint that the functional margin of w, b with respect to the training set must be 1:

$$
\hat {\gamma} = 1.
$$

<!-- page: 67 -->

Since multiplying w and b by some constant results in the functional margin being multiplied by that same constant, this is indeed a scaling constraint, and can be satisfied by rescaling $w , b$ . Plugging this into our problem above, and noting that maximizing $\hat { \gamma } / | | w | | = 1 / | | w | |$ is the same thing as minimizing $\| w \| ^ { 2 }$ , we now have the following optimization problem:

$$
\begin{array}{r l} \min _ {w, b} & \frac {1}{2} | | w | | ^ {2} \\ \mathrm{s.t.} & y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq 1, i = 1, \dots , n \end{array}
$$

We’ve now transformed the problem into a form that can be efficiently solved. The above is an optimization problem with a convex quadratic objective and only linear constraints. Its solution gives us the optimal margin classifier. This optimization problem can be solved using commercial quadratic programming (QP) code.<sup>1</sup>

While we could call the problem solved here, what we will instead do is make a digression to talk about Lagrange duality. This will lead us to our optimization problem’s dual form, which will play a key role in allowing us to use kernels to get optimal margin classifiers to work efficiently in very high dimensional spaces. The dual form will also allow us to derive an efficient algorithm for solving the above optimization problem that will typically do much better than generic QP software.

## 6.5 Lagrange duality

Let’s temporarily put aside SVMs and maximum margin classifiers, and talk about solving constrained optimization problems.

Consider a problem of the following form:

$$
\begin{array}{l l} \min _ {w} & f (w) \\ \text {s.t.} & h _ {i} (w) = 0, i = 1, \ldots , l. \end{array}
$$

Some of you may recall how the method of Lagrange multipliers can be used to solve it. (Don’t worry if you haven’t seen it before.) In this method, we define the Lagrangian to be

$$
\mathcal {L} (w, \beta) = f (w) + \sum_ {i = 1} ^ {l} \beta_ {i} h _ {i} (w)
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Q</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>You may be familiar with linear programming, which solves optimization problems that have linear objectives and linear constraints. P software is also widely available, which allows convex quadratic objectives and linear constraints.</span></small>

<!-- page: 68 -->

Here, the $\beta _ { i } \mathrm { { ^ \prime } s }$ are called the Lagrange multipliers. We would then find and set ${ \mathcal { L } } ^ { \prime } \mathrm { s }$ partial derivatives to zero:

$$
\frac {\partial \mathcal {L}}{\partial w _ {i}} = 0; \frac {\partial \mathcal {L}}{\partial \beta_ {i}} = 0,
$$

and solve for $w$ and $\beta .$

In this section, we will generalize this to constrained optimization problems in which we may have inequality as well as equality constraints. Due to time constraints, we won’t really be able to do the theory of Lagrange duality justice in this class,<sup>2</sup> but we will give the main ideas and results, which we will then apply to our optimal margin classifier’s optimization problem.

Consider the following, which we’ll call the primal optimization problem:

$$
\begin{array}{r l} \min _ {w} & f (w) \\ \text {s.t.} & g _ {i} (w) \leq 0, i = 1, \ldots , k \\ & h _ {i} (w) = 0, i = 1, \ldots , l. \end{array}
$$

To solve it, we start by defining the generalized Lagrangian

$$
\mathcal {L} (w, \alpha , \beta) = f (w) + \sum_ {i = 1} ^ {k} \alpha_ {i} g _ {i} (w) + \sum_ {i = 1} ^ {l} \beta_ {i} h _ {i} (w).
$$

Here, the $\alpha _ { i } \mathrm { { } ^ { \prime } s }$ and $\beta _ { i } \mathrm { { ^ \prime } s }$ are the Lagrange multipliers. Consider the quantity

$$
\theta_ {\mathcal {P}} (w) = \max _ {\alpha , \beta : \alpha_ {i} \geq 0} \mathcal {L} (w, \alpha , \beta).
$$

Here, the ${ } ^ { \langle } \mathcal { P } ^ { \rangle }$ subscript stands for “primal.” Let some w be given. If w violates any of the primal constraints (i.e., if either $g _ { i } ( w ) > 0$ or $h _ { i } ( w ) \neq 0$ for some i), then you should be able to verify that

$$
\begin{array}{r c l} \theta_ {\mathcal {P}} (w) & = & \max _ {\alpha , \beta : \alpha_ {i} \geq 0} f (w) + \sum_ {i = 1} ^ {k} \alpha_ {i} g _ {i} (w) + \sum_ {i = 1} ^ {l} \beta_ {i} h _ {i} (w) \\ & = & \infty . \end{array}\tag{6.1}
$$

(6.2)

Conversely, if the constraints are indeed satisfied for a particular value of $w ,$ then $\theta _ { \mathcal { P } } ( w ) = f ( w )$ . Hence,

$$
\theta_ {\mathcal {P}} (w) = \left\{ \begin{array}{l l} f (w) & \text {if w satisfies primal constraints} \\ \infty & \text {otherwise.} \end{array} \right.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Readers interested in learning more about this topic are encouraged to read, e.g., R. T. Rockarfeller (1970), Convex Analysis, Princeton University Press.</span></small>

<!-- page: 69 -->

Thus, $\theta _ { \mathcal { P } }$ takes the same value as the objective in our problem for all values of w that satisfies the primal constraints, and is positive infinity if the constraints are violated. Hence, if we consider the minimization problem

$$
\min _ {w} \theta_ {\mathcal {P}} (w) = \min _ {w} \max _ {\alpha , \beta : \alpha_ {i} \geq 0} \mathcal {L} (w, \alpha , \beta),
$$

we see that it is the same problem $\left( \mathrm { i . e . } , \right.$ and has the same solutions $\mathrm { a s } )$ our original, primal problem. For later use, we also define the optimal value of the objective to be $\quad p ^ { {  } * } {  } = {  } \operatorname { m i n } _ { {  } w } {  } \theta _ { {  } \mathcal { P } } {  } ( {  } w {  } )$ ; we call this the value of the primal problem.

Now, let’s look at a slightly different problem. We define

$$
\theta_ {\mathcal {D}} (\alpha , \beta) = \min _ {w} \mathcal {L} (w, \alpha , \beta).
$$

Here, the ${ } ^ { \langle } \mathcal { D } ^ { \rangle }$ subscript stands for “dual.” Note also that whereas in the definition of $\theta _ { \mathcal { P } }$ we were optimizing (maximizing) with respect to $\alpha , \beta ,$ , here we are minimizing with respect to w.

We can now pose the dual optimization problem:

$$
\max _ {\alpha , \beta : \alpha_ {i} \geq 0} \theta_ {\mathcal {D}} (\alpha , \beta) = \max _ {\alpha , \beta : \alpha_ {i} \geq 0} \min _ {w} \mathcal {L} (w, \alpha , \beta).
$$

This is exactly the same as our primal problem shown above, except that the order of the “max” and the “min” are now exchanged. We also define the optimal value of the dual problem’s objective to be $\begin{array} { r } { d ^ { * } = \operatorname* { m a x } _ { \alpha , \beta \colon \alpha _ { i } \geq 0 } \theta _ { \mathcal { D } } ( \alpha , \beta ) } \end{array}$

How are the primal and the dual problems related? It can easily be shown that

$$
d ^ {*} = \max _ {\alpha , \beta : \alpha_ {i} \geq 0} \min _ {w} \mathcal {L} (w, \alpha , \beta) \leq \min _ {w} \max _ {\alpha , \beta : \alpha_ {i} \geq 0} \mathcal {L} (w, \alpha , \beta) = p ^ {*}
$$

(You should convince yourself of this; this follows from the “max min” of a function always being less than or equal to the “min max.”) However, under certain conditions, we will have

$$
d ^ {*} = p ^ {*},
$$

so that we can solve the dual problem in lieu of the primal problem. Let’s see what these conditions are.

Suppose f and the $g _ { i } \mathrm { ^ { \prime } s }$ are convex,<sup>3</sup> and the $h _ { i } { } ^ { \prime } \mathrm { s }$ are affine.<sup>4</sup> Suppose further that the constraints $g _ { i }$ are (strictly) feasible; this means that there exists some w so that $g _ { i } ( w ) < 0$ for all i.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f(w) = wT n</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">A</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">f</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>When f has a Hessian, then it is convex if and only if the Hessian is positive semi-definite. For instance, f(w) = w w is convex; similarly, all linear (and affine) functions are also convex. ( function f can also be convex without being differentiable, but we won’t need those more general definitions of convexity here.)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">I.e.,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ai, i,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">i.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">i(w) = ai w + i.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4 there exists  b so that h T b “Affine” means the same thing as linear, except that we also allow the extra intercept term b</span></small>

<!-- page: 70 -->

Under our above assumptions, there must exist $w ^ { * } , \alpha ^ { * } , \beta ^ { * }$ so that $w ^ { * }$ is the solution to the primal problem, $\alpha ^ { * } , \beta ^ { * }$ are the solution to the dual problem, and moreover $p ^ { * } = d ^ { * } = \mathcal { L } ( w ^ { * } , \alpha ^ { * } , \beta ^ { * } )$ . Moreover, $w ^ { * } , \alpha ^ { * }$ and $\beta ^ { * }$ satisfy the Karush-Kuhn-Tucker (KKT) conditions, which are as follows:

$$
\frac {\partial}{\partial w _ {i}} \mathcal {L} (w ^ {*}, \alpha^ {*}, \beta^ {*}) = 0, i = 1, \dots , d\tag{6.3}
$$

$$
\frac {\partial}{\partial \beta_ {i}} \mathcal {L} (w ^ {*}, \alpha^ {*}, \beta^ {*}) = 0, i = 1, \dots , l\tag{6.4}
$$

$$
\alpha_ {i} ^ {*} g _ {i} (w ^ {*}) = 0, i = 1, \dots , k\tag{6.5}
$$

$$
g _ {i} (w ^ {*}) \leq 0, i = 1, \dots , k\tag{6.6}
$$

$$
\alpha_ {i} ^ {*} \geq 0, i = 1, \dots , k\tag{6.7}
$$

Moreover, if some $w ^ { * } , \alpha ^ { * } , \beta ^ { * }$ satisfy the KKT conditions, then $w ^ { * }$ is a solution to the primal problem and $\alpha ^ { * } , \beta ^ { * }$ are solutions to the dual problem.

We draw attention to Equation (6.5), which is called the KKT dual complementarity condition. Specifically, it implies that if $\alpha _ { i } ^ { * }   >   0$ , then $g _ { i } ( w ^ { * } ) = 0$ . (I.e., the $\text{" } g_{i}(w) \leq 0  \text{" }$ constraint is active, meaning it holds with equality rather than with inequality.) Later on, this will be key for showing that the SVM has only a small number of “support vectors”; the KKT dual complementarity condition will also give us our convergence test when we talk about the SMO algorithm.

## 6.6 Optimal margin classifiers: the dual form

Note: The equivalence of optimization problem (6.8) and the optimization problem (6.12), and the relationship between the primary and dual variables in equation (6.10) are the most important take home messages of this section.

Previously, we posed the following (primal) optimization problem for finding the optimal margin classifier:

$$
\begin{array}{r l} \min _ {w, b} & \frac {1}{2} | | w | | ^ {2} \\ \text {s.t.} & y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq 1, i = 1, \ldots , n \end{array}\tag{6.8}
$$

We can write the constraints as

$$
g _ {i} (w) = - y ^ {(i)} (w ^ {T} x ^ {(i)} + b) + 1 \leq 0.
$$

<!-- page: 71 -->

We have one such constraint for each training example. Note that from the KKT dual complementarity condition, we will have $\alpha _ { i } > 0$ only for the training examples that have functional margin exactly equal to one (i.e., the ones corresponding to constraints that hold with equality, $g _ { i } ( w ) = 0 )$ . Consider the figure below, in which a maximum margin separating hyperplane is shown by the solid line.

![](images/page_70_image_2.jpg)

The points with the smallest margins are exactly the ones closest to the decision boundary; here, these are the three points (one negative and two positive examples) that lie on the dashed lines parallel to the decision boundary. Thus, only three of the $\alpha_{i}  's — namely$ , the ones corresponding to these three training examples—will be non-zero at the optimal solution to our optimization problem. These three points are called the support vectors in this problem. The fact that the number of support vectors can be much smaller than the size the training set will be useful later.

Let’s move on. Looking ahead, as we develop the dual form of the problem, one key idea to watch out for is that we’ll try to write our algorithm in terms of only the inner product $\langle x ^ { ( i ) } , x ^ { ( j ) } \rangle$ (think of this as $( \bar { x ^ { ( i ) } } ) ^ { T } x ^ { ( j ) } )$ between points in the input feature space. The fact that we can express our algorithm in terms of these inner products will be key when we apply the kernel trick.

When we construct the Lagrangian for our optimization problem we have:

$$
\mathcal {L} (w, b, \alpha) = \frac {1}{2} | | w | | ^ {2} - \sum_ {i = 1} ^ {n} \alpha_ {i} \left[ y ^ {(i)} (w ^ {T} x ^ {(i)} + b) - 1 \right].\tag{6.9}
$$

Note that there’re only $\text{" } \alpha_{i} \text{" }$ but no ${ { } ^ { \backprime } \beta _ { i } } ^ { \backprime \prime }$ Lagrange multipliers, since the problem has only inequality constraints.

<!-- page: 72 -->

Let’s find the dual form of the problem. To do so, we need to first minimize $\mathcal { L } ( w , b , \alpha )$ with respect to w and $b$ (for fixed α), to get $\theta _ { \mathcal { D } }$ , which we’ll do by setting the derivatives of $\mathcal { L }$ with respect to w and b to zero. We have:

$$
\nabla_ {w} \mathcal {L} (w, b, \alpha) = w - \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} x ^ {(i)} = 0
$$

This implies that

$$
w = \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} x ^ {(i)}.\tag{6.10}
$$

As for the derivative with respect to $b ,$ we obtain

$$
\frac {\partial}{\partial b} \mathcal {L} (w, b, \alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} = 0.\tag{6.11}
$$

If we take the definition of w in Equation (6.10) and plug that back into the Lagrangian (Equation 6.9), and simplify, we get

$$
\mathcal {L} (w, b, \alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {n} y ^ {(i)} y ^ {(j)} \alpha_ {i} \alpha_ {j} (x ^ {(i)}) ^ {T} x ^ {(j)} - b \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)}.
$$

But from Equation (6.11), the last term must be zero, so we obtain

$$
\mathcal {L} (w, b, \alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {n} y ^ {(i)} y ^ {(j)} \alpha_ {i} \alpha_ {j} (x ^ {(i)}) ^ {T} x ^ {(j)}.
$$

Recall that we got to the equation above by minimizing L with respect to w and b. Putting this together with the constraints $\alpha _ { i } \geq 0$ (that we always had) and the constraint (6.11), we obtain the following dual optimization problem:

$$
\begin{array}{l l} \max _ {\alpha} & W (\alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {n} y ^ {(i)} y ^ {(j)} \alpha_ {i} \alpha_ {j} \langle x ^ {(i)}, x ^ {(j)} \rangle . \\ \text {s.t.} & \alpha_ {i} \geq 0, i = 1, \ldots , n \\ & \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} = 0, \end{array}\tag{6.12}
$$

You should also be able to verify that the conditions required for $p ^ { * } = d ^ { * }$ and the KKT conditions (Equations 6.3–6.7) to hold are indeed satisfied in

<!-- page: 73 -->

our optimization problem. Hence, we can solve the dual in lieu of solving the primal problem. Specifically, in the dual problem above, we have a maximization problem in which the parameters are the $\alpha _ { i } \mathrm { ^ { \prime } S } .$ . We’ll talk later about the specific algorithm that we’re going to use to solve the dual problem, but if we are indeed able to solve it (i.e., find the $\alpha ^ { \prime } \mathrm { s }$ that maximize $W ( \alpha )$ subject to the constraints), then we can use Equation (6.10) to $\mathtt { g O }$ back and find the optimal w’s as a function of the α’s. Having found $w ^ { * }$ , by considering the primal problem, it is also straightforward to find the optimal value for the intercept term b as

$$
b ^ {*} = - \frac {\max _ {i : y ^ {(i)} = - 1} w ^ {* T} x ^ {(i)} + \min _ {i : y ^ {(i)} = 1} w ^ {* T} x ^ {(i)}}{2}.\tag{6.13}
$$

(Check for yourself that this is correct.)

Before moving on, let’s also take a more careful look at Equation (6.10), which gives the optimal value of w in terms of (the optimal value of) α. Suppose we’ve fit our model’s parameters to a training set, and now wish to make a prediction at a new point input x. We would then calculate $w ^ { T } x + b ,$ and predict $y \; = \; 1$ if and only if this quantity is bigger than zero. But using (6.10), this quantity can also be written:

$$
w ^ {T} x + b = \left(\sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} x ^ {(i)}\right) ^ {T} x + b\tag{6.14}
$$

$$
= \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} \langle x ^ {(i)}, x \rangle + b.\tag{6.15}
$$

Hence, if we’ve found the ${ \alpha _ { i } } ^ { \prime } \mathrm { S } .$ in order to make a prediction, we have to calculate a quantity that depends only on the inner product between x and the points in the training set. Moreover, we saw earlier that the ${ \alpha _ { i } } ^ { \prime } \mathrm { { S } }$ will all be zero except for the support vectors. Thus, many of the terms in the sum above will be zero, and we really need to find only the inner products between x and the support vectors (of which there is often only a small number) in order calculate (6.15) and make our prediction.

By examining the dual form of the optimization problem, we gained significant insight into the structure of the problem, and were also able to write the entire algorithm in terms of only inner products between input feature vectors. In the next section, we will exploit this property to apply the kernels to our classification problem. The resulting algorithm, support vector machines, will be able to efficiently learn in very high dimensional spaces.

<!-- page: 74 -->

## 6.7 Regularization and the non-separable case

The derivation of the SVM as presented so far assumed that the data is linearly separable. While mapping data to a high dimensional feature space via φ does generally increase the likelihood that the data is separable, we can’t guarantee that it always will be so. Also, in some cases it is not clear that finding a separating hyperplane is exactly what we’d want to do, since that might be susceptible to outliers. For instance, the left figure below shows an optimal margin classifier, and when a single outlier is added in the upper-left region (right figure), it causes the decision boundary to make a dramatic swing, and the resulting classifier has a much smaller margin.

![](images/page_73_image_3.jpg)

![](images/page_73_image_4.jpg)

To make the algorithm work for non-linearly separable datasets as well as be less sensitive to outliers, we reformulate our optimization (using $\ell _ { 1 }$ regularization) as follows:

$$
\begin{array}{l l} \min _ {\gamma , w, b} & \frac {1}{2} | | w | | ^ {2} + C \sum_ {i = 1} ^ {n} \xi_ {i} \\ \text {s.t.} & y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq 1 - \xi_ {i}, i = 1, \ldots , n \\ & \xi_ {i} \geq 0, i = 1, \ldots , n. \end{array}
$$

Thus, examples are now permitted to have (functional) margin less than 1, and if an example has functional margin $1 - \xi _ { i }   \left( \mathrm { w i t h } \xi > 0 \right)$ , we would pay a cost of the objective function being increased by $C \xi _ { i }$ . The parameter C controls the relative weighting between the twin goals of making the $| | w | | ^ { 2 }$ small (which we saw earlier makes the margin large) and of ensuring that most examples have functional margin at least 1.

As before, we can form the Lagrangian:

$$
\mathcal {L} (w, b, \xi , \alpha , r) = \frac {1}{2} w ^ {T} w + C \sum_ {i = 1} ^ {n} \xi_ {i} - \sum_ {i = 1} ^ {n} \alpha_ {i} \left[ y ^ {(i)} (x ^ {T} w + b) - 1 + \xi_ {i} \right] - \sum_ {i = 1} ^ {n} r _ {i} \xi_ {i}.
$$

<!-- page: 75 -->

Here, the $\alpha _ { i }$ ’s and $r _ { i }$ ’s are our Lagrange multipliers (constrained to be $\geq 0 )$ We won’t go through the derivation of the dual again in detail, but after setting the derivatives with respect to w and b to zero as before, substituting them back in, and simplifying, we obtain the following dual form of the problem:

$$
\begin{array}{l l} \max _ {\alpha} & W (\alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {n} y ^ {(i)} y ^ {(j)} \alpha_ {i} \alpha_ {j} \langle x ^ {(i)}, x ^ {(j)} \rangle \\ \text {s.t.} & 0 \leq \alpha_ {i} \leq C, i = 1, \ldots , n \\ & \sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} = 0, \end{array}
$$

As before, we also have that w can be expressed in terms of the $\alpha _ { i } \mathrm { { } ^ { \prime } s }$ as given in Equation (6.10), so that after solving the dual problem, we can continue to use Equation (6.15) to make our predictions. Note that, somewhat surprisingly, in adding $\ell _ { 1 }$ regularization, the only change to the dual problem is that what was originally a constraint that $0   \leq   \alpha _ { i }$ has now become $0 \leq \alpha _ { i } \leq C$ . The calculation for $b ^ { * }$ also has to be modified (Equation 6.13 is no longer valid); see the comments in the next section/Platt’s paper.

Also, the KKT dual-complementarity conditions (which in the next section will be useful for testing for the convergence of the SMO algorithm) are:

$$
\alpha_ {i} = 0 \Rightarrow y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \geq 1\tag{6.16}
$$

$$
\alpha_ {i} = C \Rightarrow y ^ {(i)} (w ^ {T} x ^ {(i)} + b) \leq 1\tag{6.17}
$$

$$
0 <   \alpha_ {i} <   C \Rightarrow y ^ {(i)} (w ^ {T} x ^ {(i)} + b) = 1.\tag{6.18}
$$

Now, all that remains is to give an algorithm for actually solving the dual problem, which we will do in the next section.

## 6.8 The SMO algorithm

The SMO (sequential minimal optimization) algorithm, due to John Platt, gives an efficient way of solving the dual problem arising from the derivation of the SVM. Partly to motivate the SMO algorithm, and partly because it’s interesting in its own right, let’s first take another digression to talk about the coordinate ascent algorithm.

<!-- page: 76 -->

## 6.8.1 Coordinate ascent

Consider trying to solve the unconstrained optimization problem

$$
\max _ {\alpha} W (\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}).
$$

Here, we think of $W$ as just some function of the parameters $\alpha _ { i } { } ^ { \prime } \mathrm { S } _ { i }$ and for now ignore any relationship between this problem and SVMs. We’ve already seen two optimization algorithms, gradient ascent and Newton’s method. The new algorithm we’re going to consider here is called coordinate ascent:

Loop until convergence: {

$$
\begin{array}{l} \text {For} i = 1, \ldots , n, \{\quad \\ \alpha_ {i} := \arg \max _ {\hat {\alpha} _ {i}} W (\alpha_ {1}, \ldots , \alpha_ {i - 1}, \hat {\alpha} _ {i}, \alpha_ {i + 1}, \ldots , \alpha_ {n}). \\ \} \\ \} \end{array}
$$

Thus, in the innermost loop of this algorithm, we will hold all the variables except for some $\alpha _ { i }$ fixed, and reoptimize W with respect to just the parameter $\alpha _ { i }$ . In the version of this method presented here, the inner-loop reoptimizes the variables in order $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } , \alpha _ { 1 } , \alpha _ { 2 } , \ldots .$ (A more sophisticated version might choose other orderings; for instance, we may choose the next variable to update according to which one we expect to allow us to make the largest increase in $W ( \alpha ) .$

When the function W happens to be of such a form that the “arg max” in the inner loop can be performed efficiently, then coordinate ascent can be a fairly efficient algorithm. Here’s a picture of coordinate ascent in action:

![](images/page_75_chart_9.jpg)

<!-- page: 77 -->

The ellipses in the figure are the contours of a quadratic function that we want to optimize. Coordinate ascent was initialized at $( 2 , - 2 )$ , and also plotted in the figure is the path that it took on its way to the global maximum. Notice that on each step, coordinate ascent takes a step that’s parallel to one of the axes, since only one variable is being optimized at a time.

## 6.8.2 SMO

We close off the discussion of SVMs by sketching the derivation of the SMO algorithm.

Here’s the (dual) optimization problem that we want to solve:

$$
\max _ {\alpha} W (\alpha) = \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i, j = 1} ^ {n} y ^ {(i)} y ^ {(j)} \alpha_ {i} \alpha_ {j} \langle x ^ {(i)}, x ^ {(j)} \rangle .\tag{6.19}
$$

$$
\mathrm{s.t.} \quad 0 \leq \alpha_ {i} \leq C, i = 1, \dots , n\tag{6.20}
$$

$$
\sum_ {i = 1} ^ {n} \alpha_ {i} y ^ {(i)} = 0.\tag{6.21}
$$

Let’s say we have set of $\alpha _ { i } \mathrm { { } ^ { \prime } s }$ that satisfy the constraints (6.20-6.21). Now, suppose we want to hold $\alpha _ { 2 } , \ldots , \alpha _ { n }$ fixed, and take a coordinate ascent step and reoptimize the objective with respect to $\alpha _ { 1 }$ . Can we make any progress? The answer is no, because the constraint (6.21) ensures that

$$
\alpha_ {1} y ^ {(1)} = - \sum_ {i = 2} ^ {n} \alpha_ {i} y ^ {(i)}.
$$

Or, by multiplying both sides by $y ^ { ( 1 ) }$ , we equivalently have

$$
\alpha_ {1} = - y ^ {(1)} \sum_ {i = 2} ^ {n} \alpha_ {i} y ^ {(i)}.
$$

(This step used the fact that $y ^ { ( 1 ) } \in \{ - 1 , 1 \}$ , and hence $( y ^ { ( 1 ) } ) ^ { 2 } = 1 . )$ Hence, $\alpha _ { 1 }$ is exactly determined by the other $\alpha _ { i } \mathrm { { } ^ { \flat } S } ,$ and if we were to hold $\alpha _ { 2 } , \ldots , \alpha _ { n }$ fixed, then we can’t make any change to $\alpha _ { 1 }$ without violating the constraint (6.21) in the optimization problem.

Thus, if we want to update some subject of the $\alpha _ { i } \mathrm { { } ^ { \prime } s }$ , we must update at least two of them simultaneously in order to keep satisfying the constraints. This motivates the SMO algorithm, which simply does the following:

<!-- page: 78 -->

1. Select some pair $\alpha _ { i }$ and $\alpha _ { j }$ to update next (using a heuristic that tries to pick the two that will allow us to make the biggest progress towards the global maximum).

2. Reoptimize $W ( \alpha )$ with respect to $\alpha _ { i }$ and $\alpha _ { j }$ , while holding all the other $\alpha _ { k } \mathrm { ~ ' s ~ } ( k \neq i , j )$ fixed.

To test for convergence of this algorithm, we can check whether the KKT conditions (Equations 6.16-6.18) are satisfied to within some $t o l .$ Here, tol is the convergence tolerance parameter, and is typically set to around 0.01 to 0.001. (See the paper and pseudocode for details.)

The key reason that SMO is an efficient algorithm is that the update to $\alpha _ { i } , \; \alpha _ { j }$ can be computed very efficiently. Let’s now briefly sketch the main ideas for deriving the efficient update.

Let’s say we currently have some setting of the $\alpha _ { i } \mathrm { { } ^ { \prime } s }$ that satisfy the constraints (6.20-6.21), and suppose we’ve decided to hold $\alpha _ { 3 } , \ldots , \alpha _ { n }$ fixed, and want to reoptimize $W ( \alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } )$ with respect to $\alpha _ { 1 }$ and $\alpha _ { 2 }$ (subject to the constraints). From (6.21), we require that

$$
\alpha_ {1} y ^ {(1)} + \alpha_ {2} y ^ {(2)} = - \sum_ {i = 3} ^ {n} \alpha_ {i} y ^ {(i)}.
$$

Since the right hand side is fixed (as we’ve fixed $\alpha _ { 3 } , \ldots \alpha _ { n } )$ , we can just let it be denoted by some constant $\zeta ;$

$$
\alpha_ {1} y ^ {(1)} + \alpha_ {2} y ^ {(2)} = \zeta .\tag{6.22}
$$

We can thus picture the constraints on $\alpha _ { 1 }$ and $\alpha _ { 2 }$ as follows:

![](images/page_77_chart_10.jpg)

<!-- page: 79 -->

From the constraints (6.20), we know that $\alpha _ { 1 }$ and $\alpha _ { 2 }$ must lie within the box $[ 0 , C ] \times [ 0 , C ]$ shown. Also plotted is the line $\alpha _ { 1 } y ^ { ( 1 ) }   +   \alpha _ { 2 } y ^ { ( 2 ) } = \zeta$ , on which we know $\alpha _ { 1 }$ and $\alpha _ { 2 }$ must lie. Note also that, from these constraints, we know $L   \leq   \alpha _ { 2 }   \leq   H$ ; otherwise, $( \alpha _ { 1 } , \alpha _ { 2 } )$ can’t simultaneously satisfy both the box and the straight line constraint. In this example, $L = 0$ . But depending on what the line $\alpha _ { 1 } y ^ { ( 1 ) } + \alpha _ { 2 } y ^ { ( 2 ) } = \zeta$ looks like, this won’t always necessarily be the case; but more generally, there will be some lower-bound L and some upper-bound H on the permissible values for $\alpha _ { 2 }$ that will ensure that $\alpha _ { 1 }$ , α<sub>2</sub> lie within the box $[ 0 , C ] \times [ 0 , C ]$

Using Equation (6.22), we can also write $\alpha _ { 1 }$ as a function of $\alpha _ { 2 }$ :

$$
\alpha_ {1} = (\zeta - \alpha_ {2} y ^ {(2)}) y ^ {(1)}.
$$

(Check this derivation yourself; we again used the fact that $y ^ { ( 1 ) } \in \{ - 1 , 1 \}$ so that $( y ^ { ( 1 ) } ) ^ { 2 } = 1 . )$ Hence, the objective $W ( \alpha )$ can be written

$$
W (\alpha_ {1}, \alpha_ {2}, \dots , \alpha_ {n}) = W ((\zeta - \alpha_ {2} y ^ {(2)}) y ^ {(1)}, \alpha_ {2}, \dots , \alpha_ {n}).
$$

Treating $\alpha _ { 3 } , \ldots , \alpha _ { n }$ as constants, you should be able to verify that this is just some quadratic function in $\alpha _ { 2 }$ . I.e., this can also be expressed in the form $a \alpha _ { 2 } ^ { 2 } + b \alpha _ { 2 } + c$ for some appropriate $a ,   b ,$ and c. If we ignore the “box” constraints (6.20) (or, equivalently, that $L   \leq   \alpha _ { 2 }   \leq   H )$ , then we can easily maximize this quadratic function by setting its derivative to zero and solving. We’ll let $\alpha _ { 2 } ^ { n e w , \bar { u n c l i p p e d } }$ denote the resulting value of $\alpha _ { 2 }$ . You should also be able to convince yourself that if we had instead wanted to maximize W with respect to $\alpha _ { 2 }$ but subject to the box constraint, then we can find the resulting value optimal simply by taking $\alpha _ { 2 } ^ { n }$ new,unclipped2 and “clipping” it to lie in the [L, H] interval, to get

$$
\alpha_ {2} ^ {n e w} = \left\{ \begin{array}{l l} H & \text {if} \alpha_ {2} ^ {n e w, u n c l i p p e d} > H \\ \alpha_ {2} ^ {n e w, u n c l i p p e d} & \text {if} L \leq \alpha_ {2} ^ {n e w, u n c l i p p e d} \leq H \\ L & \text {if} \alpha_ {2} ^ {n e w, u n c l i p p e d} <   L \end{array} \right.
$$

Finally, having found the $\alpha _ { 2 } ^ { n e w }$ , we can use Equation (6.22) to $\mathrm { g o }$ back and find the optimal value of $\alpha _ { 1 } ^ { n e w }$

There’re a couple more details that are quite easy but that we’ll leave you to read about yourself in Platt’s paper: One is the choice of the heuristics used to select the next $\alpha _ { i } ,   \alpha _ { j }$ to update; the other is how to update b as the SMO algorithm is run.

<!-- page: 80 -->

Part II

Deep learning

<!-- page: 81 -->

## Chapter 7

## Deep learning

We now begin our study of deep learning. In this set of notes, we give an overview of neural networks, discuss vectorization and discuss training neural networks with backpropagation.

## 7.1 Supervised learning with non-linear models

In the supervised learning setting (predicting y from the input $x )$ , suppose our model/hypothesis is $h _ { \theta } ( x )$ . In the past lectures, we have considered the cases when $h _ { \theta } ( x ) = \theta ^ { \top } x$ (in linear regression) or $h _ { \theta } ( x ) = \theta ^ { \top } \phi ( x )$ (where $\phi ( x )$ is the feature map). A commonality of these two models is that they are linear in the parameters θ. Next we will consider learning a general family of models that are non-linear in both the parameters θ and the inputs x. The most common non-linear models are neural networks, which we will define starting from the next section. For this section, it suffices to think $h _ { \theta } ( x )$ as an abstract non-linear model.<sup>1</sup>

Suppose $\{ ( x ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { n }$ are the training examples. We will define the nonlinear model and the loss/cost function for learning it.

Regression problems. For simplicity, we start with the case where the output is a real number, that is, $y ^ { ( i ) } \in \mathbb { R }$ , and thus the model $h _ { \theta }$ also outputs a real number $h _ { \theta } ( x )   \in   \mathbb { R }$ . We define the least square cost function for the

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">θ(x) = x + x +</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1If a concrete example is helpful, perhaps think about the model h θ21 21 θ22 22 · · · + θ<sup>2</sup><sub>d</sub>x2d in this subsection, even though it’s not a neural network.</span></small>

<!-- page: 82 -->

i-th example $( x ^ { ( i ) } , y ^ { ( i ) } )$ as

$$
J ^ {(i)} (\theta) = \frac {1}{2} (h _ {\theta} (x ^ {(i)}) - y ^ {(i)}) ^ {2},\tag{7.1}
$$

and define the mean-square cost function for the dataset as

$$
J (\theta) = \frac {1}{n} \sum_ {i = 1} ^ {n} J ^ {(i)} (\theta),\tag{7.2}
$$

which is same as in linear regression except that we introduce a constant $1 / n$ in front of the cost function to be consistent with the convention. Note that multiplying the cost function with a scalar will not change the local minima or global minima of the cost function. Also note that the underlying parameterization for $h _ { \theta } ( x )$ is different from the case of linear regression, even though the form of the cost function is the same mean-squared loss. Throughout the notes, we use the words “loss” and “cost” interchangeably.

Binary classification. Next we define the model and loss function for binary classification. Suppose the inputs $x   \in   \mathbb { R } ^ { d }$ . Let $\bar { h } _ { \theta }   :   \mathbb { R } ^ { d }   \to   \mathbb { R }$ be a parameterized model (the analog of $\theta ^ { \top } x$ in logistic linear regression). We call the output $\bar { h } _ { \theta } ( x )   \stackrel { \cdot } { \in }   \mathbb { R }$ the logit. Analogous to Section 2.1, we use the logistic function $g ( \cdot )$ to turn the logit $\bar { h } _ { \theta } ( x )$ to a probability $h _ { \theta } ( x ) \in [ 0 , 1 ]$

$$
h _ {\theta} (x) = g (\bar {h} _ {\theta} (x)) = 1 / (1 + \exp (- \bar {h} _ {\theta} (x)).\tag{7.3}
$$

We model the conditional distribution of y given x and θ by

$$
\begin{array}{l l l} P (y = 1 \mid x; \theta) & = & h _ {\theta} (x) \\ P (y = 0 \mid x; \theta) & = & 1 - h _ {\theta} (x) \end{array}
$$

Following the same derivation in Section 2.1 and using the derivation in Remark 2.1.1, the negative likelihood loss function is equal to:

$$
J ^ {(i)} (\theta) = - \log p (y ^ {(i)} \mid x ^ {(i)}; \theta) = \ell_ {\mathrm{logistic}} (\bar {h} _ {\theta} (x ^ {(i)}), y ^ {(i)})\tag{7.4}
$$

As done in equation (7.2), the total loss function is also defined as the average of the loss function over individual training examples, $\begin{array} { r } { J ( \theta ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } J ^ { ( i ) } ( \theta ) } \end{array}$

<!-- page: 83 -->

Multi-class classification. Following Section 2.3, we consider a classification problem where the response variable y can take on any one of k values, i.e. $y   \in   \{ 1 , 2 , \ldots , k \}$ . Let $\bar { h } _ { \theta }   :   \mathbb { R } ^ { d }   \to   \mathbb { R } ^ { k }$ be a parameterized model. We call the outputs $\bar { h } _ { \theta } ( x ) \in \mathbb { R } ^ { k }$ the logits. Each logit corresponds to the prediction for one of the k classes. Analogous to Section 2.3, we use the softmax function to turn the logits $\bar { h } _ { \theta } ( x )$ into a probability vector with non-negative entries that sum up to 1:

$$
P (y = j \mid x; \theta) = \frac {\exp (\bar {h} _ {\theta} (x) _ {j})}{\sum_ {s = 1} ^ {k} \exp (\bar {h} _ {\theta} (x) _ {s})},\tag{7.5}
$$

where $\bar { h } _ { \theta } ( x ) _ { , }$ denotes the s-th coordinate of $\bar { h } _ { \theta } ( x )$

Similarly to Section 2.3, the loss function for a single training example $( x ^ { ( i ) } , y ^ { ( i ) } )$ is its negative log-likelihood:

$$
J ^ {(i)} (\theta) = - \log p (y ^ {(i)} \mid x ^ {(i)}; \theta) = - \log \left(\frac {\exp (\bar {h} _ {\theta} (x ^ {(i)}) _ {y ^ {(i)}})}{\sum_ {s = 1} ^ {k} \exp (\bar {h} _ {\theta} (x ^ {(i)}) _ {s})}\right).\tag{7.6}
$$

Using the notations of Section 2.3, we can simply write in an abstract way:

$$
J ^ {(i)} (\theta) = \ell_ {\mathrm{ce}} (\bar {h} _ {\theta} (x ^ {(i)}), y ^ {(i)}).\tag{7.7}
$$

The loss function is also defined as the average of the loss function of individual training examples, $\begin{array} { r } { J ( \theta ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } J ^ { ( i ) } ( \theta ) } \end{array}$

We also note that the approach above can also be generated to any conditional probabilistic model where we have an exponential distribution for y, Exponential-family $( y ; \eta )$ , where $\eta   =   \bar { h } _ { \theta } ( x )$ is a parameterized nonlinear function of $x .$ However, the most widely used situations are the three cases discussed above.

Optimizers (SGD). Commonly, people use gradient descent (GD), stochastic gradient (SGD), or their variants to optimize the loss function $J ( \theta )$ . GD’s update rule can be written $\mathrm { a s } ^ { 2 }$

$$
\theta := \theta - \alpha \nabla_ {\theta} J (\theta)\tag{7.8}
$$

where $\alpha > 0$ is often referred to as the learning rate or step size. Next, we introduce a version of the SGD (Algorithm 1), which is lightly different from that in the first lecture notes.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“a : ”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“ b”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Recall that, as defined in the previous lecture notes, we use the notation = b to denote an operation (in a computer program) in which we set the value of a variable a to be equal to the value of b. In other words, this operation overwrites a with the value of b. In contrast, we will write a =  when we are asserting a statement of fact, that the value of a is equal to the value of b.</span></small>

<!-- page: 84 -->

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 Stochastic Gradient Descent
Hyperparameter: learning rate $\alpha$, number of total iteration $n_{\text{iter}}$.
Initialize $\theta$ randomly.
for $i = 1$ to $n_{\text{iter}}$ do
    Sample $j$ uniformly from $\{1, \ldots, n\}$, and update $\theta$ by
    $\theta := \theta - \alpha \nabla_{\theta} J^{(j)}(\theta)$ (7.9)
</div>

Oftentimes computing the gradient of B examples simultaneously for the parameter θ can be faster than computing B gradients separately due to hardware parallelization. Therefore, a mini-batch version of SGD is most commonly used in deep learning, as shown in Algorithm 2. There are also other variants of the SGD or mini-batch SGD with slightly different sampling schemes.

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2 Mini-batch Stochastic Gradient Descent
Hyperparameters: learning rate $\alpha$, batch size $B$, $\#$ iterations $n_{\text{iter}}$.
Initialize $\theta$ randomly
for $i = 1$ to $n_{\text{iter}}$ do
    Sample $B$ examples $j_1, \ldots, j_B$ (without replacement) uniformly from $\{1, \ldots, n\}$, and update $\theta$ by
\[\theta := \theta - \frac{\alpha}{B} \sum_{k=1}^{B} \nabla_\theta J^{(j_k)}(\theta)\tag{7.10}\]
</div>

With these generic algorithms, a typical deep learning model is learned with the following steps. 1. Define a neural network parametrization $h _ { \theta } ( x )$ which we will introduce in Section 7.2, and 2. write the backpropagation algorithm to compute the gradient of the loss function $J ^ { ( j ) } ( \theta )$ efficiently, which will be covered in Section 7.4, and 3. run SGD or mini-batch SGD (or other gradient-based optimizers) with the loss function $J ( \theta )$

<!-- page: 85 -->

## 7.2 Neural networks

Neural networks refer to a broad type of non-linear models/parametrizations $\bar { h } _ { \theta } ( x )$ that involve combinations of matrix multiplications and other entry wise non-linear operations. To have a unified treatment for regression prob lem and classification problem, here we consider $\bar { h } _ { \theta } ( x )$ as the output of the neural network. For regression problem, the final prediction $h _ { \theta } ( x ) = \bar { h } _ { \theta } ( x )$ and for classification problem, $\bar { h } _ { \theta } ( x )$ is the logits and the predicted probability will be $h _ { \theta } ( x ) = 1 / ( 1   +   \exp ( - \bar { h } _ { \theta } ( x ) )$ (see equation 7.3) for binary classification or $h _ { \theta } ( x ) = \operatorname { s o f t m a x } ( \bar { h } _ { \theta } ( x ) )$ for multi-class classification (see equation 7.5).

We will start small and slowly build up a neural network, step by step.

A Neural Network with a Single Neuron. Recall the housing price prediction problem from before: given the size of the house, we want to predict the price. We will use it as a running example in this subsection.

Previously, we fit a straight line to the graph of size vs. housing price. Now, instead of fitting a straight line, we wish to prevent negative housing prices by setting the absolute minimum price as zero. This produces a “kink” in the graph as shown in Figure 7.1. How do we represent such a function with a single kink as $\bar { h } _ { \theta } ( x )$ with unknown parameter? (After doing so, we can invoke the machinery in Section 7.1.)

We define a parameterized function $\bar { h } _ { \theta } ( x )$ with input x, parameterized by $\theta ,$ which outputs the price of the house y. Formally, $\bar { h } _ { \theta } : x \to y$ . Perhaps one of the simplest parametrization would be

$$
\bar {h} _ {\theta} (x) = \max (w x + b, 0), \text {where} \theta = (w, b) \in \mathbb {R} ^ {2}\tag{7.11}
$$

Here $\bar { h } _ { \theta } ( x )$ returns a single value: $( w x + b )$ or zero, whichever is greater. In the context of neural networks, the function max $\{ t , 0 \}$ is called a ReLU (pronounced $``ray-lu'')$ , or rectified linear unit, and often denoted by ReL $\mathrm { U } ( t ) \triangleq$ max{t, 0}.

Generally, a one-dimensional non-linear function that maps R to R such as ReLU is often referred to as an activation function. The model $\bar { h } _ { \theta } ( x )$ is said to have a single neuron partly because it has a single non-linear activation function. (We will discuss more about why a non-linear activation is called neuron.)

When the input $x \in \mathbb { R } ^ { d }$ has multiple dimensions, a neural network with a single neuron can be written as

$$
\bar {h} _ {\theta} (x) = \mathrm{ReLU} (w ^ {\top} x + b), \text {where} w \in \mathbb {R} ^ {d}, b \in \mathbb {R}, \text {and} \theta = (w, b)\tag{7.12}
$$

<!-- page: 86 -->

The term b is often referred to as the “bias”, and the vector w is referred to as the weight vector. Such a neural network has 1 layer. (We will define what multiple layers mean in the sequel.)

Stacking Neurons. A more complex neural network may take the single neuron described above and “stack” them together such that one neuron passes its output as input into the next neuron, resulting in a more complex function.

Let us now deepen the housing prediction example. In addition to the size of the house, suppose that you know the number of bedrooms, the zip code and the wealth of the neighborhood. Building neural networks is analogous to Lego bricks: you take individual bricks and stack them together to build complex structures. The same applies to neural networks: we take individual neurons and stack them together to create complex neural networks.

![](images/page_85_chart_4.jpg)

Figure 7.1: Housing prices with a “kink” in the graph.

Given these features (size, number of bedrooms, zip code, and wealth), we might then decide that the price of the house depends on the maximum family size it can accommodate. Suppose the family size is a function of the size of the house and number of bedrooms (see Figure 7.2). The zip code may provide additional information such as how walkable the neighborhood is (i.e., can you walk to the grocery store or do you need to drive everywhere). Combining the zip code with the wealth of the neighborhood may predict the quality of the local elementary school. Given these three derived features

<!-- page: 87 -->

(family size, walkable, school quality), we may conclude that the price of the home ultimately depends on these three features.

![](images/page_86_image_2.jpg)

Figure 7.2: Diagram of a small neural network for predicting housing prices.

Formally, the input to a neural network is a set of input features $x _ { 1 } , x _ { 2 } , x _ { 3 } , x _ { 4 }$ . We denote the intermediate variables for “family size”, “walkable”, and “school quality” by $a _ { 1 } , a _ { 2 } , a _ { 3 }$ (these $a _ { i } \mathrm { ^ { \prime } s }$ are often referred to as “hidden units” or “hidden neurons”). We represent each of the $a _ { i } \mathrm { { } ^ { \prime } s }$ as a neural network with a single neuron with a subset of $x _ { 1 } , \ldots , x _ { 4 }$ as inputs. Then as in Figure 7.1, we will have the parameterization:

$$
\begin{array}{l} a _ {1} = \mathrm{ReLU} (\theta_ {1} x _ {1} + \theta_ {2} x _ {2} + \theta_ {3}) \\ a _ {2} = \mathrm{ReLU} (\theta_ {4} x _ {3} + \theta_ {5}) \\ a _ {3} = \mathrm{ReLU} (\theta_ {6} x _ {3} + \theta_ {7} x _ {4} + \theta_ {8}) \end{array}
$$

where $( \theta _ { 1 } , \cdots , \theta _ { 8 } )$ are parameters. Now we represent the final output $\bar { h } _ { \theta } ( x )$ as another linear function with $a _ { 1 } , a _ { 2 } , a _ { 3 }$ as inputs, and we $\mathrm { g e t ^ { 3 } }$

$$
\bar {h} _ {\theta} (x) = \theta_ {9} a _ {1} + \theta_ {1 0} a _ {2} + \theta_ {1 1} a _ {3} + \theta_ {1 2}\tag{7.13}
$$

where θ contains all the parameters $( \theta _ { 1 } , \cdots , \theta _ { 1 2 } )$

Now we represent the output as a quite complex function of x with parameters θ. Then you can use this parametrization $\bar { h } _ { \theta }$ with the machinery of Section 7.1 to learn the parameters θ.

Inspiration from Biological Neural Networks. As the name suggests, artificial neural networks were inspired by biological neural networks. The hidden units $a _ { 1 } , \ldots , a _ { m }$ correspond to the neurons in a biological neural network, and the parameters $\theta _ { i } \mathrm { ~ ' s ~ }$ correspond to the synapses. However, it’s

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Typically, for multi-layer neural network, at the end, near the output, we don’t apply ReLU, especially when the output is not necessarily a positive number.</span></small>

<!-- page: 88 -->

unclear how similar the modern deep artificial neural networks are to the biological ones. For example, perhaps not many neuroscientists think biological neural networks could have 1000 layers, while some modern artificial neural networks do (we will elaborate more on the notion of layers.) Moreover, it’s an open question whether human brains update their neural networks in a way similar to the way that computer scientists learn artificial neural networks (using backpropagation, which we will introduce in the next section.)

Two-layer Fully-Connected Neural Networks. We constructed the neural network in equation (7.13) using a significant amount of prior knowledge/belief about how the “family size”, “walkable”, and “school quality” are determined by the inputs. We implicitly assumed that we know the family size is an important quantity to look at and that it can be determined by only the “size” and $^ { \circ } \#$ bedrooms”. Such a prior knowledge might not be available for other applications. It would be more flexible and general to have a generic parameterization. A simple way would be to write the intermediate variable $a _ { 1 }$ as a function of all $x _ { 1 } , \ldots , x _ { 4 } ;$

$$
a _ {1} = \mathrm{ReLU} (w _ {1} ^ {\top} x + b _ {1}), \text {where} w _ {1} \in \mathbb {R} ^ {4} \text {and} b _ {1} \in \mathbb {R}\tag{7.14}
$$

$$
a _ {2} = \mathrm{ReLU} (w _ {2} ^ {\top} x + b _ {2}), \text {where} w _ {2} \in \mathbb {R} ^ {4} \text {and} b _ {2} \in \mathbb {R}
$$

$$
a _ {3} = \mathrm{ReLU} (w _ {3} ^ {\top} x + b _ {3}), \text {where} w _ {3} \in \mathbb {R} ^ {4} \text {and} b _ {3} \in \mathbb {R}
$$

We still define $\bar { h } _ { \theta } ( x )$ using equation (7.13) with $a _ { 1 } , a _ { 2 } , a _ { 3 }$ being defined as above. Thus we have a so-called fully-connected neural network because all the intermediate variables $a _ { i } \mathrm { { } ^ { \prime } s }$ depend on all the inputs $x _ { i } { } ^ { \flat } \mathrm { S }$

For full generality, a two-layer fully-connected neural network with m hidden units and d dimensional input $x \in \mathbb { R } ^ { d }$ is defined as

$$
\forall j \in [ 1, \dots , m ], \quad z _ {j} = w _ {j} ^ {[ 1 ] ^ {\top}} x + b _ {j} ^ {[ 1 ]} \text {where} w _ {j} ^ {[ 1 ]} \in \mathbb {R} ^ {d}, b _ {j} ^ {[ 1 ]} \in \mathbb {R}\tag{7.15}
$$

$$
a _ {j} = \mathrm{ReLU} (z _ {j}),
$$

$$
a = [ a _ {1}, \dots , a _ {m} ] ^ {\top} \in \mathbb {R} ^ {m}
$$

$$
\bar {h} _ {\theta} (x) = w ^ {[ 2 ] \top} a + b ^ {[ 2 ]} \text {where} w ^ {[ 2 ]} \in \mathbb {R} ^ {m}, b ^ {[ 2 ]} \in \mathbb {R},\tag{7.16}
$$

Note that by default the vectors in $\mathbb { R } ^ { d }$ are viewed as column vectors, and in particular a is a column vector with components $a _ { 1 } , a _ { 2 } , . . . , a _ { m }$ . The indices [1] and [2] are used to distinguish two sets of parameters: the $w _ { j } ^ { [ 1 ] } { } ^ { \mathrm { , } } \mathrm { s }$ (each of which is a vector in $\mathbb { R } ^ { d } )$ and $w ^ { [ 2 ] }$ (which is a vector in $\mathbb { R } ^ { m } )$ . We will have more of these later.

<!-- page: 89 -->

Vectorization. Before we introduce neural networks with more layers and more complex structures, we will simplify the expressions for neural networks with more matrix and vector notations. Another important motivation of vectorization is the speed perspective in the implementation. In order to implement a neural network efficiently, one must be careful when using for loops. The most natural way to implement equation (7.15) in code is perhaps to use a for loop. In practice, the dimensionalities of the inputs and hidden units are high. As a result, code will run very slowly if you use for loops. Leveraging the parallelism in GPUs is/was crucial for the progress of deep learning.

This gave rise to vectorization. Instead of using for loops, vectorization takes advantage of matrix algebra and highly optimized numerical linear algebra packages (e.g., BLAS) to make neural network computations run quickly. Before the deep learning era, a for loop may have been sufficient on smaller datasets, but modern deep networks and state-of-the-art datasets will be infeasible to run with for loops.

We vectorize the two-layer fully-connected neural network as below. We define a weight matrix $W ^ { [ 1 ] }$ in $\mathbb { R } ^ { m \times d }$ as the concatenation of all the vectors $w _ { j } ^ { [ 1 ] } { } ^ { \mathrm { , } } \mathrm { s }$ in the following way:

$$
W ^ {[ 1 ]} = \left[ \begin{array}{c} - w _ {1} ^ {[ 1 ] ^ {\top}} - \\ - w _ {2} ^ {[ 1 ] ^ {\top}} - \\ \vdots \\ - w _ {m} ^ {[ 1 ] ^ {\top}} - \end{array} \right] \in \mathbb {R} ^ {m \times d}\tag{7.17}
$$

Now by the definition of matrix vector multiplication, we can write $z =$ $[ z _ { 1 } , \ldots , z _ { m } ] ^ { \top } \in \mathbb { R } ^ { m }$ as

$$
\underbrace {\left[ \begin{array}{c} z _ {1} \\ \vdots \\ \vdots \\ z _ {m} \end{array} \right]} _ {z \in \mathbb {R} ^ {m \times 1}} = \underbrace {\left[ \begin{array}{c} - w _ {1} ^ {[ 1 ] ^ {\top}} - \\ - w _ {2} ^ {[ 1 ] ^ {\top}} - \\ \vdots \\ - w _ {m} ^ {[ 1 ] ^ {\top}} - \end{array} \right]} _ {W ^ {[ 1 ]} \in \mathbb {R} ^ {m \times d}} \underbrace {\left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {d} \end{array} \right]} _ {x \in \mathbb {R} ^ {d \times 1}} + \underbrace {\left[ \begin{array}{c} b _ {1} ^ {[ 1 ]} \\ b _ {2} ^ {[ 1 ]} \\ \vdots \\ b _ {m} ^ {[ 1 ]} \end{array} \right]} _ {b ^ {[ 1 ]} \in \mathbb {R} ^ {m \times 1}}\tag{7.18}
$$

Or succinctly,

$$
z = W ^ {[ 1 ]} x + b ^ {[ 1 ]}\tag{7.19}
$$

<!-- page: 90 -->

We remark again that a vector in $\mathbb { R } ^ { d }$ in this notes, following the conventions previously established, is automatically viewed as a column vector, and can also be viewed as a $d \times 1$ dimensional matrix. (Note that this is different from numpy where a vector is viewed as a row vector in broadcasting.)

Computing the activations $a   \in   \mathbb { R } ^ { m }$ from $z   \in   \mathbb { R } ^ { m }$ involves an elementwise non-linear application of the ReLU function, which can be computed in parallel efficiently. Overloading ReLU for element-wise application of ReLU (meaning, for a vector $t   \in   \mathbb { R } ^ { d }$ , ReLU(t) is a vector such that $\mathrm { R e L U } ( t ) _ { i } =$ $\operatorname { R e L U } ( t _ { i } ) )$ , we have

$$
a = \mathrm{ReLU} (z)\tag{7.20}
$$

Define $W ^ { [ 2 ] } = [ { w ^ { [ 2 ] } } ^ { \top } ] \in \mathbb { R } ^ { 1 \times m }$ similarly. Then, the model in equation (7.16) can be summarized as

$$
\begin{array}{c} {a = \mathrm{ReLU} (W ^ {[ 1 ]} x + b ^ {[ 1 ]})} \\ {\bar {h} _ {\theta} (x) = W ^ {[ 2 ]} a + b ^ {[ 2 ]}} \end{array}\tag{7.21}
$$

Here θ consists of $W ^ { [ 1 ] } , W ^ { [ 2 ] }$ (often referred to as the weight matrices) and $b ^ { [ 1 ] } , b ^ { [ 2 ] }$ (referred to as the biases). The collection of $W ^ { [ 1 ] } , \widetilde { b ^ { [ 1 ] } }$ is referred to as the first layer, and $W ^ { [ 2 ] } , b ^ { [ 2 ] }$ the second layer. The activation a is referred to as the hidden layer. A two-layer neural network is also called one-hidden-layer neural network.

Multi-layer fully-connected neural networks. With this succinct notations, we can stack more layers to get a deeper fully-connected neural network. Let r be the number of layers (weight matrices). Let $W ^ { [ 1 ] } , \ldots , W ^ { [ r ] } , b ^ { [ 1 ] } , \ldots , b ^ { [ r ] }$ be the weight matrices and biases of all the layers. Then a multi-layer neural network can be written as

$$
\begin{array}{c} a ^ {[ 1 ]} = \mathrm{ReLU} (W ^ {[ 1 ]} x + b ^ {[ 1 ]}) \\ a ^ {[ 2 ]} = \mathrm{ReLU} (W ^ {[ 2 ]} a ^ {[ 1 ]} + b ^ {[ 2 ]}) \\ \dots \\ a ^ {[ r - 1 ]} = \mathrm{ReLU} (W ^ {[ r - 1 ]} a ^ {[ r - 2 ]} + b ^ {[ r - 1 ]}) \\ \bar {h} _ {\theta} (x) = W ^ {[ r ]} a ^ {[ r - 1 ]} + b ^ {[ r ]} \end{array}\tag{7.22}
$$

We note that the weight matrices and biases need to have compatible dimensions for the equations above to make sense. If $a ^ { [ k ] }$ has dimension $m _ { k }$ then the weight matrix $W ^ { [ k ] }$ should be of dimension $m _ { k } \times m _ { k - 1 }$ , and the bias $b ^ { [ k ] } \in \mathbb { R } ^ { m _ { k } }$ . Moreover, $W ^ { [ 1 ] } \in \mathbb { R } ^ { m _ { 1 } \times d }$ and $W ^ { [ r ] } \in \mathbb { R } ^ { 1 \times m _ { r - 1 } }$

<!-- page: 91 -->

The total number of neurons in the network is $m _ { 1 } + \cdots + m _ { r }$ , and the total number of parameters in this network is $( d + 1 ) m _ { 1 } + ( m _ { 1 } + 1 ) m _ { 2 } + \cdots +$ $( m _ { r - 1 } + 1 ) m _ { r }$

Sometimes for notational consistency we also write $a ^ { [ 0 ] }   =   x$ , and $a ^ { [ r ] } =$ $h _ { \theta } ( x )$ . Then we have simple recursion that

$$
a ^ {[ k ]} = \mathrm{ReLU} (W ^ {[ k ]} a ^ {[ k - 1 ]} + b ^ {[ k ]}), \forall k = 1, \dots , r - 1\tag{7.23}
$$

Note that this would have been true for $k   =   r$ if there were an additional ReLU in equation (7.22), but often people like to make the last layer linear (aka without a ReLU) so that negative outputs are possible and it’s easier to interpret the last layer as a linear model. (More on the interpretability at the “connection to kernel method” paragraph of this section.)

Other activation functions. The activation function ReLU can be replaced by many other non-linear function $\sigma ( \cdot )$ that maps R to R such as

$$
\sigma (z) = \frac {1}{1 + e ^ {- z}} \qquad (\text {sigmoid})\tag{7.24}
$$

$$
\sigma (z) = \frac {e ^ {z} - e ^ {- z}}{e ^ {z} + e ^ {- z}} \qquad (\tanh)\tag{7.25}
$$

$$
\sigma (z) = \max \{z, \gamma z \}, \gamma \in (0, 1) \quad \text {(leaky ReLU)}\tag{7.26}
$$

$$
\sigma (z) = \frac {z}{1 + e ^ {- \beta z}}, \beta > 0 \qquad (\mathrm{Swish} _ {\beta})\tag{7.27}
$$

$$
\sigma (z) = \frac {z}{2} \left[ 1 + \mathrm{erf} (\frac {z}{\sqrt {2}}) \right] \quad \text {(GELU)}\tag{7.28}
$$

$$
\sigma (z) = \max \{z, 0 \} ^ {2} \qquad (\mathrm{ReLU} ^ {2})\tag{7.29}
$$

$$
\sigma (z) = \frac {1}{\beta} \log (1 + \exp (\beta z)), \beta > 0 \qquad \text {(Softplus)}\tag{7.30}
$$

The activation functions are plotted in Figure 7.3. Sigmoid and tanh are less and less used these days as standalone hidden-layer activations partly be cause they are bounded from both sides and their gradients vanish as z goes to both positive and negative infinity (whereas all the other activation functions above still have gradients as the input goes to positive infinity.) Sigmoid nevertheless remains important as a gating nonlinearity, for example in some mixture-of-experts routers [Nguyen et al., 2025] and gated attention mech anisms [Qiu et al., 2025]. Softplus is not used very often in practice either and can be viewed as a smoothing of ReLU so that it has a proper secondorder derivative. Swish<sub>β</sub> was introduced by Ramachandran et al. [2017]; it

<!-- page: 92 -->

![](images/page_91_chart_1.jpg)

Figure 7.3: Activation functions in deep learning. The y-axis is capped above 5 for visualization.

is also commonly called SiLU, especially in the case $\beta   =   1$ , and is used in architectures such as EfficientNet [Tan and Le, 2019]. GELU was introduced by Hendrycks and Gimpel [2016] and is widely used in Transformer language models such as BERT [Devlin et al., 2019], as well as in diffusion Transformers such as Hunyuan-DiT [Li et al., 2024]. ReL $\mathrm { _ { \mu } U ^ { 2 } }$ is a simple higher-order variant of ReLU that is used in Primer [So et al., 2021] and was later found to improve sparsity in sparse LLMs [Zhang et al., 2024].

Another practically important family, especially in modern sequence models, is gated activations. A gated linear unit (GLU) takes two affine transforms of the same input h and uses one to gate the other:

$$
\mathrm{GLU} (h) = (W _ {1} h + b _ {1}) \odot g (W _ {2} h + b _ {2}),\tag{7.31}
$$

where $g$ is typically the logistic sigmoid and  denotes element-wise multi-plication [Dauphin et al., 2016]. Thus, unlike the scalar activations above, GLU is not a map $\sigma   :   \mathbb { R }   \rightarrow   \mathbb { R }$ , but a small module combining the results of two matrix-vector multiplications through multiplicative gating. Modern Transformer feed-forward layers often use the SwiGLU variant [Shazeer, 2020, Touvron et al., 2023, Yang et al., 2025, OpenAI, 2025].

Why do we not use the identity function for $\sigma ( z ) ?$ That is, why not use $\sigma ( z ) = z ?$ Assume for sake of argument that $b ^ { [ 1 ] }$ and $b ^ { [ 2 ] }$ are zeros.

<!-- page: 93 -->

Suppose $\sigma ( z ) = z$ , then for two-layer neural network, we have that

$$
\bar {h} _ {\theta} (x) = W ^ {[ 2 ]} a ^ {[ 1 ]}\tag{7.32}
$$

$$
= W ^ {[ 2 ]} \sigma (z ^ {[ 1 ]})
$$

$$
\text {by definition}\tag{7.33}
$$

$$
= W ^ {[ 2 ]} z ^ {[ 1 ]}
$$

$$
\text {since} \sigma (z) = z\tag{7.34}
$$

$$
= W ^ {[ 2 ]} W ^ {[ 1 ]} x
$$

$$
\text {from Equation (7.18)}\tag{7.35}
$$

$$
= \tilde {W} x
$$

$$
\mathrm{where} \tilde {W} = W ^ {[ 2 ]} W ^ {[ 1 ]}\tag{7.36}
$$

Notice how $W ^ { [ 2 ] } W ^ { [ 1 ] }$ collapsed into $\tilde { W }$

This is because applying a linear function to another linear function will result in a linear function over the original input $( \mathrm { i . e . }$ , you can construct a $\tilde { W }$ such that $\tilde { W } x = W ^ { [ 2 ] } W ^ { [ 1 ] } x )$ . This loses much of the representational power of the neural network as often times the output we are trying to predict has a non-linear relationship with the inputs. Without non-linear activation functions, the neural network will simply perform linear regression.

Connection to the Kernel Method. In the previous lectures, we covered the concept of feature maps. Recall that the main motivation for feature maps is to represent functions that are non-linear in the input x by $\theta ^ { \top } \phi ( x )$ where $\theta$ are the parameters and $\phi ( x )$ , the feature map, is a handcrafted function non-linear in the raw input x. The performance of the learning algorithms can significantly depend on the choice of the feature map $\phi ( x )$ Oftentimes people use domain knowledge to design the feature map $\phi ( x )$ that suits the particular applications. The process of choosing the feature maps is often referred to as feature engineering.

We can view deep learning as a way to automatically learn the right feature map (sometimes also referred to as “the representation”) as follows. Suppose we denote by $\beta$ the collection of the parameters in a fully-connected neural networks (equation (7.22)) except those in the last layer. Then we can abstract right $\stackrel { - } { a ^ { [ r - 1 ] } }$ as a function of the input x and the parameters in $\beta \colon a ^ { [ r - 1 ] } = \phi _ { \beta } ( x )$ . Now we can write the model as

$$
\bar {h} _ {\theta} (x) = W ^ {[ r ]} \phi_ {\beta} (x) + b ^ {[ r ]}\tag{7.37}
$$

When $\beta$ is fixed, then $\phi _ { \beta } ( \cdot )$ can be viewed as a feature map, and therefore $\bar { h } _ { \theta } ( x )$ is just a linear model over the features $\phi _ { \beta } ( x )$ . However, when we train the neural networks, both the parameters in $\beta$ and the parameters $W ^ { [ r ] } , b ^ { [ r ] }$ are optimized, and therefore we are not only learning a linear model in the feature space, but also learning a good feature map $\phi _ { \beta } ( \cdot )$ itself so that it’s

<!-- page: 94 -->

possible to predict accurately with a linear model on top of the feature map. Therefore, deep learning tends to depend less on the domain knowledge of the particular applications and often requires less feature engineering. The penultimate layer $a ^ { [ r ] }$ is often (informally) referred to as the learned features or representations in the context of deep learning.

In the example of house price prediction, a fully-connected neural network does not need us to specify the intermediate quantity such as “family size”, and may automatically discover some useful features in the penultimate layer (the activation $a ^ { [ r - 1 ] } )$ , and use them to linearly predict the housing price. Often the feature map $/$ representation obtained from one dataset (that is, the function $\phi _ { \beta } ( \cdot ) )$ can also be useful for other datasets, which indicates that it contains essential information about the data. However, oftentimes, the neural network will discover complex features which are very useful for predicting the output but may be difficult for a human to understand or interpret. This is why some people refer to neural networks as a black box, as it can be difficult to understand the features it has discovered.

## 7.3 Modules in Modern Neural Networks

The multi-layer neural network introduced in equation (7.22) of Section 7.2 is often called multi-layer perceptron (MLP) these days. Modern neural networks used in practice are often much more complex and consist of multiple building blocks or multiple layers of building blocks. In this section, we will introduce some of the other building blocks and discuss possible ways to combine them.

First, each matrix multiplication can be viewed as a building block. Consider a matrix multiplication operation with parameters (W, b) where W is the weight matrix and b is the bias vector, operating on an input z,

$$
\mathrm{MM} _ {W, b} (z) = W z + b.\tag{7.38}
$$

Note that we implicitly assume all the dimensions are chosen to be compatible. We will also drop the subscripts under MM when they are clear in the context or just for convenience when they are not essential to the discussion.

Then, the MLP can be written as a composition of multiple matrix multiplication modules and nonlinear activation modules (which can also be viewed as a building block):

$$
\mathrm{MLP} (x) = \mathrm{MM} _ {W ^ {[ r ], b ^ {[ r ]}}} (\sigma (\mathrm{MM} _ {W ^ {[ r - 1 ], b ^ {[ r - 1 ]}}} (\sigma (\dots \mathrm{MM} _ W ^ {[ 1 ], b ^ {[ 1 ]}} (x)))).\tag{7.39}
$$

<!-- page: 95 -->

![](images/page_94_image_1.jpg)

Figure 7.4: Illustrative Figures for Architecture. Left: An MLP with r layers. Right: A residual network.

Alternatively, when we drop the subscripts that indicate the parameters for convenience, we can write

$$
\mathrm{MLP} (x) = \mathrm{MM} (\sigma (\mathrm{MM} \sigma (\dots \mathrm{MM} (x)))).\tag{7.40}
$$

Note that in this lecture notes, by default, all the modules have different sets of parameters, and the dimensions of the parameters are chosen such that the composition is meaningful.

Larger modules can be defined via smaller modules as well, e.g., one activation layer $\sigma$ and a matrix multiplication layer MM are often combined and called a “layer” in many papers. People often draw the architecture with the basic modules in a figure by indicating the dependency between these modules. E.g., see an illustration of an MLP in Figure 7.4, Left.

Residual connections. One of the very influential neural network architecture for vision application is ResNet, which uses the residual connections that are essentially used in almost all large-scale deep learning architectures these days. Using our notation above, a very much simplified residual block can be defined as

$$
\mathrm{Res} (z) = z + \sigma (\mathrm{MM} (\sigma (\mathrm{MM} (z)))).\tag{7.41}
$$

A much simplified ResNet is a composition of many residual blocks followed by a matrix multiplication,

$$
\mathrm{ResNet-S} (x) = \mathrm{MM} (\mathrm{Res} (\mathrm{Res} (\dots \mathrm{Res} (x)))).\tag{7.42}
$$

We also draw the dependency of these modules in Figure 7.4, Right.

<!-- page: 96 -->

We note that the ResNet-S is still not the same as the ResNet architec ture introduced in the seminal paper [He et al., 2016] because ResNet uses convolution layers instead of vanilla matrix multiplication, and adds batch normalization between convolutions and activations. We will introduce convolutional layers and some variants of batch normalization below. ResNet-S and layer normalization are part of the Transformer architecture that are widely used in modern large language models.

Layer normalization. Layer normalization, denoted by LN in this text, is a module that maps a vector $z \in \mathbb { R } ^ { m }$ to a more normalized vector $\operatorname { L N } ( z ) \in$ $\mathbb { R } ^ { m }$ . It is oftentimes used after the nonlinear activations.

We first define a sub-module of the layer normalization, denoted by LN-S.

$$
\mathrm{LN-S} (z) = \left[ \begin{array}{c} \frac {z _ {1} - \hat {\mu}}{\hat {\sigma}} \\ \frac {z _ {2} - \hat {\mu}}{\hat {\sigma}} \\ \vdots \\ \frac {z _ {m} - \hat {\mu}}{\hat {\sigma}} \end{array} \right],\tag{7.43}
$$

where $\begin{array} { r l r } { \hat { \mu } } & { = } & { \frac { \sum _ { i = 1 } ^ { m } z _ { i } } { m } } \end{array}$ <u>i</u>s the empirical mean of the vector z and $\hat { \sigma } \quad =$ $\sqrt { \textstyle \frac { 1 } { m } \sum _ { i = 1 } ^ { m } ( z _ { i } - \hat { \mu } ) ^ { 2 } }$ is the empirical standard deviation of the entries of $z . ^ { 4 }$ Intuitively, $\operatorname { L N - S } ( z )$ is a vector that is normalized to having empirical mean zero and empirical standard deviation 1.

Oftentimes zero mean and standard deviation 1 is not the most desired normalization scheme, and thus layernorm introduces two learnable scalar parameters $\beta$ and $\gamma$ as the desired mean and standard deviation, and uses an affine transformation to turn the output of $\operatorname { L N - S } ( z )$ into a vector with mean $\beta$ and standard deviation $\gamma$

$$
\mathrm{LN} (z) = \beta + \gamma \cdot \mathrm{LN-S} (z) = \left[ \begin{array}{c} \beta + \gamma \left(\frac {z _ {1} - \hat {\mu}}{\hat {\sigma}}\right) \\ \beta + \gamma \left(\frac {z _ {2} - \hat {\mu}}{\hat {\sigma}}\right) \\ \vdots \\ \beta + \gamma \left(\frac {z _ {m} - \hat {\mu}}{\hat {\sigma}}\right) \end{array} \right].\tag{7.44}
$$

Here the first occurrence of $\beta$ should technically be interpreted as a vector whose entries are all equal to $\beta$ . We also note that $\hat { \mu }$ and $\hat { \sigma }$ are also functions

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">m − 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">LN-S(z)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>Note that we divide by m instead of m − 1 in the empirical standard deviation here because we are interested in making the output of have empirical variance 1, or equivalently sum of squares equal to m (as opposed to estimating the standard deviation in statistics.)</span></small>

<!-- page: 97 -->

of z and shouldn’t be treated as constants when computing the derivatives of layernorm. Moreover, $\beta$ and $\gamma$ are learnable parameters and thus layernorm is a parameterized module (as opposed to the activation layer which doesn’t have any parameters.)

Scaling-invariant property. One important property of layer normalization is that it will make the model invariant to scaling of the parameters in the following sense. Suppose we consider composing LN with $\mathrm { M M } _ { W , b }$ and get a subnetwork $\operatorname { L N } ( \operatorname { M M } _ { W , b } ( z ) )$ . Then, we have that the output of this subnetwork does not change when the parameter in $\mathrm { M M } _ { W , b }$ is scaled:

$$
\mathrm{LN} (\mathrm{MM} _ {\alpha W, \alpha b} (z)) = \mathrm{LN} (\mathrm{MM} _ {W, b} (z)), \forall \alpha > 0.\tag{7.45}
$$

To see this, we first know that $\operatorname { L N - S } ( \cdot )$ is scale-invariant

$$
\mathrm{LN-S} (\alpha z) = \left[ \begin{array}{c} \frac {\alpha z _ {1} - \alpha \hat {\mu}}{\alpha \hat {\sigma}} \\ \frac {\alpha z _ {2} - \alpha \hat {\mu}}{\alpha \hat {\sigma}} \\ \vdots \\ \frac {\alpha z _ {m} - \alpha \hat {\mu}}{\alpha \hat {\sigma}} \end{array} \right] = \left[ \begin{array}{c} \frac {z _ {1} - \hat {\mu}}{\hat {\sigma}} \\ \frac {z _ {2} - \hat {\mu}}{\hat {\sigma}} \\ \vdots \\ \frac {z _ {m} - \hat {\mu}}{\hat {\sigma}} \end{array} \right] = \mathrm{LN-S} (z).\tag{7.46}
$$

Then we have

$$
\mathrm{LN} (\mathrm{MM} _ {\alpha W, \alpha b} (z)) = \beta + \gamma \mathrm{LN-S} (\mathrm{MM} _ {\alpha W, \alpha b} (z))\tag{7.47}
$$

$$
= \beta + \gamma \mathrm{LN-S} (\alpha \mathrm{MM} _ {W, b} (z))\tag{7.48}
$$

$$
= \beta + \gamma \mathrm{LN-S} (\mathrm{MM} _ {W, b} (z))\tag{7.49}
$$

$$
= \mathrm{LN} (\mathrm{MM} _ {W, b} (z)).\tag{7.50}
$$

Due to this property, most of the modern DL architectures for large-scale computer vision and language applications have the following scale-invariant property w.r.t all the weights that are not at the last layer. Suppose the network f has last layer’ weights $W _ { \mathrm { l a s t } }$ , and all the rest of the weights are denote by W. Then, we have $f _ { W _ { \mathrm { l a s t } } , \alpha W } ( x ) = f _ { W _ { \mathrm { l a s t } } , W } ( x )$ for all $\alpha > 0$ . Here, the last layers weights are special because there are typically no layernorm or batchnorm after the last layer’s weights.

Other normalization layers. There are several other normalization layers that aim to normalize the intermediate layers of the neural networks to a more fixed and controllable scaling, such as batch-normalization [Ioffe and Szegedy, 2015], and group normalization [Wu and He, 2018]. Batch normalization and group normalization are more often used in computer vision applications whereas layer norm is used more often in language applications.

<!-- page: 98 -->

Early Transformer models predominantly used layer normalization, but many later decoder-only Transformers instead use RMSNorm (root mean square layer normalization), which rescales a vector by the root mean square of its coordinates and omits the explicit mean-centering step [Zhang and Sennrich, 2019]. For $z \in \mathbb { R } ^ { m }$ , one can write

$$
\mathrm{RMSNorm} (z) = \gamma \cdot \frac {z}\sqrt {\frac {1}{m} \sum_ {i = 1} ^ {m} z _ {i} ^ {2}},\tag{7.51}
$$

where $\gamma$ is a learnable scale parameter. This choice appears in modern large language models such as LLaMA and Qwen [Touvron et al., 2023, Yang et al., 2025].

Convolutional Layers. Convolutional Neural Networks are neural networks that consist of convolution layers (and many other modules), and are particularly useful for computer vision applications. For the simplicity of exposition, we focus on 1-D convolution in this text and only briefly mention 2-D convolution informally at the end of this subsection. (2-D convolution is more suitable for images which have two dimensions. 1-D convolution is also used in natural language processing.)

We start by introducing a simplified version of the 1-D convolution layer, denoted by Conv1D-S(·) which is a type of matrix multiplication layer with a special structure. The parameters of Conv1D-S are a filter vector $w \in \mathbb { R } ^ { k }$ where k is called the filter size (oftentimes $k   \ll   m )$ , and a bias scalar b. Oftentimes the filter is also called a kernel (but it does not have much to do with the kernel in kernel method.) For simplicity, we assume $k = 2 \ell + 1$ is an odd number. We first pad zeros to the input vector z in the sense that we let $z _ { 1 - \ell } = z _ { 1 - \ell + 1 } = . . = z _ { 0 } = 0$ and $z _ { m + 1 } = z _ { m + 2 } = . . = z _ { m + \ell } = 0$ , and treat z as an $( m + 2 \ell )$ -dimension vector. Conv1D-S outputs a vector of dimension $\mathbb { R } ^ { m }$ where each output dimension is a linear combination of subsets of $z _ { j } ^ { \mathrm { ~ i ~ } }$ ’<sup>s</sup> with coefficients from $w ,$

$$
\mathrm{Conv1D-S} (z) _ {i} = w _ {1} z _ {i - \ell} + w _ {2} z _ {i - \ell + 1} + \dots + w _ {2 \ell + 1} z _ {i + \ell} = \sum_ {j = 1} ^ {2 \ell + 1} w _ {j} z _ {i - \ell + (j - 1)}.\tag{7.52}
$$

Therefore, one can view Conv1D-S as a matrix multiplication with shared

<!-- page: 99 -->

parameters: Conv1D-S(z) = Qz, where

$$
Q = \left[ \begin{array}{c c c c c c c c c c c c} w _ {\ell + 1} & \dots & w _ {2 \ell + 1} & 0 & 0 & \dots & \dots & \dots & \dots & \dots & \dots & 0 \\ w _ {\ell} & \dots & w _ {2 \ell} & w _ {2 \ell + 1} & 0 & \dots & \dots & \dots & \dots & \dots & \dots & 0 \\ \vdots & & & & & & & \\ w _ {1} & \dots & w _ {\ell + 1} & \dots & \dots & \dots & w _ {2 \ell + 1} & 0 & \dots & \dots & \dots & 0 \\ 0 & w _ {1} & \dots & \dots & \dots & \dots & w _ {2 \ell} & w _ {2 \ell + 1} & 0 & \dots & \dots & 0 \\ \vdots & & & & & & \\ \vdots & & & & & \\ 0 & \dots & \dots & \dots & \dots & \dots & 0 & w _ {1} & \dots & & \dots & w _ {2 \ell + 1} \\ \vdots & & & & \\ 0 & \dots & \dots & \dots & \dots & \dots & \dots & \dots & 0 & w _ {1} & \dots & w _ {\ell + 1} \end{array} \right]\tag{7.53}
$$

Note that $Q _ { i , j } = Q _ { i - 1 , j - 1 }$ for all $i , j \in \{ 2 , \ldots , m \}$ , and thus convoluation is a matrix multiplication with parameter sharing. We also note that computing the convolution only takes $O ( k m )$ times but computing a generic matrix multiplication takes $O ( m ^ { 2 } )$ time. Convolution has $k$ parameters but generic matrix multiplication will have $m ^ { 2 }$ parameters. Thus convolution is supposed to be much more efficient than a generic matrix multiplication (as long as the additional structure imposed does not hurt the flexibility of the model to fit the data).

We also note that in practice there are many variants of the convolutional layers that we define here, e.g., there are other ways to pad zeros or sometimes the dimension of the output of the convolutional layers could be different from the input. We omit some of this subtleties here for simplicity.

The convolutional layers used in practice have also many “channels” and the simplified version above corresponds to the 1-channel version. Formally, Conv1D takes in $C$ vectors $z _ { 1 } , \ldots , z _ { C }   \in   \mathbb { R } ^ { m }$ as inputs, where $C$ is referred to as the number of channels. In other words, the more general version, denoted by Conv1D, takes in a matrix as input, which is the concatenation of $z _ { 1 } , \ldots , z _ { C }$ and has dimension $m \times C$ . It can output $C ^ { \prime }$ vectors of dimension $m$ , denoted by $\operatorname { C o n v 1 D } ( z ) _ { 1 } , \ldots , \operatorname { C o n v 1 D } ( z ) _ { C ^ { \prime } }$ , where $C ^ { \prime }$ is referred to as the output channel, or equivalently a matrix of dimension $m \times C ^ { \prime }$ . Each of the output is a sum of the simplified convolutions applied on various channels.

$$
\forall i \in [ C ^ {\prime} ], \mathrm{Conv1D} (z) _ {i} = \sum_ {j = 1} ^ {C} \mathrm{Conv1D-S} _ {i, j} (z _ {j}).\tag{7.54}
$$

Note that each Conv $\mathrm { 1 D - } \mathrm { S } _ { i , j }$ are modules with different parameters, and thus the total number of parameters is $k$ (the number of parameters in a $Conv1D-S) $\times C C ^ { \prime }$$ (the number of Conv $1D-S _{i.j}  's)   =   kCC'$ . In contrast, a generic linear mapping from $\mathbb { R } ^ { m \times C }$ and $\mathbb { R } ^ { m \times C ^ { \prime } }$ has $m ^ { 2 } C C ^ { \prime }$ parameters. The

<!-- page: 100 -->

parameters can also be represented as a three-dimensional tensor of dimension $k \times C \times C ^ { \prime }$

2-D convolution $( b r i e f )$ . A 2-D convolution with one channel, denoted by Conv2D-S, is analogous to the Conv1D-S, but takes a 2-dimensional input $z   \in   \mathbb { R } ^ { m \times m }$ and applies a filter of size $k \times k$ , and outputs $Conv2D-S (z)   \in$ $\mathbb { R } ^ { m \times m }$ The full 2-D convolutional layer, denoted by Conv2D, takes in a sequence of matrices $z _ { 1 } , \ldots , z _ { C } \in \mathbb { R } ^ { m \times m }$ , or equivalently a 3-D tensor $z ~ = ~ ( z _ { 1 } , \ldots , z _ { C } ) ~ \in ~ \mathbb { R } ^ { m \times m \times C }$ and outputs a sequence of matrices, $\mathrm { C o n v 2 D } ( z ) _ { 1 } , \ldots , \mathrm { C o n v 2 D } ( z ) _ { C ^ { \prime } } \in \mathbb { R } ^ { m \times m }$ , which can also be viewed as a 3D tensor in $\mathbb { R } ^ { m \times m \times C ^ { \prime } }$ Each channel of the output is sum of the outcomes of applying Conv2D-S layers on all the input channels.

$$
\forall i \in [ C ^ {\prime} ], \mathrm{Conv2D} (z) _ {i} = \sum_ {j = 1} ^ {C} \mathrm{Conv2D-S} _ {i, j} (z _ {j}).\tag{7.55}
$$

Because there are $C C ^ { \prime }$ number of Conv2D-S modules and each of the Conv2D-S module has $k ^ { 2 }$ parameters, the total number of parameters is $C C ^ { \prime } k ^ { 2 }$ . The parameters can also be viewed as a 4D tensor of dimension $C \times C ^ { \prime } \times k \times k$

Further reading. See Mazet [2026] for discussions of basic properties, theoretical properties such as the convolution theorem, and the connection between correlation and convolution in image processing.

## 7.4 Backpropagation

In this section, we introduce backpropagation or auto-differentiation, which computes the gradient of the loss $\nabla J ( \theta )$ efficiently. We will start with an informal theorem that states that as long as a real-valued function f can be efficiently computed/evaluated by a differentiable network or circuit, then its gradient can be efficiently computed in a similar time. We will then show how to do this concretely for neural networks.

Because the formality of the general theorem is not the main focus here, we will introduce the terms with informal definitions. By a differentiable circuit or a differentiable network, we mean a composition of a sequence of differentiable arithmetic operations (additions, subtraction, multiplication, divisions, etc) and elementary differentiable functions (ReLU, exp, log, sin, cos, etc.). Let the size of the circuit be the total number of such operations and elementary functions. We assume that each of the operations and func-

<!-- page: 101 -->

tions, and their derivatives or partial derivatives ecan be computed in $O ( 1 )$ time.

Theorem 7.4.1.: [backpropagation or auto-differentiation, informally stated] Suppose a differentiable circuit of size N computes a real-valued function $f : \mathbb { R } ^ { \ell } \to \mathbb { R }$ . Then, the gradient ∇f can be computed in time $O ( N )$ , by a circuit of size $O ( N )$ <sup>5</sup>

We note that the loss function $J ^ { ( j ) } ( \theta )$ for $j \mathrm { - t h }$ example can be indeed computed by a sequence of operations and functions involving additions, subtraction, multiplications, and non-linear activations. Thus the theorem suggests that we should be able to compute the $\nabla J ^ { ( j ) } ( \theta )$ in a similar time to that for computing $J ^ { ( j ) } ( \theta )$ itself. This does not only apply to the fullyconnected neural network introduced in the Section 7.2, but also many other types of neural networks that uses more advance modules.

We remark that auto-differentiation or backpropagation is already implemented in all the deep learning packages such as tensorflow and pytorch, and thus in practice, in most of cases a researcher does not need to write their backpropagation algorithms. However, understanding it is very helpful for gaining insights into the working of deep learning.

A useful corollary of the theorem above is that any scalar function of the gradient, say $s ( \nabla f ( x ) )$ , can still have efficiently computable gradient, even though the gradient of such a quantity implicitly involves second-order derivatives of $f .$ For example, one can compute the gradient of $\ell ( \theta - \eta \nabla \ell ( \theta ) )$ with respect to $\theta$ efficiently. Another corollary is that under the same setting and assuming the basic operations are twice differentiable, for any $v   \in   \mathbb { R } ^ { \ell }$ , the Hessian-vector product $\nabla ^ { 2 } f ( x ) v$ can also be computed in $O ( N + \ell )$ time. Indeed, let $g ( x )   =   \langle \nabla f ( x ) , v \rangle$ By the theorem above, $g ( x )$ can be computed in $O ( N + \ell )$ time, and by applying the theorem again, we obtain $\nabla g ( x ) = \nabla ^ { 2 } f ( x ) v$ in $O ( N + \ell )$ time as well. These facts are a basis for many second-order methods such as second-order optimization and meta learning, but we will not cover these topics in this course.

Organization of the rest of the section. In Section 7.4.1, we will start reviewing the basic chain rule with a new perspective that is particularly useful for understanding backpropagation. Section 7.4.2 will introduce the general

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">N ≤ \`,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">O N</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>We note if the output of the function f does not depend on some of the input coordinates, then we set by default the gradient with respect to that coordinate to zero. Setting to zero does not count towards the total runtime here in our accounting scheme. This is why when  we can compute the gradient in ( ) time, which might be potentially even less than \`.</span></small>

<!-- page: 102 -->

strategy for backpropagation. Section 7.4.3 will discuss how to compute the so-called backward function for basic modules used in neural networks, and Section 7.4.4 will put everything together to get a concrete backprop algorithm for MLPs.

## 7.4.1 Preliminaries on partial derivatives

Suppose a scalar variable J depends on some variables z (which could be a scalar, matrix, or high-order tensor), we write $\frac { \partial J } { \partial z }$ as the partial derivatives of $J$ with respect to the variable z. We stress that the convention here is that $\frac { \partial J } { \partial z }$ has exactly the same dimension as z itself. For example, $\mathrm { i f } ~ z   \in   \mathbb { R } ^ { m \times n }$ then $\begin{array} { r } { \frac { \partial \boldsymbol { J } } { \partial \boldsymbol { z } } \in \mathbb { R } ^ { \vec { m \times n } } } \end{array}$ , and the $( i , j )$ -entry of $\frac { \partial J } { \partial z }$ is equal to $\frac { \partial J } { \partial z _ { i j } }$

Remark 7.4.2.: When both J and z are not scalars, the partial derivatives of J with respect to z become either a matrix or tensor and the notation becomes somewhat tricky. Besides the mathematical or notational challenges in dealing with these partial derivatives of multivariate functions, they are also expensive to compute and store, and thus rarely explicitly constructed empirically. The experience of the authors of this note is that it’s generally more productive to think only about derivatives of scalar functions with respect to vectors, matrices, or tensors. For example, in this note, we will not deal with derivatives of multivariate functions.

Chain rule. We review the chain rule in calculus but with a perspective and notions that are more relevant for auto-differentiation.

Consider a scalar variable J which is obtained by the composition of f and g on some variable $之 ,$

$$
\begin{array}{l} z \in \mathbb {R} ^ {m} \\ u = g (z) \in \mathbb {R} ^ {n} \\ J = f (u) \in \mathbb {R}. \end{array}\tag{7.56}
$$

The same derivations below can be easily extend to the cases when z and u are matrices or tensors; but we insist that the final variable J is a scalar. (See also Remark 7.4.2.) Let $u = ( u _ { 1 } , \ldots , u _ { n } )$ and let $g ( z ) = ( g _ { 1 } ( z ) , \cdots , g _ { n } ( z ) )$ Then, the standard chain rule gives us that

$$
\forall i \in \{1, \dots , m \}, \quad \frac {\partial J}{\partial z _ {i}} = \sum_ {j = 1} ^ {n} \frac {\partial J}{\partial u _ {j}} \cdot \frac {\partial g _ {j}}{\partial z _ {i}}.\tag{7.57}
$$

<!-- page: 103 -->

Alternatively, when z and u are both vectors, in a vectorized notation:

$$
\frac {\partial J}{\partial z} = \left[ \begin{array}{c c c} \frac {\partial g _ {1}}{\partial z _ {1}} & \dots & \frac {\partial g _ {n}}{\partial z _ {1}} \\ \vdots & \ddots & \vdots \\ \frac {\partial g _ {1}}{\partial z _ {m}} & \dots & \frac {\partial g _ {n}}{\partial z _ {m}} \end{array} \right] \cdot \frac {\partial J}{\partial u}.\tag{7.58}
$$

In other words, the backward function is always a linear map from $\frac { \partial J } { \partial u }$ to $\frac { \partial J } { \partial z }$ , though note that the mapping itself can depend on z in complex ways. The matrix on the RHS of (7.58) is actually the transpose of the Jacobian matrix of the function $g .$ However, we do not discuss in-depth about Jacobian matrices to avoid complications. Part of the reason is that when z is a matrix (or tensor), to write an analog of equation (7.58), one has to either flatten z into a vector or introduce additional notations on tensor-matrix product. In this sense, equation (7.57) is more convenient and effective to use in all cases. For example, when $z \in \mathbb { R } ^ { r \times s }$ is a matrix, we can easily rewrite equation (7.57) to

$$
\forall i, k, \quad \frac {\partial J}{\partial z _ {i k}} = \sum_ {j = 1} ^ {n} \frac {\partial J}{\partial u _ {j}} \cdot \frac {\partial g _ {j}}{\partial z _ {i k}}.\tag{7.59}
$$

which will indeed be used in some of the derivations in Section 7.4.3.

Key interpretation of the chain rule. We can view the formula above (equation (7.57) or (7.58)) as a way to compute $\frac { \partial J } { \partial z }$ from $\frac { \partial J } { \partial u }$ . Consider the following abstract problem. Suppose $J$ depends on z via u as defined in equation (7.56). However, suppose the function $f$ is not given or the function $f$ is complex, but we are given the value of $\frac { \partial \boldsymbol { J } ^ { \cdot } } { \partial y _ { i } }$ Then, the formula in equation (7.58) gives us a way to compute $\frac { \partial J } { \partial z }$ from ∂J. $\frac { \partial \sigma } { \partial u }$

$$
\frac {\partial J}{\partial u} \quad \xrightarrow [ \text {only requires info about $g(\cdot)$ and $z$} ]{\text {chain rule, formula (7.58)}} \quad \frac {\partial J}{\partial z}.\tag{7.60}
$$

Moreover, this formula only involves knowledge about $g$ (more precisely $\frac { \partial g _ { j } } { \partial z _ { i } } )$ . We will repeatedly use this fact in situations where $g$ is a building blocks of a complex network $f .$

Empirically, it’s often useful to modularized the mapping in (7.57) or (7.58) into a black-box, and mathematically it’s also convenient to define a notation for it. We use $\mathcal { B } [ g , z ]$ to define the function that maps $\frac { \partial J } { \partial u }$ to $\frac { \partial J } { \partial z }$ , and write

$$
\frac {\partial J}{\partial z} = \mathcal {B} [ g, z ] \left(\frac {\partial J}{\partial u}\right).\tag{7.61}
$$

<!-- page: 104 -->

We call $\mathcal { B } [ g , z ]$ the backward function for the module $g .$ Note that when z is fixed, $\mathcal { B } [ g , z ]$ is merely a linear map from $\mathbb { R } ^ { n }$ to $\mathbb { R } ^ { m }$ . Using equation (7.57), we have

$$
(\mathcal {B} [ g, z ] (v)) _ {i} = \sum_ {j = 1} ^ {m} \frac {\partial g _ {j}}{\partial z _ {i}} \cdot v _ {j}  .\tag{7.62}
$$

Or in vectorized notation, using (7.58), we have

$$
\mathcal {B} [ g, z ] (v) = \left[ \begin{array}{c c c} \frac {\partial g _ {1}}{\partial z _ {1}} & \dots & \frac {\partial g _ {n}}{\partial z _ {1}} \\ \vdots & \ddots & \vdots \\ \frac {\partial g _ {1}}{\partial z _ {m}} & \dots & \frac {\partial g _ {n}}{\partial z _ {m}} \end{array} \right] \cdot v.\tag{7.63}
$$

and therefore $\mathcal { B } [ g , z ]$ can be viewed as a matrix. However, in reality, z will be changing and thus the backward mapping has to be recomputed for different z’s while $g$ is often fixed. Thus, empirically, the backward function $\mathcal { B } [ g , z ] ( v )$ is often viewed as a function which takes in z (=the input to $g )$ and $v ( { = } \mathrm { a }$ vector that is supposed to be the gradient of some variable J with respect to the output of $g )$ as the inputs, and outputs a vector that is supposed to be the gradient of J with respect to z.

## 7.4.2 General strategy of backpropagation

We discuss the general strategy of auto-differentiation in this section to build a high-level understanding. Then, we will instantiate the approach to concrete neural networks. We take the viewpoint that neural networks are complex compositions of small building blocks such as MM, $\sigma ,$ Conv2D, LN, etc., defined in Section 7.3. Note that the losses (e.g., mean-squared loss, or the cross-entropy loss) can also be abstractly viewed as additional modules. Thus, we can abstractly write the loss function J (on a single example $( x , y ) )$ as a composition of many modules:<sup>6</sup>

$$
J = M _ {k} (M _ {k - 1} (\dots M _ {1} (x))).\tag{7.64}
$$

For example, for a binary classification problem with a MLP $\bar { h } _ { \theta } ( x )$ (defined in equation (7.39) and (7.40)), the loss function has ber written in the form of equation (7.64) with $M _ { 1 }   =   \mathrm { M M } _ { W ^ { [ 1 ] } , b ^ { [ 1 ] } } , \; M _ { 2 }   =   \sigma , \; M _ { 3 }   =   \mathrm { M M } _ { W ^ { [ 2 ] } , b ^ { [ 2 ] } }$. . . , and $M _ { k - 1 } = \mathrm { M M } _ { W ^ { [ r ] } , b ^ { [ r ] } }$ and $M _ { k } = \ell _ { \mathrm { l o g i s t i c } }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">= k( <sub>k−1</sub>(· · · 1(x)), y)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Mk</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>Technically, we should write J  M M M . However, y is treated as a constant for the purpose of computing the derivatives with respect to the parameters, and thus we can view it as part of for the sake of simplicity of notations.</span></small>

<!-- page: 105 -->

We can see from this example that some modules involve parameters, and other modules might only involve a fixed set of operations. For generality, we assume that eachj $M _ { i }$ involves a set of parameters $\theta ^ { [ i ] }$ , though $\theta ^ { [ i ] }$ could possibly be an empty set when $M _ { i }$ is a fixed operation such as the nonlinear activations. We will discuss more on the granularity of the modularization, but so far we assume all the modules $M _ { i }$ ’s are simple enough.

We introduce the intermediate variables for the computation in (7.64). Let

$$
\begin{array}{c} u ^ {[ 0 ]} = x \\ u ^ {[ 1 ]} = M _ {1} (u ^ {[ 0 ]}) \\ u ^ {[ 2 ]} = M _ {2} (u ^ {[ 1 ]}) \\ \vdots \\ J = u ^ {[ k ]} = M _ {k} (u ^ {[ k - 1 ]}). \end{array}\tag{F}
$$

Backpropagation consists of two passes, the forward pass and backward pass. In the forward pass, the algorithm simply computes $u ^ { [ 1 ] } , \ldots , u ^ { [ k ] }$ from $i   =   1 , \ldots , k$ , sequentially using the definition in (F), and saves all the intermediate variables $u ^ { [ i ] } !$ ’s in the memory.

In the backward pass, we first compute the derivatives with respect to the intermediate variables, that is, $\begin{array} { r } { \overline { { \frac { \partial J } { \partial u ^ { [ k ] } } } } , \ldots , \frac { \partial J } { \partial u ^ { [ 1 ] } } } \end{array}$ , sequentially in this backward order, and then compute the derivatives of the parameters $\frac { \partial J } { \partial \theta ^ { [ i ] } }$ from $\frac { \partial J } { \partial u ^ { [ i ] } }$ and $u ^ { [ i - 1 ] }$ . These two types of computations can also be interleaved with each other because $\frac { \partial J } { \partial \theta ^ { [ i ] } }$ only depends on $\frac { \partial J } { \partial u ^ { [ i ] } }$ and $u ^ { [ i - 1 ] }$ but not any $\frac { \partial J } { \partial u ^ { [ k ] } }$ with $k < i$

We first see why $\frac { \partial J } { \partial u ^ { [ i - 1 ] } }$ can be computed efficiently from $\frac { \partial J } { \partial u ^ { [ i ] } }$ and $u ^ { [ i ] }$ −1] by invoking the discussion in Section 7.4.1 on the chain rule. We instantiate the discussion by setting $u = u ^ { [ i ] }$ and $z = u ^ { [ i - 1 ] }$ , and $f(u) =$ $M _ { k } ( M _ { k - 1 } ( \cdots M _ { i + 1 } ( u ^ { [ i ] } ) ) )$ , and $g ( \cdot ) \; = \; M _ { i } ( \cdot )$ . Note that f is very complex but we don’t need any concrete information about $f .$ Then, the conclusive equation (7.60) corresponds to

$$
\frac {\partial J}{\partial u ^ {[ i ]}} \quad \xrightarrow [ \text {only requires info about} M _ {i} (\cdot) \text {and} u ^ {[ i - 1 ]} ]{\text {chain rule}} \quad \frac {\partial J}{\partial u ^ {[ i - 1 ]}}.\tag{7.65}
$$

More precisely, we can write, following equation (7.61)

$$
\frac {\partial J}{\partial u ^ {[ i - 1 ]}} = \mathcal {B} [ M _ {i}, u ^ {[ i - 1 ]} ] \left(\frac {\partial J}{\partial u ^ {[ i ]}}\right).\tag{B1}
$$

<!-- page: 106 -->

Instantiating the chain rule with $z = \theta ^ { [ i ] }$ and $u = u ^ { [ i ] }$ , we also have

$$
\frac {\partial J}{\partial \theta^ {[ i ]}} = \mathcal {B} [ M _ {i}, \theta^ {[ i ]} ] \left(\frac {\partial J}{\partial u ^ {[ i ]}}\right)  .\tag{B2}
$$

See Figure 7.5 for an illustration of the algorithm.

Remark 7.4.3.: [Computational efficiency and granularity of the modules] The main underlying purpose of treating a complex network as compositions of small modules is that small modules tend to have efficiently implementable backward functions. In fact, the backward functions of all the atomic modules such as addition, multiplication and ReLU can be computed as efficiently as the evaluation of these modules (up to multiplicative constant factor). Using this fact, we can prove Theorem 7.4.1 by viewing neural networks as compositions of many atomic operations, and invoking the backpropagation discussed above. However, in practice, it’s oftentimes more convenient to modularize the networks using modules on the level of matrix multiplication, layernorm, etc. As we will see, naive implementation of these operations backward functions also have the same runtime as the evaluation of these functions.

<!-- page: 107 -->

![](images/page_106_image_1.jpg)

Figure 7.5: Back-propagation through a composition of modules. Illustration of layerwise forward and backward computation in a compositional model with modules $M _ { 1 } , \ldots , M _ { k }$ . In the forward pass (left), the input $x = u ^ { [ 0 ] }$ is propagated upward through the modules, producing intermediate activations $\widetilde { u ^ { [ 1 ] } , u ^ { [ 2 ] } , \ldots , u ^ { [ k - 1 ] } }$ and finally the loss $J$ at the top. In the backward pass for activation derivatives (middle), backpropagation starts from $\partial J / \partial J = 1$ and recursively applies the local backward operator $\mathcal { B } [ M _ { \ell } , u ^ { [ \ell - }$ 1]] to transform the upstream derivative $\partial J / \partial u ^ { [ \ell ] }$ into the derivative with respect to the previous activation, $\partial J / \partial u ^ { [ \ell - 1 ] }$ . In parallel, the backward pass for parameter gradients (right) uses the same local information at each layer to compute the gradient with respect to that layer’s parameters via $\mathcal { B } [ M _ { \ell } , \theta ^ { [ \ell ] } ]$ yielding $\partial J / \partial \theta ^ { [ \ell ] }$

## 7.4.3 Backward functions for basic modules

Using the general strategy in Section 7.4.2, it suffices to compute the backward function for all modules $M _ { i } { } ^ { \flat } \mathrm { s }$ used in the networks. We compute the backward function for the basic module MM, activations $\sigma ,$ and loss functions in this section.

Backward function for MM. Suppose $\mathrm { M M } _ { W , b } ( z ) = W z + b$ is a matrix multi-

<!-- page: 108 -->

plication module where $z \in \mathbb { R } ^ { m }$ and $W \in \mathbb { R } ^ { n \times m }$ . Then, using equation (7.63), we have for $v \in \mathbb { R } ^ { n }$

$$
\mathcal {B} [ \mathrm{MM}, z ] (v) = \left[ \begin{array}{c c c} \frac {\partial (W z + b) _ {1}}{\partial z _ {1}} & \dots & \frac {\partial (W z + b) _ {n}}{\partial z _ {1}} \\ \vdots & \ddots & \vdots \\ \frac {\partial (W z + b) _ {1}}{\partial z _ {m}} & \dots & \frac {\partial (W z + b) _ {n}}{\partial z _ {m}} \end{array} \right] v  .\tag{7.66}
$$

Using the fact that $\begin{array} { r } { \forall i   \in   [ m ] , j   \in   [ n ] { , } \frac { \partial ( W z + b ) _ { j } } { \partial z _ { i } }   =   \frac { \partial b _ { j } + \sum _ { k = 1 } ^ { m } W _ { j k } z _ { k } } { \partial z _ { i } }   =   W _ { j i } } \end{array}$ , we have

$$
\mathcal {B} [ \mathrm{MM}, z ] (v) = W ^ {\top} v \in \mathbb {R} ^ {m}.\tag{7.67}
$$

In the derivation above, we have treated MM as a function of z. If we treat MM as a function of W and b, then we can also compute the backward function for the parameter variables W and b. It’s less convenient to use equation (7.63) because the variable W is a matrix and the matrix in (7.63) will be a 4-th order tensor that is challenging for us to mathematically write down. We use (7.62) instead:

$$
(\mathcal {B} [ \mathrm{MM}, W ] (v)) _ {i j} = \sum_ {k = 1} ^ {m} \frac {\partial (W z + b) _ {k}}{\partial W _ {i j}} \cdot v _ {k} = \sum_ {k = 1} ^ {m} \frac {\partial \sum_ {s = 1} ^ {m} W _ {k s} z _ {s}}{\partial W _ {i j}} \cdot v _ {k} = v _ {i} z _ {j}.\tag{7.68}
$$

In vectorized notation, we have

$$
\mathcal {B} [ \mathrm{MM}, W ] (v) = v z ^ {\top} \in \mathbb {R} ^ {n \times \times m}.\tag{7.69}
$$

Using equation (7.63) for the variable b, we have,

$$
\mathcal {B} [ \mathrm{MM}, b ] (v) = \left[ \begin{array}{c c c} \frac {\partial (W z + b) _ {1}}{\partial b _ {1}} & \dots & \frac {\partial (W z + b) _ {n}}{\partial b _ {1}} \\ \vdots & \ddots & \vdots \\ \frac {\partial (W z + b) _ {1}}{\partial b _ {n}} & \dots & \frac {\partial (W z + b) _ {n}}{\partial b _ {n}} \end{array} \right] v = v  .\tag{7.70}
$$

Here we used that $\begin{array} { r } { \frac { \partial ( W z + b ) _ { j } } { \partial b _ { i } } = 0 \mathrm { ~ i f ~ } i \neq j } \end{array}$ and $\begin{array} { r } { \frac { \partial ( W z + b ) _ { j } } { \partial b _ { i } } = 1 } \end{array}$ if $i = j$

The computational efficiency for computing the backward function is $O ( m n )$ , the same as evaluating the result of matrix multiplication up to constant factor.

Backward function for the activations. Suppose $M ( z ) = \sigma ( z )$ where σ is an element-wise activation function and $z \in \mathbb { R } ^ { m }$ . Then, using equation (7.63),

<!-- page: 109 -->

we have

$$
\mathcal {B} [ \sigma , z ] (v) = \left[ \begin{array}{c c c} \frac {\partial \sigma (z _ {1})}{\partial z _ {1}} & \dots & \frac {\partial \sigma (z _ {m})}{\partial z _ {1}} \\ \vdots & \ddots & \vdots \\ \frac {\partial \sigma (z _ {1})}{\partial z _ {m}} & \dots & \frac {\partial \sigma (z _ {m})}{\partial z _ {m}} \end{array} \right] v\tag{7.71}
$$

$$
= \mathrm{diag} (\sigma^ {\prime} (z _ {1}), \dots , \sigma^ {\prime} (z _ {m})) v\tag{7.72}
$$

$$
= \sigma^ {\prime} (z) \odot v \in \mathbb {R} ^ {m}.\tag{7.73}
$$

Here, we used the fact that $\begin{array} { r } { \frac { \partial \sigma ( z _ { j } ) } { \partial z _ { i } } = 0 } \end{array}$ when $j \neq i, \mathrm{diag}(\lambda_1, \ldots, \lambda_m)$ denotes the diagonal matrix with $\lambda _ { 1 } , \ldots , \lambda _ { m }$ on the diagonal, and $\odot$ denotes the element-wise product of two vectors with the same dimension, and $\sigma ^ { \prime } ( \cdot )$ is the element-wise application of the derivative of the activation function σ.

Regarding computation efficiency, we note that at the first sight, equation (7.71) appears to indicate the backward function takes $O ( m ^ { 2 } )$ time, but equation (7.73) shows that it’s implementable in $O ( m )$ time (which is the same as the time for evaluating of the function.) We are not supposed to be surprised by that the possibility of simplifying equation (7.71) to (7.73)—if we use smaller modules, that is, treating the vector-to-vector nonlinear activation as m scalar-to-scalar non-linear activation, then it’s more obvious that the backward pass should have similar time to the forward pass.

Backward function for loss functions. When a module M takes in a vector z and outputs a scalar, by equation (7.63), the backward function takes in a scalar v and outputs a vector with entries $( \mathcal { B } [ M , z ] ( v ) ) _ { i } = \textstyle \frac { \partial M } { \partial z _ { i } } v$ . Therefore, in vectorized notation, $\begin{array} { r } { \mathcal { B } [ M , z ] ( v ) = \frac { \partial M } { \partial z } \cdot v } \end{array}$

Recall that squared loss $\ell _ { \mathrm { M S E } } ( z , \tilde { y ) } =   \textstyle { \frac { 1 } { 2 } } ( z   -   y ) ^ { 2 }$ . Thus, $\mathcal { B } [ \ell _ { \mathrm { M S E } } , z ] ( v )   =$ $\begin{array} { r } { \frac { \partial \frac { 1 } { 2 } ( z - y ) ^ { 2 } } { \partial z } \cdot v = ( z - y ) \cdot v . } \end{array}$

For logistics loss, by equation (2.6), we have

$$
\mathcal {B} [ \ell_ {\mathrm{logistic}}, t ] (v) = \frac {\partial \ell_ {\mathrm{logistic}} (t , y)}{\partial t} \cdot v = (1 / (1 + \exp (- t)) - y) \cdot v.\tag{7.74}
$$

For cross-entropy loss, by equation (2.17), we have

$$
\mathcal {B} [ \ell_ {\mathrm{ce}}, t ] (v) = \frac {\partial \ell_ {\mathrm{ce}} (t , y)}{\partial t} \cdot v = (\phi - e _ {y}) \cdot v,\tag{7.75}
$$

where $\phi = \mathrm { s o f t m a x } ( t )$

<!-- page: 110 -->

## 7.4.4 Back-propagation for MLPs

Given the backward functions for every module needed in evaluating the loss of an MLP, we follow the strategy in Section 7.4.2 to compute the gradient of the loss with respect to the hidden activations and the parameters.

We consider the an r-layer MLP with a logistic loss. The loss function can be computed via a sequence of operations (that is, the forward pass),

$$
\begin{array}{c} z ^ {[ 1 ]} = \mathrm{MM} _ {W ^ {[ 1 ]}, b ^ {[ 1 ]}} (x), \\ a ^ {[ 1 ]} = \sigma (z ^ {[ 1 ]}) \\ z ^ {[ 2 ]} = \mathrm{MM} _ {W ^ {[ 2 ]}, b ^ {[ 2 ]}} (a ^ {[ 1 ]}) \\ a ^ {[ 2 ]} = \sigma (z ^ {[ 2 ]}) \\ \vdots \\ z ^ {[ r ]} = \mathrm{MM} _ {W ^ {[ r ]}, b ^ {[ r ]}} (a ^ {[ r - 1 ]}) \\ J = \ell_ {\mathrm{logistic}} (z ^ {[ r ]}, y). \end{array}\tag{7.76}
$$

We apply the backward function sequentially in a backward order. First, we have that

$$
\frac {\partial J}{\partial z ^ {[ r ]}} = \mathcal {B} [ \ell_ {\mathrm{logistic}}, z ^ {[ r ]} ] \left(\frac {\partial J}{\partial J}\right) = \mathcal {B} [ \ell_ {\mathrm{logistic}}, z ^ {[ r ]} ] (1).\tag{7.77}
$$

Then, we iteratively compute $\frac { \partial J } { \partial a ^ { [ i ] } }$ and $\frac { \partial J } { \partial z ^ { [ i ] } } \mathrm { { ^ \prime S } }$ by repeatedly invoking the chain rule (equation (7.62)),

$$
\begin{array}{c} \frac {\partial J}{\partial a ^ {[ r - 1 ]}} = \mathcal {B} [ \mathrm{MM}, a ^ {[ r - 1 ]} ] \left(\frac {\partial J}{\partial z ^ {[ r ]}}\right) \\ \frac {\partial J}{\partial z ^ {[ r - 1 ]}} = \mathcal {B} [ \sigma , z ^ {[ r - 1 ]} ] \left(\frac {\partial J}{\partial a ^ {[ r - 1 ]}}\right) \\ \vdots \\ \frac {\partial J}{\partial z ^ {[ 1 ]}} = \mathcal {B} [ \sigma , z ^ {[ 1 ]} ] \left(\frac {\partial J}{\partial a ^ {[ 1 ]}}\right). \end{array}\tag{7.78}
$$

Numerically, we compute these quantities by repeatedly invoking equations (7.73) and (7.67) with different choices of variables.

We note that the intermediate values of $a ^ { [ i ] }$ and $z ^ { [ i ] }$ are used in the backpropagation (equation (7.78)), and therefore these values need to be stored in the memory after the forward pass.

<!-- page: 111 -->

Next, we compute the gradient of the parameters by invoking equations (7.69) and (7.70),

$$
\frac {\partial J}{\partial W ^ {[ r ]}} = \mathcal {B} [ \mathrm{MM}, W ^ {[ r ]} ] \left(\frac {\partial J}{\partial z ^ {[ r ]}}\right)
$$

$$
\frac {\partial J}{\partial b ^ {[ r ]}} = \mathcal {B} [ \mathrm{MM}, b ^ {[ r ]} ] \left(\frac {\partial J}{\partial z ^ {[ r ]}}\right)
$$

$$
\frac {\partial J}{\partial W ^ {[ 1 ]}} = \mathcal {B} [ \mathrm{MM}, W ^ {[ 1 ]} ] \left(\frac {\partial J}{\partial z ^ {[ 1 ]}}\right)
$$

$$
\frac {\partial J}{\partial b ^ {[ 1 ]}} = \mathcal {B} [ \mathrm{MM}, b ^ {[ 1 ]} ] \left(\frac {\partial J}{\partial z ^ {[ 1 ]}}\right).\tag{7.79}
$$

We also note that the block of computations in equations (7.79) can be interleaved with the block of computation in equations (7.78) because the $\frac { \partial J } { \partial W ^ { [ i ] } }$ and $\frac { \partial J } { \partial b ^ { [ i ] } }$ can be computed as soon as $\frac { \partial J } { \partial z ^ { [ i ] } }$ is computed.

Putting all of these together, and explicitly invoking the equations (7.76), (7.78) and (7.79), we have the following algorithm (Algorithm 3).

<!-- page: 112 -->

Algorithm 3 Back-propagation for multi-layer neural networks.

1: Forward pass. Compute and store the values of $a ^ { [ k ] }   \mathrm { ` s , ~ } z ^ { [ k ] }   \mathrm { ` s }$ , and J using the equations (7.76).

2: Backward pass. Compute the gradient of loss J with respect to $z ^ { [ r ] }$ :

$$
\frac {\partial J}{\partial z ^ {[ r ]}} = \mathcal {B} [ \ell_ {\mathrm{logistic}}, z ^ {[ r ]} ] (1) = \left(1 / (1 + \exp (- z ^ {[ r ]})) - y\right).\tag{7.80}
$$

3: for $k = r - 1$ to 0 do

4: Compute the gradient with respect to parameters $W ^ { [ k + 1 ] }$ and $b ^ { [ k + 1 ] }$

$$
\begin{array}{r l} & {\frac {\partial J}{\partial W ^ {[ k + 1 ]}} = \mathcal {B} [ \mathrm{MM}, W ^ {[ k + 1 ]} ] \left(\frac {\partial J}{\partial z ^ {[ k + 1 ]}}\right)} \\ & {\qquad = \frac {\partial J}{\partial z ^ {[ k + 1 ]}} a ^ {[ k ] ^ {\top}}.} \\ & {\qquad \frac {\partial J}{\partial b ^ {[ k + 1 ]}} = \mathcal {B} [ \mathrm{MM}, b ^ {[ k + 1 ]} ] \left(\frac {\partial J}{\partial z ^ {[ k + 1 ]}}\right)} \\ & {\qquad = \frac {\partial J}{\partial z ^ {[ k + 1 ]}}.} \end{array}\tag{7.81}
$$

(7.82)

5: When $k \geq 1$ , compute the gradient with respect to $z ^ { [ k ] }$ and $a ^ { [ k ] }$

$$
\begin{array}{c} \frac {\partial J}{\partial a ^ {[ k ]}} = \mathcal {B} [ \sigma , a ^ {[ k ]} ] \left(\frac {\partial J}{\partial z ^ {[ k + 1 ]}}\right) \\ = W ^ {[ k + 1 ] ^ {\top}} \frac {\partial J}{\partial z ^ {[ k + 1 ]}}. \end{array}\tag{7.83}
$$

$$
\begin{array}{c} \frac {\partial J}{\partial z ^ {[ k ]}} = \mathcal {B} [ \sigma , z ^ {[ k ]} ] \left(\frac {\partial J}{\partial a ^ {[ k ]}}\right) \\ = \sigma^ {\prime} (z ^ {[ k ]}) \odot \frac {\partial J}{\partial a ^ {[ k ]}}. \end{array}\tag{7.84}
$$

## 7.5 Vectorization over training examples

As we discussed in Section 7.1, in the implementation of neural networks, we will leverage the parallelism across the multiple examples. This means that we will need to write the forward pass (the evaluation of the outputs) of the neural network and the backward pass (backpropagation) for multiple

<!-- page: 113 -->

training examples in matrix notation.

The basic idea. The basic idea is simple. Suppose you have a training set with three examples $x ^ { ( 1 ) } , x ^ { ( 2 ) } , x ^ { ( 3 ) }$ . The first-layer activations for each example are as follows:

$$
\begin{array}{r} z ^ {[ 1 ] (1)} = W ^ {[ 1 ]} x ^ {(1)} + b ^ {[ 1 ]} \\ z ^ {[ 1 ] (2)} = W ^ {[ 1 ]} x ^ {(2)} + b ^ {[ 1 ]} \\ z ^ {[ 1 ] (3)} = W ^ {[ 1 ]} x ^ {(3)} + b ^ {[ 1 ]} \end{array}
$$

Note the difference between square brackets [·], which refer to the layer number, and parenthesis (·), which refer to the training example number. Intuitively, one would implement this using a for loop. It turns out, we can vectorize these operations as well. First, define:

$$
X = \left[ \begin{array}{c c c} | & | & | \\ x ^ {(1)} & x ^ {(2)} & x ^ {(3)} \\ | & | & | \end{array} \right] \in \mathbb {R} ^ {d \times 3}\tag{7.85}
$$

Note that we are stacking training examples in columns and not rows. We can then combine this into a single unified formulation:

$$
Z ^ {[ 1 ]} = \left[ \begin{array}{c c c} | & | & | \\ z ^ {[ 1 ] (1)} & z ^ {[ 1 ] (2)} & z ^ {[ 1 ] (3)} \\ | & | & | \end{array} \right] = W ^ {[ 1 ]} X + b ^ {[ 1 ]}\tag{7.86}
$$

You may notice that we are attempting to add $b ^ { [ 1 ] } \in \mathbb { R } ^ { 4 \times 1 }$ to $W ^ { [ 1 ] } X \in$ $\mathbb { R } ^ { 4 \times 3 }$ . Strictly following the rules of linear algebra, this is not allowed. In practice however, this addition is performed using broadcasting. We create an intermediate $\tilde { \tilde { b } } ^ { [ 1 ] } \in \mathbb { R } ^ { 4 \times 3 }$

$$
\tilde {b} ^ {[ 1 ]} = \left[ \begin{array}{c c c} | & | & | \\ b ^ {[ 1 ]} & b ^ {[ 1 ]} & b ^ {[ 1 ]} \\ | & | & | \end{array} \right]\tag{7.87}
$$

We can then perform the computation: $Z ^ { [ 1 ] } = W ^ { [ 1 ] } X + \tilde { b } ^ { [ 1 ] }$ . Often times, it is not necessary to explicitly construct $\tilde { b } ^ { [ 1 ] }$ . By inspecting the dimensions in (7.86), you can assume $b ^ { [ 1 ] } \in \mathbb { R } ^ { 4 \times 1 }$ is correctly broadcast to $W ^ { [ 1 ] } X \in \mathbb { R } ^ { 4 \times 3 }$

The matricization approach as above can easily generalize to multiple layers, with one subtlety though, as discussed below.

<!-- page: 114 -->

Complications/Subtlety in the Implementation. All the deep learn ing packages or implementations put the data points in the rows of a data matrix. (If the data point itself is a matrix or tensor, then the data are concentrated along the zero-th dimension.) However, most of the deep learning papers use a similar notation to these notes where the data points are treated as column vectors.<sup>7</sup> There is a simple conversion to deal with the mismatch: in the implementation, all the columns become row vectors, row vectors become column vectors, all the matrices are transposed, and the orders of the matrix multiplications are flipped. In the example above, using the row major convention, the data matrix is $X \in \mathbb { R } ^ { 3 \times d }$ , the first layer weight matrix has dimensionality $d \times m$ (instead of $m \times d$ as in the two layer neural net section), and the bias vector $b ^ { [ 1 ] }   \in   \mathbb { R } ^ { 1 \times m }$ The computation for the hidden activation becomes

$$
Z ^ {[ 1 ]} = X W ^ {[ 1 ]} + b ^ {[ 1 ]} \in \mathbb {R} ^ {3 \times m}\tag{7.88}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>The instructor suspects that this is mostly because in mathematics we naturally multiply a matrix to a vector on the left hand side.</span></small>

<!-- page: 115 -->

Part III

Generalization and regularization

<!-- page: 116 -->

## Chapter 8

## Generalization

This chapter discusses tools to analyze and understand the generalization of machine learning models, i.e, their performances on unseen test examples. Recall that for supervised learning problems, given a training dataset $\{ ( x ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { n }$ , we typically learn a model $h _ { \theta }$ by minimizing a loss/cost function $J ( \theta )$ , which encourages $h _ { \theta }$ to fit the data. E.g., when the loss function is the least square loss (aka mean squared error), we have $\begin{array} { r } { J ( \theta )   =   \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( y ^ { ( i ) }   -   h _ { \theta } ( x ^ { ( i ) } ) ) ^ { 2 } } \end{array}$ . This loss function for training purposes is oftentimes referred to as the training loss/error/cost.

However, minimizing the training loss is not our ultimate goal—it is merely our approach towards the goal of learning a predictive model. The most important evaluation metric of a model is the loss on unseen test examples, which is oftentimes referred to as the test error. Formally, we sample a test example $( x , y )$ from the so-called test distribution D, and measure the model’s error on it, by, e.g., the mean squared error, $( h _ { \theta } ( x ) - y ) ^ { 2 }$ . The expected loss/error over the randomness of the test example is called the test loss/error,<sup>1</sup>

$$
L (\theta) = \mathbb {E} _ {(x, y) \sim \mathcal {D}} [ (y - h _ {\theta} (x)) ^ {2} ]\tag{8.1}
$$

Note that the measurement of the error involves computing the expectation, and in practice, it can be approximated by the average error on many sampled test examples, which are referred to as the test dataset. Note that the key difference here between training and test datasets is that the test examples

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">{(x(i), y(i))}ni=1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">b</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>In theoretical and statistical literature, we oftentimes call the uniform distribution over the training set , denoted by D, an empirical distribution, and call D the population distribution. Partly because of this, the training loss is also referred to as the empirical loss/risk/error, and the test loss is also referred to as the population loss/risk/error.</span></small>

<!-- page: 117 -->

are unseen, in the sense that the training procedure has not used the test examples. In classical statistical learning settings, the training examples are also drawn from the same distribution as the test distribution D, but still the test examples are unseen by the learning procedure whereas the training examples are seen.<sup>2</sup>

Because of this key difference between training and test datasets, even if they are both drawn from the same distribution D, the test error is not necessarily always close to the training error.<sup>3</sup> As a result, successfully minimizing the training error may not always lead to a small test error. We typically say the model overfits the data if the model predicts accurately on the training dataset but doesn’t generalize well to other test examples, that is, if the training error is small but the test error is large. We say the model underfits the data if the training error is relatively large<sup>4</sup>(and in this case, typically the test error is also relatively large.)

This chapter studies how the test error is influenced by the learning procedure, especially the choice of model parameterizations. We will decompose the test error into “bias” and “variance” terms and study how each of them is affected by the choice of model parameterizations and their tradeoffs. Using the bias-variance tradeoff, we will discuss when overfitting and underfitting will occur and be avoided. We will also discuss the double descent phe nomenon in Section 8.2 and some classical theoretical results in Section 8.3.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>These days, researchers have increasingly been more interested in the setting with “domain shift”, that is, the training distribution and test distribution are different.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>the difference between test error and training error is often referred to as the generalization gap. The term generalization error in some literature means the test error, and in some other literature means the generalization gap.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4<sub>e</sub>.g., larger than the intrinsic noise level of the data in regression problems.</span></small>

<!-- page: 118 -->

## 8.1 Bias-variance tradeoff

![](images/page_117_chart_2.jpg)

![](images/page_117_chart_3.jpg)

Figure 8.1: A running example of training and test dataset for this section.

As an illustrating example, we consider the following training dataset and test dataset, which are also shown in Figure 8.1. The training inputs $x ^ { ( i ) } \mathrm { ^ { \prime } s }$ are randomly chosen and the outputs $y ^ { ( i ) }$ are generated by $\bar { y ^ { ( i ) } } = \bar { h ^ { \star } } ( x ^ { ( i ) } ) + \xi ^ { ( i ) }$ where the function $h ^ { \star } ( \cdot )$ is a quadratic function and is shown in Figure 8.1 as the solid line, and $\xi ^ { ( i ) }$ is the a observation noise assumed to be generated from $\sim \; N ( 0 , \sigma ^ { 2 } )$ . A test example $( x , y )$ also has the same input-output relationship $y = h ^ { \star } ( x ) + \xi$ where $\xi \sim N ( 0 , \sigma ^ { 2 } )$ . It’s impossible to predict the noise ξ, and therefore essentially our goal is to recover the function $h ^ { \star } ( \cdot )$

We will consider the test error of learning various types of models. When talking about linear regression, we discussed the problem of whether to fit a “simple” model such as the linear $\text{" } y   =   \theta_{0} + \theta_{1}x  ,$ or a more “complex” model such as the polynomial $`` y = \theta_{0} + \theta_{1}x + \cdots \theta_{5}x^{5}.$

We start with fitting a linear model, as shown in Figure 8.2. The best fitted linear model cannot predict y from x accurately even on the training dataset, let alone on the test dataset. This is because the true relationship between y and x is not linear—any linear model is far away from the true function $h ^ { \star } ( \cdot )$ . As a result, the training error is large and this is a typical situation of underfitting.

<!-- page: 119 -->

![](images/page_118_chart_1.jpg)

![](images/page_118_chart_2.jpg)

Figure 8.2: The best fit linear model has large training and test errors.

The issue cannot be mitigated with more training examples—even with a very large amount of, or even infinite training examples, the best fitted linear model is still inaccurate and fails to capture the structure of the data (Figure 8.3). Even if the noise is not present in the training data, the issue still occurs (Figure 8.4). Therefore, the fundamental bottleneck here is the linear model family’s inability to capture the structure in the data—linear models cannot represent the true quadratic function $h ^ { \star } -$ , but not the lack of the data. Informally, we define the bias of a model to be the test error even if we were to fit it to a very (say, infinitely) large training dataset. Thus, in this case, the linear model suffers from large bias, and underfits (i.e., fails to capture structure exhibited by) the data.

![](images/page_118_chart_5.jpg)

Figure 8.3: The best fit linear model on a much larger dataset still has a large training error.

![](images/page_118_chart_7.jpg)

Figure 8.4: The best fit linear model on a noiseless dataset also has a large training/test error.

Next, we fit a 5th-degree polynomial to the data. Figure 8.5 shows that it fails to learn a good model either. However, the failure pattern is different from the linear model case. Specifically, even though the learnt 5th-degree

<!-- page: 120 -->

polynomial did a very good job predicting $y ^ { ( i ) } \mathrm { ^ { \prime } s }$ from $x ^ { ( i ) } \mathrm { ^ { \mathrm { , } } s }$ for training examples, it does not work well on test examples (Figure 8.5). In other words, the model learnt from the training set does not generalize well to other test examples—the test error is high. Contrary to the behavior of linear models, the bias of the 5-th degree polynomials is small—if we were to fit a 5-th de gree polynomial to an extremely large dataset, the resulting model would be close to a quadratic function and be accurate (Figure 8.6). This is because the family of 5-th degree polynomials contains all the quadratic functions (setting $\theta _ { 5 }   =   \theta _ { 4 }   =   \theta _ { 3 }   =   0$ results in a quadratic function), and, therefore, 5-th degree polynomials are in principle capable of capturing the structure of the data.

![](images/page_119_chart_2.jpg)

![](images/page_119_chart_3.jpg)

Figure 8.5: The best-fit fifth-degree polynomial has zero training error, but still has a large test error and does not recover the ground truth. This is a classic situation of overfitting.

![](images/page_119_chart_5.jpg)

Figure 8.6: The best fit 5-th degree polynomial on a huge dataset nearly recovers the ground-truth—suggesting that the culprit in Figure 8.5 is the variance (or lack of data) but not bias.

The failure of fitting 5-th degree polynomials can be captured by another

<!-- page: 121 -->

component of the test error, called variance of a model fitting procedure. Specifically, when fitting a 5-th degree polynomial as in Figure 8.7, there is a large risk that we’re fitting patterns in the data that happened to be present in our small, finite training set, but that do not reflect the wider pattern of the relationship between x and y. These “spurious” patterns in the training set are (mostly) due to the observation noise ξ(<sup>i</sup>), and fitting these spurious patters results in a model with large test error. In this case, we say the model has a large variance.

![](images/page_120_chart_2.jpg)

![](images/page_120_chart_3.jpg)

![](images/page_120_chart_4.jpg)

Figure 8.7: The best fit 5-th degree models on three different datasets generated from the same distribution behave quite differently, suggesting the existence of a large variance.

The variance can be intuitively (and mathematically, as shown in Section 8.1.1) characterized by the amount of variations across models learnt on multiple different training datasets (drawn from the same underlying dis tribution). The “spurious patterns” are specific to the randomness of the noise (and inputs) in a particular dataset, and thus are different across multiple training datasets. Therefore, overfitting to the “spurious patterns” of multiple datasets should result in very different models. Indeed, as shown in Figure 8.7, the models learned on the three different training datasets are quite different, overfitting to the “spurious patterns” of each datasets.

Often, there is a tradeoff between bias and variance. If our model is too “simple” and has very few parameters, then it may have large bias (but small variance), and it typically may suffer from underfittng. If it is too “complex” and has very many parameters, then it may suffer from large variance (but have smaller bias), and thus overfitting. See Figure 8.8 for a typical tradeoff between bias and variance.

<!-- page: 122 -->

![](images/page_121_chart_1.jpg)

Figure 8.8: An illustration of the typical bias-variance tradeoff.

As we will see formally in Section 8.1.1, the test error can be decomposed as a summation of bias and variance. This means that the test error will have a convex curve as the model complexity increases, and in practice we should tune the model complexity to achieve the best tradeoff. For instance, in the example above, fitting a quadratic function does better than either of the extremes of a first or a 5-th degree polynomial, as shown in Figure 8.9.

![](images/page_121_chart_4.jpg)

![](images/page_121_chart_5.jpg)

Figure 8.9: Best fit quadratic model has small training and test error because quadratic model achieves a better tradeoff.

Interestingly, the bias-variance tradeoff curves or the test error curves do not universally follow the shape in Figure 8.8, at least not universally when the model complexity is simply measured by the number of parameters. (We will discuss the so-called double descent phenomenon in Section 8.2.) Nevertheless, the principle of bias-variance tradeoff is perhaps still the first resort when analyzing and predicting the behavior of test errors.

<!-- page: 123 -->

## 8.1.1 A mathematical decomposition (for regression)

To formally state the bias-variance tradeoff for regression problems, we consider the following setup (which is an extension of the beginning paragraph of Section 8.1).

• Draw a training dataset $S = \{ x ^ { ( i ) } , y ^ { ( i ) } \} _ { i = 1 } ^ { n }$ such that $y ^ { ( i ) } = h ^ { \star } ( x ^ { ( i ) } ) + \xi ^ { ( i ) }$ where $\xi ^ { ( i ) } \in N ( 0 , \sigma ^ { 2 } )$

• Train a model on the dataset S, denoted by $\hat { h } _ { S }$

• Take a test example $( x , y )$ such that $y = h ^ { \star } ( x ) + \xi$ where $\xi \sim N ( 0 , \sigma ^ { 2 } )$ , and measure the expected test error (averaged over the random draw of the training set S and the randomness of $\xi ) ^ { 5 6 }$

$$
\mathrm{MSE} (x) = \mathbb {E} _ {S, \xi} [ (y - h _ {S} (x)) ^ {2} ]\tag{8.2}
$$

We will decompose the MSE into a bias and variance term. We start by stating a following simple mathematical tool that will be used twice below.

Claim 8.1.1.: Suppose A and B are two independent real random variables and $\mathbb { E } [ A ] = 0$ . Then, $\mathbb { E } [ ( A + B ) ^ { 2 } ] = \mathbb { E } [ A ^ { 2 } ] + \mathbb { E } [ B ^ { 2 } ]$

As a corollary, because a random variable A is independent with a constant c, when $\mathbb { E } [ A ] = 0$ , we have $\mathbb { E } [ ( A + c ) ^ { 2 } ] = \mathbb { E } [ A ^ { 2 } ] + \bar { c ^ { 2 } }$

The proof of the claim follows from expanding the square: $\mathbb { E } [ ( A + B ) ^ { 2 } ] =$ $\mathbb { E } [ A ^ { 2 } ] + \mathbb { E } [ B ^ { 2 } ] + 2 \mathbb { E } [ A B ] = \mathbb { E } [ A ^ { 2 } ] + \mathbb { E } [ B ^ { 2 } ]$ . Here we used the independence to show that $\mathbb{E}[AB] = \mathbb{E}[A]\mathbb{E}[B] = 0$

Using Claim 8.1.1 with $A = \xi$ and $B = h ^ { \star } ( x ) - \hat { h } _ { S } ( x )$ , we have

$$
\mathrm{MSE} (x) = \mathbb {E} [ (y - h _ {S} (x)) ^ {2} ] = \mathbb {E} [ (\xi + (h ^ {\star} (x) - h _ {S} (x))) ^ {2} ]\tag{8.3}
$$

8.1.1)

$$
= \sigma^ {2} + \mathbb {E} [ (h ^ {\star} (x) - h _ {S} (x)) ^ {2} ]\tag{8.4}
$$

Then, let’s define $h _ { \mathrm { a v g } } ( x ) = \mathbb { E } _ { S } [ h _ { S } ( x ) ]$ as the “average model”—the model obtained by drawing an infinite number of datasets, training on them, and averaging their predictions on x. Note that $h _ { \mathrm { a v g } }$ is a hypothetical model for analytical purposes that cannot be obtained in reality (because we don’t

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>For simplicity, the test input x is considered to be fixed here, but the same conceptual message holds when we average over the choice of x’s.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>The subscript under the expectation symbol is to emphasize the variables that are considered as random by the expectation operation.</span></small>

<!-- page: 124 -->

have an infinite number of datasets). It turns out that for many cases, $h _ { \mathrm { a v g } }$ is (approximately) equal to the model obtained by training on a single dataset with infinite samples. Thus, we can also intuitively interpret $h _ { \mathrm { a v g } }$ this way, which is consistent with our intuitive definition of bias in the previous subsection.

We can further decompose MSE(x) by letting $c = h ^ { \star } ( x ) { - } h _ { \mathrm { a v g } } ( x )$ (which is a constant that does not depend on the choice of S!) and $A = h _ { \mathrm { a v g } } ( x )   -   h _ { S } ( x )$ in the corollary part of Claim 8.1.1:

$$
\mathrm{MSE} (x) = \sigma^ {2} + \mathbb {E} [ (h ^ {\star} (x) - h _ {S} (x)) ^ {2} ]\tag{8.5}
$$

$$
= \sigma^ {2} + (h ^ {\star} (x) - h _ {\mathrm{avg}} (x)) ^ {2} + \mathbb {E} [ (h _ {\mathrm{avg}} - h _ {S} (x)) ^ {2} ]\tag{8.6}
$$

$$
= \underbrace {\sigma^ {2}} + \underbrace {(h ^ {\star} (x) - h _ {\mathrm{avg}} (x)) ^ {2}} + \underbrace {\operatorname{var} (h _ {S} (x))} \quad\tag{8.7}
$$

$$
\text {unavoidable} \quad \stackrel {{\triangle}} {{=}} \text {bias} ^ {2} \quad \stackrel {{\triangle}} {{=}} \text {variance}
$$

We call the second term the bias (square) and the third term the variance. As discussed before, the bias captures the part of the error that are introduced due to the lack of expressivity of the model. Recall that $h _ { \mathrm { a v g } }$ can be thought of as the best possible model learned even with infinite data. Thus, the bias is not due to the lack of data, but is rather caused by that the family of models fundamentally cannot approximate the $h ^ { \star }$ . For example, in the illustrating example in Figure 8.2, because any linear model cannot approximate the true quadratic function $h ^ { \star }$ , neither can $h _ { \mathrm { a v g } }$ , and thus the bias term has to be large.

The variance term captures how the random nature of the finite dataset introduces errors in the learned model. It measures the sensitivity of the learned model to the randomness in the dataset. It often decreases as the size of the dataset increases.

There is nothing we can do about the first term $\sigma ^ { 2 }$ as we can not predict the noise ξ by definition.

Finally, we note that the bias-variance decomposition for classification is much less clear than for regression problems. There have been several proposals, but there is as yet no agreement on what is the “right” and/or the most useful formalism.

## 8.2 The double descent phenomenon

Model-wise double descent. Recent works have demonstrated that the test error can present a “double descent” phenomenon in a range of machine

<!-- page: 125 -->

learning models including linear models and deep neural networks.<sup>7</sup> The conventional wisdom, as discussed in Section 8.1, is that as we increase the model complexity, the test error first decreases and then increases, as illustrated in Figure 8.8. However, in many cases, we empirically observe that the test error can have a second descent—it first decreases, then increases to a peak around when the model size is large enough to fit all the training data very well, and then decreases again in the so-called overparameterized regime, where the number of parameters is larger than the number of data points. See Figure 8.10 for an illustration of the typical curves of test errors against model complexity (measured by the number of parameters). To some extent, the overparameterized regime with the second descent is considered as new to the machine learning community—partly because lightly-regularized, overparameterized models are only extensively used in the deep learning era. A practical implication of the phenomenon is that one should not hold back from scaling into and experimenting with over-parametrized models because the test error may well decrease again to a level even smaller than the previous lowest point. Actually, in many cases, larger overparameterized models always lead to a better test performance (meaning there won’t be a second ascent after the second descent).

![](images/page_124_image_2.jpg)

Figure 8.10: A typical model-wise double descent phenomenon. As the number of parameters increases, the test error first decreases when the number of parameters is smaller than the training data. Then in the overparameterized regime, the test error decreases again.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>The discovery of the phenomenon perhaps dates back to Opper [1995, 2001], and has been recently popularized by Belkin et al. [2020], Hastie et al. [2019], etc.</span></small>

<!-- page: 126 -->

Sample-wise double descent. A priori, we would expect that more training examples always lead to smaller test errors—more samples give strictly more information for the algorithm to learn from. However, recent work [Nakkiran, 2019] observes that the test error is not monotonically de creasing as we increase the sample size. Instead, as shown in Figure 8.11, the test error decreases, and then increases and peaks around when the number of examples (denoted by n) is similar to the number of parameters (denoted by d), and then decreases again. We refer to this as the sample-wise double descent phenomenon. To some extent, sample-wise double descent and model-wise double descent are essentially describing similar phenomena—the test error is peaked when $n \approx d .$

Explanation and mitigation strategy. The sample-wise double descent, or, in particular, the peak of test error at $n \approx d ,$ suggests that the existing training algorithms evaluated in these experiments are far from optimal when $n \approx d .$ We will be better off by tossing away some examples and run the algorithms with a smaller sample size to steer clear of the peak. In other words, in principle, there are other algorithms that can achieve smaller test error when $n \approx d ,$ but the algorithms evaluated in these experiments fail to do so. The sub-optimality of the learning procedure appears to be the culprit of the peak in both sample-wise and model-wise double descent.

Indeed, with an optimally-tuned regularization (which will be discussed more in Section 9), the test error in the $n \approx d$ regime can be dramatically improved, and the model-wise and sample-wise double descent are both mitigated. See Figure 8.11.

The intuition above only explains the peak in the model-wise and sample wise double descent, but does not explain the second descent in the modelwise double descent—why overparameterized models are able to generalize so well. The theoretical understanding of overparameterized models is an active research area with many recent advances. A typical explanation is that the commonly-used optimizers such as gradient descent provide an implicit regularization effect (which will be discussed in more detail in Section 9.2). In other words, even in the overparameterized regime and with an unregularized loss function, the model is still implicitly regularized, and thus exhibits a better test performance than an arbitrary solution that fits the data. For example, for linear models, when $n \ll d ,$ the gradient descent optimizer with zero initialization finds the minimum norm solution that fits the data (in stead of an arbitrary solution that fits the data), and the minimum norm regularizer turns out to be a sufficiently good for the overparameterized regime (but it’s not a good regularizer when $n   \approx   d ,$ resulting in the peak of test

<!-- page: 127 -->

![](images/page_126_chart_2.jpg)

![](images/page_126_chart_3.jpg)

Figure 8.11: Left: The sample-wise double descent phenomenon for linear models. Right: The sample-wise double descent with different regularization strength for linear models. Using the optimal regularization parameter λ (optimally tuned for each $n ,$ shown in green solid curve) mitigates double descent. Setup: The data distribution of $( x , y )$ is $x   \sim   \mathcal { N } ( 0 , I _ { d } )$ and $y \sim$ $x ^ { \top } \beta + \mathcal { N } ( 0 , \sigma ^ { 2 } )$ where $d = 5 0 0 , \sigma = 0 . 5$ and $\| \beta \| _ { 2 } = 1 . ^ { 8 }$

Finally, we also remark that the double descent phenomenon has been mostly observed when the model complexity is measured by the number of parameters. It is unclear if and when the number of parameters is the best complexity measure of a model. For example, in many situations, the norm of the models is used as a complexity measure. As shown in Figure 8.12 right, for a particular linear case, if we plot the test error against the norm of the learnt model, the double descent phenomenon no longer occurs. This is partly because the norm of the learned model is also peaked around $n \approx d$ (See Figure 8.12 (middle) or Belkin et al. [2019], Mei and Montanari [2022], and discussions in Section 10.8 of James et al. [2021]). For deep neural networks, the correct complexity measure is even more elusive. The study of double descent phenomenon is an active research topic.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>The figure is reproduced from Figure 1 of Nakkiran et al. [2020]. Similar phenomenon are also observed in Hastie et al. [2022], Mei and Montanari [2022]</span></small>

<!-- page: 128 -->

![](images/page_127_chart_1.jpg)

![](images/page_127_chart_2.jpg)

![](images/page_127_chart_3.jpg)

Figure 8.12: Left: The double descent phenomenon, where the number of parameters is used as the model complexity. Middle: The norm of the learned model is peaked around $n \approx d .$ Right: The test error against the norm of the learnt model. The color bar indicate the number of parameters and the arrows indicates the direction of increasing model size. Their relationship are closer to the convention wisdom than to a double descent. Setup: We consider a linear regression with a fixed dataset of size $n = 5 0 0$ . The input x is a random ReLU feature on Fashion-MNIST, and output $y \in \mathbb { R } ^ { 1 0 }$ is the one-hot label. This is the same setting as in Section 5.2 of Nakkiran et al. [2020].

<!-- page: 129 -->

## 8.3 Sample complexity bounds

## 8.3.1 Preliminaries

In this set of notes, we begin our foray into learning theory. Apart from being interesting and enlightening in its own right, this discussion will also help us hone our intuitions and derive rules of thumb about how to best apply learning algorithms in different settings. We will also seek to answer a few questions: First, can we make formal the bias/variance tradeoff that was just discussed? This will also eventually lead us to talk about model selection methods, which can, for instance, automatically decide what order polynomial to fit to a training set. Second, in machine learning it’s really generalization error that we care about, but most learning algorithms fit their models to the training set. Why should doing well on the training set tell us anything about generalization error? Specifically, can we relate error on the training set to generalization error? Third and finally, are there conditions under which we can actually prove that learning algorithms will work well?

We start with two simple but very useful lemmas.

Lemma. (The union bound). Let $A _ { 1 } , A _ { 2 } , \ldots , A _ { k }$ be k different events (that may not be independent). Then

$$
P (A _ {1} \cup \dots \cup A _ {k}) \leq P (A _ {1}) + \dots + P (A _ {k}).
$$

In probability theory, the union bound is usually stated as an axiom (and thus we won’t try to prove it), but it also makes intuitive sense: The probability of any one of $k$ events happening is at most the sum of the probabilities of the k different events.

Lemma. (Hoeffding inequality) Let $Z _ { 1 } , \ldots , Z _ { n }$ be n independent and identically distributed (iid) random variables drawn from a Bernoulli $( \phi )$ distribution. I.e., $P ( Z _ { i } = 1 ) = \phi$ , and $P ( Z _ { i } = 0 ) = 1 - \phi$ . Let $\begin{array} { r } { \hat { \phi } = \stackrel { \leftrightarrow } { ( 1 / n ) } \sum _ { i = 1 } ^ { n } Z _ { i } } \end{array}$ be the mean of these random variables, and let any $\gamma > 0$ be fixed. Then

$$
P (| \phi - \hat {\phi} | > \gamma) \leq 2 \exp (- 2 \gamma^ {2} n)
$$

This lemma (which in learning theory is also called the Chernoff bound) says that if we take $\hat { \phi } -$ the average of n Bernoulli(φ) random variables—to be our estimate of $\phi ,$ then the probability of our being far from the true value is small, so long as n is large. Another way of saying this is that if you have a biased coin whose chance of landing on heads is $\phi ,$ then if you toss it n times and calculate the fraction of times that it came up heads, that will be a good estimate of $\phi$ with high probability (if n is large).

<!-- page: 130 -->

Using just these two lemmas, we will be able to prove some of the deepest and most important results in learning theory.

To simplify our exposition, let’s restrict our attention to binary classification in which the labels are $y \in \{ 0 , 1 \}$ . Everything we’ll say here generalizes to other problems, including regression and multi-class classification.

We assume we are given a training set $S = \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) ; i = 1 , \ldots , n \}$ of size n, where the training examples $( x ^ { ( i ) } , y ^ { ( i ) } )$ are drawn iid from some probability distribution D. For a hypothesis h, we define the training error (also called the empirical risk or empirical error in learning theory) to be

$$
\hat {\varepsilon} (h) = \frac {1}{n} \sum_ {i = 1} ^ {n} 1 \{h (x ^ {(i)}) \neq y ^ {(i)} \}.
$$

This is just the fraction of training examples that h misclassifies. When we want to make explicit the dependence of $\hat { \varepsilon } ( h )$ on the training set $S ,$ we may also write this a $\hat { \varepsilon } _ { S } ( h )$ . We also define the generalization error to be

$$
\varepsilon (h) = P _ {(x, y) \sim \mathcal {D}} (h (x) \neq y).
$$

I.e. this is the probability that, if we now draw a new example $( x , y )$ from the distribution D, h will misclassify it.

Note that we have assumed that the training data was drawn from the same distribution D with which we’re going to evaluate our hypotheses (in the definition of generalization error). This is sometimes also referred to as one of the PAC assumptions.<sup>9</sup>

Consider the setting of linear classification, and let $h _ { \theta } ( x ) = 1 \{ \theta ^ { T } x \geq 0 \}$ What’s a reasonable way of fitting the parameters $\theta ?$ One approach is to try to minimize the training error, and pick

$$
\hat {\theta} = \arg \min _ {\theta} \hat {\varepsilon} (h _ {\theta}).
$$

We call this process empirical risk minimization (ERM), and the resulting hypothesis output by the learning algorithm is $\hat { h }   =   h _ { \hat { \theta } }$ We think of ERM as the most “basic” learning algorithm, and it will be this algorithm that we focus on in these notes. (Algorithms such as logistic regression can also be viewed as approximations to empirical risk minimization.)

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>PAC stands for “probably approximately correct,” which is a framework and set of assumptions under which numerous results on learning theory were proved. Of these, the assumption of training and testing on the same distribution, and the assumption of the independently drawn training examples, were the most important.</span></small>

<!-- page: 131 -->

In our study of learning theory, it will be useful to abstract away from the specific parameterization of hypotheses and from issues such as whether we’re using a linear classifier. We define the hypothesis class H used by a learning algorithm to be the set of all classifiers considered by it. For linear classification, $\mathcal { H }   =   \{ h _ { \theta }   :   h _ { \theta } ( x )   =   1 \{ \theta ^ { T } x   \geq   0 \} , \theta   \in   \mathbb { R } ^ { d + 1 } \}$ is thus the set of all classifiers over $\mathcal { X }$ (the domain of the inputs) where the decision boundary is linear. More broadly, if we were studying, say, neural networks, then we could let H be the set of all classifiers representable by some neural network architecture.

Empirical risk minimization can now be thought of as a minimization over the class of functions $\mathcal { H } ,$ in which the learning algorithm picks the hypothesis:

$$
\hat {h} = \arg \min _ {h \in \mathcal {H}} \hat {\varepsilon} (h)
$$

## 8.3.2 The case of finite H

Let’s start by considering a learning problem in which we have a finite hypothesis class $\mathcal { H } = \{ h _ { 1 } , \ldots , h _ { k } \}$ consisting of k hypotheses. Thus, H is just a set of k functions mapping from $\mathcal { X }$ to $\{ 0 , 1 \}$ , and empirical risk minimization selects $\hat { h }$ to be whichever of these k functions has the smallest training error.

We would like to give guarantees on the generalization error of $\hat { h }$ . Our strategy for doing so will be in two parts: First, we will show that $\hat { \varepsilon } ( h )$ is a reliable estimate $of $\varepsilon ( h )$$ for all h. Second, we will show that this implies an upper-bound on the generalization error of $\hat { h }$

Take any one, fixed, $h _ { i } \in \mathcal { H }$ . Consider a Bernoulli random variable Z whose distribution is defined as follows. We’re going to sample $( x , y ) \sim \mathcal { D }$ Then, we set $Z   =   1 \{ h _ { i } ( x )   \neq   y \}$ . I.e., we’re going to draw one example, and let $Z$ indicate whether $h _ { i }$ misclassifies it. Similarly, we also define $Z _ { j } =$ $1 \{ h _ { i } ( x ^ { ( j ) } ) \neq y ^ { ( j ) } \}$ . Since our training set was drawn iid from $\mathcal { D } .$ , Z and the $Z _ { j } { } ^ { \prime } \mathrm { s }$ have the same distribution.

We see that the misclassification probability on a randomly drawn example—that is, $\varepsilon ( h )$ —is exactly the expected value of $Z$ (and $Z _ { j } )$ . Moreover, the training error can be written

$$
\hat {\varepsilon} (h _ {i}) = \frac {1}{n} \sum_ {j = 1} ^ {n} Z _ {j}.
$$

Thus, $\hat { \varepsilon } ( h _ { i } )$ is exactly the mean of the n random variables $Z _ { j }$ that are drawn iid from a Bernoulli distribution with mean $\varepsilon ( h _ { i } )$ . Hence, we can apply the Hoeffding inequality, and obtain

$$
P (| \varepsilon (h _ {i}) - \hat {\varepsilon} (h _ {i}) | > \gamma) \leq 2 \exp (- 2 \gamma^ {2} n).
$$

<!-- page: 132 -->

This shows that, for our particular $h _ { i }$ , training error will be close to generalization error with high probability, assuming n is large. But we don’t just want to guarantee that $\varepsilon ( h _ { i } )$ will be close to $\hat { \varepsilon } ( h _ { i } )$ (with high probability) for just only one particular $h _ { i }$ . We want to prove that this will be true simultaneously for all $h \in \mathcal { H }$ . To do $\mathrm { s o } ,$ let $A _ { i }$ denote the event that $| \varepsilon ( h _ { i } ) -$ $| \hat { \varepsilon } ( h _ { i } ) |   >   \gamma$ . We’ve already shown that, for any particular $A _ { i j }$ it holds true that $P ( A _ { i } ) \leq 2 \exp ( - 2 \gamma ^ { 2 } n )$ . Thus, using the union bound, we have that

$$
\begin{array}{r c l} P (\exists h \in \mathcal {H}. | \varepsilon (h _ {i}) - \hat {\varepsilon} (h _ {i}) | > \gamma) & = & P (A _ {1} \cup \dots \cup A _ {k}) \\ & \leq & \sum_ {i = 1} ^ {k} P (A _ {i}) \\ & \leq & \sum_ {i = 1} ^ {k} 2 \exp (- 2 \gamma^ {2} n) \\ & = & 2 k \exp (- 2 \gamma^ {2} n) \end{array}
$$

If we subtract both sides from 1, we find that

$$
\begin{array}{r c l} P (\neg \exists h \in \mathcal {H}. | \varepsilon (h _ {i}) - \hat {\varepsilon} (h _ {i}) | > \gamma) & = & P (\forall h \in \mathcal {H}. | \varepsilon (h _ {i}) - \hat {\varepsilon} (h _ {i}) | \leq \gamma) \\ & \geq & 1 - 2 k \exp (- 2 \gamma^ {2} n) \end{array}
$$

(The $a _ {  一  } ,$ symbol means $\text{" } not." ) \quad  So,$ with probability at least $1 -$ 2k $\exp ( - 2 \gamma ^ { 2 } n )$ , we have that $\varepsilon ( h )$ will be within $\gamma$ of $\hat { \varepsilon } ( h )$ for all $h \in \mathcal { H }$ This is called a uniform convergence result, because this is a bound that holds simultaneously for all (as opposed to just one) $h \in \mathcal { H }$

In the discussion above, what we did was, for particular values of n and $\gamma ,$ give a bound on the probability that for some $h \in \mathcal { H } ,   | \varepsilon ( h ) - \hat { \varepsilon } ( h ) | > \gamma$ There are three quantities of interest here: $n ,   \gamma$ , and the probability of error; we can bound either one in terms of the other two.

For instance, we can ask the following question: Given $\gamma$ and some $\delta > 0$ how large must n be before we can guarantee that with probability at least $1 - \delta .$ training error will be within $\gamma$ of generalization error? By setting $\delta   =   2 k \exp ( - 2 \gamma ^ { 2 } n )$ and solving for $n .$ , [you should convince yourself this is the right thing to do!], we find that if

$$
n \geq \frac {1}{2 \gamma^ {2}} \log \frac {2 k}{\delta},
$$

then with probability at least $1 - \delta ,$ we have that $| \varepsilon ( h ) - \hat { \varepsilon } ( h ) | \leq \gamma$ for all $h \in \mathcal { H }$ . (Equivalently, this shows that the probability that $| \varepsilon ( h ) - \hat { \varepsilon } ( h ) | > \gamma$

<!-- page: 133 -->

for some $h \in \mathcal { H }$ is at most $\delta . )$ This bound tells us how many training examples we need in order make a guarantee. The training set size n that a certain method or algorithm requires in order to achieve a certain level of performance is also called the algorithm’s sample complexity.

The key property of the bound above is that the number of training examples needed to make this guarantee is only logarithmic in $k ,$ the number of hypotheses in $\mathcal { H } .$ This will be important later.

Similarly, we can also hold n and $\delta$ fixed and solve for $\gamma$ in the previous equation, and show [again, convince yourself that this is right!] that with probability $1 - \delta$ , we have that for all $h \in \mathcal { H }$

$$
| \hat {\varepsilon} (h) - \varepsilon (h) | \leq \sqrt {\frac {1}{2 n} \log \frac {2 k}{\delta}}.
$$

Now, let’s assume that uniform convergence holds, i.e., that $\left| \varepsilon ( h ) { - } \hat { \varepsilon } ( h ) \right| \leq$ $\gamma$ for all $h \in \mathcal { H }$ . What can we prove about the generalization of our learning algorithm that picked $\hat { h } = \operatorname { a r g } \operatorname { m i n } _ { h \in \mathcal { H } } \hat { \varepsilon } ( h ) ?$

Define $h ^ { * } = \operatorname { a r g } \operatorname { m i n } _ { h \in \mathcal { H } } \varepsilon ( h )$ to be the best possible hypothesis in $\mathcal { H }$ . Note that $h ^ { * }$ is the best that we could possibly do given that we are using H, so it makes sense to compare our performance to that of $h ^ { * }$ . We have:

$$
\begin{array}{r c l} \varepsilon (\hat {h}) & \leq & \hat {\varepsilon} (\hat {h}) + \gamma \\ & \leq & \hat {\varepsilon} (h ^ {*}) + \gamma \\ & \leq & \varepsilon (h ^ {*}) + 2 \gamma \end{array}
$$

The first line used the fact that $\lvert \varepsilon ( \hat { h } )   -   \hat { \varepsilon } ( \hat { h } ) \rvert \leq \gamma$ (by our uniform convergence assumption). The second used the fact that ĥ was chosen to minimize $\hat { \varepsilon } ( h )$ and hence $\hat { \varepsilon } ( \hat { h } ) \leq \hat { \varepsilon } ( h )$ for all $h ,$ and in particular $\hat { \varepsilon } ( \hat { h } )   \leq   \hat { \varepsilon } ( h ^ { * } )$ . The third line used the uniform convergence assumption again, to show that $\hat { \varepsilon } ( h ^ { * } ) \leq$ $\varepsilon ( h ^ { * } ) + \gamma$ . So, what we’ve shown is the following: If uniform convergence occurs, then the generalization error of $\hat { h }$ is at most $2 \gamma$ worse than the best possible hypothesis in H!

Let’s put all this together into a theorem.

Theorem. Let $| \mathcal { H } | = k$ , and let any $n , \delta$ be fixed. Then with probability at least $1 - \delta$ , we have that

$$
\varepsilon (\hat {h}) \leq \left(\min _ {h \in \mathcal {H}} \varepsilon (h)\right) + 2 \sqrt {\frac {1}{2 n} \log \frac {2 k}{\delta}}.
$$

<!-- page: 134 -->

This is proved by letting $\gamma$ equal the $\sqrt { \cdot }$ term, using our previous argument that uniform convergence occurs with probability at least $1 - \delta$ , and then noting that uniform convergence implies $\varepsilon ( h )$ is at most $2 \gamma$ higher than $\begin{array} { r } { \varepsilon \big ( h ^ { * } \big ) = \operatorname* { m i n } _ { h \in \mathcal { H } } \varepsilon \big ( h \big ) } \end{array}$ (as we showed previously).

This also quantifies what we were saying previously saying about the bias/variance tradeoff in model selection. Specifically, suppose we have some hypothesis class $\mathcal { H } ,$ and are considering switching to some much larger hypothesis class $\mathcal { H } ^ { \prime } \supseteq \mathcal { H }$ . If we switch to ${ \mathcal { H } } ^ { \prime } ,$ then the first term min ${ } _ { \cdot h } \varepsilon ( h )$ can only decrease (since we’d then be taking a min over a larger set of functions). Hence, by learning using a larger hypothesis class, our “bias” can only decrease. However, if k increases, then the second $2 \sqrt { \cdot }$ term would also increase. This increase corresponds to our “variance” increasing when we use a larger hypothesis class.

By holding $\gamma$ and $\delta$ fixed and solving for n like we did before, we can also obtain the following sample complexity bound:

Corollary. Let $| { \mathcal { H } } | ~ = ~ k ,$ , and let any $\delta , \gamma$ be fixed. Then for $\varepsilon ( \hat { h } ) \leq$ $\begin{array} { r } { \operatorname* { m i n } _ { h \in \mathcal { H } } \varepsilon ( h ) + 2 \gamma } \end{array}$ to hold with probability at least $1 - \delta .$ , it suffices that

$$
\begin{array}{r c l} n & \geq & \frac {1}{2 \gamma^ {2}} \log \frac {2 k}{\delta} \\ & = & O \left(\frac {1}{\gamma^ {2}} \log \frac {k}{\delta}\right), \end{array}
$$

## 8.3.3 The case of infinite H

We have proved some useful theorems for the case of finite hypothesis classes. But many hypothesis classes, including any parameterized by real numbers (as in linear classification) actually contain an infinite number of functions. Can we prove similar results for this setting?

Let’s start by going through something that is not the “right” argument. Better and more general arguments exist, but this will be useful for honing our intuitions about the domain.

Suppose we have an $\mathcal { H }$ that is parameterized by d real numbers. Since we are using a computer to represent real numbers, and IEEE double-precision floating point (double’s in C) uses 64 bits to represent a floating point number, this means that our learning algorithm, assuming we’re using doubleprecision floating point, is parameterized by 64d bits. Thus, our hypothesis class really consists of at most $k = 2 ^ { 6 4 d }$ different hypotheses. From the Corollary at the end of the previous section, we therefore find that, to guarantee $\varepsilon ( \hat { h } ) \leq \varepsilon ( h ^ { * } )   +   2 \gamma$ , with to hold with probability at least $1 - \delta ,$ it suffices that

<!-- page: 135 -->

$n   \geq   O \left( { \textstyle { \frac { 1 } { \gamma ^ { 2 } } } } \log { \textstyle { \frac { 2 ^ { 6 4 d } } { \delta } } } \right)   =   O \left( { \textstyle { \frac { d } { \gamma ^ { 2 } } } } \log { \textstyle { \frac { 1 } { \delta } } } \right)   =   O _ { \gamma , \delta } ( d )$ . (The $\gamma , \delta$ subscripts indicate that the last big-O is hiding constants that may depend on $\gamma$ and $\delta . )$ Thus, the number of training examples needed is at most linear in the parameters of the model.

The fact that we relied on 64-bit floating point makes this argument not entirely satisfying, but the conclusion is nonetheless roughly correct: If what we try to do is minimize training error, then in order to learn “well” using a hypothesis class that has d parameters, generally we’re going to need on the order of a linear number of training examples in $d .$

(At this point, it’s worth noting that these results were proved for an algorithm that uses empirical risk minimization. Thus, while the linear dependence of sample complexity on $d$ does generally hold for most discriminative learning algorithms that try to minimize training error or some approximation to training error, these conclusions do not always apply as readily to discriminative learning algorithms. Giving good theoretical guarantees on many non-ERM learning algorithms is still an area of active research.)

The other part of our previous argument that’s slightly unsatisfying is that it relies on the parameterization of H. Intuitively, this doesn’t seem like it should matter: We had written the class of linear classifiers as $h _ { \theta } ( x )   =$ $1 \{ \theta _ { 0 } + \theta _ { 1 } x _ { 1 } + \cdots \theta _ { d } x _ { d } { \geq } 0 \}$ , with $n + 1$ parameters $\theta _ { 0 } , \ldots , \theta _ { d }$ . But it could also be written $h _ { u , v } ( x ) = 1 \{ ( u _ { 0 } ^ { 2 } - v _ { 0 } ^ { 2 } ) + ( u _ { 1 } ^ { 2 } - v _ { 1 } ^ { 2 } ) x _ { 1 } + \cdots ( u _ { d } ^ { 2 } - v _ { d } ^ { 2 } ) x _ { d } \geq 0 \}$ with $2 d + 2$ parameters $u _ { i } , v _ { i }$ . Yet, both of these are just defining the same $\mathcal { H } ;$ The set of linear classifiers in d dimensions.

To derive a more satisfying argument, let’s define a few more things.

Given a set $S = \{ x ^ { ( i ) } , \dot { \ldots } , \dot { x ^ { ( \mathbf { D } ) } } \}$ (no relation to the training set) of points $x ^ { ( i ) }   \in   \mathcal { X }$ , we say that H shatters S if H can realize any labeling on $S .$ I.e., if for any set of labels $\{ y ^ { ( 1 ) } , \ldots , y ^ { ( \mathbf { D } ) } \}$ , there exists some $h \in \mathcal { H }$ so that $h ( x ^ { ( i ) } ) = y ^ { ( i ) }$ for all $i = 1 , \ldots \mathbf { D }$

Given a hypothesis class H, we then define its Vapnik-Chervonenkis dimension, written $\operatorname { V C } ( { \mathcal { H } } )$ , to be the size of the largest set that is shattered by H. (If H can shatter arbitrarily large sets, then $\operatorname { V C } ( { \mathcal { H } } ) = \infty . )$

For instance, consider the following set of three points:

<!-- page: 136 -->

![](images/page_135_image_1.jpg)

Can the set H of linear classifiers in two dimensions $( h ( x ) = 1 \{ \theta _ { 0 }   +   \theta _ { 1 } x _ { 1 }   +$ $\theta _ { 2 } x _ { 2 }   \geq   0 \} )$ can shatter the set above? The answer is yes. Specifically, we see that, for any of the eight possible labelings of these points, we can find a linear classifier that obtains “zero training error” on them:

![](images/page_135_image_3.jpg)

Moreover, it is possible to show that there is no set of 4 points that this hypothesis class can shatter. Thus, the largest set that H can shatter is of size 3, and hence $\mathrm { V C } ( \mathcal { H } ) = 3$

Note that the VC dimension of H here is 3 even though there may be sets of size 3 that it cannot shatter. For instance, if we had a set of three points lying in a straight line (left figure), then there is no way to find a linear separator for the labeling of the three points shown below (right figure):

<!-- page: 137 -->

![](images/page_136_image_1.jpg)

![](images/page_136_image_2.jpg)

In order words, under the definition of the VC dimension, in order to prove that $\mathrm { V C } ( \mathcal { H } )$ is at least D, we need to show only that there’s at least one set of size D that $\mathcal { H }$ can shatter.

The following theorem, due to Vapnik, can then be shown. (This is, many would argue, the most important theorem in all of learning theory.)

Theorem. Let $\mathcal { H }$ be given, and let $\mathbf { D } = \operatorname { V C } ( { \mathcal { H } } )$ . Then with probability at least $1 - \delta$ , we have that for all $h \in \mathcal { H }$

$$
| \varepsilon (h) - \hat {\varepsilon} (h) | \leq O \left(\sqrt {\frac {\mathbf {D}}{n} \log \frac {n}{\mathbf {D}} + \frac {1}{n} \log \frac {1}{\delta}}\right).
$$

Thus, with probability at least $1 - \delta .$ , we also have that:

$$
\varepsilon (\hat {h}) \leq \varepsilon (h ^ {*}) + O \left(\sqrt {\frac {\mathbf {D}}{n} \log \frac {n}{\mathbf {D}} + \frac {1}{n} \log \frac {1}{\delta}}\right).
$$

In other words, if a hypothesis class has finite VC dimension, then uniform convergence occurs as n becomes large. As before, this allows us to give a bound on $\varepsilon ( h )$ in terms of $\varepsilon ( h ^ { * } )$ . We also have the following corollary:

Corollary. For $| \varepsilon ( h ) - \hat { \varepsilon } ( h ) | \leq \gamma$ to hold for all $h \in \mathcal { H }$ (and hence $\varepsilon ( \hat { h } ) \leq$ $\varepsilon ( h ^ { * } ) + 2 \gamma )$ with probability at least $1 - \delta$ , it suffices that $n = O _ { \gamma , \delta } ( \mathbf { D } )$

In other words, the number of training examples needed to learn “well” using H is linear in the VC dimension of $\mathcal { H } .$ It turns out that, for “most” hypothesis classes, the VC dimension (assuming a “reasonable” parameterization) is also roughly linear in the number of parameters. Putting these together, we conclude that for a given hypothesis class H (and for an algorithm that tries to minimize training error), the number of training examples needed to achieve generalization error close to that of the optimal classifier is usually roughly linear in the number of parameters of H.

<!-- page: 138 -->

# Chapter 9

# Regularization and model selection

## 9.1 Regularization

Recall that as discussed in Section 8.1, overfitting is typically a result of using too complex models, and we need to choose a proper model complexity to achieve the optimal bias-variance tradeoff. When the model complexity is measured by the number of parameters, we can vary the size of the model (e.g., the width of a neural net). However, the correct, informative complexity measure of the models can be a function of the parameters $( \mathrm { e . g . , } ~ \ell _ { 2 }$ norm of the parameters), which may not necessarily depend on the number of parameters. In such cases, we will use regularization, an important technique in machine learning, to control the model complexity and prevent overfitting.

Regularization typically involves adding an additional term, called a regularizer and denoted by $R ( \theta )$ here, to the training loss/cost function:

$$
J _ {\lambda} (\theta) = J (\theta) + \lambda R (\theta)\tag{9.1}
$$

Here $J _ { \lambda }$ is often called the regularized loss, and $\lambda \geq 0$ is called the regularization parameter. The regularizer $R ( \theta )$ is a nonnegative function (in almost all cases). In classical methods, $R ( \theta )$ is purely a function of the parameter $\theta ,$ but some modern approach allows $R ( \theta )$ to depend on the training dataset.<sup>1</sup>

The regularizer $R ( \theta )$ is typically chosen to be some measure of the complexity of the model θ. Thus, when using the regularized loss, we aim to find a model that both fit the data (a small loss $J ( \theta ) )$ and have a small

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">J θ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Here our notations generally omit the dependency on the training dataset for simplicity—we write ( ) even though it obviously needs to depend on the training dataset.</span></small>

<!-- page: 139 -->

model complexity (a small $R ( \theta ) )$ . The balance between the two objectives is controlled by the regularization parameter λ. When $\lambda = 0$ , the regularized loss is equivalent to the original loss. When λ is a sufficiently small positive number, minimizing the regularized loss is effectively minimizing the original loss with the regularizer as the tie-breaker. When the regularizer is extremely large, then the original loss is not effective (and likely the model will have a large bias.)

The most commonly used regularization is perhaps $\ell _ { 2 }$ regularization, where $R ( \theta ) \; = \; { \textstyle { \frac { 1 } { 2 } } } \| \theta \| _ { 2 } ^ { 2 }$ It encourages the optimizer to find a model with small $\ell _ { 2 }$ norm. In deep learning, it’s oftentimes referred to as weight decay, because gradient descent with learning rate $\eta$ on the regularized loss $R _ { \lambda } ( \theta )$ is equivalent to shrinking/decaying $\theta$ by a scalar factor of $1 - \eta \lambda$ and then applying the standard gradient

$$
\begin{array}{r l} & {\theta \leftarrow \theta - \eta \nabla J _ {\lambda} (\theta) = \theta - \eta \lambda \theta - \eta \nabla J (\theta)} \\ & {\quad = \underbrace {(1 - \lambda \eta) \theta} _ {\text {decaying weights}} - \eta \nabla J (\theta)} \end{array}\tag{9.2}
$$

Besides encouraging simpler models, regularization can also impose inductive biases or structures on the model parameters. For example, suppose we had a prior belief that the number of non-zeros in the ground-truth model parameters is small,<sup>2</sup>—which is oftentimes called sparsity of the model—, we can impose a regularization on the number of non-zeros in $\theta ,$ denoted by $\| \theta \| _ { 0 }$ , to leverage such a prior belief. Imposing additional structure of the parameters narrows our search space and makes the complexity of the model family smaller, $, \mathrm { {  一  } { \mathrm { { e } } } . { \mathrm { { g } } } . }$ , the family of sparse models can be thought of as having lower complexity than the family of all models—, and thus tends to lead to a better generalization. On the other hand, imposing additional structure may risk increasing the bias. For example, if we regularize the sparsity strongly but no sparse models can predict the label accurately, we will suffer from large bias (analogously to the situation when we use linear models to learn data than can only be represented by quadratic functions in Section 8.1.)

The sparsity of the parameters is not a continuous function of the parameters, and thus we cannot optimize it with (stochastic) gradient descent. A common relaxation is to use $R ( \theta ) = \| \theta \| _ { 1 }$ k<sub>1</sub> as a continuous surrogate.<sup>3</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">k k1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\`1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>For linear models, this means the model just uses a few coordinates of the inputs to make an accurate prediction.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>There has been a rich line of theoretical work that explains why θ is a good surrogate for encouraging sparsity, but it’s beyond the scope of this course. An intuition is: assuming the parameter is on the unit sphere, the parameter with smallest norm also</span></small>

<!-- page: 140 -->

The $R ( \theta )   =   \| \theta \|$ 1 (also called LASSO) and $R ( \theta )   =   \textstyle { \frac { 1 } { 2 } } \| \theta \| _ { 2 } ^ { 2 }$ are perhaps among the most commonly used regularizers for linear models. Other norm and powers of norms are sometimes also used. The $\ell _ { 2 }$ norm regularization is much more commonly used with kernel methods because $\ell _ { 1 }$ regularization is typically not compatible with the kernel trick (the optimal solution cannot be written as functions of inner products of features.)

In deep learning, the most commonly used regularizer is $\ell _ { 2 }$ regularization or weight decay. Other common ones include dropout, data augmentation, regularizing the spectral norm of the weight matrices, and regularizing the Lipschitzness of the model, etc. Regularization in deep learning is an active research area, and it’s known that there is another implicit source of regularization, as discussed in the next section.

## 9.2 Implicit regularization effect

The implicit regularization effect of optimizers, or implicit bias or algorithmic regularization, is a new concept/phenomenon observed in the deep learning era. It largely refers to that the optimizers can implicitly impose structures on parameters beyond what has been imposed by the regularized loss.

In most classical settings, the loss or regularized loss has a unique global minimum, and thus any reasonable optimizer should converge to that global minimum and cannot impose any additional preferences. However, in deep learning, oftentimes the loss or regularized loss has more than one (approx imate) global minima, and difference optimizers may converge to different global minima. Though these global minima have the same or similar train ing losses, they may be of different nature and have dramatically different generalization performance. See Figures 9.1 and 9.2 and its caption for an illustration and some experiment results. For example, it’s possible that one global minimum gives a much more Lipschitz or sparse model than others and thus has a better test error. It turns out that many commonly-used op timizers (or their components) prefer or bias towards finding global minima of certain properties, leading to a better test performance.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\`1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">happen to be the sparsest parameter with only 1 non-zero coordinate. Thus, sparsity and norm gives the same extremal points to some extent.</span></small>

<!-- page: 141 -->

![](images/page_140_chart_1.jpg)

Figure 9.1: An Illustration that different global minima of the training loss can have different test performance.

![](images/page_140_chart_3.jpg)

![](images/page_140_chart_4.jpg)

Figure 9.2: Left: Performance of neural networks trained by two different learning rates schedules on the CIFAR-10 dataset. Although both experiments used exactly the same regularized losses and the optimizers fit the training data perfectly, the models’ generalization performance differ much. Right: On a different synthetic dataset, optimizers with different initializations have the same training error but different generalization performance.<sup>4</sup>

In summary, the takehome message here is that the choice of optimizer does not only affect minimizing the training loss, but also imposes implicit regularization and affects the generalization of the model. Even if your current optimizer already converges to a small training error perfectly, you may still need to tune your optimizer for a better generalization, .

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>The setting is the same as in Woodworth et al. [2020], HaoChen et al. [2020]</span></small>

<!-- page: 142 -->

One may wonder which components of the optimizers bias towards what type of global minima and what type of global minima may generalize better. These are open questions that researchers are actively investigating. Empirical and theoretical research have offered some clues and heuristics. In many (but definitely far from all) situations, among those setting where optimization can succeed in minimizing the training loss, the use of larger initial learning rate, smaller initialization, smaller batch size, and momentum appears to help with biasing towards more generalizable solutions. A conjecture (that can be proven in certain simplified case) is that stochasticity in the optimization process help the optimizer to find flatter global minima (global minima where the curvature of the loss is small), and flat global minima tend to give more Lipschitz models and better generalization. Characterizing the implicit regularization effect formally is still a challenging open research question.

## 9.3 Model selection via cross validation

Suppose we are trying select among several different models for a learning problem. For instance, we might be using a polynomial regression model $h _ { \theta } ( x )   =   g ( \theta _ { 0 }   +   \theta _ { 1 } x   +   \theta _ { 2 } x ^ { 2 }   +   \cdots   +   \theta _ { k } x ^ { k } )$ , and wish to decide if k should be $0 ,   1 ,   \ldots ,$ or 10. How can we automatically select a model that represents a good tradeoff between the twin evils of bias and variance<sup>5</sup>? Alternatively, suppose we want to automatically choose the bandwidth parameter τ for locally weighted regression, or the parameter C for our \`1-regularized SVM. How can we do that?

For the sake of concreteness, in these notes we assume we have some finite set of models $\mathcal { M }   =   \{ M _ { 1 } , \ldots , M _ { d } \}$ that we’re trying to select among. For instance, in our first example above, the model $M _ { i }$ would be an i-th degree polynomial regression model. (The generalization to infinite M is not hard.<sup>6</sup>) Alternatively, if we are trying to decide between using an SVM, a neural network or logistic regression, then M may contain these models.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">R+</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>Given that we said in the previous set of notes that bias and variance are two very different beasts, some readers may be wondering if we should be calling them “twin” evils here. Perhaps it’d be better to think of them as non-identical twins. The phrase “the fraternal twin evils of bias and variance” doesn’t have the same ring to it, though.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>6</sup>If we are trying to choose from an infinite set of models, say corresponding to the possible values of the bandwidth τ ∈ , we may discretize τ and consider only a finite number of possible values for it. More generally, most of the algorithms described here can all be viewed as performing optimization search in the space of models, and we can perform this search over infinite model classes as well.</span></small>

<!-- page: 143 -->

Cross validation. Lets suppose we are, as usual, given a training set S. Given what we know about empirical risk minimization, here’s what might initially seem like a algorithm, resulting from using empirical risk minimization for model selection:

1. Train each model $M _ { i }$ on $S ,$ to get some hypothesis $h _ { i }$

2. Pick the hypotheses with the smallest training error.

This algorithm does not work. Consider choosing the degree of a polynomial. The higher the degree of the polynomial, the better it will fit the training set S, and thus the lower the training error. Hence, this method will always select a high-variance, high-degree polynomial model, which we saw previously is often poor choice.

Here’s an algorithm that works better. In hold-out cross validation (also called simple cross validation), we do the following:

1. Randomly split S into $S _ { \mathrm { t r a i n } }$ (say, 70% of the data) and $S _ { \mathrm { c v } }$ (the remaining 30%). Here, $S _ { \mathrm { c v } }$ is called the hold-out cross validation set.

2. Train each model $M _ { i }$ on $S _ { \mathrm { t r a i n } }$ only, to get some hypothesis $h _ { i }$

3. Select and output the hypothesis $h _ { i }$ that had the smallest error $\hat { \varepsilon } _ { S _ { \mathrm { c v } } } ( h _ { i } )$ on the hold out cross validation set. (Here $\hat { \varepsilon } _ { S _ { \mathrm { c v } } } ( h )$ denotes the average error of h on the set of examples in $S _ { \mathrm { c v } } . )$ The error on the hold out validation set is also referred to as the validation error.

By testing/validating on a set of examples $S _ { \mathrm { c v } }$ that the models were not trained on, we obtain a better estimate of each hypothesis $h _ { i }$ ’s true generalization/test error. Thus, this approach is essentially picking the model with the smallest estimated generalization/test error. The size of the validation set depends on the total number of available examples. Usually, somewhere between $1 / 4   -   1 / 3$ of the data is used in the hold out cross validation set, and 30% is a typical choice. However, when the total dataset is huge, validation set can be a smaller fraction of the total examples as long as the absolute number of validation examples is decent. For example, for the ImageNet dataset that has about 1M training images, the validation set is sometimes set to be 50K images, which is only about 5% of the total examples.

Optionally, step 3 in the algorithm may also be replaced with selecting the model $M _ { i }$ according to arg min<sub>i</sub> $\hat { \varepsilon } _ { S _ { \mathrm { c v } } } ( h _ { i } )$ , and then retraining $M _ { i }$ on the entire training set S. (This is often a good idea, with one exception being learning algorithms that are be very sensitive to perturbations of the initial

<!-- page: 144 -->

conditions and $\mathrm { { } _ { r } / o r }$ data. For these methods, $M _ { i }$ doing well on $S _ { \mathrm { t r a i n } }$ does not necessarily mean it will also do well on $S _ { \mathrm { c v } }$ , and it might be better to forgo this retraining step.)

The disadvantage of using hold out cross validation is that it “wastes” about 30% of the data. Even if we were to take the optional step of retraining the model on the entire training set, it’s still as if we’re trying to find a good model for a learning problem in which we had 0.7n training examples, rather than n training examples, since we’re testing models that were trained on only 0.7n examples each time. While this is fine if data is abundant and/or cheap, in learning problems in which data is scarce (consider a problem with $n = 2 0 ,   \mathrm { s a y } )$ , we’d like to do something better.

Here is a method, called k-fold cross validation, that holds out less data each time:

1. Randomly split $S$ into k disjoint subsets of $m / k$ training examples each. Lets call these subsets $S _ { 1 } , \ldots , S _ { k }$

2. For each model $M _ { i }$ , we evaluate it as follows:

For $j = 1 , \ldots , k$

Train the model $M _ { i }$ on $S _ { 1 } \cup \cdots \cup S _ { j - 1 } \cup S _ { j + 1 } \cup \cdots S _ { k } { ~ ( \operatorname { i . e . } ~ }$ , train on all the data except $S _ { j } )$ to get some hypothesis $h _ { i j }$

Test the hypothesis $h _ { i j }$ on $S _ { j }$ , to get $\hat { \varepsilon } _ { S _ { j } } ( h _ { i j } )$

The estimated generalization error of model $M _ { i }$ is then calculated as the average of the $\hat { \varepsilon } _ { S _ { j } } ( h _ { i j } ) \mathrm { { ' s } }$ (averaged over $j )$ .

3. Pick the model $M _ { i }$ with the lowest estimated generalization error, and retrain that model on the entire training set $S .$ The resulting hypothesis is then output as our final answer.

A typical choice for the number of folds to use here would be $k   =   1 0$ While the fraction of data held out each time is now 1/k—much smaller than before—this procedure may also be more computationally expensive than hold-out cross validation, since we now need train to each model k times.

While $k = 1 0$ is a commonly used choice, in problems in which data is really scarce, sometimes we will use the extreme choice of $k   =   m$ in order to leave out as little data as possible each time. In this setting, we would repeatedly train on all but one of the training examples in $S ,$ and test on that held-out example. The resulting $m = k$ errors are then averaged together to obtain our estimate of the generalization error of a model. This method has

<!-- page: 145 -->

its own name; since we’re holding out one training example at a time, this method is called leave-one-out cross validation.

Finally, even though we have described the different versions of cross validation as methods for selecting a model, they can also be used more simply to evaluate a single model or algorithm. For example, if you have implemented some learning algorithm and want to estimate how well it performs for your application (or if you have invented a novel learning algorithm and want to report in a technical paper how well it performs on various test sets), cross validation would give a reasonable way of doing so.

## 9.4 Bayesian statistics and regularization

In this section, we will talk about one more tool in our arsenal for our battle against overfitting.

At the beginning of the quarter, we talked about parameter fitting using maximum likelihood estimation (MLE), and chose our parameters according to

$$
\theta_ {\mathrm{MLE}} = \arg \max _ {\theta} \prod_ {i = 1} ^ {n} p (y ^ {(i)} | x ^ {(i)}; \theta).
$$

Throughout our subsequent discussions, we viewed θ as an unknown parameter of the world. This view of the $\theta$ as being constant-valued but unknown is taken in frequentist statistics. In the frequentist this view of the world, θ is not random—it just happens to be unknown—and it’s our job to come up with statistical procedures (such as maximum likelihood) to try to estimate this parameter.

An alternative way to approach our parameter estimation problems is to take the Bayesian view of the world, and think of $\theta$ as being a random variable whose value is unknown. In this approach, we would specify a prior distribution $p ( \theta )$ on $\theta$ that expresses our “prior beliefs” about the parameters. Given a training set $S = \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { n }$ , when we are asked to make a prediction on a new value of $x ,$ we can then compute the posterior distribution on the parameters

$$
\begin{array}{r c l} p (\theta | S) & = & \frac {p (S | \theta) p (\theta)}{p (S)} \\ & = & \frac {\left(\prod_ {i = 1} ^ {n} p (y ^ {(i)} | x ^ {(i)} , \theta)\right) p (\theta)}{\int_ {\theta} \left(\prod_ {i = 1} ^ {n} p (y ^ {(i)} | x ^ {(i)} , \theta) p (\theta)\right) d \theta} \end{array}\tag{9.3}
$$

In the equation above, $p ( y ^ { ( i ) } | x ^ { ( i ) } , \theta )$ comes from whatever model you’re using

<!-- page: 146 -->

for your learning problem. For example, if you are using Bayesian logistic regression, then you might choose $p(y^{(i)}|x^{(i)},\theta)=h_{\theta}(x^{(i)})^{\widetilde{y^{(i)}}}(1-h_{\theta}(x^{(i)})^{\widetilde{(1-y^{(i)})}})$ where $h _ { \theta } ( x ^ { ( i ) } ) = 1 / ( 1 + \exp ( - \theta ^ { T } \dot { x } ^ { ( i ) } ) ) . ]$ 7

When we are given a new test example x and asked to make it prediction on it, we can compute our posterior distribution on the class label using the posterior distribution on θ:

$$
p (y | x, S) = \int_ {\theta} p (y | x, \theta) p (\theta | S) d \theta\tag{9.4}
$$

In the equation above, $p ( \theta | S )$ comes from Equation (9.3). Thus, for example, if the goal is to the predict the expected value of y given x, then we would output<sup>8</sup>

$$
\operatorname{E} [ y | x, S ] = \int_ {y} y p (y | x, S) d y
$$

The procedure that we’ve outlined here can be thought of as doing “fully Bayesian” prediction, where our prediction is computed by taking an average with respect to the posterior $p ( \theta | S )$ over θ. Unfortunately, in general it is computationally very difficult to compute this posterior distribution. This is because it requires taking integrals over the (usually high-dimensional) $\theta$ as in Equation (9.3), and this typically cannot be done in closed-form.

Thus, in practice we will instead approximate the posterior distribution for θ. One common approximation is to replace our posterior distribution for $\theta$ (as in Equation 9.4) with a single point estimate. The MAP (maximum a posteriori) estimate for θ is given by

$$
\theta_ {\mathrm{MAP}} = \arg \max _ {\theta} \prod_ {i = 1} ^ {n} p (y ^ {(i)} | x ^ {(i)}, \theta) p (\theta).\tag{9.5}
$$

Note that this is the same formulas as for the MLE (maximum likelihood) estimate for $\theta ,$ except for the prior $p ( \theta )$ term at the end.

In practical applications, a common choice for the prior $p ( \theta )$ is to assume that $\theta \sim \mathcal { N } ( 0 , \tau ^ { 2 } I )$ . Using this choice of prior, the fitted parameters $\theta _ { \mathrm { M A P } }$ will have smaller norm than that selected by maximum likelihood. In practice, this causes the Bayesian MAP estimate to be less susceptible to overfitting than the ML estimate of the parameters. For example, Bayesian logistic regression turns out to be an effective algorithm for text classification, even though in text classification we usually have d $\gg n .$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“p(y|x, )”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">“p(y|x; ).”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>Since we are now viewing θ as a random variable, it is okay to condition on it value, and write θ instead of θ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>8</sup>The integral below would be replaced by a summation if y is discrete-valued.</span></small>

<!-- page: 147 -->

Part IV

Unsupervised learning

<!-- page: 148 -->

Chapter 10

# Clustering and the k-means algorithm

In the clustering problem, we are given a training set $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \}$ , and want to group the data into a few cohesive “clusters.” Here, $\boldsymbol { x } ^ { ( i ) ^ { \cdot } } \in \mathbb { R } ^ { d }$ as usual; but no labels $y ^ { ( i ) }$ are given. So, this is an unsupervised learning problem.

The k-means clustering algorithm is as follows:

1. Initialize cluster centroids $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { k } \in \mathbb { R } ^ { d }$ randomly.

2. Repeat until convergence: {

For every $i ,$ set

$$
c ^ {(i)} := \arg \min _ {j} | | x ^ {(i)} - \mu_ {j} | | ^ {2}.
$$

For each $j ,$ set

$$
\mu_ {j} := \frac {\sum_ {i = 1} ^ {n} 1 \{c ^ {(i)} = j \} x ^ {(i)}}{\sum_ {i = 1} ^ {n} 1 \{c ^ {(i)} = j \}}.
$$

In the algorithm above, k (a parameter of the algorithm) is the number of clusters we want to find; and the cluster centroids $\mu _ { j }$ represent our current guesses for the positions of the centers of the clusters. To initialize the cluster centroids (in step 1 of the algorithm above), we could choose k training examples randomly, and set the cluster centroids to be equal to the values of these k examples. (Other initialization methods are also possible.)

The inner-loop of the algorithm repeatedly carries out two steps: (i) “Assigning” each training example $x ^ { ( i ) }$ to the closest cluster centroid $\mu _ { j }$ , and

<!-- page: 149 -->

![](images/page_148_image_1.jpg)

Figure 10.1: K-means algorithm. Training examples are shown as dots, and cluster centroids are shown as crosses. (a) Original dataset. (b) Random initial cluster centroids (in this instance, not chosen to be equal to two training examples). (c-f) Illustration of running two iterations of k-means. In each iteration, we assign each training example to the closest cluster centroid (shown by “painting” the training examples the same color as the cluster centroid to which is assigned); then we move each cluster centroid to the mean of the points assigned to it. (Best viewed in color.) Images courtesy Michael Jordan.

(ii) Moving each cluster centroid $\mu _ { j }$ to the mean of the points assigned to it. Figure 10.1 shows an illustration of running k-means.

Is the k-means algorithm guaranteed to converge? Yes it is, in a certain sense. In particular, let us define the distortion function to be:

$$
J (c, \mu) = \sum_ {i = 1} ^ {n} | | x ^ {(i)} - \mu_ {c ^ {(i)}} | | ^ {2}
$$

Thus, J measures the sum of squared distances between each training example $x ^ { ( i ) }$ and the cluster centroid $\mu _ { c ^ { ( i ) } }$ to which it has been assigned. It can be shown that k-means is exactly coordinate descent on J. Specifically, the inner-loop of k-means repeatedly minimizes J with respect to c while holding $\mu$ fixed, and then minimizes J with respect to $\mu$ while holding c fixed. Thus,

<!-- page: 150 -->

J must monotonically decrease, and the value of J must converge. (Usually, this implies that c and $\mu$ will converge too. In theory, it is possible for k-means to oscillate between a few different clusterings—i.e., a few different values for c and/or µ—that have exactly the same value of J, but this almost never happens in practice.)

The distortion function J is a non-convex function, and so coordinate descent on J is not guaranteed to converge to the global minimum. In other words, k-means can be susceptible to local optima. Very often k-means will work fine and come up with very good clusterings despite this. But if you are worried about getting stuck in bad local minima, one common thing to do is run k-means many times (using different random initial values for the cluster centroids $\mu _ { j } )$ . Then, out of all the different clusterings found, pick the one that gives the lowest distortion $J ( c , \mu )$

<!-- page: 151 -->

# Chapter 11

## EM algorithms

In this set of notes, we discuss the EM (Expectation-Maximization) algorithm for density estimation.

## 11.1 EM for mixture of Gaussians

Suppose that we are given a training set $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \}$ as usual. Since we are in the unsupervised learning setting, these points do not come with any labels.

We wish to model the data by specifying a joint distribution $p ( x ^ { ( i ) } , z ^ { ( i ) } ) =$ $p ( x ^ { ( i ) } | z ^ { ( i ) } ) p ( z ^ { ( i ) } )$ . Here, $z ^ { ( i ) } \sim$ Multinomial(φ) (where $\begin{array} { r } { \phi _ { j } \geq 0 ,   \sum _ { j = 1 } ^ { k } \phi _ { j } = 1 } \end{array}$ and the parameter $\phi _ { j }$ gives $p ( z ^ { ( i ) } = j ) )$ , and $\boldsymbol { x } ^ { ( i ) } | \boldsymbol { z } ^ { ( i ) } = \boldsymbol { j } \sim \mathcal { N } ( \boldsymbol { \dot { \mu _ { j } } } , \boldsymbol { \Sigma _ { j } } )$ . We let k denote the number of values that the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ can take on. Thus, our model posits that each $x ^ { ( i ) }$ was generated by randomly choosing $z ^ { ( i ) }$ from $\{ 1 , \ldots , k \}$ , and then $x ^ { ( i ) }$ was drawn from one of k Gaussians depending on $z ^ { ( i ) }$ . This is called the mixture of Gaussians model. Also, note that the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ are latent random variables, meaning that they’re hidden/unobserved. This is what will make our estimation problem difficult.

The parameters of our model are thus $\phi ,   \mu$ and Σ. To estimate them, we can write down the likelihood of our data:

$$
\begin{array}{r c l} \ell (\phi , \mu , \Sigma) & = & \sum_ {i = 1} ^ {n} \log p (x ^ {(i)}; \phi , \mu , \Sigma) \\ & = & \sum_ {i = 1} ^ {n} \log \sum_ {z ^ {(i)} = 1} ^ {k} p (x ^ {(i)} | z ^ {(i)}; \mu , \Sigma) p (z ^ {(i)}; \phi). \end{array}
$$

However, if we set to zero the derivatives of this formula with respect to

<!-- page: 152 -->

the parameters and try to solve, we’ll find that it is not possible to find the maximum likelihood estimates of the parameters in closed form. (Try this yourself at home.)

The random variables $z ^ { ( i ) }$ indicate which of the k Gaussians each $x ^ { ( i ) }$ had come from. Note that if we knew what the $z ^ { ( i ) } !$ ’s were, the maximum likelihood problem would have been easy. Specifically, we could then write down the likelihood as

$$
\ell (\phi , \mu , \Sigma) = \sum_ {i = 1} ^ {n} \log p (x ^ {(i)} | z ^ {(i)}; \mu , \Sigma) + \log p (z ^ {(i)}; \phi).
$$

Maximizing this with respect to $\phi ,   \mu$ and Σ gives the parameters:

$$
\begin{array}{r c l} \phi_ {j} & = & \frac {1}{n} \sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \}, \\ \mu_ {j} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \} x ^ {(i)}}{\sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \}}, \\ \Sigma_ {j} & = & \frac {\sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \} (x ^ {(i)} - \mu_ {j}) (x ^ {(i)} - \mu_ {j}) ^ {T}}{\sum_ {i = 1} ^ {n} 1 \{z ^ {(i)} = j \}}. \end{array}
$$

Indeed, we see that if the $z ^ { ( i ) } \mathrm { { ^ \circ S } }$ were known, then maximum likelihood estimation becomes nearly identical to what we had when estimating the parameters of the Gaussian discriminant analysis model, except that here the $z ^ { ( i ) } { } ^ { \flat } \mathfrak { z }$ s playing the role of the class labels.<sup>1</sup>

However, in our density estimation problem, the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ are not known. What can we do?

The EM algorithm is an iterative algorithm that has two main steps. Applied to our problem, in the E-step, it tries to “guess” the values of the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ . In the M-step, it updates the parameters of our model based on our guesses. Since in the M-step we are pretending that the guesses in the first part were correct, the maximization becomes easy. Here’s the algorithm:

Repeat until convergence: {

(E-step) For each $i , j ,$ set

$$
w _ {j} ^ {(i)} := p (z ^ {(i)} = j | x ^ {(i)}; \phi , \mu , \Sigma)
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i)’</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">j</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>There are other minor differences in the formulas here from what we’d obtained in PS1 with Gaussian discriminant analysis, first because we’ve generalized the z s to be multinomial rather than Bernoulli, and second because here we are using a different Σ for each Gaussian.</span></small>

<!-- page: 153 -->

(M-step) Update the parameters:

$$
\begin{array}{r c l} \phi_ {j} & := & \frac {1}{n} \sum_ {i = 1} ^ {n} w _ {j} ^ {(i)}, \\ \mu_ {j} & := & \frac {\sum_ {i = 1} ^ {n} w _ {j} ^ {(i)} x ^ {(i)}}{\sum_ {i = 1} ^ {n} w _ {j} ^ {(i)}}, \\ \Sigma_ {j} & := & \frac {\sum_ {i = 1} ^ {n} w _ {j} ^ {(i)} (x ^ {(i)} - \mu_ {j}) (x ^ {(i)} - \mu_ {j}) ^ {T}}{\sum_ {i = 1} ^ {n} w _ {j} ^ {(i)}} \end{array}
$$

}

In the E-step, we calculate the posterior probability of our parameters the $z ^ { ( i ) } { } ^ { \gamma } \mathrm { s } ,$ given the $x ^ { ( i ) }$ and using the current setting of our parameters. I.e., using Bayes rule, we obtain:

$$
p (z ^ {(i)} = j | x ^ {(i)}; \phi , \mu , \Sigma) = \frac {p (x ^ {(i)} | z ^ {(i)} = j ; \mu , \Sigma) p (z ^ {(i)} = j ; \phi)}{\sum_ {l = 1} ^ {k} p (x ^ {(i)} | z ^ {(i)} = l ; \mu , \Sigma) p (z ^ {(i)} = l ; \phi)}
$$

Here, $p ( x ^ { ( i ) } | z ^ { ( i ) }   =   j ; \mu , \Sigma )$ is given by evaluating the density of a Gaussian with mean $\mu _ { j }$ and covariance $\Sigma _ { j }$ at $x ^ { ( i ) } ;   p ( z ^ { ( i ) } = j ; \phi )$ is given by $\phi _ { j } ,$ and so on. The values $w _ { j } ^ { ( i ) }$ calculated in the E-step represent our “soft” guesses<sup>2</sup>for the values of $z ^ { ( i ) }$ .

Also, you should contrast the updates in the M-step with the formulas we had when the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ were known exactly. They are identical, except that instead of the indicator functions $``1\{z^{(i)} = j\}$ indicating from which Gaussian each datapoint had come, we now instead have the $w _ { j } ^ { ( i ) } { } ^ { \mathrm { { , } } } \mathrm { { s } }$

The EM-algorithm is also reminiscent of the K-means clustering algorithm, except that instead of the “hard” cluster assignments $c ( i )$ , we instead have the “soft” assignments $w _ { j } ^ { ( i ) }$ . Similar to K-means, it is also susceptible to local optima, so reinitializing at several different initial parameters may be a good idea.

It’s clear that the EM algorithm has a very natural interpretation of repeatedly trying to guess the unknown $z ^ { ( i ) } { } ^ { \flat } \mathrm { S } _ { \mathfrak { z } } ^ { \flat }$ but how did it come about, and can we make any guarantees about it, such as regarding its convergence? In the next set of notes, we will describe a more general view of EM, one

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1, . . . , k</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>The term “soft” refers to our guesses being probabilities and taking values in [0, 1]; in contrast, a “hard” guess is one that represents a single best guess (such as taking values in {0, 1} or { }).</span></small>

<!-- page: 154 -->

that will allow us to easily apply it to other estimation problems in which there are also latent variables, and which will allow us to give a convergence guarantee.

## 11.2 Jensen’s inequality

We begin our discussion with a very useful result called Jensen’s inequality

Let $f$ be a function whose domain is the set of real numbers. Recall that $f$ is a convex function if $f''(x) \geq 0$ (for all $x \in \mathbb { R } )$ . In the case of $f$ taking vector-valued inputs, this is generalized to the condition that its hessian H is positive semi-definite $( H \geq 0 )$ . If $f ^ { \prime \prime } ( x )   >   0$ for all $x ,$ then we say $f$ is strictly convex (in the vector-valued case, the corresponding statement is that H must be positive definite, written $H > 0 )$ . Jensen’s inequality can then be stated as follows:

Theorem. Let $f$ be a convex function, and let X be a random variable. Then:

$$
\mathrm{E} [ f (X) ] \geq f (\mathrm{E} X).
$$

Moreover, if $f$ is strictly convex, then $\mathrm { E } [ f ( X ) ]   =   f ( \mathrm { E } X )$ holds true if and only if $X = \operatorname { E } [ X ]$ with probability $1 ( i.e., if  X$ is a constant).

Recall our convention of occasionally dropping the parentheses when writing expectations, so in the theorem above, $f(\mathrm{E}X) = f(\mathrm{E}[X])$

For an interpretation of the theorem, consider the figure below.

![](images/page_153_chart_10.jpg)

Here, $f$ is a convex function shown by the solid line. Also, X is a random variable that has a 0.5 chance of taking the value $a ,$ and a 0.5 chance of

<!-- page: 155 -->

taking the value b (indicated on the x-axis). Thus, the expected value of X is given by the midpoint between a and $b .$

We also see the values $f(a), \; f(b)$ and $f ( \operatorname { E } [ X ] )$ indicated on the y-axis. Moreover, the value $\mathrm{E}[f(X)]$ is now the midpoint on the y-axis between $f ( a )$ and $f ( b )$ . From our example, we see that because $f$ is convex, it must be the case that $\mathrm{E}[f(X)] \geq f(\mathrm{E}X)$

Incidentally, quite a lot of people have trouble remembering which way the inequality goes, and remembering a picture like this is a good way to quickly figure out the answer.

Remark. Recall that f is [strictly] concave if and only if −f is [strictly] convex $(i.e., $f''(x) \leq 0 \mathrm{~or~} H \leq 0)$$ . Jensen’s inequality also holds for concave functions $f ,$ but with the direction of all the inequalities reversed $\left( \mathrm{E}[f(X)] \leq \right.$ f(EX), etc.).

## 11.3 General EM algorithms

Suppose we have an estimation problem in which we have a training set $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \}$ consisting of n independent examples. We have a latent variable model $p ( x , z ; \theta )$ with z being the latent variable (which for simplicity is assumed to take finite number of values). The density for x can be obtained by marginalized over the latent variable z:

$$
p (x; \theta) = \sum_ {z} p (x, z; \theta)\tag{11.1}
$$

We wish to fit the parameters θ by maximizing the log-likelihood of the data, defined by

$$
\ell (\theta) = \sum_ {i = 1} ^ {n} \log p (x ^ {(i)}; \theta)\tag{11.2}
$$

We can rewrite the objective in terms of the joint density $p ( x , z ; \theta )$ by

$$
\begin{array}{r c l} \ell (\theta) & = & \sum_ {i = 1} ^ {n} \log p (x ^ {(i)}; \theta) \\ & = & \sum_ {i = 1} ^ {n} \log \sum_ {z ^ {(i)}} p (x ^ {(i)}, z ^ {(i)}; \theta). \end{array}\tag{11.3}
$$

(11.4)

But, explicitly finding the maximum likelihood estimates of the parameters $\theta$ may be hard since it will result in difficult non-convex optimization prob-

<!-- page: 156 -->

lems.<sup>3</sup> Here, the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ are the latent random variables; and it is often the case that if the $z ^ { ( i ) } \mathrm { { ^ \circ S } }$ were observed, then maximum likelihood estimation would be easy.

In such a setting, the EM algorithm gives an efficient method for max imum likelihood estimation. Maximizing \`(θ) explicitly might be difficult, and our strategy will be to instead repeatedly construct a lower-bound on \` (E-step), and then optimize that lower-bound (M-step).<sup>4</sup>

It turns out that the summation $\Sigma _ { i = 1 } ^ { n }$ is not essential here, and towards a simpler exposition of the EM algorithm, we will first consider optimizing the likelihood log $p ( x )$ for a single example x. After we derive the algorithm for optimizing log $p ( x )$ , we will convert it to an algorithm that works for n examples by adding back the sum to each of the relevant equations. Thus, now we aim to optimize log $p ( x ; \theta )$ which can be rewritten as

$$
\log p (x; \theta) = \log \sum_ {z} p (x, z; \theta)\tag{11.5}
$$

Let Q be a distribution over the possible values of z. That is, $\begin{array} { r } { \sum _ { z } Q ( z ) = 1 } \end{array}$ $Q ( z ) \geq 0 )$

Consider the following:<sup>5</sup>

$$
\begin{array}{r c l} \log p (x; \theta) & = & \log \sum_ {z} p (x, z; \theta) \\ & = & \log \sum_ {z} Q (z) \frac {p (x , z ; \theta)}{Q (z)} \\ & \geq & \sum_ {z} Q (z) \log \frac {p (x , z ; \theta)}{Q (z)} \end{array}\tag{11.6}
$$

(11.7)

The last step of this derivation used Jensen’s inequality. Specifically, $f ( x ) = \log x$ is a concave function, since $f''(x) = -1/x^2 < 0$ over its domain

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>It’s mostly an empirical observation that the optimization problem is difficult to optimize.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\`(·)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">\` .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>Empirically, the E-step and M-step can often be computed more efficiently than optimizing the function  directly. However, it doesn’t necessarily mean that alternating the two steps can always converge to the global optimum of (·) Even for mixture of Gaussians, the EM algorithm can either converge to a global optimum or get stuck, depending on the properties of the training data. Empirically, for real-world data, often EM can converge to a solution with relatively high likelihood (if not the optimum), and the theory behind it is still largely not understood.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Q</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>If z were continuous, then  would be a density, and the summations over z in our discussion are replaced with integrals over z.</span></small>

<!-- page: 157 -->

$x \in \mathbb { R } ^ { + }$ . Also, the term

$$
\sum_ {z} Q (z) \left[ \frac {p (x , z ; \theta)}{Q (z)} \right]
$$

in the summation is just an expectation of the quantity $[ p ( x , z ; \theta ) / Q ( z ) ]$ with respect to z drawn according to the distribution given by $Q . ^ { 6 }$ By Jensen’s inequality, we have

$$
f \left(\mathrm{E} _ {z \sim Q} \left[ \frac {p (x , z ; \theta)}{Q (z)} \right]\right) \geq \mathrm{E} _ {z \sim Q} \left[ f \left(\frac {p (x , z ; \theta)}{Q (z)}\right) \right],
$$

where the $\text{" } z \sim Q \text{" }$ subscripts above indicate that the expectations are with respect to z drawn from $Q .$ This allowed us to go from Equation (11.6) to Equation (11.7).

Now, for any distribution $Q ,$ the formula (11.7) gives a lower-bound on log $p ( x ; \theta )$ . There are many possible choices for the $Q ^ { \flat } \mathrm { s }$ . Which should we choose? Well, if we have some current guess $\theta$ of the parameters, it seems natural to try to make the lower-bound tight at that value of θ. I.e., we will make the inequality above hold with equality at our particular value of $\theta .$

To make the bound tight for a particular value of $\theta ,$ we need for the step involving Jensen’s inequality in our derivation above to hold with equality. For this to be true, we know it is sufficient that the expectation be taken over a “constant”-valued random variable. I.e., we require that

$$
\frac {p (x , z ; \theta)}{Q (z)} = c
$$

for some constant c that does not depend on z. This is easily accomplished by choosing

$$
Q (z) \propto p (x, z; \theta).
$$

Actually, since we know $\textstyle \sum _ { z } Q ( z ) \; = \; 1$ (because it is a distribution), this further tells us that

$$
\begin{array}{r c l} Q (z) & = & \frac {p (x , z ; \theta)}{\sum_ {z} p (x , z ; \theta)} \\ & = & \frac {p (x , z ; \theta)}{p (x ; \theta)} \\ & = & p (z | x; \theta) \end{array}\tag{11.8}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Q</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Q(z) 6=</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6We note that the notion $\begin{array} { r } { \frac { p ( x , z ; \theta ) } { Q ( z ) } } \end{array}$ only makes sense if 0 whenever p( . x, z; θ) 6= 0 Here we implicitly assume that we only consider those  with such a property.</span></small>

<!-- page: 158 -->

Thus, we simply set the $Q ^ { \flat } \mathrm { s }$ to be the posterior distribution of the z’s given x and the setting of the parameters $\theta .$

Indeed, we can directly verify that when $Q ( z )   =   p ( z | x ; \theta )$ , then equation (11.7) is an equality because

$$
\begin{array}{l} \sum_ {z} Q (z) \log \frac {p (x , z ; \theta)}{Q (z)} = \sum_ {z} p (z | x; \theta) \log \frac {p (x , z ; \theta)}{p (z | x ; \theta)} \\ \qquad = \sum_ {z} p (z | x; \theta) \log \frac {p (z | x ; \theta) p (x ; \theta)}{p (z | x ; \theta)} \\ \qquad = \sum_ {z} p (z | x; \theta) \log p (x; \theta) \\ \qquad = \log p (x; \theta) \sum_ {z} p (z | x; \theta) \\ \qquad = \log p (x; \theta) \qquad (\text {because} \sum_ {z} p (z | x; \theta) = 1) \end{array}
$$

For convenience, we call the expression in Equation (11.7) the evidence lower bound (ELBO) and we denote it by

$$
\mathrm{ELBO} (x; Q, \theta) = \sum_ {z} Q (z) \log \frac {p (x , z ; \theta)}{Q (z)}\tag{11.9}
$$

With this equation, we can re-write equation (11.7) as

$$
\forall Q, \theta , x, \quad \log p (x; \theta) \geq \operatorname{ELBO} (x; Q, \theta)\tag{11.10}
$$

Intuitively, the EM algorithm alternatively updates $Q$ and θ by a) setting $Q ( z )   =   p ( z | x ; \theta )$ following Equation (11.8) so that $\mathrm { E L B O } ( x ; Q , \theta )   =$ log $p ( x ; \theta )$ for $x$ and the current $\theta ,$ and b) maximizing $\operatorname { E L B O } ( x ; Q , \theta )$ w.r.t $\theta$ while fixing the choice of $Q$

Recall that all the discussion above was under the assumption that we aim to optimize the log-likelihood log $p ( x ; \theta )$ for a single example x. It turns out that with multiple training examples, the basic idea is the same and we only need to take a sum over examples at relevant places. Next, we will build the evidence lower bound for multiple training examples and make the EM algorithm formal.

Recall we have a training set $\{ x ^ { ( 1 ) } , \ldots , x ^ { ( n ) } \}$ . Note that the optimal choice of $Q$ is $p ( z | x ; \theta )$ , and it depends on the particular example x. Therefore here we will introduce $n$ distributions $Q _ { 1 } , \ldots , Q _ { n } ,$ one for each example $x ^ { ( i ) }$ . For each example $x ^ { ( i ) }$ , we can build the evidence lower bound

$$
\log p (x ^ {(i)}; \theta) \geq \mathrm{ELBO} (x ^ {(i)}; Q _ {i}, \theta) = \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})}
$$

<!-- page: 159 -->

Taking sum over all the examples, we obtain a lower bound for the loglikelihood

$$
\begin{array}{l} \ell (\theta) \geq \sum_ {i} \mathrm{ELBO} (x ^ {(i)}; Q _ {i}, \theta) \\ = \sum_ {i} \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})} \end{array}\tag{11.11}
$$

For $a n y$ set of distributions $Q _ { 1 } , \ldots , Q _ { n }$ , the formula (11.11) gives a lowerbound on $\ell ( \theta )$ , and analogous to the argument around equation (11.8), the $Q _ { i }$ that attains equality satisfies

$$
Q _ {i} (z ^ {(i)}) = p (z ^ {(i)} | x ^ {(i)}; \theta)
$$

Thus, we simply set the $Q _ { i } { } ^ { \prime } \mathrm { s }$ to be the posterior distribution of the $z ^ { ( i ) } \mathrm { ^ { \prime } s }$ given $x ^ { ( i ) }$ with the current setting of the parameters $\theta .$

Now, for this choice of the $Q _ { i } { } ^ { \mathfrak { j } } \mathrm { S } _ { \mathfrak { j } }$ , Equation (11.11) gives a lower-bound on the loglikelihood \` that we’re trying to maximize. This is the E-step. In the M-step of the algorithm, we then maximize our formula in Equation (11.11) with respect to the parameters to obtain a new setting of the $\theta ^ { \prime } \mathrm { s }$ . Repeatedly carrying out these two steps gives us the EM algorithm, which is as follows:

Repeat until convergence {

(E-step) For each $i ,$ set

$$
Q _ {i} (z ^ {(i)}) := p (z ^ {(i)} | x ^ {(i)}; \theta).
$$

(M-step) Set

$$
\begin{array}{l} \theta := \arg \max _ {\theta} \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i}, \theta) \\ \quad = \arg \max _ {\theta} \sum_ {i} \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})}. \end{array}\tag{11.12}
$$

How do we know if this algorithm will converge? Well, suppose $\theta ^ { ( t ) }$ and $\theta ^ { ( t + 1 ) }$ are the parameters from two successive iterations of EM. We will now prove that $\ell ( \bar { \theta } ^ { ( t ) } ) \; \leq \; \ell ( \theta ^ { ( t + 1 ) } )$ , which shows EM always monotonically improves the log-likelihood. The key to showing this result lies in our choice of

<!-- page: 160 -->

the $Q _ { i } { } ^ { \flat } \mathrm { S } .$ . Specifically, on the iteration of EM in which the parameters had started out as $\theta ^ { ( t ) }$ , we would have chosen $Q _ { i } ^ { ( t ) } ( z ^ { ( i ) } )   : =   p ( z ^ { ( \hat { i } ) } | x ^ { ( i ) } ; \theta ^ { ( t ) } )$ . We saw earlier that this choice ensures that Jensen’s inequality, as applied to get Equation (11.11), holds with equality, and hence

$$
\ell (\theta^ {(t)}) = \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i} ^ {(t)}, \theta^ {(t)})\tag{11.13}
$$

The parameters $\theta ^ { ( t + 1 ) }$ are then obtained by maximizing the right hand side of the equation above. Thus,

$$
\begin{array}{l l} \ell (\theta^ {(t + 1)}) \geq \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i} ^ {(t)}, \theta^ {(t + 1)}) \\ & \text {(because inequality (11.11) holds for all Q and \theta)} \\ \geq \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i} ^ {(t)}, \theta^ {(t)}) & \text {(see reason below)} \\ = \ell (\theta^ {(t)}) & \text {(by equation (11.13))} \end{array}
$$

where the last inequality follows from that $\theta ^ { ( t + 1 ) }$ is chosen explicitly to be

$$
\arg \max _ {\theta} \quad \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i} ^ {(t)}, \theta)
$$

Hence, EM causes the likelihood to converge monotonically. In our description of the EM algorithm, we said we’d run it until convergence. Given the result that we just showed, one reasonable convergence test would be to check if the increase in $\ell ( \theta )$ between successive iterations is smaller than some tolerance parameter, and to declare convergence if EM is improving $\ell ( \theta )$ too slowly.

Remark. If we define (by overloading ELBO(·))

$$
\mathrm{ELBO} (Q, \theta) = \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i}, \theta) = \sum_ {i} \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})}\tag{11.14}
$$

then we know $\ell ( \theta )   \geq   \mathrm { E L B O } ( Q , \theta )$ from our previous derivation. The EM can also be viewed an alternating maximization algorithm on $\operatorname { E L B O } ( Q , \theta )$ , in which the E-step maximizes it with respect to $Q$ (check this yourself), and the M-step maximizes it with respect to $\theta .$

<!-- page: 161 -->

## 11.3.1 Other interpretation of ELBO

Let EL $\begin{array} { r } { \mathrm { { } _ { \mathrm { \scriptsize ~ \cdot } } B O } \big ( x ; Q , \theta \big ) \; = \; \sum _ { z } Q \big ( z \big ) \log \frac { p ( x , z ; \theta ) } { Q ( z ) } } \end{array}$ be defined as in equation (11.9). There are several other forms of ELBO. First, we can rewrite

$$
\begin{array}{r} \mathrm{ELBO} (x; Q, \theta) = \mathrm{E} _ {z \sim Q} [ \log p (x, z; \theta) ] - \mathrm{E} _ {z \sim Q} [ \log Q (z) ] \\ = \mathrm{E} _ {z \sim Q} [ \log p (x | z; \theta) ] - D _ {K L} (Q \| p _ {z}) \end{array}\tag{11.15}
$$

where we use $p _ { z }$ to denote the marginal distribution of z (under the distribution $p ( x , z ; \theta ) )$ , and $D _ { K L } ( { \bf \Lambda } )$ denotes the KL divergence

$$
D _ {K L} (Q \| p _ {z}) = \sum_ {z} Q (z) \log \frac {Q (z)}{p (z)}\tag{11.16}
$$

In many cases, the marginal distribution of $z$ does not depend on the parameter $\theta .$ In this case, we can see that maximizing ELBO over $\theta$ is equivalent to maximizing the first term in (11.15). This corresponds to maximizing the conditional likelihood of $x$ conditioned on $z ,$ which is often a simpler question than the original question.

Another form of ELBO(·) is (please verify yourself)

$$
\mathrm{ELBO} (x; Q, \theta) = \log p (x) - D _ {K L} (Q \| p _ {z | x})\tag{11.17}
$$

where $p _ { z | x }$ is the conditional distribution of $\gtrsim \mathrm { g i }$ ven $x$ under the parameter $\theta .$ This forms shows that the maximizer of EL $\mathrm { { \mu } B O } ( Q , \theta )$ over $Q$ is obtained when $Q = p _ { z | x }$ , which was shown in equation (11.8) before.

## 11.4 Mixture of Gaussians revisited

Armed with our general definition of the EM algorithm, let’s go back to our old example of fitting the parameters $\phi ,   \mu$ and $\Sigma$ in a mixture of Gaussians. For the sake of brevity, we carry out the derivations for the M-step updates only for $\phi$ and $\mu _ { j }$ , and leave the updates for $\Sigma _ { j }$ as an exercise for the reader.

The E-step is easy. Following our algorithm derivation above, we simply calculate

$$
w _ {j} ^ {(i)} = Q _ {i} (z ^ {(i)} = j) = P (z ^ {(i)} = j | x ^ {(i)}; \phi , \mu , \Sigma).
$$

Here, $\text{" }Q_{i}(z^{(i)}=j) \text{" }$ denotes the probability of $z ^ { ( i ) }$ taking the value $j$ under the distribution $Q _ { i }$

<!-- page: 162 -->

Next, in the M-step, we need to maximize, with respect to our parameters $\phi , \mu , \Sigma$ , the quantity

$$
\begin{array}{l} \sum_ {i = 1} ^ {n} \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \phi , \mu , \Sigma)}{Q _ {i} (z ^ {(i)})} \\ \qquad = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} Q _ {i} (z ^ {(i)} = j) \log \frac {p (x ^ {(i)} | z ^ {(i)} = j ; \mu , \Sigma) p (z ^ {(i)} = j ; \phi)}{Q _ {i} (z ^ {(i)} = j)} \\ \qquad = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} w _ {j} ^ {(i)} \log \frac {\frac {1}{(2 \pi) ^ {d / 2} | \Sigma_ {j} | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x ^ {(i)} - \mu_ {j}) ^ {T} \Sigma_ {j} ^ {- 1} (x ^ {(i)} - \mu_ {j})\right) \cdot \phi_ {j}}{w _ {j} ^ {(i)}} \end{array}
$$

Let’s maximize this with respect to $\mu _ { l } .$ . If we take the derivative with respect to $\mu _ { l } ,$ , we find

$$
\begin{array}{l} \nabla_ {\mu_ {l}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} w _ {j} ^ {(i)} \log \frac {\frac {1}{(2 \pi) ^ {d / 2} | \Sigma_ {j} | ^ {1 / 2}} \exp \left(- \frac {1}{2} (x ^ {(i)} - \mu_ {j}) ^ {T} \Sigma_ {j} ^ {- 1} (x ^ {(i)} - \mu_ {j})\right) \cdot \phi_ {j}}{w _ {j} ^ {(i)}} \\ = - \nabla_ {\mu_ {l}} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} w _ {j} ^ {(i)} \frac {1}{2} (x ^ {(i)} - \mu_ {j}) ^ {T} \Sigma_ {j} ^ {- 1} (x ^ {(i)} - \mu_ {j}) \\ = \frac {1}{2} \sum_ {i = 1} ^ {n} w _ {l} ^ {(i)} \nabla_ {\mu_ {l}} 2 \mu_ {l} ^ {T} \Sigma_ {l} ^ {- 1} x ^ {(i)} - \mu_ {l} ^ {T} \Sigma_ {l} ^ {- 1} \mu_ {l} \\ = \sum_ {i = 1} ^ {n} w _ {l} ^ {(i)} \left(\Sigma_ {l} ^ {- 1} x ^ {(i)} - \Sigma_ {l} ^ {- 1} \mu_ {l}\right) \end{array}
$$

Setting this to zero and solving for $\mu _ { l }$ therefore yields the update rule

$$
\mu_ {l} := \frac {\sum_ {i = 1} ^ {n} w _ {l} ^ {(i)} x ^ {(i)}}{\sum_ {i = 1} ^ {n} w _ {l} ^ {(i)}},
$$

which was what we had in the previous set of notes.

Let’s do one more example, and derive the M-step update for the parameters $\phi _ { j }$ . Grouping together only the terms that depend on $\phi _ { j }$ , we find that we need to maximize

$$
\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} w _ {j} ^ {(i)} \log \phi_ {j}.
$$

However, there is an additional constraint that the $\phi _ { j } \mathrm { { } ^ { \prime } s }$ sum to 1, since they represent the probabilities $\phi _ { j }   =   p ( z ^ { ( i ) }   =   j ; \phi )$ . To deal with the constraint

<!-- page: 163 -->

that $\textstyle \sum _ { j = 1 } ^ { k } \phi _ { j } = 1$ , we construct the Lagrangian

$$
\mathcal {L} (\phi) = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} w _ {j} ^ {(i)} \log \phi_ {j} + \beta (\sum_ {j = 1} ^ {k} \phi_ {j} - 1),
$$

where $\beta$ is the Lagrange multiplier.<sup>7</sup> Taking derivatives, we find

$$
\frac {\partial}{\partial \phi_ {j}} \mathcal {L} (\phi) = \sum_ {i = 1} ^ {n} \frac {w _ {j} ^ {(i)}}{\phi_ {j}} + \beta
$$

Setting this to zero and solving, we get

$$
\phi_ {j} = \frac {\sum_ {i = 1} ^ {n} w _ {j} ^ {(i)}}{- \beta}
$$

$\mathrm { I . e . , ~ } \phi _ { j }   \propto   \textstyle \sum _ { i = 1 } ^ { n } w _ { j } ^ { ( i ) }$ Using the constraint that $\textstyle \sum _ { j } \phi _ { j }   =   1$ , we easily find that $\begin{array} { r } { - \beta   =   \sum _ { i = 1 } ^ { n } \sum _ { j = 1 } ^ { k } w _ { j } ^ { ( i ) }   =   \sum _ { i = 1 } ^ { n } 1   =   n } \end{array}$ . (This used the fact that $w _ { j } ^ { ( i ) } =$ $Q _ { i } ( z ^ { ( i ) } = j )$ , and since probabilities sum to $\textstyle 1 ,   \sum _ { j } w _ { j } ^ { ( i ) }   =   1 . )$ We therefore have our M-step updates for the parameters $\phi _ { j } ;$

$$
\phi_ {j} := \frac {1}{n} \sum_ {i = 1} ^ {n} w _ {j} ^ {(i)}.
$$

The derivation for the M-step updates to $\Sigma _ { j }$ are also entirely straightforward.

## 11.5 Variational inference and variational auto-encoder

Loosely speaking, variational auto-encoder Kingma and Welling [2013] gen erally refers to a family of algorithms that extend the EM algorithms to more complex models parameterized by neural networks. It extends the technique of variational inference with the additional “re-parametrization trick” which will be introduced below. Variational auto-encoder may not give the best performance for many datasets, but it contains several central ideas about how to extend EM algorithms to high-dimensional continuous latent variables

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">φj ≥ ,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>7</sup>We don’t need to worry about the constraint that 0 because as we’ll shortly see, the solution we’ll find from this derivation will automatically satisfy that anyway.</span></small>

<!-- page: 164 -->

with non-linear models. Understanding it will likely give you the language and backgrounds to understand various recent papers related to it.

As a running example, we will consider the following parameterization of $p ( x , z ; \theta )$ by a neural network. Let θ be the collection of the weights of a neural network $g ( z ; \theta )$ that maps $z \in \mathbb { R } ^ { k }$ to $\mathbb { R } ^ { d }$ . Let

$$
z \sim \mathcal {N} (0, I _ {k \times k})\tag{11.18}
$$

$$
x | z \sim \mathcal {N} (g (z; \theta), \sigma^ {2} I _ {d \times d})\tag{11.19}
$$

Here $I _ { k \times k }$ denotes identity matrix of dimension $k$ by $k ,$ and $\sigma$ is a scalar that we assume to be known for simplicity.

For the Gaussian mixture models in Section 11.4, the optimal choice of $Q ( z ) \; = \; p ( z | x ; \theta )$ for each fixed $\theta ,$ that is the posterior distribution of $z ,$ can be analytically computed. In many more complex models such as the model (11.19), it’s intractable to compute the exact posterior distribution $p ( z | x ; \theta )$

Recall that from equation (11.10), ELBO is always a lower bound for any choice of $Q ,$ and therefore, we can also aim for finding an approximation of the true posterior distribution. Often, one has to use some particular form to approximate the true posterior distribution. Let $\mathcal { Q }$ be a family of $Q ^ { \prime } \mathrm { s }$ that we are considering, and we will aim to find a $Q$ within the family of $\mathcal { Q }$ that is closest to the true posterior distribution. To formalize, recall the definition of the ELBO lower bound as a function of $Q$ and $\theta$ defined in equation (11.14)

$$
\mathrm{ELBO} (Q, \theta) = \sum_ {i = 1} ^ {n} \mathrm{ELBO} (x ^ {(i)}; Q _ {i}, \theta) = \sum_ {i} \sum_ {z ^ {(i)}} Q _ {i} (z ^ {(i)}) \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})}
$$

Recall that EM can be viewed as alternating maximization of ELBO(Q, θ). Here instead, we optimize the ELBO over $Q \in { \mathcal { Q } }$

$$
\max _ {Q \in \mathcal {Q}} \max _ {\theta} \operatorname{ELBO} (Q, \theta)\tag{11.20}
$$

Now the next question is what form of $Q$ (or what structural assumptions to make about $Q )$ allows us to efficiently maximize the objective above. When the latent variable z are high-dimensional discrete variables, one popular assumption is the mean field assumption, which assumes that $Q _ { i } ( z )$ gives a distribution with independent coordinates, or in other words, $Q _ { i }$ can be decomposed into $Q _ { i } ( z ) = Q _ { i } ^ { 1 } ( z _ { 1 } ) \cdots Q _ { i } ^ { k } ( z _ { k } )$ . There are tremendous applications of mean field assumptions to learning generative models with discrete latent variables, and we refer to Blei et al. [2017] for a survey of these models and

<!-- page: 165 -->

their impact to a wide range of applications including computational biology, computational neuroscience, social sciences. We will not get into the details about the discrete latent variable cases, and our main focus is to deal with continuous latent variables, which requires not only mean field assumptions, but additional techniques.

When $z \in \mathbb { R } ^ { k }$ is a continuous latent variable, there are several decisions to make towards successfully optimizing (11.20). First we need to give a succinct representation of the distribution $Q _ { i }$ because it is over an infinite number of points. A natural choice is to assume $Q _ { i }$ is a Gaussian distribution with some mean and variance. We would also like to have more succinct representation of the means of $Q _ { i }$ of all the examples. Note that $Q _ { i } ( z ^ { ( i ) } )$ is supposed to approximate $p ( z ^ { ( i ) } | x ^ { ( i ) } ; \theta )$ . It would make sense to let all the means of the $Q _ { i } { } ^ { \prime } \mathrm { s }$ be some function of $x ^ { ( i ) }$ . Concretely, let $q ( \cdot ; \phi ) , v ( \cdot ; \psi )$ be two functions that map from dimension d to $k ,$ which are parameterized by $\phi$ and $\psi$ , we assume that

$$
Q _ {i} = \mathcal {N} (q (x ^ {(i)}; \phi), \mathrm{diag} (v (x ^ {(i)}; \psi)) ^ {2})\tag{11.21}
$$

Here diag(w) means the $k \times k$ matrix with the entries of $w \in \mathbb { R } ^ { k }$ on the diagonal. In other words, the distribution $Q _ { i }$ is assumed to be a Gaussian distribution with independent coordinates, and the mean and standard deviations are governed by $q$ and $v   .$ Often in variational auto-encoders, $q$ and v are chosen to be neural networks.<sup>8</sup>In recent deep learning literature, often $q , v$ are called encoder (in the sense of encoding the data into latent code), whereas $g ( z ; \theta )$ is often referred to as the decoder.

We remark that $Q _ { i }$ of such form in many cases are very far from a good ap proximation of the true posterior distribution. However, some approximation is necessary for feasible optimization. In fact, the form of $Q _ { i }$ needs to satisfy other requirements (which happened to be satisfied by the form (11.21))

Before optimizing the ELBO, let’s first verify whether we can efficiently evaluate the value of the ELBO for fixed $Q$ of the form (11.21) and $\theta .$ We rewrite the ELBO as a function of $\phi , \psi , \theta$ by

$$
\begin{array}{r l} & {\mathrm{ELBO} (\phi , \psi , \theta) = \sum_ {i = 1} ^ {n} \mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})} \right],} \\ & {\qquad \mathrm{where} Q _ {i} = \mathcal {N} (q (x ^ {(i)}; \phi), \mathrm{diag} (v (x ^ {(i)}; \psi)) ^ {2})} \end{array}\tag{11.22}
$$

Note that to evaluate $Q _ { i } ( z ^ { ( i ) } )$ inside the expectation, we should be able to compute the density of $Q _ { i }$ . To estimate the expectation $\mathrm { E } _ { z ^ { ( i ) } \sim Q _ { i } }$ , we

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">8<sub>q</sub> and v can also share parameters. We sweep this level of details under the rug in this note.</span></small>

<!-- page: 166 -->

should be able to sample from the distribution $Q _ { i }$ so that we can build an empirical estimator with samples. It happens that for a Gaussian distribution $Q _ { i } = \mathcal { N } ( q ( x ^ { ( i ) } ; \phi ) , \mathrm { d i a g } ( v ( x ^ { ( i ) } ; \psi ) ) ^ { 2 } )$ , we are able to do both efficiently.

Now let’s optimize the ELBO. It turns out that we can run gradient ascent over $\phi , \psi , \theta$ instead of alternating maximization. There is no strong need to compute the maximum over each variable at a much greater cost. (For Gaussian mixture model in Section 11.4, computing the maximum is analytically feasible and relatively cheap, and therefore we did alternating maximization.) Mathematically, let $\eta$ be the learning rate, the gradient ascent step is

$$
\begin{array}{l} \theta := \theta + \eta \nabla_ {\theta} \mathrm{ELBO} (\phi , \psi , \theta) \\ \phi := \phi + \eta \nabla_ {\phi} \mathrm{ELBO} (\phi , \psi , \theta) \\ \psi := \psi + \eta \nabla_ {\psi} \mathrm{ELBO} (\phi , \psi , \theta) \end{array}
$$

Computing the gradient over θ is simple because

$$
\begin{array}{l} \nabla_ {\theta} \mathrm{ELBO} (\phi , \psi , \theta) = \nabla_ {\theta} \sum_ {i = 1} ^ {n} \mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})} \right] \\ \qquad = \nabla_ {\theta} \sum_ {i = 1} ^ {n} \mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \log p (x ^ {(i)}, z ^ {(i)}; \theta) \right] \\ \qquad = \sum_ {i = 1} ^ {n} \mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \nabla_ {\theta} \log p (x ^ {(i)}, z ^ {(i)}; \theta) \right], \end{array}\tag{11.23}
$$

But computing the gradient over $\phi$ and $\psi$ is tricky because the sampling distribution $Q _ { i }$ depends on $\phi$ and $\psi .$ (Abstractly speaking, the issue we face can be simplified as the problem of computing the gradient $\mathrm { E } _ { z \sim Q _ { \phi } } [ f ( \phi ) ]$ with respect to variable $\phi .$ We know that in general, $\nabla \mathrm { E } _ { z \sim Q _ { \phi } } [ \widetilde { f } ( \phi ) ] \neq \mathrm { E } _ { z \sim Q _ { \phi } } [ \nabla f ( \phi ) ]$ because the dependency of $Q _ { \phi }$ on $\phi$ has to be taken into account as well. )

The idea that comes to rescue is the so-called re-parameterization trick: we rewrite $\boldsymbol { z } ^ { ( i ) } \sim Q _ { i } = \mathcal { N } ( \boldsymbol { q } ( \boldsymbol { x } ^ { ( i ) } ; \boldsymbol { \phi } ) , \mathrm { d i a g } ( \boldsymbol { v } ( \boldsymbol { x } ^ { ( i ) } ; \boldsymbol { \psi } ) ) ^ { 2 } )$ in an equivalent way:

$$
z ^ {(i)} = q (x ^ {(i)}; \phi) + v (x ^ {(i)}; \psi) \odot \xi^ {(i)} \text {where} \xi^ {(i)} \sim \mathcal {N} (0, I _ {k \times k})\tag{11.24}
$$

Here $x \odot y$ denotes the entry-wise product of two vectors of the same dimension. Here we used the fact that $x   \sim   N ( \mu , \sigma ^ { 2 } )$ is equivalent to that $x = \mu { + } \xi \sigma$ with $\xi \sim N ( 0 , 1 )$ . We mostly just used this fact in every dimension simultaneously for the random variable $z ^ { ( i ) } \sim Q _ { i }$

<!-- page: 167 -->

With this re-parameterization, we have that

$$
\begin{array}{r l} & {\mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})} \right]} \\ & {= \mathrm{E} _ {\xi^ {(i)} \sim \mathcal {N} (0, I _ {k \times k})} \left[ \log \frac {p (x ^ {(i)} , q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)} ; \theta)}{Q _ {i} (q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)})} \right]} \end{array}\tag{11.25}
$$

It follows that

$$
\begin{array}{l} \nabla_ {\phi} \mathrm{E} _ {z ^ {(i)} \sim Q _ {i}} \left[ \log \frac {p (x ^ {(i)} , z ^ {(i)} ; \theta)}{Q _ {i} (z ^ {(i)})} \right] \\ = \nabla_ {\phi} \mathrm{E} _ {\xi^ {(i)} \sim \mathcal {N} (0, I _ {k \times k})} \left[ \log \frac {p (x ^ {(i)} , q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)} ; \theta)}{Q _ {i} (q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)})} \right] \\ = \mathrm{E} _ {\xi^ {(i)} \sim \mathcal {N} (0, I _ {k \times k})} \left[ \nabla_ {\phi} \log \frac {p (x ^ {(i)} , q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)} ; \theta)}{Q _ {i} (q (x ^ {(i)} ; \phi) + v (x ^ {(i)} ; \psi) \odot \xi^ {(i)})} \right] \end{array}
$$

We can now sample multiple copies of $\xi ^ { ( i ) } { } ^ { \mathrm { { , } } } \mathrm { { S } }$ to estimate the expectation in the RHS of the equation above.<sup>9</sup> We can estimate the gradient with respect to ψ similarly, and with these, we can implement the gradient ascent algorithm to optimize the ELBO over φ, ψ, θ.

Not many high-dimensional distributions with analytically computable density functions are known to be re-parameterizable. We refer to Kingma and Welling [2013] for a few other choices that can replace Gaussian distributions.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>9</sup>Empirically people sometimes just use one sample to estimate it for maximum computational efficiency.</span></small>

<!-- page: 168 -->

## Chapter 12

## Principal components analysis

In this set of notes, we will develop a method, Principal Components Analysis (PCA), that tries to identify the subspace in which the data approximately lies. PCA is computationally efficient: it will require only an eigenvector calculation (easily done with the eig function in Matlab).

Suppose we are given a dataset $\{ x ^ { ( i ) } ; i = 1 , \ldots , n \}$ of attributes of n different types of automobiles, such as their maximum speed, turn radius, and so on. Let $\boldsymbol { x } ^ { ( i ) } \in \mathbb { R } ^ { d }$ for each $i ( d \ll n )$ . But unknown to us, two different attributes—some $x _ { i }$ and $x _ { j }$ —respectively give a car’s maximum speed measured in miles per hour, and the maximum speed measured in kilometers per hour. These two attributes are therefore almost linearly dependent, up to only small differences introduced by rounding off to the nearest mph or kph. Thus, the data really lies approximately on an $n - 1$ dimensional subspace. How can we automatically detect, and perhaps remove, this redundancy?

For a less contrived example, consider a dataset resulting from a survey of pilots for radio-controlled helicopters, where $x _ { 1 } ^ { ( i ) }$ is a measure of the piloting skill of pilot $i ,$ and $x _ { 2 } ^ { ( i ) }$ captures how much he/she enjoys flying. Because RC helicopters are very difficult to fly, only the most committed students, ones that truly enjoy flying, become good pilots. So, the two attributes $x _ { 1 }$ and $x _ { 2 }$ are strongly correlated. Indeed, we might posit that the data actually lies along some diagonal axis (the $u _ { 1 }$ direction) capturing the intrinsic piloting “karma” of a person, with only a small amount of noise lying off this axis. (See figure.) How can we automatically compute this $u _ { 1 }$ direction?

<!-- page: 169 -->

![](images/page_168_image_1.jpg)

We will shortly develop the PCA algorithm. But prior to running PCA per se, typically we first preprocess the data by normalizing each feature to have mean 0 and variance 1. We do this by subtracting the mean and dividing by the empirical standard deviation:

$$
x _ {j} ^ {(i)} \leftarrow \frac {x _ {j} ^ {(i)} - \mu_ {j}}{\sigma_ {j}}
$$

where $\begin{array} { r } { \mu _ { j } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } x _ { j } ^ { ( i ) } } \end{array}$ and $\begin{array} { r } { \sigma _ { j } ^ { 2 } = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } ( x _ { j } ^ { ( i ) } - \mu _ { j } ) ^ { 2 } } \end{array}$ are the mean variance of feature j, respectively.

Subtracting $\mu _ { j }$ zeros out the mean and may be omitted for data known to have zero mean (for instance, time series corresponding to speech or other acoustic signals). Dividing by the standard deviation $\sigma _ { j }$ rescales each coordinate to have unit variance, which ensures that different attributes are all treated on the same “scale.” For instance, if $x _ { 1 }$ was cars’ maximum speed in mph (taking values in the high tens or low hundreds) and $x _ { 2 }$ were the number of seats (taking values around 2-4), then this renormalization rescales the different attributes to make them more comparable. This rescaling may be omitted if we had a priori knowledge that the different attributes are all on the same scale. One example of this is if each data point represented a grayscale image, and each $x _ { j } ^ { ( i ) }$ took a value in {0, 1, . . . , 255} corresponding to the intensity value of pixel $j$ in image i.

Now, having normalized our data, how do we compute the “major axis of variation” u—that is, the direction on which the data approximately lies? One way is to pose this problem as finding the unit vector u so that when

<!-- page: 170 -->

the data is projected onto the direction corresponding to $u ,$ the variance of the projected data is maximized. Intuitively, the data starts off with some amount of variance/information in it. We would like to choose a direction u so that if we were to approximate the data as lying in the direction/subspace corresponding to $u ,$ as much as possible of this variance is still retained.

Consider the following dataset, on which we have already carried out the normalization steps:

![](images/page_169_image_3.jpg)

Now, suppose we pick u to correspond to the direction shown in the figure below. The circles denote the projections of the original data onto this line.

<!-- page: 171 -->

![](images/page_170_image_1.jpg)

We see that the projected data still has a fairly large variance, and the points tend to be far from zero. In contrast, suppose we had instead picked the following direction:

![](images/page_170_image_3.jpg)

Here, the projections have a significantly smaller variance, and are much closer to the origin.

We would like to automatically select the direction u corresponding to the first of the two figures shown above. To formalize this, note that given a

<!-- page: 172 -->

unit vector u and a point $x ,$ the length of the projection of x onto u is given by $x ^ { T } u .$ I.e., if $x ^ { ( i ) }$ is a point in our dataset (one of the crosses in the plot), then its projection onto $u$ (the corresponding circle in the figure) is distance $x ^ { T } u$ from the origin. Hence, to maximize the variance of the projections, we would like to choose a unit-length u so as to maximize:

$$
\begin{array}{c} \frac {1}{n} \sum_ {i = 1} ^ {n} (x ^ {(i) ^ {T}} u) ^ {2} = \frac {1}{n} \sum_ {i = 1} ^ {n} u ^ {T} x ^ {(i)} x ^ {(i) ^ {T}} u \\ = u ^ {T} \left(\frac {1}{n} \sum_ {i = 1} ^ {n} x ^ {(i)} x ^ {(i) ^ {T}}\right) u. \end{array}
$$

We can recognize that maximizing this subject to $\| u \| _ { 2 } = 1$ gives the principal eigenvector of $\begin{array} { r } { \Sigma   =   \frac { 1 } { n } \sum _ { i = 1 } ^ { n } { x ^ { ( i ) } { x ^ { ( i ) } } ^ { T } } } \end{array}$ , which is just the empirical covariance matrix of the data (assuming it has zero mean).<sup>1</sup>

To summarize, we have found that if we wish to find a 1-dimensional subspace with which to approximate the data, we should choose u to be the principal eigenvector of Σ. More generally, if we wish to project our data into a k-dimensional subspace $( k < d )$ , we should choose $u _ { 1 } , \ldots , u _ { k }$ to be the top k eigenvectors of Σ. The ${ u _ { i } } ^ { \prime } \mathrm { { s } }$ now form a new, orthogonal basis for the data.<sup>2</sup>

Then, to represent $x ^ { ( i ) }$ in this basis, we need only compute the corresponding vector

$$
y ^ {(i)} = \left[ \begin{array}{c} u _ {1} ^ {T} x ^ {(i)} \\ u _ {2} ^ {T} x ^ {(i)} \\ \vdots \\ u _ {k} ^ {T} x ^ {(i)} \end{array} \right] \in \mathbb {R} ^ {k}.
$$

Thus, whereas $x ^ { ( i ) }   \in   \mathbb { R } ^ { d }$ , the vector $y ^ { ( i ) }$ now gives a lower, k-dimensional, approximation/representation for $x ^ { ( i ) }$ . PCA is therefore also referred to as a dimensionality reduction algorithm. The vectors $u _ { 1 } , \ldots , u _ { k }$ are called the first k principal components of the data.

Remark. Although we have shown it formally only for the case of $k = 1$ using well-known properties of eigenvectors it is straightforward to show that

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">λ,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">T .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Σ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Σ λ ,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ui s</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>If you haven’t seen this before, try using the method of Lagrange multipliers to maximize u Σu subject to that u u = 1 You should be able to show that u = u for some which implies u is an eigenvector of , with eigenvalue λ.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Because Σ is symmetric, the ’ will (or always can be chosen to be) orthogonal to each other.</span></small>

<!-- page: 173 -->

of all possible orthogonal bases $u _ { 1 } , \ldots , u _ { k }$ , the one that we have chosen maximizes $\textstyle \sum _ { i } \| y ^ { ( i ) } \| _ { 2 } ^ { 2 }$ . Thus, our choice of a basis preserves as much variability as possible in the original data.

PCA can also be derived by picking the basis that minimizes the approximation error arising from projecting the data onto the k-dimensional subspace spanned by them. (See more in homework.)

PCA has many applications; we will close our discussion with a few examples. First, compression—representing $x ^ { ( i ) } \mathrm { ^ { \mathrm { , } } s }$ with lower dimension $y ^ { ( i ) } \mathrm { ^ { \prime } s ^ { \prime } }$ —is an obvious application. If we reduce high dimensional data to $k = 2$ or 3 dimensions, then we can also plot the $y ^ { ( i ) } \mathrm { ^ { \prime } s }$ to visualize the data. For instance, if we were to reduce our automobiles data to 2 dimensions, then we can plot it (one point in our plot would correspond to one car type, say) to see what cars are similar to each other and what groups of cars may cluster together.

Another standard application is to preprocess a dataset to reduce its dimension before running a supervised learning algorithm with the $x ^ { ( i ) } \mathrm { ^ { \mathrm { , } } s }$ as inputs. Apart from computational benefits, reducing the data’s dimension can also reduce the complexity of the hypothesis class considered and help avoid overfitting (e.g., linear classifiers over lower dimensional input spaces will have smaller VC dimension).

Lastly, as in our RC pilot example, we can also view PCA as a noise reduction algorithm. In our example it, estimates the intrinsic “piloting karma” from the noisy measures of piloting skill and enjoyment. In class, we also saw the application of this idea to face images, resulting in eigenfaces method. Here, each point $x ^ { ( i ) }   \in   \mathbb { R } ^ { 1 0 0 \times 1 0 0 }$ was a 10000 dimensional vector, with each coordinate corresponding to a pixel intensity value in a 100x100 image of a face. Using PCA, we represent each image $\dot { x ^ { ( i ) } }$ with a much lowerdimensional $y ^ { ( i ) }$ . In doing so, we hope that the principal components we found retain the interesting, systematic variations between faces that capture what a person really looks like, but not the “noise” in the images introduced by minor lighting variations, slightly different imaging conditions, and so on. We then measure distances between faces i and $j$ by working in the reduced dimension, and computing $\| y ^ { ( i ) } - y ^ { ( j ) } \| _ { 2 }$ . This resulted in a surprisingly good face-matching and retrieval algorithm.

<!-- page: 174 -->

# Chapter 13

# Independent components analysis

Our next topic is Independent Components Analysis (ICA). Similar to PCA, this will find a new basis in which to represent our data. However, the goal is very different.

As a motivating example, consider the “cocktail party problem.” Here, d speakers are speaking simultaneously at a party, and any microphone placed in the room records only an overlapping combination of the d speakers’ voices. But lets say we have d different microphones placed in the room, and because each microphone is a different distance from each of the speakers, it records a different combination of the speakers’ voices. Using these microphone recordings, can we separate out the original d speakers’ speech signals?

To formalize this problem, we imagine that there is some data $s   \in   \mathbb { R } ^ { d }$ that is generated via d independent sources. What we observe is

$$
x = A s,
$$

where A is an unknown square matrix called the mixing matrix. Repeated observations gives us a dataset $\{ x ^ { ( i ) } ; i = 1 , \ldots , n \}$ , and our goal is to recover the sources $s ^ { ( i ) }$ that had generated our data $( x ^ { ( i ) } = A s ^ { ( i ) } )$

In our cocktail party problem, $s ^ { ( i ) }$ is an d-dimensional vector, and $s _ { j } ^ { ( i ) }$ is the sound that speaker $j$ was uttering at time i. Also, $x ^ { ( i ) }$ in an d-dimensional vector, and $x _ { j } ^ { ( i ) }$ is the acoustic reading recorded by microphone $j$ at time i.

Let $W   =   ^ { \circ } A ^ { - 1 }$ be the unmixing matrix. Our goal is to find $W$ , so that given our microphone recordings $x ^ { ( i ) }$ , we can recover the sources by computing $s ^ { ( i ) } = W \bar { x ^ { ( i ) } }$ . For notational convenience, we also let $w _ { i } ^ { T }$ denote

<!-- page: 175 -->

the i-th row of $W .$ , so that

$$
W = \left[ \begin{array}{c} - w _ {1} ^ {T} - \\ \vdots \\ - w _ {d} ^ {T} - \end{array} \right].
$$

Thus, $w _ { i } \in \mathbb { R } ^ { d }$ , and the j-th source can be recovered as $s _ { j } ^ { ( i ) } = w _ { j } ^ { T } x ^ { ( i ) }$

## 13.1 ICA ambiguities

To what degree can $W = A ^ { - 1 }$ be recovered? If we have no prior knowledge about the sources and the mixing matrix, it is easy to see that there are some inherent ambiguities in A that are impossible to recover, given only the $x ^ { ( i ) } \mathrm { ^ { \mathrm { , } } s }$

Specifically, let $P$ be any d-by-d permutation matrix. This means that each row and each column of $P$ has exactly one “1.” Here are some examples of permutation matrices:

$$
P = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right]; \quad P = \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right]; \quad P = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right].
$$

If z is a vector, then $P z$ is another vector that contains a permuted version of $z   ^ { \prime } \mathrm { s }$ coordinates. Given only the $x ^ { ( i ) } { } ^ { \flat } \mathrm { S } .$ , there will be no way to distinguish between $W$ and PW. Specifically, the permutation of the original sources is ambiguous, which should be no surprise. Fortunately, this does not matter for most applications.

Further, there is no way to recover the correct scaling of the ${ w _ { i } } ^ { \flat } \mathrm { S }$ . For instance, if A were replaced with 2A, and every $s ^ { ( i ) }$ were replaced with $( 0 . 5 ) s ^ { ( i ) }$ then our observed $x ^ { ( i ) } = 2 A \cdot ( 0 . 5 ) s ^ { ( i ) }$ would still be the same. More broadly, if a single column of A were scaled by a factor of $\alpha ,$ and the corresponding source were scaled by a factor of $1 / \alpha ,$ , then there is again no way to determine that this had happened given only the $x ^ { ( i ) } { } ^ { \flat } \mathrm { S } .$ . Thus, we cannot recover the “correct” scaling of the sources. However, for the applications that we are concerned with—including the cocktail party problem—this ambiguity also does not matter. Specifically, scaling a speaker’s speech signal $s _ { j } ^ { ( i ) }$ by some positive factor $\alpha$ affects only the volume of that speaker’s speech. Also, sign changes do not matter, and $s _ { j } ^ { ( i ) }$ and $- s _ { j } ^ { ( i ) }$ sound identical when played on a speaker. Thus, if the $w _ { i }$ found by an algorithm is scaled by any non-zero real number, the corresponding recovered source $s _ { i } = w _ { i } ^ { T } x$ will be scaled by the

<!-- page: 176 -->

same factor; but this usually does not matter. (These comments also apply to ICA for the brain/MEG data that we talked about in class.)

Are these the only sources of ambiguity in ICA? It turns out that they are, so long as the sources $s _ { i }$ are non-Gaussian. To see what the difficulty is with Gaussian data, consider an example in which $n = 2 ,$ and $s \sim \mathcal { N } ( 0 , I )$ Here, I is the $2 \mathrm { x } 2$ identity matrix. Note that the contours of the density of the standard normal distribution $\mathcal { N } ( 0 , I )$ are circles centered on the origin, and the density is rotationally symmetric.

Now, suppose we observe some $x = A s$ , where A is our mixing matrix. Then, the distribution of x will be Gaussian, $x \sim \mathcal { N } ( 0 , A A ^ { T } )$ , since

$$
\mathrm{E} _ {s \sim \mathcal {N} (0, I)} [ x ] = \mathrm{E} [ A s ] = A \mathrm{E} [ s ] = 0
$$

$$
\mathrm{Cov} [ x ] = \mathrm{E} _ {s \sim \mathcal {N} (0, I)} [ x x ^ {T} ] = \mathrm{E} [ A s s ^ {T} A ^ {T} ] = A \mathrm{E} [ s s ^ {T} ] A ^ {T} = A \cdot \mathrm{Cov} [ s ] \cdot A ^ {T} = A A ^ {T}
$$

Now, let R be an arbitrary orthogonal (less formally, a rotation/reflection) matrix, so that $R R ^ { T } = R ^ { T } R = I ,$ and let $A ^ { \prime } = A R$ . Then if the data had been mixed according to $A ^ { \prime }$ instead of $A .$ we would have instead observed $x ^ { \prime }   =   A ^ { \prime } s$ . The distribution of $x ^ { \prime }$ is also Gaussian, $\boldsymbol { x } ^ { \prime } \sim \mathcal { N } ( \boldsymbol { 0 } , \boldsymbol { A } \boldsymbol { A } ^ { T } )$ , since $\operatorname { E } _ { s \sim { \mathcal { N } } ( 0 , I ) } [ x ^ { \prime } ( x ^ { \prime } ) ^ { T } ]   =   \operatorname { E } [ A ^ { \prime } s s ^ { T } ( A ^ { \prime } ) ^ { T } ]   =   \operatorname { E } [ A R s s ^ { T } ( A R ) ^ { T } ]   =   A R \dot { R } ^ { T } A ^ { T }   \stackrel { \cdot } { = }   A A ^ { T }$ Hence, whether the mixing matrix is $A$ or $A ^ { \prime }$ , we would observe data from a $\mathcal { N } ( 0 , A A ^ { T } )$ distribution. Thus, there is no way to tell if the sources were mixed using A and $A ^ { \prime } .$ There is an arbitrary rotational component in the mixing matrix that cannot be determined from the data, and we cannot recover the original sources.

Our argument above was based on the fact that the multivariate standard normal distribution is rotationally symmetric. Despite the bleak picture that this paints for ICA on Gaussian data, it turns out that, so long as the data is not Gaussian, it is possible, given enough data, to recover the d independent sources.

## 13.2 Densities and linear transformations

Before moving on to derive the ICA algorithm proper, we first digress briefly to talk about the effect of linear transformations on densities.

Suppose a random variable s is drawn according to some density $p _ { s } ( s )$ For simplicity, assume for now that $s   \in   \mathbb { R }$ is a real number. Now, let the random variable x be defined according to $x = A s$ (here, $x \in \mathbb { R } , A \in \mathbb { R } )$ . Let $p _ { x }$ be the density of $x .$ . What is $p _ { x } ?$

Let $W   =   A ^ { - 1 }$ . To calculate the “probability” of a particular value of $x ,$ it is tempting to compute $s = W x$ , then evaluate $p _ { s }$ at that point, and

<!-- page: 177 -->

conclude that ${ \mathrm { ` } } p _ { x } ( x )   =   p _ { s } ( W x ) .$ However, this is incorrect. For example, let $s \sim \mathrm { U n i f o r m } [ 0 , 1 ]$ , so $p _ { s } ( s ) = 1 \{ 0 \leq s \leq 1 \}$ . Now, let $A = 2,    so   x = 2s$ Clearly, x is distributed uniformly in the interval $[ 0 , 2 ]$ . Thus, its density is given by $p _ { x } ( x )   =   ( 0 . 5 ) 1 \{ 0   \leq   x   \leq   2 \}$ . This does not equal $p _ { s } ( W x )$ , where $W = 0 . 5 = A ^ { - 1 }$ . Instead, the correct formula is $p _ { x } ( x ) = p _ { s } ( W x ) | W |$

More generally, if s is a vector-valued distribution with density $p _ { s }$ , and $x = A s$ for a square, invertible matrix A, then the density of x is given by

$$
p _ {x} (x) = p _ {s} (W x) \cdot | W |,
$$

where $W = A ^ { - 1 }$

Remark. If you’re seen the result that A maps $[ 0 , 1 ] ^ { d }$ to a set of volume $| A |$ then here’s another way to remember the formula for $p _ { x }$ given above, that also generalizes our previous 1-dimensional example. Specifically, let $A \in \mathbb { R } ^ { d \times d }$ be given, and let $W = A ^ { - 1 }$ as usual. Also let $C _ { 1 } = [ 0 , 1 ] ^ { d }$ be the d-dimensional hypercube, and define $C _ { 2 }   =   \{ A s   :   s   \in   C _ { 1 } \}   \subseteq   \mathbb { R } ^ { d }$ to be the image of $C _ { 1 }$ under the mapping given by A. Then it is a standard result in linear algebra (and, indeed, one of the ways of defining determinants) that the volume of $C _ { 2 }$ is given by $| A |$ . Now, suppose s is uniformly distributed in $[ 0 , 1 ] ^ { d }$ , so its density is $p _ { s } ( s ) = 1 \{ s \in C _ { 1 } \}$ . Then clearly x will be uniformly distributed in $C _ { 2 }$ . Its density is therefore found to be $p _ { x } ( x ) = 1 \{ x \in C _ { 2 } \} / \mathrm { v o l } ( C _ { 2 } )$ (since it must integrate over $C _ { 2 }$ to 1). But using the fact that the determinant of the inverse of a matrix is just the inverse of the determinant, we have $1 / \mathrm { v o l } ( C _ { 2 } ) = 1 / | A | = | A ^ { - 1 } | = | W |$ . Thus, $p _ { x } ( x ) = 1 \{ x \in C _ { 2 } \} | W | = 1 \{ W x \in$ $C _ { 1 } \} | W | = p _ { s } ( W x ) | W |$

## 13.3 ICA algorithm

We are now ready to derive an ICA algorithm. We describe an algorithm by Bell and Sejnowski, and we give an interpretation of their algorithm as a method for maximum likelihood estimation. (This is different from their original interpretation involving a complicated idea called the infomax principal which is no longer necessary given the modern understanding of ICA.)

We suppose that the distribution of each source $s _ { j }$ is given by a density $p _ { s }$ , and that the joint distribution of the sources s is given by

$$
p (s) = \prod_ {j = 1} ^ {d} p _ {s} (s _ {j}).
$$

<!-- page: 178 -->

Note that by modeling the joint distribution as a product of marginals, we capture the assumption that the sources are independent. Using our formulas from the previous section, this implies the following density on $x   =   A s   =$ $W ^ { - 1 } s ;$

$$
p (x) = \prod_ {j = 1} ^ {d} p _ {s} (w _ {j} ^ {T} x) \cdot | W |.
$$

All that remains is to specify a density for the individual sources $p _ { s }$

Recall that, given a real-valued random variable $之 ,$ its cumulative distribution function (cdf) F is defined by $\begin{array} { r } { F ( z _ { 0 } ) = P ( z \leq z _ { 0 } ) = \int _ { - \infty } ^ { z _ { 0 } } p _ { z } ( z ) d z } \end{array}$ and the density is the derivative of the cdf: $p _ { z } ( z ) = F ^ { \prime } ( z )$

Thus, to specify a density for the $s _ { i } \mathrm { ^ { \prime } s }$ , all we need to do is to specify some cdf for it. A cdf has to be a monotonic function that increases from zero to one. Following our previous discussion, we cannot choose the Gaussian cdf, as ICA doesn’t work on Gaussian data. What we’ll choose instead as a reasonable “default” cdf that slowly increases from 0 to 1, is the sigmoid function $g ( s ) = 1 / { \left( 1 + e ^ { - s } \right) }$ . Hence, $p _ { s } ( s ) = g ^ { \prime } ( s )$ <sup>1</sup>

The square matrix W is the parameter in our model. Given a training set $\{ x ^ { ( i ) } ; i = 1 , \ldots , n \}$ , the log likelihood is given by

$$
\ell (W) = \sum_ {i = 1} ^ {n} \left(\sum_ {j = 1} ^ {d} \log g ^ {\prime} (w _ {j} ^ {T} x ^ {(i)}) + \log | W |\right).
$$

We would like to maximize this in terms W. By taking derivatives and using the fact (from the first set of notes) that $\widetilde { \nabla _ { W } | W | } = \widetilde { | W | } ( W ^ { - 1 } ) ^ { T }$ , we easily derive a stochastic gradient ascent learning rule. For a training example $x ^ { ( i ) }$ the update rule is:

$$
W := W + \alpha \left(\left[ \begin{array}{c} 1 - 2 g (w _ {1} ^ {T} x ^ {(i)}) \\ 1 - 2 g (w _ {2} ^ {T} x ^ {(i)}) \\ \vdots \\ 1 - 2 g (w _ {d} ^ {T} x ^ {(i)}) \end{array} \right] x ^ {(i) T} + (W ^ {T}) ^ {- 1}\right),
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E E A 0 [x] = [ s] = .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ps(s) = g′(s)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>If you have prior knowledge that the sources’ densities take a certain form, then it is a good idea to substitute that in here. But in the absence of such knowledge, the sigmoid function can be thought of as a reasonable default that seems to work well for many problems. Also, the presentation here assumes that either the data xhas been preprocessed to have zero mean, or that it can naturally be expected to have zero mean (such as acoustic signals). This is necessary because our assumption that ps(s) = g (s) implies [s] = (the derivative of the logistic function is a symmetric function, and hence gives a density corresponding to a random variable with zero mean), which implies</span></small>

<!-- page: 179 -->

where α is the learning rate.

After the algorithm converges, we then compute $s ^ { ( i ) } = W x ^ { ( i ) }$ to recover the original sources.

Remark. When writing down the likelihood of the data, we implicitly assumed that the $x ^ { ( i ) } \mathrm { ^ { \prime } s }$ were independent of each other (for different values of $i ;$ note this issue is different from whether the different coordinates of $x ^ { ( i ) }$ are independent), so that the likelihood of the training set was given by $\textstyle \prod _ { i } p ( x ^ { ( i ) } ; W )$ . This assumption is clearly incorrect for speech data and other time series where the $x ^ { ( i ) } \mathrm { ^ { \mathrm { , } } s }$ are dependent, but it can be shown that having correlated training examples will not hurt the performance of the algorithm if we have sufficient data. However, for problems where successive training examples are correlated, when implementing stochastic gradient ascent, it sometimes helps accelerate convergence if we visit training examples in a randomly permuted order. (I.e., run stochastic gradient ascent on a randomly shuffled copy of the training set.)

<!-- page: 180 -->

Part V

Generative models and Foundation Models

<!-- page: 181 -->

## Chapter 14

## Diffusion models

Generative modeling asks us to model the distribution of the data itself. Unlike supervised learning, where the goal is to predict a target y from an input x, the goal here is to generate new plausible samples x. We will use images as the main running example.

A diffusion model does this by first defining a simple process that gradually adds noise to data, and then learning to reverse that process one step at a time. The basic idea goes back to nonequilibrium thermodynamics based models [Sohl-Dickstein et al., 2015]; its modern form was developed in de noising diffusion probabilistic models (DDPMs) [Ho et al., 2020], with later connections to score-based modeling [Song et al., 2021]. Beyond images, diffusion models are also prominent in video generation and in vision-language action (VLA) models for robotics, and there are early promising results for applying diffusion-style methods to language.

## 14.1 The diffusion process

Let $p _ { \mathrm { d a t a } }$ be the distribution of the data, such as images or normalized images, which we eventually aim to be able to generate samples from.

The forward diffusion process defines a fixed Markov chain that gradually corrupts the clean data from $p _ { \mathrm { d a t a } }$ . This Markov chain consists of a sequence of random variables $x _ { 0 } , x _ { 1 } , \ldots , x _ { T }$ , where $x _ { 0 } \sim p _ { \mathrm { d a t a } }$ . The variables $x _ { 1 } , x _ { 2 } , \ldots , x _ { T }$ are progressively noisier versions of $x _ { 0 }$ . Let $q$ denote the joint distribution of this Markov chain. Its one-step transition density is

$$
q (x _ {t} \mid x _ {t - 1}) = \mathcal {N} \Big (x _ {t}; \sqrt {1 - \beta_ {t}}   x _ {t - 1}, \beta_ {t} I \Big)  .\tag{14.1}
$$

<!-- page: 182 -->

![](images/page_181_image_1.jpg)

Figure 14.1: The forward diffusion process gradually corrupts a clean sample, while the learned reverse process denoises one step at a time.

Here $\beta _ { 1 } , \ldots , \beta _ { T } \in ( 0 , 1 )$ are scalars that indicate the noise level at each step.<sup>1</sup>

Probability notation clarification. As throughout these lecture notes, $\mathcal { N } ( \mu , \Sigma )$ denotes the Gaussian distribution with mean $\mu$ and covariance $\Sigma .$ Here we use $\mathcal { N } ( x ; \mu , \Sigma )$ to denote the corresponding Gaussian density evaluated at x: $\mathcal { N } ( x ; \mu , \Sigma ) = \frac { 1 } { ( 2 \pi ) ^ { d / 2 } | \Sigma | ^ { 1 / 2 } } \exp \left( - \frac { 1 } { 2 } ( x - \mu ) ^ { T } \Sigma ^ { - 1 } ( x - \mu ) \right)$ . In machine learning, simplified and overloaded notation is quite common. For example, $x _ { t }$ can denote either the random variable itself or a particular numerical value taken by that random variable. Thus, the notation $x _ { t } \mid x _ { t - 1 }$ denotes a conditional distribution where $x _ { t } , x _ { t - 1 }$ are interpreted as random variables, while $q ( x _ { t } \mid x _ { t - 1 } )$ denotes the conditional density evaluated at the particular values written as $x _ { t }$ and $x _ { t - 1 }$ . We will use this standard overloaded notation as well. Equation (14.1) therefore means that, under $q ,$ the conditional random variable $x _ { t }$ given $x _ { t - 1 }$ is Gaussian with mean $\sqrt { 1 - \beta _ { t } }   x _ { t - 1 }$ and covariance $\beta _ { t } I ,$ even though the equation itself is written as an equality between density functions.<sup>2</sup> We may also write the following, which more explicitly emphasizes that we are defining the distribution of $x _ { t } \mid x _ { t - 1 }$ under the transition $q ,$ denoted by $\operatorname { L a w } _ { q } ( x _ { t }   |   x _ { t - 1 } )$

$$
\mathrm{Law} _ {q} (x _ {t} \mid x _ {t - 1}) = \mathcal {N} \Big (\sqrt {1 - \beta_ {t}}   x _ {t - 1},   \beta_ {t} I \Big).\tag{14.2}
$$

We will learn a model that runs this noising process backward. Before that, we will understand some properties of the forward process. It is convenient to also define $\alpha _ { t } = 1 - \beta _ { t }$ . Then a sample from the forward process

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">βt,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2t .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(√ − βt xt−1, βt )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Following the conventional notation in the diffusion-model literature, we write the variance as  rather than as β</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">q(xt | xt−1) =</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2In machine learning, one also often sees the more overloaded notation N 1 I , where a density on the left is identified with a distribution on the right. We will avoid that usage in these notes.</span></small>

<!-- page: 183 -->

can be written as

xt =√αt xt−1 +pβt t, 1, . . . , T are independent with $\epsilon _ { t } \sim \mathcal { N } ( 0 , I )$

(14.3)

At each step, the previous noisy variable $x _ { t - 1 }$ is slightly shrunk by the factor $\sqrt { \alpha _ { t } }$ , and then fresh Gaussian noise is added. In practice, $\beta _ { t }$ is chosen to be small, for example on the order of $1 0 ^ { - 4 }$ to $1 0 ^ { - 2 }$ , so $\alpha _ { t }$ is close to one and each step perturbs the data only a little. But after many steps, the original structure is gradually washed away.

We can also see how the covariance evolves. Since the added noise is independent of $x _ { t } .$ <sub>−1</sub>,

$$
\mathrm{Cov} (x _ {t}) = \alpha_ {t} \mathrm{Cov} (x _ {t - 1}) + \beta_ {t} I.\tag{14.4}
$$

Since $\alpha _ { t } + \beta _ { t } = 1$ $\operatorname { C o v } ( x _ { t } )$ is a linear interpolation between $\mathrm { C o v } ( x _ { t - 1 } )$ and I. Thus, assuming $x _ { 0 }$ is normalized in every dimension, each step nudges the distribution toward a spherical Gaussian while preserving its scale.

Because each step only adds Gaussian noise, the cumulative noise is also Gaussian, that is, the conditional distribution of $x _ { t }$ given $x _ { 0 }$ is also Gaussian for any t. Concretely, letting $\begin{array} { r } { \bar { \alpha } _ { t } = \prod _ { s = 1 } ^ { t } \alpha _ { s } } \end{array}$ , we have

$$
x _ {t} = \sqrt {\bar {\alpha} _ {t}} x _ {0} + \sqrt {1 - \bar {\alpha} _ {t}} \hat {\epsilon} _ {t}, \quad \hat {\epsilon} _ {t} \sim \mathcal {N} (0, I).\tag{14.5}
$$

Proof of Equation (14.5). Unrolling the recursion gives

$$
x _ {t} = \sqrt {\alpha_ {t}} x _ {t - 1} + \sqrt {1 - \alpha_ {t}} \epsilon_ {t}\tag{14.6}
$$

$$
= \sqrt {\alpha_ {t} \alpha_ {t - 1}} x _ {t - 2} + \sqrt {\alpha_ {t} (1 - \alpha_ {t - 1})} \epsilon_ {t - 1} + \sqrt {1 - \alpha_ {t}} \epsilon_ {t}\tag{14.7}
$$

$$
= \sqrt {\alpha_ {t} \alpha_ {t - 1} \alpha_ {t - 2}} x _ {t - 3} + \sqrt {\alpha_ {t} \alpha_ {t - 1} (1 - \alpha_ {t - 2}) \epsilon_ {t - 2}}
$$

$$
+ \sqrt {\alpha_ {t} (1 - \alpha_ {t - 1})} \epsilon_ {t - 1} + \sqrt {1 - \alpha_ {t}} \epsilon_ {t}\tag{14.8}
$$

$$
= \sqrt {\bar {\alpha} _ {t}} x _ {0} + \sum_ {s = 1} ^ {t} \sqrt {\left(1 - \alpha_ {s}\right) \prod_ {r = s + 1} ^ {t} \alpha_ {r} \epsilon_ {s}}.\tag{14.9}
$$

The second term in Equation (14.9) is a linear combination of independent Gaussians, and is therefore Gaussian. Its covariance has to be $( 1   -   \bar { \alpha } _ { t } ) I$ indeed, if $x _ { 0 }$ has identity covariance, then the covariance recursion in Equation (14.4) gives $\mathrm { C o v } ( x _ { t } ) = I$ , while the clean-data term $\sqrt { \bar { \alpha } _ { t } }   x _ { 0 }$ contributes covariance $\bar { \alpha } _ { t } I$ . The same conclusion can also be checked by telescoping the covariance sum. Therefore the whole noise term has the same distribution as $\sqrt { 1 - \bar { \alpha } _ { t } }   \hat { \epsilon } _ { t }$ with $\hat { \epsilon } _ { t } \sim \mathcal { N } ( 0 , I )$ , giving (14.5). □

<!-- page: 184 -->

Equation (14.5) shows that $\bar { \alpha } _ { t }$ controls the clean-data component: as $\bar { \alpha } _ { t }$ decreases, $x _ { t }$ contains less information about $x _ { 0 }$ and more Gaussian noise. In the limiting regime where $T \to \infty$ and $\bar { \alpha } _ { T } \rightarrow 0$ , for every $x _ { 0 }$

$$
\begin{array}{c} q (x _ {T} \mid x _ {0}) \to \mathcal {N} (x _ {T}; 0, I), \\ \operatorname{Law} _ {q} (x _ {T} \mid x _ {0}) \to \mathcal {N} (0, I). \end{array}
$$

or in other words,

(14.10)

Thus, $x _ { T }$ eventually converges to white Gaussian noise. Averaging over $x _ { 0 }$ this also means that the marginal distribution of $x _ { T }$ under $q$ is close to $\mathcal { N } ( 0 , I )$ for large $T .$ We will assume that $q ( x _ { T } )$ is exactly spherical Gaussian in the rest of the chapter.

We note that the forward process $q$ is fixed rather than learned. This is one of the attractive features of diffusion models. The learning problem is not to discover how to corrupt the data, but only how to reverse a corruption process that we chose ourselves.

## 14.2 Parameterizing the reverse process

The previous section defined a fixed forward process. We now ask what it would mean to reverse it, and then replace the unknown reverse conditionals by a learned parameterized model. Because the forward process is Markov, the same joint distribution can also be factorized in the reverse direction in a Markov fashion. More precisely, under the distribution ${ q _ { \mathrm { { } ^ { 3 } } } ^ { 3 } }$

$$
q (x _ {0: T}) = q (x _ {T}) \prod_ {t = 1} ^ {T} q (x _ {t - 1} \mid x _ {t}),\tag{14.11}
$$

where the conditionals $q ( x _ { t - 1 } \mid x _ { t } )$ define the true reverse Markov chain. The previous section argued that the marginal distribution of $x _ { T }$ under $q$ is the standard spherical Gaussian $\mathcal { N } ( 0 , I )$

We will learn to approximate the unknown reverse conditionals $q ( x _ { t - 1 } \mid$ $x _ { t } )$ , so that we can generate from $p _ { \mathrm { d a t a } }$ by sampling $x _ { T } \sim \mathcal { N } ( 0 , I )$ and repeatedly sampling backward, xT $\cdot \to x _ { T - 1 } \to \cdots \to x _ { 1 } \to x _ { 0 }$

We approximate each reverse kernel $q ( x _ { t - 1 } \mid x _ { t } )$ by a Gaussian distribution with parameters produced by a neural network. Concretely, we define

$$
\begin{array}{r l r} & & {p _ {\theta} (x _ {t - 1} \mid x _ {t}) = \mathcal {N} \big (x _ {t - 1}; \mu_ {\theta} (x _ {t}, t), \sigma_ {t} ^ {2} I \big) ,} \\ & & {\mathrm{i.e.,} \quad \mathrm{Law} _ {p _ {\theta}} (x _ {t - 1} \mid x _ {t}) = \mathcal {N} \big (\mu_ {\theta} (x _ {t}, t), \sigma_ {t} ^ {2} I \big).} \end{array}\tag{14.12}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1:T</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x0:T</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(x1, . . . , xT ).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(x0, x1, . . . , xT ).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>We use the shorthand to denote the whole trajectory  Similarly, x denotes</span></small>

<!-- page: 185 -->

Together with the prior density $p _ { \theta } ( x _ { T } ) \quad = \quad \mathcal { N } ( x _ { T } ; 0 , I )$ , or equivalently $\mathrm { L a w } _ { p _ { \theta } } ( x _ { T } ) = \mathcal { N } ( 0 , I )$ , these conditionals define a full joint distribution over the trajectory.

$$
p _ {\theta} (x _ {0: T}) = p _ {\theta} (x _ {T}) \prod_ {t = 1} ^ {T} p _ {\theta} (x _ {t - 1} \mid x _ {t}).\tag{14.13}
$$

The mean $\mu _ { \theta } ( x _ { t } , t )$ is produced by a neural network with parameters $\theta ;$ the timestep t is embedded and fed into the network along with $x _ { t }$ . The scalar variance $\sigma _ { t } ^ { 2 }$ is fixed and will be determined later in this note, but it can also be learned [Nichol and Dhariwal, 2021].

This Gaussian reverse parametrization is not only a convenient modeling choice; it is also supported by the continuous-time reverse diffusion theorem. We return to this perspective in Section 14.4.

## 14.3 Training diffusion models by maximizing the ELBO

We now fit the parameterized reverse process by maximizing the likelihood using the standard variational approach. The goal is to maximize the likelihood $p _ { \theta } ( x _ { 0 } )$ over the parameter $\theta { \cdot } ^ { 4 }$

$$
p _ {\theta} (x _ {0}) = \int p _ {\theta} (x _ {0: T}) d x _ {1} \dots d x _ {T}\tag{14.14}
$$

Since the integration is intractable, we maximize the variational lower bound of $p _ { \theta } ( x _ { 0 } )$ . Using the standard ELBO identity, namely the definition in (11.9) together with the lower-bound statement in (11.10), with the latent variable z corresponding to the path $x _ { 1 : T }$ and the auxiliary distribution $Q ( z )$ corresponding to $q ( x _ { 1 : T } \mid x _ { 0 } )$ , we have

$$
\begin{array}{l} \log p _ {\theta} (x _ {0}) \geq \mathcal {L} _ {\mathrm{ELBO}} (x _ {0}; q) = \operatorname{E} _ {x _ {1: T} \sim \operatorname{Law} _ {q} (x _ {1: T} \mid x _ {0})} \left[ \log \frac {p _ {\theta} (x _ {0 : T})}{q (x _ {1 : T} \mid x _ {0})} \right] \\ \qquad = \operatorname{E} _ {x _ {1: T} \sim \operatorname{Law} _ {q} (x _ {1: T} \mid x _ {0})} \big [ \log p _ {\theta} (x _ {0} \mid x _ {1: T}) \big ] \\ \qquad - \operatorname{KL} \big (\operatorname{Law} _ {q} (x _ {1: T} \mid x _ {0}) \| \operatorname{Law} _ {p _ {\theta}} (x _ {1: T}) \big). \end{array}\tag{14.15}
$$

Because the reverse model is Markov, $p _ { \theta } ( x _ { 0 } | x _ { 1 : T } ) = p _ { \theta } ( x _ { 0 } | x _ { 1 } )$ . Thus the first term is the final reconstruction term. The second KL term can

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(i)’</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x . 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4More precisely, the goal is to maxθ $\textstyle \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \operatorname { l o g } p _ { \theta } ( x _ { 0 } ^ { ( i ) } )$ , where the x s are empirical examples. But here for simplicity we consider the case where there is just a single example</span></small>

<!-- page: 186 -->

be decomposed by the chain rule for KL, Lemma A.1.4, using the reverse factorizations of $p _ { \theta }$ and $q ;$

$$
\begin{array}{l} \mathrm{KL} \big (q (x _ {1: T} \mid x _ {0}) \| p _ {\theta} (x _ {1: T}) \big) \\ \quad = \underbrace {\mathrm{KL} \big (q (x _ {T} \mid x _ {0}) \| p _ {\theta} (x _ {T}) \big)} _ {\triangleq L _ {T}} + \sum_ {t = 2} ^ {T} \underbrace {\mathrm{E} _ {q} \big [ \mathrm{KL} \big (q (x _ {t - 1} \mid x _ {t} , x _ {0}) \| p _ {\theta} (x _ {t - 1} \mid x _ {t}) \big) \big ]} _ {\triangleq L _ {t - 1}}. \end{array}\tag{14.16}
$$

The term $L _ { T }   =   \mathrm { K L } ( q ( x _ { T }   \mid   x _ { 0 } ) \| p _ { \theta } ( x _ { T } ) )$ can be dropped from the training objective because $p _ { \theta } ( x _ { T } ) = \mathcal { N } ( 0 , I )$ is fixed and therefore $L _ { T }$ is independent of the learned reverse transitions. Moreover, under our assumption that the forward noising schedule makes $\bar { \alpha } _ { T }$ very close to zero, we have $q ( x _ { T } \mid x _ { 0 } ) =$ $\mathcal { N } ( \sqrt { \bar { \alpha } _ { T } } x _ { 0 } , ( 1 - \bar { \alpha } _ { T } ) I ) \: \approx \: \mathcal { N } ( 0 , I )$ , so this $L _ { T }$ term is also small. Thus by Equations (14.15) and (14.16), we have that

$$
\log p _ {\theta} (x _ {0}) \geq \mathcal {L} _ {\mathrm{ELBO}} (x _ {0}; q) = - L _ {0} - \sum_ {t = 2} ^ {T} L _ {t - 1} = - \sum_ {t = 0} ^ {T - 1} L _ {t}.\tag{14.17}
$$

The $L _ { 1 } , L _ { 2 } , \cdots , L _ { T - 1 }$ terms are the main denoising terms. At each timestep, they ask the model reverse kernel $p _ { \theta } ( x _ { t - 1 } | x _ { t } )$ to match the true Gaussian posterior $q ( x _ { t - 1 } \; \mid \; x _ { t } , x _ { 0 } )$ The term $L _ { 0 }$ is the negative expected final reconstruction term, which controls how the nearly clean sample $x _ { 1 }$ is turned back into $x _ { 0 }$ . This is the probabilistic bridge between generation and denoising: if every reverse step matches the corresponding true posterior, then chaining those steps together yields a good generative model.

Next we derive the denoising terms $L _ { 1 } , \ldots , L _ { T - 1 }$ as explicit functions of θ so that we have a concrete optimization objective. First, by basic properties of Gaussians, since $x _ { 1 } , \cdots , x _ { T }$ are jointly Gaussian given $x _ { 0 }$ , the true onestep reverse transition is also Gaussian with specific mean and variance. More concretely, we apply the conditional-Gaussian formula in Lemma A.1.2 with $A   =   x _ { t - 1 }$ and $B   =   x _ { t }$ , while treating $x _ { 0 }$ as fixed. This shows that $q ( x _ { t - 1 } | x _ { t } , x _ { 0 } )$ is Gaussian. Applying the algebra to the forward Gaussian chain gives

$$
q (x _ {t - 1} \mid x _ {t}, x _ {0}) = \mathcal {N} \Big (x _ {t - 1}; \tilde {\mu} _ {t} (x _ {t}, x _ {0}), \tilde {\beta} _ {t} I \Big),\tag{14.18}
$$

where

$$
\tilde {\beta} _ {t} = \frac {1 - \bar {\alpha} _ {t - 1}}{1 - \bar {\alpha} _ {t}} \beta_ {t}, \quad \text {and} \quad \tilde {\mu} _ {t} (x _ {t}, x _ {0}) = \frac {\sqrt {\bar {\alpha} _ {t - 1}} \beta_ {t}}{1 - \bar {\alpha} _ {t}} x _ {0} + \frac {\sqrt {\alpha_ {t}} (1 - \bar {\alpha} _ {t - 1})}{1 - \bar {\alpha} _ {t}} x _ {t}.\tag{14.19}
$$

<!-- page: 187 -->

Recall that we assume the reverse transition under $p _ { \theta }$ is also Gaussian, which has a similar form: $p _ { \theta } ( x _ { t - 1 } \: \mid \: x _ { t } ) \: = \: \mathcal { N } ( x _ { t - 1 } ; \mu _ { \theta } ( x _ { t } , t ) , \sigma _ { t } ^ { 2 } I )$ , It is natural to choose $\sigma _ { t } ^ { 2 } = \tilde { \beta } _ { t }$ so that the two distributions in the KL term, $L _ { t - 1 } .$ , have the same covariance.

The KL divergence between two Gaussians with the same covariance has the closed form

$$
\mathrm{KL} \big (\mathcal {N} (m _ {1}, \Sigma) \| \mathcal {N} (m _ {2}, \Sigma) \big) = \frac {1}{2} (m _ {1} - m _ {2}) ^ {T} \Sigma^ {- 1} (m _ {1} - m _ {2}).\tag{14.20}
$$

Therefore, for $\begin{array} { r l r l r } { t } & { { } } & { } & { { } = } & { } & { { } 2 , \ldots , T , } \end{array}$ the term $L_{t - 1} \quad  麵  \quad =$ $\operatorname { E } _ { q } \bigl [ \operatorname { K L } \bigl ( q ( x _ { t - 1 } \mid x _ { t } , x _ { 0 } ) \mathbin \Vert p _ { \theta } ( x _ { t - 1 } \mid x _ { t } ) \bigr ) \bigr ]$ is the same as

$$
L _ {t - 1} = \mathrm{E} _ {q} \left[ \frac {1}{2 \tilde {\beta} _ {t}} \left\| \tilde {\mu} _ {t} (x _ {t}, x _ {0}) - \mu_ {\theta} (x _ {t}, t) \right\| _ {2} ^ {2} \right].\tag{14.21}
$$

In other words, our model $\mu _ { \theta } ( x _ { t } , t )$ is supposed to reconstruct $\tilde { \mu } _ { t } ( x _ { t } , x _ { 0 } )$ which is a linear combination of $x _ { 0 }$ and $x _ { t }$ by Equation (14.19).

Simplifying to Reconstructing the Noise. Because $x _ { t }$ is a linear combination of $x _ { 0 }$ and $\hat { \epsilon } _ { t }$ by Equation (14.5), the posterior mean $\tilde { \mu } _ { t } ( x _ { t } , x _ { 0 } )$ can also be written in terms of $x _ { t }$ and $\hat { \epsilon } _ { t }$ . Thus, to reconstruct $\tilde { \mu } _ { t } ( x _ { t } , x _ { 0 } )$ , we can equivalently reconstruct $\hat { \epsilon } _ { t }$ .

Therefore, we can simplify further. First, by Equation (14.5), we have $\begin{array} { r } { x _ { 0 } = \frac { x _ { t } - \sqrt { 1 - \bar { \alpha } _ { t } }   \hat { \epsilon } _ { t } } { \sqrt { \bar { \alpha } _ { t } } } } \end{array}$ . Substituting this expression into the exact posterior mean (14.19), and using $\bar { \alpha } _ { t } = \alpha _ { t } \bar { \alpha } _ { t - 1 }$ and $\alpha _ { t } = 1 - \beta _ { t }$ , gives that for $t \geq 2$

$$
\tilde {\mu} _ {t} (x _ {t}, x _ {0}) = \frac {1}{\sqrt {\alpha_ {t}}} \left(x _ {t} - \frac {\beta_ {t}}{\sqrt {1 - \bar {\alpha} _ {t}}} \hat {\epsilon} _ {t}\right).\tag{14.22}
$$

We therefore can also predict $\hat { \epsilon } _ { t }$ by a parameterized neural network $\epsilon _ { \theta } ( x _ { t } , t )$ parameterized by $\theta ,$ and then let

$$
\mu_ {\theta} (x _ {t}, t) = \frac {1}{\sqrt {\alpha_ {t}}} \left(x _ {t} - \frac {\beta_ {t}}{\sqrt {1 - \bar {\alpha} _ {t}}} \epsilon_ {\theta} (x _ {t}, t)\right).\tag{14.23}
$$

Combining Equations (14.21) to (14.23), we have for $t \geq 2$

$$
L _ {t - 1} = \frac {\beta_ {t} ^ {2}}{2 \tilde {\beta} _ {t} \alpha_ {t} (1 - \bar {\alpha} _ {t})} \mathrm{E} _ {\hat {\epsilon} _ {t}} \left[ | | \hat {\epsilon} _ {t} - \epsilon_ {\theta} (x _ {t}, t) | | _ {2} ^ {2} \right].\tag{14.24}
$$

The ELBO consists of terms that are weighted noise-prediction losses.

<!-- page: 188 -->

We note that across different timesteps, $\hat { \epsilon } _ { t }$ are not independent. However, for training at a single sampled timestep, only the marginal fact $\hat { \epsilon } _ { t } \sim \mathcal { N } ( 0 , I )$ is needed, and that is why in other materials $\hat { \epsilon } _ { t }$ <sup>is</sup> often simply written as $\epsilon \sim \mathcal { N } ( 0 , I )$ . Moreover, the derivation above only applies to the denoising terms $L _ { t - 1 }$ for $t \geq 2$ because $L _ { 0 }$ has a different definition.

The $L _ { 0 }$ term. In Equation (14.13), we parameterize the reverse process as a Markov process, so $p _ { \theta } ( x _ { 0 } \mid x _ { 1 : T } ) = p _ { \theta } ( x _ { 0 } \mid x _ { 1 } )$ . A natural choice is to model $p _ { \theta } ( x _ { 0 } \vert x _ { 1 } )$ by a Gaussian distribution, $p _ { \theta } ( x _ { 0 }   \mid   x _ { 1 } )   =   \mathcal { N } ( x _ { 0 } ; \mu _ { \theta } ( x _ { 1 } , 1 ) , \sigma _ { 1 } ^ { 2 } I )$ Therefore,

$$
L _ {0} = \frac {1}{2 \sigma_ {1} ^ {2}} \mathrm{E} _ {q} \big [ \| x _ {0} - \mu_ {\theta} (x _ {1}, 1) \| _ {2} ^ {2} \big ] + \frac {d}{2} \log (2 \pi \sigma_ {1} ^ {2}).\tag{14.25}
$$

For $t \; = \; 1$ , we have $\bar { \alpha } _ { 1 } \; = \; \alpha _ { 1 }$ and $x _ { 0 }   =   ( x _ { 1 }   -   \sqrt { 1 - \bar { \alpha } _ { 1 } }   \hat { \epsilon } _ { 1 } ) / \sqrt { \bar { \alpha } _ { 1 } }   =   ( x _ { 1 }   -$ $\sqrt { \beta _ { 1 } } \thinspace \hat { \epsilon } _ { 1 } ) \big / \sqrt { \alpha _ { 1 } }$ . If we define $\tilde { \mu } _ { 1 } ( x _ { 1 } , x _ { 0 } ) = x _ { 0 }$ , then Equation (14.22) also holds at $t = 1$ . Thus we can use the same noise-prediction parametrization as in Equation (14.23), namely $\mu _ { \theta } ( x _ { 1 } , 1 ) = ( x _ { 1 } - \sqrt { \beta _ { 1 } } \thinspace \epsilon _ { \theta } ( x _ { 1 } , 1 ) ) / \sqrt { \alpha _ { 1 } }$ . Combining these expressions gives

$$
L _ {0} = \frac {\beta_ {1}}{2 \sigma_ {1} ^ {2} \alpha_ {1}} \mathrm{E} _ {\hat {\epsilon} _ {1}} \big [ \| \hat {\epsilon} _ {1} - \epsilon_ {\theta} (x _ {1}, 1) \| _ {2} ^ {2} \big ] + \frac {d}{2} \log (2 \pi \sigma_ {1} ^ {2}).\tag{14.26}
$$

The weight has the same formal pattern as Equation (14.24) at $t = 1$ , with the final-step variance $\sigma _ { 1 } ^ { 2 }$ playing the role of the variance term in the denominator. Thus, up to constants independent of $\theta ,$ the $t   =   1$ reconstruction term and the $t \geq 2$ denoising terms have the same weighted noise-prediction form.<sup>5</sup>

In practice, one often drops these coefficients and trains with the unweighted noise-prediction loss.

Training algorithm. The simplified objective leads to a particularly simple training loop:

1. Sample a clean example $x _ { 0 }$ from the dataset.

2. Sample a timestep t (often uniformly from $\{ 1 , \ldots , T \} )$

3. Sample Gaussian noise $\epsilon \sim \mathcal { N } ( 0 , I )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>In practice, image data are actually represented by discrete pixel values, and some truncation and discretization are applied on top of the continuous observation distribution; see Section 3.3 of Ho et al. [2020] for detail.</span></small>

<!-- page: 189 -->

4. Construct the noisy example by

$$
x _ {t} = \sqrt {\bar {\alpha} _ {t}} x _ {0} + \sqrt {1 - \bar {\alpha} _ {t}} \epsilon .\tag{14.27}
$$

5. Ask the network $\epsilon _ { \theta } ( x _ { t } , t )$ to predict the exact noise  that was used, by taking a gradient step on the loss

$$
L _ {t} (\theta) = \| \epsilon - \epsilon_ {\theta} (x _ {t}, t) \| _ {2} ^ {2}.\tag{14.28}
$$

Sampling at the test time. Sampling uses the same learned denoiser in reverse time:

1. Sample $x _ { T } \sim \mathcal { N } ( 0 , I )$

2. For $t = T , T - 1 , \ldots , 1$

(a) Compute $\epsilon _ { \theta } ( x _ { t } , t )$ and form the mean $\mu _ { \theta } ( x _ { t } , t )$ using (14.23).

(b) Sample

$$
x _ {t - 1} = \mu_ {\theta} (x _ {t}, t) + \sigma_ {t} \xi , \quad \xi \sim \mathcal {N} (0, I),\tag{14.29}
$$

for $t > 1$ , and set $\xi = 0$ at the final step.

## 14.4 Continuous-time view of reverse diffusion

The continuous-time view gives another way to understand why Gaussian reverse kernels and score functions naturally appear in diffusion models. Instead of using a discrete Markov chain, we describe the forward noising process by the stochastic differential equation

$$
d X _ {t} = f (X _ {t}, t) d t + g (t) d W _ {t}, \qquad 0 \leq t \leq T,\tag{14.30}
$$

where $W _ { t }$ is a Wiener process, or standard Brownian motion. Informally, $f ( X _ { t } , t )$ dt is the deterministic drift over an infinitesimal time interval, analogous to the conditional mean increment $( \sqrt { \alpha _ { t } }   -   1 ) x _ { t - 1 }$ in the discrete update, while $g ( t ) ^ { 2 }   d t$ is the infinitesimal noise variance, analogous to the role played by $\beta _ { t }$ in the discrete forward transition. The increment $d W _ { t }$ supplies the standard Gaussian randomness.

Let $p _ { t }$ denote the density of $X _ { t }$ . The reverse-time theorem of Anderson [1982] gives the form of the reverse process, and says that it is also a diffusion process. To state it, define the reverse-time process

$$
Y _ {\tau} = X _ {T - \tau}, \qquad 0 \leq \tau \leq T.\tag{14.31}
$$

Thus $\tau$ increases while the original time $T - \tau$ decreases.

<!-- page: 190 -->

Theorem 14.4.1 (Reverse-time diffusion theorem, informal). Under suitable regularity conditions, the reverse-time process $Y _ { \tau } = X _ { T - \tau }$ is again a diffusion process. Its dynamics are

$$
d Y _ {\tau} = \left(- f (Y _ {\tau}, T - \tau) + g (T - \tau) ^ {2} \nabla_ {x} \log p _ {T - \tau} (Y _ {\tau})\right) d \tau + g (T - \tau) d \bar {W} _ {\tau},\tag{14.32}
$$

where $\bar { W } _ { \tau }$ is a Wiener process with respect to the reverse-time filtration.<sup>6</sup>

The signs in Equation (14.32) come from using $\tau$ as the forward variable for the reversed process. The original drift $f$ is traversed backward, giving the term $- f ( Y _ { \tau } , T - \tau )$ . The additional score term $\nabla _ { x }$ log $p _ { T - \tau }$ appears because the reverse transition must also account for which previous states are more likely under the marginal density at time $T - \tau$

A short informal one-dimensional derivation gives the main intuition. Consider the special case

$$
d X _ {t} = f (X _ {t}, t) d t + d W _ {t}.\tag{14.34}
$$

For a small step size $h ,$ the forward transition from time $T - \tau - h$ to time $T - \tau$ is approximately Gaussian:

$$
\mathrm{Law} _ {X} (X _ {T - \tau} \mid X _ {T - \tau - h} = z) \approx \mathcal {N} (z + h f (z, T - \tau), h).\tag{14.35}
$$

Now condition on $Y _ { \tau } = y$ , which is the same event as $X _ { T - \tau } = y$ . By Bayes’ rule, as a density in $z ,$ (so that multiplicative dependencies in $y$ in the denominator of Bayes rule is omitted)

$$
p (Y _ {\tau + h} = z \mid Y _ {\tau} = y) \propto p (X _ {T - \tau} = y \mid X _ {T - \tau - h} = z) p _ {T - \tau - h} (z).\tag{14.36}
$$

The first factor in Equation (14.36) forces the norm of $z - y$ to be of order $\sqrt { h }$ with high probability. We Taylor-expand the log density and drop all the terms smaller than $O ( h )$

$$
\log p _ {T - \tau - h} (z) = \log p _ {T - \tau} (y) + \partial_ {x} \log p _ {T - \tau} (y) (z - y) + O (h).\tag{14.37}
$$

<sup>6</sup>Equivalently, one often keeps the original time variable $t ,$ but integrates it from $T$ down to $0 .$ If $\bar{X}_{t}$ denotes the same reverse process written with this decreasing original-time parameter, then

$$
d \bar {X} _ {t} = \left(f (\bar {X} _ {t}, t) - g (t) ^ {2} \nabla_ {x} \log p _ {t} (\bar {X} _ {t})\right) d t + g (t) d \bar {W} _ {t}, \qquad t: T \to 0.\tag{14.33}
$$

Here dt is interpreted as a negative time increment, and $d \bar { W } _ { t }$ is the Wiener increment in reverse time. Setting $t = T - \tau$ recovers Equation (14.32).

<!-- page: 191 -->

Note that the second term is on the order of $\sqrt { h }$ for most of the $z .$ Letting $u = z - y$ , and noting that u is mostly on the order of $\sqrt { h }$ , we can derive the log of $p ( Y _ { \tau + h } = z \mid Y _ { \tau } = y )$ by Taylor expansion,

(14.38)

$$
\begin{array}{r l} & {\log p (Y _ {\tau + h} = z \mid Y _ {\tau} = y)} \\ & {= - \frac {(y - z - h f (y , T - \tau)) ^ {2}}{2 h} + \log p _ {T - \tau - h} (z) + \mathrm{const}} \\ & {= - \frac {u ^ {2}}{2 h} - f (y, T - \tau) u + \partial_ {x} \log p _ {T - \tau} (y) u + \mathrm{const} + O (h)} \\ & {= - \frac {1}{2 h} \left(u - h \left[ - f (y, T - \tau) + \partial_ {x} \log p _ {T - \tau} (y) \right]\right) ^ {2} + \mathrm{const} + O (h).} \end{array}\tag{14.39}
$$

Here const encapsulate all terms that are only a function of $y .$ In other words, we have

$$
Y _ {\tau + h} \mid Y _ {\tau} = y \approx \mathcal {N} \big (y + h \big [ - f (y, T - \tau) + \partial_ {x} \log p _ {T - \tau} (y) \big ], h \big).\tag{14.40}
$$

This is the small-step form of (14.32) when $g   \equiv   1$ . The general case has infinitesimal variance $g ( T - \tau ) ^ { 2 } h$ and therefore the score contribution becomes $g ( T - \tau ) ^ { 2 } \nabla _ { x } \log p _ { T - \tau } .$ . This explains why the reverse process is again locally Gaussian and why diffusion models parametrize the reverse kernels by Gaussians.

<!-- page: 192 -->

## Chapter 15

## Foundation models overview

Despite their huge success, neural networks trained with supervised learning typically rely on labeled datasets of decent size, which can be costly to collect. Since around 2018, AI and machine learning have been undergoing a paradigm shift with the rise of models such as BERT [Devlin et al., 2019] and GPT-3 [Brown et al., 2020], which are pretrained on broad data at scale and then adapted to a wide range of downstream tasks. These models, called foundation models by Bommasani et al. [2021], often leverage massive unlabeled data so that a large family of downstream tasks can be solved with fewer or even no labeled examples. Moreover, although foundation models are still based on deep learning and neural networks, their scale can lead to new emergent capabilities. These models are typically trained by self-supervised learning methods, where the supervision signals are constructed from parts of the inputs.

The foundation-model paradigm consists of two phases: pretraining, or simply training, and adaptation. We first pretrain a large model on a massive dataset, often unlabeled.<sup>1</sup> Then, we adapt the pretrained model to a downstream task, often with limited or even no labeled data. The intuition is that pretraining on diverse data can teach the model broad structure that transfers to many downstream tasks. We formalize the two phases below.

Pretraining. A pretraining dataset is usually a large-scale unlabeled dataset

$$
\{x ^ {(1)}, \dots , x ^ {(n)} \}.
$$

Depending on the modality, each $x ^ { ( i ) }$ could be an image, a sequence of words, or a mixture of words, images, audio, or video. In the most common setting,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Sometimes, pretraining can involve large-scale labeled datasets as well, such as ImageNet.</span></small>

<!-- page: 193 -->

the pretraining data are unlabeled; sometimes the pretraining data can also have labels.

Let θ be the model parameters, and $\ell _ { \mathrm { p r e } }$ a loss function. The pretraining loss is often written as an average over the pretraining examples:

$$
L _ {\mathrm{pre}} (\theta) = \frac {1}{n} \sum_ {i = 1} ^ {n} \ell_ {\mathrm{pre}} (x ^ {(i)}, \theta).\tag{15.1}
$$

Here $\ell _ { \mathrm { p r e } }$ is a self-supervised loss on a single datapoint $x ^ { ( i ) }$ , because, as we will see in later examples, the “supervision” can be constructed from the datapoint itself. It is also possible that the pretraining loss is not exactly a sum over individual examples. People typically minimize $L _ { \mathrm { p r e } } ( \theta )$ using an optimizer such as SGD or Adam [Kingma and Ba, 2014].

We denote the resulting pretrained model by $\hat { \theta } .$

Adaptation. We can adapt a pretrained model to solve a downstream task. In a typical supervised downstream task, we have a labeled dataset

$$
\{(\boldsymbol {x} _ {\mathrm{task}} ^ {(1)}, \boldsymbol {y} _ {\mathrm{task}} ^ {(1)}), \dots , (\boldsymbol {x} _ {\mathrm{task}} ^ {(n _ {\mathrm{task}})}, \boldsymbol {y} _ {\mathrm{task}} ^ {(n _ {\mathrm{task}})}) \}.
$$

Often $n _ { \mathrm { t a s k } }$ is much smaller than the size of the pretraining dataset. If only a few labeled examples are available, say five to ten examples, the setting is usually called few-shot learning. If there are no labeled examples for the downstream task, the setting is called zero-shot learning; in modern language-model applications, this may mean that the model receives only a natural-language description of the task. The zero-shot setting is the most common setting now, but this chapter will mostly discuss settings with more downstream examples and defer the zero-shot setting to later chapters.

## 15.1 Linear Probe and Finetuning with Representation Learning

Representation learning is a type of pretraining method. A model $\phi _ { \theta }$ , parameterized by θ, maps a raw input x to a vector $\phi _ { \theta } ( x )$ , which is called a feature vector, embedding, or representation. A good representation should capture semantic information about x that is useful across many downstream tasks. After training this model with a pretraining loss, we obtain a pretrained representation function $\phi _ { \hat { \theta } }$

Adaptation then uses the downstream data to decide how to extract the task-specific information from these representations.

<!-- page: 194 -->

![](images/page_193_image_1.jpg)

Figure 15.1: A schematic view of pretraining and adaptation. Pretraining minimizes the generic pretraining loss in (15.1); for self-supervised examples, the single-example loss $\ell _ { \mathrm { p r e } }$ may be constructed from next-token prediction, masked-patch prediction, or another prediction task derived from $x ^ { ( i ) }$ itself. Full finetuning updates the copied weights and head, linear probing freezes the copied weights and trains only the head, LP-FT uses the probe as an initialization before finetuning, and LoRA freezes the copied base weight $W _ { 0 }$ while training a low-rank update.

Linear probing keeps $\phi _ { \hat { \theta } }$ fixed and learns only a simple prediction head on top of the representation $\phi _ { \hat { \theta } } ( x )$ . Concretely, the downstream prediction model has the form $w ^ { \top } \phi _ { \hat { \theta } } ( x )$ , where $w \in \mathbb { R } ^ { m }$ is trained and $\hat { \theta }$ is fixed. We learn w from the downstream labeled dataset. For example, for a regression task, one could solve

$$
\min _ {w \in \mathbb {R} ^ {m}} \frac {1}{n _ {\mathrm{task}}} \sum_ {i = 1} ^ {n _ {\mathrm{task}}} \left(y _ {\mathrm{task}} ^ {(i)} - w ^ {\top} \phi_ {\hat {\theta}} (x _ {\mathrm{task}} ^ {(i)})\right) ^ {2}.\tag{15.2}
$$

More generally, the squared loss in (15.2) can be replaced by a task loss $\ell _ { \mathrm { t a s k } }$

Finetuning. Finetuning uses the same downstream prediction model structure, but it also updates the pretrained representation. The prediction model is $w ^ { \top } \phi _ { \theta } ( x )$ , with parameters w and θ. We optimize both parameters on the downstream data, initializing $\theta$ at the pretrained model $\hat { \theta }$ and usually initializing w randomly:

$$
\underset {w, \theta} {\text {minimize}} \frac {1}{n _ {\text {task}}} \sum_ {i = 1} ^ {n _ {\text {task}}} \ell_ {\text {task}} \Big (y _ {\text {task}} ^ {(i)}, w ^ {\top} \phi_ {\theta} (x _ {\text {task}} ^ {(i)}) \Big)\tag{15.3}
$$

$$
\text {with initialization} \quad w \leftarrow \text {random vector},\tag{15.4}
$$

$$
\theta \leftarrow \hat {\theta}.\tag{15.5}
$$

A related case is continued pretraining or finetuning with the same loss function form as pretraining (but different data). There, we start from $\hat { \theta }$

<!-- page: 195 -->

and keep training on another unlabeled dataset, often using the same type of pretraining loss as in (15.1). This is useful when the new data distribution is closer to the downstream domain than the original pretraining data.

Linear probing then finetuning (LP-FT). LP-FT is a simple two-stage adaptation method. First, it runs linear probing: the pretrained representation $\phi _ { \hat { \theta } }$ is frozen, and only the prediction head w is learned, as in (15.2). Second, it runs full finetuning, as in (15.5), initialized at the linear-probe head and at $\theta = { \hat { \theta } } .$ . The first stage finds a task-specific readout of the pre-trained representation, while the second stage allows the representation itself to adjust to the downstream data. This procedure was proposed as a way to reduce bad feature distortion during finetuning, and it can improve out-of-distribution performance in some settings [Kumar et al., 2022].

Various other adaptation methods exist and are sometimes specialized to the particular pretraining method or model class. We will discuss them in Chapter 17.

## 15.2 Low-rank adaptation (LoRA).

Full finetuning updates all parameters of a pretrained model. When the downstream tasks or downstream data distribution are not very far from pretraining, it is possible that the resulting finetuned models are not far from pretrained models, and thus not all degrees of freedom in the pretrained parameters need to be used. Low-rank adaptation, or LoRA [Hu et al., 2022], is a parameter-efficient finetuning method that freezes the pretrained weights and trains only a low-rank update to weight matrices.

For one linear layer, suppose the pretrained weight matrix is $W _ { 0 } \in$ $\mathbb { R } ^ { d _ { \mathrm { o u t } } \times d _ { \mathrm { i n } } }$ and the layer computes $h   =   W _ { 0 } x$ . Full finetuning of the parameters starting from $W _ { 0 }$ is equivalent to finding an unconstrained update $\Delta W$ and using $h   =   ( W _ { 0 } + \Delta W ) x$ . LoRA constrains the update to be low rank. For a chosen rank $r \ll$ min $( d _ { \mathrm { o u t } } , d _ { \mathrm { i n } } )$ , it writes

$$
\Delta W = B A, \qquad B \in \mathbb {R} ^ {d _ {\mathrm{out}} \times r}, \qquad A \in \mathbb {R} ^ {r \times d _ {\mathrm{in}}},\tag{15.6}
$$

and usually scales this update as

$$
h = W _ {0} x + \frac {\alpha}{r} B A x.\tag{15.7}
$$

The key point is that $W _ { 0 }$ is frozen and only A and B are trained. A dense update has $d _ { \mathrm { o u t } } d _ { \mathrm { i n } }$ trainable parameters, whereas the LoRA update has only

$$
r (d _ {\mathrm{out}} + d _ {\mathrm{in}})\tag{15.8}
$$

<!-- page: 196 -->

trainable parameters. Here r is the LoRA rank, α is commonly called LoRA alpha, and $\alpha / r$ is the LoRA scaling factor.

The rank controls the dimension of the update, while α controls the overall size of the update relative to the frozen pretrained matrix. A common initialization sets one factor to zero, for example $B   =   0 ,$ so that $BA   =   0$ at initialization and the adapted model initially computes exactly the same function as the pretrained model. The low-rank restriction should not be interpreted as saying that the final adapted weight matrix $W _ { 0 } + ( \alpha / r ) B A$ is low rank. Usually $W _ { 0 }$ is full rank; only the change to the pretrained matrix is low rank.

LoRA reduces the number of trainable parameters, and therefore reduces the memory needed for gradients and optimizer states of the trainable update. However, the frozen base weights $W _ { 0 }$ still have to be stored and used in the forward and backward passes, and the activations needed for backpropagation are not reduced by the low-rank parameterization. Thus, in settings where the base model weights and activations dominate memory, such as large model training with data parallelism or model parallelism, the training-time memory savings can be limited. Similarly, LoRA usually gives little compute savings, because most of the forward and backward computation through the base model is still performed.

Therefore, the biggest benefit of LoRA is often in settings where multiple users are sharing compute for inference or training. Since each adapter is small, one can store many task-specific adapters for the same base model in CPU memory or even GPU memory so that they can be swapped very fast. This allows for a system that serves multiple finetuned models on the same set of machines effectively simultaneously, swapping between customized models instantly, so that all users have low latency and the compute is heavily utilized even if some users use it only occasionally. It could also be useful in multi-tenant training systems: different training jobs may share the compute by sharing the same base weights while keeping separate LoRA updates, improving GPU utilization.

Finally, LoRA is also an expressivity tradeoff: it restricts each update to lie in a low-rank family. This can work well for many adaptation tasks, but for large distribution shifts or high-capacity adaptation, full-parameter training may still be preferable.

<!-- page: 197 -->

## Chapter 16

## Representation Learning

This Chapter introduces two concrete pretraining methods for representation learning: supervised pretraining and contrastive learning.

## 16.1 Supervised pretraining

Here, the pretraining dataset is a large-scale labeled dataset (e.g., ImageNet), and the pretrained models are simply a neural network trained with vanilla supervised learning (with the last layer being removed). Concretely, suppose we write the learned neural network as $U \phi _ { \hat { \theta } } ( x )$ , where U is the last (fullyconnected) layer parameters, $\hat { \theta }$ corresponds to the parameters of all the other layers, and $\phi _ { \hat { \theta } } ( x )$ are the penultimate activations layer (which serves as the representation). We simply discard U and use $\phi _ { \hat { \theta } } ( x )$ as the pretrained representation model.

## 16.2 Contrastive learning

Contrastive learning is a self-supervised pretraining method that uses only unlabeled data. The main intuition is that a good representation function $\phi _ { \theta } ( \cdot )$ should map semantically similar images/texts to similar representations, and that random pair of images/texts should generally have distinct representations. E.g., we may want to map images of two huskies to similar representations, but a husky and an elephant should have different representations. The idea of contrastive learning is broadly useful for images, texts, video, etc, but the rest of sections will mainly use images as the main driving example.

<!-- page: 198 -->

A key question in contrastive learning is how we obtain pair of similar images. One definition of similarity is that images from the same class are similar. Using this definition will result in the so-called supervised contrastive algorithms that work well when labeled pretraining datasets are available.

Without labeled data, we can use data augmentation to generate a pair of “similar” augmented images given an original image x. Data augmentation typically means that we apply random cropping, flipping, and/or color transformation on the original image x to generate a variant. We can take two random augmentations, denoted by ˆx and ${ \tilde { x } } ,$ of the same original image $x ,$ and call them a positive pair. We observe that positive pairs of images are often semantically related because they are augmentations of the same image. We will design a loss function for $\theta$ such that the representations of a positive pair, $\phi _ { \theta } ( \hat { x } ) , \phi _ { \theta } ( \tilde { x } )$ , as close to each other as possible.

On the other hand, we can also take another random image z from the pretraining dataset and generate an augmentation ẑ from z. Note that $( \hat { x } , \hat { z } )$ are from different images; therefore, with a good chance, they are not semantically related. We call $( \hat { x } , \hat { z } )$ a negative or random pair.1 We will design a loss to push the representation of random pairs, $\phi _ { \theta } ( \hat { x } ) , \phi _ { \theta } ( \hat { z } )$ , far away from each other.

There are many recent algorithms based on the contrastive learning principle, and here we introduce SIMCLR [Chen et al., 2020] as an concrete example. The loss function is defined on a batch of examples $( x ^ { 1 } , \cdots , x ^ { ( B ) } )$ with batch size $B .$ The algorithm computes two random augmentations for each example $x ^ { ( i ) }$ in the batch, denoted by $\hat { \mathcal { X } } ^ { ( i ) }$ and $\tilde { \mathcal { X } } ^ { ( i ) }$ . As a result, we have the augmented batch of 2B examples: $\hat { x } ^ { 1 } , \cdots , \hat { x } ^ { ( B ) } ,   \tilde { x } ^ { 1 } , \cdots , \tilde { x } ^ { ( B ) }$ . The SIMCLR loss is defined $\mathrm { a s ^ { 2 } }$

$$
L _ {\mathrm{pre}} (\theta) = - \sum_ {i = 1} ^ {B} \log \frac {\exp \left(\phi_ {\theta} (\hat {x} ^ {(i)}) ^ {\top} \phi_ {\theta} (\tilde {x} ^ {(i)})\right)}{\exp \left(\phi_ {\theta} (\hat {x} ^ {(i)}) ^ {\top} \phi_ {\theta} (\tilde {x} ^ {(i)})\right) + \sum_ {j \neq i} \exp \left(\phi_ {\theta} (\hat {x} ^ {(i)}) ^ {\top} \phi_ {\theta} (\tilde {x} ^ {(j)})\right)}.
$$

The intuition is as follows. The loss is increasing in $\phi _ { \theta } ( \hat { x } ^ { ( i ) } ) ^ { \top } \phi _ { \theta } ( \tilde { x } ^ { ( j ) } )$ , and thus minimizing the loss encourages $\phi _ { \theta } ( \hat { x } ^ { ( i ) } ) ^ { \top } \phi _ { \theta } ( \tilde { x } ^ { ( j ) } )$ to be small, making $\phi _ { \theta } ( \hat { x } ^ { ( i ) } )$ far away from $\phi _ { \theta } ( \tilde { x } ^ { ( j ) } )$ . On the other hand, the loss is decreasing in $\phi _ { \theta } \dot { ( \hat { x } ^ { ( i ) } ) ^ { \top } } \phi _ { \theta } ( \tilde { x } ^ { ( i ) } )$ , and thus minimizing the loss encourages $\phi _ { \theta } ( \hat { x } ^ { ( i ) } ) ^ { \top } \phi _ { \theta } ( \tilde { x } ^ { ( i ) } )$ to be large, resulting in $\phi _ { \theta } ( \hat { x } ^ { ( i ) } )$ and $\phi _ { \theta } ( \tilde { x } ^ { ( i ) } )$ to be close.<sup>3</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">ˆ</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Random pair may be a more accurate term because it’s still possible (though not likely) that x and z are semantically related, so are x and ẑ. But in the literature, the term negative pair seems to be also common.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>This is a variant and simplification of the original loss that does not change the essence</span></small>

<!-- page: 199 -->

![](images/page_198_image_1.jpg)

Figure 16.1: A schematic view of contrastive learning. Two augmentations of the same example form a positive pair, and the loss encourages their representations to have a large inner product. Augmentations of different examples act as random or negative pairs, and the loss encourages their representations to have smaller inner products.

## 16.3 Semantic retrieval

In Chapter 15, representations are mainly used as features or inputs for downstream supervised tasks with linear probing. With modern LLMs, lin ear probes for downstream tasks are much less needed, but representations or embeddings are still widely used for semantic retrieval: searching a large corpus for objects that are relevant to a query, even when relevance is not captured by exact word overlap. The query may be a natural-language question, a product description, an image, or a short piece of code, and the corpus may contain documents, passages, images, or other objects. For example, the query “how do I stop my model from memorizing the training set?” should retrieve a document about overfitting and regularization, even if the word “memorizing” does not appear in that document.

More formally, let $\mathcal { D }   =   \{ d _ { 1 } , \ldots , d _ { N } \}$ be a collection of documents, passages, images, or other objects. Given a query $q ,$ a retrieval system returns a short ranked list $d _ { i _ { 1 } } , d _ { i _ { 2 } } , \ldots , d _ { i _ { k } }$ where the top-ranked items should be more relevant to $q .$ Many retrieval systems also compute a score $s ( q , d )$ for each query-object pair, where a larger score means that d is predicted to be more

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(but may change the efficiency slightly).</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">− log p+q p</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p, q > .</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">p,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">in q when 0</span></small>

<!-- page: 200 -->

relevant to $q .$

Semantic retrieval with embeddings. Embeddings turn retrieval into geometric search. Suppose $\phi _ { \theta }$ is an embedding model, and let $\phi _ { \theta } ( q ) , \phi _ { \theta } ( d ) \in$ $\mathbb { R } ^ { m }$ be the embeddings of a query $q$ and a document $d .$ If the embeddings are normalized to have unit norm, then the inner product $\phi _ { \theta } ( q ) ^ { \top } \phi _ { \theta } ( d )$ is also the cosine similarity cos $\angle ( \phi _ { \theta } ( q ) , \phi _ { \theta } ( d ) )$ , and it is often used as the relevance score.

In advance, the embeddings of the entire corpus $\{ \phi _ { \theta } ( d _ { 1 } ) , \ldots , \phi _ { \theta } ( d _ { N } ) \}$ are computed and typically stored in a vector database. At query time, semantic retrieval becomes a vector search problem: compute $\phi _ { \theta } ( q )$ and find the objects whose stored embeddings $\phi _ { \theta } ( d _ { i } )$ have the largest inner products with it. A brute-force search over all N objects costs $O ( N m )$ per query. This is often too slow for large corpora, so practical systems use approximate nearest-neighbor indexes that search much faster while accepting a small chance of missing an exact nearest neighbor. Common methods include graph-based indexes such as HNSW [Malkov and Yashunin, 2020], quantization, and inverted-file indexes. Another approach, useful when most data live in object storage, uses a centroid-based ANN index [Chen et al., 2021]: the system first searches a small index of cluster centroids, then fetches the most promising clusters in a few large reads and reranks the candidates. This reduces random storage round trips compared with graph traversal, while still avoiding a full scan of the corpus.

Evaluation for retrieval. Typically, one retrieval evaluation dataset involves a set of queries and a corpus. For each query, there is a set of goldstandard relevant documents, denoted by $R ( q )$

Suppose the retrieval method returns an ordered list $\begin{array} { r l } { \hat { R } ( q ) } & { { } = } \end{array}$ $( d _ { i _ { 1 } ( q ) } , \ldots , d _ { i _ { k } ( q ) } )$ . A simple metric is recall at $k ,$ defined as $Recall @  k(q) =$ $| R ( \overset { \frown } { q } ) \cap \{ d _ { i _ { 1 } ( q ) } , \dots , d _ { i _ { k } ( q ) } \} | / | R ( q ) |$ , which ignores the ranking between the documents in $R ( q )$ and $\hat { R } ( q )$

Another common ranking metric is normalized discounted cumulative gain, or NDCG [Yilmaz et al., 2008].<sup>4</sup> For this metric, the evaluation dataset specifies a ground-truth relevance grade $s ^ { * } ( q , d ) \; \geq \; 0$ for query-document

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2s  1,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2s  1.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>See the [Wikipedia page on discounted cumulative gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) for a common exponentialgain version. That version replaces a relevance grade s by − and can equivalently be obtained by redefining the relevance score to be −</span></small>

<!-- page: 201 -->

## Retrieval-Augmented Generation (RAG)

![](images/page_200_image_2.jpg)

Figure 16.2: A schematic view of retrieval-augmented generation. A query is used to retrieve relevant documents from a corpus, and the generator conditions on both the query and the retrieved documents when producing its response.

pairs. For the retrieved list $\hat { R } ( q ) = ( d _ { i _ { 1 } ( q ) } , \ldots , d _ { i _ { k } ( q ) } )$ , define

$$
\mathrm{DCG} @ k (q) = \sum_ {j = 1} ^ {k} \frac {s ^ {*} (q , d _ {i _ {j} (q)})}{\log_ {2} (j + 1)}.\tag{16.1}
$$

If $s _ { ( 1 ) } ^ { * } ( q )   \geq   s _ { ( 2 ) } ^ { * } ( q )   \geq   \cdots$ · are the relevance grades of the corpus documents sorted in decreasing order for query $q ,$ then

$$
\mathrm{IDCG} @ k (q) = \sum_ {j = 1} ^ {k} \frac {s _ {(j)} ^ {*} (q)}{\log_ {2} (j + 1)},\tag{16.2}
$$

$$
\mathrm{NDCG} @ k (q) = \frac {\mathrm{DCG} @ k (q)}{\mathrm{IDCG} @ k (q)}.\tag{16.3}
$$

Thus the denominator normalizes DCG by the score of an ideal ordering. Unlike recall at $k ,$ NDCG rewards placing more relevant documents earlier in the ranked list.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">IDCG@k(q) = 0,</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">NDCG@k q 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>An edge case occurs when IDCG@k(q) = 0, for example if all relevance grades for query q are zero. Such queries are usually removed from retrieval-evaluation datasets, since they have no relevant document to retrieve. If such a query is nevertheless included, one common convention is to define ( ) = .</span></small>

<!-- page: 202 -->

## 16.4 Retrieval-augmented generation

Beyond the typical search application, retrieval is especially useful when AI models need to use a large collection of proprietary or customized documents. Retrieval-augmented generation, or RAG, combines two steps: first retrieve relevant information from a given corpus, and then generate an answer conditioned on the retrieved information. In the simplest form, if $\hat { R } ( q )$ denotes the top k retrieved items for query $q ,$ a language model generates $y   \sim   p _ { \psi } ( y | q , \hat { R } ( q ) )$ . This can make the output more grounded in a source corpus, and it allows the accessible knowledge to be updated by changing the corpus rather than retraining the language model.

<!-- page: 203 -->

## Chapter 17

## Large language models

Natural language processing is another area where pretraining models are particularly successful. The basic object we would like to learn is the distribution of language: which sentences are plausible, how a piece of text is likely to continue. If a model can assign probabilities to text sequences and sample continuations from conditional distributions, then many tasks can be phrased as conditional generation from a prompt. This is why language modeling, and in particular next-token prediction, is a useful pretraining objective for language data.

## 17.1 Tokenization

Before defining the language-modeling objective, we need to specify how raw text is represented as model inputs. A language model does not read a sentence as one raw string. Instead, the text is first broken into small pieces called tokens. A token is simply a unit of text that the model treats as one symbol: it may be a whole word like hello, part of a word like un, punctuation, whitespace, a byte in ASCII encoding, or a special marker such as an end-of-text token. A tokenizer is the preprocessing rule that converts a string into a sequence of tokens, which we identify with discrete ids

$$
x = (x _ {1}, \dots , x _ {T}), \qquad x _ {t} \in V,
$$

where V is the vocabulary, meaning the set of all tokens the tokenizer can output. For example, the sentence A dog runs. might be represented as tokens roughly corresponding to A, dog, runs, and .; a rarer word such as unhappiness might be split into pieces such as un, h, and appiness.

Modern language models usually use subword tokenization, often based on byte-pair encoding (BPE) [Sennrich et al., 2016, Kudo and Richardson,

<!-- page: 204 -->

2018]. Subword tokenization is a compromise between two simpler choices: character-level tokenization has a small vocabulary but makes every sentence long, while word-level tokenization makes common sentences short but struggles with rare or new words. For example, if a word-level vocabulary does not contain a rare biomedical term such as glioblastoma, or a newly coined form such as LLMification, it may need to map each whole string to an unknown token. A subword tokenizer can instead encode them using reusable pieces, such as glio+blast+oma or LL+M+ification, up to the exact learned segmentation. The intuition behind byte-pair encoding is to start from very small pieces, such as bytes or characters, and repeatedly add a new token for an adjacent pair that occurs often in the text corpus. After many such merges, common strings such as ing or tion, and oftentimes whole common words, can be represented by one token, while rare words can still be represented by smaller pieces. Once the tokenizer is fixed, pretraining is formulated over token sequences rather than raw text; the choice of tokenizer affects the vocabulary size $| V |$ and the resulting sequence length $T$ . The vocabulary size $| V |$ can be on the order of $1 0 ^ { 5 } ;$ for example, Qwen3.5 uses a vocabulary of 248,320 tokens.

## 17.2 Autoregressive models and next-token prediction loss

We typically operate on the sequence level in the pre-training, that is, each “example” is a sequence. A document (or a concatenation of multi-ple documents) will be first tokenized into a sequence of tokens, denoted by $x = ( x _ { 1 } , \cdots , x _ { T } )$ , where each $x _ { i }$ is a token that belongs to the vocabulary V . When convenient, we identify the tokens in V with the indices $\{ 1 , \ldots , | V | \}$

A language model is a probabilistic model representing the probability of the sequence, denoted by $p ( x _ { 1 } , \cdots , x _ { T } )$ . This probability distribution is very complex because its support is $V ^ { T }$ with size $| V | ^ { T }$ . The vocabulary size $| V |$ can be on the order of $1 0 ^ { 5 }$ ; for example, Qwen3.5 uses a vocabulary of 248,320 tokens. And $T$ can easily be on the order of 10K or as large as $\mathrm { 1 M } ,$ and thus $| V | ^ { T }$ is an astronomical number. Thus, instead of modeling the distribution of a sequence itself, we apply the chain rule of conditional probability to decompose it as follows:

$$
p (x _ {1}, \dots , x _ {T}) = p (x _ {1}) p (x _ {2} | x _ {1}) \dots p (x _ {T} | x _ {1}, \dots , x _ {T - 1}).\tag{17.1}
$$

Now the support size of each of the conditional probability $p ( x _ { t } | x _ { 1 } , \cdots , x _ { t - 1 } )$ is $| V |$

<!-- page: 205 -->

![](images/page_204_image_1.jpg)

Figure 17.1: The inputs and outputs of a Transformer model.

We will model the conditional probability $p ( x _ { t } | x _ { 1 } , \cdots , x _ { t - 1 } )$ as a function of $x _ { 1 } , \ldots , x _ { t - 1 }$ parameterized by some parameter θ.

A parameterized model takes in numerical inputs and therefore we first introduce embeddings or representations of the tokens. Let $e _ { i } \in \mathbb { R } ^ { 1 \times d }$ be the row-vector embedding of the i-th token. Let

$$
E = \left[ \begin{array}{c} e _ {1} \\ e _ {2} \\ \vdots \\ e _ {| V |} \end{array} \right] \in \mathbb {R} ^ {| V | \times d}\tag{17.2}
$$

be the collection of the embeddings..

The most commonly used models are autoregressive versions of the Trans former [Vaswani et al., 2017] and its variants. In this section, we will introduce the input-output interface of a Transformer, but treat the intermediate computation in the Transformer as a black box, while in Section 17.3 we will discuss the details of the Transformer and other variants.

As shown in Figure 17.1, given a tokenized document $( x _ { 1 } , \cdots , x _ { T } )$ , we first translate the sequence of discrete variables into a sequence of corresponding token embeddings $( e _ { x _ { 1 } } , \cdots , e _ { x _ { T } } ) . ^ { 1 }$ We also introduce a fixed special token $x _ { 0 }   =   \bot$ in the vocabulary with corresponding embedding $e _ { \perp }$ to mark the beginning of a document. Then, the token embeddings are passed into a Transformer model, which takes in a sequence of vectors $( e _ { x _ { 0 } } , e _ { x _ { 1 } } , \cdots , e _ { x _ { T } } )$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">(x1, . . . , xT )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>The mapping from raw text to is determined by the tokenizer introduced in Section 17.1. The treatment of special boundary tokens is also model- and tokenizerdependent: some models prepend a beginning-of-sequence token, while others pack documents into long streams and use end-of-text tokens after each document, without inserting a separate beginning token. We also omit positional encodings from this input-output interface; practical Transformers add positional information to distinguish token order, and we will add this discussion in a future revision.</span></small>

<!-- page: 206 -->

and outputs a sequence of vectors $( u _ { 1 } , u _ { 2 } , \cdots , u _ { T + 1 } )$ , where $u _ { t } \in \mathbb { R } ^ { | V | }$ will be interpreted as the logits for the probability distribution of the next token. Here we use the autoregressive version of the Transformers which by design ensures $u _ { t }$ only depends on $x _ { 1 } , \cdots , x _ { t - 1 }$ (see Section 17.3 for the definition of Transformers, and note that this property does not hold in masked language models [Devlin et al., 2019] where the losses are also different.) We view the whole mapping from x’s to u’s as a black box in this subsection and call it a Transformer, denoted by $f _ { \theta }$ , where θ includes both the parameters in the Transformer and the input embeddings. We write $u _ { t } = f _ { \theta } ( x _ { 0 } , x _ { 1 } , \ldots , x _ { t - 1 } )$ where $f _ { \theta }$ denotes the mapping from the input to the outputs.

The conditional probability $p _ { \theta } ( x _ { t } | x _ { 1 } , \cdots , x _ { t - 1 } )$ is the softmax of the logits:

$$
\left[ \begin{array}{c} p _ {\theta} (x _ {t} = 1 | x _ {1} \dots , x _ {t - 1}) \\ p _ {\theta} (x _ {t} = 2 | x _ {1} \dots , x _ {t - 1}) \\ \vdots \\ p _ {\theta} (x _ {t} = | V | | x _ {1} \dots , x _ {t - 1}) \end{array} \right] = \text {softmax} (f _ {\theta} (x _ {0}, \ldots , x _ {t - 1})) \in \mathbb {R} ^ {| V |}\tag{17.3}
$$

Autoregressive generation / sampling / inference. Given an autoregressive Transformer, we can sample text from it sequentially. Given a prefix $x _ { 1 } , \ldots , x _ { t }$ , we generate a token completion $x _ { t + 1 } , \ldots , x _ { T }$ sequentially using the conditional distribution.

$$
x _ {t + 1} \sim \mathrm{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t}))\tag{17.4}
$$

$$
x _ {t + 2} \sim \mathrm{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t + 1}))\tag{17.5}
$$

(17.6)

$$
x _ {T} \sim \mathrm{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {T - 1})).\tag{17.7}
$$

Note that each generated token is used as the input to the model when generating the following tokens. In practice, people often introduce a parameter $\tau \; > \; 0$ named temperature to further adjust the entropy/sharpness of the generated distribution,

$$
x _ {t + 1} \sim \mathrm{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t}) / \tau)\tag{17.8}
$$

$$
x _ {t + 2} \sim \mathrm{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t + 1}) / \tau)\tag{17.9}
$$

(17.10)

$$
x _ {T} \sim \operatorname{softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {T - 1}) / \tau).\tag{17.11}
$$

When $\tau = 1$ , the text is sampled from the original conditional probability defined by the model. With a decreasing τ , the generated text gradually

<!-- page: 207 -->

![](images/page_206_image_1.jpg)

Figure 17.2: Autoregressive generation feeds each newly generated token back into the prefix before generating the next token.

becomes more “deterministic”. $\tau \to 0$ reduces to greedy decoding, where we generate the most probable next token from the conditional probability.

Two other common decoding heuristics are top-k sampling and top-p sampling, also called nucleus sampling. Instead of sampling from the full vocabulary distribution, top-k sampling keeps only the k tokens with largest probability and renormalizes the distribution over this smaller set. Top-p sampling keeps the smallest set of highest-probability tokens whose total probability is at least $p ,$ and renormalizes over that set. These methods are inference-time choices rather than changes to the parameterized probability distribution of the resulting training loss; they are often combined with temperature to avoid sampling from the long tail of very unlikely tokens while still allowing non-greedy generations. For example, a common choice is top p sampling with p = 0.9 together with a temperature in the range 0.7–1.0, which avoids sampling from the long tail of very unlikely tokens while still allowing non-greedy generations.

Pre-training auto-regressive LLMs The pretraining loss for training an auto-regressive Transformer θ is simply the maximum likelihood estimator, that is, minimizing the negative log-likelihood of seeing the data under the probabilistic model defined by θ, which is the cross-entropy loss on the logits. Note for convenience people normalized by the sequence length T. For one

<!-- page: 208 -->

sequence, it writes

$$
\begin{array}{l} \text {loss} (x _ {1}, \dots , x _ {T}; \theta) = - \frac {1}{T} \log p _ {\theta} (x _ {1}, \dots , x _ {T}) \\ \quad = \frac {1}{T} \sum_ {t = 1} ^ {T} - \log (p _ {\theta} (x _ {t} | x _ {0}, \dots , x _ {t - 1})) \\ \quad = \frac {1}{T} \sum_ {t = 1} ^ {T} \ell_ {\mathrm{ce}} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t - 1}), x _ {t}) \\ \quad = \frac {1}{T} \sum_ {t = 1} ^ {T} - \log (\text {softmax} (f _ {\theta} (x _ {0}, x _ {1}, \dots , x _ {t - 1})) _ {x _ {t}}). \end{array} \tag {1}\tag{17.12}
$$

(17.13)

In practice there are a larger number of training sequences, and the resulting training loss is the average of the loss over all sequences. A common optimizer for modern language-model training is AdamW [Loshchilov and Hutter, 2019], which takes a mini-batch of these sequences, computes the gradient, and applies the update rule.

## 17.3 Transformer architecture

Transformers, the dominant model architecture for language modeling, are composed of multiple blocks of multi-head self-attention and MLPs. The MLPs typically use GELU activations or SwiGLU activations as we mentioned in Section 7.3. In this section, we will introduce self-attention in details. We start with single-head self-attention, introduce multi-head self-attention , and its two variants: multi-query attention and grouped-query attention. We will then describe how multi-head self-attention and MLPs are connected as building blocks inside a Transformer.

As the input to the language model is a sequence of tokens, the model needs to gather information from all the previous tokens to predict the next token. This is not easily achievable in the standard feedforward neural net works, as the input dimension will be changing with T. The self-attention mechanism introduced in this section is the core design today for fusing information from different positions of the input sequence.<sup>2</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>We do not discuss positional embeddings in this section. They are important in practice: self-attention by itself is permutation-equivariant, so a Transformer needs some positional signal, such as learned absolute positional embeddings, sinusoidal embeddings, rotary positional embeddings, or related variants, to distinguish token order. We will add this discussion in a future revision.</span></small>

<!-- page: 209 -->

Single-head self-attention. Single-head self-attention, denoted by att1h(·), is a function whose input is a sequence of vectors (which are either embeddings or hidden activation) $( h _ { 1 } ^ { \mathrm { i n } } , \ldots , h _ { T } ^ { \mathrm { i n } } )$ and output is also a sequence of vectors (which are always activations) $\left( h _ { 1 } ^ { \mathrm { o u t } } , \dots , h _ { T } ^ { \mathrm { o u t } } \right)$ , where each hidden state is represented as a row vector: $h _ { t } ^ { \mathrm { i n } }   \in   \mathbb { R } ^ { 1 \times d }$ and $h _ { t } ^ { \mathrm { o u t } }   \in   \mathbb { R } ^ { 1 \times d _ { h } }$ for all $t   \in   \{ 1 , \ldots , T \}$ . Equivalently, if we stack the input and output vectors into matrices, then att1h maps an input matrix $H ^ { \mathrm { i n } } \in \mathbb { R } ^ { T \times d }$ to an output matrix $H ^ { \mathrm { o u t } } \; \in \; \mathbb { R } ^ { T \times d _ { h } }$ The parameters of the attention layer are $\bar { W ^ { Q } , W ^ { K } , W ^ { V } } \; \in \; \mathbb { R } ^ { d \times d _ { h } }$ , which are often called the query, key, and value projection matrices.

The first step of single-head self-attention linearly transforms the input vectors into queries, keys, and values by multiplying by the query, key and value projection matrices. Intuitively, we can think of the query vector as asking ”what information am I looking for?”, the key vector as advertising”what information I have?”, and the value vector as providing the actual information to be passed forward if the query and key match.

$$
q _ {1} = h _ {1} ^ {\mathrm{in}} W ^ {Q}, \dots , q _ {T} = h _ {T} ^ {\mathrm{in}} W ^ {Q},\tag{17.14}
$$

$$
k _ {1} = h _ {1} ^ {\mathrm{in}} W ^ {K}, \dots , k _ {T} = h _ {T} ^ {\mathrm{in}} W ^ {K},\tag{17.15}
$$

$$
v _ {1} = h _ {1} ^ {\mathrm{in}} W ^ {V}, \dots , v _ {T} = h _ {T} ^ {\mathrm{in}} W ^ {V}.\tag{17.16}
$$

Then, for each position t in the sequence, we compute the inner product of its query with the keys of all the tokens $q _ { t } k _ { 1 } ^ { \top } , \ldots , q _ { t } k _ { T } ^ { \top }$ . Without any masking (a concept that we will introduce later), the attention scores $p _ { t , 1 } , \ldots , p _ { t , T }$ are defined by applying the softmax function to these inner products.

$$
p _ {t, 1}, \dots , p _ {t, T} = \operatorname{softmax} (q _ {t} k _ {1} ^ {\top} / c, \dots , q _ {t} k _ {T} ^ {\top} / c).\tag{17.17}
$$

where c is a scaling factor. The inner product between $q _ { t }$ and $k _ { j }$ here are often referred to as “attention”, because it intuitively tries to figure out how much the output of token t should depend on, or pay attention to, the token $j .$ The total attention is normalized to sum 1 by the softmax.

In Vaswani et al. [2017], $c = \sqrt { d _ { h } }$ . A simple intuition for this scaling is as follows. Suppose that at initialization the coordinates of the query vector q and key vector k behave like independent random variables with mean zero and variance 1 (or, more generally, O(1)). Then their dot product

$$
q \cdot k = \sum_ {i = 1} ^ {d _ {h}} q _ {i} k _ {i}
$$

<!-- page: 210 -->

has mean zero and variance $d _ { h }$ up to constants. Without scaling, the attention logits would therefore grow with the head dimension, which will make the magnitude of the logits too large for large $d _ { h }$ and as a result the attention score into the saturated regime, which results in very small gradients. Divid ing by $\sqrt { d _ { h } }$ keeps the variance of the logits on the order of one. This is only a heuristic, since the query and key vectors are not generally independent in an actual Transformer. The output of the self-attention at position t is the linear combination of value vectors with attention scores as the coefficient,

$$
h _ {t} ^ {\mathrm{out}} = \sum_ {j = 1} ^ {T} p _ {t, j} v _ {j}.\tag{17.18}
$$

In this way, self-attention mixes the values vectors across positions according to the attention scores.

The same computation can be written compactly in matrix form. Stack the query, key, and value row vectors into matrices $Q , K , V \in \mathbb { R } ^ { T \times d _ { h } }$ as

$$
Q = \left[ \begin{array}{c} q _ {1} \\ \vdots \\ q _ {T} \end{array} \right] = H ^ {\mathrm{in}} W ^ {Q}, \qquad K = \left[ \begin{array}{c} k _ {1} \\ \vdots \\ k _ {T} \end{array} \right] = H ^ {\mathrm{in}} W ^ {K}, \qquad V = \left[ \begin{array}{c} v _ {1} \\ \vdots \\ v _ {T} \end{array} \right] = H ^ {\mathrm{in}} W ^ {V}.\tag{17.19}
$$

Thus the t-th rows of $Q , K , V$ are $q _ { t } , k _ { t } , v _ { t }$ . Without any masking (which will be introduced a bit later), single-head attention can be written in matrix form as follows,

$$
H ^ {\mathrm{out}} = \operatorname{softmax} _ {\mathrm{row}} \left(Q K ^ {\top} / c\right) V,\tag{17.20}
$$

The matrix form is not a new model, but the same per-position rule written so all pairwise query-key comparisons can be computed in parallel. This is one reason attention fits modern accelerators well despite the quadratic number of pairwise scores. where $\mathrm { s o f t m a x } _ { \mathrm { r o w } }$ applies softmax separately to each row (corresponding to each query vector). One can verify that the t-th row of the matrix softma $\operatorname { a x } _ { \operatorname { r o w } } \bigl ( Q K ^ { \top } / c \bigr )$ is exactly the attention scores $p _ { t , 1 } , \ldots , p _ { t , T }$ defined in (17.17), and thus the t-th row of $H ^ { \mathrm { o u t } }$ is equal to the $h _ { t } ^ { \mathrm { o u t } }$ defined in (17.18).

Masking. In an autoregressive Transformer, the final output at position $t ,$ that is $f _ { \theta } ( x _ { 0 } , \ldots , x _ { t } )$ defined in Section 17.2, shouldn’t depend on any $x _ { j }$ with $j   >   t$ . As we will see in later part where we combine attention with

<!-- page: 211 -->

MLP into a Transformer, the autoregressive property corresponds to the requirement for the attention module that the output vector at position t should not depend on any input vector at position $j > t$ . This is achieved by modifying the definition of the attention by introducing an attention mask $M   \in   \mathbb { R } ^ { T \times T }$ before the softmax operation, The mask is what lets us train on a full sequence in parallel while preserving the left-to-right prediction rule. Every position can be processed in the same forward pass, but the mask prevents position t from using tokens that would not be available when predicting the next token autoregressively.

$$
H ^ {\mathrm{out}} = \operatorname{softmax} _ {\mathrm{row}} \bigl (Q K ^ {\top} / c + M \bigr) V.\tag{17.21}
$$

The most common mask is called causal mask, which is precisely for achieving the autoregressive property: $M _ { t , j } = 0$ for $j \leq t$ and $M _ { t , j } = - \infty$ for $j > t .$ . The −∞ entries make the corresponding softmax probabilities exactly zero, so each output hidden state depends only on the current and previous positions. Concretely, one can verify that for the t-th position or t-th row, the logits before attention are

$$
q _ {t} k _ {1} ^ {\top} / c, \dots , q _ {t} k _ {t} ^ {\top} / c, - \infty , - \infty , \dots , - \infty .\tag{17.22}
$$

As a result, the attention scores are

$$
p _ {t, 1}, \dots , p _ {t, T} = \operatorname{softmax} (q _ {t} k _ {1} ^ {\top} / c, \dots , q _ {t} k _ {t} ^ {\top} / c, - \infty , - \infty , \dots , - \infty),\tag{17.23}
$$

so $p _ { t , j } = 0$ for all $j > t$ . The final output at position t is

$$
h _ {t} ^ {\mathrm{out}} = \sum_ {j = 1} ^ {t} p _ {t, j} v _ {j},\tag{17.24}
$$

which doesn’t depend on any information after the t-th step. Attention masks are useful for other purposes such as ignoring padding tokens in batched sequences, or imposing block-structured visibility constraints when different parts of the input should not attend to one another. We will discuss these use cases in later sections when they are needed.

(Multi-head) Attention. One attention layer has multiple attention heads in parallel by combining many single-head attention modules. Concretely, the output of attention is the linear transformation of the concatenation of the multiple single-head self-attention outputs. Suppose we have $n _ { h }$ attention heads, or more precisely, $n _ { h }$ single-head attention modules that are

<!-- page: 212 -->

![](images/page_211_image_1.jpg)

Figure 17.3: The structure of Transformers and Transformer blocks.

denoted by att $\mathrm { 1 h _ { 1 } , \cdots , a t t 1 h _ { \it n _ { h } } }$ . In practice, people choose $n _ { h }$ and $d _ { h }$ satisfying $n _ { h } { \cdot } d _ { h } = d$ . Recall that the outputs of these single-head attention modules are att $1 { \operatorname { h } } _ { 1 } ( h _ { 1 } , \ldots , h _ { T } ) , \cdots$ , att $\operatorname { l h } _ { n _ { h } } ( h _ { 1 } , \ldots , h _ { T } )$ , each of which is a sequence of vectors. Let $\operatorname { a t t 1 h } _ { j } ( h _ { 1 } , \ldots , h _ { T } ) _ { t }$ be the t-th vector in $\operatorname { a t t 1 h } _ { j } ( h _ { 1 } , \ldots , h _ { T } )$ , and let $z _ { t }$ be the concatenation of att $1 { \operatorname { h } } _ { 1 } ( h _ { 1 } , \ldots , h _ { T } ) _ { t } , \cdots$ , att $\operatorname { l h } _ { n _ { h } } ( h _ { 1 } , \ldots , h _ { T } ) _ { t }$ which is viewed as an $n _ { h } \cdot   d _ { h }$ dimensional row vector. Multi-head self-attention introduces an additional parameter, the output weight matrix $W ^ { O } \in \mathbb { R } ^ { ( n _ { h } \cdot d _ { h } ) \times d }$ , and applies it on $z _ { t }$ to get the t-th output of the multi-head attention. More precisely,

$$
\mathrm{att} (h _ {1}, \dots , h _ {T}) = (z _ {1} W ^ {O}, \dots , z _ {T} W ^ {O}).\tag{17.25}
$$

For clarity, the attention layer with $n _ { h }$ heads takes in a sequence of $T$ vectors of dimension d and outputs a sequence of T vectors of dimension d. Multiple heads let the layer run several attention rules in parallel. Different heads can specialize in different kinds of token interactions, and the output projection then recombines these separate views into one d-dimensional representation at each position.

Auto-regressive Generation and KV cache Equation (17.21) is the model behavior when all the tokens are available. This is an operation that is needed in (1) training the model where the tokens are given (from the pre-training datasets or self-generated in previous iteration of the model as in RL), and we are interested in computing the likelihood of the current model weights to generate the given sequence of tokens, or (2) the sequence of tokens is users’ prompts.

To generate new tokens from the model, one needs to generate each of $x _ { t }$ one-by-one, and then feed the generated results back to the transformer as

<!-- page: 213 -->

shown in (17.7). Note that the computations in (17.7) share prefixes. For example, $f _ { \theta } ( x _ { 0 } , \cdots , x _ { j } )$ and $f _ { \theta } ( x _ { 0 } , \cdots , x _ { k } )$ for $j < k$ both involve computing the keys and values for positions up to $j ,$ so these computations can be cached and do not require recomputation. This collection of cached key and value vectors is referred to as the KV-cache. In particular, at time $t ,$ the running KV-cache is the collection of all keys and values up to $t ,$

$$
K _ {1: t} = \left[ \begin{array}{c} k _ {1} \\ \vdots \\ k _ {t} \end{array} \right], \qquad V _ {1: t} = \left[ \begin{array}{c} v _ {1} \\ \vdots \\ v _ {t} \end{array} \right],\tag{17.26}
$$

and the attention output at the t-th position can be computed as

$$
h _ {t} ^ {\mathrm{out}} = \operatorname{softmax} \left(\frac {q _ {t} K _ {1 : t} ^ {\top}}{c}\right) V _ {1: t}.\tag{17.27}
$$

As t increments, the KV-cache is appended with new rows $k _ { t + 1 } , v _ { t + 1 }$ , respectively, but the previously cached keys and values do not need to be recomputed. This avoids recomputing keys and values for the whole prefix at every decoding step. We note that the cache above is only for a single attention head, and for standard attention with multiple heads, each head involves a collection of keys and values to be saved in GPU memory.

Transformer. Transformers are largely compositions of alternating applications of attention and $\mathrm { M L P s }$ , where MLPs are applied on each individual position (with shared weights) separately, as shown in Figure 17.3.

There are some detailed options on how to combine these. A layer in transformer often refers to a combination of attention and MLP layer. Let $( h _ { 1 } ^ { \ell } , \ldots , h _ { T } ^ { \ell } )$ denote the row-vector hidden states entering layer $\ell ,$ where $h _ { t } ^ { \ell } \in$ $\mathbb { R } ^ { 1 \times d }$ , and let $( h _ { 1 } ^ { \ell + 1 } , \ldots , h _ { T } ^ { \ell + 1 } )$ denote the hidden states leaving the layer. There are two kinds of mainstream structures: PostNorm and PreNorm. In PreNorm, the layer normalization is applied before the MLP and the self-attention.

$$
r _ {t} = h _ {t} ^ {\ell} + [ \mathrm{att} (\mathrm{LN} (h _ {1} ^ {\ell}), \dots , \mathrm{LN} (h _ {T} ^ {\ell})) ] _ {t}\tag{17.28}
$$

$$
h _ {t} ^ {\ell + 1} = r _ {t} + \mathrm{MLP} (\mathrm{LN} (r _ {t})).\tag{17.29}
$$

In PostNorm, the layer normalization is applied after the residual connection.

<!-- page: 214 -->

$$
r _ {t} = \mathrm{LN} (h _ {t} ^ {\ell} + [ \mathrm{att} (h _ {1} ^ {\ell}, \dots , h _ {T} ^ {\ell}) ] _ {t})\tag{17.30}
$$

$$
h _ {t} ^ {\ell + 1} = \mathrm{LN} (r _ {t} + \mathrm{MLP} (r _ {t})).\tag{17.31}
$$

See Figure 17.3 for an illustration of PreNorm and PostNorm Transformer block structures. Modern large language models usually use PreNorm structure, and with RMSNorm instead of layer norm.

Memory and compute. We discuss the memory and compute costs of attention.

Compute. In training and prompt prefilling, when all tokens are given, each attention head costs $O ( T ^ { 2 } d _ { h } )$ arithmetic operations for the masked attention computation in Equation (17.21). For multi-head attention with $n _ { h }$ heads, the $n _ { h }$ copies of Equation (17.21) cost $O ( T ^ { 2 } d _ { h } n _ { h } )$ operations, while the output projection in Equation (17.25) costs $O ( T n _ { h } d _ { h } d )$ operations and is smaller and not the dominating term for large T. The important takeaway is that the attention computation is quadratic in $T .$ , which is a main source of difficulty for long-context settings where $T$ is larger than 10K, and sometimes up to 1M or more.

During generation, the total number of attention operations needed to generate $T$ tokens is of the same order, but generation must be done sequentially token by token. This often makes it harder to saturate GPU parallelism and achieve an optimal level of utilization.

Memory. The GPU memory usage of attention depends on exactly how the computation is implemented. In training and prefilling, a naive implementation of Equation (17.21) costs $T ^ { 2 }$ memory per head because the attention-score matrix $Q K ^ { \top }$ has $T ^ { 2 }$ entries. However, methods such as FlashAttention [Dao et al., 2022] can use memory linear in T for the attention computation, essentially saving $Q ,$ K, and V and recomputing or streaming the attention scores through an equivalent sequence of operations, rather than explicitly materializing the full $Q K ^ { \top }$ matrix.

In generation and decoding, the KV cache needs to be saved in GPU memory, which costs $O ( T d _ { h } )$ per head for a length-T context, unless one is willing to move part of the KV cache to CPU memory, which is comparatively slow.

In the next section, we discuss ways to improve efficiency by changing the attention architecture.

<!-- page: 215 -->

## 17.4 Variants of Attention

GQA, MQA, and sliding window attention. Several attention variants reduce the memory size of the KV cache. Multi-query attention (MQA) keeps multiple query heads but shares a single key head and a single value head across them [Shazeer, 2019]. Grouped-query attention (GQA) is an intermediate design: the query heads are partitioned into groups, and each group shares one key head and one value head [Ainslie et al., 2023]. Thus, ordinary multi-head attention, GQA, and MQA form a spectrum trading off model quality and decoding efficiency, with the KV cache size decreasing as fewer key-value heads are used.

Mathematically, GQA means that for the t-th position, we have $n _ { h }$ queries, denoted by $q _ { t , 1 } , \ldots , q _ { t , n _ { h } }$ , and $n _ { g }$ keys and values, denoted by $k _ { t , 1 } , \cdots , k _ { t , n _ { g } }$ and $v _ { t , 1 } , \cdots , v _ { t , n _ { g } } ,$ where $n _ { g }$ divides $n _ { h }$ . Let $\tau \; = \; n _ { h } / n _ { g }$ be the number of query heads assigned to each key/value head. For query head $j \in \{ 1 , \ldots , n _ { h } \}$ , define the group index

$$
g (j) = \left\lfloor \frac {j - 1}{\tau} \right\rfloor + 1 \in \{1, \dots , n _ {g} \}.\tag{17.32}
$$

Thus the query head $j$ uses the key and value head $g ( j )$ . Let $Q _ { j }$ be the matrix whose t-th row is $q _ { t , j }$ for $j   \in   \{ 1 , \ldots , n _ { h } \}$ . For $s   \in   \{ 1 , \ldots , n _ { g } \}$ , let $K _ { s } , V _ { s }$ be the matrices whose t-th rows are $k _ { t , s }$ and $v _ { t , s } ,$ respectively.

$$
Q _ {j} = \left[ \begin{array}{c} q _ {1, j} \\ \vdots \\ q _ {T, j} \end{array} \right], \qquad K _ {s} = \left[ \begin{array}{c} k _ {1, s} \\ \vdots \\ k _ {T, s} \end{array} \right], \qquad V _ {s} = \left[ \begin{array}{c} v _ {1, s} \\ \vdots \\ v _ {T, s} \end{array} \right].\tag{17.33}
$$

The j-th output head, denoted by $H _ { j } ^ { \mathrm { o u t } }$ , is then computed by

$$
H _ {j} ^ {\mathrm{out}} = \operatorname{softmax} _ {\mathrm{row}} \left(\frac {Q _ {j} K _ {g (j)} ^ {\top}}{c} + M\right) V _ {g (j)},\tag{17.34}
$$

where M is the attention mask, such as the causal mask in autoregressive decoding. Standard multi-head attention is the special case $n _ { g } = n _ { h }$ , while MQA is the special case $n _ { g } = 1$

Another approach is sliding-window attention, where each token only attends to the most recent $w$ tokens instead of the entire prefix. This corresponds to a causal local attention mask

$$
M _ {t, j} = \left\{ \begin{array}{l l} 0, & \max (1, t - w + 1) \leq j \leq t, \\ - \infty , & \text {otherwise}, \end{array} \right.\tag{17.35}
$$

<!-- page: 216 -->

so keys and values older than the window do not affect the current output and need not remain in the active KV cache.

Query-key normalization. Another attention variant is query-key normalization, or QK-Norm [Henry et al., 2020]. In standard attention, the attention logits are dot products $q _ { t } k _ { j } ^ { \top } / c ,$ so their magnitude depends on the norms of the query and key vectors. If these norms become large, the softmax distribution can become very sharp or saturated. QK-Norm instead normalizes each query and key vector before taking their dot product, for example replacing $q _ { t } k _ { j } ^ { \top }$ with a scaled cosine similarity RMSNorm $( q _ { t } ) \mathrm { R M S N o r m } ( k _ { j } ) ^ { \top }$ for RMSNorm defined in Equation (7.51). The motivation is to control the scale of attention logits and improve training stability while still letting the model learn the overall sharpness of the attention distribution. This approach has been adopted in several recent open-weight models, for example, Qwen3 and OLMo2 [Yang et al., 2025, OLMo Team et al., 2024].

## 17.5 Mixture-of-Experts Layers

A different way to increase the size of a Transformer is to make some layers sparse. The most common example is a Mixture-of-Experts (MoE) layer. In an ordinary Transformer block, the MLP is a dense module: every token is processed by the same MLP, so every token uses the same parameters and incurs the same MLP computation. In an MoE block, the model instead has several MLPs, called experts, and a small routing network decides which experts should process each token.

Concretely, suppose the layer has experts $E _ { 1 } , \ldots , E _ { m }$ , where each $E _ { s }$ is an MLP. Given the hidden state $h _ { t }$ of token $t ,$ a router computes routing weights

$$
r _ {t} = \sigma (h _ {t} W ^ {R}) \in \mathbb {R} ^ {m},
$$

where $\sigma$ is a routing function, commonly a softmax over experts or a sigmoid applied to each expert score. The model then chooses a small set $S _ { t }$ of experts, often of a constant size k, and combines their outputs as

$$
\mathrm{MoE} (h _ {t}) = \sum_ {s \in S _ {t}} \alpha_ {t, s} E _ {s} (h _ {t}), \qquad \alpha_ {t, s} = \frac {r _ {t , s}}{\sum_ {j \in S _ {t}} r _ {t , j}}.
$$

For example, DeepSeek-V3 uses 256 routed experts in each MoE layer and activates the top 8 routed experts for each token, in addition to one shared expert [DeepSeek-AI, 2024]. A shared expert is applied to every token, so it

<!-- page: 217 -->

acts as a common feedforward path while the routed experts provide token dependent specialization. Thus each token only activates a few experts, even though the layer contains many expert parameters. This is the main appeal of MoE: it increases the total parameter count and representational capacity of the model without increasing the per-token computation by the same factor. One can think of the router as choosing which specialized MLPs are most relevant for the current token and context. MoE layers are usually used to replace some or all of the dense MLP layers in a Transformer block.

## 17.6 In-context learning

In-context learning is mostly used for few-shot settings where we have a few labeled examples $\left[ ( x _ { \mathrm { t a s k } } ^ { ( 1 ) } , y _ { \mathrm { t a s k } } ^ { ( 1 ) } ) , \cdots , ( x _ { \mathrm { t a s k } } ^ { ( n _ { \mathrm { t a s k } } ) } , y _ { \mathrm { t a s k } } ^ { ( n _ { \mathrm { t a s k } } ) } ) \right.$ . Given a test example $x _ { \mathrm { t e s t } }$ , we construct a prompt $( x _ { 1 } , \cdots , x _ { T } )$ by concatenating the labeled examples and the test example in some format. For example, we may construct the prompt as follows

$$
\begin{array}{r l r l r l} x _ {1}, \dots , x _ {T} & = & \text {"Q: 2 \sim 3 = ?"} & & x _ {\mathrm{task}} ^ {(1)} \\ & & \mathrm{A:5} & & y _ {\mathrm{task}} ^ {(1)} \\ & & \mathrm{Q:6\sim7=?} & & x _ {\mathrm{task}} ^ {(2)} \\ & & \mathrm{A:13} & & y _ {\mathrm{task}} ^ {(2)} \\ & & \dots \\ & & \mathrm{Q:15\sim2=?"} & & x _ {\mathrm{test}} \end{array}
$$

Then, we let the pretrained model generate the most likely $x _ { T + 1 } , x _ { T + 2 } , \cdots$ In this case, if the model can “learn” that the symbol ∼ means addition from the few examples, we will obtain the following which suggests the answer is 17.

$$
x _ {T + 1}, x _ {T + 2}, \dots = \text {"A: 17"}.
$$

The same idea can be used as more practical prompts. For instance, suppose we want a language model to classify customer-support messages while also returning the answer in a fixed machine-readable format. We may

<!-- page: 218 -->

give the model examples such as

“Task: Classify each message as {billing, technical, account}. Return JSON.

Message: I was charged twice for my subscription.

Output: {“label”: “billing”}

Message: The app crashes when I upload a file.

Output: {“label”: “technical”}

Message: Please change the email address on my profile.

Output: {“label”: “account”}

Message: I cannot reset my password.

Output: ”

The desired continuation is a JSON object such as {"label": "account"}. In this example, the in-context demonstrations serve two roles: they identify the task and label space, and they teach the model an output format. More elaborate prompts can also demonstrate a workflow, such as first extracting relevant facts and then producing a final answer. In-context learning was popularized as a capability of large language models by Brown et al. [2020]; subsequent work studies what information the demonstrations provide, such as the input distribution, label space, and formatting conventions [Min et al., 2022], as well as how demonstrations of intermediate reasoning steps can improve some reasoning tasks [Wei et al., 2022].

## 17.7 Zero-shot learning / prompting

For autoregressive language models, the most lightweight form of adaptation is prompting: we change the text given to the model, but do not change the model parameters. The in-context learning examples in the previous section are one form of prompting. In the zero-shot setting, there are no inputoutput examples from the downstream task, so the prompt usually describes the task in natural language and asks the model to produce an answer in a specified format. For example, we may ask

$$
\begin{array}{r l} & {x _ {\mathrm{task}} = (x _ {\mathrm{task}, 1}, \dots , x _ {\mathrm{task}, T})} \\ & {\quad = \text {"Question: Is the speed of light a universal constant?}} \\ & {\qquad \text {Answer yes or no."}} \end{array}
$$

<!-- page: 219 -->

and then decode a continuation from $p _ { \theta } ( \cdot \mid x _ { \mathrm { t a s k } } )$ . If the model continues with “No,” it has produced the intended label for this prompt. More generally, the output may be decoded greedily, sampled, constrained to a set of labels, or parsed from a longer generated answer. Prompting is attractive because it requires no training data or gradient updates, but its performance can depend on the pretrained model and on the wording of the prompt.

## 17.8 Supervised Finetuning (SFT)

Finetuning instead adapts the model by updating parameters on downstream examples. For autoregressive language models, this usually does not require adding a new prediction head. We can format each supervised example as a prompt-completion pair $( x ^ { ( i ) } , y ^ { ( i ) } )$ , where $x ^ { ( i ) }$ consists of a sequence of tokens $x _ { 1 } ^ { ( i ) } , \ldots , x _ { L _ { i } } ^ { ( i ) } )$ and $y ^ { ( i ) }$ consists of a sequence of tokens $y _ { 1 } ^ { ( i ) } , \cdots , y _ { T _ { i } } ^ { ( i ) }$ We initialize $\theta$ at the pretrained parameters $\hat { \theta } ,$ and continue minimizing the conditional next-token loss

$$
\min _ {\theta} \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ - \sum_ {t = 1} ^ {T _ {i}} \log p _ {\theta} \Big (y _ {t} ^ {(i)} \mid x ^ {(i)}, y _ {<   t} ^ {(i)} \Big) \right].\tag{17.36}
$$

For a classification task, for instance, $y ^ { ( i ) }$ may simply be the text of the class label or a short JSON object containing the label. Here $x ^ { ( i ) }$ is the question, instruction (see paragraph below), or user prompt, while $y ^ { ( i ) }$ is the desired answer or assistant response. A common implementation concatenates the prompt and answer into one causal-LM sequence

$$
z ^ {(i)} = (x _ {1} ^ {(i)}, \dots , x _ {L _ {i}} ^ {(i)}, y _ {1} ^ {(i)}, \dots , y _ {T _ {i}} ^ {(i)}),
$$

but applies the next-token loss only to the answer positions. Equivalently, for a minibatch $B ,$ one uses a loss mask $m _ { r } ^ { ( i ) }$ with $m _ { r } ^ { ( \hat { i } ) } = 0$ on prompt tokens and $m _ { r } ^ { ( i ) } \; = \; 1$ on answer tokens, and minimizes the average loss over all answer-token positions in the minibatch,

$$
- \frac {1}{\sum_ {i \in \mathcal {B}} \sum_ {r = 1} ^ {L _ {i} + T _ {i}} m _ {r} ^ {(i)}} \sum_ {i \in \mathcal {B}} \sum_ {r = 1} ^ {L _ {i} + T _ {i}} m _ {r} ^ {(i)} \log p _ {\theta} \Big (z _ {r} ^ {(i)} \mid z _ {<   r} ^ {(i)} \Big).\tag{17.37}
$$

This loss mask is separate from the attention mask: the usual causal attention mask is still used, so answer tokens can attend to the prompt and to previous answer tokens, but the prompt tokens themselves do not contribute to the SFT objective.

<!-- page: 220 -->

Instruction tuning. Instruction tuning is an important special case of finetuning. Here an instruction means a natural-language task description, such as “summarize the following paragraph in one sentence,” “classify this customer message as billing, technical, or account-related,” or “write a Python function that sorts a list.” Instead of training on only one downstream task, we collect many tasks written as natural-language instructions with desired responses, and finetune the model on the resulting mixture [Wei et al., 2021, Ouyang et al., 2022]. The goal is not merely to fit those training tasks, but to teach the model the convention that an instruction in the prompt should be followed. This is why instruction-tuned models often become much better zero-shot assistants: at test time, the user can describe a new task in words, and the model has been trained to treat such descriptions as executable in structions.

<!-- page: 221 -->

## Chapter 18

## Reasoning in LLMs

## 18.1 Chain of thoughts

Motivation. Consider the grade-school arithmetic example where Roger starts with 5 tennis balls and buys 2 cans with 3 balls each. To solve it, we naturally do it in steps, compute the number of new balls first, and only then add them to the original 5 balls:

$$
z: \quad 2 \times 3 = 6, \qquad 5 + 6 = 1 1,
$$

so the final answer is $a = 1 1$

Typical prompts to LLMs will just ask the LLMs to solve the problem. Chain-of-thought (CoT) prompting instead asks the model to include the intermediate computation before giving the answer.

The motivation is that many reasoning tasks are easier to express as a short sequence of intermediate steps followed by an answer than as a single direct prediction. The reasoning trace gives the model more time to think (more compute), and more memory to log intermediate results. The extra tokens can be useful because the autoregressive model can condition later predictions on earlier partial computations, turning one hard prediction into a sequence of smaller predictions.

Few-shot CoT. In few-shot CoT, each in-context demonstration contains not only an input and answer, but also an intermediate natural-language solution. A prompt has the form

$$
(x ^ {(1)}, z ^ {(1)}, a ^ {(1)}), \dots , (x ^ {(m)}, z ^ {(m)}, a ^ {(m)}), x,
$$

<!-- page: 222 -->

and the model is expected to continue with a new trace z and answer a for the query x. This is the prompting version of asking the model to “show its work.” Wei et al. [2022] showed that, for sufficiently large pretrained language models, few-shot CoT substantially improves arithmetic, symbolic, and commonsense reasoning compared with standard few-shot prompts that contain only final answers.

Zero-shot CoT. Zero-shot CoT removes the hand-written demonstrations and instead uses a short instruction that encourages an intermediate trace. The canonical example is to append a phrase such as “Let’s think step by step” before asking for the answer [Kojima et al., 2022]. This is useful when writing high-quality few-shot rationales is expensive or when the same prompting template should transfer across many task types.

## 18.2 RLVR with long chain-of-thought reasoning

The previous section described chain-of-thought as an inference-time format: we prompt the model so that it writes intermediate steps before giving the answer. If this format makes prediction easier, it is natural to ask whether we can train models to produce useful reasoning traces, rather than only elicit them through prompting. The challenge is that high-quality step-by step supervision is expensive. In many domains, however, the final answer can be checked automatically: a math problem may have a known answer, a programming problem may have unit tests, a theorem-proving task may have a proof checker, and a structured-output task may have a deterministic validator.

Reinforcement learning with verifiable rewards (RLVR) trains exactly in this setting. The model samples a completion containing a chain of thought and a final answer, while an automatic verifier rewards the completion according to whether the final answer passes the check. This makes RLVR especially natural for long chain-of-thought reasoning, where it is difficult to supervise the whole trace but comparatively easy to verify the final result.

OpenAI’s o1 report showed that reasoning accuracy improves with both reinforcement-learning train-time compute and test-time thinking compute [OpenAI, 2024]. DeepSeek-R1 then gave a more detailed public recipe in which DeepSeek-R1-Zero improves during RLVR-style training and produces longer reasoning traces as training progresses [DeepSeek-AI, 2025]. This em-

<!-- page: 223 -->

pirical pattern is now often described as the scaling of reasoning models: performance is treated as depending not only on pretraining scale, but also on how much compute is spent to train and sample explicit reasoning traces. Figure 18.1 shows these two empirical scaling axes.

![](images/page_222_chart_2.jpg)

![](images/page_222_chart_3.jpg)

(a) OpenAI o1 scaling.

![](images/page_222_chart_5.jpg)

![](images/page_222_chart_6.jpg)

(b) DeepSeek-R1-Zero RL trajectory.

Figure 18.1: Two compute axes for reasoning models. The o1 report plots AIME pass@1 accuracy as a function of additional reinforcement-learning train-time compute and additional test-time compute. The DeepSeek-R1 report plots the corresponding RL training trajectory for DeepSeek-R1-Zero, where accuracy rises together with the average length of the model’s responses. Together, these plots motivate treating long chain-of-thought reasoning as both an inference-time resource and a trainable behavior. Sources: OpenAI [OpenAI, 2024] and DeepSeek-AI [DeepSeek-AI, 2025].

Formulation. Let $x \sim \mathcal { D }$ be a problem prompt, and $y   =   ( y _ { 1 } , \ldots , y _ { T } )$ be the response given $x ,$ which may contain both a chain of thought and a final answer. A verifier produces a scalar reward $R ( x , y )   \in   [ 0 , 1 ]$ . For instance, $R ( x , y ) = 1$ if the extracted final answer is correct and 0 otherwise, possibly with additional format penalties.

For a fixed prompt x, autoregressive generation can be viewed as a finitehorizon Markov Decision Process (MDP, see Chapter 21). At token position $t ,$ which is also the time step t in MDP, the state of the MDP is the prefix

$$
s _ {t} = (x, y _ {<   t}),
$$

the action is the next token $a _ { t } = y _ { t }$ , sampled from the policy, which is the next token probability

$$
\pi_ {\theta} (a _ {t} \mid s _ {t}) = p _ {\theta} (y _ {t} \mid x, y _ {<   t}).
$$

After choosing $y _ { t }$ , the transition is deterministic:

$$
s _ {t + 1} = (x, y _ {\leq t}).
$$

<!-- page: 224 -->

The episode ends when the model emits an end-of-sequence token or reaches a length limit. The verifier provides the terminal reward $R ( x , y )$ . Thus the only nonzero task reward is at the end of the generated completion. The reward objective is

$$
J _ {R} (\theta) = \mathbb {E} _ {x \sim \mathcal {D}, y \sim \pi_ {\theta} (\cdot | x)} \left[ R (x, y) \right].\tag{18.1}
$$

A common regularized objective subtracts a KL penalty from this reward to encourage the policy to not drift away from a reference policy by too far:

$$
J _ {\beta} (\theta) = J _ {R} (\theta) - \beta \mathbb {E} _ {x \sim \mathcal {D}} \left[ D _ {\mathrm{KL}} (\pi_ {\theta} (\cdot \mid x) \parallel \pi_ {\mathrm{ref}} (\cdot \mid x)) \right],\tag{18.2}
$$

and the training problem is to maximize $J _ { \beta } ( \theta )$ . Here $\pi _ { \mathrm { r e f } }$ is usually the initial supervised-finetuned or instruction-tuned model. The KL term discourages the policy from moving too far from a capable language model while the verifier reward pushes it toward completions that solve the task.

Rewards and verifiers. The simplest verifier extracts a final answer and compares it to a ground-truth answer. For code, the verifier may run unit tests; for symbolic tasks, it may call a parser, theorem checker, or algebra system. In practice, the reward usually also checks that the answer appears in the requested format.

Policy gradient. With the MDP formulation above, applying the policygradient identity from Chapter 21 to the reward term $( J _ { R }$ in (18.1)) gives

$$
\nabla_ {\theta} J _ {R} (\theta) = \mathbb {E} _ {x \sim \mathcal {D}, y \sim \pi_ {\theta} (\cdot | x)} \left[ \sum_ {t = 1} ^ {T} \left(R (x, y) - b _ {t}\right) \nabla_ {\theta} \log \pi_ {\theta} (y _ {t} \mid x, y _ {<   t}) \right],\tag{18.3}
$$

where $b _ { t }$ is a sequence-level baseline. Thus, if a sampled chain of thought obtains higher reward than the baseline, the update increases the probabilities of the tokens in that completion; if it obtains lower reward, the update decreases them.

PPO. The generic PPO update is described in Section 21.2. In the language-model MDP above, PPO is applied at token states

$$
s _ {t} ^ {(i)} = (x, y _ {<   t} ^ {(i)}), \qquad a _ {t} ^ {(i)} = y _ {t} ^ {(i)}.
$$

Suppose a batch of completions $y ^ { ( 1 ) } , \ldots , y ^ { ( G ) }$ has been sampled from the old policy $\pi _ { \theta _ { \mathrm { o l d } } } ( \cdot { \mathrm { ~ \left| ~ \right)} } x$ , where $y ^ { ( i ) }   =   ( y _ { 1 } ^ { ( i ) } , \ldots , y _ { T _ { i } } ^ { ( i ) } )$ . Below, $\mathbb { E } _ { i , t }$ denotes the

<!-- page: 225 -->

empirical average over sampled completions and token positions:

$$
\mathbb {E} _ {i, t} [ \cdot ] = \frac {1}{G} \sum_ {i = 1} ^ {G} \frac {1}{T _ {i}} \sum_ {t = 1} ^ {T _ {i}} [ \cdot ].
$$

When the minibatch contains several prompts, this notation also includes the empirical average over prompts. Define the token-level likelihood ratio

$$
r _ {t} ^ {(i)} (\theta) = \frac {\pi_ {\theta} (y _ {t} ^ {(i)} \mid x , y _ {<   t} ^ {(i)})}{\pi_ {\theta_ {\mathrm{old}}} (y _ {t} ^ {(i)} \mid x , y _ {<   t} ^ {(i)})}.\tag{18.4}
$$

Given token advantages $\hat { A } _ { t } ^ { ( i ) }$ , the token-level clipped surrogate is

$$
C _ {t} ^ {(i)} (\theta) = \min \left\{r _ {t} ^ {(i)} (\theta) \widehat {A} _ {t} ^ {(i)}, \operatorname{clip} _ {[ 1 - \epsilon_ {\mathrm{clip}}, 1 + \epsilon_ {\mathrm{clip}} ]} \left(r _ {t} ^ {(i)} (\theta)\right) \widehat {A} _ {t} ^ {(i)} \right\},\tag{18.5}
$$

and the corresponding token-level PPO objective is

$$
\widehat {J} _ {\mathrm{PPO}} ^ {\mathrm{LM}} (\theta) = \mathbb {E} _ {i, t} \Big [ C _ {t} ^ {(i)} (\theta) \Big ].\tag{18.6}
$$

The update maximizes $\widehat { J } _ { \mathrm { P P O } } ^ { \mathrm { L M } } ( \theta )$ . The clipping term prevents the new policy from assigning much larger or much smaller probability to any sampled token in a single update.

GRPO. Group Relative Policy Optimization $\left( \mathrm{GRPO} \right)$ , introduced in DeepSeekMath [Shao et al., 2024] and used in later reasoning-model training recipes such as DeepSeek-R1 [DeepSeek-AI, 2025], adapts the PPO template by replacing the learned value model with a group-relative baseline. For each prompt x, sample a group of G completions $\bar { y ^ { ( 1 ) } } , \ldots , y ^ { ( G ) }$ from the old policy $\pi _ { \theta _ { \mathrm { o l d } } } ( \cdot \mid x )$ and define $R _ { i }   =   R ( x , y ^ { ( i ) } )$ . The group statistics provide the sequence-level advantage:

$$
\widehat {A} _ {i} = \frac {R _ {i} - \overline {{R}}}{s _ {R} + \epsilon}, \qquad \overline {{R}} = \mathbb {E} _ {j} [ R _ {j} ], \qquad s _ {R} ^ {2} = \mathbb {E} _ {j} \left[ (R _ {j} - \overline {{R}}) ^ {2} \right],\tag{18.7}
$$

where $\mathbb { E } _ { j }$ denotes the empirical average over the G completions for the same prompt. GRPO sets $\widehat { A } _ { t } ^ { ( i ) } = \widehat { A } _ { i }$ for every token in completion i and applies PPO-style clipping at the token level:

$$
J _ {\mathrm{GRPO}} (\theta) = \mathbb {E} _ {i, t} \Big [ C _ {t} ^ {(i)} (\theta) \Big ],\tag{18.8}
$$

where $r _ { t } ^ { ( i ) }$ is defined in (18.4), and $C _ { t } ^ { ( i ) }$ is the clipped token surrogate in (18.5). The update maximizes $J _ { \mathrm { G R P O } } ( \theta )$ . The clipping expression is the same as in $\mathrm { P P O } ;$ the key difference is that GRPO obtains its advantages by comparing several answers to the same problem, rather than by training a separate critic.

<!-- page: 226 -->

CISPO. Clipped Importance Sampling Policy Optimization (CISPO), proposed in MiniMax-M1 [MiniMax, 2025], modifies this style of update for long reasoning chains. In PPO-style clipping, tokens with very large probability ratio changes can have their gradients suppressed by the clipped surrogate. A simplified CISPO-style token objective instead clips the importance weight used as a coefficient while still taking the gradient through the log-probability term:

$$
\mathcal {L} _ {\mathrm{CISPO}} = - \mathbb {E} _ {i, t} \left[ \operatorname{stopgrad} \left(\min \left\{r _ {t} ^ {(i)} (\theta), \epsilon_ {\text {high}} \right\}\right) \widehat {A} _ {i} \log \pi_ {\theta} \left(y _ {t} ^ {(i)} \mid x, y _ {<   t} ^ {(i)}\right) \right].\tag{18.9}
$$

Here $r _ { t } ^ { ( i ) } ( \theta )$ is defined in (18.4), and the expectation averages over sampled completions and token positions. CISPO clips the importance-sampling weight while preserving a direct log-probability gradient for each sampled token, using the same sequence-level advantage $\widehat { A } _ { i }$ as in GRPO.1

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>This is the one-sided CISPO version. The MiniMax-M1 paper also presents a twosided clipped-IS version that clips the importance weight between lower and upper bounds; see the original paper for those details. In their experiments, however, the authors did not impose the lower bound and tuned only the upper bound, so we introduce the one-sided version here for simplicity.</span></small>

<!-- page: 227 -->

Part VI

Reinforcement Learning and Control

<!-- page: 228 -->

## Chapter 19

## Reinforcement learning

We now begin our study of reinforcement learning and adaptive control.

In supervised learning, we saw algorithms that tried to make their outputs mimic the labels y given in the training set. In that setting, the labels gave an unambiguous “right answer” for each of the inputs x. In contrast, for many sequential decision making and control problems, it is very difficult to provide this type of explicit supervision to a learning algorithm. For example, if we have just built a four-legged robot and are trying to program it to walk, then initially we have no idea what the “correct” actions to take are to make it walk, and so do not know how to provide explicit supervision for a learning algorithm to try to mimic.

In the reinforcement learning framework, we will instead provide our al gorithms only a reward function, which indicates to the learning agent when it is doing well, and when it is doing poorly. In the four-legged walking example, the reward function might give the robot positive rewards for moving forwards, and negative rewards for either moving backwards or falling over. It will then be the learning algorithm’s job to figure out how to choose actions over time so as to obtain large rewards.

Reinforcement learning has been successful in applications as diverse as autonomous helicopter flight, robot legged locomotion, cell-phone network routing, marketing strategy selection, factory control, and efficient web-page indexing. Our study of reinforcement learning will begin with a definition of the Markov decision processes (MDP), which provides the formalism in which RL problems are usually posed.

<!-- page: 229 -->

## 19.1 Markov decision processes

A Markov decision process is a tuple $( S , A , \{ P _ { s a } \} , \gamma , R )$ , where:

• S is a set of states. (For example, in autonomous helicopter flight, S might be the set of all possible positions and orientations of the helicopter.)

• A is a set of actions. (For example, the set of all possible directions in which you can push the helicopter’s control sticks.)

$P _ { s a }$ are the state transition probabilities. For each state $s \in S$ and action $a \in A ,   P _ { s a }$ is a distribution over the state space. We’ll say more about this later, but briefly, $P _ { s a }$ gives the distribution over what states we will transition to if we take action a in state s.

$\gamma \in [ 0 , 1 )$ is called the discount factor.

$R : S \times A \mapsto \mathbb { R }$ is the reward function. (Rewards are sometimes also written as a function of a state $S$ only, in which case we would have $R : S \mapsto \mathbb { R } )$

The dynamics of an MDP proceeds as follows: We start in some state $s _ { 0 }$ and get to choose some action $a _ { 0 } \in A$ to take in the MDP. As a result of our choice, the state of the MDP randomly transitions to some successor state $s _ { 1 }$ , drawn according to $s _ { 1 } \sim P _ { s _ { 0 } a _ { 0 } }$ . Then, we get to pick another action $a _ { 1 }$ As a result of this action, the state transitions again, now to some $s _ { 2 } \sim P _ { s _ { 1 } a _ { 1 } } .$ We then pick $a _ { 2 }$ , and so on. . . . Pictorially, we can represent this process as follows:

$$
s _ {0} \xrightarrow {a _ {0}} s _ {1} \xrightarrow {a _ {1}} s _ {2} \xrightarrow {a _ {2}} s _ {3} \xrightarrow {a _ {3}} \dots
$$

Upon visiting the sequence of states $s _ { 0 } , s _ { 1 } , \ldots$ . with actions $a _ { 0 } , a _ { 1 } , \ldots ,$ our total payoff is given by

$$
R (s _ {0}, a _ {0}) + \gamma R (s _ {1}, a _ {1}) + \gamma^ {2} R (s _ {2}, a _ {2}) + \dots .
$$

Or, when we are writing rewards as a function of the states only, this becomes

$$
R (s _ {0}) + \gamma R (s _ {1}) + \gamma^ {2} R (s _ {2}) + \dots .
$$

For most of our development, we will use the simpler state-rewards $R ( s )$ though the generalization to state-action rewards $R ( s , a )$ offers no special difficulties.

<!-- page: 230 -->

Our goal in reinforcement learning is to choose actions over time so as to maximize the expected value of the total payoff:

$$
\mathrm{E} \left[ R (s _ {0}) + \gamma R (s _ {1}) + \gamma^ {2} R (s _ {2}) + \dots \right]
$$

Note that the reward at timestep t is discounted by a factor of $\gamma ^ { t }$ . Thus, to make this expectation large, we would like to accrue positive rewards as soon as possible (and postpone negative rewards as long as possible). In economic applications where $R ( \cdot )$ is the amount of money made, $\gamma$ also has a natural interpretation in terms of the interest rate (where a dollar today is worth more than a dollar tomorrow).

A policy is any function $\pi :   S   \mapsto   A$ mapping from the states to the actions. We say that we are executing some policy $$\pi$ $\mathrm { i f } _ { \mathrm { ; } }$$ whenever we are in state $s ,$ we take action $a = \pi ( s )$ . We also define the value function for a policy π according to

$$
V ^ {\pi} (s) = \mathrm{E} \left[ R (s _ {0}) + \gamma R (s _ {1}) + \gamma^ {2} R (s _ {2}) + \dots \mid s _ {0} = s, \pi \right].
$$

$V ^ { \pi } ( s )$ is simply the expected sum of discounted rewards upon starting in state $S _ { \gamma }$ and taking actions according to $\pi .$ 1

Given a fixed policy $\pi ,$ its value function $V ^ { \pi }$ satisfies the Bellman equations:

$$
V ^ {\pi} (s) = R (s) + \gamma \sum_ {s ^ {\prime} \in S} P _ {s \pi (s)} (s ^ {\prime}) V ^ {\pi} (s ^ {\prime}).
$$

This says that the expected sum of discounted rewards $V ^ { \pi } ( s )$ for starting in s consists of two terms: First, the immediate reward $R ( s )$ that we get right away simply for starting in state $\mathcal { S } _ { \gamma }$ and second, the expected sum of future discounted rewards. Examining the second term in more detail, we see that the summation term above can be rewritten $\operatorname { E } _ { s ^ { \prime } \sim P _ { s \pi ( s ) } } [ V ^ { \pi } ( s ^ { \prime } ) ]$ . This is the expected sum of discounted rewards for starting in state $s ^ { \prime } ,$ where $s ^ { \prime }$ is distributed according $P _ { s \pi ( s ) }$ , which is the distribution over where we will end up after taking the first action $\pi ( s )$ in the $\mathrm { M D P }$ from state s. Thus, the second term above gives the expected sum of discounted rewards obtained after the first step in the MDP.

Bellman’s equations can be used to efficiently solve for $V ^ { \pi }$ . Specifically, in a finite-state MDP $( | S | < \infty )$ , we can write down one such equation for $V ^ { \pi } ( s )$ for every state $\mathcal { S } .$ This gives us a set of |S| linear equations in |S| variables (the unknown $V ^ { \pi } ( s ) \mathrm { { ' s } }$ , one for each state), which can be efficiently solved for the $V ^ { \pi } ( s ) \mathrm { { ' s } }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">π</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">π</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>This notation in which we condition on  isn’t technically correct because  isn’t a random variable, but this is quite standard in the literature.</span></small>

<!-- page: 231 -->

We also define the optimal value function according to

$$
V ^ {*} (s) = \max _ {\pi} V ^ {\pi} (s).\tag{19.1}
$$

In other words, this is the best possible expected sum of discounted rewards that can be attained using any policy. There is also a version of Bellman’s equations for the optimal value function:

$$
V ^ {*} (s) = R (s) + \max _ {a \in A} \gamma \sum_ {s ^ {\prime} \in S} P _ {s a} (s ^ {\prime}) V ^ {*} (s ^ {\prime}).\tag{19.2}
$$

The first term above is the immediate reward as before. The second term is the maximum over all actions a of the expected future sum of discounted rewards we’ll get upon after action a. You should make sure you understand this equation and see why it makes sense.

We also define a policy $\pi ^ { * } : S \mapsto A$ as follows:

$$
\pi^ {*} (s) = \arg \max _ {a \in A} \sum_ {s ^ {\prime} \in S} P _ {s a} (s ^ {\prime}) V ^ {*} (s ^ {\prime}).\tag{19.3}
$$

Note that $\pi ^ { * } ( s )$ gives the action a that attains the maximum in the “max” in Equation (19.2).

It is a fact that for every state s and every policy $\pi ,$ we have

$$
V ^ {*} (s) = V ^ {\pi^ {*}} (s) \geq V ^ {\pi} (s).
$$

The first equality says that the $V ^ { \pi ^ { * } }$ , the value function for $\pi ^ { * }$ , is equal to the optimal value function $V ^ { * }$ for every state s. Further, the inequality above says that $\pi ^ { * } \mathrm { ^ { \prime } s }$ value is at least as large as the value of any other policy. In other words, $\pi ^ { * }$ as defined in Equation (19.3) is the optimal policy.

Note that $\pi ^ { * }$ has the interesting property that it is the optimal policy for all states s. Specifically, it is not the case that if we were starting in some state s then there’d be some optimal policy for that state, and if we were starting in some other state $s ^ { \prime }$ then there’d be some other policy that’s optimal policy for $s ^ { \prime } .$ The same policy $\pi ^ { * }$ attains the maximum in Equation (19.1) for all states s. This means that we can use the same policy $\pi ^ { * }$ no matter what the initial state of our MDP is.

## 19.2 Value iteration and policy iteration

We now describe two efficient algorithms for solving finite-state MDPs. For now, we will consider only MDPs with finite state and action spaces $( | S | <$

<!-- page: 232 -->

∞, $| A | < \infty )$ . In this section, we will also assume that we know the state transition probabilities $\{ P _ { s a } \}$ and the reward function $R .$

The first algorithm, value iteration, is as follows:

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4 Value Iteration
For each state $s$, initialize $V(s) := 0$.
for until convergence do
    For every state, update
$V(s) := R(s) + \max_{a \in A} \gamma \sum_{s'} P_{sa}(s') V(s').$ (19.4)
</div>

This algorithm can be thought of as repeatedly trying to update the estimated value function using Bellman Equations (19.2).

There are two possible ways of performing the updates in the inner loop of the algorithm. In the first, we can first compute the new values for $V ( s )$ for every state s, and then overwrite all the old values with the new values. This is called a synchronous update. In this case, the algorithm can be viewed as implementing a “Bellman backup operator” that takes a current estimate of the value function, and maps it to a new estimate. (See homework problem for details.) Alternatively, we can also perform asynchronous updates. Here, we would loop over the states (in some order), updating the values one at a time.

Under either synchronous or asynchronous updates, it can be shown that value iteration will cause V to converge to $V ^ { * }$ . Having found $V ^ { * }$ , we can then use Equation (19.3) to find the optimal policy.

Apart from value iteration, there is a second standard algorithm for finding an optimal policy for an MDP. The policy iteration algorithm proceeds as follows:

Thus, the inner-loop repeatedly computes the value function for the current policy, and then updates the policy using the current value function. (The policy π found in step (b) is also called the policy that is greedy with respect to V .) Note that step (a) can be done via solving Bellman’s equations as described earlier, which in the case of a fixed policy, is just a set of |S| linear equations in |S| variables.

After at most a finite number of iterations of this algorithm, V will converge to $V ^ { * }$ , and $\pi$ will converge to $\pi ^ { * } . ^ { 2 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2Note that value iteration cannot reach the exact Vin a finite number of iterations,</span></small>

<!-- page: 233 -->

```txt
Algorithm 5 Policy Iteration
Initialize π randomly.
for until convergence do
    Let V := V^π.          ▷ typically by linear system solver
    For each state s, let
        π(s) := arg max_{a∈A} ∑_{s'} P_sa(s')V(s').
```

Both value iteration and policy iteration are standard algorithms for solving MDPs, and there isn’t currently universal agreement over which algorithm is better. For small MDPs, policy iteration is often very fats and converges with very few iterations. However, for MDPs with large state spaces, solving for $V ^ { \pi }$ explicitly would involve solving a large system of linear equations, and could be difficult (and note that one has to solve the linear system multiple times in policy iteration). In these problems, value iteration may be preferred. For this reason, in practice value iteration seems to be used more often than policy iteration. For some more discussions on the comparison and connection of value iteration and policy iteration, please see Section 19.5.

## 19.3 Learning a model for an MDP

So far, we have discussed MDPs and algorithms for MDPs assuming that the state transition probabilities and rewards are known. In many realistic prob lems, we are not given state transition probabilities and rewards explicitly, but must instead estimate them from data. (Usually, S, A and $\gamma$ are known.)

For example, suppose that, for the inverted pendulum problem (see prob-

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∗</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">whereas policy iteration with an exact linear system solver, can. This is because when the actions space and policy space are discrete and finite, and once the policy reaches the optimal policy in policy iteration, then it will not change at all. On the other hand, even though value iteration will converge to the V, but there is always some non-zero error in the learned value function.</span></small>

<!-- page: 234 -->

lem set 4), we had a number of trials in the MDP, that proceeded as follows:

$$
\begin{array}{r l} & {s _ {0} ^ {(1)} \xrightarrow {a _ {0} ^ {(1)}} s _ {1} ^ {(1)} \xrightarrow {a _ {1} ^ {(1)}} s _ {2} ^ {(1)} \xrightarrow {a _ {2} ^ {(1)}} s _ {3} ^ {(1)} \xrightarrow {a _ {3} ^ {(1)}} \dots} \\ & {s _ {0} ^ {(2)} \xrightarrow {a _ {0} ^ {(2)}} s _ {1} ^ {(2)} \xrightarrow {a _ {1} ^ {(2)}} s _ {2} ^ {(2)} \xrightarrow {a _ {2} ^ {(2)}} s _ {3} ^ {(2)} \xrightarrow {a _ {3} ^ {(2)}} \dots} \end{array}
$$

Here, $s _ { i } ^ { ( j ) }$ is the state we were at time i of trial $j ,$ and $a _ { i } ^ { ( j ) }$ is the corresponding action that was taken from that state. In practice, each of the trials above might be run until the MDP terminates (such as if the pole falls over in the inverted pendulum problem), or it might be run for some large but finite number of timesteps.

Given this “experience” in the MDP consisting of a number of trials, we can then easily derive the maximum likelihood estimates for the state transition probabilities:

$$
P _ {s a} (s ^ {\prime}) = \frac {\# \text {times took we action a in state s and got to s ^{\prime}}}{\# \text {times we took action a in state s}}\tag{19.5}
$$

Or, if the ratio above is $`` 0/0 ''$ —corresponding to the case of never having taken action a in state s before—the we might simply estimate $P _ { s a } ( s ^ { \prime } )$ to be $1 / | S |$ . (I.e., estimate $P _ { s a }$ to be the uniform distribution over all states.)

Note that, if we gain more experience (observe more trials) in the MDP, there is an efficient way to update our estimated state transition probabilities using the new experience. Specifically, if we keep around the counts for both the numerator and denominator terms of (19.5), then as we observe more trials, we can simply keep accumulating those counts. Computing the ratio of these counts then given our estimate of $P _ { s a }$

Using a similar procedure, if R is unknown, we can also pick our estimate of the expected immediate reward $R ( s )$ in state s to be the average reward observed in state s.

Having learned a model for the MDP, we can then use either value iteration or policy iteration to solve the MDP using the estimated transition probabilities and rewards. For example, putting together model learning and value iteration, here is one possible algorithm for learning in an MDP with unknown state transition probabilities:

1. Initialize π randomly.

2. Repeat {

(a) Execute π in the MDP for some number of trials.

<!-- page: 235 -->

(b) Using the accumulated experience in the MDP, update our estimates for $P _ { s a }$ (and R, if applicable).

(c) Apply value iteration with the estimated state transition probabilities and rewards to get a new estimated value function $V$

(d) Update $\pi$ to be the greedy policy with respect to $V .$

We note that, for this particular algorithm, there is one simple optimization that can make it run much more quickly. Specifically, in the inner loop of the algorithm where we apply value iteration, if instead of initializing value iteration with $V = 0$ , we initialize it with the solution found during the pre vious iteration of our algorithm, then that will provide value iteration with a much better initial starting point and make it converge more quickly.

## 19.4 Continuous state MDPs

So far, we’ve focused our attention on MDPs with a finite number of states. We now discuss algorithms for MDPs that may have an infinite number of states. For example, for a car, we might represent the state as $( x , y , \theta , \dot { x } , \dot { y } , \dot { \theta } )$ comprising its position $( x , y )$ ; orientation $\theta ;$ velocity in the x and y directions $\dot { x }$ and $\dot{y};$ and angular velocity ${ \dot { \theta } } .$ Hence, $S = \mathbb { R } ^ { 6 }$ is an infinite set of states, because there is an infinite number of possible positions and orientations for the car.<sup>3</sup> Similarly, the inverted pendulum you saw in PS4 has states $( x , \theta , { \dot { x } } , { \dot { \theta } } )$ , where $\theta$ is the angle of the pole. And, a helicopter flying in 3d space has states of the form $( x , y , z , \phi , \theta , \psi , \dot { x } , \dot { y } , \dot { z } , \dot { \phi } , \dot { \theta } , \dot { \psi } )$ , where here the roll $\phi ,$ pitch $\theta ,$ and yaw ψ angles specify the 3d orientation of the helicopter.

In this section, we will consider settings where the state space is $S = \mathbb { R } ^ { d }$ and describe ways for solving such MDPs.

## 19.4.1 Discretization

Perhaps the simplest way to solve a continuous-state MDP is to discretize the state space, and then to use an algorithm like value iteration or policy iteration, as described previously.

For example, if we have 2d states $\left( s _ { 1 } , s _ { 2 } \right)$ , we can use a grid to discretize the state space:

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">θ  R;</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∈ [−π, π)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Technically, θ is an orientation and so the range of θ is better written θ than ∈ but for our purposes, this distinction is not important.</span></small>

<!-- page: 236 -->

[t]

![](images/page_235_chart_2.jpg)

[t]

Here, each grid cell represents a separate discrete state ¯s. We can then approximate the continuous-state MDP via a discrete-state one $( \bar { S } , A , \{ P _ { \bar { s } a } \} , \gamma , R )$ , where $\bar { S }$ is the set of discrete states, $\{ P _ { \overline { { s } } a } \}$ are our state transition probabilities over the discrete states, and so on. We can then use value iteration or policy iteration to solve for the $V ^ { * } ( \bar { s } )$ and $\pi ^ { * } ( \bar { s } )$ in the discrete state MDP $( \bar { S } , A , \{ P _ { \bar { s } a } \} , \gamma , R )$ . When our actual system is in some continuous-valued state $s \in S$ and we need to pick an action to execute, we compute the corresponding discretized state ${ \overline { { \bar { S } } } } ,$ and execute action $\pi ^ { * } ( \bar { s } )$

This discretization approach can work well for many problems. However, there are two downsides. First, it uses a fairly naive representation for $V ^ { * }$ $\left(  and  \pi^{*} \right)$ . Specifically, it assumes that the value function is takes a constant value over each of the discretization intervals (i.e., that the value function is piecewise constant in each of the gridcells).

To better understand the limitations of such a representation, consider a supervised learning problem of fitting a function to this dataset:

![](images/page_235_chart_7.jpg)

<!-- page: 237 -->

Clearly, linear regression would do fine on this problem. However, if we instead discretize the x-axis, and then use a representation that is piecewise constant in each of the discretization intervals, then our fit to the data would look like this:

![](images/page_236_chart_2.jpg)

This piecewise constant representation just isn’t a good representation for many smooth functions. It results in little smoothing over the inputs, and no generalization over the different grid cells. Using this sort of representation, we would also need a very fine discretization (very small grid cells) to get a good approximation.

A second downside of this representation is called the curse of dimensionality. Suppose $S = \mathbb { R } ^ { d }$ , and we discretize each of the d dimensions of the state into k values. Then the total number of discrete states we have is $k ^ { d }$ This grows exponentially quickly in the dimension of the state space $d ,$ and thus does not scale well to large problems. For example, with a 10d state, if we discretize each state variable into 100 values, we would have $1 0 0 ^ { 1 0 } = 1 0 ^ { 2 0 }$ discrete states, which is far too many to represent even on a modern desktop computer.

As a rule of thumb, discretization usually works extremely well for 1d and 2d problems (and has the advantage of being simple and quick to im plement). Perhaps with a little bit of cleverness and some care in choosing the discretization method, it often works well for problems with up to 4d states. If you’re extremely clever, and somewhat lucky, you may even get it to work for some 6d problems. But it very rarely works for problems any higher dimensional than that.

<!-- page: 238 -->

## 19.4.2 Value function approximation

We now describe an alternative method for finding policies in continuousstate MDPs, in which we approximate $V ^ { * }$ directly, without resorting to discretization. This approach, called value function approximation, has been successfully applied to many RL problems.

## Using a model or simulator

To develop a value function approximation algorithm, we will assume that we have a model, or simulator, for the MDP. Informally, a simulator is a black-box that takes as input any (continuous-valued) state $s _ { t }$ and action $a _ { t }$ , and outputs a next-state $s _ { t + 1 }$ sampled according to the state transition probabilities $P _ { s _ { t } a _ { t } }$

![](images/page_237_image_5.jpg)

There are several ways that one can get such a model. One is to use physics simulation. For example, the simulator for the inverted pendulum in PS4 was obtained by using the laws of physics to calculate what position and orientation the cart/pole will be in at time $t + 1$ , given the current state at time t and the action a taken, assuming that we know all the parameters of the system such as the length of the pole, the mass of the pole, and so on. Alternatively, one can also use an off-the-shelf physics simulation software package which takes as input a complete physical description of a mechanical system, the current state $s _ { t }$ and action $a _ { t } ,$ and computes the state $s _ { t + 1 }$ of the system a small fraction of a second into the future.<sup>4</sup>

An alternative way to get a model is to learn one from data collected in the MDP. For example, suppose we execute n trials in which we repeatedly take actions in an MDP, each trial for T timesteps. This can be done picking actions at random, executing some specific policy, or via some other way of

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>Open Dynamics Engine (http://www.ode.com) is one example of a free/open-source physics simulator that can be used to simulate systems like the inverted pendulum, and that has been a reasonably popular choice among RL researchers.</span></small>

<!-- page: 239 -->

choosing actions. We would then observe n state sequences like the following:

$$
\begin{array}{c} s _ {0} ^ {(1)} \xrightarrow {a _ {0} ^ {(1)}} s _ {1} ^ {(1)} \xrightarrow {a _ {1} ^ {(1)}} s _ {2} ^ {(1)} \xrightarrow {a _ {2} ^ {(1)}} \dots \xrightarrow {a _ {T - 1} ^ {(1)}} s _ {T} ^ {(1)} \\ s _ {0} ^ {(2)} \xrightarrow {a _ {0} ^ {(2)}} s _ {1} ^ {(2)} \xrightarrow {a _ {1} ^ {(2)}} s _ {2} ^ {(2)} \xrightarrow {a _ {2} ^ {(2)}} \dots \xrightarrow {a _ {T - 1} ^ {(2)}} s _ {T} ^ {(2)} \\ \dots \\ s _ {0} ^ {(n)} \xrightarrow {a _ {0} ^ {(n)}} s _ {1} ^ {(n)} \xrightarrow {a _ {1} ^ {(n)}} s _ {2} ^ {(n)} \xrightarrow {a _ {2} ^ {(n)}} \dots \xrightarrow {a _ {T - 1} ^ {(n)}} s _ {T} ^ {(n)} \end{array}
$$

We can then apply a learning algorithm to predict $s _ { t + 1 }$ as a function of $s _ { t }$ and $a _ { t }$

For example, one may choose to learn a linear model of the form

$$
s _ {t + 1} = A s _ {t} + B a _ {t},\tag{19.6}
$$

using an algorithm similar to linear regression. Here, the parameters of the model are the matrices A and B, and we can estimate them using the data collected from our n trials, by picking

$$
\arg \min _ {A, B} \sum_ {i = 1} ^ {n} \sum_ {t = 0} ^ {T - 1} \left\| s _ {t + 1} ^ {(i)} - \left(A s _ {t} ^ {(i)} + B a _ {t} ^ {(i)}\right) \right\| _ {2} ^ {2}.
$$

We could also potentially use other loss functions for learning the model. For example, it has been found in recent work Luo et al. [2018] that using $\| \cdot \| _ { 2 }$ norm (without the square) may be helpful in certain cases.

Having learned A and $B ,$ one option is to build a deterministic model, in which given an input $s _ { t }$ and $a _ { t } ,$ the output $s _ { t + 1 }$ is exactly determined. Specifically, we always compute $s _ { t + 1 }$ according to Equation (19.6). Alternatively, we may also build a stochastic model, in which $s _ { t + 1 }$ is a random function of the inputs, by modeling it as

$$
s _ {t + 1} = A s _ {t} + B a _ {t} + \epsilon_ {t},
$$

where here $\epsilon _ { t }$ is a noise term, usually modeled as $\epsilon _ { t } \sim \mathcal { N } ( 0 , \Sigma )$ . (The covariance matrix Σ can also be estimated from data in a straightforward way.)

Here, we’ve written the next-state $s _ { t + 1 }$ as a linear function of the current state and action; but of course, non-linear functions are also possible. Specifically, one can learn a model $s _ { t + 1 } = A \phi _ { s } ( s _ { t } ) + B \phi _ { a } ( a _ { t } )$ , where $\phi _ { s }$ and $\phi _ { a }$ are some non-linear feature mappings of the states and actions. Alternatively, one can also use non-linear learning algorithms, such as locally weighted linear regression, to learn to estimate $s _ { t + 1 }$ as a function of $s _ { t }$ and $a _ { t } .$ These approaches can also be used to build either deterministic or stochastic simulators of an MDP.

<!-- page: 240 -->

## Fitted value iteration

We now describe the fitted value iteration algorithm for approximating the value function of a continuous state MDP. In the sequel, we will assume that the problem has a continuous state space $S = \mathbb { R } ^ { d }$ , but that the action space A is small and discrete.<sup>5</sup>

Recall that in value iteration, we would like to perform the update

$$
V (s) := R (s) + \gamma \max _ {a} \int_ {s ^ {\prime}} P _ {s a} (s ^ {\prime}) V (s ^ {\prime}) d s ^ {\prime}\tag{19.7}
$$

$$
{ = } { R ( s ) + \gamma \operatorname* { m a x } _ { a } \mathrm{E} _ { s ^ { \prime } \sim P _ { s a } } [ V ( s ^ { \prime } ) ] }\tag{19.8}
$$

(In Section 19.2, we had written the value iteration update with a summation $\begin{array} { r } { V ( s ) : = R ( s ) + \gamma \operatorname* { m a x } _ { a } \sum _ { s ^ { \prime } } P _ { s a } ( s ^ { \prime } ) V ( s ^ { \prime } ) } \end{array}$ rather than an integral over states; the new notation reflects that we are now working in continuous states rather than discrete states.)

The main idea of fitted value iteration is that we are going to approximately carry out this step, over a finite sample of states $s ^ { ( 1 ) } , \ldots , s ^ { ( n ) }$ . Specifically, we will use a supervised learning algorithm—linear regression in our description below—to approximate the value function as a linear or non-linear function of the states:

$$
V (s) = \theta^ {T} \phi (s).
$$

Here, $\phi$ is some appropriate feature mapping of the states.

For each state s in our finite sample of n states, fitted value iteration will first compute a quantity $y ^ { ( i ) }$ , which will be our approximation to $R ( s ) +$ $\gamma \operatorname { m a x } _ { a } \operatorname { E } _ { s ^ { \prime } \sim P _ { s a } } [ V ( s ^ { \prime } ) ]$ (the right hand side of Equation 19.8). Then, it will apply a supervised learning algorithm to try to get $V ( s )$ close to $R ( s ) +$ γ maxa $\operatorname { E } _ { s ^ { \prime } \sim P _ { s a } } [ V ( s ^ { \prime } ) ]$ (or, in other words, to try to get V (s) close to $y ^ { ( i ) } )$

In detail, the algorithm is as follows:

1. Randomly sample n states $s ^ { ( 1 ) } , s ^ { ( 2 ) } , \ldots s ^ { ( n ) } \in S$

2. Initialize $\theta : = 0$

3. Repeat {

$$
\text {For} i = 1, \dots , n \left\{\right.
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>In practice, most MDPs have much smaller action spaces than state spaces. E.g., a car has a 6d state space, and a 2d action space (steering and velocity controls); the inverted pendulum has a 4d state space, and a 1d action space; a helicopter has a 12d state space, and a 4d action space. So, discretizing this set of actions is usually less of a problem than discretizing the state space would have been.</span></small>

<!-- page: 241 -->

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each action $a \in A$ {
    Sample $s_1', \ldots, s_k' \sim P_{s^{(i)}a}$ (using a model of the MDP).
    Set $q(a) = \frac{1}{k} \sum_{j=1}^k \left( R(s^{(i)}) + \gamma V(s_j') \right)$
    // Hence, $q(a)$ is an estimate of $R(s^{(i)}) + \gamma \mathrm{E}_{s' \sim P_{s^{(i)}a}}[V(s')]$.
}
Set $y^{(i)} = \max_a q(a)$.
    // Hence, $y^{(i)}$ is an estimate of $R(s^{(i)}) + \gamma \max_a \mathrm{E}_{s' \sim P_{s^{(i)}a}}[V(s')]$.
}
// In the original value iteration algorithm (over discrete states)
// we updated the value function according to $V(s^{(i)}) := y^{(i)}$.
// In this algorithm, we want $V(s^{(i)}) \approx y^{(i)}$, which we'll achieve
// using supervised learning (linear regression).
Set $\theta := \arg \min_\theta \frac{1}{2} \sum_{i=1}^n \left( \theta^T \phi(s^{(i)}) - y^{(i)} \right)^2$
</div>

Above, we had written out fitted value iteration using linear regression as the algorithm to try to make $V ( s ^ { ( i ) } )$ close to $y ^ { ( i ) }$ . That step of the algorithm is completely analogous to a standard supervised learning (regression) problem in which we have a training set $\left( x ^ { ( 1 ) } , y ^ { \widetilde { ( 1 ) } } \right) , \left( x ^ { ( 2 ) } , y ^ { ( 2 ) } \right) , \ldots , \widetilde { \left( x ^ { ( n ) } , y ^ { ( n ) } \right) }$ , and want to learn a function mapping from x to $y ;$ the only difference is that here s plays the role of x. Even though our description above used linear regression, clearly other regression algorithms (such as locally weighted linear regression) can also be used.

Unlike value iteration over a discrete set of states, fitted value iteration cannot be proved to always to converge. However, in practice, it often does converge (or approximately converge), and works well for many problems. Note also that if we are using a deterministic simulator/model of the MDP, then fitted value iteration can be simplified by setting $k = 1$ in the algorithm. This is because the expectation in Equation (19.8) becomes an expectation over a deterministic distribution, and so a single example is sufficient to exactly compute that expectation. Otherwise, in the algorithm above, we had to draw k samples, and average to try to approximate that expectation (see the definition of $q ( a )$ , in the algorithm pseudo-code).

<!-- page: 242 -->

Finally, fitted value iteration outputs $V ,$ which is an approximation to $V ^ { * }$ This implicitly defines our policy. Specifically, when our system is in some state $S _ { \gamma }$ and we need to choose an action, we would like to choose the action

$$
\arg \max _ {a} \mathrm{E} _ {s ^ {\prime} \sim P _ {s a}} [ V (s ^ {\prime}) ]\tag{19.9}
$$

The process for computing/approximating this is similar to the inner-loop of fitted value iteration, where for each action, we sample $s _ { 1 } ^ { \prime } , \ldots , s _ { k } ^ { \prime }   \sim   P _ { s a }$ to approximate the expectation. (And again, if the simulator is deterministic, we can set $k = 1 .$

In practice, there are often other ways to approximate this step as well. For example, one very common case is if the simulator is of the form $s _ { t + 1 } =$ $f ( s _ { t } , a _ { t } ) + \epsilon _ { t }$ , where f is some deterministic function of the states (such as $f ( s _ { t } , a _ { t } ) = A s _ { t } + B a _ { t } )$ , and  is zero-mean Gaussian noise. In this case, we can pick the action given by

$$
\arg \max _ {a} V (f (s, a)).
$$

In other words, here we are just setting $\epsilon _ { t }   =   0 \; \left( \mathrm { i . e . } \right.$ , ignoring the noise in the simulator), and setting $k   =   1$ . Equivalent, this can be derived from Equation (19.9) using the approximation

$$
\mathrm{E} _ {s ^ {\prime}} [ V (s ^ {\prime}) ] \approx V (\mathrm{E} _ {s ^ {\prime}} [ s ^ {\prime} ])\tag{19.10}
$$

$$
= V (f (s, a)),\tag{19.11}
$$

where here the expectation is over the random $s ^ { \prime } \sim P _ { s a }$ . So long as the noise terms $\epsilon _ { t }$ are small, this will usually be a reasonable approximation.

However, for problems that don’t lend themselves to such approximations, having to sample $k [ A ]$ states using the model, in order to approximate the expectation above, can be computationally expensive.

## 19.5 Connections between Policy and Value Iteration (Optional)

In the policy iteration, line 3 of Algorithm 5, we typically use linear system solver to compute $V ^ { \pi }$ . Alternatively, one can also the iterative Bellman updates, similarly to the value iteration, to evaluate $V ^ { \pi }$ , as in the Procedure $\mathrm { V E } ( \cdot )$ in Line 1 of Algorithm 6 below. Here if we take option 1 in Line 2 of the Procedure $\mathrm { V E } ,$ then the difference between the Procedure VE from the

<!-- page: 243 -->

```txt
Algorithm 6 Variant of Policy Iteration
procedure VE(π, k) ▷ To evaluate V^π
    Option 1: initialize V(s) := 0; Option 2: Initialize from the current V in the main algorithm.
    for i = 0 to k - 1 do
        For every state s, update
            V(s) := R(s) + γ ∑_{s'} P_{sπ(s)}(s')V(s'). (19.12)
        return V
Require: hyperparameter k.
Initialize π randomly.
for until convergence do
    Let V = VE(π, k).
    For each state s, let
        π(s) := arg max_{a∈A} ∑_{s'} P_{sa}(s')V(s'). (19.13)
```

<!-- page: 244 -->

value iteration (Algorithm 4) is that on line 4, the procedure is using the action from π instead of the greedy action.

Using the Procedure VE, we can build Algorithm 6, which is a variant of policy iteration that serves an intermediate algorithm that connects policy iteration and value iteration. Here we are going to use option 2 in VE to maximize the re-use of knowledge learned before. One can verify indeed that if we take $k = 1$ and use option 2 in Line 2 in Algorithm 6, then Algorithm 6 is semantically equivalent to value iteration (Algorithm 4). In other words, both Algorithm 6 and value iteration interleave the updates in (19.13) and (19.12). Algorithm 6 alternate between k steps of update (19.12) and one step of (19.13), whereas value iteration alternates between 1 steps of update (19.12) and one step of (19.13). Therefore generally Algorithm 6 should not be faster than value iteration, because assuming that update (19.12) and (19.13) are equally useful and time-consuming, then the optimal balance of the update frequencies could be just $k = 1$ or $k \approx 1$

On the other hand, if k steps of update (19.12) can be done much faster than k times a single step of (19.12), then taking additional steps of equation (19.12) in group might be useful. This is what policy iteration is leveraging — the linear system solver can give us the result of Procedure VE with $k = \infty$ much faster than using the Procedure VE for a large k. On the flip side, when such a speeding-up effect no longer exists, $^ { \mathrm { e . g . } , }$ when the state space is large and linear system solver is also not fast, then value iteration is more preferable.

<!-- page: 245 -->

## Chapter 20

## LQR, DDP and LQG

## 20.1 Finite-horizon MDPs

In Chapter 19, we defined Markov Decision Processes (MDPs) and covered Value Iteration / Policy Iteration in a simplified setting. More specifically we introduced the optimal Bellman equation that defines the optimal value function $V ^ { \pi ^ { * } }$ of the optimal policy $\pi ^ { * }$

$$
V ^ {\pi^ {*}} (s) = R (s) + \max _ {a \in \mathcal {A}} \gamma \sum_ {s ^ {\prime} \in S} P _ {s a} (s ^ {\prime}) V ^ {\pi^ {*}} (s ^ {\prime})
$$

Recall that from the optimal value function, we were able to recover the optimal policy $\pi ^ { * }$ with

$$
\pi^ {*} (s) = \operatorname{argmax} _ {a \in \mathcal {A}} \sum_ {s ^ {\prime} \in \mathcal {S}} P _ {s a} (s ^ {\prime}) V ^ {*} (s ^ {\prime})
$$

In this chapter, we’ll place ourselves in a more general setting:

1. We want to write equations that make sense for both the discrete and the continuous case. We’ll therefore write

$$
\begin{array}{r l} \mathbb {E} _ {s ^ {\prime} \sim P _ {s a}} \left[ V ^ {\pi^ {*}} (s ^ {\prime}) \right] & \quad \text {instead of} \\ \sum_ {s ^ {\prime} \in S} P _ {s a} (s ^ {\prime}) V ^ {\pi^ {*}} (s ^ {\prime}) \end{array}
$$

meaning that we take the expectation of the value function at the next state. In the finite case, we can rewrite the expectation as a sum over

<!-- page: 246 -->

states. In the continuous case, we can rewrite the expectation as an integral. The notation $s ^ { \prime } \sim P _ { s a }$ means that the state $s ^ { \prime }$ is sampled from the distribution $P _ { s a }$

2. We’ll assume that the rewards depend on both states and actions. In other words, $R : { \mathcal { S } } \times { \mathcal { A } } \to \mathbb { R }$ . This implies that the previous mechanism for computing the optimal action is changed into

$$
\pi^ {*} (s) = \operatorname{argmax} _ {a \in \mathcal {A}} R (s, a) + \gamma \mathbb {E} _ {s ^ {\prime} \sim P _ {s a}} \left[ V ^ {\pi^ {*}} (s ^ {\prime}) \right]
$$

3. Instead of considering an infinite horizon MDP, we’ll assume that we have a finite horizon MDP that will be defined as a tuple

$$
(\mathcal {S}, \mathcal {A}, P _ {s a}, T, R)
$$

with $T > 0$ the time horizon (for instance $T = 1 0 0 )$ . In this setting, our definition of payoff is going to be (slightly) different:

$$
R (s _ {0}, a _ {0}) + R (s _ {1}, a _ {1}) + \dots + R (s _ {T}, a _ {T})
$$

instead of (infinite horizon case)

$$
\begin{array}{l} R (s _ {0}, a _ {0}) + \gamma R (s _ {1}, a _ {1}) + \gamma^ {2} R (s _ {2}, a _ {2}) + \dots \\ \sum_ {t = 0} ^ {\infty} R (s _ {t}, a _ {t}) \gamma^ {t} \end{array}
$$

What happened to the discount factor $\gamma ^ { \ell }$ Remember that the introduction of $\gamma$ was (partly) justified by the necessity of making sure that the infinite sum would be finite and well-defined. If the rewards are bounded by a constant $\bar { R } ,$ the payoff is indeed bounded by

$$
| \sum_ {t = 0} ^ {\infty} R (s _ {t}) \gamma^ {t} | \leq \bar {R} \sum_ {t = 0} ^ {\infty} \gamma^ {t}
$$

and we recognize a geometric sum! Here, as the payoff is a finite sum, the discount factor $\gamma$ is not necessary anymore.

<!-- page: 247 -->

In this new setting, things behave quite differently. First, the optimal policy $\pi ^ { * }$ might be non-stationary, meaning that it changes over time. In other words, now we have

$$
\pi^ {(t)}: \mathcal {S} \to \mathcal {A}
$$

where the superscript (t) denotes the policy at time step t. The dynamics of the finite horizon MDP following policy $\pi ^ { ( t ) }$ proceeds as follows: we start in some state $s _ { 0 }$ , take some action $a _ { 0 } : = \pi ^ { ( 0 ) } ( s _ { 0 } )$ according to our policy at time step 0. The MDP transitions to a successor ${ \mathcal { S } } _ { 1 } ,$ drawn according to $P _ { s _ { 0 } a _ { 0 } }$ . Then, we get to pick another action $a _ { 1 } : = \pi ^ { ( 1 ) } ( s _ { 1 } )$ following our new policy at time step 1 and so on...

Why does the optimal policy happen to be non-stationary in the finitehorizon setting? Intuitively, as we have a finite numbers of actions to take, we might want to adopt different strategies depending on where we are in the environment and how much time we have left. Imagine a grid with 2 goals with rewards +1 and +10. At the beginning, we might want to take actions to aim for the +10 goal. But if after some steps, dynamics somehow pushed us closer to the +1 goal and we don’t have enough steps left to be able to reach the +10 goal, then a better strategy would be to aim for the +1 goal...

## 4. This observation allows us to use time dependent dynamics

$$
s _ {t + 1} \sim P _ {s _ {t}, a _ {t}} ^ {(t)}
$$

meaning that the transition’s distribution $P _ { s _ { t } , a _ { t } } ^ { ( t ) }$ changes over time. The same thing can be said about $R ^ { ( t ) }$ . Note that this setting is a better model for real life. In a car, the gas tank empties, traffic changes, etc. Combining the previous remarks, we’ll use the following general formulation for our finite horizon MDP

$$
\big (\mathcal {S}, \mathcal {A}, P _ {s a} ^ {(t)}, T, R ^ {(t)} \big)
$$

Remark: notice that the above formulation would be equivalent to adding the time into the state.

<!-- page: 248 -->

The value function at time t for a policy π is then defined in the same way as before, as an expectation over trajectories generated following policy $\pi$ starting in state s.

$$
V _ {t} (s) = \mathbb {E} \left[ R ^ {(t)} (s _ {t}, a _ {t}) + \dots + R ^ {(T)} (s _ {T}, a _ {T}) | s _ {t} = s, \pi \right]
$$

Now, the question is

In this finite-horizon setting, how do we find the optimal value function

$$
V _ {t} ^ {*} (s) = \max _ {\pi} V _ {t} ^ {\pi} (s)
$$

It turns out that Bellman’s equation for Value Iteration is made for Dynamic Programming. This may come as no surprise as Bellman is one of the fathers of dynamic programming and the Bellman equation is strongly related to the field. To understand how we can simplify the problem by adopting an iteration-based approach, we make the following observations:

1. Notice that at the end of the game (for time step $T )$ , the optimal value is obvious

$$
\forall s \in \mathcal {S}: V _ {T} ^ {*} (s) := \max _ {a \in \mathcal {A}} R ^ {(T)} (s, a)\tag{20.1}
$$

2. For another time step $0 \; \leq \; t \; < \; T$ , if we suppose that we know the optimal value function for the next time step $V _ { t + 1 } ^ { * }$ , then we have

$$
\forall t <   T, s \in \mathcal {S}: V _ {t} ^ {*} (s) := \max _ {a \in \mathcal {A}} \left[ R ^ {(t)} (s, a) + \mathbb {E} _ {s ^ {\prime} \sim P _ {s a} ^ {(t)}} \left[ V _ {t + 1} ^ {*} (s ^ {\prime}) \right] \right]\tag{20.2}
$$

With these observations in mind, we can come up with a clever algorithm to solve for the optimal value function:

1. compute $V _ { T } ^ { * }$ using equation (20.1).

2. for $t = T - 1 , \ldots , 0 { : }$

compute $V _ { t } ^ { * }$ using $V _ { t + 1 } ^ { * }$ using equation (20.2)

<!-- page: 249 -->

Side note We can interpret standard value iteration as a special case of this general case, but without keeping track of time. It turns out that in the standard setting, if we run value iteration for T steps, we get a $\gamma ^ { T }$ approximation of the optimal value iteration (geometric convergence). See problem set 4 for a proof of the following result:

<u>Theorem</u> Let B denote the Bellman update and $| | f ( x ) | | _ { \infty } : = \operatorname { s u p } _ { x } | f ( x ) |$ If $V _ { t }$ denotes the value function at the t-th step, then

$$
\begin{array}{r l} & {| | V _ {t + 1} - V ^ {*} | | _ {\infty} = | | B (V _ {t}) - V ^ {*} | | _ {\infty}} \\ & {\qquad \leq \gamma | | V _ {t} - V ^ {*} | | _ {\infty}} \\ & {\qquad \leq \gamma^ {t} | | V _ {1} - V ^ {*} | | _ {\infty}} \end{array}
$$

In other words, the Bellman operator B is a γ-contracting operator.

## 20.2 Linear Quadratic Regulation (LQR)

In this section, we’ll cover a special case of the finite-horizon setting described in Section 20.1, for which the exact solution is (easily) tractable. This model is widely used in robotics, and a common technique in many problems is to reduce the formulation to this framework.

First, let’s describe the model’s assumptions. We place ourselves in the continuous setting, with

$$
\mathcal {S} = \mathbb {R} ^ {d}, \mathcal {A} = \mathbb {R} ^ {d}
$$

and we’ll assume linear transitions (with noise)

$$
s _ {t + 1} = A _ {t} s _ {t} + B _ {t} a _ {t} + w _ {t}
$$

where $A _ { t } \in R ^ { d \times d } , B _ { t } \in R ^ { d \times d }$ are matrices and $w _ { t }   \sim   \mathcal { N } ( 0 , \Sigma _ { t } )$ is some gaussian noise (with zero mean). As we’ll show in the following paragraphs, it turns out that the noise, as long as it has zero mean, does not impact the optimal policy!

We’ll also assume quadratic rewards

$$
R ^ {(t)} (s _ {t}, a _ {t}) = - s _ {t} ^ {\top} U _ {t} s _ {t} - a _ {t} ^ {\top} W _ {t} a _ {t}
$$

<!-- page: 250 -->

where $U _ { t } \in R ^ { d \times n } , W _ { t } \in R ^ { d \times d }$ are positive definite matrices (meaning that the reward is always negative).

Remark Note that the quadratic formulation of the reward is equivalent to saying that we want our state to be close to the origin (where the reward is higher). For example, if $U _ { t } = I _ { d }$ (the identity matrix) and $W _ { t } = I _ { d }$ , then $R _ { t } = - | | s _ { t } | | ^ { 2 } - | | a _ { t } | | ^ { 2 }$ , meaning that we want to take smooth actions (small norm of $a _ { t } )$ to go back to the origin (small norm of $s _ { t } )$ . This could model a car trying to stay in the middle of lane without making impulsive moves...

Now that we have defined the assumptions of our LQR model, let’s cover the 2 steps of the LQR algorithm

step 1 suppose that we don’t know the matrices A, B, Σ. To estimate them, we can follow the ideas outlined in the Value Approximation section of the RL notes. First, collect transitions from an arbitrary policy. Then, use linear regression to find argmin $\begin{array} { r } { \iota _ { A , B } \sum _ { i = 1 } ^ { n } \sum _ { t = 0 } ^ { T - 1 } \left\| s _ { t + 1 } ^ { ( i ) } - \left( A s _ { t } ^ { ( i ) } + B a _ { t } ^ { ( i ) } \right) \right\| ^ { 2 } } \end{array}$ . Finally, use a technique seen in Gaussian Discriminant Analysis to learn Σ.

step 2 assuming that the parameters of our model are known (given or estimated with step 1), we can derive the optimal policy using dynamic programming.

In other words, given

$$
\left\{ \begin{array}{l l} s _ {t + 1} & = A _ {t} s _ {t} + B _ {t} a _ {t} + w _ {t} \quad A _ {t}, B _ {t}, U _ {t}, W _ {t}, \Sigma_ {t} \text {known} \\ R ^ {(t)} (s _ {t}, a _ {t}) & = - s _ {t} ^ {\top} U _ {t} s _ {t} - a _ {t} ^ {\top} W _ {t} a _ {t} \end{array} \right.
$$

we want to compute $V _ { t } ^ { * }$ . If we go back to section 20.1, we can apply dynamic programming, which yields

## 1. Initialization step

For the last time step $T ,$

$$
\begin{array}{r l r} V _ {T} ^ {*} (s _ {T}) & = \max _ {a _ {T} \in \mathcal {A}} R _ {T} (s _ {T}, a _ {T}) \\ & = \max _ {a _ {T} \in \mathcal {A}} - s _ {T} ^ {\top} U _ {T} s _ {T} - a _ {T} ^ {\top} W _ {t} a _ {T} \\ & = - s _ {T} ^ {\top} U _ {t} s _ {T} \qquad \text {(maximized for a_{T} = 0)} \end{array}
$$

<!-- page: 251 -->

## 2. Recurrence step

Let $t < T$ . Suppose we know $V _ { t + 1 } ^ { * }$

<u>Fact 1:</u> It can be shown that if $V _ { t + 1 } ^ { * }$ is a quadratic function in $\mathcal { S } _ { t } ,$ then $V _ { t } ^ { * }$ is also a quadratic function. In other words, there exists some matrix Φ and some scalar Ψ such that

$$
\begin{array}{l} \mathrm{if} V _ {t + 1} ^ {*} (s _ {t + 1}) = s _ {t + 1} ^ {\top} \Phi_ {t + 1} s _ {t + 1} + \Psi_ {t + 1} \\ \mathrm{then} V _ {t} ^ {*} (s _ {t}) = s _ {t} ^ {\top} \Phi_ {t} s _ {t} + \Psi_ {t} \end{array}
$$

For time step $t = T$ , we had $\Phi _ { t } = - U _ { T }$ and $\Psi _ { T } = 0$

<u>Fact 2:</u> We can show that the optimal policy is just a linear function of the state.

Knowing $V _ { t + 1 } ^ { * }$ is equivalent to knowing $\Phi _ { t + 1 }$ and $\Psi _ { t + 1 }$ , so we just need to explain how we compute $\Phi _ { t }$ and $\Psi _ { t }$ from $\Phi _ { t + 1 }$ and $\Psi _ { t + 1 }$ and the other parameters of the problem.

$$
\begin{array}{r l} & V _ {t} ^ {*} (s _ {t}) = s _ {t} ^ {\top} \Phi_ {t} s _ {t} + \Psi_ {t} \\ & \quad = \max _ {a _ {t}} \left[ R ^ {(t)} (s _ {t}, a _ {t}) + \mathbb {E} _ {s _ {t + 1} \sim P _ {s _ {t}, a _ {t}} ^ {(t)}} [ V _ {t + 1} ^ {*} (s _ {t + 1}) ] \right] \\ & \quad = \max _ {a _ {t}} \left[ - s _ {t} ^ {\top} U _ {t} s _ {t} - a _ {t} ^ {\top} V _ {t} a _ {t} + \mathbb {E} _ {s _ {t + 1} \sim \mathcal {N} (A _ {t} s _ {t} + B _ {t} a _ {t}, \Sigma_ {t})} [ s _ {t + 1} ^ {\top} \Phi_ {t + 1} s _ {t + 1} + \Psi_ {t + 1} ] \right] \end{array}
$$

where the second line is just the definition of the optimal value function and the third line is obtained by plugging in the dynamics of our model along with the quadratic assumption. Notice that the last expression is a quadratic function in $a _ { t }$ and can thus be (easily) optimized<sup>1</sup>. We get the optimal action $a _ { t } ^ { * }$

$$
\begin{array}{r} a _ {t} ^ {*} = \left[ (B _ {t} ^ {\top} \Phi_ {t + 1} B _ {t} - V _ {t}) ^ {- 1} B _ {t} \Phi_ {t + 1} A _ {t} \right] \cdot s _ {t} \\ = L _ {t} \cdot s _ {t} \end{array}
$$

where

$$
L _ {t} := \left[ (B _ {t} ^ {\top} \Phi_ {t + 1} B _ {t} - W _ {t}) ^ {- 1} B _ {t} \Phi_ {t + 1} A _ {t} \right]
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">-wt t+1wt = r( t t+1)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">w ∼ ( )</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Use the identity E>Φ  T Σ Φ with t  N 0, Σt</span></small>

<!-- page: 252 -->

which is an impressive result: our optimal policy is linear in $s _ { t }$ . Given $a _ { t } ^ { * }$ we can solve for $\Phi _ { t }$ and $\Psi _ { t }$ . We finally get the Discrete Ricatti equations

$$
\begin{array}{l} \Phi_ {t} = A _ {t} ^ {\top} \left(\Phi_ {t + 1} - \Phi_ {t + 1} B _ {t} \left(B _ {t} ^ {\top} \Phi_ {t + 1} B _ {t} - W _ {t}\right) ^ {- 1} B _ {t} \Phi_ {t + 1}\right) A _ {t} - U _ {t} \\ \Psi_ {t} = - \operatorname{tr} \left(\Sigma_ {t} \Phi_ {t + 1}\right) + \Psi_ {t + 1} \end{array}
$$

<u>Fact 3:</u> we notice that $\Phi _ { t }$ depends on neither $\Psi$ nor the noise $\Sigma _ { t } [$ As $L _ { t }$ is a function of $A _ { t } , B _ { t }$ and $\Phi _ { t + 1 }$ , it implies that the optimal policy also does not depend on the noise! (But $\Psi _ { t }$ does depend on $\Sigma _ { t }$ , which implies that $V _ { t } ^ { * }$ depends on $\Sigma _ { t \cdot } )$ 1

Then, to summarize, the LQR algorithm works as follows

1. (if necessary) estimate parameters $A _ { t } , B _ { t } , \Sigma _ { t }$

2. initialize $\Phi _ { T } : = - U _ { T }$ and $\Psi _ { T } : = 0$

3. iterate from $t = T - 1 \dots 0$ to update $\Phi _ { t }$ and $\Psi _ { t }$ using $\Phi _ { t + 1 }$ and $\Psi _ { t + 1 }$ using the discrete Ricatti equations. If there exists a policy that drives the state towards zero, then convergence is guaranteed!

Using <u>Fact 3</u>, we can be even more clever and make our algorithm run (slightly) faster! As the optimal policy does not depend on $\Psi _ { t } .$ , and the update of $\Phi _ { t }$ only depends on $\Phi _ { t } ,$ it is sufficient to update only $\Phi _ { t } [$

## 20.3 From non-linear dynamics to LQR

It turns out that a lot of problems can be reduced to LQR, even if dynamics are non-linear. While LQR is a nice formulation because we are able to come up with a nice exact solution, it is far from being general. Let’s take for instance the case of the inverted pendulum. The transitions between states look like

$$
\left( \begin{array}{c} x _ {t + 1} \\ \dot {x} _ {t + 1} \\ \theta_ {t + 1} \\ \dot {\theta} _ {t + 1} \end{array} \right) = F \left(\left( \begin{array}{c} x _ {t} \\ \dot {x} _ {t} \\ \theta_ {t} \\ \dot {\theta} _ {t} \end{array} \right), a _ {t}\right)
$$

where the function $F$ depends on the cos of the angle etc. Now, the question we may ask is

$$
\text {Can we linearize this system?}
$$

<!-- page: 253 -->

## 20.3.1 Linearization of dynamics

Let’s suppose that at time t, the system spends most of its time in some state $\bar { s } _ { t }$ and the actions we perform are around $\bar { a } _ { t }$ . For the inverted pendulum, if we reached some kind of optimal, this is true: our actions are small and we don’t deviate much from the vertical.

We are going to use Taylor expansion to linearize the dynamics. In the simple case where the state is one-dimensional and the transition function F does not depend on the action, we would write something like

$$
s _ {t + 1} = F (s _ {t}) \approx F (\bar {s} _ {t}) + F ^ {\prime} (\bar {s} _ {t}) \cdot (s _ {t} - \bar {s} _ {t})
$$

In the more general setting, the formula looks the same, with gradients instead of simple derivatives

$$
s _ {t + 1} \approx F (\bar {s} _ {t}, \bar {a} _ {t}) + \nabla_ {s} F (\bar {s} _ {t}, \bar {a} _ {t}) \cdot (s _ {t} - \bar {s} _ {t}) + \nabla_ {a} F (\bar {s} _ {t}, \bar {a} _ {t}) \cdot (a _ {t} - \bar {a} _ {t})\tag{20.3}
$$

and now, $s _ { t + 1 }$ is linear in $s _ { t }$ and $a _ { t }$ , because we can rewrite equation (20.3) as

$$
s _ {t + 1} \approx A s _ {t} + B a _ {t} + \kappa
$$

where $A = \nabla _ { s } F ( \bar { s _ { t } } , \bar { a _ { t } } ) , \: B = \nabla _ { a } F ( \bar { s _ { t } } , \bar { a _ { t } } )$ , and $\kappa = F ( \bar { s _ { t } } , \bar { a _ { t } } ) - A \bar { s _ { t } } - B \bar { a _ { t } }$ is a constant. Now, this writing looks awfully similar to the assumptions made for LQR. We just have to get rid of the constant term κ! It turns out that the constant term can be absorbed into $s _ { t }$ by artificially increasing the dimension by one. This is the same trick that we used at the beginning of the class for linear regression...

## 20.3.2 Differential Dynamic Programming (DDP)

The previous method works well for cases where the goal is to stay around some state $s ^ { * }$ (think about the inverted pendulum, or a car having to stay in the middle of a lane). However, in some cases, the goal can be more complicated.

We’ll cover a method that applies when our system has to follow some trajectory (think about a rocket). This method is going to discretize the trajectory into discrete time steps, and create intermediary goals around which we will be able to use the previous technique! This method is called Differential Dynamic Programming. The main steps are

<!-- page: 254 -->

step 1 come up with a nominal trajectory using a naive controller, that approximate the trajectory we want to follow. In other words, our controller is able to approximate the gold trajectory with

$$
s _ {0} ^ {*}, a _ {0} ^ {*} \to s _ {1} ^ {*}, a _ {1} ^ {*} \to \dots
$$

step 2 linearize the dynamics around each trajectory point $s _ { t } ^ { * }$ , in other words

$$
s _ {t + 1} \approx F (s _ {t} ^ {*}, a _ {t} ^ {*}) + \nabla_ {s} F (s _ {t} ^ {*}, a _ {t} ^ {*}) (s _ {t} - s _ {t} ^ {*}) + \nabla_ {a} F (s _ {t} ^ {*}, a _ {t} ^ {*}) (a _ {t} - a _ {t} ^ {*})
$$

where $s _ { t } , a _ { t }$ would be our current state and action. Now that we have a linear approximation around each of these points, we can use the previous section and rewrite

$$
s _ {t + 1} = A _ {t} \cdot s _ {t} + B _ {t} \cdot a _ {t}
$$

(notice that in that case, we use the non-stationary dynamics setting that we mentioned at the beginning of these lecture notes)

Note We can apply a similar derivation for the reward $R ^ { ( t ) }$ , with a second-order Taylor expansion.

$$
\begin{array}{r l} & R (s _ {t}, a _ {t}) \approx R (s _ {t} ^ {*}, a _ {t} ^ {*}) + \nabla_ {s} R (s _ {t} ^ {*}, a _ {t} ^ {*}) (s _ {t} - s _ {t} ^ {*}) + \nabla_ {a} R (s _ {t} ^ {*}, a _ {t} ^ {*}) (a _ {t} - a _ {t} ^ {*}) \\ & \qquad + \frac {1}{2} (s _ {t} - s _ {t} ^ {*}) ^ {\top} H _ {s s} (s _ {t} - s _ {t} ^ {*}) + (s _ {t} - s _ {t} ^ {*}) ^ {\top} H _ {s a} (a _ {t} - a _ {t} ^ {*}) \\ & \qquad + \frac {1}{2} (a _ {t} - a _ {t} ^ {*}) ^ {\top} H _ {a a} (a _ {t} - a _ {t} ^ {*}) \end{array}
$$

where $H _ { x y }$ refers to the entry of the Hessian of R with respect to x and y evaluated in $\left( s _ { t } ^ { * } , a _ { t } ^ { * } \right)$ (omitted for readability). This expression can be re-written as

$$
R _ {t} (s _ {t}, a _ {t}) = - s _ {t} ^ {\top} U _ {t} s _ {t} - a _ {t} ^ {\top} W _ {t} a _ {t}
$$

for some matrices $U _ { t } , W _ { t } ,$ with the same trick of adding an extra dimension of ones. To convince yourself, notice that

$$
\left( \begin{array}{c c} 1 & x \end{array} \right) \cdot \left( \begin{array}{c c} a & b \\ b & c \end{array} \right) \cdot \binom{1}{x} = a + 2 b x + c x ^ {2}
$$

<!-- page: 255 -->

step 3 Now, you can convince yourself that our problem is strictly re-written in the LQR framework. Let’s just use LQR to find the optimal policy $\pi _ { t }$ . As a result, our new controller will (hopefully) be better!

Note: Some problems might arise if the LQR trajectory deviates too much from the linearized approximation of the trajectory, but that can be fixed with reward-shaping...

step 4 Now that we get a new controller (our new policy $\pi _ { t } )$ , we use it to produce a new trajectory

$$
s _ {0} ^ {*}, \pi_ {0} (s _ {0} ^ {*}) \rightarrow s _ {1} ^ {*}, \pi_ {1} (s _ {1} ^ {*}) \rightarrow \dots \rightarrow s _ {T} ^ {*}
$$

note that when we generate this new trajectory, we use the real F and not its linear approximation to compute transitions, meaning that

$$
s _ {t + 1} ^ {*} = F (s _ {t} ^ {*}, a _ {t} ^ {*})
$$

then, $\mathtt { g O }$ back to step 2 and repeat until some stopping criterion.

## 20.4 Linear Quadratic Gaussian (LQG)

Often, in the real word, we don’t get to observe the full state $s _ { t }$ . For example, an autonomous car could receive an image from a camera, which is merely an observation, and not the full state of the world. So far, we assumed that the state was available. As this might not hold true for most of the real-world problems, we need a new tool to model this situation: Partially Observable MDPs.

A POMDP is an MDP with an extra observation layer. In other words, we introduce a new variable $o _ { t }$ , that follows some conditional distribution given the current state $s _ { t }$

$$
o _ {t} | s _ {t} \sim O (o | s)
$$

Formally, a finite-horizon POMDP is given by a tuple

$$
(\mathcal {S}, \mathcal {O}, \mathcal {A}, P _ {s a}, T, R)
$$

Within this framework, the general strategy is to maintain a belief state (distribution over states) based on the observation $o _ { 1 } , \ldots , o _ { t }$ . Then, a policy in a POMDP maps this belief states to actions.

<!-- page: 256 -->

In this section, we’ll present a extension of LQR to this new setting. Assume that we observe $y _ { t } \in \mathbb { R } ^ { n }$ with $m < n$ such that

$$
\left\{ \begin{array}{l l} y _ {t} & = C \cdot s _ {t} + v _ {t} \\ s _ {t + 1} & = A \cdot s _ {t} + B \cdot a _ {t} + w _ {t} \end{array} \right.
$$

where $C \in R ^ { n \times d }$ is a compression matrix and $v _ { t }$ is the sensor noise (also gaussian, like $w _ { t } )$ . Note that the reward function $R ^ { ( t ) }$ is left unchanged, as a function of the state (not the observation) and action. Also, as distributions are gaussian, the belief state is also going to be gaussian. In this new framework, let’s give an overview of the strategy we are going to adopt to find the optimal policy:

step 1 first, compute the distribution on the possible states (the belief state), based on the observations we have. In other words, we want to compute the mean $s _ { t | t }$ and the covariance $\Sigma _ { t | t }$ of

$$
s _ {t} | y _ {1}, \dots , y _ {t} \sim \mathcal {N} \left(s _ {t | t}, \Sigma_ {t | t}\right)
$$

to perform the computation efficiently over time, we’ll use the Kalman Filter algorithm (used on-board Apollo Lunar Module!).

step 2 now that we have the distribution, we’ll use the mean $s _ { t | t }$ as the best approximation for $s _ { t }$

step 3 then set the action $a _ { t } : = L _ { t } s _ { t | t }$ where $L _ { t }$ comes from the regular LQR algorithm.

Intuitively, to understand why this works, notice that $s _ { t | t }$ is a noisy approximation of $s _ { t }$ (equivalent to adding more noise to LQR) but we proved that LQR is independent of the noise!

Step 1 needs to be explicated. We’ll cover a simple case where there is no action dependence in our dynamics (but the general case follows the same idea). Suppose that

$$
\left\{ \begin{array}{l l} s _ {t + 1} & = A \cdot s _ {t} + w _ {t}, \quad w _ {t} \sim N (0, \Sigma_ {s}) \\ y _ {t} & = C \cdot s _ {t} + v _ {t}, \quad v _ {t} \sim N (0, \Sigma_ {y}) \end{array} \right.
$$

As noises are Gaussians, we can easily prove that the joint distribution is also Gaussian

<!-- page: 257 -->

$$
\left( \begin{array}{c} s _ {1} \\ \vdots \\ s _ {t} \\ y _ {1} \\ \vdots \\ y _ {t} \end{array} \right) \sim \mathcal {N} (\mu , \Sigma) \qquad \text {for some} \mu , \Sigma
$$

then, using the marginal formulas of gaussians (see Factor Analysis notes), we would get

$$
s _ {t} | y _ {1}, \dots , y _ {t} \sim \mathcal {N} \left(s _ {t | t}, \Sigma_ {t | t}\right)
$$

However, computing the marginal distribution parameters using these formulas would be computationally expensive! It would require manipulating matrices of shape $t \times t .$ . Recall that inverting a matrix can be done in $O ( t ^ { 3 } )$ and it would then have to be repeated over the time steps, yielding a cost in $O ( t ^ { 4 } ) !$

The Kalman filter algorithm provides a much better way of computing the mean and variance, by updating them over time in constant time in t! The kalman filter is based on two basics steps. Assume that we know the distribution of $s _ { t } | y _ { 1 } , \ldots , y _ { t } { : }$

predict step compute $s _ { t + 1 } | y _ { 1 } , \ldots , y _ { t }$

update step compute $s _ { t + 1 } | y _ { 1 } , \ldots , y _ { t + 1 }$

and iterate over time steps! The combination of the predict and update steps updates our belief states. In other words, the process looks like

$$
(s _ {t} | y _ {1}, \dots , y _ {t}) \xrightarrow {\text {predict}} (s _ {t + 1} | y _ {1}, \dots , y _ {t}) \xrightarrow {\text {update}} (s _ {t + 1} | y _ {1}, \dots , y _ {t + 1}) \xrightarrow {\text {predict}} \dots
$$

predict step Suppose that we know the distribution of

$$
s _ {t} | y _ {1}, \dots , y _ {t} \sim \mathcal {N} \left(s _ {t | t}, \Sigma_ {t | t}\right)
$$

then, the distribution over the next state is also a gaussian distribution

$$
s _ {t + 1} | y _ {1}, \dots , y _ {t} \sim \mathcal {N} \left(s _ {t + 1 | t}, \Sigma_ {t + 1 | t}\right)
$$

where

<!-- page: 258 -->

$$
\left\{ \begin{array}{l l} s _ {t + 1 | t} & = A \cdot s _ {t | t} \\ \Sigma_ {t + 1 | t} & = A \cdot \Sigma_ {t | t} \cdot A ^ {\top} + \Sigma_ {s} \end{array} \right.
$$

update step given $s _ { t + 1 | t }$ and $\Sigma _ { t + 1 | t }$ such that

$$
s _ {t + 1} | y _ {1}, \dots , y _ {t} \sim \mathcal {N} \left(s _ {t + 1 | t}, \Sigma_ {t + 1 | t}\right)
$$

we can prove that

$$
s _ {t + 1} | y _ {1}, \dots , y _ {t + 1} \sim \mathcal {N} \left(s _ {t + 1 | t + 1}, \Sigma_ {t + 1 | t + 1}\right)
$$

where

$$
\left\{ \begin{array}{l l} s _ {t + 1 | t + 1} & = s _ {t + 1 | t} + K _ {t} (y _ {t + 1} - C s _ {t + 1 | t}) \\ \Sigma_ {t + 1 | t + 1} & = \Sigma_ {t + 1 | t} - K _ {t} \cdot C \cdot \Sigma_ {t + 1 | t} \end{array} \right.
$$

with

$$
K _ {t} := \Sigma_ {t + 1 | t} C ^ {\top} (C \Sigma_ {t + 1 | t} C ^ {\top} + \Sigma_ {y}) ^ {- 1}
$$

The matrix $K _ { t }$ is called the Kalman gain.

Now, if we have a closer look at the formulas, we notice that we don’t need the observations prior to time step t! The update step only depends on the previous distribution. Putting it all together, the algorithm first runs a forward pass to compute the $K _ { t } , \Sigma _ { t | t }$ and $s _ { t | t }$ (sometimes referred to as ŝ in the literature). Then, it runs a backward pass (the LQR updates) to compute the quantities $\Phi _ { t } , \Psi _ { t }$ and $L _ { t }$ . Finally, we recover the optimal policy with $a _ { t } ^ { * } = L _ { t } s _ { t | t }$

<!-- page: 259 -->

# Chapter 21

# Policy Gradient and its Variants

## 21.1 REINFORCE

We will present a model-free algorithm called REINFORCE that does not require the notion of value functions and $Q$ functions. It turns out to be more convenient to introduce REINFORCE in the finite horizon case, which will be assumed throughout this note: we use $\tau = ( s _ { 0 } , a _ { 0 } , \ldots , s _ { T - 1 } , a _ { T - 1 } , s _ { T } )$ t o denote a trajectory, where $T < \infty$ is the length of the trajectory. Moreover, REINFORCE only applies to learning a randomized policy. We use $\pi _ { \theta } ( a | s )$ to denote the probability of the policy $\pi _ { \theta }$ outputting the action a at state s. The other notations will be the same as in previous lecture notes.

The advantage of applying REINFORCE is that we only need to assume that we can sample from the transition probabilities $\{ P _ { s a } \}$ and can query the reward function $R ( s , a )$ at state s and action ${ a _ { \cdot } } ^ { 1 }$ but we do not need to know the analytical form of the transition probabilities or the reward function. We do not explicitly learn the transition probabilities or the reward function either.

Let $s _ { 0 }$ be sampled from some distribution $\mu .$ We consider optimizing the expected total payoff of the policy $\pi _ { \theta }$ over the parameter θ defined as

$$
\eta (\theta) \triangleq \mathrm{E} \left[ \sum_ {t = 0} ^ {T - 1} \gamma^ {t} R (s _ {t}, a _ {t}) \right]\tag{21.1}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>In these notes we will work with the general setting where the reward depends on both the state and the action.</span></small>

<!-- page: 260 -->

Recall that $s _ { t } \enspace \sim \enspace P _ { s _ { t - 1 } a _ { t - 1 } }$ and $a _ { t } ~ \sim ~ \pi _ { \theta } ( \cdot | s _ { t } )$ Also note that $\eta ( \theta ) ~ =$ $\operatorname { E } _ { s _ { 0 } \sim \mu } \left[ V ^ { \pi _ { \theta } } ( s _ { 0 } ) \right]$ if we ignore the difference between finite and infinite horizon.

We aim to use gradient ascent to maximize $\eta ( \theta )$ . The main challenge we face here is to compute (or estimate) the gradient of $\eta ( \theta )$ without the knowledge of the form of the reward function and the transition probabilities.

Let $P _ { \theta } ( \tau )$ denote the distribution of $\tau$ (generated by the policy $\pi _ { \theta } \Big )$ , and let $f ( \tau ) = \widetilde { \textstyle \sum _ { t = 0 } ^ { T - 1 } \gamma ^ { t } R ( s _ { t } , a _ { t } ) }$ . We can rewrite $\eta ( \theta )$ as

$$
\eta (\theta) = \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ f (\tau) \right]\tag{21.2}
$$

We face a similar situation in the variational auto-encoder (VAE) setting covered in the previous lectures, where we need to take the gradient with respect to a variable that shows up under the expectation — the distribution $P _ { \theta }$ depends on $\theta .$ Recall that in VAEs, we used the reparameterization trick to address this problem. However, it does not apply here because we do not know how to compute the gradient of the function $f .$ (We only have an efficient way to evaluate the function $f$ by taking a weighted sum of the observed rewards, but we do not necessarily know the reward function itself to compute the gradient.)

The REINFORCE algorithm uses another approach to estimate the gradient of $\eta ( \theta )$ . We start with the following derivation:

$$
\begin{array}{r l} \nabla_ {\theta} \mathrm{E} _ {\tau \sim P _ {\theta}} [ f (\tau) ] & = \nabla_ {\theta} \int P _ {\theta} (\tau) f (\tau) d \tau \\ & = \int \nabla_ {\theta} (P _ {\theta} (\tau) f (\tau)) d \tau \quad \text {(swap integration with gradient)} \\ & = \int (\nabla_ {\theta} P _ {\theta} (\tau)) f (\tau) d \tau \quad \text {(because f does not depend on \theta)} \\ & = \int P _ {\theta} (\tau) (\nabla_ {\theta} \log P _ {\theta} (\tau)) f (\tau) d \tau \\ & \qquad \qquad \qquad \text {(because \nabla log P_{\theta} (\tau) = \frac {\nabla P_{\theta} (\tau)}{P_{\theta} (\tau)})} \\ & = \mathrm{E} _ {\tau \sim P _ {\theta}} [ (\nabla_ {\theta} \log P _ {\theta} (\tau)) f (\tau) ] \end{array} \tag {21.3}
$$

Now we have a sample-based estimator for $\nabla _ { \theta } \mathrm { E } _ { \tau \sim P _ { \theta } } \left[ f ( \tau ) \right]$ . Let $\tau ^ { ( 1 ) } , \ldots , \tau ^ { ( n ) }$ be n empirical samples from $P _ { \theta }$ (which are obtained by running the policy $\pi _ { \theta }$ for n times, with $T$ steps for each run). We can estimate the gradient of

<!-- page: 261 -->

η(θ) by

$$
\nabla_ {\theta} \mathrm{E} _ {\tau \sim P _ {\theta}} [ f (\tau) ] = \mathrm{E} _ {\tau \sim P _ {\theta}} [ (\nabla_ {\theta} \log P _ {\theta} (\tau)) f (\tau) ]\tag{21.4}
$$

$$
\approx \frac {1}{n} \sum_ {i = 1} ^ {n} (\nabla_ {\theta} \log P _ {\theta} (\tau^ {(i)})) f (\tau^ {(i)})\tag{21.5}
$$

The next question is how to compute log $P _ { \theta } ( \tau )$ . We derive an analytical formula for log $P _ { \theta } ( \tau )$ and compute its gradient with respect to $\theta$ (using autodifferentiation). Using the definition of $\tau ,$ we have

$$
P _ {\theta} (\tau) = \mu (s _ {0}) \pi_ {\theta} (a _ {0} | s _ {0}) P _ {s _ {0} a _ {0}} (s _ {1}) \pi_ {\theta} (a _ {1} | s _ {1}) P _ {s _ {1} a _ {1}} (s _ {2}) \dots P _ {s _ {T - 1} a _ {T - 1}} (s _ {T})\tag{21.6}
$$

Here recall that $\mu$ is used to denote the density of the distribution of $s _ { 0 }$ . It follows that

$$
\begin{array}{l} \log P _ {\theta} (\tau) = \log \mu (s _ {0}) + \log \pi_ {\theta} (a _ {0} | s _ {0}) + \log P _ {s _ {0} a _ {0}} (s _ {1}) + \log \pi_ {\theta} (a _ {1} | s _ {1}) \\ \quad + \log P _ {s _ {1} a _ {1}} (s _ {2}) + \dots + \log P _ {s _ {T - 1} a _ {T - 1}} (s _ {T}) \end{array}\tag{21.7}
$$

Taking the gradient with respect to $\theta ,$ we obtain

$$
\nabla_ {\theta} \log P _ {\theta} (\tau) = \nabla_ {\theta} \log \pi_ {\theta} (a _ {0} | s _ {0}) + \nabla_ {\theta} \log \pi_ {\theta} (a _ {1} | s _ {1}) + \dots + \nabla_ {\theta} \log \pi_ {\theta} (a _ {T - 1} | s _ {T - 1})
$$

Note that many of the terms disappear because they don’t depend on $\theta$ and thus have zero gradients. (This is somewhat important — we don’t know how to evaluate those terms such as log $P _ { s _ { 0 } a _ { 0 } } ( s _ { 1 } )$ because we don’t have access to the transition probabilities, but luckily those terms have zero gradients!)

Plugging the equation above into equation (21.4), we conclude that

$$
\begin{array}{r l} \nabla_ {\theta} \eta (\theta) = \nabla_ {\theta} \mathrm{E} _ {\tau \sim P _ {\theta}} [ f (\tau) ] & = \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \left(\sum_ {t = 0} ^ {T - 1} \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t})\right) \cdot f (\tau) \right] \\ & = \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \left(\sum_ {t = 0} ^ {T - 1} \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t})\right) \cdot \left(\sum_ {t = 0} ^ {T - 1} \gamma^ {t} R (s _ {t}, a _ {t})\right) \right] \end{array}\tag{21.8}
$$

We estimate the RHS of the equation above by empirical sample trajectories, and the estimate is unbiased. The vanilla REINFORCE algorithm iteratively updates the parameter by gradient ascent using the estimated gradients.

<!-- page: 262 -->

Interpretation of the policy gradient formula (21.8). The quantity $\begin{array} { r } { \nabla _ { \theta } \log P _ { \theta } ( \tau ) = \sum _ { t = 0 } ^ { T - 1 } \nabla _ { \theta } \log \pi _ { \theta } ( a _ { t } | s _ { t } ) } \end{array}$ is the score of the trajectory. It points in the direction of parameter change that locally increases the log-probability, and hence the probability, of the trajectory $\tau$ (or of choosing the actions $a _ { 0 } , \ldots , a _ { T - 1 }$ along that trajectory). The scalar $f ( \tau )$ is the total payoff of this trajectory. Thus, by taking a gradient step, intuitively we are trying to increase the likelihood of sampled trajectories, but with a different emphasis or weight for each $\tau . \quad \mathrm { I f } \quad \tau$ is very rewarding, then $f ( \tau )$ is large and the update strongly reinforces the direction that increases the probability of that trajectory; if τ has low payoff, the same direction receives a smaller weight.

An interesting fact that follows from formula (21.3) is that

$$
\mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \sum_ {t = 0} ^ {T - 1} \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \right] = 0\tag{21.9}
$$

To see this, we take $f ( \tau )   =   1$ (that is, the reward is always a constant), then the LHS of (21.8) is zero because the payoff is always a fixed constant $\textstyle \sum _ { t = 0 } ^ { T } \boldsymbol { \gamma } ^ { t }$ . Thus the RHS of (21.8) is also zero, which implies (21.9).

In fact, one can verify that $\operatorname { E } _ { a _ { t } \sim \pi _ { \theta } ( \cdot | s _ { t } ) } \nabla _ { \theta }$ log $\pi _ { \theta } ( a _ { t } | s _ { t } ) = 0$ for any fixed t and ${ s _ { t } } . ^ { 2 }$ This fact has two consequences. First, we can simplify formula (21.8) to

$$
\begin{array}{r} \nabla_ {\theta} \eta (\theta) = \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot \left(\sum_ {j = 0} ^ {T - 1} \gamma^ {j} R (s _ {j}, a _ {j})\right) \right] \\ = \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot \left(\sum_ {j \geq t} ^ {T - 1} \gamma^ {j} R (s _ {j}, a _ {j})\right) \right] \end{array}\tag{21.10}
$$

where the second equality follows from

$$
\begin{array}{l} \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot \left(\sum_ {0 \leq j <   t} \gamma^ {j} R (s _ {j}, a _ {j})\right) \right] \\ = \mathrm{E} \left[ \mathrm{E} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) | s _ {0}, a _ {0}, \dots , s _ {t - 1}, a _ {t - 1}, s _ {t} \right] \cdot \left(\sum_ {0 \leq j <   t} \gamma^ {j} R (s _ {j}, a _ {j})\right) \right] \\ = 0 \qquad \qquad (\text {because E} [ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) | s _ {0}, a _ {0}, \dots , s _ {t - 1}, a _ {t - 1}, s _ {t} ] = 0) \end{array}
$$

Note that here we used the law of total expectation. The outer expectation in the second line above is over the randomness of $s _ { 0 } , a _ { 0 } , \ldots , a _ { t - 1 } , s _ { t }$ ,

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">x∼ [ og pθ(x)] =</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2In general, it’s true that E pθ ∇ l 0.</span></small>

<!-- page: 263 -->

whereas the inner expectation is over the randomness of $a _ { t }$ (conditioned on $s _ { 0 } , a _ { 0 } , \ldots , a _ { t - 1 } , s _ { t } . )$ We see that we’ve made the estimator slightly simpler. The second consequence of $\operatorname { E } _ { a _ { t } \sim \pi _ { \theta } ( \cdot | s _ { t } ) } \nabla _ { \theta }$ log $\pi _ { \theta } ( a _ { t } | s _ { t } ) = 0$ is the following: for any value $B ( s _ { t } )$ that only depends on $\mathcal { S } _ { t } .$ , it holds that

$$
\begin{array}{r l} & {\mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot B (s _ {t}) \right]} \\ & {= \mathrm{E} \left[ \mathrm{E} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) | s _ {0}, a _ {0}, \dots , s _ {t - 1}, a _ {t - 1}, s _ {t} \right] B (s _ {t}) \right]} \\ & {= 0 \qquad (\mathrm{because} \mathrm{E} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) | s _ {0}, a _ {0}, \dots , s _ {t - 1}, a _ {t - 1}, s _ {t} \right] = 0)} \end{array}
$$

Again here we used the law of total expectation. The outer expectation in the second line above is over the randomness of $s _ { 0 } , a _ { 0 } , \ldots , a _ { t - 1 } , s _ { t }$ whereas the inner expectation is over the randomness of $a _ { t }$ (conditioned on $s _ { 0 } , a _ { 0 } , \ldots , a _ { t - 1 } , s _ { t } . )$ It follows from equation (21.10) and the equation above that

$$
\begin{array}{r l} & {\nabla_ {\theta} \eta (\theta) = \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot \left(\sum_ {j \geq t} ^ {T - 1} \gamma^ {j} R (s _ {j}, a _ {j}) - \gamma^ {t} B (s _ {t})\right) \right]} \\ & {\quad = \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \nabla_ {\theta} \log \pi_ {\theta} (a _ {t} | s _ {t}) \cdot \gamma^ {t} \left(\sum_ {j \geq t} ^ {T - 1} \gamma^ {j - t} R (s _ {j}, a _ {j}) - B (s _ {t})\right) \right]} \end{array}\tag{21.11}
$$

Therefore, we will get a different estimator for estimating the $\nabla \eta ( \theta )$ with a different choice of $B ( \cdot )$ . The benefit of introducing a proper B(·) — which is often referred to as a baseline — is that it helps reduce the variance of the estimator.<sup>3</sup>It turns out that a near optimal estimator would be the expected future payoff E $\begin{array} { r } { \left[ \sum _ { j \geq t } ^ { T - 1 } \gamma ^ { j - t } R ( s _ { j } , a _ { j } ) | s _ { t } \right] } \end{array}$ , which is pretty much the same as the value function $\bar { V } ^ { \pi _ { \theta } } ( s _ { t } )$ (if we ignore the difference between finite and infinite horizon.) Here one could estimate the value function $V ^ { \pi _ { \theta } } ( \cdot )$ in a crude way, because its precise value doesn’t influence the mean of the estimator but only the variance. This leads to a policy gradient algorithm with baselines stated in Algorithm $7 . ^ { 4 }$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">∑j≥t j≥t T −1 j−tR</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1000 1</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1000 2</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">θ og πθ(at|st)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">E ∇θ log πθ at st 0</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">θ og πθ(at|st)</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>As a heuristic but illustrating example, suppose for a fixed t, the future reward Pγ(sj , aj ) randomly takes two values  +  and  −  with equal probability, and the corresponding values for ∇ l are vector z and −z. (Note that because [ ( | )] = , if ∇ l can only take two values uniformly, then the two values have to be two vectors in opposite directions.) In this case, without subtracting the baseline, the estimators take two values ( + )z an −( − )z, 1000  1 d 1000  2 whereas after subtracting a baseline of 1000, the estimator has two values z and 2z. The</span></small>

<!-- page: 264 -->

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 7 Vanilla policy gradient with baseline
for $i = 1, \cdots$ do
    Collect a set of trajectories by executing the current policy. Use $R_{\geq t}$ as a shorthand for $\sum_{j \geq t}^{T-1} \gamma^{j-t} R(s_j, a_j)$
    Fit the baseline by finding a function $B$ that minimizes
    $\sum_{\tau} \sum_{t} (R_{\geq t} - B(s_t))^2$ (21.12)
    Update the policy parameter $\theta$ with the gradient estimator
    $\sum_{\tau} \sum_{t} \nabla_{\theta} \log \pi_{\theta}(a_t | s_t) \cdot (R_{\geq t} - B(s_t))$ (21.13)
</div>

## 21.2 PPO

The vanilla policy-gradient algorithm above is on-policy: the trajectories used in the gradient estimator are sampled from the same policy that we are about to update. This can be data-inefficient because we can literally only do one gradient update every time we sample a number of trajectories (because after that the trajectories are sampled from an older policy). This can cause inefficiency because oftentimes sampling trajectories is expensive, and switching between sampling and gradient updates is also expensive, and thus we might want to learn more — do many updates given a fixed set of sampled trajectories.

Proximal Policy Optimization (PPO) [Schulman et al., 2017] is a modified version of the vanilla policy gradient that allows some degree of off-policy updates, that is, reusing trajectories sampled from a recent old policy for several gradient steps.

First, start from the original finite-horizon reward objective

$$
\eta (\theta) = \mathrm{E} _ {\tau \sim P _ {\theta}} \left[ \sum_ {t = 0} ^ {T - 1} \gamma^ {t} R (s _ {t}, a _ {t}) \right].\tag{21.14}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">t</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">latter estimator has much lower variance compared to the original estimator.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>4</sup>We note that the estimator of the gradient in the algorithm does not exactly match the equation 21.11. If we multiply γ in the summand of equation (21.13), then they will exactly match. Removing such discount factors empirically works well because it gives a large update.</span></small>

<!-- page: 265 -->

A convenient way to separate the ideas in PPO is to first ignore baselines and advantages, and focus only on how to reuse data sampled from an old policy. Let $\theta _ { \mathrm { o l d } }$ be the parameter that generated the sampled trajectories. For a generic sampled trajectory $\tau { = } \left( s _ { 0 } , a _ { 0 } , \ldots , s _ { T - 1 } , a _ { T - 1 } , s _ { T } \right)$ , define the reward-to-go by $\begin{array} { r } { \dot { R _ { \geq t } } = \sum _ { j = t } ^ { \dot { T } - 1 } \dot { \gamma ^ { j - t } } R ( s _ { j } , \dot { a _ { j } } ) } \end{array}$

Suppose we have taken a few gradient updates and arrived at a policy θ that is not far from $\theta _ { \mathrm { o l d } }$ . We would like to estimate an update for the policy $\pi _ { \theta }$ using trajectories sampled from $\pi _ { \theta _ { \mathrm { o l d } } }$ . In the policy-gradient estimator, each time step contributes a reward-to-go term. If the state $s _ { t }$ were fixed, then the basic correction for changing the action distribution from $\pi _ { \theta _ { \mathrm { o l d } } }$ to $\pi _ { \theta }$ is the likelihood ratio

$$
r _ {t} (\theta) = \frac {\pi_ {\theta} (a _ {t} | s _ {t})}{\pi_ {\theta_ {\mathrm{old}}} (a _ {t} | s _ {t})}.\tag{21.15}
$$

Let $d _ { \theta _ { \mathrm { o l d } } , t }$ denote the distribution of $s _ { t }$ under the old policy. The corresponding importance-weighted local surrogate has the form

$$
\mathcal {J} _ {\mathrm{IS}} (\theta) = \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {s _ {t} \sim d _ {\theta_ {\mathrm{old}}, t}} \mathrm{E} _ {a _ {t} \sim \pi_ {\theta_ {\mathrm{old}}} (\cdot | s _ {t})} \left[ r _ {t} (\theta) R _ {\geq t} \right].\tag{21.16}
$$

Here the outer expectation is still over states visited by the old policy, while the likelihood ratio converts the inner action expectation from $\pi _ { \theta _ { \mathrm { o l d } } }$ to πθ. Thus this expression should be viewed as a local surrogate: it corrects the sampled actions, but it still uses the state distribution and rollouts generated by the old policy.

A simple importance-sampling-based gradient algorithm would collect trajectories under $\pi _ { \theta _ { \mathrm { o l d } } } ,$ , compute the reward-to-go, and then take several gradient steps on the local objective (21.16). PPO starts from this local surrogate and adds two changes. First, it replaces the raw reward-to-go by subtracting a value-function baseline, turning it into an advantage estimate with lower variance, and adds a KL-divergence regularizer, as in (18.2), to penalize drift from the old policy. Second, it clips the likelihood ratio so that if θ has drifted too far from the old policy on a sampled action, the update does not keep increasing the incentive to move farther in that direction.

Recall that subtracting a state-dependent baseline from the reward-to-go does not change the expected policy-gradient direction, but it can reduce the variance of the estimator. In particular, we can subtract an approximated value-function baseline under the old policy and use the advantage estimate

$$
\widehat {A} _ {t} = R _ {\geq t} - V _ {\mathrm{old}} (s _ {t}).
$$

<!-- page: 266 -->

This gives the advantage-based loss

$$
\mathcal {J} _ {\mathrm{adv}} (\theta) = - \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {s _ {t} \sim d _ {\theta_ {\mathrm{old}}, t}} \mathrm{E} _ {a _ {t} \sim \pi_ {\theta_ {\mathrm{old}}} (\cdot | s _ {t})} \left[ r _ {t} (\theta) \widehat {A} _ {t} \right],\tag{21.17}
$$

which has the same importance-weighted structure as (21.16), but with $R _ { \geq t }$ replaced by $\widehat { A } _ { t }$ . PPO then clips the per-time-step contribution by replacing $r _ { t } ( \theta ) \widehat { A } _ { t }$ with

$$
C _ {t} (\theta) = \min \left\{r _ {t} (\theta) \widehat {A} _ {t}, \operatorname{clip} _ {[ 1 - \epsilon_ {\mathrm{clip}}, 1 + \epsilon_ {\mathrm{clip}} ]} (r _ {t} (\theta)) \widehat {A} _ {t} \right\}.\tag{21.18}
$$

And the PPO surrogate loss is then

$$
\mathcal {J} _ {\mathrm{PPO}} (\theta) = - \sum_ {t = 0} ^ {T - 1} \mathrm{E} _ {s _ {t} \sim d _ {\theta_ {\mathrm{old}}, t}} \mathrm{E} _ {a _ {t} \sim \pi_ {\theta_ {\mathrm{old}}} (\cdot | s _ {t})} \left[ C _ {t} (\theta) \right],\tag{21.19}
$$

Here the min operator can be understood by considering the sign of the advantage. If $\widehat { \boldsymbol { A } _ { t } } > 0$ , then the sampled action leads to a reward-to-go that is better than the baseline, so the update would like to increase the probability of that action. When $r _ { t } ( \theta )   \leq   1 + \epsilon _ { \mathrm { c l i p } } ,$ PPO uses the ordinary contribution $r _ { t } ( \theta ) \widehat { A } _ { t } ;$ when $r _ { t } ( \theta ) > 1 + \epsilon _ { \mathrm { c l i p } } ,$ the clipped term caps the gain at $( 1 + \epsilon _ { \mathrm { c l i p } } ) \widehat { A } _ { t } ,$ so the objective stops rewarding further increases in that action probability; this makes sense because the probability of the action under the current policy is already substantially higher than the probability under $\pi _ { \theta _ { \mathrm { o l d } } }$ , so further increasing it is unnecessary.

On the other hand, if $\hat { A } _ { t } < 0$ , then the sampled action leads to a rewardto-go that is worse than the baseline, so the update would like to decrease the probability of that action. When $r _ { t } ( \theta ) \; \geq \; 1   -   \epsilon _ { \mathrm { c l i p } }$ , PPO again uses the ordinary contribution; when $r _ { t } ( \theta ) \; < \; 1   -   \epsilon _ { \mathrm { c l i p } } ,$ the clipped term caps the improvement from making that bad action even less likely, which again avoids potentially unnecessary overshooting in that direction because the probability of the action is already lower than the probability under the old policy. We minimize this surrogate over $\theta .$ The clipping term prevents the objective from continuing to reward changes that have already made an action much more or much less likely than it was under $\pi _ { \theta _ { \mathrm { o l d } } }$

Finally, in many practical settings the advantage estimates are improved with generalized advantage estimation (GAE) [Schulman et al., 2016]. In the RLVR setting discussed in Section 18.2, the advantage estimate is often simplified further, for example by using group-relative or mean-reward baselines rather than a learned value function.

<!-- page: 267 -->

# Appendix A

## Gaussian and KL facts

This appendix collects a few elementary facts used in the derivations above.

## A.1 Basic Gaussian and KL identities

Lemma A.1.1 (Linear combinations of independent Gaussians). Let $\epsilon _ { 1 } , \dots , \epsilon _ { t }$ be independent standard Gaussian random vectors in $\mathbb { R } ^ { d }$ , and let $a _ { 1 } , \ldots , a _ { t }$ be real numbers. Then

$$
\sum_ {s = 1} ^ {t} a _ {s} \epsilon_ {s} \sim \mathcal {N} \Bigg (0, \left(\sum_ {s = 1} ^ {t} a _ {s} ^ {2}\right) I \Bigg).\tag{A.1}
$$

Proof. The sum is Gaussian because it is a linear combination of jointly Gaussian random vectors. Its mean is zero, and its covariance is

$$
\mathrm{Cov} \left(\sum_ {s = 1} ^ {t} a _ {s} \epsilon_ {s}\right) = \sum_ {s = 1} ^ {t} a _ {s} ^ {2} \mathrm{Cov} (\epsilon_ {s}) = \left(\sum_ {s = 1} ^ {t} a _ {s} ^ {2}\right) I,\tag{A.2}
$$

where independence removes the cross-covariance terms.

Lemma A.1.2 (Conditioning a joint Gaussian). Suppose

$$
\binom{A}{B} \sim \mathcal {N} \bigg (\binom{\mu_ {A}}{\mu_ {B}}, \left( \begin{array}{c c} \Sigma_ {A A} & \Sigma_ {A B} \\ \Sigma_ {B A} & \Sigma_ {B B} \end{array} \right) \bigg),\tag{A.3}
$$

with $\Sigma _ { B B }$ invertible. Then

$$
A \mid B = b \sim \mathcal {N} \big (\mu_ {A} + \Sigma_ {A B} \Sigma_ {B B} ^ {- 1} (b - \mu_ {B}), \Sigma_ {A A} - \Sigma_ {A B} \Sigma_ {B B} ^ {- 1} \Sigma_ {B A} \big).\tag{A.4}
$$

Similarly, $\mathit { i f } \: \Sigma _ { A A }$ is invertible, then

$$
B \mid A = a \sim \mathcal {N} \big (\mu_ {B} + \Sigma_ {B A} \Sigma_ {A A} ^ {- 1} (a - \mu_ {A}), \Sigma_ {B B} - \Sigma_ {B A} \Sigma_ {A A} ^ {- 1} \Sigma_ {A B} \big).\tag{A.5}
$$

<!-- page: 268 -->

Proof. Let

$$
R _ {A} = A - \mu_ {A} - \Sigma_ {A B} \Sigma_ {B B} ^ {- 1} (B - \mu_ {B}).\tag{A.6}
$$

Since $( A , B )$ is jointly Gaussian, $( R _ { A } , B )$ is jointly Gaussian. Moreover,

$$
\mathrm{Cov} (R _ {A}, B) = \Sigma_ {A B} - \Sigma_ {A B} \Sigma_ {B B} ^ {- 1} \Sigma_ {B B} = 0.\tag{A.7}
$$

For jointly Gaussian random variables, zero covariance implies independence, so $R _ { A }$ is independent of B. Its mean is zero and its covariance is

$$
\mathrm{Cov} (R _ {A}) = \Sigma_ {A A} - \Sigma_ {A B} \Sigma_ {B B} ^ {- 1} \Sigma_ {B A}.\tag{A.8}
$$

Therefore, conditioning on $B = b$ only replaces B by b in the affine representation of $A ,$ giving the displayed formula for $A   |   B   =   b$ . The formula for $B \mid A = a$ follows by the same argument with the roles of A and B interchanged. □

Lemma A.1.3 (KL between Gaussians with the same covariance). If $P =$ $\mathcal { N } ( m _ { 1 } , \Sigma )$ and $Q = \mathcal { N } ( m _ { 2 } , \Sigma )$ with the same positive definite covariance matrix Σ, then

$$
\mathrm{KL} (P \parallel Q) = \frac {1}{2} (m _ {1} - m _ {2}) ^ {T} \Sigma^ {- 1} (m _ {1} - m _ {2}).\tag{A.9}
$$

Proof. Writing the two Gaussian log densities and subtracting, the normalizing constants and quadratic terms in x cancel except for the difference in means. Taking expectation under P gives

$$
\mathrm{E} _ {P} \left[ \log \frac {d P}{d Q} \right] = \frac {1}{2} \mathrm{E} _ {P} \left[ (X - m _ {2}) ^ {T} \Sigma^ {- 1} (X - m _ {2}) - (X - m _ {1}) ^ {T} \Sigma^ {- 1} (X - m _ {1}) \right].\tag{A.10}
$$

Since $\operatorname { E } _ { P } [ X ] = m _ { 1 }$ , this reduces to the stated expression.

Lemma A.1.4 (Chain rule for KL). Suppose $q ( x , y )   =   q ( x ) q ( y   \mid   x )$ and $p ( x , y ) = p ( x ) p ( y \mid x )$ . Then

$$
\mathrm{KL} (q (x, y) \parallel p (x, y)) = \mathrm{KL} (q (x) \parallel p (x)) + \mathrm{E} _ {q (x)} \left[ \mathrm{KL} (q (y \mid x) \parallel p (y \mid x)) \right].\tag{A.11}
$$

More generally, if

$$
q (x _ {1: T}) = q (x _ {T}) \prod_ {t = 2} ^ {T} q (x _ {t - 1} \mid x _ {t: T}) \quad a n d \quad p (x _ {1: T}) = p (x _ {T}) \prod_ {t = 2} ^ {T} p (x _ {t - 1} \mid x _ {t: T}),\tag{A.12}
$$

<!-- page: 269 -->

then

$$
\begin{array}{l} \mathrm{KL} (q (x _ {1: T}) \parallel p (x _ {1: T})) = \mathrm{KL} (q (x _ {T}) \parallel p (x _ {T})) \\ \qquad + \sum_ {t = 2} ^ {T} \mathrm{E} _ {q} \big [ \mathrm{KL} \big (q (x _ {t - 1} \mid x _ {t: T}) \parallel p (x _ {t - 1} \mid x _ {t: T}) \big) \big ]. \end{array}\tag{A.13}
$$

Proof. Use the factorization inside the log likelihood ratio:

$$
\mathrm{KL} (q (x, y) \parallel p (x, y)) = \mathrm{E} _ {q} \left[ \log \frac {q (x) q (y \mid x)}{p (x) p (y \mid x)} \right]\tag{A.14}
$$

$$
= \mathrm{E} _ {q} \left[ \log \frac {q (x)}{p (x)} \right] + \mathrm{E} _ {q} \left[ \log \frac {q (y \mid x)}{p (y \mid x)} \right],\tag{A.15}
$$

which is exactly the claimed identity.

<!-- page: 270 -->

## Bibliography

Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, and Sumit Sanghai. GQA: Training generalized multi-query transformer models from multi-head checkpoints. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 4895–4901, 2023.

Brian D. O. Anderson. Reverse-time diffusion equation models. Stochastic Processes and their Applications, 12(3):313–326, 1982.

Mikhail Belkin, Daniel Hsu, Siyuan Ma, and Soumik Mandal. Reconciling modern machine-learning practice and the classical bias–variance trade-off. Science, 116(32), 2019.

Mikhail Belkin, Daniel Hsu, and Ji Xu. Two models of double descent for weak features. SIAM Journal on Mathematics of Data Science, 2(4):1167–1180, 2020.

David M Blei, Alp Kucukelbir, and Jon D McAuliffe. Variational inference: A review for statisticians. Journal of the American Statistical Association, 112(518):859–877, 2017.

Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Altman, Sim ran Arora, Sydney von Arx, Michael S. Bernstein, Jeannette Bohg, An toine Bosselut, Emma Brunskill, Erik Brynjolfsson, Shyamal Buch, Dallas Card, Rodrigo Castellon, Niladri Chatterji, Annie Chen, Kathleen Creel, Jared Quincy Davis, Dora Demszky, Chris Donahue, Moussa Doum bouya, Esin Durmus, Stefano Ermon, John Etchemendy, Kawin Etha yarajh, Li Fei-Fei, Chelsea Finn, Trevor Gale, Lauren Gillespie, Karan Goel, Noah Goodman, Shelby Grossman, Neel Guha, Tatsunori Hashimoto, Peter Henderson, John Hewitt, Daniel E. Ho, Jenny Hong, Kyle Hsu, Jing Huang, Thomas Icard, Saahil Jain, Dan Jurafsky, Pratyusha Kalluri, Siddharth Karamcheti, Geoff Keeling, Fereshte Khani, Omar Khattab, Pang Wei Kohd, Mark Krass, Ranjay Krishna, Rohith Kuditipudi, Ananya

<!-- page: 271 -->

Kumar, Faisal Ladhak, Mina Lee, Tony Lee, Jure Leskovec, Isabelle Levent, Xiang Lisa Li, Xuechen Li, Tengyu Ma, Ali Malik, Christopher D. Manning, Suvir Mirchandani, Eric Mitchell, Zanele Munyikwa, Suraj Nair, Avanika Narayan, Deepak Narayanan, Ben Newman, Allen Nie, Juan Carlos Niebles, Hamed Nilforoshan, Julian Nyarko, Giray Ogut, Laurel Orr, Isabel Papadimitriou, Joon Sung Park, Chris Piech, Eva Portelance, Christopher Potts, Aditi Raghunathan, Rob Reich, Hongyu Ren, Frieda Rong, Yusuf Roohani, Camilo Ruiz, Jack Ryan, Christopher Ré, Dorsa Sadigh, Shiori Sagawa, Keshav Santhanam, Andy Shih, Krishnan Srinivasan, Alex Tamkin, Rohan Taori, Armin W. Thomas, Florian Tramèr, Rose E. Wang, William Wang, Bohan Wu, Jiajun Wu, Yuhuai Wu, Sang Michael Xie, Michihiro Yasunaga, Jiaxuan You, Matei Zaharia, Michael Zhang, Tianyi Zhang, Xikun Zhang, Yuhui Zhang, Lucia Zheng, Kaitlyn Zhou, and Percy Liang. On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258, 2021.

Ralph Allan Bradley and Milton E. Terry. Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika, 39(3/4):324–345, 1952.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.

Qi Chen, Bing Zhao, Haidong Wang, Mingqin Li, Chuanjie Liu, Zengzhong Li, Mao Yang, and Jingdong Wang. SPANN: Highlyefficient billion-scale approximate nearest neighbor search. In Advances in Neural Information Processing Systems, volume 34, 2021. URL [https://proceedings.neurips.cc/paper/2021/hash/299dc35e747eb77177d9cea10a802da2-Abstract.html](https://proceedings.neurips.cc/paper/2021/hash/299dc35e747eb77177d9cea10a802da2-Abstract.html).

Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive learning of visual representations. In International conference on machine learning, volume 119 of Proceedings of Machine Learning Research, pages 1597–1607. PMLR, PMLR, 13–18 Jul 2020.

Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, and Dario Amodei. Deep reinforcement learning from human preferences. In Advances in Neural Information Processing Systems (NeurIPS), 2017.

<!-- page: 272 -->

Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. In Advances in Neural Information Processing Systems, volume 35, pages 16344–16359, 2022. URL [https://arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135).

Yann N Dauphin, Angela Fan, Michael Auli, and David Grangier. Language modeling with gated convolutional networks. arXiv preprint arXiv:1612.08083, 2016.

DeepSeek-AI. DeepSeek-V3 technical report. arXiv preprint arXiv:2412.19437, 2024. URL [https://arxiv.org/abs/2412.19437](https://arxiv.org/abs/2412.19437).

DeepSeek-AI. DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025. URL [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948).

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In Association for Computational Linguistics (ACL), pages 4171–4186, 2019.

Jeff Z HaoChen, Colin Wei, Jason D Lee, and Tengyu Ma. Shape matters: Understanding the implicit bias of the noise covariance. arXiv preprint arXiv:2006.08680, 2020.

Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J Tibshirani. Surprises in high-dimensional ridgeless least squares interpolation. 2019.

Trevor Hastie, Andrea Montanari, Saharon Rosset, and Ryan J Tibshirani. Surprises in high-dimensional ridgeless least squares interpolation. The Annals of Statistics, 50(2):949–986, 2022.

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 770–778, 2016.

Dan Hendrycks and Kevin Gimpel. Gaussian error linear units (gelus). arXiv preprint arXiv:1606.08415, 2016.

Alex Henry, Prudhvi Raj Dachapally, Shubham Shantaram Pawar, and Yuxuan Chen. Query-key normalization for transformers. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 4246–4253, 2020.

<!-- page: 273 -->

Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In Advances in Neural Information Processing Systems, volume 33, pages 6840–6851, 2020.

Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International Conference on Learning Representations, 2022. URL [https://openreview.net/forum?id=nZeVKeeFYf9](https://openreview.net/forum?id=nZeVKeeFYf9).

Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In Proceedings of the 32nd International Conference on Machine Learning, ICML 2015, Lille, France, 6-11 July 2015, volume 37 of JMLR Workshop and Conference Proceedings, pages 448–456. JMLR.org, 2015. URL http://jmlr.org[proceedings/papers/v37/ioffe15.html](http://jmlr.org/proceedings/papers/v37/ioffe15.html).

Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani. An introduction to statistical learning, second edition, volume 112. Springer, 2021.

Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980, 2014.

Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114, 2013.

Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large language models are zero-shot reasoners. In Advances in Neural Information Processing Systems, volume 35, pages 22199–22213, 2022. URL [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916).

Taku Kudo and John Richardson. Sentencepiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. In Empirical Methods in Natural Language Processing (EMNLP), 2018.

Ananya Kumar, Aditi Raghunathan, Robbie Jones, Tengyu Ma, and Percy Liang. Fine-tuning can distort pretrained features and underperform outof-distribution. arXiv preprint arXiv:2202.10054, 2022.

Zhimin Li, Jianwei Zhang, Qin Lin, Jiangfeng Xiong, Yanxin Long, Xinchi Deng, Yingfang Zhang, Xingchao Liu, Minbin Huang, Zedong Xiao, et al. Hunyuan-dit: A powerful multi-resolution diffusion transformer with finegrained chinese understanding. arXiv preprint arXiv:2405.08748, 2024.

<!-- page: 274 -->

Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and Min Lin. Understanding R1-Zero-like training: A critical perspective. arXiv preprint arXiv:2503.20783, 2025. URL [https://arxiv.org/abs/2503.20783](https://arxiv.org/abs/2503.20783).

Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on Learning Representations (ICLR), 2019.

Yuping Luo, Huazhe Xu, Yuanzhi Li, Yuandong Tian, Trevor Darrell, and Tengyu Ma. Algorithmic framework for model-based deep reinforcement learning with theoretical guarantees. arXiv preprint arXiv:1807.03858, 2018.

Yu A. Malkov and D. A. Yashunin. Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs. IEEE Transactions on Pattern Analysis and Machine Intelligence, 42(4):824–836, 2020. URL [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320).

Vincent Mazet. Convolution. Basics of Image Processing, 2026. Online; accessed April 22, 2026. [https://vincmazet.github.io/bip/filtering/convolution.html](https://vincmazet.github.io/bip/filtering/convolution.html).

Song Mei and Andrea Montanari. The generalization error of random features regression: Precise asymptotics and the double descent curve. Communications on Pure and Applied Mathematics, 75(4):667–766, 2022.

Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer. Rethinking the role of demonstrations: What makes in-context learning work? In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 11048–11064, 2022.

MiniMax. MiniMax-M1: Scaling test-time compute efficiently with lightning attention. arXiv preprint arXiv:2506.13585, 2025. URL [https://arxiv.org/abs/2506.13585](https://arxiv.org/abs/2506.13585).

Preetum Nakkiran. More data can hurt for linear regression: Sample-wise double descent. 2019.

Preetum Nakkiran, Prayaag Venkat, Sham Kakade, and Tengyu Ma. Optimal regularization can mitigate double descent. arXiv preprint arXiv:2003.01897, 2020.

<!-- page: 275 -->

Huy Nguyen, Thong T. Doan, Quang Pham, Nghi D. Q. Bui, Nhat Ho, and Alessandro Rinaldo. On deepseekmoe: Statistical benefits of shared experts and normalized sigmoid gating. arXiv preprint arXiv:2505.10860, 2025.

Alex Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic models. In Proceedings of the 38th International Conference on Machine Learning, pages 8162–8171, 2021.

Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, Charles Sutton, and Augustus Odena. Show your work: Scratchpads for intermediate computation with language models. arXiv preprint arXiv:2112.00114, 2021. URL [https://arxiv.org/abs/2112.00114](https://arxiv.org/abs/2112.00114).

OLMo Team, Pete Walsh, Luca Soldaini, Dirk Groeneveld, Kyle Lo, Shane Arora, Akshita Bhagia, Yuling Gu, Shengyi Huang, Matt Jordan, et al. 2 OLMo 2 furious. arXiv preprint arXiv:2501.00656, 2024.

OpenAI. Learning to reason with LLMs. [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/), September 2024.

OpenAI. gpt-oss-120b & gpt-oss-20b model card, 2025. URL [https://arxiv.org/abs/2508.10925](https://arxiv.org/abs/2508.10925).

Manfred Opper. Statistical mechanics of learning: Generalization. The Handbook of Brain Theory and Neural Networks,, pages 922–925, 1995.

Manfred Opper. Learning to generalize. Frontiers of Life, 3(part 2):763–775, 2001.

Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instructions with human feedback. In Advances in Neural Information Processing Systems, volume 35, pages 27730–27744, 2022. URL [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155).

Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, and Junyang Lin. Gated attention for large language models: Non-linearity, sparsity, and attention-sink-free. arXiv preprint arXiv:2505.06708, 2025.

<!-- page: 276 -->

Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model. In Advances in Neural Information Processing Systems, volume 36, 2023. URL [https://arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290).

Prajit Ramachandran, Barret Zoph, and Quoc V Le. Searching for activation functions. arXiv preprint arXiv:1710.05941, 2017.

John Schulman, Sergey Levine, Pieter Abbeel, Michael Jordan, and Philipp Moritz. Trust region policy optimization. In International conference on machine learning, pages 1889–1897, 2015.

John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, and Pieter Abbeel. High-dimensional continuous control using generalized advantage estimation. In International Conference on Learning Representations, 2016. URL [https://arxiv.org/abs/1506.02438](https://arxiv.org/abs/1506.02438).

John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.

Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. In Association for Computational Linguistics (ACL), 2016.

Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024. URL [https://arxiv.org/abs/2402.03300](https://arxiv.org/abs/2402.03300).

Noam Shazeer. Fast transformer decoding: One write-head is all you need. arXiv preprint arXiv:1911.02150, 2019.

Noam Shazeer. Glu variants improve transformer. arXiv preprint arXiv:2002.05202, 2020.

David R So, Wojciech Mańke, Hanxiao Liu, Zihang Dai, Noam Shazeer, and Quoc V Le. Primer: Searching for efficient transformers for language modeling. In Advances in Neural Information Processing Systems, 2021.

Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsupervised learning using nonequilibrium thermodynamics.

<!-- page: 277 -->

In Proceedings of the 32nd International Conference on Machine Learning, pages 2256–2265, 2015.

Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. In International Conference on Learning Representations, 2021.

Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel M. Ziegler, Ryan Lowe, Chelsea Voss, Alec Radford, Dario Amodei, and Paul Christiano. Learning to summarize from human feedback. In Advances in Neural Information Processing Systems, volume 33, pages 3008–3021, 2020. URL [https://arxiv.org/abs/2009.01325](https://arxiv.org/abs/2009.01325).

Mingxing Tan and Quoc V Le. Efficientnet: Rethinking model scaling for convolutional neural networks. In International Conference on Machine Learning, pages 6105–6114. PMLR, 2019.

Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. arXiv preprint arXiv:1706.03762, 2017.

Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In International Conference on Learning Representations, 2023. URL [https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171).

Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. Finetuned language models are zero-shot learners. arXiv, 2021.

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems, volume 35, pages 24824–24837, 2022.

<!-- page: 278 -->

Blake Woodworth, Suriya Gunasekar, Jason D Lee, Edward Moroshko, Pedro Savarese, Itay Golan, Daniel Soudry, and Nathan Srebro. Kernel and rich regimes in overparametrized models. arXiv preprint arXiv:2002.09277, 2020.

Yuxin Wu and Kaiming He. Group normalization. In Proceedings of the European conference on computer vision (ECCV), pages 3–19, 2018.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025.

Emine Yilmaz, Evangelos Kanoulas, and Javed A Aslam. A simple and efficient sampling method for estimating AP and NDCG. In ACM Special Interest Group on Information Retreival (SIGIR), pages 603–610, 2008.

Weihao Zeng, Yuzhen Huang, Qian Liu, Wei Liu, Keqing He, Zejun Ma, and Junxian He. SimpleRL-Zoo: Investigating and taming zero reinforcement learning for open base models in the wild. In Conference on Language Modeling, 2025. URL [https://arxiv.org/abs/2503.18892](https://arxiv.org/abs/2503.18892).

Biao Zhang and Rico Sennrich. Root mean square layer normalization. In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019. URL [https://proceedings.neurips.cc/paper\_files/paper/2019/file/1e8a19426224ca89e83cef47f1e7f53b-Paper.pdf](https://proceedings.neurips.cc/paper_files/paper/2019/file/1e8a19426224ca89e83cef47f1e7f53b-Paper.pdf).

Zhengyan Zhang, Yixin Song, Guanghui Yu, Xu Han, Yankai Lin, Chaojun Xiao, Chenyang Song, Zhiyuan Liu, Zeyu Mi, and Maosong Sun. Relu<sup>2</sup> wins: Discovering efficient activation functions for sparse llms. arXiv preprint arXiv:2402.03804, 2024.

Denny Zhou, Nathanael Scharli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, and Ed H. Chi. Least-to-most prompting enables complex reasoning in large language models. In International Conference on Learning Representations, 2023. URL [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625).

Daniel M. Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B. Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving. Fine-tuning language models from human preferences. arXiv preprint arXiv:1909.08593, 2019. URL [https://arxiv.org/abs/1909.08593](https://arxiv.org/abs/1909.08593).
