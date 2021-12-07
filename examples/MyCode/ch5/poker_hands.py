import random
import math


def is_pair(hand):
    """Return True if hand has 2 of the same card numbers else False"""
    # Iterate through the hand and store the card numbers in a list
    card_values = [card[0] for card in hand]

    # Iterate through the card numbers and check if there is more than one card of that same number. Return True or False
    for card in card_values:
        if card_values.count(card) > 1:
            return 'Pair'
    return False


def is_two_pair(hand):
    """Return True if hand has 2 occurences of a pair else False"""
    # Iterate through the hand and store the card numbers in a list
    card_values = [card[0] for card in hand]
    
    # Keep count of the number if pairs
    num_true = []
    
    # Store the card numbers that have already returned True as being a pair so we don't count them again when iterating out the list.
    card_pair_numbers = []

    # Iterate through the card numbers and check if there is more than one card of that same number. Return True or False
    for card in card_values:
        if card not in card_pair_numbers:
            if card_values.count(card) > 1:
                card_pair_numbers.append(card)
                num_true.append(True)

    if len(num_true) == 2:
        return 'Two pair'
    return False


def three_of_a_kind(hand):
    """Return true if a hand has 3 of the same card numbers else False"""
    # Iterate through the hand and store the card numbers in a list
    card_values = [card[0] for card in hand]

    # Iterate through card_values and check if the card number occurs 3 times. If so return True else False
    for card in card_values:
        if card_values.count(card) == 3:
            return 'Three of a kind'
    return False


def is_straight(hand):
    """Return True if cards can be arranged in consecutive order else False"""
    # Turn the card words into numbers
    non_number_card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    # Iterate through the hand and return card values into a list
    card_values = [card[0] for card in hand]

    # Create a list to store the card numbers in
    card_numbers = [non_number_card_values[card] for card in card_values]

    # Check the highest and lowest numbers in the hand
    lowest_card, highest_card = min(card_numbers), max(card_numbers)
    
    # Create a comparision list based of the min and max above
    comparision_list = list(range(lowest_card, highest_card + 1))

    # Sort the card_numbers
    card_numbers.sort()

    return 'Straight' if comparision_list == card_numbers else False


def is_flush(hand):
    """Return True if all card are the same suit else False"""
    card_faces = [card[1] for card in hand]
    first_card_face = card_faces[0]

    return 'Flush' if card_faces.count(first_card_face) == 5 else False


def is_full_house(hand):
    """Return True if a hand that contains three cards of one rank and two cards of another rank"""
    # Store card values in a list
    card_values = [card[0] for card in hand]
    check_pair = []

    # Check three_of_a_kind is True and append the remaining two values to check_pair
    if three_of_a_kind(hand):
        for card in card_values:
            if card_values.count(card) != 3:
                check_pair.append(card)

        if check_pair[0] == check_pair[1]:
            return 'Full house'
    else:
        return False


def four_of_a_kind(hand):
    """Return True if the hand has 4 of the same card numbers else False"""
    # Store card values in a list
    card_values = [card[0] for card in hand]

    # Iterate through the card_values and check if a card have the same value 4 times in the hand
    for card in card_values:
        if card_values.count(card) == 4:
            return 'Four of a kind'
    return False


def straight_flush(hand):
    """Return True if hand is a straight with all five cards of the same suit else False"""
    # Iterate through hand and store the suit names in a list
    card_suites = [card[1] for card in hand]

    # Use is_straight() func to confirm if the hand is a straight
    if is_straight(hand) and card_suites.count(card_suites[0]) == 5:
        return 'Straight flush'
    return False
