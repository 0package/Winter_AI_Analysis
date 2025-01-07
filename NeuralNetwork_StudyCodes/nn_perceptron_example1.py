#Jen 7th, 2025
# Neural Network - Perceptron Example 1

import numpy as np
import matplotlib.pyplot as plt

features = [[1,2],[2,1],[3,-1],[2.5,1.5],[2,3],[3,2]]
labels = [-1,-1,-1,1,1,1]

mkr = {-1:"_",1:"+"}
lbl = {-1:"minus",1:"plus"}
clr = {-1:"red",1:"blue"}

X = np.array(features)     # numpy.array(배열, 데이터 타입)
Y = np.array(labels)

category = np.unique(Y)    # 중복제거

print(X)
print(Y)
print(category)

for i in category:
    plt.scatter(X[np.where(Y==i),0], X[np.where(Y==i),1], c=clr[i],marker=mkr[i], label=lbl[i])
    
plt.xlabel('x')
plt.ylabel('y')
plt.legend(fontsize=12, loc='upper left')  #legend position
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid()
plt.show()

def plot_xy(X,Y,a,b,c):
    if ( b ==0):
        print('no graph')
    else:
        x = np.linspace(-5,5,100)
        y =-(a/b)* x -(c/b)

        # plt.plot(x, y, '-r', label='ax + by + c = 0')
        
        plt.plot(x,y,'-r')
        plt.title('Graph of ax + by + c = 0')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        # plt.legend(loc='upper left')
        # plt.axis(option='on')
        plt.axhline(y=0,color='k')
        plt.axvline(x=0,color='k')
        
        for i in category:
            plt.scatter(X[np.where(Y==i),0], X[np.where(Y==i),1], c=clr[i], marker=mkr[i],label=lbl[i])
            
        plt.legend(fontsize=12, loc='upper left')   #legend position
        plt.grid()
        plt.show()
            

plot_xy(X, Y, 1, 1, 1)