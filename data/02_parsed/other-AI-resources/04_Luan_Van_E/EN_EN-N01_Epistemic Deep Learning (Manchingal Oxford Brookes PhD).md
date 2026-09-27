<!-- page: 1 -->

# Epistemic Deep Learning: Enabling Machine Learning Models to ‘Know When They Do Not Know’

arXiv:2510.22261v1 [cs.LG] 25 Oct 2025

Shireen Kudukkil Manchingal

*This thesis is submitted in fulfillment of the requirements for the degree of*

**Doctor of Philosophy**

in **Computer Science and Mathematics**

*at the*

Department of Engineering, Computing, and Mathematics
Oxford Brookes University

May 31, 2025

<!-- page: 2 -->

<!-- page: 3 -->

iii

# Thesis Committee

## Supervisors

**Prof. Fabio Cuzzolin**
*Professor of Artificial Intelligence*
*Director of AIDAS Institute*
*Oxford Brookes University*

**Dr. Andrew Bradley**
*Reader in Automotive & Motorsport Engineering*
*Lead, Autonomous Driving and Intelligent Transport*
*Oxford Brookes University*

**Dr. Matthias Rolf**
*Reader in Artificial Intelligence & Robotics*
*Postgraduate Research Tutor, PhD Computing*
*Oxford Brookes University*

## Examiners

**Dr. Alexander Rast**
*(Internal examiner)*
*Senior Lecturer in Artificial Intelligence*
*Leadership at AIDAS Institute*
*Oxford Brookes University*

**Dr. Sébastien Destercke**
*(External examiner)*
*Senior AI Researcher*
*Centre National de la Recherche Scientifique (CNRS)*
*Laboratoire Heuristique et Diagnostic des Systèmes Complexes (Heudiasyc)*
*Paris, France*

<!-- page: 4 -->

**Keywords:** Uncertainty Quantification, Bayesian Neural Networks, Model Uncertainty, Deep Learning, Machine Learning, Predictive Uncertainty, Random Sets, Belief Functions, Dempster-Shafer Theory, Set-Valued Predictions, Classification, Deep Ensembles, Adversarial Attacks, Model Calibration, Risk Assessment, Decision Making, Robustness, Reliability.

<!-- page: 5 -->

v

# Declaration

I hereby declare that except where specific reference is made to the work of others, the contents of this thesis are original and have not been submitted in whole or in part for consideration for any other degree or qualification in this, or any other university. This thesis is my own work, except for contributions explicitly specified in the text, Acknowledgements, and any mentioned collaborations. This thesis contains less than 65,000 words excluding bibliography, footnotes, tables, and equations and has fewer than 80 figures.

Shireen Kudukkil Manchingal

May 2025

<!-- page: 6 -->

<!-- page: 7 -->

vii

# Acknowledgements

I am profoundly grateful to my supervisor, *Fabio*, whose unwavering support, patience, and insightful guidance have been the foundation of both this research and my development as a researcher. His steadfast belief in my potential, and the intellectual freedom he granted me, has been instrumental in shaping both this work and my academic identity. The impact he has had on my career is immense, and his mentorship is a guiding influence I will carry with me throughout my life.

I am also deeply thankful to my second supervisor, *Andy*, for his thoughtful advice, constant encouragement and support throughout this journey, which has greatly enriched both this work and my growth as a researcher. My sincere gratitude goes to my third supervisor, *Matthias*, whose guidance throughout my PhD journey, also in the form of my PGR tutor, provided me with the clarity and motivation needed during challenging phases.

I feel incredibly fortunate to have worked alongside brilliant colleagues throughout this journey. Special thanks to the entire Epistemic AI project team—*Kaizheng*, *Mubashar*, *Maryam*, *Matthijs*, *Hans*, *Neil*, *Julian*, *Keivan*, *David*, *Salman*, *Moritz*, *Noah*, *Pascal*, *Adam*, and *Guopeng*—for several insightul discussions and constant motivation. I am also grateful to collaborators like *Michele*, and VAIL members *Izzeddin*, *Vivek* and *Ajmal*, whose insights and camaraderie made this experience truly rewarding.

I am also sincerely thankful to the staff at the *Department of Engineering, Computing, and Mathematics* for providing a supportive academic environment and invaluable resources that made this research possible.

Most importantly, I owe my deepest gratitude to my family—my parents *Assia* and *Mohammed*, *Shafna*, *Shakeer*, *Rayyan* and *Raha*. *Safeer*, my partner, has been my greatest support and strength throughout this journey. Their unconditional love and patience have been my anchor through the challenges and triumphs of this process.

*This thesis is based on work conducted as part of the* **European Union's Horizon 2020 Research and Innovation Programme** *under Grant Agreement No. 964505 (E-pi), which has also funded my PhD and supported this research throughout.*

<!-- page: 8 -->

<!-- page: 9 -->

ix

*In loving memory of*

Ayisha,

*my grandmother,*
*and the strongest woman I know,*
*who passed away in 2023*
*during my PhD journey.*

<!-- page: 10 -->

<!-- page: 11 -->

xi

# Abstract

*Epistemic Deep Learning: Enabling Machine Learning Models to ‘Know When They Do Not Know’*

by **Shireen Kudukkil Manchingal**

Machine learning has achieved remarkable successes, particularly with deep learning, yet its deployment in safety-critical domains remains hindered by an inherent inability to manage uncertainty, resulting in overconfident and unreliable predictions when models encounter out-of-distribution data, adversarial perturbations, or naturally fluctuating environments.

This thesis, titled *Epistemic Deep Learning: Enabling Machine Learning Models to ‘Know When They Do Not Know’*, addresses these critical challenges by advancing the paradigm of **Epistemic Artificial Intelligence**, which explicitly models and quantifies *epistemic uncertainty*: the uncertainty arising from limited, biased, or incomplete training data, as opposed to the irreducible randomness of *aleatoric uncertainty*, thereby empowering models to acknowledge their limitations and refrain from overconfident decisions when uncertainty is high.

Central to this work is the development of the **Random-Set Neural Network (RS-NN)**, a novel methodology that leverages random set theory to predict belief functions over sets of classes, capturing the extent of epistemic uncertainty through the width of associated credal sets, and demonstrating superior performance in terms of robustness and out-of-distribution detection compared to traditional approaches. The final part of the thesis explores applications of RS-NN, including its adaptation to Large Language Models (LLMs) and its deployment in weather classification for autonomous racing.

In addition, the thesis proposes a **unified evaluation framework for uncertainty-aware classifiers**, motivated by the observation that existing methods employ heterogeneous uncertainty measures, such as mutual information in Bayesian models, variance in deep ensembles, thereby impeding systematic comparisons; the proposed framework bridges this gap by providing a common metric that balances prediction accuracy with precision or imprecision, enabling objective assessment and model selection for safety-critical applications.

Extensive experiments validate that integrating epistemic awareness into deep learning not only mitigates the risks associated with overconfident predictions but also lays the foundation for a paradigm shift in artificial intelligence, where the ability to ‘know when it does not know’ becomes a hallmark of robust and dependable systems. The title encapsulates the core philosophy of this work, emphasizing that true intelligence involves recognizing and managing the limits of one's own knowledge.

<!-- page: 12 -->

xii

# Contents

- Thesis Committee — iii
- Declaration — v
- Acknowledgements — vii
- Abstract — xi
- 1 Introduction — 1
  - 1.1 Motivation — 1
  - 1.2 Research Questions — 3
  - 1.3 Thesis Structure — 3
  - 1.4 Contributions — 5
  - 1.5 Dissemination — 5
- I KNOWING WHAT WE DO NOT KNOW — 7
- 2 Background: Uncertainty Quantification in Deep Learning — 9
  - 2.1 Sources of Uncertainty: Aleatoric vs. Epistemic — 9
  - 2.2 Predictive Uncertainty — 10
  - 2.3 Why Uncertainty Quantification Matters — 11
    - 2.3.1 Adversarial Robustness — 11
    - 2.3.2 Robustness and Domain Adaptation — 12
    - 2.3.3 Out-of-distribution (OoD) detection — 12
    - 2.3.4 Calibration — 13
    - 2.3.5 Sequential decision-making — 13
- 3 Related Work: Machine Learning Models For Representing Uncertainty — 15
  - 3.1 Traditional and Deterministic methods — 15
  - 3.2 Bayesian Methods — 17
  - 3.3 Ensemble methods — 20
  - 3.4 Evidential Methods — 21
  - 3.5 Conformal prediction — 21
  - 3.6 Imprecise models — 22
  - 3.7 Discussion on existing methods and motivating this thesis — 24

<!-- page: 13 -->

xiii

- II EPISTEMIC DEEP LEARNING — 26
- 4 Epistemic Artificial Intelligence — 28
  - 4.1 Concept — 28
  - 4.2 Why Epistemic AI is Essential — 29
  - 4.3 Modeling A Lack Of Knowledge — 30
    - 4.3.1 Theories of uncertainty: Beyond Bayesian Probabilities — 30
      - 4.3.1.1 Random Sets — 31
      - 4.3.1.2 Belief functions — 32
      - 4.3.1.3 Credal Sets — 33
      - 4.3.1.4 A unified example — 33
  - 4.4 Classical Probabilities vs. Random Sets & Belief Functions — 34
  - 4.5 Leveraging Epistemic AI — 35
- 5 Random-Set Neural Networks — 36
  - 5.1 Key Contributions — 38
  - 5.2 Methodology — 39
    - 5.2.1 Ground-truth Representation — 39
    - 5.2.2 Budgeting — 40
    - 5.2.3 Training RS-NN: Loss Function — 42
    - 5.2.4 Accuracy & Uncertainty Estimation — 43
    - 5.2.5 RS-NN Learning Mechanism — 44
  - 5.3 Experiments — 45
    - 5.3.1 Implementation — 45
      - 5.3.1.1 Datasets — 45
      - 5.3.1.2 Baselines and backbones — 46
      - 5.3.1.3 Training details — 47
      - 5.3.1.4 Sample prediction — 47
    - 5.3.2 Performance: Accuracy & Expected Calibration Error — 48
    - 5.3.3 Out-of-distribution detection — 50
    - 5.3.4 Uncertainty Estimation — 51
      - 5.3.4.1 Entropy of pignistic predictions — 51
      - 5.3.4.2 Credal set width — 53
      - 5.3.4.3 Entropy/Credal Set Width vs. Confidence score — 54
    - 5.3.5 Scalability to Large-Scale Architectures — 55
    - 5.3.6 Overcoming the Overconfidence Problem in CNNs — 56
    - 5.3.7 Robustness to noisy and rotated data — 57
    - 5.3.8 Robustness to Adversarial Attacks — 59
    - 5.3.9 Application to Text Classification — 61
    - 5.3.10 Ablation Studies — 62
      - 5.3.10.1 ImageNet vs. ImageNet-O — 62
      - 5.3.10.2 Ablation study on hyperparameters α and β — 63
      - 5.3.10.3 Ablation Study on the number of focal sets — 65
      - 5.3.10.4 On the feasibility of budgeting of sets — 66
  - 5.4 Discussion and Implications — 67
- 6 Credal Set Models — 68

<!-- page: 14 -->

xiv

  - 6.1 Credal Interval Neural Networks (Cre-INN) — 69
  - 6.2 Credal Deep Ensembles (CreDE) — 71
- III EVALUATING EPISTEMIC PREDICTIONS — 72
- 7 Evaluation under Uncertainty — 74
  - 7.1 Current metrics for evaluation — 74
  - 7.2 Classes of Epistemic Predictions — 75
- 8 A Unified Evaluation Framework for Epistemic Predictions — 77
  - 8.1 Key Contributions — 77
  - 8.2 Methodology: Mapping Predictions to Credal Sets — 78
    - 8.2.1 Coherent Lower Probabilities — 78
    - 8.2.2 Computing lower probabilities from a sample of probability vectors — 79
    - 8.2.3 Computing masses by Moebius inverse — 79
    - 8.2.4 Computing the Credal Set of Predictions — 80
  - 8.3 Methodology: Evaluation of Epistemic Predictions — 81
    - 8.3.1 The Metric — 81
      - 8.3.1.1 Distance Computation — 81
      - 8.3.1.2 Non-Specificity — 82
    - 8.3.2 Rationale and Interpretation — 83
    - 8.3.3 Model Selection and Scenarios — 84
    - 8.3.4 Practical utility of the Evaluation metric — 85
    - 8.3.5 Evaluation Metric or Uncertainty Measure? — 86
  - 8.4 Experiments — 87
    - 8.4.1 Implementation — 87
      - 8.4.1.1 Datasets — 87
      - 8.4.1.2 Baselines and Backbones — 87
      - 8.4.1.3 Training Details — 88
      - 8.4.1.4 Obtaining Epistemic Predictions — 88
    - 8.4.2 Analysis of the Evaluation Metric — 88
    - 8.4.3 Evaluation of the trade-off parameter — 92
    - 8.4.4 Model Selection using the Evaluation Metric — 92
    - 8.4.5 Ablation Studies — 94
      - 8.4.5.1 Metric behavior for Correct (CC) vs. Incorrect Classifications (ICC) — 95
      - 8.4.5.2 The effect of approximating credal set vertices — 95
      - 8.4.5.3 Ablation study on different distance measures — 97
      - 8.4.5.4 Ablation study on different non-specificity measures — 101
      - 8.4.5.5 Distance measure vs. Confidence score — 103
      - 8.4.5.6 Credal set size vs. Non-specificity — 105
      - 8.4.5.7 Ablation on number of prediction samples — 106
  - 8.5 Discussion and Implications — 107

<!-- page: 15 -->

xv

- IV APPLICATIONS — 108
- 9 Random-Set Large Language Models — 110
  - 9.1 Methodology — 110
  - 9.2 Experiments — 112
    - 9.2.1 Implementation — 112
    - 9.2.2 Performance — 113
    - 9.2.3 Uncertainty Estimation — 113
    - 9.2.4 Hallucination Evaluation — 113
    - 9.2.5 Budgeting Analysis — 114
    - 9.2.6 Ablation Studies — 114
  - 9.3 Discussion and Implications — 115
- 10 Application to Autonomous Racing — 117
  - 10.1 Experimental Setup for Weather/cone Classification — 117
  - 10.2 Cone classification — 118
  - 10.3 Weather classification — 119
    - 10.3.1 Domain Adaptation setting — 120
  - 10.4 Discussion — 121
- 11 Conclusions — 122
  - 11.1 Thesis Summary — 122
  - 11.2 Impact on the Epistemic AI paradigm — 123
  - 11.3 Limitations — 125
  - 11.4 Broader challenges within Epistemic Deep Learning — 126
- 12 Future Directions — 128
- V APPENDIX — 131
- A Algorithms — 133
  - A.0.1 Algorithm for Budgeting — 133
  - A.0.2 Algorithm for ECE — 133
  - A.0.3 Algorithm for AUROC, AUPRC — 134
- B Statistical guarantees — 137

<!-- page: 16 -->

xvi

# List of Figures

- 1.1 Overview of the thesis structure. — 4
- 2.1 Confidence scores of uncertainty-aware (Epistemic) and standard model with no uncertainty estimation (Traditional) for samples of ImageNet-A (adversarial) dataset. — 11
- 2.2 In-distribution (*left*) *vs.* out-of-distribution (*right*) datasets. — 13
- 3.1 Major approaches to uncertainty in AI: (a) Traditional networks and Deterministic uncertainty models, (b) Bayesian neural networks, (c) Deep ensembles, (d) Evidential approaches, and (e) Epistemic approaches. — 16
- 3.2 Visualizations of 100 prediction samples obtained prior to Bayesian Model Averaging and corresponding Bayesian Model Averaged prediction in two real scenarios from CIFAR-10. — 19
- 4.1 Epistemic Learning. — 28
- 4.2 Clusters of uncertainty theories. — 30
- 4.3 The random set associated with a cloaked die in which faces 1 and 2 are not visible. — 31
- 4.4 A belief function is equivalent to a credal set with boundaries determined by lower bounds (Eq. 7.1) on probability values. — 33
- 5.1 Inference in a Bayesian Neural Network (top) as opposed to a Random-Set Neural Network (bottom), with corresponding measures of uncertainty and their sources. — 37
- 5.2 Confidence scores of RS-NN and CNN for FGSM adversarial attack for different perturbations (ϵ = 0.05, 0.01) on MNIST dataset. — 37
- 5.3 Standard one-hot encoded ground truth in traditional neural networks vs. belief function-based encoding in Random-Set Neural Networks (RS-NN). — 39
- 5.4 RS-NN model architecture: (a) Budgeting, (b) Training and Inference. — 40
- 5.5 2D visualization of the clusters of 10 classes of CIFAR-10 dataset and the ellipses formed by RS-NN based on the hyperparameters of Gaussian Mixture Models. — 41
- 5.6 Upper and lower bounds (Eq. 5.5), in dotted red, to the probability of the predicted most likely class according to the pignistic prediction (in solid red) for 100 samples of CIFAR-10. — 43
- 5.7 Visualizations of belief and mass predictions on the power-set space and its mapping to the label space using pignistic probabilities on the CIFAR-10 dataset. — 48
- 5.8 Entropy comparison of all models for iD and OoD datasets. The plots illustrate the performance of various models, with error bars indicating the standard deviation of entropy values. — 51
- 5.9 Entropy, predicted class and belief value graph for two samples of CIFAR-10 dataset. — 52

<!-- page: 17 -->

xvii

- 5.10 Uncertainty (entropy) of MNIST digit '3' rotated between -90 and 90 degrees. The blue line indicates RS-NN estimates low uncertainty between -30 to 30, and high uncertainty for further rotations. — 52
- 5.11 Entropy Distributions for RS-NN on MNIST vs. Fashion-MNIST/Kuzushiji-MNIST. — 53
- 5.12 Entropy Distributions for RS-NN on CIFAR-10 vs. SVHN/Intel-Image. — 53
- 5.13 Width of credal predictions for CIFAR-10 test data (correctly classified, blue; incorrectly classified, red). — 53
- 5.14 Credal set widths for individual classes of CIFAR-10 dataset. For Correctly Classified samples *(left)*. For Incorrectly Classified samples *(right)*. — 54
- 5.15 Entropy vs. Confidence score on iD (left) vs. OoD (right) datasets. For CIFAR-10, most predictions are concentrated top left of the plot indicating lower entropy and higher confidence in the predictions. For SVHN and Intel Image datasets, predictions are more distributed. — 55
- 5.16 Credal Set Width vs. Confidence score on iD (left) vs. OoD (right) datasets. For CIFAR-10, confidence scores are high and credal set width is small. For SVHN and Intel Image datasets, credal set width varies for each prediction and is less reliant on confidence score. — 55
- 5.17 Confidence scores for Incorrectly Classified samples of RS-NN and CNN — 56
- 5.18 Entropy distribution of RS-NN on CIFAR-10, Noisy CIFAR-10, and Rotated CIFAR-10 — 58
- 5.19 Confidence scores of RS-NN on CIFAR-10, Noisy CIFAR-10, and Rotated CIFAR-10 — 59
- 5.20 Examples of perturbed images generated using FGSM adversarial attacks on the MNIST dataset for different epsilon values. Epsilon values range from 0 to 0.05. — 59
- 5.21 Test accuracies of RS-NN on the CIFAR-10 dataset using ResNet50, for a fixed K = 20 and different values of hyperparameters α and β in the loss function. — 64
- 5.22 Ablation study on number of non-singleton focal sets K on CIFAR-10 dataset using ViT-Base-16 (with α = β = 1e − 3). The maximum value of K can be 1013 for 10 classes (after excluding the singletons and empty set). — 65
- 6.1 Illustration of the proposed CreINN model for a three-class classification task. — 69
- 6.2 Comparison between the proposed Credal Deep Ensembles and traditional Deep Ensembles. — 71
- 7.1 Different types of uncertainty-aware model predictions, shown in a unit simplex of probability distributions defined on the list of classes **Y** = {a, b, c}. — 75
- 8.1 Different types of uncertainty-aware model predictions, shown in a unit simplex of probability distributions defined on the list of classes **Y** = {a, b, c}. The proposed evaluation framework uses a metric which combines, for each input **x**, a distance (arrows) between the corresponding ground truth (*e.g.* , (0, 1, 0)) and the *epistemic predictions* generated by the various models (in the form of credal sets), and a measure of the extent of the credal prediction (*non-specificity*). — 78
- 8.2 Measures of KL divergence (a)*(top left)*, (b) Non-specificity *(top right)*, (c) Evaluation Metric *(bottom left)* for both Correctly (CC) and Incorrectly Classified (ICC) samples from **CIFAR-10**, and (d) Evaluation metric *vs.* trade-off parameter *(bottom right)*, for all models, on the CIFAR-10 dataset. — 90

<!-- page: 18 -->

xviii

- 8.3 Measures of (a)*(top left)* Kullback-Leibler (KL) divergence, (b)*(top right)* Non-specificity (NS), (c)*(bottom left)* Evaluation Metric (E) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples (d)*(bottom right)* Evaluation metric (E) estimates vs. trade-off (λ) for all models on **MNIST**. — 90
- 8.4 Measures of (a)*(top left)* Kullback-Leibler (KL) divergence, *(top right)* Non-specificity (NS), (c)*(bottom left)* Evaluation Metric (E) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples (d)*(bottom right)* Evaluation metric (E) estimates vs. trade-off (λ) for all models on **CIFAR-100**. — 91
- 8.5 Probability simplices illustrating the convex closure of predictions and credal sets for the Bayesian model (LB-BNN) across three classes of the CIFAR-10 dataset. — 96
- 8.6 Credal set sizes for all models for 50 prediction samples of the CIFAR-10 dataset. Larger credal set sizes indicate a more imprecise prediction. — 97
- 8.7 Credal set sizes for all models for 50 prediction samples of the MNIST dataset. Larger credal set sizes indicate a more imprecise prediction — 97
- 8.8 Credal set sizes for all models for 50 prediction samples of the CIFAR-100 dataset. Larger credal set sizes indicate a more imprecise prediction — 97
- 8.9 Comparison of (a) Kullback-Leibler (KL) divergence, and (b) Jensen-Shannon (JS) divergence for Correctly Classified (CC) and Incorrectly Classified (ICC) samples from the CIFAR-10 dataset, for all models considered here. Notably, the scales of these two measures differ significantly (Y-axis). — 98
- 8.10 Comparison of mean Evaluation Metric E using mean Kullback Leibler (KL) divergence (top) and mean Jensen-Shannon (JS) divergence (bottom) for Correct (left) and Incorrect (right) predictions of the CIFAR-10 dataset. — 99
- 8.11 Scatter plots showing the relationship between uncertainty (KL and JS divergences) and non-specificity for correct and incorrect predictions across all models. Notably, the distinct ‘spike’ at non-specificity just above 1.5 highlights the characteristic output of a particular model. — 100
- 8.12 Comparison of (a) Non-Specificity (NS), and (b) Credal Uncertainty (CU) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples from the CIFAR-10 dataset, for all models considered here. Notably, the scales of these two measures differ (Y-axis). — 102
- 8.13 Comparison of mean Evaluation Metric E using mean Non-Specificity (top) and mean Credal Uncertainty (bottom) for Correct (left) and Incorrect (right) predictions of the CIFAR-10 dataset. — 102
- 8.14 Entropy vs. Confidence (top) and Non-Specificity vs. Confidence (bottom) for each of the models: (a) LB-BNN, (b) Deep Ensembles (DE), (c) CreINN, (d) E-CNN, (e) RS-NN and (f) EDL on the CIFAR-10 dataset. Entropy is strongly

<!-- page: 19 -->

xix

  linked to confidence, whereas non-specificity shows minimal correlation with it. — 104
- 8.15 Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN, (e) E-CNN and (f) RS-NN on the CIFAR-10 dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend. — 105
- 8.16 Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN, (e) E-CNN and (f) RS-NN on the MNIST dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend. — 105
- 8.17 Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN and (e) RS-NN on the CIFAR-100 dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend. — 106
- 8.18 Ablation study on the number of prediction samples of LB-BNN and the number of ensembles of DE with Evaluation Metric (E). — 107
- 9.1 Training and generation flow of RS-LLM. Training is performed in a parallel fashion using the teacher forcing method. Generation is done sequentially. For each token, the model predicts a belief function. Then the mass function, probability distribution and next token is subsequently computed/sampled from that belief function. — 111
- 9.2 Proposed budgeting method for RS-LLM. First, embeddings are computed for all the tokens in vocabulary. Then, focal sets are computed using hierarchical clustering. — 112
- 9.3 Training examples from CoQA and OBQA datasets. The text in black highlights the actual question, while the blue text represents prompt instructions. The model is trained to predict the text in green. — 112
- 9.4 Behavior of uncertainty measures of Llama2 and RS-Llama2 with respect to the correctness and closeness to the groundtruth on CoQA and OBQA datasets. — 114
- 9.5 (a) Centroid distance distribution. (b) Focal set size distribution. Sets with size > 30 excluded for visualization. — 115
- 10.1 Overview of datasets used for weather classification, including source, number of classes, class labels, and dataset sizes for training and testing. — 118
- 10.2 **Experimental setup for domain adaptation:** RS-NN and LB-BNN trained on OBR-A dataset are tested on R-Waymo. Comparison of entropy distributions (uncertainty estimates) for shared classes of both the datasets, and on the exclusive classes of the test dataset (R-Waymo) is shown. — 120
- 11.1 Comparison of Epistemic AI models (circles) and competitor models (squares) on CIFAR-10: (a) OoD detection performance (AUROC vs. AUPRC), (b) Predictive performance (Accuracy vs. ECE). — 124
- A.1 Receiver Operating Characteristic (ROC) and Precision-Recall Characteristic (PRC) curves for RS-NN, LB-BNN, ENN, and CNN evaluated on the SVHN and Intel Image OoD datasets for CIFAR-10. — 136
- A.2 Receiver Operating Characteristic (ROC) and Precision-Recall Characteristic (PRC) curves for RS-NN, LB-BNN, ENN, and CNN evaluated on the SVHN and Intel Image OoD datasets for MNIST. — 136
- B.1 Conformal prediction sets by RS-NN on the CIFAR-10 dataset. The predicted probabilities for each class is shown. — 138
- B.2 Conformal prediction threshold for CIFAR-10 indicating the boundary beyond which predictions are considered non-conformal. — 138
- B.3 Coverage per class of RS-NN for CIFAR-10 dataset. — 138
- B.4 Average size of the predictive sets generated for each class of CIFAR-10. — 138

<!-- page: 20 -->

xx

# List of Tables

- 5.1 Training Hyperparameters for All Models — 46
- 5.2 The predicted belief, mass values, pignistic probabilities, and entropy for two CIFAR-10 predictions. The figure on the top (True Label = ‘horse’) is a certain prediction with 99.9% confidence and a low entropy of 0.0017, whereas the figure on the bottom (True Label = ‘cat’) is an uncertain prediction with 33.3% confidence and a higher entropy of 2.6955. — 47
- 5.3 Test accuracies (%) and inference time (ms) for uncertainty estimation over 5 consecutive runs across methods and datasets. Average and standard deviation are shown for each experiment. — 49
- 5.4 Training time (min) for all models on the CIFAR-10 dataset. — 49
- 5.5 OoD detection performance and uncertainty estimation for models trained on ResNet50 on CIFAR-10 vs. SVHN/Intel Image, MNIST vs. F-MNIST/K-MNIST and ImageNet vs. ImageNet-O. Evaluation metrics include AUROC/AUPRC (OoD); Entropy of predictions (uncertainty) and Expected Calibration Error (ECE). — 50
- 5.6 Credal set width for RS-NN on iD vs. OoD datasets: CIFAR10 vs. SVHN/Intel Image, MNIST vs. F-MNIST/K-MNIST and ImageNet vs. ImageNet-O. — 54
- 5.7 Adaptability to large-scale model architectures with test accuracy (%) and parameters (in million) reported on CIFAR10. — 56
- 5.8 CNN fails to perform well when tested on an noisy (rotated) sample of MNIST test data. The predicted results show how a standard CNN predicts the wrong class with a high confidence score (99.95%), while the RS-NN model predicts the correct class with 49.7% confidence and a high entropy of 2.1626. — 56
- 5.9 CNN fails to perform well when tested on noisy and rotated samples of MNIST test data. The predicted results show how a standard CNN predicts the wrong class with a high confidence score, whereas the RS-NN model predicts the right class with varying confidence scores. — 57
- 5.10 Test accuracies(%) for RS-NN, standard CNN, LB-BNN (Bayesian) and ENN (Ensemble) on noisy samples of MNIST . ‘Scale’ represents the standard deviation of the normal distribution from which random numbers are being generated for random noise. — 58
- 5.11 Test accuracies(%) for RS-NN, standard CNN, LB-BNN (Bayesian) and ENN (Ensemble) on Rotated MNIST out-of-distribution (OoD) samples. Rotation angle is random between the values given. — 58
- 5.12 Test accuracies of CNN, RS-NN, LB-BNN and ENN models under FGSM adversarial attacks on MNIST and CIFAR-10 dataset for different epsilon values. Epsilon values range from 0 to 0.05. — 60

<!-- page: 21 -->

xxi

- 5.13 Test accuracies of CNN, RS-NN, LB-BNN and ENN models under PGD adversarial attacks on MNIST and CIFAR-10 datasets with α = 1/255 and number of iterations = 10. Epsilon values range from 0 to 0.05 — 60
- 5.14 Test accuracy, AUROC, AUPRC, iD vs. OoD entropy for RS-NN BERT and CNN BERT (both fine-tuned on BERT). — 62
- 5.15 Credal set width and entropy for RS-NN using ViT-B-16 model on ImageNet vs. ImageNet-O datasets. — 63
- 5.16 OoD detection and uncertainty estimation performance for iD vs. OoD dataset: CIFAR-10 vs. CIFAR-100. — 63
- 5.17 OoD detection performance: Comparison of accuracy, AUROC and AUPRC for standard RS-NN vs. budgeted RS-NN on the CIFAR-10 dataset. — 66
- 5.18 Uncertainty estimation: Comparison of pignistic entropy and credal set width for standard RS-NN vs. budgeted RS-NN on the CIFAR-10 dataset. — 66
- 5.19 Test accuracy and OoD detection (AUROC, AUPRC) results on RS-NN where budgeting is done using t-SNE vs. budgeting done on UMAP. — 67
- 5.20 Entropy and credal set width results on RS-NN where budgeting is done using t-SNE vs. budgeting done on UMAP. The goal is to minimize both metrics for in-distribution (iD) data while increasing them for out-of-distribution (OoD) data. — 67
- 8.1 Comparison of Evaluation Metric (E) for Models A, B, C, and D under different values of λ. — 85
- 8.2 Comparison of Kullback-Leibler divergence (KL), Non-Specificity (NS) and Evaluation Metric (E) for uncertainty-aware classifiers (trade-off λ = 1). Mean and standard deviation are shown for CIFAR-10, MNIST and CIFAR-100 datasets. — 89
- 8.3 Trade-off (λ) vs. Evaluation Metric (E) for different values of λ for the CIFAR-10 dataset. — 93
- 8.4 Model Rankings Based on KL and NS on CIFAR-10 for different values of λ. Model selection is based on the mean of Evaluation Metric (E) with models with the lowest E ranking first. — 93
- 8.5 Model Selection Based on Evaluation Metric using KL and Non-Specificity on MNIST. — 94
- 8.6 Model Selection Based on Evaluation Metric using KL and Non-Specificity on CIFAR-100. — 94
- 8.7 Comparison of KL divergence (KL), Non-Specificity (NS), and Evaluation Metric (E) (trade-off λ = 1) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples for each model on three datasets: CIFAR-10, MNIST, and CIFAR-100. — 95
- 8.8 Comparison of KL, Non-Specificity, Evaluation Metric (E) calculated using approximated versus naive credal set vertices for LB-BNN and DE on the CIFAR-10 dataset. — 96
- 8.9 Model Rankings Based on KL and JS Divergence on the CIFAR-10 dataset. Model selection is based on the mean of Evaluation Metric (E) with the models with the lowest E ranking first. — 99
- 8.10 Model Rankings Based on Non-Specificity (NS) and Credal Uncertainty (CU) on the CIFAR-10 dataset. Model selection is based on the mean of Evaluation Metric (E) with the models with the lowest E ranking first. The distance metric used here is KL divergence. — 103

<!-- page: 22 -->

xxii

- 9.1 Performance of Standard LLMs and RS-LLMs on CoQA and OBQA datasets. For CoQA, cosine similarity is reported while accuracy is reported for OBQA. — 113
- 9.2 Uncertainty evaluation of Standard Llama2 and RS-Llama2 on correct and incorrect context. — 113
- 9.3 Cosine similarity across α = β values. — 115
- 9.4 Cosine similarity across budget sizes on CoQA. — 115
- 10.1 The predicted belief, mass values, pignistic probabilities, and entropy for two cone-centric dataset predictions. — 118
- 10.2 Performance of RS-NN, CNN, and LB-BNN on R-WAYMO, OBR-A, and CONE datasets. We report classification accuracy, predictive entropy, and confidence estimates for both incorrect classifications (ICC ↓) and correct classifications (CC ↑). — 119
- 10.3 Performance of RS-NN, CNN, and LB-BNN on domain adaptation tasks across OBR-A and ROAD datasets. Only classification accuracy and entropy are reported, as confidence metrics are not directly applicable in cross-domain settings. — 121
- 11.1 Training (in minutes; per 100 epochs) and inference time (in milliseconds; per sample) comparison of uncertainty estimation methods on the CIFAR-10 dataset. — 124

<!-- page: 23 -->

xxiii

<!-- page: 24 -->

1

# 1 Introduction

## 1.1 Motivation

The success of artificial intelligence (AI), particularly in the realm of deep learning, is widely acknowledged and continues to redefine the boundaries of what machines can achieve (LeCun et al., 2015). AI models have demonstrated impressive capabilities across a wide spectrum of tasks, from image recognition and natural language processing to game playing and protein folding (Jumper et al., 2021). Large language models (LLMs) such as GPT-3 (Brown et al., 2020) exemplify the growing capacity of neural networks to manipulate and generate human-like language. Generative models, including DALL·E 2 (Ramesh et al., 2022), have advanced into creative domains, generating novel content across modalities. Moreover, multimodal systems like CLIP (Radford et al., 2021) have bridged vision and language, achieving strong performance in tasks requiring cross-domain understanding. Despite these advancements, the deployment of AI in real-world systems often falls short of expectations, revealing a gap between benchmark success and operational reliability.

This gap has fueled both public enthusiasm and critical reflection. Some of the most anticipated AI applications, such as fully autonomous vehicles, remain underdeveloped for worldwide deployment despite significant investment and media attention (Amodei et al., 2016). While self-driving prototypes can perform well under controlled conditions, they consistently struggle to generalize across diverse, unstructured environments. Similarly, generative AI models, while compelling, often exhibit hallucination, inconsistency, and brittleness under distributional shift (Bender et al., 2021). Meanwhile, discourse around artificial general intelligence (AGI) and the speculative risk of uncontrollable AI systems often diverts attention from the immediate, pressing challenge of ensuring robustness, reliability, and interpretability in today's systems (Russell et al., 2015).

Neural networks, while powerful, are also often overconfident in their predictions, even when presented with adversarial inputs, noise, or samples drawn from distributions not represented in the training data (Papernot et al., 2016; Hendrycks and Gimpel, 2016; Hüllermeier and Waegeman, 2021; Zhang et al., 2021). This overconfidence is not just a theoretical concern; it manifests in high-stakes applications such as autonomous driving, where models fail to generalize to unexpected scenarios like unusual weather, rare traffic patterns, or sensor failures (Bojarski, 2016). Despite mitigation strategies such as dropout regularization (Srivastava et al., 2014), domain adaptation (Ganin and Lempitsky, 2015), adversarial training (Goodfellow et al., 2014), and various ensemble methods, the core problem persists.

There is a growing consensus that the accurate estimation of *uncertainty* (Cuzzolin, 2024) is vital to improve machine learning models' reliability (Senge et al., 2014; Kendall and Gal, 2017). However, one of the most pressing limitations of modern machine learning (ML) systems is their inability to handle uncertainty in a principled and efficient manner. This has fueled increasing

<!-- page: 25 -->

2                                                                         Chapter 1. Introduction

interest in the field of uncertainty quantification (UQ), which aims to enable models to assess and express uncertainty about their predictions. Accurate uncertainty estimation is critical for deploying ML models in safety-critical environments where incorrect or overconfident decisions can result in significant harm. For instance, in autonomous driving, predictive uncertainty can be used to trigger fallback strategies or human intervention (Fort and Jastrzebski, 2019); in medical diagnosis, uncertainty-aware models can defer decisions to clinicians when confidence is low (Lambrou et al., 2010); and in climate and infrastructure applications such as flood risk estimation (Chaudhary et al., 2022) and structural health monitoring (Vega and Todd, 2022), quantifying uncertainty informs probabilistic risk assessments. Machine learning techniques for UQ span a wide methodological spectrum, including Bayesian Neural Networks (BNNs) (Blundell et al., 2015; Gal and Ghahramani, 2016; Jospin et al., 2022), Deep Ensembles (Lakshminarayanan et al., 2017), Monte Carlo dropout (Gal and Ghahramani, 2016), Evidential Deep Learning (Sensoy et al., 2018), and approaches grounded in Conformal Prediction (Angelopoulos and Bates, 2021).

However, these existing UQ methods have key limitations. *Bayesian* models are sensitive to prior mis-specification (with the risk of biasing the whole process) and incur heavy computational overhead (Fortuin, 2022; Caprio et al., 2023b), and Bayesian Model Averaging (BMA) may dilute useful predictive information (Hinne et al., 2020; Graefe et al., 2015). *Ensemble* methods are computationally demanding (Jospin et al., 2022; He et al., 2020). *Conformal* predictors lose validity and efficiency in the presence of distributional shift or model misspecification without adjustments for epistemic uncertainty (Bates et al., 2023). *Evidential* approaches (Sensoy et al., 2018) violate asymptotic assumptions, struggle with out-of-distribution data (Bengs et al., 2022; Ulmer et al., 2023; Kopetzki et al., 2021; Stadler et al., 2021) and exhibit high inference times (Tab. 11.1). These shortcomings underscore the inadequacy of current methods in capturing the full spectrum of uncertainty, as well as their inefficiency in deployment within complex, real-world environments.

This thesis addresses that gap by exploring epistemic uncertainty quantification in deep learning (for classification tasks), focusing on techniques that enable models to express *ignorance* (Sec. 4.3) in meaningful, interpretable, and actionable ways. It operates within the paradigm of **Epistemic Artificial Intelligence** (Chapter 4), which emphasizes the importance of learning from ignorance, in line with the Socratic principle: ‘know that you do not know.’ A central contribution of Epistemic Artificial Intelligence (Epistemic AI) is its principled use of second-order uncertainty measures (Sec. 4.3.1) to represent and reason about epistemic uncertainty, *i.e.*, uncertainty arising from a lack of knowledge or insufficient information. Unlike traditional probabilistic models that assign precise probabilities to outcomes (first-order uncertainty), Epistemic AI explicitly models uncertainty about uncertainty. This second-order framework enables systems to quantify their own ignorance, rather than being forced to commit to possibly overconfident or ill-informed predictions. Second-order uncertainty measures such as random sets (Molchanov, 2005) and credal sets (Levi, 1980; Cuzzolin, 2008a) are rooted in imprecise probability theory (Sec. 3.6) and offer a richer language for expressing model uncertainty in situations where the data is ambiguous, scarce, or non-representative.

To realize this Epistemic AI perspective, this thesis proposes principled frameworks for UQ in machine learning. It tackles two main challenges:

- Developing a rigorous and mathematically grounded method for estimating epistemic uncertainty by leveraging second-order uncertainty measures, which better represent ignorance and the inherent uncertainty about unknowns. This is achieved

<!-- page: 26 -->

1.2. Research Questions                                                                        3

through the introduction of **Random-Set Neural Networks (RS-NN)** (Chapter 5), a novel classification approach based on the theory of random sets that overcomes limitations of existing UQ methods. Contributions to credal set models are also briefly discussed in Chapter 6.

- **Enabling fair and consistent comparison of different UQ methods**, as their epistemic predictions often take disparate forms. This challenge is addressed by proposing A Unified Evaluation Framework for Epistemic Predictions (Chapter 8), which standardizes the evaluation process and helps practitioners select the most suitable model for their application.

## 1.2 Research Questions

Motivated by these challenges and the existing academic literature, which is detailed in Chapter 3, this thesis aims to answer the following key research questions:

> **Q1: How can epistemic uncertainty be formally and reliably quantified in deep learning models using second-order uncertainty representations such as random sets while tackling set complexity?**

Standard probabilistic models, including Bayesian approaches, struggle to represent epistemic uncertainty because a single probability distribution cannot capture ignorance. This question investigates whether more expressive, set-based frameworks can provide a principled alternative for modeling uncertainty (Chapter 5), and if they can be made computationally feasible (Sec. 5.2.2).

> **Q2: How do epistemic models that employ second-order uncertainty measures, such as random sets, behave when confronted with previously unseen or adversarial inputs at test time?**

This question explores whether such models can more effectively distinguish between familiar and unfamiliar data, thereby improving out-of-distribution (OoD) detection (Sec. 5.3.3) and providing greater robustness against adversarial perturbations (Secs. 5.3.8 & 5.3.7).

> **Q3: How can a unified and principled evaluation framework be designed to compare epistemic uncertainty predictions across methods that produce fundamentally different output structures?**

Given that different approaches yield probability vectors, intervals, belief functions, or sets, this question seeks a unified evaluation methodology (Chapter 8) for fair comparison.

## 1.3 Thesis Structure

The thesis is organized into **four** main parts as shown in Fig. 1.1. **Part I** (*Knowing What We Do Not Know*) introduces the conceptual foundations of uncertainty in machine learning (Chapter 2), why uncertainty quantification matters (Sec. 2.3), and the two main sources of uncertainty: *aleatoric* uncertainty (stems from inherent data noise) and *epistemic* uncertainty

<!-- page: 27 -->

4                                                                                Chapter 1. Introduction

(due to limited knowledge) (Sec. 2.1). It surveys a broad spectrum of existing and emerging models for representing epistemic uncertainty (Chapter 3). This part lays the foundation for robust epistemic modeling and motivates the central research questions addressed throughout the thesis.

**Part II** (*Epistemic Deep Learning*) introduces the paradigm of **Epistemic Artificial Intelligence** (Chapter 4), which emphasizes learning from ignorance, and details the use of second-order uncertainty measures (Chapter 4.3) to model a lack of knowledge (ignorance). The thesis then presents a novel **Random-Set Neural Network (RS-NN)** (Chapter 5) approach to classification which predicts *belief functions* (rather than classical probability vectors) over the class list using the mathematics of random sets. RS-NN encodes the ‘epistemic’ uncertainty induced by training sets that are insufficiently representative or limited in size via the size of the convex set of probability vectors associated with a predicted belief function. RS-NN outperforms state-of-the-art Bayesian and Ensemble methods (Sec. 5.3) in terms of *accuracy*, *uncertainty estimation* and *out-of-distribution (OoD) detection* on multiple benchmarks (CIFAR-10 *vs.* SVHN/Intel-Image, MNIST *vs.* FMNIST/KMNIST, ImageNet *vs.* ImageNet-O). RS-NN also scales up effectively to large-scale architectures (*e.g.* WideResNet-28-10, VGG16, Inception V3, EfficientNetB2 and ViT-Base-16), exhibits remarkable robustness to *adversarial attacks* and can provide statistical guarantees in a conformal learning setting (§B). RS-NN is extended to the domain of text generation through the development of **Random-Set Large Language Models (RS-LLMs)** in Part IV *(Applications)*, Chapter 9. Further collaborative research on **credal set models**, another family of second-order uncertainty representations, is briefly discussed in Chapter 6.

[FIGURE: Figure 1.1. Overview of the thesis structure.]

Text in figure:

PART I
Knowing What We Do Not Know
Introduces aleatoric vs. epistemic uncertainty, and surveys existing approaches.

PART II
Epistemic Deep Learning
Introduces Epistemic AI and a novel uncertainty method called Random-Set Neural Networks.

PART III
Evaluating Epistemic Predictions
Proposes a unified evaluation framework to compare epistemic predictions.

PART IV
Applications
Demonstrates applicability on Large Language Models (LLMs) and weather classification in autonomous racing.

**Part III** (*Evaluating Epistemic Predictions*) focuses on the evaluation of uncertainty-aware models, a largely underexplored topic. It discusses related work on evaluation under uncertainty (Chapter 7) and introduces **a unified evaluation framework for assessing epistemic predictions** (Chapter 8). This includes new metrics for gauging both *accuracy* (distance-based) and *imprecision* from predictions, supported by experimental analysis and ablation studies (Sec. 8.4).

**Part IV** *(Applications)* showcases the practical implementation of Random-Set Neural Networks (RS-NNs) through two case studies: first, their extension to Large Language Models (LLMs) for text generation, leading to the creation of **Random-Set Large Language Models**

<!-- page: 28 -->

1.4. Contributions                                                                              5

**(RS-LLMs)** (Chapter 9); and second, their use in **weather classification for autonomous racing** (Chapter 10). These applications highlight the value of modeling epistemic uncertainty to develop more robust, transparent, and safer machine learning systems in real-world scenarios.

The final chapter **concludes** the thesis (Chapter 11), providing summaries of key contributions and methods (Sec. 11.1), as well as discussions on **limitations** (Sec. 11.3) and **future research directions** (Sec. 12) for each method. Additionally, the broader **impact of the epistemic deep learning models** proposed in this thesis on the emerging field of Epistemic AI is explored in Sec. 11.2. The chapter further elaborates on **open challenges** (Sec. 11.4) and prospects for the **future of Epistemic AI** (Sec. 12). The Appendix contains detailed algorithms for the methods (§A) and statistical guarantees for RS-NN under a conformal setting (§B). The code for the experiments presented in this work is available at https://github.com/shireenkmanch.

## 1.4 Contributions

This thesis contributes a novel class of models based on random sets and establishes a principled framework for evaluating uncertainty-aware models in deep learning. The key contributions are as follows:

- **Random-Set Neural Networks (RS-NN):** A novel class of classifiers grounded in the theory of random sets, which enables models to represent and reason about epistemic uncertainty in a mathematically rigorous way. RS-NNs allow models to express structured ignorance by outputting sets of plausible labels rather than single-point predictions, a capability unavailable in standard probabilistic approaches. Importantly, this random-set framework is not limited to classification tasks; it can also be applied to complex problems such as text generation in large language models, providing a new avenue for uncertainty-aware natural language processing.
- **A scalable framework for controlling set complexity:** This thesis introduces an innovative budgeting mechanism to manage and limit the complexity of random sets, making second-order uncertainty representations both practical and interpretable. Rather than relying on the full power set of possibilities (which is often computationally infeasible), this approach strategically selects a representative subset of sets. This enables random-set models to maintain strong performance and reliable uncertainty quantification without the overhead of handling all possible combinations.
- **A Unified Evaluation Framework for Epistemic Predictions:** To enable fair comparison between epistemic uncertainty quantification methods that produce heterogeneous outputs (*e.g.*, distributions, intervals, sets), this thesis proposes a model-agnostic evaluation framework. This framework standardizes key performance metrics for epistemic models and provides guidance for selecting appropriate methods based on task-specific needs.

## 1.5 Dissemination

This thesis is based in part on the following publications, preprints, and dissemination activities:

<!-- page: 29 -->

6                                                                                Chapter 1. Introduction

**Peer-reviewed Publications**

1. **Manchingal, S. K.**, Mubashar, M., Wang, K., Shariatmadar, K., & Cuzzolin, F. *Random-Set Neural Networks*. Proceedings of the Thirteenth International Conference on Learning Representations (ICLR 2025).
2. **Manchingal, S. K.**, Mubashar, M., Wang, K., & Cuzzolin, F. *A Unified Evaluation Framework for Epistemic Predictions*. Proceedings of the 28th International Conference on Artificial Intelligence and Statistics (AISTATS 2025).
3. Wang, K., Shariatmadar, K., **Manchingal, S. K.**, Cuzzolin, F., Moens, D., & Hallez, H. *CreINNs: Credal-Set Interval Neural Networks for Uncertainty Estimation in Classification Tasks*. (Neural Networks 2025).
4. Wang, K., Cuzzolin, F., **Manchingal, S. K.**, Shariatmadar, K., Moens, D., & Hallez, H. *Credal Deep Ensembles for Uncertainty Quantification.* Advances in Neural Information Processing Systems (NeurIPS 2024).
5. **Manchingal, S. K.**, & Cuzzolin, F. *Epistemic Deep Learning*. ICML 2022 Workshop on Distribution-free Uncertainty Quantification (ICML-DFUQ 2022).

**Workshops**

In addition to the publications, the author also participated in organizing the following workshop:

- The First Workshop on Epistemic Uncertainty in Artificial Intelligence (E-pi), International Conference on Uncertainty in Artificial Intelligence (UAI 2023).

  *Workshop link*: https://sites.google.com/view/epi-workshop-uai-2023/home

  *Workshop proceedings*: https://link.springer.com/book/10.1007/978-3-031-57963-9

**Software and Reproducibility**

To promote transparency and reproducibility, all developed codebases and experiments have been made available:

- Random-Set Neural Networks (*Codebase*): https://github.com/shireenkmanch/Random-Set-Neural-Networks
- A Unified Evaluation Framework for Epistemic Predictions (*Codebase*): https://github.com/shireenkmanch/Evaluation-Epistemic-Preds
- CreINNs: Credal-Set Interval Neural Networks for Uncertainty Estimation in Classification Tasks (*Codebase*): https://github.com/WangKaizheng/CreINNs

<!-- page: 30 -->

7

# Part I

# KNOWING WHAT WE DO NOT KNOW

<!-- page: 31 -->

<!-- page: 32 -->

9

# 2 Background: Uncertainty Quantification in Deep Learning

Machine learning is fundamentally about building models from data, often with the goal of making predictions. A core challenge in this process is dealing with *uncertainty*. When a machine learning model ‘learns’, it generalizes from the specific examples it has seen to broader patterns or rules that apply beyond the training data. This process, called induction, inherently involves uncertainty because the model is only an approximation—it can never be proven absolutely correct. Instead, models are hypotheses about how the data were generated, so their predictions come with some degree of uncertainty.

Moreover, uncertainty in machine learning does not just come from the inductive nature of learning. Other sources include incorrect assumptions within the model and noise or errors in the data itself. These factors can affect the reliability of the model's predictions. Representing and managing this uncertainty accurately is essential, especially in safety-critical applications such as autonomous driving (Fort and Jastrzebski, 2019), medical diagnosis (Lambrou et al., 2010), flood uncertainty estimation (Chaudhary et al., 2022), and structural health monitoring (Vega and Todd, 2022), where incorrect decisions can have serious consequences.

Uncertainty is also a fundamental concept within machine learning techniques themselves. For example, in active learning (Aggarwal et al., 2014), algorithms focus on reducing uncertainty by selectively querying the most informative data points. Similarly, decision tree algorithms (Mitchell, 1980) use measures of uncertainty (like information gain) to decide how to split data and build the model. Machine learning models often struggle to provide reliable predictions when confronted with unfamiliar data (Guo et al., 2017a; Ovadia et al., 2019; Minderer et al., 2021), be it noisy samples (Papernot et al., 2016) deliberately designed to deceive models, or out-of-distribution data (OoD) beyond the model's training distribution. An ideal learning system, especially when deployed in safety-critical applications, should be aware of how confident it is in its own predictions, acknowledge the limits of its knowledge and gauge these limitations to make informed decisions by modelling the uncertainty associated with it, in essence, *‘to know when it does not know’*.

## 2.1 Sources of Uncertainty: Aleatoric Vs. Epistemic

The defining issue for AI now is how it manages uncertainty and leverages data, with a key distinction between *epistemic* (reducible) and *aleatoric* (irreducible) uncertainty. The latter refers to the different outcomes a random experiment produces, for example, when we play roulette, we cannot know in advance what the outcome of each single spin is, but can predict that they

<!-- page: 33 -->

10                                                              Chapter 2. Background: Uncertainty Quantification in Deep Learning

will arise (over time) with a known frequency (1/36). By contrast, the former express a more essential lack of knowledge about what underlying process drives the observed phenomenon. A player faced with the choice of playing one of a number of roulette wheels, without knowing the workings of each wheel (*i.e.*, what probability distribution models it), will be subject to such ‘epistemic’ uncertainty. A similar distinction between ‘common cause’ and ‘special cause’ (Snee, 1990) is central in the philosophy of probability (Keynes, 2013). Unlike uncertainty caused by randomness (aleatoric), uncertainty due to ignorance (epistemic) can, in principle, be reduced with the acquisition of additional information (Hüllermeier and Waegeman, 2021). However, this reduction is theoretically guaranteed only in the limit of infinite data, assuming that the data sufficiently covers the input space and that the learning algorithm has sufficient capacity to approximate the true underlying distribution.

That said, the relevance of this distinction is not universally agreed upon. In many real-world machine learning scenarios, models are trained to optimize performance rather than disentangle the origins of their uncertainty. When predictions must be made regardless of data limitations, the source of uncertainty, whether due to inherent noise or lack of knowledge, is often treated uniformly. Recent work (de Jong et al., 2024; Mucsányi et al., 2024) questions whether aleatoric and epistemic uncertainties are cleanly separable in high-capacity models, where incomplete knowledge and stochastic variability often interact.

The main source of uncertainty in AI (but also in its science and engineering applications) is the lack of a sufficient amount of data to train a model, in both quantity and quality (*i.e.*, data fairly describing all regions of operation, including rare events). This uncertainty is **epistemic in nature**, as it concerns the model itself, and can be reduced by collecting more data or information.

Epistemic uncertainty can be modeled at two levels: (i) a *target* level, where the network outputs an uncertainty measure on the target space, while its parameters (weights) remain deterministic; (ii) a *parameter* level, where uncertainty is modeled on the parameter space (*i.e.*, weights and biases). This thesis presents a novel method to feasibly implement random sets, during training and inference, to represent uncertainty at the target level. The extension of this approach to model uncertainty at the parameter level using random sets is reserved for future work (Sec. 12). In this thesis, we focus mainly on epistemic uncertainty, especially in the context of **predictive uncertainty over the target space**, as accurately quantifying it remains a central challenge in AI.

## 2.2 Predictive Uncertainty

While aleatoric uncertainty may stem from inherent ambiguities in the data or inaccuracies in class annotations, epistemic uncertainty arises from our incomplete knowledge about the true underlying model parameters governing the relationship between input features and class labels. Epistemic uncertainty represents the disparity between the true distribution \(p^*\) and and the model's estimate \(\hat{p}\). In practice, aleatoric uncertainty is almost always computed by the UQ community as the **difference between predictive (total) uncertainty and epistemic uncertainty**. Consequently, the primary focus of this thesis is on computing predictive and epistemic uncertainty.

In supervised learning tasks, e.g, classification, where the objective is to assign class labels \(y \in \mathbf{Y}\) to input data points \(\mathbf{x} \in \mathbf{X}\), *predictive uncertainty* can be represented using the predictive

<!-- page: 34 -->

2.3. Why Uncertainty Quantification Matters                                                    11

distribution \(\hat{p}(y \mid \mathbf{x}, \mathbb{D})\), where \(y \in \mathbf{Y}\) is a label, \(\mathbf{x} \in \mathbf{X}\) an input instance, and \(\mathbb{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^{\mathcal{N}} \in \mathbf{X} \times \mathbf{Y}\) the available training set, \(\mathcal{N}\) being the number of training instances. The true data-generating distribution remains unknown to us, in turn implying uncertainty about the true predictive distribution. A model will provide its best estimate \(\hat{p}(y|\mathbf{x}, \mathbb{D})\) based on the available data \(\mathbb{D}\).

As introduced earlier, this thesis proposes a novel model based on random sets that predicts epistemic uncertainty over sets of probability distributions. Since **epistemic uncertainty is defined differently across various uncertainty-aware models**, direct comparison of these measures is not straightforward. Therefore, we propose an evaluation framework that enables comparison between models predicting both predictive entropy and epistemic uncertainty, despite differences in their formulations, by leveraging their predictions within a unified metric space.

## 2.3 Why Uncertainty Quantification Matters

As mentioned in Sec. 1.1, uncertainty quantification is crucial for improving the reliability and safety of machine learning models, particularly in real-world, safety-critical applications. Without a clear understanding of prediction confidence, models can exhibit *overconfidence*, *fail to adapt to new domains*, and *make unsafe decisions*. This section highlights key motivations for uncertainty quantification, including enhancing adversarial robustness, improving domain adaptation, calibrating confidence estimates, and supporting safer sequential decision-making. Together, these aspects demonstrate why accurate modeling of uncertainty is essential for trustworthy AI systems.

### 2.3.1 Adversarial Robustness

Traditional neural networks often suffer from overconfidence, producing highly confident predictions even when incorrect, which can lead to serious consequences in safety-critical applications. This issue arises because softmax probabilities represent relative confidence rather than true uncertainty, causing these models to assign high confidence to out-of-distribution (OoD) inputs or adversarially perturbed data (Guo et al., 2017a; Hendrycks and Gimpel, 2016).

[FIGURE: Figure 2.1. Confidence scores of uncertainty-aware (Epistemic) and standard model with no uncertainty estimation (Traditional) for samples of ImageNet-A (adversarial) dataset.]

Text in figure:

ImageNet-A
Epistemic: 'walking stick' (3.96%)     'Arctic fox, white fox' (32.93%)
Traditional: 'jeweler's loupe' (86.9%)     'swing' (94.95%)
True label: 'pelican'          True label: 'pug, pug-dog'

Figure 2.1: Confidence scores of uncertainty-aware (Epistemic) and standard model with no uncertainty estimation (Traditional) for samples of ImageNet-A (adversarial) dataset. Traditional model is overconfident in a misclassification with confidence scores of 86.9% and 94.95%, whereas the epistemic model exhibits lower confidence with scores of 32.93% and 3.96% for misclassifications.

For instance, Fig. 2.1 shows incorrect predictions by a standard ResNet50 (Traditional) and an uncertainty-aware model (Epistemic) based on ResNet50 over a classification problem on

<!-- page: 35 -->

12                                                              Chapter 2. Background: Uncertainty Quantification in Deep Learning

the ImageNet-A dataset. The uncertainty-aware (Epistemic) model used here is Random-Set Neural Network (Chapter 5). ImageNet-A (adversarial) (Hendrycks et al., 2021) is a challenging adversarially filtered dataset designed to deliberately expose the overconfidence and poor generalization of models. As shown in Fig. 2.1, when a standard ResNet50 with no uncertainty estimation and an uncertainty-aware model based on ResNet50, both trained on ImageNet are tested on ImageNet-A, the standard model tends to exhibit high confidence in incorrect predictions, whereas the uncertainty-aware model assigns lower confidence to misclassifications, avoiding overconfidence.

### 2.3.2 Robustness and Domain Adaptation

Robustness in machine learning often focuses on domain adaptation (Awais et al., 2021; Alijani et al., 2024), using methods like minimax learning (Azar et al., 2017), counterfactual error bounding (Swaminathan and Joachims, 2015), and custom loss functions to adapt models to target domains. In unsupervised domain adaptation, adversarial approaches reduce the gap between source and target domain features. While reinforcement learning has less focus on robustness, some work includes adversarial methods (Pinto et al., 2017) and Bayesian Bellman formulations (Derman et al., 2020). Recent research on out-of-distribution (OoD) generalization and domain generalization (DG) addresses discrepancies between training and test distributions (Gulrajani and Lopez-Paz, 2020; Koh et al., 2021; Singh et al., 2024), with theoretical work on kernel methods (Blanchard et al., 2011; Deshmukh et al., 2019; Hu et al., 2020; Muandet et al., 2013) and domain-adversarial learning using H-divergence (Albuquerque et al., 2019). However, these methods struggle when training and test distributions differ significantly (Rosenfeld et al., 2022), and managing uncertainty can improve domain adaptation (OoD).

### 2.3.3 Out-of-distribution (OoD) Detection

Out-of-distribution (OoD) detection refers to a model's ability to identify inputs that deviate significantly from the training data distribution. In real-world scenarios, a model may encounter inputs that lie outside the support of its training distribution (Hendrycks and Gimpel, 2016). Making overconfident predictions on such OoD inputs can lead to erroneous and potentially harmful outcomes. Thus, incorporating uncertainty estimation is essential to enable models to recognize unfamiliar inputs and express appropriate caution (Amodei et al., 2016).

Quantitatively, OoD detection performance is commonly evaluated using metrics such as the Area Under the Receiver Operating Characteristic curve (AUROC) and the Area Under the Precision-Recall Curve (AUPRC). AUROC assesses the model's ability to distinguish between in- and out-of-distribution samples based on uncertainty scores, while AUPRC is particularly informative in imbalanced settings, where OoD instances are rare.

The OoD detection procedure (detailed in Algorithm §A.0.3) begins by aggregating uncertainty scores from in-distribution (iD) and OoD inputs. Binary labels are assigned (0 for iD, 1 for OoD), and these are combined with the corresponding scores to compute the ROC curve, which plots the true positive rate (TPR) against the false positive rate (FPR) across various thresholds. The AUROC is then computed as the area under this curve. Likewise, a precision-recall (PR) curve is generated, and the AUPRC is obtained. Higher AUROC and AUPRC values indicate better separation between iD and OoD samples, reflecting the model's ability to assign lower confidence (higher uncertainty) to unfamiliar inputs.

<!-- page: 36 -->

2.3. Why Uncertainty Quantification Matters                                                    13

In this thesis, out-of-distribution (OoD) data refers to inputs that differ significantly from the distribution of the training data, meaning they represent scenarios or classes that the model has not encountered during training. For example, if a model is trained on CIFAR-10 (Krizhevsky et al., 2009), which consists of natural images of objects like cats, cars, and airplanes, then inputs from the SVHN (Netzer et al., 2011) dataset composed of street-view house number digits would be considered OoD (Fig. 2.2), since they represent a fundamentally different visual domain.

[FIGURE: Figure 2.2. In-distribution (left) vs. out-of-distribution (right) datasets.]

Text in figure:

In-distribution (iD) dataset (CIFAR-10): airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck (example image grid rows)
Out-of-distribution (OoD) dataset (SVHN): street-view house number digit images

Figure 2.2: In-distribution (left) vs. out-of-distribution (right) datasets.

It is important to note that there are multiple perspectives on what constitutes OoD data: some define OoD strictly as samples from entirely new classes not present during training, while others also consider shifts in data style, context, or domain as forms of OoD, even if the underlying classes overlap.

### 2.3.4 Calibration

Neural networks are typically uncalibrated, meaning that when a network predicts \(\hat{y}\) with confidence \(\delta\), the fraction of correct predictions at confidence \(\delta\) should be equal to \(\delta\), which often does not occur (Guo et al., 2017a). To address this, various calibration techniques (Ojeda et al., 2023) like histogram binning, Bayesian binning, and Platt scaling have been proposed (Platt et al., 1999), with extensions to regression (Kuleshov et al., 2018). Metrics such as Expected Calibration Error (ECE) (Naeini et al., 2015) and Adaptive Calibration Error (ACE) (Nixon et al., 2019) are commonly used to quantify calibration error. Loss-based adjustments (Mukhoti et al., 2020; Luo et al., 2022; Tao et al., 2023) aim to actively improve model calibration, though they often overlook deeper issues in uncertainty representation.

### 2.3.5 Sequential Decision-making

In sequential decision-making tasks such as autonomous driving, the decisions made at each step influence future actions and outcomes. Unlike single-shot predictions, where uncertainty might only impact a single decision, sequential decision-making requires a model to account for uncertainty over time. This is particularly important because each decision made in a sequence can have long-term consequences (Schwarting et al., 2018), and failure to properly manage uncertainty can result in compounded errors. For instance, in autonomous driving (Teeti et al., 2023), a vehicle must make real-time decisions about route planning, vehicle control, and responding to dynamic environments (*e.g.*, pedestrians, traffic signals, or road hazards). If uncertainty in perception or state estimation is not adequately modeled, the vehicle might make

<!-- page: 37 -->

14                                                              Chapter 2. Background: Uncertainty Quantification in Deep Learning

decisions that could lead to unsafe situations, such as misinterpreting a pedestrian's motion or failing to account for out-of-date maps. Effective uncertainty quantification (Kendall and Gal, 2017; Depeweg et al., 2018), particularly epistemic uncertainty, helps the system understand when it is uncertain about its predictions, enabling more cautious and informed decision-making.

<!-- page: 38 -->

15

# 3 Related Work: Machine Learning Models For Representing Uncertainty

The machine learning community has recognized the challenge of estimating uncertainty in model predictions, leading to the development of several Bayesian approximations (Gal and Ghahramani, 2016; Charpentier et al., 2020), evidential Dirichlet models (Sensoy et al., 2018; Gao et al., 2024) and conformal prediction (Shafer and Vovk, 2008; Papadopoulos et al., 2008; Balasubramanian et al., 2014; Vovk, 2012; Angelopoulos and Bates, 2021). Ensemble-based approaches, such as Deep Ensembles (DE) (Lakshminarayanan et al., 2017) and Epistemic Neural Networks (ENN) (Osband et al., 2024), estimate uncertainty by leveraging multiple models. However, the computational cost of training ensembles, especially for large models, is often impractical. Some methods rely on prior knowledge (Fortuin, 2022), whereas others require setting a desired threshold on predictions (Angelopoulos and Bates, 2021). Some (Baron, 1987; Hüllermeier and Waegeman, 2021) have argued that classical probability is not equipped to model ‘second-level’ uncertainty on the probabilities themselves. This has led to the formulation of numerous uncertainty calculi (Cuzzolin, 2020), including possibility theory (Dubois and Prade, 1990), probability intervals (Halpern, 2017), credal sets (Levi, 1980), random sets (Nguyen, 1978) or imprecise probability (Walley, 1991).

This chapter surveys related work in uncertainty-aware ML models for classification tasks, outlining the various types of uncertainty-aware approaches, their methods for computing predictive uncertainty, and the nature of their resulting predictions. The predictions of a classifier can be plotted in the simplex (convex hull) of the one-hot probability vectors assigning probability 1 to a particular class. For instance, in a 3-class classification scenario (**Y** = {a, b, c}), the simplex would be a 2D simplex (triangle) connecting three points, each representing one of the classes, as shown in Fig. 3.1 (center). Fig. 3.1 shows major uncertainty-aware models in AI and their predictions on a 3-class probability simplex.

## 3.1 Traditional and Deterministic Methods

Traditional machine learning models provide deterministic predictions for classification (categorical labels) or regression tasks (continuous values), and inherently lacks mechanisms to capture epistemic uncertainty, as they assume precise knowledge of the dependency between inputs and outputs. One type of standard model is denoted as CNN (Convolutional Neural Network) in this thesis, as it mainly focuses on image classification. Traditional/standard neural networks (CNN) predict a vector of N scores, one for each class, duly *calibrated* to a probability vector representing a (discrete, categorical) probability distribution over the list of classes **Y**,

$$
\hat{p}_s(y \mid \mathbf{x}, \mathbb{D}),
$$
(3.1)

<!-- page: 39 -->

16                                                              Chapter 3. Related Work: Machine Learning Models For Representing Uncertainty

[FIGURE: Figure 3.1. Major approaches to uncertainty in AI: (a) Traditional networks and Deterministic uncertainty models, (b) Bayesian neural networks, (c) Deep ensembles, (d) Evidential approaches, and (e) Epistemic approaches.]

Text in figure:

(a) Traditional/DDU → Point predictions
(b) Bayesian → Bayesian Posterior → Bayesian Model Averaging
(c) Deep Ensembles → Ensemble predictions → Ensemble Averaging
(d) Evidential → Dirichlet predictions → Averaging
(e) Epistemic → Random-Set predictions → Credal sets with pignistic probability

Center: Probability simplex with classes a, b, c
p(b) = 1 (1,0,0)     p(a) = 1 (0,1,0)     p(c) = 1 (0,0,1)

Legend: (a) Traditional, DDU; (b) Bayesian; (c) Ensemble; (d) Evidential; Credal Set; Random-Set; × Pignistic

Figure 3.1: **Major approaches to uncertainty in AI.** While traditional networks and Deterministic uncertainty models (Mukhoti et al., 2023) (a) have deterministic weights, and output either a deterministic output value or a probability vector in the output space, Bayesian neural networks (Blundell et al., 2015; Gal and Ghahramani, 2016; Rudner et al., 2022) (b) compute a predictive distribution there by integrating over a learnt posterior distribution of model parameters given training data. As this is often infeasible due to the complexity of the posterior, Bayesian Model Averaging (BMA) (Hinne et al., 2020; Graefe et al., 2015) is often used to approximate the predictive distribution by averaging over predictions from many samples. The same (averaging) technique can be applied to (deep) ensembles of networks (Lakshminarayanan et al., 2017) (c), in which a number of models are trained independently using different initializations. Evidential approaches (Sensoy et al., 2018) (d) make predictions as parameters of a second-order Dirichlet distribution on the output space, instead of softmax probabilities. Finally, epistemic approaches (e) employ second-order probability representations, either in the output space or the target space, *e.g.* in the form of interval probabilities, credal sets or random sets (Manchingal et al., 2025b). A pignistic probability (Smets, 2005) estimate can be obtained from credal sets for comparison to other models (Manchingal et al., 2025a).

which represents the probability of observing class y given the input **x** and training data \(\mathbb{D}\).

A recent development, Deep Deterministic Uncertainty (DDU) (Mukhoti et al., 2023) estimates epistemic uncertainty by analyzing latent representations or using distance-sensitive functions, rather than predicted softmax probabilities (Alemi et al., 2018; Wu and Goodman, 2020; Liu et al., 2020; Mukhoti et al., 2023; Van Amersfoort et al., 2020). However, regularization techniques based on feature space distances, such as bi-Lipschitz regularization (used by most of these models), do not effectively improve OoD detection or calibration (Postels et al., 2021). This is due to the limitations of distance metrics in high-dimensional data, such as images. These methods have been applied to areas like object detection (Gasperini et al., 2021) but overlooks calibration: how well uncertainty reflects model performance under shifting distributions. Calibration is crucial for safe deployment but remains underexplored, as DDUs are typically tested only on simple tasks and datasets, leaving their effectiveness in more complex scenarios unproven (Postels et al., 2021).

Moreover, unlike other uncertainty-aware baselines, DDU represents uncertainty in the input space (by identifying an input sample as in- or out-of-distribution) rather than the prediction space. As a result, DDU provides predictions \(\hat{p}_{ddu}(y \mid \mathbf{x}, \mathbb{D})\) in the form of softmax probabilities akin to traditional neural networks. Both DDU and traditional models make point predictions (see Fig. 3.1).

<!-- page: 40 -->

3.2. Bayesian Methods                                                                          17

## 3.2 Bayesian Methods

Bayesian Deep Learning (BDL) (Buntine and Weigend, 1991; MacKay, 1992; Neal, 2012) is the most well-known approach to uncertainty quantification in AI. It leverages Bayesian neural networks (BNNs) (Blundell et al., 2015; Gal and Ghahramani, 2016; Jospin et al., 2022) to model network parameters (*i.e.*, weights and biases) as distributions, predicting a ‘second-order’ distribution, a distribution of distributions (Hüllermeier and Waegeman, 2021), with predictions often generated by running the network on sample parameters extracted from an approximated posterior.

Bayesian uncertainty quantification in deep neural networks is commonly approached through three main methods. (1) Variational inference methods aim to approximate the intractable posterior by minimizing divergence to a simpler, tractable distribution (Blundell et al., 2015; Kingma and Welling, 2013; Gal and Ghahramani, 2016; Louizos and Welling, 2017; Zhang et al., 2018). A well-known example is Monte Carlo Dropout (Gal and Ghahramani, 2016), which interprets dropout as a Bernoulli-distributed random variable and enables efficient posterior sampling at inference time. (2) Sampling-based approaches typically rely on Markov Chain Monte Carlo (MCMC) methods (Neal, 2012; Welling and Teh, 2011; Chen et al., 2016), which iteratively generate samples that approximate the posterior distribution, providing asymptotically exact inference. (3) Laplace approximation methods simplify the posterior by performing a second-order Taylor expansion around the mode of the log-posterior (MacKay, 1992; Osawa et al., 2019; Dusenberry et al., 2020; Ritter et al., 2018). Recognizing that many eigenvalues of the Hessian are near zero, Ritter et al. (2018) propose a low-rank approximation that yields efficient and scalable posterior covariance estimation, enabling the application of Laplace methods to large-scale models. Notable techniques include R-BNN (Reparameterisation) (Kingma et al., 2015), variational inference with reparameterisation and Laplace Bridge Bayesian approximation (LB-BNN) (Hobbhahn et al., 2022), which uses the Laplace Bridge to map between Gaussian and Dirichlet distributions. Various approximations of full Bayesian inference exist, such as Markov chain Monte Carlo (MCMC) (Neal, 1992; Geman and Geman, 1984), variational inference (VI) (Graves, 2011), function-space BNNs (Sun et al., 2019) such as function-space variational inference (FSVI) (Rudner et al., 2022), and Dropout Variational Inference (Gal and Ghahramani, 2015). In our experiments, we do not consider older Bayesian models such as R-BNN, MCMC and Dropout VI, since they have been superseded by higher performing approaches and are computationally expensive to train on larger datasets and architectures.

Despite the development of efficient training techniques such as variational inference (Blundell et al., 2015; Gal and Ghahramani, 2016; Kingma et al., 2015; Gal and Ghahramani, 2015; Sun et al., 2019; Rudner et al., 2022; Gal and Ghahramani, 2015), Laplace approximations (Daxberger et al., 2021; Osawa et al., 2019; Dusenberry et al., 2020) and sampling methods (Hoffman et al., 2014; Neal et al., 2011) and achieving some success in real-world tasks (Vega and Todd, 2022; Kwon et al., 2020), practical challenges remain. This includes the significant computational complexity associated with training and inference (Jospin et al., 2022), establishing appropriate prior distributions before training (Fortuin, 2022), handling complex network architectures, and ensuring real-time applicability. Furthermore, several studies have indicated that the use of single probability distributions to model the lack of knowledge is insufficient (Caprio et al., 2023b). This is further discussed in this thesis in Sec. 4.2. Recent work addresses challenges in computational cost (Hobbhahn et al., 2022; Daxberger et al., 2021) and model priors (Tran

<!-- page: 41 -->

18                                                              Chapter 3. Related Work: Machine Learning Models For Representing Uncertainty

et al., 2020). However, Bayesian models will always face challenges when the model prior is misspecified.

Bayesian Neural Networks (BNNs) (Lampinen and Vehtari, 2001; Titterington, 2004; Goan and Fookes, 2020; Hobbhahn et al., 2022) compute a predictive distribution \(\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})\) by integrating over a learnt posterior distribution of model parameters \(\theta\) given training data \(\mathbb{D}\). This is often infeasible due to the complexity of the posterior, leading to the use of *Bayesian Model Averaging* (BMA), which approximates the predictive distribution by averaging over predictions from multiple samples. When applied to classification, BMA yields point-wise predictions.

Bayesian inference integrates over the posterior distribution \(p(\theta \mid \mathbb{D})\) over model parameters \(\theta\) given training data \(\mathbb{D}\) to compute the predictive distribution \(\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})\), reflecting updated beliefs after observing the data:

$$
\hat{p}_b(y \mid \mathbf{x}, \mathbb{D}) = \int p(y \mid \mathbf{x}, \theta) p(\theta \mid \mathbb{D}) d\theta,
$$
(3.2)

where \(p(y \mid \mathbf{x}, \theta)\) represents the likelihood function of observing label \(y\) given \(x\) and \(\theta\). To overcome the infeasibility of this integral, direct sampling from \(\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})\) using methods such as Monte-Carlo (Hastings, 1970) are applied to obtain a large set of sample weight vectors, \(\{\theta_k, k\}\), from the posterior distribution. These sample weight vectors are then used to compute a set of possible outputs \(y_k\), namely:

$$
\hat{p}_b(y_k \mid \mathbf{x}, \mathbb{D}) = \frac{1}{|\Theta|} \sum_{\theta_k \in \Theta} \Phi_{\theta_k}(\mathbf{x}),
$$
(3.3)

where \(\Theta\) is the set of sampled weights, \(\Phi_{\theta_k}(\mathbf{x})\) is the prediction made by the model with weights \(\theta_k\) for input \(\mathbf{x}\), and \(\Phi\) is the function for the model. This process is called *Bayesian Model Averaging (BMA)*.

Fig. 3.2 illustrate key limitations of Bayesian model averaging (BMA). In Fig. 3.2 (*top*), the true class is ‘airplane’, but most posterior samples assign high probability mass to the ‘automobile’ class. Although one sample assigns a non-negligible probability (≈ 0.34) to ‘airplane’, the majority vote across samples overwhelms this minority, and the BMA prediction incorrectly favors automobile with final averaged probability. This highlights how averaging may suppress informative outlier samples. In Fig. 3.2 (*bottom*), the true class is ‘automobile’, and the posterior samples are more mixed: ‘truck’ receives the highest number of samples, but automobile is a close second. However, the averaging process again results in the incorrect prediction (‘truck’) despite there being substantial support for the correct class. This can limit a BNN's ability to accurately represent complex uncertainty patterns, potentially undermining its effectiveness in scenarios requiring reliable uncertainty quantification. BMA may inadvertently smooth out predictive distributions, diluting the inherent uncertainty present in individual models (Hinne et al., 2020; Graefe et al., 2015) as shown in Fig. 3.2. When applied to classification, BMA yields point-wise predictions. For fair comparison and to overcome BMA's limitations, in Chapter 8 of this thesis, we use sets of prediction samples obtained from the different posterior weights before averaging. This method of analyzing individual prediction samples before averaging appears to be relatively underexplored.

In BNNs, *predictive uncertainty* is measured by the predictive entropy of the model's output distribution, which captures the total uncertainty in predictions. Epistemic uncertainty is

<!-- page: 42 -->

3.2. Bayesian Methods                                                                          19

[FIGURE: Figure 3.2. Visualizations of 100 prediction samples obtained prior to Bayesian Model Averaging and corresponding Bayesian Model Averaged prediction in two real scenarios from CIFAR-10.]

Text in figure:

(top-left) "100 Bayesian Prediction Samples (True Class: airplane)" — scatter plot, x-axis "Number of samples", y-axis "Prediction Probability"; legend: automobile, ship, truck, airplane.
(top-right) "Bayesian Model Averaged Prediction (True Class: airplane)" — single averaged point; legend: automobile.
(bottom-left) "100 Bayesian Prediction Samples (True Class: automobile)" — scatter plot, x-axis "Number of samples", y-axis "Prediction Probability"; legend: automobile, truck.
(bottom-right) "Bayesian Model Averaged Prediction (True Class: automobile)" — single averaged point; legend: truck.

Figure 3.2: Visualizations of 100 prediction samples obtained prior to Bayesian Model Averaging and corresponding Bayesian Model Averaged prediction in two real scenarios from CIFAR-10.

sometimes represented using the mutual information (MI) between the model predictions and the model parameters (Hüllermeier and Waegeman, 2021; Hüllermeier et al., 2022). MI measures the reduction in uncertainty about the model parameters after observing the prediction and can be interpreted as the difference between the entropy of the predictive distribution and the expected entropy of the individual predictive samples. Despite its theoretical appeal, MI as an epistemic uncertainty measure is not always directly comparable with epistemic uncertainty estimates produced by other methods, such as deep ensembles or other non-Bayesian approaches. This is because different methods define and approximate epistemic uncertainty in different ways, leading to variations in scale and interpretation. Consequently, in this thesis, it is also challenging to directly compare the epistemic uncertainty measures we employ with those based on mutual information.

The predictive entropy can be calculated as:

$$
H(\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})) = -\int \hat{p}_b(y \mid \mathbf{x}, \mathbb{D}) \log \hat{p}_b(y \mid \mathbf{x}, \mathbb{D}) dy,
$$
(3.4)

where \(\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})\) is the predictive distribution and \(H(\cdot)\) denotes the Shannon entropy function. This equation represents the average uncertainty associated with the predictions across different possible values of \(y\), considering the variability introduced by the parameter uncertainty captured in the posterior distribution \(p(\theta \mid \mathbb{D})\).

<!-- page: 43 -->

20                                                              Chapter 3. Related Work: Machine Learning Models For Representing Uncertainty

## 3.3 Ensemble Methods

Ensemble methods such as Deep Ensembles (DE) (Lakshminarayanan et al., 2017), Epistemic Neural Networks (ENN) (Osband et al., 2024) and several other studies (Pearce et al., 2020; Wen et al., 2020; Beluch et al., 2018) quantify prediction uncertainty by leveraging the prediction of multiple models (*e.g.*, multiple deep networks). Thus, they represent uncertainty by aggregating a limited set of point estimates while averaging a set of single probability distributions as predictions. Deep ensembles serve as one of the top methods in literature for estimating predictive uncertainty (Ovadia et al., 2019; Gustafsson et al., 2020; Abe et al., 2022), however, they have been criticized because of their lack of robust theoretical foundations and their demand for substantial memory resources. Computational cost of training ensembles, especially for large models, is often impractical (Liu et al., 2020; Ciosek et al., 2019; He et al., 2020).

In Deep Ensembles (DEs) (Lakshminarayanan et al., 2017), a prediction \(\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D})\) for an input \(\mathbf{x}\) is obtained by averaging the predictions of \(K\) individual models:

$$
\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D}) = \frac{1}{K} \sum_{k=1}^{K} \hat{p}_{de}(y_k \mid \mathbf{x}, \mathbb{D}),
$$
(3.5)

where \(\hat{p}_k\) represents the prediction of the \(k\)-th model, trained independently with different initialisations or architectures.

In Deep Ensembles, predictive uncertainty is assessed via the predictive entropy, averaged entropy of each ensemble's prediction, while epistemic uncertainty is encoded by the predictive variance, the difference between the entropy of all ensembles and the averaged entropy of each ensemble.

Let \(\mathcal{M} = \{M_1, M_2, \ldots, M_K\}\) denote the ensemble of \(K\) neural network models for \(k = 1, 2, \ldots, K\). Given an input \(\mathbf{x}\), the prediction \(y_{\mathcal{M}}\) is obtained by averaging the predictions of individual models. The *predictive entropy* represents the entropy of the averaged prediction given the input \(\mathbf{x}\) and the observed data \(\mathbb{D}\):

$$
H(\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D})) = H\!\left(\frac{1}{K} \sum_{k=1}^{K} \hat{p}_{de}(y_k \mid \mathbf{x}, \mathbb{D})\right),
$$
(3.6)

where \(y_k\) represents the prediction of the \(k\)-th model \(M_k\).

The *predictive variance* is measured as the difference between the entropy of all the ensembles, \(H(\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D}))\), and the averaged entropy of each ensemble.

$$
H(y_{\mathcal{M}}) = H(\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D})) - \frac{1}{K} \sum_{k=1}^{K} H(\hat{p}_{de}(y_k \mid \mathbf{x}, \mathbb{D})).
$$
(3.7)

The predictive variance in DEs is considered an approximation of mutual information (Hüllermeier and Waegeman, 2021). This formulation captures both the model uncertainty inherent in the ensemble predictions and the uncertainty due to the variance among individual model predictions.

<!-- page: 44 -->

3.4. Evidential Methods                                                                          21

## 3.4 Evidential Methods

Evidential Deep Learning (EDL) models represent predictions as Dirichlet distributions, as explored in various works over the last few years (Sensoy et al., 2018; Malinin and Gales, 2018; 2019; Malinin et al., 2019; Charpentier et al., 2020). A significant amount of work in the evidential framework (Xu et al., 1992) has focused on neural networks (Rogova, 2008), decision trees (Elouedi et al., Madrid, 2000), K-nearest neighbour classifiers (Denœux, 2008), and more recently, evidential deep learning classifiers able to quantify uncertainty (Tong et al., 2021). Notably, Sensoy et al. (2018) introduced a classifier estimating second-order uncertainty in the Dirichlet representation by forming subjective opinions.

Evidential Deep Learning (EDL) methods and Prior Networks (Malinin and Gales, 2018) both leverage the Dirichlet distribution to model uncertainty, but differ in focus (Ulmer et al., 2023). The Dirichlet, as a conjugate prior to the categorical distribution, allows both methods to maintain Dirichlet-form outputs. Prior Networks (Malinin and Gales, 2018) parameterize the Dirichlet prior directly to model uncertainty before observing data, whereas EDL (Sensoy et al., 2018) infers the posterior Dirichlet by interpreting network outputs as class evidence under subjective logic (Jøsang, 2016). Thus, EDL can be viewed as a type of posterior network that learns uncertainty from data, capturing both aleatoric and epistemic uncertainty through evidence accumulation.

However, many commonly used loss functions for these networks are flawed, as they fail to ensure that epistemic uncertainty diminishes with more data, violating basic asymptotic assumptions (Bengs et al., 2022). Additionally, some approaches require out-of-distribution (OoD) data for training, which may not always be available and doesn't guarantee robustness against all types of OoD data. Studies (Ulmer et al., 2023) have shown that OoD detection degrades in certain models under adversarial conditions, and even techniques like normalizing flows (NFs) in posterior networks (Charpentier et al., 2020), while effective, can struggle with OoD data when relying on learned features (Kopetzki et al., 2021; Stadler et al., 2021).

Evidential models (Sensoy et al., 2018) make predictions \(\hat{p}_e(y \mid \mathbf{x}, \mathbb{D})\) as parameters of a second-order Dirichlet distribution on the class space, instead of softmax probabilities. EDL uses these parameters to obtain a pointwise prediction. Similar to BNNs, averaged DE and EDL predictions are point-wise predictions and averaging may not always be optimal.

## 3.5 Conformal Prediction

Conformal prediction (Vovk et al., 2005) provides a framework for estimating uncertainty (Shafer and Vovk, 2008) by applying a threshold on the error the model can make to produce prediction sets, irrespective of the underlying prediction problem. Different variants of conformal predictors are described in papers by Saunders et al. (1999), Nouretdinov et al. (2001), Proedrou et al. (2002) and Papadopoulos et al. (2008). It is a wrapper method applicable to any model, generating prediction sets (for accuracy guarantees) by computing empirical cumulative distributions and applying hypothesis testing to them. Several variants exist (*e.g.*, conditional, full conformal prediction) (Papadopoulos et al., 2002a; 2008; 2002b; Saunders et al., 1999; Nouretdinov et al., 2001; Vovk et al., 2003; Vovk, 2012; Vovk and Petej, 2012; Campos et al., 2024). Since the computational inefficiency of conformal predictors posed a problem for their use in neural networks, Inductive Conformal Predictors (ICPs) were proposed by Papadopoulos et al. (2002b).

<!-- page: 45 -->

22                                                              Chapter 3. Related Work: Machine Learning Models For Representing Uncertainty

Venn Predictors (Vovk et al., 2003), cross-conformal predictors (Vovk, 2012) and Venn-Abers predictors (Vovk and Petej, 2012) were introduced in distribution-free uncertainty quantification using conformal learning.

Conformal predictors primarily capture aleatoric uncertainty in a frequentist framework by guaranteeing marginal coverage under the assumption of data exchangeability (Vovk et al., 2005). While coverage is formally guaranteed regardless of model misspecification, the efficiency of the prediction sets (i.e., their width) depends heavily on the quality of the underlying model. Moreover, under distributional shift, conformal methods may fail to maintain valid coverage unless explicitly extended to handle epistemic uncertainty (Bates et al., 2023). Standard CP methods rely on calibration via a held-out set and do not model uncertainty about the model itself. *i.e.*, they assume the underlying model is fixed and reasonably accurate. In addition to this, since conformal prediction is a wrapper method applicable on top of any underlying model, it is not directly compared with any of the uncertainty quantification methods described in this thesis (including the related methods in this section). Instead, it can be combined with any of these methods, including the model proposed in this thesis. As demonstrated in §B, the model introduced in Chapter 5 is compatible with conformal prediction and can serve as its underlying predictive model.

## 3.6 Imprecise Models

Imprecise Probability (IP) theory models uncertainty using sets of probability distributions (*e.g.*, credal sets, random sets, *etc.*) rather than single distributions, explicitly capturing epistemic uncertainty (Levi, 1980; Hüllermeier and Waegeman, 2021). Walley (1996) introduced the imprecise Dirichlet model, which uses a set of Dirichlet priors to model prior ignorance; as a result, the predictive probabilities become intervals. Credal inference, including models such as the Naive Credal Classifier (NCC) (Corani and Zaffalon, 2008; Zaffalon, 2002; Corani and Zaffalon, 2008) and credal random forests (Shaker and Hüllermeier, 2021), provides a principled way to quantify epistemic uncertainty by predicting convex sets of probability distributions (Corani et al., 2012). The NCC, extending naive Bayes classifiers by outputting sets of classes rather than single predictions, offers robustness especially when data are scarce or incomplete (Corani and Zaffalon, 2008; Zaffalon, 2002; Corani and Zaffalon, 2008). Extensions to multilabel problems and credal networks have further generalized this approach (Antonucci and Corani, 2017; Corani et al., 2012).

Random sets provide a natural framework for modeling missing data (Cuzzolin, 2020), while belief function models, rooted in the foundational work of Dempster (Dempster, 1967) and Shafer (Shafer, 1976), have been widely applied in machine learning tasks such as ensemble classification (Liu et al., 2019; Xu et al., 1992; Rogova, 2008), regression (Gong and Cuzzolin, 2017; Laanaya et al., 2010; Gong and Cuzzolin, 2017; Denœux, 2022), and generalized max-entropy classification (Cuzzolin, 2018a). These models facilitate the representation of uncertainty through transferable belief models and convex sets, combining aleatoric and epistemic components within a unified mathematical framework (Cuzzolin, 2010a). Significant contributions have been made by Denoeux and co-authors (Denœux, 2008; Denoeux, 2000) on belief function-based unsupervised learning and clustering (ga Liu et al., 2012), and on ensemble classification, including methods based on neural networks (Rogova, 2008), decision trees (Elouedi et al., Madrid, 2000), and K-nearest neighbor classifiers (Denœux, 2008).

<!-- page: 46 -->

3.6. Imprecise models                                                                            23

Research on the use of deterministic intervals in neural networks to represent and quantify uncertainty, known as interval neural networks (INNs), focuses primarily on regression tasks. One line of INN research (Khosravi et al., 2011; Pearce et al., 2018; S. Salem et al., 2020; Lai et al., 2022) emphasizes generating deterministic interval predictions while keeping the network weights and biases fixed at point estimates. To account for epistemic uncertainty, some researchers, *e.g.*, (Pearce et al., 2018; S. Salem et al., 2020; Lai et al., 2022) have proposed using ensembles of INNs. For example, the variances of the upper and lower prediction bounds across ensemble INN members can be calculated to quantify the EU associated with each prediction bound (Pearce et al., 2018). Unlike traditional INNs that only represent predictions as intervals, an alternative approach models both network weights and biases as intervals (Ishibuchi et al., 1993; Garczarczyk, 2000; Oala et al., 2021; Betancourt and Muhanna, 2022; Tretiak et al., 2023; Cao et al., 2024). This design allows the INN to capture both aleatoric and epistemic uncertainty within an interval framework. A further advantage of these models is their capacity to handle interval-valued input data.

A limited number of studies have explored the use of INNs for classification tasks, primarily due to the practical challenges discussed earlier in the introduction. For example, (Kowalski and Kulczycki, 2017) extended the probabilistic neural network framework by incorporating interval representations to enhance robustness.

Expected utility maximization methods, such as Bayes-optimal prediction (Mortier et al., 2021) and classification with reject options for risk-averse decision-making (Nguyen et al., 2018), extend credal and belief frameworks to support decision-theoretic applications. These approaches enable partial or set-valued classification outputs that improve robustness by avoiding overconfident or risky predictions. Practical heuristics often classify all classes whose lower probabilities exceed a threshold, producing ‘safe’ classifications that balance risk and informativeness (Corani and Zaffalon, 2008; Zaffalon, 2002). This flexibility outperforms rigid single-label decisions or naive reject options, especially in uncertain or low-data regimes.

Classification with partial data has been studied by various authors (Vannoorenberghe and Smets, 2005), while a large number of papers have been published on decision trees in the belief function framework (Elouedi1 et al., 2000). Significant work in the neural network area was conducted in (Denoeux, 2000) and (Fay et al., 2006). Classification approaches based on rough sets were proposed in (Trabelsi et al., 2011). Ensemble classification (Burger et al., 2006) is another area in which uncertainty theory has been quite impactful, as the problem is one of combining the results of different classifiers. Important contributions have been made by (Xu et al., 1992) and (Rogova, 2008). Regression, on the other hand, has only recently been considered by belief theorists (Laanaya et al., 2010; Gong and Cuzzolin, 2017; Denœux, 2022). For tasks like image classification in large datasets, most of these approaches have low performance metrics including training time and test accuracy.

Recent progress in deep learning has integrated IP frameworks to enhance uncertainty quantification. For instance, Credal Bayesian Deep Learning (Credal-BDL) trains Bayesian neural networks with finitely generated credal sets of priors and likelihoods, yielding sets of posterior distributions that separate aleatoric from epistemic uncertainty and improve robustness against prior misspecification and distribution shifts (Caprio et al., 2023a). Similarly, Credal Wrappers construct convex hulls over ensemble model outputs to provide interval-valued class probabilities, enhancing calibration and out-of-distribution detection on benchmarks such as CIFAR-10

<!-- page: 47 -->

24                                                              Chapter 3. Related Work: Machine Learning Models For Representing Uncertainty

and ImageNet (Wang et al., 2024a). Methods optimizing interval-valued losses or leveraging conformal prediction with imprecise probabilities produce set-valued predictions with rigorous coverage guarantees, addressing ambiguous or partially labeled data common in medical and human-annotated vision datasets (Javanmardi et al., 2024). More recent advancements leverage Dempster–Shafer theory and subjective logic to quantify second-order uncertainty, enabling set-valued predictions that incorporate utility functions from decision theory (Tong et al., 2021).

## 3.7 Discussion On Existing Methods and Motivating This Thesis

As mentioned above, despite their popularity, many uncertainty quantification methods suffer from significant limitations. Deep Deterministic Uncertainty (DDU) relies on feature-space distances, which are only as good as the learned embeddings and often degrade in high dimensions, limiting their reliability (Postels et al., 2021). Moreover, DDU often lacks proper calibration and fail in out-of-distribution (OoD) detection. Bayesian Neural Networks (BNNs) offer principled uncertainty estimates but face **high computational costs**, complex training procedures, and sensitivity to prior choices (Jospin et al., 2022; Fortuin, 2022). Deep Ensembles are empirically strong (Lakshminarayanan et al., 2017), but **scale poorly**, with training and inference costs increasing linearly with the number of ensemble members (Ovadia et al., 2019; Gustafsson et al., 2020). They also rely on sufficient model diversity, without which their uncertainty estimates can become unreliable (Ciosek et al., 2019).

Evidential methods, which model second-order uncertainties using Dirichlet distributions, often **fail to reduce epistemic uncertainty with more data**, violating a core assumption of learning under uncertainty (Bengs et al., 2022). These models are also **sensitive to training loss formulations and regularization** choices, and some require access to OoD data during training, which is something not always available in practice (Ulmer et al., 2023). Conformal prediction, while providing **distribution-free prediction sets with guaranteed coverage**, fundamentally captures **aleatoric rather than epistemic uncertainty** since it relies on building cumulative distribution functions of ‘nonconformity scores’ to which it applies classical hypothesis testing (Bates et al., 2023). It also assumes data exchangeability, and when this assumption is violated, **coverage guarantees break down**. Together, these limitations highlight the need for approaches that are both **computationally tractable** and capable of expressing **epistemic uncertainty in a faithful and comparable manner** across different models.

While Bayesian neural networks do claim to offer a principled second-order treatment by maintaining distributions over parameters, they suffer from high computational costs, prior sensitivity, and scalability issues in real-world applications. Crucially, they also face conceptual shortcomings in modeling ignorance, detailed further in Sec. 4.2. Deep ensembles and evidential methods often approximate second-order reasoning, but do so heuristically or unreliably, relying on architectural diversity or uncertain loss formulations, which makes them sensitive and difficult to generalize. Together, these limitations suggest that while many existing methods capture aspects of uncertainty, they struggle to represent epistemic ignorance robustly, motivating the need for more expressive alternatives (Sec. 4.3.1).

Some critics, including this thesis, argue that classical probability theory cannot fully address ‘second-level’ uncertainty (Hüllermeier and Waegeman, 2021), suggesting the use of more generalized frameworks (Sec. 4.3.1), such as possibility theory (Dubois and Prade, 1990), probability intervals (Halpern, 2017), credal sets (Levi, 1980) or imprecise probabilities (Walley, 1991) (Sec.

<!-- page: 48 -->

3.7. Discussion on existing methods and motivating this thesis                                  25

3.6). This thesis presents imprecise models based on random sets, belief functions, and credal sets, motivated by the fact that these frameworks offer substantial unexplored potential. It demonstrates that significant performance improvements can be achieved without necessarily leveraging the full expressive power of second-order uncertainty measures (see Sec. 5.2.2). Instead, scalability can be effectively addressed by designing model structures that are sufficiently expressive to capture key aspects of second-order uncertainty, while remaining computationally tractable.

**The way epistemic uncertainty is managed and data is leveraged is a defining issue for AI. This thesis contributes to the debate by advocating a paradigm shift towards an *Epistemic Artificial Intelligence* in the next part (Chapter 4, Part II) that explicitly emphasizes learning under ignorance through the use of second-order uncertainty measures (Chapter 4.3, Part II).**

<!-- page: 49 -->

26

# Part II

# EPISTEMIC DEEP LEARNING

<!-- page: 50 -->

<!-- page: 51 -->

28

# 4 Epistemic Artificial Intelligence

As discussed in Chapter 3.7, existing models struggle to capture epistemic uncertainty faithfully, largely because a single probability distribution cannot adequately express ignorance about the data-generating process (Cuzzolin, 2020). Addressing this limitation requires moving beyond classical probabilistic frameworks and embracing richer, *second-order uncertainty measures* (Sec. 4.3.1), mathematical formalisms designed to explicitly represent and reason under partial knowledge.

This chapter introduces the paradigm of *epistemic artificial intelligence*, in which models are designed to reason not only from what they know but also from what they do not know. By explicitly recognizing and managing uncertainty, epistemic AI aims to enhance the resilience and robustness of AI systems, enabling them to perform more reliably in unpredictable real-world environments. Building on this foundation, this thesis presents a novel approach (Chapter 5) to effectively model, learn, and act under such uncertainty.

## 4.1 Concept

[FIGURE: Figure 4.1. Epistemic Learning.]

Text in figure:

Left: Probabilistic prediction ← Simplex of distributions over target or parameter space ← Learning ← Model (in Model space) ← Training set / Datum
Right: Epistemic prediction (e.g. a credal set) ← Epistemic Learning ← Epistemic model (second-order uncertainty) ← Datum

Figure 4.1: **Epistemic Learning.** Contrary to a traditional learning process in which a single model is learned from a training set to map new data to predictions, in the form of a probability distribution over the target space (left), epistemic learning outputs a second-order uncertainty measure (right).

**Epistemic AI rests on the ‘paradoxical’ principle that one should first and foremost learn from (or be ready for) the data it cannot see.** Prior to observing any data, the task at hand is thus completely unknown (albeit prior knowledge can be utilized to formalize the task and set a model space of solutions). The (limited) available evidence should only be used to temper our ignorance, to avoid ‘catastrophically forgetting’ how much we ignore about the problem. The problem can be formalized as one of learning a mapping (epistemic model) from input data points to predictions in the form of an uncertainty measure (*e.g.* a credal set), either on the target space or on the parameter space of the model itself (Fig. 4.1). Later, this prediction may be updated in the light of new data. For comparison with other models, a probability-like estimate called the pignistic probability (Smets, 2005) can be computed as the center of mass of the credal set (see Fig. 3.1).

<!-- page: 52 -->

4.2. Why Epistemic AI is Essential                                                                29

## 4.2 Why Epistemic AI Is Essential

In addition to the limitations discussed in Chapter 3, existing models fundamentally struggle to capture epistemic uncertainty. Bayesian methods, though widely used, falter particularly in data-sparse or ambiguous settings because they must assign fixed belief mass even when knowledge is lacking. Uninformative priors such as Jeffreys' (Jeffreys, 1998) are not invariant under reparameterization and can be improper, violating objectivity and the strong likelihood principle (Shafer, 1984). Moreover, priors must be specified even for systems without past data, leading to arbitrary modeling choices that can **bias the learning process for a long time** (Bernstein-von Mises theorem (Kleijn and Van der Vaart, 2012)). Bayesian **posteriors may appear similar whether we have no knowledge or weak evidence**, conflating ignorance with imprecise belief and potentially causing misleading overconfidence. For example, if we are predicting the probability of a number in a roulette, Bayesian inference treats the uncertainty in the wheel's bias as part of a single posterior, rather than explicitly representing how much we lack knowledge about the underlying bias.

Model selection and prior choice lack objective criteria and **prior sensitivity worsens with scarce data** (Kass and Wasserman, 1996; Berger, 2013). Further, Bayesian models **cannot naturally represent set-valued or propositional evidence**, because the additivity of probability forces allocation to individual outcomes, even when evidence supports sets of hypotheses, in contrast to random-sets which can naturally model missing data (Cuzzolin, 2020). Bayes' rule also **assumes that new evidence is sharp and definitive**, which is unrealistic in many real-world cases. Hierarchical Bayesian models, which place priors over priors, can model epistemic uncertainty and potentially address some of these issues, but are very computationally expensive in high-dimensional or open-world settings.

Moreover, Bayesian inference tends to smooth out epistemic uncertainty by averaging over models, collapsing diverse possibilities into a single estimate and failing to distinguish knowns from unknowns (Hinne et al., 2020; Graefe et al., 2015; Hüllermeier and Waegeman, 2021). Computationally, Bayesian models also often suffer from slow convergence and large inference times (Tab. 11.1), limiting their suitability for real-time safety-critical systems like autonomous vehicles (Jospin et al., 2022).

> Epistemic AI advocates for the use of second-order uncertainty measures, such as probability intervals, credal sets (Levi, 1980; Cuzzolin, 2008a) or random-sets, as they generalize classical probability using set-based representations and can richly encapsulate imprecision to model the epistemic uncertainty about an underlying, shifting data distribution, possibly the central challenge in machine learning.

Indeed, most second-order measures contain classical probability as a special case (Cuzzolin, 2024), with random-set reasoning subsuming Bayesian reasoning as a special case (Shafer, 1978). The relationship between Bayesian inference and other mathematical frameworks for uncertainty is discussed in several works (Cuzzolin, 2020; 2007; July 2011; 2009), also using the language of geometry (Cuzzolin and Frezza, 2001; Cuzzolin, 2008b; 2003; 2004b;a; 2010c; 2013; 2010c).

<!-- page: 53 -->

30                                                                 Chapter 4. Epistemic Artificial Intelligence

## 4.3 Modeling A Lack Of Knowledge

The following chapter lays the theoretical foundation by providing an overview of these alternative uncertainty frameworks, including random sets (Sec. 4.3.1.1), belief functions (Sec. 4.3.1.2), and credal sets (Sec. 4.3.1.3). These frameworks underpin the models developed throughout this thesis, offering the expressive capacity needed to reason under ignorance. Together, they support the paradigm shift toward Epistemic Artificial Intelligence discussed in Chapter 4.

### 4.3.1 Theories of Uncertainty: Beyond Bayesian Probabilities

[FIGURE: Figure 4.2. Clusters of uncertainty theories.]

Text in figure (cluster labels and their member nodes, arranged as overlapping regions with arrows indicating generality):

- Generalised Bayesian reasoning: Interpretation functions, Propensity / Harper's, Jeffrey's rule
- Robust probability: Lower/upper probabilities, Probability intervals, Feasible probability intervals, 2-monotone capacities
- Behavioural probability: P-boxes, De Finetti's previsions, Vovk-Shafer, Lower/upper previsions
- Generalised sets: Rough sets, Fuzzy sets / Possibility, Granular computing, Zadeh's GTU
- (center) Probability; Credal sets; Belief functions; Random sets; Liu's UT; Capacities
- Higher-order probabilities: Probability on fuzzy sets, Dirichlet, Meta-probability, Belief functions on fuzzy sets
- Measures on functions: MV-algebras
- Generalised measures on events

Figure 4.2: **Clusters of uncertainty theories.** Uncertainty theories can be arranged into various clusters based on the objects they quantify and their rationale. Arrows indicate the level of generality, with more general theories encompassing less general ones. Note that the quality and rigour of different approaches can vary significantly.

Uncertainty theory (UT), an array of theories devised to encode ‘second-order’, ‘epistemic’ uncertainty, *i.e.*, uncertainty about what probabilistic process actually generates the data, can provide a principled solution to this conundrum (Augustin et al., 2014; Walley, 1991). This is the situation ML is in, for we usually ignore the form of the data-generating process at hand, even accepting that it should be modelled by a probability distribution. Many (but not all) uncertainty measures amount to convex sets of distributions or ‘credal sets’ (*e.g.*, p-boxes) (Troffaes, 2007), while random sets and belief functions directly assign probability values to sets

<!-- page: 54 -->

4.3. Modeling A Lack Of Knowledge                                                                     31

of outcomes (Shafer, 1976), modelling the fact that observations often come in the form of sets. The paramount principle in UT is to refine continually one's degree of uncertainty (measured, *e.g.*, by how wide a convex set of models is) in the light of new evidence. All uncertainty theories are equipped with operators (playing the role of Bayes' rule in classical probability) allowing one to reason with such measures (*e.g.* Dempster's combination for belief functions) (Dempster, 2008; Smets and Kennes, 1994).

The various theories of uncertainty form ‘clusters’ characterized by a common rationale (Cuzzolin, 2020) (see Fig. 4.2). A first set of methods can be seen as ways of ‘robustifying’ classical probability: The most general such approach is Walley's theory of imprecise probability (Walley, 1991), a behavioral approach whose roots can be found in the ground-breaking work of de Finetti (de Finetti, 1974). In behavioral probability, the latter is a measure of an agent's propensity to gamble on the uncertain outcomes. A different cluster of approaches hinges on generalizing the very notion of set: these include, for instance, the theory of rough sets (Pawlak, 1982), possibility theory (Dubois and Prade, 2012), and Dempster-Shafer theory (Shafer, 1976). More general still are frameworks generalizing measure theory, *e.g.* the theory of monotone capacities or ‘fuzzy measures’ (Grabisch et al., 2000). Some proposals (including Popper's propensity) aim at generalizing Bayesian reasoning (Popper, 1959) in terms of either the measures used or the inference mechanisms. The theory of set-valued random variable or ‘random sets’ extends the notion of set (Molchanov, 2017) and generalizes Bayesian reasoning. Frameworks which completely replace events by scoring functions (Vovk et al., 2005) in a functional space form arguably the most general class of methods. The diagram also illustrates the relationships between different theories, indicating which are more general and which are more specific. An arrow from formalism 1 to formalism 2 suggests that the former is a less general case of the latter.

#### 4.3.1.1 Random Sets

[FIGURE: Figure 4.3. The random set associated with a cloaked die in which faces 1 and 2 are not visible.]

Text in figure:

Ω (sample space) with elements: face 1, face 2, face 3, face 4, face 5, face 6, mapped via X to ℝ (real line marked 1 2 3 4 5 6). Faces 1 and 2 are enclosed together, mapping jointly to the set {1, 2}. A die illustration is shown at the right.

Figure 4.3: The random set associated with a cloaked die in which faces 1 and 2 are not visible.

A die is a simple example of a (discrete) random variable. Its probability space is defined on the sample space \(\Theta = \{\text{face} 1, \text{face } 2, \ldots, \text{face } 6\}\), where elements are mapped to the real numbers \(1, 2, \ldots, 6\), respectively. Now, imagine that faces 1 and 2 are cloaked, and we roll the die. How do we model this new experiment, mathematically? Actually, the probability space has not changed (as the physical die has not been altered, its faces still have the same probabilities). What has changed is the mapping: since we cannot observe the outcome when a cloaked face is shown (assuming that only the top face is observable), both face 1 and face 2 (as elements of sample space \(\Theta\)) are mapped to the set of possible values \(\{1, 2\}\) on the real line \(\mathbb{R}\) (Fig. 4.3). Mathematically, this is a *random set* (Matheron, 1975; Kendall, 1974; Nguyen, 1978;

<!-- page: 55 -->

32                                                     Chapter 4. Epistemic Artificial Intelligence

Molchanov, 2005), *i.e.*, a set-valued random variable, modelling random experiments in which observations come in the form of sets. Random sets (Matheron, 1975; Kendall, 1974; Nguyen, 1978; Molchanov, 2005) are *non-additive* measures (*i.e.*, the additivity property does not hold). Their additional degrees of freedom allow to express the ‘epistemic’ uncertainty about probability values themselves.

#### 4.3.1.2 Belief Functions

Random sets have been proposed by Dempster (2008) and Shafer (1976) as a mathematical model for subjective belief, alternative to Bayesian reasoning. Thus, on finite domains (*e.g.*, for classification) they assume the name of *belief functions*. While classical discrete mass functions assign normalised, non-negative values to elements \(\theta \in \Theta\) of their sample space, a belief function independently assigns normalised, non-negative mass values to its subsets \(A \subset \Theta\):

$$
m(A) \geq 0, \quad \sum_{A} m(A) = 1, \quad \forall A \subset \Theta
$$
(4.1)

The belief function associated with a mass function \(m\) measures the total mass of the subsets of each ‘focal set’ \(A\). Mass functions can be recovered from belief functions via Moebius inversion (Shafer, 1976), which, in combinatorics, plays a role similar to that of the derivative:

$$
Bel(A) = \sum_{B \subseteq A} m(B), \quad m(A) = \sum_{B \subseteq A} (-1)^{|A \setminus B|} Bel(B).
$$
(4.2)

**Pignistic probability.** Given a belief function \(Bel\), its pignistic probability is the precise probability distribution obtained by re-distributing the mass of its focal sets \(A\) to its constituent elements, \(\theta \in A\):

$$
BetP(\theta) = \sum_{A \ni \theta} \frac{m(A)}{|A|}.
$$
(4.3)

Smets (2005) originally proposed to use the pignistic probability for decision making using belief functions, by applying expected utility to it. Notably, the pignistic probability is geometrically the centre of mass of the credal set (see Fig. 4.4) associated with a belief function (Cuzzolin, 2018b).

**Obtaining a credal prediction from belief functions.** A belief function is also associated with a convex set of probability distributions, a credal set (Sec. 4.3.1.3) (Levi, 1980; Zaffalon and Fagiuoli, 2003; Cuzzolin, 2010b; Antonucci and Cuzzolin, 2010; Cuzzolin, 2008a), on the same domain. This is the set:

$$
Cre = \{P : \Theta \to [0,1] \mid Bel(A) \leq P(A)\},
$$
(4.4)

of probability distributions \(P\) on \(\Theta\) which dominate the belief function on each focal set \(A\). The size of the resulting credal prediction measures the extent of the related epistemic uncertainty arising from lack of evidence (see Sec. 5.3.4.3). The use of credal set size as a measure of epistemic uncertainty is well-supported in literature (Hüllermeier and Waegeman, 2021; Bronevich and Klir, 2008), as it aligns with established concepts of uncertainty such as conflict and non-specificity (Yager, 2008; Kolmogorov, 1965). A credal prediction, by encompassing multiple potential distributions, reflects the model's acknowledgment of this uncertainty. A wider credal set indicates higher uncertainty, as the model refrains from committing to a specific probability distribution due to limited or conflicting evidence. In contrast, a narrower credal set implies lower uncertainty, signifying a more confident prediction based on substantial, consistent evidence.

<!-- page: 56 -->

4.3. Modeling A Lack Of Knowledge                                                                                    33

#### 4.3.1.3 Credal Sets

In decision theory and probabilistic reasoning, *credal sets* provide a robust approach to modeling epistemic uncertainty by generalizing the traditional Bayesian framework. Unlike standard probabilistic models that assign precise probabilities to events, credal sets represent **convex sets of probability distributions**, allowing for a more flexible and cautious representation of uncertainty (Walley, 1991).

A *credal set* is a closed and convex set of probability distributions over a finite space \(\Omega\). This formulation allows one to express *imprecise probabilities*, where instead of a single probability value \(P(A)\), we consider a range \([P^-(A), P^+(A)]\) that characterizes the lower and upper bounds of belief for an event \(A\). This approach is particularly useful in settings where data is scarce or conflicting, making precise probability assignments unreliable (Augustin et al., 2014). Credal sets have been extensively used in *robust Bayesian inference*, *classification*, and *decision-making under ambiguity*. In machine learning, credal classifiers (Zaffalon, 2002) extend Bayesian classifiers by considering sets of posterior probabilities rather than single estimates, improving robustness to small-sample uncertainties.

#### 4.3.1.4 A Unified Example

To concretely illustrate how mass functions, belief functions, and credal sets relate to one another, we present a small, unified example. This example serves to clarify the abstract concepts discussed earlier by grounding them in a simple, interpretable setting with three classes. It highlights how belief values can be computed from mass functions and how these, in turn, define a credal set.

Consider a sample space (class list) \(\Theta = \mathcal{C} = \{c_1, c_2, c_3\}\) and let \(\mathbb{P}(\Theta)\) be its power set (collection of all subsets). As shown in Fig. 4.4, one can define a mass function on \(\mathbb{P}(\Theta)\) as: \(m(\{c_1\}) = 0.5\), \(m(\{c_3\}) = 0.1\), \(m(\{c_1, c_2\}) = 0.4\) (Fig. 4.4, top), and the masses for all other sets (unspecified) equal to zero. Note that \(m\) is normalised: \(\sum_{B \subseteq \Theta} m(B) = 1\). By Eq. 4.2, the belief value of the composite class \(A = \{c_2, c_3\}\) is: \(Bel(\{c_2, c_3\}) = m(\{c_3\}) = 0.1\) (Fig. 4.4, left). Similarly, the belief value of composite class \(\{c_1, c_2\}\) can by computed as \(Bel(\{c_1, c_2\}) = m(\{c_1\}) + m(\{c_1, c_2\}) = 0.5 + 0.4 = 0.9\).

[FIGURE: Figure 4.4. A belief function is equivalent to a credal set with boundaries determined by lower bounds (Eq. 7.1) on probability values.]

Text in figure:

Left ("Belief values"): diagram of classes c1, c2, c3 with Bel({c1,c2}) = m({c1}) + m({c1,c2}) = 0.5 + 0.4 = 0.9; Bel({c2,c3}) = m({c3}) = 0.1.
Middle ("Mass values"): m({c1,c2}) = 0.4; m({c1}) = 0.5; m({c3}) = 0.1.
Right ("Credal set" over the probability simplex with vertices p(c1) = 1, p(c2) = 1, p(c3) = 1): the region *Bel* and its centre of mass *BetP* are marked inside the simplex. [không đọc rõ: một số nhãn giá trị xác suất chồng lấn bên trong hình vẽ simplex không thể đọc rõ hoàn toàn]

Figure 4.4: A belief function is equivalent to a credal set with boundaries determined by lower bounds (Eq. 7.1) on probability values.

<!-- page: 57 -->

34                                                    Chapter 4. Epistemic Artificial Intelligence

## 4.4 Classical Probabilities Vs. Random Sets & Belief Functions

In this section, we explain the difference between classical probability measures and non-additive measures, such as random sets.

In a standard classification task, where each input is classified into one of several mutually exclusive classes, the classical probability framework does assume that each class is distinct and independent. The output of a softmax model provides the probabilities for each class, and these probabilities sum to 1. This approach works well when you are confident about the classification, for you have sufficient evidence to assign a clear probability to each class. However, it does not capture the uncertainty or ambiguity that exists when the evidence (as provided by the training set) is insufficient (*e.g.*, because you did not sample similar points at training time, or because the test data is affected by distribution shift).

Relying solely on confidence measures (like softmax probabilities) is insufficient for a comprehensive analysis of model predictions. Fig. 2.1 shows that standard neural networks are often overconfident (Nguyen et al., 2015) even for misclassifications.

Random sets, as the name suggests, assign probability mass values to sets *independently*, and are therefore more general than classical probability measures (which are a special case of random set). As a result, belief functions offer a way to handle uncertainty and make decisions when information is incomplete or ambiguous. While in classical probability, the sum of probabilities for individual events and their unions adheres to strict additive rules, belief functions relax these constraints to better capture uncertainty. In particular, the belief in the union of two hypotheses, \(Bel(\{A,B\})\), can be greater than the sum of the beliefs in the individual hypotheses, \(Bel(\{A\})\) + \(Bel(\{B\})\), i.e, \(Bel(\{A\}) + Bel(\{B\}) \leq Bel(\{A,B\})\). This inequality captures the idea that, in some situations, the available evidence may support the true class being in the set \(\{A, B\}\), without being enough to distinguish between the two alternatives. If \(Bel(\{A,B\}) > Bel(\{A\}) + Bel(\{B\})\), it indicates that the model has significant uncertainty or confusion about distinguishing between these classes for a particular input.

Unlike classical probability theory, belief functions operate in a higher space than probability vectors, i.e, it operates in a framework that generalizes classical probability theory. Suppose we know with 100% certainty that an event is either A or B. In a classical probability setting, we might say P(A) = 0.5 and P(B) = 0.5, or we might assign different probabilities to A and B if we have some reason to favor one over the other. With belief functions, we can represent the same scenario differently. We could assign a belief value of 1 to the set {A, B} and 0 to both A and B individually (\(Bel(\{A\}) = Bel(\{B\}) = 0\), \(Bel(\{A, B\}) = 1\)). This means that while we know the outcome must be either A or B, we are entirely uncertain about which one it is. Alternatively, we could have \(Bel(\{A\}) = 0.5\), \(Bel(\{B\}) = 0.5\), \(Bel(\{A, B\}) = 1\), reflecting a different state of knowledge or evidence, where we're somewhat more informed but still not fully certain. In the behavioural interpretation of probability (Walley, 2000), the belief value of an event A is the upper bound to the price one is willing to pay for betting on an outcome A.

Consider the following example (Cuzzolin, 2020): Suppose there is a murder, and three people—Peter, John, and Mary—are suspects. Our hypothesis space is therefore \(\Theta\) = {Peter, John, Mary}. A witness testifies that the person he saw was a man, supporting the proposition A = {Peter, John} \(\subseteq \Theta\). However, the witness was tested, and the machine reported a 20% chance that

<!-- page: 58 -->

4.5. Leveraging Epistemic AI                                                                    35

he was drunk when he gave his testimony. As a result, we assign 80% belief to the proposition A, representing our uncertainty about whether any of the two could be the murderer.

In classical probability, Kolmogorov's additive probability theory (Kolmogorov and Bharucha-Reid, 2018) forces us to specify support for individual outcomes, *i.e.* to distribute this 80% probability between Peter and John individually, even when the evidence (our data) supports set propositions. This is unreasonable – an artificial constraint due to a mathematical model that is not general enough. In the example, we have do not have enough evidence to assign this 80% probability to either Peter or John, nor information on how to distribute it amongst them. The cause is the additivity constraint that probability measures are subject to. This constraint reflects a broader limitation of measure-theoretical probability, which, while effective in many scenarios, struggles with second-order uncertainties and incomplete information.

This means that *belief functions allow us to model situations where we have uncertainty not just about which class an input belongs to, but also about whether we have enough evidence to distinguish between certain classes.* This added flexibility is what makes belief functions suitable for single-label classification tasks.

## 4.5 Leveraging Epistemic AI

This thesis proposes an epistemic deep learning model, called Random-Set Neural Network (RS-NN), as a step toward realizing the vision of Epistemic AI, detailed in Chapter 5. In addition, the author contributed to the development of two credal set models through collaborative research, which are briefly outlined in Chapter 6; however, a full exposition of these co-authored models is beyond the scope of this thesis. The conclusion of this thesis aso provides a comprehensive comparison of Epistemic AI models against baselines such as Bayesian and Ensemble models. The comparison (Sec. 11.2) spans key performance metrics, including test accuracy, out-of-distribution (OoD) detection, expected calibration error (ECE), and training and inference times, demonstrating the advantages of the proposed approach in uncertainty-aware learning.

<!-- page: 59 -->

36

# 5 Random-Set Neural Networks

The *main contribution* of this thesis, presented in this chapter, is a novel approach to classification that models epistemic uncertainty using a *random set* framework (Molchanov, 2005; 2017), introduced here as **Random-Set Neural Networks (RS-NN)**. This method serves as a concrete realization of the Epistemic AI perspective (Chapter 4) by explicitly modeling uncertainty through second-order uncertainty measures (Sec. 4.3.1), specifically belief functions (Sec. 4.3.1.2), random sets (Sec. 4.3.1.1), and credal sets (Sec. 4.3.1.3).

As they assign probability values to sets of outcomes directly, random sets can naturally model the fact that observations often come in the form of sets (in particular, when missing data occurs), and accommodate ambiguity, incomplete data, and non-probabilistic uncertainties. As classification involves only a finite list of classes, we model uncertainty using *belief functions* (Shafer, 1976), the finite incarnation of random sets (Cuzzolin, 2018b), whose theory (Shafer, 1976) is, in fact, a generalisation of Bayesian inference (Smets, July 1986). Classical (discrete) probabilities can be seen as special belief functions, and Bayes' rule as a special case of the Dempster's rule of combination (Dempster, 2008) originally proposed for aggregating belief functions. For readers less familiar with the topic, in Sec. 4.4 we recall the distinction between classical probabilities and belief functions and the way they handle uncertainty in more detail.

Fig. 5.1 contrasts the inference processes of our Random-Set Neural Network (RS-NN) and of a Bayesian Neural Network (Jospin et al., 2022). In hierarchical Bayesian inference (top), a posterior distribution over the network's weights is learned from a training set. At prediction time, a predictive distribution is generated in the target space (left) by sampling from this weight posterior (middle), which amounts to a second-order probability distribution there (Hüllermeier and Waegeman, 2021). A single (mean) prediction is then typically derived by Bayesian Model Averaging (BMA) (Hoeting et al., 1999) (right), while uncertainty is measured by the entropy of the mean prediction and the variance of the predictive distribution.

In a Random-Set Neural Network (Fig. 5.1, bottom), each test input at inference time is mapped to a belief function (Shafer, 1976) on the collection of classes \(\mathcal{C}\). This belief function is encoded by a mass value \(m(A) \in [0, 1]\) assigned to a finite budget \(\mathcal{O} = \{A_k \subset \mathcal{C}\}\) of sets of classes (left). The most relevant such sets are identified from training data by fitting a Gaussian Mixture Model (GMM) to the labelled data and computing the overlap among the resulting clusters (Spruyt, 2013). Such a predicted belief function is mathematically equivalent to a convex set of probability vectors (credal set (Levi, 1980; Cuzzolin, 2008a)) on the class list \(\mathcal{C}\) (middle). A pointwise prediction (right) can then be obtained by computing the centre of mass of this credal set, termed pignistic probability (Smets and Kennes, 1994). In RS-NN, uncertainty can be expressed using either the entropy of the pignistic prediction (analogously to the Bayesian case), or the width of the credal set prediction (Antonucci and Cuzzolin, 2010). We find empirically that the pignistic entropy better separates in-distribution (iD) and out-of-distribution (OoD)

<!-- page: 60 -->

Chapter 5. Random-Set Neural Networks                                                                               37

[FIGURE: Figure 5.1. Inference in a Bayesian Neural Network (top) as opposed to a Random-Set Neural Network (bottom), with corresponding measures of uncertainty and their sources.]

Text in figure:

**Bayesian Neural Network (BNN)** (top): Second-order distribution (Bayesian inference) → Probability simplex with predictive posteriors → Bayesian Model Averaging → Bayesian mean prediction → Uncertainty measures: Predictive Entropy, H(µ); Variance, σ².

**Random-Set Neural Network (RS-NN)** (bottom): Random-set space representation (m(A1), m(A2), ..., AK, m(AK)) → Probability simplex with credal set induced by belief functions → Pignistic Probability Function → Pignistic prediction BetP → Uncertainty measures: Pignistic Entropy, H(BetP); Credal set width.

Figure 5.1: Inference in a Bayesian Neural Network (top) as opposed to a Random-Set Neural Network (bottom), with corresponding measures of uncertainty and their sources. The triangle represents the set of probability vectors (probability simplex) one can define on the target space (*e.g.*, a set of 3 classes).

samples than Bayesian entropy does (Tab. 5.5); the width of the credal prediction, as it encodes the epistemic uncertainty about the prediction itself, is empirically much less correlated with the confidence score than entropy (Sec. 5.3.4.3).

Using a random-set representation prevents the need to discard information, a challenge observed in Bayesian Model Averaging (Hinne et al., 2020; Graefe et al., 2015). While Bayesian inference requires defining prior distributions for model parameters even in the absence of relevant information, in belief theory priors are not required for the inference process, thus avoiding the selection bias risks that can seriously condition Bayesian reasoning (Freedman, 1999). Based on our extensive experiments on multiple datasets, including large-scale ones, RS-NNs not only demonstrate superior accuracy compared to state-of-the-art Bayesian and Ensemble models (Sec. 5.3.2), but also arguably better encode the epistemic uncertainty associated with the predictions (Sec. 5.3.4) and better distinguish in-distribution and out-of-distribution data (Sec. 5.3.3). Furthermore, RS-NNs effectively circumvent the tendency of standard networks to generate overconfident incorrect predictions, as illustrated in Fig. 5.2 in an experiment on Fast Gradient Sign Method (FGSM) (Goodfellow et al., 2014) adversarial attacks on MNIST (LeCun and Cortes,

[FIGURE: Figure 5.2. Confidence scores of RS-NN and CNN for FGSM adversarial attack for different perturbations (ϵ = 0.05, 0.01) on MNIST dataset.]

Text in figure:

Epsilon: 0.05 — image of digit '3'. True Label: '3'. Predictions: RS-NN {'6'} : 32.59%; CNN '4' : 99.01%.
Epsilon: 0.01 — image of digit '3'. True Label: '3'. Predictions: RS-NN {'3', '6'} : 48.25%; CNN '4' : 96.74%.

Figure 5.2: Confidence scores of RS-NN and CNN for FGSM adversarial attack for different perturbations (ϵ = 0.05, 0.01) on MNIST dataset.

<!-- page: 61 -->

38                                                                                 Chapter 5. Random-Set Neural Networks

2005). CNN misclassifies with high confidence scores of 99.01% and 96.74%, while RS-NN shows lower confidence at 32.59% and 48.25%. This calibrated uncertainty helps avoid overconfident errors and supports risk-aware decisions, rather than leading to decision paralysis. In high-stakes, real-time decision contexts such as avoidance maneuvers in autonomous driving, overconfident yet incorrect predictions, as seen in the CNN, could lead to hazardous outcomes. In contrast, RS-NN's lower, more calibrated confidence enables the system to recognize uncertainty and either defer action, engage contingency protocols, or request external intervention, thereby promoting safer and more cautious responses under uncertainty.

## 5.1 Key Contributions

- **Firstly,** a novel *Random-Set Neural Network (RS-NN)* approach is proposed based on the principle that a deep neural network predicting belief values for *sets* of classes, rather than individual classes, has the potential to be a more faithful representation of the epistemic uncertainty induced by the limited quantity and quality of the training data. RS-NN acts as a ‘wrapper’ technique that can be applied on top of any existing baseline network model, by changing only the output layers and loss function. Statistical guarantees for RS-NN predictions can be provided by applying conformal prediction on the pignistic probabilities (§B).
- **Secondly,** a *budgeting* method is outlined for efficiently selecting a limited budget of relevant sets of classes for the task at hand given the available training data, by fitting Gaussian Mixture Models to the labelled training points and computing their clusters. This overcomes the exponential complexity of vanilla random-set implementations, ensures the scalability of the approach to large datasets, and helps the network learn by limiting the available degrees of freedom (Sec. 5.3.10.3).
- **Thirdly,** two new methods are introduced for assessing the uncertainty associated with a random-set prediction: the Shannon entropy of the pignistic prediction and the width of the credal prediction itself, which prove to be more robust uncertainty measures. For instance, pignistic entropy provides a clearer distinction between in-distribution (iD) and out-of-distribution (OoD) entropy (Fig. 5.8, Sec. 5.3.4.1), while credal set width excels in separating iD and OoD samples, particularly for challenging datasets like ImageNet vs. ImageNet-O (Tab. 5.15).
- **Finally,** a large body of experimental results is presented (based on a fair comparison principle in which all competing models are trained from scratch) demonstrating how RS-NN outperforms both state-of-the-art Bayesian (LB-BNN (Hobbhahn et al., 2022), FSVI (Rudner et al., 2022)) and Ensemble (DE (Lakshminarayanan et al., 2017), ENN (Osband et al., 2024)) methods in terms of:
  (i) performance (test accuracy, inference time) (Sec. 5.3.2);
  (ii) results on various out-of-distribution (OoD) benchmarks (Sec. 5.3.3), including CIFAR-10 vs. SVHN/Intel-Image, MNIST vs. FMNIST/KMNIST, and ImageNet vs. ImageNet-O;
  (iii) ability to provide reliable measures of uncertainty quantification (Sec. 5.3.4) in the form of pignistic entropy and credal set width, verified on OoD benchmarks;
  (iv) scalability to large-scale architectures (WideResNet-28-10, Inception V3, EfficientNet B2, ViT-Base-16) and datasets (*e.g.* ImageNet) (Sec. 5.3.5).

<!-- page: 62 -->

5.2. Methodology                                                                                       39

- Additionally, RS-NN is shown to be robust to adversarial attacks (Sec. 5.3.8) and noisy data (Sec. 5.3.7), and to circumvent the overconfidence problem in CNNs (Sec. 5.3.6). A qualitative assessment of entropy *vs.* credal set width is given in Sec. 5.3.4.3 and in-distribution *vs.* out-of-distribution entropy scores are shown in Fig. 5.8.

## 5.2 Methodology

This section intoduces the proposed Random-Set Neural Network (RS-NN) approach, ground truth representation, budgeting algorithm and loss function, and explains how RS-NN utilizes the concepts introduced in the previous Chapter 4.3 to efficiently model classification uncertainty.

### 5.2.1 Ground-truth Representation

[FIGURE: Figure 5.3. Standard one-hot encoded ground truth in traditional neural networks vs. belief function-based encoding in Random-Set Neural Networks (RS-NN).]

Text in figure:

Top ("Original one-hot encoded ground truth"): a row of circles labeled Classes 0,1,2,…,N with values 0, 1, 0, …, 0 (class 1 is filled/true).
Bottom ("Belief function encoded ground truth"): a row of circles labeled with sets of classes: ϕ, {0}, {1}, {2}, {3}, …, {0,1}, {0,2}, {1,2}, …, {2,3,4}, {1,2,3,4}, …, {0,1,2,...,N}, with values 0, 0, 1, 0, 0, …, 1, 0, 1, …, 0, 1, …, 1 (filled/true for every subset containing class 1).

Figure 5.3: Standard one-hot encoded ground truth in traditional neural networks vs. belief function-based encoding in Random-Set Neural Networks (RS-NN).

A classifier \(e\) (*e.g.*, a neural network) is a mapping from an input space \(X\) to a target space \(\mathcal{C}\) (the list of classes), *i.e.*, \(e : X \to \mathcal{C}\). In our set-valued (Sec. 4.3.1.1) classification setting, on the other hand, \(e\) is a mapping from \(X\) to the set of all *subsets* of \(\mathcal{C}\), the powerset \(\mathbb{P}(\mathcal{C})\), namely: \(e : X \to \mathbb{P}(\mathcal{C})\).

As shown in Fig. 5.4 (b), RS-NN predicts for each input data point a belief function, rather than a vector of softmax probabilities as in a traditional CNN. For \(N\) classes, a ‘vanilla’ RS-NN would have \(2^N\) outputs (as \(2^N\) is the cardinality of \(\mathbb{P}(\mathcal{C})\)), each being the belief value (Eq. 4.2) of the focal set of classes \(A \in \mathbb{P}(\mathcal{C})\) corresponding to that output neuron. Our architecture focuses primarily on the final layers (Fig. 5.4 (b), in grey), acting as a wrapper applicable on top of *any* baseline representation layers from existing models (Fig. 5.4 (b), in blue). This enables the integration of pre-trained networks while fine-tuning only the final decision layers. Hence, RS-NN is easily scalable to any model architecture, as demonstrated in Sec. 5.3.5, Tab. 5.7.

Given a training datapoint with a true class attached, its ground truth is encoded by the vector **bel** = \(\{Bel(A), A \in \mathbb{P}(\mathcal{C})\}\) of belief values for each focal set of classes \(A \in \mathbb{P}(\mathcal{C})\). \(Bel(A)\) is set to 1 iff the true class is contained in the subset \(A\), 0 otherwise[^1] as shown in Fig. 5.3. This

[^1]: Note that the belief encoding of ground-truth is not related to label smoothing. It maps ground-truth labels from the original class space to a set space without adding noise, thus preserving label ‘hardness’.

<!-- page: 63 -->

40                                                                                 Chapter 5. Random-Set Neural Networks

corresponds to full certainty that the element belongs to that set and there is complete confidence in this proposition (see Sec. 5.2.5 for an example).

In this thesis, the empty set is not included in the representation of the focal set. This is because there is no ground-truth label corresponding to the empty set, *i.e.*, the training process assumes that each input belongs to at least one of the known classes. As a result, no belief is ever explicitly allocated to the empty set during training. Including the empty set would imply allocating belief to the hypothesis that none of the known classes apply, which cannot be learned or supervised in the current closed-world setting. Its exclusion is therefore a modeling decision aligned with the structure of the training data and the learning objective.

### 5.2.2 Budgeting

[FIGURE: Figure 5.4. RS-NN model architecture.]

Text in figure:

(a) *Budgeting*: Feature vector over C → Fitting Gaussian Mixture Models (GMM) on each class → Overlapping clusters over P(C) (labeled e.g. {car,truck,vehicle}, {car,truck}, {vehicle}) → Top K relevant subsets {(car,truck,vehicle), …}, A ∈ P(C).

(b) *Training and Inference*: Input (e.g., image) → network layers (grey/blue) → Predicted belief \(\hat{Bel}(A)\) → **bel̂** → Pignistic Probability BetP, Mass values \(\hat{m}(A)\), Uncertainty estimate → Pignistic Entropy H(BetP); Credal set \(\hat{Cre}\) shown on a probability simplex with vertices p(c1)=1, p(c2)=1, p(c3)=1 (labeled "Training" below, "Inference" above); ground truth belief-encoded vector **bel** = Belief encoded ground truth of most relevant subsets \(\mathcal{O} = \mathcal{C} \cup \{A_1, \ldots, A_K\}\), \(Bel(A)\), minimizing loss \(\mathcal{L}_{RS}\).

Figure 5.4: **RS-NN model architecture.** (a) *Budgeting*: Given a collection \(\mathcal{C}\) of \(N\) classes, the top \(K\) relevant (focal) sets of classes \(\{A_1, \ldots, A_K\}\) are selected from the powerset \(\mathbb{P}(\mathcal{C})\) (Algorithm in §A.0.1) and added to the singleton classes to form the budget \(\mathcal{O}\). (b) *Training and Inference*: Ground truth classes are encoded as belief vectors **bel** and used to predict a belief function **bel̂** for each training data point by minimising the loss \(\mathcal{L}_{RS}\) (5.3), to train the output layers (in grey) producing **bel̂**. Mass values \(\hat{m}\) and pignistic probability estimates \(BetP\) are computed from the predicted belief function. Uncertainty is estimated as described in Sec. 5.2.4.

To overcome the exponential complexity of using \(2^N\) sets of classes (especially for large \(N\)), a fixed budget of \(K\) relevant non-singleton (of cardinality > 1) focal sets are used. These focal sets are obtained by clustering the original classes \(\mathcal{C}\), fitting ellipses over them, and selecting the top \(K\) focal sets of classes with the highest overlap ratio (Fig. 5.4 (a)). This is computed as the intersection over union for each subset \(A\) in \(\mathbb{P}(\mathcal{C})\): \(overlap(A) = \cap_{c \in A} A^c / \cup_{c \in A} A^c\), \(A_1, \ldots, A_K \in \mathbb{P}(\mathcal{C})\). Clustering is performed on feature vectors of images generated by any feature extractor trained on the original classes \(\mathcal{C}\). In our experiments, we used features from a trained standard ResNet50 model. These feature vectors are further reduced to 3 dimensions using t-SNE (t-Distributed Stochastic Neighbor Embedding) (van der Maaten and Hinton, 2008) before applying a Gaussian Mixture Model (GMM) to them. Ellipsoids (Spruyt, 2013), covering 95% of data, are generated using eigenvectors and eigenvalues of the covariance matrix \(\Sigma_c\) and the mean vector \(\mu_c\), \(\forall c \in \mathcal{C}\), \(P_c \sim \mathcal{N}(x_c; \mu_c, \Sigma_c)\) obtained from the GMM to calculate the overlaps. To avoid computing a degree of overlap for all \(2^N\) subsets, the algorithm is early stopped when increasing

<!-- page: 64 -->

5.2. Methodology                                                                                       41

the cardinality does not alter the list of most-overlapping sets of classes. The \(K\) non-singleton focal sets so obtained, along with the \(N\) original (singleton) classes, form our network's budget of outputs \(\mathcal{O} = \mathcal{C} \cup \{A_1, \ldots, A_K\}\). E.g., in a 100-class scenario, the powerset contains \(2^{100}\) subsets (\(10^{30}\) possibilities). Setting a budget of \(K = 200\), for instance, results in \(100 + K = 300\) outputs, a far more manageable number.

As shown in our experiments, budgeting also helps the network converge without overfitting. While, in theory, a complete belief function model would be more powerful, in practice a larger number of focal sets impedes the learning process. As shown in Tab. 5.17, Sec. 5.3.10.3, RS-NN with a limited number of well-representative sets often performs better than RS-NN with a full power set of classes, and is more efficient at uncertainty estimation. The budgeting step is a one-time procedure, applied to any given dataset before training. It requires just 2 minutes for CIFAR-10, 7 minutes for CIFAR-100, and 60 minutes for ImageNet (≈ 1.1M images, 1000 classes).

Further, our budgeting procedure is not specific to t-SNE, but can use any dimensionality reduction technique (Maćkiewicz and Ratajczak, 1993). For instance, Uniform Manifold Approximation and Projection (UMAP) (McInnes et al., 2018) requires approximately 1 minute for the CIFAR-10 dataset, 2 minutes for the CIFAR-100, and around 23 minutes for ImageNet to generate embeddings (Tabs. 5.19, 5.20 in Sec. 5.3.10.4 for a t-SNE *vs.* UMAP ablation study). This is including the overlap computation which only takes a few seconds and is efficiently parallelised across 150 CPU cores.

[FIGURE: Figure 5.5. 2D visualization of the clusters of 10 classes of CIFAR-10 dataset and the ellipses formed by RS-NN based on the hyperparameters of Gaussian Mixture Models.]

Text in figure: scatter plot with legend listing the 10 CIFAR-10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck, each shown as a differently-colored cluster of points with an overlapping dashed ellipse.

Figure 5.5: 2D visualization of the clusters of 10 classes of CIFAR-10 dataset and the ellipses formed by RS-NN based on the hyperparameters of Gaussian Mixture Models.

Fig. 5.5 shows a 2D visualization of the ellipses formed by computing the principal axes and their lengths from the eigenvectors and eigenvalues of the Gaussian Mixture Models (GMMs) fitted to each class \(c\) (Spruyt, 2013). Note that this is for visualization purposes only, in practice, the method operates in 3D.

<!-- page: 65 -->

42                                                              Chapter 5. Random-Set Neural Networks

### 5.2.3 Training RS-NN: Loss Function

A random-set prediction problem is mathematically similar to the multi-label classification problem, for in both cases the ground truth vector contains several 1s. In the former case, these correspond to sets all containing the true class; in the latter, to all the class labels attached to same data point. Despite the different semantics, we can thus adopt as loss Binary Cross-Entropy (BCE) (Scott, 2012) (Eq. 5.1) with sigmoid activation, to drive the prediction of a belief value for each focal set in the identified budget:

$$
\mathcal{L}_{BCE} = -\frac{1}{b_{size}} \sum_{i=1}^{b_{size}} \frac{1}{|\mathcal{O}|} \sum_{A \in \mathcal{O}} \Big[ Bel_i(A) \log(\hat{Bel}_i(A)) + (1 - Bel_i(A)) \log(1 - \hat{Bel}_i(A)) \Big].
$$
(5.1)

Here, \(i\) is the index of the training point within a batch of cardinality \(b_{size}\), \(A\) is a focal set of classes in the budget \(\mathcal{O}\), \(Bel_i(A)\) is the \(A\)-th component of the vector **bel**\(_i\) encoding the ground truth belief values for the \(i\)-th training point, and \(\hat{Bel}_i(A)\) is the corresponding belief value in the predicted vector **bel̂**\(_i\) for the same training point. Both **bel**\(_i\) and **bel̂**\(_i\) are vectors of cardinality \(|\mathcal{O}|\) for all \(i\).

A valid belief function satisfies Eq. 4.1 which states that mass values derived from belief functions should be non-negative and should sum up to 1 (Shafer, 1976). To promote this, we incorporate a mass regularization term \(M_r\) and a mass sum term \(M_s\) in the loss function:

$$
M_r = \frac{1}{b_{size}} \sum_{i=1}^{b_{size}} \sum_{A \in \mathcal{O}} \max(0, -\hat{m}_i(A)), \quad M_s = \max\!\left(0, \frac{1}{b_{size}} \sum_{i=1}^{b_{size}} \sum_{A \in \mathcal{O}} \hat{m}_i(A) - 1\right).
$$
(5.2)

\(M_r\) encourages non-negativity of the (predicted) mass values \(\hat{m}(A)\), \(A \in \mathcal{O}\). These mass values are obtained from the predicted belief function **bel̂** via the Moebius inversion formula (Eq. 4.2). For it to be valid, the sum of the masses of the predicted belief function must be equal to 1 (Eq. 4.1), which is encouraged by the mass sum term \(M_s\). All loss components \(\mathcal{L}_{BCE}\), \(M_r\) and \(M_s\) are computed during batch training. Two hyperparameters, \(\alpha\) and \(\beta\), control the relative importance of the two mass terms, yielding as the total loss for RS-NN:

$$
\mathcal{L}_{RS} = \mathcal{L}_{BCE} + \alpha M_r + \beta M_s.
$$
(5.3)

The regularisation terms aim to penalise deviations from valid belief functions, in line with, *e.g.*, the way training time regularisation in neurosymbolic learning encourages predictions to be commonsense (Giunchiglia et al., 2023). In general, soft constraints (Márquez-Neila et al., 2017) have been shown to be not inferior to hard ones. Still, when \(\alpha\) and \(\beta\) are too small, this may not be sufficient to ensure that predictions are valid belief functions. In such cases,[^2] post-training, we set any negative masses to zero and add the ‘universal’ set of all classes to the final budget. This subset is assigned all the remaining mass, ensuring that the sum of masses across all focal sets in \(\mathcal{O}\) equals 1. This approach mimics classical approximation schemes (*e.g.* Cuzzolin (2020), Part III).

[^2]: At any rate, improper belief functions are normally used in the literature (Denoeux, 2021), *e.g.* for conditioning (Cuzzolin, 2020).

<!-- page: 66 -->

5.2. Methodology                                                                                         43

### 5.2.4 Accuracy & Uncertainty Estimation

**Pignistic prediction.** The pignistic probability (Eq. 4.3) is the central prediction associated with a belief function (seen as a credal set): standard performance metrics such as accuracy can then be calculated after extracting the most likely class according to the pignistic prediction (*e.g.* in Sec. 5.3.4.1). Notably, the RS-NN architecture and training mechanism are designed to facilitate set-based learning by incorporating class set information during training. When pignistic probabilities are computed during inference, they reflect the learning derived from the masses and beliefs of various subsets, making it more reliable than traditional softmax probabilities, as shown in Sec. 5.3.6.

**Entropy of the pignistic prediction.** The Shannon entropy of the pignistic prediction \(BetP\) can then be used as a measure of the uncertainty associated with the predictions, in some way analogous to the entropy of a Bayesian mean average prediction:

$$
H_{RS} = -\sum_{c \in \mathcal{C}} BetP(c) \log BetP(c).
$$
(5.4)

A higher entropy value (Eq. 5.4) indicates greater uncertainty in the model's predictions.

**Size of the credal prediction.** As discussed above, and further elaborated upon in Sec. 5.3.4.3, a sensible measure of the epistemic uncertainty attached to a random-set prediction **bel̂** is the size of the corresponding credal set. Several ways exist of measuring the size of a convex polytope such as a credal set (Sale et al., 2023). Given the upper and lower bounds to the probability assigned to each class \(c\) by distributions within the predicted credal set \(\hat{Cre}\) (Eq. 7.1),

$$
\overline{P}(c) = \max_{P \in \hat{Cre}} P(c), \quad \underline{P}(c) = \min_{P \in \hat{Cre}} P(c),
$$
(5.5)

we propose a simple way to measure the size of the credal set as the difference between the lower and upper bounds (Eq. 5.5) associated with the most likely class, according to the pignistic prediction. Note that the predicted pignistic estimate \(BetP(c)\) falls within the interval \([\underline{P}(c), \overline{P}(c)]\) for each class \(c\), not just for the most likely class \(\hat{c}\). Its width \(\overline{P}(c) - \underline{P}(c)\) indicates the epistemic uncertainty associated with the prediction.

[FIGURE: Figure 5.6. Upper and lower bounds (Eq. 5.5), in dotted red, to the probability of the predicted most likely class according to the pignistic prediction (in solid red) for 100 samples of CIFAR-10.]

Text in figure: line plot, y-axis 0.2 to 1.0, x-axis "Samples" 0 to 100; legend: Max P, Bet P, Min P (all in shades of red, fluctuating across the 100 samples).

Figure 5.6: Upper and lower bounds (Eq. 5.5), in dotted red, to the probability of the predicted most likely class according to the pignistic prediction (in solid red) for 100 samples of CIFAR-10.

As they have belief values as lower bounds, credal sets induced by belief functions have a peculiar shape (Fig. 4.4, right, for a case with 3 classes). Their vertices are induced by the permutations of the elements of the sample space (for us, the set of classes) (Chateauneuf and Jaffray, 1989; Cuzzolin, 2008a). Given one such permutation, *e.g.*, \((c_2, c_4, c_1, c_3)\) for a set of 4 classes, the corresponding probability vector (vertex of the credal prediction) assigns to each class the mass

<!-- page: 67 -->

44                                                     Chapter 5. Random-Set Neural Networks

of all the focal sets containing it, *but* not containing any class preceding it in the permutation order (Wallner, 2005).

For additional illustration, the lower and upper bounds (Eq. 5.5) to the probability of the top predicted class are plotted in Fig. 5.6, together with the pignistic probability, for 100 samples of CIFAR-10. The bounds Eq. 5.5 can be efficiently computed from the finite number of vertices of the credal prediction ((Cuzzolin, 2008a), Fig. 4.4).

There has been considerable research on uncertainty measures for credal sets. One of the earlier works by Yager (2008) makes the distinction between two types of uncertainty within a credal set: conflict (also known as randomness or discord) and non-specificity. Non-specificity essentially varies with the size of the credal set (Kolmogorov, 1965). Since by definition, aleatoric uncertainty refers to the inherent randomness or variability in the data, while epistemic uncertainty relates to the lack of knowledge or information about the system (Hüllermeier and Waegeman, 2021), conflict and non-specificity directly parallel these concepts. These measures of uncertainty are axiomatically justified (Bronevich and Klir, 2008).

*Predictive uncertainty* in RS-NN is represented as the pignistic entropy of predictions \(H_{BetP}\), whereas *epistemic uncertainty* can be modelled by the ‘size’ of the credal set (Eq. 7.1).

### 5.2.5 RS-NN Learning Mechanism

Here we wish to expand on the rationale behind our choices for ground-truth representation **bel**, loss function and training, and the way in which RS-NN learns sets of outcomes.

Recall from Sec. 5.2.1 that the ground-truth for a RS-NN is the belief-encoded vector **bel** = \(\{Bel(A), A \in \mathbb{P}(\mathcal{C})\}\), where \(Bel(A)\) is the belief function of a focal set \(A\) in the power set \(\mathbb{P}\) of classes \(\mathcal{C}\). In our method, \(Bel(A)\) is 1 if the true class is in subset \(A\) and 0 otherwise. Consequently, the belief-encoded ground truth **bel** will include multiple occurrences of 1. For instance, in a digit-classification task such as MNIST, if \(\{3\}\) is the true class, the belief-encoded ground truth would contain 1s in all sets where \(\{3\}\) is present, such as \(\{1, 3\}\), \(\{0, 3\}\), \(\{1, 2, 3\}\), and so forth, 0 for sets not containing \(\{3\}\) at all, such as \(\{0, 1\}\), \(\{1, 2\}\), \(\{0, 1, 2\}\), *etc.*

Since we assign precise labels for belief containing different focal sets, our model begins by penalizing predictions that differ from the observed label in the same manner, regardless of the set's composition or relationship to the true label. Using MNIST as an example, this means that the loss incurred for predicting label \(\{3\}\) is equivalent to predicting label \(\{3, 7\}\), as both sets contain the true label. This equivalence in losses might seem counterintuitive at first glance. However, despite the identical loss values, the probabilities output by the sigmoid activation function will vary due to differences in the input logit values for each label. For instance, if the correct label is \(\{3\}\), the loss for predicting \(\{3\}\) or \(\{3, 7\}\) would be the same. Still, the loss for predicting \(\{7\}\) would differ, allowing the model to discern the set structure during training.

During the training process, the model learns to capture and understand these relationships by observing patterns and dependencies in the training data. As the model optimizes its parameters based on the training objective (*e.g.*, minimizing the loss function), it gradually adjusts its internal representations to better reflect these relationships. We use as the basis for our loss function Binary cross-entropy with sigmoid activation. It allows the model to predict the presence or absence of each label separately as a binary classification problem, producing probabilities between 0 and 1 for each class. While the model is unaware that it is learning for sets of

<!-- page: 68 -->

5.3. Experiments                                                                                 45

outcomes, we leverage this technique to extract mass functions and pignistic predictions from the learnt belief functions. By re-distributing masses to original classes, we obtain the best pignistic predictions that are often more accurate than standard CNN predictions, attributing to the higher accuracy in Tab. 5.3.

## 5.3 Experiments

**Firstly**, we assess the *test accuracy* (%) and *inference time* (ms) of all baselines on all the multi-class classification datasets. Tab. 5.3 provides a comparison of test accuracies and inference times of RS-NN against the baselines. Our **second** set of experiments (Sec. 5.3.3) concerns *out-of-distribution (OoD) detection*. Tab. 5.5 shows our results on OoD detection metrics AUROC (Area Under Receiver Operating Characteristic curve) and AUPRC (Area Under Precision-Recall curve) for all the models on the iD vs. OoD datasets listed above. We also report the Expected Calibration Error (ECE) for all models on datasets CIFAR-10, MNIST and ImageNet (Tab. 5.5). In a **third** set of experiments (Sec. 5.3.4), we test the *uncertainty estimation* capabilities of RS-NN using both the entropy of the pignistic prediction and the size of the predicted credal set. Tab. 5.5 presents the predicted pignistic entropy of RS-NN alongside entropies of all baselines on iD and OoD datasets. Tab. 5.6 shows credal set widths for RS-NN predictions across the same datasets. In our **final** set of experiments, we explore the *scalability of RS-NN* (Sec. 5.3.5) to large-scale architectures, employing it on models such as WideResNet-28-10, VGG16, Inception V3, EfficientNetB2 and ViT-Base-16. Further, to underscore the model's ability to leverage transfer learning, we train and test on a pre-trained ResNet50 model initialised with ImageNet weights (Tab. 5.7).

**Additional experiments** concern obtaining statistical guarantees for RS-NN using non-conformity scores (Sec. 1.1), evaluating the robustness of RS-NN to adversarial attacks (Sec. 5.3.8), noisy and rotated in-distribution samples (Appendix Sec. 5.3.7), showing how RS-NN circumvents the overconfidence problem in CNNs (Sec. 5.3.6). Results showing how credal set width is less correlated with confidence scores than entropy are discussed in in Sec. 5.3.4.3. We also conduct ablation studies on \(\alpha\) and \(\beta\) (Sec. 5.3.10.2) and the number of non-singleton focal sets \(K\) (Sec. 5.3.10.3), which show that the best accuracy is obtained at small values (\(1e-3\)) of \(\alpha\) and \(\beta\), and for \(K = 20\) (on the CIFAR-10 dataset).

### 5.3.1 Implementation

#### 5.3.1.1 Datasets

Our experiments are performed on multi-class image classification datasets, including MNIST (LeCun and Cortes, 2005), CIFAR-10 (Krizhevsky et al., 2009), Intel Image (Bansal, 2019), CIFAR-100 (Krizhevsky, 2012), and ImageNet (Deng et al., 2009). For out-of-distribution (OoD) experiments, we assess several in-distribution (iD) *vs.* OoD datasets: CIFAR-10 *vs.* SVHN (Netzer et al., 2011)/Intel-Image (Bansal, 2019), MNIST *vs.* F-MNIST (Xiao et al., 2017)/K-MNIST (Clanuwat et al., 2018), and ImageNet *vs.* ImageNet-O (Hendrycks et al., 2021). The data is split into 40000:10000:10000 samples for training, testing, and validation respectively for CIFAR-10 and CIFAR-100, 50000:10000:10000 samples for MNIST, 13934:3000:100 for Intel Image, 1172498:50000:108669 for ImageNet. For OoD datasets, we use 10,000 testing samples,

<!-- page: 69 -->

46                                                         Chapter 5. Random-Set Neural Networks

except for Intel Image (3,000) and ImageNet-O (2,000). Training images are resized to 224 × 224 pixels.

#### 5.3.1.2 Baselines and Backbones

Our baselines include state-of-the-art Bayesian methods LB-BNN (Hobbhahn et al., 2022) and FSVI (Rudner et al., 2022), Ensemble classifiers DE (5 ensembles) (Lakshminarayanan et al., 2017) and ENN (3 ensembles) (Osband et al., 2024), and standard neural network (CNN). All models, including RS-NN, are trained on ResNet50 (on NVIDIA A100 80GB GPUs) with a learning rate scheduler initialized at 1e-3 with 0.1 decrease at epochs 80, 120, 160 and 180. Standard data augmentation (Krizhevsky et al., 2012), including random horizontal/vertical shifts with a magnitude of 0.1 and horizontal flips, is applied to all models.

Laplace Bridge Bayesian approximation (LB-BNN) (Hobbhahn et al., 2022) uses the Laplace Bridge to map efficiently between Gaussian and Dirichlet distributions and enhance computational efficiency. In our experiments, we obtain multiple samples from the LB-BNN posterior and average these samples using Bayesian Model Averaging (BMA). Function-Space Variational Inference (FSVI) (Rudner et al., 2022) utilizes variational inference to derive an approximation of the posterior distribution over the function space. FSVI proposes approximating distributions over functions as Gaussian by linearizing their mean parameters and derived a tractable and well-defined variational posterior. Deep Ensembles (DEs) (Lakshminarayanan et al., 2017) and Epistemic Neural Networks (ENNs) (Osband et al., 2024) are ensemble methods that train ensembles of models to efficiently estimate uncertainty. The mean and variance of ensemble predictions are calculated and the mean is softmaxed to obtain predictions from DE and ENN. The training hyperparameters for all models are outlined in Tab. 5.1.

Table 5.1: Training Hyperparameters for All Models

| Parameter | Value |
|---|---|
| **Architecture** | ResNet50 (excluding top classification layer) |
| **Additional Dense Layers** | 1024 and 512 neurons (ReLU activation) |
| **Output Layer Activation (RS-NN)** | Sigmoid (multi-label classification) |
| **Output Layer Activation (Other Models)** | Softmax (multi-class classification) |
| **Learning Rate** | Initial: 1e-3 |
| **Learning Rate Scheduler** | Decrease by 0.1 at epochs 80, 120, 160, 180 |
| **Training Epochs** | 200 |
| **Batch Size** | 128 |
| **Optimizer** | RS-NN: Adam, LB-BNN: Adam, ENN: Adam, DE: Adam, FSVI: SGD |
| **Training Dataset Sizes** | CIFAR-10: 40,000; CIFAR-100: 40,000; MNIST: 50,000; Intel Image: 13,934; ImageNet: 1,172,498 |
| **Testing Dataset Sizes** | CIFAR-10: 10,000; CIFAR-100: 10,000; MNIST: 10,000; Intel Image: 3,000; ImageNet: 2,000 |
| **Testing Samples for OoD Datasets** | 10,000 (except Intel Image: 3,000) |
| **Input Image Size** | 224 × 224 |
| **Data Augmentation** | Random horizontal/vertical shifts (magnitude 0.1), horizontal flips |
| **GPU** | NVIDIA A100 80GB |

<!-- page: 70 -->

5.3. Experiments                                                                                                    47

#### 5.3.1.3 Training Details

ResNet50, excluding the top classification layer, serves as the common architecture. ResNet was originally designed for classification on the ImageNet dataset (1000 classes). To accommodate a reduced number of classes as in smaller datasets (*e.g.*, CIFAR-10/MNIST with 10 classes, Intel Image with 7 classes, and CIFAR-100 with 100 classes), two additional dense layers (1024 and 512 neurons, ReLU activation) are added to ResNet50. Similar techniques are commonly applied in deep learning to adapt model architectures to datasets (He et al., 2016; Zagoruyko and Komodakis, 2016). The output layer of RS-NN on ResNet50 has the same number of units as the number of (selected) focal sets \(|\mathcal{O}|\), and uses sigmoid activation, since the ground truth encoding resembles a multi-label classification problem (Sec. 5.2.3).

For all other models, the final output layer simply consists of a softmax activation for multi-class classification. All the models were trained from scratch for 200 epochs (recommended by most), with a batch size of 128. *Our objective is to ensure a fair comparison across all models for all experiments.* Tuning each model separately to maximise performance would not guarantee that, as some models use pre-trained weights while others train for larger number of epochs, which could result in the over-training of another model. We used pre-trained weights for all models only when trained on ImageNet for efficiency. For all other training hyperparameters (e.g, optimizer), we use what is specified for each model in their respective papers (more in Sec. 5.3.1.2, Tab. 5.1). Consequently, the performance metrics reported in the original papers may vary from those presented here, as they were obtained under different training conditions.

In the budgeting phase, we obtain features directly from a pre-trained ResNet50 classifier. We use 50 CPU cores for t-SNE dimensionality reduction, and 150 CPU cores for computing the overlap of classes. We set a budget \(K\) of 20 focal sets (ablation study on K in Sec. 5.3.10.3) for CIFAR-10/ MNIST/ Intel Image, 200 for CIFAR-100 and 3000 for ImageNet. RS-NN is trained from scratch on ground-truth belief encoding of sets using the \(\mathcal{L}_{RS}\) loss function (Eq. 5.3) over 200 epochs, with a batch size (\(b_{size}\)) of 128 and \(\alpha = \beta = 1e-3\) as hyperparameter values.

#### 5.3.1.4 Sample Prediction

Table 5.2: The predicted belief, mass values, pignistic probabilities, and entropy for two CIFAR-10 predictions. The figure on the top (True Label = ‘horse’) is a certain prediction with 99.9% confidence and a low entropy of 0.0017, whereas the figure on the bottom (True Label = ‘cat’) is an uncertain prediction with 33.3% confidence and a higher entropy of 2.6955.

| Sample | Belief |  | Mass |  | Pignistic |  | Entropy |
|---|---|---:|---|---:|---|---:|---:|
| (horse image) | {'horse', 'bird'} | 0.9999402 | {'horse'} | 0.9999175 | horse | 0.9998833 | 0.0017040148 |
| | {'horse', 'dog'} | 0.9999225 | {'cat', 'truck'} | 6.859753e-05 | truck | 3.5826409e-05 | |
| | {'horse'} | 0.9999175 | {'ship', 'bird'} | 4.094290e-05 | cat | 3.3859180e-05 | |
| | {'horse', 'deer'} | 0.9998697 | {'horse', 'bird'} | 2.250525e-05 | bird | 3.3015738e-05 | |
| | {'cat', 'truck'} | 7.0380207e-05 | {'dog'} | 1.717869e-05 | ship | 2.3060647e-05 | |
| (cat image) | {'deer', 'cat'} | 0.4787728 | {'deer'} | 0.3104962 | deer | 0.3332411 | 2.6955228261 |
| | {'deer', 'airplane', 'bird'} | 0.4126398 | {'cat', 'truck'} | 0.1762222 | cat | 0.2230723 | |
| | {'horse', 'deer'} | 0.3732957 | {'dog', 'bird'} | 0.0998060 | horse | 0.1153417 | |
| | {'deer', 'bird'} | 0.3658997 | {'horse', 'bird'} | 0.0954350 | bird | 0.1086245 | |
| | {'deer', 'dog'} | 0.3651531 | {'bird'} | 0.0524873 | dog | 0.1039505 | |

<!-- page: 71 -->

48                                                                                                            Chapter 5. Random-Set Neural Networks

[FIGURE: Figure 5.7. Visualizations of belief and mass predictions on the power-set space and its mapping to the label space using pignistic probabilities on the CIFAR-10 dataset.]

Text in figure: top chart "Predicted Belief and Mass Functions (True Class: frog)" — scatter of Belief Functions and Mass Functions values (0 to 1) across many focal sets of classes on the x-axis (singletons and pairs/triples, e.g. {'airplane'}, {'bird'}, {'cat'}, …, {'cat', 'frog'}, {'deer', 'frog', 'bird'}, etc.); bottom chart "Pignistic Probability (True Class: frog)" — bar chart of pignistic probability per class (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), with 'frog' having the highest value.

Figure 5.7: Visualizations of belief and mass predictions on the power-set space and its mapping to the label space using pignistic probabilities on the CIFAR-10 dataset.

Since RS-NN predictions differ from those of other baseline models, this section presents **sample predictions** produced by RS-NN. The predicted belief, mass values, pignistic probabilities, and entropy for two CIFAR-10 predictions are illustrated in Tab. 5.2. In the top figure, corresponding to the true label ‘horse’ the model makes a highly confident prediction with 99.9% confidence and a low entropy of 0.0017. Conversely, the bottom figure, associated with the true label ‘cat’ represents an uncertain prediction with 33.3% confidence and a higher entropy of 2.6955. It is important to note that the second image is slightly unclear and poor in quality.

Fig. 5.7 shows belief function predictions for an input sample with the true class ‘frog’. The belief function predictions and their mapping to mass functions and pignistic probabilities are illustrated.

### 5.3.2 Performance: Accuracy & Expected Calibration Error

Tab. 5.3 shows that RS-NN outperforms state-of-the-art Bayesian (LB-BNN, FSVI) and Ensemble (DE, ENN) methods in terms of test accuracy (%) across all datasets. Experiments on inference

<!-- page: 72 -->

5.3. Experiments                                                                                                                                           49

Table 5.3: Test accuracies (%) and inference time (ms) for uncertainty estimation over 5 consecutive runs across methods and datasets. Average and standard deviation are shown for each experiment.

| Datasets | MNIST | CIFAR-10 | Intel Image | CIFAR-100 | ImageNet (Top-1) | ImageNet (Top-5) | Inference time (ms) |
|---|---|---|---|---|---|---|---|
| **RS-NN (ours)** | 99.71 ± 0.03 | 93.53 ± 0.09 | 94.22 ± 0.03 | 71.61 ± 0.07 | 79.92 | 94.47 | **1.91 ± 0.02** |
| LB-BNN (Hobbhahn et al., 2022) | 99.58 ± 0.04 | 89.95 ± 0.81 | 90.49 ± 0.42 | 59.89 ± 1.96 | 72.48 | 90.85 | 7.11 ± 0.89 |
| FSVI (Rudner et al., 2022) | 99.18 ± 0.03 | 80.29 ± 0.05 | 88.92 ± 0.13 | 53.34 ± 0.09 | 62.56 | 84.69 | 340.25 ± 0.76 |
| DE (Lakshminarayanan et al., 2017) | 99.25 ± 0.01 | 92.73 ± 0.04 | 91.98 ± 0.11 | 70.53 ± 0.07 | 78.77 | 94.37 | 13163.50 ± 3.37 |
| ENN (Osband et al., 2024) | 99.07 ± 0.11 | 91.55 ± 0.60 | 91.49 ± 0.19 | 68.02 ± 0.26 | 71.82 | 89.48 | 3.10 ± 0.03 |
| CNN | 99.12 ± 0.04 | 92.08 ± 0.42 | 90.89 ± 0.10 | 65.50 ± 0.08 | 78.56 | 94.34 | **1.91 ± 0.03** |

time (ms) per sample, conducted over 5 runs (a single forward propagation) on the CIFAR-10 dataset, show that RS-NN and CNN have the fastest inference times among all models (Tab. 5.3). Albeit CNN and DE are close to RS-NN in performance (*e.g.*, on ImageNet), CNN tends to be overconfident in incorrect predictions (Sec. 5.3.6), while DE has significantly longer training (Tab. 5.4, Sec. 5.3.1.2) and inference times (Tab. 5.3). The pignistic predictions derived from predicted belief functions are more reliable and accurate than predicted softmax probabilities of CNN and DE. It is important to note that the comparison with standard CNN is not based on its role as an uncertainty method, but as a benchmark, underscoring RS-NN's effectiveness in achieving high accuracy compared to other uncertainty baselines. Test accuracy for RS-NN is calculated by determining the class with the highest pignistic probability for each prediction and comparing it with the true class. This proves that, by modelling the epistemic uncertainty about the prediction, we take better into account possible distribution shifts at test time - as a result, the central prediction of the set of probabilities (credal set) associated with the predicted belief function is more likely to be closer to the ground truth. Note that the results in the FSVI paper (Rudner et al., 2022) are based on ResNet18. Although using a pre-trained ResNet50 could enhance FSVI's performance, it would provide an unfair advantage over the other baseline models in our paper, which were all trained from scratch.

We report the training times (in minutes) for all models on the CIFAR-10 dataset in Tab. 5.4. Tab. 5.4 shows that FSVI has the longest training time, followed by RNN and DE. Compared to LB-BNN, RS-NN adds 5 minutes to the training duration, while CNN has the shortest training time. However, CNNs do not provide uncertainty estimation, and RS-NN has more reliable uncertainty and OoD metrics compared to LB-BNN.

The significant training time required for Deep Ensembles (DE) often does not justify their uncertainty estimates (Abe et al., 2022; Rahaman et al., 2021). Despite the computational cost, DE is sometimes only as good as other uncertainty estimation models, which can be trained much faster. Other approaches, like methods with calibration techniques (*e.g.*, temperature scaling or Bayesian approaches), can provide similar performance without the substantial overhead that DE entails.

Table 5.4: Training time (min) for all models on the CIFAR-10 dataset.

| | RS-NN | LB-BNN | FSVI | DE | ENN | CNN |
|---|---|---|---|---|---|---|
| Training time (min) | 113.23 | 107.900 | 1518.35 | 426.66 | 712.302 | 85.333 |

As mentioned in Sec. 5.3.2, the results for FSVI are different than what was reported in (Rudner et al., 2022). The lower performance with ResNet-50 in our experiments may be attributed to the model being optimized specifically for ResNet-18. We noticed the unexpectedly low results and adhered to their suggested optimizer, SGD, instead of Adam (used in all other models), to achieve optimal performance, as mentioned in Tab. 5.1. Additionally, to enhance performance, we also

<!-- page: 73 -->

50                                                                                               Chapter 5. Random-Set Neural Networks

Table 5.5: OoD detection performance and uncertainty estimation for models trained on ResNet50 on CIFAR-10 vs. SVHN/Intel Image, MNIST vs. F-MNIST/K-MNIST and ImageNet vs. ImageNet-O. Evaluation metrics include AUROC/AUPRC (OoD); Entropy of predictions (uncertainty) and Expected Calibration Error (ECE).

CIFAR-10 (in-distribution) vs. SVHN / Intel Image (out-of-distribution):

| Model | Test accuracy (%) ↑ | Uncertainty measure | In-distribution Entropy ↓ | ECE ↓ | SVHN AUROC ↑ | SVHN AUPRC ↑ | SVHN Entropy ↑ | Intel Image AUROC ↑ | Intel Image AUPRC ↑ | Intel Image Entropy ↑ |
|---|---|---|---|---|---|---|---|---|---|---|
| RS-NN | 93.53 | Pignistic entropy | 0.088 ± 0.308 | 0.0484 | 94.91 | 93.72 | 1.132 ± 0.855 | 97.39 | 90.27 | 1.517 ± 0.740 |
| LB-BNN | 89.95 | Predictive Entropy | 0.191 ± 0.412 | 0.0585 | 88.14 | 81.96 | 0.828 ± 0.243 | 82.21 | 55.17 | 0.763 ± 0.722 |
| FSVI | 80.29 | Predictive Entropy | 0.118 ± 0.563 | 0.0521 | 80.59 | 80.84 | 0.413 ± 0.461 | 74.27 | 72.51 | 0.289 ± 0.670 |
| DE | 92.73 | Mean Entropy | 0.154 ± 0.367 | 0.0482 | 93.84 | 91.88 | 0.939 ± 0.554 | 94.25 | 79.36 | 1.166 ± 0.552 |
| ENN | 91.55 | Mean Entropy | 0.126 ± 0.323 | 0.0556 | 92.76 | 89.05 | 0.887 ± 0.514 | 85.67 | 58.09 | 0.600 ± 0.578 |
| CNN | 92.08 | Softmax Entropy | 0.114 ± 0.304 | 0.0669 | 93.11 | 91.0 | 0.930 ± 0.610 | 87.75 | 65.54 | 0.719 ± 0.673 |

MNIST (in-distribution) vs. F-MNIST / K-MNIST (out-of-distribution):

| Model | Test accuracy (%) ↑ | Uncertainty measure | In-distribution Entropy ↓ | ECE ↓ | F-MNIST AUROC ↑ | F-MNIST AUPRC ↑ | F-MNIST Entropy ↑ | K-MNIST AUROC ↑ | K-MNIST AUPRC ↑ | K-MNIST Entropy ↑ |
|---|---|---|---|---|---|---|---|---|---|---|
| RS-NN | 99.71 | Pignistic entropy | 0.010 ± 0.111 | 0.0029 | 93.89 | 93.98 | 0.530 ± 0.770 | 96.75 | 96.58 | 0.740 ± 0.917 |
| LB-BNN | 99.58 | Predictive Entropy | 0.001 ± 0.085 | 0.0032 | 89.65 | 90.36 | 0.287 ± 0.442 | 95.61 | 95.65 | 0.540 ± 0.621 |
| FSVI | 99.18 | Predictive Entropy | 0.006 ± 0.265 | 0.0047 | 92.79 | 91.17 | 0.264 ± 0.289 | 91.65 | 95.75 | 0.313 ± 0.381 |
| DE | 99.25 | Mean Entropy | 0.031 ± 0.155 | 0.0031 | 92.30 | 92.05 | 0.584 ± 0.587 | 95.81 | 94.71 | 0.564 ± 0.715 |
| ENN | 99.07 | Mean Entropy | 0.022 ± 0.127 | 0.0039 | 81.79 | 82.92 | 0.313 ± 0.464 | 95.94 | 95.45 | 0.503 ± 0.672 |
| CNN | 98.90 | Softmax Entropy | 0.023 ± 0.135 | 0.0052 | 83.77 | 84.14 | 0.278 ± 0.426 | 94.46 | 93.94 | 0.616 ± 0.688 |

ImageNet (in-distribution) vs. ImageNet-O (out-of-distribution):

| Model | Test accuracy (%) ↑ | Uncertainty measure | In-distribution Entropy ↓ | ECE ↓ | ImageNet-O AUROC | ImageNet-O AUPRC | ImageNet-O Entropy |
|---|---|---|---|---|---|---|---|
| RS-NN | 79.92 | Pignistic entropy | 2.972 ± 2.108 | 0.1416 | 60.38 | 55.16 | 3.659 ± 3.771 |
| LB-BNN | 72.48 | Predictive Entropy | 2.471 ± 2.972 | 0.5812 | 41.08 | 30.99 | 1.383 ± 0.028 |
| FSVI | 62.56 | Predictive Entropy | 1.328 ± 1.966 | 0.3890 | 50.55 | 49.88 | 1.637 ± 1.328 |
| DE | 78.77 | Mean Entropy | 1.532 ± 1.325 | 0.1940 | 55.37 | 53.20 | 1.775 ± 1.343 |
| ENN | 71.82 | Mean Entropy | 1.395 ± 1.510 | 0.5961 | 54.67 | 43.73 | 1.617 ± 1.597 |
| CNN | 78.56 | Softmax Entropy | 6.386 ± 1.388 | 0.4004 | 54.28 | 48.73 | 6.575 ± 1.512 |

incorporated the context points from ImageNet and CIFAR-100 as recommended in Rudner et al. (2022). Furthermore, we observed that FSVI uses more extensive data augmentation than our standardized setup. For instance, their data augmentation includes random crops and higher magnitude random flips (0.5), while we only used random horizontal/vertical flips of magnitude 0.1, potentially contributing to the performance gap. While increasing model capacity by using ResNet-50 (25.6M parameters) over ResNet-18 (11.7M parameters) should theoretically improve performance, this is not always the case in practice. ResNet-50 requires more careful optimization and is more prone to overfitting, particularly when used with smaller datasets or suboptimal augmentation. This explains why ResNet-50 did not consistently outperform ResNet-18 in our implementation of the compared methods.

### 5.3.3 Out-of-distribution Detection

We evaluate our out-of-distribution (OoD) detection (Tab. 5.5) against baselines using AUROC and AUPRC scores. OoD detection identifies data points deviating from the in-distribution (iD) training data by measuring true and false positive rates (AUROC) and precision and recall trade-offs (AUPRC), indicating the model's ability to handle unfamiliar data (further detailed in §A.0.3). As shown in Tab. 5.5, RS-NN greatly outperforms Bayesian, Ensemble and standard CNN models in OoD detection, with significantly higher AUROC and AUPRC scores for all iD vs. OoD datasets, especially on difficult datasets like ImageNet and ImageNet-O (Sec. 5.3.10.1). Even high-accuracy models like CNN and DE struggle to differentiate between ImageNet and ImageNet-O. While DE shows comparable AUROC scores on CIFAR-10 vs. SVHN and MNIST vs. F-MNIST/K-MNIST to RS-NN, it has lower AUPRC. While AUROC assesses a model's ability to distinguish between iD and OoD samples, AUPRC measures both the precision of correctly identified OoD samples and the recall of detected OoD samples, making it a more informative metric. Tab. 5.5 also reports the various models' Expected Calibration Error (ECE) (detailed in §A.0.2). A low ECE indicates that the model's confidence scores align closely with the actual

<!-- page: 74 -->

5.3. Experiments                                                                                                                                                                                          51

likelihood of events. RS-NN exhibits the lowest ECE indicating well-calibrated probabilistic predictions.

### 5.3.4 Uncertainty Estimation

#### 5.3.4.1 Entropy of Pignistic Predictions

Tab. 5.5 shows the mean and variance of the entropy distributions for both iD and OoD datasets. Lower entropy values for iD datasets indicate a confident prediction as the model is trained on familiar data, while higher entropy for OoD datasets reflects the model's uncertainty with unseen data. RS-NN exhibits both low entropy for iD datasets and high entropy for OoD ones. The percentage mean iD/OoD shift in entropy is most pronounced in RS-NN, especially evident in CIFAR-10 vs. SVHN/Intel Image and MNIST vs. F-MNIST/K-MNIST. For ImageNet vs. ImageNet-O, CNN exhibits high entropy for both iD and OoD datasets while RS-NN maintains a desirable iD vs. OoD entropy ratio.

[FIGURE: Figure 5.8. Entropy comparison of all models for iD and OoD datasets.]

Text in figure: three bar charts — "Entropy Comparison for CIFAR-10" (legend: In-Distribution (CIFAR-10), Out-of-Distribution (SVHN), Out-of-Distribution (Intel)), "Entropy Comparison for MNIST" (legend: In-Distribution (MNIST), Out-of-Distribution (F-MNIST), Out-of-Distribution (K-MNIST)), and "Entropy Comparison for ImageNet" (legend: In-Distribution (ImageNet), Out-of-Distribution (ImageNet-O)); x-axis in each: RS-NN, LB-BNN, FSVI, DE, ENN, CNN; y-axis: Entropy, with error bars.

Figure 5.8: Entropy comparison of all models for iD and OoD datasets. The plots illustrate the performance of various models, with error bars indicating the standard deviation of entropy values.

Fig. 5.8 illustrates that RS-NN exhibits the best **iD *vs.* OoD entropy ratio** among the evaluated baseline models. Specifically, RS-NN maintains significantly lower entropy values for iD datasets, indicating a strong ability to recognize familiar patterns while showing elevated entropy for OoD datasets. DE and CNN closely follow RS-NN but struggle to effectively differentiate entropy for the ImageNet dataset. LB-BNN shows more uncertainty regarding iD samples compared to OoD samples. FSVI demonstrates the weakest distinction between iD and OoD.

Fig. 5.9 shows the entropy for two samples of CIFAR-10, one is a slightly uncertain image, whereas the other is certain with high belief values and lower entropy. Both results are shown for K = 20 classes, additional to the 10 singletons.

**Qualitative results of entropy.** Fig. 5.10 depicts entropy-based uncertainty estimates for rotated out-of-distribution (OoD) MNIST digit ‘3’ samples. All models accurately predict the true class at −30°, 0°, and 30°. RS-NN and LB-BNN consistently exhibit low entropy in these scenarios, while ENN shows higher entropy for correct classifications at these angles. As the rotation angle increases, indicating more challenging scenarios, all models predict the wrong class. Notably, LB-BNN fails to exhibit a significant increase in entropy for these incorrect predictions. ENN performs relatively better than RS-NN at 60° and 90° rotations but has previously demonstrated high entropy levels even for accurate predictions at relatively minor

<!-- page: 75 -->

52                                                                         Chapter 5. Random-Set Neural Networks

[FIGURE: Figure 5.9. Entropy, predicted class and belief value graph for two samples of CIFAR-10 dataset.]

Text in figure: left chart — image of a cat-like animal, "Entropy: 0.8285", "Predicted Class: {'cat'}", bar chart of belief values across many focal sets of classes (singletons and pairs/triples of the 10 CIFAR-10 classes). Right chart — image of a ship, "Entropy: 0.0547", "Predicted Class: {'ship'}", bar chart of belief values similarly.

Figure 5.9: Entropy, predicted class and belief value graph for two samples of CIFAR-10 dataset.

rotations of −30° and +30° degrees. Overall, RS-NN provides a more reliable measure of uncertainty.

[FIGURE: Figure 5.10. Uncertainty (entropy) of MNIST digit '3' rotated between -90 and 90 degrees.]

Text in figure: line chart, x-axis "Rotation Degree" from -90 to 90 (with rotated '3' digit images shown along the axis at each angle), y-axis "Uncertainty" 0.0 to 3.0; legend: RS-NN (blue), ENN (red), LB-BNN (green).

Figure 5.10: Uncertainty (entropy) of MNIST digit ’3’ rotated between -90 and 90 degrees. The blue line indicates RS-NN estimates low uncertainty between -30 to 30, and high uncertainty for further rotations.

Figs. 5.11 and 5.12 show the entropy distributions for RS-NN on MNIST (iD) *vs.* Fashion-MNIST (OoD)/Kuzushiji-MNIST (OoD), and CIFAR-10 (iD) *vs.* SVHN (OoD)/Intel-Image (OoD), respectively. There is a clear iD *vs.* OoD shift in entropy for RS-NN, as detailed in Sec. 5.3.4. The plots show that RS-NN consistently exhibits larger iD *vs.* OoD entropy ratio for all datasets. For iD data, the entropy values are generally lower, indicating that these models exhibit a higher level of confidence when making predictions within familiar datasets. Conversely, the OoD side shows significantly higher entropy values for most models, particularly notable with the SVHN and Intel datasets, suggesting that the models struggle to generalize when faced with unfamiliar data.

<!-- page: 76 -->

5.3. Experiments                                                                                                                                           53

[FIGURE: Figure 5.11. Entropy Distributions for RS-NN on MNIST vs. Fashion-MNIST/Kuzushiji-MNIST.]

[FIGURE: Figure 5.12. Entropy Distributions for RS-NN on CIFAR-10 vs. SVHN/Intel-Image.]

Text in figures: density plots of entropy (x-axis 0.0–3.0) vs. Density (y-axis); Fig. 5.11 legend: IID = MNIST, OOD = Fashion-MNIST, OOD = Kuzushiji-MNIST; Fig. 5.12 legend: IID = CIFAR10, OOD = SVHN, OOD = Intel-Image.

#### 5.3.4.2 Credal Set Width

Fig. 5.13 shows a density plot of estimated credal set widths, the difference between the lower and upper probability bounds in Eq. 5.5, for correctly and incorrectly classified samples of CIFAR-10 test data. Incorrect predictions (red) correlate with larger credal set widths, indicating higher epistemic uncertainty, and are more dispersed in the plot. Correct predictions (blue) concentrate around smaller values, exhibiting smaller credal intervals as expected.

[FIGURE: Figure 5.13. Width of credal predictions for CIFAR-10 test data (correctly classified, blue; incorrectly classified, red).]

Text in figure: density plot "Density of Credal Set Width for Correct and Incorrect Classifications", x-axis "Credal Set Width" 0.0–0.7, y-axis "Density"; legend: Incorrectly Classified, Correctly Classified.

Figure 5.13: Width of credal predictions for CIFAR-10 test data (correctly classified, blue; incorrectly classified, red).

Tab. 5.6 reports the credal set widths of RS-NN predictions for iD vs. OoD datasets. Larger intervals can be observed for OoD datasets. The credal set widths for ImageNet vs. ImageNet-O are not as distinct given the nature of these datasets, as detailed in Sec. 5.3.10.1. Note that credal set width is not directly comparable to the entropy, variance or mutual information of other models, as such metrics have distinct semantics.

Fig. 5.14 plots the credal set widths for correctly and incorrectly classified samples over each class \(c\) in CIFAR-10, respectively. The box represents the interquartile range between the 25th and 75th percentiles of the data encompassing most of the data. The vertical line inside the box represents the median and the whiskers extend from the box to the minimum and maximum values within a certain range, and data points beyond this range are considered outliers and

<!-- page: 77 -->

54                                                                                             Chapter 5. Random-Set Neural Networks

Table 5.6: Credal set width for RS-NN on iD vs. OoD datasets: CIFAR10 vs. SVHN/Intel Image, MNIST vs. F-MNIST/K-MNIST and ImageNet vs. ImageNet-O.

| In-distribution (iD) | | Out-of-distribution (OoD) | | | |
|---|---|---|---|---|---|
| CIFAR10 | 0.007 ± 0.044 | SVHN | 0.260 ± 0.322 | Intel Image | 0.587 ± 0.367 |
| MNIST | 0.001 ± 0.013 | F-MNIST | 0.070 ± 0.167 | K-MNIST | 0.103 ± 0.200 |
| ImageNet | 0.238 ± 0.266 | ImageNet-O | 0.272 ± 0.275 | | |

[FIGURE: Figure 5.14. Credal set widths for individual classes of CIFAR-10 dataset. For Correctly Classified samples (left). For Incorrectly Classified samples (right).]

Text in figure: two box-plot charts "Credal set width for Correctly Classified Samples" and "Credal set width for Incorrectly Classified Samples", x-axis: the 10 CIFAR-10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), y-axis: Credal set width 0.0–0.8, with many outlier points plotted above each box.

Figure 5.14: Credal set widths for individual classes of CIFAR-10 dataset. For Correctly Classified samples *(left)*. For Incorrectly Classified samples *(right)*.

are plotted individually as dots or circles. The box plots here are shown for 10,000 samples of CIFAR-10 dataset where most samples within the incorrect classifications have higher credal set widths indicating higher uncertainty in these samples, especially for classes ‘bird’, ‘cat’, ‘deer’, and ‘dog’.

#### 5.3.4.3 Entropy/Credal Set Width Vs. Confidence Score

In this section, we discuss the correlation between uncertainty measures (pignistic entropy, credal set width) and confidence scores.

Fig. 5.15 shows the relationship between the entropy of RS-NN pignistic predictions and the associated confidence levels for the CIFAR-10 (left) and SVHN/Intel Image (right) datasets. Fig. 5.16 illustrates the relationship between credal set width and confidence for the same datasets. The distribution of iD predictions (left) for both tests show a concentration at the top left, indicating high confidence and low entropy or credal set width. Conversely, OoD predictions (middle, right) exhibit a more dispersed pattern.

Entropy, reflecting prediction uncertainty, is quite correlated with confidence, in both iD and OoD tests. In contrast, as it considers the entire set of plausible outcomes within a belief function rather than a single prediction, credal set width better quantifies the degree of epistemic uncertainty inherent to a prediction. As a result, credal set width is less dependent on the concentration of predictions and is more reflective of the overall uncertainty encompassed by the model. Fig. 5.16 shows that, unlike entropy, credal with is clearly not correlated with confidence.

<!-- page: 78 -->

5.3. Experiments                                                                                                                                55

[FIGURE: Figure 5.15. Entropy vs. Confidence score on iD (left) vs. OoD (right) datasets.]

[FIGURE: Figure 5.16. Credal Set Width vs. Confidence score on iD (left) vs. OoD (right) datasets.]

Text in figures: heatmaps, three panels each ("iD: CIFAR10", "OoD: SVHN", "OoD: Intel Image"), x-axis Entropy (Fig. 5.15) or Credal Set Width (Fig. 5.16) from 0.0 to 3.5, y-axis Confidence Score 0.0–1.0, color scale "Log Frequency" 0–8.

Figure 5.15: Entropy vs. Confidence score on iD (left) vs. OoD (right) datasets. For CIFAR-10, most predictions are concentrated top left of the plot indicating lower entropy and higher confidence in the predictions. For SVHN and Intel Image datasets, predictions are more distributed.

Figure 5.16: Credal Set Width vs. Confidence score on iD (left) vs. OoD (right) datasets. For CIFAR-10, confidence scores are high and credal set width is small. For SVHN and Intel Image datasets, credal set width varies for each prediction and is less reliant on confidence score.

### 5.3.5 Scalability To Large-Scale Architectures

Tab. 5.7 shows the scalability of RS-NN to larger model architectures and its ability to leverage transfer learning. RS-NN outperforms standard CNNs across various large-scale model architectures, including WideResNet28-10 (WRN-28-10), VGG16, InceptionV3 (IncV3), EfficientNetB2 (ENetB2), and Vision Transformer (ViT-Base-16), highlighting its versatility and ease in adopting different architectures, and the generality of the random-set concept. Notably, using a pre-trained ResNet50 (Pre-trained R50) model with ImageNet weights, RS-NN achieves higher accuracy on CIFAR-10 compared to using only the architecture (no pre-trained weights).

<!-- page: 79 -->

56                                                                   Chapter 5. Random-Set Neural Networks

Table 5.7: Adaptability to large-scale model architectures with test accuracy (%) and parameters (in million) reported on CIFAR10.

| | Model | Pre-trained R50 | WRN-28-10 | VGG16 | IncepV3 | ENetB2 | ViT-Base |
|---|---|---|---|---|---|---|---|
| Test acc. (%) | RS-NN | 94.42 | 93.58 | 87.87 | 78.24 | 92.10 | 86.75 |
| | CNN | 94.38 | 92.79 | 84.14 | 76.89 | 90.02 | **87.21** |
| Params (M) | RS-NN | 2.69 | 37.0 | 15.12 | 31.22 | 7.72 | 9.53 |
| | CNN | 2.62 | 36.7 | 15.11 | 31.21 | 7.71 | 9.52 |

### 5.3.6 Overcoming the Overconfidence Problem in CNNs

**Accuracy.** RS-NN consistently achieves higher accuracy than standard CNN (ResNet50) on all datasets as shown in Tab. 5.3. This appears to attest that, as RS-NN uses a random-set framework which does not require prior assumptions and is more data driven, it can better adapt and capture the inherent complexity of the data (as sets), contributing to its superior performance in test accuracy across various datasets (Tab. 5.3). The training hyperparameters for RS-NN and CNN are the same, since the training procedure is quite similar.

Table 5.8: CNN fails to perform well when tested on an noisy (rotated) sample of MNIST test data. The predicted results show how a standard CNN predicts the wrong class with a high confidence score (99.95%), while the RS-NN model predicts the correct class with 49.7% confidence and a high entropy of 2.1626.

True Label = ‘8’

| CNN Predictions | | RS-NN Predictions Belief values | | RS-NN Predictions Mass values | | RS-NN Predictions Pignistic Probability | |
|---|---|---|---|---|---|---|---|
| Class 6 | 0.9995 | {'6', '4', '8'} | 0.7853 | {'6', '8'} | 0.2079 | 8 | 0.4978 |
| Class 5 | 0.0002 | {'6', '8', '1'} | 0.7150 | {'9', '8', '1'} | 0.1999 | 6 | 0.2294 |
| Class 8 | 0.0001 | {'6', '8'} | 0.6357 | {'8'} | 0.1959 | 9 | 0.1002 |
| Class 0 | 1.4e-05 | {'9', '8'} | 0.5529 | {'8', '3'} | 0.0961 | 3 | 0.0502 |
| Class 4 | 1.1e-06 | {'8', '3'} | 0.4092 | {'6'} | 0.05147 | 4 | 0.0459 |
| Entropy | 0.0061 | Entropy | 2.1626 | Credal set width | 0.582 | | |

[FIGURE: Figure 5.17. Confidence scores for Incorrectly Classified samples of RS-NN and CNN.]

Text in figure: histogram/density plot "Confidence scores: CNN vs. RS-NN", x-axis 0.0–1.0, y-axis "Frequency" 0.0–3.0; legend: Incorrectly Classified CNN (red), Incorrectly Classified RS-NN (green).

Figure 5.17: Confidence scores for *Incorrectly Classified samples* of RS-NN and CNN

**Confidence.** We further analyse how RS-NN overcomes the overconfidence problem in CNNs. Tab. 5.8 shows an noisy example of a rotated MNIST image with a true label ‘8’. The standard

<!-- page: 80 -->

5.3. Experiments                                                                                       57

CNN makes an incorrect prediction (‘6’) with 99.95% confidence and a low entropy of 0.0061, highlighting a key limitation of relying solely on confidence scores and the entropy of predicted probabilities. RS-NN provides a correct prediction (class ‘8’) with a confidence of 49.7% and pignistic entropy of 2.1626 and a credal set width of 0.482. Crucially, the RS-NN's prediction process considers more than just the predicted class, taking into account both the confidence of the pignistic probability and the entropy. In this example, despite predicting the correct class (‘8’), the RS-NN demonstrates a low confidence (49.7%) and high entropy (2.1626). This holistic approach provides a more nuanced and reliable understanding of the model's uncertainty.

In Fig. 5.17, we show how a standard CNN has high confidence for incorrectly classified samples whereas RS-NN exhibits lower confidence for incorrectly classified samples.

### 5.3.7 Robustness To Noisy and Rotated Data

We split the MNIST data into training and test sets, train the RS-NN model using the training test, and test the model on noisy and rotated out-of-distribution test data. This is done by adding random noise to the test set of images to obtain noisy data and rotating MNIST images with random degrees of rotation between 0 and 360.

Table 5.9: CNN fails to perform well when tested on noisy and rotated samples of MNIST test data. The predicted results show how a standard CNN predicts the wrong class with a high confidence score, whereas the RS-NN model predicts the right class with varying confidence scores.

True Label = 2

| CNN Predictions | | RS-NN Predictions Belief values | | RS-NN Predictions Mass values | | RS-NN Predictions Pignistic | |
|---|---|---|---|---|---|---|---|
| Class 0 | 0.628 | {'2'} | 0.985 | {'2'} | 0.982 | 2 | 0.982 |
| Class 2 | 0.232 | {'2', '0', '1'} | 0.981 | {'0', '8'} | 0.009 | 8 | 0.007 |
| Class 3 | 0.117 | {'2', '1'} | 0.980 | {'7', '0', '1'} | 0.002 | 0 | 0.100 |
| Class 8 | 0.015 | {'2', '4'} | 0.979 | {'7', '8'} | 0.002 | 3 | 0.004 |

True Label = 3

| CNN Predictions | | RS-NN Predictions Belief values | | RS-NN Predictions Mass values | | RS-NN Predictions Pignistic | |
|---|---|---|---|---|---|---|---|
| Class 8 | 0.969 | {'3', '5'} | 0.772 | {'3'} | 0.361 | 3 | 0.427 |
| Class 5 | 0.018 | {'6', '3'} | 0.637 | {'7', '8'} | 0.134 | 8 | 0.205 |
| Class 9 | 0.006 | {'6', '3', '5'} | 0.620 | {'0', '8'} | 0.104 | 5 | 0.115 |
| Class 2 | 0.003 | {'3'} | 0.540 | {'8'} | 0.084 | 7 | 0.080 |

True Label = 1

| CNN Predictions | | RS-NN Predictions Belief values | | RS-NN Predictions Mass values | | RS-NN Predictions Pignistic | |
|---|---|---|---|---|---|---|---|
| Class 2 | 1.0 | {'2', '1'} | 0.999 | {'1'} | 0.556 | 1 | 0.566 |
| Class 1 | 3.39e-08 | {'1', '9'} | 0.958 | {'2'} | 0.423 | 2 | 0.423 |
| Class 6 | 1.03e-10 | {'1'} | 0.924 | {'1', '9'} | 0.020 | 9 | 0.010 |
| Class 3 | 4.92e-11 | {'1', '5'} | 0.825 | {'6'} | 4.31e-05 | 6 | 4.31e-05 |

True Label = 9

| CNN Predictions | | RS-NN Predictions Belief values | | RS-NN Predictions Mass values | | RS-NN Predictions Pignistic | |
|---|---|---|---|---|---|---|---|
| Class 5 | 0.988 | {'7', '5', '9'} | 0.831 | {'7', '9'} | 0.171 | 9 | 0.699 |
| Class 2 | 0.010 | {'7', '9'} | 0.706 | {'3'} | 0.134 | 7 | 0.023 |
| Class 3 | 0.0004 | {'5', '9'} | 0.576 | {'9'} | 0.132 | 5 | 0.004 |
| Class 7 | 0.0002 | {'3', '9'} | 0.558 | {'7', '8'} | 0.102 | 3 | 0.001 |

<!-- page: 81 -->

Tab. 5.9 shows predictions for noisy and rotated noisy MNIST samples. In cases where a standard CNN makes wrong predictions with high confidence scores, Random-Set NN manages to predict the correct class with varying confidences verifying that the model is not overcofident in uncertain cases. For example, a noisy sample with true class '3' has a standard CNN prediction of class '8' with 96.9% confidence, while RS-NN predicts the correct class {'3'} with 42.7% confidence. Similarly, for rotated '9', the standard CNN predicts class '5' with 98.8% confidence whereas RS-NN predicts the correct class {'9'} with 69.9% confidence. For a rotated '1', the standard CNN predicts class '2' with 100% confidence. Tab. 5.10 shows the test accuracies for standard CNN, RS-NN, LB-BNN and ENN at different scales of random noise. RS-NN shows significantly higher test accuracy than other models as the amount of noise added to the test data increases.

Table 5.10: Test accuracies(%) for RS-NN, standard CNN, LB-BNN (Bayesian) and ENN (Ensemble) on noisy samples of MNIST . 'Scale' represents the standard deviation of the normal distribution from which random numbers are being generated for random noise.

| Noise (scale) | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 |
|---|---|---|---|---|---|---|---|
| CNN | 93.40% | 79.08% | 79.15% | 58.33% | 40.19% | 28.15% | 28.59% |
| RS-NN | 96.90% | 85.36% | 85.91 % | 68.33 % | 51.46 % | 37.18 % | 38.05 % |
| LB-BNN | 98.47% | 95.26 % | 80.18% | 61.56% | 43.28% | 31.41% | 24.55 |
| ENN | 97.81% | 90.76% | 75.41% | 58.99% | 45.70% | 36.97% | 31.51 |

Table 5.11: Test accuracies(%) for RS-NN, standard CNN, LB-BNN (Bayesian) and ENN (Ensemble) on Rotated MNIST out-of-distribution (OoD) samples. Rotation angle is random between the values given.

| Rotation (angle) | -180/-120 | -120/-60 | -60/0 | 0/60 | 60/120 | 120/180 | 0/360 |
|---|---|---|---|---|---|---|---|
| CNN | 36.41% | 21.86% | 74.41% | 80.80% | 23.89% | 37.53% | 45.86% |
| RS-NN | 37.84% | 23.54% | 78.44% | 81.46% | 26.31% | 38.48% | 47.71% |
| LB-BNN | 37.56% | 20.19% | 75.12% | 77.67% | 23.18% | 37.83% | 46.07 |
| ENN | 36.40% | 19.43% | 71.70% | 78.59% | 18.70% | 36.38% | 44.14 |

[FIGURE: Figure 5.18: Entropy distribution of RS-NN on CIFAR-10, Noisy CIFAR-10, and Rotated CIFAR-10]

Text in figure: three histogram/density plots side by side, each with legend "Correctly Classified" and "Incorrectly Classified". X-axis labels (left to right): "Entropy: CIFAR10", "Entropy: Noisy CIFAR10", "Entropy: Rotated CIFAR10". Y-axis unlabeled, ranging 0 to 4.

The test accuracies for standard CNN, RS-NN, LB-BNN and ENN on Rotated MNIST images are shown in Tab. 5.11. The samples are randomly rotated every 60 degrees, -180◦ to -120◦ , -120◦ to -60◦ , -60◦ to 0◦ , etc. A fully random rotation between 0◦ and 360◦ also shows higher test accuracy for RS-NN at 47.71% when compared to standard CNN with test accuracy 45.86%.

Fig. 5.18 displays the entropy distribution for correctly and incorrectly classified samples of CIFAR-10, including in-distribution, noisy, and rotated images. Higher entropy is observed for incorrectly classified predictions across all three cases. A distribution of confidence scores for

<!-- page: 82 -->

[FIGURE: Figure 5.19: Confidence scores of RS-NN on CIFAR-10, Noisy CIFAR-10, and Rotated CIFAR-10]

Text in figure: three histogram/density plots side by side, each with legend "Incorrectly Classified" and "Correctly Classified". X-axis labels (left to right): "Confidence scores: CIFAR10", "Confidence scores: Noisy CIFAR10", "Confidence scores: Rotated CIFAR10". Y-axis ranging 0.0 to 12.5.

RS-NN on the same noisy and rotated experiments are shown in Fig. 5.19 for both incorrectly classified and correctly classified samples.

#### 5.3.8 Robustness To Adversarial Attacks

We conducted experiments on adversarial attacks using the well-known Fast Gradient Sign Method (FGSM) (Goodfellow et al., 2014). FGSM is a popular approach for generating adversarial examples by perturbing input images based on the sign of the gradient of the loss function with respect to the input. Mathematically, the perturbed image x′ is computed as

$$
x' = x + \epsilon \cdot \text{sign}(\nabla_x J(\theta, x, y)),
$$

(5.6)

where x is the original input image, ϵ (epsilon) is a small scalar representing the magnitude of the perturbation, J is the loss function, θ are the model parameters, and y is the true label of the input image.

[FIGURE: Figure 5.20: Examples of perturbed images generated using FGSM adversarial attacks on the MNIST dataset for different epsilon values. Epsilon values range from 0 to 0.05.]

Text in figure: two rows of paired "Original"/"Perturbed" MNIST digit '3' images, each pair labeled with an epsilon value: "Epsilon: 0", "Epsilon: 0.01", "Epsilon: 0.02" (top row); "Epsilon: 0.03", "Epsilon: 0.04", "Epsilon: 0.05" (bottom row).

In our experiments, we applied FGSM adversarial attacks on the MNIST dataset for standard CNN, Random-Set NN (RS-NN), LB-BNN (Bayesian) and ENN (Ensemble) models. This involved perturbing images from the MNIST dataset with noise generated using FGSM based on

<!-- page: 83 -->

the gradient of the loss function (namely, the cross entropy loss for CNN and the $\mathcal{L}_{B-RS}$ loss, Sec. 5.2.3, Eq. (5.3), for RS-NN).

Fig. 5.20 shows examples of perturbed images generated using FSGM adversarial attacks applied to the MNIST dataset for various epsilon values ranging from 0 to 0.05.

Table 5.12: Test accuracies of CNN, RS-NN, LB-BNN and ENN models under FGSM adversarial attacks on MNIST and CIFAR-10 dataset for different epsilon values. Epsilon values range from 0 to 0.05.

Epsilon (ϵ)

| Dataset | Model | 0 | 0.005 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 |
|---|---|---|---|---|---|---|---|---|
| MNIST | CNN | 99.12 | 98.25 | 94.82 | 72.62 | 49.75 | 38.08 | 32.43 |
| MNIST | RS-NN | 99.71 | 98.46 | 95.84 | 91.90 | 90.62 | 90.10 | 89.72 |
| MNIST | LB-BNN | 99.58 | 99.07 | 98.64 | 97.15 | 80.51 | 47.65 | 34.25 |
| MNIST | ENN | 99.07 | 98.56 | 92.98 | 51.51 | 35.04 | 27.03 | 9.47 |
| CIFAR-10 | CNN | 92.08 | 41.54 | 20.88 | 9.18 | 5.81 | 4.43 | 4.05 |
| CIFAR-10 | RS-NN | 93.53 | 63.42 | 61.73 | 61.67 | 61.53 | 61.12 | 60.35 |
| CIFAR-10 | LB-BNN | 89.95 | 23.95 | 10.54 | 6.17 | 5.96 | 6.26 | 6.47 |
| CIFAR-10 | ENN | 91.55 | 62.29 | 42.64 | 24.12 | 16.39 | 12.78 | 11.20 |

(Test acc. (%) for all rows above.)

Subsequently, we evaluated the models' predictions on these perturbed images and computed their test accuracies. Tab. 5.12 presents the test accuracies of CNN, RS-NN, LB-BNN and ENN models under FGSM adversarial attacks on the MNIST dataset for different values of ϵ. For CIFAR-10, RS-NN demonstrates higher robustness to the attack compared to all other models with increased perturbations, while for MNIST, LB-BNN has higher accuracy at lower ϵ values but drops significantly for larger values. RS-NN circumvents the FGSM attack and shows consistent accuracy values for higher ϵ. This is because FGSM for a given input image is dependent on the gradient of the loss, whereas RS-NN makes precise correct predictions with loss/gradient zero and is very confident about these predictions. As a result, despite perturbations to the input image, RS-NN consistently classifies it correctly across all tested values of ϵ.

Table 5.13: Test accuracies of CNN, RS-NN, LB-BNN and ENN models under PGD adversarial attacks on MNIST and CIFAR-10 datasets with α = 1/255 and number of iterations = 10. Epsilon values range from 0 to 0.05

Epsilon (ϵ)

| Dataset | Model | 0 | 0.005 | 0.01 | 0.02 | 0.03 | 0.04 | 0.05 |
|---|---|---|---|---|---|---|---|---|
| MNIST | CNN | 99.12 | 98.90 | 55.44 | 14.03 | 8.11 | 6.58 | 6.58 |
| MNIST | RS-NN | 99.71 | 99.13 | 93.39 | 91.06 | 89.25 | 89.07 | 89.02 |
| MNIST | LB-BNN | 99.58 | 99.35 | 99.01 | 33.67 | 16.35 | 13.64 | 13.64 |
| MNIST | ENN | 99.07 | 98.43 | 78.09 | 20.64 | 9.94 | 3.78 | 0.93 |
| CIFAR-10 | CNN | 92.08 | 23.82 | 2.47 | 0.04 | 0 | 0 | 0 |
| CIFAR-10 | RS-NN | 93.53 | 60.23 | 59.98 | 59.97 | 59.97 | 59.97 | 59.97 |
| CIFAR-10 | LB-BNN | 89.95 | 6.28 | 0.51 | 0.55 | 0.59 | 0.59 | 0.59 |
| CIFAR-10 | ENN | 91.55 | 33.95 | 4.40 | 0.15 | 0.02 | 0 | 0 |

(Test acc. (%) for all rows above.)

Additionally, we conducted experiments using the Projected Gradient Descent (PGD) adversarial attack (Madry et al., 2017), which is a more iterative and stronger attack compared to FGSM. PGD generates adversarial examples by iteratively perturbing the input image in the direction of the gradient of the loss function, followed by a projection step to ensure that the perturbation

<!-- page: 84 -->

stays within a predefined range, typically defined by a norm ball around the original image. Mathematically, the perturbed image x′ is computed as follows:

$$
x^{(0)} = x, \quad x^{(t+1)} = \text{Proj}_{\mathcal{B}(x,\epsilon)}\left(x^{(t)} + \alpha \cdot \text{sign}(\nabla_x J(\theta, x^{(t)}, y))\right),
$$

(5.7)

where x^(t) represents the image at the t-th iteration, α is the step size, ϵ is the maximum allowable perturbation (i.e., the size of the B(x, ϵ) ball), and Proj denotes the projection operation that ensures the perturbed image x′ stays within the ϵ-ball around the original image x:

$$
\mathcal{B}(x, \epsilon) = \{x' : \|x' - x\| \leq \epsilon\}.
$$

(5.8)

After a number of iterations, typically denoted as T , the final perturbed image x′ is obtained. This iterative process makes PGD a more powerful adversarial attack compared to FGSM. Tab. 5.13 presents the test accuracies of CNN, RS-NN, LB-BNN and ENN models under the PGD adversarial attack on MNIST and CIFAR-10 datasets for different values of ϵ. On MNIST, LB-BNN performs well for ϵ = 0.005 and ϵ = 0.01, but CNN, LB-BNN and ENN suffer significant decreases in accuracy at higher ϵ values. RS-NN performs better at higher ϵ values. On CIFAR-10, RS-NN significantly outperforms all models at all ϵ values, while the other models show a significant drop in performance, even at ϵ = 0.005. As explained earlier, RS-NN makes precise predictions with gradient zero and, therefore, is unaffected by PGD.

#### 5.3.9 Application To Text Classification

The random-set approach can be applied on any classification task. In this section, we detail experiments performed on text classification.

**Dataset.** We chose the BBC text dataset (Greene and Cunningham, 2006), which consists of various news categories such as tech, business, sport, and entertainment, and used this data for training our model. The task is to classify the given text into one of these categories. The dataset is structured with two columns: category and text, where the category is the label, and the text is the content to be classified. The text data will be preprocessed and fed into the model to predict the category of each text.

**Model.** To train our model, we leveraged a pre-trained BERT model available on TensorFlow Hub. Specifically, we used the small BERT (L−4H −512A −8) model, which is a lightweight version of BERT. The model is designed to take text input, preprocess it with BERT's preprocessing layer, pass it through BERT's encoder to generate embeddings, and then use a dropout layer. The final layer is a fully-connected layer with sigmoid activation for the RS-NN BERT classifier (RS-NN BERT), and a fully-connected layer with softmax activation for the standard BERT classifier (CNN BERT).

**Training.** We trained these models on the BBC text dataset, fine-tuning the BERT model as part of the training process. Both models were trained for 10 epochs using Adam optimizer, a batch size of 32, and a learning rate of 3e-5. RS-NN BERT has all the sets of classes excluding the null set and full set (2^5 = 32 - 2 = 30 classes) and CNN BERT has the 5 original classes.

**Out-of-distribution detection.** For OoD detection, we use the Emotion Detection from Text (Seyeditabari et al., 2018) dataset which contains tweets annotated with emotional labels. The

<!-- page: 85 -->

dataset includes three columns: tweetid, sentiment, and content, where sentiment represents the emotion behind each tweet. The dataset includes 13 emotion classes such as anger, fear, joy, love, sadness, and surprise, etc, aiming to identify emotional expressions in text.

Table 5.14: Test accuracy, AUROC, AUPRC, iD vs. OoD entropy for RS-NN BERT and CNN BERT (both fine-tuned on BERT).

| Dataset (iD) | Model | Test Acc. (%) (↑) | iD Entropy (↓) | Emotion Detection (OoD) AUROC (↑) | Emotion Detection (OoD) AUPRC (↑) | Emotion Detection (OoD) Entropy (↑) |
|---|---|---|---|---|---|---|
| BBC Text (iD) | RS-NN BERT | 96.85 | 0.541 ± 0.196 | 95.19 | 95.93 | 1.510 ± 0.611 |
| BBC Text (iD) | CNN BERT | 94.15 | 0.027 ± 0.125 | 56.71 | 57.54 | 0.059 ± 0.191 |

**Experimental results.** In Tab. 5.14 below, we show the test accuracy, out-of-distribution (OoD) metrics (AUROC, AUPRC), and the in-distribution (iD) vs. OoD entropy for RS-NN BERT and CNN BERT. RS-NN achieves higher overall performance with a significantly higher AUROC and AUPRC scores, highlighting the efficiency of the model at differentiating between iD and OoD samples. RS-NN has higher OoD entropy than CNN, but also has higher iD entropy than CNN, which indicates that the uncertainty in predictions is higher as it is a small dataset.

#### 5.3.10 Ablation Studies

In this section, we will address the following questions based on our experimental findings:

- **Q1:** Why are most models not able to differentiate between ImageNet and ImageNet-O in terms of entropy?
- **Q2:** What is the importance of the mass regularizers in the loss function $\mathcal{L}_{RS}$ (Sec. 5.2.3)? Why is it important to properly tune the regularization parameters α and β, and what impact does this have on the model's performance?
- **Q3:** What are the effects of budgeting on RS-NN? How was the number of budgeted focal sets K chosen? How does budgeted RS-NN differ from standard RS-NN with all the subsets in the power set?
- **Q4:** How does UMAP measure as a faster alternative to t-SNE for budgeting in RS-NN? How can the budgeting procedure be adapted for continuous data streams?

##### 5.3.10.1 ImageNet Vs. ImageNet-O

In Tab. 5.5, the clear separation between iD and OoD entropy is evident for RS-NN, yet for ImageNet vs. ImageNet-O, all other models struggle to distinguish between the iD vs. OoD entropy and the OoD dataset almost falls within the standard deviation of the iD samples.

Also, in Tab. 5.6, the credal set widths for CIFAR-10 vs. SVHN/Intel Image and MNIST vs. F-MNIST/K-MNIST are distinct, but ImageNet vs. ImageNet-O is not too different.

To better understand this, it is important to consider how ImageNet-O is generated. ImageNet-O is a dataset of adversarially filtered examples for ImageNet out-of-distribution detectors. It is created by removing all the ImageNet-1K samples from the full ImageNet-22K dataset. The remaining samples, which do not belong to ImageNet-1K classes, are classified by a trained model. The samples classified by the model as ImageNet-1K classes with high confidence becomes

<!-- page: 86 -->

ImageNet-O. Hence, in general, it is difficult for models to make the iD vs. OoD distinction as evident by uncertainty measures in Tab. 5.5.

We conducted experiments on Credal Set Width and Pignistic Entropy measures of RS-NN using a ViT-B-16 (Vision Transformer) backbone, as shown in Tab. 5.15. The pignistic entropy and credal set width show good distinction between iD and OoD measures, unlike the uncertainty measures from other baseline models in Tab. 5.5.

Table 5.15: Credal set width and entropy for RS-NN using ViT-B-16 model on ImageNet vs. ImageNet-O datasets.

| Model | Dataset | Credal Set Width | Pignistic Entropy | Softmax Entropy (CNN) |
|---|---|---|---|---|
| RS-NN | ImageNet (iD) (↓) | 0.1082 ± 0.1926 | 2.7401 ± 2.3678 | 2.3442 ± 1.2243 |
| RS-NN | ImageNet-O (OoD) (↑) | 0.1948 ± 0.2455 | 4.4238 ± 2.5744 | 2.8619 ± 1.5884 |

This is specifically due to the peculiar relation between ImageNet and ImageNet-O, and not a general problem with the models not being able to distinguish samples when they belong to the same image distribution.

To support our claim, we conducted experiments using CIFAR-10 (iD) vs. CIFAR-100 (OoD) as shown in Tab. 5.16 below, and the results indicate that our model distinguishes between these two datasets well, as evident through the AUROC, AUPRC, entropy and credal set width. Therefore, the issue seems to be specific to ImageNet and ImageNet-O, likely due to the class imbalance in ImageNet. As per the general trend for ImageNet in Tab. 5.5, all models behave uncertainly for higher number of classes which makes the difference between iD and OoD less extreme. Although, RS-NN still performs better than other models on ImageNet.

Table 5.16: OoD detection and uncertainty estimation performance for iD vs. OoD dataset: CIFAR-10 vs. CIFAR-100.

| Dataset | Model | In-distribution Entropy (↓) | Credal Set Width (↓) | CIFAR-100 AUROC (↑) | CIFAR-100 AUPRC (↑) | CIFAR-100 Entropy (↑) | CIFAR-100 Credal Set Width (↑) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | RS-NN | 0.0802 ± 0.297 | 0.0061 ± 0.039 | 88.01 | 84.93 | 0.5778 ± 0.729 | 0.0721 ± 0.165 |

##### 5.3.10.2 Ablation Study On Hyperparameters α and β

The regularization serves the purpose of ensuring that our model generates valid belief functions, which are constrained by maintaining a sum of masses equal to 1 and ensuring non-negativity. These terms are designed to penalize deviations from valid belief functions. However, it is crucial not to assign too much weight to this term, as excessively penalizing deviations may hinder the model's ability to accurately classify data points. For e.g., in a Variational Auto Encoder (VAE), if we assign too much weight to the KL divergence term in the loss, the model may prioritize fitting the latent distribution at the expense of reconstructing the input data accurately. This imbalance can lead to poor reconstruction quality and suboptimal performance on downstream tasks.

Hence, it is essential to properly tune the values of α and β to ensure that these regularization terms play a meaningful role in the training. The ablation study on hyperparameters is conducted to examine the impact of α and β on the model's accuracy. It demonstrates that small values suffice for these parameters.

<!-- page: 87 -->

In Fig. 5.21, we show the test accuracies for different values of hyperparameters α and β in $\mathcal{L}_{B-RS}$ loss function (Eq. 5.3). Hyperparameters α and β adjusts the relative significance of the regularization terms $M_r$ and $M_s$ respectively in $\mathcal{L}_{B-RS}$ loss. The test accuracies are calculated for CIFAR-10 dataset with a fixed number of focal sets K = 20 and varying α (blue) and β (red) values, α/β = [0.001, 0.005, 0.006, 0.009, 0.01, 0.015, 0.020, 0.025, 0.03, 0.04, 0.05]. Test accuracy is the highest when α and β equals 1e − 3.

The shape of the tuning curve in Fig. 5.21 shows an interesting asymmetric pattern in how accuracy responds to changes in the regularization parameters α and β. In the low-regularization regime (α, β ∈ [0, 0.001]), accuracy increases from approximately 92.5% to 93.5%. However, beyond the point α = β = 0.001, accuracy drops sharply and steadily as α or β increase further, reaching significantly lower performance by 0.05. This steep decline suggests that excessive regularization overly constrains the space of feasible belief functions. This also reinforces the idea that while α and β are necessary for producing valid beliefs, they must be used sparingly, and fine-tuning them can have a measurable impact on classification performance.

[FIGURE: Figure 5.21: Test accuracies of RS-NN on the CIFAR-10 dataset using ResNet50, for a fixed K = 20 and different values of hyperparameters α and β in the loss function.]

Text in figure: line plot, y-axis "Test Accuracy" ranging 91.0 to 94.0, x-axis "Hyperparameters α & β" ranging 0.00 to 0.05. Annotation: "Max Accuracy: 93.53" and "α = β = 0.001". Legend: "α" (blue), "β" (red).

In our experiments across various datasets and architectures, we found that a value of 1e − 3 for the hyperparameters yields satisfactory results. This includes architectures ranging from ResNet-50 to Vision Transformers (ViT-Base-16), and datasets ranging from MNIST (≈ 60,000 images of 10 classes) to ImageNet (≈ 1.1M images of 1000 classes). While conducting a parameter search for each dataset could potentially lead to further optimization, it is worth noting that, in many cases, this step can be omitted without sacrificing performance significantly. For further optimization one can, of course, perform a tailored parameter search per dataset, but this is not quite necessary.

**An alternative loss with valid belief functions.** A straightforward way of enforcing the positivity of the masses is to apply softmax over the masses computed in the BCE loss. This ensures that the masses are non-negative and sum to one. After obtaining the softmaxed masses, one can compute the belief functions from these normalized masses and minimize the loss between this computed belief and the original unnormalized belief.

The random set loss $\mathcal{L}_{RS}$ now becomes,

$$
\mathcal{L}_{RS} = \mathcal{L}_{BCE} + \mathcal{L}_{BCE_{norm}},
$$

<!-- page: 88 -->

where $\mathcal{L}_{BCE}$ is the BCE loss between belief function logits and ground truth, and $\mathcal{L}_{BCE_{norm}}$ is the BCE loss between the normalized belief function logits reconstructed from mass logits that have been softmaxed.

We implemented this simple method on ResNet50 RS-NN on the CIFAR-10 dataset and obtained an accuracy of 92.47%. This is quite close to our original accuracy of 93.53% with the mass regularizations. This mirrors results in the literature showing that soft constraints work as well as hard ones in practice (Márquez-Neila et al., 2017).

##### 5.3.10.3 Ablation Study On the Number of Focal Sets

[FIGURE: Figure 5.22: Ablation study on number of non-singleton focal sets K on CIFAR-10 dataset using ViT-Base-16 (with α = β = 1e − 3). The maximum value of K can be 1013 for 10 classes (after excluding the singletons and empty set).]

Text in figure: line plot, y-axis "Accuracy" ranging 70.0 to 90.0, x-axis "K" with values 0, 20, 60, 100, 500, 1013.

The number of non-singleton focal sets K to be budgeted is a hyperparameter and needs to be studied. A smaller value of K can lead to more similar results to classical classification while a larger value of K can increase the complexity. Therefore, we conducted an ablation study on K on the CIFAR-10 dataset. We found that a small value of K (comparable to the number of classes) works best and performs better than K = 0 (when there are no non-singleton focal sets) (Fig. 5.22). shows a clear peak in performance at a moderate number of focal sets (K=20), beyond which the test accuracy drops. This behaviour suggests that a limited number of informative non-singleton focal sets is sufficient to capture useful uncertainty while preserving model generalization. As K increases, the model may overfit to complex or overly granular belief assignments, increasing computational complexity without adding meaningful discriminatory power.

Also, using set prediction along with the proposed budgeting algorithm not only helps induce uncertainty quantification but also improves the performance of the model. Note that performance comparison was made in terms of accuracy. Smet's Pignistic Transform (Smets, 2005) was used to compute class-wise probabilities from the predicted belief function. Fig. 5.22 shows an ablation study on different number of focal sets K for CIFAR-10 on the Vision-Transformer (ViT-Base-16) model with α = β = 1e − 3.

<!-- page: 89 -->

To further support our claim, we compare a budgeted RS-NN with standard RS-NN (full 2^N sets) on the CIFAR-10 datasets using ResNet50 as the backbone. In Tabs. 5.17 and 5.18 below, we report the test accuracy, OoD detection metrics (AUROC, AUPRC), pignistic entropy and credal set width for the standard RS-NN vs. budgeted RS-NN. The standard RS-NN has 1024 (2^10) sets since CIFAR-10 has 10 classes, and the budgeted RS-NN has K = 20 focal (non-singleton) sets, so 10 + 20 = 30 input sets. Tab. 5.17 shows that budgeted RS-NN performs better than the standard model, especially iD vs. OoD entropy, and AUROC and AUPRC scores.

Table 5.17: OoD detection performance: Comparison of accuracy, AUROC and AUPRC for standard RS-NN vs. budgeted RS-NN on the CIFAR-10 dataset.

| Dataset | Model | Test accuracy (%) (↑) | ECE (↓) | SVHN AUROC (↑) | SVHN AUPRC (↑) | Intel Image AUROC (↑) | Intel Image AUPRC (↑) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | Standard RS-NN | 92.66 | 0.0501 | 93.39 | 91.38 | 95.84 | 89.33 |
| CIFAR-10 | Budgeted RS-NN | 93.53 | 0.0484 | 94.91 | 93.72 | 97.39 | 90.27 |

Table 5.18: Uncertainty estimation: Comparison of pignistic entropy and credal set width for standard RS-NN vs. budgeted RS-NN on the CIFAR-10 dataset.

| Dataset (iD) | Model | Entropy (iD) (↓) | Credal Set Width (iD) (↓) | SVHN Entropy (↑) | SVHN Credal Set Width (↑) | Intel Image Entropy (↑) | Intel Image Credal Set Width (↑) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | Standard RS-NN | 0.286 ± 0.80 | 0.048 ± 0.15 | 1.205 ± 1.20 | 0.408 ± 0.07 | 1.490 ± 0.71 | 0.669 ± 0.21 |
| CIFAR-10 | Budgeted RS-NN | 0.088 ± 0.308 | 0.007 ± 0.044 | 1.132 ± 0.855 | 0.260 ± 0.322 | 1.517 ± 0.740 | 0.587 ± 0.367 |

This shows that while, in theory, using the full power set is ideal for uncertainty estimation, in practice, having all those degrees of freedom might make it more difficult for the network to learn. When a model is confronted with an overwhelming number of input sets, it may struggle to identify meaningful patterns amidst the noise created by less relevant or redundant combinations. This excessive flexibility can hinder the network's ability to converge effectively, as it may become trapped in local minima or overfit to the training data. This can dilute the model's capacity to generalize well to unseen data, thereby complicating the learning of the underlying relationships between features and the set structure of the data.

##### 5.3.10.4 On the Feasibility of Budgeting of Sets

Tabs. 5.19 and 5.20 show that replacing t-SNE with UMAP for budgeting in the RS-NN model yields comparable performance in terms of test accuracy, out-of-distribution (OoD) detection, and uncertainty estimation. Both t-SNE and UMAP are capable of embedding data in a 3D space, with UMAP employing a faster algorithm that utilizes five nearest neighbors and a minimum distance of 0.9. This approach ensures that the integrity of the data structure is maintained while significantly reducing computational costs. UMAP offers an efficient alternative without compromising the model's effectiveness. To make the generation of embeddings for budgeting of focal sets more efficient, we can utilize faster alternatives like UMAP instead of t-SNE, without compromising the overall model performance. We chose t-SNE for our main budgeting experiments as it better preserves local neighbor structure (Wattenberg et al., 2016), often resulting in tighter and more visually distinct class clusters.

<!-- page: 90 -->

Table 5.19: Test accuracy and OoD detection (AUROC, AUPRC) results on RS-NN where budgeting is done using t-SNE vs. budgeting done on UMAP.

| Dataset | Model | Test accuracy (%) (↑) | ECE (↓) | SVHN AUROC (↑) | SVHN AUPRC (↑) | Intel Image AUROC (↑) | Intel Image AUPRC (↑) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | RS-NN (t-SNE) | 93.53 | 0.0484 | 94.91 | 93.72 | 97.39 | 90.27 |
| CIFAR-10 | RS-NN (UMAP) | 92.97 | 0.0482 | 94.31 | 92.46 | 96.22 | 89.66 |

Table 5.20: Entropy and credal set width results on RS-NN where budgeting is done using t-SNE vs. budgeting done on UMAP. The goal is to minimize both metrics for in-distribution (iD) data while increasing them for out-of-distribution (OoD) data.

| Dataset | Model | Entropy (↓) | Credal Set Width (↓) | SVHN Entropy (↑) | SVHN Credal Set Width (↑) | Intel Image Entropy (↑) | Intel Image Credal Set Width (↑) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | RS-NN (t-SNE) | 0.088 ± 0.308 | 0.007 ± 0.044 | 1.132 ± 0.855 | 0.260 ± 0.322 | 1.517 ± 0.740 | 0.587 ± 0.367 |
| CIFAR-10 | RS-NN (UMAP) | 0.082 ± 0.305 | 0.007 ± 0.047 | 1.119 ± 0.887 | 0.341 ± 0.374 | 1.423 ± 0.762 | 0.582 ± 0.402 |

### 5.4 Discussion and Implications

This chapter proposes a novel *Random-Set Neural Network (RS-NN)* for uncertainty estimation in classification predicting belief functions. This random-set representation is a foundational approach that acts as a versatile wrapper, applicable to any model architecture and classification task (e.g, text). This concept, along with budgeting for optimal selection of sets, is unprecedented. RS-NN outperforms both state-of-the-art uncertainty estimation models and standard CNNs in terms of predictive performance (**accuracy** and **calibration**), **out-of-distribution (OoD) detection**, and **adversarial robustness**. It provides **reliable uncertainty** quantification and **scales effectively** to large architectures and datasets.

What distinguishes RS-NN, however, is not just empirical superiority but the epistemological stance embedded in its design. These results are not incidental; they emerge directly from the fact that RS-NN treats prediction as inference over *sets* of outcomes. **This reflects the central claim of this thesis:** that epistemic uncertainty must be captured through second-order frameworks which can represent both partial knowledge and ambiguity in a way that other models cannot. RS-NN achieves this by modifying the network's output space to predict belief over sets and by deriving pignistic probabilities for decision-making. This makes the abstract idea of epistemic modeling tangible, producing a concrete, scalable algorithm that generalizes across tasks and architectures. The proposed *budgeting technique* enables set-valued learning to be computationally feasible, selecting informative class subsets without incurring exponential complexity. In doing so, it exemplifies how theory-driven modeling, grounded in random set theory and belief functions, can lead to practical advances in machine learning under uncertainty.

Building on the success of Random-Set Neural Networks (RS-NNs) in classification, applications of the random set framework to Large Language Models (LLMs) are demonstrated in Part IV, with the development of Random-Set Large Language Models (RS-LLMs) for text generation presented in Chapter 9, alongside other practical applications such as weather classification for autonomous racing (Chapter 10).

<!-- page: 91 -->

# 6 Credal Set Models

This chapter presents a brief description of credal set models for classification developed collaboratively within the epistemic AI framework. Although a detailed exposition of each model is beyond the scope of this thesis due to word limit constraints, their core characteristics are summarized here. These co-authored works have been published in Wang et al. (2024c) and Wang et al. (2024b). These models are evaluated in Part III and their overall performance comparison with other approaches are shown in Sec. 11.2. The following sections provide background and a concise description of each model.

Credal sets provide a formalism for representing uncertainty more robustly than traditional probabilistic models. In contrast to Bayesian models, which rely on precise priors, credal sets adopt a more agnostic approach by accommodating a set of plausible probability distributions. This is particularly advantageous when probability estimates are based on incomplete or conflicting sources, such as in medical diagnosis or risk assessment (Cozman, 2000). *Credal networks*, for example, generalize Bayesian networks by allowing imprecise conditional probability tables, leading to more cautious and reliable inferences in high-stakes domains. By capturing a range of admissible probabilities rather than a single distribution, credal sets help mitigate overconfidence in decision-making.

Models that generate *credal sets* (Levi, 1980; Zaffalon and Fagiuoli, 2003; Cuzzolin, 2010b; Antonucci and Cuzzolin, 2010; Cuzzolin, 2008a) represent uncertainty in predictions by providing a set of plausible outcomes, rather than a single point estimate. A *credal set* (Levi, 1980; Zaffalon and Fagiuoli, 2003; Cuzzolin, 2010b; Antonucci and Cuzzolin, 2010; Cuzzolin, 2008a) is a convex set of probability distributions on the target (class) space. Credal sets can be elicited, for instance, from predicted probability intervals (Wang et al., 2024c; Caprio et al., 2023b) $[\hat{p}(y), \overline{\hat{p}}(y)]$, encoding lower and upper bounds, respectively, to the probabilities of each of the classes (in list of classes Y):

$$
\hat{\mathbb{C}r}(y \mid \mathbf{x}, \mathbb{D}) = \{p \in \mathcal{P} \mid \hat{p}(y) \leq p(y) \leq \overline{\hat{p}}(y), \forall y \in \mathbf{Y}\}.
$$

(6.1)

where $\mathcal{P}$ denotes the set of all probability distributions over Y.

A credal set is efficiently represented by its extremal points; their number can vary, depending on the size of the class set and the complexity of the network prediction the credal set represents.

Based on these principles, we introduce two models: Cre-INN and CreDE, each providing a distinct mechanism for constructing and leveraging credal sets in deep learning.

<!-- page: 92 -->

## 6.1 Credal Interval Neural Networks (Cre-INN)

Credal-Set Interval Neural Networks (CreINNs) (Wang et al., 2024c), as shown in Fig. 6.1, retain the fundamental structure of traditional Interval Neural Networks, capturing weight uncertainty through deterministic intervals. CreINNs are designed to predict an upper and a lower probability bound for each class, rather than a single probability value. The probability intervals can define a credal set, facilitating estimating different types of uncertainties associated with predictions.

[FIGURE: Figure 6.1: Illustration of the proposed CreINN model for a three-class classification task.]

Text in figure: block diagram in two panels labeled "Existing INN Structure" and "CreINN Operation". Left panel ("Existing INN Structure"): inputs $[\underline{x}, \overline{x}]$ feeding into a network of nodes shown as deterministic interval vectors $[\underline{a}_1^2, \overline{a}_1^2]$, $[\underline{a}_2^2, \overline{a}_2^2]$, $[\underline{a}_3^2, \overline{a}_3^2]$, with weight/bias intervals $[\underline{w}, \overline{w}]$, $[\underline{b}, \overline{b}]$ constructed by "Interval Center & Radius"; caption "Dataset: interval format: $[\underline{x}, \overline{x}], y) \to ([\underline{x}, \overline{x}], y)$" and "standard format: $(x, y) \to ([x, x], y)$". Right panel ("CreINN Operation"): flow "Interval SoftMax Activation" → probability interval vectors $[\underline{p}_1, \overline{p}_1]$, $[\underline{p}_2, \overline{p}_2]$, $[\underline{p}_3, \overline{p}_3]$ → "Reduce Redundancy" → reachable probability interval vectors $[\underline{p}_1^*, \overline{p}_1^*]$, $[\underline{p}_2^*, \overline{p}_2^*]$, $[\underline{p}_3^*, \overline{p}_3^*]$ → a 2D probability simplex triangle labeled "Class 1", "Class 2", "Class 3" showing the credal set $\hat{\mathbb{C}r}$ for uncertainty estimation and the intersection probability $p_{int}$ for class prediction. Bottom: "Inference / Training Procedure: minimize CE$(p_{int}, y)$ s.t. $W_r, b_r \geq 0$".

CreINN introduces a novel *Interval SoftMax activation* that converts output interval scores

$$
[\underline{a}^L, \overline{a}^L] = \{[\underline{a}^L_{c_i}, \overline{a}^L_{c_i}]\}_{i=1}^N,
$$

(6.2)

where N is the number of classes and $[\underline{a}^L_{c_i}, \overline{a}^L_{c_i}]$ denotes the score interval for the $c_i$th class at the final layer L, into valid probability intervals

$$
[\underline{\hat{p}}, \overline{\hat{p}}] = \{[\underline{\hat{p}}_{c_i}, \overline{\hat{p}}_{c_i}]\}_{i=1}^N,
$$

(6.3)

<!-- page: 93 -->

with $[\underline{\hat{p}}_{c_i}, \overline{\hat{p}}_{c_i}]$ representing the predicted probability interval for class $c_i$. These intervals define a credal set

$$
\hat{\mathbb{C}r} = \left\{ p \in \mathcal{P} \mid p_{c_i} \in [\underline{\hat{p}}_{c_i}, \overline{\hat{p}}_{c_i}], \sum_{i=1}^{N} p_{c_i} = 1 \right\},
$$

(6.4)

which is a convex set of probability distributions capturing uncertainty over class assignments.

The Interval SoftMax is given by

$$
\underline{\hat{p}}_{c_i} = \frac{\exp(\underline{a}^L_{c_i})}{\exp(\underline{a}^L_{c_i}) + \sum_{c_j \neq c_i} \exp\left(\frac{\underline{a}^L_{c_j} + \overline{a}^L_{c_j}}{2}\right)}, \quad \overline{\hat{p}}_{c_i} = \frac{\exp(\overline{a}^L_{c_i})}{\exp(\overline{a}^L_{c_i}) + \sum_{c_j \neq c_i} \exp\left(\frac{\underline{a}^L_{c_j} + \overline{a}^L_{c_j}}{2}\right)},
$$

(6.5)

which ensures that the output intervals are valid probabilities, maintain order ($\underline{\hat{p}}_{c_i} \leq \overline{\hat{p}}_{c_i}$), and are differentiable for backpropagation.

CreINN enforces interval constraints on parameters by representing weights and biases as center-radius intervals:

$$
[\underline{W}, \overline{W}] = [W_c - W_r, W_c + W_r], \quad [\underline{b}, \overline{b}] = [b_c - b_r, b_c + b_r],
$$

(6.6)

where $W_c$ and $b_c$ are the center (midpoint) parameters, and $W_r \geq 0$ and $b_r \geq 0$ are the non-negative radii (half-widths) of the intervals, guaranteeing $\underline{W} \leq \overline{W}$ and $\underline{b} \leq \overline{b}$.

To prevent interval explosion in deeper architectures, an *Interval Batch Normalization* method is introduced, which stabilizes the interval propagation. Since the initial probability intervals $[\underline{\hat{p}}, \overline{\hat{p}}]$ can be redundant (i.e., some interval bounds are not achievable by any probability vector in $\hat{\mathbb{C}r}$, CreINN refines these using reachable bounds:

$$
\overline{\hat{p}}^*_{c_i} = \min\left(\overline{\hat{p}}_{c_i}, 1 - \sum_{c_j \neq c_i} \underline{\hat{p}}_{c_j}\right), \quad \underline{\hat{p}}^*_{c_i} = \max\left(\underline{\hat{p}}_{c_i}, 1 - \sum_{c_j \neq c_i} \overline{\hat{p}}_{c_j}\right),
$$

(6.7)

which ensure that for each class $c_i$, the refined interval $[\underline{\hat{p}}^*_{c_i}, \overline{\hat{p}}^*_{c_i}]$ is feasible within the simplex constraint. The resulting credal set formed by these reachable intervals accurately reflects the uncertainty in class probabilities.

Classification decisions can be made by considering intersection probabilities derived from these intervals, and the network is trained by minimizing a cross-entropy loss adapted to the interval-valued outputs subject to these interval constraints.

Experiments on standard multiclass and binary classification tasks demonstrate that the proposed CreINNs can achieve superior or comparable quality of uncertainty estimation compared to variational Bayesian Neural Networks (BNNs) and Deep Ensembles. Furthermore, CreINNs significantly reduce the computational complexity of variational BNNs during inference. Moreover, the effective uncertainty quantification of CreINNs is also verified when the input data are intervals.

<!-- page: 94 -->

## 6.2 Credal Deep Ensembles (CreDE)

Credal Deep Ensembles (CreDEs) (Wang et al., 2024b) (Fig. 6.2) build on the deep ensemble framework by incorporating credal set theory to enhance epistemic uncertainty modeling. Each ensemble member, referred to as a Credal-Set Neural Network (CreNet), is trained to output interval-valued class probabilities. The ensemble's aggregated output defines a credal set over the label space.

Each ensemble member, a Credal-Set Neural Network (CreNet), outputs interval-valued class probabilities defined by lower and upper bounds for each class, denoted as

$$
[\underline{\hat{p}}_{c_i}, \overline{\hat{p}}_{c_i}], \quad i = 1, \ldots, N,
$$

(6.8)

where N is the number of classes. These intervals form a credal set as shown in Eq. 6.1. Training each CreNet involves a distributionally robust optimization (DRO)-inspired loss function, which encourages interval widths to reflect uncertainty due to potential dataset shift. This approach enhances the model's robustness by simulating divergences between training and test distributions during learning.

[FIGURE: Figure 6.2: Comparison between the proposed Credal Deep Ensembles and traditional Deep Ensembles.]

Text in figure: two side-by-side diagrams labeled "Deep Ensembles" and "Credal Deep Ensembles". Left ("Deep Ensembles"): three networks "SNN-1", "SNN-2", "SNN-3" mapping "Model Space" to a triangle labeled "Target Space 𝕐" with vertices A, B, D and points $p_A$, $p_B$, $p_D$, captioned "(Single Probability Distributions)", combined via "Average". Right ("Credal Deep Ensembles"): three networks "CreNet-1", "CreNet-2", "CreNet-3" mapping "Model Space" to a triangle "Target Space 𝕐" with vertices A, B, D, captioned "(Credal Sets Formed by Probability Intervals)", combined via "Aggregate" into a shaded region.

Comparison between the proposed Credal Deep Ensembles and traditional Deep Ensembles. The former aggregate a collection of credal set predictions from CreNets as the final (credal) prediction, whereas the latter average a set of single probability distributions from standard SNNs as the outcome. For e.g., in the probability simplex associated with the target space $\mathbf{Y} = \{A, B, D\}$ (the triangle in the figure), a probability vector $(q_A, q_B, q_D)$ is represented as a single point. For each CreNet, the predicted lower and upper probabilities of each class act as constraints (parallel lines) which determine a credal prediction (in gray).

Extensive evaluation across multiple OoD benchmarks (e.g., CIFAR10/100 vs. SVHN or Tiny-ImageNet, CIFAR10 vs. CIFAR10-C) and architectures (ResNet50, VGG16, ViT Base) shows that CreDEs deliver superior uncertainty estimates. Compared to traditional ensembles and variational BNNs, CreDEs yield lower expected calibration error (ECE) and higher AUROC and AUPRC on OoD data. These results confirm the efficacy of credal set modeling in capturing epistemic uncertainty more faithfully.

In Sec. 11.2, we compare the performance of CreINN and CreDE with all other models in terms of accuracy vs. ECE (Fig. 11.1(b)) and OoD detection scores (Fig. 11.1(a)).

<!-- page: 95 -->

# Part III

# EVALUATING EPISTEMIC PREDICTIONS

<!-- page: 96 -->

<!-- page: 97 -->

# 7 Evaluation under Uncertainty

As mentioned in Sec. 2.2, in classification, it is imperative to account for uncertainty inherent in the predictive process, called predictive uncertainty. It can be represented using the predictive distribution $\hat{p}(y \mid x, \mathbb{D})$, where $y \in \mathbf{Y}$ is a label, $x \in \mathbf{X}$ an input instance, and $\mathbb{D} = \{(x_i, y_i)\}_{i=1}^{N} \in \mathbf{X} \times \mathbf{Y}$ the available training set, N being the number of training instances. In Bayesian models (Buntine and Weigend, 1991; Neal, 2012; Jospin et al., 2022; Kingma and Welling, 2013), this uncertainty is explicitly represented through posterior predictive distributions over the parameter space. In Ensembles (Lakshminarayanan et al., 2017), a predictive distribution is formed by aggregating the individual predictions generated by multiple independently trained models. In Evidential models (Sensoy et al., 2018), instead, predictions are parameters of a Dirichlet posterior in the label space. In deterministic (Mukhoti et al., 2023) models, predictions are point estimates obtained from a final softmax layer, similar to those of standard neural networks (CNN). Finally, in imprecise-probabilistic models (Caprio et al., 2023b; Wang et al., 2024c), predictions correspond to either credal sets (Levi, 1980; Tong et al., 2021) or random sets (Chapter 5), rather than single, precise probability vectors.

**No common evaluation setting exists to date for all these diverse kinds of predictions**, making it difficult for practitioners to consistently evaluate or rank uncertainty models based on their predictive performance.

This chapter reviews the existing literature on the evaluation of uncertainty in machine learning (Sec. 7.1) and examines the forms of predictions produced by various uncertainty-aware models (Sec. 7.2). These include all baseline methods introduced in Chapter 3, as well as the random set model developed in this thesis (Chapter 5) and the credal set models presented in Chapter 6.

### 7.1 Current Metrics For Evaluation

**Aleatoric vs. epistemic uncertainty**. Most scholars distinguish aleatoric uncertainty, caused by randomness in the data, and epistemic uncertainty, stemming from a lack of knowledge about data distribution or model parameters (Kendall and Gal, 2017; Hüllermeier and Waegeman, 2021; Manchingal and Cuzzolin, 2022; Zaffalon, 2002). Different metrics are used to quantify uncertainty across model types (see Sec. 3), depending on the nature of the predictions. For instance, Bayesian models often assess epistemic uncertainty using Mutual Information, while Deep Ensembles typically rely on predictive variance. As noted in Sec. 3.2, such measures are not directly comparable across models, as they operate over different value ranges and reflect uncertainty in model-specific ways.

**Metrics for evaluation under uncertainty**. Evaluation metrics for probabilistic graphical models ( e.g. , Bayesian networks) were detailed in Marcot (2012), including model sensitivity analysis (Thogmartin, 2010) and a model emulation strategy to enable faster evaluation using

<!-- page: 98 -->

surrogate models. Snowling and Kramer (2001) instead, considered uncertainty for model selection, using uncertainty quantification for informed decision-making. An 'alternate hypotheses' approach was proposed by Zio and Apostolakis (1996) for evaluating model uncertainty which identifies a family of possible alternate models and probabilistically combines their predictions based on Bayesian model averaging (Droguett and Mosleh, 2008). In Park and Grandhi (2011), the model probability in the alternate hypotheses approach was further quantified by the measured deviations between data and model predictions. Our approach for model selection of uncertainty-aware models (Chapter 8) is unique, especially as we no longer rely solely on test accuracy to select the best model, but can instead establish a trade-off between accuracy and imprecision.

### 7.2 Classes of Epistemic Predictions

The predictions of a classifier can be plotted in the simplex (convex hull) $\mathcal{P}$ of the one-hot probability vectors assigning probability 1 to a particular class. For instance, in a 3-class classification scenario ($\mathbf{Y} = \{a, b, c\}$), the simplex would be a 2D simplex (triangle) connecting three points, each representing one of the classes, as shown in Fig. 7.1, which depicts all types of model predictions considered here.

[FIGURE: Figure 7.1: Different types of uncertainty-aware model predictions, shown in a unit simplex of probability distributions defined on the list of classes Y = {a, b, c}.]

Text in figure: a triangular probability simplex with vertices labeled "p(a) = 1 (0,1,0)" (top), "p(b) = 1 (1,0,0)" (bottom left), "p(c) = 1 (0,0,1)" (bottom right). A legend lists markers for: $\hat{p}_s(y \mid \mathbf{x}, \mathbb{D})$ (square), $\hat{p}_{ddu}(y \mid \mathbf{x}, \mathbb{D})$ (diamond/green), $\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})$ (circle), $\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D})$ (triangle), $\hat{p}_e(y \mid \mathbf{x}, \mathbb{D})$ (diamond/dark), $\hat{\mathbb{C}r}(y \mid \mathbf{x}, \mathbb{D})$ (blue shaded region), $\hat{p}_{bel}(y \mid \mathbf{x}, \mathbb{D})$ (orange shaded region), $BetP$ (X markers). The blue and orange convex regions (representing a credal set and a belief-function-induced credal set) overlap near the centre of the simplex.

An overview of the predictions generated by all uncertainty-aware models is provided below. Further details on the functioning of these models can be found in Chapter 3.

**Traditional Neural Networks** (CNNs) predict a vector of N scores, one for each class, duly calibrated to a probability vector representing a (discrete, categorical) probability distribution over the list of classes Y, $\hat{p}_s(y \mid x, \mathbb{D})$, which represents the probability of observing class y given the input x.

**Bayesian Neural Networks** (BNNs) (Lampinen and Vehtari, 2001; Titterington, 2004; Goan and Fookes, 2020; Hobbhahn et al., 2022) compute a predictive distribution $\hat{p}_b(y \mid x, \mathbb{D})$ by integrating over a learnt posterior distribution of model parameters θ given training data $\mathbb{D}$. This

<!-- page: 99 -->

is often infeasible due to the complexity of the posterior, leading to the use of *Bayesian Model Averaging* (BMA), which approximates the predictive distribution by averaging over predictions from multiple samples. BMA inadvertently smooths out predictive distributions, diluting the inherent uncertainty present in individual models (Hinne et al., 2020; Graefe et al., 2015) as shown in Fig. 3.2, Sec. 3.2. *When applied to classification, BMA yields point-wise predictions.* For fair comparison and to overcome BMA's limitations, in our proposed method in the next Chapter 8, we also use sets of prediction samples obtained from the different posterior weights *before* averaging.

In **Deep Ensembles** (DEs) (Lakshminarayanan et al., 2017), a prediction $\hat{p}_{de}(y \mid x, \mathbb{D})$ for an input x is obtained by averaging the predictions of K individual models: $\hat{p}_{de}(y \mid x, \mathbb{D}) = \frac{1}{K}\sum_{k=1}^{K} \hat{p}_k(y \mid x, \mathbb{D})$, where $\hat{p}_k$ represents the prediction of the k-th model, trained independently with different initialisations or architectures. Uncertainty is then quantified as in Sec. 3.3.

**Evidential Deep Learning** (EDL) models (Sensoy et al., 2018) make predictions $\hat{p}_e(y \mid x, \mathbb{D})$ as parameters of a second-order Dirichlet distribution on the class space, instead of softmax probabilities. EDL uses these parameters to obtain a pointwise prediction. As for BNNs, averaging may not be optimal; hence, in our proposed evaluation method (Chapter 8), we consider individual prediction samples.

**Deep Deterministic Uncertainty** (DDU) (Mukhoti et al., 2023) models differ from other uncertainty-aware baselines as they do not represent uncertainty in the prediction space, but do so in the input space by identifying whether an input sample is in-distribution (iD) or out-of-distribution (OoD). As a result, DDU provides predictions $\hat{p}_{ddu}(y \mid x, \mathbb{D})$ in the form of softmax probabilities akin to standard neural networks (CNNs).

**Credal Models.** Credal sets ($\hat{\mathbb{C}r}(y \mid x, \mathbb{D})$) can be computed from predicted probability intervals (Wang et al., 2024c; Caprio et al., 2023a) $[\hat{p}(y), \overline{\hat{p}}(y)]$, encoding lower and upper bounds, respectively, to the probabilities of each of the classes (De Campos et al., 1994) as shown in Eq. 6.1. A credal set is efficiently represented by its extremal points; their number can vary, depending on the size of the class set and the complexity of the network prediction the credal set represents.

**Belief Function Models.** A predicted belief function $\hat{Bel}$ on $\mathbf{Y}$ is mathematically equivalent to the credal set

$$
\mathbb{C}r_{\hat{Bel}}(y \mid x, \mathbb{D}) = \{p \in \mathcal{P} \mid p(A) \geq \hat{Bel}(A)\}.
$$

(7.1)

Its center of mass, termed *pignistic probability* (Smets, 2005) $BetP[\hat{Bel}]$, assumes the role of the predictive distribution for belief function models such as RS-NN (Chapter 5) and E-CNN (Tong et al., 2021): $\hat{p}_{bel}(y \mid x, \mathbb{D}) = BetP[\hat{Bel}]$.

In summary, predictive distributions play a pivotal role in all uncertainty-aware classification models, as they encapsulate both a model's uncertainty and the inherent variability in the data. Our proposed unified evaluation framework (Sec. 8.3) relies on mapping all such types of predictive distributions to a credal set.

<!-- page: 100 -->

# 8 A Unified Evaluation Framework for Epistemic Predictions

This chapter of the thesis proposes a novel *unified evaluation framework* (Chapter 8.3) which provides a holistic assessment of predictions produced by uncertainty-aware classifiers for model selection (Sec. 8.3.3). This framework carefully balances two crucial facets: the need for accurate predictions (the distance-based 'accuracy' of a prediction) and the acknowledgment of the inherent precision or imprecision of such predictions (i.e. , how 'vague' predictions are).

The aim is to enable the selection of the most fitting uncertainty-aware machine learning model, aligning with the requirements of specific applications. For instance, in crop disease classification where abstention is allowed, practitioners may prefer models that prioritize accuracy even if uncertainty is higher, because uncertain cases can be sent for manual review; whereas in autonomous driving, where abstention is not an option and decisions must be made quickly, models that produce more decisive predictions with lower uncertainty are favored to ensure timely and safe actions. The objective here, is *not* to propose yet another measure of uncertainty.

Such a unified framework (Fig. 8.1) harnesses the fact that predictions generated by Bayesian, Ensemble, Evidential, Deterministic and Imprecise-probabilistic models can all be represented as *credal sets*, i.e. , convex sets of probability vectors (Sec. 8.2), within the simplex of all probability distributions defined on the label space, ensuring compatibility across various model architectures and types of uncertainty model.

### 8.1 Key Contributions

- **Firstly,** a novel versatile *evaluation* framework for *ranking* uncertainty-aware predictions produced by a wide range of models is proposed to facilitate model selection under uncertainty.
- **Secondly,** instrumental to the above, a method for transforming predictions to credal sets in the prediction simplex is outlined.
- **Thirdly,** a novel metric designed to assess the trade-off between accuracy and precision of predictions is proposed and shows that such metric reduces to the standard KL divergence for point-wise predictions.
- **Finally,** an experimental validation of the soundness of the evaluation framework is provided, demonstrated through suitable ablation studies, especially on the main parameter determining the trade-off between accuracy and precision.

<!-- page: 101 -->

[FIGURE: Figure 8.1: Different types of uncertainty-aware model predictions, shown in a unit simplex of probability distributions defined on the list of classes Y = {a, b, c}. The proposed evaluation framework uses a metric which combines, for each input x, a distance (arrows) between the corresponding ground truth (e.g. , (0, 1, 0)) and the epistemic predictions generated by the various models (in the form of credal sets), and a measure of the extent of the credal prediction (non-specificity).]

Text in figure: a triangular probability simplex, vertices labeled "p(a) = 1 (0,1,0)" (top), "p(b) = 1 (1,0,0)" (bottom left), "p(c) = 1 (0,0,1)" (bottom right). A legend lists: $\hat{p}_s(y \mid \mathbf{x}, \mathbb{D})$, $\hat{p}_{ddu}(y \mid \mathbf{x}, \mathbb{D})$, $\hat{p}_b(y \mid \mathbf{x}, \mathbb{D})$, $\hat{p}_{de}(y \mid \mathbf{x}, \mathbb{D})$, $\hat{p}_e(y \mid \mathbf{x}, \mathbb{D})$, $\hat{\mathbb{C}r}(y \mid \mathbf{x}, \mathbb{D})$, $\hat{p}_{bel}(y \mid \mathbf{x}, \mathbb{D})$, $BetP$. Clusters of points near the top vertex represent individual model predictions, with arrows labeled $d(y, \hat{y})$ pointing from the ground truth vertex to a blue credal-set region and an orange belief-function region, each labeled "NS[m]". Below the simplex: $\mathcal{E} = d(y, \hat{y}) + \lambda \cdot NS[m]$.

### 8.2 Methodology: Mapping Predictions To Credal Sets

Credal and belief function models directly output predictions in the form of credal sets. Traditional networks and Bayesian BMA also generate a credal set: the trivial one containing a single probability vector. For Bayesian, Ensemble, and Evidential models, we utilize the multiple predictions generated directly from the model, prior to any averaging, for a more faithful representation of the predictions. Below, we explain how predictions from Bayesian, Ensemble and Evidential models can also be represented by credal sets, leveraging *coherent lower probabilities*.

#### 8.2.1 Coherent Lower Probabilities

**Coherent lower probabilities** (Pericchi and Walley, 1991; Miranda et al., 2023; 2021; Miranda, 2008) model partial information about a probability distribution. Namely, a *lower probability* is a function $\underline{P}$ from the power set $\mathbb{P}(\mathbf{Y})$ of all subsets of $\mathbf{Y}$ into [0, 1], that (i) is monotone, i.e. , $\underline{P}(A) \leq \underline{P}(B)$ for all $A \subseteq B$; (ii) satisfies $\underline{P}(\emptyset) = 0$ and $\underline{P}(\mathbf{Y}) = 1$.

Given such a lower probability $\underline{P}$, the associated credal set $\mathbb{C}r(\underline{P})$ comprises all probability measures in $\mathcal{P}(\mathbf{Y})$ that have it as lower bound:

$$
\mathbb{C}r(\underline{P}) = \{P \in \mathcal{P}(\mathbf{Y}) \mid P(A) \geq \underline{P}(A) \quad \forall A \subseteq \mathbf{Y}\}.
$$

(8.1)

$\underline{P}$ is considered *coherent* if it can be computed as: $\underline{P}(A) = \min_{P \in \mathbb{C}r(\underline{P})} P(A) \quad \forall A \subseteq \mathbf{Y}$. From (Eq. 7.1), belief functions are also coherent lower probabilities.

<!-- page: 102 -->

A strong theoretical underpinning for reasoning with coherent lower probabilities (and, therefore, the corresponding credal sets) is that it allows us to comply with the coherence principle. In a Bayesian context, individual predictions (such as those of networks with specified weights) can be interpreted as subjective pieces of evidence about a fact (e.g. , what is the true class of an input observation). Coherence ensures that one realises the full implications of such partial assessments.

For instance, assume that the available evidence is that on a ternary classification problem is that $\underline{P}(0) = 1/4$, $\underline{P}(1) = 1/4$, $\underline{P}(2) = 1/4$, $\underline{P}(\{0, 1\}) = 1/4$. In the behavioural interpretation of probability (Walley, 1991), in which lower probability of an event A is the upper bound to the price one is willing to pay for betting on outcome A, this means that one is willing to pay up to 1/4 for betting on either 0 or 1. But then one should be willing to bet 1/4 + 1/4 = 1/2 for betting on {0, 1}, which is over the specified lower probability for it. Hence, the above specifications are incoherent. Incoherence means that lower probabilities (specified prices) on some events effectively imply lower probabilities on other events which are incompatible.

Now, learning a coherent lower probability from sample predictions does ensure coherence. This is explained, for instance, in (Bernard, 2005). The concept was originally introduced by Walley in his general treatment of imprecise probabilities (Walley, 1991). Further, as observed, e.g. in (Caprio et al., 2024), working with credal sets allows us to hedge against model misspecification, when the set of probability distributions considered by a statistician does not include the distribution that generated the observed data.

In some cases, it may be useful to consider the conjugate function of a lower probability, referred to as the upper probability, $\overline{P}(A) = 1 - \underline{P}(A^c)$ for every $A \subseteq \mathbf{Y}$. The upper and lower probabilities provide upper and lower bounds respectively for the true distribution $\mathbf{P}(A) \in \mathbb{C}r$. Notably, for any coherent lower probability $\underline{P}$, its conjugate upper probability $\overline{P}$ satisfies:

$$
\overline{P}(A) = \max_{P \leq \overline{P}} P(A) \quad \forall A \subseteq \mathbf{Y}
$$

(8.2)

This equation underscores the equivalence between the probabilistic information conveyed by the lower and upper probabilities, indicating that working with either one suffices.

#### 8.2.2 Computing Lower Probabilities From a Sample of Probability Vectors

Given the multiple probability vectors predicted by Bayesian, Ensemble or Evidential models, a lower probability can be obtained by computing the probability of any event A (as the sum of the probabilities of the elements of A) for each probability vector and then taking the minimum of such $P(A)$ over the samples. When $|\mathbf{Y}| = N$ is large, it can be highly inefficient to compute probabilities for all $2^N$ events in the powerset $\mathbb{P}(\mathbf{Y})$. We thus adopt the same budgeting technique used by RS-NN (Sec. 5.2.2, Chapter 5) that provides a fixed budget of most relevant subsets $A \in \mathbb{P}(\mathbf{Y})$, and compute lower probabilities only for those.

#### 8.2.3 Computing Masses By Moebius Inverse

To efficiently handle the credal set (Eq. 8.1), we can compute its vertices. This can be done via the *Moebius inverse*

$$
m_{\underline{P}}(A) = \sum_{B \subseteq A} (-1)^{|A \setminus B|} \underline{P}(B) \quad \forall A \subseteq \mathbf{Y},
$$

(8.3)

<!-- page: 103 -->

whose output is a *mass function* (Shafer, 1976), i.e. , a set function (Denneberg and Grabisch, 1999) $m : \mathbb{P}(\mathbf{Y}) \to [0, 1]$ such that $m(\emptyset) = 0$, $\sum_{A \subset \Theta} m(A) = 1$. The Moebius inverse of a coherent lower probability that is not a belief function may yield negative values. To ensure a coherent lower probability, we set any negative mass to zero and add the universal set (i.e., the full label set Y) as an additional focal element. This set is assigned the remaining mass needed to ensure that the total mass sums to 1. This guarantees that the resulting mass function is valid and normalized, even when starting from a lower probability that is not itself a belief function.

#### 8.2.4 Computing the Credal Set of Predictions

Once mass functions are computed, we can compute the vertices of the credal set $\mathbb{C}r(\underline{P})$ (Eq. 8.1) identified by the computed lower probabilities. Such a special credal set has, as vertices, all the distributions $p^\pi$ induced by a permutation $\pi = \{x_{\pi(1)}, \ldots, x_{\pi(|\mathbf{Y}|)}\}$ of the elements of the sample space Y, of the form (Chateauneuf and Jaffray, 1989; Cuzzolin, 2008a)

$$
p^{\pi}(x_{\pi(i)}) = \sum_{A \ni x_{\pi(i)};\ A \not\ni x_{\pi(j)}\ \forall j<i} m_{\underline{P}}(A).
$$

(8.4)

However, we do not need to compute all such vertices; instead, an approximation using only a subset of vertices is often sufficient and even preferable. With this approximation, the method can be applied to datasets with larger number of classes.

**Approximate computation.** Given the prohibitively high computational complexity associated with computing permutations as in Eq. 8.4, especially for a large number of classes, we propose an approximation technique that offers comparable effectiveness without the need to compute all vertices. For each class $c_i$, $i = 1, 2, \ldots, N$ in classes $\mathcal{C}$ where N is the number of classes, we create two permutations. In the first permutation, $c_i$ is placed as the first element, while in the second permutation, $c_i$ is placed as the last element. By doing so, $c_i$ occupies both the first and last positions in the permutations. Due to the nature of extremal probabilities calculation (Eq. 8.4), when a class $c_i$ is placed as the first element in the permutation, it occupies the initial position in the subset, allowing it to be included in the maximal number of focal elements. As a result, the extremal probability for $c_i$ in this scenario is maximized because it contributes to the sum of masses for all the focal elements containing it.

Conversely, when a class $c_i$ is placed as the last element in the permutation, it is excluded from the focal elements containing classes preceding it in the permutation order. Therefore, the extremal probability for $c_i$ is minimised, because it contributes to the sum of masses for fewer focal elements compared to when it is placed as the first element. This approach yields $2 \cdot N$ number of vertices, providing an effective approximate approach to computing all vertices. The vertices of the credal set associated with each model are computed using mass functions as in Eq. 8.4, via the approximation technique detailed in this section.

The **overall procedure** is: (1) Given a sample of predicted probability vectors, the lower probability of each subset of classes A is computed; (2) A mass function is calculated by Moebius inverse (Eq. 8.3); (3) The vertices of the credal set associated with the lower probability (and the original predictions) are computed.

<!-- page: 104 -->

### 8.3 Methodology: Evaluation of Epistemic Predictions

We propose a novel *unified evaluation framework* for a comprehensive assessment of these uncertainty models for model selection, extending beyond those specifically addressed in this paper, and understand the fundamental trade-off between predictive accuracy and the imprecision inherent in uncertainty models.

The evaluation metric (Fig. 8.1) combines a component measuring the distance in the probability simplex (in particular, the classical Kullback-Leibler (KL) divergence) between the ground truth and the prediction, represented by a credal set as explained in Secs. 7.2 and 8.2.4, with a non-specificity measure (Dubois and Prade, 1987; Dubois et al., 1993; Klir, 1987) assessing the 'imprecision' of a model, i.e. , how far the prediction is from being a precise probability vector.

Classical performance metrics assume a single (max likelihood) class is predicted; thus, they do not act directly on the predicted probability vectors. By doing so, they discard a lot of information. We propose, instead, to evaluate predictions *as they are* (either credal sets or as single probabilities, as special case).

#### 8.3.1 The Metric

Mathematically, the evaluation metric $\mathcal{E}$ can be expressed, for a single data point, as:

$$
\mathcal{E} = d(y, \hat{y}) + \lambda \cdot NS[m],
$$

(8.5)

where d is the distance, however defined, between the ground truth y and epistemic prediction $\hat{y}$, λ is a *trade-off parameter*, and $NS[m]$ is a non-specificity measure using as input the mass function representation (Eq. 8.3) of the prediction. Over a test set, the average of Eq. 8.5 is measured. Low values are desirable.

Since d and NS are conceptually and dimensionally distinct, neither can be directly compared or combined without scaling. The trade-off parameter λ serves as a dimension-matching constant that calibrates the relative importance of the non-specificity term with respect to the distance term. Adjusting the value of λ allows the user to emphasize either the accuracy of predictions or the precision/imprecision of the model determined by the uncertainty estimates, based on their specific requirements or preferences. In Sec. 8.4.3, we show experimental results on several values of λ.

The *sum formulation* intuitively represents a weighted penalty structure, aligning well with many risk or loss functions in decision theory where distinct costs additively contribute to the total expected cost. In contrast, a multiplicative combination can disproportionately amplify the effect of one term when the other is large or near zero, potentially resulting in unstable behavior.

##### 8.3.1.1 Distance Computation

To compute the distance d between (epistemic) prediction and ground truth, here we adopt, in particular, the classical Kullback-Leibler (KL) divergence $D_{KL}(y||\hat{y}) = \int_x y(x) \log \frac{y(x)}{\hat{y}(x)} dx$ between the ground truth y and the boundary of the epistemic prediction $\hat{y}$. Nevertheless, our framework is agnostic to that: ablation studies on different distance measures (specifically, the Jensen-Shannon (JS) (Menéndez et al., 1997) divergence) and their effect on $\mathcal{E}$ and model rankings are shown in Sec. 8.4.5.3.

<!-- page: 105 -->

Whatever the chosen distance, because of the convex nature of credal sets, this reduces to computing the distance to the closest vertex of the credal prediction (Sec. 8.3.1.1). For standard networks, this amounts to computing the KL (or JS) divergence between the ground truth distribution y and the single prediction. For completeness, in our experiments KL is also applied to the pointwise predictions generated by Model Averaging, in the Bayesian, Ensemble and Evidential cases.

**Why KL over L2 and other measures?** KL divergence measures the distance between two probability distributions whereas L2 measures the Euclidean distance between points or vectors. KL divergence has a clear interpretation in information theory as the amount of information lost when one distribution approximates the other (Shlens, 2014), i.e, KL can capture the relative differences between probabilities better. Other divergence measures, such as Jensen-Shannon divergence (Menéndez et al., 1997), are symmetric and handles small probabilities well, but KL is often preferred as it penalizes cases where the approximate distribution assigns probability to regions where the true distribution assigns none. This property ensures that both the distributions closely match in significant regions (Ullah, 1996), avoiding substantial probability mass in unlikely areas. Therefore, KL divergence can be advantageous over JS divergence, particularly in its sensitivity to differences between distributions, especially when small probabilities are involved. Unlike JS, which is symmetric and bounded, KL divergence can grow unbounded when there is a significant mismatch between the predicted and true distributions. This sensitivity allows KL to emphasize differences that JS might smooth out.

**Why use KL Divergence to the nearest vertex?** Measuring KL divergence to the nearest vertex of the credal set avoids giving an advantage to point predictions by deterministic models such as CNN. If we were to use the center of mass of a credal set formed by Bayesian predictions instead, there might be cases where the point prediction by CNN might align perfectly with this center. In such a case, the KL divergence would be identical for both the CNN prediction and the Bayesian prediction. This would favor the CNN prediction as their non-specificity is always zero, while the non-specificity of the Bayesian prediction depends on its credal set size. Hence, using the centroid would penalise imprecise predictions whose boundaries may be pretty close to the ground truth. While better point predictions by chance should not be discounted, focusing on the nearest vertex encourages a balanced consideration of both KL divergence and non-specificity. Now, if we were to consider the distance to farthest point in the credal set, the scoring would instead be on the basis of how wrong the most wrong prediction is. It acts as a dual (Abellán and Gómez, 2006) to the minimum distance route that we take.

It is important to clarify that using the nearest vertex is an approximation to measuring distance to the credal set boundary. Any point on the boundary could be considered, but selecting arbitrary boundary points would require conformal optimization methods that may be computationally expensive. Thus, computing the vertices provides a tractable and interpretable proxy.

##### 8.3.1.2 Non-Specificity

Assuming a mass representation m is available for the prediction (Sec. 8.2.4), a *non-specificity* measure is used to determine how imprecise the former is: the greater the non-specificity, the larger the imprecision. Non-specificity, due to Dubois and Prade (1987), (Dubois et al., 1993; Klir, 1987), is given by the degree of concentration of the mass assigned to focal set A (sets of

<!-- page: 106 -->

labels) in the label space Y:

$$
NS[m] = \sum_{A \subseteq \mathbf{Y}} m(A) \log |A|.
$$

(8.6)

Here, |A| denotes the cardinality (number of elements) of the focal set A. Non-specificity captures epistemic uncertainty, as it is higher for predictions associated with larger sets of classes (or higher mass values for those), signifying lack of confidence in the predicted probability. The log function in Eq. 8.6 grows more slowly than a linear function, providing diminishing returns as the set size increases. Non-specificity is also tied to the size of the predicted credal set, another popular measure of epistemic uncertainty (Hüllermeier et al., 2022); as the credal set increases in size, so does non-specificity.

One of the earlier works by Yager (2008) makes the distinction between two types of uncertainty within a credal set: conflict (also known as randomness or discord) and non-specificity. Non-specificity essentially varies with the size of the credal set (Kolmogorov, 1965). Since by definition, aleatoric uncertainty refers to the inherent randomness or variability in the data, while epistemic uncertainty relates to the lack of knowledge or information about the system (Hüllermeier and Waegeman, 2019), conflict and non-specificity directly parallel these concepts. These measures of uncertainty are axiomatically justified (Bronevich and Klir, 2008). Several measures of non-specificity have been proposed over the years (Kramosil, 1999; Pal et al., 1993; Huang et al., 2014; Smarandache et al., 2011; Abellán and Moral, 2000; 2005). Once again, our evaluation metric can be used with any suitable such measure. An ablation study is shown in Sec. 8.4.5.4.

Note that, for pointwise predictions (including those generated by BMA and ensemble averaging) non-specificity goes to zero (as all non-singleton focal elements |A| > 1 have mass 0, indicating perfect precision) and the credal set collapses to a single point. Thus, for precise predictions, (Eq. 8.5) reduces to the classical KL.

#### 8.3.2 Rationale and Interpretation

The rationale of Eq. 8.5 is that a 'good' model's predictions should (on average) be accurate (close to the ground truth) and specific (exhibit low uncertainty), so that the model can confidently assign probabilities to different outcomes. Conversely, a 'bad' model is one whose predictions are less accurate and/or have higher uncertainty, resulting in a wider range of possible outcomes with less confidence in their probabilities.

When evaluating models, the distinction between *correct* and *incorrect* predictions is crucial. For **correct predictions**, the ideal model exhibits low KL divergence to the ground truth and low non-specificity (uncertainty). If a correct prediction is made with high KL, the model's output is far from the ground truth, indicating it may have succeeded by chance or due to overfitting. If NS is high, the model shows indecision even when it gets the answer right, which undermines reliability.

For **incorrect predictions**, the model should display high NS to reflect uncertainty, and a controlled increase in its deviation from the ground truth (low KL). This avoids the undesirable case where the prediction is too close to an incorrect class, such as being at the opposite vertex of the simplex. For this reason, we prefer low KL at all instances. The worst kind of prediction is an incorrect (high KL) and highly confident (low NS) prediction.

<!-- page: 107 -->

This logic extends to the *out-of-distribution (OoD)* setting: a reliable model should respond to unseen inputs with high NS, and ideally, with KL divergence that increases as the input distribution diverges from training data.

Here, the best model selected by our algorithm is the one that minimizes the evaluation metric $\mathcal{E}$. We show the evaluation metric for correct and incorrect predictions (Tab. 8.7) on CIFAR-10 (Fig. 8.2), MNIST (Fig. 8.3) and CIFAR-100 (Fig. 8.4).

*Minimizing $\mathcal{E}$* balances overconfidence and underconfidence: it penalizes being overly confident (low NS) in wrong predictions (high KL) and overly cautious (high NS) when correct (low KL). Thus, the model is encouraged to avoid being both very wrong (high KL) and highly uncertain (high NS) simultaneously, pushing for controlled uncertainty, i.e., enough uncertainty when wrong, but not too much to make predictions meaningless. However, this can be a drawback of the metric, since in cases like OoD detection where high uncertainty and high error (high KL, high NS) are desirable, the metric may penalize such behaviour, potentially discouraging the model from expressing full uncertainty on unfamiliar or ambiguous inputs. In these cases, careful tuning of λ is required to reflect the presence of OoD data. But if in-distribution and OoD data are mixed without distinction, this is a limitation of the metric and reduces its usefulness.

#### 8.3.3 Model Selection and Scenarios

In Algorithm 1, we outline the process for model selection based on the evaluation metric $\mathcal{E}$. Using the following scenarios, we demonstrate (1) how to select the optimal λ for a specific application, (2) its impact on the evaluation metric, and (3) how model selection differs when abstaining from a decision is allowed vs. when a decision is mandatory.

```
Algorithm 1 Model Selection based on E.
  Input: Model predictions ŷ_K for a list of K models, ground truth labels y, trade-off parameter λ.
  Select λ based on the required precision for the task (high precision requires a high λ and vice versa).
  Output: Selected model K with the lowest Evaluation Metric E
  for each model K do
      o Obtain predictions ŷ_K for all available models on the test set.
      Compute lower probabilities P(ŷ_K) and mass functions m_P(ŷ_K) using (Eq. 8.3) over the test set.
      o Compute vertices of the credal set using (Eq. 8.4).
      o Compute the minimum KL divergence between ground truth and predictions, d(y, ŷ_K) = KL(y||ŷ_K) over the entire test set.
      o Compute the non-specificity, NS[m], of predictions on the test set using (Eq. 8.6).
      o Compute E = KL(y||ŷ_K) + λ · NS[m].
  end for
  Select the model K which has the lowest E.
```

Consider crop disease classification from drone images, aiming to categorize crops as healthy, bacterial, fungal, or viral. Ideally, we require a model with low KL divergence and low non-specificity. But since we can choose to abstain from making a decision, we can allow non-specificity to be high. Therefore, we assign a low value to λ as we want to favour the KL divergence more.

<!-- page: 108 -->

Finally, we select the model which has lowest $\mathcal{E}$. If the decision-making process in this scenario required more precision (i.e. , decision is mandatory), even at the risk of incorrect predictions, we would increase λ to penalize models with higher uncertainty.

Alternatively, consider the following safety-critical example: an autonomous vehicle driving through a crowded urban environment. The vehicle must make split-second decisions about detecting and responding to pedestrians, traffic signals, vehicles, and other objects. In this high-stakes scenario, *abstention* or making no decision is not an option because failing to act could result in accidents, injury, or property damage. Here, precision and timeliness in decision-making is crucial, and a model with high uncertainty (non-specificity) cannot be allowed to abstain. Here, the parameter λ would need to be set to a higher value to ensure that the model's non-specificity is minimized. The model must be decisive, even if there is some risk of making incorrect predictions.

This illustrates why our model selection approach is superior to conventional methods that is solely based on accuracy. In crop disease classification, the choice to abstain from decisions allows us to prioritize models that balance KL divergence and non-specificity, leading to *more informed interventions*. In contrast, for autonomous vehicles, where abstention is not an option, our method focuses on minimizing non-specificity and ensuring *decisiveness even under uncertainty*. This approach tailors model reliability and suitability to the specific decision-making context, beyond just accuracy.

#### 8.3.4 Practical utility of the Evaluation metric

**How a practitioner determines the trade-off λ.**

To select a suitable λ, the practitioner will consider the following task requirements:

- Is abstention allowed?
- Is precision or accuracy more critical?
- What are the risks associated with incorrect predictions or abstention?

Here, we use the same two examples of **crop disease classification** *(abstention from decision-making is allowed)*, and **autonomous driving** *(abstention is not allowed)*. Consider the following toy problem involving four models (A, B, C, and D) and their respective performances under different λ values, as shown in Tab. 8.1 below.

Table 8.1: Comparison of Evaluation Metric ($\mathcal{E}$) for Models A, B, C, and D under different values of λ.

| Model | KL | NS | E(Low λ = 0.1) | E(Moderate λ = 0.5) | E(High λ = 2) |
|---|---|---|---|---|---|
| Model A | 0.243 | 0.166 | 0.243 + 0.1 × 0.166 = 0.259 | 0.243 + 0.5 × 0.166 = 0.326 | 0.243 + 2 × 0.166 = 0.575 |
| Model B | 0.031 | 0.385 | 0.031 + 0.1 × 0.385 = 0.069 | 0.031 + 0.5 × 0.385 = 0.223 | 0.031 + 2 × 0.385 = 0.801 |
| Model C | 0.002 | 2.267 | 0.002 + 0.1 × 2.267 = 0.228 | 0.002 + 0.5 × 2.267 = 1.136 | 0.002 + 2 × 2.267 = 4.536 |
| Model D | 0.398 | 0.009 | 0.398 + 0.1 × 0.009 = 0.398 | 0.398 + 0.5 × 0.009 = 0.402 | 0.398 + 2 × 0.009 = 0.416 |

**Ranking:** The model selection algorithm returns the following ranking of models based on the values in Tab. 8.1.

- λ = 0.1 (*Low*): **B**, C, A, D

<!-- page: 109 -->

- λ = 0.5 (*Moderate*): **B**, A, D, C
- λ = 2 (*High*): **D**, A, B, C

**1. Crop disease classification**

Abstention is *allowed*–can afford to abstain from making predictions for uncertain cases (e.g. , sending ambiguous images for manual analysis).

**Why choose a low λ?** In this scenario, we have the option to abstain from making decisions for uncertain cases (e.g. , we can send ambiguous images for manual analysis based on the model's predictions). Therefore, we do not give much weight to non-specificity and prefer a model which has low KL, i.e. , it can give us a prediction more closer to the ground truth.

Note that our metric is not used for test set evaluation, it is only used for model selection. After the model is selected, we do not scale either of these terms up or down using λ. The model operates with its inherent uncertainty predictions without any further adjustments.

**Why not choose a high λ?** If we choose a high λ, we penalize models with high uncertainty. As a result, we end up selecting a model that is very precise in its predictions. This prevents us from leveraging the advantage of the abstention allowance.

**2. Autonomous driving**

Abstention is *not allowed*–decision making is necessary, as abstention can lead to critical failures, such as accidents, harm to pedestrians, or collisions with other vehicles.

**Why choose a high λ?** In this scenario, a decision must be made (e.g. , when there is a shadow on the road, we cannot afford to be uncertain or abstain; we must decide whether to stop or not). Therefore, we heavily penalize non-specificity. Models with lower non-specificity will rank first using our model selection, because they are more decisive in their predictions.

**Why not choose a low λ?** If we choose a low λ, we prioritize the models with high uncertainty, therefore, end up selecting a model that is very imprecise about its predictions. When there is no option to abstain, we do not want an indecisive model.

**How does it reflect in the rankings?** In the rankings for low λ (λ = 0.1), Model B ranks first due to its low KL. Conversely, with high λ (λ = 2), the ranking shifts to prioritize models with low non-specificity. Model D ranks highest because of its minimal non-specificity. This ranking penalizes uncertain models like Models C and B, pushing it to the bottom.

For crop disease classification, choosing a high λ in this scenario negates the advantage of abstention and leads to selecting a model that is overly precise at the cost of being potentially less reliable in uncertain cases. However, in autonomous driving, abstention is not an option because hesitation in decision-making can result in accidents. Here, a high λ is crucial to prioritize models with low non-specificity, ensuring the model makes more precise and decisive predictions.

#### 8.3.5 Evaluation Metric or Uncertainty Measure?

The evaluation metric is *not* a new uncertainty measure. The first term, the KL divergence, is unrelated to uncertainty and is more related to accuracy, whereas non-specificity (Yager, 2008) is a measure of epistemic uncertainty as it is directly proportional to the size of the credal set

<!-- page: 110 -->

(Hüllermeier and Waegeman, 2021). Together, with the trade-off parameter λ, the evaluation metric provides a *holistic assessment of the predictions*.

The value of the metric $\mathcal{E}$ is a function of the credal set. The distance measure $d(y, \hat{y})$ is the distance to a single one-hot probability vector, which has both 0 epistemic uncertainty (being a single point) and 0 aleatoric uncertainty (as it is one-hot). Non-specificity was originally introduced as a measure of imprecision in a random set framework in which masses are independently assigned to sets of outcomes. As discussed in (Hüllermeier and Waegeman, 2021), Sec. 4.6.1, in the case of credal sets non-specificity can be considered a measure of *epistemic*, rather than total uncertainty.

Therefore, the first term in the evaluation metric, KL divergence has no relation to uncertainty, while, the second term, non-specificity, can be considered a measure of epistemic uncertainty.

### 8.4 Experiments

**Firstly,** we designed a set of baseline experiments to evaluate the behaviour of the proposed composite performance metric (Sec. 8.4.2), using a representative for each class of predictions/models. **Secondly,** we assess how these models are ranked (Sec. 8.4.4). We also ran several ablations studies: (i) on different measures of divergence (Kullback-Leibler vs. Jensen-Shannon) (Sec. 8.4.5.3), their effect on model selection (Tab. 8.9); (ii) on different non-specificity measures (Sec. 8.4.5.4, Tab. 8.10), and why our choices of KL and NS are better; (iii) on the trade-off parameter λ, to understand its effect on the ranking (Sec. 8.4.3); (iv) on the effect of the number of sample predictions produced by Bayesian and Ensemble models (Sec. 8.4.5.7).

#### 8.4.1 Implementation

##### 8.4.1.1 Datasets

We use MNIST (LeCun and Cortes, 2005), CIFAR-10 (Krizhevsky et al., 2009) and CIFAR-100 (Krizhevsky, 2012) as datasets. The data is split into 40000:10000:10000 samples for training, testing, and validation respectively for CIFAR-10 and CIFAR-100, and 50000:10000:10000 samples for MNIST.

##### 8.4.1.2 Baselines and Backbones

To assess the behaviour of our evaluation metric we adopted the following baselines: (1) Traditional Neural Network (**CNN**) with no uncertainty estimation, (2) Laplace Bridge Bayesian Neural Network (**LB-BNN**) (Hobbhahn et al., 2022), (3) Deep Ensemble (**DE**) (Lakshminarayanan et al., 2017), (4) Evidential Deep Learning (**EDL**) (Sensoy et al., 2018), (5) Deep Deterministic Uncertainty (**DDU**) (Mukhoti et al., 2023), (6) Credal-Set Interval Neural Networks (**CreINN**) (Sec. 6.1) (Wang et al., 2024c), (7) Evidential Convolutional Neural Network (**E-CNN**) (Tong et al., 2021), and (8) Random-Set Neural Network (**RS-NN**) (Chapter 5).

EDL (Sensoy et al., 2018) predictions are obtained by sampling from the posterior Dirichlet distribution, and DDU (Mukhoti et al., 2023) predictions are softmax probabilities over classes, similar to traditional neural network CNN. CreINNs (Wang et al., 2024c) retain the structure of traditional Interval Neural Networks to generate interval probabilities, lower and upper

<!-- page: 111 -->

probabilities for each prediction, and formulate credal sets from these interval predictions. **E-CNN** is an evidential uncertainty classifier which predicts mass functions for sets of outcomes. Credal sets can directly be generated from these mass functions. ResNet50 backbone is used for all the models.

##### 8.4.1.3 Training Details

The training details for all models are the same as in Sec. 5.3.1.3. We only require a CPU for evaluation of predictions on CIFAR-10 and MNIST. For CIFAR-100, we use an Nvidia A100 40GB GPU. The entire code runs in approximately 70 seconds for CIFAR-10 dataset. The credal uncertainty estimation in ablation study (Sec. 8.4.5.4) takes an additional 90 seconds.

##### 8.4.1.4 Obtaining Epistemic Predictions

For LB-BNN, EDL and DE, we present results on both averaged predictions and credal sets generated from multiple prediction samples before averaging (100 prediction samples for LB-BNN and EDL, 15 ensembles for DE). An ablation study on number of samples *vs.* evaluation metric $\mathcal{E}$ for these models is discussed in Sec. 8.4.5.7. For CreINN, 10 samples were generated per lower and upper probability prediction. E-CNN directly predicts masses for all possible outcome sets (for CIFAR-10 with 10 classes, $2^{10} = 1024 - 1 = 1023$ outcomes, ∅ excluded), making it computationally infeasible for large datasets (e.g, CIFAR-100 where computing $2^{100}$ scores is inefficient). RS-NN generates belief functions for a budgeted set of outcomes. On CIFAR-10 and MNIST, it predicts 30 class sets (10 classes + 20 subsets), and 300 for CIFAR-100 (100 singletons + 200 subsets).

#### 8.4.2 Analysis of the Evaluation Metric

Tab. 8.2 shows the mean and standard deviation of Kullback-Leibler divergence (KL), Non-Specificity (NS) (Eq. 8.6), Evaluation Metric ($\mathcal{E}$) (Eq. 8.5), test accuracy (%) and Expected Calibration Error (ECE) for the chosen LB-BNN, DE, EDL, CreINN, E-CNN and RS-NN models. We also report these for models with point predictions only, i.e. , CNN, Bayesian Model Averaged LB-BNN (LB-BNN Avg), averaged ensemble predictions (DE Avg) and DDU, for trade-off λ = 1.

Tab. 8.2 shows that for CIFAR-10, DE outperforms all other models with a test accuracy of 93.77%, a low ECE, while DE Avg and RS-NN has the lowest $\mathcal{E}$ score. Similarly, in MNIST, RS-NN achieves the highest accuracy and the LB-BNN Avg and RS-NN has the lowest $\mathcal{E}$. Conversely, for CIFAR-100, DE has a higher test accuracy of 74.08%, but RS-NN has the lowest $\mathcal{E}$ score. The performance is markedly low for EDL and CreINN, with E-CNN showing no results due to computational infeasibility. This model selection in Tab. 8.2 is reflected in the ranking for λ = 1 in Tab. 8.4.

**KL Divergence (KL)**. For point predictions generated by CNN, LB-BNN Avg, DE Avg and DDU, we computed the KL divergence between the ground truth and the point prediction. For all other models, we computed the KL between the ground truth and the boundary of the credal set (i.e. , its closest vertex) (Sec. 8.3.1.1). The violin plot of Fig. 8.2(a) visualises the distribution of KL divergence values for correct and incorrect predictions. For each model class, the KL divergence for correct predictions is represented by a single horizontal line (in blue, left), indicating that KL values for correct predictions are highly concentrated. This implies that, when the model makes correct predictions, the boundary of the predicted credal set is very close

<!-- page: 112 -->

to the ground truth. The KL divergence for incorrect predictions (in orange, right) is more broadly distributed for all models except EDL and E-CNN, which show consistently low KL values regardless of predictions being correct or incorrect. This behavior could be attributed to the high non-specificity these models demonstrate, as shown in Fig. 8.2 (top right) and Tab. 8.2. Since non-specificity and credal set size are directly correlated, as illustrated in Figs. 8.15, 8.16 and 8.17, this may be due to the large credal set size: the credal set spans much of the simplex, allowing one of its vertices to lie close to the ground truth.

Table 8.2: Comparison of Kullback-Leibler divergence (KL), Non-Specificity (NS) and Evaluation Metric ($\mathcal{E}$) for uncertainty-aware classifiers (trade-off λ = 1). Mean and standard deviation are shown for CIFAR-10, MNIST and CIFAR-100 datasets.

| Dataset | Model | Test accuracy (%) (↑) | ECE (↓) | KL divergence (KL) | Non-Specificity (NS) | Evaluation metric (E) (↓) |
|---|---|---|---|---|---|---|
| CIFAR-10 | LB-BNN | 89.24 | 0.0565 | 0.243 ± 1.315 | 0.166 ± 0.398 | 0.409 ± 1.381 |
| CIFAR-10 | DE | 93.77 | 0.0075 | 0.031 ± 0.367 | 0.385 ± 0.715 | 0.415 ± 0.805 |
| CIFAR-10 | EDL | 59.13 | 0.0491 | 0.002 ± 0.011 | 2.267 ± 0.067 | 2.270 ± 0.066 |
| CIFAR-10 | CreINN | 88.36 | 0.0108 | 0.058 ± 0.374 | 0.596 ± 0.812 | 0.654 ± 0.892 |
| CIFAR-10 | E-CNN | 83.5 | 0.6497 | 0.193 ± 0.215 | 1.609 ± 0.003 | 1.802 ± 0.215 |
| CIFAR-10 | RS-NN | 93.53 | 0.0509 | 0.398 ± 1.895 | 0.009 ± 0.052 | 0.407 ± 0.500 |
| CIFAR-10 | CNN | 90.25 | 0.0668 | 0.481 ± 1.797 | 0.000 ± 0.000 | 0.481 ± 1.797 |
| CIFAR-10 | LB-BNN Avg | 89.24 | 0.0565 | 0.420 ± 1.520 | 0.000 ± 0.000 | 0.420 ± 1.520 |
| CIFAR-10 | DE Avg | 93.77 | 0.0075 | 0.195 ± 0.763 | 0.000 ± 0.000 | 0.195 ± 0.763 |
| CIFAR-10 | DDU | 91.34 | 0.0439 | 0.309 ± 1.115 | 0.000 ± 0.000 | 0.309 ± 1.115 |
| MNIST | LB-BNN | 99.55 | 0.0018 | 0.002 ± 0.126 | 0.091 ± 0.380 | 0.093 ± 0.401 |
| MNIST | DE | 99.32 | 0.0012 | 0.002 ± 0.072 | 0.067 ± 0.320 | 0.070 ± 0.331 |
| MNIST | EDL | 94.42 | 0.2418 | 0.00007 ± 0.002 | 2.260 ± 0.054 | 2.260 ± 0.054 |
| MNIST | CreINN | 98.23 | 0.0105 | 0.071 ± 0.609 | 0.005 ± 0.043 | 0.077 ± 0.612 |
| MNIST | E-CNN | 99.27 | 0.7878 | 0.037 ± 0.065 | 1.608 ± 0.004 | 1.645 ± 0.064 |
| MNIST | RS-NN | 99.71 | 0.0059 | 0.053 ± 0.740 | 0.001 ± 0.016 | 0.054 ± 0.741 |
| MNIST | CNN | 98.90 | 0.0057 | 0.043 ± 0.497 | 0.000 ± 0.000 | 0.043 ± 0.497 |
| MNIST | LB-BNN Avg | 99.55 | 0.0018 | 0.016 ± 0.251 | 0.000 ± 0.000 | 0.016 ± 0.251 |
| MNIST | DE Avg | 99.32 | 0.0012 | 0.020 ± 0.198 | 0.000 ± 0.000 | 0.020 ± 0.198 |
| MNIST | DDU | 99.28 | 0.0028 | 0.028 ± 0.336 | 0.000 ± 0.000 | 0.028 ± 0.336 |
| CIFAR-100 | LB-BNN | 71.34 | 0.1332 | 0.146 ± 0.504 | 2.348 ± 1.771 | 2.494 ± 1.781 |
| CIFAR-100 | DE | 74.08 | 0.0377 | 0.019 ± 0.245 | 3.182 ± 1.909 | 3.201 ± 1.906 |
| CIFAR-100 | EDL | 45.76 | 0.3558 | 0.010 ± 0.192 | 3.434 ± 1.843 | 3.445 ± 1.840 |
| CIFAR-100 | CreINN | 44.30 | 0.1831 | 0.723 ± 0.646 | 2.050 ± 1.188 | 2.774 ± 0.945 |
| CIFAR-100 | E-CNN | - | - | - | - | - |
| CIFAR-100 | RS-NN | 71.17 | 0.1336 | 1.518 ± 3.966 | 0.569 ± 1.164 | 2.088 ± 4.025 |
| CIFAR-100 | CNN | 65.51 | 0.2357 | 2.293 ± 4.199 | 0.000 ± 0.000 | 2.293 ± 4.199 |
| CIFAR-100 | LB-BNN Avg | 71.34 | 0.1332 | 1.617 ± 2.886 | 0.000 ± 0.000 | 1.617 ± 2.886 |
| CIFAR-100 | DE Avg | 74.08 | 0.0377 | 1.062 ± 1.924 | 0.000 ± 0.000 | 1.062 ± 1.924 |
| CIFAR-100 | DDU | 73.44 | 0.1142 | 1.180 ± 2.260 | 0.000 ± 0.000 | 1.180 ± 2.260 |

**Non-specificity (NS).** For models making pointwise predictions, Non-Specificity (NS) is trivially zero, as the credal set reduces to a single point (Sec. 8.2.4). it also means that models capable of expressing meaningful imprecision, such as RS-NN, EDL, and E-CNN, are inherently penalized on this metric, especially when the trade-off parameter λ places more weight on minimizing imprecision. This should be kept in mind when interpreting comparative performance, as the unified score may favor overconfident point predictors at high λ values. For all other models, NS (Eq. 8.6) is shown in Fig. 8.2(b), and is generally broadly distributed across all models except, again, E-CNN and EDL, for both correct and incorrect predictions. Both E-CNN and EDL exhibits high non-specificity for all predictions, indicating that it is a more imprecise, less informative model.

**Evaluation Metric ($\mathcal{E}$).** For point predictions, the Evaluation Metric ($\mathcal{E}$) reduces to the KL divergence between ground truth and the prediction. Fig. 8.2(c) shows the Evaluation Metric

<!-- page: 113 -->

[FIGURE: Figure 8.2: Measures of KL divergence (a)(top left), (b) Non-specificity (top right), (c) Evaluation Metric (bottom left) for both Correctly (CC) and Incorrectly Classified (ICC) samples from CIFAR-10, and (d) Evaluation metric vs. trade-off parameter (bottom right), for all models, on the CIFAR-10 dataset.]

Text in figure: four sub-plots. Top-left: "Kullback-Leibler (KL) Divergence for Correct and Incorrect Predictions" — violin plots for models LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU (x-axis), y-axis "KL Divergence" 0 to 25, legend "Correct"/"Incorrect". Top-right: "Non-Specificity (NS) for Correct and Incorrect Predictions" — same models, y-axis "Non-Specificity (NS)" -0.5 to 2.5. Bottom-left: "Evaluation Metric (E) using KL divergence" — same models, y-axis "Evaluation Metric (E)" 0 to 25. Bottom-right: "Evaluation Metric (E) vs. Trade-off (λ) for Each Model" — bar chart, x-axis "Trade-off (λ)" 0.1 to 1, y-axis "Evaluation Metric (E)" 0 to 3.0, legend listing LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU.

[FIGURE: Figure 8.3: Measures of (a)(top left) Kullback-Leibler (KL) divergence, (b)(top right) Non-specificity (NS), (c)(bottom left) Evaluation Metric (E) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples (d)(bottom right) Evaluation metric (E) estimates vs. trade-off (λ) for all models on MNIST.]

Text in figure: same four-panel layout as Fig. 8.2 (KL divergence violin plots top-left, Non-Specificity violin plots top-right, Evaluation Metric violin plots bottom-left, Evaluation Metric vs. Trade-off (λ) bottom-right), but for the MNIST dataset, with the same set of models on the x-axis/legend (LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU).

<!-- page: 114 -->

[FIGURE: Figure 8.4: Measures of (a)(top left) Kullback-Leibler (KL) divergence, (top right) Non-specificity (NS), (c)(bottom left) Evaluation Metric (E) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples (d)(bottom right) Evaluation metric (E) estimates vs. trade-off (λ) for all models on CIFAR-100.]

Text in figure: same four-panel layout as Figs. 8.2 and 8.3 (KL divergence, Non-Specificity, Evaluation Metric violin plots, and Evaluation Metric vs. Trade-off (λ) bar chart with y-axis up to 8), for the CIFAR-100 dataset, with models LB-BNN, DE, CreINN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU on the x-axis/legend.

(E) for all models with the trade-off parameter λ = 1. One can see that, when adding NS to the mix, the concentrated distributions observed in the KL divergence for correct predictions become more distributed. Higher NS means that the credal set is larger, which causes more variability in $\mathcal{E}$. EDL shows the lowest KL for both correct and incorrect predictions across datasets but struggles with non-specificity (unusually high overall), while DE and LB-BNN balance low KL with better uncertainty handling, showing higher NS for incorrect predictions and RS-NN performs consistently well on $\mathcal{E}$ for correct predictions. A more detailed discussion can be found in Tab. 8.7, Sec. 8.4.5.1.

The distributions of KL-divergence, non-specificity and evaluation metric $\mathcal{E}$ for correct and

<!-- page: 115 -->

incorrect samples on MNIST and CIFAR-100 datasets for all models are illustrated in Figs. 8.3 and 8.4, respectively. For point predictions, however, the non-specificity is 0, thus the Evaluation Metric ($\mathcal{E}$) reduces to just the KL divergence between ground truth and the prediction. Figs. 8.3(c) and 8.4(c) shows the Evaluation Metric ($\mathcal{E}$) for all models with the trade-off parameter λ = 1. All the models exhibit very concentrated distributions for KL-divergence for correct samples for both datasets, while non-specificity, and consquently, evaluation metric $\mathcal{E}$ appears more distributed. Incorrect samples, on the other hand, show more smooth distributions for all.

#### 8.4.3 Evaluation of the Trade-off Parameter

In Fig. 8.2(d), a box plot is used to show the variation in Evaluation Metric ($\mathcal{E}$) values across different trade-off (λ) settings for each model. Each box in the plot represents the spread of $\mathcal{E}$ values for a specific model. The bottom and top edges of the box correspond to the 25% and 75% percentiles, respectively, while the horizontal lines (orange) inside the boxes indicate the median $\mathcal{E}$ value. Note that the y-axis range for $\mathcal{E}$ in Fig. 8.2(d) is noticeably smaller compared to the corresponding Fig. 8.2(c), despite both plots displaying $\mathcal{E}$ values. This difference arises because Fig. 8.2(d) uses box plots, which suppresses the display of outlier values. As a result, the y-axis is automatically scaled to reflect only the range of non-outlier $\mathcal{E}$ values. In contrast, Fig. 8.2(c) visualizes the entire distribution of $\mathcal{E}$ using violin plots, which include all data points including outliers and extreme values. This results in a much broader y-axis range (up to 25), capturing the full variation in the data.

For LB-BNN, DE, and CreINN, $\mathcal{E}$ steadily increases with λ, reflecting low KL and moderate non-specificity, also shown in Tab. 8.3. In contrast, E-CNN and EDL show a shift in the range of $\mathcal{E}$ across λ values while maintaining a consistent plot height, indicating very low KL and unusually high NS. This means that despite changes in the trade-off parameter λ, the variation of the evaluation metric $\mathcal{E}$ for E-CNN and EDL remains largely unchanged. These models appear to be *highly imprecise* under all conditions. For MNIST (Fig. 8.3(d)), all the models except E-CNN show relatively consistent values across all values λ, indicating that the models are very precise for this dataset. Whereas, for CIFAR-100 (Figs. 8.4(d)), there is a noticeable trend of increasing $\mathcal{E}$ values as λ grows showcasing the potential of trade-off parameter for model selection.

In Tab. 8.3, the MNIST results show that DE has the lowest $\mathcal{E}$ for λ values 0.1 to 0.7. therefore, the model selection will return DE as the best model. As λ increases from 0.7 to 1, RS-NN has the lowest scores and the model selection procedure returns RS-NN as the best model. Overall, these are models with low $\mathcal{E}$ scores. These results are also reflected in Tab. 8.5. In the CIFAR-100 dataset, the results are even more pronounced. The evaluation metric $\mathcal{E}$ start at a relatively high baseline for most models. The standard deviations also illustrate substantial variability among models, particularly at higher λ values, where some models demonstrate higher susceptibility to the increase in non-specificity.

#### 8.4.4 Model Selection Using the Evaluation Metric

Tab. 8.4 ranks all models on the basis of the mean value of the evaluation metric $\mathcal{E}$ on CIFAR-10, across different values of λ (Tabs. 8.5, 8.6 for MNIST, CIFAR-100). Lower values indicate better model performance. Here we have excluded models predicting point estimates to better show the effect of the trade-off parameter on $\mathcal{E}$.

<!-- page: 116 -->

Table 8.3: Trade-off (λ) vs. Evaluation Metric ($\mathcal{E}$) for different values of λ for the CIFAR-10 dataset.

| Dataset | Trade-off parameter (λ) | LB-BNN | DE | EDL | CreINN | E-CNN | RS-NN |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | 0.1 | 0.259 ± 1.316 | 0.069 ± 0.375 | 0.229 ± 0.012 | 0.117 ± 0.382 | 0.354 ± 0.215 | 0.399 ± 1.895 |
| CIFAR-10 | 0.2 | 0.276 ± 1.319 | 0.108 ± 0.395 | 0.455 ± 0.016 | 0.177 ± 0.407 | 0.515 ± 0.215 | 0.400 ± 1.896 |
| CIFAR-10 | 0.3 | 0.293 ± 1.323 | 0.146 ± 0.426 | 0.682 ± 0.022 | 0.237 ± 0.445 | 0.676 ± 0.215 | 0.401 ± 1.896 |
| CIFAR-10 | 0.4 | 0.309 ± 1.327 | 0.184 ± 0.467 | 0.909 ± 0.029 | 0.296 ± 0.494 | 0.837 ± 0.215 | 0.402 ± 1.897 |
| CIFAR-10 | 0.5 | 0.326 ± 1.334 | 0.223 ± 0.514 | 1.135 ± 0.035 | 0.356 ± 0.550 | 0.998 ± 0.215 | 0.403 ± 1.897 |
| CIFAR-10 | 0.6 | 0.342 ± 1.341 | 0.261 ± 0.566 | 1.362 ± 0.042 | 0.415 ± 0.612 | 1.159 ± 0.215 | 0.404 ± 1.898 |
| CIFAR-10 | 0.7 | 0.359 ± 1.349 | 0.300 ± 0.622 | 1.588 ± 0.049 | 0.475 ± 0.679 | 1.319 ± 0.215 | 0.405 ± 1.898 |
| CIFAR-10 | 0.8 | 0.376 ± 1.359 | 0.338 ± 0.681 | 1.815 ± 0.056 | 0.535 ± 0.748 | 1.480 ± 0.215 | 0.405 ± 1.899 |
| CIFAR-10 | 0.9 | 0.392 ± 1.369 | 0.377 ± 0.742 | 2.042 ± 0.063 | 0.594 ± 0.819 | 1.641 ± 0.215 | 0.406 ± 1.899 |
| CIFAR-10 | 1 | 0.409 ± 1.381 | 0.415 ± 0.805 | 2.268 ± 0.070 | 0.654 ± 0.892 | 1.802 ± 0.215 | 0.407 ± 1.900 |
| MNIST | 0.1 | 0.011 ± 0.132 | 0.009 ± 0.080 | 0.226 ± 0.005 | 0.072 ± 0.609 | 0.198 ± 0.065 | 0.053 ± 0.740 |
| MNIST | 0.2 | 0.020 ± 0.147 | 0.016 ± 0.098 | 0.452 ± 0.011 | 0.072 ± 0.609 | 0.359 ± 0.065 | 0.053 ± 0.740 |
| MNIST | 0.3 | 0.030 ± 0.170 | 0.023 ± 0.123 | 0.678 ± 0.016 | 0.073 ± 0.610 | 0.519 ± 0.065 | 0.053 ± 0.740 |
| MNIST | 0.4 | 0.039 ± 0.198 | 0.029 ± 0.150 | 0.905 ± 0.021 | 0.074 ± 0.610 | 0.680 ± 0.064 | 0.053 ± 0.740 |
| MNIST | 0.5 | 0.048 ± 0.229 | 0.036 ± 0.179 | 1.131 ± 0.027 | 0.074 ± 0.610 | 0.841 ± 0.064 | 0.053 ± 0.740 |
| MNIST | 0.6 | 0.057 ± 0.261 | 0.043 ± 0.208 | 1.357 ± 0.032 | 0.075 ± 0.611 | 1.002 ± 0.064 | 0.053 ± 0.741 |
| MNIST | 0.7 | 0.066 ± 0.295 | 0.050 ± 0.239 | 1.583 ± 0.037 | 0.075 ± 0.611 | 1.163 ± 0.064 | 0.054 ± 0.741 |
| MNIST | 0.8 | 0.075 ± 0.330 | 0.056 ± 0.269 | 1.809 ± 0.043 | 0.076 ± 0.611 | 1.324 ± 0.064 | 0.054 ± 0.741 |
| MNIST | 0.9 | 0.084 ± 0.366 | 0.063 ± 0.300 | 2.035 ± 0.048 | 0.076 ± 0.612 | 1.484 ± 0.064 | 0.054 ± 0.741 |
| MNIST | 1 | 0.093 ± 0.401 | 0.070 ± 0.331 | 2.261 ± 0.053 | 0.077 ± 0.612 | 1.645 ± 0.064 | 0.054 ± 0.741 |
| CIFAR-100 | 0.1 | 0.381 ± 0.514 | 0.337 ± 0.299 | 0.354 ± 0.257 | 0.929 ± 0.582 | - | 1.575 ± 3.957 |
| CIFAR-100 | 0.2 | 0.616 ± 0.580 | 0.656 ± 0.437 | 0.697 ± 0.404 | 1.134 ± 0.536 | - | 1.632 ± 3.951 |
| CIFAR-100 | 0.3 | 0.850 ± 0.686 | 0.974 ± 0.605 | 1.041 ± 0.573 | 1.339 ± 0.514 | - | 1.689 ± 3.948 |
| CIFAR-100 | 0.4 | 1.085 ± 0.818 | 1.292 ± 0.784 | 1.384 ± 0.749 | 1.544 ± 0.519 | - | 1.746 ± 3.949 |
| CIFAR-100 | 0.5 | 1.320 ± 0.964 | 1.610 ± 0.967 | 1.727 ± 0.929 | 1.749 ± 0.550 | - | 1.803 ± 3.953 |
| CIFAR-100 | 0.6 | 1.555 ± 1.119 | 1.928 ± 1.153 | 2.071 ± 1.110 | 1.954 ± 0.603 | - | 1.860 ± 3.961 |
| CIFAR-100 | 0.7 | 1.789 ± 1.280 | 2.247 ± 1.340 | 2.414 ± 1.291 | 2.159 ± 0.673 | - | 1.917 ± 3.972 |
| CIFAR-100 | 0.8 | 2.024 ± 1.444 | 2.565 ± 1.528 | 2.758 ± 1.474 | 2.364 ± 0.756 | - | 1.974 ± 3.986 |
| CIFAR-100 | 0.9 | 2.259 ± 1.612 | 2.883 ± 1.717 | 3.101 ± 1.657 | 2.569 ± 0.847 | - | 2.031 ± 4.004 |
| CIFAR-100 | 1 | 2.494 ± 1.781 | 3.201 ± 1.906 | 3.445 ± 1.840 | 2.774 ± 0.945 | - | 2.088 ± 4.025 |

Table 8.4: Model Rankings Based on KL and NS on CIFAR-10 for different values of λ. Model selection is based on the mean of Evaluation Metric ($\mathcal{E}$) with models with the lowest $\mathcal{E}$ ranking first.

| Trade-off (λ) | Model Ranking | Evaluation (E) Mean |
|---|---|---|
| 0.1 | DE, CreINN, EDL, LB-BNN, E-CNN, RS-NN | [0.069, 0.117, 0.229, 0.259, 0.354, 0.399] |
| 0.2 | DE, CreINN, LB-BNN, RS-NN, EDL, E-CNN | [0.108, 0.177, 0.276, 0.309, 0.456, 0.515] |
| 0.3 | DE, CreINN, LB-BNN, RS-NN, E-CNN, EDL | [0.146, 0.237, 0.293, 0.309, 0.676, 0.682] |
| 0.4 | DE, CreINN, LB-BNN, RS-NN, E-CNN, EDL | [0.184, 0.296, 0.309, 0.402, 0.837, 0.909] |
| 0.5 | DE, LB-BNN, CreINN, RS-NN, E-CNN, EDL | [0.223, 0.326, 0.356, 0.403, 0.998, 1.136] |
| 0.6 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.261, 0.342, 0.404, 0.415, 1.159, 1.363] |
| 0.7 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.300, 0.359, 0.405, 0.475, 1.319, 1.589] |
| 0.8 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.338, 0.376, 0.405, 0.535, 1.480, 1.816] |
| 0.9 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.377, 0.392, 0.406, 0.594, 1.641, 2.043] |
| 1.0 | RS-NN, LB-BNN, DE, CreINN, E-CNN, EDL | [0.407, 0.409, 0.415, 0.654, 1.802, 2.270] |

DE consistently ranks first for most λ values, followed by CreINN and LB-BNN. As λ increases, RS-NN shows improved performance, ranking first at λ = 1.0. E-CNN and EDL perform worse overall, especially at higher λ values, where their $\mathcal{E}$ values are significantly higher. Models like DE and CreINN rank higher at lower λ values (i.e. , leaning towards imprecision in low-risk tasks like crop disease classification), while models like RS-NN and LB-BNN perform better at higher λ values (penalizing imprecision in high-risk scenarios, such as autonomous driving). An

<!-- page: 117 -->

example of practical utility of the metric is given in Sec. 8.3.4.

Table 8.5: Model Selection Based on Evaluation Metric using KL and Non-Specificity on MNIST.

| Trade-off (λ) | Model Ranking | Evaluation (E) Mean |
|---|---|---|
| 0.1 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.009, 0.011, 0.053, 0.072, 0.198, 0.226] |
| 0.2 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.016, 0.020, 0.053, 0.072, 0.359, 0.452] |
| 0.3 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.023, 0.030, 0.053, 0.073, 0.519, 0.678] |
| 0.4 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.029, 0.039, 0.053, 0.074, 0.680, 0.904] |
| 0.5 | DE, LB-BNN, RS-NN, CreINN, E-CNN, EDL | [0.036, 0.048, 0.053, 0.074, 0.841, 1.130] |
| 0.6 | DE, RS-NN, LB-BNN, CreINN, E-CNN, EDL | [0.043, 0.053, 0.057, 0.075, 1.002, 1.356] |
| 0.7 | DE, RS-NN, LB-BNN, CreINN, E-CNN, EDL | [0.050, 0.054, 0.066, 0.075, 1.163, 1.582] |
| 0.8 | RS-NN, DE, LB-BNN, CreINN, E-CNN, EDL | [0.054, 0.056, 0.075, 0.076, 1.324, 1.808] |
| 0.9 | RS-NN, DE, CreINN, LB-BNN, E-CNN, EDL | [0.054, 0.063, 0.076, 0.084, 1.484, 2.034] |
| 1.0 | RS-NN, DE, CreINN, LB-BNN, E-CNN, EDL | [0.054, 0.070, 0.077, 0.093, 1.645, 2.260] |

Table 8.6: Model Selection Based on Evaluation Metric using KL and Non-Specificity on CIFAR-100.

| Trade-off (λ) | Model Ranking | Evaluation (E) Mean |
|---|---|---|
| 0.1 | DE, EDL, LB-BNN, CreINN, RS-NN | [0.337, 0.354, 0.381, 0.929, 1.575] |
| 0.2 | LB-BNN, DE, EDL, CreINN, RS-NN | [0.616, 0.656, 0.697, 1.134, 1.632] |
| 0.3 | LB-BNN, DE, EDL, CreINN, RS-NN | [0.850, 0.974, 1.041, 1.339, 1.689] |
| 0.4 | LB-BNN, DE, EDL, CreINN, RS-NN | [1.085, 1.292, 1.384, 1.544, 1.746] |
| 0.5 | LB-BNN, DE, EDL, CreINN, RS-NN | [1.320, 1.610, 1.727, 1.749, 1.803] |
| 0.6 | LB-BNN, RS-NN, DE, CreINN, EDL | [1.555, 1.860, 1.928, 1.954, 2.071] |
| 0.7 | LB-BNN, RS-NN, CreINN, DE, EDL | [1.789, 1.917, 2.159, 2.247, 2.414] |
| 0.8 | RS-NN, LB-BNN, CreINN, DE, EDL | [1.974, 2.024, 2.364, 2.565, 2.758] |
| 0.9 | RS-NN, LB-BNN, CreINN, DE, EDL | [2.031, 2.259, 2.569, 2.883, 3.101] |
| 1.0 | RS-NN, LB-BNN, CreINN, DE, EDL | [2.088, 2.494, 2.774, 3.201, 3.445] |

As λ approaches 1, RS-NN again is selected as the best model as shown in Tabs. 8.3, 8.5 and 8.6. The trends observed in the CIFAR-100 results further reinforce the need for careful tuning of λ to optimize model performance. As λ increases, the complexity of classification tasks also rises, necessitating models that can adaptively learn from both accurate and non-specific features.

#### 8.4.5 Ablation Studies

In this section, we will address the following questions based on our experimental findings:

- **Q1:** How does the evaluation metric behave for correct vs. incorrect classifications?
- **Q2:** How does approximating credal set vertices affect the metric?
- **Q3:** How do different distance and non-specificity measures affect evaluation outcomes?
- **Q4:** Why is distance a better choice than confidence score in the evaluation metric?
- **Q5:** How does non-specificity relate to credal set size as a measure of uncertainty?
- **Q6:** How does the number of prediction samples impact metric stability and performance?

<!-- page: 118 -->

##### 8.4.5.1 Metric Behavior For Correct (CC) Vs. Incorrect Classifications (ICC)

In Tab. 8.7, a comparison of KL divergence, Non-Specificity, and Evaluation Metric ($\mathcal{E}$) with trade-off λ = 1 is presented for Correctly Classified (CC) and Incorrectly Classified (ICC) samples across each model. Incorrect samples demonstrate a higher mean value than correct samples for KL divergence, Non-Specificity, and Evaluation Metric ($\mathcal{E}$) indicating that the models are behaving appropriately, except E-CNN which gives high non-specificity for both correct and incorrect predictions.

We can form a tentative ranking of the models with Tab. 8.7. For correct predictions of CIFAR-10, MNIST, and CIFAR-100, we desire low KL and low non-specificity, as exhibited by DE and RS-CNN respectively. For incorrect predictions, a low KL and high non-specificity is optimal. Finally, evaluation metric $\mathcal{E}$ (λ = 1) should reflect a low value for both correct and incorrect predictions (RS-NN and DE).

Table 8.7: Comparison of KL divergence (KL), Non-Specificity (NS), and Evaluation Metric ($\mathcal{E}$) (trade-off λ = 1) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples for each model on three datasets: CIFAR-10, MNIST, and CIFAR-100. *It is important to note that a low $\mathcal{E}$ for incorrect predictions can result from either low KL or low NS, so $\mathcal{E}$ alone cannot distinguish between confidently wrong (low NS, high KL) and uncertain but inaccurate (high NS, low KL) cases. Thus, $\mathcal{E}$ should be interpreted alongside KL and NS.*

| Dataset | Model | KL CC (↓) | KL ICC (↓) | NS CC (↓) | NS ICC (↑) | E CC (↓) | E ICC (↓) |
|---|---|---|---|---|---|---|---|
| CIFAR-10 | LB-BNN | 0.009 ± 0.038 | 2.181 ± 3.444 | 0.109 ± 0.323 | 0.637 ± 0.600 | 0.118 ± 0.341 | 2.818 ± 3.203 |
| CIFAR-10 | DE | 0.0001 ± 0.001 | 0.489 ± 1.395 | 0.306 ± 0.639 | 1.566 ± 0.756 | 0.306 ± 0.639 | 2.055 ± 1.183 |
| CIFAR-10 | EDL | 0.00005 ± 0.0002 | 0.0051 ± 0.017 | 2.253 ± 0.080 | 2.288 ± 0.034 | 2.253 ± 0.08 | 2.293 ± 0.023 |
| CIFAR-10 | CreINN | 0.003 ± 0.006 | 0.476 ± 1.001 | 0.465 ± 0.727 | 1.590 ± 0.731 | 0.468 ± 0.728 | 2.066 ± 0.744 |
| CIFAR-10 | E-CNN | 0.108 ± 0.093 | 0.625 ± 0.115 | 1.609 ± 0.003 | 1.610 ± 0.001 | 1.717 ± 0.092 | 2.235 ± 0.115 |
| CIFAR-10 | RS-NN | 0.009 ± 0.055 | 5.562 ± 4.747 | 0.004 ± 0.031 | 0.076 ± 0.145 | 0.013 ± 0.077 | 5.638 ± 4.691 |
| CIFAR-10 | CNN | 0.021 ± 0.090 | 4.735 ± 3.604 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.021 ± 0.090 | 4.735 ± 3.604 |
| CIFAR-10 | LB-BNN Avg | 0.034 ± 0.114 | 3.628 ± 3.145 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.034 ± 0.114 | 3.628 ± 3.145 |
| CIFAR-10 | DE Avg | 0.050 ± 0.135 | 2.378 ± 2.000 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.050 ± 0.135 | 2.378 ± 2.000 |
| CIFAR-10 | DDU | 0.031 ± 0.104 | 3.243 ± 2.196 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.031 ± 0.104 | 3.243 ± 2.196 |
| MNIST | LB-BNN | 0.00002 ± 0.001 | 0.490 ± 1.832 | 0.083 ± 0.359 | 1.883 ± 0.656 | 0.083 ± 0.359 | 2.373 ± 1.449 |
| MNIST | DE | 0.00005 ± 0.001 | 0.340 ± 0.805 | 0.058 ± 0.291 | 1.503 ± 0.766 | 0.058 ± 0.291 | 1.843 ± 0.758 |
| MNIST | EDL | 0.00006 ± 0.00002 | 0.00062 ± 0.005 | 2.255 ± 0.055 | 2.301 ± 0.010 | 2.255 ± 0.055 | 2.302 ± 0.007 |
| MNIST | CreINN | 0.006 ± 0.037 | 3.720 ± 2.714 | 0.004 ± 0.032 | 0.061 ± 0.212 | 0.010 ± 0.053 | 3.781 ± 2.664 |
| MNIST | E-CNN | 0.032 ± 0.033 | 0.675 ± 0.115 | 1.608 ± 0.004 | 1.607 ± 0.003 | 1.641 ± 0.032 | 2.282 ± 0.116 |
| MNIST | RS-NN | 0.001 ± 0.023 | 6.211 ± 5.290 | 0.0004 ± 0.010 | 0.056 ± 0.120 | 0.002 ± 0.031 | 6.267 ± 5.242 |
| MNIST | CNN | 0.004 ± 0.040 | 3.484 ± 3.234 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.004 ± 0.040 | 3.484 ± 3.234 |
| MNIST | LB-BNN Avg | 0.006 ± 0.044 | 2.295 ± 2.921 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.006 ± 0.044 | 2.295 ± 2.921 |
| MNIST | DE Avg | 0.007 ± 0.048 | 1.956 ± 1.287 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.007 ± 0.048 | 1.956 ± 1.287 |
| MNIST | DDU | 0.003 ± 0.032 | 3.367 ± 2.092 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.003 ± 0.032 | 3.367 ± 2.092 |
| CIFAR-100 | LB-BNN | 0.006 ± 0.021 | 0.399 ± 0.783 | 1.790 ± 1.748 | 3.353 ± 1.309 | 1.796 ± 1.752 | 3.752 ± 0.947 |
| CIFAR-100 | DE | 0.0001 ± 0.001 | 0.074 ± 0.477 | 2.780 ± 2.013 | 4.331 ± 0.836 | 2.780 ± 2.013 | 4.405 ± 0.690 |
| CIFAR-100 | EDL | 0.005 ± 0.190 | 0.015 ± 0.194 | 2.629 ± 2.086 | 4.114 ± 1.258 | 2.634 ± 2.090 | 4.129 ± 1.238 |
| CIFAR-100 | CreINN | 0.310 ± 0.321 | 0.857 ± 0.668 | 1.483 ± 1.132 | 2.232 ± 1.147 | 1.792 ± 1.131 | 3.089 ± 0.599 |
| CIFAR-100 | E-CNN | - | - | - | - | - | - |
| CIFAR-100 | RS-NN | 0.042 ± 0.130 | 4.539 ± 5.857 | 0.242 ± 0.760 | 1.239 ± 1.510 | 0.284 ± 0.783 | 5.777 ± 5.276 |
| CIFAR-100 | CNN | 0.063 ± 0.165 | 6.528 ± 4.868 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.063 ± 0.165 | 6.528 ± 4.868 |
| CIFAR-100 | LB-BNN Avg | 0.167 ± 0.255 | 4.235 ± 3.548 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.167 ± 0.255 | 4.235 ± 3.548 |
| CIFAR-100 | DE Avg | 0.284 ± 0.349 | 3.285 ± 2.696 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.284 ± 0.349 | 3.285 ± 2.696 |
| CIFAR-100 | DDU | 0.102 ± 0.228 | 4.161 ± 2.646 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.102 ± 0.228 | 4.161 ± 2.646 |

##### 8.4.5.2 The Effect of Approximating Credal Set Vertices

To demonstrate that the approximated vertices of the credal sets are sufficient (and often, even better), we consider a 4-class example of the CIFAR-10 dataset. In Tab. 8.8, we show the

<!-- page: 119 -->

evaluation metric $\mathcal{E}$ for computed using approximated credal vertices using the approach detailed above, and the naive credal set vertices computation given in Eq. 8.4. For the naive credal set, we use the complete 24 (4!) vertices and for the approximated credal set, we use a reduced number of 8 vertices. The values in bold are the clearly better results whereas other values are quite close to each other. For DEs, for instance, the approximated credal set is a better representation for our metric, as the approximation uses the most relevant permutations only.

Table 8.8: Comparison of KL, Non-Specificity, Evaluation Metric ($\mathcal{E}$) calculated using approximated versus naive credal set vertices for LB-BNN and DE on the CIFAR-10 dataset.

| Model | Credal Set Vertices | KL CC (↓) | KL ICC (↓) | NS CC (↓) | NS ICC (↑) | E CC (↓) | E ICC (↓) |
|---|---|---|---|---|---|---|---|
| LB-BNN | Approximated | 0.0046 ± 0.023 | 0.612 ± 0.3968 | 0.564 ± 0.099 | 0.611 ± 0.140 | 0.569 ± 0.104 | 1.225 ± 0.376 |
| LB-BNN | Naive | 0.005 ± 0.023 | 0.336 ± 0.666 | 0.033 ± 0.103 | 0.286 ± 0.216 | 0.039 ± 0.121 | 0.365 ± 0.594 |
| DE | Approximated | 0.0002 ± 0.002 | 0.142 ± 0.260 | 0.058 ± 0.125 | 0.801 ± 0.170 | 0.058 ± 0.125 | 0.944 ± 0.265 |
| DE | Naive | 0.0001 ± 0.002 | 0.335 ± 0.807 | 0.080 ± 0.204 | 0.656 ± 0.219 | 0.080 ± 0.205 | 0.991 ± 0.653 |

[FIGURE: Figure 8.5: Probability simplices illustrating the convex closure of predictions and credal sets for the Bayesian model (LB-BNN) across three classes of the CIFAR-10 dataset.]

Text in figure: three triangular probability simplices side by side, titled "True Class = automobile", "True Class = airplane", "True Class = airplane" respectively, each with vertices labeled "bird" (top), "airplane" (bottom left), "automobile" (bottom right), showing scattered orange sample points and a dashed convex hull. Legend for each: "Convex Closure of Predictions" (orange dashed line), "Credal Set Vertices" (red dashed line).

**Credal set vs. convex closure of predictions.** Since our metric uses the KL divergence between the ground truth and the closest vertex of the credal set (which is convex), the credal set representation does not affect its value as such vertices correspond to (some of) the original (e.g. Bayesian) predictions, as shown in Fig. 8.5. Probability simplices illustrating the convex closure of predictions and credal sets for LB-BNN (Bayesian) model are shown in Fig. 8.5, over three classes of CIFAR-10. The convex closure of predictions often coincides with the vertices of the credal set, indicating that some Bayesian predictions are situated exactly at the extremities of the credal set. There is a slight difference between the convex closure of predictions and the credal set, which is not due to vertex approximations. (Cozman, 2000) details how there is more than a single way to specify a set of distributions inducing a given lower envelope. The credal set in Fig. 8.5 has been approximated using coherent lower probabilities and have boundries parallel to that of the simplex.

**Computation of the credal set vertices.** Fig. 8.6 shows the sizes of the credal sets predicted by all models, for 50 prediction samples of the CIFAR-10 dataset. This is obtained by taking the difference between maximal and minimal extremal probability (Eq. 8.4) for the predicted class. Similarly, Figs. 8.7 and 8.8 demonstrate the sizes of the credal sets of the MNIST and CIFAR-100 datasets, respectively. A larger credal set size signifies that the model is highly uncertain about its predictions. E-CNN exhibits the widest credal set for all predictions, indicating significant imprecision regardless of whether the model predicts the correct or incorrect class. This is

<!-- page: 120 -->

[FIGURE: Figure 8.6: Credal set sizes for all models for 50 prediction samples of the CIFAR-10 dataset. Larger credal set sizes indicate a more imprecise prediction.]

Text in figure: line/area chart titled "Maximum and Minimum Values for Vertices of 50 Samples Across All Models", y-axis "Extremal Probability" 0.00 to 1.00, x-axis "Samples" 0 to 50, legend: LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL.

[FIGURE: Figure 8.7: Credal set sizes for all models for 50 prediction samples of the MNIST dataset. Larger credal set sizes indicate a more imprecise prediction]

Text in figure: same chart layout as Fig. 8.6 ("Maximum and Minimum Values for Vertices of 50 Samples Across All Models", y-axis "Extremal Probability" 0.00 to 1.00, x-axis "Samples" 0 to 50), legend: LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, for the MNIST dataset.

[FIGURE: Figure 8.8: Credal set sizes for all models for 50 prediction samples of the CIFAR-100 dataset. Larger credal set sizes indicate a more imprecise prediction]

Text in figure: same chart layout as Figs. 8.6–8.7, legend: LB-BNN, DE, CreINN, RS-NN, EDL, for the CIFAR-100 dataset.

undesirable, as it suggests a general lack of confidence in the predicted outcomes. Models with smaller credal set sizes demonstrate higher confidence in their predictions, implying more reliable and precise outcomes. Lower non-specificity values align with smaller credal widths, indicating smaller (epistemic) uncertainty and greater model confidence.

##### 8.4.5.3 Ablation Study On Different Distance Measures

In this section, we present an ablation study comparing different distance measures, specifically Kullback-Leibler (KL) divergence and Jensen-Shannon (JS) (Menéndez et al., 1997) divergence. The goal of this analysis is to assess how these divergence measures influence the evaluation of uncertainty in our framework. While KL divergence has been chosen for its superior ability, Jensen-Shannon divergence offers a symmetric alternative that handles small probabilities more gracefully. By experimenting with both measures, we provide insights into their respective advantages and determine the most suitable metric for capturing distributional differences in uncertainty-aware model predictions.

<!-- page: 121 -->

[FIGURE: Figure 8.9: Comparison of (a) Kullback-Leibler (KL) divergence, and (b) Jensen-Shannon (JS) divergence for Correctly Classified (CC) and Incorrectly Classified (ICC) samples from the CIFAR-10 dataset, for all models considered here. Notably, the scales of these two measures differ significantly (Y-axis).]

Text in figure: two violin plots side by side. (a) "Kullback-Leibler (KL) Divergence for Correct and Incorrect Predictions", y-axis "KL Divergence" 0 to 25, x-axis models LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU, legend "Correct"/"Incorrect". (b) "Jensen-Shannon (JS) Divergence for Correct and Incorrect Predictions", y-axis "JS Divergence" 0.0 to 1.0, same models and legend.

Fig. 8.9 illustrates the Kullback-Leibler (KL) divergence (8.9(a)) and Jensen-Shannon (JS) divergence (8.9(b)) between the ground truth probabilities and the vertices of the credal set on the CIFAR-10 dataset, over the entire test set. The violin plots depict distributions of the divergences for correct (blue) and incorrect (orange) predictions. Ideally, we expect the KL divergence to be larger for incorrect predictions, but not to an extent that it approaches a completely different class on the simplex of classes. This outcome indicates a preference for models that do not make severe misclassifications, which would be reflected in excessively predicting a wrong class. The plots reveal how the KL divergence for incorrect predictions often spans a wider range, indicating greater uncertainty in these predictions compared to correct ones. The JS divergence is presented on a smaller scale compared to the KL divergence.

Fig. 8.10 shows bar plots comparing the KL and JS divergences along with their influence on the overall evaluation metric and therefore, corresponding model rankings. All values are shown as means. Again, the differing ranges of KL and JS divergences are evident, with the Y-axis scaled equally for straightforward comparison. This discrepancy affects the overall evaluation metric $\mathcal{E}$. According to Algorithm 1 for model selection, the model with the smallest evaluation metric should be chosen.

**Model Selection.** In Tab. 8.9, we show the ranking of all models (including the models that predict point estimates) arranged in ascending order of the mean of the evaluation metric, $\mathcal{E}$. As λ increases, DE, which consistently ranked highly in KL divergence across lower λ values, is replaced by point prediction model, DE Avg (since it has zero non-specificity). LB-BNN and RS-NN show mixed performance, typically appearing in the top half but with varying positions.

In terms of JS divergence, RS-NN stands out as a top performer, frequently occupying the top spots across most λ values, while CNN also maintains a strong position, often ranking within the top three or four models. E-CNN and EDL tend to rank lower for both KL and JS measures. If we exclude the point prediction models from the ranking, both KL divergence and JS divergence consistently identify **RS-NN** and **DE** as the top two models in the model selection procedure.

It is worth noting that the rankings for different values of the trade-off parameter λ vary. This variation arises from the lack of adjustment for the range of λ across the different metrics. For instance, if the KL divergence ranges from 0 to 25, while the JS divergence spans from 0 to 1, we should consider scaling down

<!-- page: 122 -->

[FIGURE: Figure 8.10: Comparison of mean Evaluation Metric E using mean Kullback Leibler (KL) divergence (top) and mean Jensen-Shannon (JS) divergence (bottom) for Correct (left) and Incorrect (right) predictions of the CIFAR-10 dataset.]

Text in figure: four bar-chart panels, all y-axis "Average Values" 0 to 6, x-axis the models LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU. Top-left: "Evaluation Metric with KL divergence (Correct Predictions)", legend "KL Divergence"/"Non-Specificity"/"Evaluation Metric". Top-right: "Evaluation Metric with KL divergence (Incorrect Predictions)", same legend. Bottom-left: "Evaluation Metric with JS divergence (Correct Predictions)", legend "JS Divergence"/"Non-Specificity"/"Evaluation Metric". Bottom-right: "Evaluation Metric with JS divergence (Incorrect Predictions)", same legend.

Table 8.9: Model Rankings Based on KL and JS Divergence on the CIFAR-10 dataset. Model selection is based on the mean of Evaluation Metric ($\mathcal{E}$) with the models with the lowest $\mathcal{E}$ ranking first.

| Lambda | Metric | Model Ranking | Evaluation Metric (E) Mean |
|---|---|---|---|
| 0.1 | KL | DE, CreINN, DE Avg, EDL, LB-BNN, DDU, E-CNN, RS-NN, LB-BNN Avg, CNN | [0.069, 0.117, 0.195, 0.229, 0.259, 0.309, 0.354, 0.399, 0.420, 0.481] |
| 0.1 | JS | DE, RS-NN, LB-BNN, CNN, DE Avg, DDU, CreINN, LB-BNN Avg, EDL, E-CNN | [0.053, 0.065, 0.095, 0.098, 0.099, 0.109, 0.109, 0.119, 0.238, 0.373] |
| 0.2 | KL | DE, CreINN, DE Avg, LB-BNN, DDU, RS-NN, LB-BNN Avg, EDL, CNN, E-CNN | [0.108, 0.177, 0.195, 0.276, 0.309, 0.400, 0.420, 0.456, 0.481, 0.515] |
| 0.2 | JS | RS-NN, DE, CNN, DE Avg, DDU, LB-BNN, LB-BNN Avg, CreINN, EDL, E-CNN | [0.066, 0.091, 0.098, 0.099, 0.109, 0.111, 0.119, 0.169, 0.464, 0.534] |
| 0.3 | KL | DE, DE Avg, CreINN, LB-BNN, DDU, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.146, 0.195, 0.237, 0.293, 0.309, 0.401, 0.420, 0.481, 0.676, 0.682] |
| 0.3 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, EDL, E-CNN | [0.067, 0.098, 0.099, 0.109, 0.119, 0.128, 0.130, 0.229, 0.691, 0.695] |
| 0.4 | KL | DE, DE Avg, CreINN, DDU, LB-BNN, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.184, 0.195, 0.296, 0.309, 0.309, 0.402, 0.420, 0.481, 0.837, 0.909] |
| 0.4 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.068, 0.098, 0.099, 0.109, 0.119, 0.145, 0.168, 0.288, 0.856, 0.918] |
| 0.5 | KL | DE Avg, DE, DDU, LB-BNN, CreINN, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.195, 0.223, 0.309, 0.326, 0.356, 0.403, 0.420, 0.481, 0.998, 1.136] |
| 0.5 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.069, 0.098, 0.099, 0.109, 0.119, 0.161, 0.206, 0.348, 1.017, 1.145] |
| 0.6 | KL | DE Avg, DE, DDU, LB-BNN, RS-NN, CreINN, LB-BNN Avg, CNN, E-CNN, EDL | [0.195, 0.261, 0.309, 0.342, 0.404, 0.415, 0.420, 0.481, 1.159, 1.363] |
| 0.6 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.070, 0.098, 0.099, 0.109, 0.119, 0.178, 0.245, 0.407, 1.178, 1.371] |
| 0.7 | KL | DE Avg, DE, DDU, LB-BNN, RS-NN, LB-BNN Avg, CreINN, CNN, E-CNN, EDL | [0.195, 0.300, 0.309, 0.359, 0.405, 0.420, 0.475, 0.481, 1.319, 1.589] |
| 0.7 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.071, 0.098, 0.099, 0.109, 0.119, 0.194, 0.283, 0.467, 1.338, 1.598] |
| 0.8 | KL | DE Avg, DDU, DE, LB-BNN, RS-NN, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.338, 0.376, 0.405, 0.420, 0.481, 0.535, 1.480, 1.816] |
| 0.8 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.072, 0.098, 0.099, 0.109, 0.119, 0.211, 0.322, 0.527, 1.499, 1.825] |
| 0.9 | KL | DE Avg, DDU, DE, LB-BNN, RS-NN, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.377, 0.392, 0.406, 0.420, 0.481, 0.594, 1.641, 2.043] |
| 0.9 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.072, 0.098, 0.099, 0.109, 0.119, 0.228, 0.360, 0.586, 1.660, 2.052] |
| 1.0 | KL | DE Avg, DDU, RS-NN, LB-BNN, DE, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.407, 0.409, 0.415, 0.420, 0.481, 0.654, 1.802, 2.270] |
| 1.0 | JS | RS-NN, CNN, DE Avg, DDU, LB-BNN Avg, LB-BNN, DE, CreINN, E-CNN, EDL | [0.073, 0.098, 0.099, 0.109, 0.119, 0.250, 0.392, 0.681, 1.810, 2.280] |

that the influence of the JS divergence is properly scaled in the overall evaluation metric, we can define a scaling factor based on their maximum values: Scaling Factor = $\frac{\max(KL)}{\max(JS)} = \frac{25}{1} = 25$.

Given that KL divergence will generally dominate due to its larger range, we should scale down

<!-- page: 123 -->

[FIGURE: Figure 8.11: Scatter plots showing the relationship between uncertainty (KL and JS divergences) and non-specificity for correct and incorrect predictions across all models. Notably, the distinct 'spike' at non-specificity just above 1.5 highlights the characteristic output of a particular model.]

Text in figure: 2×2 grid of scatter plots. Top-left "Correct Predictions: KL Divergence vs Non-Specificity" (x-axis KL Divergence 0.0–1.2, y-axis Non-Specificity 0.0–2.0); top-right "Incorrect Predictions: KL Divergence vs Non-Specificity" (x-axis KL Divergence 0–20, y-axis Non-Specificity 0.0–2.0); bottom-left "Correct Predictions: JS Divergence vs Non-Specificity" (x-axis JS Divergence 0.0–0.7, y-axis Non-Specificity 0.0–2.0); bottom-right "Incorrect Predictions: JS Divergence vs Non-Specificity" (x-axis JS Divergence 0.0–0.8, y-axis Non-Specificity 0.0–2.0). Points colored blue (top row, KL) and green (bottom row, JS).

λ for the JS divergence. A suitable adjusted range for λ in the context of JS divergence can be expressed as: $\lambda_{JS} = \lambda \times \text{Scaling Factor} = \lambda \times \frac{1}{25}$. Thus, while λ initially ranges from 0 to 1, the effective range for $\lambda_{JS}$ will be from 0 to $\frac{1}{25}$. This adjustment ensures that both KL and JS divergences contribute appropriately to the overall evaluation metric $\mathcal{E}$, reflecting their respective scales during model selection.

In Fig. 8.11, the set of scatter plots visualizes the relationship between distance measures (KL and JS divergences) and non-specificity for correct (left) and incorrect (right) predictions across all models. The top row focuses on KL divergence, showing how it correlates with non-specificity for both correct and incorrect predictions. The bottom row highlights JS divergence with the same comparisons. Both KL and JS behave similarly for correct predictions. A straight horizontal line (spike) around NS ≈ 1.6 appears with varying KL and JS values, likely reflecting the behavior of E-CNN and EDL. Similarly, the concentrated spots in incorrect predictions may correspond to these models. As NS increases, KL decreases in all the plots, likely because larger credal sets at higher NS include vertices closer to the ground truth.

**Why choose KL divergence over JS divergence?** We selected KL divergence for our measure because, as shown in Fig. 8.10, JS is symmetric and bounded while KL divergence can grow unbounded when there is a significant mismatch between the predicted and true distributions, especially in small probabilities, making it more effective in distinguishing between correct and incorrect predictions. KL's greater sensitivity can provide a clearer signal when small deviations in probabilities matter, offering sharper differentiation in model evaluation. As Fig. 8.10 shows, KL offers a clearer separation between the two, with the plot showing the mean KL and JS values. This trend is further emphasized in Fig. 8.9 where the full distributions of KL

<!-- page: 124 -->

and JS are shown. Note that in Fig. 8.9, the ranges on the Y-axis differ significantly, with KL values spanning from 0 to 25, whereas JS values range only from 0 to 1.

##### 8.4.5.4 Ablation Study On Different Non-specificity Measures

In this section, we present an ablation study on the non-specificity (NS) measure in our evaluation metric $\mathcal{E}$. Non-specificity is in fact an epistemic uncertainty measure of the credal set, and can be replaced with other suitable uncertainty measures related to credal sets. In this ablation, we present an alternative to the Dubois and Prade (1987) equation (Eq. 8.6) that we use, in the form of a different measure of credal uncertainty (CU) (Wang et al., 2024b).

This credal uncertainty (CU) measure can be computed as the difference between the credal upper bound $\overline{H}(\hat{\mathbb{C}re})$ and lower bounds $\underline{H}(\hat{\mathbb{C}re})$ computed as follows. Given a set of K individual predictive distributions from Bayesian Neural Networks, evidential models or deep ensembles, we can obtain an upper and lower probability bound for the $c_i$-th class element, denoted as $\overline{P}_{c_i}$ and $\underline{P}_{c_i}$, respectively. Recall that $\mathbf{Y} = \{c_i, i\}$ where $i = 1, 2, \ldots, N$, and N is the number of classes in $\mathcal{C}$.

These bounds can be computed as follows: $\overline{P}_{c_i} = \max_{k=1,..,K} p_{k,c_i}$, $\underline{P}_{c_i} = \min_{k=1,..,K} p_{k,c_i}$, where $p_{k,c_i}$ denotes the $c_i$-th class element of the k-th single probability vector $\mathbf{p}_k$. Such probability intervals over $\mathcal{C}$ classes define a non-empty credal set $\hat{\mathbb{C}re}$:

$$
\hat{\mathbb{C}re} = \{\mathbf{p} \mid \underline{P}_{c_i} \leq p_{c_i} \leq \overline{P}_{c_i}, \forall c_i \in \mathcal{C}, i = 1, 2, \ldots, N\}
$$

(8.7)

with the normalization condition: $\sum_{i=1}^{N} \underline{P}_{c_i} \leq 1 \leq \sum_{i=1}^{N} \overline{P}_{c_i}$.

It can be readily shown that the probability intervals given in the previous equations satisfy this condition, as follows:

$$
\sum_{i=1}^{N} \underline{P}_{c_i} = \sum_{i=1}^{N} \min_{k=1,..,K} p_{k,c_i} \leq \sum_{i=1}^{N} p_{k^*,c_i} = 1 \leq \sum_{i=1}^{N} \max_{k=1,..,K} p_{k,c_i} = \sum_{i=1}^{N} \overline{P}_{c_i},
$$

(8.8)

<!-- page: 125 -->

where $k^*$ is any index in $1, \ldots, K$ and $c_i \in \mathcal{C}$. To estimate the uncertainty using $\overline{H}(\hat{\mathbb{C}re})$ and $\underline{H}(\hat{\mathbb{C}re})$, we need to solve the following optimization problems:

$$
\overline{H}(\hat{\mathbb{C}re}) = \text{maximize} \sum_{i=1}^{N} -p_{c_i} \log_2 p_{c_i}, \quad \underline{H}(\hat{\mathbb{C}re}) = \text{minimize} \sum_{i=1}^{N} -p_{c_i} \log_2 p_{c_i},
$$

(8.9)

subject to the constraints: $\sum_{i=1}^{N} p_{c_i} = 1$, $p_{c_i} \in [\underline{P}_{c_i}, \overline{P}_{c_i}], \forall c_i$.

These optimization problems can be addressed using standard solvers, such as the SciPy optimization package (Virtanen et al., 2020).

Fig. 8.12 shows the Non-Specificity (NS) (8.12(a)) and Credal Uncertainty (CU) (8.12(b)) over the entire test set. The violin plots depict distributions of the NS and CU for correct (blue) and incorrect (orange) predictions. We expect the both the measures to be larger for incorrect predictions and smaller for correct predictions. The plots show how the range of both values differ, but the trend remains the same, except for E-CNN. Non-specificity for E-CNN is high for both correct and incorrect predictions.

[FIGURE: Figure 8.12: Comparison of (a) Non-Specificity (NS), and (b) Credal Uncertainty (CU) for Correctly Classified (CC) and Incorrectly Classified (ICC) samples from the CIFAR-10 dataset, for all models considered here. Notably, the scales of these two measures differ (Y-axis).]

Text in figure: two violin plots. (a) "Non-Specificity (NS) for Correct and Incorrect Predictions", y-axis "Non-Specificity (NS)" -0.5 to 2.5, models LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL, CNN, LB-BNN Avg, DE Avg, DDU. (b) "Credal Uncertainty for Correct and Incorrect Predictions", y-axis "Credal Uncertainty" 0.0 to 3.5, same models; legend "Correct"/"Incorrect" for both.

[FIGURE: Figure 8.13: Comparison of mean Evaluation Metric E using mean Non-Specificity (top) and mean Credal Uncertainty (bottom) for Correct (left) and Incorrect (right) predictions of the CIFAR-10 dataset.]

Text in figure: four bar-chart panels, y-axis "Average Values" 0 to 9, x-axis the same models. Top-left: "Evaluation Metric with Non-Specificity (Correct Predictions)", legend "KL Divergence"/"Non-Specificity"/"Evaluation Metric". Top-right: "Evaluation Metric with Non-Specificity (Incorrect Predictions)", same legend. Bottom-left: "Evaluation Metric with Credal Uncertainty (Correct Predictions)", legend "KL Divergence"/"Credal Uncertainty"/"Evaluation Metric". Bottom-right: "Evaluation Metric with Credal Uncertainty (Incorrect Predictions)", same legend.

Fig. 8.13 shows bar plots comparing Non-Specificity (NS) and Credal Uncertainty (CU) along with their influence on the overall evaluation metric. All values are shown as means. As discussed earlier, having larger upper bounds even for correct predictions often cause Credal Uncertainty to make the overall Evaluation Metric $\mathcal{E}$ larger.

**Model Selection.** Tab. 8.10, presents the rankings of various models based on their performance in terms of Non-Specificity (NS) and Credal Uncertainty (CU) on the CIFAR-10 dataset. The

<!-- page: 126 -->

rankings are derived from the Evaluation Metric ($\mathcal{E}$), where models are ordered by their mean $\mathcal{E}$ values. The models are assessed under different values of the parameter lambda, with lower $\mathcal{E}$ values indicating better performance. For instance, at a lambda value of 0.1, the top-ranked models for Non-Specificity are DE, CreINN, and DE Avg. Similarly, for Credal Uncertainty, DE Avg and DDU lead the rankings, emphasizing their effectiveness in managing credal uncertainty within the predictions.

Table 8.10: Model Rankings Based on Non-Specificity (NS) and Credal Uncertainty (CU) on the CIFAR-10 dataset. Model selection is based on the mean of Evaluation Metric ($\mathcal{E}$) with the models with the lowest $\mathcal{E}$ ranking first. The distance metric used here is KL divergence.

| Lambda | Metric | Model Ranking | Evaluation Metric (E) Mean |
|---|---|---|---|
| 0.1 | NS | DE, CreINN, DE Avg, EDL, LB-BNN, DDU, E-CNN, RS-NN, LB-BNN Avg, CNN | [0.069, 0.117, 0.195, 0.229, 0.259, 0.309, 0.354, 0.399, 0.420, 0.481] |
| 0.1 | CU | DE Avg, DDU, EDL, DE, CreINN, E-CNN, LB-BNN Avg, CNN, LB-BNN, RS-NN | [0.195, 0.309, 0.316, 0.357, 0.363, 0.410, 0.420, 0.481, 0.563, 0.726] |
| 0.2 | NS | DE, CreINN, DE Avg, LB-BNN, DDU, RS-NN, LB-BNN Avg, EDL, CNN, E-CNN | [0.108, 0.177, 0.195, 0.276, 0.309, 0.400, 0.420, 0.456, 0.481, 0.515] |
| 0.2 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, EDL, CreINN, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 0.627, 0.631, 0.668, 0.683, 0.883, 1.053] |
| 0.3 | NS | DE, DE Avg, CreINN, LB-BNN, DDU, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.146, 0.195, 0.237, 0.293, 0.309, 0.401, 0.420, 0.481, 0.676, 0.682] |
| 0.3 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, EDL, CreINN, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 0.844, 0.945, 0.973, 1.009, 1.202, 1.380] |
| 0.4 | NS | DE, DE Avg, CreINN, DDU, LB-BNN, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.184, 0.195, 0.296, 0.309, 0.309, 0.402, 0.420, 0.481, 0.837, 0.909] |
| 0.4 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, EDL, CreINN, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 1.061, 1.259, 1.279, 1.335, 1.522, 1.707] |
| 0.5 | NS | DE Avg, DE, DDU, LB-BNN, CreINN, RS-NN, LB-BNN Avg, CNN, E-CNN, EDL | [0.195, 0.223, 0.309, 0.326, 0.356, 0.403, 0.420, 0.481, 0.998, 1.136] |
| 0.5 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, EDL, CreINN, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 1.277, 1.573, 1.584, 1.661, 1.842, 2.034] |
| 0.6 | NS | DE Avg, DE, DDU, LB-BNN, RS-NN, CreINN, LB-BNN Avg, CNN, E-CNN, EDL | [0.195, 0.261, 0.309, 0.342, 0.404, 0.415, 0.420, 0.481, 1.159, 1.363] |
| 0.6 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, EDL, CreINN, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 1.494, 1.888, 1.889, 1.987, 2.162, 2.362] |
| 0.7 | NS | DE Avg, DE, DDU, LB-BNN, RS-NN, LB-BNN Avg, CreINN, CNN, E-CNN, EDL | [0.195, 0.300, 0.309, 0.359, 0.405, 0.420, 0.475, 0.481, 1.319, 1.589] |
| 0.7 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, CreINN, EDL, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 1.711, 2.194, 2.202, 2.313, 2.482, 2.689] |
| 0.8 | NS | DE Avg, DDU, DE, LB-BNN, RS-NN, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.338, 0.376, 0.405, 0.420, 0.481, 0.535, 1.480, 1.816] |
| 0.8 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, CreINN, EDL, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 1.928, 2.499, 2.516, 2.639, 2.802, 3.016] |
| 0.9 | NS | DE Avg, DDU, DE, LB-BNN, RS-NN, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.377, 0.392, 0.406, 0.420, 0.481, 0.594, 1.641, 2.043] |
| 0.9 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, CreINN, EDL, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 2.145, 2.805, 2.830, 2.965, 3.122, 3.343] |
| 1.0 | NS | DE Avg, DDU, RS-NN, LB-BNN, DE, LB-BNN Avg, CNN, CreINN, E-CNN, EDL | [0.195, 0.309, 0.407, 0.409, 0.415, 0.420, 0.481, 0.654, 1.802, 2.270] |
| 1.0 | CU | DE Avg, DDU, LB-BNN Avg, CNN, E-CNN, CreINN, EDL, DE, LB-BNN, RS-NN | [0.195, 0.309, 0.420, 0.481, 2.362, 3.110, 3.144, 3.292, 3.442, 3.671] |

As lambda increases, the rankings reveal variations in model performance across both metrics. Notably, while DE Avg and DDU consistently ranks highly across different lambda values, other models exhibit fluctuating positions. If we do not consider models that predict point predictions, since their NS and CU are zero and $\mathcal{E}$ is the same as KL, DE and E-CNN are the best ranked models for CU and DE and RS-NN are the best ranked models for NS.

**Why choose Non-Specificity (NS) over Credal Uncertainty?** We chose Non-Specificity (NS) over Credal Uncertainty (CU) for our measure because, as demonstrated in Fig. 8.12, CU struggles to differentiate the uncertainty between correct and incorrect predictions across all models. The mean CU remains high for both cases, as highlighted in Fig. 8.13. In contrast, NS offers a clearer distinction, with lower values for correct predictions and higher values for incorrect ones. CU, on the other hand, tends to exhibit a high upper bound for both correct and incorrect predictions, and remains consistently elevated for correct predictions regardless of the model's performance. This does not accurately reflect the true state of uncertainty within the credal set.

##### 8.4.5.5 Distance Measure Vs. Confidence Score

The choice of using distance instead of confidence in the proposed metric is motivated by the goal to capture the true nature of the prediction within the simplex and to properly characterize the credal set. A key issue with using confidence (the maximum predicted probability) is that many models, particularly standard neural networks, exhibit a problem of overconfidence even for wrong predictions. In contrast, models like Deep Ensembles are designed to mitigate overconfidence by

<!-- page: 127 -->

averaging predictions across different models. By using a distance metric, we can better capture the spread or diversity in the predicted probabilities across the output space instead of focusing solely on the confidence of predictions.

While predictive entropy is a well-known and effective method for quantifying total uncertainty, it is not useful here as we are mainly concerned with epistemic uncertainty. For instance, if infinite amounts of data were available (assuming this data is unbiased and free from measurement errors or artifacts), epistemic uncertainty (and credal set size) would reduce to zero whereas entropy will not necessarily be zero unless we have a fully confident prediction (100% confidence).

[FIGURE: Figure 8.14: Entropy vs. Confidence (top) and Non-Specificity vs. Confidence (bottom) for each of the models: (a) LB-BNN, (b) Deep Ensembles (DE), (c) CreINN, (d) E-CNN, (e) RS-NN and (f) EDL on the CIFAR-10 dataset. Entropy is strongly linked to confidence, whereas non-specificity shows minimal correlation with it.]

Text in figure: a grid of 2D histogram/heatmap panels, one pair per model (a)–(f) (LB-BNN, DE, CreINN, E-CNN, RS-NN, EDL). For each model, the top panel plots "Entropy" (or "Pignistic Entropy") vs. "Confidence", and the bottom panel plots "Non-Specificity" vs. "Confidence", with a "Log Frequency" colorbar.

Furthermore, as illustrated in Fig. 8.14 below, entropy is closely tied to confidence, while

<!-- page: 128 -->

non-specificity has little correlation with confidence. High confidence predictions lead to low entropy, while low confidence predictions result in higher entropy. However, when considering epistemic uncertainty, entropy alone may not provide a complete picture. It is also detailed in Song et al. (2018) (Sec. 3, page 5) that the entropy-based uncertainty measure mainly depends on the total distribution of probabilities without concern about the largest probability, whereas the non-specificity is related to the difference between the largest probability and other ones.

##### 8.4.5.6 Credal Set Size Vs. Non-specificity

[FIGURE: Figure 8.15: Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN, (e) E-CNN and (f) RS-NN on the CIFAR-10 dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend.]

Text in figure: a 2×3 grid of heatmap scatter panels titled "<Model>: Credal Set Size vs. Non-Specificity" for (a) LB-BNN, (b) DE, (c) EDL, (d) CreINN, (e) E-CNN, (f) RS-NN, each with x-axis "Non-Specificity" and y-axis "Credal Set Size" (0 to ~1), colored by a "Log Frequency" colorbar; each panel shows a diagonal band indicating direct correlation between the two quantities.

[FIGURE: Figure 8.16: Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN, (e) E-CNN and (f) RS-NN on the MNIST dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend.]

Text in figure: same 2×3 grid layout as Fig. 8.15 (x-axis "Non-Specificity", y-axis "Credal Set Size", "Log Frequency" colorbar, diagonal correlation band), for the MNIST dataset.

<!-- page: 129 -->

Figs. 8.15, 8.16 and 8.17 exhibits the correlation between credal set size and non-specificity for CIFAR-10, MNIST and CIFAR-100 respectively. Here, credal set size is computed by taking the average of the difference between maximal and minimal extremal probability Eq. 8.4 for each class, and non-specificity is obtained using Eq. 8.6.

There exists a direct correlation between the credal set size and non-specificity. This demonstrates the efficacy of using the non-specificity measure in the evaluation metric as it captures the uncertainty associated with model's prediction making the metric more wholesome. E-CNN produces a very wide credal set over all samples visualized in MNIST dataset indicating that it's a very imprecise model.

[FIGURE: Figure 8.17: Credal Set Size vs. Non-Specificity heatmap for (a) LB-BNN, (b) Deep Ensembles (DE), (c) EDL, (d) CreINN and (e) RS-NN on the CIFAR-100 dataset. Credal Set Size and Non-Specificity are directly correlated to each other. Log frequency is used to better showcase the trend.]

Text in figure: a grid of five heatmap scatter panels (a) LB-BNN, (b) DE, (c) EDL, (d) CreINN, (e) RS-NN (no E-CNN panel for CIFAR-100), x-axis "Non-Specificity" (up to ~4.6), y-axis "Credal Set Size" (0 to 1), "Log Frequency" colorbar, each showing a diagonal correlation band.

##### 8.4.5.7 Ablation On Number of Prediction Samples

In this ablation study, we investigate the impact of varying the number of prediction samples for LB-BNN (left) and the number of ensemble members for Deep Ensembles (DE) (right) on the evaluation metric $\mathcal{E}$, as shown in Fig. 8.18. We observe that increasing the number of samples consistently leads to an increase in the value of $\mathcal{E}$, with the effect being more pronounced for DE compared to LB-BNN.

Specifically, for LB-BNN, we vary the number of prediction samples (from posterior) from 50 to 500, while for DE, we evaluate ensemble sizes ranging from 5 to 30 networks. As the number of samples increases, the predictive distribution becomes more expressive, leading to a more comprehensive characterization of uncertainty. This results in a broader credal set, which in turn enhances the non-specificity component of the evaluation.

<!-- page: 130 -->

[FIGURE: Figure 8.18: Ablation study on the number of prediction samples of LB-BNN and the number of ensembles of DE with Evaluation Metric (E).]

Text in figure: two line charts. Left: "Evaluation metric for LB-BNN", x-axis "Prediction Sample Size" 100 to 500, y-axis approx. 0.40 to 0.47, an increasing curve. Right: "Evaluation metric for DE", x-axis "Ensemble size" 5 to 30, y-axis "Evaluation Metric (E)" approx. 0.40 to 0.65, an increasing curve.

### 8.5 Discussion and Implications

For uncertainty-aware models, evaluation should extend beyond simple accuracy. Instead, it should utilize the full information from predictions; for instance, multiple samples from a Bayesian posterior or predictions from each model in an ensemble contain information that is often smoothed out while averaging (Hinne et al., 2020; Graefe et al., 2015). Relying solely on correctness, using traditional metrics that assess whether the most probable class matches the ground truth, fails to capture critical information, such as the divergence of the prediction from the ground truth, the overall spread of the predictive distribution (represented by the credal set), and the robustness implied by this spread.

Moreover, constructing a compound metric by combining discrete accuracy with a continuous measure such as non-specificity may feel less principled. In contrast, both distance-based measures (e.g. , KL divergence) and the extent of the credal set (quantified via non-specificity) operate naturally within the geometry of the probability simplex. Rather than reducing predictions to binary decisions, this evaluation framework offers a more comprehensive and informative perspective on the performance of uncertainty-aware models.

By jointly evaluating the distance to the ground truth and the extent of predictive uncertainty, this framework enables more informative comparisons between models that may share similar accuracy but differ in how they express and manage uncertainty. It facilitates a holistic evaluation of both Bayesian and evidential models, allowing for a more principled assessment of model reliability across different uncertainty paradigms.

<!-- page: 131 -->

# Part IV

# APPLICATIONS

<!-- page: 132 -->

<!-- page: 133 -->

# 9 Random-Set Large Language Models

The success of Random-Set Neural Networks (RS-NNs) in classification (Chapter 5) offers a strong foundation for extending the random set framework to other domains. RS-NNs demonstrated that modeling predictions as distributions over sets of outcomes, rather than over single classes, yields superior performance in accuracy, calibration, adversarial robustness, and out-of-distribution (OoD) detection. Building on this theoretical and empirical foundation, RS-NNs can be naturally extended from vision-based classification to token prediction in Large Language Models (LLMs) as Random-Set Large Language Models (RS-LLMs).

Large Language Models (LLMs) (Achiam et al., 2023; Anil et al., 2023; Touvron et al., 2023) are typically trained to predict the next token from a fixed vocabulary, making next-token prediction essentially a classification problem. However, conventional LLMs output point estimates in the form of probability distributions and fail to quantify uncertainty. This becomes especially problematic when LLMs generate hallucinations, i.e., factually incorrect or ungrounded statements (Maynez et al., 2020). RS-LLMs resolve this by adapting RS-NN's belief-based prediction framework to LLMs, equipping them with the ability to express second-order uncertainty over token predictions. While LLMs are generally designed to produce plausible text rather than truth-grounded answers, our application focuses on supervised tasks (e.g., CoQA, OpenBookQA), where a ground truth is available. In this context, the LLM acts as a classifier over candidate answers or text spans, making the application of RS-NN possible.

### 9.1 Methodology

Just as RS-NNs predict belief functions over class labels, RS-LLMs predict belief functions over sets of vocabulary tokens. These belief functions, grounded in random set theory and belief function theory (Shafer, 1976; Cuzzolin, 2010c; 2018b), assign mass to subsets of the vocabulary instead of individual tokens. This extension is made computationally feasible by a budgeting technique: hierarchical clustering over token embeddings (Müllner, 2011; Ackermann et al., 2014), that selects a finite, informative set of token subsets (focal sets) over which the belief function is defined. The resulting belief function can be mapped to a credal set and its center, the pignistic distribution (Smets and Kennes, 1994), is used for actual token prediction. Fig. 9.1 shows the training and generation flow of RS-LLM.

This belief-based approach offers significant interpretive advantages. For instance, when an LLM predicts that 'Joe likes to play ___' and outputs a 50-50 split between 'baseball' and 'basketball', it is unclear whether this reflects indecision or dual correctness. By contrast, an RS-LLM can distinguish these possibilities through different belief assignments: mass on the

<!-- page: 134 -->

[FIGURE: Figure 9.1: Training and generation flow of RS-LLM. Training is performed in a parallel fashion using the teacher forcing method. Generation is done sequentially. For each token, the model predicts a belief function. Then the mass function, probability distribution and next token is subsequently computed/sampled from that belief function.]

Text in figure: two panels, "Training" and "Generation", separated by a dotted line. Training (left): three "Ground-truth" boxes feed into a "Bel Loss" computed from three "Bel" boxes below an "LLM" box, which takes inputs t1, t2, t3. Generation (right, shown as three sequential steps): each step shows an "LLM" box producing "Bel" box(es), then "Mass" box(es), then "Prob" box(es), then output token(s) o2, o3, o4 in sequence, with inputs growing from t1 to t1,o2 to t1,o2,o3.

joint set {baseball, basketball} indicates epistemic uncertainty (the model is unsure), while equal mass on individual tokens suggests both are plausible answers. Thus, RS-LLMs inherit RS-NN's ability to disambiguate types of uncertainty, bringing that clarity into the LLM domain.

Random-sets are defined on the power set of all subsets of their domain. However, this is computationally impossible when the domain cardinality is extremely large, as is the case for large language models where the typical size of vocabulary is ∼32K tokens. The number of subsets in this case would be an astronomical $2^{32K}$. Therefore, to tackle this problem, we need a method to select a budget of most appropriate focal sets and use only those as our focal sets. This is appropriate because, by intuition, the model will most likely be confused among tokens which are similar to each other and potentially have similar semantics (Farquhar et al., 2024).

As a first step, token embeddings are computed using a pre-trained LLM (in fact, any method for obtaining embedding of tokens can be used here). Then, hierarchical clustering is applied to cluster similar tokens. The number of clusters K is a hyper-parameter which determines the granularity of the belief function.

The final budget $\mathcal{O}$ of focal sets of the belief functions to be predicted is the union of the clusters of tokens so obtained and the collection of singleton sets containing the T original tokens, amounting to a total of $(K + T)$ sets. Fig. 9.2 shows a detailed overview of the proposed budgeting method. An analysis of the focal sets obtained by this budgeting strategy is presented in Sec. 9.2.5.

**Training** follows the teacher forcing paradigm (Williams and Zipser, 1989), where the model learns to predict belief functions token by token. During generation, belief functions are sequentially transformed into mass functions, from which pignistic probabilities are computed to generate the next token. This mirrors the RS-NN structure but adapts it to the autoregressive, sequential setting of LLMs. RS-LLM follows the loss function (Sec. 5.2.3) and uncertainty estimation techniques (Sec. 5.3.4) of RS-NN.

<!-- page: 135 -->

[FIGURE: Figure 9.2: Proposed budgeting method for RS-LLM. First, embeddings are computed for all the tokens in vocabulary. Then, focal sets are computed using hierarchical clustering.]

Text in figure: flow diagram. A vocabulary list ("football", "basketball", "poodle", "bulldog", "dog", "ship", ...) → "Embeddings" (row of embedding vectors) → "Clustering" (scatter plot showing two clusters, one labeled "football"/"basketball" and one labeled "poodle"/"dog"/"bulldog", plus an isolated point "ship") → final list of focal sets: {football}, {basketball}, {football, basketball}, {poodle}, {bulldog}, {dog}, {poodle, dog, bulldog}, {ship}, ...

### 9.2 Experiments

#### 9.2.1 Implementation

**Datasets.** RS-LLM is evaluated on two QA benchmarks: CoQA (Reddy et al., 2019), a generative dataset with free-text answers based on stories, and OBQA-Additional (Mihaylov et al., 2018), a multiple-choice dataset in STEM with added factual context. CoQA contains 7,200 training and 500 validation samples (used as test data) across five domains. OBQA has 4,957 training and 500 test samples.

**Models and Setup.** We use Llama2-7B-hf (Touvron et al., 2023), Mistral-7B (Jiang et al., 2023), and Phi-2 (Javaheripi et al., 2023). As with RS-NN, any LLM can be converted into a random-set LLM (RS-LLM) by redefining its output layer to produce sets of tokens. We extract K = 8,000 focal sets via budgeting, yielding final output sizes of 40K for Llama2/Mistral and 59.2K for Phi-2. For RS-Llama2, we set $\alpha = \beta = 10^{-2}$.

**Training** uses Huggingface's trl framework (Havrilla et al., 2023), 4-bit quantization, and rank-64 LoRA adapters (Yu et al., 2023) across all layers, on A100 80GB GPUs for 5 epochs with batch size 8. Models are trained via supervised fine-tuning using the template in Fig. 9.3, where instructions (blue) and questions (black) are provided, and the model predicts the answer (green). At inference, answers are generated greedily.

[FIGURE: Figure 9.3: Training examples from CoQA and OBQA datasets. The text in black highlights the actual question, while the blue text represents prompt instructions. The model is trained to predict the text in green.]

Text in figure: two example prompt templates side by side. CoQA: "### Story: The Vatican Apostolic Library (), more commonly called the Vatican Library or simply the Vat, is the library of the Holy See, located in Vatican City. Formally (.....) though some are very significant." / "Answer the following question based on the above story." / "When was the Vat formally opened?" / "### Answer: It was formally established in 1475" (answer highlighted). OBQA: "Fact: the sun is the source of energy for physical cycles on Earth" / "Answer the following question based on the above fact by selecting the correct option." / "The sun is responsible for A) puppies learning new tricks B) children growing up and getting old C) flowers wilting in a vase D) plants sprouting, blooming and wilting" / "### Answer: D" (answer highlighted).

<!-- page: 136 -->

#### 9.2.2 Performance

Tab. 9.1 shows that RS-LLMs consistently outperform standard LLMs in both cosine similarity (CoQA) and accuracy (OBQA), despite identical training conditions. This supports the expressiveness of set-valued outputs.

Table 9.1: Performance of Standard LLMs and RS-LLMs on CoQA and OBQA datasets. For CoQA, cosine similarity is reported while accuracy is reported for OBQA.

| Model | Metric | CoQA | OBQA |
|---|---|---|---|
| Llama2 | Cosine Similarity | 0.69 | - |
| Llama2 | Accuracy | - | 83.20 |
| RS-Llama2 | Cosine Similarity | 0.71 | - |
| RS-Llama2 | Accuracy | - | 89.60 |
| Mistral | Cosine Similarity | 0.67 | - |
| Mistral | Accuracy | - | 91.60 |
| RS-Mistral | Cosine Similarity | 0.72 | - |
| RS-Mistral | Accuracy | - | 93.00 |
| Phi2 | Cosine Similarity | 0.72 | - |
| Phi2 | Accuracy | - | 87.60 |
| RS-Phi2 | Cosine Similarity | 0.73 | - |
| RS-Phi2 | Accuracy | - | 91.80 |

#### 9.2.3 Uncertainty Estimation

Fig. 9.4 analyzes uncertainty behavior. In CoQA, there is no obvious trend between the pignistic entropy and cosine similarity of RS-Llama2 (Fig. 9.4(b)), standard Llama2 (Fig. 9.4(a)). On OBQA, entropy distributions for correct/incorrect predictions overlap in both models (Figs.9.4(d), 9.4(e)), limiting their usefulness. More promisingly, credal width correlates negatively with correctness (Fig. 9.4(c)) and shows some separability across correctness in OBQA (Fig. 9.4(f)).

#### 9.2.4 Hallucination Evaluation

To test hallucination, we feed the models misleading contexts: for CoQA, the question is swapped with another; for OBQA, answer choices are randomized. Tab. 9.2 reports uncertainty metrics under correct and incorrect contexts. Both models show increased uncertainty when context is wrong. RS-Llama2, in particular, separates the two better via credal width, reflecting second-level uncertainty modeling.

Table 9.2: Uncertainty evaluation of Standard Llama2 and RS-Llama2 on correct and incorrect context.

| Model | Metric | Correct Context CoQA (↓) | Correct Context OBQA (↓) | Incorrect Context CoQA (↑) | Incorrect Context OBQA (↑) |
|---|---|---|---|---|---|
| Llama2 | Entropy | 0.39 ± 0.45 | 0.75 ± 0.59 | 0.90 ± 0.80 | 1.10 ± 0.93 |
| RS-Llama2 | Credal Width | 0.13 ± 0.13 | 0.00 ± 0.04 | 0.28 ± 0.21 | 0.02 ± 0.08 |

<!-- page: 137 -->

[FIGURE: Figure 9.4: Behavior of uncertainty measures of Llama2 and RS-Llama2 with respect to the correctness and closeness to the groundtruth on CoQA and OBQA datasets.]

Text in figure: two rows of three scatter/histogram plots, grouped under "Standard LLama2" (left two columns of the top row: (a), (d)) and "Random-set LLama2" (remaining panels: (b), (c), (e), (f)). (a) "Entropy (Standard LLama2: CoQA)" vs. "Cosine Similarity" scatter, y-axis 0.0–1.0. (b) "Pignistic Entropy (Random-set LLama2: CoQA)" vs. "Cosine Similarity" scatter. (c) "Credal Width (Random-set LLama2: CoQA)" vs. "Cosine Similarity" scatter, x-axis 0.0–0.8. (d) "Entropies for Standard LLama2: OBQA" histogram, y-axis "Frequency" 0.0–1.0, legend "Incorrectly Predicted"/"Correctly Predicted". (e) "Pignistic Entropies for Random-set LLama2: OBQA" histogram, same legend. (f) "Credal Width for Random-set LLama2: OBQA" histogram, y-axis "Frequency" 0–80, same legend.

#### 9.2.5 Budgeting Analysis

We analyze the budgeted focal sets obtained using Llama2-7b-hf (token size: 32,000) with K = 8000 sampled focal sets from $2^{32000}$. The sets display semantic closeness, e.g., '[cattle, sheep]', '[shame, pity]', '[quiet, calm, quietly]', '[maintain, retain, maintained, retained]', and '[delight, pleasure, pleased, proud, pride]'.

To evaluate this, we compute centroid distance (mean Euclidean distance from the cluster center) using sentence-transformer encodings (Reimers and Gurevych, 2019). Fig. 9.5(a) shows that the mode of the distance distribution is near zero, indicating strong semantic coherence. Fig. 9.5(b) shows focal set sizes, where 2, 3, and 4 are most frequent (counts: 2142, 1940, and 1562, respectively). The largest set (size 162) consists of punctuation/symbols.

#### 9.2.6 Ablation Studies

**Hyperparameters α and β.** The regularization terms $M_s$ and $M_r$ promote valid belief functions by enforcing mass normalization and non-negativity. However, excessive weighting may reduce predictive accuracy, similar to KL divergence in VAEs.

Tab. 9.3 shows cosine similarities for different α = β values. Both 0.01 and 0.0001 yield best performance; we use 0.01 to better enforce validity.

<!-- page: 138 -->

[FIGURE: Figure 9.5: (a) Centroid distance distribution. (b) Focal set size distribution. Sets with size > 30 excluded for visualization.]

Text in figure: two histograms. (a) "Centroid Distance" (x-axis 0.0–0.8) vs. "Count" (y-axis 0–2000), a bimodal-looking distribution with a large spike near 0. (b) "Focal set size" (x-axis 0–25) vs. "Count" (y-axis 0–2000), a right-skewed distribution peaking at small set sizes.

Table 9.3: Cosine similarity across α = β values.

| α = β | 0.1 | 0.01 | 0.001 | 0.0001 |
|---|---|---|---|---|
| Cosine Similarity | 0.66 | 0.71 | 0.69 | 0.71 |

**Focal Set Budget Size.** We ablate budget size K on CoQA (Tab. 9.4). A small K behaves like classical LLMs; a large K adds complexity. The best results occur at K = 8000. The "Combined" set is the union of all budgets.

Table 9.4: Cosine similarity across budget sizes on CoQA.

| Budget Size | 2000 | 4000 | 8000 | 16000 | Combined (56538) |
|---|---|---|---|---|---|
| Cosine Similarity | 0.67 | 0.68 | 0.71 | 0.66 | 0.69 |

### 9.3 Discussion and Implications

Overall, these results substantiate the RS-NN approach's applicability and effectiveness within large language models, demonstrating that it can successfully incorporate belief function theory to enhance uncertainty quantification and semantic representation. By efficiently budgeting focal sets, the RS-NN framework manages combinatorial complexity inherent in modeling mass functions over large token vocabularies, enabling interpretable and meaningful groupings of semantically related tokens. This balance between computational tractability and expressive power validates the RS-NN paradigm as a promising direction for neural architectures that require nuanced uncertainty modeling.

Moreover, the empirical improvements observed in downstream tasks such as question answering and summarization highlight the practical benefits of integrating RS-NN principles into state-of-the-art language models. *These encouraging outcomes lay a robust foundation for further research focused on optimizing budget allocation strategies, refining focal set construction algorithms, and

<!-- page: 139 -->

exploring alternative representations of belief functions within neural networks. The integration of RS-NN with neural language models opens avenues for developing more reliable, transparent, and uncertainty-aware AI systems, thereby advancing both theoretical understanding and practical capabilities in natural language processing.*

<!-- page: 140 -->

# 10 Application to Autonomous Racing

In this chapter, the effectiveness of Random-Set Neural Networks (RS-NN) (Chapter 5) on real-world **weather and cone classification** datasets is demonstrated. RS-NN and Bayesian models are evaluated in terms of *accuracy*, *domain adaptation*, and *uncertainty estimation*. This application requires no changes to the original RS-NN model, unlike RS-LLMs where the budgeting approach needed to be adapted to the token space.

Accurate weather classification is essential for autonomous vehicles (AVs) to handle environmental uncertainty and ensure safe operation under diverse conditions. Weather affects sensor reliability and perception accuracy, leading to increased uncertainty in object detection, scene understanding, and decision-making—key challenges for AVs, especially in edge cases. By explicitly recognizing weather conditions, AV systems can adapt their perception and planning algorithms to mitigate risks posed by adverse scenarios such as rain, fog, or low visibility. This adaptation supports epistemic AI frameworks by quantifying uncertainty related to environmental variability, enabling better generalization to previously unseen conditions. Ultimately, integrating weather classification enhances the robustness and reliability of autonomous driving systems, reducing safety-critical failures and facilitating broader deployment in real-world, dynamic environments.

### 10.1 Experimental Setup For Weather/cone Classification

The experiments evaluated the performance of three models: the proposed Random-Set Neural Network (RS-NN) (Chapter 5), a baseline standard CNN, and a Bayesian neural network (LB-BNN) (Hobbhahn et al., 2022) on three datasets related to autonomous vehicle (AV) perception under different weather conditions:

- **ROAD-WAYMO (R-WAYMO)** (Khan et al., 2024): A large, diverse **weather** dataset combining ROAD (complex road activity detection) (Singh et al., 2022) and Waymo Open (Sun et al., 2020) datasets. It contains diverse perception data from diverse geographies and conditions across the U.S. (such as San Francisco, Mountain View, Los Angeles, Detroit, Seattle, and Phoenix).
- **Oxford Brookes Racing-Autonomous (OBR-A)**: A smaller dataset collected from AV test tracks lined with cones, similar to Formula Student Competition settings, under various weather conditions including exclusive classes like Droplet and Night.
- **Cone-centric (CONE)**: A dataset centered on classifying **cones** by their different colors, designed to test perception models in recognizing cone color variations under various conditions.

<!-- page: 141 -->

Fig. 10.1 presents a comprehensive summary of the various datasets employed for weather classification tasks, highlighting their origins, class distributions, and the respective sample counts allocated for training and evaluation.

| Datasets | CONE-CENTRIC | OBR-A | ROAD-WAYMO |
|---|---|---|---|
| Source | Oxford Brookes Racing - Autonomous (OBR-A) | Oxford Brookes Racing - Autonomous (OBR-A) | ROAD (complex road activity detection) and Waymo Open |
| Number of classes | 3 | 5 | 6 |
| Classes | Blue, Orange, Yellow | Sunny, Rain, Cloud, Droplet, Night | Clear, Cloud, Overcast, Partial, Rain, Sunny |
| Training data (20% val) | 1059 | 3468 | 158,081 |
| Test data | 455 | 868 | 39,987 |

[FIGURE: Figure 10.1: Overview of datasets used for weather classification, including source, number of classes, class labels, and dataset sizes for training and testing.]

Text in figure (data samples with true labels):
- CONE-CENTRIC: Label: 0 Class: blue; Label: 0 Class: yellow; Label: 0 Class: blue; Label: 0 Class: blue
- OBR-A: Label: 0 Sunny; Label: 1 Rain; Label: 2 Cloud; Label: 3 Droplet; Label: 4 Night
- ROAD-WAYMO: Label: 0 Sunny; Label: 1 Rain; Label: 2 Cloud; Label: 3 Overcast; Label: 4 Partial; Label: 5 Clear

### 10.2 Cone Classification

Tab. 10.1 shows predictions for two representative samples from the Cone-centric dataset. For the first sample (top half of the table), the predicted belief and mass functions assign nearly all the probability mass to the class *blue*, with negligible mass on other classes. This is reflected in the pignistic probability distribution, where *blue* has a probability of 1.0, and the entropy is effectively zero (1.52 × 10⁻¹⁸), indicating an almost deterministic prediction with very high confidence. This corresponds to a sample that is clearly recognizable and easy to classify for the model. In contrast, the second sample (bottom half of the table) presents a more *uncertain prediction scenario*. The mass function spreads over multiple subsets, and the pignistic probabilities are more balanced among *yellow* (0.506) and *blue* (0.391). The entropy rises to 1.3658, reflecting this uncertainty and the ambiguity in the model's belief.

Table 10.1: The predicted belief, mass values, pignistic probabilities, and entropy for two cone-centric dataset predictions.

| Sample | Belief Set | Belief Value | Mass Set | Mass Value | Pignistic Class | Pignistic Probability | Entropy |
|---|---|---|---|---|---|---|---|
| 1 | {'blue', 'orange', 'yellow'} | 1.0 | {'blue'} | 1.0 | blue | 1.0 | 1.5213470e-18 |
| 1 | {'blue', 'yellow'} | 1.0 | {'orange', 'yellow'} | 5.1360e-20 | yellow | 3.15747602e-20 | |
| 1 | {'blue', 'orange'} | 1.0 | {'yellow'} | 0.0 | orange | 2.56716262e-20 | |
| 1 | {'blue'} | 1.0 | | | | | |
| 1 | {'orange', 'yellow'} | 5.7255e-20 | | | | | |
| 2 | {'blue', 'orange', 'yellow'} | 0.999995 | {'yellow'} | 0.653616 | yellow | 0.5058069229 | 1.3657757043 |
| 2 | {'blue', 'yellow'} | 0.999994 | {'blue'} | 0.477563 | blue | 0.3906998634 | |
| 2 | {'orange', 'yellow'} | 0.903126 | {'blue', 'orange'} | 0.371394 | orange | 0.1034862920 | |
| 2 | {'blue', 'orange'} | 0.84896 | {'orange', 'yellow'} | 0.249502 | | | |
| 2 | {'yellow'} | 0.6536186 | {'orange'} | 4.9795e-06 | | | |

<!-- page: 142 -->

Tab. 10.2 presents the performance of RS-NN, CNN, and LB-BNN across three datasets: ROAD, OBR-A, and CONE. It includes classification accuracy, predictive entropy, and confidence metrics, specifically for incorrect (ICC) and correct classifications (CC). RS-NN demonstrates superior performance across all datasets, achieving the highest accuracy (*e.g.*, 99.78% on CONE) and the most favorable uncertainty metrics, with low ICC and high CC values. CNN also shows competitive CC scores (*e.g.*, 0.977 on ROAD), but suffers from higher ICC, indicating overconfidence in incorrect predictions. LB-BNN, despite being a Bayesian model, underperforms in both accuracy and calibration, with generally higher entropy and ICC values.

The CONE dataset is relatively small in size and is included primarily to evaluate how each model performs under limited-data conditions. It serves as a stress test for generalization when training data is scarce. While RS-NN, CNN, and LB-BNN all achieve high accuracy on CONE, RS-NN maintains better uncertainty calibration, highlighting its robustness even in low-data regimes. More results on larger datasets lie in the following chapter, which presents a comprehensive evaluation on the more challenging and diverse task of weather classification.

### 10.3 Weather Classification

The R-WAYMO dataset, adapted from the original WAYMO data for weather classification, serves as a challenging benchmark for evaluating models under diverse environmental conditions. Among the evaluated models in Tab. 10.2, RS-NN stands out for delivering both high classification performance and well-calibrated uncertainty estimates. It consistently shows lower uncertainty in its incorrect predictions and maintains high confidence when predictions are correct. In contrast, LB-BNN and CNN show either less accurate performance or poorer uncertainty calibration, particularly struggling with overconfident errors. Overall, RS-NN demonstrates a strong balance between accuracy and reliability, making it especially suited for complex, real-world scenarios like R-WAYMO.

Similarly, on the OBR-A dataset, RS-NN again outperforms its counterparts, offering more accurate classifications while also producing lower predictive entropy and more balanced confidence scores. While LB-BNN and CNN follow closely in accuracy, they show less consistent uncertainty behavior, particularly CNN, which tends to be overconfident even when incorrect.

Table 10.2: Performance of RS-NN, CNN, and LB-BNN on R-WAYMO, OBR-A, and CONE datasets. We report classification accuracy, predictive entropy, and confidence estimates for both incorrect classifications (ICC ↓) and correct classifications (CC ↑).

| Model | Dataset | Accuracy (%)(↑) | Entropy | Confidence (ICC(↓) / CC(↑)) |
|---|---|---|---|---|
| RS-NN | CONE | 99.78 | 0.019 ± 0.207 | 0.589 ± 0.026 / 0.922 ± 0.037 |
| RS-NN | R-WAYMO | 76.27 | 0.160 ± 0.685 | 0.554 ± 0.187 / 0.966 ± 0.103 |
| RS-NN | OBR-A | 96.42 | 0.030 ± 0.287 | 0.692 ± 0.230 / 0.990 ± 0.042 |
| LB-BNN | CONE | 98.73 | 0.562 ± 0.371 | 0.787 ± 0.160 / 0.838 ± 0.156 |
| LB-BNN | R-WAYMO | 70.85 | 0.183 ± 0.366 | 0.644 ± 0.364 / 0.846 ± 0.732 |
| LB-BNN | OBR-A | 88.82 | 0.495 ± 0.053 | 0.730 ± 0.466 / 0.954 ± 0.544 |
| CNN | CONE | 96.92 | 0.282 ± 0.361 | 0.717 ± 0.171 / 0.958 ± 0.088 |
| CNN | R-WAYMO | 71.54 | 0.285 ± 0.315 | 0.888 ± 0.152 / 0.977 ± 0.078 |
| CNN | OBR-A | 83.41 | 0.210 ± 0.241 | 0.841 ± 0.164 / 0.964 ± 0.089 |

<!-- page: 143 -->

#### 10.3.1 Domain Adaptation Setting

Both R-WAYMO and OBR-A (weather classification) datasets are collected by the respective AVs and share common weather classes— *Sunny*, *Rainy*, *Cloudy*—while the OBR-A dataset includes exclusive classes like *Droplet* and *Night*, and R-Waymo includes *Overcast*, *Clear*, and *Partial* as exclusive classes, as shown in Fig. 10.2.

The models were trained on the smaller OBR-A dataset (3,468 images) and tested on the much larger, more diverse R-Waymo dataset (39,987 images). The goal is to evaluate each model's performance in two key areas: (a) *accuracy* in predicting weather conditions when faced with similar but previously unseen data from a different domain or environment (same class, different domain), and (b) the ability to estimate *uncertainty* when encountering entirely new conditions that the model has not been trained on (different class, different domain). RS-NN significantly outperformed both the standard CNN and the Bayesian model in both:

- **Test Accuracy:** On the shared classes in the R-Waymo test set (approximately 30,087 images), RS-NN achieved a test accuracy of 75.51%, significantly outperforming the CNN (63.78%) and the Bayesian model (61.83%). This demonstrates that RS-NN, despite being trained on a smaller dataset, is more effective at generalizing to new data, leveraging the additional information captured through random sets.
- **Uncertainty Estimation:** As shown in Fig. 10.2, the entropy distribution of RS-NN model is wider and higher for *shared classes* like Sunny, Rainy, and Cloudy, compared to the Bayesian model. This improved performance suggests that RS-NN may have better uncertainty estimation. Furthermore, for *exclusive* R-Waymo classes that the model has never seen before, RS-NN's uncertainty of the predictions remains high, while the Bayesian model (LB-BNN) exhibits predominantly lower uncertainty, with most of its entropy values clustered around zero.

[FIGURE: Figure 10.2: Experimental setup for domain adaptation: RS-NN and LB-BNN trained on OBR-A dataset are tested on R-Waymo. Comparison of entropy distributions (uncertainty estimates) for shared classes of both the datasets, and on the exclusive classes of the test dataset (R-Waymo) is shown.]

Text in figure:
Autonomous Vehicles (AVs) → Training dataset: Oxford Brookes Autonomous (OBR-A) [images: Label: 0 Sunny; Label: 1 Rain; Label: 2 Cloud; Label: 3 Droplet; Label: 4 Night] → Shared classes 'Sunny', 'Rain', 'Cloud' → density plot "Entropy for shared classes: OBR-A/R-Waymo ['Sunny', 'Rain', 'Cloud']" with curves for RS-NN: OBR-A/R-Waymo and LB-BNN: OBR-A/R-Waymo (axes: Density vs entropy value).
Autonomous Vehicles (AVs) → Test dataset: ROAD-Waymo (R-Waymo) [images: Label: 0 Sunny; Label: 1 Rain; Label: 2 Cloud; Label: 3 Overcast; Label: 4 Partial; Label: 5 Clear] → Exclusive classes(R-Waymo) 'Overcast', 'Clear', 'Partial' (Classes the model has not "seen") → density plot "Entropy for exclusive classes: R-Waymo ['Overcast', 'Clear', 'Partial']" with curves for RS-NN: OBR-A/R-Waymo and LB-BNN: OBR-A/R-Waymo (axes: Density vs entropy value).

Tab. 10.3 reports classification accuracy and entropy for domain adaptation tasks across OBR-A and R-WAYMO. RS-NN shows the best generalization in both directions, while CNN and

<!-- page: 144 -->

LB-BNN struggle, especially when adapting to unseen domains. Entropy values reflect RS-NN's stronger calibration under distribution shifts.

Table 10.3: Performance of RS-NN, CNN, and LB-BNN on domain adaptation tasks across OBR-A and ROAD datasets. Only classification accuracy and entropy are reported, as confidence metrics are not directly applicable in cross-domain settings.

| Model | Datasets | Accuracy(%)(↑) | Entropy(↑) |
|---|---|---|---|
| RS-NN | OBR-A/R-WAYMO | 75.51 | 0.659 ± 0.885 |
| RS-NN | R-WAYMO/OBR-A | 78.47 | 1.163 ± 0.359 |
| LB-BNN | OBR-A/R-WAYMO | 61.83 | 0.443 ± 0.464 |
| LB-BNN | R-WAYMO/OBR-A | 28.57 | 0.287 ± 0.414 |
| CNN | OBR-A/R-WAYMO | 63.78 | 0.370 ± 0.295 |
| CNN | R-WAYMO/OBR-A | 38.09 | 0.498 ± 0.381 |

### 10.4 Discussion

The results presented in this chapter highlight the practical strengths of Random-Set Neural Networks (RS-NNs) in real-world AV perception tasks, particularly under uncertainty and domain shift. Across cone and weather classification datasets, RS-NN consistently outperforms both standard CNNs and Bayesian neural networks (LB-BNN) in terms of accuracy, uncertainty calibration, and domain generalization. These findings validate the core hypothesis of this work: RS-NNs provide a robust and uncertainty-aware framework that improves predictive reliability in safety-critical environments like autonomous driving.

<!-- page: 145 -->

# 11 Conclusions

### 11.1 Thesis Summary

This thesis provides concrete contributions that directly address each of the research questions outlined in Sec. 1.2. In doing so, it lays foundational groundwork for the emerging field of **Epistemic AI**, where the principled modeling of ignorance is a central priority.

*To answer how epistemic uncertainty can be modeled effectively and robustly*, at the core of this thesis is the development of **Random-Set Neural Networks (RS-NNs)** (Chapter 5), designed to address critical challenges in epistemic uncertainty modeling. RS-NNs model uncertainty over sets of outcomes, effectively capturing both partial knowledge and ambiguity. They demonstrate robustness against previously unseen and adversarial inputs by producing higher entropy and wider credal sets in regions of uncertainty. This capability results in improved out-of-distribution (OoD) detection (Sec. 5.3.3) and enhanced classification performance under adversarial perturbations (Sec. 5.3.8) across multiple benchmarks, including ImageNet. *Credal set models*, which predict probability intervals to represent uncertainty through sets of plausible distributions, are briefly outlined and compared to other approaches in Sec. 11.2.

*To fairly and rigorously compare epistemic uncertainty predictions from fundamentally different output structures*, ranging from scalar probabilities to belief functions, this thesis introduces a **unified evaluation framework** (Chapter 8). The framework standardizes diverse uncertainty outputs by transforming them into credal sets and applies principled metrics such as KL divergence and non-specificity within the geometry of the probability simplex. This enables comprehensive, task-relevant evaluation across Bayesian, ensemble, evidential, credal set and random-set models without declaring a universally superior approach, but instead identifying the best fit based on the precision and imprecision needs of each application.

*To answer how to address computational challenges in random-set uncertainty modeling for scalability*, the thesis tackles the combinatorial complexity by proposing a *budgeting* (Sec. 5.2.2) technique that efficiently selects informative focal sets, reducing combinatorial complexity and making RS-NNs scalable to large datasets and architectures. Building on these advances, the framework is extended to **Random-Set Large Language Models (RS-LLMs)** (Chapter 9), which improve token-level uncertainty quantification and downstream performance in natural language processing tasks such as question answering. Additionally, the applicability of RS-NNs is demonstrated in **autonomous racing** (Chapter 10) environments, further validating the robustness and scalability of the approach in real-world dynamic domains.

The following are the key findings of this work:

<!-- page: 146 -->

- RS-NNs attained **state-of-the-art accuracy** across benchmarks, outperforming Bayesian and ensemble baselines by up to 4% on CIFAR-10 and surpassing competitors by as much as 7% on the challenging, large-scale ImageNet dataset.
- Extensions to **RS-LLMs** improved token-level prediction accuracy by up to 7% on NLP tasks such as CoQA and OBQA, while enhancing uncertainty quantification.
- RS-NNs demonstrated up to 40% better accuracy under **domain shifts in weather classification** tasks, showing especially strong robustness and generalization across diverse and ambiguous real-world radar conditions such as fog, rain, and snow. RS-NNs generalize well to unseen classes, as evidenced in R-WAYMO exclusive classes where they maintain high entropy and wide credal widths, outperforming LB-BNN.
- RS-NNs outperform competing models by achieving up to 6% higher performance on **out-of-distribution (OoD) detection**. They handle unseen samples more effectively by consistently exhibiting lower entropy for in-distribution (iD) samples and higher entropy for OoD samples, resulting in a pronounced entropy gap (*e.g.*, 0.45 on CIFAR-10 vs SVHN), surpassing DE and LB-BNN. Additionally, RS-NNs show larger credal set widths for OoD samples, reflecting stronger epistemic uncertainty (*e.g.*, iD width of 0.007 vs OoD width of 0.260 on CIFAR-10 vs SVHN).
- RS-NNs achieve up to 20% better **calibration** than Bayesian models, maintaining a low Expected Calibration Error (ECE < 0.05) even under dataset shifts. Their uncertainty is also increased by up to 15% for more challenging OoD samples.
- Under FGSM and PGD **adversarial attacks**, RS-NN maintained up to 50% higher accuracy compared to baselines, demonstrating resilience that supports the claim of reliable performance under adversarial conditions.
- Most importantly, RS-NNs demonstrated **efficient inference times** (Tab. 11.1) of approximately 1.91 ms per sample, vastly outperforming Bayesian models like FSVI (340.25 ms/sample) and ensembles such as Deep Ensembles (DE) (13,163.50 ms/sample). DE achieves a CIFAR-10 accuracy of 92.73%, RS-NNs surpass this with 93.53% accuracy (an improvement of 0.8%). However, the extremely high inference time of DEs makes them impractical for real-world applications, highlighting the scalability and deployment advantages of RS-NNs.
- Using the unified evaluation framework introduced in this thesis, which balances distance-based accuracy and imprecision via a trade-off parameter, RS-NNs are consistently selected as the best-performing model at the trade-off value of 1. This indicates that when equal weight is given to accuracy and imprecision, RS-NNs provide the most favorable balance. However, RS-NN shows poorer performance at lower trade-off values. Additionally, the interpretation of the metric is based on several underlying assumptions.

### 11.2 Impact On the Epistemic AI Paradigm

This section highlights the overall impact of the models introduced in this thesis within the Epistemic AI framework. This thesis presents three models developed under the Epistemic AI paradigm using second-order uncertainty measures: RS-NN (Chapter 5), the primary contribution, and two collaborative works: CreINN (Sec. 6.1) (Wang et al., 2024c) and CreDE (Sec. 6.2)

<!-- page: 147 -->

(Wang et al., 2024b). These models demonstrated superior performance over leading competitor approaches, including Bayesian models such as LB-BNN (Hobbhahn et al., 2022) and FSVI (Rudner et al., 2022), and Ensemble-based models like Deep Ensembles (DE) (Lakshminarayanan et al., 2017) and Epistemic Neural Networks (ENN) (Osband et al., 2024). These models were used as baselines in the experimental evaluations in Chapters 5 and 8. Evaluated on large-scale benchmarks such as ImageNet, the proposed Epistemic AI models achieved notable improvements in accuracy, robustness, uncertainty quantification, and out-of-distribution (OoD) detection, enhancing the ability to recognize unfamiliar or anomalous inputs.

As shown in Fig. 11.1(a), the Epistemic AI models (depicted as circles) cluster in the top-right region on CIFAR-10, indicating consistently strong OoD detection performance, attributed to their capacity to explicitly preserve and express ignorance. In contrast, competitor models (squares) exhibit lower and more variable performance, underscoring the theoretical advantage of second-order uncertainty under distribution shift. Furthermore, Fig. 11.1(b) illustrates that Epistemic AI models strike a superior balance between accuracy and calibration, dominating the top-left region of the plot with both high predictive accuracy and low Expected Calibration Error (ECE).

[FIGURE: Figure 11.1: Comparison of Epistemic AI models (circles) and competitor models (squares) on CIFAR-10. (a) OoD detection performance (AUROC vs. AUPRC). Epistemic AI models cluster in the top-right (high separability) while competitor methods show a much greater spread (lower performance). (b) Predictive performance (Accuracy vs. ECE). Epistemic AI models cluster in the top-left (high accuracy, low calibration error) while competitor methods show poorer trade-offs (weaker calibration).]

Text in figure:
Panel (a) "OoD Detection Performance: AUROC vs AUPRC" — y-axis: AUPRC (↑), gridlines 80.0, 82.5, 85.0, 87.5, 90.0, 92.5, 95.0, 97.5; x-axis: AUROC (↑), gridlines 80.0, 82.5, 85.0, 87.5, 90.0, 92.5, 95.0, 97.5. Legend: "Model Type" — Epistemic AI (circle marker), Competitor (square marker). Labeled points, ordered from top-right toward bottom-left: Epistemic (RS-NN); Epistemic (CreINN); Epistemic (CreDE) [two points plotted]; Ensemble (DE); Traditional (CNN); Ensemble (ENN); Bayesian (LB-BNN); Bayesian (FSVI).
Panel (b) "Predictive Performance: Accuracy vs ECE" — y-axis: Accuracy (%) (↑), gridlines 80, 82, 84, 86, 88, 90, 92, 94; x-axis: ECE (↓), gridlines 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07. Legend: "Model Type" — Epistemic AI (circle marker), Competitor (square marker). Labeled points, ordered from top-left toward bottom-right: Epistemic (CreDE); Epistemic (RS-NN); Ensemble (DE); Traditional (CNN); Ensemble (ENN); Epistemic (CreINN); Bayesian (LB-BNN); Bayesian (FSVI).

Table 11.1: Training (in minutes; per 100 epochs) and inference time (in milliseconds; per sample) comparison of uncertainty estimation methods on the CIFAR-10 dataset.

| Model | Training Time (100 epochs) (min) | Inference Time (ms/sample) |
|---|---|---|
| Traditional | 85.33 | 1.91 ± 0.7 |
| Deterministic (DDU) (Mukhoti et al., 2023) | 243.85 | 59.35 ± 0.40 |
| Bayesian (LB-BNN) (Hobbhahn et al., 2022) | 107.90 | 7.11 ± 0.89 |
| Bayesian (FSVI) (Rudner et al., 2022) | 1518.35 | 340.25 ± 0.76 |
| Ensemble (DE) (Lakshminarayanan et al., 2017) | 426.66 | 13163.50 ± 3.37 |
| Ensemble (ENN) (Osband et al., 2024) | 712.30 | 3.10 ± 0.03 |
| Evidential (EDL) (Sensoy et al., 2018) | 188.57 | 6.12 ± 0.01 |
| Evidential (Hyper-Opinion EDL) (Qu et al., 2024) | 186.56 | 23.01 ± 0.15 |
| Epistemic AI (CreDE) (Wang et al., 2024b) | 122.95 | 63.0 ± 1.1 |
| Epistemic AI (RS-NN) | 113.23 | 1.91 ± 0.02 |

<!-- page: 148 -->

In Tab. 11.1, we present the training and inference times (computational costs) for the uncertainty methods discussed in Sec. 3 and Fig. 3.1. Two examples of each model type are shown, all trained on the ResNet50 backbone. More training details are given below. These models differ not only in their uncertainty modeling principles but also in computational costs (see Tab. 11.1), reflecting a spectrum of trade-offs between performance and efficiency. For instance, function-space Bayesian methods provide uncertainty but at a high computational cost (Rudner et al., 2022), while RS-NN offer competitive accuracy with efficient inference.

### 11.3 Limitations

While the application of second-order uncertainty measures, such as those based on sets of distributions including credal and random-set models, offers powerful means to represent epistemic uncertainty, it also introduces notable challenges. These methods often require computationally intensive, especially during decision-making processes (Augustin et al., 2014; Augustin, 2022). In this thesis, we use budgeting techniques (Sec. 5.2.2) for RS-NN and credal set approximations for other methods. However, extending these efficient approaches to a broader class of second-order representations remains an open research direction.

Regarding Random-Set Neural Networks (RS-NNs) (Chapter 5) specifically, the budgeting step designed to reduce the combinatorial complexity of focal set selection can sometimes be time-consuming for very large datasets, although it is a one-time pre-training procedure for a given dataset. For large-scale datasets, this process can be made more tractable by applying dimensionality reduction techniques (*e.g.*, t-SNE, autoencoders (Ghasedi Dizaji et al., 2017; Guo et al., 2017b), or PCA (Abdi and Williams, 2010)) on representative samples rather than the entire dataset, significantly decreasing computational overhead. Moreover, the current method requires manual tuning of the number of focal elements (K), which could be improved by developing dynamic strategies that adapt K based on focal set overlap or other criteria. The budgeting technique itself also holds promise for extension to multi-source or streaming data settings, but these applications require further development. Alternative approaches for subset selection, such as leveraging sparse mass functions (Itkina et al., 2020; Chen et al., 2021), may provide a more principled, quantitative basis for budgeting and remain a valuable area for exploration.

**Random-Set Neural Networks (RS-NN).** Future work includes exploring alternative ways to ensure valid belief functions without relying on mass regularization such as integrating Semantic Probabilistic Layers (Ahmed et al., 2022) or applying softmax over masses (see Appendix 5.3.10.2). Additionally, extending RS-NNs to parameter-level representations and regression tasks will be pursued. The budgeting procedure can also be modified to accommodate multiple data sources or a continuous stream of data. t-SNE can be replaced by an autoencoder (this will need to be trained first) or PCA to add continual inference capabilities in the dimensionality reduction step. Similarly, Gaussian-based dynamic probabilistic clustering (GDPC) (Diaz-Rozo et al., 2018) can be used instead of GMM clustering to handle a continuous stream of data. GDPC works by first initialising a GMM and then updating its parameters as it sees new data. In alternative, (Kulis and Jordan, 2011) have proposed an interesting approach to learn a GMM from multiple sources of data by maintaining a local and a global mixture model. Both these approaches can be plugged into our budgeting framework with little modifications to add continual learning capabilities to it. The computation of cluster overlaps remains the same, so overlapping scores and the resultant focal sets will need to be updated as the clusters evolve. However, a cluster

<!-- page: 149 -->

tracking strategy (Barbara and Chen, 2001) can be employed so that the overlap assessment step is only re-done when a sufficient drift has been detected in the clusters. All the proposed changes are efficient enough to not have a significant effect on the overall time of budgeting. Random-Set Neural Networks may also support regression, *e.g.*, for object detection, by predicting Dirichlet distributions over Borel closed intervals (Strat, 1984) for bounding box coordinates. Class labels can be modeled as sets, enabling robust uncertainty in both spatial and categorical outputs.

The proposed evaluation metric (Chapter 8) is a function of various design choices: (i) the choice of mapping all predictions to credal sets using lower probabilities, (ii) the use of specific distance and non-specificity measures, and (iii) the metric being a linear combination of them. While these choices are theoretically motivated and supported by ablation studies (Secs. 8.4.5.3 and 8.4.5.4), alternative formulations and broader validation are important avenues for future work. Additionally, practical computation of this metric depends heavily on the model class and dataset; for example, training E-CNN (Tong et al., 2021) (an imprecise model) on more complex datasets like CIFAR-100 proved infeasible, highlighting ongoing computational and architectural constraints.

Overall, this thesis provides a strong contribution toward addressing core uncertainty quantification challenges, while several important avenues remain to be explored in computational efficiency, evaluation standardization, and practical scalability.

### 11.4 Broader Challenges Within Epistemic Deep Learning

Despite significant contributions presented in this thesis, several key challenges remain in advancing Epistemic AI and second-order uncertainty quantification.

**Scaling up.** Most existing evidential approaches (Sensoy et al., 2018) struggle to scale beyond medium-sized datasets due to computational and representational bottlenecks. The budgeting method proposed in this thesis addresses this by enabling the tractable use of random-set representations on large-scale datasets such as ImageNet and architectures like Vision Transformers. This opens up further directions, such as employing Dirichlet mixture models (Yin and Wang, 2014) or dynamic clustering techniques (Shafeeq and Hareesha, 2012) to support scalability and continual adaptation. However, a central question remains: *Can epistemic representations scale to foundation models and truly massive datasets?* Notably, quantum approaches offer new promise, with recent developments in belief representation (Zhou et al., 2023), combination mechanisms (Zhou et al., 2024), and their integration into quantum circuits (Wu and Xiao, 2024).

**From one-off to continual learning.** Most deep learning pipelines assume static training datasets, yet real-world systems must learn continuously from streaming data with shifting distributions. This thesis focuses primarily on static settings, but adapting Epistemic AI for continual learning presents a major open challenge. Existing continual learning work largely centers on avoiding catastrophic forgetting (Kirkpatrick et al., 2017), using priors, task-specific parameters, or replay buffers (Rolnick et al., 2019). More recent developments include domain-incremental learning (Van de Ven and Tolias, 2019), and online convex optimization techniques (Dall'Anese et al., 2020) that offer robustness via regret minimization. Although some recent methods explore this direction for uncertainty-aware models (Zheng et al., 2021; Jha et al., 2024), a unified framework that links continual learning and second-order epistemic uncertainty remains largely unexplored.

<!-- page: 150 -->

**Learning and symbolic reasoning under uncertainty.** Epistemic uncertainty can be reduced by collecting more data or incorporating prior knowledge, such as symbolic information (*e.g.*, Snorkel (Ratner et al., 2017)), but data alone does not guarantee better performance, as seen in autonomous vehicle failures. Neurosymbolic AI integrates symbolic reasoning with deep learning to regularize predictions and enable knowledge transfer across domains (d'Avila Garcez et al., 2009; Mao et al., 2019). Current NeurAI frameworks enforce symbolic constraints but struggle with assessing output frequency or scaling to large knowledge bases (Aditya et al., 2019). Approaches like DeepProbLog (Manhaeve et al., 2018) and DL2 (Fischer et al., 2019) leverage fuzzy and probabilistic semantics but lack epistemic uncertainty modeling. Potential solutions include designing epistemic semantic losses or using logical circuits like trigger graphs (Tsamoura et al., 2021) to extend DeepProbLog-style reasoning.

**Establishing statistical guarantees.** Epistemic models introduced in this thesis offer rich uncertainty representations, but like most approaches in the field, they do not yet provide frequentist statistical guarantees. However, RS-NNs can be combined with conformal prediction techniques (§B) to yield distribution-free coverage guarantees. Broader efforts to generalize conformal learning to second-order settings are ongoing. Notably, extensions of confidence intervals to belief functions, such as confidence structures (Denœux and Li, 2018), enable frequency-calibrated belief representations. Within the random-set framework, Inferential Models (IMs) provide belief functions with strong frequentist properties (Martin and Liu, 2015), while predictive belief functions (Denœux, 2006) can express epistemic uncertainty that is provably less committed than the true distribution with a specified probability. These approaches could help bridge the gap between formal guarantees and expressive uncertainty modeling.

**Adaptive budgeting.** In this thesis, we tackled scalability for medium to large datasets by introducing a budgeting mechanism (Sec. 5.2.2, Chapter 5) that constrains the number of focal sets in RS-NN, making computation feasible on datasets like ImageNet and architectures such as Vision Transformers. However, when extending these epistemic approaches to foundation models, which are vastly larger and trained on massive datasets, new challenges emerge. The number of focal sets can grow exponentially, making budgeting essential but also requiring more advanced pruning and summarization techniques to keep inference and training tractable. Computational and memory demands increase significantly, necessitating highly optimized algorithms and hardware-aware solutions. Additionally, foundation models often undergo continual learning and fine-tuning, which calls for adaptive budget management strategies to efficiently update uncertainty representations. Moreover, the complex architectures of foundation models incorporating multi-modal inputs and sophisticated attention mechanisms pose challenges for effectively representing and propagating uncertainty without excessive overhead. Thus, while budgeting has proven useful at smaller scales, scaling RSNNs to foundation models will require new methods for scalable focal set management, adaptive budgeting, and efficient uncertainty propagation to maintain epistemic expressiveness at massive scale.

<!-- page: 151 -->

# 12 Future Directions

This thesis has introduced novel approaches to epistemic deep learning, notably through Random-Set Neural Networks and a unified evaluation framework. However, much remains to be explored to make epistemic models more expressive, scalable, and impactful, particularly in high-stakes scientific and engineering domains.

**Advancing Random-Set Learning.** This thesis has unlocked the power of random-set learning across image classification, text classification, and language generation with LLMs, revealing its versatile potential. The next exciting frontier is pushing this approach into truly multimodal realms, such as image generation in diffusion models by quantizing images into discrete tokens. Although high-resolution images pose challenges, exploring this could revolutionize how uncertainty and ambiguity are modeled in complex visual data.

From a modeling standpoint, removing the need for explicit mass regularization by integrating semantic probabilistic layers (Ahmed et al., 2022) or applying a softmax over mass functions could enforce belief validity more naturally. The budgeting procedure itself can be made more dynamic and scalable by enabling continual learning: replacing t-SNE with an autoencoder or PCA for online dimensionality reduction, and adopting stream-compatible clustering methods such as Gaussian-based Dynamic Probabilistic Clustering (GDPC) (Diaz-Rozo et al., 2018) or mixture modeling across multiple sources (Kulis and Jordan, 2011). Efficient cluster tracking techniques (Barbara and Chen, 2001) can then trigger overlap recomputation only when significant drift is detected, maintaining both accuracy and efficiency. RS-NNs also present a pathway to regression tasks, such as object detection, by predicting Dirichlet distributions over Borel closed intervals (Strat, 1984), thus enabling uncertainty modeling in both class labels and spatial coordinates.

The next frontier for the random-set approach lies in extending from target-space to parameter-space representations. *How can Bayesian posteriors be translated into random-set posteriors over model weights?* An approach is to transform Bayesian posterior distributions into random-set posteriors using Shafer's mapping (Shafer, 1976), efficiently encoded via Dirichlet distributions over parameter intervals.

**Towards a More Unified Evaluation Framework.** The proposed evaluation metric opens avenues not only for benchmarking epistemic predictions but also for training models via loss-based optimization. Future work can explore its integration as a training objective, helping models internalize and optimize their uncertainty representations. Extending this framework to structured outputs and multi-label classification could broaden its utility. Future work includes applying the evaluation framework on a real-world decision-making task (as a classification problem), moving beyond synthetic benchmarks. Additionally, deeper analysis will be done to assess model performance without overly coarse aggregations.

<!-- page: 152 -->

A central question is whether a single epistemic model can generalize effectively across a wide range of tasks, or whether specific applications require fundamentally different uncertainty structures. This also raises the critical challenge of whether a principled, task-aware trade-off between models can be computed easily and meaningfully for practical deployment.

**Towards an Epistemic Generative AI.** Generative AI systems, particularly LLMs, face critical trust challenges due to hallucinations and overconfidence. Current solutions like Laplace-LORA (Yang et al., 2023), Bayesian fine-tuning (Wang et al., 2024d), and ensemble-based methods address some of these issues but remain either computationally expensive or weakly grounded in second-order uncertainty.

Epistemic AI introduces a novel lens: instead of modeling pointwise likelihoods, we can model belief over sets of possible outputs. Random-Set LLMs (RS-LLMs) predict belief functions over vocabulary tokens, enabling the model to express ambiguity and ignorance explicitly. Hierarchical token embeddings can define meaningful focal sets, while belief-based sampling processes enhance both diversity and robustness of generations. This is especially useful in polysemous or synonym-rich languages like Japanese or Arabic. A fundamental challenge remains: *How do we teach a model that the examples it sees are only samples from an incredibly rich set of possibilities?*

**Opportunities in Science and Engineering.** Epistemic AI presents a major opportunity to advance fields such as drug discovery, materials science, and astronomy. DeepMind's Alphafold (Jumper et al., 2021) transformed protein structure prediction, but models like Alphafold and those used in weather forecasting often lack uncertainty modeling, which is crucial for real-world tasks like climate change, additive manufacturing, and nuclear fusion plasma simulation. Recent developments with Alphafoldv3 and neural operator (NO) models (Magnani et al., 2022; Garg and Chakraborty, 2023; Zou et al., 2025), applied to nuclear fusion and climate prediction, demonstrate promise but require better uncertainty quantification to improve accuracy and efficiency.

Neural Operators are powerful surrogate models for solving PDE-governed problems across science and engineering. Despite advances in Bayesian methods (Magnani et al., 2022) and conformal prediction (CP) (Gray et al., 2025), NOs face challenges in uncertainty due to limited data and PDE misspecification. CP offers calibrated uncertainty but depends on costly calibration data. Since neural operators learn mappings between functions, such as boundary conditions and PDE solutions, *how can epistemic learning quantify uncertainty in these functional spaces?* This extends classical neural network uncertainty modeling. Epistemic AI will also help bridge low- and high-fidelity simulation gaps, as shown in fusion plasma edge modeling (Faza et al., 2024). Given the wide range of NO applications, from climate science to materials research, epistemic methods have significant potential impact.

Climate change is a critical example, altering global weather cycles and increasing extreme events like floods and droughts (Samaniego et al., 2018). Accurate prediction depends on correctly representing Earth system compartments, including atmosphere, ocean, and land, and their complex interactions. These compartments evolve dynamically, making reliable long-term forecasts a challenge. *How can models trained on insufficient and sparse data quantify epistemic uncertainty to avoid forecasting errors?* Beyond simple adaptation to streaming data, this uncertainty quantification is essential to improve decision-making with important societal and scientific consequences.

<!-- page: 153 -->

**Final Remarks.** Modern AI systems are growing in complexity: *larger* models, *multimodal* inputs, and feedback loops where predictions influence future data. In this evolving landscape, *epistemic uncertainty quantification (UQ) cannot remain a post hoc correction or afterthought*. Instead, it must be embedded at the architectural level, fundamentally shaping how models learn, adapt, and communicate what they know, and crucially, what they do not know, in an interpretable and actionable manner.

Uncertainty estimation in generative foundation models for natural language tasks poses distinct challenges and opportunities. LLMs sometimes demonstrate calibrated confidence scores, yet the mechanisms enabling this calibration remain incompletely understood. Furthermore, the transfer of epistemic AI capabilities to **vision-language models** (VLMs), especially those fine-tuned with instruction, remains an open question. Future work must dissect how input data properties, training dynamics, and architectural choices affect epistemic uncertainty predictions, addressing existing biases and limitations to improve model calibration, interpretability, and trustworthiness. Progress in this direction is vital for producing more reliable and **context-aware outputs from generative AI**.

Moreover, most performance measures for these models depend heavily on the **quality of the model's predictions** themselves. This dependency means that better uncertainty quantification and epistemic modeling are not only critical for trustworthy predictions but also for the meaningful assessment of model performance. Exploration is needed to develop assessment criteria that truly reflect a model's knowledge and ignorance, beyond just predictive accuracy.

Beyond technical advances, epistemic UQ must engage with **human trust and decision-making** processes. Uncertainty is not only a mathematical construct but a critical communication tool. How uncertainty is presented, calibrated, and interpreted deeply influences its practical value. This necessitates integrating epistemic AI research with human-computer interaction, interpretability, and ethical considerations. Building trustworthy AI, especially in high-stakes domains like healthcare and public policy, depends on uncertainties that are both technically sound and socially comprehensible.

Ultimately, epistemic uncertainty quantification is not a peripheral specialty but a foundational pillar of trustworthy AI. It provides a lens for understanding model limitations, the nature of data, and the contours of knowledge itself. Expanding this perspective mathematically, methodologically, and philosophically, will empower the creation of *AI systems that are not just intelligent, but wise; systems that 'know when they do not know'*.

<!-- page: 154 -->

# Part V

# APPENDIX

<!-- page: 155 -->

<!-- page: 156 -->

# A Algorithms

This section outlines the algorithms integral to the implementation and evaluation of budgeting (§A.0.1), expected calibration error (ECE) (§A.0.2), area under the receiver operating characteristic curve (AUROC) and area under the precision-recall curve (AUPRC) (§A.0.3).

### A.0.1 Algorithm For Budgeting

For RS-NN with N classes, generating 2^N outputs is computationally infeasible due to exponential complexity. Instead, we choose K relevant subsets (A_K focal sets) from the 2^N possibilities.

To obtain these K focal subsets, we extract feature vectors from the penultimate layer of a trained standard CNN with N outputs. We then apply t-SNE for dimensionality reduction to 3 dimensions. Note that our approach is agnostic, as t-SNE could be replaced with any other dimensionality reduction technique, including autoencoders.

Next, we fit a Gaussian Mixture Model (GMM) to the reduced feature vectors of each class. Using the eigenvectors and eigenvalues of the covariance matrix \(\Sigma_c\) and the mean vector \(\mu_c\) for each class c, we define an ellipsoid covering 95% of the data. The lengths of the ellipsoid's principal axes are computed as \(length_{c,i} = 2\sqrt{7.815\lambda_i}\), where \(\lambda_i\) is the i-th eigenvalue. The scalar 7.815 corresponds to a 95% confidence interval for a chi-square distribution with 3 degrees of freedom.

The class ellipsoids are plotted in a 3D space and the overlap of each subset in the power set of N is computed. As it is computationally infeasible to compute overlap for all 2^N subsets, we start doing so from cardinality 2 and use early stopping when increasing the cardinality further does not alter the list of most-overlapping sets of classes. We choose the top-K subsets (A_K) with the highest overlapping ratio, computed as the intersection over union for each subset.

### A.0.2 Algorithm For ECE

Expected Calibration Error (ECE) is computed by comparing the average confidence and accuracy within each bin. The steps involved are as follows:

1. For each bin, calculate the absolute difference between the average confidence and the accuracy.
2. Weight each difference by the proportion of instances in that bin compared to the total number of instances.
3. Sum up these weighted differences across all bins to get the final ECE value.

The formula for ECE is given by:

$$
\text{ECE} = \sum_{i=1}^{B} |(\text{Accuracy}_i - \text{Confidence}_i)| \times \text{Weight}_i
$$

<!-- page: 157 -->

```
Algorithm 2 Budgeting Algorithm
 1: Input: D – Training data with N classes, C – The set of classes, K – Number of non-singleton
    focal sets
 2: Output: O – Set containing N + K focal sets
 3: Initialization
 4: Extract feature vectors using a trained CNN
 5: Apply t-SNE for dimensionality reduction to 3 dimensions
 6: for each class c do
 7:     Fit GMM to the reduced feature vectors for that class to obtain μc and Σc
 8:     Define an ellipsoid covering 95% data using μc and Σc
 9: end for
10: most_overlapping_sets ← Initialize an empty list for non-singleton focal sets A1, . . . , AK
11: Set current_cardinality ← 2
12: while current_cardinality ≤ N do
13:     Compute overlaps for subsets of cardinality current_cardinality
14:     overlap(A) = |∩c∈A Ac| / |∪c∈A Ac|
15:     Select top-K subsets with highest overlap
16:     Update most_overlapping_sets
17:     if no change in most_overlapping_sets then
18:         break
19:     end if
20:     current_cardinality ← current_cardinality + 1
21: end while
22: Combine selected non-singleton focal sets with N singleton sets
23: O ← C ∪ {A1, . . . , AK}
24: return O
```

where:

- Accuracy_i is the accuracy within the i-th bin.
- Confidence_i is the average confidence within the i-th bin.
- Weight_i is the proportion of instances in the i-th bin compared to the total number of instances.
- B is the total number of bins.

The final ECE value represents how much the model's estimated probabilities differ from the true (observed) probabilities. A low ECE indicates well-calibrated probabilistic predictions, demonstrating that the model's confidence scores align closely with the actual likelihood of events. RS-NN exhibits the lowest ECE as shown in Tab. 5.5.

### A.0.3 Algorithm For AUROC, AUPRC

Out-of-distribution (OoD) detection involves the identification of data points that deviate from the in-distribution (iD) data on which a model was trained. This process relies on assessing the model's uncertainty, particularly its epistemic uncertainty, which reflects the model's lack

<!-- page: 158 -->

```
Algorithm 3 Expected Calibration Error (ECE)
Require: confidences: List or array of confidence scores predicted by the model predictions:
    List or array of predicted class labels true_labels: List or array of true class labels B:
    Number of bins for binning confidence scores
Ensure: ECE: Expected Calibration Error
 1: Step 1: Normalize Confidences Normalize the confidence scores to ensure they are in
    the range [0, 1].
 2: Step 2: Binning Divide the confidence scores into num_bins bins.
 3: Step 3: Initialize Arrays Initialize arrays bin_accuracy, bin_confidence, and weights
    with zeros.
 4: Step 4: Populate Arrays
 5: for each bin do
 6:    Identify instances falling into the bin
 7:    Calculate mean accuracy and mean confidence within the bin
 8:    Update bin_accuracy, bin_confidence, and weights
 9: end for
10: Step 5: Calculate ECE Calculate the Expected Calibration Error using the populated
    arrays.
                           B
                   ECE =   Σ  |(bin_accuracyi − bin_confidencei)| × weightsi
                          i=1
```

```
Algorithm 4 Algorithm for AUROC, AUPRC
Require: uncertainty_iid: Uncertainty scores for in-distribution samples. uncertainty_ood:
    Uncertainty scores for out-of-distribution samples.
Ensure: (fpr, tpr, thresholds): ROC curve metrics.
 1: (precision, recall, prc_thresholds): Precision-Recall curve metrics.
 2: auroc: Area Under the Receiver Operating Characteristic curve.
 3: auprc: Area Under the Precision-Recall curve.
 4: Step 1: Concatenate uncertainties;
 5: uncertainties ← concatenate(uncertainty_iid, uncertainty_ood)
 6: Step 2: Create and combine labels;
 7: in_labels ← zeros(uncertainty_iid.shape[0]) ood_labels ← ones(uncertainty_ood.shape[0])
    labels ← concatenate(in_labels, ood_labels)
 8: Step 4: Calculate ROC curve;
 9: (fpr, tpr, thresholds) ← roc_curve(labels, uncertainties)
10: Step 5: Calculate AUROC;
11: auroc ← roc_auc_score(labels, uncertainties)
12: Step 6: Calculate Precision-Recall curve;
13: (precision, recall, prc_thresholds) ← precision_recall_curve(labels, uncertainties)
14: Step 7: Calculate AUPRC;
15: auprc ← average_precision_score(labels, uncertainties)
```

of knowledge or confidence in making predictions. When exposed to OoD data, which differs significantly from the training data, the model tends to exhibit higher epistemic uncertainty.

<!-- page: 159 -->

AUROC (Area Under the Receiver Operating Characteristic Curve) and AUPRC (Area Under the Precision-Recall Curve) are evaluation metrics commonly used to assess the performance of binary classification models, providing insights into their ability to distinguish between positive and negative instances. In the context of evaluating uncertainty estimation in machine learning models, these metrics quantify how well the model separates iD samples from OoD samples. AUROC is derived from the Receiver Operating Characteristic (ROC) curve, which illustrates the trade-off between True Positive Rate (TPR) and False Positive Rate (FPR) across various classification thresholds.

The AUROC value represents the area under this curve and ranges from 0 to 1, with higher values indicating better discriminative performance. AUPRC is based on the Precision-Recall curve, which plots Precision against Recall at different classification thresholds. Precision measures the accuracy of positive predictions, while Recall quantifies the ability to capture all positive instances. AUPRC calculates the area under this curve and provides a complementary perspective, particularly valuable when dealing with imbalanced datasets.

[FIGURE: Figure A.1: Receiver Operating Characteristic (ROC) and Precision-Recall Characteristic (PRC) curves for RS-NN, LB-BNN, ENN, and CNN evaluated on the SVHN and Intel Image OoD datasets for CIFAR-10.]

Text in figure:
"SVHN - ROC Curve" (y-axis: True Positive Rate (FPR); x-axis: False Positive Rate (TPR)): RS-CNN: 94.58, LB-BNN: 88.14, ENN: 92.76, CNN: 93.11.
"Intel Image - ROC Curve": RS-CNN: 97.3, LB-BNN: 82.21, ENN: 85.67, CNN: 88.02.
"SVHN - PRC Curve" (y-axis: Precision; x-axis: Recall): RS-CNN: 93.43, LB-BNN: 81.96, ENN: 89.05, CNN: 91.0.
"Intel Image - PRC Curve": RS-CNN: 90.69, LB-BNN: 55.17, ENN: 58.09, CNN: 66.62.

[FIGURE: Figure A.2: Receiver Operating Characteristic (ROC) and Precision-Recall Characteristic (PRC) curves for RS-NN, LB-BNN, ENN, and CNN evaluated on the SVHN and Intel Image OoD datasets for MNIST.]

Text in figure:
"F-MNIST - ROC Curve" (y-axis: True Positive Rate (FPR); x-axis: False Positive Rate (TPR)): RS-CNN: 93.89, LB-BNN: 89.65, ENN: 81.79, CNN: 83.77.
"K-MNIST - ROC Curve": RS-CNN: 96.75, LB-BNN: 95.61, ENN: 95.94, CNN: 94.46.
"F-MNIST - PRC Curve" (y-axis: Precision; x-axis: Recall): RS-CNN: 93.98, LB-BNN: 90.36, ENN: 82.92, CNN: 84.14.
"K-MNIST - PRC Curve": RS-CNN: 96.58, LB-BNN: 95.65, ENN: 95.45, CNN: 93.94.

Figs. A.1 and A.2 plot each model's performance, illustrating the trade-offs between True Positive Rate and False Positive Rate (ROC curve), Precision and Recall (PRC curve) for CIFAR-10 (Fig. A.1) and MNIST (Fig. A.2). The left two plots depict the AUROC curves, where the blue curve representing RS-NN outperforms others, indicating superior discrimination between true positive and false positive rates. Similarly, on the two right plots displaying Precision-Recall Curve (PRC), RS-NN exhibits the highest curve, emphasizing its precision and recall performance. These results showcase RS-NN's effectiveness in distinguishing in-distribution and out-of-distribution samples.

In real-world scenarios, encountering OoD instances is inevitable, making reliable OoD detection essential for safety-critical applications to avoid erroneous decisions on unfamiliar data. Recognising unfamiliar data signals the model about situations beyond its training, allowing it to acknowledge its own limitations and ignorance, which in turn enhances its uncertainty estimation.

<!-- page: 160 -->

# B Statistical guarantees

To complement the extensive discussion in the main paper, we provide here an in-depth discussion on how statistical guarantees can be provided in an RS-NN framework.

**Plugging RS-NN into conformal learning.** Indeed, RS-NN can be employed as the 'underlying model' in an inductive conformal learning framework[^1], which builds an empirical cumulative distribution of the 'non-conformity' scores of a set of calibration samples, and at test time outputs the set of labels whose empirical CDF is above a desired significance level \(\epsilon\) (*e.g.*, 95%).

Given a test input x and the associated predictive belief function \(\hat{Bel}(c|x)\) (the output of RS-NN), we could, for instance, set as non-conformity score

$$
s(x, c) \doteq 1 - \hat{Pl}(c|x) = \hat{Bel}(\mathcal{C} \setminus \{c\}|x) \tag{B.1}
$$

(*i.e.*, a label c is 'non-conformal' if its predicted *plausibility*, which is defined as \(Pl(A) = 1 - Bel(\Theta \setminus A)\) and has the semantic of an upper probability bound (Shafer, 1976), is low), and compute predictive regions in the usual way:

$$
\Gamma(x) = \{c \in \mathcal{C} : p^c > \epsilon\},
$$

where

$$
p^c = \frac{|(x_j, c_j) : s(x_j, c_j) > s(x, c)|}{q+1} + u \cdot \frac{|(x_j, c_j) : s(x_j, c_j) = s(x, c)|}{q+1},
$$

\((x_j, c_j)\) is the j-th calibration point, q is the number of calibration points, and \(u \sim \mathcal{U}(0,1)\) (the uniform distribution on the interval (0, 1)).

**Experiments on conformal guarantees.** Thus, we conducted experiments on CIFAR-10 dataset to provide conformal prediction guarantees with non-conformity scores as given in Eq. B.1. The goal is to assess the reliability of classification predictions by determining a threshold of non-conformity scores that covers 95% of the data.

To achieve this, non-conformity scores are obtained for all classes, and a threshold is calculated such that it contains 95% of the data. This threshold determines the coverage of the classification, which refers to the proportion of predictions that actually contain the true outcome.

This prediction threshold is determined by finding the percentile corresponding to \(1 - \alpha\), where \(\alpha\) is set to 0.05 to achieve 95% coverage. Fig. B.2 shows the non-conformity scores for all the calibration data, j = 1000 (Angelopoulos and Bates, 2021) (using the following split: 40000:10000:9000:1000 training, testing, validation and calibration data points respectively for CIFAR-10), with a cut-off threshold that ensures 95% coverage.

[^1]: https://cml.rhul.ac.uk/copa2017/presentations/CP_Tutorial_2017.pdf

<!-- page: 161 -->

The conformal prediction sets for two sample inputs are shown in Fig. B.1, along with their predicted probabilities.

[FIGURE: Figure B.1: Conformal prediction sets by RS-NN on the CIFAR-10 dataset. The predicted probabilities for each class is shown.]

Text in figure:
- Left panel: "Prediction sets: {'cat', 'horse', 'truck'}" / "[0.20296144] [0.54583361] [0.24168862]" / "True label: horse" (image of a horse)
- Right panel: "Prediction sets: {'cat', 'dog'}" / "[0.49130123] [0.41791199]" / "True label: cat" (image of a cat)

[FIGURE: Figure B.2: Conformal prediction threshold for CIFAR-10 indicating the boundary beyond which predictions are considered non-conformal.]

Text in figure: line plot; y-axis "S_i (non-conformality)" ranging 0.0 to 1.0; x-axis "Sample instance (sorted by s_i)" ranging 0 to 1000; annotation "95th percentile conformality threshold" marked by a dashed horizontal line.

[FIGURE: Figure B.3: Coverage per class of RS-NN for CIFAR-10 dataset.]

Text in figure: bar chart titled "Coverage per Class"; y-axis "Coverage" (0.0–1.0); x-axis "Class" (0–9).

[FIGURE: Figure B.4: Average size of the predictive sets generated for each class of CIFAR-10.]

Text in figure: bar chart titled "Set Size per Class"; y-axis "Set Size" (0.0–1.2); x-axis "Class" (0–9).

<!-- page: 162 -->

Figs. B.3 and B.4 show the coverage and average set size for each class on the test dataset. Coverage is the proportion of prediction sets that actually contain the true outcome, and average set size is the average number of predicted classes per instance. Higher numbers represent more overlap between the classification regions of different classes.

Summarizing the results, (1) the coverage averages across classes over the desired threshold. This indicates that the conformal prediction method is providing reliable prediction intervals that contain the true class label with the specified confidence level; (2) The spread or variability in set sizes across different samples provides insights into how well the prediction sets adapt to the difficulty of the samples. Ideally, the prediction sets should dynamically adjust based on the difficulty of each example, with larger sets for more challenging inputs and smaller sets for easier ones. Fig. B.4 shows that the average set size for classes 1, 2, 3, 4, and 6 is considerably larger than for the rest, indicating that the model found samples from these as challenging inputs.

**Alternative approaches to statistical guarantees.** In the future we plan to explore the possibility of generalising the empirical CDF at the basis of conformal learning in a belief function / random set representation, aiming to retain statistical guarantees. Given the complexity of this enterprise, we are working towards this in a separate paper.

Finally, an intriguing alternative approach (and one that is more achievable in the short term) is the study of confidence intervals in a belief functions representation, such as the one we employ in RS-NNs. In fact, recent studies have been looking at extending the notion of confidence interval (https://en.wikipedia.org/wiki/Confidence_interval) to belief functions, under the name of *confidence structures* (https://hal.science/hal-01576356v3), which generalise standard confidence distributions and generate "frequency-calibrated" belief functions.

Liu and Martin, in particular, have developed an Inferential Model (IM) approach which produces belief functions with well-defined frequentist properties (Martin and Liu, 2013; 2015). An alternative approach relies on the notion of "predictive" belief function (Denœux, 2006), which, under repeated sampling, is less committed than the true probability distribution of interest with some prescribed probability.

<!-- page: 163 -->

# Bibliography

Hervé Abdi and Lynne J Williams. Principal component analysis. Wiley interdisciplinary reviews: computational statistics, 2(4):433–459, 2010.

Taiga Abe, Estefany Kelly Buchanan, Geoff Pleiss, Richard Zemel, and John P Cunningham. Deep ensembles work, but are they necessary? Advances in Neural Information Processing Systems, 35:33646–33660, 2022.

Joaquín Abellán and Serafín Moral. A non-specificity measure for convex sets of probability distributions. International journal of uncertainty, fuzziness and knowledge-based systems, 8 (03):357–367, 2000.

Joaquín Abellán and Serafín Moral. Difference of entropies as a non-specificity function on credal sets. International journal of general systems, 34(3):201–214, 2005.

Joaquín Abellán and Manuel Gómez. Measures of divergence on credal sets. Fuzzy Sets and Systems, 157(11):1514–1531, 2006.

Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.

Marcel R Ackermann, Johannes Blömer, Daniel Kuntze, and Christian Sohler. Analysis of agglomerative clustering. Algorithmica, 69:184–215, 2014.

Somak Aditya, Yezhou Yang, and Chitta Baral. Integrating knowledge and reasoning in image understanding. arXiv preprint arXiv:1906.09954, 2019.

Charu C Aggarwal, Xiangnan Kong, Quanquan Gu, Jiawei Han, and S Yu Philip. Active learning: A survey. In Data Classification: Algorithms and Applications, pages 571–605. CRC Press, 2014.

Kareem Ahmed, Stefano Teso, Kai-Wei Chang, Guy Van den Broeck, and Antonio Vergari. Semantic probabilistic layers for neuro-symbolic learning. Advances in Neural Information Processing Systems, 35:29944–29959, 2022.

Isabela Albuquerque, João Monteiro, Mohammad Darvishi, Tiago H Falk, and Ioannis Mitliagkas. Generalizing to unseen domains via distribution matching. arXiv preprint arXiv:1911.00804, 2019.

Alexander A Alemi, Ian Fischer, and Joshua V Dillon. Uncertainty in the variational information bottleneck. arXiv preprint arXiv:1807.00906, 2018.

<!-- page: 164 -->

Shadi Alijani, Jamil Fayyad, and Homayoun Najjaran. Vision transformers in domain adaptation and domain generalization: a study of robustness. Neural Computing and Applications, 36(29): 17979–18007, 2024.

Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané. Concrete problems in ai safety. arXiv preprint arXiv:1606.06565, 2016.

Anastasios N Angelopoulos and Stephen Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv preprint arXiv:2107.07511, 2021.

Rohan Anil, Andrew M Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. Palm 2 technical report. arXiv preprint arXiv:2305.10403, 2023.

Alessandro Antonucci and Giorgio Corani. The multilabel Naive Credal Classifier. International Journal of Approximate Reasoning, 83:320–336, 2017. ISSN 0888-613X. doi: https://doi.org/10.1016/j.ijar.2016.10.006. URL https://www.sciencedirect.com/science/article/pii/S0888613X16301773.

Alessandro Antonucci and Fabio Cuzzolin. Credal sets approximation by lower probabilities: application to credal networks. In Computational Intelligence for Knowledge-Based Systems Design: 13th International Conference on Information Processing and Management of Uncertainty, IPMU 2010, Dortmund, Germany, June 28-July 2, 2010. Proceedings 13, pages 716–725. Springer, 2010.

Thomas Augustin. Statistics with imprecise probabilities—a short survey. Uncertainty in Engineering Introduction to Methods and Applications, 67, 2022.

Thomas Augustin, Frank PA Coolen, Gert De Cooman, and Matthias CM Troffaes. Introduction to imprecise probabilities, volume 591. John Wiley & Sons, 2014.

Muhammad Awais, Fengwei Zhou, Hang Xu, Lanqing Hong, Ping Luo, Sung-Ho Bae, and Zhenguo Li. Adversarial robustness for unsupervised domain adaptation. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 8568–8577, 2021.

Mohammad Gheshlaghi Azar, Ian Osband, and Rémi Munos. Minimax regret bounds for reinforcement learning. In International conference on machine learning, pages 263–272. PMLR, 2017.

Vineeth Balasubramanian, Shen-Shyang Ho, and Vladimir Vovk. Conformal prediction for reliable machine learning: theory, adaptations and applications. Newnes, 2014.

Puneet Bansal. Intel image classification. Available on https://www. kaggle. com/puneet6060/intel-image-classification, Online, 2019.

Daniel Barbara and Ping Chen. Tracking clusters in evolving data sets. In FLAIRS, pages 239–243, 2001.

Jonathan Baron. Second-order probabilities and belief functions. Theory and Decision, 23:25–36, 1987.

Stephen Bates, Emmanuel Candès, Lihua Lei, Yaniv Romano, and Matteo Sesia. Testing for outliers with conformal p-values. The Annals of Statistics, 51(1):149–178, 2023.

<!-- page: 165 -->

William H Beluch, Tim Genewein, Andreas Nürnberger, and Jan M Köhler. The power of ensembles for active learning in image classification. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 9368–9377, 2018.

Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM conference on fairness, accountability, and transparency, pages 610–623, 2021.

Viktor Bengs, Eyke Hüllermeier, and Willem Waegeman. Pitfalls of epistemic uncertainty quantification through loss minimisation. Advances in Neural Information Processing Systems, 35:29205–29216, 2022.

James O Berger. Statistical decision theory and Bayesian analysis. Springer Science & Business Media, 2013.

Jean-Marc Bernard. An introduction to the imprecise dirichlet model for multinomial data. International Journal of Approximate Reasoning, 39(2-3):123–150, 2005.

David Betancourt and Rafi L Muhanna. Interval deep learning for computational mechanics problems under input uncertainty. Probabilistic Engineering Mechanics, 70:103370, 2022.

Gilles Blanchard, Gyemin Lee, and Clayton Scott. Generalizing from several related classification tasks to a new unlabeled sample. Advances in neural information processing systems, 24, 2011.

Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, and Daan Wierstra. Weight uncertainty in neural network. In International conference on machine learning, pages 1613–1622. PMLR, 2015.

Mariusz Bojarski. End to end learning for self-driving cars. arXiv preprint arXiv:1604.07316, 2016.

Andrey Bronevich and George J Klir. Axioms for uncertainty measures on belief functions and credal sets. In NAFIPS 2008-2008 Annual Meeting of the North American Fuzzy Information Processing Society, pages 1–6. IEEE, 2008.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.

Wray L. Buntine and Andreas S. Weigend. Bayesian back-propagation. Complex Syst., 5, 1991. URL https://api.semanticscholar.org/CorpusID:14814125.

Thomas Burger, Oya Aran, and Alice Caplier. Modeling hesitation and conflict: a belief-based approach for multi-class problems. In 2006 5th International Conference on Machine Learning and Applications (ICMLA'06), pages 95–100. IEEE, 2006.

Margarida Campos, António Farinhas, Chrysoula Zerva, Mário AT Figueiredo, and André FT Martins. Conformal prediction for natural language processing: A survey. Transactions of the Association for Computational Linguistics, 12:1497–1516, 2024.

Yang Cao, Xiaojun Wang, Yi Wang, Lianming Xu, and Yifei Wang. An interval neural network method for identifying static concentrated loads in a population of structures. Aerospace, 11 (9):770, 2024.

<!-- page: 166 -->

Michele Caprio, Souradeep Dutta, Kuk Jang, Vivian Lin, Radoslav Ivanov, Oleg Sokolsky, and Insup Lee. Credal bayesian deep learning. arXiv preprint arXiv:2302.09656, 2023a.

Michele Caprio, Souradeep Dutta, Kuk Jin Jang, Vivian Lin, Radoslav Ivanov, Oleg Sokolsky, and Insup Lee. Imprecise Bayesian neural networks. arXiv preprint arXiv:2302.09656, 2023b.

Michele Caprio, Maryam Sultana, Eleni Elia, and Fabio Cuzzolin. Credal learning theory. arXiv preprint arXiv:2402.00957, 2024.

Bertrand Charpentier, Daniel Zügner, and Stephan Günnemann. Posterior network: Uncertainty estimation without ood samples via density-based pseudo-counts. Advances in neural information processing systems, 33:1356–1367, 2020.

Alain Chateauneuf and Jean-Yves Jaffray. Some characterizations of lower probabilities and other monotone capacities through the use of Möbius inversion. Mathematical Social Sciences, 17(3):263–283, 1989. ISSN 0165-4896. doi: https://doi.org/10.1016/0165-4896(89)90056-5. URL https://www.sciencedirect.com/science/article/pii/0165489689900565.

Priyanka Chaudhary, João P Leitão, Tabea Donauer, Stefano D'Aronco, Nathanaël Perraudin, Guillaume Obozinski, Fernando Perez-Cruz, Konrad Schindler, Jan Dirk Wegner, and Stefania Russo. Flood uncertainty estimation using deep ensembles. Water, 14(19):2980, 2022.

Changyou Chen, David Carlson, Zhe Gan, Chunyuan Li, and Lawrence Carin. Bridging the gap between stochastic gradient mcmc and stochastic optimization. In Artificial Intelligence and Statistics, pages 1051–1060. PMLR, 2016.

Phil Chen, Mikhal Itkina, Ransalu Senanayake, and Mykel J Kochenderfer. Evidential softmax for sparse multimodal distributions in deep Generative models. Advances in Neural Information Processing Systems, 34:11565–11576, 2021.

Kamil Ciosek, Vincent Fortuin, Ryota Tomioka, Katja Hofmann, and Richard Turner. Conservative uncertainty estimation by fitting prior networks. In International Conference on Learning Representations, 2019.

Tarin Clanuwat, Mikel Bober-Irizar, Asanobu Kitamoto, Alex Lamb, Kazuaki Yamamoto, and David Ha. Deep learning for classical Japanese literature. arXiv preprint arXiv:1812.01718, 2018.

Giorgio Corani and Marco Zaffalon. Learning reliable classifiers from small or incomplete data sets: The naive credal classifier 2. Journal of Machine Learning Research, 9(4), 2008.

Giorgio Corani, Alessandro Antonucci, and Marco Zaffalon. Bayesian networks with imprecise probabilities: Theory and application to classification. Data Mining: Foundations and Intelligent Paradigms: Volume 1: Clustering, Association and Classification, pages 49–93, 2012.

Fabio Gagliardi Cozman. Credal networks. Artificial Intelligence, 120(2):199–233, 2000.

Fabio Cuzzolin. Geometry of Upper Probabilities. In ISIPTA, pages 188–203, 2003.

Fabio Cuzzolin. Simplicial complexes of finite fuzzy sets. In Proceedings of the 10th International Conference on Information Processing and Management of Uncertainty (IPMU'04), volume 4, pages 4–9, 2004a.

<!-- page: 167 -->

Fabio Cuzzolin. Geometry of Dempster's rule of combination. IEEE Transactions on Systems, Man and Cybernetics part B, 34(2):961–977, 2004b.

Fabio Cuzzolin. Two new Bayesian approximations of belief functions based on convex geometry. IEEE Transactions on Systems, Man, and Cybernetics - Part B, 37(4):993–1008, 2007.

Fabio Cuzzolin. On the credal structure of consistent probabilities. In European Workshop on Logics in Artificial Intelligence, pages 126–139. Springer, 2008a.

Fabio Cuzzolin. A geometric approach to the theory of evidence. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 38(4):522–534, 2008b.

Fabio Cuzzolin. Complexes of outer consonant approximations. In Proceedings of the 10th European Conference on Symbolic and Quantitative Approaches to Reasoning with Uncertainty (ECSQARU'09), pages 275–286, 2009.

Fabio Cuzzolin. Three alternative combinatorial formulations of the theory of evidence. Intelligent Data Analysis, 14(4):439–464, 2010a.

Fabio Cuzzolin. Credal semantics of Bayesian transformations in terms of probability intervals. IEEE Transactions on Systems, Man, and Cybernetics, Part B: Cybernetics, 40(2):421–432, 2010b.

Fabio Cuzzolin. The geometry of consonant belief functions: simplicial complexes of necessity measures. Fuzzy Sets and Systems, 161(10):1459–1479, 2010c.

Fabio Cuzzolin. l_{p} consonant approximations of belief functions. IEEE Transactions on Fuzzy Systems, 22(2):420–436, 2013.

Fabio Cuzzolin. Generalised max entropy classifiers. In Sébastien Destercke, Thierry Denœux, Fabio Cuzzolin, and Arnaud Martin, editors, Belief Functions: Theory and Applications, pages 39–47, Cham, 2018a. Springer International Publishing.

Fabio Cuzzolin. Visions of a generalized probability theory. arXiv preprint arXiv:1810.10341, 2018b.

Fabio Cuzzolin. The Geometry of Uncertainty: The Geometry of Imprecise Probabilities. Artificial Intelligence: Foundations, Theory, and Algorithms. Springer International Publishing, 2020. ISBN 9783030631536. URL https://books.google.co.uk/books?id=jNQPEAAAQBAJ.

Fabio Cuzzolin. Uncertainty measures: A critical survey. Information Fusion, page 102609, 2024.

Fabio Cuzzolin. Lp consonant approximations of belief functions in the mass space. In Proceedings of the 7th International Symposium on Imprecise Probability: Theory and Applications (ISIPTA'11), July 2011.

Fabio Cuzzolin and Ruggero Frezza. Geometric analysis of belief space and conditional subspaces. In ISIPTA, pages 122–132, 2001.

Emiliano Dall'Anese, Andrea Simonetto, Stephen Becker, and Liam Madden. Optimization and learning with information streams: Time-varying algorithms and applications. IEEE Signal Processing Magazine, 37(3):71–83, 2020.

<!-- page: 168 -->

Erik Daxberger, Agustinus Kristiadi, Alexander Immer, Runa Eschenhagen, Matthias Bauer, and Philipp Hennig. Laplace redux-effortless Bayesian deep learning. Advances in Neural Information Processing Systems, 34:20089–20103, 2021.

Luis M. De Campos, Juan F. Huete, and Serafin Moral. Probability intervals: A tool for uncertain reasoning. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 02 (02):167–196, June 1994. ISSN 0218-4885, 1793-6411. doi: 10.1142/S0218488594000146.

Bruno de Finetti. Theory of Probability. Wiley, London, 1974.

Ivo Pascal de Jong, Andreea Ioana Sburlea, and Matias Valdenegro-Toro. How disentangled are your classification uncertainties? arXiv preprint arXiv:2408.12175, 2024.

Arthur P. Dempster. Upper and lower probability inferences based on a sample from a finite univariate population. Biometrika, 54(3-4):515–528, 1967.

Arthur P Dempster. Upper and lower probabilities induced by a multivalued mapping. In Classic works of the Dempster-Shafer theory of belief functions, pages 57–72. Springer, 2008.

Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-scale hierarchical image database. In 2009 IEEE Conference on Computer Vision and Pattern Recognition, pages 248–255. Ieee, 2009.

Dieter Denneberg and Michel Grabisch. Interaction transform of set functions over a finite set. Information Sciences, 121(1-2):149–170, 1999.

Thierry. Denoeux. A neural network classifier based on Dempster-Shafer theory. IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems and Humans, 30(2):131–150, 2000. doi: 10.1109/3468.833094.

Thierry Denœux. Constructing belief functions from sample data using multinomial confidence regions. International Journal of Approximate Reasoning, 42(3):228–252, 2006.

Thierry Denœux. A k-nearest neighbor classification rule based on Dempster–Shafer theory. In Roland R. Yager and Liping Liu, editors, Classic Works of the Dempster-Shafer Theory of Belief Functions, volume 219 of Studies in Fuzziness and Soft Computing, pages 737–760. Springer, 2008.

Thierry Denoeux. Distributed combination of belief functions. Information Fusion, 65:179–191, 2021.

Thierry Denœux. An evidential neural network model for regression based on random fuzzy numbers. In International Conference on Belief Functions, pages 57–66. Springer, 2022.

Thierry Denœux and Shoumei Li. Frequency-calibrated belief functions: review and new insights. International Journal of Approximate Reasoning, 92:232–254, 2018.

Stefan Depeweg, Jose-Miguel Hernandez-Lobato, Finale Doshi-Velez, and Steffen Udluft. Decomposition of uncertainty in bayesian deep learning for efficient and risk-sensitive learning. In International conference on machine learning, pages 1184–1193. PMLR, 2018.

Esther Derman, Daniel Mankowitz, Timothy Mann, and Shie Mannor. A bayesian approach to robust reinforcement learning. In Uncertainty in Artificial Intelligence, pages 648–658. PMLR, 2020.

<!-- page: 169 -->

Aniket Anand Deshmukh, Yunwen Lei, Srinagesh Sharma, Urun Dogan, James W Cutler, and Clayton Scott. A generalization error bound for multi-class domain generalization. arXiv preprint arXiv:1905.10392, 2019.

Javier Diaz-Rozo, Concha Bielza, and Pedro Larrañaga. Clustering of data streams with dynamic gaussian mixture models: An iot application in industrial processes. IEEE Internet of Things Journal, 5(5):3533–3547, 2018.

Enrique López Droguett and Ali Mosleh. Bayesian methodology for model uncertainty using model performance data. Risk Analysis: An International Journal, 28(5):1457–1476, 2008.

Didier Dubois and Henri Prade. Properties of measures of information in evidence and possibility theories. Fuzzy sets and systems, 24(2):161–182, 1987.

Didier Dubois and Henri Prade. Consonant approximations of belief functions. International Journal of Approximate Reasoning, 4:419–449, 1990.

Didier Dubois and Henri Prade. Possibility theory: an approach to computerized processing of uncertainty. Springer Science & Business Media, 2012.

Didier Dubois, Henri Prade, and Sandra Sandri. On possibility/probability transformations. In Fuzzy logic: State of the art, pages 103–112. Springer, 1993.

Michael Dusenberry, Ghassen Jerfel, Yeming Wen, Yian Ma, Jasper Snoek, Katherine Heller, Balaji Lakshminarayanan, and Dustin Tran. Efficient and scalable bayesian neural nets with rank-1 factors. In International conference on machine learning, pages 2782–2792. PMLR, 2020.

Artur S d'Avila Garcez, Luís C Lamb, and Dov M Gabbay. Neural-symbolic learning systems. Springer, 2009.

Zied Elouedi, Khaled Mellouli, and Philippe Smets. Decision trees using the belief function theory. In Proceedings of the Eighth International Conference on Information Processing and Management of Uncertainty in Knowledge-based Systems (IPMU 2000), volume 1, pages 141–148, Madrid, 2000.

Zied Elouedi1, Khaled Mellouli1, and Philippe Smets. Classification with belief decision trees. In International Conference on Artificial Intelligence: Methodology, Systems, and Applications, pages 80–90. Springer, 2000.

Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, and Yarin Gal. Detecting hallucinations in large language models using semantic entropy. Nature, 630(8017):625–630, 2024.

Rebecca Fay, Friedhelm Schwenker, Christian Thiel, and Günther Palm. Hierarchical neural networks utilising dempster-shafer evidence theory. In Friedhelm Schwenker and Simone Marinai, editors, Artificial Neural Networks in Pattern Recognition, pages 198–209, Berlin, Heidelberg, 2006. Springer Berlin Heidelberg. ISBN 978-3-540-37952-2.

Ghifari A Faza, Keivan Shariatmadar, Hans Hallez, and David Moens. Interval reduced order surrogate modelling framework for uncertainty quantification. In AIAA Scitech 2024 Forum, page 0387, 2024.

<!-- page: 170 -->

Marc Fischer, Mislav Balunovic, Dana Drachsler-Cohen, Timon Gehr, Ce Zhang, and Martin Vechev. Dl2: training and querying neural networks with logic. In International Conference on Machine Learning, pages 1931–1941. PMLR, 2019.

Stanislav Fort and Stanislaw Jastrzebski. Large scale structure of neural network loss landscapes. Advances in Neural Information Processing Systems, 32, 2019.

Vincent Fortuin. Priors in Bayesian Deep Learning: A Review. International Statistical Review, 90, 05 2022. doi: 10.1111/insr.12502.

David Freedman. Wald lecture: On the Bernstein-von Mises theorem with infinite-dimensional parameters. The Annals of Statistics, 27(4):1119–1141, 1999.

Zhun ga Liu, Jean Dezert, Grégoire Mercier, and Quan Pan. Belief C-means: An extension of fuzzy C-means algorithm in belief functions framework. Pattern Recognition Letters, 33(3): 291–300, 2012.

Yarin Gal and Zoubin Ghahramani. Bayesian convolutional neural networks with Bernoulli approximate variational inference. arXiv preprint arXiv:1506.02158, 2015.

Yarin Gal and Zoubin Ghahramani. Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. In International Conference on Machine Learning, pages 1050–1059. PMLR, 2016.

Yaroslav Ganin and Victor Lempitsky. Unsupervised domain adaptation by backpropagation. In International conference on machine learning, pages 1180–1189. PMLR, 2015.

Junyu Gao, Mengyuan Chen, Liangyu Xiang, and Changsheng Xu. A comprehensive survey on evidential deep learning and its applications. arXiv preprint arXiv:2409.04720, 2024.

Z.A. Garczarczyk. Interval neural networks. In Proceedings of the IEEE International Symposium on Circuits and Systems, volume 3, pages 567–570 vol.3, 2000.

Shailesh Garg and Souvik Chakraborty. Vb-deeponet: A bayesian operator learning framework for uncertainty quantification. Engineering Applications of Artificial Intelligence, 118:105685, 2023.

Stefano Gasperini, Jan Haug, Mohammad-Ali Nikouei Mahani, Alvaro Marcos-Ramiro, Nassir Navab, Benjamin Busam, and Federico Tombari. Certainnet: Sampling-free uncertainty estimation for object detection. IEEE Robotics and Automation Letters, 7(2):698–705, 2021.

Stuart Geman and Donald Geman. Stochastic relaxation, gibbs distributions, and the Bayesian restoration of images. IEEE Transactions on Pattern Analysis and Machine Intelligence, PAMI-6(6):721–741, 1984. doi: 10.1109/TPAMI.1984.4767596.

Kamran Ghasedi Dizaji, Amirhossein Herandi, Cheng Deng, Weidong Cai, and Heng Huang. Deep clustering via joint convolutional autoencoder embedding and relative entropy minimization. In Proceedings of the IEEE international conference on computer vision, pages 5736–5745, 2017.

Eleonora Giunchiglia, Mihaela Cătălina Stoian, Salman Khan, Fabio Cuzzolin, and Thomas Lukasiewicz. Road-r: The autonomous driving dataset with logical requirements. Machine Learning, pages 1–31, 2023.

<!-- page: 171 -->

Ethan Goan and Clinton Fookes. Bayesian neural networks: An introduction and survey. Case Studies in Applied Bayesian Data Science: CIRM Jean-Morlet Chair, Fall 2018, pages 45–87, 2020.

Wenjuan Gong and Fabio Cuzzolin. A belief-theoretical approach to example-based pose estimation. IEEE Transactions on Fuzzy Systems, 26(2):598–611, 2017.

Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining and harnessing adversarial examples. arXiv preprint arXiv:1412.6572, 2014.

Michel Grabisch, Michio Sugeno, and Toshiaki Murofushi. Fuzzy measures and integrals: theory and applications. New York: Springer, 2000.

Andreas Graefe, Helmut Küchenhoff, Veronika Stierle, and Bernhard Riedl. Limitations of ensemble Bayesian model averaging for forecasting social science problems. International Journal of Forecasting, 31(3):943–951, 2015.

Alex Graves. Practical variational inference for neural networks. In J. Shawe-Taylor, R. Zemel, P. Bartlett, F. Pereira, and K.Q. Weinberger, editors, Advances in Neural Information Processing Systems, volume 24. Curran Associates, Inc., 2011. URL https://proceedings.neurips.cc/paper/2011/file/7eb3c8be3d411e8ebfab08eba5f49632-Paper.pdf.

Ander Gray, Vignesh Gopakumar, Sylvain Rousseau, and Sébastien Destercke. Guaranteed confidence-band enclosures for pde surrogates. arXiv preprint arXiv:2501.18426, 2025.

Derek Greene and Pádraig Cunningham. Practical solutions to the problem of diagonal dominance in kernel document clustering. In Proc. 23rd International Conference on Machine learning (ICML'06), pages 377–384. ACM Press, 2006.

Ishaan Gulrajani and David Lopez-Paz. In search of lost domain generalization. arXiv preprint arXiv:2007.01434, 2020.

Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. On calibration of modern neural networks. In International conference on machine learning, pages 1321–1330. PMLR, 2017a.

Xifeng Guo, Xinwang Liu, En Zhu, and Jianping Yin. Deep clustering with convolutional autoencoders. In Neural Information Processing: 24th International Conference, ICONIP 2017, Guangzhou, China, November 14-18, 2017, Proceedings, Part II 24, pages 373–382. Springer, 2017b.

Fredrik K Gustafsson, Martin Danelljan, and Thomas B Schon. Evaluating scalable bayesian deep learning methods for robust computer vision. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition workshops, pages 318–319, 2020.

Joseph Y. Halpern. Reasoning About Uncertainty. MIT Press, 2017.

W. K. Hastings. Monte carlo sampling methods using markov chains and their applications. Biometrika, 57(1):97–109, 1970. ISSN 00063444, 14643510. URL http://www.jstor.org/stable/2334940.

<!-- page: 172 -->

Alexander Havrilla, Maksym Zhuravinskyi, Duy Phung, Aman Tiwari, Jonathan Tow, Stella Biderman, Quentin Anthony, and Louis Castricato. trlx: A framework for large scale reinforcement learning from human feedback. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 8578–8595, 2023.

Bobby He, Balaji Lakshminarayanan, and Yee Whye Teh. Bayesian deep ensembles via the neural tangent kernel. Advances in neural information processing systems, 33:1010–1022, 2020.

Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2016.

Dan Hendrycks and Kevin Gimpel. A baseline for detecting misclassified and out-of-distribution examples in neural networks. arXiv preprint arXiv:1610.02136, 2016.

Dan Hendrycks, Kevin Zhao, Steven Basart, Jacob Steinhardt, and Dawn Song. Natural adversarial examples. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 15262–15271, 2021.

Max Hinne, Quentin F Gronau, Don van den Bergh, and Eric-Jan Wagenmakers. A conceptual introduction to Bayesian model averaging. Advances in Methods and Practices in Psychological Science, 3(2):200–215, 2020.

Marius Hobbhahn, Agustinus Kristiadi, and Philipp Hennig. Fast predictive uncertainty for classification with Bayesian deep networks. In Uncertainty in Artificial Intelligence, pages 822–832. PMLR, 2022.

Jennifer A Hoeting, David Madigan, Adrian E Raftery, and Chris T Volinsky. Bayesian model averaging: a tutorial (with comments by m. clyde, david draper and ei george, and a rejoinder by the authors. Statistical science, 14(4):382–417, 1999.

Matthew D Hoffman, Andrew Gelman, et al. The No-U-Turn sampler: adaptively setting path lengths in Hamiltonian Monte Carlo. J. Mach. Learn. Res., 15(1):1593–1623, 2014.

Shoubo Hu, Kun Zhang, Zhitang Chen, and Laiwan Chan. Domain generalization via multidomain discriminant analysis. In Uncertainty in artificial intelligence, pages 292–302. PMLR, 2020.

Allen H Huang, Amy Y Zang, and Rong Zheng. Evidence on the information content of text in analyst reports. The Accounting Review, 89(6):2151–2180, 2014.

Eyke Hüllermeier and Willem Waegeman. Aleatoric and epistemic uncertainty in machine learning: A tutorial introduction. CoRR, abs/1910.09457, 2019. URL http://arxiv.org/abs/1910.09457.

Eyke Hüllermeier and Willem Waegeman. Aleatoric and epistemic uncertainty in machine learning: An introduction to concepts and methods. Machine Learning, 110(3):457–506, 2021.

Eyke Hüllermeier, Sébastien Destercke, and Mohammad Hossein Shaker. Quantification of credal uncertainty in machine learning: A critical analysis and empirical comparison. In Proceedings of the Uncertainty in Artificial Intelligence, pages 548–557. PMLR, 2022.

<!-- page: 173 -->

Hisao Ishibuchi, Hideo Tanaka, and Hidehiko Okada. An architecture of neural networks with interval weights and its application to fuzzy regression analysis. Fuzzy Sets and Systems, 57 (1):27–39, 1993.

Masha Itkina, Boris Ivanovic, Ransalu Senanayake, Mykel J Kochenderfer, and Marco Pavone. Evidential sparsification of multimodal latent spaces in conditional variational autoencoders. Advances in Neural Information Processing Systems, 33:10235–10246, 2020.

Mojan Javaheripi, Sébastien Bubeck, Marah Abdin, Jyoti Aneja, Sebastien Bubeck, Caio César Teodoro Mendes, Weizhu Chen, Allie Del Giorno, Ronen Eldan, Sivakanth Gopi, et al. Phi-2: The surprising power of small language models. Microsoft Research Blog, 1(3):3, 2023.

Alireza Javanmardi, David Stutz, and Eyke Hüllermeier. Conformalized credal set predictors. arXiv preprint arXiv:2402.10723, 2024.

Harold Jeffreys. The theory of probability. OuP Oxford, 1998.

Saurav Jha, Dong Gong, He Zhao, and Lina Yao. Npcl: Neural processes for uncertainty-aware continual learning. Advances in Neural Information Processing Systems, 36, 2024.

Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023. URL https://arxiv.org/abs/2310.06825.

Audun Jøsang. Subjective logic, volume 3. Springer, 2016.

Laurent Valentin Jospin, Hamid Laga, Farid Boussaid, Wray Buntine, and Mohammed Bennamoun. Hands-on bayesian neural networks—a tutorial for deep learning users. IEEE Computational Intelligence Magazine, 17(2):29–48, 2022.

John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al. Highly accurate protein structure prediction with alphafold. nature, 596(7873):583–589, 2021.

Robert E Kass and Larry Wasserman. The selection of prior distributions by formal rules. Journal of the American statistical Association, 91(435):1343–1370, 1996.

Alex Kendall and Yarin Gal. What uncertainties do we need in Bayesian deep learning for computer vision? arXiv:1703.04977, 2017.

David G. Kendall. Foundations of a theory of random sets. In E. F. Harding and D. G. Kendall, editors, Stochastic Geometry, pages 322–376. Wiley, London, 1974.

John Maynard Keynes. A treatise on probability. Courier Corporation, 2013.

Salman Khan, Izzeddin Teeti, Reza Javanmard Alitappeh, Mihaela C Stoian, Eleonora Giunchiglia, Gurkirt Singh, Andrew Bradley, and Fabio Cuzzolin. Road-waymo: Action awareness at scale for autonomous driving. arXiv preprint arXiv:2411.01683, 2024.

Abbas Khosravi, Saeid Nahavandi, Doug Creighton, and Amir F. Atiya. Lower upper bound estimation method for construction of neural network-based prediction intervals. IEEE Transactions on Neural Networks, 22(3):337–346, 2011.

<!-- page: 174 -->

Diederik P Kingma and Max Welling. Auto-encoding Variational Bayes. arXiv preprint arXiv:1312.6114, 2013.

Durk P Kingma, Tim Salimans, and Max Welling. Variational dropout and the local Reparameterization trick. Advances in Neural Information Processing Systems, 28, 2015.

James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the national academy of sciences, 114(13):3521–3526, 2017.

Bas JK Kleijn and Aad W Van der Vaart. The bernstein-von-mises theorem under misspecification. 2012.

George J Klir. Where do we stand on measures of uncertainty, ambiguity, fuzziness, and the like? Fuzzy sets and systems, 24(2):141–160, 1987.

Pang Wei Koh, Shiori Sagawa, Henrik Marklund, Sang Michael Xie, Marvin Zhang, Akshay Balsubramani, Weihua Hu, Michihiro Yasunaga, Richard Lanas Phillips, Irena Gao, et al. Wilds: A benchmark of in-the-wild distribution shifts. In International conference on machine learning, pages 5637–5664. PMLR, 2021.

Andrei N Kolmogorov. Three approaches to the quantitative definition ofinformation'. Problems of information transmission, 1(1):1–7, 1965.

Andrei N. Kolmogorov and Albert T. Bharucha-Reid. Foundations of the theory of probability: Second English Edition. Courier Dover Publications, 2018.

Anna-Kathrin Kopetzki, Bertrand Charpentier, Daniel Zügner, Sandhya Giri, and Stephan Günnemann. Evaluating robustness of predictive uncertainty estimation: Are dirichlet-based models reliable? In International Conference on Machine Learning, pages 5707–5718. PMLR, 2021.

Piotr A Kowalski and Piotr Kulczycki. Interval probabilistic neural network. Neural Computing and Applications, 28(4):817–834, 2017.

Ivan Kramosil. Nonspecificity degrees of basic probability assignments in Dempster–Shafer theory. Computing and Informatics, 18(6):559–574, 1999.

Alex Krizhevsky. Learning multiple layers of features from tiny images. University of Toronto, 2012.

Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. CIFAR-10 (Canadian Institute For Advanced Research). Technical report, CIFAR, 2009. URL https://www.cs.toronto.edu/~kriz/cifar.html.

Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convolutional neural networks. In F. Pereira, C.J. Burges, L. Bottou, and K.Q. Weinberger, editors, Advances in Neural Information Processing Systems, volume 25. Curran Associates, Inc., 2012. URL https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf.

<!-- page: 175 -->

Volodymyr Kuleshov, Nathan Fenner, and Stefano Ermon. Accurate uncertainties for deep learning using calibrated regression. In International conference on machine learning, pages 2796–2804. PMLR, 2018.

Brian Kulis and Michael I Jordan. Revisiting k-means: New algorithms via bayesian nonparametrics. arXiv preprint arXiv:1111.0352, 2011.

Yongchan Kwon, Joong-Ho Won, Beom Joon Kim, and Myunghee Cho Paik. Uncertainty quantification using Bayesian neural networks in classification: Application to biomedical image segmentation. Computational Statistics & Data Analysis, 142:106816, 2020.

Hicham Laanaya, Arnaud Martin, Driss Aboutajdine, and Ali Khenchaf. Support vector regression of membership functions and belief functions – Application for pattern recognition. Information Fusion, 11(4):338–350, 2010.

Yuandu Lai, Yucheng Shi, Yahong Han, Yunfeng Shao, Meiyu Qi, and Bingshuai Li. Exploring uncertainty in regression neural networks for construction of prediction intervals. Neurocomputing, 481:249–257, 2022.

Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles. Advances in Neural Information Processing Systems, 30, 2017.

Antonis Lambrou, Harris Papadopoulos, and Alex Gammerman. Reliable confidence measures for medical diagnosis with evolutionary algorithms. IEEE Transactions on Information Technology in Biomedicine, 15(1):93–99, 2010.

Jouko Lampinen and Aki Vehtari. Bayesian approach for neural networks—review and case studies. Neural networks, 14(3):257–274, 2001.

Yann LeCun and Corinna Cortes. The MNIST database of handwritten digits. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 1–9, 2005. doi: 10.1109/CVPR.2005.177. URL https://ieeexplore.ieee.org/document/1467284.

Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. Nature, 521(7553):436–444, 2015.

Isaac Levi. The enterprise of knowledge: An essay on knowledge, credal probability, and chance. MIT press, 1980.

Jeremiah Liu, Zi Lin, Shreyas Padhy, Dustin Tran, Tania Bedrax Weiss, and Balaji Lakshminarayanan. Simple and principled uncertainty estimation with deterministic deep learning via distance awareness. Advances in neural information processing systems, 33:7498–7512, 2020.

Zhun-Ga Liu, Yu Liu, Jean Dezert, and Fabio Cuzzolin. Evidence combination based on credal belief redistribution for pattern classification. IEEE Transactions on Fuzzy Systems, 28(4): 618–631, 2019.

Christos Louizos and Max Welling. Multiplicative normalizing flows for variational bayesian neural networks. In International Conference on Machine Learning, pages 2218–2227. PMLR, 2017.

<!-- page: 176 -->

Rachel Luo, Aadyot Bhatnagar, Yu Bai, Shengjia Zhao, Huan Wang, Caiming Xiong, Silvio Savarese, Stefano Ermon, Edward Schmerling, and Marco Pavone. Local calibration: metrics and recalibration. In Uncertainty in Artificial Intelligence, pages 1286–1295. PMLR, 2022.

David J. C. MacKay. A Practical Bayesian Framework for Backpropagation Networks. Neural Computation, 4(3):448–472, 05 1992. ISSN 0899-7667. doi: 10.1162/neco.1992.4.3.448. URL https://doi.org/10.1162/neco.1992.4.3.448.

Andrzej Maćkiewicz and Waldemar Ratajczak. Principal components analysis (pca). Computers & Geosciences, 19(3):303–342, 1993.

Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, and Adrian Vladu. Towards deep learning models resistant to adversarial attacks. stat, 1050(9), 2017.

Emilia Magnani, Nicholas Krämer, Runa Eschenhagen, Lorenzo Rosasco, and Philipp Hennig. Approximate bayesian neural operators: Uncertainty quantification for parametric pdes. arXiv preprint arXiv:2208.01565, 2022.

Andrey Malinin and Mark Gales. Predictive uncertainty estimation via prior networks. Advances in neural information processing systems, 31, 2018.

Andrey Malinin and Mark Gales. Reverse KL-divergence training of prior networks: Improved uncertainty and adversarial robustness. Advances in Neural Information Processing Systems, 32, 2019.

Andrey Malinin, Bruno Mlodozeniec, and Mark Gales. Ensemble distribution distillation. In International Conference on Learning Representations, 2019.

Shireen Kudukkil Manchingal and Fabio Cuzzolin. Epistemic deep learning. arXiv preprint arXiv:2206.07609, 2022.

Shireen Kudukkil Manchingal, Muhammad Mubashar, Kaizheng Wang, and Fabio Cuzzolin. A unified evaluation framework for epistemic predictions, 2025a. URL https://arxiv.org/abs/2501.16912.

Shireen Kudukkil Manchingal, Muhammad Mubashar, Kaizheng Wang, Keivan Shariatmadar, and Fabio Cuzzolin. Random-set neural networks. In The Thirteenth International Conference on Learning Representations, 2025b. URL https://openreview.net/forum?id=pdjkikvCch.

Robin Manhaeve, Sebastijan Dumancic, Angelika Kimmig, Thomas Demeester, and Luc De Raedt. Deepproblog: Neural probabilistic logic programming. Advances in neural information processing systems, 31, 2018.

Jiayuan Mao, Chuang Gan, Pushmeet Kohli, Joshua B Tenenbaum, and Jiajun Wu. The neuro-symbolic concept learner: Interpreting scenes, words, and sentences from natural supervision. arXiv preprint arXiv:1904.12584, 2019.

Bruce G. Marcot. Metrics for evaluating performance and uncertainty of bayesian network models. Ecological Modelling, 230:50–62, 2012. ISSN 0304-3800. doi: https://doi.org/10.1016/j.ecolmodel.2012.01.013. URL https://www.sciencedirect.com/science/article/pii/S0304380012000245.

<!-- page: 177 -->

Pablo Márquez-Neila, Mathieu Salzmann, and Pascal Fua. Imposing hard constraints on deep networks: Promises and limitations. arXiv preprint arXiv:1706.02025, 2017.

Ryan Martin and Chuanhai Liu. Inferential models: A framework for prior-free posterior probabilistic inference. Journal of the American Statistical Association, 108(501):301–313, 2013.

Ryan Martin and Chuanhai Liu. Inferential models: reasoning with uncertainty. CRC Press, 2015.

Georges Matheron. Random sets and integral geometry. Wiley Series in Probability and Mathematical Statistics, New York, 1975.

Joshua Maynez, Shashi Narayan, Bernd Bohnet, and Ryan McDonald. On faithfulness and factuality in abstractive summarization. arXiv preprint arXiv:2005.00661, 2020.

Leland McInnes, John Healy, and James Melville. Umap: Uniform manifold approximation and projection for dimension reduction. arXiv preprint arXiv:1802.03426, 2018.

María Luisa Menéndez, JA Pardo, L Pardo, and MC Pardo. The jensen-shannon divergence. Journal of the Franklin Institute, 334(2):307–318, 1997.

Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. Can a suit of armor conduct electricity? a new dataset for open book question answering. In EMNLP, 2018.

Matthias Minderer, Josip Djolonga, Rob Romijnders, Frances Hubis, Xiaohua Zhai, Neil Houlsby, Dustin Tran, and Mario Lucic. Revisiting the calibration of modern neural networks. Advances in Neural Information Processing Systems, 34:15682–15694, 2021.

Enrique Miranda. A survey of the theory of coherent lower previsions. International Journal of

<!-- page: 178 -->

Approximate Reasoning, 48(2):628–658, 2008.

Enrique Miranda, Ignacio Montes, and Paolo Vicig. On the selection of an optimal outer approximation of a coherent lower probability. Fuzzy Sets and Systems, 424:1–36, 2021.

Enrique Miranda, Ignacio Montes, and Andrés Presa. Inner approximations of coherent lower probabilities and their application to decision making problems. Annals of Operations Research, pages 1–39, 2023.

Tom M Mitchell. The need for biases in learning generalizations. 1980.

Ilya Molchanov. Random sets and random functions. Theory of Random Sets, pages 451–552, 2017.

Ilya S Molchanov. Theory of random sets, volume 19. Springer, 2005.

Thomas Mortier, Marek Wydmuch, Krzysztof Dembczyński, Eyke Hüllermeier, and Willem Waegeman. Efficient set-valued prediction in multi-class classification. Data Mining and Knowledge Discovery, 35(4):1435–1469, 2021.

Krikamol Muandet, David Balduzzi, and Bernhard Schölkopf. Domain generalization via invariant feature representation. In Proceedings of the 30th International Conference on International Conference on Machine Learning - Volume 28, ICML'13, page I–10–I–18. JMLR.org, 2013.

<!-- page: 179 -->

Bálint Mucsányi, Michael Kirchhof, and Seong Joon Oh. Benchmarking uncertainty disentanglement: Specialized uncertainties for specialized tasks. Advances in neural information processing systems, 37:50972–51038, 2024.

Jishnu Mukhoti, Viveka Kulharia, Amartya Sanyal, Stuart Golodetz, Philip Torr, and Puneet Dokania. Calibrating deep neural networks using focal loss. Advances in Neural Information Processing Systems, 33:15288–15299, 2020.

Jishnu Mukhoti, Andreas Kirsch, Joost van Amersfoort, Philip HS Torr, and Yarin Gal. Deep deterministic uncertainty: A new simple baseline. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 24384–24394, 2023.

Daniel Müllner. Modern hierarchical, agglomerative clustering algorithms. arXiv preprint arXiv:1109.2378, 2011.

Mahdi Pakdaman Naeini, Gregory Cooper, and Milos Hauskrecht. Obtaining well calibrated probabilities using bayesian binning. In Proceedings of the AAAI conference on artificial intelligence, volume 29, 2015.

Radford Neal. Bayesian learning via stochastic dynamics. In S. Hanson, J. Cowan, and C. Giles, editors, Advances in Neural Information Processing Systems, volume 5. Morgan-Kaufmann, 1992. URL https://proceedings.neurips.cc/paper/1992/file/f29c21d4897f78948b91f03172341b7b-Paper.pdf.

Radford M Neal. Bayesian learning for neural networks, volume 118. Springer Science & Business Media, 2012.

Radford M Neal et al. MCMC using Hamiltonian dynamics. Handbook of Markov Chain Monte Carlo, 2(11):2, 2011.

Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco, Baolin Wu, Andrew Y Ng, et al. Reading digits in natural images with unsupervised feature learning. In NIPS workshop on deep learning and unsupervised feature learning, volume 2011, page 7. Granada, Spain, 2011.

Anh Nguyen, Jason Yosinski, and Jeff Clune. Deep neural networks are easily fooled: High confidence predictions for unrecognizable images. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), June 2015.

Hung T. Nguyen. On random sets and belief functions. Journal of Mathematical Analysis and Applications, 65:531–542, 1978.

Vu-Linh Nguyen, Sébastien Destercke, Marie-Hélène Masson, and Eyke Hüllermeier. Reliable multi-class classification based on pairwise epistemic and aleatoric uncertainty. In Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence, IJCAI-18, pages 5089–5095. International Joint Conferences on Artificial Intelligence Organization, 7 2018. doi: 10.24963/ijcai.2018/706. URL https://doi.org/10.24963/ijcai.2018/706.

Jeremy Nixon, Michael W Dusenberry, Linchuan Zhang, Ghassen Jerfel, and Dustin Tran. Measuring calibration in deep learning. In CVPR workshops, volume 2, 2019.

Ilia Nouretdinov, Tom Melluish, and Volodya Vovk. Ridge regression confidence machine. In Proceedings of the Eighteenth International Conference on Machine Learning, pages 385–392. Morgan Kaufmann, 2001.

<!-- page: 180 -->

Luis Oala, Cosmas Heiß, Jan Macdonald, Maximilian März, Gitta Kutyniok, and Wojciech Samek. Detecting failure modes in image reconstructions with interval neural network uncertainty. International Journal of Computer Assisted Radiology and Surgery, 16(12):2089–2097, 2021.

Francisco M Ojeda, Max L Jansen, Alexandre Thiéry, Stefan Blankenberg, Christian Weimar, Matthias Schmid, and Andreas Ziegler. Calibrating machine learning approaches for probability estimation: A comprehensive comparison. Statistics in Medicine, 42(29):5451–5478, 2023.

Kazuki Osawa, Siddharth Swaroop, Mohammad Emtiyaz E Khan, Anirudh Jain, Runa Eschenhagen, Richard E Turner, and Rio Yokota. Practical deep learning with bayesian principles. Advances in neural information processing systems, 32, 2019.

Ian Osband, Zheng Wen, Seyed Mohammad Asghari, Vikranth Dwaracherla, Morteza Ibrahimi, Xiuyuan Lu, and Benjamin Van Roy. Epistemic neural networks. Advances in Neural Information Processing Systems, 36, 2024.

Yaniv Ovadia, Emily Fertig, Jie Ren, Zachary Nado, David Sculley, Sebastian Nowozin, Joshua Dillon, Balaji Lakshminarayanan, and Jasper Snoek. Can you trust your model's uncertainty? evaluating predictive uncertainty under dataset shift. Advances in neural information processing systems, 32, 2019.

Nikhil R Pal, James C Bezdek, and Rohan Hemasinha. Uncertainty measures for evidential reasoning ii: A new measure of total uncertainty. International Journal of Approximate Reasoning, 8(1):1–16, 1993.

Harris Papadopoulos, Kostas Proedrou, Volodya Vovk, and Alex Gammerman. Inductive confidence machines for regression. In Tapio Elomaa, Heikki Mannila, and Hannu Toivonen, editors, Machine Learning: ECML 2002, pages 345–356, Berlin, Heidelberg, 2002a. Springer Berlin Heidelberg. ISBN 978-3-540-36755-0.

Harris Papadopoulos, Vladimir Vovk, and Alexander Gammerman. Qualified prediction for large data sets in the case of pattern recognition. In ICMLA, pages 159–163, 2002b.

Harris Papadopoulos, Alex Gammerman, and Volodya Vovk. Normalized nonconformity measures for regression conformal prediction. In Proceedings of the 26th IASTED International Conference on Artificial Intelligence and Applications, AIA '08, page 64–69, USA, 2008. ACTA Press. ISBN 9780889867109.

Nicolas Papernot, Patrick McDaniel, Somesh Jha, Matt Fredrikson, Z Berkay Celik, and Ananthram Swami. The limitations of deep learning in adversarial settings. In 2016 IEEE European Symposium on Security and Privacy (EuroS&P), pages 372–387, 2016.

Inseok Park and Ramana V Grandhi. Quantifying multiple types of uncertainty in physics-based simulation using bayesian model averaging. AIAA journal, 49(5):1038–1045, 2011.

Zdzislaw Pawlak. Rough sets. International Journal of Computer and Information Sciences, 11 (5):341–356, 1982.

Tim Pearce, Alexandra Brintrup, Mohamed Zaki, and Andy Neely. High-quality prediction intervals for deep learning: A distribution-free, ensembled approach. In International conference on machine learning, pages 4075–4084. PMLR, 2018.

<!-- page: 181 -->

Processing. Association for Computational Linguistics, 11 2019. URL https://arxiv.org/abs/1908.10084.

Hippolyt Ritter, Aleksandar Botev, and David Barber. A scalable laplace approximation for neural networks. In 6th international conference on learning representations, ICLR 2018-conference track proceedings, volume 6. International Conference on Representation Learning, 2018.

Galina Rogova. Combining the results of several neural network classifiers. Classic Works of the Dempster-Shafer Theory of Belief Functions, pages 683–692, 2008.

David Rolnick, Arun Ahuja, Jonathan Schwarz, Timothy Lillicrap, and Gregory Wayne. Experience replay for continual learning. Advances in neural information processing systems, 32, 2019.

Elan Rosenfeld, Pradeep Ravikumar, and Andrej Risteski. An online learning approach to interpolation and extrapolation in domain generalization. In International Conference on Artificial Intelligence and Statistics, pages 2641–2657. PMLR, 2022.

Tim GJ Rudner, Zonghao Chen, Yee Whye Teh, and Yarin Gal. Tractable function-space variational inference in Bayesian neural networks. Advances in Neural Information Processing Systems, 35:22686–22698, 2022.

Stuart Russell, Daniel Dewey, and Max Tegmark. Research priorities for robust and beneficial artificial intelligence. AI magazine, 36(4):105–114, 2015.

Tárik S. Salem, Helge Langseth, and Heri Ramampiaro. Prediction intervals: Split normal mixture from quality-driven deep ensembles. In Jonas Peters and David Sontag, editors, Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI), volume 124 of Proceedings of Machine Learning Research, pages 1179–1187. PMLR, 03–06 Aug 2020.

Yusuf Sale, Michele Caprio, and Eyke Hüllermeier. Is the volume of a credal set a good measure for epistemic uncertainty? In Uncertainty in Artificial Intelligence, pages 1795–1804. PMLR, 2023.

Luis Samaniego, Stephan Thober, Rohini Kumar, Niko Wanders, Oldrich Rakovec, Ming Pan, Matthias Zink, Justin Sheffield, Eric F Wood, and Andreas Marx. Anthropogenic warming exacerbates european soil moisture droughts. Nature Climate Change, 8(5):421–426, 2018.

Craig Saunders, Alexander Gammerman, and Volodya Vovk. Transduction with confidence and credibility. In Proceedings of the Sixteenth International Joint Conference on Artificial Intelligence, IJCAI '99, page 722–726, San Francisco, CA, USA, 1999. Morgan Kaufmann Publishers Inc. ISBN 1558606130.

Wilko Schwarting, Javier Alonso-Mora, and Daniela Rus. Planning and decision-making for autonomous vehicles. Annual Review of Control, Robotics, and Autonomous Systems, 1(1): 187–210, 2018.

Clayton Scott. Calibrated asymmetric surrogate losses. Electronic Journal of Statistics, 6(none): 958 – 992, 2012. doi: 10.1214/12-EJS699. URL https://doi.org/10.1214/12-EJS699.

<!-- page: 182 -->

Robin Senge, Stefan Bösner, Krzysztof Dembczyński, Jörg Haasenritter, Oliver Hirsch, Norbert Donner-Banzhoff, and Eyke Hüllermeier. Reliable classification: Learning classifiers that distinguish aleatoric and epistemic uncertainty. Information Sciences, 255:16–29, 2014.

Murat Sensoy, Lance Kaplan, and Melih Kandemir. Evidential deep learning to quantify classification uncertainty. In Proceedings of the 32nd International Conference on Neural Information Processing Systems, NIPS'18, page 3183–3193, Red Hook, NY, USA, 2018. Curran Associates Inc.

Armin Seyeditabari, Narges Tabari, and Wlodek Zadrozny. Emotion detection in text: a review. arXiv preprint arXiv:1806.00674, 2018.

Ahamed Shafeeq and KS Hareesha. Dynamic clustering of data with modified k-means algorithm. In Proceedings of the 2012 conference on information and computer networks, pages 221–225, 2012.

Glenn Shafer. A mathematical theory of evidence, volume 42. Princeton university press, 1976.

Glenn Shafer. Two theories of probability. In PSA: Proceedings of the Biennial Meeting of the Philosophy of Science Association, volume 1978, pages 441–465. Philosophy of Science Association, 1978.

Glenn Shafer. The combination of evidence. Technical Report 162, School of Business, University of Kansas, 1984.

Glenn Shafer and Vladimir Vovk. A tutorial on Conformal Prediction. Journal of Machine Learning Research, 9(3), 2008.

Mohammad Hossein Shaker and Eyke Hüllermeier. Ensemble-based uncertainty quantification: Bayesian versus credal inference. In PROCEEDINGS 31. WORKSHOP COMPUTATIONAL INTELLIGENCE, volume 25, page 63, 2021.

Jonathon Shlens. Notes on kullback-leibler divergence and likelihood. arXiv preprint arXiv:1404.2000, 2014.

Anurag Singh, Siu Lun Chau, Shahine Bouabid, and Krikamol Muandet. Domain generalisation via imprecise learning. arXiv preprint arXiv:2404.04669, 2024.

Gurkirt Singh, Stephen Akrigg, Manuele Di Maio, Valentina Fontana, Reza Javanmard Alitappeh, Salman Khan, Suman Saha, Kossar Jeddisaravi, Farzad Yousefi, Jacob Culley, et al. Road: The road event awareness dataset for autonomous driving. IEEE transactions on pattern analysis and machine intelligence, 45(1):1036–1054, 2022.

Florentin Smarandache, Arnaud Martin, and Christophe Osswald. Contradiction measures and specificity degrees of basic belief assignments. In 14th International Conference on Information Fusion, pages 1–8. IEEE, 2011.

Philippe Smets. Decision making in the TBM: the necessity of the pignistic transformation. International Journal of Approximate Reasoning, 38(2):133–147, 2005. ISSN 0888-613X. doi: https://doi.org/10.1016/j.ijar.2004.05.003. URL https://www.sciencedirect.com/science/article/pii/S0888613X04000593.

<!-- page: 183 -->

Philippe Smets. Bayes' theorem generalized for belief functions. In Proceedings of the 7th European Conference on Artificial Intelligence (ECAI-86), volume 2, pages 169–171, July 1986.

Philippe Smets and Robert Kennes. The transferable belief model. Artificial intelligence, 66(2): 191–234, 1994.

Ronald D. Snee. Statistical thinking and its contribution to total quality. The American Statistician, 44(2):116–121, 1990.

S.D Snowling and J.R Kramer. Evaluating modelling uncertainty for model selection. Ecological Modelling, 138(1):17–30, 2001. ISSN 0304-3800. doi: https://doi.org/10.1016/S0304-3800(00)00390-2. URL https://www.sciencedirect.com/science/article/pii/S0304380000003902.

Yafei Song, Xiaodan Wang, Wenhua Wu, Wen Quan, and Wenlong Huang. Evidence combination based on credibility and non-specificity. Pattern Analysis and Applications, 21:167–180, 2018.

Vincent Spruyt. How to draw a covariance error ellipse. 2014. Computer Vision for Dummies.[Available Online-http://www. visiondummy. com/2014/04/drawerror-ellipse-representing-covariance-matrix/], 2013.

Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. The journal of machine learning research, 15(1):1929–1958, 2014.

Maximilian Stadler, Bertrand Charpentier, Simon Geisler, Daniel Zügner, and Stephan Günnemann. Graph posterior network: Bayesian predictive uncertainty for node classification. Advances in Neural Information Processing Systems, 34:18033–18048, 2021.

Thomas M Strat. Continuous belief functions for evidential reasoning. In AAAI, pages 308–313, 1984.

Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien Chouard, Vijaysai Patnaik, Paul Tsui, James Guo, Yin Zhou, Yuning Chai, Benjamin Caine, Vijay Vasudevan, Wei Han, Jiquan Ngiam, Hang Zhao, Aleksei Timofeev, Scott Ettinger, Maxim Krivokon, Amy Gao, Aditya Joshi, Yu Zhang, Jonathon Shlens, Zhifeng Chen, and Dragomir Anguelov. Scalability in perception for autonomous driving: Waymo open dataset. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), June 2020.

Shengyang Sun, Guodong Zhang, Jiaxin Shi, and Roger Grosse. Functional variational bayesian neural networks. arXiv preprint arXiv:1903.05779, 2019.

Adith Swaminathan and Thorsten Joachims. The self-normalized estimator for counterfactual learning. advances in neural information processing systems, 28, 2015.

Linwei Tao, Minjing Dong, and Chang Xu. Dual focal loss for calibration. In International Conference on Machine Learning, pages 33833–33849. PMLR, 2023.

Izzeddin Teeti, Rongali Sai Bhargav, Vivek Singh, Andrew Bradley, Biplab Banerjee, and Fabio Cuzzolin. Temporal dino: A self-supervised video strategy to enhance action prediction. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 3281–3291, 2023.

<!-- page: 184 -->

Wayne E Thogmartin. Sensitivity analysis of north american bird population estimates. Ecological Modelling, 221(2):173–177, 2010.

D Michael Titterington. Bayesian methods for neural networks and related models. Statistical science, pages 128–139, 2004.

Zheng Tong, Philippe Xu, and Thierry Denoeux. An evidential classifier based on Dempster-Shafer theory and deep learning. Neurocomputing, 450:275–293, 2021.

Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.

Salsabil Trabelsi, Zied Elouedi, and Pawan Lingras. Classification systems based on rough sets under the belief function framework. Int. J. Approx. Reason., 52:1409–1432, 2011.

Ba-Hien Tran, Simone Rossi, Dimitrios Milios, and Maurizio Filippone. All you need is a good functional prior for Bayesian deep learning. arXiv preprint arXiv:2011.12829, 2020.

Krasymyr Tretiak, Georg Schollmeyer, and Scott Ferson. Neural network model for imprecise regression with interval dependent variables. Neural Networks, 161:550–564, 2023.

Matthias Troffaes. Decision making under uncertainty using imprecise probabilities. International Journal of Approximate Reasoning, 45(1):17–29, 2007.

Efthymia Tsamoura, David Carral, Enrico Malizia, and Jacopo Urbani. Materializing knowledge bases via trigger graphs. arXiv preprint arXiv:2102.02753, 2021.

Aman Ullah. Entropy, divergence and distance measures with econometric applications. Journal of Statistical Planning and Inference, 49(1):137–162, 1996.

Dennis Thomas Ulmer, Christian Hardmeier, and Jes Frellsen. Prior and posterior networks: A survey on evidential deep learning methods for uncertainty estimation. Transactions on Machine Learning Research, 2023.

Joost Van Amersfoort, Lewis Smith, Yee Whye Teh, and Yarin Gal. Uncertainty estimation using a single deep deterministic neural network. In International conference on machine learning, pages 9690–9700. PMLR, 2020.

Gido M Van de Ven and Andreas S Tolias. Three scenarios for continual learning. arXiv preprint arXiv:1904.07734, 2019.

Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. Journal of Machine Learning Research, 9(86):2579–2605, 2008. URL http://jmlr.org/papers/v9/vandermaaten08a.html.

Patrick Vannoorenberghe and Philippe Smets. Partially supervised learning by a credal em approach. In Lluís Godo, editor, Symbolic and Quantitative Approaches to Reasoning with Uncertainty, pages 956–967, Berlin, Heidelberg, 2005. Springer Berlin Heidelberg. ISBN 978-3-540-31888-0.

Manuel A Vega and Michael D Todd. A variational Bayesian neural network for structural health monitoring and cost-informed decision-making in miter gates. Structural Health Monitoring, 21(1):4–18, 2022.

<!-- page: 185 -->

Pauli Virtanen, Ralf Gommers, Travis E Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, et al. Scipy 1.0: fundamental algorithms for scientific computing in python. Nature methods, 17(3): 261–272, 2020.

Vladimir Vovk. Cross-conformal predictors. Annals of Mathematics and Artificial Intelligence, 74, 08 2012. doi: 10.1007/s10472-013-9368-4.

Vladimir Vovk and Ivan Petej. Venn-abers predictors. arXiv preprint arXiv:1211.0025, 2012.

Vladimir Vovk, Glenn Shafer, and Ilia Nouretdinov. Self-calibrating probability forecasting. In S. Thrun, L. Saul, and B. Schölkopf, editors, Advances in Neural Information Processing Systems, volume 16. MIT Press, 2003. URL https://proceedings.neurips.cc/paper/2003/file/10c66082c124f8afe3df4886f5e516e0-Paper.pdf.

Vladimir Vovk, Alexander Gammerman, and Glenn Shafer. Algorithmic learning in a random world. Springer Science & Business Media, 2005.

Peter Walley. Statistical Reasoning with Imprecise Probabilities. Chapman and Hall, New York, 1991.

Peter Walley. Inferences from multinomial data: learning about a bag of marbles. Journal of the Royal Statistical Society Series B: Statistical Methodology, 58(1):3–34, 1996.

Peter Walley. Towards a unified theory of imprecise probability. International Journal of Approximate Reasoning, 24(2-3):125–148, 2000.

Anton Wallner. Maximal number of vertices of polytopes defined by f-probabilities. In Fabio Gagliardi Cozman, R. Nau, and Teddy Seidenfeld, editors, Proceedings of the Fourth International Symposium on Imprecise Probabilities and Their Applications (ISIPTA 2005), pages 388–395, 2005.

Kaizheng Wang, Fabio Cuzzolin, Keivan Shariatmadar, David Moens, and Hans Hallez. Credal wrapper of model averaging for uncertainty estimation on out-of-distribution detection. arXiv preprint arXiv:2405.15047, 2024a.

Kaizheng Wang, Fabio Cuzzolin, Keivan Shariatmadar, David Moens, Hans Hallez, et al. Credal deep ensembles for uncertainty quantification. Advances in Neural Information Processing Systems, 37:79540–79572, 2024b.

Kaizheng Wang, Keivan Shariatmadar, Shireen Kudukkil Manchingal, Fabio Cuzzolin, David Moens, and Hans Hallez. Creinns: Credal-set interval neural networks for uncertainty estimation in classification tasks. arXiv preprint arXiv:2401.05043, 2024c.

Yibin Wang, Haizhou Shi, Ligong Han, Dimitris Metaxas, and Hao Wang. Blob: Bayesian low-rank adaptation by backpropagation for large language models. arXiv preprint arXiv:2406.11675, 2024d.

Martin Wattenberg, Fernanda Viégas, and Ian Johnson. How to use t-sne effectively. Distill, 1 (10):e2, 2016.

<!-- page: 186 -->

Max Welling and Yee W Teh. Bayesian learning via stochastic gradient langevin dynamics. In Proceedings of the 28th international conference on machine learning (ICML-11), pages 681–688. Citeseer, 2011.

Yeming Wen, Dustin Tran, and Jimmy Ba. Batchensemble: an alternative approach to efficient ensemble and lifelong learning. arXiv preprint arXiv:2002.06715, 2020.

Ronald J Williams and David Zipser. A learning algorithm for continually running fully recurrent neural networks. Neural computation, 1(2):270–280, 1989.

Keming Wu and Fuyuan Xiao. A novel quantum belief entropy for uncertainty measure in complex evidence theory. Information Sciences, 652:119744, 2024.

Mike Wu and Noah Goodman. A simple framework for uncertainty in contrastive learning. arXiv preprint arXiv:2010.02038, 2020.

Han Xiao, Kashif Rasul, and Roland Vollgraf. Fashion-MNIST: a novel image dataset for benchmarking machine learning algorithms. arXiv preprint arXiv:1708.07747, 2017.

L. Xu, A. Krzyzak, and C.Y. Suen. Methods of combining multiple classifiers and their applications to handwriting recognition. IEEE Transactions on Systems, Man, and Cybernetics, 22(3): 418–435, 1992. doi: 10.1109/21.155943.

Ronald R Yager. Entropy and specificity in a mathematical theory of evidence. Classic works of the Dempster-Shafer theory of belief functions, pages 291–310, 2008.

Adam X Yang, Maxime Robeyns, Xi Wang, and Laurence Aitchison. Bayesian low-rank adaptation for large language models. arXiv preprint arXiv:2308.13111, 2023.

Jianhua Yin and Jianyong Wang. A dirichlet multinomial mixture model-based approach for short text clustering. In Proceedings of the 20th ACM SIGKDD international conference on Knowledge discovery and data mining, pages 233–242, 2014.

Yu Yu, Chao-Han Huck Yang, Jari Kolehmainen, Prashanth G Shivakumar, Yile Gu, Sungho Ryu Roger Ren, Qi Luo, Aditya Gourav, I-Fan Chen, Yi-Chieh Liu, et al. Low-rank adaptation of large language model rescoring for parameter-efficient speech recognition. In 2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU), pages 1–8. IEEE, 2023.

Marco Zaffalon. The Naive Credal Classifier. Journal of Statistical Planning and Inference - J STATIST PLAN INFER, 105:5–21, 06 2002. doi: 10.1016/S0378-3758(01)00201-4.

Marco Zaffalon and Enrico Fagiuoli. Tree-based credal networks for classification. Reliable computing, 9(6):487–509, 2003.

Sergey Zagoruyko and Nikos Komodakis. Wide residual networks. arXiv preprint arXiv:1605.07146, 2016.

Guodong Zhang, Shengyang Sun, David Duvenaud, and Roger Grosse. Noisy natural gradient as variational inference. In International conference on machine learning, pages 5852–5861. PMLR, 2018.

Jindi Zhang, Yang Lou, Jianping Wang, Kui Wu, Kejie Lu, and Xiaohua Jia. Evaluating adversarial attacks on driving safety in vision-based autonomous vehicles. IEEE Internet of Things Journal, 9(5):3443–3456, 2021.

<!-- page: 187 -->

Ervine Zheng, Qi Yu, Rui Li, Pengcheng Shi, and Anne Haake. A continual learning framework for uncertainty-aware interactive image segmentation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 35, pages 6030–6038, 2021.

Qianli Zhou, Guojing Tian, and Yong Deng. Bf-qc: Belief functions on quantum circuits. Expert Systems with Applications, 223:119885, 2023.

Qianli Zhou, Hao Luo, Éloi Bossé, and Yong Deng. Why combining belief functions on quantum circuits? In International Conference on Belief Functions, pages 161–170. Springer, 2024.

Enrico Zio and GE Apostolakis. Two methods for the structured assessment of model uncertainty by experts in performance assessments of radioactive waste repositories. Reliability Engineering & System Safety, 54(2-3):225–241, 1996.

Zongren Zou, Xuhui Meng, and George Em Karniadakis. Uncertainty quantification for noisy inputs–outputs in physics-informed neural networks and neural operators. Computer Methods in Applied Mechanics and Engineering, 433:117479, 2025.
