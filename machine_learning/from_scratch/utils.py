from numpy import ndarray as NDA
import numpy as np 

# Mean Square Error 
def mse(y_true:NDA, y_predicted:NDA) -> float:
    return np.mean((y_true-y_predicted)**2)

# sigmoid function 
def sigmoid(x:NDA) -> NDA:
    return 1 / (1 + np.exp(-x))

# measuring accuracy of logistic regression  
def accuracy(y_true:NDA, y_pred:NDA) -> float:
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy