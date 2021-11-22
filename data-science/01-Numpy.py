"""
BASIC CONCEPTS:
-Numpy is a library for mathmatical operations with Python.
-We will use arrays to perform such operations.

NDARRAY CLASS:
-Numpy’s array class is called ndarray.
-A numpy ndarray can hold only a single datatype.
-It has the following attributes:
    -ndim: the number of axes (dimensions) of the array. It is also called the rank of the array.
    -shape: the size of the array in each dimension. The length of the shape tuple is the rank or ndim.
    -size: the total number of elements in the array. It is equal to the product of the elements of the shape tuple.
    -type: the type of the elements in the array. It can be created or specified using Python.
"""

import numpy as np



# -----------------BASIC CONCEPTS-----------------

# Create array or matrix (a matrix is a two-dimension arrays)
# We can create arrays by converting a list
my_array = np.array([0, 1, 2])
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list = [1, 2, 3]
my_array_list = np.array(my_list)

# Get attributes of an array
print(my_array.ndim)
print(my_array.shape)
print(my_array.size)
print(my_array.dtype)

# Indexing/slicing arrays is similar to a python list
arr = np.arange(0, 11)
return_array = arr[1:5]

# Indexing/slicing in a matrix: arr_2d[row][col] or arr_2d[row,col]
arr_2d = np.array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
return_matrix = arr_2d[1]
return_matrix2 = arr_2d[1, 0]
return_matrix3 = arr_2d[:2, 1:]
return_matrix4 = arr_2d[:2]

# Comparing arrays will return boolean values
# We can use a boolean array to conditionally select or index from an array
# An alternative is select an array of an array where we apply a condition
bool_arr = arr > 5
print(arr[bool_arr])
print(arr[arr > 5])

# Broadcasting: ability of NumPy to treat arrays of different shapes during arithmetic operations
# If we assign a value to a range, the array will expand that range
arr2 = np.arange(0, 11)
arr2[0:5] = 100

# With numpy arrays, data is not copied, it's a view of the original array
# If we change a value in a view of an array, that value will change in the original array too
arr2_view = arr2.view()
arr2_view[4] = 20

# To copy an array, we must use copy() method
arr2_copy = arr2.copy()






# -----------------NUMPY FUNCTIONS-----------------

arr = np.arange(0, 11)
arr2 = np.arange(2, 9)
arr3 = np.arange(25)

# arange() -> return evenly spaced values within a given interval. We can set a step size (optional, 1 by default)
print(np.arange(0, 10))
print(np.arange(0, 11, 2))

# full() -> create an array full of a given value
array_full = np.full(10, 7)
array_full2 = np.full((3, 5), 4)

# hsplit() -> split array into several arrays
# hstack() -> stack several arrays into one array
arr4_split = np.hsplit(arr, 2)
arr4_stack = np.hstack(arr2, arr)

# linspace() -> return evenly spaced numbers over a specified interval. Default space is 50
print(np.linspace(0, 10))

# max/min()       -> find max or min values. An optional initial parameter can be filled to indicate the beginning
# argmax/argmin() -> find index locations for max or min values
arr.max(initial=0)
arr.min(initial=0)
arr.argmax()
arr.argmin()

# zero/ones() -> create an array containing only 0 or 1
array_with_zeros = np.zeros((4, 5))
array_with_ones = np.ones(3)

# ravel() -> convert a multidimensional array into a one-dimensional array
ravel_array = arr.ravel()

# reshape() -> return a new array containing the same data with a new shape
arr3.reshape(5, 5)

# rand(n)               -> return n random values from a uniform distribution
# randn(n)              -> return n random values from the "standard normal" distribution
# ranf(n)               -> return n random floats in the half-open interval [0.0, 1.0)
# randint(low, high, n) -> return n random integers from low (inclusive) to high (exclusive)
np.random.rand(2)
np.random.randn(2)
np.random.randint(1, 100)
np.random.randint(1, 100, 10)
np.random.ranf(5)

# identity(n)        -> create an identity matrix of n dimension
# linalg.inv(matrix) -> find the inverse of an array and add its diagonal data elements (only for squared matrix)
# transpose()        -> interchange rows as columns, and vice-versa
identity_matrix = np.identity(3)
inv_matrix = np.linalg.inv(my_matrix)
arr_transp = arr.transpose()






# -----------------NUMPY OPERATIONS-----------------

# We can perform common arithmetical operations
# If we try to divide by 0, we will get a warning
arr_sum = arr+arr
arr_dif = arr-arr
arr_pro = arr*arr
arr_div = arr/arr2

# We can also perform logical or comparision operations
arr_bool = arr > 3
print(arr_bool)

# Universal array/matrix functions
arr_sqrt = np.sqrt(arr)       # squared root
arr_exp = np.exp(arr)         # exponential
arr_sin = np.sin(arr)         # sin, cos, tan
arr_log = np.log(arr)         # natural logarithm
mat_std = np.std(arr)         # standard deviation
mat_sum = arr_2d.sum(axis=0)  # sum of all columns in a matrix
mat_mean = np.mean(arr)       # mean
