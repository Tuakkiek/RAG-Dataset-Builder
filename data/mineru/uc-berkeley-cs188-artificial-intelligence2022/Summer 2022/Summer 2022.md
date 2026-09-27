<!-- page: 1 -->

## CS 188 Introduction to Summer 2022Artificial Intelligence

• You have approximately 170 minutes.

• The exam is closed book, no calculator, and closed notes, other than two double-sided "crib sheets" that you may reference.

• For multiple choice questions,

– □ or **[A]** means mark **all options** that apply

– # or (A) means mark a single choice

| First name |  |
| --- | --- |
| Last name |  |
| SID |  |
| Exam Room |  |
| Name and SID of person to the right |  |
| Name and SID of person to the left |  |
| Discussion TAs (or None) |  |

**Honor code**: “As a member of the UC Berkeley community, I act with honesty, integrity, and respect for others.”

By signing below, I affirm that all work on this exam is my own work, and honestly reflects my own understanding of the course material. I have not referenced any outside materials (other than two double-sided crib sheets), nor collaborated with any other human being on this exam. I understand that if the exam proctor catches me cheating on the exam, that I may face the penalty of an automatic "F" grade in this class and a referral to the Center for Student Conduct.

Signature:

Point Distribution

| Q1. Potpourri | 29 |
| --- | --- |
| Q2. Bayes Net and Sampling | 10 |
| Q3. College Indecision | 14 |
| Q4. Dynamic Bayes Net | 6 |
| Q5. Fair or Biased? | 6 |
| Q6. Reinforcement Learning | 12 |
| Q7. So Many Derivatives | 8 |
| Q8. Settlers of Catan | 15 |
| Total | 100 |

<!-- page: 2 -->

<!-- page: 3 -->

SID:

## Q1. [29 pts] Potpourri

**(a)** True or False

**(i)** [1 pt] The Value of Perfect Information (VPI) is always non-negative. **(True) (False)**

**(ii)** [1 pt] When we run Q-learning on a fixed dataset of (state, action, next state, reward) tuples once, it will always converge to the optimal Q-values. **(True) (False)**

**(iii)** [1 pt] Iterative deepening search is optimal when all the edge costs are identical. **(True) (False)**

**(iv)** [1 pt] The space complexity of depth-first search (DFS) is linear with regard to the size of the branching factor and the maximum depth of the search tree. **(True) (False)**

**(v)** [1 pt] When solving an HMM with states 𝑆 and evidence 𝐸, it is possible for variable elimination and the forward algorithm to reach different solutions for $P ( S _ { t } | E _ { 1 : t } )$ for some timestep 𝑡. **(True) (False)**

**(vi)** [1 pt] In a constraint satisfaction problem, if we wanted to prune the domain as much as possible before selecting values, we would use the LCV heuristic. **(True) (False)**

**(vii)** [1 pt] There exists an MDP such that value iteration does not converge for some states but policy iteration converges for all states. **(True) (False)**

**(viii)** [1 pt] Consider a Markov chain with transition probabilities $P ( X _ { t } | X _ { t - 1 } )$ . For two different initial distributions $P ( X _ { 0 } )$ , the stationary distributions (if they both exist) are guaranteed to be different. **(True) (False)**

**(ix)** [1 pt] In Bayes Nets, sampling methods usually have smaller memory requirements than exact inference methods (e.g. variable elimination). **(True) (False)**

**(x)** [1 pt] While using Naive Bayes with Laplace smoothing, we pick the value of smoothing strength 𝑘 based on accuracy on the training set. **(True) (False)**

**(b) (i)** [2 pts] Which of the following statements are correct about particle filtering?

**[A]** Both the forward algorithm and particle filtering can be used to calculate (or estimate) the probability $P ( X _ { t } | E _ { 1 : t } )$ for states $X _ { t }$ and evidence $E _ { 1 : t ^ { \star } }$

**[B]** With particle filtering, we often need more samples than likelihood weighting to achieve the same level of accuracy in the estimations.

**[C]** Particle filtering is often computationally less expensive than the forward algorithm.

**[D]** In particle filtering, after we re-sample the particles, the weights of the particles remain unchanged.

**(E)** None of the above.

**(ii)** [2 pts] Which of the following are correct expressions?

**[A]** $MEU(e) = \max_{a} \sum_{s} P(s \mid e)U(s, a)$

**[B]** 𝑀 $\begin{array} { r } { I E U ( e , e ^ { \prime } ) = \operatorname* { m a x } _ { a } \sum _ { s } P ( s \mid e ) P ( s \mid e ^ { \prime } ) U ( s , a ) } \end{array}$

