import numpy as np
from sklearn import datasets 
from sklearn.model_selection import train_test_split 

from models.knn import KNN
from sklearn.neighbors import KNeighborsClassifier

# Data Preparation from scikit-learn
iris = datasets.load_iris()
X, y = iris.data, iris.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

def test_knn_model():
    n_neighbors = 5

    my_knn = KNN(n_neighbors=n_neighbors)
    my_knn.fit(X_train, y_train)
    predictions = my_knn.predict(X_test)

    acc = np.sum(predictions == y_test) / len(y_test)
    #print(acc)

    assert acc > 0.95

def test_knn_compare():
    n_neighbors = 5

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
    test_knn_model()
    test_knn_compare()