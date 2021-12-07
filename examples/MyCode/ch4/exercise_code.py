import datetime
import random 

# 4.5 
# def seconds_since_midnight(h, m, s):
#     hour_in_seconds = h * 60 * 60
#     minute_in_seconds = m * 60
#     return sum([hour_in_seconds, minute_in_seconds, s])

# print(seconds_since_midnight(13, 30, 45))




# 4.6 - Modify average function
# def average(num, *args):
#     if len(args) < 0:
#         return num

#     return (sum(args) + num) / (len(args) + 1)

# print(average(2, 1, 2, 3, 4, 6))




# 4.7 - date and time
# def date_and_time():
#     time  = datetime.datetime.today()
#     print(time)

# date_and_time()




# 4.8 - rounding numbers
# def round_num(number, places):
#     return round(number, places)

# print(round_num(13.56449, 1))




# 4.9 - temperature conversion
# def fahrenheit():
#     """Print out a celcis to fahrenheit table."""
    
#     # Print out the table header
#     print(f'Celcius    fahrenheit')
    
#     for celcius in range(0, 101):
#         fahren = (9 /5) * celcius + 32
#         print(f'{celcius:>5}{fahren:>14.1f}')

# fahrenheit()




# 4.10 - guess the number
# def guessing_game():
#     """Number guessing game."""
#     guess_range = int(input('Enter the end range to guess too: '))
#     answer = random.randrange(1, guess_range)
    
#     flag = True 
#     while flag:
#         guess = int(input('Enter your guess here: '))
        
#         if guess == answer:
#             print('Congratulations. You guessed the number!')
#             flag = False 
#         elif guess > answer:
#             print('Too high. Try again.')
#         else:
#             print('Too low. try again.')
    
#     replay = input('Do you want to play again (yes or no)? ')
#     if replay in ['yes', 'YES', 'y', 'Y']:
#         print()
#         guessing_game()
#     else:
#         print('Thanks for playing.')

# guessing_game()




# 4.11
# def guessing_game_2():
#     """Number guessing game."""
#     guess_range = int(input('Enter the end range to guess too: '))
#     answer = random.randrange(1, guess_range)
#     guess_count = 0
#     print(answer)

#     flag = True
#     while flag:
#         guess = int(input('Enter your guess here: '))
#         guess_count += 1
        
#         if guess == answer:
#             if guess_count < 11:
#                 print()
#                 print('Either you know the secret or you got lucky!')
#                 print('Congratulations. You guessed the number!')
#             else:
#                 print()
#                 print('Congratulations. You guessed the number!')
#                 print('You should be able to do better!')
#             flag = False
            
#         elif guess > answer:
#             print('Too high. Try again.')
            
#         else:
#             print('Too low. try again.')

#     replay = input('Do you want to play again (yes or no)? ')
#     if replay in ['yes', 'YES', 'y', 'Y']:
#         print()
#         guessing_game_2()
#     else:
#         print('Thanks for playing.')


# guessing_game_2()




# 4.12 - the tortoise and the hare
# def tortoise():
#     random_num = random.randrange(1, 11)
    
#     if random_num <= 5:
#         return 3
#     elif random_num <= 7:
#         return -6
#     else:
#         return 1

# def hare():
#     random_num = random.randrange(1, 11)

#     if random_num <= 2:
#         return 0
#     elif random_num <= 4:
#         return 9
#     elif random_num <= 5:
#         return -12
#     elif random_num <= 8:
#         return 1
#     else:
#         return -2

# def race():
#     """Racing game between two animals."""
    
#     # Print out the starting display
#     print('BANG !!!!!')
#     print('AND THEYRE OFF!!!!!')
    
#     # Tally or each animal
#     tortoise_count = 0
#     hare_count = 0
    
#     # While both animals are < 70
#     while tortoise_count < 71 and hare_count < 71:
#         tortoise_count += tortoise()
#         hare_count += hare()
#         spaces = ' '
        
#         if tortoise_count == hare_count:
#             print(f'{spaces * tortoise_count}OUCH!!!')
#         else:
#             print(f'{spaces * (tortoise_count - 1)}T')
#             print(f'{spaces * (hare_count - 1)}H')
        
