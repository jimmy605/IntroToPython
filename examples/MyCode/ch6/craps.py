# craps.py
"""Simulating the dice game Craps."""
import random 

# Store the results of the games
wins = {}
losses = {}

def dict_update(dict_to_check, die_num):
    if die_num in dict_to_check:
        dict_to_check[die_num] += 1
    else:
        dict_to_check[die_num] = 1


def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


def play_game():
    rolls = 1
    die_values = roll_dice()  # first roll
    # display_dice(die_values)
    
    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11): # win
        game_status = 'WON'
    elif sum_of_dice in (2,3,12): # lose
        game_status = 'LOST'
    else: # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        # print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        rolls += 1
        die_values = roll_dice()
        # display_dice(die_values)
        sum_of_dice = sum(die_values)
        
        if sum_of_dice == my_point: # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7: # lose by rolling 7
            game_status = 'LOST'

    # display "wins" or "loses" message
    if game_status == 'WON':
        return ('WON', rolls)
    else:
        return ('LOST', rolls)


def table_results(num_games, wins, losses):
    """Output a table of the results for the craps game."""
    
    # Use num_games in range to iterate through the number of games to play
    for i in range(num_games):
        result = play_game()
        if result[0] == 'WON':
            dict_update(wins, result[1])
        else:
            dict_update(losses, result[1])
    
    # Data for table and below percentages
    total_rolls = num_games
    wins_percent = round(sum(wins.values()) / total_rolls * 100,2)
    losses_percent = round(sum(losses.values()) / total_rolls * 100, 2)
    
    print(f'Percentage of wins: {wins_percent}%')
    print(f'Percentage of losses: {losses_percent}%')
    print('Percentage of wins/losses based on total number of rolls',end='\n\n')
    
    # Print the header for the table
    print(f'{"% Resolved":>24}{"Cumulative %":>24}')
    print(f'{"Rolls"}{"on this roll":>20}{"of games resolved":>26}')
    
    # Iterate through rolls 1 - 25 and fill out the table for each roll
    cumulative_total = 0
    
    for roll in range(1, 36):
        # Need to confirm that roll number is in the dicts
        wins_key, losses_key = wins.get(roll, 0), losses.get(roll, 0)
        resolved_this_roll = sum([wins_key, losses_key]) / total_rolls * 100
        cumulative_total += resolved_this_roll
        print(f'{roll:>5}{resolved_this_roll:>16.2f}%{cumulative_total:>22.2f}%')

table_results(1_000_000, wins, losses)