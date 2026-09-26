<!-- page: 1 -->

# A Gentle Introduction to Deep Learning for Graphs

Davide Bacciu\(^a\), Federico Errica\(^a\), Alessio Micheli\(^a\), Marco Podda\(^a\)

\(^a\)Department of Computer Science, University of Pisa, Italy.

arXiv:1912.12693v2 [cs.LG] 15 Jun 2020

## Abstract

The adaptive processing of graph data is a long-standing research topic that has been lately consolidated as a theme of major interest in the deep learning community. The snap increase in the amount and breadth of related research has come at the price of little systematization of knowledge and attention to earlier literature. This work is a tutorial introduction to the field of deep learning for graphs. It favors a consistent and progressive presentation of the main concepts and architectural aspects over an exposition of the most recent literature, for which the reader is referred to available surveys. The paper takes a top-down view of the problem, introducing a generalized formulation of graph representation learning based on a local and iterative approach to structured information processing. Moreover, it introduces the basic building blocks that can be combined to design novel and effective neural models for graphs. We complement the methodological exposition with a discussion of interesting research challenges and applications in the field.

*Keywords:* deep learning for graphs, graph neural networks, learning for structured data

## 1. Introduction

Graphs are a powerful tool to represent data that is produced by a variety of artificial and natural processes. A graph has a compositional nature, being a compound of atomic information pieces, and a relational nature, as the links defining its structure denote relationships between the linked entities. Also, graphs allow us to represent a multitude of associations through link orientation

Manuscript accepted for publication in Neural Networks — June 16, 2020

<!-- page: 2 -->

and labels, such as discrete relationship types, chemical properties, and strength of the molecular bonds.

But most importantly, graphs are ubiquitous. In chemistry and material sciences, they represent the molecular structure of a compound, protein interaction and drug interaction networks, biological and bio-chemical associations. In social sciences, networks are widely used to represent people's relationships, whereas they model complex buying behaviors in recommender systems.

The richness of such data, together with the increasing availability of large repositories, has motivated a recent surge in interest in deep learning models that process graphs in an adaptive fashion. The methodological and practical challenges related to such an overarching goal are several. First, learning models for graphs should be able to cater for samples that can vary in size and topology. In addition to that, information about node identity and ordering across multiple samples is rarely available. Also, graphs are discrete objects, which poses restrictions to differentiability. Moreover, their combinatorial nature hampers the application of exhaustive search methods. Lastly, the most general classes of graphs allow the presence of loops, which are a source of complexity when it comes to message passing and node visits. In other words, dealing with graph data brings in unparalleled challenges, in terms of expressiveness and computational complexity, when compared to learning with vectorial data. Hence, this is an excellent development and testing field for novel neural network methodologies.

Despite the recent burst of excitement of the deep learning community, the area of neural networks for graphs has a long-standing and consolidated history, rooting in the early nineties with seminal works on Recursive Neural Networks for tree structured data (see [114, 41, 10] and the references therein). Such an approach has later been rediscovered within the context of natural language processing applications [113, 115]. Also, it has been progressively extended to more complex and richer structures, starting from directed acyclic graphs [89], for which universal approximation guarantees have been given [56]. The recursive processing of structures has also been leveraged by probabilistic approaches, first

2

<!-- page: 3 -->

as a purely theoretical model [41] and later more practically through efficient approximated distributions [6].

The recursive models share the idea of a (neural) state transition system that traverses the structure to compute its embedding. The main issue in extending such approaches to general graphs (cyclic/acyclic, directed/undirected) was the processing of cycles. Indeed, the mutual dependencies between state variables cannot be easily modeled by the recursive neural units. The earliest models to tackle this problem have been the Graph Neural Network [104] and the Neural Network for Graphs [88]. The former is based on a state transition system similar to the recursive neural networks, but it allows cycles in the state computation within a contractive setting of the dynamical system. The Neural Network for Graphs, instead, exploits the idea that mutual dependencies can be managed by leveraging the representations from previous layers in the architecture. This way, the model breaks the recursive dependencies in the graph cycles with a multi-layered architecture. Both models have pioneered the field by laying down the foundations of two of the main approaches for graph processing, namely the recurrent [104] and the feedforward [88] ones. In particular, the latter has now become the predominant approach, under the umbrella term of graph convolutional (neural) networks (named after approaches [72, 54] which reintroduced the above concepts around 2015).

This paper takes pace from this historical perspective to provide a gentle introduction to the field of neural networks for graphs, also referred to as deep learning for graphs in modern terminology. It is intended to be a paper of tutorial nature, favoring a well-founded, consistent, and progressive opening to the main concepts and building blocks to assemble deep architectures for graphs. Therefore, it does not aim at being an exposition of the most recently published works on the topic. The motivations for such a tutorial approach are multifaceted. On the one hand, the surge of recent works on deep learning for graphs has come at the price of a certain forgetfulness, if not lack of appropriate referencing, of pioneering and consolidated works. As a consequence, there is the risk of running through a wave of rediscovery of known results and models.

3

<!-- page: 4 -->

On the other hand, the community is starting to notice troubling trends in the assessment of deep learning models for graphs [108, 34], which calls for a more principled approach to the topic. Lastly, a certain number of survey papers have started to appear in the literature [7, 19, 48, 55, 144, 130, 143], while a more slowly-paced introduction to the methodology seems lacking.

This tutorial takes a top-down approach to the field while maintaining a clear historical perspective on the introduction of the main concepts and ideas. To this end, in Section 2, we first provide a generalized formulation of the problem of representation learning in graphs, introducing and motivating the architecture roadmap that we will be following throughout the rest of the paper. We will focus, in particular, on methods that deal with local and iterative processing of information as these are more consistent with the operational regime of neural networks. In this respect, we will pay less attention to global approaches (i.e., assuming a single fixed adjacency matrix) based on spectral graph theory. We will then proceed, in Section 3, to introduce the basic building blocks that can be assembled and combined to create modern deep learning architectures for graphs. In this context, we will introduce the concepts of graph convolutions as local neighborhood aggregation functions, the use of attention, sampling, and pooling operators defined over graphs, and we will conclude with a discussion on aggregation functions that compute whole-structure embeddings. Our characterization of the methodology continues, in Section 4, with a discussion of the main learning tasks undertaken in graph representation learning, together with the associated cost functions and a characterization of the related inductive biases. The final part of the paper surveys other related approaches and tasks (Section 5), and it discusses interesting research challenges (Section 6) and applications (Section 7). We conclude the paper with some final considerations and hints for future research directions.

## 2. High-level Overview

We begin with a high-level overview of deep learning for graphs. To this aim, we first summarize the necessary mathematical notation. Secondly, we present

4

<!-- page: 5 -->

[FIGURE: Figure 1: (a) A directed graph with oriented arcs is shown. (b) If the graph is undirected, we can transform it into a directed one to obtain a viable input for graph learning methods. In particular, each edge is replaced by two oriented and opposite arcs with identical edge features. (c) We visually represent the (open) neighborhood of node \(v_1\).]

Text in figure:
- (a), (b), (c)
- \(v_1\), \(v_2\), \(v_3\), \(v_4\)
- \(\mathcal{N}_{v_1}\)

the main ideas the vast majority of works in the literature borrow from.

### 2.1. Mathematical Notation

Formally, a graph \(g = (\mathcal{V}_g, \mathcal{E}_g, \mathcal{X}_g, \mathcal{A}_g)\) is defined by a set of vertexes \(\mathcal{V}_g\) (also referred to as nodes) and by a set of edges (or arcs) \(\mathcal{E}_g\) connecting pairs of nodes [15]. When the pairs are unordered, i.e., \(\mathcal{E}_g \subseteq \{\{u, v\} \mid u, v \in \mathcal{V}_g\}\), we speak of undirected graphs and non-oriented edges. On the other hand, when pairs of nodes are ordered, i.e., \(\mathcal{E}_g \subseteq \{(u, v) \mid u, v \in \mathcal{V}_g\}\), we say a graph is directed and its edges are oriented. In both cases, the ends of an edge are said to be incident with the edge and vice versa. \(\mathcal{E}_g\) specifies how nodes are interconnected in the graph, but we can also encode this structural information into an adjacency matrix. Specifically, the adjacency matrix of \(g\) is the \(|\mathcal{V}_g| \times |\mathcal{V}_g|\) binary square matrix \(\mathbf{A}\) where \(\mathbf{A}_{uv} \in \{0, 1\}\) is 1 if there is an arc connecting \(u\) and \(v\), and it is 0 otherwise. It follows that the matrix \(\mathbf{A}\) of an undirected graph is symmetric, but the same does not necessarily hold true for a directed graph. Figure 1a depicts a directed graph with oriented arcs.

In many practical applications, it is useful to enrich the graph \(g\) with additional node and edge information belonging to the domains \(\mathcal{X}_g\) and \(\mathcal{A}_g\), respectively. Each node \(u \in |\mathcal{V}_g|\) is associated with a particular feature vector \(x_v \in \mathcal{X}_g\), while each edge holds a particular feature vector \(a_{uv} \in \mathcal{A}_g\). In [41],

5

<!-- page: 6 -->

this is referred to as nodes (respectively edges) being "uniformly labelled". In the general case one can consider \(\mathcal{X}_g \subseteq \mathbb{R}^d\), \(d \in \mathbb{N}\) and \(\mathcal{A}_g \subseteq \mathbb{R}^{d'}\), \(d' \in \mathbb{N}\). Here the terms \(d\) and \(d'\) denote the number of features associated with each node and edge, respectively. Note that, despite having defined node and edge features on the real set for the sake of generality, in many applications these take discrete values. Moreover, from a practical perspective, we can think of a graph with no node (respectively edge) features as an equivalent graph in which all node (edge) features are identical.

As far as undirected graphs are concerned, these are straightforwardly transformed to their directed version. In particular, every edge \(\{u, v\}\) is replaced by two distinct and oppositely oriented arcs \((u, v)\) and \((v, u)\), with identical edge features as shown in Figure 1b.

A path is a sequence of edges that joins a sequence of nodes. Whenever there exists a non-empty path from a node to itself with no other repeated nodes, we say the graph has a cycle; when there are no cycles in the graph, the graph is called acyclic.

A topological ordering of a directed graph \(g\) is a total sorting of its nodes such that for every directed edge \((u, v)\) from node \(u\) to node \(v\), \(u\) comes before \(v\) in the ordering. A topological ordering exists if and only if the directed graph has no cycles, i.e., if it is a directed acyclic graph (DAG).

A graph is ordered if, for each node \(v\), a total order on the edges incident on \(v\) is defined and unordered otherwise. Moreover, a graph is positional if, besides being ordered, a distinctive positive integer is associated with each edge incident on a node \(v\) (allowing some positions to be absent) and non-positional otherwise. To summarize, in the rest of the paper we will assume a general class of directed/undirected, acyclic/cyclic and positional/non-positional graphs.

The neighborhood of a node \(v\) is defined as the set of nodes which are connected to \(v\) with an oriented arc, i.e., \(\mathcal{N}_v = \{u \in \mathcal{V}_g \mid (u, v) \in \mathcal{E}_g\}\). \(\mathcal{N}_v\) is

6

<!-- page: 7 -->

[FIGURE: Figure 2: The bigger picture that all graph learning methods share. A "Deep Graph Network" takes an input graph and produces node representations \(h_v \; \forall v \in \mathcal{V}_g\). Such representations can be aggregated to form a single graph representation \(h_g\).]

Text in figure:
- DGN
- node representations
- graph representation

closed if it always includes \(u\) and open otherwise. If the domain of arc labels \(\mathcal{A}\) is discrete and finite, i.e., \(\mathcal{A} = \{c_1, \ldots, c_m\}\), we define the subset of neighbors of \(v\) with arc label \(c_k\) as \(\mathcal{N}_v^{c_k} = \{u \in \mathcal{N}_v \mid a_{uv} = c_k\}\). Figure 1c provides a graphical depiction of the (open) neighborhood of node \(v_1\).

In supervised learning applications, we may want to predict an output for a single node, an edge, or an entire graph, whose ground truth labels are referred to as \(y_v\), \(y_{uv}\), and \(y_g\) respectively. Finally, when clear from the context, we will omit the subscript \(g\) to avoid verbose notation.

### 2.2. The Bigger Picture

Regardless of the training objective one cares about, almost all deep learning models working on graphs ultimately produce node representations, also called states. The overall mechanism is sketched in Figure 2, where the input graph on the left is mapped by a model into a graph of node states with the same topology. In [41], this process is referred to as performing an isomorphic transduction of the graph. This is extremely useful as it allows tackling nodes, edges, and graph-related tasks. For instance, a graph representation can be easily computed by aggregating together its nodes representations, as shown in the right-hand side of Figure 2.

To be more precise, each node in the graph will be associated with a state vector \(h_v \; \forall v \in \mathcal{V}_g\). The models discussed in this work visit/traverse the input graph to compute node states. Importantly, in our context of general graphs, the result of this traversal does not depend on the visiting order and, in particular, no topological ordering among nodes is assumed. Being independent of a topological ordering has repercussions on how deep learning models for graphs deal with cycles (Section 2.3). Equivalently, we can say that the state vectors

7

<!-- page: 8 -->

can be computed by the model in parallel for each node of the input graph.

The work of researchers and practitioners therefore revolves around the definition of deep learning models that automatically extract the relevant features from a graph. In this tutorial, we refer to such models with the uniforming name of "Deep Graph Networks" (DGNs). On the one hand, this general terminology serves the purpose of disambiguating the terms "Graph Neural Network", which we use to refer to [104], and "Graph Convolutional Network", which refers to, e.g., [72]. These two terms have been often used across the literature to represent the whole class of neural networks operating on graph data, generating ambiguities and confusion among practitioners. On the other hand, we also use it as the base of an illustrative taxonomy (shown in Figure 3), which will serve as a road-map of the discussion in this and the following sections. Note that with the term "DGN" (and its taxonomy) we would like to focus solely on the part of the deep learning model that learns to produce node representations. Therefore, the term does not encompass those parts of the architecture that compute a prediction, e.g., the output layer. In doing so, we keep a modular view on the architecture, and we can combine a deep graph network with any predictor that solves a specific task.

We divide deep graph networks into three broad categories. The first is called Deep Neural Graph Networks (DNGNs), which includes models inspired by neural architectures. The second category is that of Deep Bayesian Graph Networks (DBGNs), whose representatives are probabilistic models of graphs. Lastly, the family of Deep Generative Graph Networks (DGGNs) leverages both neural and probabilistic models to generate graphs. This taxonomy is by no means a strict compartmentalization of methodologies; in fact, all the approaches we will focus on in this tutorial are based on local relations and iterative processing to diffuse information across the graph, regardless of their neural or probabilistic nature.

8

<!-- page: 9 -->

[FIGURE: Figure 3: The road-map of the architectures we will discuss in detail.]

Text in figure:
- DGNs (Deep Graph Networks)
- DNGNs (Deep Neural Graph Networks)
- DBGNs (Deep Bayesian Graph Networks)
- DGGNs (Deep Generative Graph Networks)
- Recurrent
- Feedforward
- Constructive
- Node-level decoder
- Graph-level decoder

### 2.3. Local relations and iterative processing of information

Learning from a population of arbitrary graphs raises two fundamental issues: i) no assumptions about the topology of the graph hold in general, and ii) structures may contain cycles. We now discuss both points, highlighting the most common solutions adopted in the literature.

