<!-- page: 1 -->

arXiv:2304.00803v1 [cs.LG] 3 Apr 2023

# A Tutorial Introduction to Reinforcement Learning

Mathukumalli Vidyasagar [^1]

April 4, 2023

## Abstract

In this paper, we present a brief survey of Reinforcement Learning (RL), with particular emphasis on Stochastic Approximation (SA) as a unifying theme. The scope of the paper includes Markov Reward Processes, Markov Decision Processes, Stochastic Approximation algorithms, and widely used algorithms such as Temporal Difference Learning and \(Q\)-learning.

## 1 Introduction

In this paper, we present a brief survey of Reinforcement Learning (RL), with particular emphasis on Stochastic Approximation (SA) as a unifying theme. The scope of the paper includes Markov Reward Processes, Markov Decision Processes, Stochastic Approximation methods, and widely used algorithms such as Temporal Difference Learning and \(Q\)-learning. Reinforcement Learning is a vast subject, and this brief survey can barely do justice to the topic. There are several excellent texts on RL, such as [4, 27, 34, 33]. The dynamics of the Stochastic Approximation (SA) algorithm are analyzed in [25, 22, 3, 23, 2, 9, 10]. The interested reader may consult those sources for more information.

In this survey, we use the phrase "reinforcement learning" to refer to decision-making with uncertain models, *and in addition, current actions alter the future behavior of the system*. Therefore, if the same action is taken at a future time, the consequences might not be the same. This additional feature distinguishes RL from "mere" decision-making under uncertainty. Figure 1 rather arbitrarily divides decision-making problems into four quadrants. Examples from each quadrant are now briefly described.

- Many if not most decision-making problems fall into the lower-left quadrant of "good model, no alteration" (meaning that the control actions do not alter the environment). An example is a fighter aircraft which usually has an excellent model thanks to aerodynamical modelling and/or wind tunnel tests. In turn this permits the control system designers to formulate and to solve an optimal (or some other form of) control problem.

- Controlling a chemical reactor would be an example from the lower-right quadrant. As a traditional control system, it can be assumed that the environment in which the reactor operates does not change as a consequence of the control strategy adopted. However, due to the complexity of a reactor, it is difficult to obtain a very accurate model, in contrast with a

[^1]: SERB National Science Chair, Indian Institute of Technology Hyderabad, Kandi, Telangana 502284, India. Email: m.vidyasagar@iith.ac.in This research was supported by the Science and Engineering Research Board, Government of India.

1

<!-- page: 2 -->

  fighter aircraft for example. In such a case, one can adopt one of two approaches. The first, which is a traditional approach in control system theory, is to use a nominal model of the system and to treat the deviations from the nominal model as uncertainties in the model. A controller is designed based on the nominal model, and robust control theory would be invoked to ensure that the controller would still perform satisfactorily (though not necessarily optimally) for the actual system. The second, which would move the problem from the lower right to the upper right quadrant, is to attempt to "learn" the unknown dynamical model by probing its response to various inputs. This approach is suggested in [33, Example 3.1]. A similar statement can be made about robots, where the geometry determines the *form* of the dynamical equations describing it, but not the parameters in the equations; see for example [30]. In this case too, it is possible to "learn" the dynamics through experimentation. In practice, such an approach is far slower than the traditional control systems approach of using a nominal model and designing a "robust" controller. However, "learning control" is a popular area in the world of machine learning. One reason is that the initial modelling error is too large, then robust control theory alone would not be sufficient to ensure the stability of the actual system with the designed controller. In contrast (and in principle), a "learning control" approach can withstand larger modelling errors. The widely-used Model Predictive Control (MPC) paradigm can be viewed as an example of a learning-based approach.

- A classic example of a problem belonging to the upper-left corner is a Markov Decision Process (MDP), which forms the backbone of one approach to RL. In an MDP, there is a state space \(\mathcal{X}\), and an action space \(\mathcal{U}\), both of which are usually assumed to be finite. In most MDPs, \(|\mathcal{X}| \gg |\mathcal{U}|\). Board games without an element of randomness such as tic-tac-toe or chess would belong to the upper-left quadrant, at least in principle. Tic-tac-toe belongs here, because the rules of the game are clear, and the number of possible games is manageable. *In principle*, games such as chess which are "deterministic" (i.e., there is no throwing of dice as in Backgammon for example) would also belong here. Chess is a two-person game in which, for each board position, it is possible to assign the likelihood of the three possible outcomes: White wins, Black wins, or it is a draw. However, due to the enormous number of possibilities, it is often not possible to *determine* these likelihoods precisely. It is pointed out explicitly in [29] that, merely because we cannot explicitly compute this likelihood function, that does not mean that the likelihood does not exist! However, as a practical matter, it is not a bad idea to treat this likelihood function as being unknown, and to *infer* it on the basis of experiment / experience. Thus, as with chemical reactors, it is not uncommon to move chess-playing from the lower-right corner to the upper-right corner.

- The upper-right quadrant is the focus of RL. There are many possible ways to formulate RL problems, each of which leads to its own solution methodologies. A very popular approach to RL is to formulate it as MDPs whose dynamics are unknown. That is the approach adopted in this paper.

In an MDP, at each time \(t\), the learner (also known as the actor or the agent) measures the state \(X_t \in \mathcal{X}\). Based on this measurement, the learner chooses an action \(U_t \in \mathcal{U}\), and receives a reward \(R(X_t, U_t)\). Future rewards are discounted by a discount factor \(\gamma \in (0,1)\). The rule by which the current action \(U_t\) is chosen as a function of the current state \(X_t\) is known as a policy. With each policy, one can associate the expected value of the total (discounted) reward over time. The problem is to find the best policy. There is a variant called POMDP (Partially Observable Markov Decision Process) in which the state \(X_t\) cannot be measured directly; rather, there is an output (or

2

<!-- page: 3 -->

[FIGURE: Figure 1: The four quadrants of decision-making under uncertainty]

Text in figure:

Interaction Between Action & Environment (vertical axis)

Model Quality (horizontal axis)

| | |
|---|---|
| Good model. Action can alter Environment | Poor model. Action can alter Environment |
| Good model. Action doesn't alter Environment | Poor model. Action doesn't alter Environment |

Figure 1: The four quadrants of decision-making under uncertainty

[FIGURE: Figure 2: Depiction of a Reinforcement Learning Problem]

Text in figure:

- Environment:Markov Process, States \(\{X_0, X_1, \cdots\}\)
- Reward \(R\), \(R_t = R(X_t, U_t)\)
- Policy \(\pi\), \(U_t = \pi(X_t)\)
- Arrows labelled \(X_t\), \(X_t\), \(U_t\), \(U_t\)

Figure 2: Depiction of a Reinforcement Learning Problem

observation) \(Y_t \in \mathcal{Y}\) which is a memoryless function, either deterministic or random, of \(X_t\). These problems are not studied here; it is always assumed that \(X_t\) can be measured directly. When the parameters of the MDP are known, there are several approaches to determining the optimal policy. RL is distinct from an MDP in that, in RL, the parameters of the underlying MDP are constant but not known to the learner; they must be learnt on the basis of experimentation. Figure 2 depicts the situation.

The remainder of the paper is organized as follows: In Section 2, Markov Reward Processes are introduced. These are a precursor to Markov Decision Processes (MDPs), which are introduced in Section 3. Specifically, in Section 3.1, the relevant problems in the study of MDPs are formulated. In Section 3.2, the solutions to these problems are given in terms of the Bellman value iteration, the action-value function, and the \(F\)-iteration to determine the optimal action-value function. In Section 3.3, we study the situation where the dynamics of the MDP under study are not known precisely. Instead, one has access only to a sample path \(\{X_t\}\) of the Markov process under study. For this situation, we present two standard algorithms, known as Temporal Difference Learning, and \(Q\)-Learning. Starting from Section 4, the paper consists of results due to the author. In Section 4.1, the concept of stochastic approximation (SA) is introduced, and its relevance to Reinforcement Learning is outlined in Section 4.2. In Section 4.3, a new theorem on the global asymptotic

3

<!-- page: 4 -->

stability of nonlinear ODEs is stated; this theorem is of independent interest. Some theorems on the convergence of the SA algorithm are presented in Sections 4.4 and 4.5. In Section 5, the results of Section 4 are applied to RL problems. In Section 5.1, a technical result on the sample paths of an irreducible Markov process is stated. Using this result, simplified conditions are given for the convergence of the Temporal Difference algorithm (Section 5.2) and \(Q\)-learning (Section 5.3). A brief set of concluding remarks ends the paper.

## 2 Markov Reward Processes

Markov reward processes are standard (stationary) Markov processes where each state has a "reward" associated with it. Markov Reward Processes are a precursor to Markov Decision Processes; so we review those in this section. There are several standard texts on Markov processes, one of which is [40].

Suppose \(\mathcal{X}\) is a finite set of cardinality \(n\), written as \(\{x_1, \ldots, x_n\}\). If \(\{X_t\}_{t\geq 0}\) is a stationary Markov process assuming values in \(\mathcal{X}\), then the corresponding state transition matrix \(A\) is defined by

$$
a_{ij} = \Pr\{X_{t+1} = x_j | X_t = x_i\}.
\tag{1}
$$

Thus the \(i\)-th row of \(A\) is the conditional probability vector of \(X_{t+1}\) when \(X_t = x_i\). Clearly the row sums of the matrix \(A\) are all equal to one. This can be expressed as \(A\mathbf{1}_n = \mathbf{1}_n\), where \(\mathbf{1}_n\) denotes the \(n\)-dimensional column vector whose entries all equal one. Therefore, if we define the induced matrix norm \(\|A\|_{\infty \to \infty}\) as

$$
\|A\|_{\infty \to \infty} := \max_{\mathbf{v} \neq \mathbf{0}} \frac{\|A\mathbf{v}\|_{\infty}}{\|\mathbf{v}\|_{\infty}},
$$

then \(\|A\|_{\infty \to \infty}\) equals one, which also equals the spectral radius of \(A\).

Now suppose that there is a "reward" function \(R : \mathcal{X} \to \mathbb{R}\) associated with each state. There is no consensus within the community about whether the reward corresponding to the state \(X_t\) is paid at time \(t\) as in [34], or time \(t+1\), as in [27, 33]. In this paper, it is assumed that the reward is paid at time \(t\), and is denoted by \(R_t\); the modifications required to handle the other approach are easy and left to the reader. The reward \(R_t\) can either be a deterministic function of \(X_t\), or a random function. If \(R_t\) is a deterministic function of \(X_t\), then we have that \(R_t = R(X_t)\) where \(R\) is the reward function mapping \(\mathcal{X}\) into (a finite subset of) \(\mathbb{R}\). Thus, whenever the trajectory \(\{X_t\}\) of the Markov process equals some state \(x_i \in \mathcal{X}\), the resulting reward \(R(X_t)\) will always equal \(R(x_i) =: r_i\). Thus the reward is captured by an \(n\)-dimensional vector \(\mathbf{r}\), where \(r_i = R(x_i)\). On the other hand, if \(R_t\) is a random function of \(X_t\), then one would have to provide the probability distribution of \(R_t\) given \(X_t\). Since \(X_t\) has only \(n\) different values, we would have to provide \(n\) different probability distributions. To avoid technical difficulties, it is common to assume that \(R(x_i)\) is a *bounded* random variable for each index \(i\). Note that, because the set \(\mathcal{X}\) is finite, if the reward function is deterministic, then we have that

$$
\max_{x_i \in \mathcal{X}} R(x_i) < \infty.
$$

In case the reward function \(R\) is random, as mentioned above, it is common to assume that \(R(x_i)\) is a *bounded* random variable for each index \(i \in [n]\), where the symbol \([n]\) equals \(\{1, \cdots, n\}\). With this assumption, it follows that

$$
\max_{x_i \in \mathcal{X}} E[R(x_i)] < \infty.
$$

4

<!-- page: 5 -->

Two kinds of Markov reward processes are widely studied, namely: Discounted reward processes, and average reward processes. In this paper, we restrict attention to discounted reward processes. However, we briefly introduce average reward processes. Define (if it exists)

$$
V(x_i) := \lim_{T \to 0} \frac{1}{T+1} E\left[\sum_{t=0}^{T} R(X_t) | X_0 = x_i\right].
$$

An excellent review of average reward processes can be found in [1].

In each discounted Markov Reward Process, there is a "discount factor" \(\gamma \in (0,1)\). This factor captures the extent to which future rewards are less valuable than immediate rewards. Fix an initial state \(x_i \in \mathcal{X}\). Then the **expected discounted future reward** \(V(x_i)\) is defined as

$$
V(x_i) := E\left[\sum_{t=0}^{\infty} \gamma^t R_t | X_0 = x_i\right] = E\left[\sum_{t=0}^{\infty} \gamma^t R(X_t) | X_0 = x_i\right].
\tag{2}
$$

We often just use "discounted reward" instead of the longer phrase. With these assumptions, because \(\gamma < 1\), the above summation converges and is well-defined. The quantity \(V(x_i)\) is referred to as the **value function** associated with \(x_i\), and the vector

$$
\mathbf{v} = [\ V(x_1) \quad \cdots \quad V(x_n)\ ]^{\top},
\tag{3}
$$

is referred to as the **value vector**. Note that, throughout this paper, we view the value as both a *function* \(V : \mathcal{X} \to \mathbb{R}\) as well as a *vector* \(\mathbf{v} \in \mathbb{R}^n\). The relationship between the two is given by (3). We shall use whichever interpretation is more convenient in a given context.

This raises the question as to how the value function and/or value vector is to be determined. Define the vector \(\mathbf{r} \in \mathbb{R}^n\) via

$$
\mathbf{r} := [\ r_1 \quad \cdots \quad r_n\ ]^{\top},
\tag{4}
$$

where \(r_i = R(x_i)\) if \(R\) is a deterministic function, and if \(R_t\) is a random function of \(X_t\), then

$$
r_i := E[R(x_i)].
\tag{5}
$$

The next result gives a useful characterization of the value vector.

**Theorem 1.** *The vector \(\mathbf{v}\) satisfies the recursive relationship*

