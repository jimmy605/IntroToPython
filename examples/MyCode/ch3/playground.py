from decimal import Decimal
import statistics

# Concise conditional expression
grade = 69
result = 'Passed' if grade >= 70 else 'Failed\nYou must take this course again'
# print(result)


product = 7

while product <= 1_000:
    product *= 7
print(product)


for char in 'Programming':
    print(char, end='  ')
print()


# Printing numbers and seperating the values
print(10, 20, 30, sep='.....')


# Adding up numbers from a list and printing the total
total = 0

for num in [2, -3, 0, 17, 9]:
    total += num
print(total)


for counter in range(10):
    print(counter, end=' ')
print()


# Calc the total of 0 - 1_000_000
total_two = 0

for num in range(1_000_001):
    total_two += num 
print(total_two)


x = 12
x **= 2
print(x)


# for num in range(2):
#     check_num = int(input('Enter a number to check if its odd or even: '))
    
#     if check_num % 2 == 0:
#         print(f'{check_num} is even')
#     else:
#         print(f'{check_num} is odd')


total = 0
for num in range(2, 101, 2):
    total += num 
print(total)


principal = Decimal('1000.00')
rate = Decimal('0.05')


print(f'Your bill is ${Decimal(37.45) * Decimal(1.0625):.2f}')


grades = [85, 93, 45, 89, 85]
print(statistics.mean(grades), statistics.median(grades), statistics.mode(grades))

nums = [47, 95, 88, 73, 88, 84]
print(statistics.mean(nums), statistics.median(nums), statistics.mode(nums))
