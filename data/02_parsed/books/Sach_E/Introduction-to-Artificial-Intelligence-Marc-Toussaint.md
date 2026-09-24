<!-- page: 1 -->
# Introduction to Artificial Intelligence

Marc Toussaint

February 4, 2019

The majority of slides on search, CSP and logic are adapted from Stuart Russell.

This is a direct concatenation and reformatting of all lecture slides and exercises from the Artificial Intelligence course (winter term 2018/19, U Stuttgart), including indexing to help prepare for exams.

Double-starred** sections and slides are not relevant for the exam.

## Contents
1 Introduction 6

2 Search 13

Motivation & Outline

2.1 Problem Formulation & Examples . . . . . . . . . . . . . . . . . . . . 13

Example: Romania (2:3) Problem Definition: Deterministic, fully observable (2:5)

2.2 Basic Tree Search Algorithms . . . . . . . . . . . . . . . . . . . . . . . 15

Tree search implementation: states vs nodes (2:11) Tree Search: General Algorithm

(2:12) Breadth-first search (BFS) (2:15) Complexity of BFS (2:16) Uniform-cost search

(2:17) Depth-first search (DFS) (2:18) Complexity of DFS (2:19) Iterative deepening

search (2:21) Complexity of Iterative Deepening Search (2:23) Graph search and re-

peated states (2:25)

2.3 A∗

Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

Best-first Search (2:29) A∗

search (2:31) A∗

: Proof 1 of Optimality (2:33) Complexity

of A∗

(2:34) A∗

: Proof 2 of Optimality (2:35) Admissible heuristics (2:37) Memory-

bounded A∗

(2:40)

<!-- page: 2 -->
3 Probabilities 31 Motivation & Outline Probabilities as (subjective) information calculus (3:2) Inference: general meaning (3:5) Frequentist vs Bayesian (3:6) 3.1 Basic definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 Definitions based on sets (3:8) Random variables (3:9) Probability distribution (3:10) Joint distribution (3:11) Marginal (3:11) Conditional distribution (3:11) Bayes’ Theorem (3:13) Multiple RVs, conditional independence (3:14) 3.2 Probability distributions** . . . . . . . . . . . . . . . . . . . . . . . . . 36 Bernoulli and Binomial distributions (3:16) Beta (3:17) Multinomial (3:20) Dirichlet (3:21) Conjugate priors (3:25) 3.3 Distributions over continuous domain** . . . . . . . . . . . . . . . . . 41 Dirac distribution (3:28) Gaussian (3:29) Particle approximation of a distribution (3:33) Utilities and Decision Theory (3:36) Entropy (3:37) Kullback-Leibler divergence (3:38) 3.4 Monte Carlo methods** . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 Monte Carlo methods (3:40) Rejection sampling (3:41) Importance sampling (3:42) Student’s t, Exponential, Laplace, Chi-squared, Gamma distributions (3:44) 4 Bandits, MCTS, & Games 48 Motivation & Outline 4.1 Bandits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 Multi-armed Bandits (4:2) 4.2 Upper Confidence Bounds (UCB) . . . . . . . . . . . . . . . . . . . . . 50 Exploration, Exploitation (4:7) Upper Confidence Bound (UCB1) (4:8) 4.3 Monte Carlo Tree Search . . . . . . . . . . . . . . . . . . . . . . . . . . 52 Monte Carlo Tree Search (MCTS) (4:14) Upper Confidence Tree (UCT) (4:19) MCTS for POMDPs (4:20) 4.4 MCTS applied to POMDPs** . . . . . . . . . . . . . . . . . . . . . . . 55 4.5 Game Playing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57 Minimax (4:29) Alpha-Beta Pruning (4:32) Evaluation functions (4:37) UCT for games (4:38) 4.6 Beyond bandits** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63 Global Optimization (4:43) GP-UCB (4:46) Active Learning (4:50) 4.7 Active Learning** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

<!-- page: 3 -->
5 Dynamic Programming 69 Motivation & Outline 5.1 Markov Decision Process . . . . . . . . . . . . . . . . . . . . . . . . . . 69 Markov Decision Process (5:3) 5.2 Dynamic Programming . . . . . . . . . . . . . . . . . . . . . . . . . . 70 Value Function (5:6) Bellman optimality equation (5:10) Value Iteration (5:12) QFunction (5:13) Q-Iteration (5:14) Proof of convergence of Q-Iteration (5:15) 5.3 Dynamic Programming in Belief Space . . . . . . . . . . . . . . . . . . 76 6 Reinforcement Learning 81 Motivation & Outline 6.1 Learning in MDPs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84 Temporal difference (TD) (6:10) Q-learning (6:10) Proof of convergence of Q-learning (6:12) Eligibility traces (6:15) Model-based RL (6:28) 6.2 Exploration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94 Epsilon-greedy exploration in Q-learning (6:31) R-Max (6:33) Bayesian RL (6:35) Optimistic heuristics (6:36) 6.3 Policy Search, Imitation, & Inverse RL** . . . . . . . . . . . . . . . . . 97 Policy gradients (6:41) Imitation Learning (6:43) Inverse RL (6:46) 7 Other models of interactive domains** 104 7.1 Basic Taxonomy of domain models . . . . . . . . . . . . . . . . . . . . 104 PDDL (7:6) Noisy Deictic Rules (7:9) POMDP (7:11) Dec-POMDP (7:20) Control (7:21) 8 Constraint Satisfaction Problems 113 Motivation & Outline 8.1 Problem Formulation & Examples . . . . . . . . . . . . . . . . . . . . 113 Inference (8:2) Constraint satisfaction problems (CSPs): Definition (8:3) MapColoring Problem (8:4) 8.2 Methods for solving CSPs . . . . . . . . . . . . . . . . . . . . . . . . . 116 Backtracking (8:10) Variable order: Minimum remaining values (8:15) Variable order: Degree heuristic (8:16) Value order: Least constraining value (8:17) Constraint propagation (8:18) Tree-structured CSPs (8:25)

<!-- page: 4 -->
9 Graphical Models 126 Motivation & Outline 9.1 Bayes Nets and Conditional Independence . . . . . . . . . . . . . . . 126 Bayesian Network (9:5) Conditional independence in a Bayes Net (9:8) Inference: general meaning (9:13) 9.2 Inference Methods in Graphical Models . . . . . . . . . . . . . . . . . 133 Inference in graphical models: overview (9:22) Variable elimination (9:23) Factor graph (9:26) Belief propagation (9:32) Message passing (9:32) Loopy belief propagation (9:36) Junction tree algorithm** (9:38) Maximum a-posteriori (MAP) inference (9:42) Conditional random field (9:43) Monte Carlo (9:45) Rejection sampling (9:46) Importance Sampling (9:48) Gibbs Sampling (9:50) 10 Dynamic Models 147 Motivation & Outline Markov Process (10:1) Hidden Markov Model (10:2) Filtering, Smoothing, Prediction (10:3) HMM: Inference (10:4) HMM inference (10:5) Kalman filter (10:8) 11 AI & Machine Learning & Neural Nets 154 Motivation & Outline Neural networks (11:8) 12 Explainable AI 165 13 Propositional Logic 173 Motivation & Outline 13.1 Syntax & Semantics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173 Knowledge base: Definition (13:3) Wumpus World example (13:4) Logic: Definition, Syntax, Semantics (13:7) Propositional logic: Syntax (13:9) Propositional logic: Semantics (13:10) Logical equivalence (13:12) 13.2 Inference Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183 Inference (13:19) Horn Form (13:23) Modus Ponens (13:23) Forward chaining (13:24) Completeness of Forward Chaining (13:27) Backward Chaining (13:28) Conjunctive Normal Form (13:31) Resolution (13:31) Conversion to CNF (13:32) 14 First-Order Logic** 199 Motivation & Outline 14.1 The FOL language . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200 FOL: Syntax (14:4) Universal quantification (14:6) Existential quantification (14:6) 14.2 FOL Inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203 Reduction to propositional inference (14:16) Unification (14:19) Generalized Modus Ponens (14:20) Forward Chaining (14:21) Backward Chaining (14:27) Conversion to CNF (14:33) Resolution (14:35)

<!-- page: 5 -->
15 Relational Probabilistic Modelling and Learning** 216 Motivation & Outline 15.1 STRIPS-like rules to model MDP transitions . . . . . . . . . . . . . . . 216 Markov Decision Process (MDP) (15:2) STRIPS rules (15:3) Planning Domain Definition Language (PDDL) (15:3) Learning probabilistic rules (15:9) Planning with probabilistic rules (15:11) 15.2 Relational Graphical Models . . . . . . . . . . . . . . . . . . . . . . . . 220 Probabilistic Relational Models (PRMs) (15:20) Markov Logic Networks (MLNs) (15:24) The role of uncertainty in AI (15:31) 16 Exercises 228 16.1 Exercise 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228 16.2 Exercise 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230 16.3 Exercise 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232 16.4 Exercise 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234 16.5 Exercise 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236 16.6 Exercise 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239 16.7 Exercise 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241 16.8 Exercise 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243 16.9 Exercise 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244 Index 246 on trees CSP graphical models MDPs sequential decision problems search BFS propositional logic FOL relational graphical models relational MDPs Reinforcement Learning HMMs ML multi-agent MDPs MCTS utilities deterministic learning probabilistic propositional relational sequential decisions games bandits UCB constraint propagation belief propagation msg. passing Active Learning Decision Theory dynamic programming $V(s)$, $Q(s,a)$ fwd/bwd chaining backtracking fwd/bwd msg. passing FOL sequential assignment alpha/beta pruning minimax

![Hinh: fig-5-1]

<!-- page: 6 -->
# 1 Introduction

(some slides based on Stuart Russell’s AI course)

### What is intelligence?

- Maybe it is easier to first ask what systems we actually talk about:

  - Decision making

  - Interacting with an environment

- Then define objectives!

  - Quantify what you consider good or successful

  - Intelligence means to optimize...

1:1

### Intelligence as Optimization?

- A cognitive scientist or psychologist: “Why are you AI people always so obsessed with optimization? Humans are not optimal!”

- That’s a total misunderstanding of what “being optimal” means.

- Optimization principles are a means to describe systems:

  - Feynman’s “unworldliness measure” objective function

  - Everything can be cast optimal – under some objective

  - Optimality principles are just a scientific means of formally describing systems and
their behaviors (esp. in physics, economy, ... and AI)

  - Toussaint, Ritter & Brock: The Optimization Route to Robotics – and Alternatives. Künstliche
Intelligenz, 2015

- Generally, I would roughly distinguish three basic types of problems:

  - Optimization

  - Logical/categorial Inference (CSP, find feasible solutions)

  - Probabilistic Inference

1:2

### What are interesting objectives?

- Learn to control all degrees of freedom of the environment that are controllable

  - DOFs are mechanical/kinematics DOFs, objects, light/temperature, mood of hu-
mans

  - This objective is generic: no preferences, not limits

  - Implies to actively go exploring and finding controllable DOFs

<!-- page: 7 -->
  - Acting to Learning (instead of ’Learning to Act’ for a fixed task)

  - Related notions in other fields: (Bayesian) Experimental Design, Active Learning, cu-
riosity, intrinsic motivation

- At time T, the system will be given a random task (e.g., random goal configuration of DOFs); the objective then is to reach it as quickly as possible

1:3

### More on objectives

![Hinh: fig-7-1]

- The value alignment dilemma

- What are objectives that describe things like “creativity”, “empathy”, etc?

- Coming up with objective functions that imply desired behavior is a core part of AI research

1:4

### Interactive domains

- We assume the agent is in interaction with a domain.

  - The world is in a state st $\in$ S (see below on what that means)

  - The agent senses observations yt $\in$ O

  - The agent decides on an action at $\in$ A

  - The world transitions to a new state st+1

- The observation yt describes all information received by the agent (sensors, also rewards, feedback, etc) if not explicitly stated otherwise (The technical term for this is a POMDP)

1:5

### State

- The notion of state is often used imprecisely

- At any time t, we assume the world is in a state st $\in$ S

- st is a state description of a domain iff future observations yt+ , t+ > t are conditionally independent of all history observations yt- , t- < t given st and future actions at:t+ :

<!-- page: 8 -->
agent $s_{0}s_{1}a_{0}s_{2}a_{1}s_{3}a_{2}a_{3}y_{0}y_{1}y_{2}y_{3}$

- Notes:

  - Intuitively, st describes everything about the world that is “relevant”

  - Worlds do not have additional latent (hidden) variables to the state st

1:6

### Examples

![Hinh: fig-8-1]

- What is a sufficient definition of state of a computer that you interact with?

- What is a sufficient definition of state for a thermostat scenario? (First, assume the ’room’ is an isolated chamber.)

- What is a sufficient definition of state in an autonomous car case? \to  in real worlds, the exact state is practically not representable \to  all models of domains will have to make approximating assumptions (e.g., about independencies)

1:7

### How can agents be formally described?

...or, what formal classes of agents do exist?

- Basic alternative agent models:

  - The agent maps yt 7\to  at
(stimulus-response mapping.. non-optimal)

  - The agent stores all previous observations and maps
f : $y_{0}$:t, $a_{0}$:t-1 7\to  at
f is called agent function. This is the most general model, including the others as
special cases.

  - The agent stores only the recent history and maps
yt-k:t, at-k:t-1 7\to  at (crude, but may be a good heuristic)

<!-- page: 9 -->
  - The agent is some machine with its own internal state nt, e.g., a computer, a finite
state machine, a brain... The agent maps (nt-1, yt) 7\to  nt (internal state update) and
nt 7\to  at

  - The agent maintains a full probability distribution (belief) $bt(st)$ over the state,
maps (bt-1, yt) 7\to  bt (Bayesian belief update), and bt 7\to  at

1:8

### POMDP coupled to a state machine agent

![Hinh: fig-9-1]

agent $s_{0}s_{1}s_{2}r_{1}r_{0}r_{2}a_{2}y_{2}a_{1}y_{1}a_{0}y_{0}$ n0 n1 n2

1:9

### Multi-agent domain models

(The technical term for this is a Decentralized POMDPs) (from Kumar et al., IJCAI 2011)

- This is a special type (simplification) of a general DEC-POMDP

- Generally, this level of description is very general, but NEXP-hard Approximate methods can yield very good results, though

1:10

### Summary – AI is about:

- Systems that interact with the environment

<!-- page: 10 -->
  - We distinguish between ’system’ and ’environment’ (cf. embodiment)

  - We just introduced basic models of interaction

  - A core part of AI research is to develop formal models for interaction

- Systems that aim to manipulate their invironment towards ’desired’ states (optimality)

  - Optimality principles are a standard way to describe desired behaviors

  - We sketched some interesting objectives

  - Coming up with objective functions that imply desired behavior is a core part of AI
research

1:11

### Organisation

1:12

### Vorlesungen der Abteilung MLR

- Bachelor:

  - Grundlagen der Künstlichen Intelligenz (3+1 SWS)

- Master:

  - Vertiefungslinie Intelligente Systeme (gemeinsam mit Andres Bruhn)

  - WS: Maths for Intelligent Systems

  - WS: Introduction to Robotics

  - SS: Machine Learning

  - (SS: Optimization)

  - (Reinforcement Learning), (Advanced Robotics)

  - Practical Course Robotics (SS)

  - (Hauptseminare: Machine Learning (WS), Robotics (SS))

1:13

### Andres Bruhn’s Vorlesungen in der Vertiefungslinie

  - WS: Computer Vision

  - SS: Correspondence Problems in Computer Vision

  - Hauptseminar: Recent Advances in Computer Vision

1:14

Vorraussetzungen für die KI Vorlesung

- Mathematik für Informatiker und Softwaretechniker

- außerdem hilfreich:

  - Algorithmen und Datenstrukturen

  - Theoretische Informatik

<!-- page: 11 -->
1:15

### Vorlesungsmaterial

- Webseite zur Vorlesung: https://ipvs.informatik.uni-stuttgart.de/mlr/marc/teaching/ die Folien und Übungsaufgaben werden dort online gestellt

- Alle Materialien des letzten Jahres sind online – bitte machen Sie sich einen Eindruck

- Hauptliteratur: Stuart Russell & Peter Norvig: Artificial Intelligence – A Modern Approach

  - Many slides are adopted from Stuart

1:16

Prüfung

- Schriftliche Prüfung, 90 Minuten

- Termin zentral organisiert

- keine Hilfsmittel erlaubt

- Anmeldung: Im LSF / beim Prüfungsamt

- Prüfungszulassung:

  - 50% der Punkte der Programmieraufgaben

  - UND 50% der Votieraufgaben

1:17

Übungen

- 8 Übungsgruppen (4 Tutoren)

- 2 Arten von Aufgaben: Coding- und Votier-Übungen

- Coding-Aufgaben: Teams von bis zu 3 Studenten geben die Coding-Aufgaben zusammen ab

- Votier-Aufgaben:

  - Zu Beginn der Übung eintragen, welche Aufgaben bearbeiten wurden/präsentiert
werden können

  - Zufällige Auswahl

- Schein-Kriterium:

  - 50% der Punkte der Programmieraufgaben

  - UND 50% der Votieraufgaben

<!-- page: 12 -->
- Registrierung https://ipvs.informatik.uni-stuttgart.de/mlr/teaching/course-registrat

1:18

<!-- page: 13 -->
# 2 Search

(slides based on Stuart Russell’s AI course)

### Motivation & Outline

Search algorithms are a core tool for decision making, especially when the domain is too complex to use alternatives like Dynamic Programming. With the increase in computational power search methods became a standard method of choice for complex domains, like the game of Go, or certain POMDPs. Recently, they are combined with machine learning methods which learn heuristics or evaluation functions to guide search. Learning about search tree algorithms is an important background for several reasons:

- The concept of decision trees, which represent the space of possible future decisions and state transitions, is generally important for thinking about decision problems.

- In probabilistic domains, tree search algorithms are a special case of MonteCarlo methods to estimate some expectation, typically the so-called Q-function. The respective Monte-Carlo Tree Search algorithms are the state-of-the-art in many domains.

- Tree search is also the background for backtracking in CSPs as well as forward and backward search in logic domains. We will cover the basic tree search methods (breadth, depth, iterative deepening) and eventually $A^*$

### Outline

- Problem formulation & examples

- Basic search algorithms

2:1

## 2.1 Problem Formulation & Examples

2:2

### Example: Romania

On holiday in Romania; currently in Arad. Flight leaves tomorrow from Bucharest Formulate goal:

$$
be in Bucharest, S_{\mathrm{goal}} = {Bucharest}
$$

<!-- page: 14 -->
Formulate problem:

$$
states: various cities, S = {Arad, Timisoara, . . . } actions: drive between cities, A = {edges between states}
$$

Find solution: sequence of cities, e.g., Arad, Sibiu, Fagaras, Bucharest

$$
minimize costs with cost function, (s, a) 7\to c
$$

2:3

### Example: Romania

![Hinh: fig-14-1]

2:4

### Deterministic, fully observable search problem

A deterministic, fully observable search problem is defined by four items:

$$
initial state s_{0} \in S e.g., s_{0} = Arad successor function succ : S \times A \to S e.g., succ(Arad,Arad-Zerind) = Zerind goal states S_{\mathrm{goal}} \subseteq S e.g., s = Bucharest
$$

step cost function cost(s, a, $s_{0}$

$$
), assumed to be \geq 0
$$

e.g., traveled distance, number of actions executed, etc. the path cost is the sum of step costs A solution is a sequence of actions leading from $s_{0}$ to a goal An optimal solution is a solution with minimal path costs

<!-- page: 15 -->
2:5

### Example: The 8-puzzle

![Hinh: fig-15-1]

states??: integer locations of tiles (ignore intermediate positions) actions??: move blank left, right, up, down (ignore unjamming etc.)

$$
goal test??: = goal state (given)
$$

path cost??: 1 per move [Note: optimal solution of n-Puzzle family is NP-hard]

2:6

## 2.2 Basic Tree Search Algorithms

2:7

### Tree search example

2:8

<!-- page: 16 -->
### Tree search example

![Hinh: fig-16-1]

2:9

### Tree search example

2:10

### Implementation: states vs. nodes

- A state is a (representation of) a physical configuration

- A node is a data structure constituting part of a search tree includes parent, children, depth, path cost $g(x)$ (States do not have parents, children, depth, or path cost!)

- The EXPAND function creates new nodes, filling in the various fields and using the SUCCESSORFN of the problem to create the corresponding states.

<!-- page: 17 -->
2:11

### Implementation: general tree search

```
function TREE-SEARCH( problem,fringe) returns a solution, or failure
fringe ← INSERT(MAKE-NODE(INITIAL-STATE[problem]),fringe)
loop do
if fringe is empty then return failure
node ← REMOVE-FRONT(fringe)
if GOAL-TEST(problem, STATE(node)) then return node
fringe ← INSERTALL(EXPAND(node,problem),fringe)
function EXPAND( node,problem) returns a set of nodes
successors ← the empty set
for each action,result in SUCCESSOR-FN(problem, STATE[node]) do
s ← a new NODE
PARENT-NODE[s] ← node; ACTION[s] ← action; STATE[s] ← result
PATH-COST[s] ← PATH-COST[node] + STEP-COST(STATE[node],action,result)
DEPTH[s] ← DEPTH[node] + 1
add s to successors
return successors
```

2:12

### Search strategies

- A strategy is defined by picking the ordering of the fringe

- Strategies are evaluated along the following dimensions: completeness—does it always find a solution if one exists? time complexity—number of nodes generated/expanded space complexity—maximum number of nodes in memory optimality—does it always find a least-cost solution?

- Time and space complexity are measured in terms of b = maximum branching factor of the search tree d = depth of the least-cost solution m = maximum depth of the state space (may be $\infty$)

2:13

### Summary of Search Strategies

- Breadth-first: fringe is a FIFO

- Depth-first: finge is a LIFO

- Iterative deepening search: repeat depth-first for increasing depth limit

- Uniform-cost: sort fringe by g

- $A^*$ : sort by f = g + h

2:14

<!-- page: 18 -->
### Breadth-first search

![Hinh: fig-18-1]

- Pick shallowest unexpanded node

- Implementation: fringe is a FIFO queue, i.e., new successors go at end

2:15

<!-- page: 19 -->
### Properties of breadth-first search

![Hinh: fig-19-1]

Complete?? Yes (if b is finite) Time?? 1 + b + b2 + b3 + . . . + bd + b(bd

$$
- 1) = O(bd+1
$$

), i.e., exp. in d Space?? $O(bd+1 )$ (keeps every node in memory)

$$
Optimal?? Yes, if cost-per-step=1; not optimal otherwise
$$

Space is the big problem; can easily generate nodes at 100MB/sec

$$
so 24hrs = 8640GB.
$$

2:16

### Uniform-cost search

- “Cost-aware BFS”: Pick least-cost unexpanded node

- Implementation: fringe = queue ordered by path cost, lowest first

- Equivalent to breadth-first if step costs all equal Complete?? Yes, if step cost $\geq$ Time?? # of nodes with g $\leq$ cost-of-optimal-solution, $O(bdC* /e )$ where $C^*$ is the cost of the optimal solution Space?? # of nodes with g $\leq$ cost-of-optimal-solution, $O(bdC* /e )$ Optimal?? Yes: nodes expanded in increasing order of $g(n)$

2:17

### Depth-first search

- Pick deepest unexpanded node

- Implementation: fringe = LIFO queue, i.e., put successors at front

<!-- page: 20 -->
![Hinh: fig-20-1]

<!-- page: 21 -->
2:18

### Properties of depth-first search

![Hinh: fig-21-1]

Complete?? No: fails in infinite-depth spaces, spaces with loops

$$
Modify to avoid repeated states along path \Rightarrow complete in finite spaces
$$

Time?? $O(bm )$: terrible if m is much larger than d but if solutions are dense, may be much faster than breadth-first Space?? $O(bm)$, i.e., linear space! Optimal?? No

2:19

### Depth-limited search

- depth-first search with depth limit l, i.e., nodes at depth l have no successors

- Recursive implementation using the stack as LIFO:

<!-- page: 22 -->
```
function DEPTH-LIMITED-SEARCH( problem,limit) returns soln/fail/cutoff
```

RECURSIVE-DLS(MAKE-$NODE(INITIAL-STATE[problem])$,problem,limit)

```
function RECURSIVE-DLS(node,problem,limit) returns soln/fail/cutoff
```

$$
cutoff-occurred? \leftarrow false
$$

if GOAL-$TEST(problem, STATE[node])$ then return node

$$
else if DEPTH[node] = limit then return cutoff
$$

else for each successor in $EXPAND(node,problem)$ do

$$
result \leftarrow RECURSIVE-DLS(successor,problem,limit) if result = cutoff then cutoff-occurred? \leftarrow true else if result 6= failure then return result
$$

if cutoff-occurred? then return cutoff else return failure

2:20

### Iterative deepening search

```
function ITERATIVE-DEEPENING-SEARCH( problem) returns a solution
inputs: problem, a problem
for depth ← 0 to ∞ do
result ← DEPTH-LIMITED-SEARCH( problem,depth)
if result 6= cutoff then return result
```

end

2:21

### Iterative deepening search

<!-- page: 23 -->
2:22

### Properties of iterative deepening search

![Hinh: fig-23-1]

Complete?? Yes

Time?? $(d + 1)b^0 + db^1 + (d - 1)b^2 + \ldots + b^d = O(b^d)$

Space?? $O(b^d)$

Optimal?? Yes, if step cost = 1

Can be modified to explore uniform-cost tree

- Numerical comparison for $b = 10$ and $d = 5$, solution at far left leaf:
  - $N(IDS) = 50 + 400 + 3\,000 + 20\,000 + 100\,000 = 123\,450$
  - $N(BFS) = 10 + 100 + 1\,000 + 10\,000 + 100\,000 + 999\,990 = 1\,111\,100$
- IDS does better because other nodes at depth $d$ are not expanded
- BFS can be modified to apply goal test when a node is generated

2:23

### Summary of algorithms

| Criterion | Breadth-First | Uniform-Cost | Depth-First | Depth-Limited | Iterative Deepening |
| --- | --- | --- | --- | --- | --- |
| Complete? | Yes* | Yes* | No | Yes, if $l \geq d$ | Yes |
| Time | $b^{d+1}$ | $b^{\left\lceil C^*/\epsilon \right\rceil}$ | $b^m$ | $b^l$ | $b^d$ |
| Space | $b^{d+1}$ | $b^{\left\lceil C^*/\epsilon \right\rceil}$ | $b^m$ | $b^l$ | $bd$ |
| Optimal? | Yes* | Yes | No | No | Yes* |

2:24
<!-- page: 24 -->
### Loops: Repeated states

![Hinh: fig-24-1]

- Failure to detect repeated states can turn a linear problem into an exponential one!

2:25

### Graph search

```
function GRAPH-SEARCH( problem,fringe) returns a solution, or failure
closed ← an empty set
fringe ← INSERT(MAKE-NODE(INITIAL-STATE[problem]),fringe)
loop do
if fringe is empty then return failure
node ← REMOVE-FRONT(fringe)
if GOAL-TEST(problem, STATE[node]) then return node
if STATE[node] is not in closed then
add STATE[node] to closed
fringe ← INSERTALL(EXPAND(node,problem),fringe)
```

end But: storing all visited nodes leads again to exponential space complexity (as for BFS)

2:26

### Summary

- In BFS (or uniform-cost search), the fringe propagates layer-wise, containing nodes of similar distance-from-start (cost-so-far), leading to optimal paths but exponential space complexity $O(bd+1 )$

- In DFS, the fringe is like a deep light beam sweeping over the tree, with space complexity $O(bm)$. Iteratively deepening it also leads to optimal paths.

- Graph search can be exponentially more efficient than tree search, but storing the visited nodes leads to exponential space complexity as BFS.

2:27

## 2.3 A∗

Search

2:28

<!-- page: 25 -->
### Best-first search

- Idea: use an arbitrary priority function $f(n)$ for each node

  - actually $f(n)$ is neg-priority: nodes with lower $f(n)$ have higher priority

- $f(n)$ should reflect which nodes could be on an optimal path

  - could is optimistic – the lower $f(n)$ the more optimistic you are that n is on an
optimal path
$\Rightarrow$ Pick the node with highest priority

- Implementation: fringe is a queue sorted with decreasing priority (increasing f-value)

- Special cases:

  - uniform-cost search (f = g)

  - greedy search (f = h)

  - $A^*$
search (f = g + h)

2:29

### Uniform-Cost Search as special case

- Define $g(n)$ = cost-so-far to reach n

- Then Uniform-Cost Search is Prioritized Search with f = g

2:30

$$
A*
$$

search

- Idea: combine information from the past and the future

  - neg-priority = cost-so-far + estimated cost-to-go

- The evaluation function is $f(n)$ = $g(n)$ + $h(n)$, with

  - $g(n)$ = cost-so-far to reach n

  - $h(n)$ = estimated cost-to-go from n

  - $f(n)$ = estimated total cost of path through n to goal

- $A^*$ search uses an admissible (=optimistic) heuristic

  - i.e., $h(n)\leq h^*$
(n) where $h^*$
(n) is the true cost-to-go from n.

  - (Also require $h(n)\geq$ 0, so $h(G)$ = 0 for any goal G.)

- E.g., $hSLD(n)$ never overestimates the actual road distance

- Theorem: $A^*$ search is optimal (=finds the optimal path)

2:31

$$
A*
$$

search example

<!-- page: 26 -->
![Hinh: fig-26-1]

2:32

<!-- page: 27 -->
$$
Proof of optimality of A*
$$

- Suppose some suboptimal goal G2 has been generated and is in the fringe (but has not yet been selected to be tested for goal condition!). We want to proof: Any node on a shortest path to an optimal goal G will be expanded before G2.

- Let n be an unexpanded node on a shortest path to G. $f(G2)$ = $g(G2)$ since $h(G2)$ = 0 > $g(G)$ since G2 is suboptimal $\geq f(n)$ since h is admissible

- Since $f(n)$ < $f(G2)$, $A^*$ will expand n before G2. This is true for any n on the shortest path. In particular, at some time G is added to the fringe, and since $f(G)$ = $g(G)$ < $f(G2)$ = $g(G2)$ it will select G before G2 for goal testing.

2:33

$$
Properties of A* Complete?? Yes, unless there are infinitely many nodes with f \leq f(G)
$$

Time?? Exponential in [relative error in h × length of soln.] Space?? Exponential. Keeps all nodes in memory Optimal?? Yes

$$
A* expands all nodes with f(n) < C* A* expands some nodes with f(n) = C* A* expands no nodes with f(n) > C*
$$

2:34

$$
Optimality of A*
$$

(more useful)

- Lemma: $A^*$ expands nodes in order of increasing f value∗ Gradually adds “f-contours” of nodes (cf. breadth-first adds layers) Contour i has all nodes with f = fi, where fi < fi+1

![Hinh: fig-27-1]

<!-- page: 28 -->
2:35

### Proof of lemma: Consistency

![Hinh: fig-28-1]

- A heuristic is consistent if $h(n)\leq c(n, a, n0 )$ + $h(n0 )$

- If h is consistent, we have $f(n0 )$ = $g(n0 )$ + $h(n0 )$ = $g(n)$ + $c(n, a, n0 )$ + $h(n0 )\geq g(n)$ + $h(n)$ = $f(n)$ I.e., $f(n)$ is nondecreasing along any path.

2:36

### Admissible heuristics

E.g., for the 8-puzzle:

$$
h1(n) = number of misplaced tiles h2(n) = total Manhattan distance
$$

(i.e., no. of squares from desired location of each tile)

<!-- page: 29 -->
$$
h1(S) =?? 6 h2(S) =?? 4+0+3+3+1+0+2+1 = 14
$$

2:37

### Dominance

![Hinh: fig-29-1]

$$
If h2(n) \geq h1(n) for all n (both admissible)
$$

then h2 dominates h1 and is better for search Typical search costs:

$$
d = 14 IDS = 3,473,941 nodes A* (h1) = 539 nodes A* (h2) = 113 nodes d = 24 IDS \approx 54,000,000,000 nodes A* (h1) = 39,135 nodes A* (h2) = 1,641 nodes
$$

Given any admissible heuristics ha, hb,

$$
h(n) = max(ha(n), hb(n))
$$

is also admissible and dominates ha, hb

2:38

### Relaxed problems

- Admissible heuristics can be derived from the exact solution cost of a relaxed version of the problem

- If the rules of the 8-puzzle are relaxed so that a tile can move anywhere, then $h1(n)$ gives the shortest solution

- If the rules are relaxed so that a tile can move to any adjacent square, then $h2(n)$ gives the shortest solution

- Key point: the optimal solution cost of a relaxed problem is no greater than the optimal solution cost of the real problem

2:39

$$
Memory-bounded A* \bullet  As with BFS, A*
$$

has exponential space complexity

<!-- page: 30 -->
- Iterative-deepening $A^*$ , works for integer path costs, but problematic for realvalued

- (Simplified) Memory-bounded $A^*$ (SM$A^*$ ):

  - Expand as usual until a memory bound is reach

  - Then, whenever adding a node, remove the worst node n0
from the tree

  - worst means: the n0
with highest f(n0
)

  - To not loose information, backup the measured step-cost cost(ñ, a, n0
) to improve
the heuristic $h(ñ)$ of its parent
SM$A^*$
is complete and optimal if the depth of the optimal path is within the
memory bound

2:40

### Summary

- Combine information from the past and the future

- A heuristic function $h(n)$ represents information about the future it estimates cost-to-go optimistically

- Good heuristics can dramatically reduce search cost

- $A^*$ search expands lowest f = g + h

  - neg-priority = cost-so-far + estimated cost-to-go

  - complete and optimal

  - also optimally efficient (up to tie-breaks, for forward search)

- Admissible heuristics can be derived from exact solution of relaxed problems

- Memory-bounded startegies exist

2:41

### Outlook

- Tree search with partial observations

  - we discuss this in a fully probabilistic setting later

- Tree search for games

  - minimax extension to tree search

  - probabilistic Monte-Carlo tree search methods for games

2:42

<!-- page: 31 -->
# 3 Probabilities

### Motivation & Outline

AI systems need to reason about what they know, or not know. Uncertainty may have so many sources: The environment might be stochatic, making it impossible to predict the future deterministically. The environment can only partially be observed, leading to uncertainty about the rest. This holds especially when the environment includes other agents or humans, the intensions of which are not directly observable. A system can only collect limited data, necessarily leading to uncertain models. We need a calculus for all this. And probabilities are the right calculus. Actually, the trivial Bayes’ rule in principle tells us how we have to process information: whenever we had prior uncertainty about something, then get new information, Bayes’ rules tells us how to update our knowledge. This concept is so general that it includes large parts of Machine Learning, (Bayesian) Reinforcement Learning, Bayesian filtering (Kalman & particle filters), etc. The caveat of course is to compute or approximate such Bayesian information processing in practise. In this lecture we introduce some basics of probabilities, many of which you’ve learned before in other courses. So the aim is also to recap and introduce the notation. What we introduce is essential for the later lectures on bandits, reinforcement learning, graphical models, and relational probabilistic models.

### Outline

- This set of slides is only for your reference. Only what is *-ed below and was explicitly discussed in the lecture is relevant for the exam.

- Basic definitions*

  - Random variables*

  - joint, conditional, marginal distribution*

  - Bayes’ theorem*

- Probability distributions:

  - Binomial & Beta

  - Multinomial & Dirichlet

  - Conjugate priors

  - Gauss & Wichart

  - Student-t; Dirak; etc

  - Dirak & Particles

- Utilities, decision theory, entropy, KLD

- Monte Carlo*, Rejection & Importance Sampling

3:1

### Probability Theory

<!-- page: 32 -->
- Why do we need probabilities?

  - Obvious: to express inherent (objective) stochasticity of the world

- But beyond this: (also in a “deterministic world”):

  - lack of knowledge!

  - hidden (latent) variables

  - expressing uncertainty

  - expressing information (and lack of information)

  - Subjective Probability

- Probability Theory: an information calculus

3:2

### Objective Probability

![Hinh: fig-32-1]

The double slit experiment:

### x

P θ

<!-- page: 33 -->
3:3

### Thomas Bayes (1702-–1761)

![Hinh: fig-33-1]

“Essay Towards Solving a Problem in the Doctrine of Chances”

- Addresses problem of inverse probabilities: Knowing the conditional probability of B given A, what is the conditional probability of A given B?

- Example: 40% Bavarians speak dialect, only 1% of non-Bavarians speak (Bav.) dialect Given a random German that speaks non-dialect, is he Bavarian? (15% of Germans are Bavarian)

3:4

### Inference

- “Inference” = Given some pieces of information (prior, observed variabes) what is the implication (the implied information, the posterior) on a non-observed variable

- Decision-Making and Learning as Inference:

  - given pieces of information: about the world/game, collected data, assumed
model class, prior over model parameters

  - make decisions about actions, classifier, model parameters, etc

3:5

### Probability: Frequentist and Bayesian

- Frequentist probabilities are defined in the limit of an infinite number of trials Example: “The probability of a particular coin landing heads up is 0.43”

<!-- page: 34 -->
- Bayesian (subjective) probabilities quantify degrees of belief Example: “The probability of it raining tomorrow is 0.3”

  - Not possible to repeat “tomorrow”

3:6

## 3.1 Basic definitions

![Hinh: fig-34-1]

3:7

### Probabilities & Sets

- Sample Space/domain Ω, e.g. Ω = {1, 2, 3, 4, 5, 6}

- Probability P : A ⊂ Ω 7\to  [0, 1] e.g., $P({1})$ = 1 6 , $P({4})$ = 1 6 , $P({2, 5})$ = 1 3 ,

- Axioms: \forall A, B ⊆ Ω

  - Nonnegativity $P(A)\geq$ 0

  - Additivity $P(A \cup B)$ = $P(A)$ + $P(B)$ if A ∩ B = { }

  - Normalization $P(\Omega)$ = 1

- Implications 0 $\leq P(A)\leq$ 1 $P(\emptyset)$ = 0 A ⊆ B $\Rightarrow P(A)\leq P(B)P(A \cup B)$ = $P(A)$ + $P(B)$ - $P(A \cap B)P(\Omega \ A)$ = 1 - $P(A)$

3:8

### Probabilities & Random Variables

- For a random variable X with discrete domain $dom(X)$ = Ω we write: \forall x$\in$Ω : 0 $\leq P(X =x)\leq$ 1 P x$\in$Ω $P(X =x)$ = 1 Example: A dice can take values Ω = {1, .., 6}. X is the random variable of a dice throw. $P(X =1)\in$ [0, 1] is the probability that X takes value 1.

