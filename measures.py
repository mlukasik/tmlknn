'''
Created on Jan 20, 2013

@author: mlukasik
'''

def acc(FN, TN, TP, FP):
    """
    Returns: 
    accuracy measure
    """
    acc = 1.0*(TP+TN)/(TP+TN+FP+FN)
    return acc

def f1(FN, TN, TP, FP):
    """
    Returns: 
    f1 measure
    """
    P = 0
    if TP > 0:
        P = 1.0*TP/(TP+FP)
    
    R = 0
    if TP > 0:
        R = 1.0*TP/(TP+FN)
    f1 = 0
    if P > 0 and R > 0:
        f1 = 2.0*P*R/(P+R)
    return f1

def f1_acc(FN, TN, TP, FP):
    """
    Returns: 
    0.5 * f1measure + 0.5 * accuracy
    """
    acc = 1.0*(TP+TN)/(TP+TN+FP+FN)
    
    P = 0
    if TP > 0:
        P = 1.0*TP/(TP+FP)
    
    R = 0
    if TP > 0:
        R = 1.0*TP/(TP+FN)
    f1 = 0
    if P > 0 and R > 0:
        f1 = 2.0*P*R/(P+R)
    return 0.5*acc + 0.5*f1