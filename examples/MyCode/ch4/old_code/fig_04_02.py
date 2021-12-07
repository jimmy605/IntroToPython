# fig_04_02.py
"""Simulating the dice game Craps."""
import random

def sum_two_dice_roll():
    """Roll two dice and return the sum."""
    roll_1 = random.randrange(1, 7)
    roll_2 = random.randrange(1, 7)
    return sum((roll_1, roll_2))


def craps():
    die_hand = sum_two_dice_roll()
    print(f'Dice hand is {die_hand}')
    # if sum is 7 or 11
    if die_hand in [7, 11]:
        # i win
        return f'WON ({die_hand})'
        
    # if sum is 2, 3 or 12
    if die_hand in [2, 3, 12]:
        # i lose
        return f'LOSE ({die_hand})'
    
    # if neither of the above are true 
    sentinel = True
    while sentinel:
        point = die_hand
        # continue to roll till 
        new_die_hand = sum_two_dice_roll()
            # i equal my roll "point". Equal to a value in point list - i win
        if new_die_hand == point:
            # WIN - break
            return f'WON through point system ({new_die_hand})'
        # roll == 7 - i lose
        if new_die_hand == 7:
            # LOSE - break
            return f'LOSE through point system ({new_die_hand})'

print(craps())

for game in range(31):
    print(craps(), end='\n\n')
