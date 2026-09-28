<!-- page: 1 -->

| CS 188 | Introduction to |  |
| --- | --- | --- |
| Fall 2014 | Artificial Intelligence | Final |

## INSTRUCTIONS

• You have 2 hours 50 minutes.

• The exam is closed book, closed notes except a one-page crib sheet.

• Please use non-programmable calculators only. Laptops, phones, etc., may not be used. If you have one in your bag please switch it off.

• Mark your answers ON THE EXAM ITSELF. If you are not sure of your answer you may wish to provide a brief explanation. All short answer sections can be successfully answered in a few sentences at most.

• Questions are not sequenced in order of difficulty. Make sure to look ahead if stuck on a particular question.

| Last Name |  |
| --- | --- |
| First Name |  |
| SID |  |
| Email |  |
| First and last name of person on left |  |
| First and last name of person on right |  |
| All the work on this exam is my own.(please sign) |  |

<table><tbody><tr><td>Q. 1</td><td>Q. 2</td><td>Q. 3</td><td>Q. 4</td><td>Q. 5</td><td>Q. 6</td><td>Q. 7</td><td colspan="3">Q. 8 Q. 9 Q. 10</td><td>Total</td></tr><tr><td>/10</td><td>/10</td><td>/ 11</td><td>/ 6</td><td>/12</td><td>/12</td><td>/11</td><td>/11</td><td>/7</td><td>/10</td><td>/100</td></tr></tbody></table>

<!-- page: 2 -->

## 1. (10 points) Agents, Search, CSPs

Please CIRCLE either True OR False for the following questions.

**(a) (1 pt)** True/False: A hill-climbing algorithm that never visits states with lower value (or higher cost) is guaranteed to find the optimal solution if given enough time to find a solution.

**(b) (1 pt)** True/False: Suppose the temperature schedule for simulated annealing is set to be constant up to time N and zero thereafter. For any finite problem, we can set N large enough so that the algorithm is returns an optimal solution with probability 1.

**(c) (1 pt)** True/False: For any local-search problem, hill-climbing will return a global optimum if the algorithm is run starting at any state that is a neighbor of a neighbor of the state corresponding to the global optimum.

**(d) (1 pt)** True/False: Given a fully observable task environment where there is more than one action at every particular state, there exists a simple reflex agent that can take a different action upon revisiting the same state.

**(e) (1 pt)** True/False: Running forward checking after the assignment of a variable in backtracking search will ensure that every variable is arc consistent with every other variable.

**(f) (1 pt)** True/False: Suppose we use the min-conflicts algorithm to try to solve a CSP. It is possible the algorithm will not terminate even if the CSP has a solution.

**(g) (1 pt)** True/False: In a CSP constraint graph, a link (edge) between any two variables implies that those two variables may not take on the same values.

**(h) (1 pt)** True/False: A model-based reflex agent maintains some internal state that it updates as the agent collects more information through percepts.

<!-- page: 3 -->

**(i) (1 pt)** True/False: For any particular CSP constraint graph, there exists exactly one minimal cutset.

**(j) (1 pt)** True/False: Suppose agent A1 is rational and agent A2 is irrational. There exists a task environment where A2’s actual score will be greater than A1’s actual score.

<!-- page: 4 -->

## 2. (10 points) Game tree search on intervals

Consider a modification of a game tree where, rather than numbers, leaf nodes are now intervals, given by [lower, upper], and where the true value is somewhere inside the interval. Here is an example (with a spare copy for later use):

![](images/page_3_image_3.jpg)

For parts (a) and (b), suppose the min and max players are both trying to optimize avg(lower, upper); that is, max is trying to maximize the average value of the interval chosen and min is trying to minimize it.

**(a) (2 pt)** In each node of the tree above, fill in the interval defining what the agent knows about the value of that node.

**(b) (2 pt)** In the tree above, cross out the leaves that would be pruned by alpha-beta pruning based on average values.

For parts (c) and (d), assume that upper(interval) is the upper bound of current interval we are looking at, lower(interval) is the lower bound, α is the best value for max seen so far and β the best value for min.

