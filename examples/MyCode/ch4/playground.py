import random
import math 
import statistics

def square(number):
    """Calculate the square of number."""
    return number ** 2

# print(square(7))
# print(square(2.5))

# print('The square of 7 is', square(7))




def square_root(number):
    """Return the square root of number."""
    
    return number ** 0.5 

# print(square_root(6.25))




def maximum(v1, v2, v3):
    """Return the maximum of 3 values."""
    return max(v1, v2, v3)

# print(maximum(12, 27, 36))




# for roll in range(10):
    # print(random.randrange(1, 7), end=' ')




# for coin in range(21):
#     print('H' if random.randrange(2) == 0 else 'T', end=' ')




def rectangle_area(length=2, width=3):
    """Return a rectangle' area."""
    return length * width

# print(rectangle_area())




def average(*args):
    return sum(args) / len(args)




def calculate_product(*args):
    product = 1
    for num in args:
        product *= num 
    
    return product

# print(calculate_product(10, 20, 30))
# print(calculate_product(*range(1, 6, 2)))




x = 7

def modify_global():
    global x
    x = 'Hello'
    print(f'x printed from modify_global: {x}')

# modify_global()


# print(id(x))

def cube(number):
    print(f'number is x: {number is x}')
    return number ** 3

# print(cube(x))




width = 15.5
# print(f'id of width originally: {id(width)}')

width += 12
# print(f'id of width modified: {id(width)}')




classmates = statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])
print(classmates)