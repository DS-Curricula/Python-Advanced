import numpy as np

'''Creating a 2D Array'''
# Create a 2D array with 2 rows and 5 columns
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_2d)

'''Accessing Elements'''
element = arr_2d[1, 2]  # Accesses the element at row index 1 and column index 2.
print(element)  # Output: 8

'''Array attributes'''
dimensions = arr_2d.ndim  # Returns the number of dimensions of the array.
print(dimensions)  # Output: 2

arr_shape = arr_2d.shape  # Returns the shape of the array as a tuple (rows, columns).
print(arr_shape)  # Output: (2, 5)

arr_size = arr_2d.size  # Returns the total number of elements in the array.
print(arr_size)  # Output: 10

'''Slicing the array'''
sub_array = arr_2d[:2, :2]  # Selects the first 2 rows and the first 2 columns.
print(sub_array)  # Output: [[1 2]. [6 7]]

# Negative slicing - refers to an index from the end
sub_array_2 = arr_2d[-4:, -4:]  # Slices the last 4 elements from both rows
print(sub_array_2)  # Output: [[ 2  3  4  5], [ 7  8  9 10]]

# Slicing with Step
sub_array_3 = arr_2d[:, ::2]  # Selects every other column from both rows.
print("result:", sub_array_3)  # Output: [[ 1  3  5],  [ 6  8 10]]

''' Statistical Operations'''
total_sum = np.sum(arr_2d)  # Computes the sum of all elements in the array.
print(total_sum)  # Output: 55

# Mean of all elements
mean = np.mean(arr_2d)  # Computes the mean (average) of all elements in the array.
print(mean)  # Output: 5.5

# Sum along axis 0 (columns)
sum_columns = np.sum(arr_2d, axis=0)  # Computes the sum of elements along axis 0 (columns).
print(sum_columns)  # Output: [ 7  9 11 13 15]

# Sum along axis 1 (rows)
sum_rows = np.sum(arr_2d, axis=1)  # Computes the sum of elements along axis 1 (rows).
print(sum_rows)  # Output: [15 40]

''' Reshaping '''
reshaped_array = arr_2d.reshape(
    (5, 2))  # Reshapes the array in 5 rows and 2 columns. The total number of elements must remain the same.
print(reshaped_array)  # Output: [[ 1  2],  [ 3  4], [ 5  6], [ 7  8], [ 9 10]]