**(c) (3 pt)** Suppose that min and max are both pessimistic: both try to optimize their worst possible outcomes. Is pruning possible in this scenario? If so, write the pruning condition which, if true, would lead to maximal pruning while evaluating a max node. If not, explain why not.

**(d) (3 pt)** Suppose that min and max are both optimistic: both try to optimize their best possible outcomes. Is pruning possible in this scenario? If so, write the pruning condition which, if true, would lead to maximal pruning while evaluating a max node. If not, explain why not.

<!-- page: 5 -->

## 3. (11 points) Propositional Logic

**(a)** <strong><u>(3 pt)</u></strong> <u>True/False:</u> $A \land B \implies C$ <u>entails</u> $( A \implies C ) \lor ( B \implies C$ <u>)</u>

**(b)** <strong><u>(2 pt)</u></strong> <u>True/False: Every nonempty propositional clause, by itself, is satisfiable.</u>

**(c) (2 pt)** True/False: Suppose a propositional clause contains three literals, each mentioning a different variable; then <u>the clause is satisfied in exactly 7 of the 8 possible models for the three variables.</u>

A ∨ B ∨ C

**(d) (4 pt)** Now explain why the following set of clauses is unsatisfiable without using truth tables:

$$
\neg A \lor B \lor C
$$

$$
A \lor B \lor \neg C
$$

$$
\neg A \lor B \lor \neg C
$$

$$
A \lor \neg B \lor C
$$

$$
\neg A \lor \neg B \lor C
$$

$$
A \lor \neg B \lor \neg C
$$

$$
\neg A \lor \neg B \lor \neg C
$$

<!-- page: 6 -->

## 4. (6 points) Bayes Nets

You’re interested in predicting whether boba stores in Berkeley will be successful or go out of business. You decide to solve this problem using probablistic inference over a model with the following variables:

• S, whether or not the store will be successful. May take two values: true or f alse.

• T, whether or not the store makes boba with real tea leaves. May take two values: true or f alse.

• N, the number of other boba stores nearby. May take three values: 0, 1, or > 1.

• L, location of the store relative to campus. May take four values: north, south, east, or west.

• C, the cost of the boba. May take two values: cheap or expensive.

**(a) (1 pt)** Your first idea for a probability model is a joint probability table over all of the variables. How many free <u>parameters would this joint probability table have (after taking into account sum-to-1 constraints)?</u>

**(b) (2 pt)** You decide this is too many parameters. To fix this, you decide to model the problem with the following Bayes net instead:

![](images/page_5_image_10.jpg)

For this network, write next to each node the total number of free parameters in its conditional probability table, taking into account sum-to-1 constraints.

**(c) (3 pt)** A new boba store is opening up! You don’t know how expensive it will be, but you have heard that it’s going to use real tea, it will be North of campus, and there will be one other boba store nearby. According to your model, what is the probability it will be successful? (Just write out the expression in terms of conditional probabilities from the model; no need to simplify, though you may include a normalizing constant.)

<!-- page: 7 -->

## 5. (12 points) Bayes Nets

A k-zigzag network has k Boolean root variables and $k + 1$ Boolean leaf variables, where root i is connected to leaves i and i + 1. Here is an example for $k   =   3 ,$ where each $D _ { i }$ represents a Boolean disease variable and each $S _ { j }$ is a Boolean symptom variable:

![](images/page_6_image_4.jpg)

Figure 1: A 3-zigzag Bayes net.

**(a) (1 pt)** Does having symptom $S _ { 4 }$ affect the probability of disease $D _ { 1 } ?$ Why or why not?

**(b) (3 pt)** Using only conditional probabilities from the model, express the probability of having symptom $S _ { 1 }$ but not symptom $S _ { 2 } ,$ given disease $D _ { 1 }$

**(c) (1 pt)** True/False: Exact inference in a k-zigzag net can be done in time $O ( k )$

**(d) (1 pt)** Suppose the values of all the symptom variables have been observed, and you would like to do Gibbs sampling on the disease variables (i.e., sample each variable given its Markov blanket). What is the largest number of non-evidence variables that have to be considered when sampling any particular disease variable? Explain your answer.

<!-- page: 8 -->