- A bit more formally: a random variable is a map from a measureable space to the domain (sample space) and thereby introduces a probability measure on the domain

3:9

<!-- page: 35 -->
### Probabilty Distributions

![Hinh: fig-35-1]

- $P(X =1)\in$ R denotes a specific probability $P(X)$ denotes the probability distribution (function over Ω) Example: A dice can take values Ω = {1, 2, 3, 4, 5, 6}. By $P(X)$ we discribe the full distribution over possible values {1, .., 6}. These are 6 numbers that sum to one, usually stored in a table, e.g.: [1 6 , 1 6 , 1 6 , 1 6 , 1 6 , 1 6 ]

- In implementations we typically represent distributions over discrete random variables as tables (arrays) of numbers

- Notation for summing over a RV: In equation we often need to sum over RVs. We then write P X $P(X)$ · · · as shorthand for the explicit notation P x$\in```text
dom(X)P(X =x)$ · · ·

3:10

### Joint distributions

Assume we have two random variables X and Y

- Definitions: Joint: $P(X, Y )$ Marginal: $P(X)$ = P Y $P(X, Y )$ Conditional: $P(X|Y )$ = P (X,Y ) P (Y ) The conditional is normalized: \forall Y : P X $P(X|Y )$ = 1

- X is independent of Y iff: $P(X|Y )$ = $P(X)$ (table thinking: all columns of $P(X|Y )$ are equal)

3:11

### Joint distributions

joint: $P(X, Y )$
```
marginal: P(X) =
```text
P Y $P(X, Y )$
```
conditional: P(X|Y ) = P (X,Y )
$$

P (Y )

- Implications of these definitions:

<!-- page: 36 -->
$$
Product rule: P(X, Y ) = P(X|Y ) P(Y ) = P(Y |X) P(X) Bayes’ Theorem: P(X|Y ) = P (Y |X) P (X)
```text
P (Y )

3:12

### Bayes’ Theorem
```
P(X|Y ) =
```text
$P(Y |X)P(X)P(Y )$
```
posterior =
```text
likelihood · prior normalization

3:13

### Multiple RVs:

- Analogously for n random variables $X1$:n (stored as a rank n tensor) Joint: $P(X_{1:n})$ Marginal: $P(X1)$ = P $X2$:n $P(X_{1:n})$, Conditional: $P(X1|X2:n)$ = P ($X1$:n) P ($X2$:n)

- X is conditionally independent of Y given Z iff: $P(X|Y, Z)$ = $P(X|Z)$

- Product rule and Bayes’ Theorem: $P(X_{1:n})$ = Qn i=1 $P(Xi|Xi+1:n)P(X1|X2:n)$ = P ($X2$|$X1$,$X3$:n) P ($X1$|$X3$:n) P ($X2$|$X3$:n) $P(X, Z, Y )$ = $P(X|Y, Z)P(Y |Z)P(Z)P(X|Y, Z)$ = P (Y |X,Z) P (X|Z) P (Y |Z) $P(X, Y |Z)$ = P (X,Z|Y ) P (Y ) P (Z)

3:14

## 3.2 Probability distributions**

recommended reference: Bishop.: Pattern Recognition and Machine Learning

3:15

### Bernoulli & Binomial

<!-- page: 37 -->
- We have a binary random variable $x \in \{0, 1\}$ (i.e. $\mathrm{dom}(x)=\{0,1\}$). The Bernoulli distribution is parameterized by a single scalar $\mu$.
```
P(x=1\mid\mu)=\mu,\qquad P(x=0\mid\mu)=1-\mu
$$

$$
\mathrm{Bern}(x\mid\mu)=\mu^x(1-\mu)^{1-x}
```text
- We have a data set of random variables $D=\{x_1,\ldots,x_n\}$, each $x_i\in\{0,1\}$. If each $x_i\sim\mathrm{Bern}(x_i\mid\mu)$ we have
```
P(D\mid\mu)=\prod_{i=1}^{n}\mathrm{Bern}(x_i\mid\mu)=\prod_{i=1}^{n}\mu^{x_i}(1-\mu)^{1-x_i}
$$

$$
\arg\max_{\mu}\log P(D\mid\mu)=\arg\max_{\mu}\sum_{i=1}^{n}\left[x_i\log\mu+(1-x_i)\log(1-\mu)\right]=\frac{1}{n}\sum_{i=1}^{n}x_i
```text
- The Binomial distribution is the distribution over the count $m=\sum_{i=1}^{n}x_i$
```
\mathrm{Bin}(m\mid n,\mu)=\binom{n}{m}\mu^m(1-\mu)^{n-m},\qquad \binom{n}{m}=\frac{n!}{(n-m)!m!}
```text
3:16

### Beta

How to express uncertainty over a Bernoulli parameter $\mu$

- The Beta distribution is over the interval $[0,1]$, typically the parameter $\mu$ of a Bernoulli:
```
\mathrm{Beta}(\mu\mid a,b)=\frac{1}{B(a,b)}\mu^{a-1}(1-\mu)^{b-1}
```text
with mean $\langle\mu\rangle=\frac{a}{a+b}$ and mode $\mu^*=\frac{a-1}{a+b-2}$ for $a,b>1$.

- The crucial point is:

  - Assume we are in a world with a “Bernoulli source” (e.g., binary bandit), but don’t know its parameter $\mu$.
  - Assume we have a prior distribution $P(\mu)=\mathrm{Beta}(\mu\mid a,b)$.
  - Assume we collected some data $D=\{x_1,\ldots,x_n\}$, $x_i\in\{0,1\}$, with counts $a_D=\sum_i x_i$ of $[x_i=1]$ and $b_D=\sum_i(1-x_i)$ of $[x_i=0]$.
  - The posterior is
```
P(\mu\mid D)=\frac{P(D\mid\mu)}{P(D)}P(\mu)\propto \mathrm{Bin}(D\mid\mu)\,\mathrm{Beta}(\mu\mid a,b)
$$

$$
\propto \mu^{a_D}(1-\mu)^{b_D}\mu^{a-1}(1-\mu)^{b-1}=\mu^{a-1+a_D}(1-\mu)^{b-1+b_D}
$$

$$
=\mathrm{Beta}(\mu\mid a+a_D,b+b_D)
```text
3:17
<!-- page: 38 -->
### Beta

![Hinh: fig-38-1]

![Hinh: fig-38-2]

The prior is $Beta(\mu | a, b)$, the posterior is $Beta(\mu | a + aD, b + bD)$

- Conclusions:

  - The semantics of a and b are counts of [xi =1] and [xi =0], respectively

  - The Beta distribution is conjugate to the Bernoulli (explained later)

  - With the Beta distribution we can represent beliefs (state of knowledge) about un-
certain \mu $\in$ [0, 1] and know how to update this belief given data

3:18

### Beta

from Bishop

3:19

### Multinomial

- We have an integer random variable x $\in$ {1, .., K} The probability of a single x can be parameterized by \mu = (\mu1, .., \muK): $P(x=k | \mu)$ = \mu_k with the constraint PK k=1 \mu_k = 1 (probabilities need to be normalized)

- We have a data set of random variables D = {$x_{1}$, .., xn}, each xi $\in$ {1, .., K}. If each xi ∼ $P(x_i | \mu)$ we have $P(D | \mu)$ = Qn i=1 \muxi = Qn i=1 QK k=1 \mu [xi=k] k = QK k=1 \mumk k

<!-- page: 39 -->
```
where mk =
$$

Pn

$$
i=1[x_i =k] is the count of [x_i =k]. The ML estimator is
$$

argmax \mu

$$
log P(D | \mu) =
```text
1 n (m1, .., mK)

- The Multinomial distribution is this distribution over the counts mk $Mult(m1, .., mK | n, \mu)$ \propto  QK k=1 \mumk k

3:20

### Dirichlet

How to express uncertainty over a Multinomial parameter \mu

- The Dirichlet distribution is over the K-simplex, that is, over \mu1, .., \muK $\in$ [0, 1] subject to the constraint PK k=1 \mu_k = 1: $Dir(\mu | \alpha)$ \propto  QK k=1 \muαk-1 k It is parameterized by α = (α1, .., αK), has mean h\mu_ii = αi P j αj and mode \mu∗ i = αi-1 P j αj -K for ai > 1.

- The crucial point is:

  - Assume we are in a world with a “Multinomial source” (e.g., an integer bandit), but
don’t know its parameter \mu

  - Assume we have a prior distribution $P(\mu)$ = $Dir(\mu | \alpha)$

  - Assume we collected some data D = {$x_{1}$, .., xn}, xi $\in$ {1, .., K}, with counts mk =
P
i[xi =k]

  - The posterior is
$P(\mu | D)$ =
$P(D | \mu)$
$P(D)$
$P(\mu)$ \propto  $Mult(D | \mu)Dir(\mu | a, b)$
\propto 
QK
k=1 \mu
mk
k
QK
k=1 \mu
αk-1
k =
QK
k=1 \mu
αk-1+mk
k
= $Dir(\mu | \alpha + m)$

3:21

### Dirichlet

The prior is $Dir(\mu | \alpha)$, the posterior is $Dir(\mu | \alpha + m)$

- Conclusions:

  - The semantics of α is the counts of [xi =k]

  - The Dirichlet distribution is conjugate to the Multinomial

<!-- page: 40 -->
  - With the Dirichlet distribution we can represent beliefs (state of knowledge) about
uncertain \mu of an integer random variable and know how to update this belief given
data

3:22

### Dirichlet

![Hinh: fig-40-1]
```
Illustrations for \alpha = (0.1, 0.1, 0.1), \alpha = (1, 1, 1) and \alpha = (10, 10, 10):
```text
from Bishop

3:23

### Motivation for Beta & Dirichlet distributions

- Bandits:

  - If we have binary [integer] bandits, the Beta [Dirichlet] distribution is a way to
represent and update beliefs

  - The belief space becomes discrete: The parameter α of the prior is continuous, but
the posterior updates live on a discrete “grid” (adding counts to α)

  - We can in principle do belief planning using this

- Reinforcement Learning:

  - Assume we know that the world is a finite-state MDP, but do not know its transition
probability P($s_{0}$
| s, a). For each (s, a), P($s_{0}$
| s, a) is a distribution over the integer
$s_{0}$

  - Having a separate Dirichlet distribution for each (s, a) is a way to represent our
belief about the world, that is, our belief about P($s_{0}$
| s, a)

  - We can in principle do belief planning using this \to  Bayesian Reinforcement Learning

- Dirichlet distributions are also used to model texts (word distributions in text), images, or mixture distributions in general

3:24

### Conjugate priors

- Assume you have data D = {$x_{1}$, .., xn} with likelihood $P(D | \theta)$ that depends on an uncertain parameter θ

<!-- page: 41 -->
Assume you have a prior $P(\theta)$

- The prior $P(\theta)$ is conjugate to the likelihood $P(D | \theta)$ iff the posterior $P(\theta | D)$ \propto  $P(D | \theta)P(\theta)$ is in the same distribution class as the prior $P(\theta)$

- Having a conjugate prior is very convenient, because then you know how to update the belief given data

3:25

### Conjugate priors

likelihood conjugate Binomial $Bin(D | \mu)$ Beta $Beta(\mu | a, b)$ Multinomial $Mult(D | \mu)$ Dirichlet $Dir(\mu | \alpha)$ Gauss $N(x | \mu, \Sigma)$ Gauss $N(\mu | \mu0, A)$ 1D Gauss $N(x | \mu, \lambda-1 )$ Gamma $Gam(\lambda | a, b)$ nD Gauss $N(x | \mu, Λ-1 )$ Wishart $Wish(Λ | W, \nu)$ nD Gauss $N(x | \mu, Λ-1 )$ Gauss-Wishart N(\mu | \mu0, (βΛ)-1 ) $Wish(Λ | W, \nu)$

3:26

## 3.3 Distributions over continuous domain**

3:27

### Distributions over continuous domain

- Let x be a continuous RV. The probability density function (pdf) $p(x)\in$ [0, $\infty$) defines the probability $P(a \leq x \leq b)$ = Z b a $p(x)$ dx $\in$ [0, 1] The (cumulative) probability distribution $F(y)$ = $P(x \leq y)$ = R y -$\infty$ dx $p(x)\in$ [0, 1] is the cumulative integral with limy\to $\inftyF(y)$ = 1 (In discrete domain: probability distribution and probability mass function $P(x)\in$ [0, 1] are used synonymously.)

- Two basic examples: Gaussian: $N(x | \mu, \Sigma)$ = 1 | 2πΣ | 1/2 e- 1 2 (x-\mu)> Σ-1 (x-\mu)

<!-- page: 42 -->
```
Dirac or \delta (“point particle”) \delta(x) = 0 except at x = 0,
$$

R

$$
\delta(x) dx = 1 \delta(x) = \partial \partial x H(x) where H(x) = [x \geq 0] = Heaviside step function
```text
3:28

### Gaussian distribution

![Hinh: fig-42-1]

- 1-dim: $N(x | \mu, \sigma2 )$ = 1 | 2πσ2 | 1/2 e- 1 2 (x-\mu)2 /σ2 $N(x|\mu, \sigma2 )$ x 2σ \mu

- n-dim Gaussian in normal form: $N(x | \mu, \Sigma)$ = 1 | 2πΣ | 1/2 exp{- 1 2 (x - \mu)> Σ-1 (x - \mu)} with mean \mu and covariance matrix Σ. In canonical form: N[x | a, A] = exp{-1 2 a> A-1 a} | 2πA-1 | 1/2 exp{- 1 2 x> A x + x> a} (1) with precision matrix A = Σ-1 and coefficient a = Σ-1 \mu (and mean \mu = A-1 a). Note: | 2πΣ | = $det(2\pi\Sigma)$ = (2π)n $det(\Sigma)$

- Gaussian identities: see http://ipvs.informatik.uni-stuttgart.de/mlr/marc/ notes/gaussians.pdf

3:29

### Gaussian identities
```
Symmetry: N(x | a, A) = N(a | x, A) = N(x - a | 0, A)
$$

Product:

