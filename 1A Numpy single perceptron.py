#Import dari Library Numpy
import numpy as np

#Input Program dengan 10 layer
inputs = [1.21, 2.97, 3.07, 2.93, 4.32, 5.2, 6.1, 7.2, 5.3, 4.4]

#Weight Program dengan 10 layer
weights = [1.23, 1.93, 1.46, 0.1, 0.2, 0.37, 1.4, 0.25, 1.3, 0.04]

#Bias dari Program
bias = 2.99

#deklarasi dari bentuk program
outputs = np.dot(weights, inputs) + bias
print(outputs)