**(e) (2 pt)** Suppose $k   =   5 0$ . You would like to run Gibbs sampling for 1 million samples. Is it a good idea to precompute all the sampling distributions, so that when generating each individual sample no arithmetic operations are needed? Explain.

**(f) (2 pt)** A k-zigzag++ network is a k-zigzag network with two extra variables: one is a root connected to all the leaves and one is a leaf to which all the roots are connected. You would like to run Gibbs sampling for 1 million samples in a 50-zigzag++ network. Is it a good idea to precompute all the sampling distributions? Explain.

**(g) (2 pt)** Let us assume that in every case the values of all symptom variables are observed, which means that we can consider training a neural net to predict diseases from symptoms rather than using a Bayes net. Mary from MIT claims that an equivalent neural net can be obtained by reversing the arrows in the figure. She argues that because $D _ { 1 }$ doesn’t affect $S _ { 3 }$ and $S _ { 4 } ,$ they are not needed for predicting $D _ { 1 }$ . Is Mary right? Explain.

<!-- page: 9 -->

## 6. (12 points) Hidden Semi-Markov Models

![](images/page_8_image_3.jpg)

A Hidden Semi-Markov Model is an extention of HMMs where the system is allowed reside in a given state for some duration before a transition occurs to the next state (which may be the same state as before). In a regular HMM the durations are all 1. The HSMM formulation is as follows:

• Chain of state variables $X _ { 1 } , \ldots , X _ { T } ; X _ { t }$ is the state of the system at time $t ;$ actual states are labeled by integers.

• Chain of evidence variables $E _ { 1 } , \ldots , E _ { T } ; E _ { t }$ is the observation at time $t ;$ actual observations are labeled by integers.

• State sequence durations $D _ { 1 } , \ldots , D _ { M }$ , which take on positive integer values; $D _ { m }$ is the number of time steps the system resides in a state $i _ { m }$ between transition $m - 1$ and transition m.

It is helpful also to define the variables $S _ { m }$ and $F _ { m } ,$ the start and finish times for period $m ,$ where $S _ { 1 }   =   1 , \; F _ { 1 }   =   D _ { 1 }$ $S _ { 2 }   =   D _ { 1 }   +   1 , \; F _ { 2 }   =   D _ { 1 }   +   D _ { 2 }$ , etc. Then we can write $X _ { S _ { m } : F _ { m } } = i _ { m }$ as shorthand for $X_{S_m} = i_m, X_{S_m+1} =$ $i _ { m } , \ldots , X _ { F _ { m } } = i _ { m }$

Suppose that a transition occurs at time t which is the end of residence period m with duration $D _ { m }$ . The new state depends on the old state and its duration, while the new duration depends only on the new state:

$$
P (X _ {t + 1}, D _ {m + 1} \mid X _ {t}, D _ {m}) = P (X _ {t + 1} | X _ {t}, d _ {m}) P (D _ {m + 1} | X _ {t + 1}).\tag{1}
$$

During a residence period, of course, the state and duration remain constant. In all cases the evidence at t depends only on the state at t. Thus, the entire probability model can be built from the following probability tables:

(A) Initial distribution of X: $P ( X _ { 1 } )$

(B) Sensor model: $P ( E | X )$

(C) Transition model: $P ( X _ { S _ { m + 1 } } = i | X _ { F _ { m } } = j , D _ { m } = d ) ;$

(D) Duration model: $P ( D | X )$

**(a) (2 pt)** Which of the following expressions are correct for $P _ { 1 } \mathop { = } P ( D _ { 1 } , X _ { 1 } , \ldots , X _ { D _ { 1 } } , E _ { 1 } , \ldots , E _ { D _ { 1 } } )$ , the probability that the first period has duration $D _ { 1 }$ and the state sequence is $X _ { 1 } , \ldots , X _ { D _ { 1 } }$ and the observation sequence is $E _ { 1 } , \ldots , E _ { D _ { 1 } }$ , assuming $X _ { 1 }   =   X _ { 2 }   =   \ldots   =   X _ { D _ { 1 } } ?$

$$
P (X _ {1}) P (D _ {1} \mid X _ {1}) \prod_ {t = 1} ^ {D _ {1}} P (E _ {t} \mid X _ {t})
$$

