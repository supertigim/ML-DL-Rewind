from typing import TypeVar, List
from numpy.typing import NDArray
from dataclasses import dataclass
import numpy as np
from collections import Counter

from utils import entropy


T = TypeVar('T', bound='TreeNode')
@dataclass
class TreeNode:
    feature: int = None      # 노드에 해당하는 피처(컬럼) 인덱스
    threshold: float = None  # 분기를 결정하는 값 피처(컬럼)에서 하나의 값
    left: T = None           # 왼쪽 노드
    right: T = None          # 오른쪽 노드 
    value: int = -1          # label 

    def is_leaf_node(self):
        return self.value != -1


class DecisionTree:

    def __init__(self,                      \
            min_samples_split:int = 2,      \
            max_depth:int = 100,            \
            n_feats:NDArray = None) -> None:
        self.min_samples_split:int  = min_samples_split
        self.max_depth:int          = max_depth
        self.n_feats:NDArray        = n_feats
        self.root:TreeNode          = None

    def fit(self, X:NDArray, y:NDArray) -> None:
        self.n_feats = X.shape[1] if not self.n_feats else min(self.n_feats, X.shape[1])
        self.root = self.__grow_tree(X, y)

    def predict(self, X:NDArray) -> NDArray:
        return np.array([self.__traverse_tree(x, self.root) for x in X])

    def __grow_tree(self, X:NDArray, y:NDArray, depth:int = 0) -> TreeNode:
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

        # stopping criteria
        if (depth >= self.max_depth
                or n_labels == 1
                or n_samples < self.min_samples_split):
            leaf_value = self.__most_common_label(y)
            return TreeNode(value=leaf_value)

        # n_features 크기의 NDArray를 0 부터 n_feats - 1까지 값으로 중복 없이 랜덤 입력
        feat_idxs = np.random.choice(n_features, self.n_feats, replace=False)

        # greedily select the best split according to information gain
        # best_feat 는 컬럼의 인덱스, best_thresh는 float 값 
        best_feat, best_thresh = self.__best_criteria(X, y, feat_idxs)
        
        # grow the children that result from the split
        left_idxs, right_idxs = self.__split(X[:, best_feat], best_thresh)
        left = self.__grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right = self.__grow_tree(X[right_idxs, :], y[right_idxs], depth+1)

        return TreeNode(best_feat, best_thresh, left, right)

    def __best_criteria(self, 
                X:NDArray, y:NDArray, 
                feat_idxs:List[int]) -> tuple[int, float]: # (index, threshold)
        best_gain = -1
        split_idx, split_thresh = None, None
        for feat_idx in feat_idxs:
            X_column = X[:, feat_idx]
            thresholds = np.unique(X_column)
            for threshold in thresholds:
                gain = self.__information_gain(y, X_column, threshold)

                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thresh = threshold

        return split_idx, split_thresh

    def __information_gain(self, y:NDArray, X_column:NDArray, split_thresh:float) -> float:
        # parent loss
        parent_entropy = entropy(y)

        # generate split
        left_idxs, right_idxs = self.__split(X_column, split_thresh)

        if len(left_idxs) == 0 or len(right_idxs) == 0:
            return 0

        # compute the weighted avg. of the loss for the children
        n = len(y)
        n_l, n_r = len(left_idxs), len(right_idxs)
        e_l, e_r = entropy(y[left_idxs]), entropy(y[right_idxs])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r

        # information gain is difference in loss before vs. after split
        ig = parent_entropy - child_entropy
        return ig

    def __split(self, X_column:NDArray, split_thresh:float) -> tuple[int, int]:
        left_idxs = np.argwhere(X_column <= split_thresh).flatten()
        right_idxs = np.argwhere(X_column > split_thresh).flatten()
        return left_idxs, right_idxs

    def __traverse_tree(self, x:NDArray, node:TreeNode) -> int:
        # Edge Case - 더이상 하위 TreeNode가 없는 Leaf 노드이면 (value 값이 존재하면)
        if node.is_leaf_node():
            return node.value

        # node(해당 Feature 또는 입력의 컬럼 하나)의 threshold로 분기 
        if x[node.feature] <= node.threshold:
            return self.__traverse_tree(x, node.left)
        return self.__traverse_tree(x, node.right)

    def __most_common_label(self, y:NDArray) -> int:
        counter = Counter(y)
        # counter.most_common(1)는 (최빈도 label 값, count 수) 반환
        most_common = counter.most_common(1)[0][0] 
        return most_common