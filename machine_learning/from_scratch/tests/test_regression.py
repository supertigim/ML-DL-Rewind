from turtle import color
import numpy as np
from sklearn import datasets 
from sklearn.linear_model import LinearRegression as SK_LR
from sklearn.model_selection import train_test_split 

from models.linear_regression import LinearRegression 
from utils import mse

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
# print(X.shape)
# print(y.shape)

def data_visualization():
    import matplotlib.pyplot as plt 

    print(f'X: {X_train.shape}, {type(X_train)} | y: {y_train.shape}, {type(y_train)}')

    fig = plt.figure(figsize=(8,6))
    plt.scatter(X[:,0], y, color='b', marker='o', s=30)
    plt.show()

def prediction_visualization():
    import matplotlib.pyplot as plt

    regressor = LinearRegression(lr=0.01)
    regressor.fit(X_train, y_train)

    y_pred_line =  regressor.predict(X)

    cmap = plt.get_cmap('viridis')
    fig = plt.figure(figsize=(8,6))
    m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
    plt.plot(X, y_pred_line, color='black', linewidth=2, label='Prediction')
    plt.show()


def test_linear_regression():
    lr:np.float64 = 0.01
    regressor = LinearRegression(lr=lr)
    regressor.fit(X_train, y_train)
    predicted = regressor.predict(X_test)
    #print('shape of predicted: ', predicted.shape)
    mse_value = mse(y_test, predicted)
    #print('from scratch: ', mse_value)

    sk_l_regressor = SK_LR()
    sk_l_regressor.fit(X_train, y_train)
    sk_predicted = sk_l_regressor.predict(X_test)
    mse_value_sk = mse(y_test, sk_predicted)
    #print('from sklearn: ', mse_value_sk)
    assert abs(mse_value-mse_value_sk) < 0.01



if __name__ == '__main__':
    data_visualization()
    prediction_visualization()
