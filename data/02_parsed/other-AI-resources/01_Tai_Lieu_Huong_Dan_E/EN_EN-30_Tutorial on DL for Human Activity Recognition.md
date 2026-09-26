<!-- page: 1 -->

# Tutorial on Deep Learning for Human Activity Recognition

arXiv:2110.06663v1 [cs.HC] 13 Oct 2021

Marius Bock  
University of Siegen  
Germany  
marius.bock@uni-siegen.de

Alexander Hölzemann  
University of Siegen  
Germany  
alexander.hoelzemann@uni-siegen.de

Michael Moeller  
University of Siegen  
Germany  
michael.moeller@uni-siegen.de

Kristof Van Laerhoven  
University of Siegen  
Germany  
kvl@eti.uni-siegen.de

## ABSTRACT

Activity recognition systems that are capable of estimating human activities from wearable inertial sensors have come a long way in the past decades. Not only have state-of-the-art methods moved away from feature engineering and have fully adopted end-to-end deep learning approaches, best practices for setting up experiments, preparing datasets, and validating activity recognition approaches have similarly evolved. This tutorial was first held at the 2021 ACM International Symposium on Wearable Computers (ISWC'21) and International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp'21). The tutorial, after a short introduction in the research field of activity recognition, provides a hands-on and interactive walk-through of the most important steps in the data pipeline for the deep learning of human activities.

All presentation slides shown during the tutorial, which also contain links to all code exercises, as well as the link of the GitHub page of the tutorial can be found on:
https://mariusbock.github.io/dl-for-har

## KEYWORDS

datasets, neural networks, human activity recognition, wearable sensing

## INTENDED AUDIENCE

We do not require prior knowledge in human activity recognition or deep learning techniques, but instead will demonstrate basic concepts, best practices and upcoming techniques to create human activity recognition systems with deep learning approaches. We assume that participants of this tutorial are already familiar with the basics of Python as a programming language[^1] . The focus of this tutorial is on the correct way to establish a data pipeline for human activity recognition from inertial data: Using existing public activity datasets, participants are shown how to systematically design and evaluate deep learning architectures for activity recognition.

This tutorial is designed to function as a guide in the typical processes to design and evaluate deep learning architectures, once an activity recognition dataset has been recorded and annotated. We show through code examples in a step-by-step process why certain steps are needed, how they affect the system's outcome, and which pitfalls present themselves when designing a deep learning classifier for activity recognition.

[^1]: For those who would like to prepare, we highly recommend this online tutorial on Python for beginners linked at: https://www.python.org/about/gettingstarted/

## 1 MOTIVATION

Physical activities constitute pivotal information that allows us to structure our daily lives. Knowing when which activities happen, and how they are performed, can reveal much about persons' intentions, habits, fitness, and state of mind; It is therefore not surprising that researchers into Ubiquitous Computing and Wearable Computers have displayed a growing interest in the machine recognition of human activities, also known as Human Activity Recognition (often abbreviated as HAR).

In 2014, Bulling et al. [2] designed and organized an exceptionally well-received tutorial on human activity recognition from wearable sensor data. Within their tutorial, they introduced concepts such as the Activity Recognition Chain (ARC), a framework for designing and evaluating activity recognition systems, as well as a case study demonstrating how to work with this ARC. Since the release of said tutorial, a lot has happened in the area of human activity recognition research. Within the last decade, deep learning methods have shown to outperform classical Machine Learning algorithms (see for instance [4, 25, 40] for a few examples) and, as a product of this success, have led to studies investigating the effectiveness of deep learning in activity recognition (see for example [15, 34]).

The ARC, as proposed by Bulling et al. [2], did not yet include deep learning techniques and was solely based on classical Machine Learning approaches. With studies having demonstrated the effectiveness of deep learning for activity recognition with wearable sensors, we argue that releasing an updated tutorial that is adapted to work with deep learning techniques was long overdue. Within this tutorial we therefore introduced the Deep Learning Activity Recognition Chain (DL-ARC), which is a reworked version of the original ARC, encompassing the advances that have been made over the years within the field of deep learning for human activity recognition and deep learning in general. Our work directly ties into the works of Bulling et al. [2] and functions as a step-by-step framework to apply deep learning to any activity recognition use case. Within this tutorial, we will show how state-of-the-art models can be achieved, while along the way explaining all design choices in detail.