$$
N(x | a, A) N(x | b, B) = N[x | A-1
```text
a + B-1 b, A-1 + B-1 ] $N(a | b, A + B)$
```
N[x | a, A] N[x | b, B] = N[x | a + b, A + B] N(A-1
$$

a | B-1 b, A-1 + B-1 ) “Propagation”: R y

$$
N(x | a + Fy, A) N(y | b, B) dy = N(x | a + Fb, A + FBF>
$$

) Transformation:

$$
N(Fx + f | a, A) = 1
```text
| F | N(x | F-1 (a - f), F-1 AF-> ) Marginal & conditional: N

x y a b , A C C> B
```
= N(x | a, A) \cdot N(y | b + C>
```text
A-1 (x - a), B - C> A-1 C) More Gaussian identities: see http://ipvs.informatik.uni-stuttgart.de/mlr/marc/ notes/gaussians.pdf

3:30

<!-- page: 43 -->
### Gaussian prior and posterior

- Assume we have data D = {$x_{1}$, .., xn}, each xi $\in$ Rn , with likelihood $P(D | \mu, \Sigma)$ = Q i $N(x_i | \mu, \Sigma)$ argmax \mu $P(D | \mu, \Sigma)$ = 1 n n X i=1 xi argmax Σ $P(D | \mu, \Sigma)$ = 1 n n X i=1 (xi - \mu)(xi - \mu)>

- Assume we are initially uncertain about \mu (but know Σ). We can express this uncertainty using again a Gaussian N[\mu | a, A]. Given data we have $P(\mu | D)$ \propto  $P(D | \mu, \Sigma)P(\mu)$ = Q i $N(x_i | \mu, \Sigma)$ N[\mu | a, A] = Q i N[\mu | Σ-1 xi, Σ-1 ] N[\mu | a, A] \propto  N[\mu | Σ-1 P i xi, nΣ-1 + A] Note: in the limit A \to  0 (uninformative prior) this becomes $P(\mu | D)$ = $N(\mu | 1 n X i x_i, 1 n \Sigma)$ which is consistent with the Maximum Likelihood estimator

3:31

### Motivation for Gaussian distributions

- Gaussian Bandits

- Control theory, Stochastic Optimal Control

- State estimation, sensor processing, Gaussian filtering (Kalman filtering)

- Machine Learning

- etc

3:32

### Particle Approximation of a Distribution

- We approximate a distribution $p(x)$ over a continuous domain Rn

- A particle distribution $q(x)$ is a weighed set S = {(xi , wi )}N i=1 of N particles

  - each particle has a “location” xi
$\in$ Rn
and a weight wi
$\in$ R

  - weights are normalized,
P
i wi
= 1
$q(x)$ :=
N
X
i=1
wi
δ(x - xi
)
where δ(x - xi
) is the δ-distribution.

<!-- page: 44 -->
- Given weighted particles, we can estimate for any (smooth) f: hf(x)ip = Z x f(x)p(x)dx ≈ PN i=1 wi $f(x_i )$ See An Introduction to MCMC for Machine Learning www.cs.ubc.ca/˜nando/ papers/mlintro.pdf

3:33

### Particle Approximation of a Distribution

![Hinh: fig-44-1]

![Hinh: fig-44-2]

![Hinh: fig-44-3]

![Hinh: fig-44-4]

Histogram of a particle representation:

3:34

### Motivation for particle distributions

- Numeric representation of “difficult” distributions

  - Very general and versatile

  - But often needs many samples

- Distributions over games (action sequences), sample based planning, MCTS

- State estimation, particle filters

- etc

3:35

### Utilities & Decision Theory

<!-- page: 45 -->
- Given a space of events Ω (e.g., outcomes of a trial, a game, etc) the utility is a function U : Ω \to  R

- The utility represents preferences as a single scalar – which is not always obvious (cf. multi-objective optimization)

- Decision Theory making decisions (that determine $p(x)$) that maximize expected utility E{U}p = Z x $U(x)p(x)$

- Concave utility functions imply risk aversion (and convex, risk-taking)

3:36

### Entropy

- The neg-log (- log $p(x)$) of a distribution reflects something like “error”:

  - neg-log of a Guassian \leftrightarrow  squared error

  - neg-log likelihood \leftrightarrow  prediction error

- The (- log $p(x)$) is the “optimal” coding length you should assign to a symbol x. This will minimize the expected length of an encoding $H(p)$ = Z x $p(x)$[- log $p(x)$]

- The entropy $H(p)$ = $Ep(x)${- log $p(x)$} of a distribution p is a measure of uncertainty, or lack-of-information, we have about x

3:37

### Kullback-Leibler divergence

- Assume you use a “wrong” distribution $q(x)$ to decide on the coding length of symbols drawn from $p(x)$. The expected length of a encoding is Z x $p(x)$[- log $q(x)$] $\geqH(p)$

- The difference D p q
```
=
```text
Z x $p(x)$ log $p(x)q(x)$
```
\geq 0
```text
is called Kullback-Leibler divergence Proof of inequality, using the Jenson inequality: - Z x $p(x)$ log $q(x)p(x)$
```
\geq - log
```text
Z x $p(x)q(x)p(x)$
```
= 0
```text
3:38

<!-- page: 46 -->
## 3.4 Monte Carlo methods**

3:39

### Monte Carlo methods

- Generally, a Monte Carlo method is a method to generate a set of (potentially weighted) samples that approximate a distribution $p(x)$. In the unweighted case, the samples should be i.i.d. xi ∼ $p(x)$ In the general (also weighted) case, we want particles that allow to estimate expectations of anything that depends on x, e.g. $f(x)$: lim N\to $\infty$ hf(x)iq = lim N\to $\infty$ N X i=1 wi $f(x_i )$ = Z x $f(x)p(x)$ dx = hf(x)ip In this view, Monte Carlo methods approximate an integral.

- Motivation: $p(x)$ itself is too complicated to express analytically or compute hf(x)ip directly

- Example: What is the probability that a solitair would come out successful? (Original story by Stan Ulam.) Instead of trying to analytically compute this, generate many random solitairs and count.

- Naming: The method developed in the 40ies, where computers became faster. Fermi, Ulam and von Neumann initiated the idea. von Neumann called it “Monte Carlo” as a code name.

3:40

### Rejection Sampling

- How can we generate i.i.d. samples xi ∼ $p(x)$?

- Assumptions:

  - We can sample x ∼ $q(x)$ from a simpler distribution $q(x)$ (e.g., uniform), called
proposal distribution

  - We can numerically evaluate $p(x)$ for a specific x (even if we don’t have an analytic
expression of $p(x)$)

  - There exists M such that \forall x : $p(x)\leqMq(x)$ (which implies q has larger or equal
support as p)

- Rejection Sampling:

  - Sample a candiate x ∼ $q(x)$

  - With probability $p(x)$
$Mq(x)$
accept x and add to S; otherwise reject

  - Repeat until |S| = n

- This generates an unweighted sample set S to approximate $p(x)$

3:41

<!-- page: 47 -->
### Importance sampling

- Assumptions:

  - We can sample x ∼ $q(x)$ from a simpler distribution $q(x)$ (e.g., uniform)

  - We can numerically evaluate $p(x)$ for a specific x (even if we don’t have an analytic
expression of $p(x)$)

- Importance Sampling:

  - Sample a candiate x ∼ $q(x)$

  - Add the weighted sample (x, $p(x)$
$q(x)$
) to S

  - Repeat n times

- This generates an weighted sample set S to approximate $p(x)$ The weights wi = $p(x_i)q(x_i)$ are called importance weights

- Crucial for efficiency: a good choice of the proposal $q(x)$

3:42

### Applications

- MCTS estimates the Q-function at branchings in decision trees or games

- Inference in graphical models (models involving many depending random variables)

3:43

### Some more continuous distributions
```
Gaussian N(x | a, A) = 1
$$

| 2πA | 1/2 e- 1 2 (x-a)> A-1 (x-a)

$$
Dirac or \delta \delta(x) = \partial \partial x H(x)
$$

Student’s t

$$
(=Gaussian for \nu \to \infty, otherwise heavy
```text
tails) $p(x; \nu)$ \propto  [1 + $x_{2}$ ν ]- ν+1 2 Exponential (distribution over single event time)
```
p(x; \lambda) = [x \geq 0] \lambda e-\lambdax
$$

Laplace (“double exponential”)

$$
p(x; \mu, b) = 1
$$

2b e- | x-\mu | /b

$$
Chi-squared p(x; k) \propto [x \geq 0] x_k/2-1
$$

e-x/2

$$
Gamma p(x; k, \theta) \propto [x \geq 0] x_k-1
```text
e-x/θ

3:44

<!-- page: 48 -->
# 4 Bandits, MCTS, & Games

### Motivation & Outline

The first lecture was about tree search (a form of sequential decision making), the second about probabilities. If we combine this we get Monte-Carlo Tree Search (MCTS), which is the focus of this lecture. But before discussing MCTS we introduce an important conceptual problem: Multi-armed bandits. This problem setting is THE prototype for so-called explorationexploitation problems. More precisely, for problems where sequential decisions influence both, the state of knowledge of the agent as well as the states/rewards the agent gets. Therefore there is some tradeoff between choosing decisions for the sake of learning (influencing the state of knowledge in a positive way) versus for the sake of rewards—while clearly, learning might also enable you to better collect rewards later. Bandits are a kind of minimalistic problem setting of this kind, and the methods and algorithms developed for Bandits translate to other explorationexploitation kind of problems within Reinforcement Learning, Machine Learning, and optimization. Interestingly, our first application of Bandit ideas and methods is tree search: Performing tree search is also a sequential decision problem, and initially the ’agent’
```
(=tree search algorithm) has a lack of knowledge of where the optimum in the
```text
tree is. This sequential decision problem under uncertain knowledge is also an exploitation-exploration problem. Applying the Bandit methods we get state-of-theart MCTS methods, which nowadays can solve problems like computer Go. We first introduce bandits, the MCTS, and mention MCTS for POMDPs. We then introduce 2-player games and how to apply MCTS in this case. 4.1 Bandits

4:1

### Multi-armed Bandits

<!-- page: 49 -->
- There are n machines

- Each machine i returns a reward y ∼ $P(y; \theta_i)$ The machine’s parameter θi is unknown

- Your goal is to maximize the reward, say, collected over the first T trials

4:2

### Bandits – applications

![Hinh: fig-49-1]

![Hinh: fig-49-2]

- Online advertisement

- Clinical trials, robotic scientist

- Efficient optimization

4:3

### Bandits

- The bandit problem is an archetype for

  - Sequential decision making

  - Decisions that influence knowledge as well as rewards/states

  - Exploration/exploitation

- The same aspects are inherent also in global optimization, active learning & RL

- The Bandit problem formulation is the basis of UCB – which is the core of serveral planning and decision making methods

- Bandit problems are commercially very relevant

4:4

<!-- page: 50 -->
## 4.2 Upper Confidence Bounds (UCB)

4:5

### Bandits: Formal Problem Definition

- Let at $\in$ {1, .., n} be the choice of machine at time t Let yt $\in$ R be the outcome

- A policy or strategy maps all the history to a new choice: π : [($a_{1}$, $y_{1}$), ($a_{2}$, $y_{2}$), ..., (at-1, yt-1)] 7\to  at

- Problem: Find a policy π that maxh PT t=1 yti or maxhyT i or other objectives like discounted infinite horizon maxh P$\infty$ t=1 γt yti

4:6

### Exploration, Exploitation

- “Two effects” of choosing a machine:

  - You collect more data about the machine \to  knowledge

  - You collect reward

- For example

  - Exploration: Choose the next action at to minhH(bt)i

  - Exploitation: Choose the next action at to maxhyti

4:7

### Upper Confidence Bound (UCB1)

1: Initialization: Play each machine once 2: repeat 3: Play the machine i that maximizes ŷi + β q 2 ln n ni 4: until

- ŷi is the average reward of machine i so far

<!-- page: 51 -->
- ni is how often machine i has been played so far

- n = P i ni is the number of rounds so far

- β is often chosen as β = 1

- The bound is derived from the Hoeffding inequality See Finite-time analysis of the multiarmed bandit problem, Auer, Cesa-Bianchi & Fischer, Machine learning, 2002.

4:8

### UCB algorithms

- UCB algorithms determine a confidence interval such that ŷi - σi < hyii < ŷi + σi with high probability. UCB chooses the upper bound of this confidence interval

- Optimism in the face of uncertainty

- Strong bounds on the regret (sub-optimality) of UCB1 (e.g. Auer et al.)

4:9

### UCB for Bernoulli**

- If we have a single Bernoulli bandits, we can count a = 1 + #wins , b = 1 + #losses

- Our posterior over the Bernoulli parameter \mu is $Beta(\mu | a, b)$

- The mean is h\mu_i = a a+b The mode (most likely) is \mu∗ = a-1 a+b-2 for a, b > 1 The variance is Var{\mu} = ab (a+b+1)(a+b)2 One can numerically compute the inverse cumulative Beta distribution \to  get exact quantiles

- Alternative strategies: argmax i 90%-$quantile(\mu_i)$ argmax i h\mu_ii + β p Var{\mu_i}

4:10

<!-- page: 52 -->
### UCB for Gauss**

- If we have a single Gaussian bandits, we can compute the mean estimator \mû = 1 n P i yi the empirical variance σ̂2 = 1 n-1 P i(yi - \mû)2 and the estimated variance of the mean estimator Var{\mû} = σ̂2 /n

- \mû and Var{\mû} describe our posterior Gaussian belief over the true underlying \mu Using the err-function we can get exact quantiles

- Alternative strategies: 90%-$quantile(\mu_i)$ \mûi + β p Var{\mu_i} = \mûi + βσ̂/ \sqrt n

4:11

### UCB - Discussion

- UCB over-estimates the reward-to-go (under-estimates cost-to-go), just like $A^*$

  - but does so in the probabilistic setting of bandits

- The fact that regret bounds exist is great!

- UCB became a core method for algorithms (including planners) to decide what to explore: In tree search, the decision of which branches/actions to explore is itself a decision problem. An “intelligent agent” (like UBC) can be used within the planner to make decisions about how to grow the tree.

4:12

## 4.3 Monte Carlo Tree Search

4:13

### Monte Carlo Tree Search (MCTS)

- MCTS is very successful on Computer Go and other games

- MCTS is rather simple to implement

- MCTS is very general: applicable on any discrete domain

<!-- page: 53 -->
- Key paper: Kocsis & Szepesvári: Bandit based Monte-Carlo Planning, ECML 2006.

- Survey paper: Browne et al.: A Survey of Monte Carlo Tree Search Methods, 2012.

- Tutorial presentation: http://web.engr.oregonstate.edu/˜afern/icaps10-MCP-tutoria ppt

4:14

### Monte Carlo methods

- General, the term Monte Carlo simulation refers to methods that generate many i.i.d. random samples xi ∼ $P(x)$ from a distribution $P(x)$. Using the samples one can estimate expectations of anything that depends on x, e.g. $f(x)$: hfi = Z x $P(x)f(x)$ dx ≈ 1 N N X i=1 $f(x_i)$ (In this view, Monte Carlo approximates an integral.)

- Example: What is the probability that a solitair would come out successful? (Original story by Stan Ulam.) Instead of trying to analytically compute this, generate many random solitairs and count.

- The method developed in the 40ies, where computers became faster. Fermi, Ulam and von Neumann initiated the idea. von Neumann called it “Monte Carlo” as a code name.

4:15

### Flat Monte Carlo

- The goal of MCTS is to estimate the utility (e.g., expected payoff \Delta) depending on the action a chosen—the Q-function: $Q(s_{0}, a)$ = E{\Delta|$s_{0}$, a} where expectation is taken with w.r.t. the whole future randomized actions (including a potential opponent)

- Flat Monte Carlo does so by rolling out many random simulations (using a ROLLOUTPOLICY) without growing a tree The key difference/advantage of MCTS over flat MC is that the tree growth focusses computational effort on promising actions

4:16

<!-- page: 54 -->
### Generic MCTS scheme

![Hinh: fig-54-1]

from Browne et al.
```
1: start tree V = {v_{0}}
$$

2: while within computational budget do

$$
3: vl \leftarrow TREEPOLICY(V ) chooses and creates a new leaf of V
$$

4: append vl to V

$$
5: \Delta \leftarrow ROLLOUTPOLICY(V ) rolls out a full simulation, with return \Delta
```text
6: $BACKUP(vl, \Delta)$ updates the values of all parents of vl 7: end while 8: return best child of $v_{0}$

4:17

### Generic MCTS scheme

- Like FlatMC, MCTS typically computes full roll outs to a terminal state. A heuristic (evaluation function) to estimate the utility of a state is not needed, but can be incorporated.

- The tree grows unbalanced

- The TREEPOLICY decides where the tree is expanded – and needs to trade off exploration vs. exploitation

- The ROLLOUTPOLICY is necessary to simulate a roll out. It typically is a random policy; at least a randomized policy.

4:18

### Upper Confidence Tree (UCT)

- UCT uses UCB to realize the TREEPOLICY, i.e. to decide where to expand the tree

- BACKUP updates all parents of vl as $n(v)$ ← $n(v)$ + 1 (count how often has it been played) $Q(v)$ ← $Q(v)$ + \Delta (sum of rewards received)

<!-- page: 55 -->
- TREEPOLICY chooses child nodes based on UCB: argmax $v_{0}
```\in$\partial (v) $Q(v_{0} )n(v_{0})$ + β s 2 ln $n(v)n(v_{0})$ or choose $v_{0}$ if $n(v_{0} )$ = 0

4:19

## 4.4 MCTS applied to POMDPs**

![Hinh: fig-55-1]

4:20

### Recall POMDPs

agent ...

  - initial state distribution $P(s_{0})$

  - transition probabilities P($s_{0}$
|s, a)

  - observation probabilities P($y_{0}$
|$s_{0}$
, a)

  - reward probabilities $P(r|s, a)$

- An optimal agent maps the history to an action, ($y_{0}$:t, $a_{0}$:t-1) 7\to  at

4:21

### Issues when applying MCTS ideas to POMDPs

- key paper: Silver & Veness: Monte-Carlo Planning in Large POMDPs, NIPS 2010

- MCTS is based on generating rollouts using a simulator

  - Rollouts need to start at a specific state st
\to  Nodes in our tree need to have states associated, to start rollouts from

- At any point in time, the agent has only the history ht = ($y_{0}$:t, $a_{0}$:t-1) to decide on an action

  - The agent wants to estimate the Q-funcion $Q(ht, at)$
\to  Nodes in our tree need to have a history associated

<!-- page: 56 -->
$$
\to Nodes in the search tree will
$$

  - maintain $n(v)$ and $Q(v)$ as before

  - have a history $h(v)$ attached

  - have a set of states $S(v)$ attached

4:22

### MCTS applied to POMDPs

![Hinh: fig-56-1]

from Silver & Veness

4:23

### MCTS applied to POMDPs

- For each rollout:

  - Choose a random world state $s_{0}$ ∼ $S(v_{0})$ from the set of states associated to the root
$v_{0}$; initialize the simulator with this $s_{0}$

  - Use a TREEPOLICY to traverse the current tree; during this, update the state sets
$S(v)$ to contain the world state simulated by the simulator

  - Use a ROLLOUTPOLICY to simulate a full rollout

  - Append a new leaf vl with novel history $h(vl)$ and a single state $S(vl)$ associated

4:24

### Monte Carlo Tree Search

<!-- page: 57 -->
- MCTS combines forward information (starting simulations from $s_{0}$) with backward information (accumulating $Q(v)$ at tree nodes)

- UCT uses an optimistic estimate of return to decide on how to expand the tree

  - this is the stochastic analogy to the $A^*$
heuristic
table PDDL NID MDP POMDP DEC-POMDP Games control
y y y y y ? y

- Conclusion: MCTS is a very generic and often powerful planning method. For many many samples it converges to correct estimates of the Q-function. However, the Q-function can be estimated also using other methods.

4:25

## 4.5 Game Playing

4:26

### Outline

- Minimax

- α–β pruning

- UCT for games

4:27

<!-- page: 58 -->
### Game tree (2-player, deterministic, turns)

![Hinh: fig-58-1]

![Hinh: fig-58-2]

4:28

### Minimax

Perfect play for deterministic, perfect-information games Idea: choose move to position with highest minimax value

$$
= best achievable payoff against best play
$$

4:29

### Minimax algorithm

- Computation by direct recursive function calls, which effectively does DFS

<!-- page: 59 -->
```
function MINIMAX-DECISION(state) returns an action
inputs: state, current state in game
return the a in ACTIONS(state) maximizing MIN-VALUE(RESULT(a,state))
function MAX-VALUE(state) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v ← -∞
for a, s in SUCCESSORS(state) do v ← MAX(v, MIN-VALUE(s))
return v
function MIN-VALUE(state) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v ← ∞
for a, s in SUCCESSORS(state) do v ← MIN(v, MAX-VALUE(s))
return v
```

4:30

### Properties of minimax

![Hinh: fig-59-1]

![Hinh: fig-59-2]

Complete?? Yes, if tree is finite (chess has specific rules for this) Optimal?? Yes, against an optimal opponent. Otherwise?? Time complexity?? $O(bm )$ Space complexity?? $O(bm)$ (depth-first exploration) For chess, b ≈ 35, m ≈ 100 for “reasonable” games

$$
\Rightarrow exact solution completely infeasible
$$

But do we need to explore every path?

4:31

α–β pruning example

<!-- page: 60 -->
![Hinh: fig-60-1]

![Hinh: fig-60-2]

4:32

α–β pruning as instance of branch-and-bound

- α is the best value (to MAX) found so far off the current path

- If V is worse than α, MAX will avoid it $\Rightarrow$ prune that branch

<!-- page: 61 -->
- Define β similarly for MIN

4:33

The α–β algorithm

```
function ALPHA-BETA-DECISION(state) returns an action
return the a in ACTIONS(state) maximizing MIN-VALUE(RESULT(a,state))
function MAX-VALUE(state,α,β) returns a utility value
inputs: state, current state in game
```

α, the value of the best alternative for MAX along the path to state β, the value of the best alternative for MIN along the path to state if TERMINAL-$TEST(state)$ then return $UTILITY(state)$

$$
v \leftarrow -\infty
$$

for a, s in $SUCCESSORS(state)$ do

$$
v \leftarrow MAX(v, MIN-VALUE(s,\alpha,\beta)) if v \geq \beta then return v \alpha \leftarrow MAX(\alpha, v)
$$

return v

```
function MIN-VALUE(state,α,β) returns a utility value
```

same as MAX-VALUE but with roles of α,β reversed

4:34

Properties of α–β

- Pruning does not affect final result

- Good move ordering improves effectiveness of pruning!

- A simple example of the value of reasoning about which computations are relevant (a form of metareasoning)

4:35

### Resource limits

Standard approach:

- Use CUTOFF-TEST instead of TERMINAL-TEST e.g., depth limit

- Use EVAL instead of UTILITY i.e., evaluation function that estimates desirability of position Suppose we have 100 seconds, explore 104 nodes/second $\Rightarrow$ 106 nodes per move ≈ 358/2 $\Rightarrow$ α–β reaches depth 8 $\Rightarrow$ pretty good chess program

4:36

<!-- page: 62 -->
### Evaluation functions

![Hinh: fig-62-1]

![Hinh: fig-62-2]

For chess, typically linear weighted sum of features

$$
EVAL(s) = w1f1(s) + w2f2(s) + . . . + wnfn(s) e.g., w1 = 9 with f1(s) = (number of white queens) – (number of black queens), etc.
$$

4:37

### Upper Confidence Tree (UCT) for games

- Standard backup updates all parents of vl as $n(v)$ ← $n(v)$ + 1 (count how often has it been played) $Q(v)$ ← $Q(v)$ + \Delta (sum of rewards received)

- In games use a “negamax” backup: While iterating upward, flip sign \Delta ← -\Delta in each iteration

- Survey of MCTS applications: Browne et al.: A Survey of Monte Carlo Tree Search Methods, 2012.

4:38

<!-- page: 63 -->
![Hinh: fig-63-1]

<!-- table structure uncertain on page 63 -->

IEEE TRANSACTIONS ON COMPUTATIONAL INTELLIGENCE AND AI IN GAMES, VOL. 4, NO. 1, MARCH 2012 48

Go

Phantom

Go

Blind

Go

NoGo

Multi-player

Go

Hex

Y,

Star,

Renkula!

Havannah

Lines

of

Action

P-Game

Clobber

Othello

Amazons

Arimaa

Khet

Shogi

Mancala

Blokus

Duo

Focus

Chinese

Checkers

Yavalath

Connect

Four

Tic

Tac

Toe

Sum

of

Switches

Chess

LeftRight

Games

Morpion

Solitaire

Crossword

SameGame

Sudoku,

Kakuro

Wumpus

World

Mazes.Tigers,Grids

C

ADIA

P

LAYER

A

RY

Flat MC/UCB + + +

BAST

$TDMC(\lambda)$ +

BB Active Learner

UCT + + + + + + + + + + + + + + + + + + + + + + ? + +

SP-MCTS +

FUSE

MP-MCTS + +

Coalition Reduction

Multi-agent MCTS +

Ensemble MCTS +

HOP

Sparse UCT

Info Set UCT

Multiple MCTS +

UCT+

MCαβ + ?

MCCFR

Reflexive MC +

Nested MC + + + + +

NRPA + +

HGSTS + +

FSSS, BFS3 +

TAG

UNLEO

UCTSAT

ρUCT + +

MRW

MHSP

UCB1-Tuned

Bayesian UCT

EXP3

HOOT

First Play Urgency +

(Anti)Decisive Moves + + + +

Move Groups + +

Move Ordering + + +

Transpositions + + + + +

Progressive Bias +

Opening Books + +

MCPG

Search Seeding +

Parameter Tuning +

History Heuristic + + + + + +

AMAF + + + +

RAVE + + + + + + + + + +

Killer RAVE +

RAVE-max +

PoolRAVE + +

MCTS-Solver +

MC-PNS +

Score Bounded MCTS + +

Progressive Widening + +

Pruning + + + +

Contextual MC + +

Fill the Board + + +

MAST, PAST, FAST +

Simulation Balancing +

Last Good Reply + +

Patterns + + + +

Score Bonus +

Decaying Reward +

Leaf Parallelisation + + + +

Root Parallelisation + +

Tree Parallelisation + +

UCT-Treesplit + +

TABLE 3

Summary of MCTS variations and enhancements applied to combinatorial games.

IEEE TRANSACTIONS ON COMPUTATIONAL INTELLIGENCE AND AI IN GAMES, VOL. 4, NO. 1, MARCH 2012 49

Tron

Ms.

Pac-Man

Pocman,

Battleship

Dead-End

Wargus

ORTS

Skat

Bridge

Poker

Dou

Di

Zhu

Klondike

Solitaire

Magic:

The

Gathering

Phantom

Chess

Urban

Rivals

Backgammon

Settlers

of

Catan

Scotland

Yard

Roshambo

Thurn

and

Taxis

OnTop

Security

Mixed

Integer

Prog.

TSP,

CTP

Sailing

Domain

Physics

Simulations

Function

Approx.

Constraint

Satisfaction

Schedul.

Benchmarks

Printer

Scheduling

Rock-Sample

Problem

PMPs

Bus

Regulation

Large

State

Spaces

Feature

Selection

PCG

Flat MC/UCB + + + + + + + + +

BAST +

$TDMC(\lambda)$

BB Active Learner

UCT + + + + + + + + + + + + + + + + + + + + + + +

SP-MCTS +

FUSE +

MP-MCTS + +

Coalition Reduction +

Multi-agent MCTS

Ensemble MCTS

HOP +

Sparse UCT +

Info Set UCT + +

Multiple MCTS

UCT+ +

MCαβ

MCCFR +

Reflexive MC

Nested MC + + +

NRPA

HGSTS

FSSS, BFS3 +

TAG +

UNLEO

UCTSAT +

ρUCT + + +

MRW +

MHSP +

UCB1-Tuned +

Bayesian UCT

EXP3 +

HOOT +

First Play Urgency

(Anti)Decisive Moves

Move Groups

Move Ordering

Transpositions

Progressive Bias +

Opening Books

MCPG +

Search Seeding

Parameter Tuning

History Heuristic

AMAF +

RAVE +

Killer RAVE

RAVE-max

PoolRAVE

MCTS-Solver +

MC-PNS

Score Bounded MCTS

Progressive Widening +

Pruning +

Contextual MC

Fill the Board

MAST, PAST, FAST

Simulation Balancing

Last Good Reply

Patterns

Score Bonus

Decaying Reward +

Leaf Parallelisation

Root Parallelisation

Tree Parallelisation

UCT-Treesplit

TABLE 4

Summary of MCTS variations and enhancements applied to other domains.

4:39

Brief notes on game theory

\bullet  Zero-sum games can be represented by a payoff matrix

\bullet  Uji denotes the utility of player 1 if she chooses the pure (=deterministic) strat-

egy i and player 2 chooses the pure strategy j.

Zero-sum games: Uji = -Uij , UT

= -U

\bullet  Fining a minimax optimal mixed strategy p is a Linear Program

max

w

w s.t. Up $\geq$ w ,

X

i

pi = 1 , p $\geq$ 0

Note that Up $\geq$ w implies minj(Up)j $\geq$ w.

\bullet  Gainable payoff of player 1: maxp minq qT

Up

Minimax-Theorem: maxp minq qT

Up = minq maxp qT

Up

Minimax-Theorem \leftrightarrow  optimal p with w $\geq$ 0 exists

4:40

4.6 Beyond bandits**

4:41

<!-- page: 64 -->
- Perhaps have a look at the tutorial: Bandits, Global Optimization, Active Learning, and Bayesian RL – understanding the common ground

4:42

### Global Optimization

- Let x $\in$ Rn , f : Rn \to  R, find min x $f(x)$ (I neglect constraints $g(x)\leq$ 0 and $h(x)$ = 0 here – but could be included.)

- Blackbox optimization: find optimium by sampling values yt = $f(xt)$ No access to ∇ f or ∇2 f Observations may be noisy y ∼ N(y | $f(xt)$, σ)

4:43

$$
Global Optimization = infinite bandits \bullet  In global optimization f(x) defines a reward for every x \in Rn
$$

  - Instead of a finite number of actions at we now have xt

- The unknown “world property” is the function θ = f

- Optimal Optimization could be defined as: find π : ht 7\to  xt that minh PT t=1 f(xt)i or minhf(xT )i

4:44

### Gaussian Processes as belief

- If all the infinite bandits would be uncorrelated, there would be no chance to solve the problem \to  No Free Lunch Theorem

- One typically assumes that nearby function values $f(x)$, $f(x_{0} )$ are correlated as described by a covariance function $k(x, x_{0} )$ \to  Gaussian Processes

4:45

<!-- page: 65 -->
### Greedy 1-step heuristics

![Hinh: fig-65-1]

![Hinh: fig-65-2]

- Maximize Probability of Improvement (MPI) from Jones (2001) xt = argmax x R y∗ -$\infty$ N(y| ˆ $f(x)$, σ̂(x))

- Maximize Expected Improvement (EI) xt = argmax x R y∗ -$\infty$ N(y| ˆ $f(x)$, σ̂(x)) (y∗ - y)

- Maximize UCB xt = argmin x ˆ $f(x)$ - βtσ̂(x) (Often, βt = 1 is chosen. UCB theory allows for better choices. See Srinivas et al. citation below.)

4:46

From Srinivas et al., 2012:

4:47

<!-- page: 66 -->
4:48

### Further reading

![Hinh: fig-66-1]

![Hinh: fig-66-2]

- Classically, such methods are known as Kriging

- Information-theoretic regret bounds for gaussian process optimization in the bandit setting Srinivas, Krause, Kakade & Seeger, Information Theory, 2012.

- Efficient global optimization of expensive black-box functions. Jones, Schonlau, & Welch, Journal of Global Optimization, 1998.

- A taxonomy of global optimization methods based on response surfaces Jones, Journal of Global Optimization, 2001.

- Explicit local models: Towards optimal optimization algorithms, Poland, Technical Report No. IDSIA-09-04, 2004.

4:49

## 4.7 Active Learning**

4:50

### Active Learning

<!-- page: 67 -->
- In standard ML, a data set Dt = {(xs, ys)}t-1 s=1 is given. In active learning, the learning agent sequentially decides on each xt – where to collect data

- Generally, the aim of the learner should be to learn as fast as possible, e.g. minimize predictive error

- Again, the unknown “world property” is the function θ = f

- Finite horizon T predictive error problem: Given $P(x* )$, find a policy π : Dt 7\to  xt that minh- log P(y∗ |x∗ , DT )iy∗,x∗,DT ;π This also can be expressed as predictive entropy: h- log P(y∗ |x∗ , DT )iy∗,x∗ = h- R y∗ $P(y* |x* , DT )$ log P(y∗ |x∗ , DT )ix∗ = hH(y∗ |x∗ , DT )ix∗ =: $H(f|DT )$

- Find a policy that min E{DT ; π}$H(f|DT )$

4:51

### Greedy 1-step heuristic

- The simplest greedy policy is 1-step Dynamic Programming: Directly maximize immediate expected reward, i.e., minimizes $H(bt+1)$. π : $bt(f)$ 7\to  argmin xt R yt $P(yt|xt, bt)H(bt[xt, yt])$

- For GPs, you reduce the entropy most if you choose xt where the current predictive variance is highest: Var($f(x)$) = $k(x, x)$ - κ(x)(K + σ2 In)-1 κ(x) This is referred to as uncertainty sampling

- Note, if we fix hyperparameters:

  - This variance is independent of the observations yt, only the set Dt matters!

  - The order of data points also does not matter

  - You can pre-optimize a set of “grid-points” for the kernel – and play them in any
order

4:52

### Further reading

- Active learning literature survey. Settles, Computer Sciences Technical Report 1648, University of Wisconsin-Madison, 2009.

<!-- page: 68 -->
- Bayesian experimental design: A review. Chaloner & Verdinelli, Statistical Science, 1995.

- Active learning with statistical models. Cohn, Ghahramani & Jordan, JAIR 1996.

- ICML 2009 Tutorial on Active Learning, Sanjoy Dasgupta and John Langford http://hunch.net/˜active_learning/

4:53

<!-- page: 69 -->
# 5 Dynamic Programming

![Hinh: fig-69-1]

![Hinh: fig-69-2]

![Hinh: fig-69-3]

### Motivation & Outline

So far we focussed on tree search-like solvers for decision problems. There is a second important family of methods based on dynamic programming approaches, including Value Iteration. The Bellman optimality equation is at the heart of these methods. Such dynamic programming methods are important also because standard Reinforcement Learning methods (learning to make decisions when the environment model is initially unknown) are directly derived from them. 5.1 Markov Decision Process

5:1

### MDP & Reinforcement Learning

- MDPs are the basis of Reinforcement Learning, where $P(s_{0} |s, a)$ is not know by the agent (around 2000, by Schaal, Atkeson, Vijayakumar) (2007, Andrew Ng et al.)

5:2

### Markov Decision Process

<!-- page: 70 -->
$a_{0}s_{0}r_{0}a_{1}s_{1}r_{1}a_{2}s_{2}r_{2}$

$$
P(s_{0:T} +1, a_{0:T} , r_{0:T} ; \pi) = P(s_{0})
$$

QT

$$
t=0 P(at|st; \pi) P(rt|st, at) P(st+1|st, at)
$$

  - world’s initial state distribution $P(s_{0})$

  - world’s transition probabilities $P(st+1 | st, at)$

  - world’s reward probabilities $P(rt | st, at)$

  - agent’s policy π(at | st) = $P(a_{0}|s_{0}; \pi)$ (or deterministic at = π(st))

- Stationary MDP:

  - We assume P($s_{0}$
| s, a) and $P(r|s, a)$ independent of time

  - We also define $R(s, a)$ := E{}r|s, a =
R
r $P(r|s, a)$ dr

5:3

### MDP

![Hinh: fig-70-1]

- In basic discrete MDPs, the transition probability $P(s_{0} |s, a)$ is just a table of probabilities

- The Markov property refers to how we defined state: History and future are conditionally independent given st $I(st+ , st- |st)$ , \forall t+ > t, t- < t

5:4

## 5.2 Dynamic Programming

5:5

### State value function

- We consider a stationary MDP described by $P(s_{0})$ , $P(s_{0} | s, a)$ , $P(r | s, a)$ , π(at | st)

<!-- page: 71 -->
- The value (expected discounted return) of policy π when started in state s: V π (s) = Eπ{$r_{0}$ + γ$r_{1}$ + γ2 $r_{2}$ + · · · | $s_{0}$ =s} discounting factor γ $\in$ [0, 1]

- Definition of optimality: A policy π∗ is optimal iff \forall s : V π∗ (s) = V ∗ (s) where V ∗ (s) = max π V π (s) (simultaneously maximising the value in all states) (In MDPs there always exists (at least one) optimal deterministic policy.)

5:6

An example for a value function... demo: test/mdp runVI

### Values provide a gradient towards desirable states

![Hinh: fig-71-1]

5:7

### Value function

- The value function V is a central concept in all of RL! Many algorithms can directly be derived from properties of the value function.

- In other domains (stochastic optimal control) it is also called cost-to-go function (cost = -reward)

5:8

<!-- page: 72 -->
### Recursive property of the value function

![Hinh: fig-72-1]

V π

$$
(s) = E{r_{0} + \gamma r_1 + \gamma^2 r_{2} + \cdot \cdot \cdot | s_{0} =s; \pi} = E{r_{0} | s_{0} =s; \pi} + \gamma E{r_{1} + \gamma r_2 + \cdot \cdot \cdot | s_{0} =s; \pi} = R(s, \pi(s)) + \gamma
$$

### P

$s_{0}$ P($s_{0}$

[unclear formula]

; π}

$$
= R(s, \pi(s)) + \gamma
$$

### P

$s_{0}$ P($s_{0}$ | s, π(s)) V π ($s_{0}$ )

- We can write this in vector notation V π = Rπ + γP π V π with vectors V π s = V π (s), Rπ s = R(s, π(s)) and matrix P π ss0 = P($s_{0}$ | s, π(s))

- For stochastic π(a|s): V π (s) =

### P

a π(a|s)$R(s, a)$ + γ

### P

$s_{0}$,a π(a|s)$P(s_{0} | s, a)$ V π ($s_{0}$ )

5:9

### Bellman optimality equation

- Recall the recursive property of the value function V π (s) = R(s, π(s)) + γ

### P

$s_{0}$ P($s_{0}$ | s, π(s)) V π ($s_{0}$ )

- Bellman optimality equation V ∗ (s) = maxa h $R(s, a)$ + γ

### P

$s_{0}$ P($s_{0}$

$$
| s, a) V *
$$

($s_{0}$ ) i

$$
with \pi* (s) = argmaxa
$$

h $R(s, a)$ + γ

### P

$s_{0}$ P($s_{0}$

$$
| s, a) V *
$$

($s_{0}$ ) i

$$
(Sketch of proof: If \pi would select another action than argmaxa[\cdot], then \pi0 which = \pi everywhere except \pi0(s) = argmaxa[\cdot] would be better.)
$$

- This is the principle of optimality in the stochastic case

5:10

Richard E. Bellman (1920—1984)

### Bellman’s principle of optimality

A B

$$
A opt \Rightarrow B opt
$$

<!-- page: 73 -->
$$
V * (s) = max
$$

a h $R(s, a)$ + γ P $s_{0}$ P($s_{0}$

$$
| s, a) V *
$$

($s_{0}$ ) i

$$
\pi* (s) = argmax
$$

a h $R(s, a)$ + γ P $s_{0}$ P($s_{0}$

$$
| s, a) V *
$$

($s_{0}$ ) i

5:11

### Value Iteration

- How can we use this to compute V ∗ ?

- Recall the Bellman optimality equation: V ∗ (s) = maxa h $R(s, a)$ + γ P $s_{0}P(s_{0} | s, a)$ V ∗ ($s_{0}$ ) i

- Value Iteration: (initialize Vk=0(s) = 0) \forall s : Vk+1(s) = max a h $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)Vk(s_{0} )$ i stopping criterion: maxs |Vk+1(s) - $Vk(s)$| $\leq$

- Note that V ∗ is a fixed point of value iteration!

- Value Iteration converges to the optimal value function V ∗ (proof below) demo: test/mdp runVI

5:12

State-action value function (Q-function)

- We repeat the last couple of slides for the Q-function...

- The state-action value function (or Q-function) is the expected discounted return when starting in state s and taking first action a: Qπ (s, a) = Eπ{$r_{0}$ + γ$r_{1}$ + γ2 $r_{2}$ + · · · | $s_{0}$ =s, $a_{0}$ =a} = $R(s, a)$ + γ X $s_{0}P(s_{0} | s, a)$ Qπ ($s_{0}$ , π($s_{0}$ )) (Note: V π (s) = Qπ (s, π(s)).)

- Bellman optimality equation for the Q-function Q∗ (s, a) = $R(s, a)$ + γ P $s_{0}P(s_{0} | s, a)$ maxa0 Q∗ ($s_{0}$ , $a_{0}$ ) with π∗ (s) = argmaxa Q∗ (s, a)

5:13

<!-- page: 74 -->
### Q-Iteration

- Recall the Bellman equation: Q∗ (s, a) = $R(s, a)$ + γ P $s_{0}P(s_{0} | s, a)$ maxa0 Q∗ ($s_{0}$ , $a_{0}$ )

- Q-Iteration: (initialize Qk=0(s, a) = 0) \forall s,a : Qk+1(s, a) = $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ max $a_{0}Qk(s_{0} , a_{0} )$ stopping criterion: maxs,a |Qk+1(s, a) - $Qk(s, a)$| $\leq$

- Note that Q∗ is a fixed point of Q-Iteration!

- Q-Iteration converges to the optimal state-action value function Q∗

5:14

### Proof of convergence

- Let \Deltak = ||Q∗ - Qk||$\infty$ = maxs,a |Q∗ (s, a) - $Qk(s, a)$| Qk+1(s, a) = $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ max $a_{0}Qk(s_{0} , a_{0} )\leq R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ max $a_{0}$ h Q∗ ($s_{0}$ , $a_{0}$ ) + \Deltak i = h $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ max $a_{0}$ Q∗ ($s_{0}$ , $a_{0}$ ) i + γ\Deltak = Q∗ (s, a) + γ\Deltak similarly: Qk $\geq$ Q∗ - \Deltak $\Rightarrow$ Qk+1 $\geq$ Q∗ - γ\Deltak

- The proof translates directly also to value iteration

5:15

### For completeness**

- Policy Evaluation computes V π instead of V ∗ : Iterate: \forall s : V π k+1(s) = R(s, π(s)) + γ P $s_{0}$ P($s_{0}$ |s, π(s)) V π k ($s_{0}$ ) Or use matrix inversion V π = (I - γP π )-1 Rπ , which is $O(|S|3 )$.

- Policy Iteration uses V π to incrementally improve the policy:

<!-- page: 75 -->
1. Initialise π0 somehow (e.g. randomly) 2. Iterate:

  - Policy Evaluation: compute V πk or Qπk

  - Policy Update: πk+1(s) ← argmaxa Qπk (s, a)
demo: test/mdp runPI

5:16

### Summary: Bellman equations

- Discounted infinite horizon: V ∗ (s) = max a Q∗ (s, a) = max a h $R(s, a)$ + γ P $s_{0}P(s_{0} | s, a)$ V ∗ ($s_{0}$ ) i Q∗ (s, a) = $R(s, a)$ + γ X $s_{0}P(s_{0} | s, a)$ max $a_{0}$ Q∗ ($s_{0}$ , $a_{0}$ )

- With finite horizon T (non stationary MDP), initializing VT +1(s) = 0 V ∗ t (s) = max a Q∗ t (s, a) = max a h $Rt(s, a)$ + γ P $s_{0}Pt(s_{0} | s, a)$ V ∗ t+1($s_{0}$ ) i Q∗ t (s, a) = $Rt(s, a)$ + γ X $s_{0}Pt(s_{0} | s, a)$ max $a_{0}$ Q∗ t+1($s_{0}$ , $a_{0}$ )

- This recursive computation of the value functions is a form of Dynamic Pro-

### gramming

5:17

### Comments & relations

- Tree search is a form of forward search, where heuristics ($A^*$ or UCB) may optimistically estimate the value-to-go

- Dynamic Programming is a form of backward inference, which exactly computes the value-to-go backward from a horizon

- UCT also estimates $Q(s, a)$, but based on Monte-Carlo rollouts instead of exact Dynamic Programming

- In deterministic worlds, Value Iteration is the same as Dijkstra backward; it labels all nodes with the value-to-go (\leftrightarrow  cost-to-go).

- In control theory, the Bellman equation is formulated for continuous state x and continuous time t and ends-up: - \partial  \partial t V (x, t) = min u h $c(x, u)$ + \partial V \partial x $f(x, u)$ i

<!-- page: 76 -->
which is called Hamilton-Jacobi-Bellman equation. For linear quadratic systems, this becomes the Riccati equation

5:18

### Comments & relations

- The Dynamic Programming principle is applicable throughout the domains

  - but inefficient if the state space is large (e.g. relational or high-dimensional
continuous)

- It requires iteratively computing a value function over the whole state space

5:19

## 5.3 Dynamic Programming in Belief Space

5:20

### Back to the Bandits

- Can Dynamic Programming also be applied to the Bandit problem? We learnt UCB as the standard approach to address Bandits – but what would be the optimal policy?

5:21

### Bandits recap

- Let at $\in$ {1, .., n} be the choice of machine at time t Let yt $\in$ R be the outcome with mean hyat i A policy or strategy maps all the history to a new choice: π : [($a_{1}$, $y_{1}$), ($a_{2}$, $y_{2}$), ..., (at-1, yt-1)] 7\to  at

- Problem: Find a policy π that maxh PT t=1 yti or maxhyT i

- “Two effects” of choosing a machine:

  - You collect more data about the machine \to  knowledge

  - You collect reward

5:22

<!-- page: 77 -->
### The Belief State

![Hinh: fig-77-1]

- “Knowledge” can be represented in two ways:

  - as the full history
ht = [($a_{1}$, $y_{1}$), ($a_{2}$, $y_{2}$), ..., (at-1, yt-1)]

  - as the belief
$bt(\theta)$ = $P(\theta|ht)$
where θ are the unknown parameters θ = (θ1, .., θn) of all machines

- In the bandit case:

  - The belief factorizes $bt(\theta)$ = $P(\theta|ht)$ =
Q
i $bt(\theta_i|ht)$
e.g. for Gaussian bandits with constant noise, θi = \mu_i
$bt(\mu_i|ht)$ = $N(\mu_i|ŷi, ŝi)$
e.g. for binary bandits, θi = pi, with prior $Beta(pi|\alpha, \beta)$:
$bt(pi|ht)$ = $Beta(pi|\alpha + ai,t, \beta + bi,t)$
ai,t =
Pt-1
s=1[as =i][ys =0] , bi,t =
Pt-1
s=1[as =i][ys =1]

5:23

### The Belief MDP

- The process can be modelled as $a_{1}a_{2}a_{3}y_{1}y_{2}y_{3}$ θ θ θ θ or as Belief MDP $a_{1}a_{2}a_{3}y_{1}y_{2}y_{3}$ b0 b1 b2 b3 $P(b0 |y, a, b)$ = ( 1 if b0 = b0 [b,a,y] 0 otherwise , $P(y|a, b)$ = R θa $b(\theta_a)P(y|\theta_a)$

- The Belief MDP describes a different process: the interaction between the information available to the agent (bt or ht) and its actions, where the agent uses his current belief to anticipate observations, $P(y|a, b)$.

- The belief (or history ht) is all the information the agent has avaiable; $P(y|a, b)$ the “best” possible anticipation of observations. If it acts optimally in the Belief MDP, it acts optimally in the original problem. Optimality in the Belief MDP $\Rightarrow$ optimality in the original problem

5:24

<!-- page: 78 -->
### Optimal policies via Dynamic Programming in Belief Space

![Hinh: fig-78-1]

- The Belief MDP: $a_{1}a_{2}a_{3}y_{1}y_{2}y_{3}$ b0 b1 b2 b3 $P(b0 |y, a, b)$ = ( 1 if b0 = b0 [b,a,y] 0 otherwise , $P(y|a, b)$ = R θa $b(\theta_a)P(y|\theta_a)$

- Belief Planning: Dynamic Programming on the value function \forall b : Vt-1(b) = max π h PT t=t yti = max at R yt $P(yt|at, b)$ h yt + $Vt(b0 [b,at,yt])$ i

5:25

$$
V * t (h) := max
$$

π Z θ $P(\theta|h)$ V π,θ t (h) (2) V π

$$
t (b) :=
$$

Z θ $b(\theta)$ V π,θ t (b) (3)

$$
V * t (b) := max
$$

π V π

$$
t (b) = max
$$

π Z θ $b(\theta)$ V π,θ t (b) (4)

$$
= max
$$

π Z θ $P(\theta|b)$ h R(π(b), b) + Z b0 P(b0 |b, π(b), θ) V π,θ t+1 (b0 ) i (5)

$$
= max
$$

a max π Z θ $P(\theta|b)$ h $R(a, b)$ + Z b0 $P(b0 |b, a, \theta)$ V π,θ t+1 (b0 ) i (6)

$$
= max
$$

a h $R(a, b)$ + max π Z θ Z b0 $P(\theta|b)P(b0 |b, a, \theta)$ V π,θ t+1 (b0 ) i (7) P(b0

$$
|b, a, \theta) =
$$

Z y $P(b0 , y|b, a, \theta)$ (8)

$$
=
$$

Z y $P(\theta|b, a, b0, y)P(b0, y|b, a)P(\theta|b, a)$ (9)

$$
=
$$

Z y $b0(\theta)P(b0, y|b, a)b(\theta)$ (10)

$$
V * t (b) = max
$$

a h $R(a, b)$ + max π Z θ Z b0 Z y $b(\theta)b0(\theta)P(b0, y|b, a)b(\theta)$ V π,θ t+1 (b0 ) i (11)

$$
= max
$$

a h $R(a, b)$ + max π Z b0 Z y $P(b0 , y|b, a)$ Z θ b0 (θ) V π,θ t+1 (b0 ) i (12)

$$
= max
$$

a h $R(a, b)$ + max π Z y $P(y|b, a)$ Z θ b0 [b,a,y](θ) V π,θ t+1 (b0 [b,a,y]) i (13)

$$
= max
$$

a h $R(a, b)$ + max π Z y $P(y|b, a)$ V π (b0 [b,a,y]) i (14)

$$
= max
$$

a h $R(a, b)$ + Z y $P(y|b, a)$ max π V π (b0 [b,a,y]) i (15)

$$
= max
$$

a h $R(a, b)$ + Z y

$$
P(y|b, a) V *
$$

t+1(b0 [b,a,y]) i (16)

5:26

<!-- page: 79 -->
### Optimal policies

- The value function assigns a value (maximal achievable expected return) to a state of knowledge

- While UCB approximates the value of an action by an optimistic estimate of immediate return; Belief Planning acknowledges that this really is a sequencial decision problem that requires to plan

- Optimal policies “navigate through belief space”

  - This automatically implies/combines “exploration” and “exploitation”

  - There is no need to explicitly address “exploration vs. exploitation” or decide for
one against the other. Optimal policies will automatically do this.

- Computationally heavy: bt is a probability distribution, Vt a function over probability distributions

- The term R yt $P(yt|at, b)$ h yt + $Vt(b0 [b,at,yt] )$ i is related to the Gittins Index: it can be computed for each bandit separately.

5:27

### Example exercise

- Consider 3 binary bandits for T = 10.

  - The belief is 3 Beta distributions $Beta(pi|\alpha + ai, \beta + bi)$ \to  6 integers

  - T = 10 \to  each integer $\leq$ 10

  - $Vt(bt)$ is a function over {0, .., 10}6

- Given a prior α = β = 1, a) compute the optimal value function and policy for the final reward and the average reward problems, b) compare with the UCB policy.

5:28

- The concept of Belief Planning transfers to other uncertain domains: Whenever decisions influence also the state of knowledge

  - Active Learning

  - Optimization

  - Reinforcement Learning (MDPs with unknown environment)

  - POMDPs

5:29

### Conclusions

- We covered two basic types of planning methods

  - Tree Search: forward, but with backward heuristics

<!-- page: 80 -->
  - Dynamic Programming: backward

- Dynamic Programming explicitly describes optimal policies. Exact DP is computationally heavy in large domains \to  approximate DP Tree Search became very popular in large domains, esp. MCTS using UCB as heuristic

- Planning in Belief Space is fundamental

  - Describes optimal solutions to Bandits, POMDPs, RL, etc

  - But computationally heavy

  - Silver’s MCTS for POMDPs annotates nodes with history and belief representatives

5:30

<!-- page: 81 -->
# 6 Reinforcement Learning

![Hinh: fig-81-1]

![Hinh: fig-81-2]

### Motivation & Outline

Reinforcement Learning means to learn to perform well in an previously unknown environment. So it naturally combines the problems of learning about the environment and decision making to receive rewards. In that sense, I think that the RL framework is a core of AI. (But one should also not overstate this: standard RL solvers typically address limited classes of MDPs—and therefore do not solve many other aspects AI.) The notion of state is central in the framework that underlies Reinforcement Learning. One assumes that there is a ‘world state’ and decisions of the agent change the state. This process is formalized as Markov Decision Process (MDP), stating that a new state may only depend the previous state and decision. This formalization leads to a rich family of algorithms underlying both, planning in known environments as well as learning to act in unknown ones. This lecture first introduces MDPs and standard Reinforcement Learning methods. We then briefly focus on the exploration problem—very much related to the exploration-exploitation problem represented by bandits. We end with a brief illustration of policy search, imitation and inverse RL without going into the full details of these. Especially inverse RL is really worth knowing about: the problem is to learn the underlying reward function from example demonstrations. That is, the agent tries to “understand” (human) demonstrations by trying to find a reward function consistent with them. (around 2000, by Schaal, Atkeson, Vijayakumar)

<!-- page: 82 -->
(2007, Andrew Ng et al.)

6:1

### Long history of RL in AI

![Hinh: fig-82-1]

Idea of programming a computer to learn by trial and error (Turing, 1954) SNARCs (Stochastic Neural-Analog Reinforcement Calculators) (Minsky, 54) Checkers playing program (Samuel, 59) Lots of RL in the 60s (e.g., Waltz & Fu 65; Mendel 66; Fu 70) MENACE (Matchbox Educable Naughts and Crosses Engine (Mitchie, 63) RL based Tic Tac Toe learner (GLEE) (Mitchie 68) Classifier Systems (Holland, 75) Adaptive Critics (Barto & Sutton, 81) Temporal Differences (Sutton, 88) from Satinder Singh’s Introduction to RL, videolectures.com

- Long history in Psychology

6:2

### Recall: Markov Decision Process

$a_{0}s_{0}r_{0}a_{1}s_{1}r_{1}a_{2}s_{2}r_{2}$

$$
P(s_{0:T} +1, a_{0:T} , r_{0:T} ; \pi) = P(s_{0})
$$

QT

$$
t=0 P(at|st; \pi) P(rt|st, at) P(st+1|st, at)
$$

  - world’s initial state distribution $P(s_{0})$

  - world’s transition probabilities $P(st+1 | st, at)$

  - world’s reward probabilities $P(rt | st, at)$

<!-- page: 83 -->
  - agent’s policy π(at | st) = $P(a_{0}|s_{0}; \pi)$ (or deterministic at = π(st))

- Stationary MDP:

  - We assume P($s_{0}$
| s, a) and $P(r|s, a)$ independent of time

  - We also define $R(s, a)$ := E{r|s, a} =
R
r $P(r|s, a)$ dr

6:3

### Recall

- Bellman equations V ∗ (s) = max a Q∗ (s, a) = max a h $R(s, a)$ + γ P $s_{0}P(s_{0} | s, a)$ V ∗ ($s_{0}$ ) i Q∗ (s, a) = $R(s, a)$ + γ X $s_{0}P(s_{0} | s, a)$ max $a_{0}$ Q∗ ($s_{0}$ , $a_{0}$ )

- Value-/Q-Iteration \forall s : Vk+1(s) = max a h $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)Vk(s_{0} )$ i \forall s,a : Qk+1(s, a) = $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ max $a_{0}Qk(s_{0} , a_{0} )$

6:4

### Towards Learning

- From Sutton & Barto’s Reinforcement Learning book: The term dynamic programming (DP) refers to a collection of algorithms that can be used to compute optimal policies given a perfect model of the environment as a Markov decision process (MDP). Classical DP algorithms are of limited utility in reinforcement learning both because of their assumption of a perfect model and because of their great computational expense, but they are still important theoretically. DP provides an essential foundation for the understanding of the methods presented in the rest of this book. In fact, all of these methods can be viewed as attempts to achieve much the same effect as DP, only with less computation and without assuming a perfect model of the environment.

- So far, we introduced basic notions of an MDP and value functions and methods to compute optimal policies assuming that we know the world (know $P(s_{0} |s, a)$ and $R(s, a)$) Value Iteration and Q-Iteration are instances of Dynamic Programming

- Reinforcement Learning?

6:5

<!-- page: 84 -->
## 6.1 Learning in MDPs

![Hinh: fig-84-1]

6:6

# model-based

# model-free

Q - l e a r n i n g T D - l e a r n i n g m o d e l l e a r n i n g a c t i o n s e l e c t i o n p l a n n i n g dynamic prog. policy search {(s, a, r, $s_{0}$ )} V (s), $Q(s, a)$ P ($s_{0}$ | a, s) $R(s, a)$ model value π(a | s) policy data

6:7

### Learning in MDPs

- While interacting with the world, the agent collects data of the form D = {(st, at, rt, st+1)}T t=1 (state, action, immediate reward, next state) What could we learn from that?

- Model-based RL: learn to predict next state: estimate $P(s_{0} |s, a)$ learn to predict immediate reward: estimate $P(r|s, a)$

- Model-free RL: learn to predict value: estimate V (s) or $Q(s, a)$

- Policy search: e.g., estimate the “policy gradient”, or directly use black box (e.g. evolutionary) search

6:8

Let’s introduce basic model-free methods first.

<!-- page: 85 -->
experience knowledge behaviour value l e a r n i n g a c t i o n s e l e c t i o n

### model-free

![Hinh: fig-85-1]

6:9

$$
Q-learning: Temporal-Difference (TD) learning of Q*
$$

- Recall the Bellman optimality equation for the Q-function: Q∗ (s, a) = $R(s, a)$ + γ P $s_{0}P(s_{0} |s, a)$ maxa0 Q∗ ($s_{0}$ , $a_{0}$ )

- Q-learning (Watkins, 1988) Given a new experience (s, a, r, $s_{0}$ ) $Qnew(s, a)$ = (1 - α) $Qold(s, a)$ + α [r + γmax $a_{0}Qold(s_{0} , a_{0} )$] = $Qold(s, a)$ + α [r + γ max $a_{0}Qold(s_{0} , a_{0} )$ - $Qold(s, a)$ | {z } TD error ]

- Reinforcement:

  - more reward than expected (r > $Qold(s, a)$ - γ maxa0 Qold($s_{0}$
, $a_{0}$
))
\to  increase $Q(s, a)$

  - less reward than expected (r < $Qold(s, a)$ - γ maxa0 Qold($s_{0}$
, $a_{0}$
))
\to  decrease $Q(s, a)$

6:10

### Q-learning pseudo code

- Q-learning is called off-policy: We estimate Q∗ while executing π

- Q-learning:

<!-- page: 86 -->
$$
1: Initialize Q(s, a) = 0
$$

2: repeat // for each episode 3: Initialize start state s 4: repeat // for each step of episode 5: Choose action a ≈ argmaxa $Q(s, a)$ 6: Take action a, observe r, $s_{0}$

$$
7: Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma maxa0 Q(s_{0}, a_{0}) - Q(s, a)] 8: s \leftarrow s_{0}
$$

9: until end of episode 10: until happy

- -greedy action selection: a ≈ argmax a $Q(s, a)$ \Leftarrow $\Rightarrow$ a = ( random with prob. argmaxa $Q(s, a)$ else

6:11

### Q-learning convergence with prob 1

- Q-learning is a stochastic approximation of Q-Iteration: Q-learning: $Qnew(s, a)$ = (1 - α)$Qold(s, a)$ + α[r + γ maxa0 $Qold(s_{0} , a_{0} )$] Q-Iteration: \forall s,a : Qk+1(s, a) = $R(s, a)$ + γ P $s_{0}P(s_{0} |s, a)$ maxa0 $Qk(s_{0} , a_{0} )$ We’ve shown convergence of Q-Iteration to Q∗

- Convergence of Q-learning: Q-Iteration is a deterministic update: Qk+1 = $T(Qk)$ Q-learning is a stochastic version: Qk+1 = (1 - α)Qk + α[$T(Qk)$ + ηk] ηk is zero mean!

6:12

### Q-learning impact

- Q-Learning was the first provably convergent direct adaptive optimal control algorithm

- Great impact on the field of Reinforcement Learning in 80/90ies

  - “Smaller representation than models”

  - “Automatically focuses attention to where it is needed,”
i.e., no sweeps through state space

  - Can be made more efficient with eligibility traces

6:13

<!-- page: 87 -->
Variants: $TD(\lambda)$, $Sarsa(\lambda)$, $Q(\lambda)$

- $TD(\lambda)$: \forall s : V (s) ← V (s) + α $e(s)$ [rt + γ$Vold(st+1)$ - $Vold(st)$]

- $Sarsa(\lambda)$ \forall s,a : $Q(s, a)$ ← $Q(s, a)$ + α $e(s, a)$ [r + γ$Qold(s_{0} , a_{0} )$ - $Qold(s, a)$]

- $Q(\lambda)$ \forall s,a : $Q(s, a)$ ← $Q(s, a)$ + α $e(s, a)$ [r + γ maxa0 $Qold(s_{0} , a_{0} )$ - $Qold(s, a)$]

- On-policy vs. off-policy learning:

  - On–policy: estimate Qπ
while executing π (Sarsa, TD)

  - Off–policy: estimate Q∗
while executing π (Q-learning)

6:14

### Eligibility traces

- Temporal Difference: based on single experience ($s_{0}$, $r_{0}$, $s_{1}$) $Vnew(s_{0})$ = $Vold(s_{0})$ + α[$r_{0}$ + γ$Vold(s_{1})$ - $Vold(s_{0})$]

- Longer experience sequence, e.g.: ($s_{0}$, $r_{0}$, $r_{1}$, $r_{2}$, $s_{3}$) Temporal credit assignment, think further backwards: receiving $r_{0}$:2 and ending up in $s_{3}$ also tells us something about V ($s_{0}$) $Vnew(s_{0})$ = $Vold(s_{0})$ + α[$r_{0}$ + γ$r_{1}$ + γ2 $r_{2}$ + γ3 $Vold(s_{3})$ - $Vold(s_{0})$]

- $TD(\lambda)$: remember where you’ve been recently (“eligibility trace”) and update those values as well: $e(st)$ ← $e(st)$ + 1 \forall s : $Vnew(s)$ = $Vold(s)$ + α $e(s)$ [rt + γ$Vold(st+1)$ - $Vold(st)$] \forall s : $e(s)$ ← γλ$e(s)$

- Core topic of Sutton & Barto book \to  great improvement of basic RL algorithms

6:15

<!-- page: 88 -->
$Q(\lambda)$ pseude code

$$
1: Initialize Q(s, a) = 0, e(s, a) = 0
$$

2: repeat // for each episode 3: Initialize start state s 4: repeat // for each step of episode 5: Choose action a ≈ argmaxa $Q(s, a)$

$$
6: Update eligibility: e(s, a) \leftarrow 1 or e(s, a) \leftarrow e(s, a) + 1
$$

7: Take action a, observe r, $s_{0}$

$$
8: Compute TD-error D = [r + \gamma maxa0 Q(s_{0}, a_{0}) - Q(s, a)] 9: \forall 	ilde{s},ã with e(s̃, ã) > 0: Q(s̃, ã) \leftarrow Q(s̃, ã) + \alpha e(s̃, ã) D 10: Discount all eligibilities \forall 	ilde{s},ã : e(s̃, ã) \leftarrow \gamma\lambda e(s̃, ã) 11: s \leftarrow s_{0}
$$

12: until end of episode 13: until happy

- Analogously for $TD(\lambda)$ and $SARSA(\lambda)$

6:16

### Experience Replay

- In large state spaces, the Q-fucntion is represented using function approximation We cannot store a full table $e(s, a)$ and update \forall s̃,ã

- Instead we store the full data D = {(si, ai, ri, si+1)}t i=o up to now (time t), called the replay buffer

- Update the Q-function for a B subsample (of contant size) of D plus the most recent experience \forall (s, a, r, $s_{0}$ ) $\in$ B : $Q(s, a)$ ← $Q(s, a)$ + α [r + γ max $a_{0}Q(s_{0} , a_{0} )$ - $Q(s, a)$] (See paper “A Deeper Look at Experience Replay” (Zhang, Sutton))

6:17

### TD-Gammon, by Gerald Tesauro**

(See section 11.1 in Sutton & Barto’s book.)

- MLP to represent the value function V (s)

<!-- page: 89 -->
- Only reward given at end of game for win.

- Self-play: use the current policy to sample moves on both sides!

- random policies \to  games take up to thousands of steps. Skilled players ∼ 50 - 60 steps.

- $TD(\lambda)$ learning (gradient-based update of NN weights)

6:18

### TD-Gammon notes**

![Hinh: fig-89-1]

- Choose features as raw position inputs (number of pieces at each place) \to  as good as previous computer programs

- Using previous computer program’s expert features \to  world-class player

- Kit Woolsey was world-class player back then:

  - TD-Gammon particularly good on vague positions

  - not so good on calculable/special positions

  - just the opposite to (old) chess programs

- See anotated matches: http://www.bkgm.com/matches/woba.html

- Good example for

  - value function approximation

  - game theory, self-play

6:19

<!-- page: 90 -->
### Detour: Dopamine**

![Hinh: fig-90-1]

Montague, Dayan & Sejnowski: A Framework for Mesencephalic Dopamine Systems based on Predictive Hebbian Learning. Journal of Neuroscience, 16:1936-1947, 1996.

6:20

So what does that mean?

  - We derived an algorithm from a general framework

  - This algorithm involves a specific variable (reward residual)

  - We find a neural correlate of exactly this variable
Great!
Devil’s advocate:

  - Does not proof that TD learning is going on
Only that an expected reward is compared with a experienced reward

  - Does not discriminate between model-based and model-free
(Both can induce an expected reward)

6:21

### Limitations of the model-free view

- Given learnt values, behavior is a fixed SR (or state-action) mapping

- If the “goal” changes: need to re-learn values for every state in the world! all previous values are obsolete

- No general “knowledge”, only values

- No anticipation of general outcomes ($s_{0}$ ), only of value

<!-- page: 91 -->
- No “planning”

6:22

Wolfgang Köhler (1917) Intelligenzprüfungen am Menschenaffen The Mentality of Apes model-free RL? NO WAY!

6:23

### Detour: Psychology**

![Hinh: fig-91-1]

![Hinh: fig-91-2]

![Hinh: fig-91-3]

![Hinh: fig-91-4]

Edward Tolman (1886 - 1959) Wolfgang Köhler (1887–1967) learn facts about the world that they could subsequently use in a flexible manner, rather than simply learning automatic responses Clark Hull (1884 - 1952) Principles of Behavior (1943) learn stimulus-response mappings based on reinforcement

6:24

### Goal-directed vs. habitual: Devaluation**

[skinner]

<!-- page: 92 -->
Niv, Joel & Dayan: A normative perspective on motivation. TICS, 10:375-381, 2006.

6:25

### Goal-directed vs. habitual: Devaluation**

![Hinh: fig-92-1]

![Hinh: fig-92-2]

Niv, Joel & Dayan: A normative perspective on motivation. TICS, 10:375-381, 2006.

6:26

By definition, goal-directed behavior is performed to obtain a desired goal. Although all instrumental behavior is instrumental in achieving its contingent goals, it is not necessarily purposively goal-directed. Dickinson and Balleine [1,11] proposed that behavior is goal-directed if: (i) it is sensitive to the contingency between action and outcome, and (ii) the outcome is desired. Based on the second condition, motivational manipulations have been used to distinguish between two systems of action control: if an instrumental

<!-- page: 93 -->
outcome is no longer a valued goal (for instance, food for a sated animal) and the behavior persists, it must not be goaldirected. Indeed, after moderate amounts of training, outcome revaluation brings about an appropriate change in instrumental actions (e.g. leverpressing) [43,44], but this is no longer the case for extensively trained responses ([30,31], but see [45]). That extensive training can render an instrumental action independent of the value of its consequent outcome has been regarded as the experimental parallel of the folk psychology maxim that wellperformed actions become habitual [9] (see Figure I). Niv, Joel & Dayan: A normative perspective on motivation. TICS, 10:375-381, 2006.

6:27

### Model-based RL

experience knowledge behaviour value l e a r n i n g p l a n n i n g model-based

- Model learning: Given data D = {(st, at, rt, st+1)}T t=1 estimate $P(s_{0} |s, a)$ and $R(s, a)$. For instance:

  - discrete state-action: P̂($s_{0}$
|s, a) = #($s_{0}$
,s,a)
#(s,a)

  - continuous state-action: P̂($s_{0}$
|s, a) = N($s_{0}$
| φ(s, a)>
β, Σ)
estimate parameters β (and perhaps Σ) as for regression
(including non-linear features, regularization, cross-validation!)

- Planning, for instance:

  - discrete state-action: Value Iteration with the estimated model

  - continuous state-action: Least Squares Value Iteration
Stochastic Optimal Control (Riccati, Differential Dynamic Prog.)

6:28

<!-- page: 94 -->
(around 2000, by Schaal, Atkeson, Vijayakumar)

- Use a simple regression method (locally weighted Linear Regression) to estimate $P(ẋ|u, x)$ local = $N(ẋ | Ax + Bu, \sigma)$

6:29

## 6.2 Exploration

![Hinh: fig-94-1]

6:30

### -greedy exploration in Q-learning

$$
1: Initialize Q(s, a) = 0
$$

2: repeat // for each episode 3: Initialize start state s 4: repeat // for each step of episode

$$
5: Choose action a =
$$

( random with prob. argmaxa $Q(s, a)$ else 6: Take action a, observe r, $s_{0}$

$$
7: Qnew(s, a) \leftarrow Qold(s, a) + \alpha [r + \gamma maxa0 Qold(s_{0}, a_{0}) - Qold(s, a)] 8: s \leftarrow s_{0}
$$

9: until end of episode 10: until happy

6:31

<!-- page: 95 -->
### Optimistic initialization & UCB

- Initialize the Q function optimistically! E.g., if you know Rmax, $Q(s, a)$ = 1/(1 - γ)Rmax (in practise, this is often too large..)

- UCB: If you can estimate a confidence bound σ(s, a) for your Q-function (e.g., using bootstrap estimates when using function approximation), choose your action based on $Q(s, a)$ + βσ(s, a)

- Generally, we need better ways to explore than -greedy!!

6:32

R-MAX Brafman and Tennenholtz (2002)

- Model-based RL: We estimate $R(s, a)$ and $P(s_{0} |s, a)$ on the fly

- Use an optimistic reward function: 1 RR-MAX (s, a) =

$$
R(s, a) c(s, a)\geq m (s, a known)
$$

Rmax $c(s, a)$<m (s, a unknown)

- Is PAC-MDP efficient

- Optimism in the face of uncertainty

6:33

### KWIK-R-max**

(Li, Littman, Walsh, Strehl, 2011)

- Extension of R-MAX to more general representations

- Let’s say the transition model $P(s_{0} | s, a)$ is defined by n parameters Typically, n number of states!

- Efficient KWIK-learner L requires a number of samples which is polynomial in n to estimate approximately correct P̂($s_{0}$ | s, a) (KWIK = Knows-what-it-knows framework)

- KWIK-R-MAX using L is PAC-MDP efficient in n \to  polynomial in number of parameters of transition model! \to  more efficient than plain R-MAX by several orders of magnitude!

6:34

<!-- page: 96 -->
### Bayesian RL**

- There exists an optimal solution to the exploration-exploitation trade-off: belief planning (see my tutorial “Bandits, Global Optimization, Active Learning, and Bayesian RL – understanding the common ground”) V π (b, s) = R(s, π(b, s)) + Z b0,$s_{0}$ P(b0 , $s_{0}$ | b, s, π(b, s)) V π (b0 , $s_{0}$ )

  - Agent maintains a distribution (belief) $b(m)$ over MDP models m

  - typically, MDP structure is fixed; belief over the parameters

  - belief updated after each observation (s, a, r, $s_{0}$
): b \to  b0

  - only tractable for very simple problems

- Bayes-optimal policy π∗ = argmaxπ V π (b, s)

  - no other policy leads to more rewards in expectation w.r.t. prior distribution over
MDPs

  - solves the exploration-exploitation tradeoff

6:35

### Optimistic heuristics

- As with UCB, choose estimators for R∗ , P∗ that are optimistic/over-confident $Vt(s)$ = max a h R∗ + P $s_{0}$ P∗ ($s_{0}$ |s, a) Vt+1($s_{0}$ ) i

- Rmax:

  - R∗
(s, a) =
(
Rmax if #s,a < n
θ̂rsa otherwise
, P∗
($s_{0}$
|s, a) =
(
δs0s∗ if #s,a < n
θ̂s0sa otherwise

  - Guarantees over-estimation of values, polynomial PAC results!

  - Read about “KWIK-Rmax”! (Li, Littman, Walsh, Strehl, 2011)

- Bayesian Exploration Bonus (BEB), Kolter & Ng (ICML 2009)

  - Choose P∗
($s_{0}$
|s, a) = P($s_{0}$
|s, a, b) integrating over the current belief $b(\theta)$ (non-over-
confident)

  - But choose R∗
(s, a) = θ̂rsa+ β
1+α0(s,a)
with a hyperparameter α0(s, a), over-estimating
return

- Confidence intervals for V -/Q-function (Kealbling ’93, Dearden et al. ’99)

6:36

### More ideas about exploration

- Intrinsic rewards for learning progress

  - “fun”, “curiousity”

  - in addition to the external “standard” reward of the MDP

<!-- page: 97 -->
  - “Curious agents are interested in learnable but yet unknown regularities, and get bored by
both predictable and inherently unpredictable things.” (J. Schmidhuber)

  - Use of a meta-learning system which learns to predict the error that the learning
machine makes in its predictions; meta-predictions measure the potential interest-
ingness of situations (Oudeyer et al.)

- Dimensionality reduction for model-based exploration in continuous spaces: lowdimensional representation of the transition function; focus exploration on relevant dimensions (A. Nouri, M. Littman)

6:37

## 6.3 Policy Search, Imitation, & Inverse RL**

![Hinh: fig-97-1]

6:38

# model-based

# model-free

Q - l e a r n i n g T D - l e a r n i n g m o d e l l e a r n i n g a c t i o n s e l e c t i o n p l a n n i n g dynamic prog. policy search {(s, a, r, $s_{0}$ )} V (s), $Q(s, a)$ P ($s_{0}$ | a, s) $R(s, a)$ model value π(a | s) policy data

  - Policy gradients are one form of policy search.

  - There are other, direct policy search methods
(e.g., plain stochastic search, “Covariance Matrix Adaptation”)

6:39

### Five approaches to learning behavior**

<!-- page: 98 -->
Policy Search Inverse RL Imitation Learning

### Model-free

![Hinh: fig-98-1]

![Hinh: fig-98-2]

### Model-based

learn value fct. V (s) policy π(s) optimize policy learn latent costs $R(s, a)$ dynamic prog. π(s) policy learn policy π(s) policy learn model π(s) $P(s_{0} |s, a)R(s, a)$ dynamic prog. V (s) V (s) π(s) demonstration data experience data

[unclear formula]

}n

$$
d=1 D = {(st, at, rt)}T t=0
$$

6:40

### Policy Gradients**

- In continuous state/action case, represent the policy as linear in arbitrary state features: π(s) = k X j=1 φ$j(s)$βj = φ(s)> β (deterministic) π(a | s) = N(a | φ(s)> β, Σ) (stochastic) with k features φj.

- Basically, given an episode ξ = (st, at, rt)H t=0, we want to estimate \partial V (β) \partial β

6:41

### Policy Gradients**

- One approach is called REINFORCE: \partial V (β) \partial β = \partial  \partial β Z $P(\xi_i|\beta)R(\xi_i)$ dξ = Z $P(\xi_i|\beta)$ \partial  \partial β log P(ξ|β)R(ξ)dξ = Eξ|β{ \partial  \partial β log P(ξ|β)$R(\xi_i)$} = Eξ|β{ H X t=0 γt \partial  log π(at|st) \partial β H X $t_{0}$=t γ$t_{0}$ -t rt0 | {z } Qπ(st,at,t) }

<!-- page: 99 -->
- Another is PoWER, which requires \partial V (β) \partial β = 0 β ← β + Eξ|β{ PH t=0 tQπ (st, at, t)} Eξ|β{ PH t=0 Qπ(st, at, t)} See: Peters & Schaal (2008): Reinforcement learning of motor skills with policy gradients, Neural Networks. Kober & Peters: Policy Search for Motor Primitives in Robotics, NIPS 2008. Vlassis, Toussaint (2009): Learning Model-free Robot Control by a Monte Carlo EM Algorithm. Autonomous Robots 27, 123-130.

6:42

### Imitation Learning**

[unclear formula]

}n

$$
d=1
$$

learn/copy

$$
\to \pi(s)
$$

- Use ML to imitate demonstrated state trajectories $x_{0}$:T Literature: Atkeson & Schaal: Robot learning from demonstration (ICML 1997) Schaal, Ijspeert & Billard: Computational approaches to motor learning by imitation (Philosophical Transactions of the Royal Society of London. Series B: Biological Sciences 2003) Grimes, Chalodhorn & Rao: Dynamic Imitation in a Humanoid Robot through Nonparametric Probabilistic Inference. (RSS 2006) Rüdiger Dillmann: Teaching and learning of robot tasks via observation of human performance (Robotics and Autonomous Systems, 2004)

6:43

### Imitation Learning**

- There a many ways to imitate/copy the oberved policy: Learn a density model P(at | st)$P(st)$ (e.g., with mixture of Gaussians) from the observed data and use it as policy (Billard et al.) Or trace observed trajectories by minimizing perturbation costs (Atkeson & Schaal 1997)

6:44

### Imitation Learning**

<!-- page: 100 -->
Atkeson & Schaal

6:45

### Inverse RL**

![Hinh: fig-100-1]

[unclear formula]

}n

$$
d=1
$$

learn

$$
\to R(s, a)
$$

DP

$$
\to V (s) \to \pi(s)
$$

- Use ML to “uncover” the latent reward function in observed behavior Literature: Pieter Abbeel & Andrew Ng: Apprenticeship learning via inverse reinforcement learning (ICML 2004) Andrew Ng & Stuart Russell: Algorithms for Inverse Reinforcement Learning (ICML 2000) Nikolay Jetchev & Marc Toussaint: Task Space Retrieval Using Inverse Feedback Control (ICML 2011).

6:46

### Inverse RL (Apprenticeship Learning)**

- Given: demonstrations D = {xd 0:T }n d=1

- Try to find a reward function that discriminates demonstrations from other

### policies

  - Assume the reward function is linear in some features $R(x)$ = w>
φ(x)

  - Iterate:

<!-- page: 101 -->
![Hinh: fig-101-1]

1. Given a set of candidate policies {π0, π1, ..} 2. Find weights w that maximize the value margin between teacher and all other candidates max w,ξ ξ

$$
s.t. \forall\pi_i
$$

: w> hφiD | {z } value of demonstrations

$$
\geq w>
$$

hφiπi | {z } value of πi +ξ ||w||2

$$
\leq 1 3. Compute a new candidate policy \pi_i that optimizes R(x) = w>
$$

φ(x) and add to candidate list. (Abbeel & Ng, ICML 2004)

6:47

6:48

<!-- page: 102 -->
Policy Search Inverse RL Imitation Learning

### Model-free

![Hinh: fig-102-1]

![Hinh: fig-102-2]

### Model-based

learn value fct. V (s) policy π(s) optimize policy learn latent costs $R(s, a)$ dynamic prog. π(s) policy learn policy π(s) policy learn model π(s) $P(s_{0} |s, a)R(s, a)$ dynamic prog. V (s) V (s) π(s) demonstration data experience data

[unclear formula]

}n

