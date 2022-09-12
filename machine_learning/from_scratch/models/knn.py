from typing import Any, Callable

import numpy as np
from collections import Counter

def euclidean_distance(x1:np.ndarray, x2:np.ndarray) -> np.ndarray:
        return np.sqrt(np.sum((x1 - x2)**2))

class KNN:
    '''
        Classifier implementing the k-nearest neighbors vote.
    '''
    def __init__(self, n_neighbors:int = 3, measurer:Callable = euclidean_distance):
        self.n_neighbors = n_neighbors
        self.measurer = measurer

    def fit(self, X:np.ndarray, y:np.ndarray):
        self.X_train = X
        self.y_train = y

    def predict(self, X:np.ndarray) -> np.ndarray:
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x:np.ndarray) -> Any:
        # x와 트레이닝 데이터세의 모든 거리를 구한다. 
        distances = [self.measurer(x, x_train) for x_train in self.X_train]
        # 거리로 정렬 후, n_neighbors 수만큼 가까운 인덱스 모음
        k_idx = np.argsort(distances)[:self.n_neighbors]
        # 인덱스 리스트의 인덱스에 해당하는 y_train의 값
        k_neighbor_labels = [self.y_train[i] for i in k_idx]  
        # 최빈도 (레이블:카운트) 1개 반환 
        most_common = Counter(k_neighbor_labels).most_common(1)
        # 첫번째 Pair에서 레이블만 반환
        return most_common[0][0] 