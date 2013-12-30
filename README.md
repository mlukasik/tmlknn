tmlknn
======

Multi Label classification algorithm: Threshold Multi-Label k Nearest Neighbours.

TML-kNN Classification is a modification of MLkNN algorithm. 

The implementation is based on Orange framework for machine learning in Python.
Both ThreshMLkNNLearner and ThreshMLkNNClassifier correspond to
MLkNNLearner and MLkNNClassifier and implement the same interface
except for the constructor of ThreshMLkNNLearner requiring additional
parameter (a function calculating measure based on FN, TN, TP, FP).

The algorithm is implemented as described in:
Michal Lukasik, Tomasz Kusmierczyk, Lukasz Bolikowski, Hung Son Nguyen. 
"Hierarchical, Multi-label Classification of Scholarly Publications: 
Modifications of ML-KNN Algorithm"
Intelligent Tools for Building a Scientific Information Platform 2013: 343-363

Implementation based on Python2.7 and Orange2.6a2.
