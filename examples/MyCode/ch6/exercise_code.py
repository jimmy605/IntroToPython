from collections import Counter 
import string 

# 6.1 Dictionary methods



# 6.2 - What's wrong with this code?
# text = ('To be or not to be that is the question')
# counter = Counter(text.split())

# for word, count in sorted(counter.items()):
#     print(f'{word:<12}{count}')




# 6.2 - What does this code do?
# temperatures = {
#     'Monday': [66, 70, 74],
#     'Tuesday': [50, 56, 64],
#     'Wednesday': [75, 80, 83],
#     'Thursday': [67, 74, 81]
# }
# # Prints the average temperature for each day to 2 decimal places
# for k, v in temperatures.items():
#     print(f'{k}: {sum(v) / len(v):.2f}')




# 6.4 - Fill in the missing code
# print({1, 2, 4, 8, 16} | {1, 4, 16, 64, 256}) # Union
# print({1, 2, 4, 8, 16} & {1, 4, 16, 64, 256}) # Intersection
# print({1, 2, 4, 8, 16} - {1, 4, 16, 64, 256}) # Difference
# print({1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256}) # Symmetric difference
# print({1, 2, 4, 8, 16} <= {1, 4, 16, 64, 256}) # Improper subset




# 6.5 - Counting duplicate words
# sentence = 'See how many words you can see in the sentence and return how many words'
# word_count = {}

# for word in sentence.split():
#     if word.lower() in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word.lower()] = 1

# for word, count in word_count.items():
#     print(f'{count}: {word}')




# 6.6 - Duplicate word removal
# def word_removal(word_list):
#     sorted_list = sorted(set([word.lower() for word in word_list.split()]))
    
#     for word in sorted_list:
#         print(word)

# word_removal(sentence)




# 6.7 - Character counts
# def character_table():
#     sentence = input('Enter a sentence to count the characters: ')
#     letter_count = {}
    
#     # Iterate over each word in the list
#     for word in sentence.split():
#     # Iterate over each character in the word
#         for char in word:
#             if char.lower() in letter_count:
#                 letter_count[char.lower()] += 1
#             else:
#                 letter_count[char.lower()] = 1
    
#     # Print the header for the table
#     print(f'{"Char"}{"Count":>8}')
    
#     # Iterate through the dict
#     for letter in sorted(letter_count.keys()):
#         print(f'{letter:>2}{letter_count[letter]:>8}')
    
#     # Workout the letters not used in the sentence and print them as a string or similar
#     # Need the alphabet
#     alphabet = string.ascii_lowercase
#     # List of letters not in letter_count
#     not_in_letter_count = list(set(alphabet) - set(letter_count.keys()))
    
#     for letter in sorted(not_in_letter_count): print(letter, end=', ')

# character_table()




# 6.8 - Writing the word equivalent of a check amount
# def num2words(num): 
#     under_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
#     tens = ['Twenty', 'Thirty', 'Forty', 'Fifty','Sixty', 'Seventy', 'Eighty', 'Ninety']
#     above_100 = {100: 'Hundred', 1000: 'Thousand'}
#     word_amount = ''
#     num_string = str(num)
#     cents = num_string[4:]
    
#     # Check if the number is 100
#     if num == 100:
#         return 'One hundred'
#     # Check in num is over 100
#     else:
#     # Use the first digit of the number as the index for under_20[digit]
#         word_amount += f'{under_20[int(num_string[0])]} Hundred '
    
#     # Check if the remaining digits are < 20
#     if int(num_string[1:3]) < 20:
#         word_amount += f'{under_20[int(num_string[1:3])]} And {cents}/100'
#         return word_amount
#     else:
#         # Take index 1 value and minus 2 off it 
#         teen_digit = int(num_string[1]) - 2
#         ten_digit = int(num_string[2])
#         word_amount += f'{tens[teen_digit]} {under_20[ten_digit]} And {cents}/100'
#         return word_amount

# print(num2words(112.43))
# print(num2words(100))
# print(num2words(142.43))




# 6.9 - Dictionary manipulations
# tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# # a)
# print('Canada' in tlds)

# # b)
# print('France' in tlds)

# # c)
# for country, code in tlds.items():
#     print(f'{country}: {code}')

# # d)
# tlds.update({'Sweden': 'sw'})
# print(tlds)

# # e)
# tlds['Sweden'] = 'se'
# print(tlds)

# # f)
# reverse_tlds = {value: key for key, value in tlds.items()}
# print(reverse_tlds)

# # g)
# upper_tlds = {key: value.upper() for key, value in reverse_tlds.items()}
# print(upper_tlds)




# 6.10 - Set manipulation
# one = {'red', 'green', 'blue'}
# two = {'cyan', 'green', 'blue', 'magenta', 'red'}

# # Union - Returns elements from both sets
# print(one | two)

# # Intersection - returns the elements that are common in both sets
# print(one & two)

# # Set difference - Returns elements that are only in two but not one
# print(two - one)

# # Symmetric difference - 
# print(one ^ two)




# 6.11 - Analyzing the game of craps. Completed in file "craps.py"




# 6.12 - Translation dictionary
# translations = {'Dean': 'Dekan', 'Cat': 'Kucing', 'Ball': 'Bola', 'Car': 'Mobil'}

# # Print header for translations
# print(f'{"English"}{"Translated":>12}')

# for word, translated in translations.items():
#     print(f'{word:>6}{translated:>11}')




# 6.13 - Synonyms dictionary
# Not sure what the question wants




# 6.14 - 6.16 Not sure how to complete




# 6.17 - Cooking with healthier ingredients
