# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


'''
inputs = [1,2,3,2.5]

weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]

biases = [2,3,0.5]

#using loops
layer_outputs = []   #output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 #output of a given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
    
print(layer_outputs)
'''
'''
#using dot product for a single neuron
inputs = [1,2,3,2.5]
weights = [0.2,0.8,-0.5,1.0]
bias = 2

output = np.dot(weights, inputs) + bias
#output = 0.2*1 + 0.8*2 + -0.5*3 + 1*2.5 + 2
print(output)
'''

#dot product with a layer of neurons
inputs = [1,2,3,2.5]


weights = [[0.2,0.8,-0.5,1.0],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]


biases = [2,3,0.5]

output = np.dot(weights, inputs) + biases
#same as 
#[np.dot(weights[0], inputs), np.dot(weights[1], inputs) , np.dot(weights[2], inputs)] + biases
#same as
#[2.8, -1.79, 1.885] + [2,3,0.5]
#same as
#[0.2*1 + 0.8*2 + -0.5*3 + 1*2.5 + 2,
#0.5*2 + -0.91*2 + 0.26*3 + -0.5*2.5 + 3,
#-0.26*1 + -0.27*2 + 0.17*3 + 0.87*2.5 + 0.5]

print(output) #[4.8,1.21,2.385]




