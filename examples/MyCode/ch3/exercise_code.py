import statistics

# Exercises from chapter 3

#3.1
# """Using nested control statements to analyze examination results."""
# # initialize variables
# passes = 0  # number of passes
# failures = 0  # number of failures

# # process 10 students
# for student in range(10):
#     # get one exam result
#     result = int(input('Enter result (1=pass, 2=fail): '))
    
#     # while loop and use sentinal controlled repetition till inpur == 1 or 2
#     while result not in [1, 2]:
#         result = int(input('Enter result (1=pass, 2=fail): '))
    
#     if result == 1:
#         passes = passes + 1
#     else:
#         failures = failures + 1

# # termination phase
# print('Passed:', passes)
# print('Failed:', failures)
# if passes > 8:
#     print(' Bonus to instructor')




#3.3
# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()




#3.4 - Note exact format as the book but i don't see another way to implement it
# for i in range(1):
#     for j in range(2):
#         print('@' * 7)
#     print()




#3.5
# """Compare integers using if statements and comparison operators."""

# print('Enter two integers and I will tell you',
#       'the relationships they satisfy.')

# # read first integer
# number1 = int(input('Enter first integer: '))

# # read second integer
# number2 = int(input('Enter second integer: '))

# if number1 == number2:
#     print(number1, 'is equal to', number2)
# else:
#     print(number1, 'is not equal to', number2)

# if number1 < number2:
#     print(number1, 'is less than', number2)
# else:
#     print(number1, 'is greater than', number2)

# if number1 <= number2:
#     print(number1, 'is less than or equal to', number2)
# else:
#     print(number1, 'is greater than or equal to', number2)




#3.6
# # Prompt user - 'What is your problem'
# problem = input('What is your problem: ')

# # Prompt user - 'Have you had this problem before (yes or no)?'
# answer = input('Have you had this problem before (yes or no)? ')

# # Double selection statement
# # If user enters yes print - 'Well, you have it again.'
# if answer in ['yes', 'Yes', 'YES', 'y', 'Y']:
#     print('Well, you have it again.')
# # Else - 'Well, you have it now.'
# else:
#     print('Well, you have it now.')




#3.7
# def square_cubes(num):
#     """Table of the squares and cubes of 'num'."""
#     print(f'Number    Square    Cube')

#     for n in range(num):
#         number, square, cube = n, n * n, n ** 3
#         print(f'{number:>6}    {square:>6}    {cube:>4}')

# square_cubes(6)




#3.8
# def calc_product(lyst):
#     total = 1
    
#     for num in lyst:
#         total *= num 
#     return total


# def data_output():
#     """Take an arbitary number of numbers and return the su, average, product, smallest and largest values."""
#     # Variables
#     numbers = int(input('How many number do you want to input: '))
#     data = []
    
#     for i in range(numbers):
#         data.append(int(input('Enter a number: ')))
    
#     total_sum = sum(data)
#     average = statistics.mean(data)
#     product = calc_product(data)
#     smallest = min(data)
#     largest = max(data)
    
#     print(f'Total sum: {total_sum}')
#     print(f'Average: {average}')
#     print(f'Product: {product}')
#     print(f'Smallest: {smallest}')
#     print(f'Largest: {largest}')

# data_output()




#3.9
def digit_seperator():
    number = input('Enter a number to be seperated: ')
    
    
    for char in number:
        if int(char) % 2 == 0:
            