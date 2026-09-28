<!-- page: 1 -->

# Deep learning: Technical introduction

Thomas Epelbaum

![](images/page_0_image_6.jpg)

September 12, 2017

<!-- page: 2 -->

<!-- page: 3 -->

## Contents

- 1 Preface 5
- 2 Acknowledgements 7
- 3 Introduction 9
- 4 Feedforward Neural Networks 11
- 4.1 Introduction 12
- 4.2 FNN architecture 13
- 4.3 Some notations 14
- 4.4 Weight averaging 14
- 4.5 Activation function 15
- 4.6 FNN layers 20
- 4.7 Loss function 21
- 4.8 Regularization techniques 22
- 4.9 Backpropagation 27
- 4.10 Which data sample to use for gradient descent? 29
- 4.11 Gradient optimization techniques 30
- 4.12 Weight initialization 32
- Appendices 33
- 4.A Backprop through the output layer 33
- 4.B Backprop through hidden layers 34
- 4.C Backprop through BatchNorm 34
- 4.D FNN ResNet (non standard presentation) 35
- 4.E FNN ResNet (more standard presentation) 38
- 4.F Matrix formulation 38
- 5 Convolutional Neural Networks 41
- 5.1 Introduction 42
- 5.2 CNN architecture 43
- 5.3 CNN specificities 43
- 5.4 Modification to Batch Normalization 49
- 5.5 Network architectures 50
- 5.6 Backpropagation 56
- Appendices 64
- 5.A Backprop through BatchNorm 64
- 5.B Error rate updates: details 65

<!-- page: 4 -->

- 5.C Weight update: details 67
- 5.D Coefficient update: details 68
- 5.E Practical Simplification 68
- 5.F Batchpropagation through a ResNet module 71
- 5.G Convolution as a matrix multiplication 72
- 5.H Pooling as a row matrix maximum 75
- 6 Recurrent Neural Networks 77
- 6.1 Introduction 78
- 6.2 RNN-LSTM architecture 78
- 6.3 Extreme Layers and loss function 80
- 6.4 RNN specificities 81
- 6.5 LSTM specificities 85
- Appendices 90
- 6.A Backpropagation trough Batch Normalization 90
- 6.B RNN Backpropagation 91
- 6.C LSTM Backpropagation 95
- 6.D Peephole connexions 101
- 7 Conclusion 103

<!-- page: 5 -->

# Chapter 1

# Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F PrefaceInput Convolution Layer . . . N + 2P T + 2P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

![](images/page_4_image_2.jpg)

started learning about deep learning fundamentals in February 2017. At this time, I knew nothing about backpropagation, and was completely ignorant about the differences between a Feedforward, Convolutional and a Recurrent Neural Network.

As I navigated through the humongous amount of data available on deep learning online, I found myself quite frustrated when it came to really understand what deep learning is, and not just applying it with some available library.

In particular, the backpropagation update rules are seldom derived, and never in index form. Unfortunately for me, I have an "index" mind: seeing a 4 Dimensional convolution formula in matrix form does not do it for me. Since I am also stupid enough to like recoding the wheel in low level programming languages, the matrix form cannot be directly converted into working code either.

I therefore started some notes for my personal use, where I tried to rederive everything from scratch in index form.

I did so for the vanilla Feedforward network, then learned about L1 and L2 regularization , dropout[1], batch normalization[2], several gradient descent optimization techniques... Then turned to convolutional networks, from conventional single digit number of layer conv-pool architectures[3] to recent VGG[4] ResNet[5] ones, from local contrast normalization and rectification to bacthnorm... And finally I studied Recurrent Neural Network structures[6], from the standard formulation to the most recent LSTM one[7].

As my work progressed, my notes got bigger and bigger, until a point when I realized I might have enough material to help others starting their own deep learning journey.

<!-- page: 6 -->

This work is bottom-up at its core. If you are searching a working Neural Network in 10 lines of code and 5 minutes of your time, you have come to the wrong place. If you can mentally multiply and convolve 4D tensors, then I have nothing to convey to you either.

If on the other hand you like(d) to rederive every tiny calculation of every theorem of every class that you stepped into, then you might be interested by what follow!

<!-- page: 7 -->

# Chapter 2

# Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F AcknowledgementsInput Convolution Layer . . . N + 2P T + 2P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

![](images/page_6_image_2.jpg)

his work has no benefit nor added value to the deep learning topic on its own. It is just the reformulation of ideas of brighter researchers to fit a peculiar mindset: the one of preferring formulas with ten indices but where one knows precisely what one is manipulating rather than

(in my opinion sometimes opaque) matrix formulations where the dimension of the objects are rarely if ever specified.

Among the brighter people from whom I learned online are Andrew Ng. His Coursera class ([here](https://www.coursera.org/learn/machine-learning)) was the first contact I got with Neural Network, and this pedagogical introduction allowed me to build on solid ground.

I also wish to particularly thanks Hugo Larochelle, who not only built a wonderful deep learning class ([here](http://info.usherbrooke.ca/hlarochelle/neural_networks/content.html)), but was also kind enough to answer emails from a complete beginner and stranger!

The Stanford class on convolutional networks ([here](http://cs231n.github.io/convolutional-networks/)) proved extremely valuable to me, so did the one on Natural Language processing ([here](http://web.stanford.edu/class/cs224n/)).

I also benefited greatly from Sebastian Ruder’s blog ([here](http://ruder.io/#open)), both from the blog pages on gradient descent optimization techniques and from the author himself.

I learned more about LSTM on colah’s blog ([here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)), and some of my drawings are inspired from there.

I also thank Jonathan Del Hoyo for the great articles that he regularly shares on LinkedIn.

Many thanks go to my collaborators at Mediamobile, who let me dig as deep as I wanted on Neural Networks. I am especially indebted to Clément, Nicolas, Jessica, Christine and Céline.

<!-- page: 8 -->

Thanks to Jean-Michel Loubes and Fabrice Gamboa, from whom I learned a great deal on probability theory and statistics.

I end this list with my employer, Mediamobile, which has been kind enough to let me work on this topic with complete freedom. A special thanks to Philippe, who supervised me with the perfect balance of feedback and freedom!

<!-- page: 9 -->

# Chapter 3

# Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F IntroductionInput Convolution Layer . . . N + 2P T + 2P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

![](images/page_8_image_2.jpg)

his note aims at presenting the three most common forms of neural network architectures. It does so in a technical though hopefully pedagogical way, buiding up in complexity as one progresses through the chapters.

Chapter 4 starts with the first type of network introduced historically: a regular feedforward neural network, itself an evolution of the original perceptron [8] algorithm. One should see the latter as a non-linear regression, and feedforward networks schematically stack perceptron layers on top of one another.

We will thus introduce in chapter 4 the fundamental building blocks of the simplest neural network layers: weight averaging and activation functions. We will also introduce gradient descent as a way to train the network when joint with the backpropagation algorithm, as a way to minimize a loss function adapted to the task at hand (classification or regression). The more technical details of the backpropagation algorithm are found in the appendix of this chapter, alongside with an introduction to the state of the art feedforward neural network, the ResNet. One can finally find a short matrix description of the feedforward network.

In chapter 5, we present the second type of neural network studied: the convolutional networks, particularly suited to treat images and label them. This implies presenting the mathematical tools related to this network: convolution, pooling, stride... As well as seeing the modification of the building block introduced in chapter 4. Several convolutional architectures are then presented, and the appendices once again detail the difficult steps of the main text.

Chapter 6 finally presents the network architecture suited for data with a temporal structure – as time series for instance, the recurrent neural network.

<!-- page: 10 -->

There again, the novelties and the modifications of the material introduced in the two previous chapters are detailed in the main text, while the appendices give all what one needs to understand the most cumbersome formula of this kind of network architecture.

<!-- page: 11 -->

## Chapter 4 Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F Feedfor ward Neural NetworksInput Convolution Layer . . . N + 2P <sup>T + 2</sup>P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

## Contents

- 4.1 Introduction 12
- 4.2 FNN architecture 13
- 4.3 Some notations 14
- 4.4 Weight averaging 14
- 4.5 Activation function 15
- 4.5.1 The sigmoid function 15
- 4.5.2 The tanh function 16
- 4.5.3 The ReLU function 17
- 4.5.4 The leaky-ReLU function 18
- 4.5.5 The ELU function 19
- 4.6 FNN layers 20
- 4.6.1 Input layer 20
- 4.6.2 Fully connected layer 21
- 4.6.3 Output layer 21
- 4.7 Loss function 21
- 4.8 Regularization techniques 22
- 4.8.1 L2 regularization 22
- 4.8.2 L1 regularization 23
- 4.8.3 Clipping 24
- 4.8.4 Dropout 24

<!-- page: 12 -->

- 4.8.5 Batch Normalization 25
- 4.9 Backpropagation 27
- 4.9.1 Backpropagate through Batch Normalization 27
- 4.9.2 error updates 27
- 4.9.3 Weight update 28
- 4.9.4 Coefficient update 28
- 4.10 Which data sample to use for gradient descent? 29
- 4.10.1 Full-batch 29
- 4.10.2 Stochastic Gradient Descent (SGD) 29
- 4.10.3 Mini-batch 29
- 4.11 Gradient optimization techniques 30
- 4.11.1 Momentum 30
- 4.11.2 Nesterov accelerated gradient 30
- 4.11.3 Adagrad 31
- 4.11.4 RMSprop 31
- 4.11.5 Adadelta 31
- 4.11.6 Adam 32
- 4.12 Weight initialization 32
- Appendices 33
- 4.A Backprop through the output layer 33
- 4.B Backprop through hidden layers 34
- 4.C Backprop through BatchNorm 34
- 4.D FNN ResNet (non standard presentation) 35
- 4.E FNN ResNet (more standard presentation) 38
- 4.F Matrix formulation 38

## 4.1 Introduction

![](images/page_11_image_4.jpg)

n this section we review the first type of neural network that has I been developed historically: a regular Feedforward Neural Network (FNN). This network does not take into account any particular structure that the input data might have. Nevertheless, it is already a very powerful machine learning tool, especially when used with the state of the art regularization techniques. These techniques – that we are going to present as

<!-- page: 13 -->

well – allowed to circumvent the training issues that people experienced when dealing with "deep" architectures: namely the fact that neural networks with an important number of hidden states and hidden layers have proven historically to be very hard to train (vanishing gradient and overfitting issues).

## 4.2 FNN architecture

![](images/page_12_image_4.jpg)

Figure 4.1: Neural Network with N + 1 layers (N − 1 hidden layers). For simplicity of notations, the index referencing the training set has not been indicated. Shallow architectures use only one hidden layer. Deep learning amounts to take several hidden layers, usually containing the same number of hidden neurons. This number should be on the ballpark of the average of the number of input and output variables.

A FNN is formed by one input layer, one (shallow network) or more (deep network, hence the name deep learning) hidden layers and one output layer. Each layer of the network (except the output one) is connected to a following layer. This connectivity is central to the FNN structure and has two main features in its simplest form: a weight averaging feature and an activation feature. We will review these features extensively in the following

<!-- page: 14 -->

## 4.3 Some notations

In the following, we will call

• N the number of layers (not counting the input) in the Neural Network.

$T _ { \mathrm { t r a i n } }$ the number of training examples in the training set.

$T _ { \mathrm { m b } }$ the number of training examples in a mini-batch (see section 4.7).

$t \in [ 0 , T _ { \mathrm { m b } } - 1 ]$ the mini-batch training instance index.

$\nu \in [ [ 0 , N ] ]$ the number of layers in the FNN.

$F _ { \nu }$ the number of neurons in the ν’th layer.

$X _ { f } ^ { ( t ) } = h _ { f } ^ { ( 0 ) ( t ) }$ where $f \in [ 0 , F _ { 0 } - 1 ]$ the input variables.

$y _ { f } ^ { ( t ) }$ where $f \in [ 0 , F _ { N } - 1 ]$ the output variables (to be predicted).

$\hat { y } _ { f } ^ { ( t ) }$ where $f \in [ 0 , F _ { N } - 1 ]$ the output of the network.

$\Theta _ { f } ^ { ( \nu ) f ^ { \prime } }$ for $f \in \bigl [ 0 , F _ { \nu } - 1 \bigr ] ,   f ^ { \prime } \in \bigl [ 0 , F _ { \nu + 1 } - 1 \bigr ]$ and $\nu \in [ 0 , N - 1 ]$ the weights matrices

• A bias term can be included. In practice, we will see when talking about the batch-normalization procedure that we can omit it.

## 4.4 Weight averaging

One of the two main components of a FNN is a weight averaging procedure, which amounts to average the previous layer with some weight matrix to obtain the next layer. This is illustrated on the figure 4.2

<!-- page: 15 -->

![](images/page_14_image_2.jpg)

Figure 4.2: Weight averaging procedure.

Formally, the weight averaging procedure reads:

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1 + \epsilon} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)},\tag{4.1}
$$

where $\nu   \in   [ 0 , N - 1 ] , \; t   \in   [ 0 , T _ { \mathsf { m b } } - 1 ]$ and $f   \in   [ [ 0 , F _ { \nu + 1 } - 1 ] ]$ The $\epsilon$ is here to include or exclude a bias term. In practice, as we will be using batchnormalization, we can safely omit it $( \epsilon = 0$ in all the following).

## 4.5 Activation function

The hidden neuron of each layer is defined as

$$
h _ {f} ^ {(t) (\nu + 1)} = g \left(a _ {f} ^ {(t) (\nu)}\right),\tag{4.2}
$$

where $\nu   \in   [ 0 , N - 2 ] , \; f   \in   [ 0 , F _ { \nu + 1 } - 1 ]$ and as usual $t   \in   [ [ 0 , T _ { \mathrm { m b } } - 1 ] ]$ . Here $g$ is an activation function – the second main ingredient of a FNN – whose non-linearity allow to predict arbitrary output data. In practice, $g$ is usually taken to be one of the functions described in the following subsections.

## 4.5.1 The sigmoid function

The sigmoid function takes its value in $] 0 , 1 [$ and reads

$$
g (x) = \sigma (x) = \frac {1}{1 + e ^ {- x}}.\tag{4.3}
$$

<!-- page: 16 -->

Its derivative is

$$
\sigma^ {\prime} (x) = \sigma (x) \left(1 - \sigma (x)\right).\tag{4.4}
$$

This activation function is not much used nowadays (except in RNN-LSTM networks that we will present later in chapter 6).

![](images/page_15_chart_5.jpg)

Figure 4.3: the sigmoid function and its derivative.

## 4.5.2 The tanh function

The tanh function takes its value in $] - 1 , 1 [$ and reads

$$
g (x) = \tanh (x) = \frac {1 - e ^ {- 2 x}}{1 + e ^ {- 2 x}}.\tag{4.5}
$$

Its derivative is

$$
\tanh ^ {\prime} (x) = 1 - \tanh ^ {2} (x).\tag{4.6}
$$

This activation function has seen its popularity drop due to the use of the activation function presented in the next section.

<!-- page: 17 -->

![](images/page_16_chart_2.jpg)

Figure 4.4: the tanh function and its derivative.

It is nevertherless still used in the standard formulation of the RNN-LSTM model (6).

## 4.5.3 The ReLU function

The ReLU – for Rectified Linear Unit – function takes its value in $\left[0, +\infty\right[$ and reads

$$
g (x) = \mathrm{ReLU} (x) = \left\{ \begin{array}{l l} x & x \geq 0 \\ 0 & x <   0 \end{array} \right..\tag{4.7}
$$

Its derivative is

$$
\mathrm{ReLU} ^ {\prime} (x) = \left\{ \begin{array}{l l} 1 & x \geq 0 \\ 0 & x <   0 \end{array} \right..\tag{4.8}
$$

<!-- page: 18 -->

ReLU function and its derivative

![](images/page_17_chart_3.jpg)

Figure 4.5: the ReLU function and its derivative.

This activation function is the most extensively used nowadays. Two of its more common variants can also be found : the leaky ReLU and ELU – Exponential Linear Unit. They have been introduced because the ReLU activation function tends to "kill" certain hidden neurons: once it has been turned off (zero value), it can never be turned on again.

## 4.5.4 The leaky-ReLU function

The leaky-ReLU –for Linear Rectified Linear Unit – function takes its value in $] - \infty , + \infty [$ and is a slight modification of the ReLU that allows non-zero value for the hidden neuron whatever the x value. It reads

$$
g (x) = 1 - \operatorname{ReLU} (x) = \left\{ \begin{array}{l l} x & x \geq 0 \\ 0. 0 1 x & x <   0 \end{array} \right..\tag{4.9}
$$

Its derivative is

$$
1 - \mathrm{ReLU} ^ {\prime} (x) = \left\{ \begin{array}{l l} 1 & x \geq 0 \\ 0. 0 1 & x <   0 \end{array} \right..\tag{4.10}
$$

<!-- page: 19 -->

Leaky ReLU function and its derivative

![](images/page_18_chart_3.jpg)

Figure 4.6: the leaky-ReLU function and its derivative.

A variant of the leaky-ReLU can also be found in the literature : the Parametric-ReLU, where the arbitrary 0.01 in the definition of the leaky-ReLU is replaced by an α coefficient, that can be computed via backpropagation.

$$
g (x) = \text {Parametric} - \operatorname{ReLU} (x) = \left\{ \begin{array}{l l} x & x \geq 0 \\ \alpha x & x <   0 \end{array} \right..\tag{4.11}
$$

Its derivative is

$$
\text {Parametric} - \mathrm{ReLU} ^ {\prime} (x) = \left\{ \begin{array}{l l} 1 & x \geq 0 \\ \alpha & x <   0 \end{array} \right..\tag{4.12}
$$

## 4.5.5 The ELU function

The ELU –for Exponential Linear Unit – function takes its value between $] - 1, + \infty [$ and is inspired by the leaky-ReLU philosophy: non-zero values for all $x ^ { \prime } s$ . But it presents the advantage of being $\bar { \mathcal { C } } ^ { 1 }$

$$
g (x) = \operatorname{ELU} (x) = \left\{ \begin{array}{l l} x & x \geq 0 \\ e ^ {x} - 1 & x <   0 \end{array} \right..\tag{4.13}
$$

Its derivative is

$$
\mathrm{ELU} ^ {\prime} (x) = \left\{ \begin{array}{l l} 1 & x \geq 0 \\ e ^ {x} & x <   0 \end{array} \right..\tag{4.14}
$$

<!-- page: 20 -->

![](images/page_19_chart_2.jpg)

Figure 4.7: the ELU function and its derivative.

## 4.6 FNN layers

As illustrated in figure 4.1, a regular FNN is composed by several specific layers. Let us explicit them one by one.

## 4.6.1 Input layer

The input layer is one of the two places where the data at disposal for the problem at hand come into place. In this chapter, we will be considering a input of size $F _ { 0 } ,$ denoted $X _ { f } ^ { ( t ) }$ , with1 $t   \in   [ [ 0 , T _ { \mathrm { m b } } - 1 ] ]$ (size of the mini-batch, more on that when we will be talking about gradient descent techniques), and $f \in [ [ 0 , F _ { 0 } - 1 ] ]$ . Given the problem at hand, a common procedure could be to center the input following the procedure

$$
\tilde {X} _ {f} ^ {(t)} = X _ {f} ^ {(t)} - \mu_ {f},\tag{4.15}
$$

with

$$
\mu_ {f} = \frac {1}{T _ {\mathrm{train}}} \sum_ {t = 0} ^ {T _ {\mathrm{train}} - 1} X _ {f} ^ {(t)}.\tag{4.16}
$$

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">Tmb  T<sub>train</sub>.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">mb</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>To train the FNN, we jointly compute the forward and backward pass for T samples of the training set, with  In the following we will thus have ∈ J − K t 0, Tmb  1 .</span></small>

<!-- page: 21 -->

This correspond to compute the mean per data types over the training set. Following our notations, let us recall that

$$
X _ {f} ^ {(t)} = h _ {f} ^ {(t) (0)}.\tag{4.17}
$$

## 4.6.2 Fully connected layer

The fully connected operation is just the conjunction of the weight averaging and the activation procedure. Namely, $\forall \nu \in \dot { [ } 0 , N - 1 ]$

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)}.\tag{4.18}
$$

and $\forall \nu \in [ 0 , N - 2 ]$

$$
h _ {f} ^ {(t) (\nu + 1)} = g \left(a _ {f} ^ {(t) (\nu)}\right).\tag{4.19}
$$

for the case where $\nu = N - 1$ , the activation function is replaced by an output function.

## 4.6.3 Output layer

The output of the FNN reads

$$
h _ {f} ^ {(t) (N)} = o (a _ {f} ^ {(t) (N - 1)}) ,\tag{4.20}
$$

where o is called the output function. In the case of the Euclidean loss function, the output function is just the identity. In a classification task, o is the softmax function.

$$
o \left(a _ {f} ^ {(t) (N - 1)}\right) = \frac {e ^ {a _ {f} ^ {(t) (N - 1)}}}{\sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} e ^ {a _ {f ^ {\prime}} ^ {(t) (N - 1)}}}\tag{4.21}
$$

## 4.7 Loss function

The loss function evaluates the error performed by the FNN when it tries to estimate the data to be predicted (second place where the data make their

<!-- page: 22 -->

appearance). For a regression problem, this is simply a mean square error (MSE) evaluation

$$
J (\Theta) = \frac {1}{2 T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f = 0} ^ {F _ {\mathrm{N}} - 1} \left(y _ {f} ^ {(t)} - h _ {f} ^ {(t) (N)}\right) ^ {2},\tag{4.22}
$$

while for a classification task, the loss function is called the cross-entropy function

$$
J (\Theta) = - \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f = 0} ^ {F _ {N} - 1} \delta_ {y ^ {(t)}} ^ {f} \ln h _ {f} ^ {(t) (N)},\tag{4.23}
$$

and for a regression problem transformed into a classification one, calling C the number of bins leads to

$$
J (\Theta) = - \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f = 0} ^ {F _ {N} - 1} \sum_ {c = 0} ^ {C - 1} \delta_ {y _ {f} ^ {(t)}} ^ {c} \ln h _ {f c} ^ {(t) (N)}.\tag{4.24}
$$

For reasons that will appear clear when talking about the data sample used at each training step, we denote

$$
J (\Theta) = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} J _ {\mathrm{mb}} (\Theta).\tag{4.25}
$$

## 4.8 Regularization techniques

On of the main difficulties when dealing with deep learning techniques is to get the deep neural network to train efficiently. To that end, several regularization techniques have been invented. We will review them in this section

## 4.8.1 L2 regularization

L2 regularization is the most common regularization technique that on can find in the literature. It amounts to add a regularizing term to the loss function in the following way

$$
J _ {\mathrm{L2}} (\Theta) = \lambda_ {\mathrm{L2}} \sum_ {\nu = 0} ^ {N - 1} \left\| \Theta^ {(\nu)} \right\| _ {\mathrm{L2}} ^ {2} = \lambda_ {\mathrm{L2}} \sum_ {\nu = 0} ^ {N - 1} \sum_ {f = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left(\Theta_ {f} ^ {(\nu) f ^ {\prime}}\right) ^ {2}.\tag{4.26}
$$

<!-- page: 23 -->

This regularization technique is almost always used, but not on its own. A typical value of $\lambda _ { \mathrm { L } 2 }$ is in the range $1 0 ^ { - 4 } - 1 0 ^ { \frac { 7 } { - 2 } }$ . Interestingly, this L2 regularization technique has a Bayesian interpretation: it is Bayesian inference with a Gaussian prior on the weights. Indeed, for a given $\nu ,$ the weight averaging procedure can be considered as

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)} + \epsilon ,\tag{4.27}
$$

where $\epsilon$ is a noise term of mean 0 and variance $\sigma ^ { 2 }$ . Hence the following Gaussian likelihood for all values of t and $f ;$

$$
\mathcal {N} \left(a _ {f} ^ {(t) (i)} \left| \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)}, \sigma^ {2}\right) \right..\tag{4.28}
$$

Assuming all the weights to have a Gaussian prior of the form $\mathcal { N } \left( \Theta _ { f ^ { \prime } } ^ { ( \nu ) f } \middle | \lambda _ { \mathrm { L } 2 } ^ { - 1 } \right)$ with the same parameter $\lambda _ { \mathrm { L } 2 } ,$ , we get the following expression

$$
\begin{array}{l} \mathcal {P} = \prod_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \prod_ {f = 0} ^ {F _ {\nu + 1} - 1} \left[ \mathcal {N} \left(a _ {f} ^ {(t) (\nu)} \bigg | \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)}, \sigma^ {2}\right) \prod_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \mathcal {N} \left(\Theta_ {f ^ {\prime}} ^ {(\nu) f} \Big | \lambda_ {\mathrm{L2}} ^ {- 1}\right) \right] \\ = \prod_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \prod_ {f = 0} ^ {F _ {\nu + 1} - 1} \left[ \frac {1}{\sqrt {2 \pi \sigma^ {2}}} e ^ {- \frac {\left(a _ {f} ^ {(t) (\nu)} - \Sigma_ {f ^ {\prime} = 0} ^ {F _ {i} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)}\right) ^ {2}}{2 \sigma^ {2}}} \prod_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sqrt {\frac {\lambda_ {\mathrm{L2}}}{2 \pi}} e ^ {- \frac {\left(\Theta_ {f ^ {\prime}} ^ {(\nu) f}\right) ^ {2} \lambda_ {\mathrm{L2}}}{2}} \right]. \end{array}\tag{4.29}
$$

Taking the log of it and forgetting most of the constant terms leads to

$$
\mathcal {L} \propto \frac {1}{T _ {\mathrm{mb}} \sigma^ {2}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f = 0} ^ {F _ {\nu + 1} - 1} \left(a _ {f} ^ {(t) (\nu)} - \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu)}\right) ^ {2} + \lambda_ {\mathrm{L2}} \sum_ {f = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left(\Theta_ {f ^ {\prime}} ^ {(\nu) f}\right) ^ {2},\tag{4.30}
$$

and the last term is exactly the L2 regulator for a given nu value (see formula (4.26)).

## 4.8.2 L1 regularization

L1 regularization amounts to replace the L2 norm by the L1 one in the L2 regularization technique

$$
J _ {\mathrm{L1}} (\Theta) = \lambda_ {\mathrm{L1}} \sum_ {\nu = 0} ^ {N - 1} \left\| \Theta^ {(\nu)} \right\| _ {\mathrm{L1}} = \lambda_ {\mathrm{L1}} \sum_ {\nu = 0} ^ {N - 1} \sum_ {f = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left| \Theta_ {f ^ {\prime}} ^ {(\nu) f} \right|.\tag{4.31}
$$

<!-- page: 24 -->

It can be used in conjunction with L2 regularization, but again these techniques are not sufficient on their own. A typical value of $\lambda _ { \mathrm { L 1 } }$ is in the range $1 0 ^ { - 4 } -$ $1 0 ^ { - 2 }$ . Following the same line as in the previous section, one can show that L1 regularization is equivalent to Bayesian inference with a Laplacian prior on the weights

$$
\mathcal {F} \left(\Theta_ {f ^ {\prime}} ^ {(\nu) f} \Big | 0, \lambda_ {\mathrm{L1}} ^ {- 1}\right) = \frac {\lambda_ {\mathrm{L1}}}{2} e ^ {- \lambda_ {\mathrm{L1}} \left| \Theta_ {f ^ {\prime}} ^ {(\nu) f} \right|}.\tag{4.32}
$$

## 4.8.3 Clipping

Clipping forbids the L2 norm of the weights to go beyond a pre-determined threshold C. Namely after having computed the update rules for the weights, if their L2 norm goes above C, it is pushed back to C

$$
\text {if} \left\| \Theta^ {(\nu)} \right\| _ {\mathrm{L2}} > C \longrightarrow \Theta_ {f ^ {\prime}} ^ {(\nu) f} = \Theta_ {f ^ {\prime}} ^ {(\nu) f} \times \frac {C}{\left\| \Theta^ {(\nu)} \right\| _ {\mathrm{L2}}}.\tag{4.33}
$$

This regularization technique avoids the so-called exploding gradient problem, and is mainly used in RNN-LSTM networks. A typical value of C is in the range $1 0 ^ { 0 } - 1 0 ^ { 1 }$ . Let us now turn to the most efficient regularization techniques for a FNN: dropout and Batch-normalization.

## 4.8.4 Dropout

A simple procedure allows for better backpropagation performance for classification tasks: it amounts to stochastically drop some of the hidden units (and in some instances even some of the input variables) for each training example.

<!-- page: 25 -->

![](images/page_24_image_2.jpg)

Figure 4.8: The neural network of figure 4.1 with dropout taken into account for both the hidden layers and the input. Usually, a different (lower) probability for turning off a neuron is adopted for the input than the one adopted for the hidden layers.

This amounts to do the following change: for $\nu \in [ 1 , N - 1 ]$

$$
h _ {f} ^ {(\nu)} = m _ {f} ^ {(\nu)} g \left(a _ {f} ^ {(\nu)}\right)\tag{4.34}
$$

with $m _ { f } ^ { ( i ) }$ following a $p$ Bernoulli distribution with usually $\textstyle p = { \frac { 1 } { 5 } }$ for the mask of the input layer and $\textstyle p = { \frac { 1 } { 2 } }$ otherwise. Dropout[1] has been the most successful regularization technique until the appearance of Batch Normalization.

## 4.8.5 Batch Normalization

Batch normalization[2] amounts to jointly normalize the mini-batch set per data types, and does so at each input of a FNN layer. In the original paper, the authors argued that this step should be done after the convolutional layers, but in practice it has been shown to be more efficient after the non-linear step. In

<!-- page: 26 -->

our case, we will thus consider $\forall i \in [ 0 , N - 2 ]$

$$
\tilde {h} _ {f} ^ {(t) (\nu)} = \frac {h _ {f} ^ {(t) (\nu + 1)} - \hat {h} _ {f} ^ {(\nu)}}{\sqrt {\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} + \epsilon}},\tag{4.35}
$$

with

$$
\hat {h} _ {f} ^ {(\nu)} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f} ^ {(t) (\nu + 1)}
$$

$$
\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left(h _ {f} ^ {(t) (\nu + 1)} - \hat {h} _ {f} ^ {(\nu)}\right) ^ {2}.\tag{4.36}
$$

(4.37)

To make sure that this transformation can represent the identity transform, we add two additional parameters $( \gamma _ { f } , \beta _ { f } )$ to the model

$$
y _ {f} ^ {(t) (\nu)} = \gamma_ {f} ^ {(\nu)} \tilde {h} _ {f} ^ {(t) (\nu)} + \beta_ {f} ^ {(\nu)} = \tilde {\gamma} _ {f} ^ {(\nu)} h _ {f} ^ {(t) (\nu)} + \tilde {\beta} _ {f} ^ {(\nu)}.\tag{4.38}
$$

The presence of the $\beta _ { f } ^ { ( \nu ) }$ coefficient is what pushed us to get rid of the bias term, as it is naturally included in batchnorm. During training, one must compute a running sum for the mean and the variance, that will serve for the evaluation of the cross-validation and the test set (calling e the number of iterations/epochs)

$$
\mathbb {E} \left[ h _ {f} ^ {(t) (\nu + 1)} \right] _ {e + 1} = \frac {e \mathbb {E} \left[ h _ {f} ^ {(t) (\nu)} \right] _ {e} + \hat {h} _ {f} ^ {(\nu)}}{e + 1},\tag{4.39}
$$

$$
\mathbb {V} a r \left[ h _ {f} ^ {(t) (\nu + 1)} \right] _ {e + 1} = \frac {e \mathbb {V} a r \left[ h _ {f} ^ {(t) (\nu)} \right] _ {e} + \left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2}}{e + 1}\tag{4.40}
$$