Beyond introducing deep learning approaches for activity recognition, other advances within the deep learning community from the past years, such as modifications to the loss function and data augmentation strategies, etc. will be discussed and analysed for their impact via comparison of results with an without employing said modifications.

<!-- page: 2 -->

Bock, Hölzemann, et al.

[FIGURE: Figure 1. Full-width diagram of the Deep Learning Activity Recognition Chain (DL-ARC) pipeline]

Text in figure:
- Raw data
- Preprocessing & segmentation
- Classification
- Evaluation
- Convolutional layers
- Dense / LSTM / … layers
- Softmax
- t
- Sliding window
- vs.
- Timeseries from sensors
- Preprocessed windows
- Neural network architecture
- Predicted vs. true class labels

Figure 1: This updated version of the ARC as proposed by Bulling et al. [2], called Deep Learning Activity Recognition Chain (DL-ARC), shows the different phases of this tutorial. Given a set of inertial sensors, the raw data is first preprocessed and segmented into sliding windows. Unlike the ARC, feature extraction becomes obsolete in the DL-ARC. The raw, segmented and preprocessed sensor data is fed into a classification neural network to obtain a set of predicted labels. The obtained set of predicted labels is assessed using state-of-the-art evaluation metrics.

## 2 OUTLINE

This tutorial is targeted towards anyone who wants to understand how to successfully establish a data pipeline for HAR from inertial data. Participants of this tutorial are shown how to systematically design and evaluate deep learning architectures for activity recognition using our suggested pipeline, namely the DL-ARC. Figure 1 illustrates the pipeline, which most prominently differs from the original ARC in that it does not contain a separate feature engineering step. As predictive performance of classical Machine Learning approaches highly relies on sophisticated, handcrafted features [35], Bulling et al. [2] included a feature extraction phase within the original ARC. However, one main advantage of using deep learning techniques is that they are able to automatically extract discriminative features from raw data input [33], thus making the feature extraction pipeline step obsolete.

To successfully understand the contents of this tutorial, we do not require participants to have prior knowledge in HAR or deep learning techniques. Participants are be able to follow along the content of the tutorial through a GitHub page. The tutorial is structured into three main phases. The first part will function as an introduction to the tutorial, the research field of human activity recognition as well as the structure of the tutorial. Next, the second part, will introduce the DL-ARC through a mix of theoretical and hands-on coding exercises. Lastly, the third part, will demonstrate next possible research steps by introducing advances within the deep learning community, which though applied in different research fields (e.g. computer vision) hold the potential to improve the predictive performance of the pipeline.

In the following, you find a compiled list of all questions which will be answered within each phase:

### Introduction

- Why this tutorial? What is its goal? What can participants expect?
- How is the GitHub page of this tutorial structured?
- What is Human Activity Recognition? Where does it find its applications? How was it approached in the past?
- What are advantages of deep learning based approaches compared to classical approaches?
- What are sample deep learning architectures for HAR? What is the DeepConvLSTM?

### The DL-ARC pipeline

#### Data collection and data analysis.

- How is data collection usually performed in the context of HAR?
- How does one typically analyse HAR datasets to get a better intuition of the use case at hand?
- What is the RealWorld HAR (RWHAR) dataset [42]?

#### Preprocessing.

- What are common issues when dealing with sensor datasets?
- How does one deal with missing data in a sensor dataset?
- How does one deal with varying sampling rates and sensitives of sensors? What is resampling? What is scaling/ normalization?
- What is the sliding window approach? Why do we need it?

#### Network architecture and training.

