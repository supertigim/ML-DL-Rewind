from typing import Final
from numpy.typing import NDArray
import numpy as np 

from models.base_regression import BaseRegression 

class LinearRegression(BaseRegression):
    def predict(self, X:NDArray) -> NDArray:
        return self._predict(X) 

    def _predict(self, X:NDArray) -> NDArray:
        y_predicted:NDArray = np.dot(X, self.weights) + self.bias
        return y_predicted 