**[C]** $VPI(E' \mid e) = MEC(E' \mid e) - MEC(e)$

**[D]** $VPI(E' \mid e) = MEC(E') - MEC(e)$

**(E)** None of the above

**(c) (i)** [1 pt] While using Naive Bayes with Laplace smoothing, if the training error is low but validation error is much higher, which of the following should we do?

**(A)** Increase k **(B)** Decrease k

<!-- page: 4 -->

**(ii)** [2 pts] When running the Perceptron algorithm, adding a feature to the input of the model will never negatively affect its performance on which of the following datasets? **[A]** Training set **[B]** Validation set **[C]** Test set **(D)** None of the above

**(iii)** [2 pts] When using a neural network, if the training error is high, which of the following could help in decreasing the training error? **[A]** Increase the network’s size **[B]** Train on more data **[C]** Increase training time **[D]** Decrease the learning rate

**(d)** Assume that we are in a standard Pacman setting where Pacman’s goal is to eat all the food pellets while avoiding ghosts. Answer the following true/false questions.

**(i)** [1 pt] **(T) (F)** The position of the ghosts is part of the minimal state space for this problem.

**(ii)** [1 pt] **(T) (F)** There exists a state space formulation with all positive edge weights > 𝜖 > 0 for some constant 𝜖 where no heuristic would make 𝐴<sup>∗</sup>search optimal.

**(e)** Arvind goes to the casino one night and is playing the following game: Initially, there is \$1 in a pot. At every round, Arvind has two actions: (1) spend \$𝑅 to draw a card from a deck or (2) leave and take the money in the pot (thereby terminating the game). For the draw action, there is a 1/4 chance that the card drawn is a winning card which multiplies the amount of money in the pot by 10, else the money in the pot is reset to \$1 and the game continues. Once the pot reaches \$100, the game ends and Arvind receives \$100 in reward. In all subparts, use a discount value of 𝛾 = 1.

**(i)** [3 pts] For this part only, let 𝑅 = 1. What are the values of each state in value iteration for times 𝑡 = 1 and 𝑡 = 2? Note that 𝑆 represents the state where the center pot contains \$𝑖.

$$
(\mathbf {1}) V _ {1} (S _ {1}) = \boxed {\quad}
$$

$$
V _ {1} (S _ {1 0}) = \boxed {\quad}\tag{3}
$$

$$
V _ {1} (S _ {1 0 0}) = \boxed {\quad}
$$

$$
(4) V _ {2} (S _ {1}) = \boxed {\quad}
$$

$$
V _ {2} (S _ {1 0}) = \boxed {\quad}
$$

$$
V _ {2} (S _ {1 0 0}) = \boxed {\quad}
$$

**(ii)** [2 pts] Again using a discount value of 𝛾 = 1, for what value of 𝑅 will the agent be indifferent between taking the action draw or leave at state $S _ { 1 0 }$ at time 𝑡 = 2? In other words, determine the value of 𝑅 where $Q _ { 2 } ( S _ { 1 0 } , d r a w ) =$ $Q _ { 2 } ( S _ { 1 0 } , l e a v e )$

**(f) (i)** [1 pt] Which of the following models use a structured state representation? **[A]** Search **[B]** CSP **[C]** Bayes Net **[D]** MDP

**(ii)** [1 pt] Which of the following models assumes stochastic transitions? **[A]** Search **[B]** CSP **[C]** Bayes Net **[D]** MDP

**(iii)** [1 pt] Which of the following models assumes known physics?

**[A]** Search **[B]** CSP **[C]** Bayes Net **[D]** MDP

<!-- page: 5 -->

## Q2. [10 pts] Bayes Net and Sampling

**(a)** [2 pts] 𝐴, 𝐵, 𝐶 are discrete random variables. Given 𝐴 ⟂⟂ 𝐵|𝐶, which of the following equations must hold?

**[A]** $P ( A | B , C ) P ( B | A , C ) = P ( A , B | C )$

**[B]** $P(A,B,C)=P(A)P(B)P(A,B|C)$

**[C]** $\begin{array} { r } { P ( A | C ) = \frac { P ( A ) P ( C | A ) } { P ( C ) } } \end{array}$

**[D]** $P ( A , B | C ) = P ( A , B )$

**(E)** None of the above.

Consider the following Bayes Net involving binary random variables 𝐴, 𝐵, 𝐶, 𝐷. The relevant probability tables are given.

![](images/page_4_image_9.jpg)

