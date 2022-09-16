from abc import ABCMeta, abstractmethod
from typing import Final
from numpy.typing import NDArray

import numpy as np

class BaseRegression(metaclass=ABCMeta):
    def __init__(self, lr:float=0.001, n_iters:int=1000) -> None:
        self.lr:Final[float] = lr
        self.n_iters:Final[int] = n_iters
        self.weights:NDArray = None
        self.bias:float = None

    def fit(self, X:NDArray, y:NDArray) -> None:
        # 초기화 
        n_samples, n_features = X.shape 
        self.weights = np.zeros(n_features)
        self.bias = 0 

        # 학습 
        for _ in range(self.n_iters):
            y_predicted = self._predict(X)
            # 경사 하강법 (by 선형대수)
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            # weight 업데이트 
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    @abstractmethod
    def predict(self, X:NDArray) -> NDArray:
        pass 

    @abstractmethod
    def _predict(self, X:NDArray) -> NDArray:
        pass 