*Graphs with variable topology.* First of all, we need a way to seamlessly process information of graphs that vary both in size and shape. In the literature, this has been solved by building models that work locally at node level rather than at graph level. In other words, the models process each node using information coming from the neighborhood. This recalls the localized processing of images in convolutional models [75], where the focus is on a single pixel and its set of finite neighbors (however defined). Such stationarity assumption allows reducing significantly the number of parameters needed by the model, as they are re-used across all nodes (similarly to how convolutional filters are shared across pixels). Moreover, it effectively and efficiently combines the "experience" of all nodes and graphs in the dataset to learn a single function. At the same time, the stationarity assumption calls for the introduction of mechanisms that can learn from the global structure of the graph as well, which we discuss in the following section.

Notwithstanding these advantages, local processing alone does not solve the

9

<!-- page: 10 -->

problem of graphs of variable neighborhood shape. This issue arises in the case of non-positional graphs, where there is no consistent way to order the nodes of a neighborhood. In this case, one common solution is to use permutation invariant functions acting on the neighborhood of each node. A permutation invariant function is a function whose output does not change upon reordering of the input elements. Thanks to this property, these functions are well suited to handle an arbitrary number of input elements, which comes in handy when working on unordered and non-positional graphs of variable topology. Common examples of such functions are the sum, mean, and product of the input elements. Under some conditions, it is possible to approximate all permutation invariant continuous functions by means of suitable transformations [140, 124]. More concretely, if the input elements belong to an uncountable space \(X\), e.g., \(\mathbb{R}^d\), and they are in finite and fixed number \(M\), then any permutation invariant continuous function \(\Psi : X^M \to Y\) can be expressed as (Theorem 4.1 of [124])

$$
\Psi(Z) = \phi\left(\sum_{z \in Z} \psi(z)\right), \tag{1}
$$

where \(\phi : M \to Y\) and \(\psi : X \to M\) are continuous functions such as neural networks (for the universal approximation theorem [26]). Throughout the rest of this work, we will use the Greek letter \(\Psi\) to denote permutation invariant functions.

*Graphs contain cycles.* A graph cycle models the presence of mutual dependencies/influences between the nodes. In addition, the local processing of graphs implies that any intermediate node state is a function of the state of its neighbors. Under the local processing assumption, a cyclic structural dependency translates into mutual (causal) dependencies, i.e., a potentially infinite loop, when computing the node states in parallel. The way to solve this is to assume an iterative scheme, i.e., the state \(h_v^{\ell+1}\) of node \(v\) at iteration \(\ell + 1\) is defined using the neighbor states computed at the previous iteration \(\ell\). The iterative scheme can be interpreted as a process that incrementally refines node representation as \(\ell\) increases. While this might seem reasonable, one may question

10

<!-- page: 11 -->

whether such an iterative process can converge, given the mutual dependencies among node states. In practice, some approaches introduce constraints on the nature of the iterative process that force it to be convergent. Instead, others map each step of the iterative process to independent layers of a deep architecture. In other words, in the latter approach, the state \(h_v^{\ell+1}\) is computed by layer \(\ell + 1\) of the model based on the output of the previous layer \(\ell\).

For the above reasons, in the following sections, we will use the symbol \(\ell\) to refer, interchangeably, to an iteration step or layer by which nodes propagate information across the graph. Furthermore, we will denote with \(h_g^\ell\) the representation of the entire graph \(g\) at layer \(\ell\).

### 2.4. Three Mechanisms of Context Diffusion

Another aspect of the process we have just discussed is the spreading of local information across the graph under the form of node states. This is arguably the most important concept of local and iterative graph learning methods. At a particular iteration \(\ell\), we (informally) define the context of a node state \(h_v^\ell\) as the set of node states that directly or indirectly contribute to determining \(h_v^\ell\); a formal characterization of context is given in [88] for the interested reader.

An often employed formalism to explain how information is actually diffused across the graph is message passing [48]. Focusing on a single node, message passing consists of two distinct operations:

- **message dispatching.** A message is computed for each node, using its current state and (possibly) edge information. Then, the message is sent to neighboring nodes according to the graph structure;
- **state update.** The incoming node messages, and possibly its state, are collected and used to update the node state.

To bootstrap the message passing process, node states need to be initialized properly. A common choice is to set the initial states to their respective node feature vectors, although variations are possible. As discussed in Section 2.2, the order in which nodes are visited by the model to compute the states is not

11

<!-- page: 12 -->

[FIGURE: Figure 4: Context spreading in an undirected graph is shown for a network of depth 3, where wavy arrows represent the context flow. Specifically, we focus on the context of node \(u\) at the last layer, by looking at the figure from right to left. It is easy to see that the context of node \(u\) at \(\ell = 2\) depends on the state of its only neighbor \(v\) at \(\ell = 1\), which in turn depends on its neighboring node representations at \(\ell = 0\) (\(u\) included). Therefore, the context of \(u\) is given by almost all the nodes in the graph.]

Text in figure:
- \(\mathcal{N}_v\)
- \(\mathcal{N}_u\)
- \(v\), \(u\)
- \(\ell = 0\), \(\ell = 1\), \(\ell = 2\)

influential. The iterative application of message passing to the nodes allows contextual information to "travel" across the graph in the form of aggregated messages. As a consequence, nodes acquire knowledge about their wider surroundings rather than being restricted to their immediate neighborhood.

Context diffusion can be visually represented in Figure 4, in which we show the "view" that node \(u\) has about the graph at iteration \(\ell = 2\). First of all, we observe that the neighborhood of \(u\) is given by node \(v\), and therefore all the contextual information that \(u\) receives must go through \(v\). If we look at the picture from right to left, \(h_u^2\) is defined in terms of \(h_v^1\), \(v \in \mathcal{N}_u\), which in turn is computed by aggregating three different colored nodes (one of which is \(u\) itself). Hence, by iteratively computing local aggregation of neighbor states, we can indirectly provide \(u\) with information about nodes farther away in the graph. It is trivial to show that \(\ell = 3\) iterations are sufficient to increase the context to include information from all nodes in the graph of Figure 4. Put differently, not only deep learning techniques are useful for automatic feature extraction, but they are also functional to context diffusion.

Under the light of the different information diffusion mechanisms they em-

12

<!-- page: 13 -->

ploy, we can partition most deep graph learning models into recurrent, feedforward and constructive approaches. We now discuss how they work and what their differences are.

*Recurrent Architectures.* This family of models implements the iterative processing of node information as a dynamical system. Two of the most popular representatives of this family are the Graph Neural Network [104] and the Graph Echo State Network [44]. Both approaches rely on imposing contractive dynamics to ensure convergence of the iterative process. While the former enforces such constraints in the (supervised) loss function, the latter inherits convergence from the contractivity of (untrained) reservoir dynamics. The Gated Graph Neural Network [78] is another example of recurrent architecture where, differently from [104], the number of iterations is fixed a priori, regardless of whether convergence is reached or not. An iterative approach based on collective inference, which does not rely on any particular convergence criteria, was introduced in [83].

This family of models handles graph cycles by modeling the mutual dependencies between node states using a single layer of recurrent units. In this case, we can interpret the symbol \(\ell\) of Figure 4 as an "iteration step" of the recurrent state transition function computed for the state of each node. Finally, we mention the recent Fast and Deep Graph Neural Network [45], a multi-layered and efficient version of the Graph Echo State Network.

*Feedforward Architectures.* In contrast to recurrent models, feedforward models do not exploit an iterative diffusion mechanism over the same layer of recurrent units. Instead, they stack multiple layers to compose the local context learned at each step. As a result, the mutual dependencies induced by cycles are managed via differently parameterized layers without the need for constraints to ensure the convergence of the encoding process. To draw a parallel with Figure 4 (here \(\ell\) corresponds to the index of a layer), this compositionality affects the context of each node, which increases as a function of the network depth up to the inclusion of the entire graph [88]. The Neural Network for Graphs [88] was

13

<!-- page: 14 -->

the first proposal of a feedforward architecture for graphs.

Not surprisingly, there is a close similarity between this kind of context diffusion and the local receptive field of convolutional networks, which increases as more layers are added to the architecture. Despite that, the main difference is that graphs have no fixed structure as neighborhoods can vary in size, and a node ordering is rarely given. In particular, the local receptive field of convolutional networks can be seen as the context of a node in graph data, whereas the convolution operator processing corresponds to the visit of the nodes in a graph (even though the parametrization technique is different). These are the reasons why the term graph convolutional layer is often used in literature.

The family of feedforward models is the most popular for its simplicity, efficiency, and performance on many different tasks. However, deep networks for graphs suffer from the same gradient-related problems as other deep neural networks, especially when associated with an "end-to-end" learning process running through the whole architecture [61, 9, 77].

*Constructive Architectures.* The last family we identify can be seen as a special case of feedforward models, in which training is performed layer-wise. The major benefit of constructive architectures is that deep networks do not incur the vanishing/exploding gradient problem by design. Thus, the context can be more effectively propagated across layers and hence across node states. In supervised contexts, the constructive technique allows us to automatically determine the number of layers needed to solve a task [35, 86]. As explained in Figure 4, this characteristic is also related to the context needed by the problem at hand; as such, there is no need to determine it a priori, as shown in [88], where the relationship between the depth of the layers and context shape is formally proved.

Moreover, an essential feature of constructive models is that they solve a problem in a divide-et-impera fashion, incrementally splitting the task into more manageable sub-tasks (thus relaxing the "end-to-end" approach). Each layer contributes to the solution of a sub-problem, and subsequent layers use this

14

<!-- page: 15 -->

result to solve the global task progressively.

Among the constructive approaches, we mention the Neural Network for Graphs [88] (which is also the very first proposed feedforward architecture for graphs) and the Contextual Graph Markov Model [3], a more recent and probabilistic variant.

## 3. Building Blocks

We now turn our attention to the main constituents of local graph learning models. The architectural bias imposed by these building blocks determines the kind of representations that a model can compute. We remark that the aim of this Section is not to give the most comprehensive and general formulation under which all models can be formalized. Rather, it is intended to show the main "ingredients" that are common to many architectures and how these can be combined to compose an effective learning model for graphs.

### 3.1. Neighborhood Aggregation

The way models aggregate neighbors to compute hidden node representations is at the core of local graph processing. We will conform to the common assumption that graphs are non-positional so that we need permutation invariant functions to realize the aggregation. For ease of notation, we will assume that any function operating on node \(v\) has access to its feature vector \(x_v\), as well as the set of incident arc feature vectors, \(\{a_{uv} \mid u \in \mathcal{N}_v\}\).

In its most general form, neighborhood aggregation for node \(v\) at layer/step \(\ell + 1\) can be represented as follows:

$$
h_v^{\ell+1} = \phi^{\ell+1}\left(h_v^\ell, \Psi(\{\psi^{\ell+1}(h_u^\ell) \mid u \in \mathcal{N}_v\})\right) \tag{2}
$$

where \(h_u^\ell\) denotes the state of a node \(u\) at layer/step \(\ell\), \(\phi\) and \(\psi\) implement arbitrary transformations of the input data, e.g., through a Multi Layer Perceptron, \(\Psi\) is a permutation invariant function, and \(\mathcal{N}_v\) can be the open or closed neighborhood of \(v\). In most cases, the base case of \(\ell = 0\) corresponds to a possibly non-linear transformation of node features \(x_v\) which does not depend on

15

<!-- page: 16 -->

structural information.

It is important to realize that the above formulation includes both Neural and Bayesian DGNs. As an example, a popular concrete instance of the neighborhood aggregation scheme presented above is the Graph Convolutional Network [72], a DNGN which performs aggregation as follows:

$$
h_v^{\ell+1} = \sigma\left(\mathbf{W}^{\ell+1} \sum_{u \in \mathcal{N}(v)} \mathbf{L}_{uv} h_u^\ell\right), \tag{3}
$$

where \(\mathbf{L}\) is the normalized graph Laplacian, \(\mathbf{W}\) is a weight matrix and \(\sigma\) is a non-linear activation function such as the sigmoid. We can readily see how Equation 3 is indeed a special case of Equation 2:

$$
m_u^v = \psi^{\ell+1}(h_u^\ell) = \mathbf{L}_{uv} h_u^\ell \tag{4}
$$

$$
M_v = \Psi(\{m_u^v \mid u \in \mathcal{N}_v\}) = \sum_{u \in \mathcal{N}(v)} m_u^v \tag{5}
$$

$$
h_v^{\ell+1} = \phi^{\ell+1}\left(h_v^\ell, M_v\right) = \sigma(\mathbf{W}^{\ell+1} M_v). \tag{6}
$$

In Section 5.2, we will describe how the neighborhood aggregation of the Graph Convolutional Network is obtained via special approximations of spectral graph theory methodologies.

