<!-- page: 1 -->

# 6.825 Recitation Problems: Spring Final

Solutions

December 13, 2001

## 1 Gaussian Units

You were not responsible for this problem.

## 2 Network Structure

Nodes A and B have no parents.

Node C has two parents: A and B

Node D has one parent: C

## 3 At the Races

1. You should bet on Bell. The expected value is \$0.40.

2. You should take the \$2 insurance and bet on Belle. The expected value is \$1.7.

## 4 Still At The Races

Nodes F and H have no parents.

Node W has two parents: H and F.

Node B has one parent: H

Node T has one parent: B

$$
P (W) = \Sigma_ {F, H} P (W | F, H) P (F) P (H)
$$

$$
\begin{array}{r c l} P (W | T) & = & \frac {P (W , T)}{P (T)} \\ & = & \frac {\Sigma_ {B , H , F} P (W | H , F) P (H) P (F) P (T | B) P (B | H)}{\Sigma_ {B , H} P (T | B) P (B | H) P (H)} \end{array}
$$

## 5 Logic

1. $\forall x . B ( x ) \land H ( x ) \to S ( x )$

2. $\forall x . S ( x ) \land H ( x ) \rightarrow B ( x )$

3. $\forall x . S ( x ) \to B ( x ) \land H ( x )$

4. $\exists x . S ( x ) \land H ( x ) \land B ( x )$

$$
\exists x. H (x) \land B (x) \land \forall y. (x \neq y \land H (x) \rightarrow S l o w e r (x, y))
$$

6. ∀ $r . R ( r ) \rightarrow \exists x . W ( x , r )$

<!-- page: 2 -->

## 6 Clausal Form

¬o(r) ∨ w(f(r))

## 7 Logic

p(b) = false

And one (or both) of p(a) and p(c) is true.

So any of the following three would work

p(a) = false; p(b) = false; p(c) = true

## 8 Bayesian Network Structure

• No

• Yes

• Yes

• No

Remove node G.

Now node I has parents E, F, H.

Node H has parent, E, F.

## 9 True and False

1. False

2. True

3. True

4. False

5. False

6. False

7. True

8. False
