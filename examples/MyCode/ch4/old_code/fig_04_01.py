# fig_04_01.py
"""Roll a six-sided die 6,000,000 times."""
import random

def die_frequency (die_sides, rolls):
    # face frequency counters
    frequency = {str(i + 1): 0 for i in range(die_sides)}

    # roll die 6,000,000 times
    for roll in range(rolls):
        die_num = str(random.randrange(1, die_sides + 1))
        frequency[die_num] += 1

    # Print the header out
    print(f'Face{"Frequency":>13}')
    for die_num, freq in frequency.items():
        print(f'{die_num:>4}{freq:>13}')

die_frequency(6, 6_000_000)