$$
\mathbf{v} = \mathbf{r} + \gamma A \mathbf{v},
\tag{6}
$$

*or, in expanded form,*

$$
V(x_i) = r_i + \gamma \sum_{j=1}^{n} a_{ij} V(x_j).
\tag{7}
$$

*Proof.* Let \(x_i \in \mathcal{X}\) be arbitrary. Then by definition we have

$$
V(x_i) = E\left[\sum_{t=0}^{\infty} \gamma^t R_t | X_0 = x_i\right] = r_i + E\left[\sum_{t=1}^{\infty} \gamma^t R_t | X_0 = x_i\right].
\tag{8}
$$

5

<!-- page: 6 -->

However, if \(X_0 = x_i\), then \(X_1 = x_j\) with probability \(a_{ij}\). Therefore we can write

$$
\begin{aligned}
E\left[\sum_{t=1}^{\infty} \gamma^t R_t | X_0 = x_i\right] &= \sum_{j=1}^{n} a_{ij} E\left[\sum_{t=1}^{\infty} \gamma^t R_t | X_1 = x_j\right] \\
&= \gamma \sum_{j=1}^{n} a_{ij} E\left[\sum_{t=0}^{\infty} \gamma^t R_t | X_0 = x_j\right] \\
&= \gamma \sum_{j=1}^{n} a_{ij} V(x_j).
\end{aligned}
\tag{9}
$$

In the second step we use fact that the Markov process is stationary. Substituting from (9) into (8) gives the recursive relationship (7). □

**Example 1.** *As an illustration of a Markov Reward process, we analyze a toy snakes and ladders game with the transitions shown in Figure 3. Here \(W\) and \(L\) denote "win" and "lose" respectively. The rules of the game are as follows:*

- *Initial state is S.*

- *A four-sided, fair die is thrown at each stage.*

- *Player must land exactly on \(W\) to win and exactly on \(L\) to lose.*

- *If implementing a move causes crossing of \(W\) and \(L\), then the move is not implemented.*

*There are twelve possible states in all: S, 1, ... , 9 , W, L. However, 2, 3, 9 can be omitted, leaving nine states, namely S, 1, 4, 5, 6, 7, 8, W, L. At each step, there are at most four possible outcomes. For example, from the state S, the four outcomes are 1, 7, 5, 4. From state 6, the four outcomes are 7, 8, 1, and W. From state 7, the four outcomes are 8, 1, W, 7. From state 8, there four possible outcomes are 1, W, L and 8 with probability 1/4 each, because if the die comes up with 4, then the move cannot be implemented. It is time-consuming but straight-forward to compute the state transition matrix as*

| | \(S\) | 1 | 4 | 5 | 6 | 7 | 8 | \(W\) | \(L\) |
|---|---|---|---|---|---|---|---|---|---|
| \(S\) | 0 | 0.25 | 0.25 | 0.25 | 0 | 0.25 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0.25 | 0.50 | 0 | 0.25 | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0.25 | 0.25 | 0.25 | 0.25 | 0 | 0 |
| 5 | 0 | 0.25 | 0 | 0 | 0.25 | 0.25 | 0.25 | 0 | 0 |
| 6 | 0 | 0.25 | 0 | 0 | 0 | 0.25 | 0.25 | 0.25 | 0 |
| 7 | 0 | 0.25 | 0 | 0 | 0 | 0 | 0.25 | 0.25 | 0.25 |
| 8 | 0 | 0.25 | 0 | 0 | 0 | 0 | 0.25 | 0.25 | 0.25 |
| \(W\) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| \(L\) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

*We define a reward function for this problem, as follows: We set \(R_t = f(X_{t+1})\), where \(f\) is defined as follows: \(f(W) = 5\), \(f(L) = -2\), \(f(x) = 0\) for all other states. However, there is an expected reward depending on the state at the next time instant. For example, if \(X_0 = 6\), then the expected value of \(R_0\) is 5/4, whereas if \(X_0 = 7\) or \(X_0 = 8\), then the expected value of \(R_0\) is 3/4.* ■

6

<!-- page: 7 -->

[FIGURE: Figure 3: A Toy Snakes and Ladders Game]

Text in figure:

A row of boxes labelled: S, 1, 2, 3, 4, 5, 6, 7, 8, 9, W, L, with curved arrows connecting them.

Figure 3: A Toy Snakes and Ladders Game

Now let us see how the implicit equation (6) can be solved to determine the value vector \(\mathbf{v}\). Since the induced matrix norm \(\|A\|_{\infty \to \infty} = 1\) and \(\gamma < 1\), it follows that the matrix \(I - \gamma A\) is nonsingular. Therefore, for every reward function \(\mathbf{r}\), there is a unique \(\mathbf{v}\) that satisfies (6). In principle it is possible to deduce from (6) that

$$
\mathbf{v} = (I - \gamma A)^{-1} \mathbf{r}.
\tag{10}
$$

The difficulty wth this formula however is that in most actual applications of Markov Decision Problems, the integer \(n\) denoting the size of the state space \(\mathcal{X}\) is quite large. Moreover, inverting a matrix has cubic complexity in the size of the matrix. Therefore it may not be practicable to invert the matrix \(I - \gamma A\). So we are forced to look for alternate approaches. A feasible approach is provided by the Contraction Mapping Theorem.

**Theorem 2.** *The map \(\mathbf{y} \mapsto T\mathbf{y} := \mathbf{r} + \gamma A \mathbf{y}\) is monotone and is a contraction with respect to the \(\ell_{\infty}\)-norm, with contraction constant \(\gamma\). Therefore, we can choose some vector \(\mathbf{y}^0\) arbitrarily, and then define*

$$
\mathbf{y}^{i+1} = \mathbf{r} + \gamma A \mathbf{y}^i.
$$

*Then \(\mathbf{y}^i\) converges to the value vector \(\mathbf{v}\).*

*Proof.* The first statement is that if \(\mathbf{y}_1 \leq \mathbf{y}_2\) componentwise (and note that the vectors \(\mathbf{y}_1, \mathbf{y}_2\) need not consist of only positive components), then \(T\mathbf{y}_1 \leq T\mathbf{y}_2\). This is obvious from the fact that the matrix \(A\) has only nonnegative components, so that \(A\mathbf{y}_1 \leq A\mathbf{y}_2\). For the second statement, note that, because the matrix \(A\) is row-stochastic, the induced matrix norm \(\|A\|_{\infty \to \infty}\) is equal to one. Therefore

$$
\|T\mathbf{y}_1 - T\mathbf{y}_2\|_{\infty} = \|\gamma A(\mathbf{y}_1 - \mathbf{y}_2)\|_{\infty} \leq \gamma \|\mathbf{y}_1 - \mathbf{y}_2\|_{\infty}.
$$

This completes the proof. □

There is however a limitation to this approach, namely, that it requires that the state transition matrix \(A\) has to be known. In Reinforcement Learning, this assumption is often not satisfied. Instead, one has access to a single sample path \(\{X_t\}\) of a Markov process over \(\mathcal{X}\), whose state transition matrix is \(A\). The question therefore arises: How can one compute the value vector \(\mathbf{v}\) in such a scenario? The answer is provided by the so-called Temporal Difference algorithm, which is discussed in Section 3.3.

7

<!-- page: 8 -->

## 3 Markov Decision Processes

### 3.1 Problem Formulation

In a Markov reward process, the state \(X_t\) evolves on its own, according to a predetermined state transition matrix. In contrast, in a MDP, there is also another variable called the "action" which affects the dynamics. Specifically, in addition to the state space \(\mathcal{X}\), there is also a finite set of actions \(\mathcal{U}\). Each action \(u_k \in \mathcal{U}\) leads to a corresponding state transition matrix \(A^{u_k} = [a_{ij}^{u_k}]\). So at time \(t\), if the state is \(X_t\), and an action \(U_t \in \mathcal{U}\) is applied, then

$$
\Pr\{X_{t+1} = x_j | X_t = x_i, U_t = u_k\} = a_{ij}^{u_k}.
\tag{11}
$$

Obviously, for each fixed \(u_k \in \mathcal{U}\), the corresponding state transition matrix \(A^{u_k}\) is row-stochastic. In addition, there is also a "reward" function \(R : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\). Note that in a Markov reward process, the reward depends only on the current state, whereas in a Markov decision process, the reward depends on both the current state as well as the action taken. As in Markov reward processes, it is possible to permit \(R\) to be a random function of \(X_t\) and \(U_t\) as opposed to a deterministic function. Moreover, to be consistent with the earlier convention, it is assumed that the reward \(R(X_t, U_t)\) is paid at time \(t\).

The most important aspect of an MDP is the concept of a "policy," which is just a systematic way of choosing \(U_t\) given \(X_t\). If \(\pi : \mathcal{X} \to \mathcal{U}\) is any map, this would be called a *deterministic* policy, and the set of all deterministic policies is denoted by \(\Pi_d\). Alternatively, let \(\mathbb{S}(\mathcal{U})\) denote the set of probability distributions on the finite set \(\mathcal{U}\). Then a map \(\pi : \mathcal{X} \to \mathbb{S}(\mathcal{U})\) would be called a probabilistic policy, and the set of probabilistic policies is denoted by \(\Pi_p\). Note that the cardinality of \(\Pi_d\) equals \(|\mathcal{U}|^{|\mathcal{X}|}\), while the set \(\Pi_p\) is uncountable.

A vital point about MDPs is this: Whenever any policy \(\pi\), whether deterministic or probabilistic, is implemented, the resulting process \(\{X_t\}\) is a Markov process with an associated state transition matrix, which is denoted by \(A_{\pi}\). This matrix can be determined as follows: If \(\pi \in \Pi_d\), then at time \(t\), if \(X_t = x_i\), then the corresponding action \(U_t\) equals \(\pi(x_i)\). Therefore

$$
\Pr\{X_{t+1} = x_j | X_t = x_i, \pi\} = a_{ij}^{\pi(x_i)}.
\tag{12}
$$

If \(\pi \in \Pi_p\) and

$$
\pi(x_i) = [\ \phi_{i1} \quad \cdots \quad \phi_{im}\ ],
\tag{13}
$$

where \(m = |\mathcal{U}|\), then

$$
\Pr\{X_{t+1} = x_j | X_t = x_i, \pi\} = \sum_{k=1}^{m} \phi_{ik} a_{ij}^{u_k}.
\tag{14}
$$

In a similar manner, for every policy \(\pi\), the reward function \(R : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\) can be converted into a reward map \(R_{\pi} : \mathcal{X} \to \mathbb{R}\), as follows: If \(\pi \in \Pi_d\), then

$$
R_{\pi}(x_i) = R(x_i, \pi(x_i)),
\tag{15}
$$

whereas if \(\pi \in \Pi_p\), then

$$
R_{\pi}(x_i) = \sum_{k=1}^{m} \phi_{ik} R(x_i, u_k).
\tag{16}
$$

Thus, given any policy \(\pi\), whether deterministic or probabilistic, we can associate with it a reward vector \(\mathbf{r}_{\pi}\). To summarize, given any MDP, once a policy \(\pi\) is chosen, the resulting process \(\{X_t\}\) is a Markov reward process with state transition matrix \(A_{\pi}\) and reward vector \(\mathbf{r}_{\pi}\).

8
<!-- page: 9 -->

**Example 2.** *To illustrate these ideas, suppose \(n = 4, m = 2\), so that there four states and two actions. Thus there are two \(4 \times 4\) state transition matrices \(A^1, A^2\) corresponding to the two actions. (In the interests of clarity, we write \(A^1\) and \(A^2\) instead of \(A^{u_1}\) and \(A^{u_2}\).) Suppose \(\pi_1\) is a deterministic policy, represented as a \(n \times m\) matrix (in this case a \(4 \times 2\) matrix), as follows:*

$$
M_1 = \left[\begin{array}{cc} 0 & 1 \\ 0 & 1 \\ 1 & 0 \\ 0 & 1 \end{array}\right].
$$

*This means that if \(X_t = x_1, x_2\) or \(x_4\), then \(U_t = u_2\), while if \(X_t = x_3\), then \(U_t = u_1\). Let us use the notation \((A^k)^i\) to denote the \(i\)-th row of the matrix \(A^k\), where \(k = 1, 2\) and \(i = 1, 2, 3, 4\). Then the state transition matrix \(A_{\pi_1}\) is given by*

$$
A_{\pi_1} = \left[\begin{array}{c} (A^2)^1 \\ (A^2)^2 \\ (A^1)^3 \\ (A^2)^4 \end{array}\right].
$$

*Thus the first, third, and fourth rows of \(A_{\pi_1}\) come from \(A^2\), while the second row comes from \(A^1\).*

*Next, suppose \(\pi_2\) is a probabilistic policy, represented by the matrix*

$$
M_2 = \left[\begin{array}{cc} 0.3 & 0.7 \\ 0.2 & 0.8 \\ 0.9 & 0.1 \\ 0.4 & 0.6 \end{array}\right].
$$

*Thus, if \(X_t = x_1\), then the action \(U_t = u_1\) with probability 0.3 and equals \(u_2\) with probability 0.7, and so on. For this policy, the resulting state transition matrix is determined as follows:*

$$
A_{\pi_2} = \left[\begin{array}{c} 0.3(A^1)^1 + 0.7(A^2)^1 \\ 0.2(A^1)^2 + 0.8(A^2)^2 \\ 0.9(A^1)^3 + 0.1(A^2)^3 \\ 0.4(A^1)^4 + 0.6(A^2)^4 \end{array}\right].
$$

■

For an MDP, one can pose three questions:

1. **Policy evaluation:** We have seen already that, given a Markov reward process, with a reward vector \(\mathbf{r}\) and a discount factor \(\gamma\), there corresponds a unique value vector \(\mathbf{v}\). We have also seen that, for any choice of a policy \(\pi\), whether deterministic or probabilistic, there corresponds a state transition matrix \(A_{\pi}\) and a reward vector \(\mathbf{r}_{\pi}\). Therefore, once a policy \(\pi\) is chosen, the Markov *decision* process becomes a Markov *reward* process with state transition matrix \(A_{\pi}\) and reward vector \(\mathbf{r}_{\pi}\). We can define \(\mathbf{v}_{\pi}(x_i)\) to be the value vector associated with this Markov reward process. The question is: How can \(\mathbf{v}_{\pi}(x_i)\) be computed?

2. **Optimal Value Determination:** For each policy \(\pi\), there is an associated value vector \(\mathbf{v}_{\pi}\). Let us view \(\mathbf{v}_{\pi}\) as a map from \(\mathcal{X}\) to \(\mathbb{R}\), so that \(V_{\pi}(x_i)\) is the \(i\)-th component of \(\mathbf{v}_{\pi}\). Now suppose \(x_i \in \mathcal{X}\) is a specified initial state, and define

$$
V^*(x_i) := \max_{\pi \in \Pi_p} V_{\pi}(x_i),
\tag{17}
$$

9

<!-- page: 10 -->

to be the **optimal value** over all policies, when the MDP is started in the initial state \(X_0 = x_i\). How can \(V^*(x_i)\) be computed? Note that in (17), the optimum is taken over all *probabilistic* policies. However, it can be shown that the optimum is the same even if \(\pi\) is restricted to only *deterministic* policies.

3. **Optimal Policy Determination:** In (17) above, we associate an optimal policy with each state \(x_i\). Now we can extend the idea and define the **optimal policy** map \(\mathcal{X} \to \Pi_d\) via

$$
\pi^*(x_i) := \arg \max_{\pi \in \Pi_d} V_{\pi}(x_i).
\tag{18}
$$

How can the optimal policy map \(\pi^*\) be determined? Note that it is not *a priori* evident that there exists *one* policy that is optimal for *all* initial states. But the existence of such an optimal policy can be shown. Also, we can restrict to \(\pi \in \Pi_d\) in (18) because it can be shown that the maximum over \(\pi \in \Pi_p\) is not any larger. In other words,

$$
\max_{\pi \in \Pi_d} V_{\pi}(x_i) = \max_{\pi \in \Pi_p} V_{\pi}(x_i).
$$

### 3.2 Markov Decision Processes: Solution

In this subsection we present answers to the three questions above.

#### 3.2.1 Policy Evaluation:

Suppose a policy \(\pi\) in \(\Pi_d\) or \(\Pi_p\) is specified. Then the corresponding state transition matrix \(A_{\pi}\) and reward vector \(\mathbf{r}_{\pi}\) are given by (12) (or (14)) and (15) respectively. As pointed out above, once the policy is chosen, the process becomes just a Markov reward process. Then it readily follows from Theorem 1 that \(\mathbf{v}_{\pi}\) satisfies an equation analogous to (6), namely

$$
\mathbf{v}_{\pi} = \mathbf{r}_{\pi} + \gamma A_{\pi} \mathbf{v}_{\pi}.
\tag{19}
$$

As before, it is inadvisable to compute \(\mathbf{v}_{\pi}\) via \(\mathbf{v}_{\pi} = (I - \gamma A_{\pi})^{-1} \mathbf{r}_{\pi}\). Instead, one should use value iteration to solve (19). Observe that, whatever the policy \(\pi\) might be, the resulting state transition matrix \(A_{\pi}\) satisfies \(\|A\|_{\infty \to \infty} = 1\). Therefore the map \(\mathbf{y} \mapsto \mathbf{r}_{\pi} + \gamma A_{\pi} \mathbf{y}\) is a contraction with respect to \(\|\cdot\|_{\infty}\), with contraction constant \(\gamma\).

#### 3.2.2 Optimal Value Determination:

Now we introduce one of the key ideas in Markov Decision Processes. Define the **Bellman iteration map** \(B : \mathbb{R}^n \to \mathbb{R}^n\) via

$$
(B\mathbf{v})_i := \max_{u_k \in \mathcal{U}} \left[R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} v_j\right].
\tag{20}
$$

**Theorem 3.** *The map \(B\) is monotone and a contraction with respect to the \(\ell_{\infty}\)-norm. Therefore the fixed point \(\bar{\mathbf{v}}\) of the map \(B\) satisfies the relation*

$$
(\bar{\mathbf{v}})_i := \max_{u_k \in \mathcal{U}} \left[R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} (\bar{\mathbf{v}})_j\right].
\tag{21}
$$

10

<!-- page: 11 -->

Note that (21) is known as the **Bellman Optimality equation**. Thus, in principle at least, we can choose an arbitrary initial guess \(\mathbf{v}_0 \in \mathbb{R}^d\), and repeatedly apply the Bellman iteration. The resulting iterations would converge to the unique fixed point of the operator \(B\), which we denote by \(\bar{\mathbf{v}}\).

The significance of the Bellman iteration is given by the next theorem.

**Theorem 4.** *Define \(\bar{\mathbf{v}} \in \mathbb{R}^n\) to be the unique fixed point of \(B\), and define \(\mathbf{v}^* \in \mathbb{R}^n\) to equal \([V^*(x_i), x_i \in \mathcal{X}]\), where \(V^*(x_i)\) is defined in (17). Then \(\bar{\mathbf{v}} = \mathbf{v}^*\).*

Therefore, the optimal value vector can be computed using the Bellman iteration. However, knowing the optimal *value* vector does not, by itself, give us an optimal *policy*.

#### 3.2.3 Optimal Policy Determination

To solve the problem of optimal policy determination, we introduce another function \(Q_{\pi} : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\), known as the **action-value function**, which is defined as follows:

$$
Q_{\pi}(x_i, u_k) := R(x_i, u_k) + E_{\pi}\left[\sum_{t=1}^{\infty} \gamma^t R_{\pi}(X_t) | X_0 = x_i, U_0 = u_k\right].
\tag{22}
$$

This function was first defined in [42]. Note that \(Q_{\pi}\) is defined only for deterministic policies. In principle it is possible to define it for probabilistic policies, but this is not commonly done. In the above definition, the expectation \(E_{\pi}\) is with respect to the evolution of the state \(X_t\) under the policy \(\pi\).

The way in which a MDP is set up is that at time \(t\), the Markov process reaches a state \(X_t\), based on the previous state \(X_{t-1}\) and the state transition matrix \(A_{\pi}\) corresponding to the policy \(\pi\). Once \(X_t\) is known, the policy \(\pi\) determines the action \(U_t = \pi(X_t)\), and then the reward \(R_{\pi}(X_t) = R(X_t, \pi(X_t))\) is generated. In particular, when defining the value function \(V_{\pi}(x_i)\) corresponding to a policy \(\pi\), we start off the MDP in the initial state \(X_0 = x_i\), *and choose the action \(U_0 = \pi(x_i)\)*. However, in defining the action-value function \(Q_{\pi}\), we do not feel compelled to set \(U_0 = \pi(X_0) = \pi(x_i)\), and can choose an *arbitrary action \(u_k \in \mathcal{U}\)*. From \(t = 1\) onwards however, the action \(U_t\) is chosen as \(U_t = \pi(X_t)\). This seemingly small change leads to some simplifications.

Just as we can interpret \(V_{\pi} : \mathcal{X} \to \mathbb{R}\) as an \(n\)-dimensional vector, we can interpret \(Q_{\pi} : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\) as an \(nm\)-dimensional vector, or as a matrix of dimension \(n \times m\). Consequently the \(Q_{\pi}\)-vector has higher dimension than the value vector.

**Theorem 5.** *For each policy \(\pi \in \Pi_d\), the function \(Q_{\pi}\) satisfies the recursive relationship*

$$
Q_{\pi}(x_i, u_k) = R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} Q_{\pi}(x_j, \pi(x_j)).
\tag{23}
$$

*Proof.* Observe that at time \(t = 0\), the state transition matrix is \(A^{u_k}\). So, given that \(X_0 = x_i\) and \(U_0 = u_k\), the next state \(X_1\) has the distribution

$$
X_1 \sim [a_{ij}^{u_k}, j = 1, \cdots, n].
$$

11

<!-- page: 12 -->

Moreover, \(U_1 = \pi(X_1)\) because the policy \(\pi\) is implemented from time \(t = 1\) onwards. Therefore

$$
\begin{aligned}
Q_{\pi}(x_i, u_k) &= R(x_i, u_k) \\
&+ E_{\pi}\left[\sum_{j=1}^{n} a_{ij}^{u_k}\left(\gamma R(x_j, \pi(x_j)) + \sum_{t=2}^{\infty} \gamma^t R_{\pi}(X_t) | X_1 = x_j, U_1 = \pi(x_j)\right)\right] \\
&= R(x_i, u_k) \\
&+ E_{\pi}\left[\gamma \sum_{j=1}^{n} a_{ij}^{u_k}\left(R(x_j, \pi(x_j)) + \sum_{t=1}^{\infty} \gamma^t R_{\pi}(X_t) | X_1 = x_j, U_1 = \pi(x_j)\right)\right] \\
&= R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} Q(x_j, \pi(x_j)).
\end{aligned}
$$

This is the desired conclusion. □

**Theorem 6.** *The functions \(V_{\pi}\) and \(Q_{\pi}\) are related via*

$$
V_{\pi}(x_i) = Q_{\pi}(x_i, \pi(x_i)).
\tag{24}
$$

*Proof.* If we choose \(u_k = \pi(x_i)\) then (23) becomes

$$
Q_{\pi}(x_i, \pi(x_i)) = R_{\pi}(x_i) + \gamma \sum_{j=1}^{n} a_{ij}^{\pi(x_j)} Q(x_j, \pi(x_j)).
$$

This is the same as (11) written out componentwise. We know that (11) has a unique solution, namely \(V_{\pi}\). This shows that (24) holds. □

The import of Theorem 6 is the following: In defining the function \(Q_{\pi}(x_i, u_k)\) for a fixed policy \(\pi \in \Pi_d\), we have the freedom to choose the initial action \(u_k\) as any element we wish in the action space \(\mathcal{U}\). However, if we choose the initial action \(u_k = \pi(x_i)\) for each state \(x_i \in \mathcal{X}\), then the corresponding action-value function \(Q_{\pi}(x_i, u_k)\) equals the value function \(V_{\pi}(x_i)\), for each state \(x_i \in \mathcal{X}\).

In view of (24), the recursive equation for \(Q_{\pi}\) can be rewritten as

$$
Q_{\pi}(x_i, u_k) = R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} V_{\pi}(x_j).
\tag{25}
$$

This motivates the next theorem.

**Theorem 7.** *Define \(Q^* : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\) by*

$$
Q^*(x_i, u_k) = R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} V^*(x_j).
\tag{26}
$$

*Then \(Q^*(\cdot, \cdot)\) satisfies the following relationships:*

$$
Q^*(x_i, u_k) = R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} \max_{w_l \in \mathcal{U}} Q^*(x_j, w_l).
\tag{27}
$$

12

<!-- page: 13 -->

$$
V^*(x_i) = \max_{u_k \in \mathcal{U}} Q^*(x_i, u_k),
\tag{28}
$$

*Moreover, every policy \(\pi \in \Pi_d\) such that*

$$
\pi^*(x_i) = \arg \max_{u_k \in \mathcal{U}} Q^*(x_i, u_k)
\tag{29}
$$

*is optimal.*

*Proof.* Since \(Q^*(\cdot, \cdot)\) is defined by (26), it follows that

$$
\max_{u_k \in \mathcal{U}} Q^*(x_i, u_k) = \max_{u_k \in \mathcal{U}} \left[R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} V^*(x_j)\right] = V^*(x_i),
$$

This establishes (28) and (29). Substituting from (28) into (26) gives (27). □

Theorem 7 converts the problem of determining an optimal policy into one of solving the implicit equation (27). For this purpose, we define an iteration on action-functions that is analogous to (20) for value functions. As with the value function, the action-value function can either be viewed as a map \(Q : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\), or as a vector in \(\mathbb{R}^{nm}\), or as an \(n \times m\) matrix. We use whichever interpretation is convenient in the given situation.

**Theorem 8.** *Define \(F : \mathbb{R}^{|\mathcal{X}| \times |\mathcal{U}|} \to \mathbb{R}^{|\mathcal{X}| \times |\mathcal{U}|}\) by*

$$
[F(Q)](x_i, u_k) := R(x_i, u_k) + \gamma \sum_{j=1}^{n} a_{ij}^{u_k} \max_{w_l \in \mathcal{U}} Q(x_j, w_l).
\tag{30}
$$

*Then the map \(F\) is monotone and is a contraction. Moreover, for all \(Q_0 : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\), the sequence of iterations \(\{F^t(Q_0)\}\) converges to \(Q^*\) as \(t \to \infty\).*

If we were to rewrite (21) and (27) in terms of expected values, the differences between the \(Q\)-function and the \(V\)-function would become apparent. We can rewrite (21) as

$$
V^*(X_t) = \max_{U_t \in \mathcal{U}}\{R(X_t, U_t) + \gamma E[V^*(X_{t+1})|X_t]\},
\tag{31}
$$

and (27) as

$$
Q^*(X_t, U_t) = R(X_t, U_t) + \gamma E\left[\max_{U_{t+1} \in \mathcal{U}} Q^*(X_{t+1}, U_{t+1})\right].
\tag{32}
$$

Thus in the Bellman formulation and iteration, the maximization occurs *outside* the expectation, whereas with the \(Q\)-formulation and \(F\)-iteration, the maximization occurs *inside* the expectation.

### 3.3 Iterative Algorithms for MDPs with Unknown Dynamics

In principle, Theorem 2 can be used to compute, to arbitrary precision, the value vector of a Markov reward process. Similarly, Theorem 8 can be use to compute, to arbitrary precision, the optimal action-value function of a Markov Decision Process, from which both the optimal value function and the optimal policy can be determined. However, both theorems depend crucially on *knowing the dynamics of the underlying process*. For instance, if the state transition matrix \(A\) is not known, it would not be possible to carry out the iterations

$$
\mathbf{y}^{i+1} = \mathbf{r} + \gamma A \mathbf{y}^i.
$$

13

<!-- page: 14 -->

Early researchers in Reinforcement Learning were aware of this issue, and developed several algorithms that do not require *explicit* knowledge of the dynamics of the underlying process. Instead, it is assumed that a sample path \(\{X_t\}_{t=0}^{\infty}\) of the Markov process, together with the associated reward process, are available for use. With this information, one can think of two distinct approaches. First, one can use the sample path to *estimate* the state transition matrix, call it \(\hat{A}\). After a sufficiently long sample path has been observed, the contraction iteration above can be applied with \(A\) replaced by \(\hat{A}\). This would correspond to so-called "indirect adaptive control." The second approach would be to use the sample path right from time \(t = 0\), and adjust *only one* component of the estimated value function at each time instant \(t\). This would correspond to so-called "direct adaptive control." Using a similar approach, it is also possible to estimate the action-value function based on a single sample path. We describe two such algorithms, namely Temporal Difference learning for estimating the value function of a Markov reward process, and \(Q\)-learning for estimating the action-function of a Markov Decision Process. Within Temporal Difference, we make a further distinction between estimating the full value vector, and estimating a projection of the value vector onto a lower-dimensional subspace.

#### 3.3.1 Temporal Difference Learning Without Function Approximation

In this subsection and the next, we describe the so-called "temporal difference" family of algorithms, first introduced in [31]. The objective of the algorithm is to compute the value vector of a Markov reward process. Recall that the value vector \(\mathbf{v}\) of a Markov reward process satisfies (6). In Temporal Difference approach, it is *not* assumed that the state transition matrix \(A\) is known. Rather, it is assumed that the learner has available a sample path \(\{(X_t)\}\) of the Markov process under study, together with the associated reward at each time. For simplicity it is assumed that the reward is deterministic and not random. Thus the reward at time \(t\) is just \(R(X_t)\) and does not add any information.

There are two variants of the algorithm. In the first, one constructs a sequence of approximations \(\hat{\mathbf{v}}_t\) that, one hopes, would converge to the true value vector \(\mathbf{v}\) as \(t \to \infty\). In the second, which is used when \(n\) is very large, one chooses a "basis representation matrix" \(\Psi \in \mathbb{R}^{n \times d}\), where \(d \ll n\). Then one constructs a sequence of vectors \(\boldsymbol{\theta}_t \in \mathbb{R}^d\), such that the corresponding sequence of vectors \(\Psi \boldsymbol{\theta}_t \in \mathbb{R}^n\) forms an approximation to the value vector \(\mathbf{v}\). Since there is no *a priori* reason to believe that \(\mathbf{v}\) belongs to the range of \(\Psi\), there is also no reason to believe that \(\Psi \boldsymbol{\theta}_t\) would converge to \(\mathbf{v}\). The second approach is called Temporal Difference Learning with function approximation. The first is studied in this subsection, while the second is studied in the next subsection.

In principle, by observing the sample path for a sufficiently long duration, it is possible to make a reliable estimate of \(A\). However, a key feature of the temporal difference algorithm is that it is a "direct" method, which works directly with the sample path, without attempting to infer the underlying Markov process. With the sample path \(\{X_t\}\) of the Markov process, one can associate a corresponding "index process" \(\{N_t\}\) taking values in \([n]\), as follows:

$$
N_t = i \text{ if } X_t = x_i \in \mathcal{X}.
$$

It is obvious that the index process has the same transition matrix \(A\) as the process \(\{X_t\}\). The idea is to start with an initial estimate \(\hat{\mathbf{v}}_0\), and update it at each time \(t\) based on the sample path \(\{(X_t, R(X_t))\}\).

Now we introduce the \(TD(\lambda)\) algorithm studied in this paper. This version of the \(TD(\lambda)\) algorithm comes from [16, Eq. (4.7)], and is as follows: Let \(\mathbf{v}^*\) denote the unique solution of the

14

<!-- page: 15 -->

equation[^2]

$$
\mathbf{v}^* = \mathbf{r} + \gamma A \mathbf{v}^*.
$$

At time \(t\), let \(\hat{\mathbf{v}}_t \in \mathbb{R}^n\) denote the current estimate of \(\mathbf{v}^*\). Thus the \(i\)-th component of \(\hat{\mathbf{v}}_t\), denoted by \(\hat{V}_{t,i}\), is the estimate of the reward when the initial state is \(x_i\). Let \(\{N_t\}\) be the index process defined above. Define

$$
\delta_{t+1} := R_{N_t} + \gamma \hat{V}_{t,N_{t+1}} - \hat{V}_{t,N_t}, \ \forall t \geq 0,
\tag{33}
$$

where \(\hat{V}_{t,N_t}\) denotes the \(N_t\)-th component of the vector \(\hat{\mathbf{v}}_t\). Equivalently, if the state at time \(t\) is \(x_i \in \mathcal{X}\) and the state at the next time \(t+1\) is \(x_j\), then

$$
\delta_{t+1} = R_i + \gamma \hat{V}_{t,j} - \hat{V}_{t,i}.
\tag{34}
$$

Next, choose a number \(\lambda \in [0,1)\). Define the "eligibility vector"

$$
\mathbf{z}_t = \sum_{\tau=0}^{t} (\gamma\lambda)^{\tau} I_{\{N_{t-\tau} = N_t\}} \mathbf{e}_{N_{t-\tau}},
\tag{35}
$$

where \(\mathbf{e}_{N_s}\) is a unit vector with a 1 in location \(N_s\) and zeros elsewhere. Since the indicator function in the above summation picks up only those occurrences where \(N_{t-\tau} = N_t\), the vector \(\mathbf{z}_t\) can also be expressed as

$$
\mathbf{z}_t = z_t \mathbf{e}_{N_t}, z_t = \sum_{\tau=0}^{t} (\gamma\lambda)^{\tau} I_{\{N_{t-\tau} = N_t\}}.
\tag{36}
$$

Thus the support of the vector \(\mathbf{z}_t\) consists of the singleton \(\{N_t\}\). Finally, update the estimate \(\hat{\mathbf{v}}_t\) as

$$
\hat{\mathbf{v}}_{t+1} = \hat{\mathbf{v}}_t + \delta_{t+1}\alpha_t \mathbf{z}_t,
\tag{37}
$$

where \(\{\alpha_t\}\) is a sequence of step sizes. Note that, at time \(t\), only the \(N_t\)-th component of \(\hat{\mathbf{v}}_t\) is updated, and the rest remain the same.

A sufficient condition for the convergence of the \(TD(\lambda)\)-algorithm is given in [16].

**Theorem 9.** *The sequence \(\{\hat{\mathbf{v}}_t\}\) converges almost surely to \(\mathbf{v}^*\) as \(t \to \infty\), provided*

$$
\sum_{t=0}^{\infty} \alpha_t^2 I_{\{N_t = i\}} < \infty, \ a.s., \ \forall i \in [n],
\tag{38}
$$

$$
\sum_{t=0}^{\infty} \alpha_t I_{\{N_t = i\}} = \infty, \ a.s., \ \forall i \in [n],
\tag{39}
$$

#### 3.3.2 \(TD\)-Learning with Function Approximation

In this set-up, we again observe a time series \(\{(X_t, R(X_t))\}\). The new feature is that there is a "basis" matrix \(\Psi \in \mathbb{R}^{n \times d}\), where \(d \ll n\). The estimated value vector at time \(t\) is given by \(\hat{v}_t = \Psi\boldsymbol{\theta}_t\), where \(\boldsymbol{\theta}_t \in \mathbb{R}^d\) is the parameter to be updated. In this representation, it is clear that, for any index \(i \in [n]\), we have that

$$
\hat{V}_{t,i} = \Psi^i \boldsymbol{\theta}_t = \langle (\Psi^i)^{\top}, \boldsymbol{\theta}_t \rangle,
$$

[^2]: For clarity, we have changed the notation so that the value vector is now denoted by \(\mathbf{v}^*\) instead of \(\mathbf{v}\) as in (6).

15

<!-- page: 16 -->

where \(\Psi^i\) denotes the \(i\)-th row of the matrix \(\Psi\).

Now we define the learning rule for updating \(\boldsymbol{\theta}_t\). Let \(\{X_t\}\) be the observed sample path. By a slight abuse of notation, define

$$
\mathbf{y}_t = [\Psi^{X_t}]^{\top} \in \mathbb{R}^d.
$$

Thus, if \(X_t = x_i\), then \(\mathbf{y}_t = [\Psi^i]^{\top}\). The **eligibility vector** \(\mathbf{z}_t \in \mathbb{R}^d\) is defined via

$$
\mathbf{z}_t = \sum_{\tau=0}^{t} (\gamma\lambda)^{t-\tau} \mathbf{y}_{\tau}.
\tag{40}
$$

Note that \(\mathbf{z}_t\) satisfies the recursion

$$
\mathbf{z}_t = \gamma\lambda \mathbf{z}_{t-1} + \mathbf{y}_t.
$$

Hence it is not necessary to keep track of an ever-growing set of past values of \(\mathbf{y}_{\tau}\). In contrast to (35), there is no term of the type \(I_{\{N_{t-\tau} = N_t\}}\) in (40). Thus, unlike the eligibility vector defined in (35), the current vector \(\mathbf{z}_t\) can have more than one nonzero component. Next, define the temporal difference \(\delta_{t+1}\) as in (33). Note that, if \(X_t = x_i\) and \(X_{t+1} = x_j\), then

$$
\delta_{t+1} = r_i + \gamma[\Psi^j]^{\top}\boldsymbol{\theta}_t - [\Psi^i]^{\top}\boldsymbol{\theta}_t.
$$

Then the updating rule is

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \alpha_t \delta_{t+1} \mathbf{z}_t,
\tag{41}
$$

where \(\alpha_t\) is the step size.

The convergence analysis of (41) is carried out in detail in [38], based on the assumption that the state transition matrix \(A\) is irreducible. This is quite reasonable, as it ensures that every state \(x_i\) occurs infinitely often in any sample path, with probability one. Since that convergence analysis does not readily fit into the methods studied in subsequent sections, we state the main results without proof. However, we state and prove various intermediate results, that are useful in their own right.

Suppose \(A\) is row-stochastic and irreducible, and let \(\boldsymbol{\mu}\) denote its stationary distribution. Define \(M = \text{Diag}(\mu_i)\) and define a norm \(\|\cdot\|_M\) on \(\mathbb{R}^d\) by

$$
\|\mathbf{v}\|_M = (\mathbf{v}^{\top} M \mathbf{v})^{1/2}.
$$

Then the corresponding distance between two vectors \(\mathbf{v}_1, \mathbf{v}_2\) is given by

$$
\|\mathbf{v}_1 - \mathbf{v}_2\|_M = ((\mathbf{v}_1 - \mathbf{v}_2)^{\top} M(\mathbf{v}_1 - \mathbf{v}_2))^{1/2}.
$$

Then the following result is proved in [38].

**Lemma 1.** *Suppose \(A \in [0,1]^{n \times n}\), is row-stochastic, and irreducible. Let \(\boldsymbol{\mu}\) be the stationary distribution of \(A\). Then*

$$
\|A\mathbf{v}\|_M \leq \|\mathbf{v}\|_M, \ \forall \mathbf{v} \in \mathbb{R}^n.
$$

*Consequently, the map \(\mathbf{v} \mapsto \mathbf{r} + \gamma A \mathbf{v}\) is a contraction with respect to \(\|\cdot\|_M\).*

*Proof.* We will show that

$$
\|A\mathbf{v}\|_M^2 \leq \|\mathbf{v}\|_M^2, \ \forall \mathbf{v} \in \mathbb{R}^n,
$$

16
<!-- page: 17 -->

which is clearly equivalent to the \(\|A\mathbf{v}\|_M \leq \|\mathbf{v}\|_M\). Now

$$
\|A\mathbf{v}\|_M^2 = \sum_{i=1}^{n} \mu_i (A\mathbf{v})_i^2 = \sum_{i=1}^{n} \mu_i \left(\sum_{j=1}^{n} A_{ij} v_j\right)^2.
$$

However, for each fixed index \(i\), the row \(A^i\) is a probability distribution, and the function \(f(Y) = Y^2\) is convex. If we apply Jensen's inequality with \(f(Y) = Y^2\), we see that

$$
\left(\sum_{j=1}^{n} A_{ij} v_j\right)^2 \leq \sum_{j=1}^{n} A_{ij} v_j^2, \ \forall i.
$$

Therefore

$$
\begin{aligned}
\|A\mathbf{v}\|_M^2 &\leq \sum_{i=1}^{n} \mu_i \left(\sum_{j=1}^{n} A_{ij} v_j^2\right) = \sum_{j=1}^{n} \left(\sum_{i=1}^{n} \mu_i A_{ij}\right) v_j^2 \\
&= \sum_{j=1}^{n} \mu_j v_j^2 = \|\mathbf{v}\|_M^2,
\end{aligned}
$$

where in the last step we use the fact that \(\boldsymbol{\mu}A = \boldsymbol{\mu}\). □

To analyze the behavior of the \(TD(\lambda)\) algorithm with function approximation, the following map \(T^{\lambda} : \mathbb{R}^n \to \mathbb{R}^n\) is defined in [38]:

$$
[T^{\lambda}\mathbf{v}]_i := (1 - \lambda) \sum_{l=0}^{\infty} \lambda^l E\left[\sum_{\tau=0}^{l} \gamma^{\tau} R(X_{\tau+1}) + \gamma^{l+1} V_{X_{l+1}} | X_0\ x_i\right].
$$

Note that \(T^{\lambda}\mathbf{v}\) can be written explicitly as

$$
T^{\lambda}\mathbf{v} = (1 - \lambda) \sum_{l=0}^{\infty} \lambda^l \left[\sum_{\tau=0}^{l} \gamma^{\tau} A^{\tau} \mathbf{r} + \gamma^{l+1} A^{l+1} \mathbf{v}\right].
$$

**Lemma 2.** *The map \(T^{\lambda}\) is a contraction with respect to \(\|\cdot\|_M\), with contraction constant \([\gamma(1-\lambda)]/(1 - \gamma\lambda)\).*

*Proof.* Note that the first term on the right side of does not depend on \(\mathbf{v}\). Therefore

$$
T^{\lambda}(\mathbf{v}_1 - \mathbf{v}_2) = \gamma(1 - \lambda) \sum_{l=0}^{\infty} (\gamma\lambda)^l A^{l+1}(\mathbf{v}_1 - \mathbf{v}_2).
$$

However, it is already known that

$$
\|A(\mathbf{v}_1 - \mathbf{v}_2)\|_M \leq \|\mathbf{v}_1 - \mathbf{v}_2\|_M.
$$

By repeatedly applying the above, it follows that

$$
\|A^l(\mathbf{v}_1 - \mathbf{v}_2)\|_M \leq \|\mathbf{v}_1 - \mathbf{v}_2\|_M, \ \forall l.
$$

Therefore

$$
\|T^{\lambda}(\mathbf{v}_1 - \mathbf{v}_2)\|_M \leq \gamma(1 - \lambda) \sum_{l=0}^{\infty} (\gamma\lambda)^l \|\mathbf{v}_1 - \mathbf{v}_2\|_M = \frac{\gamma(1-\lambda)}{1 - \gamma\lambda} \|\mathbf{v}_1 - \mathbf{v}_2\|_M.
$$

This is the desired bound. □

17

<!-- page: 18 -->

Define a projection \(\Pi : \mathbb{R}^n \to \mathbb{R}^n\) by

$$
\Pi \mathbf{a} := \Psi(\Psi^{\top} M \Psi)^{-1} \Psi^{\top} M \mathbf{a}.
$$

Then

$$
\Pi \mathbf{a} = \arg \min_{\mathbf{b} \in \Psi(\mathbb{R}^d)} \|\mathbf{a} - \mathbf{b}\|_M.
$$

Thus \(\Pi\) projects the space \(\mathbb{R}^n\) onto the image of the matrix \(\Psi\), which is a \(d\)-dimensional subspace, if \(\Psi\) has full column rank. In other words, \(\Pi\mathbf{a}\) is the closest point to \(\mathbf{a}\) in the subspace \(\Psi(\mathbb{R}^n)\).

Next, observe that the projection \(\Pi\) is nonexpansive with respect to \(\|\cdot\|_M\). As a result, the composite map \(\Pi T^{\lambda}\) is a contraction. Thus there exists a unique \(\bar{v} \in \mathbb{R}^d\) such that

$$
\Pi T^{\lambda} \bar{v} = \bar{v}.
$$

Moreover, the above equation shows that in fact \(\bar{v}\) belongs to the range of \(\Psi\). Thus there exists a \(\boldsymbol{\theta}^* \in \mathbb{R}^d\) such that \(\bar{v} = \Psi\boldsymbol{\theta}^*\), and \(\boldsymbol{\theta}^*\) is unique if \(\Psi\) has full column rank.

The limit behavior of the \(TD(\lambda)\) algorithm is given by the next theorem, which is a key result from [38].

**Theorem 10.** *Suppose that \(\Psi\) has full column rank, and that*

$$
\sum_{t=0}^{\infty} \alpha_t = \infty, \sum_{t=0}^{\infty} \alpha_t^2 < \infty.
$$

*Then the sequence \(\{\boldsymbol{\theta}_t\}\) converges almost surely to \(\boldsymbol{\theta}^* \in \mathbb{R}^d\), where \(\boldsymbol{\theta}^*\) is the unique solution of*

$$
\Pi T^{\lambda}(\Psi\boldsymbol{\theta}^*) = \Psi\boldsymbol{\theta}^*.
$$

*Moreover*

$$
\|\Psi\boldsymbol{\theta}^* - \mathbf{v}^*\|_M \leq \frac{1 - \gamma\lambda}{1 - \gamma} \|\Pi\mathbf{v}^* - \mathbf{v}^*\|_M.
$$

Note that, since \(\Psi\boldsymbol{\theta} \in \Pi(\mathbb{R}^d)\) for all \(\boldsymbol{\theta} \in \mathbb{R}^d\), the best that one can hope for is that

$$
\|\Psi\boldsymbol{\theta}^* - \mathbf{v}^*\|_M = \|\Pi\mathbf{v}^* - \mathbf{v}^*\|_M.
$$

The theorem states that the above identity might not hold, and provides an upper bound for the distance between the limit \(\Psi\boldsymbol{\theta}^*\) and the true value vector \(\mathbf{v}^*\). It is bounded by a factor \((1 - \gamma\lambda)/(1 - \gamma)\) times this minimum.

Note that \((1 - \gamma\lambda)/(1 - \gamma) > 1\). So this is the extent to which the \(TD(\lambda)\) iterations miss the optimal approximation.

#### 3.3.3 \(Q\)-Learning

The \(Q\)-learning algorithm proposed in [42] has the characterization (27) of \(Q^*\) as its starting point. The algorithm is based on the following premise: At time \(t\), the current state \(X_t\) can be observed; call it \(x_i \in \mathcal{X}\). Then the learner is free to choose the action \(U_t\); call it \(u_k \in \mathcal{U}\). With this choice, the next state \(X_{t+1}\) has the probability distribution equal to the \(i\)-th row of the state transition matrix \(A^{u_k}\). Suppose the observed next stat \(X_{t+1}\) is \(x_j \in \mathcal{X}\). With these conventions, the \(Q\)-learning algorithm proceeds as follows.

18

<!-- page: 19 -->

1. Choose an arbitrary initial guess \(Q_0 : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\) and an initial state \(X_0 \in \mathcal{X}\).

2. At time \(t\), with current state \(X_t = x_i\), choose a current action \(U_t = u_k \in \mathcal{U}\), and let the Markov process run for one time step. Observe the resulting next state \(X_{t+1} = x_j\). Then update the function \(Q_t\) as follows:

$$
\begin{aligned}
Q_{t+1}(x_i, u_k) &= Q_t(x_i, u_k) + \alpha_t[R(x_i, u_k) + \gamma V_t(x_j) - Q_t(x_i, u_k)], \\
Q_{t+1}(x_s, w_l) &= Q_t(x_s, w_l), \ \forall (x_s, w_l) \neq (x_i, u_k).
\end{aligned}
\tag{42}
$$

   where

$$
V_t(x_j) = \max_{w_l \in \mathcal{U}} Q_t(x_j, w_l),
\tag{43}
$$

   and \(\{\alpha_t\}\) is a deterministic sequence of step sizes.

3. Repeat.

It is evident that in the \(Q\)-learning algorithm, at any instant of time \(t\), only one element (namely \(Q(X_t, U_t)\)) gets updated. In the original paper by Watkins and Dayan [42], the convergence of the algorithm used some rather *ad hoc* methods. Subsequently, a general class of algorithms known as "asynchronous stochastic approximation," which included \(Q\)-learning as a special case, was introduced in [36, 16]. A sufficient condition for the convergence of the \(Q\)-learning algorithm, which was originally presented in [42], is rederived using these methods.

**Theorem 11.** *The \(Q\)-learning algorithm converges to the optimal action-value function \(Q^*\) provided the following conditions are satisfied.*

$$
\sum_{t=0}^{\infty} \alpha_t I_{(X_t, U_t) = (x_i, u_k)} = \infty, \ \forall (x_i, u_k) \in \mathcal{X} \times \mathcal{U},
\tag{44}
$$

$$
\sum_{t=0}^{\infty} \alpha_t^2 I_{(X_t, U_t) = (x_i, u_k)} < \infty, \ \forall (x_i, u_k) \in \mathcal{X} \times \mathcal{U}.
\tag{45}
$$

The main shortcoming of Theorems 9 and 11 is that the sufficient conditions (38), (39), (44) and (45) are *probabilistic* in nature. Thus it is not clear how they are to be verified in a specific application. Note that in the \(Q\)-learning algorithm, there is no guidance on how to choose the next action \(U_t\). Presumably \(U_t\) is chosen so as to ensure that (44) and (45) are satisfied. In Section 5, we show how these theorems can be proven, and also, how the troublesome probabilistic sufficient conditions can be replaced by purely algebraic conditions.

## 4 Stochastic Approximation Algorithms

### 4.1 Stochastic Approximation and Relevance to RL

The contents of the previous section make it clear that in MDP theory, a central role is played by *the need to solve fixed-point problems*. Determining the value of a Markov reward problem requires the solution of (6). Determining the optimal value of an MDP requires finding the fixed point of the Bellman iteration. Finally, determining the optimal policy for an MDP requires finding the fixed point of the \(F\)-iteration. As pointed out in Section 3.3, when the dynamics of an MDP are

19

<!-- page: 20 -->

completely known, these fixed point problems can be solved by repeatedly applying the corresponding contraction mapping. However, when the dynamics of the MDP are not known, and one has access only to a sample path of the MDP, a different approach is required. In Section 3.3, we have presented two such methods, namely the Temporal Difference algorithm for value determination, and the \(Q\)-Learning algorithm for determining the optimal action-value function. Theorems 9 and 11 respectively give sufficient conditions for the convergence of these algorithms. The proofs of these theorems, as given in the original papers, tend to be "one-off," that is, tailored to the specific algorithm. It is now shown that a probabilistic method known as "stochastic approximation " (SA) can be used to unify these methods in a common format. Moreover, instead of the convergence proofs being "one-off," the SA algorithm provides a unifying approach.

The applications of SA go beyond these two specific algorithms. There is another area called "Deep Reinforcement Learning" for problems in which the size of the state space is very large. Recall that the action-value function \(Q : \mathcal{X} \times \mathcal{U}\) can either be viewed as an \(nm\)-dimensional vector, or an \(n \times m\) matrix. In Deep RL, one determines (either exactly or approximately) the action-value function \(Q(x_i, u_k)\) for *a small number* of pairs \((x_i, u_k) \in \mathcal{X} \times \mathcal{U}\). Using these as a starting point, the overall function \(Q\) defined for *all* pairs \((x_i, u_k) \in \mathcal{X} \times \mathcal{U}\) is obtained by training a deep neural network. Training a neural network (in this or any other application) requires the minimization of the average mean-squared error, denoted by \(J(\boldsymbol{\theta})\) where \(\boldsymbol{\theta}\) denotes the vector of adjustable parameters. In general, the function \(J(\cdot)\) is not convex; hence one can at best aspire to find a *stationary point* of \(J(\cdot)\), i.e., a solution to the equation \(\nabla J(\boldsymbol{\theta}) = \mathbf{0}\). This problem is also amenable to the application of the SA approach.

Now we give a brief introduction to stochastic approximation. Suppose \(\mathbf{f} : \mathbb{R}^d \to \mathbb{R}^d\) is some function, and \(d\) can be any integer. The objective of SA is to find a solution to the equation \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{0}\), when only noisy measurements of \(\mathbf{f}(\cdot)\) are available. The SA method was introduced in [28], where the objective was to find a solution to a *scalar* equation \(f(\theta) = 0\), where \(f : \mathbb{R} \to \mathbb{R}\). The extension to the case where \(d > 1\) was first proposed in [5]. The problem of finding a fixed point of a map \(\mathbf{g} : \mathbb{R}^d \to \mathbb{R}^d\), can be formulated as the above problem with \(\mathbf{f}(\boldsymbol{\theta}) := \mathbf{g}(\boldsymbol{\theta}) - \boldsymbol{\theta}\). If it is desired to find a stationary point of a \(C^1\) function \(J : \mathbb{R}^d \to \mathbb{R}\), then we simply set \(\mathbf{f}(\boldsymbol{\theta}) = \nabla J(\boldsymbol{\theta})\). Thus the above problem formulation is quite versatile. More details are given at the start of Section 4.2.

Stochastic approximation is a family of *iterative* algorithms, in which one begins with an initial guess \(\boldsymbol{\theta}_0\), and derives the next guess \(\boldsymbol{\theta}_{t+1}\) from \(\boldsymbol{\theta}_t\). Several variants of SA are possible. In **synchronous SA**, *every* component of \(\boldsymbol{\theta}_t\) is changed to obtain \(\boldsymbol{\theta}_{t+1}\). This was the original concept of SA. If, at any time \(t\), *only one* component of \(\boldsymbol{\theta}_t\) is changed to obtain \(\boldsymbol{\theta}_{t+1}\), and the others remain unchanged, this is known as **asynchronous stochastic approximation (ASA)**. This phrase was apparently first introduced in [36], A variant of the approach in [36] is presented in [6]. Specifically, in [6], a distinction is introduced between using a "local clock" versus using a "global clock." It is also possible to study an intermediate situation where, at each time \(t\), *some but not necessarily all* components of \(\boldsymbol{\theta}_t\) are updated. There does not appear to be a common name for this situation. The phrase **Batch Asynchronous Stochastic Approximation (BASA)** is introduced in [17]. More details about these variations are given below. There is a fourth variant, known as **two time-scale SA** is introduced in [8]. In this set-up, one attempts to solve two *coupled* equations of the form

$$
\mathbf{f}(\boldsymbol{\theta}, \boldsymbol{\phi}) = \mathbf{0}, \mathbf{g}(\boldsymbol{\theta}, \boldsymbol{\phi}) = \mathbf{0},
$$

where \(\boldsymbol{\theta} \in \mathbb{R}^n, \boldsymbol{\phi} \in \mathbb{R}^m\), and \(\mathbf{f} : \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^n, \mathbf{g} : \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^m\). the idea is that one of the iterations (say \(\boldsymbol{\theta}_{t+1}\)) is updated "more slowly" than the other (say \(\boldsymbol{\phi}_{t+1}\)). Due to space limitations, two time-scale SA is not discussed further in this paper. The interested reader is

20

<!-- page: 21 -->

referred to [8, 35, 24] for the theory, and to [21, 20] for applications to a specific type of RL, known as **Actor-Critic Algorithms**.

The relevance of SA to RL arises from the following factors:

- Many (though not all) algorithms used in RL can formulated as some type of SA algorithms.

- Examples include Temporal Difference Learning, Temporal Difference Learning with function approximation, \(Q\)-Learning, Deep Neural Network Learning, and Actor-Critic Learning. The first three are discussed in detail in Section 5.

Thus: SA provides a *unifying framework* for several disparate-looking RL algorithms.

### 4.2 Problem Formulation

There are several equivalent formulations of the basic SA problem.