*Handling Graph Edges.* The general neighborhood aggregation scheme presented above entails that arcs are unattributed or contain the same information. This assumption does not hold in general, as arcs in a graph often contain additional information about the nature of the relation. This information can be either discrete (e.g., the type of chemical bonds that connect two atoms in a molecule) or continuous (e.g., node distances between atoms). Thus, we need mechanisms that leverage arc labels to enrich node representations. If \(\mathcal{A}\) is finite and discrete, we can reformulate Eq. 2 to account for different arc labels as follows:

$$
h_v^{\ell+1} = \phi^{\ell+1}\left(h_v^\ell, \sum_{c_k \in \mathcal{A}} \left(\Psi(\{\psi^{\ell+1}(h_u^\ell) \mid u \in \mathcal{N}_v^{c_k}\})\right) * w_{c_k}\right), \tag{7}
$$

16

<!-- page: 17 -->

where \(w_{c_k}\) is a learnable scalar parameter that weighs the contribution of arcs with label \(a_{uv} = c_k\), and \(*\) multiplies every component of its first argument by \(w_{c_k}\). This formulation presents an inner aggregation among neighbors sharing the same arc label, plus an outer weighted sum over each possible arc label. This way, the contribution of each arc label is learned separately. The Neural Network for Graphs [88] and the Relational Graph Convolutional Network [105] implement Eq. 7 explicitly, whereas the Contextual Graph Markov Model [3] uses the switching-parent approximation [103] to achieve the same goal. A more general solution, which works with continuous arc labels, is to reformulate Eq. 2 as

$$
h_v^{\ell+1} = \phi^{\ell+1}\left(h_v^\ell, \Psi(\{e^{\ell+1}(a_{uv})^T \psi^{\ell+1}(h_u^\ell) \mid u \in \mathcal{N}_v\})\right), \tag{8}
$$

where \(e\) can be any function. Note how we explicitly introduce a dependence on the arc \(a_{uv}\) inside the neighborhood aggregation: this has the effect of weighting the contribution of each neighbor based on its (possibly multidimensional) arc label, regardless of whether it is continuous or discrete. For example, in [48] \(e\) is implemented as a neural network that outputs a weight matrix.

*Attention.* Attention mechanisms [119] assign a relevance score to each part of the input of a neural layer, and they have gained popularity in language-related tasks. When the input is graph-structured, we can apply attention to the aggregation function. This results in a weighted average of the neighbors where individual weights are a function of node \(v\) and its neighbor \(u \in \mathcal{N}_v\). More formally, we extend the convolution of Eq. 2 in the following way:

$$
h_v^{\ell+1} = \phi^{\ell+1}\left(h_v^\ell, \Psi(\{\alpha_{uv}^{\ell+1} * \psi^{\ell+1}(h_u^\ell) \mid u \in \mathcal{N}_v\})\right), \tag{9}
$$

where \(\alpha_{uv}^{\ell+1} \in \mathbb{R}\) is the attention score associated with \(u \in \mathcal{N}_v\). In general, this score is unrelated to the edge information, and as such edge processing and attention are two quite distinct techniques. As a matter of fact, the Graph Attention Network [120] applies attention to its neighbors but it does not take into account edge information. To calculate the attention scores, the model

17

<!-- page: 18 -->

computes attention coefficients \(w_{uv}\) as follows:

$$
w_{uv}^\ell = a(\mathbf{W}^\ell h_u^\ell, \mathbf{W}^\ell h_v^\ell), \tag{10}
$$

where \(a\) is a shared attention function and \(\mathbf{W}\) are the layer weights. The attention coefficients measure some form of similarity between the current node \(v\) and each of its neighbors \(u\). Moreover, the attention function \(a\) is implemented as:

$$
a(\mathbf{W}^\ell h_u^\ell, \mathbf{W}^\ell h_v^\ell) = \text{LeakyReLU}((b^\ell)^T[\mathbf{W}^\ell h_u^\ell, \mathbf{W}^\ell h_v^\ell]), \tag{11}
$$

where \(b^\ell\) is a learnable parameter, \([\cdot, \cdot]\) denotes concatenation, and LeakyReLU is the non-linear activation function proposed in [82]. From the attention coefficients, one can obtain attention scores by passing them through a softmax function:

$$
\alpha_{uv}^\ell = \frac{\exp(w_{uv}^\ell)}{\sum_{u' \in \mathcal{N}_v} \exp(w_{u'v}^\ell)}. \tag{12}
$$

The Graph Attention Network also proposes a multi-head attention technique, in which the results of multiple attention mechanisms are either concatenated or averaged together.

*Sampling.* When graphs are large and dense, it can be unfeasible to perform aggregations over all neighbors for each node, as the number of edges becomes quadratic in \(|\mathcal{V}_g|\). Therefore, alternative strategies are needed to reduce the computational burden, and neighborhood sampling is one of them. In this scenario, only a random subset of neighbors is used to compute \(h_v^{\ell+1}\). When the subset size is fixed, we also get an upper bound on the aggregation cost per graph. Figure 5 depicts how a generic sampling strategy acts at node level. Among the models that sample neighbors we mention Fast Graph Convolutional Network (FastGCN) [23] and Graph SAmple and aggreGatE (GraphSAGE) [54]. Specifically, FastGCN samples \(t\) nodes at each layer \(\ell\) via importance sampling so that the variance of the gradient estimator is reduced. Differently from FastGCN, GraphSAGE considers a neighborhood function \(\mathcal{N} : |\mathcal{V}_g| \to 2^{|\mathcal{V}_g|}\) that

18

<!-- page: 19 -->

[FIGURE: Figure 5: The sampling technique affects the neighborhood aggregation procedure by selecting either a subset of the neighbors [23] or a subset of the nodes in the graph [54] to compute \(h_v^{\ell+1}\). Here, nodes in red have been randomly excluded from the neighborhood aggregation of node \(v\), and the context flows only through the wavy arrows.]

associates each node with any (fixed) subset of the nodes in the given graph. In practice, GraphSAGE can sample nodes at multiple distances and treat them as direct neighbors of node \(v\). Therefore, rather than learning locally, this technique exploits a wider and heterogeneous neighborhood, trading a potential improvement in performances for additional (but bounded) computational costs.

### 3.2. Pooling

Similarly to convolutional networks for images, graph pooling operators can be defined to reduce the dimension of the graph after a DGN layer. Graph pooling is mainly used for three purposes, that is to discover important communities in the graph, to imbue this knowledge in the learned representations, and to reduce the computational costs in large scale structures. Figure 6 sketches the general idea associated with this techinque. Pooling mechanisms can be differentiated in two broad classes: adaptive and topological. The former relies on a parametric, and hence trainable, pooling mechanism. A notable example of this approach is Differentiable Pooling [137], which uses a neural layer to learn a clustering of the current nodes based on their embeddings at the previous layer. Such clustering is realized by means of a DNGN layer, followed by a softmax to

19

<!-- page: 20 -->

[FIGURE: Figure 6: We show an example of the pooling technique. Each pooling layer coarsens the graph by identifying and clustering nodes of the same community together, so that each group becomes a node of the coarsened graph.]

Text in figure:
- Pooling layer

obtain a soft-membership matrix \(\mathbf{S}^{\ell+1}\) that associates nodes with clusters:

$$
\mathbf{S}^{\ell+1} = \text{softmax}(GNN(\mathbf{A}^\ell, \mathbf{H}^\ell)), \tag{13}
$$

where \(\mathbf{A}^\ell\) and \(\mathbf{H}^\ell\) are the adjacency and encoding matrices of layer \(\ell\). The \(\mathbf{S}^{\ell+1}\) matrix is then used to recombine the current graph into (ideally) one of reduced size:

$$
\mathbf{H}^{\ell+1} = {\mathbf{S}^{\ell+1}}^T \mathbf{H}^\ell \quad \text{and} \quad \mathbf{A}^{\ell+1} = {\mathbf{S}^{\ell+1}}^T \mathbf{A}^\ell \mathbf{S}^{\ell+1}. \tag{14}
$$

In practice, since the cluster assignment is soft to preserve differentiability, its application produces dense adjacency matrices. Top-k Pooling [46] overcomes this limitation by learning a projection vector \(p^\ell\) that is used to compute projection scores of the node embedding matrix using dot product, i.e.,

$$
s^{\ell+1} = \frac{\mathbf{H}^\ell p^{\ell+1}}{\|p^{\ell+1}\|}. \tag{15}
$$

Such scores are then used to select the indices of the top ranking nodes and to slice the matrix of the original graph to retain only the entries corresponding to top nodes. Node selection is made differentiable by means of a gating mechanism built on the projection scores. Self-attention Graph Pooling [76] extends Top-k Pooling by computing the score vector as an attention score with a Graph Convolutional Network [72]

$$
s^{\ell+1} = \sigma(GCN(\mathbf{A}^\ell, \mathbf{H}^\ell)). \tag{16}
$$

20

<!-- page: 21 -->

Edge Pooling [42] operates from a different perspective, by targeting edges in place of nodes. Edges are ranked based on a parametric scoring function which takes in input the concatenated embeddings of the incident nodes, that is

$$
s^{\ell+1}((v, u) \in \mathcal{E}_g) = \sigma(w^T[h_v^\ell, h_u^\ell] + b). \tag{17}
$$

The highest ranking edge and its incident nodes are then contracted into a single new node with appropriate connectivity, and the process is iterated.

Topological pooling, on the other hand, is non-adaptive and typically leverages the structure of the graph itself as well as its communities. Note that, them being non-adaptive, such mechanisms are not required to be differentiable, and their results are not task-dependent. Hence, these methods are potentially reusable in multi-task scenarios. The graph clustering software (GRACLUS) [30] is a widely used graph partitioning algorithm that leverages an efficient approach to spectral clustering. Interestingly, GRACLUS does not require an eigendecomposition of the adjacency matrix. From a similar perspective, Non-negative Matrix Factorization Pooling [2] provides a soft node clustering using a non-negative factorization of the adjacency matrix.

Pooling methods can also be used to perform graph classification by iteratively shrinking the graph up to the point in which the graph contains a single node. Generally speaking, however, pooling is interleaved with DGNs layers so that context can be diffused before the graph is shrunk.

### 3.3. Node Aggregation for Graph Embedding

If the task to be performed requires it, e.g., graph classification, node representations can be aggregated in order to produce a global graph embedding. Again, since no assumption about the size of a given graph holds in general, the aggregation needs to be permutation-invariant. More formally, a graph embedding at layer \(\ell\) can be computed as follows:

$$
h_g^\ell = \Psi\left(\{f(h_v^\ell) \mid v \in \mathcal{V}_g\}\right), \tag{18}
$$

where a common setup is to take \(f\) as the identity function and choose \(\Psi\) among element-wise mean, sum or max. Another, more sophisticated, aggregation

21

<!-- page: 22 -->

scheme draws from the work of [140], where a family of adaptive permutation-invariant functions if defined. Specifically, it implements \(f\) as a neural network applied to all the node representations in the graph, and \(\Psi\) is an element-wise summation followed by a final non-linear transformation.

There are multiple ways to exploit graph embeddings at different layers for the downstream tasks. A straightforward way is to use the graph embedding of the last layer as a representative for the whole graph. More often, all the intermediate embeddings are concatenated or given as input to permutation-invariant aggregators. The work of [78] proposes a different strategy where all the intermediate representations are viewed as a sequence, and the model learns a final graph embedding as the output of a Long Short-Term Memory [62] network on the sequence. Sort Pooling [142], on the other hand, uses the concatenation of the node embeddings of all layers as the continuous equivalent of node coloring algorithms. Then, such "colors" define a lexicographic ordering of nodes across graphs. The top ordered nodes are then selected and fed (as a sequence) to a one-dimensional convolutional layer that computes the aggregated graph encoding.

To conclude, Table 1 provides a summary of neighborhood aggregation methods for some representative models. Figure 7 visually exemplifies how the different building blocks can be arranged and combined to construct a feedforward or recurrent model that is end-to-end trainable.

## 4. Learning Criteria

After having introduced the main building blocks and most common techniques to produce node and graph representations, we now discuss the different learning criteria that can be used and combined to tackle different tasks. We will focus on unsupervised, supervised, generative, and adversarial learning criteria to give a comprehensive overview of the research in this field.

### 4.1. Unsupervised Learning

Our discussion begins with unsupervised learning criteria, as some of them act as regularizers in more complex objective functions.

22

<!-- page: 23 -->

[FIGURE: Figure 7: Two possible architectures (feedforward and recurrent) for node and graph classification. Inside each layer, one can apply the attention and sampling techniques described in this Section. After pooling is applied, it is not possible to perform node classification anymore, which is why a potential model for node classification can combine graph convolutional layers. A recurrent architecture (bottom) iteratively applies the same neighborhood aggregation, possibly until a convergence criterion is met.]

Text in figure:
- Conv.
- Conv.
- Pooling
- Conv.
- Aggregation
- Classifier
- \(y_v\)
- \(y_g\)
- \(h_v^{\ell+1}\)
- \(\alpha_{uv}^{\ell+1}\)
- \(u\)
- Recurrent

*Link Prediction.* The most common unsupervised criterion used by graph neural networks is the so-called *link prediction* or *reconstruction* loss. This learning objective aims at building node representations that are similar if an arc connects the associated nodes, and it is suitable for link prediction tasks. Formally, the reconstruction loss can be defined [72] as

$$
\mathcal{L}_{rec}(g) = \sum_{(u,v)} \|\mathbf{h}_v - \mathbf{h}_u\|^2. \tag{19}
$$

23

<!-- page: 24 -->

