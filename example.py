'''
Created on Jan 20, 2013

@author: mlukasik
'''
import Orange
import tmlknn, measures

learners = [
    Orange.multilabel.MLkNNLearner(name="mlknn",k=5),
    tmlknn.ThreshMLkNNLearner(measure=measures.acc, name="threshmlknn",k=5),
    tmlknn.ThreshMLkNNLearner(measure=measures.f1, name="threshmlknn",k=5),
    tmlknn.ThreshMLkNNLearner(measure=measures.f1_acc, name="threshmlknn",k=5)
]

data = Orange.data.Table("emotions")

res = Orange.evaluation.testing.cross_validation(learners, data,2)
loss = Orange.evaluation.scoring.mlc_hamming_loss(res)
accuracy = Orange.evaluation.scoring.mlc_accuracy(res)
precision = Orange.evaluation.scoring.mlc_precision(res)
recall = Orange.evaluation.scoring.mlc_recall(res)
print 'classifiers=', map(lambda l: l.name, learners)
print 'loss=', loss
print 'accuracy=', accuracy
print 'precision=', precision
print 'recall=', recall