1. **Finding a zero of a function:** Suppose \(\mathbf{f} : \mathbb{R}^d \to \mathbb{R}^d\) is some function. Note that \(\mathbf{f}(\cdot)\) need not be available in closed form. The only thing needed is that, given any \(\boldsymbol{\theta} \in \mathbb{R}^d\), an "oracle" returns a noise-corrupted version of \(\mathbf{f}(\boldsymbol{\theta})\). The objective is to determine a solution of the equation \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{0}\).

2. **Finding a fixed point of a mapping:** Suppose \(\mathbf{g} : \mathbb{R}^d \to \mathbb{R}^d\). The objective is to find a fixed point of \(\mathbf{g}(\cdot)\), that is, a solution to \(\mathbf{g}(\boldsymbol{\theta}) = \boldsymbol{\theta}\). If we define \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{g}(\boldsymbol{\theta}) - \boldsymbol{\theta}\), this is the same problem as the above. One might ask: Why not define \(\mathbf{f}(\boldsymbol{\theta}) = \boldsymbol{\theta} - \mathbf{g}(\boldsymbol{\theta})\)? As we shall see below, the convergence of the SA algorithm (in various forms) is closely related to the global asymptotic stability of the ODE \(\dot{\boldsymbol{\theta}} = \mathbf{f}(\boldsymbol{\theta})\). Also, as seen in the previous section, in many applications, the map \(\mathbf{g}(\cdot)\) of which we wish to find a fixed point is a contraction. In such a case, there is a unique fixed point \(\boldsymbol{\theta}^*\) of \(\mathbf{g}(\cdot)\). In such a case, under relatively mild conditions \(\boldsymbol{\theta}^*\) is a globally asymptotically stable equilibrium of the ODE \(\dot{\boldsymbol{\theta}} = \mathbf{g}(\boldsymbol{\theta}) - \boldsymbol{\theta}\), but not if the sign is reversed.

3. **Finding a stationary point of a function:** Suppose \(J : \mathbb{R}^d \to \mathbb{R}\) is a \(\mathcal{C}^1\) function. The objective is to find a stationary point of \(J(\cdot)\), that is, a \(\boldsymbol{\theta}\) such that \(\nabla J(\boldsymbol{\theta}) = \mathbf{0}\). If we define \(\mathbf{f}(\boldsymbol{\theta}) = -\nabla J(\boldsymbol{\theta})\), then this is the same problem as above. Here again, if we wish the SA algorithm to converge to a global *minimum* of \(J(\cdot)\), then the minus sign is essential. On the other hand, if we wish the SA algorithm to converge to a global *maximum* of \(J(\cdot)\), then we remove the minus sign.

Suppose the problem is one of finding a zero of a given function \(\mathbf{f}(\cdot)\). The **synchronous** version of SA proceeds as follows: An initial guess \(\boldsymbol{\theta}_0 \in \mathbb{R}^d\) is chosen (usually in a deterministic manner, but it can also be randomly chosen). At time \(t\), the available measurement is

$$
\mathbf{y}_{t+1} = \mathbf{f}(\boldsymbol{\theta}_t) + \boldsymbol{\xi}_{t+1},
\tag{46}
$$

where \(\boldsymbol{\xi}_{t+1}\) is the measurement noise. Based on this, the current guess is updated to

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \alpha_t \mathbf{y}_{t+1} = \boldsymbol{\theta}_t + \alpha_t[\mathbf{f}(\boldsymbol{\theta}_t) + \boldsymbol{\xi}_{t+1}],
\tag{47}
$$

where \(\{\alpha_t\}\) is a predefined sequence of "step sizes," with \(\alpha_t \in (0,1)\) for all \(t\). If the problem is that of finding a fixed point of \(\mathbf{g}(\cdot)\), the updating rule is

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \alpha_t[\mathbf{g}(\boldsymbol{\theta}_t) - \boldsymbol{\theta}_t + \boldsymbol{\xi}_{t+1}] = (1 - \alpha_t)\boldsymbol{\theta}_t + \alpha_t[\mathbf{g}(\boldsymbol{\theta}_t) + \boldsymbol{\xi}_{t+1}].
\tag{48}
$$

21

<!-- page: 22 -->

If the problem is to find a stationary point of \(J(\cdot)\), the updating rule is

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \alpha_t \mathbf{y}_{t+1} = \boldsymbol{\theta}_t + \alpha_t[-\nabla J(\boldsymbol{\theta}_t) + \boldsymbol{\xi}_{t+1}].
\tag{49}
$$

These updating rules represent what might be called **Synchronous SA**, because at each time \(t\), *every* component of \(\boldsymbol{\theta}_t\) is updated. Other variants of SA are studied in subsequent sections.

### 4.3 A New Theorem for Global Asymptotic Stability

In this section we state a new theorem on the global asymptotic stability of nonlinear ODEs. This theorem is new and is of interest aside from its applications to the convergence of SA algorithms. The contents of this section and the next section are taken from [41]. To state the result (Theorem 12 below), we introduce a few preliminary concepts from Lyapunov stability theory. The required background can be found in [39, 15, 18].

**Definition 1.** *A function \(\phi : \mathbb{R}_+ \to \mathbb{R}_+\) is said to **belong to class \(\mathcal{K}\)**, denoted by \(\phi \in \mathcal{K}\), if \(\phi(0) = 0\), and \(\phi(\cdot)\) is strictly increasing. A function \(\phi \in \mathcal{K}\) is said to **belong to class \(\mathcal{KR}\)**, denoted by \(\phi \in \mathcal{KR}\), if in addition, \(\phi(r) \to \infty\) as \(r \to \infty\). A function \(\phi : \mathbb{R}_+ \to \mathbb{R}_+\) is said to **belong to class \(\mathcal{B}\)**, denoted by \(\phi \in \mathcal{B}\), if \(\phi(0) = 0\), and in addition, for all \(0 < \epsilon < M < \infty\) we have that*

$$
\inf_{\epsilon \leq r \leq M} \phi(r) > 0.
\tag{50}
$$

The concepts of functions of class \(\mathcal{K}\) and class \(\mathcal{KR}\) are standard. The concept of a function of class \(\mathcal{B}\) is new. Note that, if \(\phi(\cdot)\) is continuous, then it belongs to Class \(\mathcal{B}\) if and only if \(\phi(0) = 0\), and \(\phi(r) > 0\) for all \(r > 0\).

**Example 3.** *Observe that every \(\phi\) of class \(\mathcal{K}\) also belongs to class \(\mathcal{B}\). However, the converse is not true. Define*

$$
\phi(r) = \left\{\begin{array}{ll} r, & \text{if } r \in [0,1], \\ e^{-(r-1)}, & \text{if } r > 1. \end{array}\right.
$$

*Then \(\phi\) belongs to Class \(\mathcal{B}\). However, since \(\phi(r) \to 0\) as \(r \to \infty\), \(\phi\) cannot be bounded below by any function of class \(\mathcal{K}\).*

Suppose we wish to find a solution of \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{0}\). The convergence analysis of synchronous SA depends on the stability of an associated ODE \(\dot{\boldsymbol{\theta}} = \mathbf{f}(\boldsymbol{\theta})\). We now state a new theorem on global asymptotic stability, and then use this to establish the convergence of the synchronous SA algorithm. In order to state this theorem, we first introduce some standing assumptions on \(\mathbf{f}(\cdot)\). Note that these assumptions are standard in the literature.

(F1) The equation \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{0}\) has a unique solution \(\boldsymbol{\theta}^*\).

(F2) The function \(\mathbf{f}\) is globally Lipschitz-continuous with constant \(L\).

$$
\|\mathbf{f}(\boldsymbol{\theta}) - \mathbf{f}(\boldsymbol{\phi})\|_2 \leq L\|\boldsymbol{\theta} - \boldsymbol{\phi}\|_2, \ \forall \boldsymbol{\theta}, \boldsymbol{\phi} \in \mathbb{R}^d.
\tag{51}
$$

**Theorem 12.** *Suppose Assumption (F1) holds, and that there exists a function \(V : \mathbb{R}^d \to \mathbb{R}_+\) and functions \(\eta, \psi \in \mathcal{KR}, \phi \in \mathcal{B}\) such that*

$$
\eta(\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2) \leq V(\boldsymbol{\theta}) \leq \psi(\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2), \ \forall \boldsymbol{\theta} \in \mathbb{R}^d,
\tag{52}
$$

$$
\dot{V}(\boldsymbol{\theta}) \leq -\phi(\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2), \ \forall \boldsymbol{\theta} \in \mathbb{R}^d,
\tag{53}
$$

*Then \(\boldsymbol{\theta}^*\) is a globally asymptotically stable equilibrium of the ODE \(\dot{\boldsymbol{\theta}} = \mathbf{f}(\boldsymbol{\theta})\).*

22

<!-- page: 23 -->

This is [41, Theorem 4], and the proof can be found therein. Well-known classical theorems for global asymptotic stability, such as those found in [15, 39, 18], require the function \(\phi(\cdot)\) to belong to Class \(\mathcal{K}\). Theorem 12 is an improvement, in that the function \(\phi(\cdot)\) is required only to belong to the larger Class \(\mathcal{B}\).

### 4.4 A Convergence Theorem for Synchronous Stochastic Approximation

In this subsection we present a convergence theorem for synchronous stochastic approximation. Theorem 13 below is sightly more general than a corresponding result in [41]. This theorem is obtained by combining some results from [41] and [17]. Other convergence theorems and examples can be found in [41].

In order to analyze the convergence of the SA algorithm, we need to make some assumptions about the nature of the measurement error sequence \(\{\boldsymbol{\xi}_t\}\). These assumptions are couched in terms of the conditional expectation of a random variable with respect to a \(\sigma\)-algebra. Readers who are unfamiliar with the concept are referred to [13] for the relevant background.

Let \(\boldsymbol{\theta}_0^t\) denote the tuple \(\boldsymbol{\theta}_0, \boldsymbol{\theta}_1, \cdots, \boldsymbol{\theta}_t\), and define \(\boldsymbol{\xi}_1^t\) analogously; note that there is no \(\boldsymbol{\xi}_0\). Let \(\{\mathcal{F}_t\}_{t\geq 0}\) be any filtration (i.e., increasing sequence of \(\sigma\)-algebras), such that \(\boldsymbol{\theta}_0^t, \boldsymbol{\xi}_1^t\) are measurable with respect to \(\mathcal{F}_t\). For example, one can choose \(\mathcal{F}_t\) to be the \(\sigma\)-algebra generated by the tuples \(\boldsymbol{\theta}_0^t, \boldsymbol{\xi}_1^t\).

(N1) There exists a sequence \(\{b_t\}\) of nonnegative numbers such that

$$
\|E(\boldsymbol{\xi}_{t+1}|\mathcal{F}_t)\|_2 \leq b_t \text{ a.s.}, \ \forall t \geq 0.
\tag{54}
$$

   Thus \(b_t\) provides a bound on the Euclidean norm of the conditional expectation of the measurement error with respect to the \(\sigma\)-algebra \(\mathcal{F}_t\).

(N2) There exists a sequence \(\{\sigma_t\}\) of nonnegative numbers such that

$$
E(\|\boldsymbol{\xi}_{t+1} - E(\boldsymbol{\xi}_{t+1}|\mathcal{F}_t)\|_2^2|\mathcal{F}_t) \leq \sigma_t^2(1 + \|\boldsymbol{\theta}_t\|_2^2), \text{ a.s. } \forall t \geq 0.
\tag{55}
$$

Note that the quantity on the left side of (55) is the conditional variance of \(\boldsymbol{\xi}_{t+1}\) with respect to the \(\sigma\)-algebra \(\mathcal{F}_t\).

Now we can state a theorem about the convergence of synchronous SA.

**Theorem 13.** *Suppose \(\mathbf{f}(\boldsymbol{\theta}^*) = \mathbf{0}\), and Assumptions (F1–F2) and (N1–N2) hold. Suppose in addition that there exists a \(\mathcal{C}^2\) Lyapunov function \(V : \mathbb{R}^d \to \mathbb{R}_+\) that satisfies the following conditions:*

- *There exist constants \(a, b > 0\) such that*

$$
a\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2^2 \leq V(\boldsymbol{\theta}) \leq b\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2^2, \ \forall \boldsymbol{\theta} \in \mathbb{R}^d.
\tag{56}
$$

- *There is a finite constant \(M\) such that*

$$
\|\nabla^2 V(\boldsymbol{\theta})\|_S \leq 2M, \ \forall \boldsymbol{\theta} \in \mathbb{R}^d.
\tag{57}
$$

*With these hypothesis, we can state the following conclusions:*

23

<!-- page: 24 -->

1. *If \(\dot{V}(\boldsymbol{\theta}) \leq 0\) for all \(\boldsymbol{\theta} \in \mathbb{R}^d\), and if*

$$
\sum_{t=0}^{\infty} \alpha_t^2 < \infty, \sum_{t=0}^{\infty} \alpha_t b_t < \infty, \sum_{t=0}^{\infty} \alpha_t^2 \sigma_t^2 < \infty,
\tag{58}
$$

   *then the iterations \(\{\boldsymbol{\theta}_t\}\) are bounded almost surely.*

2. *Suppose further that there exists a function \(\phi \in \mathcal{B}\) such that*

$$
\dot{V}(\boldsymbol{\theta}) \leq -\phi(\|\boldsymbol{\theta} - \boldsymbol{\theta}^*\|_2), \ \forall \boldsymbol{\theta} \in \mathbb{R}^d.
\tag{59}
$$

   *and in addition to (58), we also have*

$$
\sum_{t=0}^{\infty} \alpha_t = \infty,
\tag{60}
$$

   *Then \(\boldsymbol{\theta}_t \to \boldsymbol{\theta}^*\) almost surely as \(t \to \infty\).*

Observe the nice "division of labor" between the two conditions: Equation (58) guarantees the almost sure boundedness of the iterations, while the addition of (60) leads to the almost sure convergence of the iterations to the desired limit, namely the solution of \(\mathbf{f}(\boldsymbol{\theta}) = \mathbf{0}\). This division of labor is first found in [14]. Theorem 13 is a substantial improvement on [7], which were the previously best results. The interested reader is referred to [41] for further details.