<table><tbody><tr><td rowspan="3" colspan="4"></td><td>𝐴</td><td>𝐵</td><td>𝐶</td><td>𝑃(𝐶|𝐴,𝐵)</td><td rowspan="2" colspan="3"></td></tr><tr><td>0</td><td>0</td><td>0</td><td>0.6</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0.4</td><td>𝐵</td><td>𝐷</td><td>𝑃(𝐷|𝐵)</td></tr><tr><td colspan="2">𝑃(𝐴)</td><td colspan="2">𝑃(𝐵)</td><td>0</td><td>1</td><td>0</td><td>0.4</td><td>0</td><td>0</td><td>0.6</td></tr><tr><td>𝐴 = 0</td><td>0.5</td><td>𝐵 = 0</td><td>0.5</td><td>0</td><td>1</td><td>1</td><td>0.6</td><td>0</td><td>1</td><td>0.4</td></tr><tr><td>𝐴 = 1</td><td>0.5</td><td>𝐵 = 1</td><td>0.5</td><td>1</td><td>0</td><td>0</td><td>0.8</td><td>1</td><td>0</td><td>0.4</td></tr><tr><td rowspan="3" colspan="4"></td><td>1</td><td>0</td><td>1</td><td>?</td><td>1</td><td>1</td><td>0.6</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0.6</td><td rowspan="2" colspan="3"></td></tr><tr><td>1</td><td>1</td><td>0</td><td>0.4</td></tr></tbody></table>

**(b) (i)** [1 pt] Calculate $P ( C = 1 | A = 1 , B = 0 )$ (the ? entry in the table).

**(ii)** [1 pt] Calculate $P ( A = 1 | B = 0 , D = 1 )$

**(c)** Instead of calculating the exact quantity, suppose we want to estimate $P ( C = 1 | D = 1 )$ using different sampling methods.

**(i)** [1 pt] In this subpart we use rejection sampling. Which of the following is a valid topological order and is most efficient for rejection sampling to estimate $P ( C = 1 | D = 1 ) ?$

**(A)** $A , B , C , D$

**(B)** 𝐵, 𝐴, 𝐷, 𝐶

**(C)** 𝐵, 𝐷, 𝐴, 𝐶

**(D)** 𝐷, 𝐶, 𝐵, 𝐴

**(ii)** <u>[1 pt] In this subpart we u</u>se likelihood weighting. What is the weight of the sample $( A = 0 , B = 0 , C = 0 , D = 1 ) ?$

**(iii)** [2 pts] In this subpart we use Gibbs sampling. We initialize $A = 0 ,   B = 0 ,   C = 0 ,   D = 1$ , and choose to re-sample <u>𝐴. What is the probability that we still get 𝐴 = 0 after re-sampling?</u>

<!-- page: 6 -->

**(d)** [2 pts] We reverse the arrow between 𝐵 and 𝐷 to create a new Bayes Net (shown below).

![](images/page_5_image_1.jpg)

Which of the following statements are true?

**(A)** The set of joint distributions $P(A,B,C,D)$ that can be modeled by the two Bayes nets are the same.

**(B)** The set of joint distributions that can be modeled by the old Bayes net is a subset of the set of joint distributions that can be modeled by the new Bayes net.

**(C)** The set of joint distributions that can be modeled by the new Bayes net is a subset of the set of joint distributions that can be modeled by the old Bayes net.

**(D)** None of the above.

<!-- page: 7 -->

## Q3. [14 pts] College Indecision

**(a)** Pacman is paying to enter a lottery for summer classes, and his favorite class, CS 188, is among the 𝑛 possible classes. Without the lottery, 188 would cost \$10, and all other classes in the lottery cost \$1. Pacman is a rational agent, and his utility function is $U _ { 1 } ( \S x ) = x ^ { 2 }$ , where 𝑥 is the cost of the class that Pacman wins in the lottery.

**(i)** [2 pts] For this subpart only, Pacman would win 1 of 𝑛 possible classes in the lottery. What is the maximum amount of money he should pay to enter the lottery? You may leave your answer in terms of 𝑛.

**(ii)** [2 pts] For this subpart only, Pacman would now win 2 of 𝑛 possible classes in the lottery, and the total utility is the sum of the utility of each class. What is the new maximum amount of money he should pay to enter the lottery? You may leave your answer in terms of 𝑛.

**(b)** After taking summer classes, Pacman is deciding his major, which depends on what he finds meaningful (M) and how stressed he is (S). The amount he slept the night before (Z) influences how stressed he is.

**(i)** [2 pts] Select all of the decision networks that can represent Pacman’s decision.

![](images/page_6_image_7.jpg)

![](images/page_6_image_8.jpg)

![](images/page_6_image_9.jpg)

![](images/page_6_image_10.jpg)