| Model | Neighborhood Aggregation \(\mathbf{h}_v^{\ell+1}\) |
|---|---|
| NN4G [88] | \(\sigma\left(\mathbf{w}^{{\ell+1}^T}\mathbf{x}_v + \sum_{i=0}^{\ell}\sum_{c_k \in \mathcal{C}}\sum_{u \in \mathcal{N}_v^{c_k}} w_{c_k}^i * \mathbf{h}_u^i\right)\) |
| GNN [104] | \(\sum_{u \in \mathcal{N}_v} MLP^{\ell+1}\left(\mathbf{x}_u, \mathbf{x}_v, \mathbf{a}_{uv}, \mathbf{h}_u^\ell\right)\) |
| GraphESN [44] | \(\sigma\left(\mathbf{W}^{\ell+1}\mathbf{x}_u + \hat{\mathbf{W}}^{\ell+1}[\mathbf{h}_{u_1}^\ell, \ldots, \mathbf{h}_{u_{\mathcal{N}_v}}^\ell]\right)\) |
| GCN [72] | \(\sigma\left(\mathbf{W}^{\ell+1}\sum_{u \in \mathcal{N}(v)} \mathbf{L}_{vu}\mathbf{h}_u^\ell\right)\) |
| GAT [120] | \(\sigma\left(\sum_{u \in \mathcal{N}_v} \alpha_{uv}^{\ell+1} * \mathbf{W}^{\ell+1}\mathbf{h}_u\right)\) |
| ECC [111] | \(\sigma\left(\frac{1}{|\mathcal{N}_v|}\sum_{u \in \mathcal{N}_v} MLP^{\ell+1}(\mathbf{a}_{uv})^T \mathbf{h}_u^\ell\right)\) |
| R-GCN [105] | \(\sigma\left(\sum_{c_k \in \mathcal{C}}\sum_{u \in \mathcal{N}_v^{c_k}} \frac{1}{|\mathcal{N}_v^{c_k}|}\mathbf{W}_{c_k}^{\ell+1}\mathbf{h}_u^\ell + \mathbf{W}^{\ell+1}\mathbf{h}_v^\ell\right)\) |
| GraphSAGE [54] | \(\sigma\left(\mathbf{W}^{\ell+1}\left(\frac{1}{|\mathcal{N}_v|}[\mathbf{h}_v^\ell, \sum_{u \in \mathcal{N}_v} \mathbf{h}_u^\ell]\right)\right)\) |
| CGMM [3] | \(\sum_{i=0}^{\ell} w^i * \left(\sum_{c_k \in \mathcal{C}} w_{c_k}^i * \left(\frac{1}{|\mathcal{N}_v^{c_k}|}\sum_{u \in \mathcal{N}_v^{c_k}} \mathbf{h}_u^i\right)\right)\) |
| GIN [131] | \(MLP^{\ell+1}\left((1 + \epsilon^{\ell+1})\mathbf{h}_v^\ell + \sum_{u \in \mathcal{N}_v} \mathbf{h}_u^\ell\right)\) |

Table 1: We report some of the neighborhood aggregations present in the literature, and we provide a table in Appendix A to ease referencing and understanding of acronyms. Here, square brackets denote concatenation, and \(W, w\) and \(\epsilon\) are learnable parameters. Note that GraphESN assumes a maximum size of the neighborhood. The attention mechanism of GAT is implemented by a weight \(\alpha_{uv}\) that depends on the associated nodes. As for GraphSAGE, we describe its "mean" variant, though others have been proposed by the authors. Finally, recall that \(\ell\) represents an *iteration step* in GNN rather than a layer.

There also exists a probabilistic formulation of this loss, which is used in variational auto-encoders for graphs [71] where the decoder only focuses on structural reconstruction:

$$
P((u, v) \in \mathcal{E}_g \mid \mathbf{h}_u, \mathbf{h}_v) = \sigma(\mathbf{h}_u^T \mathbf{h}_v), \tag{20}
$$

where \(\sigma\) is the sigmoid function (with co-domain in \([0, 1]\)).

Importantly, the link prediction loss reflects the assumption that neighboring nodes should be associated to the same class/community, which is also called *homphily* [83]. In this sense, this unsupervised loss can be seen as a regularizer to be combined with other supervised loss functions. In all tasks where the homophily assumption holds, we expect this loss function to be beneficial.

24

<!-- page: 25 -->

*Maximum Likelihood.* When the goal is to build unsupervised representations that reflect the distribution of neighboring states, a different approach is needed. In this scenario, probabilistic models can be of help. Indeed, one can compute the likelihood that node \(u\) has a certain label \(x_u\) conditioned on neighboring information. Known unsupervised probabilistic learning approaches can then maximize this likelihood. An example is the Contextual Graph Markov Model [3], which constructs a deep network as a stack of simple Bayesian networks. Each layer maximizes the following likelihood:

$$
\mathcal{L}(\theta|g) = \prod_{u \in \mathcal{V}_g} \sum_{i=1}^{C} P(y_u|Q_u = i)P(Q_u = i|q_{\mathcal{N}_u}), \tag{21}
$$

where \(Q_u\) is the categorical latent variable with \(C\) states associated to node \(u\), and \(q_{\mathcal{N}_u}\) is the set of neighboring states computed so far. On the other hand, there are hybrid methods that maximize an intractable likelihood with a combination of variational approximations and DNGNs [97, 71].

Maximum likelihood can also be used in the more standard unsupervised task of density estimation. In particular, a combination of a graph encoder with a radial basis function network can be jointly optimized to solve both tasks [118, 16]. Interestingly, the formulation also extends the notion of random graphs [47, 33] to a broader class of graphs to define probability distributions on attributed graphs, and under some mild conditions it even possesses universal approximation capabilities.

*Graph Clustering.* Graph clustering aims at partitioning a set of graphs into different groups that share some form of similarity. Usually, similarity can be achieved by a distance-based criterion working on vectors obtained via graph encoders. A large family of well-known approaches for directed acyclic graphs, most of which are based on Self-Organizing Maps [73], has been reviewed and studied in [52, 58, 57]. These foundational works were later extended to deal with more cyclic graphs [95, 53] Finally, the maximum-likelihood based technique in [16] can be straightforwardly applied to graph clustering.

25

<!-- page: 26 -->

*Mutual Information.* An alternative approach to produce node representations focuses on local mutual information maximization between pairs of graphs. In particular, Deep Graph Infomax [121] uses a corruption function that generates a distorted version of a graph \(g\), called \(\tilde{g}\). Then, a discriminator is trained to distinguish the two graphs, using a bilinear score on node and graph representations. This unsupervised method requires a corruption function to be manually defined each time, e.g., injecting random structural noise in the graph, and as such it imposes a bias on the learning process.

