import datetime
import math 
import random
import operator
#4.1




#4.2 - The stack could overflow. Computer could run out of memory.




#4.3 - There is no return. It should be "return x ** 3"




#4.4 - Iterates through the list squaring each element and then added to y. Once iterated through the list the total of y is returned




#4.5
def seconds_since_midnight(*time_now):
    hour_in_seconds = 60 * 60
    minute_in_seconds = 60
    
    return sum([time_now[0] * hour_in_seconds, time_now[1] * minute_in_seconds, time_now[2]])

# print(seconds_since_midnight(13, 30, 45))




#4.6
def average(num, *args):
    if not args:
        return num 
    
    length = len(args) + 1
    total_sum = sum(args) + num
    return total_sum / length

# print(average(1, 2, 3))




#4.7
def date_and_time():
    print(datetime.datetime.today())

# date_and_time()




#4.8
def round_num(num_float):
    rounding = {
        'integer': 0,
        'tenth': 1,
        'hundredth': 2,
        'thousandth': 3
    }
    
    for rounded, num in rounding.items():
        print(f'To the nearest {rounded}: {round(num_float, num)}')

# round_num(13.56449)




#4.9
def fahrenheit():
    # F = (9 / 5) * celsius + 32

    
    print('Below is a Celsius to Fahrenhiet table that goes for 0 to 100.', end='\n\n')

    # Print the table header
    print('Celsius    Fahrenheit')
    
    # Iterate through a range of 0 - 100
    for celsius in range(0, 101):
        f = (9 / 5) * celsius + 32
        print(f'{celsius:>4}{f:>14.0f}')

# fahrenheit()




#4.10 & 4.11
def guess_the_number():
    # Choose a number between 1 - 1_000 randomly and don't display to the user
    number = random.randint(0, 1_000)
    guesses = 0
    
    while True:
        # User to guess
        user_guess = int(input('Guess my number between 1 and 1000 with the fewest guesses: '))
        guesses += 1
        
        # Check if user_guess is correct
        if user_guess == number:
            print(f'Congratulations. You guessed the number! ({number})')
            
            if guesses <= 10:
                print("Either you know the secret or you got lucky!")
            else:
                print("You should be able to do better!")
            
            # User what to play again?
            play_again = input('Do you want to play again (Y/N): ')
            if play_again in ['Y', 'y', 'Yes', 'YES', 'yes']:
                guess_the_number()
            else:
                break 
            
        elif user_guess > number:
            print('Too high. Try again.', end='\n\n')
            
        elif user_guess < number:
            print('Too low. Try again.', end='\n\n')
        
    print()
    print('Thanks for playing.')

# guess_the_number()




#4.12
# Contenders begin at square 1 of 70

def tortoise():
    """Create a random number between 1 - 10 and return how many squares to move left or right."""
    # Create a random number
    num_gen = random.randint(1, 10)
    
    moves = {
        'Fast plod': [[1, 2, 3, 4, 5], 3],
        'slip': [[6, 7], -6],
        'slow plod': [[8, 9, 10], 1]
    }
    
    for move, find in moves.items():
        if num_gen in find[0]:
            return find[1]


def hare():
    """Create a random number between 1 - 10 and return how many squares to move left or right."""
    # Create a random number
    num_gen = random.randint(1, 10)

    moves = {
        'Sleep': [[1, 2], 0],
        'Big hop': [[3, 4], 9],
        'Big slip': [[5], -12],
        'Small hop': [[6, 7, 8], 1],
        'Small slip': [[9, 10], -2]
    }

    for move, find in moves.items():
        if num_gen in find[0]:
            return find[1]


def main():
    # Count for each animal
    tortoise_count = 1
    hare_count = 1
    
    # Track total iterations of the simulation
    total_lines = 1
    
    # Heading for the start or the race
    print('BANG !!!!!\nAnd THEYRE OFF !!!!!')
    
    # Create a while loop 
    while True:
        # Run both the tortoise and hare functions and += them to each of their counts
        tortoise_count += tortoise()
        hare_count += hare()
        
        # If animals are < 1 assign them 1
        if tortoise_count < 1:
            tortoise_count = 1
        if hare_count < 1:
            hare_count = 1
        
        # If both animals land on the same square display "OUCH!!!"
        if tortoise_count == hare_count:
            print(' ' * hare_count, 'OUCH!!!')
        
        if max(tortoise_count, hare_count) < 70:
            print(' ' * tortoise_count, 'T')
            print(' ' * hare_count, 'H')
            
        # Check if either animal has reached or passed the square 70 and if so display the winner and terminate the simulation
        if tortoise_count >= 70:
            print('TORTOISE WINS!!! YAY!!!')
            print(total_lines)
            break 
        elif hare_count >= 70:
            print('HARE WINS!!! YAY!!!')
            print(total_lines)
            break 
        
        total_lines += 1

# main()




#4.13
def product(lyst):
    total = 1
    
    for num in lyst:
        total *= num 
    
    return total

# print(product([1, 2, 3, 4]))




