import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
addition = a + b

#Indexing
val = addition[1]
print(val)

#Slicing:
sub = addition[0:2]
print(sub)

#Reshaping
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