*Entropy regularization for pooling.* When using adaptive pooling methods, it can be useful to encourage the model to assign each node to a single community. Indeed, adaptive pooling can easily scatter the contribution of node \(u\) across multiple communities, and this results in low informative communities. The *entropy* loss was proposed [137] to address this issue. Formally, if we define with \(\mathbf{S} \in \mathbb{R}^{|\mathcal{V}_g| \times C}\) the matrix of soft-cluster assignments (Section 3.2, where \(C\) is the number of clusters of the pooling layer, the entropy loss is computed as follows:

$$
\mathcal{L}_{ent}(g) = \frac{1}{|\mathcal{V}_g|}\sum_{u \in \mathcal{V}_g} H(\mathbf{S}_u) \tag{22}
$$

where \(H\) is the entropy and \(\mathbf{S}_u\) is the row associated with node \(u\) clusters assignment. Notice that, from a practical point of view, it is still challenging to devise a differentiable pooling method that does not generate dense representations. However, encouraging a one-hot community assignment of nodes can enhance visual interpretation of the learned clusters, and it acts as a regularizer that enforces well-separated communities.

### 4.2. Supervised Learning

We logically divide supervised graph learning tasks in node classification, graph classification, and graph regression. Once node or graph representations are learned, the prediction step does not differ from standard vectorial machine learning, and common learning criteria are Cross-Entropy/Negative Log-likelihood for classification and Mean Square Error for regression.

26

<!-- page: 27 -->

*Node Classification.* As the term indicates, the goal of node classification is to assign the correct target label to each node in the graph. There can be two distinct settings: *inductive node classification*, which consists of classifying nodes that belong to unseen graphs, and *transductive node classification*, in which there is only one graph to learn from and only a fraction of the nodes needs to be classified. It is important to remark that benchmark results for node classification have been severely affected by delicate experimental settings; this issue was later addressed [108] by re-evaluating state of the art architectures under a rigorous setting. Assuming a multi-class node classification task with \(C\) classes, the most common learning criterion is the cross-entropy:

$$
\mathcal{L}_{CE}(y, t) = -\log\left(\frac{e^{y_t}}{\sum_{j=1}^{C} e^{y_j}}\right) \tag{23}
$$

where \(y \in R^C\) and \(t \in \{1, \ldots, C\}\) are the output vector and target class, respectively. The loss is then summed or averaged over all nodes in the dataset.

*Graph Classification/Regression.* To solve graph classification and regression tasks, it is first necessary to apply the node aggregation techniques discussed in Section 3.3. After having obtained a single graph representation, it is straightforward to perform classification or regression via standard machine learning techniques. Similarly to node classification, the graph classification field suffers from ambiguous, irreproducible, and flawed experimental procedures that have been causing a great deal of confusion in the research community. Very recently, however, it has been proposed a rigorous re-evaluation of state-of-the-art models across a consistent number of datasets [34] aimed at counteracting this troubling trend. Cross entropy is usually employed for multi-class graph classification, whereas Mean Square Error is a common criterion for graph regression:

$$
\mathcal{L}_{MSE}(y, t) = \frac{1}{|\mathcal{G}|}\|y - t\|_2^2 \tag{24}
$$

where \(\mathcal{G}\) represents the dataset the dataset and \(y, t\) are the output and target vectors, respectively. Again, the loss is summed or averaged over all graphs in the dataset.

27

<!-- page: 28 -->

### 4.3. Generative learning

Learning how to generate a graph from a dataset of available samples is arguably a more complex endeavor than the previous tasks. To sample a graph \(g\), one must have access to the underlying generating distribution \(P(g)\). However, since graph structures are discrete, combinatorial, and of variable-size, gradient-based approaches that learn the marginal probability of data are not trivially applicable. Thus, the generative process is conditioned on a latent representation of a graph/set of nodes, from which the actual structure is decoded. We now present the two most popular approaches by which DGGNs decode graphs latent samples, both of which are depicted in Figure 8. For ease of comprehension, we will focus on the case of graphs with unattributed nodes and edges. Crucially, we assume knowledge of a proper sampling technique; later on, we discuss how these sampling mechanisms can even be learned.

[FIGURE: Figure 8: A simplified schema of graph-level (top row) and node-level (bottom row) generative decoders is shown. Tilde symbols on top of arrows indicate sampling. Dashed arrows indicate that the corresponding sampling procedure is not differentiable in general. Darker shades of blue indicate higher probabilities.]

Text in figure:
- MLP
- \(p(h_g)\)
- \(\tilde{h}_g\)
- \(\tilde{A}\)
- \(p(h_v)\)
- \(\tilde{h}_v\)

*Graph-level decoding.* These approaches sample the graph adjacency matrix in one shot. More in detail, the decoder takes a graph representation as input, and it outputs a dense probabilistic adjacency matrix \(\tilde{A} \in \mathbb{R}^{k \times k}\), where \(k\) is the maximum number of nodes allowed, and each entry \(\tilde{a}_{ij}\) specifies the probability

28

<!-- page: 29 -->

of observing an arc between node \(i\) and \(j\). This corresponds to minimizing the following log-likelihood:

$$
\mathcal{L}_{decoder}(g) = -\log P(\tilde{A} \mid \tilde{h}_g), \tag{25}
$$

where \(\tilde{h}_g\) is a sampled graph representation and \(P(\tilde{A} \mid \tilde{h}_g)\) is implemented as a multi-layer perceptron applied to \(\tilde{h}_g\). To obtain a novel graph, one can either:

1. sample each entry of the probabilistic adjacency matrix, with connection probability \(\tilde{a}_{ij}\);
2. perform an approximate graph matching between the probabilistic and the ground truth matrices, as in [112, 74];
3. make the sampling procedure differentiable using a categorical reparameterization with a Gumbel-Softmax [65], as explored for example in [27].

Notice that the first two alternatives are not differentiable; in those cases, the actual reconstruction loss cannot be back-propagated during training. Thus, the reconstruction loss is computed on the probabilistic matrix instead of the actual matrix [112]. Graph-level decoders are not permutation invariant (unless approximate graph matching is used) because the ordering of the output matrix is assumed fixed.

*Node-level decoding.* Node-level decoders generate a graph starting from a set of \(k\) node representations. These are sampled according to an approximation of their probability distribution. To decode a graph in this setting, one needs to generate the adjacency matrix conditioned on the sampled node set. This is achieved by introducing all possible \(k(k + 1)/2\) unordered node pairs as input to a decoder that optimizes the following log-likelihood:

$$
\mathcal{L}_{decoder}(g) = -\frac{1}{|\mathcal{V}_g|}\sum_{v \in \mathcal{V}_g}\sum_{u \in \mathcal{V}_g} \log P(\tilde{a}_{uv} \mid \tilde{h}_v, \tilde{h}_u), \tag{26}
$$

where \(P(\tilde{a}_{uv} \mid \tilde{h}_v, \tilde{h}_u) = \sigma(\tilde{h}_v^T \tilde{h}_u)\) as in Eq. 20 and similarly to [71, 51], and \(\tilde{h}\) are sampled node representations. As opposed to graph-level decoding, this method is permutation invariant, even though it is generally more expensive to

29

<!-- page: 30 -->

calculate than one-shot adjacency matrix generation.

To complement our discussion, in the following, we summarize those generative models that can optimize the decoding objective while jointly learning how to sample the space of latent representations. We distinguish approaches that explicitly learn their (possibly approximated) probability distribution from those that implicitly learn how to sample from the distribution. The former are based on Generative Auto-Encoders [70, 116], while the latter leverage Generative Adversarial Networks [49].

*Generative Auto-Encoder for graphs.* This method works by learning the probability distribution of node (or graph) representations in latent space. Samples of this distribution are then given to the decoder to generate novel graphs. A general formulation of the loss function for graphs is the following:

$$
\mathcal{L}_{AE}(g) = \mathcal{L}_{decoder}(g) + \mathcal{L}_{encoder}(g), \tag{27}
$$

where \(\mathcal{L}_{decoder}\) is the reconstruction error of the decoder as mentioned above, and \(\mathcal{L}_{encoder}\) is a divergence measure that forces the distribution of points in latent space to resemble a "tractable" prior (usually an isotropic Gaussian \(N(0, I)\)). For example, models based on Variational AEs [70] use the following encoder loss:

$$
\mathcal{L}_{encoder}(g) = -D_{KL}[N(\mu, \sigma^2) \,\|\, N(0, I)], \tag{28}
$$

where \(D_{KL}\) is the Kullback-Leibler divergence, and the two parameters of the encoding distribution are computed as \(\mu = DGN_\mu(A, X)\) and \(\sigma = DGN_\sigma(A, X)\) [112, 80, 101]. More recent approaches such as [18] propose to replace the encoder error term in Equation 27 with a Wasserstein distance term [116].

*Generative Adversarial Networks for graphs.* This technique is particularly convenient. It does not work with \(P(g)\) directly, but it only learns an adaptive mechanism to sample from it. Generally speaking, Generative Adversarial Networks use two different functions: a generator \(G\), which generates novel graphs,

30

<!-- page: 31 -->

and a discriminator \(D\) that is trained to recognize whether its input comes from the generator or from the dataset. When dealing with graph-structured data, both the generator and the discriminator are trained jointly to minimize the following objective:

$$
\mathcal{L}_{GAN}(g) = \min_G \max_D \mathbb{E}_{g \sim P_{data}(g)}[\log D(g)] + \mathbb{E}_{z \sim P(z)}[\log(1 - D(G(z)))], \tag{29}
$$

where \(P_{data}\) is the true unknown probability distribution of the data, and \(P(z)\) is the prior on the latent space (usually isotropic Gaussian or uniform). Note that this procedure provides an implicit way to sample from the probability distribution of interest without manipulating it directly. In the case of graph generation, \(G\) can be a graph or node-level decoder that takes a random point in latent space as input and generates a graph, while \(D\) takes a graph as input and outputs the probability of being a "fake" graph produced by the generator. As an example, [36] implements \(G\) as a graph-level decoder that outputs both a probabilistic adjacency matrix \(\tilde{A}\) and a node label matrix \(\tilde{L}\) as well. The discriminator takes an adjacency matrix \(A\) and a node label matrix \(L\) as input, applies a Jumping Knowledge Network [132] to it, and decides whether the graph is sampled from the generator or the dataset with a multi-layer perceptron. In contrast, [126] works at the node level. Specifically, \(G\) generates structure-aware node representations (based on the connectivity of a breadth-first search tree of a random graph sampled from the training set), while the discriminator takes as input two node representations and decides whether they come from the training set or the generator, optimizing an objective function similar to Eq. 26.

### 4.4. Summary

We conclude this Section by providing a characterization of some of the local iterative models in accord with the building blocks and learning criteria discussed so far. Precisely, Table 2 differentiates models with respect to four key properties, namely the context diffusion method, how an embedding is computed, how layers are constructed, and the nature of the approach. Then, we added other properties that a model may possess or not, such as the ability

31

<!-- page: 32 -->

| Model | Context | Embedding | Layers | Nature |
|---|---|---|---|---|
| GNN [104] | Recurrent | Supervised | Single | Neural |
| NN4G [88] | Constructive | Supervised | Adaptive | Neural |
| GraphESN [44] | Recurrent | Untrained | Single | Neural |
| GCN [72] | Feedforward | Supervised | Fixed | Neural |
| GG-NN [78] | Recurrent | Supervised | Fixed | Neural |
| ECC [111] | Feedforward | Supervised | Fixed | Neural |
| GraphSAGE [54] | Feedforward | Both | Fixed | Neural |
| CGMM [3] | Constructive | Unsupervised | Fixed | Probabilistic |
| DGCNN [142] | Feedforward | Supervised | Fixed | Neural |
| DiffPool [137] | Feedforward | Supervised | Fixed | Neural |
| GAT [120] | Feedforward | Supervised | Fixed | Neural |
| R-GCN [105] | Feedforward | Supervised | Fixed | Neural |
| DGI [121] | Feedforward | Unsupervised | Fixed | Neural |
| GMNN [97] | Feedforward | Both | Fixed | Hybrid |
| GIN [131] | Feedforward | Supervised | Fixed | Neural |
| NMFPool [2] | Feedforward | Supervised | Fixed | Neural |
| SAGPool [76] | Feedforward | Supervised | Fixed | Neural |
| Top-k Pool [46] | Feedforward | Supervised | Fixed | Neural |
| FDGNN [45] | Recurrent | Untrained | Fixed | Neural |

| Model | Edges | Pooling | Attention | Sampling |
|---|---|---|---|---|
| GNN [104] | Continuous | ✗ | ✗ | ✗ |
| NN4G [88] | Discrete | ✗ | ✗ | ✗ |
| GraphESN [44] | ✗ | ✗ | ✗ | ✗ |
| GCN [72] | ✗ | ✗ | ✗ | ✗ |
| GG-NN [78] | ✗ | ✗ | ✗ | ✗ |
| ECC [111] | Continuous | Topological | ✗ | ✗ |
| GraphSAGE [54] | ✗ | ✗ | ✗ | ✓ |
| CGMM [3] | Discrete | ✗ | ✗ | ✗ |
| DiffPool [137] | - | Adaptive | - | - |
| DGCNN [142] | ✗ | Topological | ✗ | ✗ |
| GAT [120] | ✗ | ✗ | ✓ | ✗ |
| R-GCN [105] | Discrete | ✗ | ✗ | ✗ |
| GMNN [97] | - | - | - | - |
| DGI [121] | ✗ | ✗ | ✗ | ✓ |
| GIN [131] | ✗ | ✗ | ✗ | ✗ |
| NMFPool [2] | - | Topological | - | - |
| SAGPool [76] | - | Adaptive | - | - |
| Top-k Pool [46] | - | Adaptive | - | - |
| FDGNN [45] | ✗ | ✗ | ✗ | ✓ |

Table 2: Here we recap the main properties of DGNs, according to what we have discussed so far. Please refer to Appendix A for a description of all acronyms. For clarity, "-" means not applicable, as the model is a framework that relies on any generic learning methodology. The "Layers" column describes how many layers are used by an architecture, which can be just one, a fixed number or adaptively determined by the learning process. On the other hand, "Context" refers to the context diffusion method of a specific layer, which was discussed in Section 2.4.

to handle edges, to perform pooling, to attend over neighbors, and to sample neighbors.

32

<!-- page: 33 -->

## 5. Summary of Other Approaches and Tasks

There are several approaches and topics that are not covered by the taxonomy discussed in earlier sections. In particular, we focused our attention on deep learning methods for graphs, which are mostly based on local and iterative processing. For completeness of exposition, we now briefly review some of the topics that were kept out.

### 5.1. Kernels

There is a long-standing and consolidated line of research related to kernel methods applied to graphs [98, 122, 109, 40, 133]. A kernel is informally defined as a generalized form of positive-definite function that computes similarity scores between pairs of inputs. A crucial aspect of kernel methods, which impacts their application to graphs, is that they are usually non-local and non-adaptive, i.e., they require humans to design the kernel function. When applied to graphs, kernel methods work particularly well when the properties of interest are known, and it is still difficult to perform better with adaptive approaches. However, as mentioned above, non-adaptivity constitutes the main drawback of kernels, as it is not always clear which features we want to extract from the graph. Moreover, kernels suffer from scalability issues when the number of inputs in the dataset is too large (albeit with some exceptions, see [109]). Importantly, kernel similarity matrices can be combined with Support Vector Machines [25] to perform graph classification. Finally, we mention the Nonparametric Small Random Networks algorithm [117], a recent technique for efficient graph classification. Despite being related to the 2-graphlet graph kernel [110], its formulation is probabilistic, and it outperforms many DGNs and graph kernels on a number of tasks.

### 5.2. Spectral methods

Spectral graph theory studies the properties of a graph by means of the associated adjacency and Laplacian matrices. Many machine learning problems can be tackled with these techniques, for example Laplacian smoothing [100], graph semi-supervised learning [22, 21] and spectral clustering [123]. A graph

33

<!-- page: 34 -->

can also be analyzed with signal processing tools, such as the Graph Fourier Transform [59] and related adaptive techniques [20]. Generally speaking, spectral techniques are meant to work on graphs with the same shape and different node labels, as they are based on the eigen-decomposition of adjacency and Laplacian matrices. More in detail, the eigenvector matrix \(Q\) of the Laplacian constitutes an orthonormal basis used to compute the Graph Fourier Transform on the nodes signal \(\mathbf{f} \in \mathbb{R}^{\mathcal{V}_g}\). The transform is defined as \(\mathcal{F}(\mathbf{f}) = Q^T\mathbf{f}\), and its inverse is simply \(\mathcal{F}^{-1}(Q^T\mathbf{f}) = QQ^T\mathbf{f}\) thanks to orthogonality of \(Q\). Then, the graph convolution between a filter \(\boldsymbol{\theta}\) and the graph signal \(\mathbf{f}\) resembles the convolution of the standard Fourier analysis [12]:

$$
\mathcal{F}(\mathbf{f} \otimes \boldsymbol{\theta}) = QWQ^T\mathbf{f} \tag{30}
$$

where \(\otimes\) is the convolution operator and \(W = Q^T\boldsymbol{\theta}\) is a vector of learnable parameters. Repeated application of this convolution interleaved with nonlinearities led to the Spectral Convolutional Neural Network [20].

This approach has some drawbacks. For instance, the parameters cannot be used for graphs with a different Laplacian, and their size grows linearly with the number of nodes in the graph. This, along with the need for an eigendecomposition, makes it difficult to deal with large graphs. Finally, the resulting filter may not be localized in space, i.e., the filter does not modify the signal according to the neighborhood of each node only. This issues were later overcome [29] by using the truncated Chebyshev expansion [59]. Interestingly, the Graph Convolutional Network [72] layer truncates such expansion to the very first term, i.e., the Laplacian of the graph, such that the node states at layer \(\ell + 1\) are computed (in matrix notation) as \(H^{\ell+1} = \sigma(LH^\ell W)\), where \(W\) is the matrix of learnable parameters. Therefore, this model represents an interesting connection between the local and iterative scheme of DGNs and spectral theory.

### 5.3. Random-walks

In an attempt to capture local and global properties of the graph, random walks are often used to create node embeddings, and they have have been studied

34

<!-- page: 35 -->

for a long time [81, 122, 99, 64]. A random walk is defined as a random path that connects two nodes in the graphs. Depending on the reachable nodes, we can devise different frameworks to learn a node representation: for example, Node2Vec [50] maximizes the likelihood of a node given its surroundings by exploring the graph using a random walk. Moreover, learnable parameters guide the bias of the walk in the sense that a depth-first search can be preferred to a breadth-first search and vice-versa. Similarly, DeepWalk [96] learns continuous node representations by modeling random walks as sentences and maximizing a likelihood objective. More recently, random walks have been used to generate graphs as well [14], and a formal connection between the contextual information diffusion of GCN and random walks has been explored [132].

### 5.4. Adversarial training and attacks on graphs

Given the importance of real-world applications that use graph data structures, there has recently been an increasing interest in studying the robustness of DGNs to malicious attacks. The term adversarial training is used in the context of deep neural networks to identify a regularization strategy based on feeding the model with perturbed input. The catch is to make the network resilient to adversarial attacks [11]. Recently, neural DGNs have been shown to be prone to adversarial attacks as well [148], while the use of adversarial training for regularization is relatively new [37]. The adversarial training objective function is formulated as a min-max game where one tries to minimize the harmful effect of an adversarial example. Briefly, the model is trained with original graphs from the training set, as well as with adversarial graphs. Examples of perturbations to make a graph adversarial include arc insertion and deletions [134] or the addition of adversarial noise to the node representations [68]. The adversarial graphs are labeled according to their closest match in the dataset. This way, the space of the loss function is smooth, and it preserves the predictive power of the model even in the presence of perturbed graphs.

35

<!-- page: 36 -->

### 5.5. Sequential generative models of graphs

Another viable option to generate graphs is to model the generative process as a sequence of actions. This approach has been shown to be able to generalize to graphs coming from very different training distributions; however, it relies on a fixed ordering of graph nodes. A seminal approach is the one in [79], where the generation of a graph is modeled as a decision process. Specifically, a stack of neural networks is trained jointly to learn whether to add new nodes, whether to add new edges and which node to focus on the next iteration. Another work of interest is [138], where the generation is formulated as an auto-regressive process where nodes are added sequentially to the existing graph. Each time a new node is added, its adjacency vector with respect to the existing nodes is predicted by a "node-level" Gated Recurrent Unit network [24]. At the same time, another "graph-level" network keeps track of the state of the whole graph to condition the generation of the adjacency vector. Finally, [5, 4] models the generative tasks by learning to predict the ordered edge set of a graph using two Gated Recurrent Unit networks; the first one generates the first endpoints of the edges, while the second predicts the missing endpoints conditioned on such information.

## 6. Open Challenges and Research Avenues

Despite the steady increase in the number of works on graph learning methodologies, there are some lines of research that have not been widely investigated yet. Below, we mention some of them to give practitioners insights about potential research avenues.

### 6.1. Time-evolving graphs

Current research has been mostly focusing on methods that automatically extract features from static graphs. However, being able to model dynamically changing graphs constitutes a further generalization of the techniques discussed in this survey. There already are some supervised [78, 129] and unsupervised

36

<!-- page: 37 -->

[141] proposals in the literature. However, the limiting factor for the development of this research line seems, currently, the lack of large datasets, especially of non-synthetic nature.

### 6.2. Bias-variance trade-offs

The different node aggregation mechanisms described in Section 3.1 play a crucial role in determining the kind of structures that a model can discriminate. For instance, it has been proven that Graph Isomorphism Network is theoretically as powerful as the 1-dim Weisfeiler Lehman test of graph isomorphism [131]. As a result, this model is able to overfit most of the datasets it is applied to. Despite this flexibility, it may be difficult to learn a function that generalizes well: this is a consequence of the usual bias-variance trade-off [43]. Therefore, there is a need to characterize all node aggregation techniques in terms of structural discrimination power. A more principled definition of DGNs is essential to be able to choose the right model for a specific application.

### 6.3. A sensible use of edge information

Edges are usually treated as second-class citizens when it comes to information sources; indeed, most of the models which deal with additional edge features [88, 111, 3, 105] compute a weighted aggregation where the weight is given by a suitable transformation of edge information. However, there are interesting questions that have not been answered yet. For example, is it reasonable to apply context spreading techniques to edges as well? The advantages of such an approach are still not clear. Furthermore, it would be interesting to characterize the discriminative power of methods that exploit edge information.

### 6.4. Hypergraph learning

Hypergraphs are a generalization of graphs in which an edge is connected to a subset of nodes rather than just two of them. Some works on learning from hypergraph have recently been published [146, 145, 38, 67], and the most recent ones take inspiration from local and iterative processing of graphs. Like time-evolving graphs, the scarce availability of benchmarking datasets makes it difficult to evaluate these methods empirically.

37

<!-- page: 38 -->

## 7. Applications

Here, we give some examples of domains in which graph learning can be applied. We want to stress that the application of more general methodologies to problems that have been usually tackled by using flat or sequential representations may bring performance benefits. As graphs are ubiquitous in nature, the following list is far from being exhaustive. Nonetheless, we summarize some of the most common applications to give the reader an introductory overview. As part of our contribution, we release a software library that can be used to easily perform rigorous experiments with DGNs[^1].

### 7.1. Chemistry and Drug Design

Cheminformatics is perhaps the prominent domain where DGNs have been applied with success, and chemical compound datasets are often used to benchmark new models. At a high level, predictive tasks in this field concern learning a direct mapping between molecular structures and outcomes of interest. For example, the Quantitative Structure-Activity Relationship (QSAR) analysis deals with the prediction of the biological activity of chemical compounds. Similarly, the Quantitative Structure-Property Relationship (QSPR) analysis focuses on the prediction of chemical properties such as toxicity and solubility. Instances of pioneering applications of models for structured data to QSAR/QSPR analysis are in [10], and see [90] for a survey. DNGNs have also been applied to the task of finding structural similarities among compounds [32, 66]. Another interesting line of research is computational drug design, e.g., drug side-effect identification [147] and drug discovery. As regards the latter task, several approaches use deep generative models to discover novel compounds. These models also provide mechanisms to search for molecules with a desired set of chemical properties [69, 101, 80]. In terms of benchmarks for graph classification, there is a consistent number of chemical datasets used to evaluate performances of DGNs.

[^1]: The code is available at https://github.com/diningphil/PyDGN

38

<!-- page: 39 -->

Among them, we mention NCI1 [125], PROTEINS, [17] D&D [31], MUTAG [28], PTC [60] and ENZYMES [106].

### 7.2. Social networks

Social graphs represents users as nodes and relations such as friendship or co-authorship as arcs. User representations are of great interest in a variety of tasks, for example to detect whether an actor in the graph is the potential source of misinformation or unhealthy behavior [91, 94]. For these reasons, social networks are arguably the richest source of information for graph learning methods, in that a vast amount of features are available for each user. At the same time, the exploitation of this kind of information raises privacy and ethical concerns, this being the reason why datasets are not publicly available. The vast majority of supervised tasks on social graphs regards node and graph classification. In node classification, three major datasets in literature are usually employed to assess the performances of DGNs, namely Cora, Citeseer [107] and PubMed [93], for which a rigorous evaluation is presented in [108]. Instead, the most popular social benchmarks for (binary and multiclass) graph classification are IMDB-BINARY, IMDB-MULTI, REDDIT-BINARY, REDDIT-MULTI and COLLAB [133]. The results of a rigorous evaluation of several DGNs on these datasets, where graphs use uninformative node features, can be found in [34].

### 7.3. Natural Language Processing

Another interesting application field leverages graph learning methods for Natural Language Processing tasks, where the input is usually represented as a sequence of tokens. By means of dependency parsers, we can augment the input as a tree [1] or as a graph and learn a model that takes into account the syntactic [85] and semantic [84] relations between tokens in the text. An example is neural machine translation, which can be formulated as a graph-to-sequence problem [8] to consider syntactic dependencies in the source and target sentence.

### 7.4. Security

The field of static code analysis is a promising new application avenue for graph learning methods. Practical applications include: i) determining if two

39

<!-- page: 40 -->

assembly programs, which stem from the same source code, have been compiled by means of different optimization techniques; ii) prediction of specific types of bugs by means of augmented Abstract Syntax Trees [63]; iii) predicting whether a program is likely to be the obfuscated version of another one; iv) automatically extracting features from Control Flow Graphs [87].

### 7.5. Spatio-temporal forecasting

DGNs are also interesting to solve tasks where the structure of a graph changes over time. In this context, one is interested not only in capturing the structural dependencies between nodes but also in the evolution of these dependencies on the temporal domain. Approaches to this problem usually combine a DGN (to extract structural properties of the graph) and a Recurrent Neural Network (to model the temporal dependencies). Example of applications include the prediction of traffic in road networks [139], action recognition [128] and supply chain [102] tasks.

### 7.6. Recommender Systems

In the Recommender Systems domain [13], graphs are a natural candidate to encode the relations between users and items to recommend. For example, the typical user-item matrix can be thought of as a bipartite graph, while user-user and item-item matrices can be represented as standard undirected graphs. Recommending an item to a user is a "matrix completion" task, i.e., learning to fill the unknown entries of the user-item matrix, which can be equivalently formulated as a link prediction task. Based on these analogies, several DGN models have been recently developed to learn Recommender Systems from graph data [92, 135]. Currently, the main issues pertain scalability of computation to large graphs. As a result, techniques like neighborhood sampling have been proposed in order to reduce the computational overhead [136].

## 8. Conclusions

After a pioneering phase in the early years of the millennia, the topic of neural networks for graph processing is now a consolidated and vibrant research

40

<!-- page: 41 -->

area. In this expansive phase, research works at a fast pace producing a plethora of models and variants thereof, with less focus on systematization and tracking of early and recent literature. For the field to move further to a maturity phase, we believe that certain aspects should be deepened and pursued with higher priority. A first challenge, in this sense, pertains to a formalization of the different adaptive graph processing models under a unified framework that highlights their similarities, differences, and novelties. Such a framework should also allow reasoning on theoretical and expressiveness properties [131] of the models at a higher level. A notable attempt in this sense has been made by [48], but it does not account for the most recent developments and the variety of mechanisms being published (e.g., pooling operators and graph generation, to name a few). An excellent reference, with respect to this goal, is the seminal work of [41], which provided a general framework for tree-structured data processing. This framework is expressive enough to generalize supervised learning to tree-to-tree non-isomorph transductions, and it generated a followup of theoretical research [58, 56] which consolidated the field of recursive neural networks. The second challenge relates to the definition of a set of rich and robust benchmarks to test and assess models in fair, consistent, and reproducible conditions. Some works [34, 108] are already bringing to the attention of the community some troubling trends and pitfalls as concerns datasets and methodologies used to assess DGNs in the literature. We believe such criticisms should be positively embraced by the community to pursue the growth of the field. Some attempts to provide a set of standardized data and methods appear now under development[^2]. Also, recent progress has been facilitated by the growth and wide adoption by the community of new software packages for the adaptive processing of graphs. In particular, the PyTorch Geometrics [39] and Deep Graph Library [127] packages provide standardized interfaces to operate on graphs for ease of development. Moreover, they allow training models using all the Deep Learning tricks of the trade, such as GPU compatibility and graph mini-batching. The last challenge

[^2]: Open Graph Benchmark: http://ogb.stanford.edu/

41

<!-- page: 42 -->

relates to applications. We believe a methodology reaches its maturity when it will show the transfer of research knowledge to an impactful innovation for the society. Again, attempts in this sense are already underway, with good candidates being in the fields of chemistry [18] and life-sciences [147].

## Acknowledgements

This work has been partially supported by the Italian Ministry of Education, University, and Research (MIUR) under project SIR 2014 LIST-IT (grant n. RBSI14STDE).

42

<!-- page: 43 -->

## Appendix A. Acronyms Table

| Acronym | Model Name | Reference |
|---|---|---|
| GNN | Graph Neural Network | [104] |
| NN4G | Neural Network for Graphs | [88] |
| GraphESN | Graph Echo State Network | [44] |
| GCN | Graph Convolutional Network | [72] |
| GG-NN | Gated Graph Neural Network | [78] |
| ECC | Edge-Conditioned Convolution | [111] |
| GraphSAGE | Graph SAmple and aggreGatE | [54] |
| CGMM | Contextual Graph Markov Model | [3] |
| DGCNN | Deep Graph Convolutional Neural Network | [142] |
| DiffPool | Differentiable Pooling | [137] |
| GAT | Graph Attention Network | [120] |
| R-GCN | Relational Graph Convolutional Network | [105] |
| DGI | Deep Graph Infomax | [121] |
| GMNN | Graph Markov Neural Network | [97] |
| GIN | Graph Isomorphism Network | [131] |
| NMFPool | Non-Negative Matrix Factorization Pooling | [2] |
| SAGPool | Self-attention Graph Pooling | [76] |
| Top-k Pool | Graph U-net | [46] |
| FDGNN | Fast and Deep Graph Neural Network | [45] |

Table A.3: Reference table with acronyms, their extended names, and associated references.

43

<!-- page: 44 -->

## References

[1] Davide Bacciu and Antonio Bruno. Deep tree transductions - a short survey. In *Recent Advances in Big Data and Deep Learning*, pages 236–245. Springer, 2020.

[2] Davide Bacciu and Luigi Di Sotto. A non-negative factorization approach to node pooling in graph convolutional neural networks. In *AI\*IA 2019 – Advances in Artificial Intelligence*, pages 294–306. Springer, 2019.

[3] Davide Bacciu, Federico Errica, and Alessio Micheli. Contextual Graph Markov Model: A deep and generative approach to graph processing. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, volume 80, pages 294–303. PMLR, 2018.

[4] Davide Bacciu, Alessio Micheli, and Marco Podda. Edge-based sequential graph generation with recurrent neural networks. *Neurocomputing*. Accepted, 2019.

[5] Davide Bacciu, Alessio Micheli, and Marco Podda. Graph generation by sequential edge prediction. In *Proceedings of the European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning (ESANN)*, 2019.

[6] Davide Bacciu, Alessio Micheli, and Alessandro Sperduti. Compositional generative mapping for tree-structured data - part I: Bottom-up probabilistic modeling of trees. *IEEE Transactions on Neural Networks and Learning Systems*, 23(12):1987–2002, 2012. Publisher: IEEE.

[7] Peter W Battaglia, Jessica B Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinicius Zambaldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner, and others. Relational inductive biases, deep learning, and graph networks. *arXiv preprint arXiv:1806.01261*, 2018.

44

<!-- page: 45 -->

[8] Daniel Beck, Gholamreza Haffari, and Trevor Cohn. Graph-to-sequence Learning using Gated Graph Neural Networks. In *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL), Volume 1 (Long Papers)*, pages 273–283, 2018.

[9] Yoshua Bengio, Patrice Simard, and Paolo Frasconi. Learning long-term dependencies with gradient descent is difficult. *IEEE Transactions on Neural Networks*, 5(2):157–166, 1994.

[10] Anna Maria Bianucci, Alessio Micheli, Alessandro Sperduti, and Antonina Starita. Application of cascade correlation networks for structures to chemistry. *Applied Intelligence*, 12(1-2):117–147, 2000. Publisher: Springer.

[11] Battista Biggio and Fabio Roli. Wild patterns: Ten years after the rise of adversarial machine learning. *Pattern Recognition*, 84:317–331, 2018. Publisher: Elsevier.

[12] Jonathan M. Blackledge. Chapter 2 - 2d fourier theory. In *Digital Image Processing*, pages 30–49. Woodhead Publishing, 2005.

[13] Jesús Bobadilla, Fernando Ortega, Antonio Hernando, and Abraham Gutiérrez. Recommender systems survey. *Knowledge-Based systems*, 46:109–132, 2013. Publisher: Elsevier.

[14] Aleksandar Bojchevski, Oleksandr Shchur, Daniel Zügner, and Stephan Günnemann. NetGAN: Generating graphs via random walks. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pages 609–618, 2018.

[15] John Adrian Bondy, Uppaluri Siva Ramachandra Murty, et al. *Graph theory with applications*, volume 290. Macmillan London, 1976.

[16] Marco Bongini, Leonardo Rigutini, and Edmondo Trentin. Recursive neural networks for density estimation over generalized random graphs. *IEEE*

45

<!-- page: 46 -->

*Transactions on Neural Networks and Learning Systems*, 29(11):5441–5458, 2018. Publisher: IEEE.

[17] Karsten M Borgwardt, Cheng Soon Ong, Stefan Schönauer, SVN Vishwanathan, Alex J Smola, and Hans-Peter Kriegel. Protein function prediction via graph kernels. *Bioinformatics*, 21(suppl 1):i47–i56, 2005. Publisher: Oxford University Press.

[18] John Bradshaw, Brooks Paige, Matt J Kusner, Marwin Segler, and José Miguel Hernández-Lobato. A model to search for synthesizable molecules. In *Proceedings of the 33rd Conference on Neural Information Processing Systems (NeurIPS)*, pages 7935–7947, 2019.

[19] Michael M. Bronstein, Joan Bruna, Yann LeCun, Arthur Szlam, and Pierre Vandergheynst. Geometric deep learning: going beyond Euclidean data. *IEEE Signal Processing Magazine*, 34(4):25. 18–42, 2017.

[20] Joan Bruna, Wojciech Zaremba, Arthur Szlam, and Yann LeCun. Spectral networks and locally connected networks on graphs. *Proceedings of the 2nd International Conference on Learning Representations (ICLR)*, 2014.

[21] Daniele Calandriello, Ioannis Koutis, Alessandro Lazaric, and Michal Valko. Improved large-scale graph learning through ridge spectral sparsification. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pages 687–696, 2018.

[22] Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien. Semi-supervised learning. *IEEE Transactions on Neural Networks*, 20(3):542–542, 2006.

[23] Jie Chen, Tengfei Ma, and Cao Xiao. FastGCN: Fast learning with graph convolutional networks via importance sampling. In *Proceedings of the 6th International Conference on Learning Representations (ICLR)*, 2018.

