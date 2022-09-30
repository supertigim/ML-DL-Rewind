import pytest 
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as SK_DT

from models.decision_tree import DecisionTree 
from utils import accuracy

def load_dataset():
    data = datasets.load_breast_cancer()
    X = data.data
    y = data.target 
    print(f"전체 데이터 shape: {X.shape}")
    print(f"Label 종류: {np.unique(y)}")  # 결과 : 0 아니면 1 
    return X, y

def evaluation_my_decision_tree():
    X, y = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=1234 )

    clf = SK_DT()
    #clf = DecisionTree(max_depth=10) # 0.9210526315789473
    clf.fit(X_train, y_train) 

    y_pred = clf.predict(X_test)
    acc = accuracy(y_test, y_pred)

    print(f"Decision Tree 모델 정확도 - {acc}")

@pytest.fixture
def datasets_for_pytest():
    return load_dataset()

def test_decision_tree_with_sklearn(datasets_for_pytest):
    X, y = datasets_for_pytest
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=1234 )

    clf = DecisionTree(max_depth=10) # 0.9210526315789473
    clf.fit(X_train, y_train) 

    y_pred = clf.predict(X_test)
    acc = accuracy(y_test, y_pred)
    assert  acc > 0.9

    clf_sk = SK_DT()
    clf_sk.fit(X_train, y_train) 

    y_pred_sk = clf_sk.predict(X_test)
    assert accuracy(y_test, y_pred_sk) < acc


if __name__ == "__main__":
    evaluation_my_decision_tree()
