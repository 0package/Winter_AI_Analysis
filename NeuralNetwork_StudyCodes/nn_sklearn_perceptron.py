#Jen 7th, 2025
# Neural Network - Perceptron : Using sklearn package

from sklearn.linear_model import Perceptron

#샘플과 레이블
X = [[0,0],[0,1],[1,0],[1,1]]
Y = [0,0,0,1]

#퍼셉트론 생성. tol: 종료 조건 random_state: 난수 시드
clf = Perceptron(tol=1e-3, random_state=0)

#학습 수행
clf.fit(X,Y)

#테스트 수행
print(clf.predict(X))