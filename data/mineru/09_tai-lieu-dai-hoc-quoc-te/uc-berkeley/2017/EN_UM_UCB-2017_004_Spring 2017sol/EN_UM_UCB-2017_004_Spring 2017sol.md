<!-- page: 1 -->

• You have approximately 165 minutes (2 hours 45 minutes).

• The exam is closed book, closed calculator, and closed notes except your one-page crib sheet.

• Mark your answers ON THE EXAM ITSELF. If you are not sure of your answer you may wish to provide a brief explanation. All short answer sections can be successfully answered in a few sentences AT MOST.

• For multiple choice questions with circular bubbles, you should only mark ONE option; for those with checkboxes, you should mark ALL that apply (which can range from zero to all options)

| First name |  |
| --- | --- |
| Last name |  |
| edX username |  |

<table><tr><td colspan="2">For staff use only:</td></tr><tr><td>Total</td><td>/??</td></tr></table>

<!-- page: 2 -->

<!-- page: 3 -->

## Q1. [?? pts] Approximate Q-Learning

Consider the following MDP: We have infinitely many states $s \in \mathbb { Z }$ and actions $a \in \mathbb { Z } ,$ each represented as an integer. Taking action a from state s deterministically leads to new state $s ^ { \prime }   =   s + a$ and reward $r   =   s - a$ . For example, taking action 3 at state 1 results in new state $s ^ { \prime } = 1 + 3 = 4$ and reward $r = 1 - 3 = - 2$

We perform approximate Q-Learning, with features and initialized weights defined below.

| Feature | Initial Weight |
| --- | --- |
| f<sub>1</sub>ps,aq " s | w<sub>1</sub> " 1 |
| f<sub>2</sub>ps,aq " ´a<sup>2</sup> | w<sub>2</sub> " 2 |

(a) [?? pts] Write down $Q ( s , a )$ in terms of $w _ { 1 } ,   w _ { 2 } ,   s ,$ and a.

$$
Q (s, a) = w _ {1} * s - w _ {2} * a ^ {2}
$$

(b) [?? pts] Calculate $Q ( 1 , 1 )$ .

$$
Q (1, 1) = w _ {1} f _ {1} (1, 1) + w _ {2} f _ {2} (1, 1) = 1 * 1 - 2 * 1 ^ {2} = - 1
$$

(c) [?? pts] We observe a sample $( s , a , r , s ^ { \prime } )$ of $( 1 , 1 , 0 , 2 )$ Assuming a learning rate of $\alpha = 0 . 5$ and discount factor of $\gamma = 0 . 5$ , compute new weights after a single update of approximate Q-Learning.

$$
d i f f = (0 + 0. 5 * \max _ {a} Q (2, a)) - (- 1)
$$

$$
d i f f = (0. 5 \max _ {a} (2 - 2 * a ^ {2})) + 1
$$

$$
d i f f = (0. 5 (2 + 2 * \max _ {a} (- a ^ {2}))) + 1
$$

$$
d i f f = (0. 5 (2 + 2 * 0)) + 1
$$

$$
d i f f = 1 + 1 = 2
$$

w<sub>1</sub>: $\boxed{1 + 0.5 * 2 * 1 = 2}$

w<sub>2</sub>: $2+0.5*2*-1^{2}=1$

(d) [?? pts] Compute the new value for Q(1,1).

$$
\mathrm{Q} (1, 1) = \mathrm{w} _ {1} * 1 + w _ {2} - 1 ^ {2} = 2 * 1 + 1 * - 1 ^ {2} = 1
$$

<!-- page: 4 -->

## Q2. [?? pts] Who Spoke When

We are given a single audio recording (divided into equal and short time slots) and wish to infer when each person speaks. At every time step exactly one of N people is talking. This problem can be modeled using an HMM. Hidden variable $X _ { t } \in \{ 1 , 2 , . . . , N \}$ represents which person is talking at time step t.

(a) For this part, assume that at each time step:

• with probability $p ,$ the current speaker will continue to talk in the next time step.

• with probability $1 - p ,$ the current speaker will be interrupted by another person. Each other person is equally likely to be the interrupter.

Assume that $N = 3 .$

(i) [?? pts] Complete the Markov Chain below and write down the probabilities on each transition.

![](images/page_3_image_7.jpg)

![](images/page_3_image_8.jpg)

Self transitions for all states with probability p and all other transitions with probability $( 1 - p ) / 2$

(ii) [?? pts] What is the stationary probability distribution of this Markov chain? (Again, assume N “ 3).

$$
P (X _ {\mathrm{inf}} = 2) = \underline {{\quad 1 / 3}}
$$

$$
P (X _ {\mathrm{inf}} = 3) = \quad 1 / 3
$$

