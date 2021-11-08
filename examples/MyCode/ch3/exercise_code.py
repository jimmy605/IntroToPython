import math 
# Exercises

# 3.1 - Completed




#3.5 - Turing Test
# problem = input('What is your problem? ')

# problem = input('Have you had this problem before (yes or no)? ')
# if problem == 'yes':
#     print('Well, you have it again.')
# else:
#     print('Well, you have it now.')




#3.7 - Table of squares and cubes
# def squares_cubes(end_range):
#     # Print the header
#     print('Number   Square   Cube')
    
#     for n in range(end_range + 1):
#         number = n 
#         square = n ** 2
#         cube = n ** 3
#         print(f'{number:>6}{square:>9}{cube:>7}')

# squares_cubes(5)




#3.8 - Smallest and largest
# def smallest_largest(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     minimum = min(numbers)
#     maximum = max(numbers)
    
#     product = 1
#     for num in numbers:
#         product *= num
    
#     print(f'Total: {total}\nAverage: {average}\nMinimum: {minimum}')
#     print(f'Maximum: {maximum}\nProduct: {product}')

# smallest_largest([12, 34, 11, 5])




#3.9 - Seperating the digits in an integer
# def seperate_digits(digits):
#     output = ''
    
#     for digit in str(digits):
#         print(digit, end=', ')

# seperate_digits(291084)




#3.10 - Investment return





#3.11 - Miles per gallon
# def fuel_data():
#     total_gallons = 0
#     total_miles = 0
    
#     gallons = float(input('Enter the gallons used (-1 to end): '))
    
#     while gallons:
#         miles = int(input('Enter the miles driven: '))
#         print(f'the miles/gallon for this tank was {miles / gallons}')
        
#         total_gallons += gallons
#         total_miles += miles
        
#         gallons = float(input('Enter the gallons used (-1 to end): '))
#         if gallons == -1:
#             print(f'The overall average miles/gallon was {total_miles / total_gallons}')

# fuel_data()




#3.12 - Palindromes
# def palindromes():
#     check_digits = input('Enter the digits: ')
    
#     if check_digits == check_digits[::-1]:
#         print('It is a Palindrome')
#     else:
#         print('No, it is not a Palindrome')

# palindromes()




#3.13
# def factorials(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorials(n - 1)

# print(factorials(5))




#3.14 Mathematical constant pie
# def math_constant_pie(series):
#     pie = 4 - (4/3)
#     denominator = 5
    
#     print(f'1 = {pie}')
    
#     for num in range(series - 1):
#         if num % 2 == 1:
#             pie -= (4/denominator)
#             print(f'{num + 2} = {pie}')
#             denominator += 2
            
#         else:
#             pie += (4/denominator)
#             print(f'{num + 2} = {pie}')
#             denominator += 2
    
# math_constant_pie(1000)




#3.15 - Mathematical constant e
# def factorials(n):
#     if n < 2:
#         return 1
#     else:
#         return n * factorials(n - 1)

# def mathematical_constant_e(series):
#     e = 1 + (1 / factorials(1))
    
#     for denominator in range(2, series + 2):
#         e += 1 / factorials(denominator)
    
#     print(e)

# mathematical_constant_e(10)




#3.16 - Nested control statements
# numbers = [1,2,3,4,10,9,8,7,6,5]

# largest = 0
# second_largest = 0

# for number in numbers:
#     if number > largest:
#         largest = number
#     if number < largest and number > second_largest:
#         second_largest = number 

# print(f'This is the largest number: {largest}')
# print(f'This is the second largest number: {second_largest}')




#3.17 - Nested loops
# for section in range(1):
#     for row in range(1, 11):
#         asterisk = '*' * row
#         print(f'{asterisk:<10}')
        
#     for row in range(10, 0, -1):
#         asterisk = '*' * row
#         print(f'{asterisk:<10}')
    
#     for row in range(10, 0, -1):
#         asterisk = '*' * row
#         print(f'{asterisk:>10}')
    
#     for row in range(1, 11):
#         asterisk = '*' * row
#         print(f'{asterisk:>10}')




#3.18 - Additional nested loop side by side
# Iterate through the main loop ten times
# for i in range(1, 11):
#     a = '*' * i
#     d = '*' * i
    
#     b = '*' * (11 - i)
#     c = '*' * (11 - i)
    
#     print(f'{a:<12}{b:<12}{c:>12}{d:>12}')




#3.19 - Brute force computing Pythagorean triples
# Sides squared will equal the hypotenuse squared else not a rihgt angle triangle
# side_1 = 1
# side_2 = 1

# for h in range(1, 21):
#     if side_1 ** 2 + side_2 ** 2 == h ** 2:
#         print(side_1, side_2, h)
    
#     for side_1 in range(1, 21):
#         if side_1 ** 2 + side_2 ** 2 == h ** 2:
#             print(side_1, side_2, h)
        
#         for side_2 in range(1, 21):
#             if side_1 ** 2 + side_2 ** 2 == h ** 2:
#                 print(side_1, side_2, h)



#3.20 - binary to decimal conversion
def binary_to_decimal(binary_num):
    """Returns a binary num input to decimal input."""
    total_sum = []
    binary_decimal = [2 ** i for i in range(0,9)]
    
    # Reverse the binary_num
    reverse_binary_num = []
    for i in binary_num:
        reverse_binary_num.insert(0, i)
    
    for idx, digit in enumerate(reverse_binary_num):
        if int(digit) == 1:
            total_sum.append(binary_decimal[idx])
    
    return sum(total_sum)

print(binary_to_decimal('11111110'))