- What is deep learning? Of what parts does a typical (deep learning) training loop consist of?
- How to assess the predictive performance of a trained classification model? What are common metrics?
- What is the DeepConvLSTM [34]? What are the main parts of the architecture and what are their purpose?
- How does one train a sample deep learning model using our GitHub repository?

#### Validation and testing.

- Why do we need validation and testing? What is overfitting?
- Which different validation methods are typically used within the field of HAR?
- What is hypertuning? How should it be applied?

<!-- page: 3 -->

Tutorial on Deep Learning for Human Activity Recognition

### Next research steps

- What are examples of recent advances in the field of deep learning for computer vision?
- Can their advantageous behavior carry over to HAR and lead to an improved predictive performance of the classification network?

## 3 RELATED WORK

Recent advances in human activity recognition has empowered further development in fields like medical computer science [21, 22], industrial manufacturing [12, 24], smart environments [8, 26] and sports analysis [23, 28]. However, some of the important basics as introduced in [2], on which much research in this area has built on, are not state of the art anymore. At the latest since deep learning has found its way into activity recognition, the standards of former algorithms are often no longer completely applicable.

Feature engineering, as known from classical machine learning approaches, is no longer necessary since [14] showed that raw sensor data can be processed by using deep neural networks, even though, recent publications like [3] show that it can be beneficial when it comes to specific domains and circumstances or when using specific architectures of neural networks [6]. In classical machine learning, however, statistics of the first order are mostly used (mean, variance, median values, etc.). Unlike, when feature engineering is applied in the context of deep learning, the calculated features are usually of higher order.

New technologies, such as transfer learning [5, 10, 19, 36], data augmentation [18, 27, 38] and active learning [20], but also the constant search for more efficient network architectures [9, 31, 34] are becoming an important part in the human activity recognition community and are therefore constantly driving research in the field of deep learning. Two types of human activity recognition can be distinguished: (1) video data based, e.g. [44] and [39] and (2) inertial sensor data based activity recognition. An inertial sensor consists of at least an accelerometer and a gyroscope, but is often supplemented by a magnetometer. These datasets recorded with such sensors can be further enriched with additional information by additional sensor technology, such as temperature or light sensors. Combining an accelerometer and gyroscope alone can already significantly improve the classification results of machine learning models [13].

Therefore, current scientific research also focuses on fusion techniques for multimodal datasets, e.g. [29] and [32], or developing network architectures that are capable to handle both input types of data [16, 43]. However, algorithms from computer graphics and computer vision or even language processing often serve as inspiration, which are then transferred to sensor data-based human activity recognition. This results in a gap between both deep learning disciplines, in which the state of the art of the sensor-based human activity recognition mostly lacks behind the computer vision.

Nevertheless, the number of publications related to these topics increased constantly throughout the years (see [17] and [37] for an overview), but the focus on important fundamentals seems to be lost. These issues include that some works are difficult to reproduce as they lack open source code, focus on very specific aspects and/ or do not generalize well beyond the data set they have been developed on.

## 4 FORMAT AND DETAILED SCHEDULE

This tutorial was originally designed to be a full-day tutorial, taking about 6 hours plus breaks to work through. Given this limited timeframe we presented participants a less extensive version of the tutorial and left certain parts as take-home assignments. Nevertheless, our GitHub page contains all necessary information and hints so that participants can repeat all contents of the tutorial at any point in the future. The GitHub page guides participants through a mix of theoretical and hands-on exercise sessions. The two types of sessions will be either provided in the form of information directly displayed on the website via a slide show presentation or via Jupyter notebooks accessed through Google Colab[^2] .

Within their tutorial, Bulling et al. [2] introduced the ARC. With our tutorial we reworked the ARC to be suited for deep learning and propose a new version of it called the DL-ARC. As previously mentioned we structured the tutorial into three main phases.

