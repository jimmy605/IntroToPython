from decimal import Decimal
import statistics

# """
# Determine the first power of 7 greater than 1000.
# """
# product = 7

# while product < 1000:
#     product *= 7

# print(product)


# for character in 'Programming':
#     print(character, end='  ')
# print()


# print(10, 20, 30, sep=', ')


# total = 0
# for num in range(1_000_001):
#     total += num

# print(f'{total:,}')




# for num in range(2):
#     number = int(input('Enter a number: '))
    
#     if number % 2 == 0:
#         print(f'{number} is even')
#     else:
#         print(f'{number} is odd')




# for num in range(99, -1, -11):
#     print(num, end=' ')



# principal = Decimal('1000.00')
# print(principal)

# rate = Decimal('0.05')
# print(rate)

# x = Decimal('10.5')
# y = Decimal('2')

# print(x + y)


# for year in range(1, 11):
#     a = principal * ( 1 + rate) ** year
#     print(f'{year:>2}: {a:>10.2f}')


# bill_rate = Decimal('0.0625')
# amount = Decimal('37.45')
# print(f'{amount * (1 + bill_rate):.2f}')


grades = [85, 93, 45, 89, 85]
# mean_val = sum(grades) / len(grades)
# print(mean_val)


print(statistics.mean(grades))

values = [47, 95, 88, 73, 88, 84]

print('Mean:', statistics.mean(values))
print('Mode:', statistics.mode(values))
print('Median:', statistics.median(values))