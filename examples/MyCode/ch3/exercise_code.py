import statistics
import decimal
import math 

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
# def digit_seperator():
#     number = input('Enter a number to be seperated: ')
    
#     for char in number:
#         if int(char) % 2 == 0:
#             print(char, end='   ')
#         else:
#             print(char, end='   ')

# digit_seperator()




#3.10
# def investment_return(principal, rate, years):
#     """Returns the return on the investment."""
#     # Total amount
#     total_amount = principal
    
#     # Print header for the table
#     print(f'Year    Amount Earned')
    
#     # Loop through each year 
#     for year in range(1, years + 1):
#         # Calculate the principal + interest earned
#         total_amount *= (1 + rate)
#         # Print the data - year, total_amount
#         print(f'{year:>3}{total_amount:>15.2f}')

# investment_return(1_000, 0.07, 30)




#3.11
# # Sentinel/user input gallons used
# gallons_used = gallons_used = float(input('Enter the gallons used (-1 to end): '))
# total_gallons = 0
# total_miles = 0

# while gallons_used != -1:
#     # User input miles driven
#     miles_driven = int(input('Enter the miles driven: '))
    
#     # Update total variables 
#     total_miles += miles_driven
#     total_gallons += gallons_used
    
#     # Miles/gallon calculation
#     miles_per_gallon = miles_driven / gallons_used
    
#     # Print miles/gallon achieved
#     print(f'The miles/gallon for this tank was: {miles_per_gallon:.2f}')
#     print() # Seperate each input
    
#     gallons_used = float(input('Enter the gallons used (-1 to end): '))

# print() # Seperate data
# results_average = total_miles / total_gallons
# # Print total miles/gallon
# print(f'The overall average miles/gallon was: {results_average:.2f}')




#3.12
# def palindrome():
#     # user input to check if a palindrome
#     check_palindrome = input('Enter a number or word to check: ')
    
#     return True if check_palindrome == ''.join(check_palindrome[::-1]) else False 

# print(palindrome())




#3.13
# def fact(n):
#     if n < 2:
#         return 1
#     return n * fact(n - 1)

# for i in range(10, 31, 10):
#     print(fact(i))




#3.14
# def approx_pie():
#     # User input - How many terms to iterate through
#     terms = int(input('Enter how many terms you want to iterate through: '))
    
#     # Print the header 
#     print(f'Terms        Pie')
    
#     # Variables
#     pie = 4
#     denominator = 3
#     counter = 1 # Use to change the arithmetic operator
    
#     # Loop through if pie is > math.pi()
#     # while pie > math.pi:
#     for i in range(terms):
#         # Change the arithmetic operator each iteration
#         if counter % 2 == 1:
#             pie -= (4 / denominator)
#         else:
#             pie += (4 / denominator)
        
#         # Print the data to the table
#         print(f'{counter:>4}{pie:>16.6f}')
        
#         # Update variables
#         counter += 1
#         denominator += 2
    
#     # Return the value once pie <= math.pi()
#     print() # Seperate final pie value from table
#     print(pie)

# approx_pie()




#3.15
# def fact_2(n):
#     if n < 2:
#         return 1
#     return n * fact_2(n - 1)


# def approx_e():
#     # User input - Iterations to be completed
#     iterations = int(input('How many iterations do you want? '))
    
#     # Variables
#     e = 1
#     fact_counter = 1
    
#     for i in range(iterations):
#         e += (1 / fact_2(fact_counter))  # Use the factorial function
#         fact_counter += 1
    
#     return e 

# print(approx_e())




#3.16
# def two_largest_nums(lyst):
#     # Sort the list in place
#     lyst.sort()
#     # Return the -1 and -2 indexes
#     return lyst[-1], lyst[-2]

# print(two_largest_nums([13, 56, 345, 654, 786, 65, 456, 123, 6547, 765]))




#3.17
# Create (a) first then rethink
for i in range(4):
    counter = 1
    for j in range(10):
        print('*' * j)