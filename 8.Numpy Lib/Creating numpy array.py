import numpy as np

#Creating NumPy Arrays:

arr = np.array([1,2,3,4,5,6])

print(arr)

zeros_arr = np.zeros(5)         # Create an array of zeros: [0. 0. 0. 0. 0.]
print(zeros_arr)
ones_arr = np.ones(3)
print(ones_arr)# Create an array of ones: [1. 1. 1.]
random_arr = np.random.rand(3)  # Create an array of random numbers between 0 and 1
print(random_arr)

#Arithmetic Sequences:
seq_arr = np.arange(0, 100, 7)   # Create an array with values from 0 to 100 (exclusive) with a step of 7
print(seq_arr)