#         tortoise_count += tortoise()
#         hare_count += hare()
    
    
#     if tortoise_count > 70 and hare_count > 70:
#         print('Its a tie')
#     elif tortoise_count > 70:
#         print('TORTOISE WINS!!! YAY!!!')
#     elif hare_count > 70:
#         print('Hare wins. Yuch.')

# race()




# 4.13 - Arbitrary argument list
# def product(*nums):
#     output = 1
#     for num in nums:
#         output *= num 
    
#     return output

# print(product(1,2,3,4,5))




# 4.14 - Computer-assisted instruction
# def number_generator():
#     n1 = random.randrange(1, 10)
#     n2 = random.randrange(1, 10)
    
#     return (n1, n2)


# def multiplication():
#     """Pick 2 random positive numbers less than 10 and ask the user what the answer is if we multiple these numbers together."""
#     n1, n2 = number_generator()
#     question = int(input(f'How much is {n1} times {n2}? '))
#     answer = n1 * n2 
    
#     while question != answer:
#         print('No. Please try again.', end='\n')
#         question = int(input(f'How much is {n1} times {n2}? '))
#     else:
#         print('Very good!', end='\n')
#     multiplication()

# multiplication()

# 4.15 - Conmputer assisted instruction reducing student fatigue


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

#     while question != answer:
#         print(f'{incorrect_answers[random.randrange(0,len(incorrect_answers))]}', end='\n')
#         question = int(input(f'How much is {n1} times {n2}? '))
#     else:
#         print(
#             f'{correct_answers[random.randrange(0,len(correct_answers))]}', end='\n')
#     multiplication()

# multiplication()



# 4.16 - Computer assisted instruction difficult levels
# def number_generator():
#     level = int(input('Enter the difficulty level (1 or 2): '))
    
#     if level == 1:
#         n1 = random.randrange(1, 10)
#         n2 = random.randrange(1, 10)
#     else:
#         n1 = random.randrange(1, 100)
#         n2 = random.randrange(1, 100)

#     return (n1, n2)


# def multiplication():
#     """Pick 2 random positive numbers less than 10 and ask the user what the answer is if we multiple these numbers together."""
#     n1, n2 = number_generator()
#     question = int(input(f'How much is {n1} times {n2}? '))
#     answer = n1 * n2
    
#     correct_answers = ['Very good!', 'Nice work!', 'Keep up the good work!']
#     incorrect_answers = ['No. Keep trying',
#                          'No. Please try again.', 'Wrong. Try once more.']

#     while question != answer:
#         print(
#             f'{incorrect_answers[random.randrange(0,len(incorrect_answers))]}', end='\n')
#         question = int(input(f'How much is {n1} times {n2}? '))
#     else:
#         print(
#             f'{correct_answers[random.randrange(0,len(correct_answers))]}', end='\n')
#     multiplication()


# multiplication()




# 4.17 - compter assisted instruction varying the tupes of problems
# def arithmetic():
#     for n in ['1 +', '2 -', '3 *', '4 /', '5 + - * /']:
#         print(n)
    
#     type = int(input('Enter the arithmetic type number: '))

# def number_generator():
#     level = int(input('Enter the difficulty level (1 or 2): '))

#     if level == 1:
#         n1 = random.randrange(1, 10)
#         n2 = random.randrange(1, 10)
#     else:
#         n1 = random.randrange(1, 100)
#         n2 = random.randrange(1, 100)

#     return (n1, n2)


# def multiplication():
#     """Pick 2 random positive numbers less than 10 and ask the user what the answer is if we multiple these numbers together."""
#     n1, n2 = number_generator()
#     question = int(input(f'How much is {n1} times {n2}? '))
#     answer = n1 * n2

#     correct_answers = ['Very good!', 'Nice work!', 'Keep up the good work!']
#     incorrect_answers = ['No. Keep trying',
#                          'No. Please try again.', 'Wrong. Try once more.']

#     while question != answer:
#         print(
#             f'{incorrect_answers[random.randrange(0,len(incorrect_answers))]}', end='\n')
#         question = int(input(f'How much is {n1} times {n2}? '))
#     else:
#         print(
#             f'{correct_answers[random.randrange(0,len(correct_answers))]}', end='\n')
#     multiplication()


# arithmetic()