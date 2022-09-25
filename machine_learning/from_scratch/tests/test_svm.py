import pytest 
import numpy as np

from sklearn import datasets 
from sklearn.svm import SVC
    
from models.svm import SVM 

def load_dataset():
    X, y = datasets.make_blobs(n_samples=50, n_features=2, centers=2, cluster_std=1.05, random_state=40)
    y = np.where(y == 0, -1, 1) # 0이랑 같으면 -1, 아니면 1
    return X, y 

def compare_svm():
    X, y = load_dataset()
    
    my_clf = SVM() 
    sk_clf = SVC(kernel='linear')
    
    sk_clf.fit(X, y) 
    my_clf.fit(X, y) 

    # test 데이터 5개 생성 
    X_test, _ = datasets.make_blobs(n_samples=5, n_features=2, centers=2, cluster_std=1.05, random_state=40)

    print('X: ', X_test)
    print('sklearn: ',sk_clf.predict(X_test))
    print('my SVM: ',my_clf.predict(X_test)) 

def visualize_svm():
    import matplotlib.pyplot as plt 
    def get_hyperplane_value(x, w, b, offset):
        return (-w[0] * x + b + offset) / w[1]

    X, y = load_dataset()

    clf = SVM() 
    clf.fit(X, y) 
    
    fig = plt.figure() 
    ax = fig.add_subplot(1,1,1)
    plt.scatter(X[:,0], X[:,1], marker='o', c=y)

    x0_1 = np.amin(X[:,0])
    x0_2 = np.amax(X[:,0])

    x1_1 = get_hyperplane_value(x0_1, clf.w, clf.b, 0)
    x1_2 = get_hyperplane_value(x0_2, clf.w, clf.b, 0)

    x1_1_m = get_hyperplane_value(x0_1, clf.w, clf.b, -1)
    x1_2_m = get_hyperplane_value(x0_2, clf.w, clf.b, -1)

    x1_1_p = get_hyperplane_value(x0_1, clf.w, clf.b, 1)
    x1_2_p = get_hyperplane_value(x0_2, clf.w, clf.b, 1)

    ax.plot([x0_1, x0_2], [x1_1, x1_2], 'y--')
    ax.plot([x0_1, x0_2], [x1_1_m, x1_2_m], 'k')
    ax.plot([x0_1, x0_2], [x1_1_p, x1_2_p], 'k')

    x1_min = np.amin(X[:,1])
    x1_max = np.amax(X[:,1])
    ax.set_ylim([x1_min-3, x1_max+3])

    plt.show()

@pytest.fixture
def datasets_for_pytest():
    return load_dataset()

def test_naive_bayes(datasets_for_pytest):
    X, y = datasets_for_pytest

    my_clf = SVM() 
    sk_clf = SVC(kernel='linear')

    sk_clf.fit(X, y) 
    my_clf.fit(X, y) 

    # test 데이터 5개 생성 
    X_test, _ = datasets.make_blobs(n_samples=5, n_features=2, centers=2, cluster_std=1.05, random_state=40)
    assert all([a == b for a, b in zip(sk_clf.predict(X_test), my_clf.predict(X_test))])
    
if __name__ == '__main__':
    compare_svm() 
    visualize_svm()