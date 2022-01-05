from itertools import combinations
import random 
import operator
import re 

# 8.1  - Check protection
# def check_protection(amount):
#     """Take in a dollar amount and return the pay in a 10 character width with * used for any blank spaces."""
#     format_amount = f'{amount:,.2f}'
#     amount_length = len(format_amount)
    
#     if amount_length < 10:
#         spaces = '*' * (10 - amount_length)
#         return f'{spaces}{format_amount}'
#     else:
#         return f'{format_amount}'

# print(check_protection(4399.87))


# def check_protection2(amount):
#     """Take in a dollar amount and return the pay in a 10 character width with * used for any blank spaces."""
#     return f'{amount:*>10,.2f}'


# print(check_protection2(4399.87))


# 8.2 - Random sentences
# article = 'It seems the pip team might be trying to push us into applying custom patches. This is not a long term solution at all and is not something we want to maintain in the long run.'.split()

# noun = 'mother, father, baby, child, toddler, teenager, grandmother, student, teacher, minister, businessperson, salesclerk, woman, man, lion, tiger, bear, dog, cat, alligator, cricket, bird, wolf'.split(', ')

# verb = 'Am, is, are, was and were, being, been, and be, Have, has, had, do, does, did, will, would, shall'.split(', ')

# prepostion = 'about, above, according to, across, after, against, ahead of, along, amid, amidst, among, around, as, as far as, as of, aside from, at, athwart, atop'.split(', ')

# def compose_sentence(lyst):
#     sentence = [words[random.randint(0, len(words) - 1)] for words in lyst]
#     return ' '.join(sentence)

# print(compose_sentence([article, noun, verb, prepostion, article, noun]))

# def print_sentences(sentence_func, lyst):
#     counter = 0
#     for sentence in range(1, 21):
#         counter += 1
#         if counter == 20:
#             print(f'{sentence_func(lyst).capitalize()}.')
#         else: 
#             print(sentence_func(lyst))

# print_sentences(compose_sentence, [article, noun, verb, prepostion, article, noun])




# 8.3 - Pig latin
# def pig_latin(word):
#     # If the word being with a vowel only add 'ay' to the end
#     if word[0] in ['aeiou']:
#         return f'{word}ay'
#     # Else move the first character to the end and add 'ay' 
#     return f'{word[1:]}{word[0]}ay'

# for word in ['jump', 'the', 'computer']:
#     print(pig_latin(word))

# for word in article:
#     print(pig_latin(word))




# 8.4 - Reversing a sentence
# def reverse_sentence(words):
#     sentence = words.split(' ')
#     return ' '.join([word for word in sentence[::-1]])

# print(reverse_sentence('Dean is the best'))




# 8.5 - Tokenizing and comparing strings
# def token_strings(sentence, char):
#     return ' '.join([word for word in sentence.split(' ') if word[0] == char])

# print(token_strings('be right back. Just coding the bad ass sentence', 'b'))




# 8.6 - Tokenizing and comparing strings
# def token_strings_2(sentence:str, chars:str):
#     return ' '.join([word for word in sentence.split(' ') if word[-2:] == chars])

# print(token_strings_2('clocked off are red day.', 'ed'))




# 8.7 - Converting  integers to characters
# def int_to_chars():
#     for i in range(256):
#         print(f'{i}: {i:c}')

# int_to_chars()




# 8.8 - Converting integers to emojis
# Doesn't interest me this one




# 8.9 - Creating three letter strings froma five-letter word
# def possible_combos(string, length):
#     combos = combinations(string, length)
    
#     return '\n'.join([''.join(i) for i in combos])

# print(possible_combos('dean', 3))




# 8.10 - Project: Simple sentiment analysis
# def file_to_list(filename):
#     """Takes in a filename and returns a list of words"""
#     sentiment = []
#     with open(filename, mode='r') as words:
#         for word in words:
#             if word.endswith('\n'):
#                 sentiment.append(word[:-1])
#             else:
#                 sentiment.append(word)
    
#     return sentiment

# positive_sentiment = file_to_list('positive_words.txt')
# negative_sentiment = file_to_list('negative_words.txt')

# def sentiment_analysis(positive, negative):
#     p, n = 0, 0
#     tweet = input('Enter the Tweet you want analysed: ')
    
#     for word in tweet.split():
#         if word in positive:
#             p += 1
#         if word in negative:
#             n += 1

#     if p == n:
#         return 'Sitting on the fence'
#     elif p > n:
#         return 'Positive sentiment'
#     return 'Negative sentiment'

# print(sentiment_analysis(positive_sentiment, negative_sentiment))




# 8.11 - Project: Evaluate word problems
# def operator_problems():
#     question = input('Enter the equation to be sovled: ').split()
#     left_op, operator_type, right_op = question[0], ' '.join(question[1: -1]), question[-1]
    
#     nums_to_words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
#                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
#     operators = {'plus': operator.add, 'minus': operator.sub,
#                  'times': operator.mul, 'divided by': operator.truediv}
    
#     return operators[operator_type](int(nums_to_words[left_op]), int(nums_to_words[right_op]))

# print(operator_problems())




# 8.12 - Project: Scrambled text
# def scrambe_text():
#     # Enter the word to be scrambled
#     word = input('Enter the word to be scrambled: ')
    
#     # Variables for the first and last characters
#     first, last = word[0], word[-1]
    
#     # Variable for the characters to be scrambled and scramble them
#     middle = random.shuffle(list(word[1:-1]))
    
#     # Return the first, scrambled and last character as a string
#     return f'{first}{middle}{last}'

# print(scrambe_text())




# 8.13 - Condense spaces to a single space
# def condense_spaces():
#     # Enter the word to be condensed
#     sentence = input('Enter the sentence to be condensed: ')
    
#     # Return the condensed string
#     return ' '.join(re.split(r'\s+', sentence))

# print(condense_spaces())




# 8.14 - Capturing substrings
# def capture_substrings(sentence):
#     for word in re.split(r'\s+', sentence):
#         result = re.search(r'[b][a-z]*', word)
#         if result:
#             print(result.group())

# sentence = 'bet this doesnt work for b but instead for char bet you'
# capture_substrings(sentence)


# def capture_substrings_2(sentence):
#     for word in re.split(r'\s+', sentence):
#         result = re.search(r'ed$', word)
#         if result:
#             print(word)


# sentence_2 = 'bet this deed doesnt work. It need to but bet haved'
# capture_substrings_2(sentence_2)




# 8.15 - Counting characters and words
# def counting(string):
#     digits = len(re.findall(r'\d', string))
#     non_digits = len(re.findall(r'[^0-9\s]', string))
#     spaces = len(re.findall('\s', string))
#     words = len(re.findall('[\W]', string))
    
#     return digits, non_digits, spaces, words

# print(counting('69 isst'))




# 8.16 - Locating URL's
# url1 = 'http://www.ednoftheworld.com.au'

# def confirm_url(url):
#     protocol = True if re.match(r'http://www.', url) else False 
#     organisation = True if re.match(r'[a-z]{2}', url) else False 
#     print(protocol, organisation)

# confirm_url(url1)




# 8.17 - Matching numeric values
# def match_numeric_values():
    # num can have any number of digits
    # only digits and a decimal point (optional)
    # if the decimal appears there can only be one and must have a digit either side of it
    # there should be whitespace or a beginning or end of line character on either side of a valid number
########## TOO HARD BASEKT FOR THIS ONE ################




# 8.18 - Password format validator
# def password_validator1(string):
#     return 'Valid password' if re.fullmatch(r'\w+[.,_]{1}\w+[.,_]{1}\w+[.,_]{1}', string) else 'Not a valid password'

# print(password_validator1('Dean_is,the.'))


# def password_validator2(string):
#     return 'Valid password' if re.fullmatch(r'[A-Z+a-z+0-9+!@#$%<^>&*?]{8,}', string) else 'Not a valid password'


# print(password_validator2('Dean_9?is,the.'))




# 8.19 - Done




# 8.20 - Munging dates - Not doing it



#  8.21 - Metric conversions