and what will be used at test time is

$$
\mathbb {E} \left[ h _ {f} ^ {(t) (\nu)} \right] = \mathbb {E} \left[ h _ {f} ^ {(t) (\nu)} \right], \quad \mathbb {V a r} \left[ h _ {f} ^ {(t) (\nu)} \right] = \frac {T _ {\mathrm{mb}}}{T _ {\mathrm{mb}} - 1} \mathbb {V a r} \left[ h _ {f} ^ {(t) (\nu)} \right].\tag{4.41}
$$

so that at test time

$$
y _ {f} ^ {(t) (\nu)} = \gamma_ {f} ^ {(\nu)} \frac {h _ {f} ^ {(t) (\nu)} - E [ h _ {f} ^ {(t) (\nu)} ]}{\sqrt {\operatorname{Var} \left[ h _ {f} ^ {(t) (\nu)} \right] + \epsilon}} + \beta_ {f} ^ {(\nu)}.\tag{4.42}
$$

In practice, and as advocated in the original paper, on can get rid of dropout without loss of precision when using batch normalization. We will adopt this convention in the following.

<!-- page: 27 -->

## 4.9 Backpropagation

Backpropagation[9] is the standard technique to decrease the loss function error so as to correctly predict what one needs. As it name suggests, it amounts to backpropagate through the FNN the error performed at the output layer, so as to update the weights. In practice, on has to compute a bunch of gradient terms, and this can be a tedious computational task. Nevertheless, if performed correctly, this is the most useful and important task that one can do in a FN. We will therefore detail how to compute each weight (and Batchnorm coefficients) gradients in the following.

## 4.9.1 Backpropagate through Batch Normalization

Backpropagation introduces a new gradient

$$
\delta_ {f ^ {\prime}} ^ {f} J _ {f} ^ {(t t ^ {\prime}) (\nu)} = \frac {\partial y _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}}.\tag{4.43}
$$

we show in appendix 4.C that

$$
J _ {f} ^ {(t t ^ {\prime}) (\nu)} = \tilde {\gamma} _ {f} ^ {(\nu)} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu)} \tilde {h} _ {f} ^ {(t) (\nu)}}{T _ {\mathrm{mb}}} \right].\tag{4.44}
$$

## 4.9.2 error updates

To backpropagate the loss error through the FNN, it is very useful to compute a so-called error rate

$$
\delta_ {f} ^ {(t) (\nu)} = \frac {\partial}{\partial a _ {f} ^ {(t) (\nu)}} J (\Theta),\tag{4.45}
$$

We show in Appendix 4.B that $\forall \nu \in [ 0 , N - 2 ]$

$$
\delta_ {f} ^ {(t) (\nu)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)},\tag{4.46}
$$

the value of $\delta _ { f } ^ { ( t ) \left( N - 1 \right) }$ depends on the loss used. We show also in appendix 4.A that for the MSE loss function

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - y _ {f} ^ {(t)}\right),\tag{4.47}
$$

<!-- page: 28 -->

and for the cross entropy loss function

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - \delta_ {y ^ {(t)}} ^ {f}\right).\tag{4.48}
$$

To unite the notation of chapters 4, 5 and 6, we will call

$$
\mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu + 1)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \Theta_ {f} ^ {(\nu + 1) f ^ {\prime}},\tag{4.49}
$$

so that the update rule for the error rate reads

$$
\delta_ {f} ^ {(t) (\nu)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu + 1)} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)}.\tag{4.50}
$$

## 4.9.3 Weight update

Thanks to the computation of the error rates, the derivation of the error rate is straightforward. We indeed get $\forall \nu \in [ 1 , N - 1 ]$

