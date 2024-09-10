# Creating a NumPy array from a list
import numpy as np
# Create a NumPy array from a list
array1 = np.array([8, 5, 3, 2, 1, 1])
# print(array1)
# # example of a 1D array, or 1-dimensional array 

# # Create a NumPy multi-dimensional array from nested lists
# # import numpy as np
# array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# print(array2)

# # # Number of dimensions of array2
# print(array2.ndim)
# # # Number of elemets (rows & columns in this instance) of array2
# print(array2.shape)

# # Sorting is performed using the sort function
# print(np.sort(array1))

# An array can be broken into multiple arrays using array_split
# Split array1 into three separate arrays
newarray1 = np.array_split(array1, 3)
print(newarray1)
