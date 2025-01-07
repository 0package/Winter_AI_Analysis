#Jen 7th, 2025
# Neural Network - Submission 2 : Artificial Inteligence Perceptron

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[0,0], [1,0], [0,1], [1,1]])
Y = np.array([-1,1,1,1])

plt.scatter(X[0][0], X[0][1], c='red')
plt.scatter(X[1][0], X[1][1], c='blue')
plt.scatter(X[2][0], X[2][1], c='blue')
plt.scatter(X[3][0], X[3][1], c='blue')
plt.show()

w = np.array([1. , 1. , 1.])  # [bias, w1, w2]

def forward(x):
    return np.dot(x, w[1:]) + w[0]    # numpy.dot : numpy array 곱하기 함수. 각 자리수끼리 곱하여 모두 더한 값을 반환

def predict(X):
    return np.where(forward(X) > 0, 1, -1)  # where(조건문 , 참일 때, 거짓일 때)

print("predict (before training)", w)

for epoch in range(50):
    for x_val, y_val in zip(X, Y):
        update = 0.01 * (y_val - predict(x_val))
        w[1:] += update * x_val
        w[0] += update

print("predict (after training)", w)