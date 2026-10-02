# Write a python program to demonstrate different activation functoins.
# Functions to implemented:
#   Sigmoid
#   ReLU
#   Tanh
# Task :
#  1 Accept input values from -10 to 10
#  2 Plot all activation function using Matplotlib
#  3 Explain the use of each activation function



import tensorflow as tf
import matplotlib.pyplot as plt

border = "-" * 70

# Input values
x = tf.linspace(-10.0,10.0,100)

# Activation Functions
sigmoid = tf.sigmoid(x)
relu = tf.nn.relu(x)
tanh = tf.nn.tanh(x)

# Plots

plt.figure(figsize=(10,6))

plt.plot(x, sigmoid,label = "Sigmoid")
plt.plot(x, relu, label="ReLU")
plt.plot(x, tanh, label = "Tanh")

plt.xlabel("Input Values")
plt.ylabel("Activation output")
plt.title("Tensorflow Activation Function")
plt.grid(True)
plt.legend()

plt.show()

print(border)

print("Sigmoid: Output range  is 0 to 1 ")
print("ReLU : Negative values became 0, positive values remain unchanged")
print("Tanh : Output range is -1 to 1")

print(border)