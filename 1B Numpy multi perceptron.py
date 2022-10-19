#Import dari Library Numpy
import numpy as np

#Input Program dengan 10 layer
inputs = [1.23, 1.93, 1.46, 0.1, 0.2, 0.37, 1.4, 0.25, 1.3, 0.04]

#Weight Program dengan 5 neuron masing masing 10 layer
weights = [[0.25, 1.00, 2.37, 2.69, 2.46, 0.28, 0.73, 0.71, 0.15, 1.92],
		   [0.48, 1.93, 2.92, 2.52, 0.16, 1.79, 2.68, 2.27, 2.85, 1.32],
		   [0.98, 0.51, 2.86, 0.69, 2.19, 0.81, 2.23, 0.24, 2.81, 0.87],
           [0.53, 1.38, 2.97, 1.16, 1.92, 0.54, 2.40, 1.03, 2.21, 0.15],
           [2.69, 0.16, 1.28, 0.54, 1.50, 1.22, 0.94, 2.70, 1.45, 1.07]]

#Bias dari Program 5 layer
biases = [1.53, 0.80, 2.75, 0.71, 1.29]

#deklarasi dari bentuk program
layer_outputs = np.dot(weights, inputs) + biases
print(layer_outputs)