$$
P (X _ {1}) \prod_ {t = 1} ^ {D _ {1}} P (E _ {t} \mid X _ {t}) P (D _ {t} \mid X _ {t})
$$

$P ( X _ { 1 } ) \textstyle \prod _ { t \: = \: 1 } ^ { D _ { 1 } } P ( E _ { t } \mid X _ { t } )$

$\textstyle P ( X _ { 1 } , E _ { 1 } ) P ( D _ { 1 } \mid X _ { 1 } ) \prod _ { t \: = \: 2 } ^ { D _ { 1 } } P ( E _ { t } \mid X _ { t } )$

**(b) (2 pt)** The following expression is supposed to be the probability that the first M periods have durations $D _ { 1 } , \ldots , D _ { M }$ and the state sequence is $X _ { 1 } , \ldots , X _ { F _ { M } }$ and the observation sequence is $E _ { 1 } , \ldots , E _ { F _ { M } }$ , but one term is missing. What is that term and where does it go?

$$
P _ {1} \prod_ {m = 2} ^ {M} P (X _ {S _ {m}} \mid X _ {F _ {m - 1}}, D _ {m - 1}) \prod_ {t = S _ {m}} ^ {F _ {m}} P (E _ {t} \mid X _ {t})
$$

<!-- page: 10 -->

**(c) (3 pt)** Suppose we want to describe an HSMM as an ordinary dynamic Bayes net that yields an exactly equivalent distribution over state and observation sequences. In addition to $X _ { t }$ and $E _ { t } ,$ , we will handle durations using $C _ { t } ,$ the duration of the current period, and $R _ { t } ,$ the amount of time left in the current period. In the figure below, add an appropriate (and minimal) set of links to define the model.

![](images/page_9_image_2.jpg)

![](images/page_9_image_3.jpg)

![](images/page_9_image_4.jpg)

![](images/page_9_image_5.jpg)

![](images/page_9_image_6.jpg)

![](images/page_9_image_7.jpg)

![](images/page_9_image_8.jpg)

![](images/page_9_image_9.jpg)

**(d) (2 pt)** Describe precisely the conditional distribution for $C _ { 2 }$ in your model.

**(e) (3 pt)** The forward equation for an ordinary HMM is given by

$$
P (X _ {t + 1} \mid e _ {1: t + 1}) = \alpha P (e _ {t + 1} \mid X _ {t + 1}) \sum_ {x _ {t}} P (X _ {t + 1} \mid x _ {t}) P (x _ {t} \mid e _ {1: t}).
$$

Write the forward equation for this dynamic Bayes net; i.e., write an equation for $P ( X _ { t + 1 } , C _ { t + 1 } , R _ { t + 1 } \mid e _ { 1 : t + 1 } )$ in terms of $P ( X _ { t } , C _ { t } , R _ { t } \mid e _ { 1 : t } )$ and quantities given in the model.

<!-- page: 11 -->

## 7. (11 points) MDPs

**(a) (3 pt)** The MDP of life has two actions P arty and Study in the start state. After that, there is only one choice per state. If the agent parties, it receives a reward of +10 followed by an infinite sequence of rewards of –1. If the agent studies, it receives a reward of –10 followed by an infinite sequence of rewards of +1. For what value of the discount factor γ is the agent indifferent between partying and studying? (Recall that $1 + x + x ^ { 2 } + \cdots = 1 / ( 1 - x ) . )$

The GSIs of 188 have started a game company. Their first game, GhostBlushers, starts with two ghosts, Blinky and Pinky. On each turn, the player clicks on a ghost. Clicking on any Blinky (action a<sub>B</sub>) produces a new Blinky with probability $( 2 b + p ) / 2 ( b + p )$ and a new Pinky otherwise, whereas clicking on any Pinky (action a<sub>P</sub> ) produces a new Pinky with probability $( b + 2 p ) / 2 ( b + p )$ and a new Blinky otherwise, where b and p are the numbers of Blinkies and Pinkies in the current state. There is a reward of +1 for producing an offspring of the same kind. The game ends after T steps.

