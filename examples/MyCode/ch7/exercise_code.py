import pandas as pd
import numpy as np
import random 
import math 
from collections import Counter 
from copy import deepcopy


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
# test_list = [[1, 123, 1000345324455],
#              [23, 4567500, 56000]]

# def array_loop(lyst):
#     # Variable to store the length of the longest element in the list
#     elem_count = max([len(str(num)) for a_list in lyst for num in a_list]) + 2

#     # Iterate through the list of lists
#     for a_list in lyst:
#         for element in a_list:
#             space = ' ' * (elem_count - len(str(element)))
#             print(f'{space}{element}',end='')
#         print()

# array_loop(test_list)




# 7.8 - Reimplement DataFrame output
# test_list = [[1, 123, 1554],
#              [23, 4567500, 56000]]

# def dataframe_output(lyst):    
#     # Find the widest value in the list
#     val_width = max([len(str(num)) for a_list in lyst for num in a_list]) + 2
    
#     # Row and column values to be integer values starting with 0
#     # Print the column indices
#     count = 0
#     for num in range(len(test_list[0])):
#         if count == 0:
#             space = ' ' * (val_width // 2 + 1)
#             print(f'{space}{num}', end='')
#             count += 1
#         else:
#             space = ' ' * val_width
#             print(f'{space}{num}', end='')
            
#     print()
    
#     # Iterate through the lists. Need to print the row number at the start of each line 
#     for i, a_list in enumerate(lyst):
#         print(i, end='')
#         for i, num in enumerate(a_list):
#             space = ' ' * (val_width - len(str(num)))
#             print(f'{space}{num}', end='')
        
#         print()


# dataframe_output(test_list)




# 7.9 - Indexing and slicing arrays
# new_array = np.arange(1, 16).reshape(3, 5)


# # a) Select row 2
# print(new_array[1])

# # b) Select column 5
# print(new_array[:, 4])

# # c) Select rows 0 and 1
# print(new_array[0:2])

# # d) Select columns 2 - 4
# print(new_array[:,1:4])

# # e) Select the element that is in row 1 and column 4
# print(new_array[0, 4])

# # f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.
# print(new_array[1:3, [0,2,4]])




# 7.10 - Completed in a seperate file




# 7.11 & 7.12 - Both a little too hard for my current level ATM




# 7.13 - Research and use other broadcasting capabilities
# a = np.array([5, 7, 3, 1])
# b = np.array([1,2,3,4])
# print(a * b)

# c = 2
# print(a * c)




# 7.14 - Horizontal and vertical stacking
# array1 = np.array([[0, 1], [2, 3]])
# array2 = np.array([[4, 5], [6, 7]])

# # a)
# array3 = np.vstack((array1, array2)).reshape(2, 4)
# # print(array3)

# # b)
# def array_flatten(array_lyst):
#     return array_lyst.flatten()

# array4 = [[array_flatten(array1)[i], array_flatten(array2)[i]] for i in range(4)]
# # print(np.vstack((array4)))

# # c)
# array5 = np.vstack((array4, array4)).reshape(4, 4)
# # print(array5)

# # d)
# array6 = np.hstack((array3, array3)).reshape(4, 4)
# # print(array6)




# 7.15 - Research and use Numpy's concatenate function
# array1 = np.array([[0, 1], [2, 3]])
# array2 = np.array([[4, 5], [6, 7]])

# # a)
# array3 = np.concatenate((array1, array2), axis=0)
# # print(array3)

# # b)
# array4 = np.concatenate((array1, array2), axis=1).reshape(2, 4)
# # print(array4)




# 7.16 - Research Numpy tile function
# dashes = np.array('     |' * 10)
# asterisks = np.array('******' * 11)

# rows = 10
# repeats = 3
# print(np.tile([dashes, asterisks], (rows, repeats)))




# 7.17 - Research Numpy bincount function
# random_nums = np.array([random.randint(0, 99) for num in range(25)]).reshape(5, 5)
# bin_value = np.bincount(random_nums.flatten())
# print(f'Bin length is: {len(bin_value)}')
# print(bin_value)




# 7.18 - Median and mode of an array
# ages = np.arange(5)
# new_ages = np.arange(6)
# depth_array = np.array([random.randint(1, 5) for i in range(100)])

# def array_median(array):
#     copy_array = array
    
#     # Flatten the array if the length is greater than 1
#     if len(array) > 1:
#         copy_array = sorted(array.flatten())
    
#     # Length of the array
#     length = len(copy_array)
    
#     # Middle of an array with a odd length
#     middle = length // 2
#     if length % 2 == 1:
#         return copy_array[middle]
    
#     # Array with an even length
#     else:
#         left = middle - 1
#         right = middle
#         average = (copy_array[left] + copy_array[right]) / 2
#         return average

# print(array_median(depth_array))


# def array_mode(array):
#     copy_array = array 
    
#     # Flatten the array if the length is greater than 1
#     if len(array) > 1:
#         copy_array = sorted(array.flatten())

#     value = 0 # Current highest value count
#     output = 0 # Current most occuring value
    
#     for num, count in Counter(copy_array).items():
#         if count > value:
#             value = count
#             output = num
    
#     return output 

# array_mode(depth_array)




# 7.19 - Enchanced median and mode of an array
# Skipped this one




# 7.20 - Cant get the function working




#. 7.21 Shallow vs deep copy
# dictionary = {'Sophia': [97, 88]}
# new = dictionary.copy()
# new['Sophia'][0] = 90
# print(dictionary, new)

# new_deep_copy = deepcopy(dictionary)
# dictionary['Sophia'][0] = 90
# new_deep_copy['Sophia'][0] = 89
# print(dictionary, new_deep_copy)




# 7.22 - Pandas Series
# a)
# lyst = pd.Series([7, 11, 13, 17])

# # b)
# five_elements = pd.Series([100.0 for i in range(5)])

# # c)
# random_nums = pd.Series([random.randint(0, 101) for i in range(20)])
# stats = random_nums.describe()

# # d)
# temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])

# # e)
# dict_temps = dict(temperatures)
# new_temps = pd.Series(dict_temps)




# 7.23 - Pandas DataFrames
# a) 
temperatures = pd.DataFrame({'Maxine':[35, 34.2, 28.4],
                             'James': [24.3, 44, 39.9],
                             'Amanda': [16, 19.2, 21.1]})

# b)
temperatures.index = ['Morning', 'Afternoon', 'Evening']

# c)
# print(temperatures.loc[:]['Maxine'])

# d)
# print(temperatures.iloc[[0][:]])

# e)
# print(temperatures.iloc[[0, 2]])

# f)
# print(temperatures.iloc[:, [0, 2]])

# g)
# print(temperatures.loc['Morning':'Afternoon', ['Maxine', 'Amanda']])

# h)
# print(temperatures.describe())

# i)
# print(temperatures.T)

# j)
# print(temperatures.sort_index(axis=1))




# 7.24 AI Project: Introducing Heuristic programming with the knight's tour
# a) - Got 26 moves

# b)