$$
\Delta_ {f ^ {\prime}} ^ {\Theta (\nu) f} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime \prime} = 0} ^ {F _ {\nu}} \frac {\partial \Theta_ {f ^ {\prime \prime \prime}} ^ {(\nu) f ^ {\prime \prime}}}{\partial \Theta_ {f ^ {\prime}} ^ {(\nu) f}} y _ {f ^ {\prime \prime \prime}} ^ {(t) (\nu - 1)} \delta_ {f ^ {\prime \prime}} ^ {(t) (\nu)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \delta_ {f} ^ {(t) (\nu)} y _ {f ^ {\prime}} ^ {(t) (\nu - 1)}.\tag{4.51}
$$

and

$$
\Delta_ {f ^ {\prime}} ^ {\Theta (0) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \delta_ {f} ^ {(t) (0)} h _ {f ^ {\prime}} ^ {(t) (0)}.\tag{4.52}
$$

## 4.9.4 Coefficient update

The update rule for the Batchnorm coefficient can easily be computed thanks to the error rate. It reads

$$
\Delta_ {f} ^ {\gamma (\nu)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t) (\nu + 1)}}{\partial \gamma_ {f} ^ {(i)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(\nu + 1) f ^ {\prime}} \tilde {h} _ {f} ^ {(t) (i)} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{4.53}
$$

$$
\Delta_ {f} ^ {\beta (\nu)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t) (\nu + 1)}}{\partial \beta_ {f} ^ {(i)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(\nu + 1) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{4.54}
$$

<!-- page: 29 -->

## 4.10 Which data sample to use for gradient descent?

From the beginning we have denoted $T _ { \mathrm { m b } }$ the sample of the data from which we train our model. This procedure is repeated a large number of time (each time is called an epoch). But in the literature there exists three way to sample from the data: Full-batch, Stochastic and Mini-batch gradient descent. We explicit these terms in the following sections.

## 4.10.1 Full-batch

Full-batch takes the whole training set at each epoch, such that the loss function reads

$$
J (\Theta) = \sum_ {t = 0} ^ {T _ {\mathrm{train}} - 1} J _ {\mathrm{train}} (\Theta).\tag{4.55}
$$

This choice has the advantage to be numerically stable, but it so costly in computation time that it is rarely if ever used.

## 4.10.2 Stochastic Gradient Descent (SGD)

SGD amounts to take only one exemplary of the training set at each epoch

$$
J (\Theta) = J _ {\mathrm{SGD}} (\Theta).\tag{4.56}
$$

This choice leads to faster computations, but is so numerically unstable that the most standard choice by far is Mini-batch gradient descent.

## 4.10.3 Mini-batch

Mini-batch gradient descent is a compromise between stability and time efficiency, and is the middle-ground between Full-batch and Stochastic gradient descent: $1 \ll T _ { \mathrm { m b } } \ll T _ { \mathrm { t r a i n } }$ . Hence

$$
J (\Theta) = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} J _ {\mathrm{mb}} (\Theta).\tag{4.57}
$$

All the calculations in this note have been performed using this gradient descent technique.

<!-- page: 30 -->

## 4.11 Gradient optimization techniques

Once the gradients for backpropagation have been computed, the question of how to add them to the existing weights arise. The most natural choice would be to take

$$
\Theta_ {f ^ {\prime}} ^ {(\nu) f} = \Theta_ {f ^ {\prime}} ^ {(\nu) f} - \eta \Delta_ {f ^ {\prime}} ^ {\Theta (i) f}.\tag{4.58}
$$

where $\eta$ is a free parameter that is generally initialized thanks to cross-validation. It can also be made epoch dependent (with usually a slow exponentially decaying behaviour). When using Mini-batch gradient descent, this update choice for the weights presents the risk of having the loss function being stuck in a local minimum. Several method have been invented to prevent this risk. We are going to review them in the next sections.

## 4.11.1 Momentum

Momentum[10] introduces a new vector $v _ { \mathrm { e } }$ and can be seen as keeping a memory of what where the previous updates at prior epochs. Calling e the number of epochs and forgetting the $f , f ^ { \prime } , \nu$ indices for the gradients to ease the notations, we have

$$
v _ {\mathrm{e}} = \gamma v _ {\mathrm{e-1}} + \eta \Delta^ {\Theta},\tag{4.59}
$$

and the weights at epoch e are then updated as

$$
\Theta_ {e} = \Theta_ {e - 1} - v _ {\mathrm{e}}.\tag{4.60}
$$

$\gamma$ is a new parameter of the model, that is usually set to 0.9 but that could also be fixed thanks to cross-validation.

## 4.11.2 Nesterov accelerated gradient

Nesterov accelerated gradient[11] is a slight modification of the momentum technique that allows the gradients to escape from local minima. It amounts to take

$$
v _ {\mathrm{e}} = \gamma v _ {\mathrm{e-1}} + \eta \Delta^ {\Theta - \gamma v _ {\mathrm{e-1}}},\tag{4.61}
$$

and then again

$$
\Theta_ {e} = \Theta_ {e - 1} - v _ {\mathrm{e}}.\tag{4.62}
$$

Until now, the parameter $\eta$ that controls the magnitude of the update has been set globally. It would be nice to have a fine control of $\mathbf { i } \mathbf { t } ,$ so that different weights can be updated with different magnitudes.

<!-- page: 31 -->

## 4.11.3 Adagrad

Adagrad[12] allows to fine tune the different gradients by having individual learning rates η. Calling for each value of $f , f ^ { \prime } ,$ i

$$
v _ {\mathrm{e}} = \sum_ {e ^ {\prime} = 0} ^ {e - 1} \left(\Delta_ {e ^ {\prime}} ^ {\Theta}\right) ^ {2},\tag{4.63}
$$

the update rule then reads

$$
\Theta_ {e} = \Theta_ {e - 1} - \frac {\eta}{\sqrt {v _ {\mathrm{e}} + \epsilon}} \Delta_ {e} ^ {\Theta}.\tag{4.64}
$$

One advantage of Adagrad is that the learning rate η can be set once and for all (usually to $1 0 ^ { - 2 } )$ and does not need to be fine tune via cross validation anymore, as it is individually adapted to each weight via the $v _ { \mathrm { e } }$ term. e is here to avoid division by 0 issues, and is usually set to ${ \mathrm { 1 0 ^ { - 8 } } }$

## 4.11.4 RMSprop

Since in Adagrad one adds the gradient from the first epoch, the weight are forced to monotonically decrease. This behaviour can be smoothed via the Adadelta technique, which takes

$$
v _ {\mathrm{e}} = \gamma v _ {\mathrm{e-1}} + (1 - \gamma) \Delta_ {e} ^ {\Theta},\tag{4.65}
$$

with $\gamma$ a new parameter of the model, that is usually set to 0.9. The Adadelta update rule then reads as the Adagrad one

$$
\Theta_ {e} = \Theta_ {e - 1} - \frac {\eta}{\sqrt {v _ {\mathrm{e}} + \epsilon}} \Delta_ {e} ^ {\Theta}.\tag{4.66}
$$

η can be set once and for all (usually to 10− $^ { - 3 } )$ .

## 4.11.5 Adadelta

Adadelta[13] is an extension of RMSprop, that aims at getting rid of the η parameter. To do so, a new vector update is introduced

$$
m _ {\mathrm{e}} = \gamma m _ {\mathrm{e-1}} + (1 - \gamma) \left(\frac {\sqrt {m _ {\mathrm{e-1}} + \epsilon}}{\sqrt {v _ {\mathrm{e}} + \epsilon}} \Delta_ {e} ^ {\Theta}\right) ^ {2},\tag{4.67}
$$

<!-- page: 32 -->

and the new update rule for the weights reads

$$
\Theta_ {e} = \Theta_ {e - 1} - \frac {\sqrt {m _ {\mathrm{e-1}} + \epsilon}}{\sqrt {v _ {\mathrm{e}} + \epsilon}} \Delta_ {e} ^ {\Theta}.\tag{4.68}
$$

The learning rate has been completely eliminated from the update rule, but the procedure for doing so is ad hoc. The next and last optimization technique presented seems more natural and is the default choice on a number of deep learning algorithms.

## 4.11.6 Adam

Adam[14] keeps track of both the gradient and its square via two epoch dependent vectors

$$
m _ {\mathrm{e}} = \beta_ {1} m _ {\mathrm{e-1}} + (1 - \beta_ {1}) \Delta_ {e} ^ {\Theta}, \qquad v _ {\mathrm{e}} = \beta_ {2} v _ {\mathrm{e}} + (1 - \beta_ {2}) \left(\Delta_ {e} ^ {\Theta}\right) ^ {2},\tag{4.69}
$$

with $\beta _ { 1 }$ and $\beta _ { 2 }$ parameters usually respectively set to 0.9 and 0.999. But the robustness and great strength of Adam is that it makes the whole learning process weakly dependent of their precise value. To avoid numerical problems during the first steps, these vector are rescaled

$$
\hat {m} _ {\mathrm{e}} = \frac {m _ {\mathrm{e}}}{1 - \beta_ {1} ^ {e}}, \quad \hat {v} _ {\mathrm{e}} = \frac {v _ {\mathrm{e}}}{1 - \beta_ {2} ^ {e}}.\tag{4.70}
$$

before entering into the update rule

$$
\Theta_ {e} = \Theta_ {e - 1} - \frac {\eta}{\sqrt {\hat {v} _ {\mathrm{e}} + \epsilon}} \hat {m} _ {\mathrm{e}}.\tag{4.71}
$$

This is the optimization technique implicitly used throughout this note, alongside with a learning rate decay

$$
\eta_ {e} = e ^ {- \alpha_ {0}} \eta_ {e - 1},\tag{4.72}
$$

$\alpha _ { 0 }$ determined by cross-validation, and $\eta _ { 0 }$ usually initialized in the range $1 0 ^ { - 3 }$ $1 0 ^ { - 2 }$

## 4.12 Weight initialization

Without any regularization, training a neural network can be a daunting task because of the fine-tuning of the weight initial conditions. This is one

<!-- page: 33 -->

of the reasons why neural networks have experienced out of mode periods. Since dropout and Batch normalization, this issue is less pronounced, but one should not initialize the weight in a symmetric fashion (all zero for instance), nor should one initialize them too large. A good heuristic is

$$
\left[ \Theta_ {f} ^ {(\nu) f ^ {\prime}} \right] _ {\mathrm{init}} = \sqrt {\frac {6}{F _ {i} + F _ {i + 1}}} \times \mathcal {N} (0, 1).\tag{4.73}
$$

## Appendix

## 4.A Backprop through the output layer

Recalling the MSE loss function

$$
J (\Theta) = \frac {1}{2 T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f = 0} ^ {F _ {\mathrm{N}} - 1} \left(y _ {f} ^ {(t)} - h _ {f} ^ {(t) (N)}\right) ^ {2},\tag{4.74}
$$

we instantaneously get

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - y _ {f} ^ {(t)}\right).\tag{4.75}
$$

Things are more complicated for the cross-entropy loss function of a regression problem transformed into a multi-classification task. Assuming that we have C classes for all the values that we are trying to predict, we get

$$
\delta_ {f c} ^ {(t) (N - 1)} = \frac {\partial}{\partial a _ {f c} ^ {(t) (N - 1)}} J (\Theta) = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {N} - 1} \sum_ {d = 0} ^ {C - 1} \frac {\partial h _ {f ^ {\prime} d} ^ {(t ^ {\prime}) (N)}}{\partial a _ {f c} ^ {(t) (N - 1)}} \frac {\partial}{\partial h _ {f ^ {\prime} d} ^ {(t ^ {\prime}) (N)}} J (\Theta).\tag{4.76}
$$

Now

$$
\frac {\partial}{\partial h _ {f ^ {\prime} d} ^ {(t ^ {\prime}) (N)}} J (\Theta) = - \frac {\delta_ {y _ {f ^ {\prime}} ^ {(t ^ {\prime})}} ^ {d}}{T _ {\mathrm{mb}} h _ {f ^ {\prime} d} ^ {(t ^ {\prime}) (N)}},\tag{4.77}
$$

and

$$
\frac {\partial h _ {f ^ {\prime} d} ^ {(t ^ {\prime}) (N)}}{\partial a _ {f c} ^ {(t) (N - 1)}} = \delta_ {f ^ {\prime}} ^ {f} \delta_ {t ^ {\prime}} ^ {t} \left(\delta_ {d} ^ {c} h _ {f c} ^ {(t) (N)} - h _ {f c} ^ {(t) (N)} h _ {f d} ^ {(t) (N)}\right),\tag{4.78}
$$

<!-- page: 34 -->

so that

$$
\begin{array}{c} \delta_ {f c} ^ {(t) (N - 1)} = - \frac {1}{T _ {\mathrm{mb}}} \sum_ {d = 0} ^ {C - 1} \frac {\delta_ {y _ {f} ^ {(t)}} ^ {d}}{h _ {f d} ^ {(t) (N)}} \left(\delta_ {d} ^ {c} h _ {f c} ^ {(t) (N)} - h _ {f c} ^ {(t) (N)} h _ {f d} ^ {(t) (N)}\right) \\ = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f c} ^ {(t) (N)} - \delta_ {y _ {f} ^ {(t)}} ^ {c}\right). \end{array}\tag{4.79}
$$

For a true classification problem, we easily deduce

$$
\delta_ {f c} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - \delta_ {y ^ {(t)}} ^ {f}\right).\tag{4.80}
$$

## 4.B Backprop through hidden layers

To go further we need

$$
\begin{array}{l} \delta_ {f} ^ {(t) (\nu)} = \frac {\partial}{\partial a _ {f} ^ {(t) (\nu)}} J ^ {(t)} (\Theta) = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f} ^ {(t) (\nu)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu}} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 1) f ^ {\prime}} \frac {\partial y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial a _ {f} ^ {(t) (\nu)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\parallel} = 0} ^ {F _ {\nu}} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 1) f ^ {\prime}} \frac {\partial y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}, \end{array}\tag{4.81}
$$

so that

$$
\delta_ {f} ^ {(t) (\nu)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{4.82}
$$

## 4.C Backprop through BatchNorm

We saw in section 4.9.1 that batch normalization implies among other things to compute the following gradient.

$$
\frac {\partial y _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \gamma_ {f} ^ {(\nu)} \frac {\partial \tilde {h} _ {f ^ {\prime}} ^ {(t) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}}.\tag{4.83}
$$

<!-- page: 35 -->

We propose to do just that in this section. Firstly

$$
\frac {\partial h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \delta_ {t} ^ {t ^ {\prime}} \delta_ {f} ^ {f ^ {\prime}}, \quad \frac {\partial \hat {h} _ {f ^ {\prime}} ^ {(\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}}.\tag{4.84}
$$

Secondly

$$
\frac {\partial \left(\hat {\sigma} _ {f ^ {\prime}} ^ {(\nu)}\right) ^ {2}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \frac {2 \delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (\nu + 1)} - \hat {h} _ {f} ^ {(\nu)}\right),\tag{4.85}
$$

so that we get

$$
\begin{array}{l} \frac {\partial \tilde {h} _ {f ^ {\prime}} ^ {(t) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}} \left[ \frac {T _ {\mathrm{mb}} \delta_ {t} ^ {t ^ {\prime}} - 1}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} - \frac {\left(h _ {f} ^ {(t ^ {\prime}) (\nu + 1)} - \hat {h} _ {f} ^ {(\nu)}\right) \left(h _ {f} ^ {(t) (\nu + 1)} - \hat {h} _ {f} ^ {(\nu)}\right)}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} + \epsilon\right) ^ {\frac {3}{2}}} \right] \\ = \frac {\delta_ {f} ^ {f ^ {\prime}}}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu)} \tilde {h} _ {f} ^ {(t) (\nu)}}{T _ {\mathrm{mb}}} \right]. \end{array} \tag {4.8}\tag{4.86}
$$

To ease the notation recall that we denoted

$$
\tilde {\gamma} _ {f} ^ {(\nu)} = \frac {\gamma_ {f} ^ {(\nu)}}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}}.\tag{4.87}
$$

so that

$$
\frac {\partial y _ {f ^ {\prime}} ^ {(t) (\nu)}}{\partial h _ {f} ^ {(t) (\nu + 1)}} = \tilde {\gamma} _ {f} ^ {(\nu)} \delta_ {f} ^ {f ^ {\prime}} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu)} \tilde {h} _ {f} ^ {(t) (\nu)}}{T _ {\mathrm{mb}}} \right].\tag{4.88}
$$

## 4.D FNN ResNet (non standard presentation)

The state of the art architecture of convolutional neural networks $( \mathrm { C N N } ,$ to be explained in chapter 5) is called ResNet[5]. Its name comes from its philosophy: each hidden layer output y of the network is a small – hence the

<!-- page: 36 -->

term residual – modification of its input $( y   =   x + F ( x ) )$ , instead of a total modification $( y   =   H ( x ) )$ of its input x. This philosophy can be imported to the FNN case. Representing the operations of weight averaging, activation function and batch normalization in the following way

![](images/page_35_image_3.jpg)

Figure 4.9: Schematic representation of one FNN fully connected layer.

In its non standard form presented in this section, the residual operation amounts to add a skip connection to two consecutive full layers

![](images/page_35_image_6.jpg)

Figure 4.10: Residual connection in a FNN.

Mathematically, we had before (calling the input $y ^ { ( t ) ( \nu - 1 ) } )$

$$
\begin{array}{c} y _ {f} ^ {(t) (\nu + 1)} = \gamma_ {f} ^ {(\nu + 1)} \tilde {h} _ {f} ^ {(t) (\nu + 2)} + \beta_ {f} ^ {(\nu + 1)}, a _ {f} ^ {(t) (\nu + 1)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu + 1) f} y _ {f} ^ {(t) (\nu)} \\ y _ {f} ^ {(t) (\nu)} = \gamma_ {f} ^ {(\nu)} \tilde {h} _ {f} ^ {(t) (\nu + 1)} + \beta_ {f} ^ {(\nu)}, a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} y _ {f} ^ {(t) (\nu - 1)}, \end{array}\tag{4.89}
$$

as well as $h _ { f } ^ { \left( t \right) \left( \nu + 2 \right) }   =   g \left( a _ { f } ^ { \left( t \right) \left( \nu + 1 \right) } \right)$ and $h _ { f } ^ { \left( t \right) \left( \nu + 1 \right) }   =   g \left( a _ { f } ^ { \left( t \right) \left( \nu \right) } \right)$ . In ResNet, we now have the slight modification

$$
y _ {f} ^ {(t) (\nu + 1)} = \gamma_ {f} ^ {(\nu + 1)} \tilde {h} _ {f} ^ {\nu + 2} + \beta_ {f} ^ {(\nu + 1)} + y _ {f} ^ {(t) (\nu - 1)}.\tag{4.90}
$$

The choice of skipping two and not just one layer has become a standard for empirical reasons, so as the decision not to weight the two paths (the trivial

<!-- page: 37 -->

skip one and the two FNN layer one) by a parameter to be learned by backpropagation

$$
y _ {f} ^ {(t) (\nu + 1)} = \alpha \left(\gamma_ {f} ^ {(\nu + 1)} \tilde {h} _ {f} ^ {(t) (\nu + 2)} + \beta_ {f} ^ {(\nu + 1)}\right) + (1 - \alpha) y _ {f ^ {\prime}} ^ {(t) (\nu - 1)}.\tag{4.91}
$$

This choice is called highway nets[15], and it remains to be theoretically understood why it leads to worse performance than ResNet, as the latter is a particular instance of the former. Going back to the ResNet backpropagation algorithm, this changes the gradient through the skip connection in the following way

$$
\begin{array}{l} \delta_ {f} ^ {(t) (\nu - 1)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial a _ {f} ^ {(t) (\nu - 1)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)} + \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 2} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 2)}}{\partial a _ {f} ^ {(t) (\nu - 1)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 2)} \\ \qquad = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu) f ^ {\prime}} \frac {\partial y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (\nu - 1)}}{\partial a _ {f} ^ {(t) (\nu - 1)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)} \\ \qquad + \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 2} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 2) f ^ {\prime}} \frac {\partial y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f} ^ {(t) (\nu - 1)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 2)} \\ \qquad = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu - 1)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu) f ^ {\prime}}, \\ \qquad + g ^ {\prime} \left(a _ {f} ^ {(t) (\nu - 1)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 2} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 3) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)}, \end{array}\tag{4.92}
$$

so that

$$
\begin{array}{l} \delta_ {f} ^ {(t) (\nu - 1)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu - 1)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu - 1} - 1} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \\ \qquad \times \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 2} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 2) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 2)} \right]. \end{array}\tag{4.93}
$$

This formulation has one advantage: it totally preserves the usual FNN layer structure of a weight averaging (WA) followed by an activation function (AF) and then a batch normalization operation (BN). It nevertheless has one disadvantage: the backpropagation gradient does not really flow smoothly from one error rate to the other. In the following section we will present the standard ResNet formulation of that takes the problem the other way around: it allows the gradient to flow smoothly at the cost of "breaking" the natural FNN building block.

<!-- page: 38 -->

## 4.E FNN ResNet (more standard presentation)

![](images/page_37_image_3.jpg)

Figure 4.11: Residual connection in a FNN, trivial gradient flow through error rates.

In the more standard form of ResNet, the skip connections reads

$$
a _ {f} ^ {(t) (\nu + 2)} = a _ {f} ^ {(t) (\nu + 2)} + a _ {f} ^ {(t) (\nu)},\tag{4.94}
$$

and the updated error rate reads

$$
\delta_ {f} ^ {(t) (\nu)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} J _ {f} ^ {(t t ^ {\prime}) (\nu)} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {(\nu + 1) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} + \delta_ {f} ^ {(t ^ {\prime}) (\nu + 2)}.\tag{4.95}
$$

## 4.F Matrix formulation

In all this chapter, we adopted an "index" formulation of the FNN. This has upsides and downsides. On the positive side, one can take the formula as written here and $\mathbf { g } \mathbf { o }$ implement them. On the downside, they can be quite cumbersome to read.

Another FNN formulation is therefore possible: a matrix one. To do so, one has to rewrite

$$
h _ {f} ^ {(t) (\nu)} \mapsto h _ {f t} ^ {(\nu)} \mapsto h ^ {(\nu)} \in \mathcal {M} (F _ {\nu}, T _ {\mathrm{mb}}).\tag{4.96}
$$

In this case the weight averaging procedure (4.18) can be written as

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(\nu) f} h _ {f ^ {\prime} t} ^ {(\nu)} \mapsto a ^ {(\nu)} = \Theta^ {(\nu)} h ^ {(\nu)}.\tag{4.97}
$$

<!-- page: 39 -->

The upsides and downsides of this formulation are the exact opposite of the index one: what we gained in readability, we lost in terms of direct implementation in low level programming languages (C for instance). For FNN, one can use a high level programming language (like python), but this will get quite intractable when we talk about Convolutional networks. Since the whole point of the present work was to introduce the index notation, and as one can easily find numerous derivation of the backpropagation update rules in matrix form, we will stick with the index notation in all the following, and now turn our attention to convolutional networks.

<!-- page: 40 -->

<!-- page: 41 -->

## Chapter 5

## Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F Convolutional Neural Networks Input Convolution Layer . . . N + 2PT + 2P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

## Contents

- 5.1 Introduction 42
- 5.2 CNN architecture 43
- 5.3 CNN specificities 43
- 5.3.1 Feature map 43
- 5.3.2 Input layer 43
- 5.3.3 Padding 44
- 5.3.4 Convolution 45
- 5.3.5 Pooling 47
- 5.3.6 Towards fully connected layers 48
- 5.3.7 fully connected layers 48
- 5.3.8 Output connected layer 49
- 5.4 Modification to Batch Normalization 49
- 5.5 Network architectures 50
- 5.5.1 Realistic architectures 51
- 5.5.2 LeNet 52
- 5.5.3 AlexNet 52
- 5.5.4 VGG 53
- 5.5.5 GoogleNet 53
- 5.5.6 ResNet 54
- 5.6 Backpropagation 56

<!-- page: 42 -->

- 5.6.1 Backpropagate through Batch Normalization 57
- 5.6.2 Error updates 57
- 5.6.3 Weight update 60
- 5.6.4 Coefficient update 62
- Appendices 64
- 5.A Backprop through BatchNorm 64
- 5.B Error rate updates: details 65
- 5.C Weight update: details 67
- 5.D Coefficient update: details 68
- 5.E Practical Simplification 68
- 5.E.1 pool to conv Simplification 69
- 5.E.2 Convolution Simplification 70
- 5.E.3 Coefficient Simplification 71
- 5.F Batchpropagation through a ResNet module 71
- 5.G Convolution as a matrix multiplication 72
- 5.G.1 2D Convolution 73
- 5.G.2 4D Convolution 74
- 5.H Pooling as a row matrix maximum 75

## 5.1 Introduction

![](images/page_41_image_4.jpg)

n this chapter we review a second type of neural network that is I presumably the most popular one: Convolutional Neural Networks (CNN). CNN are particularly adapted for image classification, be it numbers or animal/car/... category. We will review the novelty involved when dealing with CNN when compared to FNN. Among them are the fundamental building blocks of CNN: convolution and pooling. We will in addition see what modification have to be taken into account for the regularization techniques introduced in the FNN part. Finally, we will present the most common CNN architectures that are used in the literature: from LeNet to ResNet.

<!-- page: 43 -->

## 5.2 CNN architecture

A CNN is formed by several convolution and pooling operations, usually followed by one or more fully connected layers (those being similar to the traditional FNN layers). We will clarify the new terms introduced thus far in the following sections.

![](images/page_42_image_4.jpg)

Figure 5.1: A typical CNN architecture (in this case LeNet inspired): convolution operations are followed by pooling operations, until the size of each feature map is reduced to one. Fully connected layers can then be introduced.

## 5.3 CNN specificities

## 5.3.1 Feature map

In each layer of a CNN, the data are no longer labeled by a single index as in a FNN. One should see the FNN index as equivalent to the label of a given image in a layer of a CNN. This label is the feature map. In each feature map $\left[ f \in \left[ 0 , \dot { F _ { \nu } } - 1 \right] \right]$ of the ν’th layer, the image is fully characterized by two additional indices corresponding to its height $\tilde { k } \in T _ { \nu } - \tilde { 1 }$ and its width $j \in N _ { \nu } - 1$ . A given $f , j , k$ thus characterizes a unique pixel of a given feature map. Let us now review the different layers of a CNN

## 5.3.2 Input layer

We will be considering a input of $F _ { 0 }$ channels. In the standard image treatment, these channels can correspond to the RGB colors $( F _ { 0 } = 3 )$ . Each image in each channel will be of size $\bar { N } _ { 0 } \times T _ { 0 }$ (width×height). The input will be denoted $X _ { f j k ^ { \prime } } ^ { ( t ) }$ with $t   \in   [ [ 0 , T _ { \mathrm { m b } } - 1 ] ]$ (size of the Mini-batch set, see chapter 4), $j \in [ 0 , \dot { N _ { 0 } } - 1 ]$ and $k \in [ 0 , T _ { 0 } - 1 ]$ A standard input treatment is to center the

<!-- page: 44 -->

data following either one of the two following procedure

$$
\tilde {X} _ {f j k} ^ {(t)} = X _ {i j k} ^ {(t)} - \mu_ {f}, \quad \tilde {X} _ {f j k} ^ {(t)} = X _ {i j k} ^ {(t)} - \mu_ {f j k}\tag{5.1}
$$

with

$$
\mu_ {f} = \frac {1}{T _ {\mathrm{train}} T _ {0} N _ {0}} \sum_ {t = 0} ^ {T _ {\mathrm{train}} - 1} \sum_ {j} ^ {N _ {0} - 1} \sum_ {k} ^ {T _ {0} - 1} X _ {f j k} ^ {(t)},\tag{5.2}
$$

$$
\mu_ {f j k} = \frac {1}{T _ {\mathrm{train}}} \sum_ {t = 0} ^ {T _ {\mathrm{train}} - 1} X _ {f j k} ^ {(t)}.\tag{5.3}
$$

This correspond to either compute the mean per pixel over the training set, or to also average over every pixel. This procedure should not be followed for regression tasks. To conclude, figure 5.2 shows what the input layer looks like.

![](images/page_43_chart_8.jpg)

Figure 5.2: The Input layer

## 5.3.3 Padding

As we will see when we proceed, it may be convenient to "pad" the feature maps in order to preserve the width and the height of the images though several hidden layers. The padding operation amounts to add 0’s around the original image. With a padding of size $P ,$ we add P zeros at the beginning of each row and column of a given feature map. This is illustrated in the following figure

<!-- page: 45 -->

![](images/page_44_chart_2.jpg)

Figure 5.3: Padding of the feature maps. The zeros added correspond to the red tiles, hence a padding of size $P = \bar { 1 }$

## 5.3.4 Convolution

The convolution operation that gives its name to the CNN is the fundamental building block of this type of network. It amounts to convolute a feature map of an input hidden layer with a weight matrix to give rise to an output feature map. The weight is really a four dimensional tensor, one dimension (F) being the number of feature maps of the convolutional input layer, another $( F _ { p } )$ the number of feature maps of the convolutional output layer. The two others gives the size of the receptive field in the width and the height direction. The receptive field allows one to convolute a subset instead of the whole input image. It aims at searching similar patterns in the input image, no matter where the pattern is (translational invariance). The width and the height of the output image are also determined by the stride: it is simply the number of pixel by which one slides in the vertical and/or the horizontal direction before applying again the convolution operation. A good picture being worth a thousand words, here is the convolution operation in a nutshell

<!-- page: 46 -->

![](images/page_45_image_2.jpg)

Figure 5.4: The convolution operation

Here $R _ { C }$ is the size of the convolutional receptive field (we will see that the pooling operation also has a receptive field and a stride) and $S _ { C }$ the convolutional stride. The widths and heights of the output image can be computed thanks to the input height T and output width N

$$
N _ {p} = \frac {N + 2 P - R _ {C}}{S _ {C}} + 1, \quad T _ {p} = \frac {T + 2 P - R _ {C}}{S _ {C}} + 1.\tag{5.4}
$$

It is common to introduce a padding to preserve the widths and heights of the input image $N = N _ { p } = T = \bar { T } _ { p } ,$ so that in these cases $S _ { C } = 1$ and

$$
P = \frac {R _ {C} - 1}{2}.\tag{5.5}
$$

For a given layer $n ,$ the convolution operation mathematically reads (similar in spirit to the weight averaging procedure of a FNN)

$$
a _ {f l m} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(o) f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (\nu)},\tag{5.6}
$$

where o characterizes the $o + 1$ convolution in the network. Here ν denotes the $\nu \mathrm { t h }$ hidden layer of the network (and thus belongs to $[ 0 , N - 1 ] )$ , and $f   \in   [ 0 , F _ { \nu + 1 } - 1 ] , \; \dot { l }   \in   [ 0 , N _ { \nu + 1 } - 1 ]$ and $m \; \in \; [ [ 0 , T _ { \nu + 1 } \stackrel { \cdot } { - } 1 ] ]$ Thus $S _ { C } l + j   \in$ $\left[ 0 , N _ { \nu } - 1 \right]$ and $S _ { C } l + j \in \left[ \left[ 0 , T _ { \nu } - 1 \right] \right]$ One then obtains the hidden units via a ReLU (or other, see chapter 4) activation function application. Taking padding into account, it reads

$$
h _ {f l + P m + P} ^ {(t) (\nu + 1)} = g \left(a _ {f l m} ^ {(t) (\nu)}\right)  .\tag{5.7}
$$

<!-- page: 47 -->

## 5.3.5 Pooling

The pooling operation, less and less used in the current state of the art CNN, is fundamentally a dimension reduction operation. It amounts either to average or to take the maximum of a sub-image – characterized by a pooling receptive field $R _ { P }$ and a stride $S _ { P } \mathrm { ~ - ~ }$ of the input feature map F to obtain an output feature map $F _ { p } = F$ of width $N _ { p } < N$ and height $T _ { p } \stackrel { \_ } { < } T$ . To be noted: the padded values of the input hidden layers are not taken into account during the pooling operation (hence the +P indices in the following formulas)

![](images/page_46_image_4.jpg)

Figure 5.5: The pooling operation

The average pooling procedure reads for a given ν’th pooling operation

$$
a _ {f l m} ^ {(t) (\nu)} = \sum_ {j, k = 0} ^ {R _ {P} - 1} h _ {f S _ {P} l + j + P S _ {P} m + k + P} ^ {(t) (\nu)},\tag{5.8}
$$

while the max pooling reads

$$
a _ {f l m} ^ {(t) (\nu)} = \max _ {j, k = 0} ^ {R _ {P} - 1} h _ {f S _ {P} l + j + P S _ {P} m + k + P} ^ {(t) (\nu)}.\tag{5.9}
$$

Here ν denotes the $\nu \mathrm { t h }$ hidden layer of the network (and thus belongs to $[ 0 , N - 1 ] )$ , and $f \; \in \; [ 0 , F _ { \nu + 1 } - 1 ] , \; \dot { l } \; \in \; [ 0 , N _ { \nu + 1 } - 1 ]$ and $m \; \in \; [ [ 0 , T _ { \nu + 1 } \stackrel { \cdot } { - } 1 ] ]$ Thus $S _ { P } l + j   \in   [ [ 0 , N _ { \nu } - 1 ] ]$ and $S _ { P } l + j   \in   [ [ 0 , T _ { \nu } - 1 ] ]$ Max pooling is extensively used in the literature, and we will therefore adopt it in all the following. Denoting $j _ { f l m } ^ { \left( t \right) \left( p \right) } ,   k _ { f l m } ^ { \left( t \right) \left( p \right) }$ the indices at which the $l ,$ m maximum of the f feature map of the t’th batch sample is reached, we have

$$
h _ {f l + P m + P} ^ {(t) (\nu + 1)} = a _ {f l m} ^ {(t) (\nu)} = h _ {f S _ {P} l + j _ {f l m} ^ {(t) (p)} + P S _ {P} m + k _ {f l m} ^ {(t) (p)} + P} ^ {(t) (\nu)}.\tag{5.10}
$$

<!-- page: 48 -->

## 5.3.6 Towards fully connected layers

At some point in a CNN the convolutional receptive field is equal to the width and the height of the input image. In this case, the convolution operation becomes a kind of weight averaging procedure (as in a FNN)

![](images/page_47_image_4.jpg)

Figure 5.6: Fully connected operation to get images of width and height 1.

This weight averaging procedure reads

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sum_ {l = 0} ^ {N - 1} \sum_ {m = 0} ^ {T - 1} \Theta_ {f ^ {\prime} l m} ^ {(o) f} h _ {f ^ {\prime} l + P m + P} ^ {(t) (\nu)},\tag{5.11}
$$

and is followed by the activation function

$$
h _ {f} ^ {(t) (\nu + 1)} = g \left(a _ {f} ^ {(t) (\nu)}\right),\tag{5.12}
$$

## 5.3.7 fully connected layers

After the previous operation, the remaining network is just a FNN one. The weigh averaging procedure reads

$$
a _ {f} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {(o) f} h _ {f ^ {\prime}} ^ {(t) (\nu)},\tag{5.13}
$$

and is followed as usual by the activation function

$$
h _ {f} ^ {(t) (\nu + 1)} = g \left(a _ {f} ^ {(t) (\nu)}\right),\tag{5.14}
$$

<!-- page: 49 -->

![](images/page_48_image_2.jpg)

Figure 5.7: Fully connected operation, identical to the FNN operations.

## 5.3.8 Output connected layer

Finally, the output is computed as in a FNN

$$
a _ {f} ^ {(t) (N - 1)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {N} - 1} \Theta_ {f ^ {\prime}} ^ {(o) f} h _ {f ^ {\prime}} ^ {(t) (N - 1)}, \qquad h _ {f} ^ {(t) (N)} = o \left(a _ {f} ^ {(t) (N - 1)}\right),\tag{5.15}
$$

where as in a FNN, o is either the L2 or the cross-entropy loss function (see chapter 4).

## 5.4 Modification to Batch Normalization

In a CNN, Batch normalization is modified in the following way (here, contrary to a regular FNN, not all the hidden layers need to be Batch normalized. Indeed this operation is not performed on the output of the pooling layers. We will hence use different names ν and n for the regular and batch normalized hidden layers)

$$
\tilde {h} _ {f l m} ^ {(t) (n)} = \frac {h _ {f l m} ^ {(t) (\nu)} - \hat {h} _ {f} ^ {(n)}}{\sqrt {\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} + \epsilon}},\tag{5.16}
$$

<!-- page: 50 -->

with

$$
\hat {h} _ {f} ^ {(n)} = \frac {1}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {n} - 1} \sum_ {m = 0} ^ {T _ {n} - 1} h _ {f l m} ^ {(t) (\nu)}\tag{5.17}
$$

$$
\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} = \frac {1}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {n} - 1} \sum_ {m = 0} ^ {T _ {n} - 1} \left(h _ {f l m} ^ {(t) (\nu)} - \hat {h} _ {f} ^ {(n)}\right) ^ {2}.\tag{5.18}
$$

The identity transform can be implemented thanks to the two additional parameters $( \gamma _ { f } , \beta _ { f } )$

$$
y _ {f l m} ^ {(t) (n)} = \gamma_ {f} ^ {(n)} \tilde {h} _ {f l m} ^ {(t) (n)} + \beta_ {f} ^ {(n)}.\tag{5.19}
$$

For the evaluation of the cross-validation and the test set (calling e the number of iterations/epochs), one has to compute

$$
\mathbb {E} \left[ h _ {f l m} ^ {(t) (\nu)} \right] _ {e + 1} = \frac {e \mathbb {E} \left[ h _ {f l m} ^ {(t) (\nu)} \right] _ {e} + \hat {h} _ {f} ^ {(n)}}{e + 1},\tag{5.20}
$$

$$
\mathbb {V} a r \left[ h _ {f l m} ^ {(t) (\nu)} \right] _ {e + 1} = \frac {i \mathbb {V} a r \left[ h _ {f l m} ^ {(t) (\nu)} \right] _ {e} + \left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2}}{e + 1}\tag{5.21}
$$

and what will be used at test time is E $\left[ h _ { f l   m } ^ { ( t ) ( \nu ) } \right]$ and $\begin{array} { r } { \frac { T _ { \mathrm { m b } } } { T _ { \mathrm { m b } } - 1 } \mathbf { V } a r \left[ h _ { f l   m } ^ { ( t ) ( \nu ) } \right] } \end{array}$

## 5.5 Network architectures

We will now review the standard CNN architectures that have been used in the literature in the past 20 years, from old to very recent (end of 2015) ones. To allow for an easy graphical representation, we will adopt the following schematic representation of the different layers.

<!-- page: 51 -->

![](images/page_50_image_2.jpg)

Figure 5.8: Schematic representation of the different layer

## 5.5.1 Realistic architectures

In realistic architectures, every fully connected layer (except the last one related to the output) is followed by a ReLU (or other) activation and then a batch normalization step (these two data processing steps can be inverted, as it was the case in the original BN implementation).

![](images/page_50_image_6.jpg)

Figure 5.9: Realistic Fully connected operation

The same holds for convolutional layers

![](images/page_50_image_9.jpg)

Figure 5.10: Realistic Convolution operation

<!-- page: 52 -->

We will adopt the simplified right hand side representation, keeping in mind that the true structure of a CNN is richer. With this in mind – and mentioning in passing [16] that details recent CNN advances, let us now turn to the first popular CNN used by the deep learning community.

## 5.5.2 LeNet

The LeNet[3] (end of the 90’s) network is formed by an input, followed by two conv-pool layers and then a fully-connected layer before the final output. It can be seen in figure 5.1

![](images/page_51_image_5.jpg)

Figure 5.11: The LeNet CNN

When treating large images (224 × 224), this implies to use large size of receptive fields and strides. This has two downsides. Firstly, the number or parameter in a given weight matrix is proportional to the size of the receptive field, hence the larger it is the larger the number of parameter. The network can thus be more prone to overfit. Second, a large stride and receptive field means a less subtle analysis of the fine structures of the images. All the subsequent CNN implementations aim at reducing one of these two issues.

## 5.5.3 AlexNet

The AlexNet[17] (2012) saw no qualitative leap in the CNN theory, but due to better processors was able to deal with more hidden layers.

![](images/page_51_image_10.jpg)

Figure 5.12: The AlexNet CNN

<!-- page: 53 -->

This network is still commonly used, though less since the arrival of the VGG network.

## 5.5.4 VGG

The VGG[4] network (2014) adopted a simple criteria: only 2 × 2 paddings of stride 2 and 3 × 3 convolutions of stride 1 with a padding of size 1, hence preserving the size of the image’s width and height through the convolution operations.

![](images/page_52_image_5.jpg)

Figure 5.13: The VGG CNN

This network is the standard one in most of the deep learning packages dealing with CNN. It is no longer the state of the art though, as a design innovation has taken place since its creation.

## 5.5.5 GoogleNet

The GoogleNet[18] introduced a new type of "layer" (which is in reality a combination of existing layers): the inception layer (in reference to the movie by Christopher Nolan). Instead of passing from one layer of a CNN to the next by a simple pool, conv or fully-connected (fc) operation, one averages the result of the following architecture.

![](images/page_52_image_10.jpg)

Figure 5.14: The Inception module

<!-- page: 54 -->

We won’t enter into the details of the concat layer, as the Google Net illustrated on the following figure is (already!) no longer state of the art.

![](images/page_53_image_3.jpg)

Figure 5.15: The GoogleNet CNN

Indeed, the idea of averaging the result of several conv-pool operations to obtain the next hidden layer of a CNN as been exploited but greatly simplified by the state of the art CNN : The ResNet.

## 5.5.6 ResNet

![](images/page_53_image_7.jpg)

Figure 5.16: The Bottleneck Residual architecture. Schematic representation on the left, realistic one on the right. It amounts to a 1 × 1 conv of stride 1 and padding 0, then a standard VGG conv and again a 1 × 1 conv. Two main modifications in our presentation of ResNet: BN operations have been put after ReLU ones, and the final ReLU is before the plus operation.

The ResNet[5] takes back the simple idea of the VGG net to always use the same size for the convolution operations (except for the first one). It also

<!-- page: 55 -->

takes into account an experimental fact: the fully connected layer (that usually contains most of the parameters given their size) are not really necessary to perform well. Removing them leads to a great decrease of the number of parameters of a CNN. In addition, the pooling operation is also less and less popular and tend to be replaced by convolution operations. This gives the basic ingredients of the ResNet fundamental building block, the Residual module of figure 5.16.

Two important points have to be mentioned concerning the Residual module. Firstly, a usual conv-conv-conv structure would lead to the following output (forgetting about batch normalization for simplicity and only for the time being, and denoting that there is no need for padding in $1 \times \dot { 1 }$ convolution operations)

$$
\begin{array}{r l} & h _ {f l + P m + P} ^ {(t) (1)} = g \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {0} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(0) f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (0)}\right) \\ & h _ {f l m} ^ {(t) (2)} = g \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(0) f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (1)}\right) \\ & h _ {f l m} ^ {(t) (3)} = g \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {2} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(0) f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (2)}\right), \end{array}\tag{5.22}
$$

whereas the Residual module modifies the last previous equation to (implying that the width, the size and the number of feature size of the input and the output being the same)

$$
\begin{array}{r l} & h _ {f l m} ^ {(t) (4)} = h _ {f l m} ^ {(t) (0)} + g \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {2} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(0) f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (2)}\right) \\ & \qquad = h _ {f l m} ^ {(t) (0)} + \delta h _ {f l m} ^ {(t) (0)}. \end{array}\tag{5.23}
$$

Instead of trying to fit the input, one is trying to fit a tiny modification of the input, hence the name residual. This allows the network to minimally modify the input when necessary, contrary to traditional architectures. Secondly, if the number of feature maps is important, a $3 \times 3$ convolution with stride 1 could be very costly in term of execution time and prone to overfit (large number of parameters). This is the reason of the presence of the $1 \times 1$ convolution, whose aim is just to prepare the input to the $3 \times 3$ conv to reduce the number of feature maps, number which is then restored with the final $1 \times 1$ conv of the Residual module. The first $1 \times 1$ convolution thus reads as a weight averaging

<!-- page: 56 -->

operation

$$
h _ {f l + P m + P} ^ {(t) (1)} = g \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {0} - 1} \Theta_ {f ^ {\prime}} ^ {(0) f} h _ {f ^ {\prime} l m} ^ {(t) (0)}\right),\tag{5.24}
$$

but is designed such that $f \in F _ { 1 } \ll F _ { 0 }$ . The second $1 \times 1$ convolution reads

$$
h _ {f l m} ^ {(t) (3)} = g \left(\sum_ {i = 0} ^ {F _ {1} - 1} \Theta_ {i} ^ {(2) f} h _ {i l m} ^ {(t) (1)}\right),\tag{5.25}
$$

with $f \in F _ { 0 } ,$ restoring the initial feature map size. The ResNet architecture is then the stacking of a large number (usually 50) of Residual modules, preceded by a conv-pool layer and ended by a pooling operation to obtain a fully connected layer, to which the output function is directly applied. This is illustrated in the following figure.

![](images/page_55_image_7.jpg)

Figure 5.17: The ResNet CNN

The ResNet CNN has accomplished state of the art results on a number of popular training sets (CIFAR, MNIST...). In practice, we will present in the following the backpropagation algorithm for CNN having standard (like VGG) architectures in mind.

## 5.6 Backpropagation

In a FNN, one just has to compute two kind of backpropagations : from output to fully connected (fc) layer and from fc to fc. In a traditional CNN, 4 new kind of propagations have to be computed: fc to pool, pool to conv, conv to conv and conv to pool. We present the corresponding error rates in the next sections, postponing their derivation to the appendix. We will consider as in a FNN a network with an input layer labelled 0, N-1 hidden layers labelled i and an output layer labelled N (N + 1 layers in total in the network).

<!-- page: 57 -->

## 5.6.1 Backpropagate through Batch Normalization

As in FNN, backpropagation introduces a new gradient

$$
\delta_ {f ^ {\prime}} ^ {f} J _ {f l l ^ {\prime} m m ^ {\prime}} ^ {(t t ^ {\prime}) (n)} = \frac {\partial y _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l m} ^ {(t) (\nu)}}.\tag{5.26}
$$

we show in appendix 5.A that for pool and conv layers

$$
J _ {f l l ^ {\prime} m m ^ {\prime}} ^ {(t t ^ {\prime}) (n)} = \tilde {\gamma} _ {f} ^ {(n)} \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {l ^ {\prime}} \delta_ {m} ^ {m ^ {\prime}} - \frac {1 + \tilde {h} _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l m} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right],\tag{5.27}
$$

while we find the FNN result as expected for fc layers

$$
J _ {f} ^ {(t t ^ {\prime}) (n)} = \tilde {\gamma} _ {f} ^ {(n)} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f} ^ {(t) (n)}}{T _ {\mathrm{mb}}} \right].\tag{5.28}
$$

## 5.6.2 Error updates

We will call the specific CNN error rates (depending on whether we need padding or not)

$$
\delta_ {f l (+ P) m (+ P)} ^ {(t) (\nu)} = \frac {\partial}{\partial a _ {f l m} ^ {(t) (i)}} J (\Theta),\tag{5.29}
$$

## 5.6.2.1 Backpropagate from output to fc

Backpropagate from output to fc is schematically illustrated on the following plot

$$
\begin{array}{c} \text {F} \\ \text {u} \\ \text {l} \\ \text {l} \end{array} \quad \begin{array}{c} \text {O} \\ \text {u} \\ \text {t} \\ \text {P} \\ \text {u} \\ \text {t} \end{array}
$$

Figure 5.18: Backpropagate from output to fc.

As in FNN, we find for the L2 loss function

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - y _ {f} ^ {(t)}\right),\tag{5.30}
$$

<!-- page: 58 -->

and for the cross-entropy one

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N)} - \delta_ {y ^ {(t)}} ^ {f}\right),\tag{5.31}
$$

## 5.6.2.2 Backpropagate from fc to fc

Backpropagate from fc to fc is schematically illustrated on the following plot

![](images/page_57_image_6.jpg)

Figure 5.19: Backpropagate from fc to fc.

As in FNN, we find

$$
\delta_ {f} ^ {(t) (\nu)} = g ^ {\prime} \left(a _ {f} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(o) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (n)} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{5.32}
$$

## 5.6.2.3 Backpropagate from fc to pool

Backpropagate from fc to pool is schematically illustrated on the following plot

![](images/page_57_image_12.jpg)

Figure 5.20: Backpropagate from fc to pool.

We show in appendix 5.B that this induces the following error rate

$$
\delta_ {f l m} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f l m} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{5.33}
$$

<!-- page: 59 -->

## 5.6.2.4 Backpropagate from pool to conv

Backpropagate from pool to conv is schematically illustrated on the following plot

![](images/page_58_image_4.jpg)

Figure 5.21: Backpropagate from pool to conv.

We show in appendix 5.A that this induces the following error rate (calling the pooling layer the pth one)

$$
\begin{array}{l}\delta_{fl + Pm + P}^{(t)(\nu)} = g^{\prime}\left(a_{fl m}^{(t)(\nu)}\right)\sum_{t^{\prime} = 0}^{T_{\mathrm{mb}} - 1}\sum_{l^{\prime} = 0}^{N_{\nu +1} - 1}\sum_{m^{\prime} = 0}^{T_{\nu +1} - 1}\delta_{fl^{\prime}m^{\prime}}^{(t^{\prime})(\nu +1)}\\ \times J_{f S_{P}l^{\prime} + j_{fl^{\prime}m^{\prime}}^{(t^{\prime})(p)} + P S_{P}m^{\prime} + k_{fl^{\prime}m^{\prime}}^{(t^{\prime})(p)} + Pl + P m + P}^{(tt^{\prime})(n)}. \end{array}\tag{5.34}
$$

Note that we have padded this error rate.

## 5.6.2.5 Backpropagate from conv to conv

Backpropagate from conv to conv is schematically illustrated on the following plot

![](images/page_58_image_11.jpg)

Figure 5.22: Backpropagate from conv to conv.

We show in appendix 5.B that this induces the following error rate

$$
\begin{array}{l} \delta_ {f l + P m + P} ^ {(t) (\nu)} = g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ \times \Theta_ {f j k} ^ {(o) f ^ {\prime}} J _ {f S _ {C} l ^ {\prime} + j S _ {C} m ^ {\prime} + k l + P m + P} ^ {(t t ^ {\prime}) (n)} \end{array}\tag{5.35}
$$

Note that we have padded this error rate.

<!-- page: 60 -->

## 5.6.2.6 Backpropagate from conv to pool

Backpropagate from conv to pool is schematically illustrated on the following plot

![](images/page_59_image_4.jpg)

Figure 5.23: Backpropagate from conv to pool.

We show in appendix 5.B that this induces the following error rate

$$
\delta_ {f l m} ^ {(t) (\nu)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {(o) f} \delta_ {f ^ {\frac {l + P - j}{S _ {C}} + P \frac {m + P - k}{S _ {C}} + P}} ^ {(t) (\nu + 1)}.\tag{5.36}
$$

## 5.6.3 Weight update

For the weight updates, we will also consider separately the weights between fc to fc layer, fc to pool, conv to conv, conv to pool and conv to input.

## 5.6.3.1 Weight update from fc to fc

For the two layer interactions

$$
\begin{array}{c} \text {F} \\ \text {u} \\ 1 \\ 1 \end{array} \xrightarrow {} \begin{array}{c} \text {F} \\ \text {u} \\ 1 \\ 1 \end{array}
$$

Figure 5.24: Weight update between two fc layers.

We have the weight update that reads

$$
\Delta_ {f ^ {\prime}} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} y _ {f ^ {\prime}} ^ {(t) (n)} \delta_ {f} ^ {(t) (\nu)}\tag{5.37}
$$

<!-- page: 61 -->

## 5.6.3.2 Weight update from fc to pool

For the two layer interactions

![](images/page_60_image_4.jpg)

Figure 5.25: Weight update between a fc layer and a pool layer.

We have the weight update that reads

$$
\Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f ^ {\prime} j + P k + P} ^ {(t) (\nu)} \delta_ {f} ^ {(t) (\nu)}\tag{5.38}
$$

## 5.6.3.3 Weight update from conv to conv

For the two layer interactions

![](images/page_60_image_10.jpg)

Figure 5.26: Weight update between two conv layers.

We have the weight update that reads

$$
\Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} y _ {f ^ {\prime} l + j m + k} ^ {(t) (n)} \delta_ {f l + P m + P} ^ {(t) (\nu)}\tag{5.39}
$$

## 5.6.3.4 Weight update from conv to pool and conv to input

For the two layer interactions

<!-- page: 62 -->

$$
\begin{array}{c} \text {Pool} \\ \hline \text {Covv} \\ \hline \text {Input} \\ \hline \text {Covv} \end{array}
$$

Figure 5.27: Weight update between a conv and a pool layer, as well as between a conv and the input layer.

$$
\Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} h _ {f ^ {\prime} l + j m + k} ^ {(t) (\nu)} \delta_ {f l + P m + P} ^ {(t) (\nu)}\tag{5.40}
$$

## 5.6.4 Coefficient update

For the Coefficient updates, we will also consider separately the weights between fc to fc layer, fc to pool, cont to pool and conv to conv.

## 5.6.4.1 Coefficient update from fc to fc

For the two layer interactions

$$
\begin{array}{c} \text {F} \\ \text {u} \\ 1 \\ 1 \end{array} \xrightarrow {} \begin{array}{c} \text {F} \\ \text {u} \\ 1 \\ 1 \end{array}
$$

Figure 5.28: Coefficient update between two fc layers.

We have

$$
\begin{array}{r l} & {\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(o) f ^ {\prime}} \tilde {h} _ {f} ^ {(t) (n)} \delta_ {f ^ {\prime}} ^ {(t) (\nu)},} \\ & {\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu)},} \end{array}\tag{5.41}
$$

<!-- page: 63 -->

## 5.6.4.2 Coefficient update from fc to pool and conv to pool

For the two layer interactions

$$
\begin{array}{c} \text {Pool1} \\ \text {Ful1} \\ \text {Pool1} \\ \text {Conv} \end{array}
$$

Figure 5.29: Coefficient update between a fc layer and a pool as well as a conv and a pool layer.

$$
\begin{array}{r l} & {\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \tilde {h} _ {f S _ {P} l + j _ {f l m} ^ {(t) (p)} + P S _ {P} m + k _ {f l m} ^ {(t) (p)} + P} ^ {(t) (n)} \delta_ {f l m} ^ {(t) (\nu)},} \\ & {\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l m} ^ {(t) (\nu)},} \end{array}\tag{5.42}
$$

## 5.6.4.3 Coefficient update from conv to conv

For the two layer interactions

$$
\begin{array}{c} \text {C} \\ \text {o} \\ \text {n} \\ \text {v} \end{array} \xleftarrow {} \begin{array}{c} \text {C} \\ \text {o} \\ \text {n} \\ \text {v} \end{array}
$$

Figure 5.30: Coefficient update between two conv layers.

We have

$$
\begin{array}{l} \Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \tilde {h} _ {f l + j m + k} ^ {(t) (n)} \delta_ {f ^ {\prime} l + P m + P} ^ {(t) (\nu)}, \\ \Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} := \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l + P m + P} ^ {(t) (\nu)}. \end{array}\tag{5.43}
$$

Let us now demonstrate all these formulas!

<!-- page: 64 -->

## Appendix

## 5.A Backprop through BatchNorm

For Backpropagation, we will need

$$
\frac {\partial y _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \gamma_ {f} ^ {(n)} \frac {\partial \tilde {h} _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l m} ^ {(t) (\nu)}}.\tag{5.44}
$$

Since

$$
\frac {\partial h _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu)}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \delta_ {t} ^ {t ^ {\prime}} \delta_ {f} ^ {f ^ {\prime}} \delta_ {l} ^ {l ^ {\prime}} \delta_ {m} ^ {m ^ {\prime}}, \quad \frac {\partial \hat {h} _ {f ^ {\prime}} ^ {(n)}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}} N _ {n} T _ {n}};\tag{5.45}
$$

and

$$
\frac {\partial \left(\hat {\sigma} _ {f ^ {\prime}} ^ {(n)}\right) ^ {2}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \frac {2 \delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \left(h _ {f l m} ^ {(t) (\nu)} - \hat {h} _ {f} ^ {(n)}\right),\tag{5.46}
$$

we get

$$
\begin{array}{l} \frac {\partial \tilde {h} _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \left[ \frac {T _ {\mathrm{mb}} N _ {n} T _ {n} \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {l ^ {\prime}} \delta_ {m} ^ {m ^ {\prime}} - 1}{\left(\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} - \frac {\left(h _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu)} - \hat {h} _ {f} ^ {(n)}\right) \left(h _ {f l m} ^ {(t) (\nu)} - \hat {h} _ {f} ^ {(n)}\right)}{\left(\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} + \epsilon\right) ^ {\frac {3}{2}}} \right] \\ = \frac {\delta_ {f} ^ {f ^ {\prime}}}{\left(\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {l ^ {\prime}} \delta_ {m} ^ {m ^ {\prime}} - \frac {1 + \tilde {h} _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l m} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right]. \end{array} \tag {5.47}
$$

To ease the notation we will denote

$$
\tilde {\gamma} _ {f} ^ {(n)} = \frac {\gamma_ {f} ^ {(n)}}{\left(\left(\hat {\sigma} _ {f} ^ {(n)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}}.\tag{5.48}
$$

so that

$$
\delta_ {f ^ {\prime}} ^ {f} J _ {f l m l ^ {\prime} m ^ {\prime}} ^ {(t t ^ {\prime}) (n)} = \frac {\partial y _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l m} ^ {(t) (\nu)}} = \tilde {\gamma} _ {f} ^ {(n)} \delta_ {f} ^ {f ^ {\prime}} \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {l ^ {\prime}} \delta_ {m} ^ {m ^ {\prime}} - \frac {1 + \tilde {h} _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l m} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right].\tag{5.49}
$$

<!-- page: 65 -->

## 5.B Error rate updates: details

We have for backpropagation from fc to pool

$$
\begin{array}{l} \delta_ {f l m} ^ {(t) (\nu)} = \frac {\partial}{\partial a _ {f l m} ^ {(t) (\nu)}} J ^ {(t)} (\Theta) = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \sum_ {j = 0} ^ {N _ {\nu + 1}} \sum_ {k = 0} ^ {T _ {\nu + 1}} \Theta_ {f ^ {\prime \prime} j k} ^ {(o) f ^ {\prime}} \frac {\partial h _ {f ^ {\prime \prime} j + P k + P} ^ {(t) (\nu + 1)}}{\partial h _ {f l + P m + P} ^ {(t) (\nu + 1)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f l m} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)}, \end{array}\tag{5.50}
$$

For backpropagation from pool to conv

$$
\begin{array}{l} \delta_ {f l + P m + P} ^ {(t) (\nu)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} = \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\varepsilon + 1} - 1} \frac \partial y _ {f ^ {\prime} S _ {P} l ^ {\prime} + j _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P S _ {P} m ^ {\prime} + k _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P}{{\partial h} _ {f l + P m + P} ^ {(t) (\nu + 1)}} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \delta_ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {S _ {P} l ^ {\prime} + j _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)} S _ {P} m ^ {\prime} + k _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)}} \delta_ {m} - \frac 1 + \tilde {h} _ {f S _ {P} l ^ {\prime} + j _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P S _ {P} m ^ {\prime} + k _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right] \\ = g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1}} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ \times J _ {f S _ {P} l ^ {\prime} + j _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P S _ {P} m ^ {\prime} + k _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P l + P m + P} ^ {(t t ') (n)} \end{array}
$$

For backpropagation from conv to conv

<!-- page: 66 -->

$$
\begin{array}{l} \delta_ {f l + P m + P} ^ {(t) (\nu)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\mu + 1} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime \prime} j k} ^ {(o) f ^ {\prime}} \\ \times \frac {\partial y _ {f ^ {\prime \prime} l ^ {\prime} + j m ^ {\prime} + k} ^ {(t ^ {\prime}) (n)}}{\partial h _ {f l + P m + P} ^ {(t) (\nu + 1)}} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)}, \end{array}\tag{5.52}
$$

so

$$
\begin{array}{l} \delta_ {f l + P m + P} ^ {(t) (\nu)} = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ \times \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l + P} ^ {l ^ {\prime} + j} \delta_ {m + P} ^ {m ^ {\prime} + k} - \frac {1 + \tilde {h} _ {f l ^ {\prime} + j m ^ {\prime} + k} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right] \\ = g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1}} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1}} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ \times \Theta_ {f j k} ^ {(o) f ^ {\prime}} J _ {f l ^ {\prime} + j m ^ {\prime} + k l + P m + P}, \end{array} \tag {5.53}
$$

and for backpropagation from conv to pool (taking the stride equal to 1 to simplify the derivation)

$$
\begin{array}{l} \delta_ {f l m} ^ {(t) (\nu)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\varepsilon + 1} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime \prime} j k} ^ {(o) f ^ {\prime}} \frac {\partial h _ {f ^ {\prime \prime} l ^ {\prime} + j m ^ {\prime} + k} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial h _ {f l + P m + P} ^ {(t) (\nu + 1)}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l + 2 P - j m + 2 P - k}. \end{array} \tag {5.54}
$$

And so on and so forth.

<!-- page: 67 -->

## 5.C Weight update: details

Fc to Fc

$$
\Delta_ {f ^ {\prime}} ^ {\Theta (o) f} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime \prime} = 0} ^ {F _ {\nu}} \frac {\partial \Theta_ {f ^ {\prime \prime \prime}} ^ {(o) f ^ {\prime \prime}}}{\partial \Theta_ {f ^ {\prime}} ^ {(o) f}} y _ {f ^ {\prime \prime \prime}} ^ {(t) (n)} \delta_ {f ^ {\prime \prime}} ^ {(t) (\nu)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \delta_ {f} ^ {(t) (\nu)} y _ {f ^ {\prime}} ^ {(t) (n)}\tag{5.55}
$$

Fc to pool

$$
\begin{array}{l} \Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime \prime} = 0} ^ {F _ {\nu}} \sum_ {j ^ {\prime} = 0} ^ {N _ {\nu + 1}} \sum_ {k ^ {\prime} = 0} ^ {T _ {\nu + 1}} \frac {\partial \Theta_ {f ^ {\prime \prime \prime} j ^ {\prime} k ^ {\prime}} ^ {(1 3) f ^ {\prime \prime}}}{\partial \Theta_ {f ^ {\prime} j k} ^ {(o) f}} h _ {f ^ {\prime \prime \prime} j ^ {\prime} + P k ^ {\prime} + P} ^ {(t) (\nu)} \delta_ {f ^ {\prime \prime}} ^ {(t) (\nu)} \\ = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \delta_ {f} ^ {(t) (\nu)} h _ {f ^ {\prime} j + P k + P} ^ {(t) (\nu)}. \end{array}\tag{5.56}
$$

and for conv to conv

$$
\begin{array}{l} \Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime \prime} l m} ^ {(t) (\nu)}}{\partial \Theta_ {f ^ {\prime} j k} ^ {(o) f}} \delta_ {f ^ {\prime \prime} l + P m + P} ^ {(t) (\nu)} \\ = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} \sum_ {f ^ {\prime \prime \prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j ^ {\prime} = 0} ^ {R _ {C} - 1} \sum_ {k ^ {\prime} = 0} ^ {R _ {C} - 1} \frac {\partial \Theta_ {f ^ {\prime \prime \prime} j ^ {\prime} k ^ {\prime}} ^ {(o) f ^ {\prime \prime}}}{\partial \Theta_ {f ^ {\prime} j k} ^ {(o) f}} \\ \times y _ {f ^ {\prime \prime \prime} S _ {C} l + j ^ {\prime} S _ {C} m + k ^ {\prime}} ^ {(t) (n)} \delta_ {f ^ {\prime \prime} l + P m + P} ^ {(t) (\nu)} \\ = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} y _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (n)} \delta_ {f l + P m + P} ^ {(t) (\nu)}. \end{array}\tag{5.57}
$$

similarly for conv to pool and conv to input

$$
\Delta_ {f ^ {\prime} j k} ^ {\Theta (o) f} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {T _ {\nu + 1} - 1} \sum_ {m = 0} ^ {N _ {\nu + 1} - 1} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t) (\nu)} \delta_ {f l + P m + P} ^ {(t) (\nu)}.\tag{5.58}
$$

<!-- page: 68 -->

## 5.D Coefficient update: details

Fc to Fc

$$
\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t) (\nu + 1)}}{\partial \gamma_ {f} ^ {(n)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(o) f ^ {\prime}} \tilde {h} _ {f} ^ {(t) (n)} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{5.59}
$$

$$
\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime}} ^ {(t) (\nu + 1)}}{\partial \beta_ {f} ^ {(n)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \Theta_ {f} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu + 1)},\tag{5.60}
$$

fc to pool and conv to pool

$$
\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \tilde {h} _ {f S _ {P} l + j _ {f l m} ^ {(t) (p)} + P S _ {P} m + k _ {f l m} ^ {(t) (p)} + P} ^ {(t) (n)} \delta_ {f l m} ^ {(t) (\nu + 1)}\tag{5.61}
$$

