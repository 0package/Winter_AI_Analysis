#Jen 8th, 2025
# Neural Network - BackPropagation Algorithm Programming

import numpy as np

#시그모이드 함수
def actf(x):
    return 1/(1+np.exp(-x))   #numpy.exp() : 밑이 자연상수 e인 지수함수(e^x)로 변환. 결과값이 inf라면 무한대(infinite)라는 것

#시그모이드 함수의 미분값
def actf_deriv(x):
    return x*(1-x)

# XOR 연산을 위한 4행*2열의 입력 행렬
# 마지막 열은 바이어스를 나타냄
X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

# XOR 연산을 위한 4행*1열의 목표 행렬
Y = np.array([[0],[1],[1],[0]])
np.random.seed(5)
inputs = 3  # 입력층의 노드 개수
hiddens = 6 # 은닉층의 노드 개수
outputs = 1 # 출력층의 노드 개수

# 가중치를 -1.0에서 1.0 사이의 난수로 초기화
weight0 = 2*np.random.random((inputs, hiddens)) - 1
weight1 = 2*np.random.random((hiddens, outputs)) - 1

#반복
for i in range(10000):
    #순방향 계산
    layer0 = X                        #입력을 layer0에 대입
    net1 = np.dot(layer0, weight0)    #행렬의 곱 계산
    layer1 = actf(net1)               #활성화 함수 적용
    layer1[:,-1] = 1.0                #마지막 열은 바이어스를 나타냄. 1.0으로 만듦  #[:,-1]  : 모든행 중에, 마지막 행(-1)
    net2 = np.dot(layer1, weight1)    #행렬의 곱 계산
    layer2 = actf(net2)               #활성화 함수 적용
    
    #출력층에서 오차 계산
    layer2_error = layer2 - Y
    
    #출력층에서의 델타값 계산
    layer2_delta = layer2_error*actf_deriv(layer2)
    
    #은닉층에서의 오차 계산.  여기서 T는 행렬의 전치를 의미.
    #역방향으로 오차를 전파할 때는 반대방향이므로 행렬이 전치되어야 함.
    layer1_error = np.dot(layer2_delta, weight1.T)
    
    #은닉층에서의 델타 계산
    layer1_delta = layer1_error*actf_deriv(layer1)
    
    #은닉층 -> 출력층을 연결하는 가중치 수정
    weight1 += -0.2*np.dot(layer1.T, layer2_delta)
    
    #입력층 -> 은닉층을 연결하는 가중치 수정
    weight0 += -0.2*np.dot(layer0.T, layer1_delta)
    
    print(layer2)  #현재 출력층의 값을 출력  # 점점 목표값에 가까워 지는 것을 볼 수 있음음