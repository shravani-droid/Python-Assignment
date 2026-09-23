# Write a program that calculate Variance and standard deviation

import pandas as pd 
import numpy as np

data = [6,7,8,9,10,11,12]

mean = np.mean(data)

sum1 = 0

for i in data :
    sub = i - mean
    square = sub ** 2
    sum1 = square + sum1
    divide = sum1 / len(data)

print("Variance is : ",divide)
print("Standard Deviation is : ",np.sqrt(divide))