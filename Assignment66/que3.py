# write a python program to calculate loss
# Task:
# Implement Mean Squared Error
# Implement Binary Cross Entropy
# Take actual and Predicted value
# Display the calcurted loss
# Explain which loss function is used for regression and classification

import numpy as np

def Marvellous_MSE(Y_True , Y_Pred):
    n = len(Y_Pred)
    total_error = 0

    for i in range(n):
        error = Y_True[i] - Y_Pred[i]
        total_error = total_error + (error ** 2)

    MSE = total_error / n
    return MSE

Y_True = [10,20,30,45,22,12]
Y_Pred = [4,12,22,40,8,11]

loss = Marvellous_MSE(Y_True,Y_Pred)

print("Loss is : ",loss)

def Marvellous_BCE(Y_True , Y_Pred):
    n = len(Y_Pred)
    total_error = 0
    
    for i in range(n):
        error = -np.mean(Y_True[i] * np.log(Y_Pred[i]) + (1 - Y_True[i]) * np.log(1 - Y_Pred[i]))
        total_error = total_error + error 

    BCE = total_error / n
    return BCE

Y_True = [1, 0, 1, 1, 0]
Y_Pred = [0.9, 0.2, 0.8, 0.7, 0.1]

loss = Marvellous_BCE(Y_True,Y_Pred)

print("BCE Loss is : ",loss)