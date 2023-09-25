from ctypes.wintypes import SIZE

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
seq_arr = np.arange(0, 100, 7)   # Create an array with values from 0 to 10 (exclusive) with a step of 2
print(seq_arr)


#Basic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

addition = a + b      # Element-wise addition
print(addition)
subtraction = a - b   # Element-wise subtraction
print(subtraction)
multiplication = a * b  # Element-wise multiplication
print(multiplication)
division = a / b      # Element-wise division
print(division)

#Indexing and Slicing:
val = addition[1]
print(val)
sub = addition[0:2]
print(sub)

arranges = np.arange(12)
print(arranges)
reshaped = arranges.reshape(3, 4)  # Reshape to a 3x4 matrix
print(reshaped)


arr = np.array([[1, 2, 3], [4, 5, 6]])
shape = arr.shape    # Shape of the array (2, 3)
print(shape)
dtype = arr.dtype    # Data type of the elements (int64)
print(dtype)
size = arr.size      # Number of elements (6)
print(size)
