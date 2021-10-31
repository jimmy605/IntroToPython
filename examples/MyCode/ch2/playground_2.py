import math
x, y = 7, 3
total = x + y
print(total)

print(type(x))

# Calculating the square root of a number.
print(9 ** 0.5)

def stats(num_list):
    min_val = min(num_list)
    max_val = max(num_list)
    range_vals = [min_val, max_val]
    
    print(f'The min is: {min_val}, max is: {max_val} and range is {range_vals[0]}:{range_vals[1]}')

stats([47,95,88,73,88,84])

########### Exercise Code Below ###############

# 2.5 - Circle area, diameter and circumference
def findings(radius):
    diamter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    
    print('Diameter:', diamter,
          'Circumference:', circumference,
          'Area:', area)

findings(2)


# #2.6 - Odd or even
def even_or_odd(num):
    print('Even' if num % 2 == 0 else 'Odd')

for i in range(5):
    even_or_odd(i)


# #2.8 - Table of squares and cubes
def table(num_range):
    # Print the table header
    print('number    Square    Cube')
    
    for i in range(1, num_range):
        print(f'{i:>4}{i ** 2:>10}{i ** 3:>10}')

table(6)


# #2.9 - Integer value of a character
def char_values(val_list):
    for value in val_list:
        print(ord(value), end=', ')

char_values(['B', 'C', 'D', 'b', 'c', 'd', '0', '1', '2', '$', '*', '+', ' '])


# #2.10 - Arithmetic, smallest and largest
def stats(nums):
    sum_total = sum(nums)
    average = sum_total / len(nums)
    min_val, max_val = min(nums), max(nums)
    product = 1
    
    for num in nums:
        product *= num 
    
    print('\n', sum_total, average, product, min_val, max_val)

stats([4, 8, 2])


#2.11 - Seperating the digits in an integer
def seperate_digits():
    # Input 5 digits
    digits = input('Enter a 5 digit number: ')
    output = ''
    
    for digit in digits:
        output += f'   {digit}'
    
    print(output)

seperate_digits()


#2.12 - Investment return
def investment_return():
    # Constants
    RATE = 0.07
    
    # Variables
    principal = int(input('Enter the principal: '))
    invest_period = int(input('Enter the loan duration (10, 20 or 30): '))
    a = principal * (1 + RATE) ** invest_period
    
    print(f'The return on the your ${principal * invest_period:,.2f} investment is ${a:,.2f}')

investment_return()


#2.15 - Sort in ascending order
def ascending_order(total_nums):
    num_floats = []
    
    for num in range(total_nums):
        num = int(input('Enter floating point number: '))
        num_floats.appned(num)
    
    return sorted(num_floats)

print(ascending_order(3))