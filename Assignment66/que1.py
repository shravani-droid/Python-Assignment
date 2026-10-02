# write a python  program to stimulate a single artificial neuron.
# input : x1=2
# x2 =3,
# w1 = 0.4,
# w2 = 0.6,
# bias = 0.5
# calculate weighted sum
# apply sigmoid activation function
# display final output
# explain whether the output is close to 0 or 1


import numpy as np
import math

def Sigmoid(z):
    return 1 / (1 + math.exp(-z))

def MarvellousFNN(inputs,weights,bias):
    print("Inputs are (x) : ",inputs)
    print("Weights are (w) :",weights)
    print("Bias are (b) : ",bias)

    z = 0
    for i in range(len(inputs)):
        z = z + (inputs[i] * weights[i])

    z = z + bias

    print("Weighted sum : ", z)

    y = Sigmoid(z)

    return y

def main():
    print("-------------- Neural Network -------------")

    inputs = [2,3]
    weights = [0.4,0.6]
    bias = 0.5

    result = MarvellousFNN(inputs,weights,bias)

    print("Predicted Result is : ", result)

    if result > 0.25:
        print("Result  is close to 1")
    else:
        print("Result is close to 0")

if __name__ == "__main__":
    main()