<!-- page: 1 -->

1. 10 = 2, 2, 2, 2, 2 = 10

2. 6 (FOL semantics 1 each)

3. 6 (interpretation 2 each)

4. 6 (unification 2 each)

5. 6 (clausal form 2 each)

6. 6 (operator descriptions 3 each)

7. 13 (graph plan)

8. 8 (conditional prob: 2 each)

9. 12 (network structures: 1/2 each)

10. 4 (counting parameters: 1 each)

11. 5 = 2, 3 = 5 (variable elim)

12. 2 (1 each) (param est)

13. 13 = 2, 2, 4, 4, 1 = 13 (Decision trees)

14. 10 (MDP: 2 each)

15. 9 (Neural net: 1 each)

16. 14 (True/False: 1 each)

Total 130

## 1 Search

a. Your current location and number of passengers in the car.

b. Distance traveled so far.

c. Current location, the number of passengers in the car, and the fares of the passengers you have in the car.

d. Some constant $c _ { 1 }$ times the distance traveled so far minus some other constant $c _ { 2 }$ times the fares of the passengers we’ve picked up so far.

e. UCS will work in the first case, because there are no negative costs, but it’s not guaranteed to find the shortest path in the second version of the problem.

<!-- page: 2 -->

## 2 FOL Semantics

a. T

b. F

c. F

d. T

e. F

f. T

## 3 Interpretations

a. $I ( p ) = \{ \mathbf { A } \}$

$I ( q ) = \{ \mathbf { C } \}$

$I ( r ) = \{ \langle \mathbf { A } , \mathbf { B } \rangle \}$

b. $I ( p ) = \{ \mathbf { B } , \mathbf { C } \}$

$I ( r ) = \{ \langle \mathbf { A } , \mathbf { B } \rangle , \langle \mathbf { B } , \mathbf { B } \rangle , \langle \mathbf { C } , \mathbf { C } \rangle \}$

c. $I ( p ) = \{ \mathbf { A } \}$

$I ( r ) = \{ \langle \mathbf { A } , \mathbf { A } \rangle , \langle \mathbf { B } , \mathbf { A } \rangle , \langle \mathbf { C } , \mathbf { A } \rangle \}$

## 4 Unification

a. $\{ z / f ( x ) , y / g ( w ) \}$

b. not unifiable

c. $\{ a / f ( x ) , x / C , y / f ( x ) \}$

## 5 Clausal Form

a. $r(f(y),y) \lor s(f(y),y)$

b. $\neg r ( x , y ) \lor p ( y )$

c. $\neg r(f(y),y) \lor p(f(y))$

## 6 Operator Descriptions

a. ∀s.on(s) → off (result(push(s))) and ∀s.off (s) → on(result(push(s)))

b. (Pre: on, Eff: off, ¬ on) and (Pre: off, Eff: on, ¬ off)

<!-- page: 3 -->

## 7 Operator Descriptions

• Level 0: not have-keys, not open, not painted.

• Level 1: getkeys, paint

• Level 2: not have-keys not open, not painted, have-keys, painted

• Level 3: getkeys, paint, open

• Level 4: not have-keys, not open, not painted, have-keys, painted, open

## 8 Conditional Probability

a. $\operatorname* { P r } ( a | c , d ) ,   \operatorname* { P r } ( b | c , d )$

b. $\operatorname* { P r } ( c | a , b ) ,   \operatorname* { P r } ( d | a , b ) ,   \operatorname* { P r } ( a , b ) ,   \operatorname* { P r } ( c , d )$

c. none

d. $\operatorname* { P r } ( a | d ) ,   \operatorname* { P r } ( b | d )$

## 9 Network Structures

a. G2

b. none

c. G3, G4

d. none

e. G2, G3

f. G1, G2, G4

## 10 Counting Parameters

a. G1. 9

b. G2. 11

c. G3. 8

d. G4. 7

<!-- page: 4 -->

## 11 Variable Elimination

b. B, C, D, E, F, A, G

## 12 Parameter Estimation

a. 2/3

b. 3/5

## 13 Decision Theory

a. ((ski (.08 win not-broken 100) (.02 win broken 50) (.72 not-win not-broken 0) (.18 not-win broken -50)) (not-ski (.2 broken -10) (.8 not-broken 0))

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
b. $\mathrm{U}(\mathrm{ski}) = 8 + 1 + 0 + -9 = 0$; $\mathrm{U}(\mathrm{not~ski}) = -2$; so we ski!
</div>

c. Given perfect info about my leg, we have the tree ((0.2 broken ((ski (.1 win 50) (.9 not-win -50)) (not-ski -10))) (0.8 not-broken ((ski (.1 win 100) (.9 not-win 0)) (not-ski 0)))) which evaluates to ((0.2 broken ((ski -40) (not-ski -10))) (0.8 not-broken ((ski 10) (not-ski 0))) ((0.2 broken -10) (0.8 not-broken 10)) With perfect information I have expected utility -2 + 8 = 6. So expected value of perfect info is 6 - 0 = 6.

d. Given perfect info about winning the race, we have the tree ((0.1 win ((ski (.2 broken 50) (.8 not-broken 100)) (not-ski (.2 broken -10) (.8 not-broken 0)))) (0.9 not-win ((ski (.2 broken -50) (.8 not-broken 0)) (not-ski (.2 broken -10) (.8 not-broken 0))))) which evaluates to ((0.1 win ((ski 90) (not-ski -2)) (0.9 not-win ((ski -10) (not-ski -2)))) which evaluates to ((0.1 win 90) (0.9 not-win -2)) = 9 - 1.8 = 7.2. So expected value of perfect info is 7.2 - 0 = 7.2.

e. Yes. You just put the win branch after the broken branch, and use the conditional probabilities for win given broken.

## 14 Markov Decision Processes

<div class="docvortex-algorithm" style="white-space: pre-wrap; font-family:monospace;">
a. $\mathrm{V(s1)} = .9^{*}.9^{*}5.5 = 4.455$  
b. $\mathrm{V(s2)} = 5.5$  
c. $\mathrm{V(s3)} = 4.5$  
d. $\mathrm{V(s4)} = 0$  
e. $\mathrm{V(s5)} = 10$
</div>

<!-- page: 5 -->

- 15 Neural Networks
- a. F
- b. T
- c. F
- d. T
- e. F
- f. F
- g. F
- h. F
- i. F
- 16 True or False
- 1. T
- 2. F
- 3. T
- 4. F
- 5. T
- 6. F
- 7. T
- 8. F
- 9. F
- 10. F
- 11. T
- 12. F
- 13. T
- 14. F
