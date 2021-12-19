import numpy as np 
import random
import pandas as pd 

grades_dict = {'Wally': [87, 96, 70], 
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90], 
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)
grades.index = ['Test1', 'Test2', 'Test3']
pd.set_option('precision', 2)

# print(grades.sort_index(ascending=False))
# print(grades.sort_index(ascending=False, axis=1))
# print(grades.loc['Test1'].sort_values(ascending=False))


temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}   

temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print(temperatures)

print(temperatures.loc[:, 'Mon':'Wed'])

print(temperatures.loc['Low'])

pd.set_option('precision', 2)
print(temperatures.mean())

