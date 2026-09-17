<!-- page: 1 -->

# Neural Machine Translation by Jointly Learning to Align and Translate
### Dzmitry Bahdanau
Jacobs University Bremen, Germany

**KyungHyun Cho Yoshua Bengio**<sup>_∗_</sup> Université de Montréal

## Abstract
Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

## 1 INTRODUCTION
_Neural machine translation_ is a newly emerging approach to machine translation, recently proposed by Kalchbrenner and Blunsom (2013), Sutskever _et al._ (2014) and Cho _et al._ (2014b). Unlike the traditional phrase-based translation system (see, e.g., Koehn _et al._ , 2003) which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation.

Most of the proposed neural machine translation models belong to a family of _encoder– decoders_ (Sutskever _et al._ , 2014; Cho _et al._ , 2014a), with an encoder and a decoder for each language, or involve a language-specific encoder applied to each sentence whose outputs are then compared (Hermann and Blunsom, 2014). An encoder neural network reads and encodes a source sentence into a fixed-length vector. A decoder then outputs a translation from the encoded vector. The whole encoder–decoder system, which consists of the encoder and the decoder for a language pair, is jointly trained to maximize the probability of a correct translation given a source sentence.

A potential issue with this encoder–decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus. Cho _et al._ (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases.

In order to address this issue, we introduce an extension to the encoder–decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words.

> _∗_ CIFAR Senior Fellow

<!-- page: 2 -->

The most important distinguishing feature of this approach from the basic encoder–decoder is that it does not attempt to encode a whole input sentence into a single fixed-length vector. Instead, it encodes the input sentence into a sequence of vectors and chooses a subset of these vectors adaptively while decoding the translation. This frees a neural translation model from having to squash all the information of a source sentence, regardless of its length, into a fixed-length vector. We show this allows a model to cope better with long sentences.

In this paper, we show that the proposed approach of jointly learning to align and translate achieves significantly improved translation performance over the basic encoder–decoder approach. The improvement is more apparent with longer sentences, but can be observed with sentences of any length. On the task of English-to-French translation, the proposed approach achieves, with a single model, a translation performance comparable, or close, to the conventional phrase-based system. Furthermore, qualitative analysis reveals that the proposed model finds a linguistically plausible (soft-)alignment between a source sentence and the corresponding target sentence.

## 2 BACKGROUND: NEURAL MACHINE TRANSLATION
From a probabilistic perspective, translation is equivalent to finding a target sentence **y** that maximizes the conditional probability of **y** given a source sentence **x** , i.e., arg max **y** _p_ ( **y** _|_ **x** ). In neural machine translation, we fit a parameterized model to maximize the conditional probability of sentence pairs using a parallel training corpus. Once the conditional distribution is learned by a translation model, given a source sentence a corresponding translation can be generated by searching for the sentence that maximizes the conditional probability.

Recently, a number of papers have proposed the use of neural networks to directly learn this conditional distribution (see, e.g., Kalchbrenner and Blunsom, 2013; Cho _et al._ , 2014a; Sutskever _et al._ , 2014; Cho _et al._ , 2014b; Forcada and Neco, 1997).<sup>˜</sup> This neural machine translation approach typically consists of two components, the first of which encodes a source sentence **x** and the second decodes to a target sentence **y** . For instance, two recurrent neural networks (RNN) were used by (Cho _et al._ , 2014a) and (Sutskever _et al._ , 2014) to encode a variable-length source sentence into a fixed-length vector and to decode the vector into a variable-length target sentence.

Despite being a quite new approach, neural machine translation has already shown promising results. Sutskever _et al._ (2014) reported that the neural machine translation based on RNNs with long shortterm memory (LSTM) units achieves close to the state-of-the-art performance of the conventional phrase-based machine translation system on an English-to-French translation task.<sup>1</sup> Adding neural components to existing translation systems, for instance, to score the phrase pairs in the phrase table (Cho _et al._ , 2014a) or to re-rank candidate translations (Sutskever _et al._ , 2014), has allowed to surpass the previous state-of-the-art performance level.

### 2.1 RNN ENCODER–DECODER
Here, we describe briefly the underlying framework, called _RNN Encoder–Decoder_ , proposed by Cho _et al._ (2014a) and Sutskever _et al._ (2014) upon which we build a novel architecture that learns to align and translate simultaneously.

In the Encoder–Decoder framework, an encoder reads the input sentence, a sequence of vectors **x** = ( _x_ 1 _, · · · , xTx_ ), into a vector _c_ .<sup>2</sup> The most common approach is to use an RNN such that

$$
ht = f (x_{t}, ht-1) (1)
$$

and

$$
c = q ({h1, \cdot \cdot \cdot , hTx}) ,
$$

where _ht ∈_ R<sup>_n_</sup> is a hidden state at time _t_ , and _c_ is a vector generated from the sequence of the hidden states. _f_ and _q_ are some nonlinear functions. Sutskever _et al._ (2014) used an LSTM as _f_ and _q_ ( _{h_ 1 _, · · · , hT }_ ) = _hT_ , for instance.

> 1 We mean by the state-of-the-art performance, the performance of the conventional phrase-based system without using any neural network-based component.

> 2 Although most of the previous works (see, e.g., Cho _et al._ , 2014a; Sutskever _et al._ , 2014; Kalchbrenner and Blunsom, 2013) used to encode a variable-length input sentence into a _fixed-length_ vector, it is not necessary, and even it may be beneficial to have a _variable-length_ vector, as we will show later.

<!-- page: 3 -->

The decoder is often trained to predict the next word _yt′_ given the context vector _c_ and all the previously predicted words _{y_ 1 _, · · · , yt′−_ 1 _}_ . In other words, the decoder defines a probability over the translation **y** by decomposing the joint probability into the ordered conditionals:

$$
T p(y) = Y p(y_{t} | {y_{1}, \cdot \cdot \cdot , y_{t}-1} , c), (2) t=1
$$

$$
where y = y_{1}, \cdot \cdot \cdot , yTy . With an RNN, each conditional probability is modeled as p(y_{t} | {y_{1}, \cdot \cdot \cdot , y_{t}-1} , c) = g(y_{t}-1, st, c), (3)
$$

where _g_ is a nonlinear, potentially multi-layered, function that outputs the probability of _yt_ , and _st_ is the hidden state of the RNN. It should be noted that other architectures such as a hybrid of an RNN and a de-convolutional neural network can be used (Kalchbrenner and Blunsom, 2013).

## 3 LEARNING TO ALIGN AND TRANSLATE
In this section, we propose a novel architecture for neural machine translation. The new architecture consists of a bidirectional RNN as an encoder (Sec. 3.2) and a decoder that emulates searching through a source sentence during decoding a translation (Sec. 3.1).

### 3.1 DECODER: GENERAL DESCRIPTION
In a new model architecture, we define each conditional probability in Eq. (2) as:

$$
p(y_i \mid y_1, \ldots, y_{i-1}, \mathbf{x}) = g(y_{i-1}, s_i, c_i),
$$

where _s_i_ is an RNN hidden state for time _i_, computed by

$$
s_i = f(s_{i-1}, y_{i-1}, c_i).
$$

It should be noted that unlike the existing encoder–decoder approach (see Eq. (2)), here the probability is conditioned on a distinct context vector _cii_ for each target word _yii_ .

The context vector _cii_ depends on a sequence of _annotations_ ( _h_ 1 _, · · · , hTx_ ) to which an encoder maps the input sentence. Each annotation _hi_ contains information about the whole input sequence with a strong focus on the parts surrounding the _i_ -th word of the input sequence. We explain in detail how the annotations are computed in the next section.
> **Figure 1:** The graphical illustration of the proposed model trying to generate the _t_ -th target word _yt_ given a source sentence ( _x_ 1 _, x_ 2 _, . . . , xT_ ).
The context vector _ci_ is, then, computed as a weighted sum of these annotations _hi_ :

$$
Tx ci = X \alpha ijhj. (5) j=1
$$

The weight _αij_ of each annotation _hj_ is computed by

$$
exp (eij) \alpha ij = , (6) PTx k=1 exp (eik)
$$

where

$$
eij = a(si-1, hj)
$$

is an _alignment model_ which scores how well the inputs around position _j_ and the output at position _i_ match. The score is based on the RNN hidden state _si−_ 1 (just before emitting _yi_ , Eq. (4)) and the _j_ -th annotation _hj_ of the input sentence.

We parametrize the alignment model _a_ as a feedforward neural network which is jointly trained with all the other components of the proposed system. Note that unlike in traditional machine translation,

<!-- page: 4 -->

the alignment is not considered to be a latent variable. Instead, the alignment model directly computes a soft alignment, which allows the gradient of the cost function to be backpropagated through. This gradient can be used to train the alignment model as well as the whole translation model jointly.

We can understand the approach of taking a weighted sum of all the annotations as computing an _expected annotation_ , where the expectation is over possible alignments. Let _αij_ be a probability that the target word _yi_ is aligned to, or translated from, a source word _xj_ . Then, the _i_ -th context vector _ci_ is the expected annotation over all the annotations with probabilities _αij_ .

The probability _αij_ , or its associated energy _eij_ , reflects the importance of the annotation _hj_ with respect to the previous hidden state _si−_ 1 in deciding the next state _si_ and generating _yi_ . Intuitively, this implements a mechanism of attention in the decoder. The decoder decides parts of the source sentence to pay attention to. By letting the decoder have an attention mechanism, we relieve the encoder from the burden of having to encode all information in the source sentence into a fixed-length vector. With this new approach the information can be spread throughout the sequence of annotations, which can be selectively retrieved by the decoder accordingly.

### 3.2 ENCODER: BIDIRECTIONAL RNN FOR ANNOTATING SEQUENCES
The usual RNN, described in Eq. (1), reads an input sequence **x** in order starting from the first symbol _x_ 1 to the last one _xTx_ . However, in the proposed scheme, we would like the annotation of each word to summarize not only the preceding words, but also the following words. Hence, we propose to use a bidirectional RNN (BiRNN, Schuster and Paliwal, 1997), which has been successfully used recently in speech recognition (see, e.g., Graves _et al._ , 2013).

A BiRNN consists of forward and backward RNN’s. The forward RNN<sup>_−→_</sup> _f_ reads the input sequence as it is ordered (from _x_ 1 to _xTx_ ) and calculates a sequence of _forward hidden states_ (<sup>_−→_</sup> _h_ 1 _, · · · ,_<sup>_−→_</sup> _h Tx_ ). The backward RNN<sup>_←−_</sup> _f_ reads the sequence in the reverse order (from _xTx_ to _x_ 1), resulting in a sequence of _backward hidden states_ (<sup>_←−_</sup> _h_ 1 _, · · · ,_<sup>_←−_</sup> _h Tx_ ).

We obtain an annotation for each word _xj_ by concatenating the forward hidden state<sup>_−→_</sup> _h j_ and the backward one<sup>_←−_</sup> _h j_ , i.e., _hj_ =  _−→h j⊤_<sup>;</sup><sup>_←−h⊤_</sup> _j_  _⊤_ . In this way, the annotation _hj_ contains the summaries of both the preceding words and the following words. Due to the tendency of RNNs to better represent recent inputs, the annotation _hj_ will be focused on the words around _xj_ . This sequence of annotations is used by the decoder and the alignment model later to compute the context vector (Eqs. (5)–(6)).

See Fig. 1 for the graphical illustration of the proposed model.

## 4 EXPERIMENT SETTINGS
We evaluate the proposed approach on the task of English-to-French translation. We use the bilingual, parallel corpora provided by ACL WMT ’14.<sup>3</sup> As a comparison, we also report the performance of an RNN Encoder–Decoder which was proposed recently by Cho _et al._ (2014a). We use the same training procedures and the same dataset for both models.<sup>4</sup>

### 4.1 DATASET
WMT ’14 contains the following English-French parallel corpora: Europarl (61M words), news commentary (5.5M), UN (421M) and two crawled corpora of 90M and 272.5M words respectively, totaling 850M words. Following the procedure described in Cho _et al._ (2014a), we reduce the size of the combined corpus to have 348M words using the data selection method by Axelrod _et al._ (2011).<sup>5</sup> We do not use any monolingual data other than the mentioned parallel corpora, although it may be possible to use a much larger monolingual corpus to pretrain an encoder. We concatenate news-test-

> 3 http://www.statmt.org/wmt14/translation-task.html

> 4 Implementations are available at https://github.com/lisa-groundhog/GroundHog.

> 5 Available online at http://www-lium.univ-lemans.fr/˜schwenk/cslm_joint_paper/.

<!-- page: 5 -->

2012 and news-test-2013 to make a development (validation) set, and evaluate the models on the test set (news-test-2014) from WMT ’14, which consists of 3003 sentences not present in the training data.

After a usual tokenization<sup>6</sup> , we use a shortlist of 30,000 most frequent words in each language to train our models. Any word not included in the shortlist is mapped to a special token ([UNK]). We do not apply any other special preprocessing, such as lowercasing or stemming, to the data.

### 4.2 MODELS
We train two types of models. The first one is an RNN Encoder–Decoder (RNNencdec, Cho _et al._ , 2014a), and the other is the proposed model, to which we refer as RNNsearch. We train each model twice: first with the sentences of length up to 30 words (RNNencdec-30, RNNsearch-30) and then with the sentences of length up to 50 word (RNNencdec-50, RNNsearch-50).

The encoder and decoder of the RNNencdec have 1000 hidden units each.<sup>7</sup> The encoder of the RNNsearch consists of forward and backward recurrent neural networks (RNN) each having 1000 hidden units. Its decoder has 1000 hidden units. In both cases, we use a multilayer network with a single maxout (Goodfellow _et al._ , 2013) hidden layer to compute the conditional probability of each target word (Pascanu _et al._ , 2014).

We use a minibatch stochastic gradient descent (SGD) algorithm together with Adadelta (Zeiler, 2012) to train each model. Each SGD update direction is computed using a minibatch of 80 sentences. We trained each model for approximately 5 days.

Once a model is trained, we use a beam search to find a translation that approximately maximizes the conditional probability (see, e.g., Graves, 2012; Boulanger-Lewandowski _et al._ , 2013). Sutskever _et al._ (2014) used this approach to generate translations from their neural machine translation model.

For more details on the architectures of the models and training procedure used in the experiments, see Appendices A and B.

## 5 RESULTS
### 5.1 QUANTITATIVE RESULTS
In Table 1, we list the translation performances measured in BLEU score. It is clear from the table that in all the cases, the proposed RNNsearch outperforms the conventional RNNencdec. More importantly, the performance of the RNNsearch is as high as that of the conventional phrase-based translation system (Moses), when only the sentences consisting of known words are considered. This is a significant achievement, considering that Moses uses a separate monolingual corpus (418M words) in addition to the parallel corpora we used to train the RNNsearch and RNNencdec.

> 6 We used the tokenization script from the open-source machine translation package, Moses.

> 7 In this paper, by a ’hidden unit’, we always mean the gated hidden unit (see Appendix A.1.1).

> **Figure 2:** The BLEU scores of the generated translations on the test set with respect to the lengths of the sen- tences. The results are on the full test set which in- cludes sentences having un- known words to the models.

<!-- page: 6 -->

> **Figure 3:** Four sample alignments found by RNNsearch-50. The x-axis and y-axis of each plot correspond to the words in the source sentence (English) and the generated translation (French), respectively. Each pixel shows the weight _αij_ of the annotation of the _j_ -th source word for the _i_ -th target word (see Eq. (6)), in grayscale (0: black, 1: white). (a) an arbitrary sentence. (b–d) three randomly selected samples among the sentences without any unknown words and of length between 10 and 20 words from the test set.
One of the motivations behind the proposed approach was the use of a fixed-length context vector in the basic encoder–decoder approach. We conjectured that this limitation may make the basic encoder–decoder approach to underperform with long sentences. In Fig. 2, we see that the performance of RNNencdec dramatically drops as the length of the sentences increases. On the other hand, both RNNsearch-30 and RNNsearch-50 are more robust to the length of the sentences. RNNsearch50, especially, shows no performance deterioration even with sentences of length 50 or more. This superiority of the proposed model over the basic encoder–decoder is further confirmed by the fact that the RNNsearch-30 even outperforms RNNencdec-50 (see Table 1).

<!-- page: 7 -->

|Model|All|No UNK<sup>_◦_</sup>|
|---|---|---|
|RNNencdec-30|13.93|24.19|
|RNNsearch-30|21.50|31.44|
|RNNencdec-50|17.82|26.71|
|RNNsearch-50|26.75|34.16|
|RNNsearch-50<sup>_⋆_</sup>|28.45|36.15|
|Moses|33.30|35.63|
> **Table 1:** BLEU scores of the trained models computed on the test set. The second and third columns show respectively the scores on all the sentences and, on the sentences without any unknown word in themselves and in the reference translations. Note that RNNsearch-50<sup>_⋆_</sup> was trained much longer until the performance on the development set stopped improving. ( _◦_ ) We disallowed the models to generate [UNK] tokens when only the sentences having no unknown words were evaluated (last column).
### 5.2 QUALITATIVE ANALYSIS
#### 5.2.1 ALIGNMENT
The proposed approach provides an intuitive way to inspect the (soft-)alignment between the words in a generated translation and those in a source sentence. This is done by visualizing the annotation weights _αij_ from Eq. (6), as in Fig. 3. Each row of a matrix in each plot indicates the weights associated with the annotations. From this we see which positions in the source sentence were considered more important when generating the target word.

We can see from the alignments in Fig. 3 that the alignment of words between English and French is largely monotonic. We see strong weights along the diagonal of each matrix. However, we also observe a number of non-trivial, non-monotonic alignments. Adjectives and nouns are typically ordered differently between French and English, and we see an example in Fig. 3 (a). From this figure, we see that the model correctly translates a phrase [European Economic Area] into [zone ´economique europ´een]. The RNNsearch was able to correctly align [zone] with [Area], jumping over the two words ([European] and [Economic]), and then looked one word back at a time to complete the whole phrase [zone ´economique europ´eenne].

The strength of the soft-alignment, opposed to a hard-alignment, is evident, for instance, from Fig. 3 (d). Consider the source phrase [the man] which was translated into [l’ homme]. Any hard alignment will map [the] to [l’] and [man] to [homme]. This is not helpful for translation, as one must consider the word following [the] to determine whether it should be translated into [le], [la], [les] or [l’]. Our soft-alignment solves this issue naturally by letting the model look at both [the] and [man], and in this example, we see that the model was able to correctly translate [the] into [l’]. We observe similar behaviors in all the presented cases in Fig. 3. An additional benefit of the soft alignment is that it naturally deals with source and target phrases of different lengths, without requiring a counter-intuitive way of mapping some words to or from nowhere ([NULL]) (see, e.g., Chapters 4 and 5 of Koehn, 2010).

#### 5.2.2 LONG SENTENCES
As clearly visible from Fig. 2 the proposed model (RNNsearch) is much better than the conventional model (RNNencdec) at translating long sentences. This is likely due to the fact that the RNNsearch does not require encoding a long sentence into a fixed-length vector perfectly, but only accurately encoding the parts of the input sentence that surround a particular word.

As an example, consider this source sentence from the test set:

_An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre_ _<u>to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.</u>_

The RNNencdec-50 translated this sentence into:

_Un privil`ege d’admission est le droit d’un m´edecin de reconnaˆıtre un patient `a l’hˆopital ou un centre m´edical_ _<u>d’un diagnostic ou de prendre un diagnostic en fonction de son etat´ de sante.´</u>_

<!-- page: 8 -->

The RNNencdec-50 correctly translated the source sentence until [a medical center]. However, from there on (underlined), it deviated from the original meaning of the source sentence. For instance, it replaced [based on his status as a health care worker at a hospital] in the source sentence with [en fonction de son ´etat de sant´e] (“based on his state of health”).

On the other hand, the RNNsearch-50 generated the following correct translation, preserving the whole meaning of the input sentence without omitting any details:

_Un privil`ege d’admission est le droit d’un m´edecin d’admettre un patient `a un hˆopital ou un centre m´edical_ _<u>pour effectuer un diagnostic ou une procedure,´ selon son statut de travailleur des soins de sante´ a` l’hopital.ˆ</u>_

Let us consider another sentence from the test set:

_This kind of experience is part of Disney’s efforts to ”extend the lifetime of its series and build new relationships with audiences_ _<u>via digital platforms that are becoming ever more important,” he added.</u>_

The translation by the RNNencdec-50 is

_Ce type d’exp´erience fait partie des initiatives du Disney pour ”prolonger la dur´ee de vie de ses nouvelles et de d´evelopper des liens avec les_ _<u>lecteurs numeriques´ qui deviennent plus complexes.</u>_

As with the previous example, the RNNencdec began deviating from the actual meaning of the source sentence after generating approximately 30 words (see the underlined phrase). After that point, the quality of the translation deteriorates, with basic mistakes such as the lack of a closing quotation mark.

Again, the RNNsearch-50 was able to translate this long sentence correctly:

_Ce genre d’exp´erience fait partie des efforts de Disney pour ”prolonger la dur´ee de vie de ses s´eries et cr´eer de nouvelles relations avec des publics_ _<u>via des plateformes numeriques´ de plus en plus importantes”, a-t-il ajoute.´</u>_

In conjunction with the quantitative results presented already, these qualitative observations confirm our hypotheses that the RNNsearch architecture enables far more reliable translation of long sentences than the standard RNNencdec model.

In Appendix C, we provide a few more sample translations of long source sentences generated by the RNNencdec-50, RNNsearch-50 and Google Translate along with the reference translations.

## 6 RELATED WORK
### 6.1 LEARNING TO ALIGN
A similar approach of aligning an output symbol with an input symbol was proposed recently by Graves (2013) in the context of handwriting synthesis. Handwriting synthesis is a task where the model is asked to generate handwriting of a given sequence of characters. In his work, he used a mixture of Gaussian kernels to compute the weights of the annotations, where the location, width and mixture coefficient of each kernel was predicted from an alignment model. More specifically, his alignment was restricted to predict the location such that the location increases monotonically.

The main difference from our approach is that, in (Graves, 2013), the modes of the weights of the annotations only move in one direction. In the context of machine translation, this is a severe limitation, as (long-distance) reordering is often needed to generate a grammatically correct translation (for instance, English-to-German).

Our approach, on the other hand, requires computing the annotation weight of every word in the source sentence for each word in the translation. This drawback is not severe with the task of translation in which most of input and output sentences are only 15–40 words. However, this may limit the applicability of the proposed scheme to other tasks.

<!-- page: 9 -->

### 6.2 NEURAL NETWORKS FOR MACHINE TRANSLATION
Since Bengio _et al._ (2003) introduced a neural probabilistic language model which uses a neural network to model the conditional probability of a word given a fixed number of the preceding words, neural networks have widely been used in machine translation. However, the role of neural networks has been largely limited to simply providing a single feature to an existing statistical machine translation system or to re-rank a list of candidate translations provided by an existing system.

For instance, Schwenk (2012) proposed using a feedforward neural network to compute the score of a pair of source and target phrases and to use the score as an additional feature in the phrase-based statistical machine translation system. More recently, Kalchbrenner and Blunsom (2013) and Devlin _et al._ (2014) reported the successful use of the neural networks as a sub-component of the existing translation system. Traditionally, a neural network trained as a target-side language model has been used to rescore or rerank a list of candidate translations (see, e.g., Schwenk _et al._ , 2006).

Although the above approaches were shown to improve the translation performance over the state-of-the-art machine translation systems, we are more interested in a more ambitious objective of designing a completely new translation system based on neural networks. The neural machine translation approach we consider in this paper is therefore a radical departure from these earlier works. Rather than using a neural network as a part of the existing system, our model works on its own and generates a translation from a source sentence directly.

## 7 CONCLUSION
The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from which a translation will be decoded. We conjectured that the use of a fixed-length context vector is problematic for translating long sentences, based on a recent empirical study reported by Cho _et al._ (2014b) and Pouget-Abadie _et al._ (2014).

In this paper, we proposed a novel architecture that addresses this issue. We extended the basic encoder–decoder by letting a model (soft-)search for a set of input words, or their annotations computed by an encoder, when generating each target word. This frees the model from having to encode a whole source sentence into a fixed-length vector, and also lets the model focus only on information relevant to the generation of the next target word. This has a major positive impact on the ability of the neural machine translation system to yield good results on longer sentences. Unlike with the traditional machine translation systems, all of the pieces of the translation system, including the alignment mechanism, are jointly trained towards a better log-probability of producing correct translations.

We tested the proposed model, called RNNsearch, on the task of English-to-French translation. The experiment revealed that the proposed RNNsearch outperforms the conventional encoder–decoder model (RNNencdec) significantly, regardless of the sentence length and that it is much more robust to the length of a source sentence. From the qualitative analysis where we investigated the (soft-)alignment generated by the RNNsearch, we were able to conclude that the model can correctly align each target word with the relevant words, or their annotations, in the source sentence as it generated a correct translation.

Perhaps more importantly, the proposed approach achieved a translation performance comparable to the existing phrase-based statistical machine translation. It is a striking result, considering that the proposed architecture, or the whole family of neural machine translation, has only been proposed as recently as this year. We believe the architecture proposed here is a promising step toward better machine translation and a better understanding of natural languages in general.

One of challenges left for the future is to better handle unknown, or rare words. This will be required for the model to be more widely used and to match the performance of current state-of-the-art machine translation systems in all contexts.

<!-- page: 10 -->

## ACKNOWLEDGMENTS
The authors would like to thank the developers of Theano (Bergstra _et al._ , 2010; Bastien _et al._ , 2012). We acknowledge the support of the following agencies for research funding and computing support: NSERC, Calcul Qu´ebec, Compute Canada, the Canada Research Chairs and CIFAR. Bahdanau thanks the support from Planet Intelligent Systems GmbH. We also thank Felix Hill, Bart van Merri´enboer, Jean Pouget-Abadie, Coline Devin and Tae-Ho Kim.

## REFERENCES
- Axelrod, A., He, X., and Gao, J. (2011). Domain adaptation via pseudo in-domain data selection. In _Proceedings of the ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 355–362. Association for Computational Linguistics.

- Bastien, F., Lamblin, P., Pascanu, R., Bergstra, J., Goodfellow, I. J., Bergeron, A., Bouchard, N., and Bengio, Y. (2012). Theano: new features and speed improvements. Deep Learning and Unsupervised Feature Learning NIPS 2012 Workshop.

- Bengio, Y., Simard, P., and Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. _IEEE Transactions on Neural Networks_ , **5** (2), 157–166.

- Bengio, Y., Ducharme, R., Vincent, P., and Janvin, C. (2003). A neural probabilistic language model. _J. Mach. Learn. Res._ , **3** , 1137–1155.

- Bergstra, J., Breuleux, O., Bastien, F., Lamblin, P., Pascanu, R., Desjardins, G., Turian, J., WardeFarley, D., and Bengio, Y. (2010). Theano: a CPU and GPU math expression compiler. In _Proceedings of the Python for Scientific Computing Conference (SciPy)_ . Oral Presentation.

- Boulanger-Lewandowski, N., Bengio, Y., and Vincent, P. (2013). Audio chord recognition with recurrent neural networks. In _ISMIR_ .

- Cho, K., van Merrienboer, B., Gulcehre, C., Bougares, F., Schwenk, H., and Bengio, Y. (2014a). Learning phrase representations using RNN encoder-decoder for statistical machine translation. In _Proceedings of the Empiricial Methods in Natural Language Processing (EMNLP 2014)_ . to appear.

- Cho, K., van Merri¨enboer, B., Bahdanau, D., and Bengio, Y. (2014b). On the properties of neural machine translation: Encoder–Decoder approaches. In _Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation_ . to appear.

- Devlin, J., Zbib, R., Huang, Z., Lamar, T., Schwartz, R., and Makhoul, J. (2014). Fast and robust neural network joint models for statistical machine translation. In _Association for Computational Linguistics_ .

- Forcada, M. L. and Neco,<sup>˜</sup> R. P. (1997). Recursive hetero-associative memories for translation. In J. Mira, R. Moreno-D´ıaz, and J. Cabestany, editors, _Biological and Artificial Computation: From Neuroscience to Technology_ , volume 1240 of _Lecture Notes in Computer Science_ , pages 453–462. Springer Berlin Heidelberg.

- Goodfellow, I., Warde-Farley, D., Mirza, M., Courville, A., and Bengio, Y. (2013). Maxout networks. In _Proceedings of The 30th International Conference on Machine Learning_ , pages 1319– 1327.

- Graves, A. (2012). Sequence transduction with recurrent neural networks. In _Proceedings of the 29th International Conference on Machine Learning (ICML 2012)_ .

- Graves, A. (2013). Generating sequences with recurrent neural networks. _arXiv:_ 1308.0850 [cs.NE].

- Graves, A., Jaitly, N., and Mohamed, A.-R. (2013). Hybrid speech recognition with deep bidirectional LSTM. In _Automatic Speech Recognition and Understanding (ASRU), 2013 IEEE Workshop on_ , pages 273–278.

<!-- page: 11 -->

- Hermann, K. and Blunsom, P. (2014). Multilingual distributed representations without word alignment. In _Proceedings of the Second International Conference on Learning Representations (ICLR 2014)_ .

- Hochreiter, S. (1991). Untersuchungen zu dynamischen neuronalen Netzen. Diploma thesis, Institut f¨ur Informatik, Lehrstuhl Prof. Brauer, Technische Universit¨at M¨unchen.

- Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. _Neural Computation_ , **9** (8), 1735–1780.

- Kalchbrenner, N. and Blunsom, P. (2013). Recurrent continuous translation models. In _Proceedings of the ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1700–1709. Association for Computational Linguistics.

- Koehn, P. (2010). _Statistical Machine Translation_ . Cambridge University Press, New York, NY, USA.

- Koehn, P., Och, F. J., and Marcu, D. (2003). Statistical phrase-based translation. In _Proceedings of the 2003 Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology - Volume 1_ , NAACL ’03, pages 48–54, Stroudsburg, PA, USA. Association for Computational Linguistics.

- Pascanu, R., Mikolov, T., and Bengio, Y. (2013a). On the difficulty of training recurrent neural networks. In _ICML’2013_ .

- Pascanu, R., Mikolov, T., and Bengio, Y. (2013b). On the difficulty of training recurrent neural networks. In _Proceedings of the 30th International Conference on Machine Learning (ICML 2013)_ .

- Pascanu, R., Gulcehre, C., Cho, K., and Bengio, Y. (2014). How to construct deep recurrent neural networks. In _Proceedings of the Second International Conference on Learning Representations (ICLR 2014)_ .

- Pouget-Abadie, J., Bahdanau, D., van Merri¨enboer, B., Cho, K., and Bengio, Y. (2014). Overcoming the curse of sentence length for neural machine translation using automatic segmentation. In _Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation_ . to appear.

- Schuster, M. and Paliwal, K. K. (1997). Bidirectional recurrent neural networks. _Signal Processing, IEEE Transactions on_ , **45** (11), 2673–2681.

- Schwenk, H. (2012). Continuous space translation models for phrase-based statistical machine translation. In M. Kay and C. Boitet, editors, _Proceedings of the 24th International Conference on Computational Linguistics (COLIN)_ , pages 1071–1080. Indian Institute of Technology Bombay.

- Schwenk, H., Dchelotte, D., and Gauvain, J.-L. (2006). Continuous space language models for statistical machine translation. In _Proceedings of the COLING/ACL on Main conference poster sessions_ , pages 723–730. Association for Computational Linguistics.

- Sutskever, I., Vinyals, O., and Le, Q. (2014). Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems (NIPS 2014)_ .

- Zeiler, M. D. (2012). ADADELTA: An adaptive learning rate method. _arXiv:_ 1212.5701 [cs.LG].

<!-- page: 12 -->

## A MODEL ARCHITECTURE
## A.1 ARCHITECTURAL CHOICES
The proposed scheme in Section 3 is a general framework where one can freely define, for instance, the activation functions _f_ of recurrent neural networks (RNN) and the alignment model _a_ . Here, we describe the choices we made for the experiments in this paper.

## A.1.1 RECURRENT NEURAL NETWORK
For the activation function _f_ of an RNN, we use the gated hidden unit recently proposed by Cho _et al._ (2014a). The gated hidden unit is an alternative to the conventional _simple_ units such as an element-wise tanh. This gated unit is similar to a long short-term memory (LSTM) unit proposed earlier by Hochreiter and Schmidhuber (1997), sharing with it the ability to better model and learn long-term dependencies. This is made possible by having computation paths in the unfolded RNN for which the product of derivatives is close to 1. These paths allow gradients to flow backward easily without suffering too much from the vanishing effect (Hochreiter, 1991; Bengio _et al._ , 1994; Pascanu _et al._ , 2013a). It is therefore possible to use LSTM units instead of the gated hidden unit described here, as was done in a similar context by Sutskever _et al._ (2014).

The new state _si_ of the RNN employing _n_ gated hidden units<sup>8</sup> is computed by

$$
si = f(si-1, y_{i}-1, ci) = (1 -z_{i}) ◦si-1 + z_{i} ◦˜si,
$$

where _◦_ is an element-wise multiplication, and _zi_ is the output of the update gates (see below). The proposed updated state ˜ _si_ is computed by

$$
˜si = tanh (We(y_{i}-1) + U [ri ◦si-1] + Cci) ,
$$

where _e_ ( _yi−_ 1) _∈_ R<sup>_m_</sup> is an _m_ -dimensional embedding of a word _yi−_ 1, and _ri_ is the output of the reset gates (see below). When _yi_ is represented as a 1-of- _K_ vector, _e_ ( _yi_ ) is simply a column of an embedding matrix _E ∈_ R<sup>_m×K_</sup> . Whenever possible, we omit bias terms to make the equations less cluttered.

The update gates _zi_ allow each hidden unit to maintain its previous activation, and the reset gates _ri_ control how much and what information from the previous state should be reset. We compute them by

$$
z_{i} = \sigma (Wze(y_{i}-1) + Uzsi-1 + Czci) , ri = \sigma (Wre(y_{i}-1) + Ursi-1 + Crci) ,
$$

where _σ_ ( _·_ ) is a logistic sigmoid function.

At each step of the decoder, we compute the output probability (Eq. (4)) as a multi-layered function (Pascanu _et al._ , 2014). We use a single hidden layer of maxout units (Goodfellow _et al._ , 2013) and normalize the output probabilities (one for each word) with a softmax function (see Eq. (6)).

## A.1.2 ALIGNMENT MODEL
The alignment model should be designed considering that the model needs to be evaluated _Tx × Ty_ times for each sentence pair of lengths _Tx_ and _Ty_ . In order to reduce computation, we use a singlelayer multilayer perceptron such that

$$
a(si-1, hj) = v⊤a tanh (Wasi-1 + Uahj) ,
$$

where _Wa ∈_ R<sup>_n×n_</sup> _, Ua ∈_ R<sup>_n×_2</sup><sup>_n_</sup> and _va ∈_ R<sup>_n_</sup> are the weight matrices. Since _Uahj_ does not depend on _i_ , we can pre-compute it in advance to minimize the computational cost.

> 8 Here, we show the formula of the decoder. The same formula can be used in the encoder by simply ignoring the context vector _ci_ and the related terms.

<!-- page: 13 -->

## A.2 DETAILED DESCRIPTION OF THE MODEL
## A.2.1 ENCODER
In this section, we describe in detail the architecture of the proposed model (RNNsearch) used in the experiments (see Sec. 4–5). From here on, we omit all bias terms in order to increase readability.

The model takes a source sentence of 1-of-K coded word vectors as input

$$
x = (x_{1}, . . . , xTx), x_{i} \in RKx
$$

and outputs a translated sentence of 1-of-K coded word vectors

$$
y = (y_{1}, . . . , yTy), y_{i} \in RKy,
$$

where _Kx_ and _Ky_ are the vocabulary sizes of source and target languages, respectively. _Tx_ and _Ty_ respectively denote the lengths of source and target sentences.

First, the forward states of the bidirectional recurrent neural network (BiRNN) are computed:

where

$$
( (1 --→z i) ◦-→h i-1 + -→z i ◦-→h i , if i > 0-→h i = 0 , if i = 0 -→h i = tanh -→WExi + -→U h-→r i ◦-→h i-1 i -→z i =\sigma -→W zExi + -→U z -→h i-1 -→r i =\sigma -→W rExi + -→U r -→hi-1 .
$$

_E ∈_ R<sup>_m×Kx_</sup> is the word embedding matrix. _W,_<sup>_−→−→_</sup> _W z, W_<sup>_−→_</sup> _r ∈_ R<sup>_n×m_</sup> ,<sup>_−→_</sup> _U ,_<sup>_−→_</sup> _U z,_<sup>_−→_</sup> _U r ∈_ R<sup>_n×n_</sup> are weight matrices. _m_ and _n_ are the word embedding dimensionality and the number of hidden units, respectively. _σ_ ( _·_ ) is as usual a logistic sigmoid function.

The backward states (<sup>_←−_</sup> _h_ 1 _, · · · ,_<sup>_←−_</sup> _h Tx_ ) are computed similarly. We share the word embedding matrix _E_ between the forward and backward RNNs, unlike the weight matrices.

We concatenate the forward and backward states to to obtain the annotations ( _h_ 1 _, h_ 2 _, · · · , hTx_ ), where

$$
" -→h i # hi = ←-h i (7)
$$

## A.2.2 DECODER
The hidden state _si_ of the decoder given the annotations from the encoder is computed by

$$
si =(1 -z_{i}) ◦si-1 + z_{i} ◦˜si,
$$

where

$$
˜si = tanh (WEyi-1 + U [ri ◦si-1] + Cci) z_{i} =\sigma (WzEyi-1 + Uzsi-1 + Czci) ri =\sigma (WrEyi-1 + Ursi-1 + Crci)
$$

_E_ is the word embedding matrix for the target language. _W, Wz, Wr ∈_ R<sup>_n×m_</sup> , _U, Uz, Ur ∈_ R<sup>_n×n_</sup> , and _C, Cz, Cr ∈_ R<sup>_n×_2</sup><sup>_n_</sup> are weights. Again, _m_ and _n_ are the word embedding dimensionality and the number of hidden units, respectively. The initial hidden state _s_ 0 is computed by _s_ 0 = tanh _Ws←−h_ 1 _,_ where _Ws ∈_ R<sup>_n×n_</sup> .

The context vector _ci_ are recomputed at each step by the alignment model:

$$
Tx ci = X \alpha ijhj, j=1
$$

<!-- page: 14 -->

|Model|Updates (_×_10<sup>5</sup>)|Epochs|Hours|GPU|Train NLL|Dev. NLL|
|---|---|---|---|---|---|---|
|RNNenc-30|8.46|6.4|109|TITAN BLACK|28.1|53.0|
|RNNenc-50|6.00|4.5|108|Quadro K-6000|44.0|43.6|
|RNNsearch-30|4.71|3.6|113|TITAN BLACK|26.7|47.2|
|RNNsearch-50|2.88|2.2|111|Quadro K-6000|40.7|38.1|
|RNNsearch-50<sup>_⋆_</sup>|6.67|5.0|252|Quadro K-6000|36.7|35.2|
> **Table 2:** Learning statistics and relevant information. Each update corresponds to updating the parameters once using a single minibatch. One epoch is one pass through the training set. NLL is the average conditional log-probabilities of the sentences in either the training set or the development set. Note that the lengths of the sentences differ.
where

$$
exp (eij) \alpha ij = PTx k=1 exp (eik) eij =v⊤a tanh (Wasi-1 + Uahj) ,
$$

and _hj_ is the _j_ -th annotation in the source sentence (see Eq. (7)). _va ∈_ R<sup>_n′_</sup> _, Wa ∈_ R<sup>_n′×n_</sup> and _Ua ∈_ R<sup>_n′×_2</sup><sup>_n_</sup> are weight matrices. Note that the model becomes RNN Encoder–Decoder (Cho _et al._ , 2014a), if we fix _ci_ to<sup>_−→_</sup> _h Tx_ .

With the decoder state _si−_ 1, the context _ci_ and the last generated word _yi−_ 1, we define the probability of a target word _yi_ as

where

$$
p(y_{i}|si, y_{i}-1, ci) ∝exp y⊤i Woti , ⊤ ti = max ˜ti,2j-1, ˜ti,2j j=1,...,l
$$

and _t_<sup>˜</sup> _i,k_ is the _k_ -th element of a vector _t_<sup>˜</sup> _i_ which is computed by

$$
˜ti =Uosi-1 + VoEyi-1 + Coci.
$$

_Wo ∈_ R<sup>_Ky×l_</sup> , _Uo ∈_ R<sup>2</sup><sup>_l×n_</sup> , _Vo ∈_ R<sup>2</sup><sup>_l×m_</sup> and _Co ∈_ R<sup>2</sup><sup>_l×_2</sup><sup>_n_</sup> are weight matrices. This can be understood as having a deep output (Pascanu _et al._ , 2014) with a single maxout hidden layer (Goodfellow _et al._ , 2013).

## A.2.3 MODEL SIZE
For all the models used in this paper, the size of a hidden layer _n_ is 1000, the word embedding dimensionality _m_ is 620 and the size of the maxout hidden layer in the deep output _l_ is 500. The number of hidden units in the alignment model _n_<sup>_′_</sup> is 1000.

## B TRAINING PROCEDURE
## B.1 PARAMETER INITIALIZATION
We initialized the recurrent weight matrices _U, Uz, Ur,_<sup>_←−_</sup> _U ,_<sup>_←−_</sup> _U z,_<sup>_←−_</sup> _U r,_<sup>_−→_</sup> _U ,_<sup>_−→_</sup> _U z_ and<sup>_−→_</sup> _U r_ as random orthogonal matrices. For _Wa_ and _Ua_ , we initialized them by sampling each element from the Gaussian distribution of mean 0 and variance 0 _._ 001<sup>2</sup> . All the elements of _Va_ and all the bias vectors were initialized to zero. Any other weight matrix was initialized by sampling from the Gaussian distribution of mean 0 and variance 0 _._ 01<sup>2</sup> .

## B.2 TRAINING
We used the stochastic gradient descent (SGD) algorithm. Adadelta (Zeiler, 2012) was used to automatically adapt the learning rate of each parameter ( _ϵ_ = 10<sup>_−_6</sup> and _ρ_ = 0 _._ 95). We explicitly

<!-- page: 15 -->

normalized the _L_ 2-norm of the gradient of the cost function each time to be at most a predefined threshold of 1, when the norm was larger than the threshold (Pascanu _et al._ , 2013b). Each SGD update direction was computed with a minibatch of 80 sentences.

At each update our implementation requires time proportional to the length of the longest sentence in a minibatch. Hence, to minimize the waste of computation, before every 20-th update, we retrieved 1600 sentence pairs, sorted them according to the lengths and split them into 20 minibatches. The training data was shuffled once before training and was traversed sequentially in this manner.

In Tables 2 we present the statistics related to training all the models used in the experiments.

## C TRANSLATIONS OF LONG SENTENCES
|Source|An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre<br>to carryout a diagnosis or aprocedure,based on his status as a health care worker at a hospital.|
|---|---|
|Reference|Le privil`ege d’admission est le droit d’un m´edecin, en vertu de son statut de membre soignant<br>d’un hˆopital, d’admettre un patient dans un hˆopital ou un centre m´edical afin d’y d´elivrer un<br>diagnostic ou un traitement.|
|RNNenc-50|Un privil`ege d’admission est le droit d’un m´edecin de reconnaˆıtre un patient `a l’hˆopital ou un<br>centre m´edical d’un diagnostic ou deprendre un diagnostic en fonction de son ´etat de sant´e.|
|RNNsearch-50|Un privil`ege d’admission est le droit d’un m´edecin d’admettre un patient `a un hˆopital ou un<br>centre m´edical pour effectuer un diagnostic ou une proc´edure, selon son statut de travailleur des<br>soins de sant´e `a l’hˆopital.|
|Google<br>Translate|Un privil`ege admettre est le droit d’un m´edecin d’admettre un patient dans un hˆopital ou un<br>centre m´edical pour effectuer un diagnostic ou une proc´edure, fond´ee sur sa situation en tant<br>que travailleur de soins de sant´e dans un hˆopital.|
|Source|This kind of experience is part of Disney’s efforts to ”extend the lifetime of its series and build<br>new relationships with audiences via digital platforms that are becoming ever more important,”<br>he added.|
|Reference|Ce type d’exp´erience entre dans le cadre des efforts de Disney pour ”´etendre la dur´ee de<br>vie de ses s´eries et construire de nouvelles relations avec son public grˆace `a des plateformes<br>num´eriquesqui sont deplus enplus importantes”,a-t-il ajout´e.|
|RNNenc-50|Ce type d’exp´erience fait partie des initiatives du Disney pour ”prolonger la dur´ee de vie de<br>ses nouvelles et de d´evelopper des liens avec les lecteurs num´eriques qui deviennent plus com-<br>plexes.|
|RNNsearch-50|Ce genre d’exp´erience fait partie des efforts de Disney pour ”prolonger la dur´ee de vie de ses<br>s´eries et cr´eer de nouvelles relations avec des publics via des plateformes num´eriques de plus<br>enplus importantes”,a-t-il ajout´e.|
|Google<br>Translate|Ce genre d’exp´erience fait partie des efforts de Disney `a “´etendre la dur´ee de vie de sa s´erie et<br>construire de nouvelles relations avec le public par le biais des plates-formes num´eriques qui<br>deviennent deplus enplus important”,at-il ajout´e.|
|Source|In a press conference on Thursday, Mr Blair stated that there was nothing in this video that might<br>constitute a ”reasonable motive” that could lead to criminal charges being brought against the<br>mayor.|
|Reference|En conf´erence de presse, jeudi, M. Blair a affirm´e qu’il n’y avait rien dans cette vid´eo qui puisse<br>constituer des ”motifs raisonnables” pouvant mener au d´epˆot d’une accusation criminelle contre<br>le maire.|
|RNNenc-50|Lors de la conf´erence de presse de jeudi, M. Blair a dit qu’il n’y avait rien dans cette vid´eo qui<br>pourrait constituer une ”motivation raisonnable” pouvant entraˆıner des accusations criminelles<br>port´ees contre le maire.|
|RNNsearch-50|Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vid´eo qui<br>pourrait constituer un ”motif raisonnable” qui pourrait conduire `a des accusations criminelles<br>contre le maire.|
|Google<br>Translate|Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vido<br>qui pourrait constituer un ”motif raisonnable” qui pourrait mener `a des accusations criminelles<br>portes contre le maire.|
> **Table 3:** The translations generated by RNNenc-50 and RNNsearch-50 from long source sentences (30 words or more) selected from the test set. For each source sentence, we also show the goldstandard translation. The translations by Google Translate were made on 27 August 2014.