1{3 for each state, because of the symmetry.

(b) [?? pts] What is the number of parameters (or degrees of freedom) needed to model the transition probability $P ( X _ { t } | X _ { t - 1 } ) ?$ Assume N people in the meeting and arbitrary transition probabilities.

$N ( N - 1 ) \quad P ( X _ { t } | X _ { t - 1 } )$ is $N \times N$ and each row should sum to one. Significant partial credit will be given to the answer $N ^ { 2 }$

(c) [?? pts] Let’s remove the assumption that people are not allowed to talk simultaneously. Now, hidden state $\hat { X _ { t } \in \{ 0 , 1 \} ^ { N } }$ will be a binary vector of length N. Each element of the vector corresponds to a person, and whether they are speaking.

Now, what is the number of parameters (or degrees of freedom) needed for modeling the transition probability $P ( X _ { t } | X _ { t - 1 } ) ?$

<!-- page: 5 -->

$2 ^ { N } ( 2 ^ { N } - 1 )$ We have $2 ^ { N }$ different states so we need $2 ^ { N } ( 2 ^ { N } - 1 )$ or roughly $2 ^ { 2 N }$ parameters.

<!-- page: 6 -->

One way to decrease the parameter count is to assume independence. Assume that the transition probability between people is independent. The figure below represents this assumption for N “ 3, where $X _ { t } = \left[ X _ { t } ( 1 ) , X _ { t } ( 2 ) , X _ { t } ( 3 ) \right]$

![](images/page_5_image_1.jpg)

(d) [?? pts] Write the following in terms of conditional probabilities given from the Bayes Net. Assume N people in the meeting.

Transition Probability $P ( X _ { t } | X _ { t - 1 } )$

$$
P (X _ {t} | X _ {t - 1}) = \prod_ {n = 1} ^ {N} P (X _ {t} (n) | X _ {t - 1} (n))
$$

Emission Probability $P ( Y _ { t } | X _ { t } )$

$$
P (Y _ {t} | X _ {t}) = P (Y _ {t} | X _ {t} (1), \dots , X _ {t} (N))
$$

(e) [?? pts] What is the number of parameters (or degrees of freedom) needed for modeling transition probability $P ( X _ { t } | X _ { t - 1 } ) ?$ Assume N people in the meeting.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">We need to define a transition matrix for each person which requires 2 parameters and there are N people. Significant partial credit for answer 4N.</span></small>

<!-- page: 7 -->

## Q3. [?? pts] Naive Bayes

(a) We use a Naive Bayes classifier to differentiate between Pacmen and Ghosts, trained on the following:

| F<sub>1</sub> | F<sub>2</sub> | Y |
| --- | --- | --- |
| 0 | 1 | Ghost |
| 1 | 0 | Ghost |
| 0 | 0 | Pac |
| 1 | 1 | Pac |

![](images/page_6_image_3.jpg)

Assume that the distributions generated from these samples perfectly estimate the CPTs. Given features $f _ { 1 } , f _ { 2 }$ we predict $\hat { Y } \in \{ G h o s t , P a c m a n \}$ using the Naive Bayes decision rule. If $P ( Y = G h o s t | F _ { 1 } = f _ { 1 } , F _ { 2 } = f _ { 2 } ) = 0 . 5$ assign Ŷ based on flipping a fair coin.

(i) [?? pts] Compute the table $P ( { \hat { Y } } | Y )$

Value $P ( \hat { Y } = G h o s t | Y = G h o s t )$ is the probability of correctly classifying a Ghost, while $P ( \hat { Y } = P a c m a n | Y = G h o s t )$ is the probability of confusing a Ghost for a P acman.

<table><tbody><tr><td>PpYˆ|Yq</td><td>Yˆ " Ghost</td><td>Yˆ " Pacman</td></tr><tr><td rowspan="2">Y " Ghost</td><td rowspan="2">12</td><td rowspan="2">12</td></tr><tr></tr><tr><td rowspan="2">Y " Pacman</td><td rowspan="2">12</td><td rowspan="2">12</td></tr><tr></tr></tbody></table>

For each modification below, recompute table $P ( { \hat { Y } } | Y )$ . The modifications for each part are separate, and do not accumulate.

(ii) [?? pts] Add extra feature $F _ { 3 } = F _ { 1 } + F _ { 2 }$ , and modify the Naive Bayes classifier appropriately.

| PpYˆ\|Yq | Yˆ " Ghost | Yˆ " Pacman |
| --- | --- | --- |
| Y " Ghost | 1 | 0 |
| Y " Pacman | 0 | 1 |

(iii) [?? pts] Add extra feature $F _ { 3 } = F _ { 1 } \times F _ { 2 }$ , and modify the Naive Bayes classifier appropriately.

<table><tbody><tr><td>PpYˆ|Yq</td><td>Yˆ " Ghost</td><td>Yˆ " Pacman</td></tr><tr><td>Y " Ghost</td><td>1</td><td>0</td></tr><tr><td rowspan="2">Y " Pacman</td><td rowspan="2">12</td><td rowspan="2">12</td></tr><tr></tr></tbody></table>

<!-- page: 8 -->

(iv) [?? pts] Add extra feature $F _ { 3 } = F _ { 1 } - F _ { 2 }$ , and modify the Naive Bayes classifier appropriately.

| PpYˆ\|Yq | Yˆ " Ghost | Yˆ " Pacman |
| --- | --- | --- |
| Y " Ghost | 1 | 0 |
| Y " Pacman | 0 | 1 |

(v) [?? pts] Perform Laplace Smoothing with $k = 1$

<table><tbody><tr><td>PpYˆ|Yq</td><td>Yˆ " Ghost</td><td>Yˆ " Pacman</td></tr><tr><td rowspan="2">Y " Ghost</td><td rowspan="2">12</td><td rowspan="2">12</td></tr><tr></tr><tr><td rowspan="2">Y " Pacman</td><td rowspan="2">12</td><td rowspan="2">12</td></tr><tr></tr></tbody></table>

(b) [?? pts] Now, we reformulate the Naive Bayes classifier so that it can choose more than one class. For example, if we are choosing which genre a book is, we want the ability to say that a romantic comedy is both a romance and a comedy.

To do this, we have multiple label nodes $Y = \{ Y _ { 1 } . . . Y _ { n } \}$ which all point to all features $F = \{ F _ { 1 } . . . F _ { m } \}$

![](images/page_7_image_6.jpg)

Select all of the following expressions which are valid Naive Bayes classification rules, i.e., equivalent to arg max $_ { Y _ { 1 } . . . Y _ { n } } P ( Y _ { 1 } , Y _ { 2 } , . . . , Y _ { n } | F _ { 1 } , F _ { 2 } , . . . , F _ { m } )$ :

$$
\square \arg \max _ {Y _ {1} \dots Y _ {n}} \prod_ {i} ^ {n} \left[ P (Y _ {i}) \prod_ {j} ^ {m} P (F _ {j} | Y _ {i}) \right]
$$

$$
\square \arg \max _ {Y _ {1} \dots Y _ {n}} \prod_ {i} ^ {n} \left[ P (Y _ {i}) \prod_ {j} ^ {m} P (F _ {j} | Y _ {1} \dots Y _ {n}) \right]
$$

$$
\arg \max _ {Y _ {1} \dots Y _ {n}} \prod_ {i} ^ {n} \left[ P (Y _ {i}) \right] \prod_ {j} ^ {m} \left[ P (F _ {j} | Y _ {1} \dots Y _ {n}) \right]
$$

$$
\square \quad \prod_ {i} ^ {n} \left[ \arg \max _ {Y _ {i}} \left\{P (Y _ {i}) \prod_ {j} ^ {m} P (F _ {j} | Y _ {i}) \right\} \right]
$$

$$
\square \prod_ {i} ^ {n} \left[ \arg \max _ {Y _ {i}} \left\{P (Y _ {i}) \prod_ {j} ^ {m} P (F _ {j} | Y _ {1}... Y _ {n}) \right\} \right]
$$

<!-- page: 9 -->

## Q4. [?? pts] Tracking a cyclist

We are trying to track cyclists as they move around a self-driving car. The car is equipped with 4 “presence detectors” corresponding to:

• Front of the car (F),

• Back of the car (B),

• Left side of the car (L),

• Right side of the car (R).

![](images/page_8_image_6.jpg)

Figure 1: Autonomous vehicle and detection zones

Unfortunately, the detectors are not perfect and feature the following conditional probabilities for detection $D \in \{ 0 , 1 \}$ (“no detection” or “detection”, respectively) given cyclist presence $C \in \{ 0 , 1 \}$ (“no cyclist” or “cyclist”, respectively).

Front detector

| P<sub>F</sub>pD\|Cq | d " 1 | d " 0 |
| --- | --- | --- |
| c " 1 | 0.8 | 0.2 |
| c " 0 | 0.1 | 0.9 |

Back detector

| P<sub>B</sub>pD\|Cq | d " 1 | d " 0 |
| --- | --- | --- |
| c " 1 | 0.6 | 0.4 |
| c " 0 | 0.4 | 0.6 |

Left & Right detectors

| P<sub>L</sub>pD\|Cq " P<sub>R</sub>pD\|Cq | d " 1 | d " 0 |
| --- | --- | --- |
| c " 1 | 0.7 | 0.3 |
| c " 0 | 0.2 | 0.8 |

(a) Detection and dynamics

(i) [?? pts] If you could freely choose any detector to equip all four detection zones, which one would be best?

The front detector. # The detector at the back. # The left/right detector.

The front detector features the confusion matrix most concentrated on the diagonal.

Dynamics: We have measured the following transition probabilities for cyclists moving around the car when driving. Assume any dynamics are Markovian. Variable $X _ { t } \in \{ f , l , r , b \}$ denotes the location of the cyclist at time t, and can be in front, left, right, or back of the car.

| PpX<sub>t</sub>`1\|X<sub>t</sub>q | X<sub>t</sub>`1 " f | X<sub>t</sub>`1 " l | X<sub>t</sub>`1 " r | X<sub>t</sub>`1 " b |
| --- | --- | --- | --- | --- |
| X<sub>t</sub> " f | pff | pfl | pfr | pfb |
| X<sub>t</sub> " l | plf | p<sub>ll</sub> | p<sub>lr</sub> | p<sub>lb</sub> |
| X<sub>t</sub> " r | prf | p<sub>rl</sub> | p<sub>rr</sub> | p<sub>rb</sub> |
| X<sub>t</sub> " b | pbf | p<sub>bl</sub> | p<sub>br</sub> | p<sub>bb</sub> |

(ii) [?? pts] Which criterion does this table have to satisfy for it to be a well defined CPT? (Select all that apply).

 Each row should sum to 1. l Each column should sum to 1. l The table should sum to 1.

<!-- page: 10 -->

(b) Let’s assume that we have been given a sequence of observations $d _ { 1 } , d _ { 2 } , \ldots , d _ { t }$ and computed the posterior probability $P ( X _ { t } | d _ { 1 } , d _ { 2 } , \ldots , d _ { t } )$ , which we represent as a four-dimensional vector.

(i) [?? pts] What is vector $P ( X _ { t + 1 } | d _ { 1 } , d _ { 2 } , \ldots , d _ { t } )$ as a function of $P ( X _ { t + 1 } | X _ { t } )$ (a 4 ˆ 4 matrix written above) and $P ( X _ { t } | d _ { 1 } , d _ { 2 } , \ldots , d _ { t } ) ?$

$$
\frac {P (X _ {t + 1} | D _ {1} , D _ {2} , \dots , D _ {t}) = P (X _ {t + 1} | X _ {t}) ^ {T} \times P (X _ {t} | D _ {1} , D _ {2} , \dots , D _ {t})}{\text {or} P (X _ {t + 1} | D _ {1} , D _ {2} , \dots , D _ {t}) = \sum_ {x _ {t}} P (X _ {t + 1} | X _ {t} = x _ {t}) \times P (X _ {t} = x _ {t} | D _ {1} , D _ {2} , \dots , D _ {t})}
$$

(ii) [?? pts] What is the computational complexity of computing $P ( X _ { t } | D _ { 1 } { = } d _ { 1 } , D _ { 2 } { = } d _ { 2 } , \ldots , D _ { t } { = } d _ { t } )$ as a function of t and the number of states S (using big O notation)?

$$
O (t \times S ^ {2}).
$$

Detailed solution: At each time step of the forward algorithm, we need to multiply a vector of size S by a matrix of size $S ^ { 2 }$ to account for the dynamics entailed in $P ( X _ { t + 1 } | X _ { t } )$

Then, we need to compute the emission probability of each state which here costs $2 \times S$ and normalize (complexity is S). Therefore, the cost of propagating beliefs forward in time through the dynamics dominates as a function of S and is $O ( S ^ { 2 } )$ for each time step. Hence the final answer.

(c) (i) [?? pts] We now add a radar to the system (random variable $E \in \{ f , l , r , b \} )$ . Assuming the detection by this device is independent from what happens with the pre-existing detectors, which of the probabilistic models could you use? If several variables are in the same node, the node represents a tuple of random variables, which itself is a random variable.

![](images/page_9_image_8.jpg)

![](images/page_9_image_9.jpg)

![](images/page_9_image_10.jpg)

![](images/page_9_image_11.jpg)

Select all that apply.

 a)  b) l c)  d)

