import statistics
from decimal import Decimal
import math 
import statistics

# Exercises from chapter 3

#3.1
"""Using nested control statements to analyze examination results."""
# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    # while loop and use sentinal controlled repetition till inpur == 1 or 2
    while result not in [1, 2]:
        result = int(input('Enter result (1=pass, 2=fail): '))
    
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print(' Bonus to instructor')




#3.3
for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()




#3.4 - Note exact format as the book but i don't see another way to implement it
for i in range(1):
    for j in range(2):
        print('@' * 7)
    print()




#3.5
"""Compare integers using if statements and comparison operators."""

print('Enter two integers and I will tell you',
      'the relationships they satisfy.')

# read first integer
number1 = int(input('Enter first integer: '))

# read second integer
number2 = int(input('Enter second integer: '))

if number1 == number2:
    print(number1, 'is equal to', number2)
else:
    print(number1, 'is not equal to', number2)

if number1 < number2:
    print(number1, 'is less than', number2)
else:
    print(number1, 'is greater than', number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)
else:
    print(number1, 'is greater than or equal to', number2)




#3.6
# Prompt user - 'What is your problem'
problem = input('What is your problem: ')

# Prompt user - 'Have you had this problem before (yes or no)?'
answer = input('Have you had this problem before (yes or no)? ')

# Double selection statement
# If user enters yes print - 'Well, you have it again.'
if answer in ['yes', 'Yes', 'YES', 'y', 'Y']:
    print('Well, you have it again.')
# Else - 'Well, you have it now.'
else:
    print('Well, you have it now.')




#3.7
def square_cubes(num):
    """Table of the squares and cubes of 'num'."""
    print(f'Number    Square    Cube')

    for n in range(num):
        number, square, cube = n, n * n, n ** 3
        print(f'{number:>6}    {square:>6}    {cube:>4}')

square_cubes(6)




#3.8
def calc_product(lyst):
    total = 1
    
    for num in lyst:
        total *= num 
    return total


def data_output():
    """Take an arbitary number of numbers and return the su, average, product, smallest and largest values."""
    # Variables
    numbers = int(input('How many number do you want to input: '))
    data = []
    
    for i in range(numbers):
        data.append(int(input('Enter a number: ')))
    
    total_sum = sum(data)
    average = statistics.mean(data)
    product = calc_product(data)
    smallest = min(data)
    largest = max(data)
    
    print(f'Total sum: {total_sum}')
    print(f'Average: {average}')
    print(f'Product: {product}')
    print(f'Smallest: {smallest}')
    print(f'Largest: {largest}')

data_output()




#3.9
def digit_seperator():
    number = input('Enter a number to be seperated: ')
    
    for char in number:
        if int(char) % 2 == 0:
            print(char, end='   ')
        else:
            print(char, end='   ')

digit_seperator()




#3.10
def investment_return(principal, rate, years):
    """Returns the return on the investment."""
    # Total amount
    total_amount = principal
    
    # Print header for the table
    print(f'Year    Amount Earned')
    
    # Loop through each year 
    for year in range(1, years + 1):
        # Calculate the principal + interest earned
        total_amount *= (1 + rate)
        # Print the data - year, total_amount
        print(f'{year:>3}{total_amount:>15.2f}')

investment_return(1_000, 0.07, 30)




#3.11
# Sentinel/user input gallons used
gallons_used = gallons_used = float(input('Enter the gallons used (-1 to end): '))
total_gallons = 0
total_miles = 0

while gallons_used != -1:
    # User input miles driven
    miles_driven = int(input('Enter the miles driven: '))
    
    # Update total variables 
    total_miles += miles_driven
    total_gallons += gallons_used
    
    # Miles/gallon calculation
    miles_per_gallon = miles_driven / gallons_used
    
    # Print miles/gallon achieved
    print(f'The miles/gallon for this tank was: {miles_per_gallon:.2f}')
    print() # Seperate each input
    
    gallons_used = float(input('Enter the gallons used (-1 to end): '))

print() # Seperate data
results_average = total_miles / total_gallons
# Print total miles/gallon
print(f'The overall average miles/gallon was: {results_average:.2f}')




#3.12
def palindrome():
    # user input to check if a palindrome
    check_palindrome = input('Enter a number or word to check: ')
    
    return True if check_palindrome == ''.join(check_palindrome[::-1]) else False 

print(palindrome())




#3.13
def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)

for i in range(10, 31, 10):
    print(fact(i))




#3.14
def approx_pie():
    # User input - How many terms to iterate through
    terms = int(input('Enter how many terms you want to iterate through: '))
    
    # Print the header 
    print(f'Terms        Pie')
    
    # Variables
    pie = 4
    denominator = 3
    counter = 1 # Use to change the arithmetic operator
    
    # Loop through if pie is > math.pi()
    # while pie > math.pi:
    for i in range(terms):
        # Change the arithmetic operator each iteration
        if counter % 2 == 1:
            pie -= (4 / denominator)
        else:
            pie += (4 / denominator)
        
        # Print the data to the table
        print(f'{counter:>4}{pie:>16.6f}')
        
        # Update variables
        counter += 1
        denominator += 2
    
    # Return the value once pie <= math.pi()
    print() # Seperate final pie value from table
    print(pie)

approx_pie()




#3.15
def fact_2(n):
    if n < 2:
        return 1
    return n * fact_2(n - 1)


def approx_e():
    # User input - Iterations to be completed
    iterations = int(input('How many iterations do you want? '))
    
    # Variables
    e = 1
    fact_counter = 1
    
    for i in range(iterations):
        e += (1 / fact_2(fact_counter))  # Use the factorial function
        fact_counter += 1
    
    return e 

