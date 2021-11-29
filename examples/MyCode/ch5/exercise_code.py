import string 
import itertools
from collections import deque
from decimal import Decimal
import operator
import random 

# 5.3 - Fill in the missing code
# lyst = [(x, x * 0.0254) for x in [69, 77, 54]]
# print(lyst)
# print(list(map(lambda x: (x, x * 0.0254), [69, 77, 54])))




# 5.4 - Iteration order
# lyst = [[10,9,8], [7,6,5]]
# count = 0

# for i, row in enumerate(lyst):
#     for j, item in enumerate(row):
#         lyst[i][j] = count
#         count += 1

# # Print the header
# print('Column1  Column2  Column3')
# for row in lyst:
#     for item in row:
#         print(f'{item:>6}', end=' ')
#     print()




# 5.5 - Slicing
# alphabet = string.ascii_lowercase

# a) First half of the string
# print(alphabet[:len(alphabet) // 2])

# b) First half of the string using only the ending index
# print(alphabet[:len(alphabet) // 2])

# c) Second half of the string
# print(alphabet[len(alphabet) // 2:])

# d) As c
# print(alphabet[len(alphabet) // 2:])

# e) Every second letter in the string starting with 'a'
# print(alphabet[::2])

# f) Entire string in reverse
# print(alphabet[::-1])

# g) Every third letter of the string in reverse starting with 'z' 
# print(alphabet[::-3])





# 5.6 - Functions returning tuples
# def rotate(a, b, c):
#     return (c, a, b)

# print(rotate('Doug', 22, 1984))




# 5.7 - Duplicate elimination
# def duplicates(lyst):
#     output = []
    
#     for item in lyst:
#         if item not in output:
#             output.append(item)
    
#     return sorted(output)

# names = ['Dean', 'Connor', 'Stacey', 'Noah', 'Dean']

# print(duplicates(names))




# 5.8 - Sieve of eratosthenes
# primes = [True for item in range(1_000)]

# for i, element in enumerate(primes[:]):
    
#     if i > 1 and element:
#         for item in range(i + 1, len(primes)):
#             if item % i == 0:
#                 primes[item] = False 

# for i, element in enumerate(primes):
#     if i > 1 and element:
#         print(i, end=', ')




# 5.9 Palindrome tester
# def is_palindrome(s):
#     reverse_s = s[::-1]
#     return True if s.lower() == reverse_s.lower() else False 

# # OR
# def is_palindrome_2(s):
#     processed = []
    
#     for element in s:
#         if element.isalpha():
#             processed.append(element)
    
#     string_processed = ''.join(processed) # Change the list into a string
#     reverse_processed = string_processed[::-1] # Reverse the string
    
#     return True if string_processed.lower() == reverse_processed.lower() else False

# print(is_palindrome_2('Dean s !! the best'))
# print(is_palindrome_2('Radar'))
# print(is_palindrome_2('radar'))




# 5.10 - Anagrams
# def anagram(s):
#     count = 0
#     result = itertools.permutations(s)
#     for item in result:
#         count += 1
#         print(item)
    
#     print(f'There was a total of {count} different permutations.')

# anagram('Dean')




# 5.11 - Summarizing letters in a string
# def summarize_letters(s):
#     # Empty list to store tuples (letter, frequency)
#     data = []
#     alphabet = list(string.ascii_lowercase)
    
#     # Iterate through s
#     for letter in s:
        
#         # Check its a letter and not a space or punctuation
#         if letter.isalpha():
#             # Change the letter to lower case
#             lower_letter = letter.lower()
            
#             if lower_letter in alphabet:
#                 # Pop the letter from the alphabet list
#                 alphabet.remove(lower_letter)
                
#                 # Count the frequency it appears
#                 count = list(s.lower()).count(lower_letter)
#                 data.append((lower_letter, count))
    
#     if alphabet:
#         return 'The string does not have all the alphabet letters.'
    
#     return 'The string has all the alphabet letters.'

# print(summarize_letters('Desan" lmnopqrstuvwxyz  ssabcdefghiljk'))





# 5.12 - Telephone-number word generator
# L = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",'8':"tuv",'9':"wxyz"}
# # Another way below (stolen also)

# # Function to return a list that contains all the generated letter combinations
# def letter_combinations_util(number, n, table):
    
#     lyst = []
#     q = deque()
#     q.append("")
    
#     while len(q) != 0:
#         s = q.pop()
        
#         # If complete word is generated push it in the list
#         if len(s) == n:
#             lyst.append(s)
#         else:
#             # Try all possible letters for current digit in number[]
#             for letter in table[number[len(s)]]:
#                 q.append(s + letter)
    
#     # Return the generated lyst
#     return lyst


# # Function that creates the mapping and calls letter_combinations_util
# def letter_combinations(number, n):

#     table = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
#     lyst = letter_combinations_util(number, n, table)
    
#     s = ""
#     for word in lyst:
#         s += word + " "
    
#     print(s)
#     return 

# # Driver code
# number = [2, 3]
# n = len(number)

# # Function call
# letter_combinations(number, n)

# 5.13 - Word or phrase to phone number generator
# This one is too hard also




# 5.14 - Is a sequence sorted?
# def is_ordered(seq):
#     # Create a copy of seq and sort it
#     sorted_seq = sorted(seq)
    
