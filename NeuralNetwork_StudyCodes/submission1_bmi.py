#Jen 7th, 2025
# Neural Network - Submission 1 : Design Health System - Calculate BMI & Show Graph of Obesity(body fat)

import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]   # 단위: m
weights = [86, 74, 59, 95, 80, 68]               # 단위: kg

np_heights = np.array(heights)
np_weights = np.array(weights)

np_bmi = np_weights/(np_heights**2)
for bmi in np_bmi:
    if bmi >= 30:
        print('2단계 비만')
    elif bmi >= 25:
        print('1단계 비만')
    elif bmi >= 23:
        print('위험체중')
    elif bmi >= 18.5:
        print('정상')
    else:
        print('저체중')

#print(bmi[bmi>25])