$$
d=1 D = {(st, at, rt)}T t=0
$$

6:49

### Conclusions

- Markov Decision Processes and RL provide a solid framework for describing behavioural learning & planning

- Little taxonomy: Policy Search Inverse RL Imitation Learning

### Model-free

### Model-based

learn value fct. V (s) policy π(s) optimize policy learn latent costs $R(s, a)$ dynamic prog. π(s) policy learn policy π(s) policy learn model π(s) $P(s_{0} |s, a)R(s, a)$ dynamic prog. V (s) V (s) π(s) demonstration data experience data

[unclear formula]

}n

$$
d=1 D = {(st, at, rt)}T t=0
$$

6:50

### Basic topics not covered

- Partial Observability (POMDPs) What if the agent does not observe the state st? \to  The policy π(at | bt) needs to build on an internal representation, called belief βt.

<!-- page: 103 -->
- Continuous state & action spaces, function approximation in RL

- Predictive State Representations, etc etc...

6:51

<!-- page: 104 -->
# 7 Other models of interactive domains**

![Hinh: fig-104-1]

## 7.1 Basic Taxonomy of domain models

7:1

### Taxonomy of domains I

- Domains (or models of domains) can be distinguished based on their state representation

  - Discrete, continuous, hybrid

  - Factored

  - Structured/relational

7:2

### Relational representations of state

- The world is composed of objects; its state described in terms of properties and relations of objects. Formally

  - A set of constants (referring to objects)

  - A set of predicates (referring to object properties or relations)

  - A set of functions (mapping to constants)

- A (grounded) state can then described by a conjunction of predicates (and functions). For example:

  - Constants: C1, C2, P1, P2, SFO, JFK

  - Predicates: $At(., .)$, $Cargo(.)$, $Plane(.)$, $Airport(.)$

  - A state description:
$At(C1, SFO)$$\land$$At(C2, JFK)$$\land$$At(P1, SFO)$$\land$$At(P2, JFK)$$\land$$Cargo(C1)$$\land$$Cargo(C2)```text
\land$
$Plane(P1)\land Plane(P2)\land Airport(JFK)\land Airport(SFO)$

7:3

### Taxonomy of domains II

- Domains (or models of domains) can additionally be distinguished based on:

<!-- page: 105 -->
- Categories of Russel & Norvig:

  - Fully observable vs. partially observable

  - Single agent vs. multiagent

  - Deterministic vs. stochastic

  - Known vs. unknown

  - Episodic vs. sequential

  - Static vs. dynamic

  - Discrete vs. continuous

- We add:

  - Time discrete vs. time continuous

7:4

### Overview of common domain models

![Hinh: fig-105-1]

prob. rel. multi PO cont.time table - - - - - PDDL (STRIPS rules) - + + - - NDRs + + - - - MDP + - - - - relational MDP + + - - - POMDP + - - + - DEC-POMDP + - + + - Games - + + - - differential eqns. (control) - - + + stochastic diff. eqns. (SOC) + - + + PDDL: Planning Domain Definition Language, STRIPS: STanford Research Institute Problem Solver, NDRs: Noisy Deictic Rules, MDP: Markov Decision Process, POMDP: Partially Observable MDP, DEC-POMDP: Decentralized POMDP, SOC: Stochastic Optimal Control

7:5

### PDDL

- Planning Domain Definition Language Developed for the 1998/2000 International Planning Competition (IPC)

<!-- page: 106 -->
(from Russel & Norvig)

- PDDL describes a deterministic mapping (s, a) 7\to  $s_{0}$ , but

  - using a set of action schema (rules) of the form
$ActionName(...)$ : PRECONDITION \to  EFFECT

  - where action arguments are variables and the preconditions and effects are con-
junctions of predicates

7:6

### PDDL

![Hinh: fig-106-1]

![Hinh: fig-106-2]

![Hinh: fig-106-3]

7:7

### PDDL

- The state-of-the-art solvers are actually $A^*$ methods. But the heuristics!!

<!-- page: 107 -->
- Scale to huge domains

- Fast-Downward is great

7:8

### Noisy Deictic Rules (NDRs)

![Hinh: fig-107-1]

![Hinh: fig-107-2]

- Noisy Deictic Rules (Pasula, Zettlemoyer, & Kaelbling, 2007)

- A probabilistic extension of “PDDL rules”:

- These rules define a probabilistic transition probability $P(s_{0} |s, a)$ Namely, if (s, a) has a unique covering rule r, then $P(s_{0} |s, a)$ = $P(s_{0} |s, r)$ = mr X i=0 pr,i $P(s_{0} |\Omega_{r},i, s)$ where $P(s_{0}|\Omega_{r},i, s)$ describes the deterministic state transition of the ith outcome (see Lang & Toussaint, JAIR 2010).

7:9

- While such rule based domain models originated from classical AI research, the following were strongly influenced also from stochastics, decision theory, Machine Learning, etc..

7:10

### Partially Observable MDPs

7:11

### Recall the general setup

- We assume the agent is in interaction with a domain.

  - The world is in a state st $\in$ S

  - The agent senses observations yt $\in$ O

  - The agent decides on an action at $\in$ A

  - The world transitions in a new state st+1

<!-- page: 108 -->
agent $s_{0}s_{1}a_{0}s_{2}a_{1}s_{3}a_{2}a_{3}y_{0}y_{1}y_{2}y_{3}$

- Generally, an agent maps the history to an action, ht = ($y_{0}$:t, $a_{0}$:t-1) 7\to  at

7:12

### POMDPs

![Hinh: fig-108-1]

- Partial observability adds a totally new level of complexity!

- Basic alternative agent models:

  - The agent maps yt 7\to  at
(stimulus-response mapping.. non-optimal)

  - The agent stores all previous observations and maps $y_{0}$:t, $a_{0}$:t-1 7\to  at
(ok)

  - The agent stores only the recent history and maps yt-k:t, at-k:t-1 7\to  at
(crude, but may be a good heuristic)

  - The agent is some machine with its own internal state nt, e.g., a computer, a finite
state machine, a brain... The agent maps (nt-1, yt) 7\to  nt (internal state update) and
nt 7\to  at

  - The agent maintains a full probability distribution (belief) $bt(st)$ over the state,
maps (bt-1, yt) 7\to  bt (Bayesian belief update), and bt 7\to  at

7:13

### POMDP coupled to a state machine agent

agent $s_{0}s_{1}s_{2}r_{1}r_{0}r_{2}a_{2}y_{2}a_{1}y_{1}a_{0}y_{0}$ n0 n1 n2

7:14

<!-- page: 109 -->
![Hinh: fig-109-1]

![Hinh: fig-109-2]

◦ http://www.darpa.mil/grandchallenge/index.asp

7:15

- The tiger problem: a typical POMDP example:

<!-- page: 110 -->
(from the a “POMDP tutorial”)

7:16

### Solving POMDPs via Dynamic Programming in Belief Space

![Hinh: fig-110-1]

$a_{0}s_{0}s_{1}s_{2}s_{3}a_{1}a_{2}y_{1}y_{2}y_{3}y_{0}r_{0}r_{1}r_{2}$

- Again, the value function is a function over the belief V (b) = max a h $R(b, s)$ + γ P b0 $P(b0 |a, b)$ V (b0 ) i

- Sondik 1971: V is piece-wise linear and convex: Can be described by m vectors (α1, .., αm), each αi = α$i(s)$ is a function over discrete s V (b) = max i P s αi(s)$b(s)$ Exact dynamic programming possible, see Pineau et al., 2003

7:17

### Approximations & Heuristics

- Point-based Value Iteration (Pineau et al., 2003)

  - Compute V (b) only for a finite set of belief points

- Discard the idea of using belief to “aggregate” history

  - Policy directly maps history (window) to actions

  - Optimize finite state controllers (Meuleau et al. 1999, Toussaint et al. 2008)

7:18

### Further reading

- Point-based value iteration: An anytime algorithm for POMDPs. Pineau, Gordon & Thrun, IJCAI 2003.

- The standard references on the “POMDP page” http://www.cassandra.org/ pomdp/

- Bounded finite state controllers. Poupart & Boutilier, NIPS 2003.

- Hierarchical POMDP Controller Optimization by Likelihood Maximization. Toussaint, Charlin & Poupart, UAI 2008.

7:19

<!-- page: 111 -->
### Decentralized POMDPs

![Hinh: fig-111-1]

- Finally going multi agent! (from Kumar et al., IJCAI 2011)

- This is a special type (simplification) of a general DEC-POMDP

- Generally, this level of description is very general, but NEXP-hard Approximate methods can yield very good results, though

7:20

### Controlled System

- Time is continuous, t $\in$ R

- The system state, actions and observations are continuous, $x(t)\in$ Rn , $u(t)\in$ Rd , $y(t)\in$ Rm

- A controlled system can be described as linear: ẋ = Ax + Bu y = Cx + Du with matrices A, B, C, D non-linear: ẋ = $f(x, u)$ y = $h(x, u)$ with functions f, h

- A typical “agent model” is a feedback regulator (stimulus-response) u = Ky

7:21

### Stochastic Control

- The differential equations become stochastic dx = $f(x, u)$ dt + dξx dy = $h(x, u)$ dt + dξy

<!-- page: 112 -->
```
d\xi_i is a Wiener processes with hd\xi_i, d\xi_i = Cij(x, u)
```text
- This is the control theory analogue to POMDPs

7:22

### Overview of common domain models

![Hinh: fig-112-1]

prob. rel. multi PO cont.time table - - - - - PDDL (STRIPS rules) - + + - - NID rules + + - - - MDP + - - - - relational MDP + + - - - POMDP + - - + - DEC-POMDP + - + + - Games - + + - - differential eqns. (control) - - + + stochastic diff. eqns. (SOC) + - + + PDDL: Planning Domain Definition Language, STRIPS: STanford Research Institute Problem Solver, NDRs: Noisy Deictic Rules, MDP: Markov Decision Process, POMDP: Partially Observable MDP, DEC-POMDP: Decentralized POMDP, SOC: Stochastic Optimal Control

7:23

<!-- page: 113 -->
# 8 Constraint Satisfaction Problems

(slides based on Stuart Russell’s AI course)

### Motivation & Outline

Here is a little cut in the lecture series. Instead of focussing on sequential decision problems we turn to problems where there exist many coupled variables. The problem is to find values (or, later, probability distributions) for these variables that are consistent with their coupling. This is such a generic problem setting that it applies to many problems, not only map colouring and sudoku. In fact, many computational problems can be reduced to Constraint Satisfaction Problems or their probabilistic analogue, Probabilistic Graphical Models. This also includes sequential decision problems, as I mentioned in some extra lecture. Further, the methods used to solve CSPs are very closely related to descrete optimization. From my perspective, the main motivation to introduce CSPs is as a precursor to introduce their probabilistic version, graphical models. These are a central language to formulate probabilitic models in Machine Learning, Robotics, AI, etc. Markov Decision Processes, Hidden Markov Models, and many other problem settings we can’t discuss in this lecture are special cases of graphical models. In both settings, CSPs and graphical models, the core it to understand what it means to do inference. Tree search, constraint propagation and belief propagation are the most important methods in this context. In this lecture we first define the CSP problem, then introduce basic methods: sequential assignment with some heuristics, backtracking, and constraint propagation. 8.1 Problem Formulation & Examples

8:1

### Inference

- The core topic of the following lectures is Inference: Given some pieces of information on some things (observed variabes, prior, knowledge base) what is the implication (the implied information, the posterior) on other things (non-observed variables, sentence)

- Decision-Making and Learning can be viewed as Inference:

  - given pieces of information: about the world/game, collected data, assumed
model class, prior over model parameters

  - make decisions about actions, classifier, model parameters, etc

- In this lecture:

<!-- page: 114 -->
  - “Deterministic” inference in CSPs

  - Probabilistic inference in graphical models variabels)

  - Logic inference in propositional & FO logic

8:2

### Constraint satisfaction problems (CSPs)

- In previous lectures we considered sequential decision problems CSPs are not sequential decision problems. However, the basic methods address them by testing sequentially ’decisions’

- CSP:

  - We have n variables xi, each with domain Di, xi $\in$ Di

  - We have K constraints Ck, each of which determines the feasible configurations of
a subset of variables

  - The goal is to find a configuration X = ($X1$, .., Xn) of all variables that satisfies all
constraints

- Formally Ck = (Ik, ck) where Ik ⊆ {1, .., n} determines the subset of variables, and ck : DIk \to  {0, 1} determines whether a configuration xIk $\in$ DIk of this subset of variables is feasible

8:3

### Example: Map-Coloring
```
Variables W, N, Q, E, V , S, T (E = New South Wales) Domains Di = {red, green, blue} for all variables
$$

Constraints: adjacent regions must have different colors