**[A] [B] [C] [D]**

**(ii)** [3 pts] Pacman keeps track of how long he slept the night before $( Z = z ^ { \prime } )$ . Write out his new MEU as a function of the CPTs corresponding to the decision network.

<!-- page: 8 -->

![](images/page_7_image_1.jpg)

**(c)** For the following statements, select if they are always, sometimes, or never true.

**(i)** [1 pt] $\mathbf { V P I } ( \mathbf { S } ) \geq \mathbf { V P I } ( \mathbf { B } )$

**(A)** Always true

**(B)** Sometimes true

**(C)** Never true

**(ii)** [1 pt] $\mathrm { V P I ( Z | M ) + V P I ( Z | B ) \leq V P I ( Z | B , M ) }$

**(A)** Always true

**(B)** Sometimes true

**(C)** Never true

**(d)** [2 pts] Under which of the following conditions (considered independently) can we safely ignore 𝐶 when solving for the MEU?

**[A]** 𝐶 is not an evidence variable

**[B]** 𝐶 is an evidence variable

**[C]** 𝑀 is not an evidence variable

**[D]** 𝑀 is an evidence variable

**(E)** None

**(e)** [1 pt] The following question is unrelated to the decision network above. Consider the following lottery $L _ { 1 } = [ 0 . 5 , \S 2 ; 0 . 5 , \S 8 ]$ Indicate whether an agent with utility function $U _ { 2 } ( x )$ is risk-seeking, risk-neutral, or risk-averse on this lottery, where

$$
U _ {2} (x) = \left\{ \begin{array}{l l} 0 & \text {if} x <   0 \\ x ^ {2} & \text {if} 0 \leq x \leq 6 \\ 4 x + 1 2 & \text {if} x > 6 \end{array} \right.\tag{1}
$$

Recall that a lottery $L = [ p _ { 1 } , P _ { 1 } ; p _ { 2 } , P _ { 2 } ]$ represents a situation where Pacman receives prize $P _ { 1 }$ with probability $p _ { 1 }$ , and prize $P _ { 2 }$ with probability $p _ { 2 }$ .

**(A)** Risk-seeking

**(B)** Risk-neutral

**(C)** Risk-averse

<!-- page: 9 -->

## Q4. [6 pts] Dynamic Bayes Net

We are given the following dynamic Bayes net:

![](images/page_8_image_3.jpg)

**(a)** [2 pts] Which of the following conditional independence relations are correct?

**[A]** $X _ { t + 1 } \perp     \perp X _ { t - 1 } | X _ { t }$

**[B]** $F _ { t + 1 } \perp     \perp F _ { t - 1 } | F _ { t }$

**[C]** $E _ { t + 1 } \perp    \perp E _ { t - 1 } | E _ { t }$

**[D]** $M_{t+1} \perp M_{t-1} | M_t$

**(E)** None of the above

**(b)** [2 pts] Which of the following is the correct update rule for the elapse-time (prediction) update?

$$
P (X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}} P (x _ {t - 1}, X _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) \sum_ {m _ {t - 1}} P (m _ {t - 1}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1})
$$

$$
(X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}} P (x _ {t - 1}, m _ {t - 1} | f _ {1: t - 1}, e _ {1: t - 1}) P (M _ {t} | f _ {t - 1}, e _ {t - 1}) P (X _ {t} | x _ {t - 1}, Z _ {t - 1}) \tag {B}
$$

$$
P (X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}, m _ {t - 1}} P (x _ {t - 1}, m _ {t - 1} | e _ {t - 1}, f _ {t - 1}) P (M _ {t} | f _ {t - 1}) P (X _ {t} | M _ {t}, x _ {t - 1})
$$

$$
P (X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}, m _ {t - 1}} P (x _ {t - 1}, m _ {t - 1} | e _ {1: t - 1}, f _ {1: t - 1}) P (M _ {t} | f _ {t - 1}) P (X _ {t} | M _ {t}, x _ {t - 1})
$$

$$
P (X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}, m _ {t - 1}} P (x _ {t - 1}, m _ {t - 1} | e _ {1: t - 1}, f _ {1: t - 1}) P (X _ {t}, M _ {t} | m _ {t - 1}, x _ {t - 1}) P (X _ {t} | f _ {t - 1})
$$

$$
P (X _ {t}, M _ {t} | f _ {1: t - 1}, e _ {1: t - 1}) = \sum_ {x _ {t - 1}, m _ {t - 1}} P (x _ {t - 1}, m _ {t - 1} | e _ {1: t - 1}, f _ {1: t - 1}) P (m _ {t - 1} | f _ {t - 1}) P (X _ {t} | M _ {t}, x _ {t - 1})
$$

