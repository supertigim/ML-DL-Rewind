import pytest 
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from models.naive_bayes import NaiveBayes

def iris_datasets():
    X, y = load_iris(return_X_y=True)
    return train_test_split(X, y, test_size=0.5, random_state=0)

def compare_naives():
    X_train, X_test, y_train, y_test = iris_datasets()

    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    print("[sklearn.GaussianNB] Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))

    my_model = NaiveBayes()
    my_model.fit(X_train, y_train)
    y_predicted_my_model = my_model.predict(X_test)
    print("[models.NaiveBayes] Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_predicted_my_model).sum()))
    # Number of mislabeled points out of a total 75 points : 4

@pytest.fixture
def iris_datasets_for_pytest():
    return iris_datasets()

def test_naive_bayes(iris_datasets_for_pytest):
    X_train, X_test, y_train, y_test = iris_datasets_for_pytest

    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)

    my_model = NaiveBayes()
    my_model.fit(X_train, y_train)
    y_predicted_my_model = my_model.predict(X_test)

    # scikit-learn의 logit regressor와 비교 
    assert (y_test != y_pred).sum() == (y_test != y_predicted_my_model).sum()

if __name__ == '__main__':
    compare_naives()



# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# X, y = load_iris(return_X_y=True)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
# gnb = GaussianNB()
# y_pred = gnb.fit(X_train, y_train).predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))

# from models.naive_bayes import NaiveBayes

# my_model = NaiveBayes()
# my_model.fit(X_train, y_train)
# y_predicted_my_model = my_model.predict(X_test)
# print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_predicted_my_model).sum()))

# # Number of mislabeled points out of a total 75 points : 4