**Introduction** The first phase gives an overview of the tutorial and an introduction to human activity recognition (HAR) and deep learning. We start by explaining the purpose of the tutorial, how it compares to the work of Bulling et al. [2], and what they can expect to learn within the next hours, as well as introduce our GitHub page which contains all the content covered within the tutorial. Afterwards, we will have a longer session where we will cover necessary theoretical knowledge. We will first answer basic questions like what HAR is and how it was approached in the past. To do so, we will sketch a timeline which will give participants a brief understanding how the area of HAR developed over the years. Next, we will go over explaining basic concepts of deep learning and where its advantages lie compared to classical (Machine Learning) approaches. We will then extend the timeline previously sketched with the influence of deep learning on the field of HAR, highlighting the most important studies conducted in the field, which demonstrated the effectiveness and applicability of deep learning for HAR, as well as other notable milestones in the other fields.

With the brief introduction of related work within the field of deep learning for HAR, we will also introduce the sample neural network architecture which participants will use throughout the tutorial, namely the DeepConvLSTM [34]. The DeepConvLSTM still remains one of the most popular and effective architectures in the field and was thus chosen by us to be architecture of choice. Nevertheless, in later steps of the tutorial, we will also demonstrate participants the modularity of the DL-ARC by showing how one would interchange the architecture to be applied by the pipeline.

**The DL-ARC pipeline** The second phase introduces participants to the DL-ARC pipeline. Using a mix of theoretical session and hands-on coding exercises, participants are guided step-by-step through each of the four main parts which the pipeline consists of. The hands-on exercises are presented as Jupyter notebooks, which can be accessed by the participants through Google Colab or locally on their workstation (see Figure 2). We recommend participants to use former as Google Colab already offers a working Python distribution as well as access to GPU resources, and therefore requires no setup effort in order to run our code.

[^2]: See https://colab.research.google.com

<!-- page: 4 -->

Bock, Hölzemann, et al.

[FIGURE: Figure 2. Screenshot of one of the interactive Colab pages]

Figure 2: A screenshot of one of the interactive Colab pages, where blocks of python code explain basic steps in Jupyter notebooks, for instance for visualization, accompanied by text blocks providing background explanations.

*Data collection and analysis.* Within the first step of the DL-ARC pipeline we give a brief overview of challenges faced with when collecting a sensor-based (HAR) dataset. We briefly discuss the different ways of collecting sensor-based data as well as challenges one faces when collecting a dataset. We further explain how accelerometers work as well as explain fundamental terms like sampling rate, interval and range. Afterwards we introduce the dataset which is used throughout the tutorial, namely the RealWorld HAR (RWHAR) dataset [42]. The dataset contains data of 15 participants performing 8 different activities (walking upstairs, walking downstairs, jumping, lying, standing, sitting, running, walking). To account for the limited timeframe of the tutorial, we will have participants use a smaller version of the dataset in order to have shorter training times. Within the first coding exercise participants are then asked to familiarise themselves with how one can load the RWHAR dataset as well as apply sample data analysis steps. This includes ways to analyse the activities performed in the dataset (e.g. average length, label distribution) and visualization techniques of the sensor streams.

*Preprocessing.* Within the second part of the DL-ARC pipeline participants are taught everything related to preprocessing HAR datasets. In order to do so we first name frequent issues that arise when dealing with sensor-based datasets like missing values, different sampling rates and sensitivities and then name sample methods which can be used to solve said problems, namely interpolation, resampling and scaling. Furthermore, we go into detail why it is necessary to segment sensor-data into sliding windows. To conclude the chapter the related coding exercise then asks participants to apply said preprocessing methods as well as also highlights pitfalls that frequently arise when applying them.

*Network architecture and training.* The third part functions as an introduction to deep learning and teach participants fundamental terms and concepts surrounding it. Before talking about which parts a deep learning training loop consists of we clarify what the term deep learning actually means. Moreover, this part also covers sample evaluation metrics that can be applied to judge the predictive performance of a classifier. Though it was not covered in the initial version of this tutorial, we offer participants to work through a separate, additional Jupyter notebook, which goes into more detail about how these metrics are computed using a toy classification example. We then talk about the types of layers one can find in a sample deep learning as well as their purpose and function, and introduce a the architecture which is used during the tutorial, namely an altered version of the DeepConvLSTM [34], which was introduced in recent publication of ours [1]. During the coding exercise related to his chapter participants are asked to implement the architecture introduced to them using PyTorch as well as write a sample training loop.

