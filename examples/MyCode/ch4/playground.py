import random
from math import ceil, floor
import statistics as stats 
import decimal as dec 

# def square(number):
#     """Calculate the square of number."""
#     return number ** 2

# print(square(7))
# print(square(2.5))

# print('The square of 7 is', square(7))


# def square_root(number):
#     return number ** 0.5

# print('The square root of 6.25 is', square_root(6.25))


# def maximum(v1, v2, v3):
#     """Return the maximum of three values."""
#     max_value = v1
#     if v2 > max_value:
#         max_value = v2 
#     if v3 > max_value:
#         max_value = v3 
#     return max_value


# print(maximum(12, 27, 36))
# print(maximum(12.3, 45.6, 9.7))
# print(maximum('yellow', 'red', 'orange'))


# for roll in range(10):
    # print(random.randrange(1, 7), end=' ')


# random.seed(32)

# for roll in range(10):
#     print(random.randrange(1, 7), end=' ')
# print()

# for roll in range(10):
#     print(random.randrange(1, 7), end=' ')
# print()

# random.seed(32)
# for roll in range(10):
#     print(random.randrange(1, 7), end=' ')

# heads = 0 
# tails = 0
# for num in range(20):
#     toss = random.randrange(0, 2)
#     if toss:
#         print('T', end=' ')
#         tails += 1
#     else:
#         print('H', end=' ')
#         heads += 1

# print('Heads=', heads, 'and Tails=', tails)


# student = ('Sue', [89, 94, 85])
# name, grades = student
# print(f'{name}: {grades}')


# def rectaongle_area(length=2, width=3):
#     """Return a rectangle's area."""
#     return length * width 

# print(rectaongle_area())
# print(rectaongle_area(10))


# def average(*args):
#     return sum(args) / len(args)

# print(average(5, 10))
# print(average(5,10,15,20))

# grades = [88,75,96,55,83]
# print(average(*grades))


# def calculate_product(*lyst):
#     product = 1    
#     for num in lyst:
#         product *= num
    
#     return product

# print(calculate_product(10, 20, 30))
# print(calculate_product(*range(1, 6, 2)))


# x = 7
# def access_global():
#     print('x printed from access_global', x)

# access_global()


# print(ceil(10.3))
# print(floor(10.7))


# grades = [85, 93, 45, 87 ,93]
# print(stats.mean(grades))


# macbook = dec.Decimal('2.5') ** 2
# print(macbook)


# x = 7
# print(id(x))


# def cube(number):
#     print('id(number):', id(number))
#     return number ** 3

# cube(7)


# def cube(number):
#     print('number is x:', number is x) # x is a bglobal variable
#     return number ** 3

# cube(x)


# def cube(number):
#     print('id(number) before modifying number:', id(number))
#     number **= 3
#     print('id(number) after modifying number:', id(number))
#     return number

# cube(x)


# width = 15.5
# print('Variable width:', id(width))

# width *= 2
# print('Variable width:', id(width))


# die_rolls = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

# def pvari(data):
#     mean_of_data = sum(data) / len(data)
#     mean_sub = [num - mean_of_data for num in data]
#     square_list = sum([num ** 2 for num in mean_sub]) / len(data)
    
#     print(square_list)

# pvari(die_rolls)
# print(stats.pvariance(die_rolls))


# lyst = [1, 2, 3, 4, 5]
# def mystery(x):
#     y = 0
#     for value in x:
#         y += value ** 2
#     return y

# print(mystery(lyst))