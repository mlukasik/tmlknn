tmlknn
======

Threshold Multi-Label k Nearest Neighbours is a multi label classification algorithm described in [1]_. It is a modification of MLkNN classification algorithm [2]_. It has been shown on a several benchmarks how TMLKNN achieves better results in terms of a few classification measures than MLKNN, while keeping the same time and space complexities [3]_.

The implementation is based on Orange framework for machine learning [4]_. Both ThreshMLkNNLearner and ThreshMLkNNClassifier correspond to MLkNNLearner and MLkNNClassifier and implement the same interface except for the constructor of ThreshMLkNNLearner requiring additional parameter: a function calculating measure based on FN, TN, TP, FP.

Implementation is based on Python2.7 and Orange2.6a2.

.. [1] Michal Lukasik, Tomasz Kusmierczyk, Lukasz Bolikowski, Hung Son Nguyen "Hierarchical, Multi-label Classification of Scholarly Publications: Modifications of ML-KNN Algorithm" Intelligent Tools for Building a Scientific Information Platform 2013: 343-363.
.. [2] Zhang, M. and Zhou, Z. 2007. "ML-KNN: A lazy learning approach to multi-label learning" Pattern Recogn. 40, 7 (Jul. 2007), 2038-2048.
.. [3] Michal Lukasik, Marcin Sydow: Threshold ML-KNN: Statistical Evaluation on Multiple Benchmarks. IIS 2013: 198-205
.. [4] http://orange.biolab.si/
