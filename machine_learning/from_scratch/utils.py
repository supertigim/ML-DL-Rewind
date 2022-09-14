from numpy import ndarray as NDA
import numpy as np 

# Mean Square Error 
def mse(y_true:NDA, y_predicted:NDA) -> float:
    return np.mean((y_true-y_predicted)**2)