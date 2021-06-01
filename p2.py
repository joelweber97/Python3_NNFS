# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#4 inputs coming into 3 neurons
#we'll need 3 weight sets of 4 values each
#the inputs for each neuron will be the same, but the weights into each output will be different.
inputs = [1,2,3,2.5]
#each unique input is also going to have a unique weight associated with it
weights1 = [0.2,0.8,-0.5,1.0]
weights2 = [0.5,-0.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]
#each neuron also has a unique bias
bias1 = 2
bias2 = 3
bias3 = 0.5

#first step for the neuron is to add up all the inputs*weights and add the bias
output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
print(output)


#How do you go about getting the correct values in the output?
#Since you can't really change in the inputs into the layer, you'll have to modify the weights and/or biases
