from numpy.typing import NDArray

import numpy as np 

class SVM:

    def __init__(self, learning_rate:float=0.001, lambda_param:float=0.01, n_iters:int=1000) -> None:
        self.lr:float = learning_rate
        self.lambda_param:float = lambda_param
        self.n_iters:int = n_iters
        self.w:NDArray = None
        self.b:float = None

    def fit(self, X:NDArray, y:NDArray) -> None:
        _, n_features = X.shape
        
        y_ = np.where(y <= 0, -1, 1)
        
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                condition = y_[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_[idx]))
                    self.b -= self.lr * y_[idx]

    def predict(self, X:NDArray) -> NDArray:
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)