Theorem 13 is a slight generalization of [41, Theorem 5]. In that theorem, it is assumed that \(b_t = 0\) for all \(t\), and that the constants \(\sigma_t\) are uniformly bounded by some constant \(\sigma\). In this case (58) and (60) become

$$
\sum_{t=0}^{\infty} \alpha_t^2 < \infty, \sum_{t=0}^{\infty} \alpha_t = \infty.
\tag{61}
$$

These two conditions are usually referred to as the Robbins-Monro conditions.

### 4.5 Convergence of Batch Asynchronous Stochastic Approximation

Equations (47) through (49) represent what might be called **Synchronous SA**, because at each time \(t\), *every* component of \(\boldsymbol{\theta}_t\) is updated. Variants of synchronous SA include Asynchronous SA (ASA), where at each time \(t\), exactly one component of \(\boldsymbol{\theta}_t\) is updated, and Batch Asynchronous SA (BASA), where at each time \(t\), some but not necessarily all components of \(\boldsymbol{\theta}_t\) are updated. We present the results for BASA, because ASA is a special case of BASA. Moreover, we focus on (48), where the objective is to find a fixed point of a contractive map \(\mathbf{g}\). The modifications required for (47) and (49) are straight-forward.

The relevant reference for these results is [17]. As a slight modification of (46), it is assumed that, at each time \(t+1\), there is available a noisy measurement

$$
\mathbf{y}_{t+1} = \mathbf{g}(\boldsymbol{\theta}_t) - \boldsymbol{\theta}_t + \boldsymbol{\xi}_{t+1}.
\tag{62}
$$

We assume that there is a given *deterministic* sequence of "step sizes" \(\{\beta_t\}\). In BASA, not every component of \(\boldsymbol{\theta}_t\) is updated at time \(t\). To determine which components are to be updated, we define \(d\) different binary "update processes" \(\{\kappa_{t,i}\}\), \(i \in [d]\). No assumptions are made regarding their independence. At time \(t\), define

$$
S(t) := \{i \in [d] : \kappa_{t,i} = 1\}.
\tag{63}
$$

24
<!-- page: 25 -->

This means that

$$
\theta_{t+1,i} = \theta_{t,i}, \ \forall i \notin S(t).
\tag{64}
$$

In order to define \(\theta_{t+1,i}\) when \(i \in S(t)\), we make a distinction between two different approaches: global clocks and local clocks. If a global clock is used, then

$$
\alpha_{t,i} = \beta_t, \ \forall i \in S(t), \alpha_{t,i} = 0, \ \forall i \notin S(t).
\tag{65}
$$

If a local clock is used, then we first define the local counter

$$
\nu_{t,i} = \sum_{\tau=0}^{t} \kappa_{\tau,i}, i \in [d],
\tag{66}
$$

which is the total number of occasions when \(i \in S(\tau)\), \(0 \leq \tau \leq t\). Equivalently, \(\nu_{t,i}\) is the total number of times up to and including time \(t\) when \(\theta_{\tau,i}\) is updated. With this convention, we define

$$
\alpha_{t,i} = \beta_{\nu_{t,i}}, \ \forall i \in S(t), \alpha_{t,i} = 0, \ \forall i \notin S(t).
\tag{67}
$$

The distinction between global clocks and local clocks was apparently introduced in [6]. Traditional RL algorithms such as \(TD(\lambda)\) and \(Q\)-learning, discussed in detail in Section 3.3 and again in Sections 5.2 and 5.3, use a global clock. That is not surprising because [6] came after [31] and [42]. It is shown in [17] that the use of local clocks actually simplifies the analysis of these algorithms.

Now we present the BASA updating rules. Let us define the "step size vector" \(\boldsymbol{\alpha}_t \in \mathbb{R}_+^d\) via (65) or (67) as appropriate. Then the update rule is

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t + \boldsymbol{\alpha}_t \circ \mathbf{y}_{t+1},
\tag{68}
$$

where \(\mathbf{y}_{t+1}\) is defined in (62). Here, the symbol \(\circ\) denotes the Hadamard product of two vectors of equal dimensions. Thus if \(\mathbf{a}, \mathbf{b}\) have the same dimensions, then \(\mathbf{c} = \mathbf{a} \circ \mathbf{b}\) is defined by \(c_i = a_i b_i\) for all \(i\).

Recall that we are given a function \(\mathbf{g} : \mathbb{R}^d \to \mathbb{R}^d\), and the objective is to find a solution to the fixed-point equation \(\mathbf{g}(\boldsymbol{\theta}) = \boldsymbol{\theta}\). Towards this end, we begin by stating the assumptions about the noise sequence.