**(G)** None of the above.

**(c)** [2 pts] What is the correct update rule for the observation update? From the six options below, select the **minimum set** of options such that, after multiplying them and normalizing, gives $P ( X _ { t } , M _ { t } | f _ { 1 : t } , e _ { 1 : t } )$

**[A]** $P ( x _ { t - 1 } , m _ { t - 1 } | e _ { 1 : t - 1 } , f _ { 1 : t - 1 } )$

**[B]** $P ( f _ { t } | X _ { t } , M _ { t } )$

**[C]** $P ( e _ { t } | f _ { t } )$

**[D]** $P ( M _ { t } | f _ { t - 1 } )$

**[E]** $P ( X _ { t } | M _ { t } , x _ { t - 1 } )$

**[F]** $P ( X _ { t } , M _ { t } | f _ { 1 : t - 1 } , e _ { 1 : t - 1 } )$

**(G)** None of the above.

<!-- page: 10 -->

## Q5. [6 pts] Fair or Biased?

We have two indistinguishable coins. The fair coin (𝐹) has 0.5 probability for getting either heads or tails; the biased coin (𝐵) always gives tails.

Our friend Angela did 3 coin flips, each time with either the fair or the biased coin, but we do not know which. We use $C _ { t }$ $( t   =   1 , 2 , 3 )$ to represent the coin that Angela chooses for the $t ^ { \mathrm { t h } }$ coin flip. We do know, however, that Angela picks the fair or biased coin with equal probability for the first flip (i.e. $P ( C _ { 1 }   =   F )   =   P ( C _ { 1 }   =   B )   =   0 . 5 )$ , and chooses the coin at each subsequent timestep according to the following probability table:

| 𝐶<sub>𝑡</sub> | 𝐶<sub>𝑡+1</sub> | 𝑃(𝐶<sub>𝑡+1</sub>\|𝐶<sub>𝑡</sub>) |
| --- | --- | --- |
| 𝐹 | 𝐹 | 0.75 |
| 𝐹 | 𝐵 | 0.25 |
| 𝐵 | 𝐹 | 0.5 |
| 𝐵 | 𝐵 | 0.5 |

We also observe the outcomes of the flips to be **(Head, Tail, Tail)**. We want to use the Viterbi algorithm to infer the most likely sequence of coins that Angela picked to flip.

**(a)** [2 pts] Shown below is the full Trellis Diagram. Fill in the values for each labeled arc connecting $C _ { 1 }$ to $C _ { 2 }$ with the product of the transition probability and the observation likelihood at the second coin flip (as seen in lecture). Recall that the observation at timestep 1 is **Head** and observation at timestep 2 is **Tail**.

![](images/page_9_image_6.jpg)

**(ii)** B:

**(b)** [2 pts] What is the most likely sequence of coin<u>s? Your answer should b</u>e a 3-character string, e.g. "BBF" means the first two coin flips are biased while the third is fair.

**(c)** [2 pts] Which of the following is true about the Viterbi algorithm in general?

**[A]** The time complexity of Viterbi is linear with regard to the number of time steps.

**[B]** The time complexity of Viterbi is linear with regard to the size of the state space.

**[C]** The space complexity of Viterbi is linear with regard to the size of the state space.

**[D]** The Viterbi algorithm computes arg max $\begin{array} { r } { \mathfrak { t } _ { x _ { 1 : N } }   P ( e _ { 1 : N } | x _ { 1 : N } ) , } \end{array}$ , where 𝑥 are the states and 𝑒 are the observations.

**(E)** None of the above.

<!-- page: 11 -->

## Q6. [12 pts] Reinforcement Learning

**(a)** In the directed graph below, we formulate the problem of commuting in the Bay Area as a simple MDP, where the cities (nodes) represent the states, and the arrows represent possible actions. We will use the direction of the arrows in the graph, i.e., "up", "down", "left", and "right" to refer to the actions.

![](images/page_10_image_3.jpg)

**(i)** [2 pts] Let’s assume that the agent does not always succeed in every action, and we want to build an estimate of the transition function 𝑇̂ and reward function 𝑅̂ from data (for model-based reinforcement learning). The agent follows some policy 𝜋 to collect a dataset of (current state, action, next state, reward) tuples, as listed below.

| s | a | s' | Reward |
| --- | --- | --- | --- |
| San Francisco | up | Oakland | -4 |
| San Francisco | up | San Mateo | -3 |
| San Mateo | up | San Francisco | -5 |
| Oakland | down | San Francisco | -2 |
| San Francisco | up | San Mateo | -3 |
| San Francisco | right | San Mateo | -6 |