$$
e.g., W 6= N, or (W, N) \in {(red, green), (red, blue), (green, red), (green, blue), . . .}
```text
<!-- page: 115 -->
8:4

### Example: Map-Coloring contd.

![Hinh: fig-115-1]

Solutions are assignments satisfying all constraints, e.g.,
```
{W = red, N = green, Q = red, E = green, V = red, S = blue, T = green}
```text
8:5

### Constraint graph

- Pair-wise CSP: each constraint relates at most two variables

- Constraint graph: a bi-partite graph: nodes are variables, boxes are constraints

- In general, constraints may constrain several (or one) variables (|Ik| 6= 2) c1 c2 c3 c6 c8 c4 c5 c7 T V E Q N S W c9

8:6

### Varieties of CSPs

<!-- page: 116 -->
- Discrete variables: finite domains; each Di of size |Di| = d $\RightarrowO(dn )$ complete assignments

  - e.g., Boolean CSPs, incl. Boolean satisfiability infinite domains (integers, strings,
etc.)

  - e.g., job scheduling, variables are start/end days for each job

  - linear constraints solvable, nonlinear undecidable

- Continuous variables

  - e.g., start/end times for Hubble Telescope observations

  - linear constraints solvable in poly time by LP methods

- Real-world examples

  - Assignment problems, e.g. who teaches what class?

  - Timetabling problems, e.g. which class is offered when and where?

  - Hardware configuration

  - Transportation/Factory scheduling

8:7

### Varieties of constraints

![Hinh: fig-116-1]
```
Unary constraints involve a single variable, |Ik| = 1 e.g., S 6= green Pair-wise constraints involve pairs of variables, |Ik| = 2 e.g., S 6= W
```text
Higher-order constraints involve 3 or more variables, |Ik| > 2 e.g., Sudoku

8:8

## 8.2 Methods for solving CSPs

8:9

### Sequential assignment approach

- Let’s start with the straightforward, dumb approach, then fix it. States are defined by the values assigned so far

- Initial state: the empty assignment, { }

- Successor function: assign a value to an unassigned variable that does not conflict with current assignment $\Rightarrow$ fail if no feasible assignments (not fixable!)

- Goal test: the current assignment is complete 1) Every solution appears at depth n with n variables $\Rightarrow$ use depth-first search 2) b = (n - `)d at depth `, hence n!dn leaves!

8:10

<!-- page: 117 -->
### Backtracking sequential assignment

- Two variable assignment decisions are commutative, i.e., [W = red then N = green] same as [N = green then W = red]

- We can fix a single next variable to assign a value to at each node! This drastically reduces the branching factor of the search tree.

- This does not compromise completeness (ability to find the solution) $\Rightarrow$ b = d and there are dn leaves

- Depth-first search for CSPs with single-variable assignments is called backtracking search

- Backtracking search is the basic uninformed algorithm for CSPs Can solve n-queens for n ≈ 25

8:11

### Backtracking search

'''  
function BACKTRACKING-SEARCH(csp) returns solution/failure
return RECURSIVE-BACKTRACKING({ },csp)
function RECURSIVE-BACKTRACKING(assignment,csp) returns soln/failure
if assignment is complete then return assignment
var ← SELECT-UNASSIGNED-VARIABLE(VARIABLES[csp],assignment,csp)
for each value in ORDERED-DOMAIN-VALUES(var,assignment,csp) do
if value is consistent with assignment given CONSTRAINTS[csp] then
add [var = value] to assignment
result ← RECURSIVE-BACKTRACKING(assignment,csp)
if result 6= failure then return result
remove [var = value] from assignment
return failure
'''  

8:12

### Backtracking example

<!-- page: 118 -->
![Hinh: fig-118-1]

![Hinh: fig-118-2]

<!-- page: 119 -->
8:13

### Improving backtracking efficiency

![Hinh: fig-119-1]

![Hinh: fig-119-2]

Simple heuristics can give huge gains in speed: 1. Which variable should be assigned next? 2. In what order should its values be tried? 3. Can we detect inevitable failure early? 4. Can we take advantage of problem structure?

8:14

### Variable order: Minimum remaining values

Minimum remaining values (MRV): choose the variable with the fewest legal values

8:15

<!-- page: 120 -->
### Variable order: Degree heuristic

![Hinh: fig-120-1]

![Hinh: fig-120-2]

Tie-breaker among MRV variables Degree heuristic: choose the variable with the most constraints on remaining variables

8:16

### Value order: Least constraining value

Given a variable, choose the least constraining value: the one that rules out the fewest values in the remaining variables Combining these heuristics makes 1000 queens feasible

8:17

### Constraint propagation

- After each decision (assigning a value to one variable) we can compute what are the remaining feasible values for all variables.

- Initially, every variable has the full domain Di. Constraint propagation reduces these domains, deleting entries that are inconsistent with the new decision.

- These dependencies are recursive: Deleting a value from the domain of one variable might imply infeasibility of some value of another variable \to  contraint propagation. We update domains until they’re all consistent with the constraints. This is Inference

8:18

<!-- page: 121 -->
### Constraint propagation

![Hinh: fig-121-1]

![Hinh: fig-121-2]

- Example: quick failure detection after 2 decisions N and S cannot both be blue!

- Constraint Propagation: propagate the implied constraints serveral steps to reduce remaining domains and detect failures early.

8:19

### Constraint propagation

- Constraint propagation generally loops through the set of constraint, considers each constraint separately, and deletes inconsistent values from its adjacent domains.

- As it considers constraints separately, it does not compute a final solution, as backtracking search does.

8:20

### Arc consistency (=constraint propagation for pair-wise constraints)

- Simplest form of propagation makes each arc consistent

- X \to  Y is consistent iff for every value x of X there is some allowed y

<!-- page: 122 -->
![Hinh: fig-122-1]

![Hinh: fig-122-2]

![Hinh: fig-122-3]

- If X loses a value, neighbors of X need to be rechecked Arc consistency detects failure earlier than forward checking Can be run as a preprocessor or after each assignment

8:21

<!-- page: 123 -->
### Arc consistency algorithm

![Hinh: fig-123-1]

'''  
function AC-3( csp) returns the CSP, possibly with reduced domains
inputs: csp, a pair-wise CSP with variables {X1, X2, . . . , Xn}
local variables: queue, a queue of arcs, initially all the arcs in csp
while queue is not empty do
'''  
```
(Xi, Xj) \leftarrow REMOVE-FIRST(queue)
```text
if REMOVE-INCONSISTENT-$VALUES(Xi, Xj)$ then for each Xk in NEIGHBORS[Xi] do add (Xk, Xi) to queue

'''  
function REMOVE-INCONSISTENT-VALUES( Xi, Xj) returns true iff DOM[Xi] changed
changed ← false
for each x in DOMAIN[Xi] do
if no value y in DOMAIN[Xj] allows (x,y) to satisfy the constraint Xi \leftrightarrow  Xj
then delete x from DOMAIN[Xi]; changed ← true
return changed
'''  

$O(n2d3)$, can be reduced to $O(n2d2)$

8:22

### Constraint propagation

- Very closely related to message passing in probabilistic models

- In practice: design approximate constraint propagation for specific problem E.g.: Sudoku: If Xi is assigned, delete this value from all peers

8:23

### Problem structure

c1 c2 c3 c6 c8 c4 c5 c7 T V E Q N S W c9 Tasmania and mainland are independent subproblems Identifiable as connected components of constraint graph

<!-- page: 124 -->
8:24

### Tree-structured CSPs

![Hinh: fig-124-1]

![Hinh: fig-124-2]

Theorem: if the constraint graph has no loops, the CSP can be solved in $O(n d2 )$ time Compare to general CSPs, where worst-case time is $O(dn )$ This property also applies to logical and probabilistic reasoning!

8:25

### Algorithm for tree-structured CSPs

1. Choose a variable as root, order variables from root to leaves such that every node’s parent precedes it in the ordering 2. For j from n down to 2, apply REMOVEINCONSISTENT(Parent(X This is backward constraint propagation 3. For j from 1 to n, assign Xj consistently with $Parent(Xj)$ This is forward sequential assignment (trivial backtracking)

8:26

<!-- page: 125 -->
### Nearly tree-structured CSPs

![Hinh: fig-125-1]

Conditioning: instantiate a variable, prune its neighbors’ domains Cutset conditioning: instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree
```
Cutset size c \Rightarrow runtime O(dc
```text
· (n - c)d2 ), very fast for small c

8:27

### Summary

- CSPs are a fundamental kind of problem: finding a feasible configuration of n variables the set of constraints defines the (graph) structure of the problem

- Sequential assignment approach Backtracking = depth-first search with one variable assigned per node

- Variable ordering and value selection heuristics help significantly

- Constraint propagation (e.g., arc consistency) does additional work to constrain values and detect inconsistencies

- The CSP representation allows analysis of problem structure

- Tree-structured CSPs can be solved in linear time If after assigning some variables, the remaining structure is a tree \to  linear time feasibility check by tree CSP

8:28

<!-- page: 126 -->
# 9 Graphical Models

### Motivation & Outline

Graphical models are a generic language to express “structured” probabilistic models. Structured simply means that we talk about many random variables and many coupling terms, where each coupling term concerns only a (usually small) subset of random variables. so, structurally they are very similar to CSPs. But the coupling terms are not boolean functions but real-valued functions, called factors. And that defines a probability distribution over all RVs. The problem then is either to find the most probable value assignment to all RVs (called MAP inference problem), or to find the probabilities over the values of a single variable that arises from the couplings (called marginal inference). There are so many applications of graphical models that is it hard to pick some to list: Modelling gene networks (e.g. to understand genetic diseases), structured text models (e.g. to cluster text into topics), modelling dynamic processes like music or human activities (like cooking or so), modelling more structured Markov Decision Processes (hierarchical RL, POMDPs, etc), modelling multi-agent systems, localization and mapping of mobile robots, and also many of the core ML methods can be expressed as graphical models, e.g. Bayesian (kernel) logistic/ridge regression, Gaussian mixture models, clustering methods, many unsupervised learning methods, ICA, PCA, etc. It is though fair to say that these methods do not have to be expressed as graphical models; but they can be and I think it is very helpful to see the underlying principles of these methods when expressing them in terms of graphical models. And graphical models then allow you to invent variants/combinations of such methods specifically for your particular data domain. In this lecture we introduce Bayesian networks and factor graphs and discuss probabilistic inference methods. Exact inference amounts to summing over variables in a certain order. This can be automated in a way that exploits the graph structure, leading to what is called variable elimination and message passing on trees. The latter is perfectly analogous to constraint propagation to exactly solve tree CSPs. For non-trees, message passing becomes loopy belief propagation, which approximates a solution. Monte-Carlo sampling methods are also important tools for approximate inference, which are beyond this lecture though. 9.1 Bayes Nets and Conditional Independence

9:1

### Outline

- A. Introduction

  - Motivation and definition of Bayes Nets

  - Conditional independence in Bayes Nets

  - Examples

<!-- page: 127 -->
- B. Inference in Graphical Models

  - Variable Elimination & Factor Graphs

  - Message passing, Loopy Belief Propagation

  - Sampling methods (Rejection, Importance, Gibbs)

9:2

### Graphical Models

- The core difficulty in modelling is specifying What are the relevant variables? How do they depend on each other? (Or how could they depend on each other \to  learning)

- Graphical models are a graphical notation for 1) which random variables exist 2) which random variables are “directly coupled” Thereby they describe a joint probability distribution $P(X1, .., Xn)$ over n random variables.

- 2 basic variants:

  - Bayesian Networks (aka. directed model, belief network)

  - Factor Graphs (aka. undirected model, Markov Random Field)

9:3

### Example
```
drinking red wine \to longevity?
```text
9:4

### Bayesian Networks

- A Bayesian Network is a

  - directed acyclic graph (DAG)

  - where each node represents a random variable Xi

  - for each node we have a conditional probability distribution
P(Xi | $Parents(Xi)$)

- In the simplest case (discrete RVs), the conditional distribution is represented as a conditional probability table (CPT)

9:5

### Bayesian Networks

- DAG \to  we can sort the RVs; edges only go from lower to higher index

<!-- page: 128 -->
- The joint distribution can be factored as $P(X_{1:n})$ = n Y i=1 P(Xi | $Parents(Xi)$)

- Missing links imply conditional independence

- Forward sampling from joint distribution

9:6

### Example

![Hinh: fig-128-1]

(Heckermann 1995)
```
P(G=empty|B=good,F=not empty)=0.04 P(G=empty|B=good,F=empty)=0.97 P(G=empty|B=bad,F=not empty)=0.10 P(G=empty|B=bad,F=empty)=0.99 P(T=no|B=good)=0.03 P(T=no|B=bad)=0.98 P(S=no|T=yes,F=not empty)=0.01 P(S=no|T=yes,F=empty)=0.92 P(S=no|T=no,Fnot empty)=1.00 P(S=no|T=no,F=empty)=1.00
$$

Fuel Gauge Battery TurnOver Start

$$
P(B=bad) =0.02 P(F=empty)=0.05 \Leftarrow\Rightarrow P(S, T, G, F, B) = P(B) P(F) P(G|F, B) P(T|B) P(S|T, F) \bullet  Table sizes: LHS = 25 - 1 = 31 RHS = 1 + 1 + 4 + 2 + 4 = 12
```text
9:7

### Bayes Nets & conditional independence

- Independence: $Indep(X, Y )$ \Leftarrow $\Rightarrow P(X, Y )$ = $P(X)P(Y )$

- Conditional independence: $Indep(X, Y |Z)$ \Leftarrow $\Rightarrow P(X, Y |Z)$ = $P(X|Z)P(Y |Z)$

<!-- page: 129 -->
Z X Y (head-to-head) $Indep(X, Y )$
```
\neg Indep(X, Y |Z)
$$

Z X Y (tail-to-tail)

$$
\neg Indep(X, Y )
```text
$Indep(X, Y |Z)$ Z X Y (head-to-tail)
```
\neg Indep(X, Y )
```text
$Indep(X, Y |Z)$

9:8

- Head-to-head: $Indep(X, Y )P(X, Y, Z)$ = $P(X)P(Y )P(Z|X, Y )P(X, Y )$ = $P(X)P(Y )$ P Z $P(Z|X, Y )$ = $P(X)P(Y )$

- Tail-to-tail: $Indep(X, Y |Z)P(X, Y, Z)$ = $P(Z)P(X|Z)P(Y |Z)P(X, Y |Z)$ = $P(X, Y, Z)$/$P(Z)$ = $P(X|Z)P(Y |Z)$

- Head-to-tail: $Indep(X, Y |Z)P(X, Y, Z)$ = $P(X)P(Z|X)P(Y |Z)P(X, Y |Z)$ = P (X,Y,Z) P (Z) = P (X,Z) P (Y |Z) P (Z) = $P(X|Z)P(Y |Z)$

9:9

### General rules for determining conditional independence in a Bayes net:

![Hinh: fig-129-1]

- Given three groups of random variables X, Y, Z $Indep(X, Y |Z)$ \Leftarrow $\Rightarrow$ every path from X to Y is “blocked by Z”

- A path is “blocked by Z” \Leftarrow $\Rightarrow$ on this path...

  - \exists  a node in Z that is head-to-tail w.r.t. the path, or

  - \exists  a node in Z that is tail-to-tail w.r.t. the path, or

  - \exists  another node A which is head-to-head w.r.t. the path
and neither A nor any of its descendants are in Z

9:10

### Example

(Heckermann 1995)

<!-- page: 130 -->
```
P(G=empty|B=good,F=not empty)=0.04 P(G=empty|B=good,F=empty)=0.97 P(G=empty|B=bad,F=not empty)=0.10 P(G=empty|B=bad,F=empty)=0.99 P(T=no|B=good)=0.03 P(T=no|B=bad)=0.98 P(S=no|T=yes,F=not empty)=0.01 P(S=no|T=yes,F=empty)=0.92 P(S=no|T=no,Fnot empty)=1.00 P(S=no|T=no,F=empty)=1.00
$$

Fuel Gauge Battery TurnOver Start

$$
P(B=bad) =0.02 P(F=empty)=0.05
```text
$Indep(T, F)$? $Indep(B, F|S)$? $Indep(B, S|T)$?

9:11

### What can we do with Bayes nets?

![Hinh: fig-130-1]

![Hinh: fig-130-2]

- Inference: Given some pieces of information (prior, observed variabes) what is the implication (the implied information, the posterior) on a non-observed variable

- Decision Making: If utilities and decision variables are defined \to  compute optimal decisions in probabilistic domains

- Learning:

  - Fully Bayesian Learning: Inference over parameters (e.g., β)

  - Maximum likelihood training: Optimizing parameters

- Structure Learning (Learning/Inferring the graph structure itself): Decide which model (which graph structure) fits the data best; thereby uncovering conditional independencies in the data.

9:12

### Inference

- Inference: Given some pieces of information (prior, observed variabes) what is the implication (the implied information, the posterior) on a non-observed variable

- In a Bayes Nets: Assume there is three groups of RVs:

<!-- page: 131 -->
  - Z are observed random variables

  - X and Y are hidden random variables

  - We want to do inference about X, not Y
Given some observed variables Z, compute the
posterior marginal $P(X | Z)$ for some hidden variable X.
$P(X | Z)$ =
$P(X, Z)$
$P(Z)$
=
1
$P(Z)$
X
Y
$P(X, Y, Z)$
where Y are all hidden random variables except for X

- Inference requires summing over (eliminating) hidden variables.

9:13

### Example: Holmes & Watson

- Mr. Holmes lives in Los Angeles. One morning when Holmes leaves his house, he realizes that his grass is wet. Is it due to rain, or has he forgotten to turn off his sprinkler?

  - Calculate $P(R|H)$, $P(S|H)$ and compare these values to the prior probabilities.

  - Calculate $P(R, S|H)$.
Note: R and S are marginally independent, but conditionally dependent

- Holmes checks Watson’s grass, and finds it is also wet.

  - Calculate $P(R|H, W)$, $P(S|H, W)$

  - This effect is called explaining away
JavaBayes: run it from the html page
http://www.cs.cmu.edu/˜javabayes/Home/applet.html

9:14

### Example: Holmes & Watson

Watson Holmes
```
P(W=yes|R=yes)=1.0 P(W=yes|R=no)=0.2 P(H=yes|R=yes,S=yes)=1.0 P(H=yes|R=yes,S=no)=1.0 P(H=yes|R=no,S=yes)=0.9 P(H=yes|R=no,S=no)=0.0
$$

Rain

$$
P(R=yes)=0.2
$$

Sprinkler

$$
P(S=yes)=0.1 P(H, W, S, R) = P(H|S, R) P(W|R) P(S) P(R)
$$

<!-- page: 132 -->
$$
P(R|H) =
```text
X W,S $P(R, W, S, H)P(H)$
```
=
```text
1 $P(H)$ X W,S $P(H|S, R)P(W|R)P(S)P(R)$
```
=
```text
1 $P(H)$ X S $P(H|S, R)P(S)P(R)$
```
P(R=1 | H =1) =
$$

1

$$
P(H =1) (1.0 \cdot 0.2 \cdot 0.1 + 1.0 \cdot 0.2 \cdot 0.9) =
$$

1

$$
P(H =1)
$$

0.2

$$
P(R=0 | H =1) =
$$

1

$$
P(H =1) (0.9 \cdot 0.8 \cdot 0.1 + 0.0 \cdot 0.8 \cdot 0.9) =
$$

1

$$
P(H =1)
```text
0.072

9:15

- These types of calculations can be automated \to  Variable Elimination Algorithm

9:16

### Example: Bavarian dialect

D B

- Two binary random $variables(RVs)$: B (bavarian) and D (dialect)

- Given: $P(D, B)$ = $P(D | B)P(B)P(D=1 | B =1)$ = 0.4, $P(D=1 | B =0)$ = 0.01, $P(B =1)$ = 0.15

- Notation: Grey shading usually indicates “observed”

9:17

### Example: Coin flipping

H d1 d2 d3 d4 d5

- One binary RV H (hypothesis), 5 RVs for the coin tosses d1, .., d5

- Given: $P(D, H)$ = Q i $P(di | H)P(H)P(H =1)$ = 999 1000 , $P(di =H | H =1)$ = 1 2 , $P(di =H | H =2)$ = 1

<!-- page: 133 -->
9:18

### Example: Ridge regression**

![Hinh: fig-133-1]

β xi yi
```
i = 1 : n
```text
- One multi-variate RV β, 2n RVs $x_{1}$:n, $y_{1}$:n (observed data)

- Given: $P(D, \beta)$ = Q i h $P(y_i | x_i, \beta)P(x_i)$ i $P(\beta)P(\beta)$ = $N(\beta | 0, \sigma2 \lambda )$, $P(y_i | x_i, \beta)$ = $N(y_i | x> i \beta, \sigma2 )$

- Plate notation: Plates (boxes with index ranges) mean “copy n-times”

9:19

### Example: Gaussian Mixture Model**

ci
```
i = 1 : N
$$

\mu_k, Σk

$$
k = 1 : K
```text
π xi

- Discrete latent RVs c1:n indicating mixture component, cont. RVs $x_{1}$:n (observed data)

- Model: $P(x_i | \mu1:K, \Sigma1:K)$ = PK k=1 $N(x_i | \mu_k, \Sigma_k)P(ci =k)$

9:20

## 9.2 Inference Methods in Graphical Models

9:21

### Inference methods in graphical models

- Message passing:

  - Exact inference on trees (includes the Junction Tree Algorithm)

  - Belief propagation

<!-- page: 134 -->
- Sampling:

  - Rejection samping, importance sampling, Gibbs sampling

  - More generally, Markov-Chain Monte Carlo (MCMC) methods

- Other approximations/variational methods

  - Expectation propagation

  - Specialized variational methods depending on the model

- Reductions:

  - Mathematical Programming (e.g. LP relaxations of MAP)

  - Compilation into Arithmetic Circuits (Darwiche at al.)

9:22

### Variable Elimination

![Hinh: fig-134-1]

9:23

### Variable Elimination example

$X6X3X5X4X2X1X6X3X5X4X2X1$ F1 \mu1 (≡ 1) $X6X3X5X2X1X6X3X5X2X1$ F2 \mu2 $X3X5X2X1$ \mu2 $X3X5X2X1$ F3 \mu2 \mu3 $X3X5X2$ \mu2 \mu3 $X3X5X2$ F4 \mu4 $X3X5$ \mu4 $X3X5$ F5 \mu5 $X5P(x_{5})$
```
=
```text
P $x_{1}$,$x_{2}$,$x_{3}$,$x_{4}$,$x_{6}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})P(x_{4}|x_{2})P(x_{5}|x_{3})P(x_{6}|x_{2}, x_{5})$
```
=
```text
P $x_{1}$,$x_{2}$,$x_{3}$,$x_{6}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})P(x_{5}|x_{3})P(x_{6}|x_{2}, x_{5})$ P $x_{4}P(x_{4}|x_{2})$ | {z } $F1(x_{2},x_{4})$
```
=
```text
P $x_{1}$,$x_{2}$,$x_{3}$,$x_{6}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})P(x_{5}|x_{3})P(x_{6}|x_{2}, x_{5})$ \mu1($x_{2}$)
```
=
```text
P $x_{1}$,$x_{2}$,$x_{3}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})P(x_{5}|x_{3})$ \mu1($x_{2}$) P $x_{6}P(x_{6}|x_{2}, x_{5})$ | {z } $F2(x_{2},x_{5},x_{6})$
```
=
```text
P $x_{1}$,$x_{2}$,$x_{3}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})P(x_{5}|x_{3})$ \mu1($x_{2}$) \mu2($x_{2}$, $x_{5}$)
```
=
```text
P $x_{2}$,$x_{3}P(x_{5}|x_{3})$ \mu1($x_{2}$) \mu2($x_{2}$, $x_{5}$) P $x_{1}P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1})$ | {z } $F3(x_{1},x_{2},x_{3})$
```
=
```text
P $x_{2}$,$x_{3}P(x_{5}|x_{3})$ \mu1($x_{2}$) \mu2($x_{2}$, $x_{5}$) \mu3($x_{2}$, $x_{3}$)
```
=
```text
P $x_{3}P(x_{5}|x_{3})$ P $x_{2}$ \mu1($x_{2}$) \mu2($x_{2}$, $x_{5}$) \mu3($x_{2}$, $x_{3}$) | {z } $F4(x_{2},x_{3},x_{5})$
```
=
```text
P $x_{3}P(x_{5}|x_{3})$ \mu4($x_{3}$, $x_{5}$)
```
=
```text
P $x_{3}P(x_{5}|x_{3})$ \mu4($x_{3}$, $x_{5}$) | {z } $F5(x_{3},x_{5})$
```
= \mu5(x_{5})
```text
9:24

<!-- page: 135 -->
### Variable Elimination example – lessons learnt

- There is a dynamic programming principle behind Variable Elimination:

  - For eliminating $X5$,4,6 we use the solution of eliminating $X4$,6

  - The “sub-problems” are represented by the F terms, their solutions by the remaining
\mu terms

  - We’ll continue to discuss this 4 slides later!

- The factorization of the joint

  - determines in which order Variable Elimination is efficient

  - determines what the terms $F(...)$ and \mu(...) depend on

- We can automate Variable Elimination. For the automation, all that matters is the factorization of the joint.

9:25

### Factor graphs

- In the previous slides we introduces the box notation to indicate terms that depend on some variables. That’s exactly what factor graphs represent.

- A Factor graph is a

  - bipartite graph

  - where each circle node represents a random variable Xi

  - each box node represents a factor fk, which is a function $fk(X\partialk)$

  - the joint probability distribution is given as
$P(X_{1:n})$ =
K
Y
k=1
$fk(X\partialk)$
Notation: \partial k is shorthand for $Neighbors(k)$

9:26
```
Bayes Net \to factor graph
```text
- Bayesian Network: $X6X3X5X4X2X1$

<!-- page: 136 -->
```
P(x_{1:6}) = P(x_{1}) P(x_{2}|x_{1}) P(x_{3}|x_{1}) P(x_{4}|x_{2}) P(x_{5}|x_{3}) P(x_{6}|x_{2}, x_{5})
```text
- Factor Graph: $X6X3X5X4X2X1P(x_{1}:6)$ = $f1(x_{1}, x_{2})f2(x_{3}, x_{1})f3(x_{2}, x_{4})f4(x_{3}, x_{5})f5(x_{2}, x_{5}, x_{6})$ \to  each CPT in the Bayes Net is just a factor (we neglect the special semantics of a CPT)

9:27

### Variable Elimination Algorithm

![Hinh: fig-136-1]

- eliminate single $variable(F, i)$ 1: Input: list F of factors, variable id i 2: Output: list F of factors 3: find relevant subset F̂ ⊆ F of factors coupled to i: F̂ = {k : i $\in$ \partial k} 4: create new factor k̂ with neighborhood \partial k̂ = all variables in F̂ except i 5: compute \mu_k̂(X\partial k̂) = P Xi Q k$\in$F̂ $fk(X\partialk)$ 6: remove old factors F̂ and append new factor \mu_k̂ to F 7: return F

- elimination $algorithm(F, M)$ 1: Input: list F of factors, tuple M of desired output variables ids 2: Output: single factor \mu over variables XM 3: define all variables present in F: V = $vars(F)$ 4: define variables to be eliminated: E = V \ M 5: for all i $\in$ E: eliminate single $variable(F, i)$ 6: for all remaining factors, compute the product \mu = Q f$\in$F f 7: return \mu

9:28

### Variable Elimination on trees

<!-- page: 137 -->
3 2 1 4 5 6 7 X $Y4Y5Y6Y7Y8Y2Y3Y1F3(Y3,4,5, X)F1(Y1,8, X)F2(Y2,6,7, X)$ The subtrees w.r.t. X can be described as
```
F1(Y1,8, X) = f1(Y8, Y1) f2(Y1, X) F2(Y2,6,7, X) = f3(X, Y2) f4(Y2, Y6) f5(Y2, Y7) F3(Y3,4,5, X) = f6(X, Y3, Y4) f7(Y4, Y5)
$$

The joint distribution is:

$$
P(Y_{1:8}, X) = F1(Y1,8, X) F2(Y2,6,7, X) F3(Y3,4,5, X)
```text
9:29

### Variable Elimination on trees

![Hinh: fig-137-1]

![Hinh: fig-137-2]

1 3 2 4 5 6 7 8
```
\mu3\toX \mu2\toX \mu6\toX
```text
$Y9$ X $Y4Y5Y6Y7Y8Y2Y3Y1F3(Y3,4,5, X)F1(Y1,8, X)F2(Y2,6,7, X)$ We can eliminate each tree independently. The remaining terms (messages) are:
```
\muF1\toX(X) =
```text
P $Y1$,8 $F1(Y1,8, X)$
```
\muF2\toX(X) =
```text
P $Y2$,6,7 $F2(Y2,6,7, X)$
```
\muF3\toX(X) =
```text
P $Y3$,4,5 $F3(Y3,4,5, X)$ The marginal $P(X)$ is the product of subtree messages
```
P(X) = \muF1\toX(X) \muF2\toX(X) \muF3\toX(X)
```text
9:30

### Variable Elimination on trees – lessons learnt

<!-- page: 138 -->
- The “remaining terms” \mu’s are called messages Intuitively, messages subsume information from a subtree

- Marginal = product of messages, $P(X)$ = Q k \muFk\to X, is very intuitive:

  - Fusion of independent information from the different subtrees

  - Fusing independent information \leftrightarrow  multiplying probability tables

- Along a (sub-) tree, messages can be computed recursively

9:31

### Message passing

![Hinh: fig-138-1]

![Hinh: fig-138-2]

- General equations (belief propagation (BP)) for recursive message computation (writing \mu_k\to $i(Xi)$ instead of \muFk\to $X(X)$): \mu_k\to $i(Xi)$ = X X\partial k\i $fk(X\partialk)$ Y j$\in$\partial k\i \mūj\to $k(Xj )$ z }| { Y k0$\in$\partial j\k \mu_k0\to $j(Xj)$ | {z } F (subtree) Q j$\in$\partial k\i: branching at factor k, prod. over adjacent variables j excl. i Q k0$\in$\partial j\k: branching at variable j, prod. over adjacent factors k0 excl. k \mūj\to $k(Xj)$ are called “variable-to-factor messages”: store them for efficiency 1 3 2 4 5 6 7 8 \mu3\to X \mu2\to X \mu1\to $Y1$ \mu4\to $Y2$ \mu5\to $Y2$ \mu7\to $Y4$ \mu6\to X \mu8\to $Y4Y9$ X $Y4Y5Y6Y7Y8Y2Y3Y1F3(Y3,4,5, X)F1(Y1,8, X)F2(Y2,6,7, X)$ Example messages: \mu2\to X = P $Y1f2(Y1, X)$ \mu1\to $Y1$ ($Y1$) \mu6\to X = P $Y3$,$Y4f6(Y3, Y4, X)$ \mu7\to $Y4$ ($Y4$) \mu8\to $Y4$ ($Y4$) \mu3\to X = P $Y2f3(Y2, X)$ \mu4\to $Y2$ ($Y2$) \mu5\to $Y2$ ($Y2$)

9:32

### Constraint propagation is ’boolean’ message passing

- Assume all factors are binary \to  boolean constraint functions as for CSP

- All messages are binary vectors

- The product of incoming messages indicates the variable’s remaining domain Di (analogous to the marginal $P(Xi)$)

- The message passing equations do constraint propagation

9:33

<!-- page: 139 -->
### Message passing remarks

- Computing these messages recursively on a tree does nothing else than Variable Elimination $\Rightarrow P(Xi)$ = Q k$\in$\partial i \mu_k\to $i(Xi)$ is the correct posterior marginal

- However, since it stores all “intermediate terms”, we can compute ANY marginal $P(Xi)$ for any i

- Message passing exemplifies how to exploit the factorization structure of the joint distribution for the algorithmic implementation

- Note: These are recursive equations. They can be resolved exactly if and only if the dependency structure (factor graph) is a tree. If the factor graph had loops, this would be a “loopy recursive equation system”...

9:34

### Message passing variants

- Message passing has many important applications:

  - Many models are actually trees: In particular chains esp. Hidden Markov Models

  - Message passing can also be applied on non-trees (\leftrightarrow  loopy graphs) \to  approximate
inference (Loopy Belief Propagation)

  - Bayesian Networks can be “squeezed” to become trees \to  exact inference in Bayes
Nets! (Junction Tree Algorithm)

9:35

### Loopy Belief Propagation

- If the graphical model is not a tree (=has loops):

  - The recursive message equations cannot be resolved.

  - However, we could try to just iterate them as update equations...

- Loopy BP update equations: (initialize with \mu_k\to i = 1) \munew k\to $i(Xi)$ = X X\partial k\i $fk(X\partialk)$ Y j$\in$\partial k\i Y k0$\in$\partial j\k \muold k0\to $j(Xj)$

9:36

<!-- page: 140 -->
### Loopy BP remarks

![Hinh: fig-140-1]

- Problem of loops intuitively: loops $\Rightarrow$ branches of a node to not represent independent information!

  - BP is multiplying (=fusing) messages from dependent sources of information

- No convergence guarantee, but if it converges, then to a state of marginal consistency X X\partial k\i $b(X\partialk)$ = X X\partial k0\i $b(X\partialk0 )$ = $b(Xi)$ and to the minimum of the Bethe approximation of the free energy (Yedidia, Freeman, & Weiss, 2001)

- We shouldn’t be overly disappointed:

  - if BP was exact on loopy graphs we could efficiently solve NP hard problems...

  - loopy BP is a very interesting approximation to solving an NP hard problem

- Ways to tackle the problems with BP convergence:

  - Damping (Heskes, 2004: On the uniqueness of loopy belief propagation fixed points)

  - CCCP (Yuille, 2002: CCCP algorithms to minimize the Bethe and Kikuchi free energies: Convergent
alternatives to belief propagation)

  - Tree-reweighted MP (Kolmogorov, 2006: Convergent tree-reweighted message passing for energy
minimization)

9:37

### Junction Tree Algorithm**

- Many models have loops Instead of applying loopy BP in the hope of getting a good approximation, it is possible to convert every model into a tree by redefinition of RVs. The Junction Tree Algorithms converts a loopy model into a tree.

- Loops are resolved by defining larger variable groups (separators) on which messages are defined

9:38

### Junction Tree Example

- Example: A B C D A B C D

<!-- page: 141 -->
- Join variable B and C to a single separator D B, C A This can be viewed as a variable substitution: rename the tuple (B, C) as a single random variable

- A single random variable may be part of multiple separators – but only along a running intersection

9:39

### Junction Tree Algorithm

![Hinh: fig-141-1]

- Standard formulation: Moralization & Triangulation A clique is a fully connected subset of nodes in a graph. 1) Generate the factor graph (classically called “moralization”) 2) Translate each factor to a clique: Generate the undirected graph where undirected edges connect all RVs of a factor 3) Triangulate the undirected graph. (This is the critical step!) 4) Translate each clique back to a factor; identify the separators between factors

- Formulation in terms of variable elimination for a given variable order: 1) Start with a factor graph 2) Choose an order of variable elimination (This is decided implicitly by trangulation above) 3) Keep track of the “remaining \mu terms” (slide 14): which RVs would they depend on? \to  this identifies the separators

9:40

### Junction Tree Algorithm Example

<!-- page: 142 -->
$X6X3X5X4X2X1X2$,3 $X2$,5 $X6X4X1$

- If we eliminate in order 4, 6, 5, 1, 2, 3, we get remaining terms ($X2$), ($X2$, $X5$), ($X2$, $X3$), ($X2$, $X3$), ($X3$) which translates to the Junction Tree on the right

9:41

### Maximum a-posteriori (MAP) inference

![Hinh: fig-142-1]

- Often we want to compute the most likely global assignment XMAP 1:n = argmax $X1$:n $P(X_{1:n})$ of all random variables. This is called MAP inference and can be solved by replacing all P by max in the message passing equations – the algorithm is called Max-Product Algorithm and is a generalization of Dynamic Programming methods like Viterbi or Dijkstra.

- Application: Conditional Random Fields $f(y, x)$ = φ(y, x)> β = k X j=1 φ$j(y\partialj, x)$βj = log h k Y j=1 eφj (y\partial j ,x)βj i with prediction x 7\to  y∗ (x) = argmax y $f(x, y)$ Finding the argmax is a MAP inference problem! This is frequently needed in the innerloop of CRF learning algorithms.

9:42

### Conditional Random Fields**

- The following are interchangable: “Random Field” \leftrightarrow  “Markov Random Field” \leftrightarrow  Factor Graph

- Therefore, a CRF is a conditional factor graph:

  - A CRF defines a mapping from input x to a factor graph over y

<!-- page: 143 -->
  - Each feature φ$j(y\partialj, x)$ depends only on a subset \partial j of variables y\partial j

  - If y\partial j are discrete, a feature φ$j(y\partialj, x)$ is usually an indicator feature (see lecture 03);
the corresponding parameter βj is then one entry of a factor $fk(y\partialj)$ that couples
these variables

9:43

### Sampling

- Read: Andrieu et al: An Introduction to MCMC for Machine Learning (Machine Learning, 2003)

- Here I’ll discuss only thee basic methods:

  - Rejection sampling

  - Importance sampling

  - Gibbs sampling

9:44

### Monte Carlo methods

- General, the term Monte Carlo simulation refers to methods that generate many i.i.d. random samples xi ∼ $P(x)$ from a distribution $P(x)$. Using the samples one can estimate expectations of anything that depends on x, e.g. $f(x)$: hfi = Z x $P(x)f(x)$ dx ≈ 1 N N X i=1 $f(x_i)$ (In this view, Monte Carlo approximates an integral.)

- Example: What is the probability that a solitair would come out successful? (Original story by Stan Ulam.) Instead of trying to analytically compute this, generate many random solitairs and count.

- The method developed in the 40ies, where computers became faster. Fermi, Ulam and von Neumann initiated the idea. von Neumann called it “Monte Carlo” as a code name.

9:45

### Rejection Sampling

- We have a Bayesian Network with RVs $X1$:n, some of which are observed: Xobs = yobs, obs ⊂ {1 : n}

<!-- page: 144 -->
- The goal is to compute marginal posteriors $P(Xi | Xobs = yobs)$ conditioned on the observations.

- We generate a set of K (joint) samples of all variables S = {xk 1:n}K k=1 Each sample xk 1:n = (xk 1, xk 2, .., xk n) is a list of instantiation of all RVs.

9:46

### Rejection Sampling

- To generate a single sample xk 1:n: 1. Sort all RVs in topological order; start with i = 1 2. Sample a value xk i ∼ P(Xi | xk $Parents(i)$) for the ith RV conditional to the previous samples xk 1:i-1 3. If i $\in$ obs compare the sampled value xk i with the observation yi. Reject and repeat from a) if the sample is not equal to the observation. 4. Repeat with i ← i + 1 from 2.

- We compute the marginal probabilities from the sample set S: $P(Xi =x | Xobs = yobs)$ ≈ $countS(x_k i = x)$ K or pair-wise marginals: $P(Xi =x, Xj =x_{0} | Xobs = yobs)$ ≈ $countS(x_k i = x \land x_k j = x_{0} )$ K

9:47

### Importance Sampling (with likelihood weighting)

- Rejecting whole samples may become very inefficient in large Bayes Nets!

- New strategy: We generate a weighted sample set S = {(xk 1:n, wk )}K k=1 where each sample xk 1:n is associated with a weight wk

- In our case, we will choose the weights proportional to the likelihood $P(Xobs = yobs | X_{1:n} =x_k 1:n)$ of the observations conditional to the sample xk 1:n

9:48

<!-- page: 145 -->
### Importance Sampling

- To generate a single sample (wk , xk 1:n): 1. Sort all RVs in topological order; start with i = 1 and wk = 1 2. a) If i 6$\in$ obs, sample a value xk i ∼ P(Xi | xk $Parents(i)$) for the ith RV conditional to the previous samples xk 1:i-1 b) If i $\in$ obs, set the value xk i = yi and update the weight according to likelihood wk ← wk $P(Xi =y_i | x_k 1:i-1)$ 3. Repeat with i ← i + 1 from 2.

- We compute the marginal probabilities as: $P(Xi =x | Xobs = yobs)$ ≈ PK k=1 wk [xk i = x] PK k=1 wk and likewise pair-wise marginals, etc. Notation: [expr] = 1 if expr is true and zero otherwise

9:49

### Gibbs Sampling**

- In Gibbs sampling we also generate a sample set S – but in this case the samples are not independent from each other. The next sample “modifies” the previous one:

- First, all observed RVs are clamped to their fixed value xk i = yi for any k.

- To generate the (k + 1)th sample, iterate through the latent variables i 6$\in$ obs, updating: xk+1 i ∼ $P(Xi | x_k 1:n\i)$ ∼ $P(Xi | x_k 1, x_k 2, .., x_k i-1, x_k i+1, .., x_k n)$ ∼ P(Xi | xk $Parents(i)$) Y j:i$\in
```Parents(j)$ P(Xj =xk j | Xi, xk $Parents(j)$\i) That is, each xk+1 i is resampled conditional to the other (neighboring) current sample values.

9:50

### Gibbs Sampling**

- As for rejection sampling, Gibbs sampling generates an unweighted sample set S which can directly be used to compute marginals. In practice, one often discards an initial set of samples (burn-in) to avoid starting biases.

<!-- page: 146 -->
- Gibbs sampling is a special case of MCMC sampling. Roughly, MCMC means to invent a sampling process, where the next sample may stochastically depend on the previous (Markov property), such that the final sample set is guaranteed to correspond to $P(X_{1:n})$. \to  An Introduction to MCMC for Machine Learning

9:51

### Sampling – conclusions

- Sampling algorithms are very simple, very general and very popular

  - they equally work for continuous & discrete RVs

  - one only needs to ensure/implement the ability to sample from conditional distri-
butions, no further algebraic manipulations

  - MCMC theory can reduce required number of samples

- In many cases exact and more efficient approximate inference is possible by actually computing/manipulating whole distributions in the algorithms instead of only samples.

9:52

### What we didn’t cover

- A very promising line of research is solving inference problems using mathematical programming. This unifies research in the areas of optimization, mathematical programming and probabilistic inference. Linear Programming relaxations of MAP inference and CCCP methods are great examples.

9:53

<!-- page: 147 -->
# 10 Dynamic Models

![Hinh: fig-147-1]

![Hinh: fig-147-2]

### Motivation & Outline

This lecture covors a special case of graphical models for dynamic processes, where the graph is roughly a chain. Such models are called Markov processes, or hidden Markov model when the random variable of the dynamic process is not observable. These models are a cornerstone of time series analysis, as well as for temporal models for language, for instance. A special case of inference in the continuous case is the Kalman filter, which can be use to tracking objects or the state of controlled system.

### Markov processes (Markov chains)

Markov assumption: Xt depends on bounded subset of $X0$:t-1

$$
First-order Markov process: P(Xt | X_{0:t}-1) = P(Xt | Xt-1) Second-order Markov process: P(Xt | X_{0:t}-1) = P(Xt | Xt-2, Xt-1) Sensor Markov assumption: P(Yt | X_{0:t}, Y_{0:t}-1) = P(Yt | Xt)
$$

Stationary process: transition model $P(Xt | Xt-1)$ and sensor model $P(Yt | Xt)$ fixed for all t

10:1

### Hidden Markov Models

- We assume we have

  - observed (discrete or continuous) variables Yt in each time slice

  - a discrete latent variable Xt in each time slice

  - some observation model $P(Yt | Xt; \theta)$

  - some transition model $P(Xt | Xt-1; \theta)$

- A Hidden Markov Model (HMM) is defined as the joint distribution $P(X0:T , Y0:T )$ = $P(X0)$ · T Y t=1 $P(Xt|Xt-1)$ · T Y t=0 $P(Yt|Xt)$ .

<!-- page: 148 -->
$X0X1X2X3Y0Y1Y2Y3$ YT XT

10:2

### Different inference problems in Markov Models

![Hinh: fig-148-1]

![Hinh: fig-148-2]

- $P(xt | y_{0}:T )$ marginal posterior

- $P(xt | y_{0}:t)$ filtering

- $P(xt | y_{0}:a)$, t > a prediction

- $P(xt | y_{0}:b)$, t < b smoothing

- $P(y_{0}:T )$ likelihood calculation

- Viterbi alignment: Find sequence x∗ 0:T that maximizes $P(x_{0}:T | y_{0}:T )$ (This is done using max-product, instead of sum-product message passing.)

10:3

### Inference in an HMM – a tree!

$X0X1X2X3Y0Y1Y2Y3$ YT XT $Fnow(X2, Y2)Ffuture(X2:T , Y3:T )Fpast(X0:2, Y0:1)$

- The marginal posterior $P(Xt | Y1:T )$ is the product of three messages $P(Xt | Y1:T )$ \propto  $P(Xt, Y1:T )$ = \mupast |{z} α (Xt) \munow |{z} % (Xt) \mufuture | {z } β (Xt)

- For all a < t and b > t

  - Xa conditionally independent from Xb given Xt

  - Ya conditionally independent from Yb given Xt

<!-- page: 149 -->
“The future is independent of the past given the present”

### Markov property

(conditioning on Yt does not yield any conditional independences)

10:4

### Inference in HMMs

$X0X1X2X3Y0Y1Y2Y3$ YT XT $Fnow(X2, Y2)Ffuture(X2:T , Y3:T )Fpast(X0:2, Y0:1)$ Applying the general message passing equations:

```text
forward msg. \mu_{X_t}-1\toXt (xt) =: \alpha_t(xt) =
```

X xt-1 $P(xt|xt-1)$ αt-1(xt-1) %t-1(xt-1)

```text
\alpha0(x_{0}) = P(x_{0}) backward msg. \mu_{X_t}+1\toXt (xt) =: \beta_t(xt) =
```

X xt+1 $P(xt+1|xt)$ βt+1(xt+1) %t+1(xt+1)

```text
\beta_T (xT ) = 1 observation msg. \muYt\toXt (xt) =: %t(xt) = P(yt | xt)
```

posterior marginal $q(xt)$ \propto  α$t(xt)$ %$t(xt)$ β$t(xt)$ posterior marginal $q(xt, xt+1)$ \propto  α$t(xt)$ %$t(xt)P(xt+1|xt)$ %t+1(xt+1) βt+1(xt+1)

10:5

### Inference in HMMs – implementation notes

- The message passing equations can be implemented by reinterpreting them as matrix equations: Let αt, βt, %t be the vectors corresponding to the probability tables α$t(xt)$, β$t(xt)$, %$t(xt)$; and let P be the matrix with enties $P(xt | xt-1)$. Then 1: α0 = π, βT = 1 2: fort=1:T -1 : αt = P (αt-1 ◦ %t-1) 3: fort=T -1:0 : βt = P> (βt+1 ◦ %t+1) 4: fort=0:T : qt = αt ◦ %t ◦ βt 5: fort=0:T -1 : Qt = P ◦ [(βt+1 ◦ %t+1) (αt ◦ %t)>] where ◦ is the element-wise product! Here, qt is the vector with entries $q(xt)$, and Qt the matrix with entries $q(xt+1, xt)$. Note that the equation for Qt describes $Qt(x_{0} , x)$ = $P(x_{0} |x)$[(βt+1($x_{0}$ )%t+1($x_{0}$ ))(α$t(x)$%$t(x)$)].

10:6

<!-- page: 150 -->
### Inference in HMMs: classical derivation

Given our knowledge of Belief propagation, inference in HMMs is simple. For reference, here is a more classical derivation:

$$
P(xt | y_{0:T} ) =
$$

$P(y_{0}:T | xt)P(xt)P(y_{0}:T )$

$$
=
$$

$P(y_{0}:t | xt)P(yt+1:T | xt)P(xt)P(y_{0}:T )$

$$
=
$$

$P(y_{0}:t, xt)P(yt+1:T | xt)P(y_{0}:T )$

$$
=
$$

α$t(xt)$ β$t(xt)P(y_{0}:T )$

$$
\alpha_t(xt) := P(y_{0:t}, xt) = P(yt|xt) P(y_{0:t}-1, xt) = P(yt|xt)
$$

X xt-1 $P(xt | xt-1)$ αt-1(xt-1)

$$
\beta_t(xt) := P(yt+1:T | xt) =
$$

X xt+1 $P(yt+1:T | xt+1)P(xt+1 | xt)$

$$
=
$$

X xt+1 h βt+1(xt+1) $P(yt+1|xt+1)$ i $P(xt+1 | xt)$ Note: αt here is the same as αt ◦ %t on all other slides!

10:7

### HMM remarks

- The computation of forward and backward messages along the Markov chain is also called forward-backward algorithm

- Sometimes, computing forward and backward messages (in disrete or continuous context) is also called Bayesian filtering/smoothing

- The EM algorithm to learn the HMM parameters is also called Baum-Welch

### algorithm

- If the latent variable xt is continuous xt $\in$ Rd instead of discrete, then such a Markov model is also called state space model.

- If the continuous transitions and observations are linear Gaussian $P(xt+1|xt)$ = $N(xt+1 | Axt + a, Q)$ , $P(yt|xt)$ = $N(yt | Cxt + c, W)$ then the forward and backward messages αt and βt are also Gaussian. \to  forward filtering is also called Kalman filtering \to  smoothing is also called Kalman smoothing

10:8

<!-- page: 151 -->
### Kalman Filter example

![Hinh: fig-151-1]

![Hinh: fig-151-2]

- filtering of a position (x, y) $\in$ R2 :

10:9

### Kalman Filter example

- smoothing of a position (x, y) $\in$ R2 :

10:10

<!-- page: 152 -->
### HMM example: Learning Bach

![Hinh: fig-152-1]

![Hinh: fig-152-2]

- A machine “listens” (reads notes of) Bach pieces over and over again \to  It’s supposed to learn how to write Bach pieces itself (or at least harmonize them).

- Harmonizing Chorales in the Style of J S Bach Moray Allan & Chris Williams (NIPS 2004)

- use an HMM

  - observed sequence $Y0$:T Soprano melody

  - latent sequence $X0$:T chord & and harmony:

10:11

### HMM example: Learning Bach

- results: http://www.anc.inf.ed.ac.uk/demos/hmmbach/

- See also work by Gerhard Widmer http://www.cp.jku.at/people/widmer/

10:12

### Dynamic Bayesian Networks

  - Arbitrary BNs in each time slide

  - Special case: MDPs, speech, etc

<!-- page: 153 -->
10:13

<!-- page: 154 -->
# 11 AI & Machine Learning & Neural Nets

### Motivation & Outline

Neural networks became a central topic for Machine Learning and AI. But in principle, they’re just parameterized functions that can be fit to data. They lack many appealing aspects that were the focus of ML research in the ’90-’10. So why are they so successful now? This lecture introduces the basics and tries to discuss the success of NNs.

### What is AI?

- AI is a research field

- AI research is about systems that take decisions

  - AI formalizes decision processes: interactive (decisions change world state), or pas-
sive

  - AI distinguishes between $agent(s)$ and the external world: decision variables

- ... systems that take optimal/desirable decisions

  - AI formalizes decision objectives

  - AI aims for systems to exhibit functionally desirable behavior

- ... systems that take optimal decisions on the basis of all available information

  - AI is about inference

  - AI is about learning

11:1

### What is Machine Learning?

- In large parts, ML is: (let’s call this ML0 ) Fitting a function f : x 7\to  y to given data D = {(xi, yi)}n i=1

- And what does that have to do with AI?

- Literally, not much:

  - The decision made by a ML0
method is only a single decision: Decide on the func-
tion f $\in$ H in the hypothesis space H

  - This “single-decision process” is not interactive; ML0
does not formalize/model/consider
how the choice of f changes the world

  - The objective $L(f, D)$ in ML0
depends only on the given static data D and the de-
cision f, not how f might change the world

  - “Learning” in ML0
is not an interactive process, but some method to pick f on the
basis of the static D. The typically iterative optimization process is not the decision
process that ML0
focusses on.

11:2

<!-- page: 155 -->
But, function approximation can be used to help solving AI (interactive decision process) problems:

- Building a trained/fixed f into an interacting system based on human expert knowledge: An engineer trains a NN f to recognize street signs based on a large fixed data set D. S/he builds f into a car to drive autonomously. That car certainly solves an AI problem; f continuously makes decisions that change the state of the world. But f was never optimized literally for the task of interacting with the world; it was only optimized to minimze a loss on the static data D. It is not a priori clear that minimizing the loss of f on D is related to maximizing rewards in car driving. That fact is only the expertise of the engineer; it is not some AI algorithm that discovered that fact. At no place there was an AI method that “learns to drive a car”. There was only an optimization method to minimize the loss of f on D.

- Using ML in interactive decision processes: To approximate a Q-function, state evaluation function, reward function, the system dynamics, etc. Then, other AI methods can use these approximate models to actually take decisions in the interactive context.

11:3

What is Machine Learning? (beyond ML0 )

- In large parts, ML is: (let’s call this ML0 ) Fitting a function f : x 7\to  y to given data D = {(xi, yi)}n i=1 Beyond ML0 :

- Fitting more structured models to data, which includes

  - Time series, recurrent processes

  - Graphical Models

  - Unsupervised learning (semi-supervised learning)
...but in all these cases, the scenario is still not interactive, the data D is static, the de-
cision is about picking a single model f from a hypothesis space, and the objective is a
loss based on f and D only.

- Active Learning, where the “ML agent” makes decisions about what data label to query next

- Bandits, Reinforcement Learning

11:4

ML0 objective: Empirical Risk Minimization

- We have a hypothesis space H of functions f : x 7\to  y In a standard parameteric case H = {fθ | θ $\in$ Rn } are functions fθ : x 7\to  y that are described by n parameters θ $\in$ Rn

<!-- page: 156 -->
- Given data D = {(xi, yi)}n i=1, the standard objective is to minimize the “error” on the data $f^*$ argmin f$\in$H n X i=1 `($f(x_i)$, yi) , where `(ŷ, y) > 0 penalizes a discrepancy between a model output ŷ and the data y.

  - Squared error `(ŷ, y) = (ŷ - y)2

  - Classification error `(ŷ, y) = [ŷ 6= y]

  - neg-log likelihood `(ŷ, y) = - log $p(y | ŷ)$

  - etc

11:5

### What is a Neural Network?

![Hinh: fig-156-1]

- A parameterized function fθ : x 7\to  y

  - θ are called weights

  - minθ
Pn
i=1 `(fθ(xi), yi) is called training

11:6

### What is a Neural Network?

- Standard fwd-forward NN Rh0 7\to  RhL with L layers: 1-layer fθ(x) = W0x θ = (W0), W0 $\in$ Rh1×h0 2-layer fθ(x) = W1σ(W0x) θ = (W1, W0), Wi $\in$ Rhi+1×hi 3-layer fθ(x) = W2σ(W1σ(W0x)) θ = (W3, W2, W0)

- The activation function σ(z) is applied element-wise rectified linear unit (ReLU) σ(z) = z[z $\geq$ 0] leaky ReLU σ(z) = ( 0.01z z < 0 z z $\geq$ 0 sigmoid, logistic σ(z) = 1/(1 + e-z ) tanh σ(z) = $tanh(z)$

11:7

### Neural Networks: Basic Equations

- Consider L layers (hidden plus output), each hl-dimensional

  - let zl = Wl-1xl-1 $\in$ Rhl be the inputs to all neurons in layer l

  - let xl = σ(zl) $\in$ Rhl be the activation of all neurons in layer l

  - redundantly, we denote by $x_{0}$ ≡ x

- Forward propagation: An L-layer NN recursively computes, \forall l=1,..,L-1 : zl = Wl-1xl-1 , xl = σ(zl) and then computes the output f ≡ zL = WLxL

<!-- page: 157 -->
- Backpropagation: Given some loss `(f), let δL \Delta = \partial ` \partial f = \partial ` \partial zL . We can recursivly compute the loss-gradient w.r.t. the inputs of layer l: \forall l=L-1,..,1 : δl \Delta = d` dzl = d` dzl+1 \partial zl+1 \partial xl \partial xl \partial zl = [δl+1 Wl] ◦ [σ0 (zl)]> where ◦ is an element-wise product. The gradient w.r.t. weights is: d` dWl,ij = d` dzl+1,i \partial zl+1,i \partial Wl,ij = δl+1,i xl,j or d` dWl = δ> l+1x> l

11:8

### Behavior of Gradient Propagation

- Propagating δl back through many layers can lead to problems

- For the classical sigmoid σ(z), σ(z)0 is always < 1 $\Rightarrow$ vanishing gradient Modern activations functions (ReLU) reduce this problem

- The Initialization of weights is super important! E.g., initialize weights in Wl with standard deviation 1 \sqrt hl . Roughly: If each element of zl has standard deviation , the same should be true for zl+1.

11:9

### NN regression & regularization

- In the standard regression case, hL = 1, we typically assume a squared error loss `(f) = P i(fθ(xi) - yi)2 . We have δL = X i 2(fθ(xi) - yi)>

- Regularization:

  - Old: Add a L2 or L1 regularization. First compute all gradients as before, then add
λWl,ij (for L2), or λ sign Wl,ij (for L1) to the gradient. Historically, this is called
weight decay, as the additional gradient leads to a step decaying the weighs.

  - Modern: Dropout

- The optimal output weights are as for standard regression W∗ L-1 = (X> X + λI)-1 X> y where X is the data matrix of activations xL-1 ≡ φ(x)

11:10

<!-- page: 158 -->
### NN classification

![Hinh: fig-158-1]

- In the multi-class case we have hL = M output neurons, one for each class. The function $f(x)\in$ Rm is the discriminative function, which means that the predicted class is the argmaxy$\in${1,..,M}[fθ(x)]y.

- Choosing neg-log-likelihood objective \leftrightarrow  logistic regression

- Choosing hinge loss objective \leftrightarrow  “NN + SVM”..

  - Let y∗
be the correct class and let’s use the short notation fy = [fθ(x)]y for the
discriminative value for class y

  - The one-vs-all hinge loss is
P
$y_{6}$=y∗ [1 - (fy∗ - fy)]+

  - For output neuron y 6= y∗
this implies a gradient δy = [fy∗ < fy + 1]

  - For output neuron y∗
this implies a gradient δy∗ = -
P
$y_{6}$=y∗ [fy∗ < fy + 1]
Only data points inside the margin induce an error (and gradient).

  - This is also called Perceptron Algorithm

11:11

Discussion: Why are NNs so successful now?

11:12

### Historical Perspective

(This is completely subjective.)

- Early (from 40ies):

  - McCulloch Pitts, Hebbian learning, Rosenblatt, Werbos (backpropagation)

- 80ies:

  - Start of connectionism, NIPS

  - ML wants to distinguish itself from pure statistics (“machines”, “agents”)

- ’90-’10:

  - More theory, better grounded, Statistical Learning theory

  - Good ML is pure statistics (again) (Frequentists, SVM)

  - ...or pure Bayesian (Graphical Models, Bayesian X)

  - sample-efficiency, great generalization, guarantees, theory

  - Great successes, in applications across disciplines; supervised, unsupervised, struc-
tured

- ’10-:

  - Big Data. NNs. Size matters. GPUs.

  - Disproportionate focus on images

  - Software engineering becomes central

11:13

<!-- page: 159 -->
- NNs did not become “better” than they were 20y ago. By the standards of ’90-’10, they would still be horrible. What changed is the standards by which they’re are evaluated: Old:

  - Sample efficiency & generalization; get the most from little data

  - Guarantees (both, w.r.t. generalization and optimization)

  - Being only as good as a nearest neighbor methods is embarrasing
New:

  - Ability to cope with billions of samples \to  no batch processing, but stochastic opti-
mization

  - Happy to end up in some local optimum. (Theory on “every local optimum of a
large deep net is good”.)

  - Stochastic optimization methods (ADAM) without monotone convergence

  - Nobody compares to nearest neighbor methods – nearest neighbor on 1B data points
is too expensive anyway. I guess that it’d perform very well (for a descent kernel)
and a NN could be glad to perform equally well

11:14

### NNs vs. nearest neighbor

- Imagine an autonomous car. Instead of carrying a neural net, it carries 1 Petabyte of data (500 hard drives, several billion pictures). In every split second it records an image from a camera and wants to query the database to returen the 100 most similar pictures. Perhaps with a non-trivial similarity metric. That’s not reasonable!

- In that sense, NNs are much better than nearest neighbor. They store/compress/memo huge amounts of data. Whether they actually generalize better than a good nearest neighbor methods is not so relevant.

- That’s how the standards changed from ’90-’10 to nowadays

11:15

### Images & Time Series

- I’d guess, 90% of the recent success of NNs is in the areas of images or time series

- For images, convolutional NNs (CNNs) impose a very sensible prior; the representations that emerge in CNNs are in fact similar to representations in the visual area of our brain.

- For time series, long-short term memory (LSTM) networks represent long-term dependencies in a way that is well trainable – something that is hard to do with other model structures.

- Both these structural priors, combined with huge data and capacity, make these methods very strong.

11:16

<!-- page: 160 -->
### Convolutional NNs

![Hinh: fig-160-1]

![Hinh: fig-160-2]

- Standard fully connected layer: full matrix Wi has hihi+1 parameters

- Convolutional: Each neuron (entry of zi+1) receives input from a square receptive field, with k × k parameters. All neurons share these parameters \to  translation invariance. The whole layer only has k2 parameters.

- There are often multiple neurons with the same receitive field (“depth” of the layer), to represent different “filters”. Stride leads to downsampling. Padding at borders.

- Pooling applies a predefined operation on the receptive field (no parameters): max or average. Typically for downsampling.

11:17

Learning to read these diagrams... AlexNet

11:18

ResNet

11:19

<!-- page: 161 -->
ResNeXt

11:20

### Pretrained networks

![Hinh: fig-161-1]

![Hinh: fig-161-2]

- ImageNet5k, AlexNet, VGG, ResNet, ResNeXt

11:21

### LSTMs

11:22

### LSTM

- c is a memory signal, that is multiplied with a sigmoid signal Γf . If that is saturated (Γf ≈ 1), the memory is preserved; and backpropagation copies gradients back

- If Γi is close to 1, a new signal c̃ is written into memory

- If Γo is close to 1, the memory contributes to the normal neural activations a

<!-- page: 162 -->
11:23

### Collateral Benefits of NNs

![Hinh: fig-162-1]

- The differentiable computation graph paradigm

  - Perhaps a new paradigm to design large scale systems, beyond what software en-
gineering teaches classically

- NN Diagrams as a specification language of models

  - “Click your Network Together”

  - High expressiveness to be creative in formulating really novel methods (e.g., Au-
toencoders, Embed2Control, GANs)

11:24

### Optimization: Stochastic Gradient Descent

- Standard optimization methods (gradient descent backtracking line search, LBFGS, other (quasi) Newton methods) have strong guarantees, but require exact gradients.

  - But computing exact gradients of the loss $L(f, D)$ would require to go through the
full data set D – for every gradient evaluation. That does not scale to big data.

- Instead, use stochastic gradient descent, where the gradient is computed only for a batch D̂ ⊂ ∼ D of fixed size k, subsampled uniformly from the whole D.

11:25

- Core reference: Yurii Nesterov (1983): A method for solving the convex programming problm with convergence rate $O(1/k2)$ Y Nesterov (2013): Introductory lectures on convex optimization: A basic course Springer

- See also: Mahsereci & Hennig (NIPS’15): Probabilistic line searches for stochastic optimization

11:26

<!-- page: 163 -->
### ADAM

![Hinh: fig-163-1]

arXiv:1412.6980 (all operations interpreted element-wise)

11:27

### Deep RL

- Value Network

- Advantage Network

- Action Network

- Experience Replay (prioritized)

- Fixed Q-targets

- etc, etc

11:28

### Conclusions

- Conventional feed-forward neural networks are by no means magic. They’re a parameterized function, which is fit to data.

- Convolutional NNs do make strong and good assumptions about how information processing on images should be structured. The results are great and related to some degree to human visual representations. A large part of the success of deep learning is on images. Also LSTMs make good assumptions about how memory signals help represent time series. The flexibility of “clicking together” network structures and general differentiable computation graphs is great.

<!-- page: 164 -->
All these are innovations w.r.t. formulating structured models for ML

- The major strength of NNs is in their capacity and that, using massive parallelized computation, they can be trained on tons of data. Maybe they don’t even need to be better than nearest neighbor lookup, but they can be queried much faster.

11:29

<!-- page: 165 -->
# 12 Explainable AI

### Explainable AI

- General Concept of Explaination

  - Data, Objective, Method, & Input

  - Counterfactuals & Pearl

- Fitting interpretable models to black-boxes

- Sensitivity Analysis

  - in general

  - in NNs: Influence functions, relevance propagation

  - Relation to Adversarial Examples

- Post-Hoc Rationalization

12:1

### Why care for Explainability

(Following Doshi-Velez & Kim’s arguments)

- Classical engineering: complete objectives and evaluation

  - formal guarantees \to  system achieves well-defined objective \to  trust

- Novel AI applications: incomplete objectives

  - Ethics, fairness & unbiasedness, privacy

  - Safety and robustness beyond testable/formalizable domains

  - Multi-objective trade-offs

- In those cases we want interpretable models and predictions

12:2

### What does Explainable mean?

- Why did you go to university today?

- In cognitive science: Counterfactuals

- A ML decision y = $f(x)$ has four ingredients:

  - The data D

  - The objective L

  - The method/algorithm/hypothesis space: M, such that f = $M(L, D)$

<!-- page: 166 -->
  - The query input x

- recall Pearl’s notion of causality based on intervention

12:3

### Fitting Interpretable models to a Black-Box

- Started in the 80ies:

  - Sun, Ron: Robust Reasoning: Integrating Rule-Based and Similarity-Based Reasoning.
AI, 1995.

  - Ras, van Gerven & Haselager (in Spring 2018): “Unlike other methods in Machine
Learning (ML), such as decision trees or Bayesian networks, an explanation for a
certain decision made by a DNN cannot be retrieved by simply scrutinizing the
inference process.”

  - Bastani et al: Interpreting Blackbox Models via Model Extraction, 2018:
“We propose to construct global explanations of complex, blackbox models in the
form of a decision tree approximating the original model.”

- (Great Work: Causal Generative Neural Networks, Guyon & Sebag)

12:4

### Sensitivity Analysis

12:5

### Sensitivity Analysis in Optimization

- Consider a general problem x∗ = argmin x $f(x)$ s.t. $g(x)\leq$ 0, $h(x)$ = 0

  - where x $\in$ Rn
, f : Rn
\to  R, g : Rn
\to  Rm
, h : Rn
\to  Rm0
, all smooth

  - First compute the optimum

  - Then explain the optimum

12:6

### Sensitivity Analysis in Optimization

- KKT conditions: x optimal $\Rightarrow$ \exists λ $\in$ Rm , ν $\in$ Rm0 such that ∇ $f(x)$ + ∇ $g(x)$> λ + ∇ $h(x)$> ν = 0 (17) $g(x)\leq$ 0 , $h(x)$ = 0 , λ $\geq$ 0 (18) λ ◦ $g(x)$ = 0 , (19)

- Consider infinitesimal variation ˜ f = f +  ˆ f, g̃ = g + ĝ, h̃ = h + ĥ; how does x∗ vary?

<!-- page: 167 -->
  - The KKT resitual will be
r̂ =
(




(
∇ˆ
f + ∇ĝ>
λ + ∇
ĥ>
ν
ĥ
λ ◦ ĝ
)




)

  - The primal-dual Newton step will be
(




(
x̂
λ̂
ν̂
)




)
= -
(




(
∇2
f ∇
g>
∇
h>
∇
h 0 0
$diag(\lambda)$∇
g $diag(g)$ 0
)




)
-1 (




(
∇ˆ
f + ∇ĝ>
λ + ∇
ĥ>
ν
ĥ
λ ◦ ĝ
)




)

- The new optimum is at x∗ + x̂

  - Insight: This derivation implies stability of constraint activity, which is “standard
constraint qualification” in the optimization literature

12:7

### Sensitivity Analysis in Optimization

- Bottom line: We can analyze how changes in the optimization problem translate to changes of the optimium x∗

- Differentiable Optimization

  - Can be embedded in auto-differentiation computation graphs (Tensorflow)

  - Important implications for Differentiable Physics

  - But: Not differentiable across constraint activations

12:8

### Sensitivity Analysis in Neural Nets

- Let f : Rn \to  R be a function from some input features xi to a discriminative value

- (From Montavan et al:)

  - We aim for a functional understanding, not a “lower-level mechanistic or algorith-
mic” understanding

  - Features xi are assumed to be in some human-interpretable domain: e.g., images,
text

  - An explanation is a collection of interpretable features that contributed to the deci-
sion

- Sensitivity Analysis \leftrightarrow  Use gradients to quantify contribution of features to a value

12:9

<!-- page: 168 -->
### Example: Guided Backprop

![Hinh: fig-168-1]

![Hinh: fig-168-2]

(Springenberg et al, 2014)

  - Correct backprop for ReLu: δl
i = [xl
i > 0] δl+1
i where δl+1
i = df
dxl+1
i

  - Guided backprop: Rl
i = [xl
i > 0] [Rl+1
i > 0] Rl+1
i

12:10

### Relevance Propagation & Deep Taylor Decomposition

- Not only gradients, but decompose value in additive relevances per feature f = X i Ri

- Deep Taylor Decomposition:

  - ReLu networks are piece-wise linear
\to  exact equations to propagate 1st-order Taylor coefficients through network

12:11

<!-- page: 169 -->
### Relevance Propagation & Deep Taylor Decomposition

![Hinh: fig-169-1]

![Hinh: fig-169-2]

12:12

### Relevance Propagation & Deep Taylor Decomposition

12:13

### Feature Inversion

- Try to find a “minimal image” that leads to the same value: x∗ = argmin x ||$f(x)$ - $f(xorig)$||2 + $R(x)$

  - Constrain x to be maskings of the original image xorig

<!-- page: 170 -->
(Du et al 2018)

12:14

### Feature Inversion

![Hinh: fig-170-1]

![Hinh: fig-170-2]

(Du et al 2018)

12:15

### Influence Functions

- Sensitivity w.r.t. data set!

  - Leave-one-out retraining

  - Vary the weighting of a training point (thereby the objective)

  - Vary a training point itself: input image x ← x + δ

  - Use linear sensitivity analysis to

<!-- page: 171 -->
(Koh & Liang, ICML’17)

12:16

### Post-Hoc Rationalization

![Hinh: fig-171-1]

![Hinh: fig-171-2]

![Hinh: fig-171-3]

12:17

### Post-Hoc Rationalization

- Given an image and a (predicted) classification, learn to rationalize it!

- Data includes explanations!

  - Caltech UCSD Birds 200-2011; 200 classes of bird species; 11,788 images

  - Plus five sentences for each image! E.g., “This is a bird with red feathers and has a
black face patch”
(Akata et al, 2018)
(Akata et al, 2018)

12:18

### References

<!-- page: 172 -->
- Koh, Pang Wei, and Percy Liang: Understanding Black-Box Predictions via Influence Functions. ArXiv:1703.04730

- Escalante, Hugo Jair, Sergio Escalera, Isabelle Guyon, Xavier Baró, Yağmur Güçlütürk, Umut Güçlü, and Marcel van Gerven: Explainable and Interpretable Models in Computer Vision and Machine Learning. Springer Series on Challenges in Machine Learning, 2018.

- Zeynep Akata, Lisa Anne Hendricks, Stephan Alaniz, and Trevor Darrell: Generating Post-Hoc Rationales of Deep Visual Classification Decisions. Springer 2018

- Montavon, Grégoire, Wojciech Samek, and Klaus-Robert Müller: Methods for Interpreting and Understanding Deep Neural Networks. Digital Signal Processing 73, 2018

- Springenberg, Jost Tobias, Alexey Dosovitskiy, Thomas Brox, and Martin Riedmiller: Striving for Simplicity: The All Convolutional Net. ArXiv:1412.6806

- Du, Mengnan, Ninghao Liu, Qingquan Song, and Xia Hu: Towards Explanation of DNNBased Prediction with Guided Feature Inversion. ArXiv:1804.00506 spangenberg

12:19

<!-- page: 173 -->
# 13 Propositional Logic

(slides based on Stuart Russell’s AI course)

### Motivation & Outline

Most students will have learnt about propositional logic their first classes. It represents the simplest and most basic kind of logic. The main motivation to teach it really is as a precursor of first-order logic (FOL), which is covered in the next lecture. The intro of the next lecture motivates FOL in detail. The main point is that in recent years there were important developments that unified FOL methods with probabilistic reasoning and learning methods, which really allows to tackle novel problems. In this lecture we go quickly over the syntax and semantics of propositional logic. Then we cover the basic methods for logic inference: fwd & bwd chaining, as well as resolution. 13.1 Syntax & Semantics

13:1

### Outline

- Example: Knowledge-based agents & Wumpus world

- Logic in general—models and entailment

- Propositional (Boolean) logic

- Equivalence, validity, satisfiability

- Inference rules and theorem proving

  - forward chaining

  - backward chaining

  - resolution

13:2

### Knowledge bases

agent $s_{0}s_{1}a_{0}s_{2}a_{1}s_{3}a_{2}a_{3}y_{0}y_{1}y_{2}y_{3}$

<!-- page: 174 -->
- An agent maintains a knowledge base Knowledge base = set of sentences of a formal language

13:3

### Wumpus World description

![Hinh: fig-174-1]

Performance measure gold +1000, death -1000 -1 per step, -10 for using the arrow Environment Squares adjacent to wumpus are smelly Squares adjacent to pit are breezy Glitter iff gold is in the same square Shooting kills wumpus if you are facing it The wumpus kills you if in the same square Shooting uses up the only arrow Grabbing picks up gold if in same square Releasing drops the gold in same square Actuators Left turn, Right turn, Forward, Grab, Release, Shoot, Climb Sensors Breeze, Glitter, Stench, Bump, Scream

13:4

### Exploring a wumpus world

<!-- page: 175 -->
![Hinh: fig-175-1]

<!-- page: 176 -->
![Hinh: fig-176-1]

<!-- page: 177 -->
![Hinh: fig-177-1]

<!-- page: 178 -->
13:5

### Other tight spots

![Hinh: fig-178-1]

![Hinh: fig-178-2]

Breeze in (1,2) and (2,1)

$$
\Rightarrow no safe actions
$$

Assuming pits uniformly distributed, (2,2) has pit w/ prob 0.86, vs. 0.31

$$
Smell in (1,1) \Rightarrow cannot move
$$

Can use a strategy of coercion: shoot straight ahead

$$
wumpus was there \Rightarrow dead \Rightarrow safe wumpus wasn’t there \Rightarrow safe
$$

13:6

### Logic in general

- A Logic is a formal languages for representing information such that conclusions can be drawn

- The Syntax defines the sentences in the language

<!-- page: 179 -->
- The Semantics defines the “meaning” of sentences; i.e., define truth of a sentence in a world E.g., the language of arithmetic x + 2 $\geq$ y is a sentence; $x_{2}$ + y > is not a sentence x + 2 $\geq$ y is true iff the number x + 2 is no less than the number y x + 2 $\geq$ y is true in a world where x = 7, y = 1 x + 2 $\geq$ y is false in a world where x = 0, y = 6

13:7

### Notions in general logic

- A logic is a language, elements α are sentences

- A model m is a world/state description that allows us to evaluate α(m) $\in$ {true, false} uniquely for any sentence α We define $M(\alpha)$ = {m : α(m) = true} as the models for which α holds

- Entailment α |= β: $M(\alpha)$ ⊆ $M(\beta)$, “\forall m : α(m) $\Rightarrow$ β(m)” (Folgerung)

- Equivalence α ≡ β: iff (α |= β and β |= α)

- A KB is a set (=conjunction) of sentences

- An inference procedure i can infer α from KB: KB `i α

- soundness of i: KB `i α implies KB |= α (Korrektheit)

- completeness of i: KB |= α implies KB `i α

13:8

### Propositional logic: Syntax

$$
hsentencei \to hatomic sentencei | hcomplex sentencei hatomic sentencei \to true | false | P | Q | R | ... hcomplex sentencei \to \neg hsentencei | (hsentencei \land hsentencei) | (hsentencei \lor hsentencei) | (hsentencei \Rightarrow hsentencei) | (hsentencei \Leftrightarrow hsentencei)
$$

13:9

### Propositional logic: Semantics

- Each model specifies true/false for each proposition symbol E.g. P1,2 P2,2 P3,1 true true false (With these symbols, 8 possible models, can be enumerated automatically.)

- Rules for evaluating truth with respect to a model m:

<!-- page: 180 -->
$$
\neg S is true iff S is false S1 \land S2 is true iff S1 is true and S2 is true S1 \lor S2 is true iff S1 is true or S2 is true S1 \Rightarrow S2 is true iff S1 is false or S2 is true
$$

i.e., is false iff S1 is true and S2 is false

$$
S1 \Leftrightarrow S2 is true iff S1 \Rightarrow S2 is true and S2 \Rightarrow S1 is true
$$

- Simple recursive process evaluates an arbitrary sentence, e.g., $\neg$P1,2 $\land$ (P2,2 $\lor$ P3,1) = true $\land$ (false $\lor$ true) = true $\land$ true = true

13:10

### Notions in propositional logic – summary

- conjunction: α $\land$ β, disjunction: α $\lor$ β, negation: $\neg$α

- implication: α $\Rightarrow$ β ≡ $\neg$α $\lor$ β

- biconditional: α $\Leftrightarrow$ β ≡ (α $\Rightarrow$ β) $\land$ (β $\Rightarrow$ α) Note: |= and ≡ are statements about sentences in a logic; $\Rightarrow$ and $\Leftrightarrow$ are symbols in the grammar of propositional logic

- α valid: true for any model (allgemeingültig). E.g., true; A $\lor\neg$A; A $\Rightarrow$ A; (A $\land$ (A $\Rightarrow$ B)) $\Rightarrow$ B Note: KB |= α iff [(KB $\Rightarrow$ α) is valid]

- α unsatisfiable: true for no model. E.g., A $\land\neg$A; Note: KB |= α iff [(KB $\land\neg$α) is unsatisfiable]

- literal: A or $\neg$A, clause: disj. of literals, CNF: conj. of clauses

- Horn clause: symbol | (conjunction of symbols $\Rightarrow$ symbol), Horn form: conjunction of Horn clauses Modus Ponens rule: complete for Horn KBs α1,...,αn, α1$\land$···$\land$αn $\Rightarrow$ β β Resolution rule: complete for propositional logic in CNF, let “`i = $\neg$mj”: `1$\lor$···$\lor$`k, m1$\lor$···$\lor$mn `1$\lor$···$\lor$`i-1$\lor$`i+1$\lor$···$\lor$`k$\lor$m1$\lor$···$\lor$mj-1$\lor$mj+1$\lor$···$\lor$mn

13:11

### Logical equivalence

- Two sentences are logically equivalent iff true in same models: α ≡ β if and only if α |= β and β |= α (α $\land$ β) ≡ (β $\land$ α) commutativity of $\land$ (α $\lor$ β) ≡ (β $\lor$ α) commutativity of $\lor$ ((α $\land$ β) $\land$ γ) ≡ (α $\land$ (β $\land$ γ)) associativity of $\land$ ((α $\lor$ β) $\lor$ γ) ≡ (α $\lor$ (β $\lor$ γ)) associativity of $\lor\neg$($\neg$α) ≡ α double-negation elimination (α $\Rightarrow$ β) ≡ ($\neg$β $\Rightarrow\neg$α) contraposition (α $\Rightarrow$ β) ≡ ($\neg$α $\lor$ β) implication elimination (α $\Leftrightarrow$ β) ≡ ((α $\Rightarrow$ β) $\land$ (β $\Rightarrow$ α)) biconditional elimination

<!-- page: 181 -->
$$
\neg(\alpha \land \beta) \equiv (\neg\alpha \lor \neg\beta) De Morgan \neg(\alpha \lor \beta) \equiv (\neg\alpha \land \neg\beta) De Morgan (\alpha \land (\beta \lor \gamma)) \equiv ((\alpha \land \beta) \lor (\alpha \land \gamma)) distributivity of \land over \lor (\alpha \lor (\beta \land \gamma)) \equiv ((\alpha \lor \beta) \land (\alpha \lor \gamma)) distributivity of \lor over \land
$$

13:12

### Example: Entailment in the wumpus world

![Hinh: fig-181-1]

![Hinh: fig-181-2]

Situation after detecting nothing in [1,1], moving right, breeze in [2,1] Consider possible models for ?s assuming only pits

# 3 Boolean choices \Rightarrow  8 possible models

13:13

### Wumpus models

13:14

<!-- page: 182 -->
### Wumpus models

![Hinh: fig-182-1]

![Hinh: fig-182-2]

$$
KB = wumpus-world rules + observations
$$

13:15

### Wumpus models

$$
KB = wumpus-world rules + observations \alpha1 = “[1,2] is safe”, KB |= \alpha1, proved by model checking
$$

13:16

<!-- page: 183 -->
### Wumpus models

![Hinh: fig-183-1]

![Hinh: fig-183-2]

$$
KB = wumpus-world rules + observations \alpha2 = “[2,2] is safe”, KB 6|= \alpha2
$$

13:17

## 13.2 Inference Methods

13:18

### Inference

- Inference in the general sense means: Given some pieces of information (prior, observed variabes, knowledge base) what is the implication (the implied information, the posterior) on other things (non-observed variables, sentence)

- KB `i α = sentence α can be derived from KB by procedure i Consequences of KB are a haystack; α is a needle. Entailment = needle in haystack; inference = finding it

- Soundness: i is sound if whenever KB `i α, it is also true that KB |= α Completeness: i is complete if whenever KB |= α, it is also true that KB `i α Preview: we will define a logic (first-order logic) which is expressive enough to say almost anything of interest, and for which there exists a sound and complete inference procedure. That is, the procedure will answer any question whose answer follows from what is known by the KB.

13:19

<!-- page: 184 -->
### Inference by enumeration

![Hinh: fig-184-1]

<!-- table structure uncertain on page 184 -->

Inference by enumeration

B1,1 B2,1 P1,1 P1,2 P2,1 P2,2 P3,1 R1 R2 R3 R4 R5 KB

false false false false false false false true true true true false false

false false false false false false true true true false true false false

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

false true false false false false false true true false true true false

false true false false false false true true true true true true true

false true false false false true false true true true true true true

false true false false false true true true true true true true true

false true false false true false false true false false true true false

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

true true true true true true true false true true false true false

Enumerate rows (different assignments to symbols),

if KB is true in row, check that α is too

13:20

```
Depth-first enumeration of all models is sound and complete

function TT-ENTAILS?(KB,α) returns true or false
inputs: KB, the knowledge base, a sentence in propositional logic
α, the query, a sentence in propositional logic
symbols ← a list of the proposition symbols in KB and α
return TT-CHECK-ALL(KB,α,symbols,[ ])
function TT-CHECK-ALL(KB,α,symbols,model) returns true or false
if EMPTY?(symbols) then
if PL-TRUE?(KB,model) then return PL-TRUE?(α,model)
else return true
else do
P ← FIRST(symbols); rest ← REST(symbols)
return TT-CHECK-ALL(KB,α,rest, EXTEND(P,true, model)) and
TT-CHECK-ALL(KB,α,rest, EXTEND(P,false, model))
O(2n) for n symbols
```

13:21

Proof methods

\bullet  Proof methods divide into (roughly) two kinds:

\bullet  Application of inference rules

– Legitimate (sound) generation of new sentences from old

– Proof = a sequence of inference rule applications

Can use inference rules as operators in a standard search alg.

– Typically require translation of sentences into a normal form

<!-- page: 185 -->
- Model checking truth table enumeration (always exponential in n) improved backtracking, e.g., Davis–Putnam–Logemann–Loveland (see book) heuristic search in model space (sound but incomplete) e.g., min-conflicts-like hill-climbing algorithms

13:22

### Forward and backward chaining

![Hinh: fig-185-1]

- Applicable when KB is in Horn Form

- Horn Form (restricted) KB = conjunction of Horn clauses Horn clause =

  - proposition symbol; or

  - (conjunction of symbols) $\Rightarrow$ symbol
E.g., C $\land$ (B $\Rightarrow$ A) $\land$ (C $\land$ D $\Rightarrow$ B)

- Modus Ponens (for Horn Form): complete for Horn KBs α1, . . . , αn, α1 $\land$ · · · $\land$ αn $\Rightarrow$ β β Can be used with forward chaining or backward chaining.

- These algorithms are very natural and run in linear time

13:23

### Forward chaining

- Represent a KB as a graph

- Fire any rule whose premises are satisfied in the KB, add its conclusion to the KB, until query is found P $\Rightarrow$ Q L $\land$ M $\Rightarrow$ P B $\land$ L $\Rightarrow$ M A $\land$ P $\Rightarrow$ L A $\land$ B $\Rightarrow$ L A B

13:24

<!-- page: 186 -->
### Forward chaining example

![Hinh: fig-186-1]

<!-- page: 187 -->
![Hinh: fig-187-1]

<!-- page: 188 -->
![Hinh: fig-188-1]

<!-- page: 189 -->
![Hinh: fig-189-1]

13:25

<!-- page: 190 -->
### Forward chaining algorithm

```
function PL-FC-ENTAILS?(KB,q) returns true or false
inputs: KB, the knowledge base, a set of propositional Horn clauses
```

q, the query, a proposition symbol local variables: count, a table, indexed by clause, initially the number of premises inferred, a table, indexed by symbol, each entry initially false agenda, a list of symbols, initially the symbols known in KB while agenda is not empty do

$$
p \leftarrow POP(agenda)
$$

unless inferred[p] do

$$
inferred[p] \leftarrow true
$$

for each Horn clause c in whose premise p appears do decrement count[c]

$$
if count[c] = 0 then do if HEAD[c] = q then return true
$$

$PUSH(HEAD[c],agenda)$ return false

13:26

### Proof of completeness

FC derives every atomic sentence that is entailed by KB 1. FC reaches a fixed point where no new atomic sentences are derived 2. Consider the final state as a model m, assigning true/false to symbols 3. Every clause in the original KB is true in m

$$
Proof: Suppose a clause a_{1} \land . . . \land ak \Rightarrow b is false in m Then a_{1} \land . . . \land ak is true in m and b is false in m
$$

Therefore the algorithm has not reached a fixed point! 4. Hence m is a model of KB

$$
5. If KB |= q, q is true in every model of KB, including m
$$

General idea: construct any model of KB by sound inference, check α

13:27

### Backward chaining

- Idea: work backwards from the query q: to prove q by BC, check if q is known already, or prove by BC all premises of some rule concluding q

- Avoid loops: check if new subgoal is already on the goal stack

- Avoid repeated work: check if new subgoal 1) has already been proved true, or 2) has already failed

