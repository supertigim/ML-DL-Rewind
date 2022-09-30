from numpy.typing import NDArray
import numpy as np 

# Mean Square Error 
def mse(y_true:NDArray, y_predicted:NDArray) -> float:
    return np.mean((y_true-y_predicted)**2)

# sigmoid function 
def sigmoid(x:NDArray) -> NDArray:
    return 1 / (1 + np.exp(-x))

# measuring accuracy of logistic regression  
def accuracy(y_true:NDArray, y_pred:NDArray) -> float:
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

# Information entropy
def entropy(y:NDArray) -> NDArray:
    hist = np.bincount(y)
    ps = hist / len(y)
    return -np.sum([p * np.log2(p) for p in ps if p > 0])