*Validation and testing.* Within the last part of introducing the DL-ARC pipeline, participants are taught about the importance of validation and testing. The fundamental pitfall that is overfitting is explained as well as shown how to be avoided via three sample validation methods, namely train-validation splits, k-fold and cross-participant cross-validation and stressing the necessity of testing. Additionally, we briefly speak about hypertuning and how it should be approached as well as partly "automatized" by using frameworks like the BOHB framework [7]. To conclude the second phase, as part of the coding exercise, participants work on implementing the validation methods themselves and test their trained networks.

**Next research steps** After demonstrating the fundamentals of the DL-ARC, the last part of the tutorial presents some opportunities of future research by exploiting some exemplary advances in the field of deep learning. The goal of this part is to give some inspiration for extending the DL-ARC in order to possibly improve results. We discuss two computer vision techniques, which - to the best of our knowledge - have not been exploited for HAR yet, namely improving generalization properties using MaxUp [11] and incorporating a level of uncertainty into the training by using label smoothing as proposed in [41] and, for instance, analyzed in [30]. While the limited time of the tutorial did not allow to implement advanced techniques live, we hope to inspire participants to conduct research on HAR network architectures and training schemes with the motivation to beat the preliminary results they obtained in our tutorial. To foster such research we provide additional resources, references and a coding exercise surrounding the discussed techniques in the form of a final Jupyter notebook. All in all, we hope that this lays the foundation for participants to utilize, test and extend all the material provided during the tutorial far beyond the day of the tutorial.

## 5 SUPPORT MATERIALS

Participants are only required to bring their own laptop to the tutorial. As training a neural networks requires GPU resources we recommend participants to use Google Colab, which is tightly integrated with GitHub. The tutorial's presentation slides, which contain links to all Colab websites with Jupyter Notebooks, can be accessed via:
https://mariusbock.github.io/dl-for-har

<!-- page: 5 -->

Tutorial on Deep Learning for Human Activity Recognition

## REFERENCES

