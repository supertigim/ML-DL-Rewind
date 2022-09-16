import pytest 
import numpy as np

from sklearn.linear_model import LogisticRegression as SK_LR
from sklearn.model_selection import train_test_split
from sklearn import datasets

from models.logic_regression import LogisticRegression
from utils import accuracy

def breast_cancer_and_datasets():
    bc = datasets.load_breast_cancer()
    X, y = bc.data, bc.target
    return train_test_split(X, y, test_size=0.2, random_state=1234)

def logit_regression_accuracy_check():
    X_train, X_test, y_train, y_test = breast_cancer_and_datasets()

    regressor = LogisticRegression(lr=0.0001, n_iters=1000)
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)

    print("Logistic Regression classification accuracy:", accuracy(y_test, predictions))

    sk_l_regressor = SK_LR(solver='lbfgs', max_iter=3000)
    sk_l_regressor.fit(X_train, y_train)
    sk_l_predictions = sk_l_regressor.predict(X_test)
    print("SK Logistic Regression classification accuracy:", accuracy(y_test, sk_l_predictions))

@pytest.fixture
def breast_cancer_and_datasets_for_pytest():
    return breast_cancer_and_datasets()

def test_logistic_regression(breast_cancer_and_datasets_for_pytest):
    X_train, X_test, y_train, y_test = breast_cancer_and_datasets_for_pytest

    regressor = LogisticRegression(lr=0.0001, n_iters=1000)
    regressor.fit(X_train, y_train)
    predictions = regressor.predict(X_test)
    acc = accuracy(y_test, predictions)

    sk_l_regressor = SK_LR(solver='lbfgs', max_iter=3000)
    sk_l_regressor.fit(X_train, y_train)
    sk_l_predictions = sk_l_regressor.predict(X_test)
    sk_acc = accuracy(y_test, sk_l_predictions)

    # scikit-learn의 logit regressor와 비교 
    assert abs(sk_acc-acc) < 0.02

if __name__ == '__main__':
    logit_regression_accuracy_check() 