#4.14
def multiplication_assistant():
    # Generate 2 random numbers between 1 - 9 and store in a tuple
    num1, num2 = random.randint(1, 9), random.randint(1, 9)
    
    # Answer - product of the 2 random numbers
    answer = num1 * num2
    
    # While loop
    while True:
        # User input - "How much is 6 times 7?"
        guess = int(input(f'How much is {num1} times {num2}? '))
        
        # If correct display messge "Very good!" and if they want to play again
        if guess == answer:
            print('Very good!')
            
            play_again = input('Do you want to play again (y or n)? ')
            if play_again in ['Y', 'y']:
                print()
                multiplication_assistant()
            else:
                print('Thanks for playing.')
                break
        # If incorrect display message "No. Please try again."
        else:
            print('No. Please try again.', end='\n\n')

# multiplication_assistant()




#4.15
def multiplication_assistant_2():
    # Generate 2 random numbers between 1 - 9
    num1, num2 = random.randint(1, 9), random.randint(1, 9)

    # Answer is the product of the 2 random numbers
    answer = num1 * num2

    responses = {
        'correct': ['Very good!', 'Nice work!', 'Keep up the good work!'],
        'incorrect': ['No. Please try again.', 'Wrong. Try once more', 'No. Keep trying']
    }
    
    # Keep looping
    while True:
        # User input. Example - "How much is 6 times 7?"
        guess = int(input(f'How much is {num1} times {num2}? '))

        response_num = random.choice([0, 1, 2])
        
        # If correct display message choice and if they want to play again
        if guess == answer:
            print(responses['correct'][response_num])
            
            play_again = input('Do you want to play again (y or n)? ')
            if play_again in ['Y', 'y']:
                print()
                multiplication_assistant_2()
            else:
                print('Thanks for playing.')
                break
        
        # If incorrect display message choice
        else:
            print(responses['incorrect'][response_num], end='\n\n')


# multiplication_assistant_2()




#4.16
def multiplication_assistant_3():
    difficulty = int(input('Enter what difficulty you want (1 or 2): '))
    
    # Generate random numbers
    if difficulty == 1:
        num1, num2 = random.randint(1, 9), random.randint(1, 9)
    else:
        num1, num2 = random.randint(10, 99), random.randint(10, 99)

    # Answer is the product of the 2 random numbers
    answer = num1 * num2

    responses = {
        'correct': ['Very good!', 'Nice work!', 'Keep up the good work!'],
        'incorrect': ['No. Please try again.', 'Wrong. Try once more', 'No. Keep trying']
    }

    # Keep looping
    while True:
        # User input. Example - "How much is 6 times 7?"
        guess = int(input(f'How much is {num1} times {num2}? '))

        response_num = random.choice([0, 1, 2])

        # If correct display message choice and if they want to play again
        if guess == answer:
            print(responses['correct'][response_num])

            play_again = input('Do you want to play again (y or n)? ')
            if play_again in ['Y', 'y']:
                print()
                multiplication_assistant_3()
            else:
                print('Thanks for playing.')
                break

        # If incorrect display message choice
        else:
            print(responses['incorrect'][response_num], end='\n\n')


# multiplication_assistant_3()




#4.17
def multiplication_assistant_4():
    difficulty = int(input('Enter what difficulty you want (1 or 2): '))

    # Generate random numbers
    if difficulty == 1:
        num1, num2 = random.randint(1, 9), random.randint(1, 9)
    else:
        num1, num2 = random.randint(10, 99), random.randint(10, 99)

    # Print the operator selection and user to input choice
    op_selection = int(input('Select a number below:\n1 = +\n2 = -\n3 = *\n4 = /\n5 = random\n:'))

    operator_lookup = ['+', '-', '*', '/']
    
    # First check if operation is random. If so pick 1 - 4 options randomly
    if op_selection == 5:
        op_selection = random.choice([1, 2, 3, 4])
        
    if op_selection == 1:
        answer = num1 + num2 
    elif op_selection == 2:
        answer = num1 - num2
    elif op_selection == 3:
        answer = num1 * num2
    elif op_selection == 4:
        answer = num1 / num2
    
    responses = {
        'correct': ['Very good!', 'Nice work!', 'Keep up the good work!'],
        'incorrect': ['No. Please try again.', 'Wrong. Try once more', 'No. Keep trying']
    }

    # Keep looping
    while True:
        # User input. Example - "How much is 6 times 7?"
        guess = int(input(f'How much is {num1} {operator_lookup[op_selection - 1]} {num2}? '))

        response_num = random.choice([0, 1, 2])

        # If correct display message choice and if they want to play again
        if guess == answer:
            print(responses['correct'][response_num])

            play_again = input('Do you want to play again (y or n)? ')
            if play_again in ['Y', 'y']:
                print()
                multiplication_assistant_4()
            else:
                print('Thanks for playing.')
                break

        # If incorrect display message choice
        else:
            print(responses['incorrect'][response_num], end='\n\n')


# multiplication_assistant_4()




#4.18