[24] Kyunghyun Cho, Bart van Merrienboer, Çaglar Gülçehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. Learning

46

<!-- page: 47 -->

phrase representations using rnn encoder-decoder for statistical machine translation. In *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing, (EMNLP)*, pages 1724–1734, 2014.

[25] Corinna Cortes and Vladimir Vapnik. Support-vector networks. *Machine Learning*, 20(3):273–297, 1995. Publisher: Springer.

[26] George Cybenko. Approximation by superpositions of a sigmoidal function. *Mathematics of control, signals and systems*, 2(4):303–314, 1989.

[27] Nicola De Cao and Thomas Kipf. MolGAN: An implicit generative model for small molecular graphs. *Workshop on Theoretical Foundations and Applications of Deep Generative Models, International Conference on Machine Learning (ICML)*, 2018.

[28] Asim Kumar Debnath, Rosa L Lopez de Compadre, Gargi Debnath, Alan J Shusterman, and Corwin Hansch. Structure-activity relationship of mutagenic aromatic and heteroaromatic nitro compounds correlation with molecular orbital energies and hydrophobicity. *Journal of Medicinal Chemistry*, 34(2):786–797, 1991. Publisher: ACS Publications.

[29] Michaël Defferrard, Xavier Bresson, and Pierre Vandergheynst. Convolutional neural networks on graphs with fast localized spectral filtering. In *Proceedings of the 30th Conference on Neural Information Processing Systems (NIPS)*, pages 3844–3852, 2016.

[30] Inderjit S Dhillon, Yuqiang Guan, and Brian Kulis. Weighted graph cuts without eigenvectors a multilevel approach. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 29(11):1944–1957, 2007. Publisher: IEEE.

[31] Paul D Dobson and Andrew J Doig. Distinguishing enzyme structures from non-enzymes without alignments. *Journal of Molecular Biology*, 330(4):771–783, 2003. Publisher: Elsevier.

47

<!-- page: 48 -->

[32] David K. Duvenaud, Dougal Maclaurin, Jorge Iparraguirre, Rafael Bombarelli, Timothy Hirzel, Alan Aspuru-Guzik, and Ryan P. Adams. Convolutional networks on graphs for learning molecular fingerprints. In *Proceedings of the 29th Conference on Neural Information Processing Systems (NIPS)*, pages 2224–2232, 2015.

[33] Paul Erdős and Alfréd Rényi. On the evolution of random graphs. *Publications of the Mathematical Institute of the Hungarian Academy of Science*, 5(1):17–60, 1960.

[34] Federico Errica, Marco Podda, Davide Bacciu, and Alessio Micheli. A fair comparison of graph neural networks for graph classification. In *Proceedings of the 8th International Conference on Learning Representations (ICLR)*, 2020.

[35] Scott E. Fahlman and Christian Lebiere. The Cascade-Correlation learning architecture. In *Proceedings of the 3rd Conference on Neural Information Processing Systems (NIPS)*, pages 524–532, 1990.

[36] S. Fan and B. Huang. Conditional labeled graph generation with GANs. In *Workshop on Representation Learning on Graphs and Manifolds, International Conference on Learning Representations (ICLR)*, 2019.

[37] Fuli Feng, Xiangnan He, Jie Tang, and Tat-Seng Chua. Graph adversarial training: Dynamically regularizing based on graph structure. *IEEE Transactions on Knowledge and Data Engineering*, 2019. Publisher: IEEE.

[38] Yifan Feng, Haoxuan You, Zizhao Zhang, Rongrong Ji, and Yue Gao. Hypergraph neural networks. In *Proceedings of the 33rd AAAI Conference on Artificial Intelligence (AAAI)*, volume 33, pages 3558–3565, 2019.

[39] Matthias Fey and Jan Eric Lenssen. Fast graph representation learning with PyTorch Geometric. *Workshop on Representation Learning on Graphs and Manifolds, International Conference on Learning Representations (ICLR)*, 2019.

48

<!-- page: 49 -->

[40] Paolo Frasconi, Fabrizio Costa, Luc De Raedt, and Kurt De Grave. klog: A language for logical and relational learning with kernels. *Artificial Intelligence*, 217:117–143, 2014. Publisher: Elsevier.

[41] Paolo Frasconi, Marco Gori, and Alessandro Sperduti. A general framework for adaptive processing of data structures. *IEEE Transactions on Neural Networks*, 9(5):768–786, 1998. Publisher: IEEE.

[42] Michael Truong Le Frederik Diehl, Thomas Brunner and Alois Knoll. Towards graph pooling by edge contraction. In *Workshop on learning and reasoning with graph-structured data, International Conference on Machine Learning (ICML)*, 2019.

[43] Jerome Friedman, Trevor Hastie, and Robert Tibshirani. *The elements of statistical learning*, volume 1. Springer series in statistics New York, 2001.

[44] Claudio Gallicchio and Alessio Micheli. Graph echo state networks. In *Proceedings of the International Joint Conference on Neural Networks (IJCNN)*, pages 1–8. IEEE, 2010.

[45] Claudio Gallicchio and Alessio Micheli. Fast and deep graph neural networks. In *Proceedings of the 34th AAAI Conference on Artificial Intelligence (AAAI)*, 2020.

[46] Hongyang Gao and Shuiwang Ji. Graph U-nets. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, pages 2083–2092, 2019.

[47] Edgar N Gilbert. Random graphs. *The Annals of Mathematical Statistics*, 30(4):1141–1144, 1959.

[48] Justin Gilmer, Samuel S Schoenholz, Patrick F Riley, Oriol Vinyals, and George E Dahl. Neural message passing for quantum chemistry. In *Proceedings of the 34th International Conference on Machine Learning (ICML)*, pages 1263–1272, 2017.

49

<!-- page: 50 -->

[49] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. Generative Adversarial Nets. In *Proceedings of the 28th Conference on Neural Information Processing Systems (NIPS)*, pages 2672–2680, 2014.

[50] Aditya Grover and Jure Leskovec. node2vec: Scalable feature learning for networks. In *Proceedings of the 22nd International Conference on Knowledge Discovery and Data Mining (SIGKDD)*, pages 855–864. ACM, 2016.

[51] Aditya Grover, Aaron Zweig, and Stefano Ermon. Graphite: Iterative generative modeling of graphs. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, pages 2434–2444, 2019.

[52] Markus Hagenbuchner, Alessandro Sperduti, and Ah Chung Tsoi. A self-organizing map for adaptive processing of structured data. *IEEE Transactions on Neural Networks*, 14(3):491–505, 2003.

[53] Markus Hagenbuchner, Alessandro Sperduti, and Ah Chung Tsoi. Graph self-organizing maps for cyclic and unbounded graphs. *Neurocomputing*, 72(7-9):1419–1430, 2009.

[54] Will Hamilton, Zhitao Ying, and Jure Leskovec. Inductive representation learning on large graphs. In *Proceedings of the 31st Conference on Neural Information Processing Systems (NIPS)*, pages 1024–1034, 2017.

[55] William L. Hamilton, Rex Ying, and Jure Leskovec. Representation learning on graphs: Methods and applications. *IEEE Data Engineering Bulletin*, 40(3):52–74, 2017.

[56] Barbara Hammer, Alessio Micheli, and Alessandro Sperduti. Universal approximation capability of cascade correlation for structures. *Neural Computation*, 17(5):1109–1159, 2005.

50

<!-- page: 51 -->

[57] Barbara Hammer, Alessio Micheli, Alessandro Sperduti, and Marc Strickert. A general framework for unsupervised processing of structured data. *Neurocomputing*, 57:3–35, 2004. Publisher: Elsevier.

[58] Barbara Hammer, Alessio Micheli, Alessandro Sperduti, and Marc Strickert. Recursive self-organizing network models. *Neural Networks*, 17(8-9):1061–1085, 2004. Publisher: Elsevier.

[59] David K Hammond, Pierre Vandergheynst, and Rémi Gribonval. Wavelets on graphs via spectral graph theory. *Applied and Computational Harmonic Analysis*, 30(2):129–150, 2011. Publisher: Elsevier.

[60] Christoph Helma, Ross D. King, Stefan Kramer, and Ashwin Srinivasan. The predictive toxicology challenge 2000–2001. *Bioinformatics*, 17(1):107–108, 2001. Publisher: Oxford University Press.

[61] Sepp Hochreiter. Untersuchungen zu dynamischen neuronalen netzen. *Diploma, Technische Universität München*, 91(1), 1991.

[62] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. *Neural computation*, 9(8):1735–1780, 1997. Publisher: MIT Press.

[63] Giacomo Iadarola. Graph-based classification for detecting instances of bug patterns. Master's thesis, University of Twente, 2018.

[64] Sergey Ivanov and Evgeny Burnaev. Anonymous walk embeddings. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pages 2191–2200, 2018.

[65] Eric Jang, Shixiang Gu, and Ben Poole. Categorical reparametrization with gumbel-softmax. In *Proceedings of the 5th International Conference on Learning Representations (ICLR)*, 2017.

[66] Woosung Jeon and Dongsup Kim. FP2VEC: A new molecular featurizer for learning molecular properties. *Bioinformatics*, 35(23):4979–4985, 2019.

51

<!-- page: 52 -->

[67] Jianwen Jiang, Yuxuan Wei, Yifan Feng, Jingxuan Cao, and Yue Gao. Dynamic hypergraph neural networks. In *Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI)*, pages 2635–2641, 2019.

[68] H. Jin and X. Zhang. Latent adversarial training of graph convolution networks. In *Workshop on Learning and Reasoning with Graph-Structured Representations, International Conference on Machine Learning (ICML)*, 2019.

[69] Wengong Jin, Regina Barzilay, and Tommi S. Jaakkola. Junction tree variational autoencoder for molecular graph generation. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pages 2328–2337, 2018.

[70] Diederik P Kingma and Max Welling. Auto-encoding variational Bayes. *Proceedings of the 2nd International Conference on Learning Representations (ICLR)*, 2014.

[71] Thomas N Kipf and Max Welling. Variational graph auto-encoders. In *Workshop on Bayesian Deep Learning, Neural Information Processing System (NIPS)*, 2016.

[72] Thomas N Kipf and Max Welling. Semi-supervised classification with graph convolutional networks. In *Proceedings of the 5th International Conference on Learning Representations (ICLR)*, 2017.

[73] Teuvo Kohonen. The self-organizing map. *Proceedings of the IEEE*, 78(9):1464–1480, 1990.

[74] Youngchun Kwon, Jiho Yoo, Youn-Suk Choi, Won-Joon Son, Dongseon Lee, and Seokho Kang. Efficient learning of non-autoregressive graph variational autoencoders for molecular graph generation. *Journal of Cheminformatics*, 11(1):70, 2019. Publisher: Springer.

52

<!-- page: 53 -->

[75] Yann LeCun, Yoshua Bengio, and others. Convolutional networks for images, speech, and time series. *The Handbook of Brain Theory and Neural Networks*, 3361(10):1995, 1995.

[76] Junhyun Lee, Inyeop Lee, and Jaewoo Kang. Self-attention graph pooling. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, pages 3734–3743, 2019.

[77] Qimai Li, Zhichao Han, and Xiao-Ming Wu. Deeper insights into graph convolutional networks for semi-supervised learning. In *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI)*, 2018.

[78] Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard S. Zemel. Gated Graph Sequence Neural Networks. In *Proceedings of the 4th International Conference on Learning Representations, (ICLR)*, 2016.

[79] Yujia Li, Oriol Vinyals, Chris Dyer, Razvan Pascanu, and Peter W. Battaglia. Learning deep generative models of graphs. *CoRR*, abs/1803.03324, 2018.

[80] Qi Liu, Miltiadis Allamanis, Marc Brockschmidt, and Alexander Gaunt. Constrained graph variational autoencoders for molecule design. In *Proceedings of the 32nd Conference on Neural Information Processing Systems (NeurIPS)*, pages 7795–7804, 2018.

[81] László Lovász and others. Random walks on graphs: A survey. *Combinatorics, Paul Erdos is eighty*, 2(1):1–46, 1993.

[82] Andrew L. Maas, Awni Y. Hannun, and Andrew Y. Ng. Rectifier nonlinearities improve neural network acoustic models. In *Workshop on Deep Learning for Audio, Speech and Language Processing, International Conference on Machine Learning (ICML)*, 2013.

[83] Sofus A Macskassy and Foster Provost. Classification in networked data: A toolkit and a univariate case study. *Journal of Machine Learning Research*, 8(May):935–983, 2007.

53

<!-- page: 54 -->

[84] Diego Marcheggiani, Joost Bastings, and Ivan Titov. Exploiting semantics in neural machine translation with graph convolutional networks. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), Volume 2 (Short Papers)*, pages 486–492, 2018.

[85] Diego Marcheggiani and Ivan Titov. Encoding sentences with graph convolutional networks for semantic role labeling. In *Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1506–1515, 2017.

[86] Enrique S Marquez, Jonathon S Hare, and Mahesan Niranjan. Deep cascade learning. *IEEE Transactions on Neural Networks and Learning Systems*, 29(11):5475–5485, 2018. Publisher: IEEE.

[87] Luca Massarelli, Giuseppe Antonio Di Luna, Fabio Petroni, Roberto Baldoni, and Leonardo Querzoni. Safe: Self-attentive function embeddings for binary similarity. In *Proceedings of the 16th International Conference on Detection of Intrusions and Malware, and Vulnerability Assessment (DIMVA)*, pages 309–329. Springer, 2019.

[88] Alessio Micheli. Neural network for graphs: A contextual constructive approach. *IEEE Transactions on Neural Networks*, 20(3):498–511, 2009. Publisher: IEEE.

[89] Alessio Micheli, Diego Sona, and Alessandro Sperduti. Contextual processing of structured data by recursive cascade correlation. *IEEE Transactions on Neural Networks*, 15(6):1396–1410, 2004. Publisher: IEEE.

[90] Alessio Micheli, Alessandro Sperduti, and Antonina Starita. An introduction to recursive neural networks and kernel methods for cheminformatics. *Current Pharmaceutical Design*, 13(14):1469–1496, 2007.

