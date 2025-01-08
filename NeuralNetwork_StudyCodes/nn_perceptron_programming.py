#Jen 8th, 2025
# Neural Network - Programmming : Using Perception Library

from sklearn.linear_model import Perceptron # scikit-learn dsm 파이썬으로 구현한 머신러닝 확장 라이브러리로 다양한 API 제공

# sample & label
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [0, 0, 0, 1]

# Create Perceptron. tol: end condition. random_state: seed of randnum
clf = Perceptron(tol=1e-3, random_state=0)

# Learning
clf.fit(X,Y) # learning by data&label

# Test
print(clf.predict(X))

print('###############################################')
#Neural Network - Programming : Not Using Library. Implement Function

#Calculate Output of Neuron Function
def calculate(input):
    global weights          #전체 네트워크에서 가중치를 공유
    global bias             #전체 네트워크에서 바이어스를 공유
    activation = bias       #바이어스
    for i in range(2):      #입력신호 총합 계산
        activation += weights[i] * input[i]
        
    if activation >= 0.0:   #스텝 활성화 함수
        return 1.0
    else:
        return 0.0
    
#Learning Algorithm
def train_weights(X,Y, l_rate, n_epoch):     #l_rate: 학습률   n_epoch: 에포크
    global weights
    global bias
    for epoch in range(n_epoch):       #repetition epoch
        sum_error = 0.0
        for row, target in zip(X,Y):   #repetition dataset
            actual = calculate(row)    #calculate real output
            error = target - actual    #calculate error : target - actual
            bias = bias + l_rate*error
            sum_error += error**2      #calculate square of error
            
            for i in range(2):         #edit weights(change weights)  
                weights[i] = weights[i] + l_rate * error * row[i]
            
            print(weights, bias)
        print('에포크 번호=%d, 학습률=%.3f, 오류=%.3f' % (epoch, l_rate, sum_error))
    return weights

#AND 연산 학습 데이터셋, 샘플
#X = [[0,0],[0,1],[1,0],[1,1]]
#Y = [0,0,0,1]

# init weights&bias
weights = [0.0, 0.0]
bias = 0.0
l_rate = 0.1  #학습률
n_epoch = 5   #에포크 횟수
weights = train_weights(X,Y,l_rate,n_epoch)
print(weights, bias)
print(X, clf.predict(X))