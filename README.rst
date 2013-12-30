tmlknn
======

Threshold Multi-Label k Nearest Neighbours is a multi label classification algorithm described in [1]_. It is a modification of MLkNN classification algorithm [2]_. It has been shown on several benchmarks how TMLKNN achieves better results than MLKNN in terms of a few classification measures, while keeping the same time and space complexities [3]_.

The implementation is based on Orange framework [4]_ (version: Orange2.6a2) in Python2.7. 

ThreshMLkNNLearner and ThreshMLkNNClassifier correspond to MLkNNLearner and MLkNNClassifier and implement the same interfaces except for the constructor of ThreshMLkNNLearner requiring additional parameter: a function calculating a classification measure based on FN, TN, TP, FP.

.. [1] Michal Lukasik, Tomasz Kusmierczyk, Lukasz Bolikowski, Hung Son Nguyen "Hierarchical, Multi-label Classification of Scholarly Publications: Modifications of ML-KNN Algorithm" Intelligent Tools for Building a Scientific Information Platform 2013: 343-363.
.. [2] Zhang, M. and Zhou, Z. 2007. "ML-KNN: A lazy learning approach to multi-label learning" Pattern Recogn. 40, 7 (Jul. 2007), 2038-2048.
.. [3] Michal Lukasik, Marcin Sydow: Threshold ML-KNN: Statistical Evaluation on Multiple Benchmarks. IIS 2013: 198-205.
.. [4] http://orange.biolab.si/