print(approx_e())




#3.16
def two_largest_nums(lyst):
    # Sort the list in place
    lyst.sort()
    # Return the -1 and -2 indexes
    return lyst[-1], lyst[-2]

print(two_largest_nums([13, 56, 345, 654, 786, 65, 456, 123, 6547, 765]))




#3.17 - It's ugly but got the job done
for i in range(1):
    for j in range(10):
        print('*' * j)
    print()
    
    for k in range(10, 0, -1):
        print('*' * k)
    print()
    
    num_spaces = 0
    for l in range(10, 0, -1):
        star = '*'
        space = ' '
        print(f'{space * num_spaces}{star * l}')
        num_spaces += 1
    
    print()
    num_spaces = 9
    for l in range(1, 11):
        star = '*'
        space = ' '
        print(f'{space * num_spaces}{star * l}')
        num_spaces -= 1




#3.18 - Code looks uglier than the last (3.17) but was a hard one for me to code out. Needs rethinks or at the minimum refactoring.
# Variables
a_d_asterisks = 1
a_d_spacers = 9

b_c_asterisks = 10
b_c_spacers = 0

space = ' '
print_spacer = '   ' # Spacer between a, b, c, and d
a = b = c = d = '*'  # Assign each print a, b, c, and d

# One main for loop that iterates 10 times
for i in range(1, 11):
    print(f'{a * a_d_asterisks}{space * a_d_spacers}{print_spacer}', end='')
    print(f'{b * b_c_asterisks}{space * b_c_spacers}{print_spacer}',end='')
    print(f'{space * b_c_spacers}{c * b_c_asterisks}{print_spacer}', end='')
    print(f'{space * a_d_spacers}{d * a_d_asterisks}{print_spacer}')
    
    # Increment or decrement a counter for each print (a, b, c, and d)
    a_d_asterisks += 1
    a_d_spacers -= 1

    b_c_asterisks -= 1
    b_c_spacers += 1




#3.19
side1 = 1
side2 = 1

# First loop - hypotenuse
for h in range(1, 21):
    if (side1 ** 2 + side2 ** 2) == (h ** 2):
        print([side1, side2, h])
        
    # Second loop - side2
    for side2 in range(1, 21):
        if (side1 ** 2 + side2 ** 2) == (h ** 2):
            print([side1, side2, h])
        
        # Third loop - side1
        for side1 in range(1, 21):
            if (side1 ** 2 + side2 ** 2) == (h ** 2):
                print([side1, side2, h])




#3.20
def binary_to_decimal(binary_num):
    """Returns a binary num input to decimal output."""
    total_sum = 0
    binary_decimal = [2 ** i for i in range(8, -1, -1)]
    
    for idx, digit in enumerate(str(binary_num)):
        if int(digit) == 1:
            total_sum += binary_decimal[idx]
    
    return total_sum

print(binary_to_decimal(111111111))


#3.21 - I couldn't solve it using float values even after 3hrs. Pennies kept going to 2 instead of 3. Even using round(change) which = 0.03 kept on returning 2 for total_coins = change // coin_to_return[coin]. In the end I had to use digit/int() values to get it to work. 
def change_of_coins():
    # Input purchase price of a dollar or less and deduct one dollar
    change = int(100 - (float(input('Enter the purchase price of the item: ')) * 100))
    
    # Coin values
    coin_to_return = {'penny': 1, 'nickel': 5, 'dime': 10, 'quarter': 25}
    
    # Print the header
    print('Your change is: ')
    
    # Iterate through each coin
    for coin in ['quarter', 'dime', 'nickel', 'penny']:
        # check if change >= a coin value
        if change >= coin_to_return[coin]:
            # Check to see how many times that coin can be divided by
            total_coins = change // coin_to_return[coin]
            # Deduct the change by the total number of coins above
            change -= total_coins * coin_to_return[coin]
            print(f'{total_coins} {coin}s')

change_of_coins()




#3.22
for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)
    if value == -1:
        break
else:
    print('The loop terminated without executing the break')




#3.23 - Coded out. Created a new file and completed in the terminal




#3.24 - Completed through the terminal




#3.25





#3.26 - Completed




#3.27 
# Current population = 7_882_801_850
# Current population growth rate = 1.04%
# Print table header - Year (1-100), total pop estimate for end of year, pop increase that year

print('Year    Total Population   Poplation Increase')
total_pop = 7_882_801_850
pop_increase = 0
growth_rate = 0.0104

for year in range(2021, (2021 + 101)):
    pop_increase = total_pop * growth_rate
    total_pop += pop_increase
    
    print(f'{year:>3}{total_pop:>21,.0f}{pop_increase:>18,.0f}')




#3.28
values = [9, 11, 22, 34, 17, 22, 34, 22, 40]

def return_values(lyst):
    mean = statistics.mean(lyst)
    median = statistics.median(lyst)
    mode = statistics.mode(lyst)
    
    return [mean, median, mode, sorted(lyst)]

# Mode is 22
print(return_values(values)) 

# Mode could be either 22 or 34 but returns 22
print(return_values(values + [34])) 




#3.29
# I don't see a problem if the two values are different as they are summed and divided by 2 to return the average.




#3.30
# Mean is most effected as it has the greatest effects on it's value than the others. Mode is least effected as it's only returning the most common value.




#3.31
# I don't understand the question but assume the answer is - "Dog type" as they are all breads of dogs.