(ii) [?? pts] ERRATUM: Which of the following values for Z are correct?

$$
P (X _ {t + 1} | D _ {1}, \dots , D _ {t + 1}, E _ {1}, \dots , E _ {t + 1}) = \sum_ {x = f, l, r, b} \frac {Z \cdot P (X _ {t} = x | D _ {1} , \dots , D _ {t} , E _ {1} , \dots , E _ {t}) \cdot P (X _ {t + 1} | X _ {t} = x)}{P (D _ {t + 1} , E _ {t + 1} | D _ {1} , \dots , D _ {t} , E _ {1} , \dots , E _ {t})}.
$$

$$
Z = P (E _ {t + 1} D _ {t + 1} | X _ {t + 1}, X _ {t}, D _ {1}, \dots , D _ {t + 1}, E _ {1}, \dots , E _ {t + 1})
$$

$$
Z = P (E _ {t + 1} | X _ {t + 1}) P (D _ {t + 1} | X _ {t + 1})
$$

$$
\square Z = P (E _ {t + 1} | X _ {t}) P (D _ {t + 1} | X _ {t})
$$

<!-- page: 11 -->

$$
\begin{array}{l l} \square & Z = P (E _ {t + 1} | E _ {t}) P (D _ {t + 1} | D _ {t}) \\ \blacksquare & Z = P (E _ {t + 1}, D _ {t + 1} | X _ {t + 1}) \\ \square & Z = P (E _ {t + 1}, D _ {t + 1} | X _ {t}) \\ & \\ & P (X _ {t + 1} | D _ {1}, \ldots , D _ {t + 1}, E _ {1}, \ldots , E _ {t + 1}) \\ & \quad = \frac {P (X _ {t + 1} , D _ {t + 1} , E _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})}{P (D _ {t + 1} , E _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})} \\ & \quad = \frac {P (D _ {t + 1} , E _ {t + 1} | X _ {t + 1} , D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t}) P (X _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})}{P (D _ {t + 1} , E _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})} \\ & \quad = \frac {{P (D _ {t + 1} | X _ {t + 1}) P (E _ {t + 1} | X _ {t + 1}) \sum_ {x} P (X _ {t + 1} | X _ {t} = x , D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t}) P (X _ {t} = x | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})}}{P (D _ {t + 1} , E _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})} \\ & \quad = \frac {{P (D _ {t + 1} | X _ {t + 1}) P (E _ {t + 1} | X _ {t + 1}) \sum_ {x} P (X _ {t + 1} | X _ {t} = x) P (X _ {t} = x | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})}}{P (D _ {t + 1} , E _ {t + 1} | D _ {1} , \ldots , D _ {t} , E _ {1} , \ldots , E _ {t})} \end{array}
$$

<!-- page: 12 -->

Consider the following MDP:

![](images/page_11_image_2.jpg)

The state space $\mathcal { S }$ and action space $\mathcal { A }$ are

$$
\mathcal {S} = \{A, B, T \}
$$

$$
\mathcal {A} = \{\text {left, right} \}
$$

where $T$ denotes the terminal state (both T states are the same). When in a terminal state, the agent has no more action and gets no more reward. In non-terminal states, the agent can only go left or right, but their action only succeeds (goes in the intended direction) with probability p. If their action fails, then they go the opposite direction. The numbers on the arrows denote the reward associated with going from one state to another.

For example, at state A taking action left:

• with probability $p ,$ the next state will be T and the agent will get a reward of 8. The episode is then terminated.

• with probability $1 - p ,$ the next state will be B and the reward will be 2.

For this problem, the discount factor $\gamma$ is 1. Let $\pi_{p}^{*}$ be the optimal policy, which may or may not depend on the value of $p .$ Let $Q ^ { \pi _ { p } ^ { * } }$ and $V ^ { \pi _ { p } ^ { * } }$ be the corresponding $Q$ and V functions of $\pi_{p}^{*}$

(a) [?? pts] If $[ p = 1$ , what is $\pi _ { p } ^ { * \gamma }$ (Select one)

$$
\bigcirc \quad \pi_ {p} ^ {*} (A) = \text {left} \quad , \quad \pi_ {p} ^ {*} (B) = \text {left}
$$

$$
\bigcirc \quad \pi_ {p} ^ {*} (A) = \text {left} \quad , \quad \pi_ {p} ^ {*} (B) = \text {right}
$$

$$
\pi_ {p} ^ {*} (A) = \text {right}, \pi_ {p} ^ {*} (B) = \text {left}
$$

$$
\bigcirc \quad \pi_ {p} ^ {*} (A) = \text {right}, \quad \pi_ {p} ^ {*} (B) = \text {right}
$$

The optimal policy just goes back and forth between A and B getting infinite points.

(b) [?? pts] If p “ 0, what is $\pi _ { p } ^ { * } ( A ) ?$ (Select one)

$$
\bigcirc \quad \pi_ {p} ^ {*} (A) = \text {left} \quad , \quad \pi_ {p} ^ {*} (B) = \text {left}
$$

$$
\pi_ {p} ^ {*} (A) = \text {left}, \pi_ {p} ^ {*} (B) = \text {right}
$$

$$
\bigcirc \quad \pi_ {p} ^ {*} (A) = \text {right} \quad , \quad \pi_ {p} ^ {*} (B) = \text {left}
$$

$$
\bigcirc \pi_ {p} ^ {*} (A) = \mathbf {r i g h t}, \pi_ {p} ^ {*} (B) = \mathbf {r i g h t}
$$

Since $p = 0 ,$ it’s the same as $p = 1$ but you just need to take the opposite action.

<!-- page: 13 -->

(c) [?? pts] Suppose $\pi _ { p } ^ { * } ( A ) = \mathtt { l e f t }$ . Which of the following statements must be true? (Select all that apply) Hint: Don’t forget that if $x = y$ , then $x \geqslant y$ and $x \leqslant y .$

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\begin{array}{l}\square\\ \hline Q^{\pi_{p}^{*}}(A,\text{left})\leqslant Q^{\pi_{p}^{*}}(A,\text{right})\\ \hline Q^{\pi_{p}^{*}}(A,\text{left})\geqslant Q^{\pi_{p}^{*}}(A,\text{right})\\ \hline Q^{\pi_{p}^{*}}(A,\text{left}) = Q^{\pi_{p}^{*}}(A,\text{right})\\ \hline V^{\pi_{p}^{*}}(A)\leqslant V^{\pi_{p}^{*}}(B)\\ \hline V^{\pi_{p}^{*}}(A)\geqslant V^{\pi_{p}^{*}}(B)\\ \hline V^{\pi_{p}^{*}}(A) = V^{\pi_{p}^{*}}(B)\\ \hline V^{\pi_{p}^{*}}(A)\leqslant Q^{\pi_{p}^{*}}(A,\text{left})\\ \hline V^{\pi_{p}^{*}}(A)\geqslant Q^{\pi_{p}^{*}}(A,\text{left})\\ \hline V^{\pi_{p}^{*}}(A) = Q^{\pi_{p}^{*}}(A,\text{left})\\ \hline V^{\pi_{p}^{*}}(A)\leqslant Q^{\pi_{p}^{*}}(A,\text{right})\\ \hline V^{\pi_{p}^{*}}(A)\geqslant Q^{\pi_{p}^{*}}(A,\text{right})\\ \hline V^{\pi_{p}^{*}}(A) = Q^{\pi_{p}^{*}}(A,\text{right})\end{array}$
</div>

For left to be the optimal action, it must be the case that $Q ^ { \pi _ { p } ^ { * } } ( A , \mathtt { l e f t } ) \geqslant Q ^ { \pi _ { p } ^ { * } } ( A , \mathtt { r i g h t } )$ . Therefore, we also get that $V ^ { \pi _ { p } ^ { * } } ( A ) { = } \operatorname { m a x } _ { a } Q ^ { \pi _ { p } ^ { * } } ( A , a ) { = } Q ^ { \pi _ { p } ^ { * } } ( A , { \tt l e f t } )$ . Also, it’s always the case that $V ^ { \pi _ { p } ^ { * } } ( A ) { \geqslant } V ^ { \pi _ { p } ^ { * } } ( B )$ for this problem.

(d) Assume $p \geqslant 0 . 5$ below.

(i) [?? $\mathrm{pts]} V^{*}(B)=\alpha V^{*}(A)+\beta$ . Find α and $\beta$ in terms of $p .$

$$
\bullet \quad \alpha = \underline {{\quad \mathrm{p}}} \quad
$$

$$
\bullet \beta = \underline {{\quad 0}}
$$

since $p \geqslant 0.5,$ it’s always optimal to go left from B. So

$$
V ^ {*} (B) = Q ^ {*} (B, \text {left}) = p (0 + V ^ {*} (A)) + (1 - p) (0 + V ^ {*} (T)) = p V ^ {*} (A)
$$

(ii) [?? pts] $Q ^ { \pi _ { p } ^ { * } } ( A , \mathtt { l e f t } ) = \alpha V ^ { * } ( B ) + \beta$ . Find α and $\beta$ in terms of $p .$

$$
\bullet \beta = \underline {{\quad 2 + 6 \mathrm{p}\quad}}
$$

$$
\begin{array}{c} Q ^ {\pi_ {p} ^ {*}} (A, \textbf {l e f t}) = p (8 + V ^ {*} (T)) + (1 - p) (2 + V ^ {*} (B)) \\ = (1 - p) V ^ {*} (B) + 2 + 6 p \end{array}
$$

(iii) [?? pts] $Q ^ { \pi _ { p } ^ { * } } ( A , \mathtt { r i g h t } ) = \alpha V ^ { * } ( B ) + \beta$ . Find α and $\beta$ in terms of $p .$

• β “ 8 ´ 6p

$$
\begin{array}{c} Q ^ {\pi_ {p} ^ {*}} (A, \text {right}) = (1 - p) (8 + V ^ {*} (T)) + p (2 + V ^ {*} (B)) \\ = p V ^ {*} (B) + 8 - 6 p \end{array}
$$

<!-- page: 14 -->

<!-- page: 15 -->

## Q6. [?? pts] Take Actions

An agent is acting in the following gridworld MDP, with the following characteristics.

• Discount factor $\gamma < 1$

• Agent gets reward $R > 0$ for entering the terminal state T, and 0 reward for all other transitions.

• When in terminal state T, the agent has no more action and gets no more reward.

• In non-terminal states tA, B, Cu, the agent can take an action $\{ U p , D o w n , L e f t , R i g h t \}$

• Assume perfect transition dynamics. For example, taking action Right at state A will always result in state C in the next time step.

• If the agent hits an edge, it stays in the same state in the next time step. For example, after taking action Right at C, the agent remains in state C.

| B | T |
| --- | --- |
| A | C |

(a) (i) [?? pts] What are all the optimal deterministic policies? Each cell should contain a single action $\{ U p , D o w n , L e f t , R i g h t \}$ . Each row corresponds to a different optimal policy. You may not need all rows.

| State | A | B | C |
| --- | --- | --- | --- |
| Optimal policy 1 | Up | Right | Up |
| Optimal policy 2 (if needed) | Right | Right | Up |
| Optimal policy 3 (if needed) |  |  |  |

(ii) [?? pts] Suppose the agent uniformly randomly chooses between the optimal policies in (i). In other words, at each state, the agent picks randomly between the actions in the corresponding column with equal probability. The agent’s location at each time step is then a Markov process where state $X _ { t } \in \{ A , B , C , T \}$ Fill in the following transition probabilities for the Markov process.

$$
\bullet P (X _ {t + 1} = B | X _ {t} = A) = \underline {{\quad 0 . 5}}
$$

$P ( X _ { t + 1 } = A | X _ { t } = B ) = \frac { 0 } { \hphantom { 0 } }$

$P ( X _ { t + 1 } = T | X _ { t } = C ) = \underline { { \hphantom { \frac { 1 } { 1 } } \hphantom { \frac { 1 } { 1 } } 1 } }$

<!-- page: 16 -->

(b) Suppose the agent is acting in the same gridworld as above, but does not get to observe their exact state $X _ { t } .$ Instead, the agent only observes $O _ { t } \in \{ b l a c k , g r e e n , p i n k \}$ . The observation probability as a function of the state $P ( O _ { t } | X _ { t } )$ is specified in the table below. This becomes a partially-observable Markov decision process (POMDP). The agent is equally likely to start in non-terminal states $\{ A , B , C \}$

| B0.5, black0.5, green | T |
| --- | --- |
| A0.5, black0.5, pink | C0.5, pink0.5, green |

(i) [?? pts] If the agent can only act based on its current observation, what are all deterministic optimal policies? You may not need all rows.

|  | Black | Green | Pink |
| --- | --- | --- | --- |
| Optimal policy 1 | Right | Right | Up |
| Optimal policy 2 (if needed) | Right | Up | Up |
| Optimal policy 3 (if needed) |  |  |  |

(ii) [?? pts] Suppose that the agent follows the policy πpBlack**q “** Right, πpGreenq “ Right, and $\pi { \big ( } { \mathrm { P i n k } } { \big ) } = U p .$ Let V pSq be the agent’s expected reward from state S. Your answer should be in terms of γ and R. Note that V pSq is the expected value before we know the observation, so you must consider all possible observations at state S.

$$
\bullet \mathrm{V(A)} = \gamma (\frac {1}{2} R + \frac {1}{2} (\frac {R}{2 - \gamma}))
$$

• V(B) = R

• V(C) = R 2´γ

V pB**q “** R because we always go right in state B.

$$
V (C) = \frac {1}{2} R + \frac {1}{2} \gamma V (C) \implies V (C) = \frac {R}{2 - \gamma}.
$$

$$
V (A) = \gamma (\frac {1}{2} V (B) + \frac {1}{2} V (C))
$$

Now suppose that the agent’s policy can also depend on all past observations and actions. Assume that when the agent is starting (and has no past observations), it behaves the same as the policy in the previous part: $\pi([\mathrm{Black}]) = \mathrm{Right}, \pi([\mathrm{Green}]) = \mathrm{Right}, \pi([\mathrm{Pink}]) = \mathrm{Up}$ . In all cases where the agent has more than one observation (for example, observed Pink in the previous time step and now observes Green), π acts optimally.

(iii) [?? pts] For each of the following sequences of two observations, write the optimal action that the policy π would take.

| Black Pink | Black Green | Green Pink | Green Green | Pink Black | Pink Green |
| --- | --- | --- | --- | --- | --- |
| Up | Up | Up | Up | Right | Right |

<!-- page: 17 -->

(iv) [?? pts] In this part only, let V pSq refer to the expected sum of discounted rewards following π if we start from state S (and thus have no previous observations yet). As in the previous part, this is the expected value before knowing the observation, so you must consider all possible observations at S.

Hint: since π now depends on sequences of observations, the way we act at states after the first state may be different, and this affects the value at the first state.

• V(A) = γR

• V(B) = R

$$
\bullet \mathrm{V(C)} = \underline {{\frac {1}{2} (1 + \gamma) R}}
$$

(c) Boba POMDP May is a venture capitalist who knows that Berkeley students love boba. She is picking between investing in Sharetea or Asha. If she invests in the better one, she will make a profit of \$1000. If she invests in the worse one, she will make no money.

At the start, she believes both Asha and Sharetea have an equal chance of being better. However, she can pay to have students taste test. At each time step, she can either choose to invest or to pay for a student taste test. Each student has a $p = 0 . 9$ probability of picking the correct place (independent of other students).

(i) [?? pts] What is the expected profit if May invests optimally after one (free) student test?

(ii) [?? pts] If she had to invest after one student test, what is the highest May should pay for the test? 400

(iii) [?? pts] Suppose after n student tests, it turns out that all students have chosen the same store. What is her expected profit after after observing these n student tests?

\# 1000p0.9n<sub>q</sub>

$\begin{array} { r l } { 1 0 0 0 ( \frac { \stackrel { \cdot } { 0 . 9 ^ { n } } } { 0 . 9 ^ { n } + 0 . 1 ^ { n } } ) } \\ \end{array}$

$1 0 0 0 ( 0 . 9 ^ { n } - 0 . 1 ^ { n } )$

$\begin{array} { r } { 1 0 0 0 ( \frac { \dot { 0 } . 9 ^ { n } - 0 . 1 ^ { n } } { 0 . 9 ^ { n } } ) } \end{array}$

$\textstyle 1 0 0 0 ( \frac { 0 . 9 ^ { \hat { n } } - 0 . 1 ^ { n } } { 0 . 9 ^ { n } + 0 . 1 ^ { n } } )$

$1 0 0 0 ( 1 - 0 . 1 ^ { n } )$

(iv) [?? pts] How many tests should May pay for if each one costs \$100? Hint: Think about the maximum possible value of information. How does this compare to the expected value of information?

<!-- page: 18 -->

## Q7. [?? pts] Graph Search

You are trying to plan a road trip from city A to city B. You are given an undirected graph of roads of the entire country, together with the distance along each road between any city X and any city Y : lengthpX, Y q (For the rest of this question, ”shortest path” is always in terms of length, not number of edges). You would like to run a search algorithm to find the shortest way to get from A to B (assume no ties).

Suppose C is the capital, and thus you know the shortest paths from city C to every other city, and you would like to be able to use this information.

Let $p a t h _ { o p t } ( X \to Y )$ denote the shortest path from X to Y and let costpX, Y q denote the cost of the shortest path between cities X and Y . Let $[ p a t h ( X \to \tilde { Y } ) , p a t h ( Y \to Z ) ]$ denote the concatenation.

(a) [?? pts] Suppose the distance along any edge is 1. You decide to initialize the queue with A, plus a list of all cities X, with path $\iota ( A \to X ) = [ p a t h _ { o p t } ( A \to C ) , p a t h _ { o p t } ( C \to X ) ]$ . You run BFS with this initial queue (sorted in order of path length). Which of the following is correct? (Select all that apply)

l You always expand the exact same nodes as you would have if you ran standard BFS.

l You might expand a different set of nodes, but still find the shortest path.

 You might expand a different set of nodes, and find the sub-optimal path.

Consider a graph of 5 nodes: A,B,C,D,E and edges (A,C), (C,E), (E,B), (A,D),(D,B). Then our initial queue (in order) is

1. C: A-C

2. E: A-C-E

3. B: A-C-E-B

4. D: A-C-A-D

The path returned will be A-C-E-B

(b) [?? pts] You decide to initialize priority queue with A, plus a list of all cities X, with $p a t h ( A \; \rightarrow \; X ) \; = \;$ $\big [ \widetilde { p a t h _ { o p t } ( A \to C ) } , p a t h _ { o p t } ( C \to X ) \big ]$ , and cos $t ( A , X ) = c o s t ( A , C ) + c o s t ( C , X )$ . You run UCS with this initial priority queue. Which of the following is correct? (Select all that apply)

 You always expand the exact same nodes as you would have if you ran standard UCS.

l You might expand a different set of nodes, but still find the shortest path.

l You might expand a different set of nodes, and find the sub-optimal path.

Regardless of what is on the queue, UCS will explore nodes in order of their shortest-path distance to A, so the set of explored nodes is always {nodes X: dist(A,X) less than dist(A,B)}

<!-- page: 19 -->

## Q8. [?? pts] Bayes Net Inference

A plate representation is useful for capturing replication in Bayes Nets. For example, Figure $? ? ( \mathrm { a } )$ is an equivalent representation of Figure ??(b). The N in the lower right corner of the plate stands for the number of replica.

![](images/page_18_image_2.jpg)

(a)

![](images/page_18_image_4.jpg)

Figure 2

Now consider the Bayes Net in Figure ??. We use $X _ { 1 : N }$ as shorthand for $( X _ { 1 } , \cdots , X _ { N } )$ . We would like to compute the query $P ( X _ { 1 : N } | Y _ { 1 : N } = y _ { 1 : N } )$ . Assume all variables are binary.

![](images/page_18_image_7.jpg)

Figure 3

(a) [?? pts] What is the number of rows in the largest factor generated by inference by enumeration, for this query?

$$
\bigcirc 2 ^ {2 N} \quad \bigcirc 2 ^ {3 N} \quad \bigcirc 2 ^ {2 N + 2} \quad \bullet 2 ^ {3 N + 2}
$$

In inference by enumeration, the full joint probability $P ( X _ { 1 : N } , Y _ { 1 : N } { = } y _ { 1 : N } , W _ { 1 : N } , Z _ { 1 : N } , A , B )$ are computed, which has size $2 ^ { 3 N + 2 }$

(b) [?? pts] Mark all of the following variable elimination orderings that are optimal for calculating the answer for the query $P ( X _ { 1 : N } | Y _ { 1 : N } = y _ { 1 : N } )$ . (A variable elimination ordering is optimal if the largest factors generated is smallest among all possible elimination orderings).

 $\operatorname { Z } _ { 1 } , \cdots , Z _ { N } , W _ { 1 } , \cdots , W _ { N } , B , A$

 $\operatorname { W } _ { 1 } , \cdots , W _ { N } , Z _ { 1 } , \cdots , Z _ { N } , B , A$

l $A , B , W _ { 1 } , \cdots , W _ { N } , Z _ { 1 } , \cdots , Z _ { N }$

l $A , B , Z _ { 1 } , \cdots , Z _ { N } , W _ { 1 } , \cdots , W _ { N }$

The only thing that matters is the size of the maximum factor generated during elimination and the final factor $P ( X _ { 1 : N } | y _ { 1 : N } )$ has size $2 ^ { N }$ . Eliminating anything other than A does not generate a factor which depends on more than one time index $i ,$ so as long as A is eliminated last, no factor of size greater than $2 ^ { N }$ is generated,

<!-- page: 20 -->

so the first two orderings are both optimal. (In fact, as long as A is eliminated before $B ,$ the ordering will be optimal, but it was not necessary to notice this to distinguish among the given options.)

(c) [?? pts] Which of the following variables can be deleted before running variable elimination, without affecting the inference result? Deleting a variable means not putting its CPT in our initial set of factors when starting the algorithm.

$$
\blacksquare \mathrm{W} _ {1} \quad \blacksquare \mathrm{Z} _ {1} \quad \square A \quad \blacksquare \mathrm{B} \quad \square \text {None}
$$

B, $W _ { 1 } .$ , and $Z _ { 1 }$ can all be deleted. In general, any variable which has no descendants that are query variables (in this case $X _ { i } )$ or evidence variables (in this case $y _ { i } )$ can be deleted. This is because when we eliminate the subgraph of all the descendants of such a variable, we will end up with a factor in which all the entries are equal to 1 and thus does not affect the results whatsoever when joined with other factors.

<!-- page: 21 -->

## Q9. [?? pts] Deep Learning

(a) [?? pts] Data Separability

![](images/page_20_image_2.jpg)

The plots above show points in feature space $( x _ { 1 } ,   x _ { 2 } )$ , also referred to as feature vectors $\mathbf { x } = [ x _ { 1 } \quad x _ { 2 } ] ^ { T }$ For each of the following, we will define a function $h ( \mathbf { x } )$ as a composition of some functions $f _ { i }$ and $g _ { i } .$ . For each one, consider the decision rule

$$
y (\mathbf {x}) = \left\{ \begin{array}{l l} \times & h (\mathbf {x}) \geqslant 0 \\ \bigcirc & h (\mathbf {x}) <   0. \end{array} \right.
$$

Under each composition of functions $h ,$ select the datasets for which there exist some linear functions $f _ { i }$ and some nonlinear functions $g _ { i }$ such that the corresponding decision rule perfectly classifies the data. (Select all that apply)

A composition of linear functions will always be linear. Parts (i), (ii), (iv) are linear. Plot (b) is linearly separable, and can be separated by linear or nonlinear decision boundaries. Plots (a),(c) require a nonlinear function to perfectly separate them.

(i) $h ( \mathbf { x } ) = f _ { 1 } ( \mathbf { x } )$

(a) l (b)  (c) l

(ii) $h ( \mathbf { x } ) = f _ { 2 } ( f _ { 1 } ( \mathbf { x } ) )$

(a) l (b)  (c) l

(iii) $h ( \mathbf { x } ) = f _ { 2 } ( g _ { 1 } ( f _ { 1 } ( \mathbf { x } ) ) )$

(a)  (b)  (c) 

(iv) $h ( \mathbf { x } ) = f _ { 4 } ( f _ { 3 } ( f _ { 2 } ( f _ { 1 } ( \mathbf { x } ) ) ) )$

(a) l (b)  (c) l

(v) $h ( \mathbf { x } ) = g _ { 2 } ( g _ { 1 } ( \mathbf { x } ) ) )$

(a)  (b)  (c) 

<!-- page: 22 -->

(b) Backpropagation Below is a deep network with input x. Values $x , h _ { 1 } , h _ { 2 } , z$ are all scalars.

$$
h _ {1} = f _ {1} (x), h _ {2} = f _ {2} (x), z = h _ {1} h _ {2}\tag{1}
$$

![](images/page_21_image_2.jpg)

Derive the following gradients in terms of $[ x , h _ { 1 } , h _ { 2 } , \frac { \hat { c } f _ { 1 } } { \hat { c } x } , \frac { \hat { c } f _ { 2 } } { \hat { c } x } .$

(i) [?? pts] Derive $\frac { \partial z } { \partial h _ { 1 } }$

When taking the partial derivative of z in terms of $h _ { 1 } .$ we treat $h _ { 2 }$ as a constant.

(ii) [?? pts] Derive $\frac { \partial z } { \partial h _ { 2 } }$

When taking the partial derivative of z in terms of $h _ { 2 }   .$ we treat $h _ { 1 }$ as a constant.

(iii) [?? pts] Derive $\frac { \partial z } { \partial x }$

We use product rule and chain rule.

$$
h _ {2} \frac {\partial f _ {1}}{\partial x} + h _ {1} \frac {\partial f _ {2}}{\partial x}
$$

<!-- page: 23 -->

(c) Deep Network Below is a deep network with inputs $x _ { 1 } , x _ { 2 }$ . The internal nodes are computed below. All variables are scalar values.

![](images/page_22_image_1.jpg)

(2)

(i) [?? pts] Forward propagation Now, given $x _ { 1 } = 1 , x _ { 2 } = - 2 , w _ { 1 1 } = 6 , w _ { 1 2 } = 2 , w _ { 2 1 } = 4 , w _ { 2 2 } = 7 ,$ $w _ { 3 1 } = 5 , w _ { 3 2 } = 1$ , and the same values for $x _ { 1 } , x _ { 2 }$ above, compute the values of the internal nodes. Please simplify any fractions.

| h<sub>1</sub> | h<sub>2</sub> | h<sub>3</sub> | r<sub>1</sub> | r<sub>2</sub> |
| --- | --- | --- | --- | --- |
| 2 | -10 | 3 | 2 | 0 |

| r<sub>3</sub> | s | y<sub>1</sub> | y<sub>2</sub> | z |
| --- | --- | --- | --- | --- |
| 3 | 3 | 11 ` e | e 1 ` e | 1 |

(ii) [?? pts] Bounds on variables.

Find the tightest bounds on y<sub>1</sub>. $y _ { 1 } \in ( 0 , 1 )$

The output of a softmax is a probability distribution. Each element of the output is between 0 and 1.

Find the tightest bounds on z. z “ 1

The sum of the probability distribution is 1.

<!-- page: 24 -->

![](images/page_23_image_0.jpg)

(3)

(iii) [?? pts] Backpropagation Compute the following gradients analytically. The answer should be an expression of any of the nodes in the network $( x _ { 1 } , x _ { 2 } , h _ { 1 } , h _ { 2 } , h _ { 3 } , r _ { 1 } , r _ { 2 } , r _ { 3 } , s _ { 1 } , y _ { 1 } , y _ { 2 } , z )$ or weights $w _ { 1 1 } , w _ { 1 2 } , w _ { 2 1 } , w _ { 2 2 } , w _ { 3 1 } , w _ { 3 2 } .$ Hint: Recall that for functions of the form $\begin{array} { l } { g ( x )   =   \frac { 1 } { 1 + e x p ( a - x ) } , \; \frac { \partial g } { \partial x }   =   g ( x ) \left( 1 - g ( x ) \right) } \\ \end{array}$ . Also, your answer may be a constant or a piecewise function.

<table><tbody><tr><td rowspan="2">Bh1Bw12</td><td rowspan="2">Bh1Bx1</td><td rowspan="2">Br1Bh1</td><td rowspan="2">By1Br1</td></tr><tr></tr><tr><td>x<sub>2</sub></td><td>w<sub>11</sub></td><td>1rh<sub>1</sub> ą 0s</td><td>y<sub>1</sub>p1 ´ y<sub>1</sub>q</td></tr></tbody></table>

<table><tbody><tr><td rowspan="2">By1Bs1</td><td rowspan="2">BzBy1</td><td rowspan="2">BzBx1</td><td rowspan="2">Bs1Br2</td></tr><tr></tr><tr><td>´y<sub>1</sub>y<sub>2</sub></td><td>1</td><td>0</td><td>1rr<sub>2</sub> ą r<sub>3</sub>s</td></tr></tbody></table>

Expanded solutions for selected examples below:

$r _ { 1 } = \operatorname* { m a x } ( h _ { 1 } , 0 )$ This is known as a ReLU (rectified linear unit) function. When $h _ { 1 }$ is positive, $r _ { 1 } = h _ { 1 }$ so the derivative is 1. When $h _ { 1 }$ is negative, $r _ { 1 }$ is flat, so the derivative is 0.

$$
\begin{array}{l} y _ {1} = \frac {\exp (r _ {1})}{\exp (r _ {1}) + \exp (r _ {2})} = \frac {1}{1 + \exp (r _ {2} - r _ {1})} \\ \frac {d y _ {1}}{d r _ {1}} = \frac {- 1}{(1 + \exp (r _ {2} - r _ {1})) ^ {2}} \times (- \exp (r _ {2} - r _ {1})), \text {by chain rule} \\ = \frac {1}{1 + \exp (r _ {2} - r _ {1})} \times \frac {\exp (r _ {2} - r _ {1})}{1 + \exp (r _ {2} - r _ {1})} \\ = y _ {1} (1 - y _ {1}) \\ = y _ {1} y _ {2} \end{array}
$$

$\begin{array} { l } { \frac { d y _ { 1 } } { d r _ { 2 } } = \frac { - 1 } { ( 1 + \operatorname { e x p } ( r _ { 2 } - r _ { 1 } ) ) ^ { 2 } } \times ( \operatorname { e x p } ( r _ { 2 } - r _ { 1 } ) ) } \\ \end{array}$ , by chain rule. Notice that this is identical to the case above, but with a negative sign missing on the 2nd term.

<!-- page: 25 -->

$$
\begin{array}{l} = \frac {- 1}{1 + \exp (r _ {2} - r _ {1})} \times \frac {\exp (r _ {2} - r _ {1})}{1 + \exp (r _ {2} - r _ {1})} \\ = - y _ {1} (1 - y _ {1}) \\ = - y _ {1} y _ {2} \end{array}
$$

No matter how $x _ { 1 } , x _ { 2 }$ change, z is always 1, so the gradient with respect to $x _ { 1 } { \mathrm { ~ i s ~ 0 ~ } }$

When $r _ { 2 } > r _ { 3 } , \: s _ { 1 } = r _ { 2 } , \: \operatorname { s o } \textstyle \frac { \hat { \circ } s _ { 1 } } { r _ { 2 } } = 1$ . When $\begin{array} { r } { r _ { 2 } < r _ { 3 } ,   s _ { 1 } = r _ { 3 } ,   \mathrm { s o }   \frac { \partial s _ { 1 } } { r _ { 2 } } = 0 . } \end{array}$

<!-- page: 26 -->
