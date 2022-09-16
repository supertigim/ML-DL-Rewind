from typing import Final
from numpy import ndarray as NDA
import numpy as np 

from models.base_regression import BaseRegression 

class LinearRegression(BaseRegression):
    def predict(self, X:NDA) -> NDA:
        return self._predict(X) 

    def _predict(self, X:NDA) -> NDA:
        y_predicted:NDA = np.dot(X, self.weights) + self.bias
        return y_predicted 