[91] Pushkar Mishra, Helen Yannakoudakis, and Ekaterina Shutova. Neural character-based composition models for abuse detection. In *Proceedings*

54

<!-- page: 55 -->

*of the 2nd Workshop on Abusive Language Online (ALW2)*, pages 1–10, 2018.

[92] Federico Monti, Michael M. Bronstein, and Xavier Bresson. Geometric matrix completion with recurrent multi-graph neural networks. In *Proceedings of the 31st International Conference on Neural Information Processing Systems*, pages 3700–3710, 2017.

[93] Galileo Mark Namata, Ben London, Lise Getoor, and Bert Huang. Query-driven active surveying for collective classification. In *Proceedings of the Workshop on Mining and Learning with Graphs*, 2012.

[94] Yaroslav Nechaev, Francesco Corcoglioniti, and Claudio Giuliano. SocialLink: exploiting graph embeddings to link DBpedia entities to Twitter profiles. *Progress in Artificial Intelligence*, 7(4):251–272, 2018. Publisher: Springer.

[95] Michel Neuhaus and Horst Bunke. Self-organizing maps for learning the edit costs in graph matching. *IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)*, 35(3):503–514, 2005.

[96] Bryan Perozzi, Rami Al-Rfou, and Steven Skiena. Deepwalk: Online learning of social representations. In *Proceedings of the 20th International Conference on Knowledge Discovery and Data Mining (SIGKDD)*, pages 701–710. ACM, 2014.

[97] Meng Qu, Yoshua Bengio, and Jian Tang. GMNN: Graph Markov Neural Networks. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, pages 5241–5250, 2019.

[98] Liva Ralaivola, Sanjay J Swamidass, Hiroto Saigo, and Pierre Baldi. Graph kernels for chemical informatics. *Neural Networks*, 18(8):1093–1110, 2005. Publisher: Elsevier.

[99] Leonardo FR Ribeiro, Pedro HP Saverese, and Daniel R Figueiredo. struc2vec: Learning node representations from structural identity. In *Pro-*

55

<!-- page: 56 -->

*ceedings of the 23rd International Conference on Knowledge Discovery and Data Mining (SIGKDD)*, pages 385–394. ACM, 2017.

[100] Veeru Sadhanala, Yu-Xiang Wang, and Ryan Tibshirani. Graph sparsification approaches for laplacian smoothing. In *Artificial Intelligence and Statistics*, pages 1250–1259, 2016.

[101] Bidisha Samanta, Abir De, Gourhari Jana, Pratim Kumar Chattaraj, Niloy Ganguly, and Manuel Gomez Rodriguez. NeVAE: A deep generative model for molecular graphs. In *Proceedings of the 33rd AAAI Conference on Artificial Intelligence (AAAI)*, pages 1110–1117, 2019.

[102] Tae San Kim, Won Kyung Lee, and So Young Sohn. Graph convolutional network approach applied to predict hourly bike-sharing demands considering spatial, temporal, and global effects. *PloS one*, 14(9), 2019. Publisher: Public Library of Science.

[103] Lawrence K Saul and Michael I Jordan. Mixed memory Markov models: Decomposing complex stochastic processes as mixtures of simpler ones. *Machine Learning*, 37(1):75–87, 1999. Publisher: Springer.

[104] Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini. The graph neural network model. *IEEE Transactions on Neural Networks*, 20(1):61–80, 2009. Publisher: IEEE.

[105] Michael Schlichtkrull, Thomas N Kipf, Peter Bloem, Rianne van den Berg, Ivan Titov, and Max Welling. Modeling relational data with graph convolutional networks. In *Proceedings of the 15th European Semantic Web Conference (ESWC)*, pages 593–607. Springer, 2018.

[106] Ida Schomburg, Antje Chang, Christian Ebeling, Marion Gremse, Christian Heldt, Gregor Huhn, and Dietmar Schomburg. BRENDA, the enzyme database: updates and major new developments. *Nucleic Acids Research*, 32(suppl 1), 2004.

56

<!-- page: 57 -->

[107] Prithviraj Sen, Galileo Namata, Mustafa Bilgic, Lise Getoor, Brian Galligher, and Tina Eliassi-Rad. Collective classification in network data. *AI magazine*, 29(3):93–93, 2008.

[108] Oleksandr Shchur, Maximilian Mumme, Aleksandar Bojchevski, and Stephan Günnemann. Pitfalls of graph neural network evaluation. *Workshop on Relational Representation Learning, Neural Information Processing Systems (NeurIPS)*, 2018.

[109] Nino Shervashidze, Pascal Schweitzer, Erik Jan van Leeuwen, Kurt Mehlhorn, and Karsten M Borgwardt. Weisfeiler-lehman graph kernels. *Journal of Machine Learning Research*, 12(Sep):2539–2561, 2011.

[110] Nino Shervashidze, SVN Vishwanathan, Tobias Petri, Kurt Mehlhorn, and Karsten Borgwardt. Efficient graphlet kernels for large graph comparison. In *Proceedings of the 12th International Conference on Artificial Intelligence and Statistics (AISTATS)*, pages 488–495, 2009.

[111] Martin Simonovsky and Nikos Komodakis. Dynamic edge-conditioned filters in convolutional neural networks on graphs. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, pages 3693–3702, 2017.

[112] Martin Simonovsky and Nikos Komodakis. GraphVAE: Towards generation of small graphs using variational autoencoders. In *Proceedings of the 27th International Conference on Artificial Neural Networks (ICANN)*, pages 412–422, 2018.

[113] Richard Socher, Cliff C Lin, Chris Manning, and Andrew Y Ng. Parsing natural scenes and natural language with recursive neural networks. In *Proceedings of the 28th International Conference on Machine Learning (ICML)*, pages 129–136, 2011.

[114] Alessandro Sperduti and Antonina Starita. Supervised neural networks for

57

<!-- page: 58 -->

the classification of structures. *IEEE Transactions on Neural Networks*, 8(3):714–735, 1997. Publisher: IEEE.

[115] Kai Sheng Tai, Richard Socher, and Christopher D. Manning. Improved semantic representations from tree-structured Long Short-Term Memory networks. In *Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics (ACL)*, pages 1556–1566, 2015.

[116] Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, and Bernhard Schoelkopf. Wasserstein auto-encoders. In *Proceedings of the 6th International Conference on Learning Representations (ICLR)*, 2018.

[117] Edmondo Trentin and Ernesto Di Iorio. Nonparametric small random networks for graph-structured pattern recognition. *Neurocomputing*, 313:14–24, 2018.

[118] Edmondo Trentin and Leonardo Rigutini. A maximum-likelihood connectionist model for unsupervised learning over graphical domains. In *Proceedings of the 12th International Conference on Artificial Neural Networks (ICANN)*, pages 40–49. Springer, 2009.

[119] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In *Proceedings of the 31st Conference on Neural Information Processing Systems (NIPS)*, pages 5998–6008, 2017.

[120] Petar Velickovic, Guillem Cucurull, Arantxa Casanova, Adriana Romero, Pietro Lio, and Yoshua Bengio. Graph attention networks. In *Proceedings of the 6th International Conference on Learning Representations (ICLR)*, 2018.

[121] Petar Velickovic, William Fedus, William L. Hamilton, Pietro Liò, Yoshua Bengio, and R. Devon Hjelm. Deep Graph Infomax. In *Proceedings of the 7th International Conference on Learning Representations (ICLR), New Orleans, LA, USA, May 6-9, 2019*, 2019.

58

<!-- page: 59 -->

[122] S Vichy N Vishwanathan, Nicol N Schraudolph, Risi Kondor, and Karsten M Borgwardt. Graph kernels. *Journal of Machine Learning Research*, 11(Apr):1201–1242, 2010.

[123] Ulrike Von Luxburg. A tutorial on spectral clustering. *Statistics and Computing*, 17(4):395–416, 2007. Publisher: Springer.

[124] Edward Wagstaff, Fabian B Fuchs, Martin Engelcke, Ingmar Posner, and Michael Osborne. On the limitations of representing functions on sets. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, pages 6487–6494, 2019.

[125] Nikil Wale, Ian A Watson, and George Karypis. Comparison of descriptor spaces for chemical compound retrieval and classification. *Knowledge and Information Systems*, 14(3):347–375, 2008. Publisher: Springer.

[126] Hongwei Wang, Jia Wang, Jialin Wang, Miao Zhao, Weinan Zhang, Fuzheng Zhang, Xing Xie, and Minyi Guo. GraphGAN: Graph representation learning with generative adversarial nets. In *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI)*, pages 2508–2515, 2018.

[127] Minjie Wang, Lingfan Yu, Da Zheng, Quan Gan, Yu Gai, Zihao Ye, Mufei Li, Jinjing Zhou, Qi Huang, Chao Ma, Ziyue Huang, Qipeng Guo, Hao Zhang, Haibin Lin, Junbo Zhao, Jinyang Li, Alexander J Smola, and Zheng Zhang. Deep Graph Library: Towards efficient and scalable deep learning on graphs. *Workshop on Representation Learning on Graphs and Manifolds, International Conference on Learning Representations (ICLR)*, 2019.

[128] Xiaolong Wang and Abhinav Gupta. Videos as space-time region graphs. In *Proceedings of the 15th European conference on computer vision (ECCV)*, pages 399–417, 2018.

59

<!-- page: 60 -->

[129] Yue Wang, Yongbin Sun, Ziwei Liu, Sanjay E Sarma, Michael M Bronstein, and Justin M Solomon. Dynamic graph cnn for learning on point clouds. *ACM Transactions on Graphics (TOG)*, 38(5):146, 2019. Publisher: ACM.

[130] Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long, Chengqi Zhang, and Philip S. Yu. A comprehensive survey on graph neural networks. *CoRR*, abs/1901.00596, 2019.

[131] Keyulu Xu, Weihua Hu, Jure Leskovec, and Stefanie Jegelka. How powerful are graph neural networks? In *Proceedings of the 7th International Conference on Learning Representations (ICLR)*, 2019.

[132] Keyulu Xu, Chengtao Li, Yonglong Tian, Tomohiro Sonobe, Ken-ichi Kawarabayashi, and Stefanie Jegelka. Representation learning on graphs with jumping knowledge networks. *Proceedings of the 35th International Conference on Machine Learning (ICML)*, pages 5453–5462, 2018.

[133] Pinar Yanardag and SVN Vishwanathan. Deep graph kernels. In *Proceedings of the 21th International Conference on Knowledge Discovery and Data Mining (SIGKDD*, pages 1365–1374. ACM, 2015.

[134] Liang Yang, Zesheng Kang, Xiaochun Cao, Di Jin, Bo Yang, and Yuanfang Guo. Topology optimization based graph convolutional network. In *Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI)*, pages 4054–4061, 2019.

[135] Ruiping Yin, Kan Li, Guangquan Zhang, and Jie Lu. A deeper graph neural network for recommender systems. *Knowledge-Based Systems*, 185:105020, 2019. Publisher: Elsevier.

[136] Rex Ying, Ruining He, Kaifeng Chen, Pong Eksombatchai, William L. Hamilton, and Jure Leskovec. Graph convolutional neural networks for web-scale recommender systems. In *Proceedings of the 24th International*

60

<!-- page: 61 -->

*Conference on Knowledge Discovery and Data Mining (SIGKDD)*, pages 974–983. ACM, 2018.

[137] Zhitao Ying, Jiaxuan You, Christopher Morris, Xiang Ren, Will Hamilton, and Jure Leskovec. Hierarchical graph representation learning with differentiable pooling. In *Proceedings of the 32nd Conference on Neural Information Processing Systems (NeurIPS)*, 2018.

[138] Jiaxuan You, Rex Ying, Xiang Ren, William L. Hamilton, and Jure Leskovec. GraphRNN: Generating realistic graphs with deep auto-regressive models. In *Proceedings of the 35th International Conference on Machine Learning (ICML)*, 2018.

[139] Bing Yu, Haoteng Yin, and Zhanxing Zhu. Spatio-temporal graph convolutional networks: A deep learning framework for traffic forecasting. In *Proceedings of the 27th International Joint Conference on Artificial Intelligence (IJCAI)*, 2018.

[140] Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh, Barnabas Poczos, Ruslan R Salakhutdinov, and Alexander J Smola. Deep sets. In *Proceedings of the 31st Conference on Neural Information Processing Systems (NIPS)*, pages 3391–3401, 2017.

[141] Daniele Zambon, Cesare Alippi, and Lorenzo Livi. Concept drift and anomaly detection in graph streams. *IEEE Transactions on Neural Networks and Learning Systems*, 29(11):5592–5605, 2018. Publisher: IEEE.

[142] Muhan Zhang, Zhicheng Cui, Marion Neumann, and Yixin Chen. An end-to-end deep learning architecture for graph classification. In *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI)*, 2018.

[143] Si Zhang, Hanghang Tong, Jiejun Xu, and Ross Maciejewski. Graph convolutional networks: a comprehensive review. *Computational Social Networks*, 6(1):11, 2019. Publisher: Springer.

61

<!-- page: 62 -->

[144] Ziwei Zhang, Peng Cui, and Wenwu Zhu. Deep learning on graphs: A survey. *CoRR*, abs/1812.04202, 2018.

[145] Zizhao Zhang, Haojie Lin, Yue Gao, and KLISS BNRist. Dynamic hypergraph structure learning. In *Proceedings of the 27th International Joint Conference on Artificial Intelligence (IJCAI)*, pages 3162–3169, 2018.

[146] Dengyong Zhou, Jiayuan Huang, and Bernhard Schölkopf. Learning with hypergraphs: Clustering, classification, and embedding. In *Proceedings of the 21st Conferece on Neural Information Processing Systems (NIPS)*, pages 1601–1608, 2007.

[147] Marinka Zitnik, Monica Agrawal, and Jure Leskovec. Modeling polypharmacy side effects with graph convolutional networks. *Bioinformatics*, 34(13):i457–i466, 2018.

[148] Daniel Zügner, Amir Akbarnejad, and Stephan Günnemann. Adversarial attacks on neural networks for graph data. In *Proceedings of the 24th International Conference on Knowledge Discovery and Data Mining (SIGKDD)*, pages 2847–2856. ACM, 2018.

62