**(b)** <strong><u>(4 pt)</u></strong> Define the game as an MDP, with a minimal state space. (No need to describe both actions, just $a _ { B } . )$

**(c) (1 pt)** The total number of states in the MDP is  O(T) O(T<sup>2</sup>) $\bigcirc \mathop { O } O ( T ^ { 3 } )$ None of these

**(d)** <strong><u>(2 pt)</u></strong> <u>Explain why value iteration applied to this problem converges exactly after O(T) iterations.</u>

**(e) (1 pt)** Assuming that Bellman backups at each state consider only successor states that have nonzero probability, the total runtime of value iteration on this problem is

$$
O (T ^ {2})
$$

$O ( 2 ^ { T } )$

None of these

<!-- page: 12 -->

## 8. (11 points) Approximate Q-Learning

The UC system is experimenting with new transportation options that will help students move between all 10 campuses.

Each possible **state** for a student is a tuple of location (one of 10 campuses) and mood (happy or upset).

Available **actions**: Bus, T axi, Motorcycle. Actions have the following properties:

| Action | Makes Stops | Max. Passengers | Has Wi-Fi |
| --- | --- | --- | --- |
| Bus | Yes | 50 | Yes |
| Taxi | No | 4 | No |
| Motorcycle | No | 1 | No |

We will use a linear, feature-based approximation of the Q-values:

Linear value function: $Q _ { \mathbf { w } } ( s , a ) = \sum _ { i = 0 } ^ { 3 } f _ { i } ( s , a ) w _ { i } .$

