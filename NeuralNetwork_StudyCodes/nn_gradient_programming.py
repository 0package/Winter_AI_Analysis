#Jen 8th, 2025
# Neural Network - Gradient descent
#경사하강법: 오류함수의 접선의 기울기를 줄여나가며 오류가 최저가 되는 점을 찾는 방법

import numpy as np
import matplotlib.pyplot as plt

x = 10
learning_rate = 0.01    #학습률
precision = 0.00001     #정확도
max_iterations = 100    #최대 반복 횟수

#손실 함수를 람다식으로 정의한다.
loss_func = lambda x: (x-3)**2 + 10

#그래디언트를 람다식으로 정의한다. 손실 함수의 1차 미분값이다.
gradient = lambda x: 2*x-6

y = []
#그래디언트 강하법
for i in range(max_iterations):
    x = x - learning_rate * gradient(x)
    y.append(x)
    print("손실 함수값(", x, ")=",loss_func(x))

print('최소값 =', x)

X = np.arange(0,100)
Y = np.array(y)

plt.plot(range(0,max_iterations), Y,'r')
plt.show()