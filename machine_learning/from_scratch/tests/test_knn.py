import pytest 
import numpy as np
from sklearn import datasets 
from sklearn.model_selection import train_test_split 

from models.knn import KNN
from sklearn.neighbors import KNeighborsClassifier

def knn_model_and_datasets():
    # Data Preparation from scikit-learn
    iris = datasets.load_iris()
    X, y = iris.data, iris.target 
    return X, y, train_test_split(X, y, test_size=0.2, random_state=1234)

def iris_data_visualization():
    import matplotlib.pyplot as plt 
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    X, y, _ = knn_model_and_datasets()

    plt.figure()
    plt.scatter(X[:,0], X[:,1], c=y, cmap=cmap, edgecolors='k', s=20)
    plt.show()

@pytest.fixture
def knn_model_and_datasets_for_pytest():
    return knn_model_and_datasets()

def test_knn_model(knn_model_and_datasets_for_pytest):
    n_neighbors = 5

    _, _, (X_train, X_test, y_train, y_test) = knn_model_and_datasets_for_pytest

    my_knn = KNN(n_neighbors=n_neighbors)
    my_knn.fit(X_train, y_train)
    predictions = my_knn.predict(X_test)

    acc = np.sum(predictions == y_test) / len(y_test)
    #print(acc)

    assert acc > 0.95

def test_knn_compare(knn_model_and_datasets_for_pytest):
    n_neighbors = 5

    _, _, (X_train, X_test, y_train, y_test) = knn_model_and_datasets_for_pytest

    my_knn = KNN(n_neighbors=n_neighbors)
    my_knn.fit(X_train, y_train)
    predictions_from_my_knn = my_knn.predict(X_test)
    acc_of_my_knn = np.sum(predictions_from_my_knn == y_test) / len(y_test)
    
    sklearn_knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    sklearn_knn.fit(X_train, y_train)
    predictions_of_sklearn_knn = sklearn_knn.predict(X_test)
    acc_of_sklearn_knn = np.sum(predictions_of_sklearn_knn == y_test) / len(y_test)
    #print(acc_of_my_knn)
    #print(acc_of_sklearn_knn)
    assert abs(acc_of_my_knn - acc_of_sklearn_knn) < 0.01

if __name__ == '__main__':
    iris_data_visualization()