<table><tr><td colspan="2">Features</td><td>Initial Weights</td></tr><tr><td colspan="2"> $f_0(state, action) = 1$  (this is a bias feature that is always 1)</td><td> $w_0 = 1$ </td></tr><tr><td colspan="2"> $f_1(state, action) = \left\{ \begin{array}{ll} 1 & \text{if action makes stops} \\ 0 & \text{otherwise} \end{array} \right.$ </td><td> $w_1 = 2.5$ </td></tr><tr><td colspan="2"> $f_2(state, action) = \left\{ \begin{array}{ll} 1 & \text{if action has max. passengers > 1} \\ 0 & \text{otherwise} \end{array} \right.$ </td><td> $w_2 = 0.5$ </td></tr><tr><td colspan="2"> $f_3(state, action) = \left\{ \begin{array}{ll} 1 & \text{if action has Wi-Fi} \\ 0 & \text{otherwise} \end{array} \right.$ </td><td> $w_3 = 1$ </td></tr></table>

Remember that the approximate Q-values are a function of the weights, so make sure to use the chain rule as follows whenever updating the weights:

$$
w _ {i} \leftarrow w _ {i} + \alpha \left[ r + \gamma \max _ {a ^ {\prime}} Q _ {\mathbf {w}} (s ^ {\prime}, a ^ {\prime}) - Q _ {\mathbf {w}} (s, a) \right] \frac {\partial}{\partial w _ {i}} Q _ {\mathbf {w}} (s, a)
$$

**(a) (3 pt)** Calculate the following initial Q values given the initial weights above:

| Q( (UCLA,upset), Bus ) |  |
| --- | --- |
| Q( (UCLA,upset), Taxi ) |  |
| Q( (UCLA,upset), Motorcycle ) |  |

**(b) (2 pt)** The initial Q-values for the state (UCLA, upset) happen to be equal to the corresponding initial Q-values for the state (Berkeley, happy). As you update the weights, will these values always be the equal to each other? In other words, will $Q _ { \mathbf { w } } ( \; ( U C L A , u p s e t ) , \: a \; ) \: = \: Q _ { \mathbf { w } } ( \; ( B e r k e l e y , h a p p y ) , \: a \; )$ given any action a and vector of weights w?

Yes No

Why / Why not? (in just one sentence)

<!-- page: 13 -->

**(c) (2 pt)** Exploration / exploitation: Given the Q-values for the state (UCLA, upset) you calculated on the previous page, what is the probability that each action could be chosen when using -greedy exploration (assuming any random movements are chosen uniformly from all actions)?

| Action | Probability (in terms of) |
| --- | --- |
| Bus |  |
| Taxi |  |
| Motorcycle |  |

**(d) (2 pt)** Given a sample with start state = (Berkeley, happy), action= Taxi, successor stat $\mathbf { c } = ( U C L A , \; u p s e t )$ , and reward = -7: Using a learning rate of α = 0.5 and discount of $\gamma = 0 . 5 ,$ , update each of the weights.

| w<sub>0</sub> = |
| --- |
| w<sub>1</sub> = |
| w<sub>2</sub> = |
| w<sub>3</sub> = |

**(e) (2 pt)** Give one advantage and one disadvantage of using approximate Q-Learning rather than standard Q-Learning.

<!-- page: 14 -->

## 9. (7 points) Decision Trees

After taking CS188, Alice wants to construct a decision tree classifier to predict flight delays. She has collected the data for a few months. A summary of the data is provided in table below. Read it **carefully**.

<table><tbody><tr><td rowspan="2">Feature</td><td colspan="2">Feature value = Yes</td><td colspan="2">Feature value = No</td></tr><tr><td># Delayed</td><td># not Delayed</td><td># Delayed</td><td># not Delayed</td></tr><tr><td>Rain</td><td>30</td><td>10</td><td>10</td><td>30</td></tr><tr><td>Wind</td><td>25</td><td>15</td><td>15</td><td>25</td></tr><tr><td>Summer</td><td>5</td><td>35</td><td>35</td><td>5</td></tr><tr><td>Winter</td><td>20</td><td>10</td><td>20</td><td>20</td></tr><tr><td>Day</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>Night</td><td>15</td><td>10</td><td>25</td><td>30</td></tr></tbody></table>

**(a) (1 pt)** Alice thinks she was tired when filling in the last column and may have made a mistake. Please correct it in the table for her.

**(b) (2 pt)** Which of “ Rain” and “Day” has the higher information gain for predicting delay? Explain without numerical calculations.

**(c) (2 pt)** Bob the Stanford student says **among all six features**, “Rain” should be at the root of the decision tree. Do you agree with him? If not, which feature should be at the root? Explain why **qualitatively**.

**(d) (2 pt)** Based **only** on the table, can you determine which feature should be on the second level (the level just beneath the root) of the decision tree? If yes, which one is it? Support your answer **qualitatively**.

<!-- page: 15 -->

![](images/page_14_image_2.jpg)

![](images/page_14_image_3.jpg)

(b)

(a)

Figure 2: (a) A neural network with two hidden layers; (b) a multiclass perceptron.

**10. (10 points) Neural Networks**

**(a) (2 pt)** Consider the (non-fully connected) neural network in Figure 2(a), where each node is assumed to have a bias input of constant value 1 that is not shown. Assume the inputs to A, B, C and the output Y are boolean (1 or 0). Could this network correctly classify each of the following logical operations? Briefly justify.

$$
(A \land B \land C) \lor (\neg A \land B \land C)
$$

A XOR B

Now assume we have the (non-fully connected) multi-class perceptron shown in Figure 2(b); here we assume no bias inputs. Such a perceptron returns as a prediction the label of the output node with the highest output value.

**(b) (4 pt)** Suppose we start with the weights [1, 1] for output S and the weights [0, 1] for output T and a learning rate of 1. Given the following example run one iteration of weight update.

$$
X _ {1} = - 1, X _ {2} = 0. 5, X _ {3} = 1, l a b e l = S
$$

<!-- page: 16 -->

**(c) (2 pt)** Independent of your answer to the previous problem, assume you arrived at the conclusion that the weights for S are [0, 2] and the weights for T are [-1, 0]. What is the condition on the inputs such that this network chooses S rather than T? Express the condition as simply as possible.

Many neural networks used in practice have weights that are shared across multiple connections. In the example below, there are two weights in the first layer, w<sub>1</sub> and w<sub>2</sub>, each of which appears twice.

![](images/page_15_image_3.jpg)

**(d) (1 pt)** What effect would you expect weight sharing to have on the training error?

It should go down

It should go up

Cannot tell given this information

It should go down

**(e) (1 pt)** What effect would you expect weight sharing to have on the test error?

It should go up