#     # Iterate through seq and check it matches with the sorted_seq above 
#     for i, item in enumerate(seq):
#         if item != sorted_seq[i]:
#             return False 
    
#     return True 

# num_sorted = [1,2,3,4,5]
# num_not_sorted = [2,4,3,1,5]

# print(is_ordered(num_sorted))
# print(is_ordered(num_not_sorted))





# 5.15 - Tuples representing invoices
# a)
# hardware_data = ((83, 'Electric sander', 7, 57.98),
#                 (24, 'Power saw', 18, 99.99),
#                 (7, 'Sledge hammer', 11, 21.50),
#                 (77, 'Hammer', 76, 11.99),
#                 (39, 'Jig saw', 3, 79.50))

# for part in sorted(hardware_data, key=operator.itemgetter(1)):
#     print(part[1])

# b)
# Header
# print('Part Number', 'Part Description', 'Qunatity', 'Price')

# for price in sorted(hardware_data, key=operator.itemgetter(3)):
#     part_num, description, quantity, cost = [item for item in price]
#     print(f'{part_num:>6}{description:>22}{quantity:>6}{cost:>9}')

# c) 
# check = map(lambda results: (results[2], results[1]), sorted(hardware_data, key=lambda x: x[2]))

# for item in check:
#     print(f'{item[1]} x {item[0]}')

# d)
# sort_price = map(lambda i: (i[1], i[2] * i[3]) ,sorted(hardware_data, key= lambda item: item[2] * item[3], reverse=True))

# for item in sort_price:
#     print(f'{item[0]} = ${item[1]:,.2f}')

# e)
# for item in filter(lambda price: price[1] > 200 and price[1] < 500, sort_price):
#     print(f'{item[0]} = ${item[1]:,.2f}')

# f)
# total = 0

# for item in sort_price:
#     total += item[1]

# print(f'The total for the invoice is ${total:,.2f}')




# 5.16 - Sorting letters and removing duplicates
# letters = 'abcdef'

# random_letters = [letters[random.randrange(0, len(letters))] for letter in range(0, 21)]

# a)
# ascending = sorted(random_letters)
# print(ascending)

# b)
# descending = sorted(random_letters, reverse=True)
# print(descending)

# c)
# unique_values = sorted(set(random_letters))
# print(unique_values)




# 5.17 - Filter/map performance
# a) The length of numbers

# b) 5 times or the number is odd numbers in the list

# c) The length of numbers




# 5.18 - Summing the triples of the even integers from 2 though 10
# lyst = [num for num in range(1, 11)]
# total = sum(map(lambda x: x * 3, 
#                 filter(lambda num: num % 2 == 0, lyst)))

# print(total)

# sum_total = sum([num * 3 for num in range(1, 11) if num % 2 == 0])
# print(sum_total)




# 5.19 - Finding the people iwth a specified last name
# names = [('Mary', 'Jones'), ('Tim', 'Davies'), ('Dean', 'Jones'), ('Connor', 'ONeill'), ('Samatha', 'Jones')]

# for name in filter(lambda i: i[1] == 'Jones', names):
#     print(f'{name[0]} {name[1]}')




# 5.20 - Display a two dimensional list in tabular format
# two_d_lyst = [[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]]

# def display_table(d_lyst):
#     """ 1    2    3    4
#     1   1    2    3    4
#     2   5    6    7    8
#     3   9   10   11   12
#     """
    
#     # Workout the column and row length 
#     column_length = len(d_lyst[0])
#     row_length = len(d_lyst)
    
#     # Print the header which will be the column indices
#     print('    ',end='')
#     for column in range(1, column_length + 1):
#         print(column, end='    ')
#     print()
    
#     # Iterate through the two d list
#     for i, row in enumerate(d_lyst):
#         print(i + 1, end='   ')
#         for j, column in enumerate(row):
#             if column > 9:
#                 print(column, end='   ')
#             else:
#                 print(column, end='    ')
#         print()

# display_table(two_d_lyst)




# 5.21 - Compter assisted instruction: Reducing student fatigue
# def number_generator():
#     n1 = random.randrange(1, 10)
#     n2 = random.randrange(1, 10)

#     return (n1, n2)


# def multiplication():
#     """Pick 2 random positive numbers less than 10 and ask the user what the answer is if we multiple these numbers together."""
#     n1, n2 = number_generator()
#     question = int(input(f'How much is {n1} times {n2}? '))
#     answer = n1 * n2

#     correct_answers = ['Very good!', 'Nice work!', 'Keep up the good work!']
#     incorrect_answers = ['No. Keep trying','No. Please try again.', 'Wrong. Try once more.']
#     responses = []
    
#     while question != answer:
#         responses.append(incorrect_answers[random.randrange(0,len(incorrect_answers))])
        
#         question = int(input(f'How much is {n1} times {n2}? '))
#     else:
#         responses.append(correct_answers[random.randrange(0, len(incorrect_answers))])
    
#     return responses

# responses = [multiplication() for i in range(5)]
# print(responses)




# 5.22 - Simulating a queue with a list
# enqueue - Join the queue
# dequeue - Get out of the line

lyst = [3,2,1]

def queue_list(nums):
    output = []
    
    for num in lyst[:]:
        output.append(num)
        print(num, end=' ... ')
    
    for num in output:
        dequeue = output.pop(0)
        print(dequeue, end=' ... ')

queue_list(lyst)