13:28

<!-- page: 191 -->
### Backward chaining example

![Hinh: fig-191-1]

<!-- page: 192 -->
![Hinh: fig-192-1]

<!-- page: 193 -->
![Hinh: fig-193-1]

<!-- page: 194 -->
![Hinh: fig-194-1]

<!-- page: 195 -->
13:29

### Forward vs. backward chaining

![Hinh: fig-195-1]

FC is data-driven, cf. automatic, unconscious processing, e.g., object recognition, routine decisions May do lots of work that is irrelevant to the goal BC is goal-driven, appropriate for problem-solving, e.g., Where are my keys? How do I get into a PhD program? Complexity of BC can be much less than linear in size of KB

13:30

<!-- page: 196 -->
### Resolution

![Hinh: fig-196-1]

- Conjunctive Normal Form (CNF—universal) conjunction of disjunctions of literals | {z } clauses E.g., (A $\lor\neg$B) $\land$ (B $\lor\neg$C $\lor\neg$D)

- Resolution inference rule (for CNF): complete for propositional logic `1$\lor$···$\lor$`k, m1$\lor$···$\lor$mn `1$\lor$···$\lor$`i-1$\lor$`i+1$\lor$···$\lor$`k$\lor$m1$\lor$···$\lor$mj-1$\lor$mj+1$\lor$···$\lor$mn where `i and mj are complementary literals.

- E.g., P1,3 $\lor$ P2,2, $\neg$P2,2 P1,3

- Resolution is sound and complete for propositional logic

13:31

### Conversion to CNF

$$
B1,1 \Leftrightarrow (P1,2 \lor P2,1) 1. Eliminate \Leftrightarrow, replacing \alpha \Leftrightarrow \beta with (\alpha \Rightarrow \beta) \land (\beta \Rightarrow \alpha). (B1,1 \Rightarrow (P1,2 \lor P2,1)) \land ((P1,2 \lor P2,1) \Rightarrow B1,1) 2. Eliminate \Rightarrow, replacing \alpha \Rightarrow \beta with \neg\alpha \lor \beta. (\neg B1,1 \lor P1,2 \lor P2,1) \land (\neg(P1,2 \lor P2,1) \lor B1,1) 3. Move \neg inwards using de Morgan’s rules and double-negation: (\neg B1,1 \lor P1,2 \lor P2,1) \land ((\neg P1,2 \land \neg P2,1) \lor B1,1) 4. Apply distributivity law (\lor over \land) and flatten: (\neg B1,1 \lor P1,2 \lor P2,1) \land (\neg P1,2 \lor B1,1) \land (\neg P2,1 \lor B1,1)
$$

13:32

### Resolution algorithm

$$
Proof by contradiction, i.e., show KB \land \neg\alpha unsatisfiable
$$

<!-- page: 197 -->
```
function PL-RESOLUTION(KB,α) returns true or false
inputs: KB, the knowledge base, a sentence in propositional logic
```

α, the query, a sentence in propositional logic

$$
clauses \leftarrow the set of clauses in the CNF representation of KB \land \neg\alpha new \leftarrow \emptyset
$$

loop do for each Ci, Cj in clauses do

$$
resolvents \leftarrow PL-RESOLVE(Ci,Cj)
$$

if resolvents contains the empty clause then return true

$$
new \leftarrow new \cup resolvents if new \subseteq clauses then return false clauses \leftarrow clauses \cup new
$$

13:33

### Resolution example

![Hinh: fig-197-1]

$$
KB = (B1,1 \Leftrightarrow (P1,2 \lor P2,1)) \land \neg B1,1 \alpha = \neg P1,2
$$

13:34

### Summary

Logical agents apply inference to a knowledge base to derive new information and make decisions Basic concepts of logic:

  - syntax: formal structure of sentences

  - semantics: truth of sentences wrt models

  - entailment: necessary truth of one sentence given another

  - inference: deriving sentences from other sentences

  - soundness: derivations produce only entailed sentences

  - completeness: derivations can produce all entailed sentences
Wumpus world requires the ability to represent partial and negated informa-
tion, reason by cases, etc.
Forward, backward chaining are linear-time, complete for Horn clauses
Resolution is complete for propositional logic
Propositional logic lacks expressive power

<!-- page: 198 -->
13:35

<!-- page: 199 -->
# 14 First-Order Logic**

(slides based on Stuart Russell’s AI course)

### Motivation & Outline

First-order logic (FOL) is exactly what is sometimes been thought of as “Good OldFashioned AI” (GOFAI) – and what was the central target of critique on AI research coming from other fields like probabilistic reasoning and machine learning. A bit over-simplified, in the AI winter many researchers said “logic doesn’t work”, therefore AI doesn’t work, and instead the focus should be on learning and probabilistic modelling. Some comments on this: First, I think one should clearly distinguish between 1) logic reasoning and inference, and 2) “first-order (or relational) representations”. Logic reasoning indeed is only applicable on discrete & deterministic knowledge bases. And as learnt knowledge is hardly deterministic (it cannot be in a Bayesian view), logic reasoning does not really apply well. In my view, this is one of the core problems with GOFAI: the fact that logic reasoning does not unify well with learning and learned models. However, using “first-order (or relational) representations” means to represent knowledge in such a way that it refers only to object properties and relations, and therefore generalizes across object identities. Sure, classical FOL knowledge bases are first-order knowledge representations. But here research has advanced tremendously: nowadays we can also represent learned classifiers/regressions, graphical models, and Markov Decision Processes in a first-order (also called “relational” or “lifted”) way. The latter are core probabilistic formalisms to account for uncertainty and learning. Therefore the current state-of-the-art provides a series of unifications of probabilistic and first-order representations. I think this is what makes it important to learn and understand first-order representations – which is best taught in the context of FOL. The reasoning and inference methods one requires for modern relational probabilistic models are of course different to classical logical reasoning. Therefore, I think knowing about “logical reasoning” is less important than knowing about “logical representations”. Still, some basic aspects of logical reasoning, such as computing all possible substitutions for an abstract sentence, thereby grounding the sentence, are essential in all first-order models. Modern research on relational machine learning has, around 2011, lead to some new optimism about modern AI, also called the spring of AI (see, e.g., “I, algorithm: A new dawn for artificial intelligence”, 2011). That wave of optimism now got over-rolled by the new hype on deep learning, which in the media is often equated with AI. However, at least up to now, one should clearly distinguish between deep learning as a great tool for machine learning with huge amounts of data; and reasoning, which includes model-based decision making, control, planning, and also (Bayesian) learning from few data. This lecture introduces to FOL. The goal is to understand FOL as the basis for decision-making problems such as STRIPS rules, as well as for relational proba-

<!-- page: 200 -->
bilistic models such as relational Reinforcement Learning and statistical relational learning methods. The latter are (briefly) introduced in the next lecture. We first introduce the FOL language, then basic inference algorithms. Perhaps one of the most important concepts is the problem of computing substitutions (also called unification or matching problem), where much of the computational complexity of FOL representations arises. 14.1 The FOL language FOL is a language—we define the syntax, the semantics, and give examples. 14:1

### The limitation of propositional logic

- Propositional logic has nice properties:

  - Propositional logic is declarative: pieces of syntax correspond to facts

  - Propositional logic allows partial/disjunctive/negated information (unlike most
data structures and databases)

  - Propositional logic is compositional: meaning of B1,1 $\land$P1,2 is derived from meaning
of B1,1 and of P1,2

  - Meaning in propositional logic is context-independent (unlike natural language, where
meaning depends on context)

- Limitation:

  - Propositional logic has very limited expressive power, unlike natural language.
E.g., we cannot express “pits cause breezes in adjacent squares” except by writing
one sentence for each square

14:2

### First-order logic

- Whereas propositional logic assumes that a world contains facts, first-order logic (like natural language) assumes the world contains

  - Objects: people, houses, numbers, theories, Ronald McDonald, colors, baseball games,
wars, centuries . . .

  - Relations: red, round, bogus, prime, multistoried . . ., brother of, bigger than, inside,
part of, has color, occurred after, owns, comes between, . . .

  - Functions: father of, best friend, third inning of, one more than, end of . . .

14:3

<!-- page: 201 -->
### FOL syntax elements

Constants KingJohn, 2, UCB, . . . Predicates Brother, >, . . . Variables x, y, a, b, . . .

$$
Connectives \land \lor \neg \Rightarrow \Leftrightarrow Equality = Quantifiers \forall \exists
$$

Functions Sqrt, LeftLegOf, . . .

14:4

### FOL syntax grammar

$$
hsentencei \to hatomic sentencei
$$

| hcomplex sentencei

$$
| [\forall | \exists] hvariablei hsentencei hatomic sentencei \to predicate(htermi,...) | htermi=htermi htermi \to function(htermi,...)
$$

| constant | variable

$$
hcomplex sentencei \to \neg hsentencei | (hsentencei [\land | \lor | \Rightarrow | \Leftrightarrow ] hsentencei)
$$

14:5

### Quantifiers

- Universal quantification \forall  hvariablesi hsentencei \forall  x P is true in a model m iff P is true with x being each possible object in the model Example: “Everyone at Berkeley is smart:” \forall  x $At(x, Berkeley)\Rightarrow Smart(x)$

- Existential quantification \exists  hvariablesi hsentencei \exists  x P is true in a model m iff P is true with x being some possible object in the model Example: “Someone at Stanford is smart:” \exists  x $At(x, Stanford)\land Smart(x)$

14:6

### Properties of quantifiers

- \forall  x \forall  y is the same as \forall  y \forall  x

- \exists  x \exists  y is the same as \exists  y \exists  x

<!-- page: 202 -->
- \exists  x \forall  y is not the same as \forall  y \exists  x \exists  x \forall  y $Loves(x, y)$: “There is a person who loves everyone in the world” \forall  y \exists  x $Loves(x, y)$: “Everyone in the world is loved by at least one person”

- Quantifier duality: each can be expressed using the other \forall  x $Likes(x, IceCream)$ ≡ $\neg$\exists  x $\neg```text
Likes(x, IceCream)$ \exists  x $Likes(x, Broccoli)$ ≡ $\neg$\forall  x $\neg
```Likes(x, Broccoli)$

14:7

### Semantics: Truth in first-order logic

![Hinh: fig-202-1]

- Sentences are true with respect to a model and an interpretation

- A model contains $\geq$ 1 objects and relations among them

- An interpretation specifies referents for constant symbols \to  objects predicate symbols \to  relations function symbols \to  functional relations

- An atomic sentence $predicate(term1, . . . , termn)$ is true iff the objects referred to by term1, . . . , termn are in the relation referred to by predicate

14:8

### Models for FOL: Example

14:9

### Models for FOL: Lots!

- Entailment in propositional logic can be computed by enumerating models

- We can also enumerate the FOL models for a given KB:

<!-- page: 203 -->
  - For each number of domain elements n from 1 to $\infty$

  - For each k-ary predicate Pk in the vocabulary

  - For each possible k-ary relation on n objects

  - For each constant symbol C in the vocabulary

  - For each choice of referent for C from n objects . . .

- Enumerating FOL models is very inefficient

14:10

### Example sentences

- “Brothers are siblings” \forall  x, y $Brother(x, y)\Rightarrow Sibling(x, y)$.

- “Sibling” is symmetric \forall  x, y $Sibling(x, y)\Leftrightarrow Sibling(y, x)$.

- “One’s mother is one’s female parent” \forall  x, y $Mother(x, y)\Leftrightarrow$ ($Female(x)\land Parent(x, y)$).

- “A first cousin is a child of a parent’s sibling” \forall  x, y $FirstCousin(x, y)\Leftrightarrow$ \exists  p, ps $Parent(p, x)$$\land$$Sibling(ps, p)$$\land$$Parent(ps, y)$

14:11

## 14.2 FOL Inference

14:12

### Universal instantiation (UI)

- Whenever a KB contains a universally quantified sentence, we may add to the KB any instantiation of that sentence, where the logic variable v is replaced by a concrete ground term g: \forall  v α $SUBST({v/g}, \alpha)$ E.g., \forall  x $King(x)\land Greedy(x)\Rightarrow Evil(x)$ yields $King(John)\land Greedy(John)\Rightarrow Evil(John)King(Richard)\land Greedy(Richard)\Rightarrow Evil(Richard)$ King($Father(John)$) $\land$ Greedy($Father(John)$) $\Rightarrow$ Evil($Father(John)$) . . .

14:13

<!-- page: 204 -->
### Existential instantiation (EI)

- Whenever a KB contains a existentially quantified sentence \exists  v α, we may add a single instantiation of that sentence to the KB, where the logic variable v is replaced by a Skolem constant symbol k which must not appear elsewhere in the knowledge base: \exists  v α $SUBST({v/k}, \alpha)$ E.g., \exists  x $Crown(x)\land OnHead(x, John)$ yields $Crown(C1)\land OnHead(C1, John)$ provided C1 is a new constant symbol, called a Skolem constant Another example: from \exists  x $d(xy )$/dy = xy we obtain $d(ey )$/dy = ey where e is a new constant symbol

14:14

### Instantiations contd.

- UI can be applied several times to add new sentences; the new KB is logically equivalent to the old

- EI can be applied once to replace the existential sentence; the new KB is not equivalent to the old, but is satisfiable iff the old KB was satisfiable

14:15

### Reduction to propositional inference

- Instantiating all quantified sentences allows us to ground the KB, that is, to make the KB propositional

- Example: Suppose the KB contains just the following: \forall  x $King(x)\land Greedy(x)\Rightarrow Evil(x)King(John)Greedy(John)Brother(Richard, John)$ Instantiating the universal sentence in all possible ways, we have $King(John)\land Greedy(John)\Rightarrow Evil(John)King(Richard)\land Greedy(Richard)\Rightarrow Evil(Richard)King(John)Greedy(John)Brother(Richard, John)$ The new KB is propositionalized: proposition symbols are $King(John)$, $Greedy(John)$, Evil(J

14:16

<!-- page: 205 -->
### Theory on propositionalization

- Claim: A ground sentence is entailed by the propositionalized KB iff entailed by original FOL KB (or “Every FOL KB can be propositionalized so as to preserve entailment”)

- Then, FOL inference can be done by: propositionalize KB and query, apply resolution, return result

- Problem: with function symbols, there are infinitely many ground terms, e.g., Father(Father($Father(John)$))

- Theorem: Herbrand (1930). If a sentence α is entailed by an FOL KB, it is entailed by a finite subset of the propositional KB

- Idea: For n = 0 to $\infty$ do create a propositional KB by instantiating with depth-n terms see if α is entailed by this KB

- Problem: works if α is entailed, loops if α is not entailed

- Theorem: Turing (1936), Church (1936), entailment in FOL is semidecidable

14:17

### Inefficiency of naive propositionalization

- Propositionalization generates lots of irrelevant sentences. Example: \forall  x $King(x)\land Greedy(x)\Rightarrow Evil(x)King(John)$ \forall  y $Greedy(y)Brother(Richard, John)$ propositionalization produces not only $Greedy(John)$, but also $Greedy(Richard)$ which is irrelevant for a query $Evil(John)$

- With p k-ary predicates and n constants, there are p · nk instantiations With function symbols, it gets much much worse!

14:18

### Unification

- Instead of instantiating quantified sentences in all possible ways, we can compute specific substitutions “that make sense”. These are substitutions that unify abstract sentences so that rules (Horn clauses, GMP, see next slide) can be applied.

- In the previous example, the “Evil-rule” can be applied if we can find a substitution θ such that $King(x)$ and $Greedy(x)$ match $King(John)$ and $Greedy(y)$. Namely, θ = {x/John, y/John} is such a substitutions. We write θ $unifies(\alpha, \beta)$ iff αθ = βθ

<!-- page: 206 -->
- Examples: p q θ $Knows(John, x)Knows(John, Jane)$ {x/Jane} $Knows(John, x)Knows(y, OJ)$ {x/OJ, y/John} $Knows(John, x)$ Knows(y, $Mother(y)$) {y/John, x/$Mother(John)$} $Knows(John, x)Knows(x, OJ)$ fail Standardizing apart the names of logic variables eliminates the overlap of variables, e.g., $Knows(z17, OJ)$

14:19

### Generalized Modus Ponens (GMP)

- For every substitution θ such that \forall i : θ $unifies(p0 i, pi)$ we can apply: p1 0 , p2 0 , . . . , pn 0 , (p1 $\land$ p2 $\land$ . . . $\land$ pn $\Rightarrow$ q) qθ Example: p1 0 is $King(John)$ p1 is $King(x)$ p2 0 is $Greedy(y)$ p2 is $Greedy(x)$ θ is {x/John, y/John} q is $Evil(x)$ qθ is $Evil(John)$

- This GMP assumes a KB of definite clauses (exactly one positive literal) By default, all variables are assumed universally quantified.

14:20

### Forward chaining algorithm

```
function FOL-FC-ASK(KB,α) returns a substitution or false
repeat until new is empty
new ← { }
for each sentence r in KB do
```

$$
( p1 \land . . . \land pn \Rightarrow q) \leftarrow STANDARDIZE-APART(r) for each \theta such that (p1 \land . . . \land pn)\theta = (p0 1 \land . . . \land p0
$$

n)θ for some p0 1, . . . , p0 n in KB

$$
q0 \leftarrow SUBST(\theta,q)
$$

if q0 is not a renaming of a sentence already in KB or new then do add q0 to new

$$
\phi \leftarrow UNIFY(q0,\alpha)
$$

if φ is not fail then return φ add new to KB return false

14:21

<!-- page: 207 -->
### Example: Crime

The law says that it is a crime for an American to sell weapons to hostile nations. The country Nono, an enemy of America, has some missiles, and all of its missiles were sold to it by Colonel West, who is American. Prove that Col. West is a criminal.

14:22

### Example: Crime – formalization

- . . . it is a crime for an American to sell weapons to hostile nations: $American(x)\land Weapon(y)\land Sells(x, y, z)\land Hostile(z)\Rightarrow Criminal(x)$

- Nono . . . has some missiles, i.e., \exists  x $Owns(Nono, x)\land Missile(x)$: $Owns(Nono, M1)$ and $Missile(M1)$

- . . . all of its missiles were sold to it by Colonel West \forall  x $Missile(x)\land Owns(Nono, x)\Rightarrow Sells(West, x, Nono)$

- Missiles are weapons: $Missile(x)\Rightarrow Weapon(x)$

- An enemy of America counts as “hostile”: $Enemy(x, America)\Rightarrow Hostile(x)$

- West, who is American . . . $American(West)$

- The country Nono, an enemy of America . . . $Enemy(Nono, America)$

14:23

### Example: Crime – forward chaining proof

<!-- page: 208 -->
14:24

### Properties of forward chaining

![Hinh: fig-208-1]

- Sound and complete for first-order definite clauses (proof similar to propositional proof)

- Datalog = first-order definite clauses + no functions (e.g., crime KB). Forward chaining terminates for Datalog in poly iterations: at most p · nk literals

- May not terminate in general if α is not entailed This is unavoidable: entailment with definite clauses is semidecidable

- Efficiency:

  - Simple observation: no need to match (=compute possible substitutions) a rule on
iteration k if a premise wasn’t added on iteration k - 1 $\Rightarrow$ match only rules whose
premise contain a newly added literal

  - Matching (computing substitutions) can be expensive:

  - Database indexing allows $O(1)$ retrieval of known facts, e.g., query $Missile(x)$
retrieves $Missile(M1)$

  - But matching conjunctive premises against known facts is NP-hard (is a CSP
problem, see below)

<!-- page: 209 -->
14:25

### Hard matching example: a CSP

![Hinh: fig-209-1]

- Consider the KB: $Diff(wa, nt)\land Diff(wa, sa)\land Diff(nt, q)\land Diff(nt, sa)\land Diff(q, nsw)\land Diff(q, sa)\land Diff(nsw, v)\land Diff(nsw, sa)\land Diff(v, sa)\Rightarrow$ Colorable() $Diff(Red, Blue)$, $Diff(Red, Green)$, $Diff(Green, Red)Diff(Green, Blue)$, $Diff(Blue, Red)$, $Diff(Blue, Green)$

- Colorable() is inferred iff the CSP has a solution CSPs include 3SAT as a special case, hence matching is NP-hard

14:26

### Backward chaining algorithm*

```
function FOL-BC-ASK(KB,goals,θ) returns a set of substitutions
inputs: KB, a knowledge base
```

goals, a list of conjuncts forming a query (θ already applied) θ, the current substitution, initially the empty substitution { } local variables: answers, a set of substitutions, initially empty if goals is empty then return {θ}

$$
q0 \leftarrow SUBST(\theta, FIRST(goals))
$$

for each sentence r in KB

$$
where STANDARDIZE-APART(r) = ( p1 \land . . . \land pn \Rightarrow q) and \theta0 \leftarrow UNIFY(q,q0) succeeds new goals \leftarrow [ p1, . . . , pn|REST(goals)] answers \leftarrow FOL-BC-ASK(KB,new goals, COMPOSE(\theta0,\theta)) \cup answers
$$

return answers

14:27

### Backward chaining example*

<!-- page: 210 -->
![Hinh: fig-210-1]

![Hinh: fig-210-2]

<!-- page: 211 -->
![Hinh: fig-211-1]

![Hinh: fig-211-2]

<!-- page: 212 -->
14:28

### Properties of backward chaining*

![Hinh: fig-212-1]

![Hinh: fig-212-2]

- Depth-first recursive proof search: space is linear in size of proof

- Incomplete due to infinite loops $\Rightarrow$ fix by checking current goal against every goal on stack

- Inefficient due to repeated subgoals (both success and failure) $\Rightarrow$ fix using caching of previous results (extra space!)

- Widely used (without improvements!) for logic programming

14:29

### Example: Prolog*

- Declarative vs. imperative programming: Logic programming Ordinary programming 1. Identify problem Identify problem 2. Assemble information Assemble information 3. Tea break Figure out solution 4. Encode information in KB Program solution 5. Encode problem instance as facts Encode problem instance as data 6. Ask queries Apply program to data 7. Find false facts Debug procedural errors

- Russell says “should be easier to debug $Capital(NewY ork, US)$ than x := x + 2!”...

14:30

### Prolog systems*

- Basis: backward chaining with Horn clauses + bells & whistles Widely used in Europe, Japan (basis of 5th Generation project) Compilation techniques $\Rightarrow$ approaching a billion LIPS

<!-- page: 213 -->
- Program = set of clauses head :- literal1, . . . literaln. $criminal(X)$ :- $american(X)$, $weapon(Y)$, $sells(X,Y,Z)$, $hostile(Z)$.

- Closed-world assumption (“negation as failure”) e.g., given $alive(X)$ :- not $dead(X)$. $alive(joe)$ succeeds if $dead(joe)$ fails

- Details:

  - Efficient unification by open coding

  - Efficient retrieval of matching clauses by direct linking

  - Depth-first, left-to-right backward chaining

  - Built-in predicates for arithmetic etc., e.g., X is Y*Z+3

14:31

### Prolog examples*

- Depth-first search from a start state X: $dfs(X)$ :- $goal(X)$. $dfs(X)$ :- $successor(X,S)$,$dfs(S)$. No need to loop over S: successor succeeds for each

- Appending two lists to produce a third: $append([],Y,Y)$. $append([X|L],Y,[X|Z])$ :- $append(L,Y,Z)$. query: $append(A,B,[1,2])$ ? answers: A=[] B=[1,2] A=[1] B=[2] A=[1,2] B=[]

14:32

### Conversion to CNF

Everyone who loves all animals is loved by someone:

$$
\forall x [\forall y Animal(y) \Rightarrow Loves(x, y)] \Rightarrow [\exists y Loves(y, x)]
$$

1. Eliminate biconditionals and implications

$$
\forall x [\neg\forall y \neg Animal(y) \lor Loves(x, y)] \lor [\exists y Loves(y, x)] 2. Move \neg inwards: \neg\forall x, p \equiv \exists x \neg p, \neg\exists x, p \equiv \forall x \neg p: \forall x [\exists y \neg(\neg Animal(y) \lor Loves(x, y))] \lor [\exists y Loves(y, x)] \forall x [\exists y \neg\neg Animal(y) \land \neg Loves(x, y)] \lor [\exists y Loves(y, x)] \forall x [\exists y Animal(y) \land \neg Loves(x, y)] \lor [\exists y Loves(y, x)]
$$

14:33

<!-- page: 214 -->
### Conversion to CNF contd.

3. Standardize variables: each quantifier should use a different one

$$
\forall x [\exists y Animal(y) \land \neg Loves(x, y)] \lor [\exists z Loves(z, x)]
$$

4. Skolemize: a more general form of existential instantiation. Each existential variable is replaced by a Skolem function of the enclosing universally quantified variables:

$$
\forall x [Animal(F(x)) \land \neg Loves(x, F(x))] \lor Loves(G(x), x)
$$

5. Drop universal quantifiers:

$$
[Animal(F(x)) \land \neg Loves(x, F(x))] \lor Loves(G(x), x) 6. Distribute \land over \lor: [Animal(F(x)) \lor Loves(G(x), x)] \land [\neg Loves(x, F(x)) \lor Loves(G(x), x)]
$$

14:34

### Resolution: brief summary

- For any substitution θ $unifies(`i, \neg mj)$ for some i and j, apply: `1$\lor$···$\lor$`k, m1$\lor$···$\lor$mn (`1$\lor$···$\lor$`i-1$\lor$`i+1$\lor$···$\lor$`k$\lor$m1$\lor$···$\lor$mj-1$\lor$mj+1$\lor$···$\lor$mn)θ Example: $\neg```text
Rich(x)\lor Unhappy(x)$, $Rich(Ken)Unhappy(Ken)$ with θ = {x/Ken}

- Apply resolution steps to $CNF(KB \land \neg\alpha)$; complete for FOL

14:35

<!-- page: 215 -->
### Example: crime – resolution proof

![Hinh: fig-215-1]

14:36

<!-- page: 216 -->
# 15 Relational Probabilistic Modelling and Learning**

### Motivation & Outline

We’ve learned about FOL and the standard logic inference methods. As I mentioned earlier, I think that the motivation to learn about FOL is less the logic inference methods, but that the FOL formalism can be used to generalize AI methods (Markov-Decision Processes, Reinforcement Learing, Graphical Models, Machine Learning) to relational domains, that is, domains where the state or input is described in terms of properties and relations of objects. As a side note: in the mentioned areas researchers often use the word relational to indicate that a model uses FOL representations. These generalizations are the topic of this lecture. We first consider MDPs and describe STRIPS rules as a relational way to model state transitions for deterministic worlds; then their probabilistic extension called NDRs and how to learn them from data. A core message here is that allowing for probabilities in transition is a crucial pre-requisite to make them learnable—because anything that is learnt from limited data is necessarily also uncertain. We then decribe briefly relational extensions of graphical models, namely Markov
```
Logic Networks (=relational factor graphs), which allow us to formulate probabilistic
```text
models over relational domains, e.g., over data bases, and use probabilistic inference methods to draw conclusions. If time permits, we also mention relational regression trees as a relational extension of standard Machine Learning regression. For brevity we skip the classical AI discussion of the situation calculus and frame problem—please see the AIMA book if you’re interested. 15.1 STRIPS-like rules to model MDP transitions

15:1

### Markov Decision Process

- Let’s recall standard MDPs $a_{0}s_{0}r_{0}a_{1}s_{1}r_{1}a_{2}s_{2}r_{2}$

- Assume the state s is a sentence (or KB) in a FOL. How could we represent transition probabilities $P(s_{0} | s, a)$, rewards $R(s, a)$, and a policy π(s)?? In general that would be very hard!

<!-- page: 217 -->
- We make the simpler assumption that the state s is a conjuction of grounded literals, that is, facts without logic variables, for instance:

  - Constants: C1, C2, P1, P2, SFO, JFK

  - Predicates: $At(., .)$, $Cargo(.)$, $Plane(.)$, $Airport(.)$

  - A state description:
$At(C1, SFO)
```\land$$At(C2, JFK)$$\land$$At(P1, SFO)$$\land$$At(P2, JFK)$$\land$$Cargo(C1)$$\land$$Cargo(C2)$$\land$
$Plane(P1)\land Plane(P2)\land Airport(JFK)\land Airport(SFO)$

