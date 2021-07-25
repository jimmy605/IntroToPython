import string 

#2.5
pie, r = 3.14159, 2
diameter, circ, area = 2 * r, 2 * pie * r, pie * r ** 2
print(f'diameter: {diameter}, circumference: {circ}, area: {area}')

#2.6
num = int(input('Enter a number: '))
print('even' if num % 2 == 0 else 'Odd')


#2.8
def square_cubes(num):
    """Table of the squares and cubes of 'num'."""
    print(f'Number    Square    Cube')
    
    for n in range(num):
        number, square, cube = n, n * n, n ** 3 
        print(f'{number:>3}    {square:>6}    {cube:>6}')

square_cubes(6)


#2.9
def ord_total():
    alphabet_lower = string.ascii_lowercase
    return sum([ord(n) for n in alphabet_lower])

print(ord_total())


#2.10
def display_data(num):
    nums = []

    for n in range(num):
        user_num = int(input('Enter a number: '))
        nums.append(user_num)
    
    print(f'Sum: {sum(nums)}, Average: {sum(nums) / len(nums)}\
, Product: Not coding, Smallest: {min(nums)} and Max: {max(nums)}')

display_data(3)


#2.11
def seperate_num(num):
    """Seperate each digit in num by 3 spaces."""
    return '   '.join(list(str(num)))

print(seperate_num(42339))


#2.12
def investment_return(principal, rate, years):
    """Returns the return on the investment."""
    return f'${principal * (1 + rate) ** years:.2f}'

print(investment_return(1_000, 0.07, 20))


#2.13
def big_integers(exponent_end):
    for n in range(exponent_end):
        print(2 ** n)

big_integers(1000)

#2.14
def target_hr():
    user_age = int(input('Enter your age: '))
    max_hr = 220 - user_age
    min_target = int(max_hr * 0.50)
    max_target = int(max_hr * 0.85)
    
    return f'Your maximum HR is: {max_target}BPM\nTraining range: {min_target}-{max_target}BPM'

print(target_hr())


#2.15
def sort_ascending(total_nums):
    nums = [] # Store the floats returned from user input
    
    for n in range(total_nums):
        n = input('Enter floating point number: ')
        nums.append(n) # Store in nums
    
    return sorted(nums)

print(sort_ascending(3))