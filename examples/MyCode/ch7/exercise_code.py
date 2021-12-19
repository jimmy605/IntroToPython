import pandas as pd
import numpy as np

# 7.1 - Filling arrays
# ones = np.ones((2, 3), dtype=int) # 2 by 3 array with 1's
# print(ones)

# zeros = np.zeros((3, 3), dtype=int) # 3 by 3 array with 0's
# print(zeros)

# sevens = np.full((2, 5), 7) # 2 by 5 array with 7s
# print(sevens)




# 7.2 - Broadcasting
# num1 = np.arange(0, 4).reshape(2, 2)

# # a) Cube every element of the array
# print(num1 ** 3)

# # b) Add 7 to every element of the array
# print(num1 + 7)

# # c) Multiply every element of the array by 2
# print(num1 * 2)




# 7.3 - Element-Wise array multiplication
# evens = np.arange(2, 19, 2).reshape(3, 3)
# print(evens)

# countdown = np.arange(9, 0, -1).reshape(3, 3)
# print(countdown)

# print(evens * countdown)




# 7.4 - Array from list of lists
# lyst = [[2, 3, 5, 7, 11], [13, 17, 19, 23, 29]]
# print(np.array(lyst).reshape(2, 5))




# 7.5 - Flattening arrays with flatten vs ravel
# flatten_ravel = np.array([2 ** num for num in range(6)]).reshape(2, 3)
# print(flatten_ravel.flatten()) # Flatten the array
# print(flatten_ravel.ravel()) # Ravel the array
# print(flatten_ravel) # Print the array to confirm it hasn't be modified




# 7.6 - Research: array method astype
# nums = np.linspace(1.1, 6.6, 6).reshape(2, 3).astype('int64')
# print(nums)




# 7.7 - Reimplement NumPy array output