# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#a single neuron with 3 inputs coming into it
inputs = [1.2, 5.1, 2.1]
#each unique input is also going to have a unique weight associated with it
weights = [3.1, 2.1, 8.7]
#each neuron also has a unique bias
bias = 3

#first step for the neuron is to add up all the inputs*weights and add the bias
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)