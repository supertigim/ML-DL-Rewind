from typing import Final
from numpy.typing import NDArray

import numpy as np

from utils import sigmoid
from models.base_regression import BaseRegression 

class LogisticRegression(BaseRegression):
    def predict(self, X:NDArray) -> NDArray:
        y_predicted_cls = [1 if i > 0.5 else 0 for i in self._predict(X)]
        return np.array(y_predicted_cls)

    def _predict(self, X:NDArray) -> NDArray:
        linear_model = np.dot(X, self.weights) + self.bias
        return sigmoid(linear_model)