**(1)** What is 𝑇̂ (San Francisco, up, Oakland)?

**(2)** What is 𝑅̂(San Francisco, up, Oakland)?

**(ii)** [1 pt] We decide to use temporal difference learning instead to learn the values of 𝜋. Assume we start with the following values for each state:

| 𝑠 | Berkeley | Oakland | Hayward | Fremont | San Jose | San Francisco | San Mateo | Palo Alto |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑉<sup>𝜋</sup>(𝑠) | -2 | -8 | -7 | -3 | -1 | -2 | -6 | -1 |

We do one update step with the sample **(San Francisco, up, Oakland, -4)**. Assume discount factor 𝛾 = 0.9 and the learning rate 𝛼 = 0.5. What is the updated value of 𝑉<sup>𝜋</sup>(San Francisco)?

**(iii)** [2 pts] Which of the following are true about temporal difference learning and Q-learning?

**[A]** Q-learning can learn an optimal policy even if the dataset contains some sub-optimal actions.

**[B]** Q-learning is an on-policy algorithm.

**[C]** Temporal difference learning returns an optimal policy.

**[D]** Temporal difference learning often leads to faster convergence than direct evaluation.

**(E)** None of the above

<!-- page: 12 -->

**(iv)** [2 pts] We want to use an exploration function to give some preference to visiting less-visited state-action pairs. Which of the following exploration functions 𝑓 permit this behavior? Assume 𝑘 is some positive real number, $N ( s , a )$ represents the number of times that state-action pair $( s , a )$ has been taken, and 𝜖 is a very small number (say 0.0001) to avoid division by zero.

**[A]** $f ( s , a ) = k \cdot Q ( s , a )$

**[B]** $f ( s , a ) = k \cdot Q ( s , a ) \cdot N ( s , a )$

**[C]** $\begin{array} { r } { f ( s , a ) = Q ( s , a ) + \frac { k } { N ( s , a ) + \epsilon } } \end{array}$

**[D]** $f ( s , a ) = Q ( s , a ) + k \cdot N ( s , a )$

**[E]** $f ( s , a ) = Q ( s , a ) + k \cdot e ^ { - N ( s , a ) }$

**(F)** None of the above

**(b)** Recall the policy improvement step:

$$
\pi_ {i + 1} (s) = \arg \max _ {a} \sum_ {s ^ {\prime}} T (s, a, s ^ {\prime}) [ R (s, a, s ^ {\prime}) + \gamma V ^ {\pi_ {i}} (s ^ {\prime}) ]
$$

**(i)** [2 pts] Which of the following modifications to the reward value $R ( s , a , s ^ { \prime } )$ in the equation above will not affect the policy chosen in policy improvement? Note that we are still using the old unmodified reward $R ( s , a , s ^ { \prime } )$ during policy evaluation. Assume that 𝑘 is a real number and $k > 0$

**[A]** $R ( s , a , s ^ { \prime } ) + k$

**[B]** $R ( s , a , s ^ { \prime } ) - k$

**[C]** $k \cdot R ( s , a , s ^ { \prime } )$

**[D]** $R ( s , a , s ^ { \prime } ) / k$

**[E]** $R ( s , a , s ^ { \prime } ) ^ { k }$

**(F)** None of the above

**(ii)** [3 pts] Which of the following expressions below is equivalent to $V ^ { \pi _ { i } } ( s ^ { \prime } ) ?$ Assume that $0 < \alpha < 1$

**[A]** $Q ^ { \pi _ { i } } ( s ^ { \prime } , \pi ( s ^ { \prime } ) )$

**[B]** $\operatorname* { m a x } _ { a ^ { \prime } } Q ^ { \pi _ { i } } ( s ^ { \prime } , a ^ { \prime } )$

**[C]** $\begin{array} { r } { \sum _ { s ^ { \prime \prime } } T ( s ^ { \prime } , \pi ( s ^ { \prime } ) , s ^ { \prime \prime } ) [ R ( s ^ { \prime } , \pi ( s ^ { \prime } ) , s ^ { \prime \prime } ) + \gamma V ^ { \pi _ { i } } ( s ^ { \prime \prime } ) ] } \end{array}$

**[D]** $\begin{array} { r } { \operatorname* { m a x } _ { a ^ { \prime } } \sum _ { s ^ { \prime \prime } } T ( s ^ { \prime } , a ^ { \prime } , s ^ { \prime \prime } ) [ R ( s ^ { \prime } , a ^ { \prime } , s ^ { \prime \prime } ) + \gamma V ^ { \pi _ { i } } ( s ^ { \prime \prime } ) ] } \end{array}$

**[E]** $( 1 - \alpha ) \cdot V ^ { \pi _ { i } } ( s ^ { \prime } ) + \alpha \cdot [ R ( s ^ { \prime } , a ^ { \prime } , s ^ { \prime \prime } ) + \gamma V ^ { \pi _ { i } } ( s ^ { \prime \prime } ) ]$

**(F)** None of the above

<!-- page: 13 -->

## Q7. [8 pts] So Many Derivatives

Consider the neural network configuration below.

![](images/page_12_image_3.jpg)

**(a)** [2 pts] Which of the following decision boundaries can be learned by the neural network? Assume $w _ { 0 } , w _ { 1 } , x _ { 0 } , x _ { 1 } , T _ { a } \in \mathbb { R } ^ { n }$ and $z = w _ { 0 } x _ { 0 } + w _ { 1 } x _ { 1 }$ . Let $g ( z )$ be the binary step activation function with $T _ { a }$ as the decision threshold, which is defined as follows:

$$
g (z) = \left\{ \begin{array}{l} 1 \text {if} z \geq T _ {a} \\ 0 \text {if} z <   T _ {a} \end{array} \right.
$$

![](images/page_12_image_6.jpg)

**[A]** Graph A **[B]** Graph B **[C]** Graph C **[D]** Graph D **[E]** Graph E **(F)** None of the above

**(b)** Now let 𝑔(𝑧) be the sigmoid activation function and y be a real number value between 0 and 1 (we will ignore the threshold $T _ { a }$ for this part). Recall that the derivative of the sigmoid function is $\begin{array} { r } { \frac { \partial } { \partial z } g ( z ) = g ( z ) \cdot ( 1 - g ( z ) ) } \end{array}$ . You can represent your answers in terms of $x _ { 0 } , x _ { 1 } , w _ { 0 } , w _ { 1 } , z , \operatorname { o r } y$

**(i)** [2 pts] Calculate the following partial derivatives for backpropagation.

![](images/page_12_image_10.jpg)

<!-- page: 14 -->

**(ii)** [2 pts] Suppose we are running gradient **descent** on the neural network above. We are trying to minimize the upstream loss 𝐿 using learning rate 𝛼. Given the upstream gradient $\frac { \partial L } { \partial y }$ <sub>and</sub> the two partial derivatives that you computed in the previous part $( \frac { \partial y } { \partial z } \mathrm { ~ a n d ~ } \frac { \partial z } { \partial w _ { 0 } } )$ , determine the gradient descent update rule for $w _ { 0 }$

![](images/page_13_image_1.jpg)

**(c)** [2 pts] The Binary Perceptron is defined as the following:

$$
y = \text {classify} (x) = \left\{ \begin{array}{l l} + 1 & \text {if} w \cdot f (x) + b \geq 0 \\ - 1 & \text {if} w \cdot f (x) + b <   0 \end{array} \right.
$$

where 𝑤 is a vector of real-valued weights, $w \cdot f ( x )$ is the dot product $\textstyle \sum _ { i = 1 } ^ { m } w _ { i } f _ { i } ( x )$ where 𝑚 is the number of features, $f _ { i } ( x )$ is the 𝑖th feature of $x ,$ and 𝑏 is the bias.

Which of the following are true about the binary perceptron as defined above?

**[A]** It is possible that the perceptron learns a decision boundary that is nonlinear in terms of the features $f ( x )$

**[B]** It is possible that the perceptron learns a decision boundary that is nonlinear in terms of the data 𝑥.

**[C]** The perceptron algorithm is guaranteed to converge if the data is linearly separable.

**[D]** The perceptron algorithm is trained using gradient descent.

**(E)** None of the above

<!-- page: 15 -->

## Q8. [15 pts] Settlers of Catan

Sid, Perry, and Andrew are playing a board game. Each terminal state (leaf) has 2 values, $x _ { 1 }$ and $x _ { 2 }$

Each player has the following utilities:

• Sid’s utility function is $U _ { s } = + x _ { 1 }$

• Perry’s utility function is $U _ { p } = - x _ { 1 }$

• Andrew’s utility function is $U _ { a } = x _ { 2 } + r \cdot x _ { 1 }$ , where $0 < r < 1$

Consider the following game tree, with the upward-pointing triangle representing Sid, downwards-pointing triangle representing Perry, and the right-pointing triangle representing Andrew.

![](images/page_14_image_8.jpg)

**(a)** [1 pt] This is a zero-sum game. **(True) (False)**

**(b)** Let terminal state values be represented in the form $[ x _ { 1 } , x _ { 2 } ]$ . For this part only, assume the leaves $A   =   [ 3 , 1 0 ] , B   =$ [4, 5], $C = [ 6 , 6 ]$ and $D = [ 9 , 4 ]$

**(i)** [1 pt] If 𝑟 = 0.5, Which terminal state’s values will Q take on? **(A) (B) (C) (D)**

**(ii)** [2 pts] What value of 𝑟 would make Andrew indifferent between choosing left or right at node 𝑄?

| [A] | [B] | [C] | [D] | [E] | [F] | [G] | [H] | [I] | [J] | [K] | [L] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M] | [N] | [O] | [P] | (None) |  |  |  |  |  |  |  |

<!-- page: 16 -->

**(d)** [2 pts] Let $[ x _ { 1 , i } , x _ { 2 , i } ]$ represent the values at leaf node 𝑖. When Sid and Perry both act optimally according to their own utilities, for which of the following values of $x _ { 2 , i }$ does Andrew act as a maximizer for Sid? For this part, assume that the first value $x _ { 1 , i }$ for all leaf nodes 𝑖 is a positive real number.

**[A]** $x _ { 2 , i } = x _ { 1 , i } \; \forall i$

**[B]** $x _ { 2 , i } = x _ { 1 , i } ^ { 2 } \; \forall i$

**[C]** $x _ { 2 , i } = \sqrt { x _ { 1 , i } } \; \forall i$

**[D]** $\begin{array} { r } { x _ { 2 , i } = \frac { 1 } { x _ { 1 , i } } \; \forall i } \end{array}$

**(E)** None of the above

**(e)** Sid decides to run Monte-Carlo Tree Search to train an agent to play for him. He counts the rollouts and the number of favorable outcomes from each node. The current search tree is shown below. Note that the fractions at every node represent the win rates for Sid, the root maximizer. You may assume that Andrew never wins the game, so the complement of Sid’s win rate is Perry’s win rate.

As a reminder, the UCB heuristic is $\mathit { U C B } ( n ) = \frac { U ( n ) } { N ( n ) } + k \sqrt { l o g \frac { N ( \mathit { P A R E N T } ( n ) ) } { N ( n ) } }$ where $N ( n )$ is the number of rollouts at node $n , P A R E N T ( n )$ is the parent node of 𝑛, and $U ( n )$ the rollout utility (# wins) for the player at $P A R E N T ( n )$

![](images/page_15_image_8.jpg)

**(i)** [1 pt] If the MCTS algorithm ended now, which action would our agent choose? **(Left) (Right)**

**(ii)** [2 pts] If 𝑘 = 188 in our UCB heuristic, which node will be expanded next? **(A) (B) (C) (D) (E) (F) (G)**

**(iii)** [1 pt] In MCTS, a greater 𝑘 value incentivizes greater exploitation over exploration. **(True) (False)**

**(iv)** [1 pt] When using the UCB heuristic at a node $p ,$ if all child nodes of $p$ have the same utility 𝑈(𝑛), then the child node with largest 𝑁(𝑛) will be expanded in the rollout as long as $k > 0 .$ **(True) (False)**

<!-- page: 17 -->

**(a) (i)**

**(ii)**

**(iii)**

**(v)**

**(vi)**

**(vii)**

**(iv)**

**(x)**

**(ix)**

**(viii)**

**(b) (i)**

**(ii)**

**(c) (i)**

**(ii)**

**(iii)**

**(d) (i)**

**(e) (i) (1)**

**(4)**

**(2)**

**(5)**

**(3)**

**(6)**

**(ii)**

**(f) (i)**

**(ii)**

**(iii)**

**Q2**

**(a)**

**(b) (i)**

**(ii)**

**(c) (i)**

**(ii)**

**(iii)**

**(d)**

<!-- page: 18 -->

**(a) (i)**

**(ii)**

**(b) (i)**

**(ii)**

**(c) (i)**

**(d)**

**(e)**

**Q4**

**(a)**

**(b)**

**(c)**

**Q5**

**(a) (i)**

**(ii)**

**(iii)**

**(iv)**

<!-- page: 19 -->

**(b)**

**(c)**

**Q6**

**(a) (i) (1)**

**(2)**

**(ii)**

**(iii)**

**(iv)**

**(b) (i)**

**(ii)**

**Q7**

**(a)**

**(b) (i) (1)**

**(2)**

**(ii)**

**(c)**

**Q8**

**(a)**

**(b)**

**(ii)**

**(c)**

**(d)**

**(e) (i)**

**(ii)**

**(iii)**

**(iv)**

SID:
