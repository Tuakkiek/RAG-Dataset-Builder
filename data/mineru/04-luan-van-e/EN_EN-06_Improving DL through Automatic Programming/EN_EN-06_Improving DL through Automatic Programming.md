<!-- page: 1 -->

# Improving Deep Learning through Automatic Programming

Master’s Thesis in Computer Science

Dang Ha The Hien

May 14, 2014 Halden, Norway

<!-- page: 2 -->

<!-- page: 3 -->

## Abstract

Deep learning and deep architectures are emerging as the best machine learning methods so far in many practical applications such as reducing the dimensionality of data, image classification, speech recognition or object segmentation. . . . In fact, many leading technology companies such as Google, Microsoft or IBM are researching and using deep architectures in their systems to replace other traditional models. Therefore, improving the performance of these models could make a very strong impact in the area of machine learning. However, deep learning is a very fast-growing research domain with many core methodologies and paradigms just discovered over the last few years. This thesis will first serve as a short summary of deep learning, which tries to include all of the most important ideas in this research area. Based on this knowledge, we suggested, and conducted some experiments to investigate the possibility of improving the deep learning based on automatic programming (ADATE). Although our experiments did produce good results, there are still many more possibilities that we could not try due to limited time as well as some limitations of the current ADATE version. I hope that this thesis can promote future work on this topic, especially when the next version of ADATE comes out. This thesis also includes a short analysis of the power of ADATE system, which could be very useful for other researchers who want to know what it is capable of.

Keywords: Deep Learning, Automatic Programming, ADATE, Neural Networks, Machine Learning

<!-- page: 4 -->

<!-- page: 5 -->

## Acknowledgments

First and foremost, I would like to thank my thesis supervisor Prof. Roland Olsson for the advice, support, and kindness that he has given to me over the past year. Without him, I definitely could not complete this thesis. Many parts of this thesis were done by both of us. Therefore, I used “we” as the subject in this thesis to indicate that fact. I would also like to thank my fellow students, especially Kristin Larsen, who has allowed me to use her experiment result in my thesis. In addition, I want to thank my family and friends, who were always beside and support me in difficult times. Last but not least, I want to thank my best friend, Nguyet Thanh, who took me out of my loneliness and encouraged me to keep following my dream.

<!-- page: 6 -->

<!-- page: 7 -->

## Prerequisites

Although machine learning as well as neural networks and deep learning is a very specialized field, which covers many different aspects of mathematics, physics, and biology. . . , we believe that a graduated student in computer science could easily understand the main ideas and results in this report. However, to get a deeper understanding, the reader should have basic knowledge about probability, statistics, linear algebra, and calculus. He or she should also be familiar with basic mathematics optimization concepts like Taylor series and steepest gradient descent.

<!-- page: 8 -->

<!-- page: 9 -->

## Contents

- Abstract
- Acknowledgments
- Prerequisites
- List of Figures
- List of Tables
- Listings
- 1 Introduction
- 1.1 Machine Learning ..... 1
- 1.2 Artificial Neural Networks ..... 2
- 1.3 Deep Architectures and Deep Learning ..... 3
- 1.4 Research Question and Methodology ..... 4
- 1.5 Report Outline ..... 5
- 2 The Need for Deep Learning and Deep Architectures
- 2.1 Deep Architectures on Circuit Problem ..... 7
- 2.2 The Challenges in training Deep Neural Networks ..... 8
- 2.3 Dominance of Deep Learning ..... 8
- 3 Deep Architectures and Related Models
- 3.1 Deep Neural Networks ..... 11
- 3.2 Boltzmann Machines - Related Models ..... 13
- 3.3 AutoEncoders ..... 16
- 4 Gradient-Based Training Algorithms for Neural Networks
- 4.1 First-order Methods ..... 25
- 4.2 Second-order Methods ..... 28
- 4.3 Line Search vs. Trust Region Strategy ..... 31
- 4.4 Initialization Analysis ..... 33
- 4.5 Cascade correlation algorithm ..... 33
- 5 Overfitting and Regularization
- 5.1 Introduction ..... 35
- 5.2 Regularization Overview ..... 39

<!-- page: 10 -->

- 6 Activation Functions 47
- 6.1 Logistic Sigmoid function 47
- 6.2 Hyperbolic tangent and its scaled version 48
- 6.3 Softsign function 49
- 6.4 Rectifier and Softplus function 49
- 6.5 Maxout Function 52
- 7 Introduction to ADATE 55
- 7.1 A Short Introduction to ADATE 55
- 7.2 A Short Analysis of the Power of ADATE System 56
- 8 ADATE Experiments 67
- 8.1 Selecting Target 67
- 8.2 Building Tiny Datasets 69
- 8.3 Design and Implementation 72
- 8.4 Writing Specification file 80
- 8.5 Experiment Results 81
- 8.6 Overfitting Problem 85
- 9 Conclusion and Future Works 89
- 9.1 Future Works 90
- Bibliography 94
- A Neural Network Libraries 95
- A.1 Matrix Library 95
- A.2 Random library 102
- A.3 Neural Network Library 103
- B ADATE Specification for Initialization Experiment 115

<!-- page: 11 -->

## List of Figures

- A typical feed forward neural network . . . . . . . . . . . . . . . . . . . 3
- Activation of a node $j^{th}$ at layer $k^{th}$ is calculated by $x_{jk} = \varphi(\sum_{i=1}^{n} x_{i(k-1)} w_{ijk})$ 3
- Difficulty on object classification task . . . . . . . . . . . . . . . . . . 9
- Hand-designed features examples . . . . . . . . . . . . . . . . . 9
- Deep learning applications . . . . . . . . . . . . . . . . . 10
- Deep neural networks represent input in multi-level feature representations 12
- Pretraining process using auto-encoder . . . . . . . . . . . . . 12
- (Taken from [40]) Left: A general Boltzmann machine. The top layer represents a vector of stochastic binary “hidden” features and the bottom layer represents a vector of stochastic binary “visible” variables. Right: A restricted Boltzmann machine with no hidden to hidden and no visible to visible connections. 13
- (Taken from [41]) Left: Deep Belief Network (DBN), with the top two layers forming an undirected graph and the remaining layers form a belief net with directed, top-down connections Right: Deep BoltzmannMachine (DBM), with both visible-to-hidden and hidden-to-hidden connections but with no within-layer connections. All the connections in a DBM are undirected. 15
- (Taken from [41]) DBN model that was used for MNIST data set 16
- A typical autoencoder 17
- Taken from [28] Each square in the figure above shows the (norm bounded) input image x that maximally actives one of 100 hidden units. We see that the different hidden units have learned to detect edges at different positions and orientations in the image. 20
- Taken from [48] Left: regular autoencoder with weight decay. The learned filters cannot capture interesting structure in the image. Right: a denoising autoencoder with additive Gaussian noise ($\sigma = 0.5$) learns Gabor-like local oriented edge detectors. Very similar to the filters learned by sparse autoencoder. 21
- Taken from [39] Results are sorted in ascending order of classification error on the test set. Best performer and models whose difference with the best performer was not statistically significant are in bold. Notice how the average Jacobian norm (before fine-tuning) appears correlated with the final test error. SAT is the average fraction of saturated units per example. 22

<!-- page: 12 -->

- 3.10 (Taken from [16]) Pretraining consists of learning a stack of RBMs, each having only one layer of feature detectors. The learned feature activations of one RBM are used as the “data” for training the next RBM in the stack. After the pretraining, the RBMs are “unrolled” to create a deep autoencoder, which is then fine-tuned using back propagation of error derivatives . 23
- 3.11 (Taken from [16]) (A) The two dimensional codes for 500 digits of each class produced by taking the first two principal components of all 60,000 training images.(B) The two dimensional codes found by a 784–1000–500–250–2 autoencoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 5.1 Underfitting and Overfitting in classification task, taken from [30] . . . . . . 36
- 5.2 Underfitting and Overfitting in regression task, taken from [30] . . . . . . 36
- 5.3 Error curves in cross validation methods . . . . . . . . . . . . . . . . . 37
- 5.4 Posterior distribution . . . . . . . . . . . . . . . . . . . 39
- 5.5 Adding Gaussian noise to inputs, taken from [15] . . . . . . . . . . . 42
- 5.6 CNN architecture used in MNIST problem [24] . . . . . . . . . . 44
- 6.1 The sigmoid, tanh, and scaled tanh functions . . . . . . 48
- 6.2 Taken from [4], tanh versus the softsign, which converges polynomially instead of exponentially towards its asymptotes. 49
- 6.3 Taken from [10], Sparse propagation of activations and gradients in network of rectifier units. The input selects a subset of active neurons and computation is linear in this subset. 51
- 6.4 Taken from [10], Rectifier and softplus activation functions. The second one is a smooth version of the first. 51
- 6.5 Taken from [11], Graphical depiction of how the maxout activation function can implement the rectified linear, absolute value rectifier, and approximate the quadratic activation function. This diagram is 2D and only shows how maxout behaves with a 1D input, but in multiple dimensions a maxout unit can approximate arbitrary convex functions. 53
- 7.1 The equivalent decision tree of the ADATE solution for edge detection problem; Left branches are the True cases. 58
- 7.2 Taken from [21], mobile navigation example: Item A is selected, and the user has pressed the up-button. The model has to predict which item the user intends to select. 60
- 8.1 Elastic deformation and TinyDigits. First line: a hand-designed pattern for the digit “0” and its deformed versions. Two bottom lines: examples of generated digits from 0 to 9. Note that all of these deformed images are intelligible. 70
- 8.2 From top to bottom: MNIST, CIFAR-10 and SVHN datasets. 71
- 8.3 General flow chart of gradient-based training algorithms for Neural Networks 79
- 8.4 Histogram of 10000 instances drawn from the tanh(tanh(randn(.))) distribution. 82
- 8.5 Learning curves for negative log likelihood training cost. 86
- 8.6 Learning curves on negative log likelihood validation cost. 86

<!-- page: 13 -->

- 8.7 Learning curves of sparse3, sparse\*, and normalized\* tested on 4-layer neural networks using a 0.05 learning rate. Each method was applied for 10 different initialization seeds. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
- 8.8 Experiment on testing overfitting sources: Architecture, Batchsize, Learning Rate, Momentum and Weight Decay. The first value for each factor was the value that used during the ADATE training process . . . . . . . . . . . . . 87
- 8.9 Experiment on testing overfitting on datasets . . . . . . . . . . . . . . . . 87

<!-- page: 14 -->

<!-- page: 15 -->

## List of Tables

- 8.1 Parameters used when training on MNIST dataset ..... 68
- 8.2 Test error rates after first 100 iterations for different learning rates and initializations ..... 68
- 8.3 Test error rates after first 100 iterations for different initializations at the same learning rates ..... 69
- 8.4 Settings used for the experiments ..... 83
- 8.5 Validation error rates after specific training epochs for different network depth ..... 84
- 8.6 Average test error (10 initialization seeds) for best validation for different network structures ..... 85
- 8.7 Gridsearch for the two constants in sparse-3 ..... 85

<!-- page: 16 -->

<!-- page: 17 -->

## Listings

- 7.1 Clean version of the best synthesized program for edge detection problem . 57
- 7.2 Taken from [21] Pseudo code for the best ADATE's solution . . . . . . . . . 60
- 7.3 One ADATE's solution for CAR problem . . . . . . . . . . . . . . . . 61
- 7.4 Typical ADATE's solution for SPEED problem . . . . . . . . . . . . . . 61
- 7.5 Typical ADATE's solution for Wine quality problem . . . . . . . . . . . . 62
- 7.6 An ADATE's solution for sorting problem . . . . . . . . . . . . . . 64
- 7.7 The original and synthesized errorEstimate function used in EBP algorithm 65
- 8.1 implementation of assertFun() and assertFuns() . . . . . . . . . . . 76
- 8.2 datatype for one layer neural network . . . . . . . . . . . 77
- 8.3 Params datatype which shows all available training options . . . . . . 77
- 8.4 Original sparse and generated sparse-3 initialization functions. The f(.) function is used to generate a list of weights for a node. These weights are then randomly assigned to its incoming connections . . . . . . 81

<!-- page: 18 -->

<!-- page: 19 -->

## Chapter 1

## Introduction

Machine learning is a huge research area based on many ideas in mathematics, physics, and biology. . . . Therefore, in this first part, we only try to give a very brief introduction to machine learning as well as explanations for some related important specialized terms, which hopefully could help one whose major is not machine learning understand the report. Besides, we also introduce artificial neural networks and deep learning - the main field that we are working on in our thesis - their advantages and practical applications as our motivations. Finally, we present our research question, research plan, and outline of the rest of the thesis.

## 1.1 Machine Learning

In the book “Machine Learning” [27], Michell 1997 defined “The field of machine learning is concerned with the question of how to construct computer programs that automatically improve with experience... A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E” and “Machine learning is inherently a multidisciplinary field. It draws on results from artificial intelligence, probability and statistics, computational complexity theory, control theory, information theory, philosophy, psychology, neurobiology, and other fields”.

Another more modern and practical definition is used in the book “Data Mining - Practical Machine Learning Tools and Techniques” [51], where the authors state that “Machine learning provides the technical basis of data mining” and “Data mining ... is to build computer programs that sift through databases automatically, seeking regularities or patterns, ..., generalize to make accurate predictions on future data”.

In general, a machine learning system is based on three main parts: training data, model, and training (i.e learning) algorithm. Each model has a set of parameters that we can use the training algorithm to train (i.e fit) these parameters to the training data, and apply that learned model on another separated test data to measure its real performance. There are two main types of learning: supervised and unsupervised learning. In supervised learning, the training data contains both the input and the desired output (e.g. images and their classifications), and the training algorithms try to construct a mapping (through adapting model’s parameters) that defines the output patterns in terms of the input patterns. In unsupervised learning, the desired output is unknown, and the training algorithms try to discover the structure in data, or even generate new similar data.

<!-- page: 20 -->

Besides, there are many different types of model, from the simplest ones such as ZeroR (just guess the most likely answer - usually used as the baseline performance) or Linear Regression to the much more complex models such as Support Vector Machine (SVM) or Deep Neural Networks (DNNs). Each model has a different assumption (i.e. inductive bias) about the possible input-output mappings (in supervised learning) or possible data distribution (in unsupervised learning). This is because the problem we are dealing with in machine learning is known to be “ill posed” (refers to chapter 5), which cannot be solved unless some prior information is asssumed. For example, in supervised learning, the mapping function may not even exist, or we do not have enough information from the training examples to reconstruct that mapping, or the unavoidable presence of noise in the training examples can make a perfect fitted model useless in practice [14]. An easy example for inductive bias in linear regression is that we assume that the input and the desired output are linearly dependent, so that we can represent the mapping from input to output through a linear equation. The training algorithm for it therefore just searches for the “best” equation.

In this thesis, we focus on supervised learning algorithm in Artificial Neural Networks (ANNs) and Deep Neural Networks (DNNs), which are very powerful models. However, we also introduce some unsupervised learning algorithms and models, which are commonly used in learning process of DNNs.

## 1.2 Artificial Neural Networks

The artificial neural networks (ANNs) have been inspired in part by the observation that biological learning systems are built of very complex webs of interconnected neurons. Artificial neural networks are built out of a densely interconnected set of simple units, where each unit takes a number of real-valued inputs (possibly the outputs of other units) and produces a single real-valued output (which may become the input to many other units) [27]. While ANNs are loosely motivated by biological neural systems, there are many complexities to biological neural systems that are not modeled by ANNs, and many features of the ANNs are known to be inconsistent with biological systems [27]. For example, we consider here ANNs whose individual units output a single constant value, whereas biological neurons output a complex time series of spikes.

There are many different types of neural networks so far. In this report, the term “Neural Networks” is used to implicitly refer to the “Artificial Feed Forward Neural Networks” if there is no other explicit explanation. A feed forward neural network is an artificial neural network where connections between the units do not form a directed cycle, and that therefore can be visualized as a multiple layers network. In Figure 1.1, we showed a typical feed forward neural network with 2 hidden layers (i.e the layers between input and output layers). The mapping between input and output is calculated by feeding the input into the input nodes, going through the hidden nodes and to the output nodes. The value (i.e activation) of each intermediate node is produced by first weighted summing of all its predecessors then going through an activation function (as described in Figure 1.2, please refer to Chapter 6 for more details). Many different activation functions can be used in ANNs, the simplest one is the sgn() function: return +1 when input is greater than 0 and return -1 otherwise; which is used in perceptron networks. The currently popular activation functions are the tanh(), the sigmoid function $\begin{array} { r } { ( f ( x ) = \frac { 1 } { 1 + e ^ { - x } } ) } \end{array}$ and the softmax function. These functions are popular partly because of their differentiability, so we can

<!-- page: 21 -->

easily compute their gradients, which is crucial in gradient-based training algorithm.

![](images/page_20_image_3.jpg)

Figure 1.1: A typical feed forward neural network

![](images/page_20_image_5.jpg)

Figure 1.2: Activation of a node $j ^ { t h }$ at layer $k ^ { t h }$ is calculated by $\textstyle x _ { j k } = \varphi ( \sum _ { i = 1 } ^ { n } x _ { i ( k - 1 ) } w _ { i j k } )$