[1] Marius Bock, Alexander Hölzemann, Michael Moeller, and Kristof Van Laerhoven. 2021. Improving Deep Learning for HAR with Shallow LSTMs. In International Symposium on Wearable Computers (ISWC '21). 7–12. https://doi.org/10.1145/3460421.3480419

[2] Andreas Bulling, Ulf Blanke, and Bernt Schiele. 2014. A Tutorial on Human Activity Recognition Using Body-Worn Inertial Sensors. Comput. Surveys 46, 3 (2014). https://doi.org/10.1145/2499621

[3] Jingcheng Chen, Yining Sun, and Shaoming Sun. 2021. Improving Human Activity Recognition Performance by Data Fusion and Feature Engineering. Sensors 21, 3 (2021). https://doi.org/10.3390/s21030692

[4] Ronan Collobert, Jason Weston, Léon Bottou, Michael Karlen, Koray Kavukcuoglu, and Pavel Kuksa. 2011. Natural Language Processing (Almost) From Scratch. Journal of Machine Learning Research 12, 76 (2011), 2493–2537. http://jmlr.org/papers/v12/collobert11a.html

[5] Xin Du, Katayoun Farrahi, and Mahesan Niranjan. 2019. Transfer Learning Across Human Activities Using a Cascade Neural Network Architecture. In Proceedings of the 23rd International Symposium on Wearable Computers (ISWC '19). 35–44. https://doi.org/10.1145/3341163.3347730

[6] Maciej Dzieżyc, Martin Gjoreski, Przemysław Kazienko, Stanisław Saganowski, and Matjaž Gams. 2020. Can We Ditch Feature Engineering? End-to-End Deep Learning for Affect Recognition from Physiological Sensor Data. Sensors 20, 22 (2020). https://doi.org/10.3390/s20226535

[7] Stefan Falkner, Aaron Klein, and Frank Hutter. 2018. BOHB: Robust and Efficient Hyperparameter Optimization at Scale. In Proceedings of the 35th International Conference on Machine Learning, Vol. 80. PMLR, 1437–1446. http://proceedings.mlr.press/v80/falkner18a.html

[8] Ekaterina Gilman, Satu Tamminen, Rumana Yasmin, Eemeli Ristimella, Ella Peltonen, Markus Harju, Lauri Lovén, Jukka Riekki, and Susanna Pirttikangas. 2020. Internet of Things for Smart Spaces: A University Campus Case Study. Sensors 20, 13 (2020). https://doi.org/10.3390/s20133716

[9] Martin Gjoreski, Vito Janko, Gašper Slapničar, Miha Mlakar, Nina Reščič, Jani Bizjak, Vid Drobnič, Matej Marinko, Nejc Mlakar, Mitja Luštrek, and others. 2020. Classical and Deep Learning Methods for Recognizing Human Activities and Modes of Transportation With Smartphone Sensors. Information Fusion 62 (2020), 47–62. https://doi.org/10.1016/j.inffus.2020.04.004

[10] Martin Gjoreski, Stefan Kalabakov, Mitja Luštrek, Matjaž Gams, and Hristijan Gjoreski. 2019. Cross-Dataset Deep Transfer Learning for Activity Recognition. In Adjunct Proceedings of the 2019 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2019 ACM International Symposium on Wearable Computers. Academic Press, 714–718. https://doi.org/10.1145/3341162.3344865

[11] Chengyue Gong, Tongzheng Ren, Mao Ye, and Qiang Liu. 2021. MaxUp: Lightweight Adversarial Training With Data Augmentation Improves Neural Network Training. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2474–2483.

[12] Rene Grzeszick, Jan Marius Lenk, Fernando Moya Rueda, Gernot A Fink, Sascha Feldhorst, and Michael ten Hompel. 2017. Deep Neural Network Based Human Activity Recognition for the Order Picking Process. In Proceedings of the 4th International Workshop on Sensor-Based Activity Recognition and Interaction (iWOAR '17). 1–6. https://doi.org/10.1145/3134230.3134231

[13] Haodong Guo, Ling Chen, Liangying Peng, and Gencai Chen. 2016. Wearable Sensor Based Multimodal Human Activity Recognition Exploiting the Diversity of Classifier Ensemble. In Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing (UbiComp '16). 1112–1123. https://doi.org/10.1145/2971648.2971708

[14] Nils Hammerla, James Fisher, Peter Andras, Lynn Rochester, Richard Walker, and Thomas Ploetz. 2015. PD Disease State Assessment in Naturalistic Environments Using Deep Learning. Proceedings of the AAAI Conference on Artificial Intelligence 29, 1 (2015). https://ojs.aaai.org/index.php/AAAI/article/view/9484

[15] Nils Y. Hammerla, Shane Halloran, and Thomas Ploetz. 2016. Deep, Convolutional, and Recurrent Models for Human Activity Recognition using Wearables. In Proceedings of the 25th International Joint Conference on Artificial Intelligence. 1533–1540. http://www.ijcai.org/Proceedings/16/Papers/220.pdf

[16] Roberto Henschel, Timo Von Marcard, and Bodo Rosenhahn. 2020. Accurate Long-Term Multiple People Tracking Using Video and Body-Worn Imus. IEEE Transactions on Image Processing 29 (2020), 8476–8489. https://doi.org/10.1109/TIP.2020.3013801

[17] Netzahualcoyotl Hernandez, Jens Lundström, Jesus Favela, Ian McChesney, and Bert Arnrich. 2020. Literature Review on Transfer Learning for Human Activity Recognition Using Mobile and Wearable Devices with Environmental Technology. SN Computer Science 1, 2 (2020), 66. https://doi.org/10.1007/s42979-020-0070-4

[18] Alexander Hoelzemann, Nimish Sorathiya, and Kristof Van Laerhoven. 2021. Data Augmentation Strategies for Human Activity Data Using Generative Adversarial Neural Networks. In IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops). 8–13. https://doi.org/10.1109/PerComWorkshops51409.2021.9431046

[19] Alexander Hoelzemann and Kristof Van Laerhoven. 2020. Digging Deeper: Towards a Better Understanding of Transfer Learning for Human Activity Recognition (ISWC '20). 50–54. https://doi.org/10.1145/3410531.3414311

[20] Enamul Hoque and John Stankovic. 2012. AALO: Activity Recognition in Smart Homes Using Active Learning in the Presence of Overlapped Activities. In 6th International Conference on Pervasive Computing Technologies for Healthcare and Workshops (PervasiveHealth). 139–146. https://doi.org/10.4108/icst.pervasivehealth.2012.248600

[21] Koyu Hori, Yufeng Mao, Yumi Ono, Hiroki Ora, Yuki Hirobe, Hiroyuki Sawada, Akira Inaba, Satoshi Orimo, and Yoshihiro Miyake. 2020. Inertial Measurement Unit-Based Estimation of Foot Trajectory for Clinical Gait Analysis. Frontiers in Physiology 10 (2020), 1530. https://doi.org/10.3389/fphys.2019.01530

[22] Fabian Horst, Djordje Slijepcevic, Sebastian Lapuschkin, Anna-Maria Raberger, Matthias Zeppelzauer, Wojciech Samek, Christian Breiteneder, Wolfgang I Schöllhorn, and Brian Horsak. 2019. On the Understanding and Interpretation of Machine Learning Predictions in Clinical Gait Analysis Using Explainable Artificial Intelligence. (2019). https://arxiv.org/pdf/1912.07737.pdf

[23] Alexander Hölzemann and Kristof Van Laerhoven. 2018. Using Wrist-Worn Activity Recognition for Basketball Game Analysis. In Proceedings of the 5th international Workshop on Sensor-based Activity Recognition and Interaction (iWOAR '18). 1–6. https://doi.org/10.1145/3266157.3266217

[24] Heli Koskimaki, Ville Huikari, Pekka Siirtola, Perttu Laurinen, and Juha Roning. 2009. Activity recognition using a wrist-worn inertial measurement unit: A case study for industrial assembly lines. In 17th Mediterranean Conference on Control and Automation. 401–405. https://doi.org/10.1109/MED.2009.5164574

[25] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. 2012. ImageNet Classification with Deep Convolutional Neural Networks. Proceedings of the 25th International Conference on Neural Information Processing Systems 1 (2012), 1097–1105. https://dl.acm.org/doi/10.5555/2999134.2999257

[26] Uwe Köckemann, Marjan Alirezaie, Jennifer Renoux, Nicolas Tsiftes, Mobyen Uddin Ahmed, Daniel Morberg, Maria Lindén, and Amy Loutfi. 2020. Open-Source Data Collection and Data Sets for Activity Recognition in Smart Homes. Sensors 20, 3 (2020). https://doi.org/10.3390/s20030879

[27] Xi'ang Li, Jinqi Luo, and Rabih Younes. 2020. ActivityGAN: Generative adversarial networks for data augmentation in sensor-based human activity recognition. In Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers (UbiComp-ISWC '20). 249–254. https://doi.org/10.1145/3410530.3414367

[28] Chunyan Ma, Ji Fan, Jinghao Yao, and Tao Zhang. 2021. NPU RGBD Dataset and a Feature-Enhanced LSTM-DGCN Method for Action Recognition of Basketball Players+. Applied Sciences 11, 10 (2021). https://doi.org/10.3390/app11104426

[29] James Male and Uriel Martinez-Hernandez. 2021. Recognition of human activity and the state of an assembly task using vision and inertial sensor fusion methods. In 22nd IEEE International Conference on Industrial Technology (ICIT, Vol. 1). 919–924. https://doi.org/10.1109/ICIT46573.2021.9453672

[30] Rafael Müller, Simon Kornblith, and Geoffrey E Hinton. 2019. When does label smoothing help?. In Advances in Neural Information Processing Systems, H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett (Eds.), Vol. 32. Curran Associates, Inc.

[31] Vishvak S. Murahari and Thomas Plötz. 2018. On Attention Models for Human Activity Recognition. In Proceedings of the 2018 ACM International Symposium on Wearable Computers (ISWC '18). 100–103. https://doi.org/10.1145/3267242.3267287

[32] Sebastian Münzner, Philip Schmidt, Attila Reiss, Michael Hanselmann, Rainer Stiefelhagen, and Robert Dürichen. 2017. CNN-Based Sensor Fusion Techniques for Multimodal Human Activity Recognition. In Proceedings of the 2017 ACM International Symposium on Wearable Computers (ISWC '17). 158–165. https://doi.org/10.1145/3123021.3123046

[33] Maryam M. Najafabadi, Flavio Villanustre, Taghi M. Khoshgoftaar, Naeem Seliya, Randall Wald, and Edin Muharemagic. 2015. Deep Learning Applications and Challenges in Big Data Analytics. Journal of Big Data 2, 1 (2015). https://doi.org/10.1186/s40537-014-0007-7

[34] Francisco Javier Ordóñez and Daniel Roggen. 2016. Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable Activity Recognition. Sensors 16, 1 (2016). https://doi.org/10.3390/s16010115

[35] Samira Pouyanfar, Saad Sadiq, Yilin Yan, Haiman Tian, Yudong Tao, Maria P. Reyes, Mei-Ling Shyu, Shu-Ching Chen, and Sundaraja S. Iyengar. 2018. A Survey on Deep Learning: Algorithms, Techniques, and Applications. Comput. Surveys 51, 5 (2018). https://doi.org/10.1145/3234150

[36] Xin Qin, Yiqiang Chen, Jindong Wang, and Chaohui Yu. 2019. Cross-Dataset Activity Recognition via Adaptive Spatial-Temporal Transfer Learning. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 3, 4 (2019), 1–25. https://doi.org/10.1145/3369818

[37] Alen Rajšp and Iztok Fister. 2020. A Systematic Literature Review of Intelligent Data Analysis Methods for Smart Sport Training. Applied Sciences 10, 9 (2020). http://dx.doi.org/10.3390/app10093013

<!-- page: 6 -->

Bock, Hölzemann, et al.

[38] Khandakar M Rashid and Joseph Louis. 2019. Times-Series Data Augmentation and Deep Learning for Construction Equipment Activity Recognition. Advanced Engineering Informatics 42 (2019). https://doi.org/10.1016/j.aei.2019.100944

[39] Yaser Souri, Mohsen Fayyaz, Luca Minciullo, Gianpiero Francesca, and Juergen Gall. 2021. Fast Weakly Supervised Action Segmentation Using Mutual Consistency. IEEE Transactions on Pattern Analysis and Machine Intelligence (2021). https://doi.org/10.1109/TPAMI.2021.3089127

[40] Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott E. Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, and Andrew Rabinovich. 2015. Going Deeper with Convolutions. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). https://doi.org/10.1109/CVPR.2015.7298594

[41] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jon Shlens, and Zbigniew Wojna. 2016. Rethinking the Inception Architecture for Computer Vision. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2818–2826. https://doi.org/10.1109/CVPR.2016.308

[42] Timo Sztyler and Heiner Stuckenschmidt. 2016. On-Body Localization of Wearable Devices: An Investigation of Position-Aware Activity Recognition. In IEEE International Conference on Pervasive Computing and Communications. 1–9. https://doi.org/10.1109/PERCOM.2016.7456521

[43] M Trumble, A Gilbert, C Malleson, A Hilton, and J Collomosse. 2017. Total Capture: 3D Human Pose Estimation Fusing Video and Inertial Sensors (BMVC, Vol. 2).

[44] Sijie Yan, Yuanjun Xiong, and Dahua Lin. 2018. Spatial temporal graph convolutional networks for skeleton-based action recognition. In 32nd AAAI Conference on Artificial Intelligence (AAAI18).