$$
\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l m} ^ {(t) (\nu + 1)},\tag{5.62}
$$

conv to conv

$$
\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \frac {a _ {f ^ {\prime} l m} ^ {(t) (\nu + 1)}}{\partial \gamma_ {f} ^ {(n)}} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)}\tag{5.63}
$$

$$
= \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \tilde {h} _ {f l + j m + k} ^ {(t) (n)} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)}\tag{5.64}
$$

$$
\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)},\tag{5.65}
$$

## 5.E Practical Simplification

When implementing a CNN, it turns out that some of the error rate computation can be very costly (in term of execution time) if naively encoded. In this section, we sketch some improvement that can be performed on the pool to conv, conv to conv error rate implementation, as well as ones on coefficient updates.

<!-- page: 69 -->

## 5.E.1 pool to conv Simplification

Let us expand the batch normalization term of the pool to conv error rate to see how we can simplify it (calling the pooling the p’th one)

$$
\begin{array}{l} \delta_ {f l m} ^ {(t) (\nu)} = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l} ^ {S _ {P} l ^ {\prime} + j _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)} S _ {P} m ^ {\prime} + k _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)}} - \frac {1 + \tilde {h} _ {f S _ {P} l ^ {\prime} + j _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P S _ {P} m ^ {\prime} + k _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right]. \end{array}\tag{5.66}
$$

Numerically, this implies that for each $t , f , l ,$ m one needs to perform 3 loops (on $t ^ { \prime } , l ^ { \prime } , m ^ { \prime } \vec { ) }$ , hence a 7 loop process. This can be reduced to 4 at most in the following way. Defining

$$
\mu_ {f} ^ {(1)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)},\tag{5.67}
$$

and

$$
\mu_ {f} ^ {(2)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \tilde {h} _ {f S _ {P} l ^ {\prime} + j _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P S _ {P} m ^ {\prime} + k _ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (p)} + P} ^ {(t ^ {\prime}) (n)},\tag{5.68}
$$

we have introduced two new variables that can be computed in four loops, but three of them are independent of the ones needed to compute $\delta _ { f l m } ^ { ( t ) ( \nu ) }$ . For the last term, the $\delta$ functions "kill" 3 loops and we are left with

$$
\begin{array}{l} \delta_ {f l m} ^ {(t) (\nu)} = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \left\{\sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \delta_ {l} ^ {S _ {P} l ^ {\prime} + j _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)}} \delta_ {m} ^ {S _ {P} m ^ {\prime} + k _ {t ^ {\prime} f l ^ {\prime} m ^ {\prime}} ^ {(p)}} \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad - \frac {\mu_ {f} ^ {(1)} + \mu_ {f} ^ {(2)} \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \Bigg \}, \end{array}\tag{5.69}
$$

which requires only 4 loops to be computed.

<!-- page: 70 -->

## 5.E.2 Convolution Simplification

Let us expand the batch normalization term of the conv to conv error rate to see how we can simplify it

$$
\begin{array}{l} \delta_ {f l m} ^ {(t) (\nu)} = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (i \nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \\ \left[ \delta_ {t} ^ {t ^ {\prime}} \delta_ {l + P} ^ {l ^ {\prime} + j} \delta_ {m + P} ^ {m ^ {\prime} + k} - \frac {1 + \tilde {h} _ {f l ^ {\prime} + j m ^ {\prime} + k} ^ {(t ^ {\prime}) (n)} \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right]. \end{array} \tag {5.}\tag{5.70}
$$

If left untouched, one now needs 10 loops (on $t , f , l ,$ m and $t ^ { \prime } , f ^ { \prime } , l ^ { \prime } , m ^ { \prime } , j , k )$ to compute $\delta _ { f l m } ^ { ( t ) ( \nu ) } \nmid$ This can be reduced to $7$ loops at most in the following way. First, we define

$$
\lambda_ {f l m} ^ {(t) (1)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l + P - j m + P - k} ^ {(t ^ {\prime}) (\nu + 1)},\tag{5.71}
$$

which is a convolution operation on a shifted index $\delta ^ { ( \nu + 1 ) }$ . This is second most expensive operation, but libraries are optimized for this and it implies two of the smallest loops (those on $R _ { C } )$ . Then we compute (four loops each)

$$
\lambda_ {f f ^ {\prime}} ^ {(2)} = \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}}, \quad \lambda_ {f ^ {\prime}} ^ {(3)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)},\tag{5.72}
$$

and (2 loops)

$$
\lambda_ {f} ^ {(4)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \lambda_ {f f ^ {\prime}} ^ {(2)} \lambda_ {f ^ {\prime}} ^ {(3)}.\tag{5.73}
$$

Finally, we compute

$$
\lambda_ {f f ^ {\prime} j k} ^ {(5)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)} \tilde {h} _ {f l ^ {\prime} + j m ^ {\prime} + k} ^ {(t ^ {\prime}) (n)},\tag{5.74}
$$

$$
\lambda_ {f} ^ {(6)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \lambda_ {f f ^ {\prime} j k} ^ {(5)}.\tag{5.75}
$$

$\lambda _ { f } ^ { ( 6 ) }$ only requires four loops, and $\lambda _ { f f ^ { \prime } j k } ^ { ( 5 ) }$ is the most expensive operation. But it is also a convolution operation that implies two of the smallest loops (those on

<!-- page: 71 -->

$R _ { C } )$ . With all these newly introduced λ, we obtain

$$
\delta_ {f l m} ^ {(t) (\nu)} = \tilde {\gamma} _ {f} ^ {(n)} g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \left\{\lambda_ {f l m} ^ {(t) (1)} - \frac {\lambda_ {f} ^ {(4)} + \lambda_ {f} ^ {(6)} \tilde {h} _ {f l + P m + P} ^ {(t) (n)}}{T _ {\mathrm{mb}} N _ {n} T _ {n}} \right\},\tag{5.76}
$$

which only requires four loops to be computed.

## 5.E.3 Coefficient Simplification

To compute

$$
\Delta_ {f} ^ {\gamma (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \tilde {h} _ {f l + j m + k} ^ {(t) (n)} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)}\tag{5.77}
$$

$$
\Delta_ {f} ^ {\beta (n)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f j k} ^ {(o) f ^ {\prime}} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)},\tag{5.78}
$$

we will first define

$$
\nu_ {f ^ {\prime} f j k} ^ {(1)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \tilde {h} _ {f l + j m + k} ^ {(t) (n)} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)}, \nu_ {f ^ {\prime}} ^ {(2)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {l = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m = 0} ^ {T _ {\nu + 1} - 1} \delta_ {f ^ {\prime} l m} ^ {(t) (\nu + 1)},\tag{5.79}
$$

so that

$$
\Delta_ {f} ^ {\gamma (n)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \nu_ {f ^ {\prime} f j k} ^ {(1)} \Theta_ {f j k} ^ {(o) f ^ {\prime}}\tag{5.80}
$$

$$
\Delta_ {f} ^ {\beta (n)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \nu_ {f ^ {\prime}} ^ {(2)} \Theta_ {f j k} ^ {(o) f ^ {\prime}},\tag{5.81}
$$

## 5.F Batchpropagation through a ResNet module

For pedagogical reasons, we introduced the ResNet structure without "break-$\mathrm { i n g } ^ { \prime \prime }$ the conv layers. Nevertheless, a more standard choice is depicted in the following figure

<!-- page: 72 -->

![](images/page_71_image_2.jpg)

Figure 5.31: Batchpropagation through a ResNet module.

Batchpropagation through this ResNet module presents no particular diffi culty. Indeed, the update rules imply the usual conv to conv backpropagation derived in the main part of this note. The only novelty is the error rate update of the input layer of the ResNet, as it now reads (assuming that the input of this ResNet module is the output of another one)

$$
\begin{array}{l} \delta_ {f l + P m + P} ^ {(t) (\nu)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 1} - 1} \frac {\partial a _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ \quad + \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 3} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 3} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu + 3} - 1} \frac {\partial a _ {f ^ {\prime} l ^ {\prime} m ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 3)}}{\partial a _ {f l m} ^ {(t) (\nu)}} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 3)} \\ \quad = g ^ {\prime} \left(a _ {f l m} ^ {(t) (\nu)}\right) \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {l ^ {\prime} = 0} ^ {N _ {\nu + 1} - 1} \sum_ {m ^ {\prime} = 0} ^ {T _ {\nu , + 1} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \delta_ {f ^ {\prime} l ^ {\prime} + P m ^ {\prime} + P} ^ {(t ^ {\prime}) (\nu + 1)} \\ \quad \times \Theta_ {f j k} ^ {(o) f ^ {\prime}} J _ {f l ^ {\prime} + j m ^ {\prime} + k l + P m + P} ^ {(t t ^ {\prime}) (n)} + \delta_ {f l + P m + P} ^ {(t) (\nu + 3)}. \end{array}\tag{5.82}
$$

This new term is what allows the error rate to flow smoothly from the output to the input in the ResNet CNN, as the additional connexion in a ResNet is like a skip path to the convolution chains. Let us mention in passing that some architecture connects every hidden layer to each others[19].

## 5.G Convolution as a matrix multiplication

Thanks to the simplifications introduced in appendix 5.E, we have reduced all convolution, pooling and tensor multiplication operations to at most 7 loops

<!-- page: 73 -->

operations. Nevertheless, in high abstraction programming languages such as python, it is still way too much to be handled smoothly. But there exists additional tricks to "reduce" the dimension of the convolution operation, such as one has only to encode three for loops (2D matrix multiplication) at the end of the day. Let us begin our presentation of these tricks with a 2D convolution example

## 5.G.1 2D Convolution

![](images/page_72_image_4.jpg)

Figure 5.32: :2D convolution as a 2D matrix multiplication

A 2D convolution operation reads

$$
a _ {l m} = \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {j k} h _ {S _ {C} l + j S _ {C} m + k}.\tag{5.83}
$$

<!-- page: 74 -->

and it involves 4 loops. The trick to reduce this operation to a 2D matrix multiplication is to redefine the h matrix by looking at each h indices are going to be multiplied by Θ for each value of l and m. Then the associated h values are stored into a $\mathring { N } _ { p } T _ { p } \times R _ { C } ^ { 2 }$ matrix. Flattening out the Θ matrix, we are left with a matrix multiplication, the flattened Θ matrix being of size $R _ { C } ^ { 2 } \times 1$ . This is illustrated on figure 5.32

## 5.G.2 4D Convolution

![](images/page_73_image_4.jpg)

Figure 5.33: 4D convolution as a 2D matrix multiplication

Following the same lines, the adding of the input and output feature maps as well as the batch size poses no particular conceptual difficulty, as illustrated

<!-- page: 75 -->

on figure 5.33, corresponding to the 4D convolution

$$
a _ {f l m} ^ {(t)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {p} - 1} \sum_ {j = 0} ^ {R _ {C} - 1} \sum_ {k = 0} ^ {R _ {C} - 1} \Theta_ {f ^ {\prime} j k} ^ {f} h _ {f ^ {\prime} S _ {C} l + j S _ {C} m + k} ^ {(t)}.\tag{5.84}
$$

## 5.H Pooling as a row matrix maximum

![](images/page_74_image_5.jpg)

Figure 5.34: 4D pooling as a 2D matrix multiplication

The pooling operation can also be simplified, seeing it as the maximum search on the rows of a flattened 2D matrix. This is illustrated on figure 5.34

$$
a _ {f l m} ^ {(t)} = \max _ {j = 0} ^ {R _ {P} - 1} \max _ {k = 0} ^ {R _ {P} - 1} h _ {f S _ {P} l + j S _ {P} m + k} ^ {(t)}.\tag{5.85}
$$

<!-- page: 76 -->

<!-- page: 77 -->

## Chapter 6 Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F Recurrent Neural NetworksInput Convolution Layer . . . N + 2P T + 2P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

## Contents

- 6.1 Introduction 78
- 6.2 RNN-LSTM architecture 78
- 6.2.1 Forward pass in a RNN-LSTM 78
- 6.2.2 Backward pass in a RNN-LSTM 80
- 6.3 Extreme Layers and loss function 80
- 6.3.1 Input layer 81
- 6.3.2 Output layer 81
- 6.3.3 Loss function 81
- 6.4 RNN specificities 81
- 6.4.1 RNN structure 81
- 6.4.2 Forward pass in a RNN 83
- 6.4.3 Backpropagation in a RNN 83
- 6.4.4 Weight and coefficient updates in a RNN 84
- 6.5 LSTM specificities 85
- 6.5.1 LSTM structure 85
- 6.5.2 Forward pass in LSTM 86
- 6.5.3 Batch normalization 87
- 6.5.4 Backpropagation in a LSTM 88
- 6.5.5 Weight and coefficient updates in a LSTM 89
- Appendices 90

<!-- page: 78 -->

- 6.A Backpropagation trough Batch Normalization 90
- 6.B RNN Backpropagation 91
- 6.B.1 RNN Error rate updates: details 91
- 6.B.2 RNN Weight and coefficient updates: details 93
- 6.C LSTM Backpropagation 95
- 6.C.1 LSTM Error rate updates: details 95
- 6.C.2 LSTM Weight and coefficient updates: details 98
- 6.D Peephole connexions 101

## 6.1 Introduction

![](images/page_77_image_4.jpg)

n this chapter, we review a third kind of Neural Network architecture: I Recurrent Neural Networks[6]. By contrast with the CNN, this kind of network introduces a real architecture novelty : instead of forwarding only in a "spatial" direction, the data are also forwarded in a new – time dependent – direction. We will present the first Recurrent Neural Network (RNN) architecture, as well as the current most popular one: the Long Short Term Memory (LSTM) Neural Network.

## 6.2 RNN-LSTM architecture

## 6.2.1 Forward pass in a RNN-LSTM

In figure 4.1, we present the RNN architecture in a schematic way

<!-- page: 79 -->

![](images/page_78_image_2.jpg)

Figure 6.1: RNN architecture, with data propagating both in "space" and in "time". In our exemple, the time dimension is of size 8 while the "spatial" one is of size 4.

The real novelty of this type of neural network is that the fact that we are trying to predict a time serie is encoded in the very architecture of the network. RNN have first been introduced mostly to predict the next words in a sentance (classification task), hence the notion of ordering in time of the prediction. But this kind of network architecture can also be applied to regression problems. Among others things one can think of stock prices evolution, or temperature forecasting. In contrast to the precedent neural networks that we introduced, where we defined (denoting ν as in previous chapters the layer index in the spatial direction)

$$
\begin{array}{c} a _ {f} ^ {(t) (\nu)} = \text {Weight Averaging} \left(h _ {f} ^ {(t) (\nu)}\right), \\ h _ {f} ^ {(t) (\nu + 1)} = \text {Activation function} \left(a _ {f} ^ {(t) (\nu)}\right), \end{array}\tag{6.1}
$$

we now have the hidden layers that are indexed by both a "spatial" and a "temporal" index (with T being the network dimension in this new direction),

<!-- page: 80 -->

and the general philosophy of the RNN is (now the a is usually characterized by a c for cell state, this denotation, trivial for the basic RNN architecture will make more sense when we talk about LSTM networks)

$$
\begin{array}{l} c _ {f} ^ {(t) (\nu \tau)} = \text {Weight Averaging} \left(h _ {f} ^ {(t) (\nu \tau - 1)}, h _ {f} ^ {(t) (\nu - 1 \tau)}\right), \\ h _ {f} ^ {(t) (\nu \tau)} = \text {Activation function} \left(c _ {f} ^ {(t) (\nu \tau)}\right), \end{array}\tag{6.2}
$$

## 6.2.2 Backward pass in a RNN-LSTM

The backward pass in a RNN-LSTM has to respect a certain time order, as illustrated in the following figure

![](images/page_79_image_6.jpg)

Figure 6.2: Architecture taken, backward pass. Here what cannot compute the gradient of a layer without having computed the ones that flow into it

With this in mind, let us now see in details the implementation of a RNN and its advanced cousin, the Long Short Term Memory (LSTM)-RNN.

## 6.3 Extreme Layers and loss function

These part of the RNN-LSTM networks just experiences trivial modifications. Let us see them

<!-- page: 81 -->

## 6.3.1 Input layer

In a RNN-LSTM, the input layer is recursively defined as

$$
h _ {f} ^ {(t) (0 \tau + 1)} = \left(\tilde {h} _ {f} ^ {(t) (0 \tau)}, h _ {f} ^ {(t) (N - 1 \tau)}\right).\tag{6.3}
$$

where $\tilde { h } _ { f } ^ { ( t ) ( 0 \tau ) }$ is $h _ { f } ^ { ( t ) ( 0 \tau ) }$ with the first time column removed.

## 6.3.2 Output layer

The output layer of a RNN-LSTM reads

$$
h _ {f} ^ {(t) (N \tau)} = o \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} \Theta_ {f ^ {\prime}} ^ {f} h _ {f} ^ {(t) (N - 1 \tau)}\right),\tag{6.4}
$$

where the output function o is as for FNN’s and CNN’s is either the identity (regression task) or the cross-entropy function (classification task).

## 6.3.3 Loss function

The loss function for a regression task reads

$$
J (\Theta) = \frac {1}{2 T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\tau = 0} ^ {T - 1} \sum_ {f = 0} ^ {F _ {N} - 1} \left(h _ {f} ^ {(t) (N \tau)} - y _ {f} ^ {(t) (\tau)}\right) ^ {2}.\tag{6.5}
$$

and for a classification task

$$
J (\Theta) = - \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\tau = 0} ^ {T - 1} \sum_ {c = 0} ^ {C - 1} \delta_ {y _ {c} ^ {(t) (\tau)}} ^ {c} \ln \left(h _ {f} ^ {(t) (N \tau)}\right).\tag{6.6}
$$

## 6.4 RNN specificities

## 6.4.1 RNN structure

RNN is the most basic architecture that takes – thanks to the way it is built in – into account the time structure of the data to be predicted. Zooming on one hidden layer of 6.1, here is what we see for a simple Recurrent Neural Network.

<!-- page: 82 -->

![](images/page_81_image_2.jpg)

Figure 6.3: RNN hidden unit details

And here is how the output of the hidden layer represented in 6.3 enters into the subsequent hidden units

![](images/page_81_image_5.jpg)

Figure 6.4: How the RNN hidden unit interact with each others

Lest us now mathematically express what is reprensented in figures 6.3 and 6.4.

<!-- page: 83 -->

## 6.4.2 Forward pass in a RNN

In a RNN, the update rules read for the first time slice (spatial layer at the extreme left of figure 6.1)

$$
h _ {f} ^ {(t) (\nu \tau)} = \tanh \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {\nu (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)}\right),\tag{6.7}
$$

and for the other ones

$$
h _ {f} ^ {(t) (\nu \tau)} = \tanh \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {\nu (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {\tau (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right).\tag{6.8}
$$

## 6.4.3 Backpropagation in a RNN

The backpropagation philosophy will remain unchanged : find the error rate updates, from which one can deduce the weight updates. But as for the hidden layers, the $\delta$ now have both a spatial and a temporal component. We will thus have to compute

$$
\delta_ {f} ^ {(t) (\nu \tau)} = \frac {\delta}{\delta h _ {f} ^ {(t) (\nu + 1 \tau)}} J (\Theta),\tag{6.9}
$$

to deduce

$$
\Delta_ {f ^ {\prime}} ^ {\Theta \mathrm{index} f} = \frac {\delta}{\delta \Delta_ {f ^ {\prime}} ^ {\Theta \mathrm{index} f}} J (\Theta),\tag{6.10}
$$

where the index can either be nothing (weights of the ouput layers), $\nu ( \nu )$ (weights between two spatially connected layers) or $\tau ( \nu )$ (weights between two temporally connected layers). First, it is easy to compute (in the same way as in chapter 1 for FNN) for the MSE loss function

$$
\delta_ {f} ^ {(t) (N - 1 \tau)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N \tau)} - y _ {f} ^ {(t) (\tau)}\right),\tag{6.11}
$$

and for the cross entropy loss function

$$
\delta_ {f} ^ {(t) (N - 1)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N \tau)} - \delta_ {y ^ {(t) (\tau)}} ^ {f}\right).\tag{6.12}
$$