The training process in ANNs is to adapt all of the connections’ weight to the training data, by minimizing a cost function (i.e. objective function) – which is usually a mean square error (MSE), cross entropy, or negative log likelihood function. There are many different training algorithms for ANNs, including evolution strategy or genetic algorithms. However, gradient-based methods are the most popular. These methods are used to minimize the cost function $f ( x )$ by iteratively following a search direction defined by the gradient (or a function of gradient) of the f function at the current point (details of these methods are provided at Chapter 4. In this thesis, we only focus on studying these gradient-based methods as the main optimization approach for deep learning.

## 1.3 Deep Architectures and Deep Learning

Deep architectures are models that are composed of multiple levels of non-linear operations, such as in Deep Neural Networks (i.e. neural networks with more than 3 hidden

<!-- page: 22 -->

layers), Deep Belief Nets (DBN), or Deep AutoEncoders. Theoretical results suggest that in order to learn the kind of complicated functions that can represent high-level abstractions (e.g., in vision, language, and other AI-level tasks), we may need deep architectures [1]. However, until 2006, training these deep architectures was believed to be difficult due to the well-known vanishing gradient problem. Hinton et al. 2006 [16] have introduced a new learning procedure to successfully tackle this problem. After that, different deep architecture models as well as new learning algorithms have been proposed and applied successfully in many areas, beating the state-of-the-art in certain applications such as in dimensionality reduction, modeling textures, modeling motion, object segmentation, information retrieval, robotics, natural language processing. . . [1]. In chapter 3, we give an overview of these deep architecture models: why we need deep architectures and the challenges of training these models. We also briefly introduce their popular training algorithms.

In fact, deep architectures are emerging as the best machine learning model so far in many practical applications such as reducing the dimensionality of data [16], image classification [22] or speech recognition [17]. . . we believe that improving just one of these models’ architectures or training algorithm, in terms of their performance or computational cost, could make a very strong impact in the machine learning area.

## 1.4 Research Question and Methodology

## 1.4.1 Research question

In this thesis, we intend to study deep architectures (especially deep neural networks) and their learning algorithms, thereby understand the challenges regarding training these models. Based on the knowledge, we could investigate the possibility of improving these models or algorithms using ADATE (Automatic Design of Algorithms Through Evolution) [31]. However, deep learning is known to run extremely slowly (sometimes takes weeks to finish), especially on big dataset. ADATE, on the contrary, needs the program to run fast (usually less than ten seconds), because it has to evaluate at least millions of different program instances to find the best version. Therefore, to use ADATE to improve deep learning, we have to train deep architectures on a very small dataset. The biggest challenge is that we have to make sure that the improved version of that algorithm can still be useful in other dataset. Moreover, deep architectures and their training algorithms are implemented as a very complex program, which definitely could not be completely generated by ADATE. Therefore, we have to choose a small part of that program, which can significantly improve the whole performance if it is improved.

Basically, at the end of this thesis, we need to answer the following research questions:

RQ 1 How can the ADATE system improve the performance of deep learning? Secondary relevant research questions are:

RQ 1.1 Which part of deep learning is possible to be improved by ADATE?

RQ 1.2 What dataset is suitable for using in ADATE to improve deep learning?

RQ 1.3 Could the improved version of deep learning be used in other dataset?

RQ 1.4 How can we implement correctly deep architectures and their training algorithms in Standard ML (SML)?

<!-- page: 23 -->

## 1.4.2 Methodology

In general, machine learning is an experimental science, in which many models or algorithms are based on heuristic equations, which are learned from experiments. This thesis is not an exception. To answer these above research questions, we have to experiment with different possible solutions, as much as possible, to find out the best one. First, we have to get a deep understanding of deep architectures and their training algorithms. Then we choose a part that is most likely to be improved using ADATE. Finally, we choose the most suitable dataset and use ADATE to improve the algorithm on that dataset automatically.

## 1.5 Report Outline

Chapter 2, 3, 4, 5 and 6 provide the necessary background about deep learning:

• In chapter 2, we presented answer the question why we need deep learning, in both theoretical and empirical ways.

• In chapter 3, we gave an overview of deep architectures and challenges of training these models. We also introduced briefly about their popular training algorithms.

• In chapter 4, we summarized different popular gradient-based training algorithms for Neural Networks.

• In chapter 5, we presented the overfitting problem, and introduced different regularization techniques as the possible solutions.

• In chapter 6, we summarized recent well-known researches about activation functions used in deep learning.

Chapter 7 provides a short introduction about ADATE system, as well as an analysis of its power. Besides, based on knowledges provided in previous chapters, this chapter also suggests different deep learning algorithms that can probably be improved by ADATE.

Chapter 8 describes our experiments with ADATE in detail, from choosing the target algorithm, buiding tiny dataset, to testing results and analyzing overfitting problem. This chapter aims at answering all the research questions posed above.

Chapter 9 presents our conclusion about this project, as well as suggestions for future works.

<!-- page: 24 -->

<!-- page: 25 -->

# The Need for Deep Learning and Deep Architectures

Deep learning is a set of algorithms in machine learning that attempt to learn layered models of inputs (deep architectures). The layers in such models correspond to distinct levels of concepts, where higher-level concepts are defined from lower-level ones, and the same lower-level concepts can help to define many higher-level concepts.

Before the invention of pre-training, which makes deep learning more feasible, most of available learning algorithms correspond to shallow architectures. However, as we all know, the mammal brain is organized in a deep architecture [42]. The brain also appears to process information through multiple stages of transformation and representation. This is particularly clear in the primate visual system, with its sequence of processing stages: detection of edges, primitive shapes, and moving up to gradually more complex visual shapes[42].

Theoretically, some functions cannot be efficiently represented (in terms of the number of tunable elements) by architectures that are too shallow. In fact, functions that can be compactly represented by a depth k architecture might require an exponential number of computational elements to be represented by a depth k − 1 architecture. Therefore, poor generalization may be expected when using an inefficiently deep architecture for representing some functions [1].

## 2.1 Deep Architectures on Circuit Problem

In [3], Bengio et al. 2007 have summarized the advantages of deep architectures on circuit problems. According to them, complexity theory of circuits strongly suggests that deep architectures can be much more efficient (sometimes exponentially) than shallow architectures, in terms of the number of computational elements required to represent some functions. For example, the parity function with d inputs (XOR problem) requires $O ( 2 ^ { d } )$ examples and parameters to be represented by a Gaussian SVM (Bengio et al., 2006), $O ( d ^ { 2 } )$ parameters for a one-hidden-layer neural network, $O ( d )$ parameters and units for a multi-layer network with $O ( \log _ { 2 } d )$ layers, and $O ( 1 )$ parameters with a recurrent neural network. More generally, boolean functions (such as the function that computes the multiplication of two numbers from their d-bit representation) expressible by $O ( \log d )$ layers of combinatorial logic with $O ( d )$ elements in each layer may require $O ( 2 ^ { d } )$ elements when expressed with only 2 layers (Utgoff & Stracuzzi, 2002; Bengio & LeCun, 2007).

<!-- page: 26 -->

## 2.2 The Challenges in training Deep Neural Networks

Both theoretical and experimental evidence suggests that training deep architectures is much more difficult than training shallow ones. In [1, 3, 7], the authors showed that gradient-based training process on deep supervised multi-layer neural networks (starting from random initialization) usually gets stuck in “apparent local optima or plateaus”, which ends up with a poorer performance result compared to the shallow ones’. This phenomenon can be explained by the vanishing gradient, local optima, and pathological curvature problems, which known to be much more serious in deep architectures. These problems prevented us from using deep learning for a very long time until the appearance of pre-training methods. Hinton et al. has completely changed the story when introducing Deep Belief Networks and greedy layer-wise unsupervised pre-training methods in 2006 [18]. After that, many successful deep learning methods have been introduced (Bengio et al., 2007; Vincent et al., 2008; Weston et al., 2008; Lee et al., 2008), but all of them use a common idea with Hinton’s one: the DNNs are first pre-trained by an unsupervised pre-training algorithm, and then fine-tuned by other classical supervised learning methods.

In the next chapter, besides deep architectures, many of the most popular models used in pre-training process of deep learning will also be introduced. Because if we could improve one of these pre-training building-block model, we could improve the performance of deep learning in general.

Besides pre-training, some recent researches have shown that learning deep networks can still be done fairly well using other classical learning methods such as Hessian-free Optimization (2<sup>nd</sup>-order method) or even a standard stochastic gradient descent (1<sup>st</sup>-order method)[26, 46]. They argued that while bad local optima do exist in deep-networks, in practice they do not seem to pose a significant threat. Instead, the difficulty is better explained by regions of pathological curvature (e.g. long narrow valley) in the objective function [26]. However, in their experiments, they could only successfully train deep autoencoders using their methods, and did not mention about other types of deep architectures. After conducting some experiments, we concluded that pre-training is still a much better approach than any other methods, in all of deep learning applications. However, there are still some exceptions, where we can train a deep architecture without the need of pre-training, such as using data augmentation [5] or convolutional neural networks (section 5.2.6).

## 2.3 Dominance of Deep Learning

In his presentation about deep learning [29], Andrew Ng. – a leading researcher in the deep learning area, has stated that “This is the first time a single type of model can compete almost all of the previous state-of-the-art results in machine learning”.

One of the most important abilities which brings the power to deep learning is that it can automatically extract useful features in almost any type of input domain (e.g. Images/Video, Audio, Text,. . . ). Figure 2.1 shows the importance of feature learning, where using raw input directly make the tasks on it (e.g. labels, classification, image search,. . . ) become almost impossible. What we need is a better way to present inputs: feature representations. For examples, to detect if the images in figure 2.1 is about motortype, we need to know: is there any wheel? Is there a handlebar?. . . Image presented in term of these features is much easier to process. However, we do not have wheel detector or

<!-- page: 27 -->

handlebar detector. For decades, thousands of experts were trying to hand-design features to capture various statistical properties of the image/audio/text. . . . Some of these features are demonstrated in Figure 2.2.

![](images/page_26_image_3.jpg)

Figure 2.1: Difficulty on object classification task

![](images/page_26_image_5.jpg)

Figure 2.2: Hand-designed features examples

Deep learning, on the other hand, can automatically learn even better features than hand-designed features on many different input domains. This makes deep learning becomes powerful and general-purpose model. Figure 2.3 shows some examples of these different tasks that deep learning outperformed any previous methods. Seeing its potential in real-life applications, many big tech companies have recently hired deep learning leading researchers. In Mar, 2013, Google hired Geoffrey Hinton – the one who enabled deep learning in 2006 by his discovery of unsupervised pre-training – and his team to make AI a Reality (as in the announcement). Facebook also decided to hire prominent NYU professor Yann LeCun – the one who discovered convolutional neural networks – as the new director of their AI lab. Acquisition of Deep Mind – a London-based artificial intelligence – by Google in Jan 2014, which cost more than \$500 million, could show the heat of deep learning.

<!-- page: 28 -->

Figure 2.3: Deep learning applications

| Problems | Best Previous accuracy | Deep learning accuracy |
| --- | --- | --- |
| Hollywood - Activity recognition | 48% | 53% |
| TIMIT - Phoneme Classification | 79.2% | 80.3% |
| CIFAR - Object classification | 80.5% | 82% |
| NORB – Object classification | 94.4% | 95% |
| AVLetters Lip reading | 58.9% | 65.8% |
| Paraphrase detection | 76.1% | 76.4% |

<!-- page: 29 -->

# Deep Architectures and Related Models

In this chapter, we give a brief introduction about different well-known deep architectures. Although we mainly focus on Deep Neural Networks and its related models, it is worth knowing other models such as Boltzmann Machines, Deep Belief Networks, or AutoEncoders, which are used in pre-training process of deep learning. This chapter is split into three general types of models: Deep Neural Networks, Boltzmann Machines-related models, and AutoEncoders models.

## 3.1 Deep Neural Networks

Being a fundamental deep architecture, Deep Neural Network is simply a neural network with many hidden layers. This is a very old idea but could not be used popularly because of difficulties in its training algorithm. After appearance of unsupervised pre-training, deep neural networks have flourished and become one of the most popular machine learning models nowadays. As shown in Figure 3.1, deep neural networks are composed of multi-layer of non-linear operations. Moreover, if learned in a good way, deep neural networks can represent input through multi-level feature representations, where features in higher layer model higher level abstractions in input.

## Layer-wise Unsupervised Pre-trainning

Greedy layer-wise unsupervised pre-training is the most important strategy in deep learning. It allows us to train very deep neural networks very effectively. This strategy contains two main stages:

• Pre-training: We first pre-train one layer of the neural networks at a time (i.e. layerwise) in a greedy way. To do this, we need a building block model. We pre-train each layer of the deep neural network by training a building block model for each layer and stack them one above another. Different building block models for this purpose can be used. The first appeared one is RBM proposed by Hinton in 2006. Since then, many different building block models have been introduced, such as sparse auto-encoders, denoising auto-encoders, or contractive auto-encoders. Figure 3.2 illustrates this pre-training process using an auto-encoder.

<!-- page: 30 -->

![](images/page_29_image_2.jpg)

Figure 3.1: Deep neural networks represent input in multi-level feature representations

![](images/page_29_image_4.jpg)

Figure 3.2: Pretraining process using auto-encoder

• Fine-tuning: After pre-training, we can use any standard backpropagation methods to fine-tune that pretrained deep neural network. The training task is now much easier than training from a random initialized network.

## Traditional Approaches for Deep learning

Besides the pretraining strategy, researchers also tried to find a traditional way to do deep learning. Martens 2010 [26] has developed a 2<sup>nd</sup>-order optimization method based on the “Hessian-free” approach, and apply it to training deep autoencoder successfully. Ilya et al. 2013 [46] proved that a deep autoencoder could also be trained with 1st-order method like stochastic gradient descent, using well-chosen random initialization schemes called and various forms of momentum-based acceleration [46]. They used a variation of momentum called Nesterov’s Accelerated Gradient to improve the convergence rate guarantee. Both Martens and Ilya et al. used “sparse initialization” in their methods. However, these methods are not good at training a general deep neural networks, where the pre-training still a much better strategy.

<!-- page: 31 -->

![](images/page_30_image_2.jpg)

Figure 3.3: (Taken from $\vert \angle \theta \rangle \rangle$ Left: A general Boltzmann machine. The top layer represents a vector of stochastic binary “hidden” features and the bottom layer represents a vector of stochastic binary “visible” variables. Right: A restricted Boltzmann machine with no hidden to hidden and no visible to visible connections.

## 3.2 Boltzmann Machines - Related Models

The most important model of this type is Restricted Boltzmann Machines (RBM), which is used as a building-block model in the unsupervised pre-training process introduced by Hinton in 2006. After that, other researchers have introduced some new types of autoencoders, which can replace the RBM’s role in pre-training process. Actually, the RBM model is very similar to an autoencoder. This similarity will be presented in the next section about autoencoders.

## 3.2.1 Boltzmann Machines

A Boltzmann machine is a type of energy-based models, which maintains an energy function to define a probability distribution of each configuration of the variables of interest. It is a kind of stochastic recurrent neural network invented by Geoffrey Hinton and Terry Sejnowski. As displayed in Figure. 3.3, a Boltzmann machine is a network of symmetrically coupled stochastic binary units. It contains a set of visible units $\pmb { v } \in 0 , 1 ^ { D }$ , and a set of hidden units $\pmb { h } \in { 0 , 1 ^ { P } }$ . The energy of the state v, h is defined as:

$$
E (\boldsymbol {v}, \boldsymbol {h}; \theta) = - \frac {1}{2} \boldsymbol {v} ^ {T} \boldsymbol {L} \boldsymbol {v} - \frac {1}{2} \boldsymbol {h} ^ {T} \boldsymbol {J} \boldsymbol {h} - \boldsymbol {v} ^ {T} \boldsymbol {W} \boldsymbol {h}\tag{3.1}
$$

where $\boldsymbol { \theta } = \{ \boldsymbol { W } , \boldsymbol { L } , \boldsymbol { J } \}$ are the model parameters, which represent visible-to-hidden, visibleto-visible, and hidden-to-hidden symmetric interaction terms. (We have omitted the bias terms for clarity of presentation)

The probability that the model assigns to a visible vector v is:

$$
\begin{array}{c} p (\boldsymbol {v}; \theta) = \frac {1}{Z (\theta)} \sum_ {\boldsymbol {h}} e x p (- E (\boldsymbol {v}, \boldsymbol {h}; \theta)) \\ Z (\theta) = \sum_ {\boldsymbol {v}} \sum_ {\boldsymbol {h}} e x p (- E (\boldsymbol {v}, \boldsymbol {h}; \theta)) \end{array}\tag{3.2}
$$

<!-- page: 32 -->

The parameter updates, originally derived by Hinton and Sejnowski (1983), that are needed to perform gradient ascent in the log-likelihood can be obtained from Eq. 3.2:

$$
\begin{array}{r} \Delta \pmb {W} = \alpha (E _ {P _ {d a t a}} [ \pmb {v} \pmb {h} ^ {\pmb {T}} ] - E _ {P _ {m o d e l}} [ \pmb {v} \pmb {h} ^ {T} ]) \\ \Delta \pmb {L} = \alpha (E _ {P _ {d a t a}} [ \pmb {v} \pmb {v} ^ {\pmb {T}} ] - E _ {P _ {m o d e l}} [ \pmb {v} \pmb {v} ^ {T} ]) \\ \Delta \pmb {J} = \alpha (E _ {P _ {d a t a}} [ \pmb {h} \pmb {h} ^ {\pmb {T}} ] - E _ {P _ {m o d e l}} [ \pmb {h} \pmb {h} ^ {T} ]) \end{array}\tag{3.3}
$$

Exact maximum likelihood learning in this model is intractable because exact computation of both the data-dependent expectations and the model’s expectations takes a time that is exponential in the number of hidden units. However, setting both $J = 0$ and $L = 0$ would introduce the well-known restricted Boltzmann machine (RBM) (Smolensky, 1986) (see Fig. 3.3, right panel), which can be learned efficiently using Contrastive Divergence (CD) (Hinton, 2002).

## 3.2.2 Restricted Boltzmann Machines - RBM

A RBM is a Boltzmann machine, which is restricted by omitting intra-layer connections (e.g. hidden-hidden and visible-visible connections). This restriction allows us to obtain exact samples from the conditional distribution $p ( \pmb { h } | \pmb { v } ; \theta )$ and $p ( \pmb { v } | \pmb { h } ; \theta )$ , thank to independence between hidden-hidden and visible-visible nodes. Therefore, we can sample configuration of h based on state of v and vice versa.

The parameter updates for RBM can be derived as following (including bias terms):

$$
\Delta w _ {i j} = \alpha (\langle v _ {i} h _ {j} \rangle_ {d a t a} - \langle v _ {i} h _ {j} \rangle_ {m o d e l})\tag{3.4}
$$

$$
\Delta b _ {i} = \alpha (\langle v _ {i} \rangle_ {d a t a} - \langle v _ {i} \rangle_ {m o d e l})\tag{3.5}
$$

$$
\Delta b _ {j} = \alpha (\langle h _ {i} \rangle_ {d a t a} - \langle h _ {i} \rangle_ {m o d e l})\tag{3.6}
$$

We can compute $\langle v _ { i } h _ { j } \rangle _ { d a t a }$ by clamping the visible units at the data vector v and then compute the expected value of h easily. To compute $\langle v _ { i } h _ { j } \rangle _ { m o d e l }$ , we can first clamp the visible units at data vector v, then sampling the hidden units, then sampling the visible units, and repeating this procedure infinitely many times. After infinitely many iterations, the model will forget its starting point and we can sample from its equilibrium distribution. However, it has been shown that this expectation can be approximated well in finite time by running the sampling chain for only a few steps. This method is called Contrastive Divergence (CD).

Using these derivatives, we can maximize the log-likelihood function, which leads to decrease the energy of training cases (increase probability) and increase the energy of other unseen cases.

The main reason RBM are interesting is its capability of pre-training a deep network.

## 3.2.3 Deep Belief Nets - DBN

Deep Belief Nets are probabilistic generative models that are composed of multiple layers of stochastic, latent (hidden) variables. The top two layers have undirected, symmetric

<!-- page: 33 -->

![](images/page_32_image_2.jpg)

Figure 3.4: (Taken from $( \not 4 I \not )$ Left: Deep Belief Network (DBN), with the top two layers forming an undirected graph and the remaining layers form a belief net with directed, top-down connections Right: Deep BoltzmannMachine (DBM), with both visible-to-hidden and hidden-to-hidden connections but with no within-layer connections. All the connections in a DBM are undirected.

connections between them and form an associative memory. The lower layers receive top-down, directed connections from the layer above (see Figure. 3.4)

Basically, DBNs extend the RBM architecture to multiple hidden layers, where the weights in layer $h _ { l }$ are trained by keeping all the weights in the lower layers constant and taking as data the activities of the hidden units at layer l − 1. Therefore, DBN is a stacked RBMs, which are trained greedily and in sequence. It can be proved that each time we add another layer of features (i.e. RBM) we improve a variational lower bound on the log probability of the training data.

## Fine-tuning for generation

After learning many layers of features, we can fine-tune the features to improve generation using the “wake-sleep” algorithm. First, we do a stochastic bottom-up pass to adjust the top-down weights to be good at reconstructing the feature activities in the layer below, then doing a few iterations of sampling in the top level RBM to adjust the weights in the top-level RBM. Finally, we do a stochastic top-down pass to adjust the bottom-up weights to be good at reconstructing the feature activities in the layer above.

## Fine-tuning for discrimination

After pre-training the DBNs, we can unfold that DBN into a deep neural network, and use standard back propagation to fine-tune the model for better discrimination.

## Applying DBN on digit recognition

Hinton 2006. has designed a DBN shown in figure 3.5 to learn the joint distribution of digit images and digit labels. The model learns to generate combinations of labels and images. To perform recognition, they start with a neutral state of the label units and do an up-pass from the image followed by a few iterations of the top-level associative memory.

For the MNIST data set (including 70,000 digit images), they achieved 1.25% error rate on test set (using generative fine-tuning) and 1.15% (using back propagation fine-tuning)

<!-- page: 34 -->

![](images/page_33_image_2.jpg)

Figure 3.5: (Taken from $( \not 4 I \not )$ DBN model that was used for MNIST data set

## 3.3 AutoEncoders

A classical autoencoder (i.e. autoassociator) is a special type of feed forward neural network which is trained to encode the input in some representation so that the input can be reconstructed from that representation. In other words, we set the target values to be equal to the inputs. This is an unsupervised learning task because we do not use labels information during the training process. A typical autoencoder is shown in Figure 3.6, which is a feed forward network with two weight-layers (usually constrained to be equal).

## 3.3.1 Basic Autoencoder (AE)

An autoencoder contains two parts:

• Encoder : is a function f that maps an input $x   \in   R ^ { d _ { x } }$ to hidden representation $h ( x ) \in R ^ { d _ { h } }$ . It has the form:

$$
h = f (x) = s _ {f} (W x + b _ {h})\tag{3.7}
$$

where $s _ { f }$ is a activation function, typically a logistic sigmoid function. The encoder is parametrized by a $d _ { h } \times d _ { x }$ weight matrix W, and a bias vector $b _ { h } \in R ^ { d _ { h } }$

• Decoder : The decoder function g maps hidden representation h back to a reconstruction y:

$$
y = g (h) = s _ {g} (W ^ {\prime} h + b _ {y})\tag{3.8}
$$

where $s _ { g }$ is the decoder’s activation function, typically either the identity (yielding linear reconstruction) or a sigmoid. The decoder’s parameters are a bias vector $b _ { y } \in R ^ { d _ { x } }$ , and matrix $W ^ { \prime }$ . The weight matrices of encoder and decoder are usually tied, in which $W ^ { \prime } = W ^ { T }$

<!-- page: 35 -->

![](images/page_34_image_2.jpg)

Figure 3.6: A typical autoencoder

Autoencoder training consists in finding parameters $\theta   =   \{ W , b _ { h } , b _ { y } \}$ that minimize the reconstruction error on a training set of examples $D_{n},$ which corresponds to minimizing the following objective function:

$$
J _ {A E} (\theta) = \sum_ {x \in D _ {n}} L (x, g (f (x)))\tag{3.9}
$$

Where L is the reconstruction error. Typical choices include the squared error $L(x,y)=$ $\| x - y \| ^ { 2 }$ used in cases of linear reconstruction <sup>1</sup>; and the cross-entropy loss when $s _ { g }$ is the sigmoid and inputs are in [0, 1]: $\begin{array} { r } { L ( x , y ) = - \sum _ { i = 1 } ^ { d _ { x } } x _ { i } l o g ( y _ { i } ) + ( 1 - x _ { i } ) l o g ( 1 - y _ { i } ) } \end{array}$ . We can use any kind of back-propagation optimization methods presented in Chapter 4 to train an autoencoder.

As shown above, the autoencoder tries to learn the function $g ( f ( ( x ) ) ) \approx x$ . In other words, it is trying to learn an approximation to the identity function, so as to output ˆx that is similar to x. However, by placing constraints on the network, such as by limiting the number of hidden units, we can discover interesting structure about the data. For example, if the number of hidden units (e.g. 50) is smaller than the number of input units (e.g. 100), the network is forced to learn a compressed representation of the input. Because it must try to reconstruct the input $x \in R ^ { 1 0 0 }$ from its hidden activations representation $h ^ { ( 2 ) }   \in   R ^ { 5 \mathring { 0 } }$ If the input were completely random then this compression task would be

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>This choice gives the hidden representation that very similar to PCA’s</span></small>

<!-- page: 36 -->

very difficult. However, if there is structure in the data, for example, if some of the input features are correlated, then this model will be able to discover some of those correlations.

If the output units are linear (i.e. linear reconstruction) and the mean squared error criterion is used to train the network, then that simple autoencoder often ends up learning a low-dimensional representation very similar to PCA’s.<sup>2</sup>. However, if the hidden units are non-linear, the autoencoder behaves very differenctly from PCA, with the ability to capture multi-modal aspects of the input distribution [1].

An autoencoder with many hidden layers is called deep autoencoder. Deep autoencoder is a special type of deep neural network and useful in dimensionality reduction, which will be introduced shortly in the following section.

Besides, many different types of autoencoder have been introduced recently, which are extremely useful in deep learning and feature extraction. In this section, I will present concisely several most interesting kinds of autoencoder, which can be used in pre-training process (replacing the RBM model) or feature extraction. In the next chapter, I will discuss more about greedy layer-wise pre-training process, which is one of the most important invention in the area of deep learning.

## 3.3.2 Similarity between autoencoder and RBMs

The RBMs and basic classical autoencoders are very similar in their functional form, although their interpretation and the procedures used for training them are quite different [48]. More specifically, the deterministic function that maps from input to hidden representation is the same for both models. One important difference is that determinis tic autoencoders use real-valued mean as their hidden representation whereas stochastic RBMs sample a binary hidden representation from that mean. However, after their initial pretraining, the way layers of RBMs are typically used in practice when stacked in a deep neural network is by propagating these real-valued means, which is more in line with the deterministic autoencoder interpretation. The reconstruction error of an autoencoder can also be seen as an approximation of the log-likelihood gradient in an RBM, in a way that is similar to the approximation made by using Contrastive Divergence updates for RBMs [2].

This similarity can explain why initializing a deep network by stacking autoencoders yields almost as good a classification performance as when stacking RBMs [3]. However, many different types of autoencoder have been introduced recently, which can outperform the RBM model in different benchmarks.

## 3.3.3 Sparse autoencoder

As shown above, without any constraint, the autoencoder will try to learn the identity function. To fix this problem, we can use different type of constraint. One common constraint used in basic classical autoencoder is limiting the number of hidden units. We can also add weight − decay into the objective function, which favors small weights by

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>Principal component analysis (PCA) is a statistical procedure that uses orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. It is a very old procedure ( Karl Pearson, 1901) and usually used in dimensionality reduction - Wiki</span></small>

<!-- page: 37 -->

adding the term $\lambda \textstyle \sum _ { i j } W _ { i j } ^ { 2 }$

$$
J _ {A E + w d} (\theta) = (\sum_ {x \in D _ {n}} L (x, g (f (x)))) + \lambda \sum_ {i j} W _ {i j} ^ {2}\tag{3.10}
$$

However, this weight-decay constraint alone does not help much and must be used together with other constraints.

One very useful constraint is sparsity constraint on the hidden units, which can force autoencoders to discover interesting structure in the data, even if the number of hidden units is large [28]

Informally, we will think of a neuron as being “active” (or as “firing”) if its output value is close to 1, or as being “inactive” if its output value is close to 0. We would like to constrain the neurons to be inactive most of the time.

To impose this constrain, we first calculate the average activation of hidden units over the training set. Let the activation of hidden unit $j$ when the network is given a specific input x is $h _ { j } ( x )$ and a dataset with m training examples, the average activation of hidden unit $j$ can be calculated by:

$$
\hat {\rho} _ {j} = \frac {1}{m} \sum_ {i = 1} ^ {m} h _ {j} (x ^ {(i)})\tag{3.11}
$$

We would like to (approximately) enforce the constraint

$$
\hat {\rho} _ {j} = \rho\tag{3.12}
$$

where $\rho$ is a sparsity parameter, typically a small value close to zero (say $\rho = 0 . 0 5 )$ . In other words, we would like the average activation of each hidden neuron $j$ to be close to 0.05 (say). To satisfy this constraint, the hidden unit’s activations must mostly be near 0.

To achieve this, we will add an extra penalty term to our optimization objective that penalizes $r \hat { h } o _ { j }$ deviating significantly from $\rho .$ Many choices of the penalty term can give reasonable results. A typical one is the Kullback-Leibler (KL) divergence. KL-divergence is a standard function for measuring how different two different distributions are. This penalty function has the property that $KL(\rho \| \hat{\rho}_j) = 0   if   \hat{\rho}_j = \rho,$ , and otherwise, it increases monotonically as $\hat { \rho } _ { j }$ diverges from $\rho .$ This sparsity penalty term can be calculated using following equation:

$$
\sum_ {j = 1} ^ {d _ {h}} K L (\rho \| \hat {\rho} _ {j}) = \sum_ {j = 1} ^ {d _ {h}} \rho l o g \frac {\rho}{\hat {\rho} _ {j}} + (1 - \rho) l o g \frac {1 - \rho}{1 - \hat {\rho} _ {j}}\tag{3.13}
$$

Our overall cost function is now:

$$
J _ {s p a r s e A E} (\theta) = J _ {A E} (\theta) + \beta \sum_ {j = 1} ^ {d _ {h}} K L (\rho \| \hat {\rho} _ {j})\tag{3.14}
$$

where $J _ { A E } ( \theta )$ is as defined in basic classical autoencoder, and $\beta$ controls the weight of the sparsity penalty term. To incorporate the KL-divergence term into backpropagation optimization process, there is a simple-to-implement trick involving only a small code change, which is explained clearly in [28]

The sparse autoencoder is very good at learning useful representations/features from different input domains (such as image, audio,...), and therefore it is usually used as feature

<!-- page: 38 -->

extractor. By first using sparse autoencoder to extract features from raw input, and then training a typical classifier such as a neural network or SVM on these features, we can get a very good result on different tasks such as MNIST and CIFAR-10. Figure 3.7 shows the filters that learned by sparse autoencoder when trained on MNIST dataset.

![](images/page_37_image_3.jpg)

Figure 3.7: Taken from [28] Each square in the figure above shows the (norm bounded) input image x that maximally actives one of 100 hidden units. We see that the different hidden units have learned to detect edges at different positions and orientations in the image.

## 3.3.4 Denoising autoencoder

We have seen that the reconstruction criterion alone is unable to guarantee the extraction of useful features as it can lead to the obvious solution “simply copy the input” or similarly uninteresting ones. To overcome that problem, one strategy is to constrain the representation: the traditional bottleneck (i.e. limiting the number of hidden units) and the more recent sparse representations both follow this strategy.

Another different strategy introduced by Vincent et al. 2010 [48] is that we can change the reconstruction criterion for a both more challenging and more interesting objective: cleaning partially corrupted input, or in short denoising. Vicent et al. 2010 suggested that “a good representation is one that can be obtained robustly from a corrupted input and that will be useful for recovering the corresponding clean input”. They expect that a higher-level representation should be rather stable and robust under corruptions of the input, and performing the denoising task well requires extracting features that capture useful structure in the input distribution.

Based on that strategy, Vincent et al. 2010 introduced a very simple variant of the basic autoencoder, which is called denoising autoencoder (DAE). DAE is trained to reconstruct a clean “repaired” input from a corrupted version of it. Each time a training example x is presented, a different corrupted version ˆx of it is generated according to a stochastic mapping $\hat { x } \sim q _ { D } ( \hat { x } | x )$

Different corruption types can be considered. But the two most commonly used corruptions are additive isotropic Gaussian noise: $\hat { x } = x + \epsilon , \epsilon \sim N ( 0 , \sigma ^ { 2 } I )$ and binary masking noise, where a fraction v of input components (randomly chosen) have their value set to 0. The degree of corruption (σ or v) controls the degree of regularization.

<!-- page: 39 -->

The denoising autoencoder is able to learn useful features in different input domains like sparse autoencoder (Figure 3.8). Besides, we can stack many layers of denoising autoencoders to pre-train a deep neural network, similarly to the way we stack RBMs. This pre-training method even yields better results in many different datasets [48].

![](images/page_38_image_3.jpg)

Figure 3.8: Taken from $\sqrt { 4 8 } J$ Left: regular autoencoder with weight decay. The learned filters cannot capture interesting structure in the image. Right: a denoising autoencoder with additive Gaussian noise $( \sigma = 0 . 5 )$ learns Gabor-like local oriented edge detectors. Very similar to the filters learned by sparse autoencoder.

## 3.3.5 Contractive autoencoder

Salah Rifai et al. 2011 [39] proposed a new variant of autoencoder called Contractive autoencoder (CAE). They introduced a new penalty term, which encourages the hidden representation to be robust to small changes of the input around the training examples. They hypothesized that whereas the proposed penalty term encourages the learned features to be locally invariant without any preference for particular directions, when it is combined with a reconstruction error or likelihood criterion, we obtain invariance in the directions that make sense in the context of the given training data, i.e., the variations that are presented in the data should also be captured in the learned representation, but the other directions may be contracted in the learned representation [39].

If input $x   \in   R ^ { d _ { x } }$ is mapped by encoding function f to hidden representation $h \in$ $R ^ { d _ { h } }$ , then to encourage robustness of the representation $f ( x )$ for a training input x, they proposed the Frobenius norm of the Jacobian $J _ { f } ( x )$ . This penalty is the sum of squares of all partial derivatives of the extracted features with respect to input dimensions:

$$
\| J _ {f} (x) \| _ {F} ^ {2} = \sum_ {i j} (\frac {\partial h _ {j} (x)}{\partial x _ {i}}) ^ {2}\tag{3.15}
$$

By penalizing $\| J _ { f } ( x ) \| _ { F } ^ { 2 }$ , we want to keep all the first derivatives of the hidden units respect to input units to be small, which induces flatness in mapping function. In other words, we encourage the mapping to the feature space to be contractive in the neighborhood of the training data. The flatness will imply an invariance or robustness of the representation for small variations of the input.

The objective function for CAE is now:

$$
J _ {C A E} (\theta) = \sum_ {x \in D _ {n}} (L (x, g (f (x))) + \lambda \| J _ {f} (x) \| _ {F} ^ {2})\tag{3.16}
$$

Computing the new penalty and its gradient is similar to and has about the same cost as computing the reconstruction error and its gradient. Please check the [39] for more details.

<!-- page: 40 -->

The CAE has close relationship with weight decay, sparse AE, and DAE.

• Weight decay: The Frobenius norm of the Jacobian becomes the L2 weight decay in the case of a linear encoder (i.e. when $s _ { f }$ is the identity function). In this case, $J _ { C A E } = J _ { A E + w d } .$

• Sparse autoencoders: sparse autoencoders encourage majority of the hidden representation close to zero. For these features to be close to zero, they must have been computed in the left saturated part of the sigmoid non-linearity, which is almost flat with a tiny first derivative. This yields a corresponding small entry in the Jacobian $J _ { f } ( x )$

• Denoising autoencoders: Robustness to input perturbations was also one of the motivations of the denoising autoencoder. However, the CAE and the DAE differ in the way they encourage the robustness.

The CAE can be used as the building block in the layer-wise pre-training strategy, just like the DAE. It gives slightly better results on some datasets and settings. Figure 3.9 show performance comparison of different autoencoders for unsupervised pre-training a 1000-units one hidden layer network on MNIST and CIFAR10-bw (gray scale version of CIFAR10) datasets.

• RBM-binary: Restricted Boltzmann Machine trained by Contrastive Divergence,

• AE: Basic autoencoder,

• AE+wd: Autoencoder with weight-decay regularization.

• DAE-g: Denoising autoencoder with Gaussian noise,

• DAE-b: Denoising autoencoder with binary masking noise.

<table><tr><td></td><td>Model</td><td>Test error</td><td>Average  $\|J_f(x)\|_F$ </td><td>SAT</td></tr><tr><td rowspan="6">MNIST</td><td>CAE</td><td>1.14</td><td> $0.73\ 10^{-4}$ </td><td>86.36%</td></tr><tr><td>DAE-g</td><td>1.18</td><td> $0.86\ 10^{-4}$ </td><td>17.77%</td></tr><tr><td>RBM-binary</td><td>1.30</td><td> $2.50\ 10^{-4}$ </td><td>78.59%</td></tr><tr><td>DAE-b</td><td>1.57</td><td> $7.87\ 10^{-4}$ </td><td>68.19%</td></tr><tr><td>AE+wd</td><td>1.68</td><td> $5.00\ 10^{-4}$ </td><td>12.97%</td></tr><tr><td>AE</td><td>1.78</td><td> $17.5\ 10^{-4}$ </td><td>49.90%</td></tr><tr><td rowspan="5">CIFAR-bw</td><td>CAE</td><td>47.86</td><td> $2.40\ 10^{-5}$ </td><td>85,65%</td></tr><tr><td>DAE-b</td><td>49.03</td><td> $4.85\ 10^{-5}$ </td><td>80,66%</td></tr><tr><td>DAE-g</td><td>54.81</td><td> $4.94\ 10^{-5}$ </td><td>19,90%</td></tr><tr><td>AE+wd</td><td>55.03</td><td> $34.9\ 10^{-5}$ </td><td>23,04%</td></tr><tr><td>AE</td><td>55.47</td><td> $44.9\ 10^{-5}$ </td><td>22,57%</td></tr></table>

Figure 3.9: Taken from [39] Results are sorted in ascending order of classification error on the test set. Best performer and models whose difference with the best performer was not statistically significant are in bold. Notice how the average Jacobian norm (before fine-tuning) appears correlated with the final test error. SAT is the average fraction of saturated units per example.

<!-- page: 41 -->

## 3.3.6 Deep AutoEncoders

A deep autoencoder is just an autoencoder with many hidden layers (Figure 3.10). This model is extremely useful in reducing the dimensionality of data, where we want to transform the high-dimensional data into a low-dimensional code. By reducing dimensionality, other tasks on high-dimensional data will become much easier such as classification, visualization, communication, or storage. The model has been introduced long ago but could only become popular by Hinton’s discovery of pre-training strategy. This model can be considered as a nonlinear generation of Principal component analysis (PCA), which is a simple and widely used method for dimensionality reduction task. In [16], Hinton shown how a deep autoencoder could be trained using pre-training strategy Figure 3.10. Of course, we can replace RBM model in his method by another type of building block models.

![](images/page_40_image_4.jpg)

Figure 3.10: (Taken from [16]) Pretraining consists of learning a stack of RBMs, each having only one layer of feature detectors. The learned feature activations of one RBM are used as the “data” for training the next RBM in the stack. After the pretraining, the RBMs are “unrolled” to create a deep autoencoder, which is then fine-tuned using back propagation of error derivatives

Figure 3.11 shows how a deep autoencoder produces much better compressed codes compared to PCA. This experiment conducted by Hinton et al. [16], in which a very deep autoencoder $7 8 4 - 1 0 0 0 - 5 0 0 - 2 5 0 - 2$ was used on MNIST dataset. We can see that a two-dimensional autoencoder produced a better visualization of the data than did the first two principal components.

<!-- page: 42 -->

![](images/page_41_image_2.jpg)

Figure 3.11: (Taken from [16]) (A) The two dimensional codes for 500 digits of each class produced by taking the first two principal components of all 60,000 training images.(B) The two dimensional codes found by a 784 − 1000 − 500 − 250 − 2 autoencoder

<!-- page: 43 -->

# Gradient-Based Training Algorithms for Neural Networks

In neural networks, optimization techniques play an important role, especially in supervised learning. They are used to explore the hypothesis space and find the best configuration, which minimizes an objective function (e.g. mean-square error, cross-entropy error. . . ). First-order optimization methods such as Steepest Gradient Descent (SGD) used to be the most popular method due to their simple implementations and computational efficiency, compared to the second-order methods (e.g. Newton’s methods). However, first-order methods are easy to be trapped in local minima and exhibit slow convergence, due to the problems described below. To help first-order methods overcome those problems, momentum-related techniques and well-designed initialization methods have been proposed recently [46]. These techniques are successfully experimented on training deep autoencoders and Recurrent Neural Networks (RNN), which was believed to be impossible (even with 2nd-order methods). These improvements could potentially change the “wrong” belief about the ability of first-order methods.

On the other hand, some of the second-other methods are computationally infeasible but show much better convergence characteristics because they take into account the curvature of the error space. The reason of its in-feasibility is the computation of the inverse of Hessian matrix $( O ( n ^ { 3 } ) )$ , which could be tackled by computing the inverse matrix directly (as in quasi-Newton’s method); approximation of it (as in Gauss-Newton’s method); or using an incomplete optimization (as in Hessian-Free method).

This chapter attempts to give a complete overview about all current well-known optimization techniques applied in Neural Network, their believed shortcomings as well as advantages.

## 4.1 First-order Methods

All first-order methods bases on the first-order Taylor series expansion to approximate the objective function F (i.e. cost function) at current state of weight configuration w:

$$
\begin{array}{c} F (w + \Delta w) \approx F (w) + \nabla F (w) \Delta w \\ \nabla F (w): \text {gradient vector of} F (w) \end{array}\tag{4.1}
$$

<!-- page: 44 -->

Therefore, if we go from the weight configuration w to the next configuration at the direction of $\Delta w = - \alpha \nabla F ( w )$ (α is learning rate), we will get:

$$
\begin{array}{r} F (w _ {n e x t}) = F (w - \alpha \nabla F (w)) \approx F (w) - \alpha \nabla F (w) ^ {2} \\ \leq F (w) \mathrm{if} \alpha \mathrm{smallenough} \end{array}
$$

The cost function is decreased as we update the weight. However, the reasoning presented here is approximate and it is true only for small enough learning rates.

## 4.1.1 Steepest Gradient Descent

Steepest Gradient Descent (SGD) is a standard first-order method, which directly uses the proof above. This method assumes that the cost function F(w) decreases fastest if we go in the direction of negative gradient of $F ( w )$

The SGD converges slowly to the optimal solution, and the learning-rate parameter α has a profound influence on its convergence behaviors. If the learning rate is small, the method is more stable but converges slowly. If the learning rate is large, it could follows a zigzagging (oscillatory path) to the optimal solution, or even diverge if it is too large. However, the size of learning rates depends on the shape of the error plane at current point, so we could not easily determine the appropriate learning rates at different point of learning process. In practice, we usually set the learning rates larger at the beginning and decrease it down when reaching the optimal solution. The second-order methods tackle this problem by using the curvature information of the error plane to somehow “adjust” the learning rates.

## 4.1.2 Stochastic and Mini-Batches Gradient Descent

In steepest gradient descent (i.e. batch gradient descent) method, the gradient vector of the cost function F is calculated by summing up the gradients of each training case. In other words, we have to go through the whole training set to make a single update on the weights matrix. Updating this way is inefficient if the training set is large, which is usually happens in practice. The stochastic (i.e. online) gradient descent approximates the gradient vector ∇F by calculate the gradient of each training case and use it to update the weights matrix right away. This method leads to a zigzagging searching path, because we are not following the steepest gradient of the error plane. The stochastic gradient descent tends to work better than the steepest gradient descent on large datasets where each iteration of gradient descent is very expensive. Besides, if each training case is used only one time, any new training cases are supplied every day, this method is capable of forgetting the old training case.

There is a compromise between the batch and stochastic method, which is often called”mini-batches”, where the true gradient is approximated by a sum over a small number of training cases.

## 4.1.3 Momentum and Nesterov’s Accelerated Gradient

The SGD method usually get trouble with plateaus or long narrow valleys (i.e. pathological curvature) in the objective function. It is because the gradient is too small (e.g. in plateau) or the curvature is too high (e.g. long narrow valley). The momentum method is used to accelerate the optimization along directions of low but persistent reduction (in

<!-- page: 45 -->

plateau), similarly to the way the second-order methods accelerate the optimization along low-curvature directions (but second-order methods also decelerate the optimization along high curvature directions, which is not done by momentum methods) [45]

The momentum method maintains a velocity vector $v _ { t }$ which is updated as follows:

$$
\begin{array}{l} {v _ {t + 1} = \mu v _ {t} - \alpha \nabla F (w _ {t})} \\ {w _ {t + 1} = w _ {t} + v _ {t + 1}} \end{array}
$$

The momentum decay coefficient $\mu   \in   [ 0 ; 1 )$ controls the rate at which old gradients are discarded. Its physical interpretation is the “friction” of the surface of the objective function, and its magnitude has an indirect effect on the magnitude of the velocity [45].

A variant of momentum known as Nesterov’s accelerated gradient (Nesterov, 1983) (NAG) has been analyzed with certain schedules of the learning rate and of the momentum decay coefficient $\mu ,$ and was shown by Nesterov (1983) to exhibit the better convergence rate $O ( 1 / T ^ { 2 } )$ versus the $O ( 1 / T )$ of SGD [46]. NAG formulas:

$$
\begin{array}{l} {v _ {t + 1} = \mu v _ {t} - \alpha \nabla F (w _ {t} + \mu v _ {t})} \\ {w _ {t + 1} = w _ {t} + v _ {t + 1}} \end{array}
$$

While momentum method compute the gradient update from the current position $w _ { t } ,$ NAG first performs a partial update to $w _ { t } .$ , computing $w _ { t } + \mu v _ { t }$ , but missing the yet unknown correction. This difference seems to allow NAG to change v in a quicker and more responsive way, letting it behave more stably than momentum in many situations, especially for higher values of $\mu$ [46].

Choosing an appropriate schedule for the momentum $\mu$ and learning rate α is difficult and usually tuned in a heuristic way. As showed in [46], Ilya et. al. 2013 have trained deep autoencoders by using these following formulas:

$$
\mu = \min (1 - 2 ^ {- 1 - \log_ {2} (\lfloor t / 2 5 0 \rfloor + 1)}, \mu_ {m a x})\tag{4.2}
$$

where $\mu _ { m a x }$ was chosen from {0.999, 0.995, 0.99, 0.9, 0}. For each point of $\mu _ { m a x }$ , the learning rate α is chosen from {0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001}. Besides, they found it beneficial to reduce $\mu$ to 0.9 during the final 1000 parameter updates of the optimization without reducing the learning rate. (see [46] for more information about momentum schedule and its effect on convergence rate and quality of final result)

## 4.1.4 Sparse Initialization

Convex objective functions $F ( w )$ are insensitive to the initial parameter setting, since the optimization will always recover the optimal solution, merely taking longer time for worse initializations. But, given that most objective functions $F ( w )$ that we want to optimize are non-convex, the initialization has a profound impact on the optimization and on the quality of the solution. Ilya et. al. 2013 shown that appropriate initializations play an even greater role than previously believed for both deep and recurrent neural networks [46]. Unfortunately, it is difficult to design good random initializations for new models, so it is important to experiment with many different initializations [45].

An initialization scheme that was successfully used to train deep and recurrent neural networks in [46] is called sparse initialization. In that initialization scheme, each random unit is connected to 15 randomly chosen units in the previous layer, whose weights are

<!-- page: 46 -->

drawn from a unit Gaussian, and the biases are set to zero. The intuitive justification is that the total amount of input to each unit will not depend on the size of the previous layer and hence they will not as easily saturate. Meanwhile, because the inputs to each unit are not all randomly weighted blends of the outputs of many 100s or 1000s of units in the previous layer, they will tend to be qualitatively more “diverse” in their response to inputs.

## 4.1.5 Resilient BackPropagation

Resilient BackProbagation (Rprop) is a first-order local adaptive learning scheme, performing supervised batch learning in multi-layer neural networks [38]. The basic principle of Rprop is to eliminate the harmful influence of the size of the partial derivative on the weight step: small in plateaus and large in ravines. It uses only the sign of the derivative to indicate the direction of the weight update. The size of the weight change is exclusively determined by a weight-specific, so-called “update-value” $\Delta _ { i j } ;$

$$
w _ {i j} ^ {(t)} = \left\{ \begin{array}{l l} - \Delta_ {i j} ^ {(t)} & \text {if} \frac {\delta E ^ {(t)}}{\delta w _ {i j}} > 0 \\ + \Delta_ {i j} ^ {(t)} & \text {if} \frac {\delta E ^ {(t)}}{\delta w _ {i j}} <   0 \\ 0 & \text {else} \end{array} \right.\tag{4.3}
$$

The second step of Rprop learning is to determine the new update-values $\Delta _ { i j } ^ { ( t ) }$ . This is based on a sign-dependent adaptation process:

$$
\Delta_ {i j} ^ {(t)} = \left\{ \begin{array}{l l} - \eta^ {+} * \Delta_ {i j} ^ {(t - 1)} & \text {if} \frac {\delta E ^ {(t - 1)}}{\delta w _ {i j}} * \frac {\delta E ^ {(t)}}{\delta w _ {i j}} > 0 \\ + \eta^ {-} * \Delta_ {i j} ^ {(t)} & \text {if} \frac {\delta E ^ {(t - 1)}}{\delta w _ {i j}} * \frac {\delta E ^ {(t)}}{\delta w _ {i j}} <   0 \\ \Delta_ {i j} ^ {(t - 1)} & \text {else} \end{array} \right.\tag{4.4}
$$

Where $0 < \eta ^ { - } < 1 < \eta ^ { + }$ . The $\eta ^ { + }$ is empirically set to 1.2 and $\eta ^ { - }$ to 0.5 [38] The adaptiverule works as follows: every time the partial derivative of the corresponding weight <sup>w</sup>ij changes its sign, which indicates that the last update was too big and the algorithm has jumped over a local minimum, the update-value $\Delta _ { i j } ^ { ( t ) }$ is decreased by the factor $\eta ^ { - }$ . If the derivative retains its sign. The update value is slightly increased in order to accelerate convergence in shallow regions.

Generally, the Rprop method converges faster than standard gradient descent method. Besides, we do not have to set any meta-parameters (such as learning rates) for Rprop to obtain optimal convergence times.

Another interesting property of Rprop is that the size of the weight-step is only dependent on the sequence of signs, not on the magnitude of the derivative. Therefore, learning is spread equally all over the entire networks: weights near the input layer have the equal chance to grow and learn as weights near the output layer. This property can help to overcome the vanishing gradient problem when training deep neural networks.

## 4.2 Second-order Methods

All second-order methods base on the idea of minimizing the quadratic approximation of the cost function (using the second-order Taylor series expansion). However, each of these methods below are different on how they calculate (or approximate) the inversion of Hessian matrix.

<!-- page: 47 -->

## 4.2.1 Newton’s Methods

This is the standard second-order methods. Specifically, using a second-order Taylor series expansion of the cost function $F ( )$ around the point w, we will have:

$$
F (w + \Delta w) \approx F (w) + \nabla F (w) \Delta w + \frac {1}{2} \Delta w ^ {T} H \Delta w\tag{4.5}
$$

With H is the Hessian (i.e. curvature) matrix of $F ( w )$

We attain the extreme of F when its derivative with respect to $\Delta w$ is equal to 0. Therefore, we have to solve the following equation:

$$
\begin{array}{c} \nabla F (w) + H \Delta w = 0 \\ \Leftrightarrow \Delta w = - H ^ {- 1} \nabla F (w) \end{array}
$$

However, finding the inverse of the Hessian in high-dimensional space can be an expensive operation $O ( n ^ { 3 } )$ . In such cases, instead of directly inverting the Hessian, we can calculate it as a solution of the system of linear equations: $H \Delta w = - \nabla F ( w )$ . This can be solved by using iterate methods like conjugate gradient (described below, used in Hessian-Free method). However, conjugate gradient requires Hessian matrix be a positive definite matrix, which is not guaranteed during training process.

Besides, we can also approximate the inversion of Hessian matrix directly from changes in the gradient, which is used in quasi-Newton’s methods (e.g. DFP, BFGS, L-BFGS, ...).

## 4.2.2 Gauss-Newton’s method

The Gauss-Newton algorithm is a method used (and can only be used) to solve non-linear least squares problems and can be seen as a modification of Newton’s method. Instead of computing the Hessian matrix, it uses the Jacobian matrix to approximate it. Therefore, this method has the advantage that second derivatives, which can be challenging to compute, are not required.

In least squares problem, given m training examples which their error cost are calculated by m functions $r _ { 1 . . m }$ we have to find the minimum of the sum of squares:

$$
F (w) = \sum_ {i = 1} ^ {m} r _ {i} ^ {2} (w)\tag{4.6}
$$

Differentiating the above equation with respect to $w _ { j }$ (an element of $\mathrm { w ) }$ , we have the elements of gradient vector of $F ( )$

$$
\nabla F (w) _ {j} = 2 \sum_ {i = 1} ^ {m} r _ {i} \frac {\partial r _ {i}}{\partial w _ {j}}\tag{4.7}
$$

Differentiating the above gradient element respect to $w _ { k }$ , we could get the elements of the Hessian matrix:

$$
H _ {j k} = 2 \sum_ {i = 1} ^ {m} (\frac {\partial r _ {i}}{\partial w _ {j}} \frac {\partial r _ {i}}{\partial w _ {k}} + r _ {i} \frac {\partial^ {2} r _ {i}}{\partial w _ {j} \partial w _ {k}})\tag{4.8}
$$

The Gauss-Newton method is obtained by ignoring the second-order derivative terms (the second term in above expression). So the Hessian is approximated by:

$$
H _ {j k} = 2 \sum_ {i = 1} ^ {m} (\frac {\partial r _ {i}}{\partial w _ {j}} \frac {\partial r _ {i}}{\partial w _ {k}}) = 2 \sum_ {i = 1} ^ {m} J _ {i j} J _ {i k}\tag{4.9}
$$

<!-- page: 48 -->

where $\begin{array} { r } { J _ { i j } = \frac { \partial r _ { i } } { \partial w _ { j } } } \end{array}$ are entries of the Jacobian $J _ { r }$ matrix. Therfore, Gauss-Newton’s methods approximate Hessian by:

$$
H \approx 2 J _ {r} ^ {T} J _ {r}\tag{4.10}
$$

This approximation of H is usually called as Gauss-Newton matrix $\mathbf { G } ,$ and this is used in Hessian-Free method instead of H matrix because it is guaranteed to be positive semi-definite, which avoids the problem of negative curvature.

## 4.2.3 Quasi-Newton’s methods

In quasi-Newton methods, the Hessian matrix does not need to be computed. The Hessian is updated by analyzing successive gradient vectors instead. The most common quasi-Newton algorithms are currently the SR1 formula (for symmetric rank one), the BHHH method, the widespread BFGS method (suggested independently by Broyden, Fletcher, Goldfarb, and Shanno, in 1970), and its low-memory extension, L-BFGS.

If we call B is an approximation of Hessian, apply the first-order Taylor series expansion on the gradient of cost function $F ( )$ , we have the following secant equation:

$$
\nabla F (w + \Delta w) = \Delta F (w) + B \Delta w\tag{4.11}
$$

The various quasi-Newton methods differ in their choice of the solution to the secant equation. Most methods (but with exceptions, such as Broyden’s method) seek a symmetric solution $B ^ { T } = B$

## 4.2.4 Conjugate gradient method

In mathematics, the conjugate gradient (CG) method is an iterative method to solve the systems of linear equations. In Hessian-Free optimization method, they use conjugate gradient method to solve the linear equation: $H \Delta w = - \nabla F ( w )$ Instead of solving this directly, CG method tries to minimize this objective function, which becomes smaller when we come closer to the solution.

$$
E (\Delta w) = \frac {1}{2} \Delta w ^ {T} H \Delta w - \Delta w ^ {T} b\tag{4.12}
$$

Therefore, we have to find $\Delta w$ that minimize the function $E ( )$ . Briefly, CG finds the solution by using a sequence of steps, each of which finds the minimum along one direction. Besides, it makes sure that new direction is “conjugate” to the previous directions so you do not mess up the minimization you already did. In fact, the “conjugate” means that as you go in the new direction, you do not change the gradients in the previous directions.

## 4.2.5 Hessian-Free optimization method

HF differs from other Newton’s methods only because it is performing an incomplete optimization (via un-converged Conjugate gradient) of approximation of $F ( )$ [26].

The first main thing about Hessian-Free optimization is that it uses conjugate gradient method to find the $\Delta w$ (direction to go) from the linear equation $H \Delta w = - \nabla F ( w )$ instead of computing the inversion of Hessian matrix (directly or indirectly). Besides, in this method, we do not wait for the CG to totally converge.

<!-- page: 49 -->

The second thing is that we use Gauss-Newton matrix G (instead of Hessian) because it is guaranteed to be positive semi-definite, and experimentally showed to be consistently better than H.

The third vital important thing in HF method is its damping technique (also called structural regularization). HF method could find a direction with extremely low curvature and will elect to move very far along it, and possibly well outside of the region where Taylor series expansion is a sensible approximation. Therefore, we add the damping parameter λ to control how “conservative” the approximation is, by adding the constant $\lambda \| d \| ^ { 2 }$ to the curvature estimate for each direction d. we can also use the “Levenberg-Marquardt” style heuristic for adjusting λ over time.

The final important thing is about the sparse initialization scheme described above.

## 4.3 Line Search vs. Trust Region Strategy

In iterative optimization techniques (including all type of first-order and second-order methods), there is two main strategies: line search and trust region. In line search approach, one first finds the descent direction (of the objective function $f )$ and then computes an appropriate step size. In trust region approach, one first determines a step size (the size of the trust region) and then finds the step direction. Generally, the line search approach is usually used to adapt the learning rate in first-order methods, while the trust region approach is used as a damping/regularization technique in second-order methods.

## 4.3.1 Line Search

In line search approach, the step direction is first computed by other methods, such as gradient descent, Newton’s method, or Quasi-Newton method. . . . The step size then can be determined either exactly or inexactly using many different rules. In [43], Shi 2004 has summarized and analyzed seven different line search rules. In this section, we provide the basic ideas of the four most popular rules, which are: minimization rule, Limited minimization rule, approximate minimization rule, and Armijo rule.

Assume that F is our objective function, $w _ { k }$ is weights configuration at step $k ^ { t h } ,   \Delta w _ { k }$ is chosen direction at step $k ^ { t h } , \; \alpha _ { k }$ is step size (or learning rate if using with first-order methods). The $\alpha _ { k }$ can be computed exactly or inexactly using these following rules:

1. Minimization rule: In this rule, we try to find the step size $\alpha _ { k }$ that can minimize the objective function $F$ in chosen direction $\Delta w _ { k }$ . This rule is implicitly used by Conjugate gradient method.

$$
\alpha_ {k} = \operatorname{argmin} _ {\alpha > 0} F (w _ {k} + \alpha \Delta w _ {k})\tag{4.13}
$$

2. Limited minimization rule: This rule is similar to the first rule, except that we limit the maximum step size by $\begin{array} { r } { s _ { k }   =   - \frac { \nabla F ( \Delta w _ { k } ) ^ { T } \Delta w _ { k } } { | | \Delta w _ { k } | | ^ { 2 } } } \end{array}$ . Note that $\nabla F ( \Delta w _ { k } ) ^ { T } \Delta w _ { k }$ is the expected decrement in F if the step is $\Delta w _ { k }$ , approximated by first order Taylor series.

$$
\alpha_ {k} = \operatorname{argmin} _ {\alpha \in [ 0, s _ {k} ]} F (w _ {k} + \alpha \Delta w _ {k})\tag{4.14}
$$

3. Approximate minimization rule: In this rule, we try to go as far as possible, as long as the objective function is still getting decreased.In the minimization rule, we go

<!-- page: 50 -->

directly to the global minima along the chosen direction of the objective function, while in this rule, we $\mathrm { g o }$ to the nearest local minima on that direction.

$$
\alpha_ {k} = \min (\alpha | \nabla F (w _ {k} + \alpha \Delta w _ {k}) ^ {T} \Delta w _ {k} = 0, \alpha > 0)\tag{4.15}
$$

4. Armijo rule: This rule ensures that the step length $\alpha _ { k }$ decreases $F$ “sufficiently”, by using this inequality:

$$
F (w _ {k}) - F (w _ {k} + \alpha_ {k} \Delta w _ {k}) \geq - c _ {1} \alpha_ {k} \nabla F (w _ {k}) ^ {T} \Delta w _ {k}\tag{4.16}
$$

This inequality ensures that the real decrement in F is bigger than a proportion $c _ { 1 }$ of the expected decrement. $c _ { 1 }$ is usually chosen to be quite small, say $1 0 ^ { - 4 }$ However, because the above inequality is always satisfied when α is small enough. Therefore, to prevent choosing too small step size, we usually add the following curvature condition to ensures that the slope has been reduced sufficiently.

$$
\nabla F (w _ {k} + \alpha_ {k} \Delta w _ {k}) ^ {T} \Delta w _ {k} \geq c _ {2} \nabla F (w _ {k}) ^ {T} \Delta w _ {k}\tag{4.17}
$$

In practice, besides using line search to control the learning rate in first-order methods, the learning rate is also usually set by $\begin{array} { r } { \alpha _ { k } = \frac { a } { b + k } } \end{array}$ , with $a , b$ are predefined constants.

## 4.3.2 Trust Region

In almost every iterative optimization techniques, the objective function is approximated using a certain model function (e.g. quadratic in second-order methods). However, that approximation is only good (trusted) in a limited region around the sample point - the trust region. The trust region approaches restricts the step size by first compute the trust region, and then find the best direction within that region. The trust region is expanded when the approximation is fit the objective function well, and contracted otherwise. This is also known as the restricted step method. The model fit is usually evaluated by comparing the ratio of expected improvement from the model approximation with the actual improvement observed in the objective function.

This method is usually used with the second-order methods such as Newton’s, Gauss-Newton or Hessian-Free optimization. Generally, in second-order methods, we find the descent direction $\Delta w$ by solving the following equation:

$$
H \Delta w = \nabla F (w)\tag{4.18}
$$

With H is the Hessian matrix or its approximation. To restrict the step size, the trust region method instead solves the following equation:

$$
(H + \lambda I) \Delta w = \nabla F (w)\tag{4.19}
$$

With I is the identity matrix, and λ is the damping parameter that controls the trustregion size. Geometrically, that term adds a paraboloid centered at $\Delta w \; = \; 0$ to the quadratic form, resulting in a smaller step. If the λ is large enough, the Hessian matrix will be ignored, and the step will be taken approximately in the direction of the gradient.

In Levenberg-Marquardt algorithm, Marquardt replace the identity matrix I with the diagonal matrix consisting of the diagonal elements of H. This approach can scale each

<!-- page: 51 -->

component of the gradient according to the curvature, so that there is larger movement along the directions where the gradient is smaller:

$$
(H + \lambda \mathrm{diag} (I)) \Delta w = \nabla F (w)\tag{4.20}
$$

The damping factor λ is adjusted by looking at the ratio $\begin{array} { r } { \rho = \frac { \Delta F _ { a c t u a l } } { \Delta f _ { p r e d } } } \end{array}$ . In [26], Martens 2010 has successfully used this damping method (using identity metrix) with Hessian-Free optimization to train deep autoencoders. He used Levenberg-Marquardt style heuristic for adjusting λ directly: if $\rho < { \textstyle { \frac { 1 } { 4 } } } : \lambda \leftarrow { \textstyle { \frac { 3 } { 2 } } } \lambda$ elseif $\rho > \textstyle { \frac { 3 } { 4 } } : \lambda \leftarrow { \stackrel { \cdot } { \frac { 2 } { 3 } } } \lambda$

## 4.4 Initialization Analysis

In [9], X. Glorot and Y. Bengio 2010 have provided a profound analysis about the influence of the non-linear activations functions, cost function types, and initialization methods, on using standard gradient descent for training deep neural networks. They showed that the logistic sigmoid activation is unsuited for deep networks with random initialization because of its mean value, which can drive especially the top hidden layer into saturation. Besides, they found that the logistic regression or conditional log-likelihood cost function coupled with softmax outputs worked much better (for classification problems) than the quadratic cost. Regarding the initialization, they explained why the standard random initialization could lead to vanishing gradient problem in training deep neural networks.

In the standard random initialization, the biases is initialized to be 0, and the $W _ { i j }$ at each layer is sampled from the uniform distribution: $\scriptstyle U \left[ - { \frac { 1 } { \sqrt { n } } } ,   { \frac { 1 } { \sqrt { n } } } \right]$ , where n is the size of the previous layer and $U [ - a , a ]$ is the uniform distribution in the interval $( - a , a )$ They proved that standard initialization would lead to variance of the weights with the following property:

$$
n _ {i} V a r [ W ^ {i} ] = \frac {1}{3}\tag{4.21}
$$

Where $n _ { i }$ is the layer size (assuming that all layers have the same size), and $W ^ { i }$ is weights of layer $i ^ { t h }$ . This will cause the variance of the back-propagated gradient to be dependent on the layer (and decreasing). We prefer the following conditions, which can keep information flowing:

$$
\begin{array}{l} \forall i, n _ {i} V a r [ W ^ {i} ] = 1 \\ \forall i, n _ {i + 1} V a r [ W ^ {i} ] = 1 \end{array}
$$

To approximately satisfy the objectives of maintaining activation variances and backpropagated gradients variance as one moves up or down the network, X. Glorot and Y. Bengio 2010 have proposed the following normalized initialization:

$$
W \sim U [ - \frac {\sqrt {6}}{\sqrt {n _ {j} + n _ {j + 1}}}, \frac {\sqrt {6}}{\sqrt {n _ {j} + n _ {j + 1}}} ]\tag{4.22}
$$

## 4.5 Cascade correlation algorithm

Cascade-Correlation is a supervised learning algorithm for neural networks. Instead of just adjusting the weights in a network of fixed topology, Cascade-Correlation begins with a

<!-- page: 52 -->

minimal network, then automatically trains and adds new hidden units one by one, creating a multi-layer structure [8]. Once a new hidden unit has been added to the network, its input-side weights are frozen. This unit then becomes a permanent feature-detector in the network, available for producing outputs or for creating other, more complex feature detectors. This approach has several advantages: it learns very quickly, the network determines its own size and topology, it retains the structure it has built even if the training set changes, and it requires no back-propagation of error signals through the connections of the network ([8]).

<!-- page: 53 -->

## Chapter 5

# Overfitting and Regularization

## 5.1 Introduction

In general, by training neural networks using a set of examples with input and output pattern (i.e. supervised learning), we are trying to construct a mapping that defines the output pattern in terms of the input patterns. However, the information content of the training examples is ordinarily not sufficient itself to reconstruct that mapping, which leads to the possibility of overfitting [14].

Hadamard (1902) has defined the term “well-posed” to indicate that whether a problem could be solved on a computer using a stable (e.i reproducible and unique result) algorithm or not. If a problem is not “well-posed”, it is said to be ill-posed. The problem of reconstructing the mapping f between input and output is said to be well-posed if Hadamard’s three conditions are satisfied:

• Existence: the mapping function“f” exists.

• Uniqueness: the mapping function is unique.

• Continuity: slight change in the input only make a limited change in the output.

However, in the context of supervised learning, Hadamard’s conditions are violated for the following reasons [14]:

• The mapping function may not exist (a certain output may not exist for any input).

• We typically do not have as much information from training examples as we need to reconstruct an unique mapping.

• The unavoidable presence of noise in training examples could lead to the violation on the continuity criterion.

There is no way to overcome these difficulties unless some prior information about the input-output mapping is available. In fact, when we are constructing a neural network for a specific task (e.g. classification, regression . . . ), we have already made some assumptions (i.e. prior information, inductive bias) about what the solution should be, such as: number of hidden units, type of units, number of layers. . . Regularization is also a set of methods to embed prior information into the learning process. The most common form of prior information involves the assumption that the input-output mapping function is smooth (i.e. similar inputs produce similar outputs) and simple (Occam’s Razor).

<!-- page: 54 -->

![](images/page_53_image_2.jpg)

Figure 5.1: Underfitting and Overfitting in classification task, taken from [30]

![](images/page_53_image_4.jpg)

Figure 5.2: Underfitting and Overfitting in regression task, taken from [30]

## 5.1.1 Overfitting - What Is It?

The overfitting problem happens when a model is trained to fit the training data so well that it loses the generality properties (ability to predict the output for an unseen input). The training data contains information about the regularities in the mapping from input to output. However, it also contains sampling error, which comes from the way the particular training cases are chosen (not representative), or the technique we use to collect these training cases. Therefore, when we fit the model to the training data, it cannot tell which regularities are real and which are caused by sampling error. So if the model is very flexible (i.e. powerful), it can model the sampling error really well, and fail to generalize to unseen examples.

In Figure 5.1 and 5.2 [30], you can see how the models classify or fit the training data very well in overfitting cases, but they are probably not the good solutions. In general, we prefer the solution that is “smooth”, simple, and able to explain the training data well enough, rather than a complex well-fitted solution. This inductive bias can be explained using the Occam’s Razor, which will be described later.

On the other hand, the underfitting problem happens when the model cannot fit the training data. It happens because the model has low representational power compared to complexity of the problem, or because the learning algorithm gets stuck (e.g. in local minima or ravine). This is a serious problem when training deep or recurrent neural networks which are believed to be hard to train, using standard learning methods.

<!-- page: 55 -->

![](images/page_54_chart_2.jpg)

Figure 5.3: Error curves in cross validation methods

## 5.1.2 How to Detect Overfitting?

A common method to detect overfitting is to use validation set [27, 30]. Firstly, we split the whole data set into three parts: training data, validation data, and test data (typically 60%, 20%, and 20% respectively). Then, we use the training data to train the model, use the validation data to tune meta-parameters (i.e. learning rate, momentum. . . ), and use test data to test the real performance of model over unseen examples. To detect overfitting, we could slot the two curves: training error and validation error (error calculated on validation set) as shown in Figure 5.4. Clearly, the overfitting problem happens when the validation error start to increase while the training error is still getting improved.

## 5.1.3 How to Solve Overfitting?

There are many ways to prevent overfitting.

1. Get more data. This is the best way to overcome overfitting, because more data probably provides more information about solution and weaken the influence of sampling error. However, collecting data is typically costly (in terms of time and labor). Besides, training with more data would require more computational power, which could be impossible in some cases.

2. Combine different models. We can learn many models with different forms, or train the model on different subsets of the training data (i.e. bagging), and average pre-dictions from these models.

<!-- page: 56 -->

3. Limit the model capacity (i.e. representational power) to enough to fit the true regularities and not enough to fit the spurious regularities (sampling errors).

We can control the capacity of a neural networks in many ways:

1. Early stopping: Start with small weights and stop learning before it overfits.

2. Architecture: Limit the number of hidden layers or the number of units per layer. Besides, weights in the network can be shared as in convolutional neural network

3. Weight-decay: Penalize large weights using penalties of constraints on their squared values (L2 penalty) or absolute values (L1 penalty).

4. Noise: Add noise to the input, weights, or the node activities.

5. DropOut and DropConnect: Randomly selected subsets of activations or weights are set to zero within each layer.

## 5.1.4 From the Occam’s Razor Point of View

Occam’s (or Ockham’s) razor is a principle attributed to the 14th century logician and Franciscan friar William of Ockham [20]. Ockham was the village in the English county of Surrey where he was born. The principle states that “Entities should not be multiplied unnecessarily”. Many scientists have adopted or reinvented Occam’s Razor, as in Leibniz’s”identity of observables” and Isaac Newton stated the rule: “We are to admit no more causes of natural things than such as are both true and sufficient to explain their appearances”. Stephen Hawking writes in A Brief History of Time: “We could still imagine that there is a set of laws that determines events completely for some supernatural being, who could observe the present state of the universe without disturbing it. However, such models of the universe are not of much interest to us mortals. It seems better to employ the principle known as Occam’s razor and cut out all the features of the theory that cannot be observed”.

The most useful statement of the principle for scientists is “when you have two competing theories that make exactly the same predictions, the simpler one is the better”, or a stronger form which is relevant to machine learning fields: “If you have two theories that both explain the observed facts, then you should use the simplest until more evidence comes along”.

In machine learning, Occam’s razor can be viewed as an inductive bias during the learning process. This theory explains why we prefer a simple relatively fitted model than a complex well-fitted model over the training data.

## 5.1.5 From the Bayesian point of view

From the Bayesian point of view, many regularization techniques correspond to imposing certain prior distributions on model parameters. For example, the L2 regularization assumes that prior distributions of weights in neural network are zero-mean Gaussian.

<!-- page: 57 -->

![](images/page_56_image_2.jpg)

Figure 5.4: Posterior distribution

The Bayesian framework assumes that we always have a prior distribution for everything, but this prior may be very vague. When we observe some data, we combine our prior distribution with a likelihood term to get a posterior distribution. The likelihood term takes into account how probable the observed data to be predicted by the model. During the learning process, the likelihood term will fights against the prior and with enough data, the likelihood terms always wins. However, if we do not have enough data, prior distribution will keep the solution reasonable.

An easy example is about tossing coin when we try to predict the probability p of producing head of a coin. Suppose we observe 100 tosses and there are 53 heads, so the maximum likelihood answer (the value of p that makes the observation of 53 heads and 47 tails) will be $p = 0 . 5 3$ . However, what if we only tossed the coin one and we got 1 head? Clearly, $p = 1$ is not a good answer because we do not have enough information. A better solution for this problem is to imply a prior distribution for the coin, such as uniform or 0.5-mean Gaussian distribution. We then combine the probability of observing a head with that prior distribution to get the posterior distribution. Therefore, choosing the right prior information could help the maximize posterior method overcome the overfitting in maximize likelihood method when lacking of training data.

## 5.2 Regularization Overview

Regularization, in mathematics and statistics and particularly in the fields of machine learning, refers to a process of introducing prior information in order to solve an illposed problem or to prevent overfitting. In machine learning, regularization techniques are usually used to constrain the weights of network to be small (L2 method), sparse (L1 method), or shared over different parts (Convolutional neural network). Besides, we can also add noise to weight or node activities. New published methods such as Dropout or Dropconnect could also do the job particularly successfully in many cases.

## 5.2.1 Least-Squared Method as Regularization

When using the Least-Squared cost function to maximize the likelihood between model’s predictions and the target values, we are actually doing a simple regularization with the prior information is that the target solution is generated by adding the Gaussian noise to the output of the neural network ([27, 15]).

Suppose that we have $y _ { c } = f ( i n p u t _ { c } , W )$ is the output of the net and $t _ { c }$ is the target value. Therefore, the probability density of the target value is given by the network’s

<!-- page: 58 -->

output plus Gaussian noise:

$$
\begin{array}{c} p (t _ {c} | y _ {c}) = \frac {1}{\sqrt {2 \pi \sigma^ {2}}} e ^ {- \frac {(t _ {c} - y _ {c}) ^ {2}}{2 \sigma^ {2}}} \\ p (t | y) = \prod_ {c \text {examples}} \frac {1}{\sqrt {2 \pi \sigma^ {2}}} e ^ {- \frac {(t _ {c} - y _ {c}) ^ {2}}{2 \sigma^ {2}}} \\ \ln p (t | y) = \sum_ {c} \ln \frac {1}{\sqrt {2 \pi \sigma^ {2}}} - \frac {(t _ {c} - y _ {c}) ^ {2}}{2 \sigma^ {2}} \end{array}
$$

Therefore, minimizing the squared error is the same as maximizing the log probability under a Gaussian noise.

$$
\begin{array}{c} W _ {M L} = \operatorname{argmax} _ {W} \sum_ {c} \ln {\frac {1}{\sqrt {2 \pi \sigma^ {2}}} - \frac {(t _ {c} - y _ {c}) ^ {2}}{2 \sigma^ {2}}} \\ {= \operatorname{argmin} _ {W} \sum_ {c} \frac {(t _ {c} - y _ {c}) ^ {2}}{2 \sigma^ {2}}} \end{array}
$$

## 5.2.2 L2 regularization

L2 regularization is a standard weight penalty method, which is widely used in leastsquared cost function. It adds an extra term to the cost function that penalizes the squared weights. However, there is also a similar regularization term which can be used with cross-entropy cost function (in case the output unit is logistic or softmax node).

$$
\begin{array}{l} C = E + \frac {\lambda}{2} \sum_ {i} w _ {i} ^ {2} \\ \quad C: \text {Final cost function} \\ \quad E: \text {Squared error - Likelihood term} \\ \quad \frac {\lambda}{2} \sum_ {i} w _ {i} ^ {2}: \text {L2 regularization term} \end{array}
$$

The L2 regularization attempt to keep the weights small unless they have big error derivatives. This method prevents the network from using weights that it does not need which can improve generalization and make a smoother model because it helps to stop the network from fitting the sampling error. For example, if the network has two very similar inputs, it prefers to put half the weight on each rather than all the weight on one.

From the Bayesian point of view, this regularization method is equivalent to assuming a zero-mean Gaussian prior for the network’s weights [15].

$$
\begin{array}{l} \ln p (W | D) = \ln p (D | W) + \ln p (W) - \ln p (D) \\ \implies W _ {M L} = \operatorname * {a r g m i n} _ {W} \frac {1}{2 \sigma_ {D} ^ {2}} \sum_ {c} (t _ {c} - y _ {c}) ^ {2} + \frac {1}{2 \sigma_ {W} ^ {2}} \sum_ {i} w _ {i} ^ {2} \\ \quad \text {W: Network weights} \\ \quad D: \text {Training data} \\ \quad \ln p (D): \text {Independent from W} \end{array}
$$

<!-- page: 59 -->

The first term in above equation come from the assumption that the model makes a Gaussian prediction. And the second term assumes a zero-mean Gaussian prior for the weights.

## 5.2.3 L1 regularization

Sometimes, it works better to penalize the absolute values of the weights instead of the squared. This is called L1 regularization.

$$
C = E + \frac {\lambda}{2} \sum_ {i} | w _ {i} |\tag{5.1}
$$

This method is widely used in sparse modeling, a popular and effective model using in image processing. It pushes many weights in network to become exactly equal to zero, which yields sparse models - easier to interpret. Besides, the L1 also outperform the L2 penalty when irrelevant features are presented in training data, because it can learn to completely ignore them.

However, this L1 regularization term makes the cost function in equation above non-differentiable. Thus, we cannot use the standard optimization method like gradient descent to find the global minimum in the same way that is done in L2 penalty.

Besides, L2 and L1 penalty, sometimes, we can use different weight penalty that allows large weights but pushes small weights to become zero.

## 5.2.4 Weight constraints

Instead of penalize the squared weights separately; we can put a constraint on the maximum squared length of the incoming weight vector of each unit. If an update violates this constraint, we scale down the vector of incoming weights to allowed length. This method has several advantages over weight penalties: It is easier to set a sensible threshold and can prevent hidden units getting stuck near zero as well as weights exploding [15]. This is more effective than a fixed penalty at pushing irrelevant weights towards zero. Besides, using a constraint rather than a penalty prevents weights from growing very large no mat ter how large the proposed weight-update is. This makes it possible to start with a very large learning rate which decays during learning, thus allowing a far more thorough search of the weight-space than methods that start with small weights and use a small learning rate [19].

This method has been used together with dropout in [19] and gave a very good results on many different applications (see Dropout section).

## 5.2.5 Adding noise

In fact, adding Gaussian noise to the inputs is equivalent to using L2 regularization. We have the variance of the noise is amplified by the squared weight before going into the next layer as showed in Figure 5.5. This makes an additive contribution to the squared error, so minimizing the squared error tends to minimize the squared weights when the inputs are noisy.

However, adding Gaussian noise to the weights of a multilayer non-linear neural network is not exactly equivalent to using an L2 penalty and could be better especially in

<!-- page: 60 -->

![](images/page_59_image_2.jpg)

Figure 5.5: Adding Gaussian noise to inputs, taken from [15]

recurrent networks. Alex Graves showed that recurrent networks significantly better if noise is added to the weights [12].

Another way is to add noise to the node activities [15]. Suppose that we have a multilayer neural network composed of logistic units and trained by back propagation. We can make the logistic units binary and stochastic (sampled from its activities) on the forward pass, but do the backward pass as in original back propagation method. This way produce the worse result on training set, and require considerably more time to train, but it does significantly better on test set.

## 5.2.6 Convolutional neural network

When applying fully-connected multilayer neural network on learning complex high-dimensional non-linear mapping such as image recognition or speech recognition, we traditionally have to use hand-designed feature extractor to gathers relevant information from the input and eliminates irrelevant variabilities. Feeding “raw” inputs directly into the network and let it learn feature extractor automatically is more interesting but causes many problems [24]. Firstly, because typical images or spoken words contain at least several hundred variables. Therefore, a first fully-connected layer with, say a few 100 units, would already contain several 10,000 weights, which leads to overfitting if the training data is scarce. Secondly, unstructured nets have no built-in invariance with respect to translations, or local distortions of the inputs (e.g. size, slant, or position variations). In principle, a fully-connected network of sufficient size could learn to produce outputs that are invariant with respect to such variations. However, learning such a task would probably result in multiple units with identical weight patterns positioned at various locations in the input. Besides, learning these weight configurations requires a very large number of training instances to cover the space of possible variations [24]. Thirdly, a fully-connected architectures entirely ignore the topology of the input (i.e. the input variables can be presented in any fixed order without affecting the outcome of the training).

The CNNs overcome these above problems by designing a network architecture that contains a certain amount of a prior knowledge about the problem [6]. CNNs combine three architectural ideas to ensure some degree of shift and distortion invariance: local receptive fields, shared weights (or weight replication) and spatial or temporal subsampling [24], which give these following advantages:

<!-- page: 61 -->

1. Local receptive fields: neurons can extract elementary visual features such as oriented edges, end-points, corners. This comes from the Hubel and Wiesel’s discovery of locally-sensitive, orientation-selective neurons in the cat’s visual system.

2. Shared weights: the elementary feature detectors that are useful on one part of the image are likely to be useful across the entire image. This knowledge can be applied by forcing a set of units, whose receptive fields are located at different places on the image, to have identical weight vectors. The outputs of such a set of neurons constitute a feature map. In order words, units in a feature map are constrained to perform the same operation on different parts of the image. A convolutional layer is usually composed of several feature maps (with different weight vectors), so that multiple features can be extracted at each location.

3. Subsampling: once a feature has been detected, its exact location become less important, as long as its approximate position relative to other features is preserved. Therefore, each convolutional layer is followed by an additional layer that performs a local averaging, and a subsampling, reducing the resolution of the feature map, and reducing the sensitivity of the output to shifts and distortions. Successive layers of convolutions and subsampling are typically alternated, resulting in a “bi-pyramid”: at each layer, the number of feature maps is increased as the spatial resolution is decreased.

Besides, the weight sharing technique has the interesting side effect of reducing the number of free parameters, thereby reducing the “capacity” of the machine and improving its generalization ability.

A very successful CNN architecture used in MNIST problem has been introduced by Y. LeCun et al. 1990, which gives one of the best performances so far (0.4% error rate) if combined with elastic deformations, and early-stopping (1.0% error rate if using CNN alone) (Figure 5.6). However, CNN architecture is usually designed in a heuristic way. Recently, many new methods have been introduced to effectively train deep neural networks, such as using generative pre-training, Hessian-free optimization, or even a standard gradient descent with well-designed initialization and momentum. Therefore, we now can train a fully-connected deep neural networks with millions of parameters to extract useful features from the training images automatically. A DNN has been used for MNIST problem with raw input and provided 1.25% error rates [16].

Recently, E. Hinton, Alex and Ilya Sutskever 2012 [23] have provided an amazing result on using Deep CNN on classifying image. They trained a large, deep CNN to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes. On the test data, they achieved top-1 and top-5 error rates of 37.5% and 17.0% which is considerably better than the previous state-of-the-art. They also used “dropout” method (described below) to reduce overfitting and that was proved to be very effective.

## 5.2.7 Dropout

Hinton et al. 2012 have proposed a very effective regularization method called Dropout. It can reduce overfitting by preventing complex co-adaptions (a feature detector is only

<!-- page: 62 -->

![](images/page_61_image_2.jpg)

Figure 5.6: CNN architecture used in MNIST problem [24]

helpful in the context of several other specific feature detectors) on the training data [19]. On each presentation of each training case, each hidden unit is randomly omitted from the network with a certain probability, say 0.5, so a hidden unit cannot rely on other hidden units being present. At test time, they use the “mean network” that contains all of the hidden units but with their outgoing weights halved to compensate for the fact that twice as many of them are active.

Another way to view the dropout procedure is as a very efficient way of performing model averaging with neural networks. We could think of it as training different network for each presentation of each training case but all of these networks share the same weights for the hidden units that are present.

Using together with weight constraint, Hinton et al. 2012 have tested this method on many different dataset. On MNIST dataset, the best published result for a standard feed forward neural network (without adding prior knowledge, preprocessing or generative pre-training) is 1.6%, which could be reduced to 1.3% using 50% dropout and weight constraints, and to 1.1% by also dropping out a random 20% of the pixels. On TIMIT, a widely used benchmark for recognition of clean speech with a small vocabulary, using 50% dropout with deep, pre-trained, feedforward neural networks reduces the recognition error rate from 22.7% to 19.7%. That is a record for methods that do not use any information about speaker identity. Lately, E. Hinton, Alex and Ilya Sutskever 2012 [23] have used a deep convolutional neural networks with dropout method to produce the best result on Imagenet dataset (classify high-resolution images into 1000 different classes).

## 5.2.8 Dropconnect

Lately, a generation of Dropout called Dropconnect has been introduced by Li Wan et al., 2013 [50]. This method sets a randomly selected subset of weights within the network to zero. Each unit thus receives input from a random subset of units in previous layer, instead of dropping out random units as in dropout method. In MNIST dataset, this method gives a slightly better result in some cases. However, it converges more slowly

<!-- page: 63 -->

than Dropout. The same thing happens to other dataset such as CIFAR-10, SVHN and NORB. In general, the Dropconnect method can slightly outperform the Dropout method, but it needs more time to converge.

<!-- page: 64 -->

<!-- page: 65 -->

## Chapter 6

## Activation Functions

What makes the deep neural networks become very powerful and universal model is the activation function. A deep neural network contain multiple layers of linear transformation can be represented by a simple one-layer neural network. The nonlinear activation function is what gives neural networks their nonlinear capabilities [25]. The activation function is generally chosen to be monotonic. There are many different types of activation functions that have been proposed. Sigmoid is one of the most common form, which is a monotonically increasing function that asymptotes at some finite value as ±∞ is approached. In this chapter, we will present the motivation behind the sigmoid function, some of its variants, and introduce some new activation forms coming from recent researches.

## 6.1 Logistic Sigmoid function

The logistic sigmoid function is given by $\begin{array} { r } { f ( x )   =   \frac { 1 } { 1 + \exp ( - x ) } } \end{array}$ (Figure 6.1). One important motivation for this form of function is the output of the logistic sigmoid function can be interpreted as posterior probabilities [27]. For example, we consider building a discriminant function for a two-class problem using logistic regression, which has form:

$$
y = f (W ^ {T} x + b)\tag{6.1}
$$

we want to predict the two-class label y from the input x, given that the class-conditional densities are given by Gaussian distributions with equal covariance matrices $\Sigma _ { 1 } = \Sigma _ { 2 } = \Sigma$ so that:

$$
P (x | C _ {k}) = \frac {1}{(2 \pi) ^ {d / 2} | \Sigma | ^ {1 / 2}} \exp \left\{- \frac {1}{2} (x - \mu_ {k}) ^ {T} \Sigma^ {- 1} (x - \mu_ {k}) \right\}\tag{6.2}
$$

Using Bayes’ theorem, the posterior probability of membership of class $C _ { 1 }$ is given by:

$$
P (C _ {1} | x) = \frac {p (x | C _ {1}) P (C _ {1})}{p (x | C _ {1}) P (C _ {1}) + p (x | C _ {2}) P (C _ {2})}\tag{6.3}
$$

Let

$$
a = \ln \frac {p (x | C _ {1}) P (C _ {1})}{p (x | C _ {2}) P (C _ {2})}\tag{6.4}
$$

we will see that the posterior probability can be expressed as the logistic sigmoid function of a:

$$
P (C _ {1} | x) = \frac {1}{1 + \exp (- a)}\tag{6.5}
$$

<!-- page: 66 -->

![](images/page_65_image_2.jpg)

Figure 6.1: The sigmoid, tanh, and scaled tanh functions

If now we substitute the expressions for the class-conditional densities from 6.2 into 6.4, we obtain:

$$
a = W ^ {T} x + b\tag{6.6}
$$

where

$$
\begin{array}{l} W = \Sigma^ {- 1} (\mu_ {1} - \mu_ {2}) \\ b = - \frac {1}{2} \mu_ {1} ^ {T} \Sigma^ {- 1} \mu_ {1} + \frac {1}{2} \mu_ {2} ^ {T} \Sigma^ {- 1} \mu_ {2} + \ln \frac {P (C _ {1})}{P (C _ {2})} \end{array}
$$

Therefore, we can see that the logistic sigmoid activation function allows the outputs of the discriminant function in 6.1 to be interpreted as posterior probabilities.

## 6.2 Hyperbolic tangent and its scaled version

The Hyperbolic tangent or tanh function is a rescaling of the logistic sigmoid, such that its outputs range from −1 to 1 instead of 0 to 1 as in logistic sigmoid. Let s(x) is the logistic sigmoid function, we can represent the tanh(x) function as a linear transformed version of s(x):

$$
\tanh (x) = \frac {e ^ {x} - e ^ {- x}}{e ^ {x} + e ^ {- x}} = 2 s (2 x) - 1\tag{6.7}
$$

In neural network, the tanh function is more popular because of its symmetry about the origin (i.e. zero-mean). In other words, the tanh are more likely to produce outputs (which are inputs to the next layer) that are on average close to zero. Moreover, the logistic function has been shown to slow down the learning process because of its none-zero mean that induces important singular values in the Hessian [25].

<!-- page: 67 -->

![](images/page_66_image_2.jpg)

Figure 6.2: Taken from ${ \sqrt { 4 } } / ,$ tanh versus the sof tsign, which converges polynomially instead of exponentially towards its asymptotes

Glorot and Bengio 2010 [9] did a deep investigation on the effect of using activation functions on deep neural network. They showed that when using sigmoid activation on 5-layers network, the last hidden layer quickly saturates at 0 (slowing down all learning), but then slowly desaturates around epoch 100. The hyperbolic tangent networks do not suffer from that kind of saturation behavior. However, with random weight initialization, the saturation phenomenon occur sequentially starting with first layer and propagating up in the network.

Lecun et al. 1998 also recommended a scaled version of tanh: $\textstyle f ( x ) = 1 . 7 1 5 9 \operatorname { t a n h } ( { \frac { 2 } { 3 } } x )$ The constants in this function are chosen so that, when used with normalized inputs (e.g. zero mean, uncorrelated, and unit covariance), the variance of the outputs will also be close to 1. In particular, this function has the properties that $(a) $f ( \pm 1 ) = \pm 1 ,$ (b)$ the second derivative is a maximum at $x = 1$ , and (c) the effective gain is close to 1.

## 6.3 Softsign function

Bergstra et al. 2009 [4] has proposed a new activation function called softsign: $f(x) =$ $\frac { x } { 1 + | x | }$ The softsign is similar to the hyperbolic tangent (its range is −1 to 1) but its tails are quadratic polynomials rather than exponentials, i.e., it approaches its asymptotes much slower [9]. In Glorot and Bengio 2010 experiment, they showed that saturation does not occur one layer of the other in deep softsign networks like for the hyperbolic tangent networks. It is faster at the beginning and then slow, and all layers move together towards larger weights [9]. Without pre-training, the softsign networks perform better than the tanh or logistic sigmoid networks on different datasets such as MNIST, Shapeset, CIFAR10, ...

## 6.4 Rectifier and Softplus function

Many differences exist between neural network models used by machine learning researchers and those used by computational neuroscientists. Glorot et al. 2011 [10] wanted

<!-- page: 68 -->

to bridge (in part) a machine learning / neuroscience gap in terms of activation function and sparsity. They have successfully applied the rectifier function suggested in neuroscience into machine learning neural network models, which could perform better than tanh or sigmoid networks in some particular settings.

There are two main neuroscience observations that inspired their works:

• Studies on brain energy expense suggest that neurons encode information in a sparse and distributed way (Attwell and Laughlin, 2001), estimating the percentage of neurons active at the same time to be between 1 and 4%. However, without additional regularization, such as an $L _ { 1 }$ penalty, ordinary feed forward neural nets do not have this property.

• A common biological model of neuron, the leaky integrate-and-fire (or LIF) (Dayan and Abott, 2001) is very different from the logistic sigmoid or tanh function used in machine learning.

Moreover, they were also inspired particularly by the sparse representations learned by sparse auto-encoder. However, they argued that when using the sparsity penalty to induce the sparse representations, the neurons end up taking small but non-zero activation. They want to build truly sparse representations, which gives rise to real zeros of activations.

Combining all of these ideas, they ended up using the rectifier neurons, which introduced in the neuroscience literature by Bush and Senowski 1995: $f(x) = \max(0, x)$ . This activation function shows the following advantages:

• The rectifier activation function allows a network to obtain sparse representations easily. For example, after uniform initialization of the weights, around 50% of hidden units continuous output values are real zeros, and this fraction can be easily increase with sparsity-inducing regularization.

• The only non-linearlity in the network comes from the path selection associated with individual neurons being active or not (illustrated in Figure 6.3). For a given input, only a subset of neurons is active. Once this subset of neurons is selected, the output is a linear function of the input. We can see the model as an exponential number of linear models that share parameters. Because of this linearity, gradients flow well on active paths of neurons (there is no gradient vanishing effect due to activation non-linearities of sigmoid or tanh units).

However, there is one potential problem, that the hard saturation at 0 may hurt optimization by blocking gradient back-propagation. The authors have evaluated this by investigating the soft-plus activation: $f ( x ) = \log ( 1   +   e ^ { x } )$ , as smooth version of the rectifier. However, experimental results suggested that hard zeros could actually help supervised training. Another problem could arise due to the unbounded behavior of the activations. Therefore, the authors used the $L _ { 1 }$ weight decay on the activation values, which also promotes additional sparsity.

Experimental results in [10] showed that rectifier performs better than other traditional activation functions on supervised training (1.43% on MNIST compared to 1.57% of tanh network). However, with unsupervised pre-training, the difference is not significant. Glorot et al. 2011 [10] also presented a short summary of sparse representation advantages, which is worth mentioning here.

<!-- page: 69 -->

![](images/page_68_image_2.jpg)

Figure 6.3: Taken from ${ \mathit { [ I 0 ] } } ,$ Sparse propagation of activations and gradients in network of rectifier units. The input selects a subset of active neurons and computation is linear in this subset

![](images/page_68_chart_4.jpg)

Figure 6.4: Taken from ${ \mathit { [ I 0 ] } } ,$ Rectifier and softplus activation functions. The second one is a smooth version of the first

<!-- page: 70 -->

• Information disentangling: A dense representation is highly entangled because almost any change in the input modifies most of the entries in the representation vector. Instead, if a representation is both sparse and robust to small input changes, the set of non-zero features is almost always roughly conserved by small changes of the input.

• Efficient variable-size representation: Different inputs may contain different amounts of information and would be more conveniently represented using a variable-size data-structure, which is common in computer representations of information. Varying the number of active neurons allows a model to control the effective dimensionality of the representation for a given input and the required precision.

• Linear separability: Sparse representations are more likely to be linearly separable simply because the information is represented in a high-dimensional space.

## 6.5 Maxout Function

Goodfellow et al. [11] proposed maxout activation function, which yields state of the art performance on MNIST, CIFAR10 and CIFAR100 datasets when applied on convolutional neural networks with dropout (0.45%, 11.58%, and 38.57% respectively). This is a very simple model, which designed to both facilitates optimization by dropout and improves the accuracy of dropout’s fast approximate model averaging technique.

As introduced in chapter 5 about regularization techniques, Dropout (Hinton et al., 2012) provides an inexpensive and simple means of both training a large ensemble of models that share parameters and approximately averaging together these models’ predictions. While dropout is known to work well in practice, it has not previously been demonstrated to actually perform model averaging for deep architectures [11]. Therefore, the authors tried to design a model that enhances dropout’s abilities as a model averaging technique.

The maxout network is simply a feed-forward neural network or deep convolutional neural network, which uses a new type of activation function: the maxout unit. Given an input $x \in R ^ { d }$ (x may be a training input or a hidden layer’s state), a maxout hidden layer implements the function:

$$
h _ {i} (x) = \max _ {j \in [ 1, k ]} z _ {i j}\tag{6.8}
$$

where $z _ { i j } = x ^ { T } W _ { \dots i j } + b _ { i j }$ and $W \in R ^ { d \times m \times k }$

Note that in maxout network, each layer contains k different weight matrix instead of only one weight matrix in feed forward network. This idea fits well in convolutional network where we have multiple feature maps on each layer. In a convolutional network, a maxout feature map can be constructed by taking the maximum across k affine feature maps (i.e., pool across channels, in addition spatial locations). When training with dropout, we perform the element wise multiplication with the dropout mask immediately prior to the multiplication by the weights in all cases - we do not drop inputs to the max operator. A single maxout unit can be interpreted as making a piecewise linear approximation to an arbitrary convex function. Therefore, maxout networks learn not just the relationship between hidden units, but also the activation function of each hidden unit. The maxout abandons many of the mainstays of traditional activation function design. The representation it produces is not sparse at all. Moreover, maxout is locally linear almost everywhere,

<!-- page: 71 -->

![](images/page_70_image_2.jpg)

Figure 6.5: Taken from ${ \mathit { [ I I ] } } ,$ Graphical depiction of how the maxout activation function can implement the rectified linear, absolute value rectifier, and approximate the quadratic activation function. This diagram is 2D and only shows how maxout behaves with a 1D input, but in multiple dimensions a maxout unit can approximate arbitrary convex functions.

while many popular activation functions have significant curvature. However, it is very robust, easy to train with dropout, and achieves excellent performance.

<!-- page: 72 -->

<!-- page: 73 -->

## Chapter 7

# Introduction to ADATE

In this chapter, we only introduced the ADATE system very briefly, which could help you understand the main ideas behind it. For more details about how its internal algorithms work, please refer to [33, 34]. Besides, writing specification file for ADATE is also an art, which needs both knowledge and experience. The paper [32] could be a very useful source for anyone wanting to write a good specification. A complete User Manual is also available, which provides many practical information about how to use ADATE [47].

## 7.1 A Short Introduction to ADATE

ADATE [35] has been developed by Prof. Roland Olsson, to automatically generate purely functional programs. For example, it has been employed to improve state-of-the-art SAT solvers [36].

To evolve a solution to a problem, the system needs a specification file that defines data types and auxiliary functions, a number of training and validation input examples, and an evaluation function that is used to grade and select potential solutions during evolution. Additionally, the specification file may contain an initial program from which evolution will start. Of course, it is possible to start the evolution from any given program, for example to search for improvements for the best known program for a given problem.

The programs are constructed using a limited number of so-called atomic program transformation. The most important ones are as follows.

• R (Replacement) - A part of an existing program is replaced by a newly synthesized expression. Due to the extremely high number of expressions that can be synthesized, R transformations are combinatorially expensive.

• REQ (Replacement preserving Equality) - An R transformation that does not make the program worse according to the given evaluation function. REQ transformations are quite useful due to their ability to explore plateaus in the search landscape.

• ABSTR (Abstraction) - Like REQ transformations, these neutral transformations exist to aid the system in exploring plateaus. In contrast to the general REQ transformation, ABSTR transformations have the very specific task of introducing new functions in the program by factoring out a piece of code and replacing it with a function call. This gives the system the important ability of inventing needed help functions on the fly, something which has proven to be an extremely useful feature.

<!-- page: 74 -->

Atomic program transformations are composed to compound program transformations using a number of different heuristics to avoid common cases of infinite recursion, unnecessary transformations etc. For example, after an ABSTR transformation, the newly introduced function should be used in some way by a following R or a REQ transformation. More details on the atomic program transformations and the heuristics employed to combine them can be found in [35].

Each time a new program is created by a compound transformation, it is considered for insertion into the so-called kingdom [49]. As in all evolutionary systems, individuals with good evaluation values are preferred, but in ADATE, the syntactic complexities of the individuals also play an important role. According to what is commonly known as Occam’s Razor, simple theories should usually be preferred over more complex ones, as the simpler theories tend to be more general. This principle is utilized by ADATE to reduce the amount of overfitting, in that small programs are preferred, and if a large program is to be allowed in the kingdom, it has to be better than all programs smaller than it [35]. In other words, a new program will only be allowed to be inserted into the kingdom if all other programs in the kingdom are either larger or worse than it. Each time a program is added to the kingdom, all programs in the kingdom both larger and worse than than the new one are removed.

Having described the most important components of the ADATE system, we conclude this section by giving a brief overview of the overall evolution occuring in a run of the system.

1. Initiate the kingdom with the single program given as the start program in the specification file (either an empty program or some program that is to be optimized). In addition to the actual programs, the system also maintains an integer value $C _ { P }$ for each program P, called the cost limit of the program. For new programs this value is set to the initial value 1000.

2. Select the program P with the lowest $C _ { P }$ value from the kingdom.

3. Apply $C _ { P }$ compound program transformations to the selected program, yielding $C _ { P }$ new programs.

4. Try to insert each of the created programs into the kingdom in accordance with the size-evaluation ordering described above.

5. Double the value of $C _ { P } ,$ and repeat from step 2.

The above loop is repeated until the user terminates the system. The ADATE system has no built-in termination criteria and it is up to the user to monitor the evolving programs and halt the system whenever he considers the evolved results good enough.

## 7.2 A Short Analysis of the Power of ADATE System

ADATE is a general-purpose automatic programming system, which can be used in different ways. Besides being well known for its ability of meta-learning or “learn how to learn” ADATE can also be applied as a traditional machine learning model on classification or regression problems. Moreover, it has showed its superior fitting power in many cases, compared to other traditional approaches.

<!-- page: 75 -->

In this section, I will do a short analysis of the power of ADATE system in different use cases, based mainly on the structure of its synthesized programs. In other words, I will basically do a black box analysis where I ignore the ADATE’s internal algorithm and only focus on what kind of programs it would probably synthesize in different use cases. For more information about how it does the “magic”, please refer to [33, 34].

## 7.2.1 ADATE on Classification Problems

Classification is the problem of predicting the value of a categorical variable based on other explanatory variables. An algorithm that implements classification is called a classifier. In this section, I will further split this problem in two different types: when explanatory variables are continuous or categorical. Because the ADATE tends to synthesize programs in different structure when applied to different type.

## Continuous Explanatory Variables

An example for this type is an edge detection problem, which is done by Kristin Larsen as her master thesis. In this problem, the classifier has to predict if the middle pixel is on an edge of a 5x5 pixels image. The explanatory variables are intensity of 24 pixels surrounding the middle one (T1 to T24). The intensity value range is an integer number in [0..255]. After trained for a prolonged time (more than two weeks), the best ADATE’s synthesized program (tested on separate validation set) is showed below <sup>2</sup>:

```perl
fun f (
    T1, T2, T3, T4, T5,
    T6, T7, T8, T9,T10,
    T11, T12, T13, T14, T15,
    T16, T17, T18, T19, T20,
    T21, T22, T23, T24 ) =
    let
        fun g x =
            realLess( x, 11 )
    in
        case
            case g( T12 ) of
                false =>
                    g(
                        case g( T8 ) of
                            false =>
                                case g( T18 ) of
                                    false => T7
                            | true =>
                                realSubtract(
                                    T18,
                                    case g( T17 ) of false => T13
                                        | true => T4
                                        )
                            | true =>
                                case g( T1 ) of
                                    false =>
                                    case g( T10 ) of
                                    false => T8
```

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>1</sup>Kristin is also a master student at Hiof. Her thesis is not finished yet.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>This code has been modified from the original one to make it clean</span></small>

<!-- page: 76 -->

```ruby
| true => realSubtract( T9, T12 )
        | true => T19
      )
    | true => true     of
    false => g( T16 )
    | true => true
end
```

Code 7.1: Clean version of the best synthesized program for edge detection problem

We can easily recognize that the above program has a similar structure to a decision tree. However, as experimented by Kristin Larsen, the random forest - an ensemble learning method for classification by constructing a multitude of decision trees - was outperformed by that program. Figure 7.1 illustrates the equivalent decision tree of that program. How could the code 7.1 outperform the decision tree, random forest, or even deep neural

![](images/page_75_image_5.jpg)

Figure 7.1: The equivalent decision tree of the ADATE solution for edge detection problem; Left branches are the True cases

network classifiers as shown in the Kristin’s experiment? I hypothesize that that is come from these following abilities of ADATE’s synthesized classifier:

Feature extraction: The ADATE can discover feature extractors when they are needed. In figure 7.1, you can see that ADATE has discovered three new features: T9 − T12, T18 − T4 and T18 − T13 as highlighted in green boxes. In this case, ADATE only learned linear feature extractors (i.e. linear filters). However, it is capable of learning much more complex feature extractors. In the next example about four-way item-to-item navigation algorithm, you will see this more clearly. This ability is extremely useful when the explanatory variables are highly correlated. There is a well-known problem (may be considered as a paradox) in statistics and machine learning literature that using all available explanatory variables to build a predictive model can hurt its performance very bad. This problem occurs when some of these explanatory variables are not independent and highly correlated. One simple and famous example of this is the collinearity problem in multivariate linear regression model, when two or more explanatory variables have linear relationship.

<!-- page: 77 -->

We can overcome (or minimize) this correlation problem in many ways, such as eliminating redundant variables manually or automatically, normalizing the input, or doing feature extraction to extract useful feature from high-dimensional and highly correlated inputs. The last solution has been shown to be the best one, especially in computer vision where we have very high-dimensional inputs (images) with highly correlated components (pixels). This explains why deep learning and feature extraction have dominated in many computer vision tasks such as digits recognitions or object classification. Please refer to chapter 3 and chapter chap:autoencoder about deep architectures and autoencoders for more information about this.

• Divide and Conquer : The ADATE can split the input space into many sub-spaces, and build different feature extractors in different sub-spaces. This is a very powerful ability, which may explain why ADATE can easily synthesize classifier that fit very well to many different problems. However, this also makes ADATE’s synthesized programs easy to be overfitted. To demonstrate this power, take example of an classification problem where the posterior distribution of the target variable y conditioned on the input x: $P ( y | x )$ is different in different sub-spaces of input, we will need to fit different model to each of these sub-spaces to make the best classifier. Even if the P(y|x) is distributed consistently in the input domain, but if it is a very complex function, dividing the input domain into many sub-spaces and trying to approximate that complex function in each sub-spaces using much more simple functions is also a very good strategy. This is a similar strategy employed by the Maxout network where it uses piecewise linear functions to approximate the activation function for each neural node<sup>3</sup>. Moreover, in classification problems where the relationships between explanatory variables are different in different input’s subspaces, we also need to have different feature extractors in different input domains.

Generally, the ADATE actually builds an ensemble of many different models in different input’s sub-spaces. This divide and conquer strategy not only brings the fitting power to the ADATE system, but also introduces ovefitting problem. Splitting the input space too much will increase the chance of discovering accidental relationships (between explanatory variables and target variable as well as among explanatory variables) of ADATE system, especially when we have low-granularity training data (i.e. not enough data). Of course, the Occam’s razor employed in ADATE searching strategy, and a good validation set could be very helpful in this case. Nevertheless, empirical results showed that in general, using ADATE to build a classifier for a high dimensionality continuous input domain is more likely to create an overfitted solution, compared to other use cases of ADATE. You will see in the next section that, on regression problem, ADATE usually does not divide the input space in its solutions, which make it harder to be overfitted.

• Good Searching Strategy: Evolution strategy used in ADATE, as far as I know, is one of the best optimization technique in machine learning, which does not suffer from the local optima and other similar problems in greedy optimization methods

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>3</sup>Please refer to chapter about activation function</span></small>

<!-- page: 78 -->

such as ID3 in decision tree or gradient-based methods in neural networks. Indeed, ID3 algorithm is a very greedy approach where it choose the best node at each time, while the gradient-based optimization methods can only discover the optima that are close enough to the initial point, i.e., it can only search for a local parameter space. The evolution strategy, on the other hand, can covers much larger parameter space. However, this optimization technique runs much slower than the others, as a trade-off for its performance.

• Compact Representation: ADATE can represent a complex decision tree in a very compact way by using helper functions or nested case instructions, which could allow it to learn a very complex tree represented in only a few lines of code. This makes ADATE powerful but easy to overfit, even if the Occam’s razor employed as a regularization in ADATE. A short program is preferred in ADATE searching strategy, but even a short program could represent a very complex model.

Another good example for the feature extraction ability of ADATE system is its solution for the four-way item-to-item navigation problem, where we have to build a model to predict which item that the user want to select, providing current selected item, list of available items and the navigation direction [21]. Figure 7.2 illustrates the problem clearly, while the best ADATE’s solution is shown in Code 7.2.

![](images/page_77_image_5.jpg)

Figure 7.2: Taken from [21], mobile navigation example: Item A is selected, and the user has pressed the up-button. The model has to predict which item the user intends to select

```python
function f(
    list_of_points,
    direction_of_movement,
    current_pos
) : point
begin
    best_p = bad_initial_value
    for each point p in list_of_points do
        vector v = line from current_pos to p
        if angle between v and
            direction_of_movement < 45 degrees
```

<!-- page: 79 -->

```ruby
and
        distance( current_pos, p ) <
        distance( current_pos, best_p )
    then
        best_p = p
        return best_p
end
```

Code 7.2: Taken from [21] Pseudo code for the best ADATE’s solution

You can see that the ADATE has discovered two new features for each point p: the angle between the vector v (vector from current selected item to the point p) and the movement direction; and the difference between the distances between selected point and the current point and the best point so far (the function for calculating the Euclidean distance is given as primitive function). If these features are used when building a decision tree (instead of the point’s coordinates) to decide whether we should select the current point as the best point so far, or ignore it, it probably becomes a very easy learning problem. However, it is very hard to build new useful features for decision-making manually. Therefore, ADATE’s ability of discovering new useful features is extremely valuable.

## Categorical Explanatory Variables

In this type of problem, all of the explanatory variables are categorical. A simple toy example for this is the CAR problem, where you have to predict the risk of being stolen of a car, based on its following attributes: the car model, is it has an security alarm?, is it parked in urban or rural area?, is it parked on street or in garage?. The ADATE solution for this type of problem will look exactly like a decision tree. One of its solution is shown in Code 7.3. However, thanks to its better optimization strategy, the ADATE will probably come up with a better decision tree, compared to a decision tree learned by a traditional approach like ID3.

```scala
fun f( X0model, X1alarm, X2area, X3parking ) =
    case X0model of
        modelopel => (
            case X3parking of
                parkingstreet => rischigh
            | parkinggarage => risclow
        )
    | modelvolvo => risclow
```

Code 7.3: One ADATE’s solution for CAR problem

## 7.2.2 ADATE on Regression Problems

Regression is the problem of predicting value of a continuous variable based on other explanatory variables. In this problem, ADATE usually synthesizes solutions that can be generalized better than in classification problem. To understand this phenomenon, I have investigated the following examples.

The first simple example is the problem of predicting the velocity of a falling ball when it hits the gr<u>ound,</u> given the height H of its starting point. The correct answer for this problem is √19.6H. A typical ADATE’s solution for this problem is shown in Code 7.4.

```txt
fun f H =
    realAdd(
```

<!-- page: 80 -->

```txt
realMultiply(
        H,
        tanh( tanh( sqrt( tanh( tanh( tanh( tanh( H )) )) ) ) )
    ),
    realAdd(
        tanh( H ),
        sqrt(3)
    )
)
```

Code 7.4: Typical ADATE’s solution for SPEED problem

As you can see, the ADATE tried to approximate the correct function by a relatively complex program with some redundant operations. However, when comparing this program to a dense neural networks with only 10 hidden nodes, the solution in Code 7.4 is much simpler. A dense neural networks with only 1 input, 10 hidden nodes, and 1 output when represented in a “program” form needs 42 operations<sup>4</sup>, while the ADATE’s solution above contains only 13 operations (some operations are even redundant and can be discarded without affecting the function much)<sup>5</sup>. Therefore, a neural network has much more freedom in its parameter’s space, which could explain why ADATE’s solution for this SPEED problem can be generalized much better than a neural network. I hypothesize that the Code 7.4 can be represented by a very deep and sparse neural network, which is the current trends, and the best way in designing neural network nowadays. The Code 7.4 contains realMultiply and sqrt function, which cannot be directly translated into a neural network. However, I believe that if we only make linear operations (i.e. realAdd and realSubstract) and an activation function (e.g. tanh or sigmoid function) available as primitive functions, ADATE will generate a solution that can be represented exactly by a very deep and sparse neural network. Besides, multiplication, division, sqrt, or many other arithmetic operations can be efficiently represented by a small one-layer neural network, which is proven by [37].

Let check my hypothesis on a different problem, which contains more explanatory variables. There is a wine quality problem where we have to predict the quality of wine based on its eleven attributes: Fixedacidity, Volatileacidity, Citricacid, Residualsugar, Chlorides, Freesulfurdioxide, Totalsulfurdioxide, Density, Ph, Sulphates, and Alcohol. All of these explanatory variables are continuous. One typical ADATE’s solution for this problem is shown in Code 7.5. You can see that the synthesized model look very like a deep sparse neural network. If assumed that the realMultiply and realDivide operations in that code can be approximated by a small shallow neural network, we can actually approximate that f function by a five-layers and very sparse neural networks.

```python
fun f
    (
        Fixedacidity,
        Volatileacidity,
        Citricacid,
        Residualsugar,
        Chlorides,
```

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">4<sub>2</sub> ∗ 10 linear operations and 10 activation functions for the first layer, and 11 ∗ 1 linear operations + 1 activation function for the output layer</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>5</sup>In fact, the formula</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">H<sub>∗</sub>t<sub>anh</sub>(t<sub>anh</sub>(p(t<sub>anh</sub>(t<sub>anh</sub>(t<sub>anh</sub>(t<sub>anh</sub>(t<sub>anh</sub>(H)))))))) can be approximated by two simple linear equations: y = 0 if H < 0 and y = 0.57143H if H ≥ 0</span></small>

<!-- page: 81 -->

```txt
Freesulfurdioxide,
    Totalsulfurdioxide,
    Density,
    Ph,
    Sulphates,
    Alcohol
) =
realMultiply(
    Alcohol,
    realAdd(
        Volatileacidity,
        sigmoid(
            realAdd(
                Totalsulfurdioxide,
                realDivide(
                    realSubtract( Volatileacidity,
                            Residualsugar ),
                    sigmoid( Volatileacidity )
                )
            )
        )
    )
)
```

Code 7.5: Typical ADATE’s solution for Wine quality problem

Another very important discovery when I investigated many different ADATE’s solutions for regression problems is that the ADATE system usually does not synthesize programs that split the input space into different sub-spaces, as in case of classification problems. Without these divide and conquer ability, the ADATE has lost a very important part of its fitting power. This lost, however, makes the ADATE system much harder to be overfitted. Generally, on regression problems, the ADATE has to build a single model for the whole input space, instead of building different simple model for different parts of the input domain. This may explain why the generality of ADATE’s solutions for regression problem is better that its solutions for classification problems.

The evolution strategy used in ADATE can be a possible factor which causes this phenomenon. The evolution strategy searches for the smallest programs first. After that, it generates other bigger programs by applying different kinds of transformation and mutation. In regression problem, we need the function f to return a continuous value. Therefore, the smallest programs which return continuous values will be more likely to be picked for later transforming and mutating. If ADATE tries to add a “case” instruction into an existing program, that case instruction has to condition on a continuous variable, which can not serve as a branching statement. Of course, the ADATE can first apply a function that returns a boolean value like “realLess” function, and introduce the case instruction after that. However, because boolean values can not be used in an equation of real-value variables, the ADATE usually ignores these transformations. In other words, if the ADATE wants to add a branching statement into a current program, it must allow a two-step transformation, where it can add a boolean-return function and a case instruction at the same time. Because if it, almost any case instruction in ADATE’s solutions for regression problems serves as an declaration instruction for temporary variables instead of a branching statement. Of course, the ADATE system can take advantages of categorical explanatory variables to generate branching statement if they exist. However, in typical regression problems, all of the explanatory variables are continuous.

<!-- page: 82 -->

## 7.2.3 ADATE on Classical algorithm

ADATE has been proven able to generate the correct algorithms for many different classical problems, such as: inserting and deleting a node in binary tree, generating all permutations of a list, or sorting a list. We would probably ask why it could generate the correct answers, instead of an approximate answer, for this task. I believe that the following reasons may answer the question:

• Existence: ADATE can discover the correct solutions for these problems may be just because they exist. In typical classification or regression problems, there is usually a probabilistic model behind the scene, instead of a deterministic model. Therefore, synthesizing an exact algorithm for these tasks is impossible.

• Suitable Representation: ADATE represents its answer in a “functional program” form, which is very suitable for expressing algorithms. Besides, these algorithms have correct answers that can be represented in a very short functional program, which is exactly what the ADATE evolution strategy prefers.

• No Constant: I hypothesize that ADATE is not very good at generating a constant number in its program. It may be because a constant number that is useful in current program will become completely irrelevant in its transformations. In other words, unlike other operations, a constant number depends very much on the program context, and when we change the program just a little bit, it becomes useless. However, you probably will not see any random constant number in classical algorithms, which may help the ADATE very much.

Code 7.6 illustrates one of the best ADATE’s solution for sorting problem, where you have to sort a list of integer number into ascending order.

```ruby
fun f (V1) =
    case V1 of
        nil => V1
    | (V1_1 :: V1') =>
    let
        fun g (V2) =
            case V2 of
                nil => (V1_1 :: nil)
            | (V2_1 :: V2') =>
            case (V1_1 < V2_1) of
                true => (V1_1 :: V2')
            | false =>
                (V2_1 :: g( V2' ))
    in
        g( f( V1' ) )
end
```

Code 7.6: An ADATE’s solution for sorting problem

This code is hard to understand at first sight. But if we look closer, we can see that the variable V 1 1 is included in the closure of the $g ( . )$ function. Therefore, we can change the function call $g ( f ( V 1 ^ { \prime } ) )$ into $g ( V 1 \_ 1 , f ( V 1 ^ { \prime } ) )$ . Now, that tail recursion is trying to apply the g function on all components of V1. For example, if $V 1 = A 1 : : A 2 : : A 3 : : A 4 : : n i l ,$ that tail recursion is equivalent to this function call:

$$
g (A 1, g (A 2, g (A 3, g (A 4, n i l))))\tag{7.1}
$$

<!-- page: 83 -->

Now if we change the name of function $g ( x , V )$ into insert $i ( x , V )$ , the equation 7.1 is now equivalent to

$$
\text {insert} (A 1, \text {insert} (A 2, \text {insert} (A 3, \text {insert} (A 4, \text {nil}))))\tag{7.2}
$$

We can see that if the inser $t ( x , V )$ function returns a sorted list by insert x into $\mathrm { V } ,$ given that V is a sorted list, then the algorithm is correct. Look at the body of insert $t ( x , V )$ function in Code $7 . 6 ^ { 6 }$ , you can see that it compare x to the first element $y$ in $V$ . If x smaller than $y ,$ then it return the list $x : : V$ . However, if x is equal or greater than $y ,$ then $y$ will be the first element in the return list. The rest of return list will be sorted again by calling $i n s e r t ( x , V ^ { \prime } )$ with $V ^ { \prime }$ is the vector V after removing its first element $y .$ This recursion continues until x smaller than $y$ or V becomes nil. Therefore, this ADATE’s solution for sorting problems is indeed a correct algorithm.

## 7.2.4 ADATE on Meta-learning

One special ability of ADATE that you cannot find in most of other machine learning tools is that it can do meta-learning or “learn how to learn”. It means that we can use ADATE to improve other algorithms or machine learning methods. The evolution strategy that employed in ADATE is very flexible which allow it to work in very different ways.

Most of machine learning optimization methods need a well-defined continuous objective function, which represents a clear relationship between the current model’s parameters configuration and its performance. Based on that function, they use some searching strategy to optimize the parameters, such as gradient-based methods. For example, the mean squared errors is a common objective function in regression, while negative log likelihood is used in classification problems. The need of continuous objective function limits the possible problems that these methods can be applied on.

On the other hand, the ADATE system uses fitness function in its searching strategy. Although the fitness function can be considered as a special type of objective function, it is very different from other types. Generally, it is not needed to be a continuous function, and the relationship between a model and its fitness measurement can be very vague. Therefore, we usually cannot get any gradient information from a fitness function.

One example that can demonstrate this ADATE flexibility clearly is using ADATE to improve decision tree pruning [13]. In this problem, the authors wanted to improve an error based pruning (EBP) algorithm used in C4.5 decision tree. Starting from the initial $f$ function that is a naive implementation of EBP, ADATE has discovered a better version of it. The original $f$ function is relatively long and complicated function. Therefore, I only choose a small part of it to demonstrate the ADATE flexibility. Code 7.7 shows the original and improved version of errorEstimate function used in EBP algorithm. This function takes two arguments: n – the number of instances that reach a given tree node, and $c -$ the number of these instances that are correctly classified by the subtree corresponding to the node.

```ocaml
(* Original errorEstimate(.) function *)
fun errorEstimate ( ( c , n) : real * real ) : real =
let
  val e = (n - c)/n
  val z = 0.69
  val z2 = z * z
  val val1 = (e/n) - (( e*e )/n )) + (z2/(4 . 0*n*n))
```

<sup>6</sup>the $g ( V 2 )$ function is the inser $t ( x , V )$ function with x is V 1 1 and V is V 2

<!-- page: 84 -->

```txt
val val2 = (e + z2 / (2 . 0 * n)) + z*(sqrt val1)
val val3 = 1.0 + z2/n
in
  val2/val3
end
(* Improved errorEstimate(.) function *)
fun errorEstimate ( ( c , n) : real * real ) : real =
let
  val v1 = tanh( tanh( tanh( (n - c) / n)))
  val v2 = sqrt( tanh( tanh( sqrt( n)))) )
  val v3 = tanh( sqrt( sqrt( c)))
in
  (v1 + v2) / v3
end
```

Code 7.7: The original and synthesized errorEstimate function used in EBP algorithm

This can be considered as a regression problem, where we want to predict (i.e. estimate) the error value, based on the two explanatory variables c and n. The ADATE’s solution for this problem can also be represented by a neural network. However, we cannot directly use neural networks or other machine learning methods on this problem, because there is no clear relationship between the output of the function errorEstimate(.) and its performance. In ADATE, that errorEstimate(.) function is called in the decision tree code, which then is tested in several different training datasets to check its performance.

In general, the ADATE can be, and has been, successfully used to improve other machine learning methods, especially when they include heuristic functions. However, the current version of ADATE has some following limitations, which can possibly be fixed in future:

• Slow Searching Strategy: Evolution strategy is a very good but slow optimization method. Therefore, we usually need to design small artificial datasets to train the ADATE first, before generalizing its solution to the real-world problems. However, in some cases, its solutions for the small datasets cannot be generalized well to other bigger datasets. This maybe comes from a bad design of artificial datasets, or bad ADATE’s configuration.

• Synthesized program can’t be called: In current ADATE version, outside of the ADATE-ML part, the synthesized program cannot be called. This means that you have to implement the whole original algorithm in ADATE-ML if you want to call the synthesized program in your algorithm. This work is not trivial, because ADATE-ML is a simplified version of Standard-ML, which is a very small and limited language. However, this limitation is going to be fixed soon. In the next ADATE version, the synthesized program may even be called from C or other external programs, which will make ADATE much easier to use and experiment. This change can also speed up the ADATE system, because programs written in C usually run much faster than their ML versions.

Hard to understand: One reason that makes ADATE’s improved version of other machine learning methods unpopular is that we usually cannot understand completely the synthesized program. It means that we cannot prove the correctness of that program in a mathematical way, which is usually desired by other researchers.

<!-- page: 85 -->

## Chapter 8

# ADATE Experiments

This chapter presents our experiments as a process, which can answer all of the research questions posed in Chapter 1. Based on deep learning knowledge that we summarized in previous chapters, we analyzed why we chose the initialization part of deep learning algorithm to experiment first. After that, we presented how we built tiny datasets and neural networks library for ADATE. After running the ADATE system to evolve the initial sparse initialization scheme, we got the sparse-3 program, which will be analyzed carefully in this chapter. A short analysis of overfitting problem of synthesized programs is also presented at the end of the chapter.

## 8.1 Selecting Target

The previous chapters about deep learning present many deep learning methods, which could possibly be improved by ADATE. The most valuable one if we could improve is the unsupervised pre-training method. However, this is a complex and time-consuming process, which is hard to work on for the first experiment. We wanted to select a simple but effective method, which does not have dependency relationship with other parts of the deep learning process. The most potential targets are:

• Autoencoder models: many different types of autoencoders have been introduced in chapter 3. By adding an extra term into the objective function, we can get a much better version of autoencoders. We can use ADATE to discover a new better term. However, we need to take the gradient of the new objective function automatically, which is relatively hard and error-prone.

• Optimization methods: chaper 4 shows that the neural networks performance can be improved significantly by changing the initialization scheme or the momentum schedule without using pre-training methods. While improving momentum schedule is currently not possible with current version of ADATE, the initialization scheme is a seperate part of the training process and can easily be improved by ADATE.

• Regularization methods: chapter 5 presents dropout and dropconnect, the two very new but effective regularization methods. However, we have to call the regularization method for each iteration of the training process, which is not possible in current ADATE version.

<!-- page: 86 -->

• Activation function: chapter 6 shows that by changing the activation function, we can improve the network’s performance. However, because we have to take the gradient of the new activation function automatically, this is not an easy target.

Therefore, the initialization scheme was chosen for our first experiment with ADATE. Other parts of the deep learning process are also potential, but we have to wait until the next version of ADATE, when we can call the synthesized program from outside of the ADATE part.

## 8.1.1 Checking the Effectiveness of Initialization Schemes

Before starting to improve the initialization scheme, we had to check if changing it makes a significant difference in the network’s performance. In this experiment, we trained a deep neural network with 3 hidden layers, their corresponding sizes are: 500, 500 and 2000, using steepest gradient descent with momentum suggested in [46]. L2 weight decay was also used and fixed at 10<sup>−5</sup>. The batch size is chosen at 200 as in [46]. Basically, all hyper-parameters in our experiment are fixed, except for the learning rate and initialization method as presented in table 8.1.

Table 8.1: Parameters used when training on MNIST dataset

| Parameters | Configuration |
| --- | --- |
| Dataset: | MNIST |
| Network structure: | [784 500 500 2000 10] |
| Cost function: | Negative log likelihood |
| MMoommeennttuumm mschaxed: ule: | µ = min(1 - 2-1-log<sub>2</sub>(bt/250c+1),µ0<sub>m</sub>.9<sub>a</sub>9<sub>x</sub>9) |
| L2 weight decay: | 10<sup>-5</sup> |
| Batch size: | 200 |
| Learning rates: | chosen from [0.05 0.01 0.005 0.001 0.0005 0.0001] |
| Initialization methods: | Normal; Normalized; Sparse |

In the first experiment, we trained the network for all possible combinations of learning rate and initialization method and stop the training process after the first 100 epochs. The result is expected to be noisy because of random initialization and 100 epochs are not enough to get the training process to be saturated, especially with small learning rate. However, we can still see the difference in performance of different initialization methods on different learning rate.

Table 8.2: Test error rates after first 100 iterations for different learning rates and initializations Initialization Learning rates

<table><tr><td>Initialization</td><td colspan="6">Learning Rates</td></tr><tr><td></td><td>0.05</td><td>0.01</td><td>0.005</td><td>0.001</td><td>0.0005</td><td>0.0001</td></tr><tr><td>Normal:</td><td>4.33%</td><td>2.89%</td><td>3.92%</td><td>6.57%</td><td>7.89%</td><td>10.76%</td></tr><tr><td>Normalized:</td><td>4.44%</td><td>3.17%</td><td>4.46%</td><td>7.28%</td><td>8.27%</td><td>11.21%</td></tr><tr><td>Sparse:</td><td>3.86%</td><td>2.94%</td><td>3.47%</td><td>4.6%</td><td>5.26%</td><td>7.56%</td></tr><tr><td> $\Delta_{\text{Normal-Sparse}}$ :</td><td></td><td></td><td colspan="2">1.45% ± 1.34%</td><td></td><td></td></tr><tr><td> $\Delta_{\text{Normalized-Sparse}}$ :</td><td></td><td></td><td colspan="2">1.86% ± 1.43%</td><td></td><td></td></tr></table>

<!-- page: 87 -->

In table 8.2, we can see that sparse initialization consistently outperforms other methods, regardless of what learning rate is using.

In the second experiment, we checked performance of different initialization methods at 0.01 learning rate, which is the best learning rate for all of them in previous experiment. For each initialization method, we trained the network 5 times in attempt to reduce noise produced by random initialization. The result in table 8.3 shows the same thing in the first experiment, but with lower noise. We again see that sparse initialization can easily outperform other initialization methods, at the same or different learning rate.

Table 8.3: Test error rates after first 100 iterations for different initializations at the same learning rates

<table><tr><td>Initialization</td><td colspan="5">Learning rates</td></tr><tr><td></td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td></tr><tr><td>Normal:</td><td>3.08%</td><td>2.96%</td><td>3.05%</td><td>3.17%</td><td>3.12%</td></tr><tr><td>Normalized:</td><td>3.11%</td><td>3.16%</td><td>3.11%</td><td>3.19%</td><td>3.01%</td></tr><tr><td>Sparse:</td><td>2.70%</td><td>2.56%</td><td>2.60%</td><td>2.45%</td><td>2.69%</td></tr><tr><td> $\Delta_{\text{Normal-Sparse}}$ :</td><td colspan="5">0.48% ± 0.139%</td></tr><tr><td> $\Delta_{\text{Normalized-Sparse}}$ :</td><td colspan="5">0.516% ± 0.164%</td></tr></table>

These two above experiments proved that initialization scheme is an essential part of the training process. In addition, if we can improve it by ADATE, we can improve the network’s performance significantly.

## 8.2 Building Tiny Datasets

ADATE usually needs to generate and evaluate at least hundreds of thousand or even millions of different programs before possibly discovering the best ones. Therefore, using huge dataset like MNIST directly is definitely impossible. Other smaller datasets such as Curves or USPS could not help also. What we need is a tiny dataset, on which training a DNN costs least than ten seconds. Besides, one crucial property that the tiny dataset has to possess is that an initialization scheme that performs well on it can be generalized and perform as well on other real and bigger datasets.

## 8.2.1 TinyDigits

In our first experiment, after searching for many possibilities, we finally ended up using the TinyDigits dataset. TinyDigits is a 10x10 digits images dataset, which is generated using the elastic deformation.

We chose to generate our own synthetic dataset consisting of 10x10 pixel images of digits that are distorted using elastic deformations. To generate this so-called TinyDigits dataset, we first hand-designed three different 8x8 pixel patterns for each digit. From these patterns, we extended their border to get 10x10 pixel images, and ran elastic deformation to auto-generate other training examples. We used the following parameters for the elastic deformation algorithm in TinyDigits:

• α and σ: parameters for elastic distortions; set to 3 and 7 respectively. (see Simard et al. 2013 [44] for more details).

<!-- page: 88 -->

![](images/page_87_image_2.jpg)

Figure 8.1: Elastic deformation and TinyDigits. First line: a hand-designed pattern for the digit $\mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } ^ { \mathrm { { } } ^ { \mathrm { { } } ^ { \mathrm { { } } ^ { \mathrm { { } } ^ { \mathrm { { } } ^ { \mathrm { { } } ^ { \mathrm { } { } ^ { \mathrm { } } ^ { \mathrm { { } } ^ { \mathrm { } } ^ { \mathrm { } { } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { } } ^ { \mathrm { } } ^ \mathrm { } } ^ { \mathrm { \mathrm { } } ^ { \mathrm } { } ^ \mathrm { } } ^ { \mathrm { \mathrm } { } ^ { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { } } ^ \mathrm { } } ^ { \mathrm { \mathrm { } } ^ \mathrm { } } ^ { \mathrm { \mathrm } { } ^ \mathrm { } } ^ { \mathrm { \mathrm } { } ^ \mathrm { } } ^ { \mathrm { \mathrm } { } } ^ \mathrm { } ^ { \mathrm { \mathrm } { } } ^ \mathrm { } ^ { \mathrm { \mathrm } { } } ^ \mathrm { } } ^ { \mathrm { \mathrm { } } ^ \mathrm { \mathrm { } } ^ { \mathrm { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { \mathrm } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { \mathrm } { } } ^ } ^ { \mathrm { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } { } ^ { \mathrm } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm { } } ^ { \mathrm { \mathrm } } ^ { \mathrm { } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { } } ^ { \mathrm } } ^ { \mathrm { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } { } } ^ } ^ { \mathrm { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm { } } } ^ { } } ^ { \mathrm \mathrm { \mathrm { } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm } { } } ^ { \mathrm } ^ { \mathrm { \mathrm { \mathrm } { } } ^ { \mathrm } { } ^ { \mathrm \mathrm { } } ^ { \mathrm { \mathrm { } } } ^ { \mathrm { \mathrm { } }$ and its deformed versions. Two bottom lines: examples of generated digits from 0 to 9. Note that all of these deformed images are intelligible

$\beta ;$ a random angle from $\left[ - \beta , \beta \right]$ is used for rotation; set to $\frac { \pi } { 1 2 }$ .

$\gamma ;$ a random scaling from $\textstyle [ 1 - { \frac { \gamma } { 1 0 0 } } , 1 + { \frac { \gamma } { 1 0 0 } } ]$ is used for horizontal and vertical scaling; set to 15.

The elastic deformation and the TinyDigits dataset are illustrated in Figure 8.1.

## 8.2.2 TinyUSPS

After testing some ADATE-generated initialization schemes, we suspected that they are overfited to the TinyDigits task. To test this hypothesis, we need more different tiny datasets, because testing on the original MNIST is time-consuming<sup>1</sup>. TinyUSPS was our first and very simple solution.

USPS is the US Postal Service handwritten digits recognition corpus. It contains normalized grey scale images of size 16x16, divided into a training set of 7291 images and a test set of 2007 images. We took the center 10x10 pixels of these USPS images to create the TinyUSPS dataset. Of course, doing this way could discard some useful information for distinguishing different numbers, which makes the task harder. However, this dataset was indeed very useful and helped us recognize the overfitting problem clearly.

## 8.2.3 Compressed MNIST, Cifar-10, and SVHN

Three of the most famous datasets for image recognition task are MNIST, CIFAR-10 and SVHN:

• The MNIST is a handwritten digits dataset, which has a training set of 60,000 examples, and a test set of 10,000 examples. The digits have been size-normalized and centered in a fixed-size image.

• The CIFAR-10 dataset is an object recognition dataset which consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

<sup>1</sup>we need to re-optimize many hyper-parameters on the MNIST dataset first, and then train the neural network for at least 10 times to check if the differences are statistical significant

<!-- page: 89 -->

• The Street View House Numbers (i.e. SVHN) is a real-world image dataset which can be seen as similar in flavor to MNIST (e.g., the images are of small cropped digits), but comes from a significantly harder, unsolved, real world problem (recognizing digits and numbers in natural scene images). SVHN is obtained from house numbers in Google Street View images.

![](images/page_88_image_3.jpg)

Figure 8.2: From top to bottom: MNIST, CIFAR-10 and SVHN datasets

MNIST, Cifar-10, and SVHN datasets contain much bigger images compared to the USPS (28x28, 32x32, and 32x32 respectively). Therefore, taking 10x10 center pixels of the images would make them unrecognizable, and change the task completely. One possible solution is that we can train a deep autoencoder to compress these datasets. For MNIST, we have used the network: [784-1000-500-100-500-1000-784] and [784-1000-500-30-500-1000-784] to create the compressedMNIST100 and compressedMNIST30 respectively. Other similar network architecture was also used for Cifar-10 and SVHN.

Currently, we use the Hinton implementation of deep autoencoder, which uses staked RBM for pre-training and Conjugate Gradient for fine-tuning. Of course, there are other

<!-- page: 90 -->

newer and better ways to train a deep autoencoder, such as using staked denoising autoencoder or sparse autoencoder. However, the Hinton’s implementation is easy to use and still a good one.

## 8.3 Design and Implementation

As mentioned earlier, a neural network library has to be implemented in SML before being able to take advantage of ADATE to improve some parts of it. Within this chapter, I will report how I had designed and developed the library. This is indeed a time-consuming and error-prone process, on which I did make several mistakes. Therefore, I want to share my experience on this process, which could be very helpful for other students or researchers. It took me months to overcome all of these mistakes.

Because SML does not support matrix operations and some useful random number generators, I had to build these libraries myself also. I also build a small unit-test library to test my implementation.

All the codes mentioned in this section are provided in Appendix A

## 8.3.1 Matrix library

Matrix operations are essential part of many machine learning algorithms, which base heavily on linear algebra. After searching for an efficient matrix library for SML and could not find any, we have decided to implement a new one. This library represents a matrix as a list of list, which supports common operators on matrix, including multiply, dot multiply, sum, . . . Besides, there is also print functions to help debugging process easier. Storing a matrix as list of list, instead of array of array, makes the implementation efficient and fit naturally in SML language. Many functions were inspired by the standard List library of SML. Besides, all matrix operators in this library have the equivalent complexity compared to what could be done using array of array implementation. We believe that with this library, we can re-implement many different machine learning algorithms easily.

However, we are trying to replace this matrix library by the standard BLAS library, which could provide much higher matrix operations’ performance. Please check the Chapter 9 about future works for more details.

## Matrix data structure

In this library, the matrix data type is defined as:

```ocaml
type 'a vector = 'a list
datatype 'a matrix =
    COLMATRIX of ('a vector list * int * int)
    | ROWMATRIX of ('a vector list * int * int)
```

There are two matrix types: COLMATRIX - matrix that stored as list of column vectors; and ROWMATRIX - matrix that stored as list of row vectors. This storing way could make many matrix operations become as efficient as using array of array. Changing between COLMATRIX and ROWMATRIX type has complexity O(n ∗ m) with n and m are the number of rows and columns of the matrix. However, we can easily transpose a matrix (and switch the matrix type at the same time) instantly at O(1) complexity. A

<!-- page: 91 -->

matrix also has its size in its data structure - the last two number in the tuple - to make checking size operations more efficient. We also provide a checkV alid function to check if a matrix is valid or not. However, if we are using this library as a separated module, the matrix datatype is hided and can only be created using one of the provided initialization functions, which makes sure that all the matrices are valid at all time. These mentioned functions above have the following signatures:

```txt
val changeType:        'a matrix -> 'a matrix
    val transpose:            'a matrix -> 'a matrix
    val checkValid:       'a matrix -> bool
    val size:             'a matrix -> int * int
```

Matrix in this library can be either an int matrix or a real matrix. However, because SML is a static type language, many matrix operations have an int and a real version. We provide six different ways to initialize either a column or a row matrix, which have the following signatures:

```ocaml
val zeroesRealCols: int * int -> real matrix
val zeroesRealRows: int * int -> real matrix
val zeroesIntCols: int * int -> int matrix
val zeroesIntRows: int * int -> int matrix
val fromList2Cols: 'a list * int * int -> 'a matrix
val fromList2Rows: 'a list * int * int -> 'a matrix
```

There are also two printing functions, one for real matrix and one for int matrix, to support debugging:

```txt
val printMatrixReal: real matrix -> unit
val printMatrixInt: int matrix -> unit
```

This library uses two exceptions: W rongM atrixT ype and UnmatchedDimension. It raises the WrongMatrixType exception when the input matrix is not at the desired type, and raises the UnmatchedDimension when the dimension of a matrix itself is unmatched (not a valid matrix) or the two input matrices’ dimensions are unmatched (as in matrix multiplication).

## Scalar operators

Scalar operators are the operators that affect all matrix elements in the same way, such as add a number to the whole matrix. All scalar operators in this library are implemented based on the function map f m, which apply f to all elements in the matrix m. This function is very similar to the function List.map, and indeed implemented based on it:

```txt
fun mapVectors f vs =
    List.map (fn v => List.map f v) vs

fun map f (COLMATRIX(vs, rows, cols)) =
    COLMATRIX (mapVectors f vs, rows, cols)
    | map f (ROWMATRIX(vs, rows, cols)) =
        ROWMATRIX (mapVectors f vs, rows, cols)
```

<!-- page: 92 -->

Using this map function, we can easily implement any scalar operators, for example:

```txt
fun addScalarInt (m, x:int) = map (fn a => a+x) m
fun addScalarReal (m, x:real) = map (fn a => a+x) m
fun mulScalarInt (m, x:int) = map (fn a => a*x) m
fun mulScalarReal (m, x:real) = map (fn a => a*x) m
```

## Matrix Element-wise operators

Matrix element-wise operators are the operators that take two equal-size matrices and combine their elements at the same position by an arbitrary function to a new create a new matrix. All matrix element-wise operators in this library are based on the merge function, which take a combining function and two input matrices to produce a new one. It use function mergeVector to merge two vector, and mergeVectors to merge two list of vectors:

```javascript
fun mergeVector f v1 v2 =
    case (v1, v2) of
        ([], [])=>[]
    | (hdv1::v1', hdv2::v2') =>
        f(hdv1, hdv2)::(mergeVector f v1' v2')
    | _ => raise UnmatchedDimension

fun mergeVectors f vs1 vs2 =
    mergeVector (fn (v1, v2) => mergeVector f v1 v2)
        vs1 vs2

fun merge f (m1, m2) =
    case (m1, m2) of
    (COLMATRIX(vs1, r1, c1), COLMATRIX(vs2, r2, c2)) =>
        COLMATRIX(mergeVectors f vs1 vs2, r1, c1)
    | (ROWMATRIX(vs1, r1, c1), ROWMATRIX(vs2, r2, c2)) =>
        ROWMATRIX(mergeVectors f vs1 vs2, r1, c1)
    | _ => raise WrongMatrixType
```

Using this merge function, we can easily implement any other matrix element-wise operators, such as:

```scala
val dotMulMatrixInt = merge (fn (a:int, b)=>a*b)
val dotMulMatrixReal = merge (fn (a:real, b)=>a*b)
val addMatrixInt = merge (fn (a:int, b)=>a+b)
val addMatrixReal = merge (fn (a:real, b)=>a+b)
```

## Matrix multiplication

Matrix multiplication is the most time-consuming operation in many algorithms. Therefore, We tried to make this operation as fast as possible. This library only allows multiply a ROWMATRIX to a COLMATRIX, and raise the exception WrongMatrixType in all other cases. Because only in that case, we can multiply the two list of list right away to produce the desired matrix product. Of course, we can use changeT ype() function to

<!-- page: 93 -->

change the matrix type to the desired one. However, that process costs O(n ∗ m) and we decided to force the users do it manually, to make sure that they are aware of that overhead computing cost. Besides, users can choose to produce a ROWMATRIX or a COLMATRIX as the matrix result. I believe that with this flexibility, you usually do not have to change the matrix type in most algorithms. Moreover, the transpose operation in this library literally cost nothing while costing O(n ∗ m) if using array of array implementation. Therefore, using transpose function can compensate for using changeType function.

Implementation of matrix multiplication is a little bit more complicated than the above functions. It uses three helper functions: foldl2Vectors, mulVectorsVector and mulVectors. The foldl2Vectors is very similar to the List.foldl function, but take two equal-size input vectors and fold them using an input function. The mulVectorsVector function multiplies a list of vectors to a vector, and the mulVectors multiplies two lists of vector. The signature of the matrix multiplication functions are:

```txt
val mulMatrixIntR: int matrix*int matrix->int matrix
val mulMatrixIntC: int matrix*int matrix->int matrix
val mulMatrixRealR: realmatrix*realmatrix->realmatrix
val mulMatrixRealC: realmatrix*realmatrix->realmatrix
```

## 8.3.2 RandomExt library

Because SML does not have any built-in function for Gaussian random number generator or random permutation operator, which is needed in neural network implementation, we had to implement them myself. For the Gaussian random generator, we used the Box–Muller method, which is very well-known and popular. For generating random permutation (i.e. shuffling), the Fisher–Yates method was used.

• Box–Muller method: is a pseudo-random number sampling method for generating pairs of independent, standard, normally distributed (zero expectation, unit variance) random numbers, given a source of uniformly distributed random numbers. There are two ways to implement this method: take samples from uniform distribution on the interval (0, 1] or [-1, +1]. In our implementation, we used the second one, which takes two samples from the uniform distribution on the interval [-1, +1] and maps them to two standard, normally distributed samples U(0, 1)

• Fisher–Yates method: also known as the Knuth shuffle (after Donald Knuth), is an algorithm for generating a random permutation of a finite set–in plain terms, for randomly shuffling the set. The Fisher–Yates shuffle is unbiased, so that every permutation is equally likely. Fisher–Yates shuffling is similar to randomly picking numbered tickets out of a hat without replacement until there are none left.

## 8.3.3 Smlunit library

Building Matrix, RandomExt, and Neural network library require implementing many different mathematical formula, which are very hard to debug if any mistake is made. Therefore, unit test is a must in this project. After searching and could not find any suitable unit-test library for SML, we had to build our own one, which is simple but

<!-- page: 94 -->

functional. This library supports comparing different datatype, measuring running time, and setting time out (for avoiding endless loop).

The most important function in this library is assertFun(), which let us test one inputoutput pair (i.e. test case) when applying the input into a specific function. Because SML is static type language which does not support type inference, the assertFun() function also needs us to provide the isEqual() function, which helps it compare the desired output and the function result. Each test case also has a corresponding explanation, which will be printed out while testing to help debugging easier. The library also provide the assertFuns() function which let us test a list of test case (i.e. test suits) for a specific function. Using assertFun() and assertFuns() functions, we can easily create appropriate testing function for different output datatypes.

```rust
//--------assertFun() function-------//
fun assertFun isEqual f (input, output, desc) =
    let
    fun runFun ()
        let
            val timer = Timer.startRealTimer()
            val result = f(input)
            val time = p_time (Timer.checkRealTimer timer)
        in
            (result, time)
        end
    val (result, time) = runFun();
    in
        assert isEqual (result, output,
                desc ^ " (" ^ time ^")")
    end

//--------assertFuns() function-------//
fun assertFuns isEqual f desc testcases =
    let
        val assert = assertFun isEqual f;
        fun assertAll [] = ()
            | assertAll (testcase::testcases) =
                (assert testcase; assertAll (testcases))
    in
        (print ("--------" ^ desc ^ " ----------\n");
        assertAll (testcases))
    end
```

Code 8.1: implementation of assertFun() and assertFuns()

Every library that we have implemented for this thesis has its own unit-test file to check its correctness. Whenever any function is modified or added, we update the unit-test file to reflect the desired changes, and run these files to check that all existing functions are working well, and new modification does not interfere with them.

## 8.3.4 Neural Network Library

Neural network is in fact a general term to indicate a type of model, which consists many different types of techniques from initialization schemes, training algorithms, to regularization methods... To build a flexible and extendable library, we modularized the neural network training process into different parts, which different techniques can be

<!-- page: 95 -->

chosen to apply on. We also designed a new appropriate data structure for neural network model, which helps developing process become easier.

## Datatype

Neural network is a layered model, which are connected by adaptive weights. Based on these properties, we represent a neural network by a list of layer, where each layer consists of one layer of weight (not layer of node), and has the following datatype:

```txt
type nnlayer = {
    input: real matrix, (* ROWMATRIX *)
    output: real matrix, (* ROWMATRIX *)
    GradW: real matrix, (* COLMATRIX *)
    GradB: real vector,
    B: real vector,
    W: real matrix,        (* COLMATRIX *)
    actType:actType
}
```

Code 8.2: datatype for one layer neural network

As you can see, each layer consists of input and output vector, which represent activation activities of input and output nodes of that layer. Besides, W and B represent the weights and bias matrix. Because different layer can have different type of activation function, there is actType field to keep this information. We also include the gradW and gradB matrix, which are the gradients calculated by a particular training algorithm.

Moreover, because there are different techniques and training options that you can choose from before training, we created a params datatype, which contains all these information and can be set through function setParams(). Figure 8.3 shows the params datatype and all available training options so far.

```txt
type params = {
    batchsize: int,      (* number of training cases per batch *)
    nBatches: int,      (* number of batches *)
    testsize: int,      (* number of testing cases *)
    lambda: real,       (* momentum coefficient *)
    momentumSchedule: bool,  (*use/no use Marten's momentum schedule*)
    maxLambda: real,   (* max momentum used in momentum schedule*)
    lr: real,           (* learning rate *)
    costType: costType,  (* cost function type
        support: NLL|MSE|CE|PER*)
    initType: initType,  (* initialization type
        support: SPARSE|NORMAL|NORMALISED*)
    actType: actType,   (* activation function type
        support: SIGM|TANH|LINEAR*)
    layerSizes: int list,  (* structure of network *)
    initWs: real matrix option list,  (* pre-initialized Ws matrices *)
    initBs: real vector option list,  (* pre-initialized Bs matrices *)
    nItrs: int,   (* number of iterations/epochs *)
    wdType: wdType,     (* weight decay type
        support: L0|L1|L2 *)
    wdValue: real,       (* weight decay value *)
    verbose: bool  (* print training information or not *)
}
```

Code 8.3: Params datatype which shows all available training options

<!-- page: 96 -->

## Modules

The general neural network training process are modularized as shown in figure 8.3. Implementation of these process boxes are the following functions:

• Pre-processing and batches creating: implemented by function readData, which can read a dataset contained in a CSV files, and split it into a list of batches.

• Network architecture: is defined in params variable and set by function setParams().

• Initialize Network: each type of initialization scheme is implemented in different function. Each function takes responsibility of initializing one network layer, and will be called by function initLayers() to generate the whole initialized network. We can also predefine the initialized neural networks by using setParams(), which is very useful when using ADATE to improve the initialization scheme.

• Forward propagation: implemented by fprop1layer() and fprop() functions, which do forward propagating for one layer and the whole network respectively.

• Compute cost: implemented in computeCost() function, which currently supports: mean square errors (MSE), cross entropy (CE), and NLL (negative log likelihood). This function is also used to compute the error rates of the network.

• Compute search direction and step size: currently, this neural network library only supports the SGD training algorithm together with momentum. This training process is computed through back propagation, which propagates the gradient of cost function from the last to the first layer. This process is implemented by bprop1layer() and bprop() for back propagating one layer and for the whole network respectively.

• Update weights: implemented by update1layer() and update() functions, which can update one layer and the whole network respectively.

• Stop criteria: currently the training process is stopped after a specific number of epochs (stored in the nItrs field of params). However, there are two options for the return value: performance of the last trained network (by using trainNN() function) or the best network during the training process (by using trainBest() function).

## 8.3.5 Important Warning!

We highly recommend that you should use Mlton instead of Standard ML of New Jersey (i.e. SML/NJ) for compiling final SML code. Mlton is a whole-program optimizing compiler for SML, which can produce very fast executables file (compared to other SML compiler). In our experience, Mlton produce executable file that run at least five times faster than SML/NJ. More importantly, the floating-point operations in Mlton are equivalent to which of Matlab or C++. We usually implement new algorithm in Matlab first, because it is easier and run faster. After that, we re-implement it in SML. Therefore, we need these two implementations to produce exactly the same result. However, if the SML/NJ is used, it is almost impossible.

However, for writing code, we still recommend using SML/NJ, because it supports a nice REPL (Read–eval–print loop) - an interactive programming environment - which you

<!-- page: 97 -->

![](images/page_96_image_2.jpg)

Figure 8.3: General flow chart of gradient-based training algorithms for Neural Networks

<!-- page: 98 -->

cannot find in Mlton. Moreover, you should use Emacs as the SML text editor. It has SML mode that provides good syntax highlighting, indentation, and integration with the SML environment.

## 8.4 Writing Specification file

Thanks to the Neural Network library, writing specification file was pretty simple. The f(.) function is the function that returns a list of initialized weights for each node in the neural network. The original f(.) was the sparse initialization scheme. The only problem was that the f(.) function is written in ADATE-ML part, which does not support the SML list datatype which is used in the neural network library. Therefore, we needed helper functions that transforms the ADATE-ML datatype to SML datatype.

The neural network in ADATE-ML defined as a weightMatrix list datatype:

```txt
datatype real_list = rnil | consr of real * real_list

datatype real_list_list = rlnil | consrl of real_list * real_list_list

datatype weightMatrix = weightMatrix of real * real_list_list

datatype weightMatrix_list = wnil | consw of weightMatrix *
    weightMatrix_list
```

while in neural network library, the neural network is represented by a list of matrix, which in turn is a list of list also.

The following functions was used to transform the weightMatrix list datatype into list of matrix datatype.

```ocaml
(* convert ADATE list type to ML list *)
fun toRealListListList (Ws: weightMatrix_list):(real * real list list) list
    =
    let
    fun toRealList (rs): real list =
        case rs of
        rnil => []
            |consr(r, rs') => r::toRealList(rs')
    fun toRealListList (rls: real_list_list): real list list =
        case rls of
        rlnil => []
            |consr(rl, rls') => toRealList(rl)::toRealListList(rls')
    in
    case Ws of
        wnil => []
    | consw((nInputs, rls),Ws') =>
        (nInputs, toRealListList(rls)) :: toRealListListList(Ws')
    end
fun toWeightList (Ws: (real * real list list) list)
    : real Matrix.matrix option list =
    let
    fun initWeightMatrix(arg as (n, W):(real * real list list))
        : real Matrix.matrix option =
        let
        val nInputs = Real.floor (n)
        fun initSparseList ((ids, initializedWeights, nInputs, I):
```

<!-- page: 99 -->

```julia
(int list * real list * int * int))
    : real list =
        case (ids, I <= nInputs) of
        (_, false) => []
            |( [], true)  =>
    0.0::initSparseList (ids, initializedWeights, nInputs, I+1)
            |( idx::ids', true) =>
        if (idx = I) then
            hd(initializedWeights)
            ::initSparseList (ids',
                    tl(initializedWeights),
                    nInputs, I+1)
        else
            0.0::initSparseList (ids,
                initializedWeights,
                nInputs, I+1)
    fun initSparseVects (nInputs, vs) =
        case vs of
        [] => []
            |v::vs' => initSparseList(
                (Randomext.rand_perm (length(v), nInputs)),
                v, nInputs, 1)::
                (initSparseVects(nInputs, vs'))
        in
        SOME (Matrix.fromVectors2Cols(initSparseVects(nInputs, W),
                (nInputs, length(W))))
    end
in
case Ws of
    [] => []
    |W::Ws' => initWeightMatrix(W) :: toWeightList(Ws')
end
```

For more detail about the specification file, please refer to Appendix B

## 8.5 Experiment Results

A set of 5 training and 5 validation TinyDigits datasets were generated and used for this experiment. Each training dataset consists of 900 training examples, while validation datasets consist of 600 examples. We were using a small DNN (100 − 80 − 80 − 200 − 10), which takes only around 1 second for each epoch.

In our experiment, we were using tanh as the activation function and soft-max with negative log likelihood as the output unit and cost function. The network structure and the number of epochs are fixed. Marten’s sparse initialization was used as the starting point for ADATE. After several days of learning, ADATE had synthesized a completely new initialization scheme, which we call sparse-3. The original sparse initialization and the sparse-3 initialization code generated by ADATE are shown in Code 8.4.

```txt
Guinea --Original sparse initialization --//
fun f( NInputs, NOputs, LayerType ) : real_list =
let
    fun h( N : real ) : real_list =
        case 0.0 < N of
            false => rnil
```

<!-- page: 100 -->

![](images/page_99_chart_2.jpg)

Figure 8.4: Histogram of 10000 instances drawn from the tanh(tanh(randn(.))) distribution

```txt
| true => consr( randn(0.0, 1.0), h( N - 1.0 ) )
in
  h 15.0
end
//--------Sparse-3 function-------//
fun f( NInputs, NOputs, LayerType ) =
  consr(
    0.456463462775,
    consr( ~1.43515478736,
      consr( tanh( tanh( rand_normal( 0.0, 1.0 ) ) ), rnil )
    )
  )
```

Code 8.4: Original sparse and generated sparse-3 initialization functions. The f(.) function is used to generate a list of weights for a node. These weights are then randomly assigned to its incoming connections

## 8.5.1 Sparse-3 description

As shown in Code 8.4, ADATE has created a totally new initialization scheme where each node only has 3 non-zero incoming weights, Two of them are set to the two constants 0.456463462775 and −1.43515478736. The third value is drawn from a new distribution: tanh(tanh(randn(.))), in which randn(.) is the normal distribution with $\mu   =   0 , \sigma ^ { 2 }   =   1$ This distribution looks like an inverted bell curve, sometimes called “the well curve” which is bi-modal and usually appears in economic and social phenomena. A histogram of this new distribution is shown in figure 8.4.

At first sight, one could imagine that the sparse-3 method may be overfitted to the artificially generated TinyDigits datasets. Starting with very large weights at the beginning of neural network training could create configurations of weights, that might be useful on TinyDigits but unlikely to be useful on other datasets. Erhan et al., 2009 also suggested

<!-- page: 101 -->

that sampling from a fat-tailed distribution in order to initialize a deep architecture could actually hurt the performance of a deep architecture[7].

However, as we shall see shortly in the next section, the performance of sparse-3 method on the MNIST dataset is statistically equivalent <sup>2</sup>to sparse and normalized initialization, but converges much faster. Moreover, while other intialization methods need L2 regularization to overcome overfitting, sparse-3 does not need it. Without weight decay, sparse and normalized methods are outperformed by sparse-3 <sup>2</sup>.

## 8.5.2 Sparse-3 Testing

## Methodology

We experimented on MNIST, a well-known 28 x 28 handwritten digits images dataset composed of 60000 training examples and 10000 test examples. The original training set was further split into a 50000-examples training set and a 10000-examples validation set in our experiments.

For sparse and normalized initialization, the learning rate and $l _ { 2 }$ cost penalty hyperparameters are optimized, chosen from [0.05, 0.02, 0.01, 0.005] and $[ [ 1 0 ^ { - 4 } , 1 0 ^ { - 5 } , 1 0 ^ { - 6 } ] ]$ respectively. The sparse-3 initialization is tested without using $l _ { 2 }$ regularization <sup>3</sup>. We used the momentum schedule suggested by Ilya Sutskever et al. 2012 [46]. All experiments on MNIST used “mini-batches” with a batch cardinality of 200 training examples.

All other hyper-parameters are shown in table 8.4. Each initialization method was experimentally evaluated on network structures with different depths using 10 different random initialization seeds. For the purpose of comparison, we also tested the performance of sparse and normalized initialization on a 4-layer network without $l _ { 2 }$ regularization.

Table 8.4: Settings used for the experiments

| Hyper-parameters | Configuration |
| --- | --- |
| Dataset: | MNIST |
| 4 layers network: | [500 500 2000] |
| 5 layers network: | [2000 1500 1000 500] |
| 6 layers network: | [1500 2000 1500 1000 500] |
| Activation function: | tanh(.) |
| Cost function: | Negative log likelihood |
| MMoommeennttuumm smchaxed: ule: | µ = min(1 - 2-1-log<sub>2</sub>(bt/2µ5<sub>m</sub>0c<sub>a</sub>+<sub>x</sub>1)=,µ0<sub>m</sub>.9<sub>a</sub>9<sub>x</sub>9) |
| L2 weight decay: | [10<sup>-4</sup>,10<sup>-5</sup>,10<sup>-6</sup>] |
| Batch cardinality: | 200 |
| Learning rates: | [0.05, 0.02, 0.01, 0.005] |

## The Convergence Speed Advantage of Sparse-3

An obvious advantage when training sparse-3 initialized networks is that the networks converge much faster than for any other initialization method, at least twice as fast. The difference is even bigger as the networks become deeper. As you can see in Table 8.5, the

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>2</sup>under the null hypothesis test with p = 0.005</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3l2 regularization could hurt sparse-3 performance</span></small>

<!-- page: 102 -->

Table 8.5: Validation error rates after specific training epochs for different network depth Epochs

|  |  | 1 | 5 | 10 | 20 | 30 | 40 | 50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4-layers | Normalized Normalized* Sparse Sparse*Sparse-3 | 8.90%8.92%8.64%8.66%6.62% | 6.44%6.38%4.59%4.68%3.51% | 4.70%4.49%3.38%3.43%2.79% | 3.30%3.32%2.88%2.86%2.47% | 2.62%2.53%2.35%2.31%2.20% | 2.27%2.30%2.22%2.24%2.14% | 2.22%2.22%2.11%2.20%1.97% |
| 5-layers | Normalized SparseSparse-3 | 8.12%8.24%5.76% | 4.86%3.86%2.90% | 3.45%3.05%2.48% | 2.56%2.63%2.10% | 2.13%2.03%2.00% | 2.06%2.07%1.88% | 2.03%2.05%1.83% |
| 6-layers | Normalized SparseSparse-3 | 7.89%8.46%5.35% | 4.45%3.59%2.78% | 3.19%3.28%2.29% | 2.53%2.61%1.85% | 2.24%2.04%1.78% | 2.17%2.03%1.81% | 2.04%2.02%1.76% |

validation error rates of sparse-3 at the beginning of the training process are much lower than for the other initializations. Until 50 epochs, sparse-3 has a clear advantage over other methods. However, as the training process comes to around 100 epochs, sparse-3 is losing its dominance and let other method (with help from $l _ { 2 }$ regularization) catch up.

This can be explained as follows. After a few dozen epochs, the $l _ { 2 }$ regularization starts to make effect on the network generalization, which leads to better validation error rates. The $l _ { 2 } ,$ however, is not a suitable regularizer for sparse-3 and could hurt its performance.

## Sparse-3 Advantage Regarding Optimization and Generalization

The experimental results in Table 8.5 show the performance of sparse-3, sparse, and normalized initialization for different neural network architectures. It is obvious from the table that sparse-3 converges much faster. For example, sparse-3 reaches a validation error rate of 1.85% after only 20 epochs for a 6-layer architecture whereas the closest state-of-the-art competitor, sparse, only reaches 2.02% after 50 epochs.

Moreover, without help from l<sub>2</sub> regularization, sparse-3 significantly outperforms sparse and normalized initialization.

To better understand its advantage, we also compared the learning curves of these methods without using $l _ { 2 }$ regularization and at a fixed 0.05 learning rate. As we all know, the error surface of deep architectures is very non-convex and hard to optimize with many local minima. As can be seen in Figure 8.5, the sparse-3 learning curves for training as well as validation error are much smoother and converge faster than those for sparse\* and normalization\*. This suggests that sparse-3 initialization puts us in a region of parameter space where optimization is easier.

Note that adding a $l _ { 2 }$ regularization term to the training cost will make the optimization process become harder (i.e. longer) in return for better generalization. Therefore, training with sparse-3 initialized networks is indeed much faster and easier. Moreover, this advantage is also magnified when the network gets deeper. This property could be very useful in training very deep neural networks like autoencoders, where underfitting is a big trouble. In fact, the original sparse initialization method was invented by Martens (2010) to overcome exactly that problem.

<!-- page: 103 -->

Table 8.6: Average test error (10 initialization seeds) for best validation for different network structures

| Network | Standard | Normalized | Normalized* | Sparse | Sparse* | Sparse-3 |
| --- | --- | --- | --- | --- | --- | --- |
| $[500 - 500 - 2000]$ | $2.17\%^{1}$ | $1.74\%$ | 1.87 | $1.73\%$ | 1.84% | $1.73\%$ |
| $[2000 - 1500 - 1000 - 500]$ | $^{-2}$ | $1.64\%^{3}$ | - | 1.66% | - | 1.63% |
| $[1500 - 2000 - 1500 - 1000 - 500]$ | - | 1.68% | - | 1.62% | - | 1.60% |

\* : l<sub>2</sub> regularization was not used.

- : results are not relevant.

1: produced by Erhan et.al. 2009 [7]. Network structure was also optimized.

2: Erhan et.al. 2009 stated that they were unable to effectively train 5-layer models using standard initialization. While X. Glorot and Y. Bengio (2010) produced 1.76% error rates.

3: produced by X. Glorot and Y. Bengio (2010) [9]. The network structure is unknown. Our experiments showed slightly worse results.

Figure 8.6 also shows that without $l _ { 2 }$ regularization, sparse-3 yields better generalization (validation errors) than other methods. Table 8.5 also confirms this point, at least during the first 50 epochs. Combining Figure 8.5 and Figure 8.6, we can see that at the same training cost level, sparse-3 yields a lower test cost. In this sense, sparse-3 appears to bring an effect to that of a regularizer, probably due to its sparsity. This could also explain why sparse-3 does not need $l _ { 2 }$ regularization.

## Sparse-3 Opimization

When looking at the sparse-3 initialization, one would probably ask if the two constants in sparse-3 already are optimal. After conducting a small gridsearch on the MNIST dataset with a 4-layer neural network, we concluded that these constants already are relatively optimal, despite being optimized for the TinyDigits dataset. Thus, the constants do not need to be changed when going from TinyDigits to MNIST even if the neural networks for the latter are about two orders of magnitude bigger.

Table 8.7: Gridsearch for the two constants in sparse-3

<table><tr><td>Variations</td><td colspan="5">-1.43515478736</td></tr><tr><td>0.456463462775</td><td>-0.2</td><td>-0.1</td><td>0.0</td><td>0.1</td><td>0.2</td></tr><tr><td>-0.06</td><td>1.88%</td><td>1.85%</td><td>1.87%</td><td>1.64%</td><td>1.69%</td></tr><tr><td>-0.03</td><td>1.98%</td><td>1.75%</td><td>1.90%</td><td>1.82%</td><td>1.75%</td></tr><tr><td>0.00</td><td>1.89%</td><td>1.76%</td><td>1.68%</td><td>1.72%</td><td>1.82%</td></tr><tr><td>0.03</td><td>1.78%</td><td>1.98%</td><td>1.77%</td><td>1.84%</td><td>1.76%</td></tr><tr><td>0.06</td><td>1.88%</td><td>2.01%</td><td>1.81%</td><td>1.88%</td><td>1.72%</td></tr></table>

## 8.6 Overfitting Problem

Sparse-3 initialization was invented by ADATE after a relatively short run. After sparse-3, we have tried to run ADATE for much longer time. Although new generated programs perform very well on TinyDigits dataset, they are almost useless when applied on MNIST. We attempted to solve this problem using different solutions. However, we did not know exactly what the main cause of overfitting was. We had tried to increase the number of tinyDigits training datasets, make the validation sets bigger, and increase the number of epochs... However, they turned out to be a very wrong way.

<!-- page: 104 -->

![](images/page_103_chart_2.jpg)

(a) b

sparse3Figure 8.5: Learning curves for negative log likelihood training cost

![](images/page_103_chart_5.jpg)

(a) b

Figure 8.6: Learning curves on negative log likelihood validation cost

Figure 8.7: Learning curves of sparse3, sparse\*, and normalized\* tested on 4-layer neural networks using a 0.05 learning rate. Each method was applied for 10 different initialization seeds.

After that, we decided to make a more systematic experiment on checking what the real overfitting source is. The followings were suspected: architecture, batch size, learning rate, weight decay, momentum, and datasets. In our first experiment, the first five suspected factors were tested. We tested the best ADATE-generated program at that time on the TinyDigits and compare the result to the sparse initialization. We changed these factors’ value at each run to see if the ADATE-generated program ovefits to the settings that used during its training process.

As shown in figure 8.8, the ADATE-generated program does not overfit to any of the above factors. Therefore, we conducted a new experiment to check if it overfits to the tinyDigits datasets. Note that we can check this using the original MNIST dataset directly. However, training neural network on MNIST takes a lot of time, including optimizing many hyper-parameters, waiting for many epochs, and training network for at least five times to assure the result. Besides, MNIST contains 28x28 images, which is different from tinyDigits. Therefore, we have to change the network structure and some other hyperparameters to be able to train on MNIST. This makes it impossible to know where the

<!-- page: 105 -->

overfitting comes from: the difference in datasets or the difference in hyper-parameters. Therefore, we used the tinyUSPS and compressedMNIST dataset in this experiment.

The figure 8.9 shows that the datasets are obviously the main source of overfitting, where the ADATE-generated program outperform the sparse initialization on tinyDigits dataset, but being much worse on the other tiny datasets. This suggests that we should mix the TinyDigits dataset with the TinyUSPS or compressedMNIST100 to make ADATE harder to overfit to the training dataset.

<table><tr><td colspan="3">Architecture</td><td colspan="3">Batch size</td></tr><tr><td>Options</td><td>ADATE</td><td>Sparse</td><td>Options</td><td>ADATE</td><td>Sparse</td></tr><tr><td>80 80 200</td><td>3.20%</td><td>4.27%</td><td>10</td><td>3.20%</td><td>4.33%</td></tr><tr><td>80 80 80</td><td>2.60%</td><td>4.27%</td><td>5</td><td>2.53%</td><td>3.40%</td></tr><tr><td>100 100 100</td><td>3%</td><td>3.67%</td><td>15</td><td>3.27%</td><td>4.27%</td></tr><tr><td>100 100 200</td><td>4.47%</td><td>4.27%</td><td>20</td><td>3.33%</td><td>4%</td></tr><tr><td>100 200 200</td><td>2.87%</td><td>3.27%</td><td>25</td><td>3.53%</td><td>4.13%</td></tr><tr><td>200 200 200</td><td>2.67%</td><td>4%</td><td>30</td><td>3.67%</td><td>4.53%</td></tr><tr><td colspan="3">Learning Rate</td><td colspan="3">Momentum</td></tr><tr><td>Options</td><td>ADATE</td><td>Sparse</td><td>Options</td><td>ADATE</td><td>Sparse</td></tr><tr><td>0.05</td><td>3.20%</td><td>4.20%</td><td>0.99</td><td>3.20%</td><td>4.53%</td></tr><tr><td>0.025</td><td>3.33%</td><td>3.73%</td><td>0.95</td><td>3.20%</td><td>4.60%</td></tr><tr><td>0.01</td><td>4.20%</td><td>4.73%</td><td>0.9</td><td>3.20%</td><td>3.73%</td></tr><tr><td>0.075</td><td>2.80%</td><td>4.07%</td><td>0</td><td>3.53%</td><td>3.80%</td></tr><tr><td>0.1</td><td>2.53%</td><td>3.53%</td><td></td><td></td><td></td></tr><tr><td colspan="3">Weight Decay</td><td rowspan="5" colspan="3"></td></tr><tr><td>Options</td><td>ADATE</td><td>Sparse</td></tr><tr><td>10^-5</td><td>3.20%</td><td>4.07%</td></tr><tr><td>10^-4</td><td>3.20%</td><td>3.73%</td></tr><tr><td>0</td><td>3.20%</td><td>4.53%</td></tr></table>

Figure 8.8: Experiment on testing overfitting sources: Architecture, Batchsize, Learning Rate, Momentum and Weight Decay. The first value for each factor was the value that used during the ADATE training process

<table><tr><td rowspan="2">Random Seeds</td><td colspan="3">TinyDigits</td><td colspan="3">TinyUSPS</td><td colspan="3">CompressedMnist100</td></tr><tr><td>ADATE</td><td>Sparse3</td><td>Sparse</td><td>ADATE</td><td>Sparse3</td><td>Sparse</td><td>ADATE</td><td>Sparse3</td><td>Sparse</td></tr><tr><td>1</td><td>3.20%</td><td>3.00%</td><td>3.67%</td><td>4.78%</td><td>4.55%</td><td>4.62%</td><td>3.12%</td><td>2.87%</td><td>2.77%</td></tr><tr><td>2</td><td>2.67%</td><td>3.80%</td><td>4.00%</td><td>4.55%</td><td>4.16%</td><td>4.16%</td><td>2.75%</td><td>2.58%</td><td>2.71%</td></tr><tr><td>3</td><td>3.27%</td><td>4.20%</td><td>3.93%</td><td>4.93%</td><td>4.31%</td><td>4.24%</td><td>2.98%</td><td>2.91%</td><td>2.75%</td></tr><tr><td>4</td><td>3.80%</td><td>3.33%</td><td>3.60%</td><td>4.08%</td><td>4.70%</td><td>3.85%</td><td>3.21%</td><td>2.66%</td><td>2.61%</td></tr><tr><td>5</td><td>2.40%</td><td>4.13%</td><td>4.07%</td><td>4.78%</td><td>4.55%</td><td>4.24%</td><td>3.03%</td><td>2.84%</td><td>2.37%</td></tr><tr><td>Mean</td><td>3.07%</td><td>3.69%</td><td>3.85%</td><td>4.62%</td><td>4.45%</td><td>4.22%</td><td>3.02%</td><td>2.77%</td><td>2.64%</td></tr><tr><td>Architecture</td><td colspan="3">80 - 80 - 200</td><td colspan="3">80 - 80 - 200</td><td colspan="3">80 - 80 - 200</td></tr><tr><td>Batchsize</td><td colspan="3">10</td><td colspan="3">10</td><td colspan="3">200</td></tr><tr><td>MaxEpochs</td><td colspan="3">100</td><td colspan="3">100</td><td colspan="3">100</td></tr></table>

Figure 8.9: Experiment on testing overfitting on datasets

<!-- page: 106 -->

<!-- page: 107 -->

## Chapter 9

# Conclusion and Future Works

This thesis aims at two main purposes: introducing deep learning and its state-of-the-art algorithms, and conducting ADATE experiments to improve deep learning.

Chapter 3 to 6 fulfil the first purpose by giving a short introduction to deep learning and summarizing many recent important discoveries which lead to the deep learning’s flourishing such as: unsupervised pre-training strategy or different types of new optimization, regularization methods, and activation functions designed particularly for deep learning. This knowledge is extremely useful for conducting ADATE experiments, especially for deciding which part of deep learning we could improve.

Chapter 8 fulfils the second purpose and answers the research question posed at the beginning of the thesis: “How can the ADATE system improve the performance of deep learning?”. The question is answered in a process where we have succesfully designed several different tiny datasets for ADATE, implemented a neural networks library in SML language, and synthesized a brand new sparse-3 initialization scheme. Despite its simplicity, our experiment results have proved the advantage of sparse-3 on classification task over other existing initialization methods. The sparse-3 can double the convergence speed of deep learning. This might suggest that deep learning is still a new subject with many aspects we still do not deeply understand. Therefore, automatic programming can help us overcome our subjective judgments, break our belief, and come up with strange but effective algorithms. This is only our first try on using ADATE to improve deep learning algorithms, and there are many other potential possibilities, such as activation function, objective function, regularization term, learning rate schedule, or momentum formula...

After the discovery of sparse-3, we also conducted other experiments but the results were not as good. We did an analysis for this and recognized the dataset overfitting problem when using the tinyDigits dataset. Other tiny datasets have been built to assess the overfitting. However, because of the time limitation, we could not complete further experiments with these new datasets for this thesis. Besides, the limitation of the ADATE current version that we cannot call the synthesized program from outside of the ADATE part makes it hard to experiment with other parts of deep learning. We expect that based on deep learning knowledge and the neural networks library provided in this thesis, other researchers who find it interesting can conduct future experiments easily, especially when the next version of ADATE is available.

<!-- page: 108 -->

## 9.1 Future Works

For future experiments, we suggest these following development directions

Improve Neural Network library performance: If we can make the SML neural network library run faster, we could open up new possibilities. We can train ADATE with bigger datasets or deeper neural networks in a shorter time. We could even train ADATE on real-world dataset, which can help it overcome the overfitting problem on generated datasets. One improvement that we can do first is instead of using the SML matrix library, we could use the BLAS (Basic Linear Algebra Subprograms) library. BLAS is a high-performance low-level linear algebra library which supports basic linear algebra operations such as copying, vector dot products, linear combinations, and matrix multiplication. There are several BLAS implementations that optimized for specific architectures (e.g. Intel, AMD, ARM...). It is used as a building-block in almost any high-performance scientific computing languages such as MATLAB, R, or Numpy. Using BLAS implementation could speed up matrix multiplication operation, which is used heavily in neural network, 10x-100x faster than using normal loop implementation (depends on CPU architectures and size of the matrices). Currently, we intend to use OpenBLAS, a BLAS implementation that is optimized for different Intel and AMD architectures. To achieve best performance, we suggest compiling the OpenBLAS library to dynamic library (e.g. \*.dll or \*.so files) for each computer in the cluster to get it optimized for different architectures.

• Overfitting problem: The most serious problem that we have to deal with when using ADATE to improve deep learning is the overfitting. We suggest two main approaches, which could possibly help overcome this problem. First, we can improve the quality of the training datasets. By improving performance of neural network library, we can train with bigger datasets, or even with real-world datasets, which could reduce the overfitting. We could also use some kinds of autoencoders to create compressed version of high-dimensionality input. The second approach for this problem is that we can make the overfitting happen as what we want. We can prove that by using ADATE, we can tune a part of deep learning to be optimized for a specific task in an acceptable time.

• State of the art Algorithms: Despite being a very new research area, the deep learning literature is developing at extreme speed and dominating all other methods in machine learning, especially for high-level abstraction tasks. Supported by an expanding and very active research community, there are new deep learning algorithms and technologies introduced every year. Therefore, to maximize the ability of ADATE on improving deep learning, we need to keep up with new technologies in deep learning. The best way to do this is to use a standard deep learning library, which is updated frequently with all new central methods. We suggest Pylearn2 for this purpose. It is a machine learning library written in Python and developed by the well-known LISA lab (University of Montreal). It consists of many state-of-the-art deep learning algorithms, and supported by one of the most active deep learning research lab.

<!-- page: 109 -->

## Bibliography

[1] Yoshua Bengio. Learning deep architectures for ai. Foundations and trends R in Machine Learning, 2(1):1–127, 2009.

[2] Yoshua Bengio and Olivier Delalleau. Justifying and generalizing contrastive divergence. Neural Computation, 21(6):1601–1621, 2009.

[3] Yoshua Bengio and Pascal Lamblin. Greedy layer-wise training of deep networks. Advances in neural . . . , (1), 2007.

[4] James Bergstra, Guillaume Desjardins, Pascal Lamblin, and Yoshua Bengio. Quadratic polynomials learn better image features. Technical report, Technical Report 1337, Departement d’Informatique et de Recherche Operationnelle, Universite de Montreal, 2009.

[5] Dan Claudiu Ciresan, Ueli Meier, Luca Maria Gambardella, and Juergen Schmidhuber. Deep big simple neural nets excel on handwritten digit recognition. arXiv preprint arXiv:1003.0358, 2010.

[6] BB Le Cun and JS Denker. Handwritten digit recognition with a back-propagation network. Advances in neural . . . , 1990.

[7] Dumitru Erhan, Pierre-Antoine Manzagol, Yoshua Bengio, Samy Bengio, and Pascal Vincent. The difficulty of training deep architectures and the effect of unsupervised pre-training. In International Conference on Artificial Intelligence and Statistics, pages 153–160, 2009.

[8] SE Fahlman and C Lebiere. The cascade-correlation learning architecture. 1989.

[9] X Glorot and Y Bengio. Understanding the difficulty of training deep feedforward neural networks. International Conference on . . . , pages 1–8, 2010.

[10] Xavier Glorot, Antoine Bordes, and Yoshua Bengio. Deep sparse rectifier networks. 15:315–323, 2011.

[11] Ian J Goodfellow, David Warde-Farley, Mehdi Mirza, Aaron Courville, and Yoshua Bengio. Maxout networks. arXiv preprint arXiv:1302.4389, 2013.

[12] Alex Graves, Marcus Liwicki, Santiago Fernández, Roman Bertolami, Horst Bunke, and Jürgen Schmidhuber. A novel connectionist system for unconstrained handwriting recognition. IEEE transactions on pattern analysis and machine intelligence, 31(5):855–68, May 2009.

<!-- page: 110 -->

[13] Stig-Erland Hansen and Roland Olsson. Improving decision tree pruning through automatic programming. pages 31–40, 2007.

[14] Simon Haykin. Neural Networks and Learning Machines. Pearson International Edition, 3rd edition, 2009.

[15] Hinton. Neural Networks for Machine Learning course, 2013.

[16] G E Hinton and R R Salakhutdinov. Reducing the dimensionality of data with neural networks. Science (New York, N.Y.), 313(5786):504–7, July 2006.

[17] Geoffrey Hinton, Li Deng, Dong Yu, George Dahl, Abdel-rahman Mohamed, Navdeep Jaitly, Vincent Vanhoucke, Patrick Nguyen, Tara Sainath, and Brian Kingsbury. Deep Neural Networks for Acoustic Modeling in Speech Recognition. pages 1–27, 2012.

[18] Geoffrey E Hinton, Simon Osindero, and Yee-Whye Teh. A fast learning algorithm for deep belief nets. Neural computation, 18(7):1527–1554, 2006.

[19] Geoffrey E Hinton, Nitish Srivastava, Alex Krizhevsky, Ilya Sutskever, and Ruslan R Salakhutdinov. Improving neural networks by preventing co-adaptation of feature detectors. arXiv preprint arXiv:1207.0580, 2012.

[20] Sugihara Hiroshi. What is Occam’s Razor? 1996.

[21] Morgan Jakobsen and Roland Olsson. Generation of a four-way item-to-item navigation algorithm using automatic programming. pages 1310–1315, 2006.

[22] A Krizhevsky. Convolutional deep belief networks on cifar-10. Unpublished manuscript, pages 1–9, 2010.

[23] Alex Krizhevsky, Ilya Sutskever, and Geoff Hinton. Imagenet classification with deep convolutional neural networks. pages 1106–1114, 2012.

[24] Y LeCun and Y Bengio. Convolutional networks for images, speech, and time series.. . . handbook of brain theory and neural networks, pages 1–14, 1995.

[25] Yann LeCun, Léon Bottou, Genevieve B Orr, and Klaus-Robert Müller. Efficient backprop. In Neural networks: Tricks of the trade, pages 9–50. Springer, 1998.

[26] James Martens. Deep learning via hessian-free optimization. pages 735–742, 2010.

[27] Tom M Mitchell. Machine Learning. McGraw Hill, 1997.

[28] Andrew Ng. Cs294a lecture notes: Sparse autoencoder, 2010.

[29] Andrew Ng. Deep learning, self-taught learning and unsupervised feature learning, 2012.

[30] Andrew Ng. Machine Learning course, 2012.

[31] J. R. Olsson. The ADATE System homepage, 1994.

[32] J Roland Olsson. The art of writing specifications for the adate automatic programming system. In Proceedings of the 3rd Annual Conference on Genetic Programmin, pages 278–283. Citeseer, 1998.

<!-- page: 111 -->

[33] Roland Olsson. Inductive functional programming using incremental program transformation; and, Execution of logic programs by iterative-deepening A\* SLD-tree search. PhD thesis, University of Oslo, Department of Informatics, 1994.

[34] Roland Olsson. Inductive functional programming using incremental program transformation. Artificial intelligence, 74(1):55–81, 1995.

[35] Roland Olsson. Inductive functional programming using incremental program transformation. Artificial Intelligence, 74(1):55–81, 1995.

[36] Roland Olsson and Arne Løkketangen. Using automatic programming to generate state-of-the-art algorithms for random 3-sat. Journal of Heuristics, 19(5):819–844, 2013.

[37] Jin-Song Pei, Eric C Mai, and Joseph P Wright. Mapping some functions and four arithmetic operations to multilayer feedforward neural networks. pages 693512–693512, 2008.

[38] Martin Riedmiller and I Rprop. Rprop-description and implementation details. (January), 1994.

[39] Salah Rifai, Pascal Vincent, Xavier Muller, Xavier Glorot, and Yoshua Bengio. Contractive auto-encoders: Explicit invariance during feature extraction. pages 833–840, 2011.

[40] Ruslan Salakhutdinov and Geoffrey Hinton. Deep boltzmann machines. International. . . , (3):448–455, 2009.

[41] Ruslan Salakhutdinov and Geoffrey Hinton. An efficient learning procedure for deep Boltzmann machines. Neural Computation, 2012.

[42] Thomas Serre, Gabriel Kreiman, Minjoon Kouh, Charles Cadieu, Ulf Knoblich, and Tomaso Poggio. A quantitative theory of immediate visual recognition. Progress in brain research, 165(06):33–56, January 2007.

[43] Zhen-Jun Shi. Convergence of line search methods for unconstrained optimization. Applied Mathematics and Computation, 157(2):393–405, October 2004.

[44] Patrice Y Simard, Dave Steinkraus, and John C Platt. Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis. (Icdar):1–6, 2003.

[45] I Sutskever. Training Recurrent Neural Networks. 2013.

[46] Ilya Sutskever, James Martens, George Dahl, and Geoffrey Hinton. On the importance of initialization and momentum in deep learning. cs.utoronto.ca, (2010), 2012.

[47] Geir Vattekar. Adate user manual. Technical report, Technical report, Ostfold University College, 2006.

[48] Pascal Vincent, Hugo Larochelle, Yoshua Bengio, and Pierre-Antoine Manzagol. Extracting and composing robust features with denoising autoencoders. pages 1096–1103, 2008.

<!-- page: 112 -->

[49] Carl von Linné and Johann Joachim Lange. Systema Naturae: Per Regna Tria Naturae, Secundum Classes, Ordines, Genera, Species, Cum Characteribus, Differentiis, Synonymis, Locis, volume 3. Curt, 1770.

[50] L Wan and Matthew Zeiler. Regularization of Neural Networks using DropConnect. Proceedings of the . . . , (1), 2013.

[51] Ian H. Witten, Eibe Frank, and Mark A. Hall. Data Mining - Practical Machine Learning Tools and Techniques. Elsevier Inc., 3rd edition, 2011.

<!-- page: 113 -->

# Neural Network Libraries

## A.1 Matrix Library

A.1.1 Matrix Signature

```ocaml
(*
  File: matrix.sml
  Content: matrix library using List of List type
  Author: Dang Ha The Hien, Hiof, hdthe@hiof.no
  Convention for variable names:
    matrix:          m, m1, m2 ...
    vector:          v, v1, v2 ...
    list of vectors: vs, v1s, v2s ...

*)
signature MATRIX =
sig
  type 'a vector = 'a list
  type 'a matrix
  exception WrongMatrixMode
  exception UnmatchedDimension
  (* basic functions for datatype matrix *)
  val changeType:   'a matrix -> 'a matrix
  val checkValid:   'a matrix -> bool
  val transpose:   'a matrix -> 'a matrix
  val transpose_changeType: 'a matrix -> 'a matrix
  val toVector:      'a matrix -> 'a list
  val size:        'a matrix -> int * int
  (* functions to create new matrix *)
  val initCols:     'a * (int * int) -> 'a matrix
  val initRows:     'a * (int * int) -> 'a matrix
  val uniRandRows: Random.rand -> real * (int * int) -> real matrix
  val uniRandCols: Random.rand -> real * (int * int) -> real matrix
  val fromVector2Cols: 'a list * (int * int) -> 'a matrix
  val fromVector2Rows: 'a list * (int * int) -> 'a matrix
  val fromVectors2Cols: 'a list list * (int * int) -> 'a matrix
  val fromVectors2Rows: 'a list list * (int * int) -> 'a matrix
  (* functions for debugging *)
  val printMatrixReal: real matrix -> unit
  val printMatrixInt: int matrix -> unit
  (* functions for output *)
  val printfMatrixReal: string * real matrix -> unit
```

<!-- page: 114 -->

```ocaml
val printfMatrixInt: string * int matrix -> unit
(* supported operators on vector *)
val mergeVector: (('a*'a)->'b) -> ('a vector * 'a vector) -> 'b vector
val mergeVect2Matrix: (('a * 'a) -> 'b) -> ('a vector * 'a matrix)
                                      -> 'b matrix
val mergeVect'2Matrix: (('a * 'a) -> 'b) -> ('a vector * 'a matrix)
                                      -> 'b matrix
val addVect2MatrixReal: real list * real matrix -> real matrix
val addVect2MatrixInt: int list * int matrix -> int matrix
(* supported operators on matrix *)
(* scalar operator *)
val map:            ('a -> 'b) -> 'a matrix -> 'b matrix
val addScalarInt:     int matrix * int -> int matrix
val mulScalarInt:     int matrix * int -> int matrix
val addScalarReal:    real matrix * real -> real matrix
val mulScalarReal:    real matrix * real -> real matrix
(* accumulate operator *)
val foldl:          (('a*'b) -> 'b) -> 'b -> ('a matrix) -> 'b vector
val sumInt:             (int matrix) -> int vector
val sumReal:           (real matrix) -> real vector
(* matrix operator *)
val merge:            (('a*'b)->'c) -> ('a matrix * 'b matrix)
                                      -> 'c matrix
val dotMulMatrixInt:   int matrix * int matrix -> int matrix
val dotMulMatrixReal:  real matrix * real matrix -> real matrix
val addMatrixInt:   int matrix * int matrix -> int matrix
val addMatrixReal:  real matrix * real matrix -> real matrix
(* real multiply operation *)
val mulMatrixIntR:      int matrix * int matrix -> int matrix
val mulMatrixIntC:      int matrix * int matrix -> int matrix
val mulMatrixRealR:      real matrix * real matrix -> real matrix
val mulMatrixRealC:      real matrix * real matrix -> real matrix
end
```

## A.1.2 Matrix Structure

```txt
structure Matrix :> MATRIX =
struct
  type 'a vector = 'a list
  datatype 'a matrix = COLMATRIX of ('a vector list * int * int)
              | ROWMATRIX of ('a vector list * int * int)
  exception WrongMatrixType
  exception UnmatchedDimension
    fun changeVectors vs =
  let
    fun getHeads vs =
      case vs of
        []       => ([], [])
        | v::vs' => case v of
          [] => ([], [])
          | hdv::tlv =>
            case getHeads(vs') of
                (hdvs, tlvs) => (hdv::hdvs, tlv::tlvs)
  in
    case getHeads(vs) of
      ([], _)       => []
      | (hdvs, tlvs) => hdvs::changeVectors(tlvs)
```

<!-- page: 115 -->

```txt
end
fun changeType (COLMATRIX(vs, rows, cols)) =
    ROWMATRIX(changeVectors(vs), rows, cols)
  | changeType (ROWMATRIX(vs, rows, cols)) =
    COLMATRIX(changeVectors(vs), rows, cols)
fun transpose m =
case m of
    COLMATRIX (vs, rows, cols) => changeType(ROWMATRIX (vs, cols, rows))
  | ROWMATRIX (vs, rows, cols) => changeType(COLMATRIX (vs, cols, rows))

fun transpose_changeType m =
case m of
    COLMATRIX (vs, rows, cols) => ROWMATRIX (vs, cols, rows)
  | ROWMATRIX (vs, rows, cols) => COLMATRIX (vs, cols, rows)
  fun fromVectors2List [] = []
  | fromVectors2List (v::vs) = v @ fromVectors2List(vs)

fun toVector m =
case m of
    ROWMATRIX (vs, rows, cols) => fromVectors2List (vs)
  |COLMATRIX (vs, rows, cols) => fromVectors2List (changeVectors(vs))

fun sizeVectors vs =
let
    val nElems = List.foldl (fn (v, lengthv) =>
        case (lengthv, (List.length(v) = lengthv)) of
            (0, _)      => List.length(v)
            | (_, true) => List.length(v)
            | (_, false) => ~1)
            0 vs
    val nVectors = List.length(vs)
in
    (nElems, nVectors)
end

fun checkValid (COLMATRIX(vs, rows, cols)) =
let val (nElems, nVectors) = sizeVectors(vs)
in
  if (nElems = rows) andalso (nVectors = cols) then true else false
end
| checkValid (ROWMATRIX(vs, rows, cols)) =
let val (nElems, nVectors) = sizeVectors(vs)
in if (nElems = cols) andalso (nVectors = rows)then true else false
end

fun initVector (value, n, acc) =
case n of
  0 => acc
| n => initVector(value, n-1, value::acc)
fun initVectors (value, rows, cols) =
let
  fun reduce(cols, acc) =
    case cols of
      0 => acc
    | cols => reduce(cols -1,
          initVector(value, rows, [])::acc)
in
    reduce(cols, [])
```

<!-- page: 116 -->

```txt
end
fun initCols (value, (rows, cols)) = COLMATRIX (initVectors(value, rows,
cols),
                    rows, cols)
fun initRows (value, (rows, cols)) = transpose_changeType (initCols(
value,
                    (cols, rows)))

fun uniRandVectors RandState (nVectors, length, max) =
let
  fun uniRandList(n) =
    if n = 0 then []
    else (max*(2.0*(Random.randReal RandState)-1.0)):: uniRandList(n-1)
    fun uniRandVectors(nVectors) =
    if nVectors = 0 then []
    else uniRandList(length):: uniRandVectors(nVectors-1)
in
  uniRandVectors(nVectors)
end

fun uniRandRows RandState (max, (rows, cols)) =
  ROWMATRIX(uniRandVectors RandState (rows, cols, max), rows, cols)
fun uniRandCols RandState (max, (rows, cols)) =
  COLMATRIX(uniRandVectors RandState (cols, rows, max), rows, cols)

fun printInfo m =
case m of
    COLMATRIX (_, rows, cols) =>
      print("Collum matrix "^Int.toString(rows)^^" * "
          ^Int.toString(cols)^"\n")
    | ROWMATRIX (_, rows, cols) =>
      print("Row matrix "^Int.toString(rows)^^" * "
          ^Int.toString(cols)^"\n")
fun printMatrix printElem printEnd m =
let
  fun printVector v =
    case v of
      [] => ()
    | last::[] => printEnd last
    | head::v' => (printElem head; printVector v')
in
    case m of
      ROWMATRIX (vs, rows, cols) =>
        (printInfo m; List.app printVector vs)
        | COLMATRIX (vs, rows, cols) =>
        (printInfo m; List.app printVector (changeVectors vs))
end

fun real2str x =
    if x >= 0.0 then Real.toString(x)
    else "-" ^ Real.toString(~x)
fun int2str x =
    if x >= 0 then Int.toString(x)
    else "-" ^ Int.toString(~x)

val printMatrixReal = printMatrix (fn a => print (real2str(a)^", "))
                     (fn a => print (real2str(a) ^"\n"))
val printMatrixInt = printMatrix (fn a => print (int2str(a)^ ", "))
```

<!-- page: 117 -->

```csv
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
```

<!-- page: 118 -->

```txt
| map f (ROWMATRIX(vs, rows, cols)) = ROWMATRIX (mapVectors f vs, rows,
cols)

fun addScalarInt (m, x:int) = map (fn a => a+x) m
fun addScalarReal (m, x:real) = map (fn a => a+x) m
fun mulScalarInt (m, x:int) = map (fn a => a*x) m
fun mulScalarReal (m, x:real) = map (fn a => a*x) m

fun mergeVector f (v1, v2) =
    case (v1, v2) of
        ([], [])=[]
        | (hdv1::v1', hdv2::v2') => f(hdv1, hdv2)::(mergeVector f (v1', v2'))
        | _ => raise UnmatchedDimension

fun mergeVectors f vs1 vs2 = mergeVector (fn (v1, v2) =>
            mergeVector f (v1, v2)) (vs1, vs2)

fun merge f (m1, m2) =
    case (m1, m2) of
        (COLMATRIX (vs1, rows1, cols1), COLMATRIX(vs2, rows2, cols2)) =>
            COLMATRIX(mergeVectors f vs1 vs2, rows1, cols1)
        | (ROWMATRIX(vs1, rows1, cols1), ROWMATRIX(vs2, rows2, cols2)) =>
            ROWMATRIX(mergeVectors f vs1 vs2, rows1, cols1)
        | _ => raise WrongMatrixType

val dotMulMatrixInt = merge (fn (a:int, b)=>a*b)
val dotMulMatrixReal = merge (fn (a:real, b)=>a*b)
val addMatrixInt     = merge (fn (a:int, b)=>a+b)
val addMatrixReal    = merge (fn (a:real, b)=>a+b)

fun mergeVect2Vects f (v1, v2s) =
case v2s of
    [] => []
    | v2::v2s' => (mergeVector f (v1, v2))::(mergeVect2Vects f (v1, v2s'))

fun mergeVect2Matrix f (vx, m) =
case m of
    COLMATRIX(vs, rows, cols) => COLMATRIX(mergeVect2Vects f (vx, vs),
rows, cols)
    | ROWMATRIX(vs, rows, cols) => ROWMATRIX(mergeVect2Vects f (vx, vs),
rows, cols)
val addVect2MatrixReal = mergeVect2Matrix (fn (v1:real, v2)=> v1+v2)
val addVect2MatrixInt   = mergeVect2Matrix (fn (v1:int, v2)=> v1+v2)

fun mergeVect'2 Vects f (v1, v2s) =
let
    fun curf a b = f (a, b)
in
    case (v1, v2s) of
        ([], []) => []
        | (x::v1', v2::v2s') => (List.map (curf x) v2) :: (mergeVect'2Vects
f (v1', v2s'))
        | _ => raise UnmatchedDimension
end

fun mergeVect'2 Matrix f (vx, m) =
case m of
```

<!-- page: 119 -->

```fortran
COLMATRIX(vs, rows, cols) => COLMATRIX(mergeVect'2Vects f (vx, vs),
rows, cols)
| ROWMATRIX(vs, rows, cols) => ROWMATRIX(mergeVect'2Vects f (vx, vs),
rows, cols)

fun fold1 f acc m =
let fun fold1Vectors(vs) =
    case vs of
        []      => []
        | v::vs' => (List.fold1 f acc v)::fold1Vectors(vs')
in
    case m of
    COLMATRIX(vs, rows, cols) => fold1Vectors(vs)
    | ROWMATRIX(vs, rows, cols) => fold1Vectors(vs)
end
val sumInt = fold1 (fn (x, acc:int) => acc+x) 0
val sumReal = fold1 (fn (x, acc:real) => acc+x) 0.0

fun fold12Vectors f acc (v1, v2) =
let fun fold1(v1, v2, acc) =
    case (v1, v2) of
        (hdv1::v1', hdv2::v2') => fold1(v1', v2', f(hdv1, hdv2, acc))
        | ([], [])          => acc
        | -              => raise UnmatchedDimension
    in
        fold1(v1, v2, acc)
end

fun mulVectors mul2VectorsFun (v1s, v2s) =
let
    fun mulVectorsVector (v1s, v2) =
    case v1s of
        []      => []
        | v1::v1s' => (mul2VectorsFun(v1, v2))::
            (mulVectorsVector (v1s',v2))
    in
        case v2s of
        []      => []
        | v2::v2s' => (mulVectorsVector (v1s, v2))::(mulVectors
mul2VectorsFun (v1s, v2s'))
end
val mul2VectorsInt   = fold12Vectors (fn (x, y, acc:int) => acc+x*y) 0
val mul2VectorsReal   = fold12Vectors (fn (x, y, acc:real) => acc+x*y) 0.0
val mulVectorsInt = mulVectors mul2VectorsInt
val mulVectorsReal = mulVectors mul2VectorsReal

fun mulMatrix mulVectorsFun returnRow ((ROWMATRIX (vs1, rows1, cols1)),
                      (COLMATRIX (vs2, rows2, cols2))) =
if cols1 <> rows2
then raise UnmatchedDimension
else if returnRow then
    (ROWMATRIX (mulVectorsFun(vs2, vs1), rows1, cols2))
else
    (COLMATRIX (mulVectorsFun(vs1, vs2), rows1, cols2))
    | mulMatrix mulVectorsFun returnRow (-, _) = raise Wrong matéria
val mulMatrixIntC = mulMatrix mulVectorsInt false
val mulMatrixIntR = mulMatrix mulVectorsInt true
val mulMatrixRealC = mulMatrix mulVectorsReal false
```

<!-- page: 120 -->

```txt
val mulMatrixRealR = mulMatrix mulVectorsReal true
end
```

## A.2 Random library

## A.2.1 Random Signature

```ocaml
signature RANDOMEXT =
sig
    val rand_normal: Random.rand -> real * real -> real
    val rand_perm:   Random.rand -> int * int -> int list
end
```

## A.2.2 Random Structure

```ocaml
val cached_rand_normal = ref 0.0;
val rand_use_last = ref false;
fun rand_normal RandState (mean, std) =
    let
        fun box_muller () =
            let
                val x1 = 2.0 * (Random.randReal RandState) - 1.0
                val x2 = 2.0 * (Random.randReal RandState) - 1.0
                val w = x1 * x1 + x2 * x2
            in
                if (w < 1.0) then
                    let
                        val v = Math.sqrt((~2.0 * Math.ln(w)) / w)
                    in
                        (rand_use_last := true;
                            cached_rand_normal := x2 * v;
                            mean + x1 * v * std)
                    end
                else
                    box_muller()
                end
            in
            case !rand_use_last of
                true => (rand_use_last := false; mean + !cached_rand_normal*std)
            | false => box_muller()
            end

fun rand_perm RandState (m, n) =
    let
        fun fisher_yates (a, i, n, m) =
            if (i = n orelse i = m) then a
            else
            let
                val randj = i + Real.floor((Random.randReal RandState)
                                *Real.fromInt(n-i))
                val j = if (randj = n) then n-1 else randj
                val tmp = Array.sub(a, j)
            in
                (Array.update(a, j, Array.sub(a, i));
```

<!-- page: 121 -->

```txt
Array.update(a, i, tmp);
            fisher_yates (a, i+1, n, m))
        end
    fun seqArray(a, i, n) =
        if i = n then a
        else (Array.update(a, i, i+1);
        seqArray(a, i+1, n))
        fun arrayToList (a, i, l) =
            if ((i = Array.length(a)) orelse (l = 0)) then []
            else Array.sub(a, i)::arrayToList(a, i+1, l-1)
    val array_perm = fisher_yates(seqArray(Array.array(n, 0), 0, n)
                    , 0, n, m)
    val list_perm = arrayToList(arrayperm, 0, m)
in
    ListMergeSort.sort (fn (a, b) => a>b) list_perm
end
```

## A.3 Neural Network Library

## A.3.1 Neural Network Signature

```txt
signature NN =
sig
    type 'a matrix = 'a Matrix.matrix
    type 'a vector = 'a Matrix.vector
    datatype costType = NLL|MSE|CE|PER
    datatype initType = SPARSE|NORMAL|NORMALISED
    datatype actType = SIGM|TANH|LINEAR
    datatype wdType = L0|L1|L2
    type nnlayer = {input: real Matrix.matrix, (* ROWMATRIX *)
        output: real Matrix.matrix,(* ROWMATRIX *)
        GradW: real Matrix.matrix, (* COLMATRIX *)
        GradB: real Matrix.vector,
        B: real Matrix.vector,
        W: real Matrix.matrix,      (* COLMATRIX *)
        actType:actType
        }
    type params = {batchsize: int, (* number of training cases per batch *)
        nBatches: int,      (* number of batches *)
        testsize: int,     (* number of testing cases *)
        lambda: real,       (* momentum coefficient *)
        momentumSchedule: bool,
        maxLambda: real,
        lr: real,           (* learning rate *)
        costType: costType,   (* cost function type *)
        initType: initType,   (* initialization type *)
        actType: actType,      (* activation function type *)
        layerSizes: int list, (* structure of network *)
        initWs: real Matrix.matrix option list,
                               (* preinitialized Ws matrices *)
        initBs: real Matrix.vector option list,
                               (* preinitialized Bs matrices *)
        nItrs: int,          (* number of iterations/epochs *)
        wdType: wdType,
        wdValue: real,
        verbose: bool
```

<!-- page: 122 -->

```ocaml
}
type fileNames = { data_train: string,
       labels_train: string,
       data_test: string,
       labels_test: string
}
exception InputError
exception NotSupported

val setParams:     params -> unit
val run:   Random.rand ->      params * fileNames -> nnlayer list * real
val readData:      string * int * int * int -> real matrix list
val trainNN:        nnlayer list * real matrix list
           * real matrix list -> nnlayer list
val trainBest:    nnlayer list * real matrix list * real matrix list
           * real matrix list * real matrix list -> real * nnlayer list
val update:      nnlayer list -> nnlayer list
val update1layer: nnlayer -> nnlayer
val computeCost:  real matrix * real matrix * costType
           -> real * real matrix
val bprop:         nnlayer list * real matrix
           -> nnlayer list * real matrix
val bprop1layer:  nnlayer * real matrix -> nnlayer * real matrix

val fprop:         nnlayer list * real matrix
           -> nnlayer list * real matrix
val fprop1layer:  nnlayer * real matrix -> nnlayer * real matrix

val initLayers: Random.rand ->  int list * real matrix option list
           * real vector option list -> nnlayer list
val initLayer:  Random.rand ->  int * int * actType
           * real matrix option * real vector option-> nnlayer end
```

## A.3.2 Neural Network Structure

```ocaml
structure NN :> NN =
struct
type 'a matrix = 'a Matrix.matrix
type 'a vector = 'a Matrix.vector
exception InputError
exception NotSupported
(* nnlayer: neural network layer type
        a neural network is a list of nnlayer variables.
        each layer contains neccessary information
        for training and predicting process
*)
(* costType: supported cost function type
    - Negative log likelihood: only use when you're using oneHot labels.
    - Mean square error
    - Cross entropy
    - Error percentage - for benchmark only
*)
datatype costType = NLL|MSE|CE|PER
(* initType: supported initialization methods
    - Sparse
```

<!-- page: 123 -->

```ocaml
- Normal
- Normalized
*)
datatype initType = SPARSE|NORMAL|NORMALISED
(* actType: supported activation function
    - Sigmoid
    - Tanh
*)
datatype actType = SIGM|TANH|LINEAR
(* wdType: supported weight decay type
    - L0: no weight decay
    - L1: L1 weight decay
    - L2: L2 weight decay
*)
datatype wdType = L0|L1|L2
type nnlayer = {input: real matrix, (* ROWMATRIX *)
    output: real matrix,(* ROWMATRIX *)
    GradW: real matrix, (* COLMATRIX *)
    GradB: real vector,
    B: real vector,
    W: real matrix,        (* COLMATRIX *)
    actType:actType
}
type params = {batchsize: int,  (* number of training cases per batch *)
    nBatches: int,      (* number of batches *)
    testsize: int,     (* number of testing cases *)
    lambda: real,   (* momentum coefficient *)
    momentumSchedule: bool,
    maxLambda: real,
    lr: real,       (* learning rate *)
    costType: costType,  (* cost function type *)
    initType: initType,(* initialization type *)
    actType: actType,   (* activation function type *)
    layerSizes: int list, (* structure of network *)
    initWs: real matrix option list, (* preinitialized Ws matrices *)
    initBs: real vector option list, (* preinitialized Bs matrices *)
    nItrs: int,         (* number of iterations/epochs *)
    wdType: wdType,
    wdValue: real,
    verbose: bool
}
val params:params ref =
    ref{batchsize = 10,   (* number of training cases per batch *)
    nBatches = 12,      (* number of batches *)
    testsize = 30,     (* number of testing cases *)
    lambda = 0.0,   (* momentum coefficient *)
    momentumSchedule = false ,
    maxLambda = 0.0,
    lr = 0.005,       (* learning rate *)
    costType = MSE,   (* cost function type *)
    initType = NORMAL,(* initialization type *)
    actType = SIGM,   (* activation function type *)
    layerSizes = [4, 8, 3], (* structure of network *)
    nItrs = 40,          (* number of iterations/epochs *)
    initWs = [] ,
    initBs = [] ,
    wdType = L0 ,
    wdValue = 0.0 ,
```

<!-- page: 124 -->

```txt
verbose = false
    };
type fileNames = { data_train: string,
            labels_train: string,
            data_test: string,
            labels_test: string
        }
(* all input file names *)
val fileNames:fileNames =
{ data_train  = "data_train.csv",
    labels_train = "labels_train.csv",
    data_test   = "data_test.csv",
    labels_test  = "labels_test.csv"
}
(* ------------------- Functions for reading inputs -------------------*)
(* parseLine: parse line of string
input
- line: string of numbers seperated by commas
output
- list of real numbers
*)
fun setParams(p: params) =
params:=p
fun parseLine(line) =
let
fun getFirstNum nil = nil
| getFirstNum (x::xs) = if x = #"," then [] else x::getFirstNum(xs);
in
case line of
[] => []
| #",":line' => parseLine(line')
| #" "":line' => parseLine(line')
| _ =>
let
val numStr = implode(getFirstNum(line))
val num = valOf(Real.fromString(numStr))
in num::parseLine(List.drop(line, size(numStr)))
end
end
(* readData: read input data
input
- nAtts: Each line has nAtts numbers seperated by commas
- batchsize: number of lines to create a matrix
- nBatches: total number of batches
output
- list of batches (each batch is a ROWMATRIX)
*)
fun readData (fileName, nAtts, batchsize, nBatches) =
let
fun readLines (fh, nlines) =
case (TextIO endorsementStream fh, nlines = 0) of
( _ , true) => []
| (false, false) =>
(parseLine(explode(valOf(TextIO.inputLine fh))))
::readLines (fh, nlines -1)
| (true, false) => raise InputError
```

<!-- page: 125 -->

```txt
fun readBatches (fh, nBatches) =
    if nBatches > 0
    then Matrix.fromVectors2Rows(readLines(fh, batchsize),
            (batchsize, nAtts))
    ::readBatches(fh, nBatches-1)
    else (TextIO.closeIn fh; [])
in
readBatches(TextIO.openIn fileName, nBatches)
end
(* ------------------- Functions for training process -------------------*)
fun initSparseW RandState (nInputs, nOutputs) =
    let
    val nconn = 4;
    fun initNode (nInputs) =
        let
        fun initSparseList (ids, i, n) =
            case (ids, i <= n) of
            (_, false) => []
            |( [], true) => 0.0::initSparseList (ids, i+1, n)
            |( idx::ids', true) =>
            if (idx = i) then
                Randomext.rand_normal RandState (0.0, 1.0)
                ::initSparseList (ids', i+1, n)
            else
                0.0::initSparseList (ids, i+1, n)
            in
            initSparseList (Randomext.rand_perm RandState (nconn, nInputs),
                    , 1, nInputs)
        end
    fun initSparseVects (nInputs, nOutputs) =
        if (nOutputs > 0) then
            initNode (nInputs)::initSparseVects (nInputs, nOutputs-1)
            else []
        in
        Matrix.fromVectors2Cols(initSparseVects (nInputs, nOutputs),
            (nInputs, nOutputs))
    end
(* initLayer: initialize a neural network layer
    input:
        - nInputs: number of incoming nodes
        - nOutputs: number of outgoing nodes
    output:
        - a initialized layer
*)
fun initLayer RandState (nInputs, nOutputs, actType, initW, initB):nnlayer
        =
        let
        val input = Matrix.initRows (0.0, (1, 1))
        val output = Matrix.initRows (0.0, (1, 1))
        val GradW = Matrix.initCols (0.0, (nInputs, nOutputs))
        val GradB = Matrix.toVector(Matrix.initRows(0.0, (nOutputs, 1)))
        val B = case initB of
            NONE => Matrix.toVector(Matrix.initRows(0.0, (nOutputs, 1)))
            | SOME v => v
        val W = case initW of
            NONE => (case #initType(!params) of
```

<!-- page: 126 -->

```txt
SPARSE => initSparseW RandState (nInputs, nOutputs)
        | NORMAL =>
        Matrix.uniRandCols RandState (
          1.0/Math.sqrt(Real.fromInt(nInputs)),
          (nInputs, nOutputs))
        |_ => raise NotSupported)
        | SOME m => m
    in
    {input = input, output = output, GradW = GradW,
      GradB = GradB, B = B, W = W, actType = actType}
    end

(* initLayers: init the whole neural network
    input
      - layerSizes: structure of neural network
    output
      - a list of initialized layer (e.g. a initlaized network)
    NOTE:
      - if cost function is NLL or CE,
        last layer should not use any activation function
*)
fun initLayers RandState (layerSizes, initWs, initBs) =
    let
    val (initW, initWs') = case initWs of
          [] => (NONE, [])
          | W::initWs' => (W, initWs')
    val (initB, initBs') = case initBs of
          [] => (NONE, [])
          | B::initBs' => (B, initBs')
    in
    case layerSizes of
      [] => []
    | last ::[] => []
    | nInputs::nOutputs::[] =>
      if (#costType(!params) = NLL) orelse (#costType(!params) = CE) then
        initLayer RandState (nInputs, nOutputs, LINEAR, initW, initB) :: []
        else
        initLayer RandState (nInputs, nOutputs, #actType(!params), initW,
        initB)
        :: []
    | nInputs::nOutputs::layerSizes' =>
      initLayer RandState (nInputs, nOutputs, #actType(!params), initW,
        initB)
      ::initLayers RandState (nOutputs::layerSizes', initWs', initBs')
    end

fun sigm x =
    if x > 13.0 then 1.0
    else if x < ~13.0 then 0.0
    else 1.0/(1.0+Math.exp(~x))
(* fprop1layer: forward propagate 1 layer
    input:
      - layer: layer to be propagated
      - input: input data to be propagated
    output:
      - (propagated layer, propagated input)
*)
fun fprop1layer (layer:nnlayer, input) =
```

<!-- page: 127 -->

```txt
let
  val z = Matrix.addVect2MatrixReal(
      #B(layer), Matrix.mulMatrixRealR(input, #W(layer)))
  val output =
      case #actType(layer) of
      SIGM => Matrix.map sigm z
      | TANH => Matrix.map Math.tanh z
      | LINEAR => z
  in
  ({input = input, output = output, GradW = #GradW(layer),
      GradB = #GradB(layer), B = #B(layer), W = #W(layer),
      actType = #actType(layer)}, output)
  end
(* fprop: fpropagate the whole network
  input:
    - layers: neural network to be forward propagated
    - input:  input to the first layer (training data)
  output:
    - (propagated network, final propagated input)
  ** Note that returning network has the inversed order of layers
      This will be inversed again when using bprop function
*)
fun fprop (layers, input) =
  List.foldl(fn(layer, (layers', input)) =>
      case fprop1layer(layer, input) of
        (fpropedLayer, output) => (fpropedLayer::layers', output))
      ([], input) layers

(* bprop1layer: backward propagate 1 layer
  input:
    - layer: layer to be propagated
    - gradInput: input gradient to be propagated
  output:
    - (propagated layer, propagated gradient)
*)
fun bprop1layer (layer:nnlayer, gradInput) =
  let
  val lambda = #lambda(!params)
  val wdValue = #wdValue(!params)
  fun dervSigm x = x * (1.0 - x)
  fun dervTanh x = 1.0-x*x
  fun momentumUpdate (a, b) = lambda*a + ((1.0 - lambda)*b)
  fun sign x = if x > 0.0 then 1.0 else ~1.0

  val gradFunc = case #actType(layer) of
      SIGM => Matrix.map dervSigm (#output(layer))
      | TANH => Matrix.map dervTanh (#output(layer))
      | LINEAR => Matrix.initRows(1.0,
                       Matrix.size(#output(layer)))
  val gradOutput = Matrix.dotMulMatrixReal(gradInput, gradFunc)
  val gradOutputC = Matrix.changeType(gradOutput)
  val oldGradW = #GradW(layer)
  val oldGradB = #GradB(layer)
  val GradW_noWd = Matrix.mulMatrixRealC(Matrix.transpose(#input(layer)),
                   gradOutputC)
  val GradW = case #wdType(!params) of
      L0 => GradW_noWd
      | L1 => Matrix.merge (fn(a, b) => a + wdValue * sign b)
```

<!-- page: 128 -->

```txt
(GradW_noWd, #W(layer))
    | L2 => Matrix.merge (fn(a, b) => a + wdValue * b)
        (GradW_noWd, #W(layer))
    val GradB = Matrix.sumReal(gradOutputC)
    val newGradW = Matrix.merge momentumUpdate (oldGradW, GradW)
    val newGradB = Matrix.mergeVector momentumUpdate (oldGradB, GradB)
    val propedGrad = Matrix.mulMatrixRealR(
        gradOutput, Matrix.transpose(#W(layer)))
    in
    ({input = #input(layer), output = #output(layer), GradW = newGradW,
        GradB = newGradB, B = #B(layer), W = #W(layer),
        actType = #actType(layer)}, propedGrad)
    end
(* bprop: back propagate the whole network
    input:
        - layers: neural network with inversed order of layers created by
        fprop
        - gradInput: gradient to the last layer
    output:
        - (propagated network, final propagated gradient)
    ** Note that the input layers has to be in inversed layer order
        Which is the order in the network returned from fprop function
*)
fun bprop (layers, gradInput) =
    List.foldl (fn (layer, (layers', gradInput)) =>
        case bprop1layer(layer, gradInput) of
            (bpropedLayer, gradOutput) =>
            (bpropedLayer::layers', gradOutput))
        ([], gradInput) layers
(* computeCost: compute training/validating cost
    input:
        - output: predicted result from the neural network
        - target: the desired target
        - costType: type of cost - MSE/NLL/PER
    output:
        - (errors, gradient)
*)
val i:int ref = ref 0;
fun computeCost(output, target, costType) =
    let
    val nSamples = Real.fromInt(#1(Matrix.size(output)))
    val max = Matrix.foldl (fn (x, acc) => if x>acc then x else acc)
            ~10000.0
    fun mean v = (List.foldl (fn (x, acc) => acc+x) 0.0 v) /
        Real.fromInt(List.length(v))
    fun calMSE() =
        let
        val diff = Matrix.merge (fn (a, b) => a - b) (output, target)
        val errors = Matrix.sumReal(Matrix.map (fn a => 0.5*a*a) diff)
        val gradient = Matrix.map (fn a => a/nSamples)
            diff
        in
        (mean errors, gradient)
        end
    fun softmax(input) =
        let
        val maxInput = max input
```

<!-- page: 129 -->

```julia
val expInput = Matrix.mergeVect'2Matrix
        (fn (a, b) => Math.exp(b - a))
        (maxInput, input)
val sumExp = Matrix.sumReal expInput
in
Matrix.mergeVect'2Matrix (fn (a, b) => b/a)
            (sumExp, expInput)
end
fun calNLL() =
    let
    val _ = i:= (!i+1)
    val softmaxOutput = softmax(output)
    val errors = Matrix.sumReal(
        Matrix.merge (fn(a,b) => ~(Math.ln(a)*b))
        (softmaxOutput, target))
    val gradient = Matrix.merge (fn(a, b) => (~a + b)/nSamples)
            (target, softmaxOutput)
    in
    (mean errors, gradient)
end
fun calCE() =
    let
    val errors = Matrix.sumReal(
        Matrix.merge
            (fn(a,b) => Math.ln(1.0 + Math.exp(a)) - a*b)
            (output, target))
    val gradient = Matrix.merge
        (fn (a, b) => (sigm(a) - b)/nSamples)
        (output, target)
    in
    (mean errors, gradient)
end
fun equalReal(a, b) = Real.abs(a-b)<0.0000000001
fun calPER() =
    let
    val max_nonzeros = Matrix.foldl
        (fn (x, acc) => if (x>acc andalso
            not (equalReal(x, 0.0)))
            then x else acc)
            ~20000.0
    val nSamples = Real.fromInt(#1(Matrix.size(output)))
    val maxOutput = max output
    val maxTarget = max_nonzeros (Matrix.merge (fn (a, b) => a*b)
            (output, target))
    val answers = Matrix.mergeVector (fn (x, y) => equalReal(x, y))
            (maxOutput, maxTarget)
    val nRights = List.foldl (fn (x, acc) => if x then acc + 1
            else acc)
        0 answers
    in
    (1.0 - (Real.fromInt(nRights) / nSamples),
        Matrix.initRows(0.0, (1, 1)))
    end

in
case costType of
    MSE => calMSE ()
| NLL => calNLL ()
```

<!-- page: 130 -->

```txt
| CE => calCE ()
    | PER => calPER ()
end
(* update1layer: update 1 layer
input
  - layer: a layer to be updated
output
  - updated layer
*)
fun update1layer (layer:nnlayer) =
  let
  val newW = Matrix.merge (fn (a,b) => a - (#lr (!params))*b)
        (#W(layer), #GradW(layer))
  val newB = Matrix.mergeVector (fn (a,b) => a - (#lr (!params))*b)
            (#B(layer), #GradB(layer))
  in
{input = #input(layer), output = #output(layer), GradW = #GradW(layer),
GradB = #GradB(layer), actType = #actType(layer), W = newW, B = newB}
end

(* update: update the whole network
*)
fun update (layers) = List.foldr (fn (a, acc) => update1layer(a)::acc)
       [] layers

(* Support method for training neural network
*)
val i:int ref = ref 0;
fun train1Batch (layers, input, target) =
  let
  val (fpropedLayers, output) = fprop (layers, input)
  val _ = i:= (!i+1)
  val (errors, grad) = computeCost(output, target,
                      #costType(!params))
  val (bpropedLayers, _) = bprop (fpropedLayers, grad)
  val _ = if #verbose(!params) then print (Real.toString(errors) ^ "\n")
              else ()
  in
  update(bpropedLayers)
  end
fun trainBatches (layers, inputs, targets) =
  case (inputs, targets) of
  ([], []) => layers
    | (input::inputs', target::targets') =>
    trainBatches(train1Batch(layers, input, target),
           inputs', targets')
  | _ => raise Matrix.UnmatchedDimension
(* trainNN: train neural network
  input:
    - data_train: list of batches of training cases
    - target_train: list of batches of desired target
  output:
    - trained neural network
*)
fun trainNN(startLayers, data_train, target_train) =
  let
    fun trainEpoches (layers, nItrs) =
```

<!-- page: 131 -->

```txt
let val _ = if #verbose(!params) then print
        ("***** epochs: "^Int.toString(nItrs) ^ " *********\n") else ()
        in
        if nItrs = 0 then layers
        else
            trainEpoches(
                trainBatches (layers, data_train, target_train)
                    ,nItrs - 1)
        end
    in
        trainEpoches(startLayers, #nItrs (!params))
    end
(* 
TrainNN on training set and pick the best result on validation set *) 
fun trainBest(startLayers, data_train, target_train,
               data_validation, target_validation) =
    let
    fun trainEpoches (layers, nItrs, bestErr) =
        let val _ = if #verbose(!params) then print
        ("***** epochs: "^Int.toString(nItrs) ^ " *********\n") else ()
            val (_, output) = fprop(layers, hd(data_validation))
            val (errors, _) = computeCost(output, hd(target_validation), PER)
            val bestErr = if bestErr < errors then bestErr else errors
            val _ = if #verbose(!params) then print
        ("Best Validation Err = "^ Real.toString(bestErr) ^ "\n") else ()
            in
            if nItrs = 0 then (bestErr, layers)
            else
                trainEpoches(
                    trainBatches (layers, data_train, target_train)
                    ,nItrs - 1, bestErr)
            end
    in
        trainEpoches(trainBatches (startLayers, data_train, target_train),
                   #nItrs (!params), 1.0)
    end
(* run: read input data and train a neural network *)
*
fun run RandState (p:params, fs:fileNames) =
    let
    val _ = params := p
    val _ = if #verbose(!params) then print
        ("********* Reading data *********\n") else ()
        val data_train = readData(#data_train(fs),
                     hd(#layerSizes (!params)),
                     #batchsize (!params), #nBatches (!params))
        val labels_train = readData(#labels_train(fs),
                     List.last(#layerSizes (!params)),
                     #batchsize (!params), #nBatches (!params))
        val data_test = readData(#data_test(fs),
                     hd(#layerSizes (!params)),
                     #testsize (!params), 1)
        val labels_test = readData(#labels_test(fs),
                     List.last(#layerSizes (!params)),
                     #testsize (!params), 1)
        val _ = if #verbose(!params) then print
```

<!-- page: 132 -->

```txt
( "****** Done reading data, start training *****\n") else ()
    val startLayers = initLayers RandState (#layerSizes(!params),
                          #initWs(!params), #initBs (!params))

    val trainedLayers = trainNN(startLayers, data_train, labels_train)
    val (_, output) = fprop(trainedLayers, hd(data_test))
    val (errors, _) = computeCost(output, hd(labels_test),
                          PER)
    in
        (trainedLayers, errors)
    end
end
```

<!-- page: 133 -->

Appendix B

# ADATE Specification for Initialization Experiment

```txt
datatype aUnit = aUnit

datatype real_list = rnil | consr of real * real_list

datatype real_list_list = rlnil | consrl of real_list * real_list_list

datatype weightMatrix = weightMatrix of real * real_list_list

datatype weightMatrix_list = wnil | consw of weightMatrix *
    weightMatrix_list
datatype layerType = visHid | hidHid1 | hidHid2 | hidOut

fun rconstLess( ( X, C ) : real * rconst ) : bool =
    case C of rconst( Compl, StepSize, Current ) => realLess( X, Current )

fun rand_normal( ( Mean, Std) : real * real ) : real =
    let
    fun box_muller( Dummy : aUnit ) : real =
        case realSubtract(realMultiply(2.0,
            (aRand 0)), 1.0) of X1
        => case realSubtract(realMultiply(2.0,
            (aRand 0)), 1.0 ) of X2
        => case realAdd(realMultiply(X1, X1), realMultiply( X2, X2)) of W
        => case realLess(W, 1.0) of
        true   => realAdd(Mean,
            realMultiply(Std,
            realMultiply(X1,
            sqrt(realDivide(realMultiply(~2.0, ln(W)), W))))
    | false => box_muller aUnit
    in
    box_muller aUnit
    end

fun rand_2 () =
    2.0*(aRand 0) - 1.0
(* Normalized initialization *)
fun f( NInputs, NOputs, LayerType ) =
```

<!-- page: 134 -->

```txt
let
    fun h( N: real) : real_list =
        case 0.0 < N of
            false => rnil
        | true =>
            consr ( realDevide (realMultiply(Math.sqrt(6.0), rand_2 ( ))
        ,
                    Math.sqrt(realAdd(NInputs, NOUTputs)) )
        ,
            h(realSubtract( N, 1.0 )))
in
    h NInputs
end

fun initW ( (NInputs, NOUTputs, LayerType) : real * real * layerType )
                        : weightMatrix =
let
    fun initSparseVects( I : real ) : real_list_list =
        case realLess (I, NOUTputs) of
            false => rlnil
        | true =>
            consrl( f( NInputs, NOUTputs, LayerType ),
            initSparseVects( I + 1.0 ) )
    in
    weightMatrix( NInputs, initSparseVects 0.0 )
end

fun main ((Layer1size, Layer2size, Layer3size, Layer4size, Layer5size) :
    real * real * real * real * real ) : weightMatrix_list =
        consw(initW(Layer1size, Layer2size, visHid),
        consw(initW(Layer2size, Layer3size, hidHid1),
        consw(initW(Layer3size, Layer4size, hidHid2),
        consw(initW(Layer4size, Layer5size, hidOut),
        wnil))))
%%

val NumInputs =
    case getCommandOption "--numInputs" of SOME S =>
    case Int.fromString S of SOME N => N

val NumIterations =
    case getCommandOption "--numIterations" of SOME S =>
    case Int.fromString S of SOME N => N

val TrainParams : NN.params =
    {batchsize = 10, (* number of training cases per batch *)
        nBatches = 90, (* number of batches *)
        testsize = 4500, (* number of testing cases *)
        lambda = 0.99, (* momentum coefficient *)
        momentumSchedule = false, (* momentum schedule *)
        maxLambda = 0.0, (* max momentum *)
        lr = 0.05, (* learning rate *)
        costType = NN.NLL, (* cost function type *)
        initType = NN.SPARSE,(* initialization type *)
        actType = NN.TANH, (* activation function type *)
```

<!-- page: 135 -->

```txt
layerSizes = [100, 80, 80, 200, 10], (* structure of network *)
nItrs = NumIterations,          (* number of iterations/epochs *)
initWs = [],            (* init weight matrices *)
initBs = [],
wdType = NN.L2,      (* weight decay type *)
wdValue = 0.00001,
verbose = false
};

val ValidationParams : NN.params =
{batchsize = 10,   (* number of training cases per batch *)
nBatches = 90,    (* number of batches *)
testsize = 4500,  (* number of testing cases *)
lambda = 0.99,       (* momentum coefficient *)
momentumSchedule = false , (* momentum schedule *)
maxLambda = 0.0,     (* max momentum *)
lr = 0.05,        (* learning rate *)
costType = NN.NLL,   (* cost function type *)
initType = NN.SPARSE,(* initialization type *)
actType = NN.TANH,   (* activation function type *)
layerSizes = [100, 80, 80, 200, 10], (* structure of network *)
nItrs = 80,         (* number of iterations/epochs *)
initWs = [],          (* init weight matrices *)
initBs = [],
wdType = NN.L2,      (* weight decay type *)
wdValue = 0.00001,
verbose = false
};

(* all training and validation use the same Network structure )

val Inputs =
[(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 79.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(100.0, 80.0, 80.0, 200.0, 10.0),
(10O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 7O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O.O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 7O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 1O.O.),,
(1O.O.O., 8O.O., 8O.O., 2O'O.O., 2P.O.
),
```

<!-- page: 136 -->

```bazel
val input_files = [("/local/data1.csv", "/local/labels1.csv",
        "/local/datavalid1.csv", "/local/labelsvalid1.csv"),
        (/local/data2.csv", "/local/labels2.csv",
        "/local/datavalid2.csv", "/local/labelsvalid2.csv"),
        (/local/data3.csv", "/local/labels3.csv",
        "/local/datavalid3.csv", "/local/labelsvalid3.csv"),
        (/local/data4.csv", "/local/labels4.csv",
        "/local/datavalid4.csv", "/local/labelsvalid4.csv"),
        (/local/data5.csv", "/local/labels5.csv",
        "/local/datavalid5.csv", "/local/labelsvalid5.csv"),
        (/local/data6.csv", "/local/labels6.csv",
        "/local/datavalid6.csv", "/local/labelsvalid6.csv"),
        (/local/data7.csv", "/local/labels7.csv",
        "/local/datavalid7.csv", "/local/labelsvalid7.csv"),
        (/local/data8.csv", "/local/labels8.csv",
        "/local/datavalid8.csv", "/local/labelsvalid8.csv"),
        (/local/data9.csv", "/local/labels9.csv",
        "/local/datavalid9.csv", "/local/labelsvalid9.csv"),
        (/local/data10.csv", "/local/labels10.csv",
        "/local/datavalid10.csv", "/local/labelsvalid10.csv"),
        (/local/data11.csv", "/local/labels11.csv",
        "/local/datavalid11.csv", "/local/labelsvalid11.csv"),
        (/local/data12.csv", "/local/labels12.csv",
        "/local/datavalid12.csv", "/local/labelsvalid12.csv"),
        (/local/data13.csv", "/local/labels13.csv",
        "/local/datavalid13.csv", "/local/labelsvalid13.csv"),
        (/local/data14.csv", "/local/labels14.csv",
        "/local/datavalid14.csv", "/local/labelsvalid14.csv"),
        (/local/data15.csv", "/local/labels15.csv",
        "/local/datavalid15.csv", "/local/labelsvalid15.csv"),
        (/local/data16.csv", "/local/labels16.csv",
        "/local/datavalid16.csv", "/local/labelsvalid16.csv"),
        (/local/data17.csv", "/local/labels17.csv",
        "/local/datavalid17.csv", "/local/labelsvalid17.csv"),
        (/local/data18.csv", "/local/labels18.csv",
        "/local/datavalid18.csv", "/local/labelsvalid18.csv"),
        (/local/data19.csv", "/local/labels19.csv",
        "/local/datavalid19.csv", "/local/labelsvalid19.csv"),
```

<!-- page: 137 -->

```julia
("/local/data20.csv", "/local/labels20.csv",
        "/local/datavalid20.csv", "/local/labelsvalid20.csv"),
        ];

fun readData (data, target, data_valid, target_valid) =
    (NN.readData(data,
        hd(#layerSizes(TrainParams)),
        #batchsize(TrainParams), #nBatches(TrainParams)),
        NN.readData(target,
        List.last(#layerSizes(TrainParams)),
        #batchsize(TrainParams), #nBatches(TrainParams)),
        NN.readData(data_valid,
        hd(#layerSizes(TrainParams)),
        #testsize(TrainParams), 1),
        NN.readData(target_valid,
        List.last(#layerSizes(TrainParams)),
        #testsize(TrainParams), 1))
(* real input data for training process *)
val input_data = Array.fromList (List.map readData input_files)

(* convert ADATE list type to ML list *)
fun toRealListListList (Ws: weightMatrix_list):(real * real list list) list
=
let
fun toRealList (rs): real list =
    case rs of
    rnil => []
    |consr(r, rs') => r::toRealList(rs')
fun toRealListList (rls: real_list_list): real list list =
    case rls of
    rlnil => []
    |consr(rl, rls') => toRealList(rl)::toRealListList(rls')
    in
case Ws of
    wnil => []
    | consw( weightMatrix(nInputs, rls),Ws') =>
    (nInputs, toRealListList(rls)) :: toRealListListList(Ws')
end
fun toWeightList RandState (Ws: (real * real list list) list)
    : real Matrix.matrix option list =
    let
fun initWeightMatrix(arg as (n, W):(real * real list list))
    : real Matrix.matrix option =
    let
val nInputs = Real.floor (n)
fun initSparseList ((ids, initializedWeights, nInputs, I):
            (Int32.int list * real list * Int32.int * Int32.int))
        : real list =
            case (ids, I <= nInputs) of
        (_, false) => []
        |( [], true) =>
0.0::initSparseList (ids, initializedWeights, nInputs, I+1)
        |( idx::ids', true) =>
if (idx = I) then
    hd(initializedWeights)
    ::initSparseList (ids',
        tl(initializedWeights),
        nInputs, I+1)
```

<!-- page: 138 -->

```ocaml
else
    0.0::initSparseList (ids,
        initializedWeights,
        nInputs, I+1)
fun initSparseVects (nInputs, vs) =
    case vs of
[] => []
|v::vs' => initSparseList(
    (rand_perm RandState (length(v), nInputs)),
    v, nInputs, 1)::
(initSparseVects(nInputs, vs'))
in
SOME (Matrix.fromVectors2Cols(initSparseVects(nInputs, W),
            (nInputs, length(W))))
end
in
case Ws of
[] => []
|W::Ws' => initWeightMatrix(W) :: toWeightList RandState (Ws')
end

val Abstract_types = []
val Reject_funs = []
fun restore_transform D = D
fun compile_transform D = D
val print_synted_program = Print.print_dec'

val Funs_to_use = [
    "false", "true",
    "realLess", "realAdd", "realSubtract", "realMultiply",
    "tanh",
    "tor", "rconstLess",
    "rand_normal",
    "0",
    "aRand",
    "rnil", "consr"
]

fun to( G : real ) : LargeInt.int =
    Real.toLargeInt IEEEReal.TO_NEAREST ( G * 1.0e14 )

structure Grade : GRADE =
struct
type grade = LargeInt.int
val NONE = LargeInt.maxInt
val zero = LargeInt.fromInt 0
val op+ = LargeInt.+ 
val comparisons = [ LargeInt.compare ]
val N = LargeInt.fromInt 1000000 * LargeInt.fromInt 1000000
val significantComparisons = [ fn( E1, E2 )
                                      => LargeInt.compare( E1 div N, E2 div N ) ]

fun toString( G : grade ) : string =
    Real.toString( Real.fromLargeInt G / 1.0E14 )

val pack = LargeInt.toString
```

<!-- page: 139 -->

```txt
fun unpack( S : string ) : grade =
    case LargeInt.fromString S of SOME G => G

val post_process = fn X => X

val toRealOpt = NONE

end

val Inputs = take( NumInputs, Inputs )

fun output_eval_fun( exactlyOne( I: int, _ : (real * real * real * real *
        real),
            WeightList : weightMatrix_list ) ) = [
let
    val _ = NN.setParams
        ( if I < Int64.fromInt NumInputs
        then TrainParams
        else ValidationParams )
    val RandState = Random.rand( 10, Int64.toInt I )
    val (data_train , labels_train , data_test , labels_test) =
        Array.sub(input_data, Int64.toInt I)
    val Ws = toWeightList RandState (toRealListListList(WeightList))
    val startLayers = NN.initLayers RandState (#layerSizes(TrainParams), Ws,
        [])
    val trainedLayers = NN.trainNN(startLayers, data_train, labels_train)
    val (_, output) = NN.fprop(trainedLayers, hd(data_test))
    val (errors, _) = NN.computeCost(output, hd(labels_test), NN.PER)

    val () = (
        p"\noutput_eval_fun: I = "; print_int64 I;
        p" errors = "; print_real errors;
        p"\n"
    )

in
    if errors > 1.0E30 orelse not ( Real.isFinite errors ) then
        { numCorrect = 0 : int, numWrong = 1 : int, grade = to 1.0E30 }
    else
        { numCorrect = 1, numWrong = 0, grade = to errors }
end
    ]

exception MaxSyntComplExn
val MaxSyntCompl = (
    case getCommandOption "--maxSyntacticComplexity" of
        NONE => 150.0
    | SOME S => case Real.fromString S of SOME N => N
) handle Ex => raise MaxSyntComplExn

fun rlEq( rnil, rnil ) = true
    | rlEq( rnil, consr( _, _ ) ) = false
    | rlEq( consr( _, _ ), _ ) = false
    | rlEq( consr( X1, Xs1 ), consr( Y1, Ys1 ) ) =
        real_eq( X1, Y1 ) andalso rlEq( Xs1, Ys1 )
```

<!-- page: 140 -->

```txt
fun rllEq( rlnil, rlnil ) = true
    | rllEq( rlnil, consrl( _, _ ) ) = false
    | rllEq( consrl( _, _ ), _ ) = false
    | rllEq( consrl( X1, Xs1 ), consrl( Y1, Ys1 ) ) =
        rlEq( X1, Y1 ) andalso rllEq( Xs1, Ys1 )

fun wmEq( weightMatrix( X, Xss ), weightMatrix( Y, Yss ) ) =
    real_eq( X, Y ) andalso rllEq( Xss, Yss )

fun wlEq( wnil, wnil ) = true
    | wlEq( wnil, consw( _, _ ) ) = false
    | wlEq( consw( _, _ ), _ ) = false
    | wlEq( consw( X1, Xs1 ), consw( Y1, Ys1 ) ) =
        wmEq( X1, Y1 ) andalso wlEq( Xs1, Ys1 )

val AllAtOnce = false
val OnlyCountCalls = false
val TimeLimit : Int.int = 10000000
val max_time_limit = fn () => Word64.fromInt TimeLimit : Word64.word
val max_test_time_limit = fn () => Word64.fromInt TimeLimit : Word64.word
val time_limit_base = fn () => real TimeLimit

fun max_syntactic_complexity() = MaxSyntCompl
fun min_syntactic_complexity() = 0.0
val Use_test_data_for_max_syntactic_complexity = false

val main_range_eq = wlEq
val File_name_extension =
    "numIterations" ^ Int.toString NumIterations ^
    "numInputs" ^ Int.toString NumInputs

val Resolution = NONE
val StochasticMode = false

val Number_of_output_attributes : Int64.int = 4

fun terminate( Nc, G ) = false
```

<!-- page: 141 -->

<!-- page: 142 -->
