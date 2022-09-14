from typing import Final

from numpy import ndarray as NDA
import numpy as np 

class LinearRegression:
    def __init__(self, lr:float=0.001, n_iters:int=1000) -> None:
        self.lr:Final[float] = lr  
        self.n_iters:Final[int] = n_iters
        self.weights:NDA = None
        self.bias:np.float64 = None 

    def fit(self, X:NDA, y:NDA) -> None:
        # 초기화 
        n_samples, n_features = X.shape 
        self.weights = np.zeros(n_features)
        self.bias = 0 

        # print('shape of X: ', X.shape)
        # print('shape of self.weights: ', self.weights.shape)

        # 학습한당
        for _ in range(self.n_iters):
            y_predicted = self.predict(X)

            dw:NDA = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db:np.float64 = (1/n_samples) * np.sum(y_predicted-y)

            self.weights -= self.lr * dw 
            self.bias -= self.lr * db  

    def predict(self, X:NDA) -> NDA:
        y_predicted:NDA = np.dot(X, self.weights) + self.bias
        #print('shape of y_predicted: ', y_predicted.shape)
        return y_predicted 