<!-- page: 84 -->

Calling

$$
\mathcal {T} _ {f} ^ {(t) (\nu \tau)} = 1 - \left(h _ {f} ^ {(t) (\nu \tau)}\right) ^ {2},\tag{6.13}
$$

and

$$
\mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau) _ {a}} = \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \Theta_ {f} ^ {a (\nu + 1) f ^ {\prime}},\tag{6.14}
$$

we show in appendix 6.B.1 that $( { \mathrm { i f ~ } } \tau + 1$ exists, otherwise the second term is absent)

$$
\delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b \epsilon}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)}.\tag{6.15}
$$

where $b _ { 0 } = \nu$ and $b _ { 1 } = \tau$

## 6.4.4 Weight and coefficient updates in a RNN

To complete the backpropagation algorithm, we need

$$
\Delta_ {f ^ {\prime}} ^ {\nu (\nu) f}, \qquad \Delta_ {f ^ {\prime}} ^ {\tau (\nu) f}, \qquad \Delta_ {f ^ {\prime}} ^ {f}, \qquad \Delta_ {f} ^ {\beta (\nu \tau)}, \qquad \Delta_ {f} ^ {\gamma (\nu \tau)}.\tag{6.16}
$$

We show in appendix 6.B.2 that

$$
\Delta_ {f ^ {\prime}} ^ {\nu (\nu -) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \mathcal {T} _ {f} ^ {(t) (\nu \tau)} \delta_ {f} ^ {(t) (\nu - 1 \tau)} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)},\tag{6.17}
$$

$$
\Delta_ {f ^ {\prime}} ^ {\tau (\nu) f} = \sum_ {\tau = 1} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \mathcal {T} _ {f} ^ {(t) (\nu \tau)} \delta_ {f} ^ {(t) (\nu - 1 \tau)} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)},\tag{6.18}
$$

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f ^ {\prime}} ^ {(t) (N - 1 \tau)} \delta_ {f} ^ {(t) (N - 1 \tau)},\tag{6.19}
$$

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)},\tag{6.20}
$$

$$
\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)}.\tag{6.21}
$$

<!-- page: 85 -->

## 6.5 LSTM specificities

## 6.5.1 LSTM structure

In a Long Short Term Memory Neural Network[7], the state of a given unit is not directly determined by its left and bottom neighbours. Instead, a cell state is updated for each hidden unit, and the output of this unit is a probe of the cell state. This formulation might seem puzzling at first, but it is philosophically similar to the ResNet approach that we briefly encounter in the appendix of chapter 4: instead of trying to fit an input with a complicated function, we try to fit tiny variation of the input, hence allowing the gradient to flow in a smoother manner in the network. In the LSTM network, several gates are thus introduced : the input gate $i _ { f } ^ { ( t ) ( \nu \tau ) }$ determines if we allow new information $g _ { f } ^ { ( t ) ( \nu \tau ) }$ to enter into the cell state. The output gate $\rho _ { f } ^ { ( t ) ( \nu \tau ) }$ determines if we set or not the output hidden value to 0, or really probes the current cell state. Finally, the forget state $f _ { f } ^ { ( t ) ( \nu \tau ) }$ determines if we forget or not the past cell state. All theses concepts are illustrated on the figure 6.5, which is the LSTM counterpart of the RNN structure of section 6.4.1. This diagram will be explained in details in the next section.

![](images/page_84_image_5.jpg)

Figure 6.5: LSTM hidden unit details

<!-- page: 86 -->

In a LSTM, the different hidden units interact in the following way

![](images/page_85_image_3.jpg)

Figure 6.6: How the LSTM hidden unit interact with each others

## 6.5.2 Forward pass in LSTM

Considering all the $\tau - 1$ variable values to be 0 when $\tau = 0 ,$ we get the following formula for the input, forget and output gates

$$
i _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {i _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {i _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.22}
$$

$$
f _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {f _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {f _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.23}
$$

$$
o _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {o _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {o _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right).\tag{6.24}
$$

The sigmoid function is the reason why the $i , f , o$ functions are called gates: they take their values between 0 and 1, therefore either allowing or forbidding information to pass through the next step. The cell state update is then

<!-- page: 87 -->

performed in the following way

$$
\begin{array}{r l} & g _ {f} ^ {(t) (\nu \tau)} = \mathrm{tanh} \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {g _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {g _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right), \\ & c _ {f} ^ {(t) (\nu \tau)} = f _ {f} ^ {(t) (\nu \tau)} c _ {f} ^ {(t) (\nu \tau - 1)} + i _ {f} ^ {(t) (\nu \tau)} g _ {f} ^ {(t) (\nu \tau)}, \end{array}\tag{6.25}
$$

(6.26)

and as announced, hidden state update is just a probe of the current cell state

$$
h _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \tanh \left(c _ {f} ^ {(t) (\nu \tau)}\right).\tag{6.27}
$$

These formula singularly complicates the feed forward and especially the backpropagation procedure. For completeness, we will us nevertheless carefully derive it. Let us mention in passing that recent studies tried to replace the tanh activation function of the hidden state $h _ { f } ^ { ( t ) ( \nu \tau ) }$ and the cell update $g _ { f } ^ { ( t ) ( \nu \tau ) }$ by Rectified Linear Units, and seems to report better results with a proper initialization of all the weight matrices, argued to be diagonal

$$
\Theta_ {f ^ {\prime}} ^ {f} (\text {init}) = \frac {1}{2} \delta_ {f ^ {\prime}} ^ {f} \left(+ \sqrt {\frac {6}{F _ {\text {in}} + F _ {\text {out}}}}\right),\tag{6.28}
$$

with the bracket term here to possibly (or not) include some randomness into the initialization

## 6.5.3 Batch normalization

In batchnorm The update rules for the gates are modified as expected

$$
i _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {i _ {\nu} (\nu -) f} y _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {i _ {\tau} (- \nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.29}
$$

$$
f _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {f _ {\nu} (\nu -) f} y _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {f _ {\tau} (- \nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.30}
$$

$$
o _ {f} ^ {(t) (\nu \tau)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {o _ {\nu} (\nu -) f} y _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {o _ {\tau} (- \nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.31}
$$

$$
g _ {f} ^ {(t) (\nu \tau)} = \tanh \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {g _ {\nu} (\nu -) f} y _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {g _ {\tau} (- \nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.32}
$$

<!-- page: 88 -->

where

$$
y _ {f} ^ {(t) (\nu \tau)} = \gamma_ {f} ^ {(\nu \tau)} \tilde {h} _ {f} ^ {(t) (\nu \tau)} + \beta_ {f} ^ {(\nu \tau)},\tag{6.33}
$$

as well as

$$
\tilde {h} _ {f} ^ {(t) (\nu \tau)} = \frac {h _ {f} ^ {(t) (\nu \tau)} - \hat {h} _ {f} ^ {(\nu \tau)}}{\sqrt {\left(\sigma_ {f} ^ {(\nu \tau)}\right) ^ {2} + \epsilon}}\tag{6.34}
$$

and

$$
\hat {h} _ {f} ^ {(\nu \tau)} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f} ^ {(t) (\nu \tau)}, \left(\sigma_ {f} ^ {(\nu \tau)}\right) ^ {2} = \frac {1}{T _ {\mathrm{mb}}} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left(h _ {f} ^ {(t) (\nu \tau)} - \hat {h} _ {f} ^ {(\nu \tau)}\right) ^ {2}.\tag{6.35}
$$

It is important to compute a running sum for the mean and the variance, that will serve for the evaluation of the cross-validation and the test set (calling e the number of iterations/epochs)

$$
\mathbb {E} \left[ h _ {f} ^ {(t) (\nu \tau)} \right] _ {e + 1} = \frac {e \mathbb {E} \left[ h _ {f} ^ {(t) (\nu \tau)} \right] _ {e} + \hat {h} _ {f} ^ {(\nu \tau)}}{e + 1},\tag{6.36}
$$

$$
\mathbb {V} a r \left[ h _ {f} ^ {(t) (\nu \tau)} \right] _ {e + 1} = \frac {e \mathbb {V} a r \left[ h _ {f} ^ {(t) (\nu \tau)} \right] _ {e} + \left(\hat {\sigma} _ {f} ^ {(\nu \tau)}\right) ^ {2}}{e + 1}\tag{6.37}
$$

and what will be used at the end is $\mathbb { E } \left[ h _ { f } ^ { ( t ) ( \nu \tau ) } \right]$ and $\begin{array} { r } { \frac { T _ { \mathsf { m b } } } { T _ { \mathsf { m b } } - 1 } \mathbf { V } a r \left[ h _ { f } ^ { \left( t \right) \left( \nu \tau \right) } \right] } \end{array}$

## 6.5.4 Backpropagation in a LSTM

The backpropagation In a LSTM keeps the same structure as in a RNN, namely

$$
\delta_ {f} ^ {(t) (N - 1 \tau)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N \tau)} - y _ {f} ^ {(t) (\tau)}\right),\tag{6.38}
$$

and (shown in appendix 6.C.1)

$$
\delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)}.\tag{6.39}
$$

<!-- page: 89 -->

What changes is the form of $\mathcal { H } ,$ now given by

$$
\mathcal {O} _ {f} ^ {(t) (\nu \tau)} = h _ {f} ^ {(t) (\nu \tau)} \left(1 - o _ {f} ^ {(t) (\nu \tau)}\right),
$$

$$
\mathcal {I} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \tanh ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) g _ {f} ^ {(t) (\nu \tau)} i _ {f} ^ {(t) (\nu \tau)} \left(1 - i _ {f} ^ {(t) (\nu \tau)}\right),
$$

$$
\mathcal {F} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \tanh ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) c _ {f} ^ {(t) (\nu \tau - 1)} f _ {f} ^ {(t) (\nu \tau)} \left(1 - f _ {f} ^ {(t) (\nu \tau)}\right),
$$

$$
\mathcal {G} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \tanh ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) i _ {f} ^ {(t) (\nu \tau)} \left(1 - \left(g _ {f} ^ {(t) (\nu \tau)}\right) ^ {2}\right),\tag{6.40}
$$

and

$$
\begin{array}{r l} & H _ {f f ^ {\prime}} ^ {(t) (\nu \tau) _ {a}} = \Theta_ {f} ^ {o _ {a} (\nu + 1) f ^ {\prime}} \mathcal {O} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} + \Theta_ {f} ^ {f _ {a} (\nu + 1) f ^ {\prime}} \mathcal {F} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} \\ & \qquad + \Theta_ {f} ^ {g _ {a} (\nu + 1) f ^ {\prime}} \mathcal {G} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} + \Theta_ {f} ^ {i _ {a} (\nu + 1) f ^ {\prime}} \mathcal {I} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)}. \end{array}\tag{6.41}
$$

## 6.5.5 Weight and coefficient updates in a LSTM

As for the RNN, (but with the H defined in section 6.5.4), we get for $\nu = 1$

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} h _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)},\tag{6.42}
$$

(6.43)

and otherwise

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} y _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)},\tag{6.44}
$$

(ντ)(t)δ( (ν −1τ)(t) ρf

(6.45)

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\tau} (\nu) f} = \sum_ {\tau = 1} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} y _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)},\tag{6.46}
$$

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)},\tag{6.47}
$$

$$
\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)}\tag{6.48}
$$

<!-- page: 90 -->

and

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} y _ {f ^ {\prime}} ^ {(t) (N - 1 \tau)} \delta_ {f} ^ {(t) (N - 1 \tau)}.\tag{6.49}
$$

## Appendix

## 6.A Backpropagation trough Batch Normalization

For Backpropagation, we will need

$$
\frac {\partial y _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \gamma_ {f} ^ {(\nu \tau)} \frac {\partial \tilde {h} _ {f ^ {\prime}} ^ {(t) (\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}}.\tag{6.50}
$$

Since

$$
\frac {\partial h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \delta_ {t} ^ {t ^ {\prime}} \delta_ {f} ^ {f ^ {\prime}}, \quad \frac {\partial \hat {h} _ {f ^ {\prime}} ^ {(\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}};\tag{6.51}
$$

and

$$
\frac {\partial \left(\hat {\sigma} _ {f ^ {\prime}} ^ {(\nu \tau)}\right) ^ {2}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \frac {2 \delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (\nu \tau)} - \hat {h} _ {f} ^ {(\nu \tau)}\right),\tag{6.52}
$$

we get

$$
\begin{array}{l} \frac {\partial \tilde {h} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \frac {\delta_ {f} ^ {f ^ {\prime}}}{T _ {\mathrm{mb}}} \left[ \frac {T _ {\mathrm{mb}} \delta_ {t} ^ {t ^ {\prime}} - 1}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu \tau)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} - \frac {\left(h _ {f} ^ {(t ^ {\prime}) (\nu \tau)} - \hat {h} _ {f} ^ {(\nu \tau)}\right) \left(h _ {f} ^ {(t) (\nu \tau)} - \hat {h} _ {f} ^ {(\nu \tau)}\right)}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu \tau)}\right) ^ {2} + \epsilon\right) ^ {\frac {3}{2}}} \right] \\ = \frac {\delta_ {f} ^ {f ^ {\prime}}}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu \tau)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu \tau)} \tilde {h} _ {f} ^ {(t) (\nu \tau)}}{T _ {\mathrm{mb}}} \right]. \end{array} \tag {6.5}\tag{6.53}
$$

<!-- page: 91 -->

To ease the notation we will denote

$$
\tilde {\gamma} _ {f} ^ {(\nu \tau)} = \frac {\gamma_ {f} ^ {(\nu \tau)}}{\left(\left(\hat {\sigma} _ {f} ^ {(\nu \tau)}\right) ^ {2} + \epsilon\right) ^ {\frac {1}{2}}}.\tag{6.54}
$$

so that

$$
\frac {\partial y _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}}{\partial h _ {f} ^ {(t) (\nu \tau)}} = \tilde {\gamma} _ {f} ^ {(\nu \tau)} \delta_ {f} ^ {f ^ {\prime}} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu \tau)} \tilde {h} _ {f} ^ {(t) (\nu \tau)}}{T _ {\mathrm{mb}}} \right].\tag{6.55}
$$

This modifies the error rate backpropagation, as well as the formula for the weight update $( y ^ { \prime } s$ instead of $h ^ { \prime } s )$ . In the following we will use the formula

$$
J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} = \tilde {\gamma} _ {f} ^ {(\nu \tau)} \left[ \delta_ {t} ^ {t ^ {\prime}} - \frac {1 + \tilde {h} _ {f} ^ {(t ^ {\prime}) (\nu \tau)} \tilde {h} _ {f} ^ {(t) (\nu \tau)}}{T _ {\mathrm{mb}}} \right].\tag{6.56}
$$

## 6.B RNN Backpropagation

## 6.B.1 RNN Error rate updates: details

Recalling the error rate definition

$$
\delta_ {f} ^ {(t) (\nu \tau)} = \frac {\delta}{\delta h _ {f} ^ {(t) (\nu + 1 \tau)}} J (\Theta),\tag{6.57}
$$

we would like to compute it for all existing values of ν and τ. As computed in chapter 4, one has for the maximum ν value

$$
\delta_ {f} ^ {(t) (N - 1 \tau)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N \tau)} - y _ {f} ^ {(t) (\tau)}\right).\tag{6.58}
$$

Now since (taking Batch Normalization into account)

$$
h _ {f} ^ {(t) (N \tau)} = o \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} \Theta_ {f ^ {\prime}} ^ {f} y _ {f} ^ {(t) (N - 1 \tau)}\right),\tag{6.59}
$$

<!-- page: 92 -->

and

$$
h _ {f} ^ {(t) (\nu \tau)} = \tanh \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {\nu (\nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime}} ^ {\tau (\nu) f} y _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}\right),\tag{6.60}
$$

we get for

$$
\begin{array}{l} \delta_ {f} ^ {(t) (N - 2 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {N} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau)} \right. \\ \left. + \sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 2 \tau + 1)} \right]. \end{array}\tag{6.61}
$$

Let us work out explicitly once (for a regression cost function and a trivial identity output function)

$$
\begin{array}{r l} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} & = \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {N - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {f ^ {\prime}} \frac {\delta y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (N - 1 \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \\ & = \Theta_ {f} ^ {f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (N - 1 \tau)}. \end{array}\tag{6.62}
$$

as well as

$$
\begin{array}{l} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} = \left[ 1 - \left(h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)}\right) ^ {2} \right] \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {N - 1} - 1} \Theta_ {f ^ {\prime \prime}} ^ {\tau (N - 1) f ^ {\prime}} \frac {\delta y _ {f ^ {\prime \prime}} ^ {(t ^ {\prime}) (N - 1 \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \\ = \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)} \Theta_ {f} ^ {\tau (N - 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (N - 1 \tau)}. \end{array}\tag{6.63}
$$

Thus

$$
\begin{array}{r l} & {\delta_ {f} ^ {(t) (N - 2 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (N - 1 \tau)} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {N} - 1} \Theta_ {f} ^ {f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau)} \right.} \\ & {\qquad + \left. \sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)} \Theta_ {f} ^ {\tau (N - 1) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 2 \tau + 1)} \right].} \end{array}\tag{6.64}
$$

<!-- page: 93 -->

Here we adopted the convention that the $\delta^{(t')(N-2\tau+1)}' \mathrm{s}   are   0   if   \tau = T$ . In a similar way, we derive for $\nu \leq N - 1$

$$
\begin{array}{c} \delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \Theta_ {f} ^ {\nu (\nu + 1) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)} \right. \\ \left. + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau + 1)} \Theta_ {f} ^ {\tau (\nu) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - 1 \tau + 1)} \right]. \end{array}\tag{6.65}
$$

Defining

$$
\mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)} = 1, \quad \Theta_ {f} ^ {\nu (N) f ^ {\prime}} = \Theta_ {f} ^ {f ^ {\prime}},\tag{6.66}
$$

the previous $\delta _ { f } ^ { ( t ) \left( \nu - 1 \tau \right) }$ formula extends to the case $\nu = N - 1$ . To unite the RNN and the LSTM formulas, let us finally define (with a either $\tau$ or ν

$$
\mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau) _ {a}} = \mathcal {T} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \Theta_ {f} ^ {a (\nu + 1) f ^ {\prime}},\tag{6.67}
$$

thus (defining $b _ { 0 } = \nu$ and $b _ { 1 } = \tau )$

$$
\delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b \epsilon}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)}.\tag{6.68}
$$

## 6.B.2 RNN Weight and coefficient updates: details

We want here to derive

$$
\Delta_ {f ^ {\prime}} ^ {\nu (\nu) f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {\nu (\nu) f}} J (\Theta) \quad \Delta_ {f ^ {\prime}} ^ {\tau (\nu) f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {\tau (\nu) f}} J (\Theta).\tag{6.69}
$$

We first expand

$$
\begin{array}{r l} & {\Delta_ {f ^ {\prime}} ^ {\nu (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(t) (\nu \tau)}}{\partial \Theta_ {f ^ {\prime}} ^ {\nu (\nu) f}} \delta_ {f ^ {\prime \prime}} ^ {(t) (\nu - 1 \tau)},} \\ & {\Delta_ {f ^ {\prime}} ^ {\tau (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(t) (\nu \tau)}}{\partial \Theta_ {j ^ {\prime}} ^ {\tau (\nu) f}} \delta_ {f ^ {\prime \prime}} ^ {(t) (\nu - 1 \tau)},} \end{array}\tag{6.70}
$$

<!-- page: 94 -->

so that

$$
\Delta_ {f ^ {\prime}} ^ {\nu (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \mathcal {T} _ {f} ^ {(t) (\nu \tau)} \delta_ {f} ^ {(t) (\nu - 1 \tau)} h _ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau)},\tag{6.71}
$$

$$
\Delta_ {f ^ {\prime}} ^ {\tau (\nu) f} = \sum_ {\tau = 1} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \mathcal {T} _ {f} ^ {(t) (\nu \tau)} \delta_ {f} ^ {(t) (\nu - 1 \tau)} h _ {f ^ {\prime}} ^ {(t) (\nu \tau - 1)}.\tag{6.72}
$$

We also have to compute

$$
\Delta_ {f ^ {\prime}} ^ {f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {f}} J (\Theta)  .\tag{6.73}
$$

We first expand

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {N} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(t) (N \tau)}}{\partial \Theta_ {f ^ {\prime}} ^ {f}} \delta_ {f ^ {\prime \prime}} ^ {(t) (N - 1 \tau)}\tag{6.74}
$$

so that

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f ^ {\prime}} ^ {(t) (N - 1 \tau)} \delta_ {f} ^ {(t) (N - 1 \tau)}.\tag{6.75}
$$

Finally, we need

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \frac {\partial}{\partial \beta_ {f} ^ {(\nu \tau)}} J (\Theta) \quad \Delta_ {f} ^ {\gamma (\nu \tau)} = \frac {\partial}{\partial \gamma_ {f} ^ {(\nu \tau)}} J (\Theta)  .\tag{6.76}
$$

First

$$
\begin{array}{l} \Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)}}{\partial \beta_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(t) (\nu \tau + 1)}}{\partial \beta_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \right], \\ \Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)}}{\partial \gamma_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(t) (\nu \tau + 1)}}{\partial \gamma_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \right]. \end{array}\tag{6.77}
$$

<!-- page: 95 -->

So that

$$
\begin{array}{r l} & {\Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} \Theta_ {f} ^ {\nu (\nu + 1) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} \right.} \\ & {\qquad + \left. \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t) (\nu \tau + 1)} \Theta_ {f} ^ {\tau (\nu) f ^ {\prime}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \right],} \\ & {\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} \Theta_ {f} ^ {\nu (\nu + 1) f^ {\prime}} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} \right.} \\ & {\qquad + \left. \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \mathcal {T} _ {f ^ {\prime}} ^ {(t) (\nu \tau + 1)} \Theta_ {f} ^ {\tau (\nu) f ^ {\prime}} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \delta_ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \right],} \end{array}\tag{6.78}
$$

(6.79)

which we can rewrite as

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)},\tag{6.80}
$$

$$
\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b \epsilon}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)}.\tag{6.81}
$$

## 6.C LSTM Backpropagation

## 6.C.1 LSTM Error rate updates: details

As for the RNN

$$
\delta_ {f} ^ {(t) (N - 1 \tau)} = \frac {1}{T _ {\mathrm{mb}}} \left(h _ {f} ^ {(t) (N \tau)} - y _ {f} ^ {(t) (\tau)}\right).\tag{6.82}
$$

Before going any further, it will be useful to define

$$
\begin{array}{r l} & {\mathcal {O} _ {f} ^ {(t) (\nu \tau)} = h _ {f} ^ {(t) (\nu \tau)} \left(1 - o _ {f} ^ {(t) (\nu \tau)}\right),} \\ & {\mathcal {I} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \mathrm{tanh} ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) g _ {f} ^ {(t) (\nu \tau)} i _ {f} ^ {(t) (\nu \tau)} \left(1 - i _ {f} ^ {(t) (\nu \tau)}\right),} \\ & {\mathcal {F} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \mathrm{tanh} ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) c _ {f} ^ {(t) (\nu \tau - 1)} f _ {f} ^ {(t) (\nu \tau)} \left(1 - f _ {f} ^ {(t) (\nu \tau)}\right)} \\ & {\mathcal {G} _ {f} ^ {(t) (\nu \tau)} = o _ {f} ^ {(t) (\nu \tau)} \left(1 - \mathrm{tanh} ^ {2} \left(c _ {f} ^ {(t) (\nu \tau)}\right)\right) i _ {f} ^ {(t) (\nu \tau)} \left(1 - \left(g _ {f} ^ {(t) (\nu \tau)}\right) ^ {2}\right),} \end{array}\tag{6.83}
$$

<!-- page: 96 -->

and

$$
\begin{array}{r l} & H _ {f f ^ {\prime}} ^ {(t) (\nu \tau) _ {a}} = \Theta_ {f} ^ {o _ {a} (\nu + 1) f ^ {\prime}} \mathcal {O} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} + \Theta_ {f} ^ {f _ {a} (\nu + 1) f ^ {\prime}} \mathcal {F} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} \\ & \qquad + \Theta_ {f} ^ {g _ {a} (\nu + 1) f ^ {\prime}} \mathcal {G} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)} + \Theta_ {f} ^ {i _ {a} (\nu + 1) f ^ {\prime}} \mathcal {I} _ {f ^ {\prime}} ^ {(t) (\nu + 1 \tau)}. \end{array}\tag{6.84}
$$

As for RNN, we will start off by looking at

$$
\begin{array}{r l} \delta_ {f} ^ {(t) (N - 2 \tau)} = & \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {N} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau)} \right. \\ & \left. + \sum_ {f ^ {\prime} = 0} ^ {F _ {N - 1} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 1 \tau + 1)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (N - 2 \tau + 1)} \right]. \end{array}\tag{6.85}
$$

We will be able to get our hands on the second term with the general formula, so let us first look at

$$
\frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)}}{\delta h _ {f} ^ {(t) (N - 1 \tau)}} = \Theta_ {f} ^ {f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (N - 1 \tau)},\tag{6.86}
$$

which is is similar to the RNN case. Let us put aside the second term of $\delta _ { f } ^ { \left( t \right) \left( N - 2 \tau \right) }$ , and look at the general case

$$
\delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau + 1)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - 1 \tau + 1)} \right],\tag{6.87}
$$

which involves to study in details

$$
\begin{array}{l} \frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = \frac {\delta o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} \mathsf {t a n h} c _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \\ \qquad + \frac {\delta c _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \left[ 1 - \mathsf {t a n h} ^ {2} c _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \right]. \end{array}\tag{6.88}
$$

<!-- page: 97 -->

Now

$$
\begin{array}{l} \frac {\delta o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \left[ 1 - o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \right] \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \Theta_ {f ^ {\prime \prime}} ^ {o _ {\nu} (\nu + 1) f ^ {\prime}} \frac {\delta y _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} \\ = o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \left[ 1 - o _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \right] \Theta_ {f} ^ {o _ {\nu} (\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)}, \end{array}\tag{6.89}
$$

and

$$
\begin{array}{r l} & {\frac {\delta c _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = \frac {\delta i _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} g _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} + \frac {\delta g _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} i _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}} \\ & {\qquad + \frac {\delta f _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} c _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)}.} \end{array}\tag{6.90}
$$

We continue our journey

$$
\begin{array}{l} \frac {\delta i _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = i _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \left[ 1 - i _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \right] \Theta_ {f} ^ {i _ {\nu} (\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)}, \\ \frac {\delta f _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = f _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \left[ 1 - f _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)} \right] \Theta_ {f} ^ {f _ {\nu} (\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)}, \\ \frac {\delta g _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = \left[ 1 - \left(g _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}\right) ^ {2} \right] \Theta_ {f} ^ {g _ {\nu} (\nu + 1) f ^ {\prime}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)}, \end{array}\tag{6.91}
$$

and our notations now come handy

$$
\frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu + 1 \tau)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} H _ {f f ^ {\prime}} ^ {(t) (\nu \tau) _ {\nu}}.\tag{6.92}
$$

This formula also allows us to compute the second term for $\delta _ { f } ^ { \left( t \right) \left( N - 2 \tau \right) }$ . In a totally similar manner

$$
\frac {\delta h _ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau + 1)}}{\delta h _ {f} ^ {(t) (\nu \tau)}} = J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} H _ {f f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1) _ {\tau}}.\tag{6.93}
$$

<!-- page: 98 -->

Going back to our general formula

$$
\begin{array}{c} \delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \left[ \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu \tau) _ {\nu}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu \tau)} \right. \\ \left. + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1) _ {\tau}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - 1 \tau + 1)} \right], \end{array}\tag{6.94}
$$

and as in the RNN case, we re-express it as (defining $b _ { 0 } = \nu$ and $b _ { 1 } = \tau )$

$$
\delta_ {f} ^ {(t) (\nu - 1 \tau)} = \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}}} J _ {f} ^ {(t t ^ {\prime}) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t ^ {\prime}) (\nu - \epsilon \tau + \epsilon)}.\tag{6.95}
$$

This formula is also valid for $\nu = N - 1$ if we define as for the RNN case

$$
\mathcal {H} _ {f ^ {\prime}} ^ {(t ^ {\prime}) (N \tau)} = 1,
$$

$$
\Theta_ {f} ^ {\nu (N) f ^ {\prime}} = \Theta_ {f} ^ {f ^ {\prime}},\tag{6.96}
$$

## 6.C.2 LSTM Weight and coefficient updates: details

We want to compute

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f}} J (\Theta) \quad \Delta_ {f ^ {\prime}} ^ {\rho_ {\tau} (\nu) f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {\rho_ {\tau} (\nu) f}} J (\Theta),\tag{6.97}
$$

with $\rho = \left( f , i , g , o \right)$ . First we expand

$$
\begin{array}{c} \Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(\nu \tau) (t)}}{\partial \Theta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu) f}} \frac {\partial}{\partial h _ {f ^ {\prime \prime}} ^ {(\nu \tau) (t)}} J (\Theta) \\ = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {\nu} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(\nu \tau) (t)}}{\partial \Theta_ {f ^ {\prime}}} \delta_ {f ^ {\prime \prime}} ^ {(\nu \tau) (t)}, \end{array}\tag{6.98}
$$

so that (with $\rho ^ { ( \nu \tau ) } = ( \mathcal { F } , \mathcal { I } , \mathcal { G } , \mathcal { O } ) )$ if $\nu = 1$

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu -) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} h _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)},\tag{6.99}
$$

<!-- page: 99 -->

and else

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\nu} (\nu -) f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} y _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)},\tag{6.100}
$$

$$
\Delta_ {f ^ {\prime}} ^ {\rho_ {\tau} (\nu) f} = \sum_ {\tau = 1} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \rho_ {f} ^ {(\nu \tau) (t)} \delta_ {f} ^ {(\nu \tau) (t)} y _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)}.\tag{6.101}
$$

We will now need to compute

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \frac {\partial}{\partial \beta_ {f} ^ {(\nu \tau)}} J (\Theta) \quad \Delta_ {f} ^ {\gamma (\nu \tau)} = \frac {\partial}{\partial \gamma_ {f} ^ {(\nu \tau)}} J (\Theta)  .\tag{6.102}
$$

For that we need to look at

$$
\begin{array}{l} \Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(\nu + 1 \tau) (t ^ {\prime})}}{\partial \beta_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(\nu \tau) (t ^ {\prime})} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \sum_ {t ^ {\prime} = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime}} ^ {(\nu \tau + 1) (t ^ {\prime})}}{\partial \beta_ {f} ^ {(\nu \tau)}} \delta_ {f ^ {\prime}} ^ {(\nu - 1 \tau + 1) (t ^ {\prime})} \\ = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \left\{\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu \tau)} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau + 1)} \right\}. \end{array} \tag {6.10}\tag{6.103}
$$

and

$$
\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \left\{\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu \tau)} \delta_ {f ^ {\prime}} ^ {(t) (\nu \tau)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} H _ {f f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \delta_ {f ^ {\prime}} ^ {(t) (\nu - 1 \tau + 1)} \right\}\tag{6.104}
$$

which we can rewrite as

$$
\Delta_ {f} ^ {\beta (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)},\tag{6.105}
$$

$$
\Delta_ {f} ^ {\gamma (\nu \tau)} = \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \tilde {h} _ {f} ^ {(t) (\nu \tau)} \sum_ {\epsilon = 0} ^ {1} \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu + 1 - \epsilon} - 1} \mathcal {H} _ {f f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon) _ {b _ {\epsilon}}} \delta_ {f ^ {\prime}} ^ {(t) (\nu - \epsilon \tau + \epsilon)}.\tag{6.106}
$$

Finally, as in the RNN case

<!-- page: 100 -->

$$
\Delta_ {f ^ {\prime}} ^ {f} = \frac {\partial}{\partial \Theta_ {f ^ {\prime}} ^ {f}} J (\Theta).\tag{6.107}
$$

We first expand

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {f ^ {\prime \prime} = 0} ^ {F _ {N} - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} \frac {\partial h _ {f ^ {\prime \prime}} ^ {(t) (N \tau)}}{\partial \Theta_ {f ^ {\prime}} ^ {f}} \delta_ {f ^ {\prime \prime}} ^ {(t) (N - 1 \tau)}\tag{6.108}
$$

so that

$$
\Delta_ {f ^ {\prime}} ^ {f} = \sum_ {\tau = 0} ^ {T - 1} \sum_ {t = 0} ^ {T _ {\mathrm{mb}} - 1} h _ {f ^ {\prime}} ^ {(t) (N - 1 \tau)} \delta_ {f} ^ {(t) (N - 1 \tau)}.\tag{6.109}
$$

<!-- page: 101 -->

## 6.D Peephole connexions

Some LSTM variants probe the cell state to update the gate themselves. This is illustrated in figure 6.7

![](images/page_100_image_4.jpg)

Figure 6.7: LSTM hidden unit with peephole

Peepholes modify the gate updates in the following way

$$
i _ {f} ^ {(\nu \tau) (t)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {i _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left[ \Theta_ {f ^ {\prime}} ^ {i _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)} + \Theta_ {f ^ {\prime}} ^ {c _ {i} (\nu) f} c _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)} \right]\right),\tag{6.110}
$$

$$
f _ {f} ^ {(\nu \tau) (t)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {f _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left[ \Theta_ {f ^ {\prime}} ^ {f _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)} + \Theta_ {f ^ {\prime}} ^ {c _ {f} (\nu) f} c _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)} \right]\right),\tag{6.111}
$$

$$
o _ {f} ^ {(\nu \tau) (t)} = \sigma \left(\sum_ {f ^ {\prime} = 0} ^ {F _ {\nu - 1} - 1} \Theta_ {f ^ {\prime}} ^ {o _ {\nu} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu - 1 \tau) (t)} + \sum_ {f ^ {\prime} = 0} ^ {F _ {\nu} - 1} \left[ \Theta_ {f ^ {\prime}} ^ {o _ {\tau} (\nu) f} h _ {f ^ {\prime}} ^ {(\nu \tau - 1) (t)} + \Theta_ {f ^ {\prime}} ^ {c _ {o} (\nu) f} c _ {f ^ {\prime}} ^ {(\nu \tau) (t)} \right]\right),\tag{6.112}
$$

which also modifies the LSTM backpropagation algorithm in a non-trivial way. As it as been shown that different LSTM formulations lead to pretty similar

<!-- page: 102 -->

results, we leave to the reader the derivation of the backpropagation update rules as an exercise.

<!-- page: 103 -->

# Chapter 7

# Input Convolution Layer . . . P + 2 N P + 2 T F C R C R CS Weights . . . . . . . p F . . Output Convolution Layer . . . p N p T p F ConclusionInput Convolution Layer . . . N + 2P <sup>T + 2</sup>P F RC RC SC Weights . . . . . . . Fp . . Output Convolution Layer... Np Tp Fp

![](images/page_102_image_2.jpg)

e have come to the end of our journey. I hope this note lived up W to its promises, and that the reader now understands better how a neural network is designed and how it works under the hood. To wrap it up, we have seen the architecture of the three most common neural networks, as well as the careful mathematical derivation of their training formulas.

Deep Learning seems to be a fast evolving field, and this material might be out of date in a near future, but the index approach adopted will still allow the reader – as it as helped the writer – to work out for herself what is behind the next state of the art architectures.

Until then, one should have enough material to encode from scratch its own FNN, CNN and RNN-LSTM, as the author did as an empirical proof of his formulas.

<!-- page: 104 -->

<!-- page: 105 -->

## Bibliography

[1] Nitish Srivastava et al. “Dropout: A Simple Way to Prevent Neural Networks from Overfitting”. In: J. Mach. Learn. Res. 15.1 (Jan. 2014), pp. 1929–1958. issn: 1532-4435. url: [http : / / dl . acm . org / citation . cfm ? id = 2627435.2670313](http://dl.acm.org/citation.cfm?id=2627435.2670313).

[2] Sergey Ioffe and Christian Szegedy. “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift”. In: (Feb. 2015).

[3] Yann Lecun et al. “Gradient-based learning applied to document recognition”. In: Proceedings of the IEEE. 1998, pp. 2278–2324.

[4] Karen Simonyan and Andrew Zisserman. “Very Deep Convolutional Networks for Large-Scale Image Recognition”. In: CoRR abs/1409.1556 (2014). url: [http://arxiv.org/abs/1409.1556](http://arxiv.org/abs/1409.1556).

[5] Kaiming He et al. “Deep Residual Learning for Image Recognition”. In: 7 (Dec. 2015).

[6] Alex Graves. Supervised Sequence Labelling with Recurrent Neural Networks. 2011.

[7] Felix A. Gers, Jürgen A. Schmidhuber, and Fred A. Cummins. “Learning to Forget: Continual Prediction with LSTM”. In: Neural Comput. 12.10 (Oct. 2000), pp. 2451–2471. issn: 0899-7667. doi: [10.1162/089976600300015015](http://dx.doi.org/10.1162/089976600300015015). url: [http://dx.doi.org/10.1162/089976600300015015](http://dx.doi.org/10.1162/089976600300015015).

[8] F. Rosenblatt. “The Perceptron: A Probabilistic Model for Information Storage and Organization in The Brain”. In: Psychological Review (1958), pp. 65–386.

[9] Yann LeCun et al. “Effiicient BackProp”. In: Neural Networks: Tricks of the Trade, This Book is an Outgrowth of a 1996 NIPS Workshop. London, UK, UK: Springer-Verlag, 1998, pp. 9–50. isbn: 3-540-65311-2. url: [http://dl.acm.org/citation.cfm?id=645754.668382](http://dl.acm.org/citation.cfm?id=645754.668382).

[10] Ning Qian. “On the momentum term in gradient descent learning algorithms”. In: Neural Networks 12.1 (1999), pp. 145 –151. issn: 0893-6080. doi: [http://dx.doi.org/10.1016/S0893-6080(98)00116-6](http://dx.doi.org/http://dx.doi.org/10.1016/S0893-6080%2898%2900116-6). url: [http://www.sciencedirect.com/science/article/pii/S0893608098001166](http://www.sciencedirect.com/science/article/pii/S0893608098001166).

[11] Yurii Nesterov. “A method for unconstrained convex minimization problem with the rate of convergence O (1/k2)”. In: Doklady an SSSR. Vol. 269. 3. 1983, pp. 543–547.

<!-- page: 106 -->

[12] John Duchi, Elad Hazan, and Yoram Singer. “Adaptive Subgradient Methods for Online Learning and Stochastic Optimization”. In: J. Mach. Learn. Res. 12 (July 2011), pp. 2121–2159. issn: 1532-4435. url: [http://dl.acm.org/citation.cfm?id=1953048.2021068](http://dl.acm.org/citation.cfm?id=1953048.2021068).

[13] Matthew D. Zeiler. “ADADELTA: An Adaptive Learning Rate Method”. In: CoRR abs/1212.5701 (2012). url: [http://dblp.uni- trier.de/db/ journals/corr/corr1212.html#abs-1212-5701](http://dblp.uni-trier.de/db/journals/corr/corr1212.html#abs-1212-5701).

[14] Diederik Kingma and Jimmy Ba. “Adam: A Method for Stochastic Optimization”. In: (Dec. 2014).

[15] Rupesh K. Srivastava, Klaus Greff, and Jurgen Schmidhuber. “Highway Networks”. In: (). url: [http://arxiv.org/pdf/1505.00387v1.pdf](http://arxiv.org/pdf/1505.00387v1.pdf).

[16] Jiuxiang Gu et al. “Recent Advances in Convolutional Neural Networks”. In: CoRR abs/1512.07108 (2015).

[17] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. “ImageNet Classification with Deep Convolutional Neural Networks”. In: Advances in Neural Information Processing Systems 25. Ed. by F. Pereira et al. Curran Associates, Inc., 2012, pp. 1097–1105. url: [http : / / papers . nips . cc / paper / 4824 - imagenet - classification - with - deep - convolutional - neural-networks.pdf](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf).

[18] Christian Szegedy et al. “Going Deeper with Convolutions”. In: Computer Vision and Pattern Recognition (CVPR). 2015. url: [http://arxiv.org/abs/1409.4842](http://arxiv.org/abs/1409.4842).

[19] Gao Huang et al. “Densely Connected Convolutional Networks”. In: (July 2017).