15:2

### STRIPS rules and PDDL

![Hinh: fig-217-1]

- STRIPS rules (Stanford Research Institute Problem Solver) are a simple way to describe deterministic transition models. The Planning Domain Definition Language (PDDL) standardizes STRIPS

15:3

### PDDL (or STRIPS)

- The precondition specifies if an action predicate is applicable in a given situation

- The effect determines the changed facts

- Frame assumption: All facts not mentioned in the effect remain unchanged.

- The majority of state-of-the-art AI planners use this format. E.g., FFplan: (B. Nebel, Freiburg) a forward chaining heuristic state space planner

15:4

<!-- page: 218 -->
### Another PDDL example

![Hinh: fig-218-1]

![Hinh: fig-218-2]

15:5

### Decision Making with STRIPS

- A general approach to planning is to query the KB for a plan that fulfills a goal condition; whether this is efficient is debated.

- The standard approach is fwd search:

  - We build a standard decision tree; every node corresponds to a situation

  - When expanding a node we need to compute all feasible actions. This implies to
compute all feasible substitutions of all action preconditions \to  matching problem.

  - This can in principle allow also for rewards and costs; if we have a heuristic we
could use $A^*$

15:6

- STRIPS are nice, intuitive, concise, easy to plan with, and work very well in deterministic domains. But they can’t really be learned. Even in a deterministc world it is very awkward and hard to try to extract deterministic rules from only limited data.

15:7

### Consider data collected by an agent...

[unclear formula]

<!-- page: 219 -->
$grab(c)$ : $box(a)box(b)ball(c)table(d)on(a,b)on(b,d)on(c,d)inhand(nil)$ ...

$$
\to box(a) box(b) ball(c) table(d) on(a,b) on(b,d) \neg on(c,d) inhand(c)
$$

...

$$
puton(a) : box(a) box(b) ball(c) table(d) on(a,b) on(b,d) \neg on(c,d) inhand(c)
$$

...

$$
\to box(a) box(b) ball(c) table(d) on(a,b) on(b,d) on(c,a) inhand(nil)
$$

... $puton(b)$ : $box(a)box(b)ball(c)table(d)on(a,b)on(b,d)on(c,a)inhand(nil)$ ...

$$
\to box(a) box(b) ball(c) table(d) on(a,b) on(b,d) on(c,a) inhand(nil)
$$

... $grab(b)$ : $box(a)box(b)ball(c)table(d)on(a,b)on(b,d)on(c,a)inhand(nil)$ ...

$$
\to box(a) box(b) ball(c) table(d) on(a,d) \neg on(b,d) on(c,d) inhand(b)
$$

... . . . }

- How can we learn a predictive model $P(s_{0} | a, s)$ for this data? With n = 20 objects, state space is > 2n2 ≈ 10120

15:8

### Learning probabilistic rules

Pasula, Zettlemoyer & Kaelbling: Learning probabilistic relational planning rules (ICAPS 2004)

- Compress this data into probabilistic relational rules: $grab(X)$ : $on(X, Y )$, $ball(X)$, $cube(Y )$, $table(Z)$ \to  \begin{cases}  \end{cases} 0.7 : $inhand(X)$, $\neg```text
on(X, Y )$ 0.2 : $on(X, Z)$, $\neg
```on(X, Y )$ 0.1 : noise Find a rule set that maximizes (likelihood - description length)

- These rules define a probabilistic transition probability $P(s_{0} |s, a)$ Namely, if (s, a) has a unique covering rule r, then $P(s_{0} |s, a)$ = $P(s_{0} |s, r)$ = mr X i=0 pr,i $P(s_{0} |\Omega_{r},i, s)$ where $P(s_{0}|\Omega_{r},i, s)$ describes the deterministic state transition of the ith outcome.

15:9

### Role of uncertainty in learning these rules

<!-- page: 220 -->
(b) (a)

```text
\Rightarrow uncertainty \leftrightarrow regularization \leftrightarrow compression & abstraction
```

- Introducing uncertainty in the rules not only allows us to model stochastic worlds, it enables to compress/regularize and thereby learn strongly generalizing models! uncertainty enables learning!

15:10

### Planning with learned probabilistic rules*

![Hinh: fig-220-1]

- Tree search (SST & UCT) does not scale with # objects

- We can propositionalize the learned knowledge into a Dynamic Bayesian Network (DBN): For every domain D they define a grounded DBN (Lang & Toussaint, JAIR 2010)

- Planning (estimating the likelihood of action sequences) can efficiently be done using probabilitic inference methods in this DBN

15:11

switch slides: 12/talk-Stanford ./talk-MIT

15:12

## 15.2 Relational Graphical Models

15:13

### Intro

<!-- page: 221 -->
- Probabilistic relational modelling has been an important development in modern AI. It fuses: Structured first-order (logic) representations (\leftrightarrow  strong generalization)

# +

![Hinh: fig-221-1]

Probabilistic/statistical modelling, inference & learning

- I use the term “Probabilistic relational modelling” for all formalisms of that kind, including Markov Logic Networks, Bayesian Logic Programs, Probabilistic Relational Models, Relational Markov Networks, Relational Probability Trees, Stochastic Logic Programming, ... BLOG

15:14

(from De Readt & Kersting)

15:15

### Intro

- A popular science article: I, algorithm: A new dawn for artificial intelligence (Anil Ananthaswamy, NewScientist, January 2011) Talks of “probabilistic programming, which combines the logical underpinnings of the old AI with the power of statistics and probability.” Cites Stuart Russel as “It’s a natural unification of two of the most powerful theories that have been developed to understand the world and reason about it.” and Josh Tenenbaum as “It’s definitely spring”.

15:16

### Intro

- I think: probabilistic relational modelling does not suddenly solve all problems, but is important because:

<!-- page: 222 -->
  - One of the great deficits of classical AI is the inefficiency of learning (constructing
deterministic knowledge bases from data) – statistical relational approaches do this
the right way

  - The world is structured in terms of objects and their properties and relations – first-
order representations offer a formalization of this structure; we need to such for-
malizations for strong generalization

  - In my view: currently the only way to express & learn uncertain & generalizing
knowledge about environments with objects, properties & relations

15:17

### References

- Pedro Domingos: CIKM-2013 tutorial on Statistical Relational Learning http://homes.cs.washington.edu/˜pedrod/cikm13.html

- Lise Getoor: ECML/PKDD 2007 tutorial on SRL http://www.ecmlpkdd2007.org/CD/tutorials/T3_Getoor/Getoor_CD.pdf (or http://www.cs.purdue.edu/probdb/updb06/UPDB-PRM-09-22-06.ppt

- Survey paper by Luc De Raedt and Kristian Kersting: https://lirias.kuleuven.be/bitstream/123456789/301404/1/pilp.pdf

15:18

### Probabilistic Relational Modelling

- In general, probabilistic relational approaches

  - make predictions based only on the properties/relations of objects, not their identity

  - generalize data seen in one world (with objects A, B, C, ...)
to another world (with objects D, E, ..)

  - thereby imply a very strong type of generalization/prior
which allows to efficiently learn in the exponentially large space

- Formally, they are frameworks that define a probability distribution $P(X; D)$ or discriminative function $F(X; D)$ over $dom(X; D)$, for any domain D where X are the random variables that exist for a given domain D (a given set of objects/constants) [[Inconsistent with previous use of word ’domain’]] (Note, this is a “transdimensional” distribution/discriminative function)

15:19

### Probabilistic Relational Models (PRMs)

- (brief informal intro, from Lise Getoor’s tutorial)

<!-- page: 223 -->
- Consider a relational data base

15:20

### PRM

![Hinh: fig-223-1]

![Hinh: fig-223-2]

- We think of the table attributes as random variables that depend on each other $P(A|Q, M)$ is a conditional probability table, which should be independent of the particular identity (primary key) of the paper and reviewer—A should only depend on the values of Q and M

15:21

### PRM

- In a particular domain D = {A1, A2, P1, P2, P3, R1, R2, R3}, the PRM defines a probability distribution over the instantiations of all attributes (grounded predicates)

<!-- page: 224 -->
15:22

### PRM

![Hinh: fig-224-1]

- Learning PRMs amounts to learning all conditional probability tables from a relational data base

- Inference with PRMs means to construct the big grounded Bayesian Network

  - Each grounded predicate \to  random variable

- PRMs are nice because they draw clear connections to relational databases. But there is a easier/cleaner formulation of such types of models: Markov Logic Networks (MLN).

15:23

### Markov Logic Networks (MLN)

15:24

### MLN example: Friends & Smokers

- Consider three weighted Horn clauses w1 = 1.5, F1 : $cancer(x)$ ← $smoking(x)$ w2 = 1.1, F2 : $smoking(x)$ ← $friends(x, y)\land smoking(y)$ w3 = 1.1, F3 : $smoking(y)$ ← $friends(X, Y )\land smoking(x)$

- Consider the domain D = {Anna, Bob}

- Set of random variables (grounded predicates) becomes: {$cancer(A)$, $cancer(B)$, $smoking(A)$, $smoking(B)$, $friends(A, A)$, $friends(A, B)$, $friends(B, A)$, $friends(B, B)$}

<!-- page: 225 -->
15:25

### MLN

![Hinh: fig-225-1]

- The MLN is defined by a set {(Fi, wi)} of pairs where

  - Fi is a formula in first-order logic

  - wi $\in$ R is a weight

- For a domain D this generates a factor graph with

  - one random variable for each grounded predicate

  - one factor for each grounding of each formula
$F(X, D)$ \propto  exp{
X
i
X
true groudings of Fi in X
wi}

- MLNs can be viewed as a factor graph template

  - For every domain D a grounded factor graph $F(X; D)$ is defined

  - The ground factor graph has many shared parameters \to  learning the weights implies
strong generalization across objects

15:26

### Generality of MLNs

- Special (non-relational) cases: (Limit of all predicates zero-arity)

  - Markov networks

  - Markov random fields

  - Bayesian networks

  - Log-linear models

  - Exponential models

  - Max. entropy models

  - Gibbs distributions

  - Boltzmann machines

  - Logistic regression

<!-- page: 226 -->
  - Hidden Markov models

  - Conditional random fields

- Limit infinite weights \to  first-order logic

15:27

### MLN

- Inference in MLN: Create the grounded factor graph

- Learning: Gradient descent on the likelihood (often hard, even with full data)

- The learned factor graph $F(X; D)$ can also define a discriminative function:

  - Relational logistic regression

  - Relational Conditional Random Fields
(See also Discriminative probabilistic models for relational data, Taskar, Abbeel & Koller; UAI 2002.)

15:28

slides: /git/3rdHand/documents/USTT/17-reviewMeeting3/slides.pdf

15:29

### Conclusions

- What all approaches have in common:

  - A “syntax” for a template that, for every domain D, defines a grounded factor
graph, Bayes Net, or DBN

  - The grounding implies parameter sharing and strong generalization, e.g. over ob-
ject identities

  - Inference, learning & planning often operate on the grounded model

- Using probabilistic modelling, inference and learning on top of first-order representations

15:30

### The role of uncertainty in AI

- What is the benefit of the probabilities in these approaches?

  - Obviously: If the world is stochastic, we’d like to represent this

  - But, at least as important:
Uncertainty enables to compress/regularize and thereby learn strongly

### generalizing models

<!-- page: 227 -->
![Hinh: fig-227-1]

(b) (a)

```text
uncertainty \leftrightarrow regularization \leftrightarrow compression & abstraction
```

- The core problem with deterministic AI is learning deterministic models

15:31

<!-- page: 228 -->
# 16 Exercises

## 16.1 Exercise 1

### 16.1.1 Programmieraufgabe: Tree Search

(The deadline for handing in your solution is Monday 2pm in the week of the tutorials) In the repository you will find the directory e01_graphsearch with a couple of files. First there is ex_graphsearch.py with the boilerplate code for the exercise. The comments in the code define what each function is supposed to do. Implement each function and you are done with the exercise. The second file you will find is tests.py. It consists of tests that check whether your functions do what they should. You don’t have to care about this file, but you can have a look in it to understand the exercise better. The next file is data.py. It consists of a very small graph and the S-Bahn net of Stuttgart as graph structure. It will be used by the test. If you like you can play around with the data in it. The last file is run_tests.sh. It runs the tests, so that you can use the test to check whether you are doing right. Note that our test suite will be different from the one we hand to you. So just mocking each function with the desired output without actually computing it will not work. You can run the tests by executing:

```bash
$ sh run_tests.sh
```

If you are done implementing the exercise simply commit your implementation and push it to our server.

```bash
$ git add ex_graphsearch.py
$ git commit
$ git push
```

Task: Implement breadth-first search, uniform-cost search, limited-depth search, iterative deepening search and A-star as described in the lecture. All methods get as an input a graph, a start state, and a list of goal states. Your methods should return two things: the path from start to goal, and the fringe at the moment when the goal state is found (that latter allows us to check correctness of the implementation). The first return value should be the found Node (which has the path implicitly included through the parent links) and a Queue (one of the following: Queue, LifoQueue, PriorityQueue and NodePriorityQueue) object holding the fringe. You also have to fill in the priority computation at the put() method of the NodePriorityQueue. Iterative Deepening and Depth-limited search are a bit different in that they do not explicitly have a fringe. You don’t have to return a fringe in those cases, of course. Depth-limited search additionally gets a depth limit as input. A-star gets a heuristic

<!-- page: 229 -->
```python
function as input, which you can call like this:
def a_star_search(graph, start, goal, heuristic):
```

# ...

$$
h = heuristic(node.state, goal)
$$

# ...

### Tips:

![Hinh: fig-229-1]

  - For those used to IDEs like Visual Studio or Eclipse: Install PyCharm (Community Edi-
tion). Start it in the git directory. Perhaps set the Keymap to ’Visual Studio’ (which sets
exactly the same keys for running and stepping in the debugger). That’s helping a lot.

  - Use the data structure Node that is provided. It has exactly the attributes mentioned on
slide 26.

  - Maybe you don’t have to implement the ’Tree-Search’ and ’Expand’ methods separately;
you might want to put them in one little routine.
16.1.2 Votieraufgabe: $A^*$
-Suche
Betrachten Sie die Rumänien-Karte aus der Vorlesung:

- Verfolgen Sie den Weg von Lugoj nach Bukarest mittels einer $A^*$ -Suche und verwenden Sie die Luftlinien-Distanz als Heuristik. Geben Sie für jeden Schritt den momentanen Stand der fringe (Rand) an. Nutzen Sie folgende Notation für die fringe: $h(A : 0 + 366 = 366)$(Z : 75 + 374 = 449)i (d.h. (Zustand : g + h = f)).

- Geben Sie den mittels der $A^*$ -Suche gefundenen kürzesten Weg an. 16.1.3 Votieraufgabe: Beispiel für Tiefensuche Betrachten Sie den Zustandsraum, in dem der Startzustand mit der Nummer 1 bezeichnet wird und die Nachfolgerfunktion für Zustand n die Zustände mit den

<!-- page: 230 -->
Nummern 4n - 2, 4n - 1, 4n und 4n + 1 zurück gibt. Nehmen Sie an, dass die hier gegebene Reihenfolge auch genau die Reihenfolge ist, in der die Nachbarn in expand durchlaufen werden und in die LIFO fringe eingetragen werden.

- Zeichnen Sie den Teil des Zustandsraums, der die Zustände 1 bis 21 umfasst.

- Geben Sie die Besuchsreihenfolge (Besuch=[ein Knoten wird aus der fringe genommen, goal-check, und expandiert]) für eine beschränkte Tiefensuche mit Grenze 2 und für eine iterative Tiefensuche, jeweils mit Zielknoten 4, an. Geben Sie nach jedem Besuch eines Knotens den dann aktuellen Inhalt der fringe an. Die initiale fringe ist h1i. Nutzen Sie für jeden Besuch in etwa die Notation: besuchter Zustand: hfringe nach dem Besuchi

- Führt ein endlicher Zustandsraum immer zu einem endlichen Suchbaum? Begründen Sie Ihre Antwort. 16.2 Exercise 2 16.2.1 Programmieraufgabe: Schach Implementieren Sie ein Schach spielendes Programm. Der grundlegende Python code ist dafür in Ihren Repositories. Wir haben auch bereits die Grundstruktur eines UCT Algorithmus implementiert, so dass Sie nur die einzelnen Funktionen implementieren müssen. Die Implementierung von möglichen Erweiterungen steht Ihnen frei. Evaluations-Funktion statt Random Rollouts: Letztes Jahr stellte sich heraus, dass der Erfolg naiver UCT Algorithmen bescheiden ist. Um die Baumsuche deutlich zu vereinfachen kann man die Evaluations-Funktion nutzen, um neue Blätter des Baums zu evaluieren (und den backup zu machen), statt eines random rollouts. Aber: Die Evaluations-Funktion ist deterministisch, und könnte die Suche fehlleiten. Als nächsten Schritt kann man deshalb sehr kurze random rollouts nehmen, die schon nach wenigen Schritten enden und mit der Evaluations-Funktion bewertet werden. Ziel: Wir ’be-punkten’ diese Aufgabe automatisiert indem wir den Schach-Agenten 10 mal gegen einen Random-Spieler antreten lassen. Ziel ist es nach Punkten zu gewinnern. (Sieg - 1 Punkt, Unentschieden - 0.5 Punkte, Niederlage - 0 Punkte). Turnier: Außerdem planen wir alle Schach-Agenten in einem Turnier gegeneinander antreten zu lassen. Das Gewinnerteam darf sich über eine kleine Belohnung freuen!

<!-- page: 231 -->
Ihr Algorithmus soll auf folgendes Interface zugreifen:

```python
class ChessPlayer(object):
def __init__(self, board, player):
```

# The game board is the board at the beginning, player is # either chess.WHITE or chess.BLACK. pass

```python
def inform_move(self, move):
```

# after each move (also your own) this function is called to info # the player of the move played (which can be a different one tha # chose, if you chose a illegal one. pass

```python
def get_next_move(self):
```

# yields the move that you want to play next. pass Sie können Ihre Implementierung testen mit

```bash
$ python2 interface.py --human --white --secs 2
```

um als Mensch gegen Ihren Spieler zu spielen. Oder mit

```bash
$ python2 interface.py --random --white --secs 2
```

um einen zufällig spielenden Spieler gegen ihr Programm antreten zu lassen. 16.2.2 Votieraufgabe: Bayes a) Box 1 contains 8 apples and 4 oranges. Box 2 contains 10 apples and 2 oranges. Boxes are chosen with equal probability. What is the probability of choosing an apple? If an apple is chosen, what is the probability that it came from box 1? b) The blue M&M was introduced in 1995. Before then, the color mix in a bag of plain M&Ms was: 30% Brown, 20% Yellow, 20% Red, 10% Green, 10% Orange, 10% Tan. Afterward it was: 24% Blue , 20% Green, 16% Orange, 14% Yellow, 13% Red, 13% Brown. A friend of mine has two bags of M&Ms, and he tells me that one is from 1994 and one from 1996. He won’t tell me which is which, but he gives me one M&M from each bag. One is yellow and one is green. What is the probability that the yellow M&M came from the 1994 bag? c) The Monty Hall Problem: I have three boxes. In one I put a prize, and two are empty. I then mix up the boxes. You want to pick the box with the prize in it. You

<!-- page: 232 -->
choose one box. I then open another one of the two remaining boxes and show that it is empty. I then give you the chance to change your choice of boxes—should you do so? Please give a rigorous argument using Bayes. d) Given a joint probability $P(X, Y )$ over 2 binary random variables as the table

$$
Y=0 Y=1 X=0 .06 .24 X=1 .14 .56
$$

What are $P(X)$ and $P(Y )$? Are X and Y independent? 16.2.3 Präsenzaufgabe: Bandits Assume you have 3 bandits. You have already tested them a few times and received returns

- From bandit 1: 8 7 12 13 11 9

- From bandit 2: 8 12

- From bandit 3: 5 13 For the returns of each bandit separately, compute a) the mean return, the b) standard deviation of returns, and c) standard deviation of the mean estimator. Which bandid would you choose next? (Distinguish cases: a) if you know this is the last chance to pull a bandit; b) if you will have many more trials thereafter.) 16.3 Exercise 3 16.3.1 Votieraufgabe: Value Iteration (Teilaufgaben werden separat votiert.) 1 7 8 2 6 3 4 5

![Hinh: fig-232-1]

<!-- page: 233 -->
Consider the circle of states above, which depicts the 8 states of an MDP. The green

```text
state (#1) receives a reward of r = 4096 and is a ’tunnel’ state (see below), the red state (#2) is punished with r = -512. Consider a discounting of \gamma = 1/2.
```

Description of $P(s_{0} |s, a)$:

- The agent can choose between two actions: going one step clock-wise or one step counter-clock-wise.

- With probability 3/4 the agent will transition to the desired state, with probability 1/4 to the state in opposite direction.

- Exception: When s = 1 (the green state) the next state will be $s_{0}$ = 4, independent of a. The Markov Decision Process never ends. Description of $R(s, a)$:

- The agent receives a reward of r = 4096 when s = 1 (the green state).

- The agent receives a reward of r = -512 when s = 2 (the red state).

- The agent receives zero reward otherwise. 1. Perform three steps of Value Iteration: Initialize Vk=0(s) = 0, what is Vk=1(s), Vk=2(s), Vk=3(s)? 2. How can you compute the value function V π (s) of a GIVEN policy (e.g., always walk clock-wise) in closed form? Provide an explicit matrix equation. 3. Assume you are given V ∗ (s). How can you compute the optimal Q∗ (s, a) form this? And assume Q∗ (s, a) is given, how can you compute the optimal V ∗ (s) from this? Provide general equations. 4. What is Qk=3(s, a) for the example above? What is the “optimal” policy given Qk=3? 16.3.2 Programmieraufgabe: Value Iteration In the repository you find python code to load the probability table $P(s_{0} |a, s)$ and the reward function $R(a, s)$ for the maze of Exercise 1. In addition, the MDP is defined by γ = 0.5. (a) Implement Value Iteration to reproduce the results of Exercise 1(a). Tip: An easy way to implement this is to iterate the two equations: $Q(s, a)$ ← $R(s, a)$ + γ X $s_{0}P(s_{0} |s, a)$ V ($s_{0}$ ) (20) V (s) ← max a $Q(s, a)$ (21)

<!-- page: 234 -->
$$
Compare with the value functions Vk=1(s), Vk=2(s), Vk=3(s) computed by hand. Also compute the Vk=100 \approx V *
$$

.

$$
(b) Implement Q-Iteration for exactly the same setting. Check that V (s) = maxa Q(s, a)
$$

converges to the same optimal value. WARNING: The test you have in your repository only tests for the specific world of Exercise 1. However, our evaluation will test your method also for other MDPs with other states, actions, rewards, and transitions! Implement general methods. 16.3.3 Präsenzaufgabe: The Tiger Problem Assume that the tiger is truly behind the left door. Consider an agent that always chooses to listen. a) Compute the belief state after each iteration. b) In each iteration, estimate the expected reward of open-left/open-right based only on the current belief state. c) When should the agent stop listening and open a door for a discount factor of

$$
\gamma = 1? (How would this change if there were zero costs for listening?)
$$

## 16.4 Exercise 4

### 16.4.1 Programmieaufgabe: Sarsa vs Q-Learning (vs your Agent)

Consider the following Cliff Walking problem. In your git repo you find an implementation of the Cliff Walking environment. This

$$
is a standard undiscounted (\gamma = 1), episodic task, with start (S) and goal (G) states,
$$

and the actions up, down, left, right causing deterministic movement. The reward is -1 for all transitions except into the region marked The Cliff. Stepping into this region incurs a reward of -100 and sends the agent instantly back to the start. An episode ends when reaching the goal state and NOT when falling down the cliff. Recall: See slide 06:12 for pseudo code of Q-Learning; it updates the Q-function using

$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma max
$$

$a_{0}Qold(s_{0} , a_{0} )$ - $Qold(s, a)$] . SARSA is exactly the same algorithm, except that it updates the Q-function with

$$
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma Q_{old}(s_{0}
$$

, $a_{0}$ ) - $Qold(s, a)$] To implement this SARSA update, you need to sample the next action $a_{0}$ before updating the Q-function. Exercises:

<!-- page: 235 -->
![Hinh: fig-235-1]

Figure 1: Cliffwalk environment and reference plot (smoothed) 1. Implement the SARSA and Q-learning methods using the -greedy action se-

$$
lection strategy with a fixed = 0.1. Choose a small learning rate \alpha = 0.1.
$$

Compare the resulting policies when greedily selecting actions based on the learned Q-tables. To compare the agents’ online performance run them for at least 500 episodes and log the reward per episode in a numpy array. Plot your logged data with episodes as x-axis and reward per episode as y-axis. Export the logged reward array for Q-Leaning and Sarsa to R ql.csv and R sa.csv respectively. See below on how to plot using python.

$$
2. Propose a schedule that gradually reduces , starting from = 1. Then redo
$$

question 1 using your schedule for instead of the fixed value. Again plot the learning graph and export your logged rewards per episode to R ql sched.csv and R sa sched.csv respectively. 3. In the lectures we introduced Rmax, which is a model-based approach. Here we consider a simplified model-free Rmax-variant working with Q-Learning: Implement standard Q-learning using greedy action selection but a modified

$$
reward function. The modified reward function assigns rmax = 0 to unknown
$$

states (#(s, a) < 100) and the original reward for known states. Plot and export your rewards per episode to R rmax.csv.

<!-- page: 236 -->
### Be sure to upload your code and all your csv files containing the rewards per

### episode. The evaluation is based on these files.

### For each exercise get an understanding for the agent’s online behavior and their

### learned policies. Be ready to explain in class!

The following example shows how to plot and export data contained in a numpy array. This is all you need to create the plots and generate the csv files for the above exercises.

```python
import numpy as np
import matplotlib.pyplot as plt
Y = np.array([5, 8, 1, 4])
```

# Export to CSV np.$savetxt(Y, ’Y.csv’)$ # Plot and display plt.$plot(Y)$ plt.show() Note: The graph may be very spiky so it might be a good idea to smooth your plot before comparing it with the graph given above, e.g. by using the simple box filter provided in the code. However you have to export and hand in the un-smoothed version. 16.4.2 Votieraufgabe: Eligibilities in TD-learning Consider TD-learning in the same maze as in the previous exercise 1 (Value Iteration), where the agent starts in state 4, and action outcomes are stochastic. Describe at what events plain TD-learning will update the value function, how it will update it. Assuming the agent always takes clock-wise actions, guess roughly how many steps the agent will have taken when for the first time V ($s_{4}$) becomes non-zero. How would this be different for eligibility traces? 16.5 Exercise 5 16.5.1 Programmieraufgabe: Constrained Satisfaction Problems Pull the current exercise from our server to your local repository.

<!-- page: 237 -->
Task 1: Implement backtracking for the constrained satisfaction problem definition you find in csp.py. Make three different versions of it 1) without any heuristic 2) with minimal remaining value as heuristic but without tie-breaker (take the first best solution) 3) with minimal remaining value and the degree heuristic as tie-breaker. Optional: Implement AC-3 or any approximate form of constraint propagation and activate it if the according parameter is set. Task 2: Implement a method to convert a Sudoku into a csp.ConstrainedSatisfactio and then use this to solve the sudoku given as a numpy array. Every empty field is set to 0. The CSP you create should cover all rules of a Sudoku, which are (from http://en.wikipedia.org/wiki/Sudoku): Fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid (also called ’blocks’) contains all of the digits from 1 to 9. In the lecture we mentioned the all different constraint for columns, rows, and blocks. As the csp.ConstrainedSatisfactionProblem only allows you to represent pairwise unequal constraints (to facilitate constraint propagation) you need to convert this. 16.5.2 Votieraufgabe: CSP Betrachten Sie folgenden Kartenausschnitt:

![Hinh: fig-237-1]

<!-- page: 238 -->
Der Kartenausschnitt soll mit insgesamt 4 Farben so eingef”arbt werden, dass je zwei Nachbarl”ander verschiedene Farben besitzen. Mit welchem Land w”urde man am ehesten beginnen? F”arben Sie das erste Land ein und wenden Sie durchgehend Constraint Propagation an. 16.5.3 Präsenzaufgabe: Generalized Arc Consistency We have n variables xi, each with the (current) domain Di. Constraint propagation by establishing local constraint consistency (“arc consistency”) in general means the following: For a variable xi and an adjacent constraint Ck, we delete all values v from Di for

$$
which there exists no tuple \tau \in DIk with \tau_i = v that satisfies the constraint.
$$

Consider a simple example

$$
x_{1}, x_{2} \in {1, 2} , x_{3}, x_{4} \in {2, .., 6} , c = AllDiff(x_{1}, .., x_{4})
$$

(a) How does constraint propagation from c to $x_{3}$ update the domain D3? (b) On http://norvig.com/sudoku.html Norvig describes his Sudoku solver, using the following rules for constraint propagation: (1) If a square has only one possible value, then eliminate that value from the square’s peers. (2) If a unit (block, row or column) has only one possible place for a value, then put the value there.

![Hinh: fig-238-1]

<!-- page: 239 -->
Is this a general implementation of constraint propagation for the allDiff constraint? Note: The generalized arc consistency is equivalent so-called message passing (or belief propagation) in probabilistic networks, except that the messages are domain sets instead of belief vectors. See also www.lirmm.fr/˜bessiere/stock/TR06020.pdf 16.6 Exercise 6 16.6.1 Programmieraufgabe: Spamfilter mit Naive Bayes Sie haben in der Vorlesung grafische Modelle und Inferenz in ihnen kennengelernt. Auf dieser Grundlage basiert der viel verwendete Naive Bayes Klassifikator. Der Bayes Klassifikator wird zum Beispiel dafür verwandet, Spam Emails automatisch zu erkennen. Dafür werden Trainings-Emails untersucht und die Wahrscheinlichkeit des Auftreten eines Wortes bestimmt, abhängig davon, ob es eine Spamoder Ham-Email ist.

$$
Sei c \in {Spam, Ham} die binäre Zufallsvariable, die angibt, ob es sich bei einer
$$

Email um Spam oder Ham handelt. Sei xi das ite Wort einer Email X. Sei $p(x|c)$ die Wahrscheinlichkeit, dass ein Wort x in einer Spambzw. Ham-Email vorkommt, die während des Trainings für jedes mögliche Wort bestimmt wurde. Dann berechnet der Naive-Bayes-Klassifikator

$$
p(c, X) = p(c)
$$

D Y

$$
i=1
$$

$p(x_i|c)$

$$
p(c | X) =
$$

$p(c, X)p(X)$

$$
=
$$

$p(c, X)$ P c $p(c, X)$ als die Wahrscheinlichkeit, dass die Email X Spam oder Ham ist, wobei D die Zahl der Wörter xi in der Email X ist. (In praktischen Implementierungen werden häufig nur Wörter berücksichtigt, bei denen $p(x|Spam)$ und $p(x|Ham)$ nicht Null sind.) Aufgabe: Implementieren Sie einen Naive Bayes Klassifikator für die Spam-Emails. Sie finden Trainingsdaten und Python-Code, der mit diesen umgehen kann, in Ihrem Repository. Ihre Implementierung sollte zwei Funktionen enthalten:

```python
class NaiveBayes(object):
def train(self, database):
```

’’’ Train the classificator with the given database. ’’’

<!-- page: 240 -->
pass

```python
def spam_prob(self, email):
```

’’’ Compute the probability for the given email that it is return 0. Tip: David Barber gibt ein seinem Buch “Bayesian Reasoning and Machine Learning” eine sehr gute Einführung in den Naive Bayes Klassifikator (Seite 243 ff., bzw. Seite 233 ff. in der kostenlosen Online Version des Buches, die man unter http:// www.cs.ucl.ac.uk/staff/d.barber/brml/ herunterladen kann). Zudem: Log-Wahrscheinlichkeiten zu addieren ist eine numerisch stabile Alternative zum Multiplizieren von Wahrscheinlichkeiten. 16.6.2 Votieraufgabe: Hidden Markov Modelle (Teilaufgaben werden separat votiert.) Sie stehen bei Nacht auf einer Br”ucke ”uber der B14 in Stuttgart und m”ochten z”ahlen, wieviele LKW, Busse und Kleintransporter in Richtung Bad Canstatt fahren. Da Sie mehrere Spuren gleichzeitig beobachten und es dunkel ist machen Sie folgende Fehler bei der Beobachtung des Verkehrs:

- Einen LKW erkennen Sie in 30% der F”alle als Bus, in 10% der F”alle als Kleintransporter.

- Einen Bus erkennen Sie in 40% der F”alle als LKW, in 10% der F”alle als Kleintransporter.

- Einen Kleintransporter erkennen Sie in je 10% der F”alle als Bus bzw. LKW. Zudem nehmen Sie folgendes an:

- Auf einen Bus folgt zu 10% ein Bus und zu 30% ein LKW, ansonsten ein Kleintransporter.

- Auf einen LKW folgt zu 60% ein Kleintransporter und zu 30% ein Bus, ansonsten ein weiterer LKW.

- Auf einen Kleintransporter folgt zu 80% ein Kleintransporter und zu je 10% ein Bus bzw. ein LKW. Sie wissen sicher, dass das erste beobachtete Fahrzeug tatsächlich ein Kleintransporter ist. a) Formulieren Sie das HMM dieses Szenarios. D.h., geben Sie explizit $P(X1)$, $P(Xt+1|Xt)$ und $P(Yt|Xt)$ an.

<!-- page: 241 -->
b) Prädiktion: Was ist die Marginal-Verteilung $P(X3)$ über das 3. Fahrzeug.

$$
c) Filtern: Sie machten die Beobachtungen Y_{1:3} = (K, B, B). Was ist die Wahrschein-
$$

lichkeit $P(X3|Y_{1:3})$ des 3. Fahrzeugs gegeben diese Beobachtungen? d) Glätten: Was ist die Wahrscheinlichkeit $P(X2|Y_{1:3})$ des 2. Fahrzeugs, gegeben die 3 Beobachtungen? e) Viterbi (wahrscheinlichste Folge): Was ist die wahrscheinlichste Folge argmaxX1:3 $P(X_{1:3}|Y_{1:3})$ an Fahrzeugen, gegeben die 3 Beobachtungen? 16.7 Exercise 7 Die Lösungen bitte als python-Datei (siehe Vorlage in der Email/Website) mit dem Namen e07/e07_sol.py (in Verzeichnis e07) in Euer git account einloggen. In der python-Datei wird das Format, in dem Antworten gegeben werden sollen, genauer erklärt. Bei Unklarheiten bitte bei dem Tutor melden. Diese letzte Übung zählt zu den Programmieraufgaben. Dies ist keine Bonusaufgabe. Präsenzund Votieraufgaben gibt es nicht mehr. Abgabe bis Montag, 20. Februar. 16.7.1 Erfüllbarkeit und allgemeine Gültigkeit (Aussagenlogik) (30%) Entscheiden Sie, ob die folgenden S”atze erf”ullbar (satisfiable), allgemein g”ultig (valid) oder keins von beidem (none) sind.

$$
(a) Smoke \Rightarrow Smoke (b) Smoke \Rightarrow Fire (c) (Smoke \Rightarrow Fire) \Rightarrow (\neg Smoke \Rightarrow \neg Fire) (d) Smoke \lor Fire \lor \neg Fire (e) ((Smoke \land Heat) \Rightarrow Fire) \Leftrightarrow ((Smoke \Rightarrow Fire) \lor (Heat \Rightarrow Fire)) (f) (Smoke \Rightarrow Fire) \Rightarrow ((Smoke \land Heat) \Rightarrow Fire) (g) Big \lor Dumb \lor (Big \Rightarrow Dumb) (h) (Big \land Dumb) \lor \neg Dumb
$$

<!-- page: 242 -->
### 16.7.2 Modelle enumerieren (Aussagenlogik) (30%)

Betrachten Sie die Aussagenlogik mit Symbolen A, B, C und D. Insgesamt existieren also 16 Modelle. In wievielen Modellen sind die folgenden S”atze erf”ullt?

$$
1. (A \land B) \lor (B \land C) 2. A \lor B 3. A \Leftrightarrow (B \Leftrightarrow C)
$$

### 16.7.3 Unifikation (Prädikatenlogik) (40%)

Geben Sie f”ur jedes Paar von atomaren S”atzen den allgemeinsten Unifikator an, sofern er existiert. Standardisieren Sie nicht weiter. Geben Sie None zurück, wenn kein Unifikator existiert. Ansonsten ein Dictioary, dass als Key die Variable und als Value die Konstante enthält.

$$
Für P(A), P(x): sol3z = {’x’: ’A’}
$$

1. $P(A, B, B)$, $P(x, y, z)$. 2. Q(y, $G(A, B)$), Q($G(x, x)$, y). 3. Older($Father(y)$, y), Older($Father(x)$, John). 4. Knows($Father(y)$, y), $Knows(x, x)$. 16.7.4 Privat-Spaß-Aufgabe: as Constraint Satisfaction Problem Consider the Generalized Modus Ponens (slide 09:15) for inference (forward and backward chaining) in first order logic. Applying this inference rule requires to find a substitution θ such that p0

$$
i\theta = pi\theta for all i.
$$

Show constructively that the problem of finding a substitution θ (also called matching problem) is equivalent to a Constraint Satisfaction Problem. “Constructively” means, explicitly construct/define a CSP that is equivalent to the matching problem. Note: The PDDL language to describe agent planning problems (slide 08:24) is similar to a knowledge in Horn form. Checking whether the action preconditions hold in a given situation is exactly the matching problem; applying the Generalized Modus Ponens corresponds to the application of the action rule on the current situation.

<!-- page: 243 -->
### 16.7.5 Privat-Spaß-Aufgabe

In the lecture we discussed the case “A first cousin is a child of a parent’s sibling”

$$
\forall x, y FirstCousin(x, y) \Leftarrow\Rightarrow \exists p, z Parent(p, x) \land Sibling(z, p) \land Parent(z, y)
$$

A question is whether this is equivalent to

$$
\forall x, y, p, z FirstCousin(x, y) \Leftarrow\Rightarrow Parent(p, x) \land Sibling(z, p) \land Parent(z, y)
$$

Let’s simplify: Show that the following two

$$
\forall x A(x) \Leftarrow\Rightarrow \exists y B(y, x) (22) \forall x, y A(x) \Leftarrow\Rightarrow B(y, x) (23)
$$

are different. For this, bring both sentences in CNF as described on slides 09:21 and 09:22 of lecture 09-FOLinference. 16.8 Exercise 9 Dieses Blatt enthält Präsenzübungen, die am 26.01. in der Übungsgruppe besprochen werden und auch zur Klausurvorbereitung dienen. Sie sind nicht abzugeben. Studenten werden zufällig gebeten, sich an den Aufgaben zu versuchen. 16.8.1 Präsenzaufgabe: Hidden Markov Modelle Sie stehen bei Nacht auf einer Br”ucke ”uber der B14 in Stuttgart und m”ochten z”ahlen, wieviele LKW, Busse und Kleintransporter in Richtung Bad Canstatt fahren. Da Sie mehrere Spuren gleichzeitig beobachten und es dunkel ist machen Sie folgende Fehler bei der Beobachtung des Verkehrs:

- Einen LKW erkennen Sie in 30% der F”alle als Bus, in 10% der F”alle als Kleintransporter.

- Einen Bus erkennen Sie in 40% der F”alle als LKW, in 10% der F”alle als Kleintransporter.

- Einen Kleintransporter erkennen Sie in je 10% der F”alle als Bus bzw. LKW. Zudem nehmen Sie folgendes an:

<!-- page: 244 -->
- Auf einen Bus folgt zu 10% ein Bus und zu 30% ein LKW, ansonsten ein Kleintransporter.

- Auf einen LKW folgt zu 60% ein Kleintransporter und zu 30% ein Bus, ansonsten ein weiterer LKW.

- Auf einen Kleintransporter folgt zu 80% ein Kleintransporter und zu je 10% ein Bus bzw. ein LKW. Sie wissen sicher, dass das erste beobachtete Fahrzeug tatsächlich ein Kleintransporter ist. a) Formulieren Sie das HMM dieses Szenarios. D.h., geben Sie explizit $P(X1)$, $P(Xt+1|Xt)$ und $P(Yt|Xt)$ an. b) Prädiktion: Was ist die Marginal-Verteilung $P(X3)$ über das 3. Fahrzeug. c) Filtern: Sie machten die Beobachtungen $Y1$:3 = (K, B, B). Was ist die Wahrscheinlichkeit $P(X3|Y_{1:3})$ des 3. Fahrzeugs gegeben diese Beobachtungen? d) Glätten: Was ist die Wahrscheinlichkeit $P(X2|Y_{1:3})$ des 2. Fahrzeugs, gegeben die 3 Beobachtungen? e) Viterbi (wahrscheinlichste Folge): Was ist die wahrscheinlichste Folge argmaxX1:3 P($X1$:3 an Fahrzeugen, gegeben die 3 Beobachtungen? 16.9 Exercise 7 Dieses Blatt enthält Präsenzübungen, die am 12.01. in der Übungsgruppe besprochen werden und auch zur Klausurvorbereitung dienen. Sie sind nicht abzugeben. Studenten werden zufällig gebeten, sich an den Aufgaben zu versuchen. 16.9.1 Präsenzaufgabe: Bedingte Wahrscheinlichkeit 1. Die Wahrscheinlichkeit, an der bestimmten tropischen Krankheit zu erkranken, betr”agt 0,02%. Ein Test, der bestimmt, ob man erkrankt ist, ist in 99,995% der F”alle korrekt. Wie hoch ist die Wahrscheinlichkeit, tats”achlich an der Krankheit zu leiden, wenn der Test positiv ausf”allt? 2. Eine andere seltene Krankheit betrifft 0,005% aller Menschen. Ein entsprechender Test ist in 99,99% der F”alle korrekt. Mit welcher Wahrscheinlichkeit ist man bei positivem Testergebnis von der Krankheit betroffen? 3. Es gibt einen neuen Test f”ur die Krankheit aus b), der in 99,995% der F”alle korrekt ist. Wie hoch ist hier die Wahrscheinlichkeit, erkrankt zu sein, wenn der Test positiv ausf”allt?

<!-- page: 245 -->
### 16.9.2 Präsenzaufgabe: Bandits

Assume you have 3 bandits. You have already tested them a few times and received returns

- From bandit 1: 8 7 12 13 11 9

- From bandit 2: 8 12

- From bandit 3: 5 13 For the returns of each bandit separately, compute a) the mean return, the b) standard deviation of returns, and c) standard deviation of the mean estimator. Which bandid would you choose next? (Distinguish cases: a) if you know this is the last chance to pull a bandit; b) if you will have many more trials thereafter.)

<!-- page: 246 -->
# Index

$A^*$search (2:31), $A^*$: Proof 1 of Optimality (2:33), $A^*$: Proof 2 of Optimality (2:35),

Active Learning (4:50), Admissible heuristics (2:37), Alpha-Beta Pruning (4:32),

Backtracking (8:10), Backward Chaining (13:28), Backward Chaining (14:27), Bayes’ Theorem (3:13), Bayesian Network (9:5), Bayesian RL (6:35), Belief propagation (9:32), Bellman optimality equation (5:10), Bernoulli and Binomial distributions (3:16),

Best-first Search (2:29), Beta (3:17), Breadth-first search (BFS) (2:15),

Completeness of Forward Chaining (13:27),

Complexity of BFS (2:16), Complexity of DFS (2:19), Complexity of Iterative Deepening Search (2:23), Complexity of $A^*$(2:34), Conditional distribution (3:11), Conditional independence in a Bayes Net (9:8), Conditional random field (9:43), Conjugate priors (3:25), Conjunctive Normal Form (13:31), Constraint propagation (8:18), Constraint satisfaction problems (CSPs): Definition (8:3), Control (7:21), Conversion to CNF (13:32), Conversion to CNF (14:33),

Dec-POMDP (7:20),

Definitions based on sets (3:8), Depth-first search (DFS) (2:18), Dirac distribution (3:28), Dirichlet (3:21),

Eligibility traces (6:15), Entropy (3:37), Epsilon-greedy exploration in Q-learning (6:31), Evaluation functions (4:37), Example: Romania (2:3), Existential quantification (14:6), Exploration, Exploitation (4:7),

Factor graph (9:26), Filtering, Smoothing, Prediction (10:3),

FOL: Syntax (14:4), Forward Chaining (14:21), Forward chaining (13:24), Frequentist vs Bayesian (3:6),

Gaussian (3:29), Generalized Modus Ponens (14:20), Gibbs Sampling (9:50), Global Optimization (4:43), GP-UCB (4:46), Graph search and repeated states (2:25),

Hidden Markov Model (10:2), HMM inference (10:5), HMM: Inference (10:4), Horn Form (13:23),

Imitation Learning (6:43), Importance Sampling (9:48), Importance sampling (3:42), Inference (13:19), Inference (8:2), Inference in graphical models: overview (9:22), Inference: general meaning (3:5),

<!-- page: 247 -->
Inference: general meaning (9:13), Inverse RL (6:46), Iterative deepening search (2:21),

Joint distribution (3:11), Junction tree algorithm** (9:38),

Kalman filter (10:8), Knowledge base: Definition (13:3), Kullback-Leibler divergence (3:38),

Learning probabilistic rules (15:9), Logic: Definition, Syntax, Semantics (13:7),

Logical equivalence (13:12), Loopy belief propagation (9:36),

Map-Coloring Problem (8:4), Marginal (3:11), Markov Decision Process (5:3), Markov Decision Process (MDP) (15:2),

Markov Logic Networks (MLNs) (15:24),

Markov Process (10:1), Maximum a-posteriori (MAP) inference (9:42), MCTS for POMDPs (4:20), Memory-bounded $A^*$(2:40), Message passing (9:32), Minimax (4:29), Model-based RL (6:28), Modus Ponens (13:23), Monte Carlo (9:45), Monte Carlo methods (3:40), Monte Carlo Tree Search (MCTS) (4:14),

Multi-armed Bandits (4:2), Multinomial (3:20), Multiple RVs, conditional independence (3:14),

Neural networks (11:8), Noisy Deictic Rules (7:9), Nono, 207

Optimistic heuristics (6:36),

Particle approximation of a distribution (3:33), PDDL (7:6), Planning Domain Definition Language (PDDL) (15:3), Planning with probabilistic rules (15:11),

Policy gradients (6:41), POMDP (7:11), Probabilistic Relational Models (PRMs) (15:20), Probabilities as (subjective) information calculus (3:2), Probability distribution (3:10), Problem Definition: Deterministic, fully observable (2:5), Proof of convergence of Q-Iteration (5:15),

Proof of convergence of Q-learning (6:12),

Propositional logic: Semantics (13:10),

Propositional logic: Syntax (13:9),

Q-Function (5:13), Q-Iteration (5:14), Q-learning (6:10),

R-Max (6:33), Random variables (3:9), Reduction to propositional inference (14:16),

Rejection sampling (3:41), Rejection sampling (9:46), Resolution (13:31), Resolution (14:35),

STRIPS rules (15:3), Student’s t, Exponential, Laplace, Chi- squared, Gamma distributions (3:44),

Temporal difference (TD) (6:10),

<!-- page: 248 -->
The role of uncertainty in AI (15:31),

Tree search implementation: states vs nodes (2:11), Tree Search: General Algorithm (2:12),

Tree-structured CSPs (8:25),

UCT for games (4:38), Unification (14:19), Uniform-cost search (2:17), Universal quantification (14:6), Upper Confidence Bound (UCB1) (4:8),

Upper Confidence Tree (UCT) (4:19),

Utilities and Decision Theory (3:36),

Value Function (5:6), Value Iteration (5:12), Value order: Least constraining value (8:17), Variable elimination (9:23), Variable order: Degree heuristic (8:16),

Variable order: Minimum remaining val- ues (8:15),

Wumpus World example (13:4),