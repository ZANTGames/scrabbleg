import random
import string
import os

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line


def deal_hand(n):

    hand = {}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):

    for letter in word:
        if hand[letter] > 0:
            hand[letter] = hand[letter] - 1
        else:
            return False

    return hand