import random 
import math 
import poker_hands as p_h 


def initialize_deck():
    """Create a new deck of cards and return them in a list of tuples such as [('Ace', 'Hearts')]"""

    # Types of suites and cards
    suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    card_numbers = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                    'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    # Store the new deck in deck
    deck = []

    # Create each card and append to deck
    for suite in suites:
        for card in card_numbers:
            deck.append((card, suite))

    # Shuffle the deck inplace
    random.shuffle(deck)
    
    # Deal a five-card poker hand as a list of five card tuples
    return deck


def hand():
    """Creates a hand from a deck of cards"""
    deck = initialize_deck()
    
    # Pick 5 random tuples out of the list of deck
    hand = [random.choice(deck) for card in range(5)]
    return hand


def check_hand():
    hand_one = hand()
    """Takes in the hand and returns the best case poker hand possible"""
    # Store all the possible poker hands in a list and iterate through best case first and work way to the bottom. Check hand against each one
    poker_hands = [p_h.straight_flush, p_h.four_of_a_kind, p_h.is_full_house, p_h.is_flush, p_h.is_straight, p_h.is_two_pair, p_h.is_pair]
    
    for i, poker_hand in enumerate(poker_hands):
        result = poker_hand(hand_one)
        if result:
            return result 


# for i in range(1_000_000):
#     check_hand()


def winning_hand(hand_1, hand_2):
    """Check which hand is the winning hand. Return which hand won and the hand they had."""
    
    # Store the hand as {8: 'Pair'} for example. 8 being the lowest hand and {1: 'straight_flush'} being the highest hand you can get
    hands = {1: 'Straight flush', 2: 'Four of a kind', 3: 'Full house', 4: 'Flush', 5: 'Straight', 6:'Three of a kind', 7: 'Two pair', 8: 'Pair'}
    
    hands_output = []
    idx = 0
    
    for hand in [hand_1, hand_2]:
        for position, hand_type in hands.items():
            if hand == hand_type:
                hands_output.append((position, hand, idx))
        idx += 1
    
    # print(hands_output)
    
    # Check which had won
    # If hands_output is empty no one won
    if len(hands_output) < 1:
        return 'No one won this hand!!!'
    
    # If hands_output == 1 idx number hand won
    if len(hands_output) == 1:
        if hands_output[0][2] == 0:
            return 'Hand One won this round!!!'
        else:
            return 'Hand Two won this round!!!'
    
    # If length of hands_ouput == 2 check which has the lowest idx
    if len(hands_output) == 2:
        idx_hand_one = hands_output[0][0]
        idx_hand_two = hands_output[1][0]
        
        if idx_hand_one == idx_hand_two:
            return 'Its a draw guys!!!'
        elif idx_hand_one < idx_hand_two:
            return 'Hand One won this round even though you had a hand!!!'
        elif idx_hand_two < idx_hand_one:
            return 'Hand Two won this round even though you had a hand!!!'


for i in range(100):
    print(winning_hand(check_hand(), check_hand()))