(N1') There exists a sequence of constants \(\{b_t\}\) such that

$$
E(\|\boldsymbol{\xi}_{t+1}\|_2|\mathcal{F}_t) \leq b_t(1 + \|\boldsymbol{\theta}_0^t\|_{\infty}), \ \forall t \geq 0.
\tag{69}
$$

(N2') There exists a sequence of constants \(\{\sigma_t\}\) such that

$$
E(\|\boldsymbol{\xi}_{t+1} - E(\boldsymbol{\xi}_{t+1}|\mathcal{F}_t)\|_2^2|\mathcal{F}_t) \leq \sigma_t^2(1 + \|\boldsymbol{\theta}_0^t\|_{\infty}^2), \ \forall t \geq 0.
\tag{70}
$$

Comparing (54) and (55) with (69) and (70) respectively, we see that the term \(\|\boldsymbol{\theta}_t\|_2^2\) is replaced by \(\|\boldsymbol{\theta}_0^t\|_{\infty}\). So the constants \(b_t\) and \(\sigma_t\) can be different in the two cases. But because the two formulations is quite similar, we denote the first set of conditions as (N1) and (N2), and the second set of conditions as (N1') and (N2').

Next we state conditions on the step size sequence, which allow us to state the theorems in a compact manner. Next, we state the assumptions on the step size sequence. Note that, if a local clock is used, then \(\alpha_{t,i}\) can be random even if \(\beta_t\) is deterministic.

25

<!-- page: 26 -->

(S1) The random step size sequences \(\{\alpha_{t,i}\}\) and the sequences \(\{b_t\}\), \(\{\sigma_t^2\}\) and satisfy

$$
\sum_{t=0}^{\infty} \alpha_{t,i}^2 < \infty, \sum_{t=0}^{\infty} \sigma_t^2 \alpha_{t,i}^2 < \infty, \sum_{t=0}^{\infty} b_t \alpha_{t,i} < \infty, \text{ a.s., } \forall i \in [d].
\tag{71}
$$

(S2) The random step size sequence \(\{\alpha_{t,i}\}\) satisfies

$$
\sum_{t=0}^{\infty} \alpha_{t,i} = \infty, \text{ a.s., } \forall i \in [d].
\tag{72}
$$

Finally we state an assumption about the map \(\mathbf{g}\).

(G) \(\mathbf{g}\) is a contraction with respect to the \(\ell_{\infty}\)-norm with some contraction constant \(\gamma < 1\).

**Theorem 14.** *Suppose that Assumptions (N1') and (N2') about the noise sequence, (S1) about the step size sequence, and (G) about the function \(\mathbf{g}\) hold. Then \(\sup_t \|\boldsymbol{\theta}_t\|_{\infty} < \infty\) almost surely.*

**Theorem 15.** *Let \(\boldsymbol{\theta}^*\) denote the unique fixed point of \(\mathbf{g}\). Suppose that Assumptions (N1') and (N2') about the noise sequence, (S1) and (S2) about the step size sequence, and (G) about the function \(\mathbf{g}\) hold. Then \(\boldsymbol{\theta}_t\) converges almost surely to \(\boldsymbol{\theta}^*\) as \(t \to \infty\).*

The proofs of these theorems can be found in [17].

## 5 Applications to Reinforcement Learning

In this section, we apply the contents of the previous section to derive sufficient conditions for two distinct RL algorithms, namely Temporal Difference Learning (without function approximation), and \(Q\)-Learning. Previously known results are stated in Section 3.3. So what is the need to re-analyze those algorithms again from the standpoint of stochastic approximation? There are two reasons for doing so. First, the historical \(TD(\lambda)\) and \(Q\)-Learning algorithms are stated using a "global clock" as defined in Section 4.5. Subsequently, the concept of a "local clock" is introduced in [6]. In [17], the authors build upon this distinction to achieve two objectives. First, when a local clock is used, there are fewer assumptions. Second, by proving a result on the sample paths of an irreducible Markov process (proved in [17]), probabilistic conditions such as (38)–(39) and (44)–(45) are replaced by purely algebraic conditions.

### 5.1 A Useful Theorem About Irreducible Markov Processes

**Theorem 16.** *Suppose \(\{N(t)\}\) is a Markov process on \([d]\) with a state transition matrix \(A\) that is irreducible. Suppose \(\{\beta_t\}_{t\geq 0}\) is a sequence of real numbers in \((0,1)\) such that \(\beta_{t+1} \leq \beta_t\) for all \(t\), and*

$$
\sum_{t=0}^{\infty} \beta_t = \infty.
\tag{73}
$$

*Then*

$$
\sum_{t=0}^{\infty} \beta_t I_{\{N(t)=i\}}(\omega) = \sum_{t=0}^{\infty} \beta_t f_i(N(t)(\omega)) = \infty, \ \forall i \in [d], \ \forall \omega \in \Omega_0,
\tag{74}
$$

*where \(I\) denotes the indicator function.*

26

<!-- page: 27 -->

### 5.2 \(TD\)–Learning Without Function Approximation

Recall the \(TD(\lambda)\) algorithm without function approximation, presented in Section 3.3. One observes a time series \(\{(X_t, R(X_t))\}\) where \(\{X_t\}\) is a Markov process over \(\mathcal{X} = \{x_1, \cdots, x_n\}\) with a (possibly unknown) state transition matrix \(A\), and \(R : \mathcal{X} \to \mathbb{R}\) is a known reward function. With the sample path \(\{X_t\}\) of the Markov process, one can associate a corresponding "index process" \(\{N_t\}\) taking values in \([n]\), as follows:

$$
N_t = i \text{ if } X_t = x_i \in \mathcal{X}.
$$

It is obvious that the index process has the same transition matrix \(A\) as the process \(\{X_t\}\). The idea is to start with an initial estimate \(\hat{v}_0\), and update it at each time \(t\) based on the sample path \(\{(X_t, R_t)\}\).

Now we recall the \(TD(\lambda)\) algorithm without function approximation. At time \(t\), let \(\hat{\mathbf{v}}_t \in \mathbb{R}^n\) denote the current estimate of \(\mathbf{v}\). Let \(\{N_t\}\) be the index process defined above. Define the "temporal difference"

$$
\delta_{t+1} := R_{N_t} + \gamma \hat{V}_{t,N_{t+1}} - \hat{V}_{t,N_t}, \ \forall t \geq 0,
\tag{75}
$$

where \(\hat{V}_{t,N_t}\) denotes the \(N_t\)-th component of the vector \(\hat{\mathbf{v}}_t\). Equivalently, if the state at time \(t\) is \(x_i \in \mathcal{X}\) and the state at the next time \(t+1\) is \(x_j\), then

$$
\delta_{t+1} = R_i + \gamma \hat{V}_{t,j} - \hat{V}_{t,i}.
\tag{76}
$$

Next, choose a number \(\lambda \in [0,1)\). Define the "eligibility vector"

$$
\mathbf{z}_t = \sum_{\tau=0}^{t} (\gamma\lambda)^{\tau} I_{\{N_{t-\tau} = N_t\}} \mathbf{e}_{N_{t-\tau}},
\tag{77}
$$

where \(\mathbf{e}_{N_s}\) is a unit vector with a 1 in location \(N_s\) and zeros elsewhere. Finally, update the estimate \(\hat{\mathbf{v}}_t\) as

$$
\hat{\mathbf{v}}_{t+1} = \hat{\mathbf{v}}_t + \delta_{t+1}\alpha_t \mathbf{z}_t,
\tag{78}
$$

where \(\alpha_t\) is the step size chosen in accordance with either a global or a local clock. The distinction between the two is described next.

To complete the problem specification, we need to specify how the step size \(\alpha_t\) is chosen in (78). The two possibilities studied here are: global clocks and local clocks. If a global clock is used, then \(\alpha_t = \beta_t\), whereas if a local clock is used, then \(\alpha_t = \beta_{\nu_{t,i}}\), where

$$
\nu_{t,i} = \sum_{\tau=0}^{t} I_{\{z_{\tau,i} \neq 0\}}.
$$

Note that in the traditional implementation of the \(TD(\lambda)\) algorithm suggested in [31, 38, 16], a global clock is used. Moreover, the algorithm is shown to converge provided

$$
\sum_{t=0}^{\infty} \alpha_t^2 < \infty, \sum_{t=0}^{\infty} \alpha_t = \infty, \text{ a.s.}
\tag{79}
$$

As we shall see below, the theorem statements when local clocks are used involve slightly fewer assumptions than when global clocks are used. Moreover, neither involves probabilistic conditions such as (38) and (39), in contrast to Theorem 9.

Next we present two theorems regarding the convergence of the \(TD(0)\) algorithm. As the hypotheses are slightly different, they are presented separately. But the proofs are quite similar, and can be found in [17].

27

<!-- page: 28 -->

**Theorem 17.** *Consider the \(TD(\lambda)\) algorithm using a local clock to determine the step size. Suppose that the state transition matrix \(A\) is irreducible, and that the deterministic step size sequence \(\{\beta_t\}\) satisfies the Robbins-Monro conditions*

$$
\sum_{t=0}^{\infty} \beta_t = \infty, \sum_{t=0}^{\infty} \beta_t^2 < \infty.
$$

*Then \(\mathbf{v}_t \to \mathbf{v}\) almost surely as \(t \to \infty\).*

**Theorem 18.** *Consider the \(TD(\lambda)\) algorithm using a global clock to determine the step size. Suppose that the state transition matrix \(A\) is irreducible, and that the deterministic step size sequence is nonincreasing (i.e., \(\beta_{t+1} \leq \beta_t\) for all \(t\)), and satisfies the Robbins-Monro conditions as described above. Then \(\mathbf{v}_t \to \mathbf{v}\) almost surely as \(t \to \infty\).*

### 5.3 \(Q\)-Learning

The \(Q\)-learning algorithm proposed in [42] is now recalled for the convenience of the reader.

1. Choose an arbitrary initial guess \(Q_0 : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\) and an initial state \(X_0 \in \mathcal{X}\).

2. At time \(t\), with current state \(X_t = x_i\), choose a current action \(U_t = u_k \in \mathcal{U}\), and let the Markov process run for one time step. Observe the resulting next state \(X_{t+1} = x_j\). Then update the function \(Q_t\) as follows:

$$
\begin{aligned}
Q_{t+1}(x_i, u_k) &= Q_t(x_i, u_k) + \beta_t[R(x_i, u_k) + \gamma V_t(x_j) - Q_t(x_i, u_k)], \\
Q_{t+1}(x_s, w_l) &= Q_t(x_s, w_l), \ \forall (x_s, w_l) \neq (x_i, u_k).
\end{aligned}
\tag{80}
$$

   where

$$
V_t(x_j) = \max_{w_l \in \mathcal{U}} Q_t(x_j, w_l),
\tag{81}
$$

   and \(\{\beta_t\}\) is a deterministic sequence of step sizes.

3. Repeat.

In earlier work such as [36, 16], it is shown that the \(Q\)-learning algorithm converges to the optimal action-value function \(Q^*\) *provided*

$$
\sum_{t=0}^{\infty} \beta_t I_{(X_t, U_t) = (x_i, u_k)} = \infty, \ \forall (x_i, u_k) \in \mathcal{X} \times \mathcal{U},
\tag{82}
$$

$$
\sum_{t=0}^{\infty} \beta_t^2 I_{(X_t, U_t) = (x_i, u_k)} < \infty, \ \forall (x_i, u_k) \in \mathcal{X} \times \mathcal{U}.
\tag{83}
$$

These conditions are stated here as Theorem 11. Similar hypotheses are present in all existing results in asynchronous SA. Note that in the \(Q\)-learning algorithm, there is no guidance on how to choose the next action \(U_t\). Presumably \(U_t\) is chosen so as to ensure that (82) and (83) are satisfied. However, we now demonstrate a way to avoid such conditions, by using Theorem 16. We also introduce batch updating and show that it is possible to use a local clock instead of a global clock.

The batch \(Q\)-learning algorithm introduced here is as follows:

28

<!-- page: 29 -->

1. Choose an arbitrary initial guess \(Q_0 : \mathcal{X} \times \mathcal{U} \to \mathbb{R}\), and \(m\) initial states \(X_0^k \in \mathcal{X}, k \in [m]\), in some fashion (deterministic or random). Note that the \(m\) initial states need not be distinct.

2. At time \(t\), for each action index \(k \in [m]\), with current state \(X_t^k = x_i^k\), choose the current action as \(U_t = u_k \in \mathcal{U}\), and let the Markov process run for one time step. Observe the resulting next state \(X_{t+1}^k = x_j^k\). Then update function \(Q_t\) as follows, once for each \(k \in [m]\):

$$
Q_{t+1}(x_i^k, u_k) = \left\{\begin{array}{ll} Q_t(x_i^k, u_k) + \alpha_{t,i,k}[R(x_i, u_k) + \gamma V_t(x_j^k) - Q_t(x_i^k, u_k)], & \text{if } x_s = x_i^k, \\ Q_t(x_s^k, u_k), & \text{if } x_s^k \neq x_i^k. \end{array}\right.
\tag{84}
$$

   where

$$
V_t(x_j^k) = \max_{w_l \in \mathcal{U}} Q_t(x_j^k, w_l).
\tag{85}
$$

   Here \(\alpha_{t,i,k}\) equals \(\beta_t\) for all \(i, k\) if a global clock is used, and equals

$$
\alpha_{t,i,k} = \sum_{\tau=0}^{t} I_{\{X_t^k = x_i\}}
\tag{86}
$$

   if a local clock is used.

3. Repeat.

**Remark:** Note that \(m\) different simulations are being run in parallel, and that in the \(k\)-th simulation, the next action \(U_t\) is always chosen as \(u_k\). Hence, at each instant of time \(t\), exactly \(m\) components of \(Q(\cdot, \cdot)\) (viewed as an \(n \times m\) matrix) are updated, namely the \((X_t^k, u_k)\) component, for each \(k \in [m]\). In typical MDPs, the size of the action space \(m\) is much smaller than the size of the state space \(n\). For example, in the Blackjack problem discussed in [33, Chapter 4], \(n \sim 2^{100}\) while \(m = 2\)! Therefore the proposed batch \(Q\)-learning algorithm is quite efficient in practice.

Now, by fitting this algorithm into the framework of Theorem 16, we can prove the following general result. The proof can be found in [17].

**Theorem 19.** *Suppose that each matrix \(A^{u_k}\) is irreducible, and that the step size sequence \(\{\beta_t\}\) satisfies the Robbins-Monro conditions (61) with \(\alpha_t\) replaced by \(\beta_t\). With this assumption, we have the following:*

1. *If a local clock is used as in (84), then \(Q_t\) converges almost surely to \(Q^*\).*

2. *If a global clock is used (i.e., \(\alpha_{t,i,k} = \beta_t\) for all \(t, i, k\)), and \(\{\beta_t\}\) is nonincreasing, then \(Q_t\) converges almost surely to \(Q^*\).*

**Remark:** Note that, in the statement of the theorem, it is *not* assumed that every *policy* \(\pi\) leads to an irreducible Markov process – only that every *action* leads to an an irreducible Markov process. In other words, the assumption is that the \(m\) different matrices \(A^{u_k}, k \in [m]\) correspond to irreducible Markov processes. This is a substantial improvement. It is shown in [37] that the following problem is NP-hard: Given an MDP, determine whether *every policy* \(\pi\) results in a Markov process that is a unichain, that is, consists of a single set of recurrent states with the associated state transition matrix being irreducible, plus possibly some transient states. Our problem is slightly different, because we don't permit any transient states. Nevertheless, this problem is also likely to be very difficult. By not requiring any condition of this sort, and also by dispensing with conditions analogous to (82) and (83), the above theorem statement is more useful.

29

<!-- page: 30 -->

## 6 Conclusions and Problems for Future Research

In this brief survey, we have attempted to sketch some of the highlights of Reinforcement Learning. Our viewpoint, which is quite mainstream, is to view RL as solving Markov Decision Problems (MDPs) when the underlying dynamics are unknown. We have used the paradigm of Stochastic Approximation (SA) as a unifying approach. We have presented convergence theorems for the standard approach, which might be thought of as "synchronous" SA, as well as variants such as Asynchronous SA (ASA) and Batch Asynchronous SA (BASA). Many of these results are due to the author and his collaborators.

In this survey, due to length limitations, we have *not* discussed actor-critic algorithms. These can be viewed as applications of the policy gradient theorem [32, 26] coupled with stochastic approximation applied to two-time scale (i.e., singularly perturbed) systems [8, 24]. Some other relevant references are [21, 20, 19]. Also, the rapidly emerging field of Finite-Time SA has not been discussed. FTSA can lead to estimates of the rate of convergence of various RL algorithms, whereas conventional SA leads to only asymptotic results. Some recent relevant papers include [11, 12].

## References

[1] Aristotle Arapostathis, Vivek S. Borkar, Emmanuel Fernández-Gaucherand, Mrinal K. Ghosh, and Steven I. Marcus. Discrete-time controlled Markov processes with average cost criterion: A survey. *SIAM Journal of Control and Optimization*, 31(2):282–344, 1993.

[2] M. Benaim. *Dynamics of stochastic approximation algorithms.* Springer Verlag, 1999.

[3] Albert Benveniste, Michel Metivier, and Pierre Priouret. *Adaptive Algorithms and Stochastic Approximation.* Springer-Verlag, 1990.

[4] D. P. Bertsekas and J. N. Tsitsiklis. *Neuro-Dynamic Programming.* Athena Scientific, 1996.

[5] Julius R. Blum. Multivariable stochastic approximation methods. *Annals of Mathematical Statistics*, 25(4):737–744, 1954.

[6] V. S. Borkar. Asynchronous stochastic approximations. *SIAM Journal on Control and Optimization*, 36(3):840–851, 1998.

[7] V. S. Borkar and S. P. Meyn. The O.D.E. method for convergence of stochastic approximation and reinforcement learning. *SIAM Journal on Control and Optimization*, 38:447–469, 2000.

[8] Vivek S. Borkar. Stochastic approximation in two time scales. *Systems & Control Letters*, 29(5):291–294, February 1997.

[9] Vivek S. Borkar. *Stochastic Approximation: A Dynamical Systems Viewpoint.* Cambridge University Press, 2008.

[10] Vivek S. Borkar. *Stochastic Approximation: A Dynamical Systems Viewpoint (Second Edition).* Hindustan Book Agency, 2022.

[11] Zaiwei Chen, Siva Theja Maguluri, Sanjay Shakkottai, and Karthikeyan Shanmugam. Finite-sample analysis of contractive stochastic approximation using smooth convex envelopes. arxiv:2002.00874v4, October 2020.

30

<!-- page: 31 -->

[12] Zaiwei Chen, Siva Theja Maguluri, Sanjay Shakkottai, and Karthikeyan Shanmugam. Finite-sample analysis of off-policy td-learning via generalized bellman operators. arxiv:2106.12729v1, June 2021.

[13] Rick Durrett. *Probability: Theory and Examples (5th Edition).* Cambridge University Press, 2019.

[14] E. G. Gladyshev. On stochastic approximation. *Theory of Probability and Its Applications*, X(2):275–278, 1965.

[15] Wolfgang Hahn. *Stability of Motion.* Springer-Verlag, 1967.

[16] Tommi Jaakkola, Michael I. Jordan, and Satinder P. Singh. Convergence of stochastic iterative dynamic programming algorithms. *Neural Computation*, 6(6):1185–1201, November 1994.

[17] Rajeeva L. Karandikar and M. Vidyasagar. Convergence of batch asynchronous stochastic approximation with applications to reinforcement learning. arxiv:2109.03445v2, July 2022.

[18] Hassan K. Khalil. *Nonlinear Systems (Third Edition).* Prentice Hall, 2002.

[19] V. Konda and J. Tsitsiklis. On actor-critic algorithms. *SIAM Journal on Control and Optimization*, 42(4):1143–1166, 2003.

[20] Vijay R. Konda and John N. Tsitsiklis. Actor-critic algorithms. In *Neural Information Processing Systems (NIPS1999)*, pages 1008–1014, 1999.

[21] Vijaymohan R. Konda and Vivek S. Borkar. Actor-critic learning algorithms for Markov decision processes. *SIAM Journal on Control and Optimization*, 38(1):94–123, 1999.

[22] Harold J. Kushner and Dean S. Clark. *Stochastic Approximation Methods for Constrained and Unconstrained Systems.* Applied Mathematical Sciences. Springer-Verlag, 1978.

[23] Harold J. Kushner and G. George Yin. *Stochastic Approximation and Recursive Algorithms and Applications.* Springer-Verlag, 1997.

[24] Chandrashekar Lakshminarayanan and Shalabh Bhatnagar. A stability criterion for two timescale stochastic approximation schemes. *Automatica*, 79:108–114, 2017.

[25] Lennart Ljung. Strong convergence of a stochastic approximation algorithm. *Annals of Statistics*, 6:680–696, 1978.

[26] Peter Marbach and John N. Tsitsiklis. Simulation-based optimization of markov reward processes. *IEEE Transactions on Automatic Control*, 46(2):191–209, February 2001.

[27] Martin L. Puterman. *Markov Decision Processes: Discrete Stochastic Dynamic Programming.* John Wiley, 2005.

[28] Herbert Robbins and Sutton Monro. A stochastic approximation method. *Annals of Mathematical Statistics*, 22(3):400–407, 1951.

[29] Claude E. Shannon. Programming a computer for playing chess. *Philosophical Magazine, Ser.7*, 41(314), March 1950.

31

<!-- page: 32 -->

[30] Mark W. Spong, Seth R. Hutchinson, and M. Vidyasagar. *Robot Modeling and Control (Second Edition).* John Wiley, 2020.

[31] R. S. Sutton. Learning to predict by the method of temporal differences. *Machine Learning*, 3(1):9–44, 1988.

[32] R. S. Sutton, D. McAllester, S. Singh, and Y.Mansour. Policy gradient methods for reinforcement learning with function approximation. In *Advances in Neural Information Processing Systems 12 (Proceedings of the 1999 conference)*, pages 1057–1063. MIT Press, 2000.

[33] Richard S. Sutton and Andrew G. Barto. *Reinforcement Learning: An Introduction (Second Edition).* MIT Press, 2018.

[34] Csaba Szepesvári. *Algorithms for Reinforcement Learning.* Morgan and Claypool, 2010.

[35] Vladimir B. Tadić. Almost sure convergence of two time-scale stochastic approximation algorithms. In *Proceedings of the American Control Conference*, volume 4, pages 3802–3807, 2004.

[36] John N. Tsitsiklis. Asynchronous stochastic approximation and q-learning. *Machine Learning*, 16:185–202, 1994.

[37] John N. Tsitsiklis. NP-Hardness of checking the unichain condition in average cost MDPs. *Operations Research Letters*, 35:319–323, 2007.

[38] John N. Tsitsiklis and Benjamin Van Roy. An analysis of temporal-difference learning with function approximation. *IEEE Transactions on Automatic Control*, 42(5):674–690, May 1997.

[39] M. Vidyasagar. *Nonlinear Systems Analysis (SIAM Classics Series).* Society for Industrial and Applied Mathematics (SIAM), 2002.

[40] M. Vidyasagar. *Hidden Markov Processes: Theory and Applications to Biology.* Princeton University Press, 2014.

[41] M. Vidyasagar. Convergence of stochastic approximation via martingale and converse Lyapunov methods. arxiv:2205.01303v1, May 2022.

[42] C. J. C. H. Watkins and P. Dayan. Q-learning. *Machine Learning*, 8(3-4):279–292, 1992.

32
