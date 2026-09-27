<!-- page: 1 -->

[FIGURE: Logo PSL Université]

THÈSE DE DOCTORAT DE L'UNIVERSITÉ PSL

Préparée à l'École Normale Supérieure

# From Weakly Supervised Learning to Active Labeling

Soutenue par
Vivien Cabannes
Le 18/07/2022

École doctorale no386
Science Mathématiques

Spécialité
Apprentissage Statistique

Composition du jury :

| Membre | Affiliation | Rôle |
|---|---|---|
| Marc Lelarge | INRIA / DI ENS / PSL | Président |
| Eyke Hüllermeier | Paderborn University | Rapporteur |
| Guillaume Lecué | ENSAE | Rapporteur |
| Joan Bruna | NYU | Examinateur |
| Francis Bach | INRIA / DI ENS / PSL | Directeur de thèse |
| Alessandro Rudi | INRIA / DI ENS / PSL | Directeur de thèse |

[FIGURE: Logo ENS]

[FIGURE: Logo PSL]

[FIGURE: Logo Inria]

<!-- page: 2 -->

<!-- page: 3 -->

*À Kwama,*

<!-- page: 4 -->

```
@PhDThesis{Cabannes2022,
author
= {Vivien Cabannes},
title
= {From Weakly Supervised Learning to Active Labeling},
year
= 2022,
school
= {\’Ecole Normale Sup\’erieure},
type
= {PhD Thesis}
}
```

<!-- page: 5 -->

# Contents

1

Forewords

7

1.1

Acknowledgement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

7

1.2

Summary of contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

8

1.3

Research chronology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9

I

Introduction

13

2

The Machine Learning Paradigm

15

2.1

From algorithmics to machine learning . . . . . . . . . . . . . . . . . . . . . . . . . . . .

15

2.2

The emergence of statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

16

2.3

A tour of problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

20

2.4

A tour of models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

22

2.5

The practice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

26

3

Learning Rates with Discrete Outputs

29

3.1

Statistical learning theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

29

3.2

Surrogate methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

31

3.3

Fast rates derivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

32

3.4

Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

33

4

Partially Supervised Learning

35

4.1

Navigating frameworks of weakly supervised learning . . . . . . . . . . . . . . . . . . . .

35

4.2

The importance to create consensus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

36

4.3

Label disambiguation to complete supervision . . . . . . . . . . . . . . . . . . . . . . . .

38

4.4

Leveraging input structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

40

4.5

Active labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

41

II

Considerations on Learning Theory

43

5

Fast Rates for Structured Prediction

45

5.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

45

5.2

Structured prediction with surrogate control . . . . . . . . . . . . . . . . . . . . . . . . .

47

5.3

Rate acceleration under margin condition . . . . . . . . . . . . . . . . . . . . . . . . . .

49

5.4

Application to nearest neighbors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

52

5.5

Application to reproducing kernel ridge regression . . . . . . . . . . . . . . . . . . . . . .

53

5.6

Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

55

Appendix

57

5.A

Fast rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

57

5.B

Nearest neighbors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

63

5.C

Kernel proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

66

<!-- page: 6 -->

4

CONTENTS

6

Exponential Convergence Rates for SVM

79

6.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

79

6.2

Exponential convergence of SVM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

82

6.3

Numerical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

85

6.4

Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

86

6.5

Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

87

Appendix

89

6.A

Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

89

6.B

Experimental details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

91

III

Learning with Partial Supervision

95

7

Inﬁmum Loss

97

7.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

97

7.2

Partial labeling with inﬁmum loss . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

98

7.3

Consistent algorithm for partial labeling . . . . . . . . . . . . . . . . . . . . . . . . . . .

100

7.4

Previous works and baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

102

7.5

Applications and experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

103

7.6

Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

106

Appendix

109

7.A

Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

109

7.B

Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

116

7.C

Minimum feedback arc set . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

123

8

Disambiguation Framework

127

8.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

127

8.2

Disambiguation of partial labeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

128

8.3

Learning algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

129

8.4

Consistency result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

129

8.5

Optimization considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

132

8.6

Related work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

134

8.7

Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

135

8.8

Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

136

Appendix

139

8.A

Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

139

8.B

IQP implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

143

8.C

Example with graphical illustrations . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

145

8.D

Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

145

9

Laplacian Regularization

149

9.1

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

149

9.2

Laplacian regularization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

150

9.3

Spectral ﬁltering with kernel Laplacian . . . . . . . . . . . . . . . . . . . . . . . . . . . .

153

9.4

Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

154

9.5

Statistical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

156

9.6

Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

157

Appendix

159

9.A

Extension to partially supervised learning . . . . . . . . . . . . . . . . . . . . . . . . . .

159

9.B

Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

160

9.C

Central operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

162

9.D

Spectral decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

168

9.E

Consistency analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

170

<!-- page: 7 -->

CONTENTS

5

IV

Active Labeling

185

10 Streaming Stochastic Gradients

187

10.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

187

10.2 The "active labeling" problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

188

10.3 Weak information as stochastic gradients . . . . . . . . . . . . . . . . . . . . . . . . . . .

189

10.4 Median regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

190

10.5 Statistical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

191

10.6 Numerical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

192

10.7 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

194

10.8 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

195

Appendix

197

10.A Proofs of the statistical analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

197

10.B Unbiased weakly supervised stochastic gradients . . . . . . . . . . . . . . . . . . . . . .

210

10.C Median surrogate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

212

10.D Classiﬁcation with a min-max game . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

214

10.E Experimental details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

216

Conclusion

221

Bibliography

223

<!-- page: 8 -->

<!-- page: 9 -->

# Chapter 1. Forewords

## 1.1 Acknowledgement

This thesis would not have been the same without the brilliant minds of Francis Bach and Alessandro Rudi, who have constantly impressed me by the speed at which they formed deep thoughts on any subject I would bring up in meetings. I consider myself really fortunate to have worked under your direction. Beside your sagacity, you have been a great source of inspiration as a person: always wise and caring, even when I was wondering about life in uncalled-for fashions, I was abusing academic freedom, or I was claiming false statements. My second thoughts go for my colleagues at INRIA Paris. I am particularly grateful to Alex Nowak for our many conversations around structured prediction, and to Yann Labbé for his continuous support. My last year as a PhD student has been highly enjoyable, which correlates with the arrival of Quentin Le Lidec in my oﬃce. Finally, I would like to warmly thank Guillaume Lecué and Eyke Hüllermeier for having accepted to review this manuscript, and especially considering how valuable your research hence your time is. In particular, Eyke, you were the ﬁrst person to give me feedback on my work, which I have experienced as an accolade that marked my entry in the research world.

Une thèse de doctorat représente un accomplissement académique certain. Ma reconnaissance s’exprime également envers toutes les entités et les personnes extérieures qui m’ont permis d’y accéder. Tout d’abord tous les professeurs qui ont su me transmettre leur enthousiasme, en particulier Xavier Lacroix et ses merveilleuses digressions. Rétrospectivement, je m’étonne du dévouement et de la pédagogie remarquable d’un grand nombre d’entre eux, l’exemple le plus frappant étant celui d’Alain Camanès qui a su m’enseigner la rigueur nécessaire pour entrer dans le monde des sciences du supérieur. Enﬁn, mon parcours n’aurait pas été le même sans la bienveillance d’un certain nombre de personnes qui ont cru en moi plus que moi-même n’y croyait, me laissant nombre de vifs souvenirs. Remercions également les institutions qui font de leur mieux pour permettre ce genre d’entreprises, notamment en les ﬁnançant. En particulier, cette thèse a été ﬁnancée par le gouvernement français via le programme « Investissements d’avenir » de l’Agence Nationale de la Recherche (référence ANR-19-P3IA-0001). Francis et Alessandro sont également soutenus ﬁnancièrement par l’European Research Council (bourses SEQUOIA 724063 et REAL 94790).

Cet accomplissement s’inscrit également dans une histoire plus intime. Celle-ci s’écrit depuis bien avant ma naissance, et si je peux ici ressusciter les morts pour les remercier, je le ferai pour l’importance qu’ils ont porté à l’éveil, l’instruction et la curiosité, des valeurs qu’à leur suite, mon père et ma grand-mère maternelle ont tout particulièrement souhaite m’inculquer. Je dois également à ma famille de précieux sentiments, nourris par le souvenir, qui me fournissent souvent les aspirations nécessaires pour repartir quand la diﬃculté se fait trop présente en moi. J’espère qu’en retour, je participe un peu au bonheur et au développement de chacun. Si ce court texte ne permet pas de remercier personnellement toutes les personnes qui m’importent, je n’oublierai ni mon papy qui m’a hébergée pendant ces trois dernières années, ni ma mère qui s’est occupée de moi si longtemps. À la famille s’ajoutent mes amis. J’aimerai les remercier tous, qui sont des éléments constitutifs de ma personne. En particulier, je citerai Thomas Kerdreux pour sa magnanimité et Charles Arnal pour ses pertinents conseils. Tous deux ont une vigueur intellectuelle et physique qui ne cesse de m’impressionner.

7

<!-- page: 10 -->

### 1.1.1 Résumé

Les mathématiques appliquées et le calcul nourrissent beaucoup d’espoirs à la suite des succès récents de l’apprentissage supervisé. Dans l’industrie, beaucoup d’ingénieurs cherchent à remplacer leurs anciens paradigmes de pensée par l’apprentissage machine. Étonnamment, ces ingénieurs passent plus de temps à collecter, annoter et nettoyer des données qu’à raﬃner des modèles. Ce phénomène motive la problématique de cette thèse: peut-on déﬁnir un cadre théorique plus général que l’apprentissage supervisé pour apprendre grâce à des données hétérogènes? Cette question est abordée via le concept de supervision faible, faisant l’hypothèse que le problème que posent les données est leur annotation. On modélise la supervision faible comme l’accès, pour une entrée donnée, non pas d’une sortie claire, mais d’un ensemble de sorties potentielles. On plaide pour l’adoption d’une perspective « optimiste » et l’apprentissage d’une fonction qui vériﬁe la plupart des observations. Cette perspective nous permet de déﬁnir un principe pour lever l’ambiguïté des informations faibles. On discute également de l’importance d’incorporer des techniques sans supervision d’appréhension des données d’entrée dans notre théorie, en particulier de compréhension de la variété sous-jacente via des techniques de diﬀusion, pour lesquelles on propose un algorithme réaliste aﬁn d’éviter le ﬂéau de la dimension, à l’inverse de ce qui existait jusqu’alors. Enﬁn, nous nous attaquons à la question de collecte active d’informations faibles, déﬁnissant le problème de « catalogage en ligne », où un intendant doit acquérir une maximum d’informations ﬁables sur ses données sous une contrainte de budget. Entre autres, nous tirons parti du fait que pour obtenir un gradient stochastique et eﬀectuer une descente de gradient, il n’y a pas besoin de supervision totale.

### 1.1.2 Abstract

Applied mathematics and machine computations have raised a lot of hope since the recent success of supervised learning. Many practitioners in industries have been trying to switch from their old paradigms to machine learning. Interestingly, those data scientists spend more time scrapping, annotating and cleaning data than ﬁne-tuning models. This thesis is motivated by the following question: can we derive a more generic framework than the one of supervised learning in order to learn from clutter data? This question is approached through the lens of weakly supervised learning, assuming that the bottleneck of data collection lies in annotation. We model weak supervision as giving, rather than a unique target, a set of target candidates. We argue that one should look for an “optimistic” function that matches most of the observations. This allows us to derive a principle to disambiguate partial labels. We also discuss the advantage to incorporate unsupervised learning techniques into our framework, in particular manifold regularization approached through diﬀusion techniques, for which we derived a new algorithm that scales better with input dimension then the baseline method. Finally, we switch from passive to active weakly supervised learning, introducing the “active labeling” framework, in which a practitioner can query weak information about chosen data. Among others, we leverage the fact that one does not need full information to access stochastic gradients and perform stochastic gradient descent.

## 1.2 Summary of contributions

1. The main contribution of this thesis is to provide a generic framework to deal with partial supervision. Along this framework, we provide a consistent algorithm for any structured prediction problem (Cabannes et al., 2020b); a principled algorithm to disambiguate weak information into full supervision which go beyond the partial supervision setting (Cabannes et al., 2021b), as well as a statistically and computationally eﬃcient way to incorporate Laplacian regularization (Cabannes et al., 2021a). 2. We provide a method to derive fast rates for any discrete output problem (Cabannes et al., 2021c) based on least-squares surrogate. Although geared toward least-squares surrogate with Tikhonov regularization, those derivations can easily be extended to self-concordant losses based on Marteau- Ferey et al. (2019) and to any spectral ﬁltering techniques based on Lin et al. (2020). We hope that this could be useful for statistical learning people, and we wish to see in the future similar results for other losses, as well as a better theory to compare surrogate problems for classiﬁcation. As a ﬁrst step in this direction, we provide some derivations for the hinge loss (Cabannes and Vigogna, 2022). 3. We provide a statistically and computationally eﬃcient method to approach Laplacian regularization (Cabannes et al., 2021a). Our method could be useful for a vast number of applications. Our low-rank approximation could help scale up exciting methods for sampling based on Langevin dynamics

<!-- page: 11 -->

(Pillaud-Vivien, 2020a), Gaussian processes with derivatives (Eriksson et al., 2018), sparse models based on regularization with derivatives (Rosasco et al., 2013). The fact that we “kernelized” Laplacian regularization, making it statistically superior to existing local averaging methods, is exciting when considering the impact of “local” methods such as diﬀusion maps (Coifman and Lafon, 2006). 4. We introduce the active labeling problem, which unify several problems of searching for information through imprecise query, and might be useful to deal with privacy issues. We provide a stochastic gradient descent method that does not require full supervision to tackle this active weakly supervised learning problem that we formalized in Cabannes et al. (2022).

### 1.2.1 List of publications

On supervised learning, reproduced in Part II.

• (Cabannes et al., 2021c) Vivien Cabannes, Alessandro Rudi, and Francis Bach. Fast rates in structured prediction. In Conference on Learning Theory, 2021. • (Cabannes and Vigogna, 2022) Vivien Cabannes and Stefano Vigogna. A case of exponential convergence rates for SVM. In preparation 2022. On partial supervision, reproduced in Parts III and IV.

• (Cabannes et al., 2020b) Vivien Cabannes, Alessandro Rudi, and Francis Bach. Structured prediction with partial labeling through the inﬁmum loss. In International Conference on Machine Learning, 2020. • (Cabannes et al., 2021a) Vivien Cabannes, Alessandro Rudi, and Francis Bach. Disambiguation of weak supervision with exponential convergence rates. In International Conference on Machine Learning, 2021. • (Cabannes et al., 2021a) Vivien Cabannes, Loucas Pillaud-Vivien, Francis Bach, and Alessandro Rudi. Overcoming the curse of dimensionality with Laplacian regularization in semi-supervised learning. In Neural Information Processing Systems, 2021. • (Cabannes et al., 2022) Vivien Cabannes, Francis Bach, Vianney Perchet, and Alessandro Rudi. Active labeling: streaming stochastic gradients. In preparation 2022. Some artistic reﬂections formatted for workshops (not reproduced).

• (Cabannes et al., 2019) Vivien Cabannes, Thomas Kerdreux, Louis Thiry, and Tina & Charly. Dialog on a canvas with a machine. In NeurIPS workshop on Creativity, 2019. • (Cabannes et al., 2020a) Vivien Cabannes, Thomas Kerdreux, Louis Thiry. Diptychs of human and machine perception. In NeurIPS workshop on Creativity, 2020. Side works done for French reviews (not reproduced).

• Vivien Cabannes. Perquisition de données sur le cloud : les Etats-Unis en avance, l’Europe à la traîne. In le Grand Continent, 2019. • (Cabannes, 2022) Vivien Cabannes. Le futur du numérique sera-t-il incarné ? Esprit, 487:117-125, 2022.

## 1.3 Research chronology

This section traces back some of my research history, before summarizing the contributions of this thesis. I wish it to be useful in order to understand the thought process behind this thesis and to ease its reading.

The thesis originated from the motivations of my supervisors to confront the interest of Francis for weak supervision with the least-squares surrogate method of Alessandro. My interest was sparked by the fact that I wondered how to better incorporate fuzzy human knowledge into learning processes. Many abstractions can be learned in a hierarchical fashion, e.g. ﬁrst recognizing edges on input images, then aggregating edges into tires, doors, handles, and those last components into cars, fridges, bridges, before understanding the semantic of an image and outputting a wanted label. Often, we have a good understanding of this hierarchical structure, but it is hard to formulate it clearly in order to guide the learning process. In this thesis, we focus on weak supervision, which is understood as specifying crucial elements in the last layer of abstraction before labels, such as specifying some animal attributes that allow us to discriminate the animals that our algorithm should learn to recognize. Other priors on the problem to solve are assumed to be incorporated into the model or into regularizers. Note that priors are distinct from supervision in the sense that they are given once and for all, while supervision can be reﬁned (e.g. samples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛are a function of 𝑛∈N that can be made larger).

<!-- page: 12 -->

From a theoretical point of view, successes of machine learning are understood as successes of supervised learning, which are successes of statistics when given enough clean data. Yet, in many problems, accessing tidy data is too costly, so many heuristics have been developed to deal with settings that do not completely ﬁt in the supervised learning setting. The goal of this thesis is to ground those heuristics into principles. To make those principles clear and rigorous, this work ﬁnds its roots in the statistical learning theory. In particular, we assume that there is a unique metric to quantify the quality of a learning algorithm, and that this metric is speciﬁed by a loss function.

The ﬁrst task was to deﬁne the setup to work on. Many directions could have been taken. For example, supervision can come as experts specifying what is their guess for the label, and what is their levels of certitude. To avoid dealing with fuzziness, we decided to assume that our supervision provides sure information that allows us to locate the label into a set of label candidates, assuming that errors on the supervision could be captured by the randomness of the label conditionally to the input. This generic yet interesting framework turns out to have already been studied in the literature under the name of partial labeling as well as superset learning. In a ﬁrst paper (Cabannes et al., 2020b), we described this framework, advocate for combining weak information in a parsimonious way and came up with some theoretical results to strengthen our point. We put on top the framework of Alessandro to exhibit a consistent algorithm with decent convergence rates. While we initially wanted to compare this principle with several heuristics and associated principles, we soon realized that this task was endless, and we reduced the experimental comparison to “comparable” principles.

Several indications point us toward a second paper (Cabannes et al., 2021b). First of all, the algorithm we came up with was dealing with a really big related surrogate problem, hard to understand, hiding in ugly constants in our convergence rates. Fundamentally, we were dealing with functions from input to set of labels, and were paying the price of the combinatorial structure of power sets. To stay in the space of functions from input to labels, we decided to explicitly retrieve labels from weak supervision before learning with a fully supervised dataset. To come up with a clear empirical objective, we thought in terms of distributions rather than functions, leveraging the kernel mean embedding structure beyond Alessandro framework. However, theoretical guarantees were much harder to obtain, missing generic tools to understand deviation between empirical principle and population principle when these principles are expressed on distributions. This forces us to incorporate assumptions to ease the theoretical understanding. Surprisingly, those assumptions were not that strong and led to much better convergence rates, and this was not only the case for our problem but for the whole framework of Alessandro. We published this interesting result in a diﬀerent paper (Cabannes et al., 2021c), and left open research questions on how far we can push those derivations. We came back to those questions recently, extending the proof mechanism to support vector machines (Cabannes and Vigogna, 2022). In the ﬁrst two papers, we built on combining weak information conditionally to a given input. While relation between inputs were captured by the model of functions we learn, the model we used was not smartly leveraging the input distribution. As such, we wanted to strengthen our principle to deal with settings akin to semi-supervised learning. In particular, we wanted to incorporate Laplacian regularization into our framework. Surprisingly, there were no good “kernelized” methods for Laplacian regularization but only “local averaging” methods. Beneﬁting from the expertise of my supervisors on kernel methods, as well as exchanging with Loucas Pillaud-Vivien, who already realized this fact, we came up with a paper on the matter (Cabannes et al., 2021a). Arguably, this gave a satisfying ﬁnal piece to the theoretical framework built in this thesis in order to learn from partial supervision.

From there were several natural continuations. Deepen the study of partial supervision by understanding and incorporating more heuristics into our frameworks, such as collaborative ﬁltering. Reﬁne our algorithms with reﬁnement of the structured prediction framework of Alessandro, for example, what can we say about conditional random ﬁelds and partial supervision? could we simplify the link between the structure of the supervision and the structure in “structured prediction”, as we have implicitly done in the ﬁrst two papers applications and algorithms? Widen our scope to all weak supervision frameworks, or even all unclutter data problems (e.g. missing input data). Ultimately, we decided to go for dataset annotation.

The ultimate goal of this work is to be useful to the practitioner hustling with data. Indeed, our research was not motivated by the fact that many datasets come with weak supervision, but by the idea that weak supervision is easier to collect for the practitioner. As a consequence, if we suppose that the practitioner is annotating data, we might help him to eﬃciently provide the most useful supervision. This problem has deep links with active learning, sequential design, non i.i.d. statistics and search games; links that were attractive to me. Building on our previous framework, we came up with a simple model of annotation cost and looked at techniques to minimize this cost for a given level of probably approximately correct bound. In

<!-- page: 13 -->

dimension one, our atomic questions are exactly the gradient of the 𝐿1 loss; this pushed us to realize that one does not need full supervision to acquire unbiased stochastic gradients (Cabannes et al., 2022). However, when dealing with highly structured prediction, naive stochastic gradient descent on continuous surrogates suﬀer from suboptimality issues. Hence, in order to have a ﬁner control on the samples we collected, we are currently switching to a bandit setting, for which, with the help of Vianney Perchet, we hope to come up with creative solutions.

### Ethical considerations

This work aims at advancing our understanding of weakly supervised learning. Weakly supervised learning enrolls in the quest of an automated artiﬁcial intelligence, free from the need of human supervision. Automation, which is at the basis of computer science (Turing, 1950), is known to increase productivity at a reduced human labor cost, and is associated with several political/societal issues.

<!-- page: 14 -->

<!-- page: 15 -->

# Part I. Introduction

13

<!-- page: 16 -->

<!-- page: 17 -->

# Chapter 2. The Machine Learning Paradigm

In 2021, the International Data Corporation estimates that by 2025, the yearly global spending on artiﬁcial intelligence (AI) will overrun $204 billions (Glennon and Shirer, 2021). To give an order of magnitude, this corresponds to the gross domestic product of countries such as Greece, New Zealand or Peru.1 It means that if this business was concentrated in Peru, its 33 millions inhabitants would only produce goods and services related to AI. Nowadays, the core engine behind AI is machine learning, that is the learning of rules and algorithms by computers. In this chapter, we provide a subjective exposition of what machine learning is about. It is written to be accessible for a large public beyond the machine learning community.

## 2.1 From algorithmics to machine learning

In this section, we present machine learning as the evolution of algorithmics.

In a prosaic fashion, an algorithm can be thought of as a cooking recipe. It is a sequence of instructions that, given some inputs, produces an output. For example, the inputs could be some apples, lard, eggs, salt and ﬂour, the sequence of instructions be the one of an apple pie recipe, and the output be a delicious pie. This can be formalized mathematically, an algorithm being understood as a sequence of instruction 𝐼, leading to a mapping 𝑓: X →Y, which, given an input 𝑥belonging to an input space X, outputs 𝑦= 𝑓(𝑥) belonging to an output space Y.

Example 1 (Cooking recipe). X is a set of potential ingredients, Y is a set of potential pies. For some ingredients 𝑥, e.g. 𝑥= (5 apples, 100g of lard, 200g of ﬂour, 1 egg, 1 pinch of salt), 𝑦= 𝑓(𝑥) describes the pie obtained by following the instructions 𝐼of a recipe.

Example 2 (Sorting algorithm). X = R𝑛is the set of lists of size 𝑛, Y = {(𝑦1, · · · , 𝑦𝑛) ∈R𝑛| 𝑦1 ≤· · · ≤𝑦𝑛} is the set of sorted lists of size 𝑛. Any sorting algorithm corresponds to 𝑓: X →Y that maps a list 𝑥= (𝑥𝑖)𝑖≤𝑛 to its sorted version 𝑦= (𝑥𝜎(𝑖))𝑖≤𝑛∈Y with 𝜎∈S𝑛a permutation.

Example 3 (House pricing). X = R2 + represents real estate properties with two features: the living space of the house, the outdoor space of the garden, both in meter square. Y = R+ represents the price of the house in US dollars. The mapping 𝑓is a model for house prices.

Example 4 (Classifying cats and dogs). X = [255]𝑑1×𝑑2×3 is a set of images of cats and dogs. Those images are represented by 𝑑1 × 𝑑2 pixels, with the three RGB channels. Y = {−1, 1} with 𝑓(𝑥) = 1 if 𝑥is an image of cats, and 𝑓(𝑥) = −1 if 𝑥is an image of dogs.

The problematics arising in our examples are all slightly diﬀerent and will be helpful to illustrate diﬀerences between algorithmics, statistics and machine learning.

Algorithmics. In classical computer science, algorithms are implemented on 𝑚bits of memories. As such, the sequence of instructions can be written as 𝐼= (𝐼𝑡)0≤𝑡≤𝑇+1, with 𝐼0 : X →{0, 1}𝑚an encoding of X on 𝑚bits, 𝐼𝑇+1 : R𝑚→Y a decoding of 𝑚bits to Y, and, for 𝑡∈[𝑇], 𝐼𝑡: {0, 1}𝑚→{0, 1}𝑚a basic bitwise operation. In problems such as sorting lists, we know exactly which 𝑓we want to achieve, but we do not 1According to the World Bank Open Data.

15

<!-- page: 18 -->

know how this mapping can be decomposed into a set of basic operations which could be implemented practically on a computer. In those algorithmic problems, an algorithm is thought of as the sequence of instructions 𝐼,and its quality is discussed under the light of two notions.

• Correctness: does this sequence of instructions correspond to the desired mapping 𝑓? In other terms, can we guarantee the equality 𝑓= 𝐼𝑇+1 ◦𝐼𝑇◦· · · ◦𝐼0? • Complexity: how much basic operations 𝑇and computer memory 𝑚does it take to perform the full sequence of instruction 𝐼? In the cooking example 1, the ﬁrst question can be rephrased as: does our recipe, given a speciﬁcation of ingredients, always lead to the same pie? The second question is related to the equipment and the time required by the recipe. When it comes to sorting lists, example 2, deriving and implementing a sequence of basic operations to solve this task is a reasonable idea. For example, think of how you sort a deck of cards, write rules about it, and implement those rules in your favorite programming language that will convert it into a sequence of bitwise instructions for the computer. When it comes to understanding images, deriving and implementing a sequence of basic operations to diﬀerentiate cats and dogs have not been proven a successful way to proceed. Indeed, even for language translation, eﬀorts, made by linguists to describe translation as a set of simple syntactic rules, have not led to eﬃcient translation algorithms.

Learning optimal sequence of instructions. Rather than designing an algorithm from a set of humanly- thought rules, machine learning suggests designing an algorithm by quantifying a notion of optimality, or equivalently a notion of error, cost or risk R, and looking among all potential sequences of instructions 𝐼∈I, in a class I of potential sequences of instruction, for the one that minimize the risk R(𝐼). For example, in the cooking example, we could consider I as all potential combinations of basic instructions such as “breaking eggs”, “mixing some ingredients”, “frying/baking a batter” and so on. Optimality, and the risk R, could be designed by some experts testing the pie, or through molecular gastronomy considerations. To ﬁnd the best recipe, that is the best sequence of basic instructions, a naive approach consists in trying all potential combinations of basic instructions 𝐼, and quantifying the result quality through R(𝐼), and considering the sequence 𝐼that achieves the minimal risk. Of course, there are zillions of ways to combine basic instructions, and baking zillions of pie, and having them tested by experts is not a viable option. But on a computer that can perform millions of operations by seconds, the picture is quite diﬀerent. Applied to the list sorting problem, such a procedure leads to a completely diﬀerent approach from the classic algorithmic one. Roughly speaking, the machine learning paradigm is to try all potential algorithms and take the best one, where “the best” is quantiﬁed through the risk R.

## 2.2 The emergence of statistics

In this section, we get more speciﬁc on what machine learning is today, that is, statistics in the era of powerful computers.

While machine learning could be seen as the art of automatically designing algorithms, nowadays, it is rather a new take on statistics in the era of powerful computers. As such, it is less focused on having a “good” correct sequence of instruction 𝐼to perform a task, but rather in ﬁnding a mapping 𝑓that is optimal for a task, such as pricing houses or distinguishing cats and dogs. In such a setting, the risk R : YX →R+ associates a score R( 𝑓), quantifying a notion of risk, cost or error, to a function 𝑓: X →Y. Ideally, we would like to retrieve an optimal mapping 𝑓∗: X →Y such that

$$
R( 𝑓∗) = R∗, where R∗= inf 𝑓:X→Y R( 𝑓). (2.1)
$$

(2.1)

The problematics of machine learning are slightly diﬀerent from the ones of algorithmics. The quality of a procedure, that allows obtaining automatically a mapping 𝑓: X →Y to solve a speciﬁed task, is discussed under the light of three notions.

• Optimality: is the risk R( 𝑓) of the obtained mapping 𝑓close to R∗? • Inference complexity: given an input 𝑥∈X, is it easy to compute 𝑓(𝑥)? • Training complexity: is it computationally easy to obtain the mapping 𝑓? The ﬁrst two issues are the direct translation of the algorithmic issues of correctness and complexity, while the third one is speciﬁc to machine learning, and has strong links with the ﬁeld of optimization.

<!-- page: 19 -->

Remark 1 (Correctness and Optimality). In classical algorithms, there is the idea that an algorithm is perfect/correct, that we know exactly what it is doing. In machine learning, the idea of 𝑓being correct is dropped by the notion of 𝑓being optimal or quite optimal. For critical applications such as ﬂying planes, replacing the notion of correctness brought in by classical algorithms, by a notion of quasi-optimality is not innocuous. Yet, once a mapping 𝑓is retrieved by an artiﬁcial intelligence system, it can be tested for correctness through formal proof management systems, or tested for statistical quality through an extensive number of testings. While replacing “being correct” by “being statistically good” can oﬀend purists, note that, in medicine, drugs are more often approved based on statistical studies, rather than on a precise description of their mechanisms and a complete understanding of their interactions with the body.

If we consider the cooking example 1, we could translate those three issues into prosaic terms. Suppose that you have a way to design new recipes. Optimality translates into “are the new dishes you make good?”. Inference complexity translates into “are the recipes easy to reproduce?”. Optimization complexity translates into “is your procedure for designing new recipes diﬃcult, is it time and money consuming?”.

### 2.2.1 Supervised learning

A simple idea to learn a mapping 𝑓between inputs 𝑥and outputs 𝑦is to consider a set of 𝑛examples (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛∈(X × Y)𝑛, where 𝑓(𝑥𝑖) should be 𝑦𝑖, and try to infer from those examples a general law between 𝑥and 𝑦. That is, for house pricing, example 3, consider 𝑛houses, report their characteristics (𝑥𝑖)𝑖≤𝑛and their prices (𝑦𝑖)𝑖≤𝑛, and try to ﬁnd a law that links house characteristics 𝑥to their prices 𝑦. In particular, a real estate agent can try to ﬁt a linear model 𝑦= 𝑤⊤𝑥, for 𝑤∈R𝑑a weight vector, the house characteristics 𝑥 assumed to belong to X ⊂R𝑑, and 𝑦the price of the house. It is usual to ﬁt 𝑤by minimizing the least-squares error

$$
𝑛 ∑︁ 𝑤⊤𝑥𝑖−𝑦𝑖 2 = ( 𝑛 ∑︁ 𝑛 ∑︁
1 𝑛
ˆ𝑤∈arg min 𝑥𝑖𝑥⊤ 𝑖)† 𝑦𝑖𝑥𝑖,
𝑤∈R𝑑 𝑖=1 𝑖=1 𝑖=1
$$

where, for a vector 𝑥∈R𝑑= R𝑑×1, 𝑥⊤∈R1×𝑑designs its transpose, and, for a matrix 𝐴, 𝐴† its pseudo-inverse. When needing to price a new house, the real estate agent could report its characteristics 𝑥and price it at 𝑦= ˆ𝑤⊤𝑥.

Such a model raises many questions. Which features 𝑥govern the price of a house? Can the price of the house be deduced as a linear combination of those features? How many houses 𝑛should I consider as training examples (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛to retrieve a ˆ𝑤such that the value ˆ𝑤⊤𝑥does reﬂect well the market price of a new house characterized by 𝑥? How much should we expect the transaction price of a house to deviate from our model of its market price? Those questions are addressed by statisticians and machine learning practitioners. They are respectively linked with features engineering, model selection, data collection, and generalization guarantees.

Perhaps the most well known result of statistics is the large law number. In essence, it tells you that if you repeat the same experiment, what you see as the result of this experiment, reﬂects what you are likely to see if you repeat this experiment one more time. For example, if you have rolled a die zillion times, and you have gotten six forty-ﬁve percent of the time, the next time you roll this die, you can expect to get a six with forty-ﬁve percent of chance. In the past two centuries, statisticians have developed many concentration inequalities that quantify, given the number of experiments you have run so far, how much the statistics collected from those experiments are likely to reﬂect the outcome of future experiments. This provides tools to give generalization guarantees on models learned from data. But beyond those results are some axioms on the experiments you run. In particular, statistics are grounded in probability theory, assuming that the experiment’s outcomes are governed by some probabilistic process that is stable over time, allowing prediction of future outcomes from prior ones. Typically, when talking about dice, we assume that you roll the same dice, in the same fashion, in the same environment.

Learning theory, and in particular supervised learning, builds on this idea of understanding observable phenomena by assuming an underlying probabilistic model. This thesis is set in this framework. It assumes the existence of a joint probability distribution 𝜌∈ΔX×Y over X and Y, that have generated the dataset D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼𝜌⊗𝑛in an independent identically distributed fashion. Moreover, it assumes that the measure of error results from the integration of a pointwise measure of error ℓ( 𝑓(𝑋),𝑌), between a prediction 𝑓(𝑋) made at the point 𝑋and its observed label 𝑌, for ℓ∈Y × Y →R a loss function, in the sense that for 𝑓: X →Y,

$$
R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] . (2.2)
$$

(2.2)

<!-- page: 20 -->

As one has no access to the distribution 𝜌but only to samples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛, it is natural to substitute the risk with its empirical counterpart RD𝑛: YX →R, deﬁned as

$$
𝑛 ∑︁
RD𝑛( 𝑓) = 1
[ℓ( 𝑓(𝑋𝑖),𝑌𝑖)] . (2.3)
𝑛
𝑖=1
$$

(2.3)

A popular approach to learn a mapping 𝑓: X →Y is to consider some model of functions F ⊂YX and to perform empirical risk minimization over this class of functions, leading to the estimate

$$
\underset{𝑓∈F}{\arg\min}\, RD𝑛( 𝑓).
$$

Yet, how optimal is this mapping 𝑓𝑛? In other terms, does it exhibit a low risk R( 𝑓)? In the machine learning community, this question refers to generalization properties of 𝑓𝑛: does what we have learned based on 𝑛 examples generalize to new situations characterized by new inputs? Statistical learning theory provides some answers to this question.

Remark 2 (Why probability?). Arguably, we live in a deterministic world. Hence, if everything has a reason, why introduce randomness in our model? Think about rolling dice, the face that pops up is a pure deterministic function of the landscape of the support the dice are rolled on, as well as the initial moment, impulsion and position of the dice, which themselves depend on the mood of the person rolling the dice. But as we cannot model those factors, we suppose them to be random, leading to the random distribution on the rolling dice, at the end of the causal chain from mood to initial physical values to dice output. The same applies to house price, many idiosyncratic factors come into play when a buying oﬀer is made on a house. When tracking those explanation variables is too diﬃcult, statisticians deal with this fact by adding randomness into the model.

### 2.2.2 Generalization bounds

In this subsection, we mimic typical derivations provided by statistical learning theory which are used in this thesis. Recall the house pricing example 3. Supervised learning consists in assuming the existence of some abstract distribution 𝜌∈X × Y, and that pairs of house characteristics and their prices (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛are actually sampled from this distribution (𝑥𝑖, 𝑦𝑖) = (𝑋𝑖,𝑌𝑖) ∼𝜌⊗𝑛– using capital letters to denote the randomness in the sampling. Trying to predict house prices from a linear combination of house characteristics leads to the model of functions F =

$$
𝑥→𝑤⊤𝑥 𝑤∈R𝑑
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

, assuming 𝑥∈X ⊂R𝑑. The best linear model, based on the mean-squares error, is deﬁned by 𝑓∗

$$
𝑥→𝑤⊤𝑥
$$

lin : 𝑥→𝑥⊤𝑤∗, with the weighting scheme

$$
h

𝑋⊤𝑤−𝑌 2i 𝑋𝑋⊤ 
𝑤∗∈arg min )† E(𝑋,𝑌)∼𝜌[𝑌𝑋] .
𝑤∈R𝑑E(𝑋,𝑌)∼𝜌 = (E𝑋∼𝜌X
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Here 𝜌X designs the marginal of 𝜌over X, that is, the distribution of 𝑋according to 𝜌. In practice, we do not have access to 𝜌but to the samples (𝑋𝑖,𝑌𝑖). As a consequence, we can replace 𝜌by ˆ𝜌= 1

$$
Í𝑛
$$

𝑖=1 𝛿(𝑋𝑖,𝑌𝑖), which leads to the empirical risk minimizer 𝑓𝑛: 𝑥→𝑥⊤ˆ𝑤with

$$
𝑛
!† !
𝑛 ∑︁ 𝑋⊤ 2 = 𝑛 ∑︁ 𝑛 ∑︁
1 𝑛 1 𝑛 1 𝑛
ˆ𝑤∈arg min 𝑖𝑤−𝑌𝑖 𝑋𝑖𝑋⊤ 𝑌𝑖𝑋𝑖 .
𝑖
𝑤∈R𝑑 𝑖=1 𝑖=1 𝑖=1
$$

As the quality of a function 𝑓is measured through the risk R, it is natural to measure the quality of 𝑓𝑛in terms of the excess of risk R( 𝑓𝑛) −R∗, with respect to the minimum achievable risk R∗. This error can be split in the following way

$$
R( 𝑓𝑛) −R∗= R( 𝑓𝑛) −R( 𝑓∗ lin) | {z } + R( 𝑓∗ lin) −R∗ | {z } approximation error . (2.4)
estimation error
$$

(2.4)

This split separates an error due to the need for more data so that ˆ𝑤estimates 𝑤∗correctly and a part due to the fact that the best linear predictor 𝑓∗ lin might not be the best pricing model. The decomposition with estimation and approximation errors, is sometimes called bias-variance decomposition. The variance, or

<!-- page: 21 -->

estimation error, is due to the randomness of the samples, while the bias, or approximation error, is due to the gap between the average (or best) estimate we expect and the solution.

The approximation error is due to the fact that our model might be inaccurate. This error can be controlled by assuming some sort of density of F in X →Y regarding the topology inherited from R, or by assuming that the best predictor 𝑓∗does belong to our class of functions F (or is well approximated by it with respect to the topology associated with R).

The estimation error is due to the fact that we have estimated a quantity deﬁned through the distribution 𝜌thanks to sample (𝑋𝑖,𝑌𝑖)𝑖≤𝑛. Similarly to rolling dice or tossing coins, when knowing 𝜌, statistics and probability can quantify, for a given number of training examples 𝑛, what is the distribution of R( 𝑓𝑛)−R( 𝑓∗ lin). This distribution should be seen as the pushforward of 𝜌⊗𝑛regarding the process that leads to the estimate 𝑓𝑛from samples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛. When not knowing 𝜌, this pushforward cannot be estimated, but with few hypotheses on 𝜌, such as control of extreme behaviors, or equivalently control of high moments, it is possible to control deviation of R( 𝑓𝑛). This is exactly what provide concentration inequalities, such as Hoeﬀding or Bernstein inequalities, that allows upper-bounding the deviations between the empirical means 1

$$
Í𝑛
Í𝑛 𝑖=1 𝑋𝑖𝑋⊤
$$

𝑖 and 1

$$
𝑛
$$

𝑖=1 𝑌𝑖𝑋𝑖and their population counterpart E[𝑋𝑋⊤] and E[𝑌𝑋], and therefore the deviation between ˆ𝑤and 𝑤∗.

$$
𝑛
$$

With assumptions to control the approximation and estimation errors, it is possible to get convergence results of the type,

$$
∀𝑡> 0, PD𝑛(R( 𝑓𝑛) −R∗> 𝑡) ≤exp(−𝜎−2𝑛𝑡2).
$$

This speciﬁc result tells you that if you have trained your model with 𝑛independent identically distributed samples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛, the risk of the learned mapping 𝑓𝑛is comparable to a random number that follows a Gaussian distribution N (0, 𝜎/√𝑛), the randomness being due to the randomness of the samples. Such a bound is called a generalization bound as it tells us what risk or error we can expect on generic examples, which is a measure of how well our predictor generalizes to new situations. When an algorithm beneﬁts from such a bound, we call it probably approximately correct (Valiant, 2013), in the sense that with high probability (the randomness being due to the sample population), it approximately minimizes the risk. It is worth noting that, in practice, we only have one realization of D𝑛, and that this result does not tell us that the risk R( 𝑓𝑛) is small, it only tells us that we would have been really unlucky if it was not the case.

### 2.2.3 Unsupervised learning

In the preceding sections, we have presented machine learning as concerned with the learning of a mapping from an input space X to an output space Y. As such, it diﬀers from statistics that are rather concerned with inferring properties of a distribution 𝜌X from samples (𝑋𝑖)𝑖≤𝑛. Indeed, many papers published as machine learning papers are concerned with this setting, usually referred to as unsupervised learning. There are two major motivations for unsupervised learning.

First, statistical problems such as density estimation, eventually done through maximum likelihood estimation, are instances of problems where we would like to infer properties of a distribution 𝜌X through samples (𝑋𝑖)𝑖≤𝑛. The usage of a computer, and of optimization routines, is crucial to deal with a large number of data in this setting. Indeed, many of the computational and statistical problematics arising from those problems are shared with standard supervised learning, justifying results on those problems to be published in machine learning conferences, and justifying the machine learning community to welcome statisticians.

Second, learning a mapping from inputs to outputs, highly beneﬁts from features engineering, which might be done without access to the supervision (𝑌𝑖)𝑖≤𝑛. From a machine learning perspective, the main goal of unsupervised learning is to discover structure beyond input data, assuming that this structure will help to ﬁnd laws that correlate those inputs to potential outputs. For example, when described as an array of pixels, images are understood as points in R𝑑for 𝑑of order 109. Yet, we expect natural images to have a strong structure that forbid them to be any points in R𝑑. Indeed, we can expect natural images to be concentrated close to a low-dimensional manifold, potentially parametrized in R𝑚for 𝑚much smaller than 𝑑, describing the many parameters of freedom of a natural image. Finding such a small representation would ease “downstream” tasks, such as learning to recognize the content of an image. Having been approached with many perspectives, unsupervised learning has been divided into many sub-problems, such as clustering, manifold learning, sparse dictionary learning, or self-supervised learning.

<!-- page: 22 -->

## 2.3 A tour of problems

In this section, we review diverse practical problems that are arguably understood as machine learning problems. We review machine learning to create artiﬁcial intelligence with human-alike capability. We showcase business motivations and driving forces beyond machine learning. We explain how data science can ﬁt into intelligent systems, and discuss how machine learning can help science and how its scope is growing behind statistical learning. We do not aim for completeness, but for simple examples.

### 2.3.1 Seeing, hearing and talking

For non-experts of machine learning, probably the most important result of this last decade was the result achieved by deep learning trained on GPU on the ImageNet challenge of 2012 (Krizhevsky et al., 2012). In essence, for the ﬁrst time, a computer was able to showcase human-like performance when recognizing simple objects in images. Similarly, we can dictate to our electronic devices and have those devices writing down our thoughts as if they were secretaries. Moreover, those devices can emit sounds articulated into words and sentences to answer a question we have eventually asked. All as if machines were to see, hear and speak. This echoes a long fantasy of machines bearing signs of human intelligence.2 Interestingly, this “artiﬁcial intelligence” replicates tasks that many animals do automatically and instantaneously, concerned with processing simple information. As such it is more concerned with intelligence as collecting pieces of information (such as “military intelligence”), rather than the more deep thought and contemplative process captured by the French notion of intelligence. Those recent successes are somewhat based on supervised learning, providing strong evidence of the usefulness of this theoretical framework, especially when compared to previous attempts to build computer vision, audio and natural language processing from so-called “expert systems”. Solving those problems has required machine learning to scale with millions of training examples 𝑛, as well as millions of input dimensions 𝑑, which has strongly pushed to advance calculations engineering (see, e.g., Chowdhery et al., 2022).

### 2.3.2 Playing games

Another highly publicized result of machine learning was the beating of all humans at Go, an abstract strategy board game known for the richness of all potential strategies (Silver et al., 2018). Games such as Go or chess do not ﬁt exactly the framework of supervised learning. Those games are characterized by a position, or state, which mainly corresponds to the disposition of pieces on the game board, that is changed by moves, or action, made iteratively by two players. The game is over when a terminal state is reached. Each terminal state is associated with a game output, could it be a draw, a win of player one or a win of player two. What needs to be learned is a strategy, or policy, that can be seen as a function that maps a game state to an action or move. The goal is to come up with a winning strategy whatsoever the opponent strategy. These problems can be approached with reinforcement learning (Sutton and Barto, 2018), whose goal is to navigate an environment over time in order to maximize some reward functions. The wording “reinforcement” came from behavioral psychology and describes the fact that the strategy is learned by trials and errors. In the case of games, the computer can simulate many games against itself before ﬁnding a winning strategy.

### 2.3.3 Recommender systems

Far away from the fantasy of creating superhuman creatures, a consequent amount of machine learning development is the fruit of businesses trying to better identify potential customers and prospects of bestseller products. A particularly hot topic is recommender systems, whose goal is to propose to a given customer characterized by some features 𝑥, the most adequate content 𝑦. Recommender systems are now everywhere to suggest personalized content, could it be for browsing music and movies, or for targeted advertising.

In 2009, Netﬂix ran a competition to predict how many stars over ﬁve a user might rank a movie. Their goal was clear : have a system that ﬁnds the most relevant movies to recommend to the user. They oﬀered $1,000,000 to anyone coming up with the best performance on this prediction problem (Bennett and Lanning, 2007; Lohr, 2009). A speciﬁcity of this problem was the absence of features to describe movies or users. Among suggestions of many participants, the best solution was provided by 2Indeed, some researchers use concepts of human psychology to describe their algorithms such as attention and saliency maps (Cabannes et al., 2020a).

<!-- page: 23 -->

"collaborative ﬁltering". This technique consists in trying to factorize the note given to a movie by a user as a product 𝑢⊤𝑚, where 𝑢characterizes the user, and 𝑚characterizes the movie with the smallest (in terms of number of coordinates) vectors 𝑢and 𝑚. The goal is to ﬁnd few characteristics for each user that respond to the same number of few characteristics for each movie in order to explain given scores and to predict future scores – think of 𝑢= (how much I like romantic movie, how much I like action movie) and of 𝑎= (how much is it a romantic movie, how much is it an action movie). Formally this technique is formalized by trying to factorize the table 𝑆= (score(user, movie))user,movie as 𝑆= 𝑈𝑀on observed scores for 𝑈and 𝑀of smallest rank. While the rank is not a continuous function, making this problem hard to solve, it is possible to relax it into a concave function thanks to the nuclear norm and get nicely behaving solutions.

### 2.3.4 Intelligent infrastructure

The machine learning of today is the science of data. The competency to manage massive amounts of data opens the way for massive systems of information. Moreover, advances in sensors and measurement tools as well as robots allowing vast automation of tasks create optimistic perspectives in ﬁelds such as farming or medicine. The big dreamer might fall for the internet of things governing hydrometry sensors, cameras recognizing aphids, automatic release of pesticides, analysis of the best companion plants and so on. But without going that far, simply putting in place numerical tools to easily perform large scale cross-sectional and longitudinal studies would highly accelerate medicine – recall debates on Hydroxychloroquine as a COVID treatment based on small studies such as Gautret et al. (2020). Arguably, the revolution promised by machine learning is not the revolution of machine learning per se, nor the creation of supra-humanoid, but the future deployment of massive active monitoring systems (Jordan, 2019).

To give a personal touch to this discussion, in 2019, with two friends, we created an “artiﬁcial intelligent system” to interact with artists during their creation process (Cabannes et al., 2019). In this project, much of our work was engineering to make sure that the process was innocuous for the artists. The machine learning algorithm running in the middle was only a part of the complete picture.

### 2.3.5 Making sense of scientiﬁc data

While we have described the application of machine learning for non-science purposes, in particular for marketing and agriculture, there is traction for machine learning as science for science. Of course, supervised learning techniques can be applied to scientiﬁc problems, such as the protein folding problem (Jumper et al., 2021). But machine learning techniques are also handy to make sense of data coming from massive scientiﬁc experiments such as the quest for the Higgs boson at the CERN (Larkoski et al., 2020), or the analysis of gravitational waves (Gebhard et al., 2019). In those last two examples, the goal is to retrieve a signal that has caused some observations given a potential high-level of noise.

### 2.3.6 Signal recovery and inverse problems

Signal recovery from noisy observations is an active ﬁeld of research with many appreciable results. The goal of compression is to, given a signal 𝑥that is heavy to describe, compress it into a signal 𝑦= 𝑓(𝑥) much lighter to describe, store, transmit, etc. such that given the knowledge of 𝑓and a prior on 𝑥, one can retrieve the signal 𝑥from the observation 𝑦. Historically, this has been studied for telecommunications with several results coming from the Bell Labs, such as the Nyquist-Shannon theorem (Shannon, 1949; Nyquist, 1928): assuming 𝑥to be a function with bounded frequencies, it can be reconstructed by interpolation (Whittaker, 1915). More recently, Candès et al. (2006) and Donoho (2006) looked at the transmission of a vector 𝑥∈R𝑛 known to be sparse, i.e. having only 𝑠<< 𝑛non-zero components, under the form 𝑦= 𝐴𝑥∈R𝑚for a chosen 𝐴∈R𝑚×𝑛. They showed that by taking the row of 𝐴suﬃciently “incoherent” it is possible to recover 𝑥with 𝑚≈2𝑠. Moreover, when the coeﬃcients of 𝐴are random, normally distributed, the “incoherence” property holds with high probability. This allows to drastically reduce compression, as well as acquisition, of sparse signal, and had successful applications in medical imaging (Lustig et al., 2008; Sidky and Pan, 2008). Think of the impact of compressed sensing when it permits reducing X-ray exposure during tomography for the same amount of reconstruction ﬁdelity.

Signal recovery is not the primary focus of machine learning, but as the ﬁeld is gaining traction, its tools and scope of applications are growing, and similarly to compressed sensing papers that ﬁnd their place in machine learning journals and conferences, other imaging techniques might as well. To conclude on those

<!-- page: 24 -->

inverse problems beyond machine learning, let us mention the work of Fink (1997), which leverages wave reversibility and information preservation to design time-reversal mirrors in order to locate a wave source and recreate the emitted wave. In the same vein, techniques such as sonar or medical ultrasonography are based on propagating waves into a medium and deduce a topography of the medium from the waves echo. Among others, they have been used to locate oil in the ground, after creating a wave with dynamite. Quite remarkably, recent research has shown those explosions to be a waste of resources as it is possible to leverage ambient noise of the Earth’s crust in order to image it (Garnier and Papanicolaou, 2016).

## 2.4 A tour of models

In this section, we focus on the supervised learning settings, and we discuss classical models to learn functions. Our classiﬁcation into local averaging, reproducing kernel and deep learning methods is aligned with the class taught by Francis, on learning from ﬁrst principles (Bach, 2023).

### 2.4.1 Local averaging methods

If you are a real estate agent pricing houses, and you encounter a new house and need to price it, a natural idea is to look for similar houses that have been sold recently, and infer a price from those similar examples. This is exactly what captures local averaging methods. Suppose that you have collected examples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛with features 𝑋𝑖characterizing a house indexed by 𝑖∈[𝑛] and its price 𝑌𝑖. Given a new house with characteristics 𝑥, you can look at the 𝑘-th nearest neighbors N𝑘(𝑥) that contains 𝑘elements in [𝑛] and such that for 𝑖∈N𝑘(𝑥) and 𝑗∈[𝑛] \ N𝑘(𝑥), 𝑑(𝑥, 𝑋𝑖) ≤𝑑(𝑥, 𝑋𝑗) according to a distance 𝑑: X × X →R. This deﬁnes the nearest neighbors predictor 𝑓𝑛: X →Y as 𝑓𝑛(𝑥) = 1 Í

𝑖∈N𝑘(𝑥) 𝑌𝑖. Eventually, you might want to give more importance to houses that are really similar to the one you are trying to price, and less to the 𝑘-th nearest neighbor. To do so, you can introduce a system of weights 𝑤𝑖= 𝑤(𝑛)

$$
𝑘
$$

𝑖 : X →R that are positive and sum to one, and reﬁne 𝑓𝑛as

$$
𝑛 ∑︁ 𝑛 ∑︁ 𝑛 ∑︁
𝑓𝑛(𝑥) = 𝑤𝑖(𝑥)𝑌𝑖= 𝑤𝑖(𝑥) 𝑓∗(𝑋𝑖) + 𝑤𝑖(𝑥)𝜀𝑖
𝑖=1 𝑖=1 𝑖=1
$$

with 𝜀𝑖= 𝑌𝑖−𝑓∗(𝑋𝑖) linked with the noise of having observed 𝑌𝑖when we would have preferred to observe 𝑓∗(𝑋𝑖).

Universal consistency. While this pricing method sounds really sensible, the job of statisticians is to make formal statements to prove its soundness. The most classical statement is to prove that when the number of examples goes to inﬁnity, we retrieve the optimal pricing rule. This property is known as consistency. Consistency is usually deﬁned formally through convergence in probability (although some prefer to deﬁne it with convergence almost surely) of the risk R( 𝑓𝑛), which is seen a random variable depending on the sampling of the dataset D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼𝜌⊗𝑛, toward the inﬁmum risk R∗. Methods that are consistent without assumptions on the solution 𝑓∗are known as universally consistent.

Consistency of local averaging methods has ﬁrst been derived by Stone (1977). In essence, it consists in assuming that the noises (𝜀𝑖)𝑖≤𝑛are well-behaved, such that Í𝑛 𝑖=1 𝑤𝑖(𝑥)𝜀𝑖cancels out as the number of samples 𝑛goes to inﬁnity, and assuming the weighting scheme concentrates locally around 𝑥such that, for 𝜌X -almost all 𝑥, informally,

$$
𝑛 ∑︁ ∫
1 𝜌X (𝐵(𝑥, 𝑟))
lim 𝑛→+∞𝑓𝑛(𝑥) = lim 𝑤𝑖(𝑥) 𝑓∗(𝑋𝑖) = lim 𝑓∗(𝑡)𝜌X (d𝑡) = 𝑓∗(𝑥).
𝑛→+∞ 𝑟↓0 𝐵(𝑥,𝑟)
𝑖=1
$$

The last inequality being due to Lebesgue diﬀerentiation theorem (the derivative of the integral of a function equals the original function), which is true when 𝑓∗is bounded.

Curse of dimensionality. Once universal consistency has been derived, statisticians focus on asymptotic rates of convergence, as well as non-asymptotic generalization bounds. Those results are more informative than universal consistency, similarly to the fact that concentration inequalities are arguably stronger than the central limit theorem which is stronger than the law of large numbers. When providing non-asymptotic

<!-- page: 25 -->

generalization bounds, we should specify a loss function. When we output continuous values, Y = R, for algebraic reasons, people tend to use the mean-squares loss, deﬁned as ℓ(𝑧, 𝑦) = ∥𝑧−𝑦∥2. In this setting, 𝑓∗(𝑥) = E𝜌[𝑌| 𝑋= 𝑥], and under the condition that 𝑓∗is Lipschitz plus some mild condition on 𝜌and classical assumptions on the weighting scheme (Györﬁet al., 2002), it is possible to get convergence rates of the type

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤𝑐𝑛−2 𝑑+2 , (2.5)
$$

(2.5)

for 𝑐a constant depending on the hardness of the problem, and 𝑑the dimension of the input space X. The dependence in 𝑑is explained by the fact that to cover the space [0, 1]𝑑with precision 𝜀in order to have meaningful neighbors to predict the value of a Lipschitz function, one need 𝜀−𝑑points. Meaning that as the dimension increases, one will need exponentially more points in order to guarantee a given risk level, a phenomenon which is referred to as the curse of dimensionality. The curse of dimensionality is troublesome for machine learning problems where the input dimension can be really large such as on images with millions of pixels.

Leveraging smoothness and higher-order information. It is possible to break the curse of dimensionality in (2.5) by leveraging additional assumed structure of 𝑓∗. In particular, if 𝑓∗admits smooth derivatives, one can use Taylor formula, and try to infer derivatives values by ﬁnite diﬀerences. This will lead to a much more precise estimate 𝑓𝑛of 𝑓∗. In particular, if 𝑓∗is 𝑠+ 1 times diﬀerentiable in every direction, when a zeroth order Taylor expansion makes a local error of order 𝜀, an 𝑠-th order expansion will make an error of order 𝜀𝑠. As such, it is natural to hope for an estimator 𝑓𝑛that achieve the following generalization bound,

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤𝑐𝑛−2𝑠 𝑑+2𝑠, (2.6)
$$

(2.6)

This is exactly the rates that local polynomial methods are achieving. We refer to Tsybakov (2009) for additional details on the matter. Note that higher-order derivatives need more points in the neighborhood of 𝑥 in order for ﬁnite diﬀerence methods to provide a good estimate of those derivatives. As such, we might expect a transitory regime, before the number of samples 𝑛gets suﬃciently large, where there are not enough points in the neighborhood of 𝑥to beneﬁt from high-order smoothness.

### 2.4.2 Reproducing kernel methods

Suppose that you are the same real agent, and that you encounter a new house that is really diﬀerent from the one you have in your database, so that local averaging prediction is meaningless. For example, suppose that the house is huge, but it is not close to any good schools, and while you have already sold big houses, or houses without good nearby schools, you have no records for big houses without good nearby schools. Then a natural idea is to proceed with factor analysis, trying to ﬁgure how the price of a house is driven by its size, and by good nearby schools. Simple factor analysis model supposes that characteristics 𝑥∈R𝑑combine linearly to form the output 𝑦∈R. This leads to the search of an estimate 𝑓𝑛as a linear model 𝑓𝑛(𝑥) = 𝑤⊤𝑥, for 𝑤∈R𝑑to be determined in order to ensure that 𝑓𝑛(𝑋𝑖) ≈𝑌𝑖on your training dataset (𝑋𝑖,𝑌𝑖)𝑖≤𝑛.

Packing features. Consider the case where X = R and when plotting (𝑋𝑖,𝑌𝑖)𝑖≤𝑛seems to indicate that a quadratic relationship links 𝑥to 𝑦rather than a linear one, as illustrated on Figure 2.1. In this case, one can enrich the input 𝑥with the features 𝜑(𝑥) = (1, 𝑥, 𝑥2) ∈R3, and perform a linear regression with the data (𝜑(𝑋𝑖),𝑌𝑖)𝑖≤𝑛. When it is hard to visualize the relationship between 𝑥and 𝑦, one might be tempted to concatenate a lot of features in the vector 𝜑(𝑥) in order to make sure to be able to predict 𝑦from 𝜑(𝑥). However, such a technique is prone to learn spurious correlation between features and outputs of the training data, and not to generalize well to unseen I/O pairs. This phenomenon is called overﬁtting.

Avoiding overﬁtting. If we directly ﬁnd the predictor 𝑓𝑛(𝑥) = 𝑤⊤𝜑(𝑥) by minimizing Í 𝑖ℓ(𝑤⊤𝜑(𝑋𝑖),𝑌𝑖), our method will likely overﬁt the training data. Overﬁtting is often the fruit of a linear combination of features 𝜔⊤𝜑(𝑋) ≈0 for 𝜔∈R𝑑(assuming 𝜑(𝑋) ∈R𝑑) that is noise spuriously correlated with 𝑌on the training data (𝑋𝑖,𝑌𝑖)𝑖≤𝑛, leading to 𝑤= 𝐶· 𝜔for a big 𝐶. As a consequence, a way to avoid overﬁtting is to constraint 𝑤 to have a small norm, or to look for the minimizer of the regularized objective 1 Í

𝑖ℓ(𝑤⊤𝜑(𝑋𝑖),𝑌𝑖) + 𝜆Ω(𝑤), for Ω : R𝑑→R a regularizing function and 𝜆∈R+ a regularizing parameter. To ease this minimization, it is possible to use Ω(𝑤) = ∥𝑤∥2

$$
𝑛
$$

2. An interesting alternative is to use the ℓ1-norm Ω(𝑤) = ∥𝑤∥1 as it pushes 𝑤

<!-- page: 26 -->

y y y x x x

[FIGURE: Figure 2.1]

Figure 2.1: Plotting (𝑋𝑖,𝑌𝑖)𝑖≤𝑛(left) indicates that a quadratic regression (right) is better suited to derive 𝑦from 𝑥 than a linear regression (middle). However a quadratic regression is nothing but a linear regression with features (1, 𝑥, 𝑥2). to be sparse (Tibshirani, 1996), which makes the predictor 𝑓𝑛(𝑥) = 𝑤⊤𝜑(𝑥) relatively simple to interpret. Sparsity is a rich concept (Bach et al., 2012), yet it was not a focus of this thesis. In the following, we will consider Ω(𝑤) = ∥𝑤∥2

2.

Kernel methods. When minimizing Í

$$
𝑖ℓ(𝑤⊤𝜑(𝑋𝑖),𝑌𝑖) + 𝑛𝜆∥𝑤∥2
$$

2, it is clear that 𝑤∗∈Span(𝜑(𝑋𝑖))𝑖≤𝑛 as any part of 𝑤supported on the orthogonal of the span of the (𝜑(𝑋𝑖))𝑖≤𝑛will not change the value of any 𝑤⊤𝜑(𝑋𝑖) but will higher ∥𝑤∥2, a fact that is referred as the representer theorem (Scholkopf and Smola, 2001). Looking for 𝑤∈R𝑑under the form 𝑤= Í 𝑖𝛼𝑖𝜑(𝑋𝑖) with 𝛼∈R𝑛leads to the new problem Í 𝑖ℓ([𝐾𝛼]𝑖,𝑌𝑖) + 𝜆𝛼⊤𝐾𝛼, with 𝐾= ( )𝑖,𝑗≤𝑛∈R𝑛×𝑛, [𝐾𝛼]𝑖the 𝑖-th entry of the vector 𝐾𝛼∈R𝑛and 𝑓𝑛(𝑥) = Í

$$
𝜑(𝑋𝑖), 𝜑(𝑋𝑗)
$$

𝑖𝛼𝑖⟨𝜑(𝑋𝑖), 𝜑(𝑥)⟩. As one can notice, everything can be expressed through the scalar product 𝑘: X × X →R+; (𝑥, 𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩, forgetting about the features map 𝜑: X →R𝑑. As such, rather than making explicit the features, one can make explicit the kernel 𝑘, under the sole condition that for any 𝑚∈N and (𝑥𝑖)𝑖≤𝑚∈X 𝑚, 𝑘(𝑥𝑖, 𝑥𝑗)𝑖,𝑗≤𝑚is symmetric semideﬁnite positive. In particular, when X is a collection of structured objects, it can be easier to describe how similar are two 𝑥through 𝑘rather than deriving features 𝜑.

When ℓ(𝑧, 𝑦) = ∥𝑧−𝑦∥2, the empirical risk minimization admits a closed form solution

$$
𝑓𝑛(𝑥) = 𝐾⊤ 𝑥(𝐾+ 𝑛𝜆𝐼)−1Y, ∫
$$

with Y = (𝑌𝑖)𝑖≤𝑛∈R𝑛and 𝐾𝑥= (𝑘(𝑋𝑖, 𝑥))𝑖≤𝑛∈R𝑛. As 𝑛, the number of data, goes to inﬁnity, this converges to 𝑓𝜆(𝑥) = ¯𝐾𝑥( ¯𝐾+ 𝜆𝐼)−1 𝑓∗where ¯𝐾operates on functions as ¯𝐾( 𝑓) = 𝑥→ 𝑘(𝑥, 𝑥′) 𝑓(𝑥′) d𝜌X (𝑥′) and ¯𝐾𝑥( 𝑓) = ¯𝐾( 𝑓)(𝑥). And as 𝜆goes to zero, under mild reachability assumption, 𝑓𝜆converges to 𝑓∗(Caponnetto and De Vito, 2006). An advantage of kernel methods is that it reduces the search of 𝑤∈R𝑑to the search of 𝛼∈R𝑛which is valuable when 𝑑>> 𝑛. This is known as the “kernel trick”.

Reproducing kernel Hilbert space (RKHS). Kernel methods are backed-up by a rich mathematical concept, linked with well-behaved classes of functions. It can be introduced in a completely diﬀerent fashion, as it has been historically by Aronszajn (1950). Consider a scalar product of functions mapping X to Y = R and the class of functions F =

$$
n 𝑓: X →Y ∥𝑓∥= √︁ ⟨𝑓, 𝑓⟩< +∞ o
$$

. Suppose also that the evaluation maps 𝐿𝑥: F →R; 𝑓→𝑓(𝑥) are bounded linear operators. This implies the existence of representer 𝑘𝑥∈F such that the “reproducing property” 𝐿𝑥( 𝑓) = ⟨𝑘𝑥, 𝑓⟩holds for any 𝑥∈X and 𝑓∈F. It can be shown that

$$
𝑓: X →Y ⟨𝑓, 𝑓⟩< +∞
$$

∥·∥. One inclusion is due to the fact that 𝑘𝑥∈F and that F is close by linear combination and completion; the other due to the fact that if 𝑓∈F ∩(𝑘𝑥)⊥ F is the completion of the linear combination of (𝑘𝑥)𝑥∈X , F = Span(𝑘𝑥)𝑥∈X 𝑥∈X than 𝑓(𝑥) = ⟨𝑘𝑥, 𝑓⟩= 0. Hence, there is a unique association between the kernel 𝑘: X × X →R; (𝑥, 𝑥′) →⟨𝑘𝑥, 𝑘𝑥′⟩and the so-called reproducing kernel Hilbert space F (Mercer, 1909).

Smoothness adaptability. Under the knowledge that the target function 𝑓∗belongs to a RKHS F, using the associated kernel 𝑘generates good learning rates, akin to linear regression. Moreover, when using the mean-squares error, one can guarantee universal consistency of the method described above, under the assumption that F is dense in 𝐿2(𝜌X ), a property that is veriﬁed for many usual kernels (Micchelli et al., 2006). But what about the rates in this case, do they deteriorate badly when 𝑓∗∉F? How does kernel methods adapt to the regularity of the function 𝑓∗? Indeed the operator ¯𝐾introduced above provides the

<!-- page: 27 -->

answer. In fact, it is possible to show that 𝐿2(𝜌X ) = im ¯𝐾0 and F = im ¯𝐾1/2 (we provide many details on this operator in sections 5.C and 9.C), and that by only adapting the regularization parameter 𝜆(which is usually done through cross-validation) the excess of risk for the least-squares error of the estimator introduced above is O(𝑛−2𝑞/(2𝑞+1)) for the biggest 𝑞∈(0, 1) such that 𝑓∗∈im ¯𝐾𝑞(Caponnetto and De Vito, 2006).

Transitory regimes. While research papers tend to showcase rates that are best in terms of exponents raising the number of samples, those rates are often not observed in practice before accessing a high number of samples. As such, practitioners might prefer to write

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤inf 0≤𝑡≤𝑞𝑐𝑡𝑛−2𝑡 2𝑡+1 , (2.7)
$$

(2.7)

for the biggest 𝑞∈(0, 1) such that 𝑓∗∈im ¯𝐾𝑞, and some constants (𝑐𝑡)0≤𝑡≤𝑞. The transitory regime corresponds to the case where the best bound is not achieved for 𝑡= 𝑞, and which is when, if the kernel 𝑘is leveraging smoothness, points are too far apart to beneﬁt from higher-order information.

### 2.4.3 Neural networks and deep learning

Most of the state-of-the-art algorithms derived through machine learning are currently based on deep learning. Deep learning consists in long artiﬁcial neural networks. Artiﬁcial neural networks are a cascade of linear operators and non-linearities that are optimized through gradient descent on empirical risks. This model appeared in the middle of the 20th century (McCulloch and Pitts, 1943; Rosenblatt, 1958), and were advocated by a few researchers in the 90s (LeCun and Bengio, 1995). It rose to dominance when implemented on graphical processing units, achieving astonishing results on image recognition (Krizhevsky et al., 2012).

Cascade of linear operation. A neural network 𝑓𝑛: R𝑑→R𝑚with three hidden layers is parametrized with four matrices 𝑊1 ∈Rℎ1×𝑑, 𝑊2 ∈Rℎ2×ℎ1, 𝑊3 ∈Rℎ3×ℎ2, 𝑊4 ∈R𝑚×ℎ3 and reads

$$
𝑓𝑛(𝑥) = 𝑊4𝜎(𝑊3𝜎(𝑊2𝜎(𝑊1𝑥))),
$$

with ℎ1, ℎ2, ℎ3 ∈N the number of neurons in the ﬁrst, second and third hidden layers, 𝜎: R →R a non-linearity, e.g. 𝜎(𝑥) = max(𝑥, 0), and the convention 𝜎((𝑥1, · · · , 𝑥𝑛)⊤) = (𝜎(𝑥1), · · · , 𝜎(𝑥𝑛))⊤. We illustrate it in Figure 2.2. Given a loss ℓ, some data D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛, a regularizer term 𝜆Ω(𝑊1, 𝑊2, 𝑊3, 𝑊4) and the consequent regularized empirical risk RD𝑛, the parameters 𝑊1, 𝑊2, 𝑊3, 𝑊4 can be optimized in order to minimize RD𝑛( 𝑓𝑛). This minimization is usually done with gradient descent, or stochastic gradient descent (Robbins and Monro, 1951), which is better suited for large scale learning problems (Bottou and Bousquet, 2007). Gradients are obtained thanks to the chain rule, and while the computation of 𝑓(𝑥) can be seen as forward propagation from 𝑥to 𝑊1𝑥to 𝑊2𝜎(𝑊1𝑥) and so on, the chain rule naturally leads to backward propagation or backpropagation, which is the name used by researchers to refer to the derivation of gradients with neural networks. Astonishingly, while such a procedure is supposed to stall into undesirable local minima, it has not constrained the recent successes of deep learning.

Hierarchy and convolution. In the last paragraph, we have described the most basic architecture of a neural network, only made of fully connected layers. There are many architectures that reﬁne this basic neural network, the most well known are recurrent neural networks (Williams et al., 1986) that allow dealing with time series of diﬀerent length and convolutional neural networks that were proven successful to understand images (LeCun et al., 2015). We refer the interested reader to this last paper to get a more precise idea on what convolutional neural networks are. In substance, a one dimensional convolutional ﬁlter replaces the linear mapping Rℎ𝑖→Rℎ𝑜𝑥→𝑊𝑥with 𝑊∈Rℎ0×ℎ𝑖by the linear mapping Rℎ𝑖→Rℎ𝑖−𝑝; 𝑥→𝑤∗𝑥with 𝑤∈R𝑝and (𝑤∗𝑥)𝑖= Í𝑝 𝑗=1 𝑤𝑖𝑥𝑖+𝑗. This is useful when 𝑥has a translation-invariant structure (Fukushima, 1980). Rather than learning to recognize the same pattern at diﬀerent places by tuning similarly diﬀerent columns of 𝑊, it allows for parameter sharing. As one ﬁlter allows for the recognition of one pattern, a convolutional layer is made of several ﬁlters, whose responses are concatenated along a new dimension in order to form the layer output. After passing through a ﬁlter bank, the response is usually pruned by keeping only local maxima, an operation known as max-pooling. This subsampling operation builds a hierarchical structure, allowing for further ﬁlters to learn broader patterns (Behnke, 2003). Translation invariance and hierarchy are two important concepts (Simon, 1962; Mallat, 1989) that have been used to design others “hand-made” methods that were used in the past to analyze images (Lowe, 1999; Dalal and Triggs, 2005).

<!-- page: 28 -->

$$
𝑥 𝑥1 = 𝜎(𝑊1𝑥) 𝑥2 = 𝜎(𝑊2𝑥1) 𝑥3 = 𝜎(𝑊3𝑥2) 𝑦= 𝑊4𝑥3
$$

[FIGURE: Figure 2.2]

Figure 2.2: Representation of a neural network with three hidden layers and parameters (𝑑, ℎ1, ℎ2, ℎ3, 𝑚) = (3, 5, 5, 4, 2), as a weighted directed acyclic graph. The input 𝑥= (𝑥(𝑖)) ∈R3 is passed through the ﬁrst set of edges, leading to the ﬁrst layer with value 𝑥1 = (𝑥1,(𝑖)) ∈R5 speciﬁed by 𝑥1,(𝑖) = 𝜎(Í 1≤𝑗≤3 𝑊1,(𝑖,𝑗)𝑥( 𝑗)) based on the set of weights 𝑊1 = (𝑊1,(𝑖,𝑗)) ∈R5×3 and the non-linearity 𝜎: R →R, and so on until reaching the output 𝑦∈R2. The wording “deep learning” refers to learning with neural networks that have a really large number of hidden layers, which can lead to hundreds of billions of parameters (see e.g. Brown et al., 2020).

Plethora of architectures. While convolutional neural networks are the model of choice to work with images, they do not exhaust what deep learning is about. Recently, transformer models (Vaswani et al., 2017) have become the model of choice to deal with time series in natural language processing, with amazing realizations in language understanding (Devlin et al., 2019) and text generation (Brown et al., 2020), and generative adversarial networks (Goodfellow et al., 2014) introduced earlier have also led to impressive applications such as “deepfakes” (Karras et al., 2019), which are synthetic images that look real and might be used for malicious purposes. The rapid spread of deep learning is partly due to its ease to implement through diﬀerential programming libraries that implement automatic diﬀerentiation and backpropagation when forward propagation is speciﬁed (Abadi et al., 2016; Paszke et al., 2019). This allows practitioners to easily develop and test new ideas and architectures, even though training neural networks is known to be quite unstable and greedy in terms of time and energy (see e.g. García-Martín et al., 2019).

Statistical properties. While neural networks work better than local averaging and kernel methods, statisticians have not arrived at a consensus in order to describe theoretically why neural networks work so well. In particular, it is currently hard to state generalization bounds akin (2.5), (2.6) and (2.7). Because of their wide-spread use, many are trying to derive a better understanding of those models. Some are trying to come up with similar models based on concepts that are better understood such as wavelets (Bruna and Mallat, 2013), kernels (Mairal et al., 2014) or sparse coding (Papyan et al., 2017). Others are looking at the properties of neural networks once the training has taken place (Mahendran and Vedaldi, 2015; Selvaraju et al., 2017), notably discovering the possibility to fool them with imperceptible noise (Szegedy et al., 2014; Ilyas et al., 2019). Finally, statisticians are trying to explain some of their characteristics with diﬀerent tools, could it be some measure of complexity (Bartlett et al., 2017; Zhang et al., 2021), group theory and harmonic analysis (Mallat, 2016), statistical physics (Spigler et al., 2019) or asymptotic limit (Jacot et al., 2018; Chizat et al., 2019; Mei and Montanari, 2022).

## 2.5 The practice

In this section, we discuss the daily job of data scientists before confronting this reality with the prior theory in order to discuss the limitations of the supervised learning framework.

### 2.5.1 The job of data scientists

There are arguably four steps in a project of a data scientist when it comes to machine learning. While we present those tasks in a downstream fashion, in practice, it is important to get a big picture and a rough sketch

<!-- page: 29 -->

of each step ﬁrst in order to ease the transitions between steps and avoid going back too often to prior steps. All along the process, intuition can be found by reﬂecting on how the work would be accomplished manually, that is without learning perspectives.

1. Deﬁne the problem. First of all, data scientists should be clear about the task to solve, look at the current solution, and see how it can be improved with machine learning. In order to prove the usefulness of the new method, they should deﬁne some clear measures of success, and benchmark simple baselines. At this point comes the deﬁnition of the output space Y and of the loss ℓ: Y × Y →R that should be deﬁned in coherence with the precedent measures of success. Once the target space Y is well-deﬁned, the next step is to ﬁnd a set of relevant features that deﬁnes the input space X and allows prediction of targets. Of course, the features that can be accessed, hence the deﬁnition of X, depend on the data one can get.

2. Get clean data. Once X and Y are well-deﬁned, it is time to ﬁnd a set of I/O examples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛. This is often the most time-consuming task. How many samples are needed regarding the statistical hardness of the task at hand? Where to scrap data? How to easily associate outputs to inputs? Once enough samples have been collected, it is usual to set aside a part of those to form a test dataset, that would only be looked at before deployment to validate the working status of the built system. The remaining data form the train set. At this point, data is often very cluttered, implying a consequent amount of cleaning before feeding a machine learning model. In particular, when collected from diﬀerent sources, there might be some coordinates missing for various input samples. For example when working with countries, it will be hard to get an indication of the number of people below poverty line in North Korea. A decision should be made with those missing data, could it be ﬁlling with the feature average, or dropping completely the corresponding sample. Similarly, the practitioners might have to deal with outliers or data sources that got stalled on wrong values.

3. Train a model. Once clean data have been collected, machine learning models are ready to be trained. In order to help models, some features engineering might be useful, such as centering and normalizing the variance of the data, or applying more advanced transformations to get samples that are well-behaved, e.g. following a unit Gaussian distribution. It is usual to combine diﬀerent models together, when those models capture diﬀerent relationships between inputs and outputs, in order to boost the overall performance, a procedure known as boosting (Schapire, 1990). Hyperparameters are generally tuned with cross-validation. Cross-validation consists in splitting the samples into a given number of folds, using all the folds but one to train the models and getting a measure of success on the last fold before averaging this measure over the diﬀerent folds that can be retained for testing. This associates a score to a method with a given set of hyperparameters. Best hyperparameters are chosen as the ones leading to the highest score. Practitioners should be careful not to try too many models or hyperparameters as the more they try, the more likely will be learned spurious correlations that only explain the training samples I/O relationship.

4. Deploy the model. Once a model has been learned to predict output from input, one should excavate the test dataset, and see if the method performs better than baselines. If so, it is time to beneﬁt from this new method and put it into production. At this point, it is important to monitor the quality of new input data, to make sure that it is not corrupted, and that its distribution is similar to the distribution of training data. There might also be an emphasis on engineering problems, such as managing databases and computing architectures.

For the curious reader, there are many good references to prepare future data scientists for their job (see e.g. Géron, 2017).

### 2.5.2 Framework limitations

Loss design. In the formalization of supervised learning that we gave earlier, we assumed that the loss ℓ: Y × Y →R is clearly deﬁned and that the risk R to minimize is nothing but the average over samples of the error made by a predictor measured with this loss. In some critical applications, such as medical one, one might prefer to build RD𝑛as the worst case of (ℓ( 𝑓(𝑋𝑖),𝑌𝑖)) or build R as some quantile of the pushforward distribution ℓ( 𝑓(·), ·)#𝜌rather than building them as their respective means. Moreover, in practice, it might be hard to deﬁne clearly the loss ℓ. For example, it is the case when it comes to style transfer, that is taking two images and outputting an image with the content of the ﬁrst one and the style of

<!-- page: 30 -->

the second, or to super-resolution, that is enhancing the resolution of an image (Johnson et al., 2016). The same is true with our cooking example, how to access the quality of a recipe derived by a computer? Should it be the most healthy, the most tasty or somewhat healthy and tasty? Can we derive such losses based on chemical considerations? Or should we only measure success based on people reviews, meaning high costs to evaluate the risk R?

Sometimes, losses can be partially or totally designed by leveraging the structure of the problem. For example, on problems where there is a desired invariance deﬁned by a set 𝐺of functions 𝑔: X →X such that we should have 𝑓◦𝑔= 𝑓, if this invariance is not built into the model, it can be built into the loss by replacing ℓ( 𝑓(𝑋),𝑌) with Í 𝑔∈𝐺ℓ( 𝑓(𝑔(𝑋)),𝑌), which is notably the idea of “data augmentation”. Another example is when we have a parametric model of the relation between 𝑋and 𝑌, 𝑌= 𝑔(𝑋, 𝜃, 𝜀) for 𝑔a known function, 𝜃an unknown parameter to optimize and 𝜀some random noise. The parameter 𝜃can be ﬁtted by maximizing the likelihood of having observed D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛under the model. Assuming the samples are independent, this probability factorizes as the product of the probability of observing each (𝑋𝑖,𝑌𝑖). As a consequence, maximizing the likelihood, or equivalently the log-likelihood, is similar to minimizing the risk R deﬁned through the loss ℓ(𝑋,𝑌, 𝜃) = −log P (𝑌| 𝑋; 𝜃) with the last term designing the probability of observing 𝑌given the observation of 𝑋under the model parametrized by 𝜃. When the parametric model is an exponential family, this procedure is to be linked with generalized linear models (Nelder and Wedderburn, 1972).

Independent identically distributed variables? Suppose you want to predict annual growth from indica- tors, such as the gross domestic product, regarding a country. You might collect a dataset (𝑋𝑐,𝑡,𝑌𝑐,𝑡)𝑐∈𝐶,𝑡∈𝑇 with many countries, indexed by a set 𝐶, and many years, indexed by a set 𝑇, features 𝑋and corresponding growth 𝑌, but this dataset will violate the independent identically distributed assumption of statistical learning. For example, an oil crisis happening in year 𝑡will have a repercussion on each (𝑌𝑐,𝑡)𝑐∈𝐶, and if one try to add oil prices in the features 𝑋to enforce the independence of the conditional variables 𝑌𝑐,𝑡

$$
𝑋𝑐,𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

𝑐∈𝐶, than the (𝑋𝑐,𝑡)𝑐∈𝐶will not be independent as this factor will be constant over countries. Similarly, for a given country, indicators are arguably forming a non-stationary process that depends on politics in place, hence (𝑋𝑐,𝑡)𝑡∈𝑇is not a family of independent random variables. However, many data scientists might be tempted to still use the many resources provided by supervised learning, without trying to leverage the underlying processes.

More importantly, suppose that one trains a model on western countries, beneﬁting from higher quality data, before deploying the model to help some decision-making in developing countries. There might be some important cofactors such as quantitative easing policies, or trust of populations in money, that change completely the picture when it comes to predicting growth from country indicators. As such, the testing distribution is not the same as the training distribution, a phenomenon known as covariate shift (Heckman, 1979; Shimodaira, 2000). Recently, this problem has come back to denounce the risk of automatic systems that reproduce human-biases (Caliskan et al., 2017), which has found an echo in the civil society (Benjamin, 2019). Interestingly, while data scientists often try to artiﬁcially squeeze their problems into the framework of supervised learning, many researchers are trying to leverage speciﬁc settings, such as the fact that data might be coming from diﬀerent datasets (Arjovsky et al., 2019).

Practice and theory regarding generalization. In theory, generalization error might be given by deriva- tions allowing to get results such as (2.5), (2.6) and (2.7). In practice, those bounds might be hard to compute because of unknown constants, yet they provide precious insights on the number of samples to consider in order to achieve statistical signiﬁcance. For example, bounds reading 𝑑/𝑛suggests that the number of samples 𝑛should be bigger than the number of dimensions 𝑑of the input space X, while bounds in 𝑛−1/𝑑 suggests that the number of samples should be exponentially bigger than the number of dimensions. Anyhow, data scientists mostly compute generalization scores by computing the empirical risk of a predictor 𝑓𝑛on a fresh test set of data. According to this practice, researchers might study the beneﬁts of the test set validation procedure. For example, they may leverage the distribution of the empirical test error in order to transform a predictor 𝑓𝑛: X →Y into a conﬁdence interval predictor 𝑓𝑛: X →2Y with a given probability to be valid (Vovk and Shafer, 2008).

<!-- page: 31 -->

# Chapter 3. Learning Rates with Discrete Outputs

Understanding the reliability of machine learning is crucial to deploy learned models in the wild. It was also an important point of this thesis that focuses on algorithms for weakly supervised learning with appreciable theoretical guarantees. This chapter elaborates on such guarantees and discusses some of our work (Cabannes et al., 2021c; Cabannes and Vigogna, 2022), which is reproduced entirely in part II. For simplicity, it is set in the supervised learning formalization made in the precedent chapter. In particular, we consider X ⊂R𝑑an input space, Y a discrete output space, 𝜌a joint distribution on X × Y, and ℓa loss function. Our goal is to minimize the risk R : YX →R deﬁned as

$$
R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] . (3.1)
$$

(3.1)

## 3.1 Statistical learning theory

In this section, we discuss results oﬀered by statistical learning theory to get insights on what can be learned from data. In particular, we get more precise about classical derivations of generalization bounds.

### 3.1.1 Insights from information theory

Artiﬁcial intelligence designs a putative system created by humans that would display signs of intelligence, whatsoever this means. Machine learning consists in implementing such a system with a machine that learns, i.e. ﬁnds in a sort of autonomous fashion, how to behave in order to produce a desired output given some input parameters. Statistical learning consists in presenting the machine with a set of training examples that show desired outputs for diﬀerent inputs in order for the machine to infer a rule to produce outputs from inputs. Statistical learning theory borrows many tools from information theory.

Information theory is concerned with transmitting information. Think that we want to describe a function 𝑓: X →Y to a friend, with only a ﬁnite number of information. If we know that 𝑓belongs to a ﬁnite set of functions F, based on dichotomy, we only need log2(|F|) bits to encode this function among all functions in F. Now, if F is continuous, we cannot encode all functions on a ﬁnite number of bits. Yet, if we only want to unravel a signal 𝑓∈F up to a precision 𝜀, given a certain error metric1 𝐿(typically 𝐿( ˆ𝑓, 𝑓) = E

$$
ℓ( ˆ𝑓(𝑋),𝑌) −ℓ( 𝑓(𝑋),𝑌)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

), we could do so with an encoding on less than

$$
log2(N (𝜀))
$$

, with N (𝜀) the minimum number of balls of size 𝜀(with the metric 𝐿) to cover F. To quantify the complexity of the set F, it is natural to look at the behavior of the number of bits we need to encode any function in F up to an error 𝜀as 𝜀get to zero. As a consequence, it is useful to deﬁne a notion of size of F (with respect to the error metric 𝐿) as the superior limit

$$
\frac{𝐶F = lim sup}{𝜀→0} −log2(N (𝜀))/log2(𝜀).
$$

Note the analogy with statistical mechanics, where signals are microscopic arrangements of unit elements, and the set F is the corresponding macroscopic system. Assuming that all arrangements have the same probability to appear, the Boltzmann entropy is exactly, up to the Boltzmann constant, the logarithm in base 1Here, the word “metric” is used in a prosaic fashion since 𝐿might not be a distance.

29

<!-- page: 32 -->

two of the cardinality of F. This explains the wording Kolmogorov entropy for the logarithm in base two of the covering number N.

To make the preceding paragraph more concrete, suppose that we want to transmit a function 𝑓: [0, 1]𝑑→R to our friend. Typically, we would give to our friend 𝑚bits of discrete information, plus some information on the function class (e.g. 𝑓is a polynomial of order 𝑑, or, thinking in terms of Fourier transform, it has a low energy on high harmonics). For example, assume that 𝑓belongs to the Sobolev space 𝐻𝑚(d𝑥), i.e. it is 𝑚times diﬀerentiable, with derivatives up to order 𝑚square integrable against the Lebesgue measure. Suppose that our friend knows that ∥𝑓∥𝐻𝑚≤1, and suppose that we want to minimize the 𝐿2 error. Then, we can give 𝑛binary information to localize this function in a covering of F = { 𝑓| ∥𝑓∥𝐻𝑚≤1} with 2𝑛 𝐿2-balls.2 At best, our friend will be able to localize the signal in an 𝐿2-ball of radius 𝜀(2𝑛), thus making at most an error 𝜀(2𝑛) on the reconstructed signal, with 𝜀(𝑛) = inf [𝜀| N (𝜀) ≤𝑛] ≈𝑛−𝐶F , and 𝐶F the size of F with respect to the 𝐿2-metric. We refer the interested reader to the seminal paper of Kolmogorov and Tikhomirov (1959) for precise quantiﬁcation of space sizes.

### 3.1.2 Vapnik-Chervonenkis theory

Machine learning is concerned with inferring information. In this setting, we want to learn a task 𝑓: X →Y, and we do so by collecting examples of the solved instance of this task (𝑥𝑖, 𝑦𝑖= 𝑓(𝑥𝑖)). In the current machine learning paradigm, we do not choose the bits of information to transmit, but we are given some points (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛that are assumed independently sampled according to the distribution that matters to us. Let us review the picture oﬀered by the classical statistical learning theory for the sake of completeness. Recall that we want to study the excess of risk. We have, with 𝑓∗ F and 𝑓𝑛the respective minimizers of the population and empirical risks over F,

$$
R( 𝑓𝑛) −R( 𝑓∗ F) ≤R( 𝑓𝑛) −RD𝑛( 𝑓𝑛) + RD𝑛( 𝑓∗ F) −R( 𝑓∗ F).
$$

For any function 𝑓∈F, we can use concentration inequality (such as Bernstein inequality) to control the diﬀerence between the empirical risk RD𝑛( 𝑓), which inherits its randomness from D𝑛, and its average R( 𝑓). This works well for the second part of the equation, due to 𝑓∗ F. Sadly, as 𝑓𝑛depends on D𝑛, we can not apply concentration inequality directly to control the deviation between its empirical and population risk. The classical way to proceed is to ﬁnd a uniform concentration bound over F, which we can do by controlling the following random quantity

$$
sup_{𝑓∈F} R( 𝑓) −RD𝑛( 𝑓).
$$

When F is ﬁnite, we can control this supremum with a union bound, joining together all individual concentration inequality. Similarly, when F is continuous, we could do similar things with a well-speciﬁed 𝜀-cover of F, which can be reﬁned based on chaining techniques, to avoid redundancy of events when performing union bound for supremum. In the statistical learning literature, it is classical to rather use a symmetrization trick to relate R( 𝑓) −RD𝑛( 𝑓) to RD′𝑛( 𝑓) −RD𝑛( 𝑓) for D′ 𝑛another dataset, and study the Rademacher complexity deﬁned as E sup 𝑓∈F 𝑛−1 Í𝑛 𝑖=1 𝜀𝑖𝑓(𝑋𝑖) for E the expectation taken over the 𝜀𝑖deﬁned as variables taking value one or minus one with probability one half.

In the case of binary classiﬁcation with the 0-1 loss, i.e. Y = {−1, 1}, ℓ(𝑦, 𝑦′) = 1𝑦≠𝑦′, Vapnik and Chervonenkis proposed slightly diﬀerent derivations leading to the following bound.

$$
√︂
𝑉F
ED𝑛R( 𝑓𝑛) −R( 𝑓∗ F) ≤𝑐 𝑛, (3.2)
$$

(3.2)

for 𝑐a universal constant, and 𝑉F the so-called VC dimension of F, that relates to the average number of points that the class F is able to shatter (Vapnik, 1995).

A natural question with generalization bounds is how well they quantify the behavior of the excess of risk R( 𝑓𝑛) −R∗. Indeed, the estimation of the excess of risk given by (3.2) is known to be optimal, in the sense that, for any class of functions F, it is possible to ﬁnd a speciﬁc distribution 𝜌such that this bound is a lower bound up to a multiplicative constant. This behavior is referred to as minimax optimality, meaning that it is not possible to ﬁnd a better bound, given the class F of estimators considered.

2Note that such a covering of F can be taken as it is compact with respect to the 𝐿2-topology - even though it is not compact with the 𝐻𝑚-topology, 𝐻𝑚being inﬁnite dimensional.

<!-- page: 33 -->

## 3.2 Surrogate methods

In this section, we discuss the diﬃculty of learning discrete-valued functions, and the possibility to tackle the learning problem through surrogate problems that consist of learning continuous-valued functions.

### 3.2.1 Practical limitations of VC theory

While VC theory was a keystone in machine learning, it does not exhaust practitioner issues, as this theory does suﬀer from some limitations.

Approximation/estimation trade-oﬀ. First of all, VC theory controls the estimation error in (2.4), that is the error in terms of population risk R between 𝑓𝑛the minimizer of the empirical risk in a hypothesis class F and 𝑓∗ F the minimizer of the population risk in the class F. In particular, equation (3.2) does not tell anything about the approximation error, that is the gap between R( 𝑓∗ F) and R∗. To control the approximation error, we need to make assumptions on how good our model F is to minimize the risk R. There is a trade-oﬀ between choosing a big model F, so that the optimal risk R∗can be achieved by R( 𝑓∗ F) inside the hypothesis class, and choosing a small model, so that its capacity, captured by 𝐶F or VF, is small.

Optimization issues. Finally, if we were to apply VC theory to learn from a continuous input space X ⊂R𝑑, to a discrete output space Y, we could consider a model F of functions from X to Y. Those functions could be characterized through their decision regions and decisions boundaries, deﬁned for 𝑦, 𝑧∈Y as

$$
𝑓−1(𝑦) = {𝑥∈X | 𝑓(𝑥) = 𝑦} ⊂X, Δ𝑦,𝑧( 𝑓) = 𝑓−1(𝑦) ∩𝑓−1(𝑧) ⊂X,
$$

where the bar stands for the closure of the set. As such, a model F could be deﬁned as a collection of putative decision regions. The region of disagreement between two functions 𝑓and 𝑔for a prediction 𝑦∈Y can be expressed through the symmetric diﬀerence 𝑓−1(𝑦)△𝑔−1(𝑦). When using the 0-1 loss, the excess of risk between 𝑓𝑛and 𝑓∗ F is controlled by the measure of the union of disagreement regions, that is 𝜌X (∪𝑦∈Y ( 𝑓𝑛)−1(𝑦)△( 𝑓∗ F)−1(𝑦)). It is then possible to retake the VC theory, using the covering number of F with respect to this pseudo-distance (Mammen and Tsybakov, 1999). Sadly, even for a simple model F, such as binary classiﬁcation with half-plane decision regions, minimizing the empirical risk is NP-hard (Arora et al., 1997). This echoes optimization issues in machine learning. While VC theory asks to consider the empirical risk minimizer 𝑓𝑛, it might be really hard to ﬁnd it in practice, and one might have to settle with an estimate ˆ𝑓of 𝑓𝑛. This adds a third term to the risk decomposition that is an optimization error term

$$
R( ˆ𝑓) −R∗= R( ˆ𝑓) −R( 𝑓𝑛) | {z } + R( 𝑓𝑛) −R( 𝑓∗ + R( 𝑓∗ lin) −R∗ | {z } approximation error
lin) | {z } .
optimization error estimation error
$$

### 3.2.2 Related continuous surrogate problems

When learning with discrete outputs, direct risk minimization leads to many combinatorial diﬃculties that translate into computational intractability. This is related to the diﬃculties of studying and optimizing discrete-valued functions. One technique to overcome this issue consists in learning a discrete-valued function, by learning a surrogate continuous-valued function and thresholding its output in order to make it discrete. Consider binary classiﬁcation, that is Y = {−1, 1} and ℓ(𝑦, 𝑧) = 1𝑦≠𝑧. In this setting, the optimal predictor 𝑓∗: X →Y is deﬁned as

$$
𝑓∗(𝑥) = sign(𝑔∗(𝑥)), where 𝑔∗(𝑥) = E(𝑋,𝑌)∼𝜌[𝑌| 𝑋= 𝑥] .
$$

This suggests learning the discrete-valued function 𝑓∗: X →Y by learning the continuous-valued function 𝑔∗: X →R. To an estimate 𝑔of 𝑔∗, we associate the estimate 𝑓= sign(𝑔) of 𝑓∗. One method to learn the conditional expectation 𝑔∗is through its characterization with the least-squares error

$$
|𝑔(𝑋) −𝑌|2 
𝑔∗∈arg min R𝑆(𝑔) := E(𝑋,𝑌)∼𝜌 .
𝑔:X→R
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 34 -->

Given data (𝑋𝑖,𝑌𝑖), one can then consider a model of real-valued functions G ⊂RX and the empirical risk minimization

$$
\underset{𝑔∈G}{\arg\min}\, \frac{1}{𝑛} \sum_{𝑛 𝑖=1} |𝑔(𝑋𝑖) −𝑌𝑖|2 .
$$

This estimate is cast as an estimate of 𝑓∗through the decoding ˆ𝑓= sign ˆ𝑔. It is natural to wonder how a good estimate of 𝑔∗translate into a good estimate of 𝑓∗. This question is answered by calibration inequalities that relate the excess of risk on the surrogate problem with the excess on risk of the original problem (Bartlett et al., 2006). For example, for the least-squares surrogate considered here, we have

$$
R(sign 𝑔) −R( 𝑓∗) ≤ √︁ R𝑆(𝑔) −R𝑆(𝑔∗).
$$

While we only present the least-squares surrogate for binary classiﬁcation, other surrogates such as the hinge loss, leading to support vector machine, the logistic loss, leading to softmax regression, can be considered. Similarly, surrogate methods can be extended beyond binary classiﬁcation, for example, in multiclass problem with the 0 −1 loss, that is Y = {1, · · · , 𝑚} and ℓ(𝑦, 𝑧) = 1𝑦≠𝑧, we can consider 𝑔∗: X →RY, deﬁned as

$$
𝑋= 𝑥 
𝑔∗(𝑥) = (P (𝑌= 𝑦| 𝑋= 𝑥))𝑦∈Y = E (1𝑌=𝑦)𝑦∈Y ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

and the decoding

$$
\underset{𝑦∈Y}{\arg\max}\, 𝑔∗ 𝑦(𝑥).
$$

In such a setting, 𝑔∗is often referred to as a score function.

Remark 3 (The pros of predicting scores). From a formal perspective, if we are only interested in the optimal mapping 𝑓: X →Y, learning 𝑔can be seen as a waste of resources. In essence, this waste of resources is similar to the one when learning the full probability function (𝑝(𝑦))𝑦∈Y for some 𝑝∈ΔY while we only care about the argmax 𝑦∗∈arg max𝑦∈Y 𝑝(𝑦). In practice, however, it might be of interest to get an estimate of 𝑔∗(𝑥) = P (𝑌= 𝑦| 𝑋= 𝑥), as it might provide important information about how speciﬁed is 𝑓∗(𝑥) and how we could conﬁdently discard other potential labels 𝑦for the input 𝑥.

We refer the interested reader to Nowak-Vila (2021) for deeper reﬂections about learning with surrogate methods.

## 3.3 Fast rates derivation

In this section, we sketch roughly the underlying machinery beyond Cabannes et al. (2021c). While writing this section, we gave a fresh look at it to avoid redundancy with results already published and reproduced in Chapter 5. Confronting this machinery with SVM has led us to Cabannes and Vigogna (2022) which is reproduced in Chapter 6.

Regularized risk minimization. For simplicity, consider a surrogate problem consisting of learning a real-valued function; with a linear parametric model of functions G = {𝑔𝜃: 𝑥→⟨𝜃, 𝜑(𝑥)⟩| 𝜃∈Θ} ⊂RX , parametrized by some Hilbert space Θ, and some features 𝜑: X →Θ. Consider the regularized empirical risk minimization

$$
\underset{𝜃}{\arg\min}\, R𝑆,D𝑛(𝑔𝜃) + 𝜆𝑛∥𝜃∥2 .
$$

Here, 𝜆𝑛is a regularization parameter that goes to zeros as the number of samples 𝑛goes to inﬁnity and the risk of overﬁtting vanishes, and R𝑆,D𝑛is the empirical surrogate risk computed from the dataset D𝑛. Eventually, we could also consider ˆ𝜃an approximation of 𝜃𝑛related to some optimization techniques. Finally, it is useful to introduce the bias estimate 𝜃𝜆∈arg min𝜃R𝑆(𝑔𝜃) + 𝜆∥𝜃∥2 .

Classical versus new convergence study. Classically, to prove that ˆ𝑓, the decoding of 𝑔ˆ𝜃, will minimize the original risk R as 𝑛goes to inﬁnity and to give rates of convergence, one can use capacity/estimation assumptions to state that ˆ𝜃concentrate around 𝜃𝜆, as well as source/approximation assumptions to state that R𝑆(𝑔𝜃𝜆) will convergence to R𝑆(𝑔∗) as 𝜆goes to zero. Finally, using calibration inequalities, one can relate concentration in 𝜃to concentration in R𝑆, and then to concentration in R. The problem with this

<!-- page: 35 -->

level lines of R(sign(𝑔𝑛)) path {𝜃𝜆; 𝜆∈[0, 4]} region {𝜃; ∥𝜃−𝜃𝜆∥< 1} Certiﬁed value of R(𝑔𝑛) when ∥𝜃𝑛−𝜃𝜆∥< 1

$$
𝜃∗ 𝜃𝜆
$$

[FIGURE: Figure 3.1]

Figure 3.1: Our new convergence analysis consists in relating natural concentration given by the surrogate method to the original excess of risk without passing by the surrogate excess of risk. As the drawing shows, concentration in parameter space Θ can be cast as deviation on the original excess of risk. Yet, this casting relation depends on the geometry of this picture, which itself depends on which surrogate is used, what is the function to learn, how the bias estimator approaches it, and how our empirical estimate concentrates around the bias estimator. technique is that cascading calibration inequalities can lead to quite suboptimal rates, as shown by the work of Audibert and Tsybakov (2007), which bypassed this procedure, and, under a simple well-thought margin condition, derived dramatically faster convergence rates than classical ones. In our view, this work can be generalized by deriving directly calibration inequality that relates the original excess of risk to concentration in the parameter space. The speciﬁcity of those new calibration inequalities is that they are not universal, but depends on some approximation hypothesis that quantiﬁes how hard or easy it is to solve the original problem based on the parametrized surrogate problem. The most well-known such hypothesis is the Tsybakov margin condition, but others were proposed (for example by Steinwart and Scovel, 2007).

Special case of exponential convergence rates. To give more light on the previous paragraph, consider the binary classiﬁcation problem. Suppose that there exists 𝜆such that sign(𝑔𝜃𝜆) = sign(𝑔∗). Suppose also that there exists 𝜀> 0 such that ∥𝜃−𝜃𝜆∥≤𝜀implies that sign(𝑔𝜃) = sign(𝑔𝜃𝜆). With those two approximation hypothesis, we have the following calibration inequality

$$
R(sign(𝑔𝜃)) −R( 𝑓∗) ≤1∥𝜃−𝜃𝜆∥>𝜀.
$$

> 𝜀 . Assuming that this last 𝜃D𝑛 concentrated around 𝜃𝜆with sub-Gaussian tails, that is PD𝑛

$$
𝜃D𝑛−𝜃𝜆
R(sign(𝑔𝜃D𝑛))
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As a consequence, ED𝑛

$$
−R( 𝑓∗) ≤PD𝑛 

𝜃D𝑛−𝜃𝜆
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

> 𝜀 ≤exp(−𝑐𝑛𝜀2), for a constant 𝑐, we get exponential convergence rates.

## 3.4 Discussion

In this section, we discuss the practical usefulness of generalization bounds, and the diﬀerent paradigms to deﬁne and quantify learnability.

Practical bounds on expected error. In theory, generalization bounds provide guarantees on how much error we might expect when deploying a model learned from data. In practice, those bounds are rather taken as indications that the learning methods are sound, but rates are not reported in order to get conﬁdence on the learned models. This might have to do with the fact that bounds often depend on parameters or constants that are hard to know in practice. As such, practitioners often prefer to derive error indications from test samples. In this line, research on conformal prediction is trying to leverage test samples to provide useful conﬁdence information on learned models.

Assumptions to quantify learnability. Given data, it is highly valuable to get an idea of what can be learned from it. Of course, learnability depends on regularity assumptions of the problem at hand. Under such assumptions, lower bounds given by minimax rates are supposed to give optimal baselines for learning rates, thus to quantify learnability. In practice, those lower bounds are derived by considering the most degenerate function respecting those assumptions. Sometimes a simple well-thought additional assumption

<!-- page: 36 -->

$$
𝑦= sup𝜃;E𝐿(𝜃)=𝑥Eℓ(𝜃)
$$

description given by the bound reality

$$
𝑥= E𝐿(𝜃)
$$

regime well described by the bound regime observed when given few samples

[FIGURE: Figure 3.2]

Figure 3.2: The behavior described by generalization bound might be relevant only when accessing an indecently large number of samples, thus being of little use in practice. can lead to much better bounds. As such, is there a natural paradigm of assumptions on the function to learn to discuss its learnability? For example, assumptions on the surrogate solution 𝑔∗are not intrinsic to the original problem but depends on the surrogate problem that is considered. On the contrary, for a ﬁxed decoding 𝑑, one can quantify the regularity of 𝑓through the most regular function 𝑔such that 𝑓= 𝑑(𝑔) (think of the binary classiﬁcation case with 𝑑= sign), this will correspond to the regularity of the decision frontier, rather than the one of the conditional expectation 𝑥→E [𝑌| 𝑋= 𝑥]. We refer to the paragraph “Beyond least-squares” in Section 9.A.1 for a practical example of such considerations. This echoes the diﬀerence between realizable-consistency and Fisher-consistency of surrogate methods (Long and Servedio, 2013).

Non-asymptoticness of ﬁnite-sample bounds? There are two points to mention about probably approxi- mately correct bounds. First they are derived by considering worst-cases, and as we said in the previous paragraph, simple assumptions often allow reﬁning those bounds by removing pathological cases. Second they tend to describe the behavior of how risks decrease with the number of samples when accessing numerous samples. As such, while those bounds are non-asymptotic in the sense that they are valid for any number of samples 𝑛, the described regime might not take place without accessing an indecent number of data, thus being of little use in practice.

To get more concrete, consider a loss ℓand a surrogate loss 𝐿. Suppose that we want to bound the excess of risk Eℓ(𝜃) on the original problem with the excess of risk E𝐿(𝜃) on the surrogate problem, where 𝜃is a learned parameter. The goal of calibration theory is to ﬁnd the best function 𝜉such that for any 𝜃, Eℓ(𝜃) ≤𝜉(E𝐿(𝜃)). In practice, people try to ﬁnd 𝜉concave (because the inequality can be derived for a single 𝑥and propagated to the whole space thanks to Jensen inequality), and will look for it under the form 𝜉(𝑥) = 𝑐𝑥𝛼with 𝑐> 0 and 𝛼∈(0, 1], trying to get the highest 𝛼– that is trying to optimize the behavior of 𝜉close to zero. This will lead to somewhat tight bounds only in the regime where E𝐿(𝜃) is small, a regime which might not be reached without an indecent number of samples. We illustrate the regime where constants matter more than exponents on Figure 3.2.

In practice, it would be more useful to take into consideration the number of samples ﬁrst, before looking for a function 𝜉that veriﬁes Eℓ(𝜃) ≤𝜉(E𝐿(𝜃)) for any 𝜃, and minimizes max 𝜉([𝑎, 𝑏]) for [𝑎, 𝑏] the range of value that we expect the surrogate risk to take given our ﬁxed number of samples.

<!-- page: 37 -->

# Chapter 4. Partially Supervised Learning

Many data scientists spend more time scrapping, annotating and cleaning data than ﬁne-tuning models. This motivates the following question: can we derive a more generic framework than the one of supervised learning in order to learn from cluttered data? In this thesis, this question is approached through the lens of weakly supervised learning, assuming that the bottleneck of data collection lies in data annotation. This chapter summarizes our main contributions to weakly supervised learning. It is based on our published work Cabannes et al. (2020b, 2021b,a), which is reproduced in part III.

## 4.1 Navigating frameworks of weakly supervised learning

In this section, we give a brief introduction to weakly supervised learning.

Weakly supervised learning is concerned with the setting where it is easy to get 𝑛inputs (𝑋𝑖)𝑖≤𝑛, but it is hard to get the corresponding outputs (𝑌𝑖)𝑖≤𝑛, a setting which is relevant for many applications. For example, when dealing with images, one can easily scrap zillions of images on the web, which provides many input data, but getting the corresponding outputs demands laborious annotations of data. The situation is similar when it comes to medical applications, such as understanding drug interactions (Davis et al., 2012) or recognizing cancers with radiography. While one can access databases from hospitals to get many X-ray images, recognizing cancers on those requires the expertise of a radiologist, which is expensive to access. Indeed, annotation costs can critically add up when one plans to use powerful models that require millions of data points to be trained. As a counter example, notice that weakly supervised learning does not help when input data are features coming from heterogeneous sources leading to missing data. We shall discern three types of weak supervision, the last two being not completely disjoint.

1. Global statistics on groups of inputs. This setting consists in accessing global information on bags of samples – e.g. knowing that half of the (𝑌𝑖)𝑖∈𝐼are zeros for a given 𝐼⊂[𝑛]. Examples of global statistics supervision include multiple-instance learning (Dietterich et al., 1997) and learning from label proportion (Quadrianto et al., 2009). We refer to those articles for motivations, descriptions and applications of those two problems.

2. Weak classiﬁers. A second approach consists in assuming the access to many weak classiﬁers 𝜑𝑗: X →Y for 𝑗∈[𝑝] that weakly correlate with 𝑓∗. Those classiﬁers might model labelers from a crowdsourcing platform, experts or noisy measurements. More generally, they might be provided by side information, coming from distant supervision (Mintz et al., 2009; Craven and Kumlien, 1999) or transferred from algorithms that have been designed for a related task (Pan and Yang, 2010). Recently, Ratner et al. (2020) have implemented a software interface based on this approach.

3. Incomplete annotation. Finally, weak supervision might be understood as the access to partial knowledge on what 𝑌𝑖is for each 𝑖∈[𝑛]. In some instances, partial observation on 𝑌𝑖can be cast as a set of potential labels 𝑆𝑖⊂Y that are compatible with this partial observation, which is the setting of partial supervision (Cour et al., 2011). Partial supervision is a generalization of semi-supervised learning, which has

35

<!-- page: 38 -->

been the classical approach to overcome the bottleneck of data annotation (Chapelle et al., 2006) and consists in learning from a set of labeled data, 𝑆𝑖= {𝑌𝑖} for 𝑖∈𝐿⊂[𝑛], and of unlabeled data, 𝑆𝑖= Y for 𝑖∈[𝑛] \ 𝐿.

Beyond those three settings, limitations that motivate weakly supervised learning might be tackled by leveraging human knowledge under the form of priors (Mann and McCallum, 2010) or of function architectures (reviving old approaches of artiﬁcial intelligence such as Muggleton and de Raedt, 1994).

## 4.2 The importance to create consensus

In this section, we review our ﬁrst approach to the problem of learning from partial supervision. We ﬁrst formalize this setting before introducing a variational objective to minimize and providing guarantee regarding this approach.

### 4.2.1 Partial supervision setting

In this thesis, hence in the following, we focus on partial supervision, which is also known as superset learning. In other terms, we assume the access to weak supervision for each label 𝑦under the form of a set 𝑠⊂Y that contains the true labels 𝑦∈𝑠. To formalize this problem, we introduce the set S ⊂2Y of closed subsets of Y and the distribution 𝜏∈ΔX×S generating samples (𝑋𝑖, 𝑆𝑖)𝑖≤𝑛∼𝜏⊗𝑛. The goal is still to minimize the risk

$$
R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] , (4.1)
$$

(4.1)

for a known loss function ℓ: Y × Y →R and a distribution on I/O pairs 𝜌∈ΔX×Y. In contrast with supervised learning, 𝜌will never be accessed, nor any samples (𝑋𝑖,𝑌𝑖) ∼𝜌.

In order to motivate our theoretical setting, we now discuss simple instances of partial supervision.

Example 5 (Classiﬁcation with attributes). Suppose that you want to learn ﬁne-grained classes on images, e.g. to precisely distinguish “caracals” and “domestic cats”, as well as “hedgehog mushrooms” and “shiitakes”. It will probably be hard for commoners hired on crowdsourcing platforms to label images with precise classes. Yet, this commoner might easily label attributes, such as “tufted ears” characterizing “caracals” among “felines”, or “spines rather gills underside of the cap” and “tan irregular cap” characterizing “hedgehogs” among “mushrooms”. Those partial labels can easily be cast as sets of labels: “feline” would be {“lion”, “panther”, . . . } and “tufted ears” be {“great horned owl”, “Araucana chicken”, . . . }. The key idea here is that it is much cheaper to get a set of many partial labels that is informative enough to learn 𝑓∗ than a set of few complete labels enabling the same learning.

Example 6 (Ranking with partial ordering). Consider a ranking problem where, given a user characterized by some features 𝑥, the goal is to learn their preference over 𝑚ﬂowers, deﬁning the output 𝑦∈S𝑚as an ordering of 𝑚elements. Once again, getting the full 𝑦is a laborious task, as one might have a hard time to rank all 𝑚ﬂowers. In contrast, one might easily provide partial ordering information, such as “I prefer roses to lilies”, or “tulips are my favorite”, which can be cast as the set of total orderings that verify those partial orderings.

Example 7 (Regression with censored data). For many regression problems, it is not possible to get exact labels but only possible to access bins or censored labels [𝑎, 𝑏] ∋𝑦. This could be due to the use of a measuring scale, or, if retaking example 3, due to some uncertainty regarding a price at which a house has been sold.

### 4.2.2 Solution deﬁnition through the inﬁmum loss

Currently, the problem (ℓ, 𝜏) is ill-deﬁned since we cannot deﬁne clearly the goal (4.1) from those two objects only – ℓbeing a loss function on pairs of outputs and 𝜏a distribution on (𝑋, 𝑆). One way to redeﬁne a solution in this context is to keep the precedent variational point of view and deﬁne a loss 𝐿: Y × 2Y →R that given a prediction 𝑧∈Y and an observation 𝑆⊂Y, provides a compatibility or performance score. Hence the new objective

$$
R𝑆( 𝑓) = E(𝑋,𝑆)∼𝜏[𝐿( 𝑓(𝑋), 𝑆)] .
$$

Yet, how to derive the loss 𝐿(𝑧, 𝑆) for 𝑧∈Y and 𝑆⊂Y when the original task was speciﬁed by the loss ℓ(𝑧, 𝑦) with 𝑦∈𝑆? Arguably there are three possibilities.

<!-- page: 39 -->

$$
𝑦𝑖 1 𝑦𝑎 2 𝑦𝑖
2
𝑦𝑎 𝑧𝑎𝑧𝑖
1
𝑦𝑎 1 𝑦𝑎
2 𝑧𝑎 𝑧𝑖
$$

[FIGURE: Figure 4.1]

Figure 4.1: Two diﬀerent ﬁgures of partial supervision in Y = R2 without input (or X being a singleton). The loss is given by the mean square error, i.e. the usual Euclidean geometry. On both ﬁgures, we represent Y with two sets, 𝑆1 in light gray and 𝑆2 in gray, and the estimates 𝑧= arg min𝑧∈Y {𝐿(𝑧, 𝑆1) + 𝐿(𝑧, 𝑆2)} provided by the inﬁmum loss (𝑧𝑖) and the average loss (𝑧𝑎). The point 𝑦𝑎 1 represents the disambiguation of 𝑆1 by the average loss. On the left ﬁgure, although 𝑆1 intersects 𝑆2, only the inﬁmum loss veriﬁes 𝑧𝑖∈𝑆1 ∩𝑆2.

1. Bounding the original excess risk from above with the supremum loss 𝐿(𝑧, 𝑆) = sup𝑦∈𝑆ℓ(𝑧, 𝑦). Suprema have been used in statistics for robustness purposes (Wald, 1945). The idea here is that if we prevent ourselves against the worst possible candidates (in terms of error given a prediction 𝑧), we will prevent ourselves against whatever is the ground truth label in 𝑆. Yet, as we will discuss later, this approach is too conservative in our setting. 2. Matching a bit of all the elements in the set 𝑆with the average loss 𝐿(𝑧, 𝑆) = 1 |𝑆| Í

𝑦∈𝑆ℓ(𝑧, 𝑆). This loss has the beneﬁt of being agnostic on what should be the true 𝑦∈𝑆regardless of what the prediction 𝑧is. Under symmetry assumptions of the original loss, for example when ℓis the 0-1 loss in classiﬁcation, averaging candidates is a reasonable solution. When the loss is not symmetric, it can insidiously bias the solution as we describe on Figure 7.1. In many cases, it is possible to correct for this asymmetry, which techniques implicitly implied by Proposition 59 and illustrated with the ﬁlling with zero techniques in section 8.5.4. 3. Making sure that the prediction 𝑧matches at least one element with the inﬁmum loss 𝐿(𝑧, 𝑆) = inf𝑦∈𝑆ℓ(𝑧, 𝑆). When ℓis seen as a distance, 𝐿is its natural extension to sets. Hüllermeier (2014) has referred to it as the optimistic loss, since given a prediction 𝑧, it somehow disambiguates 𝑦∈𝑆by considering the best label in order to minimize ℓ(𝑧, 𝑦) under the constraints 𝑦∈𝑆. Let us take a step back and recall the commoner providing the set “feline” that is 𝑆1 = {“cat”, “lion”, . . . } and the set “tufted ears”, that is 𝑆2 = {“owl”, “Araucana chicken”, . . .}, when annotating the picture of a “caracal”. Naturally, we would like to output a prediction 𝑧∈𝑆1 ∩𝑆2 = {“caracal”} of a feline with tufted ears. In other terms, we want to create consensus between observations, which is what the inﬁmum loss provides. The supremum loss is outcast from the good solutions, since it might disambiguate 𝑦1 ∈𝑆1 as “leopard” and 𝑦2 ∈𝑆2 as “owl”, as well as the average loss as we illustrated on Figure 4.1.

### 4.2.3 Theoretical guarantees

With the inﬁmum loss, we switch to the original supervised learning problem (4.1) to the new problem deﬁned through the risk

$$
R𝑆( 𝑓) = E(𝑋,𝑆)∼𝜏 inf 𝑦∈𝑆ℓ( 𝑓(𝑋), 𝑦) . (4.2)
$$

(4.2)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

How are those two problems related? In particular, we would like to make sure that solving the partially supervised problem does help to tackle the fully supervised one. Following the formalism of the previous chapter, we can try to derive a calibration inequality that relates the excess of the original risk (4.1) to the excess of the “surrogate” risk (4.2). To derive such a generic inequality, we need strong assumptions, which are usually given by ensuring non-ambiguity of the partial supervision (Deﬁnition 34), that is for each 𝑥, the sets in the support of the conditional distribution (𝑆| 𝑋= 𝑥) intersect into a singleton {𝑦𝑥} = { 𝑓∗(𝑥)}. Such an inequality was ﬁrst provided by Cour et al. (2011) in the case of classiﬁcation with the 0-1 loss, and is generalized to generic problems by Proposition 37. This technique allows us to derive rates on a structured prediction algorithm learning from partially supervised data in Theorem 14. In practice, given samples (𝑋𝑖, 𝑆𝑖), the practitioner can use their favorite algorithm to translate this population principle into an empirical objective to be optimized in order to get an estimate 𝑓𝑛of the risk minimizer.

<!-- page: 40 -->

Remark 4 (A false case against partial supervision). Partially supervised learning and the inﬁmum loss are often criticized because of the strength of the non-ambiguity assumption. This should rather be seen as a limitation of theoretical analysis, rather than a limitation of the framework. Actually, a more careful analysis based on the idea provided in the previous chapter shows that the non-ambiguity assumption is akin to the Massart noise condition, and can be used to derive much faster rates without modifying algorithms as shown by Theorem 15. This suggests that there are many interesting behaviors to characterize beyond the non-ambiguity assumption.

## 4.3 Label disambiguation to complete supervision

In this section, we characterize the solution provided by the inﬁmum loss as a disambiguation strategy, that consists in retrieving full supervision ﬁrst, before learning from it. This leads to a diﬀerent perspective in terms of learning and practical implementations.

### 4.3.1 Expected testing distribution

Let us roll back a little and think back on which solution to look for when in presence of partial supervision. The ultimate goal is to ﬁnd a mapping that minimizes the generalization error on the testing distribution 𝜌∈ΔX×Y. Yet which distribution 𝜌should we expect given the loss ℓand the distribution 𝜏∈ΔX×2Y? The only clearly deﬁned constraints is that the distribution should be compatible with the weak information we have seen on the data. The notion of compatibility can be formalized through the following deﬁnition, which we introduced in Cabannes et al. (2020b).

Deﬁnition 5 (Compatibility). Two distributions 𝜌∈ΔX×Y and 𝜏∈ΔX×S are said to be compatible if there exists an underlying distribution of probability 𝜋∈ΔX×Y×S such that 𝜌and 𝜏are the respective marginals of 𝜋according to X × Y and X × S and such that for any (𝑥, 𝑦, 𝑠) ∈supp 𝜋, we have 𝑦∈𝑠. This compatibility property will be denoted by 𝜌⊢𝜏.

To discriminate the expected 𝜌among all the distributions compatible with 𝜏, we need a principle. It is natural to look for a distribution that satisﬁes some properties. As mentioned in the last section, we would like to go for a distribution that is “consensual”, i.e. we would like to reduce the noise of the conditional (𝑌| 𝑋). In other terms, we would like those conditional distributions to be as deterministic as possible. As a consequence, we deﬁne the expected testing distribution as

$$
\underset{𝜌⊢𝜏}{\arg\min}\, E(𝜌),
$$

for E : ΔX×Y →R a measure of determinism. A well-known measure of determinism is the entropy E(𝜌) := E[−log(𝜌(𝑋,𝑌))]. This measure is independent of the loss ℓ, which might be a desirable property if one would like to reuse the same supervised distribution for diﬀerent tasks linked with diﬀerent losses. Yet, when there is a structure on Y such that its explicit dimension is much bigger than the intrinsic dimension of this space seen through the loss ℓ, the entropy will scale with the explicit dimension. For example, in ranking problems where the goal is to output an ordering over 𝑚items, which is similar to a permutation in S𝑚, the output space is of cardinality 𝑚!, while the intrinsic dimension is 𝑚. For those problems, it is wise to incorporate the loss in the objective, in particular, we suggest the following loss-based variance E(𝜌) := inf 𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)]. Once the distribution 𝜌is recovered, a function 𝑓can be learned in a supervised learning fashion

$$
𝑓∗∈arg min
$$

E(𝑋,𝑌)∼𝜌★[ℓ( 𝑓(𝑋),𝑌)], with 𝜌★= arg min

$$
inf 𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)]. (4.3)
𝑓:X→Y 𝜌⊢𝜏
$$

(4.3)

Remarkably, this second solution to the partially supervised learning problem is exactly the same as the one provided by the inﬁmum loss. This is based on the fact that, under really mild deﬁnition assumptions

$$
inf 𝜌⊢𝜏 inf 𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)] = inf 𝑓:X→Y inf 𝜌⊢𝜏E𝜌[ℓ( 𝑓(𝑋),𝑌)] = inf 𝑓:X→Y E𝜏[inf 𝑦∈𝑆ℓ( 𝑓(𝑋), 𝑦)].
$$

A nice property of this new characterization of the solution 𝑓∗is that it goes beyond the partial labeling problem. As a matter of fact, (4.3) can be applied more generally to any weakly supervised learning paradigm where the weak information acquired on the problem can be translated into hard constraints, e.g. in the case of label proportion.

<!-- page: 41 -->

### 4.3.2 Optimization issues

Before going any further, let us point out that any objective E(𝜌) that is minimized for deterministic distributions is intrinsically not-convex. Consider the case where there is no input space (or X is a singleton), Y is discrete, and E is a function taking as argument elements of the simplex ΔY and outputting a real-valued score. If E is minimized for deterministic distributions, it is minimized on extremities of the simplex. In other terms, E should really be thought of as a concave function, making its minimization a non-convex optimization problem. We picture level lines of such an objective on Figure 8.4.

Regarding the constraints, it should be noted that {𝜌∈ΔX×Y | 𝜌⊢𝜏} is a convex set. So we are trying to minimize a concave function over a convex set. In Cabannes et al. (2021b), we suggested two diﬀerent heuristics to approach this minimization procedure. The ﬁrst one consists in starting with a good “center point” and ﬁnding an extremity of the deﬁnition domain after gradient descent. Our notion of center takes into account the loss to avoid insidious bias (similarly to what we discussed the average loss). The second one is based on the Diﬀrac algorithm (Bach and Harchaoui, 2007), and consists in convexifying the objective by adding a quadratic term that is constant on extremities, perform gradient descent, and get a solution that is a convex combination of extreme points. We refer to sections 8.5 and 8.B for further discussions on those techniques.

### 4.3.3 Empirical objective

Given data (𝑋𝑖, 𝑆𝑖)𝑖≤𝑛∼𝜏⊗𝑛, how to translate the disambiguation principle (4.3) into an empirical objective allowing to disambiguate the sets (𝑆𝑖)𝑖≤𝑛into labels ( ˆ𝑌𝑖)𝑖≤𝑛? To answer this question, we need to translate an objective on distribution into an objective on samples. The usual translation of risk minimization into empirical risk minimization can be thought as the approximation 𝜌≈ˆ𝜌= 1 Í

𝑖≤𝑛𝛿𝑋𝑖⊗𝛿𝑌𝑖plus some constraints 𝑓∈F on the functions that we minimize. As such, we could go for

$$
(𝑦𝑖∈𝑆𝑖)𝑖≤𝑛inf min 𝑓∈F \sum_{𝑛 𝑖=1} ℓ( 𝑓(𝑋𝑖), 𝑦𝑖). 𝑛
$$

This will be really hard to solve in practice. The solution we suggested is based on kernel mean embedding (Muandet et al., 2017), which is a natural way to understand the surrogate approach of Ciliberto et al. (2016). It consists in incorporating directly the hypothesis on the solution of the problem in the estimated distribution with ˆ𝜌≈1 Í

𝑖,𝑗≤𝑛𝛿𝑋𝑖⊗𝛼𝑗(𝑋𝑖)𝛿𝑌𝑗, where 𝛼: X →R𝑛is a weighting scheme that states how to diﬀuse information (𝑌𝑖)𝑖≤𝑛seen at (𝑋𝑖)𝑖≤𝑛to any point 𝑥∈X. In particular, those weights might be used to estimate the conditional distribution (𝑌|𝑋= 𝑥) as Í

$$
𝑛
$$

𝑗≤𝑛𝛼𝑗(𝑥)𝛿𝑌𝑗. This leads to the following empirical objective

$$
𝑛 ∑︁
( ˆ𝑦𝑖)𝑖≤𝑛∈arg min inf (𝑧𝑖∈Y)𝑖≤𝑛 𝛼𝑖(𝑋𝑗)ℓ(𝑧𝑖, 𝑦𝑗), (4.4)
(𝑦𝑖∈𝑆𝑖)𝑖≤𝑛 𝑖,𝑗=1
$$

(4.4)

In the case of kernel ridge regression, those weights are given by 𝛼(𝑥) = (𝐾+ 𝜆𝑛)−1𝐾𝑥with the notations of section 2.4.2. But they could also be given by similarity metrics, or derived with more advanced unsupervised techniques such as the one we present in Cabannes et al. (2021a) as we detail in section 9.A.

### 4.3.4 Theoretical guarantees

The convergence of an estimate 𝑓𝑛learned on the dataset (𝑋𝑖, ˆ𝑦𝑖)𝑖with ( ˆ𝑦𝑖)𝑖≤𝑛recovered through (4.4) cannot easily be performed with the tools presented so far. Indeed, it is hard to understand how the diﬀerent disambiguation (𝑦𝑖∈𝑆𝑖) interacts when studying (4.4). This relates to the non-concavity of this objective: a small change in the optimal (𝑧𝑖)𝑖≤𝑛can lead to completely diﬀerent optimal (𝑦𝑖)𝑖≤𝑛. While there are probably good tools to think in terms of distribution and derive a consistent empirical estimate of (4.3), in Cabannes et al. (2021b), we used the fact that usual learnability assumptions for the partial labeling problem are actually quite strong, which allows us to prove impressively fast rates.

To derive consistency of algorithm learning with partially supervised data, it is classical to assume non- ambiguity of the distribution (𝑆| 𝑋= 𝑥) as well as some regularity of the function X →ΔY; 𝑥→(𝑌| 𝑋= 𝑥). Those assumptions actually imply that the data are clustered by groups where labels are all equal. When this class separation hypothesis holds true, one can leverage this structure by considering a weighting scheme

<!-- page: 42 -->

based on nearest neighbors. As we discussed in more details in section 8.4, this endows the estimate 𝑓𝑛with exponential convergence rates, meaning that the risk R( 𝑓𝑛) converges toward the minimum risk exponentially fast as the number of samples 𝑛goes to inﬁnity. This is the statement of Theorem 15.

### 4.3.5 Can collaborative ﬁltering help us to deal with weak supervision?

There is a natural link between completion of weak information and the collaborative ﬁltering problem described in section 2.3.3. To make this link we will need to introduce more concepts.

Assume that the loss ℓ: Y →Y →R can be written as ℓ(𝑧, 𝑦) = −⟨𝜓(𝑧), 𝜑(𝑦)⟩with 𝜓, 𝜑: Y →H two embeddings into a Hilbert space H, encoding the structure of the loss. For example, the Kendall loss in ranking corresponds to the correlation measure 𝜑= −𝜓= (1𝜎(𝑖)>𝜎( 𝑗))𝑖,𝑗≤𝑚for 𝜎∈Y = S𝑚a permutation. We refer to Nowak-Vila et al. (2019) for more examples. Assume also that the weak supervision correspond to observing 𝐴𝑖𝜑(𝑌𝑖) instead of 𝜑(𝑌𝑖) for a known masking operator 𝐴𝑖: H →H. For example, observing a partial ordering that 𝜎should verify is equivalent to observing some coordinates of the vector 𝜑(𝜎). The disambiguation problem can be reduced to the matrix completion problem of retrieving (𝜑(𝑦𝑖))𝑖≤𝑛from the observations (𝐴𝑖𝜑(𝑌𝑖))𝑖≤𝑛. Our algorithm suggests solving the minimization problem

$$
⊤
2
©­ « | | 𝜓(𝑧1) · · · 𝜓(𝑧𝑛) | | ª® ¬ ©­ « 𝛼𝑖(𝑋𝑗) ª® ¬ ©­ « | | 𝜑(𝑦1) · · · 𝜑(𝑦𝑛) | | ª® ¬
minimize
𝐹 subject to 𝐴𝑖𝜑(𝑦𝑖) = 𝐴𝑖𝜑(𝑌𝑖).
$$

In the case where 𝜓= −𝜑and there is no context variables, hence 𝛼𝑖(𝑋𝑗) = 1, the slightly diﬀerent measure of determinism exposed in section 8.B leads to the problem

$$
\frac{minimize}{subject to} Í𝑛 2 − 𝑖=1 𝜑(𝑦𝑖) 𝐴𝑖𝜑(𝑦𝑖) = 𝐴𝑖𝜑(𝑌𝑖).
$$

For correlation losses, it is usual for ∥𝜑(·)∥to be constant, so to minimize the last objective, one should try to align all 𝜑(𝑦𝑖) in one direction. This diﬀers from the collaborative ﬁltering solution which completes the (𝜑(𝑦𝑖)) by minimizing the cardinality of the set {𝜑(𝑦𝑖) | 𝑖∈[𝑁]}. Formally, collaborative aims at solving the following problem

$$
\frac{minimize}{subject to} | rank ©­ 𝜑(𝑦1) · · · « | 𝐴𝑖𝜑(𝑦𝑖) = 𝐴𝑖𝜑(𝑌𝑖), | 𝜑(𝑦𝑛) | \frac{ª®}{¬}
$$

which is practically implemented with the nuclear norm instead of the rank. In essence, the inﬁmum loss builds an understanding of (𝑌| 𝑋) by collapsing all observations onto a single vector in 𝜑(ΔY), while collaborative ﬁltering builds such an understanding by minimizing the number of vectors in 𝜑(Y) to complete observations without discrepancy. Bining observations into several groups makes sense when context variables do not allow for inputs to characterize outputs univocally.

Further investigations of the link between our work and collaborative ﬁltering is a research direction that we left open. We conjecture that this link might prove useful to incorporate context variables into collaborative ﬁltering techniques.

## 4.4 Leveraging input structure

In this section, we discuss unsupervised learning techniques that could be incorporated in the frameworks described previously in order to leverage unlabeled input data.

### 4.4.1 The case of semi-supervised learning

The inﬁmum loss and the disambiguation framework described previously are based on a pointwise principle that discriminates a distribution (𝑌| 𝑋) from a weakly supervised distribution (𝑆| 𝑋). Such a principle fails to provide any guideline for semi-supervised learning, which is a speciﬁc instance of partial supervision where 𝑆is either a singleton or the full set Y. In particular for unsupervised parts of the input space, which

<!-- page: 43 -->

correspond to points in the support of (𝑋| 𝑆= Y) that do not belong to the support of (𝑋| |𝑆| = 1), this principle does not provide any information on what 𝑓∗(𝑥) should be.

Eventually, the solution on those points could be inferred from the solution on the other points by looking for the simplest function completion with respect to some criterion quantifying how “simple” a function is. For regression problems, if one searches to minimize the empirical risk in a Banach space of function, the norm of this Banach space provides a simple criterion for “simplicity”. More generally, in metric space of function, this norm can be replaced more generally as the distance between a neutral function (e.g. the null function in a vector space) and the function itself.

### 4.4.2 Laplacian regularization

The classical approach to solve semi-supervised learning regression problem is to choose the criterion of “simplicity” as the Dirichlet energy 𝑓→E𝜌X [∥∇𝑓(𝑋)∥2]. This regularization is similar to the square norm of the Hilbert space of functions 𝑊1,2(𝜌X ), which is the weighted Sobolev space of functions with weak derivative endowed with the probability measure 𝜌X . Considering a square of the norm rather than the norm itself is classical in machine learning, making analysis as well as computations easier. Measuring regularity through the probability measure 𝜌X rather than the Lebesgue measure is crucial in order to leverage the unsupervised data.

This regularization has been introduced in the seminal paper of Zhu et al. (2003) which estimates the Dirichlet energy through ﬁnite diﬀerence methods akin to the Nadayara-Watson estimator. This regularization formalized many intuitions. For regression problems, it is natural to assume that the target function does not vary too much on densely populated input regions, or said otherwise, that its variations concentrate on regions without too much data. For classiﬁcation problems, this echoes the low-density separation hypothesis, assuming that decision frontiers, that is frontier between classes in the input space, lies on sparsely populated regions. In Cabannes et al. (2021a), we proposed a “kernelized” version of this estimation in order to bypass the curse of dimensionality under regularity assumptions, together with some clever low-rank factorization in order to reduce computation time to a decent amount. It should be noted that Laplacian regularization has also a natural interpretation in terms of diﬀusion, which is captured by the Langevin dynamic, and explains the wording “label propagation” found in semi-supervised literature.

### 4.4.3 Complete framework

With Laplacian regularization, one can deepen the lex parsimoniae of the precedent sections when this rule does not discriminate a unique distribution by looking for the distribution that will minimize the Dirichlet energy of its (or a continuous surrogate) risk minimizer. In particular, this approach is interesting as it could remove the usual non-ambiguity assumption usually made to deﬁne and study solutions of the partial supervision problems (Cour et al., 2011; Luo and Orabona, 2010; Liu and Dietterich, 2014; Cabannes et al., 2020b, 2021b). Yet, removing such an assumption will come at the price of adding assumptions on the surrogate problem we are solving that might be harder to verify in practice.

Finally, it should be noted that Laplacian regularization can be introduced as soon as during the preprocessing/feature engineering part of a practical machine learning pipeline. In particular, it provides principled guidelines to retrieve and parametrize a small manifold on which the input data might lie, and might prove itself useful to strengthen self-supervision techniques. At this point, it is less a theory than experiments that could conﬁrm those intuitions.

## 4.5 Active labeling

Weakly supervised learning is concerned with retrieving a target function under weak observations. It is often motivated by the bottleneck of annotating data. Yet it fails to answer the most simple question practitioners might ask themselves: how to collect the most discriminative dataset to learn this function under some cost constraints. Hence, the last part of this thesis is devoted to the “active” collection of weak supervision. Active refers to the fact that we will iteratively and adaptively search for annotations, in contrast with passive settings in which annotations are given once and for all by an exterior mechanism.

The cost of dataset annotation depends on diﬀerent task speciﬁcations. Hence, a model of annotation cost can only describe a limited number of situations. As well as we split our understanding of weakly

<!-- page: 44 -->

supervised learning in three parts (group statistics, weak classiﬁers, and labels corruption), we could split dataset annotation with the same three categories. In practice, it is frequent to annotate dataset by grouping input data according to a classiﬁer output before identifying the most present class in each group and ﬁltering mistakes, which allows annotating large chunks of data at once. In a similar fashion, ImageNet was collected by searching for diﬀerent categories on image search engines, before spotting outliers in a batch of images resulting from a single query (Deng et al., 2009).

The ﬁnal part of this thesis touches upon the active variant of partially supervised learning (Cabannes et al., 2022). In particular, we assume that given data (𝑋𝑖)𝑖≤𝑛, one can query any information of the type 1𝑌𝑖𝑡∈𝑆𝑡for 𝑖𝑡∈[𝑛] an index to choose and 𝑆𝑡∈S ⊂2Y a set to choose among certain subsets of labels. We refer the reader to Part IV for additional considerations on the matter.

<!-- page: 45 -->

# Part II. Considerations on Learning Theory

43

<!-- page: 46 -->

<!-- page: 47 -->

# Chapter 5. Fast Rates for Structured Prediction

The following is a reproduction of Cabannes et al. (2021c).

Discrete supervised learning problems such as classiﬁcation are often tackled by introducing a continuous surrogate problem akin to regression. Bounding the original error, between estimate and solution, by the surrogate error endows discrete problems with convergence rates already shown for continuous instances. Yet, current approaches do not leverage the fact that discrete problems are essentially predicting a discrete output when continuous problems are predicting a continuous value. In this paper, we tackle this issue for general structured prediction problems, opening the way to “superfast” rates, that is, convergence rates for the excess risk faster than 𝑛−1, where 𝑛is the number of observations, with even exponential rates with the strongest assumptions. We ﬁrst illustrate it for predictors based on nearest neighbors, generalizing rates known for binary classiﬁcation to any discrete problem within the framework of structured prediction. We then consider kernel ridge regression where we improve known rates in 𝑛−1/4 to arbitrarily fast rates, depending on a parameter characterizing the hardness of the problem, thus allowing, under smoothness assumptions, to bypass the curse of dimensionality.

## 5.1 Introduction

Machine learning is raising high hopes to tackle a wide variety of prediction problems, such as language translation, fraud detection, traﬃc routing, speech recognition, self-driving cars, DNA-binding proteins, etc. Its framework is appreciated as it removes humans from the burden to come up with a set of precise rules to accomplish a complex task, such as recognizing a cat on an array of pixels. Yet, it comes at a price, which is of forgetting about algorithm correctness, meaning that machine learning algorithms can make mistakes, i.e., wrong predictions, which can have dramatic implications, e.g., in medical applications. This motivates work on generalization error bounds, quantifying how often one should expect errors.

Many of the problems discussed above are of discrete nature, in the sense that the number of potential outputs is ﬁnite, or inﬁnite countable. To learn such problems, a classical technique consists in deﬁning a continuous surrogate problem, which is easier to solve, and such that:

(1) an algorithm on the surrogate problem translates into an algorithm on the original problem; (2) errors on the original problem are bounded by errors on the surrogate problem. The ﬁrst point refers to the concept of plug-in algorithms, while the second point to the notion of calibration inequalities. For example, binary classiﬁcation can be approached through regression by estimating the conditional expectation of the output 𝑌given an input 𝑋(Bartlett et al., 2006).

On the one hand, continuous surrogates for discrete problems are interesting, as they beneﬁt from functional analysis knowledge, when discrete problems are more combinatorial in nature. On the other hand, continuous surrogates can be deceptive, as they are asking to solve for more than needed. Considering the example of binary classiﬁcation, where 𝑌∈{−1, 1}, one only has to predict the sign of the conditional expectation, rather than its precise value. Interestingly, without modifying the continuous surrogate approach, this last remark can be leveraged in order to tighten generalization bounds derived through calibration inequalities (Audibert and Tsybakov, 2007). In this work, we extend those considerations, known in binary classiﬁcation (e.g., Koltchinskii and Beznosova, 2005; Chaudhuri and Dasgupta, 2014), to generic discrete supervised learning problems, and show how it can be applied to the kernel ridge regression algorithm introduced by Ciliberto et al. (2016).

45

<!-- page: 48 -->

### 5.1.1 Contributions

Our contributions are organized in the following order.

• In Section 5.2, we consider the general structured prediction from Ciliberto et al. (2020) based on Lipschitz-continuous losses and derive reﬁned calibration inequalities to leverage the fact that learning a mapping into a discrete output space is easier than learning a mapping into a continuous space. • In Section 5.3, we show how to exploit exponential concentration inequalities to turn them into fast rates under a condition generalizing the Tsybakov margin condition. • In Section 5.4, we apply Section 5.3 to local averaging methods with the particular example of nearest neighbors. This leads to extending the rates known for regression and classiﬁcation to a wide variety of structured prediction problems, with rates that match minimax rates known in binary classiﬁcation. • In Section 5.5, we show how Section 5.3 can be applied to kernel ridge regression. This allows us to improve rates known in 𝑛−1/4 to arbitrarily fast rates depending on the hardness of the associated discrete problem.

### 5.1.2 Related work

Surrogate framework. The surrogate problem we will consider to tackle structured prediction ﬁnds its roots in the approximate Bayes rule proposed by Stone (1977), analyzed through the prism of mean estimation as suggested by Friedman (1994) for classiﬁcation, and analyzed by Ciliberto et al. (2020) in the wide context of structured prediction. In particular, we will specify results on two classes of surrogate estimators: local averaging methods, or kernel ridge regression.

Local averaging methods. Neighborhood methods were ﬁrst studied by Fix and Hodges (1951) for statistical testing through density estimation. Similarly, Parzen–Rosenblatt window methods (Parzen, 1962; Rosenblatt, 1956) were developed. Those methods were cast in the context of regression as nearest neighbors (Cover and Hart, 1967) and Nadayara-Watson estimators (Watson, 1962; Nadaraya, 1964). Stone (1977) was the ﬁrst to derive consistency results for a large class of localized methods, among which are nearest neighbors and some window estimators (Spiegelman and Sacks, 1980; Devroye and Wagner, 1980). Rates were then derived, with minimax optimality (Stone, 1980; Yang, 1999). Several reviews can be found in the literature, such as Györﬁet al. (2002); Tsybakov (2009); Biau and Devroye (2015); Chen and Shah (2018).

Reproducing kernel ridge regression. The theory of real-valued reproducing kernel Hilbert spaces was formalized by Aronszajn (1950), before ﬁnding applications in machine learning (e.g., Scholkopf and Smola, 2001). Minimax rates for kernel ridge regression were achieved by casting the empirical solution estimate as a result of integral operator approximation (Smale and Zhou, 2007; Caponnetto and De Vito, 2006), allowing to control convergence through concentration inequalities in Hilbert spaces (Yurinskii, 1970; Pinelis and Sakhanenko, 1986) and on self-adjoint operator on Hilbert spaces (Minsker, 2017). First derived in 𝐿2-norm, rates were cast in 𝐿∞-norm through interpolation inequalities (e.g., Fischer and Steinwart, 2020; Lin et al., 2020).

Tsybakov margin condition. Learning a mapping into a discrete output space is indeed easier than learning a continuous mapping, as, for binary classiﬁcation for example, one typically only has to predict the sign of E[𝑌|𝑋] rather than its precise value. As such, calibration inequalities that relate the error on a discrete structured prediction problem to an error on a smooth surrogate problem are often suboptimal. This phenomenon was exploited for density discrimination, a problem consisting of testing if samples were drawn from one or the other of two potential distributions, by Mammen and Tsybakov (1999), and for binary classiﬁcation by Audibert and Tsybakov (2007). Those works introduce a parameter 𝛼∈[0, ∞) characterizing the hardness of the discrete problem, and leverage concentration inequalities to accelerate rates known for regression by a power 𝛼+ 1 (Audibert and Tsybakov, 2007), while rates plugged-in directly through calibration inequalities only present an acceleration by a power 2(𝛼+ 1)/(𝛼+ 2) (see, e.g. Boucheron et al., 2005; Bartlett et al., 2006; Bartlett and Mendelson, 2006; van Erven et al., 2015; Nowak-Vila et al., 2019).

<!-- page: 49 -->

## 5.2 Structured prediction with surrogate control

In this section, we introduce the classical supervised learning problem, and a surrogate problem that consists of conditional mean estimation. We recall a calibration inequality relating the original problem to the surrogate one. We mention how empirical estimations of the conditional means usually deviate from the real means following a sub-exponential tail bound, similarly to bounds obtained through Bernstein inequality. We end this section by providing reﬁned surrogate control, that is the key toward “superfast” rates, that is, rates faster than 1/𝑛.

### 5.2.1 Surrogate mean estimation

Consider a classic supervised learning problem, where given an input space X, an observation space Y, a prediction space Z, a joint distribution 𝜌∈ΔX×Y and a loss function ℓ: Z × Y →R+, one would like to retrieve 𝑓∗: X →Z minimizing the risk R.

$$
𝑓∗∈arg min R( 𝑓) with R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] .
𝑓:X→Z
$$

In practice, X, Y, Z and ℓare givens of the problem, while 𝜌is unknown, yet partially observed thanks to a dataset D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼𝜌⊗𝑛, with data (𝑋𝑖,𝑌𝑖) sampled independently from 𝜌. Note that in fully supervised learning, the observation space is the same as the prediction space Y = Z, yet we distinguish the two for our results to stand in more generic settings, such as instances of weak supervision (Cabannes et al., 2020b). In the following, we consider Z ﬁnite. In several cases, solving the supervised learning problem can be done through solving a surrogate problem that is easier to handle. Ciliberto et al. (2016) provides a setup that reduces a wide variety of structured prediction problems (ℓ, 𝜌) to a problem of mean estimation. It works under the following assumption.

Assumption 1 (Bilinear loss decomposition). There exists a Hilbert space H and two mappings 𝜓: Z →H, 𝜑: Y →H such that

$$
ℓ(𝑧, 𝑦) = ⟨𝜓(𝑧), 𝜑(𝑦)⟩.
$$

We will also assume that 𝜓is bounded (in norm) by a constant 𝑐𝜓.

This assumption is not really restrictive (Ciliberto et al., 2020). Among others, it works for any losses on ﬁnite spaces, usually with spaces H whose dimensionality is only polylogarithmic with respect to the cardinality of Z (Nowak-Vila et al., 2019). Under Assumption 1, solving the supervised learning problem can be done through estimating the surrogate conditional mean 𝑔∗: supp 𝜌X →H, deﬁned as

$$
𝑔∗(𝑥) = E𝑌∼𝜌|𝑥[𝜑(𝑌)] , (5.1)
$$

(5.1)

where we denote 𝜌|𝑥the conditional law of (𝑌| 𝑋) under (𝑋,𝑌) ∼𝜌.

Lemma 6 (Ciliberto et al. (2016)). Given an estimate 𝑔𝑛of 𝑔∗in (5.1), consider the estimate 𝑓𝑛: X →Z of 𝑓∗, which is obtained from “decoding” 𝑔𝑛as

$$
𝑓𝑛(𝑥) = arg min ⟨𝜓(𝑧), 𝑔𝑛(𝑥)⟩. (5.2)
𝑧∈Z
$$

(5.2)

Then the excess risk is controlled through the surrogate error as

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓∥𝑔𝑛−𝑔∗∥𝐿1(X,H,𝜌) . (5.3)
$$

(5.3)

Inequalities relating the original excess risk R( 𝑓𝑛) −R( 𝑓∗) with a measure of error on a surrogate problem are called calibration inequalities. They are useful when the measure of error between 𝑔𝑛and 𝑔∗is easier to control than the one between 𝑓𝑛and 𝑓∗.

Example 8 (Binary classiﬁcation). Binary classiﬁcation corresponds to Y = Z = {−1, 1} and ℓ(𝑧, 𝑦) = 1𝑧≠𝑦 (or equivalently ℓ(𝑧, 𝑦) = 21𝑧≠𝑦−1). The classical surrogate consists of taking H = R, with 𝜑= id and 𝜓= −id. In this setting, we have 𝑔∗(𝑥) = E𝜌[𝑌|𝑋= 𝑥], and the decoding 𝑓𝑛(𝑥) := sign 𝑔𝑛(𝑥), for any 𝑔𝑛(𝑥) ∈H. In this case R( 𝑓𝑛) −R( 𝑓∗) = E𝑋

$$
1 𝑓𝑛(𝑋)≠𝑓∗(𝑋) |𝑔∗(𝑋)|
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

≤2 ∥𝑔𝑛−𝑔∗∥𝐿1 ≤2 ∥𝑔𝑛−𝑔∗∥𝐿2 . Note that in regression the excess risk reads as the square of the 𝐿2 norm, explaining a loss of a power one half in convergence rates, when going from regression to classiﬁcation (e.g. Chen and Shah, 2018).

<!-- page: 50 -->

Diﬀerences between an empirical estimate and its population version are generally handled through concentration inequalities. In this work, we will leverage concentration on ∥𝑔𝑛(𝑥) −𝑔(𝑥)∥that is uniform for 𝑥∈supp 𝜌X , motivating the introduction of Assumption 2.

Assumption 2 (Exponential concentration inequality). Suppose that for 𝑛∈N, there exists two reals 𝐿𝑛and 𝑀𝑛, such that the tails of ∥𝑔𝑛(𝑥) −𝑔(𝑥)∥can be controlled for any 𝑡> 0 as

$$
− 𝐿𝑛𝑡2
sup 𝑥∈supp 𝜌X PD𝑛(∥𝑔𝑛(𝑥) −𝑔(𝑥)∥> 𝑡) ≤exp . (5.4)
1 + 𝑀𝑛𝑡
$$

(5.4)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Note that to satisfy Assumption 2, it is suﬃcient, yet not necessary, to have a uniform control on 𝑔𝑛−𝑔∗, i.e., a control on the tail of ∥𝑔𝑛−𝑔∗∥𝐿∞, since sup𝑥P (𝐴𝑥> 𝑡) ≤P (∪𝑥{𝐴𝑥> 𝑡}) = P sup𝑥𝐴𝑥> 𝑡 , with (𝐴𝑥) a family of random variables indexed by 𝑥∈X.

Usually, in bounds like (5.4), 𝑀𝑛is a constant of the problem, while 𝐿𝑛depends on the number of samples, therefore, we would like to give rates depending on 𝐿𝑛. Typically, in Bernstein inequalities (see Theorem 9 in Appendix), 𝐿𝑛= 𝑛𝜎−2 with 𝜎2 a variance parameter and 𝑀𝑛= 𝑐𝜎−2 with 𝑐a constant of the problem that does not depend on 𝑛.

### 5.2.2 Reﬁned calibration

While it is suﬃcient to control the excess risk through an 𝐿1-norm control on 𝑔from (5.3), it is not always necessary. In other words, the calibration bound in Lemma 6 is not always tight. Indeed, we do not predict optimally, that is, { 𝑓𝑛(𝑥) ≠𝑓∗(𝑥)} only if 𝑔𝑛(𝑥) and 𝑔∗(𝑥) do not lead to the same decoding 𝑓𝑛(𝑥) and 𝑓∗(𝑥). When Z is ﬁnite, this is characterized by 𝑔𝑛(𝑥) and 𝑔∗(𝑥) not falling in the same region 𝑅𝑧of H, where

$$
𝑅𝑧= 𝜉∈H \underset{𝑧′∈Z}{\arg\min}\, ⟨𝜓(𝑧′), 𝜉⟩ .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

To ensure that 𝑔𝑛(𝑥) and 𝑔∗(𝑥) fall in the same region, one can ensure that 𝑔𝑛(𝑥) is closer to 𝑔∗(𝑥) than 𝑔∗(𝑥) is on the frontier of those regions. Those frontiers are deﬁned by points leading to at least two minimizers in (5.2):

$$
𝐹= 𝜉∈H \underset{𝑧∈Z}{\arg\min}\, ⟨𝜓(𝑧), 𝜉⟩ > 1 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The introduction of 𝐹is motivated by the following geometric results.

Lemma 7 (Reﬁned surrogate control). When Z is ﬁnite, for any 𝑥∈supp 𝜌X ,

$$
∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥< 𝑑(𝑔∗(𝑥), 𝐹) ⇒ 𝑓𝑛(𝑥) = 𝑓∗(𝑥),
$$

with 𝑑the extension of the norm distance to sets as 𝑑(𝑔∗(𝑥), 𝐹) = inf𝜉∈𝐹∥𝑔∗(𝑥) −𝜉∥. This result allows reﬁning the calibration control from Lemma 6 as

$$
1∥𝑔𝑛(𝑋)−𝑔∗(𝑋) ∥≥𝑑(𝑔∗(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥ 
R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓E𝑋 . (5.5)
$$

(5.5)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Example 9 (Binary classiﬁcation). In binary classiﬁcation (cf. Example 8), 𝐹= {0}, and, for any 𝑥∈supp 𝜌X , 𝑑(𝑔∗(𝑥), 𝐹) = |𝑔∗(𝑥)|. Lemma 7 is based on the fact that 𝑓∗(𝑥) ≠𝑓𝑛(𝑥) implies that sign 𝑔∗(𝑥) ≠sign 𝑔𝑛(𝑥) which itself implies that |𝑔∗(𝑥) −𝑔𝑛(𝑥)| = |𝑔∗(𝑥)| + |𝑔𝑛(𝑥)| ≥|𝑔∗(𝑥)|.

To leverage (5.5), we need to control 𝑑(𝑔∗(𝑥), 𝐹) below and ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥above. While upper bounds on ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥are assumed to have been derived through concentration inequalities, lower bounds on 𝑑(𝑔∗(𝑥), 𝐹) will be assumed as a given parameter of the problem, see (5.6) and (5.7).

Remark 8 (Scope of our work). While we derived the reﬁned calibration inequality (5.5) for the surrogate conditional mean 𝑔∗and the associated pointwise metric ∥·∥H, similar inequality could be obtained for other types of surrogate methods. This suggests that our work could be extended to any smooth surrogate such as the ones considered by Nowak-Vila et al. (2020), as well as Fenchel-Young losses (Blondel et al., 2020).

<!-- page: 51 -->

### 5.2.3 Geometric understanding

In this subsection, we detail how to understand geometrically Lemma 7. While the introduction of 𝜑 and 𝜓could seem arbitrary, it can be thought in a more intrinsic manner by considering the embedding 𝜑(𝑦) = 𝛿𝑦belonging to the Banach space H of signed measured, 𝑔∗(𝑥) = 𝜌|𝑥, with the bracket operator, for 𝜇∈H and 𝑧∈Z, ⟨𝑧, 𝜇⟩=

$$
∫
$$

Y ℓ(𝑧, 𝑦)𝜇(d𝑦), and the distance between signed measures being 𝑑(𝜇1, 𝜇2) = sup𝑧∈Z ⟨𝑧, 𝜇1 −𝜇2⟩. Note that Lemma 7 is a pointwise result, holding for any 𝑥∈X, that is integrated over X afterwards. Therefore, it is enough to consider X = {𝑥} and remove the dependency in X to understand it. The simplex ΔY naturally splits into the decision region 𝑅𝑧for 𝑧∈Z as illustrated on Figure 5.1. The main idea of Lemma 7 is that one does not have to precisely estimate 𝑔∗(𝑥) = 𝜌|𝑥but only has to make sure that 𝑔𝑛(𝑥) falls in the same region on Figure 5.1.

$$
b b
𝑅𝑏
𝐹
𝜇★ 𝜇𝑛
𝑅𝑎
𝑅𝑐
a c a c
$$

[FIGURE: Figure 5.1]

Figure 5.1: Illustration of Lemma 7. Simplex ΔY, for Y = Z = {𝑎, 𝑏, 𝑐} and ℓa symmetric loss deﬁned as ℓ(𝑎, 𝑏) = ℓ(𝑎, 𝑐) = 1 and ℓ(𝑏, 𝑐) = 2, while ℓ(𝑧, 𝑧) = 0. This leads to the decision regions 𝑅𝑧represented in colors. Given 𝑥∈X, if 𝑔∗(𝑥) corresponds to a distribution 𝜇∗:= 𝜌|𝑥falling in 𝑅𝑎, and if 𝑔𝑛(𝑥) represented by ˆ𝜇falls closer to 𝜇∗than the distance between 𝜇∗and the decision frontier 𝐹(represented by a circle on the right ﬁgure), then ˆ𝜇is also in 𝑅𝑎, and therefore 𝑓∗(𝑥) = 𝑓𝑛(𝑥) = 𝑎.

## 5.3 Rate acceleration under margin condition

In this section, we introduce a condition that 𝑔∗is not too often close to the decision frontier 𝐹. It generalizes the so-called “Tsybakov margin condition” known for classiﬁcation. Under this condition, we prove rates that generalize the results of Audibert and Tsybakov (2007) from binary classiﬁcation to generic structured prediction problems, which opens the way to “superfast” rates in structured prediction.

### 5.3.1 No density separation

To get fast convergence rates, one has to make assumptions on the problem. A classical assumption is that 𝑔∗ is smooth enough in order to get concentration bounds similar to Assumption 2 when considering a speciﬁc class of estimates 𝑔𝑛. In our decoding setting (Lemma 6), learning is made easy when it is easy to estimate in which region 𝑅𝑧the optimal 𝑔∗will fall in. This is in particular the case, when there is a margin 𝑡0 > 0, for which, for no point 𝑥∈supp 𝜌X , 𝑔∗(𝑥) falls at distance 𝑡0 of the decision frontier 𝐹, motivating the following deﬁnition.

Assumption 3 (No-density separation). A surrogate solution 𝑔∗will be said to satisfy the no-density separation, if there exists a 𝑡0 > 0, such that

$$
P𝑋(𝑑(𝑔∗(𝑋), 𝐹) < 𝑡0) = 0. (5.6)
$$

(5.6)

This condition is alternatively called the hard margin condition, or sometimes “Massart’s noise condition” for binary classiﬁcation (Massart and Nédélec, 2006).

Remark 9 (Separation in Y and separation in X). It is important to realize that (5.6) is a condition of separation in ΔY that should hold for all 𝑥∈X, but it does not state any separation between classes in X for 𝑓∗: X →Z. To visualize it, consider the classiﬁcation problem where X = [−1, 1], Y = Z = {−1, 1} and ℓ(𝑧, 𝑦) = 1𝑧≠𝑦.

• A situation where 𝜌X is uniform on X and E[𝑌|𝑋= 𝑥] = 2 · 1𝑥∈𝑝N+{𝑎| |𝑎|<𝑝/4} −1, for 𝑝= 1/50, satisﬁes separation in ΔY (5.6), but classes are not separated in X.

<!-- page: 52 -->

$$
E[𝑌|𝑋= 𝑥] E[𝑌|𝑋= 𝑥]
1 𝑔∗(𝑥) 𝑓∗(𝑥) 1
𝑡0
𝑥 𝑥
𝑓∗(𝑥) 𝑔∗(𝑥)
−1 −1
$$

[FIGURE: Figure 5.2]

Figure 5.2: Illustration of Remark 9. We represent two instances of binary classiﬁcation (see Examples 8 and 9). On the left example, when 𝜌X is such that there is no mass where the sign of 𝑔∗changes, classes are separated in X, yet the no-density separation is not veriﬁed. On the right, classes are not separated in X, but the problem satisﬁes the no-density separation as there is no 𝑥such that 𝑑(𝑔∗(𝑥), 𝐹) = |𝑔∗(𝑥)| < 𝑡0. Note that when 𝜌X is uniform, the left problem satisﬁes a milder separation condition, introduced thereafter and called the 1-low-density separation.

• A situation where 𝜌is uniform on [−1, −.5] ∪[.5, 1], with E[𝑌|𝑋= 𝑥] = sign(𝑥)(1 −|𝑥|)𝑝, for 𝑝> 0, satisﬁes a separation of classes in X but does not satisfy (5.6). Note that continuity of 𝑔∗and the no-density separation in (5.6) imply separation of classes in X. Note also that to get concentration inequality such as (5.4), one usually supposes that 𝑔∗is smooth. We refer the curious reader to Section 2.4 in Steinwart and Scovel (2007) for separation in X.

The introduction of Assumption 3 is motivated by the following result.

Theorem 1 (Rates under no-density separation). When ℓis bounded by ℓ∞(i.e., ℓ(𝑧, 𝑦) ≤ℓ∞for any (𝑧, 𝑦) ∈Z × Y) and satisﬁes Assumption 1, and Z is ﬁnite, under the no-density separation Assumption 3, and the concentration Assumption 2, the excess risk is controlled

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞exp − 𝐿𝑛𝑡2 0 1 + 𝑀𝑛𝑡0 ! .
$$

Proof. Because we make a mistake only when 𝑑(𝑔∗(𝑥), 𝐹) ≥∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥, we make no mistake when ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥< 𝑡0; otherwise we can consider the worse error we are going to pay, that is ℓ∞, leading to

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞P𝑋(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡0).
$$

Taking the expectation with respect to D𝑛and using the fact that E𝐴P𝐵(𝑍) = E𝐴E𝐵[1𝑍] = E𝐵E𝐴[1𝑍] = E𝐵P𝐴(𝑍), and plug-in the concentration inequality (5.4), we get the result. □ Example 10 (Image classiﬁcation). In image classiﬁcation, one can arguably assume that the class of an image is a deterministic function of this image. With the 0-1 loss, it implies that the image classiﬁcation problem veriﬁes the no-density separation. The same holds for any discrete problem where the label is a deterministic function of the input. Based on Theorem 1 and (5.4) in which 𝑀is generally a constant when 𝐿 is proportional to the number of data, it is reasonable to ask for exponential convergences rates on such problems.

### 5.3.2 Low density separation

While we presented the no-density separation ﬁrst for readability, it is a strong assumption. Recall our example, Remark 9, with E[𝑌|𝑋= 𝑥] = sign(𝑥)(1 −|𝑥|)𝑝, only around 𝑥= 1 and 𝑥= −1 is 𝑑(𝑔∗(𝑥), 𝐹) not bounded away from zero. While the neighborhood of those points should be studied carefully, the error on all other points 𝑥∈[−1 + 𝑡, 1 −𝑡] can be controlled with exponential rates. The low-density separation, also known as the Tsybakov margin condition in binary classiﬁcation, will allow a reﬁned control to get fast rates in such a setting.

Assumption 4 (Low-density separation). A surrogate solution 𝑔∗is said to satisfy the low-density separation, if there exists 𝑐𝛼> 0, and 𝛼> 0, such that for any 𝑡> 0

$$
P𝑋(𝑑(𝑔∗(𝑋), 𝐹) < 𝑡) ≤𝑐𝛼𝑡𝛼. (5.7)
$$

(5.7)

This condition is alternatively called the margin condition.

<!-- page: 53 -->

The low-density separation spans all situations from the hard margin condition, that can be seen as 𝛼= +∞, to situations without any margin assumption corresponding to 𝛼= 0. The coeﬃcient 𝛼is an intrinsic measure of the easiness of ﬁnding 𝑓∗in the problem (ℓ, 𝜌). For example, the setting described in the last paragraph corresponds to the case 𝛼= 1/𝑝. We discuss the equivalence of Assumption 4 to deﬁnitions appearing in the literature in Remark 10.

Theorem 2 (Optimal rates under low density separation). Under reﬁned calibration in (5.5), concentration (Assumption 2), and low-density separation (Assumption 4), the risk is controlled as

$$
𝑀𝛼+1 𝑛 𝐿−(𝛼+1) −𝛼+1
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓𝑐𝛼𝑐 𝑛 + 𝐿 2 𝑛 ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

for 𝑐a constant that only depends on 𝛼, that can be expressed through the Gamma function evaluated in quantity depending on 𝛼, meaning that when 𝛼is big, 𝑐behaves like 𝛼𝛼. Note that it is not possible to derive a better bound only given (5.4), (5.5) and (5.7). \int_{0}

Sketch for Theorem 2, details in Appendix 5.A.5. Based on the reﬁned calibration inequality in (5.5), and using that E[𝑋] = 0 P(𝑋> 𝑡) d𝑡, it is possible to show that the expectation of the excess risk behave like

$$
∫∞
0 P𝑋(𝑑(𝑔∗(𝑥), 𝐹) < 𝑡) sup PD𝑛(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡) d𝑡.
𝑥
$$

Based on Assumptions 2 and 4, the integrand behaves like 𝑡𝛼exp(−𝐿𝑛𝑡2/(1 + 𝑀𝑛𝑡)). A change of variable and the study of the Gamma function leads to the result. We provide all the details in Appendix 5.A.5. Note that while we stated Theorem 2 under an exponential inequality of Bernstein type (Assumption 2), similar theorems can be derived for any type of exponential concentration inequality, as stated in Lemma 18 in Appendix 5.A.6. □ Theorem 2 is to put in perspective with the work of Nowak-Vila et al. (2019) which considers the same setup as ours, yet only succeeds to derive acceleration by a power 2(𝛼+ 1)/(𝛼+ 2), while we got an acceleration by a power (𝛼+ 1)/2 as already mentioned in the related work section. This gain will appear more clearly in Theorem 6.

Remark 10 (Independence to the decomposition of ℓ). While we have stated results based on the quantity 𝑑(𝑔∗(𝑥), 𝐹), generalization of the Tsybakov margin condition has also been expressed through the quantity inf𝑧≠𝑧∗E𝑌∼𝜌|𝑥ℓ(𝑧,𝑌)−E𝑌∼𝜌|𝑥ℓ(𝑧∗,𝑌) instead of 𝑑(𝑔∗(𝑥), 𝐹) (Nowak-Vila et al., 2019). We show in Appendix 5.A.3 that the two deﬁnitions of the margin condition are equivalent.

Remark 11 (Scope of our work). Our work relies on pointwise exponential concentration inequalities (Assumption 2) which are specially designed to work well with the Tsybakov margin condition. It is natural for localized averaging methods such as nearest neighbors, or for surrogate methods leading to 𝐿∞concentration. For surrogate methods leading to concentration of other quantities, it is possible to use similar tricks under diﬀerent “margin” conditions (e.g. Steinwart and Scovel (2007) for a margin condition designed for the Hinge loss).

Note that 𝐿2 concentration on 𝑔𝑛toward 𝑔∗(such as the one derived by Marteau-Ferey et al. (2019) for logistic regression) could also be turned into fast convergence of 𝑓𝑛toward 𝑓∗, since, in essence, for points 𝑥∈X where 𝜌(d𝑥) is high, the quantity 𝑔∗(𝑥) −𝑔𝑛(𝑥) will have a non-negligible contribution to ∥𝑔∗−𝑔𝑛∥𝐿2 – allowing to cast concentration in 𝐿2 to concentration pointwise in 𝑥– and for points 𝑥∈X where 𝜌(d𝑥) is negligible, it is acceptable to pay the worst error, since it will have a small contribution to the excess of risk.

Finally, note that it is also possible to let the right hand-side term in (5.4) depends on 𝑥, and to modify Theorem 1 with 𝐿= E[𝐿(𝑋)].

### 5.3.3 The importance of constants

In this subsection, we discuss the importance of constants when providing learning rates. Assumption 3 corresponds to asking for 𝑔∗(𝑥) never to enter a neighborhood of 𝐹deﬁned through 𝑡0. Similarly, when X is parametrized such that 𝜌X is uniform, the parameter 𝛼in Assumption 4 corresponds to the speed at which 𝑔∗(𝑥) “get through” the decision frontier 𝐹. In order to have a higher 𝛼and optimize the dependency in 𝑛in the bound of Theorem 2, it is natural to think of inﬁnitesimal perturbations of 𝑔∗to make it cross the

<!-- page: 54 -->

boundary orthogonally (or even jump over it and satisfy the no-density separation). To give a precise example, in binary classiﬁcation, let us artiﬁcially add smoothness to the function 𝑔∗(𝑥) = 𝑥𝑞when approaching zero. Consider 𝑔∗: [0, 1] →[−1, 1], 𝑥→𝑐𝑞−𝑝𝑥𝑝1𝑥<𝑐+ 𝑥𝑞1𝑥≥𝑐, and 𝑥uniform, and 𝑝< 𝑞. In this setting, 𝛼can be taken anywhere in [0, 𝑝−1). Naively, we could ask for the biggest possible 𝛼in order to have the best dependency in 𝑛in the learning rates given by Theorem 2. While this approach will higher 𝛼, it will also higher 𝑐𝛼, compensating the gain one could expect from such a strategy. Indeed, for 𝛼∈[0, 𝑝−1], at best, we can take 𝑐𝛼= 1𝛼<𝑞−1 + 𝑐1−𝑞𝛼1𝛼≥𝑞−1. This shows the importance of optimizing both 𝛼and 𝑐𝛼𝑐to minimize the lower bound appearing in Theorem 2 when given a ﬁxed number of sample 𝑛.

In a word, while we only give results that are optimized in 𝑛, when 𝑛is ﬁxed, better bounds could be given by optimizing parameters and constants simultaneously. For example, when X = R𝑑and 𝑔∗belongs to the Sobolev space 𝐻𝑚for all 𝑚∈[0, 𝑚∗], and satisﬁes Assumption 4 for all 𝛼∈[0, 𝛼∗], we expect the best bound, that could be derived from our proof technique, to be of form

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ min 𝑚≤𝑚∗,𝛼<𝛼∗𝛼𝛼𝑐𝛼𝑐𝜓∥𝑔∗∥𝐻𝑚𝑛−𝑚(𝛼+1)
2𝑑 .
$$

Yet, for simplicity, we will express those bounds as 𝑏𝑛−𝑚∗(𝛼∗+1) 2𝑑 , for 𝑏a big constant.

## 5.4 Application to nearest neighbors

In this section, we consider the Bayes approximate risk estimator proposed by Stone (1977), with weights given by nearest neighbors (Cover and Hart, 1967). We prove, under regularity assumptions, concentration inequalities similar to (5.4), which allow us to derive exponential and polynomial rates. Given samples (𝑋𝑖,𝑌𝑖) ∼𝜌⊗𝑛, 𝑘∈N and a metric 𝑑on X, the estimator is

$$
𝑘−1 if Í𝑛

𝑛 ∑︁ 𝑗=1 1𝑑(𝑥,𝑋𝑗) ≤𝑑(𝑥,𝑋𝑖) < 𝑘 0 if Í𝑛
𝑔𝑛(𝑥) = 𝛼𝑖(𝑥)𝜑(𝑌𝑖), with 𝛼𝑖(𝑥) =  𝑗=1 1𝑑(𝑥,𝑋𝑗)<𝑑(𝑥,𝑋𝑖) ≥𝑘 (𝑝𝑘)−1 else, with 𝑝= Í𝑛 (5.8)
𝑖=1 𝑗=1 1𝑑(𝑥,𝑋𝑗)=𝑑(𝑥,𝑋𝑖).
𝑛= Í𝑛
$$

(5.8)

To study the convergence of 𝑔𝑛, we introduce the noise free estimator 𝑔∗ 𝑖=1 𝛼𝑖(𝑥)𝑔∗(𝑋𝑖). This allows separating the error due to the randomness of the labels 𝑌𝑖∼𝜌|𝑋𝑖, and the error due to the diﬀerence between 𝑔∗(𝑥) and the averaging of 𝑔∗on the neighbors of 𝑥deﬁning 𝑔𝑛. To control the ﬁst error, we need a bounded moment condition on 𝜑(𝑌). We reuse an assumption from Bernstein (1937), that is classic in machine learning (e.g., Caponnetto and De Vito, 2006; Lin et al., 2020).

Assumption 5 (Sub-exponential moment of 𝜌|𝑥). Suppose that there exists 𝜎2, 𝑀> 0 such that for any 𝑥∈supp 𝜌X , for any 𝑚≥2, we have

$$
E𝑌∼𝜌|𝑥 ∥𝜑(𝑌) −𝑔∗(𝑥)∥𝑚 ≤1 2𝑚!𝜎2𝑀𝑚−2.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Example 11 (Moment bound on 𝜑(𝑌)). Assumption 5 is a classical assumption that is notably satisﬁed when 𝜑(𝑌) is bounded by 𝑀, with 𝜎2 its variance, or when (𝜑(𝑌) | 𝑋) is Gaussian with covariance bounded by a constant independent of 𝑋(see a proof of this standard result by Fischer and Steinwart, 2020).

$$
𝑔∗(𝑥) −𝑔∗
$$

behaves like sup𝑥′∈B(𝑥,𝑟) ∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥, with 𝑟such that 𝜌X (B(𝑥, 𝑟)) ≈𝑘/𝑛, such an 𝑟modeling the distance between 𝑥and its 𝑘-th neighbor. This motivates the following assumption.

To control the second error, we notice, for 𝑥∈supp 𝜌X , that the quantity

$$
𝑛(𝑥)
$$

Assumption 6 (Modiﬁed Lipschitz condition (Chaudhuri and Dasgupta, 2014)). 𝑔∗is said to verify the 𝛽-Modiﬁed Lipschitz condition if there exists 𝑐𝛽> 0 such that for any 𝑥, 𝑥′ ∈supp 𝜌X

$$
∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥≤𝑐𝛽𝜌X (B(𝑥, 𝑑(𝑥, 𝑥′)))𝛽,
$$

where 𝑑is the distance on X, and B(𝑥, 𝑡) ⊂X the ball of center 𝑥and radius 𝑡.

Typically, the 𝛽that appears in Assumption 6 is linked with the dimension of a subset of X containing most of the mass of 𝜌X (see below). This will slow the rates according to this dimension parameter, a property referred to as the curse of dimensionality.

<!-- page: 55 -->

Example 12 (Classical assumptions). When X = R𝑑, if 𝑔is 𝛽′-Hölder continuous, and 𝜌X is regular in the sense that, there exists a constant 𝑐and 𝑡∗> 0 such that for 𝑥∈supp 𝜌X and any 𝑡∈[0, 𝑡∗], 𝜌X (B(𝑥, 𝑡)) ≥𝑐𝜆(B(𝑥, 𝑡)), with 𝜆the Lebesgue measure on X, then 𝑔satisﬁes the modiﬁed Lipschitz condition with 𝛽= 𝛽′/𝑑. The condition on 𝜌X is usually split in a condition of minimal mass of 𝜌X , and a condition of regular boundaries of supp 𝜌X (e.g., Audibert and Tsybakov, 2007). We provide more details in Appendix 5.B.1.

We now state convergence results, respectively proven in Appendices 5.B.2, 5.B.3 and 5.B.4, in which the constant values 𝑏1 to 𝑏6 appear explicitly. Note that results provided by Lemma 12 are already known in the literature (Györﬁet al., 2002), while Theorems 3 and 4 were only known in binary classiﬁcation, but we generalize them to any discrete structured prediction problem. It should be noted that rates in Theorem 4 match the minimax rates derived by Audibert and Tsybakov (2007) in the case of binary classiﬁcation.

Lemma 12 (Nearest neighbors concentration). Under Assumptions 5 and 6, there exist constants 𝑏1, 𝑏2, 𝑏3 > 0, such that for any 𝑥∈supp 𝜌X and any 𝑡> 0,

$$
𝑔𝑛(𝑥) −𝑔∗ > 𝑡 ≤2 exp
−𝑏1𝑘𝑡2
PD𝑛 𝑛(𝑥) .
1 + 𝑏2𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

And for 𝑡> (𝑘/2𝑛)𝛽, when 𝜌X is continuous1

$$
PD𝑛 

𝑔∗ 𝑛(𝑥) −𝑔∗(𝑥) > 𝑡 ≤exp −𝑏3𝑛𝑡 \frac{1}{𝛽} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Theorem 3 (Nearest neighbors fast rates under no-density assumption). When ℓis bounded by ℓ∞, satisﬁes Assumption 1, and Z is ﬁnite, under the no-density separation, Assumption 3, and Assumptions 5 and 6, there exist two constants 𝑏4, 𝑏5 > 0 that do not depend on 𝑛or 𝑘such that for any 𝑛∈N∗and any 𝑘such that (𝑘/2𝑛)𝛽< 𝑡0, we have

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2ℓ∞exp(−𝑏4𝑘) + ℓ∞exp(−𝑏5𝑛). (5.9)
$$

(5.9)

Theorem 4 (Nearest neighbors fast rates under low-density assumption). When ℓsatisﬁes Assumption 1, and Z is ﬁnite, under the low-density separation, Assumption 4, and Assumptions 5 and 6, considering the

$$
j 𝑘0𝑛 \frac{2𝛽}{2𝛽+1} k
$$

, for any 𝑘0 > 0, there exists a constant 𝑏6 > 0 that does not depend on 𝑛such that for any 𝑛∈N∗, scheme 𝑘𝑛=

$$
𝑘0𝑛
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤𝑏6𝑛−𝛽(𝛼+1) 2𝛽+1 . (5.10)
$$

(5.10)

Remark 13 (Scope of our work). The same type of argument works for other local averaging methods, such as Nadaraya-Watson (Nadaraya, 1964; Watson, 1962), local polynomials (Cleveland, 1979; Audibert and Tsybakov, 2007) or decision trees (Breiman et al., 1984).

## 5.5 Application to reproducing kernel ridge regression

In this section, we consider the kernel ridge regression estimate 𝑔𝑛of 𝑔∗ﬁrst proposed by Ciliberto et al. (2016), and we prove, under regularity assumptions, uniform concentration inequalities similar to (5.4), which allow us to derive superfast rates at the end of the section. Given a symmetric, positive semi-deﬁnite kernel 𝑘: X × X →R+, the kernel ridge regression estimation 𝑔𝑛of 𝑔∗is deﬁned similarly to (5.8) yet with weights 𝛼(𝑥) ∈R𝑛deﬁned as

$$
1 1 
𝛼(𝑥) = ( ˆ𝐾+ 𝜆)−1 ˆ𝐾𝑥, ˆ𝐾= ∈R𝑛×𝑛, ˆ𝐾𝑥=
𝑛𝑘(𝑋𝑖, 𝑋𝑗) 𝑛𝑘(𝑥, 𝑋𝑖) ∈R𝑛.
𝑖,𝑗≤𝑛 𝑖≤𝑛
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

To state regularity assumptions, we introduce a minimal setup linked to the reproducing kernel 𝑘. To keep the exposition clear, we relegate technicalities in Appendix 5.C. We deﬁne the operator 𝐾operating on functions 𝑓∈𝐿2(X, H, 𝜌X ) and 𝐾X operating on 𝑓∈𝐿2(X, R, 𝜌X ), both deﬁned as

$$
(𝐾𝑓)(𝑥′) = ∫ X 𝑘(𝑥′, 𝑥) 𝑓(𝑥) d𝜌X (𝑥).
$$

1Note that this topological assumption ease derivations but is not fundamental for such non-asymptotic results.

<!-- page: 56 -->

$$
Empirical convergences \frac{α=0.1}{α=1}
$$

Excess of risk (log10) Number of sample (log10)

[FIGURE: Figure 5.3]

Figure 5.3: Empirical convergence rates. We consider binary classiﬁcation, with X = [−1, 1], 𝑔∗(𝑥) = sign(𝑥) ∗|𝑥| 1 𝛼, for 𝛼∈{.1, 1} and 𝜌X uniform. We plot in solid the logarithm of the excess risk averaged over 100 trials against the logarithm of the number of samples for 𝑛∈[10, 106], and plot in dashed the expected slope of those curves due to Theorem 4 (i.e., we ﬁt the constant 𝐶in the rate 𝐶𝑛−𝛾with 𝛾obtained from the bound in (5.10)).

Inheriting from the symmetry and positive semi-deﬁniteness of 𝑘, 𝐾is self-adjoint with the spectrum in R+. To study the convergence of 𝑔𝑛to 𝑔∗, it is useful to introduce the approximate orthogonal projection on im 𝐾

$$
1 2 , deﬁned for 𝜆> 0 as 𝑔𝜆= 𝐾(𝐾+ 𝜆)−1𝑔∗.
$$

We introduce three assumptions linked with the regularity of the problem, referred to as the capacity condition, interpolation inequality and source condition. Those are classical assumptions to prove uniform rates of the kernel ridge regression estimates. They could be found, in particular, by Fischer and Steinwart (2020) under the respective names of (EVD), (EMB) and (SRC), but also by Pillaud-Vivien et al. (2018a); Lin et al. (2020). Our assumptions diﬀer in that they are expressed for vector-valued functions, which usually generate compactness issues (Caponnetto and De Vito, 2006). However, when Z is ﬁnite, H is ﬁnite dimensional, and 𝐾can be shown to be a compact operator, which allows considering fractional power without deﬁnition issues.

$$
\frac{𝐾𝜎}{X}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Assumption 7 (Capacity condition). Suppose Tr

$$
\frac{𝐾𝜎}{X} < +∞for 𝜎∈[0, 1].
$$

Assumption 8 (Interpolation inequality). Assume the existence of 𝑝∈[0, 1

$$
2], 𝑐𝑝> 0 such that
∀𝑔∈(ker 𝐾)⊥, ∥𝐾𝑝𝑔∥𝐿∞≤𝑐𝑝∥𝑔∥𝐿2 .
$$

Assumption 9 (Source condition). Suppose 𝑔∗∈im 𝐾𝑞for 𝑞∈(𝑝, 1].

When 𝑞= 1/2, the source condition is often expressed as 𝑔∗belonging to the reproducing kernel Hilbert space associated to the kernel 𝑘. Note that when 𝑘is bounded, Assumptions 7 and 8 hold with 𝜎= 1 and 𝑝= 1/2. In those assumptions, for 𝑝and 𝜎the smaller, and for 𝑞the bigger, the faster the convergence rates will be.

Example 13 (Classical assumptions). For Assumption 8 to hold, minimal mass and regular support of 𝜌, similarly to Example 12, are often assumed, as well as regularity of functions in im 𝐾𝑝, in coherence with Remark 11. For Assumption 9 to hold, it is classical to assume regularity of 𝑔∗, matching the regularity of function spaces derived from the kernel 𝑘. The value of 𝜎in Assumption 7 often comes as a bonus of regularity assumptions on 𝜌and speciﬁcity of the RKHS implied by 𝑘. See Example 2 by Pillaud-Vivien et al. (2018a) and Section 4 by Fischer and Steinwart (2020) as well as references therein for concrete examples.

We now state convergence results respectively proven in Appendices 5.C.5 and 5.C.6, 5.C.7, and 5.C.8. Lemma 14 is a generalization to vector-valued functions of kernel ridge regression uniform convergence rates known for real-valued function (see Fischer and Steinwart, 2020). Note that a similar result to Theorem 5 was provided for binary classiﬁcation by Koltchinskii and Beznosova (2005), but we generalize exponential rates with kernel ridge regression to any discrete structured prediction problem. Theorem 6 is new, even in the context of binary classiﬁcation. It states that, while, up to now, only rates in 𝑛−1/4 were known for 𝑓𝑛(Ciliberto et al., 2020), one can indeed hope for arbitrarily fast rates, depending on the hardness of the problem, read in the value of 𝛼∈[0, ∞).

<!-- page: 57 -->

Lemma 14 (Reproducing kernel concentration). Under Assumptions 7, 8 and 9, for any 𝜆> 0,

$$
∥𝑔𝜆−𝑔∗∥𝐿∞≤𝑏1𝜆𝑞−𝑝.
$$

With 𝑏1 = 𝑐𝑝∥𝐾−𝑞𝑔∗∥𝐿2. Moreover, when the kernel 𝑘is bounded and under Assumption 5, there exists three constants 𝑏2, 𝑏3, 𝑏4, 𝑏5 > 0 that does not depend nor on 𝜆nor on 𝑛such that

$$
−𝑏3𝑛𝜆2𝑝 
−𝑛𝜆2𝑝+𝜎𝑡2
P (∥𝑔𝑛−𝑔𝜆∥∞> 𝑡) ≤𝑏2𝜆−𝜎exp + 4 exp .
𝑏4 + 𝑏5𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As long as 𝑏3𝑛≥𝜆−𝑝, and 𝜆≤min

$$
∥𝐾∥op , 1 .
$$

Theorem 5 (Kernel ridge regression fast rates under no-density assumption). When the loss ℓis bounded, satisﬁes Assumption 1 and Z is ﬁnite, under the 𝑡0-no-density separation condition, and Assumptions 5, when 𝑘is bounded, if 𝜆𝑛= 𝜆, for any 𝜆> 0 such that ∥𝑔∗−𝑔𝜆∥𝐿∞< 𝑡0, then there exist two constants 𝑏6, 𝑏7 > 0 such that, for any 𝑛∈N∗,

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤𝑏6 exp(−𝑏7𝑛), (5.11)
$$

(5.11)

with 𝑓𝑛given by the kernel ridge regression surrogate estimate.

Theorem 6 (Kernel ridge regression fast rates under low-density assumption). When ℓsatisﬁes Assumption 1, is bounded and Z is ﬁnite, under the 𝛼-low-density separation condition, and Assumptions 5, 7, 8 and 9, if 𝜆𝑛= 𝜆0𝑛− 1 2𝑞+𝜎, for any 𝜆0 > 0, there exists 𝑏8 > 0, such that for any 𝑛∈N∗,

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤𝑏8𝑛−(𝑞−𝑝) (1+𝛼) 2𝑞+𝜎 . (5.12)
$$

(5.12)

## 5.6 Conclusion

In this paper, we have shown how, for discrete problems, to leverage exponential concentration inequalities derived on continuous surrogate problems, in order to derive faster rates than rates directly obtained through calibration inequalities. Those rates are arbitrarily fast, depending on a parameter characterizing the hardness of the discrete problem. We have shown how this method directly applies to local averaging methods and to kernel ridge regression, which allows deriving “superfast” rates for any discrete structured prediction problem.

This opens the way to several follow-up, such as • Application follow-up, consisting of tackling concrete problem instances, such as predicting properties of DNA-sequence (Jaakkola et al., 2000), e.g., gene mutations responsible for diseases, with well- designed kernels on DNA in order to higher the exponent appearing in Theorem 6. • Computational follow-up, pushing our analysis further to understand how to design better algorithms on discrete problems. For example, by adding a regularization pushing 𝑔𝑛away from the decision frontier 𝐹, and adding a term in 1∥𝑔𝑛(𝑥)−𝑔∗(𝑥) ∥>𝑑(𝑔𝑛(𝑥),𝐹) in (5.5) for the analysis. • Theoretical follow-up, to widen our analysis to other types of smooth surrogates, and to parametric methods, such as deep learning models, assuming that functions are parametrized by a parameter 𝜃, that some analysis gives concentration on 𝜃𝑛−𝜃∗similar to (5.4) and that calibration inequalities relate the error on 𝜃with the error between 𝑓𝑛= 𝑓𝜃𝑛and 𝑓∗= 𝑓𝜃∗.

<!-- page: 58 -->

<!-- page: 59 -->

# Appendix

## 5.A Fast rates

In the following, we consider X and Y to be Polish spaces, i.e., separable completely metrizable topological spaces, in order to deﬁne the distribution 𝜌. We also consider Z endowed with a topology that makes it compact, and that makes 𝑧→E𝑌∼𝜇ℓ(𝑧,𝑌) continuous for any 𝜇∈ΔY, in order to have minimizer well-deﬁned. For a Polish space A, we denote by ΔA the simplex formed by the set of Borel probability measures on this space. For 𝜌∈ΔX×Y, we denote by 𝜌|𝑥the conditional distribution of 𝑌given 𝑥, and by 𝜌X the marginal distribution over X. We suppose H separable Hilbert and that the mapping 𝜑is measurable in order to deﬁne the pushforward measure 𝜑∗𝜌|𝑥. We assume that, for 𝜌X -almost every 𝑥, (𝜑(𝑌)|𝑋= 𝑥) has a second moment, in order to consider the conditional mean 𝑔∗(𝑥) as the solution of the well-deﬁned problem consisting of minimizing ∥𝜉−𝜑(𝑌)∥2 for 𝜉∈H. We consider 𝜓to be continuous, in order to have the decoding problem well posed.

### 5.A.1 Proof of Lemma 6

With the notation of Lemma 6, for 𝑥∈supp 𝜌X

$$
E𝑌∼𝜌|𝑥[ℓ( 𝑓𝑛(𝑥),𝑌) −ℓ( 𝑓∗(𝑥),𝑌)] = ⟨𝜓( 𝑓𝑛(𝑥)) −𝜓( 𝑓∗(𝑥)), 𝑔∗(𝑥)⟩H
= ⟨𝜓( 𝑓𝑛(𝑥)), 𝑔𝑛(𝑥)⟩+ ⟨𝜓( 𝑓𝑛(𝑥)), 𝑔∗(𝑥) −𝑔𝑛(𝑥)⟩−⟨𝜓( 𝑓∗(𝑥)), 𝑔∗(𝑥)⟩
≤⟨𝜓( 𝑓∗(𝑥)), 𝑔𝑛(𝑥)⟩+ ⟨𝜓( 𝑓𝑛(𝑥)), 𝑔∗(𝑥) −𝑔𝑛(𝑥)⟩−⟨𝜓( 𝑓∗(𝑥)), 𝑔∗(𝑥)⟩
= ⟨𝜓( 𝑓𝑛(𝑥)) −𝜓( 𝑓∗(𝑥)), 𝑔∗(𝑥) −𝑔𝑛(𝑥)⟩
≤∥𝜓( 𝑓𝑛(𝑥)) −𝜓( 𝑓∗(𝑥))∥H ∥𝑔∗(𝑥) −𝑔𝑛(𝑥)∥H ≤2𝑐𝜓∥𝑔∗(𝑥) −𝑔𝑛(𝑥)∥H ,
$$

where the inequality ⟨𝜓( 𝑓𝑛(𝑥)), 𝑔𝑛(𝑥)⟩≤⟨𝜓( 𝑓∗(𝑥)), 𝑔𝑛(𝑥)⟩is due to the fact that 𝑓𝑛(𝑥) minimizes the functional 𝑧→⟨𝜓(𝑧), 𝑔𝑛(𝑥)⟩. Integrating over X leads to the results in Lemma 6.

### 5.A.2 Proof of Lemma 7

The ﬁrst part of the lemma is a geometrical result stating that to go from two elements 𝜉1 and 𝜉2 in Δ𝜑(Y), leading to two diﬀerent decoding, one has to pass by a point 𝜉1/2 ∈𝐹, where there is at least two possible decodings. Let us make it clearer. Consider 𝑥∈supp 𝜌X and suppose that 𝑓𝑛(𝑥) ≠𝑓∗(𝑥), deﬁne the path

$$
𝜁: \frac{[0, 1]}{𝜆} \frac{→}{→} \frac{Δ𝜑(Y)}{𝜆𝑔𝑛(𝑥) + (1 −𝜆)𝑔∗(𝑥).}
$$

Consider 𝑑: Δ𝜑(Y) →Z the decoding function used to retrieve 𝑓∗and 𝑓𝑛, from 𝑔∗and 𝑔𝑛, satisfying 𝑑(𝜉) ∈arg min𝑧∈Z ⟨𝜓(𝑧), 𝜉⟩. Consider the path 𝑑◦𝜁: [0, 1] →Z, it goes from 𝜁(0) = 𝑓∗(𝑥) to 𝜁(1) = 𝑓𝑛(𝑥). Consider 𝜆∞the supremum of (𝑑◦𝜁)−1( 𝑓∗(𝑥)). We will show that 𝜁(𝜆∞) ∈𝐹, this will lead to

$$
∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥= ∥𝑔𝑛(𝑥) −𝜁(𝜆∞)∥+ ∥𝜁(𝜆∞) −𝑔∗(𝑥)∥≥∥𝜁(𝜆∞) −𝑔∗(𝑥)∥≥𝑑(𝑔∗(𝑥), 𝐹),
$$

and to Lemma 7 by contraposition.

57

<!-- page: 60 -->

To show that 𝜁(𝜆∞) ∈𝐹, we will show that 𝑓∗(𝑥) ∈arg min𝑧⟨𝜓(𝑧), 𝜁(𝜆∞)⟩⊄{ 𝑓∗(𝑥)} . By deﬁnition of the supremum, there exists a sequence (𝜆𝑝)𝑝∈N converging to 𝜆∞such that

$$
𝑓∗(𝑥) ∈arg min 𝜓(𝑧), 𝜆𝑝𝑔𝑛(𝑥) + (1 −𝜆𝑝)𝑔∗(𝑥) ,
𝑧
$$

meaning that for all 𝑧≠𝑓∗(𝑥)

$$
𝜓( 𝑓∗(𝑥)), 𝜆𝑝𝑔𝑛(𝑥) + (1 −𝜆𝑝)𝑔∗(𝑥) ≤ 𝜓(𝑧), 𝜆𝑝𝑔𝑛(𝑥) + (1 −𝜆𝑝)𝑔∗(𝑥) .
$$

By continuity of the scalar product, it holds for 𝑝= ∞, which means 𝑓∗(𝑥) ∈arg min𝑧⟨𝜓(𝑧), 𝜁(𝜆∞)⟩. Now, suppose that arg min𝑧⟨𝜓(𝑧), 𝜁(𝜆∞)⟩= { 𝑓∗(𝑥)}, this means that for all 𝑧≠𝑓∗(𝑥),

$$
⟨𝜓( 𝑓∗(𝑥)), 𝜆∞𝑔𝑛(𝑥) + (1 −𝜆∞)𝑔∗(𝑥)⟩< ⟨𝜓(𝑧), 𝜆∞𝑔𝑛(𝑥) + (1 −𝜆∞)𝑔∗(𝑥)⟩.
$$

By continuity of this function according to 𝜆, this means that this still holds for 𝜆∞+ 𝜀𝑧for 𝜀𝑧> 0. Taking 𝜀= inf𝑧∈Z 𝜀𝑧, it means that 𝜆∞+ 𝜀∈(𝑑◦𝜁)−1( 𝑓∗(𝑥)). When Z is ﬁnite, 𝜀> 0, which contradicts the deﬁnition of 𝜆∞. Therefore, 𝜁(𝜆∞) ∈𝐹.

The second part of Lemma 7 follows from derivations in Appendix 5.A.1.

Remark 15 (Extension to discrete cases). Note that the same argument can be generalized to discrete problems – which could be deﬁned as Z endowed with a topology that makes 𝑧→E𝑌∼𝜇[ℓ(𝑧,𝑌)] con- tinuous with respect to 𝑧, and Z \ {𝑧} locally compact for any 𝑧∈Z – that are not degenerate, in the sense that 𝜌X almost all 𝑥∈X, there exists 𝑡> 0 such that the cardinality of the set deﬁned as

$$
E𝑌∼𝜌|𝑥[ℓ(𝑧,𝑌)] −inf𝑧′∈Y E𝑌∼𝜌|𝑥[ℓ(𝑧′,𝑌)] < 𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

if ﬁnite. This holds for classiﬁcation with inﬁnite countable classes, but it does not for regression on the set of rational numbers.

$$
𝑧
$$

Remark 16 (Extension to general cases). To remove the condition Z ﬁnite, one can change the deﬁnition of 𝑑(𝑔∗(𝑥), 𝐹) to inf𝜉∈H;{ 𝑓∗(𝑥) }≠arg min⟨𝜓(𝑧),𝜉⟩∥𝜉−𝑔∗(𝑥)∥, in order to make Lemma 7 hold for any Z.

### 5.A.3 Equivalence between generalizations of the Tsybakov margin condition

While we state the margin condition with 𝑑(𝑔∗(𝑥), 𝐹), it could also be stated with 𝑑(𝑔∗(𝑥), 𝐹∩Conv(𝜑(Y))) or with, which is the quantity considered by (Nowak-Vila et al., 2019),

$$
𝛾(𝑥) = inf 𝑧≠𝑧∗E𝑌∼𝜌|𝑥ℓ(𝑧,𝑌) −E𝑌∼𝜌|𝑥ℓ(𝑧∗,𝑌) = inf 𝑧≠𝑧∗⟨𝜓(𝑧) −𝜓(𝑧∗), 𝑔∗(𝑥)⟩.
$$

Indeed, when Z is ﬁnite and ℓis proper in the sense that ℓ(·, 𝑦) = ℓ(·, 𝑧) implies 𝑧= 𝑦, and that there is no 𝑧 that minimizes a linear combination of (ℓ(·, 𝑦))𝑦∈Y without minimizing a convex combination of the same family, we have the existence of two constants such that

$$
𝑐𝛾(𝑥) ≤𝑑(𝑔∗(𝑥), 𝐹∩Conv(𝜑(Y))) ≤𝑑(𝑔∗(𝑥), 𝐹) ≤𝑐′𝛾(𝑥).
$$

Mildness of our condition Let 𝑧′ be the argmin deﬁning 𝛾, geometric properties of the scalar product imply the existence of a 𝜉∈(𝜓(𝑧′) −𝜓(𝑧∗))⊥such that

$$
⟨𝜓(𝑧′) −𝜓(𝑧∗), 𝑔∗(𝑥)⟩= ∥𝜓(𝑧′) −𝜓(𝑧∗)∥∥𝑔∗(𝑥) −𝜉∥.
$$

Therefore,

$$
⟨𝜓(𝑧′) −𝜓(𝑧∗), 𝑔∗(𝑥)⟩≥min 𝑦,𝑦′ ∥𝜓(𝑦) −𝜓(𝑦′)∥∥𝑔∗(𝑥) −𝜉∥.
$$

Note that, by deﬁnition of 𝜉, ⟨𝜉, 𝜓(𝑧′)⟩= ⟨𝜉, 𝜓(𝑧∗)⟩. If 𝜉∈𝑅𝑧∗then 𝜉∈𝐹, otherwise 𝜉∉𝑅𝑧∗and then, there exists a point between 𝜉and 𝑔∗(𝑥) that belongs to the decision frontier (see Appendix 5.A.2 for a proof - for which we need some regularity assumption such as Z ﬁnite). In every case,

$$
∥𝑔∗(𝑥) −𝜉∥≥𝑑(𝑔∗(𝑥), 𝐹).
$$

This implies the existence of 𝑐′.

<!-- page: 61 -->

5.A. FAST RATES 59 Strength of our condition For any 𝑔𝑛such that 𝑓𝑛(𝑥) = 𝑧, we have

$$
⟨𝜓(𝑧) −𝜓(𝑧∗), 𝑔∗(𝑥)⟩= ⟨𝜓(𝑧), 𝑔∗(𝑥) −𝑔𝑛(𝑥)⟩+ ⟨𝜓(𝑧), 𝑔𝑛(𝑥)⟩−⟨𝜓(𝑧∗), 𝑔∗(𝑥)⟩
≤⟨𝜓(𝑧), 𝑔∗(𝑥) −𝑔𝑛(𝑥)⟩+ ⟨𝜓(𝑧∗), 𝑔𝑛(𝑥)⟩−⟨𝜓(𝑧∗), 𝑔∗(𝑥)⟩
≤2𝑐𝜓∥𝑔∗(𝑥) −𝑔𝑛(𝑥)∥.
$$

If we take the inﬁmum on both sides we have

$$
∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥≥ 1 2𝑐𝜓 inf 𝑧≠𝑧∗⟨𝜓(𝑧) −𝜓(𝑧∗), 𝑔∗(𝑥)⟩,
𝑑(𝑔∗(𝑥), 𝐹) = inf 𝑔𝑛(𝑥)∉𝑅𝑓∗(𝑥)
$$

where the left equality is provided, when Z is ﬁnite, by a similar reasoning to the one in Appendix 5.A.2. This implies the existence of 𝑐. Note also that if the loss is proper in the sense that if 𝑧minimizes ⟨𝜓(𝑧), 𝜉⟩for a 𝜉∈H, there exists a 𝜉∈Conv 𝜑(Y) such that 𝑧minimizes ⟨𝜓(𝑧), 𝜉⟩, we can consider 𝑔𝑛(𝑥) ∈Conv(𝜑(Y)), and therefore restrict 𝐹to 𝐹∩Conv 𝜑(Y). Finally, we have shown that, when Z ﬁnite and ℓproper

$$
𝑐𝛾(𝑥) ≤𝑑(𝑔∗(𝑥), 𝐹∩Conv(𝜑(Y))) ≤𝑑(𝑔∗(𝑥), 𝐹) ≤𝑐′𝛾(𝑥).
$$

This explains why we would consider 𝛾(𝑥), 𝑑(𝑔∗(𝑥), 𝐹∩Conv(𝜑(Y))) or 𝑑(𝑔∗(𝑥), 𝐹) to deﬁne the margin condition, it will only change the value of constants in Assumptions 3 and 4.

### 5.A.4 Reﬁnement of Theorem 1

It is possible to reﬁne Theorem 1 to remove the condition that the loss ℓis bounded. In the following, we omit the dependency of 𝐿𝑛and 𝑀𝑛to 𝑛.

Lemma 17 (Reﬁnement of Theorem 1). Under reﬁned calibration (5.5), concentration, Assumption 2, and no-density separation, Assumption 3, the risk is controlled as

$$
!1/2 
𝑡2 0𝐿
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤4𝑐𝜓𝐿−1/2 exp + 4𝑐𝜓𝑀𝐿−1 exp −𝑡0𝐿
− .
2 2𝑀
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Note that it is not possible to derive a better bound only given (5.4), (5.5) and (5.6). Yet when ℓis bounded by ℓ∞, we have

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞exp − 𝐿𝑡2 0 1 + 𝑀𝑡0 ! .
$$

Proof. Using the calibration inequality along with the no-density separation one, we get

$$
1∥𝑔𝑛(𝑋)−𝑔∗(𝑋) ∥≥𝑡0 ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥ 
R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓E𝑋
∫∞
= 2𝑐𝜓 P𝑋(∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥≥𝑡) d𝑡.
𝑡0
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Taking the expectation over D𝑛and using concentration inequality we have

$$
∫∞
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓 P𝑋,D𝑛(∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥≥𝑡) d𝑡
∫∞ 𝑡0 
− 𝐿𝑡2
≤2𝑐𝜓 exp d𝑡.
1 + 𝑀𝑡
𝑡0
∫∞ 1+𝑀𝑡 
−𝐿𝑡2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We only need to study the integral

$$
𝑡0 exp
$$

d𝑡. We ﬁrst clean the dependency on 𝑡inside the exponential using that

$$
1 2 −𝐿𝑡 − 𝐿𝑡2 −𝐿𝑡2 −𝐿𝑡
exp(−𝐿𝑡2) + exp ≤exp ≤exp + exp .
𝑀 1 + 𝑀𝑡 2 2𝑀
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 62 -->

$$
∫∞
$$

𝑡0 exp(−𝐴𝑡𝑝) d𝑡, for 𝑝∈{1, 2} and 𝐴> 0. The case 𝑝= 1, directly leads to 𝐴−1 exp(−𝐴𝑡0), explaining the part in 𝐿/𝑀. The case 𝑝= 2 is similar to the Gaussian integral, and can be handled with the following tricks We are left with the study of

$$
∫∞ ∫
exp(−𝐴𝑡2) d𝑡= 1
exp(−𝐴𝑡2) d𝑡
2
𝑡0 ∫ (−∞,−𝑡0]∪[𝑡0,∞) 1/2
= 1
((−∞,−𝑡0]∪[𝑡0,∞))2 exp(−𝐴∥𝑥∥2)) d𝑥
.
2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This last integral corresponds to integrate the function 𝑥→exp(−𝐴∥𝑥∥2) for 𝑥∈R2 on the domain ((−∞, −𝑡0] ∪[𝑡0, ∞))2. This function being positive and the domain being included in the domain {∥𝑥∥≥𝑡0} and containing the domain

$$
n 2𝑡0 o
√
∥𝑥∥≥ , we get
∫∞ 2 ∫∞ 2 ∫∞
n 2𝑡0 o exp(−𝐴∥𝑥∥2) d𝑥≤ exp(−𝐴𝑡2) d𝑡 ≤ exp(−𝐴∥𝑥∥2) d𝑥.
√
∥𝑥∥≥ 𝑡0 {∥𝑥∥≥𝑡0 }
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Using polar coordinate we get

$$
∫∞ ∫∞
exp(−𝐴∥𝑥∥2) d𝑥= 2𝜋 𝑟exp(−𝐴𝑟2) d𝑟= 𝜋𝐴−1 exp(−𝐴𝑡2
0).
{∥𝑥∥≥𝑡0 } 𝑡0
$$

Therefore,

$$
2−1√𝜋𝐴−1/2 exp(−𝐴2𝑡2 0)1/2 ≤ ∫∞
exp(−𝐴𝑡2) d𝑡≤2−1√𝜋𝐴−1/2 exp(−𝐴𝑡2
0)1/2.
𝑡0
$$

This explains the rates in 𝐿. □

### 5.A.5 Proof of Theorem 2

Using the calibration and Bernstein inequalities we get, omitting the dependency of 𝐿𝑛and 𝑀𝑛to 𝑛,

$$
1𝑑(𝑔𝑛(𝑋),𝑔∗(𝑋)) ≥𝑑(𝑔∗(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥ 
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓ED𝑛,𝑋
∫∞
 1𝑑(𝑔𝑛(𝑋),𝑔∗(𝑋)) ≥𝑑(𝑔∗(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥≥𝑡 d𝑡
= 2𝑐𝜓 0 PD𝑛,𝑋
∫∞
= 2𝑐𝜓 0 E𝑋PD𝑛(∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥≥max {𝑡, 𝑑(𝑔∗(𝑋), 𝐹)}) d𝑡
∫∞ 
− 𝐿max {𝑡, 𝑑(𝑔∗(𝑋), 𝐹)}2
≤2𝑐𝜓 0 E𝑋exp d𝑡
1 + 𝑀max {𝑡, 𝑑(𝑔∗(𝑋), 𝐹)}2
∫∞ 1𝑑(𝑔∗(𝑋),𝐹)<𝑡exp 
− 𝐿𝑡2
= 2𝑐𝜓 0 E𝑋 d𝑡
 1𝑑(𝑔∗(𝑋),𝐹) ≥𝑡exp 1 + 𝑀𝑡 
∫∞
−𝐿 𝑑(𝑔∗(𝑋), 𝐹)2
+ 2𝑐𝜓 0 E𝑋 d𝑡
 1 + 𝑀𝑑(𝑔∗(𝑋), 𝐹) 
∫∞
− 𝐿𝑡2
= 2𝑐𝜓 0 P𝑋(𝑑(𝑔∗(𝑋), 𝐹) < 𝑡) exp d𝑡
 1 + 𝑀𝑡 
− 𝐿𝑑(𝑔∗(𝑋), 𝐹)2
+ 2𝑐𝜓E𝑋 𝑑(𝑔∗(𝑋), 𝐹) exp .
1 + 𝑀𝑑(𝑔∗(𝑋), 𝐹)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let us begin by working on the ﬁrst term. We have, using the low-density separation hypothesis

$$
∫∞ ∫∞
− 𝐿𝑡2 0 𝑡𝛼exp(− 𝐿𝑡2
0 P𝑋(𝑑(𝑔∗(𝑋), 𝐹) < 𝑡) exp d𝑡≤𝑐𝛼 1 + 𝑀𝑡) d𝑡.
1 + 𝑀𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 63 -->

5.A. FAST RATES 61 Recall the expression of the Gamma integral

$$
2 
∫∞ ∫∞
Γ 𝛼+1
0 𝑡𝛼exp(−𝐿𝑡) d𝑡= Γ(𝛼+ 1)
𝐿𝛼+1 and 0 𝑡𝛼exp(−𝐿𝑡2) d𝑡= 2 .
2𝐿 𝛼+1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let us brieﬂy talk about optimality. Up to now, we have only used three inequalities: calibration, exponential concentration and low-density separation. Therefore, when those inequalities hold as equalities, we get a lower bound of order on the excess of risk as

$$
∫∞
0 𝑡𝛼exp(− 𝐿𝑡2
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≥2𝑐𝜓𝑐𝛼 1 + 𝑀𝑡) d𝑡
∫∞ 1 2𝑡𝛼 
exp(−𝐿𝑡2) + exp −𝐿𝑡
≥2𝑐𝜓𝑐𝛼 d𝑡
0 2 𝑀
©­­ « Γ 𝛼+1 2 + Γ(𝛼+ 1) 2 𝑀𝛼+1𝐿−(𝛼+1)ª®®
= 2𝑐𝜓𝑐𝛼 4 𝐿−𝛼+1
.
¬
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

For the upper bound, using that exp(−𝑎/1 + 𝑏) ≤exp(−𝑎/2) + exp(−𝑎/2𝑏), we get

$$
∫∞ 1 + 𝑀𝑡) d𝑡≤ ∫∞ 2 ) d𝑡+ ∫∞
0 𝑡𝛼exp(− 𝐿𝑡2 0 𝑡𝛼exp(−𝐿𝑡2 0 𝑡𝛼exp(−𝐿𝑡
2𝑀) d𝑡
2 Γ 𝛼+ 1 
= 2 𝛼−1 𝐿−𝛼+1 2 + 2𝛼+1Γ(𝛼+ 1)𝑀𝛼+1𝐿−(𝛼+1).
2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let study the second term in the excess of risk inequality. To enhance readability, write 𝜂(𝑋) = 𝑑(𝑔∗(𝑋), 𝐹). We will ﬁrst dissociate the two parts in the exponential with

$$
− 𝐿𝜂(𝑋)2 −𝐿𝜂(𝑋)2 −𝐿𝜂(𝑋)
E𝑋 𝜂(𝑋) exp ≤E𝑋 𝜂(𝑋) exp + exp .
1 + 𝑀𝜂(𝑋) 2 2𝑀
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We are left with studying E[𝜂(𝑋) exp(−𝐴𝜂(𝑋)𝑝)], for 𝐴> 0 and 𝑝∈{1, 2}. The function 𝑡→𝑡exp(−𝐴𝑡𝑝) achieves its maximum in 𝑡0 = (𝑝𝐴)−1/𝑝, increasing before and decreasing after. Notice that the quantity

$$
P(𝜂(𝑋) < 𝑡0) E𝑋[𝜂(𝑋) exp(−𝐴𝜂(𝑋)𝑝) | 𝜂(𝑋) < 𝑡0] ≤𝑐𝛼𝑡𝛼+1 0 exp(−𝐴𝑡𝑝 0 )
= 𝑐𝛼𝑝−𝛼+1 𝑝exp(−𝑝−1/𝑝)𝐴−𝛼+1
𝑝,
$$

is exactly of the same order as the control we had on the ﬁrst term in the excess of risk decomposition. This suggests considering the following decomposition

$$
E𝑋[𝜂(𝑋) exp(−𝐴𝜂(𝑋)𝑝)] = P(𝜂(𝑋) < 𝑡0) E𝑋[𝜂(𝑋) exp(−𝐴𝜂(𝑋)𝑝) | 𝜂(𝑋) < 𝑡0]
∞ ∑︁ 2𝑖𝑡0 ≤𝜂(𝑋) < 2𝑖+1𝑡0 
+ P(2𝑖𝑡0 ≤𝜂(𝑋) < 2𝑖+1𝑡0) E𝑋 𝜂(𝑋) exp(−𝐴𝜂(𝑋)𝑝)
𝑖=0
∞ ∑︁
≤𝑐𝛼𝑡𝛼+1 𝑜 exp(−𝐴𝑡𝑝 𝑐𝛼2𝛼(2𝑖𝑡0)𝛼+1 exp(−𝐴𝑡𝑝
0 ) + 0 (2𝑖)𝑝)
𝑖=0 !
∞ ∑︁
= 𝑐𝛼𝑡𝛼+1 exp(−𝑝−1/𝑝) + 2𝛼2𝑖(𝛼+1) exp(−𝑝−1/𝑝2𝑖𝑝)
.
𝑜
𝑖=0
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The convergence of the last series, ensures the existence of a constant 𝑐such that

$$
𝐿 −(𝛼+1) 𝐿 −𝛼+1 2 !
− 𝐿𝜂(𝑋)2
E𝑋 𝜂(𝑋) exp ≤𝑐 + .
1 + 𝑀𝜂(𝑋) 2𝑀 2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Adding everything together, we get the existence of two constants 𝑐′, 𝑐′′, such that

$$
2 
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓𝑐𝛼 𝑐′𝑀𝛼+1𝐿−(𝛼+1) + 𝑐′′𝐿−𝛼+1
.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This ends the proof by considering 𝑐= max (𝑐′, 𝑐′′).

<!-- page: 64 -->

### 5.A.6 Reﬁnement of Theorem 2

Some convergence analyses lead to exponential inequalities that are not of Bernstein type, indeed, our result still holds in those settings, as mentioned by the following lemma. In the following, we omit the dependency of 𝐿𝑛and 𝑀𝑛to 𝑛.

Lemma 18 (Reﬁnement of Theorem 2). Under the assumptions of Theorem 2, if the concentration is not given by Assumption 2 but given, for some positive constants (𝑎𝑖, 𝑏𝑖, 𝑝𝑖)𝑖≤𝑚, by, for all 𝑥∈supp 𝜌X and 𝑡> 0,

$$
𝑛 ∑︁
PD𝑛(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡) ≤ 𝑎𝑖exp(−𝑏𝑖𝑡𝑝𝑖).
𝑖=1
$$

Then the excess of risk is controlled by

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤𝑐 \sum_{𝑛 𝑖=1} 𝑎𝑖𝑏 −𝛼+1 𝑝𝑖 𝑖 ,
$$

for a constant 𝑐that does not depend on (𝑎𝑖, 𝑏𝑖)𝑖≤𝑚.

Proof. First of all, remark that the proof of Theorem 2 is linear in PD𝑛(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡), therefore we only need to prove this lemma for (𝑎, 𝑏, 𝑝), for which we proceed as in Theorem 2

$$
1∥𝑔𝑛(𝑋)−𝑔(𝑋) ∥≥𝑑(𝑔(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔(𝑋)∥ 
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓ED𝑛,𝑋
∫∞
 1∥𝑔𝑛(𝑋)−𝑔(𝑋) ∥≥𝑑(𝑔(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔(𝑋)∥≥𝑡 d𝑡
= 2𝑐𝜓 0 PD𝑛,𝑋
∫∞
= 2𝑐𝜓 0 E𝑋PD𝑛(∥𝑔𝑛(𝑋) −𝑔(𝑋)∥≥max {𝑡, 𝑑(𝑔(𝑋), 𝐹)}) d𝑡
∫∞
≤2𝑐𝜓𝑎 0 E𝑋exp (−𝑏max {𝑡, 𝑑(𝑔(𝑋), 𝐹)}𝑝) d𝑡
∫∞
 1𝑑(𝑔(𝑋),𝐹)<𝑡exp (−𝑏𝑡𝑝) 
= 2𝑐𝜓𝑎 0 E𝑋 d𝑡
∫∞
 1𝑑(𝑔(𝑋),𝐹) ≥𝑡exp (−𝑏𝑑(𝑔(𝑋), 𝐹)𝑝) 
+ 2𝑐𝜓𝑎 0 E𝑋 d𝑡
∫∞
= 2𝑐𝜓𝑎 0 P𝑋(𝑑(𝑔(𝑋), 𝐹) < 𝑡) exp (−𝑏𝑡𝑝) d𝑡
+ 2𝑐𝜓𝑎E𝑋[𝑑(𝑔(𝑋), 𝐹) exp (−𝑏𝑑(𝑔(𝑋), 𝐹)𝑝)] .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let us begin by working on the ﬁrst term. We have, using the low-density separation hypothesis

$$
∫∞ −𝑏𝑡2 ∫∞
0 P𝑋(𝑑(𝑔(𝑋), 𝐹) < 𝑡) exp d𝑡≤𝑐𝛼 0 𝑡𝛽exp(−𝑏𝑡𝑝) d𝑡.
∫∞
= 𝑏−1+𝛽 0 (𝑏1/𝑝𝑡)𝛽exp(−(𝑏1/𝑝𝑡)𝑝) d(𝑏1/𝑝𝑡).
𝑝𝑐𝛼
∫∞
= 𝑏−1+𝛽 0 𝑡𝛽exp(−𝑡𝑝) d𝑡= 𝑐𝛼Γ(𝛽, 𝑝)𝑏−1+𝛽
𝑝𝑐𝛼 𝑝.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let study the second term in the excess of risk inequality. To enhance readability, write 𝜂(𝑋) = 𝑑(𝑔(𝑋), 𝐹). We are left with studying E[𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝)]. The function 𝑡→𝑡exp(−𝑏𝑡𝑝) achieves its maximum in 𝑡0 = (𝑝𝑏)−1/𝑝, increasing before and decreasing after. Notice that the quantity

$$
P(𝜂(𝑋) < 𝑡0) E𝑋[𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝) | 𝜂(𝑋) < 𝑡0] ≤𝑐𝛼𝑡𝛽+1 0 exp(−𝑏𝑡𝑝
0 )
= 𝑐𝛼𝑝−𝛽+1 𝑝exp(−𝑝−1/𝑝)𝑏−𝛽+1
𝑝,
$$

is exactly of the same order as the control we had on the ﬁrst term in the excess of risk decomposition. This

<!-- page: 65 -->

5.B. NEAREST NEIGHBORS 63 suggests considering the following decomposition

$$
E𝑋[𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝)] = P(𝜂(𝑋) < 𝑡0) E𝑋[𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝) | 𝜂(𝑋) < 𝑡0]
∞ ∑︁ 2𝑖𝑡0 ≤𝜂(𝑋) < 2𝑖+1𝑡0 
+ P(2𝑖𝑡0 ≤𝜂(𝑋) < 2𝑖+1𝑡0) E𝑋 𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝)
𝑖=0
∞ ∑︁
≤𝑐𝛼𝑡𝛽+1 𝑜 exp(−𝑏𝑡𝑝 𝑐𝛼2𝛽(2𝑖𝑡0)𝛽+1 exp(−𝑏𝑡𝑝
0 ) + 0 (2𝑖)𝑝)
𝑖=0 !
∞ ∑︁
= 𝑐𝛼𝑡𝛽+1 exp(−𝑝−1/𝑝) + 2𝛽2𝑖(𝛽+1) exp(−𝑝−1/𝑝2𝑖𝑝)
𝑜 .
𝑖=0
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The convergence of the last series ensures the existence of a constant 𝑐′ such that

$$
\frac{E𝑋[𝜂(𝑋) exp(−𝑏𝜂(𝑋)𝑝)] ≤𝑐′𝑏−𝛽+1}{𝑝.}
$$

Adding everything together ends the proof of this lemma. Note that we have the same type of optimality as the one stated in Theorem 2. □

$$
ED𝑛𝑔𝑛(𝑥) −𝑔∗(𝑥)
$$

, we can bypass this problem by adding in 1𝑡<𝜀0 in the probability, motivating the study leading to the following lemma.

Because we use concentration inequalities for terms that are not necessarily centered, we usually get that (5.4) only holds for 𝑡> 𝜀0 where, typically 𝜀0 = Lemma 19 (Handling bias in concentration inequality). Under the assumptions of Theorem 2, if the concentration is not given by Assumption 2 but given, for an 𝜀0 > 0, by, for all 𝑥∈supp 𝜌X and 𝑡> 0,

$$
PD𝑛(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡) ≤1𝑡<𝜀0.
$$

Then the excess of risk is controlled by

$$
\frac{ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓𝑐𝛼𝜀𝛼+1}{0} .
$$

Proof. We retake the beginning of the proof of Theorem 2, and change its ending with

$$
1∥𝑔𝑛(𝑋)−𝑔(𝑋) ∥≥𝑑(𝑔(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔(𝑋)∥ 
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓ED𝑛,𝑋
∫∞
 1∥𝑔𝑛(𝑋)−𝑔(𝑋) ∥≥𝑑(𝑔(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔(𝑋)∥≥𝑡 d𝑡
= 2𝑐𝜓 0 PD𝑛,𝑋
∫∞
= 2𝑐𝜓 0 E𝑋PD𝑛(∥𝑔𝑛(𝑋) −𝑔(𝑋)∥≥max {𝑡, 𝑑(𝑔(𝑋), 𝐹)}) d𝑡
∫∞
≤2𝑐𝜓 0 E𝑋1𝑡<𝜀01𝑑(𝑔(𝑋),𝐹)<𝜀0 d𝑡= 2𝑐𝜓𝜀0 P𝑋(𝑑(𝑔(𝑋), 𝐹) < 𝜀0) d𝑡.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This leads to the result after applying the 𝛼-margin condition. □

## 5.B Nearest neighbors 5.B.1 Usual assumptions to derive nearest neighbors convergence rates

$$
𝑔∗
$$

in a uniform manner. This assumption that relates the regularity of 𝑔∗with the density of 𝜌X has been historically approached in the following manner. Assume that 𝑔∗is 𝛽′-Hölder, that is, for any 𝑥, 𝑥′ ∈supp 𝜌X Assumption 6 can be seen as the backbone to control

$$
\frac{𝑛(𝑥) −𝑔∗(𝑥)}{∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥≤𝑎1𝑑(𝑥, 𝑥′)𝛽′.}
$$

Suppose that X = R𝑑, that 𝜌X is continuous against 𝜆, the Lebesgue measure, with minimal mass in the sense that there exists a 𝑝min > 0 such that d𝜌X d𝜆(X) does not intersect (0, 𝑝min), and that supp 𝜌X has regular boundaries in the sense that there exist 𝑎2, 𝑡0 > 0 such that for any 𝑥∈supp 𝜌X and 𝑡∈(0, 𝑡0)

$$
𝜆(B(𝑥, 𝑡) ∩supp 𝜌X ) ≥𝑎2𝜆(B(𝑥, 𝑡)) .
$$

<!-- page: 66 -->

For example an orthant satisﬁes this property with 𝑎2 = 2−𝑑and 𝑡0 = ∞, and B(0, 1) satisﬁes this property with 𝑎2 = 𝜆(B(0, 1) ∩B(1, 1)) /𝜆(B(0, 1)) and 𝑡0 = 1. In such a setting, we get

$$
𝜆(B(𝑥, 𝑑(𝑥, 𝑥′))) 𝛽′
∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥≤𝑎1𝑑(𝑥, 𝑥′)𝛽′ = 𝑎1 𝑑
.
𝜆(B(0, 1))
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

When 𝑑(𝑥, 𝑥′) < 𝑡0, we have

$$
𝜆(B(𝑥, 𝑑(𝑥, 𝑥′))) ≤𝑎−1 2 𝜆(B(𝑥, 𝑑(𝑥, 𝑥′)) ∩supp 𝜌X ) ≤𝑎−1 2 𝑝−1 min𝜌X (B(𝑥, 𝑑(𝑥, 𝑥′)))𝛽.
$$

This means that for any 𝑥∈supp 𝜌X and 𝑥′ ∈B(𝑥, 𝑡0) we have, with 𝛽= 𝛽′ 𝑑and the constant 𝑎3 = 𝑎1𝑎−𝛽

$$
2 𝑝−𝛽 min𝜆(B(0, 1))−𝛽
∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥≤𝑎3𝜌X (B(𝑥, 𝑑(𝑥, 𝑥′)))𝛽.
$$

While, we actually do not need the bound to hold for 𝑑(𝑥, 𝑥′) > 𝑡0 in the following proof, to check the veracity of our remark on Assumption 6, one can verify that under our assumptions on 𝜌X , supp 𝜌X is bounded, and therefore 𝑔∗is too. And if 𝑔∗is bounded by 𝑐𝜑, by considering 𝑎′

$$
3 = max 2𝑐𝜑𝑎−𝛽 2 𝑝−𝛽 \frac{min𝑡−𝛽′}{0} , 𝑎3
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

, this bound holds for any 𝑥, 𝑥′ ∈supp 𝜌X .

$$
0 , 𝑎3
$$

### 5.B.2 Proof of Lemma 12

Control of the variance term. For 𝑥∈𝜌X , the variance term can be written

$$
.
𝑔𝑛(𝑥) −𝑔∗ = 𝑘 ∑︁ 𝑋(𝑖) 
1 𝑘
𝑛(𝑥) 𝜑(𝑌(𝑖)) −E 𝑌(𝑖)
𝑖=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Where the index (𝑖) is such that 𝑋(𝑖) is the 𝑖-th nearest neighbor of 𝑥in (𝑋𝑖)𝑖≤𝑛. Since, given (𝑋𝑖)𝑖≤𝑛, the (𝑌𝑖)𝑖≠𝑛are independent, distributed according to ⊗𝑖≤𝑛𝜌|𝑋𝑖, we can use a concentration inequality to control it. We recall Bernstein concentration inequality in such spaces, derived by Yurinskii (1970), we will use the formulation of Corollary 1 from Pinelis and Sakhanenko (1986).

Theorem 7 (Concentration in Hilbert space (Pinelis and Sakhanenko, 1986)). Let denote by A a Hilbert space and by (𝜉𝑖) a sequence of independent random vectors on A such that E[𝜉𝑖] = 0, and that there exists 𝑀, 𝜎2 > 0 such that for any 𝑚≥2

$$
\sum_{𝑛 𝑖=1} E [∥𝜉𝑖∥𝑚] ≤1 2𝑚!𝜎2𝑀𝑚−2.
$$

Then for any 𝑡> 0

$$
P( \sum_{𝑛 𝑖=1} 𝜉𝑖 ≥𝑡) ≤2 exp − \frac{𝑡2}{2𝜎2 + 2𝑡𝑀} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This explains Assumption 5, allowing, because there is only 𝑘𝜉𝑖active in Í𝑛

$$
𝑖=1 𝛼𝑖(𝑥)𝜉𝑖, to get
 
 

𝑔𝑛(𝑥) −𝑔∗ > 𝑡 ≤2 exp
− 𝑘𝑡2
PD𝑛 𝑛(𝑥) .
2𝜎2 + 2𝑀𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Control of the bias term. Under the Modiﬁed Lipschitz condition, Assumption 6,

$$
≤
𝑔∗ = 𝑛 ∑︁ 𝑛 ∑︁
𝑛(𝑥) −𝑔𝑛(𝑥) 𝛼𝑖(𝑥) (𝑔𝑛(𝑥) −𝑔∗(𝑋𝑖)) 𝛼𝑖(𝑥) ∥𝑔𝑛(𝑥) −𝑔∗(𝑋𝑖)∥
𝑖=1 𝑖=1
𝑛 ∑︁
≤𝑐𝛽 𝛼𝑖(𝑥)𝜌X (B(𝑥, 𝑑(𝑥, 𝑋𝑖)))𝛽≤𝑐𝛽𝜌X (B(𝑥, 𝑑(𝑥, 𝑋𝑘(𝑥))))𝛽.
𝑖=1
$$

<!-- page: 67 -->

5.B. NEAREST NEIGHBORS 65 When 𝜌X is continuous, it follows from the probability integral transform (also known as universality of the uniform) that 𝜌X (B(𝑥, 𝑑(𝑥, 𝑋𝑘(𝑥)))) behaves like the 𝑘-th order statistics of a sample (𝑈𝑖)𝑖≤𝑛of 𝑛uniform distributions on [0, 1]. Therefore, for any 𝑠∈[0, 1]

$$
𝑛 ∑︁ !
PD𝑛(𝜌X (B(𝑥, 𝑑(𝑥, 𝑋𝑘(𝑥)))) > 𝑠) = P 1𝑈𝑖<𝑠≤𝑘 .
𝑖=1
$$

Recall the multiplicative Chernoﬀbound, stating that for (𝑍𝑖)𝑖≤𝑛𝑛independent random variables in {0, 1}, if 𝑍= Í𝑛 𝑖=1 𝑍𝑖, and 𝜇= E[𝑍], for any 𝛿> 0

$$
P (𝑍≤(1 −𝛿)𝜇) ≤exp \frac{−𝛿2𝜇}{2} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Since, for 𝑠∈[0, 1], E[1𝑈𝑖<𝑠] = P(𝑈𝑖< 𝑠) = 𝑠, we get, when 𝑘≤𝑛𝑠/2

$$
𝑛 ∑︁ ! 
 
−(𝑛𝑠−𝑘)2
−𝑛𝑠
P 1𝑈𝑖<𝑠≤𝑘 ≤exp ≤exp .
2𝑛𝑠 8
𝑖=1
1 𝛽, we get
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

With 𝑠= 𝑐−1

$$
𝛽𝑡 !
 

𝑔∗ > 𝑡 ≤exp 1 𝛽
−𝑛𝑡
PD𝑛 𝑛(𝑥) −𝑔𝑛(𝑥) .
8𝑐𝛽
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Remark that when 𝑔∗is 𝛽′ Hölder, we get the same result with 𝜌X (B(𝑥, 𝑡)) instead of 𝑡 1 𝛽by considering 1𝑋𝑖∈B(𝑥,𝑡) instead of 1𝑈𝑖≤𝑡. Note that there is a way to bound a Binomial distribution with a Gaussian for 𝑡 smaller than the mean of the binomial distribution, which would lead to a bound that holds for any 𝑡> 0 (Slud, 1977).

### 5.B.3 Proof of Theorem 3

Using the proof of Theorem 1, we get

$$
𝑔(𝑥) −𝑔∗ > 𝑡0 .
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞PD𝑛 𝑛(𝑥)
𝑔𝑛(𝑥) −𝑔∗ > 𝑡0/2 or 𝑔∗
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

> 𝑡0/2, we get using Lemma 12 Because ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡0 implies that either

$$
𝑛(𝑥) 𝑛(𝑥) −𝑔∗(𝑥)
! 
 

𝑔(𝑥) −𝑔∗ > 𝑡0 ≤2 exp 𝑏1𝑘𝑡2
0 4 + 2𝑏2𝑡0 −2−1 1 𝛽 0
PD𝑛 𝑛(𝑥) − + exp 𝛽𝑏3𝑛𝑡 + 1𝑡0<(𝑘/2𝑛) 𝛽.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This explains the result of Theorem 3.

### 5.B.4 Proof of Theorem 4

$$
𝑔𝑛(𝑥) −𝑔∗
$$

> 𝑡/2 or

$$
𝑔∗
$$

> 𝑡/2, we have the inclusion of events:

First of all for 𝑡> 0, and 𝑥∈supp 𝜌X , because ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡implies that either

$$
𝑛(𝑥)
𝑛(𝑥) −𝑔∗(𝑥)
 𝑔𝑛(𝑥) −𝑔∗ > 𝑡/2
{D𝑛| ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡} ⊂ D𝑛 𝑛(𝑥) ∪{D𝑛| ∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 𝑡/2} ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

which translates in terms of probability as

$$
𝑔𝑛(𝑥) −𝑔∗ > 𝑡 + PD𝑛 

𝑔∗ > 𝑡 .
PD𝑛(∥𝑔𝑛(𝑥) −𝑔∗(𝑥)∥> 2𝑡) ≤PD𝑛 𝑛(𝑥) 𝑛(𝑥) −𝑔∗(𝑥)
 
−𝑏1𝑘𝑡2
≤2 exp + exp 1 𝛽
−𝑏3𝑛𝑡 + 1𝑡<( 𝑘 2𝑛) 𝛽.
1 + 𝑏2𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Using the reﬁnements of Theorem 2 exposed in Appendix 5.A.6, we get that there exists a constant 𝑐> 0 that does not depend on 𝑘or 𝑛such that

$$
2 + 𝑛−𝛽(𝛼+1) + (𝑛𝑘−1)𝛽(𝛼+1) .
ED𝑛R 𝑓𝑛−R( 𝑓∗) ≤𝑐 𝑘−𝛼+1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We optimize this last quantity with respect to 𝑘by taking 𝑘= 𝑛𝛾, and choosing 𝛾such that 𝛾= 2(1 −𝛾)𝛽 leading to 𝛾= 2𝛽/(2𝛽+ 1) and to rates in 𝑛to the power minus 𝛽(𝛼+ 1)/(2𝛽+ 1).

<!-- page: 68 -->

### 5.B.5 Numerical experiments

$$
Empirical convergences
−1 α=0.05 α=0.1 α=0.5 α=1 α=2
−2
$$

Excess of risk (log10) −3 −4 −5 −6

1 2 3 4 5 6 Number of sample (log10)

[FIGURE: Figure 5.4]

Figure 5.4: Supplement to Figure 5.3. We specify the error is evaluated on 100 points forming a regular partition of X = [−1, 1], and the expectation ED𝑛is approximated by considering 100 datasets. The violet curve is cropped at 𝑛≈105, because the error was null afterwards with our evaluation parameters (only 100 points to evaluate the error), forbidding us to consider the logarithm of the excess of risk.

Interestingly, on numerical simulations such as the one presented on Figure 5.3, we observed two regimes. A ﬁrst regime where bound is meaningless because of constants being too big, and where the error decreases independently of the exponent expected through Theorem 4, and a ﬁnal regime where rates correspond to the bond given by the theorem. Note that when 𝛼>> 1, with our computation parameter, we do not get to really illustrate convergence rates, as this ﬁnal regime get place for bigger 𝑛than what we have considered (𝑛max = 106), this being partly due to the constant 𝑐𝛽in Assumption 6 being big for the 𝑔∗we considered. Furthermore, note that, for example, if a problem satisﬁed Assumption 3 with a tiny 𝑡0, we expect that exponential convergence rates are only going to be observed for 𝑛> 𝑁, with 𝑁huge, and for which the excess of risk is already minuscule.

## 5.C Kernel proofs

In this section, we study 𝐿∞convergence rates of the kernel ridge regression estimate. We use the 𝐿2-proof scheme of Caponnetto and De Vito (2006) with the remark of Ciliberto et al. (2016) to factorize the action of 𝐾on 𝐿2(X, H, 𝜌X ) through its action on 𝐿2(X, R, 𝜌X ). We retake the work of Pillaud-Vivien et al. (2018a) to relax the source condition, and use Fischer and Steinwart (2020) to cast in 𝐿∞thanks to interpolation inequality. While those results, leading to Lemma 14, are not new, we present them entirely to provide the reader with self-contained materials.

### 5.C.1 Construction of reproducing kernel Hilbert space (RKHS)

In the following, we suppose that 𝑘is bounded by 𝜅2.

Vector-valued RKHS. To study the estimator 𝑔𝑛, it is useful to introduce the reproducing kernel Hilbert space G associated with 𝑘and H (Aronszajn, 1950). To deﬁne G, deﬁne the atoms 𝑘𝑥: H →G and the scalar product, for 𝑥, 𝑥′ ∈X and 𝜉, 𝜉′ ∈H as

$$
⟨𝑘𝑥𝜉, 𝑘𝑥′𝜉′⟩G = ⟨𝜉, Γ(𝑥, 𝑥′)𝜉′⟩= 𝑘(𝑥, 𝑥′) ⟨𝜉, 𝜉′⟩H .
$$

<!-- page: 69 -->

5.C. KERNEL PROOFS 67 Where Γ is the vector valued kernel inherited from 𝑘as Γ(𝑥, 𝑥′) = 𝑘(𝑥, 𝑥′)𝐼H (Schwartz, 1964). G is deﬁned as the closure, under the metric induced by this scalar product, of the span of the atoms 𝑘𝑥𝜉for 𝑥∈X and 𝜉∈H. Note that 𝑘𝑥is linear, and continuous of norm ∥𝑘𝑥∥op =

$$
√︁
$$

𝑘(𝑥, 𝑥). When 𝑘(·, 𝑥) is square integrable for all 𝑥∈supp 𝜌X , G is homomorphic to a functional space in 𝐿2(X, H, 𝜌X ) through the linear mapping 𝑆 that associates the atom 𝑘𝑥𝜉in G to the function 𝑘(·, 𝑥)𝜉in 𝐿2, deﬁned formally as

$$
𝑆: \frac{G}{𝛾} \frac{→}{→} \frac{𝐿2}{𝑥→𝑘★} 𝑥𝛾.
$$

While intrinsically similar, it is useful to distinguish between G and im 𝑆⊂𝐿2. Note that 𝑆is continuous, since on atom 𝑘𝑥𝜉, ∥𝑆𝑘𝑥𝜉∥𝐿2 ≤∥𝑘𝑥(·)∥𝐿2 ∥𝜉∥H ≤𝑘(𝑥, 𝑥) ∥𝜉∥H = ∥𝑘𝑥𝜉∥G. The fact that 𝑆is a bounded operator justiﬁes the introduction of the following operators.

Central operators. In the following, we will make an extensive use of 𝑆★: 𝐿2(X, H, 𝜌X ) →G the adjoint of 𝑆, deﬁned as 𝑆★𝑔= E𝜌X [𝑘𝑋𝑔(𝑋)]; the covariance operator Σ : G →G, deﬁned as Σ := 𝑆★𝑆= E𝜌X [𝑘𝑋𝑘★ 𝑋]; and its action on 𝐿2, 𝐾: 𝐿2(X, H, 𝜌X ) →𝐿2(X, H, 𝜌X ), deﬁned as 𝐾𝑔:= 𝑆𝑆★𝑔= E𝑋[𝑘(·, 𝑋)𝑔(𝑋)]. Finally, we have deﬁned the four central operators

$$
(·)𝛾, 𝑆★𝑔= E𝜌X [𝑘𝑋𝑔(𝑋)] Σ := 𝑆★𝑆= E𝜌X [𝑘𝑋𝑘★ 𝑆𝛾= 𝑘★
𝑋], 𝐾𝑔:= 𝑆𝑆★𝑔= E𝑋[𝑘(·, 𝑋)𝑔(𝑋)]. (5.13)
$$

(5.13)

It should be noted that this construction is usually avoided since, based on the fact that the Frobenius norm of 𝐾behave like dim(H), meaning that when H is inﬁnite dimensional, 𝐾is not a compact operator. However, since we consider Z ﬁnite, we can always consider H = R|Z | with 𝜑(𝑦) = (ℓ(𝑧, 𝑦)𝑧∈Z and 𝜓(𝑧) = (1𝑧=𝑧′)𝑧′∈Z, and moreover, we will see that a way can be worked out, even when H is inﬁnite dimensional, which was already shown by Ciliberto et al. (2016).

Relation between real-valued versus vector-valued RKHS.

Usually convergence in RKHS is studied for real-valued functions. We need convergence results for vector-valued functions. As mentioned above, we only need the results for Euclidean space, however, we will do it for functions that are maps going into potentially inﬁnite dimensional Hilbert space. Indeed, this does not lead to major complications. We provide here one way to get around this issue. An alternative formal way to proceed can be found (Ciliberto et al., 2016).

Real-valued RKHS. We build the real-valued RKHS GX as the closure of the span of the atoms ¯𝑘𝑥for 𝑥∈X, under the metric induced by the scalar product

$$
¯𝑘𝑥, ¯𝑘𝑥′
$$

= 𝑘(𝑥, 𝑥′). Similarly, we build ¯𝑆, ¯𝑆★, ¯Σ and ¯𝐾. We shall see that the action of Σ on G can be factorized through its actions ¯Σ on GX .

$$
¯𝑘𝑥 GX = ∥𝑘𝑥∥op = √︁
$$

Algebraic equivalences. Based on the fact that 𝑘(𝑥, 𝑥), it is possible to build an isometry that match ¯𝑘𝑥in GX to 𝑘𝑥in the space of continuous linear operator from H to G. With ( ¯𝑒𝑖)𝑖∈N an orthogonal basis of GX , and ( 𝑓𝑗) 𝑗∈N an orthogonal basis of H, we get an orthogonal basis (𝑒𝑖𝑓𝑗)𝑖,𝑗∈N of G. This is exactly the construction G = GX ⊗H of (Ciliberto et al., 2016).

$$
GX = ∥𝑘𝑥∥op =
$$

Note that for 𝜇1, 𝜇2 two measures on X, we can check that

$$
E𝑋∼𝜇1 [𝑘𝑋𝑘★ 2 E𝑋∼𝜇1 [ ¯𝑘𝑋¯𝑘★ 2
𝑋] E𝑋0∼𝜇2 [𝑘𝑋0] 𝑋] E𝑋0∼𝜇2 [ ¯𝑘𝑋0]
op =
GX = E𝑋,𝑋′∼𝜇1;𝑋,𝑋′∼𝜇2 [𝑘(𝑋0, 𝑋)𝑘(𝑋, 𝑋′)𝑘(𝑋′, 𝑋′
0)].
$$

This explains that we will allow ourselves to write derivations of the type

$$
(Σ + 𝜆)−1 ( ¯Σ + 𝜆)−1
2 𝑘𝑥𝑔𝑛(𝑥) 2 ¯𝑘𝑥
G ≤ GX ∥𝑔𝑛(𝑥)∥H .
$$

Note also that for 𝑔:= Í

$$
𝑖𝑗𝑐𝑖𝑗𝑒𝑖𝑓𝑗∈G, with Í
$$

𝑖𝑗= 1, ¯𝑐𝑖:= (𝑐𝑖𝑗) 𝑗∈N ∈ℓ2, ¯𝐴a self-adjoint operator on

$$
𝑖𝑗𝑐2
$$

<!-- page: 70 -->

GX and 𝐴its version on G, we have

$$
∑︁ ¯𝐴¯𝑒𝑖, ¯𝐴¯𝑒𝑘 ∑︁ ¯𝐴¯𝑒𝑖, ¯𝐴¯𝑒𝑘
∥𝐴𝑔∥2 G = G = ¯𝑐𝑖, ¯𝑐𝑗
𝑐𝑖𝑗𝑐𝑘𝑗 ℓ2
GX
𝑖𝑗𝑘 𝑖𝑗
∑︁ ¯𝑐𝑗 ¯𝐴¯𝑒𝑖, ¯𝐴¯𝑒𝑘 ∑︁ 2 ¯𝐴 2
∥¯𝑐𝑖∥ℓ2 ¯𝐴 ∥¯𝑐𝑖∥ℓ2 ¯𝑒𝑖
≤ GX = ≤ op ,
ℓ2
𝑖𝑗 𝑖 GX
$$

which explains why we will consider derivations of the type

$$
(Σ + 𝜆) ( ¯Σ + 𝜆)
1 2 ( ˆΣ + 𝜆)−1(Σ + 𝜆) 1 2 1 2 ( ˆ¯Σ + 𝜆)−1( ¯Σ + 𝜆) 1 2
op ≤ op .
$$

X diagonalize ¯𝐴, (𝑢𝑖𝑓𝑗)𝑖,𝑗≤N ∈GN×N ≃ GN diagonalize 𝐴in G. This justiﬁes the consideration of fractional operators 𝐴𝑝for 𝑝∈R+, such as in Assumptions 8 and 9. Based on this equivalence, we will forget the bar notations, we incite the careful and attentive reader to recover them.

Finally, notice that because of the same consideration, if ( ¯𝑢𝑖)𝑖∈N ∈GN Estimate 𝑔𝑛as an empirical approximate projection on RKHS

### 5.C.2

To obtain bounds like (5.4), it is suﬃcient to control the convergence of 𝑔𝑛to 𝑔∗in 𝐿∞. Assumption 8 allow us to cast in 𝐿2 the study of the convergence in 𝐿∞. The convergence of 𝑔𝑛toward 𝑔∗can be split in two terms, a term expressing the convergence of 𝑔𝜆toward 𝑔∗that is based on geometrical properties and a term expressing the convergence of 𝑔𝑛toward 𝑔𝜆, that is based on concentration inequalities in G, such as the ones given by Pinelis and Sakhanenko (1986); Minsker (2017). For this last term, we need to characterize 𝑔𝑛and 𝑔𝜆with the following lemma.

Lemma 20 (Approximation of integral operators). 𝑔𝑛can be understood as the empirical approximation of 𝑔𝜆since

$$
𝑋] + 𝜆)−1 E ˆ𝜌[𝑘𝑋𝜑(𝑌)], 𝑔𝜆= 𝑆(E𝜌[𝑘𝑋𝑘★ 𝑋] + 𝜆)−1 E𝜌[𝑘𝑋𝜑(𝑌)],
𝑔𝑛= 𝑆(E ˆ𝜌[𝑘𝑋𝑘★
Í𝑛
$$

with ˆ𝜌= 1

$$
𝑛 𝑖=1 𝛿𝑋𝑖⊗𝛿𝑌𝑖,
$$

Proof. Indeed, the expression of 𝑔𝑛and its convergences toward 𝑔∗will be understood thanks to the operator 𝑆and its derivatives. When im 𝑆is closed in 𝐿2, on can be deﬁned the orthogonal projection of 𝑔∗to im 𝑆, with the 𝐿2 metric as 𝜋im 𝑆(𝑔∗) = 𝑆(𝑆★𝑆)†𝑆★𝑔∗. When im 𝑆is not closed, or equivalently when Σ has positive eigenvalues converging to zero, one can deﬁne approximate orthogonal projection, through eigenvalue thresholding or Tikhonov regularization. This last choice leads to the estimate

$$
𝑔𝜆= 𝑆(Σ + 𝜆)−1𝑆★𝑔∗= 𝑆(𝑆★𝑆+ 𝜆)−1𝑆★𝑔∗= 𝑆𝑆★(𝑆𝑆★+ 𝜆)−1𝑔∗= 𝐾(𝐾+ 𝜆)−1𝑔∗.
$$

Note that, because of the Bayes optimum characterization of 𝑔∗, 𝑆★𝑔∗= E𝜌[𝑘𝑋𝜑(𝑌)]. This explains the characterization of 𝑔𝜆.

Interestingly, the approximation of 𝜌by ˆ𝜌can be thought with the approximation of 𝐿2(X, H, 𝜌X ) by ℓ2(H𝑛) ≃𝐿2(X, H, ˆ𝜌X ) where for Ξ = (𝜉𝑖), 𝑍= (𝜁𝑖) ∈H𝑛,

$$
⟨Ξ, 𝑍⟩ℓ2 = 1 𝑛 Í𝑛 𝑛 \sum_{𝑛 𝑖=1} ⟨𝜉𝑖, 𝜁𝑖⟩H ,
$$

and with the empirical probability measure ˆ𝜌= 1 𝑖=1 𝛿𝑥𝑖⊗𝛿𝑦𝑖. We redeﬁne the natural homomorphism of G into ℓ2 with

$$
ˆ𝑆: \frac{G}{𝛾} 𝑛 \frac{→}{→} 𝑘★ \frac{ℓ2}{𝑥𝑖𝛾 } 𝑖≤𝑛.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We check that its adjoint is, for Ξ ∈H𝑛and 𝛾∈G

$$
* 1 𝑛 +
ˆ𝑆★Ξ, 𝛾 𝑛 ∑︁ 𝑛 ∑︁
ℓ2 = 1
Ξ, ˆ𝑆𝛾 𝜉𝑖, 𝑘★
G = 𝑥𝑖𝛾 H = 𝑘𝑥𝑖𝜉𝑖, 𝛾 .
𝑛
𝑖=1 𝑖=1 G
$$

<!-- page: 71 -->

5.C. KERNEL PROOFS 69 Similarly, we deﬁne ˆ𝐾: H𝑛→H𝑛and ˆΣ : G →G, with

$$
!
𝑛 ∑︁ 𝑛 ∑︁
1 𝑛 , ˆΣ = 1
ˆ𝐾Ξ = ˆ𝑆ˆ𝑆★Ξ = 𝑘𝑥𝑖⊗𝑘𝑥𝑖= E ˆ𝜌X [𝑘𝑋𝑘★
𝑘(𝑥𝑗, 𝑥𝑖)𝜉𝑖 𝑋].
𝑛
𝑖=1 𝑗≤𝑛 𝑖=1
$$

Finally, we deﬁne ˆΦ = (𝜑(𝑦)𝑖)𝑖≤𝑛∈H𝑛, so that

$$
\frac{ }{𝑆★𝑔∗:= E ˆ𝜌[𝜑(𝑌) · 𝑘𝑋] = ˆ𝑆★ˆΦ.}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Finally, we can express 𝑔𝑛as

$$
𝑔𝑛= 𝑆( ˆΣ + 𝜆)−1 ˆ𝑆★ˆΦ = 𝑆( ˆ𝑆★ˆ𝑆+ 𝜆)−1 ˆ𝑆★ˆΦ = 𝑆ˆ𝑆★( ˆ𝑆ˆ𝑆★+ 𝜆)−1 ˆΦ = 𝑆ˆ𝑆★( ˆ𝐾+ 𝜆)−1 ˆΦ.
$$

This explains the equivalence between 𝑔𝑛deﬁned at the beginning of Section 5.5 and the 𝑔𝑛expressed in the lemma, that will be used for derivations of theorems. □

### 5.C.3 Linear algebra and equivalent assumptions to Assumptions 7, 8

To proceed with the study of the convergence of 𝑔𝑛toward 𝑔𝜆in 𝐿2, it is helpful to pass by G. To do so, we need to express Assumptions 7 and 8 in G, which we can do using the following linear algebra property.

Lemma 21 (Linear algebra on compact operators). There exist (𝑢𝑖)𝑖∈N an orthogonal basis of GX , (𝑣𝑖)𝑖∈N an orthogonal basis of 𝐿2(X, R, 𝜌X ), and (𝜆𝑖)𝑖∈N a decreasing sequence of positive real number such that

$$
∑︁ ∑︁ ∑︁ ∑︁
𝑆= 𝜆1/2 𝑖 𝑢𝑖𝑣★ 𝑖, 𝑆★= 𝜆1/2 𝑖 𝑣𝑖𝑢★ 𝑖, Σ = 𝜆𝑖𝑢𝑖𝑢★ 𝑖, 𝐾= 𝜆𝑖𝑣𝑖𝑣★ 𝑖, (5.14)
𝑖∈N 𝑖∈N 𝑖∈N 𝑖∈N
$$

(5.14)

where the convergence of series has to be understood with the operator norms. Moreover, we have that, if the kernel 𝑘is bounded by 𝜅2, ∑︁

$$
𝑖∈N 𝜆𝑖≤𝜅2 < +∞.
$$

Therefore, 𝐾and Σ are trace-class, and 𝑆and 𝑆★are Hilbert-Schmidt.

Proof. Notice that Σ = E𝑋[𝑘𝑋⊗𝑘𝑋] and that ∥𝑘𝑥⊗𝑘𝑥∥op(GX ) = ∥𝑘𝑥∥GX = 𝑘(𝑥, 𝑥) ≤𝜅2. Therefore, Σ is a nuclear operator, so it is trace class and so it is compact.

The ﬁrst point results from diagonalization of kernel operators, known as Mercer’s Theorem (Mercer, 1909; Steinwart and Scovel, 2012). Σ is a compact operator, therefore, the Spectral Theorem gives the existence of a sequence (𝜆𝑖) ∈RN and an orthonormal basis (𝑢𝑖) ∈GN

$$
Σ = \sum_{𝑖∈N} \frac{𝜆𝑖𝑢𝑖𝑢★}{𝑖,} X of GX such that
$$

where the convergence has to be understood with the operator norm. Because Σ is of the form 𝑆★𝑆, one can consider (𝜆𝑖) a decreasing sequence of positive eigenvalues. Then, by deﬁning, for all 𝑖∈N with 𝜆𝑖> 0,

$$
\frac{𝑣𝑖= 𝜆−1/2}{𝑖} 𝑆𝑢𝑖
$$

we check that (𝑣𝑖) are orthonormal, and we complete them to form an orthonormal basis of (𝐿2(X, R, 𝜌X )). Finally, we check that

$$
𝑆= \sum_{𝑖∈N} \frac{𝜆1/2}{𝑖} \frac{𝑣𝑖𝑢★}{𝑖,}
$$

and that the other equalities hold too.

To check the second assertion, we use that 𝑘𝑥𝑘★ 𝑥is rank one when operating on GX and therefore

$$
Tr Σ = Tr E𝑋[𝑘𝑋𝑘★ 𝑋] = E𝑋 Tr 𝑘𝑋𝑘★ h

𝑘𝑋𝑘★ i
= E𝑋
 𝑋 𝑋 op(GX )
= E𝑋 ∥𝑘𝑋∥GX = E𝑋[𝑘(𝑥, 𝑥)] ≤𝜅2.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This shows that 𝑆and 𝑆★are Hilbert-Schmidt operators and that 𝐾is also trace class. □

<!-- page: 72 -->

This allows us to cast in GX the assumptions expressed in 𝐿2.

Lemma 22 (Equivalence of capacity condition). For 𝜎∈(0, 1], it is equivalent to suppose that

$$
• Tr𝐿2(X,H,𝜌X ) (𝐾𝜎) < +∞. • TrGX (Σ𝜎) < +∞. • Í 𝑖∈N 𝜆𝜎 𝑖< +∞.
$$

In Assumption 7, the smaller 𝜎, the faster the 𝜆𝑖decreases, the easier it will be to approximate Σ based on approximation of 𝜌. This appears explicitly in Theorem 8. Indeed, for 𝜎= 0, the condition should be deﬁned as Σ of ﬁnite rank. Note that when 𝑘is bounded, we know that Σ is trace class, and therefore, Assumption 7 holds with 𝜎= 1.

Lemma 23 (Interpolation inequality in RKHS). Assumption 8 implies that

$$
Σ
1 2 −𝑝𝛾 G . (5.15)
∀𝛾∈G, ∥𝑆𝛾∥𝐿∞≤𝑐𝑝
$$

(5.15)

Proof. We begin by showing the property for 𝛾∈GX . When 𝛾= Í

$$
𝑖∈N 𝑐𝑖𝑣𝑖with Í 𝑖∈N 𝑐2 𝑖< +∞, denote
$$

𝑔= Í 1 2 −𝑝 𝑖 𝑐𝑖𝑢𝑖, we have 𝑔∈𝐿2, therefore, using Assumption 8,

$$
𝑖∈N 𝜆
Σ
∥𝑆𝛾∥𝐿∞= ∥𝐾𝑝𝑔∥𝐿∞≤𝑐𝑝∥𝑔∥𝐿2 = 𝑐𝑝 1 2 −𝑝𝛾
GX .
$$

This ends the proof for GX . Note also that when the result of the Lemma holds, then Assumption 8 holds for any 𝑔∈im𝐿2(X,R,𝜌X ) 𝐾 1 2 −𝑝. Let us switch to G now. Let 𝛾∈G, and denote 𝑔= 𝑆𝛾. Suppose that 𝑔achieve it maximum in 𝑥∞, deﬁne the direction 𝜉= 𝑔(𝑥∞)/∥𝑔(𝑥∞) ∥H, and deﬁne 𝑔𝜉: 𝑥→⟨𝑔(𝑥), 𝜉⟩H ∈𝐿2(X, R, 𝜌X ), and 𝛾𝜉= Í

$$
𝑔𝜉, 𝑣𝑖 𝐿2 𝑢𝑖∈GX . We have
𝑗∈N
𝑆𝛾𝜉 Σ Σ
1 2 −𝑝𝛾𝜉 1 2 −𝑝𝛾
∥𝑆𝛾∥𝐿∞= 𝐿∞≤𝑐𝑝 GX ≤𝑐𝑝 G .
$$

When 𝑔does not achieve its maximum, one can do a similar reasoning by considering a basis ( 𝑓𝑖)𝑖∈N of H and decomposition 𝛾on the basis (𝑢𝑖𝑓𝑗)𝑖,𝑗∈N, before summing the directions. □ In Assumption 8, the bigger 1/2 −𝑝the more we are able to control our problem in G, the better. Note that this reformulation of the interpolation inequality allows generalizing it for 𝑝smaller than zero. Note that when 𝑘is bounded, ∥(𝑆𝛾)(𝑥)∥H =

$$
\frac{𝑘★}{𝑋𝛾} H ≤∥𝑘𝑋∥op ∥𝛾∥G = √︁
$$

𝑘(𝑥, 𝑥) ∥𝛾∥G , hence Assumption 8 holds with 𝑝= 1/2.

$$
𝑋𝛾 H ≤∥𝑘𝑋∥op ∥𝛾∥G =
$$

Linear algebra with atoms 𝑘𝑥and useful inequalities

### 5.C.4

From the study of the convergence of 𝑔𝑛to 𝑔𝜆will emerge two quantities linked to eigenvalues of Σ and the position of 𝑘𝑥regarding eigenspaces, that are

$$
(Σ + 𝜆)−1
N (𝜆) = Tr (Σ + 𝜆)−1Σ , N∞(𝜆) = sup 𝑥∈supp 𝜌X 2 𝑘𝑥 op . (5.16)
$$

(5.16)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

While those quantities could be bounded with brute force consideration, Assumptions 7 and 8 will help to control them more subtly.

Proposition 24 (Characterization of capacity condition). The property Í

$$
𝑖∈N 𝜆𝜎
$$

𝑖< +∞, can be rephrased in terms of eigenvalues of Σ as the existence of 𝑎1 > 0 such that, for all 𝑖> 0,

$$
𝜆𝑖≤𝑎1(𝑖+ 1)−1 𝜎. (5.17)
𝑖and Í𝑛
$$

(5.17)

Proof. Denote by 𝑢𝑖and 𝑆𝑛the respective quantities 𝜆𝜎 𝑖=1 𝑢𝑖. Because 𝑆𝑛converge, it is a Cauchy sequence, so there exists 𝑁such that for any 𝑝> 𝑞> 𝑁, 𝑆𝑝−𝑆𝑞= Í𝑝

$$
𝑖=𝑞+1 𝑢𝑖≤1. In particular, considering
$$

𝑝= 2𝑞, and because (𝜆𝑖) is decreasing, we have 𝑞𝑢2𝑞≤Í2𝑞 𝑖=𝑞+1 𝑢𝑖≤1. Therefore, we have that for all 𝑖> 2𝑁, 𝑢𝑖≤3(𝑖+ 1)−1, considering (𝑎1)𝜎= 3 + max𝑖≤2𝑁{(𝑖+ 1)𝑢𝑖}, we get the desired result. □

<!-- page: 73 -->

5.C. KERNEL PROOFS 71 \int_{0}

Proposition 25 (Characterization of N). When Tr (𝐾𝜎) < +∞, with 𝑎2 =

$$
0 𝑎1 𝑎1+𝑡 1𝜎d𝑡,
∀𝜆> 0, N (𝜆, 𝑟) ≤𝑎2𝜆−𝜎. (5.18)
$$

(5.18)

Proof. Expressed with eigenvalues, we have

$$
N (𝜆) = Tr (Σ + 𝜆)−1Σ = \sum_{𝑖∈N} \frac{𝜆𝑖}{𝜆𝑖+ 𝜆.}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Using that 𝜆𝑖≤𝑎1(𝑖+ 1)−1 𝜎, that 𝑥→ 𝑥 𝑥+𝑎is increasing with respect to 𝑥for any 𝑎> 0 and the series-integral comparison, we get for 𝜎∈(0, 1]

$$
∑︁ ∫∞ ∫∞
𝑎1(𝑖+ 1)−1 𝑎1𝑡−1
𝜎 𝑎1(𝑖+ 1)−𝜎+ 𝜆≤ 𝜎 𝑎1 𝑎1 + 𝜆𝑡
N (𝜆) ≤ d𝑡= d𝑡
0 𝑎1𝑡−1 𝜎+ 𝜆 0 1 𝜎
𝑖∈N ∫∞
𝑎1 𝑎1 + (𝜆𝜎𝑡)
= 𝜆−𝜎 d(𝜆𝜎𝑡) = 𝑎2𝜆−𝜎,
0 1 𝜎
$$

where we check the convergence of the integral. □ Indeed, Assumption 8 has a profound linear algebra meaning, it is a condition on 𝜌X -almost all the vector 𝑘𝑥∈GX not to be excessively supported on the eigenvector corresponding to small eigenvalue of Σ.

Proposition 26 (Characterization of interpolation condition). The interpolation Assumption 8 implies that, for all 𝑖∈N

$$
⟨𝑘𝑥, 𝑢𝑖⟩GX ≤𝑐𝑝𝜆
1 2 −𝑝 𝑖 . (5.19)
sup 𝑥∈𝜌X
$$

(5.19)

Proof. Consider the decomposition of 𝑘𝑥∈GX according to the eigenvectors of Σ, with 𝑎𝑖(𝑥) = ⟨𝑘𝑥, 𝑢𝑖⟩. The interpolation condition Assumption 8, expressed in GX with Lemma 23, leads to for any 𝛾X ∈GX , and 𝑆𝛾X : X →R,

$$
⟨𝑘𝑥, 𝛾X ⟩GX ≤∥𝑆𝛾X ∥𝐿∞≤𝑐𝑝 Σ
1 2 −𝑝𝛾X
|(𝑆𝛾X )(𝑥)| =
GX
$$

This implies that

$$
∑︁ !2
Σ ∑︁
1 2 −𝑝𝛾X 2 𝜆1−2𝑝
⟨𝑘𝑥, 𝛾X ⟩2 GX = ⟨𝑘𝑥, 𝑢𝑖⟩⟨𝛾X , 𝑢𝑖⟩ ≤𝑐2 GX = 𝑐2 𝑖 ⟨𝛾X , 𝑢𝑖⟩2 .
𝑝 𝑝
𝑖∈N 𝑖∈N
$$

Taking 𝛾X = 𝑢𝑖, we get that

$$
|⟨𝑘𝑥, 𝑢𝑖⟩| ≤𝑐𝑝𝜆 𝑖 \frac{1}{2 −𝑝} .
$$

This result relates the interpolation condition to the fact that 𝑘𝑥is not excessively supported on the eigenvectors corresponding to vanishing eigenvalues of Σ. □ Proposition 27 (Characterization of N∞(𝜆, 𝑟)). Under the interpolation condition, Assumption 8, we have with 𝑎3 = 𝑐𝑝(2𝑝)−𝑝(1 −2𝑝)

$$
1 2 −𝑝, or 𝑎3 = 𝑐𝑝when 𝑝= 1/2,
N∞(𝜆) ≤𝑎3𝜆−𝑝. (5.20)
$$

(5.20)

Proof. First of all, notice that

$$
(Σ + 𝜆)−1 D 2 𝑘𝑥 E ∑︁
𝛾X , (Σ + 𝜆)−1 𝑐𝑖⟨𝑘𝑥, 𝑢𝑖⟩
2 𝑘𝑥 GX = sup ∥𝛾X ∥X =1 = sup 𝑐;Í
GX (𝜆+ 𝜆𝑖) 1 2
𝑖∈N 𝑐2 𝑖=1 𝑖∈N
∑︁ 1 2 −𝑝 𝑖 (𝜆+ 𝜆𝑖)
𝑐𝑖𝜆 1 2 −𝑝
𝑡
≤𝑐𝑝 sup 𝑐;Í 1 2 ≤sup 𝑐𝑝 1 2 .
𝑖∈N𝑐2 𝑖∈N 𝑡∈R+ (𝜆+ 𝑡)
𝑖=1
$$

<!-- page: 74 -->

When 𝑝∈(0, 1/2), this last function is zero in zero and in inﬁnity, therefore its maximum 𝑡0 veriﬁes, taking the derivative of its logarithm,

$$
1/2 −𝑝 𝑡0 = 1 2(𝑡0 + 𝜆) ⇒ 𝑡0 = (1 −2𝑝)𝜆 1 2 −𝑝
𝑡 1 2 −𝑝𝜆−𝑝.
2𝑝 ⇒ sup 𝑡∈R+ 1 2 = (2𝑝)−𝑝(1 −2𝑝)
(𝜆+ 𝑡)
$$

The cases 𝑝∈{0, 1} are easy to treat. □ In the previous analysis, one fact does not appear, it is that Σ and 𝑘𝑥are linked to one another, since Σ = E𝑋[𝑘𝑋𝑘★ 𝑋]. The following remark builds on it to relate N and N∞.

Remark 28 (Relation between interpolation and capacity condition). The capacity and interpolation condition are related by the fact that it is unreasonable not to consider that 𝑝≤𝜎/2.

Proof. Because 𝑘𝑥𝑘★ 𝑥is of rank one in GX , we have

$$
h i h i
N (𝜆) = Tr (Σ + 𝜆)−1Σ = E𝑋 Tr (Σ + 𝜆)−1𝑘𝑋𝑘★ = E𝑋 Tr 𝑘★ 𝑋(Σ + 𝜆)−1𝑘𝑋
h

𝑘★ i 


(Σ + 𝜆)−1 𝑋 
2
= E𝑋 𝑋(Σ + 𝜆)−1𝑘𝑋 = E𝑋 2 𝑘𝑋 .
op
GX
(Σ + 𝜆)−1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

So indeed, N (𝜆) is the expectation of the square GX , when N∞(𝜆) is the supremum of this

$$
2 𝑘𝑋
$$

last quantity. Therefore,

$$
N (𝜆) ≤N∞(𝜆)2
$$

Supposing that the dependencies in 𝜆proved above are tight, we should have 𝜎≥2𝑝, which is the statement of this remark. We refer the reader to Lemma 6.2 of Fischer and Steinwart (2020) for more consideration to relates 𝜎and 𝑝(reading 𝑝and 𝛼/2 with their notations) □ Geometrical control of the residual ∥𝑔𝜆−𝑔∗∥𝐿∞

### 5.C.5

The proof of the ﬁrst assertion in Lemma 14 follows from, using Assumption 9, with 𝑔0 ∈𝐾−𝑞𝑔∗,

$$
𝑔𝜆−𝑔∗= (𝐾(𝐾+ 𝜆)−1 −𝐼)𝑔∗= −𝜆(𝐾+ 𝜆)−1𝑔∗= −𝜆(𝐾+ 𝜆)−1𝐾𝑞𝑔0
= −𝜆𝐾𝑝(𝐾+ 𝜆)−1𝐾𝑞−𝑝𝑔0.
$$

Then using Assumption 8,

$$
𝐾𝑞−𝑝(𝐾+ 𝜆)−1
∥𝑔∗−𝑔𝜆∥∞≤𝑐𝑝𝜆 op ∥𝑔0∥𝐿2
𝐾(𝐾+ 𝜆)−1

𝑞−𝑝 (𝐾+ 𝜆)−1

1+𝑝−𝑞
≤𝑐𝑝𝜆 op ∥𝑔0∥𝐿2
op
≤𝑐𝑝𝜆1𝑞−𝑝𝜆−(1+𝑝−𝑞) ∥𝑔0∥𝐿2 = 𝑏1𝜆𝑞−𝑝,
𝐾(𝐾+ 𝜆)−1 (𝐾+ 𝜆)−1

 ≤𝜆−1.
$$

where we have used that

$$
op = ∥𝐾∥op/( ∥𝐾∥op + 𝜆) ≤1 and that
$$

Convergence of ∥𝑔𝑛−𝑔𝜆∥through concentration inequality

### 5.C.6

For the proof of the second assertion in Lemma 14, we will put ourselves in G. For this, we deﬁne in G

$$
𝛾= E𝜌[𝑘𝑋𝜑(𝑌)], 𝛾𝜆= (Σ + 𝜆)−1𝛾, ˆ𝛾= E ˆ𝜌[𝑘𝑋𝜑(𝑌)], (5.21)
$$

(5.21)

so that 𝑔𝜆= 𝑆𝛾𝜆, and 𝑔𝑛= 𝑆( ˆΣ + 𝜆)−1 ˆ𝛾.

<!-- page: 75 -->

5.C. KERNEL PROOFS 73 Decomposition into a matrix and a vector term We begin by expressing 𝑔𝑛−𝑔𝜆in G with

$$
( ˆΣ + 𝜆)−1 ˆ𝛾−(Σ + 𝜆)−1𝛾
𝑔𝑛−𝑔𝜆= 𝑆
 
= 𝑆 ( ˆΣ + 𝜆)−1( ˆ𝛾−𝛾) + (( ˆΣ + 𝜆)−1 −(Σ + 𝜆)−1)𝛾)
 
= 𝑆 ( ˆΣ + 𝜆)−1( ˆ𝛾−𝛾) + ( ˆΣ + 𝜆)−1(Σ −ˆΣ)(Σ + 𝜆)−1𝛾)
 
= 𝑆 ( ˆΣ + 𝜆)−1(( ˆ𝛾−ˆΣ𝛾𝜆) −(𝛾−Σ𝛾𝜆))
,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where we have used that 𝐴−1 −𝐵−1 = 𝐴−1(𝐵−𝐴)𝐵−1. Therefore, using the expression, Lemma 23, of Assumption 8 in G, we get

$$
Σ 1 2 −𝑝( ˆΣ + 𝜆)−1(Σ + 𝜆) 1 2 +𝑝 op × · · · (Σ + 𝜆)−( 1
∥𝑔𝑛−𝑔𝜆∥𝐿∞≤𝑐𝑝
2 +𝑝) (( ˆ𝛾−ˆΣ𝛾𝜆) −(𝛾−Σ𝛾𝜆))
G .
$$

1 2 −𝑝(Σ + 𝜆)−( 1 2 −𝑝) ⪯𝐼. On the other hand, we have concentration of the vector ˆ𝛾−ˆΣ𝛾𝜆toward 𝛾−Σ𝛾𝜆. Indeed, the concentration of the matrix term is hard to prove (it is only a conjecture), therefore we will go for another decomposition, that will result in similar rates when 𝑝≥0, that is On the one hand, we have concentration of matrix term toward Σ

$$
Σ
1 2 −𝑝(Σ + 𝜆)−1 2
∥𝑔𝑛−𝑔𝜆∥𝐿∞≤𝑐𝑝 op A(𝜆)B(𝜆)
(Σ + 𝜆)
1 2 ( ˆΣ + 𝜆)−1(Σ + 𝜆) 1 2 (5.22)
A(𝜆) = op ,
(Σ + 𝜆)−1
B(𝜆) = 2 (( ˆ𝛾−ˆΣ𝛾𝜆) −(𝛾−Σ𝛾𝜆))
G .
$$

(5.22)

Recall the deﬁnition of the following important quantity that are going to pop up from the analysis

$$
(Σ + 𝜆)−1
N (𝜆) = Tr (Σ + 𝜆)−1Σ , N∞(𝜆) = sup 𝑥∈supp 𝜌X 2 𝑘𝑥 op . (5.16)
$$

(5.16)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Extra matrix term We control the extra matrix term with Σ

$$
Σ
1 2 −𝑝(Σ + 𝜆)−1 2 1 2 −𝑝(Σ + 𝜆)−( 1 2 −𝑝) op ∥(Σ + 𝜆)−𝑝∥op ≤𝜆−𝑝.
op =
(Σ + 𝜆)−1 (Σ + 𝜆)−1Σ
op ≤𝜆−1 and that op ≤∥Σ∥op/( ∥Σ∥op + 𝜆) ≤1.
$$

Using that Matrix concentration Let us make explicit the concentration in the matrix term with

$$
1 2 ( ˆΣ + 𝜆)−1(Σ + 𝜆) 1 2 = 𝐼+ (Σ + 𝜆) 1 2 ( ˆΣ + 𝜆)−1 −(Σ + 𝜆)−1 
1 2
(Σ + 𝜆) (Σ + 𝜆)
1 2 ( ˆΣ + 𝜆)−1 Σ −ˆΣ 
(Σ + 𝜆)−1(Σ + 𝜆) 1 2 .
= 𝐼+ (Σ + 𝜆)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

From here, notice the following implications (that are actually equivalence)

$$
Σ −ˆΣ ⪯𝑡(Σ + 𝜆) ⇒ ˆΣ + 𝜆⪰(1 −𝑡)(Σ + 𝜆)
⇒ ( ˆΣ + 𝜆)−1 ⪯(1 −𝑡)−1(Σ + 𝜆)−1.
⇒ ( ˆΣ + 𝜆)−1 −(Σ + 𝜆)−1 ⪯𝑡(1 −𝑡)−1(Σ + 𝜆)−1.
1 2 ( ˆΣ + 𝜆)−1 −(Σ + 𝜆)−1 
1 2 ⪯𝑡(1 −𝑡)−1
⇒ (Σ + 𝜆) (Σ + 𝜆)
1 2 ( ˆΣ + 𝜆)−1(Σ + 𝜆) 1 2 ⪯(1 −𝑡)−1.
⇒ (Σ + 𝜆)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 76 -->

The probability of the event Σ −ˆΣ ⪯𝑡(Σ + 𝜆), can be studied through the probability of the event 2 (Σ −ˆΣ)(Σ +𝜆)−1 2 ⪯𝑡, which can be studied through concentration of self adjoint operators. Finally, we have shown that (Σ +𝜆)−1

$$
(Σ + 𝜆)−1
op ≤𝑡 ⇒ A(𝜆) ≤ 1 1 −𝑡. (5.23)
2 (Σ −ˆΣ)(Σ + 𝜆)−1 2
$$

(5.23)

The best result that we are aware of, for covariance matrix inequality, is the extension to self-adjoint Hilbert-Schmidt operators provided by Minsker (2017) in Section 3.2 of its concentration inequality on random matrices Theorem 3.1. It can be formulated as the following.

Theorem 8 (Concentration of self-adjoint operators (Minsker, 2017)). Let denote by (𝜉𝑖)𝑖≤𝑛a sequence of independent self-adjoint operator acting on a separable Hilbert space A, such that ker(E[𝜉𝑖]) = A, that are bounded by a constant 𝑀∈R, in the sense ∥𝜉𝑖∥op ≤𝑀, with ﬁnite variance 𝜎2 =

$$
E Í𝑛 \frac{𝑖=1 𝜉2}{𝑖}
$$

op. For any 𝑡> 0 such that 6𝑡2 ≥(𝜎2 + 𝑀𝑡/3),

$$
𝑖
𝑛 ∑︁ ! 
𝑛 ∑︁
P ©­ > 𝑡ª® − 𝑡2
𝜉𝑖 ≤14 𝑟 E 𝜉2 exp ,
𝑖 2𝜎2 + 2𝑡𝑀/3
« 𝑖=1 ¬ 𝑖=1
op
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑟(𝜉) = Tr 𝜉/∥𝜉∥op.

Let us deﬁne 𝜉that goes from X to the space of self-adjoint operator action on GX as

$$
𝜉(𝑥) = (Σ + 𝜆)−1 2 𝑘𝑥𝑘★ 𝑥(Σ + 𝜆)−1 2 . (5.24)
Í𝑛
2 (Σ −ˆΣ)(Σ + 𝜆)−1 2 = E𝜌[𝜉(𝑋)] −1 𝑛
$$

(5.24)

We have that (Σ + 𝜆)−1 𝑖=1 𝜉(𝑥𝑖). To apply operator concentration, we need to bound 𝜉and its variance.

Bound on 𝜉. To bound 𝜉we proceed with, because 𝑘𝑥𝑘★

$$
𝑥is of rank one,
(Σ + 𝜆)−1 2 
2 𝑘𝑥𝑘★ 𝑥(Σ + 𝜆)−1 op = Tr (Σ + 𝜆)−1 2 𝑘𝑥𝑘★ 𝑥(Σ + 𝜆)−1
∥𝜉(𝑥)∥op = 2
 (Σ + 𝜆)−1
2
= Tr 𝑘★ 𝑥(Σ + 𝜆)−1𝑘𝑥 = 2 𝑘𝑥 GX ≤N∞(𝜆)2.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Variance of 𝜉. For the variance of 𝜉we proceed by noticing that

$$
2 = (Σ + 𝜆)−1 2 E𝑋 
E 𝜉(𝑋) = E𝑋(Σ + 𝜆)−1 2 𝑘𝑋𝑘★ 𝑋(Σ + 𝜆)−1 𝑘𝑋𝑘★ (Σ + 𝜆)−1
2
𝑋
= (Σ + 𝜆)−1 2 Σ(Σ + 𝜆)−1 2 = (Σ + 𝜆)−1Σ.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Hence,

$$
E 𝜉(𝑋)2 ⪯sup ∥𝜉(𝑥)∥op E[𝜉(𝑋)] ⪯N∞(𝜆)2(Σ + 𝜆)−1Σ.
𝑥∈X
$$

And as a consequence E 𝜉(𝑥)2

 ≤N∞(𝜆)2,

$$
(Σ + 𝜆)−1Σ
$$

where we have used that

$$
op = ∥Σ∥op/( ∥Σ∥op + 𝜆) ≤1.
$$

Concentration bound on 𝜉. Using the self-adjoint concentration theorem, we get for any 𝑡> 0, such that 6𝑛𝑡2 ≥N∞(𝜆)2(1 + 𝑡/3),

$$
E ˆ𝜌[𝜉] −E𝜌[𝜉] 
∥Σ∥op + 𝜆 − 𝑛𝑡2
PD𝑛 op > 𝑡 ≤14 N (𝜆) exp .
∥Σ∥op 2N∞(𝜆)2(1 + 𝑡/3)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Therefore, using the contraposition of the prior implication, we get

$$
A(𝜆) > 1 1 −𝑡 ∥Σ∥op + 𝜆 − 𝑛𝑡2
PD𝑛 ≤14 N (𝜆) exp . (5.25)
∥Σ∥op 2N∞(𝜆)2(1 + 𝑡/3)
$$

(5.25)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 77 -->

5.C. KERNEL PROOFS 75 Decomposition of vector term in a variance and a bias term Let switch to the vector term, consider 𝜉: X × Y →G, deﬁned as

$$
𝜉= (Σ + 𝜆)−1 2 𝑘𝑥(𝜑(𝑦) −𝑘★ 𝑥𝛾𝜆).
$$

It allows expressing in simple form the vector term as

$$
.
𝑛 ∑︁
1 𝑛
B(𝜆) = 𝜉(𝑋𝑖,𝑌𝑖) −E(𝑋,𝑌)∼𝜌[𝜉(𝑋,𝑌)]
𝑖=1
$$

We can study this term through concentration inequality in G. To proceed we will dissociate the variability due to 𝑌to the one due to 𝑋, recalling that 𝑔𝜆(𝑥) = 𝑘★ 𝑥𝛾𝜆and going for the following decomposition

$$
𝜉(𝑥, 𝑦) = 𝜉𝑣(𝑥, 𝑦) + 𝜉𝑏(𝑥)
𝜉𝑣(𝑥, 𝑦) = (Σ + 𝜆)−1 2 𝑘𝑥(𝜑(𝑦) −𝑔∗(𝑥)), (5.26)
𝜉𝑏(𝑥) = (Σ + 𝜆)−1 2 𝑘𝑥(𝑔∗(𝑥) −𝑔𝜆(𝑥)),
$$

(5.26)

which corresponds to the decomposition

$$
B(𝜆) ≤B𝑣(𝜆) + B𝑏(𝜆) E ˆ𝜌[𝜉𝑣(𝑋,𝑌)] −E𝜌[𝜉𝑣(𝑋,𝑌)]
B𝑣(𝜆) = E ˆ𝜌[𝜉𝑏(𝑋,𝑌)] −E𝜌[𝜉𝑏(𝑋,𝑌)] . (5.27)
B𝑏(𝜆) =
$$

(5.27)

The ﬁrst term is due to the error because of having observed 𝜑(𝑦) rather than 𝑔∗(𝑥), often called “variance”, and the second term is due to the aiming for 𝑔𝜆instead of 𝑔∗often called “bias”.

Control of the variance To control the variance term, we will use the Bernstein inequality stated Theorem 7.

Bound on the moment of 𝜉𝑣. First of all notice that

$$
(Σ + 𝜆)−1
∥𝜉𝑣(𝑥, 𝑦)∥G ≤ 2 𝑘𝑥 op ∥𝜑(𝑦) −𝑔∗(𝑥)∥H .
$$

Therefore, under Assumption 5, for 𝑚≥2:

$$
(Σ + 𝜆)−1 
 
𝑚
E(𝑋,𝑌)∼𝜌[∥𝜉𝑣(𝑋,𝑌)∥𝑚] ≤E𝑋∼𝜌X 2 𝑘𝑥 op E𝑌∼𝜌|𝑋 ∥𝜑(𝑦) −𝑔∗(𝑥)∥𝑚
 


(Σ + 𝜆)−1 H
≤1 2𝑚!𝜎2𝑀𝑚−2 E𝑋∼𝜌X 𝑚
2 𝑘𝑥 .
op
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We bound the last term with

$$
(Σ + 𝜆)−1 (Σ + 𝜆)−1 


(Σ + 𝜆)−1 
𝑚 𝑚−2 2
E𝑋∼𝜌X 2 𝑘𝑥 ≤ sup 𝑥∈supp 𝜌X 2 𝑘𝑥 op E𝑋∼𝜌X 2 𝑘𝑥
op op
= N∞(𝜆)(𝑚−2)N (𝜆).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Concentration on 𝜉𝑣. Applying Theorem 7, we get, for any 𝑡> 0, that

$$
− 𝑛𝑡2
P (B𝑣(𝜆) > 𝑡) ≤2 exp . (5.28)
2𝜎2N (𝜆) + 2𝑀N∞(𝜆)𝑡
$$

(5.28)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 78 -->

Control of the bias To control the bias, we recall a simpler version of Bernstein concentration inequality, that is a corollary of Theorem 7.

Theorem 9 (Concentration in Hilbert space (Pinelis and Sakhanenko, 1986)). Let denote by A a Hilbert space and by (𝜉𝑖) a sequence of independent random vectors on A such that E[𝜉𝑖] = 0, that are bounded by a constant 𝑀, with ﬁnite variance 𝜎2 = E[Í𝑛

$$
P( \sum_{𝑛 𝑖=1} 𝜉𝑖 𝑖=1 ∥𝜉𝑖∥2]. For any 𝑡> 0, ≥𝑡) ≤2 exp 𝑡2 − 2𝜎2 + 2𝑡𝑀/3 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Bound on 𝜉𝑏. We have

$$
(Σ + 𝜆)−1
∥𝜉𝑏(𝑥)∥G ≤ sup 𝑥∈supp 𝜌X 2 𝑘𝑥 op ∥𝑔𝜆(𝑥) −𝑔∗(𝑥)∥H ≤N∞(𝜆) ∥𝑔𝜆−𝑔∗∥∞.
$$

Therefore, with Appendix 5.C.5, we get

$$
∥𝜉𝑏(𝑥)∥G ≤𝑏1𝜆𝑞−𝑝N∞(𝜆).
$$

Variance of 𝜉𝑏. For the variance we proceed with

$$
∥𝜉𝑏(𝑥)∥2 G ≤N∞(𝜆)2 ∥𝑔𝜆(𝑥) −𝑔∗(𝑥)∥2 H .
$$

Therefore,

$$
E[∥𝜉𝑏(𝑋)∥2] ≤N∞(𝜆)2 ∥𝑔𝜆−𝑔∗∥2 𝐿2 .
$$

Using the derivations made in Appendix 5.C.5, we have, using that 𝑞≤1,

$$
(𝐾+ 𝜆)−1𝐾𝑞𝑔0 (𝐾+ 𝜆)−(1−𝑞)
∥𝑔𝜆−𝑔∗∥𝐿2 = 𝜆 𝐿2 ≤𝜆 op ∥(𝐾+ 𝜆)−𝑞𝐾𝑞∥op ∥𝑔0∥𝐿2
≤𝜆𝑞∥𝑔0∥𝐿2 .
$$

Concentration on 𝜉𝑏. Adding everything together, we get

$$
©­­ « ª®® ¬
− 𝑛𝑡2 2 
P (B𝑏(𝜆) > 𝑡) ≤2 exp . (5.29)
𝜆2𝑞N∞(𝜆)2 ∥𝑔0∥2 𝐿2 + 𝑏1𝜆𝑞−𝑝N∞(𝜆)𝑡/3
$$

(5.29)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Note that based on the bound on the variance, we would like N∞(𝜆)2𝜆2𝑞≈𝜆2(𝑞−𝑝) to be smaller than N (𝜆) ≈𝜆−𝜎. It is the case since 𝑞> 𝑝.

Union bound To control ∥𝑔𝑛−𝑔𝜆∥𝐿∞≤𝑐𝑝𝜆−𝑝A(𝜆)(B𝑣(𝜆) + B𝑏(𝜆)), we need to perform a union bound on the control of A and the control of B := B𝑣+ B𝑏, we use that for any 𝑡> 0 and 0 < 𝑠< 1, 𝑐𝑝𝜆−𝑝AB > 𝑡implies A > 1/(1 −𝑠) or B > (1 −𝑠)𝑡𝜆𝑝/𝑐𝑝. Similarly, B𝑣+ B𝑏> 𝑡, implies that either B𝑣> 𝑡/2, either B𝑏> 𝑡/2. Therefore, we have, the following inclusion of events (with respect to D𝑛)

$$
A > 1 1 −𝑠 B𝑣> (1 −𝑠)𝑡𝜆𝑝 B𝑏> (1 −𝑠)𝑡𝜆𝑝
{∥𝑔𝑛−𝑔𝜆∥𝐿∞> 𝑡} ⊂ ∪ ∪ .
2𝑐𝑝 2𝑐𝑝
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

In terms of probability this leads to

$$
A > 1 1 −𝑠 B > (1 −𝑠)𝑡𝜆𝑝
PD𝑛(∥𝑔𝑛−𝑔𝜆∥𝐿∞> 𝑡) ≤PD𝑛 + PD𝑛 . (5.30)
𝑐𝑝
$$

(5.30)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Looking closer it is the term in B that will be the more problematic, therefore we would like 𝑠to be small. If we take 𝑠to be a constant with respect to 𝑡, we will get something that behaves like P(𝐵> 𝑡𝜆𝑝), which is the

<!-- page: 79 -->

5.C. KERNEL PROOFS 77 best we can hope for (this also explain why we divide B > 𝑡in B𝑣> 𝑡/2 or B𝑏> 𝑡/2). We will consider 𝑠= 1/2. We express concentration based on the expression of N and N∞, assuming 𝜆≤∥Σ∥op, and 𝑛> 𝑎2

$$
3𝜆−2𝑝
PD𝑛(A > 2) ≤28𝑎2𝜆−𝜎exp(−𝑛𝜆2𝑝
10𝑎2 3 ).
$$

Similarly, we get, when 𝜆≤1, using that 𝜆−𝜎≥1

$$
− 𝑛𝜆𝜎𝑡2
PD𝑛(B𝑣> 𝑡/4) ≤2 exp .
32𝜎2𝑎2 + 8𝑀𝑎3𝜆−𝑝𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

For the bias term, we can proceed at a brutal bounding, based on the fact that for 𝜆≤1, 𝜆𝑞−𝑝≤1 ≤𝜆−𝜎, to get

$$
!
− 𝑛𝜆𝜎𝑡2
PD𝑛(B𝑏> 𝑡/4) ≤2 exp .
32𝑎2 3 ∥𝑔0∥𝐿2 + 8𝑏1𝑎3𝜆−𝑝𝑡/3
$$

With 𝑏4 = max(32𝜎2𝑎2, 32𝑎2 3 ∥𝑔0∥𝐿2) and 𝑏5 = max(8𝑀𝑎3, 8𝑏1𝑎3/3), we get the following union bound

$$
PD𝑛 \frac{B > 𝑡𝜆𝑝}{2} ≤4 exp \frac{−𝑛𝜆2𝑝+𝜎𝑡2}{𝑏4 + 𝑏5𝑡} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We proceed with the union bound on ∥𝑔𝑛−𝑔𝜆∥𝐿∞as

$$
−𝑛𝜆2𝑝+𝜎𝑡2
PD𝑛(∥𝑔𝑛−𝑔𝜆∥𝐿∞> 𝑡) ≤𝑏2𝜆−𝜎exp(−𝑏3𝑛𝜆2𝑝) + 4 exp ,
𝑏4 + 𝑏5𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑏2 = 28𝑎2 and 𝑏−1 3 = 10𝑎2 3, as long as 𝑏3𝑛> 𝜆−2𝑝, and 𝜆≤max(1, ∥𝐾∥op).

Reﬁnement of Lemma 14 Remark that the uniform control in Lemma 14 is more than we need, we only need control for each 𝑥as described in Assumption 2. Indeed, if 𝑝(𝑥) is such that there exists a constant ˜𝑐𝑝(that does not depend on 𝑥 or 𝜆), such that for any 𝑖∈N

$$
\frac{⟨𝑘𝑥, 𝑢𝑖⟩GX ≤˜𝑐𝑝𝜆𝑝(𝑥)}{𝑖} ,
$$

then considering that

$$
𝑔𝑛(𝑥) −𝑔𝜆(𝑥) = 𝑘★ 𝑥(𝛾𝑛−𝛾𝜆) = 𝑘★ 𝑥(Σ + 𝜆)−1 2 (Σ + 𝜆) 1 2 (𝛾𝑛−𝛾𝜆) ,
$$

we can improve the results of Lemma 14 by replacing 𝑝by 𝑝(𝑥). While we considered 𝑝= sup𝑥∈𝜌X 𝑝(𝑥) as a consequence of our proof scheme, one can expect to end up with the E𝑋[𝜆𝑝(𝑋)] instead of 𝜆𝑝when deriving the proof of Theorems 5 and 6 (for which one has to reﬁne Theorem 2 in order to integrate dependency of 𝐿 to 𝑥, similarly to what is done in Lemma 17), which will lead to better rates. Yet, because of the complexity of expressing a quantity of the type E𝑋[𝜑(𝑝(𝑋))], for some function 𝜑, we decided not to present this improved version in the paper.

### 5.C.7 Proof of Theorem 5

Based on the proof of Theorem 1, we know that

$$
ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞PD𝑛(∥𝑔𝑛−𝑔∗∥∞> 𝑡0) .
$$

Now we use that

$$
PD𝑛(∥𝑔𝑛−𝑔∗∥∞> 𝑡0) ≤PD𝑛(∥𝑔𝑛−𝑔𝜆∥∞> 𝑡0 −∥𝑔𝜆−𝑔∗∥∞) .
$$

The result follows from derivations in Appendix 5.C.6, where we used that when 𝑘is bounded, Assumptions 7 and 8 are veriﬁed with 𝜎= 1 and 𝑝= 1/2. Note that we do not need the source assumption, since we can bound directly ∥𝑔𝜆−𝑔∗∥𝐿2 ≤∥𝑔𝜆−𝑔∗∥𝐿∞< 𝑡0 while retaking the proof in Appendix 5.C.6. Moreover, the results of this last proof holds under the condition 𝑛𝜆𝑏3 > 1, but, since ED𝑛R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞, we can augment the constant 𝑏6 so that the result in Theorem 5 still holds for any 𝑛∈N∗.

<!-- page: 80 -->

### 5.C.8 Proof of Theorem 6

We can rephrase Lemma 14, using a union bound

$$
PD𝑛(∥𝑔𝑛−𝑔∗∥> 𝑡) ≤PD𝑛(∥𝑔𝑛−𝑔𝜆∥> 𝑡/2) + PD𝑛(∥𝑔𝜆−𝑔∗∥> 𝑡/2) 
 −𝑏3𝑛𝜆2𝑝 
−𝑛𝜆2𝑝+𝜎𝑡2
≤𝑏2𝜆−𝜎exp + 4 exp + 1𝑡≤2𝜆𝑞−𝑝.
4𝑏4 + 2𝑏5𝑡
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Using variant of Theorem 2 presented in Appendix 5.A.6, we get

$$
−𝑏3𝑛𝜆2𝑝 
R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞𝑏2𝜆−𝜎exp + 2𝑐𝜓𝑐𝛼2𝛼+1𝜆(𝑞−𝑝) (𝛼+1)
 
2 4 (𝑛𝜆2𝑝+𝜎)−𝛼+1 𝛼+1 2 + 𝑏𝛼+1 5 (𝑛𝜆2𝑝+𝜎)−(𝛼+1)
+ 2𝑐𝜓𝑐𝛼𝑐 𝑏 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As long as 𝜆≤max(∥𝐾∥op , 1) and 𝑛≥(𝑏3𝜆2𝑝)−1. We optimize those rates with 𝜆= 𝜆0𝑛−𝛾, and 𝛾satisfying

$$
2𝛾(𝑞−𝑝) = 1 −𝛾(2𝑝+ 𝜎) ⇒ 𝛾= (2𝑞+ 𝜎)−1.
$$

This leads to, for 𝑛after a certain 𝑁∈N∗

$$
0 𝑛 𝜎 2𝑞+𝜎exp 2(𝑞−𝑝)+𝜎 2𝑞+𝜎 
R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞𝑏2𝜆−𝜎 −𝑏3𝑛𝜆2𝑝
0 𝑛
+ 2𝑐𝜓𝑐𝛼2𝛼+1𝜆(𝑞−𝑝) (𝛼+1) 0 𝑛−(𝑞−𝑝) (𝛼+1)
 2𝑞+𝜎 2𝑞+𝜎 
𝛼+1 2 0 𝑛−(𝑞−𝑝) (𝛼+1) (2𝑝+𝜎)𝛼+1 2𝑞+𝜎 + 𝑏𝛼+1 5 𝜆(2𝑝+𝜎)𝛼+1 0 𝑛−2(𝑞−𝑝) (𝛼+1)
+ 2𝑐𝜓𝑐𝛼𝑐 𝑏 2 4 𝜆
≤𝑏8𝑛−2(𝑞−𝑝) (𝛼+1)
2𝑞+𝜎 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Since ℓis bounded, R( 𝑓𝑛) −R( 𝑓∗) ≤ℓ∞, and we can always higher 𝑏8, in order to have the inequality for any 𝑛∈N∗.

<!-- page: 81 -->

# Chapter 6. Exponential Convergence Rates for SVM

The following is a reproduction of Cabannes and Vigogna (2022).

Classiﬁcation is often the ﬁrst problem described in introductory machine learning classes. Generalization guarantees of classiﬁcation have historically been oﬀered by Vapnik-Chervonenkis theory. Yet those guarantees are based on intractable algorithms, which has led to the theory of surrogate methods in classiﬁcation. Guarantees oﬀered by surrogate methods are based on calibration inequalities, which have been shown to be highly suboptimal under some margin conditions, failing short to capture exponential convergence phenomena. Those “super fast” rates are becoming well understood for smooth surrogates, but the picture remains blurry for non-smooth losses such as the hinge loss, associated with the renowned support vector machines. In this paper, we present a simple mechanism to obtain fast convergence rates, and we investigate its usage for SVM. In particular, we show that SVM can exhibit exponential convergence rates even without assuming the hard Tsybakov margin condition.

## 6.1 Introduction

To solve a problem with computer calculations, classical computer science consists in handcrafting a set of rules. In contrast, machine learning is based on the collection of a vast amount of solved instances of this problem, and on the automatic tuning of an algorithm that maps inputs deﬁning the problem to the desired outputs. Denote by 𝑥in a space X the inputs, by 𝑦∈Y the outputs, and by 𝑓: X →Y the input/output mappings. To learn a mapping 𝑓∗, it is customary to introduce an explicit metric of error, and search for the function that minimizes it. Deﬁne this metric through a loss ℓ: Y × Y →R that quantiﬁes how bad a prediction 𝑓(𝑥) is when we observe 𝑦. If we assume the existence of a distribution over I/O pairs, 𝜌∈ΔX×Y, that generates the instances of the problem we mean to solve, we aim to minimize the average loss value

$$
R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] . (6.1)
$$

(6.1)

In practice, this “risk” R can be evaluated approximately with samples D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛, collected by the machine learning scientist and assumed to have been drawn independently accordingly to 𝜌.

We shall focus on the binary classiﬁcation problem where Y = {−1, 1}, and ℓis the zero-one loss ℓ(𝑦, 𝑧) = 1𝑦≠𝑧. In this setting, the risk R( 𝑓) captures the probability of mistakes of a classiﬁer 𝑓, and its minimizer is characterized by

$$
𝑓∗= arg min R( 𝑓) = sign 𝜂, where 𝜂(𝑥) = E [𝑌| 𝑋= 𝑥] . (6.2)
𝑓:X→Y
$$

(6.2)

Ideally, leveraging the dataset D𝑛, we would like to ﬁnd a mapping 𝑓D𝑛: X →Y that is close to be optimal, in the sense that the excess of risk E( 𝑓D𝑛) = R( 𝑓D𝑛) −R( 𝑓∗) is as small as it could be. Since this quantity is actually random, inheriting from the randomness of the samples, we will focus on controlling its average.1 In particular, we will show that, when our model is well-speciﬁed, as the number of samples grows, this 1Note that one could also be interested in controlling its tail, but this is out-of-score of the current literature on “super fast” rates.

79

<!-- page: 82 -->

average decays actually much faster than what usual statistical learning theory suggests. We give a brief historical review of related literature before précising our contributions.

### 6.1.1 Statistical learning theory

The classical approach to minimize (6.1) without the knowledge of 𝜌but with the sole access to samples D𝑛∼𝜌⊗𝑛is to restrict the search over functions in a class F ⊂YX , and look for an empirical risk minimizer

$$
𝑛 ∑︁
RD𝑛, where RD𝑛( 𝑓) = 1
𝑓∗ D𝑛∈arg min ℓ( 𝑓(𝑋𝑖),𝑌𝑖). (6.3)
𝑓∈F 𝑛
𝑖=1
$$

(6.3)

If we denote by 𝑓∗ F the minimizer of R in F, using the fact that RD𝑛( 𝑓∗ D𝑛), the excess of risk can be bounded as

$$
F) ≥RD𝑛( 𝑓∗
R( 𝑓) −RD𝑛( 𝑓)
R( 𝑓∗ D𝑛) −R( 𝑓∗) ≤2 sup + R( 𝑓∗ F) −R( 𝑓∗) | {z } . (6.4)
| {z } 𝑓∈F
approximation error
estimation error
$$

(6.4)

This bound can be seen as highly suboptimal because it bounds the deviation of a random function with the worst deviation in the function class. However, for any class F, there exists an “adversarial” distribution 𝜌 for which convergence rates (of the excess of risk toward zero as a function of the number of samples 𝑛∈N) derived through this bound can not be improved beside lowering some multiplicative constants (Vapnik, 1995). On the one hand, the estimation error can be controlled with general tools to bound the supremum of a random process (e.g., Dudley, 1967), and will decrease with a decrease in the size of the class F. On the other hand, the approximation error depends on assumptions of the problem, and the bigger the size of the class F, the less restrictive it will be to assume that 𝑓∗is not too diﬀerent from 𝑓∗ F. Hence, there is a clear trade-oﬀbetween controlling both errors, which should be balanced in order to optimize a bound on the full excess of risk.

### 6.1.2 Surrogate methods

In practice, due to the combinatorial nature of discrete-valued functions, ﬁnding the empirical risk minimizer (6.3) is often an intractable problem (e.g., Höﬀgen and Simon, 1992; Arora et al., 1997). Therefore, people have approached the original problem with other perspectives. A straightforward approach is given by plug-in classiﬁers, i.e., classiﬁers of the form sign ˆ𝜂, for ˆ𝜂some estimator of 𝜂. For example, such an estimator can be constructed as ˆ𝜂(𝑥) = Í𝑛 𝑖=1 𝛼𝑖(𝑥)𝑌𝑖, for 𝛼𝑖(𝑥) some weights that specify how much the observation 𝑌𝑖made at the point 𝑋𝑖should diﬀuse to the point 𝑥(see Friedman, 1994, for an example). Another popular approach to solve classiﬁcation problems is provided by support vector machines (SVM), which were introduced from geometric considerations to maximize the margin between the classes {𝑥∈X | 𝑓∗(𝑥) = 𝑦} for 𝑦∈{−1, 1} (Cortes and Vapnik, 1995).

These two approaches can be conjointly understood as introducing a surrogate loss 𝐿: R × Y →R and looking for a continuous-valued function 𝑔: X →R that solves the surrogate problem

$$
𝑓= sign 𝑔, 𝑔∗∈arg min R𝑆(𝑔), where R𝑆(𝑔) = E(𝑋,𝑌)∼𝜌[𝐿(𝑔(𝑋),𝑌)] , (6.5)
𝑔:X→R
$$

(6.5)

where the notation 𝑆stands for “surrogate”. To an estimate 𝑔: X →R of 𝑔∗we associate an estimate 𝑓: X →Y of 𝑓∗through the decoding step 𝑓= sign 𝑔. In particular, using the variational characterization of the mean, 𝜂can be estimated through 𝐿(𝑧, 𝑦) = |𝑧−𝑦|2. Regarding SVM, they are related to the hinge loss (see, e.g., Steinwart and Christmann, 2008)

$$
𝐿(𝑧, 𝑦) = max (0, 1 −𝑧𝑦) , (6.6)
$$

(6.6)

Surrogate methods beneﬁt from their relative easiness to optimize and the quality of their practical results. Arguably, they deﬁne the current state of the art in classiﬁcation, softmax regression being particularly popular to train neural networks on classiﬁcation tasks.

Surrogate methods were studied in depth by Bartlett et al. (2006), who proposed a generic framework to relate the excess of the original risk to the excess of surrogate risk through an inequality of the type

$$
R( 𝑓) −R( 𝑓∗) ≤𝜓(R𝑆(𝑔) −R𝑆(𝑔∗)) , (6.7)
$$

(6.7)

<!-- page: 83 -->

where 𝑓= sign 𝑔and 𝜓is a concave function, uniquely deﬁned from 𝐿and verifying 𝜓(0) = 0. The use of a concave function is motivated by Jensen inequality, allowing to integrate an inequality derived pointwise (conditionally on an input 𝑥).

### 6.1.3 Exponential convergence rates

On the one hand, calibration inequalities (6.7) are appealing, as they allow casting directly rates derived on the surrogate problem to rates on the original problem. On the other hand, because 𝜓has to be concave, rates in 𝑂(𝑛−𝑟) on the surrogate problem can not be cast as better rates on the original problem, corresponding to the optimal inequalities where 𝜓(𝑥) = 𝑐𝑥for some 𝑐> 0, Yet, one can ﬁnd cases where the sign of 𝜂can be estimated much faster than 𝜂itself, even when this sign is estimated with surrogate methods. In particular, Mammen and Tsybakov (1999) (see also Massart and Nédélec, 2006) introduced the following condition.

Assumption 10 (Hard margin condition). The binary classiﬁcation problem deﬁned through the distribution 𝜌is said to verify the (Tsybakov) hard margin condition if the conditional mean 𝜂is bounded away from zero, i.e.,

$$
∃𝜂0 > 0; |𝜂(𝑋)| > 𝜂0 a.s., (6.8)
$$

(6.8)

where the notation a.s. stands for almost surely. Equivalently, |𝜂|−1 ∈𝐿∞(𝜌X ).

Indeed, as shown in Appendix 6.A, under Assumption 10, leveraging sign equality, we get for any estimate 𝑔D𝑛: X →R computed from the dataset D𝑛,

$$
𝑔D𝑛−𝜂 
ED𝑛[R(sign 𝑔D𝑛)] −R( 𝑓∗) ≤PD𝑛 𝐿∞> 𝜂0 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As a consequence, an exponential concentration inequality on the 𝐿∞distance between 𝑔D𝑛and 𝜂directly translates to exponential convergence rates on the average excess of risk. In particular, estimation methods for 𝜂based on Hölder classes of functions, such as local polynomials, are known to be well-behaved with respect to the 𝐿∞norm (see, e.g., the construction of covering number by Kolmogorov and Tikhomirov, 1959). This was leveraged by Audibert and Tsybakov (2007) in a seminal paper that shows how better rates can be achieved on the classiﬁcation problem under Assumption 10 and a variety of weaker conditions (described later in Assumption 11).

Surprisingly, such an approach has remained somehow less popular than approaches based on calibration inequalities, and we are missing a framework to fully apprehend fast rates phenomena. Some results were achieved by Koltchinskii and Beznosova (2005). Recently, Cabannes et al. (2021c) showed that this result generalizes to any discrete output learning problem, and that approaches that naturally lead to concentration in 𝐿2 could be turned into fast rates based on interpolation inequalities that relate the 𝐿2 norm with the 𝐿∞ one (notably reusing the work of Fischer and Steinwart (2020) on interpolation spaces). Exploiting the work of Marteau-Ferey et al. (2019), this can be generalized to any self-concordant loss (using self-concordance to reduce the problem to a least-squares problem); and, through the work of Lin et al. (2020), to any spectral ﬁltering technique (beyond Tikhonov regularization), such as stochastic gradient descent, which was actually shown earlier for binary classiﬁcation by Pillaud-Vivien et al. (2018b) and Nitanda and Suzuki (2019). In the same stream of research, Vigogna et al. (2022) proposed a general framework to study exponential rates for smooth losses in multiclass classiﬁcation beyond least-squares.

### 6.1.4 Contribution

The proofs of exponential convergence in the works quoted above are all based on the basic mechanism outlined in Audibert and Tsybakov (2007). Unfortunately, such a mechanism does not easily extend to the hinge loss. Does this mean that support vector machines do not exhibit super fast rates, and thus they are inferior to other surrogate methods? The practice seems to answer negatively. In this paper, we give a ﬁrm theoretical answer to this question. In particular, we show not only that support vector machines do achieve exponential rates, but also that they can do so even without assuming the hard margin condition. Our main contribution is to introduce a general framework to prove exponential convergence rates, and show how this framework can be applied to the hinge loss while only considering classical assumptions.

<!-- page: 84 -->

level lines of R(sign 𝑔𝜃𝑛) path {𝜃𝜆; 𝜆> 0} region {𝜃; ∥𝜃−𝜃𝜆∥< 1} certiﬁed value of R(𝑔𝜃𝑛) when ∥𝜃𝑛−𝜃𝜆∥< 1

$$
𝜃∗ 𝜃𝜆
$$

[FIGURE: Figure 6.1]

Figure 6.1: Our convergence analysis consists in relating natural concentration given by surrogate methods to the original excess of risk without passing by the surrogate excess of risk. As the drawing shows, concentration in parameter space Θ can be cast as deviation on the original excess of risk. Yet, such a casting relation depends on the geometry of this picture, which itself depends on what surrogate is used, what is the function to learn, how a regularized estimator approached it, and how our empirical estimate concentrates around the regularized estimator. Note that this ﬁgure illustrates an abstract mechanism that generalizes the simpler mechanism we use to derive exponential convergence rates.

Outline. Our general strategy is illustrated on Figure 6.1 and consists in ﬁrst ﬁnding a relation

$$
R𝑆(𝑔𝜃) −R𝑆(𝑔𝜃∗) ≥∥𝜃−𝜃∗∥,
$$

for some natural parameter 𝜃in a Banach space Θ parametrizing a class of functions 𝑔𝜃∈F, and then show that sign 𝑔𝜃= sign 𝑔𝜃∗when ∥𝜃−𝜃∗∥is small enough, that is,

$$
∃𝜀> 0; ∥𝜃−𝜃∗∥≤𝜀 ⇒ sign 𝑔𝜃= sign 𝑔𝜃∗.
$$

Assuming that sign 𝑔𝜃∗= 𝑓∗, we deduce that, as shown in Appendix 6.A,

$$
R𝑆(𝑔𝜃𝑛) −R𝑆(𝑔𝜃∗) ≥𝜀 ,
ED𝑛[R(sign 𝑔𝜃𝑛)] −R( 𝑓∗) ≤PD𝑛
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑔𝜃𝑛is an estimate of 𝑔𝜃based on the samples D𝑛. Finally, we conclude with an exponential concentration inequality that controls the deviation of the excess of risk based on classical statistical learning theory.

## 6.2 Exponential convergence of SVM

This section is devoted to the proof of exponential convergence rates for the hinge loss. We shall ﬁx the notation R𝑆as the surrogate risk associated with (6.6). All the proofs are collected in Appendix 6.A.

### 6.2.1 Reﬁned calibration for the hinge loss

We start by introducing the classical weak margin condition (Mammen and Tsybakov, 1999).

Assumption 11 (Weak margin condition). The binary classiﬁcation problem deﬁned through the distribution 𝜌is said to verify the (Tsybakov) 𝑝-margin condition, with 𝑝∈(0, ∞), if there exists a constant 𝑐> 0 such that

$$
P𝜌X (0 < |𝜂(𝑋)| < 𝑡) ≤𝑐𝑡𝑝, (6.9)
$$

(6.9)

where the notation 𝜌X denotes the marginal of 𝜌over X.

Assumption 11 is equivalent to asking for the inverse of the conditional mean |𝜂|−1 (with the convention 0−1 = 0) to belong to the Lorentz space 𝐿𝑝,∞(𝜌X ) (also known as weak-𝐿𝑝space), which is the Banach space endowed with the norm (quasi-norm and quasi-Banach if 𝑝< 1)

$$
∥𝑓∥𝑝,∞= sup 𝑡P𝜌X ( 𝑓(𝑋) > 𝑡) 1 𝑝, (6.10)
𝑡>0
$$

(6.10)

where the 𝜌X denotes the marginal of 𝜌with respect to X. This deﬁnition can be extended to the case 𝑝= ∞ by setting 𝐿𝑝,∞(𝜌X ) = 𝐿∞(𝜌X ), which characterizes the hard margin condition in Assumption 10. We will also use ∥·∥𝑝, for 𝑝∈[1, ∞], to denote the 𝐿𝑝-norm on X endowed with 𝜌X .

We now relate the excess of risk on the hinge loss to the deviation in these spaces.

<!-- page: 85 -->

Lemma 29 (Weak-𝐿𝑞concentration due to the hinge loss). For any functions 𝑔1, 𝑔2 : X →[−1, 1],

$$
R𝑆(𝑔2) −R𝑆(𝑔1) = E𝜌X [−𝜂(𝑋)(𝑔2(𝑋) −𝑔1(𝑋))]. (6.11)
$$

(6.11)

In particular, under Assumption 10, for any 𝑔: X →R,

$$
|𝜂|−1

−1
R𝑆(𝑔) −R𝑆(𝑔∗) ≥ ∞∥𝜋(𝑔) −𝑔∗∥1 , (6.12)
$$

(6.12)

where 𝑔∗= sign 𝜂is a minimizer of R𝑆and 𝜋is the projection of R on [−1, 1], deﬁned as mapping 𝑡∈R to 𝜋(𝑡) = sign(𝑡) min{|𝑡|, 1}. Similarly, under Assumption 11, with 𝑞= 𝑝/𝑝+ 1,

$$
R𝑆(𝑔) −R𝑆(𝑔∗) ≥2−1 

|𝜂|−1

−1
𝑝,∞∥𝜋(𝑔) −𝑔∗∥𝑞,∞. (6.13)
$$

(6.13)

Lemma 29 shows that we can set the minimizer 𝑔∗= 𝑓∗∈{−1, 1}X . This is a useful fact as it implies that the excess of the original risk is zero as soon as ∥𝑔−𝑔∗∥∞< 1. In essence, the only piece missing in order to prove fast convergence rates is an interpolation inequality between 𝐿𝑞,∞and 𝐿∞. In the following, we will leverage Lemma 29 more subtly by considering a class of functions G and assumptions on the distribution 𝜌X such that, if an estimate 𝑔∈G has not the same sign almost everywhere as the estimand 𝑔∗, then ∥𝑔−𝑔∗∥𝑞,∞is bounded away from zero. By contraposition, if 𝑔∈G presents a small excess of surrogate risk, then sign 𝑔= sign 𝑔∗. When X is a metric space, one way to proceed is to assume that 𝑔is Lipschitz-continuous, together with some minimal mass assumptions. Let us begin with the minimal mass assumption. We ﬁrst need the following deﬁnition.

Deﬁnition 30 (Well-behaved sets). A set 𝑈⊂X is said to be well-behaved with respect to 𝜌if there exist constants 𝑐, 𝑟, 𝑑> 0 such that, for any 𝑥∈𝑈,

$$
∀𝜀∈[0, 𝑟]; 𝜌X (𝑈∩B(𝑥, 𝜀)) ≥𝑐𝜀𝑑, (6.14)
$$

(6.14)

and B(𝑥, 𝜀) the ball in X of center 𝑥and radius 𝜀.

The following examples show that the coeﬃcient 𝑑that appears in (6.14) results from the dimension of the ambient space, the regularity of singularities of the border of the set, and the decay of the density when approaching the frontier of the set.

Example 14. The set [0, 1] 𝑝is well-behaved with coeﬃcients 𝑟= 1, 𝑑= 𝑝and 𝑐= 2−𝑑vol(S𝑑−1) with respect to the Lebesgue measure in R𝑑.

$$
(𝑥, 𝑦) ∈R2 𝑥∈[0, 1], 𝑦∈[0, 𝑥𝑛−1]
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

is well-behaved with coeﬃcient 𝑟= 1, 𝑑= 𝑛 and 𝑐= 𝑛−1 with respect to the Lebesgue measure. Reciprocally, the set [0, 1] is well-behaved with coeﬃcient 𝑟= 1, 𝑑= 𝑛and 𝑐= 𝑛−1 with respect to the measure whose density equals 𝑝(𝑥) = 𝑥𝑛−1.

Example 15. The set Assumption 12 (Minimal mass assumption). The decision regions X𝑦= {𝑥∈supp(𝜌X ) | 𝑓∗(𝑥) = 𝑦} for 𝑦∈{−1, 1} are well-behaved.

Assumption 12 is a weakening of an assumption that is commonly found in the statistical learning literature. More precisely, it is often assumed that 𝜌is absolutely continuous according to the Lebesgue measure 𝜆on X (assumed to be a Euclidean space), that its density is bounded away from zero on its support, and that its support has smooth boundary, so that 𝜆(supp 𝜌X ∩B(𝑥, 𝜀)) > 𝑐′𝜆(B(𝑥, 𝜀)) (see the strong density assumption in Audibert and Tsybakov, 2007).

The minimal mass requirement allows relating misclassiﬁcation events to 𝐿𝑞,∞deviation.

Lemma 31. Under Assumption 12, there exists a constant 𝑐0 such that if 𝑔is 𝐺-Lipschitz-continuous for 𝐺> 𝑟−1, for any 𝑞∈(0, 1]

$$
∃𝑥∈supp 𝜌X ; |𝑔(𝑥) −𝑔∗(𝑥)| ≥1 ⇒ ∥𝑔−𝑔∗∥𝑞,∞≥𝑐0𝐺−𝑑 𝑞. (6.15)
$$

(6.15)

Putting together Lemmas 29 and 31, we obtain the following reﬁned calibration.

Proposition 32. Under Assumptions 11 and 12, if 𝑔is 𝐺-Lipschitz-continuous with 𝐺> 𝑟−1, we have

$$
R𝑆(𝑔) −R𝑆(𝑔∗) ≤2−1 

|𝜂|−1

−1
𝑝,∞𝑐0𝐺−𝑑(𝑝+1) 𝑝 ⇒ R(sign 𝑔) = R( 𝑓∗). (6.16)
$$

(6.16)

<!-- page: 86 -->

### 6.2.2 Trade-oﬀbetween estimation and approximation errors

We are now left with the research of 𝑔D𝑛inside a class of Lipschitz-continuous functions such that R𝑆(𝑔D𝑛) −R𝑆(𝑔∗) is sub-Gaussian (its randomness being inherited from the dataset D𝑛from which 𝑔D𝑛is built). To do so, let us consider a linear class of functions

$$
𝜃∈H, ∥𝜃∥H ≤𝑀
G𝑀,𝜎= 𝑥↦→ 𝜃, 𝜑(𝜎−1𝑥) , (6.17)
$$

(6.17)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where H is a separable Hilbert space, 𝜑: X →H is a 𝐺𝜑-Lipschitz-continuous mapping, and 𝜎> 0 is a scaling (or bandwidth) parameter. Such a class of functions can be entirely described from the kernel 𝑘(𝑥, 𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩(see Scholkopf and Smola, 2001, for a primer on kernel methods). An example for G is given by the Gaussian kernel, a.k.a. radial basis function, 𝑘(𝑥, 𝑥′) = exp(−∥𝑥−𝑥′∥2). Using Cauchy-Schwarz, it is easy to show that any function in G𝑀,𝜎is 𝑀𝐺𝜑𝜎−1-Lipschitz-continuous.

In order to ﬁnd a function 𝑔D𝑛that is likely to minimize R𝑆without accessing the distribution 𝜌, but only i.i.d. samples D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼𝜌⊗𝑛, it is classical to consider the empirical risk minimizer

$$
𝑛 ∑︁
1 𝑛
𝑔D𝑛∈arg min 𝐿(𝑔(𝑋𝑖),𝑌𝑖). (6.18)
𝑔∈G𝑀,𝜎 𝑖=1
$$

(6.18)

This problem is convex with respect to 𝜃parametrizing 𝑔∈G𝑀,𝜎, and is easily optimized with duality. We refer the curious reader to the extensive literature on SVM (see Cristianini and Shawe-Taylor, 2000; Scholkopf and Smola, 2001; Steinwart and Christmann, 2008, for books on the matter).

In order to show that R𝑆(𝑔D𝑛) is close to R𝑆(𝑔∗), one can apply classical results from statistical learning theory, and in particular (6.4). The estimation error can be bounded using the extensive literature on Rademacher complexity for linear classes of functions on Lipschitz-continuous losses (Bartlett and Mendelson, 2002). To bound the approximation error, one needs to make additional assumptions on the problem. We refer to Steinwart and Scovel (2007); Blaschzyk and Steinwart (2018) for advanced considerations on the matter. In view of our calibration result (6.16), the following additional assumption suﬃces to prove exponential convergence of SVM.

Assumption 13 (Source condition). The classiﬁcation problem veriﬁes the 𝑝-margin condition 11, and there exist 𝑀, 𝜎and a function 𝑔∈G𝑀,𝜎such that R𝑆(𝑔) −R𝑆(𝑔∗) ≤4−1∥|𝜂|−1 ∥−1

$$
𝑝,∞𝑐0𝑀−𝑟𝐺−𝑟
$$

𝜑𝜎𝑟with 𝑟= 𝑑(𝑝+ 1)/𝑝.

It should be noted that Assumption 13, together with Assumption 12, implies that the decision frontier X−1 ∩X1 (the bar notation corresponding to space closure), inherits from the regularity of 𝑔, since it is included in the set {𝑥∈X | 𝑔(𝑥) = 0}. In particular, if G𝑀,𝜎is included in C𝑚, this frontier would be in C𝑚. Hence, for Assumptions 13 and 12 to hold, the boundary frontier should match the regularity implicitly deﬁned by G𝑀,𝜎.

We are ﬁnally ready to state our main result, establishing exponential convergence rates for SVM.

Theorem 10 (Exponential convergence rates for SVM). Under Assumptions 11, 12 and 13, there exists a constant 𝑐> 0 such that the empirical minimizer 𝑔D𝑛deﬁned by (6.18) veriﬁes

$$
ED𝑛R(sign 𝑔D𝑛) −R( 𝑓∗) ≤exp(−𝑐𝑛). (6.19)
$$

(6.19)

### 6.2.3 Relaxing assumptions

Exponential convergence rates rely on strong assumptions in order to set the approximation error to zero. In particular, it is customary to assume that the surrogate function to learn lies in the model we have chosen, that is, in our notation, 𝑔∗∈G𝑀,𝜎. In our case this would be a strong assumption, since 𝑔∗is piecewise linear while G𝑀,𝜎is a smooth space of functions. It turns out that the assumption 𝑔∗∈G𝑀,𝜎is not necessary, and what we actually need is a suﬃciently small risk. How small is enough is quantiﬁed by the statement of Proposition 32. From a qualitative point of view, the requirement of Assumption 13 is natural (surrogate risk must be smaller than 𝜀), with the technical part being just a quantiﬁcation of the needed behavior (bound on such 𝜀).

<!-- page: 87 -->

$$
10−1 1 p=.1 p=.3 p=1 p=3
Excess of risk
η(x)
0
10−3 p=.1 p=.3 p=1 p=3
−1
101 102 103 −1 0 1 input x
Samples size
$$

[FIGURE: Figure 6.2]

Figure 6.2: SVM generalization error as a function of the number of samples (left) for a problem where 𝑋is uniform on [−1, . −1] ∪[.1, 1] and 𝜂(𝑥) = sign(𝑥) |𝑥|𝑝(right). We observe exponential convergence rates.

To deepen the study of the approximation error, one could leverage the following geometrical characteri- zation of the risk of misclassiﬁcation. For 𝑓: X →{−1, 1}, we have

$$
R( 𝑓) −R( 𝑓∗) = E[|𝜂(𝑋)| 1 𝑓(𝑥)≠𝑓∗(𝑋)] ≤P( 𝑓(𝑋) ≠𝑓∗(𝑋)) = 𝜌X 𝑓−1({1}) △X1 , (6.20)
$$

(6.20)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where △denotes the symmetric diﬀerence of sets, i.e. 𝐴△𝐵= (𝐴∪𝐵) \ (𝐴∩𝐵). In particular, if the function class G𝑀,𝜎is rich enough, and the classes X1 and X−1 are separated, in the sense that the distance between any two points in each set is bounded away from zero,2 then Assumption 13 holds, and the minimizer 𝑔G𝑀,𝜎 of the surrogate risk in G𝑀,𝜎veriﬁes

$$
𝜌X (sign 𝑔G𝑀,𝜎)−1({1}) △X1 ≤𝜓(𝑀, 𝜎), (6.21)
$$

(6.21)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

for 𝜓a function that vanishes for suﬃciently large 𝑀and small 𝜎.

On the one hand, one could control the approximation error by assuming or deriving inequalities akin to (6.20) and (6.21), with diﬀerent proﬁles of 𝜓. We conjecture that this can be done by assuming margin conditions that are well adapted to the geometric nature of SVM, such as the one proposed by Steinwart and Scovel (2007) (see also Gentile and Warmuth, 1999; Cristianini and Shawe-Taylor, 2000). On the other hand, the estimation error can be controlled by extending the ideas presented in this paper to study the worst value of the estimation error R(sign 𝑔D𝑛) −R(sign 𝑔G𝑀,𝜎) under the knowledge of R𝑆(𝑔D𝑛) −R𝑆(𝑔G𝑀,𝜎). Fitting 𝑀and 𝜎to trade estimation and approximation error, such derivations would open the way to fast polynomial rates under less restrictive assumptions.

## 6.3 Numerical analysis

In this section, we provide experiments to illustrate and validate our theoretical ﬁndings. In order to be inline with the current practice of machine learning, instead of considering the hard constraint ∥𝜃∥≤𝑀when minimizing a risk functional, we add a penalty 𝜆∥𝜃∥2 to the risk to be minimized. Going from a constrained to a penalized framework does not change the nature of the statistical analysis, and one might loosely think of 𝜆as 1/𝑀(see, for example, Bach, 2023). All experiments are made with the Gaussian kernel. Precise details of the diﬀerent settings are provided in Appendix 6.B.

First, we observe that the regime described in this paper kicks in when the error is already pretty small. On many real-world problems, we do not expect the generalization error as a function of the number of data used for training to exhibit a clear exponential behavior until an unusually big number of samples is used. This fact is illustrated on Figure 6.2, where for hard problems, the exponential behaviors still do not kick in after a thousand of samples.

2This property is sometimes referred to as the cluster assumption (Rigollet, 2007) under which even weakly supervised learning techniques may exhibit exponential convergence rates (e.g. Cabannes et al., 2021b). In terms of practical applications, this assumption says that no one can continuously modify an input to go from a region of the space linked with one class to a region linked with another class without going through inputs that will never exist. This is typically true for well-curated image datasets such as CIFAR10: one can not continuously transform an image of a truck into an image of a horse without going through images that will never appear in the CIFAR10 dataset (Krizhevsky, 2009).

<!-- page: 88 -->

$$
Level lines of η gλ,σ gλ,σ (noiseless case)
1
0.75
0.50
0.6 2
0.25 −0.3 1
0.00 0.9 0
0.0
−0.9 −1 2 3
−0.25 0.3 −3
−0.50 −0.6
−1.00 −2 −2
−0.75
Level lines of η gλ,σ gλ,σ (noiseless case)
0.75 1.6 1.6
2.4 2.4
0.50 0.9 2.4
0.6 1.6 0.8
0.25 0.3 0.0 −0.8
−0.6 −0.3 0.0 −1.6
−0.9 −2.4 −1.6 −2.4
0.00
−0.25
−0.50
−0.75 −1.00
$$

[FIGURE: Figure 6.3]

Figure 6.3: Study of the level lines of 𝑔𝜆,𝜎when 𝜂−1(0) ∈C∞(top) and 𝜂−1(0) ∈C0 \ C1 (bottom). The function 𝑔∗takes values −1 below the optimal decision frontier plotted in red and +1 above, independently of the noise. We observe that the bias error R(sign 𝑔𝜆,𝜎) −R( 𝑓∗), which is bounded by the volume between the level lines 

$$
𝑔𝜆,𝜎(𝑥) = 0
$$

and {𝑥∈X | 𝜂(𝑥) = 0} (plotted in red), depends on both the regularity of the latter, and on the noise level. Here, 𝜎is taken to be of the order of 15% of the diameter of the domain, which explains the regularity of the observed level lines. The noiseless cases on the right correspond to the situations where E[𝑌|𝑋] = sign 𝜂(𝑋) for 𝜂plotted on the left.

$$
𝑥∈X
$$

Second, this paper shows that, in order to get exponential convergence rates for SVM, one needs the minimizer 𝑔𝑀,𝜎of the surrogate risk over the selected class of functions to be a perfect classiﬁer, i.e. its sign equals the sign of 𝑔∗. While this is not constraining under the cluster assumption, we inspect divergences from this condition on Figure 6.3. We observe that, even if 𝑔∗does not depend on the noise, 𝑔𝑀,𝜎does. We also observe that the regularity of the decision boundary {𝑥∈X | 𝜂(𝑥) = 0} should match the regularity deﬁned implicitly by the kernel 𝑘and the scale parameter 𝜎.

Experimental comparisons of diﬀerent classiﬁcation approaches have been done by many people, and our goal is not to showcase the superiority of the SVM over least-squares, which might be considered as general wisdom that led to the golden age of SVM in the pre-deep-learning area (see Joachims, 1998, for example). In comparison with previous works based on calibration inequalities (Rosasco et al., 2004; Steinwart, 2007), our analysis proves the robustness of SVM to noise far away from the decision boundary, in the sense that one does not need 𝜂to be bounded away from zero. This is a distinctive aspect of SVM compared to smooth surrogate methods (Nowak-Vila et al., 2020), such as softmax regression, that implicitly estimate conditional probabilities and whose performance depends on the regularity of 𝜂. We illustrate this fact graphically on Figure 6.4.

## 6.4 Limitations

Are surrogate methods only a proxy for classiﬁcation? From a theoretical perspective, if we are only interested in the optimal mapping 𝑓: X →Y, learning surrogate quantities can be seen as a waste of resources. In essence, this waste of resources is similar to the one occurring when we learn the full probability function (𝑝(𝑦))𝑦∈Y for some probability distribution 𝑝on Y, while we only care about its mode. Yet, in practice, what we call a “surrogate” problem might actually be a problem of prime interest when we do not only want to predict 𝑓∗(𝑥), but we would also like to know how much we can conﬁdently discard other potential outputs for an input 𝑥. Furthermore, assuming that a problem is exactly deﬁned through an “original” loss that deﬁnes a clear and unique measure of error can be questioned when some practitioners evaluate methods with several metrics of performance (e.g. Chowdhery et al., 2022).

<!-- page: 89 -->

$$
η(x) SVM bias: gλ,σ Least-square bias
1 1 1
0 0 0
input x −1
−1 −1
$$

[FIGURE: Figure 6.4]

Figure 6.4: Comparison of the regularized risk (i.e. R𝑆(𝑔𝜃) + 𝜆∥𝜃∥2) minimizer for the hinge loss surrogate (middle) and the least-squares surrogate (right), when 𝜂is not regular (left). In this setting, the hinge loss is minimized for 𝑔= sign(𝜂), which can be chosen regular, while the least-squares loss is minimized for 𝑔= 𝜂, which can not be chosen regular. The reconstruction is made with 𝜎about 3% of the domain diameter, and 𝜆relatively small. We assume no density in the middle of the domain, explaining the absence of deﬁnition of 𝜂and the dashed lines of the right ﬁgures. The oscillation on the later ﬁgures is related to the Gibbs phenomenon (Wilbraham, 1848). This phenomenon prevents the regularized least-squares solution from being a perfect classiﬁer.

Do PAC-bounds provide conﬁdence levels? Since the parameters in Assumptions 11 and 12 are hard to estimate in practice, it would be diﬃcult to directly plug our bounds into a practical problem to derive conﬁdence levels on how much error one might expect when deploying a model in production. Less ambitiously, we see theorems akin to Theorem 10 as providing theoretical indications that a learning method or a set of hyperparameters is sound. This is a generic downfall of probably approximately correct (PAC) generalization bounds (Valiant, 2013), which might explain why practitioners often prefer to derive error indications from test samples (see, e.g., Géron, 2017). Along this line, research on conformal prediction provides interesting considerations to obtain useful conﬁdence information from test samples (Vovk and Shafer, 2008). Finally, all these statistical methods to get conﬁdence intervals assume representative (if not i.i.d.) data, an assumption sometimes hard to meet in practice, which is a problem that has found echoes in the civil society (e.g. Benjamin, 2019).

## 6.5 Conclusion

In this work, we were keen to illustrate a simple mechanism to get exponential convergence rates for a loss that is quite popular and whose understanding can not be easily reduced to existing work. In particular, we show that the hard margin condition is not crucial in order to derive exponential convergence rates for the SVM.

This provides a crucial step to better understand convergence rates on classiﬁcation problems. An extension to generic discrete output problems could be made by considering polyhedral losses, and deriving variants of Lemma 29 (see Frongillo and Waggoner, 2021, for calibration inequalities for such losses). An important follow-up would be to provide a more global picture of fast polynomial rates for SVM under relaxations of Assumptions 12 and 13.

Finally, Chizat and Bach (2020) have made a link between two-layer wide neural networks in the interpolation regime (which implies Assumption 10 with 𝜂0 = 1) and max-margin classiﬁers over speciﬁc linear classes of functions. As a consequence, we could directly plug in our analysis to prove exponential convergence rates for those small neural networks in this noiseless setting. Studying rates, constants and hyperparameter tuning in this setting would be of particular interest if it was to provide practical guidelines to deep learning practitioners in the spirit of Yang et al. (2021).

<!-- page: 90 -->

<!-- page: 91 -->

# Appendix

## 6.A Proofs

Notation. This paper makes use of the following standard notations. We used the simplex notation Δ𝐴 to denote the space of probability measure over a Polish space 𝐴. We also used the notation YX to denote functions from X to Y (which can be seen as a sequence of elements in Y indexed by X).

Equations. Some standard derivations in the fast rates literature were omitted in the main paper. In particular, under Assumption 10, we know that when |𝑔(𝑥) −𝜂(𝑥)| < |𝜂(𝑥)| then sign 𝑔(𝑥) = sign 𝜂(𝑥) = 𝑓∗(𝑥), hence R(sign 𝑔) −R( 𝑓∗) ≤P𝑋(sign 𝑔(𝑋) ≠𝑓∗(𝑋)) ≤1∥𝑔−𝜂∥∞≥𝜂0. As a consequence, ED𝑛[R(sign 𝑔𝑛)] − R( 𝑓∗) ≤PD𝑛(∥𝑔−𝜂∥∞≥𝜂0).

Similarly, the outline exposition follows from the fact that

$$
ED𝑛[R(sign 𝑔𝜃𝑛)] −R( 𝑓∗) = ED𝑛[R(sign 𝑔𝜃𝑛) −R(sign 𝑔𝜃∗)] ≤ED𝑛[1sign 𝑔𝜃𝑛≠(sign 𝑔𝜃∗)]
≤ED𝑛[1∥𝜃𝑛−𝜃∗∥≥𝜀] ≤PD𝑛(∥𝜃𝑛−𝜃∗∥≥𝜀)
≤PD𝑛(R𝑆(𝑔𝜃𝑛) −R(𝑔𝜃∗) ≥𝜀).
$$

### 6.A.1 Proof of Lemma 29

The ﬁrst part follows by integration of a pointwise result. Consider the function ℎ𝑝: R →R; 𝑞↦→ 𝑝(1 −𝑞)+ + (1 −𝑝)(1 + 𝑞)+, where 𝑝∈(0, 1) represents P(𝑌= 1|𝑋) and 𝑞represents 𝑔(𝑥). The function ℎ𝑝has a slope equal to −𝑝for 𝑞< −1, then slope 1 −2𝑝for 𝑞∈(−1, 1), and 1 −𝑝for 𝑞> 1. Therefore, when 𝑞1, 𝑞2 ∈(−1, 1), we have

$$
ℎ𝑝(𝑞2) −ℎ𝑝(𝑞1) = (1 −2𝑝)(𝑞2 −𝑞1).
$$

Taking 𝑝= P(𝑌= 1|𝑋), 𝑞2 = 𝑔2(𝑋) and 𝑞1 = 𝑔1(𝑋), we get 1 −2𝑝= −E[𝑌|𝑋] = −𝜂(𝑋). By integration, we obtain the claim. From the previous slope considerations, it also follows that ℎ𝑝is minimized by 𝑞= sign(2𝑝−1), meaning that one can take 𝑔∗(𝑋) = sign 𝜂(𝑋).

The second part follows from the fact that projecting on [−1, 1] can only reduce the value of the hinge loss, that 𝜂(𝑥)(𝜋(𝑔)(𝑥) −𝑔∗(𝑥)) is always negative, and the reverse Hölder inequality:

$$
|𝜂|−1

−1
R𝑆(𝑔) −R(𝑔∗) ≥R𝑆(𝜋(𝑔)) −R(𝑔∗) = ∥𝜂(𝜋(𝑔) −𝑔∗)∥1 ≥∥𝜋(𝑔) −𝑔∗∥𝑞 𝑝.
$$

A Hölder inequality also holds for weak Lebesgue spaces (see Castillo and Rafeiro, 2016, Theorem 5.23), whence

$$
|𝜂|−1

−1
R𝑆(𝑔) −R(𝑔∗) ≥∥𝜂(𝜋(𝑔) −𝑔∗)∥1 ≥∥𝜂(𝜋(𝑔) −𝑔∗)∥1,∞≥1
𝑝,∞∥𝜋(𝑔) −𝑔∗∥ 𝑝 𝑝+1 ,∞.
2
$$

This completes the proof.

### 6.A.2 Proof of Lemma 31

Assume without restrictions that there exists 𝑥∈X1 such that |𝑔∗(𝑥) −𝑔(𝑥)| ≥1. For any event 𝐴= 𝐴(𝑋), by the law of total probability we have

$$
P(𝐴) = 𝜌X (X1) P (𝐴| 𝑋∈X1) + 𝜌X (X−1) P (𝐴| 𝑋∈X−1) ≥𝜌X (X1) P (𝐴| 𝑋∈X1) .
89
$$

<!-- page: 92 -->

Hence, since 𝑔∗(X1) = {1},

$$
∥𝑔−𝑔∗∥𝑞 𝑞,∞= sup 𝑡𝑞P(|𝑔(𝑋) −𝑔∗(𝑋)| > 𝑡) ≥sup 𝑡𝑞P (|𝑔(𝑋) −1| > 𝑡| 𝑋∈X1) 𝜌X (X1).
𝑡>0 𝑡>0
$$

Using the triangular inequality, the 𝐺-Lipschitz continuity of 𝑔, and the deﬁnition of 𝑥, we have that, for any 𝑥′ ∈X,

$$
|𝑔(𝑥′) −1| ≥|𝑔(𝑥) −1| −|𝑔(𝑥′) −𝑔(𝑥)| ≥1 −𝐺𝑑(𝑥, 𝑥′).
$$

As a consequence,

$$
𝜌X X1 ∩B 𝑥, 1−𝑡
𝑥, 1 −𝑡
P (|𝑔(𝑋) −1| > 𝑡| 𝑋∈X1) ≥P 𝐺
𝑋∈B | 𝑋∈X1 = 𝜌X (X1) .
𝐺
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Combined with the previous facts, we get

$$
𝑥, 1 −𝑡
∥𝑔−𝑔∗∥𝑞 𝑞,∞≥sup 𝑡𝑞𝜌X X1 ∩B .
𝑡>0 𝐺
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Thanks to Assumption 12, there exists (𝑐, 𝑟, 𝑑) such that (6.14) holds for X1. Hence, when 𝐺−1 < 𝑟, we get the following lower bound:

$$
𝑡𝑞(1 −𝑡)𝑑= 𝑐𝐺−𝑑 𝑞𝑞𝑑𝑑
∥𝑔−𝑔∗∥𝑞 𝑞,∞≥𝑐𝐺−𝑑sup (𝑑+ 𝑞)𝑑+𝑞.
𝑡∈[0,1]
$$

This proves the statement in the lemma.

### 6.A.3 Proof of Proposition 32

Suppose R(sign 𝑔) > R( 𝑓∗). Then, observing that sign(𝜋(𝑡)) = sign(𝑡) for all 𝑡∈R, and taking 𝑔∗= 𝑓∗, we know there must be 𝑥∈supp 𝜌X such that |𝜋(𝑔(𝑥)) −𝑔∗(𝑥)| ≥1. Hence, by Lemma 31, we get

$$
𝑞

|𝜂|−1

−1
$$

∥𝜋(𝑔) −𝑔∗∥𝑞,∞≥𝑐0𝐺−𝑑 𝑞, and therefore, by Lemma 29, R𝑆(𝑔) −R𝑆(𝑔∗) ≥2−1𝑐0𝐺−𝑑 𝑝,∞. Thus, the proposition is proved.

### 6.A.4 Proof of Theorem 10

$$
𝑀𝐺𝜑𝜎−1, 𝑟−1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

From Proposition 32 and Assumption 13, we get, with ˜𝐿= max

$$
and 𝑞= 𝑝/𝑝+ 1,
 R𝑆(𝜋◦𝑔D𝑛) −R𝑆(𝑔∗) ≥2−1 

|𝜂|−1

−1 
ED𝑛[R(sign 𝑔D𝑛)] −R( 𝑓∗) ≤PD𝑛 𝑝,∞𝑐0 ˜𝐿−𝑑
 𝑞 
R𝑆(𝜋◦𝑔D𝑛) −R𝑆(𝑔𝑀,𝜎) ≥4−1 

|𝜂|−1

−1
≤PD𝑛 𝑝,∞𝑐0 ˜𝐿−𝑑
𝑞 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

To deal with this last quantity, we proceed by usign the fact that

$$
R𝑆,D𝑛(𝜋◦𝑔D𝑛) ≤R𝑆,D𝑛(𝑔D𝑛) ≤R𝑆,D𝑛(𝑔𝑀,𝜎),
$$

where R𝑆,D𝑛denotes the empirical surrogate risk, to deduce that

$$
R𝑆(𝜋◦𝑔D𝑛) −R𝑆(𝑔𝑀,𝜎) ≤R𝑆(𝜋◦𝑔D𝑛) −R𝑆,D𝑛(𝜋◦𝑔D𝑛) + R𝑆,D𝑛(𝑔𝑀,𝜎) + R𝑆(𝑔𝑀,𝜎).
$$

Hence, we get the following union bound

$$
R𝑆(𝜋◦𝑔D𝑛) −R𝑆,D𝑛(𝑔D𝑛) ≥8−1 

|𝜂|−1

−1 
ED𝑛[R(sign 𝑔D𝑛)] −R( 𝑓∗) ≤PD𝑛 𝑝,∞𝑐0 ˜𝐿−𝑑
 𝑞 
R𝑆(𝜋◦𝑔𝑀,𝜎) −R𝑆,D𝑛(𝑔𝑀,𝜎) ≥8−1 

|𝜂|−1

−1
+ PD𝑛 𝑝,∞𝑐0 ˜𝐿−𝑑
𝑞 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Regarding the ﬁrst term, we can reuse the literature on Rademacher complexity for linear models on convex risks (Bartlett and Mendelson, 2002), which ensures that

$$
" #
R𝑆(𝜋◦𝑔) −R𝑆,D𝑛(𝜋◦𝑔)
ED𝑛 sup 𝑔∈G𝑀,𝜎 ≤𝑀∥𝜑∥∞𝑛−1/2.
$$

<!-- page: 93 -->

6.B. EXPERIMENTAL DETAILS 91 Note that Assumption 12 implies that supp 𝜌X is compact, hence, if 𝜑is Lipschitz-continuous, it is bounded on supp 𝜌X . This allows us to use McDiarmid inequality to get the same type of bound on the deviation of R𝑆(𝑔D𝑛) around its mean. Let 𝐻(D𝑛) = sup𝑔∈G𝑀,𝜎R𝑆(𝜋◦𝑔) −RD𝑛(𝜋◦𝑔). Let us decompose D𝑛= ((𝑥1, 𝑦1), · · · , (𝑥𝑛, 𝑦𝑛)). We would like to show that if D′ 𝑛is equal to D𝑛for each datapoint but for (𝑥𝑖, 𝑦𝑖) that becomes (𝑥′

$$
𝑖, 𝑦′ 𝑖) then 𝐻(D𝑛) −𝐻(D′ 𝑛) is bounded. We have
𝐻(D𝑛) −𝐻(D′ 𝑛) = sup 𝑔∈G𝑀,𝜎 R𝑆(𝜋◦𝑔) −R𝑆,D𝑛(𝜋◦𝑔) − sup 𝑔′∈G𝑀,𝜎 R𝑆(𝜋◦𝑔′) −R𝑆,D′𝑛(𝜋◦𝑔′)
≤ sup 𝑔∈G𝑀,𝜎 R𝑆,D𝑛(𝜋◦𝑔) −R𝑆,D′𝑛(𝜋◦𝑔)
= 𝑛−1 sup 𝑖) −𝐿(𝜋◦𝑔(𝑥𝑖), 𝑦𝑖) ≤𝑛−1
𝐿(𝜋◦𝑔(𝑥′ 𝑖), 𝑦′
𝑔∈G𝑀,𝜎
$$

Using McDiarmid’s inequality, we get

$$
P(𝐻(D𝑛) −E[𝐻(D𝑛)] ≥𝑡) ≤exp(−2𝑛𝑡2).
$$

In other terms, when adding the control we have on the expectation, we get

$$
!
 −2𝑛𝑡2 
PD𝑛 sup 𝑔∈G𝑀,𝜎 R𝑆(𝜋◦𝑔) −R𝑆,D𝑛(𝜋◦𝑔) > 𝑡+ 𝑀∥𝜑∥∞𝑛−1/2 ≤exp . (6.22)
$$

(6.22)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

When 8−1 

|𝜂|−1

−1

$$
𝑝,∞𝑐0 ˜𝐿−𝑑 𝑞≥∥𝜑∥∞𝑀𝑛−1/2, this leads to
 R𝑆(𝜋◦𝑔D𝑛) −R𝑆,D𝑛(𝑔D𝑛) ≥8−1 

|𝜂|−1

−1 
PD𝑛 𝑝,∞𝑐0 ˜𝐿−𝑑
 𝑞−𝑀∥𝜑∥∞𝑛−1/2 2 𝑞
 8−1 

|𝜂|−1

−1 𝑝,∞𝑐0 ˜𝐿−𝑑
−𝑛
≤exp
8
©­­ « 𝑐2 2𝑑(𝑝+1) 𝑝 ª®® ¬
0𝜎 · 𝑛+ 𝑐0 ∥𝜑∥∞ · 𝑛−1/2 −𝑀2 ∥𝜑∥2 ∞ 8
≤exp − 512 |𝜂|−1

2 32 |𝜂|−1 .
2𝑑(𝑝+1) 𝑝 𝑑(𝑝+1) 𝑑(𝑝+1)
𝑝,∞(𝑀𝐺𝜑) 𝑝 −1𝐺 𝑝 𝜑
𝑝,∞𝑀
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Regarding the second term, we can use classical concentration of RD𝑛(𝑔𝑀,𝜎) around its mean. For example, using the fact that Assumption 12 implies that 𝜌X is compact, and using the fact that 𝐿and 𝑔𝜎,𝑀 are Lipschitz, we deduce that 𝐿(𝑔𝜎,𝑀,𝑌) is bounded, hence one can applies Hoeﬀding’s inequality to get the same type of exponential control on this term.

The result follows form those concentration inequality and the fact that R is bounded by one and that any min(1, 𝑎exp(−𝑏𝑛)) for 𝑎, 𝑏> 0 and 𝑛> 1 can be bounded by exp(−𝑐𝑛) for a 𝑐> 0).

## 6.B Experimental details

In our experiments, we used the SVM implementation of Chang and Lin (2011) through its Scikit-learn wrapper (Pedregosa et al., 2011) in Python. We used Numpy (Harris et al., 2020) to reduce our work to high-level array instructions, and Matplotlib for visualization (Hunter, 2007). Randomness in experiments was controlled with the random seed provided by Numpy, which we initialized at zero.

Figures 6.2 and 6.5 are derived by averaging 100 trials of the following procedure. We draw uniformly at random 𝑛independent samples uniformly distributed on X ∈{[−1, 1], [−1, −.1] ∪[.1, 1]}. We draw randomly one output 𝑦𝑖for each input 𝑥𝑖, according to 𝜂(𝑥𝑖). We consider the Gaussian kernel 𝑘(𝑥, 𝑥′) = exp(−∥𝑥−𝑥′∥2 /2𝜎2) for 𝜎= .2, and solve the empirical risk minimization associated to the hinge loss with the penalization 𝜆∥𝜃∥2 (rather than the hard constraint ∥𝜃∥< 𝑀) for 𝜆= 10−4. The generalization error is measured through the formula E[∥𝜂(𝑥)∥1 𝑓(𝑥)≠𝑓∗(𝑥)], with an empirical approximation of this sum with the points (𝑥𝑖)𝑖≤𝑛chosen such that 𝜌X ([𝑥𝑖, 𝑥𝑖+1]) = 1/𝑛and 𝜌X ([𝑥𝑛, +∞)) = 1/𝑛, with 𝑛= 104 (which makes sure that the exponential behavior observed is not due to the lack of testing samples). For each 𝑥, the height of each dark part corresponds to one standard deviation of the generalization error computed from the 100 trials, and the solid line corresponds to the empirical average. The fact that the dark parts are not centered around the averages is due to the fact that we have drawn log-plots but centered the interval for linearly-scaled plots.

<!-- page: 94 -->

10−1 p=.1 p=.3 p=1 p=3 10−1 Excess of risk Excess of risk 10−2 10−3 p=.1 p=.3 p=1 p=3 10−3 101 102 103 101 102 103 Samples size Samples size

[FIGURE: Figure 6.5]

Figure 6.5: (Left) Similar setting as Figure 6.2 but with 𝑋uniform on [−1, 1]. The behavior of the excess of risk is quite diﬀerent without the separation in X: no exponential convergence rate is kicking in after a thousand of samples. (Right) Similar setting as Figure 6.2, using kernel ridge regression with the least-squares surrogate. Exponential convergence rates are observed with a slight delay compared to the hinge loss, and are explained by the hard-margin condition 10.

Figure 6.3 is obtained by considering X = [0, 1]2 with uniform input distribution, the Gaussian kernel with 𝜎= .2, and the penalty parameter 𝜆= 10−3 (instead of a hard constraint leading to a parameter 𝑀as in the main text derivations). We take 𝑛= 104 = 1002 points uniformly spread out on X (on the regular lattice 1 √𝑛· Z2 ∩X) to approximate 𝑔𝜆,𝜎with empirical risk minimization on this curated dataset. We consider 𝜂(𝑥) = 𝜋[−1,1](2𝑥2 −.5 sin(2𝜋𝑥1) −1), and assign to each 𝑥in the dataset a sample (𝑥, 1) weighted by P (𝑌= 1 | 𝑋= 𝑥) = (𝜂(𝑥) −1)/2, and a sample (𝑥, −1), weighted by P (𝑌= −1 | 𝑋= 𝑥). The “noiseless” setting denotes the setting where (𝑌| 𝑋) is deterministic, but with the same decision frontier between the classes X1 and X−1 characterized by {(𝑥, .5 + .25 sin(2𝜋𝑥)) | 𝑥∈[0, 1]}. Once we ﬁt the support vector machine with this dataset, we test it with 𝑛= 2.5 · 105 = 5002 data points uniformly spread out on X, and use Matplotlib to automatically draw level lines.

$$
SVM bias: gλ,σ Least-square bias
1 1
0 0
−1
−1
SVM bias: gλ,σ Least-square bias
1
1
0 0
−1
−1
$$

[FIGURE: Figure 6.6]

Figure 6.6: Same setting as Figure 6.4, with 𝜎= .2 and 𝜆= 10−6 (top), and with 𝜎= 1 and 𝜆= 10−3 (bottom).

Figures 6.4 and 6.6 correspond to X = [0, 3] with the input distribution uniform on [0, 1] ∪[2, 3]. Figure 6.4 is obtained with 𝜎= .1 and 𝜆= 10−6. We derive it by considering 𝑛= 100 points uniformly spread out on the domain of 𝜂, solving the equivalent curated empirical risk minimization, that approximates

<!-- page: 95 -->

6.B. EXPERIMENTAL DETAILS 93 both

$$
D 𝑥 E
𝑔𝜆,𝜎= arg min E𝜌[(0, 1 −𝑌 )+] + 𝜆∥𝜃∥2 , (6.23)
𝜃, 𝜑
𝑔:X→R 𝜎
D 𝑥 E
2 ] + 𝜆∥𝜃∥2 . (6.24)
𝑔(LS) = arg min E𝜌[ 𝜃, 𝜑 −𝑌
𝑔:X→R 𝜎
$$

(6.24)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The robustness of SVM might be understood from its geometrical deﬁnition: when trying to ﬁnd the maximum separating margin, inﬁnitesimal modiﬁcations that change the regularity properties of 𝜂do not really matter. The picture is diﬀerent for the least-squares surrogate with kernel methods, where from few point evaluations, the system reconstructs a function by assuming regularity and inferring information on high-order derivatives. This is similar to the Runge phenomenon with Hermite interpolation. More precisely, the Gaussian kernel is linked to a space of functions with rapidly decreasing Fourier coeﬃcients (see, for example, Bach, 2023, for a more precise link). The function 𝜂that needs to be approximated on Figure 6.4 is similar to the Heaviside function, whose Fourier coeﬃcients are of the form ( 1 𝑖𝜋𝑘)𝑘∈N∗and do not decrease fast enough to be all reconstructed. This leads to some high-frequency oscillations missing in the reconstruction as it appears on Figure 6.4.

<!-- page: 96 -->

<!-- page: 97 -->

# Part III. Learning with Partial Supervision

95

<!-- page: 98 -->

<!-- page: 99 -->

# Chapter 7. Inﬁmum Loss

The following is a reproduction of Cabannes et al. (2020b).

Annotating datasets is one of the main costs nowadays in supervised learning. The goal of weak supervision is to enable models to learn while using only forms of labeling which are cheaper to collect, as partial labeling. This is a type of incomplete annotation where, for each data point, supervision is cast as a set of labels containing the real one. The problem of supervised learning with partial labeling has been studied for speciﬁc instances such as classiﬁcation, multi-label, ranking or segmentation, but a general framework is still missing. This paper provides a uniﬁed framework based on structured prediction and on the concept of inﬁmum loss to deal with partial labeling over a wide family of learning problems and loss functions. The framework leads naturally to explicit algorithms that can be easily implemented and for which proved statistical consistency and learning rates. Experiments conﬁrm the superiority of the proposed approach over commonly used baselines.

## 7.1 Introduction

Fully supervised learning demands tight supervision of large amounts of data, a supervision that can be quite costly to acquire and constrains the scope of applications. To overcome this bottleneck, the machine learning community is seeking to incorporate weaker sources of information in the learning framework. In this paper, we address those limitations through partial labeling: e.g., giving only partial ordering when learning user preferences over items, or providing the label “ﬂower” for a picture of Arum Lilies, instead of spending a consequent amount of time to ﬁnd the exact taxonomy.

Partial labeling has been studied in the context of classiﬁcation (Cour et al., 2011; Nguyen and Caruana, 2008), multilabeling (Yu et al., 2014), ranking (Hüllermeier et al., 2008; Korba et al., 2018), as well as segmentation (Verbeek and Triggs, 2008; Papandreou et al., 2015), however a generic framework is still missing. Such a framework is a crucial step toward understanding how to learn from weaker sources of information, and widening the spectrum of machine learning beyond rigid applications of supervised learning. Some interesting directions are provided by Cid-Sueiro et al. (2014); van Rooyen and Williamson (2017), to recover the information lost in a corrupt acquisition of labels. Yet, they assume that the corruption process is known, which is a strong requirement that we want to relax.

In this paper, we make the following contributions:

• We provide a principled framework to solve the problem of learning with partial labeling, via structured prediction. This approach naturally leads to a variational framework built on the inﬁmum loss. • We prove that the proposed framework is able to recover the original solution of the supervised learning problem under identiﬁability assumptions on the labeling process. • We derive an explicit algorithm which is easy to train and with strong theoretical guarantees. In particular, we prove that it is consistent, and we provide generalization error rates. • Finally, we test our method against some simple baselines, on synthetic and real examples. We show that for certain partial labeling scenarios with symmetries, our inﬁmum loss performs similarly to a simple baseline. However, in scenarios where the acquisition process of the labels is more adversarial in nature, the proposed algorithm performs consistently better.

97

<!-- page: 100 -->

## 7.2 Partial labeling with inﬁmum loss

In this section, we introduce a statistical framework for partial labeling, and we show that it is characterized naturally in terms of risk minimization with the inﬁmum loss. First, let’s recall some elements of fully supervised and weakly supervised learning.

Fully supervised learning consists in learning a function 𝑓∈YX between an input space X and an output space Y, given a joint distribution 𝜌∈ΔX×Y on X × Y, and a loss function ℓ∈RY×Y, that minimizes the risk

$$
R( 𝑓; 𝜌) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] , (7.1)
$$

(7.1)

given observations (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛∼𝜌⊗𝑛. We will assume that the loss ℓis proper, i.e. it is continuous non- negative and is zero on, and only on, the diagonal of Y × Y, and strictly positive outside. We will also assume that Y is compact.

In weakly supervised learning, given (𝑥𝑖)𝑖≤𝑛, one does not have direct observations of (𝑦𝑖)𝑖≤𝑛but weaker information. The goal is still to recover the solution 𝑓∈YX of the fully supervised problem (7.1). In partial labeling, also known as superset learning or as learning with ambiguous labels, which is an instance of weak supervision, information is cast as closed sets (𝑆𝑖)𝑖≤𝑛in S, where S ⊂2Y is the space of closed subsets of Y, containing the true labels (𝑦𝑖∈𝑆𝑖). In this paper, we model this scenario by considering a data distribution 𝜏∈ΔX×S, that generates the samples (𝑥𝑖, 𝑆𝑖). We will denote 𝜏as weak distribution to distinguish it from 𝜌. Capturing the dependence on the original problem, 𝜏must be compatible with 𝜌, a matching property that we formalize with the concept of eligibility.

Deﬁnition 33 (Eligibility). Given a probability measure 𝜏on X × S, a probability measure 𝜌on X × Y is said to be eligible for 𝜏(denoted by 𝜌⊢𝜏), if there exists a probability measure 𝜋over X × Y × S such that 𝜌is the marginal of 𝜋over X × Y, 𝜏is the marginal of 𝜋over X × S, and, for 𝑦∈Y and 𝑆∈S

$$
𝑦∉𝑆 ⇒ P𝜋(𝑆| 𝑌= 𝑦) = 0.
$$

We will alternatively say that 𝜏is a weakening of 𝜌, or that 𝜌and 𝜏are compatible.

### 7.2.1 Disambiguation principle

According to the setting described above, the problem of partial labeling is completely deﬁned by a loss and a weak distribution (ℓ, 𝜏). The goal is to recover the solution of the original supervised learning problem in (7.1) assuming that the original distribution veriﬁes 𝜌⊢𝜏. Since more than one 𝜌may be eligible for 𝜏, we would like to introduce a guiding principle to identify a 𝜌★among them. With this goal we deﬁne the concept of non-ambiguity for 𝜏, a setting in which a natural choice for 𝜌★appears.

Deﬁnition 34 (Non-ambiguity). For any 𝑥∈X, denote by 𝜏|𝑥the conditional probability of 𝜏given 𝑥, and deﬁne the set 𝑆𝑥as

$$
𝑆𝑥= \frac{Ù}{𝑆∈supp(𝜏|𝑥)} 𝑆.
$$

The weak distribution 𝜏is said non-ambiguous if, for every 𝑥∈X, 𝑆𝑥is a singleton. Moreover, we say that 𝜏 is strictly non-ambiguous if it is non-ambiguous and there exists 𝜂∈(0, 1) such that, for all 𝑥∈X and 𝑧∉𝑆𝑥

$$
P𝑆∼𝜏|𝑥(𝑧∈𝑆) ≤1 −𝜂.
$$

This concept is similar to the one by Cour et al. (2011), but more subtle because this quantity only depends on 𝜏, and makes no assumption on the original distribution 𝜌describing the fully supervised process that we can not access. In this sense, it is also more general.

When 𝜏is non-ambiguous, we can write 𝑆𝑥= {𝑦𝑥} for any 𝑥, where 𝑦𝑥is the only element of 𝑆𝑥. In this case it is natural to identify 𝜌★as the one satisfying 𝜌★|𝑥= 𝛿𝑦𝑥. Actually, such a 𝜌★is characterized without 𝑆𝑥as the only deterministic distribution that is eligible for 𝜏. Because deterministic distributions are characterized as minimizing the minimum risk (7.1), we introduce the following minimum variability principle to disambiguate between all eligible 𝜌’s, and identify 𝜌★,

$$
𝜌★∈arg min E(𝜌), E(𝜌) = inf 𝑓:X→Y R( 𝑓; 𝜌). (7.2)
𝜌⊢𝜏
$$

(7.2)

<!-- page: 101 -->

The quantity E can be identiﬁed as a variance, since if 𝑓𝜌is the minimizer of R( 𝑓; 𝜌), 𝑓𝜌(𝑥) can be seen as the mean of 𝜌|𝑥and ℓthe natural distance in Y. Indeed, when ℓ= ℓ2 is the mean square loss, this is exactly the case. The principle above recovers exactly 𝜌★|𝑥= 𝛿𝑦𝑥, when 𝜏is non-ambiguous, as stated by Theorem 35, proven in Appendix 7.A.1.

Proposition 35 (Non-ambiguity determinism). When 𝜏is non-ambiguous, the solution 𝜌★(7.2) exists and satisﬁes that, for any 𝑥∈X, 𝜌★|𝑥= 𝛿𝑦𝑥, where 𝑦𝑥is the only element of 𝑆𝑥.

Proposition 35 provides a justiﬁcation for the usage of the minimum variability principle. Indeed, under non-ambiguity assumption, following this principle will allow us to build an algorithm that recovers the original fully supervised distribution. Therefore, given samples (𝑥𝑖, 𝑆𝑖), it is of interest to test if 𝜏is non-ambiguous. Such tests should leverage other regularity hypotheses on 𝜏, which we will not address in this work.

Now, we characterize the minimum variability principle in terms of a variational optimization problem that we can tackle in Section 7.3 via empirical risk minimization.

### 7.2.2 Variational formulation via the inﬁmum loss

Given a partial labeling problem (ℓ, 𝜏), deﬁne the solutions based on the minimum variability principle as the functions minimizing the recovered risk

$$
𝑓∗∈arg min R( 𝑓; 𝜌★). (7.3)
𝑓:X→Y
$$

(7.3)

for 𝜌★a distribution solving (7.2). As shown in Theorem 11 below, proven in Appendix 7.A.2, the proposed disambiguation paradigm naturally leads to a variational framework involving the inﬁmum loss.

Theorem 11 (Inﬁmum loss (IL)). The functions 𝑓∗deﬁned in (7.3) are characterized as

$$
\underset{𝑓:X→Y}{\arg\min}\, R𝑆( 𝑓),
$$

where the risk R𝑆is deﬁned as

$$
R𝑆( 𝑓) = E(𝑋,𝑆)∼𝜏[𝐿( 𝑓(𝑋), 𝑆)] , (7.4)
$$

(7.4)

and 𝐿is the inﬁmum loss

$$
𝐿(𝑧, 𝑆) = inf 𝑦∈𝑆ℓ(𝑧, 𝑦). (7.5)
$$

(7.5)

The inﬁmum loss, also known as the ambiguous loss (Luo and Orabona, 2010; Cour et al., 2011), or as the optimistic superset loss (Hüllermeier, 2014), captures the idea that, when given a set 𝑆, this set contains the good label 𝑦but also a lot of bad ones, that should not be taken into account when retrieving 𝑓. In other terms, 𝑓should only match the best guess in 𝑆. Indeed, if ℓis seen as a distance, 𝐿is its natural extension to sets.

### 7.2.3 Recovery of the fully supervised solutions

In this subsection, we investigate the setting where an original fully supervised learning problem 𝜌0 has been weakened due to incomplete labeling, leading to a weak distribution 𝜏. The goal here is to understand under which conditions on 𝜏and ℓit is possible to recover the original fully supervised solution based on the inﬁmum loss framework. Denote 𝑓0 the function minimizing R( 𝑓; 𝜌0). The theorem below, proven in Appendix 7.A.3, shows that under non-ambiguity and deterministic conditions, it is possible to fully recover the function 𝑓0 also from 𝜏.

Theorem 12 (Supervision recovery). For an instance (ℓ, 𝜌0, 𝜏) of the weakened supervised problem, if we denote by 𝑓0 the minimizer of (7.1), we have the under the conditions that (1) 𝜏is not ambiguous (2) for all 𝑥∈X, 𝑆𝑥= { 𝑓0(𝑥)}; the inﬁmum loss recovers the original fully supervised solution, i.e. the 𝑓∗deﬁned in (7.3) veriﬁes 𝑓∗= 𝑓0.

Furthermore, when 𝜌0 is deterministic and 𝜏not ambiguous, the 𝜌★deﬁned in (7.2) veriﬁes 𝜌★= 𝜌0.

At a comprehensive level, this theorem states that under non-ambiguity of the partial labeling process, if the labels are a deterministic function of the inputs, the inﬁmum loss framework makes it possible to recover the solution of the original fully supervised problem while only accessing weak labels. In the next subsection, we will investigate which is the relation between the two problems when dealing with an estimator 𝑓of 𝑓∗.

<!-- page: 102 -->

### 7.2.4 Comparison inequality

In the following, we want to characterize the error performed by R( 𝑓; 𝜌★) with respect to the error performed by R𝑆( 𝑓). This will be useful since, in the next section, we will provide an estimator for 𝑓∗based on structured prediction, that minimizes the risk R𝑆. First, we introduce a measure of discrepancy for the loss function.

Deﬁnition 36 (Discrepancy of the loss ℓ). Given a loss function ℓ, the discrepancy degree 𝜈of ℓis deﬁned as

$$
\frac{𝜈= log sup}{𝑦,𝑧′≠𝑧} \frac{ℓ(𝑧, 𝑦)}{ℓ(𝑧, 𝑧′) .}
$$

Y will be said discrete for ℓwhen 𝜈< +∞, which is always the case when Y is ﬁnite.

Now we are ready to state the comparison inequality that generalizes a result on classiﬁcation with the 0 −1 loss from Cour et al. (2011) to arbitrary losses and output spaces.

Proposition 37 (Comparison inequality). When Y is discrete and 𝜏is strictly non-ambiguous for a given 𝜂∈(0, 1), then the following holds

$$
R( 𝑓; 𝜌★) −R( 𝑓∗; 𝜌★) ≤𝐶(R𝑆( 𝑓) −R𝑆( 𝑓∗)), (7.6)
$$

(7.6)

for any measurable function 𝑓∈YX , where 𝐶does not depend on 𝜏, 𝑓, and is deﬁned as follows and always ﬁnite

$$
𝐶= 𝜂−1𝑒𝜈.
$$

When 𝜌0 is deterministic, since we know from Theorem 12 that 𝜌★= 𝜌0, this theorem allows bounding the error made on the original fully supervised problem with the error measured with the inﬁmum loss on the weakly supervised one.

Note that the constant presented above is the product of two independent terms, the ﬁrst measuring the ambiguity of the weak distribution 𝜏, and the second measuring a form of discrepancy for the loss. In the appendix, we provide a more reﬁned bound for 𝐶, that is 𝐶= 𝐶(ℓ, 𝜏), that shows a more elaborated interaction between ℓand 𝜏. This may be interesting in situations where it is possible to control the labeling process and may suggest strategies to active partial labeling, with the goal of minimizing the costs of labeling while preserving the properties presented in this section and reducing the impact of the constant 𝐶in the learning process. An example is provided in the Appendix 7.A.5.

## 7.3 Consistent algorithm for partial labeling

In this section, we provide an algorithmic approach based on structured prediction to solve the weak supervised learning problem expressed in terms of inﬁmum loss from Theorem 11. From this viewpoint, we could consider diﬀerent structured prediction frameworks as structured SVM (Tsochantaridis et al., 2005), conditional random ﬁelds (Laﬀerty et al., 2001) or surrogate mean estimation (Ciliberto et al., 2016). For example, Luo and Orabona (2010) used a margin maximization formulation in a structured SVM fashion, Hüllermeier and Cheng (2015) went for nearest neighbors, and Cour et al. (2011) design a surrogate method speciﬁc to the 0-1 loss, for which they show consistency based on Bartlett et al. (2006).

In the following, we will use the structured prediction method of Ciliberto et al. (2016); Nowak-Vila et al. (2019), which allows us to derive an explicit estimator, easy to train and with strong theoretical properties, in particular, consistency and ﬁnite sample bounds for the generalization error. The estimator is based on the pointwise characterization of 𝑓∗as

$$
\underset{𝑧∈Y}{\arg\min}\, E𝑆∼𝜏|𝑥 inf_{𝑦∈𝑆ℓ(𝑧, 𝑦)} ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

and weights 𝛼𝑖(𝑥) that are trained on the dataset such that ˆ𝜏|𝑥= Í𝑛 𝑖=1 𝛼𝑖(𝑥)𝛿𝑆𝑖is a good approximation of 𝜏|𝑥. Plugging this approximation in the precedent equation leads to our estimator, that is deﬁned explicitly as follows

$$
𝑛 ∑︁
𝑓𝑛(𝑥) ∈arg min inf 𝑦𝑖∈𝑆𝑖 𝛼𝑖(𝑥)ℓ(𝑧, 𝑦𝑖). (7.7)
𝑧∈Y 𝑖=1
$$

(7.7)

<!-- page: 103 -->

Among possible choices for 𝛼, we will consider the following kernel ridge regression estimator to be learned at training time

$$
𝛼(𝑥) = (𝐾+ 𝑛𝜆)−1𝑣(𝑥),
$$

with 𝜆> 0 a regularizer parameter and 𝐾= (𝑘(𝑥𝑖, 𝑥𝑗))𝑖,𝑗∈R𝑛×𝑛, 𝑣(𝑥) = (𝑘(𝑥, 𝑥𝑖))𝑖∈R𝑛where 𝑘∈X × X →R is a positive-deﬁnite kernel (Scholkopf and Smola, 2001) that deﬁnes a similarity function between input points (e.g., if X = R𝑑for some 𝑑∈N a commonly used kernel is the Gaussian kernel 𝑘(𝑥, 𝑥′) = 𝑒−∥𝑥−𝑥′ ∥2). Other choices can be done to learn 𝛼, beyond kernel methods, a particularly appealing one is harmonic functions, incorporating a prior on low density separation to boost learning (Zhu et al., 2003; Zhou et al., 2003; Bengio et al., 2006). Here we use the kernel estimator since it allows deriving strong theoretical results, based on kernel conditional mean estimation (Muandet et al., 2017).

### 7.3.1 Theoretical guarantees

In this following, we want to prove that 𝑓𝑛converges to 𝑓∗as 𝑛goes to inﬁnity, and we want to quantify it with ﬁnite sample bounds. The intuition behind this result is that as the number of data points tends toward inﬁnity, ˆ𝜏concentrates toward 𝜏, making our algorithm in (7.7) converging to a minimizer of (7.4) as explained more in detail in Appendix 7.A.6.

Theorem 13 (Consistency). Let Y be ﬁnite and 𝜏be a non-ambiguous probability. Let 𝑘be a bounded continuous universal kernel, e.g. the Gaussian kernel (see Micchelli et al., 2006, for details), and 𝑓𝑛the estimator in (7.7) trained on 𝑛∈N examples and with 𝜆= 𝑛−1/2. Then, holds with probability 1

$$
\frac{𝑛→∞R( 𝑓𝑛; 𝜌★) = R( 𝑓∗; 𝜌★).}{lim}
$$

In the next theorem, instead we want to quantify how fast 𝑓𝑛converges to 𝑓∗depending on the number of examples. To obtain this result, we need a ﬁner characterization of the inﬁmum loss 𝐿as:

$$
𝐿(𝑧, 𝑆) = ⟨𝜓(𝑧), 𝜑(𝑆)⟩,
$$

where H is a Hilbert space and 𝜓: Y →H, 𝜑: 2Y →H are suitable maps. Such a decomposition always exists in ﬁnite case (as for the inﬁmum loss over Y ﬁnite) and many explicit examples for losses of interest are presented by Nowak-Vila et al. (2019). We now introduce the conditional expectation of 𝜑(𝑆) given 𝑥, deﬁned as

$$
𝑔: \frac{X}{𝑥} \frac{→}{→} \frac{H}{E𝜏[𝜑(𝑆) | 𝑋= 𝑥] .}
$$

The idea behind the proof is that the distance between 𝑓𝑛and 𝑓is bounded by the distance of 𝑔𝑛an estimator of 𝑔that is implicitly computed via 𝛼. If 𝑔has some form of regularity, e.g. 𝑔∈G, with G the space of functions representable by the chosen kernel (see Scholkopf and Smola, 2001), then it is possible to derive explicit rates, as stated in the following theorem.

Theorem 14 (Convergence rates). In the setting of Theorem 13, if 𝜏is 𝜂-strictly non-ambiguous for 𝜂∈(0, 1), and if 𝑔∈G, then there exists a ˜𝐶, such that, for any 𝛿∈(0, 1) and 𝑛∈N, holds with probability at least 1 −𝛿,

$$
8 2
R( 𝑓𝑛; 𝜌★) −R( 𝑓∗; 𝜌★) ≤˜𝐶log 𝑛−1/4. (7.8)
𝛿
$$

(7.8)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Those last two theorem are proven in Appendix 7.A.6 and combines the consistency and learning results for kernel ridge regression (Caponnetto and De Vito, 2006; Smale and Zhou, 2007), with a comparison inequality of Ciliberto et al. (2016) which relates the excess risk of the structured prediction problem with the one of the surrogate loss R𝑆, together with our Theorem 37, which relates the error R to R𝑆.

Those results make our algorithm the ﬁrst algorithm for partial labeling that, to our knowledge, is applicable to a generic loss ℓand has strong theoretical guarantees as consistency and learning rates. In the next section we will compare with the state of the art and other variational principles.

<!-- page: 104 -->

## 7.4 Previous works and baselines

Partial labeling was ﬁrst approached through discriminative models, proposing to learn (𝑌| 𝑋) among a family of parametrized distributions by maximizing the log likelihood based on expectation-maximization scheme (Jin and Ghahramani, 2002), eventually integrating knowledge on the partial labeling process (Grandvalet, 2002; Papandreou et al., 2015). In the meanwhile, some applications of clustering methods have involved special instances of partial labeling, like segmentation approached with spectral method (Weiss, 1999), semi- supervision approached with max-margin (Xu et al., 2004). Also, initially geared toward clustering, Bach and Harchaoui (2007) considered the inﬁmum principle on the mean square loss, and this was generalized to weakly supervised problems (Joulin et al., 2010). The inﬁmum loss as an objective to minimize when learning from partial labels was introduced by Cour et al. (2011) for the classiﬁcation instance and used by Luo and Orabona (2010); Hüllermeier (2014) in generic cases. Compared to those last two, we provide a framework that derives the use of inﬁmum loss from ﬁrst principles and from which we derive an explicit and easy to train algorithm with strong statistical guarantees, which were missing in previous work. In the rest of the section, we will compare the inﬁmum loss with other variational principles that have been considered in the literature, in particular the supremum loss (Guillaume et al., 2017) and the average loss (Denoeux, 2013).

Average loss (AC). A simple loss to deal with uncertainty is to average over all potential candidates, assuming 𝑆discrete,

$$
\frac{𝐿ac(𝑧, 𝑆) = 1}{|𝑆|} \sum_{𝑦∈𝑆} ℓ(𝑧, 𝑦).
$$

It is equivalent to a fully supervised distribution 𝜌ac by sampling 𝑌uniformly at random among 𝑆

$$
𝜌ac(𝑦) = ∫ S \frac{1}{|𝑆| 1𝑦∈𝑆d𝜏(𝑆).}
$$

This directly follows from the deﬁnition of 𝐿ac and of the risk R(𝑧; 𝜌ac). However, as soon as the loss ℓhas discrepancy, i.e. 𝜈> 0, the average loss will implicitly advantage some labels, which can lead to inconsistency, even in the deterministic not ambiguous setting of Theorem 37 (see Appendix 7.A.7 for more details).

Supremum loss (SP). Another loss that has been considered is the supremum loss (Wald, 1945; Madry et al., 2018), bounding from above the fully supervised risk in (7.1). It is widely used in the context of robust risk minimization and reads

$$
\frac{𝑅sp( 𝑓) = sup}{𝜌⊢𝜏} E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑥), 𝑆)] .
$$

Similarly to the inﬁmum loss in Theorem 11, this risk can be written from the loss function

$$
\frac{𝐿sp(𝑧, 𝑆) = sup}{𝑦∈𝑆} ℓ(𝑧, 𝑦).
$$

Yet, this adversarial approach is not consistent for partial labeling, even in the deterministic non-ambiguous setting of Theorem 37, since it ﬁnds the solution that best agrees with all the elements in 𝑆and not only the true one (see Appendix 7.A.7 for more details).

### 7.4.1 Instance showcasing superiority of our method

In the rest of this section, we consider a pointwise example to showcase the underlying dynamics of the diﬀerent methods. It is illustrated in Figure 7.1. Consider Y = {𝑎, 𝑏, 𝑐} and a proper symmetric loss function such that ℓ(𝑎, 𝑏) = ℓ(𝑎, 𝑐) = 1, ℓ(𝑏, 𝑐) = 2. The simplex ΔY is naturally split into decision regions, for 𝑒∈Y,

$$
𝑅𝑒= 𝜌∈ΔY \underset{𝑧∈Y}{\arg\min}\, E𝜌[ℓ(𝑧,𝑌)] .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Both IL and AC solutions can be understood geometrically by looking at where 𝜌★and 𝜌ac fall in the partition of the simplex (𝑅𝑒)𝑒∈Y. Consider a fully supervised problem with distribution 𝛿𝑐, and a weakening 𝜏of 𝜌 deﬁned by 𝜏({𝑎, 𝑏, 𝑐}) = 5 8 and 𝜏({𝑐}) = 𝜏({𝑎, 𝑐}) = 𝜏({𝑏, 𝑐}) = 1 8. This distribution can be represented

<!-- page: 105 -->

$$
b b b b
𝑅𝑏
𝜌ac
𝑅𝑎 c 𝑅𝜏
𝑅𝑐 c
a c a 𝜌0 a c a
𝜌★
$$

[FIGURE: Figure 7.1]

Figure 7.1: Simplex ΔY. (Left) Decision frontiers. (Middle left) Full and weak distributions. (Middle right) Level curves of the piecewise linear objective E (7.2), to optimize when disambiguating 𝜏into 𝜌★. (Right) Disambiguation of AC and IL. on the simplex in terms of the region 𝑅𝜏= {𝜌∈ΔY | 𝜌⊢𝜏}. Finding 𝜌★correspond to minimizing the piecewise linear function E(𝜌) (7.2) inside 𝑅𝜏. On this example, it is minimized for 𝜌★= 𝛿𝑐, which we know from Theorem 37. Now note that if we use the average loss, it disambiguates 𝜌as

$$
𝜌ac(𝑐) = 11 24 = 1 3 5 8 + 1 8 + 2 · 1 2 1 8, 𝜌ac(𝑏) = 𝜌ac(𝑎) = 13
48.
$$

This distribution falls in the decision region of 𝑎, which is inconsistent with the real label 𝑦= 𝑐. For the supremum loss, one can show, based on Rsp(𝑎) = ℓ(𝑎, 𝑐) = 1, Rsp(𝑏) = ℓ(𝑏, 𝑐) = 2 and Rsp(𝑐) = 3/2, that the supremum loss is minimized for 𝑧= 𝑎, which is also inconsistent. Instead, by using the inﬁmum loss, we have 𝑓∗= 𝑓0 = 𝑐, and moreover that 𝜌★= 𝜌0 that is the optimal one.

### 7.4.2 Algorithmic considerations for AC, SP

The averaging candidates principle, approached with the framework of quadratic surrogates (Ciliberto et al., 2016), leads to the following algorithm

$$
𝑛 ∑︁ ∑︁
𝛼𝑖(𝑥) 1
𝑓ac(𝑥) ∈arg min ℓ(𝑧, 𝑦)
|𝑆𝑖|
𝑧∈Y 𝑖=1 𝑛 ∑︁ 𝑦∈𝑆𝑖 !
∑︁
1𝑦∈𝑆𝑖 𝛼𝑖(𝑥)
= arg min ℓ(𝑧, 𝑦).
|𝑆𝑖|
𝑧∈Y 𝑦∈Y 𝑖=1
$$

This estimator is computationally attractive because the inference complexity is the same as the inference complexity of the original problem when approached with the same structured prediction estimator. Therefore, one can directly reuse algorithms developed to solve the original inference problem (Nowak-Vila et al., 2019). Finally, with a similar approach to the one in Section 7.3, we can derive the following algorithm for the supremum loss

$$
\underset{𝑧∈Y}{\arg\min}\, sup_{𝑦𝑖∈𝑆𝑖} \sum_{𝑛 𝑖=1} 𝛼𝑖(𝑥)ℓ(𝑧, 𝑦𝑖).
$$

In the next section, we will use the average candidates as baseline to compare with the algorithm proposed in this paper, as the supremum loss consistently performs worth, as it is not ﬁtted for partial labeling.

## 7.5 Applications and experiments

In this section, we will apply (7.7) to some synthetic and real datasets from diﬀerent prediction problems and compared with the average estimator presented in the section above, used as a baseline. Code is available online.1 1https://github.com/VivienCabannes/partial_labelling

<!-- page: 106 -->

dna svmguide2 0.4 IL AC IL AC 0.4 Loss Loss 0.2 0.2 0 20 40 60 80 Corruption (in %) 0 20 40 60 80 Corruption (in %)

[FIGURE: Figure 7.2]

Figure 7.2: Classiﬁcation. Testing risks (from (7.1)) achieved by AC and IL on the “DNA” and “svmguide2” datasets from LIBSVM as a function of corruption parameter 𝑐, when the corruption is as follows: for 𝑦being the most present labels of the dataset, and 𝑧′ ≠𝑧, P (𝑧′ ∈𝑆| 𝑌= 𝑧) = 𝑐· 1𝑧=𝑦. Plotted intervals show the standard deviation on eight-fold cross-validation. Experiments were done with the Gaussian kernel. See all experimental details in (7.B).

### 7.5.1 Classiﬁcation

Classiﬁcation consists in recognizing the most relevant item among 𝑚items. The output space is isomorphic to the set of indices Y = ⟦1, 𝑚⟧, and the usual loss function is the 0-1 loss

$$
ℓ(𝑧, 𝑦) = 1𝑦≠𝑧.
$$

It has already been widely studied with several approaches that are calibrated in non-ambiguous deterministic settings, notably by Cour et al. (2011). The inﬁmum loss reads 𝐿(𝑧, 𝑆) = 1𝑧∉𝑆, and its risk in (7.4) is minimized for

$$
\underset{𝑧∈Y}{\arg\max}\, P (𝑧∈𝑆| 𝑋= 𝑥) .
$$

Based on data (𝑥𝑖, 𝑆𝑖)𝑖≤𝑛, our estimator (7.7) reads

$$
\underset{𝑧∈Y}{\arg\max}\, \sum_{𝑖;𝑧∈𝑆𝑖} 𝛼𝑖(𝑥).
$$

For this instance, the supremum loss is really conservative, only learning from set that are singletons 𝐿sp(𝑧, 𝑆) = 1𝑆≠{𝑧}, while the average loss is similar to the inﬁmum one, adding an evidence weight depending on the size of 𝑆, 𝐿ac(𝑧, 𝑆) ≃1𝑧∉𝑆/|𝑆|.

Real data experiment. To compare IL and AC, we used LIBSVM datasets (Chang and Lin, 2011) on which we corrupted labels to simulate partial labeling. When the corruption is uniform, the two methods perform the same. Yet, when labels are unbalanced, such as in the “DNA” and “svmguide2” datasets, and we only corrupt the most frequent label 𝑦∈Y, the inﬁmum loss performs better as shown in Figure 7.2.

### 7.5.2 Ranking

Ranking consists in ordering 𝑚items based on an input 𝑥that is often the conjunction of a user 𝑢and a query 𝑞, (𝑥= (𝑢, 𝑞)). An ordering can be thought of as a permutation, that is, Y = S𝑚. While designing a loss for ranking is intrinsically linked to a voting system (Arrow, 1950), making it a fundamentally hard problem; Kemeny (1959) suggested approaching it through pairwise disagreement, which is current machine learning standard (Duchi et al., 2010), leading to the Kendall embedding

$$
𝜑(𝑦) = sign 𝑦𝑖−𝑦𝑗 𝑖< 𝑗≤𝑚,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

and the Kendall loss (Kendall, 1938), with 𝐶= 𝑚(𝑚−1)/2

$$
ℓ(𝑦, 𝑧) = 𝐶−𝜑(𝑦)𝑇𝜑(𝑧).
$$

Supervision often comes as partial order on items, e.g.,

$$
𝑆= 𝑦∈S𝑚 𝑦𝑖> 𝑦𝑗> 𝑦𝑘, 𝑦𝑙> 𝑦𝑚 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 107 -->

Underlying scores Ground truth Items preferences Scores x x

[FIGURE: Figure 7.3]

Figure 7.3: Ranking, experimental setting. Colors represent four diﬀerent items to rank. Each item is associated with a utility function of 𝑥shown on the left ﬁgure. From those scores, an ordering 𝑦of the items is retrieved as represented on the right.

Ranking, m=10 IL AC 0.4 Loss 0.2 0.0 50 60 70 80 90 100 Corruption (in %)

[FIGURE: Figure 7.4]

Figure 7.4: Ranking, results. Testing risks (from (7.1)) achieved by AC and IL as a function of corruption parameter 𝑐. When 𝑐= 1, both risks are similar at 0.5. The simulation setting is the same as in Figure 7.2. The error bars are deﬁned as for Figure 7.2, after cross-validation over eight folds. IL clearly outperforms AC.

It corresponds to ﬁxing some coordinates in the Kendall embedding. In this setting, AC and SP are not consistent, as one can recreate a similar situation to the one in Section 7.4, considering 𝑚= 3, 𝑎= (1, 2, 3), 𝑏= (2, 1, 3) and 𝑐= (1, 3, 2) (permutations being represented with (𝜎−1(𝑖))𝑖≤𝑚), and supervision being most often 𝑆= (1 > 3) = {𝑎, 𝑏, 𝑐} and sometimes 𝑆= (1 > 3 > 2) = {𝑐}.

Minimum feedback arc set. Dealing with Kendall’s loss requires solving problem of the form,

$$
\underset{𝑦∈𝑆}{\arg\min}\, ⟨𝑐, 𝜑(𝑦)⟩,
$$

for 𝑐∈R𝑚2, and constraints due to partial ordering encoded in 𝑆⊂Y. This problem is an instance of the constrained minimum feedback arc set problem. We provide a simple heuristic to solve it in Appendix 7.C, which consists of approaching it as an integer linear program. Such heuristics are analyzed and reﬁned for analysis purposes by Ailon et al. (2005); van Zuylen et al. (2007).

Algorithm speciﬁcation. At inference, the inﬁmum loss requires solving:

$$
𝑛 ∑︁
𝑓𝑛(𝑥) = arg max sup (𝑦𝑖) ∈𝑆𝑖 𝛼𝑖(𝑥) ⟨𝜑(𝑧), 𝜑(𝑦𝑖)⟩. (7.7)
𝑧∈Y 𝑖=1
$$

(7.7)

It can be approached with alternate minimization, initializing 𝜑(𝑦𝑖) ∈Conv(𝜑(𝑆𝑖)), by putting 0 on unseen observed pairwise comparisons, then, iteratively, solving a minimum feedback arc set problem in 𝑧, then solving several minimum feedback arc set problems with the same objective, but diﬀerent constraints in (𝑦𝑖). This is done eﬃciently using warm start on the dual simplex algorithm.

Synthetic experiments. Let us consider X = [0, 1] embodying some input features. Let {1, . . . , 𝑚}, 𝑚∈N be abstract items to order, each item being linked to a utility function 𝑣𝑖∈RX , that characterizes

<!-- page: 108 -->

Problem setting Reconstruction y y signal sets centers IL AC x x

[FIGURE: Figure 7.5]

Figure 7.5: Partial regression on R. In this setting we aim at recovering a signal 𝑦(𝑥) given upper and lower bounds on its amplitude, and in thirty percent of case, information on its phase, or equivalently in R, its sign. IL clearly outperforms the baseline. Indeed, AC is a particularly ill-ﬁtted method on such a problem, since it regresses on the barycenter of the resulting sets. the value of 𝑖for 𝑥as 𝑣𝑖(𝑥). Labels 𝑦(𝑥) ∈Y are retrieved by sorting (𝑣𝑖(𝑥))𝑖≤𝑚. To simulate a problem instance, we set 𝑣𝑖as 𝑣𝑖(𝑥) = 𝑎𝑖· 𝑥+ 𝑏𝑖, where 𝑎𝑖and 𝑏𝑖follow a standard normal distribution. Such a setting is illustrated in Figure 7.3.

After sampling 𝑥uniformly on [0, 1] and retrieving the ordering 𝑦based on scores, we simulate partial labeling by randomly losing pairwise comparisons. The comparisons are formally deﬁned as coordinates of the Kendall’s embedding (𝜑(𝑦) 𝑗𝑘) 𝑗𝑘≤𝑚. To create non-symmetric perturbations we corrupt more often items whose scores diﬀer a lot. In other words, we suppose that the partial labeling focuses on pairs that are hard to discriminate. The corruption is set upon a parameter 𝑐∈[0, 1]. In fact, for 𝑚= 10, until 𝑐= 0.5, our corruption is fruitless since it can most often be inverted based on transitivity constraints in ordering, while the problem becomes non-trivial with 𝑐≥0.5. In the latter setting, IL clearly outperforms AC on Figure 7.4.

### 7.5.3 Partial regression

Partial regression is an example of non-discrete partial labeling problem, where Y = R𝑚and the usual loss is the Euclidean distance

$$
ℓ(𝑦, 𝑧) = ∥𝑦−𝑧∥2 .
$$

This partial labeling problem consists of regression where observations are sets 𝑆⊂R𝑚that contain the true output 𝑦instead of 𝑦. Among others, it arises for example in economical models, where bounds are preferred over approximation when acquiring training labels (Tobin, 1958). As an example, we will illustrate how partial regression could appear for some phase problems arising with physical measurements. Suppose a physicist wants to measure the law between a vector quantity 𝑌and some input parameters 𝑋. Suppose that, while she can record the input parameters 𝑥, her sensors do not exactly measure 𝑦but render an interval in which the amplitude ∥𝑦∥lays and only occasionally render its phase 𝑦/∥𝑦∥, in a fashion that leads to a set of candidates 𝑆for 𝑦. The geometry over ℓ2 makes it a perfect example to showcase superiority of the inﬁmum loss as illustrated in Figure 7.5.

In this ﬁgure, we consider Y = R and suppose that 𝑌is a deterministic function of 𝑋as shown by the dotted blue line signal. If, for a given 𝑥𝑖, measurements only provides that |𝑦𝑖| ∈[1, 2] without the sign of 𝑦𝑖, a situation where the phase is lost, this corresponds to the set 𝑆𝑖= [−2, −1] ∪[1, 2], explaining the shape of observed sets that are symmetric around the origin. Whenever the acquired data has no phase, which happens seventy percent of the time in our simulation, AC will target the set centers, explaining the green curve. On the other hand, IL is aiming at passing by each set, which explains the orange curve, crossing all blue bars.

## 7.6 Conclusions

In this paper, we deal with the problem of weakly supervised learning, beyond standard regression and classiﬁcation, focusing on the more general case of arbitrary loss functions and structured prediction. We provide a principled framework to solve the problem of learning with partial labeling, from which a natural variational approach based on the inﬁmum loss is derived. We prove that under some identiﬁability assumptions on the labeling process the framework is able to recover the solution of the original supervised learning problem. The resulting algorithm is easy to train and with strong theoretical guarantees. In particular,

<!-- page: 109 -->

we prove that it is consistent, and we provide generalization error rates. Finally, the algorithm is tested on simulated and real datasets, showing that when the acquisition process of the labels is more adversarial in nature, the proposed algorithm performs consistently better than baselines. This paper focuses on the problem of partial labeling, however the resulting mathematical framework is quite ﬂexible in nature, and it is interesting to explore the possibility to extend it to tackle also other weakly supervised problems, as imprecise labels from non-experts (Dawid and Skene, 1979), more general constraints over the set (𝑦𝑖)𝑖≤𝑛 (Quadrianto et al., 2009) or semi-supervision (Chapelle et al., 2006).

<!-- page: 110 -->

<!-- page: 111 -->

# Appendix

## 7.A Proofs

In the paper, we have implicitly considered X, Y separable and completely metrizable topological spaces, i.e. Polish spaces, which allows considering probabilities. Moreover, we assumed that Y is compact, to have minimizers well-deﬁned. The observation space was considered to be the set of closed subsets of Y endowed with the Hausdorﬀdistance, S = Cl(Y), 𝑑𝐻. As such, S is also a Polish metric space, inheriting this property from Y (Beer, 1993). In the following, we will show that the closeness of sets is important in order to switch from the minimum variability principle to the inﬁmum loss.

In terms of notations, we use the simplex notation ΔA to denote the space of Borel probability measures over the space A. In particular, ΔX×Y, ΔX×S and ΔX×Y×S are endowed with the weak-* topology and are Polish, inheriting the properties from original spaces (Aliprantis and Border, 2006). The fact that such spaces are Polish allows deﬁning the conditional probabilities given 𝑥∈X. We will denote this conditional probability 𝜌|𝑥when, for example, 𝜌∈ΔX×Y. Finally, we will denote by 𝜌X the marginal distributions of 𝜌 over X.

Before diving into proofs, we would like to point out that many of our results are pointwise results. At an intuitive level, we only leverage the structure of the loss on the output space and aggregate those results over X.

Remark 38 (Going pointwise). The learning frameworks in (7.1), (7.2) and (7.4) are pointwise separable as their solutions can be written as aggregation of pointwise solutions (Devroye et al., 1996). More exactly, the partial labeling risk (and similarly the fully supervised one) can be expressed as

$$
R𝑆( 𝑓) = E𝑋 R𝑆,𝑋( 𝑓(𝑋)) ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where the conditional risk reads,

$$
R𝑆,𝑥(𝑧) = E𝑆∼𝜏|𝑥[𝐿(𝑧, 𝑆)] ,
$$

with 𝜏|𝑥the conditional distribution of (𝑆| 𝑋= 𝑥). Thus, minimizing R𝑆globally for 𝑓∈YX is equivalent to minimizing locally R𝑆,𝑥for 𝑓(𝑥) for almost all 𝑥. Similarly, for (7.2),

$$
E(𝜌) = inf 𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)] = E𝑋 inf 𝑧∈Y E𝑌∼𝜌|𝑥[ℓ(𝑧,𝑌) | 𝑋= 𝑥] .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Therefore, studies on risk can be done pointwise on instances (ℓ, 𝜌|𝑥, 𝜏|𝑥), before integrating along X. Actually, Theorems 35, 11, 12 and 37 are pointwise results.

### 7.A.1 Proof of Theorem 35

Here we want to prove that when 𝜏is non-ambiguous, then it is possible to deﬁne an optimal 𝜌★that is deterministic on Y, and that this 𝜌★is characterized by solving (7.2).

Lemma 39. When 𝜏is non-ambiguous, and there is one, and only one, deterministic distribution eligible for 𝜏. More exactly, if we write, for any 𝑥∈X in the support of 𝜏X , based on Deﬁnition 34, 𝑆𝑥= {𝑦𝑥}, then this deterministic distribution is characterized as 𝜌|𝑥= 𝛿𝑦𝑥almost everywhere.

Proof. Let us consider a probability measure 𝜏∈ΔX×S. We begin by working on the concept of eligibility. Consider 𝜌∈ΔX×Y eligible for 𝜏and a suitable 𝜋as deﬁned in Deﬁnition 33. First of all, the condition that, for 𝑦∈𝑆, P𝜋(𝑆| 𝑌= 𝑦) = 0, can be stated formally in terms of measure as

$$
\frac{𝜋({(𝑥, 𝑦, 𝑆) ∈X × Y × S | 𝑦∉𝑆}) = 0,}{109}
$$

<!-- page: 112 -->

from which we deduced that, for 𝑦∈Y and 𝑥∈X,

$$
𝜌|𝑥(𝑦) = 𝜋|𝑥({𝑦} × S) = 𝜋|𝑥({𝑦} × {𝑆∈S | 𝑦∈𝑆})
≤𝜋|𝑥(Y × {𝑆∈S | 𝑦∈𝑆}) = 𝜏|𝑥({𝑆∈S | 𝑦∈𝑆}).
$$

It follows that when 𝜌is deterministic, if we write 𝜌|𝑥= 𝛿𝑦𝑥, then we have 𝜏|𝑥({𝑆∈S | 𝑦𝑥∈𝑆}) = 1, which means that 𝑦𝑥is in all sets that are in the support of 𝜏|𝑥, or that, using notations of Deﬁnition 34, 𝑦𝑥∈𝑆𝑥. So far, we have proved that if there exists a deterministic distribution, 𝜌|𝑥= 𝛿𝑦𝑥, that is eligible for 𝜏|𝑥, we have 𝑦𝑥∈𝑆𝑥. Reciprocally, one can do the reverse derivations, to show that if 𝜌|𝑥= 𝛿𝑦𝑥, with 𝑦𝑥∈𝑆𝑥, for all 𝑥∈X, then 𝜌is eligible for 𝜏When 𝜏is non-ambiguous, 𝑆𝑥is a singleton and therefore, there could be only one deterministic eligible distribution for 𝜏, that is characterized in the lemma. □ Now we use the characterization of deterministic distribution through the minimization of the risk (7.1).

Lemma 40 (Deterministic characterization). When Y is compact and ℓproper, deterministic distribution are exactly characterized by minimum variability (7.2) as

$$
E(𝜌) = inf_{𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)] = 0.}
$$

Proof. Let’s consider 𝜌∈ΔX×Y, because Y is compact and ℓcontinuous, we can consider 𝑓𝜌a minimizer of R( 𝑓; 𝜌). Let’s now suppose that R( 𝑓𝜌; 𝜌) = 0, since ℓis non-negative, it means that almost everywhere

$$
E𝑌∼𝜌|𝑥 ℓ( 𝑓𝜌(𝑥),𝑌) = 0.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Suppose that 𝜌|𝑥is not deterministic, then there is at least two points 𝑦and 𝑧in Y in its support, then, because ℓis proper, we come to the absurd conclusion that

$$
E𝑌∼𝜌|𝑥 ℓ( 𝑓𝜌(𝑥),𝑌) ≥𝜌|𝑥(𝑦)ℓ( 𝑓𝜌(𝑥), 𝑦) + 𝜌|𝑥(𝑧)ℓ( 𝑓𝜌(𝑥), 𝑧) > 0.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

So R( 𝑓𝜌; 𝜌) = 0 implies that 𝜌is deterministic. Reciprocally, when 𝜌is deterministic it is easy to show that the risk is minimized at zero. □

### 7.A.2 Proof of Theorem 11

At a comprehensive level, Theorem 11 is composed of two parts:

• A double minimum switch, to take the minimum over 𝜌before the minimum over 𝑓, and for which we need some compactness assumption to consider the joint minimum. • A minimum-expectation switch, to take the minimum over 𝜌⊢𝜏as a minimum 𝑦∈𝑆before the expectation to compute the risk, and for which we need some measure properties. We begin with the minimum-expectation switch. To proceed with derivations, we need ﬁrst to reformulate the concept of eligibility in Deﬁnition 33 in terms of measures.

Lemma 41 (Measure eligibility). Given a probability 𝜏over X × S, the space of probabilities over X × Y satisfying 𝜌⊢𝜏is characterized by all probability measures of the form

$$
𝜌(𝐶) = ∫ X×Y×S 1𝐶(𝑥, 𝑦) d𝜋|𝑥,𝑆(𝑦) d𝜏(𝑥, 𝑆),
$$

for any 𝐶a closed subset of X × Y, and where 𝜋is a probability measure over X × Y × S that satisﬁes 𝜋X×S = 𝜏and 𝜋|𝑥,𝑆(𝑆) = 1 for any (𝑥, 𝑆) in the support of 𝜏.

Proof. For any 𝜌that is eligible for 𝜏there exists a suitable 𝜋on X × Y × S as speciﬁed by Deﬁnition 33. Actually, the set of 𝜋leading to an eligible 𝜌:= 𝜋X×Y is characterized by satisfying 𝜋X×S = 𝜏and

$$
𝜋({(𝑥, 𝑦, 𝑆) ∈X × Y × S | 𝑦∉𝑆}) = 0.
$$

This last property can be reformulated with the complementary space as

$$
𝜋({(𝑥, 𝑦, 𝑆) ∈X × Y × S | 𝑦∈𝑆}) = 1,
$$

<!-- page: 113 -->

7.A. PROOFS 111 which equivalently reads, that for any (𝑥, 𝑆) in the support of 𝜏, we have

$$
𝜋|𝑥,𝑆(𝑆) = 𝜋|𝑥,𝑆({𝑦∈Y | 𝑦∈𝑆}) = 1.
$$

Finally, using the conditional decomposition we have that, for 𝐶a closed subset of X × Y

$$
∫ 1𝐶(𝑥, 𝑦) d𝜋(𝑥, 𝑦, 𝑆) = ∫
𝜌(𝐶) = 𝜋X×Y (𝐶) = 1𝐶(𝑥, 𝑦) d𝜋|𝑥,𝑆(𝑦) d𝜋X×S (𝑥, 𝑆),
X×Y×S X×Y×S
$$

which ends the proof since 𝜏= 𝜋X×S. □ We are now ready to state the minimum-expectation switch.

Lemma 42 (Minimum-Expectation switch). For a probability measure 𝜏∈ΔX×S, and measurable functions ℓ∈RY×Y and 𝑓∈YX , the inﬁmum of eligible expectations of ℓis the expectation of the inﬁmum of 𝑓over 𝑆where 𝑆is distributed according to 𝜏. Formally

$$
inf 𝜌⊢𝜏E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] = E(𝑋,𝑆)∼𝜏 inf 𝑦∈𝑆ℓ( 𝑓(𝑋), 𝑦) .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. Before all, note that (𝑥, 𝑆) →inf𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦) inherit measurability from 𝑓allowing to consider such an expectation (see Theorem 18.19 of Aliprantis and Border, 2006, and references therein for details). Moreover, let us use Lemma 41 to reformulate the right hand side problem as

$$
∫
inf 𝜌⊢𝜏E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] = inf ℓ( 𝑓(𝑥), 𝑦) d𝜋𝑥,𝑆(𝑦) d𝜏(𝑥, 𝑆).
𝜋∈M X×Y×S
$$

Where we denote by M ⊂ΔX×Y×S the space of probability measures 𝜋that satisfy the assumption of Lemma 41. We will now prove the equality by showing that both quantities bound the other one.

(≥). To proceed with the ﬁrst bound, notice that for 𝑥∈X and 𝑆∈S, when 𝜋|𝑥,𝑆∈ΔY only charge 𝑆, i.e. if 𝜋∈M, then ∫

$$
Y ℓ( 𝑓(𝑥), 𝑦) d𝜋𝑥,𝑆(𝑦) ≥inf 𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦).
$$

The ﬁrst bound is then obtained by taking the expectation over 𝜏of this pointwise property.

(≤). For the second bound, we consider the function 𝑌∈YX×S deﬁne as

$$
\underset{𝑦∈𝑆}{\arg\min}\, ℓ( 𝑓(𝑥), 𝑦).
$$

Such a function is well-deﬁned since 𝑆is compact due to the fact that Y is compact and S is the set of closed set. However, in more general cases, one can consider a sequence that minimizes ℓ( 𝑓(𝑥), 𝑦) rather than the argmin to show the same as what we are going to show. Now, if we deﬁne 𝜋( 𝑓) with 𝜋( 𝑓) X×S := 𝜏and 𝜋( 𝑓)|𝑥,𝑆:= 𝛿𝑌(𝑥,𝑆), because 𝑌(𝑥, 𝑆) is in 𝑆, we have that 𝜋( 𝑓) is in M, so, for 𝑥∈X and 𝑆∈S

$$
∫ ∫
inf 𝜋∈M ℓ( 𝑓(𝑥), 𝑦) d𝜋𝑥,𝑆(𝑦) ≤ ℓ( 𝑓(𝑥), 𝑦) d𝜋( 𝑓) 𝑥,𝑆(𝑦) = ℓ( 𝑓(𝑥),𝑌(𝑥, 𝑆)) = inf 𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦).
Y Y
$$

We end the proof by integrating this over 𝜏. □ Now, we will move on to the minimum switch. First, we make sure that the inﬁmum loss minimizer is well-deﬁned.

Lemma 43 (Inﬁmum loss minimizer). When Y is compact and the observed set are closed, there exists a measurable function 𝑓𝑆∈YX that minimize the inﬁmum loss risk

$$
∫
R𝑆( 𝑓𝑆) = inf 𝑓:X→Y R𝑆( 𝑓), where R𝑆( 𝑓) = min 𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦) d𝜏(𝑥, 𝑆).
$$

The inﬁmum on the right hand side is a minimum because 𝑆is a closed subset of Y compact, and therefore, is compact.

<!-- page: 114 -->

Proof. First note that 𝑑(𝑦, 𝑦′) = sup𝑧∈Y |ℓ(𝑧, 𝑦) −ℓ(𝑧, 𝑦′)| is a metric on Y when ℓis a proper loss: the triangular inequality holds trivially; when 𝑦= 𝑦′ then 𝑑(𝑦, 𝑦′) = 0; when 𝑦≠𝑦′, by properness we have ℓ(𝑦, 𝑦) = 0 and 𝑑(𝑦, 𝑦′) ≥ℓ(𝑦, 𝑦′) > 0. Moreover, note that 𝐿(𝑧, 𝑆) = min𝑦∈𝑆ℓ(𝑧, 𝑦) is continuous and 1-Lipschitz with respect to the topology induced by the Hausdorﬀdistance 𝑑𝐻based on 𝑑, indeed given two sets 𝑆, 𝑆′ ∈S

$$
|𝐿(𝑧, 𝑆) −𝐿(𝑧, 𝑆′)| ≤max max 𝑦∈𝑆min 𝑦′∈𝑆′ |ℓ(𝑧, 𝑦) −ℓ(𝑧, 𝑦′)| , max 𝑦′∈𝑆′ min 𝑦∈𝑆|ℓ(𝑧, 𝑦) −ℓ(𝑧, 𝑦′)|
 
≤max max 𝑦∈𝑆min 𝑦′∈𝑆′ 𝑑(𝑦, 𝑦′), max 𝑦′∈𝑆′ min 𝑦∈𝑆𝑑(𝑦, 𝑦′) = 𝑑𝐻(𝑆, 𝑆′).
∫
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The result of existence of a measurable 𝑓𝑆minimizing R𝑆( 𝑓) = 𝐿( 𝑓(𝑥), 𝑆)𝑑𝜏(𝑥, 𝑆) follows by the compactness of Y, the continuity of 𝐿(𝑧, 𝑆) in the ﬁrst variable with respect to the topology induced by 𝑑, in the second with respect to the topology induced by 𝑑𝐻and measurability of 𝜏|𝑥in 𝑥, via Berge maximum theorem (see Theorem 18.19 of Aliprantis and Border, 2006, and references therein). □ We can state the minimum switch now.

Lemma 44 (Minimum switch). When Y is compact, and observed sets are closed, solving the partial labeling through the minimum variability principle

$$
𝑓∗∈arg min
$$

𝑓∈YX E𝜌★[ℓ( 𝑓(𝑋),𝑌)] , with 𝜌★∈arg min

$$
𝜌⊢𝜏 inf_{𝑓∈YX E𝜌[ℓ( 𝑓(𝑋),𝑌)] .}
$$

can be done jointly in 𝑓and 𝜌, and rewritten as

$$
\underset{𝑓∈YX inf}{\arg\min}\, 𝜌⊢𝜏E𝜌[ℓ( 𝑓(𝑋),𝑌)] .
$$

Proof. When (𝜌★, 𝑓∗) is a minimizer of the top problem, it also minimizes the joint problem (𝜌, 𝑓) → R( 𝑓; 𝜌), and we can switch the inﬁmum order. The hard part is to show that when 𝑓𝑆minimizes the bottom risk, the inﬁmum over 𝜌is indeed a minimum. Indeed, we know from Lemma 42 that 𝑓𝑆is characterized as a minimizer of the inﬁmum risk R𝑆, those are well-deﬁned as shown in precedent lemma. To 𝑓𝑆, we can associate 𝜌𝑆:= 𝜋( 𝑓) as deﬁned in the proof of Lemma 42, which is due to the closeness of sets in S and the compactness of Y. Indeed, ( 𝑓𝑆, 𝜌𝑆) minimize jointly the objective R( 𝑓, 𝜌), so we have that

$$
𝜌𝑆∈arg min
$$

inf 𝑓:X→Y R( 𝑓; 𝜌), and 𝑓𝑆∈arg min

$$
R( 𝑓; 𝜌𝑆).
𝜌⊢𝜏 𝑓:X→Y
$$

From which we deduced that 𝜌𝑆can be written as a 𝜌★and 𝑓𝑆as an 𝑓∗. □ Remark 45 (A counter example when sets are not closed.). The minimum switch relies on compactness assumption, which can be violated when the observed sets in S are not closed. Let us consider the case where Y = R, ℓ= ℓ2 is the mean square loss. Consider the pointwise weak supervision

$$
𝜏= 1 2𝛿Q + 1 2𝛿√ 2Q,
√
$$

In this case, we have 𝜌★= 𝛿0. Yet, for any 𝑧, we do have R𝑆,𝑥(𝑧) = 0 for any 𝑧∈R. For example, if 𝑧= 2, one can consider

$$
𝜌𝑛= 1 2𝛿√ 2 + 1 \frac{2𝛿⌊10𝑛√}{10𝑛} 2⌋ ,
$$

to show that 𝑧∈arg min𝑧∈Y inf𝜌⊢𝜏R(𝑧, 𝜌). As one can see this is counter example is based on the fact that {𝜌| 𝜌⊢𝜏} is not complete, so that there exists inﬁmum of R𝑥(𝑧, 𝜌) that are not minimum such as R𝑥(

$$
√ 2, 𝛿√ 2).
$$

### 7.A.3 Proof of Theorem 12

If 𝜏is not ambiguous, then, almost surely for 𝑥∈X, if 𝑦𝑥is the only element in 𝑆𝑥of Deﬁnition 34, we know that 𝜌★|𝑥= 𝛿𝑦𝑥, and consequently we derive 𝑓∗(𝑥) = 𝑦𝑥, so for it to be consistent with 𝑓0, we need that 𝑓0(𝑥) = 𝑦𝑥.

Moreover, because 𝜏is a weakening of 𝜌0, 𝜌0 is eligible for 𝜏. When 𝜌0 is deterministic, we know from considerations in the proof of Lemma 39, that it is 𝜌★, the only deterministic distribution eligible for 𝜏. Thus, in fact, the condition 𝑆𝑥= { 𝑓0(𝑥)} is implied by 𝜌0 deterministic.

<!-- page: 115 -->

7.A. PROOFS 113

### 7.A.4 Proof of Theorem 37

When 𝜏is not ambiguous, we know from Theorem 35, that 𝜌★is deterministic. Let us write 𝜌★|𝑥= 𝛿𝑦𝑥, we have 𝑓∗(𝑥) = 𝑦𝑥, and R𝑥( 𝑓∗) = 0, moreover, because 𝑦𝑥is in every 𝑆in the support of 𝜏|𝑆, then R𝑆,𝑥( 𝑓∗) = 0. Similarly to the bound given by Cour et al. (2011) for the 0-1 loss, we have

$$
∑︁
R𝑆,𝑥(𝑧) = E𝑆∼𝜏|𝑥[ inf 𝑧′∈𝑆ℓ(𝑧, 𝑧′)] = inf 𝑧′∉𝑆ℓ(𝑧, 𝑧′) P𝑆∼𝜏|𝑥(𝑆)
𝑆;𝑧∉𝑆
≥inf 𝑧′≠𝑧ℓ(𝑧, 𝑧′) P𝑆∼𝜏|𝑥(𝑧∉𝑆) ≥inf 𝑧′≠𝑧ℓ(𝑧, 𝑧′)𝜂,
$$

while R𝑥(𝑧) = ℓ(𝑧, 𝑦), so we deduce locally

$$
R𝑥(𝑧; 𝜌★|𝑥) −R𝑥( 𝑓∗(𝑥); 𝜌★|𝑥) ≤ ℓ(𝑧, 𝑦) inf𝑧′≠𝑧ℓ(𝑧, 𝑧′) 𝜂−1 R𝑆,𝑥(𝑧) −R𝑆,𝑥( 𝑓∗(𝑥)) 
≤𝑒𝜈𝜂−1 R𝑆,𝑥(𝑧) −R𝑆,𝑥( 𝑓∗(𝑥)) .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Integrating over 𝑥this last equation gives us the bound in Theorem 37.

### 7.A.5 Reﬁned bound analysis of Theorem 37

The constant 𝐶that appears in Theorem 37 is the result of controlling separately the corruption process and the discrepancy of the loss. Indeed, they can be controlled together, leading to a better constant. To relates the two risk R and R𝑆, we will consider the pointwise setting 𝜏∈Δ2Y and 𝜌0 ∈ΔY that satisﬁes 𝜌0 ⊢𝜏, we will also consider a prediction 𝑧∈Y.

Proposition 46 (Bound reﬁnement). When Y is discrete and 𝜏not ambiguous, the best 𝐶that veriﬁes (7.6) in the pointwise setting 𝜏∈Δ2Y is the maximum of 𝜆−1, for 𝜆∈[0, 1] such that there exists a point 𝑧≠𝑦and signed measured 𝜎that verify R(𝑧; 𝜎) = 0 and such that 𝜎+ 𝜆𝛿𝑦+ (1 −𝜆)𝛿𝑧is a probability measure that is eligible for 𝜏.

Proof. First, let’s extend our study to the space MY of signed measure over Y. We extend the risk deﬁnition in (7.1) to any signed measure 𝜇∈MY, with

$$
R𝑥(𝑧; 𝜇) = ∫ Y ℓ(𝑧, 𝑦) d𝜇(𝑦).
$$

Note that the risk is a linear function of the distribution 𝜇. Two spaces are going to be of particular interest: the one of measures of mass one MY,1, and the one of measures of mass null MY,0, where

$$
MY,𝑝= {𝜇∈M | 𝜇(Y) = 𝑝} .
$$

Let’s now relates for a 𝜌0, 𝜏and 𝑧, the risk R𝑥(𝑧; 𝜌0) and R𝑆,𝑥(𝑧). To do so, we introduce the space of signed measures of null mass, that could be said orthogonal to (ℓ(𝑧, 𝑦))𝑦∈Y, formally

$$
𝐷𝑧= 𝜇∈MY,0 R𝑥(𝑧; 𝜇) = 0 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

There are two alternatives: (1) either R𝑥(𝑧; 𝜌0) = 0, and so R𝑆,𝑥(𝑧) = 0 too, and we have related the two risk; (2) either R𝑥(𝑧, 𝜌0) ≠0, and the space MY,1 can be decomposed as

$$
MY,1 = 𝐷𝑧+ {𝜆𝜌0 + (1 −𝜆)𝛿𝑧| 𝜆∈R} .
$$

To prove it take 𝜇∈MY,1, and use linearity of the risk after writing

$$
𝜇= 𝜆𝜌0 + (1 −𝜆)𝛿𝑧+ (𝜇−(𝜆𝜌0 + (1 −𝜆)𝛿𝑧)) , with 𝜆= R𝑥(𝑧, 𝜇)
R𝑥(𝑧, 𝜌0) .
$$

For such a 𝜇, using the linearity of the risk, and the properness of the loss, if we denote by 𝑑𝑧the part in 𝐷𝑧 of the last decomposition, we have

$$
R𝑥(𝑧; 𝜇) = 𝜆R𝑥(𝑧; 𝜌0) + (1 −𝜆)R𝑥(𝑧; 𝛿𝑧) + R𝑥(𝑧; 𝑑𝑧) = 𝜆R𝑥(𝑧; 𝜌0)
$$

<!-- page: 116 -->

$$
b 1 4 𝑑(𝑏, 𝑐) ∝R𝑆(𝑏) = R(𝑏; 1 4𝛿𝑐+ 3 4𝛿𝑏)
𝑑(𝑏, 𝑐) ∝R(𝑏; 𝛿𝑐)
𝑅𝜏 𝛿𝑏+ 𝐷𝑏
a c
$$

[FIGURE: Figure 7.6]

Figure 7.6: Geometrical understanding of Proposition 46, showing the link between the inﬁmum and the fully supervised risk. The drawing is set in the aﬃne span of the simplex MY,1, where we identify 𝑎with 𝛿𝑎. The underlying instance (ℓ, 𝜏) is taken from Section 7.4, and can be linked to the setting of Proposition 46 with 𝑧= 𝑏, 𝑦= 𝑐. Are represented in the simplex the level curves of the function 𝜌→R(𝑧; 𝜌). Based on this drawing, one can recover R𝑆(𝑏) = R(𝑏)/4, which is better than the bound given in Theorem 37.

$$
𝑧+ 𝑥⊥
𝑧
𝜆𝑑(𝑧+ 𝑥⊥, 𝑦)
𝜆𝑦+ (1 −𝜆)𝑧+ 𝑥⊥
𝑆
𝑦+ 𝑥⊥
𝑦
$$

[FIGURE: Figure 7.7]

Figure 7.7: A variant of Thales theorem.

If we denote by 𝑅𝜏= {𝜌∈ΔY | 𝜌⊢𝜏}, we can conclude that

$$
R𝑆,𝑥(𝑧) R𝑥(𝑧; 𝜌0) = inf {𝜆| (𝜆𝜌0 + (1 −𝜆)𝛿𝑧) ∈𝑅𝜏+ 𝐷𝑧} .
$$

Finally, when 𝜏is not ambiguous, we know that 𝜌★is deterministic, and if 𝜌0 is deterministic then 𝜌0 = 𝜌★. In this case, there exists a 𝑦such that 𝜌0 = 𝛿𝑦, and we can suppose this 𝑦is diﬀerent from 𝑧otherwise R𝑥(𝑧; 𝜌0) = 0. In this case, we also have R𝑥(𝑧∗) = R𝑆,𝑥(𝑧∗) = 0 with 𝑧∗= 𝑦, and thus the excess of risk to relates in (7.6) is indeed the relation between the two risks.

□

Remark 47 (Proposition 46 as a variant of Thales theorem). Proposition 46 can be seen as a variant of the Thales theorem. Indeed, with the geometrical embedding 𝜋of the simplex in RY, 𝜋(𝜌) = (𝜌(𝑦))𝑦∈Y, one can have, with 𝑑the Euclidean distance

$$
R𝑆,𝑥(𝑧) R𝑥(𝑧; 𝜌0) = 𝑑(𝜋(𝛿𝑧+ 𝐷𝑧), 𝜋(𝑅𝜏)) 𝑑(𝜋(𝛿𝑧+ 𝐷𝑧), 𝜋(𝜌0)) .
$$

And conclude by using the following variant of Thales theorem, that can be derived from

[FIGURE: Figure 7.7]

Figure 7.7: For 𝑥, 𝑦, 𝑧∈R𝑑, and 𝑆⊂R𝑑, with 𝑑the Euclidean distance, if 𝑦∈𝑆, 𝑑(𝑧+ 𝑥⊥, 𝑆) = 𝛾𝑑(𝑧+ 𝑥⊥, 𝑦), where

$$
𝜆∈R, (𝜆𝑦+ (1 −𝜆)𝑧+ 𝑥⊥) ∩𝑆≠∅
𝛾= min |𝜆| .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Moreover, notice that if 𝑆is contained in the half-space that contains 𝑦regarding the cut with the hyperplane 𝑧+ 𝑥⊥, 𝜆can be restricted to be in [0, 1].

Remark 48 (Active labeling). When annotating data, as a partial labeler, you could ask yourself how to optimize your labeling. For example, suppose that you want to poll a population to retrieve preferences among a set of presidential candidates. Suppose that for a given polled person, you can only ask her to compare between four candidates. Which candidates would you ask her to compare? According to the questions you are asking, you will end up with diﬀerent sets of potential weak distribution 𝜏. If aware of the problem ℓthat your dataset is intended to tackle, and aware of a constant 𝐶= 𝐶(ℓ, 𝜏) that veriﬁes (7.6), you might want to design your questions in order to maximize on average over potential 𝜏, the quantity 𝐶(ℓ, 𝜏). An example where 𝜏is not well-designed according to ℓis given in Figure 7.8.

<!-- page: 117 -->

7.A. PROOFS 115

$$
ℓ⊥ a b 𝑅𝜏 c
$$

𝑏

[FIGURE: Figure 7.8]

Figure 7.8: Example of a bad link between 𝜏and ℓ. Same representation as Figure 7.6 with a diﬀerent instance where 𝜏= 1 2𝛿{𝑎,𝑐} + 1 2𝛿{𝑏,𝑐} and ℓ(𝑏, 𝑎) = 0, ℓ(𝑏, 𝑐) = 1. In this example 𝐶ℓ(𝜏) = +∞, and the inﬁmum loss is 0 on Y and therefore not consistent. Given the loss structure, partial labeling acquisition should focus on specifying sets that do not intersect {𝑎, 𝑏}. Note that this instance violates the proper loss assumption, explaining its inconsistency.

### 7.A.6 Proof of Theorems 13 and 14

First, note that, since R𝑆( 𝑓) is characterized by R𝑆( 𝑓) = E(𝑥,𝑆)∼𝜏min𝑢∈𝑆ℓ( 𝑓(𝑥), 𝑢), then the problem

$$
𝑓∗= arg min R𝑆( 𝑓) = arg min E(𝑥,𝑆)∼𝜏 min 𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦) .
𝑓:X→Y 𝑓:X→Y
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

can be considered as an instance of structured prediction with loss 𝐿(𝑧, 𝑆) = min𝑦∈𝑆ℓ( 𝑓(𝑥), 𝑦). The framework for structured prediction presented in Ciliberto et al. (2016), and extended in Ciliberto et al. (2020), provides consistency and learning rates in terms of the excess risk R𝑆( 𝑓𝑛) −R𝑆( 𝑓∗) when 𝑓∗is estimated via 𝑓𝑛deﬁned as in (7.7) and when the structured loss 𝐿admits the decomposition

$$
𝐿(𝑧, 𝑆) = ⟨𝜓(𝑧), 𝜑(𝑆)⟩H,
$$

for a separable Hilbert space H and two maps 𝜓: Y →H and 𝜑: S →H. Note that since Y is ﬁnite 𝐿 always admits the decomposition, indeed the cardinality of Y is ﬁnite, i.e., |Y| < ∞and |S| = 2|Y |. Choose an ordering for the elements in Y and in S and denote them respectively 𝑜Y : N →Y and 𝑜S : N →S. Let 𝑛Y : Y →N be the inverse of 𝑜Y, i.e. 𝑜Y (𝑛Y (𝑦)) = 𝑦and 𝑛Y (𝑜Y (𝑖)) = 𝑖for 𝑦∈Y and 𝑖∈1, . . . , |Y|, deﬁne analogously 𝑛S. Now let H = R|Y | and deﬁne the matrix 𝐵∈R|Y |×2|Y| with element 𝐵𝑖,𝑗= 𝐿(𝑜Y (𝑖), 𝑜S ( 𝑗)) for 𝑖= 1, . . . , |Y| and 𝑗= 1, . . . , 2|Y |, then deﬁne

$$
\frac{𝜓(𝑧) = 𝑒|Y |}{𝑛Y (𝑧),} \frac{𝜑(𝑆) = 𝐵𝑒2|Y|}{𝑛S (𝑆),}
$$

where 𝑒𝑘 𝑖is the 𝑖-th element of the canonical basis of R𝑘. We have that

$$
⟨𝜓(𝑧), 𝜑(𝑆)⟩H = ⟨𝑒|Y | 𝑛Y (𝑧), 𝐵𝑒2|Y| 𝑛S (𝑆)⟩𝑅|Y| = 𝐵𝑛Y (𝑧),𝑛S (𝑆) = 𝐿(𝑖Y (𝑛Y (𝑧)), 𝑖S (𝑛S (𝑆))) = 𝐿(𝑧, 𝑆),
$$

for any 𝑧∈Y, 𝑆∈S. So we can apply Theorem 4 and 5 of Ciliberto et al. (2016) (see also their extended forms in Theorem 4 and 5 of Ciliberto et al., 2020). The last step is to connect the excess risk on R𝑆with the excess risk on R( 𝑓, 𝜌★), which is done by our comparison inequality in Theorem 37.

Remark 49 (Illustrating the consistency in a discrete setting). Suppose that 𝜏|𝑥has been approximate, as a signed measure ˆ𝜏|𝑥= Í𝑛 𝑖=1 𝛼𝑖(𝑥)𝛿𝑆𝑖. After renormalization, one can represent it as a region 𝑅ˆ𝜏|𝑥in the aﬃne span of ΔY. Retaking the settings of Section 7.4, suppose that

$$
ˆ𝜏({𝑎, 𝑏}) = 1 2, ˆ𝜏({𝑐}) = 1 2, ˆ𝜏({𝑎, 𝑐}) = 1 4, ˆ𝜏({𝑎, 𝑏, 𝑐}) = −1
4.
$$

This corresponds to the region 𝑅ˆ𝜏represented in Figure 7.9. It leads to a disambiguation ˆ𝜌that minimizes E (7.2), inside this space as

$$
\frac{ˆ𝜌(𝑎) = 1}{2,} \frac{ˆ𝜌(𝑏) = −1}{4,} \frac{ˆ𝜌(𝑐) = 3}{4,}
$$

and to the right prediction ˆ𝑧= 𝑐, since ˆ𝜌felt in the decision region 𝑅𝑐. As the number of data augments, 𝑅ˆ𝜏 converges toward 𝑅𝜏, so does ˆ𝜌toward 𝜌★and the risk R( ˆ𝑓) toward its minimum.

<!-- page: 118 -->

$$
a b 𝑅𝜏 𝑅ˆ𝜏 ˆ𝜌 \frac{c}{𝜌★}
$$

[FIGURE: Figure 7.9]

Figure 7.9: Understanding convergence of the algorithm (7.7). Our method is approximating 𝜏as a signed measured ˆ𝜏, which leads to 𝑅ˆ𝜏in dark gray compared to the ground truth 𝑅𝜏in light gray. The disambiguation of ˆ𝜌 and 𝜌★is done on those two domains with the same objective E (7.2), which level curves are represented with light lines.

### 7.A.7 Understanding of the average and the supremum loss

For the average loss, if there is discrepancy in the loss 𝜈> 0, then there exists 𝑎, 𝑏, 𝑐such that ℓ(𝑏, 𝑐) = (1 + 𝜀)ℓ(𝑎, 𝑏), for some 𝜀> 0. In this case, one can recreate the example of Section 7.4 by considering 𝜌0 = 𝜌★= 𝛿𝑐and

$$
𝜏= 𝜆𝛿{𝑐} + (1 −𝜆)𝛿{𝑎,𝑏,𝑐}, with 𝜆= 1 2 𝜀 3ℓ(𝑎, 𝑏) + 𝜀,
$$

to show the inconsistency of the average loss. Similarly, supposing, without loss of generality that ℓ(𝑎, 𝑐) ∈[ℓ(𝑎, 𝑏), ℓ(𝑏, 𝑐)], the case where 𝜌0 = 𝜌★= 𝛿𝑏and

$$
2 min 𝜀 1 + 𝜀, 1 + 𝜀−𝑥 2 + 𝜀−𝑥 
𝜏= 𝜆𝛿{𝑏} + (1 −𝜆)𝛿{𝑎,𝑏,𝑐}, with 𝜆= 1 , 𝑥= ℓ(𝑎, 𝑐)
ℓ(𝑎, 𝑏) ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

will fail the supremum loss, which will recover 𝑧∗= 𝑎, instead of 𝑧∗= 𝑏.

## 7.B Experiments 7.B.1 Classiﬁcation

Let us consider the classiﬁcation setting of Section 7.5.1. The inﬁmum loss reads 𝐿(𝑧, 𝑆) = 1𝑧∉𝑆. Given a weak distribution 𝜏, the inﬁmum loss is therefore solving for 𝑓(𝑥) ∈arg min

$$
E𝑆∼𝜏|𝑥[𝐿(𝑧, 𝑆)] = arg min E𝑆∼𝜏|𝑥[1𝑧∉𝑆] = arg min P𝑆∼𝜏|𝑥(𝑧∉𝑆) = arg max P𝑆∼𝜏|𝑥(𝑧∈𝑆).
𝑧∈Y 𝑧∈Y 𝑧∈Y 𝑧∈Y
$$

Given data, (𝑧𝑖, 𝑆𝑖) our estimator consists in approximating the conditional distributions 𝜏|𝑥as

$$
ˆ𝜏|𝑥= \sum_{𝑛 𝑖=1} 𝛼𝑖(𝑥)𝛿𝑆𝑖,
$$

from which we deduce the inference formula, that we could also be derived from (7.7),

$$
𝑛 ∑︁ ∑︁
ˆ𝑓(𝑥) ∈arg max 𝛼𝑖(𝑥)1𝑧∈𝑆𝑖= arg max
𝛼𝑖(𝑥).
𝑧∈Y 𝑖=1 𝑧∈Y 𝑖;𝑧∈𝑆𝑖
$$

Complexity analysis The complexity of our algorithm (7.7) can be split in two parts:

• a training part, where given (𝑥𝑖, 𝑆𝑖) we precompute quantities that will be useful at inference. • an inference part, where given a new 𝑥, we compute the corresponding prediction ˆ𝑓(𝑥). In the following, we will review the time and space complexity of both parts. We give this complexity in terms of 𝑛the number of data and 𝑚the number of items in Y. Results are summed up in Table 7.1.

<!-- page: 119 -->

7.B. EXPERIMENTS 117

[TABLE: Table 7.1]

Table 7.1: Complexity of our algorithm for classiﬁcation.

| Complexity | Training | Inference |
|---|---|---|
| Time | O(𝑛²(𝑛+ 𝑚)) | O(𝑛𝑚) |
| Space | O(𝑛(𝑛+ 𝑚)) | O(𝑛+ 𝑚) |

Training. Let us suppose that computing 𝐿(𝑦, 𝑆) = 1𝑦∉𝑆can be done in a constant cost that does not depend on 𝑚. We ﬁrst compute the following matrices in O(𝑛𝑚) and O(𝑛2) in time and space.

$$
𝐿= (𝐿(𝑦, 𝑆𝑖))𝑖≤𝑛,𝑦∈Y ∈R𝑛×𝑚, 𝐾𝜆= (𝑘(𝑥𝑖, 𝑥𝑗) + 𝑛𝜆𝛿𝑖=𝑗)𝑖𝑗∈R𝑛×𝑛.
$$

We then solve the following, based on the _gesv routine of Lapack, in O(𝑛3 + 𝑛2𝑚) in time and O(𝑛(𝑛+ 𝑚)) in space (see Golub and Loan, 1996, for details)

$$
𝛽= 𝐾−1 𝜆𝐿∈R𝑛×𝑚.
$$

Inference. At inference, we ﬁrst compute in O(𝑛) in both time and space

$$
𝑣(𝑥) = (𝑘(𝑥, 𝑥𝑖))𝑖≤𝑛∈R𝑛.
$$

Then we do the following multiplication in O(𝑛𝑚) in time and O(𝑚) in space,

$$
R𝑆,𝑥= 𝑣(𝑥)𝑇𝛽∈R𝑚.
$$

Finally, we take the minimum of R𝑆,𝑥(𝑧) over 𝑧in O(𝑚) in time and O(1) in space.

Baselines The average loss is really similar to the inﬁmum loss, it reads

$$
∑︁
𝐿ac(𝑧, 𝑆) = 1 ℓ(𝑧, 𝑦) = 1 −1𝑧∈𝑆 |𝑆| ≃1 |𝑆| · 1𝑧∉𝑆= 1
|𝑆| 𝐿(𝑧, 𝑆).
|𝑆|
𝑦∈𝑆
$$

Following similar derivations to the one for the inﬁmum loss, given a distribution 𝜏, one can show that the average loss is solving for

$$
\underset{𝑧∈Y}{\arg\max}\, \sum_{𝑆;𝑧∈𝑆} \frac{1}{|𝑆| 𝜏|𝑥(𝑆),}
$$

which is consistent when 𝜏is not ambiguous. The diﬀerence with the inﬁmum loss is due to the term in |𝑆|. It can be understood as an evidence weight, giving less importance to big sets that do not allow discriminating eﬃciently between candidates. Given data (𝑥𝑖, 𝑆𝑖), it leads to the estimator

$$
\underset{𝑧∈Y}{\arg\min}\, \sum_{𝑖;𝑧∈𝑆𝑖} \frac{𝛼𝑖(𝑥)}{|𝑆𝑖| .}
$$

The supremum loss is really conservative since

$$
\frac{𝐿sp(𝑧, 𝑆) = sup}{𝑦∈𝑆} \frac{ℓ(𝑦, 𝑧) = sup}{𝑦∈𝑆} 1𝑦≠𝑧= 1𝑆≠{𝑧}.
$$

It is solving for

$$
\underset{𝑧∈Y}{\arg\max}\, 𝜏|𝑥({𝑧}),
$$

which empirically correspond to discarding all the set with more than one element

$$
\underset{𝑧∈Y}{\arg\min}\, \sum_{𝑖;𝑆𝑖={𝑧}} 𝛼𝑖(𝑥).
$$

Note that 𝜏could be not ambiguous while charging no singleton, in this case, the supremum loss is not informative, as its risk is the same for any prediction.

<!-- page: 120 -->

segment vowel IL AC 0.75 IL AC 0.15 0.50 Loss 0.10 Loss 0.25 0.05 0.00 0 20 40 60 80 Corruption (in %) 0 20 40 60 80 Corruption (in %)

[FIGURE: Figure 7.10]

Figure 7.10: Classiﬁcation. Testing risks (7.1) achieved by AC and IL on the “segment” and “vowel” datasets from LIBSVM as a function of corruption parameter 𝑐, when the corruption is uniform, as described in Section 7.B.1.

[TABLE: Table 7.2]

Table 7.2: LIBSVM datasets characteristics, showing the number of data, of classes, of input features, and the proportion of the most present class when labels are unbalanced.

| Dataset | Data (𝑛) | Classes (𝑚) | Features (𝑑) | Balanced | Most present |
|---|---|---|---|---|---|
| DNA | 2000 | 3 | 180 | × | 52.6% |
| Svmguide2 | 391 | 3 | 20 | × | 56.5% |
| Segment | 2310 | 7 | 19 | ✓ | - |
| Vowel | 528 | 11 | 10 | ✓ | - |

Corruptions on the LIBSVM datasets To illustrate the dynamic of our method versus the average baseline, we used LIBSVM datasets (Chang and Lin, 2011), that we corrupted by artiﬁcially adding false class candidates to transform fully supervised pairs (𝑥, 𝑦) into weakly supervised ones (𝑥, 𝑆). We experiment with two types of corruption processes.

• A uniform one, reading, with the 𝜇of Deﬁnition 33, for 𝑧≠𝑦,

$$
P(𝑌,𝑆)∼𝜇|Y×2Y (𝑧∈𝑆| 𝑌= 𝑦) = 𝑐.
$$

with 𝑐a corruption parameter that we vary between zero and one. In this case, the average loss and the inﬁmum one works the same as shown on Figure 7.10. • A skewed one, where we only corrupt the pair (𝑥, 𝑦) when 𝑦is the most present class in the dataset. More exactly, if 𝑦is the most present class in the dataset, for 𝑧∈Y, and 𝑧′ ≠𝑧, our corruption process reads

$$
P(𝑌,𝑆)∼𝜇|Y×2Y (𝑧′ ∈𝑆| 𝑌= 𝑧) = 𝑐· 1𝑧=𝑦.
$$

In unbalanced dataset, such as the “DNA” and “svmguide2” datasets, where the most present class represents more than ﬁfty percent of the labels as shown Table 7.2, this allows fooling the average loss as shown Figure 7.2. Indeed, this corruption was designed to fool the average loss since we knew of the evidence weight 1 |𝑆| appearing in its solution.

Reproducibility speciﬁcations All experiments were run with Python, based on the NumPy library. Randomness was controlled by instantiating the random seed of NumPy to 0 before doing any computations. Results of Figures 7.2 and 7.10 were computed by using eight folds, and trying out several hyperparameters, before keeping the set of hyperparameters that hold the lowest mean error over the eight folds. Because we used a Gaussian kernel, there were two hyperparameters, the Gaussian kernel parameter 𝜎, and the regularization parameter 𝜆. We search for the best hyperparameters based on the heuristic

$$
𝜎= 𝑐𝜎𝑑, 𝜆= 𝑐𝜆𝑛−1/2,
$$

where 𝑑is the dimension of the input X (or the number of features), and where the Gaussian kernel reads

$$
𝑘(𝑥, 𝑥′) = exp \frac{−∥𝑥−𝑥′∥2}{2𝜎2} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 121 -->

7.B. EXPERIMENTS 119

$$
10𝑖 𝑖∈⟦3, −3⟧
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We tried 𝑐𝜎∈{10, 5, 1, .5, .1, .01} and 𝑐𝜆∈ .

### 7.B.2 Ranking

Consider the ranking setting of Section 7.5.2, where Y = S𝑚, 𝜑is the Kendall’s embedding and the loss is equivalent to ℓ(𝑧, 𝑦) = −𝜑(𝑦)𝑇𝜑(𝑧).

Complexity analysis Given data (𝑥𝑖, 𝑆𝑖), our algorithm is solving at inference for

$$
𝑛 ∑︁ 𝑛 ∑︁
𝑓(𝑥) ∈arg min inf 𝑦𝑖∈𝑆𝑖− 𝛼𝑖(𝑥)𝜑(𝑧)𝑇𝜑(𝑦𝑖) = arg max sup 𝑦𝑖∈𝑆𝑖 𝛼𝑖(𝑥)𝜑(𝑧)𝑇𝜑(𝑦𝑖)
𝑧∈Y 𝑖=1 𝑧∈Y 𝑖=1
$$

We solved it through alternate minimization, by iteratively solving in 𝑧for

$$
\underset{𝜉∈𝜑(Y)}{\arg\max}\, * 𝜉, \sum_{𝑛 𝑖=1} 𝛼𝑖(𝑥)𝜑(𝑦𝑖)(𝑡) + ,
$$

and solving for each 𝑦𝑖for

$$
\underset{𝜉∈𝜑(𝑆𝑖)}{\arg\max}\, 𝛼𝑖(𝑥) ⟨𝜉, 𝜑(𝑧)⟩.
$$

We initialize the problem with the coordinates of 𝜑(𝑦𝑖) put to 0 when not speciﬁed by the constraint 𝑦𝑖∈𝑆𝑖.2 Those two problems are minimum feedback arc set problems, that are NP-hard in 𝑚, meaning that one has to check for all potential solutions, and there is 𝑚! of them, which is the cardinal of S𝑚. We suggest solving them using an integer linear programming (ILP) formulation that we relax into linear programming as explained in Appendix 7.C. All the problems in 𝑦𝑖share the same objective, up to a change in sign, but diﬀerent constraint 𝜉∈𝜑(𝑆𝑖), such a setting is particularly suited for warm start on the dual simplex algorithm to solve eﬃciently one after the other the linear programs associated to each 𝑦𝑖.

To give numbers, at training time, we compute the inverse 𝐾−1 𝜆 in O(𝑛3) in time and O(𝑛2) in space, and at inference we compute 𝛼(𝑥)𝐾−1 𝜆𝑣(𝑥) in O(𝑛2) in time and O(𝑛) in space, before solving iteratively 𝑛 NP-hard problem in 𝑚of complexity 𝑛NP(𝑚), that cost 𝑛𝑚2 in space to represent using Cplex (IBM, 2017), if we allow our self 𝑒iterations, the inference complexity is O(𝑛2 + 𝑒𝑛NP(𝑚)) in time and O(𝑛𝑚2) in space.

Baselines The supremum loss is really similar to the inﬁmum loss, only changing an inﬁmum by a supremum. However, algorithmically, this change leads to solving for a local saddle point rather than solving for a local minimum. While the latter are always deﬁned, there might be instances where no saddle point exists. In this case, the supremum optimization might stall without getting to any stable solution, and the user might consider stopping the optimization after a certain number of iteration and outputting the current state as a solution. The average loss, despite its simple formulation, does not lead to an easy implementation either. Indeed, when given a set 𝑆, the average loss is implicitly computing the center of this set 𝑐(𝑆), and replacing 𝐿ac(𝑧, 𝑆) by ℓ(𝑧, 𝑐(𝑆)), more exactly

$$
∑︁ ∑︁
𝐿ac(𝑧, 𝑆) ≃−1 𝜑(𝑧)𝑇𝜑(𝑦) = −𝜑(𝑦)𝑇©­ 1 |𝑆| 𝜑(𝑦)ª®
.
|𝑆| « ¬
𝑦∈𝑆 𝑦∈𝑆
 
Í
1 |𝑆|
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

To compute the center , we sample 𝑐𝑘∼N (0, 𝐼𝑚2), solve the resulting minimum feedback arc set problem, with the constraint 𝑦∈𝑆, and end up with solutions 𝜑(𝑦𝑘). After removing duplicates, we estimate the average with the empirical one. Note that this work is done at training, leading the average loss to have a quite good inference complexity in O(𝑛𝑚+ NP(𝑚)) in time.

$$
𝑦∈𝑆𝜑(𝑦)
$$

2Coordinates of the Kendall’s embedding correspond to pairwise comparison between two items 𝑗and 𝑘, so we put to 0 the coordinates for which we can not infer preferences from 𝑆between items 𝑗and 𝑘.

<!-- page: 122 -->

Reconstruction IL Reconstruction AC Reconstruction SP

[FIGURE: Figure 7.11]

Figure 7.11: Reconstruction of the problem of Figure 7.3, given 𝑛= 50 random points (𝑥𝑖, 𝑦𝑖)𝑖≤𝑛, after losing at random ﬁfty percent of the coordinates (𝜑(𝑦𝑖))𝑖≤𝑛, leading to sets (𝑆𝑖)𝑖≤𝑛of potential candidates. Hyperparameter were chosen as 𝜎= 1 for the Gaussian kernel and 𝜆= 10−3𝑛−1/2 for the regularization parameter. The percentage of error in the reconstructed Kendall’s embedding is 3% for IL, 4% for AC and 13% for SP. As for classiﬁcation, with such a random corruption process, AC and IL show similar behaviors.

Synthetic example: ordering lines In the following, we explain our synthetic example of Section 7.5.2. It corresponds of choosing X = [0, 1], choose 𝑚a number of items, simulate 𝑎, 𝑏∼N (0, 𝐼𝑚), compute scores 𝑣𝑖(𝑥) = 𝑎𝑥+ 𝑏, and order items according to their scores as shown on Figure 7.3. For Figure 7.4, we chose 𝑚= 10, as this is the biggest 𝑚 for which can rely on our minimum feedback arc set heuristic to recover the real minimum feedback arc set solution and therefore not to play a role in what our algorithm will output. The corruption process was deﬁned as losing coordinates in the Kendall’s embedding, more exactly given a point 𝑥∈X, we have a score (𝑣𝑖(𝑥))𝑖≤𝑚and an ordering 𝑦∈Y. To create a skewed corruption, we ﬁrst compute the normalized distance between scores as

$$
𝑑𝑖𝑗= \frac{𝑣𝑖−𝑣𝑗}{max𝑘,𝑙|𝑣𝑘−𝑣𝑙| ∈[0, 1]}
$$

and remove the pairwise comparison for which 𝑑𝑖𝑗> 𝑐, where 𝑐is a corruption parameter between 0 and 1, formally

$$
∀( 𝑗, 𝑘) ∈𝐼, 𝜑(𝑧) 𝑗𝑘= 𝜑(𝑦) 𝑗𝑘 𝑑( 𝑗,𝑘) < 𝑐
𝑆= 𝑧∈Y , where 𝐼= ( 𝑗, 𝑘) ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Because of the transitivity constraint, when 𝑐is small the comparison that we lost can be found back using transitivity between comparisons.

Reproducibility speciﬁcation To get Figure 7.4, we generate eight problems that correspond to ordering 𝑚= 10 lines, seen as eight folds. We only cross validated results with the same heuristics as in Appendix 7.B.1, yet, because computations were expensive we only tried 𝑐𝜎∈{1, .5}, and 𝑐𝜆∈ 

103, 1, 10−3	. Again, randomness was controlled by instantiating random seeds to 0. Solving the linear program behind our minimum feedback arc set was done using Cplex (IBM, 2017), which is the fastest linear program solver we are aware of.

### 7.B.3 Multilabel

Multilabel is another application of partial labeling that we did not mention in our experiment section in the core paper. This omission was motivated by the fact that, under natural weak supervision, the three losses (inﬁmum, average and supremum) are basically the same. However, we will provide, now, an explanation of this problem and our algorithm to solve it.

Multilabel prediction consists in ﬁnding which are the relevant tags (possibly more than one) among 𝑚 potential tags. In this case, one can represent Y = {−1, 1}𝑚, with 𝑦𝑖= 1 (resp. 𝑦𝑖= −1), meaning that tag 𝑖is relevant (resp. not relevant). The classical loss is the Hamming loss, which is the decoupled sum of errors for each label:

$$
ℓ(𝑦, 𝑧) = \sum_{𝑚 𝑖=1} 1𝑦𝑖≠𝑧𝑖.
$$

<!-- page: 123 -->

7.B. EXPERIMENTS 121

[TABLE: Table 7.3]

Table 7.3: Complexity of our algorithm for multilabels.

| Complexity | Time | Space |
|---|---|---|
| Training | O(𝑛²(𝑛+ 𝑚)) | O(𝑛(𝑛+ 𝑚)) |
| Inference | O(𝑛𝑚) | O(𝑛+ 𝑚) |
| Inference top-𝑘 | O(𝑛𝑚+ 𝑚log(𝑚)) | O(𝑛+ 𝑚) |

Natural weak supervision consists in mentioning only a few relevant or irrelevant tags. This is the setting of Yu et al. (2014). This leads to sets 𝑆that are built from a set 𝑃of relevant items, and a set 𝑁of irrelevant items.

$$
𝑆= {𝑦∈Y | ∀𝑖∈𝑃, 𝑦𝑖= 1, ∀𝑖∈𝑁, 𝑦𝑖= −1} .
$$

In this case, the inﬁmum loss reads,

$$
𝐿(𝑧, 𝑆) = \sum_{𝑖∈𝑃} 1𝑧𝑖=−1 + \sum_{𝑖∈𝑁} 1𝑧𝑖=1.
$$

For such supervision, the inﬁmum, the average and the supremum loss are intrinsically the same, they only diﬀers by constants, due to the fact that for each unseen labels, the inﬁmum loss pays 0, the average loss 1/2 and the supremum loss 1.

When considering data (𝑥𝑖, 𝑆𝑖)𝑖≤𝑛, where (𝑆𝑖) is built from (𝑁𝑖, 𝑃𝑖), our algorithm in (7.7) reads ˆ𝑓(𝑥) = (sign( ˆ𝑓𝑗(𝑥))) 𝑗≤𝑚, based on the scores

$$
ˆ𝑓𝑗(𝑥) = \sum_{𝑖;𝑗∈𝑃𝑖} 𝛼𝑖(𝑥) − \sum_{𝑖;𝑗∈𝑁𝑖} 𝛼𝑖(𝑥).
$$

Tackling positive bias.

In the precedent development, we implicitly assumed that the ratio between positive and negative labels given by the weak supervision reﬂects the one of the full distribution. An assumption that is often violated in practice. It is common that partial labeling only mentions a subset of the relevant tags (i.e., 𝑁= ∅). This case is ill-conditioned as always outputting all tags (𝑦= 1) will minimize the inﬁmum loss. To solve this problem, we can constrain the prediction space to the top-𝑘space Y𝑘=

$$
𝑦∈Y Í𝑚
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

, which will lead to taking the top-𝑘over the score ( ˆ𝑓𝑗) 𝑗≤𝑚. We can also break the loss symmetry and add a penalization with 𝜀> 0,

$$
𝑦∈Y 𝑖=1 1𝑦𝑗=1 = 𝑘
𝑚 ∑︁
ℓ𝜀(𝑧, 𝑦) = ℓ(𝑧, 𝑦) + 𝜀 1𝑧𝑖=1.
𝑖=1
$$

In this case, the inference algorithm will threshold scores at 𝜀rather than 0.

Complexity analysis The complexity analysis is similar to the one for classiﬁcation. At training, we compute 𝐿= (1𝑗∈𝑃𝑖−1𝑗∈𝑁𝑖), and we solve for 𝛽= 𝐾−1 𝜆𝐿in R𝑛×𝑚. At testing, we compute 𝑣(𝑥) and 𝛽𝑇𝑣(𝑥) in R𝑚, before thresholding it or taking the top-𝑘in either O(𝑚) or O(𝑚log(𝑚)). As such, complexity reads similarly as for the classiﬁcation case. Yet notice that, for multilabeling, the dimension of Y is not 𝑚but 2𝑚, meaning we do not scale with #Y but with the intrinsic dimension.

Corruptions on the MULAN datasets When sets are given by few positive and negative tags, all losses are the same. Yet, under other types of supervision, such as when the sets come as Hamming balls, deﬁned by

$$
𝐵(𝑧, 𝑟) = {𝑦∈Y | ℓ(𝑧, 𝑦) ≤𝑟} ,
$$

the methods will not behave the same. We experiment on MULAN datasets provided by Tsoumakas et al. (2011). Because supervision with Hamming balls does not lead to eﬃcient implementation, we went for

<!-- page: 124 -->

scene IL AC SP 0.86 Loss 0.85 0 2 4 6 8 10 Corruption (p.d.u.)

[FIGURE: Figure 7.12]

Figure 7.12: Multilabeling. Testing risks (from (7.1)) achieved by AC and IL on the “scene” dataset from MULAN as a function of corruption parameter c, shown in procedure deﬁned unit, when the supervision is given as Hamming balls, as described in Section 7.B.3. extensive grid search for the best solution, which reduces our ability to consider large 𝑚. Among MULAN datasets, we went for the “scene” one, with 𝑚= 6 tags, and 𝑛= 2407 data. When given a pair (𝑥, 𝑦), we add corruption on 𝑦, by ﬁrst sampling a radius parameter 𝑟∼U (() [0, 𝑐∗(𝑚+1)]), with 𝑐a corruption parameter. We then sample, with replacement, ⌊𝑟⌋coordinates to modify to pass from 𝑦to a center 𝑐. We then consider the supervision 𝑆= 𝐵(𝑐, 𝑟). For such randomness, somehow uniform corruption, the inﬁmum loss works slightly better than the average loss that both outperform the supremum loss as shown on Figure 7.12.

Reproducibility speciﬁcation To get Figure 7.12, we follow the same cross-validation scheme as for classiﬁcation and ranking. More exactly, we cross-validated over eight folds with the same heuristics for 𝜎, the Gaussian kernel parameter, and 𝜆, the regularization one, with 𝑐𝜎∈{10, 5, 1, .5, .1, .01}, and 𝑐𝜆∈

$$
10𝑖 𝑖∈⟦−3, 3⟧ .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

### 7.B.4 Partial regression

Partial regression is the regression instance of partial labeling. When supervision comes as intervals, it is known as interval regression, and known as censored regression when sets come as half-lines. Note that for censored regression, neither the average, nor the supremum loss can be properly deﬁned.

Baselines Given a bounded set 𝑆, learning with the average loss corresponds to considering the center of this set, since, for 𝑧∈Y, with 𝜆the Lebesgue measure

$$
∫ ∫ ∫
𝐿ac(𝑧, 𝑆) = 1 𝜆(𝑆) 𝑧, 1 𝜆(𝑆) + 1 𝜆(𝑆)
∥𝑧−𝑦∥2 𝜆(d𝑦) = ∥𝑧∥2 −2 𝑦𝜆(d𝑦) ∥𝑦∥2 𝜆(d𝑦)
𝑧− 1 𝜆(𝑆) 𝑆 ∫ ∫ 𝑆 ∫ 𝑆
2 + 1 𝜆(𝑆) 1 𝜆(𝑆) 2 = ∥𝑧−𝑐(𝑆)∥2 + 𝐶𝑆,
= 𝑦𝜆(d𝑦) ∥𝑦∥2 𝜆(d𝑦) − 𝑦𝜆(d𝑦)
𝑆 𝑆 𝑆
∫
$$

where 𝑐(𝑆) = 1 𝜆(𝑆) 𝑆𝑦𝜆(d𝑦) is the center of 𝑆. As such, the average loss is always convex. As the supremum of convex function, the supremum loss is also convex.

Reproducibility speciﬁcation To compute Figure 7.5, for both AC and IL, we consider 𝜎, the Gaussian kernel parameter, and 𝜆, the regularization parameter, achieving the best risk when measured with the fully supervised distribution (7.1). We tried over 𝜎∈{1, .5, .1, .05, .01} and 𝜆∈ 

103, 1, 10−3	. Randomness was controlled by instantiating random seeds.

<!-- page: 125 -->

7.C. MINIMUM FEEDBACK ARC SET 123

### 7.B.5 Beyond

Beyond the examples showcased previously, advances in dealing with weak supervision could be beneﬁcial for several problems. Supervision on image segmentation problems usually comes as partial pixel annotation. This problem is often tackled through conditional random ﬁelds (Verbeek and Triggs, 2008), making it a perfect mix between partial labeling and structured prediction. Action retrieval on instructional video, where partial supervision is retrieved from the audio track is another interesting application (Alayrac, 2018).

## 7.C Minimum feedback arc set 7.C.1 Formulation

Consider a directed weighted graph with vertices ⟦1, 𝑚⟧and edges {𝑖→𝑗} with weights (𝑤𝑖𝑗)𝑖,𝑗≤𝑚∈R𝑚2 + . The goal is to ﬁnd a directed acyclic graph 𝐺= (𝑉, 𝐸) that maximizes the weights on remaining edges

$$
\underset{𝐸}{\arg\max}\, \sum_{𝑖→𝑗∈𝐸} 𝑤𝑖𝑗.
$$

This directed acyclic graph can be seen as a preference graph, item 𝑗being preferred over item 𝑖. Since 𝑤𝑖𝑗 are non-negative, the underlying ordering in 𝐺is necessarily total, and therefore can be written based on a score function, that can be embedded in the permutation of ⟦1, 𝑚⟧, 𝜎∈S𝑚, with 𝜎( 𝑗) > 𝜎(𝑖) meaning that 𝑗is preferred over 𝑖. Thus the problem reads equivalently

$$
∑︁ ∑︁ ∑︁
arg max 𝑤𝑖𝑗1𝜎( 𝑗)>𝜎(𝑖) = arg max 𝑐𝑖𝑗1𝜎( 𝑗)>𝜎(𝑖) = arg max 𝑐𝑖𝑗sign (𝜎( 𝑗) −𝜎(𝑖))
𝜎∈S𝑚 𝑖,𝑗≤𝑚 𝜎∈S𝑚 𝑖< 𝑗≤𝑚 ∑︁ 𝜎∈S𝑚 𝑖< 𝑗≤𝑚 ∑︁
= arg min 𝑐𝑖𝑗sign (𝜎(𝑖) −𝜎( 𝑗)) = arg min 𝑐𝑖𝑗1𝜎(𝑖)>𝜎( 𝑗)
𝜎∈S𝑚 𝑖< 𝑗≤𝑚 𝜎∈S𝑚 𝑖< 𝑗≤𝑚
$$

with 𝑐𝑖𝑗= 𝑤𝑖𝑗−𝑤𝑗𝑖. This last formulation is the one usually encountered for ranking algorithms in machine learning (Duchi et al., 2010).

We are going to study in depth this problem under the formulation

$$
∑︁
arg min 𝑐𝑖𝑗sign (𝜎(𝑖) −𝜎( 𝑗)) (7.9)
𝜎∈S𝑚 𝑖< 𝑗≤𝑚
$$

(7.9)

### 7.C.2 Integer linear programming

Deﬁnition 50 (Kendall’s embedding). For 𝜎∈S𝑚, deﬁne Kendall’s embedding, with 𝑚𝑒= 𝑚(𝑚−1)/2,

$$
𝜑(𝜎) = sign (𝜎(𝑖) −𝜎( 𝑗))𝑖< 𝑗≤𝑚∈{−1, 1}𝑚𝑒.
$$

We associate it to the Kendall’s polytope of order 𝑚, Conv (𝜑(S𝑚)).

The Kendall’s embedding, Deﬁnition 50, cast the minimum feedback arcset problem (7.9) as a linear program minimize ⟨𝑐, 𝑥⟩ subject to 𝑥∈Conv (𝜑(S𝑚)) .

Since the objective is linear, the solution is known to lie on a vertex of the constraint polytope, which is the set of Kendall’s embeddings of permutations. Yet, how to describe Kendall’s polytope?

Deﬁnition 51 (Transitivity polytope). The transitivity polytope of order 𝑚is deﬁned in R𝑚𝑒as

$$
𝑥∈R𝑚𝑒 ∀𝑖< 𝑘< 𝑗; −1 ≤𝑥𝑖𝑗+ 𝑥𝑗𝑘−𝑥𝑖𝑘≤1
M =
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This polytope encodes the transitivity constraints of Kendall’s embeddings, Deﬁnition 50.

The transitivity polytope, Deﬁnition 53, will be used to approximate Kendall’s polytope based on the following property.

<!-- page: 126 -->

Percentage of perfect solutions (10000 runs) 100.0 Percentage of perfect solutions (10000 runs) 100 Solution recovery (%) 80 99.8 99.6 60 99.4 40 99.2 5 10 15 20 25 30 20 4 6 8 10

[FIGURE: Figure 7.13]

Figure 7.13: Evaluating the percentage of exact solutions of the ILP relaxation as 𝑚grows large. Evaluation is done by choosing an objective 𝑐∼N (0, 𝐼𝑚𝑒), solving the ILP relaxation, Deﬁnition 53, and evaluating if the solution is in {−1, 1}𝑚𝑒. The experience is repeated several times to estimate how often, on average, the original solution of (7.9) is returned by the ILP.

Proposition 52 (Relaxed polytope). The intersection between the transitivity polytope and the vertex of the hypercube is exactly the set of Kendall’s embeddings of permutations. Mathematically

$$
𝜑(S𝑚) = M ∩{−1, 1}𝑚𝑒.
$$

Proof. First of all it is easy to show that 𝜑(S𝑚) ⊂{−1, 1}𝑚𝑒, and that, 𝜑(S𝑚) ⊂M.

Let’s now consider 𝑥∈M ∩{−1, 1}𝑚𝑒. Let’s associate to 𝑥the symmetric embedding

$$
˜𝑥𝑖𝑗= \frac{}{} 𝑥𝑖𝑗 0 −𝑥𝑗𝑖 if if if 𝑖< 𝑗 𝑖= 𝑗 𝑗< 𝑖
$$

Let’s consider the permutation 𝜎resulting from the ordering of Í

$$
𝑘˜𝑥𝑖𝑘
𝑚 ∑︁ 𝑚 ∑︁
𝜎−1(1) = arg min
$$

˜𝑥𝑖𝑘 and 𝜎−1(𝑖) = arg min 𝑖∈⟦1,𝑚⟧\𝜎−1(⟦1,𝑖−1⟧)

$$
˜𝑥𝑖𝑘.
𝑖∈⟦1,𝑚⟧ 𝑘=1 𝑘=1
$$

Let’s now show that 𝜑(𝜎) = 𝑥, or equivalently that ˜𝜑(𝜎) = (sign(𝜎(𝑖) −𝜎( 𝑗)))𝑖,𝑗≤𝑚= ˜𝑥. First, one can show that ˜𝑥verify the transitivity constraints

$$
∀𝑖, 𝑗, 𝑘≤𝑚, −1 ≤˜𝑥𝑖𝑗+ ˜𝑥𝑗𝑘−˜𝑥𝑖𝑘≤1.
$$

This can be proven for any ordering of 𝑖, 𝑗, 𝑘based on the fact that 𝑥∈M. For example, if 𝑖< 𝑘< 𝑗, we have

$$
[−1, 1] ∋𝑥𝑖𝑘+ 𝑥𝑘𝑗−𝑥𝑖𝑗= ˜𝑥𝑖𝑘−˜𝑥𝑗𝑘−˜𝑥𝑖𝑗.
$$

which leads to

$$
˜𝑥𝑖𝑗+ ˜𝑥𝑗𝑘−˜𝑥𝑖𝑘∈−[−1, 1] = [−1, 1] .
$$

Now suppose, without loss of generality, that ˜𝑥𝑖𝑗= 1 (if ˜𝑥𝑖𝑗= −1, just consider ˜𝑥𝑗𝑖= 1). The transitivity constraints tell us that ˜𝑥𝑖𝑘≥˜𝑥𝑗𝑘for all 𝑘, therefore

$$
∑︁ ∑︁ 𝑚 ∑︁ 𝑚 ∑︁
˜𝑥𝑖𝑘≥ ˜𝑥𝑗𝑘, ⇒ ˜𝑥𝑖𝑘> ˜𝑥𝑗𝑘. ⇒ 𝜎(𝑖) > 𝜎( 𝑗).
𝑘∉{𝑖,𝑗} 𝑘∉{𝑖,𝑗} 𝑘=1 𝑘=1
$$

This shows that ˜ 𝜑(𝜎)𝑖𝑗= 1 = ˜𝑥𝑖𝑗. Thus, we have shown that 𝑥∈𝜑(S𝑚), which concludes the proof. □ Deﬁnition 53 (ILP relaxation). Based on Proposition 52, we deﬁne the canonical polytope C = M∩[−1, 1]𝑚𝑒, and relax the problem (7.9) into

$$
\frac{minimize}{subject to} \frac{⟨𝑐, 𝑥⟩}{𝑥∈C}
$$

As soon as the solution 𝑥is in {−1, 1}𝑚𝑒, Proposition 52 tells us that 𝑥recover the exact minimum feedback arc set solution (7.9).

<!-- page: 127 -->

7.C. MINIMUM FEEDBACK ARC SET 125 In small dimensions, the canonical polytope C is the same as the Kendall’s one, and the ILP relaxation gives the right solution. Yet, as shown in Figure 7.13, as soon as 𝑚> 5, there exists vertex in C that does not correspond to a permutation embedding. For small dimensions, proving that C is exactly the Kendall’s polytope is done with a simple drawing for 𝑚= 3, using unimodularity of the transitivity constraint matrix is enough for 𝑚= 4 (Hoﬀman and Kruskal, 2010). The case 𝑚= 5 is also provable, based on several tricks that we will not discuss here.

Remark 54 (Low noise consistency). Remark that the low-noise setting considered by Duchi et al. (2010) correspond to having sign(𝑐) = −𝜑(𝑦) for a 𝑦∈Y, in this case our algorithm is consistent and does recover the best solution 𝑧= 𝑦.

### 7.C.3 Sorting heuristics

When formatting and solving the integer linear program takes too much time, one can go for a simple sorting heuristic, mainly based on a heuristic to compare items two by two and using quick sorting. A review of some heuristic with guarantees is provided by Ailon et al. (2005), Similar study when in presence of constraints on the resulting total order can be found in van Zuylen et al. (2007).

<!-- page: 128 -->

<!-- page: 129 -->

# Chapter 8. Disambiguation Framework

The following is a reproduction of Cabannes et al. (2021b).

Machine learning approached through supervised learning requires expensive annotation of data. This motivates weakly supervised learning, where data are annotated with incomplete yet discriminative information. In this paper, we focus on partial labeling, an instance of weak supervision where, from a given input, we are given a set of potential targets. We review disambiguation principles to recover full supervision from weak supervision, and propose an empirical disambiguation algorithm. We prove exponential convergence rates of our algorithm under classical learnability assumptions, and we illustrate the usefulness of our method on practical examples.

## 8.1 Introduction

In many applications of machine learning, such as recommender systems, where an input 𝑥characterizing a user should be matched with a target 𝑦representing an ordering of a large number 𝑚of items, accessing fully supervised data (𝑥, 𝑦) is not an option. Instead, one should expect weak information on the target 𝑦, which could be a list of previously taken (if items are online courses), watched (if items are plays), etc., items by a user characterized by the feature vector 𝑥. This motivates weakly supervised learning, aiming at learning a mapping from inputs to targets in such a setting where tools from supervised learning can not be applied oﬀ-the-shelves.

Recent applications of weakly supervised learning showcase impressive results in solving complex tasks such as action retrieval on instructional videos (Miech et al., 2019), image semantic segmentation (Papandreou et al., 2015), salient object detection (Wang et al., 2017), 3D pose estimation (Dabral et al., 2018), text-to-speech synthesis (Jia et al., 2018), to name a few. However, those applications of weakly supervised learning are usually based on clever heuristics, and theoretical foundations of learning from weakly supervised data are scarce, especially when compared to statistical learning literature on supervised learning (Vapnik, 1995; Boucheron et al., 2005; Steinwart and Christmann, 2008). We aim to provide a step in this direction.

In this paper, we focus on partial labeling, a popular instance of weak supervision, approached with a structured prediction point of view Ciliberto et al. (2020). We detail this setup in Section 8.2. Our contributions are organized as follows.

• In Section 8.3, we introduce a disambiguation algorithm to retrieve fully supervised samples from weakly supervised ones, before applying oﬀ-the-shelf supervised learning algorithms to the completed dataset. • In Section 8.4, we prove exponential convergence rates of our algorithm, in terms of the fully supervised excess of risk, given classical learnability assumptions. • In Section 8.5, we explain why disambiguation algorithms are intrinsically non-convex, and provide guidelines based on well-grounded heuristics to implement our algorithm. We end this paper with a review of literature in Section 8.6, before showcasing the usefulness of our method on practical examples in Section 8.7, and opening on perspectives in Section 8.8.

127

<!-- page: 130 -->

## 8.2 Disambiguation of partial labeling

In this section, we review the supervised learning setup, introduce the partial labeling problem along with a principle to tackle this instance of weak supervision.

Algorithms can be formalized as mapping an input 𝑥to a desired output 𝑦, respectively belonging to an input space X and an output space Y. Machine learning consists in automating the design of the mapping 𝑓: X →Y, based on a joint distribution 𝜇∈ΔX×Y over input/output pairings (𝑥, 𝑦) and a loss function ℓ: Y × Y →R, measuring the error cost of outputting 𝑓(𝑥) when one should have output 𝑦. The optimal mapping is deﬁned as satisfying

$$
𝑓∗∈arg min E(𝑋,𝑌)∼𝜇[ℓ( 𝑓(𝑋),𝑌)] . (8.1)
𝑓:X→Y
$$

(8.1)

In supervised learning, it is assumed that one does not have access to the full distribution 𝜇, but only to independent samples (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼𝜇⊗𝑛. In practice, accessing such samples means building a dataset of examples. While input data (𝑥𝑖) are usually easily accessible, getting output pairings (𝑦𝑖) generally requires careful annotation, which is both time-consuming and expensive. For example, in image classiﬁcation, (𝑥𝑖) can be collected by scrapping images over the Internet. Subsequently, a “data labeler” might be asked to recognize a rare feline 𝑦𝑖on an image 𝑥𝑖. While getting 𝑦𝑖will be hard in this setting, recognizing that it is a feline and describing elements of color and shape is easy, and already helps to determine what outputs 𝑓(𝑥𝑖) are acceptable. A second example is given when pooling a known population (𝑥𝑖) to get estimation of their political orientation (𝑦𝑖), one might get information from recent election of percentage of voters across the political landscape, leading to global constraints that (𝑦𝑖) should verify. A supervision that gives information on (𝑦𝑖)𝑖≤𝑛without giving its precise value is called weak supervision.

Partial labeling, also known as “superset learning”, is an instance of weak supervision, in which, for an input 𝑥, we do not access the precise label 𝑦but only a set 𝑠of potential labels, 𝑦∈𝑠⊂Y. For example, on a caracal image 𝑥, one might not get the label “caracal” 𝑦, but the set 𝑠“feline”, containing all the labels 𝑦 corresponding to felines. It is modelled through a distribution 𝜈∈ΔX×2Y over X × 2Y generating samples (𝑋, 𝑆), which should be compatible with the fully supervised distribution 𝜇∈ΔX×Y as formalized by the following deﬁnition.

Deﬁnition 55 (Compatibility, Cabannes et al. (2020b)). A fully supervised distribution 𝜇∈ΔX×Y is compatible with a weakly supervised distribution 𝜈∈ΔX×Y, denoted by 𝜇⊢𝜈if there exists an underlying distribution 𝜋∈ΔX×Y×2Y, such that 𝜇, and 𝜈, are the respective marginal distributions of 𝜋over X × Y and X × 2Y, and such that 𝑦∈𝑠for any tuple (𝑥, 𝑦, 𝑠) in the support of 𝜋(or equivalently 𝜋|𝑠∈Δ𝑠, with 𝜋|𝑠 denoting the conditional distribution of 𝜋given 𝑠).

This deﬁnition means that a weakly supervised sample (𝑋, 𝑆) ∼𝜈can be thought as proceeding from a fully supervised sample (𝑋,𝑌) ∼𝜇after losing information on 𝑌according to the sampling of 𝑆∼𝜋|𝑋,𝑌. The goal of partial labeling is still to learn 𝑓∗from (8.1), yet without accessing a fully supervised distribution 𝜇∈ΔX×Y but only the weakly supervised distribution 𝜈∈ΔX×2Y. As such, this is an ill-posed problem, since 𝜈does not discriminate between all 𝜇compatible with it. Following lex parsimoniae, Cabannes et al. (2020b) have suggested looking for 𝜇such that the labels are the most deterministic function of the inputs, which they measure with a loss-based “variance”, leading to the disambiguation

$$
𝜇∗∈arg min inf 𝑓:X→Y E(𝑋,𝑌)∼𝜇[ℓ( 𝑓(𝑋),𝑌)] , (8.2)
𝜇⊢𝜈
$$

(8.2)

and to the deﬁnition of the optimal mapping 𝑓∗: X →Y

$$
𝑓∗∈arg min E(𝑋,𝑌)∼𝜇∗[ℓ( 𝑓(𝑋),𝑌)] . (8.3)
𝑓:X→Y
$$

(8.3)

This principle is motivated by Theorem 1 of Cabannes et al. (2020b) showing that 𝑓∗in (8.3) is characterized by 𝑓∗∈arg min 𝑓:X→Y E(𝑋,𝑆)∼𝜈 

, matching a prior formulation based on inﬁmum loss (Cour et al., 2011; Luo and Orabona, 2010; Hüllermeier, 2014). In practice, it means that if (𝑆|𝑋= 𝑥) has probability 50% to be the set “feline” and 50% the set “orange with black stripes”, (𝑌|𝑋= 𝑥) should be considered as 100% “tiger”, rather than 20% “cat”, 30% “lion” and 50% “orange car with black stripes”, which could also explain (𝑆|𝑋= 𝑥). Similarly to supervised learning, partial labeling consists in retrieving

$$
inf𝑦∈𝑆ℓ( 𝑓(𝑋), 𝑦)
$$

𝑓∗without accessing 𝜈but only samples (𝑋𝑖, 𝑆𝑖)𝑖≤𝑛∼𝜈⊗𝑛.

<!-- page: 131 -->

Remark 56 (Measure of determinism). (8.2) is not the only variational way to push toward distribution where labels are deterministic function of the inputs. For example, one could minimize entropy (e.g., Berthelot et al., 2019; Lienen and Hüllermeier, 2021). However, a loss-based principle is appreciable since the loss usually encodes structures of the output space (Ciliberto et al., 2020), which will allow sample and computational complexity of consequent algorithms to scale with an intrinsic dimension of the space rather than the real one, e.g., 𝑚rather than 𝑚! when Y = S𝑚and ℓis a suitable ranking loss (see Section 8.5.4 or Nowak-Vila et al., 2019).

## 8.3 Learning algorithm

In this section, given weakly supervised samples, we present a disambiguation algorithm to retrieve fully supervised samples based on an empirical expression of (8.2), before learning a mapping from X to Y based on those fully supervised samples, according to (8.3).

Given a partially labeled dataset D𝑛= (𝑥𝑖, 𝑠𝑖)𝑖≤𝑛, sampled accordingly to 𝜈⊗𝑛, we retrieve fully supervised samples, based on the following empirical version of (8.2), with 𝐶𝑛= Î

$$
𝑖≤𝑛𝑠𝑖⊂Y𝑛
𝑛 ∑︁
( ˆ𝑦𝑖)𝑖≤𝑛∈arg min inf (𝑧𝑖)𝑖≤𝑛∈Y𝑛 𝛼𝑗(𝑥𝑖)ℓ(𝑧𝑖, 𝑦𝑗), (8.4)
(𝑦𝑖)𝑖≤𝑛∈𝐶𝑛 𝑖,𝑗=1
$$

(8.4)

where (𝛼𝑖(𝑥))𝑖≤𝑛is a set of weights measuring how much one should base its prediction for 𝑥on the observations made at 𝑥𝑖. This formulation is motivated by the Bayes approximate rule proposed by Stone (1977), which can be seen as the approximation of 𝜇by 𝑛−1 Í𝑛 𝑖,𝑗=1 𝛼𝑗(𝑥𝑖)𝛿𝑥𝑖⊗𝛿𝑦𝑗in (8.2). Once fully supervised samples (𝑥𝑖, ˆ𝑦𝑖) have been recollected, one can learn 𝑓𝑛: X →Y, approximating 𝑓∗, with classical supervised learning techniques. In this work, we will consider the structured prediction estimator introduced by Ciliberto et al. (2016), deﬁned as

$$
𝑛 ∑︁
𝑓𝑛(𝑥) ∈arg min 𝛼𝑖(𝑥)ℓ(𝑧, ˆ𝑦𝑖). (8.5)
𝑧∈Y 𝑖=1
$$

(8.5)

Weighting scheme 𝛼. For the weighting scheme 𝛼, several choices are appealing. Laplacian diﬀusion is one of them as it incorporates a prior on low density separation to boost learning (Zhu et al., 2003; Zhou et al., 2003; Bengio et al., 2006; Hein et al., 2007). Kernel ridge regression is another due to its theoretical guarantees (Ciliberto et al., 2020). In the theoretical analysis, we will use nearest neighbors. Assuming X is endowed with a distance 𝑑, and assuming, for readability’ sake, that ties to deﬁne nearest neighbors do not happen, it is deﬁned as

$$
𝛼𝑖(𝑥) = \frac{ 𝑘−1}{0} if Í𝑛 \frac{𝑗=1 1𝑑(𝑥,𝑥𝑗) ≤𝑑(𝑥,𝑥𝑖) ≤𝑘}{otherwise,}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑘is a parameter ﬁxing the number of neighbors. Our analysis, leading to Theorem 15, also holds for other local averaging methods such as partitioning or Nadaraya-Watson estimators.

## 8.4 Consistency result

In this section, we assume Y ﬁnite, and prove the convergence of 𝑓𝑛toward 𝑓∗as 𝑛, the number of samples, grows to inﬁnity. To derive such a consistency result, we introduce a surrogate problem that we relate to the risk through a calibration inequality. We later assume that weights are given by nearest neighbors and review classical assumptions, that we work to derive exponential convergence rates.

In the following, we are interested in bounding the expected generalization error, deﬁned as

$$
E( 𝑓𝑛) = ED𝑛R( 𝑓𝑛) −R( 𝑓∗), (8.6)
$$

(8.6)

where R( 𝑓) = E(𝑋,𝑌)∼𝜇∗[ℓ( 𝑓(𝑋),𝑌)] , by a quantity that goes to zero, when 𝑛goes to inﬁnity. This implies, under boundedness of ℓ, convergence in probability (the randomness being inherited from D𝑛) of R( 𝑓𝑛) toward inf 𝑓:X→Y R( 𝑓), which is referred as consistency of the learning algorithm.1 We ﬁrst introduce a few objects.

$$
1If E |𝑋| < +∞and E[|𝑋𝑛−𝑋|] →0, 𝑋𝑛→𝑋in probability.
$$

<!-- page: 132 -->

𝑖). Introduce 𝜋∗∈ΔX×Y×2Y expressing the compatibility of 𝜇∗and 𝜈 as in Deﬁnition 55. Given samples (𝑥𝑖, 𝑠𝑖)𝑖≤𝑛forming a dataset D𝑛, we enrich this dataset by sampling 𝑦∗ Disambiguation ground truth (𝑦∗ 𝑖∼𝜋∗|𝑥𝑖,𝑠𝑖, which build an underlying dataset (𝑥𝑖, 𝑦∗ 𝑖, 𝑠𝑖) sampled accordingly (𝜋∗) ⊗𝑛. Given D𝑛, while a priori, 𝑦∗ 𝑖are random variables, sampled accordingly to 𝜋∗|𝑥𝑖,𝑠𝑖, because of the deﬁnition of 𝜇∗(8.2), under basic deﬁnition assumptions, they are actually deterministic, deﬁned as 𝑦∗ 𝑖= arg min𝑦∈𝑠𝑖ℓ( 𝑓∗(𝑥𝑖), 𝑦). As such, they should be seen as ground truth for ˆ𝑦𝑖.

Surrogate estimates. The approximate Bayes rule was successfully analyzed recently through the prism of plug-in estimators by Ciliberto et al. (2020). While we will not cast our algorithm as a plug-in estimator, we will leverage this surrogate approach, introducing two mappings 𝜑and 𝜓from Y to a Hilbert space H such that

$$
∀𝑧, 𝑦∈Y, ℓ(𝑧, 𝑦) = ⟨𝜓(𝑧), 𝜑(𝑦)⟩, (8.7)
$$

(8.7)

Such mappings always exist when Y is ﬁnite, and have been used to encode “problem structure” deﬁned by the loss ℓ(Nowak-Vila et al., 2019). We introduce three surrogate quantities that will play a major role in the following analysis, they map X to H as

$$
𝑛 ∑︁
𝑔∗(𝑥) = E𝜇∗[𝜑(𝑌) | 𝑋= 𝑥] , 𝑔𝑛(𝑥) = 𝛼𝑖(𝑥)𝜑( ˆ𝑦𝑖),
𝑖=1
𝑛 ∑︁
𝑔∗ 𝑛(𝑥) = 𝛼𝑖(𝑥)𝜑(𝑦∗ 𝑖). (8.8)
𝑖=1
$$

(8.8)

It is known that 𝑓∗and 𝑓𝑛are retrieved from 𝑔∗and 𝑔𝑛, through the decoding, retrieving 𝑓: X →Y from 𝑔: X →H as

$$
𝑓(𝑥) = arg min ⟨𝜓(𝑧), 𝑔(𝑥)⟩, (8.9)
𝑧∈Y
$$

(8.9)

which explains the wording of plug-in estimator (Ciliberto et al., 2020). We now introduce a calibration inequality, that relates the error between 𝑓𝑛and 𝑓∗with surrogate error quantities.

Lemma 57 (Calibration inequality). When Y is ﬁnite, and the labels are a deterministic function of the input, i.e., when 𝜇∗|𝑥is a Dirac for all 𝑥∈supp 𝜈X , for any weighting scheme such that Í𝑛 𝑖=1 |𝛼𝑖(𝑥)| ≤1 for all 𝑥∈supp 𝜈X ,

$$
𝑔∗
R( 𝑓𝑛) −R( 𝑓∗) ≤4𝑐𝜓 

𝑔∗ 𝑛−𝑔𝑛 > 𝛿 , (8.10)
𝐿1 + 8𝑐𝜓𝑐𝜑P𝑋
𝑛(𝑋) −𝑔∗(𝑋)
$$

(8.10)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑐𝜓= sup𝑧∈Y ∥𝜓(𝑧)∥, 𝑐𝜑= sup𝑧∈Y ∥𝜑(𝑦)∥, and 𝛿a parameter that depend on the geometry of ℓand its decomposition through 𝜑.

$$
\frac{𝑔𝑛−𝑔∗}{𝑛}
$$

, due to the disambiguation error between ( ˆ𝑦𝑖) and (𝑦∗ This lemma, proven in Appendix 8.A.1, separates a part reading in

$$
𝑛
𝑔∗
$$

𝑛−𝑔∗

 due to the consistency of the fully supervised learning algorithm. The expression of the ﬁrst part relates to Theorem 7 in Ciliberto et al. (2020) while the second part relates to Theorem 6 in Cabannes et al. (2021c).

𝑖) together with the stability of the learning algorithm when substituting ( ˆ𝑦𝑖) for (𝑦∗ 𝑖), and a part in

### 8.4.1 Classical learnability assumptions

In the following, we suppose that the weights 𝛼are given by nearest neighbors, that X is a compact metric space endowed with a distance 𝑑, that Y is ﬁnite and that ℓis proper in the sense that it strictly positive except on the diagonal of Y × Y diagonal where it is zero. We now review classical assumptions to prove consistency. First, assume that 𝜈X is regular in the following sense.

Assumption 14 (𝜈X well-behaved). Assume that 𝜈X is such that there exists ℎ1, 𝑐𝜇, 𝑞> 0 satisfying, with B designing balls in X,

$$
∀𝑥∈supp 𝜈X , ∀𝑟< ℎ1, 𝜈X (B(𝑥, 𝑟)) > 𝑐𝜇𝑟𝑞.
$$

<!-- page: 133 -->

Assumption 14 is useful to make sure that neighbors in D𝑛are closed with respect to the distance 𝑑, it is usually derived by assuming that X is a subset of R𝑞; that 𝜈X has a density 𝑝against the Lebesgue measure 𝜆with minimal mass 𝑝min in the sense that for any 𝑥∈supp 𝜈X , 𝑝(𝑥) > 𝑝min; and that supp 𝜈X has regular boundary in the sense that 𝜆(B(𝑥, 𝑟) ∩supp 𝜈X ) ≥𝑐𝜆(B(𝑥, 𝑟) for any 𝑥∈supp 𝜈X and 𝑟< ℎ(e.g., Audibert and Tsybakov, 2007).

We now switch to a classical assumption in partial labeling, allowing for population disambiguation.

Assumption 15 (Non ambiguity, Cour et al. (2011)). Assume the existence of 𝜂∈[0, 1), such that for any 𝑥∈supp 𝜈X , there exists 𝑦𝑥∈Y, such that P𝜈(𝑦𝑥∈𝑆| 𝑋= 𝑥) = 1, and

$$
∀𝑧≠𝑦𝑥, P𝜈(𝑧∈𝑆| 𝑋= 𝑥) ≤𝜂.
$$

Assumption 15 states that when given the full distribution 𝜈, there is one, and only one, label that is coherent with every observable sets for a given input. It is a classical assumption in literature about the learnability of the partial labeling problem (e.g., Liu and Dietterich, 2014). When ℓis proper, this implies that 𝜇∗|𝑥= 𝛿𝑦𝑥, and 𝑓∗(𝑥) = 𝑦𝑥.

Finally, we assume that 𝑔∗is regular. As we are considering local averaging method, we will use Lipschitz-continuity, which is classical in such a setting.2 Assumption 16 (Regularity of 𝑔∗). Assume that there exists 𝑐𝑔> 0, such that for any 𝑥, 𝑥′ ∈X, we have

$$
∥𝑔∗(𝑥) −𝑔∗(𝑥′)∥H ≤𝑐𝑔𝑑(𝑥, 𝑥′).
$$

It should be noted that regularity of 𝑔∗, Assumption 16, together with determinism of 𝜇∗|𝑥inherited from Assumption 15 implies that classes X𝑦= {𝑥| 𝑓∗(𝑥) = 𝑦} are separated in X, in the sense that there exists ℎ2 > 0, such that for any 𝑦, 𝑦′ ∈Y and (𝑥, 𝑥′) ∈X𝑦× X𝑦′, 𝑑(𝑥, 𝑥′) > ℎ2, which is a classical assumption to derive consistency of semi-supervised learning algorithm (e.g., Rigollet, 2007). We detailed those implications in Appendix 8.A.2.

### 8.4.2 Exponential convergence rates

We are now ready to state our convergence result. We introduce ℎ= min(ℎ1, ℎ2) and 𝑝= 𝑐𝜇ℎ𝑞, so that for any 𝑥∈supp 𝜈X , 𝜈X (B(𝑥, ℎ)) > 𝑝.

Theorem 15 (Exponential convergence rates). When the weights 𝛼are given by nearest neighbors, under Assumptions 14, 15 and 16, the excess of risk in (8.6) is bounded by

$$
−𝑛𝑝
E( 𝑓𝑛) ≤8𝑐𝜓𝑐𝜑(𝑛+ 1) exp
16
+ 8𝑐𝜓𝑐𝜑𝑚exp (−𝑘|log(𝜂)|) , (8.11)
$$

(8.11)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

as soon as 𝑘< 𝑛𝑝/4, with 𝑚= |Y|. By taking 𝑘𝑛= 𝑘0𝑛, for 𝑘0 < 𝑝/4, this implies exponential convergence rates E( 𝑓𝑛) = 𝑂(𝑛exp(−𝑛)).

Sketch for Theorem 15. In essence, based on Lemma 57, Theorem 15 can be understood as two folds.

• A fully supervised error between 𝑔∗ 𝑛and 𝑔∗. This error can be controlled in exp(−𝑛𝑝) as the non- ambiguity assumption implies a hard Tsybakov margin condition, a setting in which the fully supervised estimate 𝑔∗ 𝑛is known to converge to the population solution 𝑔∗with such rates (Cabannes et al., 2021c). • A weakly disambiguation error, that is exponential too, since, based on Assumption 15, disambiguating between 𝑧∈Y and 𝑦𝑥from 𝑘sets 𝑆sampled accordingly to 𝜈|𝑥can be done in 𝜂𝑘, and disambiguating between all 𝑧≠𝑦𝑥and 𝑦𝑥in 𝑚𝜂𝑘= 𝑚exp(−𝑘|log(𝜂)|). Appendix 8.A.3 provides details. □ Theorem 15 states that under a non-ambiguity assumption and a regularity assumption implying no-density separation, one can expect exponential convergence rates of 𝑓𝑛learned with weakly supervised data to 𝑓∗the solution of the fully supervised learning problem, measured with excess of fully supervised risk. Because of exponential convergence rates, we could expect polynomial convergence rates for a broader class of problems that are approximated by problems satisfying assumptions of Theorem 15. The derived rates in 𝑛exp(−𝑛) should be compared with rates in 𝑛−1/2 and 𝑛−1/4, respectively derived, under the same assumptions, by Cour et al. (2011); Cabannes et al. (2020b).

2Its generalization through Hölder-continuity would work too.

<!-- page: 134 -->

### 8.4.3 Discussion on assumptions

While we have retaken classical assumptions from literature, those assumptions are quite strong, which allows us, by understanding their strength, to derive exponential convergence rates. Assumptions 14 and 16 are classical in the nearest neighbor literature with full supervision. If we were using (reproducing) kernel methods to deﬁne the weighting scheme 𝛼, those assumptions would be mainly replaced with “𝑔∗belonging to the RKHS”. Assumption 15 is the strongest assumption in our view, that we will now discuss.

How to check it in practice ? First, for Assumption 15 to hold, the labels have to be a deterministic function of the inputs. In other words, a zero error is achievable. Finally, Assumption 15 is related to dataset collection. If dealing with images, weak supervision could take the form of some information on shape, color, or texture, etc., Assumption 15 supposes that the weak information potentially given on a speciﬁc image 𝑥allows retrieving the unique label 𝑦of the image (e.g., a “pig” could be recognized from its shape and its color). This is a reasonable assumption, if, for a given 𝑥, we ask at random a data labeler to provide us information on shape, color, or texture, etc. However, it will not be the case, if for some reasons (e.g. the dataset is built from several weakly annotated datasets), in some regions of the input space, we only get shape information, and in other regions, we only get color information. In particular, it is not veriﬁed for semi-supervised learning when the support of the unlabeled data distribution is not the same as the support of the labeled input data distribution.

How to relax it and what results to expect? Previous works used Assumption 15 to derive a calibration inequality between the inﬁmum loss to the original loss (e.g., see Proposition 2 by Cabannes et al., 2020b). In contrast, we relate the surrogate and original problem through a reﬁned calibration inequality (8.10). This technical progress allows us to derive exponential convergence rates similarly to the work of Cabannes et al. (2021c). Importantly, in comparison with previous work, our calibration inequality Lemma 57 can easily be extended without the determinism assumption provided by Assumption 15. Essentially, in our work, Assumption 15 is used to simplify the study of ( ˆ𝑦𝑖)𝑖≤𝑛given by the disambiguation algorithm (8.4), and therefore the study of the disambiguation error in (8.10). The study of ( ˆ𝑦𝑖)𝑖≤𝑛without Assumption 15 would require other tools than the one presented in this paper. It could be studied in the realm of graphical model and message passing algorithm, or with Wasserstein distance and topological considerations on measures. With much milder forms of Assumption 15, we expect the rates to degrade smoothly with respect to a parameter deﬁning the hardness of the problem, similarly to the works of Audibert and Tsybakov (2007); Cabannes et al. (2021c).

## 8.5 Optimization considerations

In this section, we focus on implementations to solve (8.4). We explain why disambiguation objectives, such as (8.2) are intrinsically non-convex and express a heuristic strategy to solve (8.4) besides non-convexity in classical well-behaved instances of partial labeling. Note that we do not study implementations to solve (8.5) as this study has already been done by Nowak-Vila et al. (2019). We end this section by considering a practical example to make derivations more concrete.

### 8.5.1 Non-convexity of disambiguation objectives

For readability, suppose that X is a singleton, justifying to remove the dependency on the input in the following. Consider 𝜈∈Δ2Y a distribution modelling weak supervision. While the domain {𝜇∈ΔY | 𝜇⊢𝜈} is convex, a disambiguation objective E : ΔY →R deﬁning 𝜇∗∈arg min𝜇⊢𝜈E(𝜇), similarly to (8.2), that is minimized for deterministic distributions, which correspond to 𝜇a Dirac, i.e., minimized on vertices of its deﬁnition domain ΔY, can not be convex. In other terms, any disambiguation objective that pushes toward distributions where targets are deterministic function of the input, as mentioned in Remark 56, can not be convex.

Indeed, smooth disambiguation objectives such as entropy and our piecewise linear loss-based prin- ciple (8.2), reading pointwise E(𝜇) = inf𝑧∈Y E𝑌∼𝜇[ℓ(𝑧,𝑌)], are concave. Similarly, its quadratic variant E ′(𝜇) = E𝑌,𝑌′∼𝜇[ℓ(𝑌,𝑌′)], is concave as soon as (ℓ(𝑦, 𝑦′))𝑦,𝑦′∈Y is semi-deﬁnite negative. We illustrate those considerations on a concrete example with graphical illustration in Appendix 8.C. We should see how this translates on generic implementations to solve the empirical objective (8.4).

<!-- page: 135 -->

Generic implementation for (8.4)

### 8.5.2

Depending on ℓand on the type of observed set (𝑠𝑖), (8.4) might be easy to solve. In the following, however, we will introduce optimization considerations to solve it in a generic structured prediction fashion. To do so, we recall the decomposition of ℓ(8.7) and rewrite (8.4) as

$$
𝑛 ∑︁
( ˆ𝑦𝑖)𝑖≤𝑛∈arg min inf (𝑧𝑖) ∈Y𝑛 𝛼𝑗(𝑥𝑖)𝜓(𝑧𝑖)⊤𝜑(𝑦𝑗).
𝑦𝑖∈𝐶𝑛 𝑖,𝑗=1
$$

Since, given (𝑦𝑗), the objective is linear in 𝜓(𝑧𝑗), the constraint 𝜓(𝑧𝑗) ∈𝜓(Y) can be relaxed with 𝜁𝑖∈Conv 𝜓(Y).3 Similarly, with respect to 𝜑(𝑦𝑗), this objective is the inﬁmum of linear functions, therefore is concave, and the constraint 𝜑(𝑦𝑗) ∈𝜑(𝑠𝑗), could be relaxed with 𝜉𝑖∈Conv 𝜑(𝑠𝑗). Hence, with H0 = Conv 𝜓(Y) and Γ𝑛= Î 𝑗≤𝑛Conv 𝜑(𝑠𝑗), the optimization is cast as

$$
𝑛 ∑︁
( ˆ𝜉𝑖)𝑖≤𝑛∈arg min inf (𝜁𝑖) ∈H𝑛 𝛼𝑗(𝑥𝑖)𝜁⊤ 𝑖𝜉𝑗. (8.12)
(𝜉𝑖) ∈Γ𝑛 0 𝑖,𝑗=1
$$

(8.12)

Because of concavity, ( ˆ𝜉𝑖) will be an extreme point of Γ𝑛, that could be decoded into ˆ𝑦𝑖= 𝜑−1( ˆ𝜉𝑖). However, it should be noted that if only interested in 𝑓𝑛and not in the disambiguation ( ˆ𝑦𝑖), this decoding can be avoided, since (8.5) can be rewritten as 𝑓𝑛(𝑥) ∈arg min𝑧∈Y 𝜓(𝑧)⊤Í𝑛

$$
𝑖=1 𝛼𝑖(𝑥) ˆ𝜉𝑖.
$$

### 8.5.3 Alternative minimization with good initialization

To solve (8.12), we suggest using an alternative minimization scheme. The output of such a scheme is highly dependent to the variable initialization. In the following, we introduce well-behaved problem, where (𝜉𝑖)𝑖≤𝑛 can be initialized smartly, leading to an eﬃcient implementation to solve (8.12).

Deﬁnition 58 (Well-behaved partial labeling problem). A partial labeling problem (ℓ, 𝜈) is said to be well-behaved if for any 𝑠∈supp 𝜈2Y, there exists a signed measure 𝜇𝑠on Y such that the function from Y to R deﬁned as 𝑧→

$$
∫
$$

Y ℓ(𝑧, 𝑦) d𝜇𝑠(𝑦) is minimized for, and only for, 𝑧∈𝑠.

We provide a real-world example of a well-behaved problem in Section 8.5.4 as well as a synthetic example with graphical illustration in Appendix 8.C. On those problems, we suggest solving (8.12) by considering the initialization 𝜉(0) 𝑖 = E𝑌∼𝜇𝑠𝑖[𝜑(𝑌)], and performing alternative minimization of (8.12), until attaining 𝜉(∞) as the limit of the alternative minimization scheme (which exists since each step decreases the value of the objective in (8.12) and there is a ﬁnite number of candidates for (𝜉𝑖)). It corresponds to a disambiguation guess ˜𝑦𝑖= 𝜑−1(𝜉(∞) 𝑖 ). Then we suggest learning ˆ𝑓𝑛from (𝑥𝑖, ˜𝑦𝑖) based on (8.5), and existing algorithmic tools for this problem (Nowak-Vila et al., 2019). To assert the well-foundedness of this heuristic, we refer to the following proposition, proven in Appendix 8.A.4.

Proposition 59. Under the non-ambiguity hypothesis, Assumption 15, the solution of (8.3) is characterized by 𝑓∗∈arg min 𝑓:X→Y E(𝑋,𝑆)∼𝜈

$$
E𝑌∼𝜇𝑆[ℓ( 𝑓(𝑋),𝑌)]
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

𝑛: X →H deﬁned as 𝑔◦

$$
E𝑌∼𝜇𝑆[ℓ( 𝑓(𝑋),𝑌)]
$$

. Moreover, if the surrogate function 𝑔◦

$$
𝑛(𝑥) = Í𝑛
$$

𝑖=1 𝛼𝑖(𝑥)𝜉𝑠𝑖, with 𝜉𝑠= E𝑌∼𝜇𝑠[𝜑(𝑌)], converges toward 𝑔◦(𝑥) = E𝑆∼𝜈|𝑥[𝜉𝑆] in 𝐿1, 𝑓◦ 𝑛 deﬁned through the decoding (8.9) converges in risk toward 𝑓∗.

Given that our algorithm scheme is initialized for 𝜉(0)

$$
𝑖 \frac{= 𝜉𝑠𝑖and 𝜁(0)}{𝑖}
$$

𝑛(𝑥𝑖) and stopped once having attained 𝜉(∞)

$$
𝑖 = 𝑓◦
$$

𝑖 = ˆ𝑓𝑛(𝑥𝑖), ˆ𝑓𝑛is arguably better than 𝑓◦

$$
𝑖 \frac{and 𝜁(∞)}{𝑖}
$$

𝑛, which given consistency result exposed in Proposition 59, is already good enough.

Remark 60 (IQP implementation for (8.4)). Other heuristics to solve (8.4) are conceivable. For example, considering 𝑧𝑖= 𝑦𝑖in this equation, we remark that the resulting problem is isomorphic to an integer quadratic program (IQP). Similarly to integer linear programming, this problem can be approached with relaxation of the “integer constraint” to get a real-valued solution, before “thresholding” it to recover an integer solution. This heuristic can be seen as a generalization of the Diﬀrac algorithm (Bach and Harchaoui, 2007; Joulin et al., 2010). We present it in details in Appendix 8.B.

3The minimization pushes toward extreme points of the deﬁnition domain.

<!-- page: 136 -->

Remark 61 (Link with EM, (Dempster et al., 1977)). Arguably, our alternative minimization scheme, optimizing respectively the targets 𝜉𝑖= 𝜑(𝑦𝑖) and the function estimates 𝜁𝑖= 𝜓( 𝑓𝑛(𝑥𝑖)) can be seen as the non-parametric version of the Expectation-Maximization algorithm, popular for parametric model (Dempster et al., 1977).

### 8.5.4 Application: ranking with partial ordering

Ranking is a problem consisting, for an input 𝑥in an input space X, to learn a total ordering 𝑦, belonging to Y = S𝑚, modelling preference over 𝑚items. It is usually approached with the Kendall loss ℓ(𝑦, 𝑧) = −𝜑(𝑦)⊤𝜑(𝑧), with 𝜑(𝑦) = (sign (𝑦(𝑖) −𝑦( 𝑗)))𝑖,𝑗≤𝑚∈{−1, 1}𝑚2 (Kendall, 1938). Full supervision corresponds, for a given 𝑥, to be given a total ordering of the 𝑚items. This is usually not an option, but one could expect to be given partial ordering that 𝑦should follow (Cao et al., 2007; Hüllermeier et al., 2008; Korba et al., 2018). Formally, this equates to the observation of some, but not all, coordinates 𝜑(𝑦)𝑖of the vector 𝜑(𝑦) for some 𝑖∈𝐼⊂⟦1, 𝑚⟧2.

In this setting, 𝑠⊂Y is a set of total orderings that match the given partial ordering. It can be represented by a vector 𝜉𝑠∈H, that satisﬁes the partial ordering observation, (𝜉𝑠)𝐼= 𝜑(𝑦)𝐼, and that is agnostic on unobserved coordinates, (𝜉𝑠)𝑐𝐼= 0. This vector satisﬁes that 𝑧→𝜓(𝑧)⊤𝜉𝑠is minimized for, and only for, 𝑧∈𝑠. Hence, it constitutes a good initialization for the alternative minimization scheme detailed above. We provide details in Appendix 8.A.5, where we also show that 𝜉𝑠can be formally translated in a 𝜇𝑠to match the Deﬁnition 58, proving that ranking with partial labeling is a well-behaved problem.

Many real world problems can be formalized as a ranking problem with partial ordering observations. For example, 𝑥could be a social network user, and the 𝑚items could be posts of her connection that the network would like to order on her feed accordingly to her preferences. One might be told that the user 𝑥prefer posts from her close rather than from her distant connections, which translates formally as the constraint that for any 𝑖corresponding to a post of a close connection and 𝑗corresponding to a post of a distant connection, we have 𝜑(𝑦)𝑖𝑗= 1. Nonetheless, designing non-parametric structured prediction models that scale well when the intrinsic dimension 𝑚of the space Y is very large (such as the number of post on a social network) remains an open problem, that this paper does not tackle.

## 8.6 Related work

Weakly supervised learning has been approached through parametric and non-parametric methods. Para- metric models are usually optimized through maximum likelihood (Heitjan and Rubin, 1991; Jin and Ghahramani, 2002). Hüllermeier (2014) show that this approach, as formalized by Denoeux (2013), equates to disambiguating sets by averaging candidates, which was shown inconsistent by Cabannes et al. (2020b) when data are not missing at random. Among non-parametric models, Xu et al. (2004); Bach and Harchaoui (2007) developed an algorithm for clustering, that has been cast for weakly supervised learning problem (Joulin et al., 2010; Alayrac et al., 2016), leading to a disambiguation algorithm similar than ours, yet without consistency results. More recently, half-way between theory and practice, Gong et al. (2018) derived an algorithm geared toward classiﬁcation, based on a disambiguation objective, incorporating several heuristics, such as class separation, and Laplacian diﬀusion. Those heuristics could be incorporated formally in our model.

The inﬁmum loss principle has been considered by several authors, among them Cour et al. (2011); Luo and Orabona (2010); Hüllermeier (2014). It was recently analyzed through the prism of structured prediction by Cabannes et al. (2020b), leading to a consistent non-parametric algorithm that will constitute the baseline of our experimental comparison. This principle is interesting as it does not assume knowledge on the corruption process (𝑆|𝑌) contrarily to the work of Cid-Sueiro et al. (2014) or van Rooyen and Williamson (2017).

The non-ambiguity assumption has been introduced by Cour et al. (2011) and is a classical assumption of learning with partial labeling (Liu and Dietterich, 2014). Assumptions of Lipschitzness and minimal mass are classical assumptions to prove convergence of local averaging method (Audibert and Tsybakov, 2007; Biau and Devroye, 2015). Those assumptions imply class separation in X, which has been leverage in semi-supervised learning, justifying Laplacian regularization (Rigollet, 2007; Zhu et al., 2003).

Note that those assumptions might not hold on raw representation of the data, but with appropriate metrics, which could be learned through unsupervised Duda et al. (2000) or self-supervised learning Doersch

<!-- page: 137 -->

Problem setting Reconstruction y y Signal Samples DF IL x x

[FIGURE: Figure 8.1]

Figure 8.1: Interval regression. See Appendix 8.D for the exact reproducible experimental setup (Left) Setup. The goal is to learn 𝑓∗: X →R represented by the dashed line, given samples (𝑥𝑖, 𝑠𝑖), where (𝑠𝑖) are intervals represented by the blue segments. (Right) We compare the inﬁmum loss (IL) baseline (8.13) shown in green, with our disambiguation framework (DF), (8.4) and (8.5), shown in orange; with weights 𝛼given by kernel ridge regression. (DF) retrieves ˆ𝑦𝑖before learning a smooth 𝑓𝑛based on (𝑥𝑖, ˆ𝑦𝑖), while (IL) implicitly retrieves ˆ𝑦𝑖(𝑥) diﬀerently for each input, leading to irregularity of the consequent estimator of 𝑓∗. and Zisserman (2017). As such, the practitioner might consider weights 𝛼given by similarity metrics derived through such techniques, before computing the disambiguation (8.4) and learning 𝑓𝑛from the recollected fully supervised dataset with deep learning.

## 8.7 Experiments

In this section, we review a baseline, and experiments that showcase the usefulness of our algorithm – which corresponds to (8.4) and (8.5).

Baseline. We consider as a baseline the work of Cabannes et al. (2020b), which is a consistent structured prediction approach to partial labeling through the inﬁmum loss. It is arguably the state-of-the-art of partial labeling approached through structured prediction. It follows the same loss-based variance disambiguation principle, yet in an implicit fashion, leading to the inference algorithm, 𝑓𝑛: X →Y,

$$
𝑛 ∑︁
𝑓𝑛(𝑥) ∈arg min inf (𝑦𝑖) ∈𝐶𝑛 𝛼𝑖(𝑥)ℓ(𝑧, 𝑦𝑖). (8.13)
𝑧∈Y 𝑖=1
$$

(8.13)

Statistically, exponential convergence rates similar to Theorem 15 could be derived. Yet, as we will see, our algorithm outperforms this state-of-the-art baseline.

Disambiguation coherence - Interval regression. The baseline (8.13) implicitly requires disambiguating ( ˆ𝑦𝑖(𝑥)) diﬀerently for every 𝑥∈X. This is counterintuitive since (𝑦∗ 𝑖) does not depend on 𝑥. It means that ( ˆ𝑦𝑖) could be equal to some ( ˆ𝑦(0) 𝑖 ) on a subset X0 of X, and to another ( ˆ𝑦(1) 𝑖 ) on a disjoint subset X1 ⊂X, leading to irregularity of 𝑓𝑛between X0 and X1. We illustrate this graphically on Figure 8.1. This ﬁgure showcases an interval regression problem, which corresponds to the regression setup (Y = R, ℓ(𝑦, 𝑧) = |𝑦−𝑧|2) of partial labeling, where one does not observe 𝑦∈R but an interval 𝑠⊂R containing 𝑦. Among others this problem appears in physics (Sheppard, 1897) and economy (Tobin, 1958).

Computation attractiveness - Ranking. Computationally, the baseline requires to solve a disambiguation problem, recovering ( ˆ𝑦𝑖(𝑥)) ∈𝐶𝑛for every 𝑥∈X for which we want to infer 𝑓𝑛(𝑥). This is much more costly, than doing the disambiguation of ( ˆ𝑦𝑖) ∈𝐶𝑛once, and solving the supervised learning inference problem (8.5), for every 𝑥∈X for which we want to infer 𝑓𝑛(𝑥). To illustrate the computation attractiveness of our algorithm, consider the case of ranking, deﬁned in Section 8.5.4. Fully supervised inference scheme (8.5) corresponds to solving a NP-hard problem, equivalent to the minimum feedback arcset problem (Duchi et al., 2010). While disambiguation approaches with alternative minimization implied by (8.4) and (8.13) require to solve this NP-hard problem for each minimization step. In other terms, the baseline ask to solve multiple NP-hard problem every time one wants to infer 𝑓𝑛given by (8.13) on an input 𝑥∈X. Meanwhile, our disambiguation

<!-- page: 138 -->

“Dna” dataset “Svmguide2” dataset DF IL AC DF IL AC Loss Loss 0 10 20 30 40 50 60 70 80 Corruption (in %) 0 10 20 30 40 50 60 70 80 Corruption (in %)

[FIGURE: Figure 8.2]

Figure 8.2: Testing errors as function of the supervision corruption on real dataset corresponding to classiﬁcation with partial labels. We split fully supervised LIBSVM datasets into training and testing dataset. We corrupt training data in order to get partial labels. Corruption is managed through a parameter, represented by the 𝑥-axis, that relates to the ambiguity degree 𝜂of Assumption 15. For each method (our algorithm (DF), the baseline (IL), and the baseline of the baseline (AC, consisting of averaging candidates 𝑦𝑖in sets 𝑆𝑖)), we consider weights 𝛼given by kernel ridge regression with Gaussian kernel, for which we optimized hyperparameters with cross-validation on the training set. We then learn an estimate 𝑓𝑛that we evaluate on the testing set, represented by the 𝑦-axis, on which we have full supervision. The ﬁgure shows the superiority of our method, that achieves error similar to baseline when full supervision (𝑥= 0) or no supervision (𝑥= 100%) is given, but performs better when only in presence of partial supervision. See Appendix 8.D for reproducibility speciﬁcations, where we also provide Figure 8.6 showcasing similar empirical results in the case of ranking with partial ordering. approach asks to solve multiple NP-hard problem upfront to solve (8.4), yet only require to solve one NP-hard problem to infer 𝑓𝑛given by (8.5) on an input 𝑥∈X.

Better empirical results - Classiﬁcation. Finally, we compare our algorithm, our baseline (8.13) and the baseline considered by Cabannes et al. (2020b) on real datasets from the LIBSVM dataset (Chang and Lin, 2011). Those datasets (𝑥𝑖, 𝑦𝑖) correspond to fully supervised classiﬁcation problem. In this setup, Y = ⟦1, 𝑚⟧for 𝑚a number of classes, and ℓ(𝑦, 𝑧) = 1𝑦≠𝑧. We “corrupt” labels in order to create a synthetic weak supervision datasets (𝑥𝑖, 𝑠𝑖). We consider skewed corruption, in the sense that (𝑠𝑖) is generated by a probability such that Í 𝑧∈Y P𝑆𝑖(𝑧∈𝑆𝑖|𝑦𝑖) depends on the value of 𝑦𝑖. This corruption is parametrized by a parameter that related with the ambiguity parameter 𝜂of Assumption 15. Results on Figure 8.2 show that, in addition to having a lower computation cost, our algorithm performs better in practice than the state-of-the-art baseline.4 Beyond (8.2) - Semi-supervised learning. The main limitation of (8.2) is that it is a pointwise principle that decorrelates inputs, in the sense that the optimization of 𝜇∗|𝑥, for 𝑥∈X, only depends on 𝜈|𝑥and not on what is happening on X \ {𝑥}. As such, this principle failed to tackle semi-supervised learning, where 𝜈|𝑥is equal to 𝜇|𝑥(in the sense that 𝜋|𝑥,𝑦= 𝛿{𝑦}) for 𝑥∈X𝑙and is equal to 𝛿Y for 𝑥∈X𝑢:= X \ X𝑙. In such a setting, for 𝑥∈X𝑢, 𝜇∗|𝑥can be set to any 𝛿𝑦for 𝑦∈Y. Interestingly, in practice, while the baseline suﬀer the same limitation, for our algorithm, weighting schemes have a regularization eﬀect, that contrasts with those considerations. We illustrate it on Figure 8.3.

## 8.8 Conclusion

In this work, we have introduced a structured prediction algorithm (8.4) and (8.5), to tackle partial labeling. We have derived exponential convergence rates for the nearest neighbors instance of this algorithm under classical learnability assumptions. We provided optimization considerations to implement this algorithm in practice, and have successfully compared it with the state-of-the-art. Several open problems oﬀer prospective follow-up of this works:

• Semi-supervised learning and beyond. While we only proved convergence in situation where 𝜇∗ of (8.2) is uniquely deﬁned, therefore excluding semi-supervised learning, Figure 8.3 suggests that our algorithm (8.4) could be analyzed in a broader setting than the one considered in this paper. Among 4All the code is available online - https://github.com/VivienCabannes/partial_labelling/.

<!-- page: 139 -->

Semi-supervision setting DF reconstruction IL reconstruction

[FIGURE: Figure 8.3]

Figure 8.3: Semi-supervised learning, “concentric circle” instance with four classes (red, green, blue, yellow). Reproducibility details provided in Appendix 8.D. (Left) We represent points 𝑥𝑖∈X ⊂R2, there is many unlabeled points (represented by black dots and corresponding to 𝑆𝑖= Y), and one labeled point for each class (represented in color, corresponding to 𝑆𝑖= {𝑦𝑖}). (Middle) Reconstruction 𝑓𝑛: X →Y given by our algorithm (8.4) and (8.5). Our algorithm succeeds to comprehend the concentric circle structure of the input distribution and clusters classes accordingly. (Right) Reconstruction 𝑓𝑛: X →Y given by the baseline (8.13). The baseline performs as if only the four supervised data points where given. others, we conjecture that the non-ambiguity assumption could be replaced by a cluster assumption (Rigollet, 2007) together with a non-ambiguity assumption cluster-wise in Theorem 15. • Hard-coded weak supervision. Variational principles (8.2) and (8.3) could be extended beyond partial labeling to any type of hard-coded weak supervision, which is when weak supervision can be cast as a set of hard constraint that 𝜇should satisfy, formally written as a set of fully supervised distributions compatible with weak information. Hard-coded weak supervision includes label proportion (Quadrianto et al., 2009; Dulac-Arnold et al., 2019), but excludes supervision of the type “80% of the experts say this nose is broken, and 20% say it is not”. Providing a unifying framework for those problems would make an important step in the theoretical foundation of weakly supervised learning. • Missing input data. While weak supervision assumes that only 𝑦is partially known, in many applications of machine learning, 𝑥is also only partially known, especially when the feature vector 𝑥is built from various source of information, leading to missing data. While we only considered a principle to ﬁll missing output information, similar principles could be formalized to ﬁll missing input information.

<!-- page: 140 -->

<!-- page: 141 -->

# Appendix

## 8.A Proofs

Mathematical assumptions. To make formal what should be seen as implicit assumptions heretofore, we consider X and Y Polish spaces, Y compact, ℓ: Y × Y →R continuous, H a separable Hilbert space, 𝜑 measurable, and 𝜓continuous. We also assume that for 𝜈𝑥-almost every 𝑥∈X, and any 𝜇⊢𝜈, that the pushforward measure 𝜑∗𝜇|𝑥has a second moment. This is the suﬃcient setup in order to be able to formally deﬁne objects and solutions considered all along the paper.

Notations. Beside standard notations, we use |Y| to design the cardinality of Y, and 2Y to design the set of subsets of Y. Regarding measures, we use 𝜇X and 𝜇|𝑥respectively the marginal over X and the conditional accordingly to 𝑥of 𝜇∈ΔX×Y. We denote by 𝜇⊗𝑛the distribution of the random variable (𝑍1, · · · , 𝑍𝑛), where the 𝑍𝑖are sampled independently according to 𝜇. For 𝐴a Polish space, we consider Δ𝐴the set of Borel probability measures on this space. For 𝜑: Y →H and 𝑆⊂Y, we denote by 𝜑(𝑆) the set {𝜑(𝑦) | 𝑦∈𝑆}. For a family of sets (𝑆𝑖), we denote by Î 𝑆𝑖the Cartesian product 𝑆1 × 𝑆2 × · · · , also deﬁned as the set of points (𝑦𝑖) such that 𝑦𝑖∈𝑆𝑖for all index 𝑖, and by Y𝑛the Cartesian product Î 𝑖≤𝑛Y. Finally, for 𝐸a subset of a vector space 𝐸′, Conv 𝐸denotes the convex hull of 𝐸and Span(𝐸) its span.

$$
∫
$$

Abuse of notations. For readability’ sake, we have abused notations. For a signed measure 𝜇, we denote by E𝜇[𝑋] the integral 𝑥d𝜇(𝑥), extending this notation usually reserved to probability measure. More importantly, when considering 2Y, we should actually restrict ourselves to the subspace S ⊂2Y of closed subsets of Y, as S is a Polish space (metrizable by the Hausdorﬀdistance) while 2Y is not always. However, when Y is ﬁnite, those two spaces are equals, 2Y = S.

### 8.A.1 Proof of Lemma 57

From Lemma 3 in Cabannes et al. (2021c), we pull the calibration inequality

$$
1∥𝑔𝑛(𝑋)−𝑔∗(𝑋) ∥>𝑑(𝑔∗(𝑋),𝐹) ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥ 
R( 𝑓𝑛) −R( 𝑓∗) ≤2𝑐𝜓E .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Where 𝐹is deﬁned as the set of points 𝜉∈Conv 𝜑(Y) leading to two decodings

$$
arg min > 1 
𝐹= 𝜉∈Conv 𝜑(Y) ⟨𝜓(𝑧), 𝜉⟩ ,
𝑧∈Y
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

and 𝑑is deﬁned as the extension of the norm distance to sets, for 𝜉∈H

$$
𝑑(𝜉, 𝐹) = inf 𝜉′∈𝐹∥𝜉−𝜉′∥H .
𝑔𝑛(𝑋) −𝑔∗ + 𝑔∗ and that, if 𝑎≤𝑏+ 𝑐,
$$

Using that ∥𝑔𝑛(𝑋) −𝑔∗(𝑋)∥≤

$$
𝑛(𝑋) 𝑛(𝑋) −𝑔∗(𝑋)
1𝑎>𝛿𝑎≤1𝑏+𝑐>𝛿𝑏+ 𝑐≤12 sup(𝑏,𝑐)>𝛿2 sup 𝑏, 𝑐= 2 sup 𝑒∈𝑏,𝑐 1𝑒>𝛿𝑒≤21𝑏>𝛿𝑏+ 21𝑐>𝛿𝑐.
$$

We get the reﬁned inequality R( 𝑓𝑛) −R(𝑔∗)

$$
12∥𝑔𝑛(𝑋)−𝑔∗𝑛(𝑋) ∥>𝑑(𝑔∗(𝑋),𝐹) 𝑔𝑛(𝑋) −𝑔∗ + 12∥𝑔∗𝑛(𝑋)−𝑔∗(𝑋) ∥>𝑑(𝑔∗(𝑋),𝐹) 𝑔∗ 
≤4𝑐𝜓E 𝑛(𝑋) 𝑛(𝑋) −𝑔∗(𝑋) .
139
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 142 -->

The ﬁrst term is bounded by

$$
12∥𝑔𝑛(𝑋)−𝑔∗𝑛(𝑋) ∥>𝑑(𝑔∗(𝑋),𝐹) 𝑔𝑛(𝑋) −𝑔∗ 𝑔𝑛−𝑔∗
E 𝑛(𝑋) ≤ 𝐿1 .
𝑛
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

While for the second term, we proceed with

$$
12∥𝑔∗𝑛(𝑋)−𝑔∗(𝑋) ∥>𝑑(𝑔∗(𝑋),𝐹) 𝑔∗ 
E 𝑛(𝑋) −𝑔∗(𝑋) 
𝑔∗ 𝑛−𝑔∗ 2 𝑔∗ > inf 𝑥∈supp 𝜈X 𝑑(𝑔∗(𝑋), 𝐹)
≤ 𝐿∞P𝑋 𝑛(𝑋) −𝑔∗(𝑋) .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

When weights are positive and sum to one, both 𝑔∗ 𝑛(𝑋) and 𝑔∗(𝑋) are averaging of 𝜑(𝑦) for 𝑦∈Y, therefore 𝑔∗

$$
𝑛−𝑔∗ 𝐿∞≤2𝑐𝜑.
$$

The same is true when Í 𝑖≤𝑛|𝛼𝑖(𝑥)| ≤1. Finally, when the labels are a deterministic function of the input, 𝑔∗(𝑋) = 𝜑( 𝑓∗(𝑋)), and 𝑑(𝑔∗(𝑋), 𝐹) ≤sup𝑦∈Y 𝑑(𝜑(𝑦), 𝐹). Deﬁning 𝛿:= sup𝑦∈Y 𝑑(𝜑(𝑦), 𝐹)/2, and adding everything together leads to Lemma 57.

### 8.A.2 Implication of Assumptions 15 and 16

Assume that Assumption 15 holds, consider 𝑥∈supp 𝜈X , let us show that 𝑓∗(𝑥) = 𝑦𝑥and 𝜇∗|𝑥= 𝛿𝑦𝑥. First of all, notice that Ñ 𝑆;𝑆∈supp 𝜈|𝑥= {𝑦𝑥}; that 𝛿𝑦𝑥⊢𝜈|𝑥, as it corresponds to 𝜋|𝑥,𝑆= 𝛿𝑦𝑥∈Δ𝑆, for all 𝑆in the support of 𝜈|𝑥; and that, because ℓis well-behaved,

$$
\frac{𝑧∈Y ℓ(𝑧, 𝑦𝑥) = ℓ(𝑦𝑥, 𝑦𝑥) = 0.}{inf}
$$

This inﬁmum is only achieved for 𝑧= 𝑦𝑥, hence if we prove that 𝜇∗|𝑥= 𝛿𝑦𝑥, we directly have that 𝑓∗(𝑥) = 𝑦𝑥. Finally, suppose that 𝜇|𝑥⊢𝜈|𝑥charges 𝑦≠𝑦𝑥. Because 𝑦does not belong to all sets charged by 𝜈|𝑥, 𝜇|𝑥 should charge another 𝑦′ ∈Y, and therefore

$$
inf 𝑧∈Y E𝑌∼𝜇|𝑥[ℓ(𝑧, 𝑦)] ≥inf 𝑧∈Y 𝜇|𝑥(𝑦)ℓ(𝑧, 𝑦) + 𝜇|𝑥(𝑦′)ℓ(𝑧, 𝑦′) > 0.
$$

Which shows that 𝜇∗|𝑥= 𝛿𝑦𝑥. We deduce that 𝑔∗(𝑥) = 𝑦𝑥.

Now suppose that Assumption 16 holds too, and consider two 𝑥, 𝑥′ ∈supp 𝜈X belonging to two diﬀerent classes 𝑓(𝑥) = 𝑦and 𝑓(𝑥′) = 𝑦′. We have that 𝑔∗(𝑥) = 𝜑(𝑦) and 𝑔∗(𝑥′) = 𝜑(𝑦′), therefore,

$$
𝑑(𝑥, 𝑥′) ≥𝑐−1 ∥𝜑(𝑦) −𝜑(𝑦′)∥H .
$$

Deﬁne ℎ2 = inf𝑦≠𝑦′ 𝑐−1 ∥𝜑(𝑦) −𝜑(𝑦′)∥H. Let us now show that ℎ2 > 0. When Y is ﬁnite, this inﬁmum is a minimum, therefore, ℎ2 = 0, only if there exists a 𝑦≠𝑦′, such that 𝜑(𝑦) = 𝜑(𝑦′), which would implies that ℓ(·, 𝑦) = ℓ(·, 𝑦′) and therefore ℓ(𝑦, 𝑦′) = ℓ(𝑦, 𝑦) which is impossible when ℓis proper.

### 8.A.3 Proof of Theorem 15

Reusing Lemma 57, we have

$$
𝑔∗ 1∥𝑔∗𝑛(𝑋)−𝑔∗(𝑋) ∥>𝛿 
E( 𝑓𝑛) ≤4𝑐𝜓ED𝑛,𝑋 𝑛(𝑋) −𝑔𝑛(𝑋) + 8𝑐𝜓𝑐𝜑ED𝑛,𝑋 .
H
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We will ﬁrst prove that

$$
ED𝑛 1∥𝑔∗𝑛(𝑋)−𝑔∗(𝑋) ∥>𝛿 ≤exp \frac{−𝑛𝑝}{8}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

as long as 𝑘< 𝑛𝑝/2. The error between 𝑔∗and 𝑔𝑛relates to classical supervised learning of 𝑔∗from samples (𝑋𝑖,𝑌𝑖) ∼𝜇∗. We invite the reader who would like more insights on this fully supervised part of the proof to refer to the several monographs written on local averaging methods and, in particular, nearest neighbors, such as Biau and Devroye (2015). Because of class separation, we know that if 𝑘points fall at distance at most ℎof 𝑥∈supp 𝜈X , 𝑔∗

$$
𝑛(𝑥) = 𝑘−1 Í
$$

𝑖;𝑋𝑖∈N (𝑥) 𝜑(𝑦𝑖) = 𝜑(𝑦𝑥) = 𝑔∗(𝑥), where N (𝑥) designs the 𝑘-nearest neighbors of 𝑥in (𝑋𝑖). Because the probability of falling at distance ℎof 𝑥for each 𝑋𝑖is lower bounded by 𝑝, we have that

$$
PD𝑛(𝑔∗ 𝑛(𝑥) ≠𝑔∗(𝑥)) ≤P(Bernoulli(𝑛, 𝑝) < 𝑘).
$$

<!-- page: 143 -->

8.A. PROOFS 141 This can be upper bound by exp(−𝑛𝑝/8) as soon as 𝑘< 𝑛𝑝/2, based on Chernoﬀmultiplicative bound (see Biau and Devroye, 2015, for a reference), meaning

$$
ED𝑛,𝑋 𝑔𝑛−𝑔∗ 𝑛 1∥𝑔∗𝑛(𝑋)−𝑔∗(𝑋) ∥≥𝛿 ≤exp(−𝑛𝑝/8).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

For the disambiguation part in 𝐿1, we distinguish two types of datasets, the ones where for any input 𝑋𝑖its 𝑘-neighbors at are distance at least ℎ, ensuring that disambiguation can be done by clusters, and datasets that does not verify this property. Consider the event

$$
D = \frac{𝑛}{(𝑋𝑖)𝑖≤𝑛} sup_{𝑖} 𝑑(𝑋𝑖, 𝑋(𝑘) (𝑋𝑖)) < ℎ
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑋(𝑘) (𝑥) design the 𝑘-th nearest neighbor of 𝑥in (𝑋𝑖)𝑖≤𝑛. We proceed with

$$
𝑔∗ 𝑔∗ 

𝑔∗ (𝑋𝑖) ∈D 
≤sup ∞PD𝑛((𝑋𝑖) ∉D) + ED𝑛,𝑋
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

ED𝑛,𝑋

$$
𝑛(𝑋) −𝑔𝑛(𝑋) 𝑛−𝑔𝑛 𝑛(𝑋) −𝑔𝑛(𝑋) ,
H H
𝑋∈X
$$

Which is based on 𝐸[𝑍] = P(𝑍∈𝐴) E[𝑍|𝐴] + P(𝑍∉𝐴) E[𝑍|𝑐𝐴]. For the term corresponding to bad datasets, we can bound the disambiguation error with the maximum error. Similarly to the derivation for Lemma 57, because 𝑔∗

$$
𝑛(𝑥) and 𝑔∗
$$

𝑛(𝑋), are averaging of 𝜑(𝑦), we have that

$$
sup_{𝑥∈supp 𝜈X} 𝑔𝑛(𝑥) −𝑔∗ 𝑛(𝑥) ≤2𝑐𝜑.
$$

Indeed, we allow ourselves to pay the worst error on those datasets as their probability is really small, which can be proved based on the following derivation.

$$
∪𝑖≤𝑛 
PD𝑛((𝑋𝑖)𝑖≤𝑛∉D) = P(𝑋𝑖) (sup 𝑑(𝑋𝑖, 𝑋(𝑘) (𝑋𝑖)) ≥ℎ) = P(𝑋𝑖) 𝑑(𝑋𝑖, 𝑋(𝑘) (𝑋𝑖)) ≥ℎ
𝑛 ∑︁ 𝑖
 𝑑(𝑋𝑖, 𝑋(𝑘) (𝑋𝑖)) ≥ℎ = 𝑛P𝑋,D𝑛−1 𝑑(𝑋, 𝑋(𝑘) (𝑋)) ≥ℎ .
≤ P(𝑋𝑖)
𝑖=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This last probability has already been work out when dealing with the fully supervised part, and was bounded as

$$
𝑑(𝑋, 𝑋(𝑘) (𝑋)) ≥ℎ ≤exp (−(𝑛−1)𝑝/8) .
P𝑋,D𝑛−1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

as long as 𝑘< (𝑛−1)𝑝/2. Finally, we have

$$
𝑔∗
sup 𝑋∈X 𝑛−𝑔𝑛 ∞PD𝑛((𝑋𝑖)𝑖≤𝑛∉D) ≤2𝑐𝜑𝑛exp (−(𝑛−1)𝑝/8) .
$$

For the expectation term, corresponding to datasets D𝑛∈D that cluster data accordingly to classes, we have to make sure that ˆ𝑦𝑖= 𝑦∗ 𝑖is the only acceptable solution of (8.4), which is true as soon as the intersection of 𝑆𝑗, for 𝑥𝑗the neighbors of 𝑥𝑖, only contained 𝑦∗ 𝑖. To work out the disambiguation algorithm, notice that

$$
∫ d𝜈X (𝑥) ≤ ∫
𝑔𝑛−𝑔∗ 𝑛 ∑︁ 𝑛 ∑︁ 1𝑋𝑖∈N (𝑥) 𝜑( ˆ𝑦𝑖) −𝜑(𝑦∗ d𝜈X (𝑥)
𝐿1 = 𝛼𝑖(𝑥)𝜑( ˆ𝑦𝑖) −𝜑(𝑦∗ 𝑖) 𝑘−1 𝑖)
𝑛
X 𝑖=1 X 𝑖=1
𝑛 ∑︁ 𝜑( ˆ𝑦𝑖) −𝜑(𝑦∗ ≤2𝑐𝜑𝑘−1 𝑛 ∑︁
= 𝑘−1 P𝑋(𝑋𝑖∈N (𝑋)) 𝑖) P𝑋(𝑋𝑖∈N (𝑋)) 1𝜑( ˆ𝑦𝑖)≠𝜑(𝑦∗ 𝑖).
𝑖=1 𝑖=1
$$

Finally we have, after proper conditioning, considering the variability in 𝑆𝑖while ﬁxing 𝑋𝑖ﬁrst,

$$
𝑔∗ (𝑋𝑖) ∈D 
ED𝑛,𝑋 𝑛(𝑋) −𝑔𝑛(𝑋) " 𝑛 ∑︁ i (𝑋𝑖) ∈D #
H h (𝑋𝑖)
= 2𝑐𝜑𝑘−1 E(𝑋𝑖)
P𝑋(𝑋𝑖∈N (𝑋)) E(𝑆𝑖) 1𝜑( ˆ𝑦𝑖)≠𝜑(𝑦∗ 𝑖)
𝑖=1 " 𝑛 ∑︁ (𝑋𝑖) ∈D #
1𝑋𝑖∈N (𝑋) P(𝑆𝑖) 𝜑( ˆ𝑦𝑖) ≠𝜑(𝑦∗ (𝑋𝑖) 
= 2𝑐𝜑𝑘−1 E(𝑋𝑖),𝑋
𝑖) .
𝑖=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 144 -->

We design D so that the 𝑘-th nearest neighbor of any input 𝑋𝑖is at distance at most ℎof 𝑋𝑖, meaning the because of class separation, 𝑦𝑥𝑖∈𝑆𝑗for any 𝑋𝑗∈N (𝑋𝑖). This mean that outputting ( ˆ𝑦𝑖) = (𝑦∗ 𝑖) and 𝑧𝑗= 𝑦𝑗, will lead to an optimal error in (8.4). Now suppose that there is another solution for (8.4) such that ˆ𝑦𝑖≠𝑦∗ 𝑖, it should also achieve an optimal error, therefore it should verify 𝑧𝑗= ˆ𝑦𝑗for all 𝑗as well as ˆ𝑦𝑗= ˆ𝑦𝑖for all 𝑗 such that 𝑋𝑗is one of the 𝑘nearest neighbors of 𝑋𝑖. This implies that ˆ𝑦𝑖∈∩𝑗;𝑋𝑗∈N (𝑋𝑖)𝑆𝑗, which happen with probability

$$
P(𝑆𝑗) 𝑗;𝑋𝑗∈N (𝑋𝑖) (∃𝑧≠𝑦𝑖, 𝑧∈∩𝑗𝑆𝑗) ≤𝑚P𝑆𝑗(𝑧∈𝑆𝑗)𝑘≤𝑚𝜂𝑘= 𝑚exp(−𝑘|log(𝜂)|).
$$

With 𝑚= |Y| the number of elements in Y. We deduce that

$$
𝜑( ˆ𝑦𝑖) ≠𝜑(𝑦∗ (𝑋𝑖) ≤𝑚exp(−𝑘|log(𝜂)|).
P(𝑆𝑖) 𝑖)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

And because Í𝑛

$$
𝑖=1 1𝑋𝑖∈N (𝑋) = 𝑘, we conclude that
 

𝑔∗ (𝑋𝑖) ∈D 
ED𝑛,𝑋 𝑛(𝑋) −𝑔𝑛(𝑋) ≤2𝑐𝜑𝑚exp(−𝑘|log(𝜂)|).
H
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Finally, adding everything together we get

$$
−𝑛𝑝 −(𝑛−1)𝑝
E( 𝑓𝑛) ≤8𝑐𝜑𝑐𝜓exp + 8𝑐𝜑𝑐𝜓𝑛exp + 8𝑐𝜑𝑐𝜓𝑚exp (−𝑘|log(𝜂)|) .
8 8
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

as long as 𝑘< (𝑛−1)𝑝/2, which implies Theorem 15 as long as 𝑛≥2.

Remark 62 (Other approaches). While we have proceeded with analysis based on local averaging methods, other paths could be explored to prove convergence results of the algorithm provided (8.4) and (8.5). For example, one could prove Wasserstein convergence of Í𝑛

$$
𝑖=1 𝛿(𝑥𝑖,ˆ𝑦𝑖) toward Í𝑛 𝑖=1 𝛿(𝑥𝑖,ˆ𝑦∗
$$

𝑖), together with some continuity of the learning algorithm as a function of those distributions.5 This analysis could be understood as tripartite:

• A disambiguation error, comparing ˆ𝑦𝑖to 𝑦∗ 𝑖. • A stability / robustness measure of the algorithm to learn 𝑓𝑛from data when substituting 𝑦∗ 𝑖by ˆ𝑦𝑖. • A consistency result regarding 𝑓∗ 𝑛learned with (𝑥𝑖, 𝑦∗ 𝑖). Our analysis followed a similar path, yet with the ﬁrst two parts tackled jointly.

### 8.A.4 Proof of Proposition 59

Under the non-ambiguity hypothesis (Assumption 15), the solution of (8.3) is characterized pointwise by 𝑓∗(𝑥) = 𝑦𝑥for all 𝑥∈supp 𝜈X . Similarly, under Assumption 15, we have the characterization 𝑓∗(𝑥) ∈∩𝑆∈supp 𝜈|𝑥𝑆. With the notation of Deﬁnition 58, since 𝑓∗(𝑥) minimizes 𝑧→E𝑌∼𝜇𝑆[ℓ(𝑧,𝑌)] for all 𝑆∈supp 𝜈|𝑥, it also minimizes 𝑧→E𝑆∼𝜈|𝑥E𝑌∼𝜇𝑆[ℓ(𝑧,𝑌)].

For the second part of the proposition, we use the structured prediction framework of Ciliberto et al. (2020). Deﬁne the signed measure 𝜇◦deﬁned as 𝜇◦ X := 𝜈X and 𝜇◦|𝑥:= E𝑆∼𝜈|𝑥E𝑌∼𝜇𝑆[𝛿𝑌], and 𝑓◦: X →Y the solution 𝑓◦∈arg min 𝑓:X→Y E(𝑋,𝑌)∼𝜇◦[ℓ( 𝑓(𝑋),𝑌)] = arg min 𝑓:X→Y E(𝑋,𝑌)∼𝜈 

. The ﬁrst part of the proposition tells us that 𝑓◦= 𝑓∗under Assumption 15. The framework of Ciliberto et al. (2020), tells us that 𝑓◦is obtained after decoding (8.9) of 𝑔◦: X →H, and that if 𝑔◦

$$
E𝑌∼𝜇𝑆[ℓ( 𝑓(𝑋),𝑌)]
$$

𝑛converges to 𝑔◦with the 𝐿1 norm, 𝑓◦ 𝑛converges to 𝑓◦in terms of the 𝜇◦-risk. Under Assumption 15 and mild hypothesis on 𝜇◦, it is possible to prove that convergence in terms of the 𝜇◦-risk implies convergence in terms of the 𝜇-risk (for example through calibration inequality similar to Proposition 2 of Cabannes et al. (2020b)).

### 8.A.5 Ranking with partial ordering is a well-behaved problem

Here, we discuss building directly 𝜉𝑆to initialize our alternative minimization scheme or considering 𝜇𝑆 given by the deﬁnition of well-behaved problem (Deﬁnition 58). Since the existence of 𝜇𝑆implying 𝜉𝑆 deﬁned as E𝑌∼𝜇𝑆[𝜑(𝑌)], we will only study when 𝜉𝑆can be cast as a 𝜇𝑆.

5The Wasserstein metric is useful to think in terms of distributions, which is natural when considering partial supervision that can be cast as a set of admissible fully supervised distributions. This approach has been successfully followed by Perchet and Quincampoix (2015) to deal with partial monitoring in games.

<!-- page: 145 -->

8.B. IQP IMPLEMENTATION 143 In ranking, we have that 𝜓= −𝜑, which corresponds to “correlation losses”. In this setting, we have that Span(𝜑(Y)) = Span(𝜓(Y)). More generally, looking at a “minimal” representation of ℓ, one can always assume the equality of those spans, as what happens on the orthogonal of the intersection of those spans, does not modify the scalar product 𝜑(𝑦)⊤𝜓(𝑧). Similarly, 𝜉𝑆can be restricted to Span(𝜓(Y)), and therefore Span(𝜑(Y)), which exactly the image by 𝜇→E𝑌∼𝜇[𝜑(𝑌)] of the set of signed measures, showing the existence of a 𝜇𝑆matching Deﬁnition 58.

## 8.B IQP implementation

In this section, we introduce an IQP implementation to solve for (8.4). We ﬁrst mention that our alternative minimization scheme is not restricted to well-behaved problems, before motivating the introduction of the IQP algorithm in two diﬀerent ways, and ﬁnally describing its implementation.

### 8.B.1 Initialization of alternative minimization for non-well-behaved problem

Before describing the IQP implementation to solve (8.12), we would like to stress that, even for non-well- behaved partial labeling problems, it is possible to search for smart ways to initialize variables of the alternative minimization scheme. For example, one could look at 𝑧(0) 𝑖 ∈∩𝑗;𝑥𝑗∈N𝑘𝑖𝑆𝑗, where N𝑘designs the 𝑘nearest neighbors of 𝑥𝑖in (𝑥𝑗) 𝑗≤𝑛, and 𝑘𝑖is chosen such that this intersection is a singleton.

### 8.B.2 Link with Diﬀrac and empirical risk minimization

Our IQP algorithm is similar to an existing disambiguation algorithm known as the Diﬀrac algorithm (Bach and Harchaoui, 2007; Joulin et al., 2010).6 This algorithm was derived by implicitly following empirical risk minimization of (8.2). This approach leads to algorithms written as

$$
\underset{(𝑦𝑖) ∈𝐶𝑛}{\arg\min}\, inf_{𝑓∈F} \sum_{𝑛 𝑖=1} ℓ( 𝑓(𝑥𝑖), 𝑦𝑖) + 𝜆Ω( 𝑓),
$$

for F a space of functions, and Ω : F →R+ a measure of complexity. Under some conditions, it is possible to simplify the dependency in 𝑓(e.g., Xu et al., 2004; Bach and Harchaoui, 2007). For example, if ℓ(𝑦, 𝑧) can be written as ∥𝜑(𝑦) −𝜑(𝑧)∥2 for a mapping 𝜑: X →Y, e.g. the Kendall loss detailed in Section 8.5.4,7 and the search of 𝜑( 𝑓) : X →𝜑(Y) is relaxed as a 𝑔: X →H. With Ω and F linked with kernel regression on the surrogate functional space X →H, it is possible to solve the minimization with respect to 𝑔as 𝑔(𝑥𝑖) = Í𝑛 𝑗=1 𝛼𝑗(𝑥𝑖)𝜑(𝑦𝑖), with 𝛼given by kernel ridge regression (Ciliberto et al., 2016), and to obtain a disambiguation algorithm written as

$$
\underset{𝑦𝑖∈𝑆𝑖}{\arg\min}\, \sum_{𝑛 𝑖=1} \sum_{𝑛 𝑗=1} 𝛼𝑗(𝑥𝑖)𝜑(𝑦𝑗) −𝜑(𝑦𝑖) 2.
$$

This IQP is a special case of the one we will detail. As such, our IQP is a generalization of the Diﬀrac algorithm, and this paper provides, to our knowledge, the ﬁrst consistency result for Diﬀrac.

### 8.B.3 Link with another determinism measure

While we have considered the measure of determinism given by (8.2), we could have considered its quadratic variant

$$
𝜇★∈arg min inf 𝑓:X→Y E𝑋∼𝜈X E𝑌,𝑌′∼𝜇|𝑥[ℓ(𝑌,𝑌′)] .
𝜇⊢𝜈
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This corresponds to the right drawing of Figure 8.4. We could arguably translate it experimentally as

$$
𝑛 ∑︁
( ˆ𝑦𝑖) ∈arg min 𝛼𝑖(𝑥𝑗)ℓ(𝑦𝑖, 𝑦𝑗), (8.14)
(𝑦𝑖) ∈𝐶𝑛 𝑖,𝑗=1
$$

(8.14)

6The Diﬀrac algorithm was ﬁrst introduced for clustering, which is a classical approach to unsupervised learning. In practice, it consists of changing the constraint set 𝐶𝑛= Î 𝑆𝑖by a set of the type 𝐶𝑛= arg max(𝑦𝑖)∈Y𝑛Í𝑛 𝑖,𝑗=1 1𝑦𝑖≠𝑦𝑗in (8.4) and (8.14), meaning that (𝑦𝑖) should be disambiguated into diﬀerent classes.

$$
7Since ∥𝜑(𝑦) ∥is constant.
$$

<!-- page: 146 -->

and still derive Theorem 15 when substituting (8.4) by (8.14). When the loss is a correlation loss ℓ(𝑦, 𝑧) = −𝜑(𝑦)⊤𝜑(𝑧). This leads to the quadratic problem

$$
\underset{(𝑦𝑖) ∈𝐶𝑛}{\arg\min}\, − \sum_{𝑛 𝑖,𝑗=1} 𝛼𝑖(𝑥𝑗)𝜑(𝑦𝑖)⊤𝜑(𝑦𝑗).
$$

### 8.B.4 IQP implementation

In order to make our implementation possible for any symmetric loss ℓ: Y × Y →R, on a ﬁnite space Y, we introduce the following decomposition.

Proposition 63 (Quadratic decomposition). When Y is ﬁnite, any proper symmetric loss ℓadmits a decomposition with two mappings 𝜑: Y →R𝑚, 𝜓: Y →R𝑚, for an 𝑚∈N and a 𝑐∈R, reading

$$
∀𝑦, 𝑧∈Y, ℓ(𝑦, 𝑧) = 𝜓(𝑦)⊤𝜓(𝑧) −𝜑(𝑦)⊤𝜑(𝑧) with ∥𝜑(𝑦)∥= ∥𝜓(𝑦)∥= 𝑐 (8.15)
$$

(8.15)

Proof. Consider Y = 𝑦1, ·, 𝑦𝑚and 𝐿= (ℓ(𝑦𝑖, 𝑦𝑗))𝑖,𝑗≤𝑚∈R𝑚×𝑚. 𝐿is a symmetric matrix, diagonalizable as 𝐿= Í𝑚 𝑖=1 𝜆𝑖𝑢𝑖⊗𝑢𝑖, with (𝑢𝑖) an orthonormal basis of R𝑚, and 𝜆𝑖∈R its eigenvalues. We have, with (𝑒𝑖) the Cartesian basis of R𝑚,

$$
𝑚 ∑︁ 𝑚 ∑︁
ℓ(𝑦𝑗, 𝑦𝑘) = 𝐿𝑗𝑘= 𝑒𝑗, 𝐿𝑒𝑘 = (𝜆𝑖)+ 𝑒𝑗, 𝑢𝑖 ⟨𝑒𝑘, 𝑢𝑖⟩− (𝜆𝑖)− 𝑒𝑗, 𝑢𝑖 ⟨𝑒𝑘, 𝑢𝑖⟩.
𝑖=1 𝑖=1
$$

We build the decomposition

$$
√︁ √︁ 
˜𝜓(𝑦𝑘) = (𝜆𝑖)+ ⟨𝑒𝑘, 𝑢𝑖⟩ 𝑖≤𝑚, and ˜𝜑(𝑦𝑘) = (𝜆𝑖)−⟨𝑒𝑘, 𝑢𝑖⟩
𝑖≤𝑚.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

It satisﬁes ℓ(𝑦𝑗, 𝑦𝑘) = ˜𝜓(𝑦)⊤˜𝜓(𝑧) −˜𝜑(𝑦)⊤˜𝜑(𝑧). We only need to show that we can consider 𝜑of constant norm. For

$$
˜𝜓(𝑦𝑘) 2 = Í𝑚 𝑖=1(𝜆𝑖)+ ⟨𝑢𝑖, 𝑒𝑘⟩2 ≤𝐶Í𝑚
$$

𝑖=1 ⟨𝑢𝑖, 𝑒𝑘⟩2 = 𝐶∥𝑒𝑘∥2 = 𝐶The last equalities being due to the fact that (𝑢𝑖) is orthonormal. Now, introduce the correction vector 𝜉: Y →R𝑚, this, ﬁrst consider 𝐶= max𝑖|𝜆𝑖|, we have

$$
√︃ 𝐶− ˜𝜓(𝑦) \frac{2𝑒𝑖. And consider 𝜑= ˜𝜑}{𝜉} \frac{ , 𝜓= ˜𝜓}{𝜉}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

. By construction, 𝜓is of constant norm being equal to 𝐶and 𝜉(𝑦𝑖) =

$$
𝐶− 𝜉 𝜉
$$

that ℓ(𝑦, 𝑧) = 𝜓(𝑦)𝑇𝜓(𝑧) −𝜑(𝑦)𝑇𝜑(𝑧). Finally, because ℓ(𝑦, 𝑧) = 0, we also have 𝜑of constant norm. □ Using the decomposition (8.15), (8.14) reads, with y = (𝑦𝑖)

$$
𝑛 ∑︁ 𝑛 ∑︁
ˆy ∈arg min 𝛼𝑖(𝑥𝑗)𝜓(𝑦𝑖)𝜓(𝑦𝑗) − 𝛼𝑖(𝑥𝑗)𝜑(𝑦𝑖)𝜑(𝑦𝑗).
y∈𝐶𝑛 𝑖=1 𝑖=1
$$

By deﬁning the matrix 𝐴= (𝛼𝑖(𝑥𝑗))𝑖𝑗≤𝑛∈R𝑛×𝑛, Ψ(y) = (𝜓(𝑦𝑖))𝑖≤𝑛∈R𝑛×𝑚and Φ(y) = (𝜑(𝑦𝑖))𝑖≤𝑛∈R𝑛×𝑚, we cast it as

$$
Tr 𝐴Ψ(y)Ψ(y)⊤ −Tr 𝐴Φ(y)Φ(y)⊤ .
ˆy ∈arg min
y∈𝐶𝑛
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Objective convexiﬁcation. As 𝛼𝑖(𝑥𝑗) is a measure of similarity between 𝑥𝑖and 𝑥𝑗, 𝐴is usually symmetric positive deﬁnite, making this objective convex in Ψ and concave in Φ. However, recalling (8.15), we have Tr ΦΦ⊤= Tr ΨΨ⊤= 𝑛𝑐, therefore considering the spectral norm of 𝐴, we convexify the objective as

$$
Tr (∥𝐴∥∗𝐼+ 𝐴)Ψ(y)Ψ(y)⊤ + Tr (∥𝐴∥∗𝐼−𝐴)Φ(y)Φ(y)⊤ .
ˆy ∈arg min
y∈𝐶𝑛
 ∥𝐴∥∗𝐼+ 𝐴 0 0 ∥𝐴∥∗𝐼−𝐴 Ψ(y)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Considering

$$
𝐵= and Ξ(y) = ,
Φ(y)
$$

simpliﬁes this objective as

$$
\underset{y∈𝐶𝑛}{\arg\min}\, Tr 𝐵Ξ(y)Ξ(y)⊤ .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

When parametrized by 𝜉= Ξ(y), this is an optimization problem with a convex quadratic objective and “integer-like” constraint 𝜉∈Ξ(𝐶𝑛), identifying to an integer quadratic program (IQP).

<!-- page: 147 -->

8.C. EXAMPLE WITH GRAPHICAL ILLUSTRATIONS 145

$$
b b b b
𝑅𝑏
𝑅𝑎 𝑅𝜈
𝑅𝑐
a c a c a c a c
$$

[FIGURE: Figure 8.4]

Figure 8.4: Exposition of a pointwise problem in the simplex ΔY, with Y = {𝑎, 𝑏, 𝑐} and a proper symmetric loss deﬁned by ℓ(𝑎, 𝑏) = ℓ(𝑎, 𝑐) = ℓ(𝑏, 𝑐)/2. (Left) Representation of the decision regions 𝑅𝑧=

$$
𝑧∈arg min𝑧′∈Y E𝑌∼𝜇[ℓ(𝑧, 𝑦)] 𝜇⊢𝜈
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

for 𝑧∈Y. (Middle Left) Representation of 𝑅𝜈=

$$
𝜇∈ΔY 𝜇∈ΔY
$$

for 𝜈= (5𝛿{𝑎,𝑏,𝑐} + 𝛿{𝑐} + 𝛿{𝑎,𝑐} + 𝛿{𝑏,𝑐})/8. (Middle Right) Level curves of the piecewise function ΔY →R; 𝜇→min𝑧∈Y E𝑌∼𝜇[ℓ(𝑧,𝑌)] corresponding to (8.2). (Right) Level curves of the quadratic func- tion ΔY →R; 𝜇→E𝑌,𝑌′∼𝜇[ℓ(𝑌,𝑌′)]. Our disambiguation (8.2) corresponds to minimizing the concave function represented in the middle right drawing on the convex domain represented in the middle left drawing.

Relaxation. IQP are known to be NP-hard, several tools exist in literature and optimization libraries implementing them. The most classical approach consists in relaxing the integer constraint 𝜉∈Ξ(𝐶𝑛) into the convex constraint 𝜉∈Conv(Ξ(𝐶𝑛)), solving the resulting convex quadratic program, and projecting back the solution toward an extreme of the convex set. Arguably, our alternative minimization approach is a better grounded heuristic to solve our speciﬁc disambiguation problem.

## 8.C Example with graphical illustrations

To ease the understanding of the disambiguation principle (8.2), we provide a toy example with a graphical illustration, Figure 8.4. Since (8.2) decorrelates inputs, we will consider X to be a singleton, in order to remove the dependency to X. In the following, we consider Y = {𝑎, 𝑏, 𝑐}, with the loss given by

$$
𝐿= (ℓ(𝑦, 𝑧))𝑦,𝑧∈Y = ©­ 0 1 1 1 0 2 1 2 0 ª® ¬
.
«
𝑧⊤1 = 1
$$

This problem can be represented on a triangle through the embedding of probability measures reading 𝜉: ΔY →R3; 𝜇→𝜇(𝑎)𝑒1 + 𝜇(𝑏)𝑒2 + 𝜇(𝑐)𝑒3, and onto the triangle 

. Note that 𝜉can be extended from any signed measure of total mass normalized to one onto the plane

$$
\frac{𝑧∈R3}{+} 𝑧∈R3 𝑧⊤1 = 1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

, as well as the drawings Figure 8.4 can be extended onto the aﬃne span of the represented triangles. The objective (8.2) reads pointwise as ΔY →R; 𝜇→min𝑖≤3 𝑒⊤ +

𝑖𝐿𝜉(𝜇), while its quadratic version reads ΔY →Y; 𝜇→𝜉(𝜇)⊤𝐿𝜉(𝜇). Note that while 𝐿is not deﬁnite negative, one can check that the restriction of R3 →R; 𝑧→𝑧⊤𝐿𝑧to the deﬁnition domain

$$
𝑧∈R3 𝑧⊤1 = 1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

is concave, as suggested by the right drawing of Figure 8.4.

It should be noted that (ℓ, 𝜈) being a well-behaved partial labeling problem can be understood graphically, as having the intersection of the decision regions ∩𝑧∈𝑆𝑅𝑧non-empty for any set 𝑆in the support of 𝜈. As such, it is easy to see that our toy problem is well-behaved for any distribution 𝜈. Formally, to match Deﬁnition 58, we can deﬁne 𝜇{𝑒} = 𝛿𝑒for 𝑒∈{𝑎, 𝑏, 𝑐} and

$$
𝜇{𝑎,𝑏} = .5𝛿𝑎+ .5𝛿𝑏, 𝜇{𝑎,𝑐} = .5𝛿𝑏+ .5𝛿𝑐, 𝜇{𝑏,𝑐} = 𝛿𝑏+ 𝛿𝑐−𝛿𝑎, 𝜇{𝑎,𝑏,𝑐} = .5𝛿𝑏+ .5𝛿𝑐.
$$

Graphically 𝜉(𝜇{𝑎,𝑏}) can be chosen as any points on the horizontal dashed line on the middle right drawing of Figure 8.4 (similarly for 𝜉𝜇{𝑎,𝑐}), while 𝜉(𝜇{𝑎,𝑏,𝑐}) has to be chosen has the intersection .5𝑒2 + .5𝑒3, and while 𝜉(𝜇{𝑏,𝑐}) has to be chosen outside the simplex on the half-line leaving .5𝑒2 + .5𝑒3 supported by the perpendicular bisector of [𝑒2, 𝑒3] and not containing 𝑒1.

## 8.D Experiments

While our results are much more theoretical than experimental, out of principle, as well as for reproducibility, comparison and usage sake, we detail our experiments.

<!-- page: 148 -->

### 8.D.1 Interval regression - Figure 8.1

Figure 8.1 corresponds to the regression setup consisting of learning 𝑓∗: [0, 1] →R; 𝑥→sin(𝜔𝑥), with 𝜔= 10 ≈3𝜋. The dataset represented on Figure 8.1 is collected in the following way. We sample (𝑥𝑖)𝑖≤𝑛 with 𝑛= 10, uniformly at random on X = [0, 1], after ﬁxing a random seed for reproducibility. We collect 𝑦𝑖= 𝑓(𝑥𝑖). We create (𝑠𝑖) by sampling 𝑢𝑖uniformly on [0, 1], deﬁning 𝑟𝑖= 𝑟−𝛾log(𝑢𝑖), with 𝑟= 1 and 𝛾= 3−1, sampling 𝑐𝑖uniformly at random on [0, 𝑟𝑖], and deﬁning 𝑠𝑖= 𝑦𝑖+ sign(𝑦𝑖) · 𝑐𝑖+ [−𝑟𝑖, 𝑟𝑖]. The corruption is skewed on purpose to showcase disambiguation instability of the baseline (8.13) compared to our method. We solve (8.4) with alternative minimization, initialized by taking 𝑦(0) 𝑖 at the center of 𝑠𝑖, and stopping the minimization scheme when Í

$$
\frac{𝑖≤𝑛|𝑦(𝑡+1)}{𝑖}
$$

𝑖| < 𝜀for 𝜀a stopping criterion ﬁxed to 10−6. For 𝑥∈X, the inference (8.5) and (8.13) is done through grid search, considering, for 𝑓𝑛(𝑥), 1000 guesses dividing uniformly [−6, 6] ⊂Y = R. We consider weights 𝛼given by kernel ridge regression with Gaussian kernel, deﬁned as

$$
𝑖 −𝑦(𝑡)
𝛼(𝑥) = (𝐾+ 𝑛𝜆𝐼)−1𝐾𝑥∈R𝑛, 𝐾= (𝑘(𝑥𝑖, 𝑥𝑗))𝑖,𝑗≤𝑛∈R𝑛×𝑛, 𝐾𝑥= (𝑘(𝑥𝑖, 𝑥))𝑖≤𝑛∈R𝑛,
 2𝜎2 
−∥𝑥−𝑥′ ∥2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑘(𝑥, 𝑥′) = exp , and 𝜆a regularization parameter, and 𝜎a standard deviation parameter. In our simulation, we ﬁx 𝜎= .1 based on simple considerations on the data, while we consider 𝜆∈[10−1, 10−3, 10−6]. The evaluation of the mean square error between 𝑓𝑛and 𝑓∗, which is equivalent to evaluating the risk with the regression loss ℓ(𝑦, 𝑧) = ∥𝑦−𝑧∥2, is done by considering 200 points dividing uniformly X = [0, 1] and evaluating 𝑓𝑛and 𝑓∗on it. The best hyperparameter 𝜆is chosen by minimizing this error. It leads to 𝜆= 10−1 for the baseline (8.13), and 𝜆= 10−6 for our algorithm (8.4) and (8.5). This diﬀerence in 𝜆is normal since both methods are not estimating the same surrogate quantities. The fact that 𝜆is smaller for our algorithm is natural as our disambiguation objective (8.4) already has a regularization eﬀect on the solution.8 Note that we used the same weights 𝛼for (8.4) and (8.5), which is suboptimal, but fair to the baseline, as, consequently, both methods have the same number of hyperparameters.

### 8.D.2 Classiﬁcation - Figure 8.2

Figure 8.2 corresponds to classiﬁcation problems, based on real datasets from the LIBSVM datasets repository. At the time of writing, the datasets are available at https://www.csie.ntu.edu.tw/~cjlin/ libsvmtools/datasets/multiclass.html. We present results on the “DNA” and “Svmguide2” datasets, that both have 3 classes (𝑚= 3), and respectively have 4000 samples with 180 features (𝑛= 4000,𝑑= 180) and 391 samples with 20 features (𝑛= 391, 𝑑= 20).

In terms of complexity, when Y = ⟦1, 𝑚⟧= {1, 2, · · · , 𝑚}, and weights based on kernel ridge regression with Gaussian kernel as described in the last paragraph the complexity of performing inference for (8.5) and (8.13) can be done in 𝑂(𝑛𝑚) in time and 𝑂(𝑛+ 𝑚) in space, where 𝑛is the number of training samples (Nowak-Vila et al., 2019; Cabannes et al., 2020b). The disambiguation (8.4) performed with alternative minimization is done in 𝑂(𝑐𝑛2𝑚) in time and in 𝑂(𝑛(𝑛+ 𝑚)) in space, with 𝑐the number of steps in the alternative minimization scheme. In practice, 𝑐is really small, which can be understood since we are minimizing a concave function and each step leads to a guess on the border of the constraint domain.

Based on the dataset (𝑥𝑖, 𝑦𝑖), we create (𝑠𝑖) by sampling it accordingly to 𝛾𝛿{𝑦𝑖} + 1 −𝛾𝛿{𝑦,𝑦𝑖}, with 𝑦 the most present labels in the dataset (indeed we choose the two datasets because they were not too big and presenting unequal labels proportion), and 𝛾∈[0, 1] the corruption parameter represented in percentage on the 𝑥-axis of Figure 8.2. This skewed corruption allows distinguishing methods and invalidates the simple approach consisting of averaging candidate (AC) in set to recover 𝑦𝑖from 𝑠𝑖, which works well when data are missing at random (Heitjan and Rubin, 1991). We separate (𝑥𝑖, 𝑠𝑖) in 8 folds, consider 𝜎∈𝑑· [1, .1, .01], where 𝑑is the dimension of X, and 𝜆∈𝑛−1/2 · [1, 10−3, 10−6], where 𝑛is the number of data. We tested the diﬀerent hyperparameter setup and reported the best error for each corruption parameter on Figure 8.2. Those errors are measured with the 0-1 loss, computed as averaged over the 8 folds, i.e. cross-validated, with standard deviation represented as error bars on the ﬁgure. The best hyperparameter generally corresponds to 𝜎= .1 and 𝜆= 10−3 when the corruption is small and 𝜎= 1, 𝜆= 10−3 when the corruption is big.

8Moreover, the analysis in Cabannes et al. (2020b) suggests that the baseline is estimating a surrogate function in X →2R, while our method is estimating a function in X →R, which is a much smaller function space, hence needing less regularization. However, those reﬂections are based on upper bounds, that might be suboptimal, which could invalidate those considerations.

<!-- page: 149 -->

8.D. EXPERIMENTS 147 Diﬀerences between cross-validated error and testing error were small, and we presented the ﬁrst one out of simplicity.

In terms of energy cost, the experiments were run on a personal laptop that has two processors, each of them running 2.3 billion instructions per second. During experiments, all the data were stored on the random access memory of 8 GB. Experiments were run on Python, extensively relying on the NumPy library (Harris et al., 2020). The heaviest computation is Figure 8.2. Its total runtime, cross-validation included, was around 70 seconds. This paper is the result of experimentation, we evaluate the total cost of our experimentation to be three orders of magnitude higher than the cost of reproducing the ﬁnal computations presented on Figure 8.1, 8.2 and 8.3. The total computational energy cost is negligible.

### 8.D.3 Semi-supervised learning - Figure 8.3

Underlying scores Ground truth Items preferences Scores X X

[FIGURE: Figure 8.5]

Figure 8.5: Ranking setting. We consider X an interval of R, and Y = S𝑚with 𝑚= 4 on the ﬁgure. (Right) To create a ranking dataset, we sample randomly 𝑚lines in R2, embedding a value, or equivalently a score, associated to each item as a function of the input 𝑥. (Left) By ordering those lines, we create preferences between items as a function of 𝑥. On the ﬁgure, when 𝑥is small, the “red” item is preferred over the “orange” item, itself preferred over the “blue” item, itself preferred over the “green” item. While when 𝑥is big, “green” is preferred over “blue”, preferred over “orange”, preferred over “red”. We create a partial labeling dataset by sampling (𝑥𝑖) ∈X 𝑛, and providing only partial ordering that the (𝑦𝑖) follow. For example, for a small 𝑥, we might only give the partial information that “red” is preferred over “blue”.

Ranking, m=10 DF IL AC Loss 50 60 70 80 90 100 Corruption (p.d.u.)

[FIGURE: Figure 8.6]

Figure 8.6: Performance of our algorithm for ranking with partial ordering. This ﬁgure is similar to Figure 8.2, but is based on the ranking problem illustrated on Figure 8.5. For this ﬁgure, we consider 𝑚= 10, as it is arguably the limit where the LP relaxation provided by Cabannes et al. (2020b) of the NP-hard minimum feedback arcset problem still performs well. The corruption parameter corresponds to the proportion of coordinates lost in the Kendall embedding when creating 𝑠𝑖from 𝑦𝑖. Because the Kendall embedding satisﬁes transitivity constraints, a corruption smaller than 50% is almost ineﬀective to remove any information. In this ﬁgure, we observe a similar behavior for ranking to the one observed for classiﬁcation on Figure 8.2, suggesting that those empirical ﬁndings are not spurious.

On Figure 8.3, we review a semi-supervised classiﬁcation problem with Y = ⟦1, 4⟧, X = [−4.5, 4.5]2, 𝜇X only charging

$$
𝑥= (𝑥1, 𝑥2) ∈R2 𝑥2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

1 + 𝑥2 2 ∈N∗ and the solution 𝑓∗: X →Y being deﬁned almost

<!-- page: 150 -->

1 + 𝑥2 2. We collect a dataset (𝑥𝑖, 𝑠𝑖), by sampling 2000 points 𝜃𝑖uniformly at random on [0, 1], as well as 𝑟𝑖uniformly at random in ⟦1, 4⟧= {1, 2, 3, 4}, before building 𝑥𝑖= 𝑟𝑖· (cos(2𝜋𝜃𝑖), sin(2𝜋𝜃𝑖)) ∈X, and 𝑠𝑖= Y. We add four labeled points to this dataset 𝑥2001 = (−2 everywhere as 𝑓∗(𝑥) = 𝑥2

$$
√
$$

3, 2) with 𝑠2001 = {4}, 𝑥2001 = (1, −2

$$
√ 2) with 𝑠2002 = {3}, 𝑥2001 = (− √
$$

3, −1) with 𝑠2003 = {2} and 𝑥2001 = (−1, 0) with 𝑠2004 = {1}. We designed the weights 𝛼in (8.4) with 𝑘-nearest neighbors, with 𝑘= 20, and solve this equation with a variant of alternative minimization, leading to the optimal solution ˜𝑦𝑖= 𝑦∗ 𝑖. In order to be able to compute the baseline (8.13), we design weights 𝛼for the inference task based on Nadaraya-Watson estimators with Gaussian kernel, deﬁned as 𝛼𝑖(𝑥) = exp

$$
∥𝑥−𝑥𝑖∥2 /ℎ
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

, with ℎ= .08. We solve the inference task on a grid of X composed of 2500 points, and artiﬁcially recreate the observations to make them neat and reduce the resulting PDF size. Note that it is possible to design weights 𝛼that capture the cluster structure of the data, which, in this case, will lead to a nice behavior of the baseline as well as our algorithm. Arguably, this experiment showcases a regularization property of our algorithm (8.4).

### 8.D.4 Ranking with partial ordering

To conclude this experiment section, we look at ranking with partial ordering. We refer to Section 8.5.4 for a clear description of this instance of partial labeling. We provide to the reader eager to use our method, an implementation of our algorithm, available online at https://github.com/VivienCabannes/partial_ labelling/. It is based on LP relaxation of the NP-hard minimum feedback arcset problem. This relaxation was proven exact when 𝑚≤6 by Cabannes et al. (2020b). The LP implementation relies on CPLEX (IBM, 2017). As complementary experiments, we will not provide much reproducibility details, those details would be really similar to the previous paragraphs, and the curious reader could run our code instead. We present our ranking setup on Figure 8.5 and our results on Figure 8.6.

<!-- page: 151 -->

# Chapter 9. Laplacian Regularization

The following is a reproduction of Cabannes et al. (2021a).

As annotations of data can be scarce in large-scale practical problems, leveraging unlabeled examples is one of the most important aspects of machine learning. This is the aim of semi-supervised learning. To beneﬁt from the access to unlabeled data, it is natural to diﬀuse knowledge of labeled data to unlabeled one. This induces the use of Laplacian regularization. Yet, current implementations of Laplacian regularization suﬀer from several drawbacks, notably the well-known curse of dimensionality. In this paper, we provide a statistical analysis to overcome those issues, and unveil a large body of spectral ﬁltering methods that exhibit desirable behaviors. They are implemented through (reproducing) kernel methods, for which we provide realistic computational guidelines in order to make our method usable with large amounts of data.

## 9.1 Introduction

In the last decade, machine learning has been able to tackle amazingly complex tasks, which was mainly allowed by computational power to train large learning models on large annotated datasets. For instance, ImageNet is made of tens of millions of images, which have all been manually annotated by humans (Deng et al., 2009). The greediness in data annotation of such a current learning paradigm is a major limitation. In particular, when annotation of data demands in-depth expertise, relying on techniques that require zillions of labeled data is not viable. This motivates several research streams to overcome the need for annotations, such as self-supervised learning for images or natural language processing (Devlin et al., 2019). Aiming for generality, semi-supervised learning is the most classical one, assuming access to a vast amount of input data, but among which only a scarce percentage is labeled. To leverage the presence of unlabeled data, most semi-supervised techniques assume a form of low-density separation hypothesis, as detailed in the recent review of van Engelen and Hoos (2020), and illustrated by state-of the-art models (Berthelot et al., 2019; Verma et al., 2019). This hypothesis assumes that the function to learn from the data varies smoothly in highly populated regions of the input space, but might vary more strongly in sparsely populated areas, or that the decision frontiers between classes lie in regions with low-density. In such a setting, it is natural to enforce constraints on the variations of the function to learn. While semi-supervised learning is an important learning framework, it has not provided as many exciting realizations as one could have expected. This might be related to the fact that it is classically approached through graph-based Laplacian, a technique that does not scale well with the dimension of the input space (Bengio et al., 2006).

Paper organization. In Section 9.2, we motivate Laplacian regularization, and recall drawbacks of naive implementations. These limitations are overcome in Section 9.3 where we expose a theoretically principled path to derive well-behaved algorithms. More precisely, we unveil a vast class of estimates based on spectral ﬁltering. We turn to implementation in Section 9.4 where we provide realistic guidelines to ensure scalability of the proposed algorithms. Statistical properties of our estimators are stated in Section 9.5.

Contributions. They are two folds. (i) Statistically, we explain that Laplacian regularization can be properly leveraged based on functional space considerations, and that those considerations can be turned into concrete implementations thanks to kernel methods. As a result, we provide consistent estimators that exhibit

149

<!-- page: 152 -->

fast convergence rates under a low density separation hypothesis, and that, in particular, do not suﬀer from the curse of dimensionality. (ii) Computationally, we avoid dealing with large matrices of derivatives by providing a low-rank approximation that allows dealing with 𝑛𝛾log(𝑛) × 𝑛𝛾log(𝑛) matrices, with a parameter 𝛾∈(0, 1] depending on the regularity of the problem, instead of 𝑛(𝑑+ 1) × 𝑛(𝑑+ 1) matrices, thus cutting down to O(log(𝑛)2𝑛1+2𝛾𝑑) the potential O(𝑛3𝑑3) training cost.

Related work. Interplay between graph theory and machine learning were proven successful in the 2000s (Smola and Kondor, 2003). The seminal paper of Zhu et al. (2003) introduced graph-Laplacian as a transductive method in the context of semi-supervised learning. A smoothing variant was proposed by (Zhou et al., 2003), which is coherent with the fact that enforcing constraints on labeled points leads to spikes (Alaoui et al., 2016). Interestingly, graph Laplacian do converge to diﬀusion operators linked with the weighted Laplace Beltrami operator (Hein et al., 2007; García Trillos et al., 2019). However, these local diﬀusion methods are known to suﬀer from the curse of dimensionality (Bengio et al., 2006). That is, local averaging methods are intuitive learning methods that have been used for more than half a century (Fix and Hodges, 1951). Yet, those methods do not scale well with the dimension of the input space (Yang, 1999). This is related to the fact that to cover [0, 1]𝑑, we need 𝜀−𝑑balls of radius 𝜀. Interestingly, if the function to learn is 𝑚times diﬀerentiable with smooth partial derivatives, it is possible to leverage more information from function evaluations and overcome the curse of dimensionality when 𝑚≳𝑑. This property is related to covering numbers (a.k.a. capacity) of Sobolev spaces (Kolmogorov and Tikhomirov, 1959), and is leveraged by (reproducing) kernel methods (Steinwart and Christmann, 2008; Caponnetto and De Vito, 2006). The crux of this paper is to apply this fact to Laplacian regularization techniques. Note that derivatives with reproducing kernel methods in machine learning have already been considered in diﬀerent settings by (Zhou, 2008; Rosasco et al., 2013; Eriksson et al., 2018).

## 9.2 Laplacian regularization

In this section, we introduce the notations and concepts related to the semi-supervised learning regression problem, noting that most of our results extend to any convex loss beyond least-squares. We motivate and describe Laplacian regularization that will allow us to leverage the low-density separation hypothesis. We explain statistical drawbacks usually linked with Laplacian regularization, and discuss how to circumvent them.

In the following, we denote by X = R𝑑the input space, Y = R the output space, and by 𝜌∈ΔX×Y the joint distribution on X × Y. For simplicity, we assume that 𝜌has compact support. In the following, we denote by 𝜌X the marginal of 𝜌over X, and by 𝜌|𝑥the conditional distribution of 𝑌given 𝑋= 𝑥. As usual, for 𝑝∈N∗, 𝐿𝑝(R𝑑) is the space of functions 𝑓such that 𝑓𝑝is integrable. Moreover, we deﬁne usual Sobolev spaces: for 𝑠∈N, 𝑊𝑠,𝑝(R𝑑) stands for the space of functions whose weak derivatives of order 𝑠-th are in 𝐿𝑝(R𝑑). When 𝑝= 2, they have a Hilbertian structure, and we denote, 𝐻𝑠(R𝑑) = 𝑊𝑠,2(R𝑑) these Hilbertian spaces. Ideally, we would like to retrieve the mapping 𝑔∗: X →Y deﬁned as

$$
∥𝑔(𝑋) −𝑌∥2 𝑔−𝑔𝜌 2
𝑔∗= arg min E(𝑋,𝑌)∼𝜌 = arg min 𝐿2(𝜌X ) = 𝑔𝜌, (9.1)
𝑔∈𝐿2(𝜌X ) 𝑔∈𝐿2(𝜌X )
$$

(9.1)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑔𝜌: X →Y is deﬁned as 𝑔𝜌(𝑥) = E [𝑌| 𝑋= 𝑥]. In semi-supervised learning, we assume that we do not have access to 𝜌, but we have access to 𝑛independent samples (𝑋𝑖)𝑖≤𝑛∼𝜌⊗𝑛 X , among which we have 𝑛ℓ labels 𝑌𝑖∼𝜌|𝑋𝑖for 𝑖≤𝑛ℓ, with 𝑛ℓpotentially much smaller than 𝑛. In other terms, we have 𝑛ℓsupervised pairs (𝑋𝑖,𝑌𝑖)𝑖≤𝑛ℓ, and 𝑛−𝑛ℓunsupervised samples (𝑋𝑖)𝑛ℓ<𝑖≤𝑛. While we restrict ourselves to real-valued regression for simplicity, our exposition indeed applies generically to partially supervised learning. In particular, it can be used oﬀ-the-shelve to complement the approaches of (Cabannes et al., 2020b, 2021b) as we detailed in Appendix 9.A. Diﬀusion operator L

### 9.2.1

In order to leverage unlabeled data, we will assume that 𝑔∗varies smoothly on highly populated regions of X, and might vary highly on low density regions. For example, this is the case when data are clustered in well separated regions of space, and labels are constant on clusters. This is captured by the fact that the Dirichlet

<!-- page: 153 -->

Semi-supervision setting Baseline: 휆= 0, 휇= 1 Result: 휆= 1, 휇= 1/푛

[FIGURE: Figure 9.1]

Figure 9.1: Motivating example. (Left) We suppose given 𝑛= 2000 points in X = R2, represented as black dots, spanning 4 concentric circles. Among those points are 𝑛ℓ= 4 labeled points, with labels being either 1 represented in red, and −1 represented in blue. In this setting, it is natural to assume that 𝑔∗should be constant on each circle, which can be encoded as ∥∇𝑔∗∥= 0 on supp 𝜌X . (Middle) Kernel ridge regression estimate based on the labeled points with Gaussian kernel of bandwidth 𝜎= .2𝑟, 𝑟being the radius of the innermost circle. (Right) Laplacian regularization reconstruction. The reconstruction is based on approximate empirical risk minimization with 𝑝= 𝑛, which ensures a computational complexity of 𝑂(𝑝2𝑛𝑑), instead of 𝑂(𝑛3𝑑3) needed to recover the exact empirical risk minimizer (9.5). energy ∫

$$
h ∥∇𝑔∗(𝑋)∥2i L1/2𝑔
∥∇𝑔∗(𝑥)∥2 𝜌X (d𝑥) = E𝑋∼𝜌X 2
=: 𝐿2(𝜌X ) , (9.2)
X
$$

(9.2)

is assumed to be small. Because the quadratic functional (9.2) will play a crucial role in our exposition, we deﬁne L as the self-adjoint operator on 𝐿2(𝜌X ), extending the operator on 𝐻1(𝜌X ) representing this functional. Under mild assumptions on 𝜌X , L−1 can be shown to be a compact operator, which we will assume in the following. In essence, we will assume that if we have a lot of unlabeled data and

$$
L1/2𝑔
$$

can be well approximated for any function 𝑔, then we do not need a lot of labeled data to estimate correctly 𝑔∗. To illustrate this, at one extreme, if we know that L1/2𝑔∗

 = 0, then 𝑔∗is known to be constant on each connected component of 𝜌X so that, along with the knowledge of 𝜌X , only a few labeled points would be suﬃcient to recover perfectly 𝑔∗. We illustrate those considerations on Figure 9.1.

### 9.2.2 Drawbacks of naive Laplacian regularization

Following the motivations presented previously, it is natural to consider the regularized objective and solution deﬁned, for 𝜆> 0, as

$$
∥𝑔(𝑋) −𝑌∥2 
𝑔𝜆= arg min E(𝑋,𝑌)∼𝜌 + 𝜆E𝑋∼𝜌X ∥∇𝑔(𝑋)∥2
R𝑑
𝑔∈𝐻1(𝜌X ) L1/2𝑔
𝑔−𝑔𝜌 2 (9.3)
2
= arg min 𝐿2(𝜌X ) + 𝜆 𝐿2(𝜌X ) = (𝐼+ 𝜆L)−1𝑔𝜌.
𝑔∈𝐻1(𝜌X )
$$

(9.3)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This regularization has nice properties. In particular, for small 𝜆, it can be seen as a ﬁrst order approximation of the heat equation solution 𝑒−𝜆L𝑔𝜌, which represents the temperature proﬁle at time 𝑡= 𝜆, instantiated with the initial proﬁle 𝑔𝜌, and with 𝜌X modeling the thermal conductivity. It also has interpretations in terms of random walk and Langevin diﬀusion (Pillaud-Vivien, 2020a; Klus et al., 2020). In a word, 𝑔𝜆is the diﬀusion of 𝑔𝜌with respect to the density 𝜌X , which relates to the idea of diﬀusing labeled data with respect to the intrinsic geometry of the data, which is the idea captured by (Zhu et al., 2003).

However, from a learning perspective, (9.3) is linked with the prior that 𝑔∗belongs to 𝐻1(𝜌X ), a prior that is not strong enough to overcome the curse of dimensionality as we saw in the related work section. Moreover, assuming we have enough unsupervised data to suppose known 𝜌X , and therefore L, (9.3) leads to the naive empirical estimate 𝑔(naive) ∈arg min𝑔:X→R

$$
L1/2𝑔
$$

2 . While the deﬁnition of 𝑔(naive) could seem like a great idea, in fact, such an estimate 𝑔(naive) is known to be mostly constant and spiking to interpolate the data (𝑋𝑖,𝑌𝑖) as soon as 𝑑> 2 (Nadler et al., 2009). This is to be related with the capacity of the space associated with the pseudo-norm

$$
\frac{Í𝑛ℓ}{𝑖=1 ∥𝑔(𝑋𝑖) −𝑌𝑖∥2 +𝑛ℓ𝜆}
$$

in 𝐿2. This capacity, related to 𝐻1, is too large for the Laplacian regularization term to constraint 𝑔(naive) in a meaningful way. In other terms, we need to regularize with stronger penalties.

$$
L1/2𝑔
$$

<!-- page: 154 -->

### 9.2.3 Stronger regularization

In this subsection, we discuss techniques to overcome the issues encountered with 𝑔(naive). Those techniques are based on functional space constraints or on spectral ﬁltering techniques.

Functional spaces. A solution to overcome the capacity issue of 𝐻1 in 𝐿2 is to constrain the estimate of 𝑔∗

$$
∫
$$

to belong to a smaller functional space. In the realm of graph Laplacian, (Alaoui et al., 2016) proposed to solve this problem by considering the 𝑟-Laplacian regularization reading Ω𝑟= X ∥∇𝑔(𝑋)∥𝑟𝜌(d𝑥), with 𝑟> 𝑑. In essence, this restricts 𝑔to live in 𝑊1,𝑟(𝜌X ) for 𝑟> 𝑑, and allows avoiding spikes associated with 𝑔(naive). However, considering high power of the gradient is likely to introduce instability (think that 𝑑is the potentially colossal dimension of the input space), and from a learning perspective, the capacity of 𝑊1,𝑟, which compares to the one of 𝐻2, is still too big. In this paper, we will rather keep the diﬀusion operator L, and add a second penalty to reduce the space in which we look for the solution. With G a Hilbert space of functions, we could look for, with 𝜇> 0 a second regularization parameter

$$
𝑔−𝑔𝜌 2 L1/2𝑔
2
𝑔𝜆,𝜇= arg min 𝑔:G∩𝐻1(𝜌X ) 𝐿2(𝜌X ) + 𝜆 𝐿2(𝜌X ) + 𝜆𝜇∥𝑔∥2 G . (9.4)
$$

(9.4)

This formulation restricts 𝑔𝜆,𝜇to belong both to 𝐻1(𝜌X ) (thanks to the term in 𝜆) and G (thanks to the term in 𝜇). In particular the resulting space 𝐻1(𝜌X ) ∩G to which 𝑔𝜆,𝜇belongs, has a smaller capacity in 𝐿2 than the one of G in 𝐿2. In practice, we do not have access to 𝜌and 𝜌X but to (𝑋𝑖,𝑌𝑖)𝑖≤𝑛ℓand (𝑋𝑖)𝑖≤𝑛, and we might consider the empirical estimator deﬁned through empirical risk minimization

$$
𝑛ℓ ∑︁ 𝑛 ∑︁
𝑔𝑛ℓ,𝑛= arg min 𝑛−1 ∥𝑔(𝑋𝑖) −𝑌𝑖∥2 + 𝜆𝑛−1 ∥∇𝑔(𝑋𝑖)∥2 + 𝜆𝜇∥𝑔∥2 G . (9.5)
ℓ
𝑔∈G 𝑖=1 𝑖=1
$$

(9.5)

For example, we could consider G to be the Sobolev space 𝐻𝑚(d𝑥). Note the diﬀerence between G linked with d𝑥, the Lebesgue measure, that is known, and L linked with 𝜌X , the marginal of 𝜌over X, that is not known. In this setting, the regularization ∥L1/2𝑔∥2 + 𝜇∥𝑔∥2

$$
∫ X ∥𝐷𝑔(𝑥)∥2 𝜌X (d𝑥) + 𝜇 ∫ X Í𝑚
$$

𝛼=0 ∥𝐷𝛼𝑔(𝑥)∥2 d𝑥. Because of the size of 𝐻𝑚in 𝐿2, this allows for eﬃcient approximation of 𝑔𝜆,𝜇based on empirical risk minimization. In particular, if 𝑛= +∞, we expect the minimizer (9.5) to converge toward 𝑔𝜆,𝜇at rates in 𝐿2

$$
G reads X ∥𝐷𝑔(𝑥)∥2 𝜌X (d𝑥) + 𝜇 X
$$

scaling similarly to 𝑛−𝑚/𝑑 ℓ in 𝑛ℓ. To complete the picture, depending on a prior on 𝑔𝜌, 𝑔𝜆,𝜇might exhibit good convergence properties toward 𝑔𝜌as 𝜆and 𝜇go to zero. This contrasts with the problem encountered with 𝑔(naive). Those considerations are exactly what reproducing kernel Hilbert space will provide, additionally with a computationally friendly framework to perform the estimation. Note that quantities similar to 𝑔𝜆,𝜇 were considered in (Zhou, 2008; Rosasco et al., 2013).

Spectral ﬁltering. Without looking for higher power-norm, (Nadler et al., 2009) proposed to overcome the capacity issue by considering approximation of the operator L based on the graph-based technique provided by (Belkin and Niyogi, 2003; Coifman and Lafon, 2006) and to reduce the search of 𝑔𝑛ℓon the space spanned by the ﬁrst few eigenvectors of the Laplacian. In particular, on Figure 9.1, 𝑔∗could be searched in the null space of L, that is, among functions that are constant on each connected component of supp 𝜌X . This technique exhibits two parts, the “unsupervised” estimation of L that will depend on the total number of data 𝑛, and the “supervised” search for 𝑔𝜌on the ﬁrst few eigenvectors of L that will depend on the number of labels 𝑛ℓ. While, at ﬁrst sight, this technique seems to be completely diﬀerent from Tikhonov regularization (9.4), it can be cast, along with gradient descent, into the same spectral ﬁltering framework (Lin et al., 2020). This point of view enables the use of a wide range of techniques oﬀered by spectral manipulations on the diﬀusion operator L.

This paper is motivated by the fact that current well-grounded semi-supervised learning techniques are implemented based on graph-based Laplacian, which is a local averaging method that does not leverage smartly functional capacity. In particular, as recalled earlier, graph-based Laplacian is known to suﬀer from the curse of dimensionality, in the sense that the convergence of the empirical estimator b L toward the L exhibits a rate of convergence of order O(𝑛−1/𝑑) with 𝑑the dimension of the input space X (Hein et al., 2007). In this work, we will bypass this curse of dimensionality by looking for 𝑔in a smooth universal reproducing kernel Hilbert space, which will lead to eﬃcient empirical estimates.

<!-- page: 155 -->

## 9.3 Spectral ﬁltering with kernel Laplacian

In this section, we approach Laplacian regularization from a functional analysis perspective. We ﬁrst introduce kernel methods and derivatives in reproducing kernel Hilbert space (RKHS). We then translate the considerations provided in Section 9.2.3 in the realm of kernel methods.

### 9.3.1 Kernel methods and derivatives evaluation maps

In this subsection, we introduce kernel methods (see (Aronszajn, 1950; Scholkopf and Smola, 2001; Steinwart and Christmann, 2008) for more details). Consider (H, ⟨·, ·⟩H) a reproducing kernel Hilbert space, that is a Hilbert space of functions from X to R such that the evaluation functionals 𝐿𝑥: H →R; 𝑔→𝑔(𝑥) are continuous linear forms for any 𝑥∈X. Such forms can be represented by 𝑘𝑥∈H such that, for any 𝑔∈H, 𝐿𝑥(𝑔) = ⟨𝑘𝑥, 𝑔⟩H. A reproducing kernel Hilbert space can alternatively be deﬁned from a symmetric positive semi-deﬁnite kernel 𝑘: X →X →R, that is a function such that for any 𝑛∈N and (𝑥𝑖)𝑖≤𝑛∈X 𝑛the matrix (𝑘(𝑥𝑖, 𝑥𝑗))𝑖,𝑗is symmetric positive semi-deﬁnite, by building (𝑘𝑥)𝑥∈X such that 𝑘(𝑥, 𝑥′) = ⟨𝑘𝑥, 𝑘𝑥′⟩H. From a learning perspective, it is useful to use the evaluation maps to rewrite H = {𝑔𝜃: 𝑥→⟨𝑘𝑥, 𝜃⟩H | 𝜃∈H}. As such, kernel methods can be seen as “linear models” with features 𝑘𝑥, allowing to parametrize large spaces of functions (Micchelli et al., 2006). In the following, we will diﬀerentiate 𝜃seen as an element of H and 𝑔𝜃seen as its embedding in 𝐿2. To make this distinction formal, we deﬁne the embedding 𝑆: (H, ⟨·, ·⟩H) ↩→(𝐿2(𝜌X ), ⟨·, ·⟩𝐿2); 𝜃→𝑔𝜃, as well as its adjoint 𝑆★: 𝐿2(𝜌X ) →H.

Given a linear parametric model of functions 𝑔𝜃(𝑥) = ⟨𝜃, 𝑘𝑥⟩H, it is possible to compute derivatives of 𝑔𝜃based on derivatives of the feature vector – think of H = R𝑝and of 𝑘𝑥= 𝜑(𝑥) as a feature vector with 𝜑: R𝑑→R𝑝. For 𝛼∈N𝑑, with |𝛼| = Í 𝑖≤𝑑𝛼𝑖, we have the following equality of partial derivatives, when 𝑘 is 2 |𝛼| times diﬀerentiable,

$$
𝐷𝛼𝑔𝜃(𝑥) = ⟨𝜃, 𝐷𝛼𝑘𝑥⟩, where 𝐷𝛼= 𝜕|𝛼|
(𝜕𝑥1)𝛼1(𝜕𝑥2)𝛼2 · · · (𝜕𝑥𝑑)𝛼𝑑.
$$

Here and 𝐷𝛼𝑘𝑥has to be understood as the partial derivative of the mapping of 𝑥∈X to 𝑘𝑥∈H, which can be shown to belong to H (Zhou, 2008). In the following, we assume that 𝑘is twice diﬀerentiable with continuous derivatives, and will make an extensive use of derivatives of the form 𝜕𝑖𝑘𝑥= 𝜕𝑘𝑥/𝜕𝑥𝑖for 𝑖≤𝑑and 𝑥∈X. Note that, as well as we can describe completely the Hilbertian geometry of the space Span {𝑘𝑥| 𝑥∈X } through 𝑘(𝑥, 𝑥′) = , for 𝑥, 𝑥′ ∈X, we can describe the Hilbertian geometry of Span {𝑘𝑥| 𝑥∈X } + Span {𝜕𝑖𝑘𝑥| 𝑥∈X }, through

$$
𝑘𝑥, 𝑘′
𝑥
𝜕𝑖𝑘𝑥, 𝜕𝑗𝑘𝑥′
𝜕1,𝑖𝑘(𝑥, 𝑥′) = ⟨𝜕𝑖𝑘𝑥, 𝑘𝑥′⟩H , and 𝜕1,𝑖𝜕2,𝑗𝑘(𝑥, 𝑥′) = H ,
$$

where 𝜕1,𝑖denotes the partial derivative with respect to the 𝑖-th coordinates of the ﬁrst variable. This echoes the so-called “representer theorems”.

Example 16 (Gaussian kernel). A classical kernel is the Gaussian kernel, also known as radial basis function, deﬁned for 𝜎> 0 as the following 𝑘, and satisfying, for 𝑖≠𝑗, the following equalities,

$$
−∥𝑥−𝑥′∥2 , 𝜕1,𝑖𝜕2,𝑗𝑘(𝑥, 𝑦) = −(𝑥𝑖−𝑦𝑖)(𝑥𝑗−𝑦𝑗)
𝑘(𝑥, 𝑥′) = exp 𝜎4 𝑘(𝑥, 𝑦),
2𝜎2 1 
𝜕1,𝑖𝑘(𝑥, 𝑦) = −(𝑥𝑖−𝑦𝑖) 𝜎2 −(𝑥𝑖−𝑦𝑖)2
𝜎2 𝑘(𝑥, 𝑦), 𝜕1,𝑖𝜕2,𝑖𝑘(𝑥, 𝑦) = 𝑘(𝑥, 𝑦),
𝜎4
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑥𝑖designs the 𝑖-th coordinates of the vector 𝑥∈X = R𝑑.

### 9.3.2 Tikhonov, spectral ﬁltering and dimensionality reduction

Given the kernel 𝑘, its associated RKHS H and 𝑆the embedding of H in 𝐿2, we rewrite (9.4) under its “parametrized” version

$$
𝑆𝜃−𝑔𝜌 L1/2𝑆𝜃 
2
2
𝑔𝜆,𝜇= 𝑆arg min 𝐿2(𝜌X ) + 𝜆 𝐿2(𝜌X ) + 𝜆𝜇∥𝜃∥2 . (9.4)
H
𝜃∈H
$$

(9.4)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 156 -->

Eigen vector #1 (푒1) Eigen vector #4 (푒4) Eigen vector #8 (푒8)

[FIGURE: Figure 9.2]

Figure 9.2: Few of the ﬁrst generalized eigenvectors of ( ˆΣ; ˆ𝐿+ 𝜇𝐼) (with 𝜇= 1/𝑛). The ﬁrst four eigenvectors correspond to constant functions on each circle, as shown with 𝑒1 and 𝑒4. The few eigenvectors after correspond to second harmonics localized on a single circle as shown with 𝑒8.

Do not hesitate to refer to Table 9.1 to keep track of notations. In the following, we will use that L1/2𝑆𝜃

$$
\frac{2}{𝐿2(𝜌X ) + 𝜇∥𝜃∥2} H = (𝑆★L𝑆+ 𝜇𝐼)1/2𝜃 2
$$

H . This equality explains why we consider 𝜇𝜆instead of 𝜇 in the last term. In the RKHS setting, the study of (9.4) unveils the three operators Σ, 𝐿, and 𝐼on H, (indeed 𝑔𝜆,𝜇= 𝑆arg min𝜃∈H

$$
\frac{H =}{𝜃★(Σ + 𝜆𝐿+ 𝜆𝜇)𝜃−2𝜃★𝑆★𝑔𝜌}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

) where 𝐼is the identity, and, as we detail in Appendix 9.C,

$$
" 𝑑 ∑︁ #
Σ = 𝑆★𝑆= E𝑋∼𝜌X [𝑘𝑋⊗𝑘𝑋] , and 𝐿= 𝑆★L𝑆= E𝑋∼𝜌X 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋 . (9.6)
𝑖=1
$$

(9.6)

Regularization and spectral ﬁltering have been well-studied in the inverse-problem literature. In particular, the regularization (9.4) is known to be linked with the generalized singular value decomposition of [Σ; 𝐿+ 𝜇𝐼] (see, e.g., Edelman and Wang (2020)), which is linked to the generalized eigenvalue decomposition of (Σ, 𝐿+ 𝜇𝐼) (Golub and Loan, 2013). We derive the following characterization of (9.4), whose proof is reported in Appendix 9.D.

Proposition 64. Let (𝜆𝑖,𝜇)𝑖∈N ∈RN, (𝜃𝑖,𝜇)𝑖∈N ∈HN be the generalized eigenvalue decomposition of the pair (Σ, 𝐿+ 𝜇𝐼), that is (𝜃𝑖,𝜇) generating H and such that for any 𝑖, 𝑗∈N, Σ𝜃𝑖,𝜇= 𝜆𝑖,𝜇(𝐿+ 𝜇𝐼)𝜃𝑖,𝜇, and

$$
= 1𝑖=𝑗. (9.4) can be rewritten as
$$

𝜃𝑖,𝜇, (𝐿+ 𝜇𝐼)𝜃𝑗,𝜇

$$
∑︁ !
∑︁
𝑔𝜆,𝜇= 𝜓(𝜆𝑖,𝜇)𝑆𝜃𝑖,𝜇⊗𝑆𝜃𝑖,𝜇 𝑔𝜌= 𝜓(𝜆𝑖,𝜇) 𝑆★𝑔𝜌, 𝜃𝑖,𝜇 𝑆𝜃𝑖,𝜇, (9.7)
𝑖∈N 𝑖∈N
$$

(9.7)

with 𝜓: R+ →R; 𝑥→(𝑥+ 𝜆)−1. (9.7) should be seen as a speciﬁc instance of spectral ﬁltering based on a ﬁlter function 𝜓: R+ →R.

Interestingly, the generalized eigenvalue decomposition of the pair (Σ, 𝐿+ 𝜇𝐼) was already considered by Pillaud-Vivien (2020a) to estimate the ﬁrst eigenvalue of the Laplacian. Moreover, Pillaud-Vivien (2020b) suggests leveraging this decomposition for dimensionality reduction based on the ﬁrst eigenvectors of the Laplacian. As well as (9.4) contrasts with graph-based semi-supervised learning techniques, this dimensionality reduction technique contrasts with methods based on graph Laplacian provided by (Belkin and Niyogi, 2003; Coifman and Lafon, 2006). Remarkably, the semi-supervised learning algorithm that consists in using the unsupervised data to perform dimensionality reduction based on the Laplacian eigenvalue decomposition, before solving a small linear regression problem on the small resulting space, can be seen as a speciﬁc instance of spectral ﬁltering, based on regularization by thresholding/cutting-oﬀeigenvalue, which corresponds to 𝜓: 𝑥→𝑥−11𝑥>𝜆for a given threshold 𝜆> 0 in (9.7).

## 9.4 Implementation

In this section, we discuss how to practically implement estimates for (9.7) based on empirical data (𝑋𝑖,𝑌𝑖)𝑖≤𝑛ℓ and (𝑋𝑖)𝑛ℓ<𝑖≤𝑛. We ﬁrst review how we can approximate the integral operators of (9.6) based on data. We then discuss how to implement our methods practically on a computer. We end this section by considering approximations that allow cutting down high computational costs associated with kernel methods involving

<!-- page: 157 -->

derivatives.

Algorithm 1: Empirical estimates based on spectral ﬁltering.

Data: (𝑋𝑖,𝑌𝑖)𝑖≤𝑛ℓ, (𝑋𝑖)𝑛ℓ<𝑖≤𝑛, a kernel 𝑘, a ﬁlter 𝜓, a regularizer 𝜇 Result: ˆ𝑔𝑝through 𝑐∈R𝑝deﬁning ˆ𝑔𝑝(𝑥) = Í𝑛

$$
𝑖=1 𝑐𝑖𝑘(𝑥, 𝑋𝑖) = 𝑘★
$$

𝑥𝑇𝑎𝑐 Compute 𝑆𝑛𝑇𝑎= (𝑘(𝑋𝑖, 𝑋𝑗))𝑖≤𝑛,𝑗≤𝑝∈R𝑛×𝑝in O(𝑝𝑛) Compute 𝑍𝑛𝑇𝑎= (𝜕1,𝑗𝑘(𝑋𝑙, 𝑋𝑖))( 𝑗≤𝑑,𝑙≤𝑛),𝑖≤𝑝∈R𝑛𝑑×𝑝in O(𝑝𝑛𝑑) Build 𝑇★

$$
𝑎ˆΣ𝑇𝑎= 𝑛−1(𝑆𝑛𝑇𝑎)⊤(𝑆𝑛𝑇𝑎) in O(𝑝2𝑛) Build 𝑇★
𝑎ˆ𝐿𝑇𝑎= 𝑛−1(𝑍𝑛𝑇𝑎)⊤(𝑍𝑛𝑇𝑎) in O(𝑝2𝑛𝑑)a
Build 𝑇★
$$

𝑎𝑇𝑎= (𝑘(𝑋𝑖, 𝑋𝑗))𝑖,𝑗≤𝑝∈R𝑝×𝑝in O(1) as a partial copy of 𝑆𝑛𝑇𝑎 Get (𝜆𝑖,𝜇, 𝑢𝑖,𝜇)𝑖≤𝑛the generalized eigenelements of (𝑇★

$$
𝑎( ˆ𝐿+ 𝜇𝐼)𝑇𝑎) in O(𝑝3) Get 𝑏= 𝑇★ Í𝑛ℓ 𝑎ˆΣ𝑇𝑎,𝑇★
𝑖=1 𝑌𝑖𝑘(𝑋𝑖, 𝑋𝑗)) 𝑗≤𝑝∈R𝑝in O(𝑝𝑛ℓ) Return 𝑐= Í𝑛 𝑎ˆ𝜃= (𝑛−1
ℓ
𝑖=1 𝜓(𝜆𝑖)𝑢𝑖𝑢⊤ 𝑖𝑏∈R𝑝in O(𝑝3).
$$

aBuilding this matrix can be avoided by using the generalized singular value decomposition rather than the generalized eigenvector decomposition. Implemented with Lapack, such a procedure will also require 𝑂(𝑝2𝑛𝑑) ﬂoating point operations, but with a smaller constant in the big 𝑂(Golub and Loan, 2013).

### 9.4.1 Integral operators’ approximation

The classical empirical risk minimization in (9.5) can be understood as the plugging of the approximate distributions ˆ𝜌= 𝑛−1

$$
\frac{Í𝑛ℓ}{𝑖=1 𝛿𝑋𝑖⊗𝛿𝑌𝑖and ˆ𝜌X = 𝑛−1 Í𝑛}
$$

𝑖=1 𝛿𝑋𝑖instead of 𝜌and 𝜌X in (9.4). It can also be understood as the same replacement when dealing with integral operators, leading to the three following important quantities to rewrite (9.7),

$$
ℓ
𝑛 ∑︁ 𝑛 ∑︁ 𝑑 ∑︁ 𝑛ℓ ∑︁
𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋𝑖, ˆ𝜃:= 𝑆★𝑔𝜌:= 𝑛−1
ˆΣ := 𝑛−1 𝑘𝑋𝑖⊗𝑘𝑋𝑖, ˆ𝐿:= 𝑛−1 𝑌𝑖𝑘𝑋𝑖. (9.8)
ℓ
𝑖=1 𝑖=1 𝑗=1 𝑖=1
$$

(9.8)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

It should be noted that while considering 𝑛in the deﬁnition of ˆΣ is natural from the spectral ﬁltering perspective, to make it formally equivalent with the empirical risk minimization (9.5), it should be replaced by 𝑛ℓ. (9.8) allows rewriting (9.7) without relying on the knowledge of 𝜌, by considering ( ˆ𝜆𝑖,𝜇, ˆ𝜃𝑖,𝜇) the generalized eigenvalue decomposition of ( ˆΣ, ˆ𝐿) and considering

$$
∑︁ D E
 𝑆★𝑔𝜌, ˆ𝜃𝑖,𝜇
ˆ𝑔= 𝜓( ˆ𝜆𝑖,𝜇) 𝑆ˆ𝜃𝑖,𝜇, (9.9)
𝑖∈N
$$

(9.9)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We present the ﬁrst eigenvectors (after plunging them in 𝐿2 through 𝑆) of the generalized eigenvalue decomposition of ( ˆΣ, ˆ𝐿+ 𝜇𝐼) on Figure 9.2. The ﬁrst eigenvectors recover the null space of L. This explains clearly the behavior on the right of Figure 9.1.

### 9.4.2 Matrix representation and approximation of operators

Currently, we are dealing with operators (ˆΣ, ˆ𝐿) and vectors (e.g., ˆ𝜃) in the Hilbert space H. It is natural to wonder how to represent this on a computer. The answer is the object of representer theorems (see Theorem 1 of (Zhou, 2008)), and consists in noticing that all the objects introduced are actually deﬁned in, or operate on, H𝑛+ H𝑛,𝜕⊂H, with H𝑛= Span

$$
𝑖≤𝑛 𝑖≤𝑛, 𝑗≤𝑑
and H𝑛,𝜕= Span
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

. This subspace of H is of dimension at most 𝑛(𝑑+ 1) and if 𝑇: R𝑝→H𝑛+ H𝑛,𝜕(with 𝑝≤𝑛(𝑑+ 1)) parametrizes H𝑛+ H𝑛,𝜕, our problem can be cast in R𝑝by considering the 𝑝× 𝑝matrices 𝑇★ˆΣ𝑇and 𝑇★( ˆ𝐿+ 𝜇𝐼)𝑇instead of the operators ˆΣ and ˆ𝐿+ 𝜇𝐼. The canonical representation consists in taking 𝑝= 𝑛(𝑑+ 1) and considering for 𝑐∈R𝑛(𝑑+1), the mapping 𝑇𝑐𝑐= Í𝑛

$$
\frac{𝑘𝑋𝑖}{𝑖=1 𝑐𝑖0𝑘𝑋𝑖+ Í𝑑} 𝜕𝑗𝑘𝑋𝑖
$$

𝑗=1 𝑐𝑖𝑗𝜕𝑗𝑘𝑋𝑖(Zhou, 2008; Rosasco et al., 2013). This exact implementation implies dealing and ﬁnding the generalized eigenvalue decomposition of 𝑝× 𝑝 matrices with 𝑝= 𝑛(𝑑+ 1), which leads to computational costs in O(𝑛3𝑑3), which can be prohibitive. Two solutions are known to cut down prohibitive computational costs of kernel methods. Both methods consist in looking for a space that can be parametrized by R𝑝for a small 𝑝and that approximates well the space H𝑛+ H𝑛,𝜕⊂H. The ﬁrst solution is provided by random features (Rahimi and Recht, 2007). It consists in approximating H with a space of small dimension 𝑝∈N, linked with an explicit representation 𝜑: X →R𝑝 that approximate 𝑘(𝑥, 𝑥′) ≃𝑘𝜑(𝑥, 𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩R𝑝. In theory, it substitutes the kernel 𝑘by 𝑘𝜑. In practice, all computations can be done with the explicit feature 𝜑.

<!-- page: 158 -->

Approximate solution. The second solution, which we are going to use in this work, consists in approxi- mating H𝑛+ H𝑛,𝜕by H𝑝= Span 

𝑖≤𝑝for 𝑝≤𝑛. This method echoes the celebrated Nyström method (Williams and Seeger, 2000), as well as the Rayleigh–Ritz method for Sturm–Liouville problems. In essence, (Rudi et al., 2015) shows that, when considering subsampling based on leverage score, 𝑝= 𝑛𝛾log(𝑛), with 𝛾∈(0, 1] linked to the “size” of the RKHS and the regularity of the solution, is a good enough approximation, in the sense that it only downgrades the sample complexity by a constant factor. In theory, we know that the space H𝑝will converge to H = Closure Span {𝑘𝑥}𝑥∈supp 𝜌X as 𝑝goes to inﬁnity. In practice, it means considering the approximation mapping 𝑇𝑎: R𝑝→H; 𝑐→Í𝑝

$$
𝑘𝑋𝑖
$$

𝑖=1 𝑐𝑖𝑘𝑋𝑖, and dealing with the 𝑝× 𝑝 matrices 𝑇★

$$
𝑎Σ𝑇𝑎and 𝑇★
$$

𝑎𝐿𝑇𝑎. It should be noted that the computation of 𝑇★ 𝑎𝐿𝑇𝑎requires to multiply a 𝑝× 𝑛𝑑 matrix by its transpose. Overall, training this method can be done with O(𝑝2𝑛𝑑) basic operations, and inference with this method can be done in O(𝑝). The saving cost of this approximate method is huge: without compromising the precision of our estimator, we went from 𝑂(𝑛3𝑑3) run time complexities to 𝑂(log(𝑛)2𝑛1+2𝛾𝑑) computations, with 𝛾possibly very small. Similarly, the memory cost went from 𝑂(𝑛2𝑑2) down to 𝑂(𝑛𝑑+ 𝑛2𝛾).1

## 9.5 Statistical analysis

In this section, we are interested in quantifying the risk of the learned mapping ˆ𝑔. We study it through the generalization bound, which consists in obtaining a bound on the averaged excess risk Edata ∥ˆ𝑔−𝑔𝜌∥2 𝐿2. In particular, we want to answer the following points.

1. How, and under which assumptions, Laplacian regularization boosts learning? 2. How the excess of risk relates to the number of labeled and unlabeled data? In terms of priors, we want to leverage a low-density separation hypothesis. In particular, we can suppose that when diﬀusing 𝑔𝜌with 𝑒−𝑡L we stay close to 𝑔𝜌, or that 𝑔𝜌is supported on a ﬁnite dimensional space of functions on which

$$
L1/2𝑔
$$

(which measures the variation of 𝑔) is small. Both those assumptions can be made formal by assuming the 𝑔𝜌is supported by the ﬁrst eigenvectors of the diﬀusion operator L.

Assumption 17 (Source condition). 𝑔𝜌is supported on a ﬁnite dimensional space that is left stable by the diﬀusion operator L. In other terms, if (𝑒𝑖) ∈(𝐿2)N are the eigenvectors of L, there exists 𝑟∈N, such that 𝑔𝜌∈Span {𝑒𝑖}𝑖≤𝑟.

We will also assume that the diﬀusion operator L can be well approximated by the RKHS associated with 𝑘. In practice, under mild assumptions, c.f. Appendix 9.C, the eigenvectors of the Laplacian are known to be regular, in particular to belong to 𝐻𝑚for 𝑚∈N bigger than 𝑑. As such, many classical kernels would verify the following assumption.

Assumption 18 (Approximation condition). The eigenvectors (𝑒𝑖) of L belong to the RKHS H.

We add one technical assumptions regarding the eigenvalue decay of the operator Σ compared to the operator 𝐿, with ⪯denoting the Löwner order (i.e., for 𝐴and 𝐵symmetric, 𝐴⪯𝐵if 𝐵−𝐴is positive semi-deﬁnite).

Assumption 19 (Eigenvalue decay). There exists 𝑎∈[0, 1] and 𝑐> 0 such that 𝐿⪯𝑐Σ𝛼.

Note that, in our setting, 𝐿is compact and bounded and Assumption 19 is always satisﬁed with 𝑎= 0. For translation-invariant kernels, such as Gaussian or Laplace kernels, based on considerations linking eigenvalue decay of operators with functional space capacities (Steinwart and Christmann, 2008), under mild assumptions, we can take 𝑎> 1 −2/𝑑. We discuss all assumptions in more detail in Appendix 9.C.

To study the consistency of our algorithms, we can reuse the extensive literature on kernel ridge regression (Caponnetto and De Vito, 2006; Lin et al., 2020).

This literature body provides an extensive picture on convergence rates relying on various ﬁlters and assumptions of capacity, a.k.a. eﬀective dimension, and source conditions. Our setting is slightly diﬀerent and showcases two speciﬁcities: (i) the eigenelements (𝜆𝑖,𝜇, 𝜃𝑖,𝜇) are dependent of 𝜇; (ii) the low-rank approximation in Algorithm 1 is speciﬁc to settings with derivatives. We end our exposition with the following convergence result, proven in Appendix 9.E. Note that the dependency of 𝑝in 𝑛can be improved based on subsampling techniques that leverage expressiveness of the diﬀerent (𝑘𝑋𝑖) (Rudi et al., 2015).

1Our code is available online at https://github.com/VivienCabannes/partial_labelling.

<!-- page: 159 -->

Classiﬁcation error Computational complexity 0.4 kernelized graph-based Training time (s) 101 small kernel full kernel graph-based Loss (0-1) 10−1 0.2 10−3 102 103 101 102 103 Number of samples Number of samples

[FIGURE: Figure 9.3]

Figure 9.3: (Left) Comparison between our kernelized Laplacian method (Tikhonov regularization version with 𝜆= 1, 𝜇𝑛= 𝑛−1, 𝑝= 50) and graph-based Laplacian based on the same Gaussian kernel with bandwidth 𝜎𝑛= 𝑛−1 𝑑+4 log(𝑛) as suggested by graph-based theoretical results (Hein et al., 2007). We report classiﬁcation error as a function of the number of samples 𝑛. The error is averaged over 50 trials, with error bars representing standard deviations. We ﬁxed the ratio 𝑛ℓ/𝑛to one tenth, and generated the data according to two Gaussian in dimension 𝑑= 10 with unit variance and whose centers are at distance 𝛿= 3 of each other (similar to the setting of (Castelli and Cover, 1995; Lelarge and Miolane, 2019)). Our method discovers the structure of the data much faster than graph-based Laplacian (to get a 20% error we need 40 points, while graph-based needs 700). (Right) Time to perform training with graph-based Laplacian in orange, with Algorithm 1 in blue (with the speciﬁcation of the left ﬁgure), and with the naive representation in R𝑛(𝑑+1) of the empirical minimizer (9.5) in green. When dealing with 1000 points, our algorithm, as well as graph-based Laplacian, can be computed in about one tenth of a second on a 2 GHz processor, while the naive kernel implementation requires 10 seconds. We show in Appendix 9.B that this cut in costs is not associated with a loss in performance.

Moreover, universal consistency results could also be provided when the RKHS is dense in 𝐻1, as well as convergence rates for other ﬁlters and laxer assumptions which we discuss in Appendix 9.E (in particular, the source condition can be relaxed by considering the biggest 𝑞∈(0, 1] such that 𝑔∈im L𝑞).

Theorem 16 (Convergence rates). Under Assumptions 17, 18 and 19, for 𝑛ℓ, 𝑛∈N, when considering the spectral ﬁltering Algorithm 1 with 𝜓𝜆: 𝑥→(𝑥+ 𝜆)−1, there exists a constant 𝐶independent of 𝑛, 𝑛ℓ, 𝜆, 𝜇 and 𝑝such that the estimate ˆ𝑔𝑝deﬁned in Algorithm 1 veriﬁes

$$
h

 ˆ𝑔𝑝−𝑔𝜌 2 i 
𝜎2 ℓ𝑛−1 ℓ + 𝑛−2 𝜆𝜇 + log(𝑝) ℓ + 𝑛−1 𝑝 + 𝜆log(𝑝)𝑎
ED𝑛 𝜆2 + 𝜆𝜇+ , (9.10)
≤𝐶
𝐿2 𝑝𝑎
$$

(9.10)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝜎2 ℓis a variance parameter that relates to the variance of the variable 𝑌(𝐼+ 𝜆L)−1𝛿𝑋, inheriting its randomness from (𝑋,𝑌) ∼𝜌. In particular, when the ratio 𝑟= 𝑛ℓ/𝑛is ﬁxed, with the regularization scheme 𝜆𝑛= 𝜆0𝑛−1/4, 𝜇𝑛= 𝜇0𝑛−1/4, for any 𝜆0 > 0 and 𝜇0 > 0, and the subsampling scheme 𝑝𝑛= 𝑝0𝑛𝑠log(𝑛) for any 𝑝0 > 0 and with 𝑠= max(1/2, 1/4𝑎), there exists a constant 𝐶′ independent of 𝑛and 𝑛ℓsuch that the excess of risk veriﬁes

$$
h

 ˆ𝑔𝑝−𝑔𝜌 2 i
ED𝑛 ≤𝐶′(𝑛−1/2 + 𝜎2 ℓ𝑛−1/2 ℓ ). (9.11)
𝐿2
$$

(9.11)

Theorem 16 answers the two questions asked at the beginning of this section. In particular, it characterizes the dependency of the need for labeled data to a variance parameter linked with the diﬀusion of observations (𝑋𝑖,𝑌𝑖) based on the density 𝜌X through the operator L. Intuitively, if the index set 𝐼⊂{1, 2, · · · , 𝑛} of data (𝑋𝑖)𝑖∈𝐼we labeled does not change the proﬁle of the diﬀusion solution ˆ𝑔, then we do not need that much labeled data – as this is the case on Figure 9.1.

Finally, Theorem 16 is remarkable in that it exhibits no dependency to the dimension of X in the power of 𝑛and 𝑛ℓ. This contrasts with graph-based Laplacian methods that do not scale well with the input space dimensionality (Bengio et al., 2006; Hein et al., 2007). Indeed, Figure 9.3 shows the superiority of our method over graph-based Laplacian in dimension 𝑑= 10, with a mixture of Gaussian. We provide details as well as additional experiments in Appendix 9.B.

## 9.6 Conclusion

Diﬀusing information or enforcing regularity through penalties on derivatives are natural ideas to tackle many machine learning problems. Those ideas can be captured informally with graph-based techniques and ﬁnite

<!-- page: 160 -->

element diﬀerences, or captured more formally with the diﬀusion operator we introduced in this work. This formalization allowed us to shed light on Laplacian regularization techniques based on statistical learning considerations. In order to make our method usable in practice, we provided strong computational guidelines to cut down prohibitive costs associated with a naive implementation of our methods. In particular, we were able to develop computationally eﬃcient semi-supervised techniques that do not suﬀer from the curse of dimensionality.

This work paves the way to many extensions beyond semi-supervised learning. For example, in Appendix 9.A, we describe its usefulness to the partial supervised learning problem, where minimizing the Dirichlet energy provide a learning principle, in order to bypass the restrictive non-ambiguity assumption usually made in this setup (Cour et al., 2011; Liu and Dietterich, 2014; Cabannes et al., 2020b, 2021b). Moreover, in the context of active learning, retaking the strategy of Karzand and Nowak (2020), this energy provides a computationally-eﬀective, theoretically-grounded, data-dependent score to select the next point to query. As such, follow-ups would be of interest to see how this introductory theoretical paper makes its way into the world of concrete applications.

<!-- page: 161 -->

# Appendix

## 9.A Extension to partially supervised learning

In this section, we ﬁrst show how our work can be extended to generic semi-supervised learning problems, beyond real-valued regression. This ﬁrst extension is based on the least-square surrogate introduced by Ciliberto et al. (2020) for structured prediction problems. We later show how our work can be extended to generic partially-supervised learning. This second extension is based on the work of Cabannes et al. (2020b).

### 9.A.1 Structured prediction and least-square surrogate

Until now, we have considered the least-square problem with 𝑌∈R. Indeed, our work can be extended easily to a wide class of learning problems. Consider Y an output space, ℓ: Y × Y →R a loss function, and keep X ⊂R𝑑and 𝜌∈ΔX×Y. Suppose that we want to retrieve

$$
𝑓∗= arg min R( 𝑓), with R( 𝑓) = E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)] . (9.12)
𝑓:X→Y
$$

(9.12)

Ciliberto et al. (2020) showed that as soon as ℓcan be decomposed through two mappings 𝜑: Y →HY and 𝜓: Y →HY with HY a Hilbert space as ℓ(𝑦, 𝑧) = ⟨𝜑(𝑦), 𝜓(𝑧)⟩HY, it is possible to leverage the least-square regression by considering the surrogate problem

$$
h i
𝑔∗∈arg min E(𝑋,𝑌)∼𝜌 ∥𝑔(𝑋) −𝜑(𝑌)∥2 . (9.13)
𝑔:X→HY HY
$$

(9.13)

This surrogate problem relates to the original one through the decoding 𝑑that relates a surrogate estimate 𝑔: X →HY to an estimate of the original problem 𝑓: X →Y as 𝑓= 𝑑(𝑔) deﬁned through, for 𝑥∈supp 𝜌X ,

$$
𝑓(𝑥) = arg min ⟨𝜓(𝑧), 𝑔(𝑥)⟩HY . (9.14)
𝑧∈Y
$$

(9.14)

In the real-valued regression case, presented previously, our estimates for 𝑔𝑛can all be written as 𝑔𝑛(𝑥) = Í𝑛ℓ 𝑖=1 𝛽𝑖(𝑥)𝑌𝑖, where 𝛽𝑖(𝑥) is a function of the (𝑋𝑖)𝑖≤𝑛, involving the kernel 𝑘and its derivatives. Those estimates can be cast to vector-valued regression by considering coordinates-wise regression,2 which leads to 𝑔𝑛(𝑥) = Í𝑛ℓ 𝑖=1 𝛽𝑖(𝑥)𝜑(𝑌𝑖), and to the original estimates, for any 𝑥∈supp 𝜌X ,

$$
𝑛ℓ ∑︁
𝑓𝑛(𝑥) ∈arg min 𝛽𝑖(𝑥)ℓ(𝑧,𝑌𝑖). (9.15)
𝑧∈Z 𝑖=1
$$

(9.15)

The behavior of 𝑓𝑛being independent of the decomposition (𝜑, 𝜓) of ℓwas referred to as the loss trick. In particular, Ciliberto et al. (2020) showed that convergence rates derived between ∥𝑔𝑛−𝑔∗∥𝐿2 does not change if we consider 𝑔: X →R or 𝑔: X →HY and that those rates can be cast directly as convergence rates between R( 𝑓𝑛) and R( 𝑓∗) with 𝑓𝑛= 𝑑(𝑔𝑛) deﬁned by (9.14). Moreover, when Y is a discrete output space, it is possible to get much better generalization bound on R( 𝑓𝑛) −R∗by introducing geometrical considerations regarding 𝑔∗and decision frontier between classes (Cabannes et al., 2021c).

2To parametrize functions 𝑔from X to HY, we can parametrize independently each coordinates ⟨𝑔, 𝑒𝑖⟩HY , for (𝑒𝑖) a basis of HY, by the space G – note that it is possible to generalize real-valued kernel to parametrize coordinates in a joint fashion (Caponnetto and De Vito, 2006). The coordinate-wise parametrization corresponds to the tensorization H′ = HY ⊗H and to the parametric space G′ = {𝑥→Θ𝑘𝑥| Θ ∈H′} of functions from X to HY. G′ naturally inherits the Hilbertian structure of H′, itself inherited from the structure of H and HY.

159

<!-- page: 162 -->

Example 17 (Binary classiﬁcation). This framework aims at generalizing well known surrogate considerations in the case of the binary classiﬁcation. Binary classiﬁcation corresponds to Y = {−1, 1}, ℓthe 0 −1 loss. In this setting, HY = R, 𝜑: Y →R; 𝑦→𝑦, and 𝜓= −𝜑. This deﬁnition veriﬁes ℓ(𝑦, 𝑧) = .5 −.5𝜑(𝑦)⊤𝜑(𝑧) ≃ 𝜑(𝑦)⊤𝜓(𝑧). This corresponds to the usual least-square surrogate, which is R𝑆(𝑔) = E[∥𝑔(𝑋) −𝑌∥2], 𝑔(𝑥) = E [𝑌| 𝑋= 𝑥] and 𝑓= sign 𝑔.

Beyond least-squares. Considering a least-square surrogate assumes that retrieving 𝑔∗(9.13) is the way to solve the original problem (9.12) and that the low-density separation hypothesis can be expressed as Assumption 17 being veriﬁed by 𝑔∗. We would like to point out that the low-density separation could be expressed under a much weaker form, which is that there exists 𝑔such that 𝑓∗= 𝑑(𝑔) (9.14) and 𝑔veriﬁes Assumption 17. In particular, the cluster assumption (Rigollet, 2007) could be understood as assuming that 𝑔= 𝜑( 𝑓∗), the trivial embedding of 𝑓∗in HY, is constant on clusters, which means that 𝑔belongs to the kernel of the Laplacian operator L. Yet, 𝑔∗: 𝑥→E[𝜑(𝑌)|𝑋= 𝑥], which depends on the labeling noise, could be really non-smooth, even under the cluster assumption. Those considerations are related to an open problem in machine learning, which is that we do not know what is the best statistical way (and the best surrogate problem) to solve the fully supervised binary classiﬁcation problem (see e.g. Zhang and Agarwal, 2020). However, many points introduced in the work could be retaken with other surrogate, could it be SVM (which leads to 𝑔∗= 𝜑( 𝑓∗), with 𝑔∗minimizing the Hinge loss), softmax regression (used in deep learning) or others.

### 9.A.2 Partially supervised learning

Partial supervision is a popular instance of weak supervision, which generalizes semi-supervised learning. It has been known under the name of partial labeling (Cour et al., 2011), superset learning (Liu and Dietterich, 2014), as well as learning with partial label (Grandvalet, 2002), with partial annotation (Lou and Hamprecht, 2012), with candidate labeling set (Luo and Orabona, 2010) or with multiple label (Jin and Ghahramani, 2002). It encompasses many problems such as “classiﬁcation with partial labels” (Nguyen and Caruana, 2008; Cour et al., 2011), “multilabeling with missing labels” (Yu et al., 2014), “ranking with partial ordering” (Hüllermeier et al., 2008), “regression with censored data” (Tobin, 1958), “segmentation with pixel annotation” (Verbeek and Triggs, 2008; Papandreou et al., 2015), as well as instances of “action retrieval”, especially on instructional videos (Alayrac et al., 2016; Miech et al., 2019). It consists, for a given input 𝑥, in not observing its label 𝑦∈Y, but observing a set of potential labels 𝑠∈2Y that contains the labels (𝑦∈𝑠). Typically, if Y is the space S𝑚of orderings between 𝑚items (e.g. movies on a streaming website), for a given input 𝑥(e.g. some feature vectors characterizing a user) 𝑠might be speciﬁed by a partial ordering that the true label 𝑦 should satisfy (e.g. the user prefers romantic movies over action movies).

In this setting, it is natural to create consensus between the diﬀerent sets giving information on (𝑦|𝑥), which has been formalized mathematically by the inﬁmum loss (𝑧, 𝑠) ∈Y × 2Y →inf𝑦∈𝑠ℓ(𝑧, 𝑦) ∈R for ℓ: Y × Y →R a speciﬁed loss on the underlying fully supervised learning problem. This leads, for 𝜏∈ΔX×2Y encoding the distribution generating samples (𝑋, 𝑆), to the formulation 𝑓∗∈F = arg min 𝑓:X→Y E(𝑋,𝑆)∼𝜏[inf𝑌∈𝑆ℓ( 𝑓(𝑋),𝑌)] . To study this problem, a non-ambiguity assumption is usually made (Cour et al., 2011; Luo and Orabona, 2010; Liu and Dietterich, 2014; Cabannes et al., 2020b, 2021b). This is a very strong assumption to ensure that F is, in essence, a singleton. Highly adequate to this setting, the Laplacian regularization allows relaxing this assumption, assuming that F can be big, but that we can discriminate between function in F by looking for the smoothest one in the sense deﬁned by the Laplacian penalty. Moreover, the loss trick (9.15) allows endowing, in an oﬀ-the-shelf fashion, the recent work of Cabannes et al. (2020b, 2021b) on the partial supervised learning problem with our considerations on Laplacian regularization.

## 9.B Experiments 9.B.1 Low-rank approximation

Cutting computation cost thanks to low-rank approximation, as we did by going from the naive exact empirical risk minimizer ˆ𝑔(9.5) to the smart implementation ˆ𝑔𝑝Algorithm 1, is associated with a trade-oﬀbetween computational versus statistical performance. This trade-oﬀcan be studied theoretically thanks to Theorem

<!-- page: 163 -->

9.B. EXPERIMENTS 161 Classiﬁcation error Regression error small kernel full kernel graph-based 1.5 small kernel full kernel graph-based 0.4 Loss (0-1) Loss (퐿2) 1.0 0.2 0.5 101 102 103 101 102 103 Number of samples Number of samples

[FIGURE: Figure 9.4]

Figure 9.4: Cut in computation costs are not associated with a loss in performance. The estimate ˆ𝑔𝑝Algorithm 1 (in blue), based on low-rank approximation that cut computation cuts performs as well as the exact computation of ˆ𝑔(9.5). (Left) Classiﬁcation error in the setting of Figure 9.3. (Right) Regression error in the same setting. The fact that the error of the graph-based method stalls around one, is due to the amplitude of the estimate being very small, which is coherent with behaviors described in (Nadler et al., 2009).

Trainset Kernelized estimate Graph-based estimate 휕푋 휕푋 휕푋

[FIGURE: Figure 9.5]

Figure 9.5: Setting of Figure 9.3 with 𝑛= 1000. (Left) Training set. We represent a cut of X ⊂R𝑑according to the two ﬁrst coordinates {(𝑥1, 𝑥2) | (𝑥1, 𝑥2, · · · , 𝑥𝑑) ∈X }. We have two Gaussian distributions with unit variance, one centered at 𝑥= (0, 0, · · · 0) and the other one centered at 𝑥= (3, 0, · · · , 0). One of the Gaussian distributions is associated with the blue class, the other one with the orange class. We consider 𝑛= 1000 unlabeled points, represented by small points, colored according to their classes, and 𝑛ℓ= 100 labeled points, represented in color with black edges. (Middle) Reconstruction with our kernelized Laplacian methods. Our method uncovers correctly the structure of the problem, and allows making a quite optimal reconstruction. The optimal decision frontier is illustrated by the gray line 𝜕𝑋. (Right) Reconstruction with graph-Laplacian. The graph-Laplacian diﬀuses information too far away from what it should, leading to many incorrect guesses.

16, which shows that under mild assumptions, considering 𝑝= 𝑛1/2 log(𝑛) does not lead to any loss in performance, in the sense that the convergence rates in 𝑛, the number of samples, are only changed by a constant factor. We show on Figure 9.4 that in the setting of Figure 9.3, our low-rank approximation is not associated with a loss in performance. Actually low-rank approximation can even be beneﬁcial as it tends to lower the risk for overﬁtting as discussed by Rudi et al. (2015).

### 9.B.2 Comparison with graph-based Laplacian

One the main goal of this paper is to make people drop graph-based Laplacian methods and adopt our “kernelized” technique. As such, we would like to discuss in more detail our comparison with graph-based Laplacian. In particular, we will discuss how and why we choose the hyperparameters and the setting of Figure 9.3.

The setting of Figure 9.3 is the one of Figure 9.5, we considered two Gaussian with unit variance and whose centers are at distance 𝛿= 3 of each other. We chose Gaussian distributions as it is a well-understood setting. We chose 𝛿= 3 so that there is a mild overlap between the two distributions. For the bandwidth parameter, we considered 𝜎𝑛= 𝐶𝑛−1 𝑑+4 log(𝑛) as this is known to be the optimal bandwidth for graph Laplacian (Hein et al., 2007). We chose 𝐶= 1 as this leads to 𝜎𝑛of the order of 𝛿. We chose 𝜆= 1 to enforce Laplacian regularization and 𝜇𝑛= 1/𝑛, as this is a classical regularization parameter in RKHS. Furthermore, we did not cross-validate parameters in order to be fair with graph-Laplacian that do not have

<!-- page: 164 -->

$$
푆( ˆΣ+휀)−1 푆★푔휌 푆( ˆ퐿+휀)−1 푆★푔휌
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

[FIGURE: Figure 9.6]

Figure 9.6: Usefulness of Laplacian regularization. We illustrate the reconstruction based on our spectral ﬁltering techniques based on the sole use of the covariance matrix Σ on the left, and on the sole use of the Laplacian matrix 𝐿on the right. We see that the covariance matrix does not capture the geometry of the problem, which contrasts with the use of Laplacian regularization. as many parameters as our kernel method. We compute the error in a transductive setting, retaking the exact problem and algorithm of Zhu et al. (2003). We choose 𝑑= 10, as we know that this is a good dimension parameter in order to illustrate the curse of dimensionality phenomenon without needing too much data.3

### 9.B.3 Usefulness of Laplacian regularization

It is natural to ask about the relevance of Laplacian regularization. To give convergence results, we have used Assumptions 17 and 18, which imply that 𝑔∗belongs to the RKHS H, and we got convergence rates in 𝑛1/2 𝑙 , which is not better than the rates we could get with pure kernel ridge regression. In particular, our

$$
L1/2𝑔 2
$$

algorithm can be split between an unsupervised part that learn the penalty 𝐿2(𝜌X ) and a supervised part, that solve the problem of estimating 𝑔𝜆from few labels (𝑋𝑖,𝑌𝑖) given the penalty associated to L. But the same method can be used for pure kernel ridge regression: unsupervised data could be leveraged to learn the covariance matrix Σ (9.6), and supervised data could be used to get Ŝ★𝑔𝜌to converge toward 𝑆★𝑔𝜌. The same analysis would yield the same type of convergence rates. Yet the parameter 𝜎ℓappearing in Theorem 16 would not be linked with the variance of 𝑌(𝐼+ 𝜆L + 𝜆𝜇𝐾−1)−1𝛿𝑋but with the variance of 𝑌(𝐼+ 𝜇𝐾−1)−1𝛿𝑋. This is a key fact, the geometry of the covariance operator Σ is not supposed to be that relevant to the problem, while the one of 𝐿is. We illustrate this fact on Figure 9.6.

## 9.C Central operators

The paper makes an intensive use of operators. This section aims at providing details and intuitions on those operators, in order to help the reader. In particular, we discuss Assumptions 17 and 18, and we prove the equality in (9.6).

### 9.C.1 The diﬀusion operator

In this subsection, we extend on the diﬀusion operator, and recall its basic properties.

The diﬀusion operator is a well-known operator in the realm of partial diﬀerential equations. Let us assume that 𝜌X admits a smooth density 𝜌X (𝑑𝑥) = 𝑝(𝑥)𝑑𝑥, say 𝑝∈C2(R𝑑) that cancels outside a domain Ω ⊂R𝑑. Then the diﬀusion operator L can be explicitly written, for 𝑔twice diﬀerentiable, as

$$
L𝑔(𝑥) = −Δ𝑔(𝑥) + \frac{1}{𝑝(𝑥) ⟨∇𝑝(𝑥), ∇𝑔(𝑥)⟩.}
$$

3Note that our consistency result Theorem 16 describes a convergence regime that applies to a vast class of problems. Such a regime usually takes place after a certain number of data (depending on the value of the constant 𝐶). Before entering this regime, describing the error of our algorithm would require more precise analysis speciﬁc to each problem instance, eventually involving tools from random matrix theory.

<!-- page: 165 -->

9.C. CENTRAL OPERATORS 163

[TABLE: Table 9.1]

Table 9.1: Notations

| Symbol | Description |
|---|---|
| (𝑋𝑖)𝑖≤𝑛 | 𝑛 samples of input data |
| (𝑌𝑖)𝑖≤𝑛𝑙 | 𝑛𝑙 labels |
| 𝜌 | Distribution of (𝑋,𝑌) |
| 𝑔𝜌 | Function to learn (9.1) |
| 𝜆, 𝜇 | Regularization parameters |
| 𝑔𝜆, 𝑔𝜆,𝜇 | Biased estimates (9.3, 9.4) |
| ˆ𝑔 | Empirical estimate (9.5) |
| ˆ𝑔𝑝 | Empirical estimate with low-rank approximation (Algo. 1) |
| H | Reproducing kernel Hilbert space |
| 𝑘 | Reproducing kernel |
| 𝑆 | Embedding of H in 𝐿2 |
| 𝑆★ | Adjoint of 𝑆, operating from 𝐿2 to H |
| Σ = 𝑆★𝑆 | Covariance operator on H |
| 𝐾= 𝑆𝑆★ | Equivalent of Σ on 𝐿2 |
| L | Diﬀusion operator (a.k.a. Laplacian) |
| 𝐿= 𝑆★L𝑆 | Restriction of the diﬀusion operator to H |
| 𝑔 | Generic element in 𝐿2 |
| 𝜃 | Generic element in H |
| 𝜆𝑖 | Generic eigenvalue |
| 𝑒𝑖 | Generic eigenvector in 𝐿2 |

This follows from the fact that for 𝑓once and 𝑔twice diﬀerentiable, using Stokes theorem,

$$
⟨𝑓, L𝑔⟩𝐿2(𝜌X ) = ⟨∇𝑓, ∇𝑔⟩𝐿2(𝜌X ) = ⟨∇𝑓, 𝑝∇𝑔⟩𝐿2(d𝑥) ∫
= div( 𝑓𝑝∇𝑔) d𝑥−⟨𝑓, div(𝑝∇𝑔)⟩𝐿2(d𝑥) = −⟨𝑓, div(𝑝∇𝑔)⟩𝐿2(d𝑥)
X
𝑓, 𝑝−1 div(𝑝∇𝑔) 𝑓, div ∇𝑔+ 𝑝−1(∇𝑝).∇𝑔
= − 𝐿2(𝜌X ) = − 𝐿2(𝜌X ) .
$$

Note that when the distribution is uniform on Ω, the diﬀusion operator is exactly the opposite of the usual Laplacian operator Δ. As for the Laplacian case, it can be shown that under mild assumption on 𝑝, whose smoothness properties directly translates to the smoothness properties of the boundary of Ω, that the diﬀusion operator L has a compact resolvent (that is, for 𝜆∉spec(L), (L + 𝜆𝐼)−1 is compact). This is a standard result implied by a standard version of the famous Rellich-Kondrachov compactness embedding theorem: 𝐻2(Ω) is compactly injected in 𝐿2(Ω) whenever Ω is a bounded open with 𝐶2-boundaries.

In such a setting, we can consider the eigenvalue decomposition of L−1, that is, (𝜆𝑖, 𝑒𝑖) ∈(R+ × 𝐿2)N, with (𝑒𝑖)𝑖∈N an orthonormal basis of 𝐿2 and (𝑒𝑖)𝑖≤dim ker L generating the null space of L, with the convention 𝜆𝑖= 𝑀for 𝑖≤dim ker L, with 𝑀an abstraction representing +∞, and (𝜆𝑖) decreasing toward zero afterwards. This decomposition reads

$$
∑︁
L−1 = 𝜆𝑖𝑒𝑖⊗𝑒𝑖. (9.16)
𝑖∈N
$$

(9.16)

Note that the fact that all the (𝜆𝑖) are positive, is due to the fact that L−1 is the inverse of a positive self-adjoint operator. As a consequence, the diﬀusion operator has discrete spectrum, and can be written as

$$
∑︁
L = 𝜆−1 𝑖𝑒𝑖⊗𝑒𝑖. (9.17)
𝑖∈N
$$

(9.17)

In such a setting, the kernel-free Tikhonov regularization (9.3) reads

$$
∑︁ D E
𝑔𝜆= 𝑔𝜌, 𝜆1/2 𝐿2 𝜆1/2 𝑖 𝑒𝑖, (9.18)
𝜓(𝜆𝑖) 𝑖 𝑒𝑖
𝑖∈N
$$

(9.18)

with 𝜓: 𝑥→(𝑥+ 𝜆)−1, and the convention 𝑀𝜓(𝑀) = 1.

<!-- page: 166 -->

### 9.C.2 Regularity of the eigenvectors of the diﬀusion operator

In this subsection, we extend on the regularity assumed in Assumption 18.

Introducing the kernel 𝑘and its associated RKHS H is useful when the eigenvectors of L can be well approximated by functions in H. In applications, people tend to go for kernels that are translation-invariant, which implied that the RKHS H is made of smooth functions, could it be analytical functions (for the Gaussian kernel) or functions in 𝐻𝑚(for Sobolev kernels). As a consequence, we should investigate the regularity of those eigenvectors. Indeed, if 𝜌derives from a Gibbs potential, that is 𝜌(d𝑥) = 𝑒−𝑉(𝑥) d𝑥, the eigenvectors of L can be shown to inherit from the smoothness of the potential 𝑉(Pillaud-Vivien, 2020b). For example if 𝑉belongs to 𝐻𝑚, and 𝐻𝑚⊂H, we expect (𝑒𝑖) to belong to H, thus verifying Assumption 18.

Counter-example and beyond Assumption 18. Note that if 𝜌has several connected components of non-empty interiors, the null space of L is made of functions that are constants on each connected component of supp 𝜌X . Those functions are not analytic. In such a setting, the Gaussian kernel is not suﬃcient for Assumption 18 to hold, and one should favor kernel associated with richer functional space such as the Laplace kernel or the neural tangent kernel (Chen and Xu, 2021). However, as illustrated by Figure 9.2, 𝑒𝑖not belonging to H does not mean that 𝑒𝑖can not be well approximated by H. Indeed, it is well known that the approximation power of H for 𝑒𝑖can be measure in the biggest power 𝑝such that 𝑒𝑖∈im 𝐾𝑝(Caponnetto and De Vito, 2006), where 𝐾= 𝑆𝑆∗. Assumption 18 corresponds to 𝑝= 1/2, but it should be seen as a speciﬁc instance of more generic approximation conditions.

Handling constants in RKHS. Finally, note also that many RKHS do not contain constant functions, and therefore might not contain the constant function 𝑒0 (although we are only looking for equality in the support of 𝜌X ), however this speciﬁc point with 𝑒0 can easily be circumvented either by assuming that 𝑔𝜌has zero mean, either by centering the covariance matrices Σ and ˆΣ (Pillaud-Vivien, 2020b). This relates with the usual technique for SVM consisting in adding an unpenalized bias (Steinwart and Christmann, 2008).

### 9.C.3 Low-density separation

In this subsection, we discuss how Assumption 17 relates to the idea of low-density separation.

L1/2𝑔∗

 /∥𝑔∗∥is small. As such, using Courant-Fischer principle, Assumption 17 can be reformulated as 𝑔∗belonging to the space Low-variation intuition. The low-density separation supposes that the variations of 𝑔∗take place in region with low-density, so that

$$
Span {𝑒𝑖}𝑖≤𝑟= arg min F ⊂𝐿2; dim F=𝑟 max_{𝑔∈F} L−1/2𝑔 ∥𝑔∥2 𝐿2 \frac{2}{𝐿2} .
$$

In other terms, Assumption 17 can be restated as 𝑔∗belonging to a ﬁnite dimensional space that minimizes a measure of variation given by the Dirichlet energy.

To tell the story diﬀerently, suppose that we are in a classiﬁcation setting, i.e. 𝑌∈{−1, 1}, and that the supp 𝜌X is connected. Then we know that the null space of L is made of constant functions. Then the ﬁrst eigenvector 𝑒2 of L is a function that is orthogonal to constants. Hence, 𝑒2 is a function that changes its sign and that is “balanced” in the sense that E[𝑒2] = 0 – i.e. if 𝑒2(𝑥) = E𝜇[𝑌| 𝑋= 𝑥] for some measure 𝜇, we have E𝜇[𝑌] = 0, meaning that classes are “balanced”. Moreover, in order to minimize

$$
L1/2𝑒2
$$

, the variations of 𝑒2 should take place in low-density regions of X.

Diﬀusion intuition. Finally, as L is a diﬀusion operator, we also have an interpretation of Assumption 17 in terms of diﬀusion. Consider (𝜆𝑖, 𝑒𝑖) the eigenelements of (9.17). The diﬀusion of 𝑔𝜌according the density 𝜌X can be written as, for 𝑡∈R,

$$
𝑔𝑡= 𝑒−𝑡L𝑔𝜌= \sum_{𝑖∈N} \frac{𝑖}{𝑒−𝑡𝜆−1} 𝑔𝜌, 𝑒𝑖 𝑒𝑖.
$$

<!-- page: 167 -->

9.C. CENTRAL OPERATORS 165 for big 𝑖, and big 𝜆−1 This diﬀusion will cut oﬀthe high frequencies of 𝑔𝜌that corresponds to 𝑖. Indeed, the diﬀerence between the diﬀusion and the original 𝑔𝜌can be measured as

$$
𝑔𝜌, 𝑒𝑖
𝑔𝑡−𝑔𝜌 2 ∑︁ 𝑖 −1)2 2 = ∑︁ 2 + 𝑜(𝑡2𝜆−2
𝐿2 = (𝑒−𝑡𝜆−1 𝑡2𝜆−2
𝑔𝜌, 𝑒𝑖 𝑔𝜌, 𝑒𝑖 𝑖).
𝑖
𝑖∈N 𝑖∈N
$$

Hence, assuming that 𝑔𝜌is supported on a few of the ﬁrst eigenvectors of L, can be rephrased as saying that the diﬀusion of 𝑔𝜌does not modify it too much.

The variance 𝜎ℓ. Theorem 16 shows that the need for labels depends on the variance parameter 𝜎2 ℓ. It is natural to wonder how this parameter relates to the low-density hypothesis. As we discussed, this parameter is linked to the variance of 𝑍= 𝑌(𝐼+ 𝜆L)−1𝛿𝑋. We can separate the variability of this variable due to 𝑋and the variability due to 𝑌

$$
𝑍= 𝑍𝑋+ 𝑍𝑌, with 𝑍𝑋= (𝐼+ 𝜆L)−1𝑔𝜌(𝑋)𝛿𝑋, 𝑍𝑌= (𝐼+ 𝜆L)−1(𝑌−E[𝑌| 𝑋])𝛿𝑋.
$$

As such we see that this variance depends on the structure of the density 𝜌X with the variance of (𝐼+𝜆L)−1𝛿𝑋, and the labeling noise with the variance of (𝑌| 𝑋). The low-density separation does not tell us anything about the level of noise in 𝑌or the diﬀusion structure linked with 𝜌X , but additional hypotheses could be made to characterize those.

### 9.C.4 Kernel operators

In this subsection, we deﬁne formally the operators 𝑆and Σ.

We now turn toward operators linked with the Hilbert space H. Recall that for 𝑘: X →X →R a kernel, H is deﬁned the closure of the span of the elements 𝑘𝑥under the scalar product ⟨𝑘𝑥, 𝑘𝑥′⟩= 𝑘(𝑥, 𝑥′). In particular, ∥𝑘𝑥∥2 H = 𝑘(𝑥, 𝑥). H parametrizes a vast class of functions in RX through the mapping

$$
𝑆: \frac{H}{𝜃} \frac{→}{→} \frac{RX}{(⟨𝑘𝑥, 𝜃⟩)𝑥∈X .}
$$

Under mild assumptions, 𝑆maps H to a space of functions belonging to 𝐿2.

Proposition 65. When 𝑥→𝑘(𝑥, 𝑥) belongs to 𝐿1(𝜌X ), 𝑆is a continuous mapping from H to 𝐿2(𝜌X ). This is particularly the case when 𝜌X has compact support and 𝑘is continuous.

Proof. Consider 𝜃∈H, we have

$$
∫ ∫ ∫
∥𝑆𝜃∥2 𝐿2 = ⟨𝑘𝑥, 𝜃⟩2 𝜌X (d𝑥) ≤ ⟨𝑘𝑥, 𝜃⟩2 H 𝜌X (d𝑥) ≤ ∥𝑘𝑥∥2 H ∥𝜃∥2 H 𝜌X (d𝑥)
∫
X X X
= ∥𝜃∥2 𝑘(𝑥, 𝑥)𝜌X (d𝑥) = ∥𝜃∥2 H ∥𝑥→𝑘(𝑥, 𝑥)∥𝐿1 .
H
X
$$

Moreover, when 𝜌X has compact support and 𝑘is continuous, 𝑘is bounded on the support of 𝜌X therefore 𝑥→𝑘(𝑥, 𝑥) belongs to 𝐿1. □ As a continuous operator from the Hilbert space H to the Hilbert space 𝐿2, 𝑆is naturally associated with many linear structures: in particular its adjoint 𝑆★, but also the self-adjoint operators 𝐾= 𝑆𝑆★and Σ = 𝑆★𝑆.

Proposition 66. The adjoint of 𝑆is deﬁned as

$$
𝑆★: 𝐿2 → H 𝑔 → ∫
X 𝑔(𝑥)𝑘𝑥𝜌X (d𝑥) = E𝑋∼𝜌X [𝑔(𝑋)𝑘𝑋].
$$

To 𝑆is associated the kernel self-adjoint operator on 𝐿2

$$
𝐾:= 𝑆𝑆★: 𝐿2 → 𝐿2 ∫
𝑔 → (𝑥→ X 𝑘(𝑥, 𝑥′)𝑔(𝑥′)𝜌X (d𝑥′)),
$$

as well as the (non-centered) covariance on H, Σ := 𝑆★𝑆= E𝑋∼𝜌X [𝑘𝑋⊗𝑘𝑋].

<!-- page: 168 -->

Proof. We shall prove the equality deﬁning those operators. Consider 𝜃∈H and 𝑔∈𝐿2, we have

$$
𝑆★𝑔, 𝜃 H = ⟨𝑔, 𝑆𝜃⟩𝐿2 = E𝑋∼𝜌X [𝑔(𝑋) ⟨𝑘𝑋, 𝜃⟩H] = E𝑋∼𝜌X [𝑔(𝑋)𝑘𝑋], 𝜃 H .
$$

We also have, for 𝑥∈X,

$$
(𝑆𝑆★𝑔)(𝑥) = 𝑘𝑥, E𝑋∼𝜌X [𝑔(𝑋)𝑘𝑋] H = E𝑋∼𝜌X [𝑔(𝑋) ⟨𝑘𝑥, 𝑘𝑋⟩H] = E𝑋∼𝜌X [𝑔(𝑋)𝑘(𝑋, 𝑥)].
$$

Finally, we have

$$
𝑆★𝑆𝜃= E𝑋∼𝜌X [𝑆𝜃(𝑋)𝑘𝑋] = E𝑋∼𝜌X [⟨𝜃, 𝑘𝑋⟩H 𝑘𝑋] = E𝑋∼𝜌X [𝑘𝑋⊗𝑘𝑋]𝜃.
$$

This provides the last of all the equalities stated above. □ The functional space H. In the main text, we have written everything in terms of 𝜃, highlighting the parametric nature of kernel methods. This made it easier to dissociate the norm on functions derived from H and the one derived from 𝐿2 or 𝐻1. In literature, people tend to keep everything in terms of functions 𝑔𝜃= 𝑆𝜃without even mentioning the dependency in 𝜃. Such a setting consists in considering directly the RKHS H whose scalar product is deﬁned for 𝑔, 𝑔′ ∈(ker 𝐾)⊥by ⟨𝑔, 𝑔′⟩H =

$$
𝑔, 𝐾−1𝑔′ 𝐿2.
$$

### 9.C.5 Derivative operators

In this subsection, we extend on derivatives in RKHS, and we formally deﬁne the operator 𝐿.

As well as evaluation maps can be represented in H, under mild assumptions, derivative evaluation maps can beneﬁt from such a property. Indeed, for 𝑔𝜃= 𝑆𝜃, 𝑥∈X and 𝑢∈BX (0, 1) a unit vector, we have

$$
𝑔𝜃(𝑥+ 𝑡𝑢) −𝑔𝜃(𝑥) ⟨𝜃, 𝑘𝑥+𝑡𝑢⟩H −⟨𝑔, 𝑘𝑥⟩H 𝜃, 𝑘𝑥+𝑡𝑢−𝑘𝑥
𝜕𝑢𝑔𝜃(𝑥) = lim 𝑡 = lim 𝑡 = lim
𝑡→0 𝑡→0 𝑡→0 𝑡
H
$$

As a linear combination of elements in H, the diﬀerence quotient evaluation map 𝑡−1(𝑘𝑥+𝑡𝑢−𝑘𝑥) belongs to H and has a norm

$$
2 = 𝑘(𝑥+ 𝑡𝑢, 𝑥+ 𝑡𝑢) −2𝑘(𝑥+ 𝑡𝑢, 𝑥) + 𝑘(𝑥, 𝑥)
𝑘𝑥+𝑡𝑢−𝑘𝑥
𝑡2 .
𝑡
H
$$

In order for the limit when 𝑡goes to zero to belong to H, we see the importance of 𝑘to be twice diﬀerentiable. This limit 𝜕𝑢𝑘𝑥, whose existence is proven formally by Zhou (2008), provides a derivative evaluation map in the sense that

$$
𝜕𝑢𝑔𝜃(𝑥) = ⟨𝜃, 𝜕𝑢𝑘𝑥⟩H . 𝜕𝑖𝑘𝑥, 𝜕𝑗𝑘𝑥′
$$

From this equality, we derive that 𝜕1𝑖𝑘(𝑥, 𝑥′) = ⟨𝑘𝑥′, 𝜕𝑖𝑘𝑥⟩, and recursively that = 𝜕1𝑖𝜕2𝑗𝑘(𝑥, 𝑥′). Similarly to the operator 𝑆, we can introduce the operators 𝑍𝑖for 𝑖∈[1, 𝑑], deﬁned as

$$
𝑍𝑖: \frac{H}{𝜃} \frac{→}{→} \frac{RX}{(⟨𝜕𝑖𝑘𝑥, 𝜃⟩H)𝑖≤𝑑.}
$$

Once again, under mild assumptions, im 𝑍𝑖inherit from a Hilbertian structure.

Proposition 67. When 𝑥→𝜕1𝑖𝜕2𝑖𝑘(𝑥, 𝑥) belongs to 𝐿1(𝜌X ), 𝑍𝑖is a continuous mapping from H to 𝐿2(𝜌X ). This is particularly the case when 𝜌X has compact support and 𝑘is twice diﬀerentiable with continuous derivatives.

Proof. Consider 𝜃∈H, similarly to before, we have

$$
∫ ∫
𝑥→𝜕1,𝑖𝜕2,𝑖𝑘(𝑥, 𝑥)
∥𝑍𝜃∥2 𝐿2 = ⟨𝜕𝑖𝑘𝑥, 𝜃⟩2 𝜌X (d𝑥) ≤∥𝜃∥2 ∥𝜕𝑖𝑘𝑥∥2 H 𝜌X (d𝑥) = ∥𝜃∥2
𝐿1 .
H H
X X
$$

Moreover, when 𝜌X has compact support and 𝜕1,𝑖𝜕2,𝑖𝑘is continuous, 𝜕1,𝑖𝜕2,𝑖𝑘is bounded on the support of 𝜌X therefore 𝑥→𝜕1,𝑖𝜕2,𝑖𝑘belongs to 𝐿1. □ Among the linear operators that can be built from 𝑍𝑖, in the theoretical part of this paper, we are mainly interested in 𝑍★ 𝑖𝑍𝑖. In the empirical part however, we might be interested in 𝑍𝑖𝑍★ 𝑗as well as 𝑍𝑖𝑆★as it appears in Algorithm 1 (where the notation 𝑍𝑛there has to be understood as the empirical version of 𝑍= [𝑍1; · · · ; 𝑍𝑑]).

<!-- page: 169 -->

9.C. CENTRAL OPERATORS 167 Proposition 68. The Dirichlet energy on H can be represented through the operator

$$
𝑑 ∑︁ 𝑑 ∑︁
𝑆★L𝑆= 𝑍★ 𝑖𝑍𝑖= E𝑋∼𝜌X [𝜕𝑖𝑘𝑋⊗𝜕𝑖𝑘𝑋].
𝑖=1 𝑖=1
$$

Proof. Let 𝜃∈H and 𝑔𝜃= 𝑆𝜃, we have

$$
∥∇𝑔𝜃(𝑋)∥2 𝑑 ∑︁ (𝜕𝑖𝑔𝜃(𝑋))2 
⟨𝑔𝜃, L𝑔𝜃⟩𝐿2 = 𝜃, 𝑆★L𝑆𝜃 H = E𝑋∼𝜌X = E𝑋∼𝜌X
𝑖=1 * +
𝑑 ∑︁ 𝑑 ∑︁ 𝑑 ∑︁
= E𝑋∼𝜌X ⟨𝜕𝑖𝑘𝑋, 𝜃⟩2 = ∥𝑍𝑖𝜃∥2 𝐿2 = 𝑍★
𝜃, 𝑖𝑍𝑖𝜃
H
𝑖=1 𝑖=1 * 𝑖=1 H +
𝑑 ∑︁ 𝑑 ∑︁
= E𝑋∼𝜌X [⟨𝜃, (𝜕𝑖𝑘𝑋⊗𝜕𝑖𝑘𝑋)𝜃⟩H] = 𝜃, E𝑋∼𝜌X [𝜕𝑖𝑘𝑋⊗𝜕𝑖𝑘𝑋] 𝜃 .
𝑖=1 𝑖=1 H
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Since the three operators are self-adjoint, and they all represent the same quadratic form, they are equals. □ Relation between Σ and 𝐿

### 9.C.6

In this subsection, we discuss the relation between Σ and 𝐿and show that we can expect the existence of 𝑎∈(1 −2/𝑑, 1] and 𝑐> 0 such that 𝐿⪯𝑐Σ𝑎.

Informal capacity considerations. We want to compare Σ and 𝐿, as 𝐿⪯𝑐Σ𝑎with the biggest 𝑎possible. This depends on how fast the eigenvalues are decreasing, which is linked to the entropy numbers of those two compact operators. Those entropy numbers are linked with the capacity of the functional spaces 𝑔∈𝐿2 

𝐾−1/2𝑔

$$
and 𝑔∈𝐿2 

𝐾−1/2L−1/2𝑔
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

. The ﬁrst space is the reproducing kernel Hilbert space linked with 𝑘, the second space is, roughly speaking, a space of functions whose integral belongs to the ﬁrst space. As such, if the ﬁrst space is H𝑚, the second is H𝑚−1, and we can consider 𝑎= (𝑚−1)/𝑚. Because we are considering kernels, we have 𝑚> 𝑑/2 (this to make sure that the evaluation functionals 𝐿𝑋: 𝑓→𝑓(𝑥) are continuous), so that 𝑎> 1 −2/𝑑. Without trying to make those “algebraic” considerations more formal, we will give an example on the torus.

$$
𝐿2 < ∞ 𝐿2 < ∞
$$

Translation-invariant kernel and Fourier transform. Consider 𝐿2([0, 1]𝑑, d𝑥) the space of periodic functions in dimension 𝑑, square integrable against the Lebesgue measure on [0, 1]𝑑. For simplicity, we will suppose that 𝜌X is the Lebesgue measure on [0, 1]𝑑. Consider a translation invariant kernel 𝑘(𝑥, 𝑦) = 𝑞(𝑥−𝑦) for 𝑞: R𝑑→R that is one periodic.

In this setting, the operator 𝐾, operating on 𝐿2, is the convolution by 𝑞, that is

$$
𝐾: 𝐿2 → 𝐿2 𝑔 → 𝑞∗𝑔, hence c 𝐾𝑔= ˆ𝑞ˆ𝑔.
$$

Where we have used the fact that convolutions can be represented by a product in the Fourier domain. Note that, from Böchner theorem, we know that 𝑘being positive deﬁnite implies that the Fourier transform of 𝑞 exists and is not negative. Let us deﬁne the Fourier coeﬃcient and the inverse Fourier transform as

$$
∫ ∑︁
∀𝜔∈Z𝑑, ˆ𝑔(𝜔) = [0,1]𝑑𝑔(𝑥)𝑒−2𝑖𝜋𝜔⊤𝑥d𝑥, and ∀𝑥∈[0, 1]𝑑, 𝑔(𝑥) = 𝑒2𝑖𝜋𝜔⊤𝑥ˆ𝑔(𝜔).
𝜔∈Z𝑑
$$

𝐾being a convolution operator, it is diagonalizable with eigenelements ( ˆ𝑞(𝜔), 𝑥→𝑒2𝑖𝜋𝜔⊤𝑥)𝜔∈Z𝑑. From this, we can make explicit many of our abstract operators. First of all, using Perceval’s theorem,

$$
∥𝑔∥2 H = 𝑔, 𝐾−1𝑔 𝐿2 = \sum_{𝜔∈Z𝑑} \frac{| ˆ𝑔(𝜔)|2}{ˆ𝑞(𝜔) .}
$$

<!-- page: 170 -->

$$
√︁
$$

Hence, we can parametrize H with (𝜃𝜔)𝜔∈Z𝑑∈CZ𝑑and the ℓ2-metric, where 𝜃𝜔= ˆ𝑔(𝜔)/

$$
ˆ𝑞(𝜔) and
∑︁ 𝑒2𝑖𝜋𝜔⊤𝑥√︁
(𝑆𝜃)(𝑥) = 𝑔𝜃(𝑥) = ˆ𝑞(𝜔)𝜃𝜔.
𝜔∈Z𝑑
$$

Note that this is not the usual parametrization of H by elements 𝜃∈H as (CZ𝑑, ℓ2) is not a space of functions. However, such a parametrization of H does not change any of the precedent algebraic considerations on the operators 𝑆, Σ, 𝐾, and 𝐿.

Diﬀusion operator and Fourier transform. As well as convolution operators are well represented in the Fourier domain, derivation operators are. Indeed, when 𝑔is regular, we have

$$
L1/2𝑔 𝑑 ∑︁ 𝜕𝑗𝑔 2 𝑑 ∑︁ ∑︁
2
𝐿2 = ∥∇𝑔∥2 𝐿2 = 𝐿2 = 𝜔2 𝑗| ˆ𝑔(𝜔)|2 .
𝑗=1 𝑗=1 𝜔∈Z𝑑
$$

As a consequence, using the expression of 𝑆𝜃, we have

$$
∑︁ ∑︁ 𝑑 ∑︁
Σ𝜃= ˆ𝑞(𝜔)𝜃𝜔, while 𝐿𝜃= ∥𝜔∥2 2 ˆ𝑞(𝜔)𝜃𝜔, where ∥𝜔∥2 2 = 𝜔2
𝑖.
𝜔∈Z𝑑 𝜔∈Z𝑑 𝑗=1
$$

In this setting, the eigenelements of Σ are ( ˆ𝑞(𝜔), 𝛿𝜔)𝜔∈Z𝑑while the one of 𝐿are (∥𝜔∥2

$$
2 ˆ𝑞(𝜔), 𝛿𝜔)𝜔∈Z𝑑.
$$

Eigenvalue decay comparison. Hence, having 𝐿⪯𝑐Σ𝑎is equivalent to having ∥𝜔∥2 2 ˆ𝑞(𝜔) ≤𝑐ˆ𝑞(𝜔)𝑎. Now suppose that the decay of ˆ𝑞is governed by

$$
𝑐1(1 + 𝜎−1 ∥𝜔∥2 2)−𝑚≤ˆ𝑞(𝜔) ≤𝑐2(1 + 𝜎−1 ∥𝜔∥2 2)−𝑚,
$$

for two constants 𝑐1, 𝑐2 > 0. In particular, this is veriﬁed for Matérn kernels, corresponding to the fractional Sobolev space 𝐻𝑚, and for the Laplace kernel with 𝑚= (𝑑+1)/2, which reads 𝑘(𝑥, 𝑦) = exp(−𝜎−1 ∥𝑥−𝑦∥). The Gaussian kernel could be seen as 𝑚= +∞as it has exponential decay. With such a decay we have, assuming without restrictions that we are in one dimension

$$
𝜔2 ˆ𝑞(𝜔) ≤𝑐2𝜔2(1 + 𝜎−1𝜔2)−𝑚≤𝑐2𝜎(1 + 𝜎−1𝜔2)−(𝑚−1) ≤𝑐 𝑚 𝑚−1 1 𝑐2𝜎ˆ𝑞(𝜔) 𝑚−1
𝑚.
$$

𝑚 𝑚−1 1 𝑐2𝜎and 𝑎= (𝑚−1)/𝑚. Assuming that 𝑞is square-integrable, so is ˆ𝑞, which implies that 2𝑚> 𝑑. As a consequence, we do have 𝑎> 1 −2/𝑑. Note that this reasoning could be extended to the case where 𝜌X has a density against the Lebesgue measure, that is bounded above and below away from zero.

In other terms, we can consider 𝑐= 𝑐

## 9.D Spectral decomposition

In this section, we recall facts on spectral regularization, before proving Proposition 64 and extending it to the case 𝜇= 0.

### 9.D.1 Generalized singular value with matrices

Generalized singular value decomposition. Let 𝐴∈R𝑚1×𝑛and 𝐵∈R𝑚2×𝑛be two matrices. There exists 𝑈∈R𝑚1×𝑚1, 𝑉∈R𝑚2×𝑚2 two orthogonal matrices, 𝑐∈R𝑚1×𝑟and 𝑠∈R𝑚2×𝑟two 1-diagonal matrices such that 𝑐⊤𝑐+ 𝑠⊤𝑠= 𝐼𝑟, and 𝐻∈R𝑛×𝑟a non-singular matrix such that

$$
𝐴= 𝑈𝑐𝐻−1, 𝐵= 𝑉𝑠𝐻−1.
$$

To be more precise 𝑐is such that only entries 𝑐𝑖𝑖= cos(𝜃𝑖) for 𝑖< min(𝑟, 𝑚2) are non-zeros and 𝑠such that only entries 𝑠𝑚1−𝑖,𝑟−𝑖= sin(𝜃𝑟−𝑖) for 𝑖< min(𝑟, 𝑚1) are non-zeros, with 𝜃𝑖∈[−𝜋/2, 𝜋/2] some angle. Here, 𝑐stands for cosine, 𝑠for sinus and 𝑟for rank.

<!-- page: 171 -->

9.D. SPECTRAL DECOMPOSITION 169 Link with generalized eigenvalue problem. As well as the singular value of 𝐴is linked with the eigenvalue of 𝐴⊤𝐴, the generalized singular value decomposition of [𝐴; 𝐵] is linked with the generalized eigenvalue problem linked with (𝐴⊤𝐴, 𝐵⊤𝐵). Indeed, we have

$$
𝐴⊤𝐴= 𝐻−⊤𝑐⊤𝑐𝐻−1, 𝐵⊤𝐵= 𝐻−⊤𝑠⊤𝑠𝐻−1.
$$

In particular, with (𝑒𝑖) the canonical basis of R𝑟, and ℎ𝑖the 𝑖-th column of 𝐻, we get

$$
𝐻⊤𝐴⊤𝐴ℎ𝑖= cos(𝜃𝑖)2𝑒𝑖= tan(𝜃𝑖)−2 sin(𝜃𝑖)2𝑒𝑖= tan(𝜃𝑖)−2𝐻⊤𝐵⊤𝐵ℎ𝑖.
$$

From which we deduce that, since im 𝐴∪im 𝐵⊂im 𝐻⊤,

$$
𝐴⊤𝐴ℎ𝑖= tan(𝜃𝑖)−2𝐵⊤𝐵ℎ𝑖, ℎ⊤ 𝑗𝐵⊤𝐵ℎ𝑖= sin(𝜃𝑖)21𝑖=𝑗.
$$

So if we denote by 𝑓𝑖= |sin(𝜃𝑖)|−1 ℎ𝑖and 𝜆𝑖= tan(𝜃𝑖)−2, assuming 𝜆𝑖≠0 for all 𝑖≤𝑟(which corresponds to ker 𝐵⊂ker 𝐴), (𝜆𝑖)𝑖≤𝑟, ( 𝑓𝑖)𝑖≤𝑟provide the generalized eigenvalue decomposition of (𝐴⊤𝐴, 𝐵⊤𝐵) in the sense that

$$
𝐴⊤𝐴𝑓𝑖= 𝜆𝑖𝐵⊤𝐵𝑓𝑖, 𝑓⊤ 𝑗𝐵⊤𝐵𝑓𝑖= 1𝑖=𝑗, 𝑓⊤ 𝑗𝐴⊤𝐴𝑓𝑖= 𝜆𝑖1𝑖=𝑗.
$$

### 9.D.2 Tikhonov regularization

Deﬁne the Tikhonov regularization

$$
\underset{𝑥∈R𝑛}{\arg\min}\, ∥𝐴𝑥−𝑏∥2 + 𝜆∥𝐵𝑥∥2 .
$$

When this problem is well-deﬁned, the solution is deﬁned as

$$
𝑥𝜆= (𝐴⊤𝐴+ 𝜆𝐵⊤𝐵)†𝐴⊤𝑏.
$$

With the generalized singular value decomposition of 𝐴and 𝐵, we have

$$
𝐴⊤𝐴+ 𝜆𝐵⊤𝐵= 𝐻−⊤𝛾𝜆𝐻−1, with 𝛾𝜆= 𝑐⊤𝑐+ 𝜆𝑠⊤𝑠.
$$

Using the fact that 𝐴⊤𝑏= 𝐻−⊤𝑐⊤𝑈⊤𝑏, we get

$$
𝑟∑︁ !
cos(𝜃𝑖) cos(𝜃𝑖)2 + 𝜆sin(𝜃𝑖)2 ℎ𝑖⊗𝑢𝑖
𝑥𝜆= 𝐻𝛾−1 𝜆𝑐⊤𝑈⊤𝑏= 𝑏.
𝑖=1
$$

Now, we would like to replace 𝑐𝑖𝑖, 𝑠𝑖𝑖, ℎ𝑖and 𝑢𝑖with quantities that depend on 𝜆𝑖, 𝑓𝑖and 𝐴. To do so recall that 𝐴𝐻= 𝑈𝑐, therefore cos(𝜃𝑖)𝑢𝑖= 𝐴ℎ𝑖, and recall that ℎ𝑖= sin(𝜃𝑖) 𝑓𝑖and 𝜆𝑖= cos(𝜃𝑖)2/sin(𝜃𝑖)2. Inputting this equality in the last expression of 𝑥𝜆we get

$$
𝑟∑︁ ! 𝑟∑︁ !
sin(𝜃𝑖)2 1 𝜆𝑖+ 𝜆𝑓𝑖⊗𝐴𝑓𝑖
𝑥𝜆= cos(𝜃𝑖)2 + 𝜆sin(𝜃𝑖)2 𝑓𝑖⊗𝐴𝑓𝑖 𝑏= 𝑏.
𝑖=1 𝑖=1
$$

Finally,

$$
𝑟∑︁
𝜓(𝜆𝑖) ⟨𝐴𝑓𝑖, 𝑏⟩𝐴𝑓𝑖, where 𝜓(𝑥) = 1 𝑥+ 𝜆.
𝑏𝜆= 𝐴𝑥𝜆=
𝑖=1
$$

### 9.D.3 Extension to operators

To end the proof of Proposition 64, we should prove that we can apply the generalized eigenvalue decomposition to operators. We will only prove that it is possible for (Σ, 𝐿+ 𝜇) based on simple considerations.

Proposition 69. When 𝑘is continuous and supp 𝜌X is bounded, Σ is a compact operator.

Proof. We have Σ = E[𝑘𝑋⊗𝑘𝑋] and ∥𝑘𝑥∥= 𝑘(𝑥, 𝑥). Since 𝑘is continuous and supp 𝜌X is compact, for 𝑥∈supp 𝜌X , 𝑘(𝑥, 𝑥) is bounded. Hence, Σ is a trace class and compact operator. □

<!-- page: 172 -->

Proposition 70. When 𝑘is twice diﬀerentiable with continuous derivative, and supp 𝜌X is compact, 𝐿is a compact operator. As a consequence, 𝐿has a compact spectrum, and has a pseudo-inverse that we will denote, with a slight abuse of notation, by 𝐿−1.

Proof. The proof is similar to the one showing that Σ is compact, based on the fact that 𝐿= Í𝑑 𝑖=1 E[𝜕𝑖𝑘𝑋⊗ 𝜕𝑖𝑘𝑋], and ∥𝜕𝑖𝑘𝑋∥2 = 𝜕1𝑖𝜕2𝑖𝑘(𝑥, 𝑥). □ Proposition 71. When Σ is compact, for all 𝜇> 0, (𝐿+ 𝜇)−1/2Σ(𝐿+ 𝜇)−1/2 is a compact operator.

Proof. The proof is straightforward

$$
(𝐿+ 𝜇)−1
Tr((𝐿+ 𝜇)−1/2Σ(𝐿+ 𝜇)−1/2) = Tr(Σ(𝐿+ 𝜇)−1) ≤ op Tr(Σ) ≤𝜇−1 Tr(Σ) < +∞.
$$

Therefore, the operator is trace class, hence compact. □ Proposition 72. For any 𝜇> 0, the generalized eigenvalue decomposition of (Σ, 𝐿+ 𝜇) as deﬁned in Proposition 64 exists.

Proof. Using the spectral theorem, since (𝐿+ 𝜇)−1/2Σ(𝐿+ 𝜇)−1/2 is positive self-adjoint compact operator, there exists (𝜉𝑖) a basis of H and (𝜆𝑖) ∈R+ a decreasing sequence (note that ker(𝐿+ 𝜇) = ker Σ = {0}), such that

$$
(𝐿+ 𝜇)−1/2Σ(𝐿+ 𝜇)−1/2 = \sum_{𝑖∈N} 𝜆𝑖𝜉𝑖⊗𝜉𝑖.
$$

Taking 𝜃𝑖= (𝐿+ 𝜇)−1/2𝜉𝑖, we get Σ𝜃𝑖= 𝜆𝑖𝐿𝜃𝑖. Because (𝜉𝑖) generates H, and (𝐿+ 𝜇)−1/2 is bĳective (since 𝐿is compact, (𝐿+ 𝜇)−1 is coercive), ((𝐿+ 𝜇)−1/2𝜉𝑖) generates H. □ Proposition 64 follows from prior discussion on Tikhonov regularization extended to inﬁnite summations.

$$
The case 𝜇= 0
$$

### 9.D.4

When 𝜇= 0, (9.7) should be seen as the rewriting of (9.18) based on the RKHS G = im 𝑆. This can only be done when the eigenvectors of L appearing in (9.17) belongs to G = im 𝑆= im 𝐾1/2, which is exactly what Assumption 18 provides. In such a setting, we can ﬁnd (𝜃𝑖) ∈HN to write 𝜆1/2 𝑖 𝑒𝑖= 𝑆𝜃𝑖as soon as 𝜆𝑖≠0 (write 𝑀𝑒𝑖= 𝑆𝜃𝑖for 𝑀an abstraction representing +∞when 𝜆𝑖= 0, handling the potential fact that ker 𝐵⊄ker 𝐴), we get 𝜃𝑖𝑆∗𝑆𝜃𝑗= 𝜆𝑖1𝑖=𝑗, and 𝐿𝜃𝑖= 𝜆−1 𝑖Σ𝜃𝑖, and we can extend Proposition 64 to the case 𝜇= 0, with

$$
∑︁
𝑔𝜆= 𝜓(𝜆𝑖) 𝑆★𝑔𝜌, 𝜃𝑖 𝑆𝜃𝑖, (9.19)
𝑖∈N
$$

(9.19)

where we handle the null space of L with the equality 𝑀𝜓(𝑀) = 1, veriﬁed by 𝑀our abstraction representing +∞, so that 𝜓(𝑀)

$$
𝑆★𝑔𝜌, 𝜃𝑖 𝑆𝜃𝑖= 𝑔𝜌, 𝑒𝑖 𝑒𝑖as soon as 𝜆𝑖= 0.
$$

Beyond Assumption 18. Assumption 18 could be made generic by considering the biggest (𝑝𝑖) ∈RN + such that 𝐾−𝑝𝑖𝑒𝑖belongs to 𝐿2, and rewriting (9.19) under the form 𝑔𝜆= Í 𝑆0𝐾𝑝𝑖𝜃𝑖, with 𝜃𝑖= 𝜆−1/2

$$
𝑖∈N 𝜓(𝜆𝑖) (𝑆0𝐾𝑝𝑖)★𝑔𝜌, 𝜃𝑖
$$

0 𝐾−𝑝𝑖𝜃𝑖and 𝑆0 = 𝐾−1/2𝑆the isomorphism between H and 𝐿2 (assuming that 𝑆is dense in 𝐿2). Such an assumption would describe all situations from no assumption (𝑝𝑖= 0 for all 𝑖), Assumption 18 (𝑝𝑖= 1/2 for all 𝑖) to even more optimistic assumptions (𝑝𝑖≥1 for all 𝑖).

$$
𝑖 𝑆−1
$$

## 9.E Consistency analysis

This section is devoted to the proof of Theorem 16. The proof is based on (9.7) and (9.19), and splits the error of

$$
𝑔𝜌−ˆ𝑔𝑝 2
$$

𝐿2 into several components linked with how well we approximate 𝑆★𝑔𝜌, and how well we approximate the eigenvalue decomposition (𝜆𝑖, 𝜃𝑖) of (Σ, 𝐿).

<!-- page: 173 -->

9.E. CONSISTENCY ANALYSIS 171

### 9.E.1 Sketch and understanding of the proof

In this subsection, we explain how the proofs work for consistency theorems such as Theorem 16.

Let us deﬁne the mapping 𝐺: H × C →𝐿2 with C the set of pairs of self-adjoint operators on H that admit a generalized eigenvalue decomposition, as

$$
∑︁
𝐺(𝜃, (𝐴, 𝐵)) = 𝜓(𝜆𝑖) ⟨𝜃, 𝜃𝑖⟩𝑆𝜃𝑖 with (𝜆𝑖, 𝜃𝑖) ∈GEVD(𝐴, 𝐵). (9.20)
𝑖∈N
$$

(9.20)

𝐺(𝜃, (𝐴, 𝐵)) ∈𝐿2 corresponds to writing 𝜃∈H in the basis associated with the generalized eigenvalue decomposition (GEVD) of (𝐴, 𝐵).

Proposition 73. Under Assumptions 17 and 18, and with 𝜓deﬁned in Theorem 16

$$
𝑔𝜆= 𝐺(𝑆★𝑔𝜌, (Σ, 𝐿)), and ˆ𝑔𝑝= 𝐺( 𝑆★𝑔𝜌, (𝑃ˆΣ𝑃, 𝑃ˆ𝐿𝑃+ 𝜇𝑃)),
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑃the projection matrix from H to Span

$$
𝑘𝑋𝑖 𝑖≤𝑝.
$$

Proof. This is a direct application of Assumptions 17, 18, (9.19) and Algorithm 1. □ The main point of the proof is to relate 𝑔𝜌to ˆ𝑔𝑝. To do so, we will use several functions in 𝐿2 generated by 𝐺. We detail our steps in Table 9.2. Table 9.2 gives a ﬁrst answer to the two questions asked in the opening of Section 9.5. The number of unlabeled data controls the convergence of the operators (𝑃ˆΣ𝑃, 𝑃ˆ𝐿𝑃+ 𝜇𝑃) toward (Σ, 𝐿+ 𝜇). The number of labeled data controls the convergence of the vector Ŝ★𝑔𝜌toward 𝑆★𝑔𝜌. Priors on the structure of the problem, such as source and approximation conditions, control the convergence of the bias estimate 𝑔𝜆,𝜇toward 𝑔𝜌. Furthermore, a more precise study reveals that the concentration of operators are related to eﬃcient dimension (Caponnetto and De Vito, 2006) and are accelerated by capacity assumptions on the functional space whose norm is ∥𝑔∥=

$$
(L + 𝐾−1)1/2𝑔
$$

𝐿2, and that the concentration of the vector Ŝ★𝑔𝜌is accelerated by assumptions on moments of the variable 𝑌(𝐼+ 𝜆L)−1𝛿𝑋(inheriting randomness from (𝑋,𝑌) ∼𝜌).

[TABLE: Table 9.2]

Table 9.2: Steps in the consistency analysis

| Estimate | Vector | Property of convergence | Basis |
|---|---|---|---|
| ˆ𝑔𝑝 | Ŝ★𝑔𝜌 | | (𝑃 ˆΣ𝑃, 𝑃 ˆ𝐿𝑃+ 𝜇𝑃) |
| ↓ Low-rank approx. (Rudi et al., 2015) | | | |
| ˆ𝑔 | Ŝ★𝑔𝜌 | | ( ˆΣ, ˆ𝐿+ 𝜇) |
| ↓ Operator concentration (Minsker, 2017) | | | |
| 𝑔𝑛ℓ | Ŝ★𝑔𝜌 | | (Σ, 𝐿+ 𝜇) |
| ↓ Vector concentration (Yurinskii, 1970) | | | |
| 𝑔𝜆,𝜇 | 𝑆★𝑔𝜌 | | (Σ, 𝐿+ 𝜇) |
| ↓ Source condition (Lin et al., 2020) | | | |
| 𝑔𝜆 | 𝑆★𝑔𝜌 | | (Σ, 𝐿) |
| ↓ Source condition (Caponnetto and De Vito, 2006) | | | |
| 𝑔𝜌 | | | |

<!-- page: 174 -->

Control of biases. We begin our study in a downward fashion regarding Table 9.2. Indeed, for Tikhonov regularization (9.3), we can show that for 𝑞∈[0, 1],

$$
𝑔𝜆−𝑔𝜌 𝐿2 ≤𝜆𝑞

L𝑞𝑔𝜌 𝐿2 .
$$

Meaning that if we have the source condition 𝑔𝜌∈im L𝑞(which is a condition on how fast ( )𝑖∈N decreases compared to (𝜆𝑖)𝑖∈N for (𝜆𝑖, 𝑒𝑖) the eigenvalue decomposition of L−1), the rates of convergence of this term when 𝑛goes to inﬁnity is controlled by the regularization scheme 𝜆𝑞

$$
𝑔𝜌, 𝑒𝑖
$$

𝑛. Similarly to the kernel-free bias above, for (𝑞𝑖) ∈(0, 1)N, we can have

$$
∑︁ 𝜆𝑖 𝜆+ 𝜆𝑖 2
𝑔𝜆,𝜇−𝑔𝜆 2 2 ∥𝐾−𝑞𝑖𝑒𝑖∥2
𝐿2 ≤2 𝜆2𝑞𝑖𝜇2𝑞𝑖 𝑒𝑖, 𝑔𝜌 𝐿2 .
𝑖∈N
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This shows explicitly the usefulness of controlling at the same time how 𝑔𝜌is supported on the eigenspaces of L and how the eigenvectors are well approximated by the RKHS H, which can be read in the value of (𝑞𝑖) such that all 𝑒𝑖∈im 𝐾𝑞𝑖.

$$
Í𝑛ℓ
$$

Vector concentration. Let us now switch to concentration of Ŝ★𝑔𝜌= 𝑛−1

$$
𝑔𝑛ℓ−𝑔𝜆,𝜇 2 𝑖=1 𝑌𝑖𝑘𝑋𝑖toward 𝑆★𝑔𝜌=
ℓ
$$

E(𝑋,𝑌)∼𝜌[𝑌𝑘𝑋], it will allow controlling 𝐿2 with the notations appearing in Table 9.2. Note how this convergence should be measured in terms of the reconstruction error

$$
\sum_{𝑖∈N} 𝜓(𝜆𝑖,𝜇) D \frac{𝑆★𝑔𝜌− }{𝑆★𝑔𝜌, 𝜃𝑖,𝜇} E 𝑆𝜃𝑖,𝜇 𝐿2 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This error might behave in a much better fashion than the 𝐿2 error between 𝑆𝑆★𝑔𝜌and 𝑆Ŝ★𝑔𝜌. In particular, on Figure 9.1, we can consider 𝜓(𝜆𝑖,𝜇) = 0 for 𝑖> 4, and we might have = 𝑌1𝑥∈𝐶𝑖, for 𝑖≤4 and (𝑋,𝑌) ∈X × Y, where 𝐶𝑖is the 𝑖-th innermost circle. In this setting, when all four (𝑌| 𝑋∈𝐶𝑖) are deterministic, we only need one labeled point per circle to clear the reconstruction error. Based on concentration results in Hilbert space, when |𝑌| is bounded by a constant 𝑐Y, and 𝑥→𝑘(𝑥, 𝑥) by a constant 𝜅2, we have, with D𝑛ℓ∼𝜌⊗𝑛ℓthe dataset generating the labeled data

$$
𝑌𝑘𝑋, 𝜃𝑖,𝜇
h

𝑔𝑛ℓ−𝑔𝜆,𝜇 2 i
ℓ(𝜇𝜆𝑛ℓ)−1 + 4
ED𝑛ℓ ≤2𝜎2 9𝑐2 Y𝜅2(𝜇𝜆𝑛2 ℓ)−1.
𝐿2
$$

where 𝜎2 Y Tr(Σ) is a variance parameter to relate to the variance of 𝑌(𝐼+ 𝜆L)−1𝛿𝑋(where the randomness is inherited from (𝑋,𝑌) ∼𝜌). The fact that the need for labeled data depends on the variance of (𝑋,𝑌) after being diﬀused through L is coherent with the results obtained by Lelarge and Miolane (2019) in the speciﬁc case of a mixture of two Gaussian.

$$
ℓ≤𝑐2
$$

Basis concentration. We are left with the comparison of 𝑔𝑛ℓ, which is the ﬁltering of Ŝ★𝑔𝜌with the operators (Σ, 𝐿+ 𝜇), and ˆ𝑔𝑝, which is the ﬁltering of the same vector with the operators (𝑃ˆΣ𝑃, 𝑃ˆ𝐿𝑃+ 𝜇𝑃). As the number of samples grows toward inﬁnity, we know that (𝑃ˆΣ𝑃, 𝑃ˆ𝐿𝑃+ 𝜇𝑃) will converge in operator norm toward (Σ, 𝐿+ 𝜇). Yet, how to leverage this property to quantify the convergence of ˆ𝑔𝑝toward 𝑔𝑛ℓ? Let us write (𝜆𝑖, 𝜃𝑖) = GEVD(Σ, 𝐿+ 𝜇), and (𝜆′

$$
𝑖, 𝜃′ 𝑖) = GEVD(𝑃ˆΣ𝑃, 𝑃ˆ𝐿𝑃+ 𝜇𝑃), we have
ˆ𝑔𝑝−𝑔𝑛ℓ ∑︁
with ˆ𝜃𝜌= 𝑆★𝑔𝜌.
𝐿2 = 𝜃𝑖, ˆ𝜃𝜌 𝑆𝜃𝑖−𝜓(𝜆′ 𝜃′ 𝑖, ˆ𝜃𝜌 𝑆𝜃′
𝜓(𝜆𝑖) 𝑖)
𝑖
𝑖∈N
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The generic study of this quantity requires controlling eigenspaces one by one. Note that we expect convergence of eigenspaces to depend on gaps between eigenvalues. However, when considering Tikhonov regularization, this quantity can be written under a simpler form. In particular, the concentration of operators is controlled, up to few leftovers, through the quantity

$$
(Σ + 𝜆𝐿+ 𝜇𝜆)−1/2((Σ −ˆΣ) + 𝜆(𝐿−ˆ𝐿))(Σ + 𝜆𝐿+ 𝜇𝜆)−1/2
$$

op where ∥·∥op designs the operator norm. In this setting, the low-rank approximation is controlled through

$$
(Σ + 𝜆𝐿)1/2(𝐼−𝑃) Σ1/2(𝐼−𝑃)
$$

op, and when 𝐿⪯𝑐Σ𝛼, this term can be controlled by op +

𝜆1/2 

Σ1/2(𝐼−𝑃)

$$
𝛼
$$

op which can be controlled based on the work of Rudi et al. (2015).

<!-- page: 175 -->

9.E. CONSISTENCY ANALYSIS 173

### 9.E.2 Risk decomposition

In this subsection, we decompose the risk appearing in Theorem 16.

Control of biases

$$
𝑔𝜌−ˆ𝑔𝑝
$$

We begin by splitting the error 𝐿2 between a bias term due to the regularization parameters and a variance term due to the data. With the notation of Table 9.2,

$$
𝑔𝜌−ˆ𝑔𝑝 𝑔𝜌−𝑔𝜆 𝑔𝜆−𝑔𝜆,𝜇 𝑔𝜆,𝜇−ˆ𝑔𝑝
𝐿2 ≤ 𝐿2 + 𝐿2 + 𝐿2 . (9.21)
$$

(9.21)

We will control the ﬁrst two terms here, and the last term in the following subsections.

Proposition 74 (Bias in 𝜆). Under Assumption 17

$$
𝑔𝜆−𝑔𝜌 L𝑔𝜌
𝐿2 ≤𝜆 𝐿2 . (9.22)
$$

(9.22)

Proof. Based on the deﬁnition of 𝑔𝜆= (𝐼+ 𝜆L)−1𝑔𝜌, we have

$$
𝑔𝜆−𝑔𝜌= ((𝐼+ 𝜆L)−1 −𝐼)𝑔𝜌= −𝜆L𝑔𝜌.
$$

Because 𝑔𝜌is supported on the ﬁrst eigenvectors of the Laplacian (Assumption 17), we have 𝑔𝜌= Í𝑟 𝑒𝑖, with 𝑒𝑖the eigenvector of L appearing in (9.17), and

$$
𝑔𝜌, 𝑒𝑖
$$

𝑖=1

$$
L𝑔𝜌 2 𝑟∑︁ 2 𝑟∑︁ 2 ≤𝜆−2 𝑔𝜌 2
𝐿2 = 𝜆−1 𝑔𝜌, 𝑒𝑖 𝑒𝑖 = 𝜆−2 𝑔𝜌, 𝑒𝑖 𝐿2 < +∞.
𝑖 𝑖 𝑟
𝑖=1 𝐿2 𝑖=1
$$

This ends the proof of this proposition. □ Proposition 75 (Bias in 𝜇). Under Assumptions 17 and 18, we have

$$
𝑔𝜆,𝜇−𝑔𝜆 2 𝑔𝜌 2 𝑟∑︁ 𝐾−1/2𝑒𝑖 𝑟∑︁
2
𝐿2 ≤𝜆𝜇𝑐2 𝐿2 , with 𝑐2 𝑎= 𝐿2 = ∥𝑒𝑖∥2 H . (9.23)
𝑎
𝑖=1 𝑖=1
$$

(9.23)

Proof. Before diving into the proof, recall that the RKHS norm penalization can be written as ∥𝑔∥H = 𝐾−1/2𝑔 𝐿2. Using the fact that 𝐴−1 −𝐵−1 = 𝐴−1(𝐵−𝐴)𝐵−1, we have

$$
𝑔𝜆,𝜇−𝑔𝜆= ((𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1 −(𝐼+ 𝜆L)−1)𝑔𝜌
= −(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1𝜆𝜇𝐾−1(𝐼+ 𝜆L)−1𝑔𝜌
= −(𝜆𝜇)1/2(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1/2(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1/2
· · · × (𝜆𝜇𝐾−1)1/2𝐾−1/2(𝐼+ 𝜆L)−1𝑔𝜌.
$$

As a consequence,

$$
𝑔𝜆,𝜇−𝑔𝜆 2 𝐾−1/2(𝐼+ 𝜆L)−1𝑔𝜌
2
𝐿2 ≤𝜆𝜇 𝐿2 ,
(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1/2
$$

where we used the fact that 𝐼+ 𝜆L + 𝜇𝜆𝐾−1 ⪰𝐼, so that op ≤1 (with ∥·∥op the operator norm), and that

$$
(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1/2(𝜆𝜇𝐾−1)1/2 𝐾−1/2(𝐼+ 𝜆L + 𝜇𝜆𝐾−1)−1𝐾−1/2
2
op = 𝜆𝜇
(𝐾+ 𝜆𝐾1/2L𝐾1/2 + 𝜇𝜆)−1 op
= 𝜆𝜇 op ≤1.
$$

We continue the proof with

$$
≤
𝐾−1/2(𝐼+ 𝜆L)−1𝑔𝜌 = 𝑟∑︁ 𝑟∑︁ 𝐾−1/2𝑒𝑖
𝜆𝑖 𝜆+ 𝜆𝑖 𝐾−1/2𝑒𝑖 𝜆𝑖 𝜆+ 𝜆𝑖
𝑔𝜌, 𝑒𝑖 𝑔𝜌, 𝑒𝑖
𝑖=1 𝑖=1 ∑︁ !1/2
𝑟∑︁ 𝐾−1/2𝑒𝑖 𝑔𝜌 𝐾−1/2𝑒𝑖
2
≤ 𝑔𝜌, 𝑒𝑖 𝐿2 ≤ .
𝐿2 𝐿2
𝑖=1 𝑖≤𝑟
$$

Putting all the pieces together ends the proof. □

<!-- page: 176 -->

Vector concentration

$$
ˆ𝑔𝑝−𝑔𝜆,𝜇
$$

. To ease derivations, we denote 𝐶= Σ+𝜆𝐿, ˆ𝐶= ˆΣ+𝜆ˆ𝐿, 𝜃𝜌= 𝑆★𝑔𝜌, ˆ𝜃𝜌= Ŝ★𝑔𝜌and 𝑃the projection from H to Span We are left with the study of the variance 

𝑖≤𝑝. We have, for Tikhonov regularization

$$
𝑘𝑋𝑖
ˆ𝑔𝑝−𝑔𝜆,𝜇 𝑆 
𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃ˆ𝜃𝜌−(𝐶+ 𝜆𝜇)−1𝜃𝜌
𝐿2 =
Σ1/2 𝐿2 
𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃ˆ𝜃𝜌−(𝐶+ 𝜆𝜇)−1𝜃𝜌
= H .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We begin by isolating the dependency to labeled data

$$
ˆ𝑔𝑝−𝑔𝜆,𝜇 Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1( ˆ𝜃𝜌−𝜃𝜌)
𝐿2 ≤
· · · + Σ1/2 
H (9.24)
𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝜃𝜌−(𝐶+ 𝜆𝜇)−1𝜃𝜌
H .
$$

(9.24)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We will control the ﬁrst term here, and the second term in the following subsection.

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2
$$

Lemma 76 (Vector term). When

$$
op ≤1/2, we have
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃( ˆ𝜃𝜌−𝜃𝜌) (𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌)
H ≤2 H . (9.25)
$$

(9.25)

Proof. We begin with the splitting

$$
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃( ˆ𝜃𝜌−𝜃𝜌) Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2
H ≤
· · · × (𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) op
H .
$$

The ﬁrst term will concentrate toward a matrix smaller than identity, while the second term concentrates toward zero. We can make those considerations more formal. Following basic properties with the Löwner order on operators, we have

$$
(𝐶+ 𝜆𝜇)−1/2(𝐶−ˆ𝐶)(𝐶+ 𝜆𝜇)−1/2 ⪯𝑡
⇒ ˆ𝐶⪰(1 −𝑡)𝐶−𝑡𝜆𝜇
⇒ 𝑃ˆ𝐶𝑃⪰(1 −𝑡)𝑃𝐶𝑃−𝑡𝜆𝜇𝑃⪰(1 −𝑡)𝑃𝐶𝑃−𝑡𝜆𝜇
⇒ 𝑃ˆ𝐶𝑃+ 𝜆𝜇⪰(1 −𝑡)(𝑃𝐶𝑃+ 𝜆𝜇)
⇒ (𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1 ⪯(1 −𝑡)−1(𝑃𝐶𝑃+ 𝜆𝜇)−1
⇒ (𝐶+ 𝜆𝜇)1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2
⪯(1 −𝑡)−1(𝐶+ 𝜆𝜇)1/2𝑃(𝑃𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2 ⪯(1 −𝑡)−1,
$$

where we have used the fact that the last operator is a projection. As a consequence, for any 𝑡∈(0, 1), we have

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2
op ≤𝑡
(𝐶+ 𝜆𝜇)1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1(𝐶+ 𝜆𝜇)1/2
⇒ op ≤(1 −𝑡)−1.
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2
⇒ op ≤(1 −𝑡)−1.
$$

Where the last implication follows from the fact that 𝐶+ 𝜆𝜇= Σ + 𝜆𝐿+ 𝜆𝜇⪰Σ. □ Basis concentration We are left with the study of the basis concentration with the number of unlabeled data.

<!-- page: 177 -->

9.E. CONSISTENCY ANALYSIS 175

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2
$$

Lemma 77 (Basis term). When

$$
op ≤1/2, we have
Σ1/2(𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1 −(𝐶+ 𝜆𝜇)−1)𝜃𝜌
𝐶1/2(𝐼−𝑃) (𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H (9.26)
≤3 op ∥𝑔𝜆∥H + 2 H .
𝑔𝜌
$$

(9.26)

Notice that Assumptions 17 and 18 imply ∥𝑔𝜆∥H ≤𝑐𝑎

$$
𝐿2 < +∞.
$$

Proof. First of all, using that 𝐴−1 −𝐵−1 = 𝐴−1(𝐵−𝐴)𝐵−1, notice that

$$
Σ1/2(𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1 −(𝐶+ 𝜆𝜇)−1)𝜃𝜌
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶−ˆ𝐶𝑃)(𝐶+ 𝜆𝜇)−1𝜃𝜌−Σ1/2(𝐼−𝑃)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H
=
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃( ˆ𝐶𝑃−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 Σ1/2(𝐼−𝑃)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H
≤ H +
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2 (𝐶+ 𝜆𝜇)−1/2𝑃( ˆ𝐶𝑃−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H
≤
· · · + Σ1/2(𝐼−𝑃) (𝐶+ 𝜆𝜇)−1𝜃𝜌 op H
H .
op
Σ1/2(𝐼−𝑃) 𝐶1/2(𝐼−𝑃)
$$

op, and we also have Because Σ ⪯Σ + 𝜆𝐿= 𝐶, we have

$$
op ≤
(𝐶+ 𝜆𝜇)−1𝜃𝜌 𝐶−1𝜃𝜌 𝐾−1/2𝑆𝐶−1𝜃𝜌 𝐾−1/2𝑔𝜆
H ≤ H = H = 𝐿2 = ∥𝑔𝜆∥H .
$$

Recall, that, for any 𝑡∈(0, 1), we have already shown that

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2
op ≤𝑡
Σ1/2𝑃(𝑃ˆ𝐶𝑃+ 𝜆𝜇)−1𝑃(𝐶+ 𝜆𝜇)1/2
⇒ op ≤(1 −𝑡)−1.
$$

We are left with one last term to work on

$$
(𝐶+ 𝜆𝜇)−1/2𝑃( ˆ𝐶𝑃−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 (𝐶+ 𝜆𝜇)−1/2𝑃( ˆ𝐶−𝐶)𝑃(𝐶+ 𝜆𝜇)−1𝜃𝜌
H ≤
· · · + (𝐶+ 𝜆𝜇)−1/2𝐶(𝐼−𝑃)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H
H .
$$

We control the ﬁrst term with the fact for 𝐴, 𝐵, 𝐶three self-adjoint operators and 𝑥a vector we have

$$
\frac{∥𝐴𝑃𝐵𝑃𝐶𝑥∥= ∥𝐴𝑃𝐵𝑃𝐶𝑥⊗𝑥𝐶𝑃𝐵𝑃𝐴∥1/2}{op ,}
$$

and that

$$
𝑃𝐶𝑥⊗𝑥𝐶𝑃⪯𝐶𝑥⊗𝑥𝐶
⇒ 𝑃𝐵𝑃𝐶𝑥⊗𝑥𝐶𝑃𝐵𝑃⪯𝐵𝑃𝐶𝑥⊗𝑥𝐶𝑃𝐵⪯𝐵𝐶𝑥⊗𝑥𝐶𝐵
⇒ 𝐴𝑃𝐵𝑃𝐶𝑥⊗𝑥𝐶𝑃𝐵𝑃𝐴⪯𝐴𝐵𝐶𝑥⊗𝑥𝐶𝐵𝐴,
$$

so that

$$
(𝐶+ 𝜆𝜇)−1/2𝑃( ˆ𝐶−𝐶)𝑃(𝐶+ 𝜆𝜇)−1𝜃𝜌 (𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌
H ≤ H .
$$

We control the second term with

$$
(𝐶+ 𝜆𝜇)−1/2𝐶(𝐼−𝑃)(𝐶+ 𝜆𝜇)−1𝜃𝜌
(𝐶+ 𝜆𝜇)−1/2𝐶1/2 𝐶1/2(𝐼−𝑃) (𝐶+ 𝜆𝜇)−1𝜃𝜌 .
≤
$$

Using that (𝐶+ 𝜆𝜇)−1/2𝐶1/2 ⪯𝐼, we can add up everything to get the lemma.

<!-- page: 178 -->

For the part concerning ∥𝑔𝜆∥H, notice that

$$
𝐾−1/2𝑔𝜆 𝑟∑︁ 𝑟∑︁ 𝑔𝜌 𝑒𝑖 𝐾−1/2𝑒𝑖
𝜆𝑖 𝜆𝑖+ 𝜆 𝐾−1/2𝑒𝑖
∥𝑔𝜆∥H = 𝐿2 = 𝑔𝜌, 𝑒𝑖 ≤
𝑑 ∑︁ 𝑖=1 !1/2 𝐿2 𝑖=1
𝑔𝜌 𝐾−1/2𝑒𝑖 𝑔𝜌
2
≤ = 𝑐𝑎 𝐿2 ,
𝐿2 𝐿2
𝑖=1
$$

with 𝑐𝑎deﬁned as before. □ Conclusion Based on the last subsections, we have proved the following proposition.

(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2

 ≤1/2, Under the as- sumptions 17 and 18, Proposition 78 (Risk decomposition). When

$$
ˆ𝑔𝑝−𝑔𝜌 2 𝐿2 ≤4𝜆2 

L𝑔𝜌 2 𝑔𝜌 2 (𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌)
2
𝐿2 + 4𝜆𝜇𝑐2 𝐿2 + 8
𝐶1/2(𝐼−𝑃) 𝑎 (𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌
𝑔𝜌 2 H (9.27)
2 2
· · · + 12𝑐2 𝑎 𝐿2 + 8 H .
op
$$

(9.27)

We are left with the quantiﬁcation of the diﬀerent convergences when the number of labeled and unlabeled data grows toward inﬁnity. We will quantify those convergences based on concentration inequalities.

### 9.E.3 Probabilistic inequalities

In this subsection, we bound each term appearing in (9.27) based on concentration inequalities.

Vector concentration The concentration of ˆ𝜃𝜌= Ŝ★𝑔𝜌toward 𝜃𝜌= 𝑆★𝑔𝜌is controlled through Bernstein inequality.

Theorem 17 (Concentration in Hilbert space (Yurinskii, 1970)). Let denote by A a Hilbert space and by (𝜉𝑖) a sequence of independent random vectors in A such that E[𝜉𝑖] = 0, that are bounded by a constant 𝑀, with ﬁnite variance 𝜎2 = E[Í𝑛

$$
\sum_{𝑛 P( 𝜉𝑖 𝑖=1}^{𝑖=1 ∥𝜉𝑖∥2]. For any 𝑡> 0, ≥𝑡) ≤2 exp} − \frac{𝑡2}{2𝜎2 + 2𝑡𝑀/3} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proposition 79 (Vector concentration). When |𝑌| is bounded by a constant 𝑐Y, and 𝑥→𝑘(𝑥, 𝑥) by a constant 𝜅2, we have, with D𝑛ℓ∼𝜌⊗𝑛ℓthe dataset generating the labeled data

$$
!
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 
− 𝑛ℓ𝑡2
PD𝑛ℓ H ≥𝑡 ≤2 exp , (9.28)
2𝜎2 ℓ(𝜇𝜆)−1 + 2𝑡𝑐Y (𝜇𝜆)−1/2𝜅/3
$$

(9.28)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝜎2

$$
ℓ≤𝑐2
$$

Y Tr(Σ) is a variance parameter to relate with the variance of 𝑌(𝐼+ 𝜆L)−1𝛿𝑋(where the randomness is inherited from (𝑋,𝑌) ∼𝜌).

Proof. Recall that

$$
𝑛ℓ ∑︁
(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) = (Σ + 𝜆𝐿+ 𝜆𝜇)−1/2(𝑛−1 𝑌𝑖𝑘𝑋𝑖−E𝜌[𝑌𝑘𝑋])
ℓ
𝑖=1
$$

<!-- page: 179 -->

9.E. CONSISTENCY ANALYSIS 177 We want to apply Bernstein inequality to the vector 𝜉𝑖= (Σ + 𝜆𝐿+ 𝜇𝜆)−1/2𝑌𝑖𝑘𝑋𝑖, after centering it. Let us denote by 𝑐Y a bound on |𝑌|, 𝑐Y ∈R exists since we have supposed 𝜌of compact support. We have

$$
𝑛ℓ ∑︁
𝜎2 = E[ ∥𝜉𝑖−E[𝜉𝑖]∥2] = 𝑛ℓE[∥𝜉−E[𝜉𝑖]∥2] ≤𝑛ℓE[∥𝜉∥2]
𝑖=1 𝑌2 
= 𝑛ℓE(𝑋,𝑌)∼𝜌 𝑘𝑋, (Σ + 𝜆𝐿+ 𝜇𝜆)−1𝑘𝑋
 
≤𝑛ℓ𝑐2 Y E𝑋∼𝜌X 𝑘𝑋, (Σ + 𝜆𝐿+ 𝜇𝜆)−1𝑘𝑋
 
= 𝑛ℓ𝑐2 Y Tr (Σ + 𝜆𝐿+ 𝜇𝜆)−1Σ
(Σ + 𝜆𝐿+ 𝜇𝜆)−1
≤𝑛ℓ𝑐2 Y Tr(Σ) op ≤𝑛ℓ𝑐2 Y Tr(Σ)(𝜇𝜆)−1.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Note that we have proceed with a generic upper bound, but we expect this variance, which is related to the variance of 𝑌(𝐼+ 𝜆L + 𝜆𝜇𝐾−1)−1𝛿𝑋to be potentially much smaller – if we remove the term in 𝑃the vector concentration is the concentration of the vector 𝑆(𝑆∗𝑆+ 𝜆𝑆★L𝑆+ 𝜆𝜇)−1𝑌𝑘𝑋≃𝐾1/2(𝐾+ 𝜆𝐾1/2L𝐾1/2 + 𝜆𝜇)−1𝐾1/2𝑆−★𝑌𝑘𝑋= (𝐼+ 𝜆𝐿+ 𝜆𝜇𝐾−1)−1𝑌𝑆−★𝑘𝑋≃(𝐼+ 𝜆𝐿+ 𝜆𝜇𝐾−1)−1𝑌𝛿𝑋. To capture this fact, we will write 𝜎2 ≤𝑛ℓ𝜎2 ℓ(𝜇𝜆)−1, with 𝜎ℓ= 𝑐Y Tr(Σ)1/2 in our analysis, but potentially much smaller under reﬁned hypothesis and in practice. Similarly to the bound on the variance, we have

$$
(Σ + 𝜆𝐿+ 𝜇𝜆)−1/2𝑌𝑖𝑘𝑋𝑖 ≤(𝜇𝜆)−1/2𝑐Y𝜅,
∥𝜉−E[𝜉]∥≤∥𝜉∥=
$$

with 𝜅an upper bound on 𝑘(𝑥, 𝑥)1/2 for 𝑥∈supp 𝜌X . As a consequence, applying Bernstein concentration inequality, we get, for any 𝑡> 0,

$$
𝑛−1 ≥𝑡) ≤2 exp !
𝑛ℓ ∑︁
− 𝑛ℓ𝑡2
PD𝑛ℓ( 𝜉𝑖−𝐸[𝜉𝑖] .
ℓ 2𝜎2 ℓ(𝜇𝜆)−1 + 2𝑡𝑐Y (𝜇𝜆)−1/2𝜅/3
𝑖=1
$$

This ends the proof. □ Operator concentration The convergence of ˆ𝐶toward 𝐶is controlled with Bernstein inequality for self-adjoint operators.

Theorem 18 (Bernstein inequality for self-adjoint (Minsker, 2017)). Let A be a separable Hilbert space, and (𝜉𝑖) a sequence of independent random self-adjoint operators on A. Assume that (𝜉𝑖) are bounded by 𝑀∈R, in the sense that almost everywhere ∥𝜉∥op < 𝑀, and have a ﬁnite variance 𝜎2 =

$$
Í𝑛 \frac{𝑖=1 E[𝜉2}{𝑖]}
$$

op. For any 𝑡> 0,

$$
Tr Í𝑛 𝑖] Í𝑛 
𝑛 ∑︁
P ©­ > 𝑡ª® 1 + 6 𝜎2 + 𝑀𝑡/3 𝑡2 𝑖=1 E[𝜉2 − 𝑡2
(𝜉𝑖−E[𝜉𝑖]) ≤2 exp .
𝑖=1 E[𝜉2 𝑖] 2𝜎2 + 2𝑡𝑀/3
« 𝑖=1 ¬ op
op
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proposition 80 (Operator concentration). When 𝑥→𝑘(𝑥, 𝑥) is bounded by 𝜅2, and 𝑥→𝜕1,𝑗𝜕2,𝑗𝑘(𝑥, 𝑥) is bounded by 𝜅2

$$
𝑗, we have
 


(𝐶+ 𝜇𝜆)−1 2 + 56 𝜅2 + 𝜆Í𝑑 !
𝑖=1 𝜅2
PD𝑛 2 (𝐶−ˆ𝐶)(𝐶+ 𝜇𝜆)−1 2 op > 1/2 𝑗 𝜆𝜇𝑛
≤
𝜅2 + 𝜆Í𝑑 (9.29)
𝑗=1 𝜅2 ©­­ « ª®® ¬
· · · × (1 + 𝜆𝜇∥𝐶∥−1 op) 𝑗 𝜆𝜇 exp − 𝜆𝜇𝑛 10 
𝜅2 + 𝜆Í𝑑 .
𝑗=1 𝜅2
𝑗
$$

(9.29)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. We want to apply the precedent concentration inequality to

$$
𝑑 ∑︁
𝜉𝑖= (Σ + 𝜆𝐿+ 𝜆𝜇)−1/2(𝑘𝑋𝑖⊗𝑘𝑋𝑖+ 𝜆 𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋𝑖)(Σ + 𝜆𝐿+ 𝜆𝜇)−1/2,
𝑗=1
$$

<!-- page: 180 -->

since we have, based on the fact that 𝐶= Σ + 𝜆𝐿and that Σ = E[𝑘𝑋⊗𝑘𝑋] and 𝐿= E[Í𝑛

$$
𝑗=1 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋],
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2 𝑛 ∑︁
op = 𝑛−1 𝜉𝑖−E[𝜉𝑖] .
𝑖=1 op
$$

We bound 𝜉with

$$
𝑑 ∑︁
2 ©­ « 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋ª®
(𝐶+ 𝜇𝜆)−1 (𝐶+ 𝜇𝜆)−1
∥𝜉∥op = 𝑘𝑋⊗𝑘𝑋+ 𝜆 2
𝑗=1 ¬
op
𝑑 ∑︁
≤Tr ©­ 2 ©­ « 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋ª® 2 ª® ¬
(𝐶+ 𝜇𝜆)−1 (𝐶+ 𝜇𝜆)−1
𝑘𝑋⊗𝑘𝑋+ 𝜆
« 𝑗=1 ¬
 2 𝑘𝑋⊗𝑘𝑋(𝐶+ 𝜇𝜆)−1 2 
= Tr (𝐶+ 𝜇𝜆)−1
𝑑 ∑︁ 2 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋(𝐶+ 𝜇𝜆)−1 2 
Tr (𝐶+ 𝜇𝜆)−1
· · · + 𝜆
𝑗=1
(𝐶+ 𝜇𝜆)−1 𝑑 ∑︁ (𝐶+ 𝜇𝜆)−1 𝑑 ∑︁
2 H ≤(𝜆𝜇)−1 ©­ 2 ª® ¬
= 2 𝑘𝑋 2 𝜕𝑗𝑘𝑋 𝜅2 + 𝜆 𝜅2
H + 𝜆 .
« 𝑗
𝑗=1 𝑗=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

With 𝜅2 an upper bound on the kernel 𝑘and 𝜅2 𝑗an upper bound on 𝜕1,𝑗𝜕2,𝑗𝑘. For the variance we have, using Löwner order,

$$
𝑑 ∑︁
∥𝜉(𝑋)∥op E[𝜉] ⪯(𝜆𝜇)−1 ©­ ª® ¬
E[𝜉2] ⪯sup 𝜅2 + 𝜆 𝜅2 E[𝜉]
« 𝑗
𝑋∈X 𝑗=1
𝑑 ∑︁ 𝑑 ∑︁
= (𝜆𝜇)−1 ©­ ª® ¬ (𝐶+ 𝜆)−1𝐶⪯(𝜆𝜇)−1 ©­ ª® ¬
𝜅2 + 𝜆 𝜅2 𝜅2 + 𝜆 𝜅2
.
« 𝑗 « 𝑗
𝑗=1 𝑗=1
$$

Therefore, we get for any 𝑡> 0,

$$
(𝐶+ 𝜇𝜆)−1 
PD𝑛 2 (𝐶−ˆ𝐶)(𝐶+ 𝜇𝜆)−1 2
op > 𝑡
1 + 6 (𝜅2 + 𝜆Í𝑑 !
 
𝑖=1 𝜅2 𝑗)(1 + 𝑡/3) ∥𝐶∥op + 𝜆𝜇
≤2 Tr (𝐶+ 𝜆)−1𝐶
𝜆𝜇𝑛𝑡2 ∥𝐶∥op
· · · × exp ©­­ « ª®® ¬
− 𝑛𝑡2 2(𝜆𝜇)−1 
𝜅2 + 𝜆Í𝑑 .
𝑗=1 𝜅2 (1 + 𝑡/3)
𝑗
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Remark that

$$
(𝐶+ 𝜇𝜆)−1 𝑑 ∑︁
Tr (𝐶+ 𝜇𝜆)−1𝐶 op Tr(𝐶) ≤(𝜆𝜇)−1(𝜅2 + 𝜆 𝜅2
≤ 𝑗).
𝑗=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Taking 𝑡= 1/2 ends the lemma. □ Basis concentration

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌
$$

Similarly, we could control H by using concentration of self-adjoint, yet this will lead to laxer bounds, than using concentration on vectors.

Proposition 81 (Basis concentration). When 𝑥→𝑘(𝑥, 𝑥) is bounded by 𝜅2, 𝑥→𝜕1,𝑗𝜕2,𝑗𝑘(𝑥, 𝑥) is bounded by 𝜅2 𝑗, with Assumptions 17 and 18, we have

$$
(𝐶+ 𝜇𝜆)−1 
− 𝜇𝜆𝑛𝑡2
PD𝑛 2 (𝐶−ˆ𝐶)(𝐶+ 𝜇𝜆)−1𝜃𝜌 ≤2 exp , (9.30)
H > 𝑡
2𝑐1(𝑐1 + 𝜆1/2𝜇1/2𝑡/3)
$$

(9.30)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 181 -->

9.E. CONSISTENCY ANALYSIS 179

$$
𝑔𝜌
$$

with 𝑐1 = (𝜅2 + 𝜆Í𝑑

$$
𝑖=1 𝜅2 𝑗)𝑐𝑎 𝐿2.
$$

Proof. We want to apply Bernstein concentration inequality to the vectors

$$
𝑑 ∑︁
𝜉𝑖= (𝐶+ 𝜇𝜆)−1/2 ©­ ª® ¬
𝑘𝑋𝑖⊗𝑘𝑋𝑖+ 𝜆 𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋𝑖 (𝐶+ 𝜆𝜇)−1𝜃𝜌,
« 𝑗=1
$$

since (𝐶+ 𝜇𝜆)−1

$$
𝑛 ∑︁
2 (𝐶−ˆ𝐶)(𝐶+ 𝜇𝜆)−1𝜃𝜌 H = 𝑛−1 𝜉𝑖−E[𝜉𝑖]
.
𝑖=1 H
$$

We bound 𝜉, reusing prior derivations, with

$$
𝑑 ∑︁
(𝐶+ 𝜇𝜆)−1/2 ©­ ª® ¬
∥𝜉𝑖∥H = 𝑘𝑋𝑖⊗𝑘𝑋𝑖+ 𝜆 𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋𝑖 (𝐶+ 𝜆𝜇)−1𝜃𝜌
« 𝑗=1
H
(𝐶+ 𝜇𝜆)−1/2 𝑑 ∑︁ (𝐶+ 𝜇𝜆)−1𝜃𝜌
©­ « ª® ¬
≤ 𝑘𝑋𝑖⊗𝑘𝑋𝑖+ 𝜆 𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋𝑖 H .
op
𝑗=1
op
𝑑 ∑︁ 𝑔𝜌
≤(𝜇𝜆)−1/2(𝜅2 + 𝜆 𝜅2
𝑗)𝑐𝑎 𝐿2 .
𝑖=1
$$

For the variance, we have, similarly to prior derivations,

$$
𝑑 ∑︁ (𝐶+ 𝜆𝜇)−1𝜃𝜌 2
E[∥𝜉∥2] ≤sup 𝑘𝑋⊗𝑘𝑋+ 𝜆 𝜕𝑗𝑘𝑋⊗𝜕𝑗𝑘𝑋
𝑋∈X 𝑗=1
op
· · · × E  
𝑑 ∑︁
(𝐶+ 𝜇𝜆)−1 ©­ 𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋ª®
𝑘𝑋⊗𝑘𝑋+ 𝜆
« 𝑗=1 ¬op
!
𝑑 ∑︁ 𝑔𝜌 2
𝜅2 + 𝜆 𝜅2 𝑐2
≤
𝑖 𝑎 𝐿2
𝑖=1
· · · E  
(𝐶+ 𝜇𝜆)−1𝑘𝑋⊗𝑘𝑋 𝑑 ∑︁ (𝐶+ 𝜇𝜆)−1𝜕𝑗𝑘𝑋𝑖⊗𝜕𝑗𝑘𝑋
op + 𝜆
op
! 𝑗=1
𝑑 ∑︁ 𝑔𝜌 2 
= 𝜅2 + 𝜆 𝜅2 𝑐2 𝐿2 Tr (𝐶+ 𝜇𝜆)−1𝐶
𝑖 𝑎
𝑖=1 !2
𝑑 ∑︁ 𝑔𝜌 2
≤(𝜆𝜇)−1 𝜅2 + 𝜆 𝜅2 𝑐2
𝐿2 .
𝑖 𝑎
𝑖=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As a consequence, using Bernstein inequality,

$$
> 𝑡 ! 2𝑐1(𝑐1 + 𝜆1/2𝜇1/2𝑡/3) , 
𝑛 ∑︁
− 𝜇𝜆𝑛𝑡2
P 𝑛−1 𝜉𝑖−E[𝜉𝑖] ≤2 exp
𝑖=1
𝑔𝜌
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑐1 = (𝜅2 + 𝜆Í𝑑

$$
𝑖=1 𝜅2
$$

𝐿2. Note that we have bounded naively the variable 𝜉and its variance,

$$
𝑗)𝑐𝑎 (𝐶+ 𝜆𝜇)−1𝜕𝑖𝑘𝑋
$$

and Tr((𝐶+ 𝜆𝜇)−1𝐶), which under interpolation and capacity assumptions could be controlled in a better fashion. □

$$
(𝐶+ 𝜆𝜇)−1𝑘𝑋 + 𝜆Í𝑑
$$

but we have shown how appears sup𝑋∈X

$$
𝑖=1
$$

Low-rank approximation We now switch to Nyström approximation.

<!-- page: 182 -->

Proposition 82 (Low-rank approximation). When 𝑥→𝑘(𝑥, 𝑥) is bounded by 𝜅2, for any 𝑝∈N and 𝑡> 0, we have

$$
(𝐼−𝑃)Σ1/2 
2 > 𝑡 2 + 116𝜅2 op) 𝜅2 −𝑝𝑡
PD𝑝 ≤ (2 + 𝑡∥Σ∥−1 𝑡exp
,
𝑡𝑝 10𝜅2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. Reusing Proposition 3 of Rudi et al. (2015), for any 𝛾> 0, we have, with 𝑃the projection on Span

$$
𝑖≤𝑝and ˆΣ = 𝑝−1 Í𝑝
𝑘𝑋𝑖 𝑖=1 𝑘𝑋𝑖⊗𝑘𝑋𝑖,
(𝐼−𝑃)Σ1/2 ( ˆΣ + 𝛾)−1/2Σ1/2 Σ1/2( ˆΣ + 𝛾)−1Σ1/2
2 ≤𝛾 2
op ≤𝛾 op .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

As a consequence, skipping derivations that can be retaken from our precedent proofs,

$$
(𝐼−𝑃)Σ1/2 Σ1/2( ˆΣ + 𝛾)−1Σ1/2 
2 > 𝑡
PD𝑝 ≤inf 𝛾>0 PD𝑝 𝛾 op > 𝑡
 


(Σ + 𝛾)−1/2( ˆΣ −Σ)(Σ + 𝛾)−1/2 
≤inf 𝛾>0 PD𝑝 op > (1 −𝛾𝑡−1)
 
2 + 56 𝜅2 − 𝑝𝛾𝑢2
≤inf (1 + 𝛾∥Σ∥−1 op) 𝑓𝑟𝑎𝑐𝜅2𝛾exp
,
𝛾>0 𝛾𝑝 2𝜅2(1 + 𝑢/3)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝑢= (1 −𝛾𝑡−1). Taking 𝛾= 𝑡/2, this term is simpliﬁed as

$$
(𝐼−𝑃)Σ1/2 
2 > 𝑡 2 + 116 𝜅2 op) 𝜅2 −𝑝𝑡
PD𝑝 ≤ (2 + 𝑡∥Σ∥−1 𝑡exp
,
𝑡𝑝 10𝜅2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

which is the object of this proposition. □ Lemma 83. When 𝐿≤𝑐𝑑Σ𝑎, we have

$$
(𝐼−𝑃)𝐶1/2 (𝐼−𝑃)Σ1/2 (𝐼−𝑃)Σ1/2
2 2 2𝑎
op ≤ op + 𝑐𝑑𝜆 op . (9.31)
$$

(9.31)

Proof. This follows from the fact that

$$
𝐶1/2(𝐼−𝑃)
2
op = ∥(𝐼−𝑃)𝐶(𝐼−𝑃)∥op = ∥(𝐼−𝑃)(Σ + 𝜆𝐿)(𝐼−𝑃)∥op
≤∥(𝐼−𝑃)Σ(𝐼−𝑃)∥op + 𝜆∥(𝐼−𝑃)𝐿(𝐼−𝑃)∥op ≤∥(𝐼−𝑃)Σ(𝐼−𝑃)∥op + 𝜆𝑐𝑑∥(𝐼−𝑃)Σ𝑎(𝐼−𝑃)∥op
(𝐼−𝑃)Σ1/2 (𝐼−𝑃)Σ𝑎/2
2 2
= op + 𝜆𝑐𝑑
(𝐼−𝑃)Σ1/2 (𝐼−𝑃)𝑎Σ𝑎/2 op
2 2
= op + 𝜆𝑐𝑑
(𝐼−𝑃)Σ1/2 (𝐼−𝑃)Σ1/2 op
2 2𝑎
≤ op + 𝜆𝑐𝑑 op ,
$$

where we used the fact that (𝐼−𝑃)𝑎= (𝐼−𝑃) and that ∥𝐴𝑠𝐵𝑠∥≤∥𝐴𝐵∥𝑠for 𝑠∈[0, 1] and 𝐴, 𝐵positive self-adjoint. □

### 9.E.4 Averaged excess of risk - ending the proof

Based on the precedent excess of risk decomposition, and precedent concentration inequalities, we have all the elements to derive convergence rates of our algorithm. We will enunciate this convergence in terms of the averaged excess of risk of ED𝑛

$$
h

 ˆ𝑔𝑝−𝑔𝜌 \frac{2}{𝐿2} i .
$$

<!-- page: 183 -->

9.E. CONSISTENCY ANALYSIS 181 Lemma 84. Under Assumptions 17 and 18,

$$
h

 ˆ𝑔𝑝−𝑔𝜌 2 i 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2


 ≤1/2 
ED𝑛 ≤4𝑐2 Y P
· · · + 4𝜆2 

L𝑔𝜌 2 𝐿2 𝑔𝜌 2
𝐿2 + 4𝜆𝜇𝑐2
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 𝑎 𝐿2 


𝐶1/2(𝐼−𝑃) 
𝑔𝜌 2
2 2 (9.32)
· · · + 8 ED𝑛 + 12𝑐2 𝐿2 ED𝑛
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 𝑎 op
H
2
· · · + 8 ED𝑛 .
H
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2

 ≤1/2
$$

(9.32)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. We proceed using the fact that E[𝑋] = E[𝑋| 𝑐𝐴] P(𝑐𝐴) + E[𝑋| 𝐴] P(𝐴) ≤sup 𝑋P(𝑐𝐴) + E[𝑋| 𝐴] P(𝐴), with 𝐴=

$$
D𝑛 ,
h

 ˆ𝑔𝑝−𝑔𝜌 2 i ˆ𝑔𝑝−𝑔𝜌 2 P (𝑐𝐴) + ED𝑛 h

 ˆ𝑔𝑝−𝑔𝜌 2 𝐴 i
ED𝑛 ≤sup P(𝐴).
𝐿2
D𝑛
𝑔𝜌
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

When 𝑌is bounded by 𝑐Y, because 𝑔𝜌is a convex combination of 𝑌, we know that 𝐿2 ≤𝑐Y, as a consequence, we can clip ˆ𝑔𝑝to [−𝑐Y, 𝑐Y], which will only improve the estimation of 𝑔𝜌, as a consequence, we can consider the clipping estimate for which we have supD𝑛

$$
ˆ𝑔𝑝−𝑔𝜌 \frac{2}{𝐿2 ≤4𝑐2}
$$

Y. Regarding the second part, we have already decomposed the risk under the event 𝐴=

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1/2

 ≤1/2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

. As a consequence, we have

$$
D𝑛
h

 ˆ𝑔𝑝−𝑔𝜌 2 i Y P(𝑐𝐴) + 4𝜆2 

L𝑔𝜌 2 𝑔𝜌 2
ED𝑛 ≤4𝑐2 𝐿2 P(𝐴) + 4𝜆𝜇𝑐2 𝐿2 P(𝐴)
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 𝐿2 𝐴 𝑎
2
· · · + 8 ED𝑛 P(𝐴)
 


𝐶1/2(𝐼−𝑃) H 𝐴 
𝑔𝜌 2
2
· · · + 12𝑐2 𝑎 𝐿2 ED𝑛 P(𝐴)
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 op 𝐴 
2
· · · + 8 ED𝑛 P(𝐴).
H
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

To control the conditional expectation, we use that, when 𝑋is positive

$$
E [𝑋| 𝐴] 𝑃(𝐴) = E[𝑋] −E [𝑋| 𝑐𝐴] P(𝑐𝐴) ≤E[𝑋].
$$

This ends the proof. □ \int_{0}

Based on deviation inequalities, we can control expectations based on the equality, for 𝑋positive, E[𝑋] =

$$
0 P(𝑋> 𝑡) d𝑡.
$$

Lemma 85. In the setting of the paper,

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 
2 ℓ(𝑛ℓ𝜇𝜆)−1 + 8𝑐2
ED𝑛 ≤8𝜎2 Y𝜅2(𝑛2 ℓ𝜇𝜆)−1. (9.33)
H
$$

(9.33)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. First, recall that

$$
!
 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 
− 𝑛ℓ𝑡2
P H > 𝑡 ≤2 exp
2𝜎2 ℓ(𝜇𝜆)−1 + 2𝑡𝑐Y (𝜆𝜇)−1/2𝜅/3
©­­ « ª®® ¬
− 𝑛ℓ𝑡2 2 max 
≤2 exp
2𝜎2 ℓ(𝜇𝜆)−1, 2𝑡𝑐Y (𝜆𝜇)−1/2𝜅/3
! 
−𝑛ℓ𝜇𝜆𝑡2 −3𝑛ℓ𝜇1/2𝜆1/2𝑡
≤2 exp + 2 exp .
4𝜎2 ℓ 4𝑐Y𝜅
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 184 -->

As a consequence

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) ∫+∞ 


(𝐶+ 𝜆𝜇)−1/2( ˆ𝜃𝜌−𝜃𝜌) 
2 2
E = 0 P H > 𝑡 d𝑡
∫ ! H ∫ 
−𝑛ℓ𝜇𝜆𝑡 −3𝑛ℓ𝜇1/2𝜆1/2𝑡1/2
≤2 exp d𝑡+ 2 exp d𝑡.
4𝜎2 ℓ 4𝑐Y𝜅
64𝑐2 Y𝜅2
= 8𝜎2 ℓ(𝑛ℓ𝜇𝜆)−1 + 9 (𝑛2 ℓ𝜇𝜆)−1.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This is the result stated in the lemma. □ Lemma 86. In the setting of the paper,

$$
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 
𝑔𝜌 2
2 ≤8(𝜅2 + 𝜆𝜕𝜅2)2𝑐2
ED𝑛
· · · × (𝜇𝜆𝑛)−1 + (𝜇𝜆𝑛2)−1 𝑎 𝐿2
H (9.34)
,
$$

(9.34)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

with 𝜕𝜅2 = Í𝑑

$$
𝑖=1 𝜅2 𝑖.
(𝐶+ 𝜆𝜇)−1/2( ˆ𝐶−𝐶)(𝐶+ 𝜆𝜇)−1𝜃𝜌 H, and 𝜕𝜅2 = Í𝑑
𝑖=1 𝜅2
$$

Proof. Let us denote by 𝐴the quantity 𝑗. Recall that

$$
− 𝜇𝜆𝑛𝑡2
P (𝐴> 𝑡) ≤2 exp
2𝑐1(𝑐1 + 𝜆1/2𝜇1/2𝑡/3) !
 
−𝜇𝜆𝑛𝑡2 −3(𝜇𝜆)1/2𝑛𝑡
≤2 exp + 2 exp .
4𝑐2 1 4𝑐1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We conclude the proof similarly to the precedent lemma. □ Lemma 87. Under Assumption 19,

$$
𝐶1/2(𝐼−𝑃) 10𝜅2 log(𝑝) 
2 𝑝 + 10𝑎𝜅2𝑎𝑐𝑑𝜆log(𝑝)𝑎
ED𝑛 ≤
op · · · × 𝑝𝑎 1 
(9.35)
1 + 2𝜅2 1 + 6 log(𝑝) 𝑝+ 1 5 log(𝑝)
.
∥Σ∥op log(𝑝)
𝐶1/2(𝐼−𝑃) 2
$$

(9.35)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. Once again, this result comes from integration of the tail bound obtained on

$$
Σ1/2(𝐼−𝑃) 2 𝐶1/2(𝐼−𝑃) 2 Σ1/2(𝐼−𝑃) 2
$$

op through the one we have on op and the fact that

$$
Σ1/2(𝐼−𝑃) 2𝑎 op ≤ op +
$$

op. For any 𝑎, 𝑏> 0, we have 𝑐𝑑𝜆

$$
Σ1/2(𝐼−𝑃) ∫∞ 


Σ1/2(𝐼−𝑃) 
2 2
ED𝑛 = 0 PD𝑛 op > 𝑡 d𝑡
∫∞ op 
 
1 + 58𝜅2 1 + 2𝜅2 −𝑝𝑡
0 min 1, 2𝜅2 ∥Σ∥−1 op exp d𝑡
≤
 𝑡𝑝 𝑡 10𝜅2 
∫∞ 
= 10𝜅2𝑎 1 + 58 10𝑎𝑢 1 + 𝑝 5𝑎𝑢
0 min 1, 2𝜅2 ∥Σ∥−1 op exp (−𝑎𝑢) d𝑢
𝑝 ∫∞ 
 
≤10𝜅2𝑎 1 + 6 𝑎𝑢 1 + 𝑝 5𝑎𝑢
2𝜅2 ∥Σ∥−1 op exp (−𝑎𝑢) d𝑢
𝑏+
𝑝 
𝑏 
≤10𝜅2 1 + 6 𝑎𝑏 1 + 𝑝 5𝑎𝑏
𝑎𝑏+ 2𝜅2 ∥Σ∥−1 exp (−𝑎𝑏)
op .
𝑝
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 185 -->

9.E. CONSISTENCY ANALYSIS 183 This last quantity is optimized for 𝑎𝑏= log(𝑝), which leads to the ﬁrst part of the lemma. Similarly,

$$
Σ1/2(𝐼−𝑃) ∫∞ 


Σ1/2(𝐼−𝑃) 
2𝑎 2𝑎
ED𝑛 = 0 PD𝑛 op > 𝑡 d𝑡
∫∞ 


Σ1/2(𝐼−𝑃) op 
2
= 0 PD𝑛 op > 𝑡1/𝑎 d𝑡
∫∞ 
1 + 58𝜅2 1 + 2𝜅2 −𝑝𝑡1/𝑎
0 min 1, 2𝜅2 ∥Σ∥−1 op exp d𝑡
≤
 𝑡1/𝑎𝑝 𝑡1/𝑎 10𝜅2 
∫∞ 1 𝑢1−𝑎exp (−𝑐𝑢)
= 10𝑎𝜅2𝑎𝑎𝑐𝑎 1 + 58 10𝑐𝑢 1 + 𝑝 5𝑐𝑢
0 min 𝑢𝑎−1, 2𝜅2 ∥Σ∥−1 d𝑢
𝑝𝑎 op
 𝑏𝑎 ∫∞ 1 𝑢1−𝑎exp (−𝑐𝑢) d𝑢 
≤10𝑎𝜅2𝑎𝑎𝑐𝑎 1 + 6 𝑐𝑢 1 + 𝑝 5𝑐𝑢
2𝜅2 ∥Σ∥−1 op
𝑎+
𝑝𝑎 
𝑏 1 (𝑐𝑏)1−𝑎exp (−𝑐𝑏)
≤10𝑎𝜅2𝑎 1 + 6 𝑐𝑏 1 + 𝑝 5𝑐𝑏
(𝑐𝑏)𝑎+ 2𝜅2 ∥Σ∥−1
op .
𝑝𝑎
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Once again this is optimized for 𝑐𝑏= log(𝑝). □ Remark 88 (Leverage scores). Out of simplicity, we only present a low rank approximation with random subsampling. Yet, we can improve the result by considering subsampling based on leverage scores. If we consider the Gaussian kernel, 𝑆𝑘𝑥∈𝐿2 can be thought of as a function that is a little bump around 𝑥∈X. In essence, subsampling based on leverage scores, consists in representing the solution on a subsampled sequence (𝑘𝑋𝑖)𝑖∈𝐼where the 𝑋𝑖are far from one another so that the bump functions (𝑆𝑘𝑋𝑖) can approximate a maximum of functions. (Rudi et al., 2015) shows that with leverage scores, we can take 𝑝= (𝜇𝜆)𝛾log(𝑛), with 𝛾linked with the capacity of the RKHS linked with the kernel 𝑘.

If we add all derivations, we have derived the following theorem.

Theorem 19. Under Assumptions 17, 18 and 19,

$$
h

 ˆ𝑔−𝑔𝜌 2 i
ED𝑛
 𝐿2 − 𝜆𝜇𝑛 10 𝜅2 + 𝜆𝜕𝜅2 
1 + 28 𝜅2 + 𝜆𝜕𝜅2 op) 𝜅2 + 𝜆𝜕𝜅2
≤8𝑐2 (1 + 𝜆𝜇∥𝐶∥−1 𝜆𝜇 exp
Y 𝜆𝜇𝑛
· · · + 4𝜆2 

L𝑔𝜌 2 𝑔𝜌 2
𝐿2 + 4𝜆𝜇𝑐2 𝐿2 + 64𝜎2 ℓ(𝑛ℓ𝜇𝜆)−1 + 57𝑐2 Y𝜅2(𝑛2 ℓ𝜇𝜆)−1
𝑔𝜌 𝑎 2 𝑔𝜌 2
(9.36)
· · · + 64(𝜅2 + 𝜆𝜕𝜅2)2𝑐2 𝑎 𝐿2 (𝜇𝜆𝑛)−1 + 57(𝜅2 + 𝜆𝜕𝜅2)2𝑐2 𝐿2 (𝜇𝜆𝑛2)−1
 10𝜅2 log(𝑝) 𝑎
𝑔𝜌 2
𝑝 + 10𝑎𝜅2𝑎𝑐𝑑𝜆log(𝑝)𝑎
· · · + 12𝑐2 𝑎
𝐿2 𝑝𝑎
· · · × 1 
1 + 2𝜅2 1 + 6 log(𝑝) 𝑝+ 1 5 log(𝑝)
.
∥Σ∥op log(𝑝)
$$

(9.36)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑐Y is an upper bound on 𝑌, 𝜅2 is an upper bound on 𝑥→𝑘(𝑥, 𝑥), 𝜕𝜅2 = Í𝑑

$$
𝑖=1 𝜅2 𝑖with 𝜅2
$$

𝑖a bound on 𝑥→𝜕1𝑖𝜕2𝑖𝜕𝑘𝑥𝑖, 𝑐𝑑and 𝑎the constants appearing in Assumption 19, 𝑐𝑎a constant such that ∥𝑔∥H ≤𝑐𝑎∥𝑔∥𝐿2 and 𝜎2

$$
ℓ≤𝑐2
$$

Y𝜅2 a variance parameter linked with the variance of 𝑌(𝐼+ 𝜆L)−1𝛿𝑋.

Theorem 16 is a corollary of this theorem.

<!-- page: 186 -->

<!-- page: 187 -->

# Part IV. Active Labeling

185

<!-- page: 188 -->

<!-- page: 189 -->

# Chapter 10. Streaming Stochastic Gradients

The following is a reproduction of Cabannes et al. (2022).

The workhorse of machine learning is stochastic gradient descent. To access stochastic gradients, it is common to consider iteratively input/output pairs of a training dataset. Interestingly, it appears that one does not need full supervision to access stochastic gradients, which is the main motivation of this paper. After formalizing the “active labeling” problem, which generalizes active learning based on partial supervision, we provide a streaming technique that provably minimizes the ratio of generalization error over the number of samples. We illustrate our technique in depth for robust regression.

## 10.1 Introduction

A large amount of the current hype around artiﬁcial intelligence was fueled by the recent successes of supervised learning. Supervised learning consists in designing an algorithm that maps inputs to outputs by learning from a set of input/output examples. When accessing many samples, and given enough computation power, this framework is able to tackle complex tasks. Interestingly, many of the diﬃculties arising in practice do not emerge from choosing the right statistical model to solve the supervised learning problem, but from the problem of collecting and cleaning enough data (see Chapters 1 and 2 of Géron, 2017, for example). Those diﬃculties are not disjoint from the current trends toward data privacy regulations (Council of European Union, 2016). This fact motivates this work, where we focus on how to eﬃciently collect information to carry out the learning process.

In this paper, we formalize the “active labeling” problem for weak supervision, where the goal is to learn a target function by acquiring the most informative dataset given a restricted budget for annotation. We focus explicitly on weak supervision that comes as a set of label candidates for each input, aiming to partially supervise input data in the most eﬃcient way to guide a learning algorithm. We also restrict our study to the streaming variant where, for each input, only a single partial information can be collected about its corresponding output. The crux of this work is to leverage the fact that full supervision is not needed to acquire unbiased stochastic gradients, and perform stochastic gradient descent.

The following summarizes our contributions. 1. First, we introduce the “active labeling” problem, which is a relevant theoretical framework that encompasses many useful problems encountered by practitioners trying to annotate their data in the most eﬃcient fashion, as well as its streaming variation, in order to deal with privacy preserving issues. This is the focus of Section 10.2. 2. Then, in Section 10.3, we give a high-level framework to access unbiased stochastic gradients with weak information only. This provides a simple solution to the streaming “active labeling” problem. 3. Finally, we detail this framework for a robust regression task in Section 10.4, and provide an algorithm whose optimality is proved in Section 10.5. As a proof of concept, we provide numerical simulations in Section 10.6. We conclude with a high-level discussion around our methods in Section 10.7.

Related work. Active query of information is relevant to many settings. The most straightforward applications are searching games, such as Bar Kokhba or twenty questions (Walsorth, 1882). We refer to Pelc

187

<!-- page: 190 -->

(2002) for an in-depth survey of such games, especially when liars introduce uncertainty, and their relations with coding on noisy channels. But applications are much more diverse, e.g. for numerical simulation (Chevalier et al., 2014), database search (Qarabaqi and Riedewald, 2014), or shape recognition (Geman and Jedynak, 1993), to name a few.

In terms of motivations, many streams of research can be related to this problem, such as experimental design (Chernoﬀ, 1959), statistical queries (Kearns, 1998; Fotakis et al., 2021), crowdsourcing (Doan et al., 2011), or aggregation methods in weak supervision (Ratner et al., 2020). More precisely, “active labeling”1 consists in having several inputs and querying partial information on the labels. It is close to active learning (Settles, 2010; Dasgupta, 2011; Hanneke, 2014), where there are several inputs, but exact outputs are queried; and to active ranking (Valiant, 1975; Ailon, 2011; Braverman et al., 2019), where partial information is queried, but there is only one input. The streaming variant introduces privacy preserving constraints, a problem that is usually tackled through the notion of diﬀerential privacy (Dwork et al., 2006).

In terms of formalization, we build on the partial supervision formalization of Cabannes et al. (2020b), which casts weak supervision as sets of label candidates and generalizes semi-supervised learning (Chapelle et al., 2006). Finally, our sequential setting with a unique ﬁnal reward is similar to combinatorial bandits in a pure-exploration setting (Garivier and Kaufmann, 2016; Fiez et al., 2019).

## 10.2 The “active labeling” problem

Supervised learning is traditionally modeled in the following manner. Consider X an input space, Y an output space, ℓ: Y × Y →R a loss function, and 𝜌∈ΔX×Y a joint probability distribution. The goal is to recover the function

$$
𝑓∗∈arg min R( 𝑓) := E(𝑋,𝑌)∼𝜌[ℓ( 𝑓(𝑋),𝑌)], (10.1)
𝑓:X→Y
$$

(10.1)

yet, without accessing 𝜌, but a dataset of independent samples distributed according to 𝜌, D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛∼ 𝜌⊗𝑛. In practice, accessing data comes at a cost, and it is valuable to understand the cheapest way to collect a dataset allowing to discriminate 𝑓∗.

We shall suppose that the input data (𝑋𝑖)𝑖≤𝑛are easy to collect, yet that labeling those inputs to get outputs (𝑌𝑖)𝑖≤𝑛demands a high amount of work. For example, it is relatively easy to scrap the web or medical databases to access radiography images, but labeling them by asking radiologists to recognize tumors on zillions of radiographs will be both time-consuming and expensive. As a consequence, we assume the (𝑋𝑖)𝑖≤𝑛 given but the (𝑌𝑖)𝑖≤𝑛unknown. As getting information on the labels comes at a cost (e.g., paying a pool of label workers, or spending your own time), given a budget constraint, what information should we query on the labels?

To quantify this problem, we will assume that we can sequentially and adaptively query 𝑇information of the type 1𝑌𝑖𝑡∈𝑆𝑡, for any index 𝑖𝑡∈{1, · · · , 𝑛} and any set of labels 𝑆𝑡⊂Y (belonging to a speciﬁed set of subsets of Y). Here, 𝑡∈{1, · · · ,𝑇} indexes the query sequence, and 𝑇∈N is a ﬁxed budget. The goal is to optimize the design of the sequence (𝑖𝑡, 𝑆𝑡) in order to get the best estimate of 𝑓∗in terms of risk minimization (10.1). In the following, we give some examples to make this setting more concrete.

Example 18 (Classiﬁcation with attributes). Suppose that a labeler is asked to provide ﬁne-grained classes on images (Krause et al., 2016; Zheng et al., 2019), such as the label “caracal” in Fig- ure 10.1. This would be diﬃcult for many people. Yet, it is relatively easy to recognize that the image depicts a “feline” with “tufted-ears” and “sandy color”. As such, a labeler can give the weak information that 𝑌belongs to the set “feline”, 𝑆1 = {“cat”, “lion”, “tiger”, . . .}, and the set “tufted ears”, 𝑆2 = {“Great horned owl”, “Aruacana chicken”, . . .}. This is enough to recognize that 𝑌∈𝑆1 ∩𝑆2 = {“caracal”}. The question 1𝑌∈𝑆1, corresponds to asking if the image depicts a feline. Literature on hierarchical classiﬁcation and autonomic taxonomy construction provides interesting ideas for this problem (e.g., Cesa-Bianchi et al., 2006; Gangaputra and Geman, 2006).

Example 19 (Ranking with partial ordering). Consider a problem where for a given input 𝑥, characterizing a user, we are asked to deduce their preferences over 𝑚items. Collecting such a label requires knowing the exact ordering of the 𝑚items induced by a user. This might be hard to ask for. Instead, one can easily ask 1Note that the wording “active labeling” has been more or less used as synonymous of “active learning” (e.g., Wang and Shang, 2014). In contrast, we use “active labeling” to design “active weakly supervised learning”.

<!-- page: 191 -->

[FIGURE: Figure 10.1]

Figure 10.1: Recognizing ﬁne-grained classes is diﬃcult, but recognizing attributes is easy. the user which items they prefer in a collection of a few items. The user’s answer will give weak information about the labels, which can be modeled as knowing 1𝑌𝑖∈𝑆= 1, for 𝑆the set of total orderings that satisfy this partial ordering. We refer the curious reader to active ranking and dueling bandits for additional contents (Jamieson and Nowak, 2011; Bengs et al., 2021).

Example 20 (Pricing a product). Suppose that we want to sell a product to a consumer characterized by some features 𝑥, this consumer is ready to pay a price 𝑦∈R for this product. We price it 𝑓(𝑥) ∈R, and we observe 1 𝑓(𝑥)<𝑦, that is if the consumer is willing to buy this product at this price tag or not (Cesa-Bianchi et al., 2019; Liu et al., 2021). Although, in this setting, the goal is often to minimize the regret, which contrasts with our pure exploration setting.

As a counter-example, our assumptions are not set to deal with missing data, i.e. if some coordinates of some input feature vectors 𝑋𝑖are missing (Rubin, 1976). Typically, this happens when input data comes from diﬀerent sources (e.g., when trying to predict economic growth from country information that is self-reported).

Streaming variation. The special case of the active labeling problem we shall consider consists in its variant without resampling. This corresponds to the online setting where one can only ask one question by sample, formally 𝑖𝑡= 𝑡. This setting is particularly appealing for privacy concerns, in settings where the labels (𝑌𝑖) contain sensitive information that should not be revealed totally. For example, some people might be more comfortable giving a range over a salary rather than the exact value; or in the context of polling, one might not call back a previous respondent characterized by some features 𝑋𝑖to ask them again about their preferences captured by 𝑌𝑖. Similarly, the streaming setting is relevant for web marketing, where inputs model new users visiting a website, queries model sets of advertisements chosen by an advertising company, and one observes potential clicks.

## 10.3 Weak information as stochastic gradients

In this section, we discuss how stochastic gradients can be accessed through weak information.

Suppose that we model 𝑓= 𝑓𝜃for some Hilbert space Θ ∋𝜃. With some abuse of notations, let us denote ℓ(𝑥, 𝑦, 𝜃) := ℓ( 𝑓𝜃(𝑥), 𝑦). We aim to minimize R(𝜃) = E(𝑋,𝑌) [ℓ(𝑋,𝑌, 𝜃)] . Assume that R is diﬀerentiable (or sub-diﬀerentiable) and denote its gradients by ∇𝜃R.

Deﬁnition 89 (Stochastic gradient). A stochastic gradient of R is any random function 𝐺: Θ →Θ such that E[𝐺(𝜃)] = ∇𝜃R(𝜃). Given some step size function 𝛾: N →R∗, a stochastic gradient descent (SGD) is a procedure, (𝜃𝑡) ∈ΘN, initialized with some 𝜃0 and updated as 𝜃𝑡+1 = 𝜃𝑡−𝛾(𝑡)𝐺(𝜃𝑡), where the realization of 𝐺(𝜃𝑡) given 𝜃𝑡is independent of the previous realizations of 𝐺(𝜃𝑠) given 𝜃𝑠.

In supervised learning, SGD is usually performed with the stochastic gradients ∇𝜃ℓ(𝑋,𝑌, 𝜃). More generally, stochastic gradients are given by

$$
𝐺(𝜃) = 1∇𝜃ℓ(𝑋,𝑌,𝜃) ∈𝑇· 𝜏(𝑇), (10.2)
$$

(10.2)

<!-- page: 192 -->

for 𝜏: T →Θ with T ⊂2Θ a set of subsets of Θ, and 𝑇a random variable on T , such that

$$
∀𝜃∈Θ, E𝑇[1𝜃∈𝑇· 𝜏(𝑇)] = 𝜃. (10.3)
$$

(10.3)

Stated otherwise, if you have a way to image a vector 𝜃from partial measurements 1𝜃∈𝑇such that you can reconstruct this vector in a linear fashion (10.3), then it provides you a generic strategy to get an unbiased stochastic estimate of this vector from a partial measurement (10.2).

For 𝜓: Y →Θ a function from Y to Θ (e.g., 𝜓= ∇𝜃(𝑋, ·, 𝜃)), a question 1𝜓(𝑌) ∈𝑇translates into a question 1𝑌∈𝑆for some set 𝑆= 𝜓−1(𝑇) ⊂Y, meaning that the stochastic gradient (10.2) can be evaluated from a single query. As a proof of concept, we derive a generic implementation for 𝑇and 𝜏in Appendix 10.B. This provides a generic SGD scheme to learn functions from weak queries when there are no constraints on the sets to query.

Remark 90 (Cutting plane methods). While we provide here a descent method, one could also develop cutting-plane/ellipsoid methods to localize 𝜃∗according to weak information, which corresponds to the techniques developed for pricing by Cohen et al. (2020) and related literature.

## 10.4 Median regression

In this section, we focus on eﬃciently acquiring weak information providing stochastic gradients for regression problems. In particular, we motivate and detail our methods for the absolute deviation loss.

Motivated by seminal works on censored data (Tobin, 1958), we shall suppose that we query half-spaces. For an output 𝑦∈Y = R𝑚, and any hyper-plane 𝑧+ 𝑢⊥⊂R𝑚for 𝑧∈R𝑚, 𝑢∈S𝑚−1, we can ask a labeler to tell us which half-space 𝑦belongs to. Formally, we access the quantity sign(⟨𝑦−𝑧, 𝑢⟩) for a given unit cost.

Least-squares. For regression problems, it is common to look at the mean square loss

$$
ℓ(𝑋,𝑌, 𝜃) = ∥𝑓𝜃(𝑋) −𝑌∥2 , ∇𝜃ℓ(𝑋,𝑌, 𝜃) = 2( 𝑓𝜃(𝑋) −𝑌)⊤𝐷𝑓𝜃(𝑋),
$$

where 𝐷𝑓𝜃(𝑥) ∈Y ⊗Θ denotes the Jacobian of 𝜃→𝑓𝜃(𝑥). In rich parametric models, it is preferable to ask questions on 𝑌∈Y rather than on gradients in Θ which is a potentially much bigger space. If we assume that 𝑌and 𝑓𝜃(𝑋) are bounded in ℓ2-norm by 𝑀∈R+, we can adapt (10.2) and (10.3) through the fact that for any 𝑧∈Y, such that ∥𝑧∥≤2𝑀, as proven in Appendix 10.B,

$$
1⟨𝑧,𝑈⟩≥𝑉· 𝑈 1⟨𝑒1,𝑈⟩≥𝑉· ⟨𝑒1,𝑈⟩ 
= 𝜋3/2
E𝑈,𝑉 = 𝑐1 · 𝑧, where 𝑐1 = E𝑈,𝑉 2𝑀(𝑚2 + 4𝑚+ 3) ,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

for 𝑈uniform on the sphere S𝑚−1 and 𝑉uniform on [0, 2𝑀]. Applied to 𝑧= 𝑓𝜃(𝑋) −𝑌, it designs an SGD procedure by querying information of the type 1⟨𝑌,𝑈⟩<⟨𝑓𝜃(𝑋),𝑈⟩−𝑉.

A case for median regression. Motivated by robustness purposes, we will rather expand on median regression. In general, we would like to learn a function that, given an input, replicates the output of I/O samples generated by the joint probability 𝜌. In many instances, 𝑋does not characterize all the sources of variations of 𝑌, i.e. input features are not rich enough to characterize a unique output, leading to randomness in the conditional distributions (𝑌|𝑋). When many targets can be linked to a vector 𝑥∈X, how to deﬁne a consensual 𝑓(𝑥)? For analytical reasons, statisticians tend to use the least-squares error which corresponds to asking for 𝑓(𝑥) to be the mean of the distribution (𝑌|𝑋= 𝑥). Yet, means are known to be too sensitive to rare but large outputs (see e.g., Huber, 1981), and cannot be deﬁned as good and robust consensus in a world of heavy-tailed distributions. This contrasts with the median, which, as a consequence, is often much more valuable to summarize a range of values. For instance, median income is preferred over mean income as a population indicator (see e.g., US Census Bureau, 2021).

Median regression. The geometric median is variationally deﬁned through the absolute deviation loss, leading to

$$
𝑓𝜃(𝑋) −𝑌 ∥𝑓𝜃(𝑋) −𝑌∥ ⊤
ℓ(𝑋,𝑌, 𝜃) = ∥𝑓𝜃(𝑋) −𝑌∥, ∇𝜃ℓ(𝑋,𝑌, 𝜃) = 𝐷𝑓𝜃(𝑋). (10.4)
$$

(10.4)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 193 -->

Similarly to the least-squares case, we can access weakly supervised stochastic gradients through the fact that for 𝑧∈S𝑚−1, as shown in Appendix 10.B,

$$
√𝜋Γ( 𝑚−1 2 ) 𝑚Γ( 𝑚 2 ) , (10.5)
$$

(10.5)

E𝑈[sign (⟨𝑧,𝑈⟩) · 𝑈] = 𝑐2 · 𝑧, where 𝑐2 = E𝑈[sign (⟨𝑒1,𝑈⟩) · ⟨𝑒1,𝑈⟩] = where 𝑈is uniformly drawn on the sphere S𝑚−1, and Γ is the gamma function. This suggests Algorithm 2.

Algorithm 2: Median regression with SGD.

Data: A model 𝑓𝜃for 𝜃∈Θ, some data (𝑋𝑖)𝑖≤𝑛, a labeling budget 𝑇, a step size rule 𝛾: N →R+ Result: A learned parameter ˆ𝜃and the predictive function ˆ𝑓= 𝑓ˆ𝜃. Initialize 𝜃0. for 𝑡←1 to 𝑇do Sample 𝑈𝑡uniformly on S𝑚−1. Query 𝜀= sign(⟨𝑌𝑡−𝑧,𝑈𝑡⟩) for 𝑧= 𝑓𝜃𝑡−1(𝑋𝑡). Update the parameter 𝜃𝑡= 𝜃𝑡−1 + 𝛾(𝑡)𝜀· 𝑈⊤

$$
𝑡(𝐷𝑓𝜃𝑡−1 (𝑋𝑡)).
$$

Output ˆ𝜃= 𝜃𝑇, or some average, e.g., ˆ𝜃= 𝑇−1 Í𝑇

$$
𝑡=1 𝜃𝑡.
$$

## 10.5 Statistical analysis

In this section, we quantify the performance of Algorithm 2 by proving optimal rates of convergence when the median regression problem is approached with (reproducing) kernels. For simplicity, we will assume that 𝑓∗can be parametrized by a linear model (potentially of inﬁnite dimension).

Assumption 20. Assume that the solution 𝑓∗: X →R𝑚of the median regression problem (10.1) and (10.4) can be parametrized by some separable Hilbert space H, and a bounded feature map 𝜑: X →H, such that, for any 𝑖∈[𝑚], there exists some 𝜃∗

$$
𝑖∈H such that ⟨𝑓∗(·), 𝑒𝑖⟩Y = 𝜃∗
$$

H , where (𝑒𝑖) is the canonical basis of R𝑚. Written into matrix form, there exists 𝜃∗∈Y ⊗H, such that 𝑓∗(·) = 𝜃∗𝜑(·).

$$
𝑖, 𝜑(·)
$$

The curious reader can easily relax this assumption in the realm of reproducing kernel Hilbert spaces following the work of Pillaud-Vivien et al. (2018a). Under the linear model of Assumption 20, Algorithm 2 is speciﬁed with 𝑢⊤𝐷𝑓𝜃(𝑥) = 𝑢⊗𝜑(𝑥). Note that rather than working with Θ = Y⊗H which is potentially inﬁnite- dimensional, empirical estimates can be represented in the ﬁnite-dimensional space Y ⊗Span {𝜑(𝑋𝑖)}𝑖≤𝑛, and well approximated by small-dimensional spaces to ensure eﬃcient computations (Williams and Seeger, 2000; Meanti et al., 2020). One of the key points of SGD is that gradient descent is so gradual that one can use noisy or stochastic gradients without loosing statistical guarantees while speeding up computations. This is especially true when minimizing convex functions that are nor strongly-convex, i.e., bounded below by a quadratic, nor smooth, i.e., with Lipschitz-continuous gradient (see, e.g., Bubeck, 2015). In particular, the following theorem, proven in Appendix 10.A.1, states that Algorithm 2 minimizes the population risk at a speed at least proportional to 𝑂(𝑇−1/2).

Theorem 20 (Convergence rates). Under Assumption 20, and under the knowledge of 𝜅and 𝑀two real values such that E[∥𝜑(𝑋)∥2] ≤𝜅2 and ∥𝜃∗∥≤𝑀, with a budget 𝑇∈N, a constant step size 𝛾= 𝑀 𝜅

$$
Í𝑇−1 √ 𝑇and
$$

the average estimate ˆ𝜃= 1 𝑡=0 𝜃𝑡, Algorithm 2 leads to an estimate 𝑓that suﬀers from an excess of risk

$$
𝑇
 R 𝑓ˆ𝜃 
−R( 𝑓∗) ≤2𝜅𝑀
E √ ≤𝜅𝑀𝑚3/2𝑇−1/2, (10.6)
𝑐2 𝑇
$$

(10.6)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where the expectation is taken with respect to the randomness of ˆ𝜃that depends on the dataset (𝑋𝑖,𝑌𝑖) as well as the questions (𝑖𝑡, 𝑆𝑡)𝑡≤𝑇.

While we give here a result for a ﬁxed step size, one could retake the extensive literature on SGD to prove similar results for decaying step sizes that do not require to know the labeling budget in advance (e.g. setting 𝛾(𝑡) ∝𝑡−1/2 at the expense of an extra term in log(𝑇) in front of the rates), as well as diﬀerent averaging strategies (see e.g., Bach, 2023). In practice, one might not know a priori the parameter 𝑀but could nonetheless ﬁnd the right scaling for 𝛾based on cross-validation.

<!-- page: 194 -->

The rate in 𝑂(𝑇−1/2) applies more broadly to all the strategies described in Section 10.3 as long as the loss ℓand the parametric model 𝑓𝜃ensure that R(𝜃) is convex and Lipschitz-continuous. Although the constants appearing in front of rates depend on the complexity to reconstruct the full gradient ∇𝜃ℓ( 𝑓𝜃(𝑋𝑖,𝑌𝑖)) from the reconstruction scheme (10.3). Those constants correspond to the second moment of the stochastic gradient. For example, for the least-squares technique described earlier one would have to replace 𝑐2 by 𝑐1 in (10.6).

Theorem 21, proven in Appendix 10.A.3, states that any algorithm that accesses a fully supervised learning dataset of size 𝑇cannot beat the rates in 𝑂(𝑇−1/2), hence any algorithm that collects weaker information on (𝑌𝑖)𝑖≤𝑇cannot display better rates than the ones veriﬁed by Algorithm 2. This proves minimax optimality of our algorithm up to constants.

Theorem 21 (Minimax optimality). Under Assumption 20 and the knowledge of an upper bound on ∥𝜃∗∥≤𝑀, assuming that 𝜑is bounded by 𝜅, there exists a universal constant 𝑐3 such that for any algorithm A that takes as input D𝑇= (𝑋𝑖,𝑌𝑖)𝑖≤𝑇∼𝜌⊗𝑇for any 𝑇∈N and output a parameter 𝜃,

$$
sup 𝜌∈M𝑀 ED𝑇∼𝜌⊗𝑇 R( 𝑓A(D𝑇;𝜌)) −R( 𝑓𝜌; 𝜌) ≥𝑐3𝑀𝜅𝑇−1/2. (10.7)
$$

(10.7)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The supremum over 𝜌∈M𝑀has to be understood as the supremum over all distributions 𝜌∈ΔX×Y such that the problem deﬁned through the risk R( 𝑓; 𝜌) := E𝜌[ℓ( 𝑓(𝑋),𝑌)] is minimized for 𝑓𝜌that veriﬁes Assumption 20 with ∥𝜃∗∥bounded by a constant 𝑀.

The same theorem applies for least-squares with a diﬀerent universal constant. It should be noted that minimax lower bounds are in essence quantifying worst cases of a given class of problems. In particular, to prove Theorem 21, we consider distributions that lead to hard problems; more speciﬁcally, we assumed the variance of the conditional distribution (𝑌| 𝑋) to be high. The practitioner should keep in mind that it is possible to add additional structure on the solution, leverage active learning or semi-supervised strategy such as uncertainty sampling (Nguyen et al., 2021), or Laplacian regularization (Zhu et al., 2003; Cabannes et al., 2021a), and reduce the optimal rates of convergence. To conclude this section, let us remark that most of our derivations could easily be reﬁned for practitioners facing a slightly diﬀerent cost model for annotation. In particular, they might prefer to perform batches of annotations before updating 𝜃rather than modifying the question strategy after each input annotation. This would be similar to mini-batching in gradient descent. Indeed, the dependency of our result on the annotation cost model and on Assumption 20 should not be seen as a limitation but rather as a proof of concept.

## 10.6 Numerical analysis

In this section, we illustrate the diﬀerences between our active method versus a classical passive method, for regression and classiﬁcation problems. Extensive details are provided in Appendix 10.E. Our code is available online at anonymized-url.

Let us begin with the regression problem that consists in estimating the function 𝑓∗that maps 𝑥∈[0, 1] to sin(2𝜋𝑥) ∈R. Such a regular function, which belongs to any Hölder or Sobolev classes of functions, can be estimated with the Gaussian kernel, which would ensure Assumption 20, and that corresponds to a feature map 𝜑such that 𝑘(𝑥, 𝑥′) := ⟨𝜑(𝑥), 𝜑(𝑥′)⟩= exp(−|𝑥−𝑥′| /(2𝜎2)) for any bandwidth parameter 𝜎> 0.2 On Figure 10.2, we focus on estimating 𝑓∗given data (𝑋𝑖)𝑖∈[𝑇] that are uniform on [0, 1] in the noiseless setting where 𝑌𝑖= 𝑓∗(𝑋𝑖), based on the minimization of the absolute deviation loss. The passive baseline consists in randomly choosing a threshold 𝑈𝑖∼N (0, 1) and acquiring the observations (1𝑌𝑖>𝑈𝑖)𝑖∈[𝑇] that can be cast as the observation of the half-space 𝑆𝑖=

$$
𝑦∈Y 1𝑦>𝑈𝑖= 1𝑌𝑖>𝑈𝑖
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

=: 𝑠(𝑌𝑖,𝑈𝑖). In this noiseless setting, a good baseline to learn 𝑓∗from the data (𝑋𝑖, 𝑆𝑖) is provided by the inﬁmum loss characterization (see Cabannes et al., 2020b)

$$
\underset{𝑓:X→Y}{\arg\min}\, \frac{𝑦∈Y}{E(𝑋,𝑆) [inf} 𝑦∈𝑆ℓ( 𝑓(𝑋), 𝑦)],
$$

where the distribution over 𝑋corresponds to the marginal of 𝜌over X, and the distribution over (𝑆| 𝑋= 𝑥) is the pushforward of 𝑈∼N (0, 1) under 𝑠( 𝑓∗(𝑥), ·). The left plot on Figure 10.2 corresponds to an instance 2A noteworthy computational aspect of linear models, often refer as the “kernel trick”, is that the features map 𝜑does not need to be explicit, the knowledge of 𝑘: X × X →R being suﬃcient to compute all quantities of interest (Scholkopf and Smola, 2001). This “trick” can be applied to our algorithms.

<!-- page: 195 -->

of SGD on such an objective based on the data (𝑋𝑖, 𝑆𝑖), while the right plot corresponds to Algorithm 2. We take the same hyperparameters for both plots, a bandwidth 𝜎= 0.2 and an SGD step size 𝛾= 0.3. We refer the curious reader to Figure 10.7 in Appendix 10.E for plots illustrating the streaming history, and to Figure 10.10 for “real-world” experiments. Passive strategy Active strategy Above Below Signal Reconstruction Outputs Outputs Inputs Inputs

[FIGURE: Figure 10.2]

Figure 10.2: Visual comparison of active and passive strategies. Estimation in orange of the original signal 𝑓∗in dashed blue based on median regression in a noiseless setting. Any orange point (𝑥, 𝑢) ∈R2 corresponds to an observation made that 𝑢is below 𝑓∗(𝑥), while a blue point corresponds to 𝑢above 𝑓∗(𝑥). The passive strategy corresponds to acquiring information based on (𝑈| 𝑥) following a normal distribution, while the active strategy corresponds to (𝑢| 𝑥) = 𝑓𝜃(𝑥). The active strategy reconstructs the signal much better given the budget of 𝑇= 30 observations.

To illustrate the versatility of our method, we approach a classiﬁcation problem through the median surrogate technique presented in Proposition 91. To do so, we consider the classiﬁcation problem with 𝑚∈N classes, X = [0, 1] and the conditional distribution (𝑌| 𝑋) linearly interpolating between Dirac in 𝑦1, 𝑦2 and 𝑦3 respectively for 𝑥= 0, 𝑥= 1/2 and 𝑥= 1 and the uniform distribution for 𝑥= 1/4 and 𝑥= 3/4; and 𝑋 uniform on X \ ([1/4 −𝜀, 1/4 + 𝜀] ∪[3/4 −𝜀, 3/4 + 𝜀]).

$$
Regression task Classiﬁcation task
10−1
Risk of ¯θT 10−1 Risk of ¯θT
10−3
10−2 active passive active passive
101 103 101 103
iteration T iteration T
$$

[FIGURE: Figure 10.3]

Figure 10.3: Comparison of generalization errors of passive and active strategies as a function of the annotation budget 𝑇. This error is computed by averaging over 100 trials. In solid is represented the average error, while the height of the dark area represents one standard deviation on each side. In order to consider the streaming setting where 𝑇is not known in advance, we consider the decreasing step size 𝛾(𝑡) = 𝛾0/√𝑡; and to smooth out the stochasticity due to random gradients, we consider the average estimate ¯𝜃𝑡= (𝜃1 + · · · + 𝜃𝑡)/𝑡. The left ﬁgure corresponds to the noiseless regression setting of Figure 10.2, with 𝛾0 = 1. We observe the convergence behavior in 𝑂(𝑇−1/2) of our active strategy. The right setting corresponds to the classiﬁcation problem setting described in the main text with 𝑚= 100, 𝜀= 1/20, and approached with the median surrogate. We observe the exponential convergence phenomenon described by Cabannes et al. (2021c); its kicks in earlier for the active strategy. The two plots are displayed with logarithmic scales on both axes.

<!-- page: 196 -->

## 10.7 Discussion

### 10.7.1 Discrete output problems

Learning problems with discrete output spaces are not as well understood as regression problems. This is a consequence of the complexity of dealing with combinatorial structures in contrast with continuous metric spaces. In particular, gradients are not deﬁned for discrete output models. The current state-of-the-art framework to deal with discrete output problems is to introduce a continuous surrogate problem whose solution can be decoded as a solution on the original problem (Bartlett et al., 2006). For example, one could solve a classiﬁcation task with a median regression surrogate problem, which is the object of the next proposition, proven in Appendix 10.C.

Proposition 91 (Consistency of median surrogate). The classiﬁcation setting where Y is a ﬁnite space, and ℓ: Y × Y →R is the zero-one loss ℓ(𝑦, 𝑧) = 1𝑦≠𝑧can be solved as a regression task through the simplex embedding of Y in RY with the orthonormal basis (𝑒𝑦)𝑦∈Y. More precisely, if 𝑔∗: X →RY is the minimizer of the median surrogate risk R𝑆(𝑔) = E [∥𝑔(𝑋) −𝑒𝑌∥], then 𝑓∗: X →Y deﬁned as 𝑓∗(𝑥) = arg max𝑦∈Y 𝑔∗ 𝑦(𝑥) minimizes the original risk R( 𝑓) = E [ℓ( 𝑓(𝑋),𝑌)].

More generally, any discrete output problem can be solved by reusing the consistent least-squares surrogate of Ciliberto et al. (2020). Algorithm 2 can be adapted to the least-squares problem based on speciﬁcations at the beginning of Section 10.4. This allows using our method in an oﬀ-the-shelve fashion for all discrete output problems. In this setting, Theorem 20 can be reﬁned under margin conditions where our approach would exhibit exponential convergence rates as illustrated on Figure 10.3. As a side note, while we are not aware of any generic theory encompassing the absolute-deviation surrogate of Proposition 91, we showcase its superiority over least-squares on at least two types of problems on Figures 10.4 and 10.5 in Appendix 10.C.

### 10.7.2 Supervised learning baseline with resampling

When resampling is allowed a simple baseline for the active labeling problem is provided by supervised learning. In regression problems with the query of any half-space, a method that consists in annotating each (𝑌𝑖)𝑖≤𝑛(𝑇,𝜀) up to precision 𝜀, before using any supervised learning method to learn 𝑓from (𝑋𝑖,𝑌𝑖)𝑖≤𝑛(𝑇,𝜀) could acquire 𝑛(𝑇, 𝜀) ≃𝑇/𝑚log2(𝜀−1) data points with a dichotomic search along all directions, assuming 𝑌𝑖bounded or sub-Gaussian. In terms of minimax rates, such a procedure cannot perform better than in 𝑛(𝑇, 𝜀)−1/2 + 𝜀, the ﬁrst term being due to the statistical limit in Theorem 21, the second due to the incertitude 𝜀on each 𝑌𝑖that transfers to the same level of incertitude on 𝑓. Optimizing with respect to 𝜀yields a bound in 𝑂(𝑇−1/2 log(𝑇)1/2). Therefore, this not-so-naive baseline is only suboptimal by a factor log(𝑇)1/2. In the meanwhile, Algorithm 2 can be rewritten with resampling, as well as Theorem 20, which we prove in Appendix 10.A.2. Hence, our technique will still achieve minimax optimality for the problem “with resampling”. In other terms, by deciding to acquire more imprecise information, our algorithm reduces annotation cost for a given level of generalization error (or equivalently reduces generalization error for a given annotation budget) by a factor log(𝑇)1/2 when compared to this baseline.

The picture is slightly diﬀerent for discrete-output problems. If one can ask any question 𝑠∈2Y then with a dichotomic search, one can retrieve any label with log2(𝑚) questions. Hence, to theoretically beat the fully supervised baseline with the SGD method described in Section 10.3, one would have to derive a gradient strategy (10.2) with a small enough second moment (e.g., for convex losses that are non-smooth nor strongly convex, the increase in the second moment compared to the usual stochastic gradients should be no greater than log2(𝑚)1/2). How to best reﬁne our technique to better take into account the discrete structure of the output space is an open question. Introducing bias that does not modify convergence properties while reducing variance eventually thanks to importance sampling is a potential way to approach this problem. A simpler idea would be to remember information of the type 𝑌𝑖∈𝑠to restrict the questions asked in order to locate 𝑓𝜃𝑡(𝑋𝑖) −𝑌𝑖when performing stochastic gradient descent with resampling. Combinatorial bandits might also provide helpful insights on the matter. Ultimately, we would like to build an understanding of the whole distribution (𝑌| 𝑋) and not only of 𝑓∗(𝑋) as we explore labels in order to reﬁne this exploration.

<!-- page: 197 -->

### 10.7.3 Min-max approaches

Min-max approaches have been popularized for searching games and active learning, where one searches for the question that minimizes the size of the space where a potential guess could lie under the worst possible answer to that question. A particularly well illustrative example is the solution of the Mastermind game proposed by Knuth (1977). While our work leverages plain SGD, one could build on the vector ﬁeld point-of-view of gradient descent (see, e.g., Bubeck, 2015) to tackle min-max convex concave problems with similar guarantees. In particular, we could design weakly supervised losses 𝐿( 𝑓(𝑥), 𝑠; 1𝑦∈𝑠) and min-max games where a prediction player aims at minimizing such a loss with respect to the prediction 𝑓, while the query player aims at maximizing it with respect to the question 𝑠, that is querying information that best elicit mistakes made by the prediction player. For example, the dual norm characterization of the norm leads to the following min-max approach to the median regression

$$
arg min R( 𝑓) = arg min max 𝑈∈(S𝑚−1)X×Y E(𝑋,𝑌)∼𝜌[⟨𝑈(𝑥, 𝑦), 𝑓(𝑥) −𝑦⟩] .
𝑓:X→Y 𝑓:X→Y
$$

Such min-max formulations would be of interest if they lead to improvement of computational and statistical eﬃciencies, similarly to the work of Babichev et al. (2019). For classiﬁcation problems, the following proposition introduces such a game and suggests its suitability. Its proof can be found in Appendix 10.D.

Proposition 92. Consider the classiﬁcation problem of learning 𝑓∗: X →Y where Y is of ﬁnite cardinality, with the 0-1 loss ℓ(𝑧, 𝑦) = 1𝑧≠𝑦, minimizing the risk (10.1) under a distribution 𝜌on X × Y. Introduce the surrogate score functions 𝑔: X →ΔY; 𝑥→𝑣where 𝑣= (𝑣𝑦)𝑦∈Y is a family of non-negative weights that sum to one, as well as the surrogate loss function 𝐿: ΔY × S × {−1, 1} →R; (𝑣, 𝑆, 𝜀) = 𝜀(1 −2 Í 𝑦∈𝑆𝑣𝑦), and the min-max game

$$
min 𝑔:X→ΔY max 𝜇:X→ΔS E(𝑋,𝑌)∼𝜌E𝑆∼𝜇(𝑥) [𝐿(𝑔(𝑥), 𝑆; 1𝑌∈𝑆−1𝑌∉𝑆)] . (10.8)
$$

(10.8)

When S contains the singletons and with the low-noise condition that P (𝑌≠𝑓∗(𝑥) | 𝑋= 𝑥) < 1/2 almost everywhere, then 𝑓∗can be learned through the relation 𝑓∗(𝑥) = arg min𝑦∈Y 𝑔∗(𝑥)𝑦for the unique minimizer 𝑔∗of (10.8). Moreover, the minimization of the empirical version of this objective with the stochastic gradient updates for saddle point problems provides a natural “active labeling” scheme to ﬁnd this 𝑔∗.

## 10.8 Conclusion

We have introduced the “active labeling” problem, which corresponds to “active partially supervised learning”. We provided a solution to this problem based on stochastic gradient descent. Although our method can be used for any discrete output problem, we detailed how it works for median regression, where we show that it optimizes the generalization error for a given annotation budget. In a near future, we would like to focus on better exploiting the discrete structure of classiﬁcation problems, eventually with resampling strategies.

Understanding more precisely the key issues in applications concerned with privacy, and studying how weak gradients might provide a good trade-oﬀbetween learning eﬃciently and revealing too much information also provide interesting follow-ups. Finally, regarding dataset annotation, exploring diﬀerent paradigms of weakly supervised learning would lead to diﬀerent active weakly supervised learning frameworks. While this work is based on partial labeling, similar formalization could be made based on other weak supervision models, such as aggregation (e.g., Ratner et al., 2020), or group statistics (Dietterich et al., 1997). In particular, annotating a huge dataset is often done by bagging inputs according to predicted labels and correcting errors that can be spotted on those bags of inputs (Deng et al., 2009). We left for future work the study of variants of the “active labeling” problem that model those settings.

<!-- page: 198 -->

<!-- page: 199 -->

# Appendix

## 10.A Proofs of the statistical analysis

In the following proofs, we assume X to be Polish and Y = R𝑚, so to deﬁne the joint probability 𝜌∈ΔX×Y. Moreover, we assume that E[∥𝑌∥] < +∞in order to deﬁne the risk of median regression. We consider H to be a Hilbert space that is separable (i.e. only the origin is in all the neighborhood of the origin), and 𝜑to be a measurable mapping from X to H.

In terms of notations, we denote {1, 2, · · · , 𝑛} by [𝑛] for any 𝑛∈N∗, and by (𝑥𝑖)𝑖≤𝑛the family (𝑥1, · · · , 𝑥𝑛) for any sequence (𝑥𝑖). The unit sphere in R𝑚is denoted by S𝑚−1. The symbol ⊗denotes tensors, and is extended to product measures in the notation 𝜌⊗𝑛= 𝜌× 𝜌× · · · × 𝜌. We have used the isometry between trace-class linear mappings from H to Y and the tensor space Y ⊗H, which generalizes the matrix representation of linear map between two ﬁnite-dimensional vector spaces. This space inherits from the Hilbertian structure of H and Y and we denote by ∥·∥the Hilbertian norm that generalizes the Frobenius norm on linear maps between Euclidean spaces.

### 10.A.1 Upper bound for stochastic gradient descent

This subsection is devoted to the proof of Theorem 20. For simplicity, we will work with the rescaled step size 𝛾𝑡:= 𝑐2𝛾(𝑡) rather than the step size described in the main text 𝛾(𝑡).

Convergence of stochastic gradient descent for non-smooth problems is a known result. For completeness, we reproduce and adapt a usual proof to our setting. For 𝑡∈N, let us introduce the random functions

$$
R𝑡(𝜃) = 𝑐−1 2 |⟨𝜃𝜑(𝑋𝑡) −𝑌𝑡,𝑈𝑡⟩| , where 𝑐2 = E𝑈[|⟨𝑒1,𝑈⟩|] = E𝑈[sign(⟨𝑒1,𝑈⟩) ⟨𝑒1,𝑈⟩]
$$

for (𝑋𝑡,𝑌𝑡) ∼𝜌, 𝑈𝑡uniform on the sphere S𝑚−1 ⊂Y. Those random functions all average to R(𝜃) = E𝜌E𝑈[𝑐−1 2 |⟨𝜃𝜑(𝑋) −𝑌,𝑈⟩|] = E𝜌[∥𝜃𝜑(𝑋) −𝑌∥]. After a random initialization 𝜃0 ∈Θ, the stochastic gradient update rule can be written for any 𝑡∈N as

$$
𝜃𝑡+1 = 𝜃𝑡−𝛾𝑡∇R𝑡(𝜃𝑡),
$$

where ∇R𝑡denotes any sub-gradients of R𝑡. We can compute

$$
∇R𝑡(𝜃𝑡) = 𝑐−1 2 ∇|⟨𝜃𝜑(𝑋𝑡) −𝑌𝑡,𝑈𝑡⟩| = 𝑐−1 2 sign (⟨𝜃𝜑(𝑋𝑡) −𝑌𝑡,𝑈𝑡⟩) 𝑈𝑡⊗𝜑(𝑋𝑡).
$$

This corresponds to the gradient written in Algorithm 2.

Let us now express the recurrence relation on ∥𝜃𝑡+1 −𝜃∗∥. We have

$$
∥𝜃𝑡+1 −𝜃∗∥2 = ∥𝜃𝑡−𝛾𝑡∇R𝑡(𝜃𝑡) −𝜃∗∥2
= ∥𝜃𝑡−𝜃∗∥2 + 𝛾2 𝑡∥∇R𝑡(𝜃𝑡)∥2 −2𝛾𝑡⟨∇R𝑡(𝜃𝑡), 𝜃𝑡−𝜃∗⟩.
$$

Because R𝑡is convex, it is above its tangents

$$
R𝑡(𝜃∗) ≥R𝑡(𝜃𝑡) + ⟨∇R𝑡(𝜃𝑡), 𝜃∗−𝜃𝑡⟩.
$$

Hence,

$$
∥𝜃𝑡+1 −𝜃∗∥2 ≤∥𝜃𝑡−𝜃∗∥2 + 𝛾2 𝑡∥∇R𝑡(𝜃𝑡)∥2 + 2𝛾𝑡(R𝑡(𝜃∗) −R𝑡(𝜃𝑡)).
197
$$

<!-- page: 200 -->

This allows bounding the excess of risk as

$$
2(R𝑡(𝜃𝑡) −R𝑡(𝜃∗)) ≤1 𝛾𝑡
(∥𝜃𝑡−𝜃∗∥2 −∥𝜃𝑡+1 −𝜃∗∥2) + 𝛾𝑡𝑐−2 2 ∥𝜑(𝑋𝑡)∥2 .
$$

where we used the fact that ∥∇R𝑡∥= 𝑐−1 2 ∥𝜑(𝑋𝑡)∥. Let us multiply this inequality by 𝜂𝑡> 0 and sum from 𝑡= 0 to 𝑡= 𝑇−1, we get

$$
𝑇−1 ∑︁ 𝑇−1 ∑︁ 𝑇−1 ∑︁ 𝑇−1 ∑︁
𝜂𝑡 𝛾𝑡 (∥𝜃𝑡−𝜃∗∥2 −∥𝜃𝑡+1 −𝜃∗∥2) + 𝜂𝑡𝛾𝑡𝑐−2 2 ∥𝜑(𝑋𝑡)∥2
2( 𝜂𝑡R𝑡(𝜃𝑡) − 𝜂𝑡R𝑡(𝜃∗)) ≤
𝑡=0 𝑡=0 𝑡=0 𝜂𝑡 𝑡=0
𝑇−1 ∑︁ 𝑇−1 ∑︁
= 𝜂0 ∥𝜃0 −𝜃∗∥2 −𝜂𝑇−1 ∥𝜃𝑇−𝜃∗∥2 + −𝜂𝑡−1 ∥𝜃𝑡−𝜃∗∥2 + 𝜂𝑡𝛾𝑡𝑐−2 2 ∥𝜑(𝑋𝑡)∥2 .
𝛾0 𝛾𝑇−1 𝛾𝑡 𝛾𝑡−1
𝑡=1 𝑡=0
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

From here, there is several options to obtain a convergence result, either one assume ∥𝜃𝑡−𝜃∗∥bounded and take 𝜂𝑡𝛾𝑡−1 ≥𝜂𝑡−1𝛾𝑡; or one take 𝜂𝑡= 𝛾𝑡but at the price of paying an extra log(𝑇) factor in the bound; or one take 𝛾𝑡and 𝜂𝑡independent of 𝑡. Since we suppose the annotation budget given, we will choose 𝛾𝑡and 𝜂𝑡 independent of 𝑡, only depending on 𝑇.

$$
𝑇−1 ∑︁ 𝑇−1 ∑︁ 𝑇−1 ∑︁
𝜂R𝑡(𝜃∗)) ≤𝜂 𝛾∥𝜃0 −𝜃∗∥2 + 𝜂𝛾𝑐−2 2 ∥𝜑(𝑋𝑡)∥2 .
2( 𝜂R𝑡(𝜃𝑡) −
𝑡=0 𝑡=0 𝑡=0
$$

Let now take the expectation with respect to all the random variables, for the risk

$$
𝜃𝑡 
E(𝑋𝑠,𝑌𝑠,𝑈𝑠)𝑠≤𝑡[R𝑡(𝜃𝑡)] = E(𝑋𝑠,𝑌𝑠,𝑈𝑠)𝑠≤𝑡 E(𝑋𝑡,𝑌𝑡) E𝑈𝑡[R𝑡(𝜃𝑡) | 𝜃𝑡]
= E(𝑋𝑠,𝑌𝑠,𝑈𝑠)𝑠≤𝑡[R(𝜃𝑡)] = E[R(𝜃𝑡)].
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

For the variance, E[∥𝜑(𝑋𝑠)∥2] = E[∥𝜑(𝑋)∥2] = 𝜅2.

Let us ﬁx 𝑇and consider 𝜂𝑡= 1/𝑇, by Jensen we can bound the following averaging

$$
𝑇−1 ∑︁ ! ! 𝑇−1 ∑︁ ! "𝑇−1 ∑︁ #
2 R 𝜂𝑡𝜃𝑡 −R(𝜃∗) ≤2 𝜂𝑡R (𝜃𝑡) −R(𝜃∗) = 2 E 𝜂𝑡(R𝑡(𝜃𝑡) −R𝑡(𝜃∗))
𝑡=0 𝑡=0 𝑡=0
≤1
𝑇𝛾∥𝜃0 −𝜃∗∥2 + 𝛾𝑐−2 2 𝜅2.
$$

Initializing 𝜃0 to zero, we can optimize the resulting quantity to get the desired result.

### 10.A.2 Upper bound for resampling strategy

For resampling strategies, the proof is built on classical statistical learning theory considerations. Let us decompose the risk between estimation and optimization errors. Recall the expression of the risk R, the function taking as inputs measurable functions from X to Y and outputting a real number

$$
R( 𝑓) = E𝜌[∥𝑓(𝑋) −𝑌∥].
$$

Let us denote by F the class of functions from X to Y we are going to work with. Let 𝑓𝑛be our estimate of 𝑓∗which maps almost every 𝑥∈X to the geometric median of (𝑌| 𝑋). Denote by R∗ D𝑛the best value that can be achieved by our class of functions to minimize the empirical average absolute deviation

$$
R∗ D𝑛= inf 𝑓∈F RD𝑛( 𝑓).
$$

Assumption 20 states that we have a well-speciﬁed model F to estimate the median, i.e. 𝑓∗∈F. Hence, the excess of risk can be decomposed as an estimation and an optimization error, without approximation error (it is not diﬃcult to add an approximation error, but it will make the derivations longer and the convergence rates harder to parse for the reader). Using the fact that RD𝑛( 𝑓∗) ≥R∗ D𝑛by deﬁnition of the inﬁmum, we have

$$
R( 𝑓𝑛) −R( 𝑓∗) ≤R( 𝑓𝑛) −RD𝑛( 𝑓𝑛) + RD𝑛( 𝑓∗) −R( 𝑓∗) + RD𝑛( 𝑓𝑛) −R∗ . (10.9)
| {z } D𝑛 | {z }
estimation error optimization error
$$

(10.9)

<!-- page: 201 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 199 Estimation error. Let us begin by controlling the estimation error. We have two terms in it. RD𝑛( 𝑓∗) − R( 𝑓∗) can be controlled with a concentration inequality on the empirical average of ∥𝑓∗(𝑋) −𝑌∥around its population mean. Assuming sub-Gaussian moments of 𝑌, it can be done with Bernstein inequality.

RD𝑛( 𝑓𝑛) −R( 𝑓𝑛) is harder to control as 𝑓𝑛depends on D𝑛, so we can not use the same technique. The classical technique consists in going for the brutal uniform majoration,

$$
R( 𝑓) −RD𝑛( 𝑓) , (10.10)
R( 𝑓𝑛) −RD𝑛( 𝑓𝑛) ≤sup
𝑓∈F
$$

(10.10)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where F denotes the set of functions that 𝑓𝑛could be in concordance with our algorithm. While this bound could seem highly suboptimal, when the class of functions is well-behaved, we can indeed control the deviation R( 𝑓) −RD𝑛( 𝑓) uniformly over this class without losing much (indeed for any class of functions, it is possible to build some really adversarial distribution 𝜌so that this supremum behaves similarly to the concentration we are looking for (Vapnik, 1995; Anthony and Bartlett, 1999)). This is particularly the case for our model linked with Assumption 20. Expectations of supremum processes have been extensively studied, allowing to get satisfying upper bounds (note that when the ∥𝑓(𝑋) −𝑌∥is bounded, deviation of the quantity of interest around its expectation can be controlled through McDiarmid inequality). In the statistical learning literature, it is usual to proceed with Rademacher complexity.

Lemma 93 (Uniform control of functions deviation with Rademacher complexity). The expectation of the excess of risk can be bounded as

$$
" # " #
 R( 𝑓) −RD𝑛( 𝑓) 
1 2 ED𝑛 ≤R𝑛(F, ℓ, 𝜌) := 1
sup 𝑓∈F 𝑛ED𝑛,(𝜎𝑖) sup 𝑓∈F 𝜎𝑖ℓ( 𝑓(𝑋𝑖),𝑌𝑖) , (10.11)
$$

(10.11)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where (𝜎𝑖)𝑖≤𝑛is deﬁned as a family of Bernoulli independent variables taking value one or minus one with equal probability, and R𝑛(F, ℓ, 𝜌) is called Rademacher complexity.

Proof. This results from the reduction to larger supremum and a symmetrization trick,

$$
" # " #
 R( 𝑓) −RD𝑛( 𝑓) ED′𝑛RD′𝑛( 𝑓) −RD𝑛( 𝑓) 
ED𝑛 sup 𝑓∈F = ED𝑛 sup 𝑓∈F
" #
 RD′𝑛( 𝑓) −RD𝑛( 𝑓) 
≤ED𝑛ED′𝑛 sup 𝑓∈F
" !#
𝑛 ∑︁
1 𝑛
= E(𝑋𝑖,𝑌𝑖),(𝑋′ sup 𝑓∈F ℓ( 𝑓(𝑋′ 𝑖),𝑌′ 𝑖) −ℓ( 𝑓(𝑋𝑖),𝑌𝑖)
𝑖,𝑌′ 𝑖)
" 𝑖=1 !#
𝑛 ∑︁ ℓ( 𝑓(𝑋′ 𝑖) −ℓ( 𝑓(𝑋𝑖),𝑌𝑖) 
1 𝑛
= E(𝑋𝑖,𝑌𝑖),(𝑋′ sup 𝑓∈F 𝜎𝑖 𝑖),𝑌′
𝑖,𝑌′ 𝑖),(𝜎𝑖)
" 𝑖=1 !#
𝑛 ∑︁
1 𝑛
≤2 E(𝑋𝑖,𝑌𝑖),(𝜎𝑖) sup 𝑓∈F 𝜎𝑖(ℓ( 𝑓(𝑋𝑖),𝑌𝑖)) ,
𝑖=1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

which ends the proof. □ In our case, we want to compute the Rademacher complexity for ℓgiven by the norm of Y, and F = {𝑥→𝜃𝜑(𝑥) | 𝜃∈Y ⊗H, ∥𝜃∥< 𝑀}, for 𝑀> 0 a parameter to specify in order to make sure that ∥𝜃∗∥< 𝑀, where the norm has to be understood as the ℓ2-product norm on Y ⊗H ≃H𝑚. Working with linear models and Lipschitz losses is a well-known setting, allowing to derive directly the following bound.

Lemma 94 (Rademacher complexity of linear models with Lipschitz losses). The complexity of the linear class of vector-valued function F = {𝑥→𝜃𝜑(𝑥) | 𝜃∈Y ⊗H, ∥𝜃∥< 𝑀} is bounded as

$$
" !#
𝑛 ∑︁
1 𝑛
E(𝜎𝑖) sup 𝑓∈F 𝜎𝑖∥𝑓(𝑥𝑖) −𝑦𝑖∥ ≤𝑀𝜅𝑛−1/2. (10.12)
𝑖=1
$$

(10.12)

<!-- page: 202 -->

Proof. This proposition is usually split in two. First using the fact that the composition of a space of functions with a Lipschitz function does not increase the entropy of the subsequent space (Vitushkin, 1954). Then bounding the Rademacher complexity of linear models. We refer to Maurer (2016) for a self-contained proof of this result (stated in its Section 4.3). □ Adding all the pieces together we have proven the following proposition, using the fact that the previous bound also applies to sup 𝑓∈F RD𝑛( 𝑓) −R( 𝑓) by symmetry, hence it can be used for the deviation of RD𝑛( 𝑓∗) −R( 𝑓∗).

Proposition 95 (Control of the estimation error). Under Assumption 20, with the model of computation F = {𝑥∈X →𝜃𝜑(𝑥) ∈Y | ∥𝜃∥≤𝑀}, the generalization error of 𝑓𝑛is controlled by a term in 𝑛−1/2 plus an optimization error on the empirical risk minimization

$$
h i
ED𝑛[R( 𝑓𝑛) −R( 𝑓∗)] ≤4𝑀𝜅
𝑛1/2 + ED𝑛 RD𝑛( 𝑓𝑛) −R∗ , (10.13)
D𝑛
$$

(10.13)

as long as 𝑓∗∈F.

Note that this result can be reﬁned using regularized risk (Sridharan et al., 2008), which would be useful under richer (stronger or weaker) source assumptions (e.g., Caponnetto and De Vito, 2006). Such a reﬁnement would allow switching from a constraint ∥𝜃∥< 𝑀to deﬁne F to a regularization parameter 𝜆∥𝜃∥2 added in the risk without restrictions on ∥𝜃∥, which would be better aligned with the current practice of machine learning. Under Assumption 20, this will not fundamentally change the result. The estimation error can be controlled with the derivation in Appendix 10.A.1, where stochastic gradients correspond to random sampling of a coeﬃcient 𝑖𝑡≤𝑛plus the choice of a random 𝑈𝑡. For the option without resampling, there exists an acceleration scheme speciﬁc to diﬀerent losses in order to beneﬁt from the strong convexity (e.g., Bach and Moulines, 2013).

### 10.A.3 Lower bound

In this section, we prove Theorem 21. Let us consider any algorithm A : ∪𝑛∈N(X × Y)𝑛→Θ that matches a dataset D𝑛to an estimate 𝜃D𝑛∈Θ. Let us consider jointly a distribution 𝜌and a parameter 𝜃such that Assumption 20 holds, that is 𝑓𝜌:= arg min 𝑓:X→Y E𝜌[ℓ( 𝑓(𝑋),𝑌)] = 𝑓𝜃. We are interested in characterizing for each algorithm the worst excess of risk it can achieve with respect to an adversarial distribution. The best worst performance that can be achieved by algorithms matching datasets to parameter can be written as

$$
ED𝑛∼𝜌⊗𝑛 
E = inf A sup 𝜃∈Θ,𝜌∈ΔX×Y; 𝑓𝜌= 𝑓𝜃 E(𝑋,𝑌)∼𝜌 ℓ( 𝑓A(D𝑛) (𝑋),𝑌) −ℓ( 𝑓𝜃(𝑋),𝑌) . (10.14)
$$

(10.14)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This provides a lower bound to upper bounds such as (10.6) that can be derived for any algorithm. There are many ways to get lower bounds on this quantity. Ultimately, we want to quantify the best certainty one can have on an estimate 𝜃based on some observations (𝑋𝑖,𝑌𝑖)𝑖≤𝑛. In particular, the algorithms A can be seen as rules to discriminate a model 𝜃from observations D𝑛made under 𝜌𝜃, and where the error is measured through the excess of risk R( 𝑓ˆ𝜃, 𝜌𝜃) −R( 𝑓𝜃; 𝜌𝜃) where R( 𝑓; 𝜌) = E𝜌[ℓ( 𝑓(𝑋),𝑌)] and 𝜌𝜃is a distribution parametrized by 𝜃such that 𝑓𝜃= 𝑓𝜌.

Let us ﬁrst characterize the measure of error. Surprisingly, when in presence of Gaussian noise or uniform noise, the excess of risk behaves like a quadratic metric between parameters.

Lemma 96 (Quadratic behavior of the median regression excess of risk with Gaussian noise). Consider the random variable 𝑌∼N (𝜇, 𝜎2𝐼𝑚), denote by ˆ𝜇an estimate of 𝜇, the excess of risk can be developed as

$$
∥ˆ𝜇−𝜇∥3 
EN (𝜇,𝜎2𝐼𝑚) [∥ˆ𝜇−𝑌∥−∥𝜇−𝑌∥] = 𝑐4 ∥ˆ𝜇−𝜇∥2
𝜎 + 𝑜 , (10.15)
𝜎2
2 )/(2 √
$$

(10.15)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝑐4 = Γ( 𝑚+1

$$
2Γ( 𝑚+2 2 )) ≥(𝑚+ 2)−1/2/2.
$$

Proof. With this speciﬁc noise model, one can do the following derivations.

$$
ˆ𝜇−𝜇
EN (𝜇,𝜎2𝐼𝑚) [∥ˆ𝜇−𝑌∥] = EN (0,𝐼𝑚) [∥ˆ𝜇−𝜇−𝜎𝑌∥] = 𝜎EN (0,𝐼𝑚) 𝜎 −𝑌 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 203 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 201 . It can be expressed through the generalized Laguerre functions, which allows us to get the following Taylor expansion

$$
\frac{ˆ𝜇−𝜇}{𝜎}
$$

We recognize the mean of a non-central 𝜒-distribution of parameter 𝑘= 𝑚and 𝜆=

$$
𝜎
 
√𝜋𝜎 √ −∥ˆ𝜇−𝜇∥2
( 𝑚−2 2 )
EN (𝜇,𝜎2𝐼𝑚) [∥ˆ𝜇−𝑌∥] = 2 𝐿
1 2 2𝜎2
 2 (0) ∥ˆ𝜇−𝜇∥3 
√𝜋𝜎 √ 1 2 (0) + ∥ˆ𝜇−𝜇∥2
( 𝑚−2 2 ) ( 𝑚 2 )
= 𝐿 2𝜎2 𝐿 + 𝑜 .
2 −1 𝜎2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Hence, the following expression of the excess of risk,

$$
2 (0) + 𝑜 ∥ˆ𝜇−𝜇∥3 
√𝜋∥ˆ𝜇−𝜇∥2
EN (𝜇,𝜎2𝐼𝑚) [∥ˆ𝜇−𝑌∥−∥𝜇−𝑌∥] = ( 𝑚 2 )
2 √ 2𝜎 𝐿
−1 𝜎2
 ∥ˆ𝜇−𝜇∥3 
= Γ( 𝑚+1 2 ) ∥ˆ𝜇−𝜇∥2
2 √ 2Γ( 𝑚+2 2 )𝜎 + 𝑜 .
𝜎2
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Note that in dimension one, the calculation can be done explicitly by computing integrals with the error function.

$$
ˆ𝜇−𝜇 
𝑌−ˆ𝜇−𝜇
EN (𝜇,𝜎2) [∥ˆ𝜇−𝑌∥] = 𝜎EN (0,1) 𝜎 + 21𝑌< ˆ𝜇−𝜇 𝜎 −𝑌
h 𝜎 i h i
= 𝜇−ˆ𝜇+ 2( ˆ𝜇−𝜇) EN (0,1) 1𝑌< ˆ𝜇−𝜇 𝜎 −2𝜎EN (0,1) 𝑌1𝑌< ˆ𝜇−𝜇
 1 2 + 1 2 erf ˆ𝜇−𝜇 √ ∫ ˆ𝜇−𝜇 𝜎
√
2𝜎 √𝜋 𝑦𝑒−𝑦2
= 𝜇−ˆ𝜇+ 2( ˆ𝜇−𝜇) 𝜎 2 d𝑦
−
 ˆ𝜇−𝜇 √ 2𝜎
√ −∞
2𝜎 √𝜋𝑒−( ˆ𝜇−𝜇)2
= ( ˆ𝜇−𝜇) erf − 2𝜎2 ,
2𝜎
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where we used the error function, which is the symmetric function deﬁned for 𝑥∈R+ as

$$
∫𝑥 ∫√
erf(𝑥) = 2 √𝜋 0 𝑒−𝑡2 d𝑡= 2 √ 0 𝑒−𝑢2 2𝑥
2 d𝑢= 2 EN (0,1) [10≤𝑌≤ √ 2𝑥].
2𝜋
$$

Developing those two functions in the Taylor series leads to the same quadratic behavior. □ Let us now add a context variable.

Lemma 97 (Reduction to least-squares). For Y = R𝑚, there exists a 𝜎𝑚> 0, such that if 𝜑is bounded by 𝜅, and 𝑓∗belongs to the class of functions F = {𝑥→𝜃𝜑(𝑥) | 𝜃∈Y ⊗H, ∥𝜃∥≤𝑀}, and the conditional distribution are distributed as (𝑌| 𝑋) ∼N ( 𝑓∗(𝑥), 𝜎2𝐼𝑚), with 𝜎> 2𝑀𝜅𝜎𝑚,

$$
𝑐4 ∥𝑓−𝑓∗∥2
∀𝑓∈F, R( 𝑓) −R( 𝑓∗) ≥ 𝐿2(𝜌X ) 2𝜎 . (10.16)
$$

(10.16)

Proof. According to the precedent lemma, there exists 𝜎𝑚such that ∥ˆ𝜇−𝜇∥𝜎−1 ≤𝜎−1

$$
𝑚leads to3
EN (𝜇,𝜎2𝐼𝑚) [∥ˆ𝜇−𝑌∥−∥𝜇−𝑌∥] ≥𝑐4 ∥ˆ𝜇−𝜇∥2
2𝜎 .
$$

Let 𝑓and 𝑓∗∈F be parametrized by 𝜃and 𝜃∗. For a given 𝑥, setting ˆ𝜇= 𝑓𝜃(𝑥) = 𝜃𝜑(𝑥) and 𝜇= 𝑓𝜃∗(𝑥), we get that, using the operator norm,

$$
∥ˆ𝜇−𝜇∥= ∥(𝜃−𝜃∗)𝜑(𝑥)∥≤∥𝜃−𝜃∗∥op ∥𝜑(𝑥)∥≤∥𝜃−𝜃∗∥∥𝜑(𝑥)∥≤2𝑀𝜅.
$$

Hence, as soon as 2𝑀𝜅≤𝜎𝜎−1 𝑚, we have that for almost all 𝑥∈X

$$
E𝑌[∥𝑓(𝑋) −𝑌∥−∥𝑓∗(𝑋) −𝑌∥| 𝑋= 𝑥] ≥𝑐4 ∥𝑓(𝑋) −𝑓∗(𝑋)∥2
2𝜎 .
$$

The result follows from integration over X. □ 3This best value for 𝜎𝑚can be derived by studying the Laguerre function, which we will not do in this paper.

<!-- page: 204 -->

We now have a characterization of the excess of risk that will allow us to reuse lower bounds for least-squares regression. We will follow the exposition of Bach (2023) that we reproduce and comment here for completeness. It is based on the generalized Fano’s method (Ibragimov and Khas’minskii, 1977; Birgé, 1983). Learnability over a class of functions depends on the size of this class of functions. For least-squares regression with a Hilbert class of functions, the right notion of size is given by the Kolmogorov entropy. Let us call 𝜀-packing of F with a metric 𝑑any family ( 𝑓𝑖)𝑖≤𝑁∈F 𝑁such that 𝑑( 𝑓𝑖, 𝑓𝑗) > 𝜀. The logarithm of the maximum cardinality of an 𝜀-packing deﬁnes the 𝜀-capacity of the class of functions F. We refer the interested reader to Theorem 6 in Kolmogorov and Tikhomirov (1959) to make a link between the notions of capacity and entropy of a space. To be perfectly rigorous, the least-squares error in not a norm on the space of 𝐿2 functions, but we will call it a quasi-distance as it veriﬁes symmetry, positive deﬁniteness and the inequality 𝑑(𝑥, 𝑦) ≤𝐾(𝑑(𝑥, 𝑧) + 𝑑(𝑧, 𝑦)) for 𝐾≥1. Let us deﬁne an 𝜀-packing with respect to a quasi-distance similarly as before.

The 𝜀-capacity of a space F gives a lower bound on the number of information to transmit in order to recover a function in F up to precision 𝜀. We will leverage this fact in order to show our lower bound. Let us ﬁrst reduce the problem to a statistical test.

Lemma 98 (Reduction to statistical testing). Let us consider a class of functions F and an 𝜀-packing ( 𝑓𝑖)𝑖≤𝑁 of F with respect to a quasi-distance 𝑑(·, ·) verifying the triangular inequality up to a multiplicative factor 𝐾. Then the minimax optimality of an algorithm A that takes as input the dataset D𝑛= (𝑋𝑖,𝑌𝑖)𝑖≤𝑛and output a function in F can be related to the minimax optimality of an algorithm C that takes an input the dataset D𝑛 and output an index 𝑗∈[𝑚] through

$$
ED𝑛∼𝜌⊗𝑛 𝑑 𝑓A(D𝑛), 𝑓𝜌 
≥ 𝜀 2𝐾inf C sup 𝑖∈[𝑁]
inf A sup PD𝑛∼(𝜌𝑖)⊗𝑛(C(D𝑛) ≠𝑖) , (10.17)
𝜌
$$

(10.17)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where the supremum over 𝜌has to be understood as taken over all measures whose marginals can be written N ( 𝑓∗(𝑥), 𝜎) for 𝜎bigger than a threshold 𝜎𝑚and 𝑓∗∈F, and the supremum over 𝜌𝑖taken over the same type of measures with 𝑓∗∈( 𝑓𝑖)𝑖≤𝑁.

Proof. Consider an algorithm A that takes as input a dataset D𝑛= (𝑋𝑗,𝑌𝑗) 𝑗≤𝑛and output a function 𝑓∈F. We would like to see A as deriving from a classiﬁcation rule and relate the classiﬁcation and regression errors. The natural classiﬁcation rule associated with the algorithm A can be deﬁned through 𝜋the projection from F to [𝑁] that minimizes 𝑑 𝑓, 𝑓𝜋( 𝑓) . The classiﬁcation error and regression error made by 𝜋◦A can be related thanks to the 𝜀-packing property. For any index 𝑗∈[𝑁]

$$
𝑑 𝑓𝜋◦A(D𝑛), 𝑓𝑗 ≥𝜀1𝜋◦A(D𝑛)≠𝑗.
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The error made by 𝑓A(D𝑛) relates to the one made by 𝑓𝜋◦A(D𝑛) thanks to the modiﬁed triangular inequality, using the deﬁnition of the projection

$$
𝑑 𝑓𝜋◦A(D𝑛), 𝑓𝑗 ≤𝐾 𝑑 𝑓𝜋◦A(D𝑛), 𝑓A(D𝑛) + 𝑑 𝑓A(D𝑛), 𝑓𝑗 ≤2𝐾𝑑 𝑓A(D𝑛), 𝑓𝑗 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Finally,

$$
𝑑 𝑓A(D𝑛), 𝑓𝑗 ≥ \frac{𝜀}{2𝐾1𝜋◦A(D𝑛)≠𝑗.}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Assuming that the data were generated by a 𝜌𝑖and taking the expectation, the supremum over 𝜌𝑖and the inﬁmum over A leads to

$$
𝑑 𝑓A(D𝑛), 𝑓𝑖 
≥ 𝜀 2𝐾 inf C=𝜋◦A sup
inf A sup ED𝑛∼𝜌⊗𝑛 PD𝑛∼𝜌⊗𝑛 𝑖 (C(D𝑛) ≠𝑖) .
𝜌𝑖 𝑖 (𝜌𝑖)
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Because 𝜋◦A are part of classiﬁcation rules (indeed it parametrizes all the classiﬁcation rules, simply consider A that matches a dataset to one of the functions ( 𝑓𝑖)𝑖≤𝑁), and because the distributions 𝜌𝑖are part of the distributions 𝜌deﬁned in the lemma, this last equation implies the stated result. □ One of the harshest inequalities in the last proof is due to the usage of the 𝜀-packing condition without considering error made by 𝑑 𝑓𝜋◦A(D𝑛), 𝑓𝑗 that might be much worse than 𝜀. We will later add a condition on the 𝜀-packings to ensure that the ( 𝑓𝑖) are not too far from each other. This will not be a major problem when considering small balls in big dimension spaces.

<!-- page: 205 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 203 Results from statistical testing In this section, we expand on lower bounds for statistical testing. We refer the curious reader to Cover and Thomas (1991). We begin by relaxing the supremum by an average

$$
𝑁 ∑︁
inf C sup 𝑖∈[𝑁] PD𝑛∼(𝜌𝑖)⊗𝑛(C(D𝑛) ≠𝑖) = inf C sup 𝑝𝑖PD𝑛∼(𝜌𝑖)⊗𝑛(C(D𝑛) ≠𝑖) (10.18)
𝑝∈Δ𝑁 𝑖=1
𝑁 ∑︁
1 𝑁
≥inf PD𝑛∼(𝜌𝑖)⊗𝑛(C(D𝑛) ≠𝑖) . (10.19)
C 𝑖=1
$$

(10.19)

The last quantity can be seen as the best measure of error that can be achieved by a decoder C of a signal 𝑖∈[𝑁] based on noisy observations D𝑛of the signal. A lower bound on such a similar quantity is the object of Fano’s inequality (Fano, 1968).

Lemma 99 (Fano’s inequality). Let (𝑋,𝑌) be a couple of random variables in X × Y with X, Y ﬁnite, and ˆ𝑋: Y →X be a classiﬁcation rule. Then, the error 𝑒= 𝑒(𝑋,𝑌) = 1𝑋≠ˆ𝑋(𝑌) veriﬁes

$$
𝐻(𝑋| 𝑌) ≤𝐻(𝑒) + P(𝑒) log(|X | −1) ≤log(2) + P(𝑒) log(|X |).
$$

Where for (𝑋,𝑌) ∈ΔX×Y, 𝐻(𝑋) and 𝐻(𝑋| 𝑌) denotes the entropy and conditional entropy, deﬁned as, with the convention 0 log 0 = 0,

$$
∑︁
𝐻(𝑋) = − P(𝑋= 𝑥) log(P(𝑋= 𝑥)),
𝑥∈X ∑︁
𝐻(𝑋| 𝑌) = − P(𝑋= 𝑥,𝑌= 𝑦) log(P (𝑋= 𝑥| 𝑌= 𝑦)).
𝑥∈X,𝑦∈Y
$$

Proof. This lemma is actually the result of two properties. The ﬁrst part of the proof is due to some manipulation of the entropy, consisting in showing that

$$
𝐻 𝑋 ˆ𝑋(𝑌) ≤𝐻(𝑒) + P(𝑒) log(|X | −1). (10.20)
$$

(10.20)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let us ﬁrst recall the following additive property of entropy

$$
∑︁
𝐻(𝑋,𝑌| 𝑍) = − P(𝑋= 𝑥,𝑌= 𝑦, 𝑍= 𝑧) log(P (𝑋= 𝑥,𝑌= 𝑦| 𝑍= 𝑧))
𝑥∈X,𝑦∈Y,𝑧∈Z ∑︁
= − P(𝑋= 𝑥,𝑌= 𝑦, 𝑍= 𝑧) log(P (𝑌= 𝑦| 𝑋= 𝑥, 𝑍= 𝑧))
𝑥∈X,𝑦∈Y,𝑧∈Z ∑︁
− P(𝑋= 𝑥,𝑌= 𝑦, 𝑍= 𝑧) log(P (𝑋= 𝑥| 𝑍= 𝑧))
𝑥∈X,𝑦∈Y,𝑧∈Z
= 𝐻(𝑌| 𝑋, 𝑍) + 𝐻(𝑋| 𝑍) .
$$

Using this chain rule, we get

$$
𝐻 𝑒, 𝑋 \frac{ˆ𝑋 = 𝐻 𝑒}{= 𝐻 𝑋} 𝑋, ˆ𝑋 + 𝐻 𝑋 ˆ𝑋 𝑒, ˆ𝑋 + 𝐻 𝑒 ˆ𝑋 𝑋, ˆ𝑋 = 0,
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Because 𝑒is a function of ˆ𝑋and 𝑋one can check that 𝐻𝑒

$$
𝐻 𝑒 𝑋, ˆ𝑋 = − ∑︁ P(𝑋, ˆ𝑋) P 𝑒 𝑋, ˆ𝑋 log(P 𝑒 𝑋, ˆ𝑋 )
𝑒,𝑋, ˆ𝑋 ∑︁ ∑︁
= − P(𝑋, ˆ𝑋)1𝑒=1𝑋≠ˆ𝑋log(1𝑒=1𝑋≠ˆ𝑋) = − P(𝑋, ˆ𝑋) · 0 = 0.
𝑒,𝑋, ˆ𝑋 𝑒,𝑋, ˆ𝑋
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 206 -->

Using Jensen inequality for the logarithm, we get

$$
𝐻 𝑋 𝑒, ˆ𝑋 = − ∑︁ P(𝑋, 𝑒, ˆ𝑋) log(P 𝑋 𝑒, ˆ𝑋 )
∑︁ 𝑋,𝑒, ˆ𝑋 P(𝑋= 𝑥, 𝑒= 0, ˆ𝑋= 𝑥′) log(P 𝑋= 𝑥 𝑒= 0, ˆ𝑋= 𝑥′ )
= −
𝑥,𝑥′ −P(𝑋= 𝑥, 𝑒= 1, ˆ𝑋= 𝑥′) log(P 𝑋= 𝑥 𝑒= 1, ˆ𝑋= 𝑥′ )
∑︁ P 𝑋= 𝑥, ˆ𝑋= 𝑥′ 1𝑥=𝑥′ log(1𝑥=𝑥′)
= −
𝑥,𝑥′ −P(𝑒= 1)1𝑥≠𝑥′ P(𝑋= 𝑥, ˆ𝑋= 𝑥′) log(P 𝑋= 𝑥 ˆ𝑋= 𝑥′ )
!
∑︁ ∑︁ P 𝑋= 𝑥 ˆ𝑋= 𝑥′ log
1 P 𝑋= 𝑥 ˆ𝑋= 𝑥′ 
= P(𝑒= 1) P( ˆ𝑋= 𝑥′)
𝑥′ 𝑥≠𝑥′ ∑︁ !
∑︁ P 𝑋= 𝑥 ˆ𝑋= 𝑥′ 1 P 𝑋= 𝑥
P( ˆ𝑋= 𝑥′) log ˆ𝑋= 𝑥′ 
≤P(𝑒= 1)
𝑥′ 𝑥≠𝑥′
= P(𝑒= 1) log(|X | −1).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Using that conditioning reduces the entropy, which follows again from Jensen inequality,

$$
∑︁ P (𝑋= 𝑥| 𝑌= 𝑦) 
𝐻(𝑋) −𝐻(𝑋| 𝑌) = P(𝑋= 𝑥,𝑌= 𝑦) log
P (𝑋= 𝑥)
𝑥,𝑦 ∑︁ P (𝑋= 𝑥) P (𝑌= 𝑦) 
= − P(𝑋= 𝑥,𝑌= 𝑦) log
P (𝑋= 𝑥,𝑌= 𝑦)
𝑥,𝑦 ∑︁ !
P(𝑋= 𝑥,𝑌= 𝑦) P (𝑋= 𝑥) P (𝑌= 𝑦)
≥−log = 0,
P (𝑋= 𝑥,𝑌= 𝑦)
𝑥,𝑦
ˆ𝑋 ≤𝐻(𝑒) ≤log(2).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

we get

$$
𝐻 𝑒
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Hence, we have proven that

$$
𝐻 𝑋 ˆ𝑋 ≤P(𝑒= 1) log(|X | −1) + 𝐻(𝑒).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The rest of the proof follows from the so-called data processing inequality, that is

$$
𝐻 𝑋 ˆ𝑋(𝑌) ≥𝐻(𝑋| 𝑌) . (10.21)
$$

(10.21)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We will not derive it here, since it will not be used in the following. □ In our case, a slight modiﬁcation of the proof of Fano’s inequality leads to the following Proposition.

Lemma 100 (Generalized Fano’s method). For any family of distributions (𝜌𝑖)𝑖≤𝑁on X × Y with 𝑁∈N∗, any classiﬁcation rule C : D𝑛→[𝑁] cannot beat the following average lower bound

$$
𝑁 ∑︁ ∑︁ 𝐾 𝜌𝑖 | 𝜌𝑗 , (10.22)
1 𝑁 𝑖(C(D𝑛) ≠𝑖) log(𝑁−1) ≥log(𝑁) −log(2) −𝑛
inf PD𝑛∼𝜌⊗𝑛
𝑁2
C 𝑖=1
𝑖,𝑗∈[𝑁]
$$

(10.22)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝐾(𝑝|| 𝑞) is the Kullback-Leibler divergence deﬁned for any measure 𝑝absolutely continuous with respect to a measure 𝑞as

$$
𝐾(𝑝|| 𝑞) = E𝑋∼𝑞 −log \frac{ d𝑝(𝑋)}{d𝑞(𝑋)} .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. Let us consider the joint variable (𝑋,𝑌) where 𝑋is a uniform variable on [𝑁] and (𝑌| 𝑋) is distributed according to 𝜌⊗𝑛 𝑋. For any classiﬁcation rule ˆ𝑋: D𝑛→[𝑁], using (10.20) we get

$$
𝑁 ∑︁ ˆ𝑋(D𝑛) ≠𝑖 = P( ˆ𝑋≠𝑋) log(𝑁−1) ≥𝐻 𝑋 ˆ𝑋 −log(2).
1 𝑁
PD𝑛∼𝜌⊗𝑛
𝑖=1 𝑖
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 207 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 205

$$
ˆ𝑋
$$

𝑋 with similar ideas to the data processing inequality. First of all, using the chain rule for entropy

$$
We should work on 𝐻 𝑋
𝐻 𝑋 ˆ𝑋 = 𝐻(𝑋, ˆ𝑋) −𝐻( ˆ𝑋) = 𝐻(𝑋) + (𝐻(𝑋, ˆ𝑋) −𝐻(𝑋) −𝐻( ˆ𝑋)) = log(𝑁) −𝐼(𝑋, ˆ𝑋),
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝐼is the mutual information deﬁned as, for 𝑋and 𝑍discrete

$$
∑︁ P(𝑋= 𝑥, 𝑍= 𝑧) 
𝐼(𝑋, 𝑍) = 𝐻(𝑋) + 𝐻(𝑍) −𝐻(𝑋, 𝑍) = P (𝑋= 𝑥, 𝑍= 𝑧) log
P(𝑋= 𝑥) P(𝑍= 𝑧)
∑︁ ∑︁ 𝑥,𝑧 P (𝑍= 𝑧| 𝑋= 𝑥)) 
= P(𝑋= 𝑥) P (𝑍= 𝑧| 𝑋= 𝑥) log .
P(𝑍= 𝑧)
𝑥 𝑧
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Similarly, one can deﬁne the mutual information for continuous variables. In particular, we are interested in the case where 𝑋is discrete and 𝑌is continuous, denote by 𝜇Y the marginal of (𝑋,𝑌) over 𝑌and by 𝜇|𝑥the conditional (𝑌| 𝑋= 𝑥).

$$
∑︁ ∫ 𝜇|𝑥(d𝑦) 
𝐼(𝑋,𝑌) = P(𝑋= 𝑥) 𝜇|𝑥(d𝑦) log .
𝜇(d𝑦)
𝑥 𝑦
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Let us show the following version of the data processing inequality

$$
𝐼(𝑋, ˆ𝑋(𝑌)) ≤𝐼(𝑋,𝑌). (10.23)
$$

(10.23)

To do so, we will use the conditional independence of 𝑋and ˆ𝑋given 𝑌, which leads to

$$
∫
P 𝑋= 𝑥 ˆ𝑋= 𝑥′ = P (𝑋= 𝑥| 𝑌= d𝑦) P 𝑌= d𝑦 ˆ𝑋= 𝑧 
∫ P(𝑋= 𝑥)𝜇|𝑥(d𝑦)
𝜇(d𝑦) P 𝑌= d𝑦 ˆ𝑋= 𝑧 .
=
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Hence, using Jensen inequality,

$$
𝐼(𝑋, ˆ𝑋) = 𝐻(𝑋) −𝐻 𝑋 ˆ𝑋 
∑︁ ∑︁ P(𝑋= 𝑥) log(P 𝑋= 𝑥 ˆ𝑋= 𝑧 )
= 𝐻(𝑋) + P( ˆ𝑋= 𝑧)
∑︁ 𝑧 ∑︁ 𝑥 ∫ P(𝑋= 𝑥)𝜇|𝑥(d𝑦) ˆ𝑋= 𝑧 
𝜇(d𝑦) P 𝑌= d𝑦
= 𝐻(𝑋) + P( ˆ𝑋= 𝑧) P(𝑋= 𝑥) log
∑︁ 𝑧 ∑︁ 𝑥 ∫ P(𝑋= 𝑥)𝜇|𝑥(d𝑦) 
P 𝑌= d𝑦 ˆ𝑋= 𝑧 log
P( ˆ𝑋= 𝑧) P(𝑋= 𝑥)
≤𝐻(𝑋) +
𝜇(d𝑦)
∑︁ 𝑧 ∫ 𝑥 P(𝑋= 𝑥)𝜇|𝑥(d𝑦) 
= 𝐻(𝑋) + P(𝑋= 𝑥) 𝜇(d𝑦) log
𝜇(d𝑦)
∑︁ 𝑥 ∫ P(𝑋= 𝑥)𝜇|𝑥(d𝑦) 
= P(𝑋= 𝑥) 𝜇(d𝑦) log −log(𝑃(𝑋= 𝑥)
𝜇(d𝑦)
∑︁ 𝑥 ∫ 𝜇|𝑥(d𝑦) 
= P(𝑋= 𝑥) 𝜇(d𝑦) log
𝜇(d𝑦)
𝑥
= 𝐼(𝑋,𝑌).
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We continue by computing the value of 𝐼(𝑋,𝑌), by deﬁnition and using Jensen inequality, we get

$$
∫ !
∑︁
𝐼(𝑋,𝑌) = 1 𝜌⊗𝑛 𝑖 (dD𝑛)
𝜌⊗𝑛 𝑖 (dD𝑛) log Í
𝑁 1 𝑁 𝑗∈[𝑁] 𝜌⊗𝑛 𝑗(dD𝑛)
D𝑛∼𝜌⊗𝑛 !
𝑖∈[𝑁] ∫ 𝑖
∑︁ ∑︁ ∑︁ | 𝜌⊗𝑛 
≤1 𝑖 (dD𝑛) 1 𝜌⊗𝑛 𝑖 (dD𝑛) = 1
𝜌⊗𝑛 log 𝐾 𝜌⊗𝑛 .
𝑁 𝑁 𝜌⊗𝑛 𝑗(dD𝑛) 𝑁2 𝑖 𝑗
D𝑛∼𝜌⊗𝑛
𝑖∈[𝑁] 𝑖 𝑗∈[𝑁] 𝑖,𝑗∈[𝑁]
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

<!-- page: 208 -->

We conclude from the fact that for 𝑝and 𝑞two distributions on a space Z, we have

$$
∫ d𝑝⊗𝑛(𝑧1, · · · , 𝑧𝑛) 
𝐾 𝑝⊗𝑛 | 𝑞⊗𝑛 =
Z𝑛−log 𝑞⊗𝑛(d𝑧1, · · · , d𝑧𝑛)
∫ Î d𝑞⊗𝑛(𝑧1, · · · , 𝑧𝑛) 
𝑖≤𝑛d𝑝(𝑧𝑖) Î
= Z𝑛−log 𝑞⊗𝑛(d𝑧1, · · · , d𝑧𝑛)
∫ 𝑖≤𝑛d𝑞(𝑧𝑖) d𝑝(𝑧𝑖) 
∑︁
= Z𝑛−log 𝑞⊗𝑛(d𝑧1, · · · , d𝑧𝑛)
d𝑞(𝑧𝑖)
∑︁ 𝑖≤𝑛 ∫ d𝑝(𝑧𝑖) 
= −log 𝑞(d𝑧𝑖) = 𝑛𝐾(𝑝|| 𝑞) .
d𝑞(𝑧𝑖)
𝑖≤𝑛 Z
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This explains the result. □ Let us assemble all the results proven thus far. In order to reduce our excess risk to a quadratic metric, we have assumed that the conditional distribution 𝜌𝑖|𝑥to be Gaussian noise. In order to integrate this constraint into the precedent derivations, we leverage the following lemma.

Lemma 101 (Kullback-Leibler divergence with Gaussian noise). If 𝜌𝑖and 𝜌𝑗are two diﬀerent distributions on X × Y such that there marginal over X are equal and the conditional distributions (𝑌| 𝑋= 𝑥) are respectively equal to N ( 𝑓𝑖(𝑥), 𝜎𝐼𝑚) and N ( 𝑓𝑗(𝑥), 𝜎𝐼𝑚), then

$$
𝐾 𝜌𝑖 | 𝜌𝑗 = \frac{1}{2𝜎2} 𝑓𝑖−𝑓𝑗 \frac{2}{𝐿2(𝜌X ) .}
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. We proceed with

$$
∫ " 𝑌−𝑓𝑗(𝑥) 2 #
𝐾 𝜌𝑖 | 𝜌𝑗 = ∥𝑌−𝑓𝑖(𝑥)∥2 −
E𝑌∼N ( 𝑓𝑗(𝑥),𝜎𝐼𝑚) 𝜌𝑗(d𝑥)
2𝜎2
∫ X
 ∥𝑌∥2 ∥𝑌∥2 
E𝑌∼N 𝑓𝑗(𝑥)−𝑓𝑖(𝑥) −E𝑌∼N (0,𝐼𝑚) 𝜌𝑗(d𝑥)
=
X 𝑓𝑗(𝑥) −𝑓𝑖(𝑥) √ 2𝜎 ,𝐼𝑚 2 ! 𝑓𝑗−𝑓𝑖 2
∫
𝜌𝑗(d𝑥) = 𝐿2(𝜌X ) 2𝜎2 ,
= 𝑚+ 2𝜎2 −𝑚
X
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where we have used the fact that the mean of a non-central 𝜒-square variable of parameter (𝑚, 𝜇2) is 𝑚+ 𝜇2. One could also develop the ﬁrst two squared norms and use the fact that for any vector 𝑢∈R𝑚, E[⟨𝑌−𝑓𝑖(𝑥), 𝑢⟩] = 0 to get the result. □ Combining the diﬀerent results leads to the following proposition.

Lemma 102. Under Assumption 20 with F = {𝑥∈X →𝜃𝜑(𝑥) ∈Y | ∥𝜃∥≤𝑀} and 𝜑bounded by 𝜅, for any family ( 𝑓𝑖)𝑖≤𝑁𝜀∈F 𝑁and any 𝜎> 2𝑀𝜅𝜎𝑚

$$
inf A sup ED𝑛∼𝜌⊗𝑛[R( 𝑓A(D𝑛); 𝜌)] −R∗(𝜌)
𝜌 𝑓𝑖−𝑓𝑗 2 𝑓𝑖−𝑓𝑗 2
min𝑖,𝑗∈[𝑁] 𝐿2(𝜌X ) 16(𝑚+ 2)1/2𝜎 ©­ « 1 −log(2) log(𝑁) − 𝑛max𝑖,𝑗∈[𝑁] 𝐿2(𝜌X ) 2𝜎2 log(𝑁) ª® ¬
≥ ,
$$

for any algorithm A that maps a dataset D𝑛∈(X × Y)𝑛to a parameter 𝜃∈Θ.

Covering number for linear model We are left with ﬁnding a good packing of the space induced by Assumption 20. To do so, we shall recall some property of reproducing kernel methods.

<!-- page: 209 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 207 Lemma 103 (Linear models are ellipsoids). For H a separable Hilbert space and 𝜑: X →H bounded, the class of functions F = {𝑥∈X →𝜃𝜑(𝑥) ∈Y | ∥𝜃∥≤𝑀} can be characterized by

$$
𝐾−1/2 𝑓 
F = 𝑓: X →Y 𝐿2(𝜌X ) ≤𝑀 , (10.24)
$$

(10.24)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

where 𝜌X is any distribution on X and 𝐾is the operator on 𝐿2(𝜌X ) that map 𝑓to

$$
𝐾𝑓(𝑥′) = ∫ 𝑥∈X ⟨𝜑(𝑥), 𝜑(𝑥′)⟩𝑓(𝑥)𝜌X (d𝑥),
$$

whose image is assumed to be dense in 𝐿2.

Proof. This follows for isometry between elements in H and elements in 𝐿2. More precisely, let us deﬁne

$$
𝑆: \frac{Y ⊗H}{𝜃} \frac{→}{→} \frac{𝐿2(X, Y, 𝜌X )}{𝑥→𝜃𝜑(𝑥).}
$$

The adjoint of 𝑆is characterized by

$$
𝑆∗: 𝐿2(X, Y, 𝜌X ) → Y ⊗H 𝑓 → E[ 𝑓(𝑥) ⊗𝜑(𝑋)],
$$

which follows from the fact that for 𝜃∈Y ⊗H, 𝑓∈𝐿2 we have

$$
𝑚 ∑︁ ∫
⟨𝜃, 𝑆∗𝑓⟩Y ⊗H = ⟨𝑆𝜃, 𝑓⟩𝐿2 = 𝑓𝑖(𝑥) ⟨𝜃𝑖, 𝜑(𝑥)⟩H 𝜌X (d𝑥)
𝑖=1 X
𝑚 ∑︁
= ⟨𝜃𝑖, E[ 𝑓𝑖(𝑋)𝜑(𝑋)]⟩H = ⟨𝜃, E[ 𝑓(𝑋) ⊗𝜑(𝑋)]⟩Y ⊗H .
𝑖=1
$$

When 𝑆𝑆∗is compact and dense in 𝐿2, we have

$$
∥𝜃∥Y ⊗H = (𝑆𝑆∗)−1/2𝑆𝜃 𝐿2(𝜌X ) .
$$

The compactness allows considering spectral decomposition hence fractional powers. We continue by observing that 𝑆𝑆∗= 𝐾, which follows from

$$
(𝑆𝑆∗𝑓)(𝑥′) = (𝑆E[ 𝑓(𝑋) ⊗𝜑(𝑋)])(𝑥′) = E[ 𝑓(𝑋) ⊗𝜑(𝑋)]𝜑(𝑥′) = E[⟨𝜑(𝑋), 𝜑(𝑥′)⟩𝑓(𝑋)].
$$

The compactness of 𝐾derives from the fact that

$$
∥𝐾𝑓(𝑥′)∥2 = ∥E[⟨𝜑(𝑋), 𝜑(𝑥′)⟩𝑓(𝑋)]∥2 ≤E[∥⟨𝜑(𝑋), 𝜑(𝑥′)⟩𝑓(𝑋)∥2] ≤𝜅2 ∥𝑓∥2
𝐿2 .
$$

Hence, ∥𝐾∥op ≤𝜅2. Indeed, it is not hard to prove that the trace of 𝐾is bounded by 𝑚𝜅2, hence 𝐾is not only compact but trace-class. □ It should be noted that the condition on 𝐾being dense in 𝐿2(𝜌X ) is not restrictive, as indeed all the problem is only seen through the lens of 𝜑and 𝜌X : one can replace X by supp 𝜌X and 𝐿2(𝜌X ) by the closure of the range of 𝐾in 𝐿2(𝜌X ) without modifying nor the analysis, nor the original problem.

$$
𝑓∈𝐿2 ∥𝐾−1/2 𝑓∥𝐿2(𝜌X ) ≤𝑀
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

. It is useful to split the ellipsoid between a projection on a ﬁnite dimensional space that is isomorphic to the Euclidean space R𝑘 We should study packing in the ellipsoid F = and on a residual space 𝑅where the energies (∥𝑓|𝑅∥𝐿2(𝜌X ))2 𝑓∈F are uniformly small. We begin with the following packing lemma, sometimes referred to as Gilbert-Varshamov bound (Gilbert, 1952; Varshamov, 1957) which corresponds to a more generic result in coding theory.

Lemma 104 (ℓ2 2-packing of the hypercube). For any 𝑘∈N∗, there exists a 𝑘/4-packing of the hypercube {0, 1}𝑘, with respect to Hamming distance, of cardinality 𝑁= exp(𝑘/8).

<!-- page: 210 -->

Proof. Let us consider 𝜀> 0, and a maximal 𝜀-packing (𝑥𝑖)𝑖≤𝑁of the hypercube with respect to the distance 𝑑(𝑥, 𝑦) = Í

$$
𝑖∈[𝑘] 1𝑥𝑖≠𝑦𝑖= ∥𝑥−𝑦∥1 = ∥𝑥−𝑦∥2
$$

2. By maximality, we have {0, 1}𝑘⊂∪𝑖∈[𝑁]𝐵𝑑(𝑥𝑖, 𝜀), hence

$$
2𝑘≤𝑁 𝑥∈{0, 1}𝑘 ∥𝑥∥1 ≤𝜀 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This inequality can be rewritten with 𝑍a binomial variable of parameter (𝑘, 1/2) as 1 ≤𝑁P(𝑍≤𝜀). Using Hoeﬀding inequality (Hoeﬀding, 1963), when 𝜀= 𝑘/4 we get

$$
−2𝑘2
𝑁−1 ≤P(𝑍≤𝑘/4) = P(𝑍−E[𝑍] ≤𝑘/4) ≤exp = exp (−𝑘/8) .
42𝑘
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

This is the desired result. □ Lemma 105 (Packing of inﬁnite-dimensional ellipsoids). Let F be the function in 𝐿2(𝜌X ) such that 𝐾−1/2 𝑓 𝐿2(𝜌X ) ≤𝑀for 𝐾a compact operator and 𝑀any positive number. For any 𝑘∈N∗, it is possible to ﬁnd a family of 𝑁≥exp(𝑘/8) elements ( 𝑓𝑖)𝑖∈[𝑁] in F such that for any 𝑖≠𝑗,

$$
𝑓𝑖−𝑓𝑗 2
𝑘𝑀2 Í 𝐿2(𝜌X ) ≤ 4𝑘𝑀2 Í
≤ , (10.25)
𝑖≤𝑘𝜆−1 𝑖≤𝑘𝜆−1
𝑖 𝑖
$$

(10.25)

where (𝜆𝑖)𝑖∈N are the ordered (with repetition) eigenvalues of 𝐾.

Proof. Let us denote by (𝜆𝑖)𝑖∈N the eigenvalues of 𝐾and (𝑢𝑖)𝑖∈N in 𝐿2 the associated eigenvectors. Consider (𝑎𝑠)𝑠∈[𝑁] a 𝑘-packing of the hypercube {−1, 1}𝑘for 𝑁≥exp(𝑘/8) with respect to the ℓ2 2 quasi-distance and deﬁne for any 𝑎∈{𝑎𝑠}

$$
\frac{𝑓𝑎= 𝑀}{𝑐} \sum_{𝑘 𝑠=1} 𝑎𝑖𝑢𝑖,
$$

with 𝑐2 = Í𝑘

$$
𝑖=1 𝜆−1 𝑖. We verify that
𝐾−1/2 𝑓𝑎 𝑘 ∑︁
2 𝐿2 = 𝑀2
𝜆−1 𝑖 = 𝑀2.
𝑐2
𝑖=1
𝑘 ∑︁
𝐿2 = 𝑀2 |𝑎𝑖−𝑏𝑖|2 = 𝑀2 2 ∈𝑀2
∥𝑓𝑎−𝑓𝑏∥2 𝑐2 ∥𝑎𝑖−𝑏𝑖∥2 𝑐2 · [𝑘, 4𝑘].
𝑐2
𝑖=1
$$

This is the object of the lemma. □ So far, we have proven the following lower bound.

Lemma 106. Under Assumption 20 with F = {𝑥∈X →𝜃𝜑(𝑥) ∈Y | ∥𝜃∥≤𝑀} and 𝜑bounded by 𝜅, for any family ( 𝑓𝑖)𝑖≤𝑁𝜀∈F 𝑁and any 𝜎> 2𝑀𝜅𝜎𝑚and 𝑘𝑚> 10,

$$
ED𝑛∼𝜌⊗𝑛[R( 𝑓A(D𝑛); 𝜌)] −R∗(𝜌) ≥ 1 128 min 𝑀2 
𝑖≤𝑘(𝑘𝜆𝑖)−1 , 𝜎𝑘𝑚1/2
inf A sup 𝜎𝑚1/2 Í
,
32𝑛
𝜌
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

for any algorithm A that maps a dataset D𝑛∈(X × Y)𝑛to a parameter 𝜃∈Θ, and where (𝜆𝑖) are the ordered eigenvalue of the operator 𝐾on 𝐿2(X, R, 𝜌X ) that maps any function 𝑓to the function 𝐾𝑓deﬁnes for 𝑥′ ∈X as

$$
∫
(𝐾𝑓)(𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩𝑓(𝑥)𝜌X (d𝑥).
𝑥∈X
$$

In particular, when 𝜆𝑖= 𝜅2𝑖−𝑎/𝜁(𝛼), where 𝜁denotes the Riemann zeta function, we get the following bounds. If we optimize with respect to 𝜎, there exists 𝑛𝛼∈N such that for any 𝑛> 𝑛𝛼.

$$
ED𝑛∼𝜌⊗𝑛[R( 𝑓A(D𝑛); 𝜌)] −R∗(𝜌) ≥ 𝑀𝜅 725𝜁(𝛼)1/2𝑛1/2 . (10.26)
inf A sup
𝜌
$$

(10.26)

If we ﬁx 𝜎= 𝛽𝑀𝜅with 𝛽≥2, and we optimize with respect to 𝑘, there exists a constant 𝑐𝛽and an integer 𝑛0 such that for 𝑛> 𝑛0 we have

$$
ED𝑛∼𝜌⊗𝑛[R( 𝑓A(D𝑛); 𝜌)] −R∗(𝜌) ≥ 𝑀𝜅𝑐𝛽
inf A sup . (10.27)
𝜁(𝛼) 1 1+𝛼𝑛 𝛼 𝛼+1
𝜌
$$

(10.27)

<!-- page: 211 -->

10.A. PROOFS OF THE STATISTICAL ANALYSIS 209 Proof. Reusing Lemma 102, with the same notations, we have the lower bound in

$$
𝑓𝑖−𝑓𝑗 2 𝑓𝑖−𝑓𝑗 2 !
min 1 −log(2) log(𝑁) −𝑛max
2𝜎2 log(𝑁) .
16𝜎(𝑚+ 2)1/2
$$

Let 𝐾and 𝐾Y be the self-adjoint operators on 𝐿2(X, R, 𝜌X ) and 𝐿2(X, Y, 𝜌X ) respectively, both deﬁned through the formula

$$
∫
(𝐾𝑓)(𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩𝑓(𝑥)𝜌X (d𝑥).
$$

When 𝐾is compact, it admits an eigenvalue decomposition 𝐾= Í

$$
𝑥∈X
$$

𝑖∈N 𝜆𝑖𝑢𝑖⊗𝑢𝑖where the equality as to be understood as the convergence of operator with respect to the operator norm based on the 𝐿2-topology. It follows from the product structure of 𝐿2(X, Y, 𝜌X ) ≃𝐿2(X, R, 𝜌X )𝑚that 𝐾Y = Í Í

𝑖∈N,𝑗∈[𝑚] 𝜆𝑖(𝑒𝑖⊗𝑦𝑗) ⊗(𝑒𝑖⊗𝑢𝑗) with (𝑒𝑗) the canonical basis of Y = R𝑚. As a conse- quence, if (𝜆𝑖)𝑖∈N are the ordered eigenvalues of 𝐾then (𝜆⌊𝑖/𝑚⌋) are the ordered eigenvalues of 𝐾Y. Hence, with Lemmas 103 and 105, it is possible to ﬁnd 𝑁= exp(𝑘𝑚/8) functions in F such that 𝑖∈R,𝑗∈[𝑚]

$$
𝑓𝑖−𝑓𝑗 2
𝑘𝑚𝑀2 𝐿2(𝜌X ) ≤ 4𝑘𝑚𝑀2
𝑚Í 𝑚Í
≤ .
𝑖≤𝑘𝜆−1 𝑖≤𝑘𝜆−1
𝑖 𝑖
$$

If we multiply those functions by 𝜂∈[0, 1] we get a lower bound in

$$
𝜂2𝑀2 1 −8 log(2) 𝑘𝑚 − 16𝑀2𝑛𝜂2 𝜎2𝑘𝑚Í
16𝜎(𝑚+ 2)1/2 Í 𝑖≤𝑘(𝑘𝜆𝑖)−1
.
𝑖≤𝑘(𝑘𝜆𝑖)−1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Making sure that the last two terms are smaller than one fourth and one half respectively we get the following conditions on 𝑘and 𝜂, with Λ𝑘= Í

$$
\frac{𝑖≤𝑘(𝑘𝜆𝑖)−1,}{𝑘𝑚≥32 log(2),} 32𝑀2𝑛𝜂2 ≤𝜎2𝑘𝑚Λ𝑘.
$$

Using the fact that 𝜂< 1, the lower bound becomes

$$
= 1 128 min 𝑀2 
𝑀2 1, 𝜎2𝑘𝑚Λ𝑘 32𝑀2𝑛 , 𝜎𝑘𝑚1/2
128𝜎𝑚1/2Λ𝑘 min ,
𝜎𝑚1/2Λ𝑘 32𝑛
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

as long as 𝑘𝑚> 10. When 𝜆−1

$$
𝑖 = 𝑖𝛼𝜁(𝛼)/𝜅2, since Λ𝑘≤𝜆−1
$$

𝑘, we simplify the last expression as

$$
\frac{1}{128 min} 𝜎𝑚1/2𝑘𝛼𝜁(𝛼) , 𝜎𝑘𝑚1/2 𝑀2𝜅2 32𝑛 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Optimizing with respect to 𝜎leads to

$$
\frac{𝜎2 = 32𝑛𝑀2𝜅2}{𝑚𝑘1+𝛼𝜁(𝛼) ≥4𝑀2𝜅2𝜎𝑚.}
$$

This gives

$$
𝑛𝛼,𝑚= 𝑚𝜁(𝛼)𝜎2 𝑚/8.
$$

The dependency of 𝑛𝛼to 𝑚can be removed since any problem with Y = R𝑚can be cast as a problem in R𝑚+1 by adding a spurious coordinate. Taking 𝑘= 1 and 𝑚= 10 leads to the result stated in the lemma. When 𝑛< 𝑛𝛼, one can artiﬁcially multiply the bound by 𝑛1/2 𝛼, since an optimal algorithm can not do better with fewer data. After checking that one can take 𝜎1 ≥1, this leads to a bound in

$$
\frac{𝑀𝜅}{2048𝑛1/2 .}
$$

Optimizing with respect to 𝑘leads to 𝑘𝛼+1 = 32𝑀2𝜅2𝑛/(𝜎2𝑚𝜁(𝛼)) and a bound in

$$
\frac{(𝜎𝑚1/2)}{128(32𝑛)} 𝛼−1 𝛼+1 (𝑀𝜅) 𝛼 𝛼+1 𝜁(𝛼) 2 𝛼+1 1 𝛼+1 .
$$

<!-- page: 212 -->

$$
10𝑚−1, 1
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

The condition 𝑘> min and 𝜎≥2𝑀𝜅𝜎𝑚translates into the condition

$$
4𝑀2𝜅2𝜎2 𝑚≤𝜎2 ≤32𝑀2𝜅2𝑛 1, 𝑚1+𝛼
𝑚𝜁(𝛼) min .
101+𝛼
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

We deduce that 𝜎𝑚= 𝑂(𝑚−1/2), otherwise we would not respect the upper bound derived with Rademacher complexity (or have made a mistake somewhere). Once again we can remove the dependency to 𝑚. Considering 𝜎= 𝛽𝑀𝜅leads to the result stated in the lemma. □ Controlling eigenvalues decay Based on Lemma 106, in order to prove Theorem 21, we only need to show that there exists a mapping 𝜑, an input space X and a distribution 𝜌X such that the integral operator 𝐾introduced in the lemma veriﬁes the assumption on its eigenvalues. Notice that we show in the proof of Lemma 106 that the universal constant 𝑐3 can be taken as 𝑐3 = 2−11.

To proceed, let us consider any inﬁnite dimensional Hilbert space H with a basis (𝑒𝑖)𝑖∈N, X = N and 𝜑: N →H;𝑖→𝜅𝑒𝑖. For 𝑎: N →R we have

$$
∑︁
(𝐾𝑎)(𝑖) = ⟨𝜑(𝑖), 𝜑( 𝑗)⟩𝑎( 𝑗)𝜌( 𝑗) = 𝜅2𝑎(𝑖)𝜌(𝑖).
𝑗∈N
$$

Hence, the eigenvalues of 𝐾are (𝜅2𝜌X (𝑖))𝑖≤𝑛. It suﬃces to consider 𝜌X (𝑖) = 𝑖−𝛼/𝜁(𝛼) to conclude.

The eigenvalue decay in 𝑂(𝑖−𝛼) can also be witnessed in many regression problems. One way to build those cases is to turn a sequence of non-negative real values into a one-periodic function ℎfrom R𝑑to R thanks to the inverse Fourier transform. Using Bochner (1933), one can construct a map 𝜑such that the convolution operator linked with ℎcorresponds to the operator 𝐾. When 𝜌is uniform on [0, 1]𝑑, diagonalizing this convolution operator with the Fourier functions and using the property in Lemma 103 shows that the class of functions F are akin to Sobolev spaces. Similar behavior can be proven when X = R𝑑 and 𝜌X is absolutely continuous with respect to the Lebesgue measure and has bounded density (Widom, 1963). We refer the curious reader to Scholkopf and Smola (2001) or Bach (2023) for details.

## 10.B Unbiased weakly supervised stochastic gradients

In this section, we provide a generic scheme to acquire unbiased weakly supervised stochastic gradients, as well as speciﬁcations of the formula given in the main text for least-squares and median regression.

### 10.B.1 Generic implementation

Suppose that Θ is ﬁnite dimensional, or that it can be approximated by a ﬁnite dimensional space without too much approximation error. For example, in the realm of scalar-valued kernel methods, it is usual to consider either the random ﬁnite dimensional space Span {𝜑(𝑥𝑖)}𝑖≤𝑛for (𝑥𝑖) the data points, or the ﬁnite dimension space linked to the ﬁrst eigenspaces of the operator E[𝜑(𝑋) ⊗𝜑(𝑋)]. In the context of neural networks, the parameter space is always ﬁnite-dimensional.

Suppose also that, given 𝜃, we know an upper bound 𝑀𝜃on the amplitude of ∇𝜃ℓ( 𝑓𝜃(𝑥), 𝑦), or that we know how to handle clipped gradients at amplitude 𝑀𝜃for SGD. Then, similarly to the least-squares method proposed in the main text, we can access weakly supervised gradient through the formula

$$
∇𝜃ℓ( 𝑓𝜃(𝑥), 𝑦) = 2𝑀𝜃(|Θ|2 + 4 |Θ| + 3)
𝜋3/2 E𝑈∼U (𝐵Θ),𝑉∼U ([0,𝑀𝜃]) [1𝑦∈(𝑧→⟨𝑈,∇𝜃ℓ( 𝑓𝜃(𝑥),𝑧)⟩)−1([𝑉,∞))𝑈],
$$

where 𝐵Θ is the unit ball of Θ.

This scheme is really generic, and we do not advocate for it in practice as one may hope to leverage speciﬁc structure of the loss function and the parametric model in a more eﬃcient way. This formula is rather a proof of concept to illustrate that our technique can be applied generically, and is not speciﬁc to least-squares or median regression.

<!-- page: 213 -->

10.B. UNBIASED WEAKLY SUPERVISED STOCHASTIC GRADIENTS 211

### 10.B.2 Speciﬁc implementations

Let us prove the two formulas to get stochastic gradients for both least-squares and median regression. We begin with median regression. Consider 𝑧∈S𝑚−1, and let us denote

$$
𝑥= E𝑈[sign(⟨𝑧,𝑈⟩)𝑈].
$$

The direction 𝑥/∥𝑥∥∈S𝑚−1 is characterized by the argmax over the sphere of the linear form

$$
𝑦→⟨E𝑈[sign(⟨𝑧,𝑈⟩)𝑈], 𝑦⟩= E𝑈[sign(⟨𝑧,𝑈⟩) ⟨𝑈, 𝑦⟩].
$$

This linear form has a unique maximizer on S𝑚−1 and by invariance by symmetry over the axis 𝑧, this maximizer is aligned with 𝑧, hence 𝑥= 𝑐𝑥· 𝑧. We compute the amplitude with the formula, because 𝑧is a unit vector

$$
𝑐𝑥= ⟨𝑥, 𝑧⟩= E𝑈[sign(⟨𝑧,𝑈⟩) ⟨𝑈, 𝑧⟩].
$$

By invariance by rotation of both the uniform distribution and the scalar product, 𝑐𝑥is actually a constant, it is equal to its value 𝑐2 = 𝑐𝑒1.

The same type of reasoning applies for the least-squares case. Consider 𝑧∈R𝑚, and denote

$$
𝑥= E𝑈,𝑉 1⟨𝑧,𝑈⟩≥𝑉· 𝑈 .
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

For the same reasons as before 𝑥= 𝑐𝑥· 𝑢for 𝑢= 𝑧/∥𝑧∥, and 𝑐𝑥veriﬁes

$$
𝑐𝑥= ⟨𝑥, 𝑢⟩= E𝑈,𝑉[1⟨𝑧,𝑈⟩≥𝑉⟨𝑈, 𝑢⟩] = E𝑈[E𝑉[1⟨𝑧,𝑈⟩≥𝑉] ⟨𝑈, 𝑢⟩]
⟨𝑧,𝑈⟩ 𝑀 ⟨𝑈, 𝑢⟩] = ∥𝑧∥ 𝑀E𝑈[1⟨𝑢,𝑈⟩>0 ⟨𝑈, 𝑢⟩2].
= E𝑈[1⟨𝑧,𝑈⟩>0
$$

Hence,

$$
𝑥= 1 𝑀E𝑈[1⟨𝑢,𝑈⟩>0 ⟨𝑈, 𝑢⟩2] · 𝑧= 𝑐1 · 𝑧.
$$

This explains the formula for least-squares.

Lemma 107 (Constant for the uniform strategy). Under the uniform distribution on the sphere

$$
√𝜋Γ( 𝑚−1 √
2 ) 𝑚Γ( 𝑚 2𝜋 𝑚3/2 . (10.28)
𝑐2 = E𝑢∼S𝑚−1 [|⟨𝑢, 𝑒1⟩|] = 2 ) ≥
$$

(10.28)

Proof. Let us compute 𝑐2 = E𝑢∼S𝑚−1 [|⟨𝑢, 𝑒1⟩|]. This constant can be written explicitly as

$$
𝑐2 = ∫ \int_{𝑥∈S𝑚−1 d𝑥}^{𝑥∈S𝑚−1 |𝑥1| d𝑥} .
$$

Remark that for any function 𝑓: R →R, we have

$$
∫ ∫ ∫ 1−𝑥2 1 ·S𝑚−2 d˜𝑥= ∫ ∫
S𝑚−1 𝑓(𝑥1) d𝑥= 𝑓(𝑥1) d𝑥1 𝑓(𝑥1)(1 −𝑥2 1) 𝑚−2 2 d𝑥1 ˜𝑥∈S𝑚−2 d˜𝑥.
˜𝑥∈√
𝑥1∈[−1,1] 𝑥1∈[−1,1]
$$

By denoting 𝑆𝑚the surface of the 𝑚-sphere, the last integral is nothing but 𝑆𝑚−2. By setting 𝑓(𝑥) = 1, we can retrieve by recurrence the expression of 𝑆𝑚. In our case, 𝑓(𝑥) = |𝑥|, so we compute, with 𝑢= 1 −𝑥2

$$
∫ 2 d𝑥1 = 2 ∫ 2 d𝑥1 = ∫1
2 d𝑢= 1 𝑚.
|𝑥1| (1 −𝑥2 1) 𝑚−2 𝑥1(1 −𝑥2 1) 𝑚−2 𝑚−2
𝑢
𝑥1∈[−1,1] 𝑥1∈[0,1] 𝑢=0
$$

This leads to

$$
𝑐2 = \frac{𝑆𝑚−2}{𝑚𝑆𝑚−1} = √𝜋Γ( 𝑚−1 2 ) 𝑚Γ( 𝑚 2 ) .
$$

The ratio 𝑆𝑚−2/𝑆𝑚−1 can be expressed with the integral corresponding to 𝑓= 1, but it is common knowledge that 𝑆𝑚−1 = 2𝜋𝑚/2/Γ(𝑚/2). □

<!-- page: 214 -->

Lemma 108 (Constant for least-squares). Under the uniform distributions on [0, 𝑀] and the sphere

$$
1⟨𝑢,𝑒1⟩>𝑣⟨𝑢, 𝑒1⟩ 
= 𝜋3/2
𝑐1 = E𝑦∼[0,𝑀] E𝑢∼S𝑚−1 𝑀(𝑚2 + 4𝑚+ 3) . (10.29)
$$

(10.29)

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Proof. Similarly to the previous case, this constant can be written explicitly as

$$
∫ ∫ ∫
𝑐1 = 1 𝑥∈S𝑚−1 |𝑥1| 1|𝑥1 |>𝑦d𝑦d𝑥 𝑥∈S𝑚−1 𝑥2 1 d𝑥
𝑦∈[0,𝑀] ∫ 2𝑀 ∫
= .
2 𝑥∈S𝑚−1 d𝑥 𝑥∈S𝑚−1 d𝑥
𝑀
$$

We continue as before with

$$
∫ 2 d𝑥1 = 2 ∫
2 d𝑥= 2𝜋Γ( 𝑚 2 )
|𝑥1|2 (1 −𝑥2 1) 𝑚−2 𝑥2(1 −𝑥2) 𝑚−2
4Γ( 𝑚+3 2 ) .
𝑥1∈[−1,1] 𝑥∈[0,1]
$$

This leads to

$$
√𝜋Γ( 𝑚−1 2 ) = 𝜋3/2Γ( 𝑚−1
𝑐1 = 𝜋Γ( 𝑚 2 ) 2 ) Γ( 𝑚 4𝑀Γ( 𝑚+3 2 ) = 𝜋3/2 2 )
4𝑀Γ( 𝑚+3 2 ) · 𝑀(𝑚2 + 4𝑚+ 3) .
$$

This is the result stated in the lemma. □

## 10.C Median surrogate

Let us begin this section by proving Proposition 91. This result is actually the integration over 𝑥∈X of a pointwise result, so let us ﬁx 𝑥∈X. Consider a probability distribution 𝑝∈ΔY over Y, and its median Θ∗⊂RY deﬁned as the minimizer of R𝑆(𝜃) = E𝑝[∥𝜃−𝑒𝑌∥]. We will to prove that ∪𝜃∈Θ∗arg max𝑦∈Y 𝜃𝑦= arg max𝑦∈Y 𝑝(𝑦).

Let us begin by the inclusion arg max𝑦∈Y 𝑝(𝑦) ⊂∪𝜃∈Θ∗arg max𝑦∈Y 𝜃𝑦. To do so, consider 𝜃∈RY and 𝜎∈SY the transposition of two elements 𝑦and 𝑧in Y. Denote by 𝜃𝜎∈RY, the vector such that (𝜃𝜎)𝑦′ = 𝜃𝜎(𝑦′) for any 𝑦′ ∈Y. We have

$$
∑︁ 𝑝(𝑦′) 

𝜃−𝑒𝑦′

 − 𝜃𝜎−𝑒𝑦′

 
R𝑆(𝜃) −R𝑆(𝜃𝜎) =
𝑦′∈Y
∑︁ √︄∑︁ √︄∑︁
𝑝(𝑦′) ©­ ª® ¬
= 𝜃2 𝑧′ + (1 −𝜃𝑦′)2 −𝜃2 𝑦′ − 𝜃2 𝜎(𝑧′) + (1 −𝜃𝜎(𝑦′))2 −𝜃2
« 𝜎(𝑦′)
𝑦′∈Y 𝑧′∈Y 𝑧′∈Y
√︄∑︁ √︄∑︁
= (𝑝(𝑦) −𝑝(𝑧)) ©­ 𝑧′ + 1 −2𝜃𝑧ª®
𝜃2 𝑧′ + 1 −2𝜃𝑦− 𝜃2 .
« ¬
𝑧′∈Y 𝑧′∈Y
√
$$

<!-- [đọc không chắc: một số ký hiệu dấu ngoặc/độ lớn (delimiter) trong công thức này không trích xuất được chính xác từ lớp văn bản PDF] -->

Because, for any 𝑎∈R+, the function 𝑥→ 𝑎−2𝑥is increasing, if 𝑝(𝑦) > 𝑝(𝑧), then to minimize R, we should make sure that 𝜃𝑦≥𝜃𝑧i. As a consequence, because of symmetry, the modes of 𝑝do correspond to argmax of (𝜃∗ 𝑦)𝑦∈Y for some 𝜃∗∈Θ∗. Let us now prove the second inclusion. To do so, suppose that 𝑝(1) > 𝑝(2), and let us show that 𝜃∗ 1 > 𝜃∗ 2. Let us parametrize 𝜃1 = 𝑎+ 𝜀and 𝜃2 = 𝑎−𝜀for a given 𝑎, and show that 𝜀= 0 is not optimal in order to minimize the risk R𝑆seen as a function of 𝜀. To do so, we can use the Taylor expansion of

$$
√
$$

1 + 𝑥= 1 + 𝑥/2. Hence, with 𝐴= Í 𝑦)2, retaking the last derivations

$$
𝑦>2(𝜃∗
√︁
R𝑆(𝜀) = 𝑝(1) (𝑎+ 𝜀)2 + (𝑎−𝜀)2 + 𝐴+ 1 −2(𝑎+ 𝜀)
√︁
+ 𝑝(2) (𝑎+ 𝜀)2 + (𝑎−𝜀)2 + 𝐴+ 1 −2(𝑎−𝜀)
∑︁ √︃
+ 𝑝(𝑦) (𝑎+ 𝜀)2 + (𝑎−𝜀)2 + 𝐴+ 1 −2𝜃∗𝑦
√︁ 𝑦>2
= 𝑝(1) 2𝑎2 + 2𝜀2 + 𝐴+ 1 −2𝑎−2𝜀
√︁
+ 𝑝(2) 2𝑎2 + 2𝜀2 + 𝐴+ 1 −2𝑎+ 2𝜀+ 𝑐+ 𝑜(𝜀)
= ˜𝑐+ 𝜀 √
2𝑎2 + 𝐴+ 1 −2𝑎 (𝑝(2) −𝑝(1)) + 𝑜(𝜀).
$$

<!-- page: 215 -->

10.C. MEDIAN SURROGATE 213 This shows that taking 𝜃∗ 1 = 𝜃∗ 2, that is 𝜀= 0, is not optimal, hence we have the second inclusion, which ends the proof. Note that we have proven a much stronger result, we have shown that (𝜃𝑦) and 𝑝(𝑦) are order in the exact same fashion (with respect to the strict comparison 𝑝(𝑦) > 𝑝(𝑧) ⇒𝜃∗

$$
𝑦> 𝜃∗ 𝑧for any 𝜃∗∈Θ∗).
$$

### 10.C.1 Discussion around the median surrogate.

The median surrogate have some nice properties for a surrogate method, in particular it does not fully characterize the distribution 𝑝(𝑦) in the sense that there is no one-to-one mapping from 𝑝to 𝜃∗. For example, when Y = {1, 2, 3} if 𝑝(𝑦= 𝑒1), 𝑝(𝑦= 𝑒2), 𝑝(𝑦= 𝑒3) ∝(1, 1, 2 cos(𝜋/6)), then the geometric median correspond to 𝜃∗= 𝑒3. This diﬀers from smooth surrogates, such as logistic regression or least-squares, that implicitly learn the full distribution 𝑝, which should be seen as a waste of resources. Non-smooth surrogates tend to exhibit faster rates of convergence (in terms of decrease of the original risk as a function of the number of samples) than smooth surrogates when rates are derived through calibration inequalities (Nowak-Vila, 2021). It would be nice to derive generic calibration inequality for the median surrogate for multiclass, and see how to derive a median surrogate for more structured problems such as ranking problems.

$$
1 η(x) 1 Least-square bias 1 Median bias
0 0 0
input x −1 input x −1 input x −1
1 Least-square bias 1 Median bias
0 0
input x −1 input x −1
$$

[FIGURE: Figure 10.4]

Figure 10.4: Comparison of least-squares and absolute deviation with noise irregularity for a classiﬁcation problem speciﬁed by X = [0, 3], Y = {−1, 1} with 𝑋uniform on [0, 1] ∪[2, 3] and 𝜂(𝑥) = E {𝑌| 𝑋= 𝑥} speciﬁed on the left ﬁgure. The optimal classiﬁer, with respect to the zero-one loss, 𝑓∗(𝑥) = sign 𝜂takes value one on [0, 1] and value minus one on [2, 3]. The regularized solution are deﬁned as arg min𝑔E[∥⟨𝜑(𝑋), 𝜃⟩−𝑌∥𝑝] + 𝜆∥𝜃∥with 𝑝= 2 for least-squares (middle), and 𝑝= 1 for the median (right). They can be translated into classiﬁers with the decoding 𝑓= sign 𝑔. In this ﬁgure, we choose 𝜑implicitly through the Gaussian kernel 𝑘(𝑥, 𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩= exp(−∥𝑥−𝑥′∥2 /2𝜎2) with 𝜎= .1 which explains the frequency of the observed oscillations, and choose 𝜆= 10−6 (top) and 𝜆= 10−2 (bottom). On the one hand, because the least-squares surrogate is trying to estimate 𝜂it suﬀers from its lack of regularity, leading to Gibbs phenomena that restricts it to be a perfect classiﬁer. On the other hand, the absolute deviation is trying to approach the function 𝑓∗itself, and does not suﬀer from its lack of regularity. In this setting, if we approach the original classiﬁcation problem by minimization of the surrogate empirical risks, and denote by 𝑔𝑛this minimizer and 𝑓𝑛= sign 𝑔𝑛its decoding, 𝑓𝑛obtained through median regression will converge exponentially fast toward 𝑓∗, while 𝑓𝑛obtained through least-squares will never converge to the solution 𝑓∗.

<!-- page: 216 -->

$$
simplex decision frontier η z∗
$$

[FIGURE: Figure 10.5]

Figure 10.5: Comparison of least-squares and median surrogate without context. Consider a context-free classiﬁcation problem that consists in estimating the mode of a distribution 𝑝∈ΔY, or equivalently the minimizer of the 0-1 loss. Such a problem can be visualized on the simplex Δ𝑚where Y = {𝑦1, · · · , 𝑦𝑚} ≃{1, · · · , 𝑚} is mapped to the canonical basis {𝑒𝑖}𝑖∈[𝑚] ∈R𝑚. The ﬁgure illustrates the case 𝑚= 3. The least-squares and median surrogate methods can be understood as working in this simplex, estimating a quantity 𝑧∈ΔY, before performing the decoding 𝑦(𝑧) = arg max𝑦 . Such a decoding partitions the simplex in regions whose frontiers are represented in dashed blue on the ﬁgure. The distribution 𝑝is characterized on the simplex by 𝜂= E𝑌∼𝑝[𝑒𝑌] = arg min E𝑌∼𝑝[∥𝑧−𝑒𝑌∥2]. This quantity 𝜂is exactly the quantity estimated by the least-squares surrogate. The median surrogate searches the minimizer 𝑧∗of the quantity E(𝑧) = E𝑌∼𝑝[∥𝑧−𝑒𝑌∥], whose level lines are represented in solid on the ﬁgure. One of the main advantage of the median surrogate compared to the least-squares one is that 𝑧∗is always farther away from the boundary frontier than 𝜂, meaning that for a similar estimation error on this quantity, the error on the decoding, which corresponds to an estimate of the mode of 𝑝, will be much smaller for the median surrogate. The left ﬁgure represents the case 𝑝= (1, 0, 0), the right ﬁgure the case

$$
𝑝= (.45, .35, .2). 𝑧, 𝑒𝑦
$$

## 10.D Classiﬁcation with a min-max game

In this section, we prove and extend on Proposition 92. First of all, let us consider the average loss, for (𝑣𝑦) ∈RY summing to one

$$
¯𝐿(𝑣, 𝑠) = 1 − \sum_{𝑦∈𝑠} 𝑣𝑦= \sum_{𝑦∉𝑠} 𝑣𝑦.
$$

Consider now this loss conditioned on the observation 1𝑦∈𝑠, we have plenty of characterizations of 𝐿,

$$
∑︁ ∑︁
𝐿(𝑣, 𝑠; 1𝑦∈𝑠−1𝑦∉𝑠) = 1𝑦∈𝑠¯𝐿(𝑣, 𝑠) + 1𝑦∉𝑠¯𝐿(𝑣, Y \ 𝑠) = 1𝑦∈𝑠
𝑣𝑦+ 1𝑦∉𝑠 𝑣𝑦
∑︁ 𝑦∉𝑠 ∑︁ 𝑦∈𝑆
= 1𝑦∈𝑠+ (1𝑦∉𝑠−1𝑦∈𝑠) 𝑣𝑦= 1𝑦∉𝑠+ (1𝑦∈𝑠−1𝑦∉𝑠) 𝑣𝑦
∑︁ 𝑦∈𝑠 ! 𝑦∉𝑠 !
∑︁ 1 −2 ∑︁
= 1 2 −1 2 (1𝑦∈𝑠−1𝑦∉𝑠) = 1 2 + 1 2 (1𝑦∈𝑠−1𝑦∉𝑠)
𝑣𝑦− 𝑣𝑦 𝑣𝑦 .
𝑦∈𝑠 𝑦∉𝑠 𝑦∈𝑠
$$

Minimizing this loss or the loss 2𝐿−1 as deﬁned in Proposition 92 is equivalent.

### 10.D.1 Consistency

Let us consider the loss as deﬁned in this proposition, we have the characterization

$$
∑︁ !
∑︁
𝐿(𝑣, 𝑠; 1𝑦∈𝑠−1𝑦∉𝑠) = (1𝑦∈𝑠−1𝑦∉𝑠) 𝑣𝑦− 𝑣𝑦 .
𝑦∈𝑠 𝑦∉𝑠
$$

Let us rewrite (10.8) based on this previous characterization of the loss, we have

$$
∑︁ !
∑︁
E𝑌[𝐿(𝑣, 𝑠, 1𝑌∈𝑠−1𝑌∉𝑠)] = −(P𝑌(𝑌∈𝑠) −P𝑌(𝑌∉𝑠)) 𝑣𝑦− 𝑣𝑦 .
𝑦∈𝑠 𝑦∉𝑠
$$

<!-- page: 217 -->

10.D. CLASSIFICATION WITH A MIN-MAX GAME 215 \frac{z}{z+u⊥}

[FIGURE: Figure 10.6]

Figure 10.6: Query strategy based on regression surrogate. Retaking the simplex representation of Figure 10.5, the query strategy for classiﬁcation approached with least-squares surrogate or median surrogate consists in looking at the current surrogate estimate 𝑧in the simplex ΔY, taking a random direction 𝑢∈RY and querying sign(⟨𝑒𝑌−𝑧, 𝑢⟩). We see that with three elements, when 𝑌is deterministic, the optimal query strategy consists in considering 𝑠= {𝑦}, while surrogate strategies, such as least-squares and median regression, that learn 𝑧∗= 𝑒𝑦, would only make such a query only two third of the time (which is the ratio of the solid angle of [𝑒2, 𝑒3] from 𝑒1 divided by 𝜋). This shows that those surrogate strategies do not fully leverage the speciﬁc structure of the output.

Hence, without any context variable, the min-max game (10.8) can be rewritten as

$$
∑︁ !
∑︁ ∑︁
min 𝑣∈ΔY max 𝜇∈ΔS − 𝜇𝑠(P𝑌(𝑌∈𝑠) −P𝑌(𝑌∉𝑠)) 𝑣𝑦− 𝑣𝑦 . (10.30)
𝑠∈S 𝑦∈𝑠 𝑦∉𝑠
$$

(10.30)

We will analyze this problem through the lens of a mix-actions zero-sum game. We know from von Neumann and Morgenstern (1944) that a solution to this min-max problem exists, and that one can switch the min-max to a max-min without modifying the value of the solution. Let us denote by (𝑣∗, 𝜇∗) the argument of a solution. To minimize the value of this game, the player 𝑣should play such that

$$
∑︁ ∑︁ ∑︁ ∑︁
sign( 𝑣∗ 𝑦− 𝑣∗ 𝑦) = sign(P(𝑌∈𝑠) −P(𝑌∉𝑠)) = sign( P(𝑌= 𝑦) − P(𝑌= 𝑦)),
𝑦∈𝑠 𝑦∉𝑠 𝑦∈𝑠 𝑦∉𝑠
$$

which allows this player to ensure a negative value to the game. Stated otherwise

$$
∑︁
∀𝑠∈S, P(𝑌∈𝑠) > 1 𝑦≥1
2 ⇒ 𝑣∗ 2. (10.31)
𝑦∈𝑠
$$

(10.31)

As a consequence, if there exists any set such that P(𝑌∈𝑠) = 1/2, the best strategy of player 𝜇is to play only those sets to ensure the value zero, and any 𝑣that satisﬁes (10.31) is optimal. It should be noted that (10.31) does not generally imply that (𝑣𝑦)𝑦∈Y has the same ordering as (P(𝑌= 𝑦))𝑦∈Y.

When {𝑦∗} ∈S and P(𝑌= 𝑦∗) > 1/2, if 𝑣= 𝛿𝑦∗, the prediction player is able to ensure a value of max𝑠∈S −|2 P(𝑌∈𝑠) −1|, which is maximized by the query player with 𝑠= {𝑦∗} ∪𝑠′ for any 𝑠′ such that P(𝑌∈𝑠′) = 0. Other strategies for 𝑣will only increase this value, hence 𝑣∗= 𝛿𝑦∗which implies the ﬁrst part of Proposition 92.

A counter example. While we hope that the solution (𝑣∗, 𝜇∗) does characterize the original solution 𝑦∗, it should be noted that 𝑣∗alone does not characterize 𝑦∗. Indeed, it is even possible to have 𝑣∗uniquely deﬁned without having 𝑦∗= arg max𝑦∈Y 𝑣∗ 𝑦. For example, consider the case where Y = {1, 2, 3} and (P(𝑌= 𝑖))𝑖∈[3] = (.4, .3, .3). By symmetry, the player 𝜇only has to play on S = {{1} , {2} , {3}}, which leads to the min-max game

$$
©­ « 𝜇{1} 𝜇{2} 𝜇{3} ª® ¬ ⊤ ©­ « .2 −.2 −.2 −.4 .4 −.4 −.4 −.4 .4 ª® ¬ ©­ « 𝑣1 𝑣2 𝑣3 ª® ¬
min 𝑣max .
𝜇
$$

The value of this game is −.1 and is achieved for 𝜇∗= (.5, .25, .25), 𝑣∗= (.25, .375, .375).

<!-- page: 218 -->

### 10.D.2 Optimization procedure

Let us rewrite the problem through the objective

$$
E(𝑔, 𝜇) = E(𝑋,𝑦)∼𝜌E𝑆∼𝜇(𝑥) [𝐿(𝑔(𝑋), 𝑆, 1𝑌∈𝑆−1𝑌∉𝑆)].
$$

We want to solve the min-max problem min𝑔max𝜇E(𝑔, 𝜇). This problem can be solved eﬃciently based on the vector ﬁeld point of view of gradient descent (Bubeck, 2015) if:

• we can parametrize the function 𝑔: X →ΔY such that E is convex with respect to the parametrization of 𝑔; • we can access unbiased stochastic gradients of E with respect to 𝑔that have a small second moment; • we can parametrize the function 𝜇: X →ΔS such that E is concave with respect to the parametrization of 𝜇; • we can access unbiased stochastic gradients of E with respect to 𝜇that have a small second moment. The ﬁrst two points are no problems, 𝑔can be parametrized with softmax regression, and since 𝐿is linear with respect to the scores, it will keep the problem convex. Moreover, to access a stochastic gradient of E, one can sample 𝑋𝑖∼𝜌X and 𝑆𝑖∼𝜇(𝑋𝑖) before querying 1𝑌𝑖∈𝑆𝑖and computing the gradient of 𝐿(𝑔(𝑋𝑖), 𝑆𝑖, 1𝑌𝑖∈𝑆𝑖−1𝑌𝑖∉𝑆𝑖) with respect to the parametrization of 𝑔.

The third point is slightly harder to tackle. Since E is linear with respect to 𝜇, one way to proceed is to ﬁnd a linear parametrization of 𝜇. In particular, one can take a family (𝑔𝑖)𝑖∈[𝑁] of linearly independent functions from X to ΔS and search for 𝑔under the form Í 𝑖∈[𝑁] 𝑐𝑖𝑔𝑖for (𝑐𝑖) positive summing to one. To build such a family, one can eventually use “atom functions” and simple operations such as symmetry with respect to Y and S, rescaling, translation, rotations with respect to X. For example if X is a Banach space, one could deﬁne atom functions as, for 𝑦𝑖∈Y

$$
𝑔𝑖: 𝑥→ \frac{∥𝑥∥}{1 + ∥𝑥∥} \frac{1}{|S|} \sum_{𝑠∈S} 𝑒𝑠+ \frac{1}{1 + ∥𝑥∥𝑒{𝑦𝑖}.}
$$

Those functions could be rescaled and translated as 𝑔𝜎,𝜏,𝑖(𝑥) = 𝑔𝑖(𝜎(𝑥−𝜏)), in order to specify a family (𝑔𝜎,𝜏,𝑖) from few values for 𝜏and 𝜎.

The last point is the most diﬃcult one. Without context variables, and with no-parametrization for 𝜇, a naive unbiased gradient strategy for 𝜇consists in asking random questions to update the full knowledge of (P(𝑌∈𝑠))𝑠∈S. But such a strategy will be much worse than our median surrogate technique with queries 1𝑌∈{𝑦} for 𝑦sampled uniformly at random in Y. Eventually, one should go for a biased gradient strategy, while making sure to update 𝜇coherently to avoid getting stalled on bad estimates as a result of biases.

## 10.E Experimental details

Our experiments are done in Python. We leverage the C implementation of high-level array instructions by Harris et al. (2020), as well as the visualization library of Hunter (2007). Randomness in experiments is controlled by choosing explicitly the seed of a pseudo-random number generator.

### 10.E.1 Comparison with fully supervised SGD

In this section, we investigate the diﬀerence between weakly and fully supervised SGD. According to Theorem 20, we only lost a constant factor of order 𝑚3/2 in our rates compared to fully supervised (or plain) SGD. This behavior can be checked by adding the plain SGD curve on Figure 10.3. On the left side of Figure 10.8, we do observe that the risk of both Algorithm 2 and plain SGD decrease with same exponent with respect to number of iteration but with a diﬀerent constant in front of the rates: that is we observe the same slopes on the logarithm scaled plot, but diﬀerent intercepts. Going one step further to check the tightness of our bound, one can plot the intercept, or the error achieved by both Algorithm 2 and plain SGD as a function of the output space dimension 𝑚. The right side of Figure 10.8 shows evidence that this error grows as 𝑚𝜀for some 𝜀∈[1, 3/2], which is coherent with our upper bound. Similarly to Figure 10.3, this ﬁgure was computed after cross validation to ﬁnd the best scaling of the step sizes for each dimension 𝑚.

<!-- page: 219 -->

10.E. EXPERIMENTAL DETAILS 217 T = 1 T = 2 T = 3 T = 4 T = 6 T = 8 T = 12 T = 16 T = 24 T = 32 T = 48 T = 64

[FIGURE: Figure 10.7]

Figure 10.7: Streaming history of the active strategy to reconstruct the signal in dashed blue in the same setting as Figure 10.2. At any time 𝑡, a point 𝑋𝑡is given to us, our current estimate of 𝜃𝑡plotted in dashed orange gives us 𝑧= 𝑓𝜃𝑡(𝑋𝑡), and we query sign(𝑌𝑡−𝑧). Based on the answer to this query, we update 𝜃𝑡to 𝜃𝑡+1 leading to the new estimate of the signal in solid orange. In this ﬁgure, we see that it might be useful for the practitioners in a streaming setting to reduce the bandwidth of 𝜑as they advance in time.

### 10.E.2 Passive strategies for classiﬁcation

A simple passive strategy for classiﬁcation based on median surrogate consists in using the active strategy with coordinates sampling, that is 𝑢being uniform on 

𝑦∈Y, where (𝑒𝑦)𝑦∈Y is the canonical basis of RY used to deﬁne the simplex ΔY as the convex hull of this basis. Querying 1⟨𝑔𝜃(𝑥)−𝑒𝑦,𝑒𝑦⟩>0 is formally equivalent to the query of 1𝑌=𝑦when 𝑔𝜃(𝑥) ∈ΔY. This is the baseline we plot on Figure 10.3.

$$
𝑒𝑦
$$

A more advanced passive baseline is provided by the inﬁmum loss (Cour et al., 2011; Cabannes et al., 2020b). It consists in solving

$$
arg min R𝐼( 𝑓) := E(𝑋,𝑌)∼𝜌E𝑆[𝐿( 𝑓(𝑋), 𝑆, 1𝑌∈𝑆)] ,
𝑓:X→Y
$$

where 𝑆is a random subset of Y and 𝐿is deﬁned from the original loss ℓ: Y × Y →R as, for 𝑧∈Y, 𝑠⊂Y

<!-- page: 220 -->

$$
m=5 Risk as a function of m
101
Algo 1 plain SGD Algo 1 plain SGD
Risk of ¯θ10,000 0.50
Risk of ¯θT
100
0.25
10−1
0.00
101 103 0 20 40 Output space dimension m
iteration T
$$

[FIGURE: Figure 10.8]

Figure 10.8: Comparison of generalization errors of weakly and fully supervised SGD as a function of the annotation budget 𝑇and output space dimension 𝑚. The setting is similar to Figure 10.3. We observe a transitory regime before convergence rates follows the behavior described by Theorem 20. The right side plots the error of both procedures after 10,000 iterations as a function of the output space dimension 𝑚between 1 and 50. The number of iteration ensures that, for all values of 𝑚∈[50], the reported error is well characterized by our theory, in other terms that we have entered the regime described by Theorem 20.

$$
Risk of ¯θT \frac{10−1}{10−5} Classiﬁcation task active passive 101 103 iteration T
$$

[FIGURE: Figure 10.9]

Figure 10.9: Comparison with the inﬁmum loss with better conditioned passive supervision in a similar setting to Figure 10.3 yet with 𝑚= 10, 𝜀= 0, that is 𝑋uniform on X, and 𝛾0 = 7.5 for the active strategy and 𝛾0 = 15 for the passive strategy. We see no major diﬀerences between the active strategy based on the median surrogate and the passive strategy based on the median surrogate with the inﬁmum loss. Note that the standard deviation is sometimes bigger than the average of the excess of risk, explaining the dive of the dark area on this logarithmic-scaled plot.

 inf𝑦′∈𝑠ℓ(𝑧, 𝑦′) if 𝑦∈𝑠 inf𝑦′∉𝑠ℓ(𝑧, 𝑦′) otherwise. and 𝑦∈Y,

$$
𝐿(𝑧, 𝑠, 1𝑦∈𝑠) =
$$

Random subsets 𝑆could be generated by making sure that the variable (𝑦∈𝑆)𝑦∈Y are independent balanced Bernoulli variables; and by removing the trivial sets 𝑆= ∅and 𝑆= Y from the subsequent distribution. In order to optimize this risk in practice, one can use a parametric model and a surrogate diﬀerentiable loss together with stochastic gradient descent on the empirical risk. For classiﬁcation with the 0-1 loss, we can reuse the surrogate introduced in Proposition 91 and minimize, assuming that we always observed 1𝑌𝑖∈𝑆𝑖= 1 for simplicity,

$$
ˆR𝐼,𝑆(𝜃) = \sum_{𝑛 𝑖=1} inf_{𝑦∈𝑆𝑖} 𝑔𝜃(𝑋𝑖) −𝑒𝑦 .
$$

Stochastic gradients are then given by, assuming ties have no probability to happen,

$$
𝑔𝜃(𝑋𝑡) −𝑒𝑦 = \frac{𝑔𝜃(𝑋𝑡) −𝑒𝑦∗}{𝑔𝜃(𝑋𝑡) −𝑒𝑦∗} !⊤
$$

𝐷𝑔𝜃(𝑋𝑡) with 𝑦∗:= arg max

$$
∇𝜃inf 𝑔𝜃(𝑋𝑡), 𝑒𝑦 .
𝑦∈𝑆𝑡 𝑦∈𝑆𝑡
$$

This gives a good passive baseline to compare our active strategy with. In our experiments with the Gaussian kernel, see Figure 10.9 for an example, we witness that this baseline is highly competitive. Although we ﬁnd that it is slightly harder to properly tune the step size for SGD, and that the need to compute an argmax for each gradient slows-down the computations.

<!-- page: 221 -->

10.E. EXPERIMENTAL DETAILS 219

### 10.E.3 Real-world classiﬁcation datasets

$$
“usps” dataset “pendigits” dataset
0.8 0.8
Risk of ¯θT Risk of ¯θT active passive random
0.6
0.6
active passive random 0.4
0.4 0.2
0 1000 2000 3000 4000 5000 iteration T 0 1000 2000 3000 4000 5000 iteration T
$$

[FIGURE: Figure 10.10]

Figure 10.10: Testing errors on two LIBSVM datasets with a similar setting to Figure 10.9. Those empirical errors are reported after averaging over 100 diﬀerent splits of the datasets. The step size parameter was optimized visually, which led to 𝛾0 = 15 for the active strategy on “USPS”, 𝛾0 = 60 for the passive one, 𝛾0 = 7.5 for the active strategy on “pen digits”, 𝛾0 = 30 for the passive one. The dotted line represents R = 1 −𝑚−1 which is the performance of a random model.

In Figure 10.10, we compare the “well-conditioned” passive baseline with our active strategy on the real-world problems of LIBSVM (Chang and Lin, 2011). We choose the “USPS” and “pen digits” datasets as they contain 𝑚= 10 classes each with 𝑛= 7291 and 𝑛= 7494 samples respectively, with 𝑑= 50 and 𝑑= 16 features each. We have chosen those datasets as they present enough classes that leads to many diﬀerent sets 𝑆to query, and they are made of the right number of samples to do some experiments on a laptop without the need for “advanced” computational techniques such as caching or low-rank approximation (Meanti et al., 2020). On Figure 10.10, we use the same linear model as for Figure 10.3, that is a Gaussian kernel. We choose the bandwidth to be 𝜎= 𝑑/5, and we normalize the features beforehand to make sure that they are all centered with unit variance. We report error by taking two thirds of the samples for training and one third for testing, and averaging over one hundred diﬀerent ways of splitting the datasets. We observe that the active strategy leads to important gains on the “USPS” dataset, yet is not that useful for the “pen digits” dataset. We have not dug in to understand those two diﬀerent behaviors.

### 10.E.4 Real-world regression dataset & Nyström method

In this section, we provide two experiments on real-world datasets.

In order to deal with big regression datasets, it is useful to approximate the parameter space Y ⊗H in Assumption 20 with a small dimensional space. To do so, let us remark that given samples (𝑋𝑖)𝑖≤𝑛∈X 𝑛for 𝑛∈N, we know that our estimate 𝑓𝜃𝑛can be represented as

$$
𝑓𝜃𝑛(·) = \sum_{𝑖≤𝑛} \sum_{𝑗≤𝑚} 𝑎𝑖𝑗⟨𝜑(𝑥𝑖), 𝜑(·)⟩𝑒𝑗,
$$

for some (𝑎𝑖𝑗) ∈R𝑝×𝑚and where (𝑒𝑗) 𝑗≤𝑚is the canonical basis of Y = R𝑚. For large datasets, that is when 𝑛is large, it is smart to approximate this representation through the parameterization

$$
𝑓𝑎(𝑥) = \sum_{𝑖≤𝑝} \sum_{𝑗≤𝑚} 𝑎𝑖𝑗𝑘(𝑥, 𝑥𝑖)𝑒𝑗,
$$

where 𝑝≤𝑛is the rank of our approximation, and 𝑘is the kernel deﬁned as 𝑘(𝑥, 𝑥′) = ⟨𝜑(𝑥), 𝜑(𝑥′)⟩. Stated with words, we only use a small number 𝑝, instead of 𝑛, of vectors 𝜑(𝑥𝑖) to parameterize 𝑓. This allows to only keep a matrix of size 𝑝× 𝑚in memory instead of 𝑛× 𝑚, while not fundamentally changing the statistical guarantee of the method (Rudi et al., 2015). In this setting, the stochastic gradients are speciﬁed from the fact that

$$
𝑢⊤𝐷𝑎𝑓𝑎(𝑥) = (𝑢𝑗𝑘(𝑥, 𝑥𝑖))𝑖,𝑗∈R𝑝×𝑚.
$$

In other terms, in order to update the parameter 𝑎with respect to the observation made at (𝑥, 𝑢), we check how much each coordinate of 𝑎determines the value of 𝑢⊤𝑓𝑎(𝑥).

<!-- page: 222 -->

In the following, we experiment with two real-world datasets. In order to learn the relation between inputs and outputs, we use a Gaussian kernel after normalizing input features so that each of them has zero mean and unit variance. To keep computational cost, we sample 𝑝random (Nyström) representers among the training inputs which are used to parameterize functions. To avoid overﬁtting, we add a small regularization to the empirical objective. It reads 𝜆∥𝜃∥2 H with our notations and corresponds to the Hilbertian norm inherited from the reproducing kernel 𝑘of the function 𝑓𝜃(Scholkopf and Smola, 2001).

$$
CalCOFI dataset Weather dataset
101
active passive baseline
Test risk of ¯θT Test risk of ¯θT
active passive baseline
100
10−1
101 103 105 101 103 105
Iteration T Iteration T
$$

[FIGURE: Figure 10.11]

Figure 10.11: Testing error on two real-world regression datasets. On both datasets, a single pass was made through the data in a chronological fashion, and errors were computed from the 26,453 most recent data samples for the “Weather” dataset, and from a random sample of 10,000 samples among the 155,140 most recent samples for the “CalCOFI” dataset.

Our ﬁrst experiment is based on the data collected by the California Cooperative Oceanic Fisheries Investigation between March 1949 and November 2016. It consists of more than 800,000 seawater samples including measurements of nutriments (set aside in our experiments) together with pressure, temperature, salinity, water density, dynamic height (providing ﬁve input parameters), as well as dissolved oxygen, and oxygen saturation (the two outputs we would like to predict). We assume that we can measure if any weighted sum of oxygen concentration and saturation is above a threshold by letting some population of bacteria evolves in the water sample and checking if it survives after a day. If the measurements are done on the day of the sample collection, this setting exactly ﬁts in the streaming active labeling framework. After cleaning the dataset for missing values, the dataset contains 655,140 samples. The “CalCOFI” dataset results are reported on the left of Figure 10.11, parameters were chosen as 𝑝= 100, 𝜎= 10, 𝜆= 10−6 and 𝛾0 = 1. For the passive strategy, random queries were chosen to follow a normal distribution with the same mean as the targets and one third of their standard deviation (i.e. we ask if the apparent temperature is lower than the usual one plus or minus a perturbation). The plotted baseline corresponds to linear regression performed over the entire dataset. It takes about 10,000 samples for our active strategy to be competitive with this baseline, and 200,000 samples for the passive one.

The second experiment makes use of data collected through the Dark Sky API (which is now part of Apple WeatherKit). It is made of 96,454 weather summaries between 2006 and 2016 in the city of Szeged, Hungary. Our task consists in computing the apparent temperature from real temperature, humidity, wind speed, wind bearing, visibility and pressure. The apparent temperature is an index that searches to quantify the subjective feeling of heat that humans perceive, it is expressed on the same scale as real temperature. One way to measure it would be to ask some humans if the outside is hotter or colder than a controlled room with a speciﬁc temperature and neutral meteorological conditions. Once again, this exactly ﬁts into our streaming active labeling setting. The “Weather” dataset results are reported on the right of Figure 10.11. The baseline consists in predicting the apparent temperature as the real temperature. We observe a transitory regime where the ﬁrst 1,000 samples seem to be used to calibrate the weights 𝛼. During this regime, our estimate is too bad for the active strategy to make smarter queries than the “random” ones that have been calibrated on temperature statistics. The main diﬀerence in the learning dynamic between the active and passive strategies is observed on the remaining 69,000 training samples. The parameters were the same as the “CalCOFI” dataset but for 𝛾0 = 10−2.

<!-- page: 223 -->

# Conclusion

In this thesis, we have approached weakly supervised learning through partial supervision. We have leveraged the algorithm of Ciliberto et al. (2016) to provide consistent estimators once we had formulated the problem through the inﬁmum loss, which was the focus of Cabannes et al. (2020b). By characterizing implicit disambiguation due to the inﬁmum loss, we have revisited and generalized the approach of Bach and Harchaoui (2007) to any type of discrete output problems in Cabannes et al. (2021b). Such a disambiguation strategy has the advantage of working with a smaller surrogate space (working on functions from X to RY rather than from X to R2Y), hence reducing the variance of our estimates, and making approximation assumptions more comprehensible. Regarding optimization, our min-min formulations are hard to tackle in a generic fashion; while one can reuse the relaxation in Bach and Harchaoui (2007), our implementations were based on alternate minimization with good starting points; readers and practitioners eager to come up with diﬀerent strategies might refer to literature on bilevel optimization for non-convex problems. In Cabannes et al. (2021a), advocating for the leverage of unlabeled data, we have brought up the approach of Zhu et al. (2003) to the realm of kernel methods; and to ensure computational eﬃciency, we have adapted the low-rank approximation of Rudi et al. (2015) and its proof to our speciﬁc setting with derivatives. We hope to see future works pushing forwards the usage of kernel methods with derivatives, could it be for sampling through Langevin dynamics (in the spirit of Pillaud-Vivien, 2020a) or for penalties inducing sparsity (in the spirit of Rosasco et al., 2013; Follain et al., 2022). Providing eﬃcient and user-friendly open-source implementations would arguably foster the diﬀusion of kernels with derivatives in the research community.

In order to help the practitioner collecting data, we ﬁnally set ourselves before the data collection process, and introduced the “active labeling” problem. Following the observation that one does not need to access full information in order to build stochastic gradients, we provided a ﬁrst solution to this problem based on stochastic gradient descent in Cabannes et al. (2022) that is naturally adapted to streaming settings. In a near future, we would like to focus on exploiting the discrete-output structure of classiﬁcation problems more subtly than surrogate methods, notably with ideas steaming from the “bandit” literature. In particular, we will explore how entropic coding could help to tackle the active labeling problem. Beside this project, the “active” setup opens up new possibilities, e.g., to detach ourselves from min-min formulations and try to come up with well-grounded min-max formulations that are easier to optimize, or, on a completely diﬀerent level, to deal with privacy constraints.

While working on the proof of Cabannes et al. (2021b), we discovered that usual rates of convergence on discrete output learning problems are often suboptimal thanks to the work of Audibert and Tsybakov (2007). In substance, if you have 𝐿∞-exponential concentration inequality, and margin conditions, then you can have up to exponential convergence rates. We studied the question in more detail in Cabannes et al. (2021c) and Cabannes and Vigogna (2022). Those derivations can still be pushed further, could it be to better understand the interplay between estimation error (a.k.a. variance) and approximation error (a.k.a. bias) without decoupling them, or by adapting the proof structure with concentration on other quantities than suprema and corresponding relative hardness conditions. Regarding statistical learning, a project of interest to pursue, yet which require other tools than the ones presented in the thesis, is to approach learning theory without thinking in terms of functions classes, but by thinking directly with measures, especially at the light of the disambiguation principles that we expressed directly in the space of measures. Interestingly, such an approach might help to exchange (if not unify) ideas between works on weakly supervised learning (i.e. missing output data) and works on missing (input) data.

Finally, while this thesis was more of theoretical nature, in order to maximize my “tangible impact” as a researcher, I would like to look at issues that are closer to “production” and focus more on real-world experiments. I hope that my future postdoc position at FAIR New York will provide me with such opportunities, for example by exposing myself to ongoing experimental works with self-supervised learning.

221

<!-- page: 224 -->

222

<!-- page: 225 -->

# Bibliography

Martín Abadi, Paul Barham, Jianmin Chen, Zhifeng Chen, Andy Davis, Jeﬀrey Dean, Matthieu Devin, Sanjay Ghemawat, Geoﬀrey Irving, Michael Isard, Manjunath Kudlur, Josh Levenberg, Rajat Monga, Sherry Moore, Derek G. Murray, Benoit Steiner, Paul Tucker, Vĳay Vasudevan, Pete Warden, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng. Tensorﬂow: A system for large-scale machine learning. In Conference on Operating Systems Design and Implementation, 2016.

Nir Ailon. Active learning ranking from pairwise preferences with almost optimal query complexity. In Advances in Neural Information Processing Systems, 2011.

Nir Ailon, Moses Charikar, and Alantha Newman. Aggregating inconsistent information: ranking and clustering. In Symposium on Theory of Computing, 2005.

Ahmed El Alaoui, Xiang Cheng, Aaditya Ramdas, Martin Wainwright, and Michael Jordan. Asymptotic behavior of ℓ𝑝-based Laplacian regularization in semi-supervised learning. In Conference on Learning Theory, 2016.

Jean-Baptiste Alayrac. Structured Learning from Videos and Language. Phd thesis, Ecole Normale Supérieure, 2018.

Jean-Baptiste Alayrac, Piotr Bojanowski, Nishant Agrawal, Josef Sivic, Ivan Laptev, and Simon Lacoste-Julien. Unsupervised learning from narrated instruction videos. In Conference on Computer Vision and Pattern Recognition, 2016.

Charalambos Aliprantis and Kim Border. Inﬁnite Dimensional Analysis: A Hitchhikers Guide. Springer, 2006.

Martin Anthony and Peter Bartlett. Neural Network Learning: Theoretical Foundations. Cambridge University Press, 1999.

Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and David Lopez-Paz. Invariant risk minimization. Technical Report 1907.02893, ArXiv, 2019.

Nachman Aronszajn. Theory of reproducing kernels. Transactions of the American Mathematical Society, 68(3):337–404, 1950.

Sanjeev Arora, László Babai, Jacques Stern, and Elizabeth Sweedyk. The hardness of approximate optima in lattices, codes, and systems of linear equations. Journal of Computer and System Sciences, 54(2):317–331, 1997.

Kenneth Arrow. A diﬃculty in the concept of social welfare. Journal of Political Economy, 58(4):328–346, 1950.

Jean-Yves Audibert and Alexander Tsybakov. Fast learning rates for plug-in classiﬁers. The Annals of Statistics, 35(2):608–633, 2007.

Dmitry Babichev, Dmitrii Ostrovskii, and Francis Bach. Eﬃcient primal-dual algorithms for large-scale multiclass classiﬁcation. Technical Report 1902.03755, ArXiv, 2019.

Francis Bach. Learning Theory from First Principles. To appear at MIT press, 2023.

Francis Bach and Zaïd Harchaoui. DIFFRAC: a discriminative and ﬂexible framework for clustering. In Advances in Neural Information Processing Systems, 2007.

Francis Bach and Eric Moulines. Non-strongly-convex smooth stochastic approximation with convergence rate 𝑂(1/𝑛). In Advances in Neural Information Processing Systems, 2013.

Francis Bach, Rodolphe Jenatton, Julien Mairal, and Guillaume Obozinski. Optimization with sparsity-inducing penalties. Foundations and Trends in Maching Learning, 4(1):1–106, 2012.

Peter Bartlett and Shahar Mendelson. Rademacher and gaussian complexities: Risk bounds and structural results. Journal of Machine Learning Research, 3:463–482, 2002.

223

<!-- page: 226 -->

Peter Bartlett and Shahar Mendelson. Empirical minimization. Probability Theory and Related Fields, 135 (3):311–334, 2006.

Peter Bartlett, Michael Jordan, and Jon McAuliﬀe. Convexity, classiﬁcation, and risk bounds. Journal of the American Statistical Association, 101(473):138–156, 2006.

Peter Bartlett, Dylan Foster, and Matus Telgarsky. Spectrally-normalized margin bounds for neural networks.

In Advances in Neural Information Processing Systems, 2017.

Gerald Beer. Topologies on closed and closed convex sets. Springer, 1993.

Sven Behnke. Hierarchical Neural Networks for Image Interpretation. Springer, 2003.

Mikhail Belkin and Partha Niyogi. Laplacian eigenmaps for dimensionality reduction and data representation.

Neural Computation, 15(6):1373–1396, 2003.

Yoshua Bengio, Olivier Delalleau, and Nicolas Le Roux. Label propagation and quadratic criterion. In Semi-Supervised Learning. MIT Press, 2006.

Viktor Bengs, Róbert Busa-Fekete, Adil El Mesaoudi-Paul, and Eyke Hüllermeier. Preference-based online learning with dueling bandits: A survey. Journal of Maching Learning Research, 22(7):1–108, 2021.

Ruha Benjamin. Race After Technology: Abolitionist Tools for the New Jim Code. Polity, 2019.

James Bennett and Stan Lanning. The netﬂix prize. In Knowledge Discovery and Data Mining Cup and Workshop, 2007.

Serguei Bernstein. On certain modiﬁcations of Chebyshev’s inequality. Doklady Akademii Nauk SSSR, 17 (6):275–177, 1937.

David Berthelot, Nicholas Carlini, Ian Goodfellow, Nicolas Papernot, Avital Oliver, and Colin Raﬀel.

Mixmatch: A holistic approach to semi-supervised learning. In Advances in Neural Information Processing Systems, 2019.

Gérard Biau and Luc Devroye. Lectures on the Nearest Neighbor Method. Springer, 2015.

Lucien Birgé. Approximation dans les espaces métriques et théorie de l’estimation. Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete, 65(2):181–237, 1983.

Ingrid Blaschzyk and Ingo Steinwart. Improved classiﬁcation rates under reﬁned margin conditions. Electronic Journal of Statistics, 12(1):793–823, 2018.

Mathieu Blondel, André Martins, and Vlad Niculae. Learning with Fenchel-Young losses. Journal of Machine Learning Research, 21(35):1–69, 2020.

Salomon Bochner. Monotone funktionen, stieltjessche integrale und harmonische analyse. Mathematische Annalen, 108(1):378–410, 1933.

Léon Bottou and Olivier Bousquet. The tradeoﬀs of large scale learning. In Advances in Neural Information Processing Systems, 2007.

Stéphane Boucheron, Olivier Bousquet, and Gábor Lugosi. Theory of classiﬁcation: a survey of some recent advances. ESAIM: Probability and Statistics, 9:323–375, 2005.

Mark Braverman, Jieming Mao, and Yuval Peres. Sorted top-k in rounds. In Conference on Learning Theory, 2019.

Leo Breiman, Jerome Friedman, Richard Olshen, and Charles Stone. Classiﬁcation and Regression Trees. Chapman & Hall, 1984. 224

<!-- page: 227 -->

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeﬀrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In Advances in Neural Information Processing Systems, 2020.

Joan Bruna and Stéphane Mallat. Invariant scattering convolution networks. Transactions on Pattern Analysis and Machine Intelligence, 35(8):1872–1886, 2013.

Sébastien Bubeck. Convex optimization: Algorithms and complexity. Foundations and Trends in Machine Learning, 8(3-4):231–357, 2015.

Vivien Cabannes. Le futur du numérique sera-t-il incarné ? Esprit, 487:117–125, 2022.

Vivien Cabannes and Stefano Vigogna. A case of exponential convergence rates for SVM. Technical report, ArXiv, 2022.

Vivien Cabannes, Thomas Kerdreux, Louis Thiry, and Tina & Charly. Dialog on a canvas with a machine. In NeurIPS workshop on Creativity, 2019.

Vivien Cabannes, Thomas Kerdreux, and Louis Thiry. Diptychs of human and machine perception. In NeurIPS workshop on Creativity, 2020a.

Vivien Cabannes, Alessandro Rudi, and Francis Bach. Structured prediction with partial labelling through the inﬁmum loss. In International Conference on Machine Learning, 2020b.

Vivien Cabannes, Loucas Pillaud-Vivien, Francis Bach, and Alessandro Rudi. Overcoming the curse of dimensionality with Laplacian regularization in semi-supervised learning. In Advances in Neural Information Processing Systems, 2021a.

Vivien Cabannes, Alessandro Rudi, and Francis Bach. Disambiguation of weak supervision with exponential convergence rates. In International Conference on Machine Learning, 2021b.

Vivien Cabannes, Alessandro Rudi, and Francis Bach. Fast rates in structured prediction. In Conference on Learning Theory, 2021c.

Vivien Cabannes, Francis Bach, Vianney Perchet, and Alessandro Rudi. Active labeling: streaming stochastic gradients. Technical report, ArXiv, 2022.

Aylin Caliskan, Joanna Bryson, and Arvind Narayanan. Semantics derived automatically from language corpora contain human-like biases. Science, 356(6334):183–186, 2017.

Emmanuel Candès, Justin Romberg, and Terence Tao. Robust uncertainty principles: exact signal reconstruction from highly incomplete frequency information. IEEE Transactions on Information Theory, 52(2): 489–509, 2006.

Zhe Cao, Tao Qin, Tie-Yan Liu, Ming-Feng Tsai, and Hang Li. Learning to rank: from pairwise approach to listwise approach. In International Conference of Machine Learning, 2007.

Andrea Caponnetto and Ernesto De Vito. Optimal rates for the regularized least-squares algorithm. Foundations of Computational Mathematics, 7(3):331–368, 2006.

Vittorio Castelli and Thomas Cover. On the exponential value of labeled samples. Pattern Recognition Letters, 16(1):105–111, 1995.

René Erlín Castillo and Humberto Rafeiro. An Introductory Course in Lebesgue Spaces. Springer, 2016.

Nicolò Cesa-Bianchi, Claudio Gentile, and Luca Zaniboni. Incremental algorithms for hierarchical classiﬁcation. Journal of Machine Learning Research, 7(2):31–54, 2006.

Nicolò Cesa-Bianchi, Tommaso Cesari, and Vianney Perchet. Dynamic pricing with ﬁnitely many unknown valuations. In International Conference on Algorithmic Learning Theory, 2019.

225

<!-- page: 228 -->

Chih-Chung Chang and Chih-Jen Lin. LIBSVM: a library for support vector machines. ACM Transactions on Intelligent Systems and Technology, 2(3):1–27, 2011.

Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien, editors. Semi-Supervised Learning. MIT Press, 2006.

Kamalika Chaudhuri and Sanjoy Dasgupta. Rates of convergence for nearest neighbor classiﬁcation. In Advances in Neural Information Processing Systems, 2014.

George Chen and Devavrat Shah. Explaining the success of nearest neighbor methods in prediction.

Foundations and Trends in Machine Learning, 10(5-6):337–588, 2018.

Lin Chen and Sheng Xu. Deep neural tangent kernel and Laplace kernel have the same RKHS. In International Conference on Learning Representations, 2021.

Herman Chernoﬀ. Sequential design of experiments. The Annals of Mathematical Statistics, 30(3):755–770, 1959.

Clément Chevalier, Julien Bect, David Ginsbourger, Emmanuel Vázquez, Victor Picheny, and Yann Richet.

Fast parallel kriging-based stepwise uncertainty reduction with application to the identiﬁcation of an excursion set. Technometrics, 56(4):455–465, 2014.

Lénaïc Chizat and Francis Bach. Implicit bias of gradient descent for wide two-layer neural networks trained with the logistic loss. In Conference on Learning Theory, 2020.

Lenaic Chizat, Edouard Oyallon, and Francis Bach. On lazy training in diﬀerentiable programming. In Advances in Neural Information Processing Systems, 2019.

Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, JeﬀDean, Slav Petrov, and Noah Fiedel. PaLM: Scaling language modeling with pathways. Technical Report 2204.02311, ArXiv, 2022.

Jesús Cid-Sueiro, Darío García-García, and Raúl Santos-Rodríguez. Consistency of losses for learning from weak labels. In Machine Learning and Knowledge Discovery in Databases, 2014.

Carlo Ciliberto, Lorenzo Rosasco, and Alessandro Rudi. A consistent regularization approach for structured prediction. In Advances in Neural Information Processing Systems, 2016.

Carlo Ciliberto, Lorenzo Rosasco, and Alessandro Rudi. A general framework for consistent structured prediction with implicit loss embeddings. Journal of Machine Learning Research, 21(98):1–67, 2020.

William Cleveland. Robust locally weighted regression and smoothing scatterplots. Journal of the American Statistical Association, 74(368):829–836, 1979.

Maxime Cohen, Ilan Lobel, and Renato Paes Leme. Feature-based dynamic pricing. Management Science, 66(11):4921–4943, 2020.

Ronald Coifman and Stéphane Lafon. Diﬀusion maps. Applied and Computational Harmonic Analysis, 21 (1):5–30, 2006.

Corinna Cortes and Vladimir Vapnik. Support-vector networks. Machine Learning, 20(3):273–297, 1995.

226

<!-- page: 229 -->

Council of European Union. Regulation (EU) 2016/679 of the European parliament (General Data Protection Regulation), 2016.

Timothée Cour, Benjamin Sapp, and Ben Taskar. Learning from partial labels. Journal of Machine Learning Research, 12(42):1501–1535, 2011.

Thomas Cover and Peter Hart. Nearest neighbor pattern classiﬁcation. IEEE Transactions on Information Theory, 13(1):21–27, 1967.

Thomas Cover and Joy Thomas. Elements of Information Theory. Wiley, 1991.

Mark Craven and Johan Kumlien. Constructing biological knowledge bases by extracting information from text sources. In International Conference on Intelligent Systems for Molecular Biology, 1999.

Nello Cristianini and John Shawe-Taylor. An introduction to support vector machines and other kernel-based learning methods. Cambridge university press, 2000.

Rishabh Dabral, Anurag Mundhada, Uday Kusupati, Safeer Afaque, Abhishek Sharma, and Arjun Jain.

Learning 3D human pose from structure and motion. In European Conference on Computer Vision, 2018.

Navneet Dalal and Bill Triggs. Histograms of oriented gradients for human detection. In Conference on Computer Vision and Pattern Recognition, 2005.

Sanjoy Dasgupta. Two faces of active learning. Theoretical Computer Science, 412(19):1767–1781, 2011.

Allan Davis, Thomas Wiegers, Phoebe Roberts, Benjamin King, Jean Lay, Kelley Lennon-Hopkins, Daniela Sciaky, Robin Johnson, Heather Keating, Nigel Greene, Robert Hernandez, Kevin McConnell, Ahmed Enayetallah, and Carolyn Mattingly. A CTD-Pﬁzer collaboration: manual curation of 88,000 scientiﬁc articles text mined for drug-disease and drug-phenotype interactions. Database (Oxford), 2012.

Philip Dawid and Allan Skene. Maximum likelihood estimation of observer error-rates using the EM algorithm. Journal of the Royal Statistical Society. Series C (Applied Statistics), 28(1):20–28, 1979.

Arthur Dempster, Nan Laird, and Donald Rubin. Maximum likelihood from incomplete data via the EM algorithm. Journal of the Royal Statistical Society. Series B (Methodological), 39(1):1–38, 1977.

Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Fei-Fei Li. Imagenet: A large-scale hierarchical image database. In Conference on Computer Vision and Pattern Recognition, 2009.

Thierry Denoeux. Maximum likelihood estimation from uncertain data in the belief function framework.

IEEE Transactions on Knowledge and Data Engineering, 25(1):119–130, 2013.

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training of deep bidirectional transformers for language understanding. In North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2019.

Luc Devroye and Terry Wagner. Distribution-free consistency results in nonparametric discrimination and regression function estimation. The Annals of Statistics, 8(2):231–239, 1980.

Luc Devroye, László Györﬁ, and Gábor Lugosi. A Probabilistic Theory of Pattern Recognition. Springer, 1996.

Thomas Dietterich, Richard Lathrop, and Tomás Lozano-Pérez. Solving the multiple instance problem with axis-parallel rectangles. Artiﬁcial Intelligence, 89(1-2):31–71, 1997.

AnHai Doan, Raghu Ramakrishnan, and Alon Halevy. Crowdsourcing systems on the world-wide web.

Communication of the ACM, 54(4):86–96, 2011.

Carl Doersch and Andrew Zisserman. Multi-task self-supervised visual learning. In International Conference on Computer Vision, 2017.

David Donoho. Compressed sensing. IEEE Transactions on Information Theory, 52(4):1289–1306, 2006.

227

<!-- page: 230 -->

John Duchi, Lester Mackey, and Michael Jordan. On the consistency of ranking algorithms. In International Conference on Machine Learning, 2010.

Richard Duda, Peter Hart, and David Stork. Pattern Classiﬁcation, 2nd Edition. Wiley, 2000.

Richard Dudley. The sizes of compact subsets of hilbert space and continuity of gaussian processes. Journal of Functional Analysis, 1(3):290–330, 1967.

Gabriel Dulac-Arnold, Neil Zeghidour, Marco Cuturi, Lucas Beyer, and Jean-Philippe Vert. Deep multiclass learning from label proportions. Technical Report 1905.12909, ArXiv, 2019.

Cynthia Dwork, Frank McSherry, Kobbi Nissim, and Adam Smith. Calibrating noise to sensitivity in private data analysis. In Theory of Cryptography Conference, 2006.

Alan Edelman and Yuyang Wang. The GSVD: where are the ellipses?, matrix trigonometry, and more. SIAM Journal on Matrix Analysis and Applications, 41(4):1826–1856, 2020.

David Eriksson, Kun Dong, Eric Hans Lee, David Bindel, and Andrew Gordon Wilson. Scaling Gaussian process regression with derivatives. In Advances in Neural Information Processing Systems, 2018.

Robert Fano. Transmission of Information: A Statistical Theory of Communications. MIT press, 1968.

Tanner Fiez, Lalit Jain, Kevin G Jamieson, and Lillian Ratliﬀ. Sequential Experimental Design for Transductive Linear Bandits. In Advances in Neural Information Processing Systems, 2019.

Mathias Fink. Time reversed acoustics. Physics Today, 50(3):34–40, 1997.

Simon Fischer and Ingo Steinwart. Sobolev norm learning rates for regularized least-squares algorithms.

Journal of Machine Learning Research, 21(205):1–38, 2020.

Evelyn Fix and Joseph Hodges. Discriminatory analysis. Nonparametric discrimination: Consistency properties. Technical report, School of Aviation Medicine, Randolph Field, Texas, 1951.

Bertille Follain, Umut Şimşekli, and Francis Bach. Non-parametric subspace learning through trace norm penalty. Technical report, In preparation at INRIA, 2022.

Dimitris Fotakis, Alkis Kalavasis, Vasilis Kontonis, and Christos Tzamos. Eﬃcient algorithms for learning from coarse labels. In Conference on Learning Theory, 2021.

Jerome Friedman. Flexible metric nearest neighbor classiﬁcation. Technical report, Department of Statistics, Stanford University, 1994.

Rafael Frongillo and Bo Waggoner. Surrogate regret bounds for polyhedral losses. In Advances in Neural Information Processing Systems, 2021.

Kunihiko Fukushima. Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaﬀected by shift in position. Biological Cybernetics, 36(4):193–202, 1980.

Sachin Gangaputra and Donald Geman. A design principle for coarse-to-ﬁne classiﬁcation. In Conference on Computer Vision and Pattern Recognition, 2006.

Eva García-Martín, Crefeda Faviola Rodrigues, Graham Riley, and Håkan Grahn. Estimation of energy consumption in machine learning. Journal of Parallel and Distributed Computing, 134:75–88, 2019.

Nicolás García Trillos, Moritz Gerlach, Matthias Hein, and Dejan Slepčev. Error estimates for srdectritionl convergence of the graph Laplacian on random geometric graphs toward the Laplace–Beltrami operator. Foundations of Computational Mathematics, 20(4):827–887, 2019.

Aurélien Garivier and Emilie Kaufmann. Optimal best arm identiﬁcation with ﬁxed conﬁdence. In Conference on Learning Theory, 2016.

Josselin Garnier and George Papanicolaou. Passive imaging with ambient noise. Cambridge University Press, 2016. 228

<!-- page: 231 -->

Philippe Gautret, Jean-Christophe Lagier, Philippe Parola, Van Thuan Hoang, Line Meddeb, Morgane Mailhe, Barbara Doudier, Johan Courjon, Valérie Giordanengo, Vera Esteves Vieira, Hervé Tissot Dupont, Stéphane Honoréé, Philippe Colson, Eric Chabrière, Bernard La Scola, Jean-Marc Rolain, Philippe Brouqui, and Didier Raoult. Hydroxychloroquine and azithromycin as a treatment of COVID-19: results of an open-label non-randomized clinical trial. International journal of antimicrobial agents, 56(1):105949, 2020.

Timothy Gebhard, Niki Kilbertus, Ian Harry, and Bernhard Schölkopf. Convolutional neural networks: A magic bullet for gravitational-wave detection? Physical Review D, 100(6):063015, 2019.

Donald Geman and Bruno Jedynak. Shape recognition and twenty questions. Technical report, INRIA, 1993.

Claudio Gentile and Manfred Warmuth. Linear hinge loss and average margin. In Advances in Neural Information Processing Systems, 1999.

Aurélien Géron. Hands-On Machine Learning with Scikit-Learn & TensorFlow. O’Reilly, 2017.

Edgar Gilbert. A comparison of signalling alphabets. Bell System Technical Journal, 31(3):504–522, 1952.

Mike Glennon and Michael Shirer. Investment in artiﬁcial intelligence solutions will accelerate as businesses seek insights, eﬃciency, and innovation, according to a new IDC spending guide. Technical report, International Data Corporation, 2021.

Gene Golub and Charles Van Loan. Matrix computations (3rd edition). Johns Hopkins University Press, 1996.

Gene Golub and Charles Van Loan. Matrix computations (4th edition). Johns Hopkins University Press, 2013.

Chen Gong, Tongliang Liu, Yuanyan Tang, Jian Yang, Jie Yang, and Dacheng Tao. A regularization approach for instance-based superset label learning. IEEE Transactions on Cybernetics, 48(3):967–978, 2018.

Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative adversarial nets. In Advances in Neural Information Processing Systems, 2014.

Yves Grandvalet. Logistic regression for partial labels. In Information Processing and Management of Uncertainty, 2002.

Romain Guillaume, Inés Couso, and Didier Dubois. Maximum likelihood with coarse data based on robust optimisation. In International Symposium on Imprecise Probability, 2017.

László Györﬁ, Michael Kohler, Adam Krzyzak, and Harro Walk. A Distribution-Free Theory of Nonparametric Regression. Springer, 2002.

Steve Hanneke. Theory of disagreement-based active learning. Foundations and Trends in Machine Learning, 7(2-3):131–309, 2014.

Charles Harris, Jarrod Millman, Stéfan van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten van Kerkwĳk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, and Travis Oliphant. Array programming with NumPy. Nature, 585(7825):357–362, 2020.

James Heckman. Sample selection bias as a speciﬁcation error. Econometrica, 47(1):153–161, 1979.

Matthias Hein, Jean-Yves Audibert, and Ulrike von Luxburg. Graph Laplacians and their convergence on random neighborhood graphs. Journal of Machine Learning Research, 8(48):1325–1368, 2007.

Daniel Heitjan and Donald Rubin. Ignorability and coarse data. The Annals of Statistics, 19(4):2244–2253, 1991.

229

<!-- page: 232 -->

Wassily Hoeﬀding. Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, 58(301):13–30, 1963.

Klaus-Uwe Höﬀgen and Hans Ulrich Simon. Robust trainability of single neurons. In Computational Learning Theory, 1992.

Alan Hoﬀman and Joseph Kruskal. Integral boundary points of convex polyhedra. In 50 Years of Integer Programming 1958-2008 - From the Early Years to the State-of-the-Art. Springer, 2010.

Peter Huber. Robust Statistics. Wiley, 1981.

Eyke Hüllermeier. Learning from imprecise and fuzzy observations: Data disambiguation through generalized loss minimization. International Journal of Approximate Reasoning, 55:1519–1534, 2014.

Eyke Hüllermeier and Weiwei Cheng. Superset learning based on generalized loss minimization. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 2015.

Eyke Hüllermeier, Johannes Fürnkranz, Weiwei Cheng, and Klaus Brinker. Label ranking by learning pairwise preferences. Artiﬁcial Intelligence, 72(16):1897–1916, 2008.

John Hunter. Matplotlib: A 2d graphics environment. Computing in Science & Engineering, 9(3):90–95, 2007.

IBM. IBM ILOG CPLEX 12.7 User’s Manual. IBM ILOG CPLEX Division, 2017.

Il’dar Ibragimov and Rafail Khas’minskii. On the estimation of an inﬁnite-dimensional parameter in gaussian white noise. Doklady Akademii Nauk SSSR, 236(5):1053–1055, 1977.

Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, and Aleksander Madry.

Adversarial examples are not bugs, they are features. In Advances in Neural Information Processing Systems, 2019.

Tommi Jaakkola, Mark Diekhans, and David Haussle. A discriminative framework for detecting remote protein homologies. Journal of Computational Biology, 7(1-2):95–114, 2000.

Arthur Jacot, Clément Hongler, and Franck Gabriel. Neural tangent kernel: Convergence and generalization in neural networks. In Advances in Neural Information Processing Systems, 2018.

Kevin Jamieson and Robert Nowak. Active ranking using pairwise comparisons. In Advances in Neural Information Processing Systems, 2011.

Ye Jia, Yu Zhang, Ron Weiss, Quan Wang, Jonathan Shen, Fei Ren, Zhifeng Chen, Patrick Nguyen, Ruoming Pang, Ignacio Lopez-Moreno, and Yonghui Wu. Transfer learning from speaker veriﬁcation to multispeaker text-to-speech synthesis. In Advances in Neural Information Processing Systems, 2018.

Rong Jin and Zoubin Ghahramani. Learning with multiple labels. In Advances in Neural Information Processing Systems, 2002.

Thorsten Joachims. Text categorization with support vector machines: Learning with many relevant features.

In European Conference on Machine Learning, 1998.

Justin Johnson, Alexandre Alahi, and Li Fei-Fei. Perceptual losses for real-time style transfer and super-resolution. In European Conference on Computer Vision, 2016.

Michael Jordan. Artiﬁcial Intelligence — the revolution hasn’t happened yet. Harvard Data Science Review, 2019.

Armand Joulin, Francis Bach, and Jean Ponce. Discriminative clustering for image co-segmentation. In Conference on Computer Vision and Pattern Recognition, 2010.

230

<!-- page: 233 -->

John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens Meyer, Simon Kohl, Andrew Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David Silver, Oriol Vinyals, Andrew Senior, Koray Kavukcuoglu, Pushmeet Kohli, and Demis Hassabis. Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873):583–589, 2021.

Tero Karras, Samuli Laine, and Timo Aila. A style-based generator architecture for generative adversarial networks. In Conference on Computer Vision and Pattern Recognition, 2019.

Mina Karzand and Robert Nowak. Maximin active learning in overparameterized model classes. IEEE Journal on Selected Areas in Information Theory, 1(1):167–177, 2020.

Michael Kearns. Eﬃcient noise-tolerant learning from statistical queries. Journal of the Asoociation for Computing Machinery, 45(6):983–1006, 1998.

John Kemeny. Mathematics without numbers. Daedalus, 88(4):577–591, 1959.

Maurice Kendall. A new measure of rank correlation. Biometrika, 30(1-2):81–93, 1938.

Stefan Klus, Feliks Nüske, and Boumediene Hamzi. Kernel-based approximation of the Koopman generator and Schrödinger operator. Entropy, 22(7):722, 2020.

Donald Knuth. The computer as master mind. Journal of Recreational Mathematics, 9(1):1–6, 1977.

Andrey Kolmogorov and Vladimir Tikhomirov. 𝜀-entropy and 𝜀-capacity of sets in functional spaces. Uspekhi Matematicheskikh Nauk, 14(2):3–86, 1959.

Vladimir Koltchinskii and Olexandra Beznosova. Exponential convergence rates in classiﬁcation. In International Conference on Computational Learning Theory, 2005.

Anna Korba, Alexandre Garcia, and Florence d’Alché-Buc. A structured prediction approach for label ranking. In Advances in Neural Information Processing Systems, 2018.

Jonathan Krause, Benjamin Sapp, Andrew Howard, Howard Zhou, Alexander Toshev, Tom Duerig, James Philbin, and Li Fei-Fei. The unreasonable eﬀectiveness of noisy data for ﬁne-grained recognition. In European Conference on Computer Vision, 2016.

Alex Krizhevsky. Learning multiple layers of features from tiny images. Technical report, Canadian Institute for Advanced Research, 2009.

Alex Krizhevsky, Ilya Sutskever, and Geoﬀrey Hinton. Imagenet classiﬁcation with deep convolutional neural networks. In Advances in Neural Information Processing Systems, 2012.

John Laﬀerty, Andrew McCallum, and Fernando Pereira. Conditional random ﬁelds: Probabilistic models for segmenting and labeling sequence data. In International Conference on Machine Learning, 2001.

Andrew Larkoski, Ian Moult, and Benjamin Nachman. Jet substructure at the large hadron collider: A review of recent advances in theory and machine learning. Physics Reports, 841:1–63, 2020.

Yann LeCun and Yoshua Bengio. Convolutional networks for images, speech, and time-series. In The handbook of brain theory and neural networks. MIT Press, 1995.

Yann LeCun, Yoshua Bengio, and Geoﬀrey Hinton. Deep learning. Nature, 521(7553):436–444, 2015.

Marc Lelarge and Léo Miolane. Asymptotic Bayes risk for Gaussian mixture in a semi-supervised setting. In International Workshop on Computational Advances in Multi-Sensor Adaptive Processing, 2019.

Julian Lienen and Eyke Hüllermeier. From label smoothing to label relaxation. In AAAI Conference on Artiﬁcial Intelligence, 2021.

231

<!-- page: 234 -->

Junhong Lin, Alessandro Rudi, Lorenzo Rosasco, and Volkan Cevher. Optimal rates for spectral algorithms with least-squares regression over Hilbert spaces. Applied and Computational Harmonic Analysis, 48(3): 868–890, 2020.

Allen Liu, Renato Paes Leme, and Jon Schneider. Optimal contextual pricing and extensions. In Symposium on Discrete Algorithms, 2021.

Li-Ping Liu and Thomas Dietterich. Learnability of the superset label learning problem. In International Conference on Machine Learning, 2014.

Steve Lohr. A $1 million research bargain for Netﬂix, and maybe a model for other. New York Times, 2009.

Philip Long and Rocco Servedio. Consistency versus realizable h-consistency for multiclass classiﬁcation.

In International Conference on Machine Learning, 2013.

Xinghua Lou and Fred Hamprecht. Structured learning from partial annotations. In International Conference on Machine Learning, 2012.

David Lowe. Object recognition from local scale-invariant features. In International Conference on Computer Vision, 1999.

Jie Luo and Francesco Orabona. Learning from candidate labeling sets. In Advances in Neural Information Processing Systems, 2010.

Michael Lustig, David Donoho, Juan Santos, and John Pauly. Compressed sensing MRI. Signal Processing Magazine, 25(2):72–82, 2008.

Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. Towards deep learning models resistant to adversarial attacks. In International Conference on Learning Representations, 2018.

Aravindh Mahendran and Andrea Vedaldi. Understanding deep image representations by inverting them. In Conference on Computer Vision and Pattern Recognition, 2015.

Julien Mairal, Piotr Koniusz, Zaid Harchaoui, and Cordelia Schmid. Convolutional kernel networks. In Advances in Neural Information Processing Systems, 2014.

Stéphane Mallat. Multifrequency channel decompositions of images and wavelet models. Transactions on Acoustics, Speech, and Signal Processing, 37(12):2091–2110, 1989.

Stéphane Mallat. Understanding deep convolutional networks. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 374(2065):20150203, 2016.

Enno Mammen and Alexander Tsybakov. Smooth discrimination analysis. The Annals of Statistics, 27(6):

1808–1829, 1999.

Gideon Mann and Andrew McCallum. Generalized expectation criteria for semi-supervised learning with weakly labeled data. Journal of Machine Learning Research, 11(32):955–984, 2010.

Ulysse Marteau-Ferey, Dmitrii Ostrovskii, Francis Bach, and Alessandro Rudi. Beyond least-squares: Fast rates for regularized empirical risk minimization through self-concordance. In Conference on Learning Theory, 2019.

Pascal Massart and Élodie Nédélec. Risk bounds for statistical learning. The Annals of Statistics, 34(5): 2326–2366, 2006.

Andreas Maurer. A vector-contraction inequality for Rademacher complexities. In Algorithmic Learning Theory, 2016.

Warren McCulloch and Walter Pitts. A logical calculus of the ideas immanent in nervous activity. The bulletin of mathematical biophysics, 5(4):115–133, 1943.

Giacomo Meanti, Luigi Carratino, Lorenzo Rosasco, and Alessandro Rudi. Kernel methods through the roof:

Handling billions of points eﬃciently. In Advances in Neural Information Processing Systems, 2020.

232

<!-- page: 235 -->

Song Mei and Andrea Montanari. The generalization error of random features regression: Precise asymptotics and the double descent curve. Communications on Pure and Applied Mathematics, 75(4):667–766, 2022.

James Mercer. Functions of positive and negative type and their connection with the theory of integral equations. Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character, 209:415–446, 1909.

Charles Micchelli, Yuesheng Xu, and Haizhang Zhang. Universal kernels. Journal of Machine Learning Research, 7(95):2651–2667, 2006.

Antoine Miech, Dimitri Zhukov, Jean-Baptiste Alayrac, Makarand Tapaswi, Ivan Laptev, and Josef Sivic.

Howto100m: Learning a text-video embedding by watching hundred million narrated video clips. In International Conference on Computer Vision, 2019.

Stanislav Minsker. On some extensions of Bernstein’s inequality for self-adjoint operators. Statistics & Probability Letters, 127:111–119, 2017.

Mike Mintz, Steven Bills, Rion Snow, and Dan Jurafsky. Distant supervision for relation extraction without labeled data. In International Joint Conference on Natural Language Processing, 2009.

Krikamol Muandet, Kenji Fukumizu, Bharath Sriperumbudur, and Bernhard Schölkopf. Kernel mean embedding of distributions: A review and beyond. Foundations and Trends in Machine Learnig, 10(1-2): 1–141, 2017.

Stephen Muggleton and Luc de Raedt. Inductive logic programming: Theory and methods. The Journal of Logic Programming, 19-20:629–679, 1994.

Èlizbar Nadaraya. On estimating regression. Theory of Probability & Its Applications, 9(1):141–142, 1964.

Boaz Nadler, Nathan Srebro, and Xueyuan Zhou. Statistical analysis of semi-supervised learning: The limit of inﬁnite unlabelled data. In Advances in Neural Information Processing Systems, 2009.

John Nelder and Robert Wedderburn. Generalized linear models. Journal of the Royal Statistical Society.

Series A (General), 135(3):370–384, 1972.

Nam Nguyen and Rich Caruana. Classiﬁcation with partial labels. In International Conference on Knowledge Discovery and Data Mining, 2008.

Vu-Linh Nguyen, Mohammad Hossein Shaker, and Eyke Hüllermeier. How to measure uncertainty in uncertainty sampling for active learning. Machine Learning, 111(1):89–122, 2021.

Atsushi Nitanda and Taĳi Suzuki. Stochastic gradient descent with exponential convergence rates of expected classiﬁcation errors. In International Conference on Artiﬁcial Intelligence and Statistics, 2019.

Alex Nowak-Vila. Structured prediction with theoretical guarantees. Phd thesis, Ecole Normale Supérieure, 2021.

Alex Nowak-Vila, Francis Bach, and Alessandro Rudi. Sharp analysis of learning with discrete losses. In Artiﬁcial Intelligence and Statistics, 2019.

Alex Nowak-Vila, Francis Bach, and Alessandro Rudi. A general theory for structured prediction with smooth convex surrogates. Technical Report 1902.01958, ArXiv, 2020.

Harry Nyquist. Certain topics in telegraph transmission theory. Transactions of the American Institute of Electrical Engineers, 47(2):617–644, 1928.

Sinno Pan and Qiang Yang. A survey on transfer learning. Transactions on Knowledge and Data Engineering, 22(10):1345–1459, 2010.

George Papandreou, Liang-Chieh Chen, Kevin Murphy, and Alan Yuille. Weakly- and semi-supervised learning of a deep convolutional network for semantic image segmentation. In International Conference on Computer Vision, 2015.

233

<!-- page: 236 -->

Vardan Papyan, Yaniv Romano, and Michael Elad. Convolutional neural networks analyzed via convolutional sparse coding. Journal of Machine Learning Research, 18(83):1–52, 2017.

Emanuel Parzen. On estimation of a probability density function and mode. The Annals of Mathematical Statistics, 33(3):1065–1076, 1962.

Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. Pytorch: An imperative style, high-performance deep learning library. In Advances in Neural Information Processing Systems, 2019.

Fabian Pedregosa, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas, Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot, and Édouard Duchesnay. Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(85):2825–2830, 2011.

Andrzej Pelc. Searching games with errors - ﬁfty years of coping with liars. Theoretical Compututer Science, 270(1):71–109, 2002.

Vianney Perchet and Marc Quincampoix. On a uniﬁed framework for approachability with full or partial monitoring. Mathematics of Operations Research, 40(3):596–610, 2015.

Loucas Pillaud-Vivien. Statistical estimation of the poincaré constant and application to sampling multimodal distributions. In International Conference on Artiﬁcial Intelligence and Statistics, 2020a.

Loucas Pillaud-Vivien. Learning with Reproducing Kernel Hilbert Spaces: Stochastic Gradient Descent and Laplacian Estimation. Phd thesis, Ecole Normale Supérieure, 2020b.

Loucas Pillaud-Vivien, Alessandro Rudi, and Francis Bach. Statistical optimality of stochastic gradient descent on hard learning problems through multiple passes. In Advances in Neural Information Processing Systems, 2018a.

Loucas Pillaud-Vivien, Alessandro Rudi, and Francis Bach. Exponential convergence of testing error for stochastic gradient methods. In Conference on Learning Theory, 2018b.

Iosif Pinelis and Aleksandr Sakhanenko. Remarks on inequalities for large deviation probabilities. Theory of Probability and Its Applications, 30(1):143–148, 1986.

Bahar Qarabaqi and Mirek Riedewald. User-driven reﬁnement of imprecise queries. In International Conference on Data Engineering, 2014.

Novi Quadrianto, Alexander Smola, Tibério Caetano, and Quoc V. Le. Estimating labels from label proportions. Journal of Machine Learning Research, 10(82):2349–2374, 2009.

Ali Rahimi and Benjamin Recht. Random features for large-scale kernel machines. In Advances in Neural Information Processing Systems, 2007.

Alexander Ratner, Stephen Bach, Henry Ehrenberg, Jason Fries, Sen Wu, and Christopher Ré. Snorkel: rapid training data creation with weak supervision. The VLDB Journal, 29(2):709–730, 2020.

Philippe Rigollet. Generalization error bounds in semi-supervised classiﬁcation under the cluster assumption.

Journal of Machine Learning Research, 8(49):1369–1392, 2007.

Herbert Robbins and Sutton Monro. A stochastic approximation method. The Annals of Mathematical Statistics, 22(3):400–407, 1951.

Lorenzo Rosasco, Ernesto De Vito, Andrea Caponnetto, Michele Piana, and Alessandro Verri. Are loss functions all the same? Neural Computation, 16(5):1063–1076, 2004.

Lorenzo Rosasco, Silvia Villa, Soﬁa Mosci, Matteo Santoro, and Alessandro Verri. Nonparametric sparsity and regularization. Journal of Machine Learning Research, 14(16):1665–1714, 2013.

234

<!-- page: 237 -->

Frank Rosenblatt. The perceptron: a probabilistic model for information storage and organization in the brain. Psychological Review, 65(6):386–408, 1958.

Murray Rosenblatt. Remarks on some nonparametric estimates of a density function. The Annals of Mathematical Statistics, 27(3):832–837, 1956.

Donald Rubin. Inference and missing data. Biometrika, 63(3):581–592, 1976.

Alessandro Rudi, Raﬀaello Camoriano, and Lorenzo Rosasco. Less is more: Nyström computational regularization. In Advances in Neural Information Processing Systems, 2015.

Robert Schapire. The strength of weak learnability. Machine Learning, 5(2):197–227, 1990.

Bernhard Scholkopf and Alexander Smola. Learning with kernels: support vector machines, regularization, optimization, and beyond. MIT press, 2001.

Laurent Schwartz. Sous-espaces Hilbertiens d’espaces vectoriels topologiques et noyaux associés (noyaux reproduisants). Journal d’Analyse Mathématique, 13(1):115–256, 1964.

Ramprasaath Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra. Grad-cam: Visual explanations from deep networks via gradient-based localization. In International Conference on Computer Vision, 2017.

Burr Settles. Active learning literature survey. Technical report, University of Wisconsin-Madison, 2010.

Claude Shannon. Communication in the presence of noise. Proceedings of the Institute of Radio Engineers, 37(1):10–21, 1949.

William Sheppard. On the calculation of the most probable values of frequency constants, for data arranged according to equidistant division of a scale. Proceedings of the London Mathematical Society, s1-29(1): 353–380, 1897.

Hidetoshi Shimodaira. Improving predictive inference under covariate shift by weighting the log-likelihood function. Journal of Statistical Planning and Inference, 90(2):227–244, 2000.

Emil Sidky and Xiaochuan Pan. Image reconstruction in circular cone-beam computed tomography by constrained, total-variation minimization. Physics in Medicine & Biology, 53(17):4777–4807, 2008.

David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, and Demis Hassabis. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. Science, 362(6419):1140–1144, 2018.

Herbert Simon. The architecture of complexity. Proceedings of the American Philosophical Society, 106(6):

467–482, 1962.

Eric Slud. Distribution inequalities for the binomial law. Annals of Probability, 5(3):404–412, 1977.

Steve Smale and Ding-Xuan Zhou. Learning theory estimates via integral operators and their approximations.

Constructive Approximation, 26(2):153–172, 2007.

Alexander Smola and Risi Kondor. Kernels and regularization on graphs. In Conference on Computational Learning Theory, 2003.

Cliﬀord Spiegelman and Jerome Sacks. Consistent window estimation in nonparametric regression. The Annals of Statistics, 8(2):240–246, 1980.

Stefano Spigler, Mario Geiger, Stéphane d’Ascoli, Levent Sagun, Giulio Biroli, and Matthieu Wyart. A jamming transition from under-to over-parametrization aﬀects loss landscape and generalization. Journal of Physics A: Mathematical and Theoretical, 52(47):17, 2019.

Karthik Sridharan, Shai Shalev-shwartz, and Nathan Srebro. Fast rates for regularized objectives. In Advances in Neural Information Processing Systems, 2008.

235

<!-- page: 238 -->

Ingo Steinwart. How to compare diﬀerent loss functions and their risks. Constructive Approximation, 26(2): 225–287, 2007.

Ingo Steinwart and Andreas Christmann. Support vector machines. Springer, 2008.

Ingo Steinwart and Clint Scovel. Fast rates for support vector machines using Gaussian kernels. The Annals of Statistics, 35(2):575–607, 2007.

Ingo Steinwart and Clint Scovel. Mercer’s theorem on general domains: On the interaction between measures, kernels, and RKHSs. Constructive Approximation, 35(3):363–417, 2012.

Charles Stone. Consistent nonparametric regression. The Annals of Statistics, 5(4):595–620, 1977.

Charles Stone. Optimal rates of convergence for nonparametric estimators. The Annals of Statistics, 8(6):

1348–1360, 1980.

Richard Sutton and Andrew Barto. Reinforcement Learning: An Introduction. MIT press, 2018.

Christian Szegedy, Wojciech Zaremba, Ilya Sutskever, Joan Bruna, Dumitru Erhanand Ian Goodfellow, and Rob Fergus. Intriguing properties of neural networks. In International Conference on Learning Representations, 2014.

Robert Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society.

Series B (Methodological), 58(1):267–288, 1996.

James Tobin. Estimation of relationships for limited dependent variables. Econometrica, 26(1):24–36, 1958.

Ioannis Tsochantaridis, Thorsten Joachims, Thomas Hofmann, and Yasemin Altun. Large margin methods for structured and interdependent output variables. Journal of Machine Learning Research, 6(50):1453–1484, 2005.

Grigorios Tsoumakas, Eleftherios Spyromitros Xiouﬁs, Jozef Vilcek, and Ioannis Vlahavas. MULAN: a java library for multi-label learning. Journal of Machine Learning Research, 12(71):2411–2414, 2011.

Alexander Tsybakov. Introduction to Nonparametric Estimation. Springer, 2009.

Alan Turing. Computing machinery and intelligence. Mind, 59(236):433–460, 1950.

US Census Bureau. Income and poverty in the United States: 2020, 2021.

Leslie Valiant. Parallelism in comparison problems. SIAM Journal on Computing, 4(3):348–355, 1975.

Leslie Valiant. Probably Approximately Correct. Basic Books, 2013.

Jesper van Engelen and Holger Hoos. A survey on semi-supervised learning. Machine Learning, 109(2): 373–440, 2020.

Tim van Erven, Peter Grünwald, Nishant Mehta, Mark Reid, and Robert Williamson. Fast rates in statistical and online learning. Journal of Machine Learning Research, 16(54):1793–1861, 2015.

Brendan van Rooyen and Robert Williamson. A theory of learning with corrupted labels. Journal of Machine Learning Research, 18(228):1–50, 2017.

Anke van Zuylen, Rajneesh Hegde, Kamal Jain, and David Williamson. Deterministic pivoting algorithms for constrained ranking and clustering problems. In Symposium on Discrete Algorithms, 2007.

Vladimir Vapnik. The Nature of Statistical Learning Theory. Springer, 1995.

Rom Varshamov. Estimate of the number of signals in error correcting codes. Doklady Akademii Nauk SSSR, 117:739–741, 1957.

Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems, 2017.

236

<!-- page: 239 -->

Jakob Verbeek and William Triggs. Scene Segmentation with CRFs Learned from Partially Labeled Images.

In Advances in Neural Information Processing Systems, 2008.

Vikas Verma, Alex Lamb, Juho Kannala, Yoshua Bengio, and David Lopez-Paz. Interpolation consistency training for semi-supervised learning. In International Joint Conference on Artiﬁcial Intelligence, 2019.

Stefano Vigogna, Giacomo Meanti, Ernesto De Vito, and Lorenzo Rosasco. Multiclass learning with margin: exponential rates with no bias-variance trade-oﬀ. In International Conference on Machine Learning, 2022.

Anatoliy Vitushkin. On Hilbert’s thirteenth problem. Proceedings of the USSR Academy of Sciences, 95(4):

701–704, 1954.

John von Neumann and Oskar Morgenstern. Theory of Games and Economic Behavior. Princeton University Press, 1944.

Vladimir Vovk and Glenn Shafer. A tutorial on conformal prediction. Journal of Machine Learning Research, 9(12):371–421, 2008.

Abraham Wald. Statistical decision functions which minimize the maximum risk. The Annals of Mathematics, 46(2):265–280, 1945.

Mansﬁeld Tracy Walsorth. Twenty Questions: A Short Treatise on the Game. Holt, 1882.

Dan Wang and Yi Shang. A new active labeling method for deep learning. In International Joint Conference on Neural Networks, 2014.

Lĳun Wang, Huchuan Lu, Yifan Wang, Mengyang Feng, Dong Wang, Baocai Yin, and Xiang Ruan. Learning to detect salient objects with image-level supervision. In Conference on Computer Vision and Pattern Recognition, 2017.

Geoﬀrey Watson. Smooth regression analysis. Sankhy¯a: The Indian Journal of Statistics, 26(4):359–372, 1962.

Yair Weiss. Segmentation using eigenvectors: a unifying view. In International Conference on Computer Vision, 1999.

Edmund Whittaker. On the functions which are represented by the expansions of the interpolation theory.

Proceedings of the Royal Society of Edinburgh, 35:181–194, 1915.

Harold Widom. Asymptotic behavior of the eigenvalues of certain integral equations. Transactions of the American Mathematical Society, 109(2), 1963.

Henry Wilbraham. On a certain periodic function. The Cambridge and Dublin Mathematical Journal, 3:

108–112, 1848.

Christopher Williams and Matthias Seeger. Using the Nyström method to speed up kernel machines. In Advances in Neural Information Processing Systems, 2000.

Ronald Williams, Geoﬀrey Hinton, and David Rumelhart. Learning representations by back-propagating errors. Nature, 323(6088):533–536, 1986.

Linli Xu, James Neufeld, Bryce Larson, and Dale Schuurmans. Maximum margin clustering. In Advances in Neural Information Processing Systems, 2004.

Greg Yang, Edward Hu, Igor Babuschkin, Szymon Sidor, Xiaodong Liu, David Farhi, Nick Ryder, Jakub Pachocki, Weizhu Chen, and Jianfeng Gao. Tensor programs V: Tuning large neural networks via zero-shot hyperparameter transfer. In Advances in Neural Information Processing Systems, 2021.

Yuhong Yang. Minimax nonparametric classiﬁcation. I. Rates of convergence. IEEE Transactions on Information Theory, 45(7):2271–2284, 1999.

Hsiang-Fu Yu, Prateek Jain, Purushottam Kar, and Inderjit Dhillon. Large-scale multi-label learning with missing labels. In International Conference on Machine Learning, 2014.

237

<!-- page: 240 -->

Vadim Vladimirovich Yurinskii. On an inﬁnite-dimensional version of S. N. Bernstein’s inequalities. Theory of Probability and Its Applications, 15(1):108–109, 1970.

Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, and Oriol Vinyals. Understanding deep learning (still) requires rethinking generalization. Communications of the ACM, 64(3):107–115, 2021.

Mingyuan Zhang and Shivani Agarwal. Bayes consistency vs. H-consistency: The interplay between surrogate loss functions and the scoring function class. In Advances in Neural Information Processing Systems, 2020.

Heliang Zheng, Jianlong Fu, Zheng-Jun Zha, and Jiebo Luo. Looking for the devil in the details: Learning trilinear attention sampling network for ﬁne-grained image recognition. In Conference on Computer Vision and Pattern Recognition, 2019.

Dengyong Zhou, Olivier Bousquet, Thomas Navin Lal, Jason Weston, and Bernhard Schölkopf. Learning with local and global consistency. In Advances in Neural Information Processing Systems, 2003.

Ding-Xuan Zhou. Derivative reproducing properties for kernel methods in learning theory. Journal of Computational and Applied Mathematics, 220(1):456–463, 2008.

Xiaojin Zhu, Zoubin Ghahramani, and John Laﬀerty. Semi-supervised learning using Gaussian ﬁelds and harmonic functions. In International Conference of Machine Learning, 2003.

238

<!-- page: 241 -->

<!-- page: 242 -->

RÉSUMÉ Les mathématiques appliquées et le calcul nourrissent beaucoup d’espoirs à la suite des succès récents de l’apprentissage supervisé. Dans l’industrie, beaucoup d’ingénieurs cherchent à remplacer leurs anciens paradigmes de pensée par l’apprentissage machine. Étonnamment, ces ingénieurs passent plus de temps à collecter, annoter et nettoyer des données qu’à rafﬁner des modèles. Ce phénomène motive la problématique de cette thèse: peut-on déﬁnir un cadre théorique plus général que l’apprentissage supervisé pour apprendre grâce à des données hétérogènes? Cette question est abordée via le concept de supervision faible, faisant l’hypothèse que le problème que posent les données est leur annotation. On modélise la supervision faible comme l’accès, pour une entrée donnée, non pas d’une sortie claire, mais d’un ensemble de sorties potentielles. On plaide pour l’adoption d’une perspective « optimiste » et l’apprentissage d’une fonction qui vériﬁe la plupart des observations. Cette perspective nous permet de déﬁnir un principe pour lever l’ambiguïté des informations faibles. On discute également de l’importance d’incorporer des techniques sans supervision d’appréhension des données d’entrée dans notre théorie, en particulier de compréhension de la variété sous-jacente via des techniques de diffusion, pour lesquelles on propose un algorithme réaliste aﬁn d’éviter le ﬂéau de la dimension, à l’inverse de ce qui existait jusqu’alors. Enﬁn, nous nous attaquons à la question de collecte active d’informations faibles, déﬁnissant le problème de « catalogage en ligne », où un intendant doit acquérir une maximum d’informations ﬁables sur ses données sous une contrainte de budget. Entre autres, nous tirons parti du fait que pour obtenir un gradient stochastique et effectuer une descente de gradient, il n’y a pas besoin de supervision totale.

MOTS CLÉS Apprentissage statistique. Données faiblement supervisées. Acquisition active d’informations partielles.

ABSTRACT Applied mathematics and machine computations have raised a lot of hope since the recent success of supervised learning. Many practitioners in industries have been trying to switch from their old paradigms to machine learning. Interestingly, those data scientists spend more time scrapping, annotating and cleaning data than ﬁne-tuning models. This thesis is motivated by the following question: can we derive a more generic framework than the one of supervised learning in order to learn from clutter data? This question is approached through the lens of weakly supervised learning, assuming that the bottleneck of data collection lies in annotation. We model weak supervision as giving, rather than a unique target, a set of target candidates. We argue that one should look for an “optimistic” function that matches most of the observations. This allows us to derive a principle to disambiguate partial labels. We also discuss the advantage to incorporate unsupervised learning techniques into our framework, in particular manifold regularization approached through diffusion techniques, for which we derived a new algorithm that scales better with input dimension then the baseline method. Finally, we switch from passive to active weakly supervised learning, introducing the “active labeling” framework, in which a practitioner can query weak information about chosen data. Among others, we leverage the fact that one does not need full information to access stochastic gradients and perform stochastic gradient descent.

KEYWORDS Statistical learning. Weakly supervised learning